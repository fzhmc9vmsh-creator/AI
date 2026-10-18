// 表紙(指示書 spec/ch1_ch4a.md の s01 節どおり。部品 L.cover をそのまま使う)
// fix_r1 s01: 右半分の空白に結論の要点を縦に 3 つ置く(x 9.1, w 3.73)。小見出し 11pt 灰 + 値 26pt 太字 緑
module.exports = function build(pres, L) {
  const s = L.cover(pres, {
    title: 'Oracle(ORCL)\n長期保有適格性審査',
    sub: '市場は AI 容量の現金化を疑い、株価は弱気寄りの倍率にとどまる\n第4.3版(品質確認と再検証の反映後)',
    date: '2026-10-17',
  });
  const key = [
    { y: 2.0, head: '最終判断', value: '買い検討', name: 'bg_cover_k1' },
    { y: 3.3, head: '理論株価(確率加重)', value: '251 ドル', name: 'bg_cover_k2' },
    { y: 4.6, head: '構造評価', value: 'B', name: 'bg_cover_k3' },
  ];
  key.forEach(k => {
    L.text(s, k.head, { x: 9.1, y: k.y, w: 3.73, h: 0.3, fontSize: 11, color: L.C.sub, objectName: k.name });
    L.text(s, k.value, { x: 9.1, y: k.y + 0.32, w: 3.73, h: 0.6, fontSize: 26, bold: true, color: L.C.primary, objectName: k.name + 'v' });
  });
  L.text(s, '株価 143.20 ドル(2026-10-13 終値)の 1.75 倍', { x: 9.1, y: 5.8, w: 3.73, h: 0.6, fontSize: 9.5, color: L.C.sub, objectName: 'bg_cover_note' });
  return s;
};
