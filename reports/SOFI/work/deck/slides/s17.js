// 条件1 競争優位の持続(評価 B)。指示書 spec/v4.md の H6 の s17 節
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 会員 → SoFi の事業 → 優位の源泉 ← 競合の圧力。下: 優位が続く期間。①〜⑥ は右と対応。数値は Q3 2026(一部は Q2 2026)',
    source: '会社開示(Q3 2026 の 8-K・説明会の要約、research_r5/Q3_datasheet.md。(Q2) と付した値は Q2 2026)、calc/out/growth_v4.json、research_r2/R7_funding_rates_capital.md・R9_products_people.md、research/R4_scuttlebutt.md(各社 APY・価格表の第三者集計)',
    grade: 'B', condNo: 1,
  });
  L.flowMap(s, {
    name: 's17', h: 3.75, cols: [1.45, 1.4, 1.45, 1.3], rows: 3, nodeH: 0.72,
    lanes: [{ label: '会員', c0: 0, c1: 0 }, { label: 'SoFi の事業と優位の源泉', c0: 1, c1: 2, self: true }, { label: '競合', c0: 3, c1: 3 }],
    groups: [{ label: '事業', c0: 1, c1: 1, r0: 0, r1: 2 }, { label: '優位の源泉', c0: 2, c1: 2, r0: 0, r1: 2 }],
    nodes: [
      { id: 'dd', c: 0, r: 0, label: '給与振込の会員', sub: '預金の 9 割超\n普通預金 3.30%' },
      { id: 'borrow', c: 0, r: 1, label: '借りる会員', sub: 'FICO 746(Q2)\n金利を比べて選ぶ' },
      { id: 'inv', c: 0, r: 2, label: '投資・カードの会員', sub: 'Invest 390 万(Q2)\nPlus 20.6 万人(Q2)' },
      { id: 'dep', c: 1, r: 0, kind: 'unit', label: 'SoFi Money(預金)', sub: '513 億ドル\n平均 3.07%(Q2)' },
      { id: 'bs', c: 1, r: 1, kind: 'unit', label: 'B/S 貸出', sub: 'APR 6.99〜35.49%\nNIM 6.14%' },
      { id: 'cross', c: 1, r: 2, kind: 'unit', label: 'クロスバイ', sub: '新製品の 51% は\n既存会員\n1 会員 1.56 製品' },
      { id: 'fund', c: 2, r: 0, kind: 'ok', label: '銀行免許と安い資金', sub: '倉庫ラインより\n1.45pt 安い\n(前期 1.56pt)', tag: { text: '縮小中', tone: 'amber' } },
      { id: 'price', c: 2, r: 1, kind: 'risk', label: '価格の優位', sub: 'APR 帯は競合と重なる', tag: { text: 'なし', tone: 'red' } },
      { id: 'brand', c: 2, r: 2, kind: 'ok', label: 'ブランドと関係', sub: '想起 10.4%(Q2)\n販促費 4.44 億ドル\n(四半期、+55%)', tag: { text: '販促次第', tone: 'amber' } },
      { id: 'banks', c: 3, r: 0, kind: 'risk', label: 'オンライン銀行', sub: 'Ally・Amex 3.10%\nMarcus 3.50%\nChime 最大 4.00%' },
      { id: 'lenders', c: 3, r: 1, h: 0.92, kind: 'risk', label: 'ローン専業', sub: 'LightStream\n6.49〜25.39%\nLendingClub\n5.96〜35.99%' },
      { id: 'neo', c: 3, r: 2, kind: 'risk', label: 'Robinhood・Chime', sub: '給与振込と会員を\n取りに来る' },
    ],
    edges: [
      { from: 'dd', to: 'dep', label: '給与振込', kind: 'money', n: 1 },
      { from: 'fund', to: 'dep', label: '安く集める', kind: 'ctrl', n: 2 },
      { from: 'dep', to: 'bs', label: '安い資金', kind: 'money', n: 3 },
      { from: 'borrow', to: 'bs', label: '利息 13%', kind: 'money' },
      { from: 'lenders', to: 'price', label: '同じ価格帯', kind: 'risk', n: 4 },
      { from: 'price', to: 'bs', label: '市場並みの価格', kind: 'ctrl' },
      { from: 'inv', to: 'cross', label: '製品を足す', kind: 'money' },
      { from: 'brand', to: 'cross', label: '定着させる', kind: 'ctrl', n: 5 },
      { from: 'banks', to: 'fund', label: '高い金利で引き抜く', kind: 'risk', n: 6 },
      { from: 'neo', to: 'brand', label: '会員の奪い合い', kind: 'risk' },
    ],
  });
  L.text(s, '優位が続く期間', { x: 0.5, y: 5.5, w: 1.45, h: 0.2, fontSize: 8.5, bold: true, color: L.C.primary, valign: 'middle', margin: 0, objectName: 'ovl_s17_tbhead' });
  L.timeBand(s, {
    x: 0.5, y: 5.5, w: 8.55, h: 1.1, from: 2026, to: 2036, step: 2, name: 's17tb', labelW: 1.75,
    bars: [
      { label: '銀行免許', from: 2026, to: 2036, color: L.C.dark, text: '10 年超' },
      { label: '給与振込の関係(安い資金)', from: 2026, to: 2034, color: L.C.primary, text: '7〜10 年(差は縮小中)' },
      { label: 'ブランド', from: 2026, to: 2030, color: L.C.light, text: '販促を続ける限り' },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.66, mechH: 2.0,
    mech: [
      '給与振込の会員が預金の 9 割超。普通預金 3.30% は同業の中位(Ally・Amex 3.10%、Marcus 3.50%、Chime 最大 4.00%)。預金は +58 億ドル',
      '銀行免許で集めた預金は倉庫ラインより 1.45pt 安い。ただし前期の 1.56pt から縮んだ',
      '安い預金が貸出を支え、NIM は 6.14%',
      '個人ローンの APR 6.99〜35.49% は\nLightStream・LendingClub と重なり、\n価格では勝っていない',
      'ブランド(非助成想起 10.4%、Q2)とクロスバイ 51% で会員当たり 1.56 製品。\n販促費は四半期 4.44 億ドル(+55%)',
      'Robinhood・Chime も給与振込と会員を取りに来ており、資金の差を縮める圧力が続く',
    ],
    reason: '優位は価格ではなく、給与振込の関係が\n生む安い資金。7〜10 年続くと見るが、\n差は縮小中で圧倒的ではないため B',
    up: '倉庫ライン比の差が 1.5pt 以上を保ち、\n給与振込の預金が貸出と同じ速さで伸びれば A',
    down: '差が 1.2pt を割れば C',
  });
  return s;
};
