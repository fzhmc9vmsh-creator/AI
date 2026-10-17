// 共通部品(invest-consulting-deck/references/design-spec.md 準拠)。全スライドはこの部品だけで組む。
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
const GRID = {
  title: { x: M, y: 0.32, w: W - 2 * M - 1.2, h: 0.86 },      // 右端 1.2in は評価バッジ用に空ける
  kicker: { x: M, y: 1.2, w: W - 2 * M, h: 0.3 },
  body: { x: M, y: 1.62, w: W - 2 * M, h: 5.13 },              // 1.62〜6.75
  src: { x: M, y: 6.88, w: 10.8, h: 0.42 },
  pg: { x: W - M - 0.6, y: 7.0, w: 0.6, h: 0.25 },
};
const CHAPTERS = ['評価総括', '事業・需給・成長', '13条件の構造分析', 'バリュエーション・リスク・投資アクション'];

function newDeck() {
  const pres = new pptxgen();
  pres.layout = 'LAYOUT_WIDE';
  pres.author = 'Oracle 長期保有適格性審査';
  pres.title = 'Oracle(ORCL)長期保有適格性審査';
  pres.theme = { headFontFace: FONT, bodyFontFace: FONT };
  return pres;
}

function text(slide, str, o) {
  slide.addText(str, Object.assign({ fontFace: FONT, fontSize: 11, color: C.text, margin: 0.04, valign: 'top', isTextBox: true, fit: 'none' }, o));
}

function contentSlide(pres, { title, kicker, source, page, grade, condNo }) {
  const s = pres.addSlide();
  s.background = { color: C.white };
  text(s, title, Object.assign({}, GRID.title, { objectName: 'title', fontSize: 19, bold: true, color: C.primary, valign: 'middle', margin: 0 }));
  if (kicker) text(s, kicker, Object.assign({}, GRID.kicker, { objectName: 'kicker', fontSize: 11, color: C.sub, margin: 0 }));
  if (source) text(s, '出所: ' + source, Object.assign({}, GRID.src, { objectName: 'src', fontSize: 8, color: C.sub, margin: 0, valign: 'bottom' }));
  text(s, String(page), Object.assign({}, GRID.pg, { objectName: 'pg', fontSize: 8, color: C.sub, align: 'right', margin: 0 }));
  if (grade) badge(s, W - M - 1.0, 0.36, grade, 1.0, condNo ? `条件${condNo}` : '構造評価');
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

// 目次トラッカー(表紙の次と各章の中扉)。current = 0..5、-1 は全章を白
function agenda(pres, current, page) {
  const s = pres.addSlide();
  s.background = { color: C.dark };
  s.addShape('rect', { x: 0, y: 0, w: W, h: H, fill: { color: C.dark }, line: { color: C.dark }, objectName: 'bg_agenda' });
  text(s, current < 0 ? '本日の内容' : '目次', { x: 0.9, y: 2.9, w: 3.2, h: 1.0, fontSize: 28, bold: true, color: C.white, objectName: 'bg_agenda_lbl' });
  CHAPTERS.forEach((ch, i) => {
    const y = 2.0 + i * 0.95;
    const on = current < 0 || i === current;
    s.addShape('ellipse', { x: 5.0, y, w: 0.52, h: 0.52, fill: { color: on ? C.primary : C.dark }, line: { color: C.white, width: 1 }, transparency: on ? 0 : 50, objectName: 'bg_agenda_n' + i });
    text(s, String(i + 1), { x: 5.0, y, w: 0.52, h: 0.52, fontSize: 14, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0, transparency: on ? 0 : 50, objectName: 'bg_agenda_nt' + i });
    text(s, ch, { x: 5.75, y: y + 0.02, w: 7.0, h: 0.5, fontSize: 18, bold: on, color: C.white, valign: 'middle', transparency: on ? 0 : 50, objectName: 'bg_agenda_ch' + i });
  });
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
  const s = pres.addSlide();
  s.background = { color: C.dark };
  s.addShape('rect', { x: 0, y: 0, w: W, h: H, fill: { color: C.dark }, line: { color: C.dark }, objectName: 'bg_divider' });
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
      runs.push({ text: it, options: { bullet: { indent: 12 }, breakLine: !last, paraSpaceAfter: gap } });
    }
  });
  s.addText(runs, { x, y, w, h, fontFace: FONT, fontSize, color, valign: 'top', margin: 0.04, isTextBox: true, objectName: name });
}

// 大型数値タイル(T9)。tiles = [{value, label, note, color}](最大4)
function kpiTiles(s, tiles, { x = M, y = 1.7, w = W - 2 * M, h = 1.55 } = {}) {
  const n = tiles.length, gap = 0.25, tw = (w - gap * (n - 1)) / n;
  tiles.forEach((t, i) => {
    const tx = x + i * (tw + gap);
    box(s, tx, y, tw, h, { fill: C.tint, line: C.tint, name: 'ovl_tile' + i });
    text(s, t.value, { x: tx + 0.1, y: y + 0.08, w: tw - 0.2, h: 0.78, fontSize: 32, bold: true, color: t.color || C.primary, align: 'center', valign: 'middle', margin: 0, objectName: 'tile_v' + i });
    text(s, t.label, { x: tx + 0.1, y: y + 0.88, w: tw - 0.2, h: 0.3, fontSize: 10.5, bold: true, color: C.dark, align: 'center', margin: 0, objectName: 'tile_l' + i });
    if (t.note) text(s, t.note, { x: tx + 0.1, y: y + 1.17, w: tw - 0.2, h: 0.33, fontSize: 8.5, color: C.sub, align: 'center', margin: 0, objectName: 'tile_n' + i });
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

module.exports = { pptxgen, C, GRADE, FONT, W, H, M, GRID, CHAPTERS, newDeck, text, contentSlide, badge, takeaway, box, arrow, table, agenda, cover, closing, chartStyle,
  paneHead, bullets, kpiTiles, chartPanel, structure, t15Side, twoPane, flow, matrix, T15 };
