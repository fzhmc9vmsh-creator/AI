// エグゼクティブサマリ(指示書 spec/ch1_ch4a.md の s02 節、r8b_judgment.md の担当 H3 で更新)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    title: '構造評価 B・理論株価 245 ドル(株価の 1.76 倍)で「買い」。株価は価値の分布の 9 パーセンタイルで、下回るのは AI の循環が早く崩れる道だけ',
    kicker: 'エグゼクティブサマリ',
    source: '会社開示(Q1 FY27)、Investor Day 2026-10-28(8-K Ex.99.1・CFO 資料)、需給エンジン第4.5版(calc/out/m10_fair.json・m10_extra.json・m10_sens.json)。株価は 2026-10-29 終値',
    page: 2,
  });

  // 上段: 数値タイル 4 枚
  L.kpiTiles(s, [
    { value: '245 ドル', label: '理論株価(確率加重)', note: 'ベース 246・強気 354・弱気 134' },
    { value: '139.56 ドル', label: '株価(10/29)', note: '理論株価の 57%' },
    { value: 'B', label: '構造評価', note: 'S1・A3・B9', color: C.primary },
    { value: '買い', label: '最終判断', note: '株価は即エントリー上限 151 ドルの下', color: C.dark },
  ], { y: 1.62, h: 1.45 });

  // 下段: 左レール + 本文の 5 行
  const rows = [
    ['結論', '構造は B、価格は理論株価の 57%。株価は 1,500 通りの価値の分布の 9 パーセンタイルで、価値が株価を下回るのは\nAI の循環が早く崩れる道だけ。市場との差分が分析で確立したため「買い」'],
    ['事業', 'DB 保守・SaaS の現金と顧客の前払い・他人の建屋で AI 容量を建てる。1GW は年 160 億ドルの売上に capex 370 億ドル、\n粗利率 35%(コストプラス契約)'],
    ['需給', '学習から推論へ: 推論は AI 計算の約 2/3。企業データの近くで動き、DB・OCI・アプリと一緒に売れる。\nERP の約半分がオンプレで、移行は売上 3〜4 倍'],
    ['価値', '会社の EPS(FY27 8.10・FY30 21)× 妥当 PER を年度別に評価して 245 ドル。DCF 229 ドル。\n芯は契約後の再契約の単価(経営者の発言どおりなら +48 ドル)'],
    ['市場との差分', '市場は信用リスクを高く評価するが、全 1,500 通りでレバレッジは最大 4.4 倍で倒産の道はない。\n本当のリスクは OpenAI 集中と、建設の遅れによる一時 BB+(40%)'],
  ];
  rows.forEach(([rail, body], i) => {
    const y = 3.25 + i * 0.72;
    const first = i === 0;
    L.box(s, 0.5, y, 2.3, 0.66, { fill: first ? C.dark : C.tint, line: first ? C.dark : C.tint, name: 'ovl_rail' + i });
    L.text(s, rail, { x: 0.62, y, w: 2.1, h: 0.66, fontSize: 12, bold: true, color: first ? C.white : C.dark, valign: 'middle', margin: 0, objectName: 'rail' + i });
    L.text(s, body, { x: 3.0, y, w: 9.83, h: 0.66, fontSize: 11, valign: 'middle', objectName: 'body' + i });
  });
};
