---
name: invest-consulting-deck
description: BCG等の戦略コンサルティングファーム品質のパワーポイント資料を、株式投資の銘柄分析(13条件フレームワーク審査)または個人の資産運用計画(目標額・KPI・借入活用・資本コスト)のテーマで作成するスキル。ユーザーが「銘柄分析をパワポに」「資産運用計画の資料」「コンサル品質のスライド」「BCG風の資料」「投資判断資料」「〇〇(ティッカー/企業名)を審査して資料化」「決算を反映して資料を更新」などと言及したら必ずこのスキルを使うこと。単なるpptx作成依頼でも、テーマが投資・銘柄・資産運用・ポートフォリオ・レバレッジ計画であればこのスキルを優先する。部品(lib.js)・数字の台帳(F())・配置の監査・文言の照合・自己テストを同梱し、低予算のモデルでも同じ品質で作れる。
---

# 投資資料の作り方(手順書)

この文書は**作業の順番と合否の決め方**だけを書いた手順書。詳しい作り方は `references/` にあり、各工程で「読む」と
書いた節だけを読む。デザインの一般規範は bcg-slide-method スキル、分析は meigara-bunseki-method スキル。

## 3 つの約束(どのモデルで動かしても守る)

1. **部品だけで組む。** スライドは `scripts/lib.js` の部品で組み、座標・色・文字の大きさを独自に作らない。
   新しいスライドは `scripts/examples/` の近い手本を写して直す(ゼロから書かない)。
2. **要所の数字は台帳から引く。** タイトル(meta.js)・KPI の札(kpiTiles)・結論の箱(takeaway)・関係図の評価の理由(reason)の
   数字は `F('id')` で `facts_deck.json` から引く。その他の数字は手で書いてよいが、組み上がった資料を `lint_deck.py pptx` で
   照合する(価値評価の数字の一致・古い四半期の値・未確認の値)。
3. **1 枚ずつ検査を通す。** `node one.js <id>` で「図の重なり 0 件」「監査 PASS」「文言の検査 PASS」を確かめ、画像
   (`tmp/<id>.jpg`)を目で見てから次の 1 枚へ進む。検査の道具を書き換えて通すことは禁止。

## 準備(最初に 1 回)

```bash
S=<このスキルのフォルダ>/scripts    # 例: /mnt/skills/user/invest-consulting-deck/scripts
D=<資料の作業フォルダ>              # 例: ./work/TICKER/deck
mkdir -p $D/slides $D/tmp $D/out && cd $D
cp $S/lib.js $S/facts.js $S/facts.py $S/build.js $S/one.js $S/audit_deck.py $S/lint_deck.py .
cp $S/examples/mini/meta.js meta.js          # 章・節・テーマ・なぜ・タイトルの一括管理(案件に合わせて書き換える)
npm i pptxgenjs@3.12.0 && pip install python-pptx
python3 $S/selftest_deck.py                  # 道具の自己テスト。FAIL なら作業を始めない
```

画像化には LibreOffice(soffice)と pdftoppm が要る(無い環境では画像の確認を省き、その旨を納品の報告に書く)。

## 工程 0: 用途の確認(省略しない)

- **最初に「①銘柄分析と②資産運用計画のどちらの資料か」を利用者に質問する**(依頼文から自明に見えても確認する)。
- ① は分析が終わっていることが前提。報告書・`facts.json`・`valuation.json` が無ければ、先に meigara-bunseki-method で分析する
  (資料だけ先に作らない)。② は `references/asset-plan.md`。
- 読む: `references/workflow-detail.md` の Phase 0(必須入力のチェックリスト)。不足は 1 回の質問にまとめて確かめる。

## 工程 1: 台帳を資料用に書き出す

```bash
python3 facts.py export <分析の作業フォルダ>/facts.json <分析の作業フォルダ>/valuation.json -o facts_deck.json --as-of "Q3 2026"
```

- `F('q3.revenue')` は台帳の表示値、`F('val.value.engine')` は計算機の表示値(id は `val.` + `valuation.json` の display のキー)。
- 資料の基準(as_of)と違う四半期の値には、F が自動で「(Q2)」を付ける。推定には「(推定)」、未取得は「未取得」と出る。
- 台帳に無い数字を要所に書きたくなったら、台帳(分析側の facts.json)に足して書き出し直す。手で打って逃げない。

## 工程 2: 構成案 → 利用者の承認(チェックポイント)

- 読む: `references/deck-rules-v2.md`(必須事項の全文)、`references/stock-analysis.md`(銘柄分析の標準構成)、
  `references/workflow-detail.md` の Phase 2。
- 作る: `meta.js`(章・節・テーマ・なぜ見るか・タイトル・順番)。タイトルはメッセージ型の完全文、2 行まで、改行は "\n" で
  意味の切れ目に。タイトルの数字は F で引く。
- 必須の構成(銘柄分析): 結論とエグゼクティブサマリ / 13 条件の評価一覧と構造評価の導出 / **事業理解 3 枚**(積み木 + 5W1H + 用語 /
  事業どうしの関係図 / 注目度の高い成長分野)/ **会社のシナリオ 2 枚**(ストーリー図 / 部品の採点)/ 収益構造 / 成長企業は
  **成長の尺度の章**(フェーズと二層の構造・G1〜G8・獲得投資・単位経済と資本の転換)/ 条件ごとの構造図 / 市場との差分 /
  年度別の理論株価・シナリオ(節点ツリー)・感応度 / 最終判断とエントリー圏 / リスク / 投資行動 / 前提と制約。
- **構成案(目次と各スライドのタイトル)を利用者に示し、承認を得てから工程 3 へ**(承認前に作り始めない)。

## 工程 3: 1 枚ずつ作る

- 読む: `references/design-spec.md`(座標・色・文字)、`scripts/README.md`(部品の一覧)、作るスライドに近い手本。
- 手本: `scripts/examples/mini/slides/`(台帳の引き方: KPI の札・表・チャート)、`examples/s08b.js`(事業どうしの関係図)、
  `examples/s08d_story_map.js`(会社のシナリオ)、`examples/s21_condition5_career.js`(条件5 の経歴図)。
- 1 枚ごとに:
  1. `slides/<id>.js` を手本から写して直す(`module.exports = function build(pres, L) { … }`)。
  2. `node one.js <id>` → 「図の重なり 0 件」「RESULT: PASS」「文言の検査 PASS」を確かめる。「確認:」の行が出たら、その箇所を画像で見る。
  3. `tmp/<id>.jpg` を開いて見る: 文字のはみ出し・隠れ、末行が 1〜2 文字だけの行、数字と単位の泣き別れ、出所の切れ。
  4. 直したら 2 に戻る。2 回直しても通らないときは、表を分ける・文を短くするなど構成を変える。
- 関係図(flowMap)の基準: レーンで領域を分け、10〜14 箱、矢印に数量、①〜⑥ の仕組みを右パネル(mechPanel)で説明、
  上がる条件・下がる条件、重なり 0 件。図の形は事業の形に合わせる(deck-rules-v2 §3)。
- 同じレイアウトを 3 枚以上続けない。1 枚 1 メッセージ。数字には出所(source)を書く。

## 工程 4: 全体を組んで照合する

```bash
node build.js out/deck.pptx                         # 図の重なり 0 件を確かめる
python3 audit_deck.py out/deck.pptx                 # RESULT: PASS
python3 lint_deck.py src .                          # 要所の数字は F で引いているか
python3 lint_deck.py pptx out/deck.pptx --facts facts_deck.json   # 価値評価の数字・古い四半期の値・未確認の値・版の言葉
```

- 4 つすべて PASS するまで納品しない。`lint_deck.py pptx` の誤りは、資料を直すか、台帳が足りないなら台帳を直す
  (同じ数字が別の意味でよく出て誤検知するなら、台帳のその行に `match_terms` か `stale_check: false`)。
- PDF にして全ページの一覧画像を作り、目で見る(ページ番号・章の札・見出し帯の並び、同じ数字がページ間で一致しているか)。
- 読む: `references/workflow-detail.md` の Phase 5(QA チェックリスト)。

## 工程 5: 納品

- `.pptx` と確認用の PDF を出力フォルダに置いて渡す。報告は: 総枚数、結論、検査の結果(重なり・監査・照合)、
  差し替えたくなりそうな前提の数字。
- 資料に版の言葉(第N版・前回・今回・改訂)と修正の一覧を書かない(最終版として出す)。
- 数値の更新・章の追加の再依頼は、既存の資料のソースを直して組み直す(ゼロから作り直さない)。決算の更新は、分析側で
  台帳と計算を更新 → 工程 1 から。古い四半期の値の残りは `lint_deck.py pptx` が止める。

## 低予算のモデルで動かすときの規律

- 1 枚ずつ。複数のスライドを一度に書かない。手本を写してから直す。
- 検査が FAIL のときは表示された誤りだけを直す。座標をむやみに動かさず、文を短くするか改行の位置を変える。
- 画像の確認は省かない(配置の監査で見つからない崩れがある)。「確認:」の行は必ず画像で見る。
- 複数のモデルを使い分けられるなら: スライドの制作は安いモデル、関係図・複合構成と最終の全ページ確認は上位のモデル。

## 参照ファイルの地図

| ファイル | 使う工程 |
|---|---|
| references/deck-rules-v2.md | 2・3(必須事項の全文。見出し帯・事業理解 3 枚・関係図・改行・フォント) |
| references/stock-analysis.md | 2(銘柄分析の標準構成) |
| references/asset-plan.md | 0・2(資産運用計画) |
| references/design-spec.md | 3(デザインの規定) |
| references/workflow-detail.md | 0〜5(作り方の詳細の全文と QA チェックリスト) |
| scripts/README.md | 3(部品の一覧と使い方) |
| scripts/examples/ | 3(手本) |
| scripts/selftest_deck.py | 準備(自己テスト) |
