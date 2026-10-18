// 条件7(評価 C): 安い理由の検証。指示書 spec/ch3.md の s23 節
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 市場の懸念(出所)→ 懸念の対象 → 事実 → 判定。①〜④ は右と対応。株価は 2026 年 EPS の 24.3 倍、2027 年の 17.2 倍',
    source: 'research/R3a_market_hypothesis.md(Muddy Waters・KBW・Morgan Stanley・BofA の要約)、research_r2/R5_credit_fv.md・R7_funding_rates_capital.md・R6_pnl_margin.md',
    grade: 'C', condNo: 7,
  });
  L.flowMap(s, {
    name: 's23', h: 4.66, cols: [1.5, 1.4, 1.6, 1.1], rows: 4,
    lanes: [{ label: '市場の懸念', c0: 0, c1: 0 }, { label: 'SoFi(懸念の対象)', c0: 1, c1: 1, self: true }, { label: '事実', c0: 2, c1: 2 }, { label: '判定', c0: 3, c1: 3 }],
    nodes: [
      { id: 'd1', c: 0, r: 0, label: '会計への疑い(MW)', sub: '実質の貸倒 6.1%\n未計上の債務\n3.12 億ドル' },
      { id: 'd2', c: 0, r: 1, kind: 'risk', label: '金利と公正価値(KBW)', sub: 'Q3 に\n10 億ドル超の逆風' },
      { id: 'd3', c: 0, r: 2, kind: 'risk', label: '資本を食う成長(MS)', sub: '成長が資本集約的' },
      { id: 'd4', c: 0, r: 3, kind: 'risk', label: '利益が付いてこない(BofA)', sub: '売上は上方修正\n利益計画は据え置き' },
      { id: 'o1', c: 1, r: 0, kind: 'unit', label: '貸倒と損失の前提', sub: '公正価値の\n損失前提 4.8%' },
      { id: 'o2', c: 1, r: 1, kind: 'unit', label: 'ローンの評価', sub: 'マーク 個人 104.7%' },
      { id: 'o3', c: 1, r: 2, kind: 'unit', label: '自己資本', sub: '比率 18.8%' },
      { id: 'o4', c: 1, r: 3, kind: 'unit', label: '下期の利益計画', sub: '通期 EPS 0.60 ドル' },
      { id: 'e1', c: 2, r: 0, kind: 'ok', label: '前提 4.8% > all-in 3.7%', sub: '売却した延滞債権を\n足し戻しても内側' },
      { id: 'e2', c: 2, r: 1, kind: 'risk', label: '割引率が薄い', sub: '個人 4.97%・学生 4.29%\nQ3 ヘッジ前\n−4.5〜6.5 億ドル' },
      { id: 'e3', c: 2, r: 2, kind: 'risk', label: '比率の低下', sub: '半年で 22.9% → 18.8%' },
      { id: 'e4', c: 2, r: 3, kind: 'risk', label: '下期に高い増分利益率', sub: '増分 EBITDA 率 53〜64%\n(前年は 36%)' },
      { id: 'v1', c: 3, r: 0, kind: 'ok', label: '会計の不正は\n裏付けが弱い' },
      { id: 'v2', c: 3, r: 2, rs: 2, kind: 'risk', label: '金利・資本・\n信用は\n実在のリスク' },
    ],
    edges: [
      { from: 'd1', to: 'o1', label: '疑い', kind: 'risk', n: 1 },
      { from: 'o1', to: 'e1', kind: 'ctrl' },
      { from: 'e1', to: 'v1', kind: 'ctrl' },
      { from: 'd2', to: 'o2', label: '疑い', kind: 'risk', n: 2 },
      { from: 'o2', to: 'e2', kind: 'ctrl' },
      { from: 'e2', to: 'v2', kind: 'ctrl' },
      { from: 'd3', to: 'o3', kind: 'risk', n: 3 },
      { from: 'o3', to: 'e3', kind: 'ctrl' },
      { from: 'e3', to: 'v2', kind: 'ctrl' },
      { from: 'd4', to: 'o4', kind: 'risk', n: 4 },
      { from: 'o4', to: 'e4', kind: 'ctrl' },
      { from: 'e4', to: 'v2', kind: 'ctrl' },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.32,
    mech: [
      'MW は実質の貸倒 6.1% を主張。会社の公正価値の損失前提 4.8% は、売却した延滞債権を足し戻した all-in 3.7% より高く、利益の水増しの裏付けは弱い',
      'ただし割引率は個人 4.97%・学生 4.29% と薄い。Q3 の金利上昇(+55〜60bp)でヘッジ前 −4.5〜6.5 億ドルの評価減を見込む',
      '資本比率は半年で 4.1pt 下がった。成長を続けるには LPB か増資が要る',
      '下期の利益計画は増分 EBITDA 率 53〜64%\nを要する。ただし EBITDA 計画の据え置きは、\n増収分を販促に再投資した結果(裁量)',
    ],
    reason: '安さの主因は金利・資本・信用という\n実在のリスク。「利益が付いてこない」は\n裁量の再投資のため、全体は C',
    up: 'Q3 のマークが 104% 以上、\nall-in 貸倒率 4.0% 以下、下期の計画を達成すれば B',
    down: 'マークが 103% 未満、all-in 4.8% 超、\n再表示があれば D',
  });
  L.kpiBand(s, '個人ローンのマーク 104% 以上で B 候補・103% 未満で D 候補 / all-in 貸倒率 4.0% 以下で確度を上げ・4.8% 超で D 候補(損失前提を超える)/ 再表示・当局の調査で E 候補(毎四半期)');
  return s;
};
