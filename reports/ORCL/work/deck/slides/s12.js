// 需要と供給(指示書 spec/ch2c.md の s12 節どおり)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    title: '推論・エージェント・ソブリン AI で需要は供給を上回り、部材と電力の不足を背景に 2026 年は主要クラウドが 15〜25% 値上げした',
    kicker: '左: 需要の種類と規模。右: 2026 年の値上げ(前回価格比)と供給の制約',
    source: 'research4/T4_ai_demand.md(McKinsey・Google・Anthropic・Gartner)、research4/T5_supply_components.md(TrendForce・UBS・各社の価格表)',
    page: 12,
  });

  // 左: 需要の種類と規模(表)
  L.paneHead(s, 0.5, 1.62, 6.05, '需要: 推論・エージェント・ソブリン');
  L.table(s, [
    ['種類', '規模と伸び'],
    ['推論', 'Google の月間トークン処理量 480 兆 → 3,200 兆(1 年で 6.7 倍)。\n推論の電力需要は 20.9 → 93.3GW(2030 年、年 35%)'],
    ['エージェント', '1 タスクのトークンはチャットの約 4 倍、複数エージェントで約 15 倍(Anthropic の自社データ)'],
    ['ソブリン', 'Stargate UAE 1GW(Oracle が運営)。ソブリンクラウド IaaS は\n2026 年 800 億ドル(+35.6%)。Oracle は日本に 80 億ドル超'],
    ['AI 全体', '学習 + 推論の電力は 44 → 156GW(2030 年、年 29%)。\nGoogle・AWS・Azure はそろって「供給制約」を明言'],
  ], { x: 0.5, y: 2.0, w: 6.05, colW: [1.15, 4.9], fontSize: 9.5, rowH: 0.78, align: ['left', 'left'] });
  L.text(s, '推論型モデルの計算 150 倍は DeepSeek と非推論モデルの 1 例の比較で、推論型モデル全般の値ではない', { x: 0.5, y: 6.0, w: 6.05, h: 0.7, fontSize: 8.5, color: C.sub });

  // 右: 供給の値上げ(横棒)と制約
  L.paneHead(s, 6.78, 1.62, 6.05, '供給: 値上げと制約');
  s.addChart(pres.charts.BAR, [
    { name: '値上げ率(%)', labels: ['H100 1年契約の指数', 'CoreWeave(全品目)', 'AWS Capacity Blocks', 'Oracle(GPU の更新)', 'Dell(全製品の定価)', 'Nebius(H100)'], values: [56, 25, 20, 20, 17, 17] },
  ], L.chartStyle({
    x: 6.78, y: 2.0, w: 6.05, h: 2.55, objectName: 'chart', barDir: 'bar', chartColors: [C.primary],
    dataLabelFormatCode: '"+"0"%"', valAxisMaxVal: 60, catAxisLabelFontSize: 9, catAxisOrientation: 'maxMin',
  }));
  L.bullets(s, [
    'メモリ: DRAM 契約価格は 2026 年に累計 約 3.7 倍、HBM の平均単価は 2027 年 +121%(TrendForce)。逼迫は 2028 年まで(UBS)',
    '電力: ガスタービンの受注残 116GW、計画中の DC 容量の 30〜50% が\n2028 年へ後ろ倒しの予想',
  ], { x: 6.78, y: 4.65, w: 6.05, h: 1.2, fontSize: 9.5 });
  L.takeaway(s, 6.78, 5.9, 6.05, 0.8, 'スマホと同じく、部材の逼迫が\n完成品(計算容量)の値上げとして買い手に転嫁されている');
};
