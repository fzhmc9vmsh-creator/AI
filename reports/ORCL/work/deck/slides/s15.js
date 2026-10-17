// 資金と金利(指示書 spec/ch2a.md の s15 節どおり)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    title: 'エンジンでは FY29〜30 に BB+ だが、S&P とコンセンサスは FY29 黒字。金利が下がれば 265 ドル、6% で高止まりでも 242 ドルで株価を上回る',
    kicker: '左: FCF と格付けの経路(需給エンジン、ベース)。右: 金利の経路と理論株価(株主資本コストも同じ前提で変える)',
    source: '需給エンジン第4.3版(calc/out/m8_all.json・m8_extra.json)、research2/R5_credit.md、research3/W4_rates.md',
    page: 15,
  });

  // 左: FCF の縦棒(赤字と黒字を系列に分け、該当しない年は 0)と格付けの帯
  L.paneHead(s, 0.5, 1.62, 6.3, 'FCF(10 億ドル)と格付け');
  const yrs = ['FY27', 'FY28', 'FY29', 'FY30', 'FY31', 'FY32'];
  s.addChart(pres.charts.BAR, [
    { name: '赤字', labels: yrs, values: [-34.2, -34.0, -13.5, 0, 0, 0] },
    { name: '黒字', labels: yrs, values: [0, 0, 0, 39.0, 64.1, 43.1] },
  ], L.chartStyle({
    x: 0.5, y: 1.95, w: 6.3, h: 3.1, objectName: 'chart',
    barDir: 'col', barGrouping: 'stacked', chartColors: [C.red, C.primary],
    dataLabelPosition: 'inEnd', dataLabelColor: C.white, dataLabelFormatCode: '0.0;-0.0;;',
    valAxisMinVal: -40, valAxisMaxVal: 80, valAxisMajorUnit: 20,
    showLegend: true, legendPos: 'b',
  }));
  const amber = { color: C.amber, bold: true };
  L.table(s, [
    ['FY27', 'FY28', 'FY29', 'FY30', 'FY31', 'FY32'],
    ['BBB-', 'BBB-', { text: 'BB+', options: amber }, { text: 'BB+', options: amber }, 'BBB-', 'BBB'],
  ], { x: 0.5, y: 5.1, w: 6.3, colW: [1.05, 1.05, 1.05, 1.05, 1.05, 1.05], fontSize: 10, rowH: 0.34, align: ['center', 'center', 'center', 'center', 'center', 'center'] });
  L.text(s, 'S&P の格下げ条件: 調整後レバレッジ 4.5 倍超が続く、FY29 までに FOCF が黒字化しない、\nAI 戦略への否定的な見方。S&P の基本シナリオとコンセンサスは FY29 に黒字\n(エンジンとの差は capex の水準)', { x: 0.5, y: 5.85, w: 6.3, h: 0.8, fontSize: 9.5 });

  // 右: 金利の経路と理論株価
  L.paneHead(s, 7.05, 1.62, 5.78, '金利の経路と理論株価');
  L.table(s, [
    ['金利の経路', '株主資本\nコスト', '理論株価\n(加重)', 'DCF(加重)'],
    ['市場の曲線(ベース)', '10.77%', '251', '231'],
    ['予測どおり低下(5.2 → 4.2%)', '10.43%', '265', '275'],
    ['6.0% で高止まり', '11.57%', '242', '209'],
  ], { x: 7.05, y: 2.0, w: 5.78, colW: [2.38, 1.1, 1.15, 1.15], fontSize: 10, rowH: 0.45 });
  L.bullets(s, [
    'ベースは市場の利回り曲線で割り引く\n(2 年 4.85% が FF 3.75〜4.00% を上回り、市場は利上げも織り込む)',
    '利下げの見通しはシナリオとして示す。DCF は金利に敏感だが、\n年度別理論株価は近い年度が重いので動きが小さい',
    '10 年金利は 2026 年 10 月初めに約 5.3%(2002 年以来の高値)。足元の金利は\n歴史的に低くない',
  ], { x: 7.05, y: 3.95, w: 5.78, h: 1.6, fontSize: 10 });
  L.takeaway(s, 7.05, 5.65, 5.78, 0.95, 'どの金利の経路でも、理論株価は株価 143 ドルを 68% 以上上回る');
};
