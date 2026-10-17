// 事業理解(1/3): 事業の積み木(左)+ 8 群の 5W1H 台帳(右)+ 用語の注釈(下)。指示書 spec/r6_new.md の s08 節どおり
module.exports = function build(pres, L) {
  const { C, FONT } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 事業の積み木(どの層を、どこで売るか)。右: 8 群の 5W1H 台帳。下: この資料で使う用語の注釈',
    source: 'report/r3_sections_5w1h_f20.md §2-0(会社開示・10-Q・価格表の第三者集計)、research2/R4_database_at.md。Q1 FY27 = 2026 年 6〜8 月',
  });

  // ---------- 左: 事業の積み木(層 × 動く場所) ----------
  L.paneHead(s, 0.5, 1.62, 4.45, '事業の積み木(層 × 動く場所)');
  const cx = [1.5, 2.65, 3.8], cw = 1.1, ry = [2.3, 3.1, 3.9], ch = 0.72;
  ['顧客の DC', 'OCI', '他社クラウド'].forEach((t, j) =>
    L.text(s, t, { x: cx[j], y: 1.98, w: cw, h: 0.26, fontSize: 9, bold: true, color: C.dark, align: 'center', valign: 'middle', margin: 0, objectName: 'blk_colh' + j }));
  ['アプリ', 'データ(DB)', 'インフラ', '土台'].forEach((t, i) =>
    L.text(s, t, { x: 0.5, y: i < 3 ? ry[i] : 4.7, w: 0.95, h: i < 3 ? ch : 0.42, fontSize: 9, bold: true, color: C.dark, align: 'center', valign: 'middle', margin: 0, objectName: 'blk_rowh' + i }));

  // 種類: tint = 上積み(薄緑)/ key = 利益の柱(濃緑)/ grow = 成長(緑)/ none = 該当なし(灰)
  const KIND = {
    tint: { fill: C.tint, line: C.light, color: C.dark, bold: false },
    key: { fill: C.dark, line: C.dark, color: C.white, bold: false },
    grow: { fill: C.primary, line: C.primary, color: C.white, bold: false },
    none: { fill: C.gray, line: C.gray, color: C.sub, bold: false },
  };
  const cell = (i, j, k, str) => {
    const o = KIND[k];
    s.addText(str, { shape: 'roundRect', rectRadius: 0.06, x: cx[j], y: ry[i], w: cw, h: ch, fill: { color: o.fill }, line: { color: o.line, width: 0.75 },
      fontFace: FONT, fontSize: 8.5, color: o.color, align: 'center', valign: 'middle', margin: 0.02, objectName: `blk_c${i}${j}` });
  };
  cell(0, 0, 'tint', '旧来の業務アプリ\n(E-Business ほか)');
  cell(0, 1, 'tint', 'Fusion・NetSuite\n(SaaS)');
  cell(0, 2, 'none', '—');
  cell(1, 0, 'key', 'DB ライセンス・\n保守・Exadata');
  cell(1, 1, 'key', 'Autonomous\nAI Database 26ai');
  cell(1, 2, 'key', 'Database@\n(AWS・Azure・\nGoogle)');
  cell(2, 0, 'grow', 'Cloud@Customer');
  cell(2, 1, 'grow', 'OCI 一般・主権\nAI 容量(GPU)');
  cell(2, 2, 'none', '—');
  s.addText('電力付きの建屋(開発事業者が建てて 15〜19 年で貸す)', { shape: 'roundRect', rectRadius: 0.06, x: cx[0], y: 4.7, w: cx[2] + cw - cx[0], h: 0.42,
    fill: { color: C.gray }, line: { color: C.rule, width: 0.75 }, fontFace: FONT, fontSize: 8.5, color: C.dark, align: 'center', valign: 'middle', margin: 0.04, objectName: 'blk_base' });
  L.text(s, '濃緑 = 利益の柱、緑 = 成長、薄緑 = 上積み', { x: 0.5, y: 5.2, w: 4.45, h: 0.32, fontSize: 8.5, color: C.sub, valign: 'middle', margin: 0, objectName: 'blk_legend' });

  // ---------- 右: 8 群の 5W1H 台帳 ----------
  L.paneHead(s, 5.15, 1.62, 7.68, '8 群の 5W1H 台帳(売上は Q1 FY27 の報告区分)');
  // 役割の列の色: 利益の柱=濃緑太字 / 成長・成長の主因=緑太字 / 上積み系=ティール / 他=灰
  const role = (text, options) => ({ text, options });
  const dark = { color: C.dark, bold: true };
  const green = { color: C.primary, bold: true };
  const teal = { color: C.teal };
  const grey = { color: C.sub };
  L.table(s, [
    ['群', '誰が買う', '何を・どう課金', '売上(前年比)', '役割'],
    ['DB ライセンス・保守\n(Java・旧来アプリ含む)', '既存の大企業・官公庁\nJava は全業種', { text: 'DB はプロセッサ単位 + 保守は年 22%\nJava は従業員数 × 月額', options: { margin: [0.03, 0, 0.03, 0.06] } }, 'Software 区分\n55.5 億ドル(−3%)', role('利益の柱', dark)],
    ['OCI 一般・主権クラウド', '企業全般。主権は NRI・\n富士通・中東の通信会社', '計算・保存・通信の従量課金\n主権は最低 5 年のコミット', { text: 'IaaS 区分 74 億ドル\n(+121%、AI 含む)', options: { margin: [0.03, 0, 0.03, 0.06] } }, role('成長', green)],
    ['AI 容量', 'OpenAI・xAI・Meta など\nAI 研究所', 'GPU 時間(H100 定価 10 ドル/時)\n例: 6 年 600 億ドル。更新 +20%', 'IaaS 区分に含む\n(単独は非開示)', role('成長の主因', green)],
    ['Database@', { text: 'Oracle DB を他社クラウドで\n使う企業(顧客数 +180%)', options: { margin: [0.03, 0, 0.03, 0.06] } }, '他社の DC 内で Exadata・\nAutonomous を稼働。ECPU 時間課金', '+353%\n(額は非開示)', role('上積み', teal)],
    ['Autonomous・Exadata', '大規模な Oracle DB の\n既存顧客', 'ECPU 時間で課金\nCloud@Customer は 4 年のサブスク', 'Hardware 区分\n約 8 億ドル(+15%)', role('DB の器', grey)],
    ['SaaS\n(Fusion・NetSuite)', '大企業(Fusion)\n中堅(NetSuite)', '従業員数・ユーザー数 × 月額\nAI エージェントは追加料金なし', 'SaaS 区分\n42 億ドル(+10%)', role('上積み\n(加速候補)', teal)],
    ['業種別・Oracle Health', '病院・退役軍人省\nホテル・銀行・小売', '契約ごと\n電子カルテは上限額方式', '業種別 +20% 超\n(額は非開示)', role('選択的', grey)],
    ['サービス', 'Fusion・OCI・Health の\n導入顧客', '導入・移行・運用支援\n工数・固定額', '14.1 億ドル\n(+4.8%)', role('付随', grey)],
  ], {
    x: 5.15, y: 1.98, w: 7.68, colW: [1.55, 1.75, 2.3, 1.3, 0.78], fontSize: 8.5, rowH: 0.4,
    align: ['left', 'left', 'left', 'left', 'center'],
  });

  // ---------- 下: 用語の注釈(この資料に出てくる順) ----------
  L.paneHead(s, 0.5, 5.58, 12.33, '用語の注釈(この資料に出てくる順)');
  const terms = [
    ['OCI', 'Oracle のクラウド。計算・保存・通信を従量で貸す'],
    ['AI 容量', 'AI 用の GPU 計算力の貸出。OCI の一部'],
    ['GW(ギガワット)', 'データセンターの電力容量。AI 容量の規模の単位'],
    ['受注残(RPO)', '契約済みでまだ売上にしていない額。6,640 億ドル'],
    ['Database@', '他社クラウドの DC 内で動く Oracle DB'],
    ['Exadata・Autonomous', 'DB 専用の機械と、運用を自動化した DB'],
    ['AI Database 26ai', 'AI 検索とエージェントを内蔵した DB の最新版'],
    ['保守(サポート)', 'ライセンス価格の年 22% を毎年払う更新料'],
    ['BYOL', '持っているライセンスをクラウドへ持ち込むこと'],
    ['ソブリンクラウド', 'データを国内に置く政府・規制業種向け'],
    ['ネオクラウド', 'GPU 貸出の専業(CoreWeave・Nebius など)'],
    ['事業実態 EPS', '非GAAP EPS から株式報酬(税引後)を引いた EPS'],
  ];
  terms.forEach(([term, desc], k) => {
    const col = Math.floor(k / 4), row = k % 4;
    L.text(s, [
      { text: term, options: { bold: true, color: C.dark } },
      { text: ' — ' + desc, options: { color: C.text } },
    ], { x: [0.5, 4.65, 8.8][col], y: 5.92 + row * 0.2, w: 4.03, h: 0.2, fontSize: 8.5, margin: 0, valign: 'middle', objectName: `note_${k}` });
  });
  return s;
};
