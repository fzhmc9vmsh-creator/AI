// 2-2 会社のシナリオ(2/2): 部品の採点(指示書 spec/r6_new.md の s08e 節どおり)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 筋書きの部品(P1〜P11)を、数字で作動しているかで採点。右: 規模で重みづけした判定と、会社目標・コンセンサス・需給エンジンの差',
    source: 'report/ORCL_report.md §4-3・§5-1(10-Q・決算資料)、Investor Day 2026-10-28(8-K Ex.99.1、CFO 資料 p.4・26)、需給エンジン第4.4版、LSEG コンセンサス(説明会の前)',
  });

  // 評価の色(+ は濃緑の太字、± と + 遅延 は琥珀の太字、保留 は灰)
  const ev = (t) => {
    if (t === '+') return { text: t, options: { color: C.primary, bold: true } };
    if (t === '±' || t === '+ 遅延') return { text: t, options: { color: C.amber, bold: true } };
    return { text: t, options: { color: C.sub } };
  };

  // 左: 部品の採点表
  L.table(s, [
    ['#', '部品', '評価', '進捗(数字で作動しているか)', '重み'],
    ['P1', 'OpenAI\n(約 3,000 億ドル・4.5GW)', ev('±'), '部分作動。Abilene の一部が稼働、他は遅延', '25%'],
    ['P2', 'OpenAI 以外の AI 顧客', ev('+'), '作動。OpenAI 以外の受注残は 2 倍超', '15%'],
    ['P3', '前払い・GPU 持込', ev('+'), '作動。前受収益 154 → 308 億ドル', '15%'],
    ['P4', '開発事業者とのリース', ev('±'), '作動(未開始 2,880 億ドル)。価値は更新単価しだい', '10%'],
    ['P5', '電力の確保', ev('+ 遅延'), '遅延。納入 850MW は計画の約 1GW 未満、ガス管も延期', '10%'],
    ['P6', '資金調達', ev('+'), '追加調達 200 億ドルの上限と\nFY29 FCF 300 億ドル以上を約束', '10%'],
    ['P7', 'Database@', ev('+'), '作動(+353%)', '4%'],
    ['P8', 'AI Database', ev('保留'), '数字なし', '1%'],
    ['P9', 'アプリ(SaaS)', ev('+'), '作動(+10%、横ばい)', '5%'],
    ['P10', 'GPU の更新・再販', ev('+'), '作動(全量を従来比 +20% で更新・再販)', '3%'],
    ['P11', '営業費の効率化', ev('+'), '作動(非GAAP 営業利益率 42.5%)', '2%'],
  ], {
    x: 0.5, y: 1.62, w: 8.3, colW: [0.5, 2.0, 0.8, 4.1, 0.9], fontSize: 8.5, rowH: 0.38,
    align: ['center', 'left', 'center', 'left', 'center'],
  });

  // 右上: 規模で重みづけした判定(100% 積み上げの横棒 1 本)
  L.paneHead(s, 9.05, 1.62, 3.78, '規模で重みづけした判定');
  s.addChart(pres.charts.BAR, [
    { name: '作動している +', labels: ['重み'], values: [54] },
    { name: '両面・遅延・コスト', labels: ['重み'], values: [45] },
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
    ['売上(億ドル)', '2,250', '2,242', '2,173'],
    ['営業利益(億ドル)', '900', '—', '820'],
    ['EPS(ドル)', '21', '20.53', '19.85'],
    ['FY29 FCF(億ドル)', '300', '—', '721'],
  ], { x: 9.05, y: 4.65, w: 3.78, colW: [1.38, 0.72, 0.93, 0.75], fontSize: 8.5, rowH: 0.3 });
  L.text(s, '資金の目標はエンジンでも余裕を持って届く。利益の目標は\nエンジンより 5〜9% 高い(粗利率 35% の AI が 6 割に)。\n理論株価は会社の EPS を土台にした', {
    x: 9.05, y: 6.22, w: 3.78, h: 0.6, fontSize: 8.5,
  });
};
