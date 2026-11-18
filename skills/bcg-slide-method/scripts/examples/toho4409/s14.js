// s14 市場の織り込み(作り直し)
module.exports = function build(pres, L) {
  const { F, C } = L;
  const s = L.contentSlide(pres, {
    source: '同業は Yahoo!ファイナンス(PBR)・IRBANK(今期予想ROE)、2026年11月9日。花王・東京応化(ブランドと成長の上乗せ)とミヨシ油脂(一過性の利益)は除外。逆算は PBR=(ROE−g)/(r−g)。valuate.py の交差確認',
  });

  // 上段 y1.62〜3.2
  L.paneHead(s, 0.5, 1.62, 12.333, '市場との差分 — 安さの源泉は今のROE。ROEが上がる経路が値段に入っていない');

  const tiles = [
    {
      value: `ROE ${F.n('calc.implied_roe')}%`,
      label: '株価が織り込む永続ROE(成長2%・資本コスト8.25%)',
      note: `PBR ${F('calc.pbr_h1')} から逆算。実力は ${F('calc.core_roe_h1')}`,
    },
    {
      value: F('growth.price'),
      label: '成長の値段(時価総額 − 定常状態の価値)',
      note: `時価総額 ${F.n('px.mktcap')} < 定常状態の価値 ${F.n('steady.value')}(百万円)`,
    },
    {
      value: F('px.react_1028'),
      label: '上方修正(営業利益倍増)の翌日の株価',
      note: `カバレッジなし・外国人持株 ${F('px.foreign')}`,
    },
  ];

  L.kpiTiles(s, tiles, {
    x: 0.5,
    y: 1.98,
    w: 12.333,
    h: 1.45,
    gap: 0.25,
  });

  // 中段左 x0.5 w7.0: 散布図
  L.paneHead(s, 0.5, 3.50, 7.0, '同業7社のPBRとROE(今期予想、2026年11月9日)');

  // 散布図の座標計算
  // 軸: x = ROE 5〜15%(描画域 x1.0〜7.3)、y = PBR 0〜2.0倍(描画域 y5.75〜3.75、上が大きい)
  const xMin = 5.0, xMax = 15.0, xLeft = 1.0, xRight = 7.3;
  const yMin = 0.0, yMax = 2.0, yBottom = 5.75, yTop = 3.75;

  function xPos(roe) {
    return xLeft + ((roe - xMin) / (xMax - xMin)) * (xRight - xLeft);
  }
  function yPos(pbr) {
    return yBottom - ((pbr - yMin) / (yMax - yMin)) * (yBottom - yTop);
  }

  // 目盛り線と軸ラベル(C.rule の細線、軸ラベル 8.5pt)
  // x軸目盛り (5%, 7.5%, 10%, 12.5%, 15%)
  const xTicks = [5, 7.5, 10, 12.5, 15];
  xTicks.forEach(t => {
    const xp = xPos(t);
    // 縦グリッド線
    s.addShape('line', {
      x: xp, y: yTop, w: 0.001, h: yBottom - yTop,
      line: { color: C.rule, width: 0.5 },
      objectName: 'ovl_grid_x_' + t,
    });
    // x軸ラベル
    L.text(s, `${t}%`, {
      x: xp - 0.35, y: yBottom + 0.04, w: 0.7, h: 0.22,
      fontSize: 8.5, color: C.sub, align: 'center', margin: 0,
      objectName: 'ovl_lbl_x_' + t,
    });
  });

  // y軸目盛り (0.0, 0.5, 1.0, 1.5, 2.0)
  const yTicks = [0.0, 0.5, 1.0, 1.5, 2.0];
  yTicks.forEach(t => {
    const yp = yPos(t);
    // 横グリッド線
    s.addShape('line', {
      x: xLeft, y: yp, w: xRight - xLeft, h: 0.001,
      line: { color: C.rule, width: 0.5 },
      objectName: 'ovl_grid_y_' + t,
    });
    // y軸ラベル
    const labelY = t === 2.0 ? yp + 0.04 : yp - 0.08;
    L.text(s, `${t.toFixed(1)}倍`, {
      x: xLeft - 0.52, y: labelY, w: 0.46, h: 0.18,
      fontSize: 8.5, color: C.sub, align: 'right', valign: 'middle', margin: 0,
      objectName: 'ovl_lbl_y_' + t,
    });
  });

  // 回帰線: PBR = calc.line_a + calc.line_b × ROE を x5〜15 で引く(C.dark の点線)
  const a = F.v('calc.line_a');
  const b = F.v('calc.line_b');
  const pbrStart = a + b * xMin;
  const pbrEnd = a + b * xMax;
  const x1 = xPos(xMin);
  const y1 = yPos(pbrStart);
  const x2 = xPos(xMax);
  const y2 = yPos(pbrEnd);

  s.addShape('line', {
    x: Math.min(x1, x2),
    y: Math.min(y1, y2),
    w: Math.abs(x2 - x1) || 0.001,
    h: Math.abs(y2 - y1) || 0.001,
    flipH: x2 < x1,
    flipV: y2 < y1,
    line: { color: C.dark, width: 1.25, dashType: 'dash' },
    objectName: 'ovl_reg_line',
  });

  // 線の右端に 同業の線(決定係数 calc.line_r2)
  L.text(s, `同業の線(決定係数 ${F.n('calc.line_r2')})`, {
    x: x2 - 2.2,
    y: y2 - 0.25,
    w: 2.2,
    h: 0.22,
    fontSize: 8.5,
    bold: true,
    color: C.dark,
    align: 'right',
    margin: 0,
    objectName: 'ovl_reg_label',
  });

  // 点(直径0.13の円): 同業7社 = (peer3.X.roe_f, peer3.X.pbr)、X は dks sanyo nof nsk osaka nkk adeka。色 C.sub。
  // 各点の右に会社名(8pt、略称: 第一工業製薬・三洋化成・日油・日本精化・大阪有機・日本化学・ADEKA)。
  // 重なりを防ぐため、位置関係に応じてラベルの配置オフセットを微調整
  const peers = [
    { id: 'sanyo', name: '三洋化成', pos: 'top' },
    { id: 'nkk', name: '日本化学', pos: 'bottom' },
    { id: 'adeka', name: 'ADEKA', pos: 'right_up' },
    { id: 'nsk', name: '日本精化', pos: 'right_down' },
    { id: 'osaka', name: '大阪有機', pos: 'top' },
    { id: 'dks', name: '第一工業製薬', pos: 'right' },
    { id: 'nof', name: '日油', pos: 'right_down' },
  ];

  peers.forEach(p => {
    const roe = F.v(`peer3.${p.id}.roe_f`);
    const pbr = F.v(`peer3.${p.id}.pbr`);
    const xp = xPos(roe);
    const yp = yPos(pbr);
    const d = 0.13, r = d / 2;

    s.addShape('ellipse', {
      x: xp - r,
      y: yp - r,
      w: d,
      h: d,
      fill: { color: C.sub },
      line: { color: C.sub },
      objectName: 'ovl_peer_dot_' + p.id,
    });

    let lx = xp + r + 0.04;
    let ly = yp - 0.1;
    let align = 'left';
    let lw = 1.1;

    if (p.pos === 'top') {
      lx = xp - 0.55;
      ly = yp - r - 0.22;
      align = 'center';
    } else if (p.pos === 'bottom') {
      lx = xp + r + 0.04;
      ly = yp + 0.02;
      align = 'left';
    } else if (p.pos === 'right_up') {
      lx = xp + r + 0.04;
      ly = yp - 0.18;
      align = 'left';
    } else if (p.pos === 'right_down') {
      lx = xp + r + 0.04;
      ly = yp - 0.02;
      align = 'left';
    } else if (p.pos === 'right') {
      lx = xp + r + 0.04;
      ly = yp - 0.1;
      align = 'left';
    }

    L.text(s, p.name, {
      x: lx,
      y: ly,
      w: lw,
      h: 0.20,
      fontSize: 8,
      color: C.sub,
      align,
      margin: 0,
      objectName: 'ovl_peer_lbl_' + p.id,
    });
  });

  // 東邦化学 今 = (calc.core_roe_h1, calc.pbr_h1) を C.red の円(直径0.18)と '東邦化学(今)'。
  const tohoNowRoe = F.v('calc.core_roe_h1');
  const tohoNowPbr = F.v('calc.pbr_h1');
  const xpNow = xPos(tohoNowRoe);
  const ypNow = yPos(tohoNowPbr);
  const dNow = 0.18, rNow = dNow / 2;

  s.addShape('ellipse', {
    x: xpNow - rNow,
    y: ypNow - rNow,
    w: dNow,
    h: dNow,
    fill: { color: C.red },
    line: { color: C.red },
    objectName: 'ovl_toho_now_dot',
  });

  L.text(s, '東邦化学(今)', {
    x: xpNow - 1.25,
    y: ypNow - 0.1,
    w: 1.15,
    h: 0.22,
    fontSize: 8.5,
    bold: true,
    color: C.red,
    align: 'right',
    margin: 0,
    objectName: 'ovl_toho_now_lbl',
  });

  // 東邦化学 31/3期 基準 = (fwd.base.roe31 の数値, calc.line_pbr_31) を C.primary の白抜き円と '基準の31/3期'。
  const toho31Roe = F.v('fwd.base.roe31');
  const toho31Pbr = F.v('calc.line_pbr_31');
  const xp31 = xPos(toho31Roe);
  const yp31 = yPos(toho31Pbr);
  const d31 = 0.18, r31 = d31 / 2;

  s.addShape('ellipse', {
    x: xp31 - r31,
    y: yp31 - r31,
    w: d31,
    h: d31,
    fill: { color: C.white },
    line: { color: C.primary, width: 2 },
    objectName: 'ovl_toho_31_dot',
  });

  L.text(s, '基準の31/3期', {
    x: xp31 - 0.55,
    y: yp31 - r31 - 0.24,
    w: 1.1,
    h: 0.22,
    fontSize: 8.5,
    bold: true,
    color: C.primary,
    align: 'center',
    margin: 0,
    objectName: 'ovl_toho_31_lbl',
  });

  // 今→基準へ C.primary の矢印。
  L.arrow(s, xpNow + rNow + 0.02, ypNow - 0.02, xp31 - r31 - 0.02, yp31 + 0.02, {
    color: C.primary,
    width: 1.5,
  });

  // 中段右 x7.75 w5.08: L.paneHead('ROEが上がると、同業の線で株価はいくらか')
  L.paneHead(s, 7.75, 3.50, 5.08, 'ROEが上がると、同業の線で株価はいくらか');

  const tableRows = [
    ['', 'ROE', 'PBR', '株価(今のBPS)'],
    [
      '実力(今)',
      F('calc.core_roe_h1'),
      F('calc.line_pbr_now'),
      `${Math.round(F.v('calc.line_pbr_now') * F.v('fy27h1.bps')).toLocaleString('en-US')}円`,
    ],
    [
      '基準の31/3期',
      F('fwd.base.roe31'),
      F('calc.line_pbr_31'),
      {
        text: `${F.n('calc.line_px_31')}円`,
        options: { bold: true },
      },
    ],
    [
      '中計の目標',
      F('mp.fy31_roe'),
      F('calc.line_pbr_10'),
      `${F.n('calc.line_px_10')}円`,
    ],
  ];

  L.table(s, tableRows, {
    x: 7.75,
    y: 3.86,
    w: 5.08,
    colW: [2.0, 0.9, 0.95, 1.23],
    fontSize: 9,
    rowH: 0.31,
    name: 'tbl_roe_pbr',
  });

  // その下 L.bullets(9pt)
  L.bullets(
    s,
    [
      `今の株価 ${F('px.close')} は、今のROEでの同業の線(${Math.round(F.v('calc.line_pbr_now') * F.v('fy27h1.bps')).toLocaleString('en-US')}円)とほぼ同じ。割安の正体は、ROEの経路が織り込まれていないこと`,
      `基準のROEに乗れば同業の線で約${F.n('calc.line_px_31')}円。valuate.py の理論株価 ${Math.round(parseFloat(F.n('val.value.engine'))).toLocaleString('en-US')}円と近い(別の方法での交差確認)`,
    ],
    {
      x: 7.75,
      y: 5.22,
      w: 5.08,
      h: 0.82,
      fontSize: 9,
      name: 'bullets_right',
    }
  );

  // 一番下 L.takeaway(0.5, 6.12, 12.333, 0.58)
  L.takeaway(
    s,
    0.5,
    6.12,
    12.333,
    0.58,
    '市場が待っているのはROEの証拠。四半期の利益率と、資本の返還の決定が、値段を同業の線に沿って動かす'
  );
};
