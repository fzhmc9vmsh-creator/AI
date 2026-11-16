// s10 価格決定力: 訪問件数と月額の料金線(左)、他社切替による解約率(右)
module.exports = function build(pres, L) {
  const F = L.F, C = L.C;
  const s = L.contentSlide(pres, {
    kicker: '月額は iBow = 基本料 + 訪問従量、カイポケ訪問看護 = 定額。訪問が増えるほど差は開くが、流出率は下がっている',
    source: 'ASPIC掲載のカイポケ訪問看護の価格(2026年2月)、会社KPI、当方の計算',
  });

  // 左: 月額の料金線(円/月)。訪問件数 0〜1,000 件/月
  const v = []; for (let i = 0; i <= 1000; i += 50) v.push(i);
  L.paneHead(s, 0.5, 1.62, 7.2, '訪問件数ごとの月額(円/月)', 'pane_price_head');
  s.addChart('line', [
    { name: 'iBow(基本料 18,000 円 + 100 円 × 訪問)', labels: v.map(String), values: v.map(x => 18000 + 100 * x) },
    { name: 'iBow(2027 年 1 月から 19,800 円 + 100 円 × 訪問)', labels: v.map(String), values: v.map(x => 19800 + 100 * x) },
    { name: 'カイポケ訪問看護(定額 25,000 円)', labels: v.map(String), values: v.map(() => 25000) },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 7.2, h: 3.95, objectName: 'chart_price',
    valAxisMinVal: 0, valAxisMaxVal: 120000, valAxisMajorUnit: 20000, valAxisLabelFormatCode: '#,##0',
    showValue: false, showLegend: true, legendPos: 't', legendFontSize: 8.5,
    chartColors: [C.primary, C.light, C.sub], lineSize: 2.5, lineDataSymbol: 'none', catAxisLabelFrequency: 2,
    showCatAxisTitle: true, catAxisTitle: '1 か月の訪問件数(件)', catAxisTitleFontSize: 8.5, catAxisTitleColor: C.sub, catAxisTitleFontFace: L.FONT,
  }));
  L.marks(s, [
    { x: 4.4, y: 3.35, n: 1, text: '500 訪問: iBow 68,000 円 / カイポケ 25,000 円', side: 'left' },
    { x: 1.85, y: 4.2, n: 3, text: '交点は約 71 訪問', side: 'right' },
  ]);

  // 右: 他社切替による解約率(年)
  L.paneHead(s, 8.0, 1.62, 4.83, '他社切替による解約率(年)', 'pane_sw_head');
  const sw = [['FY2024', F.v('calc.switch_rate_fy24')], ['FY2025', F.v('calc.switch_rate_fy25')], ['FY2026(年率)', F.v('calc.switch_rate_fy26')]];
  s.addChart('bar', [{ name: '他社切替による解約率', labels: sw.map(a => a[0]), values: sw.map(a => a[1]) }], L.chartStyle({
    x: 8.0, y: 1.98, w: 4.83, h: 1.6, objectName: 'chart_sw',
    barDir: 'col', barGapWidthPct: 60, valAxisMinVal: 0, valAxisMaxVal: 5, valAxisMajorUnit: 1, dataLabelFormatCode: '0.0"%"', valAxisLabelFormatCode: '0',
    chartColors: sw.map((a, i) => (i === 2 ? C.primary : C.sub)),
  }));
  L.kpiTiles(s, [
    { value: F('calc.churn_total_fy26'), label: '件数ベースの解約(年)' },
    { value: '約1〜2%', label: `売上ベースの解約(年)\nMRRチャーン 月 ${F.n('q26q3.mrr_churn')}〜0.20%` }, // lint-ok: 台帳に無い(MRRチャーンの年換算)
  ], { compact: true, x: 8.0, y: 3.68, w: 4.83, h: 1.05 });

  L.lookBox(s, [
    { n: 1, text: `カイポケより ${F('calc.price_ratio_500')} 高い(500 訪問)` },
    { n: 2, text: `流出率は ${F.n('calc.switch_rate_fy25')}% → ${F('calc.switch_rate_fy26')} に低下` },
    { n: 3, text: `利用料は訪問売上の ${F('calc.cost_share_rev')}(1 訪問 8,500 円のうち 136 円)` },
  ], { x: 8.0, y: 4.83, w: 4.83, h: 1.3 });

  L.takeaway(s, 0.5, 6.2, 12.33, 0.58,
    '価格は離脱の理由になっていない。1 訪問 100 円は 2014 年から据え置き。2027 年 1 月の基本料 +10% 後の解約(2027-05-14 頃の 1Q)が最初の試験', // lint-ok: 台帳に無い(据え置きの年・日付)
    { fontSize: 10.5 });
};
