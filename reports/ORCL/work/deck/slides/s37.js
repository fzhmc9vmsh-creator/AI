// 37 時系列投資戦略(指示書 ch4b.md s37)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    title: '株価は Z1 を下回るので、いま 2/3 を建てる。残り 1/3 は、建設の遅れで一時 BB+ になりうる FY28 下期〜FY29 の値下がりに備えて残す',
    kicker: '時系列投資戦略(4 フェーズ)。確認 KPI は第3章の監視 KPI と共通',
    source: '銘柄分析メソッド scenario-strategy §7、本資料 第3章・最終判断',
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

  // 下段: フェーズごとの期間・やること・確認 KPI・撤退条件(2〜5 列は左揃え)
  L.table(s, [
    ['', 'エントリー期', '検証期', '本格保有期', '再評価期'],
    ['期間', '今から 1〜2 四半期', '2〜4 四半期', 'FY29 の格付け通過と\nFY30 の FCF 反転の後', '株価が理論株価に近づいた後'],
    ['やること', '株価は Z1(151 ドル)を下回る。\nいま 2/3 を建て、残りは\nFY28 下期〜FY29 の値下がりに備える', '確認 KPI を四半期ごとに確かめる', '確度に応じて増やす', '新しい差分を探し、なければ縮小する'],
    ['確認 KPI', 'Q2 FY27 の capex の進み・営業 CF・前払い・納入 MW', '納入 1GW/四半期以上、36 か月比率\n50% 以上、FY28 下期の FCF 黒字化、\nOpenAI 比率 40% 未満', 'FCF 黒字の継続\n(会社: FY29 300 億以上)\nAI 粗利率 35% 以上', 'PEG 1.0 以上、コンセンサスとの差'],
    ['撤退条件', 'OpenAI の見直し・支払い遅延、\n逼迫の終わりの兆し(GPU 時間貸しの下落・capex 削減)が 2 つ以上', '合格ラインを 2 四半期続けて下回り、\n一時要因で説明できない', 'OpenAI の支払いの破綻', '差分の消失'],
  ], { x: 0.5, y: 2.55, w: 12.33, colW: [1.45, 2.72, 2.72, 2.72, 2.72], fontSize: 9.5, rowH: 0.66, align: ['left', 'left', 'left', 'left', 'left'] });

  // 下: 判別の規則
  L.takeaway(s, 0.5, 5.95, 12.33, 0.7, 'Q2 決算で capex と納入が計画どおりなら残りも建ててよい。\n撤退は OpenAI の見直しと逼迫の終わりの兆しが重なったとき');
};
