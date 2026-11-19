// 投資行動: 左に価格の梯子(46.3 以下を濃緑)、右に判別表(確認日 | 続行・買いの線 | 見直し・撤回の線)、下に結論の箱
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, {});
  L.paneHead(s, L.M, 1.62, 6.05, '価格の梯子(上ほど高い値段)', 'pane_l');
  const ladder = [
    [F('ipo.hi'), '公開価格の上限'],
    [F('ipo.lo'), '公開価格の下限(仮条件)'],
    [F('ev'), '確率で重みをつけた期待値'],
    [F('fair'), '適正株価'],
    [F('entry'), '分割で買う上限'],
    [F('bear.value'), '弱気の下値'],
  ];
  const lowFrom = 4;   // 分割で買う上限(46.3 ドル)以下を濃緑
  ladder.forEach(([v, name], i) => {
    const y = 2.0 + i * 0.6, low = i >= lowFrom;
    L.box(s, L.M, y, 6.05, 0.5, { fill: low ? C.dark : C.gray, line: low ? C.dark : C.gray, name: 'ladder_bg' + i });
    L.text(s, v, { x: L.M + 0.15, y, w: 2.0, h: 0.5, fontSize: 14, bold: true, color: low ? C.white : C.dark, valign: 'middle', margin: 0, objectName: 'ladder_v' + i });
    L.text(s, name, { x: L.M + 2.3, y, w: 3.6, h: 0.5, fontSize: 11, color: low ? C.white : C.text, valign: 'middle', margin: 0, objectName: 'ladder_n' + i });
  });
  L.paneHead(s, 6.78, 1.62, 6.05, '判別表(確認する日と、買い・撤回の線)', 'pane_r');
  const rows = [
    ['確認日', '続行・買いの線', '見直し・撤回の線'],
    ['2026-11-19 上場', '公開価格では見送り。二次市場で 46.3 ドル以下に下がれば分割で検討', '82 ドル超で決まれば、180 日後の売却制限の解除まで静観'],
    ['2027-02-28 年度の決算', '研究開発費の比率 48% 未満、年換算売上の高い伸び', '実質の粗利率 66% 割れ、大口の分散で伸びが急減'],
    ['2027-05-15 第1四半期と総会', '株数の増加が年 2.0% 未満、還元の姿勢', '年 3.5% 超の株数の増加、信託による非効率な増資'],
    [{ text: '2027-08-15(核心)上期の決算', options: { bold: true, color: C.dark } }, { text: '実質の粗利率 70% 以上かつ研究開発費の比率 40% 未満、営業利益率 20% 以上', options: { bold: true, color: C.dark } }, '実質の粗利率 62% 未満か研究開発費の比率 50% 以上が続く → 撤回'],
  ];
  L.table(s, rows, { x: 6.78, y: 2.0, w: 6.05, colW: [1.7, 2.25, 2.1], fontSize: 9.5, rowH: 0.8, align: ['left', 'left', 'left'], name: 'judge_tbl' });
  L.takeaway(s, L.M, 6.25, 12.33, 0.45, `公開価格では買わず、${F('entry')} 以下か来年8月の決算で実質の粗利率 ${F('kpi.gm')} 以上を確かめてから買う`);
};
