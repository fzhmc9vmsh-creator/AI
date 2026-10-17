// 条件7(評価 C)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: '株価が安い主因は市場の見落としではなく、OpenAI への集中(受注残の約 45%)と CDS 227bp が示す実在の信用リスクである', kicker: '条件7 PEG が低い理由がリスクの過大評価であること(MU 型の陳腐化 capex が理由ではない)', source: 'research2/R5_credit.md、research4/T2_company_rpo_capacity.md、research3/W2_gpu_economic_life.md、Bloomberg(2026-10-08)', page: 23, grade: 'C', condNo: 7 });
  L.structure(s, {
    nodes: [
      { id: 'mkt', col: 0, row: 0, label: '株式市場', sub: '事業実態 EPS の 15.7 倍', kind: 'ext' },
      { id: 'orcl', col: 1, row: 1, label: 'Oracle', sub: 'GPU を自社調達', kind: 'self' },
      { id: 'oai', col: 3, row: 0, label: 'OpenAI', sub: '受注残の約 45%・約 3,000 億ドル', kind: 'risk' },
      { id: 'bond', col: 0, row: 2, label: '社債・CDS 市場', sub: 'CDS 227bp、2056 年債 8% 超', kind: 'risk' },
      { id: 'nv', col: 3, row: 2, label: 'NVIDIA', sub: 'GPU 代', kind: 'ext' },
    ],
    edges: [
      { from: 'oai', to: 'orcl', label: '年 約 300 億ドル(2027〜)', kind: 'money' },
      { from: 'orcl', to: 'nv', label: 'GPU の購入', kind: 'money' },
      { from: 'bond', to: 'orcl', label: '資金(高い金利)', kind: 'money' },
      { from: 'oai', to: 'orcl', label: '不払いリスク', kind: 'risk', off: 0.25 },
      { from: 'orcl', to: 'mkt', label: '現金化への疑い', kind: 'risk' },
    ],
    tags: [{ node: 'oai', text: '集中リスク: Oracle 負担', tone: 'red' }],
  });
  L.t15Side(s, {
    evidence: ['OpenAI の年換算売上 240 億ドル(3 月)→ 約 500 億ドル(10/8、700 億ドル報道を下方修正)', 'OpenAI の計算契約は 1.15〜1.5 兆ドル、2026〜30 年の FCF 累計 −2,780 億ドル', 'S&P BBB-(2026-07)。FY29 までに FOCF が黒字化しなければ再格下げ', '見落としで説明できるのは GPU 寿命の悲観だけ(H100 を元の 95% で再契約の例)'],
    reason: '安さの主因は実在のリスクで、見落としは一部(GPU 寿命・J カーブ)に限られるため C',
    kpi: 'CDS 5年 200bp 未満で確度を上げ、300bp 超で D 候補 / FY29 より前の BB+ 格下げで D 候補 / OpenAI の比率 40% 未満で確度を上げ、契約変更・支払遅延の報道で E 候補',
  });
};
