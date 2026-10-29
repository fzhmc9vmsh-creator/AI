// 2-5 信用と資本の制約(指示書 spec/v4.md の s13b 節。手本: s15b の表 2 段)
// 左上: 個人ローンの純償却率の同業比較。左下: 資本と還元・増資の同業比較。右: 価値への効き(株数と EPS 経路で数える)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '上: 個人ローンの純償却率(年率)と借り手の質。下: 自己資本と還元・増資。右: 価値への効きと株価が示す前提(倍率では割り引かず、EPS 経路と株数で数える)',
    source: 'research_r5/Q3_datasheet.md(SoFi の Q3 2026)、research_r4/R16・R17(同業。検索要約。SoFi の CET1 は要検証)、calc/out/growth_v4.json の credit_capital',
  });

  // ---- 左上: 信用(個人ローンの純償却率) ----
  L.paneHead(s, 0.5, 1.62, 7.9, '信用(個人ローンの純償却率)', 'pane_credit');
  L.table(s, [
    ['貸し手', '直近', '2023〜24 年のピーク', '借り手の質'],
    ['SoFi', '報告 2.26%・all-in 約 3.4%(Q3)', '3.98%(2023Q4)', 'FICO 746・年収 15.8 万ドル\n(Q4 2025)'],
    ['LendingClub(保有分)', '3.2%', '5.0%(2023 年通期)', '未取得'],
    ['Discover', '4.21%(2025Q1)', '4.24%(2024Q4)', '未取得'],
    ['Capital One 国内カード(参考)', '4.71%', '—', '—'],
  ], {
    x: 0.5, y: 2.0, w: 7.9, colW: [2.0, 2.2, 1.6, 2.1], fontSize: 9, rowH: 0.36,
    align: ['left', 'center', 'center', 'left'], name: 'tbl_credit',
  });

  // ---- 左下: 資本(自己資本・還元・増資) ----
  L.paneHead(s, 0.5, 4.0, 7.9, '資本', 'pane_capital');
  L.table(s, [
    ['会社', 'CET1・総自己資本', '還元', '増資'],
    ['SoFi', '総自己資本 17.0%・CET1 16.9%\n(下限 14%、余裕 17 億ドル)', '0%', '2025 年に約 33 億ドル。Q3 は増資を確認できず。\n経営陣は 2027 年も不要と発言'],
    ['LendingClub', 'CET1 17.0%', '未取得', '見つからず'],
    ['Capital One', 'CET1 13.7%', '約 107%', '—'],
    ['Ally', 'CET1 10.1%', '自社株買い', '—'],
  ], {
    x: 0.5, y: 4.38, w: 7.9, colW: [1.05, 2.5, 0.85, 3.5], fontSize: 9, rowH: 0.36,
    align: ['left', 'left', 'center', 'left'], name: 'tbl_capital',
  });

  // ---- 右: 価値への効き(エンジン 23.8 ドル。growth_v4.json の credit_capital) ----
  L.paneHead(s, 8.65, 1.62, 4.18, '価値への効き(エンジン 23.8 ドル)', 'pane_value');
  L.table(s, [
    ['前提', '理論株価'],
    ['損失率 +0.5pt', '21.9'],
    ['+1.0pt(2023 年並み)', '20.2'],
    ['+2.0pt(all-in 約 5.4%)', '16.9'],
    ['増資 10 億ドル\n(株数 +5%)', '23.4'],
    ['総自己資本比率(信用 +1.0pt)', '15.8% 以上'],
  ], {
    x: 8.65, y: 2.0, w: 4.18, colW: [2.8, 1.38], fontSize: 9, rowH: 0.4,
    align: ['left', 'center'], name: 'tbl_value',
  });

  // 右下: 結論(株価が示す前提。左の資本の表の下端に揃える)
  L.takeaway(s, 8.65, 4.6, 4.18, 1.6, '株価 14.55〜16.5 ドルは、損失率が\n毎年 +2.1〜2.7pt 続く前提。\n同業の最悪期(5.0%)を上回る');
  return s;
};
