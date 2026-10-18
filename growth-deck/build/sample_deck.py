# -*- coding: utf-8 -*-
"""全部品を使ったサンプル6枚 -> sample.pptx。数値はすべて検査用の仮の値。"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deckkit import (  # noqa: E402
    new_prs, new_slide, cover, section_divider, closing, add_title, add_source,
    add_page_number, table, takeaway, arrow, box, badge, rank_badge, chevron,
    kpi_card, bar_chart, line_chart, BADGE_COLORS,
    PRIMARY, PRIMARY_DARK, SECONDARY, ACCENT,
)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "sample.pptx")

prs = new_prs()

# 1. 表紙
cover(prs, "成長テーマの評価と重点候補", "検査用サンプルデッキ", "2026年10月18日")

# 2. 目次トラッカー(中扉)
CHAPTERS = ["市場環境の確認", "テーマ別評価", "重点候補の判定"]
section_divider(prs, 1, CHAPTERS, 0)

# 3. 表 + テイクアウェイ
s = new_slide(prs)
add_title(s, "市場成長と参入余地を両立する3テーマを優先する",
          kicker="テーマ別の評価サマリー(評価記号は S〜F、NA は対象外)")
rows = [
    ["テーマ", "市場成長率(年率)", "参入余地", "総合評価"],
    ["A データ基盤", "14%", "大", "S"],
    ["B 省人化ロボット", "11%", "中", "A"],
    ["C 再生医療", "9%", "大", "B"],
    ["D 地域決済", "3%", "小", "C"],
]
cell_colors = {(r, 3): BADGE_COLORS[rows[r][3]][0] for r in range(1, len(rows))}
table(s, 0.5, 1.65, 8.0, 4.2, rows, [3.0, 1.8, 1.6, 1.6], font=12,
      cell_colors=cell_colors, col_align=["l", "r", "c", "c"], bold_cells={(1, 0), (2, 0), (3, 0)})
arrow(s, 8.55, 3.75, 8.85, 3.75)
takeaway(s, 8.9, 1.65, 3.93, 4.2,
         "市場成長と参入余地が両立するテーマ(A・B)に調査を集中させる。"
         "Dは成長率が低いため優先度を下げる。")
add_source(s, "サンプルデータ(検査用の仮の数値)")
add_page_number(s, 3)

# 4. 棒グラフ + 折れ線 + KPIカード
s = new_slide(prs)
add_title(s, "国内市場は2027年まで二桁成長が続く見通しである",
          kicker="市場規模は実績(濃緑)と予測(薄緑)を分けて示し、予測の年は「予」を付す")
kpi_card(s, 0.5, 1.6, 3.93, 1.5, "10.4兆円", "2025年 市場規模(実績)",
         note="前年比 +14.3%", color=PRIMARY)
kpi_card(s, 4.7, 1.6, 3.93, 1.5, "+14%", "2026予 前年比成長率",
         note="予測値", color=ACCENT)
kpi_card(s, 8.9, 1.6, 3.93, 1.5, "13.6兆円", "2027予 市場規模",
         note="予測値", color=ACCENT)

CATS = ["2023", "2024", "2025", "2026予", "2027予"]
box(s, 0.5, 3.25, 6.0, 0.3, text="市場規模の推移(兆円)", size=11, bold=True,
    line=None, name="chart_label_bar")
bar_chart(s, 0.5, 3.6, 6.0, 3.25, CATS,
          {"実績": [8.2, 9.1, 10.4, None, None],
           "予測": [None, None, None, 11.9, 13.6]},
          stacked=True, number_format="0.0", colors=[PRIMARY, SECONDARY])
box(s, 6.83, 3.25, 6.0, 0.3, text="成長率の推移(%)", size=11, bold=True,
    line=None, name="chart_label_line")
line_chart(s, 6.83, 3.6, 6.0, 3.25, CATS,
           {"成長率(実績)": [None, 11.0, 14.3, None, None],
            "成長率(予測)": [None, None, 14.3, 14.4, 14.3]},
           number_format="0.0", data_labels=False, colors=[PRIMARY, SECONDARY])
add_source(s, "サンプルデータ(検査用の仮の数値)。2026年以降は予測値")
add_page_number(s, 4)

# 5. 評価バッジ(7種 + NA) + 重点候補 + 手順
s = new_slide(prs)
add_title(s, "評価バッジで候補の優先順位を一目で判定できる",
          kicker="評価記号は S(極めて優良)から F(不適格)の7段階、対象外は NA")
GRADES = [("S", "極めて優良"), ("A", "優良"), ("B", "良好"), ("C", "中立"),
          ("D", "やや弱い"), ("E", "弱い"), ("F", "不適格"), ("NA", "評価対象外")]
for i, (g, label) in enumerate(GRADES):
    x = 0.5 + i * 1.55
    badge(s, x + 0.4, 2.0, g, size=0.6)
    box(s, x, 2.75, 1.4, 0.3, text=label, size=11, align="c", line=None,
        name=f"grade_label_{g}")

CHEVRONS = [("1 市場成長率で絞り込む", PRIMARY_DARK),
            ("2 参入余地を定性評価する", PRIMARY),
            ("3 評価バッジで判定する", ACCENT)]
for i, (text, fill) in enumerate(CHEVRONS):
    chevron(s, 0.5 + i * 4.2, 3.5, 3.9, 0.5, text, fill)

box(s, 0.5, 4.25, 6.0, 0.3, text="重点候補の判定", size=11, bold=True,
    line=None, name="section_label")
box(s, 10.0, 4.25, 2.8, 0.3, text="総合評価", size=11, bold=True,
    line=None, name="grade_header")
CANDIDATES = [
    ("テーマA データ基盤", "市場成長率が高く、参入余地も大きい", "S"),
    ("テーマB 省人化ロボット", "成長性は十分で、参入余地は中程度", "A"),
    ("テーマC 再生医療", "参入余地は大きいが、成長率は中程度", "B"),
]
for i, (name, reason, grade) in enumerate(CANDIDATES):
    y = 4.7 + i * 0.75
    rank_badge(s, 0.5, y, i + 1)
    box(s, 1.1, y, 8.6, 0.42, text=f"{name}:{reason}", size=12, line=None,
        valign="m", name=f"candidate_{i + 1}")
    badge(s, 10.0, y, grade, size=0.42)
add_source(s, "サンプルデータ。評価基準は検査用の仮定義")
add_page_number(s, 5)

# 6. クロージング
closing(prs, "重点候補A・Bの一次調査を開始する\n本資料は投資助言ではありません")

prs.save(OUT)
print("saved:", OUT)
