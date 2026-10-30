// 株価の位置と価値の分布(指示書 r8b_judgment.md の担当 H3 の s31b。台帳 r8 J のモンテカルロ 1,500 通り)
// 左: 価値の分布の棒グラフ(株価と中央の線)。右上: 価値が株価を下回るときの表。右下: 信用の表。下: テイクアウェイ
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    title: '1,500 通りの価値の分布で、株価は 9 パーセンタイル。価値が株価を下回るのは、OpenAI・逼迫の終わり・再契約が同時に崩れる道だけ',
    kicker: '左: 価値の分布(1 株 = DCF、倒産確率込み)。右: 価値が株価を下回る条件と、本当のリスク',
    source: '需給エンジン第4.5版のモンテカルロ(calc/m10_mc.py、out/m10_mc.json)。変数と分布は台帳 r8 J',
    page: 0,
  });

  // 左: 価値の分布(25 ドル刻みの下限。75 は 75〜100 ドル、375 以上は 375〜400 ドルの幅で表す)
  L.paneHead(s, 0.5, 1.62, 7.6, '1 株価値の分布(DCF、1,500 通り)');
  const box = { x: 0.5, y: 1.95, w: 7.6, h: 3.45 };
  const lay = { x: 0.08, y: 0.145, w: 0.9, h: 0.75 };      // プロット領域の位置(上に札の段を空ける)
  const LO = 75, SPAN = 325;                               // 横軸: 75〜400 ドル(13 区間)
  const px = box.x + lay.x * box.w, pw = lay.w * box.w;
  const py = box.y + lay.y * box.h, ph = lay.h * box.h;
  const xAt = (v) => px + pw * (v - LO) / SPAN;
  s.addChart(pres.charts.BAR, [
    { name: '割合(%)', labels: ['75', '100', '125', '150', '175', '200', '225', '250', '275', '300', '325', '350', '375 以上'],
      values: [0.1, 5.0, 6.5, 11.9, 13.6, 18.9, 14.2, 11.6, 7.2, 4.1, 2.8, 1.7, 2.4] },
  ], L.chartStyle(Object.assign({}, box, {
    objectName: 'chart', chartColors: [C.primary], layout: lay, showValue: false,
    valAxisMinVal: 0, valAxisMaxVal: 20, valAxisMajorUnit: 5, valAxisLabelFormatCode: '0"%"',
  })));
  // 株価 139.56 ドルの線(赤の点線)と中央 217 の線(濃緑の点線)。札は線の上の段に置く
  const xP = xAt(139.56), xM = xAt(217);
  s.addShape('line', { x: xP, y: py - 0.05, w: 0.001, h: ph + 0.05, line: { color: C.red, width: 1.5, dashType: 'dash' }, objectName: 'ovl_price_line' });
  s.addShape('line', { x: xM, y: py - 0.05, w: 0.001, h: ph + 0.05, line: { color: C.dark, width: 1.5, dashType: 'dash' }, objectName: 'ovl_mid_line' });
  L.text(s, '株価 139.56\n(9 パーセンタイル)', { x: xP - 1.6, y: py - 0.5, w: 1.55, h: 0.42, fontSize: 9, bold: true, color: C.red, align: 'right', valign: 'bottom', margin: 0, objectName: 'ovl_price_t' });
  L.text(s, '中央 217', { x: xM + 0.06, y: py - 0.3, w: 1.2, h: 0.22, fontSize: 9, bold: true, color: C.dark, align: 'left', valign: 'middle', margin: 0, objectName: 'ovl_mid_t' });
  L.text(s, '平均 223・中央 217。5% 125・10% 143・90% 306・95% 340 ドル', { x: 0.5, y: 5.5, w: 7.6, h: 0.3, fontSize: 10, color: C.text, margin: 0, valign: 'middle', objectName: 'stat' });
  L.text(s, '横軸は 25 ドル刻みの下限(例: 125 は 125〜150 ドル)。縦軸は 1,500 通りに占める割合', { x: 0.5, y: 5.84, w: 7.6, h: 0.25, fontSize: 8.5, color: C.sub, margin: 0, valign: 'middle', objectName: 'note' });

  // 右上: 価値が株価を下回るときの内訳
  L.paneHead(s, 8.35, 1.62, 4.48, '価値が株価を下回るのはいつか');
  L.table(s, [
    ['条件', '割合', '価値の平均', '価値 < 株価'],
    ['OpenAI が払う', '75%', '244', '0%'],
    ['OpenAI の見直し・深刻', '25%', '146〜167', '30〜51%'],
    ['逼迫が FY30 に終わる', '25%', '159', '38%'],
    ['再契約 60% 未満', '26%', '157', '37%'],
    ['建設の遅れ 3.5GW', '20%', '221', '13%'],
  ], { x: 8.35, y: 2.0, w: 4.48, colW: [1.75, 0.7, 0.98, 1.05], fontSize: 9.5, rowH: 0.32, name: 'tbl_cond' });

  // 右下: 信用(本当のリスク)
  L.paneHead(s, 8.35, 4.05, 4.48, '信用(本当のリスク)');
  L.table(s, [
    ['信用の指標', '値(1,500 通り)'],
    ['レバレッジの最大', '4.42 倍(4.5 倍超の道なし)'],
    ['BB に落ちる道', 'なし'],
    ['一時 BB+ の確率', '40%(遅れ・AI 否定の見方)'],
    ['FY29 FCF 300 億以上', '38%(遅れなしなら 89%)'],
  ], { x: 8.35, y: 4.38, w: 4.48, colW: [1.7, 2.78], fontSize: 9.5, rowH: 0.32, name: 'tbl_credit' });

  // 下: テイクアウェイ(全幅)
  L.takeaway(s, 0.5, 6.2, 12.33, 0.55, '株価は、AI の循環が早く崩れる 9% の道の値。倒産の道はなく、本当のリスクは OpenAI 集中と\n格付けの閾値。期待値は株価の 1.60 倍で、下側 5% でも −11%');
  return s;
};
