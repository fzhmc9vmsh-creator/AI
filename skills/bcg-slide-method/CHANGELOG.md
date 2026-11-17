# 改訂履歴(2026-11-17)— 必須の前提の 3 枚

利用者の指摘(eWeLL 5038 の資料): 「シンプルに最新決算の内容反映してないし、事業として何をしてるかも記載ない。事業理解の項目がない。普通に有り得ない」。
原因: 標準の構成(stock-analysis.md §3)が「結論 → 分析」で、何をしている会社か・業界の仕組み・直近の決算を置く決まりも検査も無かった。示唆の重みで枚数を配るため、
開示の基本情報(示唆ではない)が落ちた。

| 変更 | 中身 |
|---|---|
| references/stock-analysis.md §3 | 第 2 章に必須の 3 枚: 会社と事業の概要(std: business_overview)・業界の仕組みとお金の流れ(industry_basics)・最新決算のサマリー(latest_results)。示唆の重みと無関係に入れる |
| scripts/check_storyline.py(--analysis) | 3 枚が無い、本編の最初の 8 枚に無い、最新決算の message に数字が無い、を止める |
| templates/storyline.json・SKILL.md | 3 枚のひな形と手順 |

