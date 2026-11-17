// エグゼクティブサマリ: KPI の札 4 枚 + 左レールつきの 5 行。札と結論の数字は F() で引く(要所)
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, { kicker: 'エグゼクティブサマリ', source: '台帳 facts.json(8-K・説明会の要約)、valuate.py の出力 valuation.json。株価は 10/16 終値と決算後の目安' });
  L.kpiTiles(s, [
    { value: `${F('val.value.engine')} ドル`, label: '理論株価(エンジン)', note: `期待値 ${F('val.scen.ev')}・強気 ${F('val.scen.bull.value')}・弱気 ${F('val.scen.bear.value')}` },
    { value: F('price.last'), label: '株価(10/16)', note: `決算後の目安 ${F('price.alt')}` },
    { value: F('val.grade.letter'), label: '構造評価', note: `${F('val.grade.distribution')}、平均点 ${F('val.grade.avg')}`, color: C.primary },
    { value: F('val.decision.16.5'), label: '最終判断', note: `分割 ${F('val.entry.Z1')}〜${F('val.entry.Z2')}、即時 ${F('val.entry.Z1')} 以下`, color: C.dark },
  ], { y: 1.62, h: 1.45 });
  // 本文の行: 数字は台帳から引く(手で書いてもよいが、引いておけば決算の更新で台帳を直すだけで済む)
  const rows = [
    ['結論', `構造評価 ${F('val.grade.letter')}、理論株価 ${F('val.value.engine')} ドルは決算後の目安の ${F('val.gap.engine.16.5')}。分割で建て、\n次の決算で総自己資本比率(今 ${F('q3.tcr')})と LPB の割合を確かめる`],
    ['事業', `会員 ${F('q3.members')} が預金・ローン・投資・決済を 1 つのアプリで使い、預金 ${F('q3.deposits')} でローンを抱える。\n手数料型の収益は ${F('q3.fee_share')}(前年比 +${F.n('q3.fee_yoy')}%)`],
    ['成長の質', `収益は前年比 +${F.n('q3.revenue_yoy')}% に加速。新しい製品の ${F('q3.cross_buy')} は既存の会員が開いた。\n損失率(all-in)は ${F('q3.allin')} に改善(${F('q2.allin', { noPeriod: true })}(Q2)から)`],
    ['価値', `妥当 PER = 許容 PEG ${F('val.peg.start')} × 3 年の成長率 ${F('val.row.engine.2026.g')}。年度別に当てて ${F('val.value.engine')} ドル(PEG 1.0 でも ${F('val.value_peg10.engine')})。\n強気 ${F('val.scen.bull.value')} ドル・確率 ${F('val.scen.bull.p')}、弱気 ${F('val.scen.bear.value')} ドル・${F('val.scen.bear.p')}`],
    ['市場との差分', `株価は損失率の恒常的な悪化を織り込むが、実績は ${F('q3.allin')}。信用 +1pt の場合でも ${F('sens.credit_1pt')}、\n信用・金利・増資を同時に置いても ${F('sens.all_three')}`],
  ];
  rows.forEach(([rail, body], i) => {
    const y = 3.25 + i * 0.72, first = i === 0;
    L.box(s, 0.5, y, 2.3, 0.66, { fill: first ? C.dark : C.tint, line: first ? C.dark : C.tint, name: 'ovl_rail' + i });
    L.text(s, rail, { x: 0.62, y, w: 2.1, h: 0.66, fontSize: 12, bold: true, color: first ? C.white : C.dark, valign: 'middle', margin: 0, objectName: 'rail' + i });
    L.text(s, body, { x: 3.0, y, w: 9.83, h: 0.66, fontSize: 11, valign: 'middle', objectName: 'body' + i });
  });
};
