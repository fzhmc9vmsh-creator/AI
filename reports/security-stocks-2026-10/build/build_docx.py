#!/usr/bin/env python3
"""日本語 Markdown 複数ファイル -> プロ品質 docx 組版パイプライン。

    python3 build_docx.py [manifest.json] [-o 出力.docx] [--preview] [--no-prefill]

流れ
  1. manifest.json を読み、各 Markdown を pandoc で AST(JSON)にして結合
     (見出しレベルのシフト、画像パスの絶対化、日本語の改行処理、<br> 変換などは AST 上で行う)
  2. pandoc(json -> docx、reference.docx でスタイル指定)
  3. python-docx / lxml で後処理: 表紙・目次(TOC フィールド)・表の組版・図の縮小とキャプション・
     引用/コード/罫線・ヘッダー/フッター・設定(開いたとき目次の更新を促す)
  4. (既定) LibreOffice で一度 PDF 化し、目次の「キャッシュ済みページ番号」を埋める
     ※ Word で開くと更新を促される。そこで「はい」を選べば Word 側の正しい番号に置き換わる。
"""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path
from urllib.parse import unquote
from xml.sax.saxutils import escape

import docx
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Mm
from lxml import etree

HERE = Path(__file__).resolve().parent

# --------------------------------------------------------------------------- 定数
NAVY = "1F3864"
BORDER = "8496B0"
ZEBRA = "F2F5FA"
TEXT_W_TW = 9638                      # A4 幅 210mm - 余白 20mm*2 = 170mm (twips)
TEXT_W_EMU = TEXT_W_TW * 635
MAX_IMG_H_EMU = 200 * 36000           # 図の最大高さ 200mm
MARKER = "@@FILESTART@@"
BODY_PT, TABLE_PT, TABLE_SMALL_PT = 10, 8, 7
WIDE_TABLE_COLS = 8                   # この列数以上の表は 7pt

# pandoc markdown の読み込みオプション。日本語向けに:
#   east_asian_line_breaks : 全角文字間の改行を無視(ハードラップされた日本語を自然に連結)
#   lists_without_preceding_blankline / -blank_before_blockquote : 段落直後の箇条書き・引用を許容
#   -smart                 : 引用符・ダッシュを勝手に変換しない
#   -tex_math_dollars      : "$150" 等のドル表記を数式と誤認しない
#   -subscript -superscript: "10~20%" の ~ を下付きと誤認しない
#   -raw_tex -citations -auto_identifiers -implicit_header_references : 想定外の変換を避ける
MD_FORMAT = ("markdown+east_asian_line_breaks+lists_without_preceding_blankline"
             "-blank_before_blockquote-smart-tex_math_dollars-tex_math_single_backslash"
             "-subscript-superscript-raw_tex-latex_macros-citations"
             "-auto_identifiers-implicit_header_references")


# --------------------------------------------------------------------------- 汎用
class BuildError(RuntimeError):
    pass


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


def run(cmd, **kw) -> subprocess.CompletedProcess:
    r = subprocess.run(cmd, capture_output=True, **kw)
    if r.returncode != 0:
        err = r.stderr.decode("utf-8", "replace") if isinstance(r.stderr, bytes) else r.stderr
        raise BuildError(f"command failed: {' '.join(map(str, cmd))}\n{err}")
    return r


def is_wide(ch: str) -> bool:
    return unicodedata.east_asian_width(ch) in ("W", "F")


# --------------------------------------------------------------------------- 1. Markdown 前処理
def normalize_markdown(text: str) -> str:
    """pandoc が表を認識しやすいよう、パイプ表の前後に空行を補う(コードフェンス内は触らない)。"""
    text = text.lstrip("﻿").replace("\r\n", "\n").replace("\r", "\n")
    out: list[str] = []
    fence = None
    prev_is_table = False
    for line in text.split("\n"):
        stripped = line.strip()
        m = re.match(r"^(`{3,}|~{3,})", stripped)
        if m:
            tok = m.group(1)
            if fence is None:
                fence = tok[0] * 3
            elif stripped.startswith(fence):
                fence = None
            out.append(line)
            prev_is_table = False
            continue
        if fence is not None:
            out.append(line)
            continue
        is_table = stripped.startswith("|") and stripped.count("|") >= 2
        if is_table and not prev_is_table and out and out[-1].strip() != "":
            out.append("")
        if (not is_table) and prev_is_table and stripped != "" and not stripped.startswith(":"):
            out.append("")
        out.append(line)
        prev_is_table = is_table
    return "\n".join(out)


# --------------------------------------------------------------------------- 1. AST 操作
def text_inlines(s: str) -> list[dict]:
    out: list[dict] = []
    for i, w in enumerate(s.split(" ")):
        if i:
            out.append({"t": "Space"})
        if w:
            out.append({"t": "Str", "c": w})
    return out


def inline_edge_char(el: dict, last: bool) -> str:
    """インライン要素の先頭/末尾の文字(判定不能なら空文字)。"""
    t = el.get("t")
    c = el.get("c")
    if t == "Str":
        return c[-1] if last else c[0]
    if t in ("Space", "SoftBreak", "LineBreak"):
        return " "
    if t == "Code":
        s = c[1]
        return (s[-1] if last else s[0]) if s else ""
    if t in ("Emph", "Strong", "Strikeout", "Underline", "SmallCaps", "Subscript", "Superscript", "Quoted"):
        inner = c[1] if t == "Quoted" else c
        if not inner:
            return ""
        return inline_edge_char(inner[-1] if last else inner[0], last)
    if t in ("Span", "Link"):
        inner = c[1]
        if not inner:
            return ""
        return inline_edge_char(inner[-1] if last else inner[0], last)
    return ""


HTML_INLINE_MAP = {"sub": "Subscript", "sup": "Superscript", "b": "Strong", "strong": "Strong",
                   "i": "Emph", "em": "Emph", "u": "Underline", "s": "Strikeout", "del": "Strikeout"}


def fix_inline_list(items: list) -> list:
    """インライン列に対する処理: <br>→改行、<sub>等の対応付け、日本語の SoftBreak 除去。"""
    # 1) <br>
    tmp: list = []
    for x in items:
        if isinstance(x, dict) and x.get("t") == "RawInline" and x["c"][0] == "html" \
                and re.fullmatch(r"<br\s*/?>", x["c"][1].strip(), re.I):
            tmp.append({"t": "LineBreak"})
        else:
            tmp.append(x)
    # 2) <sub>..</sub> 等
    changed = True
    while changed:
        changed = False
        for i, x in enumerate(tmp):
            if isinstance(x, dict) and x.get("t") == "RawInline" and x["c"][0] == "html":
                m = re.fullmatch(r"<\s*(sub|sup|b|strong|i|em|u|s|del)\s*>", x["c"][1].strip(), re.I)
                if not m:
                    continue
                tag = m.group(1).lower()
                for j in range(i + 1, len(tmp)):
                    y = tmp[j]
                    if isinstance(y, dict) and y.get("t") == "RawInline" and y["c"][0] == "html" \
                            and re.fullmatch(rf"<\s*/\s*{tag}\s*>", y["c"][1].strip(), re.I):
                        tmp[i:j + 1] = [{"t": HTML_INLINE_MAP[tag], "c": tmp[i + 1:j]}]
                        changed = True
                        break
                if changed:
                    break
    # 3) 日本語の前後にある SoftBreak は空白にしない
    out: list = []
    for i, x in enumerate(tmp):
        if isinstance(x, dict) and x.get("t") == "SoftBreak":
            prev = inline_edge_char(out[-1], True) if out else ""
            nxt = inline_edge_char(tmp[i + 1], False) if i + 1 < len(tmp) else ""
            if (prev and is_wide(prev)) or (nxt and is_wide(nxt)):
                continue
        out.append(x)
    return out


INLINE_TYPES = {"Str", "Space", "SoftBreak", "LineBreak", "Emph", "Strong", "Strikeout", "Code", "RawInline",
                "Link", "Image", "Span", "Note", "Quoted", "Cite", "Math", "Subscript", "Superscript",
                "SmallCaps", "Underline"}
ID_ATTR_INDEX = {"Header": 1, "Div": 0, "Span": 0, "CodeBlock": 0, "Code": 0, "Image": 0, "Link": 0,
                 "Table": 0, "Figure": 0}
HR_XML = '<w:p><w:pPr><w:pStyle w:val="HorizontalRule"/></w:pPr></w:p>'


def ast_text(obj) -> str:
    """AST ノードのプレーンテキスト(表セルの数値判定用)。"""
    if isinstance(obj, list):
        return "".join(ast_text(x) for x in obj)
    if not isinstance(obj, dict):
        return ""
    t, c = obj.get("t"), obj.get("c")
    if t == "Str":
        return c
    if t in ("Space", "SoftBreak", "LineBreak"):
        return " "
    if t == "Code":
        return c[1]
    if t in ("Link", "Span", "Quoted", "Cite"):
        return ast_text(c[1])
    if t in ("Emph", "Strong", "Strikeout", "Underline", "SmallCaps", "Subscript", "Superscript", "Plain", "Para"):
        return ast_text(c)
    return ""


def auto_align_table(tbl: dict) -> None:
    """配置指定のない列(AlignDefault)が数値中心なら右寄せにする。明示指定(:--- / ---: / :-:)は尊重。"""
    colspecs, bodies = tbl["c"][2], tbl["c"][4]
    ncols = len(colspecs)
    texts: dict[int, list[str]] = {j: [] for j in range(ncols)}
    for body in bodies:
        for row in body[3]:                       # 本体行のみ(ヘッダーは判定に使わない)
            col = 0
            for cell in row[1]:
                span = cell[3]
                if span == 1 and col < ncols:
                    texts[col].append(ast_text(cell[4]))
                col += span
    for j, spec in enumerate(colspecs):
        if spec[0]["t"] != "AlignDefault":
            continue
        votes = [v for v in (numeric_like(x) for x in texts[j]) if v is not None]
        if votes and sum(1 for v in votes if v) / len(votes) >= 0.6:
            spec[0] = {"t": "AlignRight"}



class AstCtx:
    def __init__(self, base_dir: Path, prefix: str, warnings: list[str]):
        self.base_dir, self.prefix, self.warnings = base_dir, prefix, warnings


def transform(obj, ctx: AstCtx):
    if isinstance(obj, list):
        out = [transform(x, ctx) for x in obj]
        if out and all(isinstance(x, dict) and x.get("t") in INLINE_TYPES for x in out):
            out = fix_inline_list(out)
        return out
    if not isinstance(obj, dict):
        return obj
    t = obj.get("t")
    if "c" in obj:
        obj["c"] = transform(obj["c"], ctx)
    if t == "HorizontalRule":
        return {"t": "RawBlock", "c": ["openxml", HR_XML]}
    if t == "Table":
        auto_align_table(obj)
    if t in ID_ATTR_INDEX:
        c = obj["c"]
        attr = c[ID_ATTR_INDEX[t]]
        if attr[0]:
            attr[0] = ctx.prefix + attr[0]
    if t == "Link":
        url = obj["c"][2][0]
        if url.startswith("#"):
            obj["c"][2][0] = "#" + ctx.prefix + url[1:]
    if t == "Image":
        url = obj["c"][2][0]
        if not re.match(r"^(https?:|data:|file:)", url):
            path = (ctx.base_dir / unquote(url)).resolve()
            if not path.exists():
                ctx.warnings.append(f"画像が見つかりません: {url} (基準 {ctx.base_dir})")
            obj["c"][2][0] = str(path)
    return obj


def pandoc_ast(md_path: Path, shift: int) -> dict:
    text = normalize_markdown(md_path.read_text(encoding="utf-8-sig"))
    cmd = ["pandoc", "-f", MD_FORMAT, "-t", "json", f"--shift-heading-level-by={shift}"]
    r = run(cmd, input=text.encode("utf-8"))
    if r.stderr:
        log(f"[pandoc:{md_path.name}] " + r.stderr.decode("utf-8", "replace").strip())
    return json.loads(r.stdout)


def compose_ast(manifest: dict, manifest_dir: Path, warnings: list[str]) -> dict:
    base_ast: dict | None = None
    blocks: list[dict] = []
    file_no = 0
    parts = manifest.get("parts")
    if not parts:
        parts = [{"files": manifest.get("files", [])}]
    for part in parts:
        title = part.get("title")
        shift = part.get("heading_shift", manifest.get("heading_shift", 1 if title else 0))
        divider = part.get("part_divider", manifest.get("part_divider", False))
        follows_part_title = False
        if title:
            blocks.append({"t": "Header", "c": [1, ["", [], []], text_inlines(title)]})
            follows_part_title = True
        files = part.get("files", [])
        if not files:
            warnings.append(f"部「{title}」にファイルがありません")
        for fpath in files:
            md = (manifest_dir / fpath).resolve()
            if not md.exists():
                raise BuildError(f"Markdown が見つかりません: {fpath} (manifest 基準: {manifest_dir})")
            file_no += 1
            ast = pandoc_ast(md, shift)
            if base_ast is None:
                base_ast = ast
            fblocks = transform(ast["blocks"], AstCtx(md.parent, f"f{file_no}-", warnings))
            if not (follows_part_title and not divider):
                blocks.append({"t": "Para", "c": [{"t": "Str", "c": MARKER}]})
            blocks.extend(fblocks)
            follows_part_title = False
    if base_ast is None:
        raise BuildError("結合する Markdown がありません")
    base_ast["blocks"] = blocks
    base_ast["meta"] = {}
    return base_ast


# --------------------------------------------------------------------------- OOXML 小道具
PPR_ORDER = ["pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr", "widowControl", "numPr",
             "suppressLineNumbers", "pBdr", "shd", "tabs", "suppressAutoHyphens", "kinsoku", "wordWrap",
             "overflowPunct", "topLinePunct", "autoSpaceDE", "autoSpaceDN", "bidi", "adjustRightInd",
             "snapToGrid", "spacing", "ind", "contextualSpacing", "mirrorIndents", "suppressOverlap", "jc",
             "textDirection", "textAlignment", "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr",
             "sectPr", "pPrChange"]
RPR_ORDER = ["rStyle", "rFonts", "b", "bCs", "i", "iCs", "caps", "smallCaps", "strike", "dstrike", "outline",
             "shadow", "emboss", "imprint", "noProof", "snapToGrid", "vanish", "webHidden", "color", "spacing",
             "w", "kern", "position", "sz", "szCs", "highlight", "u", "effect", "bdr", "shd", "fitText",
             "vertAlign", "rtl", "cs", "em", "lang", "eastAsianLayout", "specVanish", "oMath"]
SETTINGS_ORDER = [
    "writeProtection", "view", "zoom", "removePersonalInformation", "removeDateAndTime",
    "doNotDisplayPageBoundaries", "displayBackgroundShape", "printPostScriptOverText",
    "printFractionalCharacterWidth", "printFormsData", "embedTrueTypeFonts", "embedSystemFonts",
    "saveSubsetFonts", "saveFormsData", "mirrorMargins", "alignBordersAndEdges", "bordersDoNotSurroundHeader",
    "bordersDoNotSurroundFooter", "gutterAtTop", "hideSpellingErrors", "hideGrammaticalErrors",
    "activeWritingStyle", "proofState", "formsDesign", "attachedTemplate", "linkStyles",
    "stylePaneFormatFilter", "stylePaneSortMethod", "documentType", "mailMerge", "revisionView",
    "trackRevisions", "doNotTrackMoves", "doNotTrackFormatting", "documentProtection", "autoFormatOverride",
    "styleLockTheme", "styleLockQFSet", "defaultTabStop", "autoHyphenation", "consecutiveHyphenLimit",
    "hyphenationZone", "doNotHyphenateCaps", "showEnvelope", "summaryLength", "clickAndTypeStyle",
    "defaultTableStyle", "evenAndOddHeaders", "bookFoldRevPrinting", "bookFoldPrinting",
    "bookFoldPrintingSheets", "drawingGridHorizontalSpacing", "drawingGridVerticalSpacing",
    "displayHorizontalDrawingGridEvery", "displayVerticalDrawingGridEvery",
    "doNotUseMarginsForDrawingGridOrigin", "drawingGridHorizontalOrigin", "drawingGridVerticalOrigin",
    "doNotShadeFormData", "noPunctuationKerning", "characterSpacingControl", "printTwoOnOne",
    "strictFirstAndLastChars", "noLineBreaksAfter", "noLineBreaksBefore", "savePreviewPicture",
    "doNotValidateAgainstSchema", "saveInvalidXml", "ignoreMixedContent", "alwaysShowPlaceholderText",
    "doNotDemarcateInvalidXml", "saveXmlDataOnly", "useXSLTWhenSaving", "saveThroughXslt", "showXMLTags",
    "alwaysMergeEmptyNamespace", "updateFields", "hdrShapeDefaults", "footnotePr", "endnotePr", "compat",
    "docVars", "rsids", "mathPr", "attachedSchema", "themeFontLang", "clrSchemeMapping",
    "doNotIncludeSubdocsInStats", "doNotAutoCompressPictures", "forceUpgrade", "captions",
    "readModeInkLockDown", "smartTagType", "schemaLibrary", "shapeDefaults", "doNotEmbedSmartTags",
    "decimalSymbol", "listSeparator"]


def lname(e) -> str:
    return etree.QName(e).localname


def el(tag: str, **attrs) -> etree._Element:
    e = OxmlElement(tag if ":" in tag else "w:" + tag)
    for k, v in attrs.items():
        e.set(qn("w:" + k), str(v))
    return e


def sub(parent, tag: str, **attrs):
    e = el(tag, **attrs)
    parent.append(e)
    return e


def insert_ordered(parent, child, order: list[str]) -> None:
    name = lname(child)
    old = parent.find(child.tag)
    if old is not None:
        parent.remove(old)
    idx = order.index(name)
    pos = len(parent)
    for i, c in enumerate(parent):
        n = lname(c)
        if n in order and order.index(n) > idx:
            pos = i
            break
    parent.insert(pos, child)


def get_ppr(p):
    ppr = p.find(qn("w:pPr"))
    if ppr is None:
        ppr = OxmlElement("w:pPr")
        p.insert(0, ppr)
    return ppr


def ppr_set(p, child) -> None:
    insert_ordered(get_ppr(p), child, PPR_ORDER)


def ppr_del(p, name: str) -> None:
    ppr = p.find(qn("w:pPr"))
    if ppr is not None:
        for c in ppr.findall(qn("w:" + name)):
            ppr.remove(c)


def set_pstyle(p, sid: str) -> None:
    ppr_set(p, el("pStyle", val=sid))


def get_pstyle(p) -> str | None:
    ppr = p.find(qn("w:pPr"))
    if ppr is None:
        return None
    ps = ppr.find(qn("w:pStyle"))
    return ps.get(qn("w:val")) if ps is not None else None


def rpr_set(r, child) -> None:
    rpr = r.find(qn("w:rPr"))
    if rpr is None:
        rpr = OxmlElement("w:rPr")
        r.insert(0, rpr)
    insert_ordered(rpr, child, RPR_ORDER)


def make_run(text: str | None = None, *, tab=False, fld: str | None = None, instr: str | None = None,
             bold=False, color: str | None = None, size_hp: int | None = None):
    r = el("r")
    if bold or color or size_hp:
        if bold:
            rpr_set(r, el("b"))
        if color:
            rpr_set(r, el("color", val=color))
        if size_hp:
            rpr_set(r, el("sz", val=size_hp))
            rpr_set(r, el("szCs", val=size_hp))
    if fld:
        r.append(el("fldChar", fldCharType=fld))
    elif instr is not None:
        it = el("instrText")
        it.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        it.text = instr
        r.append(it)
    elif tab:
        r.append(el("tab"))
    elif text is not None:
        t = el("t")
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        t.text = text
        r.append(t)
    return r


def make_para(text: str | None = None, style: str | None = None, **runkw):
    p = el("p")
    if style:
        set_pstyle(p, style)
    if text is not None:
        p.append(make_run(text, **runkw))
    return p


def para_text(p) -> str:
    return "".join(t.text or "" for t in p.iter(qn("w:t")))


# --------------------------------------------------------------------------- 3a. 設定・ページ
def fix_settings(d: docx.document.Document) -> None:
    st = d.settings.element
    for tag in ("embedSystemFonts", "updateFields", "compat", "themeFontLang"):
        for e in st.findall(qn("w:" + tag)):
            st.remove(e)
    st.append(el("updateFields", val="true"))
    compat = el("compat")
    cs = sub(compat, "compatSetting")
    cs.set(qn("w:name"), "compatibilityMode")
    cs.set(qn("w:uri"), "http://schemas.microsoft.com/office/word")
    cs.set(qn("w:val"), "15")
    st.append(compat)
    st.append(el("themeFontLang", val="en-US", eastAsia="ja-JP"))
    children = list(st)
    for c in children:
        st.remove(c)
    children.sort(key=lambda c: SETTINGS_ORDER.index(lname(c)) if lname(c) in SETTINGS_ORDER else 999)
    for c in children:
        st.append(c)


def setup_page(d: docx.document.Document, manifest: dict) -> None:
    sec = d.sections[0]
    sec.page_width, sec.page_height = Mm(210), Mm(297)
    sec.left_margin = sec.right_margin = sec.top_margin = sec.bottom_margin = Mm(20)
    sec.header_distance = sec.footer_distance = Mm(9)
    sec.different_first_page_header_footer = True      # 表紙にはヘッダー/フッターを出さない

    def field_par(paragraph_el, instr: str, placeholder: str):
        paragraph_el.append(make_run(fld="begin"))
        paragraph_el.append(make_run(instr=f" {instr} "))
        paragraph_el.append(make_run(fld="separate"))
        paragraph_el.append(make_run(placeholder))
        paragraph_el.append(make_run(fld="end"))

    # フッター: ページ番号(中央)
    sec.footer.is_linked_to_previous = False
    fp = sec.footer.paragraphs[0]._p
    for c in list(fp):
        fp.remove(c)
    set_pstyle(fp, "Footer")
    if manifest.get("page_numbers", True):
        field_par(fp, "PAGE", "1")
    # ヘッダー: 文書名(小さく・右寄せ)
    sec.header.is_linked_to_previous = False
    hp = sec.header.paragraphs[0]._p
    for c in list(hp):
        hp.remove(c)
    set_pstyle(hp, "Header")
    if manifest.get("running_header", True):
        hp.append(make_run(manifest.get("header_text") or manifest["title"]))
    else:
        ppr_del(hp, "pBdr")
    # 表紙(1ページ目)用の空ヘッダー/フッター
    sec.first_page_header.is_linked_to_previous = False
    sec.first_page_footer.is_linked_to_previous = False
    for part in (sec.first_page_header, sec.first_page_footer):
        pp = part.paragraphs[0]._p
        set_pstyle(pp, "Footer")


# --------------------------------------------------------------------------- 3b. 表紙
def jp_date(s: str) -> str:
    try:
        d_ = dt.date.fromisoformat(s)
        return f"{d_.year}年{d_.month}月{d_.day}日"
    except (ValueError, TypeError):
        return s or ""


def build_cover(manifest: dict) -> list:
    els = []
    frame_els = []
    # 上部のアクセントバー(段落の下罫線)
    bar = el("p")
    set_pstyle(bar, "Normal")
    ppr_set(bar, el("spacing", before=2000, after=0, line=80, lineRule="exact"))
    pb = el("pBdr")
    sub(pb, "bottom", val="single", sz=48, space=1, color=NAVY)
    ppr_set(bar, pb)
    els.append(bar)
    # タイトル
    for i, line in enumerate(str(manifest["title"]).split("\n")):
        tp = make_para(line, "Title")
        if i == 0:
            ppr_set(tp, el("spacing", before=520, after=120, line=800, lineRule="exact"))
        els.append(tp)
    if manifest.get("subtitle"):
        for line in str(manifest["subtitle"]).split("\n"):
            els.append(make_para(line, "Subtitle"))
    # 細罫線
    rule = el("p")
    set_pstyle(rule, "Normal")
    ppr_set(rule, el("spacing", before=200, after=240, line=40, lineRule="exact"))
    pb = el("pBdr")
    sub(pb, "bottom", val="single", sz=6, space=1, color="A6A6A6")
    ppr_set(rule, pb)
    els.append(rule)
    # メタ情報
    if manifest.get("date"):
        els.append(make_para(f"{manifest.get('date_label', '作成日')}: {jp_date(manifest['date'])}", "CoverMeta"))
    for key in ("organization", "author"):
        if manifest.get(key):
            els.append(make_para(str(manifest[key]), "CoverMeta"))
    # 免責(ページ下部にフレームで固定)
    disc = manifest.get("disclaimer")
    if disc:
        paras = disc if isinstance(disc, list) else str(disc).split("\n")
        frame_first = True
        head = make_para("免責事項", "CoverNote", bold=True)
        all_p = [head] + [make_para(t, "CoverNote") for t in paras if t.strip()]
        for i, p in enumerate(all_p):
            fr = el("framePr", w=TEXT_W_TW - 280, hRule="auto", hSpace=0, wrap="around", vAnchor="margin",
                    hAnchor="margin", xAlign="left", yAlign="bottom")
            ppr_set(p, fr)
            if i > 0:
                ppr_set(p, el("spacing", before=60, after=0, line=260, lineRule="exact"))
            frame_els.append(p)
    return frame_els + els


# --------------------------------------------------------------------------- 3c. 見出し・目次
def collect_headings(body) -> list[dict]:
    heads = []
    for p in body.iter(qn("w:p")):
        sid = get_pstyle(p)
        m = re.fullmatch(r"Heading([1-9])", sid or "")
        if m:
            heads.append({"p": p, "level": int(m.group(1)), "text": para_text(p).strip()})
    return heads


def add_toc_bookmarks(body, heads: list[dict]) -> None:
    ids = [int(b.get(qn("w:id"))) for b in body.iter(qn("w:bookmarkStart")) if b.get(qn("w:id"), "").lstrip("-").isdigit()]
    next_id = max(ids + [9000]) + 1
    for i, h in enumerate(heads):
        name = f"_Toc9{i:07d}"
        h["bm"] = name
        bs = el("bookmarkStart", id=next_id, name=name)
        be = el("bookmarkEnd", id=next_id)
        next_id += 1
        p = h["p"]
        ppr = p.find(qn("w:pPr"))
        p.insert(1 if ppr is not None else 0, bs)
        p.append(be)


def build_toc(heads: list[dict], pages: dict | None, title: str, max_level: int) -> list:
    items = [h for h in heads if h["level"] <= max_level]
    out = []
    tp = make_para(title, "TOCHeading")
    ppr_set(tp, el("pageBreakBefore"))
    out.append(tp)
    if not items:
        return out
    for i, h in enumerate(items):
        p = el("p")
        set_pstyle(p, f"TOC{h['level']}")
        if i == 0:
            p.append(make_run(fld="begin"))
            p.append(make_run(instr=f' TOC \\o "1-{max_level}" \\h \\z \\u '))
            p.append(make_run(fld="separate"))
        link = el("hyperlink", anchor=h["bm"], history=1)
        link.append(make_run(h["text"]))
        link.append(make_run(tab=True))
        link.append(make_run(fld="begin"))
        link.append(make_run(instr=f" PAGEREF {h['bm']} \\h "))
        link.append(make_run(fld="separate"))
        pg = pages.get(id(h["p"])) if pages else None
        link.append(make_run(str(pg) if pg else ""))
        link.append(make_run(fld="end"))
        p.append(link)
        out.append(p)
    endp = el("p")
    endp.append(make_run(fld="end"))
    out.append(endp)
    return out


# --------------------------------------------------------------------------- 3d. 改ページ・キャプション・図
def apply_markers(body) -> int:
    n = 0
    for p in list(body.iter(qn("w:p"))):
        if para_text(p).strip() != MARKER:
            continue
        nxt = p.getnext()
        if nxt is not None and nxt.tag == qn("w:p"):
            ppr_set(nxt, el("pageBreakBefore"))
            p.getparent().remove(p)
        else:
            for c in list(p):
                if c.tag != qn("w:pPr"):
                    p.remove(c)
            set_pstyle(p, "PageBreakMarker")
        n += 1
    return n


def prefix_caption(p, prefix: str, startswith: tuple) -> None:
    ts = list(p.iter(qn("w:t")))
    if not ts:
        return
    text = para_text(p).lstrip()
    if text.startswith(startswith):
        return
    ts[0].text = prefix + (ts[0].text or "")
    ts[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")


def process_figures(body) -> int:
    n = 0
    for p in body.iter(qn("w:p")):
        sid = get_pstyle(p)
        if sid == "ImageCaption":
            prefix_caption(p, "図: ", ("図",))
        elif sid == "TableCaption":
            prefix_caption(p, "表: ", ("表",))
    A = "http://schemas.openxmlformats.org/drawingml/2006/main"
    WP = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
    for inline in body.iter("{%s}inline" % WP):
        ext = inline.find("{%s}extent" % WP)
        if ext is None:
            continue
        cx, cy = int(ext.get("cx")), int(ext.get("cy"))
        # 表セル内の画像は列幅に任せ、ここでは触らない
        in_cell = any(a.tag == qn("w:tc") for a in inline.iterancestors())
        max_w = TEXT_W_EMU if not in_cell else 2000000
        ratio = min(1.0, max_w / cx, MAX_IMG_H_EMU / cy)
        if ratio < 1.0:
            ncx, ncy = int(cx * ratio), int(cy * ratio)
            ext.set("cx", str(ncx))
            ext.set("cy", str(ncy))
            for e in inline.iter("{%s}ext" % A):
                if e.get("cx") is not None:
                    e.set("cx", str(ncx))
                    e.set("cy", str(ncy))
        # 図だけの段落は中央揃え(キャプション段落と切り離されないよう keepNext)
        par = inline.getparent()
        while par is not None and par.tag != qn("w:p"):
            par = par.getparent()
        if par is not None and not in_cell:
            if get_pstyle(par) in (None, "BodyText", "FirstParagraph", "Compact", "Figure", "CaptionedFigure"):
                if len([r for r in par.findall(qn("w:r"))]) == 1:
                    set_pstyle(par, "CaptionedFigure" if get_pstyle(par) == "CaptionedFigure" else "Figure")
                    ppr_set(par, el("jc", val="center"))
        n += 1
    return n


# --------------------------------------------------------------------------- 3e. 表
def em_width(ch: str) -> float:
    ea = unicodedata.east_asian_width(ch)
    if ea in ("W", "F", "A") and ord(ch) > 0x7F:
        return 1.0
    if ea == "H":
        return 0.5
    if ch == " ":
        return 0.28
    if ch.isdigit():
        return 0.556
    if ch.isupper():
        return 0.68
    if ch.islower():
        return 0.52
    if ch in ".,:;'`|!":
        return 0.3
    if ch in "%":
        return 0.89
    if ch in "()[]{}-/":
        return 0.36
    if ord(ch) < 0x80:
        return 0.56
    return 0.6


def line_em(s: str) -> float:
    return sum(em_width(c) for c in s)


def token_ems(s: str) -> list[float]:
    """折り返し不能な塊の幅(em)。全角は1文字ずつ折れる、ASCII は語単位。"""
    out, cur = [], 0.0
    for ch in s:
        if ch.isspace():
            if cur:
                out.append(cur)
            cur = 0.0
        elif is_wide(ch):
            if cur:
                out.append(cur)
                cur = 0.0
            out.append(1.0)
        else:
            cur += em_width(ch)
    if cur:
        out.append(cur)
    return out or [0.0]


def cell_lines(tc) -> list[str]:
    lines: list[str] = []
    for p in tc.findall(qn("w:p")):
        cur = ""
        for node in p.iter():
            if node.tag == qn("w:t"):
                cur += node.text or ""
            elif node.tag == qn("w:tab"):
                cur += " "
            elif node.tag == qn("w:br"):
                lines.append(cur)
                cur = ""
        lines.append(cur)
    return lines


PLACEHOLDER_RE = re.compile(r"^[\-−–—―ーｰ‐・\s]*$|^(n/?a|N/?A|NA|nm|NM|n\.a\.|―|—)$", re.I)
NUM_START_RE = re.compile(r"^[\(（\[\-\+−–△▲▼＋－~～≈約>＞<＜≥≤±]*\s*[$¥￥€£US]*\s*[\(（]?\d")
NUM_END_RE = re.compile(r"(\d|%|％|\$|倍|[xX×]|bps|pp|pt|円|ドル|億|兆|万|千)\)?）?\]?$")
NUM_ALIGN_MAX_EM = 22.0


def numeric_like(text: str) -> bool | None:
    """True=数値らしい / False=文章 / None=空欄・ダッシュ等(判定に参加しない)"""
    t = text.strip()
    if not t or PLACEHOLDER_RE.match(t):
        return None
    t = t.replace(",", "").replace("，", "")
    if not (NUM_START_RE.match(t) or NUM_END_RE.search(t)):
        return False
    wide = sum(1 for c in t if is_wide(c))
    return wide <= 5 and line_em(t) <= NUM_ALIGN_MAX_EM


def compute_widths(cols_nat: list[float], cols_min: list[float], total: int) -> list[int]:
    n = len(cols_nat)
    nat, mn = cols_nat[:], cols_min[:]
    for i in range(n):
        mn[i] = min(mn[i], nat[i])
    sum_nat, sum_min = sum(nat), sum(mn)
    if sum_nat <= total:
        extra = total - sum_nat
        w = [nat[i] + extra * nat[i] / sum_nat for i in range(n)]
    elif sum_min >= total:
        w = [mn[i] * total / sum_min for i in range(n)]
    else:
        rest = total - sum_min
        ex = [nat[i] - mn[i] for i in range(n)]
        sx = sum(ex) or 1
        w = [mn[i] + rest * ex[i] / sx for i in range(n)]
    ws = [int(x) for x in w]
    ws[max(range(n), key=lambda i: ws[i])] += total - sum(ws)
    return ws


def process_table(tbl, stats: dict) -> None:
    grid = tbl.find(qn("w:tblGrid"))
    ncols = len(grid.findall(qn("w:gridCol"))) if grid is not None else 0
    rows = tbl.findall(qn("w:tr"))
    if not rows or ncols == 0:
        return
    small = ncols >= WIDE_TABLE_COLS
    font_pt = TABLE_SMALL_PT if small else TABLE_PT
    cell_style = "TableTextSmall" if small else "TableText"

    # ---- 行・セルの構造を読み取る
    header_n = 0
    for tr in rows:
        trpr = tr.find(qn("w:trPr"))
        if trpr is not None and trpr.find(qn("w:tblHeader")) is not None:
            header_n += 1
        else:
            break
    table = []     # table[r] = list of dict(tc, col, span, lines, vmerge)
    for tr in rows:
        col = 0
        row = []
        for tc in tr.findall(qn("w:tc")):
            tcpr = tc.find(qn("w:tcPr"))
            span = 1
            vm = None
            if tcpr is not None:
                gs = tcpr.find(qn("w:gridSpan"))
                if gs is not None:
                    span = int(gs.get(qn("w:val")))
                vm = tcpr.find(qn("w:vMerge"))
            row.append({"tc": tc, "col": col, "span": span, "lines": cell_lines(tc), "vmerge": vm})
            col += span
        table.append(row)

    # ---- 列幅の計算(内容の自然幅と最小幅から、ページ幅いっぱいに配分)
    pad = 2 * 60 + 12                       # セル左右余白 + 罫線
    unit = font_pt * 20.0                   # 1em を twips で
    nat = [0.0] * ncols
    mnw = [0.0] * ncols
    for r_i, row in enumerate(table):
        bold = 1.07 if r_i < header_n else 1.0
        for c in row:
            if c["span"] != 1:
                continue
            j = c["col"]
            full = max((line_em(l) for l in c["lines"]), default=0.0) * bold
            nat[j] = max(nat[j], full * unit + pad)
            toks = [t for l in c["lines"] for t in token_ems(l)]
            if full <= 4.6 or (r_i < header_n and full <= 6.0):
                need = full                  # 短いセル(見出し語・数値)は折り返させない
            else:
                need = max(max(min(t, 16.0) for t in toks) * bold, 2.0)
            mnw[j] = max(mnw[j], need * unit + pad)
    for j in range(ncols):                   # 全セル空の列などの保険
        nat[j] = max(nat[j], 3 * unit + pad)
        mnw[j] = max(mnw[j], 2 * unit + pad)
    widths = compute_widths(nat, mnw, TEXT_W_TW)

    # ---- 列の配置: AST 段階で決めた配置(pandoc が書いた jc)を採用。jc が無ければ内容から判定
    col_align: dict[int, str] = {}
    norm = {"start": "left", "end": "right", "left": "left", "right": "right", "center": "center", "both": "both"}
    for j in range(ncols):
        jcs, votes = [], []
        for r_i, row in enumerate(table):
            for c in row:
                if c["col"] != j or c["span"] != 1:
                    continue
                p0 = c["tc"].find(qn("w:p"))
                jc = p0.find(qn("w:pPr") + "/" + qn("w:jc")) if p0 is not None else None
                if jc is not None:
                    jcs.append(norm.get(jc.get(qn("w:val")), "left"))
                if r_i >= header_n:
                    votes.append(numeric_like(" ".join(c["lines"])))
        judged = [v for v in votes if v is not None]
        if jcs:
            col_align[j] = max(set(jcs), key=jcs.count)
        elif judged and sum(1 for v in judged if v) / len(judged) >= 0.6:
            col_align[j] = "right"
        else:
            col_align[j] = "left"
    stats["numeric_cols"] = stats.get("numeric_cols", 0) + sum(1 for a in col_align.values() if a == "right")

    # ---- tblPr / tblGrid を作り直す(スキーマ順)
    old_pr = tbl.find(qn("w:tblPr"))
    caption_el = old_pr.find(qn("w:tblCaption")) if old_pr is not None else None
    new_pr = el("tblPr")
    sub(new_pr, "tblStyle", val="Table")
    sub(new_pr, "tblW", w=TEXT_W_TW, type="dxa")
    sub(new_pr, "jc", val="left")
    sub(new_pr, "tblInd", w=0, type="dxa")
    b = sub(new_pr, "tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        sub(b, side, val="single", sz=4, space=0, color=BORDER)
    sub(new_pr, "tblLayout", type="fixed")
    m = sub(new_pr, "tblCellMar")
    sub(m, "top", w=30, type="dxa")
    sub(m, "left", w=60, type="dxa")
    sub(m, "bottom", w=30, type="dxa")
    sub(m, "right", w=60, type="dxa")
    sub(new_pr, "tblLook", val="04A0", firstRow=1 if header_n else 0, lastRow=0, firstColumn=0, lastColumn=0,
        noHBand=0, noVBand=1)
    if caption_el is not None:
        new_pr.append(caption_el)
    if old_pr is not None:
        tbl.replace(old_pr, new_pr)
    else:
        tbl.insert(0, new_pr)
    new_grid = el("tblGrid")
    for w in widths:
        sub(new_grid, "gridCol", w=w)
    tbl.replace(grid, new_grid)

    # ---- 行・セル
    keep_together = len(rows) <= 12
    for r_i, (tr, row) in enumerate(zip(rows, table)):
        is_head = r_i < header_n
        old_trpr = tr.find(qn("w:trPr"))
        new_trpr = el("trPr")
        sub(new_trpr, "cantSplit")
        if is_head:
            sub(new_trpr, "tblHeader")
        if old_trpr is not None:
            tr.replace(old_trpr, new_trpr)
        else:
            idx = 1 if tr.find(qn("w:tblPrEx")) is not None else 0
            tr.insert(idx, new_trpr)
        for c in row:
            tc, j, span = c["tc"], c["col"], c["span"]
            w = sum(widths[j:j + span])
            old_tcpr = tc.find(qn("w:tcPr"))
            new_tcpr = el("tcPr")
            sub(new_tcpr, "tcW", w=w, type="dxa")
            if span > 1:
                sub(new_tcpr, "gridSpan", val=span)
            if c["vmerge"] is not None:
                new_tcpr.append(copy.deepcopy(c["vmerge"]))
            bd = sub(new_tcpr, "tcBorders")
            for side in ("top", "left", "bottom", "right"):
                sub(bd, side, val="single", sz=4, space=0, color=BORDER)
            if is_head:
                sub(new_tcpr, "shd", val="clear", color="auto", fill=NAVY)
            elif (r_i - header_n) % 2 == 1:
                sub(new_tcpr, "shd", val="clear", color="auto", fill=ZEBRA)
            sub(new_tcpr, "vAlign", val="center")
            if old_tcpr is not None:
                tc.replace(old_tcpr, new_tcpr)
            else:
                tc.insert(0, new_tcpr)
            align = col_align.get(j, "left") if span == 1 else "left"
            cell_text = " ".join(c["lines"])
            if align == "right" and not is_head and line_em(cell_text) > NUM_ALIGN_MAX_EM:
                align = "left"
            for p in tc.findall(qn("w:p")):
                set_pstyle(p, cell_style)
                ppr_set(p, el("jc", val=align))
                if is_head or (keep_together and r_i < len(rows) - 1) or r_i == header_n:
                    ppr_set(p, el("keepNext"))
                if is_head:
                    for r in p.iter(qn("w:r")):
                        rpr_set(r, el("b"))
                        rpr_set(r, el("bCs"))
                        rpr_set(r, el("color", val="FFFFFF"))
        # tc の最後が段落でない場合の保険(空セル)
        for c in row:
            if c["tc"].find(qn("w:p")) is None:
                p = el("p")
                set_pstyle(p, cell_style)
                c["tc"].append(p)

    # ---- 表の後ろに余白用の小さい段落を入れる(次が段落の場合)
    nxt = tbl.getnext()
    if nxt is not None and nxt.tag == qn("w:p"):
        if get_pstyle(nxt) != "TableSpacer" and para_text(nxt).strip() != "":
            tbl.addnext(make_para(None, "TableSpacer"))
        elif para_text(nxt).strip() == "" and nxt.find(".//" + qn("w:drawing")) is None:
            set_pstyle(nxt, "TableSpacer")
    stats["tables"] = stats.get("tables", 0) + 1


def process_tables(body, stats: dict) -> None:
    for tbl in list(body.iter(qn("w:tbl"))):
        # 表セル内の入れ子表は対象外、本文直下の表のみ
        if tbl.getparent() is not None and tbl.getparent().tag == qn("w:body"):
            process_table(tbl, stats)


# --------------------------------------------------------------------------- 3f. その他の後処理
def fix_lists(d: docx.document.Document) -> None:
    """pandoc の numbering.xml の箇条書き記号とインデントを整える。"""
    try:
        numbering = d.part.numbering_part.element
    except Exception:
        return
    BULLETS = ["•", "–", "▪", "•", "–", "▪", "•", "–", "▪"]
    for absn in numbering.findall(qn("w:abstractNum")):
        for lvl in absn.findall(qn("w:lvl")):
            fmt = lvl.find(qn("w:numFmt"))
            il = int(lvl.get(qn("w:ilvl")))
            ind = lvl.find(qn("w:pPr") + "/" + qn("w:ind"))
            if ind is not None:
                left = 400 + 360 * il
                ind.set(qn("w:left"), str(left))
                ind.set(qn("w:hanging"), "320" if (fmt is not None and fmt.get(qn("w:val")) == "bullet") else "400")
            tab = lvl.find(qn("w:pPr") + "/" + qn("w:tabs") + "/" + qn("w:tab"))
            if tab is not None and ind is not None:
                tab.set(qn("w:pos"), ind.get(qn("w:left")))
            if fmt is not None and fmt.get(qn("w:val")) == "bullet":
                txt = lvl.find(qn("w:lvlText"))
                if txt is not None:
                    txt.set(qn("w:val"), BULLETS[il % 9])
                rpr = lvl.find(qn("w:rPr"))
                if rpr is not None:
                    lvl.remove(rpr)
                rpr = el("rPr")
                sub(rpr, "rFonts", ascii="Arial", hAnsi="Arial", eastAsia="游ゴシック", cs="Arial", hint="default")
                lvl.append(rpr)


def assemble(stage1: Path, out: Path, manifest: dict, pages: dict[int, int] | None = None,
             page_by_index: list | None = None) -> dict:
    """pandoc 出力に後処理を施して out に保存。pages は「見出し順の index -> ページ」。"""
    d = docx.Document(str(stage1))
    body = d.element.body
    stats: dict = {}

    fix_settings(d)
    fix_lists(d)
    setup_page(d, manifest)
    apply_markers(body)
    process_tables(body, stats)
    stats["images"] = process_figures(body)

    heads = collect_headings(body)
    add_toc_bookmarks(body, heads)
    stats["headings"] = len(heads)
    page_map = None
    if page_by_index is not None:
        page_map = {id(h["p"]): page_by_index[i] for i, h in enumerate(heads) if i < len(page_by_index)}
    cover = build_cover(manifest)
    toc = build_toc(heads, page_map, manifest.get("toc_title", "目次"), int(manifest.get("toc_levels", 3)))
    first = body[0] if len(body) else None
    new_front = cover + toc
    for i, e in enumerate(new_front):
        body.insert(i, e)
    stats["toc_entries"] = sum(1 for h in heads if h["level"] <= int(manifest.get("toc_levels", 3)))
    stats["heads"] = [(h["level"], h["text"]) for h in heads]

    cp = d.core_properties
    cp.title = str(manifest["title"]).replace("\n", " ")
    cp.subject = str(manifest.get("subtitle", "")).replace("\n", " ")
    cp.author = str(manifest.get("author", ""))
    cp.last_modified_by = ""
    cp.comments = ""
    try:
        cp.created = dt.datetime.fromisoformat(manifest["date"]) if manifest.get("date") else dt.datetime.now()
    except ValueError:
        cp.created = dt.datetime.now()
    d.save(str(out))
    return stats


# --------------------------------------------------------------------------- 4. 検証用レンダリング
PREVIEW_FONTCONF = """<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <include ignore_missing="yes">/etc/fonts/fonts.conf</include>
  <!-- 検証用: Word 指定の日本語フォントが無い環境(Linux)では IPAGothic に置き換えて描画する -->
  {rules}
</fontconfig>
"""


def preview_env(tmpdir: Path) -> dict:
    rules = "".join(
        f'<match target="pattern"><test name="family" qual="any"><string>{name}</string></test>'
        f'<edit name="family" mode="assign" binding="strong"><string>IPAGothic</string></edit></match>'
        for name in ("游ゴシック", "Yu Gothic", "YuGothic", "MS Gothic", "ＭＳ ゴシック", "Meiryo", "メイリオ"))
    conf = tmpdir / "fonts-preview.conf"
    conf.write_text(PREVIEW_FONTCONF.format(rules=rules), encoding="utf-8")
    env = os.environ.copy()
    env["FONTCONFIG_FILE"] = str(conf)
    env["SAL_USE_VCLPLUGIN"] = "svp"
    return env


def docx_to_pdf(docx_path: Path, outdir: Path) -> Path:
    if not shutil.which("soffice"):
        raise BuildError("soffice (LibreOffice) が見つかりません")
    outdir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="lo_") as td:
        tdp = Path(td)
        env = preview_env(tdp)
        cmd = ["soffice", f"-env:UserInstallation={(tdp / 'profile').as_uri()}", "--headless",
               "--convert-to", "pdf", "--outdir", str(outdir), str(docx_path)]
        r = subprocess.run(cmd, env=env, capture_output=True, timeout=300)
        pdf = outdir / (docx_path.stem + ".pdf")
        if not pdf.exists():
            raise BuildError("PDF 変換に失敗: " + r.stderr.decode("utf-8", "replace")[-500:])
        return pdf


def norm_title(s: str) -> str:
    return re.sub(r"\s+", "", unicodedata.normalize("NFKC", s))


def pdf_heading_pages(pdf: Path, heading_texts: list[str]) -> list[int | None]:
    """PDF のしおり(LibreOffice が見出しから生成)から、見出し順のページ番号を得る。"""
    from pypdf import PdfReader
    r = PdfReader(str(pdf))
    flat: list[tuple[str, int]] = []

    def rec(items):
        for it in items:
            if isinstance(it, list):
                rec(it)
            else:
                flat.append((norm_title(it.title), r.get_destination_page_number(it) + 1))
    rec(r.outline)
    pages: list[int | None] = []
    j = 0
    for t in heading_texts:
        nt = norm_title(t)
        found = None
        for k in range(j, len(flat)):
            if flat[k][0] == nt:
                found = k
                break
        if found is None:
            pages.append(None)
        else:
            pages.append(flat[found][1])
            j = found + 1
    return pages


def render_png(pdf: Path, outdir: Path, dpi: int = 60, first: int = 1, last: int | None = None) -> list[Path]:
    outdir.mkdir(parents=True, exist_ok=True)
    prefix = outdir / "page"
    cmd = ["pdftoppm", "-png", "-r", str(dpi), "-f", str(first)]
    if last:
        cmd += ["-l", str(last)]
    run(cmd + [str(pdf), str(prefix)])
    return sorted(outdir.glob("page-*.png"))


# --------------------------------------------------------------------------- main
def build(manifest_path: Path, out_path: Path | None, preview: bool, prefill: bool, keep: bool,
          preview_dir: Path | None, dpi: int) -> Path:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if "title" not in manifest:
        raise BuildError("manifest.json に title がありません")
    mdir = manifest_path.parent.resolve()
    if out_path is None:
        out_path = (mdir / manifest["output"]) if manifest.get("output") else mdir / f"{manifest_path.stem}.docx"
    out_path = out_path.resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    ref = HERE / "reference.docx"
    if not ref.exists():
        sys.path.insert(0, str(HERE))
        from make_reference import make_reference
        make_reference(ref)

    warnings: list[str] = []
    ast = compose_ast(manifest, mdir, warnings)
    tmp = Path(tempfile.mkdtemp(prefix="docxbuild_"))
    try:
        stage1 = tmp / "stage1.docx"
        r = run(["pandoc", "-f", "json", "-t", "docx", f"--reference-doc={ref}", "--no-highlight",
                 "-o", str(stage1)], input=json.dumps(ast, ensure_ascii=False).encode("utf-8"))
        if r.stderr:
            log("[pandoc] " + r.stderr.decode("utf-8", "replace").strip())

        stats = assemble(stage1, out_path, manifest)
        # 2 パス目: LibreOffice で組んで見出しのページ番号を目次のキャッシュに入れる
        if prefill and shutil.which("soffice"):
            try:
                pdf = docx_to_pdf(out_path, tmp / "pass1")
                heading_texts = [t for _, t in stats["heads"]]
                pages = pdf_heading_pages(pdf, heading_texts)
                if any(pages):
                    stats = assemble(stage1, out_path, manifest, page_by_index=pages)
                else:
                    warnings.append("見出しのページ番号を取得できませんでした(目次は Word で更新してください)")
            except Exception as e:                     # noqa: BLE001
                warnings.append(f"目次のページ番号プリフィルをスキップ: {e}")
        if preview:
            pdf = docx_to_pdf(out_path, preview_dir or out_path.parent / (out_path.stem + "_preview"))
            pngs = render_png(pdf, pdf.parent, dpi=dpi)
            info = run(["pdfinfo", str(pdf)]).stdout.decode()
            pages_n = re.search(r"Pages:\s+(\d+)", info)
            log(f"preview: {pdf} ({pages_n.group(1) if pages_n else '?'} pages, {len(pngs)} png)")
        if keep:
            shutil.copy(stage1, out_path.with_suffix(".stage1.docx"))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    for w in warnings:
        log(f"WARNING: {w}")
    log(f"OK: {out_path}  (見出し {stats['headings']}, 表 {stats.get('tables', 0)}, 図 {stats['images']}, "
        f"数値列 {stats.get('numeric_cols', 0)})")
    return out_path


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Markdown(複数) -> docx 組版パイプライン")
    ap.add_argument("manifest", nargs="?", default=str(HERE / "manifest.json"))
    ap.add_argument("-o", "--output", help="出力 docx(省略時は manifest の output、なければ manifest と同じ場所)")
    ap.add_argument("--preview", action="store_true", help="LibreOffice で PDF 化し PNG も出力(確認用)")
    ap.add_argument("--preview-dir", help="プレビュー出力先")
    ap.add_argument("--dpi", type=int, default=60, help="プレビュー PNG の解像度")
    ap.add_argument("--no-prefill", action="store_true", help="目次のページ番号プリフィルを行わない")
    ap.add_argument("--keep", action="store_true", help="pandoc 出力(stage1)も残す")
    a = ap.parse_args(argv)
    try:
        build(Path(a.manifest), Path(a.output) if a.output else None, a.preview, not a.no_prefill, a.keep,
              Path(a.preview_dir) if a.preview_dir else None, a.dpi)
    except BuildError as e:
        log(f"ERROR: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
