// 年度別の理論株価: 表の数字は valuate.py の表示値(val.row.*)。手で計算しない
module.exports = function build(pres, L) {
  const { F } = L;
  const s = L.contentSlide(pres, { kicker: '年度別の表: 妥当 PER = 許容 PEG × 当該年度から 3 年の EPS 成長率。今日の価値は資本コストで割り引き、年度の重み 40・30・20・10%', source: 'valuate.py の出力 valuation.json(事業エンジン経路)' });
  const rows = [['年度', 'EPS', '3 年の成長率', '許容 PEG', '妥当 PER', '適正株価', '今日の価値']];
  [2026, 2027, 2028, 2029].forEach(y => rows.push([String(y), F(`val.row.engine.${y}.eps`), F(`val.row.engine.${y}.g`), F(`val.peg.${y}`),
    F(`val.row.engine.${y}.per`), F(`val.row.engine.${y}.price`), F(`val.row.engine.${y}.pv`)]));
  rows.push(['理論株価', '', '', '', '', '', F('val.value.engine')]);
  L.table(s, rows, { x: 0.5, y: 1.75, w: 8.2, colW: [1.3, 1.0, 1.3, 1.1, 1.1, 1.2, 1.2], fontSize: 10.5, rowH: 0.42 });
  L.takeaway(s, 9.0, 1.75, 3.83, 2.2, `PEG 1.0 でも ${F('val.value_peg10.engine')} ドル。\n許容 PEG ${F('val.peg.start')} は構造評価 ${F('val.grade.letter')} の帯の中の位置 ${F('val.grade.pos')} から`);
};
