// 利益への道筋: 1株利益の推移と、製品群ごとの売上の積み上げ
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, { kicker: '製品群の売上を数量×単価で積み上げ、1株利益に落とす(数字は当分析モデルの推定)', source: '当分析の 5 か年コホートモデル' });
  L.paneHead(s, 0.5, 1.62, 5.6, '1株利益(ドル)と3年の伸び', 'pane_l');
  const years = ['2027', '2028', '2029', '2030', '2031'];
  const vals = [1.08, 1.80, 2.55, 3.18, 3.85];
  s.addChart(pres.charts.BAR, [{ name: '1株利益', labels: years, values: vals }],
    L.chartStyle({ x: 0.5, y: 2.3, w: 5.6, h: 3.3, chartColors: [C.dark, C.dark, C.dark, C.dark, C.rule], valAxisMinVal: 0, valAxisMaxVal: 5, barGapWidthPct: 60, dataLabelFormatCode: '0.00', valAxisHidden: true, valGridLine: { style: 'none' }, objectName: 'chart_eps' }));
  // 伸びのラベル(3年の伸び): 2027〜2030 の各年
  const g = ['43.1%', '28.7%', '21.8%', '19.6%'];
  s.addText('3年の伸び', { x: 0.5, y: 5.62, w: 0.9, h: 0.26, fontFace: 'Meiryo UI', fontSize: 8.5, bold: true, color: C.dark, margin: 0, valign: 'middle', isTextBox: true, objectName: 'g_lbl' });
  g.forEach((t, i) => {
    s.addText(t, { x: 1.45 + i * 0.93 - 0.05, y: 5.62, w: 0.9, h: 0.26, fontFace: 'Meiryo UI', fontSize: 9.5, bold: true, color: C.primary, align: 'center', margin: 0, valign: 'middle', isTextBox: true, objectName: 'g_' + i });
  });
  s.addText('2031 年は計画どおりの値', { x: 0.5, y: 5.9, w: 5.6, h: 0.22, fontFace: 'Meiryo UI', fontSize: 8, color: C.sub, margin: 0, valign: 'middle', isTextBox: true, objectName: 'g_note' });

  L.paneHead(s, 6.4, 1.62, 6.43, '製品群の売上(百万ドル)', 'pane_r');
  L.table(s, [
    ['製品群', '2026 年の売上', '2031 年の売上', '倍率'],
    ['クラウド事業者経由の API', '23,100', '118,080', '5.1 倍'],
    ['超大口の直販 API', '14,880', '87,300', '5.9 倍'],
    ['中核の法人 API・Claude Code', '5,670', '39,680', '7.0 倍'],
    ['法人の席', '5,940', '29,820', '5.0 倍'],
    ['個人・中小企業', '6,270', '27,195', '4.3 倍'],
    [{ text: '合計', options: { bold: true, color: C.dark } }, { text: '55,860', options: { bold: true, color: C.dark } }, { text: '302,075', options: { bold: true, color: C.dark } }, { text: '5.4 倍', options: { bold: true, color: C.dark } }],
  ], { x: 6.4, y: 2.0, w: 6.43, colW: [2.65, 1.35, 1.35, 1.08], fontSize: 10, rowH: 0.34 });
  L.lookBox(s, [
    { n: 1, text: '利益は売上より遅れて立ち上がる(2027 年 1.08 ドル)' },
    { n: 2, text: '伸びは 43.1% から 19.6% へ減速する' },
    { n: 3, text: '研究開発費の比率の低下(p.14)と単価の下落(p.15)を入れた採用の道筋' },
  ], { x: 6.4, y: 4.6, w: 6.43, h: 1.55 });
  L.termNotes(s, [{ term: 'EPS', plain: '1株あたりの純利益', why: '株価の高い安いを測る物差しの元になるため' }], { x: 0.5, y: 6.3, w: 12.33 });
};
