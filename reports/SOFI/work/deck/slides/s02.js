// エグゼクティブサマリ(指示書 spec/ch1_ch4.md の s02 節)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: 'エグゼクティブサマリ',
    source: '会社開示(Q2 2026 決算・10-Q)、コンセンサス(Yahoo・Chartmill・WallStreetZen・Benzinga)、本資料の計算(calc/out/val.json)。株価は 2026-10-16 終値',
  });

  // 上段: 数値タイル 4 枚
  L.kpiTiles(s, [
    { value: '13.4 ドル', label: '理論株価(確率加重)', note: 'ベース 13.3・強気 16.5・弱気 10.5' },
    { value: '14.55 ドル', label: '株価(10/16)', note: '理論株価の 1.09 倍' },
    { value: 'C', label: '構造評価', note: 'S1・B7・C4(条件9 は対象外)', color: C.amber },
    { value: '監視', label: '最終判断', note: '分割エントリーの目安 11.3 ドル以下', color: C.dark },
  ], { y: 1.62, h: 1.45 });

  // 下段: 左レール + 本文の 5 行
  const rows = [
    ['結論', '構造は C、株価は理論株価をやや上回る(乖離 −8%)。買いの根拠になる市場との差分は無く「監視」。\n11.3 ドル以下、または判別 KPI の合格で再検討する'],
    ['事業', '会員 1,580 万人の給与振込が預金 455 億ドルを集め、その安い資金で個人・学生ローンを抱えて利ざやを稼ぐ銀行型フィンテック'],
    ['成長の質', 'EPS はコンセンサスどおり 0.60 → 1.32 ドル(2026→29 年)に伸びうるが、成長は資本を食い、\nROTCE は 2030 年でも 14.5% と資本コスト 13.9% 近辺にとどまる'],
    ['価値', '事業実態 EPS × 妥当 PER(同業 13.6 倍・PEG × 成長率・エンジン)を年度別に当て、近い年度を重くしてベース 13.3 ドル。\nDCF 10.6 ドル・TBV×ROTCE 8〜11 ドルはさらに低い'],
    ['市場との差分', '株価は会社計画の達成を約 4 割の確率で織り込む。空売りの会計疑義は信用の前提では裏付けが弱いが、\n金利に弱い評価と資本の制約は実在のリスク。差分は無い'],
  ];
  rows.forEach(([rail, body], i) => {
    const y = 3.25 + i * 0.72;
    const first = i === 0;
    L.box(s, 0.5, y, 2.3, 0.66, { fill: first ? C.dark : C.tint, line: first ? C.dark : C.tint, name: 'ovl_rail' + i });
    L.text(s, rail, { x: 0.62, y, w: 2.1, h: 0.66, fontSize: 12, bold: true, color: first ? C.white : C.dark, valign: 'middle', margin: 0, objectName: 'rail' + i });
    L.text(s, body, { x: 3.0, y, w: 9.83, h: 0.66, fontSize: 11, valign: 'middle', objectName: 'body' + i });
  });
};
