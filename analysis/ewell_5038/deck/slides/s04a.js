// 会社と事業の概要: 利用の流れの関係図 + 製品表 + KPI の札 + 沿革の 1 行
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, { kicker: '', source: '事業計画及び成長可能性に関する事項(2026-03-30)p.3・p.20・p.21、2026年12月期3Q決算説明資料' });

  L.paneHead(s, 0.5, 1.62, 7.6, '利用の流れ(①〜⑥の順。緑の枠 = 当社の製品)', 'pane_flow');
  L.flowMap(s, {
    name: 's04a', x: 0.5, y: 1.9, w: 7.6, h: 3.4, cols: [1.5, 1.5, 1.5, 1.5], rows: 3, nodeH: 0.8, legend: false,
    nodes: [
      { id: 'n1', c: 0, r: 0, kind: 'ext', label: '① 訪問', sub: '看護師が利用者の\n自宅を訪問' },
      { id: 'n2', c: 1, r: 0, kind: 'self', label: '② 記録', sub: 'スマホ・タブレットで\n看護記録・写真' },
      { id: 'n3', c: 2, r: 0, kind: 'unit', label: '③ 計画書・報告書', sub: 'AIが下書きを作成' },
      { id: 'n4', c: 3, r: 0, kind: 'ext', label: '④ 報告', sub: '主治医・ケアマネへ' },
      { id: 'n5', c: 1, r: 1, kind: 'unit', label: '⑤ 請求書の作成', sub: '記録から自動で作成\n(iBowレセプト)' },
      { id: 'n6', c: 2, r: 1, kind: 'ext', label: '⑥ 請求', sub: '保険者(国保連など)へ' },
      { id: 'bp', c: 1, r: 2, cs: 2, kind: 'unit', label: '事務代行(BPaaS)', sub: '当社の事務スタッフが請求事務を代行' },
      { id: 'bd', c: 3, r: 2, kind: 'unit', label: 'ボード', sub: '経営指標を自動で表示' },
    ],
    edges: [
      { from: 'n1', to: 'n2', kind: 'goods' },
      { from: 'n2', to: 'n3', kind: 'goods' },
      { from: 'n3', to: 'n4', kind: 'goods' },
      { from: 'n2', to: 'n5', kind: 'goods' },
      { from: 'n5', to: 'n6', kind: 'money' },
      { from: 'n5', to: 'bp', kind: 'ctrl' },
    ],
  });

  L.paneHead(s, 8.35, 1.62, 4.48, '製品と料金', 'pane_prod');
  L.table(s, [
    ['製品', '何をするか', '料金', '利用数'],
    ['iBow', '訪問看護の電子カルテ', '基本料18,000円/月+100円/訪問', '3,695'],
    ['iBowレセプト', '保険請求書の作成', '月6,000〜99,000円', '3,212'],
    ['AI計画・報告、AIルート', '計画書の下書き、訪問ルートの自動作成', '20円・30円/訪問', '1,755・281'],
    ['事務代行(BPaaS)', '請求事務の代行', '報酬の5%か月10万円', '325'],
    ['法定研修 e-Campus', '職員研修のeラーニング', '年18万円', '—'],
    ['ボードPro', '経営の改善策を提示', '2027年1月〜月3万円', '無償期間'],
  ], { x: 8.35, y: 1.94, w: 4.48, colW: [1.0, 1.4, 1.25, 0.83], fontSize: 8, rowH: 0.6, name: 'tbl_prod' }); // lint-ok: 台帳に無い手書き(製品・料金・利用数)

  L.kpiTiles(s, [
    { value: F('q26q3.stations'), label: '契約(2026年3Q)' },
    { value: F('share.q26q3'), label: '訪問看護ステーションのシェア' },
    { value: '131名', label: '従業員' }, // lint-ok: 台帳に無い手書き(会社資料p.3)
    { value: F('fy25.opm'), label: '営業利益率(2025年12月期)' },
  ], { x: 0.5, y: 5.4, w: 12.33, h: 0.95, compact: true });

  L.text(s, '2012年6月設立(大阪)、2014年6月 iBow提供開始、2022年9月 東証グロース上場。創業者の中野社長が39.0%を保有。直販のみ', { x: 0.5, y: 6.42, w: 12.33, h: 0.3, fontSize: 10.5, color: C.text, margin: 0, valign: 'middle', objectName: 'note_hist' }); // lint-ok: 台帳に無い手書き(沿革)
};
