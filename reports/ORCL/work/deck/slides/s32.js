// 5 年 EPS 推移 T7(指示書 spec/ch1_ch4a.md の s32 節)
// 注: pptxgenjs はデータラベルの表示を系列ごとに変えられないため、強気・弱気を別の折れ線グループ(第2軸、同じ目盛り・非表示)に載せ、
//     ベースだけラベルを出す。FY27〜28 で3系列のラベルが重なるための措置(指示書の「強気と弱気だけ showValue:false」と同じ見た目)。
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    title: '事業実態 EPS は会社の見通しの経路で 6.9 ドルから FY32 に 27 ドルへ年 31% 伸びる。弱気は FY31 に OpenAI の再販で落ち込む',
    kicker: '事業実態 EPS(非GAAP EPS − 株式報酬の税引後)、ドル。FY27〜30 は会社の見通し(FY27 8.10・FY30 21)× シナリオ比、FY31〜32 は需給エンジンの伸びで延長',
    source: 'Investor Day 2026-10-28、コンセンサス(research5/U2)、需給エンジン第4.5版(calc/out/m10_*.json)。過去の成長率は使っていない',
    page: 32,
  });
  const labels = ['FY27', 'FY28', 'FY29', 'FY30', 'FY31(延長)', 'FY32(延長)'];
  const axis = { valAxisMinVal: 0, valAxisMaxVal: 40 };
  s.addChart([
    { type: pres.charts.LINE, data: [
      { name: '強気', labels, values: [7.04, 11.07, 17.41, 22.78, 27.22, 34.06] },
      { name: '弱気', labels, values: [6.69, 9.94, 11.78, 13.61, 10.01, 10.48] },
    ], options: { showValue: false } },
    { type: pres.charts.LINE, data: [
      { name: 'ベース', labels, values: [6.89, 10.62, 15.89, 19.60, 22.81, 26.63] },
    ], options: { showValue: true, secondaryValAxis: true, secondaryCatAxis: true, chartColors: [L.C.primary, L.C.primary, L.C.primary] } },
  ], L.chartStyle({
    x: L.M, y: 1.65, w: 8.35, h: 5.0, objectName: 'chart',
    showLegend: true, legendPos: 'b', chartColors: [L.C.light, L.C.red, L.C.primary], lineSize: 2, lineDataSymbolSize: 6,
    dataLabelPosition: 't', dataLabelFormatCode: '0.0', ...axis,
    valAxes: [Object.assign({}, axis), Object.assign({ valAxisHidden: true }, axis)],
    catAxes: [{ catAxisLineShow: true }, { catAxisHidden: true }],
  }));
  L.takeaway(s, 9.05, 1.7, 3.78, 1.35, 'ベースの 5 年 CAGR は 31.0%(PEG 0.65)。\n説明会前のコンセンサス(FY28 10.99・\nFY29 15.77)は会社の経路より 7〜8% 低い');
  L.bullets(s, [
    'FY27→FY30 は会社の見通しを起点に置いた。\nコンセンサスは説明会の前の値で遅れている',
    '弱気の FY31: OpenAI 向けとみなす容量の 6 割を、需給緩和後の相場で再販して 10.0 ドルへ下がる',
    'FY31・32 は延長部分で、\n確度は FY27〜30 より低い',
  ], { x: 9.05, y: 3.2, w: 3.78, h: 3.45, fontSize: 10.5, name: 'points' });
};
