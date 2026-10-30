// 2-5 需給(2/2): 学習から推論へ。左: 経営者の発言と意味(台帳 r8 H)。右上: 推論の比率(業界、二次)。右下: 推論の効きを理論株価と DCF で(台帳 r8 E)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 経営者の発言(日付つき)と、それが Oracle の何に効くか。右上: AI 計算に占める推論の比率。右下: 推論の効きを理論株価と DCF で(需給エンジン第4.5版)',
    source: 'Investor Day 2026-10-28 の書き起こし(research_v6)、Benzinga・Cloud Wars(Ellison 2025-09)、Deloitte TMT Predictions 2026(二次)、需給エンジン第4.5版(calc/out/m10_sens.json)',
  });

  // ---------- 左: 経営者の発言(列: 発言者・日付 / 発言 / 意味)----------
  L.paneHead(s, 0.5, 1.62, 7.4, '経営者の発言と、Oracle への意味');
  const who = (t, d) => ({ text: t + '\n' + d, options: { bold: false } });
  L.table(s, [
    ['発言者・日付', '発言', '意味'],
    [who('Magouyrk(共同 CEO)', '2026-10-28'), '「GW 級の拠点は学習に向く。推論が大きくなるにつれ、50〜200MW の拠点を世界中に届けている。遅延の理由で分散が要る」「AI 顧客は 1,000 社超」', '拠点が小さく分散し、データの近くへ'],
    [who('Maxson(CFO)', '2026-10-28'), '「再契約は今と同じか、より良い利益率を見込む。4 年前の GPU を元の契約単価の +20% で売却・更新した」', '価値の芯(再契約の単価)を会社は下がらないと見る'],
    [who('Ellison(会長・CTO)', '2025-09(二次)'), '「推論の市場は学習の市場よりはるかに大きい」「次は公開データの学習から私的データの推論へ」', '私的データの推論は DB の顧客基盤が効く'],
    [who('Leone(アプリ)', '2026-10-28'), '「Fusion の AI の呼び出しは Q1 に 1.5 億回、6→8 月に +42%」「AI Units(使用量の課金)」', 'アプリが AI の使用量\nで課金'],
    [who('Sicilia(共同 CEO)', '2026-10-28'), '「ERP の顧客の約半分がまだオンプレ」', 'ERP の移行が OCI と SaaS を押し上げる'],
  ], { x: 0.5, y: 2.0, w: 7.4, colW: [1.7, 3.9, 1.8], fontSize: 9, rowH: 0.62, align: ['left', 'left', 'left'] });

  // ---------- 右上: 推論の比率(AI 計算に占める)----------
  L.paneHead(s, 8.2, 1.62, 4.63, '推論の比率(AI 計算に占める、業界の推計)');
  s.addChart(pres.charts.BAR, [
    { name: '推論の比率', labels: ['2023', '2025', '2026'], values: [33, 50, 67] },
  ], L.chartStyle({
    x: 8.2, y: 1.95, w: 4.63, h: 1.9, objectName: 'chart_infer', barDir: 'col', chartColors: [C.primary], barGapWidthPct: 70,
    dataLabelFormatCode: '0"%"', dataLabelFontBold: true, valAxisHidden: true, valGridLine: { style: 'none' },
    valAxisMinVal: 0, valAxisMaxVal: 80, catAxisLabelFontSize: 10,
  }));
  L.text(s, '出所: Deloitte TMT Predictions 2026(二次)。推論は 2026 年に AI 計算の約 2/3', { x: 8.2, y: 3.87, w: 4.63, h: 0.22, fontSize: 8, color: C.sub, margin: 0, objectName: 'note_infer' });

  // ---------- 右下: 推論の効き(理論株価 / DCF)----------
  L.paneHead(s, 8.2, 4.17, 4.63, '推論の効き(理論株価 / DCF、ドル)');
  L.table(s, [
    ['前提', '理論株価 / DCF'],
    ['推論とデータの重力(ベースに入れた分)', '+7.5 / +17.0'],
    ['さらに強く(再契約 75%・長期超過 +5pt)', '+9.4 / +25.3'],
    ['経営者の発言どおり(再契約 100%)', '+47.7 / +100.4'],
  ], { x: 8.2, y: 4.52, w: 4.63, colW: [3.13, 1.5], fontSize: 9, rowH: 0.36, align: ['left', 'center'] });

  // ---------- 下: テイクアウェイ ----------
  L.takeaway(s, 0.5, 6.12, 12.33, 0.62, '推論は企業データの近くで動くため、Oracle は DB・OCI・アプリと一緒に売れる。\n契約後の単価が下がりにくくなり、価値の芯を押し上げる');
  return s;
};
