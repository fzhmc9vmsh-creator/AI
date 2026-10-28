// 条件5 経営者の能力(評価 B): 経歴 → 現職 → 担う事業 → 結果。指示書 spec/v4.md の H6 の s21 節
// 箱は 14: 経歴の gs と tw は 1 箱(Goldman・NFL・Twitter)にまとめた
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 経歴(どこで何を築いたか)→ 現職 → 担う事業 → 結果(Q3 2026 まで)。①〜⑤ は右と対応。経歴は会社発表・報道の要約に基づく',
    source: 'research/R3b_management.md、research_r2/R9_products_people.md(会社発表・DEF 14A・Form 4 の要約)、research_r5/Q3_datasheet.md(Q3 の 8-K・説明会の要約)',
    grade: 'B', condNo: 5,
  });
  L.flowMap(s, {
    name: 's21', h: 5.0, cols: [1.5, 1.45, 1.4, 1.45], rows: 4, nodeH: 0.82,
    lanes: [{ label: '経歴', c0: 0, c1: 0 }, { label: '経営陣と担う事業', c0: 1, c1: 2, self: true }, { label: '結果', c0: 3, c1: 3 }],
    nodes: [
      { id: 'gt', c: 0, r: 0, h: 1.03, kind: 'ok', label: 'Goldman・\nNFL・Twitter', sub: 'Noto: GS 1999〜\n2004 パートナー\nNFL 2008〜10\nTwitter CFO 2014〜17' },
      { id: 'uber', c: 0, r: 1, label: 'Goldman・Uber', sub: 'Lapointe: GS 2012〜15\nUber 2015〜18' },
      { id: 'cons', c: 0, r: 2, rs: 2, kind: 'ok', label: '消費者金融・\n資産運用', sub: 'JPM 住宅ローン CFO・\nCapital One・\nCitizens/Schwab・JPM' },
      { id: 'noto', c: 1, r: 0, kind: 'self', label: 'Noto\n(CEO)', sub: '2018-02 就任\nWest Point・Wharton', tag: { text: '⑤ 報酬は TBV の総額', tone: 'amber' } },
      { id: 'lap', c: 1, r: 1, kind: 'self', label: 'Lapointe\n(CFO)', sub: '2018 入社\n2020-09 CFO' },
      { id: 'sch', c: 1, r: 2, kind: 'self', label: 'Schuppenhauer\n(貸出の責任者)', sub: '2024-08 入社' },
      { id: 'keo', c: 1, r: 3, kind: 'self', label: 'Keough\n(FS の責任者)', sub: '2023-03 入社' },
      { id: 'bank', c: 2, r: 0, kind: 'unit', label: '銀行化と資本', sub: '免許・増資・資本配分' },
      { id: 'fin', c: 2, r: 1, kind: 'unit', label: '財務とガイダンス', sub: '利益計画・開示' },
      { id: 'lend', c: 2, r: 2, kind: 'unit', label: '個人・学生・\n住宅ローン', sub: '与信と SoFi Bank' },
      { id: 'fsb', c: 2, r: 3, kind: 'unit', label: '預金・投資・保険', sub: 'Spend・Invest・\nProtect・Save' },
      { id: 'res1', c: 3, r: 0, kind: 'ok', label: '銀行免許 2022 年\nGAAP 黒字 Q4 2023', sub: '約束した時期どおり' },
      { id: 'res2', c: 3, r: 1, kind: 'ok', label: 'Q3 も上振れ', sub: '収益・EPS 上振れ\n2026 年見通し増額\n2027 年 EPS 0.90 提示' },
      { id: 'res3', c: 3, r: 2, h: 0.9, kind: 'risk', label: '未達と未検証', sub: '上場時の 2024 年\n予測に収益 −7%\nTechnisys の効果は\n未検証' },
    ],
    edges: [
      { from: 'gt', to: 'noto', label: '資本市場・\n上場企業財務', kind: 'ctrl' },
      { from: 'uber', to: 'lap', label: '財務・成長', kind: 'ctrl' },
      { from: 'cons', to: 'sch', label: '消費者金融', kind: 'ctrl' },
      { from: 'cons', to: 'keo', label: '資産運用', kind: 'ctrl' },
      { from: 'noto', to: 'bank', kind: 'ctrl', n: 1 },
      { from: 'lap', to: 'fin', kind: 'ctrl', n: 2 },
      { from: 'sch', to: 'lend', kind: 'ctrl', n: 3 },
      { from: 'keo', to: 'fsb', kind: 'ctrl', n: 4 },
      { from: 'bank', to: 'res1', kind: 'ctrl' },
      { from: 'fin', to: 'res2', kind: 'ctrl' },
      { from: 'lend', to: 'res3', kind: 'ctrl' },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.66,
    mech: [
      'Noto は GS で資本市場、\nTwitter で上場企業の財務を担った。\n銀行免許(2022)と GAAP 黒字(Q4 2023)\nを約束どおり達成',
      'Lapointe は GS・Uber で財務を担い、\n2025 年は利益計画(EPS 0.25〜0.27)を上回る 0.39',
      '貸出は JPM 住宅ローン CFO・Capital One・\nCitizens の消費者金融を経た\nSchuppenhauer が率いる',
      '預金・投資・保険は Schwab・JPM で資産運用を担った Keough が率いる',
      '報酬の PSU は TBV の総額の伸びに連動し、\n1 株当たりではない。増資で総額は伸びる。\nCEO は 2026 年に約 225 万ドル\n(15.73〜18.06 ドル)を買い増し、1,228 万株を保有',
    ],
    reason: 'その事業を築いた経験の持ち主が\n貸出と預金を率い、約束の実行力は高い。\n報酬が 1 株当たりでない点で B',
    up: '報酬を 1 株当たりの指標に切り替え、\nROTCE 目標の時期を示せば A',
    down: '利益計画の下方修正か、\n低い株価での増資なら C',
  });
  return s;
};
