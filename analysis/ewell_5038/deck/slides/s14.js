// 経営と統治: 左に経歴 → 現職 → 担う事業 → 結果の関係図、右に統治の表と注目点(赤)
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, {
    kicker: '左から: 経歴(どこで何を築いたか)→ 現職 → 担う事業 → 結果。右: 統治の仕組みと、資本配分で説明が変わった点',
    source: '有価証券報告書(FY2025)p.51-53、会社開示',
  });
  L.flowMap(s, {
    name: 's14', h: 4.9, cols: [1.45, 1.4, 1.35, 1.4], rows: 3, nodeH: 0.9,
    lanes: [{ label: '経歴', c0: 0, c1: 0 }, { label: '現職と担う事業', c0: 1, c1: 2, self: true }, { label: '結果', c0: 3, c1: 3 }],
    nodes: [
      { id: 'a', c: 0, r: 0, label: '1991 年', sub: '㈱サンエース入社' },
      { id: 'b', c: 0, r: 1, label: '2012 年 1 月', sub: '葬祭式場を経営' },
      { id: 'c', c: 0, r: 2, kind: 'ok', label: '2012 年 6 月', sub: 'eWeLL を設立' },
      { id: 'ceo', c: 1, r: 1, kind: 'self', label: '代表取締役社長', sub: `2018 年 10 月から現任\n${F('hold.founder')} 保有` },
      { id: 'ibow', c: 2, r: 0, kind: 'unit', label: 'iBow', sub: '2014 年 6 月に提供' },
      { id: 'ipo', c: 2, r: 2, kind: 'unit', label: '上場', sub: '2022 年 9 月' },
      { id: 'r1', c: 3, r: 0, kind: 'ok', label: '3,843 事業所', sub: '利用先の数' },
      { id: 'r2', c: 3, r: 1, kind: 'ok', label: '営業利益率 47%', sub: '2026 年 1〜9 月' },
      { id: 'r3', c: 3, r: 2, kind: 'ok', label: '期初予想を達成', sub: '営業利益は\n4 期すべて' },
    ],
    edges: [
      { from: 'a', to: 'b', kind: 'ctrl' },
      { from: 'b', to: 'c', kind: 'ctrl' },
      { from: 'c', to: 'ceo', label: '創業', kind: 'ctrl' },
      { from: 'ceo', to: 'ibow', kind: 'goods' },
      { from: 'ceo', to: 'ipo', kind: 'goods' },
      { from: 'ibow', to: 'r1', kind: 'money' },
      { from: 'ipo', to: 'r3', kind: 'money' },
    ],
  });
  L.paneHead(s, 9.25, 1.62, 3.58, '統治の仕組み', 'pane_gov');
  L.table(s, [
    ['項目', '内容'],
    ['取締役', `${F('gov.board')}(社外 1 名)`],
    ['指名・報酬委員会', '3 名(社長・常務・社外)'],
    ['上位 2 名の持株', '55.26%'],
    ['報酬', '業績連動 + 譲渡制限付株式'],
    ['SO の希薄化', F('so.dilution')],
    ['後継の計画', '未開示'],
    ['CFO', '執行役員(取締役でない)'],
  ], { x: 9.25, y: 1.98, w: 3.58, colW: [1.35, 2.23], fontSize: 9, rowH: 0.36, align: ['left', 'left'], name: 'tbl_gov' });
  L.box(s, 9.25, 5.0, 3.58, 1.3, { fill: C.gray, line: C.red, name: 'ovl_alert' });
  L.text(s, [
    { text: '注目: 4 日で変わった還元の説明', options: { bold: true, color: C.red, breakLine: true } },
    { text: '2026-02-13 「自己株買いは検討しない」', options: { color: C.text, breakLine: true } },
    { text: '2026-02-17 300 百万円の取得を決議', options: { color: C.text } },
  ], { x: 9.35, y: 5.04, w: 3.4, h: 1.22, fontSize: 9.5, valign: 'middle', objectName: 'alert' });
  return s;
};
