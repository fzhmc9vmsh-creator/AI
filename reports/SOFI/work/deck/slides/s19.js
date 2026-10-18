// 条件3 資産の転用(評価 B)。指示書 spec/ch3.md の s19 節
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 既存の資産 → 転用の経路 → 新しい収益 ← 外部。①〜④ は右と対応。数値は Q2 2026',
    source: '会社開示(Q2 2026 決算・説明会)、research_r2/R9_products_people.md、research/R1b_kpi.md・R4_scuttlebutt.md',
    grade: 'B', condNo: 3,
  });
  L.flowMap(s, {
    name: 's19', h: 5.0, cols: [1.35, 1.4, 1.4, 1.25], rows: 4, nodeH: 0.8,
    lanes: [{ label: '既存の資産', c0: 0, c1: 0 }, { label: 'SoFi の転用と成果', c0: 1, c1: 2, self: true }, { label: '外部', c0: 3, c1: 3 }],
    groups: [{ label: '転用の経路', c0: 1, c1: 1, r0: 0, r1: 3 }, { label: '新しい収益', c0: 2, c1: 2, r0: 0, r1: 3 }],
    nodes: [
      { id: 'mem', c: 0, r: 0, kind: 'ok', label: '会員 1,580 万人', sub: '+35%\n1 会員 1.54 製品' },
      { id: 'orig', c: 0, r: 1, kind: 'ok', label: '組成の能力', sub: '個人ローン組成\n107 億ドル/四半期' },
      { id: 'charter', c: 0, r: 2, kind: 'ok', label: '銀行免許と預金', sub: '455 億ドル' },
      { id: 'tech', c: 0, r: 3, label: '技術基盤', sub: 'Galileo・Technisys' },
      { id: 'cross', c: 1, r: 0, kind: 'unit', label: 'クロスバイ', sub: '新製品の 51% は\n既存会員' },
      { id: 'lpbc', c: 1, r: 1, kind: 'unit', label: 'LPB 契約', sub: 'Blue Owl 最大\n50 億ドル\nほか 100 億ドル超' },
      { id: 'chain', c: 1, r: 2, kind: 'unit', label: '銀行の新商品', sub: '暗号資産\n2025-11 再開\nSoFiUSD 2026-05' },
      { id: 'ext', c: 1, r: 3, kind: 'unit', label: '外販', sub: '他社に\n口座基盤を提供' },
      { id: 'fs', c: 2, r: 0, kind: 'self', label: 'FS 手数料', sub: '0.87 億ドル\n(+81%)' },
      { id: 'lpb', c: 2, r: 1, kind: 'self', label: 'LPB', sub: '年 5.6 億ドル\n(+11%)' },
      { id: 'newb', c: 2, r: 2, h: 0.94, kind: 'self', label: '新領域', sub: 'SoFiUSD 流通\n約 3 億ドル\n中小企業ローン\n2026-06〜' },
      { id: 'gal', c: 2, r: 3, kind: 'risk', label: 'Galileo', sub: '収益 −23%\n大口顧客が離脱' },
      { id: 'buyers', c: 3, r: 1, h: 0.98, label: 'ローンの買い手', sub: 'Blue Owl・\nFortress・\nBasePoint\n(3 年 30 億ドル)' },
      { id: 'chime', c: 3, r: 3, kind: 'risk', label: 'Chime', sub: '自社基盤へ移行\n解約料\n1,800 万ドル' },
    ],
    edges: [
      { from: 'mem', to: 'cross', label: '既存会員', kind: 'ctrl', n: 1 },
      { from: 'cross', to: 'fs', label: '手数料', kind: 'money' },
      { from: 'orig', to: 'lpbc', label: '組成して渡す', kind: 'goods', n: 2 },
      { from: 'lpbc', to: 'lpb', label: '手数料 4.6%', kind: 'money' },
      { from: 'buyers', to: 'lpb', label: '額面+手数料', kind: 'money' },
      { from: 'charter', to: 'chain', label: '銀行が発行', kind: 'ctrl', n: 3 },
      { from: 'chain', to: 'newb', label: '流通', kind: 'money' },
      { from: 'tech', to: 'ext', kind: 'ctrl' },
      { from: 'ext', to: 'gal', label: '処理料', kind: 'money', n: 4 },
      { from: 'chime', to: 'gal', label: '離脱', kind: 'risk' },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.66,
    mech: [
      '会員 1,580 万人に製品を足す。新製品の 51% は既存会員が開き、FS 手数料は 0.87 億ドル(+81%)',
      '組成の能力を他社の資金に貸す。LPB 契約は 100 億ドル超、手数料は年 5.6 億ドル(+11%)',
      '銀行免許の上に暗号資産(2025-11 再開)と SoFiUSD(2026-05)を載せた。流通は約 3 億ドルでまだ小さい',
      '技術基盤の外販は、大口顧客(Chime)が自社基盤へ移り −23%。転用の失敗例',
    ],
    reason: '会員と組成の基盤の転用は成果が出たが、\n新領域はまだ小さく、技術基盤の外販は\n縮んでいるため B',
    up: 'LPB 手数料が年 7 億ドルを超え、\nFS 手数料が +40% 以上を保てば A',
    down: 'LPB 組成が四半期 30 億ドルを割り、\nGalileo の流出が続けば C',
  });
  return s;
};
