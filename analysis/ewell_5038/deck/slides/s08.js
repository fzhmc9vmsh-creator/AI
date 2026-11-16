// s08 粗利率とサーバー費: 左 = 四半期の全社粗利率、右 = サーバー費の年額
module.exports = function build(pres, L) {
  const F = L.F, C = L.C;
  const s = L.contentSlide(pres, {
    kicker: '全社の粗利率は直近4期で前年同期を下回る。主因はサーバー費の増加と、粗利率の低いBPaaSの構成上昇',
    source: '会社決算説明資料(2026年12月期3Q p.4・p.18・p.22)',
  });

  // 左: 四半期の全社粗利率(%)。直近4期(FY25 Q4〜FY26 Q3)を赤、それ以前は灰色
  const qs = [
    ['FY24\nQ1', 76.4], ['Q2', 76.5], ['Q3', 78.2], ['Q4', 79.1],
    ['FY25\nQ1', 80.1], ['Q2', 78.5], ['Q3', 78.5], ['Q4\n前年比\n−2.9pt', 76.2],
    ['FY26\nQ1\n−5.1pt', 75.0], ['Q2\n−1.4pt', 77.1], ['Q3\n−1.7pt', 76.8],
  ];
  L.paneHead(s, 0.5, 1.62, 6.9, '全社の粗利率(四半期、%。折れ線、縦軸は 70% から)', 'pane_gm_head');
  s.addChart('line', [{ name: '粗利率', labels: qs.map(q => q[0]), values: qs.map(q => q[1]) }], L.chartStyle({
    x: 0.5, y: 1.98, w: 6.9, h: 3.55, objectName: 'chart_gm',
    lineDataSymbol: 'circle', lineDataSymbolSize: 6, lineSize: 2, valAxisMinVal: 70, valAxisMaxVal: 82, valAxisMajorUnit: 2, valAxisLabelFormatCode: '0',
    dataLabelFormatCode: '0.0', chartColors: [C.dark],
  }));

  // 右: サーバー費の年額(百万円)。2026 は 1〜9 月を年換算した推定
  const sv = [['2023\n売上比 3.9%', 81], ['2024\n売上比 5.2%', 134], ['2025\n売上比 5.2%', 175], ['2026(推定)\n売上比 約7.2%', 303]];
  L.paneHead(s, 7.7, 1.62, 5.13, 'サーバー費の年額(百万円)', 'pane_sv_head');
  s.addChart('bar', [{ name: 'サーバー費', labels: sv.map(q => q[0]), values: sv.map(q => q[1]) }], L.chartStyle({
    x: 7.7, y: 1.98, w: 5.13, h: 3.4, objectName: 'chart_sv',
    barDir: 'col', barGapWidthPct: 60, valAxisMinVal: 0, valAxisMaxVal: 350, valAxisMajorUnit: 50,
    chartColors: sv.map((q, i) => (i === 3 ? C.red : C.sub)),
  }));
  L.text(s, `2026 年は 1〜9 月の ${F('9m26.server')}(前年同期 ${F('9m25.server')})を年換算した推定`, { x: 7.7, y: 5.44, w: 5.13, h: 0.2, fontSize: 8, color: C.sub, margin: 0, objectName: 'note_sv' });

  L.takeaway(s, 0.5, 5.75, 12.33, 1.0,
    `2027 年 1 月の基本料 +10% で年約 80 百万円を戻す = 2026 年の増分約 128 百万円の約 6 割。クラウド単体の粗利率は 1Q ${F.n('q26q1.cloud_gm', { noPeriod: true })}% → 3Q ${F('q26q3.cloud_gm')} と戻りつつあるが、BPaaS(粗利率 ${F('fy25.bpaas_gm')})の構成上昇で全社は 76〜77% が基準`, // lint-ok: 台帳に無い(基本料+10%の戻し額・増分)
    { fontSize: 11 });
};
