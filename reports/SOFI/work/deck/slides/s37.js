// 投資行動(指示書 spec/ch1_ch4.md の s37)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '時系列投資戦略(4 フェーズ)。判別 KPI は第3章の監視 KPI と共通',
    source: '銘柄分析メソッド scenario-strategy §7、本資料 第3章・最終判断',
  });

  // 上段: 4 つの矢羽(x 0.5 から幅 3.0、重ね 0.1)。薄緑の矢羽だけ濃緑の文字
  const phases = [
    { label: '1 待機・検証期', fill: L.C.dark, font: L.C.white },
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
    ['', '待機・検証期', 'エントリー期', '本格保有期', '再評価期'],
    ['期間', '今〜2027 年 Q2(4 四半期)', '合格した後、または\n株価 11.3 ドル以下', 'ROTCE 12% 超が\n2 四半期続いた後', '株価が理論株価に近づいた後'],
    ['やること', '建てずに判別 KPI を\n四半期ごとに確かめる', '11.3 ドル以下で 3 回に分けて建てる\n(9.3 ドル以下なら即時)', '確度に応じて増やす', '新しい差分を探し、なければ縮小する'],
    ['判別 KPI', 'Q3 EPS 0.15 以上・販促費率 31% 以下・\nall-in 貸倒率 4.2% 以下・\n総自己資本比率 16% 以上', '同左を 2 四半期', 'ROTCE 12% 以上、LPB 比率の上昇', 'PEG 1.0 以上、コンセンサスとの差'],
    ['撤退条件', '—', 'all-in 貸倒率 4.8% 超、増資、再表示', 'ROTCE が 2 四半期続けて 9% 未満', '差分の消失'],
  ], { x: 0.5, y: 2.55, w: 12.33, colW: [1.45, 2.72, 2.72, 2.72, 2.72], fontSize: 9.5, rowH: 0.66, align: ['left', 'left', 'left', 'left', 'left'] });

  // 下: 判別の規則
  L.takeaway(s, 0.5, 5.95, 12.33, 0.7, '判別 KPI のうち 3 つ以上を 2 四半期続けて満たしたら、構造評価を B に見直し、分割エントリーの上限を引き上げる');
};
