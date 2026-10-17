// 条件10(評価 B)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: 'DB の技術と顧客関係は長寿命で、GPU の6年償却は更新・再販の実績と整合する。ただし GPU の世代交代は速い', kicker: '条件10 無形資産投資も陳腐化リスクを厳格に評価', source: 'research3/W2_gpu_economic_life.md、会社開示(耐用年数の変更)', page: 26, grade: 'B', condNo: 10 });
  L.structure(s, {
    nodes: [
      { id: 'intang', col: 0, row: 0, label: 'DB 技術・顧客関係', sub: '寿命は数十年', kind: 'ok' },
      { id: 'gpu', col: 0, row: 2, label: 'GPU', sub: '6 年償却・上限 10 年', kind: 'risk' },
      { id: 'orcl', col: 1, row: 1, label: 'Oracle', sub: '更新・再販で回収', kind: 'self' },
      { id: 'cust', col: 3, row: 1, label: '顧客', sub: '更新 +20%', kind: 'ext' },
      { id: 'nv', col: 3, row: 2, label: 'NVIDIA の新世代', sub: 'Rubin は電力あたり約 10 倍', kind: 'risk' },
    ],
    edges: [
      { from: 'intang', to: 'orcl', label: '保守・SaaS', kind: 'money' },
      { from: 'gpu', to: 'orcl', label: '容量', kind: 'goods' },
      { from: 'cust', to: 'orcl', label: '更新料', kind: 'money' },
      { from: 'nv', to: 'gpu', label: '世代交代', kind: 'risk' },
    ],
  });
  L.t15Side(s, {
    evidence: ['CoreWeave は H100 を元の価格の 95% で再契約。中古 H100 は新品の 61% → 69%', 'Amazon はサーバーの耐用年数を 6 → 5 年に短縮', '3 年耐用なら Oracle の EPS は −17%(JPMorgan AM の試算)'],
    reason: '経済的寿命 ≧ 会計の耐用年数を示す証拠が優勢だが、電力制約の下での置き換えリスクが残るため B',
  });
};
