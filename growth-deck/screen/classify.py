"""一次ふるい通過銘柄を業種で仕分ける(構造評価の前段)。

screen.py の out/pass.csv と out/borderline.csv を読み、
- exclude: 景気循環・資源・与信・規制公益など、構造 A+(平均 4.0 以上)が原理的に難しい業種
- review : それ以外(Opus が事業説明を読んで判断する)
に分ける。review にはデータ上の特殊要因フラグを付ける。

出力: out/review.csv, out/excluded.csv, out/classify_summary.md
"""
import json
import os

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
CACHE = os.path.join(HERE, "data", "cache")

# 構造 A+ が原理的に難しい業種(完全一致)
EXCLUDE_EXACT = {
    "Banks - Regional", "Banks - Diversified", "Mortgage Finance",
    "Insurance - Life", "Insurance - Property & Casualty", "Insurance - Diversified",
    "Insurance - Specialty", "Insurance - Reinsurance",
    "Gold", "Silver", "Copper", "Aluminum", "Steel", "Uranium", "Coking Coal", "Thermal Coal",
    "Other Industrial Metals & Mining", "Other Precious Metals & Mining",
    "Chemicals", "Specialty Chemicals", "Agricultural Inputs", "Paper & Paper Products",
    "Lumber & Wood Production", "Building Materials", "Textile Manufacturing",
    "Packaging & Containers", "Farm Products", "Packaged Foods", "Confectioners",
    "Marine Shipping", "Airlines", "Trucking", "Railroads", "Integrated Freight & Logistics",
    "Auto Manufacturers", "Auto Parts", "Auto & Truck Dealerships", "Recreational Vehicles",
    "Residential Construction", "Engineering & Construction", "Metal Fabrication",
    "Farm & Heavy Construction Machinery", "Rental & Leasing Services",
    "Food Distribution", "Grocery Stores", "Department Stores", "Discount Stores",
    "Electronics & Computer Distribution", "Industrial Distribution", "Medical Distribution",
    "Solar", "Shell Companies", "Conglomerates", "Lodging", "Real Estate Services",
    "Tobacco", "Beverages - Brewers",
}
EXCLUDE_PREFIX = ("Oil & Gas", "REIT", "Real Estate", "Utilities")


def is_excluded(ind):
    if not isinstance(ind, str):
        return False
    return ind in EXCLUDE_EXACT or ind.startswith(EXCLUDE_PREFIX)


def data_flags(r):
    """一次ふるいの数字が実力を表さない可能性を示すフラグ。"""
    f = []
    base, e0, e1 = r.eps_base_yearago_local, r.eps_0y_avg_local, r.eps_1y_avg_local
    if pd.notna(base) and pd.notna(e0) and pd.notna(e1) and base > 0 and e0 > 0:
        # 今期だけ跳ねて来期は鈍い: 底からの反発・一時利益の疑い
        if e0 / base >= 1.8 and e1 / e0 < 1.15:
            f.append("rebound")
    if pd.notna(r.eps_trailing_local) and pd.notna(base) and base > 0:
        if r.eps_trailing_local / base > 3:
            f.append("trailing_jump")
    if pd.isna(r.analysts_1y_n) or r.analysts_1y_n < 3:
        f.append("thin_coverage")
    if pd.notna(r.mcap_usd_mn) and r.mcap_usd_mn < 300:
        f.append("micro")
    return ";".join(f)


def summary_text(t):
    p = os.path.join(CACHE, f"{t}.json")
    try:
        s = json.load(open(p)).get("longBusinessSummary") or ""
    except (OSError, ValueError):
        s = ""
    return s.replace("\n", " ")[:600]


def main():
    frames = []
    for name in ("pass", "borderline"):
        p = os.path.join(OUT, f"{name}.csv")
        if os.path.exists(p):
            frames.append(pd.read_csv(p))
    d = pd.concat(frames, ignore_index=True)
    d["excluded"] = d.industry.map(is_excluded)
    ex = d[d.excluded].copy()
    rv = d[~d.excluded].copy()
    rv["data_flags"] = rv.apply(data_flags, axis=1)
    rv["summary"] = rv.ticker.map(summary_text)
    rv = rv.sort_values(["status", "peg_x"], ascending=[False, True])
    cols = ["ticker", "name", "market", "status", "industry", "mcap_usd_mn", "g2_eps_cagr_pct",
            "peg_x", "forward_pe_x", "analysts_1y_n", "data_flags", "summary"]
    rv[cols].to_csv(os.path.join(OUT, "review.csv"), index=False)
    ex[["ticker", "name", "market", "status", "industry", "g2_eps_cagr_pct", "peg_x"]].to_csv(
        os.path.join(OUT, "excluded.csv"), index=False)

    lines = ["# 業種仕分けの結果", "",
             f"- 入力: pass + borderline = {len(d)} 銘柄",
             f"- 除外(業種): {len(ex)} 銘柄",
             f"- 確認対象: {len(rv)} 銘柄(うち pass {int((rv.status == 'pass').sum())})", "",
             "## 確認対象の業種分布", "", "| 業種 | 件数 |", "|---|---|"]
    for k, v in rv.industry.value_counts().items():
        lines.append(f"| {k} | {v} |")
    lines += ["", "## 除外した業種", "", "| 業種 | 件数 |", "|---|---|"]
    for k, v in ex.industry.value_counts().items():
        lines.append(f"| {k} | {v} |")
    open(os.path.join(OUT, "classify_summary.md"), "w").write("\n".join(lines) + "\n")
    print("\n".join(lines[:6]))


if __name__ == "__main__":
    main()
