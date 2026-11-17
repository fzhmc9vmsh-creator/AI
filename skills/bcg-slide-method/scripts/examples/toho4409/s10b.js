// s10b 損益の流れ(大きなサンキー図)
const path = require('path');
const SK = require('../data/sankey_fy31_slide.json');

module.exports = function build(pres, L) {
  const { F, C } = L;
  const s = L.contentSlide(pres, {
    source: '本分析の5年後モデル(基準シナリオ)。26/3期の実績は決算短信。図は meigara-bunseki-method の pl_sankey.py で作成',
  });

  // ----------------------------------------------------
  // 左: 大きなサンキー図
  // ----------------------------------------------------
  L.paneHead(s, 0.5, 1.62, 9.2, '5年後(31/3期 基準)の損益の流れ(百万円)。緑の文字は26/3期実績との比較');

  // 画像 data/sankey_fy31_slide.png を x0.5 y1.98 w9.2 h4.69 に置く(縦横比 2200:1122)
  s.addImage({
    path: path.resolve(__dirname, '../data/sankey_fy31_slide.png'),
    x: 0.5,
    y: 1.98,
    w: 9.2,
    h: 4.69,
  });

  // 図の上に番号の丸(直径0.28、C.primary 塗り白字)を3つ重ねる
  // ① 売上総利益の数字の左 (x≈3.82, y≈2.25)
  // ② 販管費の帯の左 (x≈6.25, y≈3.25)
  // ③ 営業利益の数字の左 (x≈5.48, y≈2.12)
  const circles = [
    { num: '1', x: 3.82, y: 2.25 },
    { num: '2', x: 6.25, y: 3.25 },
    { num: '3', x: 5.48, y: 2.12 },
  ];

  circles.forEach(c => {
    s.addShape('ellipse', {
      x: c.x,
      y: c.y,
      w: 0.28,
      h: 0.28,
      fill: { color: C.primary },
      line: { color: C.primary },
      objectName: `ovl_sankey_circle_${c.num}`,
    });
    s.addText(c.num, {
      x: c.x,
      y: c.y,
      w: 0.28,
      h: 0.28,
      fontFace: 'Meiryo UI',
      fontSize: 10,
      bold: true,
      color: C.white,
      align: 'center',
      valign: 'middle',
      margin: 0,
      objectName: `ovl_sankey_num_${c.num}`,
    });
  });

  // ----------------------------------------------------
  // 右: 見るところ
  // ----------------------------------------------------
  L.paneHead(s, 9.95, 1.62, 2.88, '見るところ');

  // 3つの箱(L.box C.tint、各 h1.35、間隔0.12)
  const scSpec = SK.revenues.find(r => r.name.startsWith('スペシャリティー'));
  const scSpecYoy = scSpec ? scSpec.yoy.toFixed(0) : '32';
  const gm31 = (SK.gross.value / SK.total.value * 100).toFixed(1);

  const boxData = [
    {
      num: '1',
      y: 1.98,
      text: `売上総利益 +${SK.gross.yoy.toFixed(0)}%。\n売上(+${SK.total.yoy.toFixed(0)}%)より速い。\n粗利率 ${F('fy26.gross_margin')} → ${gm31}%\n(高付加価値品の比率の上昇)`,
    },
    {
      num: '2',
      y: 1.98 + 1.35 + 0.12, // 3.45
      text: `販管費は +${SK.sga.yoy.toFixed(0)}% に抑える。\n売上の伸びの半分以下で、\n固定費を吸収する`,
    },
    {
      num: '3',
      y: 3.45 + 1.35 + 0.12, // 4.92
      text: `営業利益 +${SK.op.yoy.toFixed(0)}%。\n営業利益率 ${F('fy26.opm')} → ${F('calc.fy26_opm31')}。\nSCの売上が +${scSpecYoy}% と最も伸びる`,
    },
  ];

  boxData.forEach(b => {
    // 背景の箱
    L.box(s, 9.95, b.y, 2.88, 1.35, {
      fill: C.tint,
      line: C.tint,
      round: true,
      name: `box_focus_${b.num}`,
    });

    // 左上の番号の丸
    s.addShape('ellipse', {
      x: 10.08,
      y: b.y + 0.12,
      w: 0.28,
      h: 0.28,
      fill: { color: C.primary },
      line: { color: C.primary },
      objectName: `ovl_box_circle_${b.num}`,
    });
    s.addText(b.num, {
      x: 10.08,
      y: b.y + 0.12,
      w: 0.28,
      h: 0.28,
      fontFace: 'Meiryo UI',
      fontSize: 10,
      bold: true,
      color: C.white,
      align: 'center',
      valign: 'middle',
      margin: 0,
      objectName: `ovl_box_num_${b.num}`,
    });

    // 箱の中の文
    L.text(s, b.text, {
      x: 10.42,
      y: b.y + 0.10,
      w: 2.33,
      h: 1.18,
      fontSize: 9,
      color: C.text,
      valign: 'top',
      margin: 0,
      objectName: `box_text_${b.num}`,
    });
  });

  // 一番下 x9.95 y6.3 w2.88: L.text 8.5pt '現在(26/3期)の流れとの差は、緑と赤の比較の数字で読む'
  L.text(s, '現在(26/3期)の流れとの差は、\n緑と赤の比較の数字で読む', {
    x: 9.95,
    y: 6.35,
    w: 2.88,
    h: 0.38,
    fontSize: 8.5,
    color: C.sub,
    valign: 'middle',
    margin: 0,
    objectName: 'sankey_bottom_note',
  });
};
