# W3: AI データセンター産業の構造(ファイブフォースの材料・建設の難しさ・供給量・値下げ圧力)

- 作成日: 2026-10-12 / 対象: Oracle(NYSE: ORCL)再評価の論点「AI クラウド事業の将来の利益率と価値」のうち、産業構造の材料
- 目的: 事実・数値・出典の整理と、出典間の食い違いの指摘のみ。**投資判断・推奨・評価は書かない。**
- 取得手段: WebSearch のみ(**28 回を使い切った**。すべて mode "standard"、"extended" は 0 回)。WebFetch は使えない。**会社の原文・調査会社の原本・報告書の本文は 1 件も直接開いていない。数値はすべて検索ツールの要約に書かれていた内容。**
- Tier: 1=会社開示・決算説明会、2=規制当局・格付会社・中央銀行・公的統計、3=報道・アナリスト・調査会社、4=ブログ・SNS・販促。**`*` は「原本を読まず検索要約経由」**。本書では原本を読めた項目がないため、会社開示由来の数値も `1*`、報道由来は `3*` と書く。調査会社(CBRE・JLL・Epoch・Bain・McKinsey 等)は Tier 3 とした。
- 「(算出)」は調査者の計算で、式を併記した。丸め値(「約」)から計算した値は丸めの誤差を含む。
- 出典 ID `[W3-n]` は「n 番目の検索の要約」を指す(10 節に URL 一覧)。1 回の要約が複数サイトを統合しているため、個別の数値がどの URL 由来かを特定できない場合がある。`[R3]` `[R5]` `[R7]` `[S3]` は既存調査(`/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research2/R3_competition.md` 等、`.../research/S3_scuttlebutt.md`)からの**再掲**で、今回は再検索していない。
- 既存調査(R3・R5・R7・S3)と重複する Oracle・CoreWeave・Nebius の個別数値は再掲に留めた。W1(クラウド利益率の時系列)・W2(GPU 経済寿命)は別担当のため、本書では扱わない。

---

## 0. 要約(事実のみ、10 行)

1. **capex(2026 年)**: 会社ガイダンスは Amazon 約 $220B、Alphabet $195〜205B、Microsoft 暦 2026 年 約 $190B、Meta $125〜145B(別資料 $130〜145B)、Oracle 総額 $90〜95B(純額 約 $70B、FY2027)。5 社合計 $820〜855B(算出、Oracle は総額。基準が揃わない)。集計値は Moody's $785B(CoreWeave 含む)、Morgan Stanley $805B(2026)と $1.116T(2027)。[W3-1](Tier 3*)
2. **容量(GW)**: JLL は北米で建設中 66GW 超・うち 95% が先行契約済み、空室率 1%(2026 年中間)。CBRE の主要市場の空室率は 1.4%(2026 年上期、過去最低)、北バージニア 0.2%。建設中の 80% 超が先行リース済み。[W3-23][W3-4](Tier 3*)
3. **需要予測**: McKinsey は 2030 年に AI 関連 156GW・累計 $5.2T、Bain は 2030 年までに追加の AI 計算 200GW(半分が米国)で、売上 $2T が必要・$800B 不足、Structure Research は AI 容量 150GW(2030 年)。[W3-2][W3-19](Tier 3*)
4. **電力機器**: GE Vernova のガス発電の受注残+枠予約は 116GW(2026-07-22、Q1 は 100GW、2025 年末 83GW)。2031 年納入分を販売中。Siemens Energy の確定受注残 69GW(2026 年 6 月四半期)。納期は新規で約 3 年。大型変圧器は 128〜144 週(WoodMac、2025 Q2)。[W3-5][W3-24][W3-9](Tier 3*)
5. **系統連系**: PJM で 約 40 か月(36〜48 か月)、別資料は 5〜7 年。ERCOT の大口負荷待ち 427GW(別資料 474GW)。**全米平均値は欠損**。[W3-11](Tier 3*〜4)
6. **遅延**: 2026 年に計画された米国データセンターの 3 分の 1〜半分が遅延または中止の見込み(Bloomberg 引用)。Sightline Climate は 2026 年の計画 約 12GW に対し建設中 約 5GW。[W3-21](Tier 3*)
7. **買い手**: OpenAI の計算契約は約 $1.15T〜$1.5T(集計で幅)、2026 年売上見通し $36B、2026〜2030 年の FCF 累計 −$278B。Microsoft の商用 RPO $678B のうち OpenAI は 32%(下限)〜45%。Anthropic の年換算売上は $30B 超(2026-04)で Google/Broadcom の TPU 約 3.5GW を 2027 年から確保。[W3-6][W3-18][W3-27][W3-7](Tier 3*)
8. **価格**: H100 の 1 年契約料は $1.70(2025-10)→ $2.35(2026-03)で +38%(算出)。オンデマンドはどの GPU も売り切れ(SemiAnalysis)。一方、同等性能の推論トークン価格は年 9〜900 倍の速度で下落(Epoch)。賃料は JLL で 2020 年比 約 +70%(年 9%)。[W3-17][W3-16][W3-23](Tier 3*)
9. **資金**: CoreWeave の総債務 $35B(2026-06-30)、GPU 担保ローンは SOFR+2.25%(Moody's A3)、Lambda の TLB は SOFR+3.00%(Baa2)。Meta の Hyperion は $27B の民間債(Blue Owl 80% 出資、Meta は 4 年ごとにリース更新)。民間与信の DC 融資の総額は**欠損**。[W3-22][W3-14](Tier 3*)
10. **歴史の類例**: 2000 年前後の米国光ファイバーは約 $90B(4〜5 年)で敷設、通信会社の債務 約 $650B、使用率 2.6%(Merrill Lynch 推計)、Global Crossing は 2002-01 に負債 $12.4B で破産(ピーク時価 約 $50B)。GDP 比の設備投資は鉄道 6.0%(ピーク)、通信 1.2%(2000 年)、AI 1.2〜2.8%(2024 年、推計幅)。[W3-15][W3-26][W3-20](Tier 3*)

---

## 1. 供給: capex と容量(GW)

### 1-1. 大手の capex(2026 年・2027 年)

| 会社 | 2026 年(会社ガイダンス) | 2027 年 | 時点 | 出典 | Tier |
|---|---|---|---|---|---|
| Amazon | 現金 capex 約 **$220B**(従来 約 $200B から引上げ。主因はメモリ価格上昇)。2026・2027・2028 年とも「需要に容量が足りない」と発言 | 会社ガイダンス**欠損** | 2026 Q2 決算(7 月末) | [W3-1] | 1*/3* |
| Alphabet | **$195〜205B**(従来 $180〜190B)。Q2 単独 $44.9B(前年比 2 倍超)。FCF が会社史上初めて負 | **欠損** | 2026 Q2 決算 | [W3-1] | 1*/3* |
| Microsoft | **暦 2026 年 約 $190B**(1 つの出典)。別資料に FY2027 約 $255B(会計年度で非比較)。四半期で $50B 超とする資料あり | **欠損** | 2026-07-29 | [W3-1][R7] | 3* |
| Meta | **$125〜145B**(別資料 $130〜145B。後者は金融リースの元本返済を含む) | **欠損** | 2026 Q2 決算 | [W3-1] | 3* |
| Oracle(FY2027 = 2026-06〜2027-05) | 総額 **$90〜95B**、純額 約 **$70B**(純額 = AI 顧客が長期契約で前払いする現金を控除) | FY2028 は 約 $102B(MarketScreener 集計、[R5]) | 2026-09-10 | [W3-1][R5] | 1*/3* |
| **5 社合計(算出)** | 下限 220+195+190+125+90 = **$820B**、上限 220+205+190+145+95 = **$855B**。Oracle を純額 $70B にすると $800〜830B。Oracle を除くと $730〜760B | — | — | 算出 | — |
| 集計(Morgan Stanley) | **$805B**(Q1 決算後、従来 $765B) | **$1.116T**(+38.6% = 1,116 ÷ 805 − 1、算出) | 2026 Q1 決算後 | [W3-1] | 3* |
| 集計(Moody's) | **$785B**(CoreWeave を含む) | 「$1T に迫る」。見出しは 2027 年 capex 予想を $85B 引上げ | 2026 年 | [W3-1] | 3* |

- 算出: Amazon の引上げは $220B ÷ $200B − 1 = +10%。Alphabet のレンジ中央値は $185B → $200B(+8.1%)。
- 注: 5 社の会計期間(Microsoft・Oracle は 5〜6 月期末の会計年度)と定義(現金 capex、金融リース、総額か純額か)が揃っていない。2027 年の個別会社ガイダンスは、各社の Q3 決算(10 月下旬)が未発表のため**欠損**。

### 1-2. 容量(GW)の発表・建設中・稼働

| 項目 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| 北米で建設中 | **66GW 超**、うち **95% が先行契約済み**(算出: 66 × 0.95 = 約 62.7GW)。77% は「フロンティア市場」(算出: 66 × 0.77 = 約 50.8GW)。借り手の多くは 2028 年納入分を契約中 | 2026 年中間(JLL) | [W3-23] | 3* |
| 主要 8 市場の新規建設(CBRE) | 2026 年上期に **+24.8%**。建設中の **80% 超**が先行リース済み。残りの空きは 約 6 か月分の需要。総電力は前年比 約 3 分の 1 増。純吸収は +約 12% で **1,456MW**(2026 年上期) | 2026 年上期 | [W3-4] | 3* |
| 2026 年に 1GW 超が稼働する施設 | **5 か所**(各ハイパースケーラー別。Epoch AI、Quartz 経由) | 2026 年 | [W3-2] | 3* |
| Stargate(OpenAI) | 2029 年までに **9GW 超**(Epoch)。別報道は計画 約 7GW・目標 10GW。Abilene は 0.3GW 稼働(Epoch、日付不明。[R7] は 2026-07 に 421MW) | 2026 年 | [W3-2][R7] | 3* |
| Meta Hyperion | 設計 **5GW**、第 1 期 2GW を 2030 年まで(IEEE Spectrum 経由)。Meta は原子力 3 社と計 6GW 超の電力契約(2026-01、[R7]) | 2026 年 | [W3-2][W3-14][R7] | 3* |
| Oracle・CoreWeave・Nebius | Oracle: FY2029 までに 10GW の電力を確保(850MW を Q1 FY27 に納入)。CoreWeave: 稼働 1.5GW・契約 3.7GW(2026-06-30)。Nebius: 契約電力の年末目標 5GW([R7] の再掲) | 2026-06〜09 | [R7] | 1*/3 |
| OpenAI の計算規模 | 2025 年末に「19gw」(URL スラッグの表記。小数点が落ちている可能性があり 1.9GW か 19GW かは**要確認**)。CFO 発言とする DCD の見出し | 2025 年末 | [W3-18] | 3* |
| 世界の AI 容量(予測) | Structure Research: 現在 約 2.3GW → **2030 年 150GW**(「AI 向け容量」の定義は要約に無い) | 2026 年 | [W3-2] | 3* |
| 世界のパイプライン | datacentres.com の見出し「世界のデータセンター容量パイプラインが 25,000MW に」(本文は未読) | 2026-05-25 | [W3-8] | 3〜4 |

- 注: GW の定義(施設電力、IT 電力、契約電力、稼働済み、予定)が出典ごとに違う。上表の数値は**合算していない**(Oracle の確保電力と Stargate、CoreWeave の契約と Meta/OpenAI 向けの重複があるため)。

### 1-3. 需要の予測と需給ギャップの推計

| 出典(予測者) | 予測 | 時点 | 出典 ID | Tier |
|---|---|---|---|---|
| McKinsey | 2030 年に **AI 関連 156GW**、データセンターへの累計投資 **$5.2T**(公表日は要約に無い)。1GW あたり $5,200B ÷ 156GW = **約 $33.3B**(算出。$5.2T が電力等を含むか不明) | 2026 年の引用 | [W3-2] | 3* |
| Bain(2025-09) | 2030 年までに追加の AI 計算要件 **200GW**(米国が半分 = 約 100GW、算出)。2030 年に必要な年間売上 **$2T**、AI による節減を引いても **$800B 不足**。「約 $500B の capex を展開し、約 $2T の新規売上を見つける」(Crawford の発言) | 2025-09 | [W3-19] | 3* |
| Goldman Sachs(2025-02) | 世界のデータセンター電力需要が 2023 年比 **+165%(2030 年)**、2027 年までに +50%。米国は 2025 年 約 31GW → 2026 年 41GW → 2027 年 66GW(要約の記述。範囲は米国全体か AI かの区別が**不明**) | 2025-02 | [W3-3] | 3* |
| EPRI | 米国のデータセンターが 2030 年に全米電力の **9〜17%**(従来の推計は 4.6〜9.1%) | 2026 年の引用 | [W3-3] | 3* |
| IEA(二次ブログ経由) | データセンターの電力消費が 2030 年に 約 **945TWh** へ倍増以上 | 2026 年の引用 | [W3-3] | 2*/4 |
| S&P Global | データセンターの電力需要が 2026〜2030 年に「2 倍超」 | 2026-06 | [W3-2] | 3* |
| Liebreich(Substack) | 2030 年までに追加需要 約 **45GW**(自身の低めの推計。専門家コンセンサスは BCG・McKinsey・EPRI とする) | 2026 年 | [W3-3] | 4 |
| 需給ギャップ(GW) | **明示的な GW ベースの需給ギャップ推計は見つからなかった**。近いものは Bain の売上ギャップ($800B)と CBRE の「空きは約 6 か月分」、JLL の「95% 先行契約済み」のみ。Morgan Stanley の電力不足推計は検索で出ず | — | [W3-19][W3-4][W3-23] | — |

---

## 2. 建設と電力の制約

### 2-1. 系統連系の待ち期間

| 対象 | 待ち期間・規模 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| 全米の発電・蓄電の連系待ち(LBNL "Queued Up") | 約 **2,061GW**(約 8,200 件)、2023 年のピーク 約 2,600GW から約 10% 減。減少の理由は投機案件の撤回(処理速度向上ではない)。**LBNL 原本は未確認** | 2025 年末 | [W3-11] | 2*(二次経由) |
| PJM | 平均 約 **40 か月**。データセンター負荷増の地域では 36〜48 か月(Carbon Direct、2026-05)。別資料は 100MW 超で 5〜7 年、北バージニア(Dominion)約 7 年。構想から稼働まで平均 7 年とする記述も | 2026 年 | [W3-11][W3-9] | 3*/4 |
| ERCOT | 大口負荷の待ち **427GW**(2026-06 の資料)/ **474GW**(別資料)。100MW 超の典型待ち 3〜4 年。75MW 以上は「Batch Zero」で一括審査し、資金保証を要求 | 2026-06〜07 | [W3-11] | 3*/4 |
| 規制 | FERC の大口負荷連系に関する理由提示命令に対し、6 運営者のうち **5 者が期限(8 月 17 日)の延長を要請** | 2026-08 | [W3-11] | 3* |
| 高需要市場の延長幅 | 連系期間が **24〜72 か月**延びたとする分析(1 件、出典の質は低い) | 2026 年 | [W3-21] | 4 |
| 全米平均の待ち年数 | **欠損** | — | — | — |

- 未検証: 「8 月 3 日に Abbott 知事が ERCOT・PUCT の監査まで新規のデータセンター連系を停止」とする記述(electricchoice.com、1 件のみ)。他の出典に無い。

### 2-2. 電力機器の納期(ガスタービン・変圧器)

| 項目 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| GE Vernova(ガス発電の受注残+枠予約) | **116GW**(Q1 100GW、2025 年末 83GW)。年末までに 125GW 以上を見込む。2029 年の空き枠は Q1 時点で約 10GW → 顧客が 2030 年へ移し、2029〜2030 年の合計で約 10GW。**2031 年納入分を販売中**(2026 年末までに半分超を契約の見込み、OilPrice 経由)。新規大型の納期 約 3 年。年間生産 20GW(2026)→ 30GW(2030) | 2026-07-22(Q2 決算) | [W3-5] | 1*/3* |
| Siemens Energy(ガスタービン) | 確定受注残 **69GW**(新規 15GW 受注・6GW 出荷、2026 年 6 月四半期)。納期は全社で 3 年以上。2029〜2030 年納入を既に協議中。ガスタービンの市場は将来年 120GW(半分が米国)と CEO。年間受注は 100GW に向かう | 2026 年 6 月四半期(Q3 FY2026) | [W3-24] | 1*/3* |
| 三菱重工(大型ガスタービン) | 受注残 **35GW**、2024 年比で生産能力を倍増予定 | 2026 年 | [W3-24] | 3* |
| 受注残の滞留年数(算出) | Siemens: 69 ÷ (6 × 4) = **約 2.9 年**(四半期の出荷 6GW を 4 倍)。GE Vernova: 116 ÷ 20(2026 年の年産)= **約 5.8 年**(受注残に枠予約を含む) | — | 算出 | — |
| 3 社の合計(算出) | 116 + 69 + 35 = **220GW**。**世界・全用途で、データセンター向けのみではない**。基準が揃わない | — | 算出 | — |
| 「タービンが制約とは限らない」 | GE Vernova CEO は、EPC・許認可・燃料の方が工程を決めることが多いと発言 | 2026 年 | [W3-5] | 3* |
| 大型電力変圧器の納期 | **128 週**(約 2.5 年、算出: 128 ÷ 52)。発電機昇圧変圧器(GSU)**144 週**(約 2.8 年)(Wood Mackenzie 2025 Q2 調査) | 2025 Q2 | [W3-9] | 3* |
| 変圧器(2026 年) | GSU が **160 週超**(約 3.1 年、算出)(2024 年の平均 143 週から)。高圧変電所用は 2021 年 約 50 週 → 2024 年 120 週 → 2026 年 **140〜160 週超**。FT は最長 4〜5 年。保守業界ブログは 18〜30 か月 | 2026 年 | [W3-9] | 3*/4 |
| 変圧器の単価 | 2019 年比 電力用 **+77%**、GSU **+45%** | 2026 年 | [W3-9] | 3* |
| 業界全体の変圧器納期 | 36 か月(従来 18〜24 か月)([R7] の再掲) | 2026-07 | [R7] | 3〜4 |

### 2-3. 着工から稼働までの期間と遅延

| 項目 | 値 | 出典 | Tier |
|---|---|---|---|
| 着工から 1GW まで | 約 **12〜43 か月**(約 1〜3.6 年)。最大級は「更地から稼働まで 2 年未満」(Epoch)([R7] の再掲) | [R7][W3-2] | 3 |
| Abilene | 2024-06 着工 → 2026-07 に 421MW(25 か月、算出)。建屋 7・8 は 7 月 → 11 月へ後ろ倒し([R7] の再掲) | [R7] | 3 |
| 計画と実績の差 | Bloomberg: 2026 年に計画された米国データセンターの **3 分の 1〜半分**が遅延または中止の見込み。Sightline Climate: 2026 年の計画 **約 12GW** に対し建設中 **約 5GW**、計画容量の **30〜50%** が遅延・中止の恐れ(算出: 5 ÷ 12 = 約 42% が建設中) | [W3-21] | 3* |
| 地域の反対 | Data Center Watch: **45 件以上・約 $68B** が阻止または遅延(2026 Q2)。永久中止だけの数字ではない | [W3-21] | 3* |
| Microsoft のリース | 約 **200MW** の AI データセンターのリースを解約したと報道(会社確認なし) | [W3-21] | 3*/4 |
| Oracle の New Mexico | Stargate の 1 か所が **2029 年**へ(SoftwareSeni)。[R7] は Project Jupiter(Doña Ana)を 2028 年開業目標としており**食い違い**(8 節) | [W3-21][R7] | 3〜4 |
| CBRE の「着工から稼働までの月数」 | **欠損** | — | — |

### 2-4. 労働力

| 項目 | 値 | 出典 | Tier |
|---|---|---|---|
| 電気工の不足 | McKinsey: 2023〜2030 年に AI インフラのため **13 万人**の追加電気工が必要 | [W3-12] | 3* |
| データセンター建設の人手不足 | ITIF: 約 **43.9 万人**(二次引用) | [W3-12] | 3*/4 |
| 電気工事の費用比率 | IBEW の数字として建設費の **45〜70%** | [W3-12] | 3*/4 |
| 養成期間 | 構内配線工の徒弟は現場 **8,000 時間**+座学、通常 **4〜5 年** | [W3-12] | 3*/4 |
| 住宅工事への波及 | Abilene の住宅建設業者:データセンターの採用で電気工の賃金が約 2 倍、工期が約 **2 か月**延びた | [W3-12] | 3* |
| 発言 | NEMA のチーフエコノミスト:多くのハイパースケーラーの律速は電気工・建設労働者の確保。Microsoft の社長が電気工不足を「国内拡張を遅らせる最大の問題」と述べたと報道(日付不明) | [W3-12] | 3* |

### 2-5. 空室率と賃料

| 時点 | 指標 | 値 | 出典 | Tier |
|---|---|---|---|---|
| 2026 年上期 | CBRE: 北米 主要市場の空室率(利用可能電力の割合) | **1.4%**(過去最低)。別資料は「2025 年末に 1.4%」。2025 年上期は 1.6% | [W3-4][W3-8] | 3* |
| 2026 年上期 | CBRE: 北バージニア / シリコンバレー | **0.2%**(前年 0.7%)/ **4.2%** | [W3-4] | 3* |
| 2026 年中間 | JLL: 北米の空室率 | **1%**(「3 年連続」と要約。2025 年中間は 2.3% とする別記述があり**食い違い**) | [W3-23] | 3* |
| 2025 年下期 | CBRE: 250〜500kW の平均希望賃料 | **$196.25/kW・月**(前年比 +6.6%) | [W3-8] | 3* |
| 2026 Q1 | CBRE: 250〜500kW の賃料 | シカゴ **$200〜230**、北バージニア **$190〜235**(/kW・月)。上昇率は前年より緩やか | [W3-8] | 3* |
| 2020〜2026 年 | JLL: 賃料 | 2020 年比 **約 +70%**、年平均 約 **+9%**(算出: 1.09^6 = 1.68)。2030 年まで続く見込み(DCD の二次記事のみ) | [W3-23] | 3* |
| 参考(算出) | $196.25 × 12 = **$2,355/kW・年 = 約 $2.36M/MW・年** | 施設の賃貸料の目安(250〜500kW の小口帯で、ハイパースケールの大口契約とは別。定義が異なる) | 算出 | — |

- 賃料の時系列(年別の表)は**欠損**。JLL・Cushman & Wakefield の $/kW の値は検索で出なかった。

---

## 3. 買い手: 集中度と交渉力の材料

### 3-1. OpenAI

| 項目 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| 売上・費用 | 2026 Q1 の売上 **$5.7B**、費用(operating costs)**$3.7B**(ともに前年比 約 3 倍)。株主向け資料を The Information が報じたものの二次報道。「費用」の定義(売上原価か総費用か)は**不明**のため損益は算出しない | 2026 Q1 | [W3-6] | 3* |
| 売上見通し | **$36B(2026)→ $350B(2030)**(FT が報じた会社資料)。2026 年の残り 3 四半期の平均 = (36 − 5.7) ÷ 3 = **約 $10.1B/四半期**(算出) | 2026-09 | [W3-6] | 3* |
| FCF | **−$278B**(2026〜2030 年累計。5 月時点の見通しは −$305B)。計算・インフラ支出は 2030 年までに約 **$856B** | 2026-09 | [W3-6] | 3* |
| 損失 | 2026 年 約 **$14B** の損失とする流出資料(見出し)。低品質の集計サイトは 2026 年の現金燃焼 約 $27B・損益分岐 2030 年前後 | 2026 年 | [W3-6] | 3*/4 |
| 資金調達 | 2026-03 に **$122B**(コミット額)、post-money **$852B**。新ラウンドの協議 約 **$1.2T** の評価。ある資料は「資本は 2028 年に尽きる」。IPO は延期・2026 年は行わないとする報道が割れる | 2026-03〜09 | [W3-6] | 3* |
| 調達 ÷ 燃焼(算出) | 122 ÷ 278 = **44%** | — | 算出 | — |
| 計算契約の総額 | トラッカー **$1.15T**(2025〜2035)/ 別報道 約 **$1.4T**/ FT 計算 最大 **$1.5T**。**$1.15T ÷ 2026 年売上見通し $36B = 約 32 倍**(算出) | 2026 年 | [W3-18] | 3* |

契約の内訳(トラッカー、推計を含む。会社確認でないものが多い)

| ベンダー | 金額 | 備考 | 出典 | Tier |
|---|---|---|---|---|
| Broadcom | 約 $350B | $35B/GW の仮定による**推計** | [W3-18] | 3*/4 |
| Oracle | $300B | 約 4.5GW・5 年、WSJ 報道(会社は非公表)、開始は 2027 年と報道 | [W3-18] | 3* |
| Microsoft | $250B | 追加の Azure 購入、2025〜2030 年と推定 | [W3-18] | 3* |
| Nvidia | $100B(投資側)| 10GW の Nvidia チップ導入に最大 $350B とする別資料 | [W3-18] | 3* |
| AMD | 約 $90B(推計)| 6GW、最大 1.6 億株を 1 セントで取得できる権利 | [W3-18] | 3*/4 |
| AWS | $38B | 7 年、Nvidia Blackwell | [W3-18] | 3* |
| CoreWeave | 累計 約 $22.4B | 2025-03 の契約+追加 | [W3-18] | 3* |
| Cerebras | 約 $10B(2026-01)/ 別資料 $20B 超 | — | [W3-18] | 3* |
| 上記 7 社の合計(算出) | 350 + 300 + 250 + 100 + 90 + 38 + 22 = **$1,150B** | トラッカーの $1.15T と一致 | 算出 | — |

### 3-2. 他の大口顧客と受注残の集中

| 項目 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Microsoft 商用 RPO | **$678B**(前年比 +84% → 前年は 約 $368.5B、算出: 678 ÷ 1.84)。OpenAI を除くと +25%(CFO Hood)。OpenAI の比率は **約 32%(下限、Webull/Benzinga)**。別の四半期の数字は RPO $625B のうち **$281B(約 45%、算出: 281 ÷ 625)**。Microsoft は OpenAI の残高を開示していない | 2026-07-29(FY2026 Q4) | [W3-27] | 3* |
| Google Cloud 受注残 | **$514B**(Q1 は $462B、[R7])。Google Cloud 売上は +82% | 2026 Q2 | [W3-27][R7] | 3* |
| AWS 受注残 | **$496B**(本文)/ **$364B**(図の注記)(Tunguz 内で食い違い)。3 か月前は $364B とする記述もあり | 2026 Q2 | [W3-27] | 3* |
| 3 社の受注残合計(算出) | 678 + 514 + 496 = **$1,688B**(AWS は $496B を採用。四半期の時点が違う) | — | 算出 | — |
| Oracle RPO | $664B のうち OpenAI 約 45%([R7] の再掲。$300B ÷ $664B) | 2026-08-31 | [R7] | 3 |
| CoreWeave | 最大顧客 36%、第 2 位 26%、第 3 位 10%(2026 Q2、匿名)。Meta は 2026-03 に追加 約 $21B([R7] の再掲) | 2026 Q2 | [R7] | 1*/3 |
| Nebius | Microsoft と Meta で契約収益の約 8 割、RPO の 85%([R7] の再掲) | 2026 Q2 | [R7] | 3 |

### 3-3. Anthropic・Meta・xAI

| 買い手 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Anthropic の売上 | 年換算売上 **$30B 超**(2025 年末は 約 $9B。算出: 30 ÷ 9 = **約 3.3 倍**)。年 $1M 超を支払う顧客は 1,000 社超(2 か月弱で倍増) | 2026-04-06 | [W3-7] | 1*/3* |
| Anthropic の計算契約 | Google/Broadcom の TPU **約 3.5GW**(2027 年から)、2026 年に既に約 1GW を供給(Broadcom の SEC 提出書類とする要約)。金額は非開示。従来の米国計算コミット $50B。AWS Trainium・Google TPU・Nvidia GPU を併用。Broadcom の提出書類は Anthropic の消費が Anthropic の契約継続に依存するリスクを記載(文が途中で切れている) | 2026-04 | [W3-7] | 1*/3* |
| Meta | Google の TPU を複数年でレンタルする契約(The Information 報道)。2027 年から自社データセンター向けに TPU の購入も協議(進捗は不明) | 2026 年 | [W3-13] | 3* |
| Meta のリース条件 | Hyperion の合弁(Blue Owl 80% / Meta 20%)で、Meta は **4 年ごとにリースを更新できる**(NPR) | 2025-12 | [W3-14] | 3 |
| xAI | 売上・調達・契約:**欠損**(検索せず)。Colossus 2 は「12 か月で建設」の予定([R7]) | — | [R7] | 3 |
| 買い手の交渉力の材料(事実のみ) | (a) 上位 1 社が受注残の 3 割超〜半分(Oracle 45%、Microsoft 32〜45%、CoreWeave 36%)。(b) Meta は 4 年更新のリース。(c) OpenAI は Oracle・Microsoft・AWS・CoreWeave・Nvidia・AMD・Broadcom・Cerebras など複数の供給元と契約。(d) Anthropic は 3 種類のチップ・複数クラウドを併用 | — | 上記 | — |

---

## 4. 代替: 自社チップとオンプレ回帰

| 項目 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Google TPU の外販 | Anthropic: 2026 年 約 1GW、2027 年から約 3.5GW。「Broadcom は Google の TPU を 2031 年まで開発」(DCD 見出し)。Meta: レンタル契約、購入を協議。Anthropic への最大 100 万 TPU の従来契約 | 2026-04〜 | [W3-7][W3-13] | 1*/3* |
| Nvidia のシェア | 「AI 計算の約 80%」(出典なし、近似)。Google の TPU 売却の報道で Nvidia 株が 3〜4% 下落(2025 年 11 月の報道とする記述) | 2026 年 | [W3-13] | 3*/4 |
| AWS Trainium / Meta MTIA | **欠損**(今回の検索で数量・GW・契約が出ず)。[R7] に AWS が Trainium に強気とする記事名のみ | — | [R7] | — |
| オンプレ回帰: Cloudera(Wakefield、1,500 人) | 過去 12 か月に AI ワークロードを公衆クラウドからオンプレ・プライベートへ戻した組織 **66%**。推論の実行場所:ハイブリッド 31%、公衆クラウド 30%、プライベートクラウド 22%、オンプレ 8% | 2026-08 | [W3-28] | 4(ベンダー調査) |
| オンプレ回帰: Cloudian(203 人の IT 意思決定者) | **93%** が回帰済み・進行中・検討中。73% が今後 2 年でオンプレ/ハイブリッドへ移行を計画 | 2026-02〜03 | [W3-28] | 4 |
| オンプレ回帰: Broadcom Private Cloud Outlook | 本番の AI 推論を**プライベートクラウドで実行・計画 56%**、公衆クラウド **41%**(前年は 56%)。83% が回帰を検討、半数が一部完了 | 2026 年 | [W3-28] | 4 |
| オンプレ向け GPU 購入量 | **欠損**(IDC・Gartner・サーバーベンダー出荷の数字は出ず) | — | — | — |

- 注: 3 件の調査はいずれもベンダー委託・販促寄りで、「回帰」の定義が異なり、数値を横に比べられない。

---

## 5. 新規参入: ネオクラウドと民間資金

### 5-1. ネオクラウドの調達条件

| 事業者 | 条件 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| CoreWeave | 総債務 **$35B**(2026-06-30)、Q2 の純支払利息 $640M。年率換算 640 × 4 ÷ 35,000 = **約 7.3%**(算出。期末債務で割る概算)。DDTL 4.0:**$8.5B**、変動 **SOFR+2.25%**、2032-03 満期、Moody's A3(2026-03-31 完了)。担保付き GPU ローンの LTV は 60〜70%(分析会社による推計で方法は異なる)。無担保債は 9.6〜9.75%([R7]) | 2026-06〜03 | [W3-22][R7] | 1*/3* |
| Lambda | $926M のシニア担保 TLB:**SOFR+3.00%**、額面の 99.5% で発行、2030-12-31 満期、Moody's **Baa2**。「私募ネオクラウド初の広くシンジケートされた投資適格格付 TLB」。調達協議 最大 $3B・評価 $12B 以上(Bloomberg 二次)。別資料は $4B 調達で IPO は 2027 年 | 2026 年 | [W3-22] | 3* |
| Nscale | 2026-03 の私募ラウンドで評価 **$14.6B**(Nvidia、Blue Owl、Dell、Fidelity、Point72)。IPO 前に $3.36B 調達 | 2026 年 | [W3-22] | 3* |
| Crusoe | 評価 **$10B 超**(2025-10 時点) | 2025-10 | [W3-22] | 3*/4 |
| Fluidstack | 借入枠 最大 **$10B**(Macquarie など。会社は非開示、分析会社の記述) | 2026 年 | [W3-22] | 4 |
| 借り換え | CoreWeave・Nebius・Lambda・Crusoe・Applied Digital の GPU 担保ローン数十 $B が **2026〜2028 年**に満期(分析会社の指摘) | 2026 年 | [W3-22] | 3*/4 |
| スプレッド差(算出) | Lambda SOFR+3.00% − CoreWeave DDTL 4.0 SOFR+2.25% = **75bp** | — | 算出 | — |
| ネオクラウドの社数 | **欠損**(SemiAnalysis ClusterMAX の掲載社数も未取得。[R3] は Platinum が CoreWeave と Nebius の 2 社と記載) | — | [R3] | — |

### 5-2. プライベートクレジット

| 項目 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Meta Hyperion(Louisiana) | **$27B**、「史上最大の民間与信取引」(Dow Jones)。Blue Owl のファンドが合弁の **80%**、Meta が 20%。Morgan Stanley が独占アドバイザー兼唯一のブックランナー。最大の買い手は Pimco。借入は Blue Owl 側のエンティティで Meta のバランスシート外。債権者は資産への直接の遡及権なしとする分析。リースは Meta が 4 年ごとに更新可能 | 2025-12 の報道 | [W3-14] | 3 |
| データセンター向け民間与信の総額 | **欠損**(Morgan Stanley の推計は検索で出ず) | — | — | — |
| マクロ | Brookings(BPEA、2026-10):米国のデータセンター建設は 2025〜2032 年に GDP 比 **平均 3.63%/年**(鉄道・高速道路・通信の過去ブームより大きいと記述) | 2026-10 | [W3-20] | 3* |

---

## 6. 競争と値下げ圧力

### 6-1. GPU レンタル価格(価格のレベルと方向)

| 項目 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| H100 の 1 年契約料(SemiAnalysis 指数) | **$1.70**(2025-10、底)→ **$2.35**(2026-03)= **+38.2%**(算出: 2.35 ÷ 1.70 − 1)(見出しは「約 40%」)。月次の調査(100 者超)による指数 | 2025-10〜2026-03 | [W3-17][W3-10] | 3* |
| 稼働状況 | オンデマンド容量は**全 GPU 種で売り切れ**。保有者は高値でも手放したがらない。Hopper の価格は Blackwell の増産で下がると予想されていたが、H100 の需要は 2025 年末にかけて強まった。2026 年初の需要の主因は画像・動画の生成と二次報道。短期は上昇の見込みでネオクラウドの価格決定力が上がる(SemiAnalysis) | 2026-03 | [W3-17] | 3* |
| 2026-04 以降の 1 年契約料 | **欠損**(検索結果は 2026 年 3 月まで) | — | — | — |
| H100 のオンデマンド | 一般に **$2〜$12/GPU 時**。Vast.ai $1.49〜、RunPod $1.99〜、Lambda $3.99、CoreWeave $4.25、ハイパースケーラー最大 $6.98。AWS は 2025 年 6 月の値下げ:p5.48xlarge $98.32 → $55.04/時 = **−44.0%**(算出: 55.04 ÷ 98.32 − 1。[R3] の数値の再掲) | 2026 年 | [W3-10][R3] | 3*/4 |
| B200 | 2026 年中頃は **$5〜7/GPU 時**。2026-10 は $6.25〜6.89(Modal・RunPod・Lambda)。範囲は 約 $3.70(ネオクラウド)〜 約 $14(AWS) | 2026-10 | [W3-10] | 4 |
| Silicon Data 指数 | 製品ページは確認できたが**数値なし**([R3] の 2026-08-02 の実勢指数は再掲元を参照) | — | [W3-10][R3] | 4 |
| 旧世代 GPU の再契約価格(A100・H100 の 3〜5 年契約) | **欠損**(W2 の担当領域と重なるため追加検索せず) | — | — | — |

### 6-2. 長期契約の単価(1MW・1GW あたり。定義が揃わない参考値)

| 契約 | 年額 / MW(または /GW) | 算出式・出典 | Tier |
|---|---|---|---|
| Oracle × OpenAI | 約 **$13.3M/MW・年** | $300B ÷ 5 年 ÷ 4.5GW([R7] の再掲。WSJ 報道) | 3 |
| Nebius の大型 4 案件 | **$20〜25M/MW・年** | 株主レター要約([R7] の再掲) | 3 |
| CoreWeave の受注残 | **$28.1B/GW**(総額、年額ではない) | $104B ÷ 3.7GW([R7] の再掲) | 3 |
| 会社の例示(Oracle) | 6 年・1GW・$60B = 約 $10M/MW・年 | [R7] の再掲 | 1*/3 |
| 参考(算出) | 施設賃料(2-5 節)約 $2.36M/MW・年に対する比:13.3 ÷ 2.36 = **約 5.6 倍**、25 ÷ 2.36 = **約 10.6 倍** | **対象が違う**(施設の賃料と、GPU・運用を含む計算サービスの売上)。比較は参考のみ | — |

### 6-3. 「計算のデフレ」(同等性能の価格下落)

| 項目 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Epoch AI | GPT-4 級の性能に到達する価格が、博士級の科学問題で **年 40 倍**で低下。6 つのベンチマークで **年 9〜900 倍**。直近 1 年に最速の低下。要因は小型化とハードの費用効率(ほか不明の要因)。2026 年の更新は未確認 | 2025〜2026 | [W3-16] | 3* |
| arXiv(2026-03) | トークン価格が約 **600 倍**低下、廉価帯モデルの価格の半減期 **1.10 年** | 2026-03 | [W3-16] | 3* |
| arXiv(別論文) | 合格あたりコスト(cost-of-pass)が MATH 500 で年 **24.5 倍**、AIME 2024 で年 **3.23 倍**低下 | 2025〜2026 | [W3-16] | 3* |
| Silicon Data LLM Token Expenditure Index | **$0.97/百万トークン**(2026-09-01)。使用量加重の市場指標で、同等能力の比較ではない(KuCoin ブログ、二次) | 2026-09-01 | [W3-16] | 4 |
| 並置(事実のみ) | 「同等性能あたりのトークン価格」は年 3〜900 倍の速度で低下する一方、「H100 の 1 年契約料(GPU 時あたり)」は 2025-10 〜 2026-03 に +38%。測る単位が違う | — | [W3-16][W3-17] | — |

---

## 7. 過剰投資のリスクの材料と歴史の類例

### 7-1. 現在の材料(数値)

| 項目 | 値 | 出典 | Tier |
|---|---|---|---|
| 売上ギャップ | Bain:2030 年に必要な年間売上 $2T、AI による節減を引いても **$800B 不足** | [W3-19] | 3* |
| OpenAI の資金 | 2026〜2030 年の FCF 累計 **−$278B**、調達 $122B(3 節) | [W3-6] | 3* |
| 計算契約と売上の比 | $1.15T ÷ $36B = **約 32 倍**(算出、3-1 節) | 算出 | — |
| Alphabet の FCF | Q2 2026 に会社史上初めて**負**(−$5.9B、[R7]) | [W3-1][R7] | 3* |
| 稼働率の指標(現在) | GPU オンデマンドは売り切れ(2026-03)、空室率 1〜1.4%、建設中の 80〜95% が先行契約済み | [W3-17][W3-4][W3-23] | 3* |
| 担保・借入 | CoreWeave の GPU 担保ローンの LTV 60〜70%、2026〜2028 年に満期集中(5-1 節) | [W3-22] | 3*/4 |
| 設備投資の GDP 比(推計) | AI インフラ **1.2〜2.8%**(2024 年。Tunguz は 1.6%)。Brookings の予測は 2025〜2032 年に平均 **3.63%/年** | [W3-20] | 3*/4 |

### 7-2. 歴史の類例

| 類例 | 数値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| **光ファイバー(米国)**: 敷設量・投資額 | 数十社が約 **4,000 万マイル**を敷設、約 **$90B**(5 年、Deseret 2002)/ 約 $90B(4 年、Tampa Bay Times 2001)。通信会社の債務 約 **$650B**(2001) | 2001〜2002 | [W3-15] | 3* |
| 光ファイバー: 使用率 | Merrill Lynch 推計で使用中は **2.6%**(= 未使用 97.4%、算出)。スポンサー記事は 2002 年に長距離ファイバーの 97.5% が暗(dark)。**ただし「ライト済み(lit)ファイバーは需要とほぼ均衡」と述べるアナリストもいた** | 2001〜2002 | [W3-15][W3-26] | 3*/4 |
| 光ファイバー: 価格 | Band-X:帯域価格は 2001-01 〜 2002-09 に平均 **−44%**。太平洋横断回線は 2001-10 に建設費を下回る約 $1〜1.5M で提示 | 2001〜2002 | [W3-26] | 3* |
| 光ファイバー: 破綻 | Global Crossing は 2002-01 に Chapter 11、負債 約 **$12.4B**、ピーク時価 約 **$50B**。360networks も破産保護申請。通信サービスは 2000〜2001 年の社債デフォルトの先頭(FDIC)。Level 3 は 2002 年に銀行コベナンツ違反の恐れを表明し、のちにピーク時に世界のインターネット通信の 70% を運んだ | 2001〜2002 | [W3-26][W3-15] | 3* |
| 光ファイバー 対 現在の 5 社 capex(算出) | 5 社 2026 年 capex $820〜855B ÷ 光ファイバー全体 $90B = **9.1〜9.5 倍**。名目値で、対象範囲が違う(物価補正なし) | — | 算出 | — |
| **鉄道**: GDP 比 | ピーク **6.0%**(1870 年、Tunguz)。別の記事は 1880 年代 | — | [W3-20] | 3*/4 |
| **通信(2000 年)**: GDP 比 | 約 **1.2%**(別の LinkedIn 投稿は通信・ファイバー 1.1%、鉄道 2.24%、AI 3.63% と基準が異なる) | 2000 | [W3-20] | 3*/4 |
| **シェール**: 累積フリーキャッシュフロー | IEEFA:北米の頁岩系 34 社が 2010〜2019 年に営業 CF を **$189B** 超える投資(全年で FCF 負)。別集計は 29 社で **$184B**(2010〜2019 年前半)。年額の例:2010 年 −$14B、2012 年 −$37.8B(33 社)、2019 年 約 −$2B(34 社)。10 年平均 = 189 ÷ 10 = **$18.9B/年**(算出)。IEEFA は支持団体寄り | 2010〜2019 | [W3-25] | 3*/4 |
| 鉄道: 倒産率・破綻の数値(1873・1893 年) | **欠損**(検索で出ず) | — | — | — |
| 光ファイバー: 「$500B」・価格 −90% | **見つからなかった**(上記の数字に置換) | — | [W3-15][W3-26] | — |

---

## 8. 食い違い(どちらかを採らず併記)

| # | 項目 | 値 A | 値 B | 備考 |
|---|---|---|---|---|
| 1 | 2026 年の大手 capex 合計 | 会社ガイダンスの合算 $820〜855B(算出) | Moody's $785B / Morgan Stanley $805B / ある見出し $725B / 古い記事 $660〜690B | 対象社(CoreWeave を含む)、会計年度、総額/純額が違う |
| 2 | Microsoft の capex | 暦 2026 年 約 $190B(四半期で $50B 超とする記述) | FQ4 $41B([R7])/ FY2027 約 $255B | 暦年と会計年度が混在 |
| 3 | Meta の 2026 年 capex | $125〜145B | $130〜145B(金融リースの元本返済を含む) | 定義 |
| 4 | Oracle の FY2027 capex | 純額 約 $70B | 総額 $90〜95B | 純額 = 顧客前払いを控除 |
| 5 | AWS の受注残 | $496B(本文) | $364B(図の注記) | 同一の記事内で食い違い |
| 6 | Microsoft RPO に占める OpenAI | 約 32%(下限、$678B 中。32% × 678 = 約 $217B、算出) | 約 45%($281B ÷ $625B、別の四半期) | $281B と $217B で金額も合わない。基準・時点が違う |
| 7 | 北米の空室率 | CBRE 1.4%(2026 年上期。別資料は 2025 年末)/ 2025 年上期 1.6% | JLL 1%(「3 年連続」)だが JLL の 2025 年中間は 2.3% とする記述 | 調査範囲(主要市場か北米全体か)が違う |
| 8 | 賃料 | CBRE $196.25/kW・月(250〜500kW) | datacentres.com「卸売 $4.50〜7.50/kW・月」「年 $140〜180/kW」 | 桁が合わない。単位の誤記の疑い(本書は CBRE を採用していない。併記のみ) |
| 9 | 2026 年上期の吸収 | JLL:記録的 **25GW**(1 件の二次要約) | CBRE:純吸収 **1,456MW**(主要 8 市場) | JLL は先行契約・コミットを含む可能性。**範囲不明** |
| 10 | 北米の建設中 | JLL **66GW 超**(全期間のパイプライン) | Sightline **約 5GW**(2026 年に稼働予定 約 12GW に対する建設中) | 対象期間が違う |
| 11 | OpenAI の計算契約総額 | $1.15T(トラッカー、2025〜2035) | 約 $1.4T / 最大 $1.5T(FT)/ $856B(2030 年までの計算・インフラ支出、会社資料) | 範囲・期間が違う |
| 12 | OpenAI の FCF 累計 | −$278B(2026-09) | −$305B(2026-05) | 見通しの更新 |
| 13 | OpenAI の 2026 年損失 | 約 $14B(流出資料) | 約 $27B の現金燃焼(低品質集計) | 損益と現金で別指標の可能性 |
| 14 | H100 の価格の方向 | AWS が 2025-06 に −44%(オンデマンド定価) | 1 年契約料 +38%(2025-10〜2026-03) | 価格の種類が違う |
| 15 | PJM の連系待ち | 約 40 か月(Carbon Direct) | 5〜7 年 / 北バージニア 約 7 年 | 100MW 超か否か、起点の定義 |
| 16 | ERCOT の大口負荷待ち | 427GW | 474GW | 時点 |
| 17 | 変圧器の納期 | 128〜144 週(WoodMac 2025 Q2) | GSU 160 週超(2026 Q1)/ FT 4〜5 年 / 18〜30 か月(保守業界ブログ)/ 36 か月([R7]) | 種類・時点が違う |
| 18 | Stargate の GW | Epoch:2029 年までに 9GW 超 | 別報道:計画 約 7GW・目標 10GW /[R7]の 8.1GW | 定義 |
| 19 | Abilene の稼働 | 0.3GW(Epoch、日付不明) | 421MW(2026-07、[R7]) | 時点の違いと考えられる |
| 20 | Oracle の New Mexico | 2029 年(SoftwareSeni) | 2028 年開業目標([R7]) | 日付不明 |
| 21 | 光ファイバーの使用率 | 2.6%(Merrill Lynch) | 2.5%(97.5% が暗) | 依頼文の「2.7%」は見つからず |
| 22 | 光ファイバーの投資額 | 約 $90B / 5 年(2002) | 約 $90B / 4 年(2001) | 期間の記述が違う |
| 23 | 鉄道のピーク年 | 1870 年(6.0%) | 1880 年代(6%) | 出典 |
| 24 | シェールの累積 FCF | $189B(34 社) | $184B(29 社) | 対象社数 |
| 25 | OpenAI の IPO | 延期(秋の IPO を見送り)| 2026-09-12 に Altman が 2026 年の IPO はしないと発言 / 別資料は 2026-09 の上場可能性 | 時期不明 |

---

## 9. 欠損と試した検索語

| 項目 | 状態 | 試した検索語(番号は 10 節の検索ログ) |
|---|---|---|
| 2027 年の個別会社 capex ガイダンス | 欠損(Q3 決算は 10 月下旬で未発表。集計は Morgan Stanley・Moody's のみ) | 検索 1 |
| SemiAnalysis の容量予測 | 欠損(要約に SemiAnalysis の容量の数字が出ず) | 検索 2 |
| Epoch AI・McKinsey の原本数値 | 二次引用のみ(McKinsey の公表日も不明) | 検索 2・3 |
| GW ベースの需給ギャップ、Morgan Stanley の電力不足推計 | 欠損 | 検索 3・19 |
| 全米平均の連系待ち年数 | 欠損(PJM・ERCOT の地域値のみ) | 検索 11 |
| JLL・Cushman & Wakefield の $/kW、賃料の年別時系列 | 欠損 | 検索 8・23 |
| CBRE の着工から稼働までの月数 | 欠損 | 検索 12 |
| Siemens Energy・三菱重工の原本、Wood Mackenzie 2026 年版の原本 | 二次要約のみ | 検索 9・24 |
| xAI の売上・調達・契約 | 欠損(検索せず) | — |
| OpenAI の 2026 年損失の確定値、売上の通期実績 | 欠損(流出資料・見通し・Q1 のみ) | 検索 6 |
| AWS Trainium・Meta MTIA の数量・契約 | 欠損 | 検索 13 |
| オンプレ向け GPU 購入量 | 欠損 | 検索 28 |
| ネオクラウドの社数 | 欠損 | 検索 22 |
| データセンター向け民間与信の総額 | 欠損 | 検索 14 |
| 2026-04 以降の GPU 1 年契約料、長期契約(3〜5 年)価格、旧世代の再契約価格 | 欠損 | 検索 10・17 |
| 鉄道の倒産率(1873・1893 年) | 欠損 | 検索 25 |
| 光ファイバーの価格 −90% の根拠、$500B の根拠 | 見つからず | 検索 15・26 |
| OpenAI の「19gw」(1.9GW か 19GW か) | 要確認(スラッグのみ) | 検索 18 |

---

## 10. 出典一覧(検索ログ兼用。28 回、すべて mode "standard")

各行:ID、検索語、要約に表示された主な URL(個別の数値がどの URL 由来かは特定できない場合がある)、Tier。

| ID | 検索語 | 主な URL | Tier |
|---|---|---|---|
| W3-1 | hyperscaler capex 2026 2027 Amazon Microsoft Alphabet Meta Oracle total guidance after Q2 2026 earnings | https://datacenterdynamics.com/en/news/moodys-hyperscaler-capex-forecasts-marked-up-by-85bn-to-close-in-on-1trn-by-2027/ ; https://www.fool.com/investing/2026/08/03/microsoft-and-amazon-won-the-ai-spending-week/ ; https://fourweekmba.com/hyperscaler-capex-1-trillion-morgan-stanley/ ; https://www.benefitsandpensionsmonitor.com/news/industry-news/ai-capex-is-booming-but-can-hyperscalers-turn-steel-and-silicon-into-steady-cash/393462 ; https://traderinsightsmedia.beehiiv.com/p/tech-giants-are-spending-725-billion-on-ai-this-year-here-s-who-gets-paid ; https://paasa.com/blog/the-capex-verdict-what-fy-2027-guidance-signals-about-ai-margins | 1*/3*/4 |
| W3-2 | AI data center capacity gigawatts under construction 2026 2030 SemiAnalysis Epoch AI frontier data centers | https://qz.com/ai-data-centers-gigawatt-power-grid-strain-051126 ; https://epoch.ai/topics/data-centers ; https://www.spglobal.com/market-intelligence/en/news-insights/articles/2026/6/s-p-webinar-data-center-power-demand-to-more-than-double-by-2030-102727689 ; https://www.etcentric.org/?p=194421 ; https://www.structureresearch.net/?p=108009 | 3* |
| W3-3 | AI data center power demand forecast 2030 GW McKinsey IEA EPRI Goldman Sachs supply demand gap | https://goldmansachs.com/insights/articles/ai-to-drive-165-increase-in-data-center-power-demand-by-2030 ; https://www.publicpower.org/periodical/article/ai-drive-165-increase-data-center-power-demand-2030-goldman-sachs ; https://www.euci.com/ai-is-poised-to-drive-a-doubling-in-data-center-electricity-demand-by-2030-studies-say/ ; https://mliebreich.substack.com/p/ai-data-centre-power-and-glory-an ; https://www.coradvisors.net/2026/06/ai-data-center-electricity-demand-forecast.html | 3*/4 |
| W3-4 | CBRE North America data center trends H1 2026 vacancy rate record low rental rates per kW | https://www.cbre.com/press-releases/north-american-data-center-demand-continues-to-outpace-supply-despite-record-construction ; https://www.ciodive.com/news/data-center-all-time-low-vacancy-record-construction/829611/ ; https://letsdatascience.com/news/data-center-demand-outruns-record-north-american-constructio-c00300ba | 3* |
| W3-5 | GE Vernova gas turbine backlog slot reservations delivery 2029 2030 Q2 2026 results | https://www.power-eng.com/gas/turbines/data-centers-drive-record-surge-in-ge-vernova-power-equipment-orders-as-turbine-slots-tighten-through-2030/ ; https://arkolith.com/news/news-ge-vernova-gas-turbine-backlog.md ; https://www.nasdaq.com/articles/where-will-ge-vernova-be-10-years ; https://oilprice.com/Energy/Energy-General/The-Gas-Turbine-Shortage-Just-Became-AIs-Biggest-Constraint.amp.html | 1*/3* |
| W3-6 | OpenAI 2026 revenue loss funding round compute commitments $1.4 trillion cash burn | https://aiweekly.co/node/3125 ; https://letsdatascience.com/news/openai-forecasts-278-billion-cash-burn-through-2030-e7b0b3d7 ; https://www.kucoin.com/blog/openai-cash-burn-forecast-278-billion-through-2030-as-compute-costs-hit-856-billion ; https://windowscentral.com/artificial-intelligence/openai-chatgpt/openai-might-torch-14-billion-in-2026 ; https://runtimewire.com/article/openai-278b-cash-burn-1-2t-valuation ; https://dealroom.co/news/other-db5cs1-openai-expects-to-burn-280bn-by-2030/ | 3*/4 |
| W3-7 | Anthropic Google TPU gigawatts deal Broadcom 2026 Anthropic revenue run rate compute commitments Azure AWS | https://thenextweb.com/news/anthropic-google-broadcom-compute-deal ; https://www.theregister.com/2026/04/07/broadcom_google_chip_deal_anthropic_customer/ ; https://datacenterdynamics.com/en/news/broadcom-to-develop-google-tpus-until-2031-anthropic-signs-deal-with-both-companies-for-35gw-of-tpus/ ; https://finance.yahoo.com/sectors/technology/articles/anthropic-google-broadcom-tpu-deal-113234906.html ; https://www.vktr.com/ai-news/anthropic-reveals-30b-revenue-run-rate/ | 1*/3* |
| W3-8 | data center rental rates per kW per month 2026 wholesale colocation pricing JLL Cushman Wakefield North America record | https://www.cbre.com/insights/reports/global-data-center-trends-2026 ; https://encoradvisors.com/data-center-colocation-pricing/ ; https://www.datacentres.com/news/hyperscaler-capex-surge-pushes-global-data-centre-capacity-pipeline-to-25-000-mw-2026-05-25 ; https://www.datacentres.com/news/wholesale-vs-retail-colocation-180b-market-splits-along-diverging-economics-slot3-2026-07-21 | 3*/4 |
| W3-9 | transformer lead times 2026 weeks large power transformers Wood Mackenzie data center interconnection wait years | https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis ; https://www.ajot.com/news/us-power-companies-scramble-to-secure-equipment-as-surging-data-center-demand-strains-supplies ; https://aiweekly.co/alerts/ft-ai-data-center-boom-blows-out-power-transformer-lead-times-from-months-to-4 ; https://oxmaint.com/industries/power-plant/long-lead-item-tracking-for-power-plant-maintenance-projects | 3*/4 |
| W3-10 | H100 GPU rental price per hour 2026 Silicon Data index decline year over year B200 rental price | https://www.silicondata.com/products/silicon-index?gpu=h100 ; https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison ; https://akash.network/the-bid/h100-rental-price-2026-cost-per-hour/ ; https://www.morphllm.com/nvidia-b200 ; https://www.spheron.network/blog/nvidia-b200-cloud-pricing-2026/ ; https://deploybase.ai/articles/nvidia-b200-gpu-hourly-rental-price-where-to-rent | 4 |
| W3-11 | data center grid interconnection wait time years 2026 utility large load queue PJM ERCOT Lawrence Berkeley | https://www.carbon-direct.com/press/carbon-direct-releases-new-analysis-of-power-grid-interconnection-queues-pjm-ercot ; https://www.ascendanalytics.com/blog/large-load-interconnection-queues-data-center-grid-access ; https://capacityglobal.com/news/five-of-six-us-grid-operators-seek-delay-on-fercs-data-centre-power-deadline/ ; https://dchub.cloud/news/2026-06-28-ercot-queue-427-gw-multi-year-wait ; https://www.electricchoice.com/datacenters/interconnection-queue/ | 3*/4 |
| W3-12 | data center construction timeline months groundbreaking to operational electrician labor shortage 2026 skilled trades AI buildout | https://fortune.com/2026/03/02/ai-data-centers-electrician-shortage-gen-z-training-careers/ ; https://www.thinkbrg.com/thinkset/the-data-center-labor-shortage-a-hidden-bottleneck-for-ai-infrastructure/ ; https://www.electricalmarketing.com/market-sales-estimates/national-sales-estimates/article/55339491/nema-sees-solid-growth-in-data-center-utility-grid-construction-through-2027 ; https://explorer.hub71.com/news/feed/data-centers-poach-electricians-from-texas-homebuilders-delaying-construction-by-two-months ; https://www.classet.ai/blog/data-center-construction-staffing-ramp-plans | 3*/4 |
| W3-13 | Google TPU external sales Meta deal 2026 Trainium Meta MTIA custom silicon share of AI accelerators Nvidia market share | https://storyboard18.com/digital/meta-signs-multi-billion-dollar-ai-chip-rental-deal-with-google-90907.htm ; https://www.techradar.com/pro/meta-and-google-could-be-about-to-sign-a-mega-ai-chip-deal-and-it-could-change-everything-in-the-tech-space ; https://hwbusters.com/news/meta-google-ai-chip-a-new-front-opens-against-nvidia/ | 3*/4 |
| W3-14 | private credit data center financing 2026 total billion Blue Owl Meta Hyperion neocloud debt Morgan Stanley estimate $1.5 trillion | https://www.itiger.com/news/1142559708 ; https://www.globaldatacenterhub.com/p/meta-scales-hyperion-to-5gw-and-over ; https://www.wlrn.org/npr-breaking-news/2025-12-05/meta-is-building-a-massive-data-center-why-its-fueling-fears-of-an-ai-bubble ; https://www.theasset.com/article/55209/theasset.com | 3 |
| W3-15 | dot-com fiber optic overbuild 2001 lit fiber utilization 2.7% bandwidth price decline telecom capex $500 billion bankruptcies Global Crossing WorldCom | https://www.tampabay.com/archive/2001/06/23/overbuilding-snares-fiber-optic-industry/ ; https://www.deseret.com/2002/2/8/19636028/is-glut-killing-fiber-optic-firms/ ; https://en.wikipedia.org/wiki/Dark_fibre ; https://www.techfinitive.com/features/the-infrastructure-nobody-wanted-is-the-infrastructure-everyone-uses/ | 3*/4 |
| W3-16 | AI inference price per token decline per year Epoch AI LLM inference price trends 2026 cost of GPT-4 level intelligence fell | https://epoch.ai/data-insights/llm-inference-price-trends ; https://arxiv.org/html/2603.28576v1 ; https://arxiv.org/html/2511.23455v1 ; https://www.kucoin.com/blog/why-ai-token-costs-are-falling | 3*/4 |
| W3-17 | SemiAnalysis GPU rental contract prices rising 2026 H100 one-year contract $2.35 compute shortage sold out | https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity ; https://www.itiger.com/news/1185188896 | 3* |
| W3-18 | OpenAI compute commitments breakdown Oracle $300 billion Microsoft $250 billion AWS $38 billion CoreWeave Nvidia AMD Broadcom Cerebras total 2026 | https://tomtunguz.com/openai-hardware-spending-2025-2035/ ; https://datacenterdynamics.com/en/news/openai-cfo-says-company-ended-2025-with-19gw-of-compute-scaled-revenue-at-same-speed/ ; https://computeprices.com/deals/openai-oracle-2025-09 ; https://www.datacenterdynamics.com/en/news/openai-increases-coreweave-commitment-again-adds-up-to-65-billion/ | 3*/4 |
| W3-19 | Bain $2 trillion annual revenue needed 2030 AI compute shortfall $800 billion; Morgan Stanley data center power shortfall gigawatts 2028 | https://www.scmp.com/tech/tech-trends/article/3326510/ai-industry-faces-us800-billion-revenue-shortfall-amid-data-centre-expansion-bain ; https://www.pymnts.com/news/artificial-intelligence/2025/ai-companies-face-800-billion-dollar-funding-shortfall-bain ; https://tecknexus.com/ai-800b-revenue-gap-compute-power-and-roi-bain-report ; https://www.cityam.com/?p=2370241 | 3* |
| W3-20 | AI capex percent of GDP compared railroads 1850s telecom 1999 2000 peak capex share GDP 2026 comparison | https://tomtunguz.com/llm-impact-gdp/ ; https://www.brookings.edu/wp-content/uploads/2026/10/BPEA-S9E1-financing-the-ai-buildout.pdf ; https://privacy.getcoai.com/?p=95368 ; https://fourweekmba.com/the-ai-capital-expenditure-supernova/ ; https://fr.linkedin.com/in/eliasgaland | 3*/4 |
| W3-21 | data center project delays cancellations 2026 Microsoft lease cancellation Stargate Abilene delay power equipment shortage percent of projects delayed | https://www.techradar.com/pro/if-one-piece-of-your-supply-chain-is-delayed-then-your-whole-project-cant-deliver-nearly-half-of-us-data-centers-planned-for-2026-canceled-or-delayed-and-things-could-soon-get-much-worse ; https://letsdatascience.com/news/us-data-center-opposition-delays-68-billion-projects-16c6814d ; https://www.softwareseni.com/why-so-much-us-ai-data-centre-capacity-is-delayed-or-cancelled/ | 3*/4 |
| W3-22 | neocloud number of providers 2026 financing terms GPU-backed debt Lambda Crusoe Nscale Fluidstack raise billion interest rate | https://www.storagenewsletter.com/?p=305474 ; https://www.fierce-network.com/cloud/neocloud-nscale-raises-336b-ahead-ipo ; https://capacityglobal.com/news/coreweaves-debt-hits-35bn/ ; https://www.peony.ink/blog/neocloud-capital-raise ; https://ai2.work/blog/lambda-s-3b-pre-ipo-round-inside-the-neocloud-race-to-go-public | 3*/4 |
| W3-23 | JLL midyear 2026 North America data center report vacancy rate pipeline under construction GW rental rate trend | https://www.jll.com/en-us/insights/market-dynamics/north-america-data-centers.html ; https://www.networkworld.com/article/4208727/north-american-data-center-vacancy-holds-at-just-1.html ; https://www.datacenterdynamics.com/en/news/jll-data-center-demand-exceeds-expectations-doubles-year-over-year/ ; https://www.bdcnetwork.com/building-sector-reports/data-centers/article/55402995/data-center-demand-likely-to-be-strong-through-at-least-2028 | 3* |
| W3-24 | Siemens Energy gas turbine orders backlog 2026 delivery slots sold out until 2030 Mitsubishi Heavy turbine capacity expansion | https://www.turbomachinerymag.com/view/siemens-energy-posts-record-backlog-joining-ge-vernova-and-baker-hughes-in-a-record-quarter-for-gas-turbines ; https://www.gurufocus.com/news/9006525/siemens-energy-ag-smegf-q3-2026-earnings-call-highlights-record-orders-and-margins-signal-strong-momentum ; https://inspenet.com/en/news/record-orders-for-gas-turbines-boost-siemens/ ; https://energynewsbeat.co/electrical-generation/siemens-gas-turbine-backlog-nears-70-gw-as-company-expands-manufacturing/ | 1*/3* |
| W3-25 | US shale producers cumulative negative free cash flow 2010-2019 billion overinvestment; railroad overbuilding bankruptcies 1893 percent of mileage in receivership | https://ieefa.org/resources/shale-producers-spilled-21-billion-red-ink-last-year ; https://ieefa.org/wp-content/uploads/2019/06/Red-Ink-Keeps-Flowing-for-US-Fracking-Sector_June-2019.pdf ; https://oilprice.com/Energy/Energy-General/A-Gusher-Of-Red-Ink-For-US-Shale.amp.html ; https://es.statista.com/statistics/1127037/us-fracking-companies-free-cash-flow/ | 3*/4 |
| W3-26 | bandwidth prices fell 90% 2001 2002 telecom glut Global Crossing Level 3 market value lost telecom debt default $ billion fiber capacity price collapse | https://www.lightwaveonline.com/business/market-research/article/16648254/bandwidth-price-collapse-will-it-ever-end ; https://www.information-age.com/global-crossing-files-for-chapter-11-bankruptcy-23571 ; https://www.fdic.gov/bank/analytical/bank-trends/bt0205.pdf ; https://om.co/gigaom/the-bankrupt-go-bankrupt/ | 2*/3* |
| W3-27 | cloud backlog RPO Q2 2026 Microsoft commercial RPO OpenAI share AWS backlog Google Cloud backlog customer concentration | https://www.webull.com/news/15317720163771392 ; https://tomtunguz.com/aws-answers-the-cloud-race/ ; https://tomtunguz.com/microsoft-resells-the-frontier/ ; https://cloudwars.com/?p=78788 ; https://tech-insider.org/azure-678-billion-backlog-earnings-2026/ | 3*/4 |
| W3-28 | AI workloads on-premises repatriation 2026 survey enterprise private AI infrastructure share cloud vs on-prem GPU purchases | https://virtualizationreview.com/articles/2026/08/12/cloudera-survey-66-percent-repatriated-ai-workloads-from-public-cloud.aspx ; https://cloudian.com/press/enterprise-repatriating-ai-workloads/ ; https://storagereview.com/news/broadcom-2026-survey-cost-overtakes-security-as-top-public-cloud-concern ; https://campustechnology.com/articles/2026/08/18/survey-organizations-moving-ai-workloads-away-from-public-cloud.aspx | 4 |

既存調査(再掲元): `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research2/R3_competition.md`([R3])、`.../research2/R5_credit.md`([R5])、`.../research2/R7_capital_power.md`([R7])、`.../research/S3_scuttlebutt.md`([S3])。
