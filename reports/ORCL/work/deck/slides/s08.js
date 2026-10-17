// 5W1H 台帳(8 群)。指示書 spec/ch2b.md の s08 節どおり(Haiku 担当)。表と役割列の色だけで組む
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    title: '製品・サービスを 8 群に分けると、利益は DB 保守、成長は AI 容量、上積みは Database@ と SaaS が担う',
    kicker: '製品・サービスの 5W1H 台帳(8 群に集約)。売上は報告区分の値で、製品単独の額はほとんど開示されていない',
    source: 'report/r3_sections_5w1h_f20.md §2-0(会社開示・10-Q・価格表の第三者集計)。Q1 FY27 = 2026 年 6〜8 月',
    page: 8,
  });

  // 役割の列の色: 利益の柱=濃緑太字 / 成長・成長の主因=緑太字 / 上積み系=ティール / 他=灰
  const role = (text, options) => ({ text, options });
  const dark = { color: C.dark, bold: true };
  const green = { color: C.primary, bold: true };
  const teal = { color: C.teal };
  const grey = { color: C.sub };

  L.table(s, [
    ['群', '誰が買う(Who)', '何を・どう課金(What / How)', '売上(Q1 FY27、前年比)', '役割'],
    ['DB ライセンス・保守(Java・旧来アプリ含む)', '既存の大企業・官公庁。Java は全業種', 'DB はプロセッサー単位 + 年 22% の保守。Java は従業員数 × 月額', 'Software 区分 55.5 億ドル(−3%)', role('利益の柱', dark)],
    ['OCI 一般・主権クラウド', '企業全般。主権は NRI・富士通・中東の通信会社', '計算・保存・通信の従量。主権クラウドは最低 5 年のコミット', 'IaaS 区分 74 億ドル(+121%、AI を含む)', role('成長', green)],
    ['AI 容量', 'OpenAI・xAI・Meta など AI 研究所', 'GPU 時間(H100 定価 10 ドル/時)。6 年で 600 億ドルの契約例。更新は +20%', 'IaaS 区分に含む(単独は非開示)', role('成長の主因', green)],
    ['Database@', '他社クラウド中心で Oracle DB を使う企業(顧客数 +180%)', '他社の DC 内で Exadata・Autonomous を稼働。ECPU 時間で課金', '+353%(額は非開示)', role('上積み', teal)],
    ['Autonomous・Exadata', '大規模な Oracle DB の既存顧客', 'ECPU 時間。Cloud@Customer は 4 年のサブスク', 'Hardware 区分 約 8 億ドル(+15%)ほか', role('DB の器', grey)],
    ['SaaS(Fusion・NetSuite)', '大企業(Fusion)・中堅(NetSuite)', '従業員数・ユーザー数 × 月額。AI エージェントは追加料金なし', 'SaaS 区分 42 億ドル(+10%)', role('上積み(加速の候補)', teal)],
    ['業種別・Oracle Health', '病院・退役軍人省、ホテル・銀行・小売', '契約ごと。電子カルテは上限額方式', '業種別 +20% 超(額は非開示)', role('選択的', grey)],
    ['サービス', 'Fusion・OCI・Health の導入顧客', '導入・移行・運用支援。工数・固定額', '14.1 億ドル(+4.8%)', role('付随', grey)],
  ], {
    x: 0.5, y: 1.62, w: 12.33, colW: [2.15, 2.6, 3.6, 2.45, 1.53], fontSize: 9.5, rowH: 0.5,
    align: ['left', 'left', 'left', 'left', 'center'],
  });

  L.takeaway(s, 0.5, 6.2, 12.33, 0.5, '利益は DB 保守、成長は AI 容量、上積みは Database@ と SaaS。AI 容量だけが製品単独の売上を開示していない');
  return s;
};
