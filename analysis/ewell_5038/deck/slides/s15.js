// 価値の芯: 感応度のトルネード図(図形で描く。0 を中心に左が下振れ・右が上振れ、1 株あたりの円)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '変数を 1 つずつ動かしたときの理論株価の変化(1 株あたり、円)。上から上振れの大きい順。棒の下の小さな字が振れ幅の根拠',
    source: 'valuation.json の感応度(当方の計算)',
  });
  L.paneHead(s, 0.5, 1.62, 8.2, '理論株価への影響(円/株)', 'pane_tor');
  const rows = [
    { label: '資本コスト(評価の前提)', basis: '8.0〜9.5%', up: 349.3, dn: -174.5, upc: C.sub, dnc: C.rule, upl: '8.0%  +349.3', dnl: '9.5%  −174.5' },
    { label: '契約数', basis: '獲得 520〜820 件・解約 4.8〜6.0%', up: 132.4, dn: -26.1, upc: C.primary, dnc: C.red, upl: '強気  +132.4', dnl: '弱気  −26.1' },
    { label: '単価', basis: '年 +2.5〜8%', up: 130.3, dn: -37.1, upc: C.sub, dnc: C.red, upl: '強気  +130.3', dnl: '弱気  −37.1' },
    { label: '粗利率', basis: '74〜77.5%', up: 32.6, dn: -59.5, upc: C.sub, dnc: C.red, upl: '強気  +32.6', dnl: '弱気  −59.5' },
  ];
  const x0 = 3.7, x1 = 8.0, lo = -185, hi = 360, sc = (x1 - x0) / (hi - lo), zx = x0 - lo * sc;
  const y0 = 2.2, pitch = 0.82, bh = 0.46;
  s.addShape('line', { x: zx, y: y0 - 0.1, w: 0.001, h: pitch * rows.length, line: { color: C.sub, width: 1 }, objectName: 'ovl_tor_zero' });
  rows.forEach((r, i) => {
    const y = y0 + i * pitch;
    L.text(s, [
      { text: r.label, options: { bold: true, color: C.dark, fontSize: 10.5, breakLine: true } },
      { text: r.basis, options: { color: C.sub, fontSize: 8 } },
    ], { x: 0.85, y: y - 0.04, w: 2.1, h: 0.62, valign: 'middle', margin: 0, objectName: 'ovl_tor_l' + i });
    s.addShape('rect', { x: zx, y, w: r.up * sc, h: bh, fill: { color: r.upc }, line: { color: r.upc }, objectName: 'ovl_tor_u' + i });
    s.addShape('rect', { x: zx + r.dn * sc, y, w: -r.dn * sc, h: bh, fill: { color: r.dnc }, line: { color: r.dnc }, objectName: 'ovl_tor_d' + i });
    L.text(s, r.upl, { x: zx + r.up * sc + 0.05, y, w: 1.0, h: bh, fontSize: 9, bold: true, color: C.dark, valign: 'middle', margin: 0, objectName: 'ovl_tor_ul' + i });
    L.text(s, r.dnl, { x: zx + r.dn * sc - 1.05, y, w: 1.0, h: bh, fontSize: 9, bold: true, color: C.dark, align: 'right', valign: 'middle', margin: 0, objectName: 'ovl_tor_dl' + i });
  });
  L.text(s, '← 下振れ(円/株)          上振れ(円/株) →', { x: x0, y: y0 + rows.length * pitch - 0.1, w: x1 - x0, h: 0.22, fontSize: 8.5, color: C.sub, align: 'center', margin: 0, objectName: 'ovl_tor_axis' });
  L.marks(s, [
    { x: 0.5, y: y0 + 0.12, n: 1 },
    { x: 0.5, y: y0 + pitch + 0.12, n: 2 },
    { x: 0.5, y: y0 + 2 * pitch + 0.12, n: 2 },
    { x: 0.5, y: y0 + 3 * pitch + 0.12, n: 3 },
  ]);
  L.lookBox(s, [
    { n: 1, text: '最大は資本コストで、倍率の差そのもの。事業の見立てではなく割引率の置き方が価値を動かす' },
    { n: 2, text: '事業では契約数と単価が並ぶ。上振れが大きいのは、成長 15% 超で妥当 PER の式が切り替わるため' }, // lint-ok: 15% は式の切り替え条件
    { n: 3, text: '粗利率は下振れ(−59.5 円)が上振れ(+32.6 円)より大きい非対称。事業の変数で最大の下振れ' }, // lint-ok: 感応度の値
  ], { x: 8.95, y: 1.98, w: 3.88, h: 3.55 });
  L.takeaway(s, 0.5, 5.75, 12.33, 0.95,
    '判別 KPI の最上位は年間の新規獲得件数(2027-02-12 頃)。\n680 件以下で続行、720 件以上で見直す', // lint-ok: 判別の線は仮説書の値
    { fontSize: 11.5 });
};
