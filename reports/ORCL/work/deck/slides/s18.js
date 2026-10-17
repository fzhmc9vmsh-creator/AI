// 条件2 コア事業の現金創出(評価 B)。指示書 spec/r6_cond.md の s18 節
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 資金の出し手 → Oracle の資金の源 → 使い道 → 結果。①〜⑤ は右と対応。金額は FY27(需給エンジン第4.3版・会社開示)',
    source: '会社開示(Q1 FY27、10-Q)、需給エンジン第4.3版(calc/out/m8_all.json)、research2/R7_capital_power.md、S&P(2026-07)',
    grade: 'B', condNo: 2,
  });
  L.flowMap(s, {
    name: 's18', h: 5.0, cols: [1.35, 1.45, 1.45, 1.35], rows: 4,
    lanes: [{ label: '資金の出し手', c0: 0, c1: 0 }, { label: 'Oracle', c0: 1, c1: 2, self: true }, { label: '支払先・評価者', c0: 3, c1: 3 }],
    groups: [{ label: '資金の源', c0: 1, c1: 1, r0: 0, r1: 3 }, { label: '使い道と結果', c0: 2, c1: 2, r0: 0, r1: 3 }],
    nodes: [
      { id: 'cust', c: 0, r: 0, label: 'DB・SaaS の顧客', sub: '保守料・購読料' },
      { id: 'lab', c: 0, r: 1, label: 'AI 研究所', sub: 'GPU 代の前払い' },
      { id: 'dev', c: 0, r: 2, kind: 'ok', label: 'DC 開発事業者', sub: '10GW の 90% 超の\n建屋を負担' },
      { id: 'inv', c: 0, r: 3, label: '社債・株式の投資家', sub: '社債 430 億ドル\n優先株 50 億・\nATM 200 億ドル' },
      { id: 'core', c: 1, r: 0, kind: 'unit', label: 'コアの利益', sub: '税引後 230 億ドル' },
      { id: 'prepay', c: 1, r: 1, kind: 'ok', label: '前受収益', sub: '154 → 308 億ドル\n(1 年で倍増)' },
      { id: 'lease', c: 1, r: 2, kind: 'ok', label: '長期リース', sub: '未開始 2,880 億ドル\n15〜19 年' },
      { id: 'debt', c: 1, r: 3, kind: 'risk', label: '借入・株式', sub: 'BBB−(S&P)' },
      { id: 'capex', c: 2, r: 0, rs: 2, kind: 'key', label: 'capex(FY27)', sub: '総額 900〜950 億ドル\n\n\n前払いが\n約 24% を賄う\n\n\n純現金 700 億ドル以下\n(会社の見通し)' },
      { id: 'rent', c: 2, r: 2, kind: 'risk', label: '賃料', sub: '固定費として\n15〜19 年続く' },
      { id: 'fcf', c: 2, r: 3, kind: 'risk', label: '全社 FCF\n(エンジン)', sub: 'FY27 −342 億\nFY29 −135 億ドル' },
      { id: 'nv', c: 3, r: 0, label: 'NVIDIA・部材', sub: 'GPU・網・メモリ' },
      { id: 'sp', c: 3, r: 3, label: 'S&P', sub: 'FY29 までの\nFOCF 黒字を要求' },
    ],
    edges: [
      { from: 'cust', to: 'core', label: '保守料・\n購読料', kind: 'money' },
      { from: 'core', to: 'capex', kind: 'money', n: 1 },
      { from: 'lab', to: 'prepay', label: '前払い', kind: 'money', n: 2 },
      { from: 'prepay', to: 'capex', kind: 'money', n: 2 },
      { from: 'dev', to: 'lease', label: '建屋を賃貸', kind: 'goods', n: 3 },
      { from: 'lease', to: 'rent', kind: 'money' },
      { from: 'inv', to: 'debt', label: '社債・株式', kind: 'money', n: 4 },
      { from: 'debt', to: 'fcf', label: '不足を埋める', kind: 'money' },
      { from: 'capex', to: 'nv', label: 'GPU 代', kind: 'money' },
      { from: 'fcf', to: 'sp', label: '格付けの条件', kind: 'ctrl', n: 5, lw: 0.98 },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.66, mechH: 2.1,
    mech: [
      'コアの利益(税引後 230 億ドル)が capex の自己資金の柱になる',
      'AI 研究所が GPU 代の約 24% を前払いし、前受収益は 1 年で倍増(154 → 308 億ドル)',
      '建屋と電力は開発事業者が資金を出し、Oracle は 15〜19 年の賃料で借りる(未開始 2,880 億ドル)',
      '残りは社債・優先株・ATM で調達。\n全社 FCF はエンジンで FY29 まで赤字(FY29 −135 億ドル)',
      'S&P は FY29 までの FOCF 黒字化を、格付け維持の条件にする。S&P とコンセンサスは FY29 に黒字',
    ],
    reason: 'コアの現金は潤沢で、投資の多くは\n外部化されている。ただし自己資金で\n賄えない期間が FY29 まで続くため B',
    up: '前払いの比率が 30% を超え、FCF の黒字化が FY28 に早まれば A',
    down: 'FY29 の FCF が赤字のまま\nBB+ に格下げされれば C',
  });
  return s;
};
