// 利益率の将来(指示書 spec/ch2a.md の s10 節どおり。見本 examples.js の exChart を写し、値・文字・右下の表を差し替え)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, { title: '全社の営業利益率は立ち上げ中の AI で FY28 に 31% へ下がり、FY29 に 36% へ戻る。非GAAP の FY30 は 38% で目標 40% に届かない', kicker: '全社の営業利益率(GAAP 相当)と AI 事業の営業利益率、FY27〜32、%', source: '需給エンジン第4.4版(calc/out/m9_more.json)', page: 10 });
  const yrs = ['FY27', 'FY28', 'FY29', 'FY30', 'FY31', 'FY32'];
  L.chartPanel(pres, s, { type: pres.charts.LINE, data: [
    { name: '全社の営業利益率(GAAP 相当)', labels: yrs, values: [31.9, 31.2, 35.8, 35.2, 33.3, 33.4] },
    { name: 'AI 事業の営業利益率', labels: yrs, values: [13, 23, 33.1, 32.0, 29.0, 29.4] },
  ], opts: { showLegend: true, legendPos: 'b', chartColors: [C.dark, C.light], lineSize: 2, dataLabelPosition: 't', dataLabelFormatCode: '0.0', valAxisMinVal: 0, valAxisMaxVal: 40 } },
  { takeawayText: 'FY27〜28 は立ち上げ中の AI\n(利益率 13〜23%)が全社を押し下げ、\nFY29 に満稼働で 36% に戻る。\n非GAAP では FY30 37.7% で\n会社の 40% に届かない' });

  L.table(s, [
    ['年度', '売上成長', 'R40(FCF)', 'R40(オーナー)'],
    ['FY28', '59%', '59', '91'],
    ['FY29', '31%', '66', '67'],
    ['FY30', '6%', '28', '41'],
    ['FY31', '12%', '27', '45'],
    ['FY32', '16%', '16', '48'],
  ], { x: 9.05, y: 3.25, w: 3.78, colW: [0.78, 0.9, 0.95, 1.15], fontSize: 10, rowH: 0.34 });

  L.text(s, 'R40 = 売上成長率 + 利益率。オーナー = オーナー利益(EBITDA − 維持投資 − 現金税)。償却費は将来の現金支出ではないため、\n維持投資で置き換えた', { x: 9.05, y: 5.45, w: 3.78, h: 1.1, fontSize: 8.5, color: C.sub, objectName: 'note' });
  return s;
};
