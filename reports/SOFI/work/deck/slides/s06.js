// 構造的要因サマリー(指示書 spec/v3.md の s06 節。カード・縦帯・矢印は手本と同じ。帯のバッジは B)
// 押し下げは指示書どおり 2 項目(左から 2 枚。3 枚目の枠は空ける)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '構造的要因サマリー: 構造(だから)→ 条件の評価(となり)→ 構造評価への効き(を動かした)',
    source: '本資料 第3章・第4章、calc/out/growth_v3.json',
  });

  const up = [
    { conds: [['1', 'B'], ['11', 'B']], head: '主口座の関係と安い預金', body: '年 7.1 億ドルの節約。預金金利は\n同業より低くても預金は +54%' },
    { conds: [['1', 'B'], ['12', 'B']], head: 'クロスセルの加速', body: '製品 前年比 43%、\nクロスバイ 51%' },
    { conds: [['7', 'A'], ['8', 'B']], head: '同業より良い会員の質', body: '純償却 2.62%。同業は\n3.2〜4.2%' },
  ];
  const down = [
    { conds: [['2', 'B'], ['13', 'B']], head: '自己資本の律速', body: '自給率 0.34。比率は\n半年で −4.1pt' },
    { conds: [['6', 'A'], ['7', 'A']], head: '消費者金融の群として見られること', body: '株価が示す PEG 0.85\n(構造 C の水準)' },
  ];

  const CW = 3.1, GAP = 0.25, CH = 1.85;
  function card(c, i, y, tone) {
    const x = 0.5 + i * (CW + GAP);
    const upper = tone === 'up';
    L.box(s, x, y, CW, CH, { fill: upper ? C.tint : C.gray, line: upper ? C.light : C.red, name: 'ovl_card_' + tone + i });
    // 1 行目: 条件番号と評価のバッジ
    let bx = x + 0.1;
    L.text(s, '条件', { x: bx, y: y + 0.1, w: 0.4, h: 0.42, fontSize: 9.5, color: C.sub, valign: 'middle', margin: 0, objectName: `cn_${tone}${i}` });
    bx += 0.42;
    c.conds.forEach(([no, g], j) => {
      L.badge(s, bx, y + 0.1, g, 0.42);
      bx += 0.42 + 0.03;
      const nw = 0.12 + 0.09 * no.length;
      L.text(s, no, { x: bx, y: y + 0.1, w: nw, h: 0.42, fontSize: 9.5, bold: true, color: C.dark, valign: 'middle', margin: 0, objectName: `no_${tone}${i}_${j}` });
      bx += nw + 0.06;
    });
    // 2 行目: 構造の一言 / 3 行目: 因果の文
    L.text(s, c.head, { x: x + 0.1, y: y + 0.58, w: CW - 0.2, h: 0.3, fontSize: 11, bold: true, color: C.dark, valign: 'middle', margin: 0, objectName: `h_${tone}${i}` });
    L.text(s, c.body, { x: x + 0.1, y: y + 0.92, w: CW - 0.2, h: 0.85, fontSize: 9.5, margin: 0, objectName: `b_${tone}${i}` });
  }

  // 区画の見出し
  L.paneHead(s, 0.5, 1.62, 9.8, '押し上げ要因', 'head_up');
  L.text(s, '押し下げ要因', { x: 0.5, y: 3.97, w: 9.8, h: 0.32, fontSize: 12, bold: true, color: C.red, margin: 0, valign: 'middle', objectName: 'head_down' });
  up.forEach((c, i) => card(c, i, 2.0, 'up'));
  down.forEach((c, i) => card(c, i, 4.35, 'down'));

  // 右端の縦帯: 構造評価 B
  L.box(s, 10.75, 2.0, 2.08, 4.2, { fill: C.dark, line: C.dark, name: 'ovl_band' });
  L.badge(s, 10.75 + (2.08 - 1.4) / 2, 3.15, 'B', 1.4);
  L.text(s, '構造評価', { x: 10.75, y: 4.7, w: 2.08, h: 0.4, fontSize: 14, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0, objectName: 'band_label' });

  // カード列の右端から縦帯へ(上段は緑、下段は赤。下段は最後のカードの右端から)
  L.arrow(s, 0.5 + 2 * (CW + GAP) + CW, 2.0 + CH / 2, 10.75, 2.0 + CH / 2, { color: C.primary, width: 1 });
  L.arrow(s, 0.5 + (down.length - 1) * (CW + GAP) + CW, 4.35 + CH / 2, 10.75, 4.35 + CH / 2, { color: C.red, width: 1 });
};
