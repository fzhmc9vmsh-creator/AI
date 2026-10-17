// ブループリントの見本(Haiku が写経する元)。各関数が1枚を作る
const L = require('./lib.js');
const { C, M, W } = L;

// 見本1: T15 構造図(条件2)
function exT15(pres) {
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
    evidence: ['コア事業の税引後利益 230 億ドル(FY27、エンジン)', '前払い・持ち込み 750 億ドル累計(会社開示)', 'FCF: FY27 −342 億 / FY28 −340 億 / FY29 −135 億ドル(エンジン)', 'S&P の基本シナリオとコンセンサスは FY29 黒字'],
    reason: 'コアの現金は潤沢で投資の多くは外部化されているが、自己資金で賄えない期間が FY29 まで続くため B',
  });
  return s;
}

// 見本2: チャート+右パネル(T7)
function exChart(pres) {
  const s = L.contentSlide(pres, { title: '全社の営業利益率は AI の比率上昇で FY29 に 31% まで下がり、AI 事業内の利益率改善で FY32 に 34% へ戻る', kicker: '事業実態の営業利益率(株式報酬を費用に含む)と AI 事業の利益率、FY27〜32', source: '需給エンジン第4.3版(calc/model8.py)', page: 10 });
  const yrs = ['FY27', 'FY28', 'FY29', 'FY30', 'FY31', 'FY32'];
  L.chartPanel(pres, s, { type: pres.charts.LINE, data: [
    { name: '全社の営業利益率', labels: yrs, values: [33.3, 32.9, 31.0, 32.7, 33.5, 34.1] },
    { name: 'AI 事業の営業利益率', labels: yrs, values: [10.5, 22.1, 22.6, 27.6, 29.0, 30.4] },
  ], opts: { showLegend: true, legendPos: 'b', chartColors: [C.dark, C.light], lineSize: 2, dataLabelPosition: 't', dataLabelFormatCode: '0.0', valAxisMinVal: 0, valAxisMaxVal: 40 } },
  { takeawayText: '利益率の低下は構成の変化によるもので、AI 事業そのものは成熟で改善する', points: ['AI の売上比率: 30% → 66%', 'オーナー利益のルール・オブ・40: 76(FY28)→ 46(FY32)'], note: '注: FY31 の値は補間' });
  return s;
}

// 見本3: 流れ図(T16)
function exFlow(pres) {
  const s = L.contentSlide(pres, { title: '拒否権と C 上限の規則は発動しない。条件6 は数値上 S だが、条件7 との対評価で S を無効にし、余裕の薄さから B とした', kicker: '構造評価の導出: 評価分布 → 適用ルール → 構造評価', source: '銘柄分析メソッド Phase 6、本資料の評価一覧', page: 5 });
  L.flow(s, [
    { head: '入力: 13 条件の評価', boxes: [{ text: 'S × 1(条件4)', tone: 'key' }, { text: 'A × 2(条件3・12)', tone: 'on' }, { text: 'B × 8', tone: 'in' }, { text: 'C × 2(条件7・8)', tone: 'in' }] },
    { head: '処理: 適用ルール', boxes: [{ text: '致命条件の拒否権(E 以下): 非発動', tone: 'off' }, { text: '条件6・7 の対評価: 発動(条件6 の S を無効)', tone: 'on' }, { text: 'C × 4 以上で上限 C: 非発動(C は 2)', tone: 'off' }] },
    { head: '出力: 構造評価', boxes: [{ text: 'B', tone: 'key', h: 1.6, size: 40, bold: true }, { text: '最頻の B を採用(機械的な平均はしない)', tone: 'in' }] },
  ]);
  return s;
}

module.exports = { exT15, exChart, exFlow };
if (require.main === module) {
  const pres = L.newDeck();
  exT15(pres); exChart(pres); exFlow(pres);
  pres.writeFile({ fileName: 'examples.pptx' }).then(() => console.log('ok'));
}
