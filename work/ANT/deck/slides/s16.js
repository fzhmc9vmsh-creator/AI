// 2031年の姿: 売上から純利益までのサンキー図(当分析モデルの推定、百万ドル)。図は assets/sankey_s16.png
const path = require('path');
module.exports = function build(pres, L) {
  const { F } = L;
  const s = L.contentSlide(pres, { kicker: '左から右へ: 売上の内訳 → 粗利と原価 → 費用 → 営業利益 → 純利益(2031 年度、百万ドル)(数字は当分析モデルの推定)', source: '当分析の 5 か年コホート・リースモデル(2031 年度の基準)' });
  L.paneHead(s, 0.5, 1.62, 8.7, '2031 年度の損益の流れ(灰 = 売上、緑 = 利益、赤 = 費用)', 'pane_sk_head');
  s.addImage({ path: path.join(__dirname, '..', 'assets', 'sankey_s16.png'), x: 0.5, y: 2.0, w: 8.7, h: 4.2, altText: '2031 年度の損益のサンキー図', objectName: 'sankey_s16' });
  L.marks(s, [
    { x: 5.55, y: 2.85, n: 1 },
    { x: 5.55, y: 4.95, n: 2 },
    { x: 7.24, y: 4.95, n: 3 },
  ]);
  L.kpiTiles(s, [
    { value: F('fcf.31', { noEst: true }), label: '2031 年の FCF\n(百万ドル)' },
    { value: F('opm.31', { noEst: true }), label: '営業利益率' },
    { value: F('roe.31', { noEst: true }), label: 'ROE' },
  ], { compact: true, x: 9.4, y: 2.0, w: 3.43, h: 1.2 });
  L.lookBox(s, [
    { n: 1, text: '研究開発の比率は今(9 か月)の 57.9% から 27.1% へ下がる前提(p.14 の確度は中)' },
    { n: 2, text: '営業利益率 29.8%、純利益 78,965' },
    { n: 3, text: '最も変わるのは現金の流れ。支払い義務の 91.8% を消化し、FCF は 75,839 の回収側' },
  ], { x: 9.4, y: 3.35, w: 3.43, h: 2.85 });
  L.termNotes(s, [{ term: 'ROE', plain: '純利益 ÷ 自己資本。株主のお金で稼ぐ力', why: '将来の資本の使い方を評価するため' }], { x: 0.5, y: 6.3, w: 12.33 });
};
