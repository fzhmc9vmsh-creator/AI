// s11 段差の日付: 2026年6月〜2028年6月のロードマップと、段差の4つのピース
module.exports = function build(pres, L) {
  const C = L.C;
  const s = L.contentSlide(pres, {
    kicker: '外部の制度の日付(灰色)と、会社が決めた価格・課金の日付(緑)。次の試験は 2027 年 1 月の値上げ後の決算',
    source: '会社決算説明資料、厚労省告示74号',
  });

  L.paneHead(s, 0.5, 1.62, 12.33, '2026 年 6 月 → 2028 年 6 月の日付', 'pane_rm_head');
  const X0 = 1.0, X1 = 12.3, AY = 3.2, per = (X1 - X0) / 24;
  s.addShape('line', { x: X0 - 0.2, y: AY, w: X1 - X0 + 0.4, h: 0, line: { color: C.sub, width: 2 }, objectName: 'rm_axis' });
  [[0, '2026-06'], [6, '2026-12'], [12, '2027-06'], [18, '2027-12'], [24, '2028-06']].forEach(([m, lb]) => {
    s.addShape('line', { x: X0 + m * per, y: AY - 0.05, w: 0.001, h: 0.1, line: { color: C.sub, width: 1 }, objectName: `rm_tick${m}` });
    L.text(s, lb, { x: X0 + m * per - 0.4, y: AY + 0.07, w: 0.8, h: 0.18, fontSize: 8, color: C.sub, align: 'center', margin: 0, objectName: `rm_tl${m}` });
  });
  // m = 2026-06 からの月数、up = 軸の上に置く、co = 会社の決めた日付(緑)
  const ev = [
    { m: 0, up: true, d: '2026-06', t: '診療報酬改定\n(記録の電子化を要件化)' },
    { m: 1, up: false, d: '2026-07', t: 'AIルート課金 281件\n期末約400件目標', co: true },
    { m: 4, up: true, d: '2026-10', t: 'ボードPro\n無償提供', co: true },
    { m: 7, up: false, d: '2027-01', t: '基本料 +10%\nボードPro課金\n30,000円', co: true },
    { m: 8, up: true, d: '2027-02-12頃', t: '通期決算・\n中計のローリング', co: true },
    { m: 10, up: false, d: '2027-04', t: '介護報酬改定' },
    { m: 11, up: true, d: '2027-05-14頃', t: '1Q決算(値上げ後の\n解約・単価)', co: true },
    { m: 13, up: false, d: '2027-07', t: 'ボードPro 50,000円\n業界調査(新規開設)', co: true },
    { m: 24, up: true, d: '2028-06', t: '診療報酬改定' },
  ];
  const LW = 1.5;
  ev.forEach((e, i) => {
    const x = X0 + e.m * per, col = e.co ? C.primary : C.sub;
    const ly = e.up ? AY - 1.5 : AY + 0.42;
    s.addShape('line', { x, y: e.up ? AY - 0.4 : AY, w: 0.001, h: 0.4, line: { color: col, width: 1 }, objectName: `rm_st${i}` });
    s.addShape('ellipse', { x: x - 0.08, y: AY - 0.08, w: 0.16, h: 0.16, fill: { color: col }, line: { color: C.white, width: 1 }, objectName: `rm_dot${i}` });
    const lx = Math.min(Math.max(x - LW / 2, 0.5), 12.83 - LW);
    L.text(s, [{ text: e.d, options: { bold: true, breakLine: true, color: e.co ? C.dark : C.sub, fontSize: 10 } }, { text: e.t, options: { color: C.text, fontSize: 9 } }],
      { x: lx, y: ly, w: LW, h: 1.08, align: 'center', valign: e.up ? 'bottom' : 'top', margin: 0, objectName: `ovl_ev_t${i}` });
  });

  L.paneHead(s, 0.5, 4.6, 12.33, '段差を作る 4 つのピース', 'pane_pc_head');
  const g = (t) => ({ text: t, options: { color: C.primary, bold: true } });
  const r = (t) => ({ text: t, options: { color: C.red, bold: true } });
  L.table(s, [
    ['ピース', '動かす変数', '大きさ', '進捗'],
    ['基本料 +10%', '単価', '+1.8 千円/ST・年約 80 百万円', g('決定済み')],
    ['ボードPro', '単価', '年最大約 100 百万円', '無償期間'],
    ['AI付帯', '単価', '付帯 47% → 70% で +3 千円', '進行'],
    ['電子化要件', '獲得', '2024 年の前例で獲得 +24%', r('未確認')],
  ], { x: 0.5, y: 4.95, w: 12.33, colW: [2.3, 1.7, 5.6, 2.73], fontSize: 10.5, rowH: 0.36, name: 'tbl_pieces' });
};
