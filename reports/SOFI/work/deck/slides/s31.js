// 市場との差分(指示書 spec/v4.md の s31 節)。左上チャート・左下表・右上表・右下表の 4 区画
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左: シナリオ別の 1 株当たり価値と株価、株価が示す前提。右: 市場の仮説と構造上の見方(差分)、カタリストの日程',
    source: 'calc/out/growth_v4.json(節点ツリー・理論株価・感応度)、research_r5/Q3_datasheet.md(Q3 の実績)、research/R3a_market_hypothesis.md(Muddy Waters・KBW・Morgan Stanley・BofA・StoneX・Citi)、会社開示、research_r4/R13・R15・R17',
  });

  // 左上: シナリオ別の 1 株当たり価値と株価(横棒の 1 系列。点ごとの色は chartColors の配列で、株価と目安の棒だけアンバー)
  L.paneHead(s, 0.5, 1.62, 6.05, 'シナリオ別の価値と株価(ドル)');
  s.addChart(pres.charts.BAR, [
    { name: '1 株当たり価値(ドル)', labels: ['弱気(24.1%)', 'ベース(49.3%)', '強気(26.6%)', '期待値', '株価(10/16 終値)', '決算後の目安'], values: [13.9, 24.2, 33.5, 24.2, 14.55, 16.5] },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 6.05, h: 2.1, barDir: 'bar', chartColors: [L.C.primary, L.C.primary, L.C.primary, L.C.primary, L.C.amber, L.C.amber],
    catAxisOrientation: 'maxMin', valAxisMinVal: 0, valAxisMaxVal: 38, valAxisHidden: true, valGridLine: { style: 'none' },
    dataLabelFormatCode: '0.0#', dataLabelPosition: 'outEnd', showLegend: false, objectName: 'chart',
  }));

  // 左下: 株価が示す前提(数値は growth_v4.json の implied・tree_sens と Q3 の実績)
  L.table(s, [
    ['株価が示す前提', '値'],
    ['PEG(エンジンの成長率のまま)', '0.80(14.55)・0.90(16.5)。本資料 1.275'],
    ['損失率の恒常的な悪化', '+2.7pt(14.55)・+2.1pt(16.5)'],
    ['実績の損失率', 'all-in 約 3.4%(Q3、改善)'],
    ['N1・N2 を ±10pt 動かした期待値', '22.4〜26.0 ドル'],
  ], { x: 0.5, y: 4.25, w: 6.05, colW: [2.85, 3.2], fontSize: 9.5, rowH: 0.36 });
  L.text(s, '株価はどの感応度でも期待値を下回る。差の根拠は信用・資本・金利の過大評価(条件7)', {
    x: 0.5, y: 6.12, w: 6.05, h: 0.45, fontSize: 9.5, objectName: 'note',
  });

  // 右上: 市場の仮説 → 構造上の見方 → 差分
  L.paneHead(s, 6.78, 1.62, 6.05, '市場の仮説 → 構造上の見方');
  L.table(s, [
    ['市場の仮説(出所)', '構造上の見方', '差分'],
    ['金利で評価減(KBW)', '両面の合計 −0.54〜−0.90。\nヘッジで相殺', '過大(優位: 分析)'],
    ['信用が悪化する(景気)', '株価は同業の最悪期を超える\n損失を毎年織り込む', '過大(優位: 分析)'],
    ['成長が資本を食う(MS・KBW)', '下限まで 17 億ドル。\n2027 年から資本の上限が効く', '一部過大'],
    ['利益が付いてこない(BofA)', 'EPS 0.18 は費用の引き下げでなく\n増収で作られた', '時間軸の見落とし'],
    ['会計が甘い(Muddy Waters)', '損失前提 4.8% > 実績 約 3.4%', '裏付けが弱い'],
  ], { x: 6.78, y: 1.98, w: 6.05, colW: [1.9, 2.2, 1.95], fontSize: 8.5, rowH: 0.36, name: 'tbl_hypothesis' });

  // 右下: カタリストの日程(3 行。2027-01〜02 の行は総自己資本比率 16% 割れの四半期を見る)
  L.paneHead(s, 6.78, 4.3, 6.05, 'カタリストの日程');
  L.table(s, [
    ['時期', 'カタリスト', '何が分かるか'],
    ['2027-01〜02', 'Q4 決算・2027 年の詳細', '総自己資本比率 16% 割れの四半期の\nLPB の割合、all-in 損失率、中期目標の扱い'],
    ['2027-04', 'Q1 2027 決算', 'Tech Platform の前年比プラス転換'],
    ['随時', '景気(失業率 4.2%)', '延滞の上昇'],
  ], { x: 6.78, y: 4.65, w: 6.05, colW: [1.35, 2.0, 2.7], fontSize: 9, rowH: 0.34, name: 'tbl_catalyst' });
};
