// 2-3 収益構造(3/3): 1GW の経済性と IRR。左上: 3 つの資金調達の型の比較表。左下: IRR を更新のしかた別に(資本コストの線つき)。右: 仕組み ①〜④ と上がる/下がる条件
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左上: 会社が示した 1GW の例(資金調達の型別)。左下: 1GW の IRR(更新のしかた別)と資本コスト。右: 仕組みと、評価が動く条件',
    source: 'Investor Day 2026-10-28(CFO 資料 p.15〜22)、calc/m9_irr.py、需給エンジン第4.4版',
  });

  // ---------- 左上: 1GW の経済性(会社の例)----------
  L.paneHead(s, 0.5, 1.62, 8.5, '1GW の経済性(会社の例)');
  const bold = (t) => ({ text: t, options: { bold: true, color: C.dark } });
  L.table(s, [
    ['項目', '自己資金', 'ベンダー金融(ハードの 70%)', 'BYOH(顧客が GPU を持ち込む)'],
    [bold('年換算売上'), '160 億ドル', '160 億ドル', '110 億ドル'],
    [bold('最初の 2 年の capex'), '370 億ドル', '180 億ドル', '60 億ドル(ネットワークだけ)'],
    [bold('粗利率・営業利益率'), '35%・34%', '35%・34%', '35% 超・34% 超'],
    [bold('誰が GPU を負うか'), 'Oracle', 'Oracle(借入)', '顧客'],
  ], { x: 0.5, y: 1.97, w: 8.5, colW: [2.0, 1.6, 2.5, 2.4], fontSize: 9.5, rowH: 0.36, align: ['left', 'center', 'center', 'center'] });

  // ---------- 左下: IRR(更新のしかた別)----------
  L.paneHead(s, 0.5, 4.02, 8.5, 'IRR(更新のしかた別、%。四半期で計算)');
  // 横棒は先頭の項目が下になるので、見せたい順の逆に渡す
  const items = [
    ['更新なし(5 年で終わる)', 17.6],
    ['2 年更新・単価 60%', 21.5],
    ['2 年更新・単価 120%(会社の更新 +20%)', 26.6],
    ['capex +10%・更新なし', 15.7],
  ];
  const rev = items.slice().reverse();
  const box = { x: 0.5, y: 4.36, w: 8.5, h: 2.36 };
  const lay = { x: 0.34, y: 0.15, w: 0.62, h: 0.72 };
  const MAX = 30;
  s.addChart(pres.charts.BAR, [{ name: 'IRR(%)', labels: rev.map(r => r[0]), values: rev.map(r => r[1]) }], L.chartStyle(Object.assign({}, box, {
    objectName: 'chart_irr', barDir: 'bar', chartColors: [C.primary], layout: lay, barGapWidthPct: 45,
    dataLabelFormatCode: '0.0"%"', dataLabelFontBold: true, valAxisMinVal: 0, valAxisMaxVal: MAX, valAxisMajorUnit: 10, valAxisHidden: false,
    catAxisLabelFontSize: 9.5,
  })));
  // 資本コスト 約 10% の点線(プロット領域の座標で描く)
  const px = box.x + lay.x * box.w, py = box.y + lay.y * box.h, pw = lay.w * box.w, ph = lay.h * box.h;
  const xk = px + pw * 10 / MAX;
  s.addShape('line', { x: xk, y: py - 0.2, w: 0.001, h: ph + 0.2, line: { color: C.red, width: 1.25, dashType: 'dash' }, objectName: 'ovl_irr_wacc' });
  L.text(s, '資本コスト 約 10%', { x: xk + 0.08, y: py - 0.2, w: 1.5, h: 0.2, fontSize: 8.5, bold: true, color: C.red, margin: 0, valign: 'middle', objectName: 'ovl_irr_wacc_t' });
  L.text(s, 'AI 事業の資本コスト 約 9.6〜10.2%(無リスク金利 4.9〜5.5% + 1.10 × 4.23%)。どのケースでも上回る', {
    x: 0.5, y: 6.62, w: 8.5, h: 0.2, fontSize: 8.5, color: C.sub, margin: 0, valign: 'middle', objectName: 'note_irr',
  });

  // ---------- 右: 仕組み ----------
  L.mechPanel(s, {
    head: '仕組み(①〜④)', fontSize: 11,
    bottom: 6.7,
    mech: [
      'ROI 28% は利回り\n(1 年分の現金 ÷ 投資)で、\nIRR ではない。償却 6 年・\n現金費用 44 億ドル/GW と整合',
      '更新なしでも黒字\n5 年の契約だけで IRR 17.6%。\n資本コスト 約 10% を上回る',
      '芯は契約後の単価\n更新 ±20% で理論株価 +12 / −10、\nDCF +16 / −19 ドル',
      'コストプラス\n原価の上昇は顧客に転嫁\n(capex +10% でも 15.7%)。\n超過利益も取りにくい(条件8 C)',
    ],
    reason: '1GW は更新なしでも資本コストを\n上回る。価値の芯は契約後の更新単価',
    up: '4 年前の GPU の更新 +20% が続く',
    down: '逼迫が FY30 に解け、契約後の単価が 6 割に',
  });
  return s;
};
