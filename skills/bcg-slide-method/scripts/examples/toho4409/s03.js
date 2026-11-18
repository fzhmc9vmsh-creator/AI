// s03 利益の増減(会社自身の分解)
module.exports = function build(pres, L) {
  const { F, C } = L;
  const s = L.contentSlide(pres, {
    source: '2027年3月期第2四半期 決算説明資料 p.7(営業利益の増減分析)・p.4、決算短信 p.2。\n同業は各社の2027年3月期第2四半期決算短信。2022〜24年の営業利益率は各年3月期の有価証券報告書',
  });

  // ======================= 左: ウォーターフォール =======================
  L.paneHead(s, 0.5, 1.62, 7.7, '上期営業利益の増減(百万円、2026年3月期上期→2027年3月期上期、会社の分析)', 'pane_wf_head');

  // データ定義
  const wfItems = [
    { label: '前年上期', val: F.v('fy26h1.op'), type: 'total', disp: Math.round(F.v('fy26h1.op')).toLocaleString('en-US') },
    { label: '販売価格及び\n販売構成', val: F.v('pb.price_mix'), type: 'step', disp: `+${Math.round(F.v('pb.price_mix')).toLocaleString('en-US')}` },
    { label: '販売数量', val: F.v('pb.volume'), type: 'step', disp: `+${Math.round(F.v('pb.volume')).toLocaleString('en-US')}`, highlight: true },
    { label: '原料費', val: F.v('pb.raw'), type: 'step', disp: `▲${Math.round(Math.abs(F.v('pb.raw'))).toLocaleString('en-US')}` },
    { label: 'その他売上原価\n(用役費等)', val: F.v('pb.other'), type: 'step', disp: `▲${Math.round(Math.abs(F.v('pb.other'))).toLocaleString('en-US')}` },
    { label: '販管費', val: F.v('pb.sga'), type: 'step', disp: `▲${Math.round(Math.abs(F.v('pb.sga'))).toLocaleString('en-US')}` },
    { label: '今期上期', val: F.v('fy27h1.op'), type: 'total', disp: Math.round(F.v('fy27h1.op')).toLocaleString('en-US') },
  ];

  L.waterfall(s, wfItems, { x: 0.55, y: 2.22, w: 7.60, h: 3.09, name: 'wf', valueFontSize: 8.5 });

  // 棒の下の bullets
  L.bullets(s, [
    `価格と構成の改善 +${F.n('pb.price_mix')} は、原料高 ${F.n('pb.raw')} の${Math.round(-F.v('pb.price_mix') / F.v('pb.raw') * 100)}%を取り返した。原料高の後に利益率を落とした2022〜24年(営業利益率 ${F('toho.opm_fy22')}→${(F.v('fy24.op') / F.v('fy24.revenue') * 100).toFixed(2)}%)と逆の結果`,
    `その上に数量 +${F.n('pb.volume')} が乗った。会社が数量増を挙げた品目は帯電防止剤・ヘアケア基剤・石油添加剤・樹脂エマルション・電子材料で、いずれも中計の「高機能・高付加価値製品」`,
  ], { x: 0.5, y: 5.48, w: 7.7, h: 1.24, fontSize: 9.2, gap: 4, name: 'wf_bullets' });

  // ======================= 右: 同業比較 + 四半期推移 =======================
  L.paneHead(s, 8.45, 1.62, 4.38, '同業も同じ動きか(中間期の営業利益率)', 'pane_peer_head');

  const peerRows = [
    ['', '前年上期', '今期上期'],
    ['東邦化学', F('toho.opm_h1_26'), { text: F('fy27h1.opm'), options: { bold: true } }],
    ['第一工業製薬', F('peer.dks.opm_h1_26'), F('peer.dks.opm_h1_27')],
    ['日油', F('peer.nof.opm_h1_26'), F('peer.nof.opm_h1_27')],
  ];
  L.table(s, peerRows, { x: 8.45, y: 1.98, w: 4.38, colW: [1.7, 1.3, 1.38], fontSize: 9, rowH: 0.28, name: 'tbl_peer' });

  L.text(s, '第一工業製薬も上げたが、日油は下げた。業界一律の追い風ではない。東邦化学は水準が低いぶん、伸びしろが大きい', {
    x: 8.45, y: 3.16, w: 4.38, h: 0.58, fontSize: 9, color: C.text, objectName: 'txt_peer_note',
  });

  L.paneHead(s, 8.45, 3.82, 4.38, '四半期の営業利益(百万円)', 'pane_q_head');

  const qChartData = [
    {
      name: '営業利益',
      labels: ['26/3期 1Q', '26/3期 2Q', '27/3期 1Q', '27/3期 2Q'],
      values: [
        F.v('fy26.q1_op'),
        F.v('fy26h1.op') - F.v('fy26.q1_op'),
        F.v('fy27.q1_op'),
        F.v('fy27.q2_op'),
      ],
    },
  ];

  s.addChart(pres.charts.BAR, qChartData, L.chartStyle({
    x: 8.45, y: 4.18, w: 4.38, h: 2.45,
    valAxisMinVal: 0,
    showValue: true,
    dataLabelPosition: 'outEnd',
    chartColors: [C.sub, C.sub, C.primary, C.primary],
    objectName: 'chart_q_op',
  }));
};
