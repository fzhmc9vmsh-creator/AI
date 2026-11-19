// s19 株価の前提: 78 ドルに要る成長(横棒)と計画の成長、見るところ、用語の注釈(PER・PEG)
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, { source: '当分析(公開価格 ÷ 2027 年の 1 株利益)' });

  L.text(s, '78 ドル ÷ 2027 年の 1 株利益 1.08 ドル = PER 72 倍', {
    x: 0.5, y: 1.62, w: 12.33, h: 0.34, fontSize: 12, bold: true, color: C.dark, valign: 'middle', margin: 0, objectName: 'formula',
  });

  const labels = [
    'PEG 1.0 で 78 ドルに要る伸び',
    '許容 PEG で要る伸び',
    '2 章の 1 株利益の伸び(2027 年から)',
    '2 章の 1 株利益の伸び(2030 年から)',
  ];
  // 色を棒ごとに変えるため、赤・濃緑・灰の系列に分けて積み上げる(他の系列は 0 にして、ラベルは 0 を隠す)
  s.addChart(pres.charts.BAR, [
    { name: '要る伸び', labels, values: [72, 58, 0, 0] },
    { name: '計画の伸び(2027 年から)', labels, values: [0, 0, 43.1, 0] },
    { name: '計画の伸び(2030 年から)', labels, values: [0, 0, 0, 19.6] },
  ], L.chartStyle({
    x: 0.5, y: 2.05, w: 8.2, h: 3.25,
    barDir: 'bar', barGrouping: 'stacked', catAxisOrientation: 'maxMin',
    valAxisMinVal: 0, valAxisMaxVal: 80, valAxisMajorUnit: 20, valAxisLabelFormatCode: '0"%"',
    dataLabelFormatCode: '0.0"%";;', dataLabelPosition: 'ctr', dataLabelColor: C.white,
    barGapWidthPct: 60,
    chartColors: [C.red, C.dark, C.sub],
    objectName: 'chart_growth',
  }));

  L.lookBox(s, [
    { text: '78 ドルを正当化するには年 58〜72% の伸びが要る' },
    { text: '2 章の計画の伸びは 43.1% から 19.6% へ減速' },
    { text: '差は、計画の満額実現(会社の最善の筋 77.9 ドル相当)を前提にした分' },
  ], { x: 8.85, y: 2.05, w: 3.98, h: 3.25, name: 'look' });

  L.takeaway(s, 0.5, 5.5, 12.33, 0.62, `公開価格は PER ${F('per.78')}。要る伸び ${F('ig.allow')} に対し、計画の伸びは ${F('g.2027', { noEst: true })}`);

  L.termNotes(s, [
    { term: 'PER', plain: '株価 ÷ EPS。利益の何年分の値段か', why: '今の株価が前提にする成長を逆算するため' },
    { term: 'PEG', plain: 'PER ÷ EPSの成長率(%)。1倍なら成長に見合う値段', why: '成長の速さに対して値段が高いかを見るため' },
  ], { x: 0.5, y: 6.3, w: 12.33 });
};
