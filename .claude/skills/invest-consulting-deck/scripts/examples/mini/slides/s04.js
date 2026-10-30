// 収益の伸び: チャートの値は F.v() で台帳から引く
module.exports = function build(pres, L) {
  const { F } = L;
  const s = L.contentSlide(pres, { kicker: '手数料型の収益の比率を前の四半期と並べる', source: '台帳 facts.json(8-K・説明会の要約)' });
  s.addChart(pres.charts.BAR, [{ name: '手数料型の比率(%)', labels: ['Q2 2026', 'Q3 2026'], values: [F.v('q2.fee_share'), F.v('q3.fee_share')] }],
    Object.assign(L.chartStyle({ dataLabelFormatCode: '0' }), { x: 0.5, y: 1.75, w: 6.5, h: 4.2, objectName: 'chart_fee' }));
  L.takeaway(s, 7.4, 1.75, 5.43, 1.6, `比率は ${F('q2.fee_share')} から ${F('q3.fee_share')} へ。\n手数料型の収益は前年比 +${F.n('q3.fee_yoy')}%`);
};
