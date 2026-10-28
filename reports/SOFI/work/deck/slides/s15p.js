// フェーズの診断。型: 対象ごとのフェーズ表と takeaway(手本: 表の判定セル、takeaway の位置)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: 'フェーズの目安: ① 立ち上げ / ② 急成長(収益 +40% 超、赤字〜損益分岐) / ③ スケール(収益 +20〜40%、黒字、販促・開発が収益の 20% 超) / ④ 成熟への移行(+10〜20%) / ⑤ 成熟',
    source: '会社開示(Q3 2026)、research_r5/Q3_datasheet.md、calc/A4_q3_memo.md の §1 フェーズ、銘柄分析メソッド growth-stage-evaluation §1',
  });

  // フェーズのセル: ③ は A の色(緑)、②→③ は B の色(薄緑)、回復期はアンバー(L.GRADE の色)
  const ph = (k, st) => ({ text: k, options: { fill: { color: st.fill }, color: st.font, bold: true, align: 'center' } });
  const name = (t) => ({ text: t, options: { bold: true } });
  L.table(s, [
    ['対象', '数字(Q3 2026、前年比)', 'フェーズ', '経営の重心', '次の段階に移る条件と時期'],
    [name('会社全体'),
      '収益 +44%・会員 +36%・製品 +44%、黒字、販促費 32%・技術 14%、\nEBITDA 率 34%',
      ph('③ スケール(上端、加速)', L.GRADE.A), '獲得 + クロスセル',
      '収益 +20% 未満・販促費率 28% 以下:\nエンジンで 2028 年(収益 +18%)'],
    [name('Lending(貸出)'),
      '収益 8.21 億ドル(+66%)、貢献利益率 55%',
      ph('③ スケール', L.GRADE.A), '保有して NII を積む',
      '自給率 1 以上:\nエンジンで 2028 年(1.04)'],
    [name('Financial Services'),
      '収益 5.25 億ドル(+25%)、NII +38%・非金利 +13%、\n交換手数料 +77%、貢献利益率 46 → 50%',
      ph('② → ③(底打ち)', L.GRADE.B), '投資(Plus・暗号資産・販促)',
      '貢献利益率 50% 超の定着'],
    [name('Technology Platform'),
      '収益 0.87 億ドル(前年比 −24%、大口を除き +18%)、\n貢献利益率 16%',
      ph('回復期 → 再成長', L.GRADE.C), '自社の預金基盤を移行、\n新規 13 社(Q2)',
      '前年比のプラス転換(Q1 2027)'],
  ], {
    x: 0.5, y: 1.62, w: 12.33, colW: [1.7, 4.2, 1.6, 2.0, 2.83], fontSize: 9.5, rowH: [0.5, 0.85, 0.85, 0.85, 0.85],
    align: ['left', 'left', 'center', 'left', 'left'],
  });

  // 下: takeaway
  L.takeaway(s, 0.5, 5.9, 12.33, 0.75, 'フェーズ ③ の ROTCE 約 10%(推定)は、販促費 32% と成長のための資本の使い方の結果。\n水準ではなく傾き(EBITDA +70%、純利益 +73%)で読み、将来の構造と実現確率で補う(次ページ)');
};
