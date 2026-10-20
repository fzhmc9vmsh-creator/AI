"""第一段階の各班 CSV を集計する。

name・reason 列にカンマを含みクォートされていない行があるため、先頭を ticker とし、
phase 列(①〜⑤)の位置から固定の列を読む。reason は残り全部。
出力: stage1/summary.csv と summary.md(深掘り候補と構造上位)
"""
import csv
import glob
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TAIL = ["phase", "c1", "c2", "c3", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13",
        "avg", "avg_upper", "structure", "consensus_cagr_pct", "cagr_years", "peg", "growth", "next", "reason"]


def rows(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    for line in lines[1:]:
        if not line.strip():
            continue
        cells = next(csv.reader([line]))
        if len(cells) < len(TAIL) + 2:
            continue
        # name・reason の両方にカンマが入りうるので、phase(①〜⑤を含む列)の位置を左から探す
        ticker = cells[0]
        i = next((k for k in range(2, len(cells)) if any(c in cells[k] for c in "①②③④⑤")), None)
        if i is None:
            continue
        fixed = cells[i:i + len(TAIL) - 1] + [",".join(cells[i + len(TAIL) - 1:])]
        r = dict(zip(TAIL, fixed))
        r["ticker"], r["batch"] = ticker, os.path.basename(path)[6:8]
        yield r


def f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def main():
    allr = []
    for p in sorted(glob.glob(os.path.join(HERE, "batch_*.csv"))):
        allr += list(rows(p))
    with open(os.path.join(HERE, "summary.csv"), "w", newline="", encoding="utf-8") as fo:
        w = csv.DictWriter(fo, fieldnames=["batch", "ticker"] + TAIL)
        w.writeheader()
        w.writerows(allr)
    top = sorted(allr, key=lambda r: -(f(r["avg"]) or 0))[:30]
    L = ["# 第一段階の集計", "", f"- 採点済み: {len(allr)} 社(班: {sorted({r['batch'] for r in allr})})",
         f"- 深掘り: {sum(r['next'] == '深掘り' for r in allr)} 社", "",
         "## 構造平均の上位30社", "", "| 班 | ticker | avg | avg_upper | 構造 | CAGR | PEG | 成長 | 次 |",
         "|---|---|---:|---:|---|---:|---:|---|---|"]
    for r in top:
        L.append(f"| {r['batch']} | {r['ticker']} | {r['avg']} | {r['avg_upper']} | {r['structure']} | "
                 f"{r['consensus_cagr_pct']} | {r['peg']} | {r['growth']} | {r['next']} |")
    open(os.path.join(HERE, "summary.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
