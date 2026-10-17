// 条件12(評価 A)
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: 'OCI は従量・確約、保守・SaaS は継続課金で、受注残 6,640 億ドルが積み上がるストック型の収益である', kicker: '条件12 従量課金型の収益性格(ORCL IaaS 型)であり売り切り・供給過多型(VRT 型)でない', source: '会社開示(10-Q、RPO の期間別)、research4/T1_consensus.csv、research3/W5_oracle_ai_economics.md', page: 28, grade: 'A', condNo: 12 });
  s.addChart(pres.charts.BAR, [
    { name: '12か月以内 860 億', labels: ['RPO'], values: [86] },
    { name: '13〜36か月 2,460 億', labels: ['RPO'], values: [246] },
    { name: '37〜60か月 2,260 億', labels: ['RPO'], values: [226] },
    { name: '60か月超 1,060 億', labels: ['RPO'], values: [106] },
  ], L.chartStyle({ x: 0.5, y: 1.75, w: 8.3, h: 2.2, barDir: 'bar', barGrouping: 'stacked', chartColors: [L.C.dark, L.C.primary, L.C.light, L.C.teal], showValue: false, dataLabelPosition: 'ctr', dataLabelColor: L.C.white, showLegend: true, legendPos: 'b', showValAxisTitle: true, valAxisTitle: '単位: 10 億ドル', valAxisTitleFontSize: 9, valAxisTitleColor: L.C.sub, objectName: 'chart' }));
  L.bullets(s, [
    '36 か月以内の 3,320 億ドルが、コンセンサス売上(FY28 1,315 億、FY29 1,820 億ドル)の大半を裏付ける',
    '前払い・持ち込み 750 億ドル分は陳腐化リスクを顧客に移している',
    'take-or-pay・解約条項・価格改定条項は公開情報で確認できない',
  ], { x: 0.5, y: 4.15, w: 8.3, h: 2.0 });
  L.t15Side(s, {
    evidence: ['RPO 6,640 億ドル(前年比 +2,090 億)', '36 か月以内 50%(前期 46%)', 'OCI は従量・確約、保守・SaaS は継続課金'],
    reason: '継続課金と長期の確約が積み上がるストック型。解約条件が見えないため S でなく A',
  });
};
