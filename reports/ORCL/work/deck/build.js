// 全 40 枚を順に組み立てる: node build.js → ORCL_deck.pptx(存在しないスライドは飛ばして警告)
const L = require('./lib.js');
const fs = require('fs');
const pres = L.newDeck();
const missing = [];
for (let i = 1; i <= 40; i++) {
  const f = `./slides/s${String(i).padStart(2, '0')}.js`;
  if (fs.existsSync(f)) require(f)(pres, L); else missing.push(i);
}
pres.writeFile({ fileName: 'ORCL_deck.pptx' }).then(() => console.log('written; missing:', missing.join(',') || 'none'));
