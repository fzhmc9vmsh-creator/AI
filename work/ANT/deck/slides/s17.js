// s17 リスクの大きさ(手本 c06)
module.exports = function build(pres, L) {
  const { C, FONT } = L;
  const s = L.contentSlide(pres, {
    kicker: '6つのリスクを「起きる確率 × 起きたときの株価の下落」で並べ、見張る順番を決める',
    source: '当分析(リスク台帳 outlook.json)',
  });
  L.paneHead(s, 0.5, 1.62, 7.9, 'リスクの大きさ: 横 = 2031年までに起きる確率、縦 = 理論株価の下落、円 = 期待損失', 'pane_rk_head');
  L.bubbleMatrix(s, {
    xTitle: '2031年までに起きる確率(%)', yTitle: '起きたときの理論株価の下落(%)',
    xMin: 0, xMax: 70, xTicks: [0, 10, 25, 40, 55, 70], xFmt: v => v + '%',
    yMin: 0, yMax: 100, yTicks: [0, 25, 50, 75, 100], yFmt: v => (v ? '−' : '') + v + '%',
    xSplit: 25, ySplit: 15,
    quad: { tl: '稀だが重い', tr: '最優先: 起きやすく重い', bl: '許容', br: '軽い' },
    hot: 'tr',
    sizeMax: 0.8, sizeLegend: '円の面積 = 期待損失(確率 × 下落率)',
    items: [
      { label: '需要の減速で遊休', sub: '20% × −93%', x: 20, y: 93, size: 18.6, tone: 'risk', n: 1, lpos: 'r' },
      { label: '実質の粗利率の低下', sub: '45% × −21.9%', x: 45, y: 21.9, size: 9.9, tone: 'risk', n: 2, lpos: 't' },
      { label: '資本コストの上乗せ', sub: '60% × −11%', x: 60, y: 11, size: 6.6, tone: 'amber', lpos: 'b' },
      { label: '研究開発費の高止まり', sub: '50% × −13%', x: 50, y: 13, size: 6.5, tone: 'amber', lpos: 'b' },
      { label: '株数の増加', sub: '40% × −8.5%', x: 40, y: 8.5, size: 3.4, tone: 'muted', lpos: 'l' },
      { label: '大口顧客の離脱', sub: '15% × −10%', x: 15, y: 10, size: 1.5, tone: 'muted', lpos: 't' },
    ],
  }, { x: 0.5, y: 2.12, w: 7.9, h: 4.05, name: 'rk' });
  s.addText('確率は過去の実績の回数から、下落は価値評価の計算機で理論株価を動かした差', { x: 0.5, y: 6.25, w: 7.9, h: 0.25, fontFace: FONT, fontSize: 9, color: C.sub, margin: 0, valign: 'middle', isTextBox: true, objectName: 'rk_note' });
  L.lookBox(s, [
    { n: 1, text: '期待損失の最大は需要の減速(20% × 93% = 18.6)。\n兆候は年換算売上の月次の伸びで、前月比マイナスが2か月で見直し' },
    { n: 2, text: '次が実質の粗利率の低下(9.9)。\n62%割れで撤回' },
    { n: 3, text: '振れ幅で見た1位(粗利率)と、確率を掛けた1位(需要)は違う' },
  ], { x: 8.65, y: 1.98, w: 4.18, h: 4.19 });
};
