// 競合優位と産業構造。指示書 spec/ch2b.md の s11 節どおり。左: 競合比較の表、右: ファイブフォース(十字配置)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    title: '優位の源泉は価格ではなく DB と資金・敷地の確保にある。電力の確保に 3〜4 年かかる構造が参入を遅らせ、利益の上限は NVIDIA と買い手の集中が決める',
    kicker: '左: 競合に対する価格・品質・差を生む活動(米国のオンデマンド定価)。右: ファイブフォース(各力の強さと Oracle の利益率への効き)',
    source: 'report/r3_sections_5w1h_f20.md §3-4(F20)、research3/W3_industry_structure.md、research2/R3_competition.md、ClusterMAX v3.0(2026-09)',
    page: 11,
  });

  // ---- 左: 競合比較 ----
  L.paneHead(s, 0.5, 1.62, 6.05, '競合比較: 品質 × 価格 × 価値連鎖', 'pane_l');
  L.table(s, [
    ['製品', '価格(対競合)', '品質', '差を生む活動'],
    ['AI 容量(H100)', '10 ドル/時。AWS の 1.45 倍・CoreWeave の 1.62 倍', 'ClusterMAX は Gold(最上位は CoreWeave・Nebius)', '資金と DC・電力の確保'],
    ['汎用計算', '月額で AWS・Azure より 45% 安い', 'SLA 99.99% で同水準', 'ハード外の仮想化'],
    ['外向き通信', '月 50TB で AWS の 12.6 分の 1', '比較なし', 'ネットワーク設計'],
    ['DB ライセンス', '同じコアで必要なライセンスが半分', 'DB 本体は同一', 'ライセンス規則'],
    ['Database@', 'OCI と同一価格。他社の契約枠に算入可', '移設不要で低遅延', '他社クラウド内への配置'],
  ], {
    x: 0.5, y: 2.0, w: 6.05, colW: [1.25, 1.75, 1.55, 1.5], fontSize: 9, rowH: 0.6,
    align: ['left', 'left', 'left', 'left'], name: 'tbl_compete',
  });
  L.takeaway(s, 0.5, 5.75, 6.05, 0.95, '安いのは汎用計算・通信・DB ライセンス。GPU は高く品質も最上位ではない。優位は価格ではなく DB と資金・敷地の確保');

  // ---- 右: ファイブフォース ----
  L.paneHead(s, 6.78, 1.62, 6.05, 'ファイブフォース(業界構造)', 'pane_r');
  const BW = 1.9, BH = 1.45;
  const STR = { 弱: C.primary, 中: C.amber, 強: C.red };
  const forces = [
    { id: 'entry', x: 8.855, y: 2.0, name: '新規参入', str: '弱', fact: 'ガスタービン納期 約 3 年、系統連系 約 40 か月、変圧器 128〜160 週' },
    { id: 'supp', x: 6.78, y: 3.55, name: '供給者', str: '強', fact: 'NVIDIA が AI 計算の約 8 割(近似)。メモリ価格の上昇が capex を押し上げ' },
    { id: 'rival', x: 8.855, y: 3.55, name: '業界内の競争', str: '中', fact: 'H100 実勢: 大手 7.19 ドル・ネオクラウド 2.80 ドル。1 年契約は +38%' },
    { id: 'buyer', x: 10.93, y: 3.55, name: '買い手', str: '強', fact: 'OpenAI が受注残の約 45%。計算契約は売上見通しの約 32 倍' },
    { id: 'subst', x: 8.855, y: 5.1, name: '代替', str: '中', fact: 'Google TPU(Anthropic 2027 年から約 3.5GW)、AWS 自社チップ 年換算 250 億ドル超' },
  ];
  forces.forEach(f => {
    L.box(s, f.x, f.y, BW, BH, { round: true, name: 'ovl_force_' + f.id });
    L.text(s, f.name, { x: f.x + 0.08, y: f.y + 0.07, w: 1.3, h: 0.28, fontSize: 10, bold: true, color: C.dark, margin: 0, valign: 'middle', objectName: 'force_n_' + f.id });
    L.text(s, f.str, { x: f.x + 1.38, y: f.y + 0.07, w: 0.44, h: 0.28, fontSize: 10, bold: true, color: STR[f.str], align: 'right', margin: 0, valign: 'middle', objectName: 'force_s_' + f.id });
    L.text(s, f.fact, { x: f.x + 0.08, y: f.y + 0.4, w: BW - 0.16, h: BH - 0.47, fontSize: 8.5, color: C.text, margin: 0, objectName: 'force_f_' + f.id });
  });

  // 中央の箱から上下左右の箱へ細い矢印(灰)
  const cx = 8.855 + BW / 2, cy = 3.55 + BH / 2;
  L.arrow(s, cx, 3.55, cx, 3.55 - 0.1, { color: C.sub, width: 1 });                    // 上: 新規参入
  L.arrow(s, cx, 3.55 + BH, cx, 3.55 + BH + 0.1, { color: C.sub, width: 1 });          // 下: 代替
  L.arrow(s, 8.855, cy, 8.855 - 0.175, cy, { color: C.sub, width: 1 });                // 左: 供給者
  L.arrow(s, 8.855 + BW, cy, 8.855 + BW + 0.175, cy, { color: C.sub, width: 1 });      // 右: 買い手

  L.text(s, '強さは Oracle の利益率への圧力。弱 = 参入が遅く Oracle に有利', { x: 10.93, y: 5.1, w: BW, h: BH, fontSize: 8.5, color: C.sub, objectName: 'force_legend' });
  return s;
};
