// 損益フロー(サンキー)。図は assets/make_sankey.py で作る
// 箇条書きの続きの行: 記号を出さず(空白の記号)、字下げだけ先頭行にそろえる
const CONT = { bullet: { characterCode: '00A0', indent: 12 } };
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    title: 'Q1 FY27 の売上 193 億ドルから GAAP 営業利益 67 億ドルが残る。費用の最大項目は AI 容量を含むクラウドの原価である',
    kicker: '損益フロー(サンキー)、Q1 FY27(2026 年 6〜8 月)、10 億ドル。( )は前年同期比。GAAP 基準',
    source: 'Oracle FY27 Q1 決算発表・10-Q(2026-09)。非GAAP との差: 株式報酬 11.3 億・無形資産償却 2.0 億・リストラ等 0.9 億ドル',
    page: 9,
  });
  s.addImage({ path: 'assets/sankey_q1fy27.png', x: 0.5, y: 1.6, w: 8.4, h: 5.0 });
  L.takeaway(s, 9.05, 1.7, 3.78, 1.45, 'クラウド・ソフトの原価が +77% と売上(+33%)の 2 倍以上の速さで伸び、同部門の粗利率は 72.0% → 62.7% に下がった');
  L.bullets(s, [
    [{ text: '営業利益 +24.5 億ドル(+57%)は、', options: { breakLine: true, paraSpaceAfter: 0 } }, { text: '営業費の減少 8.8 億ドル(うち', options: Object.assign({ breakLine: true, paraSpaceAfter: 0 }, CONT) }, { text: '償却とリストラの減少 5.4 億)に支えられた', options: CONT }],
    'GAAP 営業利益率 34.8%(非GAAP 42%)。差は株式報酬と償却',
    [{ text: '構成比: クラウド 60%・ソフトウェア 29%・', options: { breakLine: true, paraSpaceAfter: 0 } }, { text: 'サービス 7%・ハード 4%', options: CONT }],
    '原価の伸びは、AI 容量の稼働前の費用(電力・賃料)を含む',
  ], { x: 9.05, y: 3.3, w: 3.78, h: 3.3, fontSize: 10.5 });
};
