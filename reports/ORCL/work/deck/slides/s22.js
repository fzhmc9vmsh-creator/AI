// 条件6(評価 B)。本文は構造図ではなく表。右パネルは L.t15Side
// 箇条書きの続きの行: 記号を出さず(空白の記号)、字下げだけ先頭行にそろえる
const CONT = { bullet: { characterCode: '00A0', indent: 12 } };
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: '事業実態 EPS の5年成長率は3経路とも 30% を超え PEG は 0.60〜0.66 だが、エンジン経路の余裕は 1.5pt で自社株買いに依存する', kicker: '条件6 5年後 EPS 成長率で PEG<1(EPS CAGR 30% 以上)。事業実態 EPS = 非GAAP EPS − 株式報酬の税引後', source: 'コンセンサス(Yahoo・FactSet・tickflow)、会社の FY30 目標(FAM 2025-10)、需給エンジン第4.3版(calc/out/m8_extra.json)。株価 143.20 ドル', page: 22, grade: 'B', condNo: 6 });
  L.table(s, [
    ['経路', 'FY27', 'FY32', '5年 CAGR', 'PER', 'PEG'],
    ['コンセンサス', '6.85', '29.48', '33.9%', '20.9', '0.62'],
    ['会社(FY30 目標 21 ドル)', '6.89', '30.20', '34.4%', '20.8', '0.60'],
    ['需給エンジン', '6.89', '27.14', '31.5%', '20.8', '0.66'],
  ], { x: 0.5, y: 1.75, w: 8.3, colW: [2.1, 1.25, 1.25, 1.2, 1.2, 1.3], fontSize: 11, rowH: 0.42 });
  L.bullets(s, [
    'エンジン経路の余裕は 1.5pt。超過 FCF の自社株買いがなければ 30.0%、確率加重の経路では 28.6%',
    '条件7 が C(安い理由の一部は実在のリスク)のため、規則により S は無効',
    'FY27→FY30 の3年では全経路が 36% 超。減速は FY30〜32 の容量追加の減速による',
  ], { x: 0.5, y: 3.7, w: 8.3, h: 1.0, fontSize: 10.5 });
  // fix_r1 s22: 左下の空白を縦棒チャート(5年 CAGR)で埋める。閾値 30% は線を引かず、チャート上の注記にする
  s.addChart(pres.charts.BAR, [{ name: '5 年 CAGR', labels: ['コンセンサス', '会社(FY30 目標)', '需給エンジン', '確率加重の経路'], values: [33.9, 34.4, 31.5, 28.6] }],
    L.chartStyle({ x: 0.5, y: 4.75, w: 8.3, h: 1.95, barDir: 'col', chartColors: [L.C.primary], dataLabelFormatCode: '0.0"%"', valAxisMinVal: 0, valAxisMaxVal: 40, objectName: 'chart_cagr' }));
  L.text(s, '閾値 30%', { x: 6.9, y: 5.1, w: 1.9, h: 0.28, fontSize: 9, color: L.C.amber, align: 'right', objectName: 'ovl_thr' });
  L.t15Side(s, {
    evidence: [[{ text: '5年 CAGR の閾値 30%: FY32 の事業実態 EPS', options: { breakLine: true, paraSpaceAfter: 0 } }, { text: '25.6 ドル以上', options: CONT }],'PER は 143.20 ÷ FY27 の事業実態 EPS', '第1版の評価は C(エンジン 22.1%)'],
    reason: '数値は S の基準を満たすが、余裕が薄く条件7 と対で評価して B',
  });
};
