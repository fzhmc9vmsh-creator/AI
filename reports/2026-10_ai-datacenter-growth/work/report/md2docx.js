#!/usr/bin/env node
/**
 * md2docx.js - 日本語の投資分析報告書 Markdown を Word(.docx) に変換する。
 *
 * 使い方:
 *   node md2docx.js input.md output.docx [--no-toc] [--header "ヘッダ文言"] [--strict]
 *
 *   画像の相対パスは input.md のあるディレクトリ基準。
 *   --no-toc  : 表紙があっても目次を作らない
 *   --header  : ヘッダ右の短縮タイトルを明示する(省略時は表紙タイトルから自動生成)
 *   --strict  : 画像欠落などの警告があれば終了コード 1 で終了する(docx 自体は出力する)
 *
 * 依存: docx (npm, v9系)。見つからなければ `npm root -g` から読み込む。
 *
 * 対応する Markdown:
 *   表紙ブロック(先頭の `% タイトル` `% サブタイトル` `% 日付`)、# ～ ####、段落、**太字**、*斜体*、
 *   ~~取消線~~、`コード`、[文字](URL)・<URL>・裸の URL、箇条書き(-, *, +)と番号付き(1.)の入れ子、
 *   GFM 表(整列指定・セル内 <br> 対応)、画像 ![キャプション](path)、引用 >、水平線 ---、
 *   <!-- pagebreak -->、コードブロック(```)。
 */
'use strict';

const fs = require('fs');
const path = require('path');

// ---------------------------------------------------------------------------
// docx の読み込み
// ---------------------------------------------------------------------------
function loadDocx() {
  try {
    return require('docx');
  } catch (e) {
    try {
      const root = require('child_process').execSync('npm root -g', { encoding: 'utf8' }).trim();
      return require(path.join(root, 'docx'));
    } catch (e2) {
      console.error('docx モジュールが見つかりません。NODE_PATH=$(npm root -g) を設定して再実行してください。');
      process.exit(1);
    }
  }
}
const {
  Document, Packer, Paragraph, TextRun, ExternalHyperlink, ImageRun, Table, TableRow, TableCell,
  Header, Footer, PageNumber, AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
  VerticalAlign, LevelFormat, PageBreak, TableOfContents, TableLayoutType, UnderlineType,
  LineRuleType, SectionType,
} = loadDocx();

// ---------------------------------------------------------------------------
// 定数
// ---------------------------------------------------------------------------
const PAGE_W = 11906;               // A4 縦 (DXA)
const PAGE_H = 16838;
const MARGIN = { top: 1134, bottom: 1134, left: 1020, right: 1020, header: 567, footer: 567 }; // 20mm / 18mm
const CONTENT_W = PAGE_W - MARGIN.left - MARGIN.right;                                         // 9866

const NAVY = '1F3864';
const BLUE = '2E5597';
const GRAY_TEXT = '595959';
const ZEBRA = 'F2F2F2';
const QUOTE_BG = 'EDF2F9';
const LINK_BLUE = '0563C1';

const FONT = { ascii: 'Calibri', hAnsi: 'Calibri', cs: 'Calibri', eastAsia: 'Yu Gothic' };
const MONO = { ascii: 'Consolas', hAnsi: 'Consolas', cs: 'Consolas', eastAsia: 'Yu Gothic' };

const BODY_SIZE = 20;               // 10pt (half-points)
const TABLE_SIZE = 17;              // 8.5pt
const TABLE_MIN_COL = 680;          // 最小列幅 (DXA)
const TABLE_MIN_COL_CAP = 1000;     // 「内容が収まる幅」を最小幅とする場合の上限 (DXA)
const TABLE_WEIGHT_CAP = 60;        // 1 列の重みの上限(極端に長いセルが他列を潰さないように)
const UNIT_DXA = 90;                // 表示幅 1 単位(半角1字)の目安 (8.5pt 太字を含む余裕)
const CELL_PAD_DXA = 190;           // セル左右余白 + 余裕
const PAD_UNITS = 2.2;              // セル余白を重みに換算した値
const IMG_MAX_W = Math.floor(CONTENT_W / 15);   // 本文幅 (px, 96dpi 換算)
const IMG_MAX_H = 740;                           // 画像の高さ上限 (px)

const DISCLAIMER = '本報告書は情報整理を目的とし、投資助言ではない。';

const warnings = [];
function warn(msg) {
  warnings.push(msg);
  console.error('WARNING: ' + msg);
}

// ---------------------------------------------------------------------------
// ユーティリティ
// ---------------------------------------------------------------------------
const CJK_RE = /[　-ヿ㐀-鿿豈-﫿＀-￯]/;

function charWidth(cp) {
  if (
    (cp >= 0x1100 && cp <= 0x115f) || (cp >= 0x2e80 && cp <= 0xa4cf) || (cp >= 0xac00 && cp <= 0xd7a3) ||
    (cp >= 0xf900 && cp <= 0xfaff) || (cp >= 0xfe30 && cp <= 0xfe6f) || (cp >= 0xff01 && cp <= 0xff60) ||
    (cp >= 0xffe0 && cp <= 0xffe6) || (cp >= 0x20000 && cp <= 0x3fffd)
  ) return 2;
  // 和文フォントで全角幅になりやすい記号
  if (
    (cp >= 0x2190 && cp <= 0x22ff) || (cp >= 0x25a0 && cp <= 0x26ff) || cp === 0x203b ||
    (cp >= 0x2010 && cp <= 0x2015) || cp === 0x00d7 || cp === 0x00f7
  ) return 2;
  return 1;
}
/** 全角=2、半角=1 で数えた表示幅 */
function displayWidth(str) {
  let w = 0;
  for (const ch of str) w += charWidth(ch.codePointAt(0));
  return w;
}

function readImageInfo(buf) {
  // PNG
  if (buf.length > 24 && buf.slice(0, 8).equals(Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]))) {
    return { type: 'png', width: buf.readUInt32BE(16), height: buf.readUInt32BE(20) };
  }
  // JPEG
  if (buf.length > 4 && buf[0] === 0xff && buf[1] === 0xd8) {
    let p = 2;
    while (p + 9 < buf.length) {
      if (buf[p] !== 0xff) { p++; continue; }
      const marker = buf[p + 1];
      if (marker === 0xd8 || marker === 0x01 || (marker >= 0xd0 && marker <= 0xd7)) { p += 2; continue; }
      const len = buf.readUInt16BE(p + 2);
      if (marker >= 0xc0 && marker <= 0xcf && marker !== 0xc4 && marker !== 0xc8 && marker !== 0xcc) {
        return { type: 'jpg', height: buf.readUInt16BE(p + 5), width: buf.readUInt16BE(p + 7) };
      }
      p += 2 + len;
    }
  }
  // GIF
  if (buf.length > 10 && buf.slice(0, 3).toString('latin1') === 'GIF') {
    return { type: 'gif', width: buf.readUInt16LE(6), height: buf.readUInt16LE(8) };
  }
  return null;
}

// ---------------------------------------------------------------------------
// インライン・パーサ
//   戻り値: セグメント配列
//     { t:'text', text, bold, italic, strike, code, link }  /  { t:'br' }
// ---------------------------------------------------------------------------
const ESCAPABLE = /[\\`*_{}\[\]()#+\-.!|~<>]/;

function matchLink(s, i) {
  // s[i] === '['
  let depth = 0;
  let j = i;
  for (; j < s.length; j++) {
    const c = s[j];
    if (c === '\\') { j++; continue; }
    if (c === '[') depth++;
    else if (c === ']') { depth--; if (depth === 0) break; }
  }
  if (j >= s.length || s[j + 1] !== '(') return null;
  let k = j + 2;
  let d = 1;
  for (; k < s.length; k++) {
    const c = s[k];
    if (c === '\\') { k++; continue; }
    if (c === '(') d++;
    else if (c === ')') { d--; if (d === 0) break; }
  }
  if (k >= s.length) return null;
  let dest = s.slice(j + 2, k).trim();
  const tm = /^(<[^>]*>|\S+)\s+(?:"[^"]*"|'[^']*')$/.exec(dest);
  if (tm) dest = tm[1];
  if (dest.startsWith('<') && dest.endsWith('>')) dest = dest.slice(1, -1);
  return { text: s.slice(i + 1, j), url: dest, end: k + 1 };
}

function findClose(s, from, c, n) {
  for (let j = from; j < s.length; j++) {
    const ch = s[j];
    if (ch === '\\') { j++; continue; }
    if (ch === '`') {
      let len = 1;
      while (s[j + len] === '`') len++;
      const end = s.indexOf('`'.repeat(len), j + len);
      if (end > -1) { j = end + len - 1; continue; }
      j += len - 1;
      continue;
    }
    if (ch === c) {
      let k = 0;
      while (s[j + k] === c) k++;
      const prevOk = j > from && !/\s/.test(s[j - 1]);
      if (c === '~') {
        if (k >= 2 && prevOk) return j;
      } else if (k === n && prevOk) {
        return j;
      } else if (n === 2 && k === 3 && prevOk) {
        return j + 1;                       // **太字 *斜体***
      } else if (n === 1 && k === 3 && prevOk) {
        return j + 2;                       // *斜体 **太字***
      } else if (n === 3 && k > 3 && prevOk) {
        return j + (k - 3);
      }
      j += k - 1;
    }
  }
  return -1;
}

function trimUrl(url) {
  let u = url.replace(/[.,;:!?'"]+$/, '');
  while (u.endsWith(')') && (u.match(/\)/g) || []).length > (u.match(/\(/g) || []).length) u = u.slice(0, -1);
  return u;
}

function safeLink(url) {
  return /^(https?:|mailto:|ftp:)/i.test(url) ? url : null;
}

function parseInlineInto(s, fmt, out) {
  let buf = '';
  const flush = () => {
    if (buf) { out.push(Object.assign({ t: 'text', text: buf }, fmt)); buf = ''; }
  };
  let i = 0;
  while (i < s.length) {
    const c = s[i];

    if (c === '\\' && i + 1 < s.length && ESCAPABLE.test(s[i + 1])) {
      buf += s[i + 1];
      i += 2;
      continue;
    }

    if (c === '<') {
      const rest = s.slice(i, i + 200);
      const br = /^<br\s*\/?>/i.exec(rest);
      if (br) { flush(); out.push({ t: 'br' }); i += br[0].length; continue; }
      const au = /^<((?:https?|mailto):[^\s<>]+)>/i.exec(rest);
      if (au) {
        flush();
        out.push(Object.assign({ t: 'text', text: au[1] }, fmt, { link: au[1] }));
        i += au[0].length;
        continue;
      }
    }

    if (c === '`') {
      let n = 1;
      while (s[i + n] === '`') n++;
      const fence = '`'.repeat(n);
      const end = s.indexOf(fence, i + n);
      if (end > -1) {
        flush();
        let code = s.slice(i + n, end);
        if (code.length > 2 && code.startsWith(' ') && code.endsWith(' ')) code = code.slice(1, -1);
        out.push(Object.assign({ t: 'text', text: code }, fmt, { code: true }));
        i = end + n;
        continue;
      }
      buf += fence;
      i += n;
      continue;
    }

    if (c === '!' && s[i + 1] === '[') {                // 文中の画像は代替テキストのみ
      const l = matchLink(s, i + 1);
      if (l) { buf += l.text; i = l.end; continue; }
    }

    if (c === '[' && !fmt.link) {
      const l = matchLink(s, i);
      if (l) {
        flush();
        const url = safeLink(l.url);
        parseInlineInto(l.text, url ? Object.assign({}, fmt, { link: url }) : fmt, out);
        i = l.end;
        continue;
      }
    }

    if (c === '*' || c === '~') {
      let run = 0;
      while (s[i + run] === c) run++;
      const want = c === '~' ? (run >= 2 ? 2 : 0) : Math.min(run, 3);
      if (want > 0 && i + want < s.length && !/\s/.test(s[i + want])) {
        const close = findClose(s, i + want, c, want);
        if (close > -1) {
          flush();
          const f2 = Object.assign({}, fmt);
          if (c === '~') f2.strike = true;
          else if (want === 1) f2.italic = true;
          else if (want === 2) f2.bold = true;
          else { f2.bold = true; f2.italic = true; }
          parseInlineInto(s.slice(i + want, close), f2, out);
          i = close + want;
          continue;
        }
      }
      buf += c.repeat(run);
      i += run;
      continue;
    }

    if (c === 'h' && !fmt.link && (i === 0 || !/[A-Za-z0-9]/.test(s[i - 1]))) {
      const m = /^https?:\/\/[A-Za-z0-9\-._~:\/?#\[\]@!$&'()+,;=%]+/.exec(s.slice(i));
      if (m) {
        const url = trimUrl(m[0]);
        flush();
        out.push(Object.assign({ t: 'text', text: url }, fmt, { link: url }));
        i += url.length;
        continue;
      }
    }

    buf += c;
    i++;
  }
  flush();
}

function parseInline(s) {
  const out = [];
  parseInlineInto(s, {}, out);
  return out;
}

function segsPlain(segs) {
  return segs.map((s) => (s.t === 'br' ? '\n' : s.text)).join('');
}

function splitSegLines(segs) {
  const lines = [[]];
  for (const s of segs) {
    if (s.t === 'br') lines.push([]);
    else lines[lines.length - 1].push(s);
  }
  while (lines.length > 1 && !lines[lines.length - 1].length) lines.pop();
  return lines;
}

// ---------------------------------------------------------------------------
// ブロック・パーサ
// ---------------------------------------------------------------------------
const isBlank = (l) => /^\s*$/.test(l);
const reHeading = /^\s{0,3}(#{1,6})[ \t]+(.*?)\s*$/;
const reHr = /^\s{0,3}([-*_])(?:[ \t]*\1){2,}[ \t]*$/;
const reQuote = /^\s{0,3}>/;
const reImg = /^\s*!\[([^\]]*)\]\(\s*(<[^>]+>|[^)\s]+)(?:\s+(?:"[^"]*"|'[^']*'))?\s*\)\s*$/;
const reList = /^([ \t]*)([-*+]|\d{1,9}[.)])[ \t]+(.*)$/;
const reFence = /^\s{0,3}(`{3,}|~{3,})\s*(.*)$/;
const rePageBreak = /^\s*<!--\s*pagebreak\s*-->\s*$/i;
const reComment = /^\s*<!--.*-->\s*$/;
const reSep = /^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$/;

function indentOf(ws) {
  return ws.replace(/\t/g, '    ').length;
}

function splitRow(line) {
  let s = line.trim();
  if (s.startsWith('|')) s = s.slice(1);
  if (s.endsWith('|') && !s.endsWith('\\|')) s = s.slice(0, -1);
  const cells = [];
  let cur = '';
  for (let i = 0; i < s.length; i++) {
    if (s[i] === '\\' && s[i + 1] === '|') { cur += '\\|'; i++; continue; }
    if (s[i] === '|') { cells.push(cur.trim()); cur = ''; continue; }
    cur += s[i];
  }
  cells.push(cur.trim());
  return cells;
}

function joinLines(lines) {
  let out = '';
  let prevHard = false;
  lines.forEach((l, idx) => {
    let hard = / {2,}$/.test(l);
    let body = l.replace(/^\s+/, '').replace(/\s+$/, '');
    if (/\\$/.test(body) && !/\\\\$/.test(body)) { body = body.slice(0, -1); hard = true; }
    if (idx > 0 && !prevHard && out && body) {
      const a = out.slice(-1);
      const b = body[0];
      out += CJK_RE.test(a) || CJK_RE.test(b) ? '' : ' ';
    }
    out += body;
    if (hard && idx < lines.length - 1) out += '<br>';
    prevHard = hard && idx < lines.length - 1;
  });
  return out;
}

function parseBlocks(lines) {
  const n = lines.length;
  const blocks = [];
  let i = 0;

  const isTableStart = (k) =>
    k + 1 < n && lines[k].includes('|') && lines[k + 1].includes('|') && reSep.test(lines[k + 1]) &&
    splitRow(lines[k]).length === splitRow(lines[k + 1]).length;

  const startsBlock = (k) => {
    const l = lines[k];
    return (
      reHeading.test(l) || reHr.test(l) || reQuote.test(l) || reFence.test(l) || rePageBreak.test(l) ||
      reComment.test(l) || reImg.test(l) || reList.test(l) || isTableStart(k)
    );
  };

  while (i < n) {
    const line = lines[i];
    if (isBlank(line)) { i++; continue; }

    if (rePageBreak.test(line)) { blocks.push({ type: 'pagebreak' }); i++; continue; }
    if (reComment.test(line)) { i++; continue; }
    if (/^\s*<!--/.test(line)) {                       // 複数行コメントは読み飛ばす
      while (i < n && !/-->/.test(lines[i])) i++;
      i++;
      continue;
    }

    const fence = reFence.exec(line);
    if (fence) {
      const mark = fence[1];
      const code = [];
      i++;
      while (i < n && !new RegExp('^\\s{0,3}' + mark[0] + '{' + mark.length + ',}\\s*$').test(lines[i])) {
        code.push(lines[i]);
        i++;
      }
      i++;
      blocks.push({ type: 'code', lines: code });
      continue;
    }

    const h = reHeading.exec(line);
    if (h) {
      const text = h[2].replace(/\s+#+\s*$/, '').replace(/^#+\s*$/, '');
      blocks.push({ type: 'heading', level: Math.min(h[1].length, 4), segs: parseInline(text) });
      i++;
      continue;
    }

    if (reHr.test(line)) { blocks.push({ type: 'hr' }); i++; continue; }

    if (reQuote.test(line)) {
      const q = [];
      while (i < n && reQuote.test(lines[i])) {
        q.push(lines[i].replace(/^\s{0,3}>[ \t]?/, ''));
        i++;
      }
      const paras = [];
      let cur = [];
      const pushCur = () => {
        if (cur.length) { paras.push({ segs: parseInline(joinLines(cur)) }); cur = []; }
      };
      for (const ql of q) {
        if (isBlank(ql)) { pushCur(); continue; }
        const lm = reList.exec(ql);
        if (lm) {
          pushCur();
          const bullet = /^[-*+]$/.test(lm[2]);
          paras.push({
            segs: parseInline(bullet ? lm[3] : lm[2] + ' ' + lm[3]),
            bullet,
          });
          continue;
        }
        cur.push(ql);
      }
      pushCur();
      blocks.push({ type: 'quote', paras });
      continue;
    }

    if (isTableStart(i)) {
      const header = splitRow(lines[i]);
      const aligns = splitRow(lines[i + 1]).map((c) => {
        const l = c.startsWith(':');
        const r = c.endsWith(':');
        return l && r ? 'center' : r ? 'right' : l ? 'left' : null;
      });
      i += 2;
      const rows = [];
      while (i < n && !isBlank(lines[i]) && lines[i].includes('|') && !reHeading.test(lines[i])) {
        rows.push(splitRow(lines[i]));
        i++;
      }
      const ncol = header.length;
      const norm = (cells) => {
        const c = cells.slice(0, ncol);
        while (c.length < ncol) c.push('');
        return c.map((t) => splitSegLines(parseInline(t)));
      };
      blocks.push({ type: 'table', ncol, aligns, header: norm(header), rows: rows.map(norm) });
      continue;
    }

    const img = reImg.exec(line);
    if (img) {
      let src = img[2];
      if (src.startsWith('<') && src.endsWith('>')) src = src.slice(1, -1);
      blocks.push({ type: 'image', alt: img[1].trim(), src });
      i++;
      continue;
    }

    if (reList.test(line)) {
      const res = parseList(lines, i);
      blocks.push(res.block);
      i = res.next;
      continue;
    }

    // 段落
    const buf = [];
    while (i < n && !isBlank(lines[i])) {
      if (buf.length && startsBlock(i)) break;
      buf.push(lines[i]);
      i++;
    }
    blocks.push({ type: 'para', segs: parseInline(joinLines(buf)) });
  }
  return blocks;

  function parseList(ls, start) {
    const items = [];
    const stack = [];
    let j = start;
    let type0 = null;
    const total = ls.length;
    while (j < total) {
      const l = ls[j];
      if (isBlank(l)) {
        let k = j + 1;
        while (k < total && isBlank(ls[k])) k++;
        if (k < total && reList.test(ls[k]) && !reHr.test(ls[k])) { j = k; continue; }
        break;
      }
      const m = reList.exec(l);
      if (m && !reHr.test(l)) {
        const indent = indentOf(m[1]);
        const ordered = /\d/.test(m[2]);
        while (stack.length > 1 && indent < stack[stack.length - 1]) stack.pop();
        if (!stack.length) stack.push(indent);
        else if (indent >= stack[stack.length - 1] + 2) stack.push(indent);
        const level = Math.min(stack.length - 1, 2);
        if (level === 0) {
          if (type0 === null) type0 = ordered;
          else if (type0 !== ordered) break;          // 先頭階層の種類が変わったら別リスト
        }
        items.push({ level, ordered, num: ordered ? parseInt(m[2], 10) : 0, text: m[3] });
        j++;
        continue;
      }
      if (indentOf(/^[ \t]*/.exec(l)[0]) >= 2 && items.length) {   // 継続行
        const it = items[items.length - 1];
        it.text = joinLines([it.text, l]);
        j++;
        continue;
      }
      break;
    }
    items.forEach((it) => { it.segs = parseInline(it.text); delete it.text; });
    return { block: { type: 'list', items }, next: j };
  }
}

// ---------------------------------------------------------------------------
// 表の列幅計算
// ---------------------------------------------------------------------------
function allocateColumns(weights, total, mins) {
  const n = weights.length;
  mins = mins.slice();
  const sumMin = mins.reduce((a, b) => a + b, 0);
  if (sumMin > total) {                       // 列が多すぎる場合は最小幅を等比で縮める
    for (let k = 0; k < n; k++) mins[k] = Math.floor((mins[k] * total) / sumMin);
  }
  const widths = new Array(n).fill(0);
  const fixed = new Array(n).fill(false);
  for (let guard = 0; guard <= n; guard++) {
    const free = [];
    let used = 0;
    for (let k = 0; k < n; k++) { if (fixed[k]) used += mins[k]; else free.push(k); }
    if (!free.length) break;
    const sumW = free.reduce((a, k) => a + weights[k], 0);
    let changed = false;
    for (const k of free) widths[k] = ((total - used) * weights[k]) / sumW;
    for (const k of free) {
      if (widths[k] < mins[k]) { fixed[k] = true; widths[k] = mins[k]; changed = true; }
    }
    if (!changed) break;
  }
  const res = widths.map((w) => Math.floor(w));
  const diff = total - res.reduce((a, b) => a + b, 0);
  let big = 0;                                // 端数は最も広い列に足す
  for (let k = 1; k < n; k++) if (res[k] > res[big]) big = k;
  res[big] += diff;
  return res;
}

// ---------------------------------------------------------------------------
// ラン生成
// ---------------------------------------------------------------------------
function makeRuns(segs, base = {}) {
  const out = [];
  for (const s of segs) {
    if (s.t === 'br') { out.push(new TextRun({ break: 1 })); continue; }
    const o = {
      text: s.text,
      size: base.size,
      bold: s.bold || base.bold || undefined,
      italics: s.italic || base.italics || undefined,
      strike: s.strike || undefined,
      color: base.color,
    };
    if (s.code) {
      o.font = MONO;
      o.size = base.size ? Math.max(base.size - 1, 14) : undefined;
      o.shading = { type: ShadingType.CLEAR, color: 'auto', fill: ZEBRA };
    }
    if (s.link) {
      o.color = base.linkColor || LINK_BLUE;
      o.underline = { type: UnderlineType.SINGLE, color: o.color };
      out.push(new ExternalHyperlink({ link: s.link, children: [new TextRun(o)] }));
    } else {
      out.push(new TextRun(o));
    }
  }
  return out;
}

// ---------------------------------------------------------------------------
// ブロックの描画
// ---------------------------------------------------------------------------
function createRenderer(baseDir) {
  const numberingConfigs = [];
  const sharedBullets = new Map();
  let numberingSeq = 0;

  function levelsFor(types, starts) {
    return [0, 1, 2].map((l) => {
      const ord = types[l] === 'ordered';
      const left = (ord ? 500 : 440) + l * 440;
      const hanging = ord ? 380 : 280;
      const style = { paragraph: { indent: { left, hanging } } };
      return ord
        ? { level: l, format: LevelFormat.DECIMAL, text: `%${l + 1}.`, alignment: AlignmentType.LEFT, start: starts[l] || 1, style }
        : { level: l, format: LevelFormat.BULLET, text: l === 0 ? '•' : '–', alignment: AlignmentType.LEFT, style };
    });
  }

  function numberingRef(items) {
    const types = [];
    const starts = [];
    for (const it of items) {
      if (types[it.level] === undefined) {
        types[it.level] = it.ordered ? 'ordered' : 'bullet';
        if (it.ordered) starts[it.level] = it.num;
      }
    }
    const hasOrdered = types.includes('ordered');
    const key = [0, 1, 2].map((l) => types[l] || 'bullet').join(',');
    if (!hasOrdered && sharedBullets.has(key)) return sharedBullets.get(key);
    const reference = `list-${++numberingSeq}`;
    numberingConfigs.push({ reference, levels: levelsFor(types, starts) });
    if (!hasOrdered) sharedBullets.set(key, reference);
    return reference;
  }

  const spacingBefore = (gap) => (gap ? { before: gap } : undefined);

  function renderHeading(b, opts) {
    const level = [HeadingLevel.HEADING_1, HeadingLevel.HEADING_2, HeadingLevel.HEADING_3, HeadingLevel.HEADING_4][b.level - 1];
    return new Paragraph({
      heading: level,
      pageBreakBefore: opts.pageBreakBefore || undefined,
      children: makeRuns(b.segs),
    });
  }

  function renderPara(b, gap) {
    return new Paragraph({ spacing: spacingBefore(gap), children: makeRuns(b.segs) });
  }

  function renderList(b, gap) {
    const ref = numberingRef(b.items);
    return b.items.map((it, idx) => {
      const last = idx === b.items.length - 1;
      const sp = { after: last ? 120 : 40 };
      if (idx === 0 && gap) sp.before = gap;
      return new Paragraph({
        numbering: { reference: ref, level: it.level },
        spacing: sp,
        children: makeRuns(it.segs),
      });
    });
  }

  function renderQuote(b, gap) {
    return b.paras.map((p, idx) => {
      const first = idx === 0;
      const last = idx === b.paras.length - 1;
      const sp = { before: first ? 120 + (gap || 0) : 0, after: last ? 200 : 80 };
      const o = { style: 'QuoteBlock', spacing: sp, children: makeRuns(p.segs) };
      if (p.bullet) {
        o.indent = { left: 240 + 200, hanging: 200 };
        o.children = [new TextRun({ text: '・' }), ...o.children];
      }
      return new Paragraph(o);
    });
  }

  function renderHr(gap) {
    return new Paragraph({
      spacing: { before: 120 + (gap || 0), after: 160 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: 'A6A6A6', space: 1 } },
      run: { size: 8 },
      children: [],
    });
  }

  function renderCode(b, gap) {
    const lines = b.lines.length ? b.lines : [''];
    return lines.map((l, idx) => new Paragraph({
      style: 'CodeBlock',
      spacing: { before: idx === 0 ? 40 + (gap || 0) : 0, after: idx === lines.length - 1 ? 160 : 0, line: 252, lineRule: LineRuleType.AUTO },
      children: [new TextRun({ text: l.replace(/\t/g, '    '), font: MONO, size: 17 })],
    }));
  }

  function renderImage(b, gap) {
    const abs = path.resolve(baseDir, decodeSafe(b.src));
    const placeholder = (msg) => {
      warn(msg);
      return [new Paragraph({
        spacing: spacingBefore(gap),
        children: [new TextRun({ text: `[画像を挿入できません: ${b.src}]`, color: 'C00000', bold: true })],
      })];
    };
    if (/^https?:\/\//i.test(b.src)) return placeholder(`リモート画像は未対応です: ${b.src}`);
    let buf;
    try { buf = fs.readFileSync(abs); } catch (e) { return placeholder(`画像が見つかりません: ${abs}`); }
    const info = readImageInfo(buf);
    if (!info) return placeholder(`画像形式を判別できません(PNG/JPEG/GIF のみ対応): ${abs}`);
    const scale = Math.min(1, IMG_MAX_W / info.width, IMG_MAX_H / info.height);
    const width = Math.max(1, Math.round(info.width * scale));
    const height = Math.max(1, Math.round(info.height * scale));
    const name = path.basename(abs);
    const out = [new Paragraph({
      alignment: AlignmentType.CENTER,
      keepNext: !!b.alt,
      spacing: { before: 80 + (gap || 0), after: b.alt ? 40 : 160 },
      children: [new ImageRun({
        type: info.type,
        data: buf,
        transformation: { width, height },
        altText: { title: b.alt || name, description: b.alt || name, name },
      })],
    })];
    if (b.alt) {
      out.push(new Paragraph({ style: 'Caption', children: makeRuns(parseInline(b.alt)) }));
    }
    return out;
  }

  function renderTable(b) {
    const { ncol, aligns } = b;
    // 列幅: 各列の最大表示幅(全角=2,半角=1)に比例させる。セル余白ぶんの重み(PAD_UNITS)を加え、
    // 列ごとの最小幅(内容が短い列はその幅、最大でも TABLE_MIN_COL_CAP)を確保する。
    const maxUnits = new Array(ncol).fill(2);
    const scan = (cells) => cells.forEach((lines, c) => {
      for (const segs of lines) maxUnits[c] = Math.max(maxUnits[c], displayWidth(segsPlain(segs)));
    });
    scan(b.header);
    b.rows.forEach(scan);
    const weights = maxUnits.map((u) => Math.min(u, TABLE_WEIGHT_CAP) + PAD_UNITS);
    const mins = maxUnits.map((u) => Math.min(Math.max(Math.round(u * UNIT_DXA + CELL_PAD_DXA), TABLE_MIN_COL), TABLE_MIN_COL_CAP));
    const widths = allocateColumns(weights, CONTENT_W, mins);

    const mkCell = (lines, c, kind, rowIdx) => {
      const header = kind === 'header';
      const base = header
        ? { size: TABLE_SIZE, bold: true, color: 'FFFFFF', linkColor: 'FFFFFF' }
        : { size: TABLE_SIZE };
      const alignment = aligns[c] || (header ? 'center' : null);
      const al = alignment === 'center' ? AlignmentType.CENTER : alignment === 'right' ? AlignmentType.RIGHT : AlignmentType.LEFT;
      const paras = lines.map((segs) => new Paragraph({ style: 'TableText', alignment: al, children: makeRuns(segs, base) }));
      let shading;
      if (header) shading = { type: ShadingType.CLEAR, color: 'auto', fill: NAVY };
      else if (rowIdx % 2 === 0) shading = { type: ShadingType.CLEAR, color: 'auto', fill: ZEBRA };
      return new TableCell({
        width: { size: widths[c], type: WidthType.DXA },
        verticalAlign: VerticalAlign.CENTER,
        shading,
        children: paras.length ? paras : [new Paragraph({ style: 'TableText', children: [] })],
      });
    };

    const rows = [
      new TableRow({
        tableHeader: true,
        cantSplit: true,
        children: b.header.map((lines, c) => mkCell(lines, c, 'header', 0)),
      }),
      ...b.rows.map((cells, r) => new TableRow({
        cantSplit: true,
        children: cells.map((lines, c) => mkCell(lines, c, 'body', r + 1)),   // r+1 が偶数 = 偶数行
      })),
    ];

    const line = { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF' };
    return new Table({
      width: { size: CONTENT_W, type: WidthType.DXA },
      columnWidths: widths,
      layout: TableLayoutType.FIXED,
      margins: { marginUnitType: WidthType.DXA, top: 50, bottom: 50, left: 90, right: 90 },
      borders: { top: line, bottom: line, left: line, right: line, insideHorizontal: line, insideVertical: line },
      rows,
    });
  }

  /** blocks → docx の子要素配列 */
  function renderBlocks(blocks, { startedWithBreak }) {
    const children = [];
    let seenH1 = false;
    let justBroke = !!startedWithBreak;      // 直前が改ページ(章の二重改ページ防止)
    let prev = null;
    // 末尾の pagebreak は不要(空白ページ防止)
    const list = blocks.slice();
    while (list.length && list[list.length - 1].type === 'pagebreak') list.pop();

    for (const b of list) {
      const gap = prev && ['table', 'image', 'code'].includes(prev.type) ? 120 : 0;
      switch (b.type) {
        case 'pagebreak':
          if (!justBroke) children.push(pageBreakParagraph());
          justBroke = true;
          prev = b;
          continue;
        case 'heading': {
          const pbb = b.level === 1 && seenH1 && !justBroke;
          if (b.level === 1) seenH1 = true;
          children.push(renderHeading(b, { pageBreakBefore: pbb }));
          break;
        }
        case 'para': children.push(renderPara(b, gap)); break;
        case 'list': children.push(...renderList(b, gap)); break;
        case 'quote': children.push(...renderQuote(b, gap)); break;
        case 'hr': children.push(renderHr(gap)); break;
        case 'code': children.push(...renderCode(b, gap)); break;
        case 'image': children.push(...renderImage(b, gap)); break;
        case 'table': children.push(renderTable(b)); break;
        default: break;
      }
      justBroke = false;
      prev = b;
    }
    if (prev && prev.type === 'table') {
      children.push(new Paragraph({ spacing: { before: 0, after: 0 }, run: { size: 4 }, children: [] }));
    }
    return children;
  }

  return { renderBlocks, numberingConfigs };
}

function decodeSafe(s) {
  try { return decodeURI(s); } catch (e) { return s; }
}

function pageBreakParagraph() {
  // 改ページ後の段落記号が占める高さを実質ゼロにする
  return new Paragraph({
    spacing: { before: 0, after: 0, line: 20, lineRule: LineRuleType.EXACT },
    children: [new PageBreak()],
  });
}

// ---------------------------------------------------------------------------
// スタイル
// ---------------------------------------------------------------------------
function buildStyles() {
  // 見出し1-4は docx-js 組み込みの Heading1..4 を styles.default.headingN で置き換える。
  // (paragraphStyles に同じ id を足すと styles.xml に同一 styleId が二重定義されるため、この方法で上書きする)
  const heading = (size, color, extra, outline) => ({
    run: { font: FONT, size, bold: true, color },
    paragraph: Object.assign({ keepNext: true, keepLines: true, outlineLevel: outline }, extra),
  });
  return {
    default: {
      document: {
        run: { font: FONT, size: BODY_SIZE, language: { value: 'en-US', eastAsia: 'ja-JP' } },
        paragraph: { spacing: { after: 120, line: 276, lineRule: LineRuleType.AUTO } },
      },
      heading1: heading(32, NAVY, {
        spacing: { before: 360, after: 200 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: NAVY, space: 4 } },
      }, 0),
      heading2: heading(26, BLUE, { spacing: { before: 300, after: 140 } }, 1),
      heading3: heading(22, '262626', { spacing: { before: 220, after: 100 } }, 2),
      heading4: heading(21, '262626', { spacing: { before: 180, after: 80 } }, 3),
    },
    paragraphStyles: [
      {
        id: 'CoverTitle', name: 'Cover Title', basedOn: 'Normal', next: 'Normal',
        run: { font: FONT, size: 56, bold: true, color: NAVY },
        paragraph: {
          spacing: { before: 3400, after: 280, line: 276, lineRule: LineRuleType.AUTO },
          border: { bottom: { style: BorderStyle.SINGLE, size: 24, color: NAVY, space: 14 } },
        },
      },
      {
        id: 'CoverSubtitle', name: 'Cover Subtitle', basedOn: 'Normal', next: 'Normal',
        run: { font: FONT, size: 30, color: BLUE },
        paragraph: { spacing: { before: 240, after: 240, line: 276, lineRule: LineRuleType.AUTO } },
      },
      {
        id: 'CoverDate', name: 'Cover Date', basedOn: 'Normal', next: 'Normal',
        run: { font: FONT, size: 24, color: GRAY_TEXT },
        paragraph: { spacing: { before: 360, after: 0 } },
      },
      {
        id: 'CoverNote', name: 'Cover Note', basedOn: 'Normal', next: 'Normal',
        run: { font: FONT, size: 18, color: GRAY_TEXT },
        paragraph: {
          spacing: { before: 5200, after: 0 },
          border: { top: { style: BorderStyle.SINGLE, size: 6, color: 'A6A6A6', space: 8 } },
        },
      },
      {
        id: 'TocTitle', name: 'TOC Title', basedOn: 'Normal', next: 'Normal',
        run: { font: FONT, size: 32, bold: true, color: NAVY },
        paragraph: {
          keepNext: true,
          spacing: { before: 0, after: 240 },
          border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: NAVY, space: 4 } },
        },
      },
      {
        id: 'TOC1', name: 'toc 1', basedOn: 'Normal', next: 'Normal', uiPriority: 39,
        run: { font: FONT, size: 21, bold: true },
        paragraph: { spacing: { before: 140, after: 40 } },
      },
      {
        id: 'TOC2', name: 'toc 2', basedOn: 'Normal', next: 'Normal', uiPriority: 39,
        run: { font: FONT, size: 20 },
        paragraph: { spacing: { before: 0, after: 20 }, indent: { left: 280 } },
      },
      {
        id: 'Caption', name: 'caption', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { font: FONT, size: 17, color: GRAY_TEXT },
        paragraph: { alignment: AlignmentType.CENTER, spacing: { before: 0, after: 200, line: 240, lineRule: LineRuleType.AUTO } },
      },
      {
        id: 'QuoteBlock', name: 'Quote Block', basedOn: 'Normal', next: 'Normal',
        run: { font: FONT, size: BODY_SIZE, color: '262626' },
        paragraph: {
          indent: { left: 240, right: 120 },
          shading: { type: ShadingType.CLEAR, color: 'auto', fill: QUOTE_BG },
          border: {
            left: { style: BorderStyle.SINGLE, size: 24, color: BLUE, space: 8 },
            top: { style: BorderStyle.SINGLE, size: 2, color: QUOTE_BG, space: 5 },
            bottom: { style: BorderStyle.SINGLE, size: 2, color: QUOTE_BG, space: 5 },
          },
        },
      },
      {
        id: 'TableText', name: 'Table Text', basedOn: 'Normal', next: 'Normal',
        run: { font: FONT, size: TABLE_SIZE },
        paragraph: { spacing: { before: 0, after: 0, line: 252, lineRule: LineRuleType.AUTO } },
      },
      {
        id: 'CodeBlock', name: 'Code Block', basedOn: 'Normal', next: 'Normal',
        run: { font: MONO, size: 17 },
        paragraph: {
          shading: { type: ShadingType.CLEAR, color: 'auto', fill: ZEBRA },
          indent: { left: 120, right: 120 },
        },
      },
    ],
  };
}

// ---------------------------------------------------------------------------
// 文書の組み立て
// ---------------------------------------------------------------------------
function shortTitle(title) {
  const LIMIT = 80;                           // 表示幅(全角=2)。8.5pt なら本文幅の約 8 割
  if (displayWidth(title) <= LIMIT) return title;
  const head = title.split(/[―—–:：|｜]/)[0].trim();
  const t = head && displayWidth(head) <= LIMIT ? head : title;
  if (displayWidth(t) <= LIMIT) return t;
  let out = '';
  let w = 0;
  for (const ch of t) {
    const cw = charWidth(ch.codePointAt(0));
    if (w + cw > LIMIT - 2) break;
    out += ch;
    w += cw;
  }
  const sp = out.lastIndexOf(' ');            // できれば単語(空白)の区切りで切る
  if (sp > out.length / 2) out = out.slice(0, sp);
  return out.trimEnd() + '…';
}

function buildDocument(md, baseDir, opts) {
  const lines = md.replace(/^﻿/, '').replace(/\r\n?/g, '\n').split('\n');

  // 表紙ブロック
  let k = 0;
  while (k < lines.length && isBlank(lines[k])) k++;
  const cov = [];
  while (k < lines.length && cov.length < 3 && /^%/.test(lines[k])) {
    cov.push(lines[k].replace(/^%[ \t]?/, '').trim());
    k++;
  }
  const cover = cov.length ? { title: cov[0], subtitle: cov[1] || '', date: cov[2] || '' } : null;

  const blocks = parseBlocks(cover ? lines.slice(k) : lines);
  const renderer = createRenderer(baseDir);
  const withToc = !!cover && !opts.noToc;

  const bodyChildren = [];
  if (withToc) {
    bodyChildren.push(new Paragraph({ style: 'TocTitle', children: [new TextRun({ text: '目次' })] }));
    // TOC フィールドは Word で開いて更新するまで中身が空なので、更新前に表示されるヒントを入れておく
    // (更新すると見出し1〜2の一覧に置き換わる)
    const tocHint = new Paragraph({
      children: [new TextRun({
        text: '(目次は Word で開いた際にフィールドを更新すると表示されます。表示されない場合は目次を右クリックし「フィールドの更新」を選択してください。)',
        size: 18,
        color: '7F7F7F',
        italics: true,
      })],
    });
    bodyChildren.push(new TableOfContents('目次', {
      hyperlink: true,
      headingStyleRange: '1-2',
      contentChildren: [tocHint],
    }));
    bodyChildren.push(pageBreakParagraph());
  }
  bodyChildren.push(...renderer.renderBlocks(blocks, { startedWithBreak: withToc }));
  if (!bodyChildren.length) bodyChildren.push(new Paragraph({ children: [] }));

  const docTitle = cover ? cover.title : path.basename(opts.input, path.extname(opts.input));
  const headerText = opts.header || (cover ? shortTitle(cover.title) : '');

  const pageProps = {
    page: { size: { width: PAGE_W, height: PAGE_H }, margin: MARGIN },
  };

  const sections = [];
  if (cover) {
    const cc = [new Paragraph({ style: 'CoverTitle', children: [new TextRun({ text: cover.title })] })];
    if (cover.subtitle) cc.push(new Paragraph({ style: 'CoverSubtitle', children: makeRuns(parseInline(cover.subtitle)) }));
    if (cover.date) cc.push(new Paragraph({ style: 'CoverDate', children: [new TextRun({ text: cover.date })] }));
    cc.push(new Paragraph({ style: 'CoverNote', children: [new TextRun({ text: DISCLAIMER })] }));
    sections.push({ properties: pageProps, children: cc });
  }

  // ヘッダ右に短縮タイトル(表紙も --header も無ければヘッダ自体を作らない)
  const header = headerText
    ? new Header({
      children: [new Paragraph({
        alignment: AlignmentType.RIGHT,
        spacing: { after: 0 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF', space: 3 } },
        children: [new TextRun({ text: headerText, size: 17, color: '7F7F7F' })],
      })],
    })
    : null;
  const footer = new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 0 },
      children: [new TextRun({ children: [PageNumber.CURRENT], size: 18, color: GRAY_TEXT })],
    })],
  });
  sections.push({
    properties: Object.assign({ type: SectionType.NEXT_PAGE }, pageProps),
    headers: header ? { default: header } : undefined,
    footers: { default: footer },
    children: bodyChildren,
  });

  return new Document({
    creator: 'md2docx',
    lastModifiedBy: 'md2docx',
    title: docTitle,
    description: cover && cover.subtitle ? cover.subtitle : undefined,
    compatibility: { version: 15 },
    features: withToc ? { updateFields: true } : undefined,
    styles: buildStyles(),
    numbering: { config: renderer.numberingConfigs },
    sections,
  });
}

// ---------------------------------------------------------------------------
// CLI
// ---------------------------------------------------------------------------
async function main() {
  const argv = process.argv.slice(2);
  const pos = [];
  const opts = { noToc: false, header: null, strict: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--no-toc') opts.noToc = true;
    else if (a === '--strict') opts.strict = true;
    else if (a === '--header') opts.header = argv[++i] || '';
    else if (a === '-h' || a === '--help') pos.length = 0, pos.push('-h');
    else pos.push(a);
  }
  if (pos.length < 2 || pos[0] === '-h') {
    console.error('使い方: node md2docx.js input.md output.docx [--no-toc] [--header "文言"] [--strict]');
    process.exit(pos[0] === '-h' ? 0 : 1);
  }
  const input = path.resolve(pos[0]);
  const output = path.resolve(pos[1]);
  opts.input = input;
  const md = fs.readFileSync(input, 'utf8');
  const doc = buildDocument(md, path.dirname(input), opts);
  const buf = await Packer.toBuffer(doc);
  fs.writeFileSync(output, buf);
  console.log(`OK: ${output} (${buf.length} bytes)` + (warnings.length ? `, 警告 ${warnings.length} 件` : ''));
  if (opts.strict && warnings.length) process.exit(1);
}

main().catch((e) => {
  console.error(e && e.stack ? e.stack : e);
  process.exit(1);
});
