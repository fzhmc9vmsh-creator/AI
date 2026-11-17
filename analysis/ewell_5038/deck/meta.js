// eWeLL(5038) 銘柄分析の資料。章・節・テーマ・なぜ・タイトルの一括管理。タイトルの数字は F('id') で台帳から引く
const F = require('./facts.js');
const CH = [
  { no: 1, name: '結論', short: '結論', why: '判断と、株価との差の正体を先に示す', secs: [['1-1', '結論'], ['1-2', '目次'], ['1-3', '価値の橋']] },
  { no: 2, name: '事業の前提', short: '前提', why: '何をしている会社か、業界とお金の流れ、直近の決算を先に押さえる', secs: [['2-1', '事業の概要'], ['2-2', '業界とお金の流れ'], ['2-3', '最新決算'], ['2-4', '製品と課金'], ['2-5', '損益の流れ']] },
  { no: 3, name: '変化', short: '変化', why: '単価と粗利率で何が変わったかを分解する', secs: [['3-1', '顧客単価の分解'], ['3-2', '粗利率とサーバー費']] },
  { no: 4, name: '持続と段差', short: '持続', why: '成長の分母と、奪われない理由と、次の段差の日付', secs: [['4-1', '獲得の分母'], ['4-2', '事業構造の解剖'], ['4-3', '価格決定力'], ['4-4', '段差の日付']] },
  { no: 5, name: '5年後の構造', short: '5年後', why: '数量×単価で損益と資本を積み上げる', secs: [['5-1', '5年後の損益'], ['5-2', 'ROEと資本']] },
  { no: 6, name: '経営', short: '経営', why: '誰が実行し、資本をどう配るか', secs: [['6-1', '経営と統治']] },
  { no: 7, name: '市場との差分と価値', short: '価値', why: '市場の前提を数字にし、いくらで・いつ動くかを決める', secs: [['7-1', '価値の芯'], ['7-2', '13条件'], ['7-3', '反論'], ['7-4', '投資行動']] },
];
const ORDER = ['s01', 's02', 's03', 's04', 's04a', 's04b', 's04c', 's05', 's06', 's07', 's08', 's09', 's09a', 's10', 's11', 's12', 's13', 's14', 's15', 's16', 's17', 's18'];
const META = {
  s01: { ch: 1, kind: 'cover' },
  s02: { ch: 1, sec: '1-1', theme: '結論', why: '判断・理論株価・エントリー圏・見直しの日を最初に示す',
    title: `質の高い従量課金SaaSだが、株価 ${F('price.last')} は資本コスト約 ${F('calc.implied_coe')} を前提にする。\n理論株価 ${F('deck.theory')}で「${F('val.decision.last')}」、${F('deck.z2')}以下で分割` },
  s03: { ch: 1, sec: '1-2', theme: '目次', why: '7つの問いの順に、判断の根拠を確かめる',
    title: '前提 → 変化 → 持続 → 5年後 → 人 → 価格の順に、\n7つの問いで判断の根拠を確かめる' },
  s04: { ch: 1, sec: '1-3', theme: '価値の橋', why: '株価との差を段に分け、市場の前提を数字にする',
    title: `株価と理論株価の差 ${F('deck.gap')} のうち ${F('deck.gap_multiple')}(${F('deck.gap_multiple_share')})は倍率の差。\n株価は資本コスト約 ${F('calc.implied_coe')}(当方 ${F('deck.coe')})を前提にする` },
  s04a: { ch: 2, sec: '2-1', theme: '事業の概要', why: '何をしている会社かを、分析の前に平易に押さえる',
    title: `訪問看護の事業所に、記録から請求までスマホで済む電子カルテ iBow を提供。\n契約 ${F('q26q3.stations')}(シェア ${F('share.q26q3')})、基本料 ${F('price.base_now')} + 1 訪問 ${F('price.per_visit')}` },
  s04b: { ch: 2, sec: '2-2', theme: '業界とお金の流れ', why: '顧客の収入の源と、当社がお金の流れのどこにいるかを押さえる',
    title: `訪問看護は公定価格の医療・介護サービス。保険から 1 訪問約 ${F('revenue_per_visit_station')} が\n事業所に入り、約 ${F('deck.take_per_visit')}(売上の ${F('calc.cost_share_rev')})が当社に払われる` },
  s04c: { ch: 2, sec: '2-3', theme: '最新決算', why: '直近の四半期で何が起き、何が変わったかを押さえる',
    title: `3Q 累計は売上 ${F('9m26.revenue')}(+${F('9m26.rev_yoy')})・営業利益 ${F('9m26.op')}(+${F('9m26.op_yoy')})。\n値上げを決め単価は加速したが、新規獲得は前年並み` },
  s05: { ch: 2, sec: '2-4', theme: '製品と課金', why: '課金の単位が事業の性質を決める',
    title: `売上の 7 割は基本料 ${F('price.base_now')} + 1 訪問 ${F('price.per_visit')} の iBow。\n1 訪問 ${F('revenue_per_visit_station')} のうち当社の取り分は約 ${F('deck.take_per_visit')}(${F('calc.cost_share_rev')})` },
  s06: { ch: 2, sec: '2-5', theme: '損益の流れ', why: '費用を維持・獲得・投資に分けて読む',
    title: `粗利率 ${F('fy25.gm')}・営業利益率 ${F('fy25.opm')}。販売費を除けば ${F('calc.opm_ex_sales')} で、\n粗利の約 9 割はクラウドにたまる` },
  s07: { ch: 3, sec: '3-1', theme: '顧客単価の分解', why: '従量課金が業界の成長を取り込んでいるかを確かめる',
    title: `顧客単価の伸び +${F('deck.arpu_delta')} の約 9 割は AI と BPaaS。\niBow 本体の 1ST 単価は ${F('calc.ibow_per_st_q26')} で前年同期から +${F('deck.ibow_delta')} の横ばい` },
  s08: { ch: 3, sec: '3-2', theme: '粗利率とサーバー費', why: '粗利率の低下が一時か構造かを分ける',
    title: `サーバー費は 3 年で約 ${F('deck.server_mult')} になり、粗利率は 4 期連続で前年割れ。\n2027 年 1 月の基本料 +${F('price.hike_pct')} で増分の約 6 割を戻す` },
  s09: { ch: 4, sec: '4-1', theme: '獲得の分母', why: '契約数の伸びを決めるものを特定する',
    title: `業界の新規開設は年約 ${F('deck.new_avg')} で 3 年横ばい(直近 ${F('ind.new_2026')})。\n獲得は約 ${F('deck.adds_base')} で頭打ちで、契約数の伸びは ${F('deck.st_growth_now')}(3Q)→ 2029 年に約 ${F('deck.st_growth_2029')} へ減速` },
  s09a: { ch: 4, sec: '4-2', theme: '事業構造の解剖', why: '並べる相手を変えると、会社の説明と違う構造が見える',
    title: `価値の正体は請求の正しさ、成長の律速は自社の外、守れているのは既存顧客。\n利用料は事業所の売上の ${F('calc.cost_share_rev')} だが、利益の ${F.n('deck.fee_profit_lo')}〜${F('deck.fee_profit_hi')} を占める` },
  s10: { ch: 4, sec: '4-3', theme: '価格決定力', why: '価格が離脱の理由になっているかを確かめる',
    title: `定額の競合より ${F('calc.price_ratio_500')} 高いのに、他社への流出は年 ${F.n('calc.switch_rate_fy25')}% → ${F('calc.switch_rate_fy26')} に低下。\n1 訪問 ${F('price.per_visit')} は 12 年据え置きの未行使の価格決定力` },
  s11: { ch: 4, sec: '4-4', theme: '段差の日付', why: '経営陣のシナリオを日付と変数に直す',
    title: `次の段差は 2027 年 1 月の基本料 +${F('price.hike_pct')} とボード Pro の課金。\n大きさは年約 80〜180 百万円で、売上の約 ${F.n('deck.step_lo')}〜${F('deck.step_hi')}` },
  s12: { ch: 5, sec: '5-1', theme: '5年後の損益', why: '数量×単価で積み上げ、会社計画と並べる',
    title: `2030 年は契約 ${F('model.st2030')} × 単価 ${F('model.arpu2030')} で売上 ${F('model.rev2030')}・EPS ${F('model.eps2030')}。
単価は会社計画の 2028 年の水準に 2 年遅れで届く` },
  s13: { ch: 5, sec: '5-2', theme: 'ROEと資本', why: '利益が現金になった後の使い道を見る',
    title: `現預金が総資産の ${F('deck.cash_share')} に積み上がり、ROE は ${F('fy21.roe')} → ${F('fy25.roe')} に半減。\n今の株価での自己株取得の益回り ${F('deck.buyback_yield')} は資本コスト ${F('deck.coe')} を下回る` },
  s14: { ch: 6, sec: '6-1', theme: '経営と統治', why: '事業を築いた人と、資本配分の規律を分けて見る',
    title: `創業者(${F('hold.founder')} 保有)が 2012 年に設立し、3,843 事業所の事業を築いた。\n社外取締役は 4 名中 1 名で、還元方針の説明は 4 日で変わった` },
  s15: { ch: 7, sec: '7-1', theme: '価値の芯', why: 'ありうる振れ幅で変数を 1 株の円に直して並べる',
    title: `価値を最も動かすのは資本コスト(${F('deck.coe_low')} で +${F('deck.coe80_diff')})。\n事業の変数では契約数(+${F('deck.sens_st')})と単価(+${F('deck.sens_arpu')})が並ぶ` },
  s16: { ch: 7, sec: '7-2', theme: '13条件', why: '構造評価を倍率に直す前提を示す',
    title: `13 条件は平均 ${F('val.grade.avg')} で等級 ${F('val.grade.letter')}。\n強みは FCF と従量課金(A)、弱みは EPS 成長(D)` },
  s17: { ch: 7, sec: '7-3', theme: '反論', why: '結論を壊しに行き、正しい反論で前提を直す',
    title: `反論 ${F('deck.n_rebut')} のうち正しい ${F('deck.n_correct')} と一部正しい ${F('deck.n_partial')} で前提を直した。\n理論株価は約 ${F('deck.value_pre')} から ${F('deck.theory')}に下がり、判断は変わらない` },
  s18: { ch: 7, sec: '7-4', theme: '投資行動', why: '撤回の線と日付で行動を決める',
    title: `「${F('val.decision.last')}」。${F('deck.z2')}以下で分割(PER ${F('deck.per_mature')} でも年率約 ${F('deck.irr_entry_r')})。\n2027 年 2 月・5 月・7 月の数字で見直す` },
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
const DOC_TITLE = 'eWeLL(5038)銘柄分析 ― 質は高いが、価格がそれを払っている', DOC_AUTHOR = '銘柄分析メソッド';
module.exports = { CH, ORDER, META, ctxFor, secPages, DOC_TITLE, DOC_AUTHOR };
