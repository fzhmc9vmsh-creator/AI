// s13 計画の確度(手本 c06 の形)
module.exports = function build(pres, L) {
  const { C, FONT } = L;
  const s = L.contentSlide(pres, {
    kicker: '会社の計画の4要素を「確度 × 影響」で並べ、どこまで信じてよいかを見る(数字は当分析モデルの推定)',
    source: '当分析の5か年コホートモデル(確度は上場ソフト会社の実績・契約・完工・数字に出たかで判定、影響は価値評価の計算機で理論株価を動かした幅)',
  });
  L.paneHead(s, 0.5, 1.62, 7.9, '計画の確度: 横 = 確度、縦 = 実現しないときの理論株価の動く幅、円 = 確度 × 影響', 'pane_cf_head');
  L.bubbleMatrix(s, {
    xTitle: '確度(%)', yTitle: '実現しないと理論株価が動く幅(%)',
    xMin: 20, xMax: 85, xTicks: [20, 40, 60, 80], xFmt: v => v + '%',
    yMin: -12, yMax: 100, yTicks: [0, 25, 50, 75, 100], yFmt: v => v + '%',
    xSplit: 40, ySplit: 10,
    quad: { tl: '確度が低く影響が大きい', tr: '確度が高く影響が大きい', bl: '確度が低く影響が小さい', br: '確度が高く影響が小さい' },
    hot: 'tl',
    sizeMax: 0.8, sizeLegend: '円の面積 = 確度 × 影響',
    items: [
      { label: '研究開発費の比率の低下', sub: '確度 50% × 影響 13%', x: 50, y: 13, size: 6.5, tone: 'focus', n: 1, lpos: 'l' },
      { label: '直販の比率の上昇', sub: '確度 60% × 影響 10%', x: 60, y: 10, size: 6.0, tone: 'muted', lpos: 'b' },
      { label: '支払い義務の消化', sub: '確度 60% × 影響 93%', x: 60, y: 93, size: 55.8, tone: 'risk', n: 2, lpos: 'r' },
      { label: '5製品群の売上5.4倍', sub: '確度 62% × 影響 20%', x: 62, y: 20, size: 12.4, tone: 'muted', n: 3, lpos: 'r' },
    ],
  }, { x: 0.5, y: 2.12, w: 7.9, h: 3.7, name: 'cf' });
  s.addText('物差し  確度: 高 = 70% 以上(契約・完工・数字に出た)/ 中 = 40〜70% / 低 = 40% 未満。影響: 大 = ±10% 以上', { x: 0.5, y: 5.9, w: 7.9, h: 0.3, fontFace: FONT, fontSize: 9, color: C.sub, margin: 0, valign: 'middle', isTextBox: true, objectName: 'cf_scale' });
  L.lookBox(s, [
    { n: 1, text: '研究開発費の比率は53.5%→27.1%が計画の最大の源。\n上場ソフト会社の実績27.5〜40%に27%未満は無く、確度は中' },
    { n: 2, text: '支払い義務の消化は、需要が計画を下回ると\n理論株価の9割を失う' },
    { n: 3, text: '売上の伸びは確度62%' },
  ], { x: 8.65, y: 1.98, w: 4.18, h: 4.19 });
  L.termNotes(s, [
    { term: '研究開発費率', plain: '研究開発費 ÷ 売上。AIモデルの学習費を含む', why: '計画で最大の価値の源のため' },
  ], { x: 0.5, y: 6.3, w: 12.33 });
};
