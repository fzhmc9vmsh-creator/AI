// 資金と信用(1/2): 預金と資本。指示書 spec/ch2.md の s12 節どおり
// 型: 左にチャートと表、右に表・bullets・takeaway
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 総自己資本比率の経路(%、2026 年末以降は事業エンジン)。右: 預金の調達コストと構成',
    source: '10-Q(Q1・Q2 2026)の規制資本の表、research_r2/R7_funding_rates_capital.md、calc/out/val.json',
  });

  // 左: 総自己資本比率(実績と予想を積み上げ。該当しない年は 0 にしてラベルを消す)
  L.paneHead(s, 0.5, 1.62, 6.3, '総自己資本比率(%)');
  const yrs = ['2025-12', '2026-03', '2026-06', '2026-12予', '2027-12予', '2028-12予'];
  s.addChart(pres.charts.BAR, [
    { name: '実績', labels: yrs, values: [22.9, 21.3, 18.8, 0, 0, 0] },
    { name: '予想', labels: yrs, values: [0, 0, 0, 17.0, 16.1, 16.3] },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 6.3, h: 2.9, objectName: 'chart',
    barDir: 'col', barGrouping: 'stacked', chartColors: [C.primary, C.light],
    dataLabelPosition: 'inEnd', dataLabelColor: C.white, dataLabelFormatCode: '0.0;-0.0;;',
    valAxisMinVal: 0, valAxisMaxVal: 25,
    showLegend: true, legendPos: 'b',
  }));
  L.table(s, [
    ['', '2025-12', '2026-06'],
    ['リスク資産(RWA)', '372 億ドル', '487 億ドル(+31%)'],
    ['総自己資本', '85.2 億ドル', '91.7 億ドル'],
  ], { x: 0.5, y: 4.95, w: 6.3, colW: [2.1, 2.1, 2.1], fontSize: 10, rowH: 0.32 });
  L.text(s, '運用下限は low-to-mid teens(14〜15%)。エンジンでは 2027 年に貸出の伸びが\n資本で止まり(+32% の希望 → 約 +22%)、溢れた分を LPB に回す', { x: 0.5, y: 6.0, w: 6.3, h: 0.7, fontSize: 9.5 });

  // 右: 預金の調達コストの表、箇条書き、結論
  L.paneHead(s, 7.05, 1.62, 5.78, '預金の調達コスト');
  L.table(s, [
    ['指標', '値'],
    ['預金の平均金利(2026 年上期)', '3.07%\n(普通 3.24%・当座 1.07%・定期 3.95%)'],
    ['倉庫ラインとの差', '1.93pt(2024-12)→ 1.56pt(2026-06)'],
    ['年間の金利の節約', '7.1 億ドル'],
    ['普通預金の金利', '3.30%(9 月の利上げ後も据え置き)'],
    ['ブローカー預金の比率', '3.7% → 10.0%(半年)'],
  ], { x: 7.05, y: 2.0, w: 5.78, colW: [2.7, 3.08], fontSize: 10, rowH: 0.38, align: ['left', 'left'] });
  L.bullets(s, [
    '利上げ(9/16、FF 3.75〜4.00%)の後も普通預金の金利を据え置き、\n利ざやは守られている',
    '預金の増加の約 6 割がブローカー預金。\n給与振込の預金の伸びが貸出に追いついていない',
  ], { x: 7.05, y: 4.4, w: 5.78, h: 1.3, fontSize: 10 });
  L.takeaway(s, 7.05, 5.8, 5.78, 0.85, '安い資金は続くが差は縮小。\n成長の上限を決めるのは資金ではなく自己資本');
};
