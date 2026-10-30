// 2-2 会社のシナリオ(3/3): 説明会で変わったこと(第4.5版)。左: 6 項目の表(前 → 後 → 評価への効き)。右: 理論株価の階段(滝の図)第4.3版 → 第4.5版
// 滝の図は addChart の積み上げ棒(透明な土台 + 増加 + 減少 + 両端の合計)。プロット領域の位置を固定し、値と項目名は同じ座標で重ねて描く
module.exports = function build(pres, L) {
  const { C, FONT } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 説明会(2026-10-28)の前後で変わった 6 項目と、理論株価への効き。右: 第4.3版 → 第4.5版 の理論株価の変化(説明会の資料と、利用者の指摘による変更)',
    source: 'Investor Day 2026-10-28(8-K Ex.99.1、CFO 資料 p.4・8・13・15〜20・26〜28)、需給エンジン第4.3〜4.5版(m9_waterfall.json・m10_fair.json、台帳 r8 A)',
  });

  // ---------- 左: 6 項目の表 ----------
  L.paneHead(s, 0.5, 1.62, 7.6, '説明会で変わった 6 項目と、理論株価への効き');
  const bold = (t) => ({ text: t, options: { bold: true, color: C.dark } });
  L.table(s, [
    ['項目', '説明会の前', '説明会(10/28)', '評価への効き'],
    [bold('FCF の黒字化'), 'S&P の条件は FY29、\nエンジンは FY30', 'FY28 下期に黒字化、\nFY29 に 300 億ドル以上', 'エンジンは FY29 399 億。\n容量の頭打ちで capex が減る'],
    [bold('追加調達'), '2026 年に 450〜500 億ドルの計画\n(ATM 200 億は Q1 で完了)', 'FY27〜30 に 200 億ドルが上限\n(株 100・債 100)', '株式 100 億 = 7,200 万株\n(希薄化 2.4%)'],
    [bold('容量'), '確保電力 10GW 超\n(エンジン FY30 14GW)', 'FY26 3GW → FY28 末 10GW、\nFY30 約 10GW', '容量の計画 −13.1 ドル'],
    [bold('1GW の経済性'), '未開示(エンジンは\n現金費用 27 億ドル/GW)', '売上 160 億・capex 370 億・\n粗利率 35%・契約 5 年', '単価 +6.5、粗利率 −19.0\n芯は再契約の単価\n(経営者: 同じか、より良い利益率)'],
    [bold('FY30 の目標'), '売上 2,250 億・EPS 21\n(FAM 2025)', '営業利益率 40%・営業利益\n900 億を追加', '会社の EPS を起点に\n+7.9 ドル'],
    [bold('信用の目標'), '—', '純負債/EBITDA 3.5 倍未満\n(ベンダー金融込み)', 'エンジンは FY29 2.4 倍'],
  ], { x: 0.5, y: 1.97, w: 7.6, colW: [1.05, 2.3, 2.3, 1.95], fontSize: 9, rowH: 0.57, align: ['left', 'left', 'left', 'left'] });

  // ---------- 右: 理論株価の階段(滝の図)第4.3版 → 第4.5版----------
  L.paneHead(s, 8.4, 1.62, 4.43, '理論株価の階段(ドル、確率加重)');
  const steps = [
    { cat: '第4.3版', kind: 'total', v: 250.5 },
    { cat: '説明会\nの資料', kind: 'delta', v: -14.6 },
    { cat: '第4.4版', kind: 'total', v: 235.9 },
    { cat: '立ち上げ', kind: 'delta', v: -0.8 },
    { cat: 'ERP\n移行', kind: 'delta', v: 2.3 },
    { cat: '推論の\n需要', kind: 'delta', v: 7.5 },
    { cat: '第4.5版', kind: 'total', v: 245.2 },
  ];
  const box = { x: 8.4, y: 1.97, w: 4.43, h: 3.5 };
  const lay = { x: 0.1, y: 0.06, w: 0.88, h: 0.74 };
  const MIN = 225, MAX = 255, GAP = 40;
  // 系列: 土台(透明)・増加・減少・合計
  const base = [], up = [], down = [], tot = [];
  let cur = 0;
  const lv = [];   // 各棒の [始点, 終点]
  steps.forEach(st => {
    if (st.kind === 'total') { base.push(0); up.push(0); down.push(0); tot.push(st.v); lv.push([st.v, st.v]); cur = st.v; return; }
    const a = cur, b = cur + st.v;
    base.push(Math.min(a, b)); up.push(st.v > 0 ? st.v : 0); down.push(st.v < 0 ? -st.v : 0); tot.push(0);
    lv.push([a, b]); cur = b;
  });
  const cats = steps.map(st => st.cat.replace('\n', ''));
  s.addChart(pres.charts.BAR, [
    { name: '土台', labels: cats, values: base },
    { name: '増加', labels: cats, values: up },
    { name: '減少', labels: cats, values: down },
    { name: '合計', labels: cats, values: tot },
  ], L.chartStyle(Object.assign({}, box, {
    objectName: 'chart_waterfall', barDir: 'col', barGrouping: 'stacked', barGapWidthPct: GAP, layout: lay,
    chartColors: ['transparent', C.primary, C.red, C.dark], showValue: false, showLegend: false,
    valAxisMinVal: MIN, valAxisMaxVal: MAX, valAxisMajorUnit: 10, catAxisLabelPos: 'none',
  })));
  // プロット領域の座標(inch)
  const px = box.x + lay.x * box.w, py = box.y + lay.y * box.h, pw = lay.w * box.w, ph = lay.h * box.h;
  const slot = pw / steps.length, bw = slot / (1 + GAP / 100);
  const yOf = (v) => py + (1 - (v - MIN) / (MAX - MIN)) * ph;
  const xc = (i) => px + slot * (i + 0.5);
  steps.forEach((st, i) => {
    const top = Math.max(lv[i][0], lv[i][1]);
    const txt = st.kind === 'total' ? st.v.toFixed(1) : (st.v > 0 ? '+' : '−') + Math.abs(st.v).toFixed(1);
    const col = st.kind === 'total' ? C.dark : (st.v > 0 ? C.primary : C.red);
    L.text(s, txt, { x: xc(i) - slot / 2, y: yOf(top) - 0.22, w: slot, h: 0.2, fontSize: 9, bold: true, color: col, align: 'center', valign: 'bottom', margin: 0, objectName: 'ovl_wf_val' + i });
    L.text(s, st.cat, { x: xc(i) - slot / 2, y: py + ph + 0.06, w: slot, h: 0.34, fontSize: 8, color: C.text, align: 'center', valign: 'top', margin: 0, objectName: 'ovl_wf_cat' + i });
    if (i < steps.length - 1) {
      const y = yOf(lv[i][1]);
      s.addShape('line', { x: xc(i) + bw / 2, y, w: slot - bw, h: 0.001, line: { color: C.sub, width: 0.5, dashType: 'sysDash' }, objectName: 'ovl_wf_conn' + i });
    }
  });
  L.text(s, '説明会の資料 −14.6 の内訳(足した順):市場の値 +3.2・\n容量 −13.1・1GW の単価 +6.5・粗利率 −19.0・資金 −0.2・\nEPS の起点 +7.9。縦軸は 225 ドルから。丸めのため、\n第4.5版の 245.2 は積み上げと 0.3 ずれる', {
    x: 8.4, y: 5.5, w: 4.43, h: 0.58, fontSize: 8, color: C.sub, margin: 0, valign: 'top', objectName: 'note_wf',
  });

  // ---------- 下: テイクアウェイ ----------
  L.takeaway(s, 0.5, 6.12, 12.33, 0.62, '説明会の資料で理論株価は −15 ドル、利用者の指摘(立ち上げ・ERP・推論)で +9 ドル。\n理論株価は 245 ドル(株価の 1.76 倍)');
  return s;
};
