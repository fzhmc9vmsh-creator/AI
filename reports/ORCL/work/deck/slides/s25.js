// 条件9 運用上の不可欠性(評価 B): 供給の基盤 → Oracle → 顧客の運用 ← 代替
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 供給の基盤 → Oracle → 顧客の運用 ← 代替。①〜④ は右と対応',
    source: '会社開示(Q4 FY26・Q1 FY27 説明会)、research4/T4_ai_demand.md(McKinsey)、report/r3_sections_5w1h_f20.md §3-4',
    grade: 'B', condNo: 9,
  });
  L.flowMap(s, {
    name: 's25', h: 5.0, cols: [1.35, 1.4, 1.55, 1.4], rows: 3, nodeH: 0.86,
    lanes: [
      { label: '供給の基盤', c0: 0, c1: 0 },
      { label: 'Oracle', c0: 1, c1: 1, self: true },
      { label: '顧客の運用', c0: 2, c1: 2 },
      { label: '代替', c0: 3, c1: 3 },
    ],
    nodes: [
      { id: 'power', c: 0, r: 0, kind: 'ok', label: '電力付きの建屋', sub: 'Q1 FY27 に\n850MW を納入' },
      { id: 'gpu', c: 0, r: 1, label: 'GPU クラスタ', sub: '稼働率 97.9%' },
      { id: 'db', c: 0, r: 2, kind: 'ok', label: 'Oracle DB', sub: '基幹データ' },
      { id: 'oci', c: 1, r: 0, rs: 2, kind: 'self', label: 'OCI(AI 容量)', sub: '学習・推論の容量\n\nQ4 FY26:\n顧客の 49% が\nGPU の 92% を更新' },
      { id: 'dbs', c: 1, r: 2, kind: 'unit', label: 'DB・Database@', sub: '基幹業務の DB' },
      { id: 'train', c: 2, r: 0, label: 'AI 研究所の学習', sub: '止まると開発が遅れる' },
      { id: 'inf', c: 2, r: 1, label: 'AI 研究所の推論(本番)', sub: '止まると売上が止まる' },
      { id: 'ent', c: 2, r: 2, label: '企業の基幹業務と AI', sub: 'DB 内のデータで推論' },
      { id: 'alt1', c: 3, r: 0, kind: 'risk', label: '他社クラウド・\nネオクラウド', sub: '乗り換えに\n数か月〜数年' },
      { id: 'alt2', c: 3, r: 1, kind: 'risk', label: 'TPU・自社チップ', sub: 'Anthropic は TPU\n約 3.5GW(2027〜)' },
      { id: 'alt3', c: 3, r: 2, kind: 'risk', label: 'DB の移行', sub: '数年がかり' },
    ],
    edges: [
      { from: 'power', to: 'oci', label: '容量', kind: 'goods' },
      { from: 'gpu', to: 'oci', kind: 'goods' },
      { from: 'db', to: 'dbs', kind: 'goods' },
      { from: 'oci', to: 'train', label: '計算容量', kind: 'goods' },
      { from: 'oci', to: 'inf', label: '本番の推論', kind: 'goods', n: 1 },
      { from: 'dbs', to: 'ent', kind: 'goods', n: 3 },
      { from: 'alt1', to: 'train', label: '乗り換え', kind: 'risk', n: 2 },
      { from: 'alt2', to: 'inf', label: '代替の計算', kind: 'risk', n: 4 },
      { from: 'alt3', to: 'ent', label: '移行', kind: 'risk' },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.66, mechH: 2.0,
    mech: [
      '推論は本番の稼働で、止まると顧客の売上が止まる。推論の電力比率は 2025 年 47.5% → 2030 年 60%',
      '乗り換えには電力付きの容量の確保が要り、数か月〜数年かかる',
      '企業の AI は Oracle DB 内のデータで動く。DB の移行には数年かかる',
      'Q4 FY26 は顧客の 49% が GPU の 92% を更新。ただし他社クラウドや TPU という代替がある',
    ],
    reason: '電力付きの容量と DB は止められない\n運用を支え更新率も高いが、\n代替のクラウドが存在するため B',
    up: '大型顧客の更新率が 90% を超え、\n乗り換えの事例が出なければ A',
    down: '大型顧客が TPU や自社チップへ\n移る事例が出れば C',
  });
  return s;
};
