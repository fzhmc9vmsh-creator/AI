// エグゼクティブサマリ(指示書 spec/ch1_ch4a.md の s02 節)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    title: '構造評価 B・理論株価 251 ドル(株価の 1.75 倍)で「買い検討」。争点は FY29 の FCF と OpenAI の支払能力',
    kicker: 'エグゼクティブサマリ',
    source: '会社開示(Q1 FY27)、コンセンサス(Yahoo・FactSet・tickflow)、需給エンジン第4.3版(calc/out/m8_fair.json)。株価は 2026-10-13 終値',
    page: 2,
  });

  // 上段: 数値タイル 4 枚
  L.kpiTiles(s, [
    { value: '251 ドル', label: '理論株価(確率加重)', note: 'ベース 261・強気 359・弱気 121' },
    { value: '143.20 ドル', label: '株価(10/13)', note: '理論株価の 57%' },
    { value: 'B', label: '構造評価', note: 'S1・A2・B8・C2', color: C.primary },
    { value: '買い検討', label: '最終判断', note: '分割エントリー圏 136〜229 ドル', color: C.dark },
  ], { y: 1.62, h: 1.45 });

  // 下段: 左レール + 本文の 5 行
  const rows = [
    ['結論', '構造は B、価格は理論株価の 57%。ただし争点(FY29 の FCF・OpenAI)で市場との差分が確立していないため「買い」ではなく「買い検討」'],
    ['事業', 'DB 保守・SaaS の現金と顧客の前払い・逼迫前の長期リースで AI 容量を建てる設備先行型(AWS 型)'],
    ['需給', '受注残 6,640 億ドル・確保電力 10GW 超で FY29 までのコンセンサス売上は裏付けあり。FY30 以降は電力と資金が伸びを決める'],
    ['価値', '事業実態 EPS × 妥当 PER(同業 23 倍・成長率×PEG・需給エンジン)を年度別に評価し、近い年度を重くして 251 ドル。DCF 231 ドルと整合'],
    ['市場との差分', '株価は事業実態 EPS の 15.7 倍で弱気(13.6 倍)寄り。疑われているのは EPS ではなく現金化(FY29 の FCF・格付け・OpenAI)'],
  ];
  rows.forEach(([rail, body], i) => {
    const y = 3.25 + i * 0.72;
    const first = i === 0;
    L.box(s, 0.5, y, 2.3, 0.66, { fill: first ? C.dark : C.tint, line: first ? C.dark : C.tint, name: 'ovl_rail' + i });
    L.text(s, rail, { x: 0.62, y, w: 2.1, h: 0.66, fontSize: 12, bold: true, color: first ? C.white : C.dark, valign: 'middle', margin: 0, objectName: 'rail' + i });
    L.text(s, body, { x: 3.0, y, w: 9.83, h: 0.66, fontSize: 11, valign: 'middle', objectName: 'body' + i });
  });
};
