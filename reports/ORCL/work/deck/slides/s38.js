// サマリと示唆(指示書 spec/ch4b.md の s38 節)。左 5 行の事実と右 5 行の示唆は同じ行で対応させる
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: '評価の事実は「構造 B・価格 1.69 倍・差分は確立の途中」で、行動は「2 回目まで建て、KPI で差分を確かめる」', kicker: '左: 分析結果のサマリ(事実)。右: 示唆とネクストアクション(左の行と対応)', source: '本資料の各章', page: 38 });

  L.paneHead(s, 0.5, 1.62, 6.05, '分析結果のサマリ');
  L.paneHead(s, 6.78, 1.62, 6.05, '示唆・ネクストアクション');

  const rows = [
    ['構造評価 B(S1・A2・B8・C2)。弱点は条件7・8', '判断は「買い検討」。株価 139.56 ドルは Z1(155 ドル)を下回る'],
    ['理論株価 236 ドル(株価の 1.69 倍)。3 経路の乖離は +50〜+69%', '3 回に分けて建て、2 回目までを今の水準で。AI 投資の逆回転で −50% でも許容できる大きさに抑える'],
    ['下値 −1%(DCF では −31%)、上値 +144%', '下値は DCF の −31% を前提に建玉を決める'],
    ['市場は説明会の後も、株価を弱気の値(138 ドル)に置く', '引き上げ条件: 納入 1GW/四半期・OpenAI 比率 40% 未満・CDS 200bp 未満・FY31 以降の電力確保のうち 2 つ以上'],
    ['争点は FY33 の更新の山(契約後の更新単価)と OpenAI の支払能力', '撤退: OpenAI の契約変更・支払遅延、FY29 より前の BB+、\nCDS 300bp 超。次の確認は 12 月の Q2 決算'],
  ];

  rows.forEach(([left, right], i) => {
    const y = 2.05 + i * 0.92;
    const h = 0.82;

    // 左: 白地に灰枠の箱 + 本文(事実)
    L.box(s, 0.5, y, 6.05, h, { fill: L.C.white, line: L.C.rule, name: 'ovl_sum' + i });
    L.text(s, left, { x: 0.62, y: y + 0.08, w: 5.81, h: h - 0.16, fontSize: 10.5, color: L.C.text, valign: 'middle', objectName: 'sum_t' + i });

    // 右: 薄緑の箱 + 濃緑の本文(示唆)
    L.box(s, 6.78, y, 6.05, h, { fill: L.C.tint, line: L.C.tint, name: 'ovl_imp' + i });
    L.text(s, right, { x: 6.9, y: y + 0.08, w: 5.81, h: h - 0.16, fontSize: 10.5, color: L.C.dark, valign: 'middle', objectName: 'imp_t' + i });
  });
};
