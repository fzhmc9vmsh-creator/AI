# デッキ実装仕様(Opus作成。実装担当はこの数値を「写経」する。発明しない)

## 0. 前提
- python-pptx 1.0.2 で実装。スライド 16:9 = 13.333in × 7.5in。単位は inch で指定。
- 余白: 左右 0.5in、上 0.4in、下 0.45in。コンテンツ領域 x=0.5〜12.833, y=1.45〜6.85。
- フォント: 日本語・英数字とも "Meiryo UI"(east asian も同じ名前を設定)。auto_size は使わない。
  word_wrap=True。テキストボックスは想定幅 +10% の余裕を持たせる(LibreOffice で IPAゴシックに置換されるため)。
- 文字が入らないときは座標を動かさず、文字を削る(原稿側に差し戻す)。

## 1. カラーパレット(これ以外の色は使用禁止。チャートも含む)
PRIMARY=197A56 PRIMARY_DARK=0E4D33 SECONDARY=86C99B ACCENT=1BA1A6 NEG=C0392B AMBER=D68910
TEXT=333333 SUB=767676 RULE=D9D9D9 WHITE=FFFFFF LIGHT_BG=EEF6F1(薄緑背景:テイクアウェイ用) GRAY_BG=F4F4F4
評価バッジ: S=0E4D33 A=197A56 B=86C99B(文字0E4D33) C=D68910 D=E67E22 E=C0392B F=7B241C NA=767676
(E67E22, 7B241C はバッジ専用)

## 2. タイポグラフィ
- メッセージ型タイトル: 20pt Bold, PRIMARY, 位置 (0.5, 0.35) 幅 12.3 高さ 0.85, 最大2行(全角45字×2行が上限)
- キッカー(タイトル直下): 11pt, SUB, 位置 (0.5, 1.12) 幅 12.3 高さ 0.3, 1行
- 本文/表セル: 10.5〜12pt, TEXT
- 大型数値: 40〜54pt Bold
- 出所: 8pt SUB, 位置 (0.5, 6.95) 幅 10.8 高さ 0.35, 「出所: 」で始める
- ページ番号: 8pt SUB, 右下 (12.2, 6.98) 幅 0.65 右寄せ
- 右下フッター左に "© 2026 Growth Theme Research | 投資助言ではありません" を 7pt SUB (8.6,7.18 幅3.5) に任意
- タイトル下のアクセント線・スライド端の装飾バーは禁止。

## 3. 部品(関数として実装し、全スライドはこれだけで組む)
- add_title(slide, title, kicker=None)
- add_source(slide, text) / add_page_number(slide, n)
- badge(slide, x, y, grade, size=0.42): 角丸四角+中央に太字1文字(S〜F/NA)、色は §1
- rank_badge(slide, x, y, rank): 濃緑の円に白字「1」「2」「3」
- box(slide, x,y,w,h, fill=None, line=RULE, text=None, size=11, bold=False, color=TEXT, align='l', valign='t')
- takeaway(slide, x,y,w,h, text): LIGHT_BG 塗り、左に幅0.06in の PRIMARY 縦帯、11pt
- table(slide, x,y,w,h, rows(list of list), col_widths, header=True, font=10.5,
        header_fill=PRIMARY_DARK, header_color=WHITE, zebra=False, row_height=None,
        cell_colors={(r,c):hex}, bold_cells=set()): 罫線は RULE の水平線のみ(縦罫なし)
- arrow(slide, x1,y1,x2,y2, color=SUB, width_pt=1.5, dashed=False, head=True)
- chevron(slide, x,y,w,h, text, fill)
- kpi_card(slide, x,y,w,h, value, label, note=None, color=PRIMARY)
- bar_chart / line_chart: python-pptx のネイティブチャート(XL_CHART_TYPE)で作る。系列色は
  PRIMARY, SECONDARY, ACCENT, SUB の順。予測値は SECONDARY かつ「予」を軸ラベルに付す。
  軸・凡例 9pt。グリッド線は RULE。データラベル 9pt。画像貼り付けは禁止。
- section_divider(prs, chapter_no, chapters(list), current_idx): 濃緑(PRIMARY_DARK)背景の
  トラッカー型目次。左に「目次」ラベル、右に章リスト(番号バッジ+章名)。現在章のみ白文字+
  白地に濃緑数字のバッジ、他章は文字色 86C99B。
- cover(prs, title, subtitle, date): 左〜中央 8.6in 幅の PRIMARY_DARK パネル、白文字タイトル 30pt、
  サブ 14pt、日付 12pt。右側は WHITE。
- closing(prs, text): PRIMARY_DARK 全面+白文字。

## 4. 機械監査スクリプト audit.py(実装必須。PASSログが出るまで完成ではない)
pptx を読み、全 shape について次を検査し、違反を一覧出力、0件なら "AUDIT PASS" を出す:
1. bounds: shape がスライド外(x<0, y<0, x+w>13.333, y+h>7.5)にはみ出していない
2. palette: fill/line/font の RGB が §1 のパレット内
3. font: 全 run のフォント名が Meiryo UI、サイズが 7pt 以上
4. text-fit: テキスト量の推定(全角=1.0em, 半角=0.55em, em=pt/72 in)で、行数×行高(1.25em)が
   ボックス高さを超えない(内側余白 0.05in×2 を考慮)。表セルも検査する
5. overlap: テキストを持つ shape 同士が 0.02in 以上重ならない(意図的な重ね=背景用の塗り box は
   name を "bg_" で始めて除外)
6. title: タイトル位置にテキストがあり、体言止め(末尾が「分析」「について」「一覧」「概要」)でない
7. source: 表紙・目次・中扉・クロージング以外のスライドに「出所:」で始まるテキストがある
