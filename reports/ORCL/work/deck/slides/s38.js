// サマリと示唆(指示書 spec/ch4b.md の s38 節)。左 5 行の事実と右 5 行の示唆は同じ行で対応させる
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: '評価の事実は「構造 B・価格 1.75 倍・差分未確立」で、行動は「分割で建て、KPI で差分を確かめる」', kicker: '左: 分析結果のサマリ(事実)。右: 示唆とネクストアクション(左の行と対応)', source: '本資料の各章', page: 38 });

  L.paneHead(s, 0.5, 1.62, 6.05, '分析結果のサマリ');
  L.paneHead(s, 6.78, 1.62, 6.05, '示唆・ネクストアクション');

  const rows = [
    ['構造評価 B(S1・A2・B8・C2)。弱点は条件7・8', '判断は「買い検討」。株価 143.20 ドルは分割エントリー圏(136〜229 ドル)'],
    ['理論株価 251 ドル(株価の 1.75 倍)。3 経路の乖離は +61〜+77%', '3 回に分けて建て、AI 投資の逆回転で −50% でも許容できる大きさに抑える'],
    ['下値 −16%(DCF では −36%)、上値 +150%', '下値は DCF の −36% を前提に建玉を決める'],
    ['市場は弱気寄りの倍率(15.7 倍)で、EPS ではなく現金化を疑う', '引き上げ条件: 納入 1GW/四半期・OpenAI 比率 40% 未満・CDS 200bp 未満・FY30〜32 の電力確保のうち 2 つ以上'],
    ['争点は FY29 の FCF と OpenAI の支払能力', '撤退: OpenAI の契約変更・支払遅延、FY29 より前の BB+、CDS 300bp 超。次の確認は AI World と 12 月の Q2 決算'],
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
