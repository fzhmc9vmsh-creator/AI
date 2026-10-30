// 条件6(評価 B)。本文は構造図ではなく表。右パネルは L.t15Side
// 箇条書きの続きの行: 記号を出さず(空白の記号)、字下げだけ先頭行にそろえる
const CONT = { bullet: { characterCode: '00A0', indent: 12 } };
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: '事業実態 EPS の 5 年成長率は 29.1〜31.0%、PEG は 0.65〜0.70。閾値 30% の前後で余裕はなく、エンジンの経路だけが 30% を下回る', kicker: '条件6 5年後 EPS 成長率で PEG<1(EPS CAGR 30% 以上)。事業実態 EPS = 非GAAP EPS − 株式報酬の税引後', source: 'コンセンサス(Yahoo・FactSet・tickflow)、会社の FY30 目標(Investor Day 2026-10-28)、需給エンジン第4.5版(calc/out/m10_*.json)。株価 139.56 ドル(2026-10-29 終値)', page: 22, grade: 'B', condNo: 6 });
  L.table(s, [
    ['経路', '5 年 CAGR', 'PEG', '閾値 30% との差'],
    ['会社(FY30 目標 21 ドル)', '31.0%', '0.65', '+1.0pt'],
    ['コンセンサス(説明会の前)', '30.3%', '0.67', '+0.3pt'],
    ['需給エンジン', '29.1%', '0.70', '−0.9pt'],
  ], { x: 0.5, y: 1.75, w: 8.3, colW: [3.1, 1.7, 1.5, 2.0], fontSize: 11, rowH: 0.42 });
  L.bullets(s, [
    'エンジン経路は 29.1% で閾値を 0.9pt 下回る。会社とコンセンサスの経路は 30% を超える',
    '条件7 が B のため条件6 の S は無効にしないが、数値が閾値の前後のため B',
    'FY30 の EPS が 3 経路の差になる(会社 21 ドル・コンセンサス 20.53 ドル・エンジン 19.59 ドル)',
  ], { x: 0.5, y: 3.7, w: 8.3, h: 1.0, fontSize: 10.5 });
  // fix_r1 s22: 左下の空白を縦棒チャート(5年 CAGR)で埋める。閾値 30% は線を引かず、チャート上の注記にする
  s.addChart(pres.charts.BAR, [{ name: '5 年 CAGR', labels: ['会社(FY30 目標)', 'コンセンサス', '需給エンジン'], values: [31.0, 30.3, 29.1] }],
    L.chartStyle({ x: 0.5, y: 4.75, w: 8.3, h: 1.95, barDir: 'col', chartColors: [L.C.primary], dataLabelFormatCode: '0.0"%"', valAxisMinVal: 0, valAxisMaxVal: 40, objectName: 'chart_cagr' }));
  L.text(s, '閾値 30%', { x: 6.9, y: 5.1, w: 1.9, h: 0.28, fontSize: 9, color: L.C.amber, align: 'right', objectName: 'ovl_thr' });
  L.t15Side(s, {
    evidence: ['3 経路の CAGR は会社 31.0%・コンセンサス 30.3%・エンジン 29.1%。\n閾値 30% の前後で、PEG は 0.65〜0.70', [{ text: '5年 CAGR の閾値 30%: FY32 の事業実態 EPS', options: { breakLine: true, paraSpaceAfter: 0 } }, { text: '25.6 ドル以上', options: CONT }],'PER は 139.56 ÷ FY27 の事業実態 EPS(20.2 倍)', '第1版の評価は C(エンジン 22.1%)'],
    reason: '数値は S の基準を満たすが、閾値の前後で余裕が薄いため B',
  });
};
