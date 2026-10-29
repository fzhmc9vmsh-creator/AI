// エグゼクティブサマリ(指示書 spec/v4.md の s02 節。kpiTiles 4 枚 + 左レールの 5 行)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: 'エグゼクティブサマリ',
    source: 'research_r5/Q3_datasheet.md(Q3 の 8-K・説明会の要約)、calc/out/growth_v4.json。株価は 2026-10-16 終値、決算後の目安は 10/27 の報道',
  });

  // 上段: 数値タイル 4 枚
  L.kpiTiles(s, [
    { value: '23.8 ドル', label: '理論株価(エンジン)', note: '期待値 24.2・強気 33.5・弱気 13.9' },
    { value: '14.55 ドル', label: '株価(10/16)', note: '決算後の目安 16.5 ドル' },
    { value: 'B', label: '構造評価', note: 'S1・A3・B8(C は 0)', color: L.C.primary },
    { value: '買い(分割)', label: '最終判断', note: '分割 15.3〜21.4 ドル、即時 15.3 以下', color: C.dark },
  ], { y: 1.62, h: 1.45 });

  // 下段: 左レール + 本文の 5 行
  const rows = [
    ['結論', '構造は B(上方の留保)、理論株価 23.8 ドルは株価の +45〜64%。B 行の「買い」で、分割で建てる。\n次の確認は Q4 決算の総自己資本比率と LPB の割合'],
    ['事業', '会員 1,710 万人が 1 つのアプリで預金・ローン・投資・決済を使い、預金 513 億ドルでローンを抱えて\n利ざやを稼ぐ。手数料型の収益は 42%。フェーズ ③(収益 +44%・黒字・販促費 32%)の上端で加速'],
    ['成長の質', '会員は前年比 36%・純増 120 万で過去最高、製品は +44%。会員 1 人の年間収益は 337 ドル(+5%)。\n束では獲得費・貸倒が同業より低い。律速は自己資本(比率 17.0%)'],
    ['価値', '妥当 PER = 許容 PEG 1.275 × 3 年の成長率 32.5%。年度別に当ててエンジン 23.8 ドル(PEG 1.0 でも 19.5)。\n2027 年 EPS 0.90 は会社の見通し。強気 33.5 ドル・確率 27%、弱気 13.9 ドル・24%'],
    ['市場との差分', '株価は損失率 +2.1〜2.7pt の恒常化とPEG 0.80〜0.90(構造 C の 1.0 未満)を織り込む。実績の損失率は 3.4% に改善。\n信用 +1pt・金利 +100bp・増資を同時に置いても 19.4 ドル'],
  ];
  rows.forEach(([rail, body], i) => {
    const y = 3.25 + i * 0.72;
    const first = i === 0;
    L.box(s, 0.5, y, 2.3, 0.66, { fill: first ? C.dark : C.tint, line: first ? C.dark : C.tint, name: 'ovl_rail' + i });
    L.text(s, rail, { x: 0.62, y, w: 2.1, h: 0.66, fontSize: 12, bold: true, color: first ? C.white : C.dark, valign: 'middle', margin: 0, objectName: 'rail' + i });
    L.text(s, body, { x: 3.0, y, w: 9.83, h: 0.66, fontSize: 11, valign: 'middle', objectName: 'body' + i });
  });
};
