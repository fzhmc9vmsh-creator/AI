// 損益の流れ: 売上から営業損益までの滝グラフ(9か月、百万ドル)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { kicker: '売上から費用を順に引いていくと、手元に残る利益がどこで消えるかが見える', source: 'S-1/A-3 の機能別損益(注記 8)' });
  L.paneHead(s, 0.5, 1.62, 8.0, '売上から営業損益まで(9か月、百万ドル)', 'pane_wf_head');
  L.waterfall(s, [
    { label: '売上', val: 33242, type: 'total' },
    { label: '推論の\n計算資源\n(売上原価)', val: -4812, type: 'step' },
    { label: '見かけの粗利\n(85.5%)', val: 28430, type: 'total' },
    { label: 'クラウド事業者の手数料', val: -5086, type: 'step' },
    { label: '実質の粗利\n(70.2%)', val: 23344, type: 'total', highlight: true },
    { label: '研究開発', val: -19240, type: 'step', highlight: true },
    { label: '販売\n(手数料を\n除く)', val: -1533, type: 'step' },
    { label: '管理', val: -3831, type: 'step' },
    { label: '会計上の\n営業損益', val: -1260, type: 'total' },
  ], { x: 0.5, y: 2.2, w: 8.0, h: 3.95, name: 'wf' });
  L.lookBox(s, [
    { n: 1, text: '見かけの粗利率 85.5% は、\n推論の原価だけを引いた数字' },
    { n: 2, text: '手数料 5,086 は販売費に入っている。引くと実質の粗利率は 70.2%' },
    { n: 3, text: '研究開発 19,240(売上の 57.9%)が会計上の赤字の主因。株式報酬などを除いた調整後の営業利益は +4,081' },
  ], { x: 8.75, y: 2.0, w: 4.08, h: 4.1 });
  L.termNotes(s, [{ term: '実質の粗利率', plain: '売上から計算資源とCSPの手数料を引いた残りの比率', why: '見かけの粗利率85.5%では手元に残る分を見誤るため' }], { x: 0.5, y: 6.3, w: 12.33 });
};
