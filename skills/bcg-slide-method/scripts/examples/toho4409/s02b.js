// s02b セグメントと製品群
module.exports = function build(pres, L) {
  const { F, C } = L;
  const s = L.contentSlide(pres, {
    source: '2026年3月期 決算短信(セグメント別の状況・セグメント情報)、2027年3月期第2四半期 決算短信、中期経営計画 TOHO Step Up Plan 2027 p.14・p.16、決算説明資料 p.14。電材の売上は本分析の推定',
  });

  // 4列の箱(x0.5 から、各 w2.95、間隔 0.17、y1.98〜4.40)。
  // 各箱: 上に見出しの帯(h0.36、塗り C.dark、白字 11pt。スペシャリティーケミカルだけ C.primary)
  // その下に数字2行(8.8pt): `売上 ${F.n('fy26.seg_X_sales')}・利益 ${F.n('fy26.seg_X_profit')}(26/3期、百万円)`、`利益率 a%→b%(26/3期→27/3期上期)`(a = seg_X_profit/seg_X_sales、b = fy27h1 の同じ比。小数1桁)、
  // その下に製品群の箇条書き(L.bullets 8.8pt)。X は surf / resin / chem / spec。

  const segs = [
    {
      id: 'surf',
      name: '界面活性剤',
      isPrimary: false,
      gap: 4.5,
      items: [
        '香粧原料(一般洗浄剤・ヘアケア用基剤)◆',
        'プラスチック用添加剤(帯電防止剤)★',
        '土木建築用薬剤(コンクリート用)',
        '紙パルプ用薬剤(サイズ剤・消泡剤・脱墨剤)',
        '農薬助剤',
        '繊維助剤',
      ],
    },
    {
      id: 'resin',
      name: '樹脂',
      isPrimary: false,
      gap: 9,
      items: [
        '石油樹脂(道路舗装関連)',
        '合成樹脂(トナーインキ用・土木関連)',
        '樹脂エマルション(塗料用・金属表面処理)★',
        'アクリレート',
      ],
    },
    {
      id: 'chem',
      name: '化成品',
      isPrimary: false,
      gap: 14,
      items: [
        'ロジン系乳化重合剤(合成ゴム・ABS樹脂用)',
        '石油添加剤',
        '金属加工油剤(切削油剤・洗浄剤)',
      ],
    },
    {
      id: 'spec',
      name: 'スペシャリティーケミカル',
      isPrimary: true,
      gap: 8,
      items: [
        '溶剤(医薬品用・ブレーキ液基剤)',
        '電子情報産業用の微細加工用樹脂\n(半導体のレジスト)★',
      ],
      note: `電材の売上は ${F('em.sales_now')}、\n全社の${F('em.share_now')}。SCの売上の大半は溶剤`,
    },
  ];

  const boxW = 2.95;
  const gap = 0.17;
  const topY = 1.98;
  const boxH = 2.42;

  segs.forEach((seg, i) => {
    const x = 0.5 + i * (boxW + gap);
    const fillColor = seg.isPrimary ? C.primary : C.dark;

    // 外枠
    L.box(s, x, topY, boxW, boxH, { fill: C.white, line: C.rule, name: `ovl_seg_box_${seg.id}` });

    // 見出し帯
    s.addShape('rect', {
      x,
      y: topY,
      w: boxW,
      h: 0.36,
      fill: { color: fillColor },
      line: { color: fillColor },
      objectName: `ovl_seg_hdr_${seg.id}`,
    });

    L.text(s, seg.name, {
      x,
      y: topY,
      w: boxW,
      h: 0.36,
      fontSize: 11,
      bold: true,
      color: C.white,
      align: 'center',
      valign: 'middle',
      margin: 0,
      objectName: `seg_name_${seg.id}`,
    });

    // 数字行
    const a = (F.v(`fy26h1.seg_${seg.id}_profit`) / F.v(`fy26h1.seg_${seg.id}_sales`) * 100).toFixed(1);
    const b = (F.v(`fy27h1.seg_${seg.id}_profit`) / F.v(`fy27h1.seg_${seg.id}_sales`) * 100).toFixed(1);
    const line1 = `売上 ${F.n(`fy26.seg_${seg.id}_sales`)}・利益 ${F.n(`fy26.seg_${seg.id}_profit`)}(26/3期、百万円)`;
    const line2 = `上期の利益率 ${a}%→${b}%(前年同期→今期)`;

    L.text(s, `${line1}\n${line2}`, {
      x: x + 0.1,
      y: topY + 0.40,
      w: boxW - 0.2,
      h: 0.54,
      fontSize: 8.8,
      color: C.text,
      lineSpacingMultiple: 1.18,
      margin: 0,
      objectName: `seg_nums_${seg.id}`,
    });

    // 区切り線
    s.addShape('line', {
      x: x + 0.1,
      y: topY + 0.98,
      w: boxW - 0.2,
      h: 0,
      line: { color: C.rule, width: 0.5 },
      objectName: `ovl_seg_rule_${seg.id}`,
    });

    // 製品群箇条書き
    L.bullets(s, seg.items, {
      x: x + 0.1,
      y: topY + 1.04,
      w: boxW - 0.2,
      h: seg.note ? 0.65 : 1.34,
      fontSize: 8.8,
      gap: seg.gap || 4,
      name: `seg_bullets_${seg.id}`,
    });

    // SC の注記
    if (seg.note) {
      L.text(s, seg.note, {
        x: x + 0.1,
        y: topY + 1.74,
        w: boxW - 0.2,
        h: 0.64,
        fontSize: 8.5,
        color: C.sub,
        margin: 0,
        objectName: `seg_note_${seg.id}`,
      });
    }
  });

  // 箱の下 y4.60〜6.65:
  // 左 x0.5 w7.6 に addChart BAR 横棒の100%積み上げ(barDir 'bar'、barGrouping 'percentStacked'、dataLabelPosition 'ctr'、ラベル '0%')
  const totSales = F.v('fy26.seg_surf_sales') + F.v('fy26.seg_resin_sales') + F.v('fy26.seg_chem_sales') + F.v('fy26.seg_spec_sales');
  const totProf26 = F.v('fy26.seg_surf_profit') + F.v('fy26.seg_resin_profit') + F.v('fy26.seg_chem_profit') + F.v('fy26.seg_spec_profit');
  const totProf27h1 = F.v('fy27h1.seg_surf_profit') + F.v('fy27h1.seg_resin_profit') + F.v('fy27h1.seg_chem_profit') + F.v('fy27h1.seg_spec_profit');

  const chartData = [
    {
      name: '界面活性剤',
      labels: ['売上 26/3期', '利益 26/3期', '利益 27/3期上期'],
      values: [
        F.v('fy26.seg_surf_sales') / totSales,
        F.v('fy26.seg_surf_profit') / totProf26,
        F.v('fy27h1.seg_surf_profit') / totProf27h1,
      ],
    },
    {
      name: '樹脂',
      labels: ['売上 26/3期', '利益 26/3期', '利益 27/3期上期'],
      values: [
        F.v('fy26.seg_resin_sales') / totSales,
        F.v('fy26.seg_resin_profit') / totProf26,
        F.v('fy27h1.seg_resin_profit') / totProf27h1,
      ],
    },
    {
      name: '化成品',
      labels: ['売上 26/3期', '利益 26/3期', '利益 27/3期上期'],
      values: [
        F.v('fy26.seg_chem_sales') / totSales,
        F.v('fy26.seg_chem_profit') / totProf26,
        F.v('fy27h1.seg_chem_profit') / totProf27h1,
      ],
    },
    {
      name: 'SC',
      labels: ['売上 26/3期', '利益 26/3期', '利益 27/3期上期'],
      values: [
        F.v('fy26.seg_spec_sales') / totSales,
        F.v('fy26.seg_spec_profit') / totProf26,
        F.v('fy27h1.seg_spec_profit') / totProf27h1,
      ],
    },
  ];

  s.addChart(
    pres.charts.BAR,
    chartData,
    L.chartStyle({
      x: 0.5,
      y: 4.60,
      w: 7.6,
      h: 1.95,
      barDir: 'bar',
      barGrouping: 'percentStacked',
      dataLabelPosition: 'ctr',
      showValue: true,
      dataLabelFormatCode: '0%',
      valAxisLabelFormatCode: '0%',
      valAxisMinVal: 0,
      valAxisMaxVal: 1,
      showLegend: true,
      legendPos: 'b',
      chartColors: [C.sub, C.gray, C.rule, C.primary],
    })
  );

  // 右 x8.3 w4.53: L.paneHead('読み方') + L.bullets(9pt)
  L.paneHead(s, 8.3, 4.60, 4.53, '読み方');

  L.bullets(
    s,
    [
      '★の3テーマは、4つのセグメントにまたがっている。\n会社はセグメントではなく製品の単位で資源を寄せている',
      `中計はSCで全社の営業利益の5割を目指す(28/3期)。\n上期のSCの利益は ${F('fy27h1.seg_spec_profit')}(前年同期 ${F('fy26h1.seg_spec_profit')})`, // lint-ok: 5割
      '次ページで、15の製品群が上期にどう動いたかを見る',
    ],
    {
      x: 8.3,
      y: 5.02,
      w: 4.53,
      h: 1.62,
      fontSize: 9.5,
      gap: 6,
      name: 'reading_bullets',
    }
  );
};
