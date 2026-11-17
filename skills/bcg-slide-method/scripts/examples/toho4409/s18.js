// s18 投資行動
module.exports = function build(pres, L) {
  const { F, C } = L;
  const s = L.contentSlide(pres, {
    source: 'valuate.py のエントリー圏(Z1=即時、Z2=分割)、決算短信、本分析。判定は報告のためのもので、売買の指示ではない',
  });

  // 左: 価格の梯子
  L.paneHead(s, 0.5, 1.62, 3.9, '価格の梯子(円)');

  // 数直線の座標定義
  const pMin = 500, pMax = 1250;
  const yTop = 2.15, yBot = 6.45;
  const totalH = yBot - yTop;
  const py = (p) => yBot - ((p - pMin) / (pMax - pMin)) * totalH;

  const z1Val = parseFloat(F.n('val.entry.Z1'));
  const z2Val = parseFloat(F.n('val.entry.Z2'));
  const pxVal = F.v('px.close');
  const crashVal = parseFloat(F.n('val.crash'));
  const bearVal = parseFloat(F.n('val.scen.bear.value'));
  const engineVal = parseFloat(F.n('val.value.engine'));
  const evVal = parseFloat(F.n('val.scen.ev'));

  const yZ1 = py(z1Val);
  const yZ2 = py(z2Val);

  // 帯の描画 (x: 0.6, w: 0.85)
  const bx = 0.6, bw = 0.85;

  // Z2以上 (上値・保有圏)
  L.box(s, bx, yTop, bw, yZ2 - yTop, {
    fill: C.tint, line: C.rule, name: 'ovl_band_tint',
  });
  s.addText('上値・保有圏', {
    x: bx, y: yTop + 0.1, w: bw, h: 0.25,
    fontFace: 'Meiryo UI', fontSize: 8.5, color: C.sub, align: 'center', margin: 0,
    objectName: 'ovl_band_tint_t',
  });

  // Z1〜Z2 (分割圏)
  L.box(s, bx, yZ2, bw, yZ1 - yZ2, {
    fill: C.light, line: C.rule, name: 'ovl_band_light',
  });
  s.addText('分割圏', {
    x: bx, y: (yZ1 + yZ2) / 2 - 0.12, w: bw, h: 0.24,
    fontFace: 'Meiryo UI', fontSize: 8.5, bold: true, color: C.dark, align: 'center', margin: 0,
    objectName: 'ovl_band_light_t',
  });

  // Z1以下 (即時圏)
  L.box(s, bx, yZ1, bw, yBot - yZ1, {
    fill: C.primary, line: C.rule, name: 'ovl_band_primary',
  });
  s.addText('即時圏', {
    x: bx, y: (yBot + yZ1) / 2 - 0.12, w: bw, h: 0.24,
    fontFace: 'Meiryo UI', fontSize: 8.5, bold: true, color: C.white, align: 'center', margin: 0,
    objectName: 'ovl_band_primary_t',
  });

  // 数直線の軸線
  s.addShape('line', {
    x: bx + bw, y: yTop, w: 0.001, h: totalH,
    line: { color: C.rule, width: 1.5 },
    objectName: 'ovl_axis_line',
  });

  // 目盛りとラベル
  // 重なりを避けるため、各ラベルのyオフセットを調整
  const labels = [
    { p: evVal, text: `${Math.round(evVal).toLocaleString('en-US')}円 期待値(EV)`, yOff: 0, bold: true, color: C.dark },
    { p: engineVal, text: `${Math.round(engineVal).toLocaleString('en-US')}円 事業エンジン`, yOff: 0, bold: true, color: C.primary },
    { p: bearVal, text: `${Math.round(bearVal)}円 弱気の価値`, yOff: -0.12, bold: false, color: C.text },
    { p: z2Val, text: `${Math.round(z2Val)}円 分割の上限(Z2)`, yOff: 0.12, bold: false, color: C.sub },
    { p: z1Val, text: `${Math.round(z1Val)}円 即時圏の上限(Z1)`, yOff: -0.12, bold: false, color: C.sub },
    { p: pxVal, text: `${pxVal}円 現在値`, yOff: 0.12, bold: true, color: C.red },
    { p: crashVal, text: `${Math.round(crashVal)}円 2022年型下振れ`, yOff: 0, bold: false, color: C.darkred },
  ];

  labels.forEach((it, idx) => {
    const actY = py(it.p);
    const textY = actY + it.yOff - 0.11;

    // 目盛りティック
    s.addShape('line', {
      x: bx + bw - 0.05, y: actY, w: 0.12, h: 0.001,
      line: { color: it.color === C.red ? C.red : C.sub, width: it.color === C.red ? 2 : 1 },
      objectName: `ovl_tick_${idx}`,
    });

    // 引出線(オフセットがある場合)
    if (Math.abs(it.yOff) > 0.02) {
      s.addShape('line', {
        x: bx + bw + 0.07, y: actY, w: 0.08, h: Math.abs(it.yOff) || 0.001,
        flipV: it.yOff < 0,
        line: { color: C.rule, width: 0.75, dashType: 'dash' },
        objectName: `ovl_guide_${idx}`,
      });
    }

    // ラベル文字
    s.addText(it.text, {
      x: bx + bw + 0.18, y: textY, w: 2.3, h: 0.24,
      fontFace: 'Meiryo UI', fontSize: 8.8, bold: it.bold, color: it.color,
      valign: 'middle', margin: 0, isTextBox: true,
      objectName: `ovl_lbl_${idx}`,
    });
  });

  // 現在値の赤い三角マーカー
  const curY = py(pxVal);
  s.addShape('rightArrow', {
    x: bx - 0.18, y: curY - 0.08, w: 0.15, h: 0.16,
    fill: { color: C.red }, line: { color: C.red },
    objectName: 'ovl_cur_marker',
  });
  // 現在値の横線
  s.addShape('line', {
    x: bx, y: curY, w: bw, h: 0.001,
    line: { color: C.red, width: 2 },
    objectName: 'ovl_cur_line',
  });

  // 右上: 判別のKPI
  L.paneHead(s, 4.65, 1.62, 8.18, '判別のKPI(続行と撤退の線)');
  const kpiRows = [
    ['日付', '見るもの', '続行', '見直し'],
    [
      '2027年2月4日',
      '第3四半期の売上総利益率と\nセグメント利益率',
      `粗利率が前年下期の ${F('calc.fy26_h2_gm')} 前後\n(通期 ${F('calc.fy27_op_gm_fy26h2')} 規模)`,
      `会社予想の下期前提 ${F('fy27.guid_h2_gm')} を下回り、\n利益率が2四半期続けて下がる`,
    ],
    [
      '2027年5月13日',
      '製品在庫日数、2028年3月期の\n計画、還元方針',
      `製品在庫日数が ${F('mfg.fg_days')} から短くなる。\n営業利益${F.n('mp.fy28_op')}百万円以上の計画`, // lint-ok: 指示書の確定値
      '在庫日数が伸びる。\n還元が返済のみ',
    ],
    [
      '2027年中',
      '電材二期の立ち上げ\n(SCの利益)',
      `SCの上期利益 ${F('fy27h1.seg_spec_profit')} を\n上回るペース`,
      'SCの利益が横ばい',
    ],
    [
      '随時',
      '自己株取得・政策保有株の売却・\n社長交代',
      '資本の返還が始まる。\n後継が変革の推進役から出る',
      '後継が外部から変革と無関係に\n選ばれる',
    ],
  ];

  L.table(s, kpiRows, {
    x: 4.65, y: 1.98, w: 8.18,
    colW: [1.3, 2.2, 2.3, 2.38],
    fontSize: 8.8,
    rowH: 0.60,
    align: ['center', 'left', 'left', 'left'],
  });

  // 右下: 4つのフェーズ
  L.paneHead(s, 4.65, 5.20, 8.18, '4つのフェーズ');

  const phases = [
    {
      title: '①今: 即時圏で打診',
      body: `株価 ${Math.round(parseFloat(F.n('val.entry.Z1')))}円以下。売買代金は\n1日 ${F('px.turnover')}。数週間に分けて買う`,
    },
    {
      title: '②2月4日',
      body: '粗利率の維持を確認して\n本格保有',
    },
    {
      title: '③5月13日',
      body: '在庫日数と還元方針で\n保有を継続',
    },
    {
      title: '④見直し',
      body: `見直しの線に2つ該当、または\n${Math.round(parseFloat(F.n('val.value.engine'))).toLocaleString('en-US')}円を超えて\n上値が小さくなったとき`,
    },
  ];

  const pw = 1.93;
  const pgap = (8.18 - pw * 4) / 3;
  const pTop = 5.56, pH = 1.05;

  phases.forEach((ph, i) => {
    const px = 4.65 + i * (pw + pgap);
    L.box(s, px, pTop, pw, pH, {
      fill: i === 0 ? C.tint : C.white,
      line: i === 0 ? C.primary : C.rule,
      lw: i === 0 ? 1.25 : 0.75,
      name: `ovl_ph_box_${i}`,
    });

    s.addText(ph.title, {
      x: px + 0.08, y: pTop + 0.10, w: pw - 0.16, h: 0.28,
      fontFace: 'Meiryo UI', fontSize: 9.5, bold: true,
      color: i === 0 ? C.primary : C.dark, align: 'center', margin: 0,
      objectName: `ovl_ph_title_${i}`,
    });

    s.addText(ph.body, {
      x: px + 0.06, y: pTop + 0.38, w: pw - 0.12, h: 0.60,
      fontFace: 'Meiryo UI', fontSize: 8.8,
      color: C.text, align: 'center', valign: 'middle', margin: 0,
      objectName: `ovl_ph_body_${i}`,
    });

    // 矢印
    if (i < 3) {
      s.addShape('rightArrow', {
        x: px + pw + 0.02, y: pTop + pH / 2 - 0.12, w: pgap - 0.04, h: 0.24,
        fill: { color: C.light }, line: { color: C.light },
        objectName: `ovl_ph_arr_${i}`,
      });
    }
  });
};
