// 2-1 成長分野(指示書 spec/r6_new.md の s08c 節どおり)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 成長分野の比較(注目度の高い順)。右: 1 株価値 × 伸びで見た位置。注目度 = 価値への効きが大きいか、伸びが速く結果がまだ決まっていない分野',
    source: '需給エンジン第4.3版(セグメント価値)、research2/R4_database_at.md、research4/T4_ai_demand.md(Gartner)、会社開示(Q1 FY27)、本資料 2-6',
  });

  // 注目度の星(★★★ は濃緑の太字、★★ はティール、★ は灰)
  const star = (t) => {
    const color = t === '★★★' ? C.primary : (t === '★★' ? C.teal : C.sub);
    return { text: t, options: { color, bold: t === '★★★' } };
  };

  // 左: 成長分野の比較表
  L.table(s, [
    ['分野', '規模(Q1 FY27)', '伸び', '1 株価値への効き', '見るべき KPI', '注目度'],
    ['AI 容量', 'IaaS 区分\n74 億ドルの大半', 'IaaS +121%', '1 株 117 ドル\n(価値の 45%)', '納入 GW/四半期・AI\n粗利率・更新プレミアム', star('★★★')],
    ['Database@', '額は非開示', '+353%(4 期前は +1,529%)', 'FY30 に +5.4 ドル。\nDB 保守 45 ドルの\n流出を防ぐ', '伸びの減速の速さ・顧客数(+180%)', star('★★★')],
    ['AI Database 26ai', '非開示', '非開示', '未計上(オプション)', '顧客数と課金の開示', star('★★')],
    ['ソブリンクラウド', 'UAE 1GW・日本に 80 億ドル超', '市場 +35.6%\n(2026 年)', 'AI 容量・OCI に含む', '国別の受注の開示', star('★★')],
    ['SaaS\n(AI エージェント)', '42 億ドル', '+10%(14% への加速を想定)', 'SaaS 全体で\n1 株 44 ドル', '繰延収益の伸び・\n移行した社数', star('★')],
  ], {
    x: 0.5, y: 1.62, w: 8.2, colW: [1.35, 1.4, 1.35, 1.55, 1.75, 0.8], fontSize: 9, rowH: 0.62,
    align: ['left', 'left', 'left', 'left', 'left', 'center'],
  });
  L.takeaway(s, 0.5, 5.55, 8.2, 0.8, 'AI 容量は価値の大きさで、Database@ は DB の利益を他社クラウドへ広げて守る点で注目度が最も高い。\nAI Database は数字が出るまでオプションとして扱う');

  // 右: 1 株価値 × 伸び の 2 × 2
  L.paneHead(s, 8.95, 1.62, 3.88, '1 株価値 × 伸びで見た位置');
  L.matrix(s, {
    x: 8.95, y: 1.98, w: 3.88, h: 3.3,
    xLabels: ['伸び 穏やか', '伸び 速い'],
    yLabels: ['1 株価値 大', '1 株価値 小'],
    yTitle: '',
    xTitle: '伸びは前年同期比',
    cells: [
      [{ text: 'SaaS\nDB 保守' }, { text: 'AI 容量' }],
      [{ text: '—' }, { text: 'Database@\nソブリン\nAI Database' }],
    ],
    highlight: [[1, 0]],
  });
  L.text(s, '★★★ = 1 株価値への効きが大きいか、伸びが速く結果が未確定の分野。\n★ = 伸びが穏やかで前提の幅が小さい分野。\n右下の 3 つは「次の大きな柱」の候補', {
    x: 8.95, y: 5.55, w: 3.88, h: 1.1, fontSize: 8.5, color: C.sub,
  });
};
