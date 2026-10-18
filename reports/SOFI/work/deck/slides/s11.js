// 2-4 競争優位(手本 ORCL s11 を写経。左: 競合比較の表、右: ファイブフォース。タイトル・ページ番号は meta.js が入れる)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 競合に対する価格・品質・差を生む活動(各社の公表レンジ、2026 年)。右: ファイブフォース(各力の強さと SoFi の利ざやへの効き)',
    source: 'research_r2/R9_products_people.md(LendingTree・NerdWallet・各社ページ・J.D. Power)、research/R4_scuttlebutt.md(預金金利・TransUnion)',
  });

  // ---- 左: 競合比較 ----
  L.paneHead(s, 0.5, 1.62, 6.05, '競合比較: 品質 × 価格 × 価値連鎖', 'pane_l');
  L.table(s, [
    ['製品', '価格(対競合)', '品質', '差を生む活動'],
    ['個人ローン', 'APR 6.99〜35.49%・手数料 0〜7%。\nLightStream 6.49〜25.39%・\n手数料なし', 'アプリ評価 4.7。\n借り手 FICO 746', '会員の基盤と\n安い預金'],
    ['普通預金', '3.30%(給与振込が条件)。\nAlly 4.00・Amex 3.90・\nChime 3.75%', 'NerdWallet 5.0、\n月額手数料なし', '給与振込で\n主口座になる'],
    ['大学院ローン', '固定 2.45〜14.83%。\n連邦 PLUS 9.07%+手数料 4.2%', 'Yale が代替の\n筆頭に案内', '借換で培った\n審査'],
    ['投資', '売買手数料 0 ドル(競合も 0)', 'J.D. Power\nDIY 部門 1 位', 'アプリの一体化'],
    ['会員サブスク', 'Plus 月 10 ドル。Robinhood\nGold 5 ドル、Chime Prime 無料', '有料 20.6 万人', '預金金利の\n上乗せ'],
  ], {
    x: 0.5, y: 2.0, w: 6.05, colW: [1.25, 1.75, 1.55, 1.5], fontSize: 9, rowH: 0.6,
    align: ['left', 'left', 'left', 'left'], name: 'tbl_compete',
  });
  L.takeaway(s, 0.5, 5.75, 6.05, 0.95, '安いのは学生ローンだけで、個人ローンと Plus は割高。それでも預金は競合より安く集まる。優位は価格ではなく、給与振込で主口座になる関係');

  // ---- 右: ファイブフォース(中央は SoFi の利ざや。右下は takeaway) ----
  L.paneHead(s, 6.78, 1.62, 6.05, 'ファイブフォース(業界構造)', 'pane_r');
  const BW = 1.9, BH = 1.45;
  const STR = { 弱: C.primary, 中: C.amber, 強: C.red };
  const forces = [
    { id: 'rival', x: 6.78, y: 2.0, name: '業界内の競争', str: '強', fact: '個人ローン残高 2,810 億ドル(+9.6%)を LendingClub・Upstart・大手行が奪い合う' },
    { id: 'entry', x: 8.855, y: 2.0, name: '新規参入', str: '中', fact: '銀行免許は 1〜3 年・払込資本 7.5 億ドル。規制緩和で取得は容易に(Upstart が申請)' },
    { id: 'supp', x: 6.78, y: 3.55, name: '資金の出し手(供給者)', str: '弱', fact: '預金者は給与振込で定着。LPB の買い手は契約 100 億ドル超で取り合い' },
    { id: 'buyer', x: 10.93, y: 3.55, name: '借り手(買い手)', str: '中', fact: 'FICO 746 の高所得層は他行も欲しい顧客。金利で乗り換える' },
    { id: 'subst', x: 8.855, y: 5.1, name: '代替品', str: '中', fact: 'カード・ホームエクイティ・プライベートクレジットの直接貸出' },
  ];
  forces.forEach(f => {
    L.box(s, f.x, f.y, BW, BH, { round: true, name: 'ovl_force_' + f.id });
    L.text(s, f.name, { x: f.x + 0.08, y: f.y + 0.07, w: 1.3, h: 0.28, fontSize: 10, bold: true, color: C.dark, margin: 0, valign: 'middle', objectName: 'force_n_' + f.id });
    L.text(s, f.str, { x: f.x + 1.38, y: f.y + 0.07, w: 0.44, h: 0.28, fontSize: 10, bold: true, color: STR[f.str], align: 'right', margin: 0, valign: 'middle', objectName: 'force_s_' + f.id });
    L.text(s, f.fact, { x: f.x + 0.08, y: f.y + 0.4, w: BW - 0.16, h: BH - 0.47, fontSize: 8.5, color: C.text, margin: 0, objectName: 'force_f_' + f.id });
  });

  // 中央: SoFi の利ざや(濃緑の箱)。各力は中央へ矢印で向かう
  const hx = 8.855, hy = 3.55, cx = hx + BW / 2, cy = hy + BH / 2;
  L.box(s, hx, hy, BW, BH, { round: true, fill: C.dark, line: C.dark, name: 'ovl_hub' });
  L.text(s, 'SoFi の利ざや\nNIM 5.98%', { x: hx + 0.08, y: hy + 0.1, w: BW - 0.16, h: BH - 0.2, fontSize: 13, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0, objectName: 'hub_t' });
  L.arrow(s, cx, 3.45, cx, hy, { color: C.sub, width: 1 });                              // 上: 新規参入
  L.arrow(s, cx, 5.1, cx, hy + BH, { color: C.sub, width: 1 });                          // 下: 代替品
  L.arrow(s, 6.78 + BW, cy, hx, cy, { color: C.sub, width: 1 });                         // 左: 資金の出し手
  L.arrow(s, 10.93, cy, hx + BW, cy, { color: C.sub, width: 1 });                        // 右: 借り手
  L.arrow(s, 6.78 + BW, 2.0 + BH, hx, hy, { color: C.sub, width: 1 });                   // 左上: 業界内の競争

  // 右下: takeaway(手本の位置)
  L.takeaway(s, 10.93, 5.1, BW, BH, '競争が強いのは貸出の市場。資金の側が弱い(SoFi に有利)ことが、利ざやを支える');
  return s;
};
