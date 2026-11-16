// 価値の橋: 株価 → 今の利益が続く価値 → 理論株価(手本 c01_value_bridge を写す)
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, { kicker: '', source: '当方の計算(valuate.py、lenses.py L18)' });

  L.paneHead(s, 0.5, 1.62, 7.7, '株価から理論株価への橋渡し(1株あたり円)', 'pane_wf_head');
  L.waterfall(s, [
    { label: '株価', val: 2297, type: 'total', disp: '2,297' },
    { label: '今の利益が続く価値\nとの差', val: -1173, type: 'step' },
    { label: '今の利益が続く価値', val: 1124, type: 'total', disp: '1,124' },
    { label: '成長と変化の上乗せ', val: 534, type: 'step', highlight: true },
    { label: '理論株価', val: 1657.5, type: 'total', disp: '1,657.5' },
  ], { x: 0.55, y: 2.02, w: 7.6, h: 3.22, unit: '円/株', name: 'wf' });
  L.marks(s, [
    { x: 4.24, y: 3.06, n: 1 },
    { x: 3.42, y: 2.5, n: 2 },
    { x: 6.87, y: 2.4, n: 3 },
  ]);

  L.kpiTiles(s, [
    { value: F('calc.implied_coe'), label: '暗黙の資本コスト' },
    { value: '8.9%', label: '当方の資本コスト' }, // lint-ok: 台帳に無い手書き
    { value: `年率 ${F('calc.irr_172')}`, label: 'PER17.2倍の場合' }, // lint-ok: 台帳に無い手書き(PER前提)
    { value: `年率 ${F('calc.irr_20')}`, label: 'PER20倍の場合' }, // lint-ok: 台帳に無い手書き(PER前提)
  ], { compact: true, x: 0.55, y: 5.42, w: 7.6, h: 1.26 });

  L.paneHead(s, 8.45, 1.62, 4.38, '差640円の内訳', 'pane_split');
  L.table(s, [
    ['内訳', '円', '割合'],
    ['倍率(資本コスト)の差', '455', '71%'],
    ['EPSの見立ての差', '185', '29%'],
  ], { x: 8.45, y: 1.98, w: 4.38, colW: [2.6, 0.9, 0.88], fontSize: 10, rowH: 0.34, name: 'tbl_split' });
  L.text(s, '倍率の差: 会社計画の経路の価値(1,842.5円)と株価の差\nEPSの差: 理論株価と会社計画の経路の価値の差', { x: 8.45, y: 3.04, w: 4.38, h: 0.42, fontSize: 8.5, color: C.sub, margin: 0, objectName: 'note_split' });

  L.lookBox(s, [
    { n: 1, text: '1,124円 = 12か月先EPS約100円 ÷ 資本コスト8.9%(今の利益が続くだけの価値)' },
    { n: 2, text: '株価を正当化する資本コストは約7.5%(7.5%で2,269円)' },
    { n: 3, text: '余剰現金150円を足しても約1,810円。株価には届かない' },
  ], { x: 8.45, y: 3.58, w: 4.38, h: 1.66 }); // lint-ok: 台帳に無い手書き(1,124の式・2,269・1,810)

  L.takeaway(s, 8.45, 5.42, 4.38, 1.26,
    '株価は今の利益の約2倍(成長の値段1,173円=株価の51%)を払う。差の主因は事業の見立てではなく、市場が置く低い割引率', // lint-ok: 台帳に無い手書き
    { fontSize: 10.5 });
};
