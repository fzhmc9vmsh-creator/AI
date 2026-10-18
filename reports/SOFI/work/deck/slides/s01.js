// 表紙(指示書 spec/ch1_ch4.md の s01 節どおり。部品 L.cover をそのまま使う)
// 右半分に結論の要点を縦に 3 つ置く(x 9.1, w 3.73)。小見出し 11pt 灰 + 値 26pt 太字 緑
module.exports = function build(pres, L) {
  const s = L.cover(pres, {
    title: 'SoFi Technologies(SOFI)\n長期保有適格性審査',
    sub: '銀行免許を持つフィンテック。攻めの獲得投資で会員を重ね、\n自己資本が成長を律速する。第2版: 成長の尺度で評価し直した',
    date: '2026-10-18(第2版)',
  });
  const key = [
    { y: 2.0, head: '最終判断', value: '監視', name: 'bg_cover_k1' },
    { y: 3.3, head: '理論株価(確率加重)', value: '14.7 ドル', name: 'bg_cover_k2' },
    { y: 4.6, head: '構造評価', value: 'B', name: 'bg_cover_k3' },
  ];
  key.forEach(k => {
    L.text(s, k.head, { x: 9.1, y: k.y, w: 3.73, h: 0.3, fontSize: 11, color: L.C.sub, objectName: k.name });
    L.text(s, k.value, { x: 9.1, y: k.y + 0.32, w: 3.73, h: 0.6, fontSize: 26, bold: true, color: L.C.primary, objectName: k.name + 'v' });
  });
  L.text(s, '株価 14.55 ドル(2026-10-16 終値)は理論株価の 0.99 倍', { x: 9.1, y: 5.8, w: 3.73, h: 0.6, fontSize: 9.5, color: L.C.sub, objectName: 'bg_cover_note' });
  return s;
};
