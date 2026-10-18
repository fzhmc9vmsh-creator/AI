// 2-3 増収の源泉と利益率の経路(手本 ORCL s15 の横棒の作りと、ORCL s10 の右パネルの表の作り。タイトル・ページ番号は meta.js が入れる)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 増収の内訳(Q2 2025 → Q2 2026、百万ドル)。右: 利益率の経路(事業エンジン)と、2026 年下期の計画が求める利益率',
    source: '会社開示(Q2 2026 10-Q)、research_r2/R6_pnl_margin.md §1・§4、calc/out/val.json',
  });

  // 左: 増収の内訳。増加と減少を 2 系列に分け、100% 重ねた横棒(各項目は片方の系列だけが値を持つ = 積み上げと同じ見た目)。
  // 積み上げにしないのは、短い棒(13.5)の白いラベルが白地にはみ出して読めなくなるため。ラベルは棒の外に濃い字で出す。0 の点は消す
  L.paneHead(s, 0.5, 1.62, 6.3, '増収 3.64 億ドルの内訳(百万ドル)');
  const cats = ['純金利収益', 'ローン組成・売却の損益', 'インターチェンジ・会費ほか', 'LPB 手数料', 'テクノロジー'];
  s.addChart(pres.charts.BAR, [
    { name: '増加', labels: cats, values: [270.4, 79.5, 38.7, 13.5, 0] },
    { name: '減少', labels: cats, values: [0, 0, 0, 0, -38.3] },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 6.3, h: 3.3, objectName: 'chart',
    barDir: 'bar', barGrouping: 'clustered', barOverlapPct: 100, chartColors: [C.primary, C.red],
    dataLabelPosition: 'outEnd', dataLabelColor: C.text, dataLabelFormatCode: '0.0;-0.0;;',
    catAxisOrientation: 'maxMin', catAxisLabelPos: 'low',
    valAxisHidden: true, valGridLine: { style: 'none' }, valAxisMinVal: -80, valAxisMaxVal: 300,
    showLegend: true, legendPos: 'b',
  }));
  L.text(s, '会員当たり収益(年換算)は 304 → 316 ドル(+4%)。会員 +35% × 会員当たり +4% で増収 +40%。\n増収の 74% は B/S 貸出の利ざや。ローン損益の増加は主に金利スワップの益(前年は損失)', {
    x: 0.5, y: 5.4, w: 6.3, h: 1.25, fontSize: 9.5,
  });

  // 右上: 利益率の経路(事業エンジン)。行数が手本より多いので行の高さを 0.32 にして、次の見出しと重ならないようにする
  L.paneHead(s, 7.05, 1.62, 5.78, '利益率の経路(事業エンジン)');
  L.table(s, [
    ['年', '販促費率', '税引前利益率', 'ROTCE'],
    ['2026', '32.0%', '22.0%', '7〜9%'],
    ['2027', '30.0%', '25.7%', '10.9%'],
    ['2028', '28.5%', '28.6%', '12.5%'],
    ['2029', '27.0%', '31.3%', '13.6%'],
    ['2030', '25.5%', '33.7%', '14.5%'],
  ], { x: 7.05, y: 1.98, w: 5.78, colW: [1.2, 1.5, 1.6, 1.48], fontSize: 10, rowH: 0.32 });

  // 右中: 2026 年下期の計画が求めるもの
  L.paneHead(s, 7.05, 3.98, 5.78, '2026 年下期の計画が求めるもの');
  L.table(s, [
    ['', '上期(実績)', '下期(逆算)'],
    ['調整後 EBITDA 率', '30.4%', '35〜37%'],
    ['調整後純利益', '3.3 億ドル', '5.0 億ドル(+52%)'],
    ['増分 EBITDA 率(前年比)', '36%', '53〜64%'],
  ], { x: 7.05, y: 4.3, w: 5.78, colW: [2.3, 1.7, 1.78], fontSize: 10, rowH: 0.34 });

  // 右下: takeaway
  L.takeaway(s, 7.05, 5.75, 5.78, 0.9, '利益率の改善は構成の変化ではなく販促費率の低下(事業内の効果)にかかる。下期の達成が最初の試金石');
};
