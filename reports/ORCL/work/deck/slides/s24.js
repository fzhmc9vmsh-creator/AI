// 条件8(評価 C): コモディティ性。指示書 spec/r6_cond.md の s24 節
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 供給者 → Oracle の事業(1 株価値の内訳)→ 買い手 ← 代替と価格の基準。①〜⑤ は右と対応',
    source: '需給エンジン第4.3版(セグメント価値)、research3/W3_industry_structure.md、ICE・CME の発表(2026-05)、Epoch AI、SemiAnalysis ClusterMAX v3.0',
    grade: 'C', condNo: 8,
  });
  L.flowMap(s, {
    name: 's24', h: 4.66, cols: [1.2, 1.45, 1.4, 1.35], rows: 3,
    lanes: [{ label: '供給者', c0: 0, c1: 0 }, { label: 'Oracle の事業', c0: 1, c1: 1, self: true }, { label: '買い手', c0: 2, c1: 2 }, { label: '代替・価格の基準', c0: 3, c1: 3 }],
    nodes: [
      { id: 'dbtech', c: 0, r: 0, kind: 'ok', label: 'DB の技術', sub: '代替なし' },
      { id: 'nv', c: 0, r: 1, label: 'NVIDIA', sub: 'AI 計算の約 8 割' },
      { id: 'mem', c: 0, r: 2, kind: 'risk', label: 'メモリ・電力', sub: '逼迫は\n2028 年まで' },
      { id: 'diff', c: 1, r: 0, kind: 'unit', label: 'DB 保守・SaaS・\nOCI 一般', sub: '1 株 120 ドル\n(45 + 44 + 31)', tag: { text: '差別化', tone: 'green', above: true } },
      { id: 'ai', c: 1, r: 1, rs: 2, kind: 'unit', label: 'AI 容量', sub: '1 株 117 ドル\n(価値の 45%)\n\n差: 電力の確保・\nRDMA 網・品質 Gold', tag: { text: '緩和後は商品', tone: 'red', above: true } },
      { id: 'ent', c: 2, r: 0, label: '企業', sub: 'データの近くで推論' },
      { id: 'lab', c: 2, r: 1, label: 'AI 研究所', sub: '最も安い容量を選ぶ' },
      { id: 'hyper', c: 3, r: 0, label: '大手クラウド', sub: 'H100 実勢\n7.19 ドル/時' },
      { id: 'neo', c: 3, r: 1, kind: 'risk', label: 'ネオクラウド', sub: 'H100 実勢\n2.80 ドル/時' },
      { id: 'fut', c: 3, r: 2, kind: 'risk', label: '価格指数・先物', sub: 'Silicon Data・Ornn\nICE・CME が準備' },
    ],
    edges: [
      { from: 'dbtech', to: 'diff', kind: 'goods' },
      { from: 'ai', to: 'nv', label: 'GPU 代', kind: 'money' },
      { from: 'mem', to: 'ai', label: '原価の上昇', kind: 'risk' },
      { from: 'diff', to: 'ent', label: '代替なし', kind: 'goods', n: 1 },
      { from: 'ai', to: 'lab', label: 'GPU 時間', kind: 'goods', n: 2 },
      { from: 'neo', to: 'lab', label: '約 2.6 倍\n安い', kind: 'risk', n: 3, lw: 0.8 },
      { from: 'hyper', to: 'ent', label: 'DB の移行', kind: 'risk' },
      { from: 'fut', to: 'ai', label: '価格の標準化', kind: 'risk', n: 4 },
      { from: 'lab', to: 'ai', kind: 'risk', n: 5 },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.32,
    mech: [
      'DB・Database@ はデータのある場所で動く。代替がなく、価格は Oracle が決める',
      'AI 容量の買い手は最も安い容量を選ぶ。\nOracle の差は電力の確保・RDMA 網・品質(ClusterMAX Gold)',
      'ネオクラウドの H100 実勢は大手の約 2.6 倍安い。需給が緩むと、限界供給者の損益分岐が価格になる',
      '価格指数と現金決済の先物(ICE・CME)が整い、GPU 時間の価格が標準化しつつある',
      '推論トークンの価格は、同じ性能で\n年 9〜900 倍の速さで下がっている(Epoch)',
    ],
    reason: '価値の 45% を占める AI 容量が、逼迫の緩和後に商品として値決めされる層にあるため C',
    up: 'AI 粗利率 35% 以上が続き、緩和期に入っても更新プレミアムが正なら B',
    down: 'AI 粗利率が 25% 未満か、更新プレミアムが 0% 以下なら D 候補',
  });
  L.kpiBand(s, 'AI 粗利率(最終開示 32%)が 25% 未満で D 候補・35% 以上で B 候補 / 更新プレミアム(+20%)が 0% 以下で D 候補 / H100 1 年契約の指数(2.65 ドル)が 2.00 ドル未満');
  return s;
};
