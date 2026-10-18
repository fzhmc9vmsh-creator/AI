// 事業実態 EPS の経路(指示書 spec/ch1_ch4.md の s32 節)。左に折れ線、右に takeaway と bullets
// 注: pptxgenjs はデータラベルの表示を系列ごとに変えられないため、強気・弱気・コンセンサスを第1グループ(ラベルなし)、
//     ベースだけを第2グループ(第2軸、同じ目盛り・非表示)に載せ、ベースだけラベルを出す。
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '事業実態 EPS(調整後 EPS。株式報酬を費用に含む)、ドル。2026〜29 年はコンセンサス・会社目標・事業エンジン、2030 年は延長',
    source: 'コンセンサス(R2・R8)、会社の中期目標(2025→28 年 EPS CAGR 38〜42%)、calc/out/growth_v2.json(4 節点すべて成功・失敗)、calc/out/val.json(事業エンジン)。過去の成長率は使っていない',
  });
  const labels = ['2026', '2027', '2028', '2029', '2030(延長)'];
  const axis = { valAxisMinVal: 0, valAxisMaxVal: 2.2 };
  s.addChart([
    { type: pres.charts.LINE, data: [
      { name: '4 節点すべて成功', labels, values: [0.673, 1.01, 1.367, 1.716, 2.156] },
      { name: '4 節点すべて失敗', labels, values: [0.525, 0.684, 0.854, 1.015, 1.221] },
      { name: 'コンセンサス', labels, values: [0.60, 0.83, 1.08, 1.32, 1.558] },
    ], options: { showValue: false } },
    { type: pres.charts.LINE, data: [
      { name: 'ベース(事業エンジン)', labels, values: [0.5993, 0.8448, 1.1034, 1.3494, 1.6571] },
    ], options: { showValue: true, secondaryValAxis: true, secondaryCatAxis: true, chartColors: [L.C.dark] } },
  ], L.chartStyle({
    x: L.M, y: 1.65, w: 8.35, h: 5.0, objectName: 'chart',
    showLegend: true, legendPos: 'b', chartColors: [L.C.light, L.C.red, L.C.teal], lineSize: 2, lineDataSymbolSize: 6,
    dataLabelPosition: 't', dataLabelFormatCode: '0.00', ...axis,
    valAxes: [Object.assign({}, axis), Object.assign({ valAxisHidden: true }, axis)],
    catAxes: [{ catAxisLineShow: true }, { catAxisHidden: true }],
  }));
  L.takeaway(s, 9.05, 1.7, 3.78, 1.35, 'ベースの 2026→29 年の CAGR は 31%。\nコンセンサスとの差は ±3% で、\nEPS の見通しに差分は無い');
  L.bullets(s, [
    'ROTCE(エンジン)は 2027 年 10.9%\n→ 2030 年 14.5%。定常(成長投資を止めた場合)は\n約 15%(必要資本ベース 18%)',
    '2027 年から自己資本比率の下限で貸出の伸びが止まり、溢れた分は LPB へ回る',
    '強気・弱気は 4 節点(獲得効率・資本の転換・\n信用・新しい収益線)を同じ幅で\n逆に動かした(対称)',
  ], { x: 9.05, y: 3.2, w: 3.78, h: 3.45, fontSize: 10.5, name: 'points' });
};
