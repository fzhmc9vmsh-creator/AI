// 業界の仕組みとお金の流れ: お金の流れの図 + 業界の数字 + 訪問看護とは + 見るところ
module.exports = function build(pres, L) {
  const { C, F } = L;
  const s = L.contentSlide(pres, { kicker: '', source: '会社資料(成長可能性 p.7・p.15・p.20)、全国訪問看護事業協会(2026)、厚労省(介護事業経営概況調査、告示74号)' });

  L.paneHead(s, 0.5, 1.62, 7.6, 'お金の流れ(1訪問あたり。金額は月の目安)', 'pane_flow');
  L.flowMap(s, {
    name: 's04b', x: 0.5, y: 1.9, w: 7.6, h: 3.3, cols: [1.7, 2.1, 1.6], rows: 3, nodeH: 0.8, legend: false,
    nodes: [
      { id: 'pay', c: 0, r: 0, rs: 2, kind: 'ext', label: '保険者と利用者', sub: '保険者\n(国保連・支払基金)\n\n利用者の自己負担\n1〜3割' },
      { id: 'st', c: 1, r: 0, rs: 2, kind: 'ok', label: '訪問看護ステーション', sub: `全国 ${F('ind.stations_2026')}\n月約500訪問(約425万円)\n収支差率 10.3%` }, // lint-ok: 台帳に無い手書き(平均訪問数・収支差率)
      { id: 'staff', c: 2, r: 0, kind: 'ext', label: '看護師などの職員', sub: '費用の大半は給与' },
      { id: 'ew', c: 2, r: 1, kind: 'key', label: 'eWeLL', sub: 'iBowなどの利用料' },
      { id: 'cost', c: 2, r: 2, kind: 'unit', label: 'クラウド基盤・開発', sub: 'と事務の人員に充てる' },
    ],
    edges: [
      { from: 'pay', to: 'st', label: '1訪問 約8,500円', kind: 'money' },
      { from: 'st', to: 'staff', label: '給与', kind: 'money' },
      { from: 'st', to: 'ew', label: '月68,000円\n(売上の1.6%)', kind: 'money' }, // lint-ok: 台帳に無い手書き(月額・利益比)
      { from: 'ew', to: 'cost', kind: 'goods' },
    ],
  });
  L.text(s, '月68,000円は事業所の営業利益(月約43万円)の約16%に当たる', { x: 0.5, y: 5.24, w: 7.6, h: 0.26, fontSize: 9, color: C.sub, margin: 0, objectName: 'note_flow' }); // lint-ok: 台帳に無い手書き(利益比)

  L.lookBox(s, [
    { n: 1, text: '事業所の収入は国が決める公定価格(1訪問約8,500円)' },
    { n: 2, text: '当社の取り分は売上の1.6%だが、事業所の利益の約16%' },
    { n: 3, text: '業界の伸びは鈍化している(稼働数の伸び 10.4% → 8.2% → 6.9%)' },
  ], { x: 0.5, y: 5.55, w: 7.6, h: 1.2 });
  L.marks(s, [{ x: 5.45, y: 2.0, n: 1 }, { x: 6.45, y: 3.2, n: 2 }]);

  L.paneHead(s, 8.35, 1.62, 4.48, '業界の数字', 'pane_ind');
  L.table(s, [
    ['項目', '数字'],
    ['市場規模', '1兆1,733億円(年+12.3%)'],
    ['うち医療・介護', '7,205 + 4,528(億円)'],
    ['稼働事業所(2026-04-01)', F('ind.stations_2026')],
    ['新規開設・廃止(前年度)', `${F('ind.new_2026')}・${F('ind.closed_2026')}`],
    ['稼働数の伸び', '10.4% → 8.2% → 6.9%'],
    ['ICT化率', '約30%(会社推計)'],
  ], { x: 8.35, y: 1.94, w: 4.48, colW: [2.0, 2.48], fontSize: 9, rowH: 0.3, name: 'tbl_ind' }); // lint-ok: 台帳に無い手書き(市場規模・伸び・ICT化率)
  L.marks(s, [{ x: 12.5, y: 3.46, n: 3 }]);

  L.paneHead(s, 8.35, 4.2, 4.48, '訪問看護とは', 'pane_what');
  L.box(s, 8.35, 4.54, 4.48, 2.18, { fill: C.tint, line: C.light, round: true, name: 'ovl_what' });
  L.text(s, '看護師などが自宅を訪問し、医師の指示で点滴・カテーテル管理・服薬・床ずれの処置・看取りなどを行う医療サービス(0歳から高齢者まで)。生活援助の訪問介護とは別。報酬は公定価格で、診療報酬は2年・介護報酬は3年ごとに改定。2026年6月の改定で、高齢者住まい併設の事業所に1日あたりの包括報酬が新設され、記録の電子化が要件になった。', { x: 8.47, y: 4.6, w: 4.24, h: 2.06, fontSize: 10.5, color: C.text, margin: 0, valign: 'middle', objectName: 'what_t' }); // lint-ok: 台帳に無い手書き(制度の説明)
};
