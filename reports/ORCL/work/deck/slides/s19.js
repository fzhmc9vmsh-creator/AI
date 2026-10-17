// 条件3(評価 A)。指示書 spec/ch3_conditions.md の s19 節どおり
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: 'DB とネットワークの技術が OCI(+121%)と Database@(+353%)に転用され、増収の主因になった', kicker: '条件3 コア技術・データが AI 事業に転用され成果が出始めている', source: '会社開示(Q1 FY27)、research3/W6_database_at.md、research3/W8_aws_vs_commodity.md', page: 19, grade: 'A', condNo: 3 });
  L.structure(s, {
    nodes: [
      { id: 'tech', col: 0, row: 1, label: 'DB・Exadata の技術', sub: 'RDMA ネットワーク・Autonomous', kind: 'self' },
      { id: 'oci', col: 1, row: 0, label: 'OCI', sub: '売上 74 億ドル(+121%)', kind: 'self' },
      { id: 'dbat', col: 1, row: 2, label: 'Database@', sub: '他社クラウド内の Oracle DB(+353%)', kind: 'self' },
      { id: 'lab', col: 3, row: 0, label: 'AI 研究所', sub: 'GPU クラスタを利用', kind: 'ext' },
      { id: 'hyper', col: 3, row: 2, label: 'AWS・Azure・GCP', sub: '70 リージョンに配置', kind: 'ext' },
    ],
    edges: [
      { from: 'tech', to: 'oci', label: 'ネットワーク設計', kind: 'goods' },
      { from: 'tech', to: 'dbat', label: 'DB をそのまま提供', kind: 'goods' },
      { from: 'oci', to: 'lab', label: '計算容量', kind: 'goods' },
      { from: 'dbat', to: 'hyper', label: '顧客接点は提携先', kind: 'risk' },
    ],
    tags: [{ node: 'dbat', text: '追加投資は小さい', tone: 'green' }],
  });
  L.t15Side(s, {
    evidence: ['OCI 売上 74 億ドル(+121%、Q1 FY27)', 'Database@ +353%、70 リージョン・119 AZ(AWS は 22 リージョン)', 'AI 容量の顧客が DB・アプリも買う証拠は見つからない'],
    reason: '転用は増収の主因になったが、主因は容量の貸し出しで、DB の転用収益が過半ではないため S でなく A',
  });
  return s;
};
