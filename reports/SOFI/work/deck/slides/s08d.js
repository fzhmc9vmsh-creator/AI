// 会社のシナリオ(1/2): 筋書きの図。目標の札 → 筋書きの関係図(会員 → 調達 → 貸出・組成 → 収益化 → 成果)→ 会員数の時間軸
module.exports = function build(pres, L) {
  const { C, FONT } = L;
  const s = L.contentSlide(pres, {
    kicker: '経営陣の発言と目標を、会員の獲得 → 調達 → 貸出・組成 → 収益化 → 成果の順に並べた。赤は筋書きの進み方を決める制約。下は会員数の道筋と節目',
    source: '会社開示(Q4 2025・Q3 2026 決算の 8-K・説明会の要約、2025 年の株主への手紙)、research_r5/Q3_datasheet.md、research/R3b_management.md、calc/out/growth_v4.json(会員数の道筋と EPS の経路は事業エンジン)',
  });

  // ---------- 上段: 会社の目標(4 つの札)----------
  const goals = [
    ['収益 CAGR 30% 以上', '2025→2028 年(再確認は未取得)'],
    ['2027 年 EPS 0.90', '会社の見通し。収益 64 億ドル'],
    ['会員 +30% 以上/年', '2026 年の目標(Q3 は +36%)'],
    ['ROTCE 20〜30%', '長期の目標(時期は示していない)'],
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
    name: 's08d', x: 0.5, y: 2.6, w: 12.33, h: 2.75, cols: [1.85, 1.85, 1.85, 1.85, 1.85], rows: 2, legend: true,
    nodes: [
      { id: 'dem', c: 0, r: 0, kind: 'unit', label: '① 会員の獲得', sub: 'ブランドと販促\n四半期 120 万人\n販促費 4.4 億ドル' },
      { id: 'fund', c: 1, r: 0, kind: 'unit', label: '② 預金で調達', sub: '給与振込の預金\n513 億ドル(+58 億)\n2025 年に 33 億ドル増資' },
      { id: 'lend', c: 2, r: 0, kind: 'unit', label: '③ 貸出と組成', sub: '組成 169 億ドル/四半期\n個人ローンの 71% は保有' },
      { id: 'mon', c: 3, r: 0, kind: 'unit', label: '④ 収益化', sub: '利ざや NIM 6.14%\nLPB 組成 36 億ドル\nクロスバイ 51%' },
      { id: 'out', c: 4, r: 0, kind: 'key', label: '⑥ 成果', sub: '2028 年 EPS 1.02〜1.12 ドル\nROTCE 20〜30%(長期)' },
      { id: 'quote', c: 0, r: 1, kind: 'ok', label: '会社の言葉', sub: '「会員数・会員当たり製品数・\n製品当たり収益の 3 つで伸びる」\n「利益の上積みより投資を選ぶ」', subSize: 8, w: 2.2, dx: 0.175 },
      { id: 'rate', c: 1, r: 1, kind: 'risk', label: '金利', sub: '10 年債 約 5.1%(10/15)\n公正価値と預金コスト' },
      { id: 'cap', c: 2, r: 1, kind: 'risk', label: '自己資本', sub: '総自己資本比率 17.0%\n運用下限は low-to-mid teens' },
      { id: 'credit', c: 3, r: 1, kind: 'risk', label: '信用サイクル', sub: 'all-in 貸倒率 約 3.4%\n失業率 4.2%' },
      { id: 'add', c: 4, r: 1, kind: 'unit', label: '⑤ 上積み', sub: 'Plus・SoFiUSD・暗号資産\n中小企業・法人銀行' },
    ],
    edges: [
      { from: 'dem', to: 'fund', label: '会員が\n預金を運ぶ', kind: 'money', lw: 0.7 },
      { from: 'fund', to: 'lend', label: '安い資金', kind: 'money' },
      { from: 'lend', to: 'mon', label: '利息・\n手数料', kind: 'money', lw: 0.7 },
      { from: 'mon', to: 'out', label: '利益', kind: 'money' },
      { from: 'mon', to: 'lend', label: '利益が次の\n貸出へ', kind: 'money', lw: 0.7 },
      { from: 'add', to: 'out', label: '上積み', kind: 'goods' },
      { from: 'cap', to: 'lend', label: '上限', kind: 'risk' },
      { from: 'credit', to: 'mon', label: '貸倒', kind: 'risk' },
      { from: 'rate', to: 'fund', label: '評価・コスト', kind: 'risk' },
    ],
  });

  // ---------- 下段: 会員数の道筋(横の時間軸。自作)----------
  const ax0 = 0.8, ax1 = 12.5, ay = 6.13;
  const tk = { 2025: 3.0, 2026: 6.0, 2027: 9.0, 2028: 12.0 };
  L.text(s, '会員数(年末)\n2026 年以降は事業エンジン', { x: 0.5, y: 5.5, w: 1.95, h: 0.4, fontSize: 9, bold: true, color: C.dark, margin: 0, valign: 'top', objectName: 'ovl_tl_head' });
  s.addShape('line', { x: ax0, y: ay, w: ax1 - ax0, h: 0.001, line: { color: C.sub, width: 1.25 }, objectName: 'ovl_tl_axis' });
  const vals = { 2025: '1,370 万', 2026: '1,830 万', 2027: '2,290 万', 2028: '2,730 万' };
  Object.entries(tk).forEach(([yr, x]) => {
    s.addShape('ellipse', { x: x - 0.08, y: ay - 0.08, w: 0.16, h: 0.16, fill: { color: C.primary }, line: { color: C.primary }, objectName: 'ovl_tl_dot_' + yr });
    L.text(s, yr, { x: x - 0.4, y: ay + 0.12, w: 0.8, h: 0.2, fontSize: 8.5, color: C.sub, align: 'center', margin: 0, valign: 'middle', objectName: 'ovl_tl_tick_' + yr });
    if (vals[yr]) L.text(s, vals[yr], { x: x - 0.5, y: ay - 0.3, w: 1.0, h: 0.2, fontSize: 10, bold: true, color: C.dark, align: 'center', margin: 0, valign: 'bottom', objectName: 'ovl_tl_val_' + yr });
  });
  // 節目の注記: 目盛の間(白抜きの印と細い点線で軸に結ぶ)と、2028 の目盛の上
  const mid = (a, b) => (tk[a] + tk[b]) / 2;
  const notes = [
    { x: mid(2025, 2026), w: 2.4, t: '2026-04: Plus を有料で再開\n2026-07: Grad PLUS の新規廃止', marker: true },
    { x: mid(2026, 2027), w: 2.2, t: '2027 年: 自己資本比率が\n運用下限に近づく(エンジン)', marker: true },
    { x: tk[2028], w: 1.4, t: '会社目標の年' },
  ];
  notes.forEach((n, i) => {
    L.text(s, n.t, { x: n.x - n.w / 2, y: 5.52, w: n.w, h: 0.34, fontSize: 8.5, color: C.text, align: 'center', margin: 0, valign: 'bottom', objectName: 'ovl_tl_note' + i });
    if (n.marker) {
      s.addShape('line', { x: n.x, y: 5.88, w: 0.001, h: ay - 0.06 - 5.88, line: { color: C.sub, width: 0.75, dashType: 'sysDot' }, objectName: 'ovl_tl_lead' + i });
      s.addShape('ellipse', { x: n.x - 0.06, y: ay - 0.06, w: 0.12, h: 0.12, fill: { color: C.white }, line: { color: C.primary, width: 1.25 }, objectName: 'ovl_tl_mark' + i });
    }
  });
  return s;
};
