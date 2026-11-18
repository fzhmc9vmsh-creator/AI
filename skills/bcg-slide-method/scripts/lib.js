// 共通部品(references/design-spec.md 準拠)。全スライドはこの部品だけで組む。
// 座標は inch。16:9 = 13.333 × 7.5。余白 0.5。フォントは Meiryo UI(数字も同じ。Arial は表の数値列で使用可)。
const pptxgen = require('./node_modules/pptxgenjs');

const C = {
  primary: '197A56', dark: '0E4D33', light: '86C99B', teal: '1BA1A6', red: 'C0392B', amber: 'D68910',
  text: '333333', sub: '767676', rule: 'D9D9D9', white: 'FFFFFF', orange: 'E67E22', darkred: '7B241C',
  tint: 'EAF4EE', gray: 'F2F2F2',
};
const GRADE = {
  S: { fill: C.dark, font: C.white }, A: { fill: C.primary, font: C.white }, B: { fill: C.light, font: C.dark },
  C: { fill: C.amber, font: C.white }, D: { fill: C.orange, font: C.white }, E: { fill: C.red, font: C.white },
  F: { fill: C.darkred, font: C.white }, 'N/A': { fill: C.sub, font: C.white },
};
const FONT = 'Meiryo UI';
const W = 13.333, H = 7.5, M = 0.5;
// 上から: 現在地の帯 0〜0.34 / テーマ + なぜ 0.39〜0.65 / タイトル 0.71〜1.35(19pt 2 行まで)/ リード 1.40〜1.60 / 本文 1.62〜6.75
const GRID = {
  title: { x: M, y: 0.71, w: W - 2 * M - 1.2, h: 0.64 },      // 右端 1.2in は評価バッジ用に空ける
  kicker: { x: M, y: 1.4, w: W - 2 * M, h: 0.2 },
  body: { x: M, y: 1.62, w: W - 2 * M, h: 5.13 },
  src: { x: M, y: 6.88, w: 10.8, h: 0.42 },
  pg: { x: W - M - 0.6, y: 7.0, w: 0.6, h: 0.25 },
};
const MT = require('./meta.js');
// 数字の台帳: スライドの数字は F('id') で引く(facts.js)。facts_deck.json が無い案件でも部品は動く(F を呼んだ時に止まる)
const F = require('./facts.js');
const CHAPTERS = MT.CH.map(c => c.name);

// 組立の文脈(build.js / one.js が setCtx で渡す): ページ番号・章・節・テーマ・なぜ・タイトル
let ctx = null;
function setCtx(id) { ctx = id ? MT.ctxFor(id) : null; return ctx; }

// 文字列の幅の見積もり(inch)。全角 1em、半角 0.55em(空白 0.3em)
function estW(str, pt) {
  let em = 0;
  for (const ch of String(str)) em += ch.charCodeAt(0) < 0x80 ? (ch === ' ' ? 0.3 : 0.55) : 1.0;
  return em * pt / 72;
}

// 図の部品が見つけた重なり(one.js が表示する)
const warnings = [];
// 画像で確かめるべき箇所(重なりではないが、描画で崩れやすい所)。one.js が「確認:」として表示する
const notices = [];

function newDeck() {
  const pres = new pptxgen();
  pres.layout = 'LAYOUT_WIDE';
  pres.author = MT.DOC_AUTHOR || '長期保有適格性審査';   // 文書情報は meta.js の DOC_TITLE・DOC_AUTHOR から(案件の名前を残さない)
  pres.title = MT.DOC_TITLE || '長期保有適格性審査';
  pres.theme = { headFontFace: FONT, bodyFontFace: FONT };
  return pres;
}

function text(slide, str, o) {
  slide.addText(str, Object.assign({ fontFace: FONT, fontSize: 11, color: C.text, margin: 0.04, valign: 'top', isTextBox: true, fit: 'none' }, o));
}

// 見出し帯: 上端の灰帯に「第N章 › 節(何枚目)」と章の進捗、その下にテーマの札と「なぜ見るか」
function header(s) {
  if (!ctx || !ctx.meta.theme) return;
  const m = ctx.meta;
  s.addShape('rect', { x: 0, y: 0, w: W, h: 0.34, fill: { color: C.gray }, line: { color: C.gray }, objectName: 'bg_hdr' });
  s.addText([
    { text: `第${ctx.ch.no}章 ${ctx.ch.name}`, options: { color: C.sub } },
    { text: '   ›   ', options: { color: C.sub } },
    { text: ctx.secLabel, options: { color: C.dark, bold: true } },
  ], { x: M, y: 0.06, w: W - 2 * M - MT.CH.length * 0.9 - 0.1, h: 0.22, fontFace: FONT, fontSize: 9, margin: 0, valign: 'middle', isTextBox: true, objectName: 'hdr_crumb' });
  const pw = 0.86, gap = 0.04, n = MT.CH.length;
  MT.CH.forEach((c, i) => {
    const x = W - M - (n - i) * pw - (n - 1 - i) * gap, on = c.no === ctx.ch.no;
    s.addShape('roundRect', { x, y: 0.07, w: pw, h: 0.2, fill: { color: on ? C.primary : C.white }, line: { color: on ? C.primary : C.rule, width: 0.75 }, rectRadius: 0.04, objectName: 'bg_hdr_pill' + i });
    s.addText(`${c.no} ${c.short}`, { x, y: 0.07, w: pw, h: 0.2, fontFace: FONT, fontSize: 8, bold: on, color: on ? C.white : C.sub, align: 'center', valign: 'middle', margin: 0, isTextBox: true, objectName: 'bg_hdr_pt' + i });
  });
  const tag = 'テーマ: ' + m.theme, tw = estW(tag, 10) + 0.3;
  s.addShape('roundRect', { x: M, y: 0.39, w: tw, h: 0.26, fill: { color: C.dark }, line: { color: C.dark }, rectRadius: 0.05, objectName: 'ovl_theme_bg' });
  s.addText(tag, { x: M, y: 0.39, w: tw, h: 0.26, fontFace: FONT, fontSize: 10, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0, isTextBox: true, objectName: 'hdr_theme' });
  if (m.why) s.addText([{ text: 'なぜ見るか   ', options: { bold: true, color: C.teal } }, { text: m.why, options: { color: C.text } }],
    { x: M + tw + 0.16, y: 0.39, w: W - 2 * M - tw - 0.16, h: 0.26, fontFace: FONT, fontSize: 10, valign: 'middle', margin: 0, isTextBox: true, objectName: 'hdr_why' });
}

// 内容スライド。ctx があれば META のタイトル・リードとページ番号を優先する
function contentSlide(pres, { title, kicker, source, page, grade, condNo }) {
  const m = (ctx && ctx.meta) || {};
  title = m.title || title;
  if (m.kicker !== undefined) kicker = m.kicker;
  if (ctx) page = ctx.page;
  const s = pres.addSlide();
  s.background = { color: C.white };
  header(s);
  text(s, title, Object.assign({}, GRID.title, { objectName: 'title', fontSize: 19, bold: true, color: C.primary, valign: 'middle', margin: 0 }));
  if (kicker) text(s, kicker, Object.assign({}, GRID.kicker, { w: grade ? 11.2 : GRID.kicker.w, objectName: 'kicker', fontSize: 9.5, color: C.sub, margin: 0, valign: 'middle' }));
  if (source) text(s, '出所: ' + source, Object.assign({}, GRID.src, { objectName: 'src', fontSize: 8, color: C.sub, margin: 0, valign: 'bottom' }));
  text(s, String(page), Object.assign({}, GRID.pg, { objectName: 'pg', fontSize: 8, color: C.sub, align: 'right', margin: 0 }));
  if (grade) badge(s, W - M - 0.95, 0.71, grade, 0.95, condNo ? `条件${condNo}` : '構造評価');
  return s;
}

function badge(s, x, y, grade, size = 0.5, label) {
  const g = GRADE[grade] || GRADE['N/A'];
  s.addShape('roundRect', { x, y, w: size, h: size * (label ? 0.78 : 1), fill: { color: g.fill }, line: { color: g.fill }, rectRadius: 0.08, objectName: 'ovl_badge' });
  s.addText(grade, { x, y, w: size, h: size * (label ? 0.55 : 1), fontFace: FONT, fontSize: Math.round(size * 30), bold: true, color: g.font, align: 'center', valign: 'middle', margin: 0, isTextBox: true, objectName: 'ovl_badge_t' });
  if (label) s.addText(label, { x, y: y + size * 0.5, w: size, h: size * 0.26, fontFace: FONT, fontSize: 8, color: g.font, align: 'center', valign: 'middle', margin: 0, isTextBox: true, objectName: 'ovl_badge_l' });
}

function takeaway(s, x, y, w, h, str, o = {}) {
  s.addShape('rect', { x, y, w, h, fill: { color: C.tint }, line: { color: C.tint }, objectName: 'ovl_takeaway_bg' });
  text(s, str, Object.assign({ x: x + 0.12, y: y + 0.08, w: w - 0.24, h: h - 0.16, fontSize: 11, color: C.dark, bold: true, valign: 'middle', objectName: 'takeaway' }, o));
}

function box(s, x, y, w, h, o = {}) {
  s.addShape(o.round ? 'roundRect' : 'rect', Object.assign({ x, y, w, h, fill: { color: o.fill || C.white }, line: { color: o.line || C.rule, width: o.lw || 0.75 }, objectName: o.name || 'ovl_box' },
    o.round ? { rectRadius: 0.06 } : {}));
}

function arrow(s, x1, y1, x2, y2, o = {}) {
  s.addShape('line', { x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.abs(x2 - x1) || 0.001, h: Math.abs(y2 - y1) || 0.001,
    flipH: x2 < x1, flipV: y2 < y1, line: { color: o.color || C.sub, width: o.width || 1.25, dashType: o.dash || 'solid', endArrowType: 'triangle' }, objectName: 'ovl_arrow' });
}

// 表: rows = [[セル, …], …](1 行目は見出し)。colW は inch の配列
function table(s, rows, { x, y, w, colW, fontSize = 10, rowH = 0.3, headFill = C.dark, align, name = 'tbl' }) {
  const data = rows.map((r, i) => r.map((cell, j) => {
    const c = typeof cell === 'object' && cell !== null && !Array.isArray(cell) ? cell : { text: String(cell) };
    const base = { fontFace: FONT, fontSize, color: i === 0 ? C.white : C.text, bold: i === 0, valign: 'middle', margin: [0.03, 0.06, 0.03, 0.06],
      fill: { color: i === 0 ? headFill : (i % 2 === 0 ? C.gray : C.white) }, align: (align && align[j]) || (j === 0 ? 'left' : 'center'),
      border: [{ type: 'none' }, { type: 'none' }, { pt: 0.75, color: C.rule }, { type: 'none' }] };
    return { text: c.text, options: Object.assign(base, c.options || {}) };
  }));
  s.addTable(data, { x, y, w, colW, rowH, objectName: name });
}

// 目次(表紙の次と各章の中扉)。current = 0..3(その章を強調)。右に「この章の構成」(節とページ)と、その章を読む理由
function agenda(pres, current, page) {
  if (ctx) page = ctx.page;
  const s = pres.addSlide();
  s.background = { color: C.dark };
  s.addShape('rect', { x: 0, y: 0, w: W, h: H, fill: { color: C.dark }, line: { color: C.dark }, objectName: 'bg_agenda' });
  text(s, '目次', { x: 0.8, y: 0.55, w: 3.0, h: 0.7, fontSize: 26, bold: true, color: C.white, objectName: 'bg_agenda_lbl' });
  MT.CH.forEach((c, i) => {
    const step = MT.CH.length > 4 ? 1.02 : 1.25;           // 5 章以上は間隔を詰める
    const y = 1.6 + i * step, on = i === current;
    s.addShape('ellipse', { x: 0.85, y, w: 0.5, h: 0.5, fill: { color: on ? C.primary : C.dark }, line: { color: C.white, width: 1 }, transparency: on ? 0 : 50, objectName: 'bg_agenda_n' + i });
    text(s, String(c.no), { x: 0.85, y, w: 0.5, h: 0.5, fontSize: 14, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0, transparency: on ? 0 : 50, objectName: 'bg_agenda_nt' + i });
    text(s, c.name, { x: 1.55, y: y - 0.02, w: 6.2, h: 0.54, fontSize: 18, bold: on, color: C.white, valign: 'middle', margin: 0, transparency: on ? 0 : 50, objectName: 'bg_agenda_ch' + i });
    if (on) text(s, c.why, { x: 1.55, y: y + 0.5, w: 6.2, h: MT.CH.length > 4 ? 0.48 : 0.62, fontSize: MT.CH.length > 4 ? 10 : 10.5, color: C.light, margin: 0, objectName: 'bg_agenda_why' + i });
  });
  if (current >= 0) {
    const c = MT.CH[current];
    s.addShape('line', { x: 8.25, y: 1.6, w: 0, h: 4.8, line: { color: C.light, width: 0.75 }, objectName: 'bg_agenda_rule' });
    text(s, `第${c.no}章の構成`, { x: 8.55, y: 1.55, w: 4.2, h: 0.4, fontSize: 13, bold: true, color: C.light, margin: 0, objectName: 'bg_agenda_sh' });
    MT.secPages(c.no).forEach((r, j) => {
      const y = 2.1 + j * 0.5;
      text(s, `${r.no}  ${r.name}`, { x: 8.55, y, w: 3.35, h: 0.4, fontSize: 12.5, color: C.white, valign: 'middle', margin: 0, objectName: 'bg_agenda_s' + j });
      text(s, r.from === r.to ? `p.${r.from}` : `p.${r.from}–${r.to}`, { x: 11.9, y, w: 0.93, h: 0.4, fontSize: 10.5, color: C.light, align: 'right', valign: 'middle', margin: 0, objectName: 'bg_agenda_p' + j });
    });
    if (c.note) text(s, c.note, { x: 8.55, y: 2.1 + c.secs.length * 0.5 + 0.15, w: 4.28, h: 0.6, fontSize: 9.5, color: C.light, margin: 0, objectName: 'bg_agenda_note' });
  }
  text(s, String(page), { x: W - M - 0.6, y: 7.0, w: 0.6, h: 0.25, fontSize: 8, color: C.light, align: 'right', margin: 0, objectName: 'pg' });
  return s;
}

function cover(pres, { title, sub, date }) {
  const s = pres.addSlide();
  s.background = { color: C.white };
  s.addShape('rect', { x: 0, y: 0, w: 8.6, h: H, fill: { color: C.dark }, line: { color: C.dark }, objectName: 'bg_cover' });
  text(s, title, { x: 0.8, y: 2.0, w: 7.2, h: 1.9, fontSize: 30, bold: true, color: C.white, valign: 'bottom', objectName: 'bg_cover_title' });
  text(s, sub, { x: 0.8, y: 4.1, w: 7.2, h: 1.2, fontSize: 14, color: C.white, objectName: 'bg_cover_sub' });
  text(s, date, { x: 0.8, y: 6.5, w: 5, h: 0.4, fontSize: 11, color: C.light, objectName: 'bg_cover_date' });
  return s;
}

function closing(pres, { title, note, page }) {
  if (ctx) page = ctx.page;
  const s = pres.addSlide();
  s.background = { color: C.dark };
  s.addShape('rect', { x: 0, y: 0, w: W, h: H, fill: { color: C.dark }, line: { color: C.dark }, objectName: 'bg_divider' });
  if (ctx && ctx.meta.theme) text(s, `${ctx.secLabel}   ›   テーマ: ${ctx.meta.theme}(${ctx.meta.why})`, { x: 0.9, y: 0.5, w: 11.5, h: 0.3, fontSize: 9.5, color: C.light, margin: 0, objectName: 'bg_close_crumb' });
  text(s, title, { x: 0.9, y: 2.6, w: 11.5, h: 0.9, fontSize: 26, bold: true, color: C.white, objectName: 'bg_close_t' });
  text(s, note, { x: 0.9, y: 3.7, w: 11.5, h: 2.2, fontSize: 11, color: C.white, objectName: 'bg_close_n' });
  text(s, String(page), { x: W - M - 0.6, y: 7.0, w: 0.6, h: 0.25, fontSize: 8, color: C.light, align: 'right', margin: 0, objectName: 'pg' });
  return s;
}

// 棒・線グラフの共通の見た目(全チャートで同じ)
function chartStyle(o = {}) {
  return Object.assign({
    catAxisLabelFontFace: FONT, valAxisLabelFontFace: FONT, dataLabelFontFace: FONT, legendFontFace: FONT, titleFontFace: FONT,
    catAxisLabelFontSize: 9, valAxisLabelFontSize: 9, dataLabelFontSize: 9, legendFontSize: 9,
    catAxisLabelColor: C.text, valAxisLabelColor: C.sub, dataLabelColor: C.text,
    valGridLine: { color: 'E6E6E6', size: 0.5 }, catGridLine: { style: 'none' },
    catAxisLineShow: true, valAxisLineShow: false, showLegend: false, showValue: true, dataLabelPosition: 'outEnd',
    chartColors: [C.primary, C.light, C.teal, C.amber, C.sub, C.dark],   // 規定の色(pptxgenjs の既定色は使わない)
  }, o);
}

// ======================= ブループリント(レイアウトの型。座標は固定、中身だけ差し替える) =======================
// 共通: 本文領域 y 1.62〜6.75。右パネル x 9.05 w 3.78。左右2分割は x 0.5 w 6.05 / x 6.78 w 6.05。

// 区画の見出し(濃緑の太字 12pt + 細い罫線なし)
function paneHead(s, x, y, w, str, name = 'pane_head') {
  text(s, str, { x, y, w, h: 0.32, fontSize: 12, bold: true, color: C.dark, margin: 0, valign: 'middle', objectName: name });
}

// 箇条書き(各項目 = 文字列。強調したい語は [{text, options:{bold:true,color}}] の配列でも可)
function bullets(s, items, { x, y, w, h, fontSize = 10.5, color = C.text, name = 'bullets', gap = 4 }) {
  const runs = [];
  items.forEach((it, i) => {
    const last = i === items.length - 1;
    if (Array.isArray(it)) {
      it.forEach((r, j) => runs.push({ text: r.text, options: Object.assign({ bullet: j === 0 ? { indent: 12 } : undefined, breakLine: j === it.length - 1 && !last, paraSpaceAfter: gap }, r.options || {}) }));
    } else {
      // 項目の中の "\n" は同じ項目の中で改行する(記号を付け直さない)
      // (pptxgenjs は bullet を持つ塊で段落を分けるので、続きの塊には bullet を付けない)
      String(it).split('\n').forEach((pt, j, arr) => runs.push({ text: pt, options: Object.assign(j === 0 ? { bullet: { indent: 12 }, paraSpaceAfter: gap } : { softBreakBefore: true },
        j === arr.length - 1 ? { breakLine: !last } : {}) }));
    }
  });
  s.addText(runs, { x, y, w, h, fontFace: FONT, fontSize, color, valign: 'top', margin: 0.04, isTextBox: true, objectName: name });
}

// 大型数値タイル(T9)。tiles = [{value, label, note, color}](最大4)
function kpiTiles(s, tiles, { x = M, y = 1.7, w = W - 2 * M, h = 1.55, gap: optGap, compact: optCompact } = {}) {
  // compact: true で小さい札(図の下に 3 枚並べるとき)。指定しなければ今までの大きさ(既存の資料の見た目を変えない)
  const compact = optCompact === true;
  const n = tiles.length, gap = optGap ?? (compact ? 0.16 : 0.25), tw = (w - gap * (n - 1)) / n;
  tiles.forEach((t, i) => {
    const tx = x + i * (tw + gap);
    box(s, tx, y, tw, h, { fill: C.tint, line: C.tint, name: 'ovl_tile' + i });
    if (!compact) {
      text(s, t.value, { x: tx + 0.1, y: y + 0.08, w: tw - 0.2, h: 0.78, fontSize: 32, bold: true, color: t.color || C.primary, align: 'center', valign: 'middle', margin: 0, objectName: 'tile_v' + i });
      text(s, t.label, { x: tx + 0.1, y: y + 0.88, w: tw - 0.2, h: 0.3, fontSize: 10.5, bold: true, color: C.dark, align: 'center', margin: 0, objectName: 'tile_l' + i });
      if (t.note) text(s, t.note, { x: tx + 0.1, y: y + 1.17, w: tw - 0.2, h: 0.33, fontSize: 8.5, color: C.sub, align: 'center', margin: 0, objectName: 'tile_n' + i });
    } else {
      const innerW = (tw - 0.10) * 0.92;
      const vfs = [26, 22, 20, 18, 16, 15, 14].find(f => estW(t.value, f) * 1.15 <= innerW) || 14;
      const vh = t.note ? h * 0.44 : h * 0.48;
      text(s, t.value, { x: tx + 0.05, y: y + 0.05, w: tw - 0.10, h: vh, fontSize: vfs, bold: true, color: t.color || C.primary, align: 'center', valign: 'middle', margin: 0, objectName: 'tile_v' + i });
      const ly = y + 0.05 + vh + 0.02;
      const lh = t.note ? 0.28 : (h - (ly - y) - 0.05);
      text(s, t.label, { x: tx + 0.05, y: ly, w: tw - 0.10, h: lh, fontSize: 8.8, bold: true, color: C.dark, align: 'center', valign: t.note ? 'middle' : 'top', margin: 0, objectName: 'tile_l' + i });
      if (t.note) text(s, t.note, { x: tx + 0.05, y: ly + lh + 0.01, w: tw - 0.10, h: Math.max(0.24, y + h - (ly + lh + 0.03)), fontSize: 8, color: C.sub, align: 'center', valign: 'top', margin: 0, objectName: 'tile_n' + i });
    }
  });
}

// チャート+右パネル(T7)。chart は addChart の引数 {type, data, opts}
function chartPanel(pres, s, chart, { takeawayText, points, note }) {
  s.addChart(chart.type, chart.data, chartStyle(Object.assign({ x: M, y: 1.65, w: 8.35, h: 5.0, objectName: 'chart' }, chart.opts || {})));
  takeaway(s, 9.05, 1.7, 3.78, 1.35, takeawayText);
  if (points) bullets(s, points, { x: 9.05, y: 3.2, w: 3.78, h: note ? 2.6 : 3.45, fontSize: 10.5, name: 'points' });
  if (note) text(s, note, { x: 9.05, y: 5.9, w: 3.78, h: 0.8, fontSize: 8.5, color: C.sub, objectName: 'note' });
}

// 構造図(T15)。nodes: [{id, col 0..3, row 0..2, label, sub, kind: self|ext|ok|risk}]
// edges: [{from, to, label, kind: money|goods|risk}]。tags: [{node, text, tone: red|green}]
const T15 = { x0: 0.6, y0: 1.9, dx: 2.08, dy: 1.42, nw: 1.75, nh: 0.92 };
function nodePos(n) { return { x: T15.x0 + n.col * T15.dx, y: T15.y0 + n.row * T15.dy, w: T15.nw, h: T15.nh }; }
function structure(s, { nodes, edges = [], tags = [], legend = true }) {
  const pos = {};
  nodes.forEach(n => { pos[n.id] = nodePos(n); });
  const labels = [];
  edges.forEach((e, i) => {
    const a = pos[e.from], b = pos[e.to];
    const ax = a.x + a.w / 2, ay = a.y + a.h / 2, bx = b.x + b.w / 2, by = b.y + b.h / 2;
    let x1, y1, x2, y2;
    if (Math.abs(bx - ax) >= Math.abs(by - ay)) { x1 = ax + Math.sign(bx - ax) * a.w / 2; y1 = ay + (e.off || 0); x2 = bx - Math.sign(bx - ax) * b.w / 2; y2 = by + (e.off || 0); }
    else { x1 = ax + (e.off || 0); y1 = ay + Math.sign(by - ay) * a.h / 2; x2 = bx + (e.off || 0); y2 = by - Math.sign(by - ay) * b.h / 2; }
    const col = e.kind === 'risk' ? C.red : (e.kind === 'goods' ? C.teal : C.dark);
    arrow(s, x1, y1, x2, y2, { color: col, width: e.kind === 'money' ? 1.75 : 1.25, dash: e.kind === 'risk' ? 'dash' : 'solid' });
    if (e.label) labels.push({ e, i, x1, y1, x2, y2, col });
  });
  // ラベルは全部の矢印を描いた後に、白地の箱で載せる(線が文字を横切らないように)。幅は文字数から見積もる
  labels.forEach(({ e, i, x1, y1, x2, y2, col }) => {
    const est = [...e.label].reduce((acc, ch) => acc + (ch.charCodeAt(0) < 0x80 ? 0.066 : 0.122), 0) + 0.12;
    const lw = Math.min(1.75, Math.max(0.5, est));
    const lines = est > 1.75 ? 2 : 1;
    const lh = 0.2 * lines + 0.06;
    const mx = (x1 + x2) / 2 + (e.dx || 0), my = (y1 + y2) / 2 + (e.dy || 0);
    const horiz = Math.abs(y2 - y1) < 0.05, vert = Math.abs(x2 - x1) < 0.05;
    let bx = mx - lw / 2, by = my - lh / 2;                // 斜めの線: 中点に白地で載せる
    if (horiz) by = e.below ? my + 0.04 : my - lh - 0.04;  // 水平線: 線の上(below なら下)に置き、線を隠さない
    else if (vert) bx = mx + 0.06;                         // 垂直線: 線の右に置く
    s.addText(e.label, { x: bx, y: by, w: lw, h: lh, fontFace: FONT, fontSize: 8.5, color: col, align: 'center', valign: 'middle',
      margin: 0.02, fill: { color: C.white }, isTextBox: true, objectName: 'ovl_elabel' + i });
  });
  nodes.forEach(n => {
    const p = pos[n.id];
    const self = n.kind === 'self';
    const fill = self ? C.primary : (n.kind === 'risk' ? 'FDEDEC' : (n.kind === 'ok' ? C.tint : C.white));
    const line = self ? C.primary : (n.kind === 'risk' ? C.red : (n.kind === 'ok' ? C.light : C.sub));
    s.addShape('roundRect', { x: p.x, y: p.y, w: p.w, h: p.h, fill: { color: fill === 'FDEDEC' ? C.gray : fill }, line: { color: line, width: 1 }, rectRadius: 0.08, objectName: 'ovl_node_' + n.id });
    text(s, n.label, { x: p.x + 0.05, y: p.y + 0.06, w: p.w - 0.1, h: n.sub ? 0.36 : p.h - 0.12, fontSize: 10.5, bold: true, color: self ? C.white : C.dark, align: 'center', valign: n.sub ? 'top' : 'middle', margin: 0, objectName: 'ovl_node_t_' + n.id });
    if (n.sub) text(s, n.sub, { x: p.x + 0.05, y: p.y + 0.42, w: p.w - 0.1, h: p.h - 0.46, fontSize: 8.5, color: self ? C.white : C.text, align: 'center', margin: 0, objectName: 'ovl_node_s_' + n.id });
  });
  tags.forEach((t, i) => {
    const p = pos[t.node];
    const col = t.tone === 'red' ? C.red : C.primary;
    s.addShape('roundRect', { x: p.x, y: p.y + p.h + 0.04, w: p.w, h: 0.26, fill: { color: col }, line: { color: col }, rectRadius: 0.05, objectName: 'ovl_tag' + i });
    text(s, t.text, { x: p.x, y: p.y + p.h + 0.04, w: p.w, h: 0.26, fontSize: 8, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0, objectName: 'ovl_tag_t' + i });
  });
  if (legend) {
    const ly = 6.12;
    [['カネ', C.dark, 'solid'], ['モノ・サービス', C.teal, 'solid'], ['リスク', C.red, 'dash']].forEach(([lab, col, dash], i) => {
      arrow(s, 0.6 + i * 2.0, ly + 0.14, 1.05 + i * 2.0, ly + 0.14, { color: col, dash });
      text(s, lab, { x: 1.12 + i * 2.0, y: ly, w: 1.3, h: 0.28, fontSize: 8.5, color: C.sub, margin: 0, objectName: 'ovl_legend' + i });
    });
  }
}

// 構造図スライドの右パネル(根拠 + 評価理由)と下帯(C 以下の監視 KPI)
function t15Side(s, { evidence, reason, kpi }) {
  box(s, 9.05, 1.62, 3.78, 3.05, { fill: C.white, line: C.rule, name: 'ovl_evbox' });
  paneHead(s, 9.17, 1.68, 3.5, '根拠', 'ev_head');
  bullets(s, evidence, { x: 9.17, y: 2.02, w: 3.56, h: 2.6, fontSize: 9.5, name: 'evidence' });
  takeaway(s, 9.05, 4.8, 3.78, 1.25, reason, { fontSize: 10.5 });
  if (kpi) {
    box(s, M, 6.42, W - 2 * M, 0.42, { fill: C.gray, line: C.amber, name: 'ovl_kpibox' });
    text(s, '監視 KPI とトリガー: ' + kpi, { x: M + 0.1, y: 6.44, w: W - 2 * M - 0.2, h: 0.38, fontSize: 9, color: C.text, valign: 'middle', margin: 0, objectName: 'kpi' });
  }
}

// 左右2分割(複合構成)。left/right は (s, x, y, w, h) を受け取る関数
function twoPane(s, leftHead, rightHead, left, right) {
  paneHead(s, M, 1.62, 6.05, leftHead, 'pane_l');
  paneHead(s, 6.78, 1.62, 6.05, rightHead, 'pane_r');
  left(s, M, 2.0, 6.05, 4.75);
  right(s, 6.78, 2.0, 6.05, 4.75);
}

// 流れ図(T16・T18): cols = [{head, boxes:[{text, tone: on|off|key, h}]}]。列の間は太矢印
function flow(s, cols, { x = M, y = 1.7, w = W - 2 * M, h = 4.4, gap = 0.45 } = {}) {
  const n = cols.length, cw = (w - gap * (n - 1)) / n;
  cols.forEach((c, i) => {
    const cx = x + i * (cw + gap);
    text(s, c.head, { x: cx, y, w: cw, h: 0.32, fontSize: 11, bold: true, color: C.dark, align: 'center', margin: 0, objectName: 'flow_h' + i });
    let by = y + 0.42;
    const totalH = c.boxes.reduce((a, b) => a + (b.h || 0.9), 0) + 0.12 * (c.boxes.length - 1);
    if (totalH < h - 0.42) by += (h - 0.42 - totalH) / 2;
    c.boxes.forEach((b, j) => {
      const bh = b.h || 0.9;
      const fill = b.tone === 'on' ? C.primary : (b.tone === 'key' ? C.dark : (b.tone === 'off' ? C.gray : C.tint));
      const fc = (b.tone === 'on' || b.tone === 'key') ? C.white : (b.tone === 'off' ? C.sub : C.dark);
      box(s, cx, by, cw, bh, { fill, line: fill, round: true, name: 'ovl_fbox' + i + '_' + j });
      text(s, b.text, { x: cx + 0.08, y: by + 0.04, w: cw - 0.16, h: bh - 0.08, fontSize: b.size || 10, bold: !!b.bold, color: fc, align: 'center', valign: 'middle', margin: 0, objectName: 'flow_t' + i + '_' + j });
      by += bh + 0.12;
    });
    if (i < n - 1) s.addShape('rightArrow', { x: cx + cw + Math.min(0.08, gap * 0.15), y: y + 0.42 + (h - 0.42) / 2 - 0.2, w: Math.max(0.12, gap - 2 * Math.min(0.08, gap * 0.15)), h: 0.4, fill: { color: C.light }, line: { color: C.light }, objectName: 'ovl_farrow' + i });
  });
}

// 2軸マトリクス(T13): cells は行×列の文字列(推奨セルは tone 'rec')、points = [{x,y,label}] は 0..1 の位置
function matrix(s, { x, y, w, h, xLabels, yLabels, xTitle, yTitle, cells, highlight = [] }) {
  const nx = xLabels.length, ny = yLabels.length, lw = 1.1, lh = 0.4;
  const cw = (w - lw) / nx, ch = (h - lh) / ny;
  text(s, yTitle, { x, y, w: lw, h: lh, fontSize: 9, color: C.sub, margin: 0, valign: 'bottom', objectName: 'mx_yt' });
  xLabels.forEach((l, i) => text(s, l, { x: x + lw + i * cw, y, w: cw, h: lh, fontSize: 9.5, bold: true, color: C.dark, align: 'center', valign: 'bottom', margin: 0, objectName: 'mx_x' + i }));
  yLabels.forEach((l, j) => {
    text(s, l, { x, y: y + lh + j * ch, w: lw - 0.05, h: ch, fontSize: 9.5, bold: true, color: C.dark, valign: 'middle', margin: 0, objectName: 'mx_y' + j });
    xLabels.forEach((_, i) => {
      const hl = highlight.some(([hi, hj]) => hi === i && hj === j);
      const cell = cells[j][i];
      box(s, x + lw + i * cw, y + lh + j * ch, cw - 0.04, ch - 0.04, { fill: hl ? C.primary : (cell.tone === 'rec' ? C.tint : C.white), line: C.rule, name: 'ovl_mx' + i + '_' + j });
      text(s, cell.text, { x: x + lw + i * cw + 0.05, y: y + lh + j * ch + 0.03, w: cw - 0.14, h: ch - 0.1, fontSize: 9.5, bold: hl, color: hl ? C.white : C.text, align: 'center', valign: 'middle', margin: 0, objectName: 'mx_t' + i + '_' + j });
    });
  });
  if (xTitle) text(s, xTitle, { x: x + lw, y: y + h + 0.02, w: w - lw, h: 0.26, fontSize: 9, color: C.sub, align: 'center', margin: 0, objectName: 'mx_xt' });
}

// ======================= 関係図(レーン型。条件スライド・事業の関係・会社の筋書きに使う) =======================
// 列(c)× 行(r)の格子に箱を置く。列の間の空き(通路)を矢印とラベルが通る。
// spec = {
//   x, y, w, h        図の領域(既定 0.5, 1.66, 8.55, 4.66。右の 3.58in は mechPanel 用)
//   cols: [幅, …]      箱の列の幅(inch)。通路の幅 = (w − Σ幅) ÷ (列数 − 1)。ラベルを置く通路は 1.0in 以上(手本 s08b は約 1.0in)
//   rows: n            行数。r = 0..n-1(0.5 刻み可)
//   nodeH              箱の高さ(既定: 行の高さ − 0.22、最大 0.82)
//   lanes: [{label, c0, c1, self}]     背景の帯(誰の領域か)。self = 自社(薄緑)、他は薄灰
//   groups: [{label, c0, c1, r0, r1}]  事業単位などの点線の囲み(ラベルは上辺の上に載る)
//   nodes: [{id, c, r, cs, rs, label, sub, kind, h, w, dx, dy, tag: {text, tone: red|green|amber}}]
//          kind: self(自社本体・緑塗り)/ unit(自社の事業・白地に緑枠)/ ext(外部)/ ok(有利・薄緑)/ risk(不利・赤枠)/ key(要点・濃緑塗り)/ note(枠なしの注記)
//   edges: [{from, to, label, kind, n, fs, ts, fo, tof, mx, my, lpos, lw, ldx, ldy, below, left, both}]
//          kind: money(カネ・濃緑の太線)/ goods(モノ・サービス・ティール)/ risk(リスク・赤の破線)/ ctrl(契約・統治・情報・灰の破線)
//          n: 仕組みの番号 → ラベルの頭に ①② が付き、mechPanel の同じ番号の説明と対応する
//          fs/ts: 出る辺・入る辺 'l'|'r'|'t'|'b'(既定は位置から自動)。fo/tof: 辺の上の位置のずらし(inch、既定は自動で振り分け)
//          mx/my: 折れ線の曲がる位置。lpos: ラベルを置く線分 'a'(最初)|'b'(最後)|'v'(縦)。ldx/ldy: ラベルの微調整
//   legend: true(下端に凡例)
// }
// 重なり(ラベル×箱、ラベル×ラベル、線×無関係の箱)は L.warnings に入り、one.js が表示する。0 件にしてから納品する。
const CIRC = ['', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩'];
function edgeStyle(k) {
  if (k === 'risk') return { color: C.red, width: 1.25, dash: 'dash' };
  if (k === 'goods') return { color: C.teal, width: 1.5, dash: 'solid' };
  if (k === 'ctrl') return { color: C.sub, width: 1.0, dash: 'sysDash' };
  return { color: C.dark, width: 1.75, dash: 'solid' };
}
function seg(s, x1, y1, x2, y2, st, head, both, name) {
  if (Math.abs(x2 - x1) < 0.003 && Math.abs(y2 - y1) < 0.003) return;
  s.addShape('line', { x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.abs(x2 - x1) || 0.001, h: Math.abs(y2 - y1) || 0.001, flipH: x2 < x1, flipV: y2 < y1,
    line: Object.assign({ color: st.color, width: st.width, dashType: st.dash }, head ? { endArrowType: 'triangle' } : {}, both ? { beginArrowType: 'triangle' } : {}), objectName: name });
}
function overlap(p, q, tol = 0.015) {
  return Math.min(p.x + p.w, q.x + q.w) - Math.max(p.x, q.x) > tol && Math.min(p.y + p.h, q.y + q.h) - Math.max(p.y, q.y) > tol;
}
function segHits(ax, ay, bx, by, r, pad = 0.02) {   // 水平・垂直の線分が箱の内側を通るか
  const x0 = r.x + pad, x1 = r.x + r.w - pad, y0 = r.y + pad, y1 = r.y + r.h - pad;
  if (Math.abs(ay - by) < 0.005) return ay > y0 && ay < y1 && Math.max(ax, bx) > x0 && Math.min(ax, bx) < x1;
  if (Math.abs(ax - bx) < 0.005) return ax > x0 && ax < x1 && Math.max(ay, by) > y0 && Math.min(ay, by) < y1;
  return false;
}
function flowMap(s, spec) {
  const X = spec.x ?? M, Y = spec.y ?? 1.66, WD = spec.w ?? 8.55, HD = spec.h ?? 4.66;
  const cols = spec.cols, nc = cols.length;
  const gap = nc > 1 ? (WD - cols.reduce((a, b) => a + b, 0)) / (nc - 1) : 0;
  const cx = []; { let a = X; cols.forEach(w => { cx.push(a); a += w + gap; }); }
  const spanW = (c, cs = 1) => cx[c + cs - 1] + cols[c + cs - 1] - cx[c];
  const laneH = spec.lanes ? 0.3 : 0, legH = spec.legend === false ? 0 : 0.3;
  const top = Y + laneH + 0.1, bot = Y + HD - legH;
  const pitch = (bot - top) / spec.rows;
  const nodeH = spec.nodeH || Math.min(0.82, pitch - 0.22);
  const tag = (name) => (spec.name || 'fm') + '_' + name;
  const warn = (msg) => warnings.push(`[${spec.name || 'flowMap'}] ${msg}`);

  // 1. レーン(背景の帯)と見出し
  (spec.lanes || []).forEach((ln, i) => {
    const pad = Math.min(0.12, gap / 4), lx = cx[ln.c0] - pad, lw = spanW(ln.c0, ln.c1 - ln.c0 + 1) + 2 * pad;
    s.addShape('rect', { x: lx, y: Y, w: lw, h: bot - Y + 0.02, fill: { color: ln.self ? C.tint : C.gray }, line: { color: ln.self ? C.tint : C.gray }, objectName: 'bg_lane' + i });
    s.addShape('rect', { x: lx, y: Y, w: lw, h: laneH, fill: { color: ln.self ? C.primary : C.rule }, line: { color: ln.self ? C.primary : C.rule }, objectName: 'bg_laneh' + i });
    text(s, ln.label, { x: lx, y: Y, w: lw, h: laneH, fontSize: 9.5, bold: true, color: ln.self ? C.white : C.dark, align: 'center', valign: 'middle', margin: 0, objectName: 'bg_lanet' + i });
  });

  // 2. 箱の位置
  const rect = {};
  spec.nodes.forEach(n => {
    const cs = n.cs || 1, rs = n.rs || 1;
    const h = n.h || (rs > 1 ? rs * pitch - 0.22 : nodeH);
    const w = n.w || spanW(n.c, cs);
    const x = cx[n.c] + (n.dx || 0) + (n.w ? (spanW(n.c, cs) - n.w) / 2 : 0);
    const y = top + n.r * pitch + (rs * pitch - h) / 2 + (n.dy || 0);
    rect[n.id] = { x, y, w, h, n };
  });

  // 3. 囲み(点線)。ラベルは上辺に載せる
  const glabels = [];
  (spec.groups || []).forEach((g, i) => {
    const gx = cx[g.c0] - 0.07, gw = spanW(g.c0, g.c1 - g.c0 + 1) + 0.14;
    const gy = top + g.r0 * pitch + 0.03, gh = (g.r1 - g.r0 + 1) * pitch - 0.06;
    s.addShape('roundRect', { x: gx, y: gy, w: gw, h: gh, fill: { color: C.white, transparency: 100 }, line: { color: C.primary, width: 1, dashType: 'dash' }, rectRadius: 0.06, objectName: 'ovl_grp' + i });
    const lw = estW(g.label, 8) + 0.16;
    glabels.push({ x: gx + 0.1, y: gy - 0.09, w: lw, h: 0.18, txt: g.label, i });
  });

  // 4. 矢印: 辺の決定 → 辺の上の位置の振り分け → 経路
  const E = (spec.edges || []).map((e, i) => {
    const a = rect[e.from], b = rect[e.to];
    if (!a || !b) throw new Error(`flowMap: 箱がない ${e.from} → ${e.to}`);
    let fs, ts;
    if (b.x >= a.x + a.w - 0.02) [fs, ts] = ['r', 'l'];
    else if (b.x + b.w <= a.x + 0.02) [fs, ts] = ['l', 'r'];
    else [fs, ts] = b.y > a.y ? ['b', 't'] : ['t', 'b'];
    return Object.assign({}, e, { i, a, b, fs: e.fs || fs, ts: e.ts || ts });
  });
  // 4a. 向かい合う辺が重なる箱どうしは、同じ高さ(横の線)・同じ位置(縦の線)で結んで直線にする。同じ 2 箱の往復は ±0.09 ずらす
  E.forEach(e => {
    if (e.mx !== undefined || e.my !== undefined) return;
    const hz = 'lr'.includes(e.fs) && 'lr'.includes(e.ts), vt = 'tb'.includes(e.fs) && 'tb'.includes(e.ts);
    if (!hz && !vt) return;
    const [p0, p1] = hz ? ['y', 'h'] : ['x', 'w'];
    const lo = Math.max(e.a[p0], e.b[p0]) + 0.08, hi = Math.min(e.a[p0] + e.a[p1], e.b[p0] + e.b[p1]) - 0.08;
    if (hi < lo) return;
    const sm = e.a[p1] <= e.b[p1] ? e.a : e.b;
    let v = Math.max(lo, Math.min(hi, sm[p0] + sm[p1] / 2));
    const twin = E.find(o => o !== e && o._fix !== undefined && ((o.from === e.from && o.to === e.to) || (o.from === e.to && o.to === e.from)));
    if (twin) { twin._fix = v - 0.09; v += 0.09; e.below = e.below ?? true; }
    e._fix = v;
  });
  E.forEach(e => {
    if (e._fix === undefined) return;
    const hz = 'lr'.includes(e.fs), c = (r) => hz ? r.y + r.h / 2 : r.x + r.w / 2;
    if (e.fo === undefined) e.fo = e._fix - c(e.a);
    if (e.tof === undefined) e.tof = e._fix - c(e.b);
  });
  // 4b. 残りの線は、辺の上で相手の位置の順に並べる(固定した線の間に均等に振り分ける)
  const ports = {};
  E.forEach(e => { (ports[e.from + ':' + e.fs] = ports[e.from + ':' + e.fs] || []).push({ e, end: 'f' }); (ports[e.to + ':' + e.ts] = ports[e.to + ':' + e.ts] || []).push({ e, end: 't' }); });
  Object.entries(ports).forEach(([k, list]) => {
    const [id, side] = k.split(':'), r = rect[id], vs = side === 'l' || side === 'r';
    const key = (p) => { const o = p.end === 'f' ? p.e.b : p.e.a; return vs ? o.y + o.h / 2 : o.x + o.w / 2; };
    const fixedOf = (p) => (p.end === 'f' ? p.e.fo : p.e.tof);
    list.sort((p, q) => { const fp = fixedOf(p), fq = fixedOf(q); return (fp ?? (key(p) - (vs ? r.y + r.h / 2 : r.x + r.w / 2))) - (fq ?? (key(q) - (vs ? r.y + r.h / 2 : r.x + r.w / 2))); });
    const L = vs ? r.h : r.w, half = L / 2 - 0.07, sp = vs ? 0.2 : 0.45;
    let j = 0;
    while (j < list.length) {
      if (fixedOf(list[j]) !== undefined) { const v = fixedOf(list[j]); if (list[j].end === 'f') list[j].e._fo = v; else list[j].e._to = v; j++; continue; }
      let k2 = j; while (k2 < list.length && fixedOf(list[k2]) === undefined) k2++;
      const openA = j === 0, openB = k2 === list.length, n = k2 - j;
      const a = openA ? -half : fixedOf(list[j - 1]) + 0.12, b = openB ? half : fixedOf(list[k2]) - 0.12;
      let offs;
      if (openA && openB) { const st = Math.min(sp, (L * 0.8) / Math.max(1, n)); offs = [...Array(n)].map((_, t) => (t - (n - 1) / 2) * st); }
      else {
        const st = n > 1 ? Math.min(sp, Math.max(0.06, (b - a) / (n - 1))) : 0;
        if (openA) offs = [...Array(n)].map((_, t) => b - (n - 1 - t) * st);          // 下側だけ固定: 固定の上に詰める
        else if (openB) offs = [...Array(n)].map((_, t) => a + t * st);               // 上側だけ固定: 固定の下に詰める
        else offs = [...Array(n)].map((_, t) => (a + b) / 2 + (t - (n - 1) / 2) * st);
      }
      offs.forEach((off, t) => { off = Math.max(-half, Math.min(half, off)); const p = list[j + t]; if (p.end === 'f') p.e._fo = off; else p.e._to = off; });
      j = k2;
    }
  });
  const pt = (r, side, off) => side === 'r' ? [r.x + r.w, r.y + r.h / 2 + off] : side === 'l' ? [r.x, r.y + r.h / 2 + off]
    : side === 'b' ? [r.x + r.w / 2 + off, r.y + r.h] : [r.x + r.w / 2 + off, r.y];
  E.forEach(e => {
    let [x1, y1] = pt(e.a, e.fs, e._fo), [x2, y2] = pt(e.b, e.ts, e._to);
    const hs = 'lr'.includes(e.fs), ht = 'lr'.includes(e.ts);
    if (hs && ht) {
      if (Math.abs(y1 - y2) < 0.06 && e.mx === undefined) { const ym = (y1 + y2) / 2; e.pts = [[x1, ym], [x2, ym]]; }
      else { const mx = e.mx ?? (x1 + x2) / 2; e.pts = [[x1, y1], [mx, y1], [mx, y2], [x2, y2]]; e._auto = e.mx === undefined; }
    } else if (!hs && !ht) {
      if (Math.abs(x1 - x2) < 0.06 && e.my === undefined) { const xm = (x1 + x2) / 2; e.pts = [[xm, y1], [xm, y2]]; }
      else { const my = e.my ?? (y1 + y2) / 2; e.pts = [[x1, y1], [x1, my], [x2, my], [x2, y2]]; }
    } else if (hs) e.pts = [[x1, y1], [x2, y1], [x2, y2]];
    else e.pts = [[x1, y1], [x1, y2], [x2, y2]];
  });
  // 同じ通路で縦の線が重なる自動の折れ線は、横にずらして並べる
  const lanesOfMx = {};
  E.filter(e => e._auto).forEach(e => { const k = Math.round(e.pts[1][0] / 0.1); (lanesOfMx[k] = lanesOfMx[k] || []).push(e); });
  Object.values(lanesOfMx).forEach(list => {
    if (list.length < 2) return;
    list.sort((p, q) => p.pts[0][1] - q.pts[0][1]);
    list.forEach((e, j) => { const d = (j - (list.length - 1) / 2) * 0.14; e.pts[1][0] += d; e.pts[2][0] += d; });
  });
  E.forEach(e => {
    const st = edgeStyle(e.kind); e.col = st.color;
    for (let k = 0; k < e.pts.length - 1; k++) seg(s, e.pts[k][0], e.pts[k][1], e.pts[k + 1][0], e.pts[k + 1][1], st, k === e.pts.length - 2, k === 0 && e.both, 'ovl_' + tag('e' + e.i + '_' + k));
  });

  // 5. 箱(線の端を隠すため線の後に描く)
  spec.nodes.forEach(n => {
    const r = rect[n.id], k = n.kind || 'ext';
    if (k === 'note') {
      text(s, n.label, { x: r.x, y: r.y, w: r.w, h: r.h, fontSize: n.size || 8.5, color: n.color || C.sub, align: n.align || 'left', valign: 'middle', margin: 0.02, objectName: 'ovl_' + tag('note_' + n.id) });
      return;
    }
    const fill = { self: C.primary, key: C.dark, ok: C.tint }[k] || C.white;
    const line = { self: C.primary, key: C.dark, unit: C.primary, ok: C.light, risk: C.red }[k] || C.sub;
    const lw = { unit: 1.5, risk: 1.5 }[k] || 0.75;
    const fc = (k === 'self' || k === 'key') ? C.white : C.dark;
    s.addShape('roundRect', { x: r.x, y: r.y, w: r.w, h: r.h, fill: { color: fill }, line: { color: line, width: lw }, rectRadius: 0.06, objectName: 'ovl_' + tag('n_' + n.id) });
    // 名前は 10pt → 9pt → 9pt 2 行(明示の "\n" も可)の順に収める
    const lab = String(n.label), fitW = (r.w - 0.12) * 0.92;   // 監査と同じ 8% の余裕
    const lsz = estW(lab, 10) <= fitW && !lab.includes('\n') ? 10 : 9;
    const lLines = lab.split('\n').reduce((a, ln) => a + Math.max(1, Math.ceil(estW(ln, lsz) / fitW - 0.02)), 0);
    const lh = 0.06 + lLines * 0.165;
    text(s, lab, { x: r.x + 0.04, y: r.y + 0.03, w: r.w - 0.08, h: n.sub ? lh : r.h - 0.06, fontSize: lsz, bold: true, color: k === 'risk' ? C.red : fc, align: 'center', valign: 'middle', margin: 0, objectName: 'ovl_' + tag('nt_' + n.id) });
    if (n.sub) text(s, n.sub, { x: r.x + 0.05, y: r.y + 0.03 + lh, w: r.w - 0.1, h: r.h - lh - 0.06, fontSize: n.subSize || 8.5, color: (k === 'self' || k === 'key') ? C.white : C.text, align: 'center', valign: 'top', margin: 0, objectName: 'ovl_' + tag('ns_' + n.id) });
  });
  const tags = [];
  spec.nodes.filter(n => n.tag).forEach(n => {
    const r = rect[n.id], col = { red: C.red, amber: C.amber }[n.tag.tone] || C.primary;
    const tw = Math.min(r.w, estW(n.tag.text, 8) + 0.2), tx = r.x + (r.w - tw) / 2, ty = n.tag.above ? r.y - 0.23 : r.y + r.h + 0.03;
    s.addShape('roundRect', { x: tx, y: ty, w: tw, h: 0.2, fill: { color: col }, line: { color: col }, rectRadius: 0.04, objectName: 'ovl_' + tag('tag_' + n.id) });
    text(s, n.tag.text, { x: tx, y: ty, w: tw, h: 0.2, fontSize: 8, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0, objectName: 'ovl_' + tag('tagt_' + n.id) });
    tags.push({ x: tx, y: ty, w: tw, h: 0.2, id: n.id });
  });

  // 6. ラベル(最後に白地で載せる)
  const labs = [];
  E.filter(e => e.label || e.n).forEach(e => {
    const segs = [];
    for (let k = 0; k < e.pts.length - 1; k++) {
      const [ax, ay] = e.pts[k], [bx, by] = e.pts[k + 1];
      segs.push({ ax, ay, bx, by, horiz: Math.abs(ay - by) < 0.005, len: Math.hypot(bx - ax, by - ay) });
    }
    let sg;
    if (e.lpos === 'v') sg = segs.find(q => !q.horiz) || segs[0];
    else if (e.lpos === 'a') sg = segs[0];
    else if (e.lpos === 'b') sg = segs[segs.length - 1];
    else { const hz = segs.filter(q => q.horiz); sg = hz.length ? hz.reduce((p, q) => (q.len > p.len ? q : p)) : segs[0]; }
    if (!e.label) {   // 番号だけの丸(ラベルを置く余地がない線)。説明は右の「仕組み」に書く
      const bx = (sg.ax + sg.bx) / 2 - 0.13 + (e.ldx || 0), by = (sg.ay + sg.by) / 2 - 0.13 + (e.ldy || 0);
      s.addShape('ellipse', { x: bx, y: by, w: 0.26, h: 0.26, fill: { color: e.col }, line: { color: C.white, width: 1 }, objectName: 'ovl_' + tag('num' + e.i) });
      text(s, String(e.n), { x: bx, y: by, w: 0.26, h: 0.26, fontSize: 9, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0, objectName: 'ovl_' + tag('numt' + e.i) });
      labs.push({ x: bx, y: by, w: 0.26, h: 0.26, e, name: CIRC[e.n] });
      return;
    }
    const head = e.n ? CIRC[e.n] + ' ' : '';
    const est = estW(head + e.label, 8.5) * 1.08 + 0.12;   // 描画のフォント幅に 8% の余裕
    const maxW = e.lw || (sg.horiz ? Math.max(0.9, Math.min(1.9, sg.len - 0.08)) : 1.45);
    const lines = Math.max(1, Math.ceil(est / maxW - 0.03));
    const lw = lines > 1 ? maxW : est, lh = 0.155 * lines + 0.07;
    const mx = (sg.ax + sg.bx) / 2, my = (sg.ay + sg.by) / 2;
    let lx, ly;
    if (sg.horiz) { lx = mx - lw / 2; ly = e.below ? my + 0.03 : my - lh - 0.03; }
    else { lx = e.left ? mx - lw - 0.05 : mx + 0.05; ly = my - lh / 2; }
    lx += e.ldx || 0; ly += e.ldy || 0;
    const runs = [];
    if (head) runs.push({ text: head, options: { bold: true } });
    runs.push({ text: e.label, options: { bold: !!e.bold } });
    s.addText(runs, { x: lx, y: ly, w: lw, h: lh, fontFace: FONT, fontSize: 8.5, color: e.col, align: 'center', valign: 'middle', margin: 0.02, fill: { color: C.white }, isTextBox: true, objectName: 'ovl_' + tag('lab' + e.i) });
    labs.push({ x: lx, y: ly, w: lw, h: lh, e, name: e.label });
  });
  glabels.forEach(g => {
    s.addText(g.txt, { x: g.x, y: g.y, w: g.w, h: g.h, fontFace: FONT, fontSize: 8, bold: true, color: C.primary, align: 'center', valign: 'middle', margin: 0, fill: { color: C.white }, isTextBox: true, objectName: 'ovl_' + tag('glab' + g.i) });
  });

  // 7. 凡例
  if (spec.legend !== false) {
    const ly = bot + 0.06;
    const used = new Set(E.map(e => e.kind || 'money'));
    [['カネ', 'money'], ['モノ・サービス', 'goods'], ['リスク', 'risk'], ['契約・統治', 'ctrl']].filter(([, k]) => used.has(k)).forEach(([lab, k], i) => {
      const st = edgeStyle(k), lx = X + i * 1.55;
      seg(s, lx, ly + 0.11, lx + 0.4, ly + 0.11, st, true, false, 'ovl_' + tag('leg' + i));
      text(s, lab, { x: lx + 0.46, y: ly, w: 1.05, h: 0.22, fontSize: 8, color: C.sub, margin: 0, valign: 'middle', objectName: 'ovl_' + tag('legt' + i) });
    });
    if (E.some(e => e.n)) text(s, '①② … は右の「仕組み」の番号', { x: X + 4 * 1.55, y: ly, w: WD - 4 * 1.55, h: 0.22, fontSize: 8, color: C.sub, margin: 0, valign: 'middle', align: 'right', objectName: 'ovl_' + tag('legn') });
  }

  // 8. 重なりの検査
  const nodes = Object.entries(rect).map(([id, r]) => Object.assign({ id }, r));
  const name = (r) => (r.n ? r.n.label : '').slice(0, 12);
  labs.forEach((l, i) => {
    const ln = String(l.name).slice(0, 14);
    nodes.forEach(r => { if (overlap(l, r)) warn(`ラベル「${ln}」が箱「${name(r)}」に重なる`); });
    tags.forEach(t => { if (overlap(l, t)) warn(`ラベル「${ln}」が札(${t.id})に重なる`); });
    glabels.forEach(g => { if (overlap(l, g)) warn(`ラベル「${ln}」が囲みの名前「${g.txt}」に重なる`); });
    labs.slice(i + 1).forEach(m => { if (overlap(l, m)) warn(`ラベル「${ln}」と「${String(m.name).slice(0, 14)}」が重なる`); });
    if (l.x < X - 0.15 || l.x + l.w > X + WD + 0.15 || l.y < Y || l.y + l.h > bot + 0.05) warn(`ラベル「${ln}」が図の領域の外`);
    E.forEach(e => { if (e === l.e) return; for (let k = 0; k < e.pts.length - 1; k++) if (segHits(e.pts[k][0], e.pts[k][1], e.pts[k + 1][0], e.pts[k + 1][1], l, 0.03)) { warn(`ラベル「${ln}」が別の線(${e.from}→${e.to})を隠す`); break; } });
  });
  tags.forEach(t => nodes.forEach(r => { if (r.id !== t.id && overlap(t, r)) warn(`札(${t.id})が箱「${name(r)}」に重なる`); }));
  glabels.forEach(g => nodes.forEach(r => { if (overlap(g, r)) warn(`囲みの名前「${g.txt}」が箱「${name(r)}」に重なる`); }));
  nodes.forEach((r, i) => nodes.slice(i + 1).forEach(q => { if (overlap(r, q)) warn(`箱「${name(r)}」と「${name(q)}」が重なる`); }));
  E.forEach(e => {
    for (let k = 0; k < e.pts.length - 1; k++) {
      nodes.forEach(r => { if (r.id !== e.from && r.id !== e.to && segHits(e.pts[k][0], e.pts[k][1], e.pts[k + 1][0], e.pts[k + 1][1], r)) warn(`線 ${e.from}→${e.to} が箱「${name(r)}」を横切る`); });
    }
  });
  return { rect, cx, top, pitch, gap, bot };
}

// 関係図スライドの右パネル: 仕組み(図の番号と対応)→ 評価の理由 → 上がる条件・下がる条件
// 文字量から高さを見積もり、収まる最大の文字の大きさ(10.5〜9pt)を選ぶ。理由の箱は中身に合わせ、上がる/下がる条件は下端に揃える
function mechPanel(s, { mech, reason, up, down, head = '仕組み(図の ①② … と対応)', x = 9.25, mechH = 0, bottom = 6.32, fontSize }) {
  const w = W - M - x;
  const lh = (pt) => pt / 72 * 1.2;
  const lines = (str, pt, bw) => String(str).split('\n').reduce((a, ln) => a + Math.max(1, Math.ceil(estW(ln, pt) * 1.08 / (bw - 0.08) - 0.02)), 0);
  const hasUD = up || down;
  const udH = hasUD ? (up ? lines('上がる条件  ' + up, 8.5, w) : 0) * lh(8.5) + (down ? lines('下がる条件  ' + down, 8.5, w) : 0) * lh(8.5) + 0.08 : 0;
  const reasonH = lines(reason, 10, w - 0.24) * lh(10) + 0.3;
  const mechEst = (pt) => mech.reduce((a, m, i) => a + lines(CIRC[i + 1] + ' ' + m, pt, w) * lh(pt) + 5 / 72, 0) + 0.08;
  const avail = bottom - 1.98 - 0.08 - (hasUD ? 0.08 : 0);
  let fs = fontSize;
  if (!fs) fs = [11, 10.5, 10, 9.5, 9].find(f => Math.max(mechH, mechEst(f)) + reasonH + udH <= avail) || 9;
  const mh = Math.max(mechH, mechEst(fs));
  // 行幅いっぱいの行は、描画で折り返して空行ができ、下の項目が理由の箱に隠れることがある(監査では見つからない)。ここで止める
  // 対象は「直後に改行 \n がある行」だけ(項目の最後の行は折り返しても空行にならない)
  mech.forEach((m, i) => String(CIRC[i + 1] + ' ' + m).split('\n').forEach((ln, j, arr) => {
    if (j === arr.length - 1) return;
    const r = estW(ln, fs) * 1.08 / (w - 0.08);
    const frac = r - Math.floor(r);
    if (r >= 0.9 && (frac >= 0.93 || frac <= 0.02)) notices.push(`mechPanel: ${CIRC[i + 1]} の行「${ln.slice(0, 16)}…」が行幅に近い。画像で、この項目の下に空行ができて次の項目が理由の箱に隠れていないかを見る(隠れていたら文を短くする)`);
  }));
  const extra = Math.max(0, avail - mh - reasonH - udH);
  const rBox = reasonH + Math.min(extra, 0.3);
  paneHead(s, x, 1.62, w, head, 'mech_head');
  const runs = [];
  mech.forEach((m, i) => {
    const last = i === mech.length - 1;
    runs.push({ text: CIRC[i + 1] + ' ', options: { bold: true, color: C.primary, paraSpaceAfter: 5 } });
    // 項目の中の "\n" は段落を分けずに改行する(項目の間隔と区別するため)
    const parts = String(m).split('\n');
    parts.forEach((pt, j) => runs.push({ text: pt, options: Object.assign({ color: C.text, paraSpaceAfter: 5 }, j > 0 ? { softBreakBefore: true } : {}, j === parts.length - 1 ? { breakLine: !last } : {}) }));
  });
  s.addText(runs, { x, y: 1.98, w, h: mh, fontFace: FONT, fontSize: fs, valign: 'top', margin: 0.03, isTextBox: true, objectName: 'mech' });
  const ry = bottom - (hasUD ? udH + 0.08 : 0) - rBox;
  takeaway(s, x, ry, w, rBox, reason, { fontSize: 10 });
  if (hasUD) {
    const r = [];
    if (up) r.push({ text: '上がる条件  ', options: { bold: true, color: C.primary } }, { text: up, options: { color: C.text, breakLine: !!down } });
    if (down) r.push({ text: '下がる条件  ', options: { bold: true, color: C.red } }, { text: down, options: { color: C.text } });
    s.addText(r, { x, y: bottom - udH, w, h: udH, fontFace: FONT, fontSize: 8.5, valign: 'top', margin: 0.03, isTextBox: true, objectName: 'updown' });
  }
}

// 下端の監視 KPI の帯(C 以下の条件で使う)
function kpiBand(s, kpi) {
  box(s, M, 6.42, W - 2 * M, 0.42, { fill: C.gray, line: C.amber, name: 'ovl_kpibox' });
  text(s, '監視 KPI とトリガー: ' + kpi, { x: M + 0.1, y: 6.44, w: W - 2 * M - 0.2, h: 0.38, fontSize: 9, color: C.text, valign: 'middle', margin: 0, objectName: 'kpi' });
}

// 時間軸の帯: 期間の長さを並べて比べる(契約・リース・償却・優位の期間など)。bars = [{label, from, to, color, text}]
function timeBand(s, { x, y, w, h, from, to, step = 5, bars, labelW = 1.55, name = 'tb', fmt = (t) => String(t) }) {
  const ax = x + labelW, aw = w - labelW, px = (t) => ax + (t - from) / (to - from) * aw;
  for (let t = from; t <= to; t += step) {
    text(s, fmt(t), { x: px(t) - 0.3, y, w: 0.6, h: 0.2, fontSize: 8, color: C.sub, align: 'center', margin: 0, objectName: `ovl_${name}_tk${t}` });
    s.addShape('line', { x: px(t), y: y + 0.2, w: 0.001, h: h - 0.2, line: { color: C.rule, width: 0.5, dashType: 'dash' }, objectName: `ovl_${name}_gl${t}` });
  }
  const rh = (h - 0.24) / bars.length;
  bars.forEach((b, i) => {
    const by = y + 0.24 + i * rh, bh = Math.min(0.26, rh * 0.72);
    text(s, b.label, { x, y: by, w: labelW - 0.08, h: rh, fontSize: 8.5, bold: true, color: C.dark, valign: 'middle', margin: 0, objectName: `ovl_${name}_l${i}` });
    const x0 = px(b.from), x1 = px(Math.min(b.to, to));
    s.addShape('rect', { x: x0, y: by + (rh - bh) / 2, w: Math.max(0.05, x1 - x0), h: bh, fill: { color: b.color || C.primary }, line: { color: b.color || C.primary }, objectName: `ovl_${name}_b${i}` });
    if (b.text) {
      const inside = estW(b.text, 8) + 0.1 < x1 - x0;
      text(s, b.text, { x: inside ? x0 : x1 + 0.05, y: by + (rh - bh) / 2, w: inside ? x1 - x0 : Math.max(0.6, x + w - x1 - 0.05), h: bh, fontSize: 8, bold: inside, color: inside ? (b.color === C.light ? C.dark : C.white) : C.text, align: inside ? 'center' : 'left', valign: 'middle', margin: 0, objectName: `ovl_${name}_t${i}` });
    }
  });
}

// 滝グラフ(ウォーターフォール): items = [{label, val, type: 'total'|'step', disp, highlight, ref}]
// opt = {x, y, w, h, name, unit, axisMin, labelFontSize, valueFontSize}
function waterfall(s, items, opt = {}) {
  const X = opt.x ?? M, Y = opt.y ?? 2.22, WD = opt.w ?? 7.60, HD = opt.h ?? 3.09;
  const pfx = opt.name || 'wf';
  const lblFs = opt.labelFontSize ?? 8.5, valFs = opt.valueFontSize ?? 9;
  const axisMin = (opt.axisMin !== undefined && Number(opt.axisMin) > 0) ? Number(opt.axisMin) : 0;
  const n = items.length;
  if (!n) return;

  let cur = 0;
  const bars = items.map(item => {
    const isTotal = item.type === 'total';
    const v = Number(item.val) || 0;
    const start = isTotal ? axisMin : cur;
    const end = isTotal ? v : cur + v;
    cur = end;
    const topVal = Math.max(start, end);
    const botVal = Math.min(start, end);
    const disp = item.disp !== undefined ? String(item.disp) : (
      isTotal
        ? (v < 0 ? '▲' + Math.round(Math.abs(v)).toLocaleString('en-US') : Math.round(v).toLocaleString('en-US'))
        : (v >= 0 ? '+' + Math.round(v).toLocaleString('en-US') : '▲' + Math.round(Math.abs(v)).toLocaleString('en-US'))
    );
    return { item, isTotal, v, start, end, topVal, botVal, disp };
  });

  const maxV = Math.max(axisMin, ...bars.map(b => b.topVal));
  const minV = Math.min(axisMin, ...bars.map(b => b.botVal));
  const spanV = (maxV - minV) || 1;
  const topPad = 0.28, botPad = minV < axisMin ? 0.75 : 0.51;
  const plotTop = Y + topPad, plotH = Math.max(0.5, HD - topPad - botPad);
  const scale = plotH / spanV;
  const yBase = plotTop + (maxV - axisMin) * scale;

  const xStart = X + 0.05, innerW = WD - 0.10;
  const bw = Math.min(1.1, Math.round((innerW / (n * 1.488)) * 100) / 100);
  const gap = n > 1 ? (innerW - n * bw) / (n - 1) : 0;

  if (opt.unit) {
    s.addText(String(opt.unit), {
      x: X, y: Y - 0.02, w: 1.5, h: 0.22,
      fontFace: FONT, fontSize: 8, color: C.sub, align: 'left', valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_${pfx}_unit`,
    });
  }
  if (axisMin > 0) {
    const axX = opt.unit ? (X + estW(String(opt.unit), 8) + 0.14) : X;
    s.addText(`縦軸は ${axisMin} から`, {
      x: axX, y: Y - 0.02, w: 2.2, h: 0.22,
      fontFace: FONT, fontSize: 8, color: C.sub, align: 'left', valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_${pfx}_axismin`,
    });
  }

  s.addShape('line', {
    x: X, y: yBase, w: WD, h: 0,
    line: { color: C.rule, width: 0.75 },
    objectName: `ovl_${pfx}_base`,
  });

  let prevConnectX = null, prevConnectY = null;
  bars.forEach((b, i) => {
    const x = xStart + i * (bw + gap);
    const boxH = Math.abs(b.topVal - b.botVal) * scale;
    const boxY = yBase - (b.topVal - axisMin) * scale;
    const isHl = !b.isTotal && !!b.item.highlight;
    const fillColor = b.isTotal ? C.dark : (isHl ? C.primary : (b.v >= 0 ? C.rule : C.sub));
    const lineOpt = isHl ? { color: C.dark, width: 1.5 } : (b.isTotal ? { color: C.dark, width: 0.5 } : { color: C.sub, width: 0.5 });
    const labelY = b.v < 0 ? (boxY + boxH + 0.04) : (boxY - 0.28);
    const connectY = yBase - (b.end - axisMin) * scale;
    b.x = x;
    b.boxY = boxY;
    b.boxH = boxH;

    if (i > 0 && prevConnectY !== null) {
      s.addShape('line', {
        x: prevConnectX, y: prevConnectY, w: x - prevConnectX, h: 0,
        line: { color: C.sub, width: 0.75, dashType: 'dash' },
        objectName: `ovl_${pfx}_dash_${i}`,
      });
    }

    s.addShape('rect', {
      x, y: boxY, w: bw, h: Math.max(boxH, 0.02),
      fill: { color: fillColor }, line: lineOpt,
      objectName: `ovl_${pfx}_bar_${i}`,
    });
    if (axisMin > 0 && b.isTotal && boxH > 0.28) {
      [yBase - 0.21, yBase - 0.12].forEach((by, bi) => {
        s.addShape('rect', {
          x: x - 0.03, y: by, w: bw + 0.06, h: 0.035, rotate: -8,
          fill: { color: C.white }, line: { color: C.white, width: 0 },
          objectName: `ovl_${pfx}_brk_${i}_${bi}`,
        });
      });
    }

    s.addText(b.disp, {
      x: x - 0.1, y: labelY, w: bw + 0.2, h: 0.25,
      fontFace: FONT, fontSize: valFs,
      bold: !!(b.item.highlight || b.isTotal),
      color: b.isTotal ? C.dark : (isHl ? C.primary : C.text),
      align: 'center', valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_${pfx}_v_${i}`,
    });

    prevConnectX = x + bw;
    prevConnectY = connectY;
  });

  const yAxisLbl = Math.max(
    yBase + 0.06,
    ...bars.map(b => (b.v < 0 ? b.boxY + b.boxH + 0.30 : (b.botVal < axisMin ? b.boxY + b.boxH + 0.06 : 0)))
  );

  bars.forEach((b, i) => {
    const lblW = bw + 0.18;
    const lblLines = String(b.item.label).split('\n').reduce((acc, ln) =>
      acc + Math.max(1, Math.ceil(estW(ln, lblFs) * 1.08 / lblW - 0.02)), 0);
    const lblH = b.item.ref ? Math.max(0.24, lblLines * (lblFs / 72 * 1.25) + 0.04) : 0.45;
    s.addText(String(b.item.label), {
      x: b.x - 0.09, y: yAxisLbl, w: lblW, h: lblH,
      fontFace: FONT, fontSize: lblFs, color: C.text, bold: !!b.item.highlight,
      align: 'center', valign: 'top', margin: 0, isTextBox: true,
      objectName: `ovl_${pfx}_lbl_${i}`,
    });
    if (b.item.ref) {
      const yRef = yAxisLbl + lblLines * (lblFs / 72 * 1.25) + 0.02;
      s.addText(String(b.item.ref), {
        x: b.x - 0.09, y: yRef, w: lblW, h: 0.20,
        fontFace: FONT, fontSize: 8, color: C.sub,
        align: 'center', valign: 'top', margin: 0, isTextBox: true,
        objectName: `ovl_${pfx}_ref_${i}`,
      });
    }
  });
}

// 図の上に ①②③ の丸い印を置く: list = [{x, y, n(1〜3), text, side('right'|'left'|'top'|'bottom')}]
function marks(s, list = []) {
  const d = 0.22;
  list.forEach((it, i) => {
    s.addShape('ellipse', {
      x: it.x, y: it.y, w: d, h: d,
      fill: { color: C.primary }, line: { color: C.primary },
      objectName: `ovl_mark_c_${i}`,
    });
    s.addText(String(it.n), {
      x: it.x, y: it.y, w: d, h: d,
      fontFace: FONT, fontSize: 9, bold: true, color: C.white,
      align: 'center', valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_mark_n_${i}`,
    });
    if (it.text) {
      const side = it.side || 'right';
      const lines = String(it.text).split('\n');
      const maxLnW = Math.max(...lines.map(ln => estW(ln, 8.5)));
      const tw = Math.max(0.55, Math.ceil((maxLnW / 0.88 + 0.10) * 100) / 100);
      const th = Math.max(0.22, lines.length * (8.5 / 72 * 1.25) + 0.04);
      let tx, ty, align;
      if (side === 'left') {
        tx = it.x - tw - 0.05; ty = it.y + (d - th) / 2; align = 'right';
      } else if (side === 'top') {
        tx = it.x + d / 2 - tw / 2; ty = it.y - th - 0.04; align = 'center';
      } else if (side === 'bottom') {
        tx = it.x + d / 2 - tw / 2; ty = it.y + d + 0.04; align = 'center';
      } else {
        tx = it.x + d + 0.05; ty = it.y + (d - th) / 2; align = 'left';
      }
      s.addText(String(it.text), {
        x: tx, y: ty, w: tw, h: th,
        fontFace: FONT, fontSize: 8.5, bold: true, color: C.primary,
        align, valign: 'middle', margin: 0, isTextBox: true,
        objectName: `ovl_mark_t_${i}`,
      });
    }
  });
}

// 「見るところ」の箱: items = [{n, text}](最大3), opt = {x, y, w, h, title, name}
function lookBox(s, items = [], opt = {}) {
  const x = opt.x ?? 8.55, y = opt.y ?? 1.98, w = opt.w ?? (W - M - x), h = opt.h ?? 2.4;
  const title = opt.title ?? '見るところ', name = opt.name || 'look';
  box(s, x, y, w, h, { fill: C.tint, line: C.light, round: true, name: `ovl_${name}_bg` });
  text(s, title, {
    x: x + 0.14, y: y + 0.10, w: w - 0.28, h: 0.30,
    fontSize: 11, bold: true, color: C.dark, valign: 'middle', margin: 0,
    objectName: `ovl_${name}_head`,
  });
  const list = (items || []).slice(0, 3);
  const topY = y + 0.46, availH = h - 0.54, rowH = availH / Math.max(1, list.length);
  list.forEach((it, i) => {
    const ry = topY + i * rowH;
    s.addShape('ellipse', {
      x: x + 0.14, y: ry + 0.04, w: 0.24, h: 0.24,
      fill: { color: C.primary }, line: { color: C.primary },
      objectName: `ovl_${name}_c_${i}`,
    });
    s.addText(String(it.n ?? (i + 1)), {
      x: x + 0.14, y: ry + 0.04, w: 0.24, h: 0.24,
      fontFace: FONT, fontSize: 9, bold: true, color: C.white,
      align: 'center', valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_${name}_n_${i}`,
    });
    text(s, String(it.text), {
      x: x + 0.46, y: ry + 0.02, w: w - 0.58, h: Math.max(0.36, rowH - 0.04),
      fontSize: 9.5, color: C.text, valign: 'top', margin: 0,
      objectName: `ovl_${name}_t_${i}`,
    });
  });
}

// 収益非対称棒(ペイオフ): d = {price, unit, rows:[{label, value, p, note}], floor:{value, label}, zones:[{from, to, label}]}
// opt = {x, y, w, h, name}
function payoffBar(s, d, opt = {}) {
  const X = opt.x ?? M, Y = opt.y ?? 2.22, WD = opt.w ?? 7.60, HD = opt.h ?? 3.60;
  const pfx = opt.name || 'po';
  const price = Number(d.price) || 0;
  const unit = d.unit ?? '円';
  const rows = d.rows || [];
  const zones = d.zones || [];
  if (!rows.length) return;

  const fmtEnd = (r) => {
    const diff = r.value - price;
    const pct = price ? Math.round((diff / price) * 100) : 0;
    const sign = pct > 0 ? '+' : (pct < 0 ? '−' : '±');
    const pTxt = r.p !== undefined ? ` 確率${Math.round(r.p * 100)}%` : '';
    return `${Math.round(r.value).toLocaleString('en-US')}${unit} (${sign}${Math.abs(pct)}%)${pTxt}`;
  };

  const labelW = 0.86;
  const endTxts = rows.map(fmtEnd);
  const leftRows = rows.map((r, i) => ({ r, t: endTxts[i] })).filter(x => x.r.value < price);
  const rightRows = rows.map((r, i) => ({ r, t: endTxts[i] })).filter(x => x.r.value >= price);
  const maxLeftLblW = leftRows.length
    ? Math.max(...leftRows.map(x => estW(x.t, 8.5) * 1.15 + 0.16)) + 0.06
    : 0.15;
  const maxRightLblW = rightRows.length
    ? Math.max(...rightRows.map(x => Math.max(estW(x.t, 8.5), x.r.note ? estW(x.r.note, 8) : 0) * 1.15 + 0.20))
    : 0.40;

  const diffs = rows.map(r => r.value - price);
  if (d.floor) diffs.push(d.floor.value - price);
  zones.forEach(z => { diffs.push(z.from - price, z.to - price); });
  const minDiff = Math.min(0, ...diffs);
  const maxDiff = Math.max(0, ...diffs);
  const span = (maxDiff - minDiff) || 1;

  const availBarW = Math.max(1.5, WD - labelW - maxLeftLblW - maxRightLblW - 0.12);
  const scale = availBarW / span;
  const xZero = X + labelW + maxLeftLblW + (-minDiff) * scale;
  const px = (v) => xZero + (v - price) * scale;

  const topPad = 0.34;
  const botPad = (zones.length || d.floor) ? 0.38 : 0.12;
  const plotTop = Y + topPad;
  const plotH = Math.max(0.8, HD - topPad - botPad);
  const plotBot = plotTop + plotH;

  // 1. 買う価格帯(棒の列の下に細い帯)
  zones.forEach((z, i) => {
    const zx0 = px(Math.min(z.from, z.to));
    const zx1 = px(Math.max(z.from, z.to));
    const zw = Math.max(0.02, zx1 - zx0);
    s.addShape('rect', {
      x: zx0, y: plotBot + 0.02, w: zw, h: 0.12,
      fill: { color: i === 0 ? C.light : C.rule },
      line: { color: i === 0 ? C.primary : C.sub, width: 0.5 },
      objectName: `ovl_${pfx}_zone_${i}`,
    });
    if (z.label) {
      const lbl = String(z.label);
      const lw = Math.max(zw, estW(lbl, 8) * 1.15 + 0.16);
      const narrow = zw < lw;
      let lx = zx0 + (zw - lw) / 2;
      let align = 'center';
      if (zones.length >= 2 && narrow) {
        if (i === 0) {
          lx = zx1 - lw - 0.03;
          align = 'right';
        } else {
          lx = zx0 + 0.03;
          align = 'left';
        }
      }
      s.addText(lbl, {
        x: lx, y: plotBot + 0.16, w: lw, h: 0.22,
        fontFace: FONT, fontSize: 8, bold: i === 0, color: i === 0 ? C.primary : C.sub,
        align, valign: 'middle', margin: 0, isTextBox: true,
        objectName: `ovl_${pfx}_zonel_${i}`,
      });
    }
  });

  // 2. 下値の支え(縦の破線)
  if (d.floor) {
    const fx = px(d.floor.value);
    s.addShape('line', {
      x: fx, y: plotTop - 0.02, w: 0.001, h: plotH + 0.04,
      line: { color: C.dark, width: 1.0, dashType: 'dash' },
      objectName: `ovl_${pfx}_floor`,
    });
    if (d.floor.label) {
      const flw = estW(d.floor.label, 8) * 1.15 + 0.16;
      const fy = zones.length ? (plotTop - 0.26) : (plotBot + 0.06);
      s.addText(String(d.floor.label), {
        x: fx - flw / 2, y: fy, w: flw, h: 0.22,
        fontFace: FONT, fontSize: 8, bold: true, color: C.dark,
        align: 'center', valign: 'middle', margin: 0, isTextBox: true,
        objectName: `ovl_${pfx}_floorl`,
      });
    }
  }

  // 3. シナリオ行と横棒
  const rowH = plotH / rows.length;
  rows.forEach((r, i) => {
    const ry = plotTop + i * rowH;
    const bh = Math.min(0.32, rowH * 0.54);
    const by = ry + (rowH - bh) / 2;
    const isDown = r.value < price;
    const isBase = String(r.label).includes('基準');
    const isBull = String(r.label).includes('強気');
    const barFill = isDown ? C.red : (isBase ? C.primary : (isBull ? C.light : C.rule));
    const barLine = isDown ? C.red : (isBase ? C.dark : (isBull ? C.light : C.sub));
    const bw = Math.abs(r.value - price) * scale;
    const bx = isDown ? xZero - bw : xZero;

    s.addText(String(r.label), {
      x: X, y: ry, w: labelW - 0.06, h: rowH,
      fontFace: FONT, fontSize: 9, bold: isBase,
      color: isDown ? C.red : (isBase ? C.dark : C.text),
      align: 'left', valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_${pfx}_lbl_${i}`,
    });

    if (bw > 0) {
      s.addShape('rect', {
        x: bx, y: by, w: bw, h: bh,
        fill: { color: barFill },
        line: { color: barLine, width: isBase ? 0.75 : 0.5 },
        objectName: `ovl_${pfx}_bar_${i}`,
      });
    }

    const endTxt = endTxts[i];
    const lw = estW(endTxt, 8.5) * 1.15 + 0.16;
    if (isDown) {
      s.addText(endTxt, {
        x: bx - lw - 0.05, y: ry, w: lw, h: rowH,
        fontFace: FONT, fontSize: 8.5, bold: true, color: C.red,
        align: 'right', valign: 'middle', margin: 0, isTextBox: true,
        objectName: `ovl_${pfx}_v_${i}`,
      });
      if (r.note) {
        const nw = Math.max(1.2, estW(r.note, 8) * 1.15 + 0.16);
        s.addText(String(r.note), {
          x: xZero + 0.08, y: ry, w: nw, h: rowH,
          fontFace: FONT, fontSize: 8, color: C.sub,
          align: 'left', valign: 'middle', margin: 0, isTextBox: true,
          objectName: `ovl_${pfx}_note_${i}`,
        });
      }
    } else {
      const hasNote = !!r.note;
      s.addText(endTxt, {
        x: bx + bw + 0.06, y: hasNote ? (by - 0.04) : ry, w: lw, h: hasNote ? 0.22 : rowH,
        fontFace: FONT, fontSize: 8.5, bold: isBase, color: isBase ? C.primary : C.text,
        align: 'left', valign: 'middle', margin: 0, isTextBox: true,
        objectName: `ovl_${pfx}_v_${i}`,
      });
      if (hasNote) {
        const nw = estW(r.note, 8) * 1.15 + 0.16;
        s.addText(String(r.note), {
          x: bx + bw + 0.06, y: by + bh / 2 + 0.02, w: nw, h: 0.20,
          fontFace: FONT, fontSize: 8, color: C.sub,
          align: 'left', valign: 'middle', margin: 0, isTextBox: true,
          objectName: `ovl_${pfx}_note_${i}`,
        });
      }
    }
  });

  // 4. 現在値の 0 縦線と上部ラベル
  s.addShape('line', {
    x: xZero, y: plotTop - 0.04, w: 0.001, h: plotH + 0.08,
    line: { color: C.dark, width: 1.5 },
    objectName: `ovl_${pfx}_zero`,
  });
  const zTxt = `現在値 ${Math.round(price).toLocaleString('en-US')}${unit}`;
  const zw = Math.max(1.5, estW(zTxt, 9) * 1.15 + 0.16);
  s.addText(zTxt, {
    x: Math.max(X, Math.min(X + WD - zw, xZero - zw / 2)), y: Y, w: zw, h: 0.26,
    fontFace: FONT, fontSize: 9, bold: true, color: C.dark,
    align: 'center', valign: 'middle', margin: 0, isTextBox: true,
    objectName: `ovl_${pfx}_zerol`,
  });
}

// 階段の図(段差と閾値): d = {unit, points:[{label, value}], events:[{i, label}], threshold:{value, label}, line:{label, values:[..]}}
// opt = {x, y, w, h, name}
function stepChart(s, d, opt = {}) {
  const X = opt.x ?? M, Y = opt.y ?? 2.22, WD = opt.w ?? 7.60, HD = opt.h ?? 3.60;
  const pfx = opt.name || 'st';
  const pts = d.points || [];
  const n = pts.length;
  if (!n) return;
  const unit = d.unit ?? '';
  const lineVals = (d.line && d.line.values) || [];

  const maxV = Math.max(
    1,
    ...pts.map(p => p.value),
    ...lineVals,
    d.threshold ? d.threshold.value : 0
  );
  const topPad = 0.56, botPad = 0.38;
  const plotLeft = X + 0.08;
  const plotW = WD - 0.16;
  const plotTop = Y + topPad;
  const plotH = Math.max(0.8, HD - topPad - botPad);
  const plotBot = plotTop + plotH;
  const colW = plotW / n;
  const xCol = (i) => plotLeft + i * colW;
  const cx = (i) => xCol(i) + colW / 2;
  const scaleY = plotH / maxV;
  const py = (v) => plotBot - v * scaleY;

  // 連続する同値を段にまとめる
  const runs = [];
  pts.forEach((p, i) => {
    const last = runs[runs.length - 1];
    if (last && last.value === p.value) last.i1 = i;
    else runs.push({ i0: i, i1: i, value: p.value });
  });

  if (unit) {
    s.addText(String(unit), {
      x: X, y: Y, w: 1.0, h: 0.22,
      fontFace: FONT, fontSize: 8, color: C.sub,
      align: 'left', valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_${pfx}_unit`,
    });
  }

  const evMin = (d.events && d.events.length) ? Math.min(...d.events.map(e => e.i)) : Infinity;

  // 1. 段の面
  runs.forEach((r, rIdx) => {
    const isLast = rIdx === runs.length - 1 || r.i0 >= evMin;
    const rx = xCol(r.i0);
    const rw = (r.i1 - r.i0 + 1) * colW;
    const rh = r.value * scaleY;
    const ry = plotBot - rh;
    s.addShape('rect', {
      x: rx, y: ry, w: rw, h: Math.max(0.01, rh),
      fill: { color: isLast ? C.tint : C.gray },
      line: { color: isLast ? C.tint : C.gray, width: 0 },
      objectName: `ovl_${pfx}_step_${rIdx}`,
    });
  });

  // 2. 水平の段の線と垂直の立ち上がり線 + 段の上の値
  runs.forEach((r, rIdx) => {
    const isLast = rIdx === runs.length - 1 || r.i0 >= evMin;
    const rx0 = xCol(r.i0);
    const rx1 = xCol(r.i1 + 1);
    const ry = py(r.value);
    s.addShape('line', {
      x: rx0, y: ry, w: rx1 - rx0, h: 0,
      line: { color: isLast ? C.primary : C.sub, width: 2.25 },
      objectName: `ovl_${pfx}_htop_${rIdx}`,
    });
    if (rIdx > 0) {
      const prevY = py(runs[rIdx - 1].value);
      s.addShape('line', {
        x: rx0, y: Math.min(prevY, ry), w: 0.001, h: Math.max(0.01, Math.abs(prevY - ry)),
        line: { color: isLast ? C.primary : C.sub, width: 2.0 },
        objectName: `ovl_${pfx}_vstep_${rIdx}`,
      });
    }
    const vTxt = `${Math.round(r.value).toLocaleString('en-US')}${unit}`;
    const vw = estW(vTxt, 9.5) * 1.15 + 0.16;
    const sameStart = rIdx === 0 && lineVals.length && lineVals[0] === r.value;
    const vx = sameStart ? (cx(r.i0) - vw / 2) : ((rx0 + rx1) / 2 - vw / 2);
    s.addText(vTxt, {
      x: vx, y: ry - 0.26, w: vw, h: 0.24,
      fontFace: FONT, fontSize: 9.5, bold: true, color: isLast ? C.primary : C.sub,
      align: 'center', valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_${pfx}_sval_${rIdx}`,
    });
  });

  // 3. 閾値(横の破線)
  if (d.threshold) {
    const ty = py(d.threshold.value);
    s.addShape('line', {
      x: plotLeft, y: ty, w: plotW, h: 0,
      line: { color: C.red, width: 1.0, dashType: 'dash' },
      objectName: `ovl_${pfx}_thr`,
    });
    if (d.threshold.label) {
      const tw = estW(d.threshold.label, 8) * 1.15 + 0.16;
      s.addText(String(d.threshold.label), {
        x: plotLeft + plotW - tw, y: ty - 0.22, w: tw, h: 0.20,
        fontFace: FONT, fontSize: 8, bold: true, color: C.red,
        align: 'right', valign: 'middle', margin: 0, isTextBox: true,
        objectName: `ovl_${pfx}_thrl`,
      });
    }
  }

  // 4. 出来事(立ち上がりの縦の細線と短い文)
  (d.events || []).forEach((ev, i) => {
    const ex = xCol(ev.i);
    s.addShape('line', {
      x: ex, y: Y + 0.04, w: 0.001, h: plotBot - (Y + 0.04),
      line: { color: C.primary, width: 1.0, dashType: 'dash' },
      objectName: `ovl_${pfx}_ev_${i}`,
    });
    if (ev.label) {
      const ew = estW(ev.label, 8.5) * 1.15 + 0.16;
      const lx = (ex + 0.06 + ew <= X + WD) ? (ex + 0.06) : Math.max(X, ex - ew - 0.06);
      const align = (ex + 0.06 + ew <= X + WD) ? 'left' : 'right';
      s.addText(String(ev.label), {
        x: lx, y: Y, w: ew, h: 0.24,
        fontFace: FONT, fontSize: 8.5, bold: true, color: C.primary,
        align, valign: 'middle', margin: 0, isTextBox: true,
        objectName: `ovl_${pfx}_evl_${i}`,
      });
    }
  });

  // 5. 比較の折れ線
  if (lineVals.length) {
    for (let i = 0; i < lineVals.length - 1; i++) {
      const x1 = cx(i), y1 = py(lineVals[i]);
      const x2 = cx(i + 1), y2 = py(lineVals[i + 1]);
      s.addShape('line', {
        x: Math.min(x1, x2), y: Math.min(y1, y2),
        w: Math.abs(x2 - x1) || 0.001, h: Math.abs(y2 - y1) || 0.001,
        flipH: x2 < x1, flipV: y2 < y1,
        line: { color: C.sub, width: 2.0 },
        objectName: `ovl_${pfx}_lseg_${i}`,
      });
    }
    lineVals.forEach((v, i) => {
      const px0 = cx(i), py0 = py(v);
      s.addShape('ellipse', {
        x: px0 - 0.05, y: py0 - 0.05, w: 0.10, h: 0.10,
        fill: { color: C.white }, line: { color: C.sub, width: 1.5 },
        objectName: `ovl_${pfx}_ldot_${i}`,
      });
      const vStr = String(v);
      const vw = Math.max(0.42, estW(vStr, 8) * 1.15 + 0.14);
      const below = (i === 0 && v === pts[0].value) || (v < pts[i].value);
      s.addText(vStr, {
        x: px0 - vw / 2, y: below ? (py0 + 0.06) : (py0 - 0.22), w: vw, h: 0.20,
        fontFace: FONT, fontSize: 8, bold: false, color: C.sub,
        align: 'center', valign: 'middle', margin: 0, isTextBox: true,
        objectName: `ovl_${pfx}_lval_${i}`,
      });
    });
    if (d.line.label) {
      const lw = estW(d.line.label, 8.5) * 1.15 + 0.16;
      const lastY = py(lineVals[lineVals.length - 1]);
      s.addText(String(d.line.label), {
        x: plotLeft + plotW - lw, y: lastY - 0.28, w: lw, h: 0.22,
        fontFace: FONT, fontSize: 8.5, bold: true, color: C.sub,
        align: 'right', valign: 'middle', margin: 0, isTextBox: true,
        objectName: `ovl_${pfx}_llbl`,
      });
    }
  }

  // 6. ベースラインと X 軸ラベル
  s.addShape('line', {
    x: plotLeft, y: plotBot, w: plotW, h: 0,
    line: { color: C.rule, width: 0.75 },
    objectName: `ovl_${pfx}_base`,
  });
  pts.forEach((p, i) => {
    const lbl = String(p.label);
    const lw = Math.max(colW, estW(lbl, 8.5) * 1.15 + 0.12);
    s.addText(lbl, {
      x: cx(i) - lw / 2, y: plotBot + 0.06, w: lw, h: 0.24,
      fontFace: FONT, fontSize: 8.5, color: C.text,
      align: 'center', valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_${pfx}_xl_${i}`,
    });
  });
}

// 体制転換の時系列: d = {labels:[..], bars:{label, unit, values:[..]}, line:{label, unit, values:[..]}, breakIndex, beforeLabel, afterLabel, highlight:[..]}
// opt = {x, y, w, h, name}
function regimeSeries(s, d, opt = {}) {
  const X = opt.x ?? M, Y = opt.y ?? 2.22, WD = opt.w ?? 7.60, HD = opt.h ?? 3.60;
  const pfx = opt.name || 'rg';
  const labels = d.labels || [];
  const n = labels.length;
  const bVals = (d.bars && d.bars.values) || [];
  const lVals = (d.line && d.line.values) || [];
  if (!n || !bVals.length) return;

  const bi = d.breakIndex ?? (n - 1);
  const hlSet = new Set(d.highlight || [bi]);
  const leftAxisW = 0.44;
  const rightAxisW = lVals.length ? 1.05 : 0.15;
  const topPad = 0.50, botPad = 0.44;
  const plotLeft = X + leftAxisW;
  const plotW = Math.max(1.5, WD - leftAxisW - rightAxisW);
  const plotTop = Y + topPad;
  const plotH = Math.max(0.8, HD - topPad - botPad);
  const plotBot = plotTop + plotH;
  const colW = plotW / n;
  const xCol = (i) => plotLeft + i * colW;
  const cx = (i) => xCol(i) + colW / 2;

  const barMax = Math.max(1, ...bVals) * 1.25;
  const scaleBar = plotH / barMax;
  const pyBar = (v) => plotBot - v * scaleBar;

  const lineMax = lVals.length ? Math.max(1, ...lVals) * 1.08 : 1;
  const scaleLine = plotH / lineMax;
  const pyLine = (v) => plotBot - v * scaleLine;

  const bx = xCol(bi);
  const bandTop = Y + 0.24;
  const bandH = plotBot - bandTop;

  // 1. 前後の背景帯
  if (bi > 0) {
    s.addShape('rect', {
      x: plotLeft, y: bandTop, w: bx - plotLeft, h: bandH,
      fill: { color: C.gray }, line: { color: C.gray, width: 0 },
      objectName: `ovl_${pfx}_bg_bef`,
    });
  }
  s.addShape('rect', {
    x: bx, y: bandTop, w: plotLeft + plotW - bx, h: bandH,
    fill: { color: C.tint }, line: { color: C.tint, width: 0 },
    objectName: `ovl_${pfx}_bg_aft`,
  });

  // 2. 前後ラベル
  if (d.beforeLabel && bi > 0) {
    const bwLbl = Math.max(0.8, bx - plotLeft - 0.16);
    s.addText(String(d.beforeLabel), {
      x: plotLeft + 0.06, y: Y + 0.26, w: bwLbl, h: 0.22,
      fontFace: FONT, fontSize: 8.5, bold: true, color: C.sub,
      align: 'center', valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_${pfx}_befl`,
    });
  }
  const cxAfter = (bx + plotLeft + plotW) / 2;
  if (d.afterLabel) {
    const awLbl = Math.max(plotLeft + plotW - bx, estW(d.afterLabel, 8.5) * 1.15 + 0.16);
    const ayLbl = (plotLeft + plotW - bx < awLbl) ? (Y + 0.02) : (Y + 0.26);
    s.addText(String(d.afterLabel), {
      x: cxAfter - awLbl / 2, y: ayLbl, w: awLbl, h: 0.22,
      fontFace: FONT, fontSize: 8.5, bold: true, color: C.primary,
      align: 'center', valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_${pfx}_aftl`,
    });
  }

  // 3. 棒(左軸に比例)
  bVals.forEach((v, i) => {
    const bw = colW * 0.58;
    const xBar = xCol(i) + (colW - bw) / 2;
    const bh = v * scaleBar;
    const yBar = plotBot - bh;
    const isHl = hlSet.has(i) || i >= bi;
    s.addShape('rect', {
      x: xBar, y: yBar, w: bw, h: Math.max(0.01, bh),
      fill: { color: isHl ? C.primary : C.rule },
      line: { color: isHl ? C.dark : C.rule, width: 0.5 },
      objectName: `ovl_${pfx}_bar_${i}`,
    });
  });

  // 4. 前後それぞれの棒の平均線と値
  const bUnit = (d.bars && d.bars.unit) || '';
  if (bi > 0) {
    const avgBefore = bVals.slice(0, bi).reduce((a, b) => a + b, 0) / bi;
    const yAvgB = pyBar(avgBefore);
    s.addShape('line', {
      x: plotLeft, y: yAvgB, w: bx - plotLeft, h: 0,
      line: { color: C.sub, width: 1.0, dashType: 'dash' },
      objectName: `ovl_${pfx}_avgb`,
    });
    const avgBTxt = `平均 ${avgBefore.toFixed(1)}${bUnit}`;
    const abw = estW(avgBTxt, 8) * 1.15 + 0.16;
    s.addText(avgBTxt, {
      x: plotLeft + 0.06, y: yAvgB - 0.23, w: abw, h: 0.21,
      fontFace: FONT, fontSize: 8, bold: true, color: C.sub,
      fill: { color: C.gray }, align: 'left', valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_${pfx}_avgbl`,
    });
  }
  if (n - bi > 0) {
    const avgAfter = bVals.slice(bi).reduce((a, b) => a + b, 0) / (n - bi);
    const yAvgA = pyBar(avgAfter);
    s.addShape('line', {
      x: bx, y: yAvgA, w: plotLeft + plotW - bx, h: 0,
      line: { color: C.primary, width: 1.25 },
      objectName: `ovl_${pfx}_avga`,
    });
    const avgATxt = `${avgAfter.toFixed(1)}${bUnit}`;
    const aaw = Math.max(0.54, estW(avgATxt, 8.5) * 1.15 + 0.14);
    const narrowAfter = (plotLeft + plotW - bx) < aaw + 0.08;
    const avgAX = narrowAfter ? (plotLeft + plotW + 0.06) : (cxAfter - aaw / 2);
    const avgAY = narrowAfter ? (yAvgA - 0.10) : (yAvgA - 0.22);
    s.addText(avgATxt, {
      x: avgAX, y: avgAY, w: aaw, h: 0.20,
      fontFace: FONT, fontSize: 8.5, bold: true, color: C.primary,
      fill: narrowAfter ? undefined : { color: C.tint },
      align: narrowAfter ? 'left' : 'center', valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_${pfx}_avgal`,
    });
  }

  // 5. 転換点の縦の破線
  s.addShape('line', {
    x: bx, y: bandTop, w: 0.001, h: bandH,
    line: { color: C.primary, width: 1.25, dashType: 'dash' },
    objectName: `ovl_${pfx}_brk`,
  });

  // 6. 折れ線(右軸に比例)
  if (lVals.length) {
    for (let i = 0; i < lVals.length - 1; i++) {
      const x1 = cx(i), y1 = pyLine(lVals[i]);
      const x2 = cx(i + 1), y2 = pyLine(lVals[i + 1]);
      s.addShape('line', {
        x: Math.min(x1, x2), y: Math.min(y1, y2),
        w: Math.abs(x2 - x1) || 0.001, h: Math.abs(y2 - y1) || 0.001,
        flipH: x2 < x1, flipV: y2 < y1,
        line: { color: C.sub, width: 2.0 },
        objectName: `ovl_${pfx}_lseg_${i}`,
      });
    }
    lVals.forEach((v, i) => {
      s.addShape('ellipse', {
        x: cx(i) - 0.045, y: pyLine(v) - 0.045, w: 0.09, h: 0.09,
        fill: { color: C.white }, line: { color: C.sub, width: 1.5 },
        objectName: `ovl_${pfx}_ldot_${i}`,
      });
    });
  }

  // 7. 系列名の直接配置と左右の軸目盛り(最小・最大など2〜3個)
  if (d.bars && d.bars.label) {
    const bSeriesTxt = `■ ${d.bars.label}${bUnit ? '(' + bUnit + ')' : ''}`;
    const bsw = estW(bSeriesTxt, 8.5) * 1.15 + 0.16;
    s.addText(bSeriesTxt, {
      x: plotLeft, y: Y, w: bsw, h: 0.22,
      fontFace: FONT, fontSize: 8.5, bold: true, color: C.primary,
      align: 'left', valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_${pfx}_blbl`,
    });
  }
  const bMin = Math.min(...bVals), bMax = Math.max(...bVals);
  [
    { v: 0, txt: '0' },
    { v: bMin, txt: bMin.toFixed(1) },
    { v: bMax, txt: bMax.toFixed(1) },
  ].forEach((tk, idx) => {
    s.addText(tk.txt, {
      x: X, y: pyBar(tk.v) - 0.10, w: leftAxisW - 0.06, h: 0.20,
      fontFace: FONT, fontSize: 8, color: C.sub,
      align: 'right', valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_${pfx}_ly_${idx}`,
    });
  });

  if (lVals.length) {
    const lMin = Math.min(...lVals), lMax = Math.max(...lVals);
    const lUnit = (d.line && d.line.unit) || '';
    const lastV = lVals[lVals.length - 1];
    const lastY = pyLine(lastV);
    const rX = plotLeft + plotW + 0.06;
    const rW = rightAxisW - 0.06;
    const lLbl = `${(d.line && d.line.label) || ''}\n${lastV}${lUnit ? '(' + lUnit + ')' : ''}`;
    s.addText(lLbl, {
      x: rX, y: Math.max(Y + 0.24, lastY - 0.28), w: rW, h: 0.38,
      fontFace: FONT, fontSize: 8, bold: true, color: C.sub,
      align: 'left', valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_${pfx}_llbl`,
    });
    const rTicks = [{ v: 0, txt: '0' }, { v: lMin, txt: String(lMin) }];
    if (lMax !== lastV) rTicks.push({ v: lMax, txt: String(lMax) });
    rTicks.forEach((tk, idx) => {
      s.addText(tk.txt, {
        x: rX, y: pyLine(tk.v) - 0.10, w: rW, h: 0.20,
        fontFace: FONT, fontSize: 8, color: C.sub,
        align: 'left', valign: 'middle', margin: 0, isTextBox: true,
        objectName: `ovl_${pfx}_ry_${idx}`,
      });
    });
  }

  // 8. ベースラインと X 軸ラベル
  s.addShape('line', {
    x: plotLeft, y: plotBot, w: plotW, h: 0,
    line: { color: C.rule, width: 0.75 },
    objectName: `ovl_${pfx}_base`,
  });
  labels.forEach((raw, i) => {
    let lbl = String(raw);
    if (!lbl.includes('\n') && estW(lbl, 8) * 1.15 > colW - 0.02) {
      const m = lbl.match(/^(\d+\/\d+)(.+)$/);
      if (m) lbl = m[1] + '\n' + m[2];
    }
    const isHl = hlSet.has(i) || i >= bi;
    const twoLine = lbl.includes('\n');
    const maxLineW = Math.max(...lbl.split('\n').map(ln => estW(ln, 8) * 1.15 + 0.06));
    const lw = Math.max(colW, maxLineW);
    s.addText(lbl, {
      x: cx(i) - lw / 2, y: plotBot + 0.04, w: lw, h: twoLine ? 0.36 : 0.22,
      fontFace: FONT, fontSize: 8, bold: isHl, color: isHl ? C.primary : C.sub,
      align: 'center', valign: 'top', margin: 0, isTextBox: true,
      objectName: `ovl_${pfx}_xl_${i}`,
    });
  });
}


// ======================= 2 軸のバブル図(製品ポートフォリオ・リスクマトリクス・確度×影響度で共用) =======================
// 2026-11-18 追加(利用者: 「製品群を製品ポートフォリオなんかにするとわかりやすい」「リスク要因とその起きうる確率、影響度を分析してほしい」)。
// 1 枚で「どこに何があるか」が 3 秒で分かる形にする。位置は値に比例、円の面積は size に比例(直径でなく面積)。
// d = {
//   xTitle, yTitle                    軸の名前(何を測るか + 単位。例: '相対的な強さ(市場シェア ÷ 最大の競合)'、'市場の伸び(年率 %)')
//   xMin, xMax, yMin, yMax            軸の範囲。xLog: true で横軸を対数(相対シェアのとき)
//   xTicks, yTicks: [値, …]           目盛り。xFmt / yFmt(値 → 文字)
//   xSplit, ySplit                    4 象限の境の値(破線)。省略すると線を引かない
//   quad: {tl, tr, bl, br}            象限の名前(例: PPM なら 花形・問題児・金のなる木・負け犬、リスクなら 最優先・監視・許容 など)
//   hot: 'tr'|'tl'|'br'|'bl'          注意を向ける象限を薄く塗る(リスク: 確率高 × 影響大)。heatTone: 'red'|'green'
//   items: [{label, x, y, size, tone: 'focus'|'dark'|'risk'|'muted'|'ok', sub, n, lpos: 'r'|'l'|'t'|'b'}]
//          label は名前(全角 10 字まで)、sub は数字 1 つ(例: '売上 14,627')。n は ①② の番号(lookBox と対応)
//   sizeMax                           最大の円の直径(inch。既定 0.95)。sizeLegend: '円の大きさ = 売上(百万ドル)'
//   arrows: [{from: [x, y], to: [x, y], label}]   動き(現在 → 5 年後など)を矢印で
// }
// opt = {x, y, w, h, name}。ラベルどうし・ラベルと円の重なりは L.warnings に入る(0 件にする)
function bubbleMatrix(s, d, opt = {}) {
  const pfx = opt.name || 'bm';
  const X0 = opt.x ?? 0.5, Y0 = opt.y ?? 1.66, W0 = opt.w ?? 7.9, H0 = opt.h ?? 4.6;
  const axL = 0.62, axB = 0.52, pT = 0.12, pR = 0.12;
  const px = X0 + axL, py = Y0 + pT, pw = W0 - axL - pR, ph = H0 - pT - axB;
  const lg = !!d.xLog;
  const tx = (v) => lg ? (Math.log(v) - Math.log(d.xMin)) / (Math.log(d.xMax) - Math.log(d.xMin)) : (v - d.xMin) / (d.xMax - d.xMin);
  const ty = (v) => (v - d.yMin) / (d.yMax - d.yMin);
  const cx = (v) => px + Math.max(0, Math.min(1, tx(v))) * pw;
  const cy = (v) => py + ph - Math.max(0, Math.min(1, ty(v))) * ph;
  const xFmt = d.xFmt || ((v) => String(v)), yFmt = d.yFmt || ((v) => String(v));
  // 円の位置を先に決める(象限の名前と矢印のラベルが円を避けるため)
  const items = d.items || [];
  const smax = Math.max(...items.map(it => Math.abs(it.size || 1)), 1e-9), dmax = d.sizeMax || 0.95;
  const circ = items.map((it) => {
    const dia = Math.max(0.2, dmax * Math.sqrt(Math.abs(it.size || smax) / smax));
    return { it, dia, x: cx(it.x) - dia / 2, y: cy(it.y) - dia / 2 };
  });
  const hit = (r, q) => Math.min(r[0] + r[2], q[0] + q[2]) - Math.max(r[0], q[0]) > 0.02 && Math.min(r[1] + r[3], q[1] + q[3]) - Math.max(r[1], q[1]) > 0.02;
  const placed = circ.map(c => [c.x, c.y, c.dia, c.dia, 'circle:' + c.it.label]);
  // 象限の塗りと境の線。象限の名前は角に置き、円と重なるなら同じ象限の反対の角(上 ↔ 下)へ移す
  const quadText = [];
  if (d.xSplit !== undefined && d.ySplit !== undefined) {
    const sx = cx(d.xSplit), sy = cy(d.ySplit);
    const quads = { tl: [px, py, sx - px, sy - py], tr: [sx, py, px + pw - sx, sy - py], bl: [px, sy, sx - px, py + ph - sy], br: [sx, sy, px + pw - sx, py + ph - sy] };
    Object.entries(quads).forEach(([k, [qx, qy, qw, qh]]) => {
      const hot = d.hot === k;
      s.addShape('rect', { x: qx, y: qy, w: qw, h: qh, fill: { color: hot ? (d.heatTone === 'green' ? C.tint : C.red) : C.white, transparency: hot && d.heatTone !== 'green' ? 88 : 0 },
        line: { color: C.white, width: 0 }, objectName: `ovl_${pfx}_q_${k}` });
      if (d.quad && d.quad[k]) {
        const right = k === 'tr' || k === 'br', top = k === 'tl' || k === 'tr';
        const lw = Math.min(qw - 0.1, estW(d.quad[k], 9) / 0.9 + 0.1);
        const lx = right ? qx + qw - lw - 0.06 : qx + 0.06;
        const cand = (top ? [qy + 0.04, qy + qh - 0.26] : [qy + qh - 0.26, qy + 0.04]).map(yy => [lx, yy, lw, 0.22, 'quad:' + k]);
        const r = cand.find(c => !placed.some(q => hit(c, q))) || cand[0];
        if (cand.every(c => placed.some(q => hit(c, q)))) warnings.push(`${pfx}: 象限の名前「${d.quad[k]}」が円に重なる(quad の文を短くするか、軸の範囲を広げる)`);
        placed.push(r);
        quadText.push({ r, t: d.quad[k], color: hot ? (d.heatTone === 'green' ? C.primary : C.red) : C.sub, right, k });
      }
    });
    s.addShape('line', { x: sx, y: py, w: 0.001, h: ph, line: { color: C.sub, width: 0.75, dashType: 'dash' }, objectName: `ovl_${pfx}_sx` });
    s.addShape('line', { x: px, y: sy, w: pw, h: 0.001, line: { color: C.sub, width: 0.75, dashType: 'dash' }, objectName: `ovl_${pfx}_sy` });
    quadText.forEach(q => s.addText(q.t, { x: q.r[0], y: q.r[1], w: q.r[2], h: q.r[3], fontFace: FONT, fontSize: 9, bold: true, color: q.color, align: q.right ? 'right' : 'left', valign: 'middle', margin: 0, isTextBox: true, objectName: `ovl_${pfx}_ql_${q.k}` }));
  }
  // 軸
  s.addShape('line', { x: px, y: py + ph, w: pw, h: 0.001, line: { color: C.sub, width: 1 }, objectName: `ovl_${pfx}_ax` });
  s.addShape('line', { x: px, y: py, w: 0.001, h: ph, line: { color: C.sub, width: 1 }, objectName: `ovl_${pfx}_ay` });
  (d.xTicks || []).forEach((v, i) => s.addText(xFmt(v), { x: cx(v) - 0.4, y: py + ph + 0.03, w: 0.8, h: 0.18, fontFace: FONT, fontSize: 8, color: C.sub, align: 'center', margin: 0, isTextBox: true, objectName: `ovl_${pfx}_xt_${i}` }));
  (d.yTicks || []).forEach((v, i) => s.addText(yFmt(v), { x: X0, y: cy(v) - 0.09, w: axL - 0.06, h: 0.18, fontFace: FONT, fontSize: 8, color: C.sub, align: 'right', margin: 0, isTextBox: true, objectName: `ovl_${pfx}_yt_${i}` }));
  if (d.xTitle) s.addText(d.xTitle + (lg ? '(対数目盛)' : '') + '  →', { x: px, y: py + ph + 0.24, w: pw, h: 0.22, fontFace: FONT, fontSize: 9, bold: true, color: C.dark, align: 'center', margin: 0, isTextBox: true, objectName: `ovl_${pfx}_xT` });
  if (d.yTitle) s.addText('↑ ' + d.yTitle, { x: px + 0.06, y: Y0 - 0.2, w: pw * 0.7, h: 0.2, fontFace: FONT, fontSize: 9, bold: true, color: C.dark, align: 'left', margin: 0, isTextBox: true, objectName: `ovl_${pfx}_yT` });
  // 円
  const TONE = { focus: C.primary, dark: C.dark, risk: C.red, muted: C.rule, ok: C.light, amber: C.amber };
  circ.slice().sort((a, b) => b.dia - a.dia).forEach((c, k) => {
    const col = TONE[c.it.tone || 'muted'] || C.rule;
    s.addShape('ellipse', { x: c.x, y: c.y, w: c.dia, h: c.dia, fill: { color: col, transparency: 20 }, line: { color: c.it.tone === 'muted' || !c.it.tone ? C.sub : col, width: 0.75 }, objectName: `ovl_${pfx}_c_${k}` });
    if (c.it.n) s.addText(CIRC[c.it.n] || String(c.it.n), { x: c.x + c.dia / 2 - 0.13, y: c.y + c.dia / 2 - 0.13, w: 0.26, h: 0.26, fontFace: FONT, fontSize: 10, bold: true,
      color: c.it.tone === 'muted' || c.it.tone === 'ok' || !c.it.tone ? C.dark : C.white, align: 'center', valign: 'middle', margin: 0, isTextBox: true, objectName: `ovl_${pfx}_n_${k}` });
  });
  // 矢印(動き)。線の外接の箱をラベルの避ける所に入れる
  (d.arrows || []).forEach((a) => {
    const x1 = cx(a.from[0]), y1 = cy(a.from[1]), x2 = cx(a.to[0]), y2 = cy(a.to[1]);
    arrow(s, x1, y1, x2, y2, { color: C.dark, width: 1.25, dash: 'dash' });
    placed.push([Math.min(x1, x2), Math.min(y1, y2) - 0.03, Math.abs(x2 - x1) || 0.06, (Math.abs(y2 - y1) || 0) + 0.06, 'arrow']);
    const lw = estW(a.label || '', 8) / 0.9 + 0.08;
    a._cand = a.label ? [[x2 + 0.06, y2 - 0.1], [x2 - lw / 2, y2 + 0.06], [x2 - lw / 2, y2 - 0.28], [x2 - lw - 0.06, y2 - 0.1]].map(([xx, yy]) => [xx, yy, lw, 0.2, 'arrowlabel']) : [];
  });
  // ラベル(右 → 左 → 上 → 下 の順に、円・他のラベル・象限の名前・矢印・図の外に重ならない所へ)
  circ.forEach((c, i) => {
    const lines = [c.it.label].concat(c.it.sub ? [c.it.sub] : []);
    const lw = Math.max(...lines.map(l => estW(l, 9))) / 0.9 + 0.08, lh = lines.length * 0.17 + 0.04;
    const ccx = c.x + c.dia / 2, ccy = c.y + c.dia / 2;
    const pos = { r: [c.x + c.dia + 0.04, ccy - lh / 2], l: [c.x - lw - 0.04, ccy - lh / 2], t: [ccx - lw / 2, c.y - lh - 0.02], b: [ccx - lw / 2, c.y + c.dia + 0.02] };
    const order = [c.it.lpos].concat(['r', 'l', 't', 'b']).filter((v, j, a) => v && a.indexOf(v) === j);
    let best = null;
    for (const k of order) {
      const r = [pos[k][0], pos[k][1], lw, lh];
      const inside = r[0] >= X0 && r[0] + r[2] <= X0 + W0 && r[1] >= Y0 - 0.02 && r[1] + r[3] <= py + ph;
      if (inside && !placed.some(q => q[4] !== 'circle:' + c.it.label && hit(r, q))) { best = r; break; }
    }
    if (!best) { const k = order[0]; best = [pos[k][0], pos[k][1], lw, lh]; warnings.push(`${pfx}: 「${c.it.label}」のラベルが円か他のラベルに重なる(lpos を変えるか、label を短く)`); }
    placed.push(best.concat(['label:' + c.it.label]));
    s.addText(lines.map((l, j) => ({ text: l, options: { bold: j === 0, fontSize: j === 0 ? 9 : 8.5, color: j === 0 ? C.text : C.sub, breakLine: j < lines.length - 1 } })),
      { x: best[0], y: best[1], w: best[2], h: best[3], fontFace: FONT, margin: 0, valign: 'middle', isTextBox: true, objectName: `ovl_${pfx}_l_${i}` });
  });
  (d.arrows || []).forEach((a, i) => {
    if (!a.label) return;
    const r = a._cand.find(c => !placed.some(q => q[4] !== 'arrow' && hit(c, q))) || a._cand[0];
    if (!a._cand.some(c => !placed.some(q => q[4] !== 'arrow' && hit(c, q)))) warnings.push(`${pfx}: 矢印のラベル「${a.label}」が重なる`);
    placed.push(r);
    s.addText(a.label, { x: r[0], y: r[1], w: r[2], h: r[3], fontFace: FONT, fontSize: 8, bold: true, color: C.dark, margin: 0, valign: 'middle', isTextBox: true, objectName: `ovl_${pfx}_al_${i}` });
  });
  if (d.sizeLegend) s.addText('○ ' + d.sizeLegend, { x: px + pw - 3.2, y: py + ph + 0.24, w: 3.2, h: 0.2, fontFace: FONT, fontSize: 8, color: C.sub, align: 'right', margin: 0, isTextBox: true, objectName: `ovl_${pfx}_sl` });
}

// 用語の注釈(図の下や右に置く): items = [{term, plain, why}]。「用語: 意味 — この資料で見る理由」を 1 項目 1 行で書く
// 利用者(2026-11-18): 「専門用語が出てくるが注釈がない。何故その用語が必要かも不明」。初出のページに必ず置く(lint_deck.py が照合する)
function termNotes(s, items = [], opt = {}) {
  const x = opt.x ?? M, y = opt.y ?? 6.3, w = opt.w ?? (W - 2 * M), name = opt.name || 'terms';
  const fs = opt.fontSize || 8.5, rowH = fs / 72 * 1.3;
  const runs = [];
  items.forEach((it, i) => {
    runs.push({ text: it.term, options: { bold: true, color: C.dark } });
    runs.push({ text: `: ${it.plain}` + (it.why ? ` — ${it.why}` : ''), options: { color: C.text, breakLine: i < items.length - 1 } });
  });
  const h = opt.h ?? Math.max(0.22, items.length * rowH + 0.06);
  s.addShape('rect', { x, y, w, h, fill: { color: C.gray }, line: { color: C.gray }, objectName: `ovl_${name}_bg` });
  s.addText([{ text: '用語  ', options: { bold: true, color: C.teal } }].concat(runs), { x: x + 0.08, y, w: w - 0.16, h, fontFace: FONT, fontSize: fs, margin: 0, valign: 'middle', isTextBox: true, objectName: name });
}

// 保存: pptxgenjs 3.12 は複数の文字の塊(runs)を持つ段落で <a:pPr> を塊ごとに出す(スキーマ違反で、PowerPoint の修復の警告の原因)。
// 段落ごとに最初の <a:pPr> だけを残して書き出す。build.js・one.js はこの関数で保存する
function dedupePPr(xml) {
  return xml.replace(/<a:p>([\s\S]*?)<\/a:p>/g, (m, inner) => {
    let seen = false;
    return '<a:p>' + inner.replace(/<a:pPr\b[^>]*\/>|<a:pPr\b[^>]*>[\s\S]*?<\/a:pPr>/g, (pp) => { if (seen) return ''; seen = true; return pp; }) + '</a:p>';
  });
}
async function save(pres, fileName) {
  const JSZip = require('./node_modules/jszip');
  const buf = await pres.write({ outputType: 'nodebuffer' });
  const zip = await JSZip.loadAsync(buf);
  let fixed = 0;
  for (const f of Object.keys(zip.files).filter(n => /^ppt\/(slides|slideLayouts|slideMasters)\/[^/]+\.xml$/.test(n))) {
    const x = await zip.file(f).async('string'), y = dedupePPr(x);
    if (y !== x) { fixed++; zip.file(f, y); }
  }
  require('fs').writeFileSync(fileName, await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' }));
  return fixed;
}

module.exports = { F, save, dedupePPr, pptxgen, C, GRADE, FONT, W, H, M, GRID, CHAPTERS, MT, newDeck, text, contentSlide, header, badge, takeaway, box, arrow, table, agenda, cover, closing, chartStyle,
  paneHead, bullets, kpiTiles, chartPanel, structure, t15Side, twoPane, flow, matrix, T15,
  flowMap, mechPanel, kpiBand, timeBand, waterfall, marks, lookBox, payoffBar, stepChart, regimeSeries, bubbleMatrix, termNotes, estW, CIRC, setCtx, warnings, notices };
