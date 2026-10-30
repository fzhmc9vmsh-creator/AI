// 分析ロジック(指示書 spec/r8_slides.md の s05 節)。examples.js の exFlow と同じ部品で、分布と対評価の記述を第4.5版に合わせた
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: '拒否権と C 上限の規則は発動しない。条件7 は A で条件6 の S を無効にしないが、条件6 は閾値 30% の前後のため B とした', kicker: '構造評価の導出: 評価分布 → 適用ルール → 構造評価', source: '銘柄分析メソッド Phase 6、本資料の評価一覧', page: 5 });
  L.flow(s, [
    { head: '入力: 13 条件の評価', boxes: [{ text: 'S × 1(条件4)', tone: 'key' }, { text: 'A × 3(条件3・7・12)', tone: 'on' }, { text: 'B × 9', tone: 'in' }] },
    { head: '処理: 適用ルール', boxes: [{ text: '致命条件の拒否権(E 以下): 非発動', tone: 'off' }, { text: '条件6・7 の対評価: 条件7 が A のため条件6 の S は無効にしないが、条件6 は閾値 30% の前後のため B', tone: 'on' }, { text: 'C × 4 以上で上限 C: 非発動(C は 0)', tone: 'off' }] },
    { head: '出力: 構造評価', boxes: [{ text: 'B', tone: 'key', h: 1.6, size: 40, bold: true }, { text: '最頻の B を採用(機械的な平均はしない)', tone: 'in' }] },
  ]);
  return s;
};
