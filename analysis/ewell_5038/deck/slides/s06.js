// 損益の流れ: サンキー図(本文幅の 7 割以上)+ 見るところ
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, { kicker: '', source: '有価証券報告書(FY2025)p.63-64・p.70、当方の計算' });
  const w = 8.8, h = w * 1122 / 2200;
  s.addImage({ path: '../fig/sankey_fy25_deck.png', x: 0.5, y: 1.7, w, h, altText: 'FY2025の損益の流れ(サンキー図、百万円)' });
  L.text(s, '単位: 百万円(FY2025)', { x: 0.5, y: 1.7 + h + 0.05, w: 3, h: 0.22, fontSize: 8, color: C.sub, margin: 0, objectName: 'unit' });
  L.marks(s, [
    { x: 4.85, y: 5.15, n: 1 },
    { x: 6.31, y: 3.77, n: 2 },
    { x: 7.2, y: 5.55, n: 3 },
  ]);
  L.lookBox(s, [
    { n: 1, text: '粗利率78.3%。原価738のうち労務365、サーバーを含む外注284' },
    { n: 2, text: `販管費1,117のうち販売費は約409(獲得費)。除けば営業利益率 ${F('calc.opm_ex_sales')}` },
    { n: 3, text: `新規1件の獲得費は約61万円で、約16か月で回収。LTV/CAC ${F('calc.ltv_cac')}` },
  ], { x: 9.5, y: 1.7, w: 3.33, h: 4.49 }); // lint-ok: 台帳に無い手書き(粗利率・原価内訳・販売費・獲得費・回収月数)
};
