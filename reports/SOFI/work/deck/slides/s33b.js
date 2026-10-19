// 5-2 確率の節点ツリー(複合構成。手本: s08d の札、s04・s35 の表)
// 左: 4 節点の札(良い側の中身・確率・根拠 +/−)/ 右上: 束の表 / 右下: 市場との比較 / 下: takeaway
module.exports = function build(pres, L) {
  const { C, FONT } = L;
  const s = L.contentSlide(pres, {
    kicker: '確率は基準(事業エンジン)より良い側に振れる確率。振れ幅は対称。N1・N2 は信用(N3)に条件付き。16 通りを加重。組み合わせごとに構造を判定し、その許容 PEG で価値を出す',
    source: 'calc/growth_v3.py・out/growth_v3.json、research_r3/R12(参照クラス)、research/R4(マクロ)',
  });

  // ---------- 左: 4 節点の札 ----------
  const LX = 0.5, LW = 6.7;
  L.paneHead(s, LX, 1.62, LW, '4 つの節点(良い側に振れる確率と根拠)', 'pane_l');
  const nodes = [
    { id: 'n1', name: 'N1 獲得効率', good: '会員の伸び・販促費率・NIM が\n基準より良い', p: 55, cond: '信用が良いとき 65%、\n悪いとき 48%',
      plus: '製品の前年比 43%(加速)・クロスバイ 51%', minus: '会員当たり販促費 +17%' },
    { id: 'n2', name: 'N2 資本の転換', good: 'LPB が基準より伸び、資本の上限を\n超えた分を受ける', p: 41, cond: '信用が良いとき 55%、\n悪いとき 30%',
      plus: '契約 100 億ドル超', minus: 'LPB 37→31 億ドル・金利上昇・\n買い手は衝撃時に 3 回中 2 回引いた' },
    { id: 'n3', name: 'N3 信用', good: 'all-in 貸倒率が 3.7% より良い\n(3.2%。悪い側は 4.2%)', p: 43, cond: 'N1・N2 の\n確率の条件になる',
      plus: '純償却 2.62%(同業 3.2〜4.2%)・固定金利', minus: '失業率 4.2%・業界の延滞の上昇' },
    { id: 'n4', name: 'N4 新しい収益線', good: 'Tech Platform の伸びが 8〜10% を\n上回る、SoFiUSD', p: 50, cond: '',
      plus: '前期比 +12.5%・自社利用', minus: '貢献利益率の低下' },
  ];
  const CY0 = 2.0, CH = 0.93, CG = 0.07;
  nodes.forEach((n, i) => {
    const y = CY0 + i * (CH + CG);
    // 札の背景(薄緑)と、左の濃緑の帯(節点名)
    L.box(s, LX, y, LW, CH, { fill: C.tint, line: C.tint, name: 'ovl_card_' + n.id });
    L.box(s, LX, y, 0.07, CH, { fill: C.dark, line: C.dark, name: 'ovl_cardbar_' + n.id });
    L.text(s, n.name, { x: LX + 0.17, y: y + 0.07, w: 2.2, h: 0.26, fontSize: 11, bold: true, color: C.dark, margin: 0, valign: 'middle', objectName: 'node_n_' + n.id });
    L.text(s, n.good, { x: LX + 0.17, y: y + 0.36, w: 2.2, h: 0.5, fontSize: 8.5, color: C.text, margin: 0, objectName: 'node_g_' + n.id });
    // 確率(大きな数字)と条件付き確率
    L.text(s, [{ text: String(n.p), options: { fontSize: 22, bold: true, color: C.primary } }, { text: '%', options: { fontSize: 12, bold: true, color: C.primary } }],
      { x: LX + 2.45, y: y + 0.05, w: 1.1, h: 0.42, margin: 0, valign: 'middle', objectName: 'node_p_' + n.id });
    // 確率の棒(幅は確率に比例)
    s.addShape('rect', { x: LX + 2.45, y: y + 0.5, w: 0.9, h: 0.06, fill: { color: C.white }, line: { color: C.white }, objectName: 'ovl_ptrack_' + n.id });
    s.addShape('rect', { x: LX + 2.45, y: y + 0.5, w: 0.9 * n.p / 100, h: 0.06, fill: { color: C.primary }, line: { color: C.primary }, objectName: 'ovl_pfill_' + n.id });
    if (n.cond) L.text(s, n.cond, { x: LX + 2.45, y: y + 0.6, w: 1.3, h: 0.3, fontSize: 8, color: C.sub, margin: 0, objectName: 'node_c_' + n.id });
    // 根拠: + は緑、− は赤(記号と本文を別の箱にして、折り返しの 2 行目を本文の頭に揃える)
    const ex = LX + 3.8, LH = 0.145;
    const pl = n.plus.split('\n').length, mi = n.minus.split('\n').length;
    const tot = (pl + mi) * LH + 0.05;
    let ey = y + (CH - tot) / 2;
    [['+', C.primary, n.plus, pl, 'p'], ['−', C.red, n.minus, mi, 'm']].forEach(([mk, col, tx, ln, k]) => {
      L.text(s, mk, { x: ex, y: ey, w: 0.14, h: ln * LH, fontSize: 8.5, bold: true, color: col, margin: 0, objectName: 'node_m' + k + '_' + n.id });
      L.text(s, tx, { x: ex + 0.15, y: ey, w: LW - 3.95 - 0.1, h: ln * LH, fontSize: 8.5, color: C.text, margin: 0, objectName: 'node_e' + k + '_' + n.id });
      ey += ln * LH + 0.05;
    });
  });

  // ---------- 右上: 束の表 ----------
  const RX = 7.45, RW = 5.38;
  L.paneHead(s, RX, 1.62, RW, '4 節点を束ねた結果(16 通りの加重)', 'pane_r');
  const bold = { bold: true, color: C.dark };
  const key = (t) => ({ text: t, options: Object.assign({ fill: { color: C.tint } }, bold) });
  L.table(s, [
    ['束', '定義', '確率', '理論株価', '構造(PEG)'],
    [key('強気\n(うまくいった場合)'), key('N1 と N2 が\nともに良い側'), key('23.6%'), key('31.2'), key('A(1.33〜1.43)')],
    ['ベース', '片方だけ\n良い側', '48.9%', '21.5', 'B〜C'],
    ['弱気', 'N1 と N2 が\nともに悪い側', '27.5%', '12.9', 'C(1.0)'],
    ['4 節点すべて成功', '—', '7.7%', '34.3', 'A(1.43)'],
    ['4 節点すべて失敗', '—', '10.4%', '11.4', 'C(1.0)'],
    [{ text: '期待値\n(16 通りの加重)', options: bold }, '—', '—', { text: '21.4\n(標準偏差 7.1)', options: bold }, '—'],
  ], { x: RX, y: 2.0, w: RW, colW: [1.51, 1.02, 0.58, 1.15, 1.12], fontSize: 9, rowH: 0.36, align: ['left', 'left', 'center', 'center', 'center'], name: 'tbl_bundle' });

  // ---------- 右下: 市場との比較 ----------
  L.paneHead(s, RX, 4.65, RW, '市場との比較', 'pane_r2');
  L.bullets(s, [
    '株価 14.55 ドルは弱気(12.9)とベース(21.5)の間。\n株価が示す PEG は 0.85(構造 C の水準)',
    'N1・N2 を ±10pt 動かした期待値は 19.8〜23.1 ドルで、どれも株価を上回る',
    '強気(31.2)は 2028 年 EPS 1.28 ドル × 構造 A の PEG。\nアナリストの最高目標(Citi 30 ドル)と近い',
  ], { x: RX, y: 4.99, w: RW, h: 1.12, fontSize: 9, gap: 3, name: 'bul_market' });

  // ---------- 下: takeaway ----------
  L.takeaway(s, 0.5, 6.15, 12.33, 0.6, 'うまくいった場合は構造 A で 31.2 ドル(確率 24%)。期待値 21.4 ドルは株価の 1.47 倍で、弱気でも 12.9 ドル(株価の −11%)');
  return s;
};
