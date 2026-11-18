#!/usr/bin/env python3
"""
銘柄分析レンズ (lenses.py)

作業フォルダ内の series.json (および valuation.json) を読み込み、
19本のレンズ(L01〜L19)で示唆の種(異常値・構造・逆算・同業線等)を機械的に掘り出し、
lenses.json と lenses.md を出力する。標準ライブラリのみ使用。

使い方:
    py -3 lenses.py <作業フォルダ>
"""

from __future__ import annotations

import json
import math
import os
import re
import statistics
import sys
from pathlib import Path
from typing import Any, Callable


# ---------------------------------------------------------------------------
# 共通ヘルパー
# ---------------------------------------------------------------------------

def strip_help(obj: Any) -> Any:
    """_help で始まるキーを再帰的に取り除く。"""
    if isinstance(obj, dict):
        return {
            k: strip_help(v)
            for k, v in obj.items()
            if not k.startswith("_help")
        }
    if isinstance(obj, list):
        out = []
        for x in obj:
            cleaned = strip_help(x)
            # テンプレート雛形の空要素などを除外しない(そのまま返す)
            out.append(cleaned)
        return out
    return obj


def is_num(v: Any) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def ols(xs: list[float], ys: list[float]) -> tuple[float, float, float, float]:
    """
    単回帰 y = a + b*x と 相関係数 r、決定係数 R^2 を返す。
    戻り値: (a, b, r, r2)
    """
    n = len(xs)
    if n < 2:
        raise ValueError("データ点が2未満です")
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    if sxx == 0:
        raise ValueError("xの分散が0です")
    b = sxy / sxx
    a = my - b * mx
    if syy == 0:
        r = 0.0
        r2 = 0.0
    else:
        r = sxy / math.sqrt(sxx * syy)
        r2 = r * r
    return a, b, r, r2


def rnd(v: float | None, digits: int = 2) -> float | None:
    if v is None or not is_num(v):
        return None
    return round(float(v), digits)


def fmt_num(v: float | None, digits: int = 1, comma: bool = True) -> str:
    if v is None or not is_num(v):
        return "-"
    if digits == 0:
        return f"{round(v):,}" if comma else f"{round(v)}"
    fmt = f",.{digits}f" if comma else f".{digits}f"
    return format(v, fmt)


def make_result(
    lid: str,
    name: str,
    status: str = "ok",
    missing: list[str] | None = None,
    numbers: dict[str, Any] | None = None,
    reads: list[str] | None = None,
    flags: list[dict[str, str]] | None = None,
) -> dict[str, Any]:
    return {
        "id": lid,
        "name": name,
        "status": status,
        "missing": missing or [],
        "numbers": numbers or {},
        "reads": reads or [],
        "flags": flags or [],
    }


def add_flag(
    flags: list[dict[str, str]],
    lid: str,
    text: str,
    question: str,
    check: str,
) -> None:
    fid = f"{lid}-{len(flags) + 1}"
    flags.append({
        "id": fid,
        "text": text,
        "question": question,
        "check": check,
    })


def get_rows_with(rows: list[dict[str, Any]], keys: list[str]) -> list[dict[str, Any]]:
    return [r for r in rows if isinstance(r, dict) and all(is_num(r.get(k)) for k in keys)]


def find_base_scenario(model: list[dict[str, Any]]) -> dict[str, Any] | None:
    if not model:
        return None
    # "基準" または "base" を優先
    candidates = [
        m for m in model
        if isinstance(m, dict) and str(m.get("scenario", "")) in ("基準", "base", "Base")
    ]
    if candidates:
        return candidates[-1]
    return model[-1]


def find_first_last_annual_with(
    annual: list[dict[str, Any]], keys: list[str]
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    valid = get_rows_with(annual, keys)
    if not valid:
        return None, None
    return valid[0], valid[-1]


# ---------------------------------------------------------------------------
# L01 〜 L17 レンズ実装
# ---------------------------------------------------------------------------

def lens_l01(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L01", "利益の増減"
    bridge = data.get("bridge") or {}
    items = bridge.get("items") if isinstance(bridge, dict) else None
    annual = data.get("annual") or []

    has_bridge = isinstance(items, dict) and any(is_num(v) for v in items.values())
    ann_2 = get_rows_with(annual, ["revenue", "gross", "sga", "op"])

    if not has_bridge and len(ann_2) < 2:
        missing = []
        if not has_bridge:
            missing.append("bridge.items")
        if len(ann_2) < 2:
            missing.append("annual(直近2期のrevenue,gross,sga,op)")
        return make_result(lid, name, status="入力不足", missing=missing)

    numbers: dict[str, Any] = {}
    reads: list[str] = []
    flags: list[dict[str, str]] = []

    top_item_name: str | None = None
    if has_bridge:
        clean_items = {k: float(v) for k, v in items.items() if is_num(v)}
        pos_items = {k: v for k, v in clean_items.items() if v > 0}
        pos_total = sum(pos_items.values())
        net_change = sum(clean_items.values())
        max_pos_name, max_pos_val = (
            max(pos_items.items(), key=lambda kv: kv[1]) if pos_items else (None, 0.0)
        )
        max_abs_name, max_abs_val = max(clean_items.items(), key=lambda kv: abs(kv[1]))
        share_pct = (max_pos_val / pos_total * 100.0) if (max_pos_name and pos_total > 0) else None
        top_item_name = max_pos_name or max_abs_name

        numbers["bridge_label"] = bridge.get("label", "")
        numbers["bridge_items"] = clean_items
        numbers["bridge_net_change"] = rnd(net_change, 1)
        numbers["bridge_pos_total"] = rnd(pos_total, 1)
        numbers["max_positive_item"] = max_pos_name
        numbers["max_positive_value"] = rnd(max_pos_val, 1)
        numbers["max_positive_share_pct"] = rnd(share_pct, 1)
        numbers["max_abs_item"] = max_abs_name
        numbers["max_abs_value"] = rnd(max_abs_val, 1)

        reads.append(
            f"会社増減({bridge.get('label', '')})の正の要因合計は+{fmt_num(pos_total, 0)}、純増減は{net_change:+,.0f}。"
            + (
                f"最大の増益要因は「{max_pos_name}」(+{fmt_num(max_pos_val, 0)}、正の寄与の{fmt_num(share_pct, 1)}%)。"
                if max_pos_name and share_pct is not None
                else ""
            )
            + (
                f"絶対値最大の項目は「{max_abs_name}」({max_abs_val:+,.0f})。"
                if max_abs_name and max_abs_name != max_pos_name
                else ""
            )
        )

        # 価格と原料の差し引き(スプレッド)で主因を見直す
        price_keys = [k for k in clean_items if any(w in k for w in ("価格", "単価", "値上げ", "構成", "ミックス"))]
        raw_keys = [k for k in clean_items if any(w in k for w in ("原料", "原材料", "仕入", "燃料", "エネルギー"))]
        qty_keys = [k for k in clean_items if any(w in k for w in ("数量", "販売量", "物量"))]
        if price_keys and raw_keys:
            price_sum = sum(clean_items[k] for k in price_keys)
            raw_sum = sum(clean_items[k] for k in raw_keys)
            qty_sum = sum(clean_items[k] for k in qty_keys) if qty_keys else None
            spread = price_sum + raw_sum
            recover = (price_sum / abs(raw_sum) * 100.0) if raw_sum < 0 else None
            numbers["spread_net"] = rnd(spread, 1)
            numbers["raw_recovery_pct"] = rnd(recover, 1)
            numbers["volume_effect"] = rnd(qty_sum, 1) if qty_sum is not None else None
            txt = f"価格・構成({price_sum:+,.0f})と原料({raw_sum:+,.0f})を差し引くとスプレッドは{spread:+,.0f}"
            if recover is not None:
                txt += f"(原料高の取り返し率 {recover:.0f}%)"
            if qty_sum is not None:
                txt += f"。数量は{qty_sum:+,.0f}"
                if qty_sum > max(spread, 0):
                    top_item_name = qty_keys[0]
                    numbers["max_positive_item"] = "数量(価格と原料の差し引き後)"
                    numbers["max_positive_share_pct"] = rnd(qty_sum / (qty_sum + max(spread, 0)) * 100.0, 1)
                    txt += "で、差し引き後の実質の主因は数量"
                elif spread > 0:
                    txt += "で、差し引き後の実質の主因はスプレッドの拡大(値上げが原料高を上回った)"
            reads.append(txt + "。")

    # 通期直近2期での売上・OP変動率および恒等式分解も計算(あれば)
    rev_chg_pct = None
    op_chg_pct = None
    decomp_top = None
    if len(ann_2) >= 2:
        prev, curr = ann_2[-2], ann_2[-1]
        d_rev = curr["revenue"] - prev["revenue"]
        d_op = curr["op"] - prev["op"]
        gm_prev = prev["gross"] / prev["revenue"]
        gm_curr = curr["gross"] / curr["revenue"]
        d_gm = gm_curr - gm_prev
        d_sga = curr["sga"] - prev["sga"]

        vol_eff = d_rev * gm_prev
        margin_eff = d_gm * curr["revenue"]
        sga_eff = -d_sga

        rev_chg_pct = (d_rev / prev["revenue"] * 100.0) if prev["revenue"] else None
        op_chg_pct = (d_op / abs(prev["op"]) * 100.0) if prev["op"] else None

        decomp = {"売上高変化(数量等)": vol_eff, "粗利率変化(価格・構成等)": margin_eff, "販管費増減": sga_eff}
        decomp_pos = {k: v for k, v in decomp.items() if v > 0}
        decomp_pos_sum = sum(decomp_pos.values())
        if decomp_pos:
            decomp_top = max(decomp_pos.items(), key=lambda kv: kv[1])[0]

        numbers["annual_pair"] = f"{prev.get('fy')}→{curr.get('fy')}"
        numbers["annual_rev_chg_pct"] = rnd(rev_chg_pct, 2)
        numbers["annual_op_chg_pct"] = rnd(op_chg_pct, 2)
        numbers["decomp_delta_op"] = rnd(d_op, 1)
        numbers["decomp_volume_effect"] = rnd(vol_eff, 1)
        numbers["decomp_margin_effect"] = rnd(margin_eff, 1)
        numbers["decomp_sga_effect"] = rnd(sga_eff, 1)
        if not has_bridge and decomp_pos_sum > 0 and decomp_top:
            numbers["max_positive_item"] = decomp_top
            numbers["max_positive_share_pct"] = rnd(decomp_pos[decomp_top] / decomp_pos_sum * 100.0, 1)

        reads.append(
            f"通期直近({prev.get('fy')}→{curr.get('fy')})は売上{rev_chg_pct:+.1f}%・営業利益{op_chg_pct:+.1f}%({d_op:+,.0f})。"
            f"粗利・販管費分解では 売上変化×前期粗利率={vol_eff:+,.0f}、粗利率変化×当期売上={margin_eff:+,.0f}、−Δ販管費={sga_eff:+,.0f}。"
        )

    # 旗判定 1: 売上の増減が±5%以内なのに営業利益が±20%超動いた
    if is_num(rev_chg_pct) and is_num(op_chg_pct):
        if abs(rev_chg_pct) <= 5.0 and abs(op_chg_pct) > 20.0:
            add_flag(
                flags,
                lid,
                f"売上増減{rev_chg_pct:+.1f}%(±5%以内)に対し営業利益が{op_chg_pct:+.1f}%(±20%超)と大きく変動",
                "なぜ売上がほぼ横ばいなのに対営業利益がここまで大きく動いたのか(値上げ・構成変化か一過性要因か)？",
                "決算説明資料の営業利益増減要因分析と製品別の単価・数量・在庫評価影響の記述",
            )

    # 旗判定 2: 最大項目が「価格」ではなく「数量」(またはその逆)
    driver = top_item_name or decomp_top
    if driver:
        is_price = ("価格" in driver) or ("粗利率" in driver) or ("単価" in driver)
        is_qty = ("数量" in driver) or ("売上変化" in driver)
        if is_price:
            add_flag(
                flags,
                lid,
                f"増益の最大項目が「数量」ではなく「{driver}」(シェア{fmt_num(numbers.get('max_positive_share_pct'), 1)}%)",
                f"なぜ増益の主役が数量ではなく「{driver}」なのか？値上げ・構成改善は今後も持続するか？",
                "会社の利益の増減分析と品目別の値上げ浸透・プロダクトミックスに関する記述",
            )
        elif is_qty:
            add_flag(
                flags,
                lid,
                f"増益の最大項目が「価格」ではなく「{driver}」(シェア{fmt_num(numbers.get('max_positive_share_pct'), 1)}%)",
                f"なぜ増益の主役が価格ではなく「{driver}」なのか？稼働率・需要の持続性はどの程度か？",
                "会社の利益の増減分析と品目別の販売数量・稼働率推移の記述",
            )

    return make_result(lid, name, status="ok", numbers=numbers, reads=reads, flags=flags)


def lens_l02(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L02", "加速度"
    periods = data.get("periods") or {}
    per_year = periods.get("per_year") if isinstance(periods, dict) else None
    rows = periods.get("rows") if isinstance(periods, dict) else None

    if not isinstance(per_year, int) or per_year <= 0 or not isinstance(rows, list):
        return make_result(lid, name, status="入力不足", missing=["periods.per_year", "periods.rows"])

    valid_rows = [r for r in rows if isinstance(r, dict) and is_num(r.get("revenue")) and r.get("revenue", 0) > 0 and is_num(r.get("op"))]
    if len(valid_rows) <= per_year:
        return make_result(
            lid, name, status="入力不足",
            missing=[f"periods.rows(前年同期比較には最低{per_year + 1}期必要、現在{len(valid_rows)}期)"]
        )

    opm_list = [r["op"] / r["revenue"] * 100.0 for r in valid_rows]
    gm_list = [
        (r["gross"] / r["revenue"] * 100.0 if is_num(r.get("gross")) else None)
        for r in valid_rows
    ]

    opm_yoy = [opm_list[i] - opm_list[i - per_year] for i in range(per_year, len(valid_rows))]
    gm_yoy = []
    for i in range(per_year, len(valid_rows)):
        if gm_list[i] is not None and gm_list[i - per_year] is not None:
            gm_yoy.append(gm_list[i] - gm_list[i - per_year])
        else:
            gm_yoy.append(None)

    def count_streak(diffs: list[float]) -> tuple[int, str]:
        if not diffs:
            return 0, "不明"
        last = diffs[-1]
        if last > 0:
            s = 0
            for d in reversed(diffs):
                if d > 0:
                    s += 1
                else:
                    break
            return s, "改善"
        elif last < 0:
            s = 0
            for d in reversed(diffs):
                if d < 0:
                    s += 1
                else:
                    break
            return s, "悪化"
        return 0, "横ばい"

    opm_streak, opm_dir = count_streak(opm_yoy)
    gm_valid_yoy = [d for d in gm_yoy if d is not None]
    gm_streak, gm_dir = count_streak(gm_valid_yoy)

    # 2階差分 (前年同期比の前回からの加速、または期毎変化の2階差分)
    opm_second_diff_yoy = (opm_yoy[-1] - opm_yoy[-2]) if len(opm_yoy) >= 2 else None
    opm_second_diff_seq = (
        (opm_list[-1] - opm_list[-2]) - (opm_list[-2] - opm_list[-3])
        if len(opm_list) >= 3
        else None
    )
    gm_second_diff_yoy = (gm_valid_yoy[-1] - gm_valid_yoy[-2]) if len(gm_valid_yoy) >= 2 else None

    numbers = {
        "latest_period": valid_rows[-1].get("p"),
        "latest_opm_pct": rnd(opm_list[-1], 2),
        "latest_opm_yoy_pt": rnd(opm_yoy[-1], 2),
        "opm_yoy_streak": opm_streak,
        "opm_yoy_direction": opm_dir,
        "opm_second_diff_yoy_pt": rnd(opm_second_diff_yoy, 2),
        "opm_second_diff_seq_pt": rnd(opm_second_diff_seq, 2),
        "latest_gm_pct": rnd(gm_list[-1], 2) if gm_list[-1] is not None else None,
        "latest_gm_yoy_pt": rnd(gm_yoy[-1], 2) if gm_yoy[-1] is not None else None,
        "gm_yoy_streak": gm_streak if gm_valid_yoy else None,
        "gm_yoy_direction": gm_dir if gm_valid_yoy else None,
        "gm_second_diff_yoy_pt": rnd(gm_second_diff_yoy, 2),
    }

    reads = [
        f"直近期({valid_rows[-1].get('p')})の営業利益率は{fmt_num(opm_list[-1], 2)}%(前年同期比{opm_yoy[-1]:+.2f}pt、{opm_streak}期連続{opm_dir})。"
        + (f"粗利率は{fmt_num(gm_list[-1], 2)}%(前年同期比{gm_yoy[-1]:+.2f}pt、{gm_streak}期連続{gm_dir})。" if gm_yoy[-1] is not None else "")
        + (f"営業利益率の前期比2階差分は{opm_second_diff_seq:+.2f}pt。" if opm_second_diff_seq is not None else "")
        + (f"前年同期比ベースの2階差分は比較期数が1期のみのため未算出。" if opm_second_diff_yoy is None else f"前年同期比の2階差分は{opm_second_diff_yoy:+.2f}pt。")
    ]

    flags: list[dict[str, str]] = []
    if opm_streak >= 3:
        add_flag(
            flags, lid,
            f"営業利益率の前年同期比が{opm_streak}期連続で{opm_dir}",
            f"なぜ営業利益率の{opm_dir}が{opm_streak}期も続いているのか(構造的変化か循環サイクルか)？",
            "四半期/半期別の粗利率・販管費率推移と価格改定・稼働率のコメント",
        )
    if len(opm_yoy) >= 2 and opm_yoy[-2] > 0 and opm_yoy[-1] < 0:
        add_flag(
            flags, lid,
            f"営業利益率の前年同期比が改善({opm_yoy[-2]:+.2f}pt)から悪化({opm_yoy[-1]:+.2f}pt)へ反転",
            "なぜ利益率モメンタムが改善から悪化に転じたのか(一時的費用か競争激化か)？",
            "直近四半期短信・説明資料の原価率変動要因と一過性費用の注記",
        )
    if gm_valid_yoy and gm_streak >= 3:
        add_flag(
            flags, lid,
            f"粗利率の前年同期比が{gm_streak}期連続で{gm_dir}",
            f"なぜ粗利率の{gm_dir}が{gm_streak}期連続で起きているのか？",
            "原料価格・売価スプレッドと製品ミックスの四半期推移",
        )
    if len(gm_valid_yoy) >= 2 and gm_valid_yoy[-2] > 0 and gm_valid_yoy[-1] < 0:
        add_flag(
            flags, lid,
            f"粗利率の前年同期比が改善({gm_valid_yoy[-2]:+.2f}pt)から悪化({gm_valid_yoy[-1]:+.2f}pt)へ反転",
            "なぜ粗利率が改善から悪化へ反転したのか？",
            "足元の原料市況と値上げ・価格転嫁のタイムラグの記載",
        )

    return make_result(lid, name, status="ok", numbers=numbers, reads=reads, flags=flags)


def lens_l03(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L03", "限界利益率と損益分岐点"
    annual = data.get("annual") or []
    rows = get_rows_with(annual, ["revenue", "op"])
    if len(rows) < 3:
        return make_result(lid, name, status="入力不足", missing=["annual(3期以上のrevenue,op)"])

    xs = [float(r["revenue"]) for r in rows]
    ys = [float(r["op"]) for r in rows]
    a_intercept, slope, _r, r2 = ols(xs, ys)
    # 営業利益 = slope * 売上 - F => F = -a_intercept
    marginal_margin = slope * 100.0
    fixed_cost = -a_intercept
    latest_rev = xs[-1]

    bep_rev = (fixed_cost / slope) if (slope > 0 and fixed_cost > 0 and r2 >= 0.3) else None
    mos_pct = ((latest_rev - bep_rev) / latest_rev * 100.0) if (bep_rev is not None and latest_rev > 0) else None

    numbers = {
        "n_years": len(rows),
        "marginal_margin_pct": rnd(marginal_margin, 2),
        "fixed_cost": rnd(fixed_cost, 1),
        "r2": rnd(r2, 4),
        "latest_revenue": rnd(latest_rev, 1),
        "breakeven_revenue": rnd(bep_rev, 1),
        "margin_of_safety_pct": rnd(mos_pct, 2),
    }

    bep_txt = f"{fmt_num(bep_rev, 0)}、安全余裕率{fmt_num(mos_pct, 1)}%" if bep_rev is not None else "回帰が当てはまらないため出さない"
    fc_sign = f"− {fixed_cost:,.0f}" if fixed_cost >= 0 else f"+ {abs(fixed_cost):,.0f}"
    reads = [
        f"過去{len(rows)}期の回帰(営業利益 = {slope*100:.2f}%×売上 {fc_sign})のR²は{r2:.3f}。"
        f"見かけの限界利益率は{marginal_margin:.1f}%、損益分岐点売上は{bep_txt}。"
    ]
    if r2 < 0.3:
        reads.append(f"R²={r2:.3f} (<0.3) であり、利益は売上の増減(数量)では説明できず、市況スプレッドや製品構成で決まっている。")

    flags: list[dict[str, str]] = []
    if r2 < 0.3:
        add_flag(
            flags, lid,
            f"売上と営業利益の回帰R²が{r2:.3f}(<0.3)と低く、利益は売上の量で説明できない",
            "なぜ売上高の増減で営業利益が説明できないのか(原料市況・単価連動かミックス変化か)？",
            "有価証券報告書のセグメント・主要製品別売上と原料市況・粗利率の長期推移",
        )
    if mos_pct is not None and mos_pct < 15.0:
        add_flag(
            flags, lid,
            f"損益分岐点に基づく安全余裕率が{mos_pct:.1f}%(<15%)と低い",
            "なぜ損益分岐点に対する余裕が乏しいのか(固定費の重さか直近の低採算か)？",
            "有価証券報告書の労務費・減価償却費の内訳と稼働率・固定費削減計画",
        )

    return make_result(lid, name, status="ok", numbers=numbers, reads=reads, flags=flags)


def lens_l04(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L04", "外部要因と自然実験"
    annual = data.get("annual") or []
    rows = [r for r in get_rows_with(annual, ["revenue", "gross", "input_price"]) if r["revenue"] > 0]
    if len(rows) < 4:
        return make_result(lid, name, status="入力不足", missing=["annual(4期以上のrevenue,gross,input_price)"])

    inp_name = str(data.get("input_price_name") or "").strip() or "外部要因"

    # 各年の粗利率(%)と外部要因(input_price)
    gms = [round(r["gross"] / r["revenue"] * 100.0, 2) for r in rows]
    prices = [float(r["input_price"]) for r in rows]
    a, b, r_corr, r2 = ols(prices, gms)

    preds = [a + b * p for p in prices]
    residuals = [gm - pred for gm, pred in zip(gms, preds)]
    n = len(residuals)
    sigma_pop = math.sqrt(sum(e * e for e in residuals) / n)
    sigma_sample = math.sqrt(sum(e * e for e in residuals) / (n - 2)) if n > 2 else sigma_pop
    sigma = sigma_pop

    # 外部要因の前年比が最大だった年(annual 内)
    max_yoy_idx = None
    max_yoy_pct = -1.0
    for i in range(1, len(rows)):
        if prices[i - 1] > 0:
            yoy = (prices[i] - prices[i - 1]) / prices[i - 1] * 100.0
            if abs(yoy) > max_yoy_pct:
                max_yoy_pct = abs(yoy)
                max_yoy_idx = i
    max_shock_fy = rows[max_yoy_idx].get("fy") if max_yoy_idx is not None else None
    max_shock_input_yoy = (
        (prices[max_yoy_idx] - prices[max_yoy_idx - 1]) / prices[max_yoy_idx - 1] * 100.0
        if max_yoy_idx is not None else None
    )
    max_shock_gm_chg = (
        gms[max_yoy_idx] - gms[max_yoy_idx - 1]
        if max_yoy_idx is not None else None
    )

    # 直近期: guidance.ytd に input_price と revenue, gross があればそれを使用
    guidance = data.get("guidance") or {}
    ytd = guidance.get("ytd") if isinstance(guidance, dict) else None
    use_ytd = (
        isinstance(ytd, dict)
        and is_num(ytd.get("input_price"))
        and is_num(ytd.get("revenue"))
        and ytd.get("revenue", 0) > 0
        and is_num(ytd.get("gross"))
    )
    if use_ytd:
        latest_label = f"FY{guidance.get('fy', '')}累計" if guidance.get("fy") else "進行期累計"
        latest_gm = round(ytd["gross"] / ytd["revenue"] * 100.0, 2)
        latest_input = float(ytd["input_price"])
        latest_input_yoy = (latest_input - prices[-1]) / prices[-1] * 100.0 if prices[-1] > 0 else None
        latest_gm_chg = latest_gm - gms[-1]
    else:
        latest_label = str(rows[-1].get("fy", "直近期"))
        latest_gm = gms[-1]
        latest_input = prices[-1]
        latest_input_yoy = (prices[-1] - prices[-2]) / prices[-2] * 100.0 if len(prices) >= 2 and prices[-2] > 0 else None
        latest_gm_chg = (gms[-1] - gms[-2]) if len(gms) >= 2 else None

    latest_pred = a + b * latest_input
    latest_res = latest_gm - latest_pred
    latest_z = (latest_res / sigma) if sigma > 0 else 0.0
    latest_z_sample = (latest_res / sigma_sample) if sigma_sample > 0 else 0.0

    numbers = {
        "input_price_name": inp_name,
        "n_years": n,
        "corr": rnd(r_corr, 4),
        "r2": rnd(r2, 4),
        "reg_intercept": rnd(a, 3),
        "reg_slope_per_10k": rnd(b * 10000.0, 3),
        "residual_sigma_pt": rnd(sigma, 2),
        "residual_sigma_sample_pt": rnd(sigma_sample, 2),
        "max_input_yoy_fy": max_shock_fy,
        "max_input_yoy_pct": rnd(max_shock_input_yoy, 1),
        "max_shock_gm_delta_pt": rnd(max_shock_gm_chg, 2),
        "latest_label": latest_label,
        "latest_input_price": rnd(latest_input, 2),
        "latest_actual_gm_pct": rnd(latest_gm, 2),
        "latest_pred_gm_pct": rnd(latest_pred, 2),
        "latest_residual_pt": rnd(latest_res, 2),
        "latest_residual_sigma": rnd(latest_z, 2),
        "latest_residual_sigma_sample": rnd(latest_z_sample, 2),
        "latest_input_vs_prev_pct": rnd(latest_input_yoy, 1),
        "latest_gm_delta_pt": rnd(latest_gm_chg, 2),
    }

    slope_txt = (
        f"{b*10000:+.3f}pt/1万単位"
        if max(abs(p) for p in prices) >= 1000
        else f"{b:+.4f}pt/1単位"
    )
    inp_val_str = (
        f"{latest_input:,.0f}"
        if (abs(latest_input) >= 1000 and float(latest_input).is_integer())
        else f"{latest_input:,.2f}".rstrip("0").rstrip(".")
    )
    inp_yoy_str = f"{latest_input_yoy:+.1f}%" if latest_input_yoy is not None else "-"
    gm_chg_str = f"{latest_gm_chg:+.2f}pt" if latest_gm_chg is not None else "-"

    reads = [
        f"過去{n}期の粗利率と{inp_name}の相関係数は{r_corr:.2f}(回帰予測式: 粗利率={a:.2f}%{slope_txt}、残差σ={sigma:.2f}pt)。",
        f"{inp_name}前年比が最大だったのは{max_shock_fy}年({max_shock_input_yoy:+.1f}%)で、粗利率変化は{max_shock_gm_chg:+.2f}pt。"
        if max_shock_fy is not None else "",
        f"直近({latest_label}、{inp_name} {inp_val_str})の実績粗利率{latest_gm:.2f}%は回帰予測{latest_pred:.2f}%に対し"
        f"{latest_res:+.2f}pt({latest_z:+.2f}σ、対直近通期 {inp_name}{inp_yoy_str}・粗利率{gm_chg_str})。",
    ]
    reads = [r for r in reads if r]

    flags: list[dict[str, str]] = []
    if abs(r_corr) >= 0.5 and abs(latest_z) > 1.5:
        dir_word = "上振れ" if latest_res >= 0 else "下振れ"
        add_flag(
            flags, lid,
            f"相関係数{r_corr:.2f}の{inp_name}連動式に対し直近({latest_label})残差が{latest_res:+.2f}pt({latest_z:+.2f}σ > 1.5σ)",
            f"なぜ過去の{inp_name}連動(相関{r_corr:.2f})から外れて粗利率が{latest_res:+.2f}pt{dir_word}(乖離)したのか？値上げ等の体質変化かタイムラグ等の一時要因か？",
            f"{inp_name}の推移と値上げ発表日・契約条件・タイムラグ要因の開示",
        )

    return make_result(lid, name, status="ok", numbers=numbers, reads=reads, flags=flags)


def lens_l05(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L05", "会社予想の逆算"
    g = data.get("guidance")
    if not isinstance(g, dict):
        return make_result(lid, name, status="入力不足", missing=["guidance"])
    ytd = g.get("ytd") if isinstance(g.get("ytd"), dict) else {}

    missing = []
    for k in ("revenue", "op", "ytd_months"):
        if not is_num(g.get(k)):
            missing.append(f"guidance.{k}")
    for k in ("revenue", "op"):
        if not is_num(ytd.get(k)):
            missing.append(f"guidance.ytd.{k}")
    if missing:
        return make_result(lid, name, status="入力不足", missing=missing)

    g_rev = float(g["revenue"])
    g_op = float(g["op"])
    ytd_m = float(g["ytd_months"])
    rest_m = 12.0 - ytd_m
    if rest_m <= 0 or ytd_m <= 0:
        return make_result(lid, name, status="入力不足", missing=["guidance.ytd_months(1〜11の範囲)"])

    y_rev = float(ytd["revenue"])
    y_op = float(ytd["op"])
    rest_rev = g_rev - y_rev
    rest_op = g_op - y_op
    if rest_rev <= 0 or y_rev <= 0:
        return make_result(lid, name, status="入力不足", missing=["guidance.revenue > ytd.revenue"])

    ytd_opm = y_op / y_rev * 100.0
    rest_opm = rest_op / rest_rev * 100.0
    gap_opm = rest_opm - ytd_opm

    # 粗利率データがある場合: guidance.gross があればそのまま使用、無ければ販管費2通りで推定
    has_ytd_gm = is_num(ytd.get("gross"))
    has_g_gross = is_num(g.get("gross"))
    ytd_gm = (float(ytd["gross"]) / y_rev * 100.0) if has_ytd_gm else None
    ytd_sga = (float(ytd["gross"]) - y_op) if has_ytd_gm else None

    gm_is_estimated = has_ytd_gm and not has_g_gross
    rest_gm_primary = None
    gap_gm_primary = None
    rest_gm_a = None
    rest_gm_b = None
    gap_gm_a = None
    gap_gm_b = None
    rest_sga_for_if = None

    if has_ytd_gm and has_g_gross:
        rest_gross = float(g["gross"]) - float(ytd["gross"])
        rest_sga_actual = rest_gross - rest_op
        rest_gm_primary = rest_gross / rest_rev * 100.0
        gap_gm_primary = rest_gm_primary - ytd_gm
        rest_sga_for_if = rest_sga_actual
    elif has_ytd_gm and ytd_sga is not None:
        # (a) 残り期間の販管費 = 累計と同額
        sga_a = ytd_sga
        rest_gross_a = rest_op + sga_a
        rest_gm_a = rest_gross_a / rest_rev * 100.0
        gap_gm_a = rest_gm_a - ytd_gm
        # (b) 残り期間の販管費 = 累計の売上比率 × 残り期間の売上
        sga_b = (ytd_sga / y_rev) * rest_rev
        rest_gross_b = rest_op + sga_b
        rest_gm_b = rest_gross_b / rest_rev * 100.0
        gap_gm_b = rest_gm_b - ytd_gm

        rest_gm_primary = rest_gm_a
        gap_gm_primary = gap_gm_a
        rest_sga_for_if = sga_a

    # もし残りが ytd 並みの利益率なら
    fy_op_if_ytd_opm = y_op + rest_rev * (ytd_opm / 100.0)
    fy_op_if_ytd_gm = (
        y_op + rest_rev * (ytd_gm / 100.0) - rest_sga_for_if
        if (ytd_gm is not None and rest_sga_for_if is not None)
        else None
    )
    primary_if_ytd = fy_op_if_ytd_gm if fy_op_if_ytd_gm is not None else fy_op_if_ytd_opm

    # prior_rest の比較
    pr = g.get("prior_rest") if isinstance(g.get("prior_rest"), dict) else {}
    has_pr = is_num(pr.get("revenue")) and pr.get("revenue", 0) > 0 and is_num(pr.get("op"))
    pr_opm = (float(pr["op"]) / float(pr["revenue"]) * 100.0) if has_pr else None
    pr_gm = (float(pr["gross"]) / float(pr["revenue"]) * 100.0) if (has_pr and is_num(pr.get("gross"))) else None
    diff_vs_pr_opm = (rest_opm - pr_opm) if pr_opm is not None else None
    diff_vs_pr_gm = (rest_gm_primary - pr_gm) if (rest_gm_primary is not None and pr_gm is not None) else None

    fy_op_if_pr_opm = (y_op + rest_rev * (pr_opm / 100.0)) if pr_opm is not None else None
    fy_op_if_pr_gm = (
        y_op + rest_rev * (pr_gm / 100.0) - rest_sga_for_if
        if (pr_gm is not None and rest_sga_for_if is not None)
        else None
    )

    prog_pct = (y_op / g_op * 100.0) if g_op != 0 else None
    std_prog_pct = ytd_m / 12.0 * 100.0
    prog_diff_pt = (prog_pct - std_prog_pct) if prog_pct is not None else None

    numbers: dict[str, Any] = {
        "fy": g.get("fy", ""),
        "guidance_revenue": rnd(g_rev, 1),
        "guidance_op": rnd(g_op, 1),
        "ytd_months": int(ytd_m),
        "rest_revenue": rnd(rest_rev, 1),
        "rest_op": rnd(rest_op, 1),
        "ytd_opm_pct": rnd(ytd_opm, 2),
        "rest_opm_pct": rnd(rest_opm, 2),
        "rest_minus_ytd_opm_pt": rnd(gap_opm, 2),
        "ytd_gm_pct": rnd(ytd_gm, 2),
        "rest_implied_gm_pct": rnd(rest_gm_primary, 2),
        "rest_minus_ytd_gm_pt": rnd(gap_gm_primary, 2),
        "gm_is_estimated": gm_is_estimated,
        "fy_op_if_ytd_margin": rnd(primary_if_ytd, 0),
        "fy_op_if_ytd_gm": rnd(fy_op_if_ytd_gm, 0),
        "fy_op_if_ytd_opm": rnd(fy_op_if_ytd_opm, 0),
        "prior_rest_opm_pct": rnd(pr_opm, 2),
        "prior_rest_gm_pct": rnd(pr_gm, 2),
        "rest_minus_prior_opm_pt": rnd(diff_vs_pr_opm, 2),
        "rest_minus_prior_gm_pt": rnd(diff_vs_pr_gm, 2),
        "fy_op_if_prior_opm": rnd(fy_op_if_pr_opm, 0),
        "fy_op_if_prior_gm": rnd(fy_op_if_pr_gm, 0),
        "op_progress_pct": rnd(prog_pct, 1),
        "standard_progress_pct": rnd(std_prog_pct, 1),
        "progress_excess_pt": rnd(prog_diff_pt, 1),
    }
    if gm_is_estimated:
        numbers["rest_gm_est_a_pct"] = rnd(rest_gm_a, 2)
        numbers["rest_gm_est_b_pct"] = rnd(rest_gm_b, 2)
        numbers["rest_minus_ytd_gm_a_pt"] = rnd(gap_gm_a, 2)
        numbers["rest_minus_ytd_gm_b_pt"] = rnd(gap_gm_b, 2)

    reads = [
        f"会社予想(売上{g_rev:,.0f}・営業利益{g_op:,.0f})から累計実績を引いた残り期間({int(rest_m)}か月)の前提は、"
        f"売上{rest_rev:,.0f}・営業利益{rest_op:,.0f}・営業利益率{rest_opm:.2f}%(累計{ytd_opm:.2f}%比{gap_opm:+.2f}pt)。",
    ]
    if fy_op_if_ytd_gm is not None:
        if gm_is_estimated:
            reads.append(
                f"残り期間の粗利率の前提は (a) {rest_gm_a:.2f}% 〜 (b) {rest_gm_b:.2f}%(推定。販管費の置き方による)、"
                f"累計{ytd_gm:.2f}%比は (a) {gap_gm_a:+.2f}pt・(b) {gap_gm_b:+.2f}pt。"
                f"累計並みの粗利率なら通期営業利益は{fy_op_if_ytd_gm:,.0f}(営業利益率基準では{fy_op_if_ytd_opm:,.0f})。"
            )
        else:
            reads.append(
                f"残り期間の粗利率の前提は{rest_gm_primary:.2f}%(累計{ytd_gm:.2f}%比{gap_gm_primary:+.2f}pt)。"
                f"累計並みの粗利率なら通期営業利益は{fy_op_if_ytd_gm:,.0f}(営業利益率基準では{fy_op_if_ytd_opm:,.0f})。"
            )
    else:
        reads.append(f"定義[営業利益率基準]: 残りが累計並みの営業利益率({ytd_opm:.2f}%)なら通期営業利益は{fy_op_if_ytd_opm:,.0f}。")
    if has_pr:
        pr_str = f"前年残り期間の営業利益率は{pr_opm:.2f}%(今期予想比{diff_vs_pr_opm:+.2f}pt)、営業利益率基準の通期は{fy_op_if_pr_opm:,.0f}"
        if fy_op_if_pr_gm is not None:
            pr_str += f"(粗利率{pr_gm:.2f}%基準の通期は{fy_op_if_pr_gm:,.0f})"
        reads.append(pr_str + "。")
    if prog_pct is not None:
        if prog_diff_pt < 0:
            reads.append(f"通期営業利益に対する進捗率は{prog_pct:.1f}%で、標準進捗{std_prog_pct:.1f}%を{abs(prog_diff_pt):.1f}pt下回る。")
        else:
            reads.append(f"通期営業利益に対する進捗率は{prog_pct:.1f}%で、標準進捗{std_prog_pct:.1f}%を{prog_diff_pt:.1f}pt上回る。")

    flags: list[dict[str, str]] = []
    if gap_opm <= -1.5:
        add_flag(
            flags, lid,
            f"残り期間の前提の利益率が累計より低い(営業利益率差{gap_opm:+.2f}pt)",
            "残り期間の利益率低下の前提は保守的な計画か、原料高・定修・値戻し等の悪化要因を織り込んでいるのか？",
            "会社業績予想の前提条件(原料価格・為替前提)と足元の原料市況・下期定修予定",
        )
    elif gm_is_estimated and gap_gm_a is not None and gap_gm_b is not None and gap_gm_a <= -1.5 and gap_gm_b <= -1.5:
        add_flag(
            flags, lid,
            f"残り期間の粗利率の前提(推定)が累計より低い。営業利益率は {gap_opm:+.2f}pt",
            "販管費を抑える前提か、粗利率の低下を織り込むのか",
            "会社業績予想の前提条件(販管費計画・原価率前提)と足元の粗利率推移",
        )
    elif (not gm_is_estimated) and gap_gm_primary is not None and gap_gm_primary <= -1.5:
        add_flag(
            flags, lid,
            f"残り期間の粗利率の前提が累計より低い(粗利率差{gap_gm_primary:+.2f}pt)。営業利益率は {gap_opm:+.2f}pt",
            "販管費を抑える前提か、粗利率の低下を織り込むのか",
            "会社業績予想の前提条件(販管費計画・原価率前提)と足元の粗利率推移",
        )
    if prog_diff_pt is not None and prog_diff_pt >= 10.0:
        add_flag(
            flags, lid,
            f"営業利益の進捗率{prog_pct:.1f}%が期間按分{std_prog_pct:.1f}%を{prog_diff_pt:+.1f}pt(>=10pt)上回る",
            "なぜ進捗が大幅に先行しているのに通期予想が据え置かれているのか？",
            "通期予想据え置きの理由に関する決算短信・説明会の質疑応答と下期特有の費用計上予定",
        )

    return make_result(lid, name, status="ok", numbers=numbers, reads=reads, flags=flags)


def lens_l06(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L06", "年換算と計画"
    segs = data.get("segments")
    if not isinstance(segs, list) or not segs:
        return make_result(lid, name, status="入力不足", missing=["segments"])

    rows = []
    missing_fields = []
    for s in segs:
        if not isinstance(s, dict):
            continue
        if not (is_num(s.get("ytd_months")) and is_num(s.get("ytd_profit"))) or s.get("ytd_months", 0) <= 0:
            missing_fields.append(str(s.get("name", "segment")))
            continue
        ann = float(s["ytd_profit"]) * 12.0 / float(s["ytd_months"])
        has_plan = is_num(s.get("plan_lo")) and is_num(s.get("plan_hi"))
        mid = ((float(s["plan_lo"]) + float(s["plan_hi"])) / 2.0) if has_plan else None
        ratio = (ann / mid * 100.0) if (mid is not None and mid != 0) else None
        status_seg = (
            ("先行" if ratio > 105.0 else ("遅れ" if ratio < 90.0 else "順調"))
            if ratio is not None
            else None
        )
        row: dict[str, Any] = {
            "name": s.get("name", ""),
            "strategic": bool(s.get("strategic", False)),
            "ytd_profit": rnd(s["ytd_profit"], 1),
            "annualized_profit": rnd(ann, 1),
            "plan_mid": rnd(mid, 1),
            "ratio_pct": rnd(ratio, 1),
            "pace": status_seg,
        }
        if is_num(s.get("prev_profit")):
            prev_p = float(s["prev_profit"])
            vs_prev = (ann / prev_p * 100.0) if prev_p > 0 else None
            row["prev_profit"] = rnd(prev_p, 1)
            row["vs_prev_pct"] = rnd(vs_prev, 1)
        rows.append(row)

    if not rows:
        return make_result(lid, name, status="入力不足", missing=["segments(ytd_months,ytd_profit)"])

    plan_rows = [r for r in rows if r["plan_mid"] is not None]
    prev_rows = [r for r in rows if "prev_profit" in r]

    ahead = [r["name"] for r in plan_rows if r["pace"] == "先行"]
    behind = [r["name"] for r in plan_rows if r["pace"] == "遅れ"]

    strat_rows = [r for r in rows if r["strategic"]]
    nonstrat_rows = [r for r in rows if not r["strategic"]]

    def group_ratio(grp: list[dict[str, Any]]) -> tuple[float | None, float, float | None]:
        ann_sum = sum(r["annualized_profit"] for r in grp)
        p_grp = [r for r in grp if r["plan_mid"] is not None]
        if not p_grp:
            return None, ann_sum, None
        mid_sum = sum(r["plan_mid"] for r in p_grp)
        ann_p_sum = sum(r["annualized_profit"] for r in p_grp)
        ratio = (ann_p_sum / mid_sum * 100.0) if mid_sum > 0 else None
        return ratio, ann_sum, mid_sum

    strat_ratio, strat_ann, strat_mid = group_ratio(strat_rows)
    nonstrat_ratio, nonstrat_ann, nonstrat_mid = group_ratio(nonstrat_rows)

    numbers = {
        "segments": rows,
        "ahead_segments": ahead,
        "behind_segments": behind,
        "strategic_annualized": rnd(strat_ann, 1),
        "strategic_plan_mid": rnd(strat_mid, 1),
        "strategic_ratio_pct": rnd(strat_ratio, 1),
        "non_strategic_annualized": rnd(nonstrat_ann, 1),
        "non_strategic_plan_mid": rnd(nonstrat_mid, 1),
        "non_strategic_ratio_pct": rnd(nonstrat_ratio, 1),
    }

    reads: list[str] = []
    if plan_rows:
        seg_txt = "、".join(
            f"{r['name']} {r['ratio_pct']:.0f}%({r['pace']})"
            for r in plan_rows
            if r["ratio_pct"] is not None
        )
        reads.append(f"セグメント別の年換算利益÷計画中央値: {seg_txt}。")
        if strat_ratio is not None and nonstrat_ratio is not None:
            reads.append(
                f"戦略セグメント合計は年換算{strat_ann:,.0f}÷目標{strat_mid:,.0f}={strat_ratio:.1f}%、"
                f"非戦略セグメント合計は{nonstrat_ann:,.0f}÷{nonstrat_mid:,.0f}={nonstrat_ratio:.1f}%。"
            )
    else:
        seg_ann_txt = "、".join(
            f"{r['name']} 年換算{r['annualized_profit']:,.0f}(累計{r['ytd_profit']:,.0f})"
            for r in rows
        )
        reads.append(f"セグメント別の年換算利益(計画未開示): {seg_ann_txt}。")

    if prev_rows:
        prev_parts = []
        for r in prev_rows:
            if r.get("vs_prev_pct") is not None:
                prev_parts.append(f"{r['name']} {r['vs_prev_pct']:.1f}%(年換算{r['annualized_profit']:,.0f}÷前期{r['prev_profit']:,.0f})")
            else:
                prev_parts.append(f"{r['name']} 年換算{r['annualized_profit']:,.0f}(前期{r['prev_profit']:,.0f})")
        reads.append(f"セグメント別の年換算利益÷前期通期: {'、'.join(prev_parts)}。")

    if not plan_rows and prev_rows:
        over20 = []
        for r in prev_rows:
            prev_p = r["prev_profit"]
            if prev_p and prev_p != 0:
                chg_pct = (r["annualized_profit"] - prev_p) / abs(prev_p) * 100.0
                if abs(chg_pct) > 20.0:
                    over20.append(f"{r['name']}({chg_pct:+.1f}%)")
        if over20:
            reads.append(f"年換算が前期比で±20%超のセグメント: {'、'.join(over20)}。")
        else:
            reads.append("年換算が前期比で±20%超のセグメントはなし。")

    flags: list[dict[str, str]] = []
    if plan_rows and strat_ratio is not None and nonstrat_ratio is not None and strat_ratio < 90.0 and nonstrat_ratio > 105.0:
        add_flag(
            flags, lid,
            f"戦略セグメントが遅れ({strat_ratio:.1f}%<90%)、非戦略セグメントが先行({nonstrat_ratio:.1f}%>105%)で達成の中身が計画と異なる",
            "なぜ成長の核である戦略セグメントが計画に届かず、非戦略事業が計画を大きく超過しているのか？",
            "セグメント別業績概況・中計目標との差異説明と顧客採用・市況要因の内訳",
        )

    return make_result(lid, name, status="ok", missing=missing_fields, numbers=numbers, reads=reads, flags=flags)


def lens_l07(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L07", "デュポン"
    annual = data.get("annual") or []
    model = data.get("model") or []
    first, last = find_first_last_annual_with(annual, ["revenue", "net", "assets", "equity"])
    valid_model = get_rows_with(model, ["revenue", "net", "assets", "equity"])

    if not last:
        return make_result(lid, name, status="入力不足", missing=["annual(revenue,net,assets,equity)"])

    def calc_dupont(label: str, r: dict[str, Any]) -> dict[str, Any]:
        rev = float(r["revenue"])
        net = float(r["net"])
        assets = float(r["assets"])
        equity = float(r["equity"])
        npm = net / rev * 100.0
        tat = rev / assets
        lev = assets / equity
        roe_end = net / equity * 100.0
        out = {
            "label": label,
            "net_margin_pct": rnd(npm, 2),
            "asset_turnover": rnd(tat, 3),
            "leverage": rnd(lev, 3),
            "roe_ending_pct": rnd(roe_end, 2),
        }
        if is_num(r.get("roe")):
            out["roe_reported_pct"] = rnd(float(r["roe"]), 2)
        return out

    items = []
    if first and first is not last:
        items.append(calc_dupont(f"実績_{first.get('fy')}", first))
    last_dp = calc_dupont(f"実績_{last.get('fy')}", last)
    items.append(last_dp)
    for m in valid_model:
        lbl = f"モデル_{m.get('fy','')}_{m.get('scenario','')}"
        items.append(calc_dupont(lbl, m))

    numbers: dict[str, Any] = {"rows": items}
    reads: list[str] = []
    flags: list[dict[str, str]] = []

    reads.append(
        "実績デュポン: "
        + " → ".join(
            f"{it['label']}(純利益率{it['net_margin_pct']:.2f}%×回転率{it['asset_turnover']:.2f}×レバ{it['leverage']:.2f}=期末ROE{it['roe_ending_pct']:.2f}%)"
            for it in items[:2 if (first and first is not last) else 1]
        )
    )

    base_m = find_base_scenario(valid_model)
    if base_m:
        m_dp = calc_dupont(f"モデル_{base_m.get('fy','')}_{base_m.get('scenario','')}", base_m)
        m_npm = float(base_m["net"]) / float(base_m["revenue"])
        m_tat = float(base_m["revenue"]) / float(base_m["assets"])
        last_lev = float(last["assets"]) / float(last["equity"])
        roe_if_same_lev = m_npm * m_tat * last_lev * 100.0
        m_roe = m_dp["roe_ending_pct"]
        lev_drag_pt = roe_if_same_lev - m_roe

        numbers["model_base_label"] = m_dp["label"]
        numbers["model_base_roe_pct"] = m_roe
        numbers["roe_if_last_leverage_pct"] = rnd(roe_if_same_lev, 2)
        numbers["leverage_drag_pt"] = rnd(lev_drag_pt, 2)

        reads.append(
            f"{m_dp['label']}の期末ROEは{m_roe:.2f}%だが、レバレッジが直近実績({last_lev:.2f}倍)のままなら"
            f"ROEは{roe_if_same_lev:.2f}%になり、レバレッジ低下がROEを{lev_drag_pt:+.2f}pt押し下げている。"
        )

        # 旗判定: 直近実績 -> モデル基準最終年
        npm_gain = m_dp["net_margin_pct"] - last_dp["net_margin_pct"]
        roe_gain = m_roe - last_dp["roe_ending_pct"]
        if npm_gain > 0 and roe_gain < 1.0:
            add_flag(
                flags, lid,
                f"純利益率は改善({npm_gain:+.2f}pt)するのにROE上昇が{roe_gain:+.2f}pt(<1pt)に留まる",
                "なぜ稼ぐ力(純利益率)の上昇がROE改善に結びつかないのか？",
                "将来の自己資本蓄積・キャッシュ配分計画と資産回転率の前提",
            )
        if lev_drag_pt >= 1.0:
            add_flag(
                flags, lid,
                f"財務レバレッジ低下({last_dp['leverage']:.2f}倍→{m_dp['leverage']:.2f}倍)がモデルROEを{lev_drag_pt:.2f}pt(>=1pt)削る",
                "なぜ財務レバレッジが大きく下がりROEを押し下げる設計なのか(過剰資本の滞留・還元不足か)？",
                "中期経営計画のキャッシュアロケーション・目標自己資本比率・配当/自己株買い方針",
            )

    # 実績の最初 -> 最後でも純利益率上昇かつROE改善1pt未満を確認
    if first and first is not last:
        f_dp = items[0]
        if (last_dp["net_margin_pct"] - f_dp["net_margin_pct"]) > 0 and (last_dp["roe_ending_pct"] - f_dp["roe_ending_pct"]) < 1.0:
            add_flag(
                flags, lid,
                f"実績({first.get('fy')}→{last.get('fy')})で純利益率は上昇({f_dp['net_margin_pct']:.2f}%→{last_dp['net_margin_pct']:.2f}%)したがROE改善は1pt未満",
                "なぜ純利益率が上がっても実績ROEが上がっていないのか？",
                "有価証券報告書の貸借対照表(総資産と自己資本の増加要因)",
            )

    return make_result(lid, name, status="ok", numbers=numbers, reads=reads, flags=flags)


def lens_l08(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L08", "資本の使い道"
    assume = data.get("assume") or {}
    price = data.get("price") or {}
    annual = data.get("annual") or []
    cap_uses = data.get("capital_uses") or []

    coe = assume.get("coe")
    tax = assume.get("tax")
    cash_yield_raw = assume.get("cash_yield")
    cash_yield = float(cash_yield_raw) if is_num(cash_yield_raw) else 0.1
    close = price.get("close")
    eps_next = price.get("eps_next")

    debt_rows = get_rows_with(annual, ["interest", "debt"])
    last_debt_row = debt_rows[-1] if debt_rows else None
    last_ann = annual[-1] if (isinstance(annual, list) and annual and isinstance(annual[-1], dict)) else None

    missing = []
    if not is_num(coe):
        missing.append("assume.coe")
    if not is_num(tax):
        missing.append("assume.tax")
    if not is_num(close) or close <= 0:
        missing.append("price.close")
    if not is_num(eps_next):
        missing.append("price.eps_next")
    if not last_debt_row or last_debt_row["debt"] <= 0:
        missing.append("annual(直近期のinterest,debt)")

    if missing and (not is_num(coe) or (not cap_uses and len(missing) >= 3)):
        return make_result(lid, name, status="入力不足", missing=missing)

    options = []
    bb_yield: float | None = None
    if is_num(close) and close > 0 and is_num(eps_next):
        bb_yield = float(eps_next) / float(close) * 100.0
        options.append({"name": "自己株取得(益回り)", "yield_pct": rnd(bb_yield, 2), "note": f"eps_next {eps_next} ÷ close {close}"})
    if last_debt_row and last_debt_row["debt"] > 0 and is_num(tax):
        debt_yield = float(last_debt_row["interest"]) / float(last_debt_row["debt"]) * (1.0 - float(tax) / 100.0) * 100.0
        options.append({"name": "借入返済(税後)", "yield_pct": rnd(debt_yield, 2), "note": f"利子{last_debt_row['interest']}÷負債{last_debt_row['debt']}×(1-税率{tax}%)"})

    cash_ratio_pct: float | None = None
    if last_ann and is_num(last_ann.get("cash")) and last_ann["cash"] > 0:
        cash_val = float(last_ann["cash"])
        if is_num(last_ann.get("assets")) and last_ann["assets"] > 0:
            cash_ratio_pct = cash_val / float(last_ann["assets"]) * 100.0
        cash_note_txt = f"現預金{cash_val:,.0f}" + (f"(総資産の{cash_ratio_pct:.1f}%)" if cash_ratio_pct is not None else "")
        options.append({"name": "現預金の保有", "yield_pct": rnd(cash_yield, 2), "note": f"{cash_note_txt}・想定利回り{cash_yield:.2f}%"})

    for cu in cap_uses:
        if isinstance(cu, dict) and is_num(cu.get("yield")):
            cu_item: dict[str, Any] = {
                "name": str(cu.get("name", "")),
                "yield_pct": rnd(float(cu["yield"]), 2),
                "note": str(cu.get("note", "")),
            }
            if cu.get("actual") is False:
                cu_item["actual"] = False
            options.append(cu_item)

    if not options or not is_num(coe):
        return make_result(lid, name, status="入力不足", missing=missing or ["capital_uses"])

    coe_f = float(coe)
    options.sort(key=lambda x: x["yield_pct"], reverse=True)
    for i, op_item in enumerate(options, 1):
        op_item["rank"] = i
        op_item["spread_vs_coe_pt"] = rnd(op_item["yield_pct"] - coe_f, 2)

    below_coe = [
        op_item["name"]
        for op_item in options
        if op_item["yield_pct"] < coe_f
        and op_item.get("actual", True) is not False
        and op_item["name"] != "自己株取得(益回り)"
    ]

    numbers: dict[str, Any] = {
        "coe_pct": rnd(coe_f, 2),
        "ranked_uses": options,
        "below_coe_names": below_coe,
    }
    if cash_ratio_pct is not None:
        numbers["cash_to_assets_pct"] = rnd(cash_ratio_pct, 1)

    rank_str = " > ".join(f"{o['rank']}位 {o['name']}({o['yield_pct']:.2f}%)" for o in options)
    reads = [f"株主資本コスト({coe_f:.2f}%)に対する資本使途の税後利回り順位: {rank_str}。"]
    if below_coe:
        reads.append(f"株主資本コストを下回る使途: {'・'.join(below_coe)}。")
    if bb_yield is not None and bb_yield < coe_f:
        reads.append(f"自己株取得の益回り {bb_yield:.2f}% は資本コスト {coe_f:.2f}% を下回る(今の株価での取得は割高)。")

    flags: list[dict[str, str]] = []
    if below_coe:
        cash_flag_note = (
            f"(現預金が総資産の{cash_ratio_pct:.1f}%)"
            if (cash_ratio_pct is not None and cash_ratio_pct >= 20.0)
            else ""
        )
        add_flag(
            flags, lid,
            f"株主資本コスト({coe_f:.2f}%)を下回る資本使途あり: {'、'.join(below_coe)}{cash_flag_note}",
            f"なぜ資本コストより利回りの低い「{'、'.join(below_coe)}」に資本を滞留・配分させているのか？",
            "資本コストや株価を意識した経営の開示資料・政策保有株縮減方針・借入返済と自己株買いの優先順位",
        )

    return make_result(lid, name, status="ok", missing=missing, numbers=numbers, reads=reads, flags=flags)


def lens_l09(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L09", "織り込みROEと成長の値段"
    assume = data.get("assume") or {}
    price = data.get("price") or {}
    annual = data.get("annual") or []
    model = data.get("model") or []

    coe = assume.get("coe")
    g = assume.get("g")
    close = price.get("close")
    bps = price.get("bps")
    eps_next = price.get("eps_next")

    missing = []
    if not is_num(coe) or coe <= 0:
        missing.append("assume.coe")
    if not is_num(g):
        missing.append("assume.g")
    if not is_num(close):
        missing.append("price.close")
    if not is_num(bps) or bps <= 0:
        missing.append("price.bps")
    if not is_num(eps_next):
        missing.append("price.eps_next")

    if missing:
        return make_result(lid, name, status="入力不足", missing=missing)

    coe_f = float(coe)
    g_f = float(g)
    close_f = float(close)
    bps_f = float(bps)
    eps_f = float(eps_next)

    pbr = close_f / bps_f
    implied_roe = pbr * (coe_f - g_f) + g_f
    steady_value = eps_f / (coe_f / 100.0)
    growth_price = close_f - steady_value

    roe_rows = get_rows_with(annual, ["net", "equity"])
    actual_roe = (roe_rows[-1]["net"] / roe_rows[-1]["equity"] * 100.0) if roe_rows else None
    diff_actual = (implied_roe - actual_roe) if actual_roe is not None else None

    base_m = find_base_scenario(model)
    model_roe = None
    if base_m:
        if is_num(base_m.get("roe")):
            model_roe = float(base_m["roe"])
        elif is_num(base_m.get("net")) and is_num(base_m.get("equity")) and base_m["equity"] > 0:
            model_roe = float(base_m["net"]) / float(base_m["equity"]) * 100.0
    diff_model = (implied_roe - model_roe) if model_roe is not None else None

    numbers = {
        "pbr": rnd(pbr, 3),
        "implied_roe_pct": rnd(implied_roe, 2),
        "actual_roe_pct": rnd(actual_roe, 2),
        "implied_minus_actual_pt": rnd(diff_actual, 2),
        "model_base_roe_pct": rnd(model_roe, 2),
        "implied_minus_model_pt": rnd(diff_model, 2),
        "steady_state_value": rnd(steady_value, 1),
        "price_of_growth": rnd(growth_price, 1),
        "price_of_growth_pct_of_close": rnd(growth_price / close_f * 100.0, 1) if close_f else None,
    }

    reads = [
        f"PBR {pbr:.2f}倍(株価{close_f:,.0f}円÷BPS{bps_f:,.1f}円)・COE {coe_f:.2f}%・g {g_f:.1f}%からの市場織り込みROEは{implied_roe:.2f}%。",
        f"定常状態価値(予想EPS {eps_f:.1f}円÷COE)は{steady_value:,.0f}円で、株価に織り込まれた成長の値段は{growth_price:+,.0f}円。",
    ]
    if actual_roe is not None:
        reads.append(f"直近実績ROE({actual_roe:.2f}%)との差は{diff_actual:+.2f}pt。")
    if model_roe is not None:
        reads.append(f"5年後基準モデルROE({model_roe:.2f}%)との差は{diff_model:+.2f}pt。")

    flags: list[dict[str, str]] = []
    if actual_roe is not None and implied_roe < actual_roe:
        add_flag(
            flags, lid,
            f"織り込みROE({implied_roe:.2f}%)が直近実績ROE({actual_roe:.2f}%)を下回り、今の実力すら株価に入っていない",
            "なぜ足元の実績ROEより低い水準しか市場が織り込んでいないのか(減益懸念か資本効率への不信か)？",
            "市場コンセンサス予想・同業他社PBR比較と減益リスク要因(有価証券報告書リスク情報)",
        )
    if growth_price <= 0:
        add_flag(
            flags, lid,
            f"成長の値段が{growth_price:+,.0f}円(<=0)で、将来の成長を無料以下で売っている",
            "なぜ定常状態価値すら下回るディスカウントで放置されているのか？",
            "実質資産価値(賃貸等不動産・政策保有株)の注記と株主還元・流動性制約",
        )
    if model_roe is not None and implied_roe < model_roe - 1.5:
        add_flag(
            flags, lid,
            f"織り込みROE({implied_roe:.2f}%)がモデル基準ROE({model_roe:.2f}%)を{-diff_model:.2f}pt(>1.5pt)下回る",
            "モデルが想定するROE改善経路を市場がまだ織り込んでいない理由は何か(達成確度への疑義か認知不足か)？",
            "中期経営計画の定量目標の前提と過去の計画達成実績",
        )

    return make_result(lid, name, status="ok", numbers=numbers, reads=reads, flags=flags)


def lens_l10(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L10", "同業の線"
    peers = data.get("peers")
    price = data.get("price") or {}
    annual = data.get("annual") or []
    model = data.get("model") or []

    if not isinstance(peers, list) or len(peers) < 3:
        return make_result(lid, name, status="入力不足", missing=["peers(3社以上)"])

    valid_peers = [p for p in peers if isinstance(p, dict) and is_num(p.get("pbr")) and is_num(p.get("roe"))]
    if len(valid_peers) < 3:
        return make_result(lid, name, status="入力不足", missing=["peers(3社以上のpbr,roe)"])

    close = price.get("close")
    bps = price.get("bps")
    if not is_num(close) or not is_num(bps) or bps <= 0:
        return make_result(lid, name, status="入力不足", missing=["price.close", "price.bps"])

    xs = [float(p["roe"]) for p in valid_peers]
    ys = [float(p["pbr"]) for p in valid_peers]
    a, b, _r, r2 = ols(xs, ys)

    actual_pbr = float(close) / float(bps)
    roe_rows = get_rows_with(annual, ["net", "equity"])
    actual_roe = (
        roe_rows[-1]["net"] / roe_rows[-1]["equity"] * 100.0
        if (roe_rows and roe_rows[-1]["equity"] > 0)
        else None
    )
    forward_roe = (float(price["eps_next"]) / float(bps) * 100.0) if is_num(price.get("eps_next")) else None

    line_pbr_actual = (a + b * actual_roe) if actual_roe is not None else None
    diff_actual_pct = ((actual_pbr - line_pbr_actual) / line_pbr_actual * 100.0) if (line_pbr_actual and line_pbr_actual > 0) else None

    line_pbr_forward = (a + b * forward_roe) if forward_roe is not None else None
    diff_forward_pct = ((actual_pbr - line_pbr_forward) / line_pbr_forward * 100.0) if (line_pbr_forward and line_pbr_forward > 0) else None

    base_m = find_base_scenario(model)
    model_roe = None
    if base_m:
        if is_num(base_m.get("roe")):
            model_roe = float(base_m["roe"])
        elif is_num(base_m.get("net")) and is_num(base_m.get("equity")) and base_m["equity"] > 0:
            model_roe = float(base_m["net"]) / float(base_m["equity"]) * 100.0

    line_pbr_model = (a + b * model_roe) if model_roe is not None else None
    line_px_model = (line_pbr_model * float(bps)) if line_pbr_model is not None else None

    line_pbr_10 = a + b * 10.0
    line_px_10 = line_pbr_10 * float(bps)

    numbers = {
        "n_peers": len(valid_peers),
        "reg_a": rnd(a, 4),
        "reg_b": rnd(b, 4),
        "r2": rnd(r2, 4),
        "actual_pbr": rnd(actual_pbr, 3),
        "actual_roe_pct": rnd(actual_roe, 2),
        "line_pbr_at_actual_roe": rnd(line_pbr_actual, 3),
        "pbr_diff_vs_line_pct": rnd(diff_actual_pct, 1),
        "forward_roe_pct": rnd(forward_roe, 2),
        "line_pbr_at_forward_roe": rnd(line_pbr_forward, 3),
        "pbr_diff_vs_line_forward_pct": rnd(diff_forward_pct, 1),
        "model_base_roe_pct": rnd(model_roe, 2),
        "line_pbr_at_model_roe": rnd(line_pbr_model, 3),
        "line_price_at_model_roe": rnd(line_px_model, 1),
        "line_pbr_at_roe10": rnd(line_pbr_10, 3),
        "line_price_at_roe10": rnd(line_px_10, 1),
    }

    reads = [
        f"同業{len(valid_peers)}社のPBR-ROE回帰(PBR = {a:.3f} + {b:.4f}×ROE)のR²は{r2:.2f}。",
    ]
    ref_suffix = ": 参考値(線が当てはまらない)" if r2 < 0.5 else ""
    if line_pbr_actual is not None:
        diff_txt = f"実際PBR({actual_pbr:.2f}倍)との差は{diff_actual_pct:+.1f}%" if diff_actual_pct is not None else f"実際PBRは{actual_pbr:.2f}倍"
        reads.append(
            f"自社の実績ROE({actual_roe:.2f}%)上の線上PBRは{line_pbr_actual:.2f}倍で、{diff_txt}。"
        )
    if line_pbr_forward is not None:
        diff_fwd_txt = f"実際PBR({actual_pbr:.2f}倍)との差は{diff_forward_pct:+.1f}%" if diff_forward_pct is not None else f"実際PBRは{actual_pbr:.2f}倍"
        reads.append(
            f"自社の予想ROE({forward_roe:.2f}%)上の線上PBRは{line_pbr_forward:.2f}倍で、{diff_fwd_txt}。"
        )
    if line_px_model is not None:
        reads.append(
            f"5年後基準モデルROE({model_roe:.2f}%)での線上PBRは{line_pbr_model:.2f}倍(線上株価{line_px_model:,.0f}円{ref_suffix})、ROE10%では{line_pbr_10:.2f}倍({line_px_10:,.0f}円{ref_suffix})。"
        )
    else:
        reads.append(f"ROE10%での線上PBRは{line_pbr_10:.2f}倍(線上株価{line_px_10:,.0f}円{ref_suffix})。")

    if r2 < 0.5:
        reads.append(f"同業の PBR は ROE では説明できない(R² {r2:.2f})。業態で同業を分け直すか、別の物差し(成長率など)を使う。")

    flags: list[dict[str, str]] = []
    if r2 >= 0.5 and r2 >= 0.6:
        diverged = (
            diff_actual_pct is not None
            and diff_forward_pct is not None
            and (diff_actual_pct < -10.0) != (diff_forward_pct < -10.0)
        )
        if diverged:
            add_flag(
                flags, lid,
                f"実績ROEでは割安に見えるが、予想ROEでは同業並み(見かけの割安: 実績ROE基準{diff_actual_pct:+.1f}%・予想ROE基準{diff_forward_pct:+.1f}%)",
                "なぜ実績ROEと予想ROEで同業線に対する評価が逆転しているのか(一過性利益の剥落か減益見通しか)？",
                "会社予想・コンセンサスの利益変動要因と一過性損益の有無、同業他社の予想ROEとの比較",
            )
        else:
            primary_diff = diff_forward_pct if diff_forward_pct is not None else diff_actual_pct
            if primary_diff is not None:
                if -10.0 <= primary_diff <= 10.0:
                    add_flag(
                        flags, lid,
                        f"同業線(R²={r2:.2f})と実際PBRの差が{primary_diff:+.1f}%(±10%以内): 今の実力には同業並みの値段、入っていないのは将来の経路",
                        "現在のROEはすでに同業並みに評価されているが、モデルROE到達までの改善経路が織り込まれていない根拠は何か？",
                        "同業他社の予想ROEコンセンサスと自社の利益率・ROE改善ドライバーの開示",
                    )
                elif primary_diff < -10.0:
                    add_flag(
                        flags, lid,
                        f"同業線(R²={r2:.2f})に対して実際PBRが{primary_diff:+.1f}%(-10%超のディスカウント)",
                        "なぜ同業他社のROE-PBR線上から10%超も割安に放置されているのか(規模・流動性・収益安定性の差か)？",
                        "同業他社との事業ポートフォリオ・時価総額・売買代金・株主還元性向の比較",
                    )

    return make_result(lid, name, status="ok", numbers=numbers, reads=reads, flags=flags)


def lens_l11(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L11", "能力と市場"
    caps = data.get("capacity")
    if not isinstance(caps, list) or not caps:
        return make_result(lid, name, status="入力不足", missing=["capacity"])

    items = []
    flags: list[dict[str, str]] = []
    reads: list[str] = []
    missing = []

    for c in caps:
        if not isinstance(c, dict):
            continue
        req = ("now", "after", "years", "market_cagr")
        if not all(is_num(c.get(k)) for k in req) or c["now"] <= 0 or c["years"] <= 0 or c["market_cagr"] <= 0:
            missing.append(str(c.get("name", "capacity")))
            continue
        now_v = float(c["now"])
        after_v = float(c["after"])
        yrs = float(c["years"])
        mkt = float(c["market_cagr"])
        demand_now = float(c["demand_now"]) if is_num(c.get("demand_now")) and c["demand_now"] > 0 else None

        cap_cagr = ((after_v / now_v) ** (1.0 / yrs) - 1.0) * 100.0
        cap_ratio = cap_cagr / mkt

        req_vol_cagr = (
            ((after_v / demand_now) ** (1.0 / yrs) - 1.0) * 100.0
            if demand_now is not None
            else cap_cagr
        )
        req_ratio = req_vol_cagr / mkt

        item = {
            "name": c.get("name", ""),
            "unit": c.get("unit", ""),
            "now": now_v,
            "after": after_v,
            "when": c.get("when", ""),
            "years": yrs,
            "market_cagr_pct": rnd(mkt, 2),
            "cap_cagr_pct": rnd(cap_cagr, 2),
            "cap_vs_market_ratio": rnd(cap_ratio, 2),
            "demand_now": demand_now,
            "required_vol_cagr_pct": rnd(req_vol_cagr, 2),
            "required_vs_market_ratio": rnd(req_ratio, 2),
        }
        items.append(item)
        reads.append(
            f"{item['name']}: 規模・能力{now_v:g}→{after_v:g}{item['unit']}({yrs:g}年)は年率+{cap_cagr:.1f}%で市場成長率{mkt:.1f}%の{cap_ratio:.2f}倍。"
            + (f"現在水準{demand_now:g}{item['unit']}基準の必要増加年率は+{req_vol_cagr:.1f}%({req_ratio:.2f}倍)。" if demand_now else "")
        )
        if req_ratio > 1.5:
            add_flag(
                flags, lid,
                f"{item['name']}の計画達成に必要な増加年率(+{req_vol_cagr:.1f}%)が市場成長率({mkt:.1f}%)の{req_ratio:.2f}倍(>1.5倍)",
                f"市場成長率を大きく上回る年率+{req_vol_cagr:.1f}%の拡大(シェア獲得・出店余地等)をどの領域・顧客層でどう実現するのか？",
                "顧客・需要側の進捗状況、出店・拡張計画と競合他社の動向",
            )

    if not items:
        return make_result(lid, name, status="入力不足", missing=missing or ["capacity(now,after,years,market_cagr)"])

    return make_result(lid, name, status="ok", missing=missing, numbers={"items": items}, reads=reads, flags=flags)


def lens_l12(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L12", "EPSの漏れ口"
    annual = data.get("annual") or []
    assume = data.get("assume") or {}
    tax_assumed = assume.get("tax")

    last_int = get_rows_with(annual, ["interest", "op"])
    last_tax = get_rows_with(annual, ["pretax", "net"])
    sh_rows = [r for r in get_rows_with(annual, ["shares_m"]) if r["shares_m"] > 0]
    full_eps_rows = [
        r for r in get_rows_with(annual, ["revenue", "net", "shares_m"])
        if r["revenue"] > 0 and r["net"] > 0 and r["shares_m"] > 0
    ]

    if not last_int and not last_tax and len(sh_rows) < 2 and len(full_eps_rows) < 2:
        return make_result(lid, name, status="入力不足", missing=["annual(interest,op,pretax,net,shares_m)"])

    numbers: dict[str, Any] = {}
    reads: list[str] = []
    flags: list[dict[str, str]] = []

    if last_int:
        r = last_int[-1]
        int_ratio = (r["interest"] / r["op"] * 100.0) if r["op"] > 0 else None
        numbers["interest_to_op_pct"] = rnd(int_ratio, 2)
        reads.append(f"直近期({r.get('fy')})の支払利息÷営業利益は{fmt_num(int_ratio, 1)}%。")
        if int_ratio is not None and int_ratio >= 15.0:
            add_flag(
                flags, lid,
                f"支払利息が営業利益の{int_ratio:.1f}%(>=15%)を占め、利益が金利に漏れている",
                "なぜ営業利益に対する金利負担がここまで高いのか(有利子負債水準か調達金利上昇か)？",
                "有価証券報告書の借入金明細・平均利率・返済スケジュールと金利上昇時の感応度",
            )

    if last_tax:
        r = last_tax[-1]
        eff_tax = ((r["pretax"] - r["net"]) / r["pretax"] * 100.0) if r["pretax"] > 0 else None
        numbers["effective_tax_rate_pct"] = rnd(eff_tax, 2)
        reads.append(f"直近期({r.get('fy')})の実効税率((税前−純利)÷税前)は{fmt_num(eff_tax, 1)}%。")
        if eff_tax is not None and is_num(tax_assumed):
            if abs(eff_tax - float(tax_assumed)) > 8.0:
                add_flag(
                    flags, lid,
                    f"実効税率{eff_tax:.1f}%が想定税率{float(tax_assumed):.1f}%±8ptの外にある",
                    "なぜ実効税率が法定税率から大きく乖離しているのか(税額控除・海外子会社税率・繰延税金資産か)？",
                    "有価証券報告書の税効果会計注記(法定実効税率と負担率の差異内訳)",
                )

    if len(sh_rows) >= 2:
        s0, s1 = sh_rows[0], sh_rows[-1]
        try:
            yrs = max(1, int(str(s1.get("fy"))) - int(str(s0.get("fy"))))
        except Exception:
            yrs = len(sh_rows) - 1
        sh_cagr = ((s1["shares_m"] / s0["shares_m"]) ** (1.0 / yrs) - 1.0) * 100.0
        numbers["shares_cagr_pct"] = rnd(sh_cagr, 2)
        numbers["shares_span"] = f"{s0.get('fy')}→{s1.get('fy')}"
        reads.append(f"株数({s0.get('fy')}→{s1.get('fy')}、{yrs}年間)の年率は{sh_cagr:+.2f}%。")
        if sh_cagr > 2.0:
            add_flag(
                flags, lid,
                f"株式数が年率{sh_cagr:+.2f}%(>2%)で増加し希薄化が起きている",
                "なぜ株式数が年2%超のペースで増えているのか(増資・CB・新株予約権か)？",
                "有価証券報告書の株式総数推移・新株発行履歴と資金使途",
            )

    if len(full_eps_rows) >= 2:
        r0, r1 = full_eps_rows[0], full_eps_rows[-1]
        eps0 = r0["net"] / r0["shares_m"]
        eps1 = r1["net"] / r1["shares_m"]
        npm0 = r0["net"] / r0["revenue"]
        npm1 = r1["net"] / r1["revenue"]
        ln_eps = math.log(eps1 / eps0)
        ln_rev = math.log(r1["revenue"] / r0["revenue"])
        ln_npm = math.log(npm1 / npm0)
        ln_sh = math.log(r1["shares_m"] / r0["shares_m"])
        numbers["ln_decomp_span"] = f"{r0.get('fy')}→{r1.get('fy')}"
        numbers["ln_eps_ratio"] = rnd(ln_eps, 4)
        numbers["ln_revenue_ratio"] = rnd(ln_rev, 4)
        numbers["ln_net_margin_ratio"] = rnd(ln_npm, 4)
        numbers["ln_shares_ratio"] = rnd(ln_sh, 4)
        reads.append(
            f"EPS対数分解({r0.get('fy')}→{r1.get('fy')}): ln(EPS比)={ln_eps:+.3f} = "
            f"ln(売上比)({ln_rev:+.3f}) + ln(純利益率比)({ln_npm:+.3f}) − ln(株数比)({ln_sh:+.3f})。"
        )

    return make_result(lid, name, status="ok", numbers=numbers, reads=reads, flags=flags)


def lens_l13(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L13", "投資と回収"
    annual = data.get("annual") or []
    capex_rows = get_rows_with(annual, ["capex", "op"])
    if len(capex_rows) < 2:
        return make_result(lid, name, status="入力不足", missing=["annual(2期以上のcapex,op)"])

    # 直近5期(最大5期)
    recent5 = capex_rows[-5:]
    cum5_capex = sum(float(r["capex"]) for r in recent5)

    # 同じ期間の営業利益の増加 (開始直前期があればそれを基準、なければrecent5の先頭基準)
    first_idx = annual.index(recent5[0])
    prev_op_row = annual[first_idx - 1] if (first_idx > 0 and is_num(annual[first_idx - 1].get("op"))) else recent5[0]
    op_gain = float(recent5[-1]["op"]) - float(prev_op_row["op"])
    inc_roi_pct = (op_gain / cum5_capex * 100.0) if cum5_capex > 0 else None

    dep_rows = get_rows_with(annual, ["capex", "dep"])
    latest_capex_dep = (dep_rows[-1]["capex"] / dep_rows[-1]["dep"]) if (dep_rows and dep_rows[-1]["dep"] > 0) else None

    tat_rows = [r for r in get_rows_with(annual, ["revenue", "assets"]) if r["assets"] > 0]
    tat_first = (tat_rows[0]["revenue"] / tat_rows[0]["assets"]) if tat_rows else None
    tat_last = (tat_rows[-1]["revenue"] / tat_rows[-1]["assets"]) if tat_rows else None
    tat_diff = (tat_last - tat_first) if (tat_first is not None and tat_last is not None and len(tat_rows) >= 2) else None

    op_tat_rows = [
        r for r in get_rows_with(annual, ["revenue", "assets", "cash", "cip"])
        if (float(r["assets"]) - float(r["cash"]) - float(r["cip"])) > 0
    ]
    op_tat_first = (
        float(op_tat_rows[0]["revenue"]) / (float(op_tat_rows[0]["assets"]) - float(op_tat_rows[0]["cash"]) - float(op_tat_rows[0]["cip"]))
        if len(op_tat_rows) >= 2 else None
    )
    op_tat_last = (
        float(op_tat_rows[-1]["revenue"]) / (float(op_tat_rows[-1]["assets"]) - float(op_tat_rows[-1]["cash"]) - float(op_tat_rows[-1]["cip"]))
        if len(op_tat_rows) >= 2 else None
    )
    op_tat_diff = (op_tat_last - op_tat_first) if (op_tat_first is not None and op_tat_last is not None) else None

    latest_assets = tat_rows[-1]["assets"] if tat_rows else None
    cum5_vs_assets_pct = (cum5_capex / latest_assets * 100.0) if (latest_assets and latest_assets > 0) else None
    cum_all_capex = sum(float(r["capex"]) for r in capex_rows)
    cum_all_vs_assets_pct = (cum_all_capex / latest_assets * 100.0) if (latest_assets and latest_assets > 0) else None

    numbers = {
        "window_fys": f"{recent5[0].get('fy')}〜{recent5[-1].get('fy')}",
        "cum5_capex": rnd(cum5_capex, 1),
        "op_base_fy": prev_op_row.get("fy"),
        "op_gain": rnd(op_gain, 1),
        "pretax_incremental_roi_pct": rnd(inc_roi_pct, 2),
        "latest_capex_to_dep": rnd(latest_capex_dep, 2),
        "tat_first_fy": tat_rows[0].get("fy") if tat_rows else None,
        "tat_first": rnd(tat_first, 3),
        "tat_last_fy": tat_rows[-1].get("fy") if tat_rows else None,
        "tat_last": rnd(tat_last, 3),
        "tat_diff": rnd(tat_diff, 3),
        "cum5_capex_pct_of_assets": rnd(cum5_vs_assets_pct, 1),
        "cum_all_capex": rnd(cum_all_capex, 1),
        "cum_all_capex_pct_of_assets": rnd(cum_all_vs_assets_pct, 1),
    }
    if op_tat_diff is not None:
        numbers["op_tat_first_fy"] = op_tat_rows[0].get("fy")
        numbers["op_tat_first"] = rnd(op_tat_first, 3)
        numbers["op_tat_last_fy"] = op_tat_rows[-1].get("fy")
        numbers["op_tat_last"] = rnd(op_tat_last, 3)
        numbers["op_tat_diff"] = rnd(op_tat_diff, 3)

    reads = [
        f"直近{len(recent5)}期({numbers['window_fys']})の設備投資累計は{cum5_capex:,.0f}(全データ{len(capex_rows)}期累計は{cum_all_capex:,.0f})、"
        f"営業利益増加({prev_op_row.get('fy')}→{recent5[-1].get('fy')})は{op_gain:+,.0f}で税前増分利回りは{fmt_num(inc_roi_pct, 1)}%。",
        f"直近期の設備投資÷減価償却は{fmt_num(latest_capex_dep, 2)}倍。"
        + (f"総資産回転率は{tat_rows[0].get('fy')}年{tat_first:.3f}→{tat_rows[-1].get('fy')}年{tat_last:.3f}({tat_diff:+.3f})。" if tat_diff is not None else "")
        + (f"累計投資額は直近総資産の{cum5_vs_assets_pct:.1f}%(全{len(capex_rows)}期累計では{cum_all_vs_assets_pct:.1f}%)。" if cum5_vs_assets_pct is not None else ""),
    ]
    if op_tat_diff is not None:
        reads.append(
            f"(総資産−現預金−建設仮勘定)に対する売上回転率は{op_tat_rows[0].get('fy')}年{op_tat_first:.3f}→{op_tat_rows[-1].get('fy')}年{op_tat_last:.3f}({op_tat_diff:+.3f})。"
        )
        if tat_diff is not None and tat_diff <= 0.02 and op_tat_diff > 0:
            reads.append("回転率の低下は現金と未稼働の設備による。")

    flags: list[dict[str, str]] = []
    heavy_invest = (cum5_vs_assets_pct is not None and cum5_vs_assets_pct > 25.0) or (
        cum_all_vs_assets_pct is not None and cum_all_vs_assets_pct > 25.0
    )
    if heavy_invest and tat_diff is not None and tat_diff <= 0.02 and (op_tat_diff is None or op_tat_diff <= 0):
        pct_disp = cum5_vs_assets_pct if (cum5_vs_assets_pct and cum5_vs_assets_pct > 25.0) else cum_all_vs_assets_pct
        span_disp = f"直近{len(recent5)}期" if (cum5_vs_assets_pct and cum5_vs_assets_pct > 25.0) else f"過去{len(capex_rows)}期"
        add_flag(
            flags, lid,
            f"設備投資累計({span_disp})が直近総資産の{pct_disp:.1f}%(>25%)なのに総資産回転率がほぼ横ばい/未上昇({tat_diff:+.3f})",
            "巨額の設備投資がまだ売上回転に結びついていない理由は何か(建設仮勘定の滞留・立上げ遅れ・単価下落か)？",
            "有価証券報告書の設備の新設等・建設仮勘定残高と主要工場の完工・商業稼働時期",
        )

    return make_result(lid, name, status="ok", numbers=numbers, reads=reads, flags=flags)


def lens_l14(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L14", "キャッシュ"
    annual = data.get("annual") or []

    inv_rows = [
        r for r in get_rows_with(annual, ["inventory", "revenue", "gross"])
        if (r["revenue"] - r["gross"]) > 0
    ]
    ccc_rows = [
        r for r in get_rows_with(annual, ["inventory", "receivables", "payables", "revenue", "gross"])
        if r["revenue"] > 0 and (r["revenue"] - r["gross"]) > 0
    ]
    fcf_rows = get_rows_with(annual, ["ocf", "capex"])

    if not inv_rows and not fcf_rows:
        return make_result(lid, name, status="入力不足", missing=["annual(inventory,ocf,capex)"])

    numbers: dict[str, Any] = {}
    reads: list[str] = []
    flags: list[dict[str, str]] = []

    if inv_rows:
        def inv_days(r: dict[str, Any]) -> float:
            cogs = float(r["revenue"]) - float(r["gross"])
            return float(r["inventory"]) / cogs * 365.0

        d0 = inv_days(inv_rows[0])
        d1 = inv_days(inv_rows[-1])
        diff_days = (d1 - d0) if len(inv_rows) >= 2 else None
        numbers["inv_days_first_fy"] = inv_rows[0].get("fy")
        numbers["inv_days_first"] = rnd(d0, 1)
        numbers["inv_days_last_fy"] = inv_rows[-1].get("fy")
        numbers["inv_days_last"] = rnd(d1, 1)
        numbers["inv_days_diff"] = rnd(diff_days, 1)
        if len(inv_rows) >= 2:
            reads.append(f"在庫日数は{inv_rows[0].get('fy')}年{d0:.1f}日→{inv_rows[-1].get('fy')}年{d1:.1f}日({diff_days:+.1f}日)。")
        else:
            reads.append(f"在庫日数は{inv_rows[-1].get('fy')}年{d1:.1f}日(実績1期のみのため経年差は未算出)。")

        last_r = inv_rows[-1]
        last_inv = float(last_r["inventory"])
        last_cogs = float(last_r["revenue"]) - float(last_r["gross"])
        formula_line = (
            f"在庫日数の式: 期末の在庫 ÷ 売上原価 × 365"
            f"({last_r.get('fy')}年は {last_inv:,.0f} ÷ {last_cogs:,.0f} × 365 = {d1:.1f}日"
        )
        periods = data.get("periods") or {}
        per_year = periods.get("per_year") if isinstance(periods, dict) else None
        p_rows = periods.get("rows") if isinstance(periods, dict) else None
        valid_p_cogs = []
        if isinstance(per_year, int) and per_year > 0 and isinstance(p_rows, list):
            valid_p_cogs = [
                r for r in p_rows
                if isinstance(r, dict) and is_num(r.get("revenue")) and is_num(r.get("gross"))
                and (float(r["revenue"]) - float(r["gross"])) > 0
            ]
        last_inv_only = get_rows_with(annual, ["inventory"])
        if valid_p_cogs and last_inv_only:
            inv_for_p = float(last_inv_only[-1]["inventory"])
            last_p = valid_p_cogs[-1]
            ann_p_cogs = (float(last_p["revenue"]) - float(last_p["gross"])) * float(per_year)
            d_p_ann = inv_for_p / ann_p_cogs * 365.0
            numbers["inv_days_period_label"] = last_p.get("p", "")
            numbers["inv_days_period_annualized"] = rnd(d_p_ann, 1)
            formula_line += f"、直近期{last_p.get('p', '')}の年換算売上原価 {ann_p_cogs:,.0f} 基準では {d_p_ann:.1f}日"
        formula_line += ")。"
        reads.append(formula_line)

        if diff_days is not None and diff_days >= 15.0:
            add_flag(
                flags, lid,
                f"在庫日数が{diff_days:+.1f}日(>=15日)増加している",
                "なぜ在庫回転日数が大きく長期化しているのか(戦略的積み増しか滞留・販売不振か)？",
                "有価証券報告書のたな卸資産内訳(製品・原材料・仕掛品)と需給コメント",
            )

    if ccc_rows:
        r = ccc_rows[-1]
        cogs = float(r["revenue"]) - float(r["gross"])
        dio = float(r["inventory"]) / cogs * 365.0
        dso = float(r["receivables"]) / float(r["revenue"]) * 365.0
        dpo = float(r["payables"]) / cogs * 365.0
        ccc = dio + dso - dpo
        numbers["ccc_last_fy"] = r.get("fy")
        numbers["ccc_days"] = rnd(ccc, 1)
        numbers["dso_days"] = rnd(dso, 1)
        numbers["dpo_days"] = rnd(dpo, 1)
        reads.append(f"CCC({r.get('fy')}年)は{ccc:.1f}日(在庫{dio:.1f}日+債権{dso:.1f}日−債務{dpo:.1f}日)。")

    if fcf_rows:
        r5 = fcf_rows[-5:]
        fcfs = [float(r["ocf"]) - float(r["capex"]) for r in r5]
        cum_fcf = sum(fcfs)
        last_fcf = fcfs[-1]
        numbers["fcf_window_fys"] = f"{r5[0].get('fy')}〜{r5[-1].get('fy')}"
        numbers["fcf_n_years"] = len(r5)
        numbers["fcf_cum"] = rnd(cum_fcf, 1)
        numbers["fcf_last"] = rnd(last_fcf, 1)
        reads.append(
            f"FCF(確認可能{len(r5)}期: {numbers['fcf_window_fys']})の累計は{cum_fcf:+,.0f}、直近期({r5[-1].get('fy')})は{last_fcf:+,.0f}。"
        )
        if cum_fcf < 0:
            add_flag(
                flags, lid,
                f"FCF({numbers['fcf_window_fys']}の{len(r5)}期)累計が{cum_fcf:+,.0f}(<0)とマイナス",
                "なぜフリーキャッシュフローがマイナスなのか(成長投資の前倒しか運転資本膨張か)？",
                "キャッシュ・フロー計算書と大型投資案件の投資回収計画・資金調達手段",
            )

    return make_result(lid, name, status="ok", numbers=numbers, reads=reads, flags=flags)


def lens_l15(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L15", "利益のたまり場"
    segs = data.get("segments")
    if not isinstance(segs, list) or not segs:
        return make_result(lid, name, status="入力不足", missing=["segments"])

    valid = get_rows_with(segs, ["revenue", "profit"])
    if not valid:
        return make_result(lid, name, status="入力不足", missing=["segments(revenue,profit)"])

    tot_rev = sum(float(s["revenue"]) for s in valid)
    tot_prof = sum(float(s["profit"]) for s in valid)
    if tot_rev <= 0 or tot_prof <= 0:
        return make_result(lid, name, status="入力不足", missing=["segments(正の売上・利益合計)"])

    seg_adj = data.get("segment_adjust")
    has_adj = is_num(seg_adj)

    out_segs = []
    high_ratio_names = []
    for s in valid:
        rev_share = float(s["revenue"]) / tot_rev * 100.0
        prof_share = float(s["profit"]) / tot_prof * 100.0
        opm = float(s["profit"]) / float(s["revenue"]) * 100.0
        conc = (prof_share / rev_share) if rev_share > 0 else 0.0
        out_segs.append({
            "name": s.get("name", ""),
            "revenue_share_pct": rnd(rev_share, 1),
            "profit_share_pct": rnd(prof_share, 1),
            "margin_pct": rnd(opm, 2),
            "profit_to_rev_share_ratio": rnd(conc, 2),
        })
        if conc >= 1.3 and prof_share >= 5.0:
            high_ratio_names.append(f"{s.get('name', '')}({conc:.2f}倍)")

    out_segs.sort(key=lambda x: x["profit_to_rev_share_ratio"], reverse=True)
    numbers: dict[str, Any] = {"segments": out_segs, "high_concentration_segments": high_ratio_names}
    if has_adj:
        numbers["segment_adjust"] = rnd(float(seg_adj), 1)

    reads = [
        "セグメント別 利益構成比÷売上構成比: "
        + "、".join(
            f"{s['name']}(売上{s['revenue_share_pct']:.1f}%・利益{s['profit_share_pct']:.1f}%・利益率{s['margin_pct']:.1f}%・倍率{s['profit_to_rev_share_ratio']:.2f}x)"
            for s in out_segs
        )
        + "。"
    ]
    if has_adj:
        adj_f = float(seg_adj)
        reads.append(
            f"セグメント利益合計は{tot_prof:,.0f}、調整額(全社費用等)は{adj_f:+,.0f}、連結調整後は{tot_prof + adj_f:,.0f}(構成比は調整額を除くセグメント合計で算出)。"
        )

    flags: list[dict[str, str]] = []
    if high_ratio_names:
        add_flag(
            flags, lid,
            f"利益構成比÷売上構成比が1.3倍以上の稼ぎ頭セグメント: {'、'.join(high_ratio_names)}",
            "なぜこのセグメントに利益が集中しているのか(参入障壁・独自技術か一過性の好採算か)？",
            "有価証券報告書のセグメント別の主力製品・顧客構成・競合環境と設備投資配分",
        )

    return make_result(lid, name, status="ok", numbers=numbers, reads=reads, flags=flags)


def _normalize_sens_name(raw_name: str) -> str:
    """'+1pt' / '-1pt' や括弧内変動を束ねる基底名を返す。"""
    s = raw_name.strip()
    # 末尾の括弧 (EPS +21%) 等を除去して基底名を見る
    base = re.sub(r"[（(][^()（）]*[+-−][^()（）]*[)）]", "", s).strip()
    # +30t, −30t, +1pt, -10% などの符号付き変化量を除く
    base = re.sub(r"\s*[+＋\-−]\s*\d+(?:\.\d+)?\s*(?:pt|%|％|t|円)?", "", base).strip()
    return base if base else s


def lens_l16(_data: dict[str, Any], val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L16", "感応度の換算"
    if val is None:
        return make_result(
            lid,
            name,
            status="対象外",
            reads=["valuation.json がまだ無い。価値評価(工程5)の後に実行し直す"],
        )
    if not isinstance(val.get("sensitivities"), list) or not val["sensitivities"]:
        return make_result(lid, name, status="入力不足", missing=["valuation.json:sensitivities"])

    raw_items = [x for x in val["sensitivities"] if isinstance(x, dict) and is_num(x.get("diff")) and x.get("name")]
    if not raw_items:
        return make_result(lid, name, status="入力不足", missing=["valuation.json:sensitivities"])

    grouped: dict[str, dict[str, Any]] = {}
    for x in raw_items:
        rname = str(x["name"])
        gname = _normalize_sens_name(rname)
        adiff = abs(float(x["diff"]))
        has_pair_sign = bool(re.search(r"[+＋\-−]\s*\d", rname))
        if gname not in grouped:
            grouped[gname] = {
                "name": gname,
                "max_abs_diff": adiff,
                "signed_diffs": [float(x["diff"])],
                "raw_names": [rname],
                "is_paired": False,
            }
        else:
            grouped[gname]["signed_diffs"].append(float(x["diff"]))
            grouped[gname]["raw_names"].append(rname)
            grouped[gname]["is_paired"] = True
            if adiff > grouped[gname]["max_abs_diff"]:
                grouped[gname]["max_abs_diff"] = adiff
        if has_pair_sign and len(grouped[gname]["raw_names"]) >= 2:
            grouped[gname]["is_paired"] = True

    all_ranked = sorted(grouped.values(), key=lambda g: g["max_abs_diff"], reverse=True)

    # 事業変数の単一ドライバーと、機械的一律EPS変動・複合歴史シナリオを区別
    def is_stress_or_mechanical(gname: str) -> bool:
        return (
            gname.startswith("EPS")
            or ("型" in gname)
            or ("反落" in gname)
            or ("ショック" in gname)
            or ("シナリオ" in gname)
        )

    driver_ranked = [g for g in all_ranked if not is_stress_or_mechanical(g["name"])]
    target_list = driver_ranked if len(driver_ranked) >= 2 else all_ranked

    top1 = target_list[0]
    ratios_vs_top1 = []
    for other in target_list[1:]:
        ratio = top1["max_abs_diff"] / other["max_abs_diff"] if other["max_abs_diff"] > 0 else None
        ratios_vs_top1.append({
            "name": other["name"],
            "abs_diff": rnd(other["max_abs_diff"], 1),
            "top1_div_other": rnd(ratio, 2),
        })

    top2 = target_list[1] if len(target_list) >= 2 else None
    top1_vs_top2 = (top1["max_abs_diff"] / top2["max_abs_diff"]) if (top2 and top2["max_abs_diff"] > 0) else None

    # ペア(±対)の中での順位も把握
    paired_drivers = [g for g in target_list if g["is_paired"]]
    pair_ratio = None
    pair_second = None
    if len(paired_drivers) >= 2 and paired_drivers[1]["max_abs_diff"] > 0:
        pair_second = paired_drivers[1]
        pair_ratio = paired_drivers[0]["max_abs_diff"] / pair_second["max_abs_diff"]

    numbers = {
        "core_candidate": top1["name"],
        "core_abs_diff": rnd(top1["max_abs_diff"], 1),
        "driver_ranking": [
            {"name": g["name"], "abs_diff": rnd(g["max_abs_diff"], 1), "is_paired": g["is_paired"]}
            for g in target_list
        ],
        "all_ranking": [
            {"name": g["name"], "abs_diff": rnd(g["max_abs_diff"], 1), "is_paired": g["is_paired"]}
            for g in all_ranked
        ],
        "ratios_vs_top1": ratios_vs_top1,
        "top1_to_top2_ratio": rnd(top1_vs_top2, 2),
        "paired_second_name": pair_second["name"] if pair_second else None,
        "top1_to_paired_second_ratio": rnd(pair_ratio, 2),
    }

    sign_prefix = "±" if top1["is_paired"] else ""
    reads = [
        f"価値の芯の候補は「{top1['name']}」({sign_prefix}{top1['max_abs_diff']:.0f}円)。"
    ]
    if top2:
        reads.append(
            f"事業ドライバー2位「{top2['name']}」({top2['max_abs_diff']:.1f}円)の{top1_vs_top2:.2f}倍"
            + (
                f"、対称ドライバー2位「{pair_second['name']}」(±{pair_second['max_abs_diff']:.1f}円)の約{pair_ratio:.1f}倍。"
                if pair_second and pair_second is not top2
                else "。"
            )
        )
    if all_ranked[0] is not top1:
        reads.append(f"なお複合/一律ショック最大は「{all_ranked[0]['name']}」({all_ranked[0]['max_abs_diff']:.1f}円)。")

    flags: list[dict[str, str]] = []
    if top1_vs_top2 is not None and top1_vs_top2 >= 1.5:
        add_flag(
            flags, lid,
            f"感応度1位「{top1['name']}」({sign_prefix}{top1['max_abs_diff']:.0f}円)が2位の{top1_vs_top2:.2f}倍(>=1.5倍)で、価値の芯が1つに絞れる",
            f"価値を最も動かす「{top1['name']}」の前提は保守的か楽観的か、改善・悪化の具体的ドライバーは何か？",
            "事業別の原価・売価・ミックス変動履歴と価格改定/数量成長の実績開示",
        )

    return make_result(lid, name, status="ok", numbers=numbers, reads=reads, flags=flags)


def lens_l17(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L17", "流動性"
    price = data.get("price") or {}
    adv = price.get("adv")
    positions = price.get("positions")
    unit = data.get("unit", "百万円")

    missing = []
    if not is_num(adv) or adv <= 0:
        missing.append("price.adv")
    if not isinstance(positions, list) or not any(is_num(p) for p in positions):
        missing.append("price.positions")
    if missing:
        return make_result(lid, name, status="入力不足", missing=missing)

    daily_cap = float(adv) * 0.20
    pos_days = []
    for p in positions:
        if is_num(p):
            days = float(p) / daily_cap
            pos_days.append({"position": float(p), "days": rnd(days, 2)})

    max_pos = max(pos_days, key=lambda x: x["days"])
    numbers = {
        "adv": float(adv),
        "participation_rate_pct": 20.0,
        "daily_20pct_capacity": rnd(daily_cap, 2),
        "positions_days": pos_days,
        "max_days": max_pos["days"],
    }
    reads = [
        f"1日売買代金{float(adv):g}{unit}の20%参加({daily_cap:.2f}{unit}/日)で算出: "
        + "、".join(f"{x['position']:g}{unit}は{x['days']:.1f}日" for x in pos_days)
        + "。"
    ]

    flags: list[dict[str, str]] = []
    if max_pos["days"] > 20.0:
        add_flag(
            flags, lid,
            f"最大想定ポジション({max_pos['position']:g}{unit})の執行に{max_pos['days']:.1f}日(>20日)を要し流動性がタイト",
            "流動性が低い中でポジションを建てた後、イベント時の撤退や段階的売却が可能か？",
            "直近6か月・1年の出来高/売買代金推移と大株主構成(浮動株比率)",
        )

    return make_result(lid, name, status="ok", numbers=numbers, reads=reads, flags=flags)


def lens_l18(data: dict[str, Any], val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L18", "価値の橋"
    assume = data.get("assume") or {}
    price = data.get("price") or {}
    model = data.get("model") or []

    coe = assume.get("coe")
    close = price.get("close")
    eps_next = price.get("eps_next")

    missing = []
    if not is_num(close) or close <= 0:
        missing.append("price.close")
    if not is_num(eps_next):
        missing.append("price.eps_next")
    if not is_num(coe) or coe <= 0:
        missing.append("assume.coe")
    if missing:
        return make_result(lid, name, status="入力不足", missing=missing)

    coe_f = float(coe)
    close_f = float(close)
    eps_f = float(eps_next)

    steady_val = eps_f / (coe_f / 100.0)
    implied_eps = close_f * (coe_f / 100.0)
    implied_eps_diff_pct = ((implied_eps - eps_f) / abs(eps_f) * 100.0) if eps_f != 0 else None

    base_m = find_base_scenario(model)
    model_roe = None
    if base_m:
        if is_num(base_m.get("net")) and is_num(base_m.get("equity")) and base_m["equity"] > 0:
            model_roe = float(base_m["net"]) / float(base_m["equity"]) * 100.0
        elif is_num(base_m.get("roe")):
            model_roe = float(base_m["roe"])
    roe_spread_pt = (model_roe - coe_f) if model_roe is not None else None

    b_val = None
    if isinstance(val, dict):
        entry = val.get("entry")
        if isinstance(entry, dict) and is_num(entry.get("B")):
            b_val = float(entry["B"])

    current_power_gap = steady_val - close_f

    if eps_f > 0 and implied_eps_diff_pct is not None:
        if implied_eps_diff_pct < 0:
            eps_dir = f"今より {abs(implied_eps_diff_pct):.1f}% 低い"
        elif implied_eps_diff_pct > 0:
            eps_dir = f"今より {implied_eps_diff_pct:.1f}% 高い"
        else:
            eps_dir = "今と同水準"
        eps_clause = f"株価は EPS が {implied_eps:,.1f}円({eps_dir})で続くことを前提にしている"
    else:
        eps_clause = f"株価は EPS が {implied_eps:,.1f}円で続くことを前提にしている"

    numbers: dict[str, Any] = {
        "close": rnd(close_f, 1),
        "eps_next": rnd(eps_f, 2),
        "coe_pct": rnd(coe_f, 2),
        "steady_state_value": rnd(steady_val, 1),
        "current_power_gap": rnd(current_power_gap, 1),
        "implied_sustained_eps": rnd(implied_eps, 2),
        "implied_eps_vs_next_pct": rnd(implied_eps_diff_pct, 1),
        "model_base_roe_pct": rnd(model_roe, 2),
        "roe_spread_vs_coe_pt": rnd(roe_spread_pt, 2),
    }

    reads: list[str] = []
    flags: list[dict[str, str]] = []

    if b_val is not None:
        total_gap = b_val - close_f
        growth_add = b_val - steady_val
        current_power_share_pct = (current_power_gap / total_gap * 100.0) if total_gap != 0 else None
        growth_add_share_pct = (growth_add / total_gap * 100.0) if total_gap != 0 else None

        numbers["theoretical_price_B"] = rnd(b_val, 1)
        numbers["total_gap"] = rnd(total_gap, 1)
        numbers["growth_add"] = rnd(growth_add, 1)
        numbers["current_power_share_pct"] = rnd(current_power_share_pct, 1)
        numbers["growth_add_share_pct"] = rnd(growth_add_share_pct, 1)

        if total_gap > 0 and current_power_share_pct is not None and growth_add_share_pct is not None:
            reads.append(
                f"現在値 {close_f:,.0f}円 → 今の利益が続く場合 {steady_val:,.0f}円({current_power_gap:+,.0f}円、差の {current_power_share_pct:.1f}%)"
                f"→ 理論株価 {b_val:,.0f}円(成長と変化の上乗せ {growth_add:+,.0f}円、差の {growth_add_share_pct:.1f}%)。"
                f"{eps_clause}。"
            )
        else:
            reads.append(
                f"現在値 {close_f:,.0f}円 → 今の利益が続く場合 {steady_val:,.0f}円({current_power_gap:+,.0f}円)"
                f"→ 理論株価 {b_val:,.0f}円(成長と変化の上乗せ {growth_add:+,.0f}円、合計差 {total_gap:+,.0f}円)。"
                f"{eps_clause}。"
            )
        if roe_spread_pt is not None:
            reads.append(
                f"モデル基準シナリオ最終年のROEは{model_roe:.2f}%で、資本コスト({coe_f:.2f}%)との開きは{roe_spread_pt:+.2f}pt。"
            )

        if total_gap > 0 and current_power_share_pct is not None and current_power_share_pct >= 60.0:
            add_flag(
                flags, lid,
                "差の大半は、今の利益が続くだけで埋まる。論点は成長ではなく持続性",
                "なぜ市場は今の利益が続かないと見ているのか",
                "過去の利益の反落の履歴と、今回それが起きない根拠",
            )
        if total_gap > 0 and growth_add_share_pct is not None and growth_add_share_pct >= 60.0:
            add_flag(
                flags, lid,
                "差の大半は成長の実現。論点は段差の確度",
                "どの成長ドライバーの段差がいつ実現し、その確度はどの程度か",
                "中期経営計画・設備増強計画と顧客採用・受注の進捗",
            )
        if roe_spread_pt is not None and abs(roe_spread_pt) <= 1.0:
            add_flag(
                flags, lid,
                "ROE が資本コストとほぼ同じで、成長は価値をほとんど生まない。価値を生むのは ROE の上昇(利益率・資本の返還)",
                "利益率の引き上げか資本の返還でROEを資本コスト以上に高められるか",
                "中期経営計画のROE目標・利益率改善策と株主還元・資本配分方針",
            )
        if steady_val < close_f and b_val > close_f:
            add_flag(
                flags, lid,
                "今の利益が続くだけでは株価に届かない。株価はすでに成長を前提にしている",
                "市場がすでに織り込んでいる成長ペースをさらに上回る根拠はあるか",
                "株価が織り込む成長率・EPS水準と事業エンジンの成長見通しの比較",
            )
    else:
        reads.append(
            f"現在値 {close_f:,.0f}円 → 今の利益が続く場合 {steady_val:,.0f}円({current_power_gap:+,.0f}円)。{eps_clause}。"
        )
        if roe_spread_pt is not None:
            reads.append(
                f"モデル基準シナリオ最終年のROEは{model_roe:.2f}%で、資本コスト({coe_f:.2f}%)との開きは{roe_spread_pt:+.2f}pt。"
            )
        if steady_val >= close_f * 1.20:
            upside_pct = (steady_val - close_f) / close_f * 100.0
            add_flag(
                flags, lid,
                f"今の利益が続くだけで株価を {upside_pct:.1f}% 上回る",
                "なぜ市場は今の利益が続かないと見ているのか",
                "過去の利益の反落の履歴と、今回それが起きない根拠",
            )
        if steady_val < close_f:
            add_flag(
                flags, lid,
                "今の利益が続くだけでは株価に届かない。株価はすでに成長を前提にしている",
                "市場がすでに織り込んでいる成長ペースをさらに上回る根拠はあるか",
                "株価が織り込む成長率・EPS水準と事業エンジンの成長見通しの比較",
            )

    return make_result(lid, name, status="ok", numbers=numbers, reads=reads, flags=flags)


def lens_l19(data: dict[str, Any], _val: dict[str, Any] | None) -> dict[str, Any]:
    lid, name = "L19", "会社予想と計画の癖"
    gh_raw = data.get("guidance_history") or []
    ph_raw = data.get("plan_history") or []

    gh_rows = [
        r for r in (gh_raw if isinstance(gh_raw, list) else [])
        if isinstance(r, dict) and is_num(r.get("initial_op")) and r["initial_op"] != 0 and is_num(r.get("actual_op"))
    ]
    ph_rows = [
        r for r in (ph_raw if isinstance(ph_raw, list) else [])
        if isinstance(r, dict) and is_num(r.get("target_op")) and r["target_op"] > 0 and is_num(r.get("actual_op"))
    ]

    if len(gh_rows) < 3 and not ph_rows:
        missing = []
        if len(gh_rows) < 3:
            missing.append("guidance_history(3期以上)")
        if not ph_rows:
            missing.append("plan_history")
        return make_result(lid, name, status="入力不足", missing=missing)

    numbers: dict[str, Any] = {}
    reads: list[str] = []
    flags: list[dict[str, str]] = []
    missing_partial: list[str] = []

    if len(gh_rows) >= 3:
        gh_items = []
        diffs = []
        for r in gh_rows:
            init_op = float(r["initial_op"])
            act_op = float(r["actual_op"])
            diff_pct = (act_op - init_op) / abs(init_op) * 100.0
            diffs.append(diff_pct)
            gh_items.append({
                "fy": str(r.get("fy", "")),
                "initial_op": rnd(init_op, 1),
                "actual_op": rnd(act_op, 1),
                "surprise_pct": rnd(diff_pct, 1),
            })
        n_total = len(diffs)
        n_beat = sum(1 for d in diffs if d > 0)
        n_miss = sum(1 for d in diffs if d < 0)
        beat_ratio = n_beat / n_total
        miss_ratio = n_miss / n_total
        mean_diff = sum(diffs) / n_total
        median_diff = statistics.median(diffs)

        numbers["guidance_history"] = gh_items
        numbers["n_guidance_periods"] = n_total
        numbers["n_beat"] = n_beat
        numbers["n_miss"] = n_miss
        numbers["beat_ratio_pct"] = rnd(beat_ratio * 100.0, 1)
        numbers["mean_surprise_pct"] = rnd(mean_diff, 1)
        numbers["median_surprise_pct"] = rnd(median_diff, 1)

        reads.append(
            f"期初予想に対し、過去 {n_total}期のうち {n_beat}期で実績が上回った"
            f"(中央値 {median_diff:+.1f}%、平均 {mean_diff:+.1f}%)。"
        )
        if beat_ratio >= 0.8:
            add_flag(
                flags, lid,
                "会社予想は保守的に出す癖がある(今期の予想も同じ読み方ができるかを、前提の逆算 L05 と合わせて確かめる)",
                "なぜ期初予想が保守的になりやすいのか(期中の上方修正の傾向か一過性要因か)？",
                "過去の期初予想と実績・修正開示の推移および今期予想の前提条件",
            )
        if miss_ratio >= 0.6:
            add_flag(
                flags, lid,
                "会社予想は未達の癖がある。計画の確率を下げる",
                "なぜ期初予想が未達になりやすいのか(市場見通しの甘さか期中リスクの過小評価か)？",
                "過去の期初予想の下方修正理由と今期計画の達成条件",
            )
    elif gh_raw:
        missing_partial.append("guidance_history(3期以上)")

    if ph_rows:
        plan_items = []
        missed_plans = []
        for r in ph_rows:
            tgt = float(r["target_op"])
            act = float(r["actual_op"])
            ach_pct = act / tgt * 100.0
            item = {
                "name": str(r.get("name", "")),
                "fy": str(r.get("fy", "")),
                "target_op": rnd(tgt, 1),
                "actual_op": rnd(act, 1),
                "achievement_pct": rnd(ach_pct, 1),
            }
            plan_items.append(item)
            if ach_pct < 80.0:
                missed_plans.append(item)
        numbers["plan_history"] = plan_items
        plan_txt = "、".join(
            f"{it['name'] or it['fy']}({it['fy']}年): 目標{it['target_op']:,.0f}→実績{it['actual_op']:,.0f}(達成率{it['achievement_pct']:.1f}%)"
            for it in plan_items
        )
        reads.append(f"過去の中計等の達成状況: {plan_txt}。")
        if missed_plans:
            add_flag(
                flags, lid,
                "前の中計は未達。今の中計の確率の出発点(基準率)を下げる",
                "前の中計が目標に届かなかった主因は解消されたのか、今の中計でも同じ楽観が残っていないか？",
                "前の中計の未達要因の総括と、今の中計の前提条件・達成確率の見直し",
            )

    return make_result(lid, name, status="ok", missing=missing_partial, numbers=numbers, reads=reads, flags=flags)


LENSES: list[tuple[str, str, Callable[[dict[str, Any], dict[str, Any] | None], dict[str, Any]]]] = [
    ("L01", "利益の増減", lens_l01),
    ("L02", "加速度", lens_l02),
    ("L03", "限界利益率と損益分岐点", lens_l03),
    ("L04", "外部要因と自然実験", lens_l04),
    ("L05", "会社予想の逆算", lens_l05),
    ("L06", "年換算と計画", lens_l06),
    ("L07", "デュポン", lens_l07),
    ("L08", "資本の使い道", lens_l08),
    ("L09", "織り込みROEと成長の値段", lens_l09),
    ("L10", "同業の線", lens_l10),
    ("L11", "能力と市場", lens_l11),
    ("L12", "EPSの漏れ口", lens_l12),
    ("L13", "投資と回収", lens_l13),
    ("L14", "キャッシュ", lens_l14),
    ("L15", "利益のたまり場", lens_l15),
    ("L16", "感応度の換算", lens_l16),
    ("L17", "流動性", lens_l17),
    ("L18", "価値の橋", lens_l18),
    ("L19", "会社予想と計画の癖", lens_l19),
]


# ---------------------------------------------------------------------------
# レポート生成・メイン
# ---------------------------------------------------------------------------

def render_markdown(output: dict[str, Any]) -> str:
    meta = output["meta"]
    summary = output["summary"]
    all_flags = output["flags"]
    lenses = output["lenses"]

    lines: list[str] = []
    title_name = f"{meta['name']}({meta['ticker']})" if meta.get("ticker") else (meta.get("name") or "分析対象")
    lines.append(f"# {title_name} レンズ分析レポート")
    lines.append("")
    lines.append(
        f"レンズ ok {summary['ok']} / 入力不足 {summary['missing']} / "
        f"対象外 {summary['skipped']} / 旗 {summary['flags']} (単位: {meta.get('unit', '')})"
    )
    lines.append("")
    lines.append("## 示唆の種(旗)の一覧")
    lines.append("")
    if all_flags:
        lines.append("| id | 旗 | 問い | 確かめ方 |")
        lines.append("|---|---|---|---|")
        for f in all_flags:
            lines.append(
                f"| {f['id']} | {f['text']} | {f['question']} | {f['check']} |"
            )
    else:
        lines.append("（立った旗はありません）")
    lines.append("")
    lines.append("## レンズ別の詳細")
    lines.append("")

    for res in lenses:
        lines.append(f"### {res['id']} {res['name']} [{res['status']}]")
        if res["status"] == "入力不足" and res["missing"]:
            lines.append(f"- 不足入力: {', '.join(res['missing'])}")
        for rd in res["reads"]:
            lines.append(f"- {rd}")
        if res["numbers"]:
            compact = json.dumps(res["numbers"], ensure_ascii=False)
            lines.append(f"- 主な数字: `{compact}`")
        if res["flags"]:
            for fl in res["flags"]:
                lines.append(f"- **旗 {fl['id']}**: {fl['text']} / 問い: {fl['question']} / 確かめ方: {fl['check']}")
        lines.append("")

    return "\n".join(lines)


def run_lenses(work_dir: Path) -> dict[str, Any]:
    series_path = work_dir / "series.json"
    if not series_path.exists():
        raise FileNotFoundError(f"series.json が見つかりません: {series_path}")

    with series_path.open("r", encoding="utf-8") as f:
        raw_series = json.load(f)
    data = strip_help(raw_series)
    if not isinstance(data, dict):
        data = {}

    val_path = work_dir / "valuation.json"
    val_data = None
    if val_path.exists():
        with val_path.open("r", encoding="utf-8") as f:
            val_data = json.load(f)

    skip_map = data.get("skip") if isinstance(data.get("skip"), dict) else {}

    results: list[dict[str, Any]] = []
    all_flags: list[dict[str, str]] = []
    cnt_ok = 0
    cnt_missing = 0
    cnt_skip = 0

    for lid, lname, fn in LENSES:
        if lid in skip_map:
            reason = str(skip_map[lid])
            res = make_result(lid, lname, status="対象外", reads=[f"対象外: {reason}"])
            cnt_skip += 1
        else:
            try:
                res = fn(data, val_data)
            except Exception as exc:
                res = make_result(lid, lname, status="入力不足", missing=[f"計算エラー: {exc}"])
            if res["status"] == "ok":
                cnt_ok += 1
            elif res["status"] == "入力不足":
                cnt_missing += 1
            else:
                cnt_skip += 1
        results.append(res)
        all_flags.extend(res["flags"])

    output = {
        "meta": {
            "ticker": str(data.get("ticker", "")),
            "name": str(data.get("name", "")),
            "unit": str(data.get("unit", "百万円")),
        },
        "summary": {
            "ok": cnt_ok,
            "missing": cnt_missing,
            "skipped": cnt_skip,
            "flags": len(all_flags),
        },
        "flags": all_flags,
        "lenses": results,
    }

    json_out = work_dir / "lenses.json"
    md_out = work_dir / "lenses.md"
    with json_out.open("w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    with md_out.open("w", encoding="utf-8") as f:
        f.write(render_markdown(output))

    return output


def main() -> int:
    if len(sys.argv) < 2:
        print("使い方: py -3 lenses.py <作業フォルダ>", file=sys.stderr)
        return 1
    work_dir = Path(sys.argv[1]).resolve()
    try:
        output = run_lenses(work_dir)
    except Exception as exc:
        print(f"エラー: {exc}", file=sys.stderr)
        return 1

    s = output["summary"]
    print(f"レンズ ok {s['ok']} / 入力不足 {s['missing']} / 対象外 {s['skipped']} / 旗 {s['flags']}")
    for fl in output["flags"]:
        print(f"{fl['id']}: {fl['text']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
