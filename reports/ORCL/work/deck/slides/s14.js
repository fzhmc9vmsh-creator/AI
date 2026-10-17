// 上積みの2つ: SaaS と Database@(指示書 spec/ch2b.md の s14 節どおり)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    title: '上積みの2つ: SaaS は旧 ERP 顧客の移行で 10% → 14% に加速すると見て、Database@ は FY30 に 46 億ドル・1株 5 ドルの純増と置く',
    kicker: '左: SaaS の先行指標・製品特性・反証と前提。右: Database@ の伸び(前年同期比)と前提',
    source: 'research4/T3_saas_products.md、research2/R4_database_at.md、research3/W6_database_at.md、需給エンジン第4.3版(calc/model8.py)',
    page: 14,
  });

  // 左: SaaS の表と前提
  L.paneHead(s, 0.5, 1.62, 6.05, 'SaaS: 製品の特性から加速を読む');
  L.table(s, [
    ['観点', '事実'],
    ['実績', 'SaaS +10%(Q1 FY27)。直近 5 四半期は\n10〜13% で、まだ加速していない'],
    ['先行指標', '繰延収益 +16% が売上 +10% を上回る(Q4 FY26、要約 1 件)'],
    ['移行の余地', '旧来 ERP の顧客 8,500 社のうち Fusion へ移行済みは約 1,000 社(CEO 発言、時点不明)'],
    ['需要', 'エージェント型 AI のソフト支出は 2030 年に 9,850 億ドル(Gartner)'],
    ['同業', 'SAP クラウド +22%、ServiceNow 購読 +24.5%、Salesforce +11%'],
    ['反証', 'エージェントは追加料金なし。AI で席数が減る懸念(2026-02 に\nソフト株が急落)'],
  ], { x: 0.5, y: 2.0, w: 6.05, colW: [1.45, 4.6], fontSize: 9.5, rowH: 0.44, align: ['left', 'left'] });
  L.takeaway(s, 0.5, 5.2, 6.05, 1.5, '前提: FY27 10% → FY31 14% → FY36 に 8%。ERP は取引データと\n実行権限を持つため、エージェントの普及は移行を後押しする。\n反証は弱気シナリオで −2pt として数える');

  // 右: Database@ の縦棒と前提
  L.paneHead(s, 6.78, 1.62, 6.05, 'Database@: 3 桁成長は続くが減速している');
  s.addChart(pres.charts.BAR, [
    { name: 'Database@ 前年同期比(%)', labels: ['Q1 FY26', 'Q2', 'Q3', 'Q4', 'Q1 FY27'], values: [1529, 817, 531, 404, 353] },
  ], L.chartStyle({
    x: 6.78, y: 2.0, w: 6.05, h: 2.6, objectName: 'chart',
    barDir: 'col', chartColors: [C.teal], dataLabelFormatCode: '0"%"', valAxisMaxVal: 1800,
  }));
  L.bullets(s, [
    '70 リージョン・119 AZ(Azure 33・Google 14・AWS 22)、顧客数 +180%',
    '前提: FY30 に 46 億ドル。移行した保守売上(70%)÷ 移行倍率 2.5 を\n保守から差し引いても 1 株 5.4 ドルの純増',
    '会社の FY30 目標(クラウド DB 全体 200 億ドル)より保守的。\n伸びは毎期 5pt ずつ減速させた',
  ], { x: 6.78, y: 4.75, w: 6.05, h: 1.95, fontSize: 10 });
};
