// 条件7(評価 A): 安い理由の検証(市場の懸念 → 経済的な大きさ → 株価が示す前提 → 判定)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 市場の懸念(出所)→ 経済的な大きさ(本資料の推計)→ 株価が示す前提 → 判定。①〜④ は右と対応',
    source: 'research/R3a(KBW・Morgan Stanley・BofA・Muddy Waters)、research_r4/R15・R17、research_r5/Q3_datasheet.md、calc/out/growth_v4.json の credit_capital',
    grade: 'A', condNo: 7,
  });
  L.flowMap(s, {
    name: 's23', h: 4.66, cols: [1.95, 1.95, 1.95, 1.4], rows: 4,
    lanes: [{ label: '市場の懸念', c0: 0, c1: 0 }, { label: '経済的な大きさ', c0: 1, c1: 1, self: true }, { label: '株価が示す前提', c0: 2, c1: 2 }, { label: '判定', c0: 3, c1: 3 }],
    nodes: [
      { id: 'd1', c: 0, r: 0, label: '金利と評価減(KBW)', sub: 'ヘッジ前で\n10 億ドル超の逆風' },
      { id: 'd2', c: 0, r: 1, label: '信用(景気)', sub: '失業率 4.2%\n業界の延滞の上昇' },
      { id: 'd3', c: 0, r: 2, label: '資本を食う成長(MS・KBW)', sub: '比率 9 か月で −5.9pt' },
      { id: 'd4', c: 0, r: 3, label: '利益が付いてこない(BofA)', sub: 'EPS 0.13 → 0.12 → 0.12\n→ 0.18(Q3)' },
      { id: 'e1', c: 1, r: 0, kind: 'unit', label: '両面で 約 −0.6 ドル', sub: 'ヘッジ後の評価減\n0〜−0.18 ドル' },
      { id: 'e2', c: 1, r: 1, kind: 'unit', label: '+1.0pt で 20.2 ドル', sub: '同業のピーク\nLC 5.0%・DFS 4.2%' },
      { id: 'e3', c: 1, r: 2, kind: 'unit', label: '下限まで 17 億ドル', sub: '信用 +1.0pt でも\n15.8% 以上\n増資 10 億で −2%' },
      { id: 'e4', c: 1, r: 3, kind: 'unit', label: 'EPS 0.18(増収で)', sub: '前期 0.12 から\n税・株数は未開示' },
      { id: 'm1', c: 2, r: 0, kind: 'risk', label: '報道の日 −1.05 ドル' },
      { id: 'm2', c: 2, r: 1, kind: 'risk', label: '損失率 +2.1〜2.7pt が\n毎年続く前提', sub: 'all-in 約 5.5〜6.1%' },
      { id: 'm3', c: 2, r: 2, kind: 'risk', label: '構造 C の PEG 0.80〜0.90' },
      { id: 'm4', c: 2, r: 3, kind: 'risk', label: 'EPS の横ばいを嫌う' },
      { id: 'v1', c: 3, r: 0, rs: 4, kind: 'ok', label: '株価の割引は\n経済的な大きさを\n大きく上回る\n(3 つ同時でも\n19.4 ドル)' },
    ],
    edges: [
      { from: 'd1', to: 'e1', kind: 'risk', n: 1 },
      { from: 'e1', to: 'm1', kind: 'ctrl' },
      { from: 'm1', to: 'v1', kind: 'ctrl' },
      { from: 'd2', to: 'e2', kind: 'risk', n: 2 },
      { from: 'e2', to: 'm2', kind: 'ctrl' },
      { from: 'm2', to: 'v1', kind: 'ctrl' },
      { from: 'd3', to: 'e3', kind: 'risk', n: 3 },
      { from: 'e3', to: 'm3', kind: 'ctrl' },
      { from: 'm3', to: 'v1', kind: 'ctrl' },
      { from: 'd4', to: 'e4', kind: 'risk', n: 4 },
      { from: 'e4', to: 'm4', kind: 'ctrl' },
      { from: 'm4', to: 'v1', kind: 'ctrl' },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.32,
    mech: [
      '金利 +100bp の両面の合計は約 −0.6 ドル。\n評価減はスワップ 287 億ドル(Q2)で相殺し、\n報道の日の下落 −1.05 ドルは\nヘッジ後の推計の 6 倍以上',
      '個人ローンの純償却は 2.26%\n(all-in 約 3.4%、同業 3.2〜4.2%)。株価は損失率 +2.1〜2.7pt が毎年続く前提で、LendingClub の 2023 年 5.0% も上回る',
      '資本は下限 14% まで 17 億ドル。\n信用 +1.0pt でも総自己資本比率は\n15.8% 以上で下限を割らない。\n経営陣は普通株の増資は不要と発言',
      'EPS は前期 0.12 から 0.18 に増え、\n増収で作られた。税率と株数は未開示',
    ],
    reason: '安い理由は実在するが、株価の割引は\n経済的な大きさを大きく上回る。\n確認 KPI と時期(Q4 決算)があり A',
    up: 'Q4 で評価の純額 1.5 億ドル以下・\nall-in 3.4% 以下・増資なしなら、S の候補',
    down: 'all-in 4.5% 超か普通株の増資なら B、\n損失率が 5.7%(損益分岐)に近づけば C',
  });
  L.kpiBand(s, 'ヘッジ後の評価の純額(Q4 の 10-K)/ all-in 損失率 3.4% 以下で確度を上げ・4.5% 超で B 候補 /\n普通株の増資で B 候補(毎四半期、次は Q4 決算)');
  return s;
};
