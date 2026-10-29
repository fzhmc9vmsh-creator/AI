// 確率の節点ツリー(指示書 spec/v4.md の s33b 節。複合構成。手本: s08d の札、s04・s35 の表)
// 左: 4 節点の札(良い側の中身・確率・根拠 +/−)/ 右上: 束の表 / 右下: 市場との比較 / 下: takeaway
module.exports = function build(pres, L) {
  const { C, FONT } = L;
  const s = L.contentSlide(pres, {
    kicker: '確率は基準(事業エンジン)より良い側に振れる確率。振れ幅は対称。N1・N2 は信用(N3)に条件付き。16 通りを加重。組み合わせごとに構造を判定し、その許容 PEG で価値を出す',
    source: 'calc/growth_v4.py・out/growth_v4.json(tree: p_nodes・bundles・combos)、research_r3/R12(参照クラス)、research/R4(マクロ)',
  });

  // ---------- 左: 4 節点の札 ----------
  const LX = 0.5, LW = 6.7;
  L.paneHead(s, LX, 1.62, LW, '4 つの節点(良い側に振れる確率と根拠)', 'pane_l');
  const nodes = [
    { id: 'n1', name: 'N1 獲得効率', good: '会員の伸び・販促費率・NIM が\n基準より良い', p: 59, cond: '信用が良いとき 68%、\n悪いとき 52%',
      plus: '純増 120 万(過去最高)・上方修正の記録', minus: '会員当たり販促費 370 ドル(+4%)' },
    { id: 'n2', name: 'N2 資本の転換', good: 'LPB が基準より伸び、資本の上限を\n超えた分を受ける', p: 43, cond: '信用が良いとき 57%、\n悪いとき 32%',
      plus: 'LPB 36 億ドル(+16%)・手数料型 42%', minus: 'LPB の割合 29% のまま・総自己資本 −1.8pt' },
    { id: 'n3', name: 'N3 信用', good: 'all-in 貸倒率が 3.4% より良い', p: 45, cond: 'N1・N2 の\n確率の条件になる',
      plus: '純償却 2.26%(同業 3.2〜4.2%)', minus: '失業率 4.2%・同業の延滞の上昇' },
    { id: 'n4', name: 'N4 新しい収益線', good: 'Tech Platform の伸びが 2027 年\n+15% を上回る', p: 55, cond: '',
      plus: '大口を除き +18%・貢献利益率 16%', minus: '新規契約の数字なし' },
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
    [key('強気\n(うまくいった場合)'), key('N1 と N2 が\nともに良い側'), key('26.6%'), key('33.5'), key('A(1.38〜1.43)')],
    ['ベース', '片方だけ\n良い側', '49.3%', '24.2', 'A〜C'],
    ['弱気', 'N1 と N2 が\nともに悪い側', '24.1%', '13.9', 'C(1.0)'],
    ['4 節点すべて成功', '—', '9.6%', '36.3', 'A(1.43)'],
    ['4 節点すべて失敗', '—', '8.1%', '12.2', 'C(1.0)'],
    [{ text: '期待値\n(16 通りの加重)', options: Object.assign({ align: 'left' }, bold) }, '—', '—', { text: '24.2\n(標準偏差 7.3)', options: Object.assign({ align: 'center' }, bold) }, '—'],
  ], { x: RX, y: 2.0, w: RW, colW: [1.51, 1.02, 0.58, 1.15, 1.12], fontSize: 9, rowH: 0.36, align: ['left', 'left', 'center', 'center', 'center'], name: 'tbl_bundle' });

  // ---------- 右下: 市場との比較 ----------
  L.paneHead(s, RX, 4.65, RW, '市場との比較', 'pane_r2');
  L.bullets(s, [
    '株価 14.55〜16.5 ドルは弱気(13.9)とベース(24.2)の間。\n株価が示す PEG は 0.80〜0.90(構造 C の 1.0 も下回る)',
    'N1・N2 を ±10pt 動かした期待値は 22.4〜26.0 ドルで、どれも株価を上回る',
    '強気(33.5)は 2028 年 EPS 1.34 × 構造 A の PEG',
  ], { x: RX, y: 4.99, w: RW, h: 1.12, fontSize: 9, gap: 3, name: 'bul_market' });

  // ---------- 下: takeaway ----------
  L.takeaway(s, 0.5, 6.15, 12.33, 0.6, 'うまくいった場合は構造 A で 33.5 ドル(確率 27%)。期待値 24.2 ドルで、弱気でも 13.9 ドル(14.55 の −4%)');
  return s;
};
