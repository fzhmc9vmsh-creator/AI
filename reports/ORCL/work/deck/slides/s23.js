// 条件7(評価 C): 安い理由の検証。指示書 spec/r6_cond.md の s23 節
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 市場の疑い → 疑いの対象 → 証拠 → 判定。①〜④ は右と対応。株価は事業実態 EPS の 13.3 倍(弱気シナリオの値とほぼ同じ)',
    source: 'Investor Day 2026-10-28、需給エンジン第4.4版(calc/out/m9_all.json)、research2/R5_credit.md、research4/T2_company_rpo_capacity.md、research3/W2_gpu_economic_life.md、Bloomberg(2026-10-08)、S&P(2026-07)',
    grade: 'C', condNo: 7,
  });
  L.flowMap(s, {
    name: 's23', h: 4.66, cols: [1.5, 1.4, 1.6, 1.1], rows: 4,
    lanes: [{ label: '市場の疑い', c0: 0, c1: 0 }, { label: 'Oracle(疑いの対象)', c0: 1, c1: 1, self: true }, { label: '証拠', c0: 2, c1: 2 }, { label: '判定', c0: 3, c1: 3 }],
    nodes: [
      { id: 'd1', c: 0, r: 0, label: 'GPU 寿命の悲観', sub: '「2〜3 年で陳腐化」' },
      { id: 'd2', c: 0, r: 1, label: 'FCF の J カーブ', sub: 'FY29 まで赤字' },
      { id: 'd3', c: 0, r: 2, kind: 'risk', label: 'OpenAI への集中', sub: '受注残の約 45%' },
      { id: 'd4', c: 0, r: 3, kind: 'risk', label: '信用リスク', sub: 'CDS 277bp\n(10 月中旬 300bp 前後)' },
      { id: 'o1', c: 1, r: 0, kind: 'unit', label: 'GPU(自社調達)', sub: '6 年償却' },
      { id: 'o2', c: 1, r: 1, kind: 'unit', label: 'capex', sub: 'FY27\n900〜950 億ドル' },
      { id: 'o3', c: 1, r: 2, kind: 'unit', label: '受注残', sub: '6,640 億ドル' },
      { id: 'o4', c: 1, r: 3, kind: 'unit', label: '借入と格付け', sub: 'BBB−(S&P)' },
      { id: 'e1', c: 2, r: 0, kind: 'ok', label: '更新・再販 +20%', sub: 'H100 を元の 95% で\n再契約した例' },
      { id: 'e2', c: 2, r: 1, label: '会社の資金計画', sub: 'FY29 FCF 300 億以上\n追加調達 200 億が上限' },
      { id: 'e3', c: 2, r: 2, kind: 'risk', label: 'OpenAI の資金', sub: '2026〜30 年の FCF\n累計 −2,780 億ドル' },
      { id: 'e4', c: 2, r: 3, kind: 'risk', label: 'S&P の条件', sub: 'FY29 までに FOCF\n黒字でなければ\n再格下げ' },
      { id: 'v1', c: 3, r: 0, kind: 'ok', label: '見落とし', sub: '機会' },
      { id: 'v2', c: 3, r: 1, label: '一部見落とし', sub: '時期は不確か' },
      { id: 'v3', c: 3, r: 2, kind: 'risk', label: '実在', sub: '罠' },
      { id: 'v4', c: 3, r: 3, kind: 'risk', label: '実在', sub: '罠' },
    ],
    edges: [
      { from: 'd1', to: 'o1', label: '寿命を疑う', kind: 'risk' },
      { from: 'o1', to: 'e1', label: '反証', kind: 'ctrl', n: 1 },
      { from: 'e1', to: 'v1', kind: 'ctrl' },
      { from: 'd2', to: 'o2', label: '赤字を疑う', kind: 'risk' },
      { from: 'o2', to: 'e2', label: '裏付け', kind: 'ctrl', n: 2 },
      { from: 'e2', to: 'v2', kind: 'ctrl' },
      { from: 'd3', to: 'o3', label: '集中を疑う', kind: 'risk' },
      { from: 'o3', to: 'e3', label: '支払いは\n調達頼み', kind: 'risk', n: 3, lw: 0.85 },
      { from: 'e3', to: 'v3', kind: 'risk' },
      { from: 'd4', to: 'o4', label: '信用を疑う', kind: 'risk' },
      { from: 'o4', to: 'e4', label: '債券も\n同じ見方', kind: 'risk', n: 4, lw: 0.85 },
      { from: 'e4', to: 'v4', kind: 'risk' },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.32,
    mech: [
      'GPU 寿命の悲観は、更新・再販 +20% と H100 の再契約(元の 95%)が反証する。\n市場の見落とし',
      'FCF の赤字は契約済み需要への\n先行投資(J カーブ)。会社は FY28 下期の黒字化と追加調達の上限を約束し、\nエンジンでも成り立つ',
      '受注残の約 45% は OpenAI。\nOpenAI の FCF は 2026〜30 年累計 −2,780 億ドルで、支払いは資金調達頼み',
      'CDS 277bp(5 年で 21% の倒産を織り込む)と\nS&P の条件は、債券市場がまだリスクを価格に入れている証拠',
    ],
    reason: '資金繰りの疑いには会社の数字の道筋が出た\n(B に近づく)。ただし事前の条件(CDS 200bp 未満・OpenAI 比率 40% 未満)は未達で、OpenAI 集中は実在のため C',
    up: 'OpenAI の比率が 40% 未満に下がり、CDS が 200bp 未満に戻れば B',
    down: 'CDS が 300bp を超えるか、FY29 より前に BB+ になれば D 候補',
  });
  L.kpiBand(s, 'CDS 5年 200bp 未満で B(現在 277bp)、300bp 超で D 候補 / FY29 より前の BB+ で D 候補 / OpenAI の比率 40% 未満で確度を上げ、契約変更・支払遅延の報道で E 候補');
  return s;
};
