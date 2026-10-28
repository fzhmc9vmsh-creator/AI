// 事業理解(1/3): 事業の積み木(左)+ 8 群の 5W1H 台帳(右)+ 用語の注釈(下)
module.exports = function build(pres, L) {
  const { C, FONT } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 事業の積み木(何を、どの資金で売るか)。右: 8 群の 5W1H 台帳。下: この資料で使う用語の注釈',
    source: '会社開示(Q3 2026 決算の 8-K・説明会の要約)、research_r5/Q3_datasheet.md、research_r2/R9_products_people.md(各社の価格表の第三者集計)。残高は公正価値の額。(Q2)は前期の値',
  });

  // ---------- 左: 事業の積み木(層 × 資金の出どころ) ----------
  L.paneHead(s, 0.5, 1.62, 4.45, '事業の積み木(層 × 資金の出どころ)');
  const cx = [1.5, 2.65, 3.8], cw = 1.1, ry = [2.3, 3.1, 3.9], ch = 0.72;
  ['自社の資金\n(B/S)', '他社の資金\n(LPB)', '他社へ提供\n(B2B)'].forEach((t, j) =>
    L.text(s, t, { x: cx[j], y: 1.96, w: cw, h: 0.32, fontSize: 9, bold: true, color: C.dark, align: 'center', valign: 'middle', margin: 0, objectName: 'blk_colh' + j }));
  ['借りる', '預ける・使う', '増やす', '土台'].forEach((t, i) =>
    L.text(s, t, { x: 0.5, y: i < 3 ? ry[i] : 4.7, w: 0.95, h: i < 3 ? ch : 0.42, fontSize: 9, bold: true, color: C.dark, align: 'center', valign: 'middle', margin: 0, objectName: 'blk_rowh' + i }));

  // 種類: tint = 上積み(薄緑)/ key = 利益の柱(濃緑)/ grow = 成長(緑)/ none = 該当なし(灰)
  const KIND = {
    tint: { fill: C.tint, line: C.light, color: C.dark, bold: false },
    key: { fill: C.dark, line: C.dark, color: C.white, bold: false },
    grow: { fill: C.primary, line: C.primary, color: C.white, bold: false },
    none: { fill: C.gray, line: C.gray, color: C.sub, bold: false },
  };
  const cell = (i, j, k, str) => {
    const o = KIND[k];
    s.addText(str, { shape: 'roundRect', rectRadius: 0.06, x: cx[j], y: ry[i], w: cw, h: ch, fill: { color: o.fill }, line: { color: o.line, width: 0.75 },
      fontFace: FONT, fontSize: 8.5, color: o.color, align: 'center', valign: 'middle', margin: 0.02, objectName: `blk_c${i}${j}` });
  };
  cell(0, 0, 'key', '個人ローン・\n学生ローン・\n住宅ローン');
  cell(0, 1, 'grow', 'LPB\n(個人・中小企業・\nホームエクイティ)');
  cell(0, 2, 'none', '—');
  cell(1, 0, 'key', 'SoFi Money\n(預金・カード)');
  cell(1, 1, 'tint', 'SoFiUSD・\n暗号資産');
  cell(1, 2, 'tint', '法人銀行\n(Big Business\nBanking)');
  cell(2, 0, 'tint', 'SoFi Invest・\nPlus(月 10 ドル)');
  cell(2, 1, 'none', '—');
  cell(2, 2, 'tint', 'Galileo・\nTechnisys\n(口座の基盤)');
  s.addText('銀行免許(SoFi Bank, N.A.、2022 年)と自社の技術基盤', { shape: 'roundRect', rectRadius: 0.06, x: cx[0], y: 4.7, w: cx[2] + cw - cx[0], h: 0.42,
    fill: { color: C.gray }, line: { color: C.rule, width: 0.75 }, fontFace: FONT, fontSize: 8.5, color: C.dark, align: 'center', valign: 'middle', margin: 0.04, objectName: 'blk_base' });
  L.text(s, '濃緑 = 利益の柱、緑 = 成長、薄緑 = 上積み', { x: 0.5, y: 5.2, w: 4.45, h: 0.32, fontSize: 8.5, color: C.sub, valign: 'middle', margin: 0, objectName: 'blk_legend' });

  // ---------- 右: 8 群の 5W1H 台帳 ----------
  L.paneHead(s, 5.15, 1.62, 7.68, '8 群の 5W1H 台帳(規模は Q3 2026。(Q2)は前期の値)');
  // 役割の列の色: 利益の柱=濃緑太字 / 成長=緑太字 / 上積み系=ティール / 他=灰
  const role = (text, options) => ({ text, options });
  const dark = { color: C.dark, bold: true };
  const green = { color: C.primary, bold: true };
  const teal = { color: C.teal };
  const grey = { color: C.sub };
  L.table(s, [
    ['群', '誰が買う', '何を・どう課金', '規模(前年比)', '役割'],
    ['個人ローン\n(B/S で保有)', 'FICO 746・年収 15.8 万\nドルの会員', '固定 6.99〜35.49%・手数料 0〜7%\n平均クーポン 13.0%(Q2)', '残高 約 321 億ドル\n組成 126 億(+69%)', role('利益の柱', dark)],
    ['学生ローン\n(借換・大学院)', 'FICO 765 の会員\n大学院生(Grad PLUS 廃止)', '大学院 固定 2.45〜14.83%\n平均クーポン 5.9%(Q2)', '残高 約 185 億ドル\n組成 29 億(+96%)', role('成長', green)],
    ['LPB', 'Blue Owl・Fortress など\n投資家と銀行', '組成して引き渡し、手数料 4.3%\nサービシングは保持', '組成 36 億ドル\n手数料 1.53 億', role('成長', green)],
    ['SoFi Money\n(預金・カード)', '給与振込の会員\n(預金の約 9 割)', '普通預金 3.30%(条件付き)\nインターチェンジ', '預金 513 億ドル\n口座 790 万(Q2)', role('利益の柱', dark)],
    ['SoFi Invest・Plus', '個人投資家・会員', '売買手数料 0 ドル\nPlus は月 10 ドル', '口座 390 万(Q2)\nPlus 有料 20.6 万人(Q2)', role('上積み', teal)],
    ['住宅ローン・HE', '住宅を持つ会員', '固定金利。売却または LPB', '残高 約 18 億ドル\n組成 14 億(+44%)', role('選択的', grey)],
    ['Tech Platform\n(Galileo)', 'フィンテック・銀行', '口座数・処理件数に課金', '収益 0.87 億ドル\n(−24%。大口除き +18%)', role('回復', grey)],
    ['新領域', '中小企業・法人・会員', '中小企業ローン・SoFiUSD・\n暗号資産・法人銀行', 'SoFiUSD 流通\n約 3 億ドル(Q2 報道)', role('選択的', grey)],
  ], {
    x: 5.15, y: 1.98, w: 7.68, colW: [1.4, 1.7, 2.2, 1.6, 0.78], fontSize: 8.5, rowH: 0.4,
    align: ['left', 'left', 'left', 'left', 'center'],
  });

  // ---------- 下: 用語の注釈(この資料に出てくる順) ----------
  L.paneHead(s, 0.5, 5.58, 12.33, '用語の注釈(この資料に出てくる順)');
  const terms = [
    ['会員', 'SoFi の製品を 1 つ以上持つ顧客。1,710 万人(+36%)'],
    ['製品', '会員が持つ口座・ローンの数。会員当たり 1.56'],
    ['クロスバイ', '新製品のうち既存会員が開いた比率。51%'],
    ['LPB', '他社の資金でローンを組成し手数料を得る事業'],
    ['NIM', '利付資産に対する純金利収益の比率。6.14%'],
    ['公正価値(マーク)', '時価の額面比。個人 104.7%(Q2)'],
    ['貸倒率(all-in)', '売却した延滞債権を足し戻した純償却率'],
    ['ROTCE', '有形自己資本に対する利益率。7〜9%'],
    ['TBV(TBVPS)', '有形自己資本(1 株当たり 7.48 ドル)'],
    ['総自己資本比率', '自己資本 ÷ リスク資産(RWA)。17.0%'],
    ['倉庫ライン', '銀行から借りる短期の資金枠。預金より高い'],
    ['SoFiUSD', 'SoFi Bank が発行するドル連動のステーブルコイン'],
  ];
  terms.forEach(([term, desc], k) => {
    const col = Math.floor(k / 4), row = k % 4;
    L.text(s, [
      { text: term, options: { bold: true, color: C.dark } },
      { text: ' — ' + desc, options: { color: C.text } },
    ], { x: [0.5, 4.65, 8.8][col], y: 5.92 + row * 0.2, w: 4.03, h: 0.2, fontSize: 8.5, margin: 0, valign: 'middle', objectName: `note_${k}` });
  });
  return s;
};
