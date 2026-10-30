// 年度別の理論株価: 表の数字は valuate.py の表示値(val.row.*)。手で計算しない。下に 3 経路と PEG 1.0 の検算を並べる
module.exports = function build(pres, L) {
  const { F } = L;
  const s = L.contentSlide(pres, { kicker: '年度別の表: 妥当 PER = 許容 PEG × 当該年度から 3 年の EPS 成長率。今日の価値は資本コストで割り引き、年度の重み 40・30・20・10%', source: 'valuate.py の出力 valuation.json(3 経路の EPS は台帳 facts.json)' });
  L.paneHead(s, 0.5, 1.62, 8.2, '事業エンジンの経路(採用)', 'pane_a');
  const rows = [['年度', 'EPS', '3 年の成長率', '許容 PEG', '妥当 PER', '適正株価', '今日の価値']];
  [2026, 2027, 2028, 2029].forEach(y => rows.push([String(y), F(`val.row.engine.${y}.eps`), F(`val.row.engine.${y}.g`), F(`val.peg.${y}`),
    F(`val.row.engine.${y}.per`), F(`val.row.engine.${y}.price`), F(`val.row.engine.${y}.pv`)]));
  rows.push(['理論株価(重み付き)', '', '', '', '', '', F('val.value.engine')]);
  L.table(s, rows, { x: 0.5, y: 1.98, w: 8.2, colW: [1.7, 0.9, 1.2, 1.0, 1.0, 1.1, 1.3], fontSize: 10.5, rowH: 0.38 });
  L.paneHead(s, 0.5, 4.45, 8.2, '3 経路と PEG 1.0 の検算(平均しない)', 'pane_b');
  L.table(s, [
    ['経路', '理論株価', 'PEG 1.0 の場合', '決算後の目安との差'],
    ['事業エンジン(採用)', F('val.value.engine'), F('val.value_peg10.engine'), F('val.gap.engine.16.5')],
    ['会社の中期目標', F('val.value.company'), F('val.value_peg10.company'), F('val.gap.company.16.5')],
    ['見通し + コンセンサスの伸び', F('val.value.consensus'), F('val.value_peg10.consensus'), F('val.gap.consensus.16.5')],
  ], { x: 0.5, y: 4.81, w: 8.2, colW: [2.9, 1.6, 1.8, 1.9], fontSize: 10.5, rowH: 0.38 });
  L.takeaway(s, 9.0, 1.98, 3.83, 2.0, `許容 PEG ${F('val.peg.start')} は構造評価 ${F('val.grade.letter')} の帯の中の位置 ${F('val.grade.pos')} から。\nPEG 1.0 でも ${F('val.value_peg10.engine')} ドル`);
  L.bullets(s, ['妥当 PER は許容 PEG × g だけで決める(同業の PER・DCF は交差確認)', '成熟年度(5 年の成長率 15% 未満)は理論式', '信用・資本・希薄化は EPS 経路・確率・株数で数える'],
    { x: 9.0, y: 4.2, w: 3.83, h: 2.2, fontSize: 10, name: 'notes' });
};
