// 数字の台帳(facts_deck.json)から表示値を引く。スライドとタイトルの数字は、すべて F('id') で書く(手で数字を打たない)。
// facts_deck.json は meigara-bunseki-method の scripts/facts.py export(台帳 + valuate.py の表示値)で作る。
//   F('q3.revenue')          → '1385.1 百万ドル'(台帳の disp。丸めは台帳で 1 回だけ)
//   F('val.value.engine')    → '23.8'(valuate.py の display。id は 'val.' + display のキー)
//   F.n('q3.revenue')        → '1385.1'(単位なし)
//   F.v('q3.revenue')        → 1385.1(チャートの数値。数値型)
// 時点のラベル: 四半期の値(period が 'Q2 2026' など)が資料の基準の時点(as_of)と違うと、自動で '(Q2)' を付ける。
//   本文で時点をすでに書いているときだけ F(id, { noPeriod: true }) で外す(lint_deck.py が一覧にする)。
// 推定・未取得: 推定の値には '(推定)' を付け、未取得は '未取得' を返す。
const fs = require('fs');
const path = require('path');

let DB = null;
function load() {
  if (DB) return DB;
  const p = process.env.FACTS_DECK || path.join(process.cwd(), 'facts_deck.json');
  if (!fs.existsSync(p)) throw new Error(`facts_deck.json が見つからない(${p})。facts.py export で作ってから組む`);
  DB = JSON.parse(fs.readFileSync(p, 'utf8'));
  return DB;
}

function get(id) {
  const db = load();
  const f = db.facts[id];
  if (!f) throw new Error(`台帳に無い id: '${id}'。facts.json に登録して facts.py export をやり直す(数字を手で書いて逃げない)`);
  return f;
}

function periodLabel(f, asOf) {
  const q = /^Q([1-4]) (\d{4})$/;
  const m = q.exec(f.period || ''), a = q.exec(asOf || '');
  if (!m || f.period === asOf) return '';
  return a && a[2] === m[2] ? `(Q${m[1]})` : `(Q${m[1]} ${m[2]})`;
}

function F(id, o = {}) {
  const db = load();
  const f = get(id);
  if (f.status === '未取得') return '未取得';
  let s = o.num ? numPart(f) : f.disp;
  if (!o.noPeriod) s += periodLabel(f, db.as_of);
  if (f.status === '推定' && !o.noEst) s += '(推定)';
  return s;
}
function numPart(f) {
  const u = f.unit || '';
  if (!u) return f.disp;
  return f.disp.replace(new RegExp('\\s*' + u.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$'), '');
}
F.n = (id, o = {}) => F(id, Object.assign({}, o, { num: true }));
F.v = (id) => { const f = get(id); if (typeof f.value !== 'number') throw new Error(`'${id}' は数値でない(チャートには数値の行を使う)`); return f.value; };
F.has = (id) => { try { get(id); return true; } catch (e) { return false; } };
F.asOf = () => load().as_of;
module.exports = F;
