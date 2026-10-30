// 資金と金利(指示書 spec/ch2a.md の s15 節どおり)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    title: '格付けはエンジンでも BBB- を保ち、FY29 に FCF 399 億ドル。CDS・社債は市場の評価で、調達コストには新発債の利回りで効く',
    kicker: '左: FCF と格付けの経路(需給エンジン、ベース)。右: 金利の経路と理論株価(株主資本コストも同じ前提で変える)',
    source: '需給エンジン第4.5版(calc/out/m10_*.json)、research2/R5_credit.md、research3/W4_rates.md',
    page: 15,
  });

  // 左: FCF の縦棒(赤字と黒字を系列に分け、該当しない年は 0)と格付けの帯
  L.paneHead(s, 0.5, 1.62, 6.3, 'FCF(10 億ドル)と格付け');
  const yrs = ['FY27', 'FY28', 'FY29', 'FY30', 'FY31', 'FY32'];
  s.addChart(pres.charts.BAR, [
    { name: '赤字', labels: yrs, values: [-48.4, -16.6, 0, 0, 0, 0] },
    { name: '黒字', labels: yrs, values: [0, 0, 39.9, 47.1, 44.6, 67.6] },
  ], L.chartStyle({
    x: 0.5, y: 1.95, w: 6.3, h: 3.1, objectName: 'chart',
    barDir: 'col', barGrouping: 'stacked', chartColors: [C.red, C.primary],
    dataLabelPosition: 'inEnd', dataLabelColor: C.white, dataLabelFormatCode: '0.0;-0.0;;',
    valAxisMinVal: -60, valAxisMaxVal: 80, valAxisMajorUnit: 20,
    showLegend: true, legendPos: 'b',
  }));
  L.table(s, [
    ['FY27', 'FY28', 'FY29', 'FY30', 'FY31', 'FY32'],
    ['BBB-', 'BBB-', 'BBB-', 'BBB', 'BBB+', 'BBB+'],
  ], { x: 0.5, y: 5.1, w: 6.3, colW: [1.05, 1.05, 1.05, 1.05, 1.05, 1.05], fontSize: 10, rowH: 0.34, align: ['center', 'center', 'center', 'center', 'center', 'center'] });
  L.text(s, 'S&P の格下げ条件: 調整後レバレッジ 4.5 倍超が続く、FY29 までに FOCF が黒字化しない、\nAI 戦略への否定的な見方。会社は FY28 下期の黒字化と FY29 の FCF 300 億ドル以上を約束。\nエンジンは FY29 に 399 億ドル', { x: 0.5, y: 5.85, w: 6.3, h: 0.8, fontSize: 9.5 });

  // 右: 金利の経路と理論株価
  L.paneHead(s, 7.05, 1.62, 5.78, '金利の経路と理論株価');
  L.table(s, [
    ['金利の経路', '株主資本\nコスト', '理論株価\n(加重)', 'DCF(加重)'],
    ['市場の曲線(ベース)', '10.63%', '245', '229'],
    ['予測どおり低下', '10.47%', '257', '264'],
    ['6.0% で高止まり', '11.61%', '235', '204'],
  ], { x: 7.05, y: 2.0, w: 5.78, colW: [2.38, 1.1, 1.15, 1.15], fontSize: 10, rowH: 0.45 });
  L.bullets(s, [
    'ベースは市場の利回り曲線で割り引く\n(2 年金利が FF 金利を上回り、市場は利上げも織り込む)',
    '利下げの見通しはシナリオとして示す。DCF は金利に敏感だが、\n年度別理論株価は近い年度が重いので動きが小さい',
    'CDS・社債のスプレッドは市場の評価で、本当のリスクは別に判断する。\n調達コストには新発債の利回りで効く(社債の金利 +1pt で FY30 EPS −0.44 ドル)',
  ], { x: 7.05, y: 3.95, w: 5.78, h: 1.6, fontSize: 10 });
  L.takeaway(s, 7.05, 5.65, 5.78, 0.95, 'どの金利の経路でも、理論株価は株価 139.56 ドルを 68% 以上上回る');
};
