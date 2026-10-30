// 表紙(指示書 spec/ch1_ch4a.md の s01 節どおり。部品 L.cover をそのまま使う)
// fix_r1 s01: 右半分の空白に結論の要点を縦に 3 つ置く(x 9.1, w 3.73)。小見出し 11pt 灰 + 値 26pt 太字 緑
module.exports = function build(pres, L) {
  const s = L.cover(pres, {
    title: 'Oracle(ORCL)\n長期保有適格性審査',
    sub: '市場は説明会の後も、株価を弱気シナリオの値に置いている\n第4.4版(Investor Day 2026-10-28 の会社資料を反映)',
    date: '2026-10-30',
  });
  const key = [
    { y: 2.0, head: '最終判断', value: '買い検討', name: 'bg_cover_k1' },
    { y: 3.3, head: '理論株価(確率加重)', value: '236 ドル', name: 'bg_cover_k2' },
    { y: 4.6, head: '構造評価', value: 'B', name: 'bg_cover_k3' },
  ];
  key.forEach(k => {
    L.text(s, k.head, { x: 9.1, y: k.y, w: 3.73, h: 0.3, fontSize: 11, color: L.C.sub, objectName: k.name });
    L.text(s, k.value, { x: 9.1, y: k.y + 0.32, w: 3.73, h: 0.6, fontSize: 26, bold: true, color: L.C.primary, objectName: k.name + 'v' });
  });
  L.text(s, '株価 139.56 ドル(2026-10-29 終値)の 1.69 倍',{ x: 9.1, y: 5.8, w: 3.73, h: 0.6, fontSize: 9.5, color: L.C.sub, objectName: 'bg_cover_note' });
  return s;
};
