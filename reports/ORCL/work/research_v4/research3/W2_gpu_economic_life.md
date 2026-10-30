# W2: GPU の経済的耐用年数と、世代別の価格推移・再契約価格

- 対象: Oracle(NYSE: ORCL)再評価のうち「AI クラウド事業の将来の利益率と価値」に関わる GPU の耐用年数と価格
- 作成日: 2026-10-12(検索上限 26 回を全て使用。mode はすべて standard)
- 範囲: 事実・数値・出典の整理のみ。投資判断・推奨は書かない
- 表記: 出典 ID は検索番号(W2-01〜W2-26)。末尾の「出典一覧」に URL を置く。「既S1〜S4」「既R2〜R7」は既存調査の再掲
- Tier: 1=会社開示・決算説明会 / 2=規制当局・公的統計 等 / 3=報道・アナリスト・調査会社 / 4=ブログ・SNS・販促。`*` は検索要約経由で原本を読めていない
- 検索結果は要約として返るため、本書の数値は原則すべて `*` 付き(原本未読)。原本を読めた項目はない

---

## 0. 要約(事実のみ)

1. **H100 の時間単価は 2025-10 以降に上昇した。** SemiAnalysis の H100 1 年契約指数は $1.70(2025-10)→ $2.35(2026-03)→ 約 $2.65(2026-06)。Silicon Data のネオクラウド指数は $2.00(2025-12、既S3)→ $2.80(2026-08-02)。Nebius の定価は $3.85 → $4.50(2026-10-01 改定、+16.9%)。系列の定義が違い、2026 年 8〜9 月の H100 の水準は $2.53〜$4.50 に分かれる。2023〜2024 年の系列は欠損。(Tier 3*〜4*)
2. **新しい世代も同時に上昇した。** Ornn の Blackwell 指数は $2.75(2026-02 中旬)→ $4.08(2026-04-13)で +48%。Nebius は 2026-10-01 に B200 +18.9%、B300 +21.0%、H200 +20.0% を改定(5 月にも平均 +29%)。Silicon Data(2026-08-02)は H200 $3.16、B200 $5.66。(Tier 3*)
3. **Oracle の更新データ。** Q1 FY27(2026-06〜08 期、説明会 2026-09-10)「更新時期を迎えた GPU は従来契約比 +20% のプレミアムで更新または再販。過半は 4 年以上前の GPU」。稼働率 97.9%。世代・数量・更新のみの単価は非開示。(Tier 3、原典 1*)
4. **CoreWeave の発言。** 2026-08-11 の説明会で A100 契約(2029 年まで)を「attractive price」で締結と開示。Intrator「旧世代 SKU の価格は数年前と同等以上」。別に、CNBC で「期限切れの H100 を元の価格の 95% で再契約」と報じられた(日付未確認)。(Tier 3*)
5. **会計上の耐用年数。** Amazon は 2025-01-01 から一部サーバーを 6 → 5 年に短縮(10-K FY2025、理由は技術進歩、特に AI/ML)。2025 年の影響は減価償却 +$1.4B、純利益 -$1.0B。Oracle・Microsoft・Alphabet・CoreWeave は 6 年、Meta は 5.5 年(既S4 再掲)。Nebius の 4 年は今回確認できず。(Tier 1*)
6. **批判側の推計。** Burry(2025-11)は 2026〜2028 年の減価償却の過小計上を累計 $176B、Oracle の利益を約 27%、Meta を約 21% 過大と推計。JPMorgan AM の感応度は、3 年耐用で再計算すると 2025 年 EPS が Oracle -17%、Amazon・Meta・Microsoft -7%、Alphabet -6%。(Tier 3*)
7. **Huang 発言。** GTC 2025 で「Blackwell が大量出荷されたら Hopper はただでも要らない」(ジョーク調と報じられた)。2026-08-11 の寄稿と X では「NVIDIA compute is fungible, durable and highly rentable」「A100 は 2020〜2029 年稼働可能」。明示的な撤回・訂正の発言は見つからず。(Tier 3*)
8. **電力当たり性能(ベンダー主張)。** Rubin NVL72 は GB200 NVL72 比で約 10 倍の tokens/MW(CoreWeave ブログ、DeepSeek R1)。GB300 比では NVIDIA が最大 30 倍、独立集計は 100 TPS で 2.09 倍。SemiAnalysis InferenceX の MiniMax M2.5/M2.7 では GB200 約 1.58M、H100 約 356K tokens/s/MW(約 4.4 倍、算出)。モデルと速度の条件で H100 の方が安い点もある。(Tier 1*〜3*)
9. **1MW・1GW の経済。** Huang 発言として 1GW あたり $50〜60B、うち NVIDIA 約 $35B(NVIDIA 比率 58〜70%、算出)。実績ベースの 1MW 年売上は会社例示 $10M〜Nebius $20〜25M(再掲)。NVL72 ラック電力で換算した定価ベースの上限は $36〜95M/MW・年(算出、定価のため実績と乖離)。世代別の 1MW 売上は欠損。(Tier 3*)
10. **中古。** Silicon Data の分析で H100 中古の中央値は新品価格の 61%(2024)→ 69%(2025)。ServerBuyback(2026-07)は H100 PCIe 中古 $14,000〜25,000(新品 $25,000〜34,000)。ほとんどが提示価格で、成約価格・SXM 別の系列は欠損。(Tier 3*〜4*)

---

## 1. 世代別 GPU 時間単価(2023〜2026)

### 1-1. H100 の時系列(年・四半期・月)

| 時点 | 系列(定義) | 値(USD/GPU 時) | 出典 | Tier |
|---|---|---|---|---|
| 2023 | 欠損 | 欠損 | — | — |
| 2024 | 欠損 | 欠損 | — | — |
| 2025-06 | AWS p5.48xlarge オンデマンドの値下げ | $12.29 → $6.88(-44%) | 既R3 | 再掲 |
| 2025-10 | SemiAnalysis H100 1 年契約指数(底) | 約 $1.70 | W2-02 | 3* |
| 2025-12 | Silicon Data H100 ネオクラウド指数 | $2.00 | 既S3・既S4 | 再掲 |
| 2026-03 | SemiAnalysis H100 1 年契約指数 | $2.35。2025-10 比 +38.2%(算出: 2.35 ÷ 1.70 - 1) | W2-02、W2-21 | 3* |
| 2026-05 | SemiAnalysis スポット指数のピーク | 値は欠損。6 月の $2.42 が「5 月ピークより約 40% 低い」と記述。逆算で約 $4.03(算出: 2.42 ÷ (1 - 0.40)、「約 40%」の丸めを含む) | W2-02 | 3* |
| 2026-06 | SemiAnalysis スポット指数 | $2.42 | W2-02 | 3* |
| 2026-06 | SemiAnalysis H100 1 年契約指数 | 約 $2.65。2025-10 比 +55.9%、2026-03 比 +12.8%(算出: 2.65 ÷ 1.70 - 1、2.65 ÷ 2.35 - 1) | W2-02 | 3* |
| 2026-06-14 | Lambda Cloud の H100 標準単価(Spheron の比較表) | $3.29〜$3.99(PCIe と SXM の別あり) | W2-19 | 4* |
| 2026 年中盤 | AIMultiple のオンデマンド H100 中央値 | 約 $2.99 | W2-02 | 4* |
| 2026-07/08 | Silicon Data ネオクラウド指数 | $2.75〜$2.80(既S3・既S4 再掲) | 既S3 | 再掲 |
| 2026-08-02 | Silicon Data H100 ネオクラウド / ハイパースケーラー | $2.80 / $7.19(比 2.57 倍、算出: 7.19 ÷ 2.80) | W2-01 | 3* |
| 2026-08 | tech-insider: ネオクラウドの H100 スポット / ハイパースケーラーの 3 年リザーブ | $2.43〜$2.63 / $7.43〜$7.52 | W2-01 | 3〜4* |
| 2026-08 | Akash の記事: 単体 GPU オンデマンドの範囲 / ある集計の中央値 | $2〜$7 / 約 $3.37 | W2-01 | 4* |
| 日付なし | Silicon Data の H100 ネオクラウド指数ページ(ティッカー SDH100RT)の表示値 | $2.53(ページに日付なし) | W2-01 | 3* |
| 2026-09-14 | スポット指数(Nebius 値上げ記事中の記述。指数の発行元は不明) | $2.75 | W2-18 | 4* |
| 2026-09 | Ornn の H100 | 約 $3.17(Ornn ページ)/ 約 $3.28(30 日で +22% とする報道)。NVIDIA は確認していない | W2-26、W2-24 | 3〜4* |
| 2026-09(改定前) | Nebius の H100 オンデマンド定価 | $3.85 | W2-21 | 3* |
| 2026-10-01(改定後) | Nebius の H100 オンデマンド定価 | $4.50(+16.9%、算出: 4.50 ÷ 3.85 - 1) | W2-21 | 3* |
| 2026-09 〜 2027-03(先物) | Kalshi の先物曲線の H100(LinkedIn 投稿の記述) | $2.62 → $2.77 | W2-06 | 4*(検証不能) |

- 補足: CME Group と Silicon Data が 2026-10-05 に H100・B200 の貸出指数先物を開始したとする記述が 1 件あるが、一次情報で確認できていない(W2-02)。
- 補足: SemiAnalysis の説明として「オンデマンドの容量が売り切れ、長期契約の保有者が容量をプールに出さない」ことが 1 年契約価格上昇の理由とされる(W2-02、複数の再掲経由)。

### 1-2. 世代別スナップショット(2026 年 4〜10 月)

| 世代 | 系列 | 値(USD/GPU 時) | 時点 | 出典 | Tier |
|---|---|---|---|---|---|
| A100 | Jarvislabs のクラウド範囲 | $1.49〜$3.43 | 2026-03 | W2-15 | 4* |
| A100 | DeployBase の範囲 | $1.19〜$1.48 | 2026-03 | W2-15 | 4* |
| A100 | RunC.AI のスナップショット | Vast.ai の市場掲載が $1 未満、マネージドやハイパースケーラー型が $3 超 | 2026-06 | W2-15 | 4* |
| A100 | Kalshi の先物曲線(LinkedIn 投稿) | 約 $1.10〜$1.12(ほぼ横ばい) | 2026-09〜2027-03 | W2-06 | 4*(検証不能) |
| H200 | Silicon Data | $3.16 | 2026-08-02 | W2-01 | 3* |
| H200 | Ornn(futuresearch が API 値として引用) | $3.47〜$3.78 | 2026-06 中旬 | W2-06 | 3〜4* |
| H200 | Nebius 定価(改定前 → 後) | $4.50 → $5.40(+20.0%) | 2026-10-01 | W2-21 | 3* |
| H200 | Kalshi の先物曲線 | $4.61 → $4.27 | 2026-09〜2027-03 | W2-06 | 4*(検証不能) |
| B200 | Silicon Data | $5.66 | 2026-08-02 | W2-01 | 3* |
| B200 | 集計サイトの中央値(67 社、B300 の記事内) | $6.25 | 2026-09 頃 | W2-22 | 4* |
| B200 | Nebius 定価(改定前 → 後) | $7.15 → $8.50(+18.9%) | 2026-10-01 | W2-21 | 3* |
| B200 | Kalshi の先物曲線 | $5.83 → $5.30 | 2026-09〜2027-03 | W2-06 | 4*(検証不能) |
| Blackwell(型番の別は不明) | Ornn の指数(The Next Web 経由) | $2.75(2026-02 中旬)→ $4.08(2026-04-13)。+48.4%(算出: 4.08 ÷ 2.75 - 1)。30 社超のネオクラウドのスポット取引を捕捉と記述 | 2026-02〜04 | W2-06 | 3〜4* |
| GB200 | OCI $16.00、CoreWeave $10.50(既R3 再掲) | 既R3 | 2026 | 既R3 | 再掲 |
| GB200 | あるプロバイダーの掲載「$8.00 から、Available Now」(社名は要約に無し) | $8.00〜 | 2026 | W2-22 | 4* |
| B300 | Nebius 定価(改定前 → 後) | $7.85 → $9.50(+21.0%) | 2026-10-01 | W2-21 | 3* |
| B300 | 5 月の改定前の Nebius 水準 | 約 $6.10。5 月改定後の $7.85 は +28.7%、10 月改定後の $9.50 は 5 月前比 +55.7%(算出: 7.85 ÷ 6.10 - 1、9.50 ÷ 6.10 - 1)。Benzinga は 5 月の改定をオンデマンド平均 +29%、スポット平均 +51% と報じる | 2026-05〜10 | W2-21 | 3* |
| B300 | 主要サイトのオンデマンド範囲(Modal が下限、AWS が上限) | $7.10〜$17.80 | 2026 | W2-22 | 4* |
| B300 | Akash の記事 | 約 $6.00 | 2026-09 | W2-22 | 4* |
| B300 | 67 社の中央値 / 長期・一括の例 | $8.23 / $7.00〜$12.00 | 2026 | W2-22 | 4* |
| GB300 | 集計サイトの中央値(オンデマンド、7 月比 +17%) | $15.36 → $18.00(プロバイダーの構成で中央値が動く、と同ページが注記) | 2026-07 → 2026-09 頃 | W2-22 | 4* |
| GB300 | io.net の予測(掲載価格ではない) | $4.50〜$6.50(2026 年 3Q・4Q) | 2026 | W2-22 | 4*(予測) |
| GB300 | Azure の VM の第三者推計(1 VM の GPU 数は要約に無く、GPU 当たり単価に直せない) | 約 $28.12/時 | 2026 | W2-22 | 4*(公式価格ではない) |

### 1-3. 世代間の比率(算出)

| # | 内容 | 式 | 値 |
|---|---|---|---|
| a | H200 ÷ H100(Silicon Data、ネオクラウド、2026-08-02) | 3.16 ÷ 2.80 | 1.13 倍 |
| b | B200 ÷ H100(同) | 5.66 ÷ 2.80 | 2.02 倍 |
| c | B200 ÷ H100(Nebius 定価、改定前 → 後) | 7.15 ÷ 3.85、8.50 ÷ 4.50 | 1.86 倍 → 1.89 倍 |
| d | B300 ÷ H100(Nebius 定価、改定前 → 後) | 7.85 ÷ 3.85、9.50 ÷ 4.50 | 2.04 倍 → 2.11 倍 |
| e | H100 のハイパースケーラー ÷ ネオクラウド(Silicon Data) | 7.19 ÷ 2.80 | 2.57 倍 |
| f | H100 の Silicon Data ネオクラウド上昇率(2025-12 → 2026-08-02) | 2.80 ÷ 2.00 - 1 | +40.0% |
| g | Oracle の更新・再販の +20% との並置 | 基準が異なる(Oracle は「従来契約比」、指数は特定日比)ため同じ軸に置けない | — |

### 1-4. 事実のまとめ(1 章)

- 2025-10 から 2026-09 の間、H100・H200・B200・B300 の各社の価格系列は上方向に報じられている。A100 は「上昇」(CoreWeave の 2025 年 Q4 説明会、technews 2026-08-04)、「大きく低下」(ある記事)、「ほぼ横ばい」(先物曲線の記述)が併存する(第 6 章に併記)。
- 水準は系列の定義(スポット、1 年契約、定価、ハイパースケーラーの 3 年リザーブ)で 2 倍以上開く。
- 2023〜2024 年の世代別系列、および長期契約(3〜5 年)の世代別単価は今回の検索で取得できていない(第 7 章)。

---

## 2. 再契約・更新の価格と稼働率

### 2-1. Oracle(再掲を中心に、今回の追加を明記)

| 項目 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Q1 FY27 の発言(逐語に近い) | "Of all the GPUs that came up for renewal in Q1, that capacity was renewed or resold at a 20% premium to prior contracts. The majority of those GPUs are four years or older." | 説明会 2026-09-10(DCD)。別の 1 件は 09-11 | W2-04 | 3(Constellation Research の引用、原典 1*) |
| 発言の位置 | Constellation Research は「経営陣の prepared remarks(準備された発言)」として引用。話者名は今回の要約に無い(既S4 は Q4 の話者を Magouyrk と記載) | 同上 | W2-04 | 3 |
| 同じ四半期の文脈 | 四半期中に GPU 30 万基超・850MW を顧客に納入、稼働率 97.9%、RPO $664B、FY27 売上見通し $90B 以上(+34%) | 同上 | W2-04(DCD、Zacks、CryptoBriefing) | 3* |
| Q4 FY26 の更新実績(再掲) | 35,000 GPU・59 顧客が更新時期。顧客の 49% が GPU の 92% を更新(既S4: 更新された GPU は約 32,200 基) | 2026-06-10 | 既S4 | 再掲 |
| 条件の開示範囲 | 更新・再販の合算の +20%。GPU 世代、対象数、契約期間、更新のみの単価は開示が見つからない | — | W2-04、既S4 | — |
| 「4 年以上前」の読み方(既S4 の整理を再掲) | Q1 FY27 時点で 4 年以上前は 2022-09 以前の調達分。世代は会社が明示していない | — | 既S4 | 再掲 |
| 表現の食い違い | CryptoBriefing は「失効する全 GPU 契約が 20% 高い単価で更新」と書くが、引用された発言は「更新**または再販**」 | 2026-09 | W2-04 | 4* |

### 2-2. CoreWeave

| 項目 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| A100 の新規契約 | A100 クラウド容量の契約を「attractive price」で締結、期間は 2029 年まで。顧客名、GPU 数、契約額、開始日、時間単価は非開示 | 2026-08-11 の説明会 | W2-05 | 3*(Tom's Hardware 経由の報道) |
| 価格水準の発言(Intrator) | 「旧世代 SKU の価格は数年前と同等以上」("pricing for prior generation SKUs is at or above where it was years ago") | 同上 | W2-05 | 3* |
| 価格水準の発言(別の要約) | CFO が旧世代 GPU の平均販売単価を「約 1 年前と同等以上」と述べたとする要約が 1 件(基準時点が Intrator の発言と異なる) | 同上 | W2-05 | 3* |
| 2025 年 Q4 説明会(2026 年初の開催) | 2025 年に A100 の需要と価格が上昇。H100 の価格は年初比 10% 以内 | 2026-02 頃(開催日は要約に無し) | W2-05 | 3* |
| H100 の再契約 95% | Intrator が CNBC に「期限切れ契約から戻った H100 を元の価格の 95% で再契約した」と発言と報じられた。説明会の逐語では確認できていない | 日付未確認(Burry の批判への反論の文脈と報じられる、2025-11 頃) | W2-03、W2-13 | 3*(単一の二次情報) |
| 95% の別表現 | 仏語記事は「再契約時に元の価格の約 95% にとどまることが多い」と書く(英語の一次情報は確認できず) | — | W2-05 | 4* |
| A100 の稼働 | CoreWeave の CEO が「2020 年に購入した A100 はフル稼働」と述べたとされる | 2025-11〜2026 | W2-23 | 3* |
| 契約期間の長さ | A100(2020 年発売)の契約が 2029 年まで = 9 年(算出: 2029 - 2020) | 2026-08 | W2-26(hwbusters 他) | 3* |

### 2-3. Nebius・Lambda・Crusoe

| 事業者 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Nebius | 更新単価・稼働率の発言は今回見つからず(欠損)。定価の改定は 1-2 のとおり: 2026-05 に平均 +29%(オンデマンド)・+51%(スポット)、2026-10-01 に H100 +16.9%、H200 +20.0%、B200 +18.9%、B300 +21.0% | 2026-05 / 2026-10 | W2-21 | 3* |
| Nebius | 中国語の解説は「約 4 年前発売の H100 も値上げ対象で、急速に陳腐化する資産なら値上げしない」と解釈(Nebius 自身の発言ではない) | 2026-09-17 | W2-18 | 4* |
| Nebius | 値上げが Nebius から公表済みかは報道で割れる。Benzinga は報道時点で未確認、Newsquawk の見出しは確認済みと書く | 2026-09 | W2-21 | 3* |
| Lambda | 契約更新・稼働率の発言は見つからず(欠損)。標準単価の比較表のみ(1-1 を参照) | — | W2-19 | — |
| Crusoe | 契約更新・稼働率の発言は見つからず(欠損) | — | W2-19 | — |

### 2-4. NVIDIA 側の発言(旧世代の稼働)

| 項目 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Kress(CFO) | 「6 年前に出荷した A100 がフル稼働している」と Burry への反論の文脈で述べたと報じられる。説明会の逐語は未確認。四半期は Q3 FY26(2025-11)か Q4 FY26(2026-02)かで要約が割れる | 2025-11〜2026-02 | W2-13、W2-26 | 3* |
| Huang | 2026-08-11 の寄稿「AI Factory Compute Is Becoming an Investable Asset Class」で「A100 fleet は 2020 年から 2029 年まで稼働可能(mission-capable)」「Fungibility drives utilization and extends durability, making NVIDIA compute a productive asset: rentable, durable and financeable」 | 2026-08-11 | W2-26 | 3* |
| Huang(X の返信) | 「NVIDIA compute is fungible, durable and highly rentable」(2026-09-07 の投稿、タイムスタンプは未検証) | 2026-09-07 | W2-26 | 4* |

### 2-5. 2026 年に A100 が貸し出されているか

- CoreWeave の A100 契約が 2029 年まで(2-2)。
- 2026 年 3 月時点でクラウド掲載価格は $1.19〜$3.43(1-2、掲載元により範囲が異なる)。
- technews(2026-08-04)は「A100・H100・H200 の貸出料が複数世代で同時に上昇」と報じる。別の記事は「A100 の貸出価格は大きく低下」とも書く(第 6 章に併記)。
- UOB のレポート(2026-06)は「H100・A100 の堅調さは、旧世代が座礁資産という見方への反証」と記述(推論・解釈を含む)。(W2-19、W2-24)
- Oracle の更新対象の過半が 4 年以上前の GPU(2-1)。世代は非開示。

---

## 3. 減価償却年数の論争

### 3-1. 会計上の耐用年数(サーバー・ネットワーク機器)

| 企業 | 年数 | 変更・影響額 | 出典 | Tier |
|---|---|---|---|---|
| Oracle | 5 → 6 年(FY2025 期初から)。FY2026 の 10-K も 6 年 | FY25 の営業費用 -$733M、純利益 +$573M(既S4 再掲) | 既S4 | 再掲 |
| Amazon | 一部のサーバー・ネットワーク機器を 6 → 5 年(2025-01-01 適用) | 2025 年: 減価償却・償却 約 +$1.4B、純利益 -$1.0B、主に AWS(10-K FY2025)。S4 の 10-Q 要約(9 か月 -$677M)から Q4 単独は約 -$323M(算出: 1,000 - 677) | W2-07 | 1* |
| Amazon(過去) | 2022 年に 4 → 5 年(FY2022 10-K、ハードウェアとデータセンター設計の改善を理由に記載)、2024 年に 5 → 6 年(The Register) | 2024 年 Q4 に一部設備の早期除却で加速償却 約 $920M(Deep Quarry、個人ブログ) | W2-07 | 1*(10-K)/ 3〜4* |
| Microsoft | 4 → 6 年(FY2023 適用) | FY23 営業利益 約 +$3.7B(既S4 再掲、W2-18 も同数) | 既S4 | 再掲 |
| Alphabet | 4 → 6 年(2023 年適用) | 2023 年の減価償却 -$3.9B(既S4 再掲) | 既S4 | 再掲 |
| Meta | 5.5 年(2025-01-01 適用)。3 年間に 3 回延長し最新が 2025-01(W2-23) | 2025 年の減価償却 -$2.92B、純利益 +$2.59B(既S4 再掲) | 既S4、W2-23 | 再掲 / 3〜4* |
| CoreWeave | 6 年(2023 年初に 5 → 6 年) | 変更は上場前(既S4 再掲) | 既S4 | 再掲 |
| Nebius | 4 年とされるが、今回の検索で確認できず(欠損) | — | W2-18 | — |
| 2026 年の変更 | Microsoft・Alphabet・Meta の 2026 年 10-Q での変更は見つからず(既S4 と同じ) | — | W2-23 | — |

- David Rosenthal のブログ(2026-02)は「2020 年以降ハイパースケーラーは耐用年数を延長し続け、2025 年に Amazon だけが逆方向」と記述(W2-23)。Tier 4*。

### 3-2. Amazon の短縮の理由(10-K FY2025 の要約)

- 文言(要約): 一部のサーバー・ネットワーク機器の見積耐用年数を 6 年から 5 年に変更(2025-01-01)。理由は技術開発の加速、特に AI と機械学習。(W2-07、Tier 1*)
- 個人ブログ(Behind the Balance Sheet)の解釈「AI ワークロードの性能要求が耐久性の利点を上回った」は筆者の推論で、Amazon の記載ではない。(W2-07、Tier 4*)

### 3-3. 批判側の推計

| 項目 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Burry の主張 | ハイパースケーラーは Nvidia チップ(実際の寿命は 2〜3 年と彼は主張)を購入しつつ耐用年数を延ばし、費用を先送りして純利益を押し上げている | 2025-11(X への投稿) | W2-08 | 3* |
| Burry の推計額 | 2026〜2028 年の減価償却の過小計上が累計 **$176B**。2028 年までに Oracle の利益を約 27%(S3: 26.9%)、Meta を約 21% 過大 | 2025-11 | W2-08、既S3・既S4 | 3* |
| Burry の図の内容 | Meta のネットワーク機器 3 → 5.5 年(2025)、Alphabet 3 → 6 年、Oracle 5 → 6 年、Amazon は 2025 年に 5 年へ短縮 | 2025-11 | W2-08 | 3* |
| 反論側の記述 | $176B は Burry 自身の推計。CNBC は「見積りの裁量が大きく証明は難しい」と報じる。各社は GAAP に従っていると説明。ハイパースケーラーの個別の応答は今回の要約に無し | 2025-11 | W2-08 | 3* |
| JPMorgan Asset Management の感応度 | GPU・ネットワーク設備を 3 年耐用で再計算した場合の 2025 年 EPS への影響: Amazon・Meta・Microsoft -7%、Alphabet -6%、Oracle -17% | 2026 年の記事での引用 | W2-23 | 3*(アナリストのシナリオで会社開示ではない) |
| 比較上の注意 | Burry は 2028 年までの累計、JPM は 2025 年 1 年の EPS と基準が異なり、同じ軸に置けない(Oracle: 約 27% と -17%) | — | W2-08、W2-23 | — |

### 3-4. Huang の「Blackwell が出たら Hopper はただでも要らない」

| 項目 | 内容 | 出典 | Tier |
|---|---|---|---|
| 発言の場 | GTC 2025(2025-03)。Datacenter Dynamics(スペイン語版)の訳:「Blackwell が大量に出荷され始めたら、Hopper はただでも引き取り手がない」 | W2-09 | 3* |
| 文脈 | 同記事は「ジョーク」と書き、聴衆の多くが Hopper を保有する NVIDIA 顧客だったため「痛いところを突いたかもしれない」と記述。英語の逐語と前後の文は今回確認できず | W2-09 | 3* |
| その後の発言 | 2026-08-11 の寄稿と X で「NVIDIA compute is fungible, durable and highly rentable」、A100 は 2020〜2029 年稼働可能(2-4)。Huang が当該ジョークを撤回・訂正した発言は見つからず(欠損) | W2-26、W2-24 | 3* |
| 実態の数字(並置) | H100 の 1 年契約指数は 2025-10 の約 $1.70 から 2026-06 の約 $2.65(1-1)。Ornn は H100 が 2026-09 に 8 月より高いと表示(W2-26)。Nebius は 2026-10-01 に H100 定価を $4.50 へ改定 | W2-02、W2-26、W2-21 | 3* |
| 利益相反の指摘 | 分析記事は「Huang は GPU が耐久資産と市場が信じることで直接の利益を得る」と注記 | W2-26 | 3* |
| 反対側の見方 | チップの改善が加速すれば旧世代は 2〜3 年で経済価値を失うとの見方。Huang の反論は「旧世代は要求の高い AI から推論や小型モデルへ移ることで使い続けられる」 | W2-26 | 3* |

### 3-5. Nadella の発言

| 項目 | 内容 | 出典 | Tier |
|---|---|---|---|
| 発言(報道) | 「NVIDIA から学んだ最大の教訓の一つは、移行のペースが加速していること。これは重要な要素だ。**1 世代の製品について 4 年、5 年の減価償却を抱えたくない**」("I don't want to carry four or five years of depreciation on a single generation of products.")。出典記事の間で語句に揺れがある | W2-17 | 3*(日付・場は未確認) |
| 関連の報道 | 「新しい NVIDIA チップの最大の競合は一つ前の世代」と彼が述べたとする記述 | W2-17 | 3* |
| 「fungible fleet」の語 | 今回の 3 回の検索(W2-10、W2-14、W2-17)では Nadella の「fungible fleet」の逐語を確認できず(欠損)。Dwarkesh のポッドキャスト(2025-11)に Fairwater 2(合計 2GW 超)の見学と「CAPEX explosion」の節があるが、償却に関する発言は要約に出ない | W2-14 | 3* |
| Hood(CFO)の説明会発言 | 「今期と前期に稼働した GPU を全て Azure に割り当てていれば、Azure の成長率は既に 40% を超えていた」(Microsoft FY2026 Q2 の説明会。供給制約の説明であり償却の話ではない) | W2-17 | 3* |
| Maya 200 | 従来の fleet 比で TCO が 30% 超改善、推論と合成データ生成に展開(報道) | W2-17 | 3* |

### 3-6. 事実の並置(評価はしない)

| 内容 | 値 | 出典 |
|---|---|---|
| Oracle の会計上の耐用年数 | 6 年 | 既S4 |
| Oracle の Q1 FY27 に更新・再販された GPU | 過半が 4 年以上前 | W2-04 |
| CoreWeave の会計上の耐用年数 / A100 の最新契約期間 | 6 年 / 2029 年まで(2020 年発売から 9 年、算出) | 既S4、W2-05 |
| Amazon の一部機器 | 5 年(2025-01 から) | W2-07 |
| Burry の主張する実際の寿命 | 2〜3 年 | W2-08 |
| NVIDIA(Huang)の主張 | A100 は 2020〜2029 年稼働可能 | W2-26 |
| Microsoft の姿勢(Nadella、報道) | 1 世代に 4〜5 年の償却を抱えたくない | W2-17 |

---

## 4. 電力あたり性能と 1MW の経済

### 4-1. ベンダーの主張(tokens/MW)

| 比較 | 主張 | 条件・注意 | 出典 | Tier |
|---|---|---|---|---|
| Rubin NVL72 ÷ GB200 NVL72 | 約 10 倍の tokens/秒/MW | DeepSeek R1、同じ対話速度の目標。比較の基準は 2025 年初のソフトウェア構成の GB200(CoreWeave ブログ自身の記述) | W2-12 | 1*(CoreWeave 公式ブログ、ベンダー性能主張) |
| Rubin NVL72 ÷ GB300 NVL72 | 最大 30 倍の MW 当たりスループット | 160 tokens/秒/ユーザー、AgentX の DeepSeek V4 Pro。「SemiAnalysis の確認待ち」と記載 | W2-12 | 3* |
| Rubin NVL72 ÷ GB300 NVL72(独立の内訳) | 100 TPS で Rubin 59.4M、GB300(Dynamo SGLang)28.5M、GB300(Dynamo TRTLLM)21.1M tokens/秒/MW。強い方の GB300 に対し 2.09 倍(算出: 59.4 ÷ 28.5 = 2.08、59.4 ÷ 21.1 = 2.82) | 差はサービング・エンジンに強く依存 | W2-12 | 3* |
| Rubin の「67 倍」の主張 | 見出しは「67 倍の利得は 60〜100 TPS で 1.4〜3 倍」(本文は未読) | 見出しのみ | W2-12 | 3* |
| GB300 NVL72 ÷ H200 NVL8 | DeepSeek V4 Pro 1.6T で最大 15 倍、Kimi K3 2.8T で約 80 倍の MW 当たりスループット | H200 との比較(H100 ではない) | W2-12 | 3* |
| Blackwell(B200)の MW 当たり値 | 今回の検索では取得できず(欠損) | — | W2-12 | — |

### 4-2. SemiAnalysis InferenceX(旧 InferenceMAX)の GB200 NVL72 と H100 の比較

| モデル・速度 | GB200 NVL72 | H100 | 備考 | 出典 | Tier |
|---|---|---|---|---|---|
| gpt-oss 120B、117 tokens/秒/ユーザー | 18,899 tokens/秒/GPU、$0.03/百万トークン | 2,622 tokens/秒/GPU、$0.14/百万トークン | GPU 当たり 7.2 倍(算出: 18,899 ÷ 2,622)、単価は 4.7 倍安い(算出: 0.14 ÷ 0.03) | W2-20 | 3* |
| DeepSeek R1、41 tokens/秒/ユーザー | 5,383 tokens/秒/GPU、$0.11 | 269 tokens/秒/GPU、$1.35 | GPU 当たり 20.0 倍(算出: 5,383 ÷ 269)、単価は 12.3 倍安い(算出: 1.35 ÷ 0.11) | W2-20 | 3* |
| MiniMax M3 428B、52 tokens/秒/ユーザー | $0.38 / $0.43(2 つの値、要約では区別不明) | 要約に無し | GB200 が安い | W2-20 | 3* |
| MiniMax M3 428B、87 tokens/秒/ユーザー | 要約に無し | 要約に無し | H100 が安い | W2-20 | 3* |
| MiniMax M3 428B、122 tokens/秒/ユーザー | 211 tokens/秒/GPU、$2.86 | 271 tokens/秒/GPU、$1.32 | H100 が GPU 当たり 1.28 倍、単価は 2.17 倍安い(算出: 271 ÷ 211、2.86 ÷ 1.32) | W2-20 | 3* |
| MiniMax M2.5/M2.7(tokens/秒/MW) | 約 1.58M | 約 356K | 約 4.4 倍(算出: 1.58M ÷ 356K)。行と列の対応は要約の表順からの推定で未検証。MW 当たりの値が載るのはこのモデルのみ | W2-20 | 3* |
| InferenceX が置く単価 | GB200 NVL72 $1.86/チップ時、H100 $1.17/チップ時(2026-07 の調査)。旧設定: $2.21 と $1.30(2025-08 の調査) | — | 定義(所有コスト基準かレンタル基準か)は要約から不明。1-1 の市場価格(H100 約 $2.5〜$3.3)とは別の水準 | W2-20 | 3* |

### 4-3. ラック電力・GPU 当たり電力・1MW 当たり GPU 数

| 項目 | 値 | 出典 | Tier |
|---|---|---|---|
| GB200 NVL72 のラック電力 | 約 120 kW | W2-25 | 3〜4* |
| GB300 NVL72 のラック電力 | 132〜140 kW(ピーク 155 kW)。Gigabyte の仕様は最大 140 kW、他に持続 120 kW・混合精度の学習中ピーク 120.8 kW とする記述もあり | W2-25 | 1*〜4* |
| B300 の GPU 当たり TDP | 1,460 W(参照アーキテクチャ)/ 約 1,400 W(別の記述) | W2-25 | 3〜4* |
| NVL72 の GPU 当たりラック電力(算出) | 120 ÷ 72 = 1.67 kW、132 ÷ 72 = 1.83 kW、140 ÷ 72 = 1.94 kW | 算出 | — |
| 1MW(ラック電力のみ)当たりの GPU 数(算出) | 1,000 ÷ 1.94 = 514 基、1,000 ÷ 1.67 = 600 基(冷却・ネットワーク・PUE を含まない) | 算出 | — |
| H100・H200・B200 の GPU 当たり電力、DGX の電力 | 欠損(今回の検索で出典を取得できず) | W2-25 | — |
| Vera Rubin NVL144/NVL72 のラック電力 | 欠損 | W2-25 | — |

### 4-4. 1GW の投資額(Huang 発言)

| 項目 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| 1GW の建設費 | 「1GW のデータセンターは $50〜60B、うち NVIDIA のチップとシステムが約 $35B」と投資家に述べたと報じられた | 2025 年(OpenAI 契約の報道期。正確な日付は未確認) | W2-11 | 3* |
| 別の数字 | Crypto Briefing は「1GW の AI ファクトリーは最大 $100B」と書き、$50〜60B を「2025 年中盤の従来推計」と位置づける。より確かな出典では未確認 | 不明 | W2-11 | 4* |
| 売上の主張(二次) | 「1GW の NVIDIA ファクトリーは年 約 $50B を生む」(Digg の投稿。YouTube チャンネルの二次情報) | 不明 | W2-11 | 4* |
| 算出 | NVIDIA の取り分比率 = 35 ÷ 60〜35 ÷ 50 = 58%〜70%。NVIDIA 以外(建屋・電力・冷却等)= $15〜25B/GW = $15〜25M/MW。総額 $50〜60M/MW、うち NVIDIA $35M/MW | 算出 | — | — |
| 既存調査との並置 | CoreWeave の追加電力 1MW 当たり設備投資は 約 $18.8M/MW(既R7 の粗い参考値) | 既R7 | 再掲 | 再掲 |

### 4-5. 1MW 当たり売上(定義別の値。単位が揃わない)

| 区分 | 値(M USD/MW・年) | 式・条件 | 出典 |
|---|---|---|---|
| CoreWeave の実績(売上 ÷ アクティブ電力) | 6.9〜8.2 | 既R7 の算出(再掲) | 既R7 |
| Oracle の会社例示(6 年・1GW・$60B) | 10 | 60B ÷ 6 年 ÷ 1,000MW(再掲) | 既S1・既R7 |
| Oracle の OpenAI 契約の推計 | 13.3 | 約 $300B ÷ 5 年 ÷ 4.5GW(再掲) | 既R7 |
| Nebius の大型 4 案件 | 20〜25 | 株主レターの要約(再掲) | 既R7 |
| NVL72 の定価ベース(上限、稼働率 100%)(算出) | GB200 $8.00/時: 36.0〜42.0。GB200 $10.50/時(CoreWeave 定価、既R3): 47.3〜55.2。GB300 中央値 $18.00/時: 81.1〜94.6 | 単価 × 8,760 時 × 514〜600 基。例: 10.50 × 8,760 × 514 = $47.3M、× 600 = $55.2M。ラック電力のみを 1MW とみなした場合 | 算出 |
| 契約値から逆算した GPU 時単価(算出) | $10M/MW → $1.90〜2.22/時。$13.3M → $2.53〜2.95。$20〜25M → $3.81〜5.55 | 式: 契約値 ÷ (514〜600 基 × 8,760 時)。1MW を NVL72 のラック電力と等置した場合のみ成り立つ(MW の定義は出典が区別しない) | 算出 |
| Huang の売上主張(二次) | 約 50 | 年 $50B ÷ 1,000MW(Digg の二次情報) | W2-11 |

- 世代別(H100 / B200 / GB300 / Rubin)の 1MW 当たり売上は、出典付きの値が今回見つからなかった(欠損)。H100 の GPU 当たり電力が未取得のため、算出もできない。

### 4-6. 電力が制約のとき、旧世代の置換判断に使える事実(評価はしない)

| 材料 | 事実 | 出典 |
|---|---|---|
| 価格比(世代差) | B200 は H100 の 2.0 倍(Silicon Data)、B300 は 2.04〜2.11 倍(Nebius 定価) | 1-3 |
| 電力比 | NVL72 は GPU 当たり 1.67〜1.94 kW(ラック電力)。H100 の値は欠損 | 4-3 |
| ベンダーの MW 当たり性能 | GB300 は H200 比で最大 15 倍、Rubin は GB200 比で約 10 倍・GB300 比で最大 30 倍(独立集計は 2.09 倍) | 4-1 |
| 独立ベンチマーク | GB200 は H100 比で MW 当たり約 4.4 倍(MiniMax M2.5/M2.7、未検証の対応)。MiniMax M3 の 87・122 tokens/秒/ユーザーでは H100 の方が百万トークン単価が安い | 4-2 |
| 市場の需給 | 2026 年に H100 の価格は上昇、オンデマンドは売り切れ(SemiAnalysis の説明)。Hopper と Blackwell の価格が同時に上昇(Nebius 2026-10-01) | 1-1、1-2 |
| Rubin の出荷時期・価格 | 欠損 | — |
| 欠損 | 世代別の MW 当たり売上、旧世代を外して新世代に置換した実例の収益差 | 第 7 章 |

---

## 5. 中古 GPU の流通価格・残存価値

| 項目 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| H100 中古 ÷ 新品(Silicon Data の掲載分析) | 中央値は同時期の新品価格の約 61%(2024、発売後約 2 年)、約 69%(2025、約 3 年)。再生品は約 85%・約 84% | 2024〜2025 | W2-16 | 3* |
| H100 PCIe 80GB(ServerBuyback) | 中古 $14,000〜25,000、新品 $25,000〜34,000。中点比 66%(算出: 19,500 ÷ 29,500) | 2026-07 | W2-16 | 3〜4* |
| H100 PCIe(Compute Exchange) | 中古 $16,000〜20,000 | 2026 | W2-16 | 4* |
| H100 NVL 94GB(CCIR) | 掲載の中央値 $34,050、成約の中央値 $25,750(成約は掲載の 75.6%、算出: 25,750 ÷ 34,050) | 2026 | W2-16 | 3* |
| 中古 H100 のピーク | 2024 年中盤に最大 $50,000 → 供給増で急落 | 2024 | W2-16 | 3* |
| 2026 年の調査(範囲) | 中古 H100 $15,000〜28,000 | 2026 | W2-24 | 4* |
| 中古 A100 | 約 $7,800〜18,900(SKU・状態による)。2026 年中に購入価格がさらに 10〜15% 下がる見通しとする報告が 1 件(出典が弱い) | 2026 | W2-15 | 4* |
| 注意 | 掲載価格が中心で成約データは稀。IntuitionLabs の 2026 年 Q3 分析は「中古価格の数字は新品に対する市場全体の割引を示さない」と注記。SXM の中古価格系列は見つからず | 2026 | W2-15、W2-16 | 3〜4* |
| 参考(会計との基準の違い) | 中古の比率は「同時期の新品価格」が分母で、取得原価が分母の簿価(定額法の残存率)とは基準が異なるため、同じ軸で比較しない | — | 注記 | — |

---

## 6. 食い違い

| # | 項目 | A | B(ほか) | 扱い |
|---|---|---|---|---|
| 1 | 2026 年 8〜9 月の H100 の水準 | Silicon Data ネオクラウド $2.53(日付なし)〜$2.80 | Ornn $3.17〜$3.28、Akash 中央値 $3.37、AIMultiple $2.99、SemiAnalysis 1 年契約 $2.65(6 月)、Nebius 定価 $3.85 → $4.50、Lambda $3.29〜$3.99、ハイパースケーラー $7.19〜$7.52 | 系列の定義(スポット、1 年契約、定価、3 年リザーブ)が違うため併記。どれも採らない |
| 2 | CoreWeave の再契約価格 | Intrator(説明会): 旧世代 SKU は「数年前と同等以上」 | CFO 側の要約: 「約 1 年前と同等以上」。Q4 2025 説明会: H100 は年初比 10% 以内。CNBC 報道: H100 を元の 95% で再契約 | 基準時点(数年前、1 年前、年初、元の契約)が異なる。併記 |
| 3 | A100 の価格の方向 | CoreWeave の 2025 年 Q4 説明会(2025 年に上昇)、technews 2026-08-04(上昇) | 「大きく低下」とする記事、Kalshi の先物曲線(ほぼ横ばい)、「事実上のレガシー容量」とする記事 | 併記。A100 の統一指数は取得できず |
| 4 | A100 の掲載価格の範囲 | Jarvislabs $1.49〜$3.43 | DeployBase $1.19〜$1.48 | 集計元の違い。併記 |
| 5 | Kress の発言の四半期 | Q3 FY26(2025-11) | Q4 FY26(2026-02) | 原典未確認。併記 |
| 6 | Oracle の説明会日 | 2026-09-10(DCD) | 2026-09-11(1 件) | 併記 |
| 7 | 1GW の費用 | $50〜60B(NVIDIA 約 $35B) | 最大 $100B(Crypto Briefing、未確認) | 併記 |
| 8 | 1GW の年間売上 | 約 $50B(Digg、二次) | Oracle の例示 $10B/GW・年、OpenAI 契約の推計 $13.3B/GW・年(既R7) | 定義が違う。併記 |
| 9 | Rubin の優位 | NVIDIA 主張: GB300 比で最大 30 倍、GB200 比で約 10 倍 | 独立集計: 100 TPS で GB300 比 2.09 倍 | 条件(速度、エンジン、ソフトの世代)が違う。併記 |
| 10 | H100 の費用の置き方 | InferenceX: $1.17/チップ時 | 市場の契約価格 $2.35〜$2.65(1 年契約) | 定義が不明。併記 |
| 11 | Burry と JPM の影響額 | Burry: 2028 年までに Oracle の利益 約 27% 過大 | JPM AM: 3 年耐用なら 2025 年 EPS が Oracle -17% | 基準(累計 vs 単年、方向)が異なる。併記 |
| 12 | Nadella 発言の語句 | "I don't want to carry four or five years of depreciation on a single generation" | 出典記事ごとに語句が揺れる(要約) | 原典未確認 |
| 13 | Amazon の耐用年数の経路 | 10-K FY2025: 一部機器を 6 → 5 年(2025) | The Register: 2024 年に 5 → 6 年へ延長。FY2022 10-K: 2022 年に 4 → 5 年 | 年ごとの変更で矛盾ではない。経路として併記 |
| 14 | Nebius の値上げの公表 | Newsquawk: 確認済み | Benzinga: 報道時点で未確認 | 併記 |
| 15 | 2026-09-14 のスポット指数 $2.75 | 記事中の記述(発行元不明) | Silicon Data 2026-08-02 $2.80、SemiAnalysis 6 月スポット $2.42 | 指数の違い。併記 |

---

## 7. 欠損と試した検索語

| # | 欠損項目 | 試した検索語(検索番号) |
|---|---|---|
| 1 | 2023〜2024 年の世代別(A100・H100)時間単価の時系列 | "Silicon Data H100 rental index price per hour 2026"(W2-01)、"SemiAnalysis H100 one-year contract price index rising A100 H100 rental prices 2026"(W2-02)。履歴ページ(gpusmith 等)は検索結果に出たが内容は取得できず |
| 2 | 世代別の長期契約(3〜5 年)の時間単価(A100、H100、H200、B200、GB200、GB300) | W2-02、W2-06、W2-22。GB300 の長期契約の公表条件は見つからず |
| 3 | Oracle Q1 FY27 の公式トランスクリプト(話者、更新のみの単価、世代、対象数) | "Oracle Q1 fiscal 2027 earnings call transcript GPUs came up for renewal 20% premium Magouyrk"(W2-04) |
| 4 | Oracle の A100・H100 の別、契約期間 | W2-04 |
| 5 | Nebius の更新価格・稼働率の発言、Nebius の耐用年数 4 年の確認 | "Nebius useful life GPUs 4 years depreciation H100 contracts renewal pricing older GPUs 2026"(W2-18)、W2-21 |
| 6 | Lambda・Crusoe の H100/A100 契約更新価格・稼働率 | "Lambda OR Crusoe H100 A100 contract renewal pricing utilization older generation GPUs rebooked 2026"(W2-19) |
| 7 | CoreWeave の「95%」の説明会での逐語、CNBC 発言の日付 | "CoreWeave H100 contract renewal 95% of original price earnings call"(W2-03)、W2-05 |
| 8 | Nadella の「fungible fleet」の逐語・日付・場 | "Satya Nadella fungible fleet \"four or five years of depreciation\" one generation don't want to get stuck"(W2-10)、"Nadella Dwarkesh podcast fungible fleet Fairwater ..."(W2-14)、"Nadella \"fungible\" fleet Microsoft earnings call ..."(W2-17) |
| 9 | Huang の GTC 2025 発言の英語逐語、前後の文脈、訂正・撤回の発言 | "Jensen Huang \"give Hoppers away\" GTC 2025 Blackwell context later Hopper still fully utilized H100 prices rising"(W2-09)、W2-24、W2-26 |
| 10 | Kress の A100 発言の逐語と四半期 | "Colette Kress A100 GPUs shipped six years ago still running at full utilization ..."(W2-13) |
| 11 | H100・H200・B200 の GPU 当たり電力、DGX の電力、Vera Rubin のラック電力 | "DGX H100 10.2 kW DGX B200 14.3 kW GB200 NVL72 rack 120 kW GB300 NVL72 power per GPU watts Vera Rubin NVL144 rack power"(W2-25) |
| 12 | 世代別の 1MW 当たり売上、B200 の MW 当たりスループット | "tokens per second per megawatt H100 vs B200 vs GB300 NVL72 vs Vera Rubin revenue per megawatt throughput per watt"(W2-12)、"InferenceMAX SemiAnalysis H100 vs GB200 NVL72 tokens per megawatt cost per million tokens revenue per MW older GPUs"(W2-20) |
| 13 | Huang の「1GW $50〜60B」の発言日と一次出典(CNBC 等) | "Jensen Huang 1 gigawatt data center $50 to $60 billion Nvidia content $35 billion per GW"(W2-11) |
| 14 | Rubin の出荷時期と価格 | W2-12 |
| 15 | 2026 年の 10-Q での耐用年数変更(Microsoft・Alphabet・Meta) | "hyperscaler servers useful life 2026 Microsoft Alphabet Meta depreciation estimate change 10-Q 2026 GPU useful life debate"(W2-23)。確認できず(既S4 と同じ) |
| 16 | 残存価値(salvage value)の会計上の仮定 | 今回は検索せず(上限 26 回に達したため) |
| 17 | 中古 H100 SXM の系列、成約価格データ、ServNet UK「GPU residual value study 2026」の中身 | "used H100 resale price secondary market 2026 residual value NVIDIA H100 SXM server resale"(W2-16)。ServNet のページは見出しのみ |
| 18 | Ornn / Kalshi の A100 指数の現在値 | W2-06(先物曲線の A100 値のみ。Kalshi の A100 市場ページの見出しは確認できたが本文値は不明) |
| 19 | CME・Silicon Data の先物開始(2026-10-05)の一次確認 | W2-02 |
| 20 | Amazon の耐用年数短縮の説明会での追加説明、経営陣の発言 | W2-07(10-K の要約のみ) |

---

## 8. 出典一覧

### 8-1. 検索の一覧(検索 26 回、すべて WebSearch の standard)

| ID | 検索語 | 用途 |
|---|---|---|
| W2-01 | Silicon Data H100 rental index price per hour 2026 | H100 指数 |
| W2-02 | SemiAnalysis H100 one-year contract price index rising A100 H100 rental prices 2026 | 1 年契約指数 |
| W2-03 | CoreWeave H100 contract renewal 95% of original price earnings call | 再契約 95% |
| W2-04 | Oracle Q1 fiscal 2027 earnings call transcript GPUs came up for renewal 20% premium Magouyrk | Oracle の +20% |
| W2-05 | CoreWeave A100 contract through 2029 Intrator prior generation pricing at or above where it was years ago | A100 の 2029 年契約 |
| W2-06 | Ornn compute price index H100 B200 A100 price per GPU hour 2026 Blackwell rental price surge | Ornn・先物 |
| W2-07 | Amazon shortens useful life servers 6 years to 5 years 2025 10-K advancements in AI machine learning reason | Amazon の短縮 |
| W2-08 | Michael Burry depreciation $176 billion understated 2026-2028 hyperscalers useful life servers two to three years | Burry |
| W2-09 | Jensen Huang "give Hoppers away" GTC 2025 Blackwell context later Hopper still fully utilized H100 prices rising | Huang の GTC 2025 |
| W2-10 | Satya Nadella fungible fleet "four or five years of depreciation" one generation don't want to get stuck | Nadella |
| W2-11 | Jensen Huang 1 gigawatt data center $50 to $60 billion Nvidia content $35 billion per GW | 1GW の費用 |
| W2-12 | tokens per second per megawatt H100 vs B200 vs GB300 NVL72 vs Vera Rubin revenue per megawatt throughput per watt | tokens/MW |
| W2-13 | Colette Kress A100 GPUs shipped six years ago still running at full utilization installed base Nvidia earnings call | Kress |
| W2-14 | Nadella Dwarkesh podcast fungible fleet Fairwater not get stuck with one generation depreciation Microsoft | Nadella |
| W2-15 | A100 rental price per hour 2026 A100 80GB cloud still in demand price trend secondary market | A100 の価格 |
| W2-16 | used H100 resale price secondary market 2026 residual value NVIDIA H100 SXM server resale | 中古 H100 |
| W2-17 | Nadella "fungible" fleet Microsoft earnings call don't want to overbuy one generation GPU depreciation | Nadella |
| W2-18 | Nebius useful life GPUs 4 years depreciation H100 contracts renewal pricing older GPUs 2026 | Nebius |
| W2-19 | Lambda OR Crusoe H100 A100 contract renewal pricing utilization older generation GPUs rebooked 2026 | Lambda・Crusoe |
| W2-20 | InferenceMAX SemiAnalysis H100 vs GB200 NVL72 tokens per megawatt cost per million tokens revenue per MW older GPUs | InferenceX |
| W2-21 | Nebius raises on-demand GPU prices October 1 2026 H100 B300 increase | Nebius の値上げ |
| W2-22 | GB300 NVL72 B300 GPU rental price per hour 2026 neocloud contract GB200 price per GPU hour | B300・GB300 |
| W2-23 | hyperscaler servers useful life 2026 Microsoft Alphabet Meta depreciation estimate change 10-Q 2026 GPU useful life debate | 2026 の耐用年数 |
| W2-24 | Jensen Huang Hopper A100 old GPUs still valuable rental prices rising 2026 "Hopper" installed base utilization token demand | Huang の最近の発言 |
| W2-25 | DGX H100 10.2 kW DGX B200 14.3 kW GB200 NVL72 rack 120 kW GB300 NVL72 power per GPU watts Vera Rubin NVL144 rack power | ラック電力 |
| W2-26 | Jensen Huang "fungible, durable" GPUs A100 still running six years AI factory investable asset class H100 rental defends value | Huang の 2026-08 寄稿 |

### 8-2. URL(検索結果に出たもの。いずれも本文の原本は未読で、検索要約経由)

- W2-01: https://www.silicondata.com/products/silicon-index?gpu=h100 、https://xenospectrum.com/en/nvidia-gpu-rental-depreciation/ 、https://tech-insider.org/nvidia-blackwell-gpu-rental-price-surge-ornn-index-2026/ 、https://akash.network/the-bid/h100-rental-price-2026-cost-per-hour/ 、https://www.silicondata.com/blog/h200-vs-h100-rental-prices-may-july-2026(見出しのみ)
- W2-02: https://gpusmith.com/articles/en/h100-rental-price-history-trends 、https://www.aicoin.com/en/news-flash/2954859 、https://threadreaderapp.com/thread/2070341387283800179 、https://intuitionlabs.ai/pdfs/data-center-gpu-pricing-2026.pdf 、https://simplefunctions.dev/answer/h100max
- W2-03・W2-05・W2-13: https://letsdatascience.com/news/coreweave-secures-nvidia-a100-contract-through-2029-b3a23ed2 、https://xenospectrum.com/en/coreweave-a100-contract-2029/ 、https://hyper.ai/fr/stories/3ef0d9179a4ad4e314ed70ff9c8bda76 、https://theoutpost.ai/news-story/core-weave-extends-nvidia-a100-contracts-to-2029-proving-older-ai-gp-us-still-generate-profit-29732/ 、https://www.aol.com/articles/coreweave-crwv-q4-2025-earnings-165353917.html 、https://www.nasdaq.com/articles/coreweave-q1-earnings-call-highlights 、https://www.fortune.com/2025/11/10/coreweave-earnings-infrastructure-debt-ai-bubble
- W2-04: https://www.constellationr.com/insights/news/oracle-q1-strong-and-so-capital-expenditures 、https://www.datacenterdynamics.com/en/news/oracle-delivered-300000-gpus-in-q1-fy2027/ 、https://cryptobriefing.com/oracle-ai-contracts-renew-higher-rates/ 、https://cryptobriefing.com/oracle-q1-fy27-earnings-revenue-rpo/ 、https://betafinch.com/episodes/ORCL_2027_Q1_en 、https://kucoin.com/news/flash/oracle-renews-ai-gpu-contracts-at-20-higher-rates-amid-surging-demand
- W2-06: https://theinnermostloop.substack.com/p/the-first-tradable-compute-price 、https://www.miningstockeducation.com/2026/04/ornn-compute-price-index-added-to-bloomberg-terminal/ 、https://aiweekly.co/alerts/ornn-raises-33m-led-by-a16z-to-build-gpu-compute-futures-market 、https://sg.linkedin.com/in/wsayjon(Kalshi の先物曲線) 、https://futuresearch.ai/app/p/a/kalshi-kxh200ms-27jan-jun23
- W2-07: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm(Amazon 10-K FY2025) 、https://www.sec.gov/Archives/edgar/data/1018724/000101872423000004/amzn-20221231.htm(10-K FY2022) 、https://www.theregister.com/2025/02/07/amazon_q4_fy_2024/ 、https://deepquarry.substack.com/p/amazon-revises-server-lifespan-amid 、https://behindthebalancesheet.substack.com/p/amazons-ai-reality-check
- W2-08: https://www.streetinsider.com/General+News/Michael+Burry+warns+of+%24176+billion+depreciation+understatement+by+tech+giants/25584209.html 、https://www.itiger.com/news/1139425265 、https://davefriedman.substack.com/p/the-176-billion-accounting-question 、https://techstrong.ai/features/tech-investor-michael-burry-alleges-accounting-irregularities-at-hyperscalers-in-pursuit-of-ai-boom/ 、https://www.idnfinancials.com/news/58679/michael-burry-global-ai-giants-polish-profits-through-depreciation
- W2-09: https://www.datacenterdynamics.com/es/features/la-economia-de-las-nubes/
- W2-10・W2-14・W2-17: https://www.itiger.com/hans/news/1171588490 、https://longportapp.cn/news/265946691 、https://www.aol.com/articles/microsoft-msft-q2-2026-earnings-000320024.html 、https://poderato.com/shows/dwarkesh-podcast/satya-nadella-how-microsoft-is-preparing-for-agi 、https://wallstreetcn.com/articles/3759295
- W2-11: https://startupmap.iamsterdam.com/news/feed/nvidia-ceo-says-1-gigawatt-ai-facility-costs-50b--60b-boosting-neocloud-valuations 、https://techround.co.uk/news/openai-nvidias-100-billion-investment/ 、https://www.canberratimes.com.au/story/9327886/nvidia-wall-st-firms-plan-500b-ai-infrastructure-push/ 、https://cryptobriefing.com/nvidia-100b-ai-factory-cost/ 、https://digg.com/ai/80ba7g5n
- W2-12: https://www.coreweave.com/blog/nvidia-vera-rubin-nvl72-on-coreweave-10x-more-tokens-per-megawatt-than-blackwell 、https://www.digitalcitizen.life/nvidia-vera-rubin-delivers-up-to-30x-higher-agentic-ai-throughput-per-watt-than-blackwell/ 、https://fourweekmba.com/ai-semianalysis-vera-rubin-67x-vs-3x-speed-target/ 、https://www.remio.ai/post/openai-semianalysis-lens-vera-rubin-nvl72-beats-gb200-but-the-tco-case-is-narrow
- W2-15: https://jarvislabs.ai/blog/a100-price 、https://deploybase.ai/articles/a100-price 、https://dev.to/runcai/rent-an-a100-cloud-gpu-2026-pricing-workload-fit-and-setup-4j0n 、https://introl.com/blog/secondary-gpu-markets-buying-selling-used-hardware-guide-2025 、https://intuitionlabs.ai/articles/used-ai-gpu-prices-resale-trends 、https://simplefunctions.dev/odds/a100ms
- W2-16: https://www.silicondata.com/use-cases/h100-gpu-market-value-trends 、https://intuitionlabs.ai/pdfs/used-ai-gpu-prices-resale-trends.pdf 、https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/ 、https://www.servnetuk.com/research/gpu-residual-value-study-2026(見出しのみ) 、https://www.gpunex.com/blog/buying-selling-gpus-2026
- W2-18・W2-21: https://news.10jqka.com.cn/20260917/c680017427.shtml 、https://www.kucoin.com/news/flash/nebius-to-hike-gpu-rental-prices-by-up-to-21-from-october-1 、https://fourweekmba.com/ai-nebius-lifts-on-demand-gpu-prices-up-to-21-from-1-october/ 、https://www.spheron.network/blog/nebius-gpu-price-hike-2026-h100-to-b300-rates-rise-up-to-21/ 、https://www.newsquawk.com/headlines/nebius-nbis-hikes-prices-for-on-demand-cpu-and-gpu-services-will-raise-gpu-rates-for-nvidia-nvda-h100-h200-b200-and-b300 、https://www.benzinga.com/markets/tech/26/09/61837011 、https://spheron.network/blog/nebius-h100-h200-pricing-2026
- W2-19: https://finance.technews.tw/2026/08/04/nvidia-a100-h100-and-h200-gpu-rental-rates-continue-to-price-upwards/ 、https://www.uob.com.sg/assets/web-resources/private/pdfs/compute-is-revenue.pdf 、https://www.spheron.network/blog/nvidia-h100-news-2026/
- W2-20: https://inferencex.semianalysis.com/compare/deepseek-r1-gb200-vs-h100 、https://inferencex.semianalysis.com/compare/gptoss-120b-gb200-vs-h100 、https://inferencex.semianalysis.com/compare/minimax-m3-gb200-vs-h100 、https://inferencex.semianalysis.com/compare-per-dollar/minimax-m27-gb200-vs-h100 、https://newsletter.semianalysis.com/p/h100-vs-gb200-nvl72-training-benchmarks(見出しのみ)
- W2-22: https://akash.network/the-bid/b300-rental-price-2026-cost-per-hour/ 、https://getdeploying.com/gpus/nvidia-gb300 、https://www.spheron.network/blog/azure-gb300-pricing-2026/ 、https://io.net/p/gb300-nvl72-cloud-rental-how-to-access-nvidias-blackwell-ultra-architecture-in-2026 、https://www.gmicloud.ai/en/blog/rent-gb200-gb300-on-demand-lead-times 、https://telnyx.com/resources/nvidia-b300-pricing
- W2-23: https://fourweekmba.com/ai-nvidia-gpu-depreciation-durability-debate-huang-2026/ 、https://blog.dshr.org/2026/02/mind-gaap-again.html 、https://appliedconjectures.substack.com/p/how-long-do-gpus-last-anyway-a-look 、https://algeriatech.news/hyperscaler-gpu-obsolescence-capex-cycle-2026/
- W2-24: https://parameter.io/nvidia-nvda-stock-gains-as-ceo-defends-value-of-h100-chip-rentals/ 、https://daily.dev/posts/nvidia-ai-factory-compute-is-becoming-an-investable-asset-class-mvkiasw47 、https://www.itiger.com/news/1185188896 、https://thundercompute.com/blog/ai-gpu-rental-market-trends
- W2-25: https://www.gigabyte.com/Enterprise/GIGAPOD-Pod-Scale/AI-DLC-POD_NVIDIA-GB300-NVL72 、https://introl.com/blog/why-nvidia-gb300-nvl72-blackwell-ultra-matters 、https://rdp.in/gpu-mart/knowledge-base/gb300-nvl72-anatomy-of-a-120-kw-rack-scale-ai-factory/ 、https://lenovopress.lenovo.com/DS0207 、https://www.supermicro.com/zh_tw/products/rack/srs-gb300-nvl72
- W2-26: https://fourweekmba.com/ai-nvidia-gpu-depreciation-durability-debate-huang-2026/ 、https://www.diariobitcoin.com/tecnologia/jensen-huang-defiende-la-durabilidad-de-los-gpus-a100-de-nvidia-hasta-2029/ 、https://hwbusters.com/news/coreweave-booked-nvidia-a100-through-2029-nine-years-of-rent-from-one-2020-gpu/ 、https://scanx.trade/stock-market-news/companies/nvidia-says-a100-gpus-mission-capable-through-2029/48162004

### 8-3. 既存調査(再掲元)

- 既S3・既S4: /tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research/S3_scuttlebutt.md 、同 S4_core_variables.md
- 既R3(競合価格)・既R7(電力・1MW 単位経済): /tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research2/R3_competition.md 、同 R7_capital_power.md
