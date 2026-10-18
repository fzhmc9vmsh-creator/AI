// 条件10・11(評価 B・B): 模倣困難性と陳腐化。指示書 spec/ch3.md の s26 節
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 再現に時間がかかる資産 / 陳腐化しうる資産 ← 競合の動き。下: 資産ごとの持ちの長さ。①〜⑤ は右と対応',
    source: '会社開示(Q2 2026 決算)、research/R4_scuttlebutt.md(Chime の S-1、Robinhood・LendingClub の Q2 2026 決算)、research_r2/R9_products_people.md',
    grade: 'B', condNo: '10・11',
  });
  L.flowMap(s, {
    name: 's26', y: 1.66, h: 3.75, cols: [1.45, 1.55, 1.35, 1.45], rows: 3, nodeH: 0.74,
    lanes: [
      { label: '再現に時間がかかる資産(条件11)', c0: 0, c1: 1 },
      { label: '陳腐化する資産(条件10)', c0: 2, c1: 2, self: true },
      { label: '競合の動き', c0: 3, c1: 3 },
    ],
    nodes: [
      { id: 'charter', c: 0, r: 0, kind: 'ok', label: '銀行免許', sub: '2022 年に銀行を買収\n審査に約 1 年' },
      { id: 'mem', c: 0, r: 1, kind: 'ok', label: '会員 1,580 万人', sub: '1 会員 1.54 製品' },
      { id: 'dep', c: 0, r: 2, kind: 'ok', label: '預金 455 億ドル', sub: '給与振込が約 9 割' },
      { id: 'brand', c: 1, r: 0, kind: 'ok', label: 'ブランド', sub: '想起 10.4%\n(販促が必要)' },
      { id: 'data', c: 1, r: 1, kind: 'ok', label: '信用データ', sub: '組成の実績\n(個人ローンの損失履歴)' },
      { id: 'lpbn', c: 1, r: 2, kind: 'unit', label: 'LPB の買い手の網', sub: '100 億ドル超の契約' },
      { id: 'tech', c: 2, r: 0, kind: 'risk', label: '技術基盤', sub: 'Galileo・Technisys\n(買収 約 23 億ドル)' },
      { id: 'app', c: 2, r: 1, kind: 'unit', label: 'アプリ・製品', sub: '機能は真似\nされやすい' },
      { id: 'gal', c: 2, r: 2, kind: 'risk', label: 'Galileo の外販', sub: '収益 −23%' },
      { id: 'chime', c: 3, r: 0, kind: 'risk', label: 'Chime', sub: '自社基盤 ChimeCore へ\n解約料 1,800 万ドル' },
      { id: 'rh', c: 3, r: 1, kind: 'risk', label: 'Robinhood', sub: '銀行業務 入金\n30 億ドル超\nGold 480 万人' },
      { id: 'lc', c: 3, r: 2, label: 'LendingClub', sub: '預金 102 億ドル\n借り手が新規口座の\n15% 超' },
    ],
    edges: [
      { from: 'chime', to: 'gal', label: '内製化で離脱', kind: 'risk', n: 1, mx: 7.25, lpos: 'v', left: true, ldy: -0.51 },
      { from: 'tech', to: 'gal', kind: 'ctrl', fs: 'l', ts: 'l', mx: 4.9 },
      { from: 'rh', to: 'app', kind: 'risk', n: 2, ldx: -0.3 },
      { from: 'lc', to: 'dep', kind: 'risk', n: 3, fs: 'b', ts: 'b', my: 5.06, ldy: -0.05 },
      { from: 'charter', to: 'dep', kind: 'ctrl', n: 4, fs: 'r', ts: 'r', mx: 2.35 },
      { from: 'mem', to: 'brand', kind: 'ctrl', n: 5, mx: 2.6, lpos: 'v' },
    ],
  });
  L.text(s, '資産ごとの持ちの長さ', { x: 0.5, y: 5.5, w: 1.45, h: 0.2, fontSize: 8.5, bold: true, color: L.C.primary, valign: 'middle', margin: 0, objectName: 'ovl_s26_tbhead' });
  L.timeBand(s, {
    x: 0.5, y: 5.5, w: 8.55, h: 1.1, from: 2026, to: 2036, step: 2, name: 's26tb', fmt: (t) => String(t),
    bars: [
      { label: '銀行免許', from: 2026, to: 2036, color: L.C.dark, text: '10 年超' },
      { label: '会員と預金', from: 2026, to: 2034, color: L.C.primary, text: '7〜10 年' },
      { label: 'ブランド', from: 2026, to: 2030, color: L.C.light, text: '販促が続く限り' },
      { label: '技術基盤', from: 2026, to: 2030, color: L.C.amber, text: '3〜5 年で更新が要る' },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.66, mechH: 2.45,
    mech: [
      'Chime は自社基盤へ移り、\n解約料 1,800 万ドルを払って Galileo を離れた。\n技術基盤の外販は内製化で陳腐化しうる',
      'Robinhood は銀行業務(入金 30 億ドル超、\n給与振込の設定 約 4 割)を始め、\nアプリの機能は真似されやすい',
      'LendingClub は貸し手と預金を組み合わせた\n同じ型(預金 102 億ドル)。\n型そのものは独占ではない',
      '銀行免許は買収と審査に約 1 年\n(2021-03 契約 → 2022-02 完了)。\n給与振込の預金 455 億ドルは短期に再現できない',
      '会員 1,580 万人とブランドは、\n販促を続ける限り積み上がる',
    ],
    reason: '免許・会員・預金は再現に数年かかる(11 B)。\n技術基盤の外販は内製化で陳腐化しうる(10 B)',
    up: 'Galileo の外販が増収に戻り、\n会員当たりの製品が 1.7 を超えれば A',
    down: '他のフィンテックの銀行免許取得が続き、\n資金の差が 1.2pt を割れば C',
  });
  return s;
};
