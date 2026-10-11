# 組版パイプライン(Markdown 複数ファイル → Word .docx)

日本語の長い報告書(Markdown 複数ファイル)を、表紙・目次・本文つきの A4 縦 docx に組版する。
内容には一切手を入れない(見出しレベルの調整と体裁だけ)。

## 実行(1行)

```bash
python3 /home/user/AI/reports/security-stocks-2026-10/build/build_docx.py            # build/manifest.json -> manifest の "output"
python3 build/build_docx.py path/to/manifest.json -o out/report.docx                 # 入力・出力を指定
python3 build/build_docx.py --preview                                                # + PDF / PNG を作って目視確認(後述)
```

依存: python3(python-docx, lxml, pypdf)、pandoc 3.x、LibreOffice(`soffice`、目次ページ番号の事前計算とプレビューにのみ使用)、`pdftoppm`(プレビューのみ)。

## manifest.json

結合順序とメタデータ。相対パスは **manifest.json のあるディレクトリ基準**。

```json
{
  "title": "世界のトップ・サイバーセキュリティ銘柄 投資分析報告書",
  "subtitle": "6社の長期保有13条件審査と順位付け",
  "date": "2026-10-11",
  "disclaimer": ["本書は情報提供を目的とし…", "投資判断はご自身の責任で…"],
  "output": "../out/security-stocks-report.docx",
  "parts": [
    {"title": "第I部 総合ランキング", "files": ["../analysis/X_ranking.md"]},
    {"title": "第II部 銘柄別報告書",   "files": ["../analysis/PANW_report.md", "../analysis/CRWD_report.md"]}
  ]
}
```

| キー | 必須 | 説明 |
|---|---|---|
| `title` / `subtitle` / `date` | title のみ必須 | 表紙。`\n` で改行可。date は `YYYY-MM-DD` なら「2026年10月11日」と表示 |
| `disclaimer` | 任意 | 文字列または文字列の配列。表紙の下部に「免責事項」として固定 |
| `output` | 任意 | 出力 docx(manifest 基準)。省略時は `<manifest名>.docx`。`-o` が優先 |
| `parts[].title` | 任意 | 部の見出し(見出し1)。省略した部は見出し1を出さない |
| `parts[].files` | 必須 | その部に入れる Markdown(順序どおり) |
| `heading_shift` | 任意 | Markdown の見出しを何段下げるか。既定は「部に title があれば 1(`#`→見出し2)、なければ 0」。部ごとにも指定可 |
| `part_divider` | 任意 | true なら部の見出しだけのページを置き、最初のファイルも次ページから始める(既定 false) |
| `toc_levels` / `toc_title` | 任意 | 目次の深さ(既定 3)/ 見出し(既定「目次」) |
| `running_header` / `header_text` / `page_numbers` | 任意 | 各ページ上部の文書名(既定 true・文書名)/ フッターのページ番号(既定 true) |
| `author` / `organization` / `date_label` | 任意 | 表紙の追記・「作成日」のラベル変更 |

見出し構造(既定): 部=見出し1(直前で改ページ)、ファイル先頭の `#`=見出し2(ファイルごとに改ページ)、`##`=見出し3、`###`=見出し4、`####`=見出し5。目次は見出し1〜3。

## 組版仕様(要件との対応)

- **ページ**: A4 縦・余白 20mm(本文幅 170mm)。表紙のみヘッダー/フッターなし。フッター中央にページ番号(PAGE フィールド)。
- **フォント**: 和文「游ゴシック」(eastAsia 指定)、欧文 Arial(Segoe UI は Mac 版 Word に無いため Arial を採用)。本文 10pt、表 8pt、**8列以上の表は 7pt**。
  行送りは `exact`(固定)指定。游ゴシックは内部行間が大きく、倍率指定だと Word と LibreOffice で組が大きくズレるため。
- **表紙 → 目次 → 本文**: 目次は Word の TOC フィールド(`TOC \o "1-3" \h \z \u`)。`settings.xml` の `updateFields` により、**Word で開くと「フィールドを更新しますか」と表示される**(「はい」で目次が最新化)。
  更新前でも空にならないよう、目次の見出し・ページ番号は事前に埋め込み済み(LibreOffice で一度組んだ PDF のしおりからページ番号を取得)。
- **表**: 全罫線、ヘッダー行=濃紺(1F3864)背景+白太字、ヘッダー行を各ページで繰り返し(`tblHeader`)、行の分断禁止(`cantSplit`)、幅=本文幅いっぱい(固定レイアウト、列幅は DXA で `tblGrid` と各セル `tcW` の両方に指定)、セル内余白は小さく(上下 1.5pt・左右 3pt)、偶数行に薄い縞。
  列幅は「内容の自然幅」と「折り返せない最小幅」から自動配分(全角は 1em、半角は文字種別の幅で計算。短いセルは折り返さない)。12 行以下の表は keepNext でページ内に収める。
- **数値列の右寄せ**: 配置未指定の列について、本文セルの 60% 以上が「数字・%・$・¥ 等で始まる/終わる短い値」なら列全体(ヘッダー含む)を右寄せ。「-」「n/a」等は判定から除外。第1列は行ラベルとして常に左寄せ。
  Markdown 側で `---:` / `:---` / `:-:` と明示した場合はそれを優先。
- **画像**: 本文幅(170mm)・高さ 200mm に収まるよう縮小(拡大はしない)、中央揃え、直下に「図: キャプション」(`![キャプション](パス)` の alt テキスト。すでに「図」で始まる場合は重複させない)。画像パスは **各 Markdown のあるディレクトリ基準**。画像が無い場合は警告を出し「[画像なし: …]」を入れる。
- **引用**: 左罫線(太)+灰色背景。**コードブロック**: 等幅(Consolas / MS ゴシック)8.5pt、薄い背景と枠、行の途中で分断しない。**水平線**: 細い灰色罫線。
- **見出し**: 濃紺系で階層を区別(見出し1=22pt 太い下罫線、見出し2=16pt 細い下罫線、見出し3=13pt 青+左バー、見出し4/5=11/10pt 太字)。
- 「…は次のとおり:」のように `:` で終わる段落は、直後の表・コード・図と別ページに分かれない。

## Markdown 側の注意(pandoc 設定)

日本語の長文向けに次のように読み込む(`build_docx.py` の `MD_FORMAT`)。

- ハードラップされた日本語の改行は空白にせず連結する(全角文字の前後。英数字どうしの改行のみ空白になる)。
- 段落の直後に空行なしで続く箇条書き・引用・パイプ表を許容する(表の前後には空行を自動補完)。
- `<br>` はセル内/段落内の改行になる。`<sub>` `<sup>` `<b>` `<i>` も解釈する。HTML コメントは消える。YAML フロントマターは無視。
- **無効化している記法**: `$…$` の数式(`$150〜$200` を誤認しないため)、`~下付き~` / `^上付き^`(`10~20%` を誤認しないため)、`@引用`、生の LaTeX、`smart`(引用符・ダッシュの自動変換)、見出しの自動 ID。
  下付き・上付きが必要なら `<sub>` `<sup>` を使う。
- 入れ子の箇条書きは 2 / 3 / 4 空白のどれでも可。

## 確認用プレビュー

```bash
python3 build/build_docx.py build/sample/manifest.json --preview --preview-dir build/sample/preview --dpi 80
```

LibreOffice で PDF 化し(`<名前>.pdf`)、`pdftoppm -png` で `page-N.png` を出力する。Linux には游ゴシック等が無いため、プレビュー時のみ fontconfig で IPAGothic に置き換えて描画している(docx 自体のフォント指定は変えない)。
**Word 実機ではフォントの字幅が変わるため、改ページ位置は多少ずれる**(行送りを固定しているのでズレは小さい)。

`--no-prefill`(目次のページ番号の事前計算を省略)、`--keep`(pandoc 直後の中間 docx を残す)、`--strict`(画像欠落などの警告で異常終了)も使える。

## 構成

| ファイル | 役割 |
|---|---|
| `build_docx.py` | パイプライン本体(Markdown→AST 結合→pandoc→python-docx/lxml 後処理→目次プリフィル) |
| `make_reference.py` / `reference.docx` | pandoc 用スタイル定義(スタイルを変えるときは前者を編集。`build_docx.py` は更新を検知して `reference.docx` を作り直す) |
| `sample/` | 動作確認一式: `manifest.json`、`sample.md`(12列×20行の表・箇条書き・図・引用・コード)、`sample2.md`(文章量の多い表・長い表・セル内改行)、`sample3.md`、`make_chart.py`(日本語ラベルのグラフ生成)、`sample.docx`、`preview/`(PDF と PNG) |

サンプルの数値・社名はすべて架空。

## 既知の制限

- 目次のページ番号は LibreOffice 組版の値(事前計算)。Word では開いたときの更新確認で「はい」を選ぶと Word 側の正しい番号になる(「いいえ」だと数ページずれる場合がある)。
- 本文直下以外(箇条書き・引用の中)の表は、罫線・ヘッダー色は付くが列幅の自動配分と数値右寄せの対象外。
- 表のセル結合は pandoc のグリッド表で表現できる範囲のみ(列幅計算では結合セルを無視)。
- 横向きページには対応しない(12 列の表も縦 A4 に 7pt で収める)。
- Word の「更新確認」ダイアログは仕様上避けられない(ユーザーに更新を促す設定のため)。
