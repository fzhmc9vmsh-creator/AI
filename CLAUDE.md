# このリポジトリでの作業の約束

## スキル(別のセッションでも同じ型で作業するために)
- 銘柄分析・投資資料の作業では、`.claude/skills/` にあるプロジェクト版のスキルを使う。アカウントに同名のスキル(`anthropic-skills:…`)があっても、プロジェクト版を優先する(利用者の最新のフィードバックはプロジェクト版にだけ入っている)。
  - `.claude/skills/meigara-bunseki-method/` 銘柄分析メソッド(分析と報告書)
  - `.claude/skills/invest-consulting-deck/` 投資資料のパワポ(最新の必須事項は `references/deck-rules-v2.md`、部品は `scripts/`)
  - `.claude/skills/bcg-slide-method/` スライドの作り方の一般規範(references は代替版)
- アカウントにアップロードする版は `skills/*.skill`(zip)。プロジェクト版を直したら `python3 skills/build_skills.py --node-modules <node_modules>` で作り直す(検査と自己テストを通ったときだけ zip ができる)。
- 計算は `meigara-bunseki-method/scripts/valuate.py`、数字は台帳 `facts.json`、工程の合否は `gate.py`。資料の要所の数字は `F('id')` で台帳から引き、組み上がった資料は `lint_deck.py pptx` で照合する。手で計算した数字・手で丸め直した数字を資料に書かない。

## 資料の必須事項(要約。詳細は deck-rules-v2.md)
- 全スライドの左上に現在地(章 › 節)、その下に「テーマ: …」と「なぜ見るか」。
- 事業理解は 3 枚(積み木 + 5W1H + 用語の注釈 / 事業どうしの関係図 / 注目度の高い成長分野)、会社のシナリオは 2 枚(ストーリー図 / 採点)。
- 関係図はレーン・10〜14 箱・数量つきの矢印・番号つきの仕組み・上がる/下がる条件。重なり 0 件。
- 経営者(条件5)は経歴とその事業への経験から評価する。
- 成長企業は成長段階の尺度(G1〜G8: 単位経済・獲得投資の裁量性・切替コスト・クロスセル・資本の転換・B2B 基盤の段階・コスト構造の変化・業態の組み合わせと資本コスト)で構造を評価し、「成長の尺度」の章とシナリオ確率の節点ツリーを入れる(詳細は meigara-bunseki-method の growth-stage-evaluation.md)。
- 成長企業は、フェーズを最初に決め、現在と将来(実現性を加味)の二層で構造を評価する。初歩の規律(KPI は前期比・前年比の率で読む、EPS の四半期を税・株数で分ける、フライホイールとバリューチェーンを競合と比べる、資本モデルは業界と比べてから評価、マクロ要因は両面で市場の織り込みと比べる、条件6 は市場との乖離で評価、図は事業の形に合わせる)の上に、市場が値段に入れていない示唆を出す(growth-stage-evaluation.md 第5版)。
- 妥当 PER は許容 PEG × g(当該年度から 3〜5 年の EPS CAGR)だけで決め、同業の PER・DCF とは平均しない(交差確認に使う)。信用と資本の制約は同業と比べて数量化し、倍率でなく EPS 経路・確率・株数で数える(valuation-model §3-3 第5.2版、growth-stage-evaluation §6-2)。
- 構造評価の変化は必ず許容 PEG と α に反映する。等級の文字だけで決めず、等級の中の位置を条件の点数で決める(meigara-bunseki-method の valuation-model §3-3 第5.1版)。
- 改行位置を明示し、末行 1〜2 文字や数字と単位の泣き別れを作らない。Windows 向けはフォント Meiryo UI。
- 制作は Haiku、指示は Opus、難しいもの(関係図・複合構成)は Sonnet。

## 成果物
- 銘柄ごとの成果物は `reports/<TICKER>/`。作業用のスクリプト・指示書・計算は `reports/<TICKER>/work/`。
