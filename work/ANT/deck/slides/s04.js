// 2-1 会社の一枚紹介: 上に主要な数字 4 枚、下に「何者か」を 4 段の表で
module.exports = function build(pres, L) {
  const { F, C } = L;
  const s = L.contentSlide(pres, {
    kicker: '上: 会社の規模を表す 4 つの数字。下: 何を・どう稼ぎ・どこで売り・どう統治されるかの 4 段',
    source: 'S-1/A-3',
  });
  L.kpiTiles(s, [
    { value: F('arr.oct'), label: '年換算売上(10月末、百万ドル)' },
    { value: F('rev.9m'), label: '9か月の売上(百万ドル)' },
    { value: F('rev.usage.pct'), label: '従量課金の比率', note: '使った量に応じた課金' },
    { value: F('big.cust'), label: '年 10 万ドル以上の顧客(社)' }, // lint-ok: 指示書の顧客の定義(数字は台帳)
  ], { y: 1.66, h: 1.45 });
  const lab = (t) => ({ text: t, options: { bold: true, color: C.dark, fill: { color: C.tint } } });
  L.table(s, [
    ['問い', '答え'],
    [lab('何を売るか'), 'AI モデル「Claude」を API で企業に貸す。ほかに開発ツール Claude Code と、社員向けの席の契約'],
    [lab('どう稼ぐか'), '使った量に応じた従量課金が 79.1%、定額の契約が 20.9%'],
    [lab('どこで売るか'), '直販が 56%、クラウド事業者経由が 44%'],
    [lab('上場と統治'), '米国 Nasdaq に上場(公開価格の仮条件 70〜78 ドル)。公益を目的に含む会社で、信託が取締役の過半を選ぶ'],
  ], { x: 0.5, y: 3.3, w: 12.33, colW: [2.0, 10.33], fontSize: 11.5, rowH: 0.58, align: ['left', 'left'] });
  L.termNotes(s, [
    { term: 'API', plain: 'ソフトから他のソフトの機能を呼び出す窓口。ここではAIモデルの貸し出し', why: '売上の8割がAPIの従量課金のため' },
    { term: 'ARR', plain: '直近の月の売上を12倍した年換算売上', why: '急成長企業の今の規模を測るため' },
    { term: '従量課金', plain: '使った量に応じて払う料金', why: '売上が顧客の利用量で伸び縮みする仕組みを見るため' },
  ], { x: 0.5, y: 6.25, w: 12.33 });
  return s;
};
