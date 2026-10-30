# 資料の部品(scripts/)

資料の作業フォルダに写して使う(手順は SKILL.md の「準備」)。部品の引数の詳しい説明は lib.js の各関数の直前のコメント。

## ファイル

| ファイル | 役割 |
|---|---|
| lib.js | デザインの部品(見出し帯・表・チャート・関係図・仕組みパネル・時間軸など)。座標と色の正。`L.F` で台帳を引ける |
| facts.js | 台帳 `facts_deck.json` から表示値を引く `F('id')`・`F.n('id')`(単位なし)・`F.v('id')`(チャート用の数値) |
| facts.py | 台帳の検査と書き出し(meigara-bunseki-method と同じもの): `python3 facts.py export facts.json valuation.json -o facts_deck.json --as-of "Q3 2026"` |
| build.js | meta.js の順に全スライドを組む: `node build.js out/deck.pptx` |
| one.js | 1 枚だけ組んで、図の重なり・配置の監査・文言の検査・画像化: `node one.js 08b` → `tmp/s08b.jpg` |
| audit_deck.py | 配置の監査(範囲・余白・配色・フォント・文字の収まり・重なり・改行・見出し帯・出所) |
| lint_deck.py | 文言の検査(要所の手書きの数字・価値評価の数字の一致・古い四半期の値・未確認の値・版の言葉) |
| selftest_deck.py | 自己テスト(手本を組んで検査が通るか、わざと入れた誤りを止めるか) |

## 手本(examples/)

| ファイル | 何の手本か |
|---|---|
| mini/ | 台帳を使う最小の資料(4 枚): meta.js(タイトルを F で書く)、KPI の札・表・チャート・結論の箱。新しい案件の meta.js はここから写す |
| s08b.js | 事業どうしの関係図(flowMap + mechPanel)。関係図はこの密度と書き方を基準にする |
| s08d_story_map.js | 会社のシナリオ(目標の札 + ストーリー図 + 容量の時間軸) |
| s21_condition5_career.js | 条件5(経営者)を経歴 → 現職 → 担う事業 → 結果で描いた例 |
| meta_orcl_40slides.js | 40 枚の資料の章立ての例(章・節・テーマ・なぜの書き方の参考。数字は手書きなので写すときは F に直す) |

## 手本を写すときに書き換える所(examples/mini は SoFi の台帳の id を使っている)

1. `meta.js`: `DOC_TITLE`・`DOC_AUTHOR`、章(`CH`)・順番(`ORDER`)・各スライドの `theme`・`why`・`title`。
2. `F('id')` の id: 自分の `facts_deck.json` にある id に置き換える(無い id は組み立てが「台帳に無い id」で止まる。
   台帳に足して `facts.py export` をやり直す)。価値評価の id は `val.` + `valuation.json` の display のキー
   (例: `val.value.engine`、`val.decision.<prices の名前>`、`val.gap.engine.<prices の名前>`)。
3. 表紙の文言、各スライドの `kicker`(リード)と `source`(出所)。
4. グラフ: 棒グラフは `valAxisMinVal: 0`(軸を切らない)。色は `L.chartStyle` の既定(規定の色)のまま。

## 部品の選び方

| 伝えたいこと | 部品 | 注意 |
|---|---|---|
| 1 枚の骨組み(見出し帯・タイトル・リード・出所・ページ番号) | `L.contentSlide(pres, {kicker, source, grade, condNo})` | タイトルは meta.js から入る。スライドに書かない |
| 大きな数字 4 つ | `L.kpiTiles(s, [{value, label, note, color}])` | 要所: 数字は F |
| 結論の箱 | `L.takeaway(s, x, y, w, h, text)` | 要所: 数字は F |
| 表 | `L.table(s, rows, {x, y, w, colW, fontSize, rowH})` | 列幅の合計 = w。セルの末行が 1〜2 文字にならないよう "\n" で改行 |
| チャート | `s.addChart(type, data, L.chartStyle({...}))` | 値は `F.v('id')` |
| 事業どうしの関係・仕組み | `L.flowMap(s, spec)` + `L.mechPanel(s, {mech, reason, up, down})` | 10〜14 箱、矢印に数量、①〜⑥ を右パネルで説明。reason の数字は F |
| 流れ図(導出・計算の手順) | `L.flow(s, cols)` | |
| 2 軸の位置づけ | `L.matrix(s, {...})` | |
| 期間の比較 | `L.timeBand(s, {...})` | |
| 監視 KPI の帯(C 以下の条件) | `L.kpiBand(s, text)` | |
| 表紙・目次・中扉・最後 | `L.cover` / `L.agenda` / `L.closing` | |

## 検査の読み方

- `図の重なり N 件`: 0 件にする(関係図のラベル×箱、ラベル×ラベル、線×無関係の箱)。
- `確認:`: 重なりではないが描画で崩れやすい所(例: 仕組みパネルの行幅に近い行)。画像で見て、崩れていれば直す。
- `RESULT: PASS / FAIL`: 配置の監査。Blocker・Major を 0 にする。Minor(末行の孤立など)も直す。
- `lint_deck.py`: `誤り:` を 0 にする。要所の数字は F に、時点の無い古い値は「(Q2)」を付けるか今の値に、未確認の値は削る。
