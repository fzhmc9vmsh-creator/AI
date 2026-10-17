// 構造的要因サマリー T17(指示書 spec/ch1_ch4a.md の s06 節)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    title: 'DB の切替コストと前払い・長期リースの資金構造が評価を押し上げ、AI 容量の商品性と OpenAI 集中が押し下げる',
    kicker: '構造的要因サマリー: 構造(だから)→ 条件の評価(となり)→ 構造評価への効き(を動かした)',
    source: '本資料 第3章、需給エンジン第4.3版',
    page: 6,
  });

  const up = [
    { conds: [['1', 'B'], ['11', 'B'], ['12', 'A']], head: 'DB の切替コスト', body: '数十年続く保守・継続課金が土台になり、価格決定力と模倣困難性を支えて評価を上げた' },
    { conds: [['2', 'B'], ['13', 'B']], head: '前払い・長期リースの資金構造', body: 'GPU の一部と建屋の資金を顧客・パートナーに移し、自己資金の負担を軽くして評価を支えた' },
    { conds: [['3', 'A']], head: 'DB の AI 転用', body: 'OCI と Database@ が増収の主因になり、転用の成果として評価を上げた' },
  ];
  const down = [
    { conds: [['8', 'C']], head: 'AI 容量の商品性', body: '価値の 45% が需給緩和後に限界供給者の損益分岐で値決めされ、評価を下げた' },
    { conds: [['7', 'C']], head: 'OpenAI 集中と信用リスク', body: '受注残の約 45% が1社に集中し、CDS 227bp が示す実在のリスクが安さの主因になった' },
    { conds: [['2', 'B'], ['11', 'B']], head: '長期リースの固定費', body: '需要が鈍れば 15〜19 年の賃料が空室のまま残り、資金構造の利点の裏返しとして評価を抑えた' },
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

  // 右端の縦帯: 総合評価 B
  L.box(s, 10.75, 2.0, 2.08, 4.2, { fill: C.dark, line: C.dark, name: 'ovl_band' });
  L.badge(s, 10.75 + (2.08 - 1.4) / 2, 3.15, 'B', 1.4);
  L.text(s, '構造評価', { x: 10.75, y: 4.7, w: 2.08, h: 0.4, fontSize: 14, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0, objectName: 'band_label' });

  // カード列の右端から縦帯へ(上段は緑、下段は赤)
  L.arrow(s, 0.5 + 2 * (CW + GAP) + CW, 2.0 + CH / 2, 10.75, 2.0 + CH / 2, { color: C.primary, width: 1 });
  L.arrow(s, 0.5 + 2 * (CW + GAP) + CW, 4.35 + CH / 2, 10.75, 4.35 + CH / 2, { color: C.red, width: 1 });
};
