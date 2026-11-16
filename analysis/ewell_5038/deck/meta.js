// eWeLL(5038) 銘柄分析の資料。章・節・テーマ・なぜ・タイトルの一括管理。タイトルの数字は F('id') で台帳から引く
const F = require('./facts.js');
const CH = [
  { no: 1, name: '結論', short: '結論', why: '判断と、株価との差の正体を先に示す', secs: [['1-1', '結論'], ['1-2', '目次'], ['1-3', '価値の橋']] },
  { no: 2, name: '事業の前提', short: '前提', why: '何を売り、どこで稼ぐかを先に押さえる', secs: [['2-1', '製品と課金'], ['2-2', '損益の流れ']] },
  { no: 3, name: '変化', short: '変化', why: '単価と粗利率で何が変わったかを分解する', secs: [['3-1', '顧客単価の分解'], ['3-2', '粗利率とサーバー費']] },
  { no: 4, name: '持続と段差', short: '持続', why: '成長の分母と、奪われない理由と、次の段差の日付', secs: [['4-1', '獲得の分母'], ['4-2', '価格決定力'], ['4-3', '段差の日付']] },
  { no: 5, name: '5年後の構造', short: '5年後', why: '数量×単価で損益と資本を積み上げる', secs: [['5-1', '5年後の損益'], ['5-2', 'ROEと資本']] },
  { no: 6, name: '経営', short: '経営', why: '誰が実行し、資本をどう配るか', secs: [['6-1', '経営と統治']] },
  { no: 7, name: '市場との差分と価値', short: '価値', why: '市場の前提を数字にし、いくらで・いつ動くかを決める', secs: [['7-1', '価値の芯'], ['7-2', '13条件'], ['7-3', '反論'], ['7-4', '投資行動']] },
];
const ORDER = ['s01', 's02', 's03', 's04', 's05', 's06', 's07', 's08', 's09', 's10', 's11', 's12', 's13', 's14', 's15', 's16', 's17', 's18'];
const META = {
  s01: { ch: 1, kind: 'cover' },
  s02: { ch: 1, sec: '1-1', theme: '結論', why: '判断・理論株価・エントリー圏・見直しの日を最初に示す',
    title: `質の高い従量課金SaaSだが、株価 ${F('price.last')} は資本コスト約 ${F('calc.implied_coe')} を前提にする。\n理論株価 ${F('val.value.engine')} 円で「${F('val.decision.last')}」、${F('val.entry.Z2')} 円以下で分割` },
  s03: { ch: 1, sec: '1-2', theme: '目次', why: '7つの問いの順に、判断の根拠を確かめる',
    title: '前提 → 変化 → 持続 → 5年後 → 人 → 価格の順に、\n7つの問いで判断の根拠を確かめる' },
  s04: { ch: 1, sec: '1-3', theme: '価値の橋', why: '株価との差を段に分け、市場の前提を数字にする',
    title: `株価と理論株価の差 640 円のうち 455 円(71%)は倍率の差。\n株価は資本コスト約 ${F('calc.implied_coe')}(当方 8.9%)を前提にする` },
  s05: { ch: 2, sec: '2-1', theme: '製品と課金', why: '課金の単位が事業の性質を決める',
    title: `売上の 7 割は基本料 18,000 円 + 1 訪問 100 円の iBow。\n1 訪問 8,500 円のうち当社の取り分は約 136 円(${F('calc.cost_share_rev')})` },
  s06: { ch: 2, sec: '2-2', theme: '損益の流れ', why: '費用を維持・獲得・投資に分けて読む',
    title: `粗利率 78%・営業利益率 45%。販売費を除けば ${F('calc.opm_ex_sales')} で、\n粗利の約 9 割はクラウドにたまる` },
  s07: { ch: 3, sec: '3-1', theme: '顧客単価の分解', why: '従量課金が業界の成長を取り込んでいるかを確かめる',
    title: `顧客単価の伸び +6.0 千円の約 9 割は AI と BPaaS。\niBow 本体の 1ST 単価は ${F('calc.ibow_per_st_q26')} で前年同期から +0.1 千円の横ばい` },
  s08: { ch: 3, sec: '3-2', theme: '粗利率とサーバー費', why: '粗利率の低下が一時か構造かを分ける',
    title: 'サーバー費は 3 年で約 3.7 倍になり、粗利率は 4 期連続で前年割れ。\n2027 年 1 月の基本料 +10% で増分の約 6 割を戻す' },
  s09: { ch: 4, sec: '4-1', theme: '獲得の分母', why: '契約数の伸びを決めるものを特定する',
    title: `業界の新規開設は年約 2,450 件で 3 年横ばい(直近 ${F('ind.new_2026')})。\n獲得は約 660 件で頭打ちで、契約数の伸びは 13.5% → 約 9% に減速する` },
  s10: { ch: 4, sec: '4-2', theme: '価格決定力', why: '価格が離脱の理由になっているかを確かめる',
    title: `定額の競合より ${F('calc.price_ratio_500')} 高いのに、他社への流出は年 ${F.n('calc.switch_rate_fy25')}% → ${F('calc.switch_rate_fy26')} に低下。\n1 訪問 100 円は 12 年据え置きの未行使の価格決定力` },
  s11: { ch: 4, sec: '4-3', theme: '段差の日付', why: '経営陣のシナリオを日付と変数に直す',
    title: '次の段差は 2027 年 1 月の基本料 +10% とボード Pro の課金。\n大きさは年約 80〜180 百万円で、売上の約 2〜4%' },
  s12: { ch: 5, sec: '5-1', theme: '5年後の損益', why: '数量×単価で積み上げ、会社計画と並べる',
    title: '2030 年は契約 5,615 件 × 単価 110.3 千円で、売上 7,191 百万円。\n営業利益 3,380 百万円・EPS 156.5 円。会社計画より単価が約 7% 低い' },
  s13: { ch: 5, sec: '5-2', theme: 'ROEと資本', why: '利益が現金になった後の使い道を見る',
    title: '現預金が総資産の 67% に積み上がり、ROE は 67% → 32% に半減。\n今の株価での自己株取得の益回り 4.35% は資本コスト 8.9% を下回る' },
  s14: { ch: 6, sec: '6-1', theme: '経営と統治', why: '事業を築いた人と、資本配分の規律を分けて見る',
    title: `創業者(${F('hold.founder')} 保有)が 2012 年に設立し、3,843 事業所の事業を築いた。\n社外取締役は 4 名中 1 名で、還元方針の説明は 4 日で変わった` },
  s15: { ch: 7, sec: '7-1', theme: '価値の芯', why: 'ありうる振れ幅で変数を 1 株の円に直して並べる',
    title: '価値を最も動かすのは資本コスト(8.0% で +349 円)。\n事業の変数では契約数(+147.5 円)と単価(+145.3 円)が並ぶ' },
  s16: { ch: 7, sec: '7-2', theme: '13条件', why: '構造評価を倍率に直す前提を示す',
    title: `13 条件は平均 ${F('val.grade.avg')} で等級 ${F('val.grade.letter')}。\n強みは FCF と従量課金(A)、弱みは EPS 成長(D)` },
  s17: { ch: 7, sec: '7-3', theme: '反論', why: '結論を壊しに行き、正しい反論で前提を直す',
    title: `弱気の反論 8 件を検証し、3 件が正しく前提を直した。\n理論株価は約 1,702 円から ${F('val.value.engine')} 円に下がり、判断は変わらない` },
  s18: { ch: 7, sec: '7-4', theme: '投資行動', why: '撤回の線と日付で行動を決める',
    title: `「${F('val.decision.last')}」。${F('val.entry.Z2')} 円以下で分割(PER 17.2 倍でも年率約 23%)。\n2027 年 2 月・5 月・7 月の数字で見直す` },
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
