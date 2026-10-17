// 分析ロジック(指示書 spec/ch1_ch4a.md の s05 節どおり。見本 examples.js の exFlow をそのまま使う)
const ex = require('../examples.js');
module.exports = function build(pres, L) {
  return ex.exFlow(pres);
};
