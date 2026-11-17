// s02a 目次(意図つき)
module.exports = function build(pres, L) {
  const { F, C } = L;
  const s = L.contentSlide(pres, {
    source: '本資料の構成',
  });

  const CH = L.MT.CH;

  // 上段 y1.98〜2.95: 6つの横長の矢印型の箱(L.box、各 w1.95、間隔 0.12、x0.5 から)。第2〜7章を順に。
  // 各箱の中に 2行: 1行目 第N章 章の名前(bold、9.5pt、白字、塗り C.dark、第3・5・7章だけ C.primary)、2行目 CH[i].q(8.8pt)。箱の間に小さな ▶。
  const boxW = 1.95;
  const gap = 0.12;
  const topY = 1.98;
  const boxH = 0.95;

  // 箱の中の問いテキスト（自然な改行位置に調整）
  const boxQuestions = [
    '',
    '何を作り、\nどこで稼ぐ会社か',
    '何が変わったか。\n一時の値上げではないか',
    '変化はなぜ続くか。\n次の段差はいつか',
    '5年後の損益・資本・\nROEはどうなるか',
    '誰が実行し、\n誰が引き継ぐか',
    '市場は何を見落とし、\nいくらで、いつ動くか',
  ];

  for (let i = 1; i <= 6; i++) {
    const ch = CH[i];
    const x = 0.5 + (i - 1) * (boxW + gap);
    const isHighlight = [3, 5, 7].includes(ch.no);

    // 外枠
    L.box(s, x, topY, boxW, boxH, { fill: C.white, line: C.rule, name: `ovl_ch_box_${ch.no}` });

    // 1行目の見出し帯 (塗り C.dark、第3・5・7章だけ C.primary)
    s.addShape('rect', {
      x,
      y: topY,
      w: boxW,
      h: 0.32,
      fill: { color: isHighlight ? C.primary : C.dark },
      line: { color: isHighlight ? C.primary : C.dark },
      objectName: `ovl_ch_hdr_${ch.no}`,
    });

    L.text(s, `第${ch.no}章 ${ch.name}`, {
      x,
      y: topY,
      w: boxW,
      h: 0.32,
      fontSize: ch.no === 4 ? 8.5 : 9.3,
      bold: true,
      color: C.white,
      align: 'center',
      valign: 'middle',
      margin: 0,
      objectName: `ch_title_${ch.no}`,
    });

    // 2行目 CH[i].q(8.8pt)
    L.text(s, boxQuestions[i], {
      x: x + 0.05,
      y: topY + 0.34,
      w: boxW - 0.1,
      h: boxH - 0.36,
      fontSize: 8.8,
      color: C.text,
      align: 'center',
      valign: 'middle',
      margin: 0,
      objectName: `ch_q_${ch.no}`,
    });

    // 箱の間に小さな ▶ (audit_deck の最小フォント 8.0pt 以上を満たすため 8.5pt)
    if (i < 6) {
      L.text(s, '▶', {
        x: x + boxW,
        y: topY,
        w: gap,
        h: boxH,
        fontSize: 8.5,
        color: C.sub,
        align: 'center',
        valign: 'middle',
        margin: 0,
        objectName: `ch_arrow_${ch.no}`,
      });
    }
  }

  // ページの列は L.MT.secPages(章番号) の最初と最後から p.a–b を作る。
  function pageRange(chNo) {
    const pages = L.MT.secPages(chNo);
    const from = pages[0].from;
    const to = pages[pages.length - 1].to;
    return from === to ? `p.${from}` : `p.${from}–${to}`;
  }

  // 下段 y3.15〜6.0: L.table(x0.5 w12.33、colW [1.6, 2.6, 4.9, 2.2, 1.03]、fontSize 9、rowH 0.46) 見出し ['章', '問い', 'この資料の答え', '決め手の数字', 'ページ']。6行(第2〜7章)
  const rows = [
    ['章', '問い', 'この資料の答え', '決め手の数字', 'ページ'],
    [
      '2 事業の前提',
      CH[1].q,
      '売上の約7割は汎用品。電材は売上の数%だが、\n会社は3つの長期戦略テーマに資源を寄せる', // lint-ok: 指示書の確定値
      `汎用品の売上比率 ${F('seg.legacy_share')}`,
      pageRange(2),
    ],
    [
      '3 変化は起きている',
      '何が変わったか。\n一時の値上げではないか',
      '倍増の主因は数量。8品目が販売増、\n汎用品は値上げ。下期の予想は原料高を織り込む', // lint-ok: 指示書の確定値
      `数量効果 +${F.n('pb.volume')}`,
      pageRange(3),
    ],
    [
      '4 シナリオと段差',
      CH[3].q,
      '6ピース中4つが作動。中計の利益は汎用品が先に稼ぎ、電材は計画の8割。2026年に段差が重なる', // lint-ok: 指示書の確定値
      `電材の能力 ${F.n('cap.ep1_capacity')}→${F.n('em.capacity_after')}t`,
      pageRange(4),
    ],
    [
      '5 5年後の構造',
      CH[4].q,
      '営業利益は約2倍。ただし資本が積み上がり、ROEは返還しだい', // lint-ok: 指示書の確定値
      `基準のROE ${F('fwd.base.roe31')}`,
      pageRange(5),
    ],
    [
      '6 経営',
      CH[5].q,
      '推進役は見えている。社長80歳の承継が論点', // lint-ok: 指示書の確定値
      '社長 80歳', // lint-ok: 指示書の確定値
      pageRange(6),
    ],
    [
      '7 市場との差分と価値',
      '市場は何を見落とし、\nいくらで、いつ動くか',
      `市場はROE${F.n('calc.implied_roe')}%の永続を織り込む。価値の芯は全社の粗利率`,
      `理論株価 ${Math.round(parseFloat(F.n('val.value.engine'))).toLocaleString('en-US')}円`,
      pageRange(7),
    ],
  ];

  L.table(s, rows, {
    x: 0.5,
    y: 3.12,
    w: 12.33,
    colW: [1.6, 2.6, 4.9, 2.2, 1.03],
    fontSize: 9,
    rowH: 0.41,
    align: ['left', 'left', 'left', 'left', 'center'],
  });

  // 一番下 L.takeaway(0.5, 6.1, 12.333, 0.6): '第2章で事業の形を押さえ、第3〜5章で「変化は本物で、続き、5年後の構造を変える」ことを確かめ、第7章で価格との差を測る'
  L.takeaway(s, 0.5, 6.1, 12.333, 0.6, '第2章で事業の形を押さえ、第3〜5章で「変化は本物で、続き、5年後の構造を変える」ことを確かめ、第7章で価格との差を測る');
};
