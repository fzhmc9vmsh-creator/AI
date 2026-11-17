// 収益の伸び: チャートの値は F.v() で台帳から引く。棒グラフの軸は 0 から(軸を切ると差が大げさに見える)
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, { kicker: '手数料型の収益の比率と主要な数字を、前の四半期と並べる', source: '台帳 facts.json(8-K・説明会の要約)' });
  L.paneHead(s, 0.5, 1.62, 6.5, '手数料型の収益の比率(%)', 'pane_chart');
  s.addChart(pres.charts.BAR, [{ name: '手数料型の比率', labels: ['Q2 2026', 'Q3 2026'], values: [F.v('q2.fee_share'), F.v('q3.fee_share')] }],
    L.chartStyle({ x: 0.5, y: 1.98, w: 6.5, h: 4.4, chartColors: [C.primary], valAxisMinVal: 0, valAxisMaxVal: 50, barGapWidthPct: 80, objectName: 'chart_fee' }));
  // 列の見出しに時点があるので、セルでは時点ラベルを外す(noPeriod)
  L.table(s, [
    ['項目', 'Q2 2026', 'Q3 2026'],
    ['手数料型の比率', F('q2.fee_share', { noPeriod: true }), F('q3.fee_share')],
    ['販促費', F('q2.sm', { noPeriod: true }), F('q3.sm')],
    ['希薄化後 EPS', F('q2.eps', { noPeriod: true }), F('q3.eps')],
    ['会員数', F('q2.members', { noPeriod: true }), F('q3.members')],
    ['総自己資本比率', F('q2.tcr', { noPeriod: true }), F('q3.tcr')],
  ], { x: 7.4, y: 1.98, w: 5.43, colW: [2.03, 1.7, 1.7], fontSize: 10.5, rowH: 0.38 });
  L.takeaway(s, 7.4, 4.5, 5.43, 1.6, `比率は ${F('q2.fee_share')} から ${F('q3.fee_share')} へ。手数料型の収益は前年比 +${F.n('q3.fee_yoy')}% で、\n資本を使わない収益が伸びた`);
};
