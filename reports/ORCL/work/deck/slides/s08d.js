// 会社のシナリオ(1/2): 筋書きの図。需要の 3 層(学習・推論・アプリ)→ 資金と建設 → 収益化(AI 容量・企業向け OCI・DB・SaaS)→ 成果。右: 仕組み ①〜⑥ と上がる/下がる条件。下: AI 容量の道筋と節目
module.exports = function build(pres, L) {
  const { C, FONT } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 需要の 3 層(学習・推論・アプリ)が、資金と建設を経て AI 容量・DB・OCI・SaaS の売上になる筋書き。①〜⑥ は右と対応。赤は制約。下は AI 容量の道筋と節目',
    source: 'report/ORCL_report.md §4-1・4-2、Investor Day 2026-10-28(8-K Ex.99.1、CFO 資料 p.4・8・26)、需給エンジン第4.5版(calc/out/m10_*.json)',
  });

  // ---------- 上段: 会社の FY30 目標(4 つの札)----------
  const goals = [
    ['売上 2,250 億ドル', 'FY30 目標・CAGR 35% 超'],
    ['OCI 1,660 億ドル', '売上に占める比率 38% → 74%'],
    ['EPS 21 ドル', '非GAAP・5 年 CAGR 28%'],
    ['AI 容量の粗利 30〜40%', '立ち上がり後(会社の言葉)'],
  ];
  goals.forEach(([v, note], i) => {
    s.addText([
      { text: v, options: { fontSize: 11.5, bold: true, color: C.primary, breakLine: true } },
      { text: note, options: { fontSize: 8, color: C.sub } },
    ], { shape: 'rect', x: 0.5 + i * (2.0 + 0.15), y: 1.62, w: 2.0, h: 0.56, fill: { color: C.tint }, line: { color: C.tint, width: 0.75 },
      fontFace: FONT, align: 'center', valign: 'middle', margin: 0.03, objectName: 'goal_' + i });
  });

  // ---------- 左: 筋書きの関係図(4 レーン × 3 行)----------
  L.flowMap(s, {
    name: 's08d', x: 0.5, y: 2.3, w: 8.45, h: 3.37, cols: [1.5, 1.6, 1.75, 1.45], rows: 3, nodeH: 0.64,
    lanes: [
      { label: '需要の 3 層', c0: 0, c1: 0 },
      { label: 'Oracle の資金と建設', c0: 1, c1: 1, self: true },
      { label: 'Oracle の収益化', c0: 2, c1: 2, self: true },
      { label: '成果と制約', c0: 3, c1: 3 },
    ],
    nodes: [
      { id: 'learn', c: 0, r: 0, label: '学習', sub: 'GW 級の拠点・大型契約\nコストプラス', subSize: 8 },
      { id: 'infer', c: 0, r: 1, label: '推論', sub: '推論は AI 計算の約 2/3\n企業データの近く', subSize: 8 },
      { id: 'app', c: 0, r: 2, label: 'アプリ・ERP', sub: 'ERP の約半分がオンプレ\n移行で売上 3〜4 倍', subSize: 8 },
      { id: 'fin', c: 1, r: 0, kind: 'unit', label: '資金の外部化', sub: '前払い・BYOH・ベンダー\n各 約 350〜400 億ドル', subSize: 8 },
      { id: 'bld', c: 1, r: 1, kind: 'unit', label: '建設', sub: '総容量 FY26 約 3GW →\nFY28 末 約 10GW', subSize: 8 },
      { id: 'ai', c: 2, r: 1, kind: 'unit', label: 'AI 容量', sub: '粗利率 35%(立ち上がり後)\n更新は従来比 +20%', subSize: 8 },
      { id: 'db', c: 2, r: 2, kind: 'unit', label: '企業向け OCI・DB', sub: '粗利率が非常に高い\nDB の顧客基盤・Database@', subSize: 8 },
      { id: 'saas', c: 2, r: 0, kind: 'unit', label: 'SaaS', sub: '二桁成長\nFusion・NetSuite', subSize: 8 },
      { id: 'out', c: 3, r: 1, kind: 'key', label: '成果(FY30)', sub: '売上 2,250 億ドル\nEPS 21 ドル(会社)', subSize: 8 },
      { id: 'oai', c: 3, r: 2, kind: 'risk', label: 'OpenAI の支払能力', sub: '受注残の約 45%\n集中が最大のリスク', subSize: 8 },
    ],
    edges: [
      { from: 'learn', to: 'fin', label: '呼び水', kind: 'money', n: 1 },
      { from: 'fin', to: 'bld', label: '建設', kind: 'money', n: 2 },
      { from: 'bld', to: 'ai', label: '稼働', kind: 'goods', n: 3 },
      { from: 'ai', to: 'out', kind: 'money', n: 6 },
      { from: 'saas', to: 'out', kind: 'goods', mx: 7.0 },
      { from: 'db', to: 'out', kind: 'goods', mx: 7.3 },
      { from: 'infer', to: 'db', label: 'データの重力', kind: 'goods', n: 4, mx: 2.36, lpos: 'v', ldy: 0.12 },
      { from: 'app', to: 'db', kind: 'goods' },
      { from: 'app', to: 'saas', label: 'AI Units', kind: 'money', n: 5, mx: 4.97, ldx: 0.55 },
      { from: 'oai', to: 'ai', kind: 'risk', mx: 7.42 },
    ],
  });

  // ---------- 右: 仕組み ①〜⑥ と上がる/下がる条件 ----------
  L.mechPanel(s, {
    bottom: 5.6, x: 9.25,
    mech: [
      '学習の大型契約が、外部資金(前払い・GPU 持込・ベンダー金融)を呼ぶ',
      '資金は建設へ。追加調達は 200 億ドルが上限で、BBB− の維持が条件',
      '稼働した容量が AI 容量の売上になる。電力の遅れは時期の問題',
      '推論は企業データの近くで DB・OCI に乗る。\n拠点は 50〜200MW に分散',
      'アプリ(ERP・Fusion)は AI Units で従量課金される',
      '3 本の売上が FY30 の成果に。\n会社の目標は売上 2,250 億ドル',
    ],
    reason: '学習が資金と建設を呼び、推論とアプリは DB・OCI を通って収益になる。争点は OpenAI への集中と、契約後の再契約の単価',
    up: 'FY28 下期に FCF が黒字化し、再契約が続く',
    down: 'FY29 FCF が 300 億ドル未満、格付け BB+ へ',
    head: '仕組み(図の ①〜⑥ と対応)',
  });

  // ---------- 下段: AI 容量の道筋(横の時間軸。自作)----------
  // FY26〜FY30 は等間隔、FY30 と FY36〜37 の間は途中を略した点線
  const ax0 = 0.8, ax1 = 12.5, ay = 6.3;
  const tk = { FY26: 1.9, FY27: 3.9, FY28: 5.9, FY29: 7.9, FY30: 9.9, FY37: 11.6 };
  L.text(s, 'AI 容量の道筋(需給エンジン第4.5版、GW)', { x: 0.5, y: 5.74, w: 3.4, h: 0.2, fontSize: 9, bold: true, color: C.dark, margin: 0, valign: 'middle', objectName: 'ovl_tl_head' });
  s.addShape('line', { x: ax0, y: ay, w: tk.FY30 - ax0, h: 0.001, line: { color: C.sub, width: 1.25 }, objectName: 'ovl_tl_axis' });
  s.addShape('line', { x: tk.FY30, y: ay, w: ax1 - tk.FY30, h: 0.001, line: { color: C.sub, width: 1.25, dashType: 'sysDash' }, objectName: 'ovl_tl_axis2' });
  const vals = { FY27: '4.7GW', FY28: '8.2GW', FY29: '9.5GW', FY30: '10.5GW' };
  Object.entries(tk).forEach(([fy, x]) => {
    const red = fy === 'FY37', col = red ? C.red : C.primary;
    s.addShape('ellipse', { x: x - 0.08, y: ay - 0.08, w: 0.16, h: 0.16, fill: { color: col }, line: { color: col }, objectName: 'ovl_tl_dot_' + fy });
    L.text(s, red ? 'FY36〜37' : fy, { x: x - 0.45, y: ay + 0.1, w: 0.9, h: 0.18, fontSize: 8.5, bold: red, color: red ? C.red : C.sub, align: 'center', margin: 0, valign: 'middle', objectName: 'ovl_tl_tick_' + fy });
    if (vals[fy]) L.text(s, vals[fy], { x: x - 0.5, y: ay - 0.3, w: 1.0, h: 0.2, fontSize: 10, bold: true, color: C.dark, align: 'center', margin: 0, valign: 'bottom', objectName: 'ovl_tl_val_' + fy });
  });
  // 下の注記: 目盛の年の節目(FY36〜37 は赤の制約)
  const dn = [
    { x: tk.FY28, w: 2.4, t: 'FCF 黒字化(会社: FY28 下期)', col: C.text },
    { x: tk.FY29, w: 2.0, t: 'FCF 300 億ドル以上', col: C.text },
    { x: tk.FY30, w: 1.5, t: '会社目標の年', col: C.text },
    { x: tk.FY37, w: 2.6, t: '更新の山(再契約しだい)', col: C.red, bold: true },
  ];
  dn.forEach((n, i) => {
    L.text(s, n.t, { x: n.x - n.w / 2, y: ay + 0.3, w: n.w, h: 0.22, fontSize: 8.5, bold: !!n.bold, color: n.col, align: 'center', margin: 0, valign: 'middle', objectName: 'ovl_tl_dn' + i });
  });
  return s;
};
