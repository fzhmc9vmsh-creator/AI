// 条件6 成長と割安度(評価 A・第3版)。指示書 spec/v3.md の s22 節どおり(作り直し)
// 上: 経路ごとの EPS の伸び・PEG と市場・同業との比(表)。下: PEG の横棒。右: L.t15Side
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '条件6: EPS 成長 30% 以上かつ PEG<1 を満たせば B(A 寄り)から出発し、市場と同業からの乖離で A まで上げる(第5版)。PER は 12 か月先 18.6 倍(EPS 0.78)',
    source: 'research_r4/R13_peer_growth_peg.md(FactSet・各社コンセンサスの要約)、calc/out/growth_v3.json の cond6',
    grade: 'A', condNo: 6,
  });

  // 上の表: 3 経路と A の基準(基準の行は灰の字)
  const g = { color: C.sub };
  L.table(s, [
    ['経路', 'EPS の伸び\n(26→28)', 'PEG', '市場の PEG\nとの比', '市場の成長\nとの倍率', '同業の中央値\nとの比'],
    ['コンセンサス', '34.2%', '0.54', '0.43', '2.3 倍', '1.05'],
    ['会社の計画の延長', '36.4%', '0.51', '0.40', '2.4 倍', '0.98'],
    ['事業エンジン', '35.7%', '0.52', '0.41', '2.4 倍', '1.00'],
    [{ text: 'A の基準', options: g }, { text: '30% 以上', options: g }, { text: '1 未満', options: g },
      { text: '0.6 以下', options: g }, { text: '2 倍以上', options: g }, { text: '1.00 以下', options: g }],
  ], { x: 0.5, y: 1.75, w: 8.3, colW: [2.3, 1.25, 1.0, 1.25, 1.2, 1.3], fontSize: 10, rowH: 0.4 });

  // 下: PEG の横棒(SOFI は主色、S&P 500 は市場としてアンバー、同業は薄緑)
  L.paneHead(s, 0.5, 4.0, 8.3, 'PEG の比較(小さいほど割安)');
  s.addChart(pres.charts.BAR, [
    { name: 'PEG', labels: ['SOFI', 'NU', 'COF', 'LC', 'ALLY', 'HOOD', 'S&P 500'], values: [0.54, 0.52, 0.51, 0.33, 0.33, 1.62, 1.27] },
  ], L.chartStyle({
    x: 0.5, y: 4.3, w: 8.3, h: 2.3, barDir: 'bar',
    chartColors: [C.primary, C.light, C.light, C.light, C.light, C.light, C.amber],
    catAxisOrientation: 'maxMin', valAxisMinVal: 0, valAxisMaxVal: 2, valAxisHidden: true, valGridLine: { style: 'none' },
    dataLabelFormatCode: '0.00', showLegend: false, objectName: 'chart_peg',
  }));

  L.t15Side(s, {
    evidence: [
      'S&P 500 は PER 19.0 倍・2027 年の EPS 成長 約 15%・PEG 1.27',
      '成長の近い同業(NU 0.52・LC 0.33・HOOD 1.4〜1.8)の中央値 0.52',
      '安さは消費者金融の群の安さ(ALLY・LC 0.33、COF 0.51)',
    ],
    reason: '市場比は 3 経路とも A の基準を大きく\n超える。同業とは並ぶため S ではなく A',
  });
};
