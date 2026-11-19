// 損益の流れ: 売上から営業損益までのサンキー図(9か月、百万ドル)。図は assets/sankey_s08.png(assets/pl_sankey_local.py と s08.json から作る)
const path = require('path');
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { kicker: '左から右へ: 売上の内訳 → 粗利と原価 → 費用 → 営業損益(9 か月、百万ドル)', source: 'S-1/A-3 の機能別損益(注記 8)' });
  L.paneHead(s, 0.5, 1.62, 8.7, '売上から営業損益までの流れ(灰 = 売上、緑 = 粗利、赤 = 費用、斜線 = 営業損失)', 'pane_sk_head');
  s.addImage({ path: path.join(__dirname, '..', 'assets', 'sankey_s08.png'), x: 0.5, y: 2.0, w: 8.7, h: 4.2, altText: '9 か月の損益のサンキー図', objectName: 'sankey_s08' });
  L.marks(s, [
    { x: 4.3, y: 3.0, n: 1 },
    { x: 5.9, y: 4.8, n: 2 },
    { x: 5.9, y: 2.75, n: 3 },
  ]);
  L.lookBox(s, [
    { n: 1, text: '見かけの粗利率 85.5% は、推論の原価だけを引いた数字' },
    { n: 2, text: '販売費に入っているクラウド事業者の手数料 5,086 も引くと、実質の粗利率は 70.2%' },
    { n: 3, text: '研究開発 19,240(売上の 57.9%)が会計上の赤字の主因。株式報酬などを除いた調整後の営業利益は +4,081' },
  ], { x: 9.4, y: 2.0, w: 3.43, h: 4.2 });
  L.termNotes(s, [{ term: '実質の粗利率', plain: '売上から計算資源とCSPの手数料を引いた残りの比率', why: '見かけの粗利率85.5%では手元に残る分を見誤るため' }], { x: 0.5, y: 6.3, w: 12.33 });
};
