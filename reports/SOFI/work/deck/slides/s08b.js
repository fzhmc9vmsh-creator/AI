// 事業理解(2/3): 事業どうしの関係図(会員 → 資金を集める柱 → 稼ぐ柱 → 資金の出し手・提携先)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左: 会員 → SoFi の事業(資金を集める柱 → 稼ぐ柱)→ 資金の出し手・提携先。①〜⑦ は右の「仕組み」と対応。数値は Q2 2026',
    source: '会社開示(Q2 2026 決算・10-Q)、research_r2/R5_credit_fv.md・R6_pnl_margin.md・R7_funding_rates_capital.md、research/R1b_kpi.md',
  });
  L.flowMap(s, {
    name: 's08b', h: 5.0, cols: [1.32, 1.36, 1.5, 1.32], rows: 4.2, nodeH: 0.78,
    lanes: [{ label: '会員(顧客)', c0: 0, c1: 0 }, { label: 'SoFi の事業', c0: 1, c1: 2, self: true }, { label: '資金の出し手・提携先', c0: 3, c1: 3 }],
    groups: [{ label: '資金を集める柱', c0: 1, c1: 1, r0: 0, r1: 2 }, { label: '稼ぐ柱', c0: 2, c1: 2, r0: 0, r1: 3 }],
    nodes: [
      { id: 'dd', c: 0, r: 0, label: '給与振込の会員', sub: '会員 1,580 万人(+35%)\n預金の約 9 割' },
      { id: 'borrow', c: 0, r: 1.5, label: '借りる会員', sub: 'FICO 746\n年収 15.8 万ドル' },
      { id: 'inv', c: 0, r: 3, label: '投資・Plus の会員', sub: 'Invest 390 万口座\nPlus 有料 20.6 万人' },
      { id: 'dep', c: 1, r: 0, kind: 'key', label: 'SoFi Money(預金)', sub: '455 億ドル・平均 3.07%\n倉庫ラインより 1.56pt 安い' },
      { id: 'cap', c: 1, r: 1.5, kind: 'unit', label: '銀行免許と自己資本', sub: '総自己資本比率 18.8%\n(半年で −4.1pt)' },
      { id: 'tp', c: 1, r: 3, kind: 'unit', label: 'Tech Platform', sub: 'Galileo 0.85 億ドル\n(−23%、大口が離脱)' },
      { id: 'bs', c: 2, r: 0, kind: 'key', label: 'B/S 貸出', sub: '個人 261・学生 161 億ドル\nNIM 5.98%' },
      { id: 'lpb', c: 2, r: 1.5, kind: 'unit', label: 'LPB', sub: '組成 31 億ドル/四半期\n手数料 4.6%' },
      { id: 'fs', c: 2, r: 3, kind: 'unit', label: 'FS 手数料', sub: 'インターチェンジ・売買・Plus\n0.87 億ドル(+81%)' },
      { id: 'eq', c: 3, r: 0, label: '株主', sub: '2025 年に 33 億ドル増資\n(20.85・27.50 ドル)' },
      { id: 'buyers', c: 3, r: 1.5, label: 'ローンの買い手', sub: 'Blue Owl・Fortress・銀行\n契約 100 億ドル超' },
      { id: 'b2b', c: 3, r: 3, label: 'フィンテック・銀行', sub: 'Galileo の顧客\n口座 1.35 億' },
    ],
    edges: [
      { from: 'dd', to: 'dep', label: '給与振込', kind: 'money', n: 1 },
      { from: 'dep', to: 'bs', label: '安い資金', kind: 'money', n: 2 },
      { from: 'borrow', to: 'bs', label: '利息 13%', kind: 'money', n: 3, fs: 't', ts: 'b', fo: 0.22, tof: -0.2, my: 3.3, lpos: 'v' },
      { from: 'bs', to: 'borrow', kind: 'goods', fs: 'b', ts: 't', fo: -0.4, tof: -0.22, my: 3.12 },
      { from: 'bs', to: 'lpb', label: '抱えきれない分', kind: 'goods', n: 4 },
      { from: 'lpb', to: 'buyers', label: 'ローンを引き渡す', kind: 'goods', n: 4 },
      { from: 'buyers', to: 'lpb', label: '額面+手数料', kind: 'money' },
      { from: 'eq', to: 'cap', label: '増資', kind: 'money', n: 5, fs: 'b', ts: 't', my: 3.55 },
      { from: 'cap', to: 'bs', label: '資本が上限', kind: 'ctrl', n: 5, lpos: 'v' },
      { from: 'inv', to: 'fs', label: '手数料・会費', kind: 'money', n: 6, fs: 't', ts: 't', fo: 0, tof: -0.2, my: 4.85 },
      { from: 'fs', to: 'borrow', label: 'クロスバイ 51%', kind: 'ctrl', n: 6, fs: 't', ts: 'b', fo: 0.2, my: 4.62, lpos: 'v' },
      { from: 'b2b', to: 'tp', label: '処理料', kind: 'money', n: 7, fs: 'b', ts: 'b', my: 6.2 },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.66, mechH: 3.3,
    mech: [
      '給与振込の会員が預金の約 9 割を占め、455 億ドルを平均 3.07% で集める。倉庫ラインより 1.56pt 安い',
      '安い預金が B/S の貸出を支え、NIM 5.98%。収益の 65% はこの利ざや',
      '借りる会員は平均クーポン 13% の個人ローンを借りる。貸倒は all-in で年 3.7%',
      '資本で抱えきれない分は LPB で買い手へ。額面+手数料 4.6% で売り、信用リスクは買い手が負う',
      '貸出の伸びは自己資本で決まる。2025 年の増資で比率は 22.9% に上がったが、半年で 18.8% に下がった',
      '投資・Plus・カードの会員は手数料を払い、新製品の 51% は既存会員が開く',
      'Galileo は他社に口座の基盤を売るが、大口顧客の内製化で −23%',
    ],
    reason: '会員の預金が安い資金になり、自社の貸出の利ざやが収益の 3 分の 2 を生む。伸びの上限は自己資本で、ここが最大の争点',
  });
  return s;
};
