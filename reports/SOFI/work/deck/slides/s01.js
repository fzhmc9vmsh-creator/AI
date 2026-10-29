// 表紙(指示書 spec/v4.md の s01 節。部品 L.cover をそのまま使う)
// 右半分に結論の要点を縦に 3 つ置く(x 9.1, w 3.73)。小見出し 11pt 灰 + 値 26pt 太字 緑
module.exports = function build(pres, L) {
  const s = L.cover(pres, {
    title: 'SoFi Technologies(SOFI)\n長期保有適格性審査',
    sub: '銀行免許を持つフィンテック。会員の束で獲得費と資金を下げ、\n自己資本が成長を律速する。Q3 2026 決算と 2027 年見通しを反映',
    date: '2026-10-28(Q3 2026 決算後)',
  });
  const key = [
    { y: 2.0, head: '最終判断', value: '買い(分割)', name: 'bg_cover_k1' },
    { y: 3.3, head: '理論株価(エンジン)', value: '23.8 ドル', name: 'bg_cover_k2' },
    { y: 4.6, head: '構造評価', value: 'B', name: 'bg_cover_k3' },
  ];
  key.forEach(k => {
    L.text(s, k.head, { x: 9.1, y: k.y, w: 3.73, h: 0.3, fontSize: 11, color: L.C.sub, objectName: k.name });
    L.text(s, k.value, { x: 9.1, y: k.y + 0.32, w: 3.73, h: 0.6, fontSize: 26, bold: true, color: L.C.primary, objectName: k.name + 'v' });
  });
  L.text(s, '株価 14.55 ドル(10/16 終値)は理論株価の 0.61 倍。\n決算後の目安 16.5 ドルでは 0.69 倍', { x: 9.1, y: 5.8, w: 3.73, h: 0.6, fontSize: 9.5, color: L.C.sub, objectName: 'bg_cover_note' });
  return s;
};
