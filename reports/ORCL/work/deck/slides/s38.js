// サマリと示唆(指示書 spec/ch4b.md の s38 節)。左 5 行の事実と右 5 行の示唆は同じ行で対応させる
module.exports = function build(pres, L) {
  const s = L.contentSlide(pres, { title: '評価の事実は「構造 B・価格 1.76 倍・株価は価値の 9 パーセンタイル」で、行動は「いま 2/3 を建て、格付けの閾値の時期に残りを建てる」', kicker: '左: 分析結果のサマリ(事実)。右: 示唆とネクストアクション(左の行と対応)', source: '本資料の各章', page: 38 });

  L.paneHead(s, 0.5, 1.62, 6.05, '分析結果のサマリ');
  L.paneHead(s, 6.78, 1.62, 6.05, '示唆・ネクストアクション');

  const rows = [
    ['構造評価 B(S1・A3・B9)。弱点は OpenAI 集中と再契約の単価', '判断は「買い」。株価 139.56 ドルは Z1(151 ドル)の下'],
    ['理論株価 245 ドル(株価の 1.76 倍)。3 経路の乖離は +64〜+76%', '株価は価値の分布の 9 パーセンタイル(1,500 通り)'],
    ['下値 −4%(DCF −28%)、上値 +154%', '下値(DCF −28%)を前提に建玉を決める。\nいま 2/3、残り 1/3 は FY28 下期〜FY29 に'],
    ['市場は説明会の後も、株価を弱気の値(134 ドル)に置く', '検証: Q2 決算の capex・納入、FY28 下期の FCF、OpenAI の資金調達'],
    ['争点は契約後の再契約の単価(推論とデータの重力)と OpenAI の支払能力', '撤退: OpenAI の見直し・支払い遅延と逼迫の終わりの兆しが重なったとき。\n次の確認は 12 月の Q2 決算'],
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
