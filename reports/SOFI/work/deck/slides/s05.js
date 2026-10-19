// 構造評価の導出(指示書 spec/v3.md の s05 節。手本の流れ図 exFlow を写し、L.flow を直接呼ぶ)
// 1 列目は 5 箱なので箱の高さを 0.7 に絞る(5 × 0.7 + 4 × 0.12 = 3.98 = 列の高さ)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '構造評価の導出: 評価分布 → 適用ルール → 等級 → 等級の中の位置 → 許容 PEG・α(第5.1版の規則)',
    source: '銘柄分析メソッド Phase 6・valuation-model §3-3、calc/out/growth_v3.json の grade_rule',
  });
  L.flow(s, [
    { head: '入力: 13 条件の評価', boxes: [
      { text: 'S × 1(条件4)', tone: 'key', h: 0.7 },
      { text: 'A × 2(条件6・7)', tone: 'in', h: 0.7 },
      { text: 'B × 9(条件1・2・3・5・8・10・11・12・13)', tone: 'in', h: 0.7 },
      { text: 'C × 0', tone: 'off', h: 0.7 },
      { text: '対象外 × 1(条件9)', tone: 'off', h: 0.7 },
    ] },
    { head: '処理: 適用ルールと点数', boxes: [
      { text: '拒否権(E 以下): 非発動', tone: 'off' },
      { text: '条件6・7 の対評価: S だけ無効\n(条件6 は同業比で S に届かず A)', tone: 'on' },
      { text: 'C × 4 以上で B 以上にしない: 非発動(C は 0)', tone: 'off' },
      { text: '平均点 = (5 + 4×2 + 3×9) ÷ 12 = 3.33', tone: 'on' },
    ] },
    { head: '出力: 構造評価と倍率', boxes: [
      { text: 'B', tone: 'key', h: 1.2, size: 40, bold: true },
      { text: '帯 2.5〜3.5 の中の位置 0.83\n許容 PEG 1.25(2029 年 1.10)・α 20.8%', tone: 'in' },
      { text: '第2版(S1・B8・C3、2.92 点)は\n同じ規則で PEG 1.125', tone: 'in' },
    ] },
  ]);
  return s;
};
