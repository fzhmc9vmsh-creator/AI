// 二層の構造。型: 左に構造の数字と統合の規則、右に条件ごとの現在・将来・実現確率(手本: s04 の表 + s15b の takeaway)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '現在(2026 年)と、実現性を加味した将来(2028 年、事業エンジンの基準)。実現確率は節点ツリー(5-2)の同じ節点から',
    source: 'calc/A4_q3_memo.md の §2 二層の構造、calc/out/growth_v4.json の engine・tree・grade',
  });
  // 等級セル(L.GRADE の色で塗る)
  const g = (k) => ({ text: k, options: { fill: { color: L.GRADE[k].fill }, color: L.GRADE[k].font, bold: true, align: 'center' } });
  const bold = (t) => ({ text: t, options: { bold: true } });

  // 左: 構造の数字(エンジンの基準)
  L.paneHead(s, 0.5, 1.62, 5.0, '構造の数字(エンジンの基準)');
  L.table(s, [
    ['項目', '2026 年', '2028 年'],
    ['収益の伸び', '+40%', '+18%'],
    ['会員', '1,830 万', '2,730 万'],
    ['手数料型の比率(会社定義)', '42%(Q3)', '—'],
    ['ROTCE', '8.4%', '13.1%'],
    ['自己資本の自給率', '0.89(2027)', '1.04'],
    ['総自己資本比率', '17.0%(Q3)', '16.4%'],
  ], { x: 0.5, y: 1.98, w: 5.0, colW: [2.2, 1.4, 1.4], fontSize: 9, rowH: 0.42, align: ['left', 'center', 'center'], name: 'tbl_numbers' });
  // 統合の規則(リード行に収まらないため、左の表の下に置く)
  L.box(s, 0.5, 5.0, 5.0, 0.5, { fill: L.C.gray, line: L.C.gray, name: 'ovl_rulebox' });
  L.text(s, [
    { text: '統合の規則  ', options: { bold: true, color: L.C.dark } },
    { text: '60% 以上かつ先行指標が 2 期 → 中間', options: { color: L.C.text, breakLine: true } },
    { text: '40〜60% → 上方の留保 / 40% 未満 → 現在', options: { color: L.C.text } },
  ], { x: 0.58, y: 5.02, w: 4.84, h: 0.46, fontSize: 9, valign: 'middle', margin: 0, objectName: 'note_rule' });

  // 右: 条件 × 現在 × 将来 × 実現確率 × 統合
  L.paneHead(s, 5.75, 1.62, 7.08, '条件 × 現在 × 将来 × 実現確率 × 統合');
  const row = (cond, now, fut, node, prob, lead, merged) => [cond, g(now), g(fut), node, prob, lead, bold(merged)];
  L.table(s, [
    ['条件', '現在', '将来', '決める節点', '実現確率', '先行指標', '統合'],
    row('1 競争優位', 'B', 'A', 'N1', '59%', '純増の過去最高・\n上方修正の記録', 'B(上方の留保)'),
    row('2 コア事業の CF', 'B', 'B', 'N1・N2', '—', 'ROTCE 推定 10% → 13%', 'B'),
    row('3 資産の転用', 'A', 'A', 'N4', '55%', '大口を除き +18%', 'A'),
    row('8 コモディティでない', 'B', 'A', 'N1', '59%', '同上', 'B(上方の留保)'),
    row('11 模倣困難', 'B', 'A', 'N1', '59%', '同上', 'B(上方の留保)'),
    row('12 収益の性格', 'B', 'A', 'N2・N4', '43%', '手数料型 42%(1 四半期)', 'B(上方の留保)'),
    row('13 アーキタイプ', 'B', 'A', 'N2', '43%', 'LPB の割合 29% のまま', 'B(上方の留保)'),
  ], { x: 5.75, y: 1.98, w: 7.08, colW: [1.55, 0.55, 0.55, 0.85, 0.75, 1.75, 1.08], fontSize: 9, rowH: 0.44,
    align: ['left', 'center', 'center', 'center', 'center', 'left', 'center'], name: 'tbl_layers' });

  L.takeaway(s, 0.5, 5.85, 12.33, 0.75, 'B から将来 A に上がる条件は 5 つあるが、実現確率は 43〜59% で 60% に届かない。等級は B に上方の留保を付け、\n上振れは確率ツリーの組み合わせごとに構造を判定して価値に入れる(強気は構造 A・PEG 1.4、弱気は構造 C・PEG 1.0)');
};
