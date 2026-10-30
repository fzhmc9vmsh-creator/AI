// 条件6(評価 B)。本文は構造図ではなく表。右パネルは L.t15Side
// 箇条書きの続きの行: 記号を出さず(空白の記号)、字下げだけ先頭行にそろえる
const CONT = { bullet: { characterCode: '00A0', indent: 12 } };
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: '事業実態 EPS の 5 年成長率は 28.7〜30.3%、PEG は 0.67〜0.71。閾値 30% の前後で余裕はなく、30% を超えるのは会社の経路だけ', kicker: '条件6 5年後 EPS 成長率で PEG<1(EPS CAGR 30% 以上)。事業実態 EPS = 非GAAP EPS − 株式報酬の税引後', source: 'コンセンサス(Yahoo・FactSet・tickflow)、会社の FY30 目標(Investor Day 2026-10-28)、需給エンジン第4.4版(calc/out/m9_extra.json)。株価 139.56 ドル(2026-10-29 終値)', page: 22, grade: 'B', condNo: 6 });
  L.table(s, [
    ['経路', '5 年 CAGR', 'PEG', '閾値 30% との差'],
    ['会社(FY30 目標 21 ドル)', '30.3%', '0.67', '+0.3pt'],
    ['コンセンサス(説明会の前)', '29.5%', '0.68', '−0.5pt'],
    ['需給エンジン', '28.7%', '0.71', '−1.3pt'],
  ], { x: 0.5, y: 1.75, w: 8.3, colW: [3.1, 1.7, 1.5, 2.0], fontSize: 11, rowH: 0.42 });
  L.bullets(s, [
    'エンジン経路は 28.7% で閾値を 1.3pt 下回る。会社の経路だけが 30% を超える',
    '条件7 が C(安い理由の一部は実在のリスク)のため、規則により S は無効',
    'FY27→FY30 の3年では全経路が 36% 超。減速は FY30〜32 の容量追加の減速による',
  ], { x: 0.5, y: 3.7, w: 8.3, h: 1.0, fontSize: 10.5 });
  // fix_r1 s22: 左下の空白を縦棒チャート(5年 CAGR)で埋める。閾値 30% は線を引かず、チャート上の注記にする
  s.addChart(pres.charts.BAR, [{ name: '5 年 CAGR', labels: ['会社(FY30 目標)', 'コンセンサス', '需給エンジン'], values: [30.3, 29.5, 28.7] }],
    L.chartStyle({ x: 0.5, y: 4.75, w: 8.3, h: 1.95, barDir: 'col', chartColors: [L.C.primary], dataLabelFormatCode: '0.0"%"', valAxisMinVal: 0, valAxisMaxVal: 40, objectName: 'chart_cagr' }));
  L.text(s, '閾値 30%', { x: 6.9, y: 5.1, w: 1.9, h: 0.28, fontSize: 9, color: L.C.amber, align: 'right', objectName: 'ovl_thr' });
  L.t15Side(s, {
    evidence: ['3 経路の CAGR は会社 30.3%・コンセンサス 29.5%・エンジン 28.7%。\n閾値 30% の前後で、PEG は 0.67〜0.71', [{ text: '5年 CAGR の閾値 30%: FY32 の事業実態 EPS', options: { breakLine: true, paraSpaceAfter: 0 } }, { text: '25.6 ドル以上', options: CONT }],'PER は 139.56 ÷ FY27 の事業実態 EPS(20.2 倍)', '第1版の評価は C(エンジン 22.1%)'],
    reason: '数値は S の基準を満たすが、余裕が薄く条件7 と対で評価して B',
  });
};
