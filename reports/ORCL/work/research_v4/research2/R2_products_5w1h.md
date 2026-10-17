# R2: Oracle (NYSE: ORCL) 製品・サービス棚卸し(5W1H+価格)

作成日: 2026-10-12 / 担当: 株式調査アシスタント(事実・数値・出典の整理と、出典間の食い違いの指摘のみ。投資判断は含まない)
前提: 決算期末は5月31日。最新の報告済み四半期は Q1 FY2027(2026-08-31 終了、2026-09-10 発表)。

---

## 0. 読み方と制約(先に読むこと)

1. **取得手段は WebSearch の要約のみ。28 回を使い切った**(standard 26 回、extended 2 回)。WebFetch は使っていない。Oracle の公式価格表(oracle.com/cloud/price-list)は検索結果に一覧として出たが、**料金の数字は要約に含まれなかった**。10-K・決算説明会の本文も直接読めていない。したがって、価格と数値はすべて「検索要約に書かれていた内容」である。
2. **Tier**: 1=会社開示・決算説明会、2=規制当局・格付会社・公的統計、3=報道・アナリスト・調査会社、4=ブログ・SNS・販促ページ・ライセンス助言会社。`T1*` = 会社の一次書類・公式ページだが、検索要約経由でしか見ていないもの(要原典確認)。
3. **「(算出)」は調査者の計算**で、式を併記した。会社や第三者の主張ではない。
4. **出典ID**: `[W01]` 等は本書 7 節の出典一覧(今回の検索)。`[既S1]` `[既S3]` `[既S4]` は `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research/` の既存調査、`[既H1]` 等は同 `data/` の既存データ。重複調査を避け、既存の数値は再掲に留めた。
5. **価格の注意**: 実際の取引価格は交渉による。Oracle は多くの製品で定価を公表せず、公表されている定価も検索要約では確認できないものが多い。第三者(T4、主にライセンス助言会社)の価格は、売り込み目的のため高めに出る傾向があり、出典同士の食い違いも大きい。**表中の価格は「定価または第三者の見積り」であり、顧客の実支払額ではない。**
6. **「欠損」**は、検索したが見つからなかった項目。試した検索語は 8 節に残した。
7. **競合欄**: 出典で確認できたものは出典IDを付けた。「※」は一般的な業界認識で、**今回の検索では確認していない**ことを意味する。
8. 英語の発言は和訳主体、原文は要所のみ括弧で付けた。

---

## 1. 規模の把握(製品別売上の開示状況)

Oracle が開示している売上区分は粗く、本書の 12 製品のうち**単独の売上額が開示されているものはない**。開示は、IaaS・SaaS・Software・Services・Hardware の区分と、Fusion ERP・NetSuite の一部四半期の概算額、マルチクラウド DB の成長率だけである。

| 区分 | FY2026(2026-05-31 期、通期) | Q1 FY2027(2026-08-31 終了) | 本書の製品との対応(確認できた範囲) | 出典 / Tier |
|---|---|---|---|---|
| 総売上 | $67.4B(+17%) | $19.3B(+30%)。$19.345B は既存調査の値 | 全体 | [W35][W33][既S4] T1* |
| Cloud 合計 | $34.0B(+39%) | $11.6B(+62%) | ①〜⑩ のクラウド部分 | [W36][W33] T1*/T3 |
| IaaS(Cloud Infrastructure) | $18.1B(+77%、定率 +75%) | $7.4B(+121%) | ①②③ と、DB クラウドサービスを含む可能性が高い(既存データは Oracle Cloud Database を IaaS 区分に記載、T3) | [W36][W33][既H1] |
| SaaS(Cloud Applications) | $15.9B(+11%、定率 +10%) | $4.2B(+10%) | ⑧⑨⑩⑪ | [W36][W33] |
| Software | $24.5B(-1%) | $5.55B(-3%、構成比 29%、前年 38%) | ライセンス+サポート、Java、MySQL(オンプレ)等 | [W36] T3、[既S4] T1* |
| Hardware | $3.1B(+5%) | 約 $0.8B(+15%)。既存データは $0.774B | Exadata 等(内訳は欠損) | [W36] T3、[既S4]、[既H1] T3 |
| Services | $5.7B(+10%) | $1.4B(+5%) | コンサル・導入支援 | [W36] T3、[既S4] |
| RPO(受注残) | $638B(FY26 末) | $664B(前年比 +$209B) | 全体(OpenAI 等 AI 契約が大半) | [既S4][既H1] |

**算出(区分の比率)**

| # | 内容 | 式 |
|---|---|---|
| a | FY26 の Cloud に占める SaaS 比率は 46.8%。10-K 要約の「47%(FY25 58%、FY24 65%)」と整合 | 15.9 ÷ 34.0 = 0.468 |
| b | したがって Cloud に占める IaaS 比率は FY26 約 53%。FY25 は約 42%、FY24 は約 35% | 100 − 47 = 53、100 − 58 = 42、100 − 65 = 35 |
| c | Q1 FY27 の総売上に占める IaaS は 38%、SaaS は 22%、Software は 29% | 7.4 ÷ 19.345 = 0.383、4.2 ÷ 19.345 = 0.217、5.55 ÷ 19.345 = 0.287 |
| d | FY25 の IaaS は約 $10.2B、SaaS は約 $14.3B | 18.1 ÷ 1.77 = 10.2、15.9 ÷ 1.11 = 14.3 |

**事実要約**
- 2 年間で売上の重心が SaaS から IaaS に移った(Cloud 内の SaaS 比率 65% → 47%、IaaS は +77%、SaaS は +11%)。
- Software は減少傾向(-1% → -3%)。会社は「顧客のオンプレミス・ソフトからクラウドへの移行」と説明している [既S4]。
- 製品別の売上は、⑧⑨ の一部を除き**開示が見つからない**(2.2 節以降で個別に記載)。

---

## 2. 製品 × 5W1H+価格 の一覧表(要点のみ。出典と数値の詳細は 3 節)

「欠損」は検索で見つからなかった項目。「※」は競合欄で、今回の検索では確認していない一般的な業界認識。

| # | 製品 | Who(顧客層・顧客名) | What | When(契約・期間) | Where | Why(仕事・代替・乗換) | How(課金方式・単位) | How much(公表価格・売上・成長率) | 主な競合 |
|---|---|---|---|---|---|---|---|---|---|
| ① | OCI AI インフラ(GPU スーパークラスタ) | 大型 AI 研究所・ハイパースケーラー級。OpenAI、xAI、Meta、NVIDIA、AMD を名指し [既S1]。小口も多い(Q4 FY26 更新対象は 59 顧客・3.5 万 GPU) | GPU ベアメタル・クラスタ、Zettascale10(最大 80 万 GPU)、顧客持込(BYOH)/前払い型 | 長期(例: 6 年 $60B の会社説明、OpenAI は約 5 年・約 $300B の報道)。更新は +20% | OCI(Oracle 運営の DC。Abilene 等) | 電力・DC・GPU 調達の代行。代替は自前 DC・ネオクラウド。更新率 GPU 92%(Q4 FY26) | GPU 時間(定価表)。大口契約の単位は非開示 | 定価 H100 $10.00〜10.75/GPU 時(T4)。IaaS 売上 $7.4B(+121%) | AWS、Azure、Google、CoreWeave、Nebius、Crusoe、Nscale [W47] |
| ② | OCI 一般向け計算・保存・ネットワーク | 企業全般。顧客名は欠損 | VM・ベアメタル、Object Storage、ネットワーク | 従量、またはユニバーサル・クレジット(確約。割引率は非公表) | OCI パブリックリージョン(最新の数は欠損) | 低価格の出口料金(10 TB/月無料)が売り。代替は AWS/Azure/Google | OCPU 時間、GB 月、GB 転送 | 例: Arm A1 $0.01/OCPU 時、保存約 $0.0255/GB 月、出口約 $0.0085/GB(T4)。単独売上は欠損 | AWS 28%、Azure 20%、Google 15%(Q2 CY2026 シェア)[W47] |
| ③ | 専用・主権クラウド(Dedicated Region、Alloy、Cloud@Customer、政府・主権) | 政府、通信事業者、金融。Alloy: NRI、Fujitsu、Team IM、stc、du、Ooredoo | 顧客 DC 内の OCI リージョン、パートナーが運営する Oracle クラウド、EU 主権クラウド、各国政府クラウド | 最低 5 年・年次コミット(Oracle 政府向け資料) | 顧客/パートナー DC、EU 内(マドリード・フランクフルト)、政府専用 | データ主権・規制対応。5 年固定+サイト準備費が乗換の壁 | 年次の消費コミット。価格は公開リージョンと同水準の方針 | 最低コミットは出典で食い違い($1M/年〜$3M/年)。売上は欠損 | ※ 他社の主権クラウド施策 |
| ④ | Autonomous Database | Oracle DB 利用企業。顧客名は欠損 | 運用自動化の DB(DW、トランザクション、JSON、APEX) | 従量(時間課金)またはユニバーサル・クレジット | OCI(他は未確認) | DB 運用の自動化。代替は自社運用、他社 DBaaS ※ | ECPU 時間+ストレージ GB | ADW/ATP $0.336/ECPU 時。売上は欠損(Cloud Database +35%、T3) | ※ AWS Aurora/RDS、Azure SQL、Google Cloud SQL 等 |
| ⑤ | Exadata(オンプレ、Cloud@Customer) | 大規模 DB 利用企業。顧客名は欠損 | DB 専用エンジニアド・システム | Cloud@Customer のインフラは 4 年サブスク | 顧客 DC、OCI、他社クラウド内 | 性能・可用性。乗換は DB 依存で高い(定量欠損) | インフラ月額+ECPU 別売(最小 8 ECPU/ノード) | C@C X11M: 月額 $3,200〜$9,000(単位は要確認)。オンプレ価格は欠損 | ※ 他社 DBaaS、IBM、Dell 等 |
| ⑥ | Oracle Database@Azure / @AWS / @Google Cloud | Oracle DB を使い他社クラウドを主に使う企業。顧客名は欠損。顧客数 +180% | 他社 DC 内で Oracle DB(Exadata・Autonomous)を稼働 | マーケットプレイス契約。Azure は MACC 充当可 | Azure 28 リージョン、AWS 20、Google 約 15 | 移行せず低遅延で使う。代替は DB 移設・他社 DB | ECPU 時間(Oracle 課金)+マーケットプレイス経由 | 売上 +353%(Q1 FY27)。絶対額は欠損 | ※ 他社マネージド DB、OCI への移設 |
| ⑦ | Oracle AI Database 26ai | 既存 Oracle DB 顧客 | ベクトル検索、AI エージェント(Select AI Agent、MCP) | 23ai からリリース更新(2025-10 RU)で移行 | オンプレ・OCI・マルチクラウド(範囲は未確認) | 別ベクトル DB を使わず AI を DB に統合 | 高度な AI 機能は追加費用なし(会社説明) | 個別売上は欠損 | ※ 専用ベクトル DB、他社 DB の AI 機能 |
| ⑧ | Fusion Cloud Apps(ERP・HCM・SCM・CX) | 大企業・中堅。顧客名は欠損 | 業務アプリ+AI エージェント(26B から) | サブスク(期間は欠損) | Oracle Cloud(EU 主権版あり) | 業務の統合・自動化。乗換は大工事(定量欠損) | HCM は従業員数×月額、ERP はユーザー×月額 | HCM 定価 $54〜100/人月(T4)。SaaS $4.2B(+10%)、Fusion +14% | SAP、Workday [W37][W39] |
| ⑨ | NetSuite | 中堅・成長企業 | クラウド ERP(中堅向け) | サブスク(多くは年契約。期間は欠損) | Oracle Cloud | 会計・在庫・EC の一体化 | ライセンス(ユーザー)+基本料、月額 | フルユーザー $129/月(T4)。Q3 FY26 売上 $1.1B(+14%) | ※ Microsoft Dynamics、Sage 等 |
| ⑩ | Oracle Health(旧 Cerner) | 病院・政府(米 VA 等) | 電子カルテ(EHR)ほか | VA は 2018 年契約(長期) | 病院側 DC、Oracle クラウド | 診療記録。乗換は極めて高い | 契約ごと(大型は上限額方式) | 売上は欠損。VA は $10B → $16B 超(食い違いあり) | Epic、MEDITECH [W41] |
| ⑪ | 業種別アプリ(銀行・小売・ホテル等) | ホテル(OPERA)、銀行(FLEXCUBE)、小売 | 業種特化アプリ | サブスク/ライセンス(欠損) | Oracle クラウド・顧客環境 | 業種特化業務。ERP との同時販売 | 欠損 | 業種別アプリ成長 +20% 超(Q1 FY27、要約)。金額は欠損 | Amadeus、Agilysys(ホテル)[W42]。他は※ |
| ⑫ | Java SE・MySQL HeatWave ほか | 全業種(Java は従業員数課金) | Java サブスク、MySQL HeatWave | Java は年次サブスク(欠損) | 顧客環境、OCI/AWS/Azure(HeatWave) | Java の利用権。代替は OpenJDK 系 ※ | Java は従業員数×月額。HeatWave は ECPU 時間 | Java $15(1〜999 人)〜約 $5.25 /人月(T4)。MySQL 小構成例 $127.93/月 | MySQL: AWS、Google、Azure の MySQL サービス [W45]。Java: ※ |

---

## 3. 製品別の詳細(各製品 3 行以内の要約+根拠)

### ① OCI の AI インフラ(GPU スーパークラスタ、大型 AI 研究所向け容量)

**要約(3 行)**
- 顧客は OpenAI、xAI、Meta、NVIDIA、AMD など。容量は数年契約で、一部は顧客が GPU 代金を前払い、または GPU を購入して持ち込む形(BYOH)。
- 定価は H100 で 1 GPU 時あたり約 $10〜10.75(T4)。Silicon Data 指数ではハイパースケーラー中央値 $7.19、ネオクラウド $2.80(2026-08-02)で、定価は実勢より高い。
- 会社は契約期間通算の粗利率を 30〜40% と説明。更新は +20% のプレミアム(Q1 FY27)。

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| Who | OpenAI、xAI、Meta、NVIDIA、AMD ほか(Catz 発言「AI 界の顔ぶれ」、2025-09-09)。Meta は $20B(Magouyrk 発言の Reuters 要約)。Q4 FY26 の更新対象は 59 顧客・35,000 GPU(1 顧客平均約 590 基。算出: 35,000 ÷ 59) | [既S1] T1*/T3、[既S4] |
| What | GPU ベアメタル(H100/H200/B200/GB200 等)、クラスタ。Zettascale10: 最大 80 万基の NVIDIA GPU を目標、最大 16 zettaFLOPS(ピーク性能)、Ethernet 系 RoCEv2 の Acceleron ネットワーク、Abilene で最初に展開。注文受付中で 2026 年後半に提供予定と発表(GA の確認は取れず) | [W48] T1/T3 |
| When | 長期契約。会社の例示: 6 年・総額 $60B で通算粗利率 35%(2025-10)。OpenAI: 約 $300B・約 5 年・2027 年開始は WSJ 報道で、OpenAI は 4.5GW を確認したが総額は非開示。更新: Q4 FY26 は顧客の 49% が GPU の 92% を更新。Q1 FY27 は更新対象の全量が更新または再販され、従来契約比 +20%(過半が 4 年以上前の GPU) | [既S3][既S1][既S4] T1*/T3 |
| Where | OCI(Oracle 運営)。Abilene(TX)は 1.2GW、Crusoe が開発。他拠点は既存調査 S1/S3 参照 | [既S1][既S3] |
| Why(仕事) | 学習・推論に必要な電力・DC・GPU を期限内に確保する。 | 会社説明(要約) |
| Why(代替と費用) | (1) ネオクラウドの H100: $2.80/GPU 時(2026-08-02)。(2) ハイパースケーラーの H100: $7.19(同日)。(3) OCI 定価の H100: $10.00〜10.75。**算出**: 定価はハイパースケーラー中央値の 1.39〜1.50 倍、ネオクラウド指数の 3.6〜3.8 倍(10.00÷7.19、10.75÷7.19、10.00÷2.80、10.75÷2.80)。定価と大口の契約単価は別物で、OCI の実契約単価は非開示 | [既S3] T3、[W01][W02] T4 |
| Why(乗換の難しさ) | GPU 稼働率 97.9%(Q1 FY27)。更新実績は上記。大型契約は数年固定で、前払い・BYOH 部分は累計 $75B(顧客側の資金が先に拘束される)。乗換コストの定量データは欠損 | [既S4][既S1] |
| How | 公表の定価表は GPU 時間(ノード単位の時間課金)。大口契約の課金単位(MW、GPU 数×期間等)と、take-or-pay の有無は**非開示・未確認**。前払いまたは BYOH(GPU を顧客が購入して Oracle に提供) | [W01][既S1] |
| How much | 定価(第三者の集計、Oracle の価格表では数字を取得できず): H100 $10.00(または $10.75)、H200 $10.00($80/ノード時。別の資料は約 $12.25)、B200 $14.00($112/ノード時)、GB200 $16.00、GB300 NVL72 $18.00(1 社のみ)。IaaS 売上 FY26 $18.1B(+77%)、Q1 FY27 $7.4B(+121%)。AI インフラ売上の伸びは Q3 FY26 で +243%。粗利率: 契約通算 30〜40%(会社)、Q3 FY26 の AI 容量 32%(ガイダンス 30%)、The Information 報道は 14%(2025 年 6〜8 月) | [W01][W02][W04][W05] T4、[W36] T3、[既S1][既S3][既S4] |
| 主な競合 | AWS 28%・Microsoft 20%・Google 15%(Synergy、Q2 CY2026)。Oracle は「第 2 グループ」(CoreWeave、OpenAI、Crusoe、Nebius、Anthropic、Nscale と並ぶ)で、シェアの数値は非開示。CoreWeave は 2026 年 7 月に全 SKU で約 25% 値上げと報道(既存調査) | [W47] T3、[既S3] |

**参考算出(前提が未確認のため参考扱い)**: 仮に OpenAI の約 $300B(5 年)が 4.5GW に対応するなら、年 $60B ÷ 4.5GW = 約 $13.3B/GW 年(約 $13.3M/MW 年)。この対応関係は会社が確認していない。CoreWeave の約 $40M/MW(短期契約)は単位が確認できておらず、比較しない(算出: 300 ÷ 5 ÷ 4.5)。

---

### ② OCI の一般向け計算・保存・ネットワーク(企業向け IaaS)

**要約(3 行)**
- 汎用 IaaS。公表定価は第三者の集計が中心で、Oracle の価格表から数字は取得できなかった。
- 売りは低い転送料金(月 10 TB 無料、超過約 $0.0085/GB)。割引(ユニバーサル・クレジット)の水準は非公表。
- 一般 IaaS だけの売上は開示がなく、IaaS $7.4B(Q1 FY27)の大半は AI 向けと見られるが、内訳は欠損。

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| Who | 企業全般・スタートアップ(無料枠あり)。代表的な顧客名は今回欠損 | [W07] T4 |
| What | VM(Arm A1、AMD E4/E5 等)、ベアメタル、オブジェクト・ストレージ、ネットワーク | [W06][W07] T4 |
| When | 従量課金(Pay as You Go)、確約(ユニバーサル・クレジット)。契約期間は欠損。**ユニバーサル・クレジット/年次フレックスの条件は検索で見つからず** | [W06] T4 |
| Where | OCI パブリックリージョン(総数の最新値は欠損) | — |
| Why | 転送料金の安さでの乗り換え誘因。他社の転送料金との比較値は今回検索しておらず欠損 | [W06] T4 |
| How | OCPU 時間、GB 月、GB 転送 | [W06] T4 |
| How much | A1.Flex $0.01/OCPU 時、E5.Flex $0.03、E4.Flex $0.025(別の資料は約 $0.048。**食い違い**)。標準オブジェクト保存 約 $0.0255/GB 月(別の資料は約 $0.026)。出口: 月 10 TB まで無料、超過 約 $0.0085/GB。無料枠: Arm 4 OCPU・24GB・ストレージ 200GB | [W06][W07] T4 |
| 規模 | 一般 IaaS 単独の売上は欠損。**参考算出(定義・期間が一致せず目安にならない)**: Q1 FY27 の IaaS $7.4B ÷ Synergy の Q2 CY2026 市場 $143B = 約 5.2% | [W47] T3、[W33] |
| 主な競合 | AWS 28%・Microsoft 20%・Google 15%(Q2 CY2026、Synergy)。市場規模 $143B(+43%、8 年ぶりの高成長) | [W47] T3 |

---

### ③ 専用・主権クラウド(Dedicated Region、Oracle Alloy、Cloud@Customer、政府・主権クラウド)

**要約(3 行)**
- 顧客またはパートナーのデータセンター内に OCI を置く方式(Dedicated Region、Alloy)と、EU・各国政府向けの分離リージョンの 2 系統。
- Oracle の政府向け資料では、Dedicated Region/Alloy は最低 5 年契約で年次コミットが必要。最低コミット額は出典により $1M/年〜$3M/年と割れる。
- パートナー型の顧客は日本(NRI、Fujitsu)、NZ、サウジ、UAE、カタール。売上は個別に開示されていない。

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| Who | Alloy: NRI(日本、100 超の OCI サービスを提供予定)、Fujitsu(日本。2024-04 発表、他市場への展開を検討)、Team IM(NZ。「NZ 初の国内資本のハイパースケールクラウド」)、stc(サウジ)、du(UAE。政府向け)、Ooredoo(カタール。Oracle 発表 2026-02-16)。Dedicated Region: NRI(東京・大阪、2022 年に金融 SaaS を移行)、ITHCA Group(オマーン政府のデータセンター計画で 2 つ目、日付不明)。EU 主権クラウド: 政府・防衛・金融が使うと Oracle が説明(具体名なし)。Vodafone 関連の見出し(SDxCentral)はあるが本文未読で、Alloy パートナーかは**未確認** | [W12][W13][W14][W15][W16][W11][W17] T1/T3 |
| What | **Dedicated Region**: 顧客 DC に完全な OCI リージョン。**Alloy**: パートナーが Oracle クラウドを買い、地域クラウド事業者として自社ブランドで運営(顧客関係はパートナー、Oracle はパートナーと直接契約)。**EU 主権クラウド**: マドリードとフランクフルトの 2 リージョン、EU 内の要員・EU 法人が運営、100 超のサービス、2024-11 に SaaS へ拡張、NVIDIA GPU 提供、Fusion 向けのデータシートは 2026-03。**政府クラウド**: 米・英・豪の政府向けクラウド、国家安全保障向けの隔離リージョン(Oracle 説明)。**Alloy Reserved Regions**: 規制業種向けの専用容量 | [W12][W14][W17][W18] T1/T3 |
| When | Dedicated Region/Alloy は**最低 5 年契約、各年のコミットメント**(Oracle の政府向け資料)。サイト準備と導入は顧客・パートナー負担で別請求 | [W08] T1* |
| Where | 顧客またはパートナーの DC、EU 内、各国政府専用リージョン | [W08][W17] |
| Why(仕事) | データ主権・規制・遅延の要件を満たしつつ、フルスタックのクラウドを使う。 | 会社説明 |
| Why(代替と乗換) | 代替(他社の主権クラウド施策等)の費用比較は今回検索しておらず欠損。乗換の壁: 5 年固定+現地のサイト準備・導入費(Oracle 資料)。定量データは欠損 | [W08] |
| How | 年次の消費コミット。価格は Oracle の商用パブリック・クラウドと同じ水準にする意図と記載(政府向け資料)。EU 主権クラウドは、100 超のサービスを主権機能の追加料金なしで提供(アナリスト 1 社の記述) | [W08][W17] |
| How much(最低コミット) | **出典が食い違う**: (a) 2022 年の値下げで、最低が「3 年間で年 $6M」から約「年 $1M」に(CIO.com、2022 年とされる)。(b) 助言会社 A: 2026 年の標準最低は年 $3M・最短 3 年(算出: 総額 $3M × 3 = $9M)。(c) 助言会社 B: 約 $1M/月 × 36 か月(算出: $36M)。(d) Oracle の政府向け資料: 最低 5 年。Oracle の一次価格表の数字は取得できず | [W09] T3、[W10] T4、[W08] T1* |
| 売上 | 個別開示なし(IaaS に含まれると推定されるが未確認) | — |
| 主な競合 | ※ AWS・Microsoft・Google の主権クラウド施策(今回未検索) | — |

---

### ④ Autonomous Database

**要約(3 行)**
- 運用自動化の DB サービス。課金は ECPU 時間+ストレージ GB で、ADW/ATP の定価は $0.336/ECPU 時。
- FAQ は旧名称で、現行は「Autonomous AI Database」への改称が見られる(価格が同一かは未確認)。
- 単独の売上・顧客数は欠損。「Oracle Cloud Database(IaaS)+35%」(T3)のみ。

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| Who | Oracle DB の既存顧客が中心と見られるが、顧客名・件数は欠損 | — |
| What | Autonomous Data Warehouse(ADW)、Autonomous Transaction Processing(ATP)、JSON Database、APEX Service | [W19] T1* |
| When | 従量(時間)またはユニバーサル・クレジット。契約期間は欠損 | — |
| Where | OCI。Cloud@Customer・マルチクラウドでの提供範囲は**未確認** | — |
| Why | DB 管理の自動化。代替(自社運用の Oracle DB、他社のマネージド DB)の費用比較は欠損 | — |
| How | ECPU 時間(最小 2 ECPU)+ストレージ(GB)。ストレージは別課金 | [W19] T1* |
| How much | ADW・ATP: $0.336/ECPU 時。JSON・APEX: $0.0807/ECPU 時。ストレージ: ADW $0.0244/GB(1TB 単位)、ATP・JSON・APEX $0.1156/GB(最小 20GB)。期間単位(月額か)は要約に明記なし。**算出**: 2 ECPU を 730 時間/月使うと計算分のみで約 $490.6(0.336 × 2 × 730。730 = 8,760 時間 ÷ 12 の仮定) | [W19] T1* |
| 売上 | 欠損。Oracle Cloud Database(IaaS)は +35%(T3。Q3 FY26 の値の可能性。[既H1] 備考 10) | [既H1] T3 |
| 主な競合 | ※ AWS Aurora/RDS、Azure SQL、Google Cloud SQL 等 | — |

---

### ⑤ Exadata(オンプレ、Exadata Cloud@Customer)

**要約(3 行)**
- DB 専用のエンジニアド・システム。オンプレ(購入)、顧客 DC 内のクラウド型(Cloud@Customer)、OCI・他社クラウド内の 3 形態。
- Cloud@Customer の X11M は、インフラを 4 年サブスクで契約し、ECPU を別途購入する形。
- 顧客名・Exadata 単独の売上は欠損。Hardware は FY26 $3.1B(+5%)で、Exadata の比率は不明。

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| Who | 顧客名は欠損(銀行・通信を狙った検索で該当なし) | — |
| What | Exadata X11M(AMD CPU 採用、X10M 比で最大 1.25 倍の同時トランザクション・直列処理と Oracle が主張)。Exascale は公開クラウド側の入口価格を下げる位置づけ(Oracle 説明) | [W20] T1* |
| When | Cloud@Customer のインフラは **4 年サブスク**。ECPU は別購入 | [W20] T1* |
| Where | 顧客 DC(オンプレ・Cloud@Customer)、OCI、Azure・Google 内(Oracle の各ページは価格が OCI の Exadata Database Service と同じと説明) | [W20][W21] T1* |
| Why | 大規模 DB の性能・可用性。乗換の難しさ(DB 依存)の定量データは欠損 | — |
| How | Cloud@Customer: インフラ月額+ECPU(最小 8 ECPU/DB ノード)。OCI/他社クラウド: インフラ時間+ECPU 時間 | [W20][W21] T1* |
| How much | Cloud@Customer X11M の定価(月額): Base System $3,200、Rack $4,320、Rack-L $5,760、Rack-XL $9,000。DB サーバーは $1,600(Base)〜$4,500(XL)。**これらの単位(ラック全体か構成要素か)は要約から確認できず**、実額は原典で確認が必要。オンプレ価格は欠損 | [W20] T1* |
| 売上 | 欠損。Hardware: FY26 $3.1B(+5%)、Q1 FY27 約 $0.8B(+15%)。Hardware に占める Exadata の比率は欠損 | [W36] T3、[既S4] |
| 主な競合 | ※ 他社マネージド DB、汎用サーバー上の DB | — |

---

### ⑥ Oracle Database@Azure / @AWS / @Google Cloud(マルチクラウド)

**要約(3 行)**
- 他社クラウドのデータセンター内で Oracle DB(Exadata 等)を動かし、その他社クラウドの画面・請求から使える。
- Q1 FY27 に売上 +353%、顧客数 +180%(決算説明会の要約複数)。絶対額は非開示。
- AWS は 2026-05-29 に 20 リージョンへ拡大(2 月 7、4 月 12)。

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| Who | Oracle DB を使い、アプリを他社クラウドに置く企業。顧客名は欠損。顧客数は Q1 FY27 で前年比 +180% | [W34] T3 |
| What | Exadata Database Service や Autonomous 等を、他社 DC 内の OCI インフラで稼働 | [W21][W23] |
| When | マーケットプレイス契約。Azure は Azure Consumption Commitment(MACC)に充当可(Oracle のページの記述。個別の適格性は顧客ごとに確認が必要と助言会社が注記)。AWS は Channel Partner Private Offer で再販可 | [W23][W22] T1/T4 |
| Where | 他社クラウドの DC 内。**Azure 28 リージョン(1 社の記述、日付不明。来年さらに 5 追加予定)**、**AWS 20 リージョン(2026-05-29 の AWS 発表。2026-02 は 7、2026-04 は 12)**、**Google 約 15 拠点(DCD、日付不明。2024-09 に GA)**。Q1 FY27 説明会の要約は「70 リージョン・119 アベイラビリティゾーン」と記載したが、再検索では確認できず(単一出典) | [W24][W25][W23][W34] |
| Why | アプリを他社クラウドに置いたまま、Oracle DB を近接して使いたい。代替(DB の移設、他社 DB への切替、OCI への移設)の費用は欠損 | 会社説明 |
| How | Oracle が ECPU 時間で課金し、マーケットプレイス側が取引と MACC を処理(助言会社の記述)。Oracle の公式価格表の数字は取得できず | [W22] T4 |
| How much | **売上の伸び**: Q1 FY27 +353%、顧客数 +180%。過去: Q4 FY26 +404%(予約 +325%、T4)、Q3 FY26 +531%、Q1 FY26 +1,529%(T4)。**絶対額は非開示**。古い参考値: Q1 FY26 の Cloud Database サービス +32%、年換算約 $2.8B(既存調査) | [W34] T3、[既S1][既S4] |
| 主な競合 | ※ 他社のマネージド DB サービス、DB の OCI への移設 | — |

---

### ⑦ Oracle AI Database 26ai(ベクトル検索・AI エージェント)

**要約(3 行)**
- 23ai の長期サポート版後継。2025 年 10 月のリリース更新を適用すると 23ai から 26ai になる(DB のアップグレード不要と Oracle が説明)。
- AI Vector Search などの高度な AI 機能は追加費用なしで含まれ、無料ティアもある(Oracle の説明)。
- 個別の売上・導入数は欠損。Q1 FY27 の説明は「企業顧客のほぼ全員が自社データで AI に推論させたい」。

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| Who | 既存の Oracle DB 顧客(23ai 利用者を含む) | [W27] T1 |
| What | AI Vector Search、Unified Hybrid Vector Search(ベクトルとリレーショナル・テキスト・JSON・グラフ・空間の述語を 1 つのクエリで併用)、Select AI Agent(DB 内でエージェントを定義・実行・統制する枠組み。アナリスト 1 社の記述)、MCP サーバー対応 | [W27] T1、[W28] T3 |
| When | 2025-10 のリリース更新で 23ai → 26ai。Oracle の発表日は検索要約に表示なし | [W27] |
| Where | オンプレ、OCI、マルチクラウドの全てで同一かは**未確認** | — |
| Why | 別のベクトル DB を立てず、既存 DB のデータに AI を直結する。代替(専用ベクトル DB 等)の費用は欠損 | 会社説明 |
| How | 高度な AI 機能は追加費用なしで 26ai に含まれる(Oracle のページ)。Autonomous AI Database でも同様かは**未確認** | [W27] T1 |
| How much | 個別価格なし(DB 本体のライセンス・サポートまたはクラウド使用料に内包)。売上は欠損 | — |
| 主な競合 | ※ 専用ベクトル DB、他社 DB の AI 機能 | — |

---

### ⑧ Fusion Cloud Applications(ERP・HCM・SCM・CX)

**要約(3 行)**
- 業務アプリの統合スイートで、SaaS(Cloud Apps)は FY26 $15.9B(+11%)、Q1 FY27 $4.2B(+10%)。
- 課金は HCM が従業員数、ERP がユーザー数。定価は非公表で、第三者の見積りは幅が広く、実勢は定価の 35〜60% 引きと助言会社が主張。
- 競合は SAP と Workday。Apps Run The World は 2024 年のクラウド ERP シェアを Oracle 21.7%、SAP 15.0% と推計。

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| Who | 大企業・中堅。顧客数・顧客名は欠損(営業リスト会社 Landbase の「5,000 社」https://data.landbase.com/technology/oracle-fusion/ は T4 で、ページに「架空の企業ロゴ」の注記があり信頼性が低いため不採用) | 検索 #14 の結果(T4) |
| What | ERP、HCM、SCM、CX。Release 26B で「Fusion Agentic Applications」が登場(Oracle の Fusion Insider ブログ)。600 超の AI エージェントが追加ライセンス費用なしとする SNS 投稿あり(T4) | [W38] T1、[W39] T4 |
| When | サブスク。契約期間は欠損。Q2 FY26 は ERP、SCM、HCM、NetSuite、CX がいずれも 2 桁成長(CEO 発言、Apps Run The World 経由) | [W37] T3 |
| Where | Oracle Cloud(OCI 上)。EU 主権クラウド版のデータシートは 2026-03 | [W17] |
| Why | 業務の一元化と自動化。会社説明: 業種別アプリが Fusion を牽引する、またはその逆の案件が増えている(Sicilia、2025-12-10、要約)。乗換の難しさの定量データは欠損 | [既S1] T1* |
| How | HCM: 従業員数×月額(全従業員が課金対象、最低 1,000 人)。ERP: ホステッド・ネームドユーザー×月額 | [W39] T4 |
| How much | HCM の定価: スイート全体で $54〜100/人月、実勢 $22〜50(50〜60% 引き)。別資料は $13〜34、$20〜35。ERP: $625/ユーザー月(別資料は $175〜625)。5 年総額は 1,000 人規模で $8M〜$20M(助言会社の推計)。**売上**: Cloud Apps FY26 $15.9B、Q1 FY27 $4.2B(+10%)。「Fusion +14%」「業種別アプリ +20% 超」(決算説明会の要約)。Fusion ERP は Q1 FY26 に約 $1.0B(+17%) | [W39] T4、[W36][W33] T1*/T3、[W34] T3、[W32] T1 |
| 主な競合 | SAP、Workday([W39])。クラウド ERP シェア 2024 年: Oracle 21.7%、SAP 15.0%(Apps Run The World の推計、Gartner のデータではない) | [W37] T3 |

---

### ⑨ NetSuite

**要約(3 行)**
- 中堅向けのクラウド ERP。Oracle は定価を公表せず、第三者はフルユーザー $129/月(従来 $99)、基本料 $999〜2,499/月と見積もる。
- 売上は Q1 FY26 が約 $1.0B(+16%)、Q3 FY26 が $1.1B(+14%、定率 +11%)。単四半期の 4 倍で約 $4.4B(算出)。
- Q1 FY27 の NetSuite の公式値は確認できず、「NetSuite の意思決定サイクルが長くなり、他の SaaS より成長が鈍い」との言及のみ。

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| Who | 中堅・成長企業。顧客数は「4 万社超・219 の国と地域」との記述が 1 件あるが、出典の特定ができず信頼度は低い。公式の最新顧客数は欠損 | [W30][W29] T4 |
| What | クラウド ERP(会計、在庫、EC 等)。AI 機能の詳細は欠損 | — |
| When | サブスク。期間は欠損(第三者の資料は年契約が多いと記述するが、今回の要約では確認できず) | — |
| Where | Oracle Cloud | — |
| Why | 中堅の基幹業務の一体運用。5 年総額の例は 1,000 人規模の Oracle ERP 向けで、NetSuite 単独の値ではない | [W39] |
| How | ユーザー数×月額+基本プラットフォーム料+モジュール | [W29] T4 |
| How much | フルユーザー $129/月(従来 $99 からの約 30% 値上げと記述する資料。レンジは $99〜199)。基本料は多くの米中堅で $999〜2,499/月、大企業版は約 $5,000/月から。従業員セルフサービス $10〜25/月。Oracle は価格を公表していない。**売上**: Q1 FY26 約 $1.0B(+16%)、Q3 FY26 $1.1B(+14%、定率 +11%)。**算出**: Q3 FY26 を年換算して約 $4.4B(1.1 × 4)。これは報告された ARR ではない | [W29] T4、[W32] T1、[W30] T3 |
| 主な競合 | ※ Microsoft Dynamics 365、Sage、SAP の中堅向け製品(今回未検索) | — |

---

### ⑩ Oracle Health(旧 Cerner)

**要約(3 行)**
- 米国の急性期病院で、Epic(43.7%)に次ぐ 2 位(21.9%、KLAS 2026)。2025 年に純減 56 病院で 3 年連続の純減。
- 最大顧客は米国退役軍人省(VA)。契約は 2018 年の約 $10B から、費用が $16B 超に増加し、上限額の拡大が議論されている(総額の数字は出典で割れる)。
- Oracle Health の売上は開示が見つからない。VA の導入は 2026-07 時点で 14 拠点。

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| Who | 病院、政府。VA(2018 年に Cerner と約 $10B で契約)。KLAS: 米急性期病院の 21.9%、ベッド数の 20.4% | [W40][W41] T3 |
| What | 電子カルテ(EHR)。新しい AI 搭載 EHR プラットフォームを 2026 年に展開中(KLAS は 2026 年を「重要な年」と評価) | [W41] T3 |
| When | VA は長期の導入計画。2026-07 時点で 14 拠点に展開済み、2028-01 までにさらに 36 拠点、残る 120 拠点は現行の上限・工程では完了しない | [W40] T3 |
| Where | 病院側の環境、Oracle クラウド(詳細は欠損) | — |
| Why | 診療記録の基幹システム。乗換の難しさは極めて高い(Epic 側へ年々流出している事実が KLAS に出ている)。定量コストは欠損 | [W41] T3 |
| How | 契約ごと。VA は上限額方式 | [W40] |
| How much | **VA 契約額は出典間で食い違い**: (a) 2018 年の約 $10B、費用はその後 $16B 超(Becker's)。(b) 下院委員会の記事は $16.9B の増額。(c) 下院議員の発表は $10B から約 $27B へ。整合は取れていない。**売上は欠損**(Oracle Health 単独の開示は見つからず、買収価格 $28.3B も今回の検索で確認できず) | [W40] T3 |
| 状況 | KLAS: 2025 年に純 56 病院・14,676 ベッドを失い、5 年で純 173 病院減。EHR 購入判断を行う病院は 2024 年比 -40%、2023 年比で約 -50%。10 病院超の大規模システムで 2025 年に全社 EHR を決めたのは 2 件で、いずれも Epic。下院 VA 委員会は Oracle の幹部に証言を求める動議を全会一致で可決(Oracle は公聴会を欠席、2026-09) | [W41][W40] T3 |
| 主な競合 | Epic(43.7%)、MEDITECH(14.7%)。KLAS 2026 | [W41] T3 |

---

### ⑪ 業種別アプリ(銀行・小売・ホテル等)

**要約(3 行)**
- ホテル向けの OPERA Cloud と MICROS(POS)、銀行向けの FLEXCUBE などが代表。小売アプリの情報は今回欠損。
- Q1 FY27 に「業種別アプリが 20% 超成長」との決算説明会の要約があるが、売上額・顧客数は欠損。
- 価格は全て欠損。IHG が 2026-01 に OPERA Cloud を承認 PMS に追加したことは確認。

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| Who | ホテル: IHG が OPERA Cloud を 2026-01 に承認(米州と EMEAA。フランチャイズ加盟者が選択可。導入数ではない)。MICROS は 180 超の国で利用(買収時の説明)。銀行: Bank Aston が全技術基盤で協業(日付不明の SNS 投稿)。小売: 欠損 | [W42] T3、[W43] T4 |
| What | OPERA Cloud(ホテル管理)、Simphony(POS)、FLEXCUBE(コア・バンキング、V14)、Oracle の銀行製品群は OCI での稼働を検証済み | [W42][W43] |
| When | 欠損 | — |
| Where | Oracle クラウド、顧客環境 | — |
| Why | 業種特化機能。銀行: OCI での TCO が現行オンプレ比で約 50% 低いと Oracle が主張(日付不明のブログ、販促性が高い)。会社説明: 業種別アプリと Fusion が相互に案件を牽引 | [W43] T1/T4、[既S1] |
| How | 欠損 | — |
| How much | 価格は欠損。業種別アプリの成長 +20% 超(Q1 FY27、要約) | [W34] T3 |
| 主な競合 | ホテル: Amadeus、Agilysys [W42]。銀行(Temenos、Finastra 等)・小売: ※ 今回未検索 | [W42] T3 |

---

### ⑫ Java・MySQL HeatWave ほか(データベース・ライセンスを含む)

**要約(3 行)**
- Java SE は従業員数に応じた月額のサブスク(第三者が整理した定価は 1〜999 人で $15/人月、大規模では約 $5.25〜5.70)。全従業員が対象で、Java 利用者数ではない。
- MySQL HeatWave は ECPU 時間課金(OCI、AWS、Azure)。Oracle の例で小構成 200GB が月 $127.93。
- DB ライセンスは Enterprise Edition が約 $47,500/プロセッサー、サポートは年 22%(いずれも第三者の記述)。Software 売上は減少傾向。

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| Who | **Java**: 全業種。従業員数で課金するため、大企業ほど負担が大きい。**MySQL**: Web・SaaS 事業者等。顧客名・件数は欠損。**DB ライセンス**: 既存顧客の基盤 | [W44] T4 |
| What | Java SE Universal Subscription、MySQL HeatWave(OCI・AWS・Azure で提供、機能の同等性は異なる)、Oracle Database のライセンス+サポート | [W44][W45] |
| When | Java: 年次サブスク(更新時に年 8% まで上がり得るとの助言会社の記述、Oracle の文書では未確認)。DB サポート: 年次(年 4% 以上の増加との記述が 1 件)。MySQL: 従量 | [W44][W46] T4 |
| Where | 顧客環境(Java、DB ライセンス)、OCI/AWS/Azure(HeatWave) | [W45] |
| Why(代替) | Java の代替は OpenJDK 系の無償ディストリビューション ※(今回未検索)。MySQL HeatWave の代替は AWS・Google・Azure の MySQL サービスで、Oracle は 2025 年のブログで HeatWave が大幅に安いと主張(US East・特定サイズの比較、販促) | [W45] T1/T4 |
| How | Java: 従業員数×月額(派遣・契約社員を含む定義と記述)。HeatWave: ECPU 時間+HeatWave 容量+ストレージ。DB: プロセッサー課金または Named User Plus+年 22% サポート | [W44][W45][W46] |
| How much(Java) | 定価: 1〜999 人で $15.00/人月、最大帯は約 $5.25〜5.70。上位 2 帯の区切りは出典で食い違う。**算出**: 1 万人規模で約 $990K/年(8.25 × 10,000 × 12。別の資料は $1.8〜2.4M で、同じ価格表と整合せず)。交渉割引は 30〜60% との助言会社の主張(検証不能) | [W44] T4 |
| How much(MySQL) | Oracle 公式ページの例: 小構成(200GB)で月 $127.93。第三者の記述では OCPU 時間約 $0.3536(旧単位)。OCPU シェイプは 2024-09-05 以降の新規作成が停止、2026-03-13 以降利用不可(助言会社 1 社の記述、要確認)。売上・顧客数は欠損 | [W45] T1*/T4 |
| How much(DB ライセンス) | Enterprise Edition 約 $47,500/プロセッサー、Standard Edition 2 は $17,500、Named User Plus は約 $950(算出: 47,500 ÷ 50)、最低 25 ユーザー/プロセッサー。Partitioning 約 $11,500/プロセッサー。サポートは年 22%(正味ライセンス額基準との記述が多い。**算出**: 定価ベースで 47,500 × 0.22 = $10,450/年)。割引は 40〜70% との助言会社の記述。**Software 売上**: FY26 $24.5B(-1%)、Q1 FY27 $5.55B(-3%)。ライセンスとサポートの内訳、サポート更新率は欠損 | [W46] T4、[W36] T3、[既S4] |
| 主な競合 | MySQL: AWS・Google・Azure の MySQL サービス [W45]。Java・DB: ※ OpenJDK 系、PostgreSQL、他社 DB | [W45] |

---

## 4. 出典間の食い違いと、既存データへの修正提案

| # | 項目 | 食い違い | 所見 |
|---|---|---|---|
| 1 | Q1 FY27 のマルチクラウド DB 成長率 | 既存データ [既H1] 表 A は **+531%**(備考 10)。決算説明会の要約(Yahoo、BigGo 等)と [既S4] は **+353%、顧客 +180%** | +531% は Q3 FY26 の値([既S1])と一致。Q1 FY27 は +353%(複数の要約で確認)が妥当と見られるが、会社の逐語は未読。**[既H1] の修正を推奨** |
| 2 | Q1 FY27 の Fusion の成長 | [既H1]: Fusion ERP $1.1B(+17%)。説明会の要約: 「Fusion は +14%」 | +17% は Q1 FY26 の Fusion ERP(+17%、$1.0B、Oracle 発表 [W32])と同じ。範囲(Fusion 全体か ERP か)も異なる可能性。**未解決** |
| 3 | Q1 FY27 の NetSuite | [既H1]: $1.1B(+14%)。Zacks 系の記事: Q3 FY26 が $1.1B(+14%、定率 +11%) | 同じ値が Q3 FY26 の値として出ており、誤帰属の可能性。Q1 FY27 の NetSuite は**未確認** |
| 4 | OCI の H100 定価 | $10.00/GPU 時と $10.75 の 2 つ | 同じ H100 でも出典で異なる。H200 も $10.00 と約 $12.25 |
| 5 | GB200 の単価 | OCI 定価 $16.00(computeprices)。既存調査 [既S3] のネオクラウド GB200 は $8.00(GMI Cloud)と $10.50 | 事業者が異なり直接比較できない。出典はいずれも T4 |
| 6 | Dedicated Region の最低コミット | 年 $1M(2022、CIO.com)、年 $3M・3 年(助言会社)、月 $1M・36 か月(助言会社)、5 年(Oracle) | 時点と定義が混在。Oracle の一次価格表の数字は未取得 |
| 7 | VA 契約の総額 | 約 $10B(2018)、$16B 超、$16.9B の増額、約 $27B | 「当初」「現在の上限」「見込み総額」が混在している可能性 |
| 8 | OCI の E4 計算単価 | $0.025/OCPU 時と約 $0.048 | 同一シェイプで 2 倍近い差 |
| 9 | マルチクラウドの拠点数 | 説明会の要約 70 リージョン・119 AZ(単一)。個別: Azure 28、AWS 20、Google 約 15(算出合計 63。時点・重複未確認) | 合計は一致せず、重複も未検証。**参考扱い** |
| 10 | Cloud Database(IaaS)+35% | [既H1] は Q1 FY27 の値と記載、[既S1] は Q3 FY26 の値と記載 | 時点が割れている |
| 11 | ネオクラウドとの定価差 | OCI の定価(H100 $10.00〜10.75)は Silicon Data のハイパースケーラー中央値 $7.19 より高い | 定価と実勢の乖離。契約単価の開示はなし |

---

## 5. 製品別の「開示の濃さ」一覧(どこまで数字が取れたか)

| 製品 | 売上額 | 成長率 | 顧客名 | 定価 | 課金単位 | 契約期間 |
|---|---|---|---|---|---|---|
| ① AI インフラ | 区分のみ(IaaS) | あり(+243% は Q3 FY26) | あり(5 社) | 第三者(T4) | 一部 | 例示あり |
| ② 一般 IaaS | 欠損 | 欠損 | 欠損 | 第三者(T4) | あり | 欠損 |
| ③ 専用・主権 | 欠損 | 欠損 | あり(Alloy 6 社) | 最低額が割れる | 一部 | 5 年(Oracle) |
| ④ Autonomous | 欠損 | +35%(時点不明) | 欠損 | Oracle FAQ | あり | 欠損 |
| ⑤ Exadata | 欠損 | 欠損 | 欠損 | C@C のみ | あり | 4 年(C@C) |
| ⑥ マルチクラウド DB | 絶対額欠損 | あり(+353%) | 欠損 | 欠損 | 一部 | 欠損 |
| ⑦ 26ai | 欠損 | 欠損 | 欠損 | 追加費用なし(会社説明) | — | — |
| ⑧ Fusion | 区分のみ(SaaS) | あり | 欠損 | 第三者(T4) | あり | 欠損 |
| ⑨ NetSuite | 概算あり | あり | 欠損 | 第三者(T4) | あり | 欠損 |
| ⑩ Oracle Health | 欠損 | 欠損 | VA ほか | 欠損 | 欠損 | VA のみ |
| ⑪ 業種別 | 欠損 | +20% 超(要約) | 一部 | 欠損 | 欠損 | 欠損 |
| ⑫ Java/MySQL | Software のみ | -3% | 欠損 | 第三者/Oracle ページ | あり | 年次 |

---

## 6. 全体の事実要約(5 行)

1. 売上の重心は SaaS から IaaS に移り、Q1 FY27 の IaaS は $7.4B(+121%)で総売上の 38%(算出)。SaaS は +10%、Software は -3%。
2. AI インフラ(①)の定価は H100 で $10.00〜10.75/GPU 時(T4)と、実勢指数(ハイパースケーラー $7.19、ネオクラウド $2.80)より高い。実際の契約単価は非開示で、更新は +20%(Q1 FY27)。
3. 専用・主権(③)とマルチクラウド DB(⑥)は、Oracle の DB 資産を顧客の望む場所(自国・他社クラウド)に置く方式。③ は最低 5 年の年次コミット、⑥ は他社マーケットプレイス経由の課金。
4. アプリ(⑧〜⑪)の製品別売上は NetSuite(約 $1.0〜1.1B/四半期)以外ほぼ開示がない。Oracle Health は米国市場で純減が続き、VA 契約の総額が議論されている。
5. 公表価格の多くは第三者(ライセンス助言会社)の記述で、出典間の食い違いが大きい。Oracle の公式価格表の数字は取得できなかった。

---

## 7. 出典一覧

Tier の `*` は、会社・規制当局の一次書類だが検索要約経由でしか見ていないことを示す。掲載日は検索要約に表示があったものだけ記載し、表示がないものは「日付不明」とした。

### 7-1. 既存調査(再掲元)

| ID | 内容 | パス |
|---|---|---|
| 既S1 | 経営陣シナリオ(顧客名、BYOH、マルチクラウド等) | `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research/S1_management_scenario.md` |
| 既S3 | スカットルバット(GPU 単価、粗利率、拠点) | 同 `S3_scuttlebutt.md` |
| 既S4 | 芯の追加事実(GPU 更新、セグメント、耐用年数) | 同 `S4_core_variables.md` |
| 既H1 | 財務データ(四半期 P/L と KPI) | `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/data/H1_financials.md` |

### 7-2. 今回の検索で得た出典

| ID | 媒体・内容 | URL | 掲載日 | Tier |
|---|---|---|---|---|
| W01 | Spheron「OCI GPU pricing 2026」 | https://www.spheron.network/blog/oracle-cloud-oci-gpu-pricing-2026/ | 2026-06 頃(要約に「June 2026」と記載) | 4 |
| W02 | computeprices.com(Oracle の GB200・B200・H200) | https://computeprices.com/providers/oracle/gpus/gb200 、https://computeprices.com/providers/oracle/gpus/b200 、https://computeprices.com/providers/oracle/gpus/h200 | 日付不明 | 4 |
| W03 | Oracle OCI Price List(SKU 名のみ、料金の数字は要約に出ず) | https://www.oracle.com/cloud/price-list/ | 日付不明 | 1* |
| W04 | Flopper(Oracle Cloud) | https://flopper.io/providers/oracle-cloud | 日付不明 | 4 |
| W05 | Thunder Compute / oraclelicensingexperts の GPU SKU 解説 | https://www.thundercompute.com/blog/oracle-cloud-oci-gpu-pricing 、https://oraclelicensingexperts.com/blog/oracle-cloud-gpu-skus-pricing/ | 2026-04 頃 | 4 |
| W06 | Finout「OCI Costs Overview」 | https://www.finout.io/blog/oci-costs-overview | 日付不明 | 4 |
| W07 | oraclelicensingexperts / getdeploying / selfhost.it.com(OCI サービスと無料枠) | https://oraclelicensingexperts.com/oracle-cloud-infrastructure-services-and-the-costs 、https://getdeploying.com/oracle-cloud 、https://selfhost.it.com/blog/oci-free-tier-breakdown | 日付不明 | 4 |
| W08 | Oracle 政府向け「digital gov suite cloud deployment」(Dedicated Region/Alloy 最低 5 年) | https://www.oracle.com/a/ocom/docs/industries/government/digital-gov-suite-cloud-deployment.pdf | 日付不明 | 1* |
| W09 | CIO.com「Oracle cuts price of OCI Dedicated Region to expand user base」 | https://cio.com/article/401641/oracle-cuts-price-of-oci-dedicated-region -to-expand-user-base.html | 2022 年(要約の記述) | 3 |
| W10 | Redress Compliance / oraclelicensingexperts(Dedicated Region 費用) | https://redresscompliance.com/oracle-dedicated-region-cost-optimization-cost-and-licensing/ 、https://oraclelicensingexperts.com/oracle-dedicated-region-guide/ | 2026 年と記載 | 4 |
| W11 | SDxCentral「Oracle snares Vodafone deal, adds cheaper OCI option」(見出しのみ、本文未読) | https://www.sdxcentral.com/news/oracle-snares-vodafone-deal-adds-cheaper-oci-option/ | 日付不明 | 3 |
| W12 | DatacenterDynamics「Nomura Research Institute deploys Oracle Alloy」 | https://www.datacenterdynamics.com/en/news/nomura-research-institute-deploys-oracle-alloy-in-its-data-centers | 日付不明 | 3 |
| W13 | Fujitsu 発表 / TelecomTV(Fujitsu と Oracle、日本の主権クラウド) | https://info.archives.global.fujitsu/global/about/resources/news/press-releases/2024/0418-01.html 、https://telecomtv.com/content/digital-platforms-services/fujitsu-and-oracle-collaborate-to-deliver-sovereign-cloud-and-ai-capabilities-in-japan-50162 | 2024-04-18 | 1/3 |
| W14 | Oracle Alloy ページ(Team IM、NRI、stc) | https://oracle.com/rs/cloud/alloy | 日付不明 | 1* |
| W15 | Oracle 発表「Ooredoo と Oracle」 | https://www.oracle.com/ae/news/announcement/ooredoo-oracle-collaborating-to-provide-ai-and-cloud-computing-services-2026-02-16/ | 2026-02-16 | 1* |
| W16 | DatacenterDynamics「du to launch cloud and sovereign AI services for UAE govt with Oracle Alloy」 | https://www.datacenterdynamics.com/en/news/du-to-launch-cloud-and-sovereign-ai-services-for-uae-govt-with-oracle-alloy/ | 日付不明 | 3 |
| W17 | EU 主権クラウド: Oracle ブログ、Futurum、Oracle の Fusion 向けデータシート(2026-03)ほか | https://blogs.oracle.com/cloud-infrastructure/oracle-eu-sovereign-cloud-lessons-learned 、https://futurumgroup.com/insights/oracle-demonstrates-strategic-commitment-to-data-privacy-and-sovereignty-with-eu-sovereign-cloud-launch 、https://www.oracle.com/hr/a/ocom/docs/cloud/oracle-eu-sovereign-cloud-for-fusion-apps-datasheet.pdf 、https://www.telecomtv.com/content/digital-platforms-services/oracle-addresses-european-data-privacy-and-sovereignty-requirements-with-new-eu-sovereign-cloud-47823/ | 2024-11〜2026-03 | 1*/3 |
| W18 | Oracle Alloy Reserved Regions | https://www.oracle.com/cloud/alloy/reserved-regions/ | 日付不明 | 1* |
| W19 | Oracle「Autonomous Database ECPU FAQ」 | https://oracle.com/a/ocom/docs/autonomous-database-ecpu-faq.pdf | 日付不明(旧名称) | 1* |
| W20 | Oracle「Exadata Cloud@Customer Pricing」 | https://www.oracle.com/engineered-systems/exadata/cloud-at-customer/pricing/ | 日付不明 | 1* |
| W21 | Oracle の Exadata Database Service 価格(Azure / Google ページ) | https://www.oracle.com/cloud/azure/oracle-database-at-azure/pricing/ 、https://www.oracle.com/cloud/google/oracle-database-at-google-cloud/pricing/ | 日付不明 | 1* |
| W22 | oraclelicensingexperts(Database@Azure の価格・ライセンス) | https://oraclelicensingexperts.com/blog/oracle-database-at-azure-pricing-benchmarks/ 、https://oraclelicensingexperts.com/blog/oracle-database-at-azure-licensing/ | 日付不明 | 4 |
| W23 | Oracle「Oracle Cloud goes everywhere」(Magouyrk、マルチクラウド)。Azure 28 リージョンの記述の出典ページは特定できず | https://www.oracle.com/cloud/multicloud/clay-magouyrk-oracle-cloud-aws-google-azure/ | 日付不明 | 1* |
| W24 | AWS What's New: Database@AWS 20 リージョン / 12 リージョン / 2 リージョン追加 | https://aws.amazon.com/de/about-aws/whats-new/2026/05/oracle-database-aws-available-twenty-regions/ 、https://aws.amazon.com/about-aws/whats-new/2026/04/oracle-database-aws-available-twelve-regions 、https://aws.amazon.com/about-aws/whats-new/2026/02/oracle-database-aws-available-canada-central-sydney-aws-regions | 2026-05-29 / 2026-04 / 2026-02 | 1(AWS) |
| W25 | DatacenterDynamics「Oracle Database@AWS now offered in 20 global regions」(Google 約 15 拠点の記述を含む) | https://www.datacenterdynamics.com/en/news/oracle-databaseaws-now-offered-in-20-global-regions/ | 日付不明 | 3 |
| W26 | Oracle 発表「Database@Azure が東南アジアで利用可能」(一覧のみ) | https://www.oracle.com/sg/news/announcement/oracle-database-at-azure-now-available-in-southeast-asia-2025-03-12 | 2025-03-12 | 1* |
| W27 | Oracle「Oracle AI Database 26ai」ブログ・製品ページ | https://blogs.oracle.com/database/oracle-announces-oracle-ai-database-26ai 、https://www.oracle.com/database/ai-native-database-26ai/ | 2025-10 頃(要約に発表日の表示なし) | 1 |
| W28 | NAND Research「Oracle Database 26ai Delivers Fully Integrated AI」 | https://nand-research.com/research-brief-oracle-database-26ai-delivers-fully-integrated-ai/ | 日付不明 | 3 |
| W29 | NetSuite 価格ガイド(Hyperbots、Fuzen、Redress 等) | https://blog.hyperbots.com/netsuite-pricing-(2025)-costs-calculator-roi 、https://www.fuzen.io/posts/netsuite-cost-breakdown 、https://redresscompliance.com/oracle-netsuite-licensing-guide.html | 2025〜2026 | 4 |
| W30 | Nasdaq / Zacks「Oracle's NetSuite Division in Focus」 | https://www.nasdaq.com/articles/oracles-netsuite-division-focus-will-it-boost-revenue-growth | 2026 年(日付不明) | 3 |
| W31 | Houseblend「Oracle FY2026 結果分析」 | https://www.houseblend.io/articles/en/analyse-resultats-oracle-exercice-2026-netsuite-ia-cloud | 2026-05-01 | 4 |
| W32 | Oracle Q1 FY2026 決算発表(Fusion ERP 約 $1.0B・+17%、NetSuite 約 $1.0B・+16%) | https://www.oracle.com/news/announcement/q1fy26-earnings-release-2025-09-09/ | 2025-09-09 | 1* |
| W33 | Oracle Q1 FY2027 決算発表 | https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/ | 2026-09-10 | 1* |
| W34 | Q1 FY2027 説明会の要約: Yahoo Finance、BigGo、MarketBeat | https://finance.yahoo.com/markets/stocks/articles/oracle-q1-earnings-call-highlights-230310387.html 、https://finance.yahoo.com/markets/stocks/articles/oracle-corp-orcl-q1-2027-090101356.html 、https://finance.biggo.com/quote/ORCL/earnings-call/US_ORCL_2026-09-10 、https://www.marketbeat.com/instant-alerts/transcript-oracle-q1-earnings-call-highlights-2026-09-10/ | 2026-09-10 以降 | 3 |
| W35 | Oracle FY2026 Form 10-K(Cloud Apps が Cloud 売上の 47%/58%/65%) | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526277521/orcl-20260531.htm | 2026-06 | 1* |
| W36 | Q4 FY2026 決算発表と報道(FY26 の区分別売上): Oracle IR、StorageNewsletter、Verdict | https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/ 、https://www.storagenewsletter.com/2026/06/12/oracle-fiscal-4q26-and-fy26-financial-results/ 、https://www.verdict.co.uk/?p=402027 | 2026-06-10〜12 | 1*/3 |
| W37 | Apps Run The World(Oracle のクラウド ERP シェア、Q2 FY26 の 2 桁成長) | https://appsruntheworld.com/oracle-cloud-applications-and-infrastructure-shine-in-2q26 、https://www.appsruntheworld.com/oracle-on-track-to-lead-both-cloud-erp-and-total-erp/ | 2025-12 頃 / 日付不明 | 3 |
| W38 | Oracle Fusion Insider ブログ(Release 26B、Fusion Agentic Applications) | https://blogs.oracle.com/fusioninsider/post/roadmaps | 日付不明 | 1 |
| W39 | Fusion の価格解説: ERP Research、oraclelicensingexperts ほか | https://erpresearch.com/en-gb/oracle-erp-fusion-cloud-pricing 、https://www.erpresearch.com/pages/en-us/oracle-erp-cloud-vs-workday 、https://oraclelicensingexperts.com/blog/oracle-fusion-hcm-cloud-pricing/ | 2024〜2026 | 4 |
| W40 | Oracle Health と VA: Becker's、下院議員の発表、Federal News Network | https://beckershospitalreview.com/healthcare-information-technology/ehrs/va-proposes-expanding-oracle-health-contract-past-10b-ceiling 、https://budzinski.house.gov/posts/27-billion-and-counting-budzinski-demands-answers-from-va-admin-on-exploding-oracle-costs 、https://federalnewsnetwork.com/veterans-affairs/2026/09/house-va-lawmakers-to-subpoena-oracle-over-ehr-contract/ 、https://www.beckershospitalreview.com/healthcare-information-technology/ehrs/va-deploys-oracle-health-ehr-at-4-more-sites/ | 2026-07〜09 | 3 |
| W41 | KLAS 2026 EHR 市場シェア: HIT Consultant、Healthcare IT News、Becker's | https://hitconsultant.net/2026/05/14/klas-2026-ehr-market-share-report/ 、https://www.healthcareitnews.com/news/epic-gains-ground-acute-care-ehr-purchasing-slows 、https://www.beckershospitalreview.com/healthcare-information-technology/ehrs/health-systems-moving-to-epic-oracle-in-2026/ | 2026-05-14 | 3 |
| W42 | ホテル向け: IT Brief(IHG が OPERA Cloud を承認)、Nasdaq(Oracle Hospitality)、DBTA(MICROS 買収) | https://itbrief.co.uk/story/ihg-approves-oracle-opera-cloud-for-hotels-globally 、https://www.nasdaq.com/articles/oracle-hospitality-push-highlights-cloud-expansion-whats-ahead 、https://www.dbta.com/Editorial/News-Flashes/Oracle-Expands-Reach-in-Hospitality-and-Retail-with-MICROS-Acquisition-97794.aspx | 2026-01 / 日付不明 | 3 |
| W43 | 銀行向け: Oracle ブログ(FLEXCUBE on OCI)、Retail Banker International(FLEXCUBE V14)、Bank Aston の投稿 | https://blogs.oracle.com/cloud-infrastructure/post/oracle-flexcube-on-oracle-cloud-infrastructure 、https://www.retailbankerinternational.com/news/oracle-unveils-flexcube-v14/ 、https://finchannel.com/?p=25132 | 日付不明 | 1/3/4 |
| W44 | Java SE 価格: Redress Compliance、oraclelicensingexperts | https://redresscompliance.com/oracle-java-licensing-cost-2026-updated-pricing 、https://oraclelicensingexperts.com/blog/oracle-java-se-subscription-pricing-2026/ | 2026 | 4 |
| W45 | MySQL HeatWave: Oracle 価格ページ、Oracle ブログ(コスト比較 2025)、Redress、oraclelicensingexperts | https://www.oracle.com/mysql/pricing 、https://blogs.oracle.com/mysql/mysql-cloud-services-cost-comparison-who-provides-the-best-value-2025 、https://redresscompliance.com/oracle-mysql-heatwave-database-service-cost-model 、https://oraclelicensingexperts.com/blog/oracle-oci-mysql-heatwave/ | 2025〜2026 | 1*/4 |
| W46 | Oracle DB ライセンス価格: Redress、oraclelicensingexperts | https://redresscompliance.com/oracle-price-list-pdf-2026 、https://oraclelicensingexperts.com/how-much-does-an-oracle-database-license-cost | 2026 | 4 |
| W47 | Synergy Research「Q2 Cloud Market Passes $143 Billion」と報道(The Register、DCD) | https://www.srgresearch.com/articles/q2-cloud-market-passes-143-billion-highest-growth-rate-in-eight-years 、https://www.theregister.com/a/5281835 、https://www.datacenterdynamics.com/en/news/enterprise-cloud-infrastructure-spending-hits-143-billion-report/ | 2026-Q3 初頭(Q2 CY2026 の結果) | 3 |
| W48 | Zettascale10: Oracle 発表、DCD、Network World | https://www.oracle.com/ae/news/announcement/ai-world-oracle-unveils-next-generation-oci-zettascale10-cluster-for-ai-2025-10-14/ 、https://www.datacenterdynamics.com/en/news/oracle-unveils-zettascale10-ai-supercomputer-claims-it-will-be-largest-in-the-cloud/ 、https://www.networkworld.com/article/4073420/oracles-big-bet-for-ai-zettascale10.html | 2025-10-14 | 1*/3 |

---

## 8. 未確認事項と検索ログ

### 8-1. 未確認事項(欠損)

| # | 項目 | 試した検索(要旨) | 結果 |
|---|---|---|---|
| 1 | OCI 公式価格表の数字(GPU、計算、保存) | #1、#2(公式価格表を含む検索) | 公式ページは URL のみ。数字は第三者(T4)から取得 |
| 2 | ユニバーサル・クレジット、年次フレックスの条件・割引率 | #2 | 見つからず(割引率は非公表と記載する資料あり) |
| 3 | OCI の GPU の実契約単価、大口契約の課金単位(MW 等) | #1(既存調査 S3 でも未取得) | 欠損 |
| 4 | Dedicated Region の最低コミットの一次情報、導入拠点数、Alloy のパートナー総数 | #3、#20、#26 | 最低額は出典間で食い違い。パートナーは 6 社確認(NRI、Fujitsu、Team IM、stc、du、Ooredoo)。総数は欠損。Vodafone は見出しのみで未確認 |
| 5 | 政府案件(JWCC、Top Secret、NATO) | #26 | 見つからず |
| 6 | 主権クラウドの 2026 年の具体的な顧客名 | #4 | 見つからず |
| 7 | Autonomous Database の顧客名・売上・名称変更後の価格 | #5 | FAQ(旧名称)のみ |
| 8 | Exadata の売上・顧客名・オンプレ価格、C@C 価格の単位 | #5、#19 | C@C の月額は取得したが単位が不明確 |
| 9 | マルチクラウドの現行リージョン数(Azure、Google)と 70 リージョンの確認、絶対売上額、価格 | #6、#18、#25、#28 | AWS 20 のみ公式確認。他は単一出典 |
| 10 | 26ai の発表日、Autonomous での追加費用の有無、導入数 | #7 | 日付なし。Autonomous は未確認 |
| 11 | Fusion の顧客数・顧客名、契約期間、公式価格 | #14、#27 | 欠損(Landbase の 5,000 社は不採用) |
| 12 | Q1 FY27 の NetSuite の公式値・顧客数 | #8、#9、#13、#25、#28 | 見つからず。Q3 FY26 と Q1 FY26 のみ |
| 13 | Oracle Health の売上、買収価格 $28.3B の確認、DoD(MHS Genesis) | #10、#21 | 欠損 |
| 14 | 銀行(FLEXCUBE 等)・小売(Xstore 等)の顧客名・売上・価格 | #15、#22 | 小売は該当なし。銀行は日付のない記事のみ |
| 15 | Java・MySQL・DB サポートの売上、サポート更新率 | #11、#12、#16 | 欠損 |
| 16 | 競合の価格・比較(主権クラウド、DB、ERP の中堅、銀行・小売、Java) | 検索せず(枠の制約) | 「※」を付けて一般的な業界認識を記載 |
| 17 | 10-K の原文(製品説明、顧客数、セグメント注記) | #17 | 要約のみ。FY26 の区分別売上と Cloud Apps 比率 47% を確認 |

### 8-2. 検索ログ(28 回。mode: standard 26、extended 2)

| # | 検索語(要旨) | mode | 主な成果 |
|---|---|---|---|
| 1 | OCI GPU 価格 H100 H200 B200 GB200 | standard | 定価(第三者) |
| 2 | OCI 価格 OCPU、保存、出口、ユニバーサル・クレジット | standard | 保存・出口・無料枠 |
| 3 | Oracle Alloy / Dedicated Region 顧客数・最低コミット | standard | 最低コミットの食い違い |
| 4 | Oracle 主権クラウド、EU、政府、Cloud@Customer | standard | EU 主権クラウドの範囲 |
| 5 | Autonomous Database 価格 ECPU、Exadata C@C | standard | ECPU 価格 |
| 6 | Database@Azure/AWS/Google リージョン、顧客、MACC | standard | Marketplace、MACC |
| 7 | Oracle AI Database 26ai | standard | 追加費用なしの AI 機能 |
| 8 | NetSuite 顧客数、価格、売上 | standard | 価格、Q3 FY26 売上 |
| 9 | Q1 FY2027 Fusion/NetSuite/Health 説明会 | standard | 取得できず(Q1 FY26 が返る) |
| 10 | Oracle Health 売上、VA 契約、DoD | standard | VA 契約 |
| 11 | Java SE 価格 | standard | 価格帯 |
| 12 | MySQL HeatWave 価格 | standard | 価格ページ |
| 13 | Q1 FY27 決算発表(見出し) | standard | 区分別売上 |
| 14 | Fusion 顧客数、価格、シェア | standard | 10-K、シェア推計 |
| 15 | 銀行・小売・ホテル向けアプリ | standard | OPERA/IHG |
| 16 | DB ライセンス価格、サポート 22% | standard | ライセンス価格 |
| 17 | 10-K FY2026 区分別売上 | standard | IaaS $18.1B、SaaS $15.9B |
| 18 | Database@AWS/Google リージョン | standard | AWS 20 |
| 19 | Exadata C@C 顧客、X11M | standard | C@C 月額 |
| 20 | Alloy パートナー一覧 | standard | NRI、Fujitsu、Team IM、stc |
| 21 | Oracle Health 市場シェア(KLAS) | standard | Epic 43.7%、Oracle 21.9% |
| 22 | FLEXCUBE、Retail Xstore | standard | 銀行は日付なしのみ |
| 23 | Synergy Q2 2026 シェア | standard | AWS 28%、Azure 20%、Google 15% |
| 24 | Zettascale10 | standard | 80 万 GPU、2026 年後半 |
| 25 | Q1 FY27 説明会の逐語・マルチクラウド・アプリ | extended | +353%、顧客 +180%、Fusion +14% |
| 26 | Dedicated Region、政府、JWCC | standard | du、Ooredoo、ITHCA |
| 27 | Fusion の従業員あたり価格 | standard | HCM/ERP 価格 |
| 28 | Q1 FY27 説明会のハイライト(NetSuite、Health、70 リージョン) | extended | 再確認、NetSuite・70 リージョンは取れず |
