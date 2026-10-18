// 成長の前提: 根幹 KPI の加速度(指示書 spec/ch2.md の s14 節どおり)
// 型: 左に表(2 階差分の色: 加速・改善は緑、減速・悪化は赤、横ばいは灰)、右にチャートと結論
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 根幹 KPI の水準と加速度(前期比は年率換算)。右: コンセンサスの四半期 EPS(2026 年)',
    source: '会社開示(Q4 2024〜Q2 2026)、research/R1b_kpi.md、research_r2/R6・R7・R8(Benzinga の四半期コンセンサス)',
  });

  // 左: 根幹 KPI の表(2 階差分の列に色を付ける)
  const green = { color: C.primary, bold: true }, red = { color: C.red, bold: true }, gray = { color: C.sub };
  const c = (text, options) => ({ text, options });
  L.table(s, [
    ['根幹 KPI', '水準(Q2 2026)', '前期比(年率)', '前年比', '2 階差分', 'コンセンサス'],
    ['会員数', '1,580 万人', '+34%', '+35%', c('横ばい(+35% が 3 期)', gray), '2026 年\n+30% 以上'],
    ['会員純増', '110 万人', '0%(Q1 も 110 万)', '+29%', c('減速', red), '—'],
    ['会員当たり製品数', '1.54', '+8%', '+5%', c('加速(1.46 → 1.54)', green), '—'],
    ['クロスバイ', '51%', '+8pt', '+16pt', c('加速', green), '—'],
    ['調整後純収益', '12.1 億ドル', '+51%', '+40%', c('横ばい(+41 → +40%)', gray), '2026 年\n47.5〜48.5 億'],
    ['LPB の組成', '31 億ドル', '+14%', '+29%', c('減速(Q4 2025 の\n37 億がピーク)', red), '—'],
    ['all-in 貸倒率', '3.7%', '−0.7pt', '−0.8pt', c('改善', green), '—'],
    ['販促費率', '32.2%', '+1.7pt', '+1.2pt', c('悪化', red), '下期に\n低下を前提'],
    ['総自己資本比率', '18.8%', '−2.5pt', '—', c('低下が加速', red), '—'],
  ], { x: 0.5, y: 1.62, w: 8.3, colW: [1.7, 1.45, 1.3, 1.1, 1.55, 1.2], fontSize: 9, rowH: 0.4, align: ['left', 'left', 'left', 'left', 'left', 'left'] });

  // 右: 四半期 EPS の積み上げ縦棒(実績と予想。該当しない期は 0 にしてラベルを消す)と結論
  L.paneHead(s, 9.05, 1.62, 3.78, '四半期 EPS(調整後、ドル)');
  s.addChart(pres.charts.BAR, [
    { name: '実績', labels: ['Q1', 'Q2', 'Q3 予', 'Q4 予'], values: [0.12, 0.12, 0, 0] },
    { name: '予想', labels: ['Q1', 'Q2', 'Q3 予', 'Q4 予'], values: [0, 0, 0.17, 0.19] },
  ], L.chartStyle({
    x: 9.05, y: 1.98, w: 3.78, h: 3.0, objectName: 'chart',
    barDir: 'col', barGrouping: 'stacked', chartColors: [C.primary, C.light],
    dataLabelPosition: 'inEnd', dataLabelColor: C.white, dataLabelFormatCode: '0.00;-0.00;;',
    valAxisMinVal: 0, valAxisMaxVal: 0.2, valAxisMajorUnit: 0.05, valAxisLabelFormatCode: '0.00',
    showLegend: true, legendPos: 'b',
  }));
  L.takeaway(s, 9.05, 5.1, 3.78, 1.55, 'コンセンサスは下期に EPS +50% を前提にし、\n会社の通期 0.60 と一致。\n会員の伸びは横ばい、\n販促費率と資本比率は悪化');
};
