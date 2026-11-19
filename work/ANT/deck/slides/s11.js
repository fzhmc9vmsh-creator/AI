// s11 強さと弱さ: 法人 API のシェア・開発者の採用率(横棒)、売上の構成の帯、見るところ
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, { source: 'Menlo Ventures(2026)、JetBrains 調査(2026)、S-1/A-3' });

  L.paneHead(s, 0.5, 1.62, 7.6, '法人 API のシェアと開発者の採用率(%)', 'pane_share_head');
  const labels = [
    'Anthropic(法人 API のシェア)',
    'OpenAI(法人 API のシェア)',
    'Google(法人 API のシェア)',
    'Claude Code(開発者の採用率)',
  ];
  // 色を棒ごとに変えるため、濃緑の系列と灰の系列に分けて積み上げる(片方は 0 にして、ラベルは 0 を隠す)
  s.addChart(pres.charts.BAR, [
    { name: '自社', labels, values: [40, 0, 0, 39] },
    { name: '競合', labels, values: [0, 27, 21, 0] },
  ], L.chartStyle({
    x: 0.5, y: 1.98, w: 7.6, h: 2.3,
    barDir: 'bar', barGrouping: 'stacked', catAxisOrientation: 'maxMin',
    valAxisMinVal: 0, valAxisMaxVal: 50, valAxisHidden: true, valGridLine: { style: 'none' },
    dataLabelFormatCode: '0"%";;', dataLabelPosition: 'ctr', dataLabelColor: C.white,
    barGapWidthPct: 60,
    chartColors: [C.dark, C.sub],
    objectName: 'chart_share',
  }));

  L.paneHead(s, 0.5, 4.45, 7.6, '売上の構成(%)', 'pane_band_head');
  const bw = 7.6, big = 0.74;
  L.box(s, 0.5, 4.85, bw * big, 0.5, { fill: C.dark, line: C.dark, name: 'ovl_band_big' });
  L.text(s, '年 10 万ドル以上の 11,900 社 74%', { x: 0.5, y: 4.85, w: bw * big, h: 0.5, fontSize: 10.5, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0, objectName: 'band_big' });
  L.box(s, 0.5 + bw * big, 4.85, bw * (1 - big), 0.5, { fill: C.rule, line: C.rule, name: 'ovl_band_rest' });
  L.text(s, 'その他 26%', { x: 0.5 + bw * big, y: 4.85, w: bw * (1 - big), h: 0.5, fontSize: 10.5, color: C.text, align: 'center', valign: 'middle', margin: 0, objectName: 'band_rest' });

  L.text(s, '比較対象: OpenAI(同じ法人 API を売る最大の競合、非上場)、Google(Gemini を自社クラウドで売る競合)。Meta はモデルを無償公開し API で競わないため外した', {
    x: 0.5, y: 5.55, w: 7.6, h: 0.5, fontSize: 9, color: C.sub, margin: 0, valign: 'top', objectName: 'note_compare',
  });

  L.lookBox(s, [
    { text: '首位の理由は安全性と開発ツールへの組み込み' },
    { text: 'OpenAI は ChatGPT と API を提供する最大の競合、Google は自社クラウドで売る競合' },
    { text: '上位への集中が弱さ(1 社の減速の影響が大きい)' },
  ], { x: 8.4, y: 1.98, w: 4.43, h: 3.8, name: 'look' });
};
