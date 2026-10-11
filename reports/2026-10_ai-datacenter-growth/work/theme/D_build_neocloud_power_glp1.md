# テーマ調査メモ D群(D1〜D4):建設/電気工事・ネオクラウド・電力半導体/800V HVDC・GLP-1供給網

- 作成日: 2026-10-11
- 作成者: アナリスト補佐(判断材料の収集に徹する。投資判断・推奨は行わない)
- 調査手段: WebSearch のみ(WebFetch/curl は遮断)。検索結果の「要約テキスト」を根拠にしており、**原文ページ本体は開いていない**。
- **重要な制約(調査の打ち切り)**: 本セッションの WebSearch 上限(1ターン200回、全エージェント共有)に到達し、D4 の後半(経口GLP-1が注射デバイスに与える影響、価格下落、Lilly の増産計画)と、日本株の補完調査(D2/D3/D4)を実施できていない。**未取得の項目は「未取得」と明記**し、訓練知識で補った箇所は「訓練知識・未検証」を付している。
- 表記ルール:
  - 本文中の `[D1-3]` のような記号は、各テーマ末尾の「出所一覧」(URL・公表日・種別)に対応する。
  - 種別: **一次**=会社PR/SEC/適時開示、**二次**=報道・決算要約、**低**=ブログ・個人投稿・出所不明。
  - 検索要約どうしで数字が食い違う場合は併記し、「食い違い」と注記した。
  - 「(算出)」は補佐が出所の数値から計算した値。出所そのものの数値ではない。
  - 為替換算は行っていない(通貨は出所のまま)。

---

# D1. データセンター・電力設備の建設/電気工事/専門施工

## D1-1. 需要の強烈さの証拠

### 米国(2026年6月末=Q2 の決算)

| 社名 | 受注残(Backlog/RPO) | 伸び | 備考 | 出所 |
|---|---|---|---|---|
| Comfort Systems USA (FIX) | 140.6億ドル(2026-06-30、過去最高)。前四半期末124.5億ドル、前年同期81.2億ドル | 前年比+73%(算出でも一致)。既存店ベースの受注残は137.0億ドル(+69%) | 売上のうちテクノロジー(データセンター・半導体等)が上期売上の58%(前年同期40%)。粗利率25.9%(前年23.5%)。Q2 EPS 12.53ドル(+92%)。会社は「データセンター需要に減速なし」と述べたと要約されている。設備投資は売上の約5%(モジュール工場の増設中心)。 | [D1-1][D1-2][D1-3][D1-4] |
| EMCOR (EME) | RPO 171.4億ドル(2026-06-30、過去最高)。前年同期119.1億ドル | +43.9% | 通期売上高予想を200〜205億ドルに引き上げ(従前185〜192.5億ドル)。受注残の伸びが大きい分野はネットワーク・通信(データセンター含む)、上下水道、公共施設、医療。Q2売上51.5億ドル(+19.8%)という数字が別の要約にある(出所は二次)。 | [D1-5][D1-6] |
| Quanta Services (PWR) | 受注残534億ドル(うちRPO 336億ドル)(2026-06-30、過去最高) | 前年比は未取得 | Q2売上95.6億ドル(+41%)、調整後EPS 4.24ドル(予想3.29ドル)。通期ガイダンスを全項目で引き上げ。**電力会社向け送配電・再エネが主体で、データセンター比率は未取得**。 | [D1-7] |
| Sterling Infrastructure (STRL) | 受注残43.3億ドル(+116%)、コンバインド(未確定を含む)56.2億ドル(+150%)(2026-06-30) | +116%/+150% | E-Infrastructure 受注残の92%が「ミッションクリティカル」(データセンター、製造、半導体工場)。 | [D1-8] |
| IES Holdings (IESC) | 受注残 約45億ドル(2026-06-30、会社発表の過去最高)。**+91%は「FY2025末比」であり前年同期比ではない**。RPOは28億ドル。 | 同左 | 受注残に基本合意書(LOI)段階の案件を含むとの分析あり。Communications(データセンター)売上4.531億ドル(+51%)。総売上12.43億ドル(+40%)、希薄化後EPS 7.57ドル。住宅部門は売上-6%・営業利益-51%。2026-08-21付で2対1の株式分割。 | [D1-9][D1-10] |
| MYR Group (MYRG) | 受注残31.6億ドル(2026-06-30、過去最高)。前年同期26.4億ドル | +19.6% | 内訳 送配電12.7億ドル、商業・産業(C&I)18.9億ドル。売上10.8億ドル(+20%)。C&I売上5.577億ドル(+41.5%)、送配電売上5.24億ドル(+3.5%)。フリーキャッシュフローは-2,559万ドル(前年+1,164万ドル)。7月1日に Valley Electric と Comet Electric の買収を完了。 | [D1-11][D1-12] |
| Primoris (PRIM) | 受注残139億ドル(うち包括保守契約(MSA)82億ドル、過去最高) | 未取得 | **Q2売上16.9億ドル(-10.7%)、純損失(再エネ案件の問題)**。データセンター比率は未取得。反例・参考として掲載。 | [D1-8]の検索要約内。個別URLは検索結果に出ていないため要再確認 |

### 日本(適時開示・決算要約)

| 社名 | 数字 | 出所 |
|---|---|---|
| 関電工(1942) | 2026年3月期 売上高7,420億円(+10.4%)、営業利益831億円(+42.5%)、純利益635億円(+49.9%)。決算発表 2026-04-28。増益要因は「AI・半導体関連の工場建設と都心再開発」(分析記事の説明)。**受注残・データセンター受注額は未取得**。 | [D1-13][D1-14] |
| きんでん(1944) | 2026年3月期 売上高7,507億円(+6.5%)、経常利益944.9億円(+46.4%)。2027年3月期 会社予想 売上8,100億円(+7.9%)、経常利益960億円(+1.6%)。2027年3月期Q1(発表2026-07-29)売上1,623億円(+14.8%)。2026-01-30に通期予想を上方修正(第3四半期累計の売上・利益は過去最高)。**受注残は未取得**。 | [D1-15][D1-16][D1-17] |
| 高砂熱学工業(1969) | 2026年3月期 売上高4,239億円(+11.1%)、経常利益506億円(+44.8%)、受注高4,600億円(+10.6%)、いずれも過去最高。要因は半導体・データセンター投資(生成AI等)。 | [D1-18] |
| ダイダン(1980) | 2026年3月期 売上高2,562億円(-2.5%)だが、採算改善で過去最高益、受注工事高も過去最高、期末繰越高は大幅増。決算説明は2026-05-13。 | [D1-18] |
| 三機工業(1961) | 2026年3月期 売上高2,547億円(+0.6%)。受注の過去最高は確認できず。 | [D1-18] |
| 新日本空調(1952) | 2027年3月期Q1 受注工事高575億円台(-6.7%)、繰越工事高1,707億円台(データセンター・半導体案件が積み上がっていると説明)。 | [D1-19](企業とURLの対応は検索要約に基づく。要再確認) |
| 九電工(1959) | **今回の調査では決算数値を取得できず(未取得)**。投資情報サイトが「西日本のデータセンター分野でシェアが高い」と紹介(二次)。 | [D1-20] |

### 人手・施工能力(律速要因)の証拠

- 電気工事は、データセンター建設費の45〜70%を占めるとIBEW(米国電気労働組合)が述べたと要約されている。ブルッキングス研究所の Darrell West 氏は、電気工事士不足を「データセンター建設の主要な障壁」としている。[D1-21]
- 4大ハイパースケーラー(Amazon、Microsoft、Alphabet、Meta)の2026年AIインフラ計画は約7,250億ドルで、2025年(約4,100億ドル)から約77%増。Financial Times の数字を二次ブログ経由で引用したもので、**原典未確認**。同じ要約に、Microsoft の Brad Smith 氏が2026年3月に「電気工事士不足が米国のデータセンター拡張を遅らせる最大の問題」と述べたとあるが、これも**二次ブログの記述**。[D1-22]
- 供給側の制約: 米労働統計局(BLS)の見通しでは電気工事士の欠員は年約8.1万人で、多くは退職によるもの。徒弟制度は4〜5年かかるため、今採用した人が有資格者になるのは約2031年。McKinsey は2023〜2030年にAI需要のため追加で約13万人の訓練済み電気工事士が必要としている。ただしこれらは範囲の異なる推計で、同一の数字ではない。[D1-21][D1-22]
- テキサス州では、データセンターが住宅建設会社から電気工事士を引き抜き、住宅の工期が約2か月延びたと報じられている。[D1-23]
- **リードタイム、価格改定(値上げ)、顧客の前払い・長期契約の具体数値は今回未取得**。参考値として FIX の粗利率が前年比+2.4ポイント(25.9% 対 23.5%)に上がっていることが、価格決定力の間接的な指標になりうる(算出、因果は断定できない)。[D1-3]

## D1-2. 途上性

- **市場規模**: データセンター建設・電気工事そのものの「現在値と2030年見通し」は**未取得**。代替指標として、(a) 4大ハイパースケーラーの2026年設備投資計画 約7,250億ドル(二次、原典未確認)[D1-22]、(b) 日本の電気工事業の完成工事高 2024年度 約11兆9,623億円(データセンターが需要を牽引と整理)[D1-24]、のみ。
- **S字カーブの位置(事実の整理)**: 受注残の前年比が+44%(EME)〜+150%(STRL コンバインド)で加速中、FIX は前期末比でも+13%(124.5億→140.6億ドル、算出)。需要側は「減速なし」と述べる会社が多い一方、成長率の頭打ちを示す証拠は今回の調査範囲では見つかっていない。MYRG は受注残の伸びが+19.6%と相対的に低い。
- **供給能力の増設計画**:
  - FIX: 設備投資を売上の約5%(モジュール工場中心)。顧客のコミットメントに連動して増強し、投機的には増やさないと要約されている。[D1-3][D1-4]
  - IESC: データセンター向けの施工チームを増員・訓練し、生産能力を追加中。[D1-9]
  - MYRG: Valley Electric と Comet Electric を買収(2026-07-01)し、C&I 能力を強化。[D1-11]
  - 人手: 新人の有資格者化は約2031年まで見込めない(上記)ため、人手による制約の解消時期は**2030年前後以降**とみられる(補佐の推論。出所は BLS の徒弟期間)。

## D1-3. 投資家の認知度

| 銘柄 | 2026年年初来 | 過去1年 | 予想PER(12か月先) | 予想EPS成長率・PEG | アナリスト | 出所 |
|---|---|---|---|---|---|---|
| FIX | +73.1%、+79.5%、+77.4%、+80.5%、+81%(記事ごとに日付が異なり食い違い) | 未取得 | 29.9倍、31.8倍、35.1〜35.3倍、約37倍、42.7倍(Yahoo、2026年6月中旬)。2026年初は約42.5倍と報じられた | 通期EPS成長率は未取得(Q2単体は+92%)。PEGは算出不能 | Benzinga(2026-09-11): 8人が買い、平均目標1,974ドル、終値1,690.82ドル。valueinvesting.io: 14人(強い買い7・買い5・保有2)、平均目標約2,100ドル、株価約1,877.61ドル(日付不明)。UBSが2026-07-27に目標を2,125→2,225ドル、DA Davidsonが2026-08-21に買い・2,100ドルで新規カバー | [D1-25][D1-26][D1-27][D1-28][D1-29] |
| EME | +32.3%(上記と同じZacks比較記事、日付不明) | 未取得 | 23.7〜23.9倍 | Zacks予想 2026年EPS 27.41ドル(+8.6%)。**この数字は決算前の可能性があり、受注残の伸びとの整合が疑わしい**。PEG≒2.8(算出、参考値) | Zacksランク #3(保有) | [D1-25][D1-26] |
| PWR | +56.6% | 未取得 | 37.4倍、41.1倍 | Zacks予想 2026年EPS 12.38ドル(+16.9%)。PEG≒2.2〜2.4(算出、参考値) | Zacksランク #3 | [D1-25][D1-26] |
| STRL | +68.7%、または+115.8%(日付違い) | 未取得 | 21.8倍、22.4倍 | 未取得 | 未取得 | [D1-27][D1-30] |
| IESC / MYRG / PRIM | 未取得 | 未取得 | 未取得 | 未取得 | 未取得 | — |

- **テーマETF**: 今回の検索では確認できず(未取得)。訓練知識では、インフラETF(PAVE 等)や送電網ETF(GRID 等)にこれらの銘柄が組み入れられていたが、**訓練知識・未検証**。
- **報道での扱い**: Zacks や Nasdaq 掲載記事は、FIX を「最もバリュエーションが高い」、STRL を「成長が速いがハイパースケーラー設備投資への集中リスク」、EME を「最も割安で分散」と整理(二次)[D1-27]。Webull は PWR を「受注残急増後の割高な評価」と報じた[D1-31]。**「バブル」を名指しする記事は今回の検索範囲では確認できなかった**(検索要約の結論)。Simply Wall St のユーザー投稿には「データセンター不況と人手不足が案件パイプラインを侵食する」という弱気シナリオがある[D1-32]。

## D1-4. 代表銘柄(日本または米国に本籍かつ主上場)

| 銘柄 | コード | 時価総額 | 直近売上成長率(YoY) | 純度(テーマが売上に占める割合の目安) | 予想PER | 出所 |
|---|---|---|---|---|---|---|
| Comfort Systems USA | NYSE: FIX | 未取得。参考: 終値1,690.82ドル(2026-09-11)。株数は訓練知識の約3,500万株とすると約600億ドル(**訓練知識・未検証**) | Q2売上 約32.6億ドル。粗利÷粗利率からの逆算で前年約21.7億ドル、約+50%(算出)。既存店売上+44% | 高。テクノロジー部門が上期売上の58%(データセンターを含む広い定義) | 約30〜43倍(上記) | [D1-2][D1-3][D1-25] |
| EMCOR Group | NYSE: EME | 未取得 | Q2売上51.5億ドル(+19.8%、二次) | 中。ネットワーク・通信が受注残の伸びを牽引。**比率は未取得** | 約23.8倍 | [D1-5][D1-6][D1-25] |
| Quanta Services | NYSE: PWR | 未取得 | Q2売上95.6億ドル(+41%) | 低〜中。電力インフラが主体。**比率は未取得** | 約37〜41倍 | [D1-7][D1-25] |
| Sterling Infrastructure | NASDAQ: STRL | 未取得 | 未取得(受注残+116%) | 中〜高。E-Infrastructure受注残の92%がミッションクリティカル(データセンター、製造、半導体)。全社比率は未取得 | 約22倍 | [D1-8][D1-27] |
| IES Holdings | NASDAQ: IESC | 未取得 | FQ3売上12.43億ドル(+40%) | 中。Communications売上÷総売上=約36%(算出)。住宅等は非データセンター | 未取得 | [D1-9][D1-10] |
| MYR Group | NASDAQ: MYRG | 未取得 | Q2売上10.8億ドル(+20%) | 低〜中。C&I売上÷総売上=約52%(算出)だがC&Iは非データセンターを含む | 未取得 | [D1-11] |
| Primoris | NASDAQ: PRIM | 未取得 | Q2売上-10.7% | 低。データセンター比率は未取得。減収・赤字の対照例 | 未取得 | [D1-8]の検索要約内 |
| 関電工 | 1942 | 未取得 | 2026年3月期 +10.4% | 中(推定)。DC比率は未取得 | 未取得 | [D1-13] |
| きんでん | 1944 | 未取得 | 2026年3月期 +6.5%(2027年3月期Q1 +14.8%) | 中(推定)。DC比率は未取得 | 未取得 | [D1-15][D1-16] |
| 九電工 | 1959 | 未取得 | 未取得 | 未取得 | 未取得 | [D1-20] |
| 高砂熱学工業 | 1969 | 未取得 | 2026年3月期 +11.1% | 中(半導体・DC向け空調。比率は未取得) | 未取得 | [D1-18] |
| ダイダン | 1980 | 未取得 | 2026年3月期 -2.5% | 未取得 | 未取得 | [D1-18] |
| 三機工業 | 1961 | 未取得 | 2026年3月期 +0.6% | 未取得 | 未取得 | [D1-18] |
| 新日本空調 | 1952 | 未取得 | Q1受注 -6.7% | 未取得 | 未取得 | [D1-19] |

**参考(ゲート外=他国本籍)**: 今回は調査していない(未取得)。

## D1-5. 弱気材料

1. **ハイパースケーラー設備投資への集中**: STRL は「ハイパースケーラーの設備投資が縮小すれば FIX や Vertiv より打撃が大きい」「第3四半期の受注は時期のずれで弱くなる可能性」と指摘されている(二次、Zacks 系)。[D1-30]
2. **公的な反対と州のモラトリアム**: FIX のQ2要約が「データセンターへの住民反対と、特にニューヨーク州での州単位の一時停止の可能性」を逆風として挙げている。[D1-1]
3. **バリュエーション**: FIX は2026年初に約42.5倍で、わずかな悪材料でも崩れやすいと指摘。[D1-27]
4. **コスト増・関税**: 人件費・資材費の上昇と2026年の関税が利益率を圧迫し、データセンター拡大を冷やしうると指摘。[D1-27]
5. **受注残の質**: IESC の受注残はLOI段階を含む(確定度が低い案件が混在)。IESC の住宅部門は営業利益-51%。[D1-9][D1-10]
6. **キャッシュフロー**: MYRG のフリーキャッシュフローは-2,559万ドル(前年+1,164万ドル)。[D1-12]
7. **顧客資金の源泉の悪化**: D2 のネオクラウドの資金調達不安(2026年7月の株価急落、CoreWeave の債券利回り10.3%)は、データセンター建設の資金源に波及しうる(補佐の指摘。因果は未検証)。
8. **日本の個別差**: ダイダンは減収(-2.5%)、三機工業は横ばい、新日本空調のQ1受注は-6.7%、きんでんの2027年3月期経常利益予想は+1.6%にとどまる(会社予想は保守的な可能性もあり、判断は上位者へ)。[D1-15][D1-18][D1-19]
9. **弱気シナリオ(投稿)**: 「データセンター不況と人手不足が案件パイプラインを侵食」(Simply Wall St ナラティブ、個人投稿=低)。[D1-32]

## D1 出所一覧

| ID | URL | 公表日 | 種別 |
|---|---|---|---|
| D1-1 | https://www.nasdaq.com/articles/comfort-systems-usa-q2-earnings-call-highlights | 2026-07-24頃 | 二次 |
| D1-2 | https://www.businesswire.com/news/home/20260723227439/en | 2026-07-23 | 一次(会社PR) |
| D1-3 | https://www.marketbeat.com/instant-alerts/comfort-systems-usa-q2-earnings-call-highlights-2026-07-24/ | 2026-07-24 | 二次 |
| D1-4 | https://www.nasdaq.com/articles/fix-q2-earnings-call-highlights-data-center-demand-and-capacity | 2026-07下旬 | 二次 |
| D1-5 | https://emcorgroup.gcs-web.com/news-releases/news-release-details/emcor-group-inc-reports-second-quarter-2026-results/ ; https://www.sec.gov/Archives/edgar/data/0000105634/000010563426000112/eme-ex991_2026630xq2.htm | 2026-07-30〜31頃 | 一次 |
| D1-6 | https://www.marketbeat.com/instant-alerts/emcor-group-q2-earnings-call-highlights-2026-07-31/ ; https://www.nasdaq.com/articles/eme-q2-earnings-beat-estimates-broad-based-growth-stock | 2026-07-31頃 | 二次 |
| D1-7 | https://www.tikr.com/blog/quanta-services-just-reported-a-53-billion-backlog-the-electricity-supercycle-is-barely-getting-started ; https://www.nasdaq.com/articles/quanta-services-q2-earnings-call-highlights ; https://www.marketbeat.com/instant-alerts/quanta-services-q2-earnings-call-highlights-2026-07-31/ | 2026-07-30〜31 | 二次(+決算PR PDFが検索結果に存在) |
| D1-8 | https://www.sec.gov/Archives/edgar/data/0000874238/000087423826000100/a20260803ex991earningsrele.htm | 2026-08-03頃 | 一次(STRL)。Primoris分は個別URLなし |
| D1-9 | https://investors.ies-corporate.com/node/19476 | 2026-08上旬 | 一次 |
| D1-10 | https://www.panabee.com/news/ies-earnings-q3-2026 ; https://247wallst.com/cards/ies-holdings-inc-q3-2026-earnings-iesc-01kyw0cnvczfxhzbc4f87anz0b | 2026-08上旬 | 二次 |
| D1-11 | https://www.barchart.com/story/news/3534493/myr-group-inc-announces-second-quarter-and-first-half-2026-results | 2026-07-29 | 一次(PR転載) |
| D1-12 | https://www.chartmill.com/news/external/102513/myr-group-q2-earnings-beat-estimates-backlog-hits-record | 2026-07-29〜30 | 二次 |
| D1-13 | https://scouter.monex.co.jp/news/detail/1942_20260428_act_20260428_130005_2 | 2026-04-28 | 二次 |
| D1-14 | https://www.gyokaidigest.com/companies/kandenko/report/2026-FY | 2026-04以降 | 二次 |
| D1-15 | https://www2.jpx.co.jp/disc/19440/081220260420506537_tse-acedjpsm-19440-20260427319440-ixbrl.htm | 2026-04-27 | 一次(決算短信) |
| D1-16 | https://www2.jpx.co.jp/disc/19440/081220260728501118_tse-qcedjpsm-19440-20260729319440-ixbrl.htm | 2026-07-29 | 一次(Q1決算短信) |
| D1-17 | https://dempa-digital.com/?p=706791 | 2026-01-30 | 二次 |
| D1-18 | https://finance.logmi.jp/articles/384521 ほか(https://assets.finboard.net/tdnet-filings/20260212557973.pdf、https://the-shashi.com/rankings/facility-contractor/ 等) | 2026-05頃 | 二次(各社URLの個別対応は要再確認) |
| D1-19 | https://pdf.irpocket.com/C1952/xoA3/ieAo/Bawv/eoUE.pdf | 2026-07〜08頃 | 一次(想定) |
| D1-20 | https://www.asset-alive.com/thema/thema.php?tid=2223 | 不明 | 低 |
| D1-21 | https://fortune.com/2026/03/02/ai-data-centers-electrician-shortage-gen-z-training-careers/ | 2026-03-02 | 二次 |
| D1-22 | https://www.globaldatacenterhub.com/p/what-725-billion-cannot-buy-and-why ; https://www.thinkbrg.com/thinkset/the-data-center-labor-shortage-a-hidden-bottleneck-for-ai-infrastructure/ | 2026 | 低〜二次 |
| D1-23 | https://explorer.hub71.com/news/feed/data-centers-poach-electricians-from-texas-homebuilders-delaying-construction-by-two-months | 2026 | 二次 |
| D1-24 | https://www.crex-data.com/industry/construction/electrical-construction | 不明 | 二次 |
| D1-25 | https://www.nasdaq.com/articles/emcor-vs-quanta-which-construction-stock-has-more-upside-2026 ; https://www.nasdaq.com/articles/comfort-systems-vs-quanta-which-infrastructure-stock-buy-now ; https://www.nasdaq.com/articles/can-comfort-systems-81-electrical-growth-keep-outpacing-mechanical ; https://finance.yahoo.com/quote/FIX/?p=FIX | 2026年(日付はまちまち) | 二次(Zacks系) |
| D1-26 | https://www.tradingview.com/news/zacks:811b867d4094b:0-is-comfort-systems-stock-a-buy-after-wall-street-raises-estimates/ | 2026 | 二次 |
| D1-27 | https://www.barchart.com/story/news/3972766/forget-chips-these-3-stocks-are-building-the-ai-data-center-boom ; https://247wallst.com/investing/2026/09/02/the-ai-boom-isnt-just-about-chips-these-3-overlooked-stocks-keep-data-centers-running/ ; https://www.chartmill.com/news/external/72282/comfort-systems-stock-surges-81-ytd-buy-hold-or-take-profits | 2026-09-02 ほか | 二次 |
| D1-28 | https://www.benzinga.com/quote/FIX/analyst-ratings | 2026-09-11時点 | 二次 |
| D1-29 | https://valueinvesting.io/FIX/estimates | 不明 | 二次 |
| D1-30 | https://www.nasdaq.com/articles/how-long-can-sterling-rely-e-infrastructure-visibility | 2026 | 二次(Zacks) |
| D1-31 | https://www.webull.com/news/15325439088862208 | 2026-07〜08 | 二次 |
| D1-32 | https://www.simplywall.st/narratives/td5v6g5r-data-center-slump-and-labor-scarcity-will-erode-project-pipelines | 不明 | 低 |

---

# D2. AIネオクラウド/GPUクラウド・推論インフラ(ビットコインマイナーのAI転換を含む)

## D2-1. 需要の強烈さの証拠

| 社名 | 受注残・契約済み | 売上・成長 | 供給・価格・その他 | 出所 |
|---|---|---|---|---|
| CoreWeave (CRWV) | 売上バックログ **1,042億ドル**(2026-06-30、前年比+246%)。四半期終了後に追加された新規コミットメント250億ドル超は含まない。定義は「残存履行義務+コミット契約に基づく将来売上見込み(施設提供能力に依存)」 | Q2売上25.8億ドル(+112%、前四半期比+24%)。通期売上予想124〜132億ドル。Q3予想34.5〜36億ドル。年末の年換算売上ランレート予想185〜195億ドル | 稼働電力 約1.5GW、契約済み 約3.7GW。「近い将来の供給能力は事実上売り切れ」と経営陣が述べた。通期設備投資予想350〜390億ドル(従前310〜350億ドル)、Q2設備投資94億ドル。純損失6.26億ドル、支払利息6.4億ドル(Q3は8.6〜9.4億ドルの予想)。今後の投資は追加の債務・株式調達が必要と経営陣が示唆 | [D2-1][D2-2][D2-3][D2-4] |
| Nebius (NBIS) | 契約電力の年末目標を **5GW** に引き上げ(従前4GW超)。ほぼ全てが今後2〜3.5年で稼働予定 | Q2売上 5.823億ドル(+454%)。別の投稿では5.75億ドル・+514%(**食い違い**)。ARR 約30億ドル(Q1は19.2億ドル)。通期売上予想30〜34億ドル、年末ARR 70〜90億ドル、調整後EBITDA率 約40%、設備投資200〜250億ドル | 稼働電力は2026年末に0.8〜1GWの見通し。新規契約の年間契約額は1MWあたり2,000万〜2,500万ドル(既存の2026年容量は約1,200万ドル)。GAAP継続事業純損失1.904億ドル | [D2-5][D2-6][D2-7] |
| IREN | 2026年容量の契約済みARR **40億ドル**(うち稼働中は10億ドル、残りは年末までに稼働見込み)。2026年末のAIクラウド売上目標は40億ドル超(従前37億ドル、約85%が契約済み)。7月に28億ドルの新規契約 | FY26(2026年6月期)AIクラウド売上1.288億ドル(約8倍)。Q4 AIクラウド売上7,050万ドル(前四半期比+100%超)、Q4総売上1.372億ドル、調整後EBITDA 1,920万ドル(予想を約53%下回る。別の記事では68%減) | 2026年のAI容量はほぼ完売、2027年分は協議の後期。直近の3年契約は1MWあたり2,000万ドル超、2,500万ドルを協議中。FY26純損失7.026億ドル(うち約6.388億ドルが主にビットコイン採掘機器の減損)。決算発表後に株価-12.5% | [D2-8][D2-9][D2-10] |
| Hut 8 | AI契約の総容量949MW(Beacon Point 704MW+River Bend 245MW)、基本契約期間の総額 **266億ドル**。Beacon Point(テキサス州、1GW)に2本目の15年リースを締結し、キャンパス全体で基本契約額が **196億ドル**(見出しでは2本目のリースが98億ドル) | 売上は未取得 | 借り手は投資適格のテナント(社名は要約に記載なし) | [D2-11][D2-12] |
| TeraWulf (WULF) | Anthropic と20年・約190億ドルのリース(401MW)。管理下パイプライン2.1GW | Q2売上4,477万ドル(HPCリース収益が約71%) | Lake Mariner は収益化済み102MW、建設中336MW。Anthropic 向けデータセンターのため35億ドルの調達を計画。建設費は1MWあたり8,000万〜1億ドル説と800万〜1,000万ドル説が併存(**単位の誤りの疑い、要確認**) | [D2-13][D2-14] |
| Core Scientific (CORZ) | 契約済み顧客電力 約1.1GW、潜在契約売上240億ドル超。AMDとの提携で最大2.5GWの賃貸可能容量 | Q2売上1.642億ドル(コロケーション1.367億ドル=約83%、算出)。請求対象 437MW | CoreWeave による買収に関する記述(「破産したマイナーを取得」)が検索要約にあったが、**事実関係が不明確なため採用しない** | [D2-15] |
| Cipher Mining (CIFR) | AWS 300MW・15年・約55億ドル、Fluidstack(Google保証付き)168MW・10年・約30億ドル、合計85億ドル超(2025年の契約)。Fluidstack への引き渡しは2026年9月予定 | **Q2 2026決算は未取得** | — | [D2-16][D2-17] |
| Applied Digital (APLD) | CoreWeave と2本の15年リースで250MW・約70億ドル。追加150MWのオプションを CoreWeave が行使し、合計 約110億ドル | FQ3(2026-02-28終了)売上1.2664億ドル、純損失1.0086億ドル。**FQ4 2026は未取得** | 2026-04-01の改定で親会社保証と5,000万ドルの信用状を追加 | [D2-18][D2-19] |

**GPUレンタル価格(需給の指標)**
- H100の1年契約価格指数(SemiAnalysis)は、2025年10月の1.70ドル/GPU時から2026年3月の2.35ドルへ約+40%。オンデマンドは売り切れで契約価格が上昇。[D2-20]
- 一方、スポット・オンデマンドのH100は1GPU時あたり約2〜4ドル(ネオクラウド)、ハイパースケーラーは約7〜12ドル。CloudZero の2026年8月の確認では、Blackwell出荷後は価格が低下傾向。B200のネオクラウド価格系列は薄い(Spheron: 約4.90ドル、インド)。[D2-20][D2-21]
- **食い違い**: 契約価格は上昇、スポットは低下傾向、と方向が割れている。Spheron のH100価格はページごとに異なる(PCIe 2.01ドル、SXM5 3.94ドル、別記事 2.64ドル)。ベンダー公表値が多く信頼度は低い。

## D2-2. 途上性

- **市場規模の現在値と2030年見通し**(定義が異なるため直接比較不可):
  - Synergy Research: ネオクラウド全体の売上は2030年に約1,800億ドル(年平均+69%)。2025年は230億ドル超の見込み。ネオクラウドの定義が広く、OpenAI のチャットボット購読を含む。[D2-22]
  - ABI Research(GPUaaSのみ): 2030年に約2,500億ドル(2025年420億ドルから年平均+43%)。**同社の2025年7月時点の予測は2030年に650億ドル超**で、大幅に上方修正されている。2030年の推論比率は80%、北米比率は2026年88%→2030年72%。[D2-23][D2-24]
  - Gartner(2026-06-26): ネオクラウドがAIクラウド市場(2030年に2,670億ドル)の20%を獲得。20%を掛けると約530億ドル(算出、Gartner自身の数字ではない)。[D2-25]
  - 3社の2030年予測は530億〜2,500億ドルと**約5倍の開きがある**。
- **S字カーブ**: 売上成長率は+112%(CoreWeave)〜+454%(Nebius)と非常に高く、初期の急拡大局面。ただし GAAP では赤字が拡大し、成長のために調達に依存。
- **供給能力の増設計画・不足解消の時期**: CoreWeave 稼働1.5GW→契約3.7GW、Nebius 契約5GW(2〜3.5年で稼働)、Hut 8 949MW、Core Scientific 約1.1GW、TeraWulf パイプライン2.1GW。**不足がいつ解消するか**(供給過剰に転じる時期を含む)の見通しは今回未取得。IREN は2026年分が完売、2027年分を協議中。[D2-1][D2-5][D2-8][D2-11][D2-13][D2-15]

## D2-3. 投資家の認知度

| 銘柄 | 株価動向 | 時価総額 | 予想PER・EPS成長・PEG | アナリスト | 出所 |
|---|---|---|---|---|---|
| CoreWeave | Q2決算後に最大+14〜18%(時間外)。2026年6月はOpenAI資金調達懸念の局面で約95.74ドル。IPO後の高値186ドルから**-61%超**(2026-07-25時点の記事)。2026-09-22に一時+16%の報道。**年初来は未取得** | 未取得 | 赤字のためPER・PEGは算出不能。予想EV/売上 約7倍、EV/EBITDA 約12倍(Seeking Alpha、2026年9月) | 32人で「中程度の買い」とする記事。目標平均 138.90ドル。Rothschild Redburn は売り・目標54ドルで新規カバー、Rosenblatt は買い・250ドル、Cantor は176ドル、BofA は買い・100ドルでカバー再開 | [D2-26][D2-27][D2-28][D2-29] |
| Nebius | 年初来**+158%**(Parameter.io、株価約215ドル。日付不明)。2026年高値から-37.3%(2026-07-25時点) | 692億ドル(Benzinga、2026-08-16)→493億ドル(同、2026-09-02)。別記事は約550億ドル | 予想売上倍率 約5.6倍(Seeking Alpha)。赤字でPER・PEG算出不能 | Benzinga(2026-09-02): 9人、目標**175〜410ドル**、平均264.18ドル。Morgan Stanley は保有・144ドル | [D2-30][D2-31][D2-32] |
| IREN | 2026年高値から-47%(2026-07-25時点)。決算後-12.5% | 未取得 | 赤字。「ウォール街は損失しか見ていない」と報じられた | 未取得 | [D2-27][D2-9] |
| その他(Cipher、TeraWulf、Hut 8、Core Scientific、Applied Digital) | 未取得(Hut 8 と IREN の契約発表で株価が二桁上昇した報道あり、2026年7月) | 未取得 | 未取得 | 未取得 | [D2-11] |

- **テーマETF**: 今回は未取得。
- **報道の扱い**: 2026年7月に CoreWeave、Nebius、IREN の株価が急落(原因として、サーバー・メモリ・チップ価格の上昇が設備投資を押し上げ追加調達が必要になること、SpaceX や Meta との競争が挙げられた)[D2-27]。Root Capital の Substack は2027〜2028年の信用逼迫シナリオを提示[D2-28]。**主要機関による明示的な「バブル」警告は今回の検索範囲では確認できなかった**。

## D2-4. 代表銘柄

**本籍が米国で主上場も米国(ゲート内)**

| 銘柄 | ティッカー | 時価総額 | 直近売上成長率 | 純度 | 予想PER | 出所 |
|---|---|---|---|---|---|---|
| CoreWeave | NASDAQ: CRWV | 未取得 | Q2 +112% | 高(AIクラウド専業) | 赤字で算出不能 | [D2-1] |
| Hut 8 | NASDAQ: HUT | 未取得 | 未取得 | 中(AIリースへ転換中。ビットコイン採掘も残る) | 算出不能の見込み(赤字なら) | [D2-11][D2-12] |
| Cipher Mining | NASDAQ: CIFR | 未取得 | 未取得 | 中〜高(AIリースが主、採掘も残る) | 未取得 | [D2-16][D2-17] |
| TeraWulf | NASDAQ: WULF | 未取得 | Q2売上4,477万ドル(前年比は未取得) | HPCリース売上が71% | 未取得 | [D2-13][D2-14] |
| Core Scientific | NASDAQ: CORZ | 未取得 | 未取得 | コロケーション売上が約83%(算出) | 未取得 | [D2-15] |
| Applied Digital | NASDAQ: APLD | 未取得 | 未取得 | 高(CoreWeave向けHPCホスティング) | 未取得 | [D2-18][D2-19] |

- 本籍(デラウェア州等)は訓練知識に基づく推定で、**訓練知識・未検証**。Hut 8 は2024年の合併後に米国本社(フロリダ州)に移ったと認識しているが未検証。
- **日本のGPUクラウド**: さくらインターネット(3778)、ハイレゾ(3993)、GMOインターネット(9449)などが候補だが、**今回は調査できていない(未取得)**。

**参考(ゲート外=他国本籍またはADR)**

| 銘柄 | ティッカー | 本籍 | 備考 | 出所 |
|---|---|---|---|---|
| Nebius Group | NASDAQ: NBIS | オランダ(社名の N.V. から。訓練知識で補強、未検証) | 上記の数字参照 | [D2-5][D2-30] |
| IREN | NASDAQ: IREN | オーストラリア(**訓練知識・未検証、本籍の確認が必要**) | 上記の数字参照 | [D2-8] |
| Lambda、Fluidstack、Crusoe、Nscale | 非上場 | — | Fluidstack は Cipher の借り手(Google が保証)として登場 | [D2-17] |

## D2-5. 弱気材料

1. **資金調達・レバレッジ**:
   - CoreWeave の総負債は2026-06-30時点で350億ドル(Capacity Global)。別の記事は250億ドル超(Invezz、2026年7月)。**集計方法の違いの可能性、要確認**。2026〜2028年に満期が集中する「借り換えの壁」と指摘。[D2-27][D2-33]
   - 2032年債の利回りは10.32%、S&PのB格(投機的水準)。2025年12月にCDSスプレッドが1週間で368→643bpに拡大したと報じられた。[D2-27]
   - 30億ドルの転換社債の計画は希薄化とキャッシュの懸念材料。負債資本比率は約522%。[D2-26]
   - Q3の支払利息は8.6〜9.4億ドルの予想(Q2は6.4億ドル)。[D2-2]
2. **顧客集中・サプライヤー依存**: NVIDIAの供給への依存と顧客集中を指摘する記事。IREN の借り手は Microsoft、Nvidia、Perplexity、Figure AI 等だが、Applied Digital は CoreWeave 依存を収益性のリスクとして指摘されている。[D2-26][D2-19][D2-8]
3. **コスト上昇**: サーバー・メモリ・チップ価格の上昇が設備投資を押し上げる。[D2-27]
4. **スポット価格の低下**: Blackwell出荷後のH100価格低下(CloudZero)。契約価格は上昇しており方向が割れる。[D2-20][D2-21]
5. **収益性**: IREN はQ4の調整後EBITDAが予想を53%下回り、FY26純損失7.0億ドル。Nebius はGAAPで赤字、CoreWeave は純損失6.26億ドル。[D2-2][D2-5][D2-8]
6. **需要側のイベントリスク**: 2026年6月に OpenAI の資金調達懸念で CoreWeave 株が下落した(約95.74ドル)。[D2-26]
7. **競合**: SpaceX や Meta との競争が指摘された。[D2-27]
8. **市場規模予測のばらつき**: 2030年の見通しが530億〜2,500億ドルと約5倍開く(上記)。

## D2 出所一覧

| ID | URL | 公表日 | 種別 |
|---|---|---|---|
| D2-1 | https://www.marketbeat.com/instant-alerts/coreweave-q2-earnings-call-highlights-2026-08-11/ ; https://quartr.com/events/coreweave-inc-crwv-q2-2026_F6huCJA4 | 2026-08-11 | 二次 |
| D2-2 | https://pulse2.com/coreweave-revenue-backlog-reaches-104-billion-before-another-25-billion-of-new-commitments/ ; https://dashboard.channelchek.com/?p=104902 ; https://beancount.io/blog/2026/09/22/coreweave-fy2026-q2-earnings-analysis | 2026-08〜09 | 二次(Substack の longyield は設備投資64億ドルとするが整合せず不採用) |
| D2-3 | https://longyield.substack.com/p/coreweave-books-104-billion-it-also | 2026-08 | 低(参考のみ) |
| D2-4 | https://www.indmoney.com/blog/us-stocks/crwv-stock-jumps-coreweave-q2-earnings-analysis | 2026-08 | 二次 |
| D2-5 | https://quartr.com/events/nebius-group-n-v-nbis-q2-2026_ozKEzQzr ; https://theenergymag.com/news/market-news/nebius-group-reports-454-revenue-growth-in-q2-2026-raises-power-guidance-to-5-gw | 2026-08-12頃 | 二次 |
| D2-6 | https://discussion.fool.com/t/my-nebius-q2-2026-notes/125967 | 2026-08 | 低(個人投稿) |
| D2-7 | https://www.marketbeat.com/instant-alerts/nebius-group-q2-earnings-call-highlights-2026-08-12/ | 2026-08-12 | 二次 |
| D2-8 | https://iren.gcs-web.com/news-releases/news-release-details/iren-reports-fy26-results | 2026-08-27 | 一次 |
| D2-9 | https://www.kucoin.com/news/flash/iren-q4-fy2026-revenue-meets-expectations-ai-cloud-revenue-doubles ; https://ground.news/article/iren-reports-fy26-results | 2026-08 | 二次 |
| D2-10 | https://pulse2.com/iren-contracted-arr-reaches-4-billion-as-ai-cloud-revenue-jumps-nearly-eightfold/ | 2026-08 | 二次 |
| D2-11 | https://theblock.co/post/408920/hut-8-fully-commercializes-1-gw-texas-ai-campus-with-second-9-8b-lease-as-iren-signs-2-8b-in-contracts-shares-climb-double-digits | 2026-07 | 二次 |
| D2-12 | https://forklog.com/en/hut-8-leases-ai-capacity-for-9-8-billion/ ; https://whale-alert.io/stories/99d00110a11cda/IREN-raises-AI-cloud-revenue-target-above-4B-on-28B-in-new-multi-year-contracts | 2026-07 | 二次 |
| D2-13 | https://www.marketbeat.com/instant-alerts/terawulf-q2-earnings-call-highlights-2026-08-05/ ; https://blockspace.media/insight/terawulf-anthropic-lease-q2-revenue-2026/ | 2026-08-05 | 二次 |
| D2-14 | https://tangem.com/en/news/investments/35988-terawulf-q2-hpc-revenue-surges-19b-anthropic-deal/ | 2026-08 | 二次 |
| D2-15 | https://stocks.observer-reporter.com/observerreporter/article/bizwire-2026-7-28-core-scientific-announces-second-quarter-2026-results | 2026-07-28 | 一次(PR転載) |
| D2-16 | https://www.datacenterdynamics.com/en/news/aws-signs-300mw-hosting-deal-to-lease-capacity-from-cipher-mining/ | 2025年(契約発表時) | 二次 |
| D2-17 | https://www.theblock.co/post/379722/cipher-mining-full-site-fluidstack-lease-raise-333-million-texas-expansion ; https://simplywall.st/stocks/us/software/nasdaq-cifr/cipher-mining/news/cipher-mining-cifr-is-down-111-after-75-billion-ai-pivot-wit | 2025年 | 二次 |
| D2-18 | https://www.nasdaq.com/articles/apld-boosts-hyperscale-growth-with-250mw-ai-data-center-lease | 2025〜2026 | 二次 |
| D2-19 | https://www.cnhinews.com/news/article_405b940d-0024-5f7c-bd29-bde41465e187.html ; https://www.nasdaq.com/articles/crwv-vs-apld-which-ai-data-center-stock-has-more-upside-potential | 2026 | 二次 |
| D2-20 | https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity | 2026-03頃 | 二次(専門調査) |
| D2-21 | https://cloudzero.com/blog/h100-gpu-cost/ ; https://www.spheron.network/blog/nvidia-h100-price-2026/ ; https://www.spheron.network/blog/h100-price-per-hour-2026/ | 2026-08 | 低(ベンダー) |
| D2-22 | https://srgresearch.com/articles/neoclouds-currently-growing-by-over-200-per-year-will-reach-180-billion-in-revenues-by-2030 | 2025〜2026 | 二次 |
| D2-23 | https://abiresearch.com/blog/neocloud-market-trends | 2026 | 二次 |
| D2-24 | https://www.abiresearch.com/news-resources/chart-data/gpu-as-a-service-revenue-for-neoclouds ; https://aapnews.aap.com.au/news/cision20250722AE34004 | 2026/2025-07-22(旧予測650億ドル超) | 二次 |
| D2-25 | https://www.intelligentcio.com/north-america/2026/06/26/gartner-predicts-neocloud-vendors-will-capture-20-of-the-ai-cloud-market-by-2030/ | 2026-06-26 | 二次 |
| D2-26 | https://letsdatascience.com/news/coreweave-reports-large-backlog-amid-elevated-debt-costs-28a8d777 ; https://finance.yahoo.com/markets/stocks/articles/coreweave-raised-20-billion-capital-144406639.html ; https://www.simplywall.st/stocks/us/software/nasdaq-crwv/coreweave/future | 2026 | 二次 |
| D2-27 | https://invezz.com/ie/news/2026/07/25/why-are-nvidia-backed-coreweave-nebius-and-iren-stocks-plunging/ | 2026-07-25 | 二次 |
| D2-28 | https://rootcapital.substack.com/p/coreweave-is-undervalued | 2026 | 低(個人投稿) |
| D2-29 | https://www.marketbeat.com/instant-alerts/price-coreweave-nasdaq-crwv-trading-up-16-time-to-buy-2026-09-22/ ; https://seekingalpha.com/article/4936102 | 2026-09-22 | 二次 |
| D2-30 | https://www.benzinga.com/quote/NBIS/report | 2026-08-16 / 2026-09-02 | 二次 |
| D2-31 | https://parameter.io/should-you-buy-nebius-nbis-stock-after-its-recent-16-decline/ | 日付不明 | 低 |
| D2-32 | https://www.itiger.com/news/1108115233 | 2026 | 低 |
| D2-33 | https://capacityglobal.com/news/coreweaves-debt-hits-35bn/ | 2026-08 | 二次 |

---

# D3. 電力半導体と800V HVDC データセンター電源、電源ユニット・電源管理IC

## D3-1. 需要の強烈さの証拠

**前提**: 800V HVDCは「いま売上が立つ」のではなく**2027年以降に立ち上がる**段階。現在の業績の押し上げは、従来構成(54V・SiC AC-DC電源・電源管理IC・配電機器)のAIサーバー向け需要が主体である。

| 社名 | 数字 | 800V関連の時期 | 出所 |
|---|---|---|---|
| Monolithic Power Systems (MPWR) | Q2売上9.806億ドル(+47.6%、前四半期比+21.9%)。Enterprise Data(データセンター)3.806億ドル(**+164.3%**、売上の38.8%、Q1は32.7%)。Q3予想 中央値11.5億ドル(アナリスト予想9.868億ドルを大幅に上回る)。調整後EPS 6.50ドル(予想5.88ドル)。決算後株価+10.5% | 800V向け高電圧AC-DC製品のサンプル出荷を開始。生産能力目標を「60億ドル超」に拡大。(通期Enterprise Data成長見通しを85%→130%に引き上げたとの記述は**二次のみで未確認**) | [D3-1][D3-2][D3-3] |
| Vertiv (VRT) | Q2売上32.74億ドル(+24%、うち有機+18%、買収+5%、為替+1%)。希薄化後EPS+53%、調整後EPS+60%。通期売上予想は中央値約140億ドル、有機成長+31%(ともに引き上げ)。**バックログは2025年Q4時点で150億ドル(前年比+109%)、受注/売上比2.9倍**。2025年Q4決算から四半期ごとの受注・バックログ開示を取りやめた(変動の印象を減らすため)ため、**最新のバックログは未取得** | 未取得 | [D3-4][D3-5][D3-6] |
| Eaton (ETN) | 電力(Electrical)Americas: 直近12か月平均受注+41%、受注/売上比1.3、バックログ+33%。電力部門全体のバックログ+43%。Americas売上は有機+18%で過去最高の40億ドル、営業利益率27.5%。データセンター売上は約+65%。2026年の有機成長見通しを11〜13%、調整後EPS 13.40〜13.60ドルに引き上げ(2026-07-31)。(「307GWの米データセンターバックログ」という数字はWebullのみで未確認) | 未取得 | [D3-7][D3-8] |
| Vicor (VICR) | 受注残3.8億ドル(前四半期比+26%、前年同期比+145%)。Q2製品・ロイヤルティ売上1.434億ドル+新ライセンス契約のロイヤルティ売上1,500万ドル。純利益4,980万ドル。Q3は約+10%成長、通期売上6億ドル超の見通し。25億ドルの売上目標の達成には第2の半導体工場が必要。決算後は「年初来の急騰」を背景に株価が下落(2026-07-21) | 縦型電力供給(VPD)をAIデータセンター向けに訴求。48V/800V別の数字は未取得 | [D3-9][D3-10] |
| Navitas (NVTS) | Q2売上1,050万ドル(前四半期比+22%だが**前年同期の1,450万ドルから約-28%**、算出)。非GAAP粗利率39.5%。Q3予想1,350万ドル(±50万ドル)。通期は前年比で個位数%成長、Q4は二桁成長。AIインフラ(データセンター+送配電・エネルギー)は年末までに売上の3分の1超を見込む。モバイル・低価格コンシューマ事業は縮小中 | NVIDIAと800V HVDC(2025-05-21発表)で協業。800V対応のGaN/SiC生産サンプルを出荷中。ハイパースケーラー・XPU向けの量産は**2027年**。800V DC出力のパワー・サイドカーは2027年から含有額が増え、ネイティブ800V DC構成はその後 | [D3-11][D3-12][D3-13] |
| Wolfspeed (WOLF) | FQ4 2026(2026-08-19発表)売上約1.5億ドル(前年同期1.97億ドルから-24%)、うち電力部門約1.06億ドル。AIデータセンター売上はFY26に2倍超、Q4は前四半期比約+20%。調整後粗利率-19.9%、EBITDA -6,200万ドル。FQ1予想1.4〜1.6億ドル(粗利率はマイナス継続) | 800V化でSiC使用量が増えると説明。Lite-On、Magmeet等の電源メーカーで設計採用 | [D3-14][D3-15] |
| Power Integrations (POWI) | Q2売上1.189億ドル(会社ガイダンス1.15〜1.2億ドルの範囲内) | **主電力経路(800V→GPU)の売上が実質的に立つのは2028年以降**。補助電源は2028年から。2,200V GaNは実証段階 | [D3-16] |
| onsemi (ON) | Q2売上16億ドル(前年比+9%、前四半期比+6%)。AIデータセンター売上は2025年比で**2倍超**の見通し(売上内訳での個別開示はなし) | 未取得 | [D3-17] |
| Advanced Energy (AEIS) | Q2売上5.741億ドル(+30%)。データセンター・コンピューティング売上1.92億ドル(+35%)、通期成長見通しを「+50%以上」に引き上げ。Q3予想6.4億ドル(±2,000万ドル)、EPS 3.00ドル(±0.25ドル)。タイ工場は第4四半期に生産売上開始、完成時の売上生産能力は約50億ドル | **800V製品の初期売上は2027年後半、本格量産は2028年** | [D3-18][D3-19] |
| 三菱電機(6503) | 2026年度(2027年3月期)目標 売上6兆2,000億円、調整後営業利益5,900億円(9.5%)。データセンター向けでは液冷関連が2030年度目標(1,000億円超)の半分弱。データセンター800V電源のシェア見通しはIR Day 2026で質疑があったが詳細未取得 | 未取得 | [D3-20][D3-21] |
| ローム(6963) | 2026年3月期は本業の営業利益108億円の黒字だが、SiC関連の減損で最終損益は**1,584億円の赤字**。2026年度は増収増益・黒字転換の計画で、AIサーバー向けは2.5倍、SiCデバイス/モジュールは+55%以上。NVIDIAと800V電力供給アーキテクチャの開発で協業と発表 | 協業発表済み(時期の詳細は未取得) | [D3-22] |
| 富士電機(6504) | **今回は2026年度の業績・データセンター向け情報を取得できず(未取得)** | 未取得 | [D3-22] |

**800V HVDC普及・関連機器市場の予測(定義が異なり直接比較不可)**
- Citi: 新設データセンター容量に占める800VDCの採用率は2027年16.0%→**2030年79.1%**。固体変圧器(SST)需要は2027年901MVA→2030年37,152MVA(容量ベースで売上ではない)。[D3-23]
- Goldman Sachs の Brian Lee 氏: Nvidiaのロードマップでは最初の導入は早ければ2028年。NVIDIAの800V HVDCへの移行は2027年に始まる(12V/48V構成の置き換え)。[D3-23]
- SST市場の売上予測: MarketsandMarkets(米国のデータセンター向け)は2025年4,030万ドル→2030年1.54億ドル(年平均+30.8%)。Astute Analytics(世界)は2025年約2.507億ドル→2035年約65億ドル(2026〜2035年平均+38.5%)。中国の証券会社は世界SSTの年平均+25〜35%(5〜10年)。[D3-24][D3-25]
- **予測の差は約40倍**(米国のみ対世界、年次も異なる)。Citiは最も強気な採用率予測で、調査会社の売上予測は保守的かつ非同質。

## D3-2. 途上性

- **現在値と2030年見通し**: 800V HVDCそのものの市場規模(ドル)は単一の信頼できる数字を**未取得**。採用率は Citi 16%(2027)→79%(2030)。SST売上予測は上記のとおりバラつく。
- **S字カーブ**: 800V対応の売上計上時期は、Navitas・MPWR 2027年、AEIS 2027年後半〜2028年、POWI 2028年以降、Goldman 2028年。**売上は2027〜2028年から**で、現時点は立ち上がり前。足元の増収は従来構成のAIサーバー向け(MPWR +164%、onsemi 2倍超、Wolfspeed 2倍超)。
- **供給能力の増設計画**: MPWR 生産能力目標60億ドル超、AEIS タイ工場(完成時に約50億ドルの生産能力)、Vicor 第2工場(25億ドルの売上目標達成に必要)。[D3-1][D3-18][D3-9]
- **不足解消の時期**: 未取得。

## D3-3. 投資家の認知度

- **株価の年初来・過去1年、予想PER、予想EPS成長率、PEG、アナリストのカバー数、テーマETF**: **今回の検索では取得できていない(未取得)**。以下は断片情報のみ。
  - Vicor: 決算後、「年初来の急騰」を背景に株価が下落(2026-07-21)。[D3-10]
  - MPWR: Q2決算後に株価+10.5%。[D3-3]
  - IREN などと異なり、このテーマに特化した「過熱」「バブル」報道は未確認。
  - 電源(PSU)・SSTを「千億円規模の市場」とする中国系報道がある(見出しのみ)。[D3-25]

## D3-4. 代表銘柄

**本籍が米国で主上場も米国(ゲート内)**

| 銘柄 | ティッカー | 時価総額 | 直近売上成長率(YoY) | 純度(目安) | 予想PER | 出所 |
|---|---|---|---|---|---|---|
| Vertiv | NYSE: VRT | 未取得 | Q2 +24%(有機+18%) | 売上の大半がデータセンター向けと認識しているが**未取得(訓練知識・未検証)** | 未取得 | [D3-4] |
| Monolithic Power Systems | NASDAQ: MPWR | 未取得 | Q2 +47.6% | Enterprise Data=売上の38.8% | 未取得 | [D3-1] |
| Vicor | NASDAQ: VICR | 未取得 | 未取得(受注残+145%) | AI比率は未取得 | 未取得 | [D3-9] |
| Navitas Semiconductor | NASDAQ: NVTS | 未取得 | Q2 約-28%(算出) | AIインフラ(データセンター+送配電)は年末に売上の1/3超の見込み(現状は1/3未満とみられる=推論) | 赤字のため算出不能 | [D3-11] |
| Wolfspeed | NYSE: WOLF | 未取得 | FQ4 -24% | AIデータセンター比率は未取得 | 赤字のため算出不能 | [D3-14] |
| Power Integrations | NASDAQ: POWI | 未取得 | 未取得 | 低(主電力経路は2028年以降) | 未取得 | [D3-16] |
| onsemi | NASDAQ: ON | 未取得 | Q2 +9% | 低(AI売上は個別開示なし) | 未取得 | [D3-17] |
| Advanced Energy | NASDAQ: AEIS | 未取得 | Q2 +30% | データセンター・コンピューティング÷総売上=約33%(算出) | 未取得 | [D3-18] |
| 三菱電機 | 6503 | 未取得 | 未取得 | 低(総合電機。DC向け液冷等が一部) | 未取得 | [D3-20][D3-21] |
| ローム | 6963 | 未取得 | 未取得(2026年3月期は純損失1,584億円) | 低〜中(AIサーバー向け2.5倍の計画だが全体比率は未取得) | 未取得 | [D3-22] |

**参考(ゲート外=他国本籍)**

| 銘柄 | 備考 |
|---|---|
| Eaton (ETN、アイルランド本籍=社名の plc から) | 上記の数字参照。米国上場だが本籍は米国外 [D3-7] |
| Infineon、STMicroelectronics、Delta Electronics、Lite-On、Schneider Electric、ABB 等 | 今回は調査していない(未取得)。Infineon、STMicro、TI、ADI は同じ領域を競合として狙っているとの記述あり [D3-16] |
| Texas Instruments (TXN、米国本籍) | 競合として言及されるのみ。Q2数字は未取得 [D3-16] |
| 日本: 富士電機(6504)、サンケン電気(6707)、新電元工業(6844)、TDK(6762)、村田製作所(6981)、ニチコン(6996)等 | 候補として列挙するのみ。今回は調査していない(未取得)。**訓練知識・未検証** |

## D3-5. 弱気材料

1. **立ち上がりの遅れ**: 800V関連の本格売上は2028年以降(POWI、AEIS)。NVIDIA計画の遅延があれば売上計上は後ろ倒しになる。2,200V GaNは実証段階。[D3-16][D3-18]
2. **業績の弱さ**: Navitas のQ2売上は前年同期比約-28%、Wolfspeed は売上-24%・粗利率-19.9%、ローム は SiC減損で最終赤字1,584億円。[D3-11][D3-14][D3-22]
3. **需要の変動**: MPWR について、AIサーバー需要や顧客の発注パターンが想定より不安定になるリスクがアナリストから指摘されている。[D3-1]
4. **期待の織り込み**: Vicor は好決算でも「年初来の急騰」の後で株価が下落した。[D3-10]
5. **情報開示の後退**: Vertiv は2025年Q4決算から四半期の受注・バックログ開示を取りやめた。Q2は売上・利益・FCFが中心で、FCFに関する懸念(ainvest)と、四半期間の売上の期ずれ(金額は開示なし)の報道あり。[D3-5][D3-6]
6. **競合**: Infineon、STMicro、TI、ADI が同じ領域を狙う。[D3-16]
7. **業界再編**: ローム・東芝・三菱電機がパワー半導体事業の統合協議(基本合意書、2026-03)。デンソーはロームへの買収提案を取り下げ。事業環境の不確実性を示す(価格・競争環境への影響は未検証)。[D3-22][D3-26]
8. **予測の分散**: SST/800V の市場予測が約40倍開き、採用率予測(Citi 79%)に対し売上予測は小さい。

## D3 出所一覧

| ID | URL | 公表日 | 種別 |
|---|---|---|---|
| D3-1 | https://www.sec.gov/Archives/edgar/data/0001280452/000162828026051029/mpwr-20260630xexx991.htm ; https://www.panabee.com/news/monolithic-power-earnings-q2-2026 | 2026-07-30 | 一次+二次 |
| D3-2 | https://www.monolithicpower.com/media/investor-relations/press-releases/Q2_2026_MPS_Earnings_Commentary_1.pdf | 2026-07-30 | 一次 |
| D3-3 | https://www.barchart.com/story/news/3561533/monolithic-power-systems-nasdaqmpwr-beats-expectations-in-strong-q2-stock-jumps-10-5 | 2026-07-30〜31 | 二次 |
| D3-4 | https://www.sec.gov/Archives/edgar/data/0001674101/000162828026050323/q22026exhibit991vrt07292026.htm ; https://investors.vertiv.com/news/news-details/2026/Vertiv-Reports-Strong-Second-Quarter-2026-with-Diluted-EPS-Growth-of-53-Adjusted-Diluted-EPS-Growth-of-60-Raises-Full-Year-2026-Guidance-Across-All-Key-Metrics/default.aspx | 2026-07-29 | 一次 |
| D3-5 | https://www.marketbeat.com/instant-alerts/vertiv-q4-earnings-call-highlights-2026-02-11/ ; https://www.trefis.com/articles/617134/should-you-think-about-vertiv-differently-now/2026-09-30 | 2026-02-11 / 2026-09-30 | 二次 |
| D3-6 | https://www.ainvest.com/news/vertiv-q2-read-stumble-free-cash-flow-2609/ | 2026-09頃 | 低〜二次 |
| D3-7 | https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000027/etn06302026exhibit99.htm ; https://www.emr-online.com/eaton-eaton-reports-record-second-quarter-2026-results-with-strong-organic-growth-accelerating-orders-and-backlog-and-raises-organic-growth-guidance/ | 2026-07-31頃 | 一次+二次 |
| D3-8 | https://www.marketbeat.com/instant-alerts/eaton-q2-earnings-call-highlights-2026-07-31/ ; https://pulse2.com/eaton-electrical-global-backlog-more-than-doubles-as-orders-rise-33/ | 2026-07-31 | 二次 |
| D3-9 | https://www.sec.gov/Archives/edgar/data/0000751978/000119312526309538/d115827dex991.htm | 2026-07-21 | 一次 |
| D3-10 | https://seekingalpha.com/news/4615968-vicor-tops-q2-estimates-as-ai-demand-drives-backlog-shares-fall-on-outlook ; https://www.marketbeat.com/instant-alerts/vicor-q2-earnings-call-highlights-2026-07-21/ | 2026-07-21 | 二次 |
| D3-11 | https://ir.navitassemi.com/news-releases/news-release-details/navitas-semiconductor-announces-second-quarter-2026-financial | 2026-07-27 | 一次 |
| D3-12 | https://semiconductor-today.com/news_items/2026/jul/navitas-290726.shtml ; https://www.marketbeat.com/instant-alerts/navitas-semiconductor-q2-earnings-call-highlights-2026-07-27/ | 2026-07-27〜29 | 二次 |
| D3-13 | https://ir.navitassemi.com/news-releases/news-release-details/nvidia-selects-navitas-collaborate-next-generation-800-v-hvdc | 2025-05-21 | 一次 |
| D3-14 | https://s29.q4cdn.com/278875087/files/doc_earnings/2026/q4/earnings-result/Wolfspeed_Q4_2026_Earnings_Release.pdf | 2026-08-19 | 一次 |
| D3-15 | https://semiconductor-today.com/news_items/2026/aug/wolfspeed-250826.shtml ; https://www.marketbeat.com/instant-alerts/wolfspeed-q4-earnings-call-highlights-2026-08-19/ | 2026-08-19〜25 | 二次 |
| D3-16 | https://www.marketbeat.com/instant-alerts/power-integrations-q2-earnings-call-highlights-2026-08-05/ ; https://www.nasdaq.com/articles/power-integrations-q2-earnings-call-highlights | 2026-08-05 | 二次 |
| D3-17 | https://www.nasdaq.com/articles/onsemi-q2-earnings-call-highlights ; https://www.remio.ai/post/onsemis-q2-beat-shows-the-ai-power-race-is-accelerating | 2026-07〜08 | 二次 |
| D3-18 | https://www.marketbeat.com/instant-alerts/advanced-energy-industries-q2-earnings-call-highlights-2026-08-03/ ; https://www.chartmill.com/news/external/109552/aeis-q2-earnings-beat-on-semiconductor-and-data-center-strength | 2026-08-03〜04 | 二次 |
| D3-19 | https://www.fool.com/earnings/call-transcripts/2026/08/10/advanced-energy-aeis-q2-2026-earnings-call-transcript/ | 2026-08-10 | 二次 |
| D3-20 | https://www.mitsubishielectric.co.jp/ja/pr/2026/pdf/0529_co7.pdf | 2026-05-29 | 一次 |
| D3-21 | https://monoist.itmedia.co.jp/mn/spv/2604/30/news062_2.html | 2026-04-30 | 二次 |
| D3-22 | https://eetimes.itmedia.co.jp/ee/spv/2605/13/news069_2.html ; https://jioinc.jp/investleaders/?p=13684 | 2026-05-13 | 二次 |
| D3-23 | https://www.thestandard.com.hk/innovation/article/337678/AI-data-center-power-shift-to-800VDC-to-reach-79pc-adoption-by-2030-Citi | 2026 | 二次 |
| D3-24 | https://www.marketsandmarkets.com/Market-Reports/us-data-centers-solid-state-transformers-market-51807964.html | 不明 | 二次(調査会社) |
| D3-25 | https://www.astuteanalytica.com/ko/industry-report/data-center-solid-state-transformer-market ; https://www.itiger.com/hans/news/2645092828 | 不明 | 二次〜低 |
| D3-26 | https://eetimes.itmedia.co.jp/ee/spv/2603/27/news118.html | 2026-03-27 | 二次 |

---

# D4. GLP-1・肥満症治療薬のサプライチェーン(CDMO、注射デバイス、原薬)※比較対照

## D4-1. 需要の強烈さの証拠

**最終需要(川下)**

| 項目 | 数字 | 出所 |
|---|---|---|
| Eli Lilly Q2 2026(2026-08-05発表) | 売上**230億ドル(+48%)**。内訳は数量要因が約+60ポイント、価格が約-13ポイント。Mounjaro 99億ドル(+91%、米国48億ドル+45%、米国外52億ドル+172%、中国の償還リスト入りが寄与)。Zepbound 49億ドル(+46%)。経口剤 orforglipron(ブランド名 Foundayo)は発売初四半期に9,800万ドル。2026年通期売上予想を850〜870億ドルに引き上げ(従前820〜850億ドル)、非GAAP EPS予想は35.50〜36.50ドル。retatrutide の生物学的製剤承認申請(BLA)は2027年Q1の予定 | [D4-1][D4-2][D4-3][D4-4] |
| Lilly のGLP-1/GIP売上の年率換算(算出) | Mounjaro+Zepbound=148億ドル/四半期 → 年率換算 約590億ドル(算出)。2023〜2025年の市場予測(後述)が控えめに見える一因 | 同上(算出) |
| Novo Nordisk 2026年 | 2026年2月に通期の売上・営業利益が-5〜-13%と見通し(「前例のない価格圧力」とCEO)。Q1で上方修正され-4〜-12%(定率為替)と要約されている。米国の現金払い向け価格は経口Wegovyが月149ドル(4月に199ドルへ)、注射剤が月349ドル。経口Wegovyは米国初四半期で22.6億デンマーククローネ(約3.54億ドル)、処方約130万件、アナリスト予想の約2倍。ZEUS試験が2026-07-31に失敗し株価急落。**Q2の実績値は未取得**。別の見出し「Novo Nordisk Raises 2026 Sales and Profit Outlook」(sentisense)が存在するが日付が曖昧(要確認) | [D4-5][D4-6][D4-7][D4-8] |

**サプライチェーン(川中・川上)**

| 社名/項目 | 数字 | 出所 |
|---|---|---|
| ペプチド原薬の逼迫 | 新設の大規模能力まで18〜36か月、熟練ペプチド化学者も不足。Bachem、Lonza、CordenPharma、PolyPeptide が巨額の増強を約束 | [D4-9] |
| CordenPharma(非上場) | 2024年に9億ユーロ(別報道で9.81億ドル)のGLP-1ペプチド投資。複数年契約の総額30億ユーロ(32.6億ドル)。米AmbioPharm(サウスカロライナ州・上海)を買収(**クロージングは未確認**)。スイスMuttenzに5,000L超の新工場 | [D4-10][D4-11][D4-12] |
| Neuland(インド) | 4モジュール計画の第1が稼働(7,000L)。セマグルチド特許の失効(2026年4月)でインドの後発品が急増 | [D4-9] |
| CPC Scientific | カリフォルニア州の原薬工場が2026年末に全面稼働予定 | [D4-9] |
| Bachem(スイス) | H1 2026売上3.264億スイスフラン(+4.3%、現地通貨+7.3%)、EBITDA 8,280万フラン(-9%、マージン25.4%、前年29.1%)。商用API売上は約-20%、成長はH2に偏る。新設の Building K は2026年4月に開所し、GLP-1向けペプチドを生産、初回商用GMP材料を製造。2026年通期は現地通貨で+35〜40%成長(Quartr。3月時点は35〜45%との差異あり=**食い違い**)、EBITDA率は30%台前半、設備投資3.5〜4億フラン。2026年の残りの受注は満杯 | [D4-13][D4-14][D4-15] |
| West Pharmaceutical (WST、注射剤向けエラストマー部材) | Q2 2026売上8.723億ドル(+13.8%、有機+12.7%)。高付加価値(HVP)部材4.241億ドル(+19.4%、売上の49%、有機+18.4%)、GLP-1向けエラストマーの成長が寄与。通期有機成長の見通しを7〜9%→**10〜11%**に引き上げ、売上33.45〜33.8億ドル、調整後EPS 8.85〜9.05ドル。Q3売上8.2〜8.35億ドル。**GLP-1単独の売上は未開示**。2026年5月のサイバー事案が West Vantage 部門に影響(中位の個位数%の売上ブレーキ) | [D4-16][D4-17] |
| 中外製薬(4519) | 2026年12月期上期 売上収益6,633億円(+14.7%)、Core営業利益3,291億円(+21.0%)、通期予想据え置き。**orforglipron のロイヤルティ収入の金額・位置付けは今回の検索で確認できず(未取得)** | [D4-18] |
| 日本の注射デバイス(テルモ、ニプロ等) | **検索で関連情報なし(未取得)** | — |

## D4-2. 途上性

- **市場規模の現在値と2030年見通し**(いずれも2023〜2025年の予測で古い):
  - Goldman Sachs: 2030年の世界の抗肥満薬市場を1,300億ドル→**950億ドル**に下方修正(-27%)。ピークは米国700億ドル、米国外500億ドル。米国の価格が従来想定より速く下がると見る。[D4-19]
  - TD Cowen(2025年2月): 2030年のGLP-1世界売上1,390億ドル。[D4-19]
  - 悲観的モデル(CMC Markets 引用): 2030年に約330億ドル。[D4-20]
  - **2026年版の更新は今回未取得**。Lilly単独の2026年売上予想が850〜870億ドルであり、これらの過去予測は既に現状と乖離している可能性がある(補佐の指摘)。
- **S字カーブ**: Mounjaro米国外+172%、Zepbound+46%、経口剤の発売初期。成長期の途中〜前半とみられるが、価格は下落(Lilly 価格要因-13ポイント、Novo の現金払い価格149〜349ドル)。
- **供給能力の増設**: ペプチド原薬は18〜36か月かかる。CordenPharma、Neuland、CPC Scientific、Bachem(Building K)が2026年に稼働・稼働予定。**Lilly と Novo の自社増設額と不足解消の時期は今回未取得**。

## D4-3. 投資家の認知度

| 銘柄 | 株価動向 | 時価総額 | 予想PER・EPS成長・PEG | アナリスト | 出所 |
|---|---|---|---|---|---|
| Eli Lilly (LLY) | 年初来 **+8.9%**(S&P500は+12.8%、Barchart、2026年8月頃)。4月時点は-7.5%。過去1年は未取得 | 約1.1兆ドル(2026-07-23 Google Finance 約1.11兆ドル) | 予想PER 約31.6倍(Yahoo、2026-06-09)。2026年通期の調整後EPS予想34.71ドル(+43.4%)。**PEG≒0.73**(算出: 31.6÷43.4。EPSは仕掛研究開発費の影響を受けるため参考値) | 29人、コンセンサス「強い買い」。平均目標1,351ドル(高1,600ドル、安1,135ドル、2026年7月) | [D4-21][D4-22] |
| Novo Nordisk (NVO ADR) | 2026年2月の通期見通しで株価-14%(ADR)。ZEUS試験失敗(2026-07-31)で急落 | 未取得 | 未取得 | 未取得 | [D4-6][D4-8] |
| West (WST)、Bachem 等 | 未取得 | 未取得 | 未取得 | 未取得 | — |

- **テーマETF**: 未取得(訓練知識では GLP-1/肥満症テーマETFが存在したが、**訓練知識・未検証**)。
- **報道の扱い**: Barron's が「ウォール街は減量薬への熱狂から後退」(日付は不明)[D4-23]、Goldman は「抗肥満薬市場は想定より小さいかもしれない」と分析[D4-19]。**「バブル」を名指しする2026年の記事は今回未確認**。

## D4-4. 代表銘柄

**本籍が日本または米国で主上場も同国(ゲート内)**

| 銘柄 | コード | 時価総額 | 直近売上成長率(YoY) | 純度(GLP-1が売上に占める割合の目安) | 予想PER | 出所 |
|---|---|---|---|---|---|---|
| Eli Lilly | NYSE: LLY | 約1.1兆ドル | Q2 +48% | 高(Mounjaro+Zepbound=14.8/23.0=約64%、算出)。ただし**川上ではなくメーカー本体** | 約31.6倍 | [D4-1][D4-21] |
| West Pharmaceutical Services | NYSE: WST | 未取得 | Q2 +13.8%(有機+12.7%) | 低〜中。HVP部材は売上の49%だが、GLP-1単独比率は未開示 | 未取得 | [D4-16] |
| 中外製薬 | 4519 | 未取得 | 上期 +14.7% | 低(orforglipron ロイヤルティの比率は未取得) | 未取得 | [D4-18] |
| Becton Dickinson (BDX)、Thermo Fisher (TMO)、Amneal 等 | — | 未調査(未取得) | 未取得 | 未取得 | 未取得 | — |
| テルモ(4543)、ニプロ(8086)、富士フイルム(4901)、AGC(5201)、味の素(2802)、日東電工(6988) | — | 未調査(未取得)。候補として列挙するのみで、GLP-1との関係は**訓練知識・未検証** | 未取得 | 未取得 | 未取得 | — |

**参考(ゲート外=他国本籍またはADR)**

| 銘柄 | 備考 | 出所 |
|---|---|---|
| Novo Nordisk (NVO ADR、デンマーク本籍) | 上記参照 | [D4-5] |
| Bachem (SIX: BANB、スイス) | H1売上+4.3%、通期+35〜40%の見通し | [D4-13] |
| CordenPharma(非上場)、Neuland(インド)、CPC Scientific、Lonza、PolyPeptide、Stevanato、Gerresheimer、Ypsomed、SCHOTT Pharma | 今回は個別調査していない。Neuland と CordenPharma のみ設備投資の記述あり | [D4-9][D4-10] |

## D4-5. 弱気材料

1. **価格の下落**: Lilly の売上成長のうち価格は約-13ポイント。Novo は2026年の売上・営業利益が減少する見通しで、米国の現金払い価格を月149〜349ドルまで下げた。[D4-1][D4-5][D4-6]
2. **競争と特許切れ**: セマグルチドの米国外での特許失効(インドでは2026年4月)が後発品の急増を招く。Novo は競争の激化も要因に挙げる。[D4-5][D4-9]
3. **市場予測の下方修正**: Goldman は2030年予測を-27%に下方修正(米国の価格が速く下がるため)。[D4-19]
4. **供給網側の逆風(個別)**:
   - Bachem はH1の商用API売上が約-20%、EBITDA率が25.4%(前年29.1%)に低下し、Building K の立ち上げコストが重い。H2への偏重で、実現しなければ通期ガイダンス(+35〜40%)の下振れ余地がある(補佐の指摘)。[D4-13][D4-14]
   - West は2026年5月のサイバー事案で West Vantage 部門に打撃。[D4-17]
5. **経口剤シフトの影響(未検証の論点)**: Wegovy錠(経口)は発売初期に好調。経口剤の拡大は注射デバイス需要への逆風になりうる。**これを直接検証する記事は予算超過のため未取得**。また orforglipron は低分子で、ペプチド原薬のCDMO需要を代替しうるとされる論点があるが、**訓練知識・未検証**。
6. **供給能力の同時増設による将来の供給過剰リスク**: CordenPharma、Neuland、CPC Scientific、Bachem、Lonza、PolyPeptide が同時に増設中。能力過剰に至るかは未検証(補佐の推論で、出所は増設計画の併存のみ)。[D4-9][D4-10]
7. **臨床・個別イベント**: Novo の ZEUS 試験が2026-07-31に失敗。[D4-8]
8. **規制・償還**: TrumpRx、Medicare適用拡大などの価格・償還動向は**未取得**(予算超過)。

## D4 出所一覧

| ID | URL | 公表日 | 種別 |
|---|---|---|---|
| D4-1 | https://investor.lilly.com/node/54781 ; https://www.sec.gov/Archives/edgar/data/0000059478/000005947826000077/q226lillysalesandearningsp.htm | 2026-08-05 | 一次 |
| D4-2 | https://www.americanpharmaceuticalreview.com/1315-News/627249-Lilly-Q2-Revenue-Jumps-48-as-Mounjaro-and-Zepbound-Drive-Guidance-Raise/ | 2026-08 | 二次 |
| D4-3 | https://rivkin.com.au/?p=37235 | 2026-08 | 低〜二次 |
| D4-4 | https://www.1stoncology.com/blog/?p=112662 ; https://www.newsquawk.com/headlines/eli-lilly-lly-q2-2026-usd-adj-eps-838-exp-601-revenue-23bln-exp-207bln | 2026-08 | 低〜二次 |
| D4-5 | https://pharmaphorum.com/news/novo-nordisk-slumps-tougher-2026-financial-outlook ; https://www.benefitsandpensionsmonitor.com/news/industry-news/novo-nordisk-learns-the-weight-of-pricing-pressure/393067 | 2026-02 / 2026 | 二次 |
| D4-6 | https://parameter.io/novo-nordisk-nvo-stock-falls-14-as-company-projects-first-sales-drop-since-2017/ | 2026-02 | 低〜二次 |
| D4-7 | https://app.sentisense.ai/stories/novo-nordisk-raises-2026-sales-and-profit-outlook-on-strong-glp-1-sales-08042026 | 日付曖昧(2026-04-08または08-04) | 低 |
| D4-8 | https://www.regardsofwallstreet.com/news/when-does-novo-nordisk-report-earnings-august-5-2026 | 2026-08 | 低〜二次 |
| D4-9 | https://www.chemanalyst.com/NewsAndDeals/NewsDetails/glp-1-capacity-race-heats-up-as-neuland-launches-large-scale-peptide-44620 ; https://www.dcatvci.org/features/cdmo-cmo-expansion-update-riding-the-strength-of-tides | 2026 | 二次 |
| D4-10 | https://www.fiercepharma.com/manufacturing/glp-1-manufacturer-cordenpharma-strikes-deal-peptide-cdmo-lining-new-production-sites | 2026 | 二次 |
| D4-11 | https://www.manufacturingdive.com/news/cordenpharma-to-invest-980-million-us-europe-glp-1-peptides-expansion/722009 | 2024 | 二次 |
| D4-12 | https://www.pharmamanufacturing.com/sector/contract-manufacturing/article/55380076/cordenpharma-buys-ambiopharm-to-boost-its-global-peptide-api-capacity | 2026 | 二次 |
| D4-13 | https://quartr.com/events/bachem-holding-ag-banb-h1-2026_oqPWIwpp ; https://www.vermoegenszentrum.ch/boersen-und-maerkte/news/bachem-uebertrifft-im-ersten-halbjahr-2026-die-erwartungen | 2026-07-30 | 二次 |
| D4-14 | https://www.gurufocus.com/stock/CHIX:BANBZ/transcripts/8996527 | 2026-07-30頃 | 二次 |
| D4-15 | https://www.bachem.com/articles/news/ad-hoc/bachem-reports-strong-sales-growth-and-sustained-high-profitability/ | 2026-03-12 | 一次 |
| D4-16 | https://www.marketbeat.com/instant-alerts/west-pharmaceutical-services-q2-earnings-call-highlights-2026-07-23/ ; https://quartr.com/events/west-pharmaceutical-services-inc-wst-q2-2026_3svcwUXy | 2026-07-23 | 二次 |
| D4-17 | https://www.mychesco.com/?p=674724 | 2026-07 | 二次 |
| D4-18 | https://www2.jpx.co.jp/disc/45190/140120260723598727.pdf ; https://www.gyokaidigest.com/companies/chugai-pharm/report/2026-Q2 | 2026-07-23 | 一次+二次 |
| D4-19 | https://www.goldmansachs.com/insights/articles/the-anti-obesity-drug-market-may-prove-smaller-than-expected | 2025頃(日付は要確認) | 二次 |
| D4-20 | https://www.cmcmarkets.com/en/opto/anti-obesity-drugs-a-100bn-market | 不明 | 二次 |
| D4-21 | https://www.barchart.com/story/news/3686486/eli-lilly-stock-analyst-estimates-ratings ; https://finance.yahoo.com/quote/lly | 2026-08頃 / 2026-06-09 | 二次 |
| D4-22 | https://www.google.com/finance/quote/LLY%3ANYSE ; https://www.barchart.com/story/news/1745234/do-wall-street-analysts-like-eli-lilly-stock | 2026-07-23 / 2026-04頃 | 二次 |
| D4-23 | https://www.itiger.com/hans/news/2526504266 | 日付不明 | 低(Barron's転載) |

---

# 付録A. 調査の限界(上位アナリスト向け)

1. **WebSearch の上限に到達**したため、D4後半と日本株の補完調査は未実施。未取得項目は本文中に「未取得」と記載。
2. **時価総額・年初来・予想PER・PEG・ETF**は、D1(FIX/EME/PWR/STRL)、D2(CRWV/NBIS)、D4(LLY)を除いてほぼ未取得。**スクリーニングの定量比較には別途データ取得が必要**。
3. 検索要約の数値は原文を開いていないため、**表記の揺れ・転記誤りの可能性**がある。特に、(a) 日付が不明確な株価・PER(D1の複数Zacks記事)、(b) 同一指標で食い違う数値(Nebius Q2売上、Bachem のガイダンス範囲、CoreWeave の負債額)、(c) Primoris と関電工等の個別URLの対応、は要再確認。
4. **本籍の判定**(ゲート内/外)のうち、Nebius(オランダ)、IREN(オーストラリア)、Eaton(アイルランド)、米国マイナー各社(デラウェア州等)の一部は訓練知識に基づく推定を含み、未検証。
5. 本メモは判断材料の収集であり、投資判断や推奨を含まない。補佐の推論には「(算出)」「補佐の指摘/推論」と付記した。

# 付録B. 優先して取り直すべき項目(次回調査の提案)

1. D1: 九電工・関電工・きんでんの受注残と手持工事高、データセンター比率。FIX/EME/PWR/STRL/IESC/MYRG の時価総額・年初来・過去1年・予想PER。
2. D2: CoreWeave の年初来・過去1年、Cipher と Applied Digital の最新四半期、さくらインターネット等の日本のGPUクラウド。
3. D3: VRT/MPWR/VICR/NVTS/WOLF の株価動向・予想PER・カバー数。富士電機、サンケン、TDK、村田等の日本企業。Vertiv の最新バックログ(10-Q)。
4. D4: 経口剤が注射デバイスとペプチドCDMOに与える影響の定量分析、価格・償還の動向、Lilly/Novo の自社増設額、Novo のQ2実績、テルモ・ニプロ・富士フイルム・AGC の GLP-1関連売上。
