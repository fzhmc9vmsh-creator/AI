// 構造評価の導出(指示書 spec/ch1_ch4.md の s05 節。手本の流れ図 exFlow を写し、L.flow を直接呼ぶ)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '構造評価の導出: 評価分布 → 適用ルール → 構造評価',
    source: '銘柄分析メソッド Phase 6、本資料の評価一覧',
  });
  L.flow(s, [
    { head: '入力: 13 条件の評価', boxes: [
      { text: 'S × 1(条件4)', tone: 'key' },
      { text: 'B × 8(条件1・2・3・5・6・10・11・12)', tone: 'in' },
      { text: 'C × 3(条件7・8・13)', tone: 'in' },
      { text: '対象外 × 1(条件9)', tone: 'off' },
    ] },
    { head: '処理: 適用ルール', boxes: [
      { text: '致命条件の拒否権(E 以下): 非発動', tone: 'off' },
      { text: '条件6・7 の対評価: 発動\n(条件7 が C のため条件6 は B が上限)', tone: 'on' },
      { text: 'C × 4 以上で B 以上にしない: 非発動(C は 3)', tone: 'off' },
    ] },
    { head: '出力: 構造評価', boxes: [
      { text: 'B', tone: 'key', h: 1.6, size: 40, bold: true },
      { text: '最頻の B。条件2 は C との境界(自給率 0.34)。\n第1版は C(条件2 を現在の ROTCE で判定していた)', tone: 'in' },
    ] },
  ]);
  return s;
};
