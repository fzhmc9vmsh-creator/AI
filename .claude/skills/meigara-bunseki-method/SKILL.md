---
name: meigara-bunseki-method
description: スキル和名は「銘柄分析メソッド」。目的は割安な優良企業の見極めであり、事業本体(原子単位とエンジン式、ユニットエコノミクス、増収の源泉、自己強化ループと制約、需要の連鎖、資本の出し手と資産の外部化、経済的耐用年数、フロー→ストック、定常状態利益、競争優位期間)を把握し、価値感度分析で芯(価値を最も動かす変数)を特定し、市場の仮説との差分と優位の種類として結論を出す。報告書の軸は「経営陣の成長シナリオ」で、シナリオは事業エンジンの変数に翻訳して採点する。ユーザーが「〇〇(ティッカー/企業名)を分析して」「銘柄を審査して」「13条件で評価して」「長期保有できるか調べて」「投資候補を調査して」「ビジネスの根幹を分析して」「決算が出たので分析を更新して」などと言及したら必ずこのスキルを使うこと。長期保有13条件、成長企業の構造評価(フェーズ・二層の構造・獲得投資の裁量性・単位経済・資本の転換・確率の節点ツリー)、EPS品質フォレンジック、コンセンサス/会社シナリオ/事業エンジンの3経路、年度別適正株価、エントリー価格帯と時系列投資戦略を含む。計算は同梱の計算機、数字は台帳、各工程は検査スクリプトで合否を出すので、低予算のモデルでも同じ品質で動く。報告書の本体はWord文書(docx)で、パワポ化はinvest-consulting-deckスキルとbcg-slide-methodスキルを使う。
---

# 銘柄分析メソッド(手順書)

この文書は**作業の順番と合否の決め方**だけを書いた手順書。方法の詳細は `references/` にあり、各工程で
「読む」と書いた節だけを、その工程で読む(最初に全部を読まない)。

## 3 つの約束(どのモデルで動かしても守る)

1. **計算は道具でする。** 許容 PEG・妥当 PER・理論株価・エントリー圏・シナリオの期待値は `scripts/valuate.py` が出す。
   手で計算しない。結果の数字は `valuation.json` の `display`(1 回だけ丸めた表示値)を写す。
2. **数字は台帳から出す。** 報告書・資料の要所の数字は `facts.json` に 1 行ずつ、時点・出所・状態を付けて登録する。
   未確認の数字(T4)は使わない。前の四半期の値は「(Q2)」のように時点を付けて比較にだけ使う。
3. **検査を通してから次へ進む。** 各工程の終わりに `scripts/gate.py` を実行し、PASS してから次の工程へ進む。
   FAIL のときは、出た誤りだけを直して再実行する。検査の道具・手本の答えを書き換えて通すことは禁止。

利用者に指摘された誤りの一覧は `references/must-rules.md`。各工程の終わりに、その工程の行を読んで確かめる。

## 準備(最初に 1 回)

```bash
S=<このスキルのフォルダ>            # 例: /mnt/skills/user/meigara-bunseki-method
W=<作業フォルダ>                    # 例: ./work/TICKER
mkdir -p $W && cp $S/templates/*.json $S/templates/report_outline.md $W/
python3 $S/scripts/selftest.py      # 道具の自己テスト。FAIL なら作業を始めない
```

作業フォルダの標準のファイル: `facts.json`(台帳)・`conditions.json`(13 条件)・`valuation_input.json`(計算の入力)
→ `valuation.json` / `valuation.md`(計算の出力)・`report.md`(報告書の原稿)。手本は `examples/sofi/`。

## 工程 0: ゲート審査と型の判定

- 読む: `references/method-detail.md` の「Phase 0」。
- 決める: ① 日本株か米国株か(違えば短い報告で終了)、② 会計不正が進行中でないか、③ AI 関連か(違えば条件9 は N/A)、
  ④ **成長企業か**(`references/growth-stage-evaluation.md` §0 の適用条件)。成長企業なら `conditions.json` の
  `growth_company` を true にし、**フェーズ(①〜⑤)を最初に決めて** `phase` に書く(§1)。
- 決算の更新のときは、下の「決算の更新」を先に読む。

## 工程 1: 調査 → 台帳(facts.json)

- 読む: `references/research-protocol.md` §1(調査項目)・§2(情報源の Tier)・§4(コンセンサスの取り方)。
- 作る: `facts.json`。要所の数字だけでよい(目安 40〜150 行)。
  - タイトル・結論・KPI に出す数字、価値評価の入力(EPS の実績と予想・株価・資本コストの材料)
  - 根幹 KPI の最新の四半期と、**前の四半期・前年同期の主要な値**(率で読むため。古い値の混入の検出にも使う)
  - 使わないと決めた未確認の値(`not_for_deck: true` と `reason`)
- 規則: 最新の決算・株価・ガイダンスは必ず検索で取る(記憶で書かない)。会社が開示する指標は自分で計算し直さない。
  計算した値は `status: 計算` と `note` に式。基準(GAAP・調整後)を `basis` に書く。
- 利用者の資料(メモ・表)だけで作るときは検索しない。資料に無い項目は `status: 未取得` で登録し、報告書の「既知の制約」に書く
  (8 四半期の系列が無い、など)。資料の中の数字どうしの食い違いも「既知の制約」に書き、どちらを使ったかを残す。
- 株価は台帳に入れてよいが、工程 5 の 1(前提の固定)が終わるまで、価値の計算と条件6・7 の採点には使わない。
- 検査: `python3 $S/scripts/gate.py facts $W` → PASS。

## 工程 2: 事業本体と収益構造(報告書 2〜3 章の原稿)

- 読む: `references/product-and-pnl-flow.md` §1〜§2、`references/business-core-method.md` §3(10 層)・§3A(芯)・§4(市場の仮説)。
- 書く(`report.md` の 2〜3 章):
  1. 製品・サービスの 5W1H 台帳(報告売上の 90% 以上を説明)
  2. 損益の流れ(セグメント → 粗利 → 営業費 → 純利益、各段に前年比)と、売上より速く伸びた費用
  3. 事業エンジンの式(原子単位 × 単価 × …)で報告売上を ±5% で再現。できなければ工程 1 に戻る(最大 2 周)
  4. 自己強化ループと、いま成長を律速している段階(制約)
  5. 市場の仮説(出典つき)と、差分の初期仮説
  6. 芯(1 株当たり価値を最も動かす 1〜3 変数)
- 確かめる: `must-rules.md` の C2・C4・C10・C13。

## 工程 3: 成長企業の評価(成長企業だけ)

- 読む: `references/growth-stage-evaluation.md` §1〜§9(初歩の規律)、§10(尺度 G1〜G8)、§12(節点ツリー)、§14(示唆)。
- 書く(報告書の 3・6・7 章と付録): フェーズ、現在と将来の二層の構造、KPI の率の推移、EPS の四半期分解(税・株数・一時要因)、
  フライホイールとバリューチェーンの競合比較、資本モデルの業界比較、信用と資本の制約の同業比較、マクロ要因の両面と
  市場の織り込み、G1〜G8 の採点、節点ツリーの節点(2〜4 個)と確率の根拠、**市場が値段に入れていない示唆を 1 つ以上**。
- 確かめる: `must-rules.md` の C1〜C7・C12。

## 工程 4: 13 条件の採点(conditions.json)

- 読む: `references/condition-guide.md`(判定の軸・目安・落とし穴)。条件5 は「経歴 → 現職 → 担う事業 → 結果」。
- **条件6・7 はここでは採点しない**(株価を使うため)。工程 5 の 3 で採点する。ここでは残りの 11 条件を埋める。
- 作る: `conditions.json`。条件ごとに `grade`・決め手の一文 `reason`・根拠 `evidence`(2 個以上、台帳の id を 1 つ以上)。
  C 以下は `kpi` と `trigger`。成長企業は条件 1・2・3・6・7・11・12・13 に将来の評価 `future_grade` と実現確率 `future_p`。
- 規則: 迷ったら評価を動かさず、決め手の証拠を追加調査する(最大 2 周)。証拠なしに上げも下げもしない。
  「規模が小さいから対象外」にしない。条件6 は閾値を満たせば B(A 寄り)から出発し、市場・同業との乖離で A まで。
- 検査: 条件6・7 を埋めた後(工程 5 の 3)で `python3 $S/scripts/gate.py conditions $W` → PASS。
- 利用者や前工程の見立てがあっても、根拠(台帳の数字)と合わなければ採点を直し、報告に理由を書く(見立てをそのまま写さない)。

## 工程 5: 価値評価(valuation_input.json → valuate.py)

- 読む: `references/valuation-model.md` §3-0〜§3-4(EPS の品質・3 経路・許容 PEG・年度別の表)、
  `references/intrinsic-valuation-credit.md` §1〜§3、`references/scenario-strategy.md` §6。
- 順番(事前登録):
  1. 株価を見る前に、資本コスト(`coe`)・3 経路の EPS(`eps_paths`。過去の伸びの外挿は禁止)・シナリオ(`tree` か
     `scenarios`)・感応度(`sensitivities`。最低でも EPS ±10%、株数が分かれば増資)・成熟年度の ROE(`maturity.roe` と `note`)・
     生存確率(`survival`。借入で成長する企業は倒産確率から。そうでなければ 1.0 と `survival_note` に理由)を書く。
     評価は `conditions_file` で採点表から読む(手で写さない)。項目の意味は `scripts/valuate.py` の冒頭、式は valuation-model §3-4-2。
  2. その後で `prices`(株価)と `edge`(市場との差分があるか)を入れる。`edge` は工程 2 の市場の仮説から決める。
     工程 2 を行っていない・差分が書けないときは false(判断の上限は「買い検討」、即時圏なし)。前提を後から変えたら、理由を付録 B に残す。
  3. 条件6・7 を採点する(condition-guide の定義どおり、現在 PER = 株価 ÷ 12 か月先の EPS)。`gate.py conditions` を通す。
  4. `python3 $S/scripts/valuate.py $W/valuation_input.json` → `valuation.json`・`valuation.md`。検査 NG があれば入力を直す。
  5. 成長企業の将来の評価(`future_grade`)は、節点ツリーの `links` を通じて価値に入る。将来の評価が現在と違う条件は、
     どれかの節点の `links` に入れる(gate valuation が抜けを知らせる)。
- 規則: 妥当 PER は許容 PEG × g だけ(同業の PER・DCF は `cross_checks` に並べるだけで平均しない)。
  信用・資本・希薄化は EPS 経路・確率・株数で数える。比べる期間は `cagr_windows` で揃える。
- 検査: `python3 $S/scripts/gate.py valuation $W` → PASS。確かめる: `must-rules.md` の A 群。

## 工程 6: シナリオの採点・最終判断・投資行動

- 読む: `references/scenario-strategy.md` §1〜§5・§7。
- 書く: シナリオのピースの採点、強気派・弱気派(実在の論者・出典、同じ粒度で数値化)、成立条件、判別 KPI(合格ラインと
  確度の更新値)、リスク(効果で測る。テールは分離して兆候トリガー)、最終判断(`valuation.json` の `decision`)、
  エントリー圏(`entry`)、4 フェーズの投資戦略。判断・エントリー圏は計算機の出力を写す。

## 工程 7: 報告書(report.md → docx)

- 使う: `templates/report_outline.md` の章立て(見出しを残して中身を書く。見出しは主張を含む完全文に置き換える)。
- 読む: `references/report-design.md`、`references/method-detail.md` の「Phase 7」と「報告書全体の品質ゲート」。
- 規則: 日本語で完結(英語の引用は和訳を主に)。専門用語は初出で一言定義。原因は 2 層以上。版の言葉(第N版・前回・今回)と
  修正の履歴は書かない。数字は台帳と計算機の表示値を写す。
- 検査: `python3 $S/scripts/gate.py report $W` → PASS(章・数字の一致・優位の種類・版の言葉)。
- docx にする(docx スキル)。パワポにするかは利用者が決める。作るなら invest-consulting-deck スキル(台帳と
  `valuation.json` をそのまま渡す)。

## 決算の更新(既存の分析を新しい四半期で直す)

1. `facts.json` の `as_of` を新しい四半期にする。前の四半期の値は消さずに残す(時点が付いているので比較に使える)。
2. 前回の仮説と示唆を 1 つずつ、当たり・外れ・一部・未確認で答え合わせし、外れは示唆ごと直す(報告書・資料に修正の一覧は書かない)。
3. 工程 4〜7 をやり直す(採点が変われば許容 PEG と α は計算機が変える)。
4. 資料がある場合は invest-consulting-deck の手順で作り直し、`lint_deck.py pptx` で古い時点の値が残っていないかを確かめる。

## 低予算のモデルで動かすときの規律

- 工程は上から順に 1 つずつ。各工程の「読む」以外の参照は読まない(読む量を減らして規則の取りこぼしを防ぐ)。
- 検査が FAIL のときは、表示された誤りだけを直す。2 回直しても通らないときは、その項目を報告書の「既知の制約」に書き、
  利用者に状況を報告して止まる(推測で埋めて先へ進まない)。
- 判断の工程(工程 2・3・4・6)は、決定表(`condition-guide.md`、`growth-stage-evaluation.md` の表)に当てはめ、
  根拠に台帳の id を書く。表に当てはまらないときは「評価保留」とし、確認 KPI と閾値を置く。
- 複数のモデルを使い分けられるなら: 調査と台帳づくりは安いモデル、工程 4・6 の判定の見直しと報告書の最終確認は
  上位のモデルに任せると、品質と費用の釣り合いが良い。

## 参照ファイルの地図

| ファイル | 使う工程 |
|---|---|
| references/must-rules.md | 全工程(誤りの一覧と検査) |
| references/method-detail.md | Phase 0〜7 の全文(手順の詳細と報告書の品質ゲート) |
| references/research-protocol.md | 1 |
| references/product-and-pnl-flow.md | 2 |
| references/business-core-method.md | 2(10 層・芯・市場の仮説・確認層・リスクの効果測定) |
| references/growth-and-capex-valuation.md | 2・5(設備先行型・利益率の 3 区分) |
| references/growth-stage-evaluation.md | 0・3・4(成長企業) |
| references/structure-thinking.md・structure-map-method.md | 2・7(構造図) |
| references/condition-guide.md | 4 |
| references/valuation-model.md・intrinsic-valuation-credit.md | 5 |
| references/scenario-strategy.md | 5・6 |
| references/report-design.md | 7 |
| scripts/valuate.py・facts.py・gate.py・selftest.py | 計算機・台帳・検査・自己テスト |
| templates/ | 台帳・採点表・計算の入力・報告書の章立て |
| examples/sofi/ | 手本(SoFi、Q3 2026 決算後。台帳・採点表・計算の入出力) |
| CHANGELOG.md | 版の履歴(作業には不要) |
