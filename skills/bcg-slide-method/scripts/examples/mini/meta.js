// 手本(4 枚): 章・節・テーマ・なぜ・タイトルの一括管理。タイトルの数字は F('id') で台帳から引く(lint_deck.py src が検査)
const F = require('./facts.js');
const CH = [
  { no: 1, name: '評価総括', short: '総括', why: '結論と評価の全体像を先に示し、以降の章で根拠を確かめる', secs: [['1-1', '結論']] },
  { no: 2, name: '価値評価', short: '価値', why: '構造評価を倍率に変えて理論株価を出す', secs: [['2-1', '年度別の理論株価'], ['2-2', '収益の伸び']] },
];
const ORDER = ['s01', 's02', 's03', 's04'];
const META = {
  s01: { ch: 1, kind: 'cover' },
  s02: { ch: 1, sec: '1-1', theme: '結論', why: '最初に判断と根拠の骨格を示す',
    title: `構造評価 ${F('val.grade.letter')}・理論株価 ${F('val.value.engine')} ドルで「${F('val.decision.16.5')}」。\nQ3 は収益 +${F.n('q3.revenue_yoy')}% に加速し、2027 年の EPS 見通しは ${F('g27.eps')}` },
  s03: { ch: 2, sec: '2-1', theme: '年度別の理論株価', why: '妥当 PER を年度ごとに出し、今日の価値に割り引く',
    title: `妥当 PER は許容 PEG × 3 年の成長率(2026 年は ${F('val.peg.2026')} × ${F('val.row.engine.2026.g')}\n= ${F('val.row.engine.2026.per')} 倍)。年度の重みを付けて ${F('val.value.engine')} ドル。PEG 1.0 でも ${F('val.value_peg10.engine')} ドル` },
  s04: { ch: 2, sec: '2-2', theme: '収益の伸び', why: '何が伸びを作ったかを、前の四半期と並べて確かめる',
    title: `手数料型の収益は ${F('q3.fee_rev')}(前年比 +${F.n('q3.fee_yoy')}%)で、比率は\n${F('q2.fee_share')} から ${F('q3.fee_share')} に上がった` },
};
function ctxFor(id) {
  const meta = META[id];
  if (!meta) throw new Error('META にない id: ' + id);
  const page = ORDER.indexOf(id) + 1;
  const ch = CH[meta.ch - 1];
  let secLabel = '';
  if (meta.sec) {
    const sec = ch.secs.find(r => r[0] === meta.sec);
    const same = ORDER.filter(k => META[k].sec === meta.sec && META[k].ch === meta.ch);
    secLabel = meta.sec + ' ' + (sec ? sec[1] : '') + (same.length > 1 ? `(${same.indexOf(id) + 1}/${same.length})` : '');
  }
  return { id, page, total: ORDER.length, meta, ch, secLabel };
}
function secPages(chNo) {
  return CH[chNo - 1].secs.map(([no, name]) => {
    const pages = ORDER.map((k, i) => [k, i + 1]).filter(([k]) => META[k].ch === chNo && META[k].sec === no).map(([, p]) => p);
    return { no, name, from: pages[0], to: pages[pages.length - 1] };
  });
}
const DOC_TITLE = 'SoFi Technologies(SOFI)長期保有適格性審査(手本)', DOC_AUTHOR = '長期保有適格性審査';
module.exports = { CH, ORDER, META, ctxFor, secPages, DOC_TITLE, DOC_AUTHOR };
