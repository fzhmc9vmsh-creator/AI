// 条件8(評価 B): コモディティ性。今と将来を分ける。今 = 学習向けの大型容量(C)、将来 = 推論・企業向け OCI・DB・アプリ(B)。左から 供給者 → Oracle の事業 → 買い手 ← 代替と価格の基準
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 供給者 → Oracle の事業(今: 学習向け → 将来: 推論・企業向け)→ 買い手 ← 代替と価格の基準。①〜⑤ は右と対応。価値の比率は需給エンジン第4.5版',
    source: '需給エンジン第4.5版(calc/out/m10_*.json: セグメント価値)、Investor Day 2026-10-28(CFO 資料)、research_v6、research3/W3_industry_structure.md、ICE・CME の発表(2026-05)、Epoch AI、SemiAnalysis ClusterMAX v3.0',
    grade: 'B', condNo: 8,
  });
  L.flowMap(s, {
    name: 's24', h: 4.66, cols: [1.5, 2.0, 1.5, 1.6], rows: 4,
    lanes: [{ label: '供給者', c0: 0, c1: 0 }, { label: 'Oracle の事業', c0: 1, c1: 1, self: true }, { label: '買い手', c0: 2, c1: 2 }, { label: '代替・価格の基準', c0: 3, c1: 3 }],
    groups: [{ label: 'AI 容量 1 株 113 ドル(44%)', c0: 1, c1: 1, r0: 0, r1: 1 }],
    nodes: [
      { id: 'nv', c: 0, r: 0, label: 'NVIDIA', sub: 'AI 計算の約 8 割' },
      { id: 'mem', c: 0, r: 1, kind: 'risk', label: '電力・メモリ', sub: '逼迫は 2028 年まで' },
      { id: 'dbtech', c: 0, r: 2, kind: 'ok', label: 'DB の技術', sub: '代替なし' },
      { id: 'learn', c: 1, r: 0, kind: 'risk', label: '学習向けの大型容量', sub: '今: コストプラス\n価格は原価で決まる', tag: { text: '今: C', tone: 'red' } },
      { id: 'inf', c: 1, r: 1, kind: 'ok', label: '推論(企業データの近く)', sub: '将来: 分散 50〜200MW\nDB・OCI と一体', tag: { text: '将来: B', tone: 'green' } },
      { id: 'db', c: 1, r: 2, kind: 'ok', label: '企業向け OCI・DB', sub: 'ソフト保守 16%・OCI 一般 14%\nDatabase@ 4%(価値の比率)', tag: { text: '将来: B', tone: 'green' } },
      { id: 'apps', c: 1, r: 3, kind: 'ok', label: 'アプリ(SaaS)', sub: 'SaaS 18%(価値の比率)' },
      { id: 'lab', c: 2, r: 0, label: 'AI 研究所', sub: '最も安い容量を選ぶ' },
      { id: 'ent', c: 2, r: 2, label: '企業', sub: 'データの近くで推論' },
      { id: 'neo', c: 3, r: 0, kind: 'risk', label: 'ネオクラウド', sub: 'H100 実勢 2.80 ドル/時\n大手の約 2.6 倍安い' },
      { id: 'fut', c: 3, r: 1, kind: 'risk', label: '価格指数・先物', sub: 'ICE・CME が準備' },
      { id: 'hyper', c: 3, r: 2, label: '大手クラウド', sub: 'H100 実勢 7.19 ドル/時' },
    ],
    edges: [
      { from: 'nv', to: 'learn', kind: 'money' },
      { from: 'mem', to: 'learn', kind: 'risk' },
      { from: 'dbtech', to: 'db', kind: 'goods', n: 1, lpos: 'v' },
      { from: 'db', to: 'ent', kind: 'goods' },
      { from: 'learn', to: 'lab', kind: 'goods', n: 2 },
      { from: 'lab', to: 'learn', kind: 'risk' },
      { from: 'inf', to: 'ent', kind: 'goods', n: 5 },
      { from: 'apps', to: 'ent', kind: 'goods' },
      { from: 'neo', to: 'lab', kind: 'risk', n: 3 },
      { from: 'fut', to: 'lab', kind: 'risk', n: 4 },
      { from: 'hyper', to: 'ent', kind: 'risk' },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.32,
    mech: [
      'DB・Database@ はデータのある場所で動く。代替がなく、価格は Oracle が決める',
      'AI 容量の買い手は最も安い容量を選ぶ。学習向けの大型容量は原価で値決めされ、今は C',
      'ネオクラウドの H100 実勢は大手の約 2.6 倍安い。需給が緩むと、限界供給者の損益分岐が価格になる',
      '価格指数と現金決済の先物(ICE・CME)が整い、GPU 時間の価格が標準化しつつある',
      '推論はデータの近くで DB・OCI・アプリと一体になり、コモディティにならない。将来は B',
    ],
    reason: '価値の 44% の AI 容量のうち、コモディティ化の恐れが大きいのは学習向けの部分。\n推論はデータの近くで DB・OCI と一体になり、企業向け OCI・DB・アプリはコモディティではないため B',
    up: '推論の比率と GPU 以外のサービス(契約総額の 13%)が上がり、再契約の単価が保たれれば A',
    down: '緩和期に再契約の単価が 6 割を下回るか、AI 粗利率が 25% 未満なら C',
  });
  L.kpiBand(s, '再契約の単価(会社: 4 年前の GPU +20%)/ GPU 以外のサービスの比率(13%)/ AI 粗利率(1GW 例 35%)が 25% 未満で C 候補');
  return s;
};
