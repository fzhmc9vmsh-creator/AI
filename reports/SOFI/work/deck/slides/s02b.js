// Q3 決算の要点(指示書 spec/v4.md の s02b 節。新規。手本: slides/s02.js の kpiTiles + slides/s15b.js の表)
// 上段 4 枚の数値タイル(kpiTiles と同じ位置・箱。値だけ 28pt にして「13.85 億ドル」を 1 行に収める)
// 下段は左に ガイダンスの表、右に 何が起きたかの表、最下段に結論の帯
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: 'Q3 2026(2026-09-30 締め、10/27 発表)の実績とガイダンス。前年比は Q3 2025 比',
    source: 'research_r5/Q3_datasheet.md(Q3 の 8-K・説明会の要約)、calc/out/growth_v4.json',
  });

  // 上段: 数値タイル 4 枚(kpiTiles と同じ箱・配置。値の大きさだけ 28pt)
  const tiles = [
    { value: '13.85 億ドル', label: '総純収益', note: '前年比 +44%(Q2 +42.5%)' },
    { value: '0.18 ドル', label: 'EPS', note: 'コンセンサス 0.17、前年比 +67%' },
    { value: '120 万人', label: '会員純増', note: '過去最高、会員 1,710 万' },
    { value: '17.0%', label: '総自己資本比率', note: '前期比 −1.8pt、下限 14%' },
  ];
  const ty = 1.62, th = 1.45, gap = 0.25, tw = (L.W - 2 * L.M - gap * 3) / 4;
  tiles.forEach((t, i) => {
    const tx = L.M + i * (tw + gap);
    L.box(s, tx, ty, tw, th, { fill: C.tint, line: C.tint, name: 'ovl_tile' + i });
    L.text(s, t.value, { x: tx + 0.1, y: ty + 0.08, w: tw - 0.2, h: 0.78, fontSize: 28, bold: true, color: C.primary, align: 'center', valign: 'middle', margin: 0, objectName: 'tile_v' + i });
    L.text(s, t.label, { x: tx + 0.1, y: ty + 0.88, w: tw - 0.2, h: 0.3, fontSize: 10.5, bold: true, color: C.dark, align: 'center', margin: 0, objectName: 'tile_l' + i });
    L.text(s, t.note, { x: tx + 0.1, y: ty + 1.17, w: tw - 0.2, h: 0.33, fontSize: 8.5, color: C.sub, align: 'center', margin: 0, objectName: 'tile_n' + i });
  });

  // 左下: ガイダンスの表(7/29 時点 → 10/27 時点)。二段の欄は改行を明示
  L.table(s, [
    ['ガイダンス', '7/29 時点', '10/27 時点'],
    ['2026 年 調整後純収益', '47.5〜48.5 億', '50.4 億'],
    ['2026 年 EPS', '約 0.60', '約 0.61'],
    ['2027 年 調整後純収益', '—', '64 億(+27%)'],
    ['2027 年 EBITDA', '—', '22.4 億(率 35%)'],
    ['2027 年 EPS', '—\n(決算前コンセンサス 0.82)', '0.90\n(2026 年比 +48%)'],
    ['Q4 2026(通期からの含意、推定)', '—', '収益 前期比 +1%\nEPS 約 0.19'],
  ], {
    x: 0.5, y: 3.25, w: 6.05, colW: [2.35, 1.95, 1.75], fontSize: 10, rowH: [0.36, 0.36, 0.36, 0.36, 0.36, 0.46, 0.46],
    align: ['left', 'center', 'center'],
  });

  // 右下: 何が起きたか
  L.table(s, [
    ['何が起きたか', '数字'],
    ['増収の源泉は NII', 'NII +1.41 億ドル(前期比)、運用資産 +15%、NIM +16bp'],
    ['販促費は増やした', '3.92 → 4.44 億ドル(+13%)、収益比 32% で横ばい'],
    ['手数料型は 42% へ', '5.71 億ドル(+40%)、交換手数料 +77%'],
    ['信用は改善', '純償却 2.26%、all-in 約 3.4%'],
    ['資本を使った', '総自己資本 18.8 → 17.0%、RWA +15%'],
    ['Tech Platform', '大口を除き +18%、貢献利益率 16%'],
  ], {
    x: 6.78, y: 3.25, w: 6.05, colW: [2.2, 3.85], fontSize: 10, rowH: 0.389,
    align: ['left', 'left'],
  });

  // 下端: 結論の帯
  L.takeaway(s, 0.5, 6.1, 12.33, 0.66, '上振れは増収(NII)で作られ、販促費は削っていない。代わりに自己資本を 1 四半期で 1.8pt 使った。\n2027 年見通し(EPS 0.90)の達成は、資本の弁(LPB)と手数料が伸びを担えるかにかかる');
  return s;
};
