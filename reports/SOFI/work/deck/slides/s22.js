// 条件6 成長と割安度(評価 B)。指示書 spec/ch3.md の s22 節どおり
// 本文は構造図ではなく表。右パネルは L.t15Side
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '条件6 3 年 EPS 成長率で PEG<1(EPS CAGR 30% 前後)。EPS は調整後(会社定義)。PER は株価 14.55 ドル ÷ 2026 年 EPS 0.60',
    source: 'コンセンサス(research_r2/R8_peers_consensus.md)、会社の中期目標(2025〜28 年の調整後 EPS CAGR 38〜42%、2026-01-30。上端 42% を 2028 年まで使い、以降は +32%・+25%)、需給エンジン(calc/out/val.json の paths)',
    grade: 'B', condNo: 6,
  });
  L.table(s, [
    ['経路', '2026', '2029', '3 年 CAGR', 'PER', 'PEG'],
    ['コンセンサス', '0.60', '1.32', '30.1%', '24.3', '0.81'],
    ['会社の目標(42%)の延長', '0.60', '1.47', '34.9%', '24.3', '0.70'],
    ['需給エンジン', '0.60', '1.35', '31.1%', '24.3', '0.78'],
  ], { x: 0.5, y: 1.75, w: 8.3, colW: [2.1, 1.25, 1.25, 1.2, 1.2, 1.3], fontSize: 11, rowH: 0.42 });
  L.bullets(s, [
    '年ごとの伸びはエンジンで +41% → +31% → +22% → +23%、コンセンサスで +38% → +30% → +22% → +18%。\n2029 年以降は 20% 台',
    '成長の約 3 割は販促費率の低下(32% → 27%)による。\n販促費率を据え置くと 2029 年 EPS は 1.13 ドル(エンジン 1.35)',
    '条件7 が C(安い理由の主因は実在のリスク)のため、規則により B が上限',
  ], { x: 0.5, y: 3.7, w: 8.3, h: 1.0, fontSize: 10.5 });
  s.addChart(pres.charts.BAR, [{ name: '3 年 CAGR(%)', labels: ['コンセンサス', '会社の目標の延長', '需給エンジン'], values: [30.1, 34.9, 31.1] }],
    L.chartStyle({ x: 0.5, y: 4.75, w: 8.3, h: 1.95, barDir: 'col', chartColors: [L.C.primary], dataLabelFormatCode: '0.0"%"', valAxisMinVal: 0, valAxisMaxVal: 40, objectName: 'chart_cagr' }));
  L.text(s, '閾値 30%', { x: 6.9, y: 5.1, w: 1.9, h: 0.28, fontSize: 9, color: L.C.amber, align: 'right', objectName: 'ovl_thr' });
  L.t15Side(s, {
    evidence: ['PER 24.3 倍 = 14.55 ÷ 2026 年 EPS 0.60', '3 年 CAGR は 2026 → 2029 年', 'コンセンサスとエンジンの差は 2029 年で 0.03 ドル(EPS に差分なし)'],
    reason: '数値は PEG<1 を満たすが、余裕が小さく\n条件7 と対で評価して B',
  });
};
