// 獲得投資の裁量性。型: 左に純増 1 件当たりの販促費の折れ線、右に 6 つの検査と EPS への効きの表
// 系列の出所: 2024 年 Q1〜2026 年 Q2 は research_r3/R10、2026 年 Q3 は research_r5/Q3_datasheet
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 純増 1 件当たりの販促費(ドル、販促費 ÷ 純増。ローンのリード費・既存会員向けの特典を含むため上限寄り)。右: 6 つの検査と EPS への効き',
    source: 'research_r5/Q3_datasheet.md(Q3 の 8-K・説明会の要約)、research_r3/R10_growth_engine_cac.md(Q1 2024〜Q2 2026 の系列)、calc/out/growth_v4.json',
  });

  // 左: 折れ線(3 系列。null は線を切る)
  L.paneHead(s, 0.5, 1.62, 6.3, '純増 1 件当たりの販促費(ドル)');
  const labels = ['Q1 24', 'Q2 24', 'Q3 24', 'Q4 24', 'Q1 25', 'Q2 25', 'Q3 25', 'Q4 25', 'Q1 26', 'Q2 26', 'Q3 26'];
  s.addChart(pres.charts.LINE, [
    { name: '会員当たり', labels, values: [269, 287, 284, 292, 298, 311, 317, 306, 305, 357, 370] },
    { name: '製品当たり', labels, values: [169, 195, 195, 208, 198, 210, 205, 191, 186, 178, 202] },
    { name: '新規会員の製品当たり', labels, values: [null, null, null, 311, 310, 323, 342, 318, 327, 364, null] },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 6.3, h: 3.25, objectName: 'chart',
    showLegend: true, legendPos: 'b', showValue: false, displayBlanksAs: 'gap',
    chartColors: [C.red, C.primary, C.amber], lineSize: 2, lineDataSymbolSize: 6,
    valAxisMinVal: 0, valAxisMaxVal: 400, valAxisMajorUnit: 100, valAxisLabelFormatCode: '0',
  }));
  L.text(s, 'Q3 2026: 会員当たり 370 ドル(前期比 +4%)、製品当たり 202 ドル(前期比 +13%)。\n新規会員の製品当たりは Q3 未開示。\n製品の純増 220 万件の 51% は既存会員が開いた(獲得費がほぼかからない)', { x: 0.5, y: 5.3, w: 6.3, h: 0.5, fontSize: 9, objectName: 'note_q2' });
  L.takeaway(s, 0.5, 5.9, 6.3, 0.75, '販促費は攻めのまま増やし、増収で EPS を作った。EPS の調整弁は\n販促費ではなく B/S の伸び(資本)。2027 年は資本の上限が効く');

  // 右上: 6 つの検査の表。判定は「攻め」を緑のセル、ほかは太字の文字
  L.paneHead(s, 7.05, 1.62, 5.78, '6 つの検査(攻めか、必要に迫られた支出か)');
  const judge = (k) => k === '攻め'
    ? { text: k, options: { fill: { color: L.GRADE.A.fill }, color: L.GRADE.A.font, bold: true, align: 'center' } }
    : { text: k, options: { color: C.dark, bold: true, align: 'center' } };
  L.table(s, [
    ['検査', 'SoFi の材料', '判定'],
    ['限界 CAC', '会員当たり +4%(357 → 370)、製品当たり +13%', judge('混合')],
    ['解約・休眠', '非開示', judge('保留')],
    ['価格', '基本金利 3.30% 据え置き、新規は上乗せ +1.10%\n(新規の獲得に金利を使い始めた)', judge('攻め')],
    ['競合', '販促費 +55%\n(Chime +25%、Robinhood の営業費用 +33%)', judge('攻め')],
    ['経営の運用', '売上計画を上げ、EBITDA 率は\n33〜34% → 32.9%(再投資)', judge('攻め')],
    ['有機的な獲得', '認知度 10.4%(Q2)、クロスバイ 51%', judge('攻め')],
  ], { x: 7.05, y: 1.98, w: 5.78, colW: [1.35, 3.6, 0.83], fontSize: 10, rowH: 0.36, align: ['left', 'left', 'center'] });

  // 右下: EPS への効き(見出し行なし。値の列を太字)
  L.paneHead(s, 7.05, 4.72, 5.78, 'EPS への効き(経営が出し入れできる部分)');
  const eps = [
    ['販促費率 1pt', 'EPS 約 0.028 ドル\n(2026 年の収益 50.4 億)'],
    ['Q3 の実績', '販促費 +0.52 億ドルでも\nEPS +0.06(増収で)'],
    ['2027 年見通し', '販促費率を大きく下げずに EPS 0.90'],
  ];
  L.table(s, eps.map((r, i) => r.map((t, j) => ({ text: t, options: { fill: { color: i % 2 === 0 ? C.gray : C.white }, color: C.text, bold: j === 1 } }))),
    { x: 7.05, y: 5.08, w: 5.78, colW: [2.9, 2.88], fontSize: 10, rowH: [0.46, 0.34, 0.34], align: ['left', 'left'] });
};
