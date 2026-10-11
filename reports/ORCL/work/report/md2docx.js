// Markdown(限定記法)→ docx 変換。報告書専用。
// 対応: # タイトル / ## 章 / ### 節 / #### 小節 / 段落 / **太字** / - 箇条書き / 1. 番号 /
//       パイプ表 / ![caption](path){width=NN} / > 囲み / <!-- pagebreak --> / <!-- toc -->
// 使い方: node md2docx.js input.md output.docx
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, AlignmentType, ImageRun, PageBreak,
  TableOfContents, Header, Footer, PageNumber, LevelFormat, TableLayoutType,
  VerticalAlign,
} = require('docx');

const [, , inPath, outPath] = process.argv;
const baseDir = path.dirname(path.resolve(inPath));
const src = fs.readFileSync(inPath, 'utf8').replace(/\r/g, '');
const lines = src.split('\n');

const FONT = { ascii: 'Arial', hAnsi: 'Arial', eastAsia: 'Yu Gothic', cs: 'Arial' };
const C = {
  navy: '1F3A5F', blue: '2E5C8A', light: 'E8EEF5', grid: 'A6B4C4', muted: '5A6B7D',
  callout: 'F3F6FA', calloutBar: '2E5C8A', accent: 'B23A3A',
};
const PAGE_W = 11906, PAGE_H = 16838, MARGIN = 1000; // A4, 約1.76cm
const CONTENT_W = PAGE_W - MARGIN * 2;

function runs(text, base = {}) {
  // **bold** と `code` を解釈
  const out = [];
  const re = /(\*\*[^*]+\*\*)/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), font: FONT, ...base }));
    out.push(new TextRun({ text: m[0].slice(2, -2), bold: true, font: FONT, ...base }));
    last = m.index + m[0].length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), font: FONT, ...base }));
  if (out.length === 0) out.push(new TextRun({ text: '', font: FONT, ...base }));
  return out;
}

function displayLen(s) {
  let n = 0;
  for (const ch of s.replace(/\*\*/g, '')) n += /[\u3000-\u9fff\uff00-\uffef]/.test(ch) ? 2 : 1;
  return n;
}

function parseRow(line) {
  let t = line.trim();
  if (t.startsWith('|')) t = t.slice(1);
  if (t.endsWith('|')) t = t.slice(0, -1);
  return t.split('|').map((c) => c.trim().replace(/<br>/g, '\n'));
}

function buildTable(rows) {
  const header = rows[0];
  const body = rows.slice(1);
  const nCol = header.length;
  // 列幅: 各列の表示長の(上限付き)最大値で比例配分
  const w = new Array(nCol).fill(4);
  for (const r of rows) r.forEach((c, i) => {
    if (i < nCol) {
      const l = Math.max(...c.split('\n').map(displayLen));
      w[i] = Math.max(w[i], Math.min(l, 46));
    }
  });
  const sum = w.reduce((a, b) => a + b, 0);
  let widths = w.map((x) => Math.max(600, Math.round((x / sum) * CONTENT_W)));
  const s2 = widths.reduce((a, b) => a + b, 0);
  widths = widths.map((x) => Math.round((x * CONTENT_W) / s2));
  widths[widths.length - 1] += CONTENT_W - widths.reduce((a, b) => a + b, 0);
  const fontSize = nCol >= 9 ? 13 : nCol >= 7 ? 14 : 16; // half-points
  const border = { style: BorderStyle.SINGLE, size: 4, color: C.grid };
  const borders = { top: border, bottom: border, left: border, right: border };
  const mk = (cells, isHeader) => new TableRow({
    tableHeader: isHeader,
    cantSplit: true,
    children: Array.from({ length: nCol }, (_, i) => {
      const txt = cells[i] !== undefined ? cells[i] : '';
      return new TableCell({
        width: { size: widths[i], type: WidthType.DXA },
        borders,
        verticalAlign: VerticalAlign.CENTER,
        shading: isHeader ? { fill: C.navy, type: ShadingType.CLEAR, color: 'auto' } : undefined,
        margins: { top: 40, bottom: 40, left: 70, right: 70 },
        children: txt.split('\n').map((part) => new Paragraph({
          spacing: { before: 0, after: 0, line: 252 },
          children: runs(part, { size: fontSize, color: isHeader ? 'FFFFFF' : '222222', bold: isHeader || undefined }),
        })),
      });
    }),
  });
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: widths,
    layout: TableLayoutType.FIXED,
    rows: [mk(header, true), ...body.map((r) => mk(r, false))],
  });
}

const children = [];
let i = 0;
let para = [];
const flushPara = () => {
  if (para.length) {
    children.push(new Paragraph({
      spacing: { after: 120, line: 300 },
      children: runs(para.join(' '), { size: 20 }),
    }));
    para = [];
  }
};

while (i < lines.length) {
  const line = lines[i];
  const t = line.trim();
  if (t === '') { flushPara(); i++; continue; }
  if (t === '<!-- pagebreak -->') { flushPara(); children.push(new Paragraph({ children: [new PageBreak()] })); i++; continue; }
  if (t === '<!-- toc -->') {
    flushPara();
    children.push(new TableOfContents('目次', { hyperlink: true, headingStyleRange: '1-2' }));
    i++; continue;
  }
  if (t.startsWith('<!--')) { i++; continue; }
  let m;
  if ((m = t.match(/^(#{1,4})\s+(.*)$/))) {
    flushPara();
    const level = m[1].length;
    const text = m[2];
    if (level === 1) {
      children.push(new Paragraph({
        alignment: AlignmentType.LEFT, spacing: { before: 0, after: 200 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: C.navy, space: 6 } },
        children: runs(text, { size: 36, bold: true, color: C.navy }),
      }));
    } else {
      const map = { 2: HeadingLevel.HEADING_1, 3: HeadingLevel.HEADING_2, 4: HeadingLevel.HEADING_3 };
      children.push(new Paragraph({ heading: map[level], children: runs(text) }));
    }
    i++; continue;
  }
  if (t.startsWith('|')) {
    flushPara();
    const rows = [];
    while (i < lines.length && lines[i].trim().startsWith('|')) {
      const r = lines[i].trim();
      if (!/^\|[\s:\-|]+\|$/.test(r)) rows.push(parseRow(r));
      i++;
    }
    children.push(buildTable(rows));
    children.push(new Paragraph({ spacing: { after: 80 }, children: [] }));
    continue;
  }
  if ((m = t.match(/^!\[(.*)\]\((.*?)\)(\{width=(\d+)\})?$/))) {
    flushPara();
    const p = path.resolve(baseDir, m[2]);
    const pct = m[4] ? parseInt(m[4], 10) : 100;
    const data = fs.readFileSync(p);
    // PNG サイズ取得
    const wpx = data.readUInt32BE(16), hpx = data.readUInt32BE(20);
    const maxW = Math.round((CONTENT_W / 1440) * 96 * (pct / 100));
    const outW = maxW, outH = Math.round((hpx / wpx) * outW);
    children.push(new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 80, after: 40 }, keepNext: true,
      children: [new ImageRun({ type: 'png', data, transformation: { width: outW, height: outH } })],
    }));
    if (m[1]) children.push(new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { after: 160 },
      children: runs(m[1], { size: 17, color: C.muted, italics: true }),
    }));
    i++; continue;
  }
  if (t.startsWith('> ')) {
    flushPara();
    const buf = [];
    while (i < lines.length && lines[i].trim().startsWith('>')) { buf.push(lines[i].trim().replace(/^>\s?/, '')); i++; }
    const paras = buf.join('\n').split(/\n\s*\n|\n(?=[-・])/);
    for (const [k, p] of buf.entries()) {
      if (p === '') continue;
      children.push(new Paragraph({
        shading: { fill: C.callout, type: ShadingType.CLEAR, color: 'auto' },
        border: { left: { style: BorderStyle.SINGLE, size: 24, color: C.calloutBar, space: 8 } },
        indent: { left: 160, right: 120 },
        spacing: { before: k === 0 ? 80 : 0, after: k === buf.length - 1 ? 160 : 0, line: 300 },
        children: runs(p, { size: 20 }),
      }));
    }
    void paras;
    continue;
  }
  if ((m = line.match(/^(\s*)- (.*)$/))) {
    flushPara();
    const lvl = Math.min(2, Math.floor(m[1].length / 2));
    children.push(new Paragraph({ numbering: { reference: 'bul', level: lvl }, spacing: { after: 40, line: 290 }, children: runs(m[2], { size: 20 }) }));
    i++; continue;
  }
  if ((m = line.match(/^(\s*)\d+\. (.*)$/))) {
    flushPara();
    const lvl = Math.min(1, Math.floor(m[1].length / 2));
    children.push(new Paragraph({ numbering: { reference: 'num', level: lvl }, spacing: { after: 40, line: 290 }, children: runs(m[2], { size: 20 }) }));
    i++; continue;
  }
  para.push(t);
  i++;
}
flushPara();

const doc = new Document({
  creator: 'Claude Code',
  title: 'Oracle(ORCL)投資判断報告書',
  features: { updateFields: true },
  styles: {
    default: { document: { run: { font: FONT, size: 20 } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 28, bold: true, color: C.navy, font: FONT },
        paragraph: { spacing: { before: 360, after: 160 }, outlineLevel: 0, keepNext: true,
          border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: C.blue, space: 4 } } } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 23, bold: true, color: C.blue, font: FONT },
        paragraph: { spacing: { before: 240, after: 100 }, outlineLevel: 1, keepNext: true } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 21, bold: true, color: '333333', font: FONT },
        paragraph: { spacing: { before: 180, after: 80 }, outlineLevel: 2, keepNext: true } },
    ],
  },
  numbering: {
    config: [
      { reference: 'bul', levels: [0, 1, 2].map((l) => ({ level: l, format: LevelFormat.BULLET, text: ['●', '○', '・'][l], alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360 + l * 360, hanging: 260 } }, run: { size: 14, color: C.blue } } })) },
      { reference: 'num', levels: [0, 1].map((l) => ({ level: l, format: l === 0 ? LevelFormat.DECIMAL : LevelFormat.LOWER_LETTER, text: l === 0 ? '%1.' : '%2)', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 400 + l * 360, hanging: 300 } } } })) },
    ],
  },
  sections: [{
    properties: { page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } } },
    headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: runs('Oracle(ORCL)投資判断報告書 | 2026-10-11 | 投資助言ではない', { size: 15, color: C.muted }) })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], size: 16, color: C.muted, font: FONT }), new TextRun({ text: ' / ', size: 16, color: C.muted, font: FONT }), new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 16, color: C.muted, font: FONT })] })] }) },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(outPath, buf); console.log('wrote', outPath, children.length, 'blocks'); });
