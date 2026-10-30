// 条件11 模倣困難性(評価 B): Oracle の資産 → 再現に要るもの → 再現にかかる時間 ← 競合
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: Oracle の資産 → 再現に要るもの → 再現にかかる時間 ← 競合。①〜④ は右と対応',
    source: 'research3/W3_industry_structure.md、research4/T5_supply_components.md、research4/T2_company_rpo_capacity.md、GE Vernova・PJM の開示',
    grade: 'B', condNo: 11,
  });
  L.flowMap(s, {
    name: 's27', h: 5.0, cols: [1.45, 1.5, 1.2, 1.45], rows: 4,
    lanes: [
      { label: 'Oracle の資産', c0: 0, c1: 0, self: true },
      { label: '再現に要るもの', c0: 1, c1: 1 },
      { label: '時間', c0: 2, c1: 2 },
      { label: '競合', c0: 3, c1: 3 },
    ],
    nodes: [
      { id: 'base', c: 0, r: 0, kind: 'ok', label: 'DB の顧客基盤', sub: '数十年の導入実績' },
      { id: 'place', c: 0, r: 1, kind: 'ok', label: 'Database@ の配置', sub: '70 リージョン\n119 AZ' },
      { id: 'cap', c: 0, r: 2, kind: 'unit', label: 'AI 容量', sub: '10GW 超を確保\n(FY29 まで)' },
      { id: 'bld', c: 0, r: 3, kind: 'unit', label: '電力付きの建屋', sub: '90% 超を\nパートナーが負担' },
      { id: 'mig', c: 1, r: 0, label: 'データ移行・\nアプリ改修', sub: '顧客側に数年' },
      { id: 'part', c: 1, r: 1, label: '競合クラウドとの提携', sub: 'AWS・Azure・Google\nの合意' },
      { id: 'money', c: 1, r: 2, label: '資本', sub: '1GW あたり\n数百億ドル' },
      { id: 'grid', c: 1, r: 3, kind: 'risk', label: '電力・系統', sub: '連系 約 40 か月\nタービンは\n2031 年分を販売中' },
      { id: 't1', c: 2, r: 0, kind: 'ok', label: '10 年超', sub: '実質再現できない' },
      { id: 't2', c: 2, r: 1, kind: 'ok', label: '提携先次第' },
      { id: 't3', c: 2, r: 2, kind: 'risk', label: '2〜4 年', sub: '資本があれば' },
      { id: 't4', c: 2, r: 3, kind: 'risk', label: '3〜4 年', sub: '電力の確保' },
      { id: 'pg', c: 3, r: 0, label: '他社 DB', sub: 'PostgreSQL ほか' },
      { id: 'hyp', c: 3, r: 1, label: '大手クラウド', sub: '自社 DB を推す' },
      { id: 'neo', c: 3, r: 2, kind: 'risk', label: 'ネオクラウド・大手', sub: '実際に建設中' },
      { id: 'util', c: 3, r: 3, label: '電力会社・開発事業者', sub: 'ほかの顧客にも供給' },
    ],
    edges: [
      { from: 'base', to: 'mig', kind: 'ctrl', n: 1 },
      { from: 'mig', to: 't1', kind: 'ctrl' },
      { from: 'pg', to: 't1', label: '追随できない', kind: 'risk' },
      { from: 'place', to: 'part', kind: 'ctrl', n: 2 },
      { from: 'part', to: 't2', kind: 'ctrl' },
      { from: 'hyp', to: 't2', label: '提携が要る', kind: 'risk' },
      { from: 'cap', to: 'money', kind: 'ctrl', n: 3 },
      { from: 'money', to: 't3', kind: 'ctrl' },
      { from: 'neo', to: 't3', label: '追随', kind: 'risk' },
      { from: 'bld', to: 'grid', kind: 'ctrl', n: 4 },
      { from: 'grid', to: 't4', kind: 'ctrl' },
      { from: 'util', to: 't4', label: '奪い合い', kind: 'risk' },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.66, mechH: 2.1,
    mech: [
      'DB の顧客基盤は数十年の導入とデータ移行の重さで、資本があっても再現できない',
      'Database@ は競合クラウドの DC 内に置く提携で、他社が同じ配置を得るのは難しい',
      'AI 容量は資本と電力があれば 2〜4 年で再現できる。大手・ネオクラウドが実際に建設中',
      '障壁として効くのは電力。\n系統連系に約 40 か月、ガスタービンは 2031 年分を販売中',
    ],
    reason: 'DB と配置は模倣が難しいが、\nAI 容量の障壁は時間にすぎず、\n資本のある競合には破られるため B',
    up: 'FY30〜32 分の電力を確保し、\n競合に 3 年以上先行できれば A',
    down: '競合の大型容量が 2027〜28 年に\n相次いで稼働し、AI 容量の単価が下がれば C',
  });
  return s;
};
