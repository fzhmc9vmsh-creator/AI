// 全スライドを meta.js の ORDER 順に組み立てる: node build.js out/deck.pptx(省略時は deck.pptx)
// ページ番号・現在地・テーマ・なぜ・タイトルは meta.js から入る(スライド側の page は使わない)
const L = require('./lib.js');
const fs = require('fs');
const pres = L.newDeck();
const missing = [];
for (const id of L.MT.ORDER) {
  const f = `./slides/${id}.js`;
  if (!fs.existsSync(f)) { missing.push(id); continue; }
  L.setCtx(id);
  const before = L.warnings.length, nb = L.notices.length;
  require(f)(pres, L);
  L.warnings.slice(before).forEach(w => console.log(`${id}: 図: ${w}`));
  L.notices.slice(nb).forEach(w => console.log(`${id}: 確認: ${w}`));
}
L.setCtx(null);
const out = process.argv[2] || 'deck.pptx';
L.save(pres, out).then(() => console.log(`written ${out}; slides ${L.MT.ORDER.length - missing.length}; missing: ${missing.join(',') || 'none'}; 図の重なり ${L.warnings.length} 件; 画像で確認 ${L.notices.length} 件`));
