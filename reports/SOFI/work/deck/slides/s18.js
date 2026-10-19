// 条件2 コア事業の稼ぐ力と資本(評価 B)。指示書 spec/v3.md の s18 節(小改訂)
// 配置は 4 列・4 行、評価 B の高さ(h 4.66、mechPanel bottom 6.32)と kpiBand
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 資金の出し手 → SoFi の資本の源 → 使い道と結果 → 評価。①〜⑥ は右と対応。数値は Q2 2026(2026-06-30)と需給エンジン',
    source: '会社開示(10-Q Q2 2026、自己資本比率の表)、research_r2/R7_funding_rates_capital.md、calc/out/val.json(engine_detail・steady_state・rotce)、calc/out/growth_v2.json(定常の ROTCE)',
    grade: 'B', condNo: 2,
  });
  L.flowMap(s, {
    name: 's18', h: 4.66, cols: [1.35, 1.45, 1.45, 1.35], rows: 4, nodeH: 0.72,
    lanes: [{ label: '資金の出し手', c0: 0, c1: 0 }, { label: 'SoFi', c0: 1, c1: 2, self: true }, { label: '評価', c0: 3, c1: 3 }],
    groups: [{ label: '資本の源', c0: 1, c1: 1, r0: 0, r1: 3 }, { label: '使い道と結果', c0: 2, c1: 2, r0: 0, r1: 3 }],
    nodes: [
      { id: 'eq', c: 0, r: 0, label: '株主', sub: '2025 年に\n33 億ドル増資\n(20.85・27.50 ドル)' },
      { id: 'dep', c: 0, r: 1, label: '預金者', sub: '455 億ドル' },
      { id: 'mem', c: 0, r: 2, label: '借りる会員', sub: '組成 107 億ドル\n(四半期、+54%)' },
      { id: 'buyers', c: 0, r: 3, label: 'ローンの買い手', sub: 'LPB 契約\n100 億ドル超' },
      { id: 'cap', c: 1, r: 0, kind: 'key', label: '自己資本', sub: '91.7 億ドル\n総自己資本比率 18.8%' },
      { id: 'ni', c: 1, r: 1, kind: 'unit', label: '利益', sub: '2026 年 8.3 億ドル\n(エンジン)' },
      { id: 'sbc', c: 1, r: 2, kind: 'unit', label: '株式報酬', sub: '年 2.6 億ドル\n(資本に加わる)' },
      { id: 'floor', c: 1, r: 3, kind: 'risk', label: '運用の下限', sub: '比率 14〜15%\n(10% 台前半〜半ば)' },
      { id: 'rwa', c: 2, r: 0, kind: 'risk', label: 'リスク資産(RWA)', sub: '372 → 487 億ドル\n(半年で +31%)' },
      { id: 'bs', c: 2, r: 1, kind: 'unit', label: 'B/S 貸出', sub: 'NIM 5.98%' },
      { id: 'lpb', c: 2, r: 2, kind: 'ok', label: 'LPB', sub: '資本を使わない\n手数料 4.6%' },
      { id: 'steady', c: 2, r: 3, kind: 'unit', label: '定常の稼ぐ力', sub: '成長を止めれば\n純利益 約 15 億ドル\n(ROTCE 約 15%)' },
      { id: 'rotce', c: 3, r: 0, kind: 'risk', label: 'ROTCE', sub: '2026 年 7〜9%\n資本コスト 13.9%' },
      { id: 'tbv', c: 3, r: 2, label: 'TBVPS', sub: '7.34 ドル\n(増資で +56%)' },
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
      '2025 年の増資 33 億ドルで\n総自己資本比率は 22.9% に。TBVPS は 7.34 ドル',
      '自前の資本生成は、利益と株式報酬で年約 11 億ドル',
      '上期の貸出の伸びが続くと、必要資本は年約 30 億ドルで自前の約 3 倍。比率は半年で 22.9% → 18.8%',
      'このままでは 2027 年に\n運用の下限(14〜15%)に当たる',
      'その先は資本を使わない LPB に回すか増資。CFO は「現行計画では増資は不要」',
      '今の規模で成長を止めれば純利益は約 15 億ドル\n(ROTCE 約 15%、必要資本ベース 18%)で\n資本コストを上回る。今の 7〜9% は成長投資の結果',
    ],
    reason: 'フェーズ ③ の成長投資の結果で、定常の\n稼ぐ力は資本コストを上回る。保有の\n資本 ROE 約 24%。自給率は監視',
    up: 'ROTCE 12% 以上と比率 16% 以上を保ち、\nLPB の配分が 40% 超に戻れば A 寄り',
    down: '自給率が上がらないまま比率 15% 未満、\nまたは増資なら C',
  });
  L.kpiBand(s, '総自己資本比率 16% 未満で警戒・14% 未満で C 候補 / 自給率(資本の生成 ÷ 必要資本の増加)0.5 以上で確度を上げる / LPB の配分 40% 超で A 候補(毎四半期)');
  return s;
};
