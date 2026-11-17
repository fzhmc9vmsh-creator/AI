// s12 ROEと資本の使い道
const M = require('../data/fwd_v3.json');

module.exports = function build(pres, L) {
  const { F, C } = L;
  const s = L.contentSlide(pres, {
    source: '決算短信、中期経営計画 p.12・p.23〜24、本分析の5年後モデルと valuate.py(定常ROEの交差確認)。電材の増設のROICは推定。デュポンは期中平均で計算',
  });

  // ==================== 左側 (x 0.5, w 6.3) ====================

  // 左上: ROEの分解(デュポン)
  L.paneHead(s, 0.5, 1.62, 6.3, 'ROEの分解(デュポン)— 利益率は上がるが、レバレッジが下がる');

  const net26 = F.v('fy26.net');
  const rev26 = F.v('fy26.revenue');
  const ast26 = F.v('fy26.assets');
  const eq26 = F.v('fy26.equity');

  const npm26 = (net26 / rev26) * 100;
  const turn26 = rev26 / ast26;
  const lev26 = ast26 / eq26;
  const roe26 = F('roe.fy26_dupont');

  const rows = [
    ['', '純利益率', '総資産回転', '財務レバレッジ', 'ROE'],
    ['26/3期 実績', `${npm26.toFixed(2)}%`, `${turn26.toFixed(2)}倍`, `${lev26.toFixed(2)}倍`, { text: roe26, options: { bold: true, color: C.text } }],
  ];

  // 28/3期 基準 〜 31/3期 基準
  const baseScen = M.scenarios['基準'];
  const years = ['28/3期 基準', '29/3期 基準', '30/3期 基準', '31/3期 基準'];
  for (let i = 1; i <= 4; i++) {
    const r = baseScen[i];
    const is31Base = i === 4;
    rows.push([
      years[i - 1],
      `${r.npm.toFixed(2)}%`,
      `${r.turnover.toFixed(2)}倍`,
      `${r.leverage.toFixed(2)}倍`,
      {
        text: `${r.roe.toFixed(2)}%`,
        options: { bold: true, color: is31Base ? C.red : C.text },
      },
    ]);
  }

  // 31/3期 弱気
  const bear31 = M.scenarios['弱気'][4];
  rows.push([
    '31/3期 弱気',
    `${bear31.npm.toFixed(2)}%`,
    `${bear31.turnover.toFixed(2)}倍`,
    `${bear31.leverage.toFixed(2)}倍`,
    { text: `${bear31.roe.toFixed(2)}%`, options: { bold: true, color: C.text } },
  ]);

  // 31/3期 強気
  const bull31 = M.scenarios['強気'][4];
  rows.push([
    '31/3期 強気',
    `${bull31.npm.toFixed(2)}%`,
    `${bull31.turnover.toFixed(2)}倍`,
    `${bull31.leverage.toFixed(2)}倍`,
    { text: `${bull31.roe.toFixed(2)}%`, options: { bold: true, color: C.text } },
  ]);

  L.table(s, rows, {
    x: 0.5,
    y: 1.98,
    w: 6.3,
    colW: [1.55, 1.15, 1.15, 1.15, 1.3],
    fontSize: 8.8,
    rowH: 0.26,
  });

  // 表の下のテキスト
  const r31Base = baseScen[4];
  const hypoRoe = r31Base.npm * r31Base.turnover * lev26;
  const diffPt = (hypoRoe - r31Base.roe).toFixed(1);
  L.text(
    s,
    `もしレバレッジが26/3期の水準のままなら、31/3期の基準のROEは ${hypoRoe.toFixed(1)}%。資本の積み上がりがROEを約${diffPt}ptも削る`,
    {
      x: 0.5,
      y: 4.14,
      w: 6.3,
      h: 0.38,
      fontSize: 9,
      color: C.dark,
      valign: 'middle',
      margin: 0,
    }
  );

  // 左下: ROE10%(中計の2030年度目標)に届く道
  L.paneHead(s, 0.5, 4.62, 6.3, 'ROE10%(中計の2030年度目標)に届く道');

  L.bullets(
    s,
    [
      `基準のままでは ${F('fwd.base.roe31')}。10%には ${F('roe.return_need')}(時価総額の${F.n('roe.return_need_mc')}%)の資本の返還が要る`,
      `その全額を株価 ${F('px.close')} で自己株取得すれば、31/3期のEPSは ${F('bb.eps31')}(+${F.n('bb.eps_up')}%)、ROE ${F('bb.roe31')}(返還額は純利益が変わらない前提の必要額。借入で賄うと金利の分だけ純利益が減り、10%に少し届かない)`,
      `中計の株主還元は3期で ${F('mp.return_plan')} 以上。この規模では届かない`,
      `返還の原資はB/Sの中にある: 製品在庫を同業並みに縮めれば ${F('gap2.fg_release')}、政策保有株 ${F('bs.inv_sec_fy26')}。合計 ${(F.v('gap2.fg_release') + F.v('bs.inv_sec_fy26')).toLocaleString('en-US')}百万円で、必要額を上回る`,
      `強気シナリオは政策保有株の売却(5年で${M.scenarios['強気'].reduce((a, r) => a + r.sec_sold, 0).toLocaleString('en-US')}百万円)と自己株取得(29/3期から年${M.scenarios['強気'][4].buyback}百万円)を置き、31/3期のROEは${M.scenarios['強気'][4].roe}%`,
    ],
    {
      x: 0.5,
      y: 4.98,
      w: 6.3,
      h: 1.75,
      fontSize: 8.6,
      gap: 2,
    }
  );

  // ==================== 右側 (x 7.05, w 5.78) ====================

  // 右上: 資本の使い道の利回り(税後)
  L.paneHead(s, 7.05, 1.62, 5.78, '資本の使い道の利回り(税後)');

  const roicVal = typeof F.v('em.roic_at') === 'number' ? F.v('em.roic_at') : 20;
  const chartData = [
    {
      name: '税後利回り',
      labels: ['電材の増設(ROIC)', '自己株取得(益回り)', '政策保有株(配当利回り)', '借入の返済(税後金利)'],
      values: [roicVal, F.v('bb.yield'), F.v('sec.yield'), F.v('debt.cost_at')],
    },
  ];

  s.addChart(
    pres.charts.BAR,
    chartData,
    L.chartStyle({
      x: 7.05,
      y: 1.98,
      w: 5.78,
      h: 2.05,
      barDir: 'bar',
      catAxisOrientation: 'maxMin', // 上から順に「電材の増設」「自己株取得」...にする
      chartColors: [C.primary, C.primary, C.sub, C.sub],
      valAxisMinVal: 0,
      showValue: true,
      dataLabelPosition: 'outEnd',
      dataLabelFormatCode: '0.0"%"',
    })
  );

  // チャートの下のテキスト
  L.text(s, `株主資本コスト ${F.n('val.coe')}。これを上回るのは上の2つだけ`, {
    x: 7.05,
    y: 4.14,
    w: 5.78,
    h: 0.24,
    fontSize: 8.8,
    color: C.dark,
    bold: true,
    valign: 'middle',
    margin: 0,
  });

  // 右下: ROEの経路が株価を分ける
  L.paneHead(s, 7.05, 4.46, 5.78, 'ROEの経路が株価を分ける');

  const enginePrice = Math.round(parseFloat(F.n('val.value.engine'))).toLocaleString('en-US');
  L.kpiTiles(
    s,
    [
      {
        value: `${F.n('val.roe65')}円`,
        label: '定常ROE 6.5%(返還なし)', // lint-ok: 指示書の確定値
        note: '現在値に対する上値が小さい',
        color: C.sub,
      },
      {
        value: `${enginePrice}円`,
        label: '定常ROE 9%(返還を半分織り込む)', // lint-ok: 指示書の確定値
        note: `現在値 ${F('px.close')}`,
        color: C.primary,
      },
    ],
    {
      x: 7.05,
      y: 4.75,
      w: 5.78,
      h: 1.45,
      gap: 0.20,
    }
  );

  // 一番下のテキスト(句点で改行して末行孤立を防ぐ)
  L.text(
    s,
    '判別の印: 自己株取得の決定と政策保有株の売却ペース。\n返済だけに使えば、利益が倍になっても株価は追いつかない',
    {
      x: 7.05,
      y: 6.28,
      w: 5.78,
      h: 0.42,
      fontSize: 9,
      color: C.text,
      valign: 'middle',
      margin: 0,
    }
  );
};
