// 利益率の将来(指示書 spec/ch2a.md の s10 節どおり。見本 examples.js の exChart を写し、値・文字・右下の表を差し替え)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, { title: '全社の営業利益率は AI の比率上昇で FY29 に 31% まで下がり、AI 事業内の改善で FY32 に 34% へ戻る。オーナー利益のルール・オブ・40 は 46〜76', kicker: '事業実態の営業利益率(株式報酬を費用に含む。GAAP の Q1 は 34.8%、非GAAP は 42%)と AI 事業の利益率、%', source: '需給エンジン第4.3版(calc/model8.py)', page: 10 });
  const yrs = ['FY27', 'FY28', 'FY29', 'FY30', 'FY31', 'FY32'];
  L.chartPanel(pres, s, { type: pres.charts.LINE, data: [
    { name: '全社の営業利益率', labels: yrs, values: [33.3, 32.9, 31.0, 32.7, 33.5, 34.1] },
    { name: 'AI 事業の営業利益率', labels: yrs, values: [10.5, 22.1, 22.6, 27.6, 29.3, 30.4] },
  ], opts: { showLegend: true, legendPos: 'b', chartColors: [C.dark, C.light], lineSize: 2, dataLabelPosition: 't', dataLabelFormatCode: '0.0', valAxisMinVal: 0, valAxisMaxVal: 40 } },
  { takeawayText: '利益率の低下は構成の変化(AI の売上比率\n30% → 66%)によるもので、\nAI 事業そのものは稼働の成熟で改善する' });

  L.table(s, [
    ['年度', '売上成長', 'R40(FCF)', 'R40(オーナー)'],
    ['FY28', '43%', '18', '76'],
    ['FY29', '34%', '27', '67'],
    ['FY30', '29%', '46', '64'],
    ['FY31', '17%', '40', '51'],
    ['FY32', '12%', '26', '46'],
  ], { x: 9.05, y: 3.25, w: 3.78, colW: [0.78, 0.9, 0.95, 1.15], fontSize: 10, rowH: 0.34 });

  L.text(s, 'R40 = 売上成長率 + 利益率。オーナー = オーナー利益(EBITDA − 維持投資 − 現金税)。償却費は将来の現金支出ではないため、\n維持投資で置き換えた', { x: 9.05, y: 5.45, w: 3.78, h: 1.1, fontSize: 8.5, color: C.sub, objectName: 'note' });
  return s;
};
