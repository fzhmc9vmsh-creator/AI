// s14b 価値の芯
module.exports = function build(pres, L) {
  const { F, C } = L;
  const s = L.contentSlide(pres, {
    source: 'valuate.py の感応度(valuation.json)、同業は第一工業製薬・三洋化成工業の2026年3月期決算短信、本分析の5年後モデル。電材の1tあたり営業利益は推定',
  });

  // 左上: 理論株価の感応度 (トルネード図)
  L.paneHead(s, 0.5, 1.62, 7.4, '理論株価の感応度(円、事業エンジン経路 1,022円からの差。valuate.py)'); // lint-ok: 指示書の確定値

  function parseDiff(id) {
    // valuate.py の差(小数1桁)を整数に丸める。p.24 の感応度の表も同じ丸めを使う
    const raw = F.n(id);
    const num = Math.round(parseFloat(raw.replace(/−/g, '-').replace(/[+,]/g, '').trim()));
    return isNaN(num) ? 0 : num;
  }

  const vEngine = parseFloat(F.n('val.value.engine'));
  const vRoe65 = F.v('val.roe65');

  // 行(上から、各 h0.42、間隔0.22):
  // 1 '全社の粗利率 ±1pt' 右に +val.sens.全社の粗利率 +1pt(EPS +21%).diff(C.primary)、左に val.sens.全社の粗利率 −1pt(EPS −21%).diff(C.sub)
  // 2 '定常ROE 6.5%(返還なし)' 左に (val.roe65 − value.engine)(C.sub)
  // 3 '借入金利 +1%' 左に val.sens.借入金利が1%上昇(EPS −11%).diff(C.sub)
  // 4 '電材の販売数量 ±30t' 右 val.sens.電材の販売数量 +30t(EPS +8%).diff(C.primary)、左 −30t(C.sub)
  const rows = [
    {
      name: '全社の粗利率 ±1pt', // lint-ok: 指示書の確定値
      posVal: parseDiff('val.sens.全社の粗利率 +1pt(EPS +21%).diff'),
      negVal: parseDiff('val.sens.全社の粗利率 −1pt(EPS −21%).diff'),
    },
    {
      name: '定常ROE 6.5%(返還なし)', // lint-ok: 指示書の確定値
      posVal: null,
      negVal: Math.round(vRoe65 - vEngine),
    },
    {
      name: '借入金利 +1%', // lint-ok: 指示書の確定値
      posVal: null,
      negVal: parseDiff('val.sens.借入金利が1%上昇(EPS −11%).diff'),
    },
    {
      name: '電材の販売数量 ±30t', // lint-ok: 指示書の確定値
      posVal: parseDiff('val.sens.電材の販売数量 +30t(EPS +8%).diff'),
      negVal: parseDiff('val.sens.電材の販売数量 −30t(EPS −8%).diff'),
    },
  ];

  const centerX = 4.2;
  const scale = 0.0070; // 1円 = 0.0070in 程度
  const startY = 2.12;
  const rowH = 0.42;
  const rowGap = 0.22;
  const labelColW = 1.65; // 行の名前の列幅 (x: 0.5 〜 2.15)
  const gridH = (rowH + rowGap) * 4 - rowGap;

  // 中心の縦線 (基準 1,022円)
  s.addShape('line', {
    x: centerX,
    y: startY - 0.06,
    w: 0.001,
    h: gridH + 0.12,
    line: { color: C.rule, width: 1.0, dashType: 'dash' },
    objectName: 'ovl_center_line',
  });

  // 中心線の注記 (縦線の下端)
  L.text(s, '基準 0円 (1,022円)', { // lint-ok: 基準線の目盛
    x: centerX - 0.9,
    y: startY + gridH + 0.08,
    w: 1.8,
    h: 0.22,
    fontSize: 8.5,
    color: C.sub,
    align: 'center',
    objectName: 'ovl_center_lbl',
  });

  rows.forEach((r, idx) => {
    const curY = startY + idx * (rowH + rowGap);

    // 行の名前 (棒の左外、右寄せ)
    L.text(s, r.name, {
      x: 0.5,
      y: curY,
      w: labelColW,
      h: rowH,
      fontSize: 8.5,
      color: C.dark,
      align: 'right',
      valign: 'middle',
      margin: 0,
      objectName: `row_name_${idx}`,
    });

    // 左側 (マイナス) 棒
    if (r.negVal !== null && r.negVal !== 0) {
      const absNeg = Math.abs(r.negVal);
      const barW = absNeg * scale;
      const barX = centerX - barW;
      L.box(s, barX, curY, barW, rowH, { fill: C.sub, line: C.sub, name: `ovl_neg_bar_${idx}` });

      const negStr = `−${Math.round(absNeg)}`;
      const numW = 0.44;
      L.text(s, negStr, {
        x: barX - numW - 0.04,
        y: curY,
        w: numW,
        h: rowH,
        fontSize: 9,
        bold: true,
        color: C.sub,
        align: 'right',
        valign: 'middle',
        margin: 0,
        objectName: `neg_num_${idx}`,
      });
    }

    // 右側 (プラス) 棒
    if (r.posVal !== null && r.posVal > 0) {
      const barW = r.posVal * scale;
      L.box(s, centerX, curY, barW, rowH, { fill: C.primary, line: C.primary, name: `ovl_pos_bar_${idx}` });

      const posStr = `+${Math.round(r.posVal)}`;
      L.text(s, posStr, {
        x: centerX + barW + 0.06,
        y: curY,
        w: 0.50,
        h: rowH,
        fontSize: 9,
        bold: true,
        color: C.primary,
        align: 'left',
        valign: 'middle',
        margin: 0,
        objectName: `pos_num_${idx}`,
      });
    }
  });

  // 左下 y5.0〜6.72: L.bullets(9pt)
  L.bullets(
    s,
    [
      `粗利率1ptの営業利益は ${F('gm.sens_op')}。電材の1tあたり営業利益(推定)で割ると ${F('calc.gm1_tons')}、ほぼ二期増設(${F('cap.ep2_capacity')})1つ分`,
      '粗利率を動かすのは製品構成と採算是正(第2・3章)。\n電材の増設と同じ重さで、汎用品の値上げと高付加価値品の数量を見る',
      '判別KPIの最上位を粗利率に置くのはこのため(投資行動のページ)',
    ],
    {
      x: 0.5,
      y: 4.95,
      w: 7.4,
      h: 1.75,
      fontSize: 9,
      gap: 4,
    }
  );

  // 右 x8.15 w4.68: L.paneHead('上値の源泉: 同業との粗利率の差')
  L.paneHead(s, 8.15, 1.62, 4.68, '上値の源泉: 同業との粗利率の差');

  const barChartData = [
    {
      name: '売上総利益率',
      labels: ['東邦化学', '業態の近い2社の平均'],
      values: [F.v('fy26.gross_margin'), F.v('peer2.gm')],
    },
  ];

  s.addChart(
    pres.charts.BAR,
    barChartData,
    L.chartStyle({
      x: 8.15,
      y: 1.98,
      w: 4.68,
      h: 2.30,
      valAxisMinVal: 0,
      showValue: true,
      dataLabelPosition: 'outEnd',
      dataLabelFormatCode: '0.0"%"',
      chartColors: [C.sub, C.primary],
      objectName: 'chart_peer_gm',
    })
  );

  // その下 L.kpiTiles 1枚(w4.68、h1.25)
  L.kpiTiles(
    s,
    [
      {
        value: `+${F.n('gap2.gm_third_eps')}円`,
        label: '差の3分の1が埋まった場合のEPSの増加',
        note: `差は ${F('gap2.gm_pt')}。いまの実力EPS ${F('fy27.core_eps')} に匹敵`,
      },
    ],
    {
      x: 8.15,
      y: 4.38,
      w: 4.68,
      h: 1.35,
    }
  );

  // その下 L.text(8.8pt)
  L.text(
    s,
    '基準シナリオは粗利率を5年で約1pt(16.0→16.9%)しか上げていない。\n差の大半は上値として残っている', // lint-ok: 指示書の確定値
    {
      x: 8.15,
      y: 5.86,
      w: 4.68,
      h: 0.55,
      fontSize: 8.8,
      color: C.sub,
      objectName: 'txt_peer_note',
    }
  );
};
