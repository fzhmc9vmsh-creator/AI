// 適正株価: 年度別の表と、公開価格から適正株価への価値の橋
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, { kicker: '許容 PEG で年度ごとに今日の価値へ直し、重みをつけて 1 つの適正株価にする', source: '当分析の価値評価' });
  L.paneHead(s, 0.5, 1.62, 5.8, '年度別の1 株あたりの適正株価(ドル)', 'pane_l');
  const bold = (t) => ({ text: t, options: { bold: true, color: C.dark } });
  L.table(s, [
    ['年度', '1 株利益', '3 年の伸び', '許容 PEG', '妥当 PER', '今日の価値'],
    ['2027', '1.08', '43.1%', '1.242', '53.6', '55.1'],
    ['2028', '1.80', '28.7%', '1.192', '34.3', '52.6'],
    ['2029', '2.55', '21.8%', '1.142', '24.9', '48.3'],
    ['2030', '3.18', '19.6%', '1.092', '21.4', '46.4'],
    [bold('重み付きの適正株価'), '', '', '', '', bold('51.7')],
  ], { x: 0.5, y: 2.0, w: 5.8, colW: [1.5, 0.75, 0.9, 0.8, 0.8, 1.05], fontSize: 10, rowH: 0.4 });
  L.paneHead(s, 6.6, 1.62, 6.23, '価値の橋(1 株あたり、ドル)', 'pane_r');
  L.waterfall(s, [
    { label: '公開価格の\n上限', val: 78.0, type: 'total', disp: '78.0' },
    { label: '今の利益だけでは\n説明できない分', val: -68.6, type: 'step', disp: '▲68.6', ref: 'p.8' },
    { label: '今の利益が続く\n場合の価値', val: 9.4, type: 'total', disp: '9.4' },
    { label: '成長の上乗せ', val: 42.3, type: 'step', disp: '+42.3', highlight: true, ref: 'p.15' },
    { label: '適正株価', val: 51.7, type: 'total', disp: '51.7', ref: 'p.21' },
  ], { x: 6.6, y: 2.0, w: 6.23, h: 3.4, name: 'wf', labelFontSize: 8 });
  s.addText('10 年の割引現金流での確認 53.5 ドル、確率加重の期待値 55.3 ドル、会社の最善の筋 77.9 ドル(平均しない)', { x: 0.5, y: 4.55, w: 5.8, h: 0.6, fontFace: 'Meiryo UI', fontSize: 9.5, color: C.sub, margin: 0, valign: 'top', isTextBox: true, objectName: 'cross' });
  L.takeaway(s, 0.5, 5.7, 12.33, 0.75, `適正株価 ${F('fair')}。差 ${F('fair.gap')} は成長の満額実現を先に払う分`, { fontSize: 12 });
};
