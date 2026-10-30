// 2-2 会社のシナリオ(2/2): 部品の採点(第4.5版)。左: 部品の採点表(13 部品・重みは規模で加重、合計 100%)。右: 判定の積み上げ棒と会社・コンセンサス・エンジンの差
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 筋書きの部品(P1〜P13)を、数字で作動しているかで採点。右: 規模で重みづけした判定と、会社目標・コンセンサス・需給エンジンの差',
    source: 'report/ORCL_report.md §4-3・§5-1、Investor Day 2026-10-28(8-K Ex.99.1、CFO 資料 p.4・26)、需給エンジン第4.5版(m10_*.json)、LSEG コンセンサス(説明会前)',
  });

  // 評価の色(+ は濃緑の太字、± と + 遅延 は琥珀の太字、保留 は灰)
  const ev = (t) => {
    if (t === '+') return { text: t, options: { color: C.primary, bold: true } };
    if (t === '±' || t === '+ 遅延') return { text: t, options: { color: C.amber, bold: true } };
    return { text: t, options: { color: C.sub } };
  };

  // 左: 部品の採点表(重みは 4.4 版の重みを比例で縮め、新しい 2 部品を足して 100%)
  L.table(s, [
    ['#', '部品', '評価', '進捗(数字で作動しているか)', '重み'],
    ['P1', 'OpenAI\n(約 3,000 億ドル・4.5GW)', ev('±'), '部分作動。Abilene の一部が稼働、他は遅延', '21%'],
    ['P2', 'OpenAI 以外の AI 顧客', ev('+'), '作動。OpenAI 以外の受注残は 2 倍超', '13%'],
    ['P3', '前払い・GPU 持込', ev('+'), '作動。前受収益 154 → 308 億ドル', '13%'],
    ['P4', '開発事業者とのリース', ev('±'), '作動(未開始 2,880 億ドル)。価値は更新単価しだい', '9%'],
    ['P5', '電力の確保', ev('+ 遅延'), 'NM・WI で 1 年前後の遅れ。賃料は引き渡しから、\n価値への効きは小さい(時期のずれ)', '9%'],
    ['P6', '資金調達', ev('+'), '追加調達 200 億ドルの上限と\nFY29 FCF 300 億ドル以上を約束', '9%'],
    ['P7', 'Database@', ev('+'), '作動(+353%)', '3%'],
    ['P8', 'AI Database', ev('保留'), '数字なし', '1%'],
    ['P9', 'アプリ(SaaS)', ev('+'), '作動(+10%、横ばい)', '4%'],
    ['P10', 'GPU の更新・再販', ev('+'), '作動(全量を従来比 +20% で更新・再販)', '3%'],
    ['P11', '営業費の効率化', ev('+'), '作動(非GAAP 営業利益率 42.5%)', '2%'],
    ['P12', '推論の需要(企業データの近く)', ev('+'), '推論は AI 計算の約 2/3(2026)。\n分散 50〜200MW の拠点を供給', '9%'],
    ['P13', 'アプリの AI 収益化・ERP 移行', ev('+'), 'ERP の約半分がオンプレ、移行で 3〜4 倍。\nAI 呼び出し +42%(6→8 月)', '4%'],
  ], {
    x: 0.5, y: 1.62, w: 8.3, colW: [0.5, 2.0, 0.8, 4.1, 0.9], fontSize: 8.5, rowH: 0.33,
    align: ['center', 'left', 'center', 'left', 'center'],
  });

  // 右上: 規模で重みづけした判定(100% 積み上げの横棒 1 本。重みの合計から計算: 作動 60・両面・遅延 39・保留 1)
  L.paneHead(s, 9.05, 1.62, 3.78, '規模で重みづけした判定');
  s.addChart(pres.charts.BAR, [
    { name: '作動している +', labels: ['重み'], values: [60] },
    { name: '両面・遅延・コスト', labels: ['重み'], values: [39] },
    { name: '保留', labels: ['重み'], values: [1] },
  ], L.chartStyle({
    x: 9.05, y: 1.95, w: 3.78, h: 1.15, barDir: 'bar', barGrouping: 'percentStacked',
    chartColors: [C.primary, C.amber, C.sub], showLegend: true, legendPos: 'b',
    dataLabelPosition: 'ctr', dataLabelColor: 'FFFFFF', dataLabelFormatCode: '[>=2]0"%";""', // 2% 未満の細い区間(保留 1%)は表の P8 で読む
    catAxisHidden: true, valAxisHidden: true, valGridLine: { style: 'none' }, objectName: 'chart_weight',
  }));
  L.takeaway(s, 9.05, 3.2, 3.78, 0.95, '判定は「条件付きのプラス」。両面・遅延の部品は失敗ではなく、遅れと条件');

  // 右下: 会社の目標をどこまで信じるか(FY30 と FY29 FCF)
  L.paneHead(s, 9.05, 4.3, 3.78, '会社の目標をどこまで信じるか');
  L.table(s, [
    ['', '会社', 'コンセンサス', 'エンジン'],
    ['売上(億ドル)', '2,250', '2,242', '2,239'],
    ['営業利益(億ドル)', '900', '—', '834'],
    ['EPS(ドル)', '21', '20.53', '19.59'],
    ['FY29 FCF(億ドル)', '300', '—', '399'],
  ], { x: 9.05, y: 4.65, w: 3.78, colW: [1.38, 0.72, 0.93, 0.75], fontSize: 8.5, rowH: 0.3 });
  L.text(s, '売上と資金の目標はエンジンでも届く。利益率は 3pt 低い\n(会社「FY28・29 も 40% を大きく下回らない」に対し 37%)', {
    x: 9.05, y: 6.22, w: 3.78, h: 0.6, fontSize: 8.5,
  });
};
