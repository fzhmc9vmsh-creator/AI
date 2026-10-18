// 3-4 銀行免許 × フィンテックの組み合わせと資本コスト(複合構成。手本: s11 の「左に表、右に図」と s12 のチャート)
// 左: 希少さの表と再現コスト / 右: 必要利回りの積み上げ縦棒と節約の使い道 / 下: takeaway(横長)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 組み合わせの希少さと再現コスト。右: 貸出 100 ドル当たりの税引前の必要利回り(負債 85.5% + 株主資本 14.5%、費用と信用損失の前)と、預金の節約の使い道',
    source: 'calc/A2_growth_memo.md §5、calc/out/growth_v2.json(g8)、research_r2/R7(預金と倉庫ラインの差)、research/R4・research_r3/R12(競合)',
  });

  // ---- 左: 希少さの表 ----
  L.paneHead(s, 0.5, 1.62, 6.05, '希少さ(片方だけを持つ相手と比べる)', 'pane_l');
  const me = (t) => ({ text: t, options: { bold: true, color: C.dark, fill: { color: C.tint } } });
  L.table(s, [
    ['会社', '銀行免許・預金', 'フィンテックの製品・技術基盤'],
    [me('SoFi'), me('国法銀行(2022)、\n預金 455 億ドル'), me('会員 1,580 万人、\nGalileo・Technisys(外販)')],
    ['LendingClub', '銀行(2021 年に買収)、\n預金 102 億ドル', '個人ローン中心、\n外販の基盤なし'],
    ['Chime', 'なし(提携銀行)', '会員 1,040 万人、\n自社基盤 ChimeCore'],
    ['Robinhood', 'なし(銀行業務は提携)', '資金入り顧客 2,840 万人'],
    ['Upstart', 'なし(買い手・資本市場で資金)', 'AI 審査の貸出'],
    ['伝統的な銀行', 'あり(無利息預金が厚く、\n預金コストは低い)', '製品の速さ・会員の伸びで劣る'],
  ], {
    x: 0.5, y: 2.0, w: 6.05, colW: [1.1, 2.45, 2.5], fontSize: 9, rowH: 0.37,
    align: ['left', 'left', 'left'], name: 'tbl_rare',
  });

  // ---- 左の下: 再現コスト ----
  L.paneHead(s, 0.5, 4.78, 6.05, '再現コスト', 'pane_l2');
  L.bullets(s, [
    '販促費 26.2 億(2024〜26 年上期)+ 技術の買収 約 23 億 + 払込資本 7.5 億\n= 約 57 億ドルと数年(時価総額 約 188 億ドルの約 3 割)',
    '部品ごとの再現例はある: LendingClub は買収で約 1 年で免許、\nChime は基盤を自前で、Robinhood は提携で銀行業務',
  ], { x: 0.5, y: 5.12, w: 6.05, h: 0.95, fontSize: 10, name: 'bul_repro' });

  // ---- 右: 必要利回りの積み上げ縦棒 ----
  L.paneHead(s, 6.78, 1.62, 6.05, '必要利回り(%、税引前)', 'pane_r');
  const cats = ['SoFi(β 1.93)', '免許なしの\nフィンテック', 'SoFi(β 1.3 なら)', 'SoFi(β 1.0 なら)'];
  const totals = ['5.24', '6.57', '4.71', '4.45'];
  const cx = 6.78, cw = 6.05;
  s.addChart(pres.charts.BAR, [
    { name: '負債', labels: cats, values: [2.62, 3.96, 2.62, 2.62] },
    { name: '株主資本', labels: cats, values: [2.61, 2.61, 2.08, 1.83] },
  ], L.chartStyle({
    x: cx, y: 2.3, w: cw, h: 2.3, objectName: 'chart',
    barDir: 'col', barGrouping: 'stacked', chartColors: [C.primary, C.amber],
    dataLabelPosition: 'ctr', dataLabelColor: C.white, dataLabelFormatCode: '0.00', barGapWidthPct: 60,
    valAxisMinVal: 0, valAxisMaxVal: 7, valAxisMajorUnit: 1, valAxisLabelFormatCode: '0',
    showLegend: true, legendPos: 'r',
  }));
  // 合計の注記(棒の上の列。カテゴリの中心に合わせる)
  const px0 = cx + 0.28, pw = 1.215;   // 値軸の目盛(左)と凡例(右)を除いた作図域の見積もり(画像で棒の中心に合わせた)
  totals.forEach((t, i) => {
    L.text(s, [{ text: '合計 ', options: { fontSize: 9, color: C.sub } }, { text: t, options: { fontSize: 12, bold: true, color: C.dark } }],
      { x: px0 + i * pw, y: 2.0, w: pw, h: 0.28, align: 'center', valign: 'middle', margin: 0, objectName: 'total_' + i });
  });

  // ---- 右の下: 読み取り ----
  L.bullets(s, [
    '負債は銀行並みに安い: 預金で 1.33pt 得(免許なし比)。\n株主資本はテック並みに高い: β 1.93 の負担は銀行並みの β 比 0.79pt',
    '預金は貸出の資金で、広告・開発の直接の原資ではない。原資は厚くなった利ざや:\n節約 年 7.1 億ドル = 販促費の 45%、販促 + 開発の 31%(税引後 1 株 0.40 ドル)',
    '広告・開発は自己資本(コスト 13.9%)を減らす費用。律速は自己資本(自給率 0.34)',
    '差は縮小中: 1.93pt(Q4 2024)→ 1.56pt(Q2 2026)。\n預金コストは政策金利より約 0.8pt 低いだけ',
  ], { x: 6.78, y: 4.68, w: 6.05, h: 1.4, fontSize: 9.5, gap: 3, name: 'bul_read' });

  // ---- 下: takeaway(横長) ----
  L.takeaway(s, 0.5, 6.15, 12.33, 0.6, '組み合わせは希少で、負債の安さは本物。ただし株主資本はテック並みに高く、差は縮小中で、部品は買える →\nG8 は B、条件11 は B(A との境界)。資金の優位は NIM に既に入っており、理論株価に別建てで足さない', { fontSize: 10.5 });
  return s;
};
