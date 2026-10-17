// 条件5(評価 B、A との境界): 経歴から評価し直す。指示書 spec/r6_cond.md の s21 節
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 経歴(どこで何を築いたか)→ 現職 → 担う事業 → 結果。①〜⑤ は右と対応。経歴は報道・会社発表の要約に基づく',
    source: 'research4/T7_executives.md(Oracle 発表・8-K 2025-09-22・2026-04-06、Bloomberg・Reuters ほか)、DEF 14A(報酬)、会社開示(FY26〜27 のガイダンス)',
    grade: 'B', condNo: 5,
  });
  L.flowMap(s, {
    name: 's21', h: 5.0, cols: [1.5, 1.45, 1.4, 1.45], rows: 4, nodeH: 0.82,
    lanes: [{ label: '経歴', c0: 0, c1: 0 }, { label: '経営陣と担う事業', c0: 1, c1: 2, self: true }, { label: '結果', c0: 3, c1: 3 }],
    nodes: [
      { id: 'aws', c: 0, r: 0, label: 'AWS(〜2014)', sub: 'クラウド基盤の\n技術者 約 6〜7 年' },
      { id: 'prim', c: 0, r: 1, label: 'Primavera(1993〜)', sub: '技術者 → CTO\n2008 年に\nOracle が買収' },
      { id: 'aes', c: 0, r: 2, kind: 'ok', label: 'AES・Schneider', sub: '電力・インフラ企業の\n財務 約 12 年・約 10 年' },
      { id: 'found', c: 0, r: 3, label: 'Oracle 創業(1977)', sub: 'DB 事業を起こす' },
      { id: 'mag', c: 1, r: 0, kind: 'self', label: 'Magouyrk\n(共同 CEO)', sub: '2014 年に OCI を創設\nGen2 を設計・統括' },
      { id: 'sic', c: 1, r: 1, kind: 'self', label: 'Sicilia\n(共同 CEO)', sub: '業種別事業を統括\nアプリを AI で再構築' },
      { id: 'max', c: 1, r: 2, kind: 'self', label: 'Maxson\n(CFO)', sub: '2026-04 就任\nCEO に報告' },
      { id: 'ell', c: 1, r: 3, label: 'Ellison\n(会長・CTO)', sub: '株式 約 41%\nキーパーソン' },
      { id: 'oci', c: 2, r: 0, kind: 'unit', label: 'OCI・AI 容量', sub: 'IaaS +121%' },
      { id: 'app', c: 2, r: 1, kind: 'unit', label: 'アプリ・業種別', sub: 'SaaS +10%\nOracle Health' },
      { id: 'cap', c: 2, r: 2, kind: 'unit', label: 'capex と資金調達', sub: 'FY27 総額\n900〜950 億ドル' },
      { id: 'pay', c: 2, r: 3, kind: 'risk', label: '業績連動の報酬\n(PSO)', sub: 'KPI は FY28 総売上\n(1 株指標ではない)' },
      { id: 'rpo', c: 3, r: 0, kind: 'ok', label: '受注残\n6,640 億ドル', sub: 'GPU 更新 +20%' },
      { id: 'va', c: 3, r: 1, kind: 'risk', label: 'VA の電子カルテ', sub: '2026-03 に全国障害\n上限 100 億ドルを\n早期消化' },
      { id: 'over', c: 3, r: 2, kind: 'risk', label: 'capex の超過', sub: 'FY26 見通し\n350 → 500 → 実績\n557 億ドル' },
      { id: 'gap', c: 3, r: 3, kind: 'risk', label: '1 株価値とのずれ', sub: '総額の拡大に\n報酬が連動' },
    ],
    edges: [
      { from: 'aws', to: 'mag', label: '基盤の技術', kind: 'ctrl', n: 1 },
      { from: 'prim', to: 'sic', label: '業種別ソフト', kind: 'ctrl', n: 2, lw: 0.6 },
      { from: 'aes', to: 'max', label: '電力の財務', kind: 'ctrl', n: 3 },
      { from: 'found', to: 'ell', kind: 'ctrl' },
      { from: 'mag', to: 'oci', kind: 'ctrl' },
      { from: 'sic', to: 'app', kind: 'ctrl' },
      { from: 'max', to: 'cap', kind: 'ctrl' },
      { from: 'ell', to: 'pay', label: '取締役会', kind: 'ctrl' },
      { from: 'oci', to: 'rpo', label: '受注と更新', kind: 'goods' },
      { from: 'app', to: 'va', label: '導入の遅れ', kind: 'risk' },
      { from: 'cap', to: 'over', kind: 'risk', n: 4 },
      { from: 'pay', to: 'gap', kind: 'risk', n: 5 },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.66,
    mech: [
      'Magouyrk は AWS でクラウド基盤を担い、2014 年に OCI を創設。\n今の成長エンジンを設計した当事者',
      'Sicilia は Primavera の技術者から CTO。\n買収後は業種別アプリを統括。Oracle Health(VA)は障害と遅れが続く',
      'CFO の Maxson は電力会社の AES と電機の Schneider で財務を約 22 年。\n設備と電力の資金計画に合うが、就任 6 か月',
      'capex は FY26 に見通し 350 → 500 → 実績 557 億ドル。\n共同 CEO の資本配分の実績はまだ 1 年',
      '業績連動の報酬の KPI は FY28 の総売上で、1 株当たりの指標ではない(80% は時間ベース)',
    ],
    reason: '経歴と事業の適合は高い(A 相当)。ただし CEO としての資本配分の実績が 1 年と短く、capex の超過と総額 KPI の報酬が残るため B(A との境界)',
    up: 'FY27 の capex が見通しの範囲に収まり、FCF の黒字化の時期を示せば A',
    down: 'capex が再び見通しを 10% 超上回るか、VA の契約で損失が出れば C',
  });
  return s;
};
