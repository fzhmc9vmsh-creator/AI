// meta.js のタイトルを F() 展開後の字数で測る。全角=1、半角=0.55 で換算し、1行40を超えたら警告
const MT = require(require('path').resolve(process.cwd(), 'meta.js'));   // 資料のフォルダ(meta.js のある場所)で実行する
const w = s => [...s].reduce((a, c) => a + (c.charCodeAt(0) < 0x2000 ? 0.55 : 1), 0);
let bad = 0;
for (const id of MT.ORDER) {
  const t = MT.META[id].title; if (!t) continue;
  const lines = t.split('\n'); const lw = lines.map(w);
  const over = lines.length > 2 || lw.some(x => x > 40);
  if (over) bad++;
  console.log(`${over ? 'NG' : 'ok'} ${id} ` + lw.map(x => x.toFixed(0)).join('/') + (over ? '  ' + lines.map(l => l.slice(0, 18) + '…').join(' | ') : ''));
}
console.log('NG', bad);
