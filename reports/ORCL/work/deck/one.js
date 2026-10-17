// 1 枚だけ作って確認する: node one.js 17 → tmp/s17.pptx と tmp/s17.jpg、監査結果を表示
const L = require('./lib.js');
const { execSync } = require('child_process');
const n = String(process.argv[2]).padStart(2, '0');
const build = require(`./slides/s${n}.js`);
const pres = L.newDeck();
build(pres, L);
const out = `tmp/s${n}.pptx`;
pres.writeFile({ fileName: out }).then(() => {
  const SK = '/root/.claude/skills/synced/d5524a36-023e-44e0-82ef-a185c180efe9_97f00e8a-e07f-474c-8eeb-29009efb3a97/pptx';
  try { console.log(execSync(`python3 audit_deck.py ${out}`).toString()); } catch (e) { console.log(e.stdout.toString()); }
  execSync(`cd tmp && python3 ${SK}/scripts/office/soffice.py --headless --convert-to pdf s${n}.pptx >/dev/null 2>&1 && pdftoppm -jpeg -r 80 -singlefile s${n}.pdf s${n}`);
  console.log('image:', require('path').resolve(`tmp/s${n}.jpg`));
});
