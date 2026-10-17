// 条件11(評価 B)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: 'DB の顧客基盤と他社クラウド内の配置は再現が難しいが、AI 容量は資本と電力があれば 2〜4 年で再現できる', kicker: '条件11 既存 CF・設備・技術が停めない運用に不可欠かつ模倣困難・代替不可能', source: 'research3/W3_industry_structure.md、research4/T5_supply_components.md、research4/T2_company_rpo_capacity.md', page: 27, grade: 'B', condNo: 11 });
  L.structure(s, {
    nodes: [
      { id: 'dev', col: 0, row: 1, label: 'DC 開発事業者', sub: 'Crusoe・Vantage・Related・STACK', kind: 'ok' },
      { id: 'grid', col: 0, row: 0, label: '電力・系統', sub: '連系 約 40 か月、タービン 2031 年分を販売中', kind: 'risk' },
      { id: 'orcl', col: 2, row: 1, label: 'Oracle', sub: '10GW 超を確保(FY29 まで)', kind: 'self' },
      { id: 'hyper', col: 3, row: 0, label: '提携先クラウド', sub: 'Oracle DB を 70 リージョンに', kind: 'ext' },
      { id: 'comp', col: 3, row: 2, label: '資金のある競合', sub: '2〜4 年で再現', kind: 'risk' },
    ],
    edges: [
      { from: 'dev', to: 'orcl', label: '電力付き建屋(90% 超を相手が資金負担)', kind: 'goods', off: -0.15 },
      { from: 'orcl', to: 'dev', label: '15〜19 年の賃料', kind: 'money', off: 0.15, below: true },
      { from: 'grid', to: 'dev', label: '電力の制約', kind: 'risk' },
      { from: 'orcl', to: 'hyper', label: 'DB の配置', kind: 'goods' },
      { from: 'comp', to: 'orcl', label: '追随', kind: 'risk' },
    ],
  });
  L.t15Side(s, {
    evidence: ['GE Vernova のガス発電の受注残 116GW、変圧器 128〜144 週', 'PJM 2028/29 で信頼度要件に 6,831MW 不足', 'Jupiter(2.45GW)は不可抗力通知の報道(単一系統、未確認)。10/13 に電力計画を提案'],
    reason: 'DB の配置は模倣困難だが、AI 容量の障壁は時間で、資本のある競合には破られるため B',
  });
};
