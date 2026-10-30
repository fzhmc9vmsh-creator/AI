// 時系列投資戦略(指示書 ch4b.md の s37。r9_external.md の G の s37: 撤退の表に「売る量」を追加)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    title: '株価は Z1 を下回るので、いま 2/3 を建てる。残り 1/3 は、建設の遅れで一時 BB+ になりうる FY28 下期〜FY29 の値下がりに備えて残す',
    kicker: '時系列投資戦略(4 フェーズ)。確認 KPI は第3章の監視 KPI と共通',
    source: '銘柄分析メソッド scenario-strategy §7、本資料 第3章・最終判断、需給エンジン第4.5版の分布(台帳 r8 J・r9 F)',
    page: 37,
  });

  // 上段: 4 つの矢羽(x 0.5 から幅 3.0、重ね 0.1)。薄緑の矢羽だけ濃緑の文字
  const phases = [
    { label: '1 エントリー期', fill: L.C.dark, font: L.C.white },
    { label: '2 検証期', fill: L.C.primary, font: L.C.white },
    { label: '3 本格保有期', fill: L.C.light, font: L.C.dark },
    { label: '4 再評価期', fill: L.C.teal, font: L.C.white },
  ];
  phases.forEach((p, i) => {
    const x = 0.5 + i * 2.9;
    s.addShape('chevron', { x, y: 1.7, w: 3.0, h: 0.7, fill: { color: p.fill }, line: { color: p.fill }, objectName: 'ovl_chev' + i });
    s.addText(p.label, { x, y: 1.7, w: 3.0, h: 0.7, fontFace: L.FONT, fontSize: 12, bold: true, color: p.font, align: 'center', valign: 'middle', margin: 0, isTextBox: true, objectName: 'ovl_chev_t' + i });
  });

  // 中段: フェーズごとの期間・やること・確認 KPI・撤退条件(行の高さを詰めた)
  L.table(s, [
    ['', 'エントリー期', '検証期', '本格保有期', '再評価期'],
    ['期間', '今から 1〜2 四半期', '2〜4 四半期', 'FY29 の格付け通過と\nFY30 の FCF 反転の後', '株価が理論株価に近づいた後'],
    ['やること', '株価は Z1(151 ドル)を下回る。\nいま 2/3 を建て、残りは\nFY28 下期〜FY29 の値下がりに備える', '確認 KPI を四半期ごとに確かめる', '確度に応じて増やす', '新しい差分を探し、なければ縮小する'],
    ['確認 KPI', 'Q2 FY27 の capex の進み・営業 CF・前払い・納入 MW', '納入 1GW/四半期以上、36 か月比率\n50% 以上、FY28 下期の FCF 黒字化、\nOpenAI 比率 40% 未満', 'FCF 黒字の継続\n(会社: FY29 300 億以上)\nAI 粗利率 35% 以上', 'PEG 1.0 以上、コンセンサスとの差'],
    ['撤退条件', 'OpenAI の深刻な不払い、または\n逼迫の終わり(FY30)+\n再契約 6 割未満(売る量は下の表)', '合格ラインを 2 四半期続けて下回り、\n一時要因で説明できない', 'OpenAI の支払いの破綻', '差分の消失'],
  ], { x: 0.5, y: 2.5, w: 12.33, colW: [1.45, 2.72, 2.72, 2.72, 2.72], fontSize: 9.5, rowH: [0.3, 0.46, 0.62, 0.62, 0.62], align: ['left', 'left', 'left', 'left', 'left'] });

  // 下段左: 撤退の表(起きたこと → 何をするか。売る量まで決める)
  L.table(s, [
    ['起きたこと', '何をするか(保有の何割を売るか)'],
    ['OpenAI の見直し(85% 払い)', '売らず、買い増しを止める(価値の平均 167 > 株価)'],
    ['OpenAI の深刻な不払い(5 割払い)', '半分を売る(価値の平均 146 ≒ 株価)'],
    ['逼迫の終わり(FY30)+ 再契約 6 割未満', '全部を売る(価値の平均 133、71% の道で株価割れ)'],
    ['建設の遅れで一時 BB+', '売らず、残りの 1/3 を建てる(価値は変わらない)'],
    ['会計の耐用年数の短縮(6 → 4 年)', '売らない(現金は変わらない)'],
  ], { x: 0.5, y: 5.27, w: 8.0, colW: [3.4, 4.6], fontSize: 9.5, rowH: 0.25, align: ['left', 'left'], name: 'tbl_withdraw' });

  // 下段右: 判別の規則
  L.takeaway(s, 8.7, 5.27, 4.13, 1.5, 'Q2 決算で capex と納入が\n計画どおりなら、残りも建ててよい。\n売る条件は左の表だけ。\nOpenAI の見直しだけでは売らない');
};
