// c03_step.js 段差と閾値の階段図(手本): 能力増強の段差と市場の伸びを L.stepChart + L.marks + L.kpiTiles + L.lookBox + L.takeaway で描く
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, {
    source: '有価証券報告書・決算説明資料および市場調査より作成(手本用の固定値)',
  });

  L.paneHead(s, 0.5, 1.62, 7.7, '電子材料用樹脂の生産能力の段差と市場の伸び(t)', 'pane_st_head');

  L.stepChart(s, {
    unit: 't',
    points: [
      { label: '24/3', value: 120 },
      { label: '25/3', value: 120 },
      { label: '26/3', value: 120 },
      { label: '27/3', value: 210 },
      { label: '28/3', value: 210 },
      { label: '29/3', value: 210 },
    ],
    events: [
      { i: 3, label: '二期完工 2026年11月(+90t)' },
    ],
    line: {
      label: '市場の伸び(年6.5%で120から)',
      values: [120, 128, 136, 145, 154, 164],
    },
  }, { x: 0.55, y: 2.02, w: 7.60, h: 3.22, name: 'st' });

  L.marks(s, [
    { x: 3.10, y: 2.82, n: 1, text: '能力+75%', side: 'right' },
    { x: 4.55, y: 2.82, n: 2, text: '需要を上回る余力', side: 'right' },
    { x: 2.05, y: 3.74, n: 3, text: '完工前は能力上限', side: 'right' },
  ]);

  L.kpiTiles(s, [
    { value: '120→210t', label: '生産能力の段差(+75%)\n(2026年11月 二期完工)' }, // lint-ok: 手本用の固定値
    { value: '年6.5%', label: '市場成長率の前提\n(29/3時点で需要164t相当)' }, // lint-ok: 手本用の固定値
    { value: '+46t', label: '29/3時点の供給余力\n(能力210t − 市場成長164t)' }, // lint-ok: 手本用の固定値
  ], { compact: true, x: 0.55, y: 5.42, w: 7.60, h: 1.26 });

  L.lookBox(s, [
    { n: 1, text: '2026年11月の二期完工で生産能力が\n120t→210t(+90t・+75%)へ一段上がる' },
    { n: 2, text: '市場(年6.5%増)は29/3で164t相当。\n能力210tを埋めるにはシェア獲得が必要' },
    { n: 3, text: '26/3までは能力120tが上限となり、\n市場の伸び(136t)を取り込めない制約' },
  ], { x: 8.45, y: 2.02, w: 4.38, h: 3.22 });

  L.takeaway(s, 8.45, 5.42, 4.38, 1.26,
    '二期完工で供給制約は解けるが、市場成長だけでは46t余る。\n増設分の販売は既存先での採用拡大とシェア獲得が鍵', // lint-ok: 手本用の固定値
    { fontSize: 10 });
};
