// B2B 基盤と SoFiUSD(指示書 spec/v4.md の H6 の s15e 節)
// 型: 左に積み上げ縦棒(大口離脱後の系列を別色)・段階の帯・注、右に表 2 つと takeaway
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: Tech Platform の四半期収益(百万ドル)と段階(G6)。右: SoFiUSD の稼働状況と費用効果の感応度(G7、算術のみ)',
    source: 'research_r5/Q3_datasheet.md(Q3 の 8-K・説明会の要約)、research_r3/R11_techplatform_sofiusd.md(SoFiUSD の発行・会員向け提供)、calc/out/growth_v4.json',
  });

  // 左上: Tech Platform の四半期収益(大口離脱後の系列を別色。0 の点はラベルを消す)
  L.paneHead(s, 0.5, 1.62, 6.3, 'Tech Platform の収益(百万ドル)');
  const labels = ['Q1 24', 'Q2 24', 'Q3 24', 'Q4 24', 'Q1 25', 'Q2 25', 'Q3 25', 'Q4 25', 'Q1 26', 'Q2 26', 'Q3 26'];
  s.addChart(pres.charts.BAR, [
    { name: '収益', labels, values: [94.4, 95.4, 102.5, 102.8, 103.4, 109.8, 114.6, 122.0, 0, 0, 0] },
    { name: '大口離脱後', labels, values: [0, 0, 0, 0, 0, 0, 0, 0, 75.1, 84.5, 87.4] },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 6.3, h: 2.7, objectName: 'chart',
    barDir: 'col', barGrouping: 'stacked', chartColors: [C.primary, C.amber],
    dataLabelPosition: 'inEnd', dataLabelColor: C.white, dataLabelFormatCode: '0.0;-0.0;;',
    valAxisMinVal: 0,
    showLegend: true, legendPos: 'b',
  }));

  // 左下: 段階の帯(4 つの箱を横に並べる。現在の段階「再成長の入口」だけ濃緑)
  L.flow(s, [
    { head: '失注', boxes: [{ text: '大口顧客が\n2025 年末に離脱\n(Q1 前年比 −27%)', tone: 'in', h: 0.95, size: 9.5 }] },
    { head: '底打ち(Q1・Q2)', boxes: [{ text: '前期比 +12.5%(Q2)\n大口離脱後の底', tone: 'in', h: 0.95, size: 9.5 }] },
    { head: '再成長の入口', boxes: [{ text: '大口を除き\n+18%(Q3)\n貢献利益率 16%', tone: 'key', h: 0.95, size: 9.5 }] },
    { head: '再成長', boxes: [{ text: '前年比のプラスは\nQ1 2027 の見通し', tone: 'in', h: 0.95, size: 9.5 }] },
  ], { x: 0.5, y: 4.82, w: 6.3, h: 1.37, gap: 0.3 });
  L.text(s, '貢献利益は Q2 1,180 万 → Q3 1,420 万ドル(率 14% → 16%)。\n大口を除く前年比は Q3 +18%(Q1 は +12%)', { x: 0.5, y: 6.3, w: 6.3, h: 0.42, fontSize: 9.5 });

  // 右上: SoFiUSD の稼働状況
  L.paneHead(s, 7.05, 1.62, 5.78, 'SoFiUSD(G7)');
  L.table(s, [
    ['指標', '値'],
    ['会員向けの提供', '2026-05-27(対象 1,470 万人)'],
    ['流通額', '出所でばらばら(未確定)'],
    ['収益', '未開示'],
  ], { x: 7.05, y: 2.0, w: 5.78, colW: [2.2, 3.58], fontSize: 10, rowH: 0.3, align: ['left', 'left'] });

  // 右下: 費用効果の感応度(算術のみ)
  L.paneHead(s, 7.05, 3.8, 5.78, '費用効果の感応度(算術のみ)');
  L.table(s, [
    ['前提', '年額', 'EPS'],
    ['決済の削減 1bp', '250 万ドル', '0.0014'],
    ['決済の削減 5bp', '1,250 万ドル', '0.007'],
    ['流通 30 億ドル × 利ざや 1%', '3,000 万ドル', '0.017'],
    ['流通 100 億ドル × 利ざや 1%', '1 億ドル', '0.056'],
  ], { x: 7.05, y: 4.2, w: 5.78, colW: [2.78, 1.6, 1.4], fontSize: 10, rowH: 0.3 });

  L.takeaway(s, 7.05, 5.95, 5.78, 0.75, 'Tech Platform は再成長の入口に立ち、大口を除き +18%。\nSoFiUSD は仕組みとして正しいが、収益は未開示で、\n効果は EPS の 1% 未満(推計)。オプションとして扱う');
};
