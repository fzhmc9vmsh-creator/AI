// 増収の内訳と利益率の経路(Q3 2026。タイトル・ページ番号は meta.js が入れる)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 前年比の増収の内訳(Q3 2025 → Q3 2026、百万ドル)。右: 利益率の経路(事業エンジン)と、2027 年の見通しが求めるもの',
    source: '会社の Q3 2026 決算・2027 年見通し(8-K・説明会の要約)、research_r5/Q3_datasheet.md §1、calc/out/growth_v4.json(エンジン)',
  });

  // 左: 増収の内訳。NII と非金利収益に分ける(両方の和が前年比の増収 4.24 億ドルに一致する)。最後の棒は合計
  L.paneHead(s, 0.5, 1.62, 6.3, '増収の内訳(前年比、百万ドル)');
  s.addChart(pres.charts.BAR, [
    { name: '前年比の増加(百万ドル)', labels: ['純金利収益(NII)', '非金利収益', '増収の合計'], values: [345, 79, 424] },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 6.3, h: 2.9, objectName: 'chart',
    barDir: 'bar', chartColors: [C.primary, C.light, C.dark],
    catAxisOrientation: 'maxMin', catAxisLabelPos: 'low',
    valAxisHidden: true, valGridLine: { style: 'none' }, valAxisMinVal: 0, valAxisMaxVal: 480,
    dataLabelPosition: 'outEnd', dataLabelColor: C.text, dataLabelFormatCode: '+0;-0;;',
    showLegend: false,
  }));
  L.text(s, '前年比の増収 4.24 億ドルの 81% は NII(利ざや)。\n非金利収益は、手数料・売却益・評価の純額', {
    x: 0.5, y: 4.95, w: 6.3, h: 0.5, fontSize: 9.5, objectName: 'note',
  });
  L.takeaway(s, 0.5, 5.6, 6.3, 1.1, '2027 年は収益 +27% に対し純利益 +52%。\n販促費率を大きく下げずに、規模で利益率を上げる計画。\nただし B/S の伸びは資本が律速する');

  // 右上: 利益率の経路(事業エンジン)。行の高さは 0.3
  L.paneHead(s, 7.05, 1.62, 5.78, '利益率の経路(事業エンジン)');
  L.table(s, [
    ['年', '販促費率', '税引前利益率', 'ROTCE'],
    ['2026', '32.0%', '21.5%', '8.4%'],
    ['2027', '30.0%', '25.6%', '11.7%'],
    ['2028', '28.5%', '28.7%', '13.1%'],
    ['2029', '27.0%', '31.5%', '14.3%'],
    ['2030', '25.5%', '33.9%', '15.2%'],
  ], { x: 7.05, y: 1.98, w: 5.78, colW: [1.2, 1.5, 1.6, 1.48], fontSize: 10, rowH: 0.3 });

  // 右下: 2027 年の見通しが求めるもの
  L.paneHead(s, 7.05, 3.98, 5.78, '2027 年の見通しが求めるもの');
  L.table(s, [
    ['項目', '2026 年', '2027 年'],
    ['調整後純収益', '50.4 億', '64 億(+27%)'],
    ['EBITDA(率)', '16.6 億(33%)', '22.4 億(35%)'],
    ['純利益', '約 8.4 億', '12.8 億(+52%)'],
    ['EPS', '0.61', '0.90(+48%)'],
    ['暗黙の株数', '13.8 億', '14.2 億(+3%)'],
  ], { x: 7.05, y: 4.3, w: 5.78, colW: [2.2, 1.6, 1.98], fontSize: 10, rowH: 0.3 });
};
