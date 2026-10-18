// 市場との差分(指示書 spec/ch1_ch4.md の s31 節)。左上チャート・左下表・右上表・右下表の 4 区画
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左: シナリオ別の 1 株当たり価値と株価、株価が示す強気の確率。右: 市場の仮説と構造上の見方(差分の候補)、カタリストの日程',
    source: 'calc/out/growth_v2.json(節点ツリー・理論株価)、calc/out/val.json、research/R3a_market_hypothesis.md(Muddy Waters・KBW・Morgan Stanley・BofA・StoneX・Citi)、会社開示',
  });

  // 左上: シナリオ別の 1 株当たり価値と株価(横棒の 1 系列。点ごとの色は chartColors の配列で、株価の棒だけアンバー)
  L.paneHead(s, 0.5, 1.62, 6.05, 'シナリオ別の価値と株価(ドル)');
  s.addChart(pres.charts.BAR, [
    { name: '1 株当たり価値(ドル)', labels: ['弱気(29.9%)', 'ベース(48.3%)', '強気(21.7%)', '期待値', '株価'], values: [11.8, 14.9, 18.2, 14.7, 14.55] },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 6.05, h: 2.1, barDir: 'bar', chartColors: [L.C.primary, L.C.primary, L.C.primary, L.C.primary, L.C.amber],
    catAxisOrientation: 'maxMin', valAxisMinVal: 0, valAxisMaxVal: 22, valAxisHidden: true, valGridLine: { style: 'none' },
    dataLabelFormatCode: '0.0#', dataLabelPosition: 'outEnd', showLegend: false, objectName: 'chart',
  }));

  // 左下: 株価が示す強気の確率
  L.table(s, [
    ['株価が示す確率(定義)', '値'],
    ['株価に合う強気の確率\n(弱気 29.9% を固定し、強気とベースの比を逆算)', '16.6%'],
    ['本資料の確率(節点ツリー)', '21.7%'],
    ['N1・N2 を ±10pt 動かした幅', '13.6〜31.9%'],
  ], { x: 0.5, y: 4.25, w: 6.05, colW: [4.25, 1.8], fontSize: 9.5, rowH: 0.36 });
  L.text(s, '差 5pt は感応度の幅の内側。買いの根拠になる差分にはならない', {
    x: 0.5, y: 5.75, w: 6.05, h: 0.9, fontSize: 9.5, objectName: 'note',
  });

  // 右上: 市場の仮説 → 構造上の見方
  L.paneHead(s, 6.78, 1.62, 6.05, '市場の仮説 → 構造上の見方');
  L.table(s, [
    ['市場の仮説(出所)', '構造上の見方', '差分'],
    ['会計が甘い(Muddy Waters)', '損失の前提 4.8% は実績 3.7% より保守的。ただし割引率は薄い', '一部は過大(優位: 分析)'],
    ['成長が資本を食う(MS・KBW)', '自給率 0.34、律速は自己資本', '無し(市場と同じ)'],
    ['利益が売上に付いてこない(BofA)', '販促の裁量的な再投資\n(6 検査中 4 つが攻め)', '見方の違い\n(価値への効きは小さい)'],
    ['下げすぎ(StoneX・Citi)', '理論株価 14.7 で株価とほぼ同じ', '無し'],
  ], { x: 6.78, y: 1.98, w: 6.05, colW: [1.9, 2.2, 1.95], fontSize: 8.5, rowH: 0.42, name: 'tbl_hypothesis' });

  // 右下: カタリストの日程
  L.paneHead(s, 6.78, 4.2, 6.05, 'カタリストの日程');
  L.table(s, [
    ['時期', 'カタリスト', '何が分かるか'],
    ['10/27', 'Q3 2026 決算', 'EPS 0.17 の達成、公正価値のマーク、\n販促費率、総自己資本比率'],
    ['10/28', 'FOMC', '利上げの有無(確率 3〜5 割)'],
    ['2027-01', 'Q4 決算・2027 年見通し', '2027 年の EPS・ROTCE の見通し'],
    ['2027-07', 'Q2 2027 決算', '自己資本比率 15% 前後で\nLPB への切替が進むか'],
    ['随時', '景気(失業率 4.2%)', 'all-in 貸倒率の上昇'],
  ], { x: 6.78, y: 4.55, w: 6.05, colW: [1.35, 2.0, 2.7], fontSize: 9, rowH: 0.34, name: 'tbl_catalyst' });
};
