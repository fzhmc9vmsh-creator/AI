// 手数料型の収益(Q3 2026。新規。手本: slides/s14.js の表 + 右チャート、組み合わせ図は s13 の作り)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '手数料型の収益(会社定義、非 GAAP): 組成手数料・LPB・交換手数料・証券・紹介・Plus・Tech Platform の手数料。比率は調整後純収益に対する割合',
    source: 'research_r5/Q3_datasheet.md §1-2(R19)、Q3 の 8-K・説明会の要約',
  });
  const green = (t) => ({ text: t, options: { color: C.primary, bold: true } });

  // 左上: 四半期の表。最新の Q3 26 の行は緑の太字
  L.paneHead(s, 0.5, 1.62, 6.3, '手数料型の収益と比率(四半期)');
  L.table(s, [
    ['四半期', '手数料型の収益', '前期比', '前年比', '比率'],
    ['Q3 25', '4.09 億', '+8%', '+50%', '43%'],
    ['Q4 25', '4.43 億', '+8%', '+53%', '44%'],
    ['Q1 26', '3.87 億', '−13%', '+23%', '36%'],
    ['Q2 26', '4.72 億', '+22%', '+25%', '39%'],
    [green('Q3 26'), green('5.71 億'), green('+21%'), green('+40%'), green('42%')],
  ], { x: 0.5, y: 1.98, w: 6.3, colW: [1.2, 1.7, 1.13, 1.13, 1.14], fontSize: 10, rowH: 0.3 });

  // 左下: Q3 の担い手(数字は四半期の表と同じ出所)
  L.paneHead(s, 0.5, 4.0, 6.3, 'Q3 26 の担い手');
  L.table(s, [
    ['担い手', '数字'],
    ['組成手数料(Lending)', '+158%(前年比)'],
    ['LPB', '1.53 億ドル(組成 36 億、手数料率 4.3%)'],
    ['交換手数料(FS)', '+77%(年換算の決済額 310 億ドル)'],
    ['Tech Platform', '0.87 億ドル(大口を除き +18%)'],
    ['証券・Plus・紹介', '未開示'],
  ], { x: 0.5, y: 4.3, w: 6.3, colW: [2.2, 4.1], fontSize: 9.5, rowH: 0.3, align: ['left', 'left'] });

  // 右: 縦棒(手数料型の収益、億ドル)と折れ線(比率、%)。折れ線は第 2 軸で、棒の上に浮かせる
  L.paneHead(s, 7.05, 1.62, 5.78, '手数料型の収益(億ドル、棒)と比率(%、線)');
  const labels = ['Q3 25', 'Q4 25', 'Q1 26', 'Q2 26', 'Q3 26'];
  // 軸は消さず(delete にすると第 2 軸の線が描かれない)、目盛りの文字だけを出さない
  const axis = { valAxisLabelPos: 'none', valGridLine: { style: 'none' } };
  s.addChart([
    { type: pres.charts.BAR, data: [
      { name: '手数料型の収益(億ドル)', labels, values: [4.09, 4.43, 3.87, 4.72, 5.71] },
    ], options: { chartColors: [C.primary], dataLabelPosition: 'outEnd', dataLabelFormatCode: '0.00' } },
    { type: pres.charts.LINE, data: [
      { name: '比率(%)', labels, values: [43, 44, 36, 39, 42] },
    ], options: { chartColors: [C.amber], secondaryValAxis: true, secondaryCatAxis: true, showValue: true,
      dataLabelPosition: 't', dataLabelFormatCode: '0"%"' } },
  ], L.chartStyle({
    x: 7.05, y: 1.98, w: 5.78, h: 3.5, objectName: 'chart',
    showLegend: true, legendPos: 'b', lineSize: 2, lineDataSymbolSize: 7,
    valAxes: [Object.assign({ valAxisMinVal: 0, valAxisMaxVal: 9 }, axis), Object.assign({ valAxisMinVal: 0, valAxisMaxVal: 50 }, axis)],
    catAxes: [{ catAxisLineShow: true }, { catAxisHidden: true }],
  }));

  // 右下: takeaway
  L.takeaway(s, 7.05, 5.65, 5.78, 1.0, '比率は Q1 の 36% を底に 42% へ。\nLPB の配分(29%)ではなく、組成手数料と\n交換手数料の多様化で上がった。資本を使わない収益が伸びる');
};
