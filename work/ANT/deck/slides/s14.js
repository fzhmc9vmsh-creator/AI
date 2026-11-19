// s14 市場の脅威と機会
module.exports = function build(pres, L) {
  const { C, FONT } = L;
  const s = L.contentSlide(pres, {
    kicker: '会社の計画の外で起きうる脅威と機会を「確度 × 影響」で並べ、将来の構造に入れるものを選ぶ(数字は当分析モデルの推定)',
    source: '当分析の価値評価(影響は理論株価を動かした幅)、市場データ',
  });
  L.paneHead(s, 0.5, 1.62, 7.9, '市場の脅威と機会: 横 = 確度、縦 = 影響の大きさ、円 = 確度 × 影響', 'pane_mt_head');
  L.bubbleMatrix(s, {
    xTitle: '確度(%)', yTitle: '理論株価への影響の大きさ(%)',
    xMin: 0, xMax: 100, xTicks: [0, 20, 40, 60, 80, 100], xFmt: v => v + '%',
    yMin: 0, yMax: 30, yTicks: [0, 10, 20, 30], yFmt: v => v + '%',
    xSplit: 40, ySplit: 10,
    quad: { tl: '選ばない', tr: '選ぶ: 確度40%以上かつ影響±10%以上', bl: '許容', br: '確度は高いが影響が小さい' },
    hot: 'tr',
    sizeMax: 0.95, sizeLegend: '円の面積 = 確度 × 影響',
    items: [
      { label: '利用単価の下落(2年で70〜90%)', sub: '確度 45% × 影響 −21.9%', x: 45, y: 21.9, size: 985, tone: 'risk', n: 1, lpos: 'r' },
      { label: '作業量の増加(タスクあたり5〜30倍)', sub: '確度 35% × 影響 +10.3%', x: 35, y: 10.3, size: 360, tone: 'ok', n: 2, lpos: 'b' },
    ],
  }, { x: 0.5, y: 2.12, w: 7.9, h: 4.05, name: 'mt' });
  L.lookBox(s, [
    { n: 1, text: '単価の下落は選ぶ水準。2031年の実質の粗利率を\n65.5%→57.5%に下げた筋を作った' },
    { n: 2, text: '作業量の増加は確度35%で選ばず、\n上振れの筋として残した' },
    { n: 3, text: 'どちらも実質の粗利率に出る' },
  ], { x: 8.65, y: 1.98, w: 4.18, h: 4.19 });
  L.termNotes(s, [
    { term: 'トークン', plain: 'AIが文章を処理する単位(単語の断片)', why: '利用単価(1トークンあたりの値段)の下落がリスクの1位のため' },
  ], { x: 0.5, y: 6.3, w: 12.33 });
};
