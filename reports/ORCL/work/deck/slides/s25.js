// 条件9(評価 B)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: '止まれば顧客の AI 事業が止まる電力付きの容量で更新率は高いが、代替のクラウドもあり不可欠とまでは言えない', kicker: '条件9 顧客の AI 実装の「停めない運用」に不可欠', source: '会社開示(Q4 FY26・Q1 FY27 説明会)、research4/T4_ai_demand.md', page: 25, grade: 'B', condNo: 9 });
  L.structure(s, {
    nodes: [
      { id: 'orcl', col: 1, row: 1, label: 'Oracle OCI', sub: '稼働率 97.9%', kind: 'self' },
      { id: 'lab', col: 3, row: 0, label: 'AI 研究所', sub: '学習・推論(本番)', kind: 'ext' },
      { id: 'ent', col: 3, row: 2, label: '企業', sub: 'Oracle DB 内のデータで推論', kind: 'ext' },
      { id: 'power', col: 0, row: 1, label: '電力付きの容量', sub: 'Q1 FY27 に 850MW 納入', kind: 'ok' },
      { id: 'alt', col: 1, row: 2, label: '代替のクラウド', sub: '乗り換えに数か月〜数年', kind: 'risk' },
    ],
    edges: [
      { from: 'power', to: 'orcl', label: '容量', kind: 'goods' },
      { from: 'orcl', to: 'lab', label: '計算容量', kind: 'goods' },
      { from: 'orcl', to: 'ent', label: 'DB と推論', kind: 'goods' },
      { from: 'alt', to: 'ent', label: '乗り換えの選択肢', kind: 'risk' },
    ],
  });
  L.t15Side(s, {
    evidence: ['Q4 FY26 は顧客の 49% が GPU の 92% を更新', '推論の比率(電力): 2025 年 47.5% → 2030 年 60.0%(McKinsey)', '推論は本番稼働で、止まると顧客の売上が止まる'],
    reason: '電力付きの容量と DB は止められない運用を支えるが、代替が存在するため B',
  });
};
