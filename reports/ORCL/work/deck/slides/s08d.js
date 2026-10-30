// 会社のシナリオ(1/2): 筋書きの図。FY30 目標の札 → 筋書きの関係図(需要→資金→建設→収益化→成果)→ 稼働容量の時間軸
module.exports = function build(pres, L) {
  const { C, FONT } = L;
  const s = L.contentSlide(pres, {
    kicker: '経営陣の発言と目標を、需要 → 資金 → 建設 → 収益化 → 成果の順に並べた。赤は筋書きの進み方を決める制約。下は AI 容量の道筋と節目',
    source: 'report/ORCL_report.md §4-1・4-2(FAM 2025-10、決算説明会、DEF 14A)、Investor Day 2026-10-28(8-K Ex.99.1、CFO 資料 p.4・8・26)、需給エンジン第4.4版(容量の道筋)',
  });

  // ---------- 上段: 会社の FY30 目標(4 つの札)----------
  const goals = [
    ['売上 2,250 億ドル', 'FY30 目標・FY26〜30 の CAGR 35% 超'],
    ['OCI 1,660 億ドル', '売上に占める比率 38% → 74%'],
    ['EPS 21 ドル', '非GAAP・5 年 CAGR 28%'],
    ['AI 容量の粗利 30〜40%', '立ち上がり後(会社の言葉)'],
  ];
  goals.forEach(([v, note], i) => {
    s.addText([
      { text: v, options: { fontSize: 16, bold: true, color: C.primary, breakLine: true } },
      { text: note, options: { fontSize: 8.5, color: C.sub } },
    ], { shape: 'rect', x: 0.5 + i * (2.95 + 0.18), y: 1.66, w: 2.95, h: 0.78, fill: { color: C.tint }, line: { color: C.tint, width: 0.75 },
      fontFace: FONT, align: 'center', valign: 'middle', margin: 0.04, objectName: 'goal_' + i });
  });

  // ---------- 中段: 筋書きの関係図 ----------
  L.flowMap(s, {
    name: 's08d', x: 0.5, y: 2.6, w: 12.33, h: 2.75, cols: [1.85, 1.85, 1.85, 1.85, 1.85], rows: 2, legend: true, nodeH: 0.9,
    nodes: [
      { id: 'dem', c: 0, r: 0, kind: 'unit', label: '① 需要', sub: 'AI 研究所と企業の推論\n30 日で新規契約 650 億ドル' },
      { id: 'fin', c: 1, r: 0, kind: 'unit', label: '② 資金の外部化', sub: '前払い・BYOH・ベンダー金融\n各 約 350〜400 億ドル\n追加調達は 200 億ドルが上限', subSize: 8.5 },
      { id: 'bld', c: 2, r: 0, kind: 'unit', label: '③ 建設', sub: '総容量 FY26 約 3GW →\nFY28 末 約 10GW(7GW 追加)', subSize: 8.5 },
      { id: 'mon', c: 3, r: 0, kind: 'unit', label: '④ 収益化', sub: '粗利 30〜40%\n(立ち上がり後)\n更新は従来比 +20%' },
      { id: 'out', c: 4, r: 0, kind: 'key', label: '⑥ 成果', sub: 'FY30 売上 2,250 億ドル\n営業利益率 40%・EPS 21 ドル', subSize: 8 },
      { id: 'quote', c: 0, r: 1, kind: 'ok', label: '会社の言葉', sub: '「最終的に粗利 30〜40%」\n「前払いでも利益率は\n下がらない」\n「全量を +20% で更新・再販」', subSize: 8 },
      { id: 'cap', c: 1, r: 1, kind: 'risk', label: '資本と格付け', sub: 'BBB−、FY27 の純現金\ncapex 700 億ドル以下\nFY33: 7GW の更新期', subSize: 8 },
      { id: 'pow', c: 2, r: 1, kind: 'risk', label: '電力の解放', sub: 'ガス管の延期(2027-02)\n不可抗力通知の報道' },
      { id: 'oai', c: 3, r: 1, kind: 'risk', label: 'OpenAI の支払能力', sub: '受注残の約 45%' },
      { id: 'add', c: 4, r: 1, kind: 'unit', label: '⑤ 上積み', sub: 'Database@・AI Database\nSaaS のエージェント' },
    ],
    edges: [
      { from: 'dem', to: 'fin', label: '契約が\n資金を呼ぶ', kind: 'money', lw: 0.7 },
      { from: 'fin', to: 'bld', label: '建設', kind: 'money' },
      { from: 'bld', to: 'mon', label: '稼働', kind: 'goods' },
      { from: 'mon', to: 'out', label: '売上・利益', kind: 'money' },
      { from: 'mon', to: 'bld', label: '現金が次の\n建設へ', kind: 'money', lw: 0.7 },
      { from: 'add', to: 'out', label: '上積み', kind: 'goods' },
      { from: 'cap', to: 'fin', label: '上限', kind: 'risk' },
      { from: 'pow', to: 'bld', label: '律速', kind: 'risk' },
      { from: 'oai', to: 'mon', label: '集中', kind: 'risk' },
    ],
  });

  // ---------- 下段: AI 容量の道筋(横の時間軸。自作)----------
  // FY26〜FY30 は等間隔、FY30 と FY33 の間は途中を略した点線(FY33 は第 2 の山の年)
  const ax0 = 0.8, ax1 = 12.5, ay = 6.08;
  const tk = { FY26: 1.9, FY27: 3.9, FY28: 5.9, FY29: 7.9, FY30: 9.9, FY33: 11.9 };
  L.text(s, 'AI 容量(需給エンジン第4.4版)', { x: 0.5, y: 5.48, w: 2.2, h: 0.22, fontSize: 9, bold: true, color: C.dark, margin: 0, valign: 'middle', objectName: 'ovl_tl_head' });
  s.addShape('line', { x: ax0, y: ay, w: tk.FY30 - ax0, h: 0.001, line: { color: C.sub, width: 1.25 }, objectName: 'ovl_tl_axis' });
  s.addShape('line', { x: tk.FY30, y: ay, w: ax1 - tk.FY30, h: 0.001, line: { color: C.sub, width: 1.25, dashType: 'sysDash' }, objectName: 'ovl_tl_axis2' });
  const vals = { FY27: '4.7GW', FY28: '8.7GW', FY29: '9.0GW', FY30: '9.5GW' };
  Object.entries(tk).forEach(([fy, x]) => {
    const red = fy === 'FY33', col = red ? C.red : C.primary;
    s.addShape('ellipse', { x: x - 0.08, y: ay - 0.08, w: 0.16, h: 0.16, fill: { color: col }, line: { color: col }, objectName: 'ovl_tl_dot_' + fy });
    L.text(s, fy, { x: x - 0.4, y: ay + 0.12, w: 0.8, h: 0.2, fontSize: 8.5, bold: red, color: red ? C.red : C.sub, align: 'center', margin: 0, valign: 'middle', objectName: 'ovl_tl_tick_' + fy });
    if (vals[fy]) L.text(s, vals[fy], { x: x - 0.5, y: ay - 0.3, w: 1.0, h: 0.2, fontSize: 10, bold: true, color: C.dark, align: 'center', margin: 0, valign: 'bottom', objectName: 'ovl_tl_val_' + fy });
  });
  // 上の注記: 目盛の間の出来事(白抜きの印と細い点線で軸に結ぶ)
  const mid = (a, b) => (tk[a] + tk[b]) / 2;
  const up = [
    { x: mid('FY26', 'FY27'), w: 1.7, t: 'Q1 FY27: 850MW 納入' },
    { x: mid('FY27', 'FY28'), w: 2.2, t: '2027: OpenAI の大型契約が開始\nNM のガス管(2027-02)' },
  ];
  up.forEach((n, i) => {
    L.text(s, n.t, { x: n.x - n.w / 2, y: 5.52, w: n.w, h: 0.34, fontSize: 8.5, color: C.text, align: 'center', margin: 0, valign: 'bottom', objectName: 'ovl_tl_note' + i });
    s.addShape('line', { x: n.x, y: 5.88, w: 0.001, h: ay - 0.06 - 5.88, line: { color: C.sub, width: 0.75, dashType: 'sysDot' }, objectName: 'ovl_tl_lead' + i });
    s.addShape('ellipse', { x: n.x - 0.06, y: ay - 0.06, w: 0.12, h: 0.12, fill: { color: C.white }, line: { color: C.primary, width: 1.25 }, objectName: 'ovl_tl_mark' + i });
  });
  // 下の注記: 目盛の年の節目(FY33 は赤の制約)
  const dn = [
    { x: tk.FY28, w: 2.4, t: 'FCF 黒字化(会社: FY28 下期)', col: C.text },
    { x: tk.FY29, w: 1.7, t: 'FCF 300 億ドル以上', col: C.text },
    { x: tk.FY30, w: 1.5, t: '会社目標の年', col: C.text },
    { x: tk.FY33 - 0.25, w: 2.5, t: '第 2 の山: 7GW の更新期\n(FCF −562 億ドル)', col: C.red, bold: true },
  ];
  dn.forEach((n, i) => {
    L.text(s, n.t, { x: n.x - n.w / 2, y: ay + 0.36, w: n.w, h: 0.34, fontSize: 8.5, bold: !!n.bold, color: n.col, align: 'center', margin: 0, valign: 'top', objectName: 'ovl_tl_dn' + i });
  });
  return s;
};
