// 付録: 外部資料の検証(指示書 spec/r9_external.md の G の s39b。台帳は r9 A・B、数字の出所は一次資料)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '左: 外部資料の主張と一次資料の照合(A の 11 行)。右: 外部資料の前提を本資料の枠に入れたときの理論株価',
    source: '外部資料 ORCL_deck_2026-10-29.pdf(56 枚)、Oracle 10-Q Q1 FY27(SEC)、Investor Day 2026-10-28 の CFO 資料と書き起こし、CNBC・S&P Global MI(CDS)、需給エンジン第4.5版(calc/m10_gemini.py)',
    page: 0,
  });

  // 判定の色(誤り・誇張・古い = 赤、正しい = 緑)
  const bad = (t) => ({ text: t, options: { color: C.red, bold: true, align: 'center' } });
  const good = (t) => ({ text: t, options: { color: C.primary, bold: true, align: 'center' } });
  const rows = [
    ['#', '外部資料の主張', '一次資料・本資料', '判定', '向き'],
    ['1', '10/28 の後、CDS は約 115bp に縮小し、信用不安は遮断', 'CDS 5 年は 10/28 約 277bp(10/15 288bp)。115bp の出所はない', bad('誤り'), '楽観'],
    ['2', '4 年超の GPU の全量が +20% で更新', 'CFO: 4 年前の GPU の実例 1 件(+20%)。\n全量ではない', bad('誇張'), '楽観'],
    ['3', '1GW の capex 370 億ドルに建屋・受変電を含む', 'CFO 資料: capex はチップ・メモリ・ネットワーク。土地・建屋は買わない', bad('誤り'), '—'],
    ['4', '株主資本コスト 9.20%(無リスク金利 4.20%)', '10 年金利は 5.02%(10/29、古い金利)。本資料は 10.63%(β 1.33)', bad('誤り'), '楽観'],
    ['5', '前受収益 224.8 億ドル(前期比 +42%)', '10-Q: 前受収益の合計\n307.9 億ドル(5 月末から +154 億)', bad('誤り'), '—'],
    ['6', 'Q1 の営業 CF 231 億、capex 285 億、FCF −54 億ドル', '10-Q: 23,103 / 28,499 / −5,396 百万ドル', good('正しい'), '—'],
    ['7', 'GPU の償却は 6 年', '10-Q: サーバー・網機器は 6 年。\n4 年なら EPS 基準で −18.5 ドル', good('正しい'), '—'],
    ['8', '定常価値 154.8 ドル > 株価(成長がマイナスに評価)', '定常オーナー利益 ÷ 9.2% は、残りの capex と純負債 890 億を引いていない', bad('誤り'), '楽観'],
    ['9', 'S&P の格下げ条件は純負債/EBITDA 4.0 倍超の滞留', 'S&P: 調整後レバレッジ 4.5 倍超が続く、FY29 までに FOCF が黒字化しない', bad('誤り'), '楽観'],
    ['10', 'コンセンサスの FY30 売上\n1,850 億ドル', 'LSEG は 2,242 億ドル(説明会の前)', bad('誤り'), '—'],
    ['14', '基準株価 144.54 ドル(10/28 終値)', '10/29 終値は 139.56 ドル。古い基準で割安度を小さく見せる', bad('古い'), '悲観'],
  ];
  L.table(s, rows, {
    x: 0.5, y: 1.62, w: 7.75, colW: [0.45, 2.45, 3.4, 0.7, 0.75], fontSize: 9, rowH: [0.3].concat(Array(11).fill(0.42)),
    align: ['center', 'left', 'left', 'center', 'center'], name: 'tbl_claims',
  });

  // 右上: 外部資料の前提を入れたときの理論株価(横棒。株価 139.56 の赤の点線。棒は下から並ぶので配列を逆順に渡す)
  L.paneHead(s, 8.5, 1.62, 4.33, '外部資料の前提を入れたときの理論株価(ドル)');
  const box = { x: 8.5, y: 1.95, w: 4.33, h: 2.85 };
  const lay = { x: 0.37, y: 0.1, w: 0.58, h: 0.8 };
  const MAX = 300;
  s.addChart(pres.charts.BAR, [
    { name: '理論株価(ドル)', labels: ['外部資料の結論', '3 つ同時', 'PEG 1.196', '株主資本コスト 9.20%', '外部資料の EPS', '本資料(第4.5版)'],
      values: [244.7, 222.0, 259.1, 251.9, 207.5, 245.2] },
  ], L.chartStyle(Object.assign({}, box, {
    objectName: 'chart', barDir: 'bar', chartColors: [C.primary], layout: lay,
    dataLabelFormatCode: '0.0', valAxisMinVal: 0, valAxisMaxVal: MAX, valAxisMajorUnit: 100, barGapWidthPct: 45,
  })));
  // 株価 139.56 ドルの線(プロット領域の座標で描く)
  const px = box.x + lay.x * box.w, py = box.y + lay.y * box.h, pw = lay.w * box.w, ph = lay.h * box.h;
  const xP = px + (139.56 / MAX) * pw;
  s.addShape('line', { x: xP, y: py - 0.04, w: 0.001, h: ph + 0.04, line: { color: C.red, width: 1.5, dashType: 'dash' }, objectName: 'ovl_price_line' });
  L.text(s, '株価 139.56', { x: xP - 0.6, y: py - 0.27, w: 1.2, h: 0.2, fontSize: 9, bold: true, color: C.red, align: 'center', valign: 'middle', margin: 0, objectName: 'ovl_price_t' });

  // 右下: 読み取り(3 行)
  L.bullets(s, [
    '外部資料の 244.7 は、悲観の EPS(−38)と楽観の資本コスト・PEG(+20)と成熟 PER 20.1 倍が打ち消し合った値',
    '外部資料の悲観の EPS(本資料の分布の 25 パーセンタイル)でも 207.5 ドルで、株価を 49% 上回る',
    '取り込んだもの: Q1 の現金の実績(10-Q)、\n償却 6 年の確認と 4 年短縮のリスク(−18.5)、撤退の売る量',
  ], { x: 8.5, y: 5.0, w: 4.33, h: 1.7, fontSize: 10, name: 'points', gap: 6 });
};
