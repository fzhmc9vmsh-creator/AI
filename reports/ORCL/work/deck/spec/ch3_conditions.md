# 指示書: 第3章 13条件の構造分析(スライド 17〜29)

## 共通ルール(全スライド)
- ファイル: `slides/sNN.js`(NN = スライド番号 2 桁)。`module.exports = function build(pres, L) { ... }` の形で、1 枚だけ作る。
- 見本は `examples.js` の `exT15`。同じ部品だけを使う: `L.contentSlide`、`L.structure`、`L.t15Side`(条件4 だけ `L.kpiTiles`)。
- 座標は部品が決める。ノードの位置は下の表の col(列 0〜3)・row(行 0〜2)をそのまま使う。文字が入らなければ、座標やフォントを変えずに文字を削って私(指示者)に報告する。
- タイトル・キッカー・出所・数値は一字一句このとおり。勝手に言い換えない。
- 矢印の kind: money(カネ、濃緑実線)/ goods(モノ・サービス、ティール実線)/ risk(リスク、赤破線)。ノードの kind: self(Oracle 側、緑塗り)/ ext(外部、白)/ ok(陳腐化しにくい資産・低リスク、薄緑)/ risk(リスクの所在、灰地・赤枠)。
- 確認: `node one.js NN` で 1 枚だけ作り、`python3 audit_deck.py tmp/sNN.pptx` が PASS、`tmp/sNN.jpg` を目で見て重なり・はみ出しがないこと。
- 出所の共通の書き方: 「会社開示」は決算発表・説明会、「需給エンジン第4.3版」は calc/model8.py の結果。

---

## s17 条件1(評価 B)
- title: `DB の切替コストは 10 年以上続くが、AI の単価優位は逼迫期(FY32 まで)に限られ、10 年の圧倒的優位とは言えない`
- kicker: `条件1 10年間の価格決定力・競争優位・成長性を圧倒的水準で維持`
- source: `会社開示(Q1 FY27 説明会)、research4/T5_supply_components.md、research4/T3_saas_products.md、calc/prereg2.md §9`
- page: 17 / grade: 'B' / condNo: 1
- nodes:
  - db: col 0, row 0, `DB・SaaS 顧客`, sub `切替に数年。保守料は継続課金`, kind ext
  - orcl: col 1, row 1, `Oracle`, sub `DB を土台に複数の収益線`, kind self
  - lab: col 3, row 0, `AI 研究所`, sub `容量料。更新は従来比 +20%`, kind ext
  - comp: col 3, row 2, `競合クラウド`, sub `AWS・Azure・GCP・ネオクラウド`, kind risk
  - lease: col 0, row 2, `長期リース`, sub `賃料を FY47 まで固定`, kind ok
- edges:
  - db → orcl, `保守料・購読料`, money
  - lab → orcl, `容量料(逼迫期 +5%/年)`, money
  - comp → orcl, `緩和後の値下げ圧力`, risk
  - orcl → lease, `固定賃料`, money
- tags: db `優位: 数十年`(green)、lab `優位: FY32 まで`(red)
- evidence(4 行):
  - `更新期の GPU をすべて従来契約比 +20% で更新・再販(Q1 FY27)`
  - `2026 年の値上げ: AWS +15〜20%、Nebius +17〜21%`
  - `需給が緩んだ後の長期の超過利益はベースで 0%(逼迫の終わり FY32)`
  - `SaaS +10%・Software −3% は SAP クラウド ERP +25% より遅い`
- reason: `DB の優位は長いが、AI の価格優位は業界全体の逼迫によるもので、緩和後は消えるため B`

## s18 条件2(評価 B)
- examples.js の exT15 をそのまま使う(タイトル・ノード・矢印・根拠・理由は見本どおり)。ただし page は 18、根拠の4行目を `S&P の基本シナリオとコンセンサスは FY29 に FCF 黒字(エンジンは −135 億ドル)` に替える。

## s19 条件3(評価 A)
- title: `DB とネットワークの技術が OCI(+121%)と Database@(+353%)に転用され、増収の主因になった`
- kicker: `条件3 コア技術・データが AI 事業に転用され成果が出始めている`
- source: `会社開示(Q1 FY27)、research3/W6_database_at.md、research3/W8_aws_vs_commodity.md`
- page: 19 / grade: 'A' / condNo: 3
- nodes:
  - tech: col 0, row 1, `DB・Exadata の技術`, sub `RDMA ネットワーク・Autonomous`, kind self
  - oci: col 1, row 0, `OCI`, sub `売上 74 億ドル(+121%)`, kind self
  - dbat: col 1, row 2, `Database@`, sub `他社クラウド内の Oracle DB(+353%)`, kind self
  - lab: col 3, row 0, `AI 研究所`, sub `GPU クラスタを利用`, kind ext
  - hyper: col 3, row 2, `AWS・Azure・GCP`, sub `70 リージョンに配置`, kind ext
- edges:
  - tech → oci, `ネットワーク設計`, goods
  - tech → dbat, `DB をそのまま提供`, goods
  - oci → lab, `計算容量`, goods
  - dbat → hyper, `顧客接点は提携先`, risk
- tags: dbat `追加投資は小さい`(green)
- evidence:
  - `OCI 売上 74 億ドル(+121%、Q1 FY27)`
  - `Database@ +353%、70 リージョン・119 AZ(AWS は 22 リージョン)`
  - `AI 容量の顧客が DB・アプリも買う証拠は見つからない`
- reason: `転用は増収の主因になったが、主因は容量の貸し出しで、DB の転用収益が過半ではないため S でなく A`

## s20 条件4(評価 S)
- title: `NYSE 上場の米国企業で、審査の前提条件を満たす`
- kicker: `条件4 日本株か米国株`
- source: `NYSE 上場銘柄情報`
- page: 20 / grade: 'S' / condNo: 4
- 本文: `L.kpiTiles(s, [...])` で 3 枚: `{value:'NYSE', label:'上場市場', note:'ティッカー ORCL'}`、`{value:'米ドル', label:'取引通貨', note:'米国の普通株'}`、`{value:'充足', label:'判定', note:'ゲート条件。減点要素なし'}`。
- その下に `L.takeaway(s, 0.5, 3.6, 12.33, 0.7, 'ゲート条件のため構造図は不要。評価の集計には S として数える')`

## s21 条件5(評価 B)
- title: `CEO は OCI をゼロから築き容量と受注で実績を出したが、capex は見通しを繰り返し超え、報酬は総売上で決まる`
- kicker: `条件5 CEO が信頼に足り事業拡大の経歴を持つ`
- source: `DEF 14A(報酬)、会社開示(FY26〜27 のガイダンス)、research4/T2_company_rpo_capacity.md`
- page: 21 / grade: 'B' / condNo: 5
- nodes:
  - ceo: col 0, row 1, `共同 CEO`, sub `Magouyrk(OCI 創設者)・Sicilia`, kind self
  - board: col 0, row 0, `報酬委員会`, sub `PSO の KPI = FY28 総売上`, kind ext
  - capex: col 2, row 1, `capex`, sub `FY26 実績 557 億ドル`, kind risk
  - rpo: col 2, row 0, `受注残`, sub `6,640 億ドル`, kind ok
  - sh: col 3, row 2, `株主`, sub `1株価値`, kind ext
- edges:
  - board → ceo, `報酬(80% は時間ベース)`, money
  - ceo → rpo, `容量で受注を確保`, goods
  - ceo → capex, `見通し 350 → 500 → 557 億ドル`, money
  - capex → sh, `総額 KPI と1株価値のずれ`, risk
- evidence:
  - `FY26 capex: 当初見通し 約 350 億 → 2025-12 に約 500 億 → 実績 557 億ドル(最新見通し比 +11%)`
  - `FY27 売上ガイダンスは 85 → 89 → 90 → 90 以上と引き上げ`
  - `PSO の KPI は FY28 の非GAAP 総売上(1株指標ではない)`
  - `FAM の FY27 EPS 目標 10.65 ドルは単一出典で、FactSet の FY28 中央値と同値(年度ずれの可能性)`
- reason: `成長の実行力は高いが、資本配分の規律と報酬の設計に留保が残るため B(C との境界)`

## s22 条件6(評価 B)
- title: `事業実態 EPS の5年成長率は3経路とも 30% を超え PEG は 0.60〜0.66 だが、エンジン経路の余裕は 1.5pt で自社株買いに依存する`
- kicker: `条件6 5年後 EPS 成長率で PEG<1(EPS CAGR 30% 以上)。事業実態 EPS = 非GAAP EPS − 株式報酬の税引後`
- source: `コンセンサス(Yahoo・FactSet・tickflow)、会社の FY30 目標(FAM 2025-10)、需給エンジン第4.3版(calc/out/m8_extra.json)。株価 143.20 ドル`
- page: 22 / grade: 'B' / condNo: 6
- 本文は構造図ではなく表(`L.table`)。x 0.5, y 1.75, w 8.3, colW [2.1, 1.25, 1.25, 1.2, 1.2, 1.3], fontSize 11, rowH 0.42:
  - 見出し: `経路` / `FY27` / `FY32` / `5年 CAGR` / `PER` / `PEG`
  - `コンセンサス` / `6.85` / `29.48` / `33.9%` / `20.9` / `0.62`
  - `会社(FY30 目標 21 ドル)` / `6.89` / `30.20` / `34.4%` / `20.8` / `0.60`
  - `需給エンジン` / `6.89` / `27.14` / `31.5%` / `20.8` / `0.66`
- 表の下に `L.bullets`(x 0.5, y 3.7, w 8.3, h 2.4, fontSize 10.5):
  - `エンジン経路の余裕は 1.5pt。超過 FCF の自社株買いがなければ 30.0%、確率加重の経路では 28.6%`
  - `条件7 が C(安い理由の一部は実在のリスク)のため、規則により S は無効`
  - `FY27→FY30 の3年では全経路が 36% 超。減速は FY30〜32 の容量追加の減速による`
- 右パネル `L.t15Side`: evidence = [`5年 CAGR の閾値 30%: FY32 の事業実態 EPS 25.6 ドル以上`, `PER は 143.20 ÷ FY27 の事業実態 EPS`, `第1版の評価は C(エンジン 22.1%)`], reason = `数値は S の基準を満たすが、余裕が薄く条件7 と対で評価して B`

## s23 条件7(評価 C)
- title: `株価が安い主因は市場の見落としではなく、OpenAI への集中(受注残の約 45%)と CDS 227bp が示す実在の信用リスクである`
- kicker: `条件7 PEG が低い理由がリスクの過大評価であること(MU 型の陳腐化 capex が理由ではない)`
- source: `research2/R5_credit.md、research4/T2_company_rpo_capacity.md、research3/W2_gpu_economic_life.md、Bloomberg(2026-10-08)`
- page: 23 / grade: 'C' / condNo: 7
- nodes:
  - mkt: col 0, row 0, `株式市場`, sub `事業実態 EPS の 15.7 倍`, kind ext
  - orcl: col 1, row 1, `Oracle`, sub `GPU を自社調達`, kind self
  - oai: col 3, row 0, `OpenAI`, sub `受注残の約 45%・約 3,000 億ドル`, kind risk
  - bond: col 0, row 2, `社債・CDS 市場`, sub `CDS 227bp、2056 年債 8% 超`, kind risk
  - nv: col 3, row 2, `NVIDIA`, sub `GPU 代`, kind ext
- edges:
  - oai → orcl, `年 約 300 億ドル(2027〜)`, money
  - orcl → nv, `GPU の購入`, money
  - bond → orcl, `資金(高い金利)`, money
  - oai → orcl, `不払いリスク`, risk, off 0.25
  - orcl → mkt, `現金化への疑い`, risk
- tags: oai `集中リスク: Oracle 負担`(red)
- evidence:
  - `OpenAI の年換算売上 240 億ドル(3 月)→ 約 500 億ドル(10/8、700 億ドル報道を下方修正)`
  - `OpenAI の計算契約は 1.15〜1.5 兆ドル、2026〜30 年の FCF 累計 −2,780 億ドル`
  - `S&P BBB-(2026-07)。FY29 までに FOCF が黒字化しなければ再格下げ`
  - `見落としで説明できるのは GPU 寿命の悲観だけ(H100 を元の 95% で再契約の例)`
- reason: `安さの主因は実在のリスクで、見落としは一部(GPU 寿命・J カーブ)に限られるため C`
- kpi: `CDS 5年 200bp 未満で確度を上げ、300bp 超で D 候補 / FY29 より前の BB+ 格下げで D 候補 / OpenAI の比率 40% 未満で確度を上げ、契約変更・支払遅延の報道で E 候補`

## s24 条件8(評価 C)
- title: `DB は代替の利かない製品だが、価値の 45% を占める AI 容量は、需給が緩むと限界供給者の損益分岐で値が決まる商品になる`
- kicker: `条件8 コモディティではない(AVGO 型でない)`
- source: `需給エンジン第4.3版(セグメント価値)、research3/W3_industry_structure.md、ICE・CME の発表(2026-05)`
- page: 24 / grade: 'C' / condNo: 8
- nodes:
  - db: col 0, row 0, `Oracle DB・Database@`, sub `差別化あり`, kind ok
  - gpu: col 0, row 2, `AI 容量(GPU 時間)`, sub `価値の 45%`, kind risk
  - lab: col 2, row 1, `AI 研究所`, sub `最も安い容量を選ぶ`, kind ext
  - neo: col 3, row 0, `ネオクラウド`, sub `H100 で約 2.6 倍安い`, kind ext
  - fut: col 3, row 2, `計算の先物`, sub `ICE・CME が準備`, kind risk
- edges:
  - db → lab, `データの近くで推論`, goods
  - gpu → lab, `GPU 時間`, goods
  - neo → lab, `代替の容量`, goods
  - fut → gpu, `価格の標準化`, risk
- tags: gpu `緩和後の値下げ: Oracle 負担`(red)、db `代替なし`(green)
- evidence:
  - `セグメント価値(1株): AI 117、ソフト保守 45、SaaS 44、OCI 一般 31`
  - `需給が緩んだ後の超過利益はベース 0%(NVIDIA の取り分、TPU、買い手の集中)`
  - `推論トークンの価格は同等性能で年 9〜900 倍の速さで下落(Epoch)`
- reason: `価値の半分近くが、緩和後に商品化する層にあるため C`
- kpi: `AI 粗利率(最終開示 32%)が 25% 未満で D 候補・35% 以上で B 候補 / 更新プレミアム(+20%)が 0% 以下で D 候補 / H100 1年契約指数(2.65 ドル)が 2.00 ドル未満`

## s25 条件9(評価 B)
- title: `止まれば顧客の AI 事業が止まる電力付きの容量で更新率は高いが、代替のクラウドもあり不可欠とまでは言えない`
- kicker: `条件9 顧客の AI 実装の「停めない運用」に不可欠`
- source: `会社開示(Q4 FY26・Q1 FY27 説明会)、research4/T4_ai_demand.md`
- page: 25 / grade: 'B' / condNo: 9
- nodes:
  - orcl: col 1, row 1, `Oracle OCI`, sub `稼働率 97.9%`, kind self
  - lab: col 3, row 0, `AI 研究所`, sub `学習・推論(本番)`, kind ext
  - ent: col 3, row 2, `企業`, sub `Oracle DB 内のデータで推論`, kind ext
  - power: col 0, row 1, `電力付きの容量`, sub `Q1 FY27 に 850MW 納入`, kind ok
  - alt: col 1, row 2, `代替のクラウド`, sub `乗り換えに数か月〜数年`, kind risk
- edges:
  - power → orcl, `容量`, goods
  - orcl → lab, `計算容量`, goods
  - orcl → ent, `DB と推論`, goods
  - alt → ent, `乗り換えの選択肢`, risk
- evidence:
  - `Q4 FY26 は顧客の 49% が GPU の 92% を更新`
  - `推論の比率(電力): 2025 年 47.5% → 2030 年 60.0%(McKinsey)`
  - `推論は本番稼働で、止まると顧客の売上が止まる`
- reason: `電力付きの容量と DB は止められない運用を支えるが、代替が存在するため B`

## s26 条件10(評価 B)
- title: `DB の技術と顧客関係は長寿命で、GPU の6年償却は更新・再販の実績と整合する。ただし GPU の世代交代は速い`
- kicker: `条件10 無形資産投資も陳腐化リスクを厳格に評価`
- source: `research3/W2_gpu_economic_life.md、会社開示(耐用年数の変更)`
- page: 26 / grade: 'B' / condNo: 10
- nodes:
  - intang: col 0, row 0, `DB 技術・顧客関係`, sub `寿命は数十年`, kind ok
  - gpu: col 0, row 2, `GPU`, sub `6 年償却・上限 10 年`, kind risk
  - orcl: col 1, row 1, `Oracle`, sub `更新・再販で回収`, kind self
  - cust: col 3, row 1, `顧客`, sub `更新 +20%`, kind ext
  - nv: col 3, row 2, `NVIDIA の新世代`, sub `Rubin は電力あたり約 10 倍`, kind risk
- edges:
  - intang → orcl, `保守・SaaS`, money
  - gpu → orcl, `容量`, goods
  - cust → orcl, `更新料`, money
  - nv → gpu, `世代交代`, risk
- evidence:
  - `CoreWeave は H100 を元の価格の 95% で再契約。中古 H100 は新品の 61% → 69%`
  - `Amazon はサーバーの耐用年数を 6 → 5 年に短縮`
  - `3 年耐用なら Oracle の EPS は −17%(JPMorgan AM の試算)`
- reason: `経済的寿命 ≧ 会計の耐用年数を示す証拠が優勢だが、電力制約の下での置き換えリスクが残るため B`

## s27 条件11(評価 B)
- title: `DB の顧客基盤と他社クラウド内の配置は再現が難しいが、AI 容量は資本と電力があれば 2〜4 年で再現できる`
- kicker: `条件11 既存 CF・設備・技術が停めない運用に不可欠かつ模倣困難・代替不可能`
- source: `research3/W3_industry_structure.md、research4/T5_supply_components.md、research4/T2_company_rpo_capacity.md`
- page: 27 / grade: 'B' / condNo: 11
- nodes:
  - dev: col 0, row 0, `DC 開発事業者`, sub `Crusoe・Vantage・Related・STACK`, kind ok
  - grid: col 0, row 2, `電力・系統`, sub `連系 約 40 か月、タービン 2031 年分を販売中`, kind risk
  - orcl: col 1, row 1, `Oracle`, sub `10GW 超を確保(FY29 まで)`, kind self
  - hyper: col 3, row 0, `提携先クラウド`, sub `Oracle DB を 70 リージョンに`, kind ext
  - comp: col 3, row 2, `資金のある競合`, sub `2〜4 年で再現`, kind risk
- edges:
  - dev → orcl, `電力付き建屋(90% 超を相手が資金負担)`, goods
  - orcl → dev, `15〜19 年の賃料`, money, off 0.2
  - grid → dev, `電力の制約`, risk
  - orcl → hyper, `DB の配置`, goods
  - comp → orcl, `追随`, risk
- evidence:
  - `GE Vernova のガス発電の受注残 116GW、変圧器 128〜144 週`
  - `PJM 2028/29 で信頼度要件に 6,831MW 不足`
  - `Jupiter(2.45GW)は不可抗力通知の報道(単一系統、未確認)。10/13 に電力計画を提案`
- reason: `DB の配置は模倣困難だが、AI 容量の障壁は時間で、資本のある競合には破られるため B`

## s28 条件12(評価 A)
- title: `OCI は従量・確約、保守・SaaS は継続課金で、受注残 6,640 億ドルが積み上がるストック型の収益である`
- kicker: `条件12 従量課金型の収益性格(ORCL IaaS 型)であり売り切り・供給過多型(VRT 型)でない`
- source: `会社開示(10-Q、RPO の期間別)、research4/T1_consensus.csv、research3/W5_oracle_ai_economics.md`
- page: 28 / grade: 'A' / condNo: 12
- 本文は構造図の代わりに積み上げ横棒(RPO の期間別)を左に置く: `s.addChart(pres.charts.BAR, [...], L.chartStyle({...}))`
  - x 0.5, y 1.75, w 8.3, h 2.2, barDir 'bar', barGrouping 'stacked', 系列 4 本(各1点、ラベル 'RPO'): `12か月以内 86`、`13〜36か月 246`、`37〜60か月 226`、`60か月超 106`(単位 10億ドル)、chartColors [L.C.dark, L.C.primary, L.C.light, L.C.teal]、dataLabelPosition 'ctr'、showLegend true、legendPos 'b'
- その下に `L.bullets`(x 0.5, y 4.15, w 8.3, h 2.0):
  - `36 か月以内の 3,320 億ドルが、コンセンサス売上(FY28 1,315 億、FY29 1,820 億ドル)の大半を裏付ける`
  - `前払い・持ち込み 750 億ドル分は陳腐化リスクを顧客に移している`
  - `take-or-pay・解約条項・価格改定条項は公開情報で確認できない`
- 右パネル `L.t15Side`: evidence = [`RPO 6,640 億ドル(前年比 +2,090 億)`, `36 か月以内 50%(前期 46%)`, `OCI は従量・確約、保守・SaaS は継続課金`], reason = `継続課金と長期の確約が積み上がるストック型。解約条件が見えないため S でなく A`

## s29 条件13(評価 B)
- title: `保守・SaaS・Database@ は ORCL 型だが、自社で GPU を買う大型 AI 契約の部分が MU 型に寄る`
- kicker: `条件13(総合)アーキタイプ照合: ORCL 型か MU/VRT/AVGO 型か`
- source: `需給エンジン第4.3版、会社開示(FY27 capex ガイダンス)、research4/T2_company_rpo_capacity.md`
- page: 29 / grade: 'B' / condNo: 13
- 本文は左に「スペクトル」(横一列の5つの箱)と下に2段の比較:
  - `L.flow(s, cols, {x:0.5, y:1.75, w:8.3, h:1.5, gap:0.15})` で 5 列、各列 1 箱(h 0.9): `ORCL 型`(tone key)、`保守・SaaS`(on)、`Database@・OCI 一般`(on)、`AI 容量(前払い・持ち込み)`(in)、`AI 容量(自社調達 GPU)`(off) ※見出しは順に `原型` `A` `A` `B` `C〜G`
  - その下 `L.table` x 0.5, y 3.55, w 8.3, colW [2.3, 3.0, 3.0], fontSize 10, rowH 0.4:
    - 見出し: `観点` / `ORCL 型の要素` / `MU 型の要素`
    - `課金` / `継続課金・従量・確約` / `—`
    - `陳腐化リスク` / `前払い・持ち込みで顧客へ移す` / `自社調達 GPU は Oracle が負う`
    - `capex(FY27)` / `純現金 capex 700 億ドル以下(ガイダンス)` / `エンジン 942 億ドル・純現金 733 億ドル`
    - `価値の比率` / `保守・SaaS・OCI 一般 約 50%` / `AI 容量 45%`
- 右パネル `L.t15Side`: evidence = [`前払い・持ち込み累計 750 億ドル`, `10GW の 90% 超はパートナーが資金負担`, `FY27 の総 capex 900〜950 億ドルのうち、顧客の前払いが約 24%`], reason = `原型は ORCL 型のまま。自社調達の GPU が増えると MU 型に寄るため B`
