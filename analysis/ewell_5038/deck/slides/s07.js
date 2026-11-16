// s07 顧客単価の分解: 2025年3Q → 2026年3Q の稼働1STあたり月額を製品別に分ける滝グラフ
module.exports = function build(pres, L) {
  const F = L.F;
  const s = L.contentSlide(pres, {
    kicker: '稼働1STあたりの月額(製品別売上 ÷ 平均稼働ST ÷ 3)。伸びの中身を、本体・付帯・事務代行に分ける',
    source: '会社決算説明資料(製品別売上・KPI)、当方の計算(製品別売上÷平均稼働ST÷3)',
  });

  L.paneHead(s, 0.5, 1.62, 7.7, '稼働1STあたりの月額の変化(千円/月、2025年3Q → 2026年3Q)', 'pane_wf_head');
  L.waterfall(s, [
    { label: '2025年3Q', val: F.v('q25q3.arpu'), type: 'total', disp: F.n('q25q3.arpu', { noPeriod: true }) },
    { label: 'iBow本体', val: 0.1, type: 'step', disp: '+0.1' },
    { label: 'iBow\nレセプト', val: 0.6, type: 'step', disp: '+0.6' },
    { label: 'AI\n計画報告・\nルート', val: 2.5, type: 'step', disp: '+2.5', highlight: true },
    { label: 'BPaaS\n事務代行', val: 2.7, type: 'step', disp: '+2.7', highlight: true },
    { label: 'その他・端数', val: 0.1, type: 'step', disp: '+0.1' },
    { label: '2026年3Q', val: F.v('q26q3.arpu'), type: 'total', disp: F.n('q26q3.arpu') },
  ], { x: 0.55, y: 2.1, w: 7.6, h: 3.7, unit: '千円/月', axisMin: 80, name: 'wf' });

  L.marks(s, [
    { x: 1.9, y: 2.95, n: 1, text: '本体は横ばい', side: 'right' },
    { x: 4.35, y: 2.2, n: 2, text: '2つで+5.2', side: 'left' },
    { x: 7.2, y: 3.6, n: 3, text: '小規模STが相殺', side: 'left' },
  ]);

  L.paneHead(s, 8.55, 1.62, 4.28, '区分別の単価(法人単位、2026年6月)', 'pane_tbl_head');
  L.table(s, [
    ['区分', '単価', 'NRR'],
    ['立ち上げ期\n(400訪問未満の単独ST)', F('nrr.seg_start'), '—'],
    ['拡大期\n(複数ST法人)', F('nrr.seg_expand'), '114.7%'],
    ['全体', '—', F('nrr.jun26')],
  ], { x: 8.55, y: 1.98, w: 4.28, colW: [2.2, 1.04, 1.04], fontSize: 9.5, rowH: [0.3, 0.5, 0.5, 0.3], name: 'tbl_seg' });

  L.lookBox(s, [
    { n: 1, text: `本体は ${F.n('calc.ibow_per_st_q25', { noPeriod: true })} → ${F('calc.ibow_per_st_q26')}。約475訪問/月で不変` },
    { n: 2, text: 'AIとBPaaSで+5.2千円。伸び+6.0千円の約9割' },
    { n: 3, text: `既存法人の伸び(NRR ${F('nrr.jun26')})は新規の小規模STで相殺` },
  ], { x: 8.55, y: 3.78, w: 4.28, h: 2.02 });

  L.takeaway(s, 0.5, 5.95, 12.33, 0.8,
    '従量課金が業界の成長を自動で取り込む構造は、ST単位では働いていない。単価の判別KPIはAIとボードProの付帯', { fontSize: 11.5 });
};
