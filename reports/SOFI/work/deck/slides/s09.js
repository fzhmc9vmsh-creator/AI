// 損益フロー(サンキー、Q3 2026)。図は assets/make_sankey.py が assets/data/f19_sankey_*.csv から作る(画像: assets/sankey_q3_2026.png)
module.exports = function build(pres, L) {
  const { C } = L;
  const s = L.contentSlide(pres, {
    kicker: '損益フロー(サンキー)、Q3 2026(2026 年 7〜9 月)、百万ドル。( )は前年同期比。GAAP 基準',
    source: '会社の Q3 2026 決算(8-K・説明会)の要約、research_r5/Q3_datasheet.md §1。税引前・税・運営一般管理・その他は推定',
  });
  s.addImage({ path: 'assets/sankey_q3_2026.png', x: 0.5, y: 1.6, w: 8.4, h: 5.0 });
  L.text(s, '税引前・税・運営一般管理は、純利益と税率 22% から逆算した推定(8-K の内訳は未取得)', {
    x: 0.5, y: 6.62, w: 8.4, h: 0.22, fontSize: 8, color: C.sub, objectName: 'note',
  });
  L.takeaway(s, 9.05, 1.7, 3.78, 1.45, '販促費 +55% は売上 +44% より\n速く伸びたが、純利益は +73%。\n増収の源泉は NII(+59%)');
  L.bullets(s, [
    '総純収益の 67% は NII(利ざや)',
    '手数料型の収益 5.71 億ドル(42%)は非 GAAP で、\n非金利収益(4.56 億)と定義が違う',
    '調整後 EBITDA 4.70 億ドル(率 34%)',
  ], { x: 9.05, y: 3.3, w: 3.78, h: 3.3, fontSize: 10.5 });
  return s;
};
