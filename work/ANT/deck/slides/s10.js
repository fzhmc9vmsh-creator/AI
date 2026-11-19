// s10 資本の構造: Q3 末と公開後の現金・自己資本(棒)、貸借の表、見るところ
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, { source: 'S-1/A-3 の見込みの貸借対照表' });

  L.paneHead(s, 0.5, 1.62, 7.6, 'Q3 末と公開後の姿(百万ドル)', 'pane_chart_head');
  s.addChart(pres.charts.BAR, [
    { name: 'Q3 実績', labels: ['現金', '自己資本'], values: [131845, -149873] },
    { name: '公開後', labels: ['現金', '自己資本'], values: [215650, 221928] },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 7.6, h: 2.45,
    showLegend: true, legendPos: 't',
    valAxisMinVal: -200000, valAxisMaxVal: 300000, valAxisMajorUnit: 100000,
    valAxisLabelFormatCode: '#,##0', dataLabelFormatCode: '#,##0',
    barGapWidthPct: 70,
    chartColors: [C.sub, C.primary],
    objectName: 'chart_capital',
  }));

  L.table(s, [
    ['項目(百万ドル)', 'Q3 実績', '公開後'],
    ['現預金', '131,845', '215,650'],
    ['総資産', '154,294', '238,099'],
    ['転換社債', '130,502', '0(資本へ)'],
    ['自己資本', '−149,873', '221,928'],
    ['1 株純資産', '—', '12.32 ドル'],
  ], { x: 0.5, y: 4.6, w: 7.6, colW: [3.2, 2.2, 2.2], fontSize: 10.5, rowH: 0.3, name: 'tbl_capital' });

  L.lookBox(s, [
    { text: '債務超過は Amazon の転換社債を負債に置き、公開前の資本の組み入れが無いため' },
    { text: `転換後は 1 株純資産 ${F('bps.pf')}` },
    { text: '資本の大半は現金で、計算資源の支払い義務(p.9)に備える' },
  ], { x: 8.4, y: 1.98, w: 4.43, h: 3.2, name: 'look' });
};
