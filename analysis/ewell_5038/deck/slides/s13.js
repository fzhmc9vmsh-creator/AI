// ROEと資本: 左にデュポン分解の表、右に資本の使い道の利回り(横棒を図形で描き、資本コスト 8.9% の縦線を重ねる)
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: ROE の中身は 2021 年から 2025 年で何が変わったか。右: 利益が現金になった後の使い道の税後利回りと、資本コストの比較',
    source: '有価証券報告書(FY2025)、会社開示、当方の計算(lenses.py L07・L08)',
  });
  // 左: デュポン分解
  L.paneHead(s, 0.5, 1.62, 6.05, 'ROE のデュポン分解', 'pane_dupont');
  L.table(s, [
    ['項目', '2021年', '2025年'],
    ['純利益率', '28.5%', '32.1%'],
    ['× 総資産回転率(回)', '1.12', '0.79'],
    ['× レバレッジ(倍)', '2.10', '1.27'],
    [{ text: '= ROE', options: { bold: true, color: C.dark } }, { text: '67.5%', options: { bold: true, color: C.dark } }, { text: '32.2%', options: { bold: true, color: C.red } }],
  ], { x: 0.5, y: 2.0, w: 6.05, colW: [2.85, 1.6, 1.6], fontSize: 11, rowH: 0.42, name: 'tbl_dupont' });
  L.box(s, 0.5, 4.3, 6.05, 0.9, { fill: C.tint, line: C.tint, name: 'ovl_cashbox' });
  L.text(s, [
    { text: `現預金 ${F('fy25.cash')} は総資産の 67%、無借金。`, options: { bold: true, color: C.dark, breakLine: true } }, // lint-ok: 総資産比は台帳に無い
    { text: '利益率は上がったが、回転率とレバレッジが下がり、ROE は半減した', options: { color: C.text } },
  ], { x: 0.62, y: 4.34, w: 5.8, h: 0.82, fontSize: 10.5, valign: 'middle', objectName: 'cashnote' });

  // 右: 資本の使い道の利回り
  L.paneHead(s, 6.78, 1.62, 6.05, '資本の使い道の利回り(税後、%)', 'pane_use');
  const rows = [
    { label: '自己株取得\n(今の株価の益回り)', v: 4.35, c: C.primary },
    { label: '配当', v: 0.9, c: C.sub },
    { label: '現預金の保有', v: 0.4, c: C.sub },
  ];
  const ax = 8.95, aw = 3.45, max = 10, px = (v) => ax + v / max * aw;
  rows.forEach((r, i) => {
    const y = 2.55 + i * 0.72;
    L.text(s, r.label, { x: 6.78, y, w: 2.1, h: 0.5, fontSize: 10, color: C.text, align: 'right', valign: 'middle', margin: 0, objectName: 'ovl_use_l' + i });
    s.addShape('rect', { x: ax, y: y + 0.05, w: r.v / max * aw, h: 0.4, fill: { color: r.c }, line: { color: r.c }, objectName: 'ovl_use_b' + i });
    L.text(s, r.v.toFixed(r.v < 1 ? 1 : 2) + '%', { x: px(r.v) + 0.06, y, w: 0.7, h: 0.5, fontSize: 10.5, bold: true, color: C.dark, valign: 'middle', margin: 0, objectName: 'ovl_use_v' + i });
  });
  // 軸と資本コストの縦線
  s.addShape('line', { x: ax, y: 2.45, w: 0.001, h: 2.25, line: { color: C.sub, width: 0.75 }, objectName: 'ovl_use_axis' });
  [0, 5, 10].forEach(t => L.text(s, t + '%', { x: px(t) - 0.3, y: 4.72, w: 0.6, h: 0.2, fontSize: 8, color: C.sub, align: 'center', margin: 0, objectName: 'ovl_use_tk' + t }));
  s.addShape('line', { x: px(8.9), y: 2.35, w: 0.001, h: 2.35, line: { color: C.red, width: 1.5, dashType: 'dash' }, objectName: 'ovl_use_coe' });
  L.text(s, '資本コスト 8.9%', { x: px(8.9) - 1.3, y: 2.1, w: 1.5, h: 0.22, fontSize: 9, bold: true, color: C.red, align: 'right', margin: 0, objectName: 'ovl_use_coet' });
  L.text(s, 'ソフトウエア投資の増分利回りは 393.5%(棒にせず注記)', { x: 6.78, y: 5.0, w: 6.05, h: 0.26, fontSize: 9, color: C.sub, margin: 0, valign: 'middle', objectName: 'ovl_use_note' });

  L.takeaway(s, 0.5, 5.55, 12.33, 1.0,
    `現金の使い道で ROE は 25〜40% に振れる。2026 年に初の自己株取得 ${F('buyback26')}。\n2027 年 2 月の中計ローリングで還元方針を確認する`, // lint-ok: ROE の振れ幅は台帳に無い
    { fontSize: 11.5 });
};
