// 投資行動(指示書 spec/v4.md の H9 s37)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '時系列投資戦略(4 フェーズ)。判別 KPI は第3章(成長の尺度)・第4章と共通',
    source: '銘柄分析メソッド scenario-strategy §7、本資料 第3・4章・最終判断',
  });

  // 上段: 4 つの矢羽(x 0.5 から幅 3.0、重ね 0.1)。薄緑の矢羽だけ濃緑の文字
  const phases = [
    { label: '1 分割で建てる・検証期', fill: L.C.dark, font: L.C.white },
    { label: '2 エントリー期', fill: L.C.primary, font: L.C.white },
    { label: '3 本格保有期', fill: L.C.light, font: L.C.dark },
    { label: '4 再評価期', fill: L.C.teal, font: L.C.white },
  ];
  phases.forEach((p, i) => {
    const x = 0.5 + i * 2.9;
    s.addShape('chevron', { x, y: 1.7, w: 3.0, h: 0.7, fill: { color: p.fill }, line: { color: p.fill }, objectName: 'ovl_chev' + i });
    s.addText(p.label, { x, y: 1.7, w: 3.0, h: 0.7, fontFace: L.FONT, fontSize: 12, bold: true, color: p.font, align: 'center', valign: 'middle', margin: 0, isTextBox: true, objectName: 'ovl_chev_t' + i });
  });

  // 下段: フェーズごとの期間・やること・判別 KPI・撤退条件(2〜5 列は左揃え)
  L.table(s, [
    ['', '分割で建てる・検証期', 'エントリー期', '本格保有期', '再評価期'],
    ['期間', '今〜2027 年 Q2', '資本の弁が開いた後\n(16% 割れの四半期に LPB 40% 超)', 'ROTCE 12% 超かつ LPB の配分 40% 超が\n2 四半期続いた後', '株価が理論株価に近づいた後'],
    ['やること', '15.3〜21.4 ドルで分割、\n15.3 ドル以下は即時に買い増す', '15.3 超〜21.4 ドル以下で分割して建てる\n(15.3 ドル以下なら即時)', '確度に応じて増やす', '2027 年: 総自己資本比率\n16% 割れの四半期に LPB 40% 超なら\nN2 を上げ、強気の確率を見直す。\n差分を探し、なければ縮小する'],
    ['判別 KPI', 'Q4 決算: 総自己資本比率と LPB の割合、\nall-in 3.4% 以下、会員純増 110 万以上、\n手数料型 40% 以上', '同左を 2 四半期', 'ROTCE 12% 超かつ自給率 1 以上', '株価が示す PEG 1.275 以上\n(理論株価に到達)'],
    ['撤退条件', '増資、all-in 4.5% 超、\n2027 年見通しの引き下げ', '評価の純額 3 億ドル超、all-in 4.5% 超、\n増資、再表示', 'ROTCE が 2 四半期続けて 9% 未満', '差分の消失。\n損失率が 5.7%(保有の損益分岐)に\n近づく、または理論株価\n(その時点の再計算)を株価が上回る'],
  ], { x: 0.5, y: 2.55, w: 12.33, colW: [1.45, 2.72, 2.72, 2.72, 2.72], fontSize: 9, rowH: 0.62, align: ['left', 'left', 'left', 'left', 'left'] });

  // 下: 判別の規則(表の下端より下に置く)
  L.takeaway(s, 0.5, 5.95, 12.33, 0.7, '判別 KPI のうち 3 つ以上を 2 四半期続けて満たしたら、強気の確率を見直し、\n分割エントリーの上限を引き上げる');
};
