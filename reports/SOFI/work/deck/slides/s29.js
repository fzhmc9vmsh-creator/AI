// 条件13 アーキタイプ照合(評価 C)。指示書 spec/ch3.md の s29 節どおり
// 型: 流れ図(原型と 5 つの要素)+ 表 + 右パネル(根拠・評価理由・監視 KPI)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '条件13(総合)アーキタイプ照合: ORCL 型(継続課金・低い陳腐化)か MU 型(景気循環)・VRT 型・AVGO 型か',
    source: '会社開示(Q2 2026 決算)、research_r2/R5_credit_fv.md、calc/out/val.json',
    grade: 'C', condNo: 13,
  });
  L.flow(s, [
    { head: '原型', boxes: [{ text: 'ORCL 型', tone: 'key', h: 0.9 }] },
    { head: 'A', boxes: [{ text: '預金・FS 手数料', tone: 'on', h: 0.9 }] },
    { head: 'B', boxes: [{ text: 'LPB(資本を\n使わない手数料)', tone: 'on', h: 0.9 }] },
    { head: 'C', boxes: [{ text: '学生ローン(B/S)', tone: 'in', h: 0.9 }] },
    { head: 'D', boxes: [{ text: '個人ローン(B/S)', tone: 'off', h: 0.9 }] },
  ], { x: 0.5, y: 1.75, w: 8.3, h: 1.5, gap: 0.15 });
  L.table(s, [
    ['観点', 'ORCL 型の要素', 'MU 型の要素'],
    ['課金', '預金の利ざや・継続手数料(収益の約 76%)', '売却益は組成と市況で変わる(約 24%)'],
    ['信用の損失', 'LPB は損失を買い手が負う', '個人ローン組成の 71% を自社で保有\n(Q4 2025 は 51%)'],
    ['資本', 'LPB と手数料は資本を使わない', '貸出の伸びが資本を食い、\n比率は半年で −4.1pt'],
    ['技術', '会員の基盤は長く使える', 'Galileo は内製化で縮小(AVGO 型の商品化)'],
  ], { x: 0.5, y: 3.55, w: 8.3, colW: [2.3, 3.0, 3.0], fontSize: 10, rowH: 0.4 });
  L.t15Side(s, {
    evidence: ['個人ローン組成のうち自社で保有する比率\n51% → 71%(Q4 2025 → Q2 2026)\nB/S 保有の組成 38 → 76 億ドル', 'all-in 貸倒率 3.7%。景気後退で +0.75pt なら理論株価 −1.9 ドル', 'ROTCE が資本コストを超えるのは 2029〜30 年'],
    reason: '原型は ORCL 型に近いが、自社で抱える\n個人ローンの比率が上がり MU 型に寄るため C',
    kpi: '個人ローン組成の自社保有の比率 65% 未満で B 候補・75% 超で D 候補(毎四半期)',
  });
};
