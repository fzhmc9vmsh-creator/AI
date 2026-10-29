// 条件2 コア事業の稼ぐ力と資本(評価 B)。指示書 spec/v4.md の H6 の s18 節
// 配置は 4 列・4 行、評価 B の高さ(h 4.66、mechPanel bottom 6.32)と kpiBand
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 資金の出し手 → SoFi の資本の源 → 使い道と結果 → 評価。①〜⑥ は右と対応。数値は Q3 2026(2026-09-30)と事業エンジン',
    source: '会社開示(Q3 2026 の 8-K・自己資本比率の要約、research_r5/Q3_datasheet.md)、research_r2/R7_funding_rates_capital.md、calc/out/growth_v4.json(定常の ROTCE・エンジン)',
    grade: 'B', condNo: 2,
  });
  L.flowMap(s, {
    name: 's18', h: 4.66, cols: [1.35, 1.45, 1.45, 1.35], rows: 4, nodeH: 0.72,
    lanes: [{ label: '資金の出し手', c0: 0, c1: 0 }, { label: 'SoFi', c0: 1, c1: 2, self: true }, { label: '評価', c0: 3, c1: 3 }],
    groups: [{ label: '資本の源', c0: 1, c1: 1, r0: 0, r1: 3 }, { label: '使い道と結果', c0: 2, c1: 2, r0: 0, r1: 3 }],
    nodes: [
      { id: 'eq', c: 0, r: 0, label: '株主', sub: '2025 年に\n33 億ドル増資\n(20.85・27.50 ドル)' },
      { id: 'dep', c: 0, r: 1, label: '預金者', sub: '513 億ドル' },
      { id: 'mem', c: 0, r: 2, label: '借りる会員', sub: '組成 169 億ドル\n(四半期、+71%)' },
      { id: 'buyers', c: 0, r: 3, label: 'ローンの買い手', sub: 'LPB 契約\n100 億ドル超' },
      { id: 'cap', c: 1, r: 0, kind: 'key', label: '自己資本', sub: '95.8 億ドル\n総自己資本比率 17.0%' },
      { id: 'ni', c: 1, r: 1, kind: 'unit', label: '利益', sub: '2026 年 8.4 億\n(エンジン)\nQ3 純利益 2.41 億' },
      { id: 'sbc', c: 1, r: 2, kind: 'unit', label: '株式報酬', sub: '年 2.6 億ドル\n(資本に加わる)' },
      { id: 'floor', c: 1, r: 3, kind: 'risk', label: '運用の下限', sub: '比率 14%\n(会社の目標は\n10% 台前半〜半ば)' },
      { id: 'rwa', c: 2, r: 0, kind: 'risk', label: 'リスク資産(RWA)', sub: '487 → 562 億ドル\n(前期比 +15%)' },
      { id: 'bs', c: 2, r: 1, kind: 'unit', label: 'B/S 貸出', sub: 'NIM 6.14%' },
      { id: 'lpb', c: 2, r: 2, kind: 'ok', label: 'LPB', sub: '資本を使わない\n手数料 4.3%' },
      { id: 'steady', c: 2, r: 3, kind: 'unit', label: '定常の稼ぐ力', sub: '成長を止めれば\n純利益 約 15 億ドル\n(ROTCE 約 15%)' },
      { id: 'rotce', c: 3, r: 0, kind: 'risk', label: 'ROTCE', sub: '約 10%(Q3 年率)\n2027 年 12%\n2028 年 13%' },
      { id: 'tbv', c: 3, r: 2, label: 'TBVPS', sub: '7.48 ドル\n(前期 7.34 ドル)' },
    ],
    edges: [
      { from: 'eq', to: 'cap', label: '増資 33 億', kind: 'money', n: 1 },
      { from: 'ni', to: 'cap', label: '年約 11 億', kind: 'money', n: 2, left: true },
      { from: 'sbc', to: 'ni', kind: 'money' },
      { from: 'dep', to: 'bs', label: '預金', kind: 'money', fs: 'b', ts: 'b', my: 4.05, tof: -0.5, ldx: -1.05 },
      { from: 'mem', to: 'bs', label: '利息', kind: 'money', fs: 't', ts: 'b', my: 4.12, tof: -0.25, below: true, ldx: -1.24 },
      { from: 'bs', to: 'rwa', label: '貸出が増える', kind: 'goods', n: 3 },
      { from: 'rwa', to: 'cap', label: '必要資本 年約 30 億', kind: 'risk', n: 3 },
      { from: 'cap', to: 'floor', label: '2027 年', kind: 'risk', n: 4, fs: 'r', ts: 'r', mx: 4.45, fo: 0.25, lpos: 'v', lw: 0.74, ldy: 0.43 },
      { from: 'bs', to: 'lpb', label: '抱えきれない分', kind: 'goods', n: 5, fo: 0.15, tof: 0.15 },
      { from: 'lpb', to: 'buyers', label: '引き渡し', kind: 'goods', fs: 'b', ts: 't', my: 5.03, ldx: -1.24 },
      { from: 'steady', to: 'rotce', label: '成長の先行費用', kind: 'ctrl', n: 6, mx: 7.45, lpos: 'v', ldy: -0.6 },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.32,
    mech: [
      '2025 年の増資 33 億ドルで\n総自己資本比率は 22.9%(2025 年末)に。\nTBVPS は 7.48 ドル(Q3)',
      '自前の資本生成は、利益と株式報酬で年約 11 億ドル',
      '貸出が伸びると、必要資本は年約 30 億ドルで\n自前の約 3 倍。比率は 22.9% →\n18.8%(Q2)→ 17.0%(Q3)',
      'このままでは 2027 年に\n運用の下限(14%)に当たる',
      'その先は資本を使わない LPB に回すか増資。\nCFO は「現行計画では増資は不要」',
      '今の規模で成長を止めれば純利益は約 15 億ドル\n(ROTCE 約 15%、必要資本ベース 18%)で、\n資本コストを上回る。今の約 10%(Q3 年率)は\n成長投資の結果',
    ],
    reason: 'フェーズ ③ の成長投資の結果で、定常の\n稼ぐ力は資本コストを上回る。保有の\n資本 ROE 約 26%(Q3)。自給率は監視',
    up: 'ROTCE 12% 以上と比率 16% 以上を保ち、\nLPB の配分が 40% 超に戻れば A 寄り',
    down: '自給率が上がらないまま比率 15% 未満、\nまたは増資なら C',
  });
  L.kpiBand(s, '総自己資本比率 16% 未満で LPB の割合 40% 超なら確度を上げ・増資なら C 候補(毎四半期)');
  return s;
};
