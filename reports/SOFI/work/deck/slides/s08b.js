// 事業理解(2/3): 事業どうしの関係図(上の帯 = 会員を中心にした放射、下の帯 = お金の流れ)
// flowMap は使わず L.box・L.arrow・L.text で描く。線の交差・箱の貫通・文字の重なりは、このファイルの中で検査して L.warnings に積む。
module.exports = function build(pres, L) {
  const C = L.C;
  const s = L.contentSlide(pres, {
    kicker: '上: 会員が 1 つのアプリで受け取るもの(体験の束)。下: お金の流れ(預金 → 貸出 → 売却)。①〜⑥ は右と対応。数値は Q3 2026(有料会員のみ Q2)',
    source: '会社開示(Q3 2026 決算の 8-K・説明会の要約)、research_r5/Q3_datasheet.md、research_r4/R16_flywheel_quality_holding.md(構造)。残高は公正価値の額',
  });

  const boxes = {}, segs = [], labs = [];
  const warn = (m) => L.warnings.push('[s08b] ' + m);

  // ---- 部品 -------------------------------------------------------------------------
  // 箱: kind = key(濃緑)/ unit(白・緑枠)/ ext(白・灰枠)/ risk(白・赤枠)。名前 10pt(hub は 12pt)+ 補足 9pt
  function node(id, x, y, w, h, kind, label, sub, o = {}) {
    boxes[id] = { x, y, w, h };
    const fill = { key: C.dark }[kind] || C.white;
    const line = { key: C.dark, unit: C.primary, risk: C.red }[kind] || C.sub;
    const lw = { unit: 1.5, risk: 1.5 }[kind] || 0.75;
    const dark = kind === 'key';
    L.box(s, x, y, w, h, { round: true, fill, line, lw, name: 'ovl_s08b_n_' + id });
    const lsz = o.lsz || 10, ssz = o.ssz || 9;
    const lh = (o.lh !== undefined) ? o.lh : 0.06 + 0.165 * (lsz / 10);
    L.text(s, label, { x: x + 0.04, y: y + 0.03, w: w - 0.08, h: lh, fontSize: lsz, bold: true, color: kind === 'risk' ? C.red : (dark ? C.white : C.dark), align: 'center', valign: 'middle', margin: 0, objectName: 'ovl_s08b_nt_' + id });
    if (sub) L.text(s, sub, { x: x + 0.05, y: y + 0.03 + lh, w: w - 0.1, h: h - lh - 0.06, fontSize: ssz, color: dark ? C.white : C.text, align: 'center', valign: 'top', margin: 0, objectName: 'ovl_s08b_ns_' + id });
  }
  // 線(矢印あり/なし)。水平・垂直・斜めのどれでも可
  function line(id, x1, y1, x2, y2, st, head) {
    segs.push({ id, x1, y1, x2, y2 });
    if (head) { L.arrow(s, x1, y1, x2, y2, st); return; }
    s.addShape('line', { x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.abs(x2 - x1) || 0.001, h: Math.abs(y2 - y1) || 0.001, flipH: x2 < x1, flipV: y2 < y1,
      line: { color: st.color, width: st.width, dashType: st.dash || 'solid' }, objectName: 'ovl_s08b_l_' + id });
  }
  // 線の上の丸数字(説明は右の「仕組み」)
  function num(id, n, cx, cy, col) {
    const d = 0.26, x = cx - d / 2, y = cy - d / 2;
    s.addShape('ellipse', { x, y, w: d, h: d, fill: { color: col }, line: { color: C.white, width: 1 }, objectName: 'ovl_s08b_num' + n + id });
    L.text(s, String(n), { x, y, w: d, h: d, fontSize: 9, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0, objectName: 'ovl_s08b_numt' + n + id });
    labs.push({ name: '丸数字' + n, x, y, w: d, h: d, own: id });
  }
  // 矢印のラベル(白地)。num があれば先頭に丸数字(太字)
  function label(id, n, str, x, y, w, h, col) {
    const runs = [];
    const parts = String(str).split('\n');
    parts.forEach((p, j) => {
      if (j === 0 && n) runs.push({ text: ['', '①', '②', '③', '④', '⑤', '⑥'][n] + ' ', options: { bold: true } });
      runs.push({ text: p, options: j < parts.length - 1 ? { breakLine: true } : {} });
    });
    s.addText(runs, { x, y, w, h, fontFace: L.FONT, fontSize: 9, color: col, align: 'center', valign: 'middle', margin: 0.02, fill: { color: C.white }, isTextBox: true, objectName: 'ovl_s08b_lab_' + id });
    labs.push({ name: str.replace('\n', ''), x, y, w, h, own: id });
  }
  // 帯の見出し: 細い罫線の上に白地の見出しを中央で載せる
  function bandHead(id, str, y, w) {
    s.addShape('line', { x: 0.5, y, w: 8.35, h: 0.001, line: { color: C.rule, width: 0.75 }, objectName: 'ovl_s08b_rule_' + id });
    L.text(s, str, { x: 4.675 - w / 2, y: y - 0.11, w, h: 0.22, fontSize: 9.5, bold: true, color: C.dark, align: 'center', valign: 'middle', margin: 0, fill: { color: C.white }, objectName: 'ovl_s08b_head_' + id });
  }

  // ---- 上の帯: 会員を中心にした放射 ------------------------------------------------------
  bandHead('top', '体験の束(会員が受け取るもの)', 1.72, 3.0);
  const spoke = { color: C.primary, width: 1.25 };

  // 中央のハブ
  const hub = { x: 3.55, y: 2.95, w: 2.25, h: 0.95 };
  node('hub', hub.x, hub.y, hub.w, hub.h, 'key', '会員 1,710 万人', '前年比 +36%\n1 会員 1.56 製品\nクロスバイ 51%', { lsz: 12, ssz: 9, lh: 0.28 });
  // 周りの 6 箱: 左 2(体験・主口座)、上 2(ローン・保険)、右 2(投資・カード)
  node('exp', 0.5, 1.9, 2.2, 0.6, 'unit', '毎日の体験', '給与を最大 2 日早く\nATM 5.5 万台・補償 300 万ドル');
  node('money', 0.5, 3.36, 2.2, 0.64, 'unit', 'SoFi Money(主口座)', '預金 513 億ドル\n給与振込の会員が 9 割超');
  node('loan', 3.05, 1.9, 1.55, 0.6, 'unit', 'ローン', '個人・学生・住宅\n会員割引 各 0.25%');
  node('ins', 4.75, 1.9, 1.55, 0.6, 'ext', '保険(提携)', 'アプリから加入');
  node('inv', 6.65, 1.9, 2.2, 0.6, 'unit', '投資・暗号資産', 'Invest・暗号資産 25 銘柄超');
  node('card', 6.65, 3.36, 2.2, 0.64, 'unit', 'カード・Plus', '交換手数料 +77%\nPlus は 2026-04 に有料化');

  // 中央 → 各箱(細い実線。箱は線のあとに描くので端は箱で隠れる。ここでは線を先に積み、箱の上に出ないよう端点を縁に置く)
  line('hub-money', hub.x, 3.68, 2.7, 3.68, spoke);
  line('hub-exp', hub.x, 3.2, 2.7, 2.35, spoke);
  line('hub-loan', 3.825, hub.y, 3.825, 2.5, spoke);
  line('hub-ins', 5.525, hub.y, 5.525, 2.5, spoke);
  line('hub-inv', hub.x + hub.w, 3.2, 6.65, 2.35, spoke);
  line('hub-card', hub.x + hub.w, 3.68, 6.65, 3.68, spoke);
  num('hub-money', 1, 3.125, 3.68, C.primary);
  num('hub-loan', 2, 3.825, 2.725, C.primary);
  num('hub-card', 3, 6.225, 3.68, C.primary);
  num('hub-inv', 3, 6.225, 2.775, C.primary);

  // ---- 下の帯: お金の流れ(左 → 右) ------------------------------------------------------
  bandHead('bot', 'お金の流れ', 4.15, 1.3);
  const RY = 4.52, RH = 0.8, AY = RY + RH / 2;           // 行の上端・高さ・矢印の高さ
  node('dep', 0.5, RY, 1.05, RH, 'unit', '預金', '513 億ドル\n前期比 +58 億');
  node('bs', 2.9, RY, 1.25, RH, 'key', 'B/S 貸出', 'NIM 6.14%\n個人 321 億ドル\n学生 185 億ドル');
  node('lpb', 5.35, RY, 1.25, RH, 'unit', 'LPB・売却', '四半期 36 億ドル\n手数料 4.3%');
  node('buy', 7.4, RY, 1.45, RH, 'ext', 'ローンの買い手', 'Blue Owl・Fortress\n契約 100 億ドル超');
  node('cap', 2.45, 5.67, 2.0, 0.63, 'risk', '自己資本', '比率 17.0%\n下限まで 17 億ドル');

  const flow = { color: C.dark, width: 1.75 };
  line('dep-bs', 1.55, AY, 2.9, AY, flow, true);
  line('bs-lpb', 4.15, AY, 5.35, AY, flow, true);
  line('lpb-buy', 6.6, AY, 7.4, AY, flow, true);
  label('dep-bs', 4, '倉庫ラインより\n1.45pt 安い', 1.58, AY - 0.43, 1.29, 0.4, C.dark);
  label('bs-lpb', 5, '資本で\n抱えきれない分', 4.18, AY - 0.43, 1.14, 0.4, C.dark);
  label('lpb-buy', 0, '額面 +\n手数料', 6.63, AY - 0.43, 0.74, 0.4, C.dark);
  // 貸出 → 自己資本(点線: 資本を使う)
  line('bs-cap', 3.525, RY + RH, 3.525, 5.67, { color: C.red, width: 1.25, dash: 'dash' }, true);
  label('bs-cap', 6, '資本を使う', 3.6, 5.41, 1.0, 0.21, C.red);
  // 帯をまたぐ線は 1 本だけ: SoFi Money → 預金
  line('money-dep', 1.05, 4.0, 1.05, RY, flow, true);
  label('money-dep', 0, '主口座の預金', 1.12, 4.22, 0.95, 0.2, C.dark);

  // 凡例(右下の空き)
  s.addShape('line', { x: 5.2, y: 6.1, w: 0.4, h: 0.001, line: { color: C.dark, width: 1.75, endArrowType: 'triangle' }, objectName: 'ovl_s08b_leg0' });
  L.text(s, 'お金・貸出の流れ', { x: 5.66, y: 5.99, w: 1.3, h: 0.22, fontSize: 9, color: C.sub, margin: 0, valign: 'middle', objectName: 'ovl_s08b_legt0' });
  s.addShape('line', { x: 7.0, y: 6.1, w: 0.4, h: 0.001, line: { color: C.red, width: 1.25, dashType: 'dash', endArrowType: 'triangle' }, objectName: 'ovl_s08b_leg1' });
  L.text(s, '資本を使う', { x: 7.46, y: 5.99, w: 1.0, h: 0.22, fontSize: 9, color: C.sub, margin: 0, valign: 'middle', objectName: 'ovl_s08b_legt1' });

  // ---- 検査: 線が箱を貫く / 線どうしが交差 / 文字どうしが重なる ------------------------------------
  const R = Object.entries(boxes).map(([id, r]) => Object.assign({ id }, r));
  const touch = (sg, r) => {      // 線分と矩形(内側に 0.03 縮める)の交差。端点が縁にある線は縁の外側なので数えない
    const x0 = r.x + 0.03, x1 = r.x + r.w - 0.03, y0 = r.y + 0.03, y1 = r.y + r.h - 0.03;
    const inside = (x, y) => x > x0 && x < x1 && y > y0 && y < y1;
    if (inside(sg.x1, sg.y1) || inside(sg.x2, sg.y2)) return true;
    const pts = [[x0, y0, x1, y0], [x1, y0, x1, y1], [x1, y1, x0, y1], [x0, y1, x0, y0]];
    return pts.some(([a, b, c, d]) => cross(sg.x1, sg.y1, sg.x2, sg.y2, a, b, c, d));
  };
  function cross(ax, ay, bx, by, cx, cy, dx, dy) {
    const o = (px, py, qx, qy, rx, ry) => (qx - px) * (ry - py) - (qy - py) * (rx - px);
    const d1 = o(ax, ay, bx, by, cx, cy), d2 = o(ax, ay, bx, by, dx, dy), d3 = o(cx, cy, dx, dy, ax, ay), d4 = o(cx, cy, dx, dy, bx, by);
    return d1 * d2 < -1e-9 && d3 * d4 < -1e-9;
  }
  segs.forEach(sg => {
    const [from, to] = sg.id.split('-');
    R.forEach(r => { if (r.id !== from && r.id !== to && touch(sg, r)) warn(`線 ${sg.id} が箱「${r.id}」を貫く`); });
  });
  segs.forEach((a, i) => segs.slice(i + 1).forEach(b => { if (cross(a.x1, a.y1, a.x2, a.y2, b.x1, b.y1, b.x2, b.y2)) warn(`線 ${a.id} と ${b.id} が交差`); }));
  const ov = (p, q) => Math.min(p.x + p.w, q.x + q.w) - Math.max(p.x, q.x) > 0.015 && Math.min(p.y + p.h, q.y + q.h) - Math.max(p.y, q.y) > 0.015;
  labs.forEach((l, i) => {
    R.forEach(r => { if (ov(l, r)) warn(`ラベル「${l.name}」が箱「${r.id}」に重なる`); });
    labs.slice(i + 1).forEach(m => { if (ov(l, m)) warn(`ラベル「${l.name}」と「${m.name}」が重なる`); });
    segs.forEach(sg => { if (sg.id !== l.own) {
      const lx0 = Math.min(sg.x1, sg.x2), lx1 = Math.max(sg.x1, sg.x2), ly0 = Math.min(sg.y1, sg.y2), ly1 = Math.max(sg.y1, sg.y2);
      const hit = (Math.abs(sg.y1 - sg.y2) < 0.005 && sg.y1 > l.y && sg.y1 < l.y + l.h && lx1 > l.x && lx0 < l.x + l.w) ||
                  (Math.abs(sg.x1 - sg.x2) < 0.005 && sg.x1 > l.x && sg.x1 < l.x + l.w && ly1 > l.y && ly0 < l.y + l.h);
      if (hit) warn(`ラベル「${l.name}」が線 ${sg.id} を隠す`);
    } });
  });

  // ---- 右パネル ----------------------------------------------------------------------
  L.mechPanel(s, {
    bottom: 6.32,
    mech: [
      '会員は 1 つのアプリで預金・ローン・\n投資・カード・保険を使う。\n1 会員 1.56 製品、新製品の 51% は既存会員',
      '給与振込が主口座を作る。\n給与の早期受け取り・ATM・預金の補償・\nローンの会員割引が乗り換えを難しくする',
      '製品を重ねるほど獲得費は下がる。\n製品当たり 202 ドルは\n会員当たり 370 ドルの半分強',
      '主口座の預金は倉庫ラインより\n1.45pt 安く、年 7.45 億ドルの節約',
      '資本で抱えきれないローンは LPB で\n手数料 4.3% を取って買い手へ渡す',
      'ただし貸出は自己資本を使う。\n比率 17.0%、下限 14% まで 17 億ドル',
    ],
    reason: '会員の束が獲得費と資金コストを下げ、\n預金が貸出を支える。律速は自己資本',
    up: 'クロスバイ 50% 超と預金の伸びが続けば、\n束の価値が上がる',
    down: '会員当たり販促費の上昇が続き、\n自己資本が下限に近づけば伸びが止まる',
  });
  return s;
};
