// 条件12(評価 B): 収益の性格(3 列 + 外部 1 列の配置)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 収益の源 → SoFi の収益の種類 → ストックとフロー → 続く条件。①〜④ は右と対応。金額は Q3 2026(百万ドル)。継続手数料と売却益は未開示',
    source: '会社開示(Q3 2026 決算、損益計算書)、research_r5/Q3_datasheet.md、research_r2/R5_credit_fv.md(期前返済率)',
    grade: 'B', condNo: 12,
  });
  L.flowMap(s, {
    name: 's28', h: 5.0, cols: [1.35, 1.45, 1.4, 1.3], rows: 4, nodeH: 0.8,
    lanes: [{ label: '収益の源', c0: 0, c1: 0 }, { label: 'SoFi の収益', c0: 1, c1: 2, self: true }, { label: '続く条件', c0: 3, c1: 3 }],
    groups: [{ label: '収益の種類', c0: 1, c1: 1, r0: 0, r1: 3 }, { label: '性格', c0: 2, c1: 2, r0: 0, r1: 3 }],
    nodes: [
      { id: 'loans', c: 0, r: 0, label: 'B/S のローン', sub: '個人 261・学生\n161 億ドル(Q2)' },
      { id: 'acct', c: 0, r: 1, label: '会員の口座', sub: '預金 513 億ドル\nInvest 390 万(Q2)' },
      { id: 'orig', c: 0, r: 2, label: '新しい組成', sub: '126 億ドル/四半期' },
      { id: 'b2b', c: 0, r: 3, label: 'Galileo の顧客', sub: '口座 1.40 億' },
      { id: 'nii', c: 1, r: 0, kind: 'key', label: '純金利収益', sub: '929.5(収益の 67%)' },
      { id: 'fee', c: 1, r: 1, kind: 'unit', label: '継続手数料', sub: '未開示(Q2 86.7)\nインターチェンジ・Plus', subSize: 8 },
      { id: 'flow', c: 1, r: 2, kind: 'unit', label: '売却益・LPB', sub: '売却益は未開示\nLPB 153.4(11%)' },
      { id: 'tp', c: 1, r: 3, kind: 'unit', label: 'Tech Platform', sub: '87.4(6%)' },
      { id: 'stock', c: 2, r: 0, rs: 2, h: 1.85, kind: 'self', label: 'ストック型 約 76%', sub: '残高・口座に課金' },
      { id: 'flowk', c: 2, r: 2, kind: 'risk', label: 'フロー型 約 24%', sub: '組成のたびに発生' },
      { id: 'runoff', c: 2, r: 3, kind: 'risk', label: '残高の目減り', sub: '期前返済 年 25.8%\n個人ローンは 2〜3 年' },
      { id: 'cond1', c: 3, r: 1, kind: 'ok', label: '会員と預金が\n増える', sub: '会員 +36%' },
      { id: 'cond2', c: 3, r: 2, kind: 'risk', label: '組成を続ける', sub: '組成が止まれば\n残高が減る' },
    ],
    edges: [
      { from: 'loans', to: 'nii', label: '利息', kind: 'money', n: 1 },
      { from: 'acct', to: 'fee', label: '会費・\n手数料', kind: 'money', n: 2 },
      { from: 'orig', to: 'flow', label: '売る・渡す', kind: 'goods', n: 3 },
      { from: 'b2b', to: 'tp', label: '処理料', kind: 'money' },
      { from: 'nii', to: 'stock', kind: 'ctrl' },
      { from: 'fee', to: 'stock', kind: 'ctrl' },
      { from: 'tp', to: 'stock', kind: 'ctrl', fo: -0.2, mx: 4.6 },
      { from: 'cond1', to: 'stock', kind: 'ctrl' },
      { from: 'cond2', to: 'flowk', kind: 'ctrl' },
      { from: 'flow', to: 'flowk', kind: 'ctrl' },
      { from: 'runoff', to: 'nii', label: '目減り', kind: 'risk', n: 4, fo: 0.2, mx: 5.05, lpos: 'v', ldy: -0.165 },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.66, mechH: 1.8,
    mech: [
      'B/S のローン残高に利息が付く\n純金利収益が 929.5 百万ドルで収益の 67%',
      '会員の口座に付く継続手数料と\nTech Platform を足すと、ストック型は約 76%',
      '売却益と LPB は組成のたびに生じる\nフロー型で、約 24%',
      'ただし個人ローンは期前返済が\n年 25.8% と速く、2〜3 年で返済される。\n残高を保つには組成を続ける必要がある',
    ],
    reason: '収益の約 4 分の 3 は残高に課金する\nストック型。ただし残高は 2〜3 年で\n入れ替わるため B',
    up: 'Plus の有料会員が 100 万人を超え、\n継続手数料が収益の 15% を超えれば A',
    down: '組成の減速で B/S の残高が\n減り始めれば C',
  });
  return s;
};
