// 5 年 EPS 推移 T7(指示書 spec/ch1_ch4a.md の s32 節)
// 注: pptxgenjs はデータラベルの表示を系列ごとに変えられないため、強気・弱気を別の折れ線グループ(第2軸、同じ目盛り・非表示)に載せ、
//     ベースだけラベルを出す。FY27〜28 で3系列のラベルが重なるための措置(指示書の「強気と弱気だけ showValue:false」と同じ見た目)。
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    title: '事業実態 EPS はコンセンサス経路で 6.9 ドルから FY32 に 29 ドルへ年 34% 伸びる。弱気は FY31 に OpenAI の再販で落ち込む',
    kicker: '事業実態 EPS(非GAAP EPS − 株式報酬の税引後)、ドル。FY27〜30 はコンセンサス × シナリオ比、FY31〜32 は需給エンジンの伸びで延長',
    source: 'コンセンサス(research4/T1_consensus.csv)、需給エンジン第4.3版(calc/out/m8_fair.json)。過去の成長率は使っていない',
    page: 32,
  });
  const labels = ['FY27', 'FY28', 'FY29', 'FY30', 'FY31(延長)', 'FY32(延長)'];
  const axis = { valAxisMinVal: 0, valAxisMaxVal: 40 };
  s.addChart([
    { type: pres.charts.LINE, data: [
      { name: '強気', labels, values: [7.01, 10.00, 16.00, 22.95, 29.61, 37.43] },
      { name: '弱気', labels, values: [6.64, 9.10, 10.31, 12.12, 8.63, 8.67] },
    ], options: { showValue: false } },
    { type: pres.charts.LINE, data: [
      { name: 'ベース', labels, values: [6.85, 9.65, 14.42, 19.07, 24.33, 29.48] },
    ], options: { showValue: true, secondaryValAxis: true, secondaryCatAxis: true, chartColors: [L.C.primary, L.C.primary, L.C.primary] } },
  ], L.chartStyle({
    x: L.M, y: 1.65, w: 8.35, h: 5.0, objectName: 'chart',
    showLegend: true, legendPos: 'b', chartColors: [L.C.light, L.C.red, L.C.primary], lineSize: 2, lineDataSymbolSize: 6,
    dataLabelPosition: 't', dataLabelFormatCode: '0.0', ...axis,
    valAxes: [Object.assign({}, axis), Object.assign({ valAxisHidden: true }, axis)],
    catAxes: [{ catAxisLineShow: true }, { catAxisHidden: true }],
  }));
  L.takeaway(s, 9.05, 1.7, 3.78, 1.35, 'ベースの 5 年 CAGR は 33.9%(PEG 0.62)。\nFY30 の非GAAP EPS はコンセンサス\n20.5 ドルで、会社目標 21 ドルとほぼ同じ');
  L.bullets(s, [
    'FY27→FY30 の 3 年は、どのシナリオでも\nコンセンサス × シナリオ比で置いた',
    '弱気の FY31: OpenAI 向けとみなす容量の 6 割を、需給緩和後の相場で再販して 8.6 ドルへ下がる',
    'FY31・32 は延長部分で、\n確度は FY27〜30 より低い',
  ], { x: 9.05, y: 3.2, w: 3.78, h: 3.45, fontSize: 10.5, name: 'points' });
};
