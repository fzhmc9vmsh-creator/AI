// 条件8(評価 B): 単品はコモディティ、束は同業との相対で評価
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 借り手 → SoFi の事業 → ローンの買い手 ← 価格の基準。①〜⑤ は右と対応。収益の内訳は Q3 2026。評価は単品でなく束 × 同業との相対で決める',
    source: '会社開示(Q3 2026 決算)、research_r5/Q3_datasheet.md、research_r2/R9_products_people.md、research/R4_scuttlebutt.md、research_r4/R16・R17',
    grade: 'B', condNo: 8,
  });
  L.flowMap(s, {
    name: 's24', h: 4.66, cols: [1.2, 1.45, 1.4, 1.35], rows: 3,
    lanes: [{ label: '借り手', c0: 0, c1: 0 }, { label: 'SoFi の事業', c0: 1, c1: 1, self: true }, { label: 'ローンの買い手', c0: 2, c1: 2 }, { label: '価格の基準', c0: 3, c1: 3 }],
    nodes: [
      { id: 'borrow', c: 0, r: 0, label: '借りる会員', sub: 'FICO 746\n純償却 2.26%\n(同業 3.2〜4.2%)' },
      { id: 'rel', c: 0, r: 1, kind: 'ok', label: '会員との関係', sub: 'クロスバイ 51%\n1 会員 1.56 製品' },
      { id: 'dd', c: 0, r: 2, kind: 'ok', label: '給与振込の預金', sub: '平均 3.07%(上期)' },
      { id: 'nii', c: 1, r: 0, kind: 'unit', label: '貸出の利ざや', sub: '収益の 67%\nNIM 6.14%', tag: { text: '商品', tone: 'red', above: true } },
      { id: 'lpb', c: 1, r: 1, kind: 'unit', label: 'LPB・売却益', sub: 'LPB 手数料 1.53 億\n(売却益は未開示)', tag: { text: '商品', tone: 'red', above: true } },
      { id: 'fee', c: 1, r: 2, kind: 'unit', label: '手数料・会費', sub: '手数料型 42%\n(会社定義)', tag: { text: '差別化(束)', tone: 'green', above: true } },
      { id: 'bo', c: 2, r: 0, label: 'Blue Owl・Fortress', sub: 'LPB 契約\n100 億ドル超' },
      { id: 'pc', c: 2, r: 1, kind: 'risk', label: 'プライベート\nクレジット', sub: '個人ローン組成の約 1/4\nに資金(前年 6%)', subSize: 8 },
      { id: 'bank', c: 2, r: 2, label: '銀行・ABS の投資家', sub: '全額売却 106.5%\n(Q4 2025)' },
      { id: 'apr', c: 3, r: 0, kind: 'risk', h: 1.0, label: '競合の APR', sub: 'LendingClub\n5.96〜35.99%\nLightStream\n6.49〜25.39%' },
      { id: 'par', c: 3, r: 1, kind: 'risk', label: '売却の価格', sub: 'ほぼ額面\n+ 手数料 4.6%' },
      { id: 'brand', c: 3, r: 2, kind: 'ok', label: 'ブランド', sub: '想起 10.4%' },
    ],
    edges: [
      { from: 'borrow', to: 'nii', label: '利息 13%', kind: 'money', n: 1 },
      { from: 'apr', to: 'borrow', label: '比べる', kind: 'risk', fs: 't', ts: 't', my: 2.02, below: true, ldx: 2.4 },
      { from: 'nii', to: 'lpb', label: '抱えきれない分', kind: 'goods', n: 2, fo: -0.4, tof: -0.4, ldy: -0.11 },
      { from: 'lpb', to: 'bo', label: '引き渡し', kind: 'goods', lpos: 'v' },
      { from: 'par', to: 'lpb', label: '価格の上限', kind: 'risk', n: 3, fs: 'b', ts: 'b', my: 4.55, ldx: 1.2 },
      { from: 'pc', to: 'bo', kind: 'risk', n: 4 },
      { from: 'rel', to: 'fee', kind: 'money', n: 5, mx: 1.9, tof: 0.15 },
      { from: 'dd', to: 'nii', label: '安い資金', kind: 'ctrl', mx: 2.05, fo: -0.15, lpos: 'v' },
      { from: 'brand', to: 'rel', kind: 'ctrl', fs: 't', ts: 'b', my: 4.65 },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.32,
    mech: [
      '借り手は FICO 746 の優良層で、金利を比べて\n選ぶ。APR 帯は LendingClub・LightStream と重なる',
      '抱えきれないローンは LPB と売却で\n他社に渡す。LPB 手数料は 1.53 億(売却益は未開示)',
      '買い手はほぼ額面と手数料 4.6% で買う。単品のローンは市場で値の付く商品',
      'プライベートクレジットは 2025 年の個人ローン\n組成の約 1/4 に資金を出し(前年 6%)、\n競合にも同じ資金が回る',
      '束では差が出る: 製品当たり獲得費 202 ドル\n(会員当たりの約半分)、純償却は同業より低い。\n預金の基本金利は同業の中位',
    ],
    reason: '単品は商品だが、束では獲得費と貸倒で\n同業より低い。束に値段が付く証拠は\nまだ無く B',
    up: '有料会員と手数料型の比率が上がり、\n束に値段が付けば A',
    down: '純償却が同業並み(3.5% 超)になり、\n預金金利を同業並みに上げないと預金が\n減るなら C',
  });
  L.kpiBand(s, '製品当たり獲得費 200 ドル以下・個人ローン純償却 3.0% 以下で確度を上げ / 預金の基本金利を同業並みに上げないと預金が減れば C 候補(毎四半期)');
  return s;
};
