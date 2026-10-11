#!/usr/bin/env python3
"""sample.md 用の日本語ラベル付きグラフ(架空データ)を生成する。"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

for f in ("/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf", "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"):
    if Path(f).exists():
        font_manager.fontManager.addfont(f)
        break
plt.rcParams["font.family"] = "IPAGothic"
plt.rcParams["axes.unicode_minus"] = False

BLUE, ORANGE = "#2a78d6", "#eb6834"       # dataviz 既定パレットのスロット1・2(検証済み)
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"

years = ["FY2022", "FY2023", "FY2024", "FY2025", "FY2026"]
revenue = [1480, 1760, 2090, 2510, 2980]       # 架空
op_income = [190, 262, 341, 452, 566]          # 架空

fig, ax = plt.subplots(figsize=(8.0, 3.8), dpi=200)
x = range(len(years))
w = 0.36
b1 = ax.bar([i - w / 2 - 0.01 for i in x], revenue, w, color=BLUE, label="売上高", linewidth=0)
b2 = ax.bar([i + w / 2 + 0.01 for i in x], op_income, w, color=ORANGE, label="営業利益", linewidth=0)
ax.set_xticks(list(x))
ax.set_xticklabels(years, color=MUTED, fontsize=9)
ax.set_ylabel("億円", color=MUTED, fontsize=9, rotation=0, labelpad=18)
ax.tick_params(axis="y", colors=MUTED, labelsize=9, length=0)
ax.tick_params(axis="x", length=0)
ax.set_ylim(0, 3400)
ax.yaxis.grid(True, color=GRID, linewidth=0.8)
ax.set_axisbelow(True)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRID)
# 直接ラベルは最終年度のみ
for b, v in ((b1[-1], revenue[-1]), (b2[-1], op_income[-1])):
    ax.text(b.get_x() + b.get_width() / 2, v + 50, f"{v:,}", ha="center", va="bottom", fontsize=9, color=INK)
ax.set_title("サンプル(株)の売上高と営業利益(架空データ)", loc="left", fontsize=11, color=INK, pad=14)
ax.legend(frameon=False, loc="upper left", fontsize=9, ncol=2, bbox_to_anchor=(0.0, 1.0),
          labelcolor=MUTED, handlelength=1.0)
fig.tight_layout()
out = Path(__file__).with_name("chart_revenue.png")
fig.savefig(out, facecolor="white")
print(out)
