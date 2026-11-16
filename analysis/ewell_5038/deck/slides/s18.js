// 投資行動: 上にエントリー圏の帯(比例尺)と現在値・52週レンジの印、下に日付ごとの判別表
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, {
    kicker: '上: 株価の水準ごとの行動(即時・分割・見送り)。下: 日付ごとに見る数字と、続行・見直しの線',
    source: 'valuation.json、hypotheses.json(撤回の線・予測)',
  });
  const z1 = parseFloat(F.n('val.entry.Z1')), z2 = parseFloat(F.n('val.entry.Z2'));
  const lo = 1000, hi = 3000, x0 = 0.7, x1 = 12.6, px = (v) => x0 + (v - lo) / (hi - lo) * (x1 - x0);
  const n1 = (k) => parseFloat(F.n(k)).toLocaleString('en-US', { minimumFractionDigits: 1 });
  const by = 2.45, bh = 0.6;
  const zones = [
    { a: lo, b: z1, fill: C.primary, color: C.white, t: `即時 ≤ ${n1('val.entry.Z1')}円` },
    { a: z1, b: z2, fill: C.light, color: C.dark, t: `分割 ${n1('val.entry.Z1')}〜\n${n1('val.entry.Z2')}円` },
    { a: z2, b: hi, fill: C.rule, color: C.text, t: `見送り > ${n1('val.entry.Z2')}円` },
  ];
  zones.forEach((z, i) => {
    s.addShape('rect', { x: px(z.a), y: by, w: px(z.b) - px(z.a), h: bh, fill: { color: z.fill }, line: { color: C.white, width: 1 }, objectName: 'ovl_zone' + i });
    const tx0 = i === 2 ? px(2380) : px(z.a), tx1 = i === 2 ? px(2900) : px(z.b);
    L.text(s, z.t, { x: tx0, y: by, w: tx1 - tx0, h: bh, fontSize: 9, bold: true, color: z.color, align: 'center', valign: 'middle', margin: 0, objectName: 'ovl_zone_t' + i });
  });
  L.text(s, '株価(円)', { x: 0.5, y: 1.66, w: 1.2, h: 0.22, fontSize: 9, bold: true, color: C.dark, margin: 0, objectName: 'ovl_band_head' });
  const pins = [
    { v: 1695, t: '52 週安値 1,695円', al: 'center', c: C.sub },
    { v: 2297, t: `現在値 ${F('price.last')}`, al: 'center', c: C.red, bold: true },
    { v: 2940, t: '52 週高値 2,940円', al: 'right', c: C.sub },
  ];
  pins.forEach((p, i) => {
    const x = px(p.v), w = 1.7;
    s.addShape('line', { x, y: 2.1, w: 0.001, h: by + bh + 0.12 - 2.1, line: { color: p.c, width: p.bold ? 2 : 1.25 }, objectName: 'ovl_pin' + i });
    const tx = p.al === 'right' ? x - w + 0.05 : x - w / 2;
    L.text(s, p.t, { x: tx, y: 1.86, w, h: 0.22, fontSize: 9.5, bold: !!p.bold, color: p.c, align: p.al, margin: 0, objectName: 'ovl_pin_t' + i });
  });
  [1000, 1500, 2000, 2500, 3000].forEach(v => L.text(s, v.toLocaleString('en-US'), { x: px(v) - 0.3, y: by + bh + 0.12, w: 0.6, h: 0.2, fontSize: 8, color: C.sub, align: 'center', margin: 0, objectName: 'ovl_tk' + v }));
  L.takeaway(s, 0.5, 3.38, 12.33, 0.46,
    `${n1('val.entry.Z2')}円で買えば PER 17.2 倍でも年率 ${F('calc.irr_entry')}`, // lint-ok: PER は台帳に無い
    { fontSize: 11 });
  const rows = [
    ['日付', '見る数字', '続行の線', '見直しの線', '予測(確率)'],
    ['2027-02-12 頃', '2026 年の新規獲得', '680 件以下', '720 件以上(680〜720 は保留)', '700 件以下 80%'],
    ['同', '2026 年の売上・営業利益', '売上 < 4,277・営業利益 ≥ 1,900', '—', '80%・75%'],
    ['2027-05-14 頃', '1Q の顧客単価・MRR チャーン', '単価 約 99 千円・チャーン ≤ 0.20%', '単価 ≥ 101 千円かつチャーン ≤ 0.20%(値上げの定着)\nチャーン > 0.25%(分割圏でも買わない)', 'チャーン ≤ 0.20% 65%'],
    ['同', '1Q のクラウド粗利率', '79.5% 未満', '79.5% 以上', '50%'],
    ['2027-07 頃', '業界の新規開設', '約 2,450 件で横ばい', '2,700 件超(永続成長 4% で置き直し、DCF 約 2,680 円)', '—'],
  ];
  L.table(s, rows, { x: 0.5, y: 4.0, w: 12.33, colW: [1.45, 2.3, 2.75, 3.9, 1.93], fontSize: 9, rowH: 0.44, align: ['left', 'left', 'left', 'left', 'center'], name: 'tbl_trig' });
};
