// 条件8(評価 C): コモディティ性。指示書 spec/ch3.md の s24 節
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 借り手 → SoFi の事業 → ローンの買い手 ← 価格の基準。①〜⑤ は右と対応。収益の内訳は Q2 2026',
    source: '会社開示(Q2 2026 決算・10-Q)、research_r2/R9_products_people.md(各社の価格表)、research/R4_scuttlebutt.md(LPB 契約・プライベートクレジット)',
    grade: 'C', condNo: 8,
  });
  L.flowMap(s, {
    name: 's24', h: 4.66, cols: [1.2, 1.45, 1.4, 1.35], rows: 3,
    lanes: [{ label: '借り手', c0: 0, c1: 0 }, { label: 'SoFi の事業', c0: 1, c1: 1, self: true }, { label: 'ローンの買い手', c0: 2, c1: 2 }, { label: '価格の基準', c0: 3, c1: 3 }],
    nodes: [
      { id: 'borrow', c: 0, r: 0, label: '借りる会員', sub: 'FICO 746\n金利を比べて選ぶ' },
      { id: 'rel', c: 0, r: 1, kind: 'ok', label: '会員との関係', sub: 'クロスバイ 51%\n1 会員 1.54 製品' },
      { id: 'dd', c: 0, r: 2, kind: 'ok', label: '給与振込の預金', sub: '平均 3.07%' },
      { id: 'nii', c: 1, r: 0, kind: 'unit', label: '貸出の利ざや', sub: '収益の 65%\nNIM 5.98%', tag: { text: '商品', tone: 'red', above: true } },
      { id: 'lpb', c: 1, r: 1, kind: 'unit', label: 'LPB・売却益', sub: '収益の 24%', tag: { text: '商品', tone: 'red', above: true } },
      { id: 'fee', c: 1, r: 2, kind: 'unit', label: '手数料・会費', sub: '収益の 11%', tag: { text: '差別化', tone: 'green', above: true } },
      { id: 'bo', c: 2, r: 0, label: 'Blue Owl・Fortress', sub: 'LPB 契約\n100 億ドル超' },
      { id: 'pc', c: 2, r: 1, kind: 'risk', label: 'プライベートクレジット', sub: '個人ローン組成の約 1/4\nに資金(前年 6%)' },
      { id: 'bank', c: 2, r: 2, label: '銀行・ABS の投資家', sub: '全額売却 106.5%\n(Q4 2025)' },
      { id: 'apr', c: 3, r: 0, kind: 'risk', label: '競合の APR', sub: 'LendingClub 5.96〜35.99%\nLightStream 6.49〜25.39%' },
      { id: 'par', c: 3, r: 1, kind: 'risk', label: '売却の価格', sub: 'ほぼ額面 + 手数料 4.6%' },
      { id: 'brand', c: 3, r: 2, kind: 'ok', label: 'ブランド', sub: '想起 10.4%' },
    ],
    edges: [
      { from: 'borrow', to: 'nii', label: '利息 13%', kind: 'money', n: 1 },
      { from: 'apr', to: 'borrow', label: '比べる', kind: 'risk', fs: 't', ts: 't', my: 2.02, below: true },
      { from: 'nii', to: 'lpb', label: '抱えきれない分', kind: 'goods', n: 2, fo: -0.4, tof: -0.4 },
      { from: 'lpb', to: 'bo', label: '引き渡し', kind: 'goods' },
      { from: 'par', to: 'lpb', label: '価格の上限', kind: 'risk', n: 3, fs: 'b', ts: 'b', my: 4.55 },
      { from: 'pc', to: 'bo', kind: 'risk', n: 4 },
      { from: 'rel', to: 'fee', label: '製品を足す', kind: 'money', n: 5 },
      { from: 'dd', to: 'nii', label: '安い資金', kind: 'ctrl' },
      { from: 'brand', to: 'rel', kind: 'ctrl', fs: 't', ts: 'b', my: 4.65 },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.32,
    mech: [
      '借り手は FICO 746 の優良層で、金利を比べて選ぶ。APR 帯は LendingClub・LightStream と重なる',
      '抱えきれないローンは LPB と売却で他社に渡す。収益の 24%',
      '買い手はほぼ額面と手数料 4.6% で買う。市場で値の付く商品で、上乗せは小さい',
      'プライベートクレジットは 2025 年の個人ローン組成の約 1/4 に資金を出し(前年 6%)、競合にも同じ資金が回る',
      '差別化は会員との関係(クロスバイ 51%)と安い預金。商品の部分が収益の約 6 割を占める',
    ],
    reason: 'ローンは市場で値の付く商品。\n差別化は会員との関係と預金にあり、\n収益の約 6 割が商品の性格のため C',
    up: 'NIM 5.8% 以上と LPB 手数料率 4.5% 以上を\n保てば B',
    down: 'NIM 5.3% 未満か、手数料率 3.5% 未満なら D',
  });
  L.kpiBand(s, 'NIM 5.8% 以上で B 候補・5.3% 未満で D 候補 / LPB の手数料率 4.5% 以上で確度を上げ・3.5% 未満で D 候補(毎四半期)');
  return s;
};
