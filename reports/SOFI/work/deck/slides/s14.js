// 根幹 KPI の率(指示書 spec/v3.md の s14 節。作り直し。手本: 既存の s14 の表 + 右チャートの配置、折れ線は s15c の作り)
// 型: 左上に KPI の四半期表(判定の行つき)、左下に FS の前年比の分解、右にチャートと結論
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '伸びを率で読む: 前期比(年率換算)・前年比・率の推移・純増の前年比。判定の言葉は前年比の率の推移で決める(3 期 ±2pt 以内 = 維持)',
    source: '会社開示(Q2 2025〜Q2 2026)、research/R1b_kpi.md、research_r4/R16、calc/out/growth_v3.json の kpi',
  });

  // 左上: 四半期の KPI 表。判定の行: 維持は灰、加速・上昇は緑の太字
  const grey = (t) => ({ text: t, options: { color: C.sub } });
  const green = (t) => ({ text: t, options: { color: C.primary, bold: true } });
  L.table(s, [
    ['四半期', '会員\n前期比(年率)', '会員\n前年比', '会員純増\n前年比', '製品\n前年比', '製品純増\n前年比', '会員当たり\n製品', '預金\n前年比', '収益\n前年比'],
    ['Q2 25', '+7.3%(32.8%)', '+33.4%', '+32%', '+33.6%', '+33%', '1.46', '—', '—'],
    ['Q3 25', '+7.7%(34.5%)', '+34.5%', '+20%', '+35.8%', '+27%', '1.48', '—', '+39.5%'],
    ['Q4 25', '+8.7%(39.8%)', '+35.2%', '+27%', '+37.4%', '+45%', '1.47', '+44.2%', '+37.1%'],
    ['Q1 26', '+7.3%(32.6%)', '+34.9%', '+38%', '+39.2%', '+50%', '1.50', '+47.3%', '+41.1%'],
    ['Q2 26', '+7.5%(33.5%)', '+35.0%', '+29%', '+42.7%', '+75%', '1.54', '+54.2%', '+40.5%'],
    // 判定の行: 維持は灰、加速・上昇は緑の太字
    [{ text: '判定', options: { bold: true } }, '—', grey('高水準で維持'), '—', green('加速'), '—', green('上昇'), green('加速'), grey('加速の後に維持')],
  ], { x: 0.5, y: 1.62, w: 8.3, colW: [0.7, 1.0, 0.95, 0.85, 0.8, 0.85, 0.9, 0.8, 1.45], fontSize: 9, rowH: 0.36 });

  // 左下: FS の前年比の分解(Q2 2026)
  L.text(s, 'FS の前年比の分解(Q2 2026)', { x: 0.5, y: 4.45, w: 5.6, h: 0.28, fontSize: 9.5, bold: true, color: C.dark, valign: 'middle', objectName: 'sub_head' });
  L.table(s, [
    ['FS の内訳', '前年比'],
    ['FS 合計', '+29%'],
    ['うち NII', '+29%'],
    ['うち LPB の手数料', '+11%'],
    ['うち その他の手数料(交換手数料・証券・Plus)', '+83%'],
    ['LPB を除く FS', '+38%'],
    ['Lending(貸出)', '+59%'],
  ], { x: 0.5, y: 4.75, w: 5.6, colW: [4.1, 1.5], fontSize: 9, rowH: 0.27 });

  // 右: 前年比の推移(折れ線 2 系列)。値の重なりを避けて数値ラベルは出さず、同じ値を左の表で読む
  L.paneHead(s, 9.05, 1.62, 3.78, '前年比の推移(%)');
  s.addChart(pres.charts.LINE, [
    { name: '会員', labels: ['Q2 25', 'Q3 25', 'Q4 25', 'Q1 26', 'Q2 26'], values: [33.4, 34.5, 35.2, 34.9, 35.0] },
    { name: '製品', labels: ['Q2 25', 'Q3 25', 'Q4 25', 'Q1 26', 'Q2 26'], values: [33.6, 35.8, 37.4, 39.2, 42.7] },
  ], L.chartStyle({
    x: 9.05, y: 1.98, w: 3.78, h: 3.0, objectName: 'chart',
    showValue: false, showLegend: true, legendPos: 'b', chartColors: [C.primary, C.teal], lineSize: 2, lineDataSymbolSize: 6,
    valAxisMinVal: 30, valAxisMaxVal: 45, valAxisMajorUnit: 5, valAxisLabelFormatCode: '0',
  }));
  L.takeaway(s, 9.05, 5.1, 3.78, 1.55, '会員の純増が 2 期続けて 110 万人でも、\n前年比 35% を維持(母数の効果)。\n製品は加速 → 収益化が進む。\nFS の伸びの低下は LPB からの配分替え');
};
