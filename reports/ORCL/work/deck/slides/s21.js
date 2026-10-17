// 条件5(評価 B)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: 'CEO は OCI をゼロから築き容量と受注で実績を出したが、capex は見通しを繰り返し超え、報酬は総売上で決まる', kicker: '条件5 CEO が信頼に足り事業拡大の経歴を持つ', source: 'DEF 14A(報酬)、会社開示(FY26〜27 のガイダンス)、research4/T2_company_rpo_capacity.md', page: 21, grade: 'B', condNo: 5 });
  L.structure(s, {
    nodes: [
      { id: 'ceo', col: 0, row: 1, label: '共同 CEO', sub: 'Magouyrk(OCI 創設者)・Sicilia', kind: 'self' },
      { id: 'board', col: 0, row: 0, label: '報酬委員会', sub: 'PSO の KPI = FY28 総売上', kind: 'ext' },
      { id: 'capex', col: 2, row: 1, label: 'capex', sub: 'FY26 実績 557 億ドル', kind: 'risk' },
      { id: 'rpo', col: 2, row: 0, label: '受注残', sub: '6,640 億ドル', kind: 'ok' },
      { id: 'sh', col: 3, row: 2, label: '株主', sub: '1株価値', kind: 'ext' },
    ],
    edges: [
      { from: 'board', to: 'ceo', label: '報酬(80% は時間ベース)', kind: 'money' },
      { from: 'ceo', to: 'rpo', label: '容量で受注を確保', kind: 'goods', dx: 0.35, dy: -0.12 },
      { from: 'ceo', to: 'capex', label: '見通し 350 → 500 → 557 億ドル', kind: 'money' },
      { from: 'capex', to: 'sh', label: '総額 KPI と1株価値のずれ', kind: 'risk' },
    ],
  });
  L.t15Side(s, {
    evidence: ['FY26 capex: 当初見通し 約 350 億 → 2025-12 に約 500 億 → 実績 557 億ドル(最新見通し比 +11%)', 'FY27 売上ガイダンスは 85 → 89 → 90 → 90 以上と引き上げ', 'PSO の KPI は FY28 の非GAAP 総売上(1株指標ではない)', 'FAM の FY27 EPS 目標 10.65 ドルは単一出典で、FactSet の FY28 中央値と同値(年度ずれの可能性)'],
    reason: '成長の実行力は高いが、資本配分の規律と報酬の設計に留保が残るため B(C との境界)',
  });
};
