// s04a 下期の試金石(新規)
module.exports = function build(pres, L) {
  const { F, C } = L;
  const s = L.contentSlide(pres, {
    source: '決算短信(2026年3月期・2027年3月期第2四半期)、決算説明資料 p.12。下期の粗利率は会社予想の営業利益から販管費を上期並みとして逆算(本分析)',
  });

  // ======================= 左: 上下2つのチャート =======================
  // 上: 売上総利益率(半期)
  L.paneHead(s, 0.5, 1.62, 6.2, '売上総利益率(半期)', 'pane_gm_head');

  const gmChartData = [
    {
      name: '売上総利益率',
      labels: ['26/3期 上期', '26/3期 下期', '27/3期 上期', '27/3期 下期(会社予想)'],
      values: [
        F.v('fy26h1.gross_margin'),
        F.v('calc.fy26_h2_gm'),
        F.v('fy27h1.gross_margin'),
        F.v('fy27.guid_h2_gm'),
      ],
    },
  ];

  s.addChart(pres.charts.BAR, gmChartData, L.chartStyle({
    x: 0.5,
    y: 1.95,
    w: 6.2,
    h: 1.85,
    valAxisMinVal: 12,
    showValue: true,
    dataLabelPosition: 'outEnd',
    dataLabelFormatCode: '0.00"%"',
    chartColors: [C.sub, C.sub, C.primary, C.light],
    objectName: 'chart_gm',
  }));

  // 下: 営業利益(半期、百万円)
  L.paneHead(s, 0.5, 3.95, 6.2, '営業利益(半期、百万円)', 'pane_op_head');

  const opChartData = [
    {
      name: '営業利益',
      labels: [
        '26/3期 上期',
        '26/3期 下期',
        '27/3期 上期',
        '27/3期 下期(予想)',
        '27/3期 下期(上期並み)',
      ],
      values: [
        F.v('fy26h1.op'),
        F.v('calc.fy26_h2_op'),
        F.v('fy27h1.op'),
        F.v('fy27.guid_h2_op'),
        F.v('fy27.guid_h2_op') + F.v('calc.h2_op_upside'),
      ],
    },
  ];

  s.addChart(pres.charts.BAR, opChartData, L.chartStyle({
    x: 0.5,
    y: 4.28,
    w: 6.2,
    h: 1.85,
    valAxisMinVal: 0,
    showValue: true,
    dataLabelPosition: 'outEnd',
    dataLabelFormatCode: '#,##0',
    catAxisLabelFontSize: 7,
    chartColors: [C.sub, C.sub, C.sub, C.light, C.primary],
    objectName: 'chart_op',
  }));

  // ======================= 右: 通期の営業利益と読み =======================
  // 下期の粗利率の判別表(百万円)
  L.paneHead(s, 6.95, 1.62, 5.88, '下期の粗利率で、通期の営業利益はこう変わる(百万円)', 'pane_fy_op_head');
  const hd = (t) => ({ text: t, options: { bold: true, color: C.white, fill: { color: C.dark } } });
  const em = (t) => ({ text: t, options: { bold: true, color: C.primary } });
  const opTableRows = [
    [hd('下期の粗利率'), hd('通期の営業利益'), hd('意味')],
    [`${F('fy27.guid_h2_gm')}(会社予想)`, F.n('fy27.guid_op'), '原料高をそのまま織り込む'],
    ['15.0%', F.n('calc.fy27_op_gm_150'), `中計目標(${F.n('mp.fy28_op')})を今期に超える`], // lint-ok: 判別表の刻み
    ['15.6%', F.n('calc.fy27_op_gm_156'), '値上げの効果が半分残る'], // lint-ok: 判別表の刻み
    [em(`${F('calc.fy26_h2_gm')}(前年下期)`), em(F.n('calc.fy27_op_gm_fy26h2')), em('値上げと構成の改善が定着')],
    [`${F('fy27h1.gross_margin')}(上期並み)`, F.n('calc.fy27_op_gm_h1'), '原料のピーク越えも効く'],
  ];
  L.table(s, opTableRows, {
    x: 6.95, y: 1.98, w: 5.88, colW: [1.9, 1.3, 2.68], fontSize: 9, rowH: 0.27,
    align: ['left', 'right', 'left'], name: 'tbl_fy_op',
  });

  // 読み
  L.paneHead(s, 6.95, 3.78, 5.88, '読み', 'pane_reading_head');
  L.bullets(s, [
    `下期の粗利率1ptで営業利益は ${F('calc.h2_op_per_pt')} 動く。会社予想の ${F('fy27.guid_h2_gm')} は上期より ${F('calc.h2_gm_gap')}、前年下期(${F('calc.fy26_h2_gm')})よりも低い`,
    `原料: 国産ナフサは4〜6月 ${F('mkt.naphtha_2026q2')}(+${F.n('calc.naphtha_q2_chg')}%)、7〜9月 ${F('mkt.naphtha_2026q3')}(${F('calc.naphtha_q3_chg')})。酸化エチレンも春に${F('mkt.eo_hike_nsk')}以上の値上げ。高値の原料は下期の原価に出るが、ピークは越えた`,
    '会社自身は「営業利益目標30億円の1年前倒しでの達成を目指す」(説明資料 p.12)(30億円=3,000百万円)。予想はその手前に置く', // lint-ok: 30億円は原文
  ], {
    x: 6.95, y: 4.12, w: 5.88, h: 1.92, fontSize: 8.8, gap: 3, name: 'bullets_reading',
  });

  // 一番下
  L.takeaway(s, 6.95, 6.12, 5.88, 0.58, '判別の最初の日は2027年2月4日。第3四半期の粗利率が前年下期並み(16%前後)なら、変化は持続している'); // lint-ok: 判別の線
};
