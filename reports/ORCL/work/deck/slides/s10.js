// 利益率の将来(指示書 spec/ch2a.md の s10 節どおり。見本 examples.js の exChart を写し、値・文字・右下の表を差し替え)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, { title: '全社の営業利益率は立ち上げ中の AI で FY28 に 33% へ下がり、FY29〜30 に 35% で並ぶ。非GAAP は 37% で目標 40% に 3pt 届かない', kicker: '全社の営業利益率(GAAP 相当)と AI 事業の営業利益率、FY27〜32、%', source: '需給エンジン第4.5版(calc/out/m10_*.json)', page: 10 });
  const yrs = ['FY27', 'FY28', 'FY29', 'FY30', 'FY31', 'FY32'];
  L.chartPanel(pres, s, { type: pres.charts.LINE, data: [
    { name: '全社の営業利益率(GAAP 相当)', labels: yrs, values: [34.2, 33.3, 34.7, 34.8, 34.1, 33.3] },
    { name: 'AI 事業の営業利益率', labels: yrs, values: [18, 26.4, 31.3, 31.9, 30.8, 29.7] },
  ], opts: { showLegend: true, legendPos: 'b', chartColors: [C.dark, C.light], lineSize: 2, dataLabelPosition: 't', dataLabelFormatCode: '0.0', valAxisMinVal: 0, valAxisMaxVal: 40 } },
  { takeawayText: 'FY27〜28 は立ち上げ中の AI\n(利益率 18〜26%)が全社を押し下げ、\nFY29〜30 に 35% で並ぶ。\n非GAAP は 37% で会社の 40% より 3pt 低い' });

  L.table(s, [
    ['年度', '売上成長', 'R40(FCF)', 'R40(オーナー)'],
    ['FY28', '54%', '42', '83'],
    ['FY29', '36%', '57', '69'],
    ['FY30', '16%', '37', '50'],
    ['FY31', '13%', '30', '46'],
    ['FY32', '13%', '37', '45'],
  ], { x: 9.05, y: 3.25, w: 3.78, colW: [0.78, 0.9, 0.95, 1.15], fontSize: 10, rowH: 0.34 });

  L.text(s, 'R40 = 売上成長率 + 利益率。オーナー = オーナー利益(EBITDA − 維持投資 − 現金税)。償却費は将来の現金支出ではないため、\n維持投資で置き換えた', { x: 9.05, y: 5.45, w: 3.78, h: 1.1, fontSize: 8.5, color: C.sub, objectName: 'note' });
  return s;
};
