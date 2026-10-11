# -*- coding: utf-8 -*-
"""chartkit - 投資分析報告書(Word 埋め込み用 PNG)のグラフ描画ツールキット

- 出力: PNG、幅 16cm(6.3in)× dpi 200 = 1260px、白背景。高さは図ごとに自動/指定。
- 日本語フォント: IPAGothic(/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf)を明示登録。
- 配色: dataviz スキルの検証済みパレット(blue/orange/aqua)。4本目は無彩色(弱気・その他)。
- 予測値/延長部分は破線・白抜き・薄い色で実績と区別する。
- すべての図の下に「単位 / 期間 / 出所」を小さく注記する。

公開関数
    plot_f13 / plot_f18 / plot_f10 / plot_f7
    plot_scatter_growth_valuation / plot_ranking_bars / plot_rule40 / plot_sbc_vs_eps
共通キーワード引数: unit=, period=, source=, subtitle=, fictional=, height=
使い方は charts/README.md を参照。
"""
from __future__ import annotations

import csv
import json
import math
import os
import re
import sys
import unicodedata
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.font_manager as fm  # noqa: E402
import matplotlib.patheffects as pe  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.legend_handler import HandlerTuple  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch, Rectangle  # noqa: E402
from matplotlib.ticker import FuncFormatter, MaxNLocator  # noqa: E402
from matplotlib.transforms import Bbox  # noqa: E402

__all__ = [
    "plot_f13", "plot_f18", "plot_f10", "plot_f7",
    "plot_scatter_growth_valuation", "plot_ranking_bars", "plot_rule40", "plot_sbc_vs_eps",
    "DEFAULT_SOURCE", "set_default_source",
]

# --------------------------------------------------------------------------------------
# 定数: 寸法・フォント・配色
# --------------------------------------------------------------------------------------
W_IN = 6.3          # 16cm 相当(Word の本文幅)
DPI = 200
MARGIN = 0.12       # 図の左右の余白(in)

FONT_PATH = os.environ.get("CHARTKIT_FONT", "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf")

FS_TITLE = 10.5
FS_SUB = 7.5
FS_LEG = 7.5
FS_TICK = 7.2
FS_LAB = 7.2
FS_SMALL = 6.6
FS_NOTE = 6.6

# dataviz パレット(light)。表面は白(Word 背景に合わせる)
SURFACE = "#ffffff"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
AXIS = "#c3c2b7"
BLUE = "#2a78d6"      # slot1
ORANGE = "#eb6834"    # slot2
AQUA = "#1baf7a"      # slot3
YELLOW = "#eda100"    # slot4(積み上げ棒の隣接のみ。重なる図では使わない)
NEUTRAL = INK2        # 弱気・その他: 無彩色(カテゴリ色の4本目として hue を使わない)
RED = "#e34948"       # 発散配色の負側(ランキング図)
# 状態パレット(エントリーゾーンの淡い地色)
ZONE_GO = "#0ca30c"
ZONE_WARN = "#fab219"
ZONE_STOP = "#898781"

DEFAULT_SOURCE = "出所: 各社決算資料・コンセンサス(TradingView 等)をもとに分析者が算定"


def set_default_source(text: str) -> None:
    """全図の既定の出所注記を差し替える(例: set_default_source('出所: 各社IR、TradingView(2026-10-09取得)'))。"""
    global DEFAULT_SOURCE
    DEFAULT_SOURCE = text


def _register_font() -> str:
    if os.path.exists(FONT_PATH):
        fm.fontManager.addfont(FONT_PATH)
        return fm.FontProperties(fname=FONT_PATH).get_name()
    for cand in ("IPAGothic", "IPAexGothic", "Noto Sans CJK JP", "Noto Sans JP", "TakaoGothic"):
        if any(f.name == cand for f in fm.fontManager.ttflist):
            warnings.warn(f"IPAGothic が見つからないため {cand} で代替します")
            return cand
    raise RuntimeError(f"日本語フォントが見つかりません: {FONT_PATH}")


FONT_NAME = _register_font()
plt.rcParams.update({
    "font.family": FONT_NAME,
    "font.size": FS_TICK,
    "axes.unicode_minus": True,
    "figure.dpi": DPI,
    "savefig.dpi": DPI,
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "text.color": INK,
    "axes.edgecolor": AXIS,
    "axes.labelcolor": INK2,
    "xtick.color": INK2,
    "ytick.color": INK2,
    "axes.linewidth": 0.8,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "xtick.major.size": 2.5,
    "ytick.major.size": 2.5,
    "svg.fonttype": "none",
    "text.parse_math": False,   # $ を含む文字列を数式として解釈させない
})

# 経路ごとの固定スタイル(色は経路=実体に固定。順位や本数で塗り替えない)
PATH_STYLE = {
    "consensus": dict(label="コンセンサス経路", short="コンセンサス", color=BLUE, marker="o"),
    "company": dict(label="会社シナリオ経路", short="会社シナリオ", color=ORANGE, marker="s"),
    "engine": dict(label="事業エンジン経路", short="事業エンジン", color=AQUA, marker="D"),
    "bear": dict(label="弱気経路", short="弱気", color=NEUTRAL, marker="v"),
}
PATH_ALIAS = {
    "コンセンサス": "consensus", "コンセンサス経路": "consensus", "市場": "consensus",
    "会社": "company", "会社シナリオ": "company", "会社シナリオ経路": "company", "経営陣": "company",
    "エンジン": "engine", "事業エンジン": "engine", "事業エンジン経路": "engine",
    "弱気": "bear", "弱気経路": "bear",
}
TARGET_LABEL = {
    "consensus": "コンセンサス目標", "company": "会社シナリオ目標",
    "engine": "事業エンジン目標", "bear": "弱気目標",
}


# --------------------------------------------------------------------------------------
# 入力ヘルパ
# --------------------------------------------------------------------------------------
def _num(x, default=float("nan")) -> float:
    if x is None:
        return default
    if isinstance(x, (int, float, np.integer, np.floating)):
        return float(x)
    s = str(x).strip().replace(",", "")
    if s == "" or s.lower() in ("na", "n/a", "nan", "null", "none", "-", "—", "欠損"):
        return default
    if s.endswith("%"):
        try:
            return float(s[:-1]) / 100.0
        except ValueError:
            return default
    try:
        return float(s)
    except ValueError:
        return default


def _bool(x) -> bool:
    if isinstance(x, (int, float, np.integer, np.floating)):
        return bool(x) and not (isinstance(x, float) and math.isnan(x))
    return str(x).strip().lower() in ("1", "1.0", "true", "t", "yes", "y", "はい", "延長")


def _rows(src) -> list[dict]:
    """CSV パス / dict のリスト / DataFrame を dict のリストにする。"""
    if hasattr(src, "to_dict") and not isinstance(src, (str, Path, list, dict)):
        return src.to_dict("records")
    if isinstance(src, (list, tuple)):
        return [dict(r) for r in src]
    with open(src, encoding="utf-8-sig", newline="") as f:
        return [dict(r) for r in csv.DictReader(f)]


def _need(rows: list[dict], cols: list[str], what: str) -> None:
    if not rows:
        raise ValueError(f"{what}: データが空です")
    missing = [c for c in cols if c not in rows[0]]
    if missing:
        raise ValueError(f"{what}: 必須列がありません {missing}(あり: {list(rows[0].keys())})")


def _get(row: dict, *keys, default=None):
    for k in keys:
        if k in row and row[k] not in (None, ""):
            return row[k]
    return default


def _name(row: dict, name_key="name") -> str:
    return str(_get(row, name_key, "ticker", "name", "label", default="?"))


# --------------------------------------------------------------------------------------
# 書式ヘルパ
# --------------------------------------------------------------------------------------
def _minus(s: str) -> str:
    return s.replace("-", "−")


def _usd(v: float, d: int | None = None) -> str:
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "n/a"
    if d is None:
        d = 0 if (abs(v) >= 100 or abs(v - round(v)) < 1e-9) else (1 if abs(v) >= 10 else 2)
    return _minus(f"${v:,.{d}f}") if v >= 0 else _minus(f"-${abs(v):,.{d}f}")


def _pct(v: float, d: int = 0, sign: bool = False) -> str:
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "n/a"
    s = f"{v * 100:+.{d}f}%" if sign else f"{v * 100:.{d}f}%"
    return _minus(s)


def _fy_label(fy: str) -> str:
    m = re.match(r"^\s*(\d{4})[-/年]?(\d{1,2})(?:[-/月]\d{1,2})?", str(fy))
    if m:
        return f"{m.group(1)}年\n{int(m.group(2))}月期"
    return str(fy)


def _fy_key(fy: str):
    m = re.match(r"^\s*(\d{4})[-/年]?(\d{1,2})", str(fy))
    return (int(m.group(1)), int(m.group(2))) if m else (9999, 0)


def _tw(s: str, fs: float) -> float:
    """文字列の概算幅(pt)。全角=1em、半角=0.55em。複数行は最長行。"""
    best = 0.0
    for line in str(s).split("\n"):
        w = 0.0
        for ch in line:
            w += fs if unicodedata.east_asian_width(ch) in ("W", "F") else fs * 0.56
        best = max(best, w)
    return best


def _wrap(text: str, width_pt: float, fs: float) -> list[str]:
    """日本語向けの幅ベース折り返し(区切り「 ／ 」を優先)。"""
    out: list[str] = []
    for para in str(text).split("\n"):
        parts = re.split(r"(?<=／)", para) if "／" in para else [para]
        cur = ""
        for part in parts:
            if cur and _tw(cur + part, fs) > width_pt:
                out.append(cur.strip("　 "))
                cur = ""
            cur += part
            while _tw(cur, fs) > width_pt:
                # 1文字ずつ詰めて分割
                k = len(cur)
                while k > 1 and _tw(cur[:k], fs) > width_pt:
                    k -= 1
                out.append(cur[:k])
                cur = cur[k:]
        if cur.strip("　 "):
            out.append(cur.strip("　 "))
    return out or [""]


def _lum(hexcolor: str) -> float:
    h = hexcolor.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4  # noqa: E731
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def _text_on(fill: str) -> str:
    """塗りの上の文字色: 白とインクのうちコントラストが高い方。"""
    L = _lum(fill)
    return "#ffffff" if (1.05 / (L + 0.05)) > ((L + 0.05) / 0.0555) else INK


def _tint(hexcolor: str, a: float) -> str:
    h = hexcolor.lstrip("#")
    c = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
    return "#" + "".join(f"{int(round(255 * (1 - a) + v * a)):02x}" for v in c)


def _tick_idx(n: int, step: int) -> list[int]:
    """間引いた目盛の添字。最終期を必ず含める(最後から step 刻み)。"""
    return sorted(range(n - 1, -1, -step))


def _thin_step(labels: list[str], avail_in: float, fs: float) -> int:
    if not labels:
        return 1
    w = max(_tw(s, fs) for s in labels) / 72 + 0.07
    return max(1, int(math.ceil(w * len(labels) / max(avail_in, 0.1))))


# --------------------------------------------------------------------------------------
# キャンバス: タイトル・凡例・注記を配置し、描画領域を返す
# --------------------------------------------------------------------------------------
class _Canvas:
    def __init__(self, height_in: float, title: str, *, subtitle: str | None = None,
                 legend: tuple | None = None, unit=None, period=None, source=None,
                 extra_note=None, fictional: bool = False):
        self.W, self.H = W_IN, float(height_in)
        self.fig = plt.figure(figsize=(self.W, self.H), dpi=DPI, facecolor=SURFACE)
        fig = self.fig
        cur = 0.09
        t_lines = _wrap(title, (self.W - 2 * MARGIN) * 72, FS_TITLE)
        self.title_txt = fig.text(MARGIN / self.W, 1 - cur / self.H, "\n".join(t_lines), fontsize=FS_TITLE,
                                 color=INK, ha="left", va="top", linespacing=1.25,
                                 path_effects=[pe.withStroke(linewidth=0.45, foreground=INK)])
        cur += len(t_lines) * FS_TITLE * 1.3 / 72 + 0.03
        if subtitle:
            s_lines = _wrap(subtitle, (self.W - 2 * MARGIN) * 72, FS_SUB)
            fig.text(MARGIN / self.W, 1 - cur / self.H, "\n".join(s_lines), fontsize=FS_SUB, color=INK2,
                     ha="left", va="top", linespacing=1.35)
            cur += len(s_lines) * FS_SUB * 1.4 / 72 + 0.03
        cur += 0.04
        if legend:
            handles, labels, ncol, hmap = legend
            leg = fig.legend(handles, labels, loc="upper left",
                             bbox_to_anchor=(MARGIN / self.W, 1 - cur / self.H), bbox_transform=fig.transFigure,
                             ncol=ncol, frameon=False, fontsize=FS_LEG, handlelength=2.4, handleheight=1.0,
                             columnspacing=1.3, handletextpad=0.5, borderaxespad=0, borderpad=0,
                             labelspacing=0.45, labelcolor=INK2, handler_map=hmap)
            self.legend = leg
            r = fig.canvas.get_renderer()
            cur += leg.get_window_extent(r).height / DPI + 0.10
        self.top_used = cur

        notes = []
        if unit:
            notes.append("単位: " + unit)
        if period:
            notes.append("期間: " + period)
        if extra_note:
            notes.append(extra_note)
        notes.append(source if source else DEFAULT_SOURCE)
        if fictional:
            notes.append("※架空データ(試験用・実在の数値ではない)")
        note = "　／　".join(notes)
        n_lines = _wrap(note, (self.W - 2 * MARGIN) * 72, FS_NOTE)
        fig.text(MARGIN / self.W, 0.07 / self.H, "\n".join(n_lines), fontsize=FS_NOTE, color=INK2,
                 ha="left", va="bottom", linespacing=1.4)
        self.note_h = len(n_lines) * FS_NOTE * 1.45 / 72
        self.bottom_used = 0.07 + self.note_h + 0.10
        if fictional:
            fig.text(0.5, 0.5, "架空データ", fontsize=46, color=INK, alpha=0.055, rotation=18,
                     ha="center", va="center", zorder=-5)

    # 描画領域(in): 左/右/下は軸ラベルの分を含めた余白
    def region(self, left=0.55, right=0.15, bottom=0.30, top=0.0):
        x0 = left
        y0 = self.bottom_used + bottom
        w = self.W - left - right
        h = self.H - self.top_used - top - y0
        return x0, y0, w, h

    def axes(self, x0, y0, w, h, **kw):
        ax = self.fig.add_axes([x0 / self.W, y0 / self.H, w / self.W, h / self.H], **kw)
        ax.set_facecolor("none")
        return ax

    def save(self, out_png):
        out = Path(out_png)
        out.parent.mkdir(parents=True, exist_ok=True)
        self.fig.savefig(out, dpi=DPI, facecolor=SURFACE)
        plt.close(self.fig)
        try:   # RGBA → RGB に落とし、dpi メタデータ(200)を明示して Word で 16cm 幅に載るようにする
            from PIL import Image
            with Image.open(out) as im:
                im.convert("RGB").save(out, dpi=(DPI, DPI), optimize=True)
        except Exception as e:  # PIL が無くても PNG 自体は出力済み
            warnings.warn(f"PNG の RGB 変換をスキップ: {e}")
        return str(out)


def _style_axes(ax, *, grid="y", spine_left=False, spine_bottom=True):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_visible(spine_left)
    ax.spines["bottom"].set_visible(spine_bottom)
    ax.spines["left"].set_color(AXIS)
    ax.spines["bottom"].set_color(AXIS)
    ax.tick_params(axis="both", labelsize=FS_TICK, labelcolor=INK2, color=AXIS)
    if grid in ("y", "both"):
        ax.yaxis.grid(True, color=GRID, lw=0.6, ls="-")
    if grid in ("x", "both"):
        ax.xaxis.grid(True, color=GRID, lw=0.6, ls="-")
    ax.set_axisbelow(True)


def _unit_label(ax, text, x=0.0, y=1.025, ha="left"):
    """軸の単位を縦軸の上に水平に置く(回転ラベルを避ける)。"""
    ax.text(x, y, text, transform=ax.transAxes, ha=ha, va="bottom", fontsize=FS_SMALL + 0.4, color=INK2)


def _side_labels(ax, ax_w_in, items, fs=FS_LAB):
    """右余白に直接ラベルを置く。衝突時は縦にずらし、細い引き出し線でつなぐ。
    items: dict(y, text, color, marker, origin=('data', x) | ('axis',))"""
    fig = ax.figure
    fig.canvas.draw()
    gap_px = fs * DPI / 72 * 1.45
    ys = [ax.transData.transform((0, it["y"]))[1] for it in items]
    order = sorted(range(len(items)), key=lambda i: ys[i])
    pos = [ys[i] for i in order]
    for k in range(1, len(pos)):
        pos[k] = max(pos[k], pos[k - 1] + gap_px)
    top_lim = ax.transAxes.transform((0, 1.0))[1] + gap_px * 0.4
    over = pos[-1] - top_lim
    if over > 0:
        pos = [p - over for p in pos]
    bot_lim = ax.transAxes.transform((0, 0.0))[1]
    for k in range(len(pos) - 2, -1, -1):
        pos[k] = min(pos[k], pos[k + 1] - gap_px)
    pos = [max(p, bot_lim - gap_px * 0.4) if i == 0 else p for i, p in enumerate(pos)]
    for k in range(1, len(pos)):
        pos[k] = max(pos[k], pos[k - 1] + gap_px)
    mk_dx = 0.075 / ax_w_in
    tx_dx = 0.15 / ax_w_in
    for rank, i in enumerate(order):
        it = items[i]
        y_ax = ax.transAxes.inverted().transform((0, pos[rank]))[1]
        if it.get("marker"):
            ax.plot([1 + mk_dx], [y_ax], transform=ax.transAxes, marker=it["marker"], ms=4.6, ls="none",
                    mfc=it["color"], mec=SURFACE, mew=0.8, clip_on=False, zorder=6)
        ax.text(1 + tx_dx, y_ax, it["text"], transform=ax.transAxes, ha="left", va="center", fontsize=fs,
                color=INK, clip_on=False)
        if it["origin"][0] == "data":
            xy, xyc = (it["origin"][1], it["y"]), "data"
        else:
            xy, xyc = (1.0, it["y"]), ax.get_yaxis_transform()
        end_dx = mk_dx * 0.55 if it.get("marker") else (tx_dx - 0.03 / ax_w_in)
        ax.annotate("", xy=xy, xycoords=xyc, xytext=(1 + end_dx, y_ax), textcoords=ax.transAxes,
                    arrowprops=dict(arrowstyle="-", color=AXIS if it.get("marker") else INK, lw=0.6,
                                    shrinkA=0, shrinkB=2, relpos=(0, 0.5)), annotation_clip=False)


def _style_for_path(p: str) -> tuple[str, dict]:
    key = PATH_ALIAS.get(str(p).strip(), str(p).strip().lower())
    if key not in PATH_STYLE:
        raise ValueError(f"path='{p}' は consensus/company/engine/bear のいずれかにしてください")
    return key, PATH_STYLE[key]


def _grid_legend(row_entries, ncol):
    """行優先で並べたい凡例を、matplotlib の列優先の並びに直す。row_entries: [[(handle,label),...], ...]"""
    blank = (Patch(alpha=0, lw=0), " ")
    nrow = len(row_entries)
    cells = [[(r[c] if c < len(r) else blank) for c in range(ncol)] for r in row_entries]
    flat = [cells[r][c] for c in range(ncol) for r in range(nrow)]
    return [h for h, _ in flat], [l for _, l in flat]


# --------------------------------------------------------------------------------------
# F13: 年度別適正株価パス
# --------------------------------------------------------------------------------------
def plot_f13(csv_path, out_png, title, price_now, *, price_label=None, unit="USD/株",
             period=None, source=None, subtitle=None, fictional=False, height=4.1):
    """年度別適正株価パス。経路ごとに fair_price_low〜high の帯と中央線、現在株価の水平線。
    is_extension=1 の年度は破線・白抜きマーカー・薄い帯(延長部分)。"""
    rows = _rows(csv_path)
    _need(rows, ["fy_end", "path", "fair_price_low", "fair_price_high"], "F13")
    fy_list = sorted({str(r["fy_end"]) for r in rows}, key=_fy_key)
    xi = {fy: i for i, fy in enumerate(fy_list)}
    series: dict[str, list] = {}
    for r in rows:
        key, _ = _style_for_path(r["path"])
        lo, hi = _num(r["fair_price_low"]), _num(r["fair_price_high"])
        if math.isnan(lo) or math.isnan(hi):
            continue
        if lo > hi:
            lo, hi = hi, lo
        series.setdefault(key, []).append((xi[str(r["fy_end"])], lo, hi, _bool(r.get("is_extension", 0))))
    for k in series:
        series[k].sort()
    keys = [k for k in PATH_STYLE if k in series]
    if not keys:
        raise ValueError("F13: 描画できる行がありません")
    has_ext = any(p[3] for k in keys for p in series[k])
    n_x = len(fy_list)

    row1 = []
    for k in keys:
        st = PATH_STYLE[k]
        row1.append(((Patch(facecolor=st["color"], alpha=0.20, lw=0),
                      Line2D([0], [0], color=st["color"], lw=1.6, marker=st["marker"], ms=4.6, mfc=st["color"],
                             mec=SURFACE, mew=0.8)), st["label"]))
    row2 = [((Patch(facecolor=INK2, alpha=0.18, lw=0), Line2D([0], [0], color=INK2, lw=1.0)),
             "帯=許容PEGの幅、線=中央")]
    if has_ext:
        row2.append((Line2D([0], [0], color=INK2, lw=1.4, ls=(0, (3.5, 2)), marker="o", ms=4.6, mfc=SURFACE,
                            mec=INK2, mew=1.0), "破線・白抜き=延長部分"))
    row2.append((Line2D([0], [0], color=INK, lw=1.0), "現在株価"))
    handles, labels = _grid_legend([row1, row2], 4)
    legend = (handles, labels, 4, {tuple: HandlerTuple(ndivide=None)})

    per = period or f"{_fy_label(fy_list[0]).replace(chr(10), '')}〜{_fy_label(fy_list[-1]).replace(chr(10), '')}(各社の会計年度)"
    cv = _Canvas(height, title, subtitle=subtitle, legend=legend,
                 unit=unit + "(適正株価=事業実態EPS×妥当PER、妥当PER=許容PEG×3年EPS成長率)" if unit == "USD/株" else unit,
                 period=per, source=source,
                 extra_note=("延長部分=コンセンサス最終年度より先(事業エンジン経路の考え方で延長)" if has_ext else None),
                 fictional=fictional)
    x0, y0, w, h = cv.region(left=0.55, right=1.30, bottom=0.42, top=0.18)
    ax = cv.axes(x0, y0, w, h)
    _style_axes(ax, grid="y")

    all_lo = [p[1] for k in keys for p in series[k]] + [price_now]
    all_hi = [p[2] for k in keys for p in series[k]] + [price_now]
    ymin, ymax = min(all_lo), max(all_hi)
    pad = (ymax - ymin) * 0.10 + 1e-9
    ax.set_ylim(max(0.0, ymin - pad), ymax + pad)
    ax.set_xlim(-0.35, n_x - 1 + 0.35)
    ax.yaxis.set_major_locator(MaxNLocator(nbins=6, steps=[1, 2, 2.5, 5, 10]))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:,.0f}"))
    step = _thin_step([_fy_label(f) for f in fy_list], w, FS_TICK)
    ti = _tick_idx(n_x, step)
    ax.set_xticks(ti)
    ax.set_xticklabels([_fy_label(fy_list[i]) for i in ti], fontsize=FS_TICK, linespacing=1.25)
    _unit_label(ax, "USD/株")

    # 現在株価
    ax.axhline(price_now, color=INK, lw=1.0, zorder=3)

    for k in keys:
        st, pts = PATH_STYLE[k], series[k]
        c = st["color"]
        for a, b in zip(pts[:-1], pts[1:]):
            ext = b[3]
            ax.fill_between([a[0], b[0]], [a[1], b[1]], [a[2], b[2]], color=c, alpha=0.10 if ext else 0.20,
                            lw=0, zorder=2)
            ax.plot([a[0], b[0]], [(a[1] + a[2]) / 2, (b[1] + b[2]) / 2], color=c, lw=1.6, solid_capstyle="round",
                    ls=(0, (3.5, 2)) if ext else "-", zorder=4)
        if len(pts) == 1:
            ax.vlines(pts[0][0], pts[0][1], pts[0][2], color=c, lw=5, alpha=0.2, zorder=2)
        for (x, lo, hi, ext) in pts:
            mid = (lo + hi) / 2
            if ext:
                ax.plot([x], [mid], marker=st["marker"], ms=4.8, mfc=SURFACE, mec=c, mew=1.1, ls="none", zorder=5)
            else:
                ax.plot([x], [mid], marker=st["marker"], ms=4.8, mfc=c, mec=SURFACE, mew=0.8, ls="none", zorder=5)

    items = [dict(y=(series[k][-1][1] + series[k][-1][2]) / 2,
                  text=f"{PATH_STYLE[k]['short']} {_usd((series[k][-1][1] + series[k][-1][2]) / 2)}",
                  color=PATH_STYLE[k]["color"], marker=PATH_STYLE[k]["marker"],
                  origin=("data", series[k][-1][0])) for k in keys]
    items.append(dict(y=price_now, text=(price_label or f"現在株価 {_usd(price_now)}"), color=INK, marker=None,
                      origin=("axis",)))
    _side_labels(ax, w, items)
    return cv.save(out_png)


# --------------------------------------------------------------------------------------
# F18: 根幹KPIの加速度
# --------------------------------------------------------------------------------------
def plot_f18(csv_path, out_png, title, *, ratio=True, unit="%(前年比・前期比年率)", period=None,
             source=None, subtitle=None, fictional=False, height=None):
    """KPI ごとの小パネル(最大4)。棒=ttm_yoy(前年比)、折れ線=qoq_annualized(前期比年率)。
    ratio=True なら CSV の値は小数(0.25=25%)、False なら既に % 単位。"""
    rows = _rows(csv_path)
    _need(rows, ["kpi", "period", "qoq_annualized", "ttm_yoy"], "F18")
    kpis: list[str] = []
    for r in rows:
        if r["kpi"] not in kpis:
            kpis.append(r["kpi"])
    if len(kpis) > 4:
        warnings.warn(f"F18: KPI が {len(kpis)} 個あります。先頭の4個だけ描きます: {kpis[:4]}")
        kpis = kpis[:4]
    mult = 100.0 if ratio else 1.0
    n = len(kpis)
    ncols = 1 if n == 1 else 2
    nrows = int(math.ceil(n / ncols))
    h = height or (1.50 + 2.0 * nrows)

    handles = [Patch(facecolor=BLUE, lw=0), Line2D([0], [0], color=ORANGE, lw=1.6, marker="o", ms=4.0, mfc=ORANGE,
                                                    mec=SURFACE, mew=0.7)]
    labels = ["前年比(直近12か月 TTM)", "前期比年率(直近四半期を年率換算)"]
    pers = [str(r["period"]) for r in rows]
    cv = _Canvas(h, title, subtitle=subtitle, legend=(handles, labels, 2, {}), unit=unit,
                 period=period or f"{pers[0]}〜{pers[-1]}", source=source,
                 extra_note="パネルごとに縦軸の目盛は異なる(同一パネル内は同一軸)", fictional=fictional)
    x_left, gx = 0.52, 0.52                  # 左の目盛余白、パネル間の横余白
    head_h, foot_h = 0.42, 0.26              # パネル上部の見出し(KPI名+最新値)と下部の目盛ラベルの高さ
    x0, y0, w, hh = cv.region(left=0.0, right=0.0, bottom=0.0, top=0.0)
    pw = (cv.W - x_left - 0.15 - gx * (ncols - 1)) / ncols
    cell_h = hh / nrows
    ph = cell_h - head_h - foot_h
    for idx, kpi in enumerate(kpis):
        r_i, c_i = divmod(idx, ncols)
        px = x_left + c_i * (pw + gx)
        py = y0 + hh - (r_i + 1) * cell_h + foot_h
        ax = cv.axes(px, py, pw, ph)
        _style_axes(ax, grid="y")
        sub = [r for r in rows if r["kpi"] == kpi]
        per_lbl = [str(r["period"]) for r in sub]
        yoy = np.array([_num(r["ttm_yoy"]) * mult for r in sub])
        qoq = np.array([_num(r["qoq_annualized"]) * mult for r in sub])
        xs = np.arange(len(sub))
        bw = min(0.62, 0.30 / (pw / max(len(sub), 1)))
        ax.bar(xs, np.where(np.isnan(yoy), 0, yoy), width=bw, color=BLUE, lw=0, zorder=2)
        ok = ~np.isnan(qoq)
        ax.plot(xs[ok], qoq[ok], color=ORANGE, lw=1.5, marker="o", ms=3.6, mfc=ORANGE, mec=SURFACE, mew=0.6,
                zorder=4, solid_capstyle="round")
        vals = np.concatenate([yoy[~np.isnan(yoy)], qoq[ok], [0]])
        lo, hi = vals.min(), vals.max()
        padv = (hi - lo) * 0.12 + 1e-9
        ax.set_ylim(lo - (padv if lo < 0 else 0), hi + padv)
        ax.set_xlim(-0.6, len(sub) - 0.4)
        ax.yaxis.set_major_locator(MaxNLocator(nbins=4, steps=[1, 2, 2.5, 5, 10]))
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _minus(f"{v:.0f}%")))
        if lo < 0:
            ax.axhline(0, color=INK2, lw=0.7, zorder=3)
        step = _thin_step(per_lbl, pw - 0.2, FS_SMALL)
        ti = _tick_idx(len(sub), step)
        ax.set_xticks(ti)
        ax.set_xticklabels([per_lbl[i] for i in ti], fontsize=FS_SMALL)
        ax.tick_params(axis="x", length=2)
        ax.text(-(x_left - 0.12) / pw, 1 + 0.24 / ph, kpi, transform=ax.transAxes, ha="left", va="bottom",
                fontsize=8.6, color=INK, path_effects=[pe.withStroke(linewidth=0.35, foreground=INK)])
        last = sub[-1]
        sd = _num(last.get("second_diff"))
        parts = [per_lbl[-1] + " "]
        yo = "" if np.isnan(yoy[-1]) else f"前年比 {_minus(f'{yoy[-1]:.1f}%')}"
        qo = f"前期比年率 {_minus(f'{qoq[-1]:.1f}%')}" if ok[-1] else ""
        qo_s = f"年率 {_minus(f'{qoq[-1]:.1f}%')}" if ok[-1] else ""
        ac = ""
        if not math.isnan(sd):
            arrow = "▲" if sd > 0 else ("▼" if sd < 0 else "―")
            ac = f"加速度 {arrow}{_minus(f'{sd * mult:+.1f}')}pt"
        stat = ""
        for q in (qo, qo_s):          # 幅に収まる表記を選ぶ
            stat = "最新 " + per_lbl[-1] + ":" + "|".join(t for t in (yo, q, ac) if t)
            if _tw(stat, FS_SMALL) / 72 <= pw + (x_left - 0.12) - 0.05:
                break
        ax.text(-(x_left - 0.12) / pw, 1 + 0.07 / ph, stat, transform=ax.transAxes, ha="left", va="bottom",
                fontsize=FS_SMALL, color=INK2)
    return cv.save(out_png)


# --------------------------------------------------------------------------------------
# F10: 収益ミックスの時系列
# --------------------------------------------------------------------------------------
def plot_f10(csv_path, out_png, title, *, unit="百万USD", period=None, source=None, subtitle=None,
             fictional=False, height=3.9):
    """積み上げ棒+各期の合計ラベル。収益ラインは最大4(超過分は小さい順に「その他」へ畳む)。
    予測期は薄い色: 列 is_forecast=1、または period が「E」「(予)」で終わる。"""
    rows = _rows(csv_path)
    _need(rows, ["period", "line", "revenue_usd_mn"], "F10")
    periods: list[str] = []
    lines: list[str] = []
    fc_flag: dict[str, bool] = {}
    for r in rows:
        p, ln = str(r["period"]), str(r["line"])
        if p not in periods:
            periods.append(p)
        if ln not in lines:
            lines.append(ln)
        isf = _bool(r.get("is_forecast", 0)) or bool(re.search(r"(E|予|\(予\)|予想)$", p))
        fc_flag[p] = fc_flag.get(p, False) or isf
    data = {ln: {p: 0.0 for p in periods} for ln in lines}
    for r in rows:
        v = _num(r["revenue_usd_mn"], 0.0)
        data[str(r["line"])][str(r["period"])] += 0.0 if math.isnan(v) else v
    folded = None
    if len(lines) > 4:
        tot = {ln: sum(data[ln].values()) for ln in lines}
        keep = sorted(lines, key=lambda s: -tot[s])[:3]
        rest = [ln for ln in lines if ln not in keep]
        data["その他"] = {p: sum(data[ln][p] for ln in rest) for p in periods}
        folded = rest
        lines = [ln for ln in lines if ln in keep] + ["その他"]
    palette = [BLUE, ORANGE, AQUA, YELLOW]
    colors = {}
    for i, ln in enumerate(lines):
        colors[ln] = NEUTRAL if (folded and ln == "その他") else palette[i]
    any_fc = any(fc_flag.values())

    handles = [Patch(facecolor=colors[ln], lw=0) for ln in lines]
    labels = list(lines)
    if any_fc:
        handles.append(Patch(facecolor=_tint(INK2, 0.35), lw=0))
        labels.append("薄い色=予測期")
    note = (f"「その他」は {'・'.join(folded)} の合計" if folded else None)
    cv = _Canvas(height, title, subtitle=subtitle, legend=(handles, labels, min(len(labels), 5), {}), unit=unit,
                 period=period or f"{periods[0]}〜{periods[-1]}", source=source,
                 extra_note=((note + "。" if note else "") + "最終期の帯内の数値は構成比"), fictional=fictional)
    x0, y0, w, h = cv.region(left=0.62, right=0.15, bottom=0.30, top=0.16)
    ax = cv.axes(x0, y0, w, h)
    _style_axes(ax, grid="y")
    n = len(periods)
    slot_in = w / n
    bw = min(0.66, 0.40 / slot_in)
    xs = np.arange(n)
    bottoms = np.zeros(n)
    tot = np.array([sum(data[ln][p] for ln in lines) for p in periods])
    for ln in lines:
        vals = np.array([data[ln][p] for p in periods])
        for i, p in enumerate(periods):
            ax.bar(xs[i], vals[i], bottom=bottoms[i], width=bw, color=colors[ln], lw=1.1, ec=SURFACE,
                   alpha=0.5 if fc_flag[p] else 1.0, zorder=2)
        bottoms += vals
    ymax = tot.max() if len(tot) else 1
    ax.set_ylim(0, ymax * 1.12)
    ax.set_xlim(-0.6, n - 0.4)
    ax.yaxis.set_major_locator(MaxNLocator(nbins=5, steps=[1, 2, 2.5, 5, 10]))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.0f}"))
    step = _thin_step(periods, w, FS_TICK)
    ti = _tick_idx(n, step)
    ax.set_xticks(ti)
    ax.set_xticklabels([periods[i] for i in ti], fontsize=FS_TICK)
    _unit_label(ax, "百万USD")
    # 合計ラベル(多い場合は間引き、最終期は必ず出す)
    lab_step = 1 if _tw("0,000", FS_LAB) / 72 + 0.05 < slot_in else 2
    for i in range(n):
        if (n - 1 - i) % lab_step == 0:
            ax.text(xs[i], tot[i] + ymax * 0.015, f"{tot[i]:,.0f}", ha="center", va="bottom", fontsize=FS_LAB,
                    color=INK)
    # 最終期の構成比(収まるときだけ帯内に置く)
    fig = ax.figure
    fig.canvas.draw()
    last = n - 1
    if tot[last] > 0 and len(lines) > 1:
        base = 0.0
        for ln in lines:
            v = data[ln][periods[last]]
            seg_h_pt = (ax.transData.transform((0, base + v))[1] - ax.transData.transform((0, base))[1]) * 72 / DPI
            txt = f"{v / tot[last] * 100:.0f}%"
            if seg_h_pt >= FS_SMALL * 1.7 and (bw * slot_in * 72) >= _tw(txt, FS_SMALL) + 5:
                fill = _tint(colors[ln], 0.5) if fc_flag[periods[last]] else colors[ln]
                ax.text(xs[last], base + v / 2, txt, ha="center", va="center", fontsize=FS_SMALL,
                        color=_text_on(fill), zorder=5)
            base += v
    return cv.save(out_png)


# --------------------------------------------------------------------------------------
# F7: エントリー価格ゾーン
# --------------------------------------------------------------------------------------
def plot_f7(summary_json_path, out_png, title, *, unit="USD/株", period=None, source=None, subtitle=None,
            fictional=False, price_date=None):
    """summary.json の price / entry_zones(Z1,Z2,zone) / targets_12m(4経路)を使うゾーン図。
    Z1 が null なら即エントリー圏を描かない(Z2 も null ならゾーン帯なし)。"""
    if isinstance(summary_json_path, dict):
        S = summary_json_path
    else:
        with open(summary_json_path, encoding="utf-8") as f:
            S = json.load(f)
    price = _num(S.get("price"))
    if math.isnan(price):
        raise ValueError("F7: summary に price がありません")
    ez = S.get("entry_zones") or {}
    z1, z2 = _num(ez.get("Z1")), _num(ez.get("Z2"))
    if not math.isnan(z1) and not math.isnan(z2) and z1 > z2:
        warnings.warn("F7: Z1 > Z2 のため入れ替えます")
        z1, z2 = z2, z1
    tg = S.get("targets_12m") or {}
    tkeys = [k for k in PATH_STYLE if not math.isnan(_num(tg.get(k)))]
    rows_def = [("price", "現在株価", price)] + [(k, TARGET_LABEL[k], _num(tg[k])) for k in tkeys]
    nrow = len(rows_def)

    vals = [price] + [r[2] for r in rows_def[1:]] + [v for v in (z1, z2) if not math.isnan(v)]
    lo, hi = min(vals), max(vals)
    xmin = max(0.0, lo - (hi - lo) * 0.18 - 1e-9)
    xmax = hi + (hi - lo) * 0.28 + 1e-9
    zones = []   # (name_candidates, x_from, x_to, color)
    if math.isnan(z2):
        zones.append((["エントリー圏の算定なし"], xmin, xmax, ZONE_STOP))
    else:
        if not math.isnan(z1):
            zones.append(([f"即エントリー圏\n{_usd(z1)}以下", f"即エントリー\n{_usd(z1)}以下", f"即\n{_usd(z1)}以下"],
                          xmin, z1, ZONE_GO))
            zones.append(([f"分割エントリー圏\n{_usd(z1)}〜{_usd(z2)}", f"分割エントリー\n{_usd(z1)}〜{_usd(z2)}",
                           f"分割\n{_usd(z1)}〜{_usd(z2)}"], z1, z2, ZONE_WARN))
        else:
            zones.append(([f"分割エントリー圏\n{_usd(z2)}以下", f"分割エントリー\n{_usd(z2)}以下"], xmin, z2, ZONE_WARN))
        zones.append(([f"見送り圏\n{_usd(z2)}超", f"見送り\n{_usd(z2)}超"], z2, xmax, ZONE_STOP))

    cur_zone = ez.get("zone")
    sub = subtitle
    if sub is None:
        bits = []
        if cur_zone:
            bits.append(f"現在の判定: {cur_zone}")
        if math.isnan(z1) and not math.isnan(z2):
            bits.append("Z1 は算定対象外のため即エントリー圏なし")
        sub = "　".join(bits) or None
    strip_h, row_h = 0.52, 0.36
    height = 0.09 + 0.2 + (0.2 if sub else 0) + 0.08 + strip_h + 0.05 + row_h * nrow + 0.50 + 0.5
    pdate = price_date or S.get("price_date")
    cv = _Canvas(height, title, subtitle=sub, unit=unit + "(目標株価は12か月後の水準)", period=period or
                 (f"現在株価は {pdate} 終値、目標株価は評価基準日から12か月後" if pdate else "目標株価は評価基準日から12か月後"),
                 source=source, fictional=fictional)
    x0, y0, w, h = cv.region(left=1.20, right=0.20, bottom=0.50, top=strip_h + 0.05)
    ax = cv.axes(x0, y0, w, h)
    strip = cv.axes(x0, y0 + h + 0.05, w, strip_h)
    for a in (ax, strip):
        a.set_xlim(xmin, xmax)
    _style_axes(ax, grid="none", spine_bottom=True)
    ax.set_ylim(nrow - 0.5, -0.5)
    ax.set_yticks(range(nrow))
    ax.set_yticklabels([r[1] for r in rows_def], fontsize=FS_LAB, color=INK)
    ax.tick_params(axis="y", length=0, pad=6)
    ax.xaxis.set_major_locator(MaxNLocator(nbins=7, steps=[1, 2, 2.5, 5, 10]))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:,.0f}"))
    ax.set_xlabel("株価(USD/株)", fontsize=FS_SMALL + 0.4, color=INK2, labelpad=2)
    strip.set_ylim(0, 1)
    strip.axis("off")
    fig = cv.fig
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    for names, a, b, col in zones:
        ax.axvspan(a, b, color=_tint(col, 0.16), lw=0, zorder=0)
        strip.add_patch(Rectangle((a, 0.0), b - a, 1.0, facecolor=_tint(col, 0.30), lw=0))
        # 帯の左右の境界(白い隙間で区切る)
        strip.add_patch(Rectangle((a, 0.0), (xmax - xmin) * 0.0035, 1.0, facecolor=SURFACE, lw=0))
        zone_w_pt = (strip.transData.transform((b, 0))[0] - strip.transData.transform((a, 0))[0]) * 72 / DPI
        placed = False
        for cand in names:
            for fs in (FS_LAB, FS_SMALL + 0.2, 6.0):
                if _tw(cand, fs) + 6 <= zone_w_pt:
                    strip.text((a + b) / 2, 0.5, cand, ha="center", va="center", fontsize=fs, color=INK,
                               linespacing=1.3)
                    placed = True
                    break
            if placed:
                break
        if not placed:
            strip.text((a + b) / 2, 0.5, names[-1].split("\n")[0][:1], ha="center", va="center",
                       fontsize=FS_SMALL, color=INK)
    for z in (z1, z2):
        if not math.isnan(z):
            ax.axvline(z, color=MUTED, lw=0.6, zorder=1)
    # 行ガイド
    for i in range(nrow):
        ax.plot([xmin, xmax], [i, i], color=_tint(INK2, 0.25), lw=0.6, zorder=1)
    ax.axvline(price, color=INK, lw=1.0, zorder=3)
    span = xmax - xmin
    for i, (k, lab, v) in enumerate(rows_def):
        if k == "price":
            ax.plot([v], [i], marker="o", ms=5.4, mfc=INK, mec=SURFACE, mew=0.9, ls="none", zorder=5)
            txt = _usd(v)
        else:
            st = PATH_STYLE[k]
            ax.plot([v], [i], marker=st["marker"], ms=6.2, mfc=st["color"], mec=SURFACE, mew=0.9, ls="none", zorder=5)
            txt = f"{_usd(v)}  ({_pct(v / price - 1, 0, True)})"
        # ラベルは既定で右。現在株価の縦線をまたぐ/右端を超えるときは反対側に置く
        wd = (_tw(txt, FS_LAB) / 72 / w) * span + span * 0.03
        right = True
        if k != "price":
            crosses_r = v < price < v + wd
            crosses_l = v - wd < price < v
            overflow_r = v + wd > xmax
            if crosses_r or overflow_r:
                right = False
            if not right and crosses_l and not overflow_r:
                right = True
        ax.text(v + (span * 0.018 if right else -span * 0.018), i, txt, ha="left" if right else "right",
                va="center", fontsize=FS_LAB, color=INK, zorder=6)
    return cv.save(out_png)


# --------------------------------------------------------------------------------------
# 横比較: 共通の補助
# --------------------------------------------------------------------------------------
def _place_point_labels(ax, xs, ys, names, fs=FS_LAB, marker_pt=5.0):
    fig = ax.figure
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    pts = ax.transData.transform(np.c_[xs, ys])
    axbb = ax.get_window_extent(r)
    mr = marker_pt * DPI / 72 * 0.75
    placed = [Bbox([[p[0] - mr, p[1] - mr], [p[0] + mr, p[1] + mr]]) for p in pts]
    cands = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    gap = mr + 3
    for p, name in zip(pts, names):
        tmp = ax.text(0, 0, name, fontsize=fs)
        bb = tmp.get_window_extent(r)
        tw, th = bb.width, bb.height
        tmp.remove()
        best, best_score = None, 1e18
        for dx, dy in cands:
            cx = p[0] + dx * (gap + (tw / 2 if dx else 0)) + (0 if dx else 0)
            cy = p[1] + dy * (gap + (th / 2 if dy else 0))
            if dx == 0:
                cx = p[0]
            if dy == 0:
                cy = p[1]
            box = Bbox([[cx - tw / 2, cy - th / 2], [cx + tw / 2, cy + th / 2]])
            score = 0.0
            for q in placed:
                if box.overlaps(q):
                    score += 1000
            if box.x0 < axbb.x0 or box.x1 > axbb.x1 or box.y0 < axbb.y0 or box.y1 > axbb.y1:
                score += 500
            score += (abs(dx) + abs(dy)) * 0.5
            if score < best_score:
                best_score, best = score, (cx, cy, box)
        cx, cy, box = best
        placed.append(box)
        ax.annotate(name, xy=(0, 0), xycoords="figure pixels", xytext=(cx, cy), textcoords="figure pixels",
                    ha="center", va="center", fontsize=fs, color=INK, annotation_clip=False)


# --------------------------------------------------------------------------------------
# 横比較 1: 成長率 × バリュエーション散布図
# --------------------------------------------------------------------------------------
def plot_scatter_growth_valuation(rows, out_png, title, *, y_key="per", x_key="growth", name_key="name",
                                  x_label="成長率(%)", y_label=None, unit=None, period=None, source=None,
                                  subtitle=None, fictional=False, height=3.7, ratio=True):
    """x=成長率、y=PER または PEG(y_key='per'|'peg')、点に銘柄名。
    rows: dict のリスト(name, growth, per, peg)。成長率は ratio=True で小数(0.25=25%)。"""
    rows = _rows(rows)
    _need(rows, [x_key, y_key], "散布図")
    mult = 100.0 if ratio else 1.0
    pts, skipped = [], []
    for r in rows:
        x, y = _num(r[x_key]) * mult, _num(r[y_key])
        if math.isnan(x) or math.isnan(y) or y <= 0:
            skipped.append(_name(r, name_key))
            continue
        pts.append((_name(r, name_key), x, y))
    is_peg = y_key.lower() == "peg"
    y_label = y_label or ("PEG(PER÷成長率)" if is_peg else "PER(倍)")
    note = ("算定不可で非表示: " + "・".join(skipped)) if skipped else None
    cv = _Canvas(height, title, subtitle=subtitle, unit=unit or f"x軸=成長率(%)、y軸={y_label}", period=period,
                 source=source, extra_note=note, fictional=fictional)
    x0, y0, w, h = cv.region(left=0.55, right=0.30, bottom=0.42, top=0.18)
    ax = cv.axes(x0, y0, w, h)
    _style_axes(ax, grid="both")
    xs = np.array([p[1] for p in pts])
    ys = np.array([p[2] for p in pts])
    xmax = max(xs.max() * 1.18, 1) if len(xs) else 1
    ymax = max(ys.max() * 1.18, 1.2 if is_peg else 1) if len(ys) else 1
    ax.set_xlim(min(0, xs.min() * 1.2 if len(xs) and xs.min() < 0 else 0), xmax)
    ax.set_ylim(0, ymax)
    ax.xaxis.set_major_locator(MaxNLocator(nbins=7, steps=[1, 2, 2.5, 5, 10]))
    ax.yaxis.set_major_locator(MaxNLocator(nbins=6, steps=[1, 2, 2.5, 5, 10]))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: _minus(f"{v:.0f}%")))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}" if is_peg else f"{v:.0f}倍"))
    ax.set_xlabel(x_label, fontsize=FS_LAB, color=INK2, labelpad=3)
    _unit_label(ax, y_label)
    if is_peg:
        ax.axhline(1.0, color=INK2, lw=0.8, zorder=2)
        ax.text(ax.get_xlim()[1], 1.0, "PEG=1(割高/割安の目安)", ha="right", va="bottom", fontsize=FS_SMALL,
                color=INK2)
    ax.scatter(xs, ys, s=(5.2 * 2) ** 2 / 1.0, c=BLUE, edgecolors=SURFACE, linewidths=1.2, zorder=4)
    _place_point_labels(ax, xs, ys, [p[0] for p in pts], marker_pt=5.2)
    return cv.save(out_png)


# --------------------------------------------------------------------------------------
# 横比較 2: 期待リターンの横棒
# --------------------------------------------------------------------------------------
def plot_ranking_bars(rows, out_png, title, *, value_key="expected_return", name_key="name",
                      decision_key="decision", unit="% (確率加重の期待株価 ÷ 現在株価 − 1)", period=None,
                      source=None, subtitle=None, fictional=False, height=None):
    """期待リターン(小数)の横棒。降順、0線あり、正=青/負=赤(発散配色)。decision があれば右端に表示。"""
    rows = _rows(rows)
    _need(rows, [value_key], "ランキング")
    items = [(_name(r, name_key), _num(r[value_key]), str(_get(r, decision_key, default="")))
             for r in rows if not math.isnan(_num(r[value_key]))]
    items.sort(key=lambda t: -t[1])
    n = len(items)
    has_dec = any(t[2] for t in items)
    handles = [Patch(facecolor=BLUE, lw=0), Patch(facecolor=RED, lw=0)]
    labels = ["期待リターンがプラス", "期待リターンがマイナス"]
    h = height or (1.35 + 0.36 * n + 0.55)
    cv = _Canvas(h, title, subtitle=subtitle, legend=(handles, labels, 2, {}), unit=unit, period=period,
                 source=source, fictional=fictional)
    x0, y0, w, hh = cv.region(left=0.95, right=0.92 if has_dec else 0.25, bottom=0.30, top=0.0)
    ax = cv.axes(x0, y0, w, hh)
    _style_axes(ax, grid="x", spine_bottom=False)
    ys = np.arange(n)
    vals = np.array([t[1] for t in items]) * 100
    colors = [BLUE if v >= 0 else RED for v in vals]
    bh = min(0.58, 0.20 / (hh / max(n, 1)))
    ax.barh(ys, vals, height=bh, color=colors, lw=0, zorder=2)
    lo, hi = min(vals.min(), 0), max(vals.max(), 0)
    span = (hi - lo) or 1
    ax.set_xlim(lo - span * (0.20 if lo < 0 else 0.02), hi + span * 0.20)
    ax.set_ylim(n - 0.5, -0.5)
    ax.set_yticks(ys)
    ax.set_yticklabels([t[0] for t in items], fontsize=FS_LAB + 0.6, color=INK)
    ax.tick_params(axis="y", length=0, pad=5)
    ax.xaxis.set_major_locator(MaxNLocator(nbins=6, steps=[1, 2, 2.5, 5, 10]))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: _minus(f"{v:+.0f}%") if v else "0%"))
    ax.axvline(0, color=INK2, lw=0.9, zorder=3)
    for i, v in enumerate(vals):
        off = span * 0.015
        ax.text(v + (off if v >= 0 else -off), i, _minus(f"{v:+.1f}%"), ha="left" if v >= 0 else "right",
                va="center", fontsize=FS_LAB, color=INK, zorder=5)
    if has_dec:
        ax.text(1 + 0.18 / w, 1.0 + 0.10 / hh, "最終判断", transform=ax.transAxes, ha="left", va="bottom",
                fontsize=FS_SMALL, color=INK2)
        for i, t in enumerate(items):
            ax.text(1 + 0.18 / w, i, t[2], transform=ax.get_yaxis_transform(), ha="left", va="center",
                    fontsize=FS_LAB, color=INK, clip_on=False)
    return cv.save(out_png)


# --------------------------------------------------------------------------------------
# 横比較 3: Rule of 40
# --------------------------------------------------------------------------------------
def plot_rule40(rows, out_png, title, *, growth_key="revenue_growth", margin_key="fcf_margin", name_key="name",
                unit="%(売上成長率+FCFマージン)", period=None, source=None, subtitle=None, fictional=False,
                height=None):
    """売上成長率+FCFマージンの積み上げ横棒。合計の降順、40%の基準線。値は小数。"""
    rows = _rows(rows)
    _need(rows, [growth_key, margin_key], "Rule of 40")
    items = []
    for r in rows:
        g, m = _num(r[growth_key]) * 100, _num(r[margin_key]) * 100
        if math.isnan(g) or math.isnan(m):
            continue
        items.append((_name(r, name_key), g, m))
    items.sort(key=lambda t: -(t[1] + t[2]))
    n = len(items)
    handles = [Patch(facecolor=BLUE, lw=0), Patch(facecolor=ORANGE, lw=0)]
    labels = ["売上成長率(前年同期比)", "FCFマージン(FCF÷売上)"]
    h = height or (1.35 + 0.40 * n + 0.55)
    cv = _Canvas(h, title, subtitle=subtitle, legend=(handles, labels, 2, {}), unit=unit, period=period,
                 source=source, fictional=fictional)
    x0, y0, w, hh = cv.region(left=0.95, right=0.20, bottom=0.30, top=0.0)
    ax = cv.axes(x0, y0, w, hh)
    _style_axes(ax, grid="x", spine_bottom=False)
    ys = np.arange(n)
    bh = min(0.60, 0.22 / (hh / max(n, 1)))
    tot = np.array([t[1] + t[2] for t in items])
    gmax = max([t[1] for t in items] + [t[1] + t[2] for t in items] + [40])
    lo = min([0] + [t[2] for t in items if t[2] < 0] + [t[1] for t in items if t[1] < 0])
    ax.set_xlim(lo * 1.35 if lo < 0 else 0, gmax * 1.30)
    ax.set_ylim(n - 0.5, -0.5)
    fig = ax.figure
    for i, (nm, g, m) in enumerate(items):
        # 成長率(0 から右)、FCF はその右に積む(負なら 0 から左)
        ax.barh(i, g, height=bh, color=BLUE, lw=1.0, ec=SURFACE, zorder=2)
        if m >= 0:
            ax.barh(i, m, left=max(g, 0), height=bh, color=ORANGE, lw=1.0, ec=SURFACE, zorder=2)
        else:
            ax.barh(i, m, left=0, height=bh, color=ORANGE, lw=1.0, ec=SURFACE, zorder=2)
    ax.set_yticks(ys)
    ax.set_yticklabels([t[0] for t in items], fontsize=FS_LAB + 0.6, color=INK)
    ax.tick_params(axis="y", length=0, pad=5)
    ax.xaxis.set_major_locator(MaxNLocator(nbins=7, steps=[1, 2, 2.5, 5, 10]))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: _minus(f"{v:.0f}%")))
    ax.axvline(0, color=INK2, lw=0.8, zorder=3)
    ax.axvline(40, color=INK, lw=0.9, zorder=3)
    ax.text(40, -0.5 - 0.05 / (hh / n), "基準 40%", ha="center", va="bottom", fontsize=FS_SMALL, color=INK)
    fig.canvas.draw()
    for i, (nm, g, m) in enumerate(items):
        # 帯内ラベル(収まるときだけ)
        for val, left, col in ((g, 0.0, BLUE), (m, max(g, 0.0) if m >= 0 else 0.0, ORANGE)):
            txt = _minus(f"{val:.0f}%")
            wpt = abs(ax.transData.transform((left + val, 0))[0] - ax.transData.transform((left, 0))[0]) * 72 / DPI
            if wpt >= _tw(txt, FS_SMALL) + 6:
                ax.text(left + val / 2, i, txt, ha="center", va="center", fontsize=FS_SMALL, color=_text_on(col),
                        zorder=5)
        end = max(g, 0) + max(m, 0)
        ax.text(end + gmax * 0.012, i, f"合計 {_minus(f'{tot[i]:.0f}%')}", ha="left", va="center", fontsize=FS_LAB,
                color=INK, zorder=6, bbox=dict(boxstyle="square,pad=0.18", fc=SURFACE, ec="none"))
    return cv.save(out_png)


# --------------------------------------------------------------------------------------
# 横比較 4: 調整後EPS vs 事業実態EPS
# --------------------------------------------------------------------------------------
def plot_sbc_vs_eps(rows, out_png, title, *, adj_key="adj_eps", biz_key="business_eps", name_key="name",
                    unit="USD/株(同一年度)", period=None, source=None, subtitle=None, fictional=False,
                    height=3.6):
    """会社定義の調整後EPSと、SBC控除後の事業実態EPSを銘柄ごとに並べた棒。
    銘柄名の下の( )内は 事業実態EPS÷調整後EPS(SBCを引いても残る割合)。"""
    rows = _rows(rows)
    _need(rows, [adj_key, biz_key], "SBC vs EPS")
    items = [(_name(r, name_key), _num(r[adj_key]), _num(r[biz_key])) for r in rows]
    n = len(items)
    handles = [Patch(facecolor=BLUE, lw=0), Patch(facecolor=ORANGE, lw=0)]
    labels = ["調整後EPS(会社定義の non-GAAP、SBC を費用に含めない)", "事業実態EPS(調整後EPS から SBC を税引後で控除)"]
    sub = subtitle or "銘柄名の下の( )内 = 事業実態EPS ÷ 調整後EPS"
    cv = _Canvas(height, title, subtitle=sub, legend=(handles, labels, 1, {}), unit=unit, period=period,
                 source=source, fictional=fictional)
    x0, y0, w, h = cv.region(left=0.55, right=0.15, bottom=0.45, top=0.12)
    ax = cv.axes(x0, y0, w, h)
    _style_axes(ax, grid="y")
    xs = np.arange(n)
    slot_in = w / n
    bw = min(0.36, 0.30 / slot_in)
    adj = np.array([t[1] for t in items])
    biz = np.array([t[2] for t in items])
    ax.bar(xs - bw / 2 - 0.015, np.nan_to_num(adj), width=bw, color=BLUE, lw=0, zorder=2)
    ax.bar(xs + bw / 2 + 0.015, np.nan_to_num(biz), width=bw, color=ORANGE, lw=0, zorder=2)
    allv = np.concatenate([np.nan_to_num(adj), np.nan_to_num(biz), [0]])
    lo, hi = allv.min(), allv.max()
    span = (hi - lo) or 1
    ax.set_ylim(lo - (span * 0.14 if lo < 0 else 0), hi + span * 0.14)
    ax.set_xlim(-0.6, n - 0.4)
    ax.yaxis.set_major_locator(MaxNLocator(nbins=5, steps=[1, 2, 2.5, 5, 10]))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _minus(f"${v:.2f}") if abs(v) < 10 else _minus(f"${v:.0f}")))
    if lo < 0:
        ax.axhline(0, color=INK2, lw=0.8, zorder=3)
        ax.spines["bottom"].set_visible(False)
    ticklabels = []
    for nm, a, b in items:
        ratio = (b / a) if (not math.isnan(a) and not math.isnan(b) and a > 0) else float("nan")
        ticklabels.append(f"{nm}\n({_pct(ratio, 0)})")
    ax.set_xticks(xs)
    ax.set_xticklabels(ticklabels, fontsize=FS_LAB, linespacing=1.35)
    ax.tick_params(axis="x", length=0, pad=4)
    _unit_label(ax, "USD/株")
    off = span * 0.015
    for i in range(n):
        for val, xx in ((adj[i], xs[i] - bw / 2 - 0.015), (biz[i], xs[i] + bw / 2 + 0.015)):
            if math.isnan(val):
                continue
            ax.text(xx, val + (off if val >= 0 else -off), _minus(f"{val:.2f}"), ha="center",
                    va="bottom" if val >= 0 else "top", fontsize=FS_SMALL + 0.2, color=INK, zorder=5)
    return cv.save(out_png)


if __name__ == "__main__":
    print(__doc__)
    print("試験は charts/_test/run_tests.py を実行してください。", file=sys.stderr)
