// 市場との差分(指示書 spec/v3.md の s31 節)。左上チャート・左下表・右上表・右下表の 4 区画
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左: シナリオ別の 1 株当たり価値と株価、株価が示す前提。右: 市場の仮説と構造上の見方(差分)、カタリストの日程',
    source: 'calc/out/growth_v3.json(節点ツリー・理論株価)、calc/out/val.json、research/R3a_market_hypothesis.md(Muddy Waters・KBW・Morgan Stanley・BofA・StoneX・Citi)、会社開示、research_r4/R13・R15・R17',
  });

  // 左上: シナリオ別の 1 株当たり価値と株価(横棒の 1 系列。点ごとの色は chartColors の配列で、株価の棒だけアンバー)
  L.paneHead(s, 0.5, 1.62, 6.05, 'シナリオ別の価値と株価(ドル)');
  s.addChart(pres.charts.BAR, [
    { name: '1 株当たり価値(ドル)', labels: ['弱気(27.5%)', 'ベース(48.9%)', '強気(23.6%)', '期待値', '株価'], values: [12.9, 21.5, 31.2, 21.4, 14.55] },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 6.05, h: 2.1, barDir: 'bar', chartColors: [L.C.primary, L.C.primary, L.C.primary, L.C.primary, L.C.amber],
    catAxisOrientation: 'maxMin', valAxisMinVal: 0, valAxisMaxVal: 35, valAxisHidden: true, valGridLine: { style: 'none' },
    dataLabelFormatCode: '0.0#', dataLabelPosition: 'outEnd', showLegend: false, objectName: 'chart',
  }));

  // 左下: 株価が示す前提(感応度の数値は指示書どおり)
  L.table(s, [
    ['株価が示す前提', '値'],
    ['PEG(エンジンの成長率のまま)', '0.85(構造 C の水準。本資料 1.25)'],
    ['損失率の恒常的な悪化(他は同じ)', '+2.3pt(all-in 約 6.0%)'],
    ['同業の最悪期・SoFi のピーク', 'LendingClub 5.0%・SoFi 4.0%'],
    ['N1・N2 を ±10pt 動かした期待値', '19.8〜23.1 ドル'],
  ], { x: 0.5, y: 4.25, w: 6.05, colW: [3.3, 2.75], fontSize: 9.5, rowH: 0.36 });
  L.text(s, '株価はどの感応度でも期待値を下回る。差の根拠は信用・資本・金利の過大評価(条件7)', {
    x: 0.5, y: 6.12, w: 6.05, h: 0.45, fontSize: 9.5, objectName: 'note',
  });

  // 右上: 市場の仮説 → 構造上の見方 → 差分
  L.paneHead(s, 6.78, 1.62, 6.05, '市場の仮説 → 構造上の見方');
  L.table(s, [
    ['市場の仮説(出所)', '構造上の見方', '差分'],
    ['金利で評価減(KBW)', '両面の合計 −0.54〜−0.90。\nヘッジで相殺', '過大(優位: 分析)'],
    ['信用が悪化する(景気)', '株価は同業の最悪期を超える\n損失を毎年織り込む', '過大(優位: 分析)'],
    ['成長が資本を食う(MS・KBW)', '下限まで 23 億ドル、\n弱気でも割らない', '一部過大'],
    ['利益が付いてこない(BofA)', '税と株数。税引前 +82%', '時間軸の見落とし'],
    ['会計が甘い(Muddy Waters)', '損失前提 4.8% > 実績 3.7%', '裏付けが弱い'],
  ], { x: 6.78, y: 1.98, w: 6.05, colW: [1.9, 2.2, 1.95], fontSize: 8.5, rowH: 0.36, name: 'tbl_hypothesis' });

  // 右下: カタリストの日程(10/27 の行だけ第3版の確認項目。他の行はそのまま)
  L.paneHead(s, 6.78, 4.3, 6.05, 'カタリストの日程');
  L.table(s, [
    ['時期', 'カタリスト', '何が分かるか'],
    ['10/27', 'Q3 2026 決算', 'ヘッジ後の評価の純額、all-in 損失率、\n販促費率、総自己資本比率、EPS 0.17'],
    ['10/28', 'FOMC', '利上げの有無(確率 3〜5 割)'],
    ['2027-01', 'Q4 決算・2027 年見通し', '2027 年の EPS・ROTCE の見通し'],
    ['2027-07', 'Q2 2027 決算', '自己資本比率 15% 前後で\nLPB への切替が進むか'],
    ['随時', '景気(失業率 4.2%)', 'all-in 貸倒率の上昇'],
  ], { x: 6.78, y: 4.65, w: 6.05, colW: [1.35, 2.0, 2.7], fontSize: 9, rowH: 0.34, name: 'tbl_catalyst' });
};
