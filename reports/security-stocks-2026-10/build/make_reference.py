#!/usr/bin/env python3
"""reference.docx (pandoc 用スタイル定義) を生成する。

pandoc 既定の reference.docx をベースに、styles.xml を丸ごと差し替え、
ページ設定(A4 縦・余白 20mm)を埋め込む。スタイル ID は pandoc が参照するものに合わせてある。

使い方:  python3 make_reference.py [出力パス]     (既定: ./reference.docx)
"""
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

# ---------------------------------------------------------------- デザイン定数
NAVY = "1F3864"      # 見出し1・表ヘッダー背景
BLUE = "2F5496"      # 見出し3・リンク
SOFT = "8FAADC"      # 見出し2の下罫線
SLATE = "44546A"     # 見出し4・副題
GRAY = "595959"
BORDER = "8496B0"    # 表罫線
ZEBRA = "F2F5FA"     # 表の縞

LATIN = "Arial"
EAST_ASIA = "游ゴシック"
MONO_LATIN = "Consolas"
MONO_EA = "MS Gothic"

PAGE_W, PAGE_H, MARGIN = 11906, 16838, 1134      # A4, 20mm (twips)
TEXT_W = PAGE_W - 2 * MARGIN                      # 9638


def rfonts(latin=LATIN, ea=EAST_ASIA):
    return (f'<w:rFonts w:ascii="{latin}" w:hAnsi="{latin}" '
            f'w:eastAsia="{ea}" w:cs="{latin}"/>')


def size(pt):
    hp = int(round(pt * 2))
    return f'<w:sz w:val="{hp}"/><w:szCs w:val="{hp}"/>'


def exact(pt):
    """行送りを固定(フォントの内部行間に依存しないので Word / LibreOffice で組が揃う)。"""
    return f'w:line="{int(round(pt * 20))}" w:lineRule="exact"'


def style(sid, name, kind="paragraph", based="Normal", nxt=None, ppr="", rpr="",
          custom=False, ui=None, q=True, link=None, extra=""):
    attrs = f'w:type="{kind}"'
    if custom:
        attrs += ' w:customStyle="1"'
    attrs += f' w:styleId="{sid}"'
    out = [f'<w:style {attrs}>', f'<w:name w:val="{name}"/>']
    if based:
        out.append(f'<w:basedOn w:val="{based}"/>')
    if nxt:
        out.append(f'<w:next w:val="{nxt}"/>')
    if link:
        out.append(f'<w:link w:val="{link}"/>')
    if ui is not None:
        out.append(f'<w:uiPriority w:val="{ui}"/>')
    if q:
        out.append('<w:qFormat/>')
    out.append(extra)
    if ppr:
        out.append(f'<w:pPr>{ppr}</w:pPr>')
    if rpr:
        out.append(f'<w:rPr>{rpr}</w:rPr>')
    out.append('</w:style>')
    return "".join(out)


def build_styles_xml() -> str:
    S = []
    # ---- docDefaults / Normal ------------------------------------------------
    defaults = (
        '<w:docDefaults><w:rPrDefault><w:rPr>'
        + rfonts() + size(10)
        + '<w:lang w:val="en-US" w:eastAsia="ja-JP" w:bidi="ar-SA"/>'
        '</w:rPr></w:rPrDefault>'
        '<w:pPrDefault><w:pPr><w:spacing w:after="0" ' + exact(16) + '/></w:pPr></w:pPrDefault>'
        '</w:docDefaults>'
    )
    S.append('<w:latentStyles w:defLockedState="0" w:defUIPriority="99" w:defSemiHidden="0" '
             'w:defUnhideWhenUsed="0" w:defQFormat="0" w:count="376"/>')

    S.append('<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/>'
             '<w:pPr><w:widowControl/><w:kinsoku/><w:overflowPunct/>'
             '<w:spacing w:before="0" w:after="0" ' + exact(16) + '/></w:pPr></w:style>')
    S.append('<w:style w:type="character" w:default="1" w:styleId="DefaultParagraphFont">'
             '<w:name w:val="Default Paragraph Font"/><w:uiPriority w:val="1"/><w:semiHidden/><w:unhideWhenUsed/></w:style>')
    S.append('<w:style w:type="numbering" w:default="1" w:styleId="NoList"><w:name w:val="No List"/>'
             '<w:uiPriority w:val="99"/><w:semiHidden/><w:unhideWhenUsed/></w:style>')
    S.append('<w:style w:type="table" w:default="1" w:styleId="TableNormal"><w:name w:val="Normal Table"/>'
             '<w:uiPriority w:val="99"/><w:semiHidden/><w:unhideWhenUsed/><w:tblPr><w:tblInd w:w="0" w:type="dxa"/>'
             '<w:tblCellMar><w:top w:w="0" w:type="dxa"/><w:left w:w="108" w:type="dxa"/>'
             '<w:bottom w:w="0" w:type="dxa"/><w:right w:w="108" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>')

    # ---- 本文系 ---------------------------------------------------------------
    S.append(style("BodyText", "Body Text", nxt=None, link="BodyTextChar",
                   ppr='<w:spacing w:before="0" w:after="120" ' + exact(16) + '/>'))
    S.append(style("FirstParagraph", "First Paragraph", based="BodyText", nxt="BodyText", custom=True))
    S.append(style("Compact", "Compact", based="BodyText", custom=True,
                   ppr='<w:spacing w:before="20" w:after="20" ' + exact(16) + '/>'))
    S.append(style("BodyTextChar", "Body Text Char", kind="character", based="DefaultParagraphFont",
                   custom=True, q=False, link="BodyText"))

    # 表紙用(通常は post-process 側で生成)
    S.append(style("Title", "Title", nxt="BodyText", ui=10,
                   ppr='<w:keepNext/><w:keepLines/><w:spacing w:before="0" w:after="160" ' + exact(40) + '/>',
                   rpr='<w:b/><w:bCs/><w:color w:val="' + NAVY + '"/>' + size(28)))
    S.append(style("Subtitle", "Subtitle", nxt="BodyText", ui=11,
                   ppr='<w:keepNext/><w:keepLines/><w:spacing w:before="0" w:after="240" ' + exact(26) + '/>',
                   rpr='<w:color w:val="' + SLATE + '"/>' + size(14)))
    S.append(style("Author", "Author", custom=True, nxt="BodyText",
                   ppr='<w:keepNext/><w:keepLines/>'))
    S.append(style("Date", "Date", nxt="BodyText", ppr='<w:keepNext/><w:keepLines/>'))
    S.append(style("AbstractTitle", "Abstract Title", custom=True, nxt="Abstract",
                   ppr='<w:keepNext/><w:keepLines/><w:spacing w:before="200" w:after="60"/>',
                   rpr='<w:b/><w:color w:val="' + NAVY + '"/>'))
    S.append(style("Abstract", "Abstract", custom=True, nxt="BodyText",
                   ppr='<w:spacing w:before="60" w:after="200"/>', rpr=size(9.5)))
    S.append(style("CoverMeta", "Cover Meta", custom=True, nxt="BodyText",
                   ppr='<w:spacing w:before="0" w:after="60" ' + exact(20) + '/>',
                   rpr='<w:color w:val="404040"/>' + size(11)))
    S.append(style("CoverNote", "Cover Note", custom=True, nxt="BodyText",
                   ppr=('<w:pBdr><w:top w:val="single" w:sz="4" w:space="6" w:color="BFBFBF"/>'
                        '<w:left w:val="single" w:sz="4" w:space="6" w:color="BFBFBF"/>'
                        '<w:bottom w:val="single" w:sz="4" w:space="6" w:color="BFBFBF"/>'
                        '<w:right w:val="single" w:sz="4" w:space="6" w:color="BFBFBF"/></w:pBdr>'
                        '<w:shd w:val="clear" w:color="auto" w:fill="F7F7F7"/>'
                        '<w:spacing w:before="0" w:after="0" ' + exact(13) + '/>'
                        '<w:ind w:left="140" w:right="140"/>'),
                   rpr='<w:color w:val="404040"/>' + size(8)))
    S.append(style("Bibliography", "Bibliography", nxt="Bibliography"))

    # ---- 見出し ---------------------------------------------------------------
    # 見出し1: 濃紺・大・下罫線太・直前で改ページ
    S.append(style("Heading1", "heading 1", nxt="BodyText", ui=9,
                   ppr=('<w:keepNext/><w:keepLines/><w:pageBreakBefore/>'
                        '<w:pBdr><w:bottom w:val="single" w:sz="18" w:space="4" w:color="' + NAVY + '"/></w:pBdr>'
                        '<w:spacing w:before="0" w:after="260" ' + exact(30) + '/><w:outlineLvl w:val="0"/>'),
                   rpr='<w:b/><w:bCs/><w:color w:val="' + NAVY + '"/>' + size(22)))
    # 見出し2: 濃紺・中・下罫線細
    S.append(style("Heading2", "heading 2", nxt="BodyText", ui=9,
                   ppr=('<w:keepNext/><w:keepLines/>'
                        '<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="3" w:color="' + SOFT + '"/></w:pBdr>'
                        '<w:spacing w:before="360" w:after="160" ' + exact(24) + '/><w:outlineLvl w:val="1"/>'),
                   rpr='<w:b/><w:bCs/><w:color w:val="' + NAVY + '"/>' + size(16)))
    # 見出し3: 青・左バー
    S.append(style("Heading3", "heading 3", nxt="BodyText", ui=9,
                   ppr=('<w:keepNext/><w:keepLines/>'
                        '<w:pBdr><w:left w:val="single" w:sz="24" w:space="6" w:color="' + BLUE + '"/></w:pBdr>'
                        '<w:spacing w:before="280" w:after="120" ' + exact(20) + '/>'
                        '<w:ind w:left="200"/><w:outlineLvl w:val="2"/>'),
                   rpr='<w:b/><w:bCs/><w:color w:val="' + BLUE + '"/>' + size(13)))
    S.append(style("Heading4", "heading 4", nxt="BodyText", ui=9,
                   ppr='<w:keepNext/><w:keepLines/><w:spacing w:before="220" w:after="80" ' + exact(18) + '/><w:outlineLvl w:val="3"/>',
                   rpr='<w:b/><w:bCs/><w:color w:val="' + SLATE + '"/>' + size(11)))
    S.append(style("Heading5", "heading 5", nxt="BodyText", ui=9,
                   ppr='<w:keepNext/><w:keepLines/><w:spacing w:before="180" w:after="60" ' + exact(16) + '/><w:outlineLvl w:val="4"/>',
                   rpr='<w:b/><w:bCs/><w:color w:val="' + GRAY + '"/>' + size(10)))
    for n in (6, 7, 8, 9):
        S.append(style(f"Heading{n}", f"heading {n}", nxt="BodyText", ui=9,
                       ppr=f'<w:keepNext/><w:keepLines/><w:spacing w:before="160" w:after="60" ' + exact(16)
                           + f'/><w:outlineLvl w:val="{n - 1}"/>',
                       rpr='<w:b/><w:bCs/><w:i/><w:iCs/><w:color w:val="' + GRAY + '"/>' + size(10)))

    # ---- 引用(左罫線+灰色背景) ----------------------------------------------
    S.append(style("BlockText", "Block Text", based="BodyText", nxt="BodyText", ui=9,
                   ppr=('<w:pBdr>'
                        '<w:top w:val="single" w:sz="4" w:space="3" w:color="F2F2F2"/>'
                        '<w:left w:val="single" w:sz="24" w:space="8" w:color="' + BORDER + '"/>'
                        '<w:bottom w:val="single" w:sz="4" w:space="3" w:color="F2F2F2"/>'
                        '</w:pBdr><w:shd w:val="clear" w:color="auto" w:fill="F2F2F2"/>'
                        '<w:spacing w:before="0" w:after="0" ' + exact(16) + '/>'
                        '<w:ind w:left="300" w:right="120" w:firstLine="0"/>'),
                   rpr='<w:color w:val="404040"/>'))

    # ---- コード --------------------------------------------------------------
    S.append(style("SourceCode", "Source Code", custom=True, based="Normal", nxt="SourceCode", q=True,
                   ppr=('<w:pBdr>'
                        '<w:top w:val="single" w:sz="4" w:space="3" w:color="D0D7E2"/>'
                        '<w:left w:val="single" w:sz="4" w:space="4" w:color="D0D7E2"/>'
                        '<w:bottom w:val="single" w:sz="4" w:space="3" w:color="D0D7E2"/>'
                        '<w:right w:val="single" w:sz="4" w:space="4" w:color="D0D7E2"/></w:pBdr>'
                        '<w:shd w:val="clear" w:color="auto" w:fill="F5F7FA"/>'
                        '<w:wordWrap w:val="0"/>'
                        '<w:spacing w:before="120" w:after="160" ' + exact(13) + '/>'
                        '<w:ind w:left="140" w:right="140"/>'),
                   rpr=rfonts(MONO_LATIN, MONO_EA) + size(8.5)))
    S.append(style("VerbatimChar", "Verbatim Char", kind="character", based="DefaultParagraphFont",
                   custom=True, q=False,
                   rpr=rfonts(MONO_LATIN, MONO_EA) + size(8.5)))

    # ---- 脚注・定義・図表キャプション ---------------------------------------------
    S.append(style("FootnoteText", "footnote text", nxt="FootnoteText", ui=9,
                   ppr='<w:spacing w:before="0" w:after="20" ' + exact(12) + '/>', rpr=size(8)))
    S.append(style("FootnoteReference", "footnote reference", kind="character",
                   based="DefaultParagraphFont", q=False, rpr='<w:vertAlign w:val="superscript"/>'))
    S.append(style("DefinitionTerm", "Definition Term", custom=True, nxt="Definition",
                   ppr='<w:keepNext/><w:keepLines/><w:spacing w:before="60" w:after="0" ' + exact(16) + '/>',
                   rpr='<w:b/><w:bCs/>'))
    S.append(style("Definition", "Definition", custom=True,
                   ppr='<w:spacing w:before="0" w:after="80" ' + exact(16) + '/><w:ind w:left="400"/>'))
    S.append(style("Caption", "caption", nxt="Normal", ui=35,
                   ppr='<w:spacing w:before="60" w:after="120" ' + exact(15) + '/>',
                   rpr='<w:color w:val="404040"/>' + size(9)))
    S.append(style("TableCaption", "Table Caption", based="Caption", custom=True,
                   ppr='<w:keepNext/><w:spacing w:before="200" w:after="80" ' + exact(15) + '/>',
                   rpr='<w:b/><w:bCs/>'))
    S.append(style("ImageCaption", "Image Caption", based="Caption", custom=True,
                   ppr='<w:spacing w:before="40" w:after="240" ' + exact(15) + '/><w:jc w:val="center"/>'))
    S.append(style("Figure", "Figure", custom=True,
                   ppr='<w:spacing w:before="120" w:after="0" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/>'))
    S.append(style("CaptionedFigure", "Captioned Figure", based="Figure", custom=True,
                   ppr='<w:keepNext/>'))

    # ---- 表 -------------------------------------------------------------------
    S.append('<w:style w:type="table" w:styleId="Table"><w:name w:val="Table"/><w:basedOn w:val="TableNormal"/>'
             '<w:uiPriority w:val="59"/><w:qFormat/><w:tblPr><w:tblInd w:w="0" w:type="dxa"/>'
             '<w:tblBorders>'
             f'<w:top w:val="single" w:sz="4" w:space="0" w:color="{BORDER}"/>'
             f'<w:left w:val="single" w:sz="4" w:space="0" w:color="{BORDER}"/>'
             f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="{BORDER}"/>'
             f'<w:right w:val="single" w:sz="4" w:space="0" w:color="{BORDER}"/>'
             f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{BORDER}"/>'
             f'<w:insideV w:val="single" w:sz="4" w:space="0" w:color="{BORDER}"/>'
             '</w:tblBorders>'
             '<w:tblCellMar><w:top w:w="30" w:type="dxa"/><w:left w:w="60" w:type="dxa"/>'
             '<w:bottom w:w="30" w:type="dxa"/><w:right w:w="60" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>')
    S.append(style("TableText", "Table Text", custom=True,
                   ppr='<w:spacing w:before="0" w:after="0" ' + exact(12) + '/>', rpr=size(8)))
    S.append(style("TableTextSmall", "Table Text Small", based="TableText", custom=True,
                   ppr='<w:spacing w:before="0" w:after="0" ' + exact(10.5) + '/>', rpr=size(7)))
    S.append(style("TableSpacer", "Table Spacer", custom=True, q=False,
                   ppr='<w:spacing w:before="0" w:after="0" ' + exact(8) + '/>', rpr=size(4)))
    S.append(style("HorizontalRule", "Horizontal Rule", custom=True, q=False,
                   ppr=('<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="A6A6A6"/></w:pBdr>'
                        '<w:spacing w:before="120" w:after="160" ' + exact(4) + '/>'),
                   rpr=size(2)))
    S.append(style("PageBreakMarker", "Page Break Marker", custom=True, q=False,
                   ppr='<w:pageBreakBefore/><w:spacing w:before="0" w:after="0" ' + exact(1) + '/>', rpr=size(1)))

    # ---- 目次・ヘッダー・フッター ------------------------------------------------
    S.append(style("TOCHeading", "TOC Heading", based="Normal", nxt="BodyText", ui=39,
                   ppr=('<w:keepNext/><w:keepLines/>'
                        '<w:pBdr><w:bottom w:val="single" w:sz="18" w:space="4" w:color="' + NAVY + '"/></w:pBdr>'
                        '<w:spacing w:before="0" w:after="260" ' + exact(30) + '/>'),
                   rpr='<w:b/><w:bCs/><w:color w:val="' + NAVY + '"/>' + size(22)))
    tab = f'<w:tabs><w:tab w:val="right" w:leader="dot" w:pos="{TEXT_W}"/></w:tabs>'
    S.append(style("TOC1", "toc 1", nxt="Normal", ui=39, q=False,
                   ppr=tab + '<w:spacing w:before="140" w:after="30" ' + exact(16) + '/><w:ind w:right="560"/>',
                   rpr='<w:b/><w:bCs/><w:color w:val="' + NAVY + '"/>' + size(10.5)))
    S.append(style("TOC2", "toc 2", nxt="Normal", ui=39, q=False,
                   ppr=tab + '<w:spacing w:before="20" w:after="10" ' + exact(15) + '/><w:ind w:left="240" w:right="560"/>',
                   rpr=size(10)))
    S.append(style("TOC3", "toc 3", nxt="Normal", ui=39, q=False,
                   ppr=tab + '<w:spacing w:before="0" w:after="0" ' + exact(14) + '/><w:ind w:left="480" w:right="560"/>',
                   rpr='<w:color w:val="404040"/>' + size(9)))
    S.append(style("Header", "header", ui=99, q=False,
                   ppr=('<w:pBdr><w:bottom w:val="single" w:sz="4" w:space="3" w:color="BFBFBF"/></w:pBdr>'
                        f'<w:tabs><w:tab w:val="right" w:pos="{TEXT_W}"/></w:tabs>'
                        '<w:spacing w:before="0" w:after="0" ' + exact(12) + '/>'),
                   rpr='<w:color w:val="7F7F7F"/>' + size(8)))
    S.append(style("Footer", "footer", ui=99, q=False,
                   ppr='<w:spacing w:before="0" w:after="0" ' + exact(12) + '/><w:jc w:val="center"/>',
                   rpr='<w:color w:val="595959"/>' + size(9)))
    S.append(style("Hyperlink", "Hyperlink", kind="character", based="DefaultParagraphFont", ui=99, q=False,
                   rpr='<w:color w:val="' + BLUE + '"/><w:u w:val="single"/>'))
    S.append(style("Strong", "Strong", kind="character", based="DefaultParagraphFont", ui=22,
                   rpr='<w:b/><w:bCs/>'))
    S.append(style("SectionNumber", "Section Number", kind="character", based="BodyTextChar", custom=True, q=False))

    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
            + defaults + "".join(S) + '</w:styles>')


def build_document_xml() -> str:
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><w:body>'
            '<w:p><w:pPr><w:pStyle w:val="BodyText"/></w:pPr></w:p>'
            f'<w:sectPr><w:pgSz w:w="{PAGE_W}" w:h="{PAGE_H}"/>'
            f'<w:pgMar w:top="{MARGIN}" w:right="{MARGIN}" w:bottom="{MARGIN}" w:left="{MARGIN}" '
            'w:header="510" w:footer="510" w:gutter="0"/></w:sectPr></w:body></w:document>')


def make_reference(out_path: Path) -> Path:
    out_path = Path(out_path)
    with tempfile.TemporaryDirectory() as td:
        default = Path(td) / "default.docx"
        with open(default, "wb") as f:
            subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"],
                           check=True, stdout=f)
        tmp_out = Path(td) / "ref.docx"
        with zipfile.ZipFile(default) as zin, zipfile.ZipFile(tmp_out, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename == "word/styles.xml":
                    data = build_styles_xml().encode("utf-8")
                elif item.filename == "word/document.xml":
                    data = build_document_xml().encode("utf-8")
                zout.writestr(item, data)
        shutil.copyfile(tmp_out, out_path)
    return out_path


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("reference.docx")
    print(make_reference(target))
