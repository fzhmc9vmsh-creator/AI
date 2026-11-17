// 結論: KPI の札 4 枚 + 左にキーメッセージ 5 本 + 右に市場との差分の表 + takeaway
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, { kicker: '', source: '会社決算説明資料(2026年12月期3Q)、有価証券報告書、当方の計算(valuate.py)' });
  L.kpiTiles(s, [
    { value: F('price.last'), label: '株価(2026-11-16)', color: C.sub },
    { value: `${F('deck.theory')}`, label: '理論株価(エンジン)', note: '資本コスト8.9%' }, // lint-ok: 台帳に無い手書き(当方の資本コスト)
    { value: F('val.decision.last'), label: '判断', color: C.dark },
    { value: `≤ ${F('deck.z2')}`, label: '分割圏', note: `即時は ${F('deck.z1')}以下` },
  ], { y: 1.62, h: 1.2, compact: true });
  const msgs = [
    'iBow本体の1ST単価は横ばいで、成長は契約数とアップセルの2本',
    '契約数は業界の新規開設(年約2,450件で3年横ばい)に縛られ、伸びは13.5%→約9%に減速',
    '定額の競合より2.7倍高くても流出は減り、解約・粗利・FCFの質は高い',
    '株価は資本コスト約7.5%を前提にし、理論株価との差640円の7割は倍率',
    '見送り。1,465円以下で分割、2027年2月・5月・7月の数字で見直す',
  ];
  L.paneHead(s, 0.5, 2.98, 6.3, 'キーメッセージ', 'pane_msg');
  msgs.forEach((m, i) => {
    const y = 3.34 + i * 0.5;
    s.addShape('ellipse', { x: 0.5, y: y + 0.07, w: 0.28, h: 0.28, fill: { color: i === 4 ? C.dark : C.primary }, line: { color: C.primary }, objectName: 'ovl_k_c' + i });
    L.text(s, 'K' + (i + 1), { x: 0.5, y: y + 0.07, w: 0.28, h: 0.28, fontSize: 8, bold: true, color: C.white, align: 'center', valign: 'middle', margin: 0, objectName: 'ovl_k_n' + i });
    L.text(s, m, { x: 0.9, y, w: 5.9, h: 0.44, fontSize: 10.5, valign: 'middle', margin: 0, bold: i === 4, objectName: 'msg' + i });
  });
  L.paneHead(s, 7.1, 2.98, 5.73, '市場の前提と当方の差', 'pane_diff');
  L.table(s, [
    ['項目', '市場の前提', '当方'],
    ['資本コスト', '約7.5%', '8.9%'],
    ['3年のEPS成長', '約19〜21%(会社計画)', '16.4%'],
    ['顧客単価(2028年)', '110.3千円', '102.5千円'],
    ['年間の新規獲得', '約660件', '約660件(加速の兆候なし)'],
  ], { x: 7.1, y: 3.34, w: 5.73, colW: [1.6, 2.0, 2.13], fontSize: 10, rowH: 0.42, name: 'tbl_diff' });
  L.takeaway(s, 7.1, 5.62, 5.73, 1.1, `基準のEPSでも倍率が17〜20倍に収れんすれば年率リターンは ${F('calc.irr_172')}〜${F('calc.irr_20')} で資本コスト並み。安全余裕が無い`, { fontSize: 10.5 }); // lint-ok: 台帳に無い手書き(17〜20倍)
};
