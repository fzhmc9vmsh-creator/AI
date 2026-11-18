// c01_value_bridge.js 価値の橋(手本): 現在値 → 理論株価を L.waterfall + L.marks + L.kpiTiles + L.lookBox + L.takeaway で描く
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    source: '本分析の価値評価モデル(手本)。現在値・理論株価・ROE・資本コスト・EPSは手本用の固定値',
  });

  L.paneHead(s, 0.5, 1.62, 7.7, '現在値から理論株価への橋渡し(価値の橋、1株あたり円)', 'pane_wf_head');

  L.waterfall(s, [
    { label: '現在値', val: 786, type: 'total' },
    { label: '今の利益が続く場合\nの価値との差', val: 193, type: 'step', highlight: true, ref: 'p.8' },
    { label: '成長と変化の上乗せ', val: 26, type: 'step', ref: 'p.14' },
    { label: '理論株価', val: 1005, type: 'total' },
  ], { x: 0.55, y: 2.02, w: 7.60, h: 3.22, unit: '円', axisMin: 700, name: 'wf' });

  L.marks(s, [
    { x: 3.90, y: 3.20, n: 1, text: '差の約9割', side: 'right' },
    { x: 5.35, y: 2.62, n: 2, text: '上乗せは小さい', side: 'right' },
  ]);

  L.kpiTiles(s, [
    { value: '約65円', label: '株価が前提にするEPS\n(786円 × 資本コスト8.25%)' }, // lint-ok: 手本用の固定値
    { value: '約81円', label: '今の実力のEPS\n(2027年3月期・特別損益を除く)' }, // lint-ok: 手本用の固定値
    { value: '8.5% と 8.25%', label: '定常ROE と 株主資本コスト\n(ほぼ同じ = 成長は価値を生まない)' }, // lint-ok: 手本用の固定値
  ], { compact: true, x: 0.55, y: 5.42, w: 7.60, h: 1.26 });

  L.lookBox(s, [
    { n: 1, text: '差219円の約9割は、\n今の利益が続くだけで埋まる' },
    { n: 2, text: '成長の上乗せは約26円。\nROE が資本コストとほぼ同じため' },
    { n: 3, text: '株価は EPS が2割減る前提。\n問うべきは利益の持続性' },
  ], { x: 8.45, y: 2.02, w: 4.38, h: 3.22 });

  L.takeaway(s, 8.45, 5.42, 4.38, 1.26,
    '投資の本質は成長ではなく、今の利益が続くか。\n見るべきは第3四半期の粗利率', // lint-ok: 手本用の固定値
    { fontSize: 10.5 });
};
