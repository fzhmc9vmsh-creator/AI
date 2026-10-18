// 2-2 会社のシナリオ(2/2): 部品の採点(手本を写経。タイトル・ページ番号は meta.js が入れる)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 筋書きの部品(P1〜P10)を、数字で作動しているかで採点。右: 規模で重みづけした判定と、会社目標・コンセンサス・事業エンジンの差',
    source: '会社開示(Q4 2025〜Q2 2026)、research/R1b_kpi.md・R3b_management.md、research_r2/R6・R7、calc/out/val.json',
  });

  // 評価の色: + は濃緑太字、± は琥珀太字、− は赤太字、保留は灰
  const ev = (t) => {
    if (t === '+') return { text: t, options: { color: C.primary, bold: true } };
    if (t === '±') return { text: t, options: { color: C.amber, bold: true } };
    if (t === '−') return { text: t, options: { color: C.red, bold: true } };
    return { text: t, options: { color: C.sub } };
  };

  // 左: 部品の採点表
  L.table(s, [
    ['#', '部品', '評価', '進捗(数字で作動しているか)', '重み'],
    ['P1', '会員の獲得(ブランド・販促)', ev('+'), '作動。純増 110 万人/四半期、ブランド想起 10.4%', '20%'],
    ['P2', 'クロスバイ', ev('±'), '作動(51%)。ただし FS 製品当たり収益は 104 → 88 ドル', '10%'],
    ['P3', '預金による調達', ev('+'), '作動。倉庫比 −1.56pt、年 7.1 億ドルの節約。差は縮小', '20%'],
    ['P4', 'B/S 貸出の拡大', ev('+'), '作動。純金利収益 +52%。自己資本比率は −4.1pt/半年', '20%'],
    ['P5', 'LPB(手数料型)', ev('±'), '停滞。組成 37 → 31 億ドル(Q4 2025 → Q2 2026)', '10%'],
    ['P6', '学生ローン(Grad PLUS)', ev('+'), '作動。組成 +170%', '5%'],
    ['P7', '増資と資本政策', ev('+'), '作動。33 億ドルの増資で TBVPS +56%', '5%'],
    ['P8', 'Tech Platform(Galileo)', ev('±'), '底打ち。前期比 +12.5%、自社コアへ移行。貢献利益率は 30 → 14%', '5%'],
    ['P9', '新領域(SoFiUSD ほか)', ev('保留'), '数字が小さい(SoFiUSD 約 3 億ドル)', '3%'],
    ['P10', '販促費の効率', ev('±'), '販促費率 30.3% → 32.2%。下期の改善待ち', '2%'],
  ], {
    x: 0.5, y: 1.62, w: 8.3, colW: [0.5, 2.0, 0.8, 4.1, 0.9], fontSize: 8.5, rowH: 0.38,
    align: ['center', 'left', 'center', 'left', 'center'],
  });

  // 右上: 規模で重みづけした判定(100% 積み上げの横棒 1 本、4 系列)
  L.paneHead(s, 9.05, 1.62, 3.78, '規模で重みづけした判定');
  s.addChart(pres.charts.BAR, [
    { name: '作動している +', labels: ['重み'], values: [70] },
    { name: '両面・停滞', labels: ['重み'], values: [27] },
    { name: '逆行 −', labels: ['重み'], values: [0] },
    { name: '保留', labels: ['重み'], values: [3] },
  ], L.chartStyle({
    x: 9.05, y: 1.95, w: 3.78, h: 1.15, barDir: 'bar', barGrouping: 'percentStacked',
    chartColors: [C.primary, C.amber, C.red, C.sub], showLegend: true, legendPos: 'b',
    // 4% 未満の細い区間(保留 3%)はラベルを出さず、表の P9 で読む(5% と 3% のラベルが重なるため)
    dataLabelPosition: 'ctr', dataLabelColor: 'FFFFFF', dataLabelFormatCode: '[>=4]0"%";""',
    catAxisHidden: true, valAxisHidden: true, valGridLine: { style: 'none' }, objectName: 'chart_weight',
  }));
  L.takeaway(s, 9.05, 3.2, 3.78, 0.95, '判定は「条件付きのプラス」。作動している部品の多くが資本を使い、資本の上限が筋書きの速さを決める');

  // 右下: 会社の目標をどこまで信じるか(2028 年)
  L.paneHead(s, 9.05, 4.3, 3.78, '会社の目標をどこまで信じるか(2028 年)');
  L.table(s, [
    ['', '会社', 'コンセンサス', 'エンジン'],
    ['EPS(ドル)', '1.03〜1.12', '1.08', '1.10'],
    ['ROTCE', '20〜30%\n(長期)', '—', '12.5%'],
  ], { x: 9.05, y: 4.65, w: 3.78, colW: [1.06, 0.9, 0.91, 0.91], fontSize: 8.5, rowH: 0.34 });
  L.text(s, 'EPS の目標はエンジンでも届く。ROTCE の目標には\n届かず、成長が生む価値は小さい。理論株価は\nエンジンの EPS を土台にした', {
    x: 9.05, y: 5.75, w: 3.78, h: 0.95, fontSize: 8.5,
  });
};
