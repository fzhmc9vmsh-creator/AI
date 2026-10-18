// 市場との差分(指示書 spec/ch1_ch4.md の s31 節)。左上チャート・左下表・右上表・右下表の 4 区画
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左: 市場が付ける倍率と、株価が示す強気の確率。右: 市場の仮説と構造上の見方(差分の候補)、カタリストの日程',
    source: 'calc/out/val.json、research/R3a_market_hypothesis.md(Muddy Waters・KBW・Morgan Stanley・BofA・StoneX・Citi)、会社開示',
  });

  // 左上: 市場の倍率(横棒の積み上げ。市場だけアンバー、シナリオは緑)
  L.paneHead(s, 0.5, 1.62, 6.05, '市場の倍率(2026 年末、2027 年 EPS 比)');
  s.addChart(pres.charts.BAR, [
    { name: '市場', labels: ['弱気', '市場(株価 14.55)', 'ベース', '強気'], values: [0, 17.2, 0, 0] },
    { name: 'シナリオ', labels: ['弱気', '市場(株価 14.55)', 'ベース', '強気'], values: [16.4, 0, 16.4, 16.5] },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 6.05, h: 2.1, barDir: 'bar', barGrouping: 'stacked', chartColors: [L.C.amber, L.C.primary],
    dataLabelFormatCode: '0.0"倍";;;', dataLabelPosition: 'ctr', dataLabelColor: L.C.white, showLegend: false, objectName: 'chart',
  }));

  // 左下: 株価が示す強気の確率
  L.table(s, [
    ['株価が示す確率(定義)', '株価 14.55'],
    ['ベースと強気の 2 点で強気の確率を逆算', '40%'],
    ['本資料の確率(強気 25%・ベース 50%・弱気 25%)', '25%'],
  ], { x: 0.5, y: 4.25, w: 6.05, colW: [4.25, 1.8], fontSize: 9.5, rowH: 0.36 });
  L.text(s, '市場はベースと強気の間の、強気側 40% の位置にいる。\n会社計画(2028 年 EPS 約 1.1 ドル)の達成をかなりの確率で織り込む', {
    x: 0.5, y: 5.75, w: 6.05, h: 0.9, fontSize: 9.5, objectName: 'note',
  });

  // 右上: 市場の仮説 → 構造上の見方
  L.paneHead(s, 6.78, 1.62, 6.05, '市場の仮説 → 構造上の見方');
  L.table(s, [
    ['市場の仮説(出所)', '構造上の見方', '差分'],
    ['会計が甘い(Muddy Waters)', '損失の前提 4.8% は実績 3.7% より保守的。ただし割引率は薄い', '一部は過大(優位: 分析)'],
    ['成長が資本を食う(MS・KBW)', '自己資本比率 −4.1pt/半年。ROTCE < 資本コスト', '無し(市場と同じ)'],
    ['利益が売上に付いてこない(BofA)', '下期は増分利益率 50% 超が必要', '無し'],
    ['下げすぎ(StoneX・Citi)', '理論株価 13.4 で株価は上回る', '無し'],
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
