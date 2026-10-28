// 構造評価の導出(指示書 spec/v4.md の s05 節。手本の流れ図を写し、L.flow を直接呼ぶ)
// 1 列目は 5 箱なので箱の高さを 0.7 に絞る(5 × 0.7 + 4 × 0.12 = 3.98 = 列の高さ)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '構造評価の導出: 評価分布 → 適用ルール → 等級 → 等級の中の位置 → 許容 PEG・α',
    source: '銘柄分析メソッド Phase 6・valuation-model §3-3、calc/out/growth_v4.json の grade',
  });
  L.flow(s, [
    { head: '入力: 13 条件の評価', boxes: [
      { text: 'S × 1(条件4)', tone: 'key', h: 0.7 },
      { text: 'A × 3(条件3・6・7)', tone: 'in', h: 0.7 },
      { text: 'B × 8(条件1・2・5・8・10・11・12・13)', tone: 'in', h: 0.7 },
      { text: 'C × 0', tone: 'off', h: 0.7 },
      { text: '対象外 × 1(条件9)', tone: 'off', h: 0.7 },
    ] },
    { head: '処理: 適用ルールと点数', boxes: [
      { text: '拒否権(E 以下): 非発動', tone: 'off' },
      { text: '条件6・7 の対評価: S だけ無効\n(条件6 は株価 15.9 ドル超では A)', tone: 'on' },
      { text: 'C × 4 以上で B 以上にしない: 非発動(C は 0)', tone: 'off' },
      { text: '平均点 = (5 + 4×3 + 3×8) ÷ 12 = 3.42', tone: 'on' },
    ] },
    { head: '出力: 構造評価と倍率', boxes: [
      { text: 'B', tone: 'key', h: 1.2, size: 40, bold: true },
      { text: '帯 2.5〜3.5 の中の位置 0.92\n許容 PEG 1.275(2029 年 1.125)・α 20.4%', tone: 'in' },
      { text: 'A の境目 3.5 まで 0.08 点。\n条件1・8・11 か 12・13 の 1 つが A で構造 A', tone: 'in' },
    ] },
  ]);
  return s;
};
