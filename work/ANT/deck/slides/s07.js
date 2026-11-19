// s07 製品ポートフォリオ(手本 c05)
module.exports = function build(pres, L) {
  const { C, FONT } = L;
  const s = L.contentSlide(pres, {
    kicker: '製品群を「売上の伸び × 相対的な強さ」で並べ、現金を生むのはどれか、食うのはどれかを見る',
    source: '当分析の5か年コホートモデル、Menlo Ventures(2026)',
  });
  L.paneHead(s, 0.5, 1.62, 7.9, '製品ポートフォリオ: 縦 = 売上の伸び、横 = 相対的な強さ、円 = 2026年の売上(百万ドル)', 'pane_pf_head');
  L.bubbleMatrix(s, {
    xTitle: '相対的な強さ(全社のシェアからの推定)', yTitle: '製品群の売上の伸び(5年の年率 %)',
    xMin: 0.3, xMax: 2.0, xLog: true, xTicks: [0.3, 0.5, 1, 1.5, 2], xFmt: v => v + '倍',
    yMin: 30, yMax: 56, yTicks: [30, 40, 50], yFmt: v => v + '%',
    xSplit: 1.0, ySplit: 40,
    quad: { tl: '問題児: 伸びるが弱い', tr: '花形: 伸びて強い', bl: '負け犬', br: '金のなる木: 現金を生む' },
    hot: 'br', heatTone: 'green',
    sizeMax: 0.72, sizeLegend: '円の面積 = 2026年の売上(百万ドル)',
    items: [
      { label: 'クラウド事業者経由API', sub: '売上 23,100', x: 1.48, y: 38.5, size: 23100, tone: 'dark', n: 1, lpos: 'b' },
      { label: '超大口の直販API', sub: '売上 14,880', x: 1.48, y: 42.6, size: 14880, tone: 'focus', n: 2, lpos: 'l' },
      { label: '中核法人API・Claude Code', sub: '売上 5,670', x: 1.56, y: 47.6, size: 5670, tone: 'amber', n: 2, lpos: 't' },
      { label: '法人の席の契約', sub: '売上 5,940', x: 0.8, y: 38.0, size: 5940, tone: 'muted', lpos: 'l' },
      { label: '個人・中小企業', sub: '売上 6,270', x: 0.4, y: 33.9, size: 6270, tone: 'amber', n: 3, lpos: 'r' },
    ],
  }, { x: 0.5, y: 2.12, w: 7.9, h: 4.05, name: 'pf' });
  L.lookBox(s, [
    { n: 1, text: '規模の柱はクラウド事業者経由のAPIだが、\n手数料で現金の残りが減る' },
    { n: 2, text: '伸びの柱は直販とClaude Code(5年で7.0倍)。\n直販は手数料が無い' },
    { n: 3, text: '個人向けは無料枠と計算資源で現金を食う入口' },
  ], { x: 8.65, y: 1.98, w: 4.18, h: 2.75 });
  s.addText([
    { text: '色: 濃緑 = 現金を生む / アンバー = 現金を食う / 灰 = 均衡', options: { breakLine: true } },
    { text: '伸びは市場全体ではなく当分析の製品群の計画の伸びで代用。相対的な強さは全社のシェアからの推定' },
  ], { x: 8.65, y: 4.85, w: 4.18, h: 1.3, fontFace: FONT, fontSize: 9, color: C.sub, margin: 0, valign: 'top', isTextBox: true, objectName: 'pf_note' });
  L.termNotes(s, [
    { term: '製品ポートフォリオ', plain: '製品を市場の伸び×自社の強さで並べた図', why: 'どの製品が現金を生み、どこへ投じるかを見るため' },
    { term: 'PLC', plain: '製品ライフサイクル。導入・成長・成熟・衰退の段階', why: '段階で現金を生むか食うかが変わるため' },
  ], { x: 0.5, y: 6.28, w: 12.33 });
};
