// フェーズの診断(指示書 spec/v3.md の s15p 節。新規。手本: slides/s15b.js の表と判定セル、takeaway の位置)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: 'フェーズの目安: ① 立ち上げ / ② 急成長(収益 +40% 超、赤字〜損益分岐) / ③ スケール(収益 +20〜40%、黒字、販促・開発が収益の 20% 超) / ④ 成熟への移行(+10〜20%) / ⑤ 成熟',
    source: '会社開示(Q2 2026)、calc/A3_v3_memo.md §1、calc/out/growth_v3.json の phase、銘柄分析メソッド growth-stage-evaluation §1',
  });

  // フェーズのセル: ③ は A の色(緑)、②→③ は B の色(薄緑)、回復期はアンバー(L.GRADE の色)
  const ph = (k, st) => ({ text: k, options: { fill: { color: st.fill }, color: st.font, bold: true, align: 'center' } });
  const name = (t) => ({ text: t, options: { bold: true } });
  L.table(s, [
    ['対象', '数字(Q2 2026、前年比)', 'フェーズ', '経営の重心', '次の段階に移る条件と時期'],
    [name('会社全体'),
      '収益 +40.5%・会員 +35%・製品 +43%、黒字、販促費 32%・技術開発 16%(収益比)、\n税引前利益率 13.1 → 16.8%、増分の税引前利益率 25%',
      ph('③ スケール(上端)', L.GRADE.A), '獲得 + クロスセル',
      '収益の伸び 20% 未満・販促費率 28% 以下:\nエンジンで 2028 年(収益 +19%・販促費 28.5%)'],
    [name('Lending(貸出)'),
      '収益 7.1 億ドル(+59%)、貢献利益率 56%',
      ph('③ スケール', L.GRADE.A), '保有して NII を積む',
      '自己資本の自給率 1 以上:\nエンジンで 2028 年(1.04)'],
    [name('Financial Services'),
      '収益 4.7 億ドル(+29%)。LPB を除くと +38%、その他の手数料 +83%。\n貢献利益率 52 → 46%',
      ph('② → ③', L.GRADE.B), '投資(Plus・暗号資産・販促)',
      '貢献利益率の底打ち'],
    [name('Technology Platform'),
      '収益 0.85 億ドル(前年比 −23%、前期比 +12.5%)、貢献利益率 14%',
      ph('回復期\n(失注 → 底打ち → 信頼獲得)', L.GRADE.C), '自社の預金基盤を移行、新規 13 社',
      '前年比がプラスに戻る Q1 2027'],
  ], {
    x: 0.5, y: 1.62, w: 12.33, colW: [1.7, 4.4, 1.6, 2.2, 2.43], fontSize: 9.5, rowH: 0.5,
    align: ['left', 'left', 'center', 'left', 'left'],
  });

  // 下: takeaway
  L.takeaway(s, 0.5, 5.9, 12.33, 0.75, 'フェーズ ③ の ROTCE 7% は、販促費 32%(維持水準 16% の 2 倍)と余剰資本(比率 18.8%、下限 14%)の結果。\n水準ではなく傾き(増分利益率 25%、税引前利益率 +3.7pt/年)で読み、将来の構造と実現確率で補う(次ページ)');
};
