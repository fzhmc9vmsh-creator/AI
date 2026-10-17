// 条件8(評価 C)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: 'DB は代替の利かない製品だが、価値の 45% を占める AI 容量は、需給が緩むと限界供給者の損益分岐で値が決まる商品になる', kicker: '条件8 コモディティではない(AVGO 型でない)', source: '需給エンジン第4.3版(セグメント価値)、research3/W3_industry_structure.md、ICE・CME の発表(2026-05)', page: 24, grade: 'C', condNo: 8 });
  L.structure(s, {
    nodes: [
      { id: 'db', col: 0, row: 0, label: 'Oracle DB・Database@', sub: '差別化あり', kind: 'ok' },
      { id: 'gpu', col: 0, row: 2, label: 'AI 容量(GPU 時間)', sub: '価値の 45%', kind: 'risk' },
      { id: 'lab', col: 2, row: 1, label: 'AI 研究所', sub: '最も安い容量を選ぶ', kind: 'ext' },
      { id: 'neo', col: 3, row: 0, label: 'ネオクラウド', sub: 'H100 で約 2.6 倍安い', kind: 'ext' },
      { id: 'fut', col: 3, row: 2, label: '計算の先物', sub: 'ICE・CME が準備', kind: 'risk' },
    ],
    edges: [
      { from: 'db', to: 'lab', label: 'データの近くで推論', kind: 'goods' },
      { from: 'gpu', to: 'lab', label: 'GPU 時間', kind: 'goods' },
      { from: 'neo', to: 'lab', label: '代替の容量', kind: 'goods' },
      { from: 'fut', to: 'gpu', label: '価格の標準化', kind: 'risk' },
    ],
    tags: [{ node: 'gpu', text: '緩和後の値下げ: Oracle 負担', tone: 'red' }, { node: 'db', text: '代替なし', tone: 'green' }],
  });
  L.t15Side(s, {
    evidence: ['セグメント価値(1株): AI 117、ソフト保守 45、SaaS 44、OCI 一般 31', '需給が緩んだ後の超過利益はベース 0%(NVIDIA の取り分、TPU、買い手の集中)', '推論トークンの価格は同等性能で年 9〜900 倍の速さで下落(Epoch)'],
    reason: '価値の半分近くが、緩和後に商品化する層にあるため C',
    kpi: 'AI 粗利率(最終開示 32%)が 25% 未満で D 候補・35% 以上で B 候補 / 更新プレミアム(+20%)が 0% 以下で D 候補 / H100 1年契約指数(2.65 ドル)が 2.00 ドル未満',
  });
};
