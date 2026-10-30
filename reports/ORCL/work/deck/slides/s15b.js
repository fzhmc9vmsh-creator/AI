// 2-7 資金と信用(2/2): FCF の橋渡しと更新の山(第4.5版)。左: 会社の資金の橋渡し(滝の図)。右: FCF と capex(FY27〜FY34・FY37)。下: 読み取り 3 点
// 滝の図は addChart の積み上げ棒(透明な土台 + 増加 + 減少 + 両端の合計)。プロット領域の位置を固定し、値と項目名は同じ座標で重ねて描く
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 約 6GW の建設資金(自己資金なら 2,200 億ドル)が何で減り、最後に 200 億ドルが残る道筋。右: FCF と capex の経路(ベース)と FY36〜37 の更新の山',
    source: 'Investor Day 2026-10-28(CFO 資料 p.18・26・28)、需給エンジン第4.5版(calc/out/m10_all.json)',
  });
  const fmt = (n) => String(Math.abs(n)).replace(/\B(?=(\d{3})+(?!\d))/g, ',');

  // ---------- 左: 会社の資金の橋渡し(滝の図)----------
  L.paneHead(s, 0.5, 1.62, 5.9, '会社の資金の橋渡し(Q2 FY27〜Q4 FY28、億ドル)');
  const steps = [
    { cat: '約 6GW の\n建設', kind: 'total', v: 2200, txt: '2,200', color: C.dark },
    { cat: 'ベンダー\n金融', kind: 'delta', v: -380 },
    { cat: 'BYOH', kind: 'delta', v: -380 },
    { cat: '前払い', kind: 'delta', v: -380 },
    { cat: 'その他の\n営業 CF', kind: 'delta', v: -860 },
    { cat: '最後の\n調達', kind: 'total', v: 200, txt: '200', color: C.dark },
  ];
  const wbox = { x: 0.5, y: 1.97, w: 5.9, h: 3.15 };
  const wlay = { x: 0.04, y: 0.1, w: 0.92, h: 0.7 };
  const WMIN = 0, WMAX = 2400, WGAP = 40;
  const base = [], up = [], down = [], tot = [], lv = [];
  let cur = 0;
  steps.forEach(st => {
    if (st.kind === 'total') { base.push(0); up.push(0); down.push(0); tot.push(st.v); lv.push([st.v, st.v]); cur = st.v; return; }
    const a = cur, b = cur + st.v;
    base.push(Math.min(a, b)); up.push(st.v > 0 ? st.v : 0); down.push(st.v < 0 ? -st.v : 0); tot.push(0);
    lv.push([a, b]); cur = b;
  });
  const wcats = steps.map(st => st.cat.replace('\n', ''));
  s.addChart(pres.charts.BAR, [
    { name: '土台', labels: wcats, values: base },
    { name: '増加', labels: wcats, values: up },
    { name: '減少', labels: wcats, values: down },
    { name: '合計', labels: wcats, values: tot },
  ], L.chartStyle(Object.assign({}, wbox, {
    objectName: 'chart_bridge', barDir: 'col', barGrouping: 'stacked', barGapWidthPct: WGAP, layout: wlay,
    chartColors: ['transparent', C.primary, C.light, C.dark], showValue: false, showLegend: false,
    valAxisMinVal: WMIN, valAxisMaxVal: WMAX, valAxisHidden: true, valGridLine: { style: 'none' }, catAxisLabelPos: 'none',
  })));
  {
    const px = wbox.x + wlay.x * wbox.w, py = wbox.y + wlay.y * wbox.h, pw = wlay.w * wbox.w, ph = wlay.h * wbox.h;
    const slot = pw / steps.length, bw = slot / (1 + WGAP / 100);
    const yOf = (v) => py + (1 - (v - WMIN) / (WMAX - WMIN)) * ph;
    const xc = (i) => px + slot * (i + 0.5);
    steps.forEach((st, i) => {
      const top = Math.max(lv[i][0], lv[i][1]);
      const txt = st.kind === 'total' ? st.txt : '−約 ' + fmt(st.v);
      L.text(s, txt, { x: xc(i) - slot / 2, y: yOf(top) - 0.22, w: slot, h: 0.2, fontSize: 9.5, bold: true, color: st.kind === 'total' ? C.dark : C.primary, align: 'center', valign: 'bottom', margin: 0, objectName: 'ovl_br_val' + i });
      L.text(s, st.cat, { x: xc(i) - slot / 2, y: py + ph + 0.06, w: slot, h: 0.36, fontSize: 8.5, color: C.text, align: 'center', valign: 'top', margin: 0, objectName: 'ovl_br_cat' + i });
      if (i < steps.length - 1) s.addShape('line', { x: xc(i) + bw / 2, y: yOf(lv[i][1]), w: slot - bw, h: 0.001, line: { color: C.sub, width: 0.5, dashType: 'sysDash' }, objectName: 'ovl_br_conn' + i });
    });
  }
  L.text(s, 'ベンダー金融・BYOH・前払いの額は図の目盛からの概算(各 350〜400 億ドル)。\n3 項目は各 380 億ドル、その他の営業 CF は 860 億ドルと置き、残りが 200 億ドルになるようにした', {
    x: 0.5, y: 5.14, w: 5.9, h: 0.36, fontSize: 8, color: C.sub, margin: 0, objectName: 'note_bridge',
  });

  // ---------- 右: FCF と capex(FY27〜FY34)----------
  L.paneHead(s, 6.75, 1.62, 6.08, 'FCF と capex(ベース、億ドル)');
  const yrs = ['FY27', 'FY28', 'FY29', 'FY30', 'FY31', 'FY32', 'FY33', 'FY34', 'FY37'];
  const fcf = [-484, -166, 399, 471, 446, 676, 887, 689, -434];
  const capex = [1072, 844, 474, 599, 791, 671, 553, 695, 2033];
  const cbox = { x: 6.75, y: 1.97, w: 6.08, h: 3.5 };
  const clay = { x: 0.04, y: 0.15, w: 0.94, h: 0.62 };
  const CMIN = -1000, CMAX = 2500, CGAP = 10;
  s.addChart(pres.charts.BAR, [
    { name: 'FCF', labels: yrs, values: fcf },
    { name: 'capex', labels: yrs, values: capex },
  ], L.chartStyle(Object.assign({}, cbox, {
    objectName: 'chart_fcf', barDir: 'col', barGrouping: 'clustered', barGapWidthPct: CGAP, layout: clay,
    chartColors: [C.primary, 'BFBFBF'], showValue: false, showLegend: true, legendPos: 'b',
    valAxisMinVal: CMIN, valAxisMaxVal: CMAX, valAxisMajorUnit: 500, valAxisHidden: true, valGridLine: { style: 'none' },
  })));
  {
    const px = cbox.x + clay.x * cbox.w, py = cbox.y + clay.y * cbox.h, pw = clay.w * cbox.w, ph = clay.h * cbox.h;
    const slot = pw / yrs.length, bw = slot / (2 + CGAP / 100);
    const yOf = (v) => py + (1 - (v - CMIN) / (CMAX - CMIN)) * ph;
    const xc = (i) => px + slot * (i + 0.5);
    const bx = (i, j) => xc(i) - bw + (j + 0.5) * bw;   // 2 本の棒の中心
    // 値ラベルの箱は棒の幅(bw)に収め、隣の棒のラベルと横に重ならないようにする。折り返しは切る(wrap: false)
    const lw = bw - 0.02;
    yrs.forEach((fy, i) => {
      const neg = fcf[i] < 0;
      const t1 = (neg ? '−' : '+') + fmt(fcf[i]);
      // FCF: 正の値は緑の棒の中の上端(白)、負の値は棒の下(赤)
      L.text(s, t1, { x: bx(i, 0) - lw / 2, y: neg ? yOf(fcf[i]) + 0.02 : yOf(fcf[i]) + 0.03, w: lw, h: 0.18, fontSize: 8, bold: true, color: neg ? C.red : C.white, align: 'center', valign: 'top', margin: 0, wrap: false, objectName: 'ovl_fcf_v' + i });
      // capex: 灰の棒の上
      L.text(s, fmt(capex[i]), { x: bx(i, 1) - lw / 2, y: yOf(capex[i]) - 0.2, w: lw, h: 0.18, fontSize: 8, color: C.sub, align: 'center', valign: 'bottom', margin: 0, wrap: false, objectName: 'ovl_cap_v' + i });
    });
    // FY36〜37 の札(更新の山)
    const tw = 2.9, tx = Math.min(xc(8) - tw / 2, cbox.x + cbox.w - tw), ty = cbox.y + 0.02;
    s.addShape('roundRect', { x: tx, y: ty, w: tw, h: 0.36, fill: { color: C.red }, line: { color: C.red }, rectRadius: 0.05, objectName: 'ovl_peak_tag' });
    L.text(s, '更新の山は FY36〜37(再契約しだい)\n再契約が続くため後ろへずれる', { x: tx, y: ty, w: tw, h: 0.4, fontSize: 8, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0, objectName: 'ovl_peak_tag_t' });
    s.addShape('line', { x: xc(8), y: ty + 0.36, w: 0.001, h: yOf(2033) - 0.22 - ty - 0.36, line: { color: C.red, width: 1, dashType: 'dash' }, objectName: 'ovl_peak_lead' });
  }

  // ---------- 下: 読み取り 3 点 ----------
  L.bullets(s, [
    'FY29 の FCF は利益率でなく、容量の頭打ちから出る(capex 1,072 億 → 474 億ドル)',
    'ベンダー金融は借入の別名で、会社も純負債に含める。会社の FCF は元本返済の前の数字。\n資金負担を本当に減らすのは BYOH と前払い',
    '更新の山は再契約しだい: 再契約が続けば FY36〜37 に後ろへずれる。\n単価 ±20% で DCF ±35 ドル(FY37 capex 2,033 億ドル・FCF −434 億ドル)',
  ], { x: 0.5, y: 5.65, w: 12.33, h: 1.15, fontSize: 11.5, gap: 5 });
  return s;
};
