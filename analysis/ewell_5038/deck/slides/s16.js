// 13 条件: 現在と将来(確率)の評価を表にし、色は A 緑・B 灰・C 以下 赤の 3 色
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, {
    kicker: '各条件の現在の評価と、将来の評価(達成確率)。決め手を右に置く。評価の色: A 緑、B 灰、C 以下 赤',
    source: '当方の構造評価(13 条件)、会社決算説明資料、有価証券報告書、当方の計算',
  });
  const fillOf = (g) => g === 'A' ? { fill: { color: C.primary }, color: C.white } : (g === 'B' ? { fill: { color: C.rule }, color: C.text } : { fill: { color: C.red }, color: C.white });
  const g = (txt) => ({ text: txt, options: Object.assign({ bold: true }, fillOf(txt[0])) });
  const data = [
    ['1', '価格決定力・競争優位・成長性', 'B', 'A(40%)', '2.7 倍高くても流出低下、分母は横ばい'],
    ['2', 'コア事業の CF', 'A', 'A(80%)', 'FCF 1,191 百万円(売上の 35%)'],
    ['3', 'コア資産の転用', 'B', 'A(50%)', '単価の伸びの約 9 割が AI・BPaaS'],
    ['4', '日本株', 'A', 'A', '東証グロース'],
    ['5', 'CEO', 'B', 'B(60%)', '創業者。資本配分と統治に留保'],
    ['6', 'EPS CAGR 30%・PEG < 1', 'D', 'C(30%)', '3 年 CAGR 16.4〜19.3%'],
    ['7', '安い理由', 'C', 'B(45%)', '減速は正しいリスク'],
    ['8', '非コモディティ', 'B', 'B', '機能の束で差別化'],
    ['9', 'AI の停めない運用', 'C', 'B(40%)', 'AI は付加価値'],
    ['10', '無形資産の陳腐化', 'B', 'B', '資産計上 180 百万円'],
    ['11', '模倣困難', 'B', 'B', '乗り換えの痛み'],
    ['12', '従量課金型', 'A', 'A', '売上の約 95% がリカーリング'],
    ['13', 'アーキタイプ', 'B', 'B', 'ORCL 型の小型版'],
  ];
  const rows = [['#', '条件', '現在', '将来(確率)', '決め手']].concat(data.map(r => [r[0], r[1], g(r[2]), g(r[3]), r[4]]));
  L.table(s, rows, { x: 0.5, y: 1.68, w: 12.33, colW: [0.55, 4.0, 1.0, 1.4, 5.38], fontSize: 9.5, rowH: 0.31, align: ['center', 'left', 'center', 'center', 'left'], name: 'tbl_cond' });
  L.takeaway(s, 0.5, 6.08, 12.33, 0.66,
    `分布 A3・B7・C2・D1、平均 ${F('val.grade.avg')} で等級 ${F('val.grade.letter')} → 許容 PEG 1.127(2026 年)。条件 6 の D は基準として残し、拒否権は適用しない(利用者の方針)`, // lint-ok: 分布と PEG は台帳に無い
    { fontSize: 10.5 });
};
