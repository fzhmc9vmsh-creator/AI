#!/usr/bin/env python3
"""構造の再評価用に、銘柄ごとの財務の事実表を作る。

入力: data/structure_universe.csv(ticker 列)
出力:
  data/fs_cache/<ticker>.json   yfinance の生データ(info の抜粋・年次と四半期の損益・CF・BS)
  out/factsheets/<ticker>.md    事実表(利益率の推移、景気循環の実績、設備投資の負担、財務)
  out/factsheets_index.csv      主要指標の一覧

事実だけを並べ、良し悪しの判定はしない(判定は採点者が行う)。
"""
import argparse
import csv
import json
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from fetch import clean, df_to_dict, safe_name, with_backoff
from universe import DATA, HERE, log

FS_CACHE = DATA / "fs_cache"
OUT = HERE / "out" / "factsheets"
INFO_KEYS = [
    "shortName", "longName", "country", "sector", "industry", "currency", "financialCurrency",
    "marketCap", "enterpriseValue", "fullTimeEmployees", "grossMargins", "operatingMargins",
    "ebitdaMargins", "profitMargins", "returnOnEquity", "returnOnAssets", "revenueGrowth",
    "earningsGrowth", "totalCash", "totalDebt", "freeCashflow", "operatingCashflow", "ebitda",
    "totalRevenue", "heldPercentInsiders", "heldPercentInstitutions", "trailingPE", "forwardPE",
    "priceToSalesTrailing12Months", "beta", "dividendYield", "payoutRatio", "longBusinessSummary",
    "numberOfAnalystOpinions", "recommendationKey", "targetMeanPrice", "currentPrice",
]
IS_ROWS = ["Total Revenue", "Gross Profit", "Operating Income", "Net Income",
           "Research And Development", "Selling General And Administration", "Diluted EPS"]
CF_ROWS = ["Operating Cash Flow", "Capital Expenditure", "Free Cash Flow",
           "Stock Based Compensation", "Repurchase Of Capital Stock"]
BS_ROWS = ["Total Debt", "Cash And Cash Equivalents", "Stockholders Equity", "Total Assets",
           "Goodwill And Other Intangible Assets", "Inventory", "Accounts Receivable"]


def pick(d, rows):
    """{日付: {項目: 値}} から必要な項目だけ残す。"""
    if not d:
        return None
    return {k: {r: v.get(r) for r in rows if r in v} for k, v in d.items()}


def fetch_one(yf, t):
    p = FS_CACHE / f"{safe_name(t)}.json"
    if p.exists():
        return json.loads(p.read_text())
    tk = yf.Ticker(t)
    out = {"ticker": t, "errors": []}

    def block(name, fn):
        try:
            out[name] = with_backoff(fn)
        except Exception as e:  # 一部が取れなくても続ける
            out[name] = None
            out["errors"].append(f"{name}: {type(e).__name__}: {str(e)[:120]}")

    block("info", lambda: {k: clean(tk.info.get(k)) for k in INFO_KEYS})
    block("is_y", lambda: pick(df_to_dict(tk.income_stmt.T), IS_ROWS))
    block("is_q", lambda: pick(df_to_dict(tk.quarterly_income_stmt.T), IS_ROWS))
    block("cf_y", lambda: pick(df_to_dict(tk.cashflow.T), CF_ROWS))
    block("bs_y", lambda: pick(df_to_dict(tk.balance_sheet.T), BS_ROWS))
    out["fetched_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    p.write_text(json.dumps(out, ensure_ascii=False))
    time.sleep(0.4)
    return out


def series(d, row):
    """古い順の [(日付, 値)]。"""
    if not d:
        return []
    return sorted(((k[:10], v.get(row)) for k, v in d.items() if v.get(row) is not None))


def pct(x, nd=1):
    return "-" if x is None else f"{x * 100:.{nd}f}%"


def num(x):
    if x is None:
        return "-"
    a = abs(x)
    for div, unit in ((1e12, "兆"), (1e8, "億"), (1e6, "百万")):
        if a >= div:
            return f"{x / div:,.2f}{unit}"
    return f"{x:,.2f}"


def ratio(a, b):
    return None if (a is None or not b) else a / b


def build_md(t, d, scored):
    info = d.get("info") or {}
    isy, isq, cfy, bsy = d.get("is_y"), d.get("is_q"), d.get("cf_y"), d.get("bs_y")
    rev, gp, oi, ni = (series(isy, r) for r in ("Total Revenue", "Gross Profit", "Operating Income", "Net Income"))
    rd = dict(series(isy, "Research And Development"))
    ocf, capex, fcf, sbc = (dict(series(cfy, r)) for r in
                            ("Operating Cash Flow", "Capital Expenditure", "Free Cash Flow", "Stock Based Compensation"))
    gpd, oid, nid = dict(gp), dict(oi), dict(ni)
    L = [f"# {t} {info.get('longName') or info.get('shortName') or ''}", ""]
    s = scored or {}
    L += [f"- 国・業種: {info.get('country')} / {info.get('sector')} / {info.get('industry')}",
          f"- 通貨: 株価 {info.get('currency')} / 財務 {info.get('financialCurrency')}",
          f"- 時価総額: {num(info.get('marketCap'))}、EV: {num(info.get('enterpriseValue'))}、従業員: {info.get('fullTimeEmployees')}",
          f"- 一次判定: {s.get('status')}、g2 {s.get('g2_eps_cagr_pct')}%、来期 {s.get('g1f_eps_growth_pct')}%、"
          f"PE {s.get('forward_pe_x')}、PEG {s.get('peg_x')}、アナリスト {s.get('analysts_1y_n')}",
          f"- 直近12か月: 粗利率 {pct(info.get('grossMargins'))}、営業利益率 {pct(info.get('operatingMargins'))}、"
          f"純利益率 {pct(info.get('profitMargins'))}、ROE {pct(info.get('returnOnEquity'))}、ROA {pct(info.get('returnOnAssets'))}",
          f"- 財務: 現金 {num(info.get('totalCash'))}、負債 {num(info.get('totalDebt'))}、EBITDA {num(info.get('ebitda'))}、"
          f"FCF {num(info.get('freeCashflow'))}",
          f"- 保有: 内部者 {pct(info.get('heldPercentInsiders'))}、機関 {pct(info.get('heldPercentInstitutions'))}", ""]
    L += ["## 年次の推移(yfinance、最大4〜5期)", "",
          "| 期 | 売上 | 売上伸び | 粗利率 | 営業利益率 | 純利益 | 研究開発/売上 | 営業CF | 設備投資/売上 | FCF | 株式報酬/売上 |",
          "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    prev = None
    for k, v in rev:
        g = ratio(v, prev) - 1 if prev else None
        cx = capex.get(k)
        L.append(f"| {k} | {num(v)} | {pct(g)} | {pct(ratio(gpd.get(k), v))} | {pct(ratio(oid.get(k), v))} | "
                 f"{num(nid.get(k))} | {pct(ratio(rd.get(k), v))} | {num(ocf.get(k))} | "
                 f"{pct(ratio(-cx if cx else None, v))} | {num(fcf.get(k))} | {pct(ratio(sbc.get(k), v))} |")
        prev = v
    qrev, qoi = series(isq, "Total Revenue"), dict(series(isq, "Operating Income"))
    if qrev:
        L += ["", "## 四半期の推移", "", "| 四半期 | 売上 | 営業利益率 |", "|---|---:|---:|"]
        for k, v in qrev:
            L.append(f"| {k} | {num(v)} | {pct(ratio(qoi.get(k), v))} |")
    # 景気循環の実績: 期間内の営業利益の最大の落ち込み
    dd = None
    peak = None
    for _, v in oi:
        if v is None:
            continue
        peak = v if peak is None or v > peak else peak
        if peak and peak > 0:
            x = v / peak - 1
            dd = x if dd is None or x < dd else dd
    L += ["", "## 機械的な指標(判定ではない)", "",
          f"- 期間内の営業利益の最大の落ち込み(山からの下落率): {pct(dd)}"]
    if bsy:
        last = max(bsy)
        b = bsy[last]
        L.append(f"- 直近の BS({last[:10]}): 自己資本 {num(b.get('Stockholders Equity'))}、のれん等 "
                 f"{num(b.get('Goodwill And Other Intangible Assets'))}、在庫 {num(b.get('Inventory'))}、"
                 f"売掛金 {num(b.get('Accounts Receivable'))}")
    L += ["", "## 事業の説明(yfinance)", "", (info.get("longBusinessSummary") or "-"), ""]
    if d.get("errors"):
        L += ["## 取得できなかった項目", ""] + [f"- {e}" for e in d["errors"]]
    return "\n".join(L) + "\n", {"ticker": t, "oi_max_drawdown": dd,
                                  "gross_margin": info.get("grossMargins"),
                                  "op_margin": info.get("operatingMargins"), "roe": info.get("returnOnEquity")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=3)
    a = ap.parse_args()
    import yfinance as yf
    FS_CACHE.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    tickers = [r["ticker"] for r in csv.DictReader(open(DATA / "structure_universe.csv"))]
    scored = {r["ticker"]: r for r in csv.DictReader(open(HERE / "out" / "all_scored.csv"))}
    log(f"factsheet: {len(tickers)} 銘柄")
    done = [0]

    def run(t):
        try:
            d = fetch_one(yf, t)
        except Exception as e:
            log(f"  ERROR {t}: {type(e).__name__}: {e}")
            return None
        md, row = build_md(t, d, scored.get(t))
        (OUT / f"{safe_name(t)}.md").write_text(md)
        done[0] += 1
        if done[0] % 50 == 0:
            log(f"  {done[0]} / {len(tickers)}")
        return row

    with ThreadPoolExecutor(a.workers) as ex:
        rows = [r for r in ex.map(run, tickers) if r]
    with open(HERE / "out" / "factsheets_index.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    log(f"factsheet 完了: {len(rows)} / {len(tickers)}")


if __name__ == "__main__":
    main()
