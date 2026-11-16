// s12 5年後の損益: 売上・営業利益(基準の棒 + 会社計画の点)と、2030年の弱気・基準・強気
module.exports = function build(pres, L) {
  const F = L.F, C = L.C;
  const s = L.contentSlide(pres, {
    kicker: '棒は当方の基準(2025 年は実績)、点は会社の中期経営計画。会社計画との差は主に顧客単価',
    source: '当方の事業エンジン(engine.py)、会社の中期経営計画、会社決算説明資料',
  });

  const yrs = ['2025', '2026', '2027', '2028', '2029', '2030'];
  const combo = (bars, plan, max, unit, name, x, y, w, h) => {
    s.addChart([
      { type: pres.charts.BAR, data: [{ name: '当方の基準', labels: yrs, values: bars }],
        options: { chartColors: bars.map((b, i) => (i === 0 ? C.sub : C.primary)), barGapWidthPct: 50 } },
      { type: pres.charts.LINE, data: [{ name: '会社計画', labels: yrs, values: plan }],
        options: { chartColors: [C.text], lineSize: 0, lineDataSymbol: 'diamond', lineDataSymbolSize: 9 } },
    ], L.chartStyle({
      x, y, w, h, objectName: name, barDir: 'col', valAxisMinVal: 0, valAxisMaxVal: max, valAxisMajorUnit: max / 4, valAxisLabelFormatCode: '#,##0',
      dataLabelFormatCode: '#,##0', showLegend: true, legendPos: 't', dataLabelPosition: 'inEnd', dataLabelColor: C.white,
    }));
  };
  L.paneHead(s, 0.5, 1.62, 7.6, '売上(百万円)', 'pane_rev_head');
  combo([F.v('fy25.revenue'), 4210, 4951, 5705, 6454, 7191], [null, F.v('g26.revenue'), 5199, F.v('plan28.revenue'), null, null], 8000, '百万円', 'chart_rev', 0.5, 1.92, 7.6, 2.4);
  L.paneHead(s, 0.5, 4.38, 7.6, '営業利益(百万円)', 'pane_op_head');
  combo([F.v('fy25.op'), 1928, 2278, 2653, 3034, 3380].map((v, i) => (i === 1 ? 1928 : v)), [null, F.v('g26.op'), 2350, F.v('plan28.op'), null, null], 4000, '百万円', 'chart_op', 0.5, 4.68, 7.6, 2.1);

  // 右: 2030年の弱気・基準・強気
  L.paneHead(s, 8.4, 1.62, 4.43, '2030 年の見立て', 'pane_tbl_head');
  const base = (t) => ({ text: t, options: { bold: true, color: C.primary } });
  L.table(s, [
    ['', '弱気', '基準', '強気'],
    ['契約ST(件)', '5,104', base('5,615'), '6,136'],
    ['顧客単価(千円)', '103.0', base(F.n('plan28.arpu')), '117.0'],
    ['営業利益率', '43.5%', base('47.0%'), '48.5%'],
    ['EPS(円)', '125.6', base('156.5'), '183.9'],
  ], { x: 8.4, y: 1.98, w: 4.43, colW: [1.55, 0.9, 1.0, 0.98], fontSize: 10, rowH: 0.34, name: 'tbl_2030' });

  L.lookBox(s, [
    { n: 1, text: `会社計画との差は主に単価(2028 年 ${F.n('plan28.arpu')} vs 102.5 千円)` },
    { n: 2, text: '営業利益率は 45% 台 → 47%(規模の効果)' },
    { n: 3, text: '検証の誤差は売上 −5.5%(制度変更の加速を見落とす癖)' },
  ], { x: 8.4, y: 3.85, w: 4.43, h: 2.1 });
  L.text(s, '顧客単価・契約ST は 2030 年の稼働1STあたり月額・年末の契約件数', { x: 8.4, y: 6.05, w: 4.43, h: 0.4, fontSize: 8.5, color: C.sub, margin: 0, objectName: 'note_def' });
  L.marks(s, [
    { x: 5.0, y: 2.25, n: 1 }, { x: 7.2, y: 4.95, n: 2 },
  ]);
};
