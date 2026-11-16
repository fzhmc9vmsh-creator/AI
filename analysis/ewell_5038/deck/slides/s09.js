// s09 獲得の分母: 業界の新規開設・廃止(左)と、当社の獲得と契約数の式(右)
module.exports = function build(pres, L) {
  const F = L.F, C = L.C;
  const s = L.contentSlide(pres, {
    kicker: '当社の獲得は、業界の新規開設の約 27% を占める(他社からの切替を含む上限)。分母が横ばいなら獲得も頭打ちになる',
    source: '全国訪問看護事業協会「訪問看護ステーション数調査」各年(4月1日)、会社決算説明資料、当方の計算',
  });

  // 左: 業界の新規開設と廃止(件、4月1日調査)
  const yrs = ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026'];
  const nw = [1221, 1383, 1376, 1633, 1806, 1968, 2437, 2487, 2428];
  const cl = [482, 534, 526, 541, 490, 568, 701, 886, 960];
  L.paneHead(s, 0.5, 1.62, 7.0, '業界の新規開設と廃止(訪問看護ステーション、件/年、4月1日調査)', 'pane_ind_head');
  s.addChart('bar', [{ name: '新規開設', labels: yrs, values: nw }, { name: '廃止', labels: yrs, values: cl }], L.chartStyle({
    x: 0.5, y: 1.98, w: 7.0, h: 3.4, objectName: 'chart_ind',
    barDir: 'col', barGrouping: 'clustered', barGapWidthPct: 40, valAxisMinVal: 0, valAxisMaxVal: 3000, valAxisMajorUnit: 500,
    chartColors: [C.sub, C.red], showLegend: true, legendPos: 't', dataLabelFontSize: 8, dataLabelFormatCode: '#,##0', valAxisLabelFormatCode: '#,##0',
  }));
  // 2024〜2026 の「横ばい」の帯
  s.addShape('rect', { x: 5.22, y: 2.42, w: 2.23, h: 2.52, fill: { color: C.white, transparency: 100 }, line: { color: C.primary, width: 1, dashType: 'dash' }, objectName: 'band_flat' });
  L.text(s, '3年横ばい(年約 2,450 件)', { x: 5.22, y: 2.2, w: 2.23, h: 0.2, fontSize: 8.5, bold: true, color: C.primary, align: 'center', margin: 0, objectName: 'band_flat_t' });

  // 右上: 当社の新規獲得(件)
  L.paneHead(s, 7.85, 1.62, 4.98, '当社の新規獲得(件)', 'pane_acq_head');
  const aq = [['2023', 511], ['2024', 633], ['2025', 670], ['2025\n1〜3Q', 511], ['2026\n1〜3Q', 499]];
  s.addChart('bar', [{ name: '新規獲得', labels: aq.map(a => a[0]), values: aq.map(a => a[1]) }], L.chartStyle({
    x: 7.85, y: 1.98, w: 4.98, h: 2.2, objectName: 'chart_acq',
    barDir: 'col', barGapWidthPct: 45, valAxisMinVal: 0, valAxisMaxVal: 800, valAxisMajorUnit: 200,
    chartColors: aq.map((a, i) => (i === 4 ? C.primary : C.sub)), catAxisLabelFontSize: 8, dataLabelFontSize: 8.5,
  }));
  L.text(s, [{ text: '獲得 ÷ 業界の新規開設 = ', options: { color: C.text } }, { text: F('calc.capture_openings'), options: { bold: true, color: C.primary } }, { text: '(2025 年の 670 件 ÷ 2026 年 4 月の ' + F.n('ind.new_2026') + ' 件)', options: { color: C.sub } }],
    { x: 7.85, y: 4.2, w: 4.98, h: 0.24, fontSize: 9, margin: 0, valign: 'middle', objectName: 'cap_capture' });

  // 右下: 契約数の式
  L.paneHead(s, 7.85, 4.58, 4.98, '契約数の流量の式', 'pane_eq_head');
  L.text(s, '契約数 = 前年末 + 獲得約 660 件 − 解約 5.3% × 前年末', { x: 7.85, y: 4.9, w: 4.98, h: 0.24, fontSize: 9.5, bold: true, color: C.dark, margin: 0, valign: 'middle', objectName: 'eq_text' });
  L.table(s, [
    ['', '2026 年末', '2027 年末', '2028 年末'],
    ['契約数(件)', '3,950', '4,401', '4,828'],
    ['中期経営計画(件)', '—', '4,418', '4,882'],
    ['伸び率(2026 → 2029 年)', '12.8% → 11.4%', '→ 9.7%', '→ 8.4%'],
  ], { x: 7.85, y: 5.2, w: 4.98, colW: [1.74, 1.24, 1.0, 1.0], fontSize: 8.5, rowH: 0.31, name: 'tbl_eq' });

  L.lookBox(s, [
    { n: 1, text: '新規開設は 3 年横ばい(2,437 → 2,487 → ' + F.n('ind.new_2026') + ' 件)' },
    { n: 2, text: '廃止は 701 → ' + F.n('ind.closed_2026') + ' 件に増え、業界の純増(新規−廃止)は縮んでいる' },
    { n: 3, text: '流量の式は中期経営計画の契約数を ±1% で再現する(2027 年 −0.4%、2028 年 −1.1%)' },
  ], { x: 0.5, y: 5.5, w: 7.0, h: 1.25 });
  L.marks(s, [
    { x: 6.05, y: 2.0, n: 1 },
    { x: 6.9, y: 3.8, n: 2 },
    { x: 12.45, y: 4.61, n: 3 },
  ]);
};
