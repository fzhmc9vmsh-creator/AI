// 4-1 会社の計画: 4 つの要素が 2031 年の目標を支える
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左: 目標を支える 4 つの要素(現在 → 2031 年)。右: 目標。①〜④ は右の「仕組み」と対応(数字は当分析モデルの推定)',
    source: 'S-1/A-3、当分析の 5 か年コホートモデル',
  });
  L.flowMap(s, {
    name: 's12', h: 4.5, cols: [3.4, 2.6], rows: 4, nodeH: 0.7,
    lanes: [{ label: '支える要素', c0: 0, c1: 0 }, { label: '2031 年の目標', c0: 1, c1: 1, self: true }],
    nodes: [
      { id: 'dir', c: 0, r: 0, kind: 'unit', label: '直販の比率', sub: '56% → 61%' },
      { id: 'rd', c: 0, r: 1, kind: 'unit', label: '研究開発費の比率', sub: '2026年度 53.5% → 27.1%' },
      { id: 'cmp', c: 0, r: 2, kind: 'unit', label: '計算資源の自社確保', sub: '支払い義務の 91.8% を消化' },
      { id: 'rev', c: 0, r: 3, kind: 'unit', label: '5 つの製品群の売上', sub: '5.4 倍' },
      { id: 'goal', c: 1, r: 0, rs: 4, kind: 'key', label: '\n\n\n\n売上 302,075 百万ドル', sub: '(5.4 倍)\n\n営業利益率 29.8%' },
    ],
    edges: [
      { from: 'dir', to: 'goal', kind: 'goods', n: 1 },
      { from: 'rd', to: 'goal', kind: 'goods', n: 2 },
      { from: 'cmp', to: 'goal', kind: 'goods', n: 3 },
      { from: 'rev', to: 'goal', kind: 'goods', n: 4 },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.6, mechH: 2.9,
    mech: [
      '直販は手数料が無く、比率が上がるほど利益が残る',
      '研究開発費の比率が下がるほど営業利益率が上がる',
      '計算資源を先に確保し、支払い義務の大半を消化して現金を生む側へ移る',
      '5 つの製品群の売上がそろって伸びる',
    ],
    head: '計画の中身(図の ①〜④ と対応)',
    reason: 'なぜ 2031 年か: 会社の 5 か年計画の最終年で、支払い義務の大半が満期を迎え、現金の流れが投資先行から回収に変わる年', // lint-ok: 指示書の年
  });
  return s;
};
