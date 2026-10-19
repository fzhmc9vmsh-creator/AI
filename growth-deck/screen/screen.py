#!/usr/bin/env python3
"""Step 3: 一次ふるい。ネットワーク不要(data/ のキャッシュと為替を読むだけ)。

判定:
  g2   = (EPS_+1y平均 / 実績年EPS)^(1/2) - 1   (2年CAGR)
  g1f  = EPS_+1y平均 / EPS_0y平均 - 1          (来期の伸び。底からの反発で g2 だけ膨らむのを防ぐ)
  g    = min(g2, g1f)
  PE   = 株価 / ((EPS_0y + EPS_+1y) / 2)        (株価 = trailingPE x trailingEps。
         yfinance の forwardPE/forwardEps は分割前の値などで壊れていることがあるため使わない。
         予想EPSの通貨が株価の通貨と違う場合(香港上場の中国企業など)は為替で換算する)
  PEG  = PE / (g x 100)
  合格 pass     : g >= 31% かつ PEG <= 0.75
  境界 borderline: g >= 22% かつ PEG <= 1.00 (合格以外。二次審査で厳しく見るので網は広めに取る)
  共通の必須条件: 実績EPS > 0, 予想EPS(0y, +1y) > 0, 時価総額 >= 2億USD, アナリスト数 >= 1
  不合格 fail   : 上の条件を満たさない (理由を reasons に残す)
  欠損 missing  : 判定に必要な値が無く、ほかに不合格理由が無い
  取得失敗 error: キャッシュが無い (fetch 段階で失敗)

循環フラグ cyclical_flag=1 は除外せず印だけ付ける(業種による機械的判定、人が見直す)。

出力: out/pass.csv, out/borderline.csv, out/all_scored.csv, out/summary.md
"""
import argparse
import csv
import datetime as dt
import json
import math
from pathlib import Path

from fetch import cache_path
from universe import DATA, HERE, log

OUT = HERE / "out"
G2_PASS, PEG_PASS = 0.31, 0.75
G2_BORDER, PEG_BORDER = 0.22, 1.00
MCAP_USD_MIN = 2e8
ANALYSTS_MIN = 1
MARKET_ORDER = ["JP", "US", "HK", "SH", "SG", "ID", "TH", "MY"]
TOP_N = 50

CYCLICAL_SECTORS = {"Energy", "Basic Materials"}
CYCLICAL_INDUSTRY_KEYS = [
    "bank", "insurance", "auto", "steel", "chemical", "aluminum", "copper", "metal",
    "memory", "engineering & construction", "heavy", "construction", "shipping", "marine", "airline",
]

COLS = ["ticker", "name", "market", "status", "reasons", "missing", "cyclical_flag", "currency",
        "sector", "industry", "mcap_local_mn", "mcap_usd_mn", "fx_local_per_usd",
        "eps_trailing_local", "eps_0y_avg_local", "eps_1y_avg_local", "eps_base_yearago_local",
        "g2_eps_cagr_pct", "g1f_eps_growth_pct", "g_used_pct", "g5y_eps_growth_pct", "price_local",
        "est_currency", "forward_pe_x", "peg_x", "analysts_1y_n",
        "revenue_1y_avg_mn_local", "fetched_at", "data_source"]


def num(x):
    if x is None or isinstance(x, bool):
        return None
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return None if (math.isnan(v) or math.isinf(v)) else v


def cyclical_flag(sector, industry):
    s, i = (sector or ""), (industry or "").lower()
    if s in CYCLICAL_SECTORS:
        return 1
    if s == "Real Estate" and "development" in i:  # 不動産開発
        return 1
    return 1 if any(k in i for k in CYCLICAL_INDUSTRY_KEYS) else 0


def evaluate(u, d, rates):
    """u: universe 行, d: キャッシュ内容。判定結果の dict を返す。"""
    cur = d.get("currency") or ""
    fx = num(rates.get(cur))
    mcap_local = num(d.get("marketCap"))
    mcap_usd = mcap_local / fx if (mcap_local is not None and fx) else None
    ee = d.get("earnings_estimate") or {}
    e0, e1 = ee.get("0y") or {}, ee.get("+1y") or {}
    eps_tr = num(d.get("trailingEps"))
    eps0, eps1 = num(e0.get("avg")), num(e1.get("avg"))
    base = num(e0.get("yearAgoEps"))          # 実績年のEPS(0y行のyearAgoEps)
    base_from_trailing = base is None and num(d.get("trailingEps")) is not None
    est_cur = e1.get("currency") or e0.get("currency") or cur
    if est_cur != cur:                        # 予想EPSを株価の通貨に換算
        fx_est = num(rates.get(est_cur))
        conv = (fx / fx_est) if (fx and fx_est) else None
        eps0, eps1, base = [(v * conv if (v is not None and conv) else None) for v in (eps0, eps1, base)]
    if base_from_trailing:                    # 実績年EPSが無いときは直近12か月EPSで代用(株価通貨)
        base = eps_tr
    an1 = num(e1.get("numberOfAnalysts"))
    tpe = num(d.get("trailingPE"))
    price = tpe * eps_tr if (tpe and eps_tr and tpe > 0 and eps_tr > 0) else None
    if price is None:
        fpe0, feps = num(d.get("forwardPE")), num(d.get("forwardEps"))
        price = fpe0 * feps if (fpe0 and feps and fpe0 > 0 and feps > 0) else None
    fpe = None
    if price is not None and eps0 is not None and eps1 is not None and (eps0 + eps1) > 0:
        fpe = price / ((eps0 + eps1) / 2)
    g5 = num(((d.get("growth_estimates") or {}).get("stock") or {}).get("+5y"))
    rev1 = num(((d.get("revenue_estimate") or {}).get("+1y") or {}).get("avg"))

    fails, missing = [], []

    if mcap_local is None:
        missing.append("marketCap")
    elif fx is None:
        missing.append(f"為替({cur})")
    elif mcap_usd < MCAP_USD_MIN:
        fails.append("時価総額<2億USD")

    for name, v in [("実績EPS", eps_tr), ("予想EPS(0y)", eps0), ("予想EPS(+1y)", eps1)]:
        if v is None:
            missing.append(name)
        elif v <= 0:
            fails.append(f"{name}<=0(赤字)")

    if an1 is None:
        missing.append("アナリスト数(+1y)")
    elif an1 < ANALYSTS_MIN:
        fails.append("アナリスト数<1")

    if base is None:
        missing.append("yearAgoEps(0y)")
    elif base <= 0:
        fails.append("基準EPS<=0(CAGR計算不能)")

    if fpe is None:
        missing.append("株価または予想EPS")
    elif fpe <= 0:
        fails.append("予想PE<=0")

    g2 = None
    if base is not None and base > 0 and eps1 is not None and eps1 > 0:
        g2 = (eps1 / base) ** 0.5 - 1
    g1f = (eps1 / eps0 - 1) if (eps0 is not None and eps0 > 0 and eps1 is not None) else None
    g = min(g2, g1f) if (g2 is not None and g1f is not None) else None
    peg = None
    if g is not None and g > 0 and fpe is not None and fpe > 0:
        peg = fpe / (g * 100)
    if g is not None:
        if g < G2_BORDER:
            fails.append("EPS成長<22%" + ("(来期)" if g1f is not None and g1f < g2 else ""))
        elif peg is not None and peg > PEG_BORDER:
            fails.append("PEG>1.00")

    if fails:
        status = "fail"
    elif missing:
        status = "missing"
    elif g >= G2_PASS and peg <= PEG_PASS:
        status = "pass"
    elif g >= G2_BORDER and peg <= PEG_BORDER:
        status = "borderline"
    else:  # ここには来ない想定の保険
        status = "fail"
        fails.append("境界外")

    reasons = ""
    if status == "fail":
        reasons = ";".join(fails)
    elif status == "missing":
        reasons = "欠損のため判定不能"
    elif status == "borderline":
        notes = []
        if g < G2_PASS:
            notes.append("EPS成長22-31%")
        if peg > PEG_PASS:
            notes.append("PEG 0.75-1.00")
        reasons = ";".join(notes)

    def r(x, nd):
        return None if x is None else round(x, nd)

    return {
        "ticker": u["ticker"], "name": u.get("name") or d.get("shortName") or "",
        "market": u.get("market", ""), "status": status, "reasons": reasons,
        "missing": ";".join(missing), "cyclical_flag": cyclical_flag(d.get("sector"), d.get("industry")),
        "currency": cur, "sector": d.get("sector") or "", "industry": d.get("industry") or "",
        "mcap_local_mn": r(mcap_local / 1e6 if mcap_local is not None else None, 1),
        "mcap_usd_mn": r(mcap_usd / 1e6 if mcap_usd is not None else None, 1),
        "fx_local_per_usd": fx,
        "eps_trailing_local": eps_tr, "eps_0y_avg_local": eps0, "eps_1y_avg_local": eps1,
        "eps_base_yearago_local": base,
        "g2_eps_cagr_pct": r(g2 * 100 if g2 is not None else None, 2),
        "g1f_eps_growth_pct": r(g1f * 100 if g1f is not None else None, 2),
        "g_used_pct": r(g * 100 if g is not None else None, 2),
        "g5y_eps_growth_pct": r(g5 * 100 if g5 is not None else None, 2),
        "price_local": r(price, 3), "est_currency": est_cur,
        "forward_pe_x": r(fpe, 2), "peg_x": r(peg, 3), "analysts_1y_n": an1,
        "revenue_1y_avg_mn_local": r(rev1 / 1e6 if rev1 is not None else None, 1),
        "fetched_at": d.get("fetched_at", ""), "data_source": d.get("source", ""),
    }


def error_row(u, msg):
    return {"ticker": u["ticker"], "name": u.get("name", ""), "market": u.get("market", ""),
            "status": "error", "reasons": msg, "missing": "", "cyclical_flag": "", "currency": "",
            "sector": "", "industry": "", "mcap_local_mn": None, "mcap_usd_mn": None,
            "fx_local_per_usd": None, "eps_trailing_local": None, "eps_0y_avg_local": None,
            "eps_1y_avg_local": None, "eps_base_yearago_local": None, "g2_eps_cagr_pct": None,
            "g5y_eps_growth_pct": None, "forward_pe_x": None, "peg_x": None, "analysts_1y_n": None,
            "revenue_1y_avg_mn_local": None, "fetched_at": "", "data_source": ""}


def write_csv(path, rows, cols=COLS):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def sort_key(r):
    peg = r["peg_x"] if r["peg_x"] is not None else 1e9
    return (peg, -(r["g_used_pct"] or 0))


def fmt(x, nd=2):
    if x is None or x == "":
        return "-"
    if isinstance(x, float):
        return f"{x:,.{nd}f}"
    return str(x)


def read_errors(path):
    if not path.exists():
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def build_summary(universe, rows, fx_meta, fetch_errs, uni_errs, generated):
    by_mkt = {}
    for r in rows:
        m = r["market"]
        b = by_mkt.setdefault(m, {"n": 0, "error": 0, "missing": 0, "fail": 0, "pass": 0,
                                  "borderline": 0, "cyc": 0})
        b["n"] += 1
        b[r["status"]] += 1
        if r["status"] in ("pass", "borderline") and r["cyclical_flag"] == 1:
            b["cyc"] += 1
    mkts = sorted(by_mkt, key=lambda m: (MARKET_ORDER.index(m) if m in MARKET_ORDER else 99, m))
    tot = {k: sum(by_mkt[m][k] for m in mkts) for k in ["n", "error", "missing", "fail", "pass", "borderline", "cyc"]}

    fail_reasons, miss_fields = {}, {}
    for r in rows:
        if r["status"] == "fail":
            for x in r["reasons"].split(";"):
                if x:
                    fail_reasons[x] = fail_reasons.get(x, 0) + 1
        for x in (r["missing"].split(";") if r["missing"] else []):
            miss_fields[x] = miss_fields.get(x, 0) + 1

    cand = sorted([r for r in rows if r["status"] == "pass"], key=sort_key) + \
           sorted([r for r in rows if r["status"] == "borderline"], key=sort_key)
    top = cand[:TOP_N]
    partial_n = sum(1 for e in fetch_errs if e.get("stage") == "partial")
    fetch_fail = [e for e in fetch_errs if e.get("stage") in ("fetch", "fx")]

    L = []
    L.append("# 一次ふるい 結果サマリー")
    L.append("")
    L.append(f"- 生成: {generated}")
    mode = fx_meta.get("source", "")
    if mode == "mock":
        L.append("- **モード: offline(モックデータ)。数値・銘柄はすべて架空。実データの結果ではない。**")
    else:
        L.append(f"- モード: {mode}")
    L.append(f"- 為替: {fx_meta.get('as_of', '')} 基準 (1 USD あたり 現地通貨: "
             + ", ".join(f"{k} {v}" for k, v in fx_meta.get("rates", {}).items()) + ")")
    L.append(f"- ユニバース: {len(universe)} 銘柄 / 取得失敗 {tot['error']} / 欠損 {tot['missing']} / "
             f"一部ブロック欠損(yfinance) {partial_n}")
    L.append("")
    L.append("## 判定基準")
    L.append("")
    L.append("- g2 = (EPS_+1y平均 / 実績年EPS)^(1/2) - 1、g1f = EPS_+1y / EPS_0y - 1、g = min(g2, g1f)")
    L.append("- PE = 株価 / ((EPS_0y + EPS_+1y)/2)、株価 = trailingPE x trailingEps、予想EPSは株価通貨に換算")
    L.append("- PEG = PE / (g x 100)")
    L.append("- 合格: g >= 31% かつ PEG <= 0.75")
    L.append("- 境界: g >= 22% かつ PEG <= 1.00 (合格を除く)")
    L.append("- 共通必須: 実績EPS > 0、予想EPS(0y・+1y) > 0、時価総額 >= 2億USD、アナリスト数 >= 1")
    L.append("- 循環フラグ: 業種による機械的な印 (除外はしない)。合格・境界の件数に併記")
    L.append("")
    L.append("## 市場別件数")
    L.append("")
    L.append("| 市場 | 対象 | 取得失敗 | 欠損 | 不合格 | 合格 | 境界 | 循環フラグ付き(合格+境界) |")
    L.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for m in mkts:
        b = by_mkt[m]
        L.append(f"| {m} | {b['n']} | {b['error']} | {b['missing']} | {b['fail']} | {b['pass']} | "
                 f"{b['borderline']} | {b['cyc']} |")
    L.append(f"| **合計** | **{tot['n']}** | **{tot['error']}** | **{tot['missing']}** | **{tot['fail']}** | "
             f"**{tot['pass']}** | **{tot['borderline']}** | **{tot['cyc']}** |")
    L.append("")
    L.append(f"## 合格・境界 上位{TOP_N}社 (合格を先、PEG 昇順)")
    L.append("")
    if top:
        L.append("| # | 判定 | ticker | 名称 | 市場 | 通貨 | 時価総額(百万USD) | EPS成長 g(%) | 5年成長(%) | PEG | 予想PE(x) | アナリスト数 | 循環 | 備考 |")
        L.append("|---:|---|---|---|---|---|---:|---:|---:|---:|---:|---:|:---:|---|")
        for i, r in enumerate(top, 1):
            judge = "合格" if r["status"] == "pass" else "境界"
            L.append(f"| {i} | {judge} | {r['ticker']} | {r['name']} | {r['market']} | {r['currency']} | "
                     f"{fmt(r['mcap_usd_mn'], 0)} | {fmt(r['g_used_pct'])} | {fmt(r['g5y_eps_growth_pct'])} | "
                     f"{fmt(r['peg_x'], 3)} | {fmt(r['forward_pe_x'], 1)} | {fmt(r['analysts_1y_n'], 0)} | "
                     f"{'○' if r['cyclical_flag'] == 1 else ''} | {r['reasons']} |")
    else:
        L.append("(該当なし)")
    L.append("")
    L.append("## 不合格の理由 (件数。1銘柄に複数理由があれば重複計上)")
    L.append("")
    if fail_reasons:
        for k, v in sorted(fail_reasons.items(), key=lambda kv: -kv[1]):
            L.append(f"- {k}: {v}")
    else:
        L.append("- (なし)")
    L.append("")
    L.append("## 欠損の内訳 (項目別件数)")
    L.append("")
    if miss_fields:
        for k, v in sorted(miss_fields.items(), key=lambda kv: -kv[1]):
            L.append(f"- {k}: {v}")
    else:
        L.append("- (なし)")
    L.append("")
    L.append("## 取得失敗・欠損の銘柄")
    L.append("")
    bad = [r for r in rows if r["status"] in ("error", "missing")]
    if bad:
        L.append("| ticker | 市場 | 区分 | 内容 |")
        L.append("|---|---|---|---|")
        for r in bad:
            kind = "取得失敗" if r["status"] == "error" else "欠損"
            detail = r["reasons"] if r["status"] == "error" else r["missing"]
            L.append(f"| {r['ticker']} | {r['market']} | {kind} | {detail} |")
    else:
        L.append("- (なし)")
    L.append("")
    L.append(f"- 取得段階の記録: data/errors.csv (取得失敗 {len(fetch_fail)} 件 / 一部ブロック欠損 {partial_n} 件)")
    if uni_errs:
        L.append("")
        L.append("## ユニバース段階の警告 (data/errors_universe.csv)")
        L.append("")
        for e in uni_errs:
            L.append(f"- [{e['market']}/{e['stage']}] {e['error']}")
    L.append("")
    L.append("## 注記")
    L.append("")
    L.append("- 境界の定義は、合格を除いて 'g >= 22% かつ PEG <= 1.00' を満たすもの。"
             "必須条件(EPS・時価総額・アナリスト)を満たさないものは境界に入れず不合格。")
    L.append("- 循環フラグは業種名の機械的判定。メモリ半導体などは人が個別に見直すこと。")
    L.append("- 詳細は out/all_scored.csv (全銘柄の数値と理由)、out/pass.csv、out/borderline.csv を参照。")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--offline", action="store_true", help="互換用。screen は常にローカルのみを読む")
    ap.add_argument("--universe", default=str(DATA / "universe.csv"))
    args = ap.parse_args()

    fx_path = DATA / "fx.json"
    if not fx_path.exists():
        raise SystemExit("data/fx.json が無い。先に fetch.py を実行してください。")
    fx_meta = json.loads(fx_path.read_text(encoding="utf-8"))
    rates = fx_meta.get("rates", {})

    with open(args.universe, encoding="utf-8", newline="") as f:
        universe = list(csv.DictReader(f))
    fetch_errs = read_errors(DATA / "errors.csv")
    fetch_msg = {e["ticker"]: e["error"] for e in fetch_errs if e.get("stage") == "fetch"}
    uni_errs = read_errors(DATA / "errors_universe.csv")

    rows = []
    for u in universe:
        p = cache_path(u["ticker"])
        if not p.exists():
            rows.append(error_row(u, fetch_msg.get(u["ticker"], "キャッシュなし(取得未実施)")))
            continue
        d = json.loads(p.read_text(encoding="utf-8"))
        rows.append(evaluate(u, d, rates))

    OUT.mkdir(parents=True, exist_ok=True)
    passed = sorted([r for r in rows if r["status"] == "pass"], key=sort_key)
    border = sorted([r for r in rows if r["status"] == "borderline"], key=sort_key)
    write_csv(OUT / "pass.csv", passed)
    write_csv(OUT / "borderline.csv", border)
    write_csv(OUT / "all_scored.csv", rows)

    generated = dt.datetime.now().isoformat(timespec="seconds")
    summary = build_summary(universe, rows, fx_meta, fetch_errs, uni_errs, generated)
    (OUT / "summary.md").write_text(summary, encoding="utf-8")

    counts = {s: sum(1 for r in rows if r["status"] == s)
              for s in ["pass", "borderline", "fail", "missing", "error"]}
    log(f"screen: 合格 {counts['pass']} / 境界 {counts['borderline']} / 不合格 {counts['fail']} / "
        f"欠損 {counts['missing']} / 取得失敗 {counts['error']}")
    log("出力: out/pass.csv, out/borderline.csv, out/all_scored.csv, out/summary.md")


if __name__ == "__main__":
    main()
