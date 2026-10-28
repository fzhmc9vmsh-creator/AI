// 条件13 アーキタイプ照合(評価 B)
// 型: 流れ図(原型と 5 つの要素)+ 表 + 右パネル(根拠・評価理由・監視 KPI)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '条件13(総合)アーキタイプ照合: 業界と比べた後に、経済の中身で ORCL 型(継続課金・低い陳腐化)と MU 型(景気循環で陳腐化する設備)・VRT 型・AVGO 型のどこかを決める',
    source: '会社開示(Q3 2026 決算)、research_r5/Q3_datasheet.md、research_r2/R5_credit_fv.md、research_r4/R16・R17、calc/out/growth_v4.json',
    grade: 'B', condNo: 13,
  });
  L.flow(s, [
    { head: '原型', boxes: [{ text: 'ORCL 型', tone: 'key', h: 0.9 }] },
    { head: 'A', boxes: [{ text: '預金・FS 手数料', tone: 'on', h: 0.9 }] },
    { head: 'B', boxes: [{ text: 'LPB(資本を\n使わない手数料)', tone: 'on', h: 0.9 }] },
    { head: 'C', boxes: [{ text: '学生ローン(B/S)', tone: 'in', h: 0.9 }] },
    { head: 'D', boxes: [{ text: '個人ローン(B/S)', tone: 'off', h: 0.9 }] },
  ], { x: 0.5, y: 1.75, w: 8.3, h: 1.5, gap: 0.15 });
  L.table(s, [
    ['観点', 'ORCL 型に近い要素', '貸し手(景気循環)の要素'],
    ['課金', '預金の利ざや・継続手数料\n(残高と利用に乗る)', '売却益は組成と市況で変わる'],
    ['信用の保有', '71% 保有は銀行の標準に近く、\n売却の選択肢あり', '信用の損失を負う\n(損益分岐 5.7%、実績 3.4%(Q3))'],
    ['資本', 'LPB と手数料は資本を使わない', '自給率 0.89(2027)→\n1.04(2028、エンジン)'],
    ['技術', '会員の基盤は長く使える。自社コアへ移行', 'Galileo の大口は内製化で離脱'],
  ], { x: 0.5, y: 3.55, w: 8.3, colW: [2.3, 3.0, 3.0], fontSize: 10, rowH: 0.4 });
  L.t15Side(s, {
    evidence: ['業界: 銀行はほぼ全額保有、LendingClub 21〜36%、Upstart 約 6%', '保有の資本 ROE 約 24% > 資本コスト 13.9%', 'MU 型は陳腐化する設備に資本を投じる型。信用の保有はそれに当たらない'],
    reason: '会員型の基盤(ORCL 型)と貸し手の間。\n保有は業界の標準で MU 型ではない。\n手数料の比率が上がれば A',
    kpi: '手数料型の比率 42%(Q3)。40% 超が 2 四半期で A 候補・35% 未満が続けば C 候補 / 個人ローンの保有比率は資本に応じて 50〜75%(毎四半期)',
  });
};
