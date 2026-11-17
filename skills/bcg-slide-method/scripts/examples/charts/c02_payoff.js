// c02_payoff.js 非対称ペイオフ棒(手本): 現在値からの上振れ・下振れと買う価格帯を L.payoffBar + L.marks + L.kpiTiles + L.lookBox + L.takeaway で描く
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    source: '本分析の価値評価モデル(手本)。現在値・シナリオ別理論株価・確率・買う価格帯は手本用の固定値',
  });

  L.paneHead(s, 0.5, 1.62, 7.7, 'シナリオ別の理論株価と現在値からの上振れ・下振れ(円)', 'pane_po_head');

  L.payoffBar(s, {
    price: 786,
    unit: '円',
    rows: [
      { label: '最悪の筋', value: 553, note: '2022年型の利益率崩れ' },
      { label: '弱気', value: 896, p: 0.12 },
      { label: '基準', value: 1020, p: 0.70 },
      { label: '強気', value: 1556, p: 0.18 },
    ],
    zones: [
      { from: 553, to: 775, label: '即時 775円以下' },
      { from: 775, to: 890, label: '分割 775〜890円' },
    ],
  }, { x: 0.55, y: 2.02, w: 7.60, h: 3.22, name: 'po' });

  L.marks(s, [
    { x: 5.05, y: 2.56, n: 1, text: '下値は約3割', side: 'right' },
    { x: 6.10, y: 3.81, n: 2, text: '上値+30%が中心', side: 'right' },
    { x: 5.55, y: 3.19, n: 3, text: '弱気でも+14%', side: 'right' },
  ]);

  L.kpiTiles(s, [
    { value: '1,102円', label: '確率加重の期待値\n(現在値786円比 +40%)' }, // lint-ok: 手本用の固定値
    { value: '88%', label: '現在値を上回る確率\n(基準70% + 強気18%)' }, // lint-ok: 手本用の固定値
    { value: '775〜890円', label: '分割エントリー圏\n(即時エントリーは775円以下)' }, // lint-ok: 手本用の固定値
  ], { compact: true, x: 0.55, y: 5.42, w: 7.60, h: 1.26 });

  L.lookBox(s, [
    { n: 1, text: '最悪の筋(553円)でも下値は約3割。\n2022年型の利益率崩れを織り込んだ底' },
    { n: 2, text: '基準(1,020円・確率70%)で+30%。\n強気(1,556円)と合わせ88%で上振れ' },
    { n: 3, text: '弱気(896円)でも現在値786円を上回り、\n現在値は分割圏(775〜890円)の下限近く' },
  ], { x: 8.45, y: 2.02, w: 4.38, h: 3.22 });

  L.takeaway(s, 8.45, 5.42, 4.38, 1.26,
    '下値−30%に対し基準+30%・期待値1,102円と非対称。\n現在値786円は分割圏の下限近く、Q3で持続性を確かめる', // lint-ok: 手本用の固定値
    { fontSize: 10 });
};
