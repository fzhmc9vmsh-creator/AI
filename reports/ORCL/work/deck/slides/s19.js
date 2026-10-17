// 条件3 技術の AI 転用(評価 A)。指示書 spec/r6_cond.md の s19 節
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 既存の資産 → 転用の経路 → 新しい収益 ← 顧客。①〜④ は右と対応。数値は Q1 FY27',
    source: '会社開示(Q1 FY27)、research3/W6_database_at.md、research3/W8_aws_vs_commodity.md、report/r3_sections_5w1h_f20.md §2-0',
    grade: 'A', condNo: 3,
  });
  L.flowMap(s, {
    name: 's19', h: 5.0, cols: [1.35, 1.4, 1.4, 1.25], rows: 3, nodeH: 0.88,
    lanes: [{ label: '既存の資産', c0: 0, c1: 0 }, { label: 'Oracle の転用と成果', c0: 1, c1: 2, self: true }, { label: '顧客', c0: 3, c1: 3 }],
    groups: [{ label: '転用の経路', c0: 1, c1: 1, r0: 0, r1: 2 }, { label: '新しい収益', c0: 2, c1: 2, r0: 0, r1: 2 }],
    nodes: [
      { id: 'dbt', c: 0, r: 0, kind: 'ok', label: 'Oracle Database', sub: 'Exadata・\nAutonomous' },
      { id: 'net', c: 0, r: 1, kind: 'ok', label: 'RDMA ネットワーク', sub: 'Exadata 由来の\n低遅延の網' },
      { id: 'data', c: 0, r: 2, kind: 'ok', label: '既存顧客のデータ', sub: 'DB 内の基幹データ' },
      { id: 'dbat', c: 1, r: 0, kind: 'unit', label: 'Database@', sub: '他社の DC に\nExadata を設置' },
      { id: 'cluster', c: 1, r: 1, kind: 'unit', label: 'GPU クラスタ', sub: 'RDMA で GPU を\n大規模につなぐ' },
      { id: 'aidb', c: 1, r: 2, kind: 'unit', label: 'AI Database 26ai', sub: 'DB にベクトル検索・\nエージェントを内蔵' },
      { id: 'rev1', c: 2, r: 0, kind: 'self', label: 'マルチクラウド DB', sub: '売上 +353%\n顧客 +180%' },
      { id: 'rev2', c: 2, r: 1, kind: 'self', label: 'OCI', sub: '売上 74 億ドル\n(+121%)' },
      { id: 'rev3', c: 2, r: 2, label: '企業 AI 推論', sub: '売上は非開示' },
      { id: 'hyper', c: 3, r: 0, label: 'AWS・Azure・\nGoogle', sub: '70 リージョン\n119 AZ' },
      { id: 'lab', c: 3, r: 1, label: 'AI 研究所', sub: '学習・推論' },
      { id: 'ent', c: 3, r: 2, label: '企業', sub: '自社データで推論' },
    ],
    edges: [
      { from: 'dbt', to: 'dbat', label: 'そのまま提供', kind: 'goods', n: 1, lw: 1.0 },
      { from: 'net', to: 'cluster', label: 'GPU 間の網に', kind: 'goods', n: 2, lw: 1.0 },
      { from: 'data', to: 'aidb', label: 'AI を直結', kind: 'goods', n: 3 },
      { from: 'dbat', to: 'rev1', kind: 'money' },
      { from: 'cluster', to: 'rev2', kind: 'money' },
      { from: 'aidb', to: 'rev3', kind: 'money' },
      { from: 'hyper', to: 'rev1', label: '契約枠で購入', kind: 'money' },
      { from: 'lab', to: 'rev2', label: '容量料', kind: 'money', n: 4 },
      { from: 'ent', to: 'rev3', label: '利用', kind: 'money' },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.66, mechH: 1.8,
    mech: [
      'DB をそのまま他社の DC に置く(Database@)。追加の開発は小さく、売上 +353%',
      'Exadata 由来の RDMA 網で GPU を大規模につなぎ、OCI +121% の土台になった',
      '26ai は DB の中に AI 検索を内蔵し、企業データの AI 需要を DB に取り込む(売上は非開示)',
      'ただし OCI の伸びの主因は GPU の貸し出しで、DB の転用による収益が過半ではない',
    ],
    reason: '転用先が全社の増収の主因になったため A。\n主因は GPU の貸し出しで、DB 転用の収益が\n過半ではないため S ではない',
    up: 'AI 容量の顧客が DB やアプリも買う証拠\n(クロスセル)が出れば S',
    down: 'Database@ の伸びが 100% を割り、OCI の伸びが AI 容量だけになれば B',
  });
  return s;
};
