// エグゼクティブサマリ(指示書 spec/v3.md の s02 節)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: 'エグゼクティブサマリ',
    source: '会社開示(Q2 2026 決算・10-Q)、コンセンサス(Yahoo・Chartmill・WallStreetZen・Benzinga)、本資料の計算(calc/out/growth_v3.json)。株価は 2026-10-16 終値',
  });

  // 上段: 数値タイル 4 枚
  L.kpiTiles(s, [
    { value: '21.9 ドル', label: '理論株価(エンジン)', note: '期待値 21.4・強気 31.2・弱気 12.9' },
    { value: '14.55 ドル', label: '株価(10/16)', note: '理論株価の 0.66 倍' },
    { value: 'B', label: '構造評価', note: 'S1・A2・B9(C は 0)', color: L.C.primary },
    { value: '買い(分割)', label: '最終判断', note: '分割 14.3〜19.6 ドル、即時 14.3 以下', color: C.dark },
  ], { y: 1.62, h: 1.45 });

  // 下段: 左レール + 本文の 5 行
  const rows = [
    ['結論', '構造は B(上方の留保)、理論株価 21.9 ドルは株価の +51%。B 行の「買い」で、分割で建てる。\nQ3 決算(10/27)で評価の純額・貸倒・販促費を確かめる'],
    ['事業', '会員 1,580 万人が 1 つのアプリで預金・ローン・投資を使い、給与振込の預金 455 億ドルで\nローンを抱えて利ざやを稼ぐ。フェーズ ③(収益 +40%・黒字・販促費 32%)の上端'],
    ['成長の質', '会員は前年比 35% を維持し製品は加速(43%)。EPS の横ばいは税と株数で、税引前は +82%。\n束では獲得費・貸倒・資金が同業より低い。律速は自己資本'],
    ['価値', '妥当 PER = 許容 PEG 1.25 × 3 年の成長率 31%。年度別に当ててエンジン 21.9 ドル(PEG 1.0 でも 18.3)。\n強気 31.2 ドル・確率 24%、弱気 12.9 ドル・28%'],
    ['市場との差分', '株価は損失率 +2.3pt が毎年続く前提(同業の最悪期 5.0% を上回る)と構造 C の PEG 0.85 を織り込む。\n信用 +1pt・金利 +100bp・増資を同時に置いても 17.7 ドル'],
  ];
  rows.forEach(([rail, body], i) => {
    const y = 3.25 + i * 0.72;
    const first = i === 0;
    L.box(s, 0.5, y, 2.3, 0.66, { fill: first ? C.dark : C.tint, line: first ? C.dark : C.tint, name: 'ovl_rail' + i });
    L.text(s, rail, { x: 0.62, y, w: 2.1, h: 0.66, fontSize: 12, bold: true, color: first ? C.white : C.dark, valign: 'middle', margin: 0, objectName: 'rail' + i });
    L.text(s, body, { x: 3.0, y, w: 9.83, h: 0.66, fontSize: 11, valign: 'middle', objectName: 'body' + i });
  });
};
