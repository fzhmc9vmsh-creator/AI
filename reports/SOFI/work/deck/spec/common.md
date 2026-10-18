# SOFI 資料の指示書: 共通ルール(全担当が最初に読む)

作業フォルダ: `/home/user/AI/reports/SOFI/work/deck/`(以下 deck/)。部品は deck/lib.js、見出し・タイトル・順番は deck/meta.js(Opus が作成済み。書き換えない)。

## 1. 作り方(写経)
- 各スライドは「ORCL 版の同じ型のスライド」を写して作る。手本のソースは `/home/user/AI/reports/ORCL/work/deck/slides/<id>.js`(指示書に「手本: ORCL sXX」と書く)。
  - 手本の関数・座標・列幅・色の使い方をそのまま使い、**中身(文字・数値)だけ**を本指示書の値に置き換える。
  - ORCL の数値・社名・文言を 1 つも残さない(Oracle、OCI、GW、OpenAI などが残っていたら不合格)。
- 書き出し先: `deck/slides/<id>.js`。形は `module.exports = function build(pres, L) { … }`。
- **タイトルとページ番号はスライドのファイルに書かない**(meta.js の title が優先され、番号は自動)。`L.contentSlide(pres, { kicker, source })` だけを渡す。評価バッジがあるスライドは `grade` と `condNo` も渡す(手本どおり)。
- 数値・文言は本指示書のものだけを使う。指示書に無い数値を足さない。足りなければ、作業を止めて返答で報告する。
- 日本語で書く。英略語は指示書の表記のまま。

## 2. 確認(1 枚ずつ必ず行う)
1. `cd /home/user/AI/reports/SOFI/work/deck && node one.js <番号>`(例: `node one.js 08b`、`node one.js 17`)
2. 出力の「図の重なり 0 件」と `RESULT: PASS`(Blocker 0・Major 0)を確かめる。Minor も、画像で実際に起きていれば直す。
3. 出力された画像 `deck/tmp/<id>.jpg` を Read ツールで**目で見る**。はみ出し・重なり・空白の偏り・読めない小ささがあれば直して 1 からやり直す。
4. 直すときは、座標を大きく動かすより先に**文字を削る・改行位置を "\n" で直す**。末行が 1〜2 文字になる改行、数字と単位の泣き別れ(`455 億` / `ドル`)を作らない。

## 3. 書式の約束(lib.js と deck-rules-v2)
- フォントは lib.js の既定(Meiryo UI)。色は lib.js の `L.C`(primary 197A56・dark 0E4D33・light 86C99B・teal 1BA1A6・red C0392B・amber D68910・text 333333・sub 767676・rule D9D9D9・tint EAF4EE・gray F2F2F2)以外を使わない。
- 評価の色: S 濃緑・A 緑・B 薄緑・C アンバー(`L.GRADE`)。対象外は灰の `N/A`。
- 関係図は `L.flowMap` + `L.mechPanel`(手本 ORCL s08b・s17〜s28)。レーンで領域を分け、自社を事業・資産に分けて合計 10〜14 箱、線に数量、①〜⑥ の番号と右パネルの説明、上がる条件・下がる条件。C の条件は下端に `L.kpiBand`。
- 出所(source)は「出所:」を付けずに書く(lib が付ける)。数値の出所は検索要約経由である旨を本文に書く必要はない(付録 s39 でまとめて書く)。

## 4. 数値の正
- 計算: `/home/user/AI/reports/SOFI/work/calc/out/val.json`(理論株価・経路・感応度)
- 調査: `/home/user/AI/reports/SOFI/work/research/`(1 周目)と `research_r2/`(2 周目)。いずれも WebSearch の要約経由。
- 株価 14.55 ドル(2026-10-16 終値)。最新の確定四半期は Q2 2026(2026 年 4〜6 月、7/29 発表)。Q3 決算は 10/27 予定。

## 5. 返答
完了したら、作ったファイル、各スライドの「図の重なり件数」「監査結果」「画像で直したこと」、指示書どおりにできなかった点だけを短く返す。
