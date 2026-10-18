# blueprints.md — 座標の正と部品の引数

代替版(2026-10-17)。原本は同期フォルダに無いため、invest-consulting-deck の scripts/(lib.js・audit_deck.py)と deck-rules-v2.md から再構成した。

原本の R1〜R11 のブループリントは手元にない。座標は **lib.js の値をそのまま写した**(単位 inch、スライドは 13.333 × 7.5、余白 M = 0.5)。レイアウトを発明せず、部品を呼んで中身だけ差し替える。座標を動かして文字を収めない。入らなければ文字を削る。

## 1. 共通の領域(GRID と見出し帯)

| 領域 | x | y | w | h | 書式 |
|---|---|---|---|---|---|
| 灰帯 `bg_hdr` | 0 | 0 | 13.333 | 0.34 | 塗り F2F2F2 |
| 現在地 `hdr_crumb` | 0.5 | 0.06 | 8.4 | 0.22 | 9pt。節名は濃緑の太字 |
| 章の札 ×4 | 右端 12.833 から左へ | 0.07 | 0.86(間 0.04) | 0.2 | 8pt。今の章だけ緑塗り |
| テーマ札 | 0.5 | 0.42 | 文字幅 + 0.3 | 0.27 | 10pt 太字、0E4D33 塗りに白字 |
| なぜ見るか | 札の右 + 0.16 | 0.42 | 残り全部 | 0.27 | 10pt。見出し語はティールの太字 |
| タイトル `title` | 0.5 | 0.76 | 11.133 | 0.64 | 19pt 太字・197A56・中央縦。右 1.2 はバッジ用 |
| リード `kicker` | 0.5 | 1.41 | 12.333(バッジ付き 11.2) | 0.2 | 9.5pt・767676・1 行 |
| 本文 | 0.5 | 1.62 | 12.333 | 5.13 | 下端 6.75 |
| 出所 `src` | 0.5 | 6.88 | 10.8 | 0.42 | 8pt・767676・下寄せ。「出所: 」は自動 |
| ページ `pg` | 12.233 | 7.0 | 0.6 | 0.25 | 8pt・右寄せ |
| 評価バッジ | 11.883 | 0.76 | 0.95 | 0.74 | `contentSlide({grade, condNo})`。下に「条件N」または「構造評価」 |

`contentSlide(pres, {title, kicker, source, page, grade, condNo})`: 見出し帯は `L.setCtx(id)` で meta.js の値が入ったときだけ描く。title・kicker・ページは meta.js を優先する。

## 2. 領域別の座標

**左右 2 分割**: 区画見出し(h 0.32・12pt 太字・濃緑)を y 1.62 に、左 x 0.5 w 6.05、右 x 6.78 w 6.05。本体は y 2.0〜6.75(h 4.75)。`twoPane` はこの座標で left/right 関数を呼ぶ。

**チャート + 右パネル(`chartPanel`)**
- チャート x 0.5 y 1.65 w 8.35 h 5.0
- takeaway x 9.05 y 1.7 w 3.78 h 1.35(11pt 太字)
- 要点 x 9.05 y 3.2 w 3.78 h 3.45(注ありは 2.6)、10.5pt
- 注 x 9.05 y 5.9 w 3.78 h 0.8、8.5pt 灰
- 右端は 12.83

**KPI タイル(`kpiTiles`)**: 既定 x 0.5 y 1.7 w 12.333 h 1.55、最大 4 枚、間 0.25。値 32pt 太字、ラベル 10.5pt 太字、注 8.5pt。塗り EAF4EE。

**関係図(`flowMap`)**
- 領域: x 0.5 y 1.66 w 8.55、h は 4.66(下端 6.32。下に kpiBand を置く場合)または 5.0(下端 6.66)。右パネル(`mechPanel`)は x 9.25〜12.83。
- 内部: 帯の見出し h 0.3、凡例 h 0.3(下端)、箱の上端は y + 帯 + 0.1。行ピッチ = 余りの高さ ÷ 行数。箱の高さの既定は min(0.82, ピッチ − 0.22)。
- 通路の幅 = (w − 列幅の合計) ÷ (列数 − 1)。コメントはラベルを置く通路を 1.2 以上と推奨。手本 s08b は 1.02(列 1.32/1.36/1.5/1.32)。ラベルが入らないときは番号の丸にして右で説明する。
- 囲み(点線): x −0.07・w +0.14、y +0.03・h −0.06。ラベルは 8pt。
- 凡例: 下端に 4 項目(間 1.55)。
- 手本の呼び方: `name`、`h`、`cols`、`rows`、`nodeH`、`lanes`、`groups`、`nodes`、`edges`。

**`mechPanel`** x 9.25(既定)〜12.833。見出し y 1.62(12pt)。仕組み本文 y 1.98、h = mechH(既定: 上がる/下がる条件ありで 2.55、なしで 2.95)、9.5pt、番号は濃緑の太字。評価の理由(takeaway、10pt)はその下 +0.08 から。上がる/下がる条件は bottom − 0.74、h 0.74、8.5pt。bottom の既定 6.32(s08b は 6.66)。

**`kpiBand`** x 0.5 y 6.42 w 12.333 h 0.42。F2F2F2 地にアンバー枠、9pt、頭に「監視 KPI とトリガー: 」。

**`timeBand`** 手本 s17: x 0.5 y 5.5 w 8.55 h 1.1(上の flowMap は h 3.75)。軸ラベル 8pt、棒の行高 = (h − 0.24) ÷ 本数、棒の高さ ≤ 0.26。位置 px(t) = 軸の左端 + (t − from) ÷ (to − from) × 軸幅。labelW 既定 1.55。

**`flow`** 既定 x 0.5 y 1.7 w 12.333 h 4.4、列の間 0.45(矢印)。列見出し h 0.32・11pt。箱の高さ既定 0.9、箱の間 0.12、10pt。tone: on 緑 / key 濃緑 / off 灰 / それ以外 薄緑。

**`matrix`** 行見出し列 w 1.1、列見出し行 h 0.4。セル 9.5pt。`highlight: [[列, 行]]` を濃緑、tone `rec` を薄緑。

**`table`** 見出し行は 0E4D33 に白字太字、見出しを 0 行目として偶数行が F2F2F2、罫線は下辺のみ D9D9D9 0.75。先頭列は左寄せ、他は中央。

**`takeaway`** 薄緑 EAF4EE 地、内側 左右 0.12・上下 0.08、11pt 太字・濃緑。

## 3. 部品の引数と既定値

| 部品 | 引数 | 既定 |
|---|---|---|
| `table(s, rows, o)` | x y w colW fontSize rowH headFill align name | fontSize 10, rowH 0.3 |
| `bullets(s, items, o)` | x y w h fontSize color name gap | 10.5, 333333, gap 4 |
| `kpiTiles(s, tiles, o)` | tiles = {value, label, note, color} | x 0.5, y 1.7, h 1.55 |
| `chartPanel(pres, s, chart, o)` | chart = {type, data, opts}、o = {takeawayText, points, note} | — |
| `flow(s, cols, o)` | cols = {head, boxes: [{text, tone, h, size, bold}]} | gap 0.45 |
| `matrix(s, o)` | x y w h xLabels yLabels xTitle yTitle cells highlight | — |
| `flowMap(s, spec)` | spec は lib.js 冒頭のコメントが正 | h 4.66 |
| `mechPanel(s, o)` | mech[] reason up down head x mechH bottom fontSize | x 9.25, bottom 6.32 |
| `timeBand(s, o)` | x y w h from to step bars labelW name fmt | step 5 |
| `agenda(pres, current)` | current = 0..3 | — |
| `cover(pres, {title, sub, date})` | 左パネル x 0 w 8.6、題 30pt、副題 14pt | — |
| `closing(pres, {title, note})` | 題 26pt、本文 11pt | — |

`agenda`: 背景 0E4D33、章は y 1.6 + 1.25 × i、現在章以外は透明度 50%。右に「第N章の構成」(x 8.55)と節 + ページ範囲。`cover`: 右半分(x 9.1, w 3.73)に結論の要点を 3 つ置ける。

## 4. 文字数の概算(スロットの検算)

audit_deck.py の式: 1 行の字数 = (枠幅 − 左右余白) × 0.92 ÷ (pt ÷ 72)。高さ = 行数 × pt ÷ 72 × 1.2 + 上下余白 ≦ 枠高 + 0.02。全角 1em、英数 0.56em。

| 枠 | 1 行の字数(全角) |
|---|---|
| title(19pt, w 11.133, 余白 0) | 38 字、2 行まで |
| kicker(9.5pt, w 12.333 / 11.2) | 85 字 / 78 字、1 行 |

他の枠は、設計時に式で概算し、最終は `audit_deck.py` の text-fit に任せる。
