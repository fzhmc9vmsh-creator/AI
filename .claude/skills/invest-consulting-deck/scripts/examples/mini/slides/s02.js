// エグゼクティブサマリ: KPI の札と結論の箱の数字は F() で引く(要所)。本文の行は手で書いてよい(pptx の照合で確かめる)
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, { kicker: 'エグゼクティブサマリ', source: '台帳 facts.json(8-K・説明会の要約)、valuate.py の出力 valuation.json' });
  L.kpiTiles(s, [
    { value: `${F('val.value.engine')} ドル`, label: '理論株価(エンジン)', note: `期待値 ${F('val.scen.ev')}・強気 ${F('val.scen.bull.value')}・弱気 ${F('val.scen.bear.value')}` },
    { value: F('price.last'), label: '株価(10/16)', note: `決算後の目安 ${F('price.alt')}` },
    { value: F('val.grade.letter'), label: '構造評価', note: `${F('val.grade.distribution')}、平均点 ${F('val.grade.avg')}`, color: C.primary },
    { value: F('val.decision.16.5'), label: `最終判断(株価 ${F('price.alt', { noPeriod: true })})`, note: `分割 ${F('val.entry.Z1')}〜${F('val.entry.Z2')}、即時 ${F('val.entry.Z1')} 以下`, color: C.dark },
  ], { y: 1.62, h: 1.45 });
  L.table(s, [
    ['項目', 'Q3 2026', '前の四半期など'],
    ['総純収益', '13.85 億ドル(前年比 +44%)', '—'],
    ['預金', '513 億ドル', '455 億ドル(Q2)'],
    ['総自己資本比率', '17.0%', '18.8%(Q2)'],
    ['損失率(all-in)', '3.4%', '3.7%(Q2)'],
  ], { x: 0.5, y: 3.3, w: 7.6, colW: [2.2, 2.8, 2.6], fontSize: 10, rowH: 0.36 });
  L.takeaway(s, 8.4, 3.3, 4.43, 1.8, `理論株価 ${F('val.value.engine')} ドルは株価の ${F('val.gap.engine.16.5')}〜${F('val.gap.engine.14.55')}。\n律速は自己資本(比率 ${F('q3.tcr')})で、損失率は ${F('q3.allin')} に改善`);
};
