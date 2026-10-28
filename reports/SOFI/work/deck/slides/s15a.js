// 成長エンジン。関係図(会員 → 獲得と関係 → 収益化 → 資金と資本)。手本は s08b(flowMap + mechPanel)。評価バッジなし
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 会員 → SoFi の獲得と関係 → 収益化 → 資金と資本。①〜⑥ は右と対応。数値は Q3 2026(販促費は年換算)',
    source: 'research_r5/Q3_datasheet.md、会社開示(Q3 2026)、calc/out/growth_v4.json',
  });
  L.flowMap(s, {
    name: 's15a', h: 5.0, cols: [1.4, 1.5, 1.55, 1.3], rows: 4.2, nodeH: 0.72,
    lanes: [{ label: '会員', c0: 0, c1: 0 }, { label: 'SoFi の成長エンジン', c0: 1, c1: 2, self: true }, { label: '資金と資本', c0: 3, c1: 3 }],
    groups: [{ label: '獲得と関係', c0: 1, c1: 1, r0: 0, r1: 3.1 }, { label: '収益化', c0: 2, c1: 2, r0: 0, r1: 3.1 }],
    nodes: [
      { id: 'dd', c: 0, r: 0, label: '給与振込の会員', sub: '給与振込の比率は\n未開示(主口座)' },
      { id: 'newm', c: 0, r: 1.55, h: 0.84, label: '新しい会員', sub: '純増 120 万人/四半期\n会員当たり\n販促費 370 ドル' },
      { id: 'ex', c: 0, r: 3.1, label: '既存会員', sub: '1,710 万人\n1 会員 1.56 製品' },
      { id: 'money', c: 1, r: 0, kind: 'unit', label: 'SoFi Money(預金)', sub: '513 億ドル\n平均金利は未開示' },
      { id: 'sm', c: 1, r: 1.55, h: 0.84, kind: 'unit', label: '販促・ブランド', sub: '年 17.8 億ドル\n(収益の 32%)\n認知度 10.4%(Q2)' },
      { id: 'cross', c: 1, r: 3.1, kind: 'unit', label: 'クロスバイ', sub: '新製品の 51%\n(1 年前 40%)' },
      { id: 'bs', c: 2, r: 0, kind: 'key', label: 'B/S 貸出', sub: 'NIM 6.14%' },
      { id: 'lpb', c: 2, r: 1.1, kind: 'unit', label: 'LPB', sub: '配分 49% → 29%' },
      { id: 'tp', c: 2, r: 2.1, h: 0.82, kind: 'unit', label: 'Tech Platform・\nSoFiUSD', sub: '大口を除き +18%\n自社コアへ移行' },
      { id: 'fees', c: 2, r: 3.1, kind: 'unit', label: '手数料・会費', sub: '手数料型 +40%\n比率 42%' },
      { id: 'cap', c: 3, r: 0, kind: 'risk', label: '自己資本', sub: '比率 17.0%\n自給率 0.89(2027)' },
      { id: 'buyers', c: 3, r: 1.1, label: 'ローンの買い手', sub: '契約 100 億ドル超' },
    ],
    edges: [
      { from: 'sm', to: 'newm', label: '獲得', kind: 'money', n: 1 },
      { from: 'newm', to: 'dd', label: '給与振込', kind: 'money', n: 2, fo: -0.4, tof: -0.4 },
      { from: 'dd', to: 'money', label: '安い預金', kind: 'money' },
      { from: 'money', to: 'bs', label: '資金', kind: 'money', n: 3 },
      { from: 'ex', to: 'cross', label: '製品を足す', kind: 'goods', n: 4, lw: 0.93 },
      { from: 'cross', to: 'fees', label: '手数料', kind: 'money' },
      { from: 'cross', to: 'sm', label: '製品当たり\n獲得費 202 ドル', kind: 'ctrl', n: 5, lw: 0.95, fo: -0.3, tof: -0.3 },
      { from: 'bs', to: 'cap', label: '資本を使う', kind: 'risk', n: 6, lw: 0.86 },
      { from: 'bs', to: 'lpb', label: '抱えきれない分', kind: 'goods' },
      { from: 'lpb', to: 'buyers', label: '引き渡し', kind: 'goods' },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.66,
    mech: [
      '販促費(年 17.8 億ドル、収益の 32%)で会員を取る。\n純増は四半期 120 万人、会員当たり 370 ドル',
      '新しい会員が給与振込を設定して主口座になる。\n給与振込の比率は Q3 では未開示',
      '安い預金(倉庫ラインより 1.45pt 安い)が\nB/S 貸出を支え、NIM 6.14%',
      '既存会員が製品を足す。\nクロスバイは 1 年で 40% → 51%。\n製品純増 220 万件の過半が既存会員',
      'クロスバイ 51% で製品当たり獲得費は\n202 ドル(会員当たり 370 ドルの約半分)',
      'ただし貸出は自己資本を使う。自給率 0.89(2027)で、\nLPB への配分は 49% → 29% に下がった',
    ],
    reason: '連鎖は回っている(純増の過去最高、\nクロスバイ 51%)。律速は預金ではなく\n自己資本',
    up: '会員当たり販促費 330 ドル以下と\nクロスバイ 50% 超が続けば成長の価値が上がる',
    down: '会員当たり販促費の上昇が続き、\nLPB の配分が戻らなければ成長は資本で止まる',
  });
  return s;
};
