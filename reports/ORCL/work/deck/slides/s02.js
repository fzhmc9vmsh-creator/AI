// エグゼクティブサマリ(指示書 spec/ch1_ch4a.md の s02 節)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    title: '構造評価 B・理論株価 236 ドル(株価の 1.69 倍)で「買い検討」を維持。説明会で資金の道筋は見えたが、価値の芯は契約後の更新単価',
    kicker: 'エグゼクティブサマリ',
    source: '会社開示(Q1 FY27)、Investor Day 2026-10-28(8-K Ex.99.1・CFO 資料)、需給エンジン第4.4版(calc/out/m9_fair.json・m9_extra.json)。株価は 2026-10-29 終値',
    page: 2,
  });

  // 上段: 数値タイル 4 枚
  L.kpiTiles(s, [
    { value: '236 ドル', label: '理論株価(確率加重)', note: 'ベース 233・強気 340・弱気 138' },
    { value: '139.56 ドル', label: '株価(10/29)', note: '理論株価の 59%' },
    { value: 'B', label: '構造評価', note: 'S1・A2・B8・C2', color: C.primary },
    { value: '買い検討', label: '最終判断', note: '株価は分割圏 155〜204 ドルの下', color: C.dark },
  ], { y: 1.62, h: 1.45 });

  // 下段: 左レール + 本文の 5 行
  const rows = [
    ['結論', '構造は B、価格は理論株価の 59%。説明会で資金の道筋は示されたが、事前に決めた引き上げ条件(CDS 200bp 未満など)が\n未達のため「買い検討」を維持'],
    ['事業', 'DB 保守・SaaS の現金と顧客の前払い・他人の建屋で AI 容量を建てる。1GW は年 160 億ドルの売上に capex 370 億ドル、\n粗利率 35%(コストプラス契約)'],
    ['需給', '容量は FY26 約 3GW → FY28 末 約 10GW(会社)。受注残 6,640 億ドルの約 9 割がクラウド基盤。FY31 以降の伸びは\n自己資金と契約後の更新単価が決める'],
    ['価値', '会社の EPS(FY27 8.10・FY30 21)× 妥当 PER を年度別に評価して 236 ドル。DCF 210 ドル。第4.3版から −15\n(1GW の粗利率 35% −19、容量 −13、会社の EPS +8、1GW の単価 +7)'],
    ['市場との差分', '株価は弱気の値(138 ドル)とほぼ同じ。CDS 277bp は 5 年で 21% の倒産を織り込むが、エンジンは 1.9%。\nCDS の確率で割り引いても DCF は 170 ドル'],
  ];
  rows.forEach(([rail, body], i) => {
    const y = 3.25 + i * 0.72;
    const first = i === 0;
    L.box(s, 0.5, y, 2.3, 0.66, { fill: first ? C.dark : C.tint, line: first ? C.dark : C.tint, name: 'ovl_rail' + i });
    L.text(s, rail, { x: 0.62, y, w: 2.1, h: 0.66, fontSize: 12, bold: true, color: first ? C.white : C.dark, valign: 'middle', margin: 0, objectName: 'rail' + i });
    L.text(s, body, { x: 3.0, y, w: 9.83, h: 0.66, fontSize: 11, valign: 'middle', objectName: 'body' + i });
  });
};
