// s24 価値を動かす変数: 適正株価からの増減(トルネード・横棒)と見るところ
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, { source: '当分析の価値評価の感応度' });

  L.paneHead(s, 0.5, 1.62, 8.2, `基準の適正株価 ${F('fair')} からの増減(1 株あたり、ドル)`, 'pane_tornado_head');

  const labels = [
    '実質の粗利率 −8pt',
    '研究開発費の比率 +5pt',
    '資本コスト +1%(統治)',
    '実質の粗利率 −4pt',
    '実質の粗利率 +4pt',
    '株数の増加 +4%/年',
  ];
  // 赤(最大の下振れ)・灰(その他の下振れ)・濃緑(上振れ)の系列に分けて積み上げる(他の系列は 0。ラベルは 0 を隠す)
  s.addChart(pres.charts.BAR, [
    { name: '最大の下振れ', labels, values: [-11.3, 0, 0, 0, 0, 0] },
    { name: 'その他の下振れ', labels, values: [0, -6.7, -5.7, -5.4, 0, -4.4] },
    { name: '上振れ', labels, values: [0, 0, 0, 0, 5.3, 0] },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 8.2, h: 4.6,
    barDir: 'bar', barGrouping: 'stacked', catAxisOrientation: 'maxMin', catAxisLabelPos: 'low',
    valAxisMinVal: -14, valAxisMaxVal: 8, valAxisMajorUnit: 2, valAxisLabelFormatCode: '+0;-0;0',
    dataLabelFormatCode: '+0.0;-0.0;', dataLabelPosition: 'ctr', dataLabelColor: C.white,
    barGapWidthPct: 50,
    chartColors: [C.red, C.sub, C.primary],
    objectName: 'chart_tornado',
  }));

  L.lookBox(s, [
    { text: '1 位の実質の粗利率は 2 位の約 1.7 倍' },
    { text: '振れ幅の大きさの順と、確率を掛けた期待損失の順(p.17、1 位は需要の減速)は違う' },
    { text: 'だから見張るのは「実質の粗利率」と「年換算売上の月次の伸び」の 2 本' },
  ], { x: 9.05, y: 1.98, w: 3.78, h: 4.2, name: 'look' });
};
