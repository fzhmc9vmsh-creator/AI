// s05a 中計の進捗(新規)
module.exports = function build(pres, L) {
  const { F, C } = L;
  const s = L.contentSlide(pres, {
    source: '中期経営計画 TOHO Step Up Plan 2027 p.11(連結営業利益計画のセグメント別内訳)、決算短信(2025年3月期・2026年3月期・2027年3月期第2四半期)のセグメント情報。\n年換算は上期×2(本分析)',
  });

  // ======================= 左: セグメント利益の比例描画 =======================
  L.paneHead(s, 0.5, 1.62, 7.6, 'セグメント利益: 25/3期実績・27/3期上期の年換算・中計(28/3期)の計画(百万円)', 'pane_left_head');

  const segments = [
    { name: '界面活性剤', key: 'surf', isSpec: false },
    { name: '樹脂', key: 'resin', isSpec: false },
    { name: '化成品', key: 'chem', isSpec: false },
    { name: 'スペシャリティーケミカル', key: 'spec', isSpec: true },
  ];

  const baseX = 2.35;
  const scale = 5.55 / 1700; // 0〜1,700百万円を比例 (1百万円 = 5.55/1700 in)
  const startY = 2.05;
  const rowHeight = 0.95;

  segments.forEach((seg, i) => {
    const rowY = startY + i * rowHeight;

    // 行の左に名前(x0.5 w1.75、9pt、bold)
    L.text(s, seg.name, {
      x: 0.5,
      y: rowY + 0.32,
      w: 1.75,
      h: 0.32,
      fontSize: 9,
      bold: true,
      color: C.text,
      valign: 'middle',
      margin: 0,
      objectName: `ovl_seg_name_${seg.key}`,
    });

    // ① 細い灰色の棒(C.rule、h0.2)= 25/3期実績 F.v('fy25.seg_X_profit')
    const v1 = F.v(`fy25.seg_${seg.key}_profit`);
    const w1 = Math.max(0.02, v1 * scale);
    L.box(s, baseX, rowY + 0.14, w1, 0.20, {
      fill: C.rule,
      line: C.rule,
      name: `ovl_bar1_${seg.key}`,
    });

    // ② 太い棒(h0.32)= 上期の年換算 F.v('calc.h1ann_X')。汎用3つは C.primary、SC だけ C.sub
    const v2 = F.v(`calc.h1ann_${seg.key}`);
    const w2 = Math.max(0.02, v2 * scale);
    const bar2Color = seg.isSpec ? C.sub : C.primary;
    L.box(s, baseX, rowY + 0.38, w2, 0.32, {
      fill: bar2Color,
      line: bar2Color,
      name: `ovl_bar2_${seg.key}`,
    });

    // ③ 計画の幅 = mp.seg_X_lo〜mp.seg_X_hi を、枠だけの箱(塗りなし、枠 C.dark の点線、h0.5)で②の棒に重ねて描く
    const vlo = F.v(`mp.seg_${seg.key}_lo`);
    const vhi = F.v(`mp.seg_${seg.key}_hi`);
    const planX = baseX + vlo * scale;
    const planW = Math.max(0.02, (vhi - vlo) * scale);
    s.addShape('rect', {
      x: planX,
      y: rowY + 0.29,
      w: planW,
      h: 0.50,
      fill: { color: C.white, transparency: 100 },
      line: { color: C.dark, width: 1.0, dashType: 'dash' },
      objectName: `ovl_plan_box_${seg.key}`,
    });

    // 各棒の右端に数字(8.5pt): ②の棒の右に 年換算 1,418(計画比 113%) の形で書く
    // surf や spec のように描画域右端や計画箱と干渉しないよう、2行で綺麗に収める
    const labelText = `年換算 ${F.n(`calc.h1ann_${seg.key}`)}\n(計画比 ${F.n(`calc.plan_prog_${seg.key}`)}%)`;
    L.text(s, labelText, {
      x: baseX + w2 + 0.05,
      y: rowY + 0.32,
      w: 1.05,
      h: 0.44,
      fontSize: 8.5,
      color: C.text,
      valign: 'middle',
      margin: 0,
      objectName: `ovl_val_${seg.key}`,
    });
  });

  // 凡例を描画域の下(y5.95)に1行: 細い灰色=25/3期実績、太い棒=27/3期上期の年換算、点線の箱=中計の計画(28/3期)
  const legY = 5.92;
  // ① 細い灰色
  L.box(s, 2.35, legY + 0.07, 0.28, 0.08, { fill: C.rule, line: C.rule, name: 'ovl_leg_box1' });
  L.text(s, '25/3期実績', { x: 2.68, y: legY, w: 0.95, h: 0.22, fontSize: 8.5, color: C.sub, valign: 'middle', margin: 0, objectName: 'ovl_leg_t1' });

  // ② 太い棒
  L.box(s, 3.80, legY + 0.04, 0.28, 0.14, { fill: C.primary, line: C.primary, name: 'ovl_leg_box2' });
  L.text(s, '27/3期上期の年換算', { x: 4.13, y: legY, w: 1.45, h: 0.22, fontSize: 8.5, color: C.sub, valign: 'middle', margin: 0, objectName: 'ovl_leg_t2' });

  // ③ 点線の箱
  s.addShape('rect', {
    x: 5.75,
    y: legY + 0.02,
    w: 0.28,
    h: 0.18,
    fill: { color: C.white, transparency: 100 },
    line: { color: C.dark, width: 1.0, dashType: 'dash' },
    objectName: 'ovl_leg_box3',
  });
  L.text(s, '中計の計画(28/3期)', { x: 6.08, y: legY, w: 1.60, h: 0.22, fontSize: 8.5, color: C.sub, valign: 'middle', margin: 0, objectName: 'ovl_leg_t3' });

  // ======================= 右: 進捗の表と読み =======================
  L.paneHead(s, 8.35, 1.62, 4.48, '進捗の表(百万円)', 'pane_right_head');

  const fy25Total = F.v('fy25.seg_surf_profit') + F.v('fy25.seg_resin_profit') + F.v('fy25.seg_chem_profit') + F.v('fy25.seg_spec_profit');

  const hd = (t) => ({ text: t, options: { bold: true, color: C.white, fill: { color: C.dark } } });
  const tableRows = [
    [hd(''), hd('25/3期'), hd('上期年換算'), hd('中計計画'), hd('進捗')],
    [
      '界面活性剤',
      F.n('fy25.seg_surf_profit'),
      F.n('calc.h1ann_surf'),
      `${F.n('mp.seg_surf_lo')}〜${F.n('mp.seg_surf_hi')}`,
      { text: F('calc.plan_prog_surf'), options: { color: C.primary, bold: true } },
    ],
    [
      '樹脂',
      F.n('fy25.seg_resin_profit'),
      F.n('calc.h1ann_resin'),
      `${F.n('mp.seg_resin_lo')}〜${F.n('mp.seg_resin_hi')}`,
      { text: F('calc.plan_prog_resin'), options: { color: C.primary, bold: true } },
    ],
    [
      '化成品',
      F.n('fy25.seg_chem_profit'),
      F.n('calc.h1ann_chem'),
      `${F.n('mp.seg_chem_lo')}〜${F.n('mp.seg_chem_hi')}`,
      { text: F('calc.plan_prog_chem'), options: { color: C.primary, bold: true } },
    ],
    [
      'スペシャリティーケミカル',
      F.n('fy25.seg_spec_profit'),
      F.n('calc.h1ann_spec'),
      `${F.n('mp.seg_spec_lo')}〜${F.n('mp.seg_spec_hi')}`,
      { text: F('calc.plan_prog_spec'), options: { color: C.red, bold: true } },
    ],
    [
      { text: '4セグメント計', options: { bold: true } },
      { text: Math.round(fy25Total).toLocaleString('en-US'), options: { bold: true } },
      { text: F.n('calc.seg_ann_total'), options: { bold: true } },
      { text: '3,000〜3,300', options: { bold: true } }, // lint-ok: 指示書の確定値
      { text: '—', options: { bold: true } },
    ],
  ];

  L.table(s, tableRows, {
    x: 8.35,
    y: 1.98,
    w: 4.48,
    colW: [1.35, 0.8, 0.85, 0.85, 0.63],
    fontSize: 9,
    rowH: 0.25,
    align: ['left', 'right', 'right', 'right', 'right'],
    name: 'tbl_progress',
  });

  // 読み
  L.paneHead(s, 8.35, 3.86, 4.48, '読み', 'pane_reading_head');
  L.bullets(s, [
    `汎用3セグメントの年換算 ${F.n('calc.legacy_ann')} は計画の中央値 ${F.n('calc.legacy_plan_mid')} を ${F.n('calc.legacy_vs_plan')} 上回る。値上げと構成の改善が、計画より2年早く効いた`,
    `SCは計画の中央値まで ${F.n('calc.spec_gap_plan')} 足りない。電材二期(+90t、11月完工予定)の立ち上げで埋める計画`,
    `前年は下期のほうが利益が大きかった(SC 上期 ${F.n('fy26h1.seg_spec_profit')} → 下期 ${F.n('calc.fy26_h2_spec')})。年換算は季節性では過大にならない。ただし下期は原料高が効く`,
    '中計の達成は、汎用品の粗利率の維持(価値の芯)と電材の立ち上げの両方にかかる。前者が崩れるとSCだけでは届かない',
  ], {
    x: 8.35,
    y: 4.2,
    w: 4.48,
    h: 1.84,
    fontSize: 8.8,
    gap: 2,
    name: 'bullets_reading',
  });

  // ======================= 一番下: テイクアウェイ =======================
  L.takeaway(s, 0.5, 6.15, 12.333, 0.55, '次の確認(2月4日): 汎用3セグメントの利益の水準が保たれ、SCが上期の年換算を上回るか。両方なら中計の営業利益3,000百万円は今期に届く'); // lint-ok: 指示書の確定値
};
