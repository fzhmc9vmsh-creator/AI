// 構造的要因サマリー(指示書 spec/ch1_ch4.md の s06 節。カード・縦帯・矢印は手本と同じ。第2版: 帯のバッジは 'B')
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '構造的要因サマリー: 構造(だから)→ 条件の評価(となり)→ 構造評価への効き(を動かした)',
    source: '本資料 第3章・第4章、calc/out/growth_v2.json',
  });

  const up = [
    { conds: [['1', 'B'], ['11', 'B']], head: '銀行免許 × フィンテックの安い調達', body: '会員の預金の約 97% が給与振込。\n負債は免許なしより 1.33pt 安く、\n節約は年 7.1 億ドル(販促費の 45%)' },
    { conds: [['3', 'B'], ['12', 'B']], head: '会員の厚みとクロスバイ', body: 'クロスバイは 1 年で 35% → 51%。\n既存会員の製品は 2.5 倍で、\n製品当たり獲得費は −15%' },
    { conds: [['2', 'B'], ['5', 'B']], head: '攻めの獲得投資と単位経済', body: '販促費 +48% は 6 検査中 4 つで攻め。\n経済的 LTV/CAC は約 2 倍、\n定常の ROTCE 約 15%' },
  ];
  const down = [
    { conds: [['13', 'C']], head: '自己資本の律速と買い手への依存', body: '自給率 0.34。LPB への配分は\n49% → 29% と逆方向で、\n2027 年に資本の下限で試される' },
    { conds: [['8', 'C']], head: 'ローンの商品性', body: 'ローンは買い手がほぼ額面と手数料で\n買う市場の商品で、金利帯も競合と\n重なり、利ざやを守りにくい' },
    { conds: [['7', 'C']], head: '金利に弱い評価と信用', body: '公正価値の割引率が金利に連動し、\n金利上昇でマークが下がる。景気後退\nなら貸倒も増える' },
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

  // 右端の縦帯: 総合評価 C
  L.box(s, 10.75, 2.0, 2.08, 4.2, { fill: C.dark, line: C.dark, name: 'ovl_band' });
  L.badge(s, 10.75 + (2.08 - 1.4) / 2, 3.15, 'B', 1.4);
  L.text(s, '構造評価', { x: 10.75, y: 4.7, w: 2.08, h: 0.4, fontSize: 14, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0, objectName: 'band_label' });

  // カード列の右端から縦帯へ(上段は緑、下段は赤)
  L.arrow(s, 0.5 + 2 * (CW + GAP) + CW, 2.0 + CH / 2, 10.75, 2.0 + CH / 2, { color: C.primary, width: 1 });
  L.arrow(s, 0.5 + 2 * (CW + GAP) + CW, 4.35 + CH / 2, 10.75, 4.35 + CH / 2, { color: C.red, width: 1 });
};
