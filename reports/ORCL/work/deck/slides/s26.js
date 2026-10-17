// 条件10 陳腐化リスク(評価 B): 資産 → 回収の経路 ← 価値を下げる力。下に時間軸
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 資産 → 回収の経路 ← 価値を下げる力。下: 資産ごとの寿命と契約の長さ。①〜⑤ は右と対応',
    source: 'research3/W2_gpu_economic_life.md、会社開示(耐用年数の変更、Q1 FY27 説明会)、JPMorgan AM の試算、Amazon 10-K',
    grade: 'B', condNo: 10,
  });
  // 行の間の通路(箱と箱の間の空き)の高さ。図の領域 y 1.66・h 3.75・行数 3 から求める
  const Y = 1.66, H = 3.75, top = Y + 0.4, pitch = (Y + H - 0.3 - top) / 3;
  const lane12 = top + 2 * pitch;     // 行 1 と行 2 の間の通路の中心
  L.flowMap(s, {
    name: 's26', y: Y, h: H, cols: [1.45, 1.55, 1.35, 1.45], rows: 3, nodeH: 0.74,
    lanes: [
      { label: '資産', c0: 0, c1: 0 },
      { label: 'Oracle の回収', c0: 1, c1: 2, self: true },
      { label: '価値を下げる力', c0: 3, c1: 3 },
    ],
    nodes: [
      { id: 'intang', c: 0, r: 0, kind: 'ok', label: 'DB の技術・顧客関係', sub: '寿命は数十年' },
      { id: 'gpu', c: 0, r: 1, kind: 'risk', label: 'GPU(自社調達)', sub: '6 年償却\n(5 → 6 年に延長)' },
      { id: 'soft', c: 0, r: 2, label: 'OCI のソフト', sub: '世代交代が速い' },
      { id: 'maint', c: 1, r: 0, kind: 'unit', label: '保守・SaaS', sub: '継続課金' },
      { id: 'first', c: 1, r: 1, kind: 'unit', label: '最初の契約', sub: '5〜6 年\n契約 ≒ 償却期間' },
      { id: 'renew', c: 1, r: 2, kind: 'unit', label: '更新・再販', sub: '従来比 +20%\n(Q1 FY27)' },
      { id: 'cust', c: 2, r: 0, label: 'DB・SaaS の顧客', sub: '保守料' },
      { id: 'lab', c: 2, r: 1, label: 'AI 研究所・企業', sub: '初回の契約料\n更新料' },
      { id: 'nv', c: 3, r: 0, kind: 'risk', label: 'NVIDIA の新世代', sub: 'Rubin は電力あたり\n約 10 倍' },
      { id: 'amzn', c: 3, r: 1, kind: 'risk', label: 'Amazon の判断', sub: 'サーバーの耐用年数を\n6 → 5 年に短縮' },
      { id: 'used', c: 3, r: 2, label: '中古 GPU 市場', sub: '中古 H100 は新品の\n61% → 69%' },
    ],
    edges: [
      { from: 'intang', to: 'maint', kind: 'goods', n: 1 },
      { from: 'gpu', to: 'first', kind: 'goods', n: 2, ldx: -0.2 },
      { from: 'gpu', to: 'renew', kind: 'goods' },
      { from: 'cust', to: 'maint', label: '保守料', kind: 'money' },
      { from: 'lab', to: 'first', kind: 'money' },
      { from: 'lab', to: 'renew', kind: 'money', n: 3, lpos: 'v', ldy: -0.2 },
      { from: 'nv', to: 'gpu', label: '置き換えを迫る', kind: 'risk', n: 4, fs: 'b', ts: 't', ldy: 0.1425 },
      { from: 'amzn', to: 'gpu', label: '寿命の見方', kind: 'risk', fs: 'b', ts: 'b', my: lane12, ldy: 0.1425, ldx: 1.2 },
      { from: 'used', to: 'renew', label: '再販の値', kind: 'ctrl' },
    ],
  });
  L.timeBand(s, {
    x: 0.5, y: 5.5, w: 8.55, h: 1.1, from: 2027, to: 2047, step: 5, name: 's26tb', fmt: (t) => 'FY' + (t % 100),
    bars: [
      { label: 'GPU の最初の契約', from: 2027, to: 2032, color: L.C.primary, text: '5〜6 年' },
      { label: 'GPU の償却', from: 2027, to: 2033, color: L.C.amber, text: '6 年' },
      { label: '⑤ 建屋のリース', from: 2027, to: 2045, color: L.C.light, text: '15〜19 年(GPU の 2〜3 世代分)' },
      { label: 'DB の技術・顧客関係', from: 2027, to: 2047, color: L.C.dark, text: '数十年' },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.66, mechH: 2.45,
    mech: [
      'DB の技術と顧客関係は数十年使われ、保守料で回収が続く',
      'GPU は最初の 5〜6 年の契約で償却の大半を回収する(契約期間 ≒ 償却期間)',
      '更新期の GPU は従来比 +20% で更新・再販。CoreWeave も H100 を元の 95% で再契約',
      '新世代(Rubin は電力あたり約 10 倍)が出ると、電力が限られる中で旧世代の置き換えを迫られる',
      '建屋のリースは 15〜19 年で GPU の 2〜3 世代分。需要が鈍れば固定費として残る',
    ],
    reason: '経済的寿命が会計の耐用年数以上であることを\n示す証拠が優勢。ただし電力制約の下での\n世代交代の速さが残るため B',
    up: '大型契約の更新(2031 年〜)で元の単価の\n6 割以上が確認できれば A',
    down: '更新プレミアムが 0% 以下に落ちれば C\n(3 年耐用なら EPS −17%、JPMorgan AM の試算)',
  });
  return s;
};
