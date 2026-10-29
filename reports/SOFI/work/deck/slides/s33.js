// 年度別理論株価(指示書 spec/v4.md の s33 節)。上段の flow 5 列 + 下段の表 + bullets
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '年度別理論株価 = Σ 重み × [ 許容 PEG × 当該年度から 3 年の成長率 × 当該年度の EPS を資本コスト 13.9% で今日へ割引 ]',
    source: 'calc/growth_v4.py・out/growth_v4.json(rows・values・values_peg10)、銘柄分析メソッド valuation-model §3-3・§3-4',
  });
  L.flow(s, [
    { head: '構造評価', boxes: [{ text: 'B', tone: 'key', size: 28, bold: true, h: 0.8 }, { text: '平均点 3.42・位置 0.92', tone: 'in', h: 0.55 }] },
    { head: '許容 PEG', boxes: [{ text: '1.275 → 1.125', tone: 'on', size: 20, bold: true, h: 0.8 }, { text: '年度で −0.05', tone: 'in', h: 0.55, size: 9 }] },
    { head: '妥当 PER', boxes: [{ text: 'PEG × 3 年の成長率\n(他の方法と平均しない)', tone: 'in', h: 1.4 }] },
    { head: '年度の適正株価', boxes: [{ text: '妥当 PER × 当該年度の EPS', tone: 'in', h: 1.4 }] },
    { head: '理論株価', boxes: [{ text: '23.8 ドル', tone: 'key', size: 26, bold: true, h: 0.8 }, { text: '期待値 24.2\n株価 14.55〜16.5', tone: 'in', h: 0.55 }] },
  ], { y: 1.62, h: 1.6, gap: 0.3 });
  // 構造評価の箱だけ B の色(L.GRADE.B = 薄緑の地に濃緑の字)。flow の tone に B の色が無いので、描いた箱と字の色を差し替える
  const gBox = s._slideObjects.find(o => o.options && o.options.objectName === 'ovl_fbox0_0');
  const gTxt = s._slideObjects.find(o => o.options && o.options.objectName === 'flow_t0_0');
  gBox.options.fill.color = L.GRADE.B.fill;
  gBox.options.line.color = L.GRADE.B.fill;
  gTxt.options.color = L.GRADE.B.font;
  gTxt.text.forEach(r => { r.options.color = L.GRADE.B.font; });
  const bo = t => ({ text: t, options: { bold: true } });
  L.table(s, [
    ['年度', 'EPS', '3 年の成長率', '許容 PEG', '妥当 PER', '適正株価', '今日の価値(重み)'],
    ['2026', '0.61', '32.5%', '1.275', '41.4', '25.3', '25.0(40%)'],
    ['2027', '0.90', '25.0%', '1.225', '30.6', '27.5', '23.8(30%)'],
    ['2028', '1.15', '22.2%', '1.175', '26.1', '30.1', '22.9(20%)'],
    ['2029', '1.42', '20.1%', '1.125', '22.7', '32.2', '21.5(10%)'],
    [bo('理論株価'), bo(''), bo(''), bo(''), bo(''), bo(''), bo('23.8')],
  ], { x: 0.5, y: 3.6, w: 12.33, colW: [1.5, 1.5, 1.7, 1.6, 1.6, 1.7, 2.73], fontSize: 10, rowH: 0.34 });
  L.text(s, '3 経路: エンジン 23.8・会社の中期目標 22.9・見通し + コンセンサスの伸び 21.4(コンセンサスの伸びの 2029 年は成熟年度の理論式)。PEG 1.0 固定ならそれぞれ 19.5・18.7・17.4', {
    x: 0.5, y: 5.72, w: 12.33, h: 0.24, fontSize: 8.5, color: L.C.sub, margin: 0, objectName: 'note',
  });
  L.bullets(s, [
    '2026・2027 年は会社の見通し(EPS 0.61・0.90)にエンジンを較正。2028 年以降はエンジン(資本の上限・LPB・手数料)',
    '中期目標(2025→28 年 EPS 年 38〜42%)の上端 1.12 に対し、エンジンは 1.15',
    '資本コスト 13.9% = 米 10 年債 5.2% + β 1.93 × 4.5%。信用・資本・希薄化は EPS 経路・確率・株数で数え、倍率では割り引かない',
  ], { x: 0.5, y: 6.0, w: 12.33, h: 0.8, fontSize: 9.5 });
};
