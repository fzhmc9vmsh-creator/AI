// 2-1 事業理解(2/3): 事業どうしの関係(Opus の手本。関係図の基準はこの密度と描き方)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左: 顧客 → Oracle の事業(稼ぐ柱 → 伸びる柱)。右: 提携先と資本の出し手。①〜⑦ は右の「仕組み」と対応。売上は Q1 FY27(2026 年 6〜8 月)',
    source: 'report/r3_sections_5w1h_f20.md §2-0・§3-4、research2/R4_database_at.md、10-Q と決算資料(Q4 FY26・Q1 FY27)、calc/prereg2.md(コアの税引後利益)',
  });
  L.flowMap(s, {
    name: 's08b', h: 5.0, cols: [1.32, 1.36, 1.5, 1.32], rows: 4, nodeH: 0.78,
    lanes: [{ label: '顧客', c0: 0, c1: 0 }, { label: 'Oracle の事業', c0: 1, c1: 2, self: true }, { label: '提携先・資本の出し手', c0: 3, c1: 3 }],
    groups: [{ label: '稼ぐ柱', c0: 1, c1: 1, r0: 0, r1: 2 }, { label: '伸びる柱', c0: 2, c1: 2, r0: 0, r1: 3 }],
    nodes: [
      { id: 'apps', c: 0, r: 0, label: '業務アプリの\n利用企業', sub: '大企業・中堅' },
      { id: 'ent', c: 0, r: 1, rs: 2, label: '既存の DB 顧客', sub: '大企業・官公庁\n\nDB の切替に数年\n\n他社クラウドへ\n移った企業も含む' },
      { id: 'lab', c: 0, r: 3, label: 'AI 研究所', sub: 'OpenAI・Meta・xAI' },
      { id: 'saas', c: 1, r: 0, kind: 'unit', label: 'SaaS', sub: 'Fusion・NetSuite\n42 億ドル(+10%)' },
      { id: 'db', c: 1, r: 1, rs: 2, kind: 'key', label: 'DB ライセンス・保守', sub: 'Software 区分\n55.5 億ドル(−3%)\n\n保守はライセンスの\n年 22%\n\n営業利益の柱' },
      { id: 'oci', c: 2, r: 0, kind: 'unit', label: 'OCI 一般・主権', sub: '計算・保存の従量課金\n主権は最低 5 年' },
      { id: 'dbat', c: 2, r: 1, kind: 'unit', label: 'Database@', sub: '他社 DC 内で稼働\n売上 +353%' },
      { id: 'aidb', c: 2, r: 2, kind: 'unit', label: 'AI Database 26ai', sub: '自社データで AI 推論\n売上は非開示' },
      { id: 'aicap', c: 2, r: 3, kind: 'self', label: 'AI 容量', sub: 'GPU 時間の貸出\nIaaS +121% の主因' },
      { id: 'hyper', c: 3, r: 0, label: 'AWS・Azure・\nGoogle', sub: '競合かつ提携先' },
      { id: 'inv', c: 3, r: 2, label: '社債・株式の\n投資家', sub: '社債 430 億ドル\nATM 200 億ドル' },
      { id: 'dev', c: 3, r: 3, label: 'DC 開発事業者', sub: '建屋と電力を用意\n15〜19 年で貸す' },
    ],
    edges: [
      { from: 'apps', to: 'saas', label: '購読料', kind: 'money' },
      { from: 'ent', to: 'db', label: '保守料', kind: 'money', n: 1 },
      { from: 'saas', to: 'oci', label: 'OCI 上で稼働', kind: 'goods' },
      { from: 'db', to: 'oci', kind: 'goods', n: 2, lpos: 'v' },
      { from: 'db', to: 'dbat', label: '同じ DB を他社の DC へ', kind: 'goods', n: 3, below: true },
      { from: 'dbat', to: 'hyper', kind: 'ctrl', n: 3, lpos: 'v' },
      { from: 'db', to: 'aidb', label: 'AI を内蔵', kind: 'goods', n: 4 },
      { from: 'db', to: 'aicap', kind: 'money', n: 5, lpos: 'v' },
      { from: 'lab', to: 'aicap', label: '利用料と GPU 代の前払い', kind: 'money', n: 6 },
      { from: 'aicap', to: 'lab', label: 'GPU の計算容量', kind: 'goods' },
      { from: 'dev', to: 'aicap', label: '建屋を賃貸', kind: 'goods', n: 7, below: true },
      { from: 'inv', to: 'aicap', kind: 'money', n: 7, lpos: 'v' },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.66, mechH: 3.3,
    mech: [
      '既存顧客は保守料(ライセンスの年 22%)を払い続ける。切替に数年かかり、営業利益の柱になる',
      'OCI へ持ち込むと必要なライセンスは半分。さらに OCI の利用額の 25% 以上を保守料から値引きする',
      '同じ DB を AWS・Azure・Google の DC 内で提供。顧客は他社の契約枠で買え、売上は +353%',
      '26ai は DB に AI 検索とエージェントを追加費用なしで内蔵し、自社データで AI を動かす需要を DB の中に取り込む',
      'DB 保守と SaaS が生む税引後 約 230 億ドル/年が、AI 容量の建設の自己資金になる',
      'AI 研究所は容量の買い手であり、GPU 代の前払いや GPU の持込(該当契約 750 億ドル)で建設資金も出す',
      '建屋は開発事業者が建てて 15〜19 年で貸す。不足分は社債 430 億ドルと ATM 200 億ドルで賄う',
    ],
    reason: 'DB の顧客と現金が成長事業の土台。AI 容量だけは外部の資金(前払い・リース・社債)に頼り、ここが最大の争点',
  });
  return s;
};
