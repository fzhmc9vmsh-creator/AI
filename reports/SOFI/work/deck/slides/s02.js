// エグゼクティブサマリ(指示書 spec/ch1_ch4.md の s02 節)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: 'エグゼクティブサマリ',
    source: '会社開示(Q2 2026 決算・10-Q)、コンセンサス(Yahoo・Chartmill・WallStreetZen・Benzinga)、本資料の計算(calc/out/val.json)。株価は 2026-10-16 終値、calc/out/growth_v2.json',
  });

  // 上段: 数値タイル 4 枚
  L.kpiTiles(s, [
    { value: '14.7 ドル', label: '理論株価(確率加重)', note: 'ベース 14.9・強気 18.2・弱気 11.8' },
    { value: '14.55 ドル', label: '株価(10/16)', note: '理論株価の 0.99 倍' },
    { value: 'B', label: '構造評価', note: 'S1・B8・C3(条件 9 は対象外)', color: L.GRADE.B.fill },
    { value: '監視', label: '最終判断', note: '分割エントリーの目安 13.2 ドル以下', color: C.dark },
  ], { y: 1.62, h: 1.45 });

  // 下段: 左レール + 本文の 5 行
  const rows = [
    ['結論', '構造は B(C との境界)、株価は理論株価とほぼ同じ(乖離 +1%)。市場との差分は無く「監視」。\n13.2 ドル以下、または判別 KPI の合格で再検討する'],
    ['事業', '会員 1,580 万人の給与振込が預金 455 億ドルを集め、その安い資金で個人・学生ローンを抱えて利ざやを稼ぐ銀行型フィンテック'],
    ['成長の質', '販促費 +48% は攻めの再投資(6 検査中 4 つ)で、単位経済は正(経済的 LTV/CAC 約 2 倍)。\nクロスバイは 51% に加速。ただし自己資本の自給率は 0.34 で、成長を律速する'],
    ['価値', '構造 B の許容 PEG(1.0〜1.15)を年度別に当ててベース 14.9 ドル、節点ツリーの期待値 14.7 ドル。\n強気(うまくいった場合)18.2 ドル・確率 22%、弱気 11.8 ドル・30%'],
    ['市場との差分', '株価は強気の確率 約 17% を織り込み、本資料の 22% との差は感応度の幅の内側。\n銀行免許による資金の優位(年 7.1 億ドル)は既に NIM に入っている。差分は無い'],
  ];
  rows.forEach(([rail, body], i) => {
    const y = 3.25 + i * 0.72;
    const first = i === 0;
    L.box(s, 0.5, y, 2.3, 0.66, { fill: first ? C.dark : C.tint, line: first ? C.dark : C.tint, name: 'ovl_rail' + i });
    L.text(s, rail, { x: 0.62, y, w: 2.1, h: 0.66, fontSize: 12, bold: true, color: first ? C.white : C.dark, valign: 'middle', margin: 0, objectName: 'rail' + i });
    L.text(s, body, { x: 3.0, y, w: 9.83, h: 0.66, fontSize: 11, valign: 'middle', objectName: 'body' + i });
  });
};
