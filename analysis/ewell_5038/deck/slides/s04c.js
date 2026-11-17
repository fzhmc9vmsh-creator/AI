// 最新決算のサマリー: 業績表 + 進捗の横棒 + KPI 表 + トピックス + takeaway
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, { kicker: '', source: '2026年12月期 第3四半期 決算短信・決算説明資料(2026-11-13)、株予報' });

  L.paneHead(s, 0.5, 1.62, 7.6, '業績(百万円)', 'pane_pl');
  L.table(s, [
    ['', '2025年\n1〜9月', '2026年\n1〜9月', '前年比', '2026年\n3Q単独', '前年同期比'],
    ['売上', '2,473', '3,067', '+24.0%', '1,076', '+23.6%'],
    ['  うちクラウド', '2,137', '2,617', '+22.4%', '910', '+21.3%'],
    ['  うちBPaaS', '317', '440', '+38.6%', '162', '+41.2%'],
    ['売上総利益(率)', '1,954(79.0%)', '2,342(76.3%)', '+19.8%', '827(76.8%)', '+20.9%'],
    ['営業利益(率)', '1,195(48.3%)', '1,454(47.4%)', '+21.6%', '508(47.2%)', '+24.6%'],
  ], { x: 0.5, y: 1.94, w: 7.6, colW: [1.5, 1.3, 1.3, 0.9, 1.3, 1.3], fontSize: 9.5, rowH: 0.36, name: 'tbl_pl' }); // lint-ok: 台帳に無い手書き(決算短信の数字)

  L.paneHead(s, 0.5, 4.3, 7.6, '通期予想に対する進捗(幅は100%に比例。通期予想は据え置き)', 'pane_prog');
  const bars = [
    { label: '売上', cur: 71.7, prev: 72.9 },
    { label: '営業利益', cur: 75.5, prev: 77.8 },
  ];
  const bx = 1.6, bw = 4.8;
  bars.forEach((b, i) => {
    const y = 4.72 + i * 0.5;
    L.text(s, b.label, { x: 0.5, y, w: 1.0, h: 0.34, fontSize: 10, bold: true, color: C.text, margin: 0, valign: 'middle', objectName: `pg_l${i}` });
    L.box(s, bx, y, bw, 0.34, { fill: C.gray, line: C.rule, name: `ovl_pg_bg${i}` });
    L.box(s, bx, y, bw * b.cur / 100, 0.34, { fill: C.primary, line: C.primary, name: `ovl_pg_bar${i}` });
    L.box(s, bx + bw * b.prev / 100 - 0.01, y - 0.04, 0.03, 0.42, { fill: C.text, line: C.text, name: `ovl_pg_prev${i}` });
    L.text(s, `${b.cur}%(前年 ${b.prev}%)`, { x: bx + bw + 0.1, y, w: 1.4, h: 0.34, fontSize: 10, bold: true, color: C.dark, margin: 0, valign: 'middle', objectName: `pg_v${i}` });
  }); // lint-ok: 台帳に無い手書き(進捗率)
  L.text(s, '黒線 = 前年同期の進捗。通期予想: 売上4,277・営業利益1,927。売上のコンセンサスは4,188', { x: 0.5, y: 5.75, w: 7.6, h: 0.26, fontSize: 9, color: C.sub, margin: 0, objectName: 'note_prog' }); // lint-ok: 台帳に無い手書き(通期予想・コンセンサス)

  L.paneHead(s, 8.35, 1.62, 4.48, '主要KPI(3Q)', 'pane_kpi');
  L.table(s, [
    ['項目', '3Q', '比較'],
    ['契約', '3,843', '前年同期比 +13.5%'],
    ['新規', '153', '前年同期 150'],
    ['解約', '35', '前年同期 51'],
    ['休止の純増', '11', '過去最大'],
    ['顧客単価', '94.1千円', '+6.8%(前四半期 90.7)'],
    ['MRRチャーン', '月0.10%', '前四半期 0.20%'],
  ], { x: 8.35, y: 1.94, w: 4.48, colW: [1.3, 1.0, 2.18], fontSize: 9, rowH: 0.3, name: 'tbl_kpi' }); // lint-ok: 台帳に無い手書き(3Q KPI)

  L.paneHead(s, 8.35, 4.18, 4.48, 'トピックス', 'pane_topic');
  L.lookBox(s, [
    { n: 1, text: '2027年1月に基本料+10%(創業来初)。サーバー費は3年で約3.7倍' },
    { n: 2, text: 'ボードProを10月提供、2027年1月から月3万円' },
    { n: 3, text: '採用支援「カエドキ」を無料で開始。期末の社員は約140名' },
  ], { x: 8.35, y: 4.5, w: 4.48, h: 1.52, title: '3 点(カエドキと社員数は 1 行)' });

  L.takeaway(s, 0.5, 6.1, 12.33, 0.62, '変わったこと: 単価の加速・解約の減少・値上げの決定。変わらなかったこと: 新規獲得(1〜3Q 499件、前年511件)と粗利率の低さ。株価は翌営業日に+4.0%(2,208円から2,297円へ)', { fontSize: 10.5 }); // lint-ok: 台帳に無い手書き(株価反応)
};
