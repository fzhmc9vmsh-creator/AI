// 東邦化学工業(4409) 長期保有適格性審査 v6: 本編25枚・7章(目次は意図つきで1枚。付録なし。設計は deck_design_v6.md)
// タイトル = メッセージライン(2行、各34字以内)。数字は台帳(facts_deck.json)・valuate.py の出力(val.*)・5年後モデル(data/fwd_v3.json)から読む。
const F = require('./facts.js');
const M = require('./data/fwd_v3.json');
const SK = require('./data/sankey_fy31_slide.json');
const R = id => Math.round(parseFloat(F.n(id).replace(/,/g, ''))).toLocaleString('en-US');   // valuate.py の表示値(文字列)を円単位に丸める
const P = id => parseFloat(F.n(id).replace(/[,+]/g, ''));                                      // valuate.py の表示値を数値に
const B31 = M.scenarios['基準'][4];
const INC = B31.op - F.v('fy26.op');                                   // 5年間の営業利益の増分(基準)
const SHARE = (now, then) => Math.round((then - now) / INC * 10);     // 増分に占める割合(割)
const GM31 = (SK.gross.value / SK.total.value * 100).toFixed(1);

const CH = [
  { no: 1, name: '結論', short: '結論', why: '判断と根拠の柱を先に示し、読む順を決める', q: '買うべきか。なぜか', secs: [['1-1', '結論'], ['1-2', '目次']] },
  { no: 2, name: '事業の前提', short: '前提', why: '何を作り、どこで稼ぐ会社かを製品群の単位で押さえる', q: '何を作り、どこで稼ぐ会社か',
    secs: [['2-1', 'セグメントと製品群'], ['2-2', '製品群の地図']] },
  { no: 3, name: '変化は起きている', short: '変化', why: '会社自身の利益の分解と品目の動きで、変化の主因と持続性を確かめる', q: '何が変わったか。一時の値上げではないか',
    secs: [['3-1', '利益の増減'], ['3-2', '製品構成の変化'], ['3-3', '原料高への耐性'], ['3-4', '下期の試金石']] },
  { no: 4, name: '経営陣シナリオと次の段差', short: 'シナリオ', why: 'TOHO Step Up Plan 2027 のピースと、制約が解ける日付を押さえる', q: '変化はなぜ続くか。次の段差はいつか',
    secs: [['4-1', 'シナリオ台帳'], ['4-2', '中計の進捗'], ['4-3', '変曲点'], ['4-4', '電子材料'], ['4-5', '技術の主因'], ['4-6', '工場の作り替え']] },
  { no: 5, name: '5年後の構造', short: '5年後', why: '損益と貸借対照表を5年先まで通し、ROEの経路を見る', q: '5年後の損益・資本・ROEはどうなるか',
    secs: [['5-1', '営業利益の積み上げ'], ['5-2', '損益の流れ'], ['5-3', '貸借対照表'], ['5-4', 'ROEと資本の使い道']] },
  { no: 6, name: '経営', short: '経営', why: '変革を誰が進め、誰が引き継ぐか', q: '誰が実行し、誰が引き継ぐか', secs: [['6-1', '推進役と承継']] },
  { no: 7, name: '市場との差分と価値', short: '価値', why: 'なぜ安いか、価値は何で決まるか、いくらか、いつ何を見て動くか', q: '市場は何を見落とし、いくらで、いつ動くか',
    secs: [['7-1', '市場の織り込み'], ['7-2', '価値の芯'], ['7-3', '13条件'], ['7-4', '価値評価'], ['7-5', '弱気の反論'], ['7-6', '投資行動'], ['7-7', '下振れ']] },
];

const ORDER = ['s01', 's02', 's02a', 's02b', 's02c', 's03', 's04', 's04b', 's04a', 's05', 's05a', 's06', 's07', 's08', 's09',
  's10', 's10b', 's11', 's12', 's13', 's14', 's14b', 's15', 's16', 's17', 's18b', 's18', 's19'];

const META = {
  s01: { ch: 1, kind: 'cover' },
  s02: { ch: 1, sec: '1-1', theme: '結論', why: '最終主張とキーメッセージ5本を1枚で示す',
    title: `変革の成果が上期の過去最高益として出始めたが、市場は無反応\n構造評価${F.n('val.grade.letter')}・理論株価${R('val.value.engine')}円(${F.n('val.gap.engine.last')})で${F.n('val.decision.last')}。株価は${F.n('val.entry.zone.last')}圏` },
  s02a: { ch: 1, sec: '1-2', theme: '目次', why: '6つの問いの順に読むと、結論の根拠がそろう',
    title: `読む順は、事業の前提→変化の事実→続く仕組み→5年後→人→価格\n各章は問いへの答えを先に置き、結論の根拠は後ろの章にそろう` },
  s02b: { ch: 2, sec: '2-1', theme: 'セグメントと製品群', why: '4つのセグメントの中身(製品・用途・稼ぎ)を、会社の説明より平易に示す',
    title: `売上の約7割は汎用の界面活性剤・樹脂・化成品で、SCの大半も溶剤\n電材は売上の数%だが、会社は3つの長期戦略テーマに資源を寄せる` }, // lint-ok: 「約7割」は seg.legacy_share 68.7%、「3つ」はテーマの数
  s02c: { ch: 2, sec: '2-2', theme: '製品群の地図', why: '15の製品群を、上期の動き(数量か値上げか)と会社の位置づけで並べる',
    title: `上期に販売が伸びた8品目は戦略テーマ品が中心、残る7品目は値上げ\n高付加価値品は数量で稼ぎ、汎用品は採算で選んでいる` }, // lint-ok: 品目の数(決算短信の品目別の記述)
  s03: { ch: 3, sec: '3-1', theme: '利益の増減', why: '変化の主因が数量か価格かを、会社自身の分解で確かめる',
    title: `上期の営業利益倍増は、数量増(+${F.n('pb.volume')}百万円)が生んだ\n伸びたのは高付加価値品。原料高は価格と構成の改善で${Math.round(-F.v('pb.price_mix') / F.v('pb.raw') * 10)}割取り返した` },
  s04: { ch: 3, sec: '3-2', theme: '製品構成の変化', why: '変化が一時の価格ではなく、製品構成の移行であることを示す',
    title: `製品単位で高収益品へ移り、セグメント利益率は底から4四半期連続で上昇\n界面活性剤は売上${F.n('surf.rev_chg_fy26')}%でも利益+${F.n('surf.op_chg_fy26')}%。会社も構成の変化と明記` }, // lint-ok: 「4四半期」は期間の数
  s04b: { ch: 3, sec: '3-3', theme: '原料高への耐性', why: '値上げが一時のものか、値決めの体質が変わったのかを、過去13期の原料高と比べて確かめる',
    title: `粗利率は13期ナフサと逆に動いた(相関${F.n('hist.gm_nap_corr')})。今期は初めて崩れなかった\n2022年3月期はナフサ+81%で粗利率${F.n('hist.gm_chg_fy22')}pt、今期は+${F.n('hist.nap_h1_chg')}%でも+${F.n('hist.gm_chg_h1fy27')}pt` }, // lint-ok: 「13期」は期間の数、「+81%」は hist.naphtha の前年比
  s04a: { ch: 3, sec: '3-4', theme: '下期の試金石', why: '会社予想の前提を分解し、変化が続くかを測る最初の日付を示す',
    title: `会社予想は下期の粗利率を${F.n('calc.h2_gm_gap')}pt下げる。4〜6月の原料高を織り込む\n前年下期並みでも通期の営業利益は${F.n('calc.fy27_op_gm_fy26h2')}百万円。判別は2月4日` },
  s05: { ch: 4, sec: '4-1', theme: 'シナリオ台帳', why: '会社の計画をピースに分け、どれが数字で作動しているかを見る',
    title: `経営陣シナリオの6ピースのうち、利益を動かす4つが作動している\n電子材料・上海・高付加価値品・採算是正。資本政策は途中` }, // lint-ok: 「6」「4」はピースの数
  s05a: { ch: 4, sec: '4-2', theme: '中計の進捗', why: '中計のセグメント別の計画に対し、どのレバーが先行し、どれが遅れているかを示す',
    title: `中計の目標は汎用3セグメントが先に稼ぐ。年換算で計画を${F.n('calc.legacy_vs_plan')}百万円超え\nSC(電材)は計画の${F.n('calc.plan_prog_spec')}%。残りは電材二期の立ち上げにかかる` }, // lint-ok: 「30億」は中計の目標の呼び名
  s06: { ch: 4, sec: '4-3', theme: '変曲点', why: '成長を律速していた制約が、いつ解けるかを日付で押さえる',
    title: `変曲点は2026年に集中する。上海は3月稼働、電材二期は11月完工予定\n投資の山を越え、2027年3月期からFCFが黒字に転じる` },
  s07: { ch: 4, sec: '4-4', theme: '電子材料', why: '最大のピースの成長余地と、投資の利回りを数量で示す',
    title: `電材の能力は${F.n('cap.ep1_capacity')}t→${F.n('em.capacity_after')}t。市場は年6〜9%、差はシェアで取る\n増設の税後ROICは${F('em.roic_at')}。KrF需要と取引先の要請が裏付け` }, // lint-ok: 「6〜9%」は mkt.resist_cagr・mkt.resist_cagr_qy・mkt.krf_cagr の幅
  s08: { ch: 4, sec: '4-5', theme: '技術の主因', why: 'なぜ他社でなく東邦化学なのかを、成長分野と現金を稼ぐ側の両方で示す',
    title: `電材は狭分散PHSの作り分け、界面活性剤は1つの技術の6用途展開\n両者は設備と人を共有し、汎用品の現金が電材を育てている` }, // lint-ok: 「1つ」「6用途」は数
  s09: { ch: 4, sec: '4-6', theme: '工場の作り替え', why: '変化を生む仕組み(工場の役割分担)を図で示す',
    title: `千葉を電子材料の拠点に、汎用品を上海・鹿島へ移している\n取引先の要請に応える能力と人を、千葉に集めている` },
  s10: { ch: 5, sec: '5-1', theme: '営業利益の積み上げ', why: '5年間の増益をセグメントに分け、会社の目標・シナリオと並べる',
    title: `5年後の営業利益は基準で${F.n('fwd.base.op31')}百万円。増益の${SHARE(F.v('fy26.seg_spec_profit'), B31.sc)}割はSC、${SHARE(F.v('fy26.seg_surf_profit'), B31.surf)}割は界面活性剤\n中計目標${F.n('mp.fy31_op')}百万円より${F.n('calc.op_gap_target')}百万円低い、保守的な置き方` },
  s10b: { ch: 5, sec: '5-2', theme: '損益の流れ', why: '5年後の損益の流れを大きく示し、見るべき3か所を指す',
    title: `5年後は売上+${SK.total.yoy.toFixed(0)}%に対し、営業利益+${SK.op.yoy.toFixed(0)}%と利益が速く伸びる\n粗利率${F.n('fy26.gross_margin')}→${GM31}%の上昇と、販管費の伸びの抑制が効く` },
  s11: { ch: 5, sec: '5-3', theme: '5年後の貸借対照表', why: '設備投資・償却・売却・配当・返済で、貸借対照表がどう変わるかを示す',
    title: `5年後の貸借対照表は、借入が減る一方で自己資本が積み上がる\n借入${F.n('fy26.ibd')}→${F.n('fwd.base.ibd31')}百万円。返さなければ資本が余りROEを抑える` },
  s12: { ch: 5, sec: '5-4', theme: 'ROEと資本の使い道', why: 'ROEの経路が株価の分かれ目であり、資本の使い道の利回りに序列があることを示す',
    title: `ROE10%には利益の伸びだけでは届かず、${F.n('roe.return_need')}百万円の返還が要る\nPBR${F.n('px.pbr')}倍での自己株取得ならEPSは+${F.n('bb.eps_up')}%。最大の分かれ目` }, // lint-ok: 「10%」は会社の目標値(mp.fy31_roe)
  s13: { ch: 6, sec: '6-1', theme: '推進役と承継', why: '変革を誰が進め、誰が引き継ぐかを経歴と担当から示す',
    title: `変革の推進役は見えている。資本政策は川崎常務、生産移管は越坂常務\n社長は80歳で交代期。後継の選び方が最大の論点` }, // lint-ok: 「80歳」は有報の生年からの年齢
  s14: { ch: 7, sec: '7-1', theme: '市場の織り込み', why: '株価が前提にしているROEを逆算し、市場との差を数字で示す',
    title: `市場の株価は、ROE${F.n('calc.implied_roe')}%が永久に続く前提の値段になっている\n実力${F.n('calc.core_roe_h1')}%、5年後${F.n('fwd.base.roe31')}%への経路も、上方修正も織り込まれていない` },
  s14b: { ch: 7, sec: '7-2', theme: '価値の芯', why: '理論株価を最も動かす変数を、valuate.py の感応度で特定する',
    title: `価値の芯は全社の粗利率。1ptで理論株価が±${Math.round(P('val.sens.全社の粗利率 +1pt(EPS +21%).diff'))}円、電材30tの約${(P('val.sens.全社の粗利率 +1pt(EPS +21%).diff') / P('val.sens.電材の販売数量 +30t(EPS +8%).diff')).toFixed(1)}倍\n粗利率1ptは電材${F.n('calc.gm1_tons', { noEst: true })}t分。同業との差${F('gap2.gm_pt')}が上値の源泉になる` }, // lint-ok: 「1pt」は感応度の単位、「30t」は感応度の幅
  s15: { ch: 7, sec: '7-3', theme: '13条件(1〜7)', why: '構造評価の根拠を、現在・5年後・確率の3列で示す',
    title: `条件1〜7: 稼ぐ力は価格転嫁と数量で示され、安い理由は見落とし\nFCFは今C、投資の山を越えて5年後はB(確率70%)` }, // lint-ok: 条件番号と確率は採点表(conditions.json)の値
  s16: { ch: 7, sec: '7-3', theme: '13条件(8〜13)', why: '構造評価の根拠を、現在・5年後・確率の3列で示す',
    title: `条件8〜13: 汎用品の比率は高いが、製品単位で高収益品へ移っている\n電材は止められない消耗品で、更なる増設なら条件3・9が上がる` }, // lint-ok: 条件番号
  s17: { ch: 7, sec: '7-4', theme: '価値評価', why: '3経路・シナリオ・感応度で価値を示す(計算は valuate.py)',
    title: `理論株価は事業エンジン経路で${R('val.value.engine')}円(${F.n('val.gap.engine.last')})、3経路とも上回る\n弱気${R('val.scen.bear.value')}円・強気${R('val.scen.bull.value')}円。定常ROEが6.5%なら${F.n('val.roe65')}円` }, // lint-ok: 「6.5%」は交差確認の前提
  s18b: { ch: 7, sec: '7-5', theme: '弱気の反論', why: '懐疑的な投資家の反論を数字で検証し、正しいものは評価に入れる',
    title: `弱気の反論8つを検証した。ナフサ下落は逆に追い風で、流動性は足りる\n還元の実績ゼロと販管費の伸びは正しく、定常ROEと感応度に入れた` }, // lint-ok: 「8つ」は反論の数
  s18: { ch: 7, sec: '7-6', theme: '投資行動', why: 'エントリー圏と判別KPIを日付つきで示す',
    title: `現在値${F.n('px.close')}円は${F.n('val.entry.zone.last')}圏(即時は${R('val.entry.Z1')}円以下)。判別は2月4日と5月13日\n粗利率の維持と製品在庫日数の改善を確かめて、本格保有へ移る` },
  s19: { ch: 7, sec: '7-7', theme: '下振れ', why: '最大の下振れの大きさと、兆候で管理するリスクを示す',
    title: `最大の下振れは2022年型の利益率の崩れで、その場合${F.n('val.crash')}円\n承継・原料・金利・金属酸化物レジストは兆候で管理する` },
};

function ctxFor(id) {
  const meta = META[id];
  if (!meta) throw new Error('META にない id: ' + id);
  const page = ORDER.indexOf(id) + 1;
  const ch = CH[meta.ch - 1];
  let secLabel = '';
  if (meta.sec) {
    const sec = ch.secs.find(r => r[0] === meta.sec);
    const same = ORDER.filter(k => META[k].sec === meta.sec && META[k].ch === meta.ch);
    secLabel = meta.sec + ' ' + (sec ? sec[1] : '') + (same.length > 1 ? `(${same.indexOf(id) + 1}/${same.length})` : '');
  }
  return { id, page, total: ORDER.length, meta, ch, secLabel };
}
function secPages(chNo) {
  return CH[chNo - 1].secs.map(([no, name]) => {
    const pages = ORDER.map((k, i) => [k, i + 1]).filter(([k]) => META[k].ch === chNo && META[k].sec === no).map(([, p]) => p);
    return { no, name, from: pages[0], to: pages[pages.length - 1] };
  });
}
const DOC_TITLE = '東邦化学工業(4409)長期保有適格性審査', DOC_AUTHOR = '長期保有適格性審査';
module.exports = { CH, ORDER, META, ctxFor, secPages, DOC_TITLE, DOC_AUTHOR };
