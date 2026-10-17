// 条件1(評価 B)。指示書 spec/ch3_conditions.md の s17 節どおり
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: 'DB の切替コストは 10 年以上続くが、AI の単価優位は逼迫期(FY32 まで)に限られ、10 年の圧倒的優位とは言えない', kicker: '条件1 10年間の価格決定力・競争優位・成長性を圧倒的水準で維持', source: '会社開示(Q1 FY27 説明会)、research4/T5_supply_components.md、research4/T3_saas_products.md、calc/prereg2.md §9', page: 17, grade: 'B', condNo: 1 });
  L.structure(s, {
    nodes: [
      { id: 'db', col: 0, row: 0, label: 'DB・SaaS 顧客', sub: '切替に数年。保守料は継続課金', kind: 'ext' },
      { id: 'orcl', col: 1, row: 1, label: 'Oracle', sub: 'DB を土台に複数の収益線', kind: 'self' },
      { id: 'lab', col: 3, row: 0, label: 'AI 研究所', sub: '容量料。更新は従来比 +20%', kind: 'ext' },
      { id: 'comp', col: 3, row: 2, label: '競合クラウド', sub: 'AWS・Azure・GCP・ネオクラウド', kind: 'risk' },
      { id: 'lease', col: 0, row: 2, label: '長期リース', sub: '賃料を FY47 まで固定', kind: 'ok' },
    ],
    edges: [
      { from: 'db', to: 'orcl', label: '保守料・購読料', kind: 'money', dx: -0.4, dy: 0.42 },
      { from: 'lab', to: 'orcl', label: '容量料(逼迫期 +5%/年)', kind: 'money' },
      { from: 'comp', to: 'orcl', label: '緩和後の値下げ圧力', kind: 'risk' },
      { from: 'orcl', to: 'lease', label: '固定賃料', kind: 'money' },
    ],
    tags: [{ node: 'db', text: '優位: 数十年', tone: 'green' }, { node: 'lab', text: '優位: FY32 まで', tone: 'red' }],
  });
  L.t15Side(s, {
    evidence: ['更新期の GPU をすべて従来契約比 +20% で更新・再販(Q1 FY27)', '2026 年の値上げ: AWS +15〜20%、Nebius +17〜21%', '需給が緩んだ後の長期の超過利益はベースで 0%(逼迫の終わり FY32)', 'SaaS +10%・Software −3% は SAP クラウド ERP +25% より遅い'],
    reason: 'DB の優位は長いが、AI の価格優位は業界全体の逼迫によるもので、緩和後は消えるため B',
  });
  return s;
};
