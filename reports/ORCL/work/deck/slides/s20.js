// 条件4(評価 S)。指示書 spec/ch3_conditions.md の s20 節どおり(構造図なし。KPI タイル 3 枚 + 下の帯)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: 'NYSE 上場の米国企業で、審査の前提条件を満たす', kicker: '条件4 日本株か米国株', source: 'NYSE 上場銘柄情報', page: 20, grade: 'S', condNo: 4 });
  L.kpiTiles(s, [
    { value: 'NYSE', label: '上場市場', note: 'ティッカー ORCL' },
    { value: '米ドル', label: '取引通貨', note: '米国の普通株' },
    { value: '充足', label: '判定', note: 'ゲート条件。減点要素なし' },
  ]);
  L.takeaway(s, 0.5, 3.6, 12.33, 0.7, 'ゲート条件のため構造図は不要。評価の集計には S として数える');
  return s;
};
