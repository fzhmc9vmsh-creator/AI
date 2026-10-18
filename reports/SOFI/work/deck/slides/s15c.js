// 獲得投資の裁量性(指示書 spec/v2.md の s15c 節。手本 s14(表 + チャート)と s12・s13 の型)
// 左: 純増 1 件当たりの販促費の折れ線(新規会員の製品当たりは 2024 年 Q1〜Q3 が欠測のため線を切る)
// 右: 6 つの検査の表と、EPS への効きの表
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 純増 1 件当たりの販促費(ドル、販促費 ÷ 純増。ローンのリード費・既存会員向けの特典を含むため上限寄り)。右: 6 つの検査と EPS への効き',
    source: 'research_r3/R10_growth_engine_cac.md(10-Q・8-K の要約)、calc/out/growth_v2.json',
  });

  // 左: 折れ線(3 系列。null は線を切る)
  L.paneHead(s, 0.5, 1.62, 6.3, '純増 1 件当たりの販促費(ドル)');
  const labels = ['Q1 24', 'Q2 24', 'Q3 24', 'Q4 24', 'Q1 25', 'Q2 25', 'Q3 25', 'Q4 25', 'Q1 26', 'Q2 26'];
  s.addChart(pres.charts.LINE, [
    { name: '会員当たり', labels, values: [269, 287, 284, 292, 298, 311, 317, 306, 305, 357] },
    { name: '製品当たり', labels, values: [169, 195, 195, 208, 198, 210, 205, 191, 186, 178] },
    { name: '新規会員の製品当たり', labels, values: [null, null, null, 311, 310, 323, 342, 318, 327, 364] },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 6.3, h: 3.25, objectName: 'chart',
    showLegend: true, legendPos: 'b', showValue: false, displayBlanksAs: 'gap',
    chartColors: [C.red, C.primary, C.amber], lineSize: 2, lineDataSymbolSize: 6,
    valAxisMinVal: 0, valAxisMaxVal: 400, valAxisMajorUnit: 100, valAxisLabelFormatCode: '0',
  }));
  L.text(s, 'Q2 2026: 会員当たり 357 ドル(前期比 +17%)、製品当たり 178 ドル(前年比 −15%)。\n製品の純増 220 万件の 51% は既存会員が開いた(獲得費がほぼかからない)', { x: 0.5, y: 5.3, w: 6.3, h: 0.5, fontSize: 9, objectName: 'note_q2' });
  L.takeaway(s, 0.5, 5.9, 6.3, 0.75, '販促は攻めの再投資で、EPS は必要なら上げられる。\nただし Q2 は会員当たりの効率が悪化した(前期比 +17%)');

  // 右上: 6 つの検査の表。判定は「攻め」を緑のセル、ほかは太字の文字
  L.paneHead(s, 7.05, 1.62, 5.78, '6 つの検査(攻めか、必要に迫られた支出か)');
  const judge = (k) => k === '攻め'
    ? { text: k, options: { fill: { color: L.GRADE.A.fill }, color: L.GRADE.A.font, bold: true, align: 'center' } }
    : { text: k, options: { color: C.dark, bold: true, align: 'center' } };
  L.table(s, [
    ['検査', 'SoFi の材料', '判定'],
    ['限界 CAC', '製品当たり −15%、会員当たり +15%', judge('混合')],
    ['解約・休眠', '非開示', judge('保留')],
    ['価格', '普通預金 3.30% を利上げ後も据え置き', judge('攻め')],
    ['競合', '販促費 +48%\n(Chime +25%、Robinhood の営業費用 +33%)', judge('攻め')],
    ['経営の運用', '売上計画を上げ、EBITDA 計画は据え置き(再投資)', judge('攻め')],
    ['有機的な獲得', '認知度 10.4%、クロスバイ 51%', judge('攻め')],
  ], { x: 7.05, y: 1.98, w: 5.78, colW: [1.35, 3.6, 0.83], fontSize: 10, rowH: 0.36, align: ['left', 'left', 'center'] });

  // 右下: EPS への効き(見出し行なし。値の列を太字)
  L.paneHead(s, 7.05, 4.72, 5.78, 'EPS への効き(経営が出し入れできる部分)');
  const eps = [
    ['販促費率 1pt', 'EPS 0.027 ドル'],
    ['維持水準(16%)なら 2026 年 EPS', '1.04 ドル(13〜19% で 0.95〜1.12)'],
    ['2026 年の再投資(売上計画の上振れ分)', 'EPS 0.08 ドル相当'],
    ['EPS 成長(2026→29)のうち\n販促費率の低下による部分', '約 30%(32% 据え置きなら\n2029 年 1.13、エンジン 1.35)'],
  ];
  L.table(s, eps.map((r, i) => r.map((t, j) => ({ text: t, options: { fill: { color: i % 2 === 0 ? C.gray : C.white }, color: C.text, bold: j === 1 } }))),
    { x: 7.05, y: 5.08, w: 5.78, colW: [2.9, 2.88], fontSize: 10, rowH: 0.34, align: ['left', 'left'] });
};
