# T5: 供給能力と部材の逼迫、価格への転嫁(GPU・アクセラレータ出荷、CoWoS、HBM/DRAM/NAND、サーバー・クラウド価格、GW 計画、電力)

- 作成日: 2026-10-13 / 対象: Oracle(NYSE: ORCL)の AI インフラ事業の需給の見通しのうち、供給側と部材の材料
- 目的: 事実・数値・出典の整理のみ。**投資判断・推奨は書かない。**
- 取得手段: WebSearch のみ(**26 回を使い切った**。すべて mode "standard"、"extended" は 0 回)。WebFetch は使えない。**会社の原文・調査会社の原本・決算説明会の逐語録は 1 件も直接開いていない。数値はすべて検索ツールの要約に書かれていた内容。**
- Tier: 1=会社開示, 2=規制当局・公的統計・系統運用者, 3=報道・アナリスト・調査会社, 4=ブログ・SNS・販促。**`*` は検索要約経由**。本書では原本を読めた項目がないため、会社発言由来も `1*`(要約が会社発言を引用している場合)または `3*`(報道・二次記事経由)と書いた。
- 「(算出)」は調査者の計算で、式を併記した。丸め値から計算した値は丸めの誤差を含む。
- 出典 ID `[T5-n]` は「n 番目の検索の要約」を指す(11 節に検索語と URL)。1 回の要約が複数サイトを統合しているため、個別の数値がどの URL 由来か特定できない場合がある。`[W2]` `[W3]` `[W8]` は既存調査(`/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research3/` の同名ファイル)からの**再掲**で、今回は再検索していない。
- 利用者の比喩(スマホは需要を上回る供給があっても部品・完成品の価格が上がっている)に関する事実は 4 節に分けて整理した。比喩が ORCL に当てはまるかの判断は書かない。

---

## 0. 要約(事実のみ、10 行)

1. **CoWoS(TSMC の先端パッケージ)**: 月産能力の推計は 2026 年末に 115k〜140k ウェハ/月、2027 年末に 150k〜170k 超、2028 年末に 260k(最も強気、二次報道)。同じ時点で推計が 10〜20% ずれる。需要側は Morgan Stanley が 2026 年 1.394M ウェハ → 2027 年 2.694M(+93.3%、算出)。TrendForce は「2.5D パッケージの不足は 2027 年に緩和」と予想。[T5-1][T5-2](3*)
2. **アクセラレータ出荷**: Google TPU は 2026 年 3.2M〜4.6M 個、2027 年 5M(複数社)〜8.84M、2028 年 7M(TrendForce・Jon Peddie)。NVIDIA は 2026 年に Rubin 1.5M〜2.9M 個(推計が約 2 倍ずれる)。AMD は Helios の出荷が 2026 年 Q3 末に始まり 2027 年に増加。AWS Trainium の**台数予測は欠損**。[T5-1][T5-3][T5-19][T5-25](3*)
3. **DRAM・NAND の契約価格(TrendForce)**: 2026 Q1 の汎用 DRAM は前期比 +90〜95%(予測の上方修正)、Q2 のコンシューマー向け DRAM は +45〜50%、Q3 は汎用 DRAM +13〜18%・NAND +10〜15%、**Q4(2026-09-30 公表)は汎用 DRAM +10〜15%、HBM 込みの DRAM +15〜20%、NAND +15〜20%**。上昇率は鈍化しつつ、なお上昇。[T5-4](3*)
4. **メモリの逼迫期間**: SK hynix CEO は 2026-07-10 に「2027 年は供給面で業界史上最悪の年になり得る」「2030 年以降も顧客需要が生産能力を上回る」と発言(Reuters 経由)。Micron は 2026 年 6 月に「逼迫は暦年 2027 年を超えて続く」。UBS は DRAM の供給不足が 2028 年 Q2 まで。HPE CEO は「高い価格は 2027 年に入っても続く」。[T5-6][T5-7][T5-16][T5-11](1*/3*)
5. **HBM**: TrendForce は HBM の混合平均単価(ASP)が 2027 年に前年比 **+121%**(2026-09-29)、UBS は +79%。HBM4 の 2027 年向け提示価格は約 $4 台中盤〜後半/Gb で、HBM3E の約 $1.50/Gb の約 3 倍(算出)。いずれも提示価格・予測で確定契約ではない。[T5-26](3*)
6. **転嫁の実例**: Dell は 2026-03-30 に全製品の定価を約 17% 引上げ、Lenovo は 2026-01-01 に未処理の見積を取消して 10〜15% 高く再提示、HPE は 2025-11・12 月と 2026-01 に値上げし出荷時点までの再価格設定を可能にした。サーバーの BOM(部品原価)の 50% 超が DRAM・NAND(HPE CEO)。Counterpoint はスマホの低価格帯 +約 $30、フラッグシップ +$150〜200 を予想。[T5-8][T5-11](3*)
7. **クラウド・GPU の価格**: AWS の EC2 Capacity Blocks は 2026-01-04 に H200 系で約 +15%(p5e.48xlarge $34.61 → $39.80/時)、2026-07-01 に約 +20%(The Information 経由)。Nebius は 2026-10-01 に H100 $3.85 → $4.50(+16.9%)、B300 $7.85 → $9.50(+21.0%)。Azure・Google Cloud の 2026 年値上げは**確認できず**。Oracle の更新 +20%・CoreWeave 約 +25% は既存調査の再掲。[T5-10][T5-21][W2][W8]
8. **NVIDIA の供給契約(2026-08-26、Q2 FY27)**: 供給コミットメント $279B(前四半期 $119B から +134%、算出: 279 ÷ 119 = 2.34 倍、主にメモリ調達)。粗利率 75.0%、Q4 は 71〜72% に低下見通しで、FY28 は 72〜73%(「実行済みの値上げが Q1 から効く」)。「一部の供給制約」が残ると発言。Q3 売上見通し $108B ± 2%。[T5-13](1*/3*)
9. **容量(GW)と需給**: Morgan Stanley は AI 計算容量が 31GW → 117GW(2028 年、約 3.8 倍、算出: 117 ÷ 31)。米国の 2026〜2028 年の新規電力需要 68GW に対し手当済み 30GW・未解決 38GW(同社、2026-08)。別の要約は総ギャップ 57GW・オンサイト発電控除後 32GW。需給の均衡時期は Goldman が 2028 年(従来の 2027 年末から後ろ倒し)。[T5-12][T5-15][T5-24](3*)
10. **電力の公的データ**: PJM の 2028/29 年度の容量オークション(2026-07-14)は価格上限 $325/MW-日で 3 回連続、信頼度要件に **6,831MW 不足**(算出: 不足割合 6,831 ÷ 149,182 = 4.6%)。2027/28 年度は 6.6GW 不足。Microsoft は容量制約を「少なくとも 2026 年 6 月まで」と述べ(2025-10)、2026-07 の決算でも制約下。[T5-22][T5-17](2*/3*)

---

## 1. 年×指標の表(2025〜2030 年)

注: 空欄は「欠損」。同じ行でも出典によって定義が異なる(能力 vs 需要、年末時点 vs 年間、会社 vs 調査会社)。数値の根拠は 2〜10 節。

| 指標 | 2025 | 2026 | 2027 | 2028 | 2029〜2030 |
|---|---|---|---|---|---|
| CoWoS 月産能力(千ウェハ/月、年末時点) | — | 115(JPM、2026-01)〜140(EDN 経由、2026-06)。約 130(EDN 経由、2026-09) | 150〜170 超(KGI 170、2026-03) | 260(EDN 経由、2026-09、二次) | 欠損 |
| CoWoS 年間(百万ウェハ) | — | 需要 1.394(MS、2026-07)/ 能力 0.65(KeyBanc) | 需要 2.694(MS)/ 能力 0.84(KeyBanc) | 欠損 | 欠損 |
| NVIDIA GPU(百万個) | — | KeyBanc の容量試算: Blackwell 5.5〜6 + Rubin 1.5 + Hopper 1 = 8.0〜8.5(算出)。別の証券会社: 総計約 6.3(うち Rubin 約 2.9) | NVIDIA の CoWoS 割当 1.222M ウェハ(45%、MS)。**台数は欠損** | 欠損 | 欠損 |
| Google TPU(百万個) | — | 3.2(MS)/ 3.3(DigiTimes)〜4.6(BofA)/ 約 4(Jon Peddie)/ 4.504(GF) | 5(MS・TrendForce・Jon Peddie)/ 8.84(GF) | 7(TrendForce・Jon Peddie) | 欠損 |
| Broadcom の TPU 関連需要(GW) | — | 欠損 | 5 | 10 | 欠損 |
| AMD の MI4xx | — | Helios の出荷は Q3 末に開始。OpenAI の最初の 1GW は 2026 年下期 | MI455 約 1M + MI450 約 0.5M 個(MS)。AMD の CoWoS 割当 240k ウェハ。Anthropic の最初の 1GW は 2027 年上期 | 欠損 | 欠損 |
| AWS Trainium(台数) | 欠損 | 欠損(Trainium3 の増産は 2027 年初に及ぶ可能性、DigiTimes の断片) | 欠損 | 欠損 | 欠損 |
| DRAM 契約価格(前期比) | — | Q1 汎用 +90〜95%(予測)/ Q2 コンシューマー +45〜50% / Q3 汎用 +13〜18% / Q4 汎用 +10〜15%(HBM 込み +15〜20%) | 欠損(HBM の ASP は +121% 予測) | 欠損 | 欠損 |
| NAND 契約価格(前期比) | — | Q1 モバイル NAND +90% 超(Counterpoint)/ Q3 +10〜15% / Q4 +15〜20% | 欠損 | 欠損 | 欠損 |
| HBM 市場規模(十億ドル) | 約 35(Micron) | 50.5(Meticulous)〜54.6(ChipPub) | 欠損 | 約 100(Micron の TAM) | 欠損 |
| HBM の平均単価 | — | HBM3E 約 $1.50/Gb(提示) | 前年比 +121%(TrendForce)/ +79%(UBS)。HBM4 提示 $4 台中盤〜後半/Gb | 欠損 | 欠損 |
| メモリの需給の状態 | — | HBM は 2026 年分を売り切れ | SK hynix CEO「業界史上最悪の供給年」。DRAM 供給は需要の約 60%(Nikkei 経由)。割当は要求量の 60〜70%(単一出典) | UBS: 2028 年 Q2 まで供給不足 | SK hynix CEO「2030 年以降も需要が能力を上回る」 |
| GPU 時間単価の動き | — | H100 1 年契約 $1.70 → $2.35 → 約 $2.65 [W2]、AWS Capacity Blocks +15%・+20%、CoreWeave 約 +25%、Nebius +17〜21%、Oracle 更新 +20% | 欠損 | 欠損 | 欠損 |
| AI 計算容量(GW、世界) | 31(MS、基準年は 2026 年初と推定せず、要約は「31GW から」と記述) | — | — | 117(MS) | 欠損 |
| 米国の電力ギャップ(GW) | — | — | 15 以上(Musk、2027 年)/ PJM −6.6(2027/28) | 2026〜2028 年累計: 必要 68、手当済み 30、未解決 38(MS)/ 総 57・純 32(別の要約)/ PJM −6.8(2028/29) | 欠損 |

---

## 2. アクセラレータの出荷と CoWoS

### 2-1. TSMC の CoWoS 能力の推移(ウェハ/月)

| 出典(時点) | 内容 | Tier |
|---|---|---|
| JPMorgan(2026-01) | 2026 年末 約 **115k**/月(TSMC)。ASE・Amkor が追加で 12k〜15k。別の古い(日付不明)メモは 2026 年末 95k・2027 年末 112k | 3* [T5-2] |
| KGI(2026-03-09) | 2027 年末の見通しを 155k → **170k**/月に引上げ。理由は土地・人員・クリーンルームの制約 | 3* [T5-2] |
| Morgan Stanley(2025-11) | 120k〜130k/月 | 3* [T5-2] |
| Economic Daily News 経由 TrendForce(2026-06) | TSMC 単体 **120k〜140k**/月(2026 年)。OSAT 込みで業界は 200k に接近。TrendForce は 2.5D パッケージの不足が **2027 年に緩和**、TSMC は 2027 年までに CoWoS を 60% 超拡張と予想 | 3* [T5-2] |
| Economic Daily News 経由(2026-09) | 2026 年末 約 **130k** → 2028 年末 **260k**(2 倍、算出: 260 ÷ 130)。最も強気、二次報道 | 3* [T5-2] |
| TSMC(2026 年 5 月のシンポジウム、Reuters 経由) | CoWoS の能力は 2022〜2027 年に CAGR **80% 超** | 1*/3* [T5-2] |
| KeyBanc | 2026 年の能力 **650k ウェハ**、2027 年 **840k**(+29.2%、算出: 840 ÷ 650 − 1)。2026 年は Blackwell 5.5〜6M 個 + Rubin 1.5M + Hopper 1M を支える試算(合計 8.0〜8.5M、算出) | 3* [T5-1] |

### 2-2. CoWoS の需要(ウェハ/年)

| 出典 | 内容 | Tier |
|---|---|---|
| Morgan Stanley(2026-07) | 世界の CoWoS 需要 2026 年 **1.394M** → 2027 年 **2.694M**(+93.3%、算出: 2.694 ÷ 1.394 − 1)。NVIDIA は 2027 年に 1.222M(45.4%、算出: 1.222 ÷ 2.694)。2026 年の NVIDIA の予約は以前の推計で 約 595k | 3* [T5-1] |
| TSMC 調査(アナリスト) | 2027 年の追加 CoWoS 供給は NVIDIA・Broadcom 向けに各 約 100k、拡張の大半は 2027 年下期 | 3* [T5-1] |
| AMD | 2027 年の CoWoS 割当 約 **240k** ウェハ(報道) | 3* [T5-1] |

- 注: 「年末の月産能力 × 12」(例 130k × 12 = 1.56M、算出)と「年間需要 1.394M」は、年末時点と年間平均の違いがあり、直接の比較はできない。MS の需要と KeyBanc の能力(0.65M)は定義が大きく異なる(8 節)。

### 2-3. 個別アクセラレータの出荷予測

**NVIDIA**

| 項目 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Rubin の 2026 年の台数(KeyBanc) | 2.0M → **1.5M**(HBM4 の SK hynix での認定が遅れたため。Rubin ラックは 12k〜14k → 約 6k)。後の 2026-07 のメモは「わずかな遅れ。B300 の追加出荷で相殺」 | 2026-04 / 2026-07 | [T5-25] | 3* |
| Rubin の 2026 年の台数(別の証券会社) | **約 2.9M**、NVIDIA の AI GPU 総出荷 約 **6.3M** | 日付不明 | [T5-1] | 3* |
| KGI | Rubin 系の 2026 年 CoWoS 出荷は NVIDIA の割当の**半分未満**(SK hynix の HBM4 供給制約) | 2026-03-09 | [T5-1] | 3* |
| SK hynix の HBM4 | 当初目標より出荷を **20〜30% 削減**(Rubin の遅れ、ZDNet 経由) | 2026-04 | [T5-23] | 3* |
| TrendForce | 2026 年の NVIDIA の高性能 GPU に占める Rubin の比率 29% → **22%** に低下 | 日付不明(2026 年初〜4 月と推定せず) | [T5-23] | 3* |
| NVIDIA の発言 | 遅れの報道は誤り・Rubin は予定通り。**2026-08-26**: Vera Rubin は「フル生産」、Blackwell と Rubin の両方を出荷、「一部の供給制約」は残る | 2026-04〜08 | [T5-23][T5-25][T5-13] | 1*/3* |
| 未検証 | TrendForce のレポート題名「NVIDIA Rubin Ramp Delayed to 2027 on HBM Snag」(URL コード RP260921NC3)が検索結果に出たが、**本文は未確認**。別の検索では「Rubin が 2027 年に遅れる」とする出典は見つからなかった | — | [T5-1][T5-25] | 3(題名のみ) |
| Kyber NVL144 | SemiAnalysis が「12 か月超遅れて 2028 年」と報じた(二次) | 日付不明 | [T5-25] | 3* |
| 2027 年・2028 年の台数 | **欠損** | — | — | — |

**Google TPU**

| 出典 | 2026 | 2027 | 2028 | Tier |
|---|---|---|---|---|
| Morgan Stanley | 3.2M | 5M | — | 3* [T5-3] |
| TrendForce | — | 5M | 7M | 3* [T5-3] |
| Jon Peddie | 約 4M(従来の約 2M から引上げ) | 5M | 7M | 3* [T5-3] |
| GF Securities(強気ケース) | 4.504M | 8.84M(+96.3%、算出: 8.84 ÷ 4.504 − 1) | — | 3* [T5-3] |
| 2026 年の範囲 | 3.3M(DigiTimes、CoWoS 制約のため)〜4.6M(Bank of America) | — | — | 3* [T5-3] |
| Piper Sandler(Broadcom 経営陣の話の要約) | — | **5GW** | **10GW** | 3* [T5-3] |

- 算出: Morgan Stanley の 2026 → 2027 年は +56.3%(5 ÷ 3.2 − 1)、TrendForce の 2027 → 2028 年は +40.0%(7 ÷ 5 − 1)。
- 注: 見出し「Google TPU Volume Could Triple to 8.8 Million by 2027」(247wallst、2026-08-25)は「3 倍」と書くが、GF の 2026 年 4.504M との比は 1.96 倍(算出: 8.84 ÷ 4.504)。「3 倍」の基準年は不明(8 節)。
- Anthropic への TPU 約 3.5GW(2027 年から)は [W3] の再掲。

**AMD**

| 項目 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Helios(MI450) | 「フル生産」。出荷は **Q3 末に開始**し 2027 年に増加(Lisa Su、Advancing AI 2026) | 2026 年 | [T5-19] | 1*/3* |
| OpenAI 6GW | 最初の 1GW(MI450)は 2026 年下期。OpenAI は「年末に向け大規模に開始し 2027 年を通じて加速」 | 2026 年 | [T5-19] | 1*/3* |
| Anthropic(最大 2GW) | 最初の 1GW の出荷は **2027 年上期**。データセンターの準備次第で 2027 年に前倒し | 2026 年 | [T5-19] | 3* |
| Meta(追加 6GW) | 複数世代の Instinct。出荷は 2026 年下期に開始予定 | 2026 年 | [T5-19] | 3* |
| 台数(Morgan Stanley) | 2027 年に MI455 約 **1M**、MI450 約 **0.5M** 個 | 2026-07 | [T5-1] | 3* |
| 四半期別の台数・売上 | **欠損** | — | [T5-19] | — |

**AWS Trainium**

| 項目 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Trainium3 の時期 | Amazon は 2025-10 に「年末にプレビュー、本格的な量は 2026 年初」。Digitimes(2026-06-23、断片のみ)は Trainium3 サーバーの量産、出荷増は 2027 年初に及ぶ可能性 | 2025-10〜2026-06 | [T5-5] | 1*/3* |
| AWS の ASIC 出荷(TrendForce) | 2025 年に 2 倍超、2026 年は約 +20%(日付不明。全自社チップの合計) | 日付不明 | [T5-5] | 3* |
| Project Rainier | Trainium2 約 50 万個で稼働(出典により 2024 年末/2025 年末と食い違い)。100 万個への拡張目標とする記述あり(低信頼度の出典) | 2025 年 | [T5-5] | 3*/4 |
| AWS の容量 | Jassy:「2027 年末までに容量が 2 倍」(二次引用) | 2026 年 | [T5-5] | 3* |
| 自社チップのランレート | $20B 超(2026 Q1)/ $25B 超(2026 Q2)[W8] の再掲 | 2026 年 | [W8] | 3* |
| Trainium の台数予測(2026〜2028 年) | **欠損** | — | — | — |

### 2-4. NVIDIA の決算(2026-08-26、Q2 FY2027、四半期末 2026-07-26)

| 項目 | 値 | 出典 | Tier |
|---|---|---|---|
| 売上 | **$96.2B**(前年比 +106%、前期比 +18%)。データセンター $89.0B(+117%) | [T5-13] | 1*/3* |
| GAAP 粗利率 | **75.0%**(Q1 74.9%、前年同期 72.4%) | [T5-13] | 1*/3* |
| Q3 見通し | 売上 **$108.0B ± 2%**(+12.3%、算出: 108 ÷ 96.2 − 1)、粗利率 74.0% ± 50bp。中国向けデータセンター計算の売上は含まない | [T5-13] | 1*/3* |
| 粗利率の見通し(CFO) | Q4 に **71〜72%** で底、FY2028 は **72〜73%**。「実行済みの価格引上げが Q1 から効く」 | [T5-13] | 1*/3* |
| 供給コミットメント | **$279B**(前四半期 $119B。主にメモリ調達)。「クラウド契約・リース・投資を含む総コミットメント 約 $366B」とする記述あり | [T5-13] | 1*/3* |
| 供給制約 | 「一部の供給制約(certain supply constraints)」が残る。Vera Rubin は「会社史上最速の立上げ」 | [T5-13] | 1*/3* |
| 注 | KuCoin の要約は題名に「$3.66 Trillion」、本文に「$100B 見通し」「$260B 株主還元」と書くが、他の出典(売上見通し $108B、還元 $26.0B)と合わず、誤記と考えられる(8 節) | [T5-13] | 4 |

---

## 3. メモリ(HBM・DRAM・NAND)の需給と価格

### 3-1. 契約価格の推移(TrendForce)

| 期 | 汎用 DRAM | 他 | 出典 | Tier |
|---|---|---|---|---|
| 2026 Q1 | 予測を **+55〜60%** → **+90〜95%**(前期比)に上方修正。Counterpoint: モバイル DRAM が前期比 +50% 超、NAND が +90% 超 | Samsung の 32GB DDR5 モジュールが $149 → $239(+60.4%、算出: 239 ÷ 149 − 1) | [T5-8][T5-11] | 3* |
| 2026 Q2 | コンシューマー DRAM が前期比 **+45〜50%**(生産能力の制約と注文の移転、2026-04) | — | [T5-4] | 3* |
| 2026 Q3 | **+13〜18%** | NAND **+10〜15%** | [T5-4] | 3* |
| 2026 Q4(2026-09-30 公表) | **+10〜15%**。HBM 込みの DRAM 全体は **+15〜20%** | NAND **+15〜20%**。サーバー向け DRAM の不足は続く。PC 向け DRAM の Q4 見通しは +0〜5% → **+3〜8%** に上方修正。NAND は AI 向け需要が増える一方でコンシューマー需要は弱い | [T5-4] | 3* |
| 累計(参考、算出) | Q1 〜 Q4 の中央値を連乗: 1.925 × 1.475 × 1.155 × 1.125 = **約 3.7 倍**。下限(1.90 × 1.45 × 1.13 × 1.10)= 3.4 倍、上限(1.95 × 1.50 × 1.18 × 1.15)= 4.0 倍 | **注意**: Q1 は予測値、Q2 は「コンシューマー DRAM」、Q3・Q4 は「汎用 DRAM」で、**分類が揃わない**。2025 年末の水準を 1 とした目安にすぎない。別の見出し「DRAM prices in 2026 have doubled」(softwareseni)は「2 倍」 | 算出 / [T5-8] | — |
| スポット | Micron の決算前の記事で DRAM スポットが 1 月比 **+52%** | — | [T5-7] | 3* |

- Q4 の HBM 単独の価格上昇率は検索で出なかった(欠損)。

### 3-2. HBM

| 項目 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| 混合 ASP の 2027 年見通し | TrendForce: 前年比 **+121%**(2026-09-29)。UBS: **+79%**。TrendForce(2026-08): 2027 年の契約価格 **+50% 超** | 2026-08〜09 | [T5-26] | 3* |
| 提示価格(2027 年向け) | HBM4 は **$4 台中盤〜後半/Gb**、HBM3E は約 **$1.50/Gb**(約 3 倍、算出: 4.5 ÷ 1.5。**確定契約ではなく提示価格**) | 2026 年 | [T5-26] | 3* |
| スタック当たり | HBM3 約 $200、HBM3E 約 $300、HBM4 約 $500(推計、ラベルは estimate)。**36GB(288Gb)× $4.5/Gb = $1,296**(算出)と合わない(8 節) | 日付不明 | [T5-26] | 4 |
| スポット対長期契約 | 36GB の HBM3E が現物で 約 **$2,100**、長期契約の通常価格は $300〜400 | 日付不明 | [T5-26] | 3*/4 |
| 市場規模 | Micron: 2025 年 約 $35B → 2028 年 約 **$100B**(年 約 40%、算出: (100 ÷ 35)^(1/3) − 1 = 41.9%)。2026 年は $50.5B(Meticulous)/ $54.6B(ChipPub) | 2025〜2026 年 | [T5-26] | 3*/4 |
| 2027 年の交渉 | 2027 年の契約交渉は 2026 年 6 月から進行(TrendForce)。Samsung は NVIDIA・Broadcom との 2027 年 HBM4 供給交渉が最終段階。見出し「Samsung HBM4 2027 pricing set to more than double 2026」(siliconanalysts、2026-10-07、本文未確認) | 2026-06〜10 | [T5-26] | 3*/4 |
| 供給の売り切れ | HBM は 2026 年分を売り切れ。3 社が 2027 年の DRAM・HBM 生産を割当済みとする報道(出所不明の業界筋、DigiTimes 等) | 2026 年 | [T5-6][T5-7] | 3*/4 |

### 3-3. メーカーの決算・発言

| 会社 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Micron(FQ4 2026、四半期末は 9 月上旬、決算 2026-09-30) | 売上 **$54.23B**(前年比 +379%、LSEG 予想 $51.07B)。DRAM は $39.77B(73.3%、算出: 39.77 ÷ 54.23)。前年同期は 約 $11.3B(算出: 54.23 ÷ 4.79)。FQ1 2027 見通し **$61.5B**(+13.4%、算出: 61.5 ÷ 54.23 − 1)。CFO: DRAM の出荷ビットは**一桁%増**、価格は**「10% 台後半」**上昇 | 2026-09-30 | [T5-7] | 1*/3* |
| Micron CEO | 2026 年 6 月:「逼迫は暦年 2027 年を超えて続く」。別の二次記事は「少なくとも 2028 年まで」 | 2026-06 | [T5-7][T5-24] | 1*/3* |
| Micron(9 月の決算説明会) | 2027 年の供給と HBM の売上・価格目標の明示は**欠損** | — | [T5-7] | — |
| Samsung(2026 Q3 暫定、2026-10-08) | 営業利益 **107.4 兆ウォン**・売上 **195 兆ウォン**(営業利益率 55.1%、算出: 107.4 ÷ 195)。前年同期 12.17 兆ウォンの 8.8 倍(+782.5%、算出: 107.4 ÷ 12.17 − 1)。初の 100 兆ウォン超。事業別の内訳は非開示で、アナリストは**メモリ単独で約 110 兆ウォン**と推計(全社を上回る = 他事業が赤字の計算、推計値)。DRAM 価格の上昇は前四半期より鈍化したが二桁。確定決算・説明会は **2026-10-29** | 2026-10-08 | [T5-9] | 1*/3* |
| SK hynix CEO(Kwak Noh-jung) | 2026-07-10(Reuters):「2027 年は供給面で業界史上最悪の年になり得る」「**2030 年以降も顧客需要が生産能力を上回る**」。別の記事は「HBM は 2027 年まで需要に対し逼迫」(2025-10) | 2026-07 | [T5-6] | 1*/3* |
| UBS | DRAM は少なくとも **2028 年 Q2** まで供給不足 | 2026 年 | [T5-6] | 3* |
| Bank of America(二次引用) | 技術・建設の制約で、SK hynix の 2028 年までの追加能力は計画の **6 分の 1** にとどまる | 2026 年 | [T5-6] | 3*/4 |
| SK Group 会長(低信頼度の出典) | 「逼迫は 2030 年まで」。メーカーが 2027 年に満たせるのは需要の 60% | 日付不明 | [T5-16] | 4 |
| HPE CEO(Neri) | 「高い(elevated)メモリ価格は **2027 年に入っても**続く」 | 2026 年 | [T5-11] | 1*/3* |
| IDC | メモリ不足は「2027 年に入っても」続く | 2026 年 | [T5-8] | 3* |

### 3-4. メモリの供給側の容量計画

| 会社 | 内容 | 出典 | Tier |
|---|---|---|---|
| Micron | 最初の波は 2027 年(シンガポールの HBM パッケージ、Idaho ID1、Tongluo)。次の大きな追加は **2028 年下期**。別の記事は Idaho の最初のウェハ出荷が 2027 年半ば、第 2 工場が 2028 年末 | [T5-16] | 3* |
| Samsung | 平沢 P4 は 2026 年稼働だが量産は 2027 年以降。P5(HBM 向け)は 2028 年以降 | [T5-16] | 3* |
| SK hynix | 清州 M15X を 2026 年 2 月に開所。龍仁(Yongin)の日程を 3 か月前倒しして **2027 年 2 月** | [T5-16] | 3* |
| 産業全体 | Counterpoint: 2027 年まで年 **12%** の出力増が必要に対し計画は約 **7.5%**。Nikkei(二次):DRAM 供給は 2027 年まで需要の約 **60%**。3 社の 2027 年割当で顧客は要求量の **60〜70%**(単一出典) | [T5-16] | 3*/4 |
| 新規能力の用途 | 新規能力の多くはサーバー DRAM と HBM 向けで、コンシューマー向けではない(BuySellRAM) | [T5-16] | 4 |
| 留意 | メモリは過去に好不況を繰り返し、新工場の稼働後に価格が大きく下がった歴史があるとのアナリストの警告(記事内) | [T5-16] | 3* |

---

## 4. 価格への転嫁の実例(スマホ・PC・サーバー・AI サーバー)

### 4-1. スマホ・PC

| 項目 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| PC 各社 | Lenovo・Dell・HP・Acer・ASUS が **15〜20%** の値上げを表明とする集計 | 2026 年 | [T5-8] | 3* |
| IDC(PC 出荷) | 2026 年は基準で **−4.9%**、DRAM 不足が悪化すれば最大 **−8.9%**。別の記事は IDC の見通しを **−11.3%** と記述(食い違い) | 2025 年末〜2026 年 | [T5-8] | 3* |
| Counterpoint(スマホ出荷) | 2026 年は **−2.1%**(1 件)/ **−12%** で「記録上最大の減少」(別の集計。食い違い) | 2026 年 | [T5-8] | 3* |
| Counterpoint(スマホ価格) | 低価格帯の小売価格 **+約 $30**、フラッグシップ **+$150〜200** | 2026-03 | [T5-8] | 3* |
| 影響の差 | 低採算の Android 各社が最も影響を受け、Apple・Samsung は比較的影響が小さい(Counterpoint) | 2026 年 | [T5-8] | 3* |
| 見出し(本文未確認) | 「Memory shortages raise PC, smartphone prices 8% in 2026」(TechSpot) | 2025 年末 | [T5-8] | 3 |

### 4-2. サーバー

| 項目 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Dell | 全製品の定価を約 **17%** 引上げ。COO は値引きの圧縮と見積の有効期間の短縮にも言及 | 2026-03-30 | [T5-11] | 1*/3* |
| HPE | 2025-11・12 月と 2026-01 に値上げ。**出荷時点まで注文の再価格設定が可能**。DRAM と NAND が従来型サーバーの BOM の **50% 超**。値上げで需要は減速していない(Neri) | 2025-11〜2026-01 | [T5-11] | 1*/3* |
| Lenovo | 2026-01-01 に未処理の見積を全て取消し、**10〜15% 高く**再提示 | 2026-01-01 | [T5-11] | 3* |
| 一般 | メモリは典型的なサーバー BOM の最大 **25%**(メモリ重視の仮想化ホストではそれ以上)。サーバー全体の値上げは約 **15%**(TechRadar) | 2026 年 | [T5-11] | 3*/4 |
| Supermicro | 公式の値上げ発表は**確認できず**。Reddit の個人投稿(60% 値上げ、未検証)のみ | 2026-05 | [T5-11] | 4 |
| AI サーバーへの転嫁率 | メーカーが AI サーバーの買い手へどの程度転嫁したかを示す直接の発言は**欠損** | — | [T5-11] | — |

### 4-3. 大手の capex への影響(再掲)

- Amazon の 2026 年 capex は約 $200B → 約 **$220B**(+10%)で、主因は**メモリ価格の上昇**([W1][W3] の再掲)。
- NVIDIA の供給コミットメントが $119B → $279B(主にメモリ調達)([T5-13] 前掲)。

---

## 5. GPU サーバー・クラウドの価格(2026 年の値上げの実例)

| 主体 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| AWS(1 回目) | EC2 Capacity Blocks for ML の価格ページを静かに更新し、H200 系を約 **+15%**。p5e.48xlarge $34.61 → $39.80/時(+15.0%、算出: 39.80 ÷ 34.61 − 1) | 2026-01-04 | [T5-10] | 3*/4 |
| AWS(2 回目) | Capacity Blocks の NVIDIA GPU インスタンスを約 **+20%**(The Information の報道、2026-07-01 から)。対象は P6-B300・P6-B200・P5・P5e・P5en・P4de。新料金は P6-B300 が **$14.04/アクセラレータ時**、P6-B200 が **$12.355** | 2026-07-01 | [T5-10] | 3* |
| AWS の説明 | 予約価格は「需給に基づき定期的に更新」し、購入時点の料金が適用される。Corey Quinn(クラウド経済アナリスト)は 1 月の変更を「需給ではなく方針の決定」と批評 | 2026 年 | [T5-10] | 3* |
| Nebius | 2026-10-01 からオンデマンドを **+17〜21%**。H100 SXM5 $3.85 → **$4.50**(+16.9%、算出: 4.50 ÷ 3.85 − 1)、B300 $7.85 → **$9.50**(+21.0%、算出: 9.50 ÷ 7.85 − 1)。3 か月で 2 回目の改定。出所の Spheron は競合 GPU 業者(Tier 4) | 2026-10-01 | [T5-21] | 3*/4 |
| CoreWeave | 2026 年 7 月に定価を約 **+25%**(全 SKU)、容量は実質売り切れ。新規契約は以前より高い価格(報道) | 2026-07 | [T5-21] [W8] | 3* |
| Oracle | 更新時期の GPU は従来契約比 **+20% のプレミアム**で更新または再販、稼働率 97.9% | 2026-09-10 | [T5-18][W2] | 1* |
| 傾向(分析 1 件) | 予約・契約・新規 Blackwell の価格は 2026 年上期に上昇し、スポットと旧世代 Hopper は軟化。ネオクラウドの H100 は約 **$2.89**/時、AWS・Azure・GCP は **$7〜12**/時(第三者の集計) | 2026-08-16 | [T5-21] | 4 |
| Azure・Google Cloud | 2026 年の GPU 価格改定は**確認できず**(欠損) | — | [T5-10][T5-21] | — |
| Lambda | 2026 年の価格改定は**欠損** | — | [T5-21] | — |
| NVIDIA の価格 | CFO:「実行済みの価格引上げ」が FY2028 Q1 から粗利率に寄与(供給側の部材コスト上昇の転嫁と読めるが、要約は直接の説明を載せていない) | 2026-08-26 | [T5-13] | 1*/3* |
| 既存調査の H100 指数 | SemiAnalysis の 1 年契約指数 $1.70(2025-10)→ $2.35(2026-03)→ 約 $2.65(2026-06) [W2] の再掲 | — | [W2] | 3* |

---

## 6. 供給側の容量計画(GW)と需給ギャップ

### 6-1. ハイパースケーラー・ネオクラウドの GW

| 主体 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Microsoft | Nadella:「データセンターの規模を今後 **2 年で約 2 倍**」。2026 年度(2026-06 期)に 88 のデータセンターを追加(MarketBeat 要約) | 2026 年 | [T5-12][T5-17] | 3* |
| Synergy Research | 世界のハイパースケール容量は「**12 四半期強で 2 倍**」(約 3 年)。2031 年にハイパースケーラーが容量の **67%**、2018 年の **14 倍** | 2026 年 | [T5-12] | 3* |
| Amazon | 稼働中の電力 約 **10.6GW**(Microsoft・Google の約 2 倍)。Jassy:「2027 年末までに容量 2 倍」(二次) | 2026 年 | [T5-12][T5-5] | 3* |
| パイプライン | AWS・Microsoft・Google・Meta で世界のパイプライン MW の約 **58%**(Datacentres.com)。世界のデータセンター容量が約 **50GW**(2026-07-13 の見出し) | 2026-07 | [T5-12] | 3*/4 |
| Morgan Stanley | AI 計算容量が **31GW → 117GW(2028 年)**、約 3.8 倍(算出: 117 ÷ 31)。「過剰供給への懸念に反論」(基準年と定義は要約にない) | 2026 年 | [T5-24] | 3* |
| 会社別の 2027〜2030 年の GW スケジュール | **欠損**(会社別の GW 表は検索で出なかった) | — | [T5-12] | — |
| Oracle | FY2029 までに 10GW の電力を確保、850MW を Q1 FY27 に納入、GPU 30 万基超 [W3][W2] の再掲 | 2026-09 | [T5-18] | 1* |
| 外販チップの GW | OpenAI-AMD 6GW、Anthropic-AMD 最大 2GW、Meta-AMD 6GW、Broadcom/Google の TPU 5GW(2027 年)・10GW(2028 年)、Anthropic の TPU 約 3.5GW(2027 年から、[W3]) | 2026 年 | [T5-19][T5-3] | 3* |
| 懐疑論 | 「発表された GW の合計は約 500GW で、変圧器・系統連系・シリコンの裏付けがない」(Yahoo Finance の記事題名、本文未確認) | 2026 年 | [T5-12] | 3 |

### 6-2. 需給ギャップの推計と均衡の時期

| 出典 | 内容 | 時点 | Tier |
|---|---|---|---|
| Morgan Stanley(米国の電力) | 2026〜2028 年に新規電力 **68GW** が必要、建設中と契約済みの系統容量で **30GW** を賄える、**38GW** は未解決(算出: 68 − 30 = 38) | 2026-08 | 3* [T5-15] |
| Morgan Stanley(別の要約) | 総ギャップ **57GW**、プラグアンドプレイ電源(オンサイト発電・燃料電池)を引いた後の純ギャップ **32GW**(総需要の **34%**)。24/7 Wall St.: 必要 97GW − 建設中 21GW − 系統の空き 19GW = **57GW**(算出: 97 − 21 − 19) | 2026-08〜09 | 3*/4 [T5-15] |
| Elon Musk(G20 のイノベーション閣僚会合) | 2027 年に AI チップ向け電力が **少なくとも 15GW 不足**(「アナリストのコンセンサス」と本人が説明) | 2026 年 | 3*/4 [T5-15] |
| Gartner(旧い予測) | 2027 年までに AI データセンターの 40% が電力不足で運用制約(2024 年の予測) | 2024 年 | 3* [T5-15] |
| Goldman Sachs | AI インフラの需給は **2028 年**まで均衡しない可能性。以前の想定は 2027 年末で、その後 **2028 年上期**が現実的とのコメント。ハイパースケーラーの capex は減らず増え続ける | 2026 年 | 3* [T5-24] |
| Digitimes | NVIDIA の次世代向けメモリ不足は 2027 年を通じて強まり 2028 年にかかる | 2026-06-08 | 3* [T5-24] |
| SemiAnalysis(Patel、インタビュー) | 資本は供給を拡大できるが、半導体・インフラの対応は新規能力に数年かかるため遅い。研究所は外部推論より研究・訓練・継続学習に自社の計算を多く配分する可能性 | 2026-08 | 3* [T5-24] |
| BCG Henderson Institute(旧い) | 2028 年に生成 AI が世界のデータセンターの AI 計算供給に占めるのは約 **34%**。生成 AI の急速な普及だけで世界の計算ハードウェアの生産能力を超えることはない。エネルギーがより大きなリスク | 日付不明 | 3 [T5-24] |
| 結論の併記 | 銀行・チップ供給の予測は 2028 年に向けた不足を示し、BCG のモデルは供給が追いつくとする。2028 年に過剰供給が起きるとする具体的な予測は**検索結果に出なかった** | — | [T5-24] |
| 会社の発言(再掲) | Amazon は 2026・2027・2028 年とも「需要に容量が足りない」[W3]。Microsoft は 2025-10 に「容量制約は少なくとも 2026 年 6 月(会計年度末)まで」、2026-01 に「需要が供給を上回り続ける」 | 2025-10〜2026-01 | 1*/3* [T5-17] |
| Microsoft 2026-07 の決算 | Azure 成長 +43%、2027 会計年度 Q1 見通し 約 +45%(固定為替)、容量制約下。制約の終期は**欠損**。ある二次記事:「Azure の成長を制約しているのはハードウェアの調達でなく電力とデータセンター空間」 | 2026-07-29 | 3* [T5-17] |
| Alphabet | 決算前の記事:「計算容量の制約が売上成長と製品投入の速度を制限し得る」(2026 Q2 の決算前) | 2026-07 | 3* [T5-14] |

---

## 7. 電力・建設の制約の更新(W3 との差分)

| 項目 | 新しい情報 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| PJM 2028/29 年度の容量オークション | 2026-07-14 公表。発電・DR で **138,318MW**(UCAP)+ FRR 地域 10,864MW = **149,182MW**(算出で一致)。価格は全域 **$325/MW-日**(上限)で **3 回連続**。信頼度要件に **6,831MW 不足**。上限(コリドー)がなければ約 $555/MW-日(シミュレーション)。予備率 14.7%。ピーク負荷予測は前回より約 2,000MW 高い | 2026-07-14 | [T5-22] | 2*(PJM 公表、要約経由) |
| PJM 2027/28 年度 | 2025-12 のオークションで **145,777MW**、信頼度要件に **6.6GW 不足**。2027 年夏が初めて容量不足を見込む季節。データセンター増が新規発電の約 2 倍 | 2025-12 | [T5-15] | 2*/3* |
| PJM の追加調達 | 9 月に FERC の承認を得て「Backstop Procurement」を実施する意向。**承認の有無は未確認** | 2026-07〜09 | [T5-22] | 3* |
| 要約内の表記ゆれ | Renewable Energy World と Power Engineering は「13,318MW」と記載、PJM の発表は 138,318MW(桁落ちと考えられ、PJM を採用) | — | [T5-22] | — |
| 計画の遅延 | アナリストは 2026 年に計画されたデータセンター容量の **30〜50%** が 2028 年に後ろ倒しされると予想(W3 の再掲と同趣旨) | 2026-06 | [T5-20] | 3* |
| 変圧器 | リード時間 **36 か月**(従来 18〜24 か月、[W3] の再掲)。今回の検索では**新しい数値は出ず** | 2026 年 | [T5-12] | 3* |
| ガスタービン・FERC の大口負荷連系の規則・オンサイト発電 | 今回の検索では**新しい情報は出ず**([W3] の GE Vernova 116GW、Siemens Energy 69GW 等が最新) | — | [T5-22] | — |

---

## 8. その他の部材の制約

| 部材 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| T-glass(高性能ガラスクロス) | 最上位の CTE 2.8% の T-glass は、認定済みの供給元が事実上 **Nittobo の 1 社**。新規能力は 2026 年末に稼働し 2027 年に出荷。台湾の基板メーカーは 2026 年に **10〜20%** の不足、2026 年下期の高級ガラスクロスは **40% 超**の不足を予想。PCB のリード時間は **20 週超** | 2026-04〜06 | [T5-20] | 3* |
| 光トランシーバー・レーザー | Yole:「レーザーが最も目に付く上流の制約」。800G 以上のトランシーバーは **2026 年と 2027 年に約 150M 個**(「各年」か「2 年合計」かは要約から判別不能)。光部品の新工場は稼働まで 12〜18 か月 | 2026 年 | [T5-20] | 3* |
| 光(反対の見方) | LightCounting:InP レーザー・VCSEL の不足は 2026 年半ばまでに緩和し、2026 年末に 1〜2 四半期の横ばいの可能性(2026-01 の記述。Yole と食い違い) | 2026-01 | [T5-20] | 3* |
| GDDR7 | GDDR7 の不足と HBM4 の遅れが 2026 年の GPU 供給を絞る(SoftwareSeni の見出し、本文未確認) | 2026 年 | [T5-1] | 4 |
| 液冷・変圧器 | 今回の検索では**新しい数値は出ず**(欠損) | — | [T5-20] | — |

---

## 9. 食い違い(どちらかを採らず併記)

| # | 項目 | 値 A | 値 B | 備考 |
|---|---|---|---|---|
| 1 | CoWoS の 2026 年 | KeyBanc 能力 650k ウェハ/年 | Morgan Stanley 需要 1.394M ウェハ/年。月産能力は 115k〜140k(年末、× 12 で 1.4M〜1.7M) | 能力と需要、OSAT の含否、年末の月産と年間の違い |
| 2 | CoWoS の 2027 年末の月産能力 | JPM(旧)112k | KGI 170k | 日付が違う。JPM の新しい推計(2026-01)では 2026 年末が 115k |
| 3 | NVIDIA の 2026 年の台数 | KeyBanc の容量試算 8.0〜8.5M(Blackwell + Rubin + Hopper) | 別の証券会社 総計 約 6.3M、Rubin 約 2.9M | Rubin は 1.5M(KeyBanc、4 月)と 2.9M で約 2 倍の差。Hopper を含むか不明 |
| 4 | Rubin の時期 | NVIDIA:「フル生産」、遅れの報道は誤り(2026-08-26) | KeyBanc(4 月):2.0M → 1.5M、SK hynix の HBM4 出荷 −20〜30%、TrendForce の題名「2027 年に遅れる」(本文未確認) | 時点が違う。KeyBanc の 7 月のメモは「わずかな遅れ、B300 で相殺」 |
| 5 | 2027 年の TPU | 5M(Morgan Stanley・TrendForce・Jon Peddie) | 8.84M(GF Securities の強気ケース) | 見出し「3 倍で 8.8M」は GF の 2026 年(4.504M)との比で 1.96 倍 |
| 6 | 2026 年の TPU | 3.2M(MS)/ 3.3M(DigiTimes) | 4.6M(BofA)/ 4.504M(GF) | 供給制約を織り込むか |
| 7 | DRAM 2026 Q1 の上昇率 | 55〜60%(従来の予測) | 90〜95%(上方修正) | 予測の時点 |
| 8 | DRAM の累計上昇 | 見出し「2026 年に 2 倍」(softwareseni) | 算出 約 3.4〜4.0 倍(分類が混在) | 起点と分類が違う。算出は参考値 |
| 9 | HBM4 の価格 | $4 台中盤〜後半/Gb(2027 年提示価格)→ 36GB スタックで約 $1,296(算出) | スタック当たり約 $500(推計) | 日付と提示価格・推計の違い |
| 10 | Micron の逼迫の終期 | CEO(2026-06):暦年 2027 年を超えて | 二次記事:少なくとも 2028 年まで | 同趣旨の可能性。原文は未確認 |
| 11 | メモリの逼迫の終期 | SK hynix CEO:2030 年以降も需要が能力を上回る | UBS:2028 年 Q2 まで / HPE:2027 年に入っても / IDC:2027 年に入っても | 話者・対象(HBM、DRAM 全体、サーバー価格)が違う |
| 12 | IDC の PC 出荷 | −4.9%(基準)/ −8.9%(悪化ケース) | −11.3%(別の記事) | 時点・ケース |
| 13 | Counterpoint のスマホ出荷 | −2.1%(2026 年) | −12%(「記録上最大」とする集計) | 時点・版 |
| 14 | Microsoft の capex | 2027 会計年度 約 $175B(MarketBeat 要約) | 暦 2026 年 約 $190B / FY2027 約 $255B([W3]) | 会計年度と暦年、定義 |
| 15 | Alphabet の 2026 年 capex | $180〜190B(決算前の記事) | $195〜205B([W3]、Q2 決算後) | 時点 |
| 16 | NVIDIA の供給コミットメント | $279B(CFO のコメント) | $105B(The Energy Mag)/ 総コミットメント 約 $366B | 範囲(購入契約のみか、クラウド契約・リースを含むか)。KuCoin の題名「$3.66 Trillion」は桁の誤記と考えられる |
| 17 | Morgan Stanley の電力ギャップ | 必要 68GW − 手当 30GW = 未解決 38GW | 総 57GW / 純 32GW(必要 97GW − 建設中 21GW − 空き 19GW) | 総需要の定義が 68 と 97 で異なる。基準年・オンサイト電源の扱いが違うと考えられる |
| 18 | 光レーザーの逼迫 | Yole:レーザーが最大の上流制約 | LightCounting:2026 年半ばに緩和 | 時点(2026-01 と 2026 年中) |
| 19 | Project Rainier | 2024 年末に Trainium2 50 万個 → 2025 年末に 100 万個 | 2025 年末に初回 50 万個 | 出典の質が低い |
| 20 | PJM の MW | 138,318MW(PJM) | 13,318MW(2 つの記事) | 桁落ちと考えられる。PJM を採用 |
| 21 | AWS の値上げの性格 | AWS:需給に基づく定期更新 | Corey Quinn:方針の決定 | 解釈の違い |
| 22 | 世界のデータセンター容量 | 約 50GW(Datacentres.com、2026-07 の見出し) | Morgan Stanley の「31GW から 117GW」 | 対象(世界の全データセンターか AI 計算容量か)が違う |

---

## 10. 欠損と試した検索語

| 項目 | 状態 | 試した検索語(番号は 11 節) |
|---|---|---|
| NVIDIA の 2027・2028 年の出荷台数 | 欠損。TSMC の CoWoS 割当(MS)と AMD の台数のみ | 検索 1・25 |
| AWS Trainium の台数(2026〜2028 年) | 欠損。時期と Project Rainier の個数(低信頼度)のみ | 検索 3・5 |
| HBM の確定した契約価格、HBM の bit 供給量 | 欠損。提示価格・予測のみ | 検索 26・6 |
| Q4 の HBM 単独の価格上昇率 | 欠損 | 検索 4 |
| Azure・Google Cloud の GPU 価格改定(2026 年)、Lambda の改定 | 欠損 | 検索 10・21 |
| AI サーバーの買い手への値上げ転嫁率(Dell・HPE・Supermicro) | 欠損。通常サーバーの値上げのみ | 検索 11 |
| Supermicro の公式値上げ | 欠損 | 検索 11 |
| Oracle の部材コスト・メモリ価格・価格転嫁に関する発言 | 欠損(+20% の更新のみ) | 検索 18 |
| Microsoft・Amazon・Alphabet の Q2 2026 決算の容量制約の逐語(終期) | 欠損 | 検索 14・17 |
| 会社別の 2027〜2030 年の GW スケジュール | 欠損 | 検索 12 |
| 2029〜2030 年の容量・アクセラレータ・GW の予測 | 欠損(Broadcom の 2028 年 10GW が最長) | 検索 3・12・24 |
| 2028 年に過剰供給となる予測 | 検索結果に出ず | 検索 24 |
| Micron の FQ4 説明会の 2027 年の供給・HBM の発言の逐語 | 欠損 | 検索 7 |
| SK hynix・Samsung の確定決算(Samsung は 2026-10-29 に発表予定) | 欠損 | 検索 9 |
| FERC の大口負荷連系の規則、PJM の追加調達の承認、オンサイト発電・ガスタービンの新規情報 | 欠損 | 検索 22 |
| 液冷・変圧器の新しい納期 | 欠損 | 検索 20 |
| TrendForce「Rubin Ramp Delayed to 2027」の本文 | 未確認(題名のみ) | 検索 1・23・25 |
| KGI・KeyBanc・Morgan Stanley・TrendForce・Goldman・UBS の原本 | 未開封(要約経由) | 検索 1〜4・24 |

---

## 11. 出典一覧(検索ログ兼用。26 回、すべて mode "standard")

各検索の語と、要約が根拠にした主な URL。URL は検索結果に表示されたもので、本文は開いていない。

- **[T5-1]** NVIDIA GPU shipments forecast 2026 2027 2028 Blackwell Rubin units million CoWoS allocation — https://www.itiger.com/news/1159152887 、https://www.kucoin.com/news/flash/morgan-stanley-report-cowos-demand-to-double-by-2027-amd-and-asics-drive-ai-chip-growth 、https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/tsmc_2330-tt_09032026e.pdf 、https://www.softwareseni.com/hbm4-delays-and-gddr7-shortages-the-memory-bottlenecks-squeezing-gpu-supply-in-2026/ 、https://www.trendforce.com/research/download/RP260921NC3 、https://longportapp.cn/news/281776591
- **[T5-2]** TSMC CoWoS capacity 2026 2027 wafers per month expansion forecast — https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/tsmc_2330-tt_09032026e.pdf 、https://www.trendforce.com/news/2026/09/14/news-tsmc-reportedly-targets-22-2nm-16-3nm-capacity-boost-by-mid-2027-cowos-to-double-by-2028/ 、https://www.trendforce.com/news/?p=59316 、https://www.trendforce.com/news/?p=64011 、https://www.itiger.com/hans/news/1159152887
- **[T5-3]** Google TPU shipments 2026 2027 2028 forecast million units Broadcom Trainium shipments — https://www.kucoin.com/news/flash/morgan-stanley-defends-broadcom-s-role-in-google-s-tpu-supply-chain-forecasts-5m-shipments-by-2027 、https://www.trendforce.com/news/?p=51034 、https://www.jonpeddie.com/techwatch/google-tpu-roadmap-custom-silicon-scaling/ 、https://finviz.com/news/398220/piper-sandler-forecasts-google-tpu-hardware-revenue-to-reach-104-billion-by-2028 、https://247wallst.com/investing/2026/08/25/google-tpu-volume-could-triple-to-8-8-million-by-2027/
- **[T5-4]** TrendForce DRAM contract price 4Q26 forecast increase HBM NAND shortage — https://technews.tw/?p=1622115 、https://www.kucoin.com/news/flash/trendforce-raises-q3-q4-dram-contract-price-forecasts-benefits-micron 、https://money.udn.com/money/amp/story/5607/9426895 、https://www.ctee.com.tw/news/20260408700166-430501
- **[T5-5]** AWS Trainium3 shipments 2026 2027 million chips forecast Anthropic Project Rainier capacity — https://www.nextplatform.com/2025/10/31/aws-bullish-on-homegrown-trainium-ai-accelerators/ 、https://www.digitimes.com/news/a20260623PD213.html 、https://www.trendforce.com/news/?p=47625 、https://algeriatech.news/?p=21172
- **[T5-6]** SK hynix HBM sold out 2027 supply shortage until 2028 memory chair statement — https://propakistani.pk/2026/07/13/sk-hynix-warns-memory-shortage-will-be-worst-ever-in-2027/ 、https://www.gadgetreview.com/?p=402543 、https://view.asiae.co.kr/en/article/2025102910334843684 、https://xenospectrum.com/en/sk-hynix-memory-shortage-2027-2030-capacity-gap/ 、https://aiweekly.co/alerts/sk-hynix-crosses-1-trillion-as-2026-hbm-sells-out
- **[T5-7]** Micron fiscal Q4 2026 results September 2026 HBM guidance supply tight 2027 DRAM pricing — https://aiweekly.co/alerts/micron-q4-revenue-jumps-379-to-542b-on-ai-memory-demand-guides-fiscal-2027-q1 、https://www.nextplatform.com/store/2026/10/02/microns-numbers-show-why-hbm4-memory-is-worth-15x-its-weight-in-gold/5300701 、https://stockhub.kr/en/insights/view_1790837291827_6kep8ibsm-micron-fy26-q4-ai-memory-supply-20261001 、https://www.zacks.com/stock/news/2756578/micron-beats-on-q4-earnings:-will-strong-guidance-lift-the-stock
- **[T5-8]** memory prices smartphone PC price increase 2026 IDC Counterpoint shipments forecast cut DRAM costs — https://www.techspot.com/news/110679-memory-shortages-raise-pc-smartphone-prices-8-2026.html 、https://www.malaysianwireless.com/2026/03/counterpoint-rising-memory-costs-push-up-smartphone-prices/ 、https://www.roic.ai/news/memory-prices-soar-up-to-90-in-q1-2026-counterpoint-02-05-2026 、https://www.91mobiles.com/updates/global-memory-shortage-disrupt-smartphone-pc-markets-2026-idc/ 、https://www.softwareseni.com/dram-prices-in-2026-have-doubled-and-the-numbers-are-getting-worse/ 、https://www.techradar.com/pro/experts-warn-pc-prices-could-rise-even-more-in-2026-as-ram-costs-set-to-soar-higher
- **[T5-9]** Samsung Electronics Q3 2026 preliminary operating profit memory prices HBM4 October 2026 — https://www.koreatimes.co.kr/business/companies/20261008/samsung-electronics-estimates-803-bil-in-q3-operating-profit 、https://xenospectrum.com/en/samsung-q3-2026-memory-profit-gap/ 、https://www.stockhub.kr/en/insights/view_1791453341972_4n6eooju8-citi-samsung-005930-q3-2026-hbm4-20261008 、https://www.trendforce.com/news/?p=65017
- **[T5-10]** AWS raises EC2 prices GPU instances Capacity Blocks price increase 2026 Azure Google Cloud price hike memory costs — https://aiweekly.co/alerts/aws-raises-ec2-gpu-capacity-block-prices-20-from-july-1 、https://convergedigest.com/aws-raises-ec2-prices-by-about-20-for-ai-gpu-reservations/ 、https://introl.com/blog/aws-gpu-price-increase-h200-january-2026 、https://algeriatech.news/aws-gpu-price-hike-15-percent-cloud-costs-era-ends-2026/
- **[T5-11]** Dell HPE Supermicro server price increase 2026 memory costs pass through AI server pricing — https://www.crnasia.com/news-network/2026/hpe-ceo-antonio-neri-elevated-memory-prices-to-persist-we 、https://www.ciodive.com/news/dell-memory-chip-crunch-pc-server-market-contracts/813420 、https://www.networkworld.com/article/4093752/server-memory-prices-could-double-by-2026-as-ai-demand-strains-supply.html 、https://www.techradar.com/pro/the-bad-news-continues-server-prices-set-to-rise-in-latest-blow-to-hardware-budgets 、https://reddit.sentinel-team.org/posts/1thp0ok/snapshots/2026-05-22T21%3A26%3A58.02755Z
- **[T5-12]** hyperscaler data center capacity plan gigawatts 2027 2028 2030 Microsoft Google Amazon Meta add GW doubling — https://www.datacentres.com/news/hyperscaler-capex-surge-pushes-global-data-centre-capacity-to-50-gw-as-power-con-slot1-2026-07-13 、https://www.ciodive.com/news/hyperscalers-two-thirds-data-center-capacity-2031/817016/ 、https://www.ftportfolios.com/Commentary/EconomicResearch/2026/7/16/hyperscalers-can-the-ai-buildout-last 、https://finance.yahoo.com/sectors/technology/articles/big-tech-making-empty-promises-100951250.html
- **[T5-13]** Nvidia Q2 fiscal 2027 results August 2026 supply commitments gross margin memory costs Rubin ramp data center revenue guidance — https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf 、https://www.nasdaq.com/articles/nvidias-supply-commitments-more-doubled-279-billion-heres-what-it-does-stock 、https://quartr.com/events/nvidia-corporation-nvda-q2-2027_33dRoFp6 、https://beancount.io/blog/2026/08/26/nvidia-fy2027-q2-earnings-analysis 、https://www.kucoin.com/news/flash/nvidia-q2-2027-earnings-revenue-surpasses-96-billion-ai-infrastructure-commitments-hit-3-66-trillion 、https://theenergymag.com/news/market-news/nvidia-q2-revenue-hits-96-2-b-as-data-center-surges-117-and-vera-rubin-ramps
- **[T5-14]** capacity constrained through 2027 Amazon Microsoft Alphabet Q2 2026 earnings call "capacity" constraints demand exceeds supply Hood Jassy Pichai — https://pepperstone.com/en-au/insights/market-analysis/equities/alphabet-q2-earnings-preview-cloud-and-capex-take-center-stage 、https://pepperstone.com/en-gb/insights/market-analysis/equities/amzn-q2-2026-earnings-preview-ai-capex-in-focus 、https://www.itiger.com/hans/news/1101967665
- **[T5-15]** AI data center power shortfall GW 2027 2028 supply demand gap estimate grid constraints October 2026 — https://www.kucoin.com/news/flash/morgan-stanley-reports-38-gigawatt-power-shortfall-for-ai-data-centers-by-2028 、https://cryptobriefing.com/morgan-stanley-ai-data-centers-38-gigawatt-power-gap/ 、https://247wallst.com/investing/2026/09/29/the-coming-ai-blackout-10-trillion-data-center-surge-threatens-to-break-the-grid/ 、https://introl.com/blog/pjm-grid-crisis-6gw-shortfall-data-center-power-2027 、https://datacentremagazine.com/news/g20-elon-musk-speaks-on-global-data-centre-opportunity
- **[T5-16]** DRAM new fab capacity 2027 2028 Samsung P5 SK hynix Yongin Micron Idaho supply catch up demand when shortage ends — https://www.trendforce.com/news/?p=64868 、https://implicator.ai/samsung-sk-hynix-and-micron-chase-ai-memory-as-buyers-wait-to-2027/ 、https://www.how2shout.com/news/memory-shortage-2027-ai-hbm-samsung-sk-hynix-micron.html 、https://www.webull.com/news/15350144979772416 、https://www.buysellram.com/?p=19931 、https://longportapp.cn/news/269683934 、https://feedbagel.com/post/ram-shortage-expected-to-persist-until-2030-manufacturers-to-meet-only-60-of-dem
- **[T5-17]** Microsoft Azure capacity constrained fiscal 2027 Amy Hood July 2026 earnings call AI capacity short supply through — https://www.marketbeat.com/instant-alerts/microsoft-q4-earnings-call-highlights-2026-07-29 、https://www.fool.com/earnings/call-transcripts/2025/10/29/microsoft-msft-q1-2026-earnings-call-transcript 、https://introl.com/blog/hyperscaler-capex-690-billion-microsoft-azure-power-bottleneck-2026 、https://dc.fortune.com/2026/01/28/microsoft-stock-drops-azure-growth-slows-capex-spending-q2
- **[T5-18]** Oracle Q1 fiscal 2027 earnings September 2026 capacity supply constrained GPUs memory costs Magouyrk Catz capex pricing — https://www.datacenterdynamics.com/en/news/oracle-delivered-300000-gpus-in-q1-fy2027/ 、https://kucoin.com/news/flash/oracle-renews-ai-gpu-contracts-at-20-higher-rates-amid-surging-demand 、https://www.constellationr.com/insights/news/oracle-q1-strong-and-so-capital-expenditures 、https://cryptobriefing.com/oracle-q1-fy27-earnings-revenue-rpo/ 、https://fourweekmba.com/ai-oracle-q1-fy2027-backlog-capex-analysis/
- **[T5-19]** AMD MI450 Helios 2026 shipments ramp OpenAI 6 gigawatt first gigawatt second half 2026 2027 volume — https://fierce-network.com/cloud/amd-launches-full-stack-ai-compute-agentic-era 、https://datacenterfrontier.com/machine-learning/article/55322262/amd-scales-the-ai-factory-6-gw-openai-deal-korean-hbm-push-and-helios-debut 、https://www.nasdaq.com/articles/advanced-micro-devices-bets-helios-agentic-ai-drive-data-center-growth 、https://convergedigest.com/?p=113861
- **[T5-20]** AI supply chain bottlenecks 2026 2027 optical transceivers lasers substrates T-glass liquid cooling transformers shortage lead times — https://www.yolegroup.com/strategy-insights/opinion-optical-transceivers-at-the-chokepoint-of-ai-growth-and-supply-chain-constraints/ 、https://borecraft.com/2026/06/09/the-ai-bottleneck-is-spreading-from-chips-to-substrates-glass-and-power/ 、https://www.trendforce.com/presscenter/news/20260420-13017.html 、https://lightcounting.com/newsletter/en/january-2026-optics-for-ai-clusters-366
- **[T5-21]** CoreWeave Nebius Lambda GPU price increase 2026 neocloud raises prices Azure Google Cloud GPU instance price increase — https://www.spheron.network/blog/nebius-gpu-price-hike-2026-h100-to-b300-rates-rise-up-to-21/ 、https://spendark.com/blog/cloud-gpu-price-war-2026/ 、https://spheron.network/blog/coreweave-h100-h200-pricing-2026 、https://cryptobriefing.com/coreweave-nebius-ai-chip-demand/
- **[T5-22]** PJM capacity auction 2028/2029 results data center load large load interconnection FERC rule gas turbine behind-the-meter September 2026 — https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2026-releases/20260714-pjm-capacity-auction-procures-138318-mw-of-generation-resources.pdf 、https://www.opis.com/resources/energy-market-news-from-opis/pjms-2028-2029-capacity-auction-clears-at-price-cap-for-third-time/ 、https://www.publicpower.org/periodical/article/pjm-capacity-auction-procures-138318-mw-generation-resources-capacity-price-comes-cap-325 、https://www.power-eng.com/business/policy-and-regulation/pjm-capacity-auction-easily-hits-price-cap-again/ 、https://oilprice.com/Energy/Energy-General/PJM-Auction-Comes-Up-68-Gigawatts-Short-As-Data-Centers-Devour-Power.amp.html
- **[T5-23]** Rubin ramp delayed HBM4 SK hynix Samsung TrendForce September 2026 Vera Rubin shipments 2026 2027 NVL144 — https://www.sdxcentral.com/news/sk-hynix-memory-production-delay-impact-could-impact-nvidia-rubin-release-report/ 、https://tomshardware.com/tech-industry/hbm4-mass-production-delayed-as-nvidia-pushes-memory-specs-higher 、https://www.trendforce.com/presscenter/news/20260108-12869.html 、https://www.trendforce.com/news/?p=56030
- **[T5-24]** when will AI compute supply catch up with demand shortage end 2028 GPU capacity glut analyst forecast inference demand agentic tokens — https://www.kucoin.com/blog/th-ai-infrastructure-shortage-may-last-until-2028-as-hyperscaler-capex-keeps-rising 、https://startupmap.iamsterdam.com/news/feed/morgan-stanley-projects-ai-compute-capacity-to-quadruple-to-117gw-by-2028-as-nebius-targets-51b-revenue 、https://apps.digitimes.com/news/a20260608PD208/nvidia-dram-capacity-2028.html 、https://bcghendersoninstitute.com/generative-ais-impact-on-computing-power-lessons-from-a-bullish-model-of-global-demand/ 、https://tweaktown.com/news/111454/microns-ceo-says-ai-memory-demand-is-just-in-its-first-innings-and-memory-supply-is-already-insufficient/index.html
- **[T5-25]** KGI KeyBanc Nvidia Rubin 2026 units cut 1.5 million HBM4 constraint Rubin delay 2027 Nvidia denies — https://longportapp.cn/news/281776591 、https://www.webull.com/news/15244452445561856 、https://invezz.com/en-ae/news/2026/04/06/nvidia-stock-stuck-below-dollar180-whats-hurting-the-ai-darling/ 、https://www.sdxcentral.com/news/sk-hynix-memory-production-delay-impact-could-impact-nvidia-rubin-release-report/
- **[T5-26]** HBM market size 2026 2027 2028 forecast billion HBM4 price per stack premium HBM3E price increase 2027 contract negotiation — https://siliconanalysts.com/market/samsung-hbm4-2027-pricing-set-to-more-than-double-2026-10-07 、https://www.trendforce.com/research/download/RP260603TD3 、https://chippub.substack.com/p/hbm-latest-forecast 、https://www.techradar.com/pro/micron-wants-a-bigger-slice-of-the-usd100-billion-hbm-market-with-its-2026-bound-hbm4-and-hbm4e-memory-solutions 、https://www.meticulousresearch.com/product/high-bandwidth-memory-hbm-market-6953

既存調査(再掲元): `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research3/` の W1_cloud_margin_history.md、W2_gpu_economic_life.md、W3_industry_structure.md、W8_aws_vs_commodity.md。
