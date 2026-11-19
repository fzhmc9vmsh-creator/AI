// 3-3 現金の流れ: 左「生む」→ 営業CF → 右「投じる」。下に時間軸の帯と 3 つの数字
module.exports = function build(pres, L) {
  const { F } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 現金を生む製品群と前受け(9か月)。右: 現金の行き先',
    source: 'S-1/A-3 のCF計算書と契約義務の注記(pp.178-181)',
  });
  L.flowMap(s, {
    name: 's09', x: 0.5, y: 1.62, w: 12.33, h: 3.0, legend: false, cols: [2.5, 2.3, 3.3], rows: 3, nodeH: 0.66,
    lanes: [{ label: '生む', c0: 0, c1: 1, self: true }, { label: '投じる(9か月)', c0: 2, c1: 2 }],
    nodes: [
      { id: 'api', c: 0, r: 0, kind: 'unit', label: 'API 直販', sub: '売上の 56%' },
      { id: 'csp', c: 0, r: 1, kind: 'unit', label: 'クラウド事業者経由', sub: '売上の 44%' },
      { id: 'flat', c: 0, r: 2, kind: 'unit', label: '定額の契約', sub: '席の契約など' },
      { id: 'rpo', c: 1, r: 0, label: '契約残高(RPO)', sub: '13,800\n12 か月以内に 75% を売上に' },
      { id: 'ocf', c: 1, r: 1.5, h: 0.9, kind: 'key', label: '営業CF', sub: '+6,569(9 か月)' },
      { id: 'rd', c: 2, r: 0, label: '研究開発', sub: '19,240(学習の計算資源を含む)' },
      { id: 'cap', c: 2, r: 1, label: '設備投資', sub: '2,880' },
      { id: 'ob', c: 2, r: 2, kind: 'risk', label: '計算資源の支払い義務', h: 0.82, sub: '900,900(うち解約できない 714,700)\n2026 年第4四半期〜2030 年に 451,600 発生見込み' },
    ],
    edges: [
      { from: 'api', to: 'ocf', kind: 'money' },
      { from: 'csp', to: 'ocf', kind: 'money' },
      { from: 'flat', to: 'ocf', kind: 'money' },
      { from: 'rpo', to: 'ocf', kind: 'goods', label: '前受け' },
      { from: 'ocf', to: 'rd', kind: 'money', label: '投じる' },
      { from: 'ocf', to: 'cap', kind: 'money' },
      { from: 'ocf', to: 'ob', kind: 'risk', label: '将来の支払い' },
    ],
  });
  L.takeaway(s, 0.5, 4.72, 12.33, 0.42, '売上より先に、何年分もの計算資源の支払いが確定している → 投資が先行する事業', { fontSize: 12 });
  L.kpiTiles(s, [
    { value: F('oblig.x'), label: '支払い義務 ÷ 自己資本' },
    { value: F('ocf.9m'), label: '営業CF(9か月、百万ドル)' },
    { value: F('rpo'), label: '契約残高(RPO、百万ドル)' },
  ], { y: 5.18, h: 0.9, compact: true });
  L.termNotes(s, [
    { term: '営業CF', plain: '本業で実際に入った現金から出た現金を引いたもの', why: '利益と現金の時期のずれを見るため' },
    { term: 'FCF', plain: '営業CFから設備などの投資を引いた、自由に使える現金', why: '将来の構造で最も変わるのがFCFのため' },
    { term: 'RPO', plain: '契約済みでまだ売上にしていない金額(契約残高)', why: '現金と売上の時期のずれを見るため' },
    { term: 'CF', plain: 'キャッシュフロー。現金の出入り', why: '利益と現金の時期がずれる事業のため' },
  ], { x: 0.5, y: 6.12, w: 12.33 });
  return s;
};
