// 市場の見方・波及・カタリスト(指示書 spec/ch4b.md の s31 節)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    title: '株価は事業実態 EPS の 15.7 倍で弱気(13.6 倍)寄り。前払い・長期リースは ROIC を支え、OpenAI 集中は底堅さを下げる。試金石は 10 月末〜12 月の開示',
    kicker: '左: 市場が付ける倍率と、株価が示す弱気の確率。右: 構造の変化が数字に及ぶ道筋と、カタリストの日程',
    source: '需給エンジン第4.3版(calc/out/m8_fair.json)、Oracle AI World 公式ページ、会社開示、report/ORCL_report.md §11',
    page: 31,
  });

  // ↑ は緑字、↓ は赤字
  const up = t => ({ text: t, options: { color: L.C.primary } });
  const down = t => ({ text: t, options: { color: L.C.red } });

  // 左上: 市場の倍率(横棒。市場だけアンバー、他は緑系)
  L.paneHead(s, 0.5, 1.62, 6.05, '市場の倍率(FY27 末、翌年度の事業実態 EPS 比)');
  s.addChart(pres.charts.BAR, [
    { name: '市場', labels: ['弱気', '市場(株価 143.20)', 'ベース', '強気'], values: [0, 15.7, 0, 0] },
    { name: 'シナリオ', labels: ['弱気', '市場(株価 143.20)', 'ベース', '強気'], values: [13.6, 0, 26.5, 32.3] },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 6.05, h: 2.1, barDir: 'bar', barGrouping: 'stacked', chartColors: [L.C.amber, L.C.primary],
    dataLabelFormatCode: '0.0"倍";;;', dataLabelPosition: 'ctr', dataLabelColor: L.C.white, showLegend: false, objectName: 'chart',
  }));

  // 左下: 株価が示す弱気の確率
  L.table(s, [
    ['株価が示す弱気の確率(定義)', '株価 143.20'],
    ['強気:ベース = 1:2 を固定して弱気の確率を逆算', '87%'],
    ['ベースと弱気の 2 点で逆算', '84%'],
    ['DCF の値で定義1 と同じ計算', '72%'],
  ], { x: 0.5, y: 4.25, w: 6.05, colW: [4.25, 1.8], fontSize: 9.5, rowH: 0.36 });
  L.text(s, '市場は弱気とベースの間の、弱気側 16% の位置にいる。疑っているのは EPS ではなく、\nEPS が現金になるか(FY29 の FCF・格付け・OpenAI)', {
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
    ['10/25〜28', 'AI World 2026(日程は\n出典で 1 日ずれあり)', '新製品、FY30 以降の目標の有無'],
    ['12 月中旬', 'Q2 FY27 決算(日付は未確定)', '納入 MW、AI 粗利率、FCF、\n受注残の構成'],
    ['2027-02', 'NM のガス管の稼働予定', 'Jupiter(2.45GW)の時期'],
    ['2027 前半', 'OpenAI の大型資金調達', '支払能力'],
    ['FY29', 'FCF の黒字化(S&P の条件)', '格下げの回避'],
  ], { x: 6.78, y: 4.55, w: 6.05, colW: [1.35, 2.0, 2.7], fontSize: 9, rowH: 0.34, name: 'tbl_catalyst' });
};
