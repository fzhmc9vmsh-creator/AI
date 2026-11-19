// 結論: 専門用語・略語を使わない。上に 4 枚の札、下に理由の表と結論の箱
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, { source: '当分析(S-1/A-3 と価値評価)',});
  L.kpiTiles(s, [
    { value: '見送り', label: '判断', color: C.dark },
    { value: F('fair'), label: '適正株価' },
    { value: F('ipo.hi'), label: '公開価格の上限' },
    { value: F('entry'), label: '分割で買う上限' },
  ], { y: 1.7, h: 1.55 });
  const rows = [
    ['理由', '中身', '詳しく'],
    ['今の構造', '利用量に応じて課金するAIモデルの首位だが、計算資源の長期の支払いが売上より先に積み上がる事業', 'p.9'],
    ['将来の確度', '利益の最大の伸びしろ(研究開発費の比率の低下)は確度が中', 'p.14'],
    ['リスク', '需要が鈍ると支払いだけが残る筋が、起きる確率を掛けた損失で最大', 'p.19'],
    ['値段', '公開価格は、成長が計画どおり満額実現する前提の値段', 'p.22・p.25'],
  ];
  L.table(s, rows, { x: L.M, y: 3.5, w: 12.33, colW: [2.2, 8.13, 2.0], fontSize: 11, rowH: 0.46, align: ['left', 'left', 'center'], name: 'concl_tbl' });
  L.takeaway(s, L.M, 6.0, 12.33, 0.62, `次に確かめる日: 来年8月の決算。手元に残る粗利の比率 ${F('kpi.gm')} 以上・研究開発費の比率 ${F('kpi.rd')} 未満なら買いを考え直す`);
};
