// 目次: 読む順の 1 行 → 章の表(章 | 問い | この資料の答え | 決め手の数字 | ページ)
module.exports = function build(pres, L) {
  const { C, F, M } = L;
  const s = L.contentSlide(pres, {});
  // 章の流れ(矢印つきの箱 5 つ)
  const steps = ['事実(2・3章)', '予測(4章)', '不確実性(5章)', '値段(6章)', '判定(7章)'];
  const bw = 2.05, gap = (12.33 - steps.length * bw) / (steps.length - 1);
  steps.forEach((t, i) => {
    const x = M + i * (bw + gap), last = i === steps.length - 1;
    L.box(s, x, 1.66, bw, 0.42, { round: true, fill: last ? C.dark : C.tint, line: last ? C.dark : C.tint, name: 'flow_box' + i });
    L.text(s, t, { x, y: 1.66, w: bw, h: 0.42, fontSize: 11, bold: true, color: last ? C.white : C.dark, align: 'center', valign: 'middle', margin: 0, objectName: 'flow_t' + i });
    if (i < steps.length - 1) L.arrow(s, x + bw + 0.06, 1.87, x + bw + gap - 0.06, 1.87, { color: C.primary, width: 1.5 });
  });
  const rows = [
    ['章', '問い', 'この資料の答え', '決め手の数字', 'ページ'],
    ['1 結論', L.MT.CH[0].q, `見送り。現金は黒字に転じたが、適正株価は${F('fair')}。${F('entry')}以下か2027年8月の決算を待つ`, `適正株価 ${F('fair')}`, 'p.2–3'],
    ['2 会社と業界の前提', L.MT.CH[1].q, `企業にAIモデルを従量課金で貸す会社で、モデル開発の位置から売上の${F('csp.share')}をクラウド事業者経由で得る`, `年換算売上 ${F('arr.oct')} 百万ドル`, 'p.4–6'],
    ['3 現在の構造', L.MT.CH[2].q, `柱はAPIで実質の粗利率${F('gm.real')}。営業の現金は黒字だが、支払い義務${F('oblig')} 百万ドルが先行する投資先行型`, `実質の粗利率 ${F('gm.real')}`, 'p.7–11'],
    ['4 将来の構造', L.MT.CH[3].q, '計画どおりなら2031年の1株利益は3.85ドルで、現金は回収の側に移る。最大の源の研究開発費率の低下は確度が中', `2031年の1株利益 ${F('eps.2031', { noEst: true })}`, 'p.12–16'],
    ['5 リスク', L.MT.CH[4].q, '期待損失の最大は需要の減速で支払い義務が遊休になる筋(確率20%・−93%)。次が実質の粗利率の8pt低下', `確率 ${F('risk.demand.p')}・下落 ${F('risk.demand.imp')}`, 'p.17–18'],
    ['6 今の値段', L.MT.CH[5].q, `PER ${F('per.78')}。1株利益が年${F('g.2027', { noEst: true })}で伸び続ける計画の満額実現を前提にしている`, `PER ${F('per.78')}`, 'p.19–20'],
    ['7 判定と行動', L.MT.CH[6].q, `成長に対する値段は${F('peg.78')}で、許容の${F('peg.allow')}を上回る。適正株価は${F('fair')}。${F('entry')}以下か2027年8月の実質の粗利率${F('kpi.gm')}以上で買う`, `成長に対する値段 ${F('peg.78')}`, 'p.21–25'],
  ];
  L.table(s, rows, { x: M, y: 2.3, w: 12.33, colW: [2.0, 3.0, 4.6, 2.0, 0.73], fontSize: 10, rowH: 0.5, align: ['left', 'left', 'left', 'left', 'center'], name: 'toc_tbl' });
  L.text(s, '将来の章(4章)の数字は当分析モデルの推定', { x: M, y: 6.5, w: 8, h: 0.22, fontSize: 8.5, color: C.sub, margin: 0, objectName: 'toc_note' });
};
