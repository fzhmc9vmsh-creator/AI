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
    ['1', '価格決定力・競争優位・成長性', 'B', 'C(40%)', '既存は守れるが、新規の取り分は未確定'],
    ['2', 'コア事業の CF', 'A', 'A', '定常利益率 57%、LTV/CAC 6.5〜12 倍'], // lint-ok: 決め手の数字は構造の解剖
    ['3', 'コア資産の転用', 'B', 'B', '成果は事務代行(粗利率 64%)。AI は赤字の増分'], // lint-ok: 決め手の数字は構造の解剖
    ['4', '日本株', 'A', 'A', '東証グロース'],
    ['5', 'CEO', 'B', 'B', '創業者。資本配分と統治に留保'],
    ['6', 'EPS CAGR 30%・PEG < 1', 'D', 'D', '3 年 CAGR 16.4〜19.3%'], // lint-ok: 決め手の数字は構造の解剖
    ['7', '安い理由', 'C', 'C(30%)', '同業 PER の約 1.12 倍。減速の恐れは正しい'], // lint-ok: 決め手の数字は構造の解剖
    ['8', '非コモディティ', 'B', 'B', '単品は商品、束で差'],
    ['9', 'AI の停めない運用', 'C', 'C', 'AI は付加機能。外しても運用は止まらない'],
    ['10', '無形資産の陳腐化', 'B', 'B', '改定対応・記録と請求の一体・既存客'],
    ['11', '模倣困難', 'B', 'C(40%)', '壁は既存客の乗り換えの痛み。開発は 14 名'], // lint-ok: 決め手の数字は構造の解剖
    ['12', '従量課金型', 'B', 'B', '反復 95% だが単独 ST の継続率 102.5%'], // lint-ok: 決め手の数字は構造の解剖
    ['13', 'アーキタイプ', 'B', 'C(40%)', 'ORCL 型の要素を部分的に満たす'],
  ];
  const rows = [['#', '条件', '現在', '将来(確率)', '決め手']].concat(data.map(r => [r[0], r[1], g(r[2]), g(r[3]), r[4]]));
  L.table(s, rows, { x: 0.5, y: 1.68, w: 12.33, colW: [0.55, 4.0, 1.0, 1.4, 5.38], fontSize: 9.5, rowH: 0.31, align: ['center', 'left', 'center', 'center', 'left'], name: 'tbl_cond' });
  L.takeaway(s, 0.5, 6.08, 12.33, 0.66,
    `分布 A2・B8・C2・D1、平均 ${F('val.grade.avg')} で等級 ${F('val.grade.letter')} → 許容 PEG 1.104(2026 年)。条件 6 の D は基準として残し、拒否権は適用しない(利用者の方針)`, // lint-ok: 分布と PEG は台帳に無い
    { fontSize: 10.5 });
};
