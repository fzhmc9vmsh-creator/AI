// 条件1 競争優位の持続(評価 B)。指示書 spec/r6_cond.md の s17 節
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '左から: 顧客 → Oracle の事業 → 優位の源泉(壁)← 競合の圧力。下: 優位が続く期間。①〜④ は右と対応',
    source: '会社開示(Q1 FY27 説明会)、research4/T5_supply_components.md、research4/T3_saas_products.md、calc/prereg2.md §9(逼迫の終わり FY32)',
    grade: 'B', condNo: 1,
  });
  L.flowMap(s, {
    name: 's17', h: 3.75, cols: [1.45, 1.4, 1.45, 1.3], rows: 3, nodeH: 0.72,
    lanes: [{ label: '顧客', c0: 0, c1: 0 }, { label: 'Oracle の事業と優位の源泉', c0: 1, c1: 2, self: true }, { label: '競合・代替', c0: 3, c1: 3 }],
    groups: [{ label: '事業', c0: 1, c1: 1, r0: 0, r1: 2 }, { label: '優位の源泉(壁)', c0: 2, c1: 2, r0: 0, r1: 2 }],
    nodes: [
      { id: 'ent', c: 0, r: 0, label: 'DB の既存顧客', sub: '大企業・官公庁' },
      { id: 'apps', c: 0, r: 1, label: '業務アプリの顧客', sub: 'ERP・人事' },
      { id: 'lab', c: 0, r: 2, label: 'AI 研究所', sub: 'OpenAI・Meta・xAI' },
      { id: 'db', c: 1, r: 0, kind: 'unit', label: 'DB ライセンス・保守', sub: '保守は年 22%\nSoftware −3%' },
      { id: 'saas', c: 1, r: 1, kind: 'unit', label: 'SaaS', sub: '+10%' },
      { id: 'aicap', c: 1, r: 2, kind: 'unit', label: 'AI 容量', sub: '更新は従来比 +20%' },
      { id: 'sw', c: 2, r: 0, kind: 'ok', label: '切替コスト', sub: 'データ移行と\nアプリ改修に数年', tag: { text: '数十年', tone: 'green' } },
      { id: 'erp', c: 2, r: 1, kind: 'ok', label: '業務データの蓄積', sub: '移行は 8,500 社中\n約 1,000 社', tag: { text: '中', tone: 'amber' } },
      { id: 'tight', c: 2, r: 2, dy: -0.07, kind: 'risk', label: '業界全体の逼迫', sub: '電力・部材の不足\n(自社の優位ではない)', tag: { text: 'FY32 まで', tone: 'red' } },
      { id: 'hyper', c: 3, r: 0, label: 'AWS・Azure・\nGoogle', sub: 'DB 移行サービス' },
      { id: 'sap', c: 3, r: 1, label: 'SAP・Workday', sub: 'クラウド ERP +25%' },
      { id: 'neo', c: 3, r: 2, kind: 'risk', label: 'ネオクラウド・TPU', sub: 'H100 実勢は\n約 2.6 倍安い' },
    ],
    edges: [
      { from: 'ent', to: 'db', label: '保守料', kind: 'money', n: 1 },
      { from: 'apps', to: 'saas', label: '購読料', kind: 'money', n: 2 },
      { from: 'lab', to: 'aicap', label: '容量料\n+5%/年', kind: 'money', n: 3 },
      { from: 'sw', to: 'db', label: '顧客を囲う', kind: 'ctrl' },
      { from: 'erp', to: 'saas', label: '移行を促す', kind: 'ctrl' },
      { from: 'tight', to: 'aicap', label: '値上げを許す', kind: 'ctrl' },
      { from: 'hyper', to: 'sw', label: '移行の誘い', kind: 'risk' },
      { from: 'sap', to: 'erp', label: '乗り換えの誘い', kind: 'risk' },
      { from: 'neo', to: 'tight', label: '緩和後の\n値下げ', kind: 'risk', n: 4 },
    ],
  });
  L.text(s, '優位が続く期間', { x: 0.5, y: 5.5, w: 1.45, h: 0.2, fontSize: 8.5, bold: true, color: L.C.primary, valign: 'middle', margin: 0, objectName: 'ovl_s17_tbhead' });
  L.timeBand(s, {
    x: 0.5, y: 5.5, w: 8.55, h: 1.1, from: 2027, to: 2047, step: 5, name: 's17tb', fmt: (t) => 'FY' + (t % 100),
    bars: [
      { label: 'DB の切替コスト', from: 2027, to: 2047, color: L.C.dark, text: '数十年' },
      { label: 'AI 容量の単価優位', from: 2027, to: 2032, color: L.C.red, text: '逼迫が終わる FY32 まで' },
      { label: '建屋の賃料の固定', from: 2027, to: 2047, color: L.C.light, text: '長期リースで FY47 まで' },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.66, mechH: 2.0,
    mech: [
      'DB の顧客はデータ移行とアプリ改修に数年かかり、保守料(年 22%)を払い続ける',
      'SaaS は旧 ERP 顧客の移行で伸びるが +10% で、SAP のクラウド ERP(+25%)より遅い',
      'AI 容量は更新期の GPU を従来比 +20% で更新・再販。ただし業界全体の値上げ(AWS +15〜20%)の一部',
      '逼迫が緩む FY32 以降は、ネオクラウド・TPU との価格競争で超過利益はベースで 0%',
    ],
    reason: 'DB の優位は数十年続くが、\n価値の 41% を占める AI 容量の優位は\n逼迫が続く FY32 までに限られるため B',
    up: '緩和の兆しが出ても\nAI 容量の更新プレミアムが正のまま続けば A',
    down: 'Software の減収が −5% を超えて加速すれば C',
  });
  return s;
};
