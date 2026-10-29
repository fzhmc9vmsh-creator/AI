// 資金と信用(2/2): 貸倒と公正価値(指示書 spec/v4.md の s13 節)。型: 左にチャートと表・注、右に表・注・takeaway
// 折れ線は 2 グループ(主軸: 報告値・損失前提、第2軸・同じ目盛り: all-in。ラベルは all-in だけ)。破線は主軸グループ単位のため、報告値も破線になる
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 個人ローンの貸倒率(報告値・all-in)と公正価値の損失前提(年率、%)。右: 公正価値のマークと金利への感応度',
    source: '8-K・10-Q(Q2 2024〜Q2 2026)、research_r5/Q3_datasheet.md(Q3 2026 の 8-K 要約)、research_r2/R5_credit_fv.md',
  });

  // 左: 貸倒率と損失前提の折れ線(null は線を切る。Q3 26 の損失前提は未開示のため Q2 の値を延ばした)
  L.paneHead(s, 0.5, 1.62, 6.3, '個人ローンの貸倒率と損失前提(%)');
  const labels = ['Q2 24', 'Q3 24', 'Q4 24', 'Q1 25', 'Q2 25', 'Q3 25', 'Q4 25', 'Q1 26', 'Q2 26', 'Q3 26'];
  const axis = { valAxisMinVal: 0, valAxisMaxVal: 6 };
  s.addChart([
    { type: pres.charts.LINE, data: [
      { name: '報告値', labels, values: [3.84, 3.52, 3.37, 3.31, 2.83, 2.60, 2.80, 3.03, 2.62, 2.26] },
      { name: '公正価値の損失前提', labels, values: [4.8, null, 4.55, 4.37, 4.28, 4.33, 4.46, 4.57, 4.8, 4.8] },
    ], options: { showValue: false, lineDash: 'dash' } },
    { type: pres.charts.LINE, data: [
      { name: 'all-in(売却した延滞債権を足し戻し)', labels, values: [5.4, 5.0, null, 4.8, 4.5, null, 4.4, 4.4, 3.7, 3.4] },
    ], options: { showValue: true, secondaryValAxis: true, secondaryCatAxis: true, chartColors: [C.primary] } },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 6.3, h: 3.2, objectName: 'chart',
    showLegend: true, legendPos: 'b', chartColors: [C.teal, C.red, C.primary], lineSize: 2, lineDataSymbolSize: 6, displayBlanksAs: 'gap',
    dataLabelPosition: 't', dataLabelFormatCode: '0.0', ...axis,
    valAxes: [Object.assign({}, axis), Object.assign({ valAxisHidden: true }, axis)],
    catAxes: [{ catAxisLineShow: true }, { catAxisHidden: true }],
  }));
  L.text(s, '損失前提の Q3 は未開示(Q2 の 4.8% を延ばして表示)。all-in は会社の推計(Q3 2024 から開示)。空売り(Muddy Waters)の主張は約 6.1%。\n2022 年 Q4〜2025 年 Q3 組成の累積損失は 4.68%(残存元本 35%)で、2017 年組成の同時点 6.43% を下回る。借り手は FICO 746・年収 15.8 万ドル(Q4 2025。Q3 は未取得)', { x: 0.5, y: 5.3, w: 6.3, h: 1.35, fontSize: 9.5 });

  // 右: 公正価値のマークと感応度の表、注、結論(Q3 の評価損益・マーク・スワップは未開示)
  L.paneHead(s, 7.05, 1.62, 5.78, '公正価値のマークと金利');
  L.table(s, [
    ['', '個人ローン', '学生ローン'],
    ['残高(公正価値・Q3)', '約 321 億ドル', '約 185 億ドル'],
    ['マーク(Q3)', '未開示', '未開示'],
    ['割引率(2026-06 → 09)', '4.97 → 5.56%', '4.29 → 5.11%'],
    ['割引率 1bp あたりのマーク', '約 1.4〜2.0bp', '約 2.4〜3.3bp'],
    ['Q3 の評価損益・スワップ損益', '未開示', '未開示'],
  ], { x: 7.05, y: 1.98, w: 5.78, colW: [2.4, 1.69, 1.69], fontSize: 10, rowH: 0.42 });
  L.text(s, '割引率は Q3 に +59〜82bp 上がったが、EPS は上振れし通期見通しを引き上げた', { x: 7.05, y: 4.6, w: 5.78, h: 0.5, fontSize: 9 });
  L.takeaway(s, 7.05, 5.2, 5.78, 1.45, '損失の前提は実績より保守的。\nQ3 の金利上昇で割引率は大きく上がったが、\n利益の見通しは上がった。\n評価減とヘッジの額は Q3 の 8-K・10-Q で確かめる');
};
