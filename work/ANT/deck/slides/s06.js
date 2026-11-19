// 用語: storyline.json の glossary 全語を表にする(意味・なぜ要るか は glossary の文をそのまま写す)
const path = require('path');
const SL = require(path.join(process.cwd(), 'storyline.json'));
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {});
  const rows = [['用語', '意味', 'この資料でなぜ要るか', '初めて出るページ']];
  SL.glossary.forEach(g => rows.push([g.term, g.plain, g.why, 'p.' + Number(String(g.first_page).replace(/^s0?/, ''))]));
  L.table(s, rows, { x: L.M, y: 1.66, w: 12.33, colW: [1.7, 5.2, 4.1, 1.33], fontSize: 9.5, rowH: 0.245, align: ['left', 'left', 'left', 'center'], name: 'gloss_tbl' });
};
