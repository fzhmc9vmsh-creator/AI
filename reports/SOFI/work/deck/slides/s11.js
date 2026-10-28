// 2-4 競争優位: 体験の束(指示書 spec/v4.md の s11 節。手本: s04 の表 + s15b の takeaway)
// タイトル・ページ番号は meta.js が入れる。左: 体験の束の同業比較の表、右: 束の差が数字に出ているかの表(SoFi は Q3 2026)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 体験の束を同業と比べる(○ あり / × なし / — 未確認。各社の公開情報の理解で原文とは未照合)。右: 束の差が数字に出ているか',
    source: 'research_r5/Q3_datasheet.md、research_r4/R16_flywheel_quality_holding.md、research_r4/R17_credit_capital_peers.md、research/R1b_kpi.md、各社の公開情報',
  });

  // ---- 左: 体験の束の同業比較(SoFi の列は tint の地に太字) ----
  L.paneHead(s, 0.5, 1.62, 7.6, '体験の束の要素(同業との比較)', 'pane_l');
  const so = (t) => ({ text: t, options: { fill: { color: C.tint }, bold: true } });
  L.table(s, [
    ['要素', 'SoFi', 'Chime', 'LendingClub', 'Ally', 'Robinhood'],
    ['銀行免許(自前の預金)', so('○'), '×(提携銀行)', '○', '○', '×'],
    ['給与の早期受け取り', so('○(最大 2 日)'), '○', '—', '—', '—'],
    ['個人ローン', so('○'), '×', '○', '×', '×'],
    ['学生ローン', so('○'), '×', '×', '×', '×'],
    ['証券・暗号資産', so('○'), '×', '×', '○(証券)', '○'],
    ['有料会員', so('○(Plus)'), '—', '×', '×', '○(Gold)'],
    ['会員向けのローン金利割引', so('○(各 0.25%)'), '—', '—', '—', '—'],
  ], {
    x: 0.5, y: 2.0, w: 7.6, colW: [1.9, 1.1, 1.1, 1.3, 1.1, 1.1], fontSize: 9.5, rowH: 0.42,
    align: ['left', 'center', 'center', 'center', 'center', 'center'], name: 'tbl_bundle',
  });

  // ---- 右: 束の差が数字に出ているか(SoFi は Q3 2026) ----
  L.paneHead(s, 8.35, 1.62, 4.48, '束の差が数字に出ているか(Q3 2026)', 'pane_r');
  L.table(s, [
    ['指標', 'SoFi', '比較'],
    ['獲得費(製品当たり)', '202 ドル', '会員当たり 370 ドルの約半分'],
    ['個人ローンの純償却', '2.26%', 'LendingClub 3.2%・\nDiscover 4.2%'],
    ['預金の基本金利', '3.30%', 'Ally・Amex 3.10%、\nMarcus 3.50%、\nChime 最大 4.00%(同業の中位)'],
    ['預金の伸び(前年比)', '+56%', '新規は上乗せ +1.10% で集める'],
    ['資金(倉庫ライン比)', '−1.45pt', '年 7.45 億ドルの節約'],
  ], {
    x: 8.35, y: 2.0, w: 4.48, colW: [1.45, 0.85, 2.18], fontSize: 9, rowH: 0.56,
    align: ['left', 'center', 'left'], name: 'tbl_numbers',
  });

  // 下端: 結論(単品は市場の商品、束で 3 つが同業より低い)
  L.takeaway(s, 0.5, 5.95, 12.33, 0.7, '単品(ローン・預金)は市場の商品。だが束では獲得費と貸倒が同業より低い。\n全部の要素を持つのは SoFi だけで、預金の基本金利は同業の中位でも預金は前期比 +58 億ドル');
  return s;
};
