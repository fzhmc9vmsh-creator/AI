// 2-2 業界の地図: 上流(計算資源)→ 自社 → 販路 → 顧客の流れ
module.exports = function build(pres, L) {
  const { F } = L;
  const s = L.contentSlide(pres, {
    kicker: '左 → 右: 計算資源 → Anthropic(モデル開発)→ 販路 → 企業。①〜③ は右の「仕組み」と対応',
    source: 'S-1/A-3、AWS Marketplace の料率',
  });
  L.flowMap(s, {
    name: 's05', h: 4.3, cols: [1.25, 1.35, 1.55, 1.35], rows: 3, nodeH: 0.92,
    lanes: [{ label: '上流', c0: 0, c1: 0 }, { label: '自社', c0: 1, c1: 1, self: true }, { label: '販路', c0: 2, c1: 2 }, { label: '顧客', c0: 3, c1: 3 }],
    nodes: [
      { id: 'cmp', c: 0, r: 0.5, h: 1.2, label: '計算資源', sub: 'NVIDIA\nGoogle TPU\nAWS Trainium' },
      { id: 'ant', c: 1, r: 0.5, h: 1.2, kind: 'self', label: 'Anthropic', sub: 'モデル開発\n実質の粗利率 ' + F('gm.real') },
      { id: 'csp', c: 2, r: 0, kind: 'risk', label: 'クラウド事業者', sub: 'AWS・Google Cloud\nAzure\n手数料 実効 34.8%' },
      { id: 'dir', c: 2, r: 1, kind: 'ok', label: '直販', sub: '売上の 56%\n手数料なし' },
      { id: 'ent', c: 3, r: 0.5, h: 1.2, label: '企業', sub: '年 10 万ドル以上の\n11,900 社が\n売上の 74%\n業務の自動化・\nソフト開発' },
      { id: 'cmpt', c: 1, r: 2, kind: 'ext', label: '競合', sub: 'OpenAI 27%\nGoogle 21%\n(法人 API シェア)' },
    ],
    edges: [
      { from: 'ant', to: 'cmp', label: '支払い', kind: 'money', n: 1 },
      { from: 'ant', to: 'csp', label: 'モデル提供', kind: 'goods', n: 2 },
      { from: 'ant', to: 'dir', label: 'モデル提供', kind: 'goods', n: 3 },
      { from: 'csp', to: 'ent', label: '利用', kind: 'goods' },
      { from: 'dir', to: 'ent', label: '利用', kind: 'goods' },
    ],
  });
  L.mechPanel(s, {
    bottom: 6.0, mechH: 2.3,
    mech: [
      '計算資源へ支払う。上流(計算資源)と販路(クラウド事業者)に大手 3 社ずつが並び、その間で価値を取り合う',
      'クラウド事業者経由は売上の ' + F('csp.share') + '。手数料で利益が削られる',
      '直販は手数料が無い',
    ],
    reason: '利益が残るかは、直販の比率と、利用単価(トークンあたり)の下落の速さで決まる',
    up: '直販の比率が上がる',
    down: '手数料の高止まりと利用単価の下落',
  });
  L.termNotes(s, [
    { term: 'CSP', plain: 'AWS・Google Cloud・Azureなどのクラウド事業者', why: '売上の44%がCSP経由で、手数料が利益を削るため' },
    { term: 'トークン', plain: 'AIが文章を処理する単位(単語の断片)', why: '利用単価(1トークンあたりの値段)の下落がリスクの1位のため' },
  ], { x: 0.5, y: 6.3, w: 12.33 });
  return s;
};
