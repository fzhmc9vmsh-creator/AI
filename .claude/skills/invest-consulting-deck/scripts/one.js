// 1 枚だけ作って確認する: node one.js 17(または 08b)→ tmp/s17.pptx と tmp/s17.jpg、図の重なりと監査結果を表示
const L = require('./lib.js');
const { execSync } = require('child_process');
const arg = String(process.argv[2]);
const id = 's' + (/^\d$/.test(arg) ? '0' + arg : arg);
const build = require(`./slides/${id}.js`);
const pres = L.newDeck();
L.setCtx(L.MT.META[id] ? id : null);
build(pres, L);
L.warnings.forEach(w => console.log('図:', w));
console.log(`図の重なり ${L.warnings.length} 件`);
const out = `tmp/${id}.pptx`;
L.save(pres, out).then(() => {
  try { console.log(execSync(`python3 audit_deck.py ${out}`).toString()); } catch (e) { console.log(e.stdout.toString()); }
  // 画像化: pptx スキルの soffice.py(サンドボックス向けの起動)があれば使い、なければ soffice を直接呼ぶ
  const fs = require('fs'), glob = (d) => { try { return fs.readdirSync(d).map(x => d + '/' + x + '/pptx/scripts/office/soffice.py').find(f => fs.existsSync(f)); } catch (e) { return null; } };
  const sp = process.env.SOFFICE_PY || glob('/root/.claude/skills/synced');
  const conv = sp ? `python3 ${sp}` : 'soffice';
  execSync(`cd tmp && ${conv} --headless -env:UserInstallation=file:///tmp/lo_${id} --convert-to pdf ${id}.pptx >/dev/null 2>&1 && pdftoppm -jpeg -r ${process.env.DPI || 80} -singlefile ${id}.pdf ${id}`);
  console.log('image:', require('path').resolve(`tmp/${id}.jpg`));
});
