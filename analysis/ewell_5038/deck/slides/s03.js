// 目次: 流れの矢印 + 並びの理由 + 章の表
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, { kicker: '', source: '本資料の構成' });
  const steps = ['前提', '変化', '持続', '5年後', '人', '価格'];
  const w = 1.7, gap = 0.4, x0 = 0.5 + (12.33 - (6 * w + 5 * gap)) / 2;
  steps.forEach((t, i) => {
    const x = x0 + i * (w + gap);
    L.box(s, x, 1.68, w, 0.42, { fill: i === 5 ? C.dark : C.tint, line: i === 5 ? C.dark : C.light, round: true, name: 'ovl_step' + i });
    L.text(s, t, { x, y: 1.68, w, h: 0.42, fontSize: 11, bold: true, color: i === 5 ? C.white : C.dark, align: 'center', valign: 'middle', margin: 0, objectName: 'step_t' + i });
    if (i < 5) L.arrow(s, x + w + 0.04, 1.89, x + w + gap - 0.04, 1.89);
  });
  L.text(s, '並びの理由: 株価との差の正体(倍率)を先に示し、事業の分解で倍率を支える根拠が弱いことを確かめる', { x: 0.5, y: 2.2, w: 12.33, h: 0.3, fontSize: 10.5, color: C.dark, bold: true, margin: 0, objectName: 'reason' });
  L.table(s, [
    ['章', '問い', '答え', '決め手の数字', 'ページ'],
    ['1 結論', '今買うべきか', '見送り。価格が質を払っている', '理論株価1,657.5円', '2-4'],
    ['2 事業の前提', '何をしている会社か。業界・最新決算・どこで稼ぐか', '訪問看護の電子カルテ。1訪問8,500円のうち約136円を取る', '3Q 売上+24.0%', '5-9'],
    ['3 変化', '何が変わったか', '単価の伸びはアップセル、本体は横ばい', '+0.1千円', '10-11'],
    ['4 持続と段差', 'なぜ続き、次の段差はいつか', '流出は少ないが獲得は開設に縛られる', '2.7倍・2,450件', '12-14'],
    ['5 5年後', '損益とROEは', 'EPS156.5円、ROEは現金で薄まる', '7,191百万円', '15-16'],
    ['6 経営', '誰が実行するか', '創業者。統治に留保', '社外1/4名', '17'],
    ['7 価値', '市場は何を前提にし、いくらで、いつ', '資本コスト約7.5%、見送り', '1,468円', '18-21'],
  ], { x: 0.5, y: 2.65, w: 12.33, colW: [1.7, 3.0, 4.2, 2.43, 1.0], fontSize: 10.5, rowH: 0.5, align: ['left', 'left', 'left', 'center', 'center'], name: 'tbl_toc' });
};
