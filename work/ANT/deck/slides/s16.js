// 2031年の姿: FCF の基準と弱気、2031 年の財務の 3 指標
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, { kicker: '道筋どおりなら現金の流れがどう変わるかを、基準と弱気の 2 本で比べる(数字は当分析モデルの推定)', source: '当分析の 5 か年コホートモデル、価値評価の計算機' });
  L.paneHead(s, 0.5, 1.62, 7.5, 'FCF の推移(百万ドル)', 'pane_l');
  s.addChart(pres.charts.BAR, [
    { name: '基準', labels: ['2027', '2028', '2029', '2030', '2031'], values: [7270, 20834, 39116, 56456, 75839] },
    { name: '弱気(確率 20%)', labels: ['2027', '2028', '2029', '2030', '2031'], values: [-5209, -8601, -8253, -1941, 6040] },
  ], L.chartStyle({ x: 0.5, y: 1.98, w: 7.5, h: 4.2, chartColors: [C.primary, 'C0392B'], showLegend: true, legendPos: 'b', barGapWidthPct: 50, valAxisMinVal: -20000, valAxisMaxVal: 90000, valAxisLabelFormatCode: '#,##0', dataLabelFormatCode: '#,##0', catAxisLabelPos: 'low', objectName: 'chart_fcf' }));
  L.kpiTiles(s, [
    { value: F('fcf.31', { noEst: true }), label: '2031 年の FCF\n(百万ドル)' },
    { value: F('opm.31', { noEst: true }), label: '2031 年の営業利益率' },
    { value: F('roe.31', { noEst: true }), label: '2031 年の ROE' },
  ], { compact: true, x: 8.25, y: 1.98, w: 4.58, h: 1.3 });
  L.lookBox(s, [
    { n: 1, text: '基準では支払い義務の 91.8% を消化し、現金を生む側に移る' },
    { n: 2, text: '弱気(確率 20%)では 4 年続けて FCF が赤字' },
    { n: 3, text: '最も変わる財務は、損益より現金の流れ' },
  ], { x: 8.25, y: 3.5, w: 4.58, h: 2.68 });
  L.termNotes(s, [{ term: 'ROE', plain: '純利益 ÷ 自己資本。株主のお金で稼ぐ力', why: '将来の資本の使い方を評価するため' }], { x: 0.5, y: 6.3, w: 12.33 });
};
