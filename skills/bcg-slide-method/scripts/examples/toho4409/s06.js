// s06 変曲点(ロードマップ)
const M = require('../data/fwd_v3.json');

module.exports = function build(pres, L) {
  const { F, C } = L;
  const s = L.contentSlide(pres, {
    source: '中期経営計画 p.10〜15・p.18、決算説明資料 p.12〜13、有価証券報告書「設備の新設」、決算短信のキャッシュ・フロー計算書。2028年3月期以降のFCFは本分析の5年後モデル(基準シナリオ)',
  });

  // ========== 左パネル: ロードマップ (ガントチャート) ==========
  // 左 x0.5 w8.9 にガント
  L.paneHead(s, 0.5, 1.62, 8.9, '制約が解ける日付(現在地 = 2026年11月)');

  const labelW = 2.15;
  const ax = 0.5 + labelW; // 2.65
  const aw = 8.9 - labelW;  // 6.75
  const tFrom = 2025 + 3 / 12; // 2025年4月
  const tTo = 2031 + 3 / 12;   // 2031年3月末
  const getX = (y, m) => {
    const t = y + (m - 1) / 12;
    return ax + Math.max(0, Math.min(1, (t - tFrom) / (tTo - tFrom))) * aw;
  };
  const nowX = getX(2026, 11);

  // 年度の目盛り (2025〜2030年度)
  const headerY = 2.02;
  const headerH = 0.28;
  const years = [2025, 2026, 2027, 2028, 2029, 2030];
  const chartBottom = 6.45;

  years.forEach((yr, i) => {
    const x0 = getX(yr, 4);
    const x1 = getX(yr + 1, 4);
    const w = x1 - x0;
    // ヘッダー背景
    s.addShape('rect', {
      x: x0, y: headerY, w, h: headerH,
      fill: { color: i % 2 === 0 ? C.tint : C.white },
      line: { color: C.rule, width: 0.5 },
      objectName: `ovl_s06_yr_bg_${yr}`,
    });
    L.text(s, `${yr}年度`, {
      x: x0, y: headerY, w, h: headerH,
      fontSize: 8.5, bold: true, color: C.dark, align: 'center', valign: 'middle', margin: 0,
      objectName: `ovl_s06_yr_txt_${yr}`,
    });
    // 縦グリッド線
    if (i > 0) {
      s.addShape('line', {
        x: x0, y: headerY + headerH, w: 0.001, h: chartBottom - (headerY + headerH),
        line: { color: C.rule, width: 0.5, dashType: 'sysDot' },
        objectName: `ovl_s06_grid_${yr}`,
      });
    }
  });

  // ガントの各行
  const gridTop = headerY + headerH + 0.06; // 2.36
  const rowPitch = (chartBottom - gridTop) / 7; // 約 0.58
  const barH = 0.32;

  const rows = [
    {
      label: '中期経営計画',
      render: (ry) => {
        const x0 = getX(2025, 4);
        const x1 = getX(2028, 4);
        s.addShape('roundRect', {
          x: x0, y: ry, w: x1 - x0, h: barH,
          fill: { color: C.sub }, line: { color: C.sub }, rectRadius: 0.04,
          objectName: 'ovl_s06_b1',
        });
        L.text(s, 'TOHO Step Up Plan 2027', {
          x: x0 + 0.05, y: ry, w: x1 - x0 - 0.1, h: barH,
          fontSize: 8.5, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0,
          objectName: 'ovl_s06_b1_t',
        });
        // 2028-03 に '営業利益30億円・ROE8%' のラベル
        L.text(s, `営業利益${F.n('mp.fy28_op')}百万円・ROE8%`, { // lint-ok: 指示書の確定値
          x: x1 + 0.08, y: ry, w: 2.5, h: barH,
          fontSize: 8.5, bold: true, color: C.primary, valign: 'middle', margin: 0,
          objectName: 'ovl_s06_b1_lbl',
        });
      },
    },
    {
      label: '上海 第3期(+10,500t)',
      render: (ry) => {
        // 2024-10〜2026-03 建設 → 2026-03 稼働の印(◆)→ 以降 C.primary の帯 '生産量・販売量が増加中'
        const xStart = getX(2025, 4);
        const xOp = getX(2026, 4);
        const xEnd = getX(2031, 4);
        // 建設帯 (2025-04〜2026-03)
        s.addShape('roundRect', {
          x: xStart, y: ry, w: xOp - xStart, h: barH,
          fill: { color: C.gray }, line: { color: C.rule, width: 0.75 }, rectRadius: 0.04,
          objectName: 'ovl_s06_b2_const',
        });
        L.text(s, '建設(24/10〜)', {
          x: xStart, y: ry, w: xOp - xStart, h: barH,
          fontSize: 8.5, color: C.sub, align: 'center', valign: 'middle', margin: 0,
          objectName: 'ovl_s06_b2_const_t',
        });
        // 稼働の印(◆) 2026-03
        s.addShape('diamond', {
          x: xOp - 0.11, y: ry + barH / 2 - 0.11, w: 0.22, h: 0.22,
          fill: { color: C.dark }, line: { color: C.white, width: 1 },
          objectName: 'ovl_s06_b2_mark',
        });
        // 稼働後の帯
        s.addShape('roundRect', {
          x: xOp + 0.05, y: ry, w: xEnd - (xOp + 0.05), h: barH,
          fill: { color: C.primary }, line: { color: C.primary }, rectRadius: 0.04,
          objectName: 'ovl_s06_b2_op',
        });
        L.text(s, '26/3稼働 ◆ 生産量・販売量が増加中', {
          x: nowX + 0.15, y: ry, w: xEnd - (nowX + 0.15) - 0.1, h: barH,
          fontSize: 8.5, bold: true, color: C.white, align: 'left', valign: 'middle', margin: 0,
          objectName: 'ovl_s06_b2_op_t',
        });
      },
    },
    {
      label: `電材 二期(+90t、${F.n('cap.ep2_invest')}百万円)`,
      render: (ry) => {
        // 2025-04〜2026-11 建設 → 2026-11 完工 ◆ → 2026-11〜2028-10 '立ち上げ(約2年)' C.light → 以降 '本格稼働 210t'
        const x0 = getX(2025, 4);
        const xNov26 = getX(2026, 11);
        const xOct28 = getX(2028, 10);
        const xEnd = getX(2031, 4);

        // 建設帯
        s.addShape('roundRect', {
          x: x0, y: ry, w: xNov26 - x0, h: barH,
          fill: { color: C.gray }, line: { color: C.rule, width: 0.75 }, rectRadius: 0.04,
          objectName: 'ovl_s06_b3_const',
        });
        L.text(s, '建設', {
          x: x0, y: ry, w: xNov26 - x0, h: barH,
          fontSize: 8.5, color: C.sub, align: 'center', valign: 'middle', margin: 0,
          objectName: 'ovl_s06_b3_const_t',
        });

        // 完工 ◆
        s.addShape('diamond', {
          x: xNov26 - 0.11, y: ry + barH / 2 - 0.11, w: 0.22, h: 0.22,
          fill: { color: C.dark }, line: { color: C.white, width: 1 },
          objectName: 'ovl_s06_b3_mark',
        });

        // 立ち上げ帯 (C.light)
        s.addShape('roundRect', {
          x: xNov26 + 0.05, y: ry, w: xOct28 - (xNov26 + 0.05), h: barH,
          fill: { color: C.light }, line: { color: C.light }, rectRadius: 0.04,
          objectName: 'ovl_s06_b3_ramp',
        });
        L.text(s, '立ち上げ(約2年)', {
          x: xNov26 + 0.05, y: ry, w: xOct28 - (xNov26 + 0.05), h: barH,
          fontSize: 8.5, bold: true, color: C.dark, align: 'center', valign: 'middle', margin: 0,
          objectName: 'ovl_s06_b3_ramp_t',
        });

        // 本格稼働 210t
        s.addShape('roundRect', {
          x: xOct28 + 0.04, y: ry, w: xEnd - (xOct28 + 0.04), h: barH,
          fill: { color: C.primary }, line: { color: C.primary }, rectRadius: 0.04,
          objectName: 'ovl_s06_b3_full',
        });
        L.text(s, '本格稼働 210t', {
          x: xOct28 + 0.04, y: ry, w: xEnd - (xOct28 + 0.04), h: barH,
          fontSize: 8.5, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0,
          objectName: 'ovl_s06_b3_full_t',
        });
      },
    },
    {
      label: '電材 更なる能力拡大',
      render: (ry) => {
        // 2027-04〜 '検討中(要員の確保・育成を進行)' の点線の帯。強気は2029年度実行・2030年度寄与(275t)
        const x0 = getX(2027, 4);
        const xEnd = getX(2031, 4);
        s.addShape('roundRect', {
          x: x0, y: ry, w: xEnd - x0, h: barH,
          fill: { color: C.tint }, line: { color: C.teal, width: 1, dashType: 'dash' }, rectRadius: 0.04,
          objectName: 'ovl_s06_b4',
        });
        L.text(s, '検討中(要員の確保・育成を進行) / 強気は2029年度実行・2030年度寄与(275t)', {
          x: x0 + 0.08, y: ry, w: xEnd - x0 - 0.16, h: barH,
          fontSize: 8.5, bold: true, color: C.dark, align: 'left', valign: 'middle', margin: 0,
          objectName: 'ovl_s06_b4_t',
        });
      },
    },
    {
      label: '汎用品の上海・鹿島への移管',
      render: (ry) => {
        // 2025-04〜2028-03 '進行中'
        const x0 = getX(2025, 4);
        const x1 = getX(2028, 4);
        s.addShape('roundRect', {
          x: x0, y: ry, w: x1 - x0, h: barH,
          fill: { color: C.tint }, line: { color: C.rule, width: 0.75 }, rectRadius: 0.04,
          objectName: 'ovl_s06_b5',
        });
        L.text(s, '進行中', {
          x: x0, y: ry, w: x1 - x0, h: barH,
          fontSize: 8.5, bold: true, color: C.dark, align: 'center', valign: 'middle', margin: 0,
          objectName: 'ovl_s06_b5_t',
        });
      },
    },
    {
      label: '投資の山',
      render: (ry) => {
        // 2018-04〜2026-03 は範囲外なので、行の左端に `8期累計 ${F('capex.cum8y')}` と書き、2026-03 で終わる帯
        const x0 = getX(2025, 4);
        const x1 = getX(2026, 4);
        s.addShape('roundRect', {
          x: x0, y: ry, w: x1 - x0, h: barH,
          fill: { color: C.amber }, line: { color: C.amber }, rectRadius: 0.04,
          objectName: 'ovl_s06_b6',
        });
        L.text(s, '〜26/3 集中期', {
          x: x0, y: ry, w: x1 - x0, h: barH,
          fontSize: 8.5, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0,
          objectName: 'ovl_s06_b6_t',
        });
        // 帯の右側(現在地線の右側)に 8期累計と補足を記載し、赤線との重なりを回避
        L.text(s, `8期累計 ${F('capex.cum8y')} → 投資の山を越え上期からFCF黒字化`, {
          x: nowX + 0.15, y: ry, w: 4.5, h: barH,
          fontSize: 8.5, bold: true, color: C.dark, valign: 'middle', margin: 0,
          objectName: 'ovl_s06_b6_lbl',
        });
      },
    },
    {
      label: '資本政策',
      render: (ry) => {
        // 2025-04 IR部署新設 ◆、2025-05 資本コスト開示 ◆、2026-06 資本コスト資料更新 ◆、2030年度 'ROE10%・配当50円' の目標印
        const x2504 = getX(2025, 4);
        const x2606 = getX(2026, 6);
        const x3004 = getX(2030, 4);

        // 2025-04 & 2025-05 (1つのまとまりとしてすっきり表示)
        s.addShape('diamond', {
          x: x2504 - 0.08, y: ry + barH / 2 - 0.08, w: 0.16, h: 0.16,
          fill: { color: C.teal }, line: { color: C.teal },
          objectName: 'ovl_s06_b7_d1',
        });
        L.text(s, '25/4 IR新設\n25/5 コスト開示', {
          x: x2504 + 0.10, y: ry - 0.06, w: 1.15, h: barH + 0.12,
          fontSize: 8.5, color: C.dark, valign: 'middle', margin: 0,
          objectName: 'ovl_s06_b7_t1',
        });

        // 2026-06
        s.addShape('diamond', {
          x: x2606 - 0.08, y: ry + barH / 2 - 0.08, w: 0.16, h: 0.16,
          fill: { color: C.teal }, line: { color: C.teal },
          objectName: 'ovl_s06_b7_d2',
        });
        L.text(s, '26/6 資料更新', {
          x: x2606 + 0.10, y: ry, w: 1.10, h: barH,
          fontSize: 8.5, color: C.dark, valign: 'middle', margin: 0,
          objectName: 'ovl_s06_b7_t2',
        });

        // 2030年度 'ROE10%・配当50円'
        s.addShape('roundRect', {
          x: x3004, y: ry, w: getX(2031, 4) - x3004, h: barH,
          fill: { color: C.tint }, line: { color: C.primary, width: 1 }, rectRadius: 0.04,
          objectName: 'ovl_s06_b7_t3_bg',
        });
        L.text(s, '◆ ROE10%・配当50円 目標', { // lint-ok: 指示書の確定値
          x: x3004 + 0.05, y: ry, w: getX(2031, 4) - x3004 - 0.1, h: barH,
          fontSize: 8.5, bold: true, color: C.primary, align: 'center', valign: 'middle', margin: 0,
          objectName: 'ovl_s06_b7_t3',
        });
      },
    },
  ];

  // 現在地 2026-11 の縦線(行の帯より先に描き、帯の文字の下に隠れるようにする)
  s.addShape('line', {
    x: nowX, y: headerY - 0.02, w: 0.001, h: chartBottom - headerY + 0.02,
    line: { color: C.red, width: 1.5, dashType: 'dash' },
    objectName: 'ovl_s06_now_line',
  });

  // 行の描画
  rows.forEach((r, i) => {
    const ry = gridTop + i * rowPitch + (rowPitch - barH) / 2;
    // 行ラベル
    L.text(s, r.label, {
      x: 0.5, y: ry - 0.05, w: labelW - 0.1, h: barH + 0.1,
      fontSize: 8.8, bold: true, color: C.dark, valign: 'middle', margin: 0,
      objectName: `ovl_s06_lbl_${i}`,
    });
    // ガントバー
    r.render(ry);
  });

  // 現在地のラベル
  s.addShape('roundRect', {
    x: nowX - 0.48, y: headerY - 0.22, w: 0.96, h: 0.20,
    fill: { color: C.red }, line: { color: C.red }, rectRadius: 0.03,
    objectName: 'ovl_s06_now_bg',
  });
  L.text(s, '現在地 (26/11)', {
    x: nowX - 0.48, y: headerY - 0.22, w: 0.96, h: 0.20,
    fontSize: 8.5, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0,
    objectName: 'ovl_s06_now_txt',
  });

  // ========== 右パネル: FCF(百万円) ==========
  // x 9.6, w 3.23
  L.paneHead(s, 9.6, 1.62, 3.23, 'FCF(百万円)');

  // グラフデータ
  const fcfLabels = ['26/3', '27/3上', '28/3', '29/3', '30/3', '31/3'];
  const fcfActual = [
    F.v('fy26.ocf') - F.v('fy26.capex'),
    F.v('fy27h1.ocf') - F.v('fy27h1.capex'),
    null, null, null, null,
  ];
  const fcfForecast = [
    null, null,
    M.scenarios['基準'][1].fcf,
    M.scenarios['基準'][2].fcf,
    M.scenarios['基準'][3].fcf,
    M.scenarios['基準'][4].fcf,
  ];

  s.addChart(pres.charts.BAR, [
    { name: '実績', labels: fcfLabels, values: fcfActual },
    { name: '予測(基準)', labels: fcfLabels, values: fcfForecast },
  ], L.chartStyle({
    x: 9.6,
    y: 1.98,
    w: 3.23,
    h: 2.75,
    barGrouping: 'stacked',
    barGapWidthPct: 45,
    dataLabelPosition: 'ctr',
    dataLabelFontSize: 7.5,
    dataLabelFormatCode: '#,##0',
    catAxisLabelFontSize: 8,
    valAxisLabelFontSize: 8,
    valAxisLabelFormatCode: '#,##0',
    chartColors: [C.primary, C.light],
    showLegend: false,
    showValue: true,
    objectName: 's06_chart_fcf',
  }));

  // 下の bullets
  L.bullets(s, [
    `上期の設備投資 ${F('fy27h1.capex')} は減価償却 ${F('fy27h1.dep')} とほぼ同額。投資を営業CFの範囲内に抑える方針どおり`,
    '5年間のFCFは借入返済・増配・自己株取得の原資になる。何に使うかが s12 の論点',
  ], {
    x: 9.6,
    y: 4.86,
    w: 3.23,
    h: 1.82,
    fontSize: 9,
    name: 's06_bullets',
  });
};
