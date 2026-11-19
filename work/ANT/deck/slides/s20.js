// s20 同業との比較: PEG の横棒(公開価格の上限・同業・市場)、許容 PEG の破線、比較対象の表
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, { source: '当分析、市場データ(2026-11)' });

  L.paneHead(s, 0.5, 1.62, 12.33, 'PEG(成長に対する値段、倍)', 'pane_peg_head');

  // 棒ごとの色のため赤・灰の系列に分けて積み上げる。plot 領域を固定して、許容 PEG の破線の位置を計算できるようにする
  const CX = 0.5, CY = 1.98, CW = 12.33, CH = 2.65;
  const LAY = { x: 0.2, y: 0.12, w: 0.74, h: 0.72 };
  const AX_MAX = 2.0, ALLOW = 1.242;
  const labels = ['公開価格の上限(今の PEG)', 'ServiceNow', 'S&P500'];
  s.addChart(pres.charts.BAR, [
    { name: '公開価格の上限', labels, values: [1.67, 0, 0] },
    { name: '同業・市場', labels, values: [0, 0.92, 0.72] },
  ], L.chartStyle({
    x: CX, y: CY, w: CW, h: CH, layout: LAY,
    barDir: 'bar', barGrouping: 'stacked', catAxisOrientation: 'maxMin',
    valAxisMinVal: 0, valAxisMaxVal: AX_MAX, valAxisMajorUnit: 0.5, valAxisLabelFormatCode: '0.0"倍"',
    dataLabelFormatCode: '0.00"倍";;', dataLabelPosition: 'ctr', dataLabelColor: C.white,
    barGapWidthPct: 60,
    chartColors: [C.red, C.sub],
    objectName: 'chart_peg',
  }));

  // 許容 PEG 1.242 倍の破線(plot 領域の位置から計算)
  const px0 = CX + LAY.x * CW, pw = LAY.w * CW, py0 = CY + LAY.y * CH, ph = LAY.h * CH;
  const xl = px0 + (ALLOW / AX_MAX) * pw;
  s.addShape('line', { x: xl, y: py0 - 0.05, w: 0.001, h: ph + 0.05, line: { color: C.dark, width: 1, dashType: 'dash' }, objectName: 'ovl_allow_line' });
  L.text(s, '許容 PEG 1.242 倍', { x: xl - 1.1, y: CY - 0.02, w: 2.2, h: 0.24, fontSize: 9, bold: true, color: C.dark, align: 'center', valign: 'middle', margin: 0, objectName: 'ovl_allow_label' });

  L.table(s, [
    ['比較対象', '何の会社か', 'なぜ比べるか'],
    ['ServiceNow', '企業向けの業務ソフトを継続課金で売る会社', '法人顧客・継続課金・高い利益率で成長が続く会社の上限の目安'],
    ['S&P500', '米国の大型株 500 社の指数', '市場全体が成長に払う値段の基準'],
  ], { x: 0.5, y: 4.85, w: 12.33, colW: [2.0, 4.6, 5.73], fontSize: 10, rowH: 0.36, align: ['left', 'left', 'left'], name: 'tbl_peers' });

  L.text(s, '指標: PEG = PER ÷ 今後 3 年の 1 株利益の伸び(%)。成長の速さに対して値段が高いかを見る。NVIDIA は半導体で稼ぎ仕組みが違うため外した', {
    x: 0.5, y: 6.1, w: 12.33, h: 0.45, fontSize: 9.5, color: C.text, margin: 0, valign: 'top', objectName: 'note_metric',
  });
};
