// 条件2(見本 exT15 をそのまま使う。根拠の4行目のみ差し替え)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: 'コア事業は税引後 230 億ドルを稼ぎ、AI の投資は前払いと長期リースで外部化するが、全社 FCF はエンジンで FY29 まで赤字', kicker: '条件2 コア事業が潤沢なキャッシュフローを持つ', source: '会社開示(Q1 FY27、10-Q)、需給エンジン第4.3版(calc/out/m8_all.json)、research2/R7_capital_power.md', page: 18, grade: 'B', condNo: 2 });
  L.structure(s, {
    nodes: [
      { id: 'core', col: 0, row: 0, label: 'DB 保守・SaaS', sub: '税引後 230 億ドル(FY27)', kind: 'self' },
      { id: 'orcl', col: 1, row: 1, label: 'Oracle', sub: 'AI 容量の投資', kind: 'self' },
      { id: 'cust', col: 3, row: 0, label: '顧客(OpenAI ほか)', sub: '前払い 24%・受注残 6,640 億ドル', kind: 'ext' },
      { id: 'partner', col: 0, row: 2, label: 'DC パートナー', sub: '建屋・電力(15〜19 年リース)', kind: 'ok' },
      { id: 'gpu', col: 3, row: 2, label: 'GPU・ネットワーク', sub: 'Oracle が保有(6 年償却)', kind: 'risk' },
    ],
    edges: [
      { from: 'core', to: 'orcl', label: '営業 CF', kind: 'money' },
      { from: 'cust', to: 'orcl', label: '前払い・利用料', kind: 'money' },
      { from: 'orcl', to: 'partner', label: '賃料(固定)', kind: 'money' },
      { from: 'orcl', to: 'gpu', label: 'capex', kind: 'money' },
      { from: 'gpu', to: 'cust', label: '計算容量', kind: 'goods', off: 0.2 },
    ],
    tags: [{ node: 'gpu', text: '陳腐化リスク: Oracle 負担', tone: 'red' }, { node: 'partner', text: '建屋の資金: パートナー', tone: 'green' }],
  });
  L.t15Side(s, {
    evidence: ['コア事業の税引後利益 230 億ドル(FY27、エンジン)', '前払い・持ち込み 750 億ドル累計(会社開示)', 'FCF: FY27 −342 億 / FY28 −340 億 / FY29 −135 億ドル(エンジン)', 'S&P の基本シナリオとコンセンサスは FY29 に FCF 黒字(エンジンは −135 億ドル)'],
    reason: 'コアの現金は潤沢で投資の多くは外部化されているが、自己資金で賄えない期間が FY29 まで続くため B',
  });
};
