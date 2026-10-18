// シナリオ確率と感応度 T7(指示書 spec/ch1_ch4a.md の s34 節)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    title: '確率加重 251 ドル。弱気の確率を 50% に上げても 207 ドルで、株価を 45% 上回る',
    kicker: '左: 弱気シナリオの確率と理論株価(強気:ベース = 1:2 を固定)。右: 単独の前提を動かしたときの理論株価(加重)の変化',
    source: '需給エンジン第4.3版(calc/out/m8_fair.json・m8_extra.json)',
    page: 34,
  });

  // 左: 弱気の確率別の理論株価(縦棒)
  s.addChart(pres.charts.BAR, [
    { name: '理論株価(ドル)', labels: ['弱気 15%', '25%(本資料)', '35%', '50%', '75%'], values: [268, 251, 233, 207, 164] },
  ], L.chartStyle({
    x: 0.5, y: 1.65, w: 6.3, h: 4.6, objectName: 'chart', chartColors: [L.C.primary],
    dataLabelFormatCode: '0', valAxisMinVal: 0, valAxisMaxVal: 300,
  }));
  L.text(s, '株価 143.20 ドルに一致する弱気の確率は 72〜87%(定義により異なる)', {
    x: 0.5, y: 6.3, w: 6.3, h: 0.4, fontSize: 9.5, color: L.C.sub, objectName: 'note',
  });

  // 右: 単独の前提を動かしたときの変化(表)
  L.table(s, [
    ['前提(ベース → 変化)', '下側', '上側'],
    ['同業 PER 23 倍 → 20 / 26 倍', '−10.8', '+10.8'],
    ['PEG 1.0 → 0.8 / 1.2', '−16.7', '+16.7'],
    ['EPS −10% / +10%', '−17.2', '+17.2'],
    ['重み → FY27 末のみ / 均等', '−25.6', '+9.5'],
    ['金利 → 6% 高止まり / 予測どおり低下', '−8.8', '+14.6'],
    ['EPS をエンジンの値にする', '−11.5', '—'],
    ['PEG の成長率から自社株買いの効果を除く', '−3.6〜−10.0', '—'],
  ], { x: 7.05, y: 1.7, w: 5.78, colW: [3.3, 1.24, 1.24], fontSize: 10, rowH: 0.36 });

  L.takeaway(s, 7.05, 5.1, 5.78, 1.1, '最も効くのは重み・EPS・PEG。\nどれを単独で動かしても理論株価は株価を 57% 以上上回る');
};
