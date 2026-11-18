// s11 5年後の貸借対照表(作り直し: 色を抑え、2本に絞る)
const M = require('../data/fwd_v3.json');

module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    source: '決算短信(2026年3月期)の貸借対照表、本分析の5年後モデル(設備投資は営業CFの範囲内、配当は中計の30円→50円、政策保有株は縮減方針)',
  });

  const base26 = M.base_fy2026;
  const B31 = M.scenarios['基準'][4];

  // ----------------------------------------------------
  // 左側: 純額の貸借対照表(百万円): 26/3期実績と31/3期基準
  // ----------------------------------------------------
  L.paneHead(s, 0.5, 1.62, 7.7, '純額の貸借対照表(百万円): 26/3期実績と31/3期基準');

  // 尺度: 大きい方の合計で高さ3.7in (y2.0〜5.7 の下揃え)
  const useTotal26 = base26.ppe + base26.wc + base26.inv_sec + base26.cash;
  const useTotal31 = B31.ppe + B31.wc + B31.inv_sec + B31.cash;
  const maxTotal = Math.max(useTotal26, useTotal31);
  const chartH = 3.7;
  const baseY = 5.7;

  // 2組の描画設定: 組の幅 3.3、棒幅 1.35、間隔は組の中 0.15・組の間 0.6
  // 中央に注記が入るよう、組1はやや左(x=0.625)、組2はやや右(x=4.725)に棒を配置
  const barW = 1.35;
  const barGap = 0.15;
  const groups = [
    { label: '26/3期 実績', data: base26, barStartX: 0.625, lblX: 0.5, lblW: 3.1 },
    { label: '31/3期 基準', data: B31, barStartX: 4.725, lblX: 4.6, lblW: 3.1 },
  ];

  groups.forEach((g, gi) => {
    const d = g.data;
    const useTotal = d.ppe + d.wc + d.inv_sec + d.cash;
    const otherVal = useTotal - d.ibd - d.equity;

    // 使い道(左の棒): 有形固定資産 ppe(C.sub)/ 運転資本 wc(C.gray)/ 投資有価証券 inv_sec(C.rule)/ 現金 cash(C.tint)
    const useItems = [
      { name: '有形固定資産', val: d.ppe, color: C.sub, textColor: C.white, bold: true },
      { name: '運転資本', val: d.wc, color: C.gray, textColor: C.text, line: C.rule },
      { name: '投資有価証券', val: d.inv_sec, color: C.rule, textColor: C.text, line: C.sub },
      { name: '現金', val: d.cash, color: C.tint, textColor: C.text, line: C.sub },
    ];

    // 調達(右の棒): 自己資本 equity(C.primary)/ 有利子負債 ibd(C.dark)/ その他(純額)= 使い道の合計 − ibd − equity(C.tint)
    const fundItems = [
      { name: '自己資本', val: d.equity, color: C.primary, textColor: C.white, bold: true },
      { name: '有利子負債', val: d.ibd, color: C.dark, textColor: C.white, bold: true },
      { name: 'その他(純額)', val: otherVal, color: C.tint, textColor: C.text, line: C.rule },
    ];

    const leftBarX = g.barStartX;
    const rightBarX = leftBarX + barW + barGap;

    // 使い道棒 (左) 積み上げ
    let currY = baseY;
    useItems.forEach((item, ii) => {
      const h = (item.val / maxTotal) * chartH;
      const segY = currY - h;
      L.box(s, leftBarX, segY, barW, h, {
        fill: item.color,
        line: item.line || item.color,
        lw: 0.75,
        name: `ovl_bar_use_${gi}_${ii}`,
      });

      // 区画の中に名前と数字(8.5pt、塗りが濃い区画は白字)
      const valStr = Math.round(item.val).toLocaleString('en-US');
      const textContent = h >= 0.45 ? `${item.name}\n${valStr}` : `${item.name} ${valStr}`;
      s.addText(textContent, {
        x: leftBarX + 0.04,
        y: segY,
        w: barW - 0.08,
        h: h,
        fontFace: 'Meiryo UI',
        fontSize: 8.5,
        bold: !!item.bold,
        color: item.textColor,
        align: 'center',
        valign: 'middle',
        margin: 0,
        isTextBox: true,
        objectName: `ovl_txt_use_${gi}_${ii}`,
      });
      currY = segY;
    });

    // 調達棒 (右) 積み上げ
    currY = baseY;
    fundItems.forEach((item, ii) => {
      const h = (item.val / maxTotal) * chartH;
      const segY = currY - h;
      L.box(s, rightBarX, segY, barW, h, {
        fill: item.color,
        line: item.line || item.color,
        lw: 0.75,
        name: `ovl_bar_fund_${gi}_${ii}`,
      });

      const valStr = Math.round(item.val).toLocaleString('en-US');
      const textContent = h >= 0.45 ? `${item.name}\n${valStr}` : `${item.name} ${valStr}`;
      s.addText(textContent, {
        x: rightBarX + 0.04,
        y: segY,
        w: barW - 0.08,
        h: h,
        fontFace: 'Meiryo UI',
        fontSize: 8.5,
        bold: !!item.bold,
        color: item.textColor,
        align: 'center',
        valign: 'middle',
        margin: 0,
        isTextBox: true,
        objectName: `ovl_txt_fund_${gi}_${ii}`,
      });
      currY = segY;
    });

    // 組の下のラベル: '26/3期 実績' '31/3期 基準' と 自己資本比率 x%
    s.addText(g.label, {
      x: g.lblX,
      y: 5.76,
      w: g.lblW,
      h: 0.22,
      fontFace: 'Meiryo UI',
      fontSize: 9.5,
      bold: true,
      color: C.dark,
      align: 'center',
      valign: 'middle',
      margin: 0,
      isTextBox: true,
      objectName: `ovl_grp_lbl_${gi}`,
    });
    s.addText(`自己資本比率 ${d.equity_ratio}%`, {
      x: g.lblX,
      y: 5.98,
      w: g.lblW,
      h: 0.20,
      fontFace: 'Meiryo UI',
      fontSize: 8.5,
      color: C.sub,
      align: 'center',
      valign: 'middle',
      margin: 0,
      isTextBox: true,
      objectName: `ovl_grp_eq_${gi}`,
    });
  });

  // 2組の間の注記 (太字、矢印つき)
  // 有利子負債: ${(B31.ibd - M.base_fy2026.ibd).toLocaleString('en-US')} (C.dark)
  // 自己資本: +${(B31.equity - M.base_fy2026.equity).toLocaleString('en-US')} (C.primary)
  const midX1 = 0.625 + barW * 2 + barGap; // 3.475
  const midX2 = 4.725;                     // 4.725
  const midCenterX = (midX1 + midX2) / 2;  // 4.10
  const noteW = 1.18;
  const noteX = midCenterX - noteW / 2;    // 3.51

  // 有利子負債の注記
  const ibdDiff = B31.ibd - base26.ibd;
  const ibdDiffStr = `有利子負債 ${ibdDiff.toLocaleString('en-US')}`;
  s.addText(ibdDiffStr, {
    x: noteX,
    y: 3.12,
    w: noteW,
    h: 0.22,
    fontFace: 'Meiryo UI',
    fontSize: 8.5,
    bold: true,
    color: C.dark,
    align: 'center',
    valign: 'middle',
    fill: { color: C.white },
    margin: 0,
    isTextBox: true,
    objectName: 'ovl_note_ibd',
  });
  L.arrow(s, midX1 + 0.08, 3.36, midX2 - 0.08, 3.36, { color: C.dark, width: 1.5 });

  // 自己資本の注記
  const eqDiff = B31.equity - base26.equity;
  const eqDiffStr = `自己資本 +${eqDiff.toLocaleString('en-US')}`;
  s.addText(eqDiffStr, {
    x: noteX,
    y: 4.54,
    w: noteW,
    h: 0.22,
    fontFace: 'Meiryo UI',
    fontSize: 8.5,
    bold: true,
    color: C.primary,
    align: 'center',
    valign: 'middle',
    fill: { color: C.white },
    margin: 0,
    isTextBox: true,
    objectName: 'ovl_note_equity',
  });
  L.arrow(s, midX1 + 0.08, 4.78, midX2 - 0.08, 4.78, { color: C.primary, width: 1.5 });

  // 左下の補足注記
  s.addText('※ 運転資本=売上債権+棚卸資産−仕入債務。その他(純額)=投資その他の資産−その他固定負債等', {
    x: 0.5,
    y: 6.30,
    w: 7.7,
    h: 0.22,
    fontFace: 'Meiryo UI',
    fontSize: 8.5,
    color: C.sub,
    valign: 'middle',
    margin: 0,
    isTextBox: true,
    objectName: 'ovl_bs_note',
  });

  // ----------------------------------------------------
  // 右側上段: 5年間のお金の使い道(基準、累計)
  // ----------------------------------------------------
  L.paneHead(s, 8.45, 1.62, 4.38, '5年間のお金の使い道(基準、累計)');

  const baseScen = M.scenarios['基準'];
  const sumOcf = baseScen.reduce((acc, r) => acc + r.ocf, 0);
  const sumCapex = baseScen.reduce((acc, r) => acc + r.capex, 0);
  const sumFcf = baseScen.reduce((acc, r) => acc + r.fcf, 0);
  const sumDiv = baseScen.reduce((acc, r) => acc + r.dps * r.shares, 0);
  const secSold = base26.inv_sec - B31.inv_sec;
  const ibdRepaid = base26.ibd - B31.ibd;
  const eqInc = B31.equity - base26.equity;

  const rows1 = [
    ['', '百万円'],
    ['営業CF', `+${Math.round(sumOcf).toLocaleString('en-US')}`],
    ['設備投資', `-${Math.round(sumCapex).toLocaleString('en-US')}`],
    [
      { text: 'FCF', options: { bold: true } },
      { text: `+${Math.round(sumFcf).toLocaleString('en-US')}`, options: { bold: true } },
    ],
    ['配当', `-${Math.round(sumDiv).toLocaleString('en-US')}`],
    ['政策保有株などの売却', `+${Math.round(secSold).toLocaleString('en-US')}`],
    [
      { text: '有利子負債の返済', options: { bold: true } },
      { text: `-${Math.round(ibdRepaid).toLocaleString('en-US')}`, options: { bold: true } },
    ],
    [
      { text: '自己資本の増加', options: { bold: true, color: C.primary } },
      { text: `+${Math.round(eqInc).toLocaleString('en-US')}`, options: { bold: true, color: C.primary } },
    ],
  ];

  L.table(s, rows1, {
    x: 8.45,
    y: 1.96,
    w: 4.38,
    colW: [2.5, 1.88],
    fontSize: 9,
    rowH: 0.25,
    align: ['left', 'right'],
  });

  // ----------------------------------------------------
  // 右側中段: シナリオ別の31/3期
  // ----------------------------------------------------
  L.paneHead(s, 8.45, 4.14, 4.38, 'シナリオ別の31/3期');

  const bear31 = M.scenarios['弱気'][4];
  const bull31 = M.scenarios['強気'][4];

  const rows2 = [
    ['', '弱気', '基準', '強気'],
    [
      '有利子負債',
      Math.round(bear31.ibd).toLocaleString('en-US'),
      Math.round(B31.ibd).toLocaleString('en-US'),
      Math.round(bull31.ibd).toLocaleString('en-US'),
    ],
    [
      '自己資本',
      Math.round(bear31.equity).toLocaleString('en-US'),
      Math.round(B31.equity).toLocaleString('en-US'),
      Math.round(bull31.equity).toLocaleString('en-US'),
    ],
    [
      '自己資本比率',
      `${bear31.equity_ratio.toFixed(1)}%`,
      `${B31.equity_ratio.toFixed(1)}%`,
      `${bull31.equity_ratio.toFixed(1)}%`,
    ],
    [
      'ROE',
      `${bear31.roe.toFixed(1)}%`,
      `${B31.roe.toFixed(1)}%`,
      `${bull31.roe.toFixed(1)}%`,
    ],
  ];

  L.table(s, rows2, {
    x: 8.45,
    y: 4.48,
    w: 4.38,
    colW: [1.38, 1.0, 1.0, 1.0],
    fontSize: 8.8,
    rowH: 0.26,
    align: ['left', 'right', 'right', 'right'],
  });

  // ----------------------------------------------------
  // 右側下段: takeaway
  // ----------------------------------------------------
  L.takeaway(
    s,
    8.45,
    6.08,
    4.38,
    0.62,
    '返済に回すほど自己資本が積み上がり、ROEを押し下げる。何に使うかは次ページ'
  );
};
