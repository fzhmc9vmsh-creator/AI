// 条件7(評価 A): 安い理由の検証。左: 市場の疑いと市場の評価(CDS・社債)。中: Oracle の事業。右の列: 事業と資金の数字で判断した本当のリスク。判定は右のパネル(根拠は r8 台帳 J・K)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 市場の疑い・市場の評価 → Oracle の事業 → 事業と資金の数字で判断。①〜④ は右と対応。株価は価値の分布の 9 パーセンタイル(1,500 通り)',
    source: 'Investor Day 2026-10-28、需給エンジン第4.5版(calc/m10_mc.py・calc/out/m10_*.json、台帳 r8 J・K)、research2/R5_credit.md、research4/T2_company_rpo_capacity.md、research3/W2_gpu_economic_life.md、S&P(2026-07)',
    grade: 'A', condNo: 7,
  });
  L.flowMap(s, {
    name: 's23', h: 4.66, cols: [2.0, 1.9, 2.0], rows: 4,
    lanes: [{ label: '市場の疑い・評価', c0: 0, c1: 0 }, { label: 'Oracle(疑いの対象)', c0: 1, c1: 1, self: true }, { label: '事業と資金の数字で判断', c0: 2, c1: 2 }],
    nodes: [
      { id: 'd1', c: 0, r: 0, label: 'GPU 寿命の悲観', sub: '「2〜3 年で陳腐化」' },
      { id: 'd2', c: 0, r: 1, label: 'FCF の J カーブ', sub: 'FY29 まで赤字' },
      { id: 'd3', c: 0, r: 2, kind: 'risk', label: 'OpenAI への集中', sub: '受注残の約 45%' },
      { id: 'd4', c: 0, r: 3, kind: 'ext', label: 'CDS・社債\n(市場の評価)', sub: 'CDS 277bp・社債 263bp\n融資銀行のヘッジでも広がる' },
      { id: 'o1', c: 1, r: 0, kind: 'unit', label: 'GPU(自社調達)', sub: '6 年償却' },
      { id: 'o2', c: 1, r: 1, kind: 'unit', label: 'capex', sub: 'FY27\n900〜950 億ドル' },
      { id: 'o3', c: 1, r: 2, kind: 'unit', label: '受注残', sub: '6,640 億ドル' },
      { id: 'o4', c: 1, r: 3, kind: 'unit', label: '借入と格付け', sub: 'BBB−(S&P)' },
      { id: 'e1', c: 2, r: 0, kind: 'ok', label: '更新・再販 +20%', sub: 'H100 を元の 95% で\n再契約した例' },
      { id: 'e2', c: 2, r: 1, kind: 'ok', label: '会社の資金計画', sub: 'FY29 FCF 300 億以上\n追加調達 200 億が上限' },
      { id: 'e3', c: 2, r: 2, kind: 'risk', label: 'OpenAI の資金', sub: '2026〜30 年の FCF\n累計 −2,780 億ドル' },
      { id: 'e4', c: 2, r: 3, kind: 'risk', label: 'S&P の閾値', sub: 'FY29 までに FOCF 黒字\n建設の遅れで一時 BB+' },
    ],
    edges: [
      { from: 'd1', to: 'o1', label: '寿命を疑う', kind: 'risk' },
      { from: 'o1', to: 'e1', label: '反証', kind: 'ctrl', n: 1 },
      { from: 'd2', to: 'o2', label: '赤字を疑う', kind: 'risk' },
      { from: 'o2', to: 'e2', label: '裏付け', kind: 'ctrl', n: 2 },
      { from: 'd3', to: 'o3', label: '集中を疑う', kind: 'risk' },
      { from: 'o3', to: 'e3', label: '支払いは調達頼み', kind: 'risk', n: 3, lw: 0.9 },
      { from: 'd4', to: 'o4', label: '信用を疑う', kind: 'risk' },
      { from: 'o4', to: 'e4', label: '格付けの閾値', kind: 'risk', n: 4, lw: 1.2 },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.32,
    mech: [
      'GPU 寿命の悲観は、更新・再販 +20% と H100 の再契約(元の 95%)が反証する。市場の見落とし',
      'FCF の赤字は契約済み需要への先行投資。会社の約束は FY29 FCF 300 億ドル以上と、追加調達 200 億ドルの上限',
      '受注残の約 45% は OpenAI。OpenAI の FCF は 2026〜30 年累計 −2,780 億ドルで、支払いは資金調達頼み',
      'CDS・社債は市場の評価。本当の判定は格付けの閾値で、建設が遅れると一時 BB+ の確率 40%',
    ],
    reason: '市場が評価する信用リスクは、事業と資金の数字で裏付けられない(全 1,500 通りでレバレッジ最大 4.4 倍、倒産の道なし)。\n本当のリスクは OpenAI 集中と格付けの閾値のため S ではなく A',
    up: 'OpenAI の比率が 40% 未満に下がり、FY28 下期の FCF 黒字化を確かめれば S',
    down: 'OpenAI の契約見直し・支払い遅延か、FY29 FCF が赤字で BB+ が続けば B',
  });
  L.kpiBand(s, 'OpenAI の比率 40% 未満で S 候補・見直しや遅延で B / FY28 下期の FCF 黒字化・FY29 FCF 300 億ドル(遅れなしで 89%)/ 一時 BB+ の確率 40%(建設の遅れ・AI 否定の見方)');
  return s;
};
