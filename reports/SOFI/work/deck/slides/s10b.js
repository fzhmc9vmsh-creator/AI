// EPS の四半期分解(Q3 2026。手本の配置: 左の表 + 右のチャート。横棒の負値と点ごとの色は s10b の作り)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 四半期の収益・税引前利益・税率・株数・EPS(GAAP、百万ドル・百万株・ドル)。右: 純利益の前期比の増分の源泉(Q2 26 → Q3 26、百万ドル。その他・税は残差で推定)',
    source: '会社の 10-Q・8-K の要約(research_r5/Q3_datasheet.md §1、research_r4/R14_quarterly_eps_drivers.md)、calc/A4_q3_memo.md',
  });

  // 左上: 四半期の表。実効税率は 6.2・6.4% を灰、16.4・23.4% をアンバーの字。税引前 ÷ 株数は緑の太字。Q3 26 の未開示は灰
  const grey = (t) => ({ text: t, options: { color: C.sub } });
  const amber = (t) => ({ text: t, options: { color: C.amber } });
  const green = (t) => ({ text: t, options: { color: C.primary, bold: true } });
  L.table(s, [
    ['四半期', '収益', '税引前', '税引前利益率', '実効税率', '希薄化後株数', 'EPS', '税引前 ÷ 株数'],
    ['Q2 25', '855', '112', '13.1%', '13.3%', '1,183', '0.082', green('0.095')],
    ['Q3 25', '962', '149', '15.4%', grey('6.2%'), '1,291', '0.108', green('0.115')],
    ['Q4 25', '1,027', '185', '18.0%', grey('6.4%'), '1,346', '0.129', green('0.138')],
    ['Q1 26', '1,100', '200', '18.1%', amber('16.4%'), '1,378', '0.121', green('0.145')],
    ['Q2 26', '1,219', '204', '16.8%', amber('23.4%'), '1,352', '0.116', green('0.151')],
    ['Q3 26', '1,385', grey('未開示'), grey('未開示'), grey('未開示'), grey('推定 13.4〜13.8 億'), '0.18', grey('—')],
  ], { x: 0.5, y: 1.62, w: 8.3, colW: [0.9, 0.85, 0.85, 1.1, 1.0, 1.6, 0.8, 1.2], fontSize: 9, rowH: 0.34 });

  // 左下: 税・株数・EPS の読み
  L.bullets(s, [
    '税と株数: Q3 は未開示(逆算で税率 20〜25%、\n株数 13.4〜13.8 億株)。通期の税率の前提は 22%(7/29 時点)',
    'EPS 0.18 は前期比 +50%(丸めた 0.12 基準)、\n前年比 +67%(Q3 25 は 0.108)',
    '2027 年見通しの EPS 0.90 は純利益 12.8 億 ÷ 14.2 億株',
  ], { x: 0.5, y: 4.4, w: 8.3, h: 2.2, fontSize: 10.5, name: 'bullets', gap: 6 });

  // 右: 純利益の前期比の増分の源泉(横棒の 1 系列。点ごとの色: 増収・NII は緑、費用は赤、純利益は濃緑)
  L.paneHead(s, 9.05, 1.62, 3.78, '純利益の前期比の増分(百万ドル)');
  s.addChart(pres.charts.BAR, [
    { name: '純利益の前期比の増分(百万ドル)', labels: ['NII', '非金利収益', '販促費', '技術・製品開発', 'その他・税(推定)', '純利益'], values: [141, 25, -52, -6, -24, 84] },
  ], L.chartStyle({
    x: 9.05, y: 1.98, w: 3.78, h: 3.0, objectName: 'chart',
    barDir: 'bar', chartColors: [C.primary, C.primary, C.red, C.red, C.red, C.dark],
    catAxisOrientation: 'maxMin', catAxisLabelPos: 'low',
    valAxisHidden: true, valGridLine: { style: 'none' }, valAxisMinVal: -80, valAxisMaxVal: 170,
    dataLabelPosition: 'outEnd', dataLabelColor: C.text, dataLabelFormatCode: '+0;-0;0',
    showLegend: false,
  }));

  // 右下: takeaway
  L.takeaway(s, 9.05, 5.1, 3.78, 1.55, 'EPS は販促費を削らず、増収(NII)で\n作られた。調整弁は販促費ではなく、\nB/S の伸び(資本)');
};
