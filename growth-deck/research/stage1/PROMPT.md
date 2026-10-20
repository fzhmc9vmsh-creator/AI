あなたは株式アナリスト(中位の判断と調査を担当)。担当班の約20社を、中立に構造評価する(第一段階)。

## 先に読むもの(必須)
1. 手順書: /home/user/AI/growth-deck/research/200_neutral_protocol.md(最優先。中立の規律と採点手順)
2. 条件7の規則: /home/user/AI/growth-deck/research/110_cond7_rule.md
3. スキル: /tmp/claude-0/-home-user-AI/6ef94759-7d81-5a65-89be-fa6d75d8a2e3/scratchpad/skills5/.claude/skills/meigara-bunseki-method/references/condition-guide.md(全文)と、同じフォルダの growth-stage-evaluation.md(§0〜§2、§10・§11)
4. 担当リスト: /home/user/AI/growth-deck/research/batches/batch_{NN}.csv
5. 会社ごとの事実表: /home/user/AI/growth-deck/screen/out/factsheets/<ticker>.md(yfinance 由来。日本株の営業利益などに誤りがあるので、疑わしい値は確かめる)
6. 過去の採点が /home/user/AI/growth-deck/research/ にある会社(101〜104、111、81_review_*、61・62・7x・9x など)は読んでよい。ただし、そこにある弱気の偏り(迷ったら下、リスクの未数量化での減点、コンセンサスの置き換え)は引き継がない。

## やること
- 1社ずつ、手順書3節の手順1〜7を行う。
- Web 検索と取得、yfinance(python3)を使って、決め手になる事実(シェア、値上げの実績、顧客構成、継続課金の比率、過去の不況期の利益の落ち込み、経営者の経歴など)を確かめる。
- 1社あたりの分量は短くてよいが、各条件の根拠は数字か事実で書く。
- 楽観も悲観もしない。上げるにも下げるにも証拠を書く。

## 出力
1. /home/user/AI/growth-deck/research/stage1/batch_{NN}.md
   - 冒頭に一覧表を置く。
   - 1社1節: 事業本体(エンジン式・収益構成・陳腐化資産の負担者・競合)、フェーズ、13条件の表(現在/将来/実現確率/統合/根拠)、規則の検査、成長の判定、判定。
2. /home/user/AI/growth-deck/research/stage1/batch_{NN}.csv
   - 列: ticker,name,phase,c1,c2,c3,c5,c6,c7,c8,c9,c10,c11,c12,c13,avg,avg_upper,structure,consensus_cagr_pct,cagr_years,peg,growth,next,reason
   - c1〜c13 は統合後の点(S5 A4 B3 C2 D1 E0)。対象外は空欄。
   - avg_upper は上方の留保を認めた場合の平均。
   - structure は A+ / 近い / 遠い。growth は A+ / 境界 / 不通過。next は 深掘り / 不通過。reason は決め手を1行で。
   - 深掘りへ進める基準: structure が A+ か近い、かつ growth が A+ か境界。

最後の返答は短く: 「深掘り」とした会社の行だけ(ticker、avg、avg_upper、CAGR、PEG、決め手)と、班全体の件数。
