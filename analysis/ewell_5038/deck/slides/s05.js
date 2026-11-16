// 製品と課金: 製品表 + 1 訪問の内訳の比例帯 + 見るところ
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, { kicker: '', source: '会社決算説明資料(2026年12月期3Q)、有価証券報告書、当方の計算' });

  L.paneHead(s, 0.5, 1.62, 8.2, '製品別の売上と課金(★ = アップセル)', 'pane_tbl');
  const star = { options: { color: C.primary, bold: true } };
  L.table(s, [
    ['製品', 'FY2025売上\n(百万円)', '構成比', '課金', '稼働数\n(2026年3Q)', '戦略'],
    ['iBow', '2,392', '70.5%', '基本料18,000円/月+100円/訪問', '3,695', '中核'],
    ['iBowレセプト', '278', '8.2%', '月6,000〜99,000円(訪問件数に応じて)', '3,212', '付帯'],
    ['AI計画報告・AIルート', '105', '3.1%', '20円・30円/訪問', '1,755・281', { text: '★', options: star.options }],
    ['法定研修・その他クラウド', '156', '4.6%', '年180,000円(一括計上)', '—', '非リカーリング'],
    ['BPaaS(事務代行)', '441', '13.0%', '月10万円か診療報酬の5%の高い方', '325', { text: '★', options: star.options }],
    ['その他', '21', '0.6%', '介護伝送980円/月ほか', '—', '維持'],
  ], { x: 0.5, y: 1.98, w: 8.2, colW: [1.75, 0.9, 0.7, 2.9, 0.9, 1.05], fontSize: 9, rowH: 0.4, name: 'tbl_prod' });
  L.marks(s, [{ x: 8.76, y: 2.47, n: 1 }, { x: 8.76, y: 3.27, n: 2 }]);

  L.lookBox(s, [
    { n: 1, text: '売上の約8割は訪問件数の従量(基本料のほかは訪問ごとの課金)' },
    { n: 2, text: 'アップセル(★)は単価の伸びの約9割' },
    { n: 3, text: `利用料は事業所売上の ${F('calc.cost_share_rev')}(1訪問8,500円のうち約136円)` },
  ], { x: 9.05, y: 1.62, w: 3.78, h: 3.1 });

  // 比例帯: 8,364 : 136 を幅で描く
  const bx = 0.5, bw = 12.33, by = 5.45, bh = 0.5, tot = 8500, iw = bw * 136 / tot;
  L.paneHead(s, 0.5, 5.0, 8.2, '1訪問8,500円の内訳(幅は金額に比例)', 'pane_band');
  L.box(s, bx, by, bw - iw, bh, { fill: C.rule, line: C.rule, name: 'ovl_band_office' });
  L.text(s, '事業所の取り分 8,364円', { x: bx, y: by, w: bw - iw, h: bh, fontSize: 11, bold: true, color: C.text, align: 'center', valign: 'middle', margin: 0, objectName: 'ovl_band_office_t' });
  L.box(s, bx + bw - iw, by, iw, bh, { fill: C.primary, line: C.primary, name: 'ovl_band_ibow' });
  L.text(s, `iBow 約136円(${F('calc.cost_share_rev')})`, { x: bx + bw - 3.0, y: by + bh + 0.04, w: 3.0, h: 0.26, fontSize: 10, bold: true, color: C.primary, align: 'right', margin: 0, objectName: 'band_ibow_t' });
  L.marks(s, [{ x: bx + bw - iw - 0.04, y: by - 0.3, n: 3 }]);
  L.text(s, '500訪問のSTで月68,000円。2027年1月から基本料19,800円(+2.6%)', { x: 0.5, y: 6.3, w: 8.0, h: 0.3, fontSize: 10, color: C.text, margin: 0, objectName: 'note_price' });
};
