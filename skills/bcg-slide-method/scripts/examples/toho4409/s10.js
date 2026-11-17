// s10 営業利益の積み上げ(作り直し)
const M = require('../data/fwd_v3.json');

module.exports = function build(pres, L) {
  const { F, C } = L;
  const s = L.contentSlide(pres, {
    source: '決算短信(2026年3月期・2027年3月期第2四半期)のセグメント情報、中期経営計画 p.10〜14。31/3期は本分析の5年後モデル(model/fwd_v3.py)',
  });

  const B31 = M.scenarios['基準'][4];

  // ----------------------------------------------------
  // 左ペイン: 営業利益の積み上げ(ウォーターフォール)
  // ----------------------------------------------------
  L.paneHead(s, 0.5, 1.62, 8.2, '営業利益の積み上げ(百万円): 26/3期実績 → 31/3期 基準、セグメント別');

  // ウォーターフォール棒データ
  // 1. 26/3期 実績: F.v('fy26.op')
  // 2. SC: M.scenarios['基準'][4].sc - F.v('fy26.seg_spec_profit')
  // 3. 界面活性剤: B31.surf - F.v('fy26.seg_surf_profit')
  // 4. 樹脂: B31.resin - F.v('fy26.seg_resin_profit')
  // 5. 化成品: B31.chem - F.v('fy26.seg_chem_profit')
  // 6. 調整額: -F.v('calc.seg_adj_fy26')
  // 7. 31/3期 基準: B31.op
  // 比較の棒:
  // 8. 中計目標: F.v('mp.fy31_op')
  // 9. 弱気: M.scenarios['弱気'][4].op
  // 10. 強気: M.scenarios['強気'][4].op

  const v26 = F.v('fy26.op');
  const dSC = B31.sc - F.v('fy26.seg_spec_profit');
  const dSurf = B31.surf - F.v('fy26.seg_surf_profit');
  const dResin = B31.resin - F.v('fy26.seg_resin_profit');
  const dChem = B31.chem - F.v('fy26.seg_chem_profit');
  const dAdj = -F.v('calc.seg_adj_fy26');
  const v31Base = B31.op;
  const vTarget = F.v('mp.fy31_op');
  const vBear = M.scenarios['弱気'][4].op;
  const vBull = M.scenarios['強気'][4].op;

  // 描画域 y2.1〜5.4、尺度は最大値(強気)で決める
  const maxVal = vBull; // 5062
  const baselineY = 5.08;
  const plotH = 2.65; // 強気の棒の高さ
  const scale = plotH / maxVal;

  const barW = 0.52;
  const gapWF = 0.16;
  const xStart = 0.55;

  // 各棒の定義
  // type: 'base' (0からスタート) | 'flow' (前回のトップから) | 'compare' (0からスタート)
  const wfBars = [
    { label: '26/3期\n実績', val: v26, disp: F.n('fy26.op'), bottom: 0, top: v26, fill: C.dark, line: C.dark },
    { label: 'SC', val: dSC, disp: `+${dSC.toLocaleString('en-US')}`, bottom: v26, top: v26 + dSC, fill: C.primary, line: C.primary },
    { label: '界面\n活性剤', val: dSurf, disp: `+${dSurf.toLocaleString('en-US')}`, bottom: v26 + dSC, top: v26 + dSC + dSurf, fill: C.sub, line: C.sub },
    { label: '樹脂', val: dResin, disp: `+${dResin.toLocaleString('en-US')}`, bottom: v26 + dSC + dSurf, top: v26 + dSC + dSurf + dResin, fill: C.gray, line: C.rule },
    { label: '化成品', val: dChem, disp: `+${dChem.toLocaleString('en-US')}`, bottom: v26 + dSC + dSurf + dResin, top: v26 + dSC + dSurf + dResin + dChem, fill: C.gray, line: C.rule },
    { label: '調整額', val: dAdj, disp: `${dAdj.toLocaleString('en-US')}`, bottom: v26 + dSC + dSurf + dResin + dChem + dAdj, top: v26 + dSC + dSurf + dResin + dChem, fill: C.rule, line: C.sub },
    { label: '31/3期\n基準', val: v31Base, disp: v31Base.toLocaleString('en-US'), bottom: 0, top: v31Base, fill: C.dark, line: C.dark },
  ];

  const compareBars = [
    { label: '中計\n目標', val: vTarget, disp: F.n('mp.fy31_op'), bottom: 0, top: vTarget, fill: C.white, line: C.dark, dash: 'dash' },
    { label: '弱気', val: vBear, disp: vBear.toLocaleString('en-US'), bottom: 0, top: vBear, fill: C.gray, line: C.rule },
    { label: '強気', val: vBull, disp: vBull.toLocaleString('en-US'), bottom: 0, top: vBull, fill: C.gray, line: C.rule },
  ];

  // ベースライン (x軸線)
  s.addShape('line', {
    x: xStart,
    y: baselineY,
    w: 7.45,
    h: 0,
    line: { color: C.rule, width: 1.0 },
    objectName: 'ovl_baseline',
  });

  // ウォーターフォール棒の描画
  let curX = xStart;
  wfBars.forEach((b, i) => {
    const barH = (b.top - b.bottom) * scale;
    const barY = baselineY - b.top * scale;

    L.box(s, curX, barY, barW, Math.max(barH, 0.02), {
      fill: b.fill,
      line: b.line,
      lw: 0.75,
      name: `ovl_wf_bar_${i}`,
    });

    // 棒の上に数字
    L.text(s, b.disp, {
      x: curX - 0.1,
      y: barY - 0.22,
      w: barW + 0.2,
      h: 0.2,
      fontSize: 8.5,
      bold: true,
      color: C.text,
      align: 'center',
      valign: 'bottom',
      margin: 0,
      objectName: `ovl_wf_num_${i}`,
    });

    // x軸ラベル
    L.text(s, b.label, {
      x: curX - 0.1,
      y: baselineY + 0.06,
      w: barW + 0.2,
      h: 0.34,
      fontSize: 8.5,
      color: C.text,
      align: 'center',
      valign: 'top',
      margin: 0,
      objectName: `ovl_wf_lbl_${i}`,
    });

    // 次の棒への接続点線
    if (i < wfBars.length - 1 && i > 0 && i < 6) {
      const nextY = baselineY - (b.val < 0 ? b.bottom : b.top) * scale;
      s.addShape('line', {
        x: curX + barW,
        y: nextY,
        w: gapWF,
        h: 0,
        line: { color: C.rule, width: 0.75, dashType: 'dash' },
        objectName: `ovl_wf_conn_${i}`,
      });
    }

    curX += barW + gapWF;
  });

  // 基準の棒と中計目標の棒の間の間隔
  const gapSep = 0.75;
  const noteX = curX - gapWF; // 基準棒の右端
  curX = curX - gapWF + gapSep;

  // 差の注記: 基準と中計目標の間
  L.text(s, `差 ${F.n('calc.op_gap_target')}`, {
    x: noteX,
    y: 2.72,
    w: gapSep,
    h: 0.3,
    fontSize: 8.5,
    bold: true,
    color: C.primary,
    align: 'center',
    valign: 'middle',
    margin: 0,
    objectName: 'ovl_gap_note',
  });

  // 比較の棒の描画
  const gapComp = 0.22;
  compareBars.forEach((b, i) => {
    const barH = (b.top - b.bottom) * scale;
    const barY = baselineY - b.top * scale;

    s.addShape('rect', {
      x: curX,
      y: barY,
      w: barW,
      h: Math.max(barH, 0.02),
      fill: { color: b.fill },
      line: { color: b.line, width: 1.0, dashType: b.dash || 'solid' },
      objectName: `ovl_comp_bar_${i}`,
    });

    // 棒の上に数字
    L.text(s, b.disp, {
      x: curX - 0.1,
      y: barY - 0.22,
      w: barW + 0.2,
      h: 0.2,
      fontSize: 8.5,
      bold: true,
      color: C.text,
      align: 'center',
      valign: 'bottom',
      margin: 0,
      objectName: `ovl_comp_num_${i}`,
    });

    // x軸ラベル
    L.text(s, b.label, {
      x: curX - 0.1,
      y: baselineY + 0.06,
      w: barW + 0.2,
      h: 0.34,
      fontSize: 8.5,
      color: C.text,
      align: 'center',
      valign: 'top',
      margin: 0,
      objectName: `ovl_comp_lbl_${i}`,
    });

    curX += barW + gapComp;
  });

  // 左下の要点
  L.bullets(s, [
    `増益 +${(B31.op - F.v('fy26.op')).toLocaleString('en-US')} のうち、SCが5割、界面活性剤が4割。SCは電材の数量(27/3期 ${M.scenarios['基準'][0].em_t}t → 31/3期 ${B31.em_t}t)が中心`, // lint-ok: 割合は meta と同じ計算
    `基準は、上期のセグメント利益の年換算 ${F.n('calc.h1_seg_annual')} から +${F.n('calc.base31_vs_h1')}% しか伸ばしていない。樹脂と化成品は上期のペースより低く置いた`,
  ], {
    x: 0.5,
    y: 5.55,
    w: 8.2,
    h: 1.15,
    fontSize: 9,
    gap: 4,
    name: 'wf_bullets',
  });

  // ----------------------------------------------------
  // 右ペイン: 年度別(百万円)
  // ----------------------------------------------------
  L.paneHead(s, 8.95, 1.62, 3.88, '年度別(百万円)');

  const scBase = M.scenarios['基準'];
  const scBear = M.scenarios['弱気'];
  const scBull = M.scenarios['強気'];

  const tableRows = [
    ['年度', '基準', '弱気', '強気'],
    ['26/3期', F.n('fy26.op'), F.n('fy26.op'), F.n('fy26.op')],
    ['28/3期', Math.round(scBase[1].op).toLocaleString('en-US'), Math.round(scBear[1].op).toLocaleString('en-US'), Math.round(scBull[1].op).toLocaleString('en-US')],
    ['29/3期', Math.round(scBase[2].op).toLocaleString('en-US'), Math.round(scBear[2].op).toLocaleString('en-US'), Math.round(scBull[2].op).toLocaleString('en-US')],
    ['30/3期', Math.round(scBase[3].op).toLocaleString('en-US'), Math.round(scBear[3].op).toLocaleString('en-US'), Math.round(scBull[3].op).toLocaleString('en-US')],
    ['31/3期', Math.round(scBase[4].op).toLocaleString('en-US'), Math.round(scBear[4].op).toLocaleString('en-US'), Math.round(scBull[4].op).toLocaleString('en-US')],
    ['中計目標', `28/3期 ${F.n('mp.fy28_op')}`, '—', { text: `31/3期 ${F.n('mp.fy31_op')}`, options: { bold: true } }],
  ];

  L.table(s, tableRows, {
    x: 8.95,
    y: 1.98,
    w: 3.88,
    colW: [1.0, 0.95, 0.95, 0.98],
    fontSize: 9,
    rowH: 0.28,
    name: 'tbl_fwd_op',
  });

  L.text(s, `営業利益率は ${F('fy26.opm')} → ${F('calc.fy26_opm31')}(基準)。中計の\n2030年度目標 ${F('mp.fy31_opm')} にほぼ並ぶ`, {
    x: 8.95,
    y: 4.14,
    w: 3.88,
    h: 0.55,
    fontSize: 9,
    color: C.sub,
    margin: 0,
    objectName: 'fwd_opm_note',
  });
};
