// 事業実態 EPS の経路(指示書 spec/v4.md の s32 節)。左に折れ線、右に takeaway と bullets
// 注: 3 経路(エンジン・会社の中期目標・見通し + コンセンサスの伸び)は 2026〜2030 年の線。
//     4 節点すべて成功・失敗(○○○○・××××)は growth_v4.json の tree.combos[].eps の 2026〜2030 年の全年で引く。
// pptxgenjs はデータラベルの表示を系列ごとに変えられないため、エンジンだけを第2グループ(第2軸、同じ目盛り・非表示)に載せ、ラベルを出す。
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '事業実態 EPS(調整後 EPS。株式報酬を費用に含む)、ドル。3 経路と、4 節点すべて成功・すべて失敗の線は、いずれも 2026〜2030 年',
    source: 'calc/out/growth_v4.json(3 経路の EPS・tree.combos の 2026〜2030 年 EPS)、research_r5/Q3_datasheet.md §3(見通し・コンセンサス)、会社の中期目標(2025→28 年 EPS CAGR 38〜42%)',
  });
  const labels = ['2026', '2027', '2028', '2029', '2030'];
  const axis = { valAxisMinVal: 0, valAxisMaxVal: 2.4, valAxisMajorUnit: 0.4 };
  s.addChart([
    { type: pres.charts.LINE, data: [
      { name: '会社の中期目標', labels, values: [0.61, 0.9, 1.117, 1.396, 1.703] },
      { name: '見通し + コンセンサスの伸び', labels, values: [0.61, 0.9, 1.171, 1.431, 1.689] },
      { name: '4 節点すべて成功(確率 9.6%、2030 年 2.27)', labels, values: [0.6899, 1.0718, 1.4246, 1.8048, 2.2730] },
      { name: '4 節点すべて失敗(確率 8.1%、2030 年 1.29)', labels, values: [0.5349, 0.7238, 0.8917, 1.0700, 1.2897] },
    ], options: { showValue: false } },
    { type: pres.charts.LINE, data: [
      { name: 'エンジン(事業エンジン)', labels, values: [0.612, 0.898, 1.153, 1.423, 1.753] },
    ], options: { showValue: true, secondaryValAxis: true, secondaryCatAxis: true, chartColors: [L.C.dark], dataLabelFormatCode: '[<0.65]"";0.00' } },
  ], L.chartStyle({
    x: L.M, y: 1.65, w: 8.35, h: 5.0, objectName: 'chart',
    showLegend: true, legendPos: 'b', chartColors: [L.C.teal, L.C.light, L.C.primary, L.C.red], lineSize: 2, lineDataSymbolSize: 6,
    dataLabelPosition: 't', dataLabelFormatCode: '0.00', ...axis,
    valAxes: [Object.assign({}, axis), Object.assign({ valAxisHidden: true }, axis)],
    catAxes: [{ catAxisLineShow: true }, { catAxisHidden: true }],
  }));
  L.takeaway(s, 9.05, 1.7, 3.78, 1.5, '2026・2027 年は会社の見通し(0.61・0.90)。\n2026→29 年は年 32.5%。2028 年のエンジン\n1.15 は中期目標の上端 1.12 を超える。\n2028 年の目標は控えめ');
  L.bullets(s, [
    'ROTCE(エンジン)は 2026 年 8.4% から\n2030 年 15.2%',
    '2027 年は資本の上限で B/S の伸びが\n抑えられ、溢れた分は LPB へ',
    '強気・弱気は、4 節点(獲得効率・資本の\n転換・信用・新しい収益線)を同じ幅で\n逆に動かした(対称)',
    '4 節点すべて成功は 2026 年 0.69 → 2030 年 2.27\n(確率 9.6%、36.3 ドル)。すべて失敗は\n0.54 → 1.29(確率 8.1%、12.2 ドル)',
  ], { x: 9.05, y: 3.35, w: 3.78, h: 3.3, fontSize: 10.5, name: 'points' });
};
