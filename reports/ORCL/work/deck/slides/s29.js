// 条件13(評価 B)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: '保守・SaaS・Database@ は ORCL 型だが、自社で GPU を買う大型 AI 契約の部分が MU 型に寄る', kicker: '条件13(総合)アーキタイプ照合: ORCL 型か MU/VRT/AVGO 型か', source: '需給エンジン第4.3版、会社開示(FY27 capex ガイダンス)、research4/T2_company_rpo_capacity.md', page: 29, grade: 'B', condNo: 13 });
  L.flow(s, [
    { head: '原型', boxes: [{ text: 'ORCL 型', tone: 'key', h: 0.9 }] },
    { head: 'A', boxes: [{ text: '保守・SaaS', tone: 'on', h: 0.9 }] },
    { head: 'A', boxes: [{ text: 'Database@・OCI 一般', tone: 'on', h: 0.9 }] },
    { head: 'B', boxes: [{ text: 'AI 容量(前払い・持ち込み)', tone: 'in', h: 0.9 }] },
    { head: 'C〜G', boxes: [{ text: 'AI 容量(自社調達 GPU)', tone: 'off', h: 0.9 }] },
  ], { x: 0.5, y: 1.75, w: 8.3, h: 1.5, gap: 0.15 });
  L.table(s, [
    ['観点', 'ORCL 型の要素', 'MU 型の要素'],
    ['課金', '継続課金・従量・確約', '—'],
    ['陳腐化リスク', '前払い・持ち込みで顧客へ移す', '自社調達 GPU は Oracle が負う'],
    ['capex(FY27)', '純現金 capex 700 億ドル以下(ガイダンス)', 'エンジン 942 億ドル・純現金 733 億ドル'],
    ['価値の比率', '保守・SaaS・OCI 一般 約 50%', 'AI 容量 45%'],
  ], { x: 0.5, y: 3.55, w: 8.3, colW: [2.3, 3.0, 3.0], fontSize: 10, rowH: 0.4 });
  L.t15Side(s, {
    evidence: ['前払い・持ち込み累計 750 億ドル', '10GW の 90% 超はパートナーが資金負担', 'FY27 の総 capex 900〜950 億ドルのうち、顧客の前払いが約 24%'],
    reason: '原型は ORCL 型のまま。自社調達の GPU が増えると MU 型に寄るため B',
  });
};
