// シナリオ確率と感応度(頑健さ)。左: 弱気の確率別の理論株価(株価の線つき)。右: 単独の前提を動かしたときの理論株価の変化
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    title: '確率加重の理論株価は 236 ドル。弱気の確率を 50% に上げても\n203 ドルで、株価を 46% 上回る',
    kicker: '左: 弱気シナリオの確率と理論株価(強気:ベース = 1:2 を固定)。右: 単独の前提を動かしたときの理論株価(加重)の変化',
    source: '需給エンジン第4.4版(calc/out/m9_fair.json・m9_extra.json・m9_more.json)',
    page: 34,
  });

  // 左: 弱気の確率別の理論株価(縦棒)
  const box = { x: 0.5, y: 1.65, w: 6.3, h: 4.6 };
  const lay = { x: 0.08, y: 0.06, w: 0.9, h: 0.82 };
  const MAX = 300;
  s.addChart(pres.charts.BAR, [
    { name: '理論株価(ドル)', labels: ['弱気 15%', '25%(本資料)', '35%', '50%', '75%'], values: [249, 236, 223, 203, 170] },
  ], L.chartStyle(Object.assign({}, box, {
    objectName: 'chart', chartColors: [L.C.primary], layout: lay,
    dataLabelFormatCode: '0', valAxisMinVal: 0, valAxisMaxVal: MAX,
  })));
  // 株価 139.56 ドルの線(プロット領域の座標で描く)
  const px = box.x + lay.x * box.w, py = box.y + lay.y * box.h, pw = lay.w * box.w, ph = lay.h * box.h;
  const yp = py + (1 - 139.56 / MAX) * ph;
  s.addShape('line', { x: px, y: yp, w: pw, h: 0.001, line: { color: C.red, width: 1.25, dashType: 'dash' }, objectName: 'ovl_price_line' });
  L.text(s, '株価 139.56 ドル', { x: px + pw - 1.3, y: yp - 0.11, w: 1.3, h: 0.22, fontSize: 9, bold: true, color: C.red, align: 'center', valign: 'middle', margin: 0, fill: { color: C.white }, line: { color: C.red, width: 0.75 }, objectName: 'ovl_price_t' });
  L.text(s, '株価 139.56 ドルに一致する弱気の確率は 71〜98%(定義により異なる)', {
    x: 0.5, y: 6.3, w: 6.3, h: 0.4, fontSize: 9.5, color: L.C.sub, objectName: 'note',
  });

  // 右: 単独の前提を動かしたときの変化(表)
  L.table(s, [
    ['前提(ベース → 変化)', '下側', '上側'],
    ['契約後の更新単価 ±20%', '−10.0', '+11.6'],
    ['逼迫の終わり −2 / +2 年', '−8.3', '+22.4'],
    ['同業 PER 20 / 26 倍', '−12.2', '+12.2'],
    ['PEG 0.8 / 1.2', '−11.3', '+11.3'],
    ['EPS −10% / +10%', '−16.4', '+16.4'],
    ['重み FY27 末のみ / 均等', '−12.7', '+1.5'],
    ['金利 6% 高止まり / 予測どおり低下', '−8.4', '+9.4'],
  ], { x: 7.05, y: 1.7, w: 5.78, colW: [3.3, 1.24, 1.24], fontSize: 10, rowH: 0.42 });

  L.takeaway(s, 7.05, 5.3, 5.78, 1.0, '最も効くのは EPS・逼迫の長さ・同業 PER。\nどれを単独で動かしても理論株価は株価を 57% 以上上回る');
};
