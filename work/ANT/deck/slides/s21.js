// 成長に対する値段: 前の章の数字を 6 段でつなぎ、公開価格の PEG を許容 PEG と比べる
module.exports = function build(pres, L) {
  const { F } = L;
  const s = L.contentSlide(pres, { kicker: '前の章までの数字を順につなぐと、公開価格が許容を超えるかどうかが決まる', source: '当分析' });
  L.flow(s, [
    { head: '① 1 株利益', boxes: [{ text: '1 株利益\n2027 年 1.08 ドル\n(p.16)', tone: 'off', size: 11, h: 1.7 }] },
    { head: '② 成長', boxes: [{ text: '伸び 43.1%\n(リスクを入れた採用の道筋、p.16・p.19)', tone: 'off', size: 11, h: 1.7 }] },
    { head: '③ 値段', boxes: [{ text: '公開価格の上限の\nPER 72 倍\n(p.22)', tone: 'off', size: 11, h: 1.7 }] },
    { head: '④ 今の PEG', boxes: [{ text: '72 ÷ 43.1\n= 1.67 倍', tone: 'key', bold: true, size: 12, h: 1.7 }] },
    { head: '⑤ 許容 PEG', boxes: [{ text: '1.242 倍\n(13 の条件の評価 B から、p.27)', tone: 'on', size: 11, h: 1.7 }] },
    { head: '⑥ 判定', boxes: [{ text: '許容を超える', tone: 'on', bold: true, size: 12, h: 1.7 }] },
  ], { x: 0.5, y: 1.7, w: 12.33, h: 2.4, gap: 0.3 });
  L.kpiTiles(s, [
    { value: F('peg.78'), label: '今の PEG(公開価格の上限)' },
    { value: F('peg.allow'), label: '許容 PEG' },
    { value: F('peg.allow.30'), label: '成長が 2030 年に減速した後の許容 PEG' },
  ], { compact: true, x: 0.5, y: 4.4, w: 12.33, h: 1.5 });
  L.termNotes(s, [{ term: '許容PEG', plain: '13条件の構造評価から決める、払ってよいPEGの上限', why: '今のPEGが妥当かを判定する基準のため' }], { x: 0.5, y: 6.3, w: 12.33 });
};
