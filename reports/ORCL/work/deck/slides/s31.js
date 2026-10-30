// 市場の見方・波及・カタリスト(指示書 spec/ch4b.md の s31 節)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    title: '株価は事業実態 EPS の 13.9 倍で、説明会の後も弱気シナリオの値に近い。市場は EPS ではなく現金化を疑い、次の試金石は 12 月の Q2 決算',
    kicker: '左: 市場が付ける倍率と、株価が示す弱気の確率。右: 構造の変化が数字に及ぶ道筋と、カタリストの日程',
    source: '需給エンジン第4.5版(calc/out/m10_*.json)、Investor Day 2026-10-28、会社開示、report/ORCL_report.md §11',
    page: 31,
  });

  // ↑ は緑字、↓ は赤字
  const up = t => ({ text: t, options: { color: L.C.primary } });
  const down = t => ({ text: t, options: { color: L.C.red } });

  // 左上: 市場の倍率(横棒。市場だけアンバー、他は緑系)
  L.paneHead(s, 0.5, 1.62, 6.05, '市場の倍率(FY27 末、翌年度の事業実態 EPS 比)');
  s.addChart(pres.charts.BAR, [
    { name: '市場', labels: ['弱気', '市場(株価 139.56)', 'ベース', '強気'], values: [0, 13.9, 0, 0] },
    { name: 'シナリオ', labels: ['弱気', '市場(株価 139.56)', 'ベース', '強気'], values: [13.8, 0, 24.0, 31.0] },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 6.05, h: 2.1, barDir: 'bar', barGrouping: 'stacked', chartColors: [L.C.amber, L.C.primary],
    dataLabelFormatCode: '0.0"倍";;;', dataLabelPosition: 'ctr', dataLabelColor: L.C.white, showLegend: false, objectName: 'chart',
  }));

  // 左下: 株価が示す弱気の確率
  L.table(s, [
    ['株価が示す弱気の確率(定義)', '株価 139.56'],
    ['強気:ベース = 1:2 を固定して弱気の確率を逆算', '96%'],
    ['ベースと弱気の 2 点', '95%'],
    ['DCF の値で定義1 と同じ計算', '77%'],
  ], { x: 0.5, y: 4.25, w: 6.05, colW: [4.25, 1.8], fontSize: 9.5, rowH: 0.36 });
  L.text(s, '市場は説明会の後も、株価を弱気シナリオの値(134 ドル)に置く。\n疑っているのは EPS ではなく、EPS が現金になるか(資金・格付け・OpenAI)。\nCDS・社債は市場の評価で、本当のリスクは数字で別に判断する', {
    x: 0.5, y: 5.75, w: 6.05, h: 0.9, fontSize: 9.5, objectName: 'note',
  });

  // 右上: 構造の変化 → 数字への波及
  L.paneHead(s, 6.78, 1.62, 6.05, '構造の変化 → 数字への波及');
  L.table(s, [
    ['構造の変化', 'ROIC', '需要の長さ', '底堅さ'],
    ['前払い・持ち込み', up('↑ 進行中'), '—', up('↑')],
    ['逼迫前の長期リース', up('↑ FY47 まで'), '—', down('↓ 需要鈍化時は\n固定費')],
    ['OpenAI への集中', '—', up('↑ 2032 年まで'), down('↓ 2027〜')],
    ['SaaS へのエージェント組込み', '—', up('↑'), up('↑')],
    ['Database@ の配置', up('↑'), up('↑'), up('↑')],
  ], { x: 6.78, y: 1.98, w: 6.05, colW: [2.15, 1.3, 1.3, 1.3], fontSize: 9, rowH: 0.34, name: 'tbl_ripple' });

  // 右下: カタリストの日程
  L.paneHead(s, 6.78, 4.2, 6.05, 'カタリストの日程');
  L.table(s, [
    ['時期', 'カタリスト', '何が分かるか'],
    ['10/25〜28', 'AI World 2026(日程は\n出典で 1 日ずれあり)', '済み(10/28 Investor Day: FCF の時期と資金の上限を開示)'],
    ['12 月中旬', 'Q2 FY27 決算', 'capex の進み・営業 CF・前払い、\n納入 MW、AI 粗利率'],
    ['2027-02', 'NM のガス管の稼働予定', 'Jupiter(2.45GW)の時期'],
    ['2027 前半', 'OpenAI の大型資金調達', '支払能力'],
    ['FY29', 'FCF 300 億ドル以上\n(会社の約束)', '格下げの回避'],
  ], { x: 6.78, y: 4.55, w: 6.05, colW: [1.35, 2.0, 2.7], fontSize: 9, rowH: 0.34, name: 'tbl_catalyst' });
};
