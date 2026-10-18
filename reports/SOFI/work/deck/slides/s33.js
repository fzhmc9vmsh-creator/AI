// 年度別理論株価(指示書 spec/ch1_ch4.md の s33 節)。上段の flow 5 列 + 下段の表 + bullets
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    kicker: '年度別理論株価 = Σ 重み × [ 妥当 PER × 翌年度の事業実態 EPS × 生存確率 98.5% を株主資本コスト 13.9% で今日へ割引 ]',
    source: 'calc/val_model.py・out/val.json・out/growth_v2.json、銘柄分析メソッド valuation-model §3-3(構造評価 B の出発 PEG 1.0〜1.3)',
  });
  L.flow(s, [
    { head: '構造評価', boxes: [{ text: 'B', tone: 'key', size: 28, bold: true, h: 0.8 }, { text: '出発 PEG 1.0〜1.3', tone: 'in', h: 0.55 }] },
    { head: '許容 PEG', boxes: [{ text: '1.0〜1.15', tone: 'on', size: 24, bold: true, h: 0.8 }, { text: '年度で下げる\n(2026 末 1.15 → 2029 末 1.00)', tone: 'in', h: 0.55, size: 9 }] },
    { head: '妥当 PER(3 経路の平均)', boxes: [{ text: 'a 同業 13.6 倍 /\nb PEG × 3 年成長率 /\nc 事業エンジンの価値', tone: 'in', h: 1.4 }] },
    { head: '年度末の目標', boxes: [{ text: 'PER × 翌年度 EPS ×\n生存確率', tone: 'in', h: 1.4 }] },
    { head: '理論株価', boxes: [{ text: '14.9 ドル', tone: 'key', size: 26, bold: true, h: 0.8 }, { text: '期待値 14.7・株価 14.55', tone: 'in', h: 0.55 }] },
  ], { y: 1.62, h: 1.6, gap: 0.3 });
  // 構造評価の箱だけ B の色(L.GRADE.B = 薄緑の地に濃緑の字)。flow の tone に B の色が無いので、描いた箱と字の色を差し替える
  const gBox = s._slideObjects.find(o => o.options && o.options.objectName === 'ovl_fbox0_0');
  const gTxt = s._slideObjects.find(o => o.options && o.options.objectName === 'flow_t0_0');
  gBox.options.fill.color = L.GRADE.B.fill;
  gBox.options.line.color = L.GRADE.B.fill;
  gTxt.options.color = L.GRADE.B.font;
  gTxt.text.forEach(r => { r.options.color = L.GRADE.B.font; });
  L.table(s, [
    ['年度末', '翌年度 EPS', '3年成長率', 'a 同業 13.6 倍', 'b PEG × 成長', 'c エンジン', '目標(平均)', '今日の価値(重み)'],
    ['2026 末', '0.84', '25.2%', '11.5', '24.5', '10.8', '15.6', '14.9(40%)'],
    ['2027 末', '1.10', '21.6%', '15.0', '26.2', '12.3', '17.9', '15.0(30%)'],
    ['2028 末', '1.35', '19.8%', '18.4', '28.0', '14.0', '20.1', '14.9(20%)'],
    ['2029 末', '1.66', '16.8%', '22.5', '27.8', '16.0', '22.1', '14.4(10%)'],
    ['ベース', '', '', '', '', '', '', { text: '14.9', options: { bold: true } }],
  ], { x: 0.5, y: 3.6, w: 12.33, colW: [1.5, 1.6, 1.4, 1.5, 1.5, 1.5, 1.6, 1.73], fontSize: 10, rowH: 0.34 });
  L.text(s, '注: a・b・c の列は「倍率 × 翌年度 EPS」の価格(ドル)。', {
    x: 0.5, y: 5.72, w: 12.33, h: 0.24, fontSize: 8.5, color: L.C.sub, margin: 0, objectName: 'note',
  });
  L.bullets(s, [
    'b の PEG は 2026 末 1.15・2027 末 1.10・2028 末 1.05・2029 末 1.00(構造 B)。下限は無成長の PER(1/資本コスト = 7.2 倍)',
    'c は事業エンジン(必要資本を引いた株主への配分可能額の DCF)の年度末の価値',
    '株主資本コスト 13.9% = 米 10 年債 5.2% + β 1.93 × 4.5%(β は SOFI 2.2 と同業 NU・HOOD の中央 1.65 の平均)',
    '構造評価が C なら(第1版)ベース 13.3 ドル',
  ], { x: 0.5, y: 6.0, w: 12.33, h: 0.8, fontSize: 9.5 });
};
