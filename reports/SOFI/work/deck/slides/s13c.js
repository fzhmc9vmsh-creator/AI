// 金利の両面(指示書 spec/v4.md の s13c 節)。左上: 経路ごとの効果の表 / 右上: 1 株当たりの横棒 / 左下: 市場の反応との比較 / 右下: 預金の価格
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '金利 +100bp の経路ごとの効果(税引前、億ドル。1 年目と 3 年目)と 1 株当たりの価値への効果、市場の反応との比較',
    source: 'research_r4/R15_rate_two_sided.md(10-Q の NII 感応度・ヘッジ・預金ベータ)、calc/A4_q3_memo.md(金利の両面)、research/R3a_market_hypothesis.md(KBW)、research_r5/Q3_datasheet.md',
  });
  const LX = 0.5, LW = 7.7, RX = 8.45, RW = 4.38;
  const pos = { color: L.C.primary, bold: true }, neg = { color: L.C.red, bold: true };
  const c = (text, o) => ({ text, options: o });

  // 左上: 経路ごとの効果(+ の行は緑の字、− の行は赤の字)
  L.paneHead(s, LX, 1.62, LW, '経路ごとの効果(+100bp、税引前・億ドル)');
  L.table(s, [
    ['経路', '1 年目', '3 年目', '根拠'],
    [c('貸出の再価格(+)', pos), c('+1.7', pos), c('+3.3', pos), '個人 261 億ドルは 1 年で 55%、学生 161 億ドルは\n15% が組成の入れ替え'],
    [c('現金・有価証券(+)', pos), c('+0.7', pos), c('+0.7', pos), '約 66 億ドル(全額変動の上限)'],
    [c('預金のコスト(−)', neg), c('−2.7〜−3.9', neg), c('同', neg), '預金 455 億ドル × ベータ 0.60〜0.85'],
    [c('NII の合計', { bold: true }), c('−0.4〜−1.5\n(会社の表 −1.0)', { bold: true }), c('+0.1〜+1.3', { bold: true }), '負債感応型は 1 年目だけ'],
    [c('貸倒(−)', neg), c('0〜−0.65', neg), c('同', neg), '固定金利で返済額は不変。景気の経路のみ'],
    [c('評価減(一時)', neg), c('総額 −7.5〜−10.5\nヘッジ後 0〜−3.2', neg), c('保有分は戻る', neg), 'スワップ 287 億ドル。上期は益 > 評価減'],
  ], { x: LX, y: 1.98, w: LW, colW: [1.5, 1.6, 1.1, 3.5], fontSize: 9, rowH: 0.28, align: ['left', 'center', 'center', 'left'], name: 'tbl_paths' });

  // 右上: 1 株当たり(横棒 1 系列。値は負なので、項目名は左端(low)に置く)
  L.paneHead(s, RX, 1.62, RW, '1 株当たり(ドル)');
  s.addChart(pres.charts.BAR, [
    { name: '1 株当たり(ドル)', labels: ['NII', '貸倒', '評価減(一時)', '資本コスト +1pt', '合計(両面)'], values: [-0.07, -0.20, -0.08, -0.18, -0.54] },
  ], L.chartStyle({
    x: RX, y: 1.98, w: RW, h: 1.8, barDir: 'bar', chartColors: [L.C.red, L.C.red, L.C.red, L.C.red, L.C.dark],
    catAxisOrientation: 'maxMin', catAxisLabelPos: 'low', valAxisMinVal: -0.75, valAxisMaxVal: 0, valAxisHidden: true, valGridLine: { style: 'none' },
    dataLabelFormatCode: '0.00', dataLabelPosition: 'outEnd', showLegend: false, barGapWidthPct: 45, objectName: 'chart',
  }));
  L.text(s, '資本コストを倍率まで下げてみると −0.54 で、合計 −0.90', { x: RX, y: 3.8, w: RW, h: 0.3, fontSize: 8.5, color: L.C.sub, objectName: 'note_chart' });

  // 左下: 市場の反応との比較(Q3 の結果の行を追加)
  L.paneHead(s, LX, 4.22, LW, '市場の反応との比較(1 株当たり、ドル)');
  L.table(s, [
    ['項目', '値'],
    ['経済的な影響(+100bp、両面の合計)', '−0.54〜−0.90'],
    ['KBW の報道の日の下落(10/14)', '−1.05'],
    ['KBW の「ヘッジ前 10 億ドル超」を税引後に', '−0.58'],
    ['ヘッジ後の評価減の推計', '0〜−0.18'],
    ['年初来の下落(25.1 → 14.55)', '−10.55(金利で説明できるのは 5〜9%)'],
    ['Q3 の結果', '割引率 +59〜82bp でも EPS 0.18 で上振れ、NIM +16bp'],
  ], { x: LX, y: 4.56, w: LW, colW: [3.6, 4.1], fontSize: 9, rowH: 0.22, align: ['left', 'center'], name: 'tbl_market' });

  // 右下: 預金の価格(Q3 の基本金利・上乗せ・同業・前期比)
  L.paneHead(s, RX, 4.22, RW, '預金の価格');
  L.table(s, [
    ['項目', '値'],
    ['9/16 の利上げ後の基本 APY', '3.30%(据え置き)'],
    ['新規の上乗せ', '+1.10%(10/20、最大 4.40%)'],
    ['同業', 'Ally・Amex 3.10%、\nMarcus 3.50%、Chime 最大 4.00%'],
    ['預金の前期比', '+58 億ドル'],
  ], { x: RX, y: 4.56, w: RW, colW: [1.9, 2.48], fontSize: 9, rowH: 0.26, align: ['left', 'center'], name: 'tbl_deposit' });

  L.takeaway(s, 0.5, 6.2, 12.33, 0.6, '金利の痛みは「評価減の総額」で語られるが、両面の合計は小さく、評価減はヘッジで相殺され保有分は戻る。市場の反応は経済的な影響を上回る');
};
