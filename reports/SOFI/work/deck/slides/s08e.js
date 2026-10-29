// 2-2 会社のシナリオ(2/2): 部品の採点(手本を写経。タイトル・ページ番号は meta.js が入れる)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 筋書きの部品(P1〜P10)を、数字で作動しているかで採点。右: 規模で重みづけした判定と、会社目標・コンセンサス・事業エンジンの差',
    source: '会社開示(Q4 2025〜Q3 2026 決算の 8-K・説明会の要約)、research_r5/Q3_datasheet.md、research/R3b_management.md、calc/out/growth_v4.json',
  });

  // 評価の色: + は濃緑太字、± は琥珀太字、− は赤太字、保留は灰
  const ev = (t) => {
    if (t === '+') return { text: t, options: { color: C.primary, bold: true } };
    if (t === '±') return { text: t, options: { color: C.amber, bold: true } };
    if (t === '−') return { text: t, options: { color: C.red, bold: true } };
    return { text: t, options: { color: C.sub } };
  };

  // 左: 部品の採点表
  L.table(s, [
    ['#', '部品', '評価', '進捗(数字で作動しているか)', '重み'],
    ['P1', '会員の獲得(ブランド・販促)', ev('+'), '作動。純増 120 万/四半期(過去最高)', '20%'],
    ['P2', 'クロスバイ', ev('+'), '作動(51%)。新製品の過半は既存会員', '10%'],
    ['P3', '預金による調達', ev('+'), '作動。513 億ドル、倉庫ライン比 −1.45pt', '20%'],
    ['P4', 'B/S 貸出の拡大', ev('+'), '作動。NII +59%、NIM 6.14%', '20%'],
    ['P5', 'LPB(手数料型)', ev('±'), '横ばい。36 億ドル、割合 29%', '10%'],
    ['P6', '学生ローン(Grad PLUS)', ev('+'), '作動。組成 +96%', '5%'],
    ['P7', '手数料型(交換・組成・Plus)', ev('+'), '作動。手数料型 +40%(42%)', '5%'],
    ['P8', 'Tech Platform(Galileo)', ev('±'), '底打ち → 再成長の入口。大口を除き +18%', '5%'],
    ['P9', '新領域(SoFiUSD ほか)', ev('保留'), '数字なし(流通額は未開示)', '3%'],
    ['P10', '販促費の効率', ev('±'), '一部。会員当たり 370 ドル', '2%'],
  ], {
    x: 0.5, y: 1.62, w: 8.3, colW: [0.5, 2.0, 0.8, 4.1, 0.9], fontSize: 8.5, rowH: 0.38,
    align: ['center', 'left', 'center', 'left', 'center'],
  });

  // 右上: 規模で重みづけした判定(100% 積み上げの横棒 1 本、4 系列)
  L.paneHead(s, 9.05, 1.62, 3.78, '規模で重みづけした判定');
  s.addChart(pres.charts.BAR, [
    { name: '作動している +', labels: ['重み'], values: [80] },
    { name: '両面・停滞', labels: ['重み'], values: [17] },
    { name: '逆行 −', labels: ['重み'], values: [0] },
    { name: '保留', labels: ['重み'], values: [3] },
  ], L.chartStyle({
    x: 9.05, y: 1.95, w: 3.78, h: 1.15, barDir: 'bar', barGrouping: 'percentStacked',
    chartColors: [C.primary, C.amber, C.red, C.sub], showLegend: true, legendPos: 'b',
    // 4% 未満の細い区間(保留 3%)はラベルを出さず、表の P9 で読む(5% と 3% のラベルが重なるため)
    dataLabelPosition: 'ctr', dataLabelColor: 'FFFFFF', dataLabelFormatCode: '[>=4]0"%";""',
    catAxisHidden: true, valAxisHidden: true, valGridLine: { style: 'none' }, objectName: 'chart_weight',
  }));
  L.takeaway(s, 9.05, 3.2, 3.78, 0.95, '判定は「プラス(資本の弁が条件)」。作動している部品の多くが資本を使い、資本の上限が筋書きの速さを決める');

  // 右下: 会社の目標をどこまで信じるか(2027・2028 年)
  L.paneHead(s, 9.05, 4.3, 3.78, '会社の目標をどこまで信じるか');
  L.table(s, [
    ['', '会社', 'コンセンサス', 'エンジン'],
    ['EPS 2027', '0.90', '0.82(決算前)', '0.90'],
    ['EPS 2028', '1.02〜1.12', '1.06(決算前)', '1.15'],
    ['ROTCE 2028', '20〜30%\n(長期)', '—', '13.1%'],
  ], { x: 9.05, y: 4.65, w: 3.78, colW: [1.06, 0.9, 0.91, 0.91], fontSize: 8.5, rowH: 0.32 });
  L.text(s, 'EPS の目標はエンジンでも届く。ROTCE の目標には\n届かず、成長が生む価値は小さい。理論株価は\nエンジンの EPS を土台にした', {
    x: 9.05, y: 6.2, w: 3.78, h: 0.5, fontSize: 8.5,
  });
};
