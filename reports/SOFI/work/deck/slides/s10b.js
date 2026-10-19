// EPS の四半期分解(指示書 spec/v3.md の s10b 節。新規。手本: slides/s14.js の左表 + 右チャート、横棒の負値は s10.js、点ごとの色は s31.js)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 四半期の収益・税引前利益・税率・株数・EPS(GAAP、百万ドル・百万株・ドル)。右: EPS の前年比の要因(Q2 2025 → Q2 2026、ドル)',
    source: 'research_r4/R14_quarterly_eps_drivers.md(10-Q・8-K の要約)、calc/out/growth_v3.json',
  });

  // 左上: 四半期の表。実効税率は 6.2・6.4% を灰、16.4・23.4% をアンバーの字。税引前 ÷ 株数は緑の太字
  const grey = (t) => ({ text: t, options: { color: C.sub } });
  const amber = (t) => ({ text: t, options: { color: C.amber } });
  const green = (t) => ({ text: t, options: { color: C.primary, bold: true } });
  L.table(s, [
    ['四半期', '収益', '税引前', '税引前利益率', '実効税率', '希薄化後株数', 'EPS', '税引前 ÷ 株数'],
    ['Q1 25', '772', '80', '10.3%', '10.9%', '1,185', '0.060', green('0.067')],
    ['Q2 25', '855', '112', '13.1%', '13.3%', '1,183', '0.082', green('0.095')],
    ['Q3 25', '962', '149', '15.4%', grey('6.2%'), '1,291', '0.108', green('0.115')],
    ['Q4 25', '1,027', '185', '18.0%', grey('6.4%'), '1,346', '0.129', green('0.138')],
    ['Q1 26', '1,100', '200', '18.1%', amber('16.4%'), '1,378', '0.121', green('0.145')],
    ['Q2 26', '1,219', '204', '16.8%', amber('23.4%'), '1,352', '0.116', green('0.151')],
  ], { x: 0.5, y: 1.62, w: 8.3, colW: [0.9, 0.95, 0.95, 1.2, 1.1, 1.2, 0.9, 1.1], fontSize: 9, rowH: 0.34 });

  // 左下: 税・株数・下期の読み。見出しの語だけを濃い字にする
  L.bullets(s, [
    [{ text: '税: ', options: { bold: true, color: C.dark } }, { text: '6% → 23% の正常化は 1 回限りの段差。2026 年 EPS を約 0.12 ドル下げる(税率 6.5% のままなら 0.72)。' },
      { text: '会社の通期の前提は 22%', options: { softBreakBefore: true } }],
    [{ text: '株数: ', options: { bold: true, color: C.dark } }, { text: '前年比 +14.3%。増資 1.41 億株が 83%、残り 0.29 億株は株式報酬など。2029 年の転換社債は最大 0.79 億株' }],
    [{ text: '下期: ', options: { bold: true, color: C.dark } }, { text: '通期 EPS 0.60 は Q3 0.17・Q4 0.19 を要し、Q3 の税引前は前期比 +44%。' },
      { text: '販促費を 392 → 330 百万ドルに戻せば届く設計', options: { softBreakBefore: true } }],
  ], { x: 0.5, y: 4.4, w: 8.3, h: 2.2, fontSize: 9.5, name: 'bullets', gap: 6 });

  // 右: EPS の前年比の要因(横棒の 1 系列。点ごとの色: 増収・利益率は緑、税率・株数は赤、合計は濃緑)
  L.paneHead(s, 9.05, 1.62, 3.78, 'EPS の前年比の要因(ドル)');
  s.addChart(pres.charts.BAR, [
    { name: 'EPS の前年比(ドル)', labels: ['増収', '利益率', '税率', '株数', '合計'], values: [0.035, 0.033, -0.017, -0.017, 0.034] },
  ], L.chartStyle({
    x: 9.05, y: 1.98, w: 3.78, h: 3.0, objectName: 'chart',
    barDir: 'bar', chartColors: [C.primary, C.primary, C.red, C.red, C.dark],
    catAxisOrientation: 'maxMin', catAxisLabelPos: 'low',
    valAxisHidden: true, valGridLine: { style: 'none' }, valAxisMinVal: -0.05, valAxisMaxVal: 0.06,
    dataLabelPosition: 'outEnd', dataLabelColor: C.text, dataLabelFormatCode: '+0.000;-0.000',
    showLegend: false,
  }));

  // 右下: takeaway
  L.takeaway(s, 9.05, 5.1, 3.78, 1.55, '税引前は +82%、1 株当たり税引前は +59%。\n税と株数が増益の半分を打ち消した。\n税の段差は Q2 で終わり、以後の EPS は\n税引前に沿って伸びる');
};
