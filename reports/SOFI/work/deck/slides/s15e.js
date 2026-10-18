// B2B 基盤と SoFiUSD(指示書 spec/v2.md の s15e 節どおり)
// 型: 左に積み上げ縦棒(底打ち局面の 2 期だけ別系列の色)・段階の帯・注、右に表 2 つと takeaway(手本 s13 の左右の型、段階の帯は s05 の箱の並べ方)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: Tech Platform の四半期収益(百万ドル)と段階(G6)。右: SoFiUSD の稼働状況と費用効果の感応度(G7、算術のみ)',
    source: 'research_r3/R11_techplatform_sofiusd.md(8-K・10-Q・会社発表の要約)、calc/out/growth_v2.json(g7)',
  });

  // 左上: Tech Platform の四半期収益(Q1 26・Q2 26 だけ別系列の色にする。0 の点はラベルを消す)
  L.paneHead(s, 0.5, 1.62, 6.3, 'Tech Platform の収益(百万ドル)');
  const labels = ['Q1 24', 'Q2 24', 'Q3 24', 'Q4 24', 'Q1 25', 'Q2 25', 'Q3 25', 'Q4 25', 'Q1 26', 'Q2 26'];
  s.addChart(pres.charts.BAR, [
    { name: '収益', labels, values: [94.4, 95.4, 102.5, 102.8, 103.4, 109.8, 114.6, 122.0, 0, 0] },
    { name: '大口離脱後', labels, values: [0, 0, 0, 0, 0, 0, 0, 0, 75.1, 84.5] },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 6.3, h: 2.7, objectName: 'chart',
    barDir: 'col', barGrouping: 'stacked', chartColors: [C.primary, C.amber],
    dataLabelPosition: 'inEnd', dataLabelColor: C.white, dataLabelFormatCode: '0.0;-0.0;;',
    valAxisMinVal: 0,
    showLegend: true, legendPos: 'b',
  }));

  // 左下: 段階の帯(4 つの箱を横に並べる。現在の段階「底打ち」だけ濃緑)
  L.flow(s, [
    { head: '失注', boxes: [{ text: '大口顧客が\n2025 年末に離脱\n(前年比 −27%)', tone: 'in', h: 0.95, size: 9.5 }] },
    { head: '底打ち(現在)', boxes: [{ text: '前期比 +12.5%、\n口座 +190 万', tone: 'key', h: 0.95, size: 9.5 }] },
    { head: '信頼獲得', boxes: [{ text: 'SoFi Money を\n自社の新コアへ\n移行、新規 13 社', tone: 'in', h: 0.95, size: 9.5 }] },
    { head: '再成長', boxes: [{ text: 'Q1 2027 から\n前年比が楽になる', tone: 'in', h: 0.95, size: 9.5 }] },
  ], { x: 0.5, y: 4.82, w: 6.3, h: 1.37, gap: 0.3 });
  L.text(s, '貢献利益は 1,200 万 → 1,180 万ドル(率 16% → 14%)で未底打ち。\n大口除外後の伸び 12%(目標 20%)', { x: 0.5, y: 6.3, w: 6.3, h: 0.42, fontSize: 9.5 });

  // 右上: SoFiUSD の稼働状況
  L.paneHead(s, 7.05, 1.62, 5.78, 'SoFiUSD(G7)');
  L.table(s, [
    ['指標', '値'],
    ['発行', '2025-12 発表、2026-05 会員向け'],
    ['流通残高', '約 3 億ドル(Q2 末、報道)'],
    ['自社カードの決済', '2026-09-22 に Mastercard 決済を\nSoFiUSD へ切替(年 250 億ドル超の見込み)'],
    ['費用削減の開示', 'なし'],
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

  L.takeaway(s, 7.05, 5.95, 5.78, 0.75, 'Tech Platform は収益で底打ち、利益は未底打ち。\nSoFiUSD は仕組みとして正しいが、効果はまだ\nEPS の 1% 未満で、オプションとして扱う');
};
