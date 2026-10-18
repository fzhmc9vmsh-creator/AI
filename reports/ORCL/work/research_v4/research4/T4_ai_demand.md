# T4: AI 計算資源の需要の量と伸び(学習・推論・推論モデル・エージェント型 AI・ソブリン AI)

- 作成日: 2026-10-13 / 対象: Oracle(NYSE: ORCL)の AI インフラ事業の需給の見通し(需要側)
- 範囲: 事実・数値・出典の整理のみ。投資判断・推奨・評価は書かない。
- 取得手段: WebSearch のみ。26 回 / 上限 26 回を使い切った(standard 25 回、extended 1 回 = T4-26)。WebFetch は使えない。
- **原本(会社の決算説明会書き起こし、Google/Anthropic のブログ本文、調査会社の報告書本文、Bloomberg/FT/WSJ 記事)は 1 件も直接開いていない。数値はすべて検索ツールの要約に書かれていた内容。** そのため会社開示由来でも Tier に `*` を付ける。多くの二次・三次の要約(集約サイト、アグリゲーター、SNS 引用)は互いに引用し合っており、独立した確認になっていない。
- Tier: 1=会社開示, 2=規制当局・公的統計, 3=報道・アナリスト・調査会社, 4=ブログ・SNS・集約サイト。`*`=検索要約経由。「(算出)」は調査者の計算(式を併記)。「欠損」は見つからなかったもの(試した検索語を 5 節に記載)。
- 出典 ID `[T4-nn]` は「nn 番目の検索」(6 節に URL)。1 回の要約が複数サイトを統合しているため、個別の数値がどの URL 由来かを特定できない場合がある。`[W2]` `[W3]` `[W5]` `[W8]` は /tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research3/ の既存調査(再掲のみ)。
- 今日は 2026-10-13。検索で拾えた最新の数値は 2026-09 末〜10-08 まで。

---

## 0. 要約(事実のみ、10 行)

1. **トークン処理量**: Google は月間 9.7T(2024-05)→ 480T(2025-05)→ 3,200T = 3.2 quadrillion(2026-05)。直近 1 年で 6.7 倍(算出: 3,200 ÷ 480)。ByteDance Doubao は日次 120T 超(2026-03、3 か月で倍増)で、月換算 3,600T(算出)。OpenAI API は 6B/分(DevDay 2025)→ 15B/分(2026-03)。Microsoft・Anthropic・Meta の総量は欠損。(1*, 3*)
2. **推論と学習の比率**: McKinsey(電力 GW)は推論 20.9GW(2025)→ 93.3GW(2030)、年 35%。学習 23.1 → 62.2GW。推論の比率 47.5% → 60.0%(算出)。Futurum(支出)は 2025 年に推論が学習を逆転、2030 年 71.7%。Deloitte(計算量、二次引用)は推論が 2023 年 約 1/3、2025 年 約 1/2、2026 年 約 2/3。指標が違い直接比較できない。(3*)
3. **1 タスクの計算量**: Janus Henderson の記録で、DeepSeek(推論モデル)は非推論モデル比で 20 倍のトークン・150 倍の計算。Huang(GTC 2025)は推論モデルが「1 タスク 100 倍」。Anthropic の自社データで、エージェントはチャットの約 4 倍、マルチエージェントは約 15 倍のトークン。(1*, 3*)
4. **AI の売上(年換算)**: Anthropic は約 $9B(2025 末)→ $14B(2026-02)→ $30B 超(2026-04)→ $65B(2026-07、Bloomberg 引用の集約サイト)。OpenAI は $24B(2026-03-31)→ $40B 超(2026-08)→ 約 $50B(Bloomberg、2026-10-08)〜約 $70B(Axios/Reuters 引用、2026-09 下旬、OpenAI 未確認)。AWS の AI 事業は年換算 $25B 超(2026 Q2)。(1*〜4*)
5. **クラウドの成長と制約**: Google Cloud 売上 $24.8B(+82%、2026 Q2)・受注残 $514B・「supply constrained」。Azure +43%(FY26 Q4)・次四半期ガイダンス約 45%・「需要が供給を上回る」(緩和時期は示さず)。AWS +36.7%・受注残 $496B。Nvidia データセンター売上 $89.0B(+117%、2026-07 期)、次四半期ガイダンス $108B(中国の DC 計算売上を含まず)。(1*, 3*)
6. **投資額の予測**: Goldman は米大手 5 社(Amazon・Alphabet・Microsoft・Oracle・Meta)の AI インフラ投資を 2027 年 $1.2T(+54%、上振れ $1.4T)、2026〜2031 年の累計 $7.6T。BofA(2026-07)は 2026 年 $730B、2027〜2028 年は年 $1T 超。Morgan Stanley の 2026 年 $805B・2027 年 $1.116T は [W3] の再掲。(3*)
7. **GW の予測**: McKinsey(2025-04)の AI 容量 2030 年 156GW(追加 約 125GW。加速 +205GW、抑制 +78GW)。IEA は DC 電力 485TWh(2025)→ 945TWh(2030)。Morgan Stanley(2026-08)は米国の 2026〜2028 年の新規電力需要 68GW のうち 38GW が不足。Epoch は最大の学習ランが 2030 年に 4〜16GW。SemiAnalysis の 2026 年以降の数値は欠損。(2*, 3*)
8. **供給が追いつく時期**: 引用できた見方は「2027 年が制約のピーク、緩和は 2028 年以降」(主にメモリ。Intel CEO「2028 年まで救済なし」、FT 引用「2028 年以前は緩和しにくい」、Counterpoint「最短で 2027 年 Q4 に需給曲線が交差」)。Microsoft は容量を 2 年で約 2 倍にするが緩和の時期は示さず。電力・DC 用地・パッケージも別の制約。(3*)
9. **ソブリン AI**: Stargate UAE は 1GW(G42 建設、OpenAI と Oracle が運営、最初の 200MW は 2026 末予定)・UAE-US AI キャンパス 5GW。フランスは 1.4GW(2028 稼働予定)。EU は最大 5 か所の AI ギガファクトリー向け €20B 基金。Gartner のソブリンクラウド IaaS は 2026 年 $80B(+35.6%)。Oracle の国別投資は日本 $8B 超(10 年)、独 $2B・蘭 $1B(5 年)、英 $5B(5 年)。Nvidia のソブリン売上は欠損。(3*, 4*)
10. **Oracle の受注**: RPO $664B(2026-08-31、前年差 +$209B)、Q1 FY27 に AI 契約 $30B 超を追加、OCI 売上 $7.4B(+121%)。OpenAI との約 $300B 契約は約 4.5GW・約 5 年・2027 年から年 約 $30B(報道)。サウジ・独のソブリン案件の金額は欠損。(1*, 3*)

---

## 1. 推論と学習の比率、推論の計算需要の伸び(テーマ 1)

### 1-1. 比率の予測(指標が異なるため 4 系列を併記)

| 系列(指標) | 2023 | 2024 | 2025 | 2026 | 2027 | 2030 | 出典 | Tier |
|---|---|---|---|---|---|---|---|---|
| McKinsey: 推論の電力(GW) | 欠損 | 欠損 | 20.9 | 欠損 | 欠損 | 93.3(年 35%) | [T4-02] | 3* |
| McKinsey: 学習の電力(GW) | 欠損 | 欠損 | 23.1 | 欠損 | 欠損 | 62.2 | [T4-02] | 3* |
| 推論の比率(推論 ÷ (推論+学習)、算出) | — | — | 47.5%(20.9 ÷ 44.0) | — | — | 60.0%(93.3 ÷ 155.5) | 算出 | — |
| Futurum: 推論の支出の比率 | 欠損 | 学習と同水準(CY2024) | 推論が学習を上回る | 欠損 | 欠損 | 71.7%(推論 $106.8B、学習 $42.2B) | [T4-02] | 3* |
| Deloitte(二次引用): 推論の計算量の比率 | 約 1/3 | 欠損 | 約 1/2 | 約 2/3(推定) | 欠損 | 欠損 | [T4-02] | 3*(二次) |
| Introl(二次): 推論の計算量の比率 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 2029 年 65% | [T4-02] | 4* |
| Gartner: AI 最適化 IaaS($42B、2026)のうち推論向け | — | — | — | 55%(約 $23.1B、算出: 42 × 0.55) | 59% | 欠損 | [T4-02] | 3* |

- McKinsey の増分(算出): 推論 +72.4GW(93.3 − 20.9)、学習 +39.1GW(62.2 − 23.1)。増分に占める推論の比率 64.9%(算出: 72.4 ÷ 111.5)。学習の年率 21.9%(算出: (62.2 ÷ 23.1)^(1/5) − 1)。AI 合計 44.0GW → 155.5GW、年率 28.7%(算出)。
- McKinsey は 2030 年に推論が DC 総需要の 40% 超、学習は 30% 弱とも記述(要約)。2025 年は学習がわずかに大きい(GW 基準)。
- Futurum の合計(算出: 106.8 + 42.2)は $149.0B で、「AI プラットフォームのインフラ支出」という別の範囲。大手の capex($1T 超の予測)とは範囲が違う(2 節の食い違い)。Futurum の発表は 2026-08。
- 推論の計算需要そのものの年率(推論だけの成長率)を明記した出典は見つからなかった。代理指標はトークン処理量(2 節)。

---

## 2. トークン処理量の推移(テーマ 2)

### 2-1. 各社の実績

| 主体 | 指標 | 時点と値 | 伸び | 出典 | Tier |
|---|---|---|---|---|---|
| Google(全面) | 月間処理トークン | 9.7T(2024-05)→ 480T(2025-05)→ 3,200T(2026-05、I/O 2026) | 2024→2025 は 49.5 倍(算出: 480 ÷ 9.7)。2025→2026 は 6.7 倍(算出: 3,200 ÷ 480、会社は「約 7 倍」)。2 年で 330 倍(算出: 3,200 ÷ 9.7) | [T4-01] | 1*(会社発表の二次報道。未監査) |
| Google(API) | 毎分トークン | 約 19B/分(2026-05) | 月換算 820.8T(算出: 19B × 60 × 24 × 30)。全面 3,200T の 25.7%(算出) | [T4-01] | 1* |
| Google(顧客) | 年 1T トークン超を処理した Cloud 顧客 | 375 社超(過去 1 年、2026-05)。月間開発者 850 万人超 | 欠損 | [T4-01] | 1* |
| Google(Gemini アプリ) | 月間利用者 | 4 億(2025-05)→ 9 億(2026-05)。2026 Q2 決算で「約 10 億に接近」 | 2.25 倍(算出: 9 ÷ 4) | [T4-01][T4-16] | 1*〜3* |
| Microsoft(Foundry) | 年 1T トークン超の処理が見込まれる顧客数 | 250 社超(2026-01-28、FY26 Q2)→ 300 社超(2026-04-29、FY26 Q3) | +20%(算出: 300 ÷ 250 − 1)。Futurum は「前四半期比 30% 加速」と記述(食い違い) | [T4-05] | 1*/3* |
| Microsoft | 総トークン量 | 欠損 | 欠損 | [T4-05] | — |
| OpenAI(API) | 毎分トークン | 6B/分(DevDay 2025 時点、日付は要約に記載なし)→ 15B/分(2026-03) | 2.5 倍(算出: 15 ÷ 6)。15B/分は月換算 648T(算出: 15B × 43,200) | [T4-03] | 1*(アグリゲーター経由) |
| OpenAI(ChatGPT) | 週間利用者 | 9 億超(2026-02-27)→ 約 10 億(2026-07、OpenAI 広報が The Verge に) | +11%(算出: 10 ÷ 9 − 1) | [T4-03] | 1*〜3* |
| ByteDance Doubao | 日次トークン | 120T 超(2026-03、Volcano Engine 発表。3 か月で倍増、2024-05 の公開時から 1,000 倍)。別の集約サイトは 180T 超(2026-06、未確認) | 月換算 3,600T(算出: 120T × 30)。Google の 3,200T と同じ桁(定義は別) | [T4-24] | 3*(180T は 4*) |
| OpenRouter(第三者ルーター) | 週間トークン | 4.6T(2025-09)→ 113T(2026-08、Digg 経由の技術者のグラフ)。別の報道は「週 90T 超(2026 年中盤)」「2024-01 から 9,000 倍」 | 24.6 倍(算出: 113 ÷ 4.6)。「エージェント型の日次トークン消費が 2026-02〜08 に 14 倍」(報道) | [T4-24] | 4* |
| Anthropic | 総トークン量 | 欠損(売上のみ。6 節) | — | — | — |
| Meta | 総トークン量・Meta AI 利用者 | 欠損 | — | [T4-24] | — |

- 単位換算(算出、30 日 = 1 か月): Google 全面 106.7T/日(3,200T ÷ 30)、Google API 27.4T/日(19B × 1,440)、OpenAI API 21.6T/日(15B × 1,440)、OpenRouter 16.1T/日(113T ÷ 7)。各社の定義(入力のみ/出力込み、キャッシュの扱い、検索の AI 要約を含むか)は未確認。
- Google 値は会社発表を二次報道が引用したもの。報道の一つは「自己申告・未監査で、消費電力は非開示」と注記。
- 1T トークンの価値について Tunguz の記事要約は「1T トークン ≒ 年売上 $5b」と記載しているが、$5/百万トークンなら 1T トークンは $5M(算出: 10^12 ÷ 10^6 × $5)で桁が合わない(食い違い)。この換算値は採用しない。

---

## 3. 推論モデル・エージェント型 AI の 1 タスクあたりの計算量(テーマ 3)

| 比較 | 倍率 | 条件・出典の記述 | 時点 | 出典 | Tier |
|---|---|---|---|---|---|
| 推論モデル vs 従来の推論(1 タスク) | 100 倍 | Huang の GTC 2025 での主張(報道: 「推論モデルは従来の推論 AI の 100 倍の計算を 1 タスクに要する」) | 2025-03 | [T4-06] | 1*〜3*(ベンダーの主張) |
| 推論モデル(DeepSeek)vs 非推論モデル(Meta のモデル) | トークン 20 倍・計算 150 倍 | Janus Henderson の記録。DeepSeek の応答の方が正確。Nvidia ではなく独立の資産運用会社の記述 | 2025-03 | [T4-06] | 3* |
| 推論モデル vs 従来 LLM | 数百トークン → 1 ステップあたり数万トークン | Info-Tech の GTC 2025 要約。倍率は明記なし(算出: 数万 ÷ 数百 = 数十〜数百倍の幅) | 2025-03 | [T4-06] | 3* |
| エージェント vs チャット | 約 4 倍 | Anthropic の自社データ(エンジニアリング記事) | 2025-06 | [T4-17] | 1* |
| マルチエージェント vs チャット | 約 15 倍 | 同上。トークン使用量だけで性能のばらつきの 80% を説明(ツール呼び出し数とモデル選択が他の 2 要因)。タスクの価値が高くないと割に合わないとも記述。コーディングは並列化しにくい領域とも記述 | 2025-06 | [T4-17] | 1* |
| Claude Code の 1 タスクあたりトークン | 欠損 | 実測の公表値は見つからず(Simon Willison の定性的な記述のみ) | — | [T4-17] | — |

- 上記の倍率は 2025 年前半のもので、2026 年のモデル・エージェントで再測定した値は見つからなかった。
- 需要側の実績との対応(算出なし、並記のみ): OpenRouter の「エージェント型ワークロードの日次トークンが 2026-02〜08 に 14 倍」(4*)、Claude Code の年換算売上 $2.5B 超(2026-02、二次報道)。
- Epoch(2025): 最先端の学習計算量は年 4〜5 倍で増加。最大の学習ランの電力は年 2.2 倍(算出なしの引用)。[T4-22] 3*

---

## 4. ソブリン AI(テーマ 4)

### 4-1. 各国・地域の計画

| 国・地域 | 計画 | 規模 | 時期 | 出典 | Tier |
|---|---|---|---|---|---|
| UAE(Stargate UAE) | G42・OpenAI・Oracle・Nvidia・SoftBank・Cisco が発表。G42 が建設、OpenAI と Oracle が運営。Nvidia GB300 を供給。OpenAI の「OpenAI for Countries」の第 1 号 | 1GW のクラスター。UAE-US AI キャンパス全体は 5GW(残り 4GW は米ハイパースケーラーと協議中) | 2025-05-22 発表。最初の 200MW は 2026 年末までの予定(G42 の Al Kaissi、GITEX 2025)。稼働の確認は見つからず | [T4-25][T4-08] | 3* |
| サウジアラビア | Humain。ある一覧は $100B(Tier 4)。「数十万個の Nvidia 最上位チップを 5 年で購入」 | GW は欠損 | 5 年 | [T4-08] | 4* |
| フランス | MGX・Bpifrance・Mistral・Nvidia の合弁。欧州最大の AI キャンパス(パリ地域) | 1.4GW | 着工 2026 年下半期、稼働 2028 年 | [T4-08] | 3*/4* |
| EU | 最大 5 か所の「AI ギガファクトリー」向け基金 | €20B | 欠損 | [T4-08] | 3*/4* |
| インド | GPU を 5 倍にして 100,000 個(2026 年末) | 金額は欠損 | 2026 年末 | [T4-08] | 4* |
| 韓国 | GPU 260,000 個を展開 | 金額は欠損 | 欠損 | [T4-08] | 4* |
| 米国(Stargate) | 発表額 $500B。JPMorgan 推計で 10GW・GB200 ラック 70,000 台相当 | 10GW | 欠損 | [T4-08] | 4* |
| 全世界(ベンダーブログの推計) | ソブリン AI の計算支出 2026 年 約 $100B。中東 約 $10B(UAE・サウジ 各 約 $4B)。公表された政府コミットメントと予算に基づく推計 | 約 $100B | 2026 | [T4-08] | 4*(GPU 販売業者のブログ) |
| 全世界(Gartner) | ソブリンクラウド IaaS の支出 | $80B(2026)、+35.6%。2025 年は 約 $59.0B(算出: 80 ÷ 1.356) | 2026 | [T4-18](Oracle Alloy 資料の引用) | 3* |

- Nvidia のソブリン AI 売上は、2 回の検索(T4-08、T4-14)で見つからなかった(欠損)。Nvidia の 2026-07 期は、データセンター $89.0B のうち「AI Clouds, Industrial & Enterprise」が $40.3B(+138%)で 45.3%(算出: 40.3 ÷ 89.0)、ハイパースケールが $48.7B(+102%)で 54.7%(算出)。ソブリンの内訳は非開示または未確認。[T4-14] 3*
- 要約には「relentless enterprise and sovereign demand」と記述されているのみで、金額はなし。

### 4-2. Oracle のソブリン・国別案件(確認できた範囲)

| 国・案件 | 内容 | 規模 | 時期 | 出典 | Tier |
|---|---|---|---|---|---|
| UAE: Stargate UAE | Oracle は運営側(OpenAI と共に)。Oracle の契約額は欠損 | 1GW(最初の 200MW は 2026 年末予定) | 2025-05 発表 | [T4-25] | 3* |
| 日本 | 公共クラウドリージョン(東京・大阪)の拡張、ソブリン運用チーム | $8B 超 / 10 年 | 発表日は要約に記載なし | [T4-18] | 3* |
| 日本: SoftBank | Oracle Alloy によるソブリンクラウド。東日本 2026-04、西日本 2026-10 の予定 | 金額・GW は欠損 | 2026 | [T4-18][T4-07] | 3* |
| ドイツ | フランクフルトの AI 容量等 | $2B / 5 年 | 発表日は要約に記載なし | [T4-18] | 3* |
| オランダ | アムステルダムの AI 容量等 | $1B / 5 年 | 同上 | [T4-18] | 3* |
| 英国 | OCI 拡張、英国ソブリンクラウドで政府・防衛向け AI | $5B / 5 年 | 2025-03 | [T4-18] | 3* |
| サウジアラビア | Oracle の契約は見つからず | 欠損 | — | [T4-07][T4-18] | — |
| 米国: OpenAI(Stargate) | 約 $300B・約 4.5GW(報道は 5GW 超とも)・約 5 年。2027 年から Oracle の売上に年 約 $30B。Abilene は Crusoe が建設・所有、Oracle が機器と運用 | 4.5GW | 2025-09 契約。施設の稼働は早ければ 2026 年夏、完成目標は 2027 年初(Bloomberg 引用) | [T4-07] | 3* |

- Oracle Q1 FY27(2026-09-10 発表)の決算発表の要約には「sovereign」の記載が見つからなかった。ソブリン案件単独の RPO は欠損。[T4-09]
- 国別投資額(日本・独・蘭・英)は「投資計画」であり、顧客契約額(RPO)ではない。

### 4-3. Oracle の直近の受注・売上(再確認のみ。詳細は [W5] 8 節)

| 指標 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| RPO | $664B(前年差 +$209B。前年は 約 $455B、算出: 664 − 209。前年比 +45.9%、算出)。前四半期差 +$26B([W5]) | 2026-08-31(Q1 FY27) | [T4-09][W5-22] | 1* |
| 新規 AI クラウド契約 | $30B 超(追加の資金調達への影響なしと説明) | Q1 FY27 | [T4-09] | 1* |
| 売上・OCI | 総売上 $19.3B(+30%)、OCI $7.4B(+121%。前年 約 $3.35B、算出: 7.4 ÷ 2.21)、クラウドアプリ $4.2B(+10%) | Q1 FY27 | [T4-09] | 1* |
| マルチクラウド | マルチクラウドのデータベース売上 +353%、顧客数 +180% | Q1 FY27 | [T4-09] | 1* |
| RPO の認識時期 | 「約半分が 36 か月以内」(単一の二次要約)。[W5] の 10-Q 要約は「約 13% が 12 か月以内」。Q4 FY26 は 12% が 12 か月以内、34% が 13〜36 か月(合計 46%、算出)。 | Q1 FY27 | [T4-09][W5] | 3*/1* |
| FCF・資金 | FCF −$5B。$20B の ATM(市場売出し)の株式売却を完了 | Q1 FY27 | [T4-09] | 1* |

---

## 5. AI データセンター需要の定量予測(GW・投資額、2026〜2032)(テーマ 5)

### 5-1. 容量(GW)・電力の予測

| 出典(予測の作成時期) | 内容 | 値 | 対象年 | Tier |
|---|---|---|---|---|
| McKinsey「Cost of compute」(2025-04) | AI 関連 DC 容量(ベース: continued momentum) | 156GW。2025〜2030 年の追加 約 125GW(The Register は 124GW)。2025 年の水準は 約 31GW(算出: 156 − 125) | 2030 | 3* |
| 同上 | 加速シナリオ / 抑制シナリオ | 追加 約 205GW($7.9T)/ 追加 約 78GW($3.7T)。ベースは $5.2T。幅は 2.6 倍(算出: 205 ÷ 78) | 2030 | 3* |
| 同上 | DC 総需要(AI + 従来) | 約 219GW。新規需要の約 70% が AI。総額 $6.7T(AI $5.2T、従来 $1.5T) | 2030 | 3* |
| McKinsey「AI workloads」チャート(作成時期は要約に記載なし) | AI の学習+推論の電力 | 44.0GW(2025、算出)→ 155.5GW(2030、算出) | 2025/2030 | 3* |
| IEA「Energy and AI」(2025-04。2026 年の改訂は確認できず) | DC の電力需要(ベース) | 485TWh(2025)→ 945TWh(2030)、年 14.3%(算出: (945 ÷ 485)^(1/5) − 1)。世界の電力の約 3%。AI 関連は約 3 倍 | 2030 | 2* |
| 同上(地域) | 米国 224 → 426TWh(年 13.7%、算出)、中国 117 → 277TWh(年 18.8%、算出) | 同上 | 2025→2030 | 2* |
| Morgan Stanley(2026-08、Crypto Briefing 経由) | 米国 DC の新規電力需要 68GW(2026〜2028)のうち 30GW は建設中・契約済みの系統でカバー、残り 38GW が不足(算出: 68 − 30 = 38) | 38GW | 2026〜2028 | 3* |
| Morgan Stanley(別の要約) | 総ギャップ 57GW、BTM 発電・燃料電池等の「plug-and-play」控除後の純ギャップ 32GW(同期間の総需要の 34%)。楽観 15GW、悲観 42GW | 32〜57GW | 2026〜2028 | 3*/4* |
| Morgan Stanley(2025-11) | 2028 年の電力ギャップ 約 44GW(従来予測 36GW から上方修正)。別の 2025 年版は 2025〜2028 年で 約 55GW | 44GW | 2028 | 3*/4* |
| Epoch AI(2025、EPRI と共同) | 最大の学習ランの電力。2030 年に 4〜16GW(年 2.2〜2.9 倍)。下限は既発表の複数 GW 級 DC と整合。GW 級 DC の建設は約 2 年(trends ページ) | 4〜16GW | 2030 | 3* |
| SemiAnalysis(2024-03、旧) | 世界の DC クリティカル IT 需要 96GW(うち AI 約 40GW) | 96GW | 2026 | 3* |
| SemiAnalysis DC モデル(有料) | 5,000 超の施設を追跡、2017〜2032 年をカバーと記載。2026 年以降の数値は見つからず | 欠損 | 〜2032 | 3* |
| Goldman(旧、The Register 経由) | DC 容量 +50% で 2027 年に 約 92GW | 92GW | 2027 | 3* |
| Bain / Structure Research / JLL / CBRE | [W3] の再掲(Bain: 追加 200GW・売上 $2T 必要・$800B 不足、Structure: 150GW、JLL: 北米建設中 66GW 超の 95% が先行契約、空室率 1%) | — | 2030 / 2026 | 3* |

### 5-2. 投資額(capex)の予測

| 出典 | 内容 | 値 | 対象年 | Tier |
|---|---|---|---|---|
| Goldman(2026-09 時点の報道) | 米大手 5 社(Amazon・Alphabet・Microsoft・Oracle・Meta)の AI インフラ投資 | 2027 年 $1.2T(+54%。2026 年は 約 $779B、算出: 1,200 ÷ 1.54)。上振れ $1.4T | 2027 | 3* |
| 同上 | 2028 年 | $1.4T(成長率が 12% に鈍化)という報道と、総額 $2T という報道が併存 | 2028 | 3*/4* |
| 同上 | 累計 AI インフラ支出 | $7.6T | 2026〜2031 | 3* |
| 同上 | 市場コンセンサス(2027) | $1.1T(一報道)/ 約 $920B(別の報道)。Goldman は 2026 年を通じて予測を上方修正と記述 | 2027 | 3* |
| BofA(2026-07) | ハイパースケーラーの capex | 2026 年 $730B。2027 年・2028 年は年 $1T 超。Evercore も 2027 年に $1T 超 | 2026〜2028 | 3* |
| Morgan Stanley([W3] 再掲) | 集計 capex | $805B(2026)、$1.116T(2027) | 2026/2027 | 3* |
| 会社ガイダンス(今回新規) | Microsoft FY27(2026-07〜2027-06)約 $175B。Google 2026 年 $195〜205B(従来 $180〜190B)。Amazon 2026 年 約 $220B(従来 約 $200B、主因はメモリ価格の上昇) | — | 2026〜2027 | 1*〜3* |
| McKinsey(2025-04) | AI 関連の累計 capex | $5.2T(ベース)、$3.7T(抑制)〜$7.9T(加速) | 〜2030 | 3* |
| OpenAI(会社資料の報道) | 計算への支出計画 約 $600B(2030 年まで。Altman の従来の $1.4T / 30GW から縮小)。2030 年売上見通し $280B 超 | $600B | 〜2030 | 3* |

### 5-3. 計算資源の供給側・需要側の実績(今回新規。四半期の決算)

| 指標 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Nvidia 売上 / データセンター | $96.2B(+106% 前年比、+18% 前四半期比)/ $89.0B(+117%、+18%)。前年同期のデータセンター 約 $41.0B(算出: 89.0 ÷ 2.17) | 2026-07-26 期(FY27 Q2) | [T4-14] | 1*/3* |
| Nvidia 次四半期ガイダンス | $108.0B ±2%(+12.3% 前四半期比、算出: 108 ÷ 96.2)。中国の DC 計算売上を含まず。粗利率 74.0% ±50bp | FY27 Q3 | [T4-14] | 1* |
| Nvidia FY2028 | 「CFO が 70% 成長を示唆、従来のコンセンサスは 45%」(中国語の単一報道。未確認) | 2026-08 | [T4-14] | 4* |
| Nvidia Vera Rubin | フル生産へランプ。CoreWeave・Google Cloud・Azure・OCI・Nebius 等で稼働 | 2026-08 | [T4-14] | 1*/3* |
| Google Cloud | 売上 $24.8B(+82%。前年同期 約 $13.6B、算出: 24.8 ÷ 1.82。年換算 $99.2B、算出)。営業利益 $8.8B(率 35.6%、前年 20.7%)。受注残 $514B(2026 Q1 は $460B 超)。「slightly more than half」が 24 か月で売上化(新規受注を除く算出: 514 × 0.5 ÷ 2 = 年 $128.5B 超)。既存顧客は契約を 50% 超上回る利用 | 2026 Q2(2026-07) | [T4-16] | 1*/3* |
| Google 供給 | 「we continue to be supply constrained」。第三者の容量も利用、Cloud の利益率を短期的に押し下げる見込み | 2026 Q2 | [T4-16] | 3* |
| Azure | +43%(FY26 Q4。FY26 Q2 は +38% cc)。FY27 Q1 ガイダンス 約 45%(cc)。需要は供給を上回り続ける。容量は新規分が「immediately monetized」。当四半期に 31 か所追加(年 88 か所)、1GW 追加、2 年で全体容量を 約 2 倍にする方向 | 2026-06 期 | [T4-15] | 1*/3* |
| Microsoft capex | FY27 約 $175B | 2026-07-29 | [T4-15] | 1* |
| AWS | 売上 +36.7%(18 四半期で最速)、年換算 約 $169B。受注残 $496B(3 か月前は $364B、+36%、算出: 496 ÷ 364)。AI 事業 年換算 $25B 超・前年比 3 桁成長。自社チップ事業も $25B 超。Anthropic・OpenAI と複数 GW の Trainium 契約。Amazon の 2026 年 capex を $200B → $220B に引き上げ(主因はメモリ価格) | 2026 Q2 | [T4-20] | 1*/3* |
| 3 社の受注残 | Microsoft $678B・Google $514B・AWS $496B の合計 $1,688B([W3] の再掲、時点が異なる) | 2026 Q2 | [W3] | 3* |

### 5-4. 供給が追いつく時期についての各社の見方

| 見方の主 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Microsoft(CFO Hood) | 需要は供給を上回り続ける。改善の時期の見通しは示さず。効率化で容量の納期が前倒しに | 2026-07-29 | [T4-15] | 3* |
| Google(Pichai) | supply constrained を継続。第三者容量も利用 | 2026-07 | [T4-16] | 3* |
| Creative Strategies | 2026 年の投資は 2027 年に寄与し始め、満額の効果は 2028 年。「2027 年が制約のピーク」 | 2026 | [T4-21] | 4* |
| Intel CEO | メモリは「2028 年まで救済なし」 | 2026 | [T4-21] | 3* |
| FT(アナリスト引用) | メモリの逼迫は 2028 年以前には緩和しにくい(新設工場の時間) | 2026 | [T4-21] | 3* |
| Counterpoint(Tarun Pathak) | メモリの需給曲線が交差するのは最短で 2027 年 Q4 | 2026 | [T4-21] | 3* |
| AMD CEO | 2027 年に CPU/GPU 供給を大幅に増やす | 2026 | [T4-21] | 3* |
| Primus Partners | 2027 年に中程度の緩和。プレミアム価格はインフラ全体の供給が増えるまで継続 | 2026 | [T4-21] | 3* |
| Micron CEO | AI のメモリ需要は「first innings」、供給はすでに不足 | 2026 | [T4-21] | 3* |
| SK Hynix CEO(二次) | 逼迫が 2030 年まで続く可能性(あまり確立されていない媒体。未確認) | 2026 | [T4-21] | 4* |
| 新設工場 | 主要な新工場の本格量産は 2030 年(要約の記述) | — | [T4-21] | 4* |
| Amazon(参考) | 2026 年 capex の引き上げ分(約 $20B)の主因は「メモリチップのコスト上昇」 | 2026 Q2 | [T4-20] | 3* |

- 要約は「電力・DC 空間・先端パッケージも制約で、メモリの緩和は GPU・電力の緩和と同じ速度ではない」と記述。
- 電力・変圧器・系統連系・DC の遅延の数値は [W3](GE Vernova 受注残 116GW、変圧器 128〜144 週、PJM 約 40 か月、2026 年計画の 1/3〜半分が遅延、Sightline: 計画 約 12GW に対し建設中 約 5GW)の再掲。今回の検索では追加できていない。
- 予測の時期と地平: 数値予測は 2030 年までが大半(McKinsey・IEA・Epoch・Bain)。Goldman は 2031 年までの累計、SemiAnalysis のモデルは 2032 年までをカバーするが数値は未取得。2032 年の数値は欠損。
- 予測の幅(算出): McKinsey の追加容量は 78〜205GW(2.6 倍)、Morgan Stanley の 2026〜2028 年ギャップは 15〜42GW、Epoch の 2030 年最大ランは 4〜16GW(4 倍)。

---

## 6. AI の売上の伸び(テーマ 6)

### 6-1. モデル提供者の年換算売上(run rate)

| 時点 | OpenAI | Anthropic | 出典 | Tier |
|---|---|---|---|---|
| 2025 末 | $20B 超(2025 年の run rate)。別の出典は 2025 Q4 の年換算 $16B | 約 $9B | [T4-03][T4-04][T4-19] | 3*/4* |
| 2026-02 | 欠損 | $14B | [T4-04] | 4* |
| 2026-03-31 | $24B(同じ出典は「Anthropic が OpenAI を上回った」と記述) | 欠損 | [T4-19] | 4* |
| 2026-04 | 欠損 | $30B 超(CNBC Disruptor 50 に関連する記事。[W3] の再掲) | [T4-04][W3-7] | 3* |
| 2026-07 | 約 $24B(一出典。他と整合せず) | $65B(Bloomberg 引用の集約サイト)。2026 Q2 の売上は $11.5B 超(同)または $10.9B(WSJ の予測) | [T4-03][T4-04] | 4* |
| 2026-08 | $40B 超(Bloomberg、CNBC が報じたとの記述。未確認) | 欠損 | [T4-03][T4-26] | 3*/4* |
| 2026-09 下旬 | 約 $70B(Axios・Reuters の情報源。エンタープライズ販売は 7 月から 2 倍超。OpenAI 未確認) | 欠損 | [T4-26] | 3*/4* |
| 2026-10-08 | 約 $50B(Bloomberg「投資家の期待より小さい」)。2026 年末に $70B 以上という見込みの報道あり | 欠損 | [T4-26] | 3* |

- Anthropic の伸び(算出): $9B → $65B = 7.2 倍(2025 末 → 2026-07、約 7 か月)。$9B → $14B = 1.56 倍、$14B → $30B 超 = 2.1 倍超、$30B 超 → $65B = 2.2 倍(算出)。Claude Code は年換算 $2.5B 超(2026-02、二次報道)。Q2 売上 $11.5B を年換算すると $46B(算出: 11.5 × 4)で、7 月の run rate $65B は時点値。
- OpenAI の伸び(算出): $24B(2026-03-31)→ 約 $50B(2026 年 9 月末、Bloomberg)= 2.1 倍(約 6 か月)。
- OpenAI の計算能力(CFO Friar): 0.6GW(2024)→ 1.9GW(2025)= 3.2 倍(算出)。2026-04 の株主向けメモで「確保済み 8GW 超、2030 年に 30GW を目標」(確保と稼働は別概念)。[T4-19] 3*
- OpenAI の会社見通し(報道): 2030 年売上 $280B 超(消費者と法人で半々)。[W3] は 2026 年売上見通し $36B、2026〜2030 年の FCF 累計 −$278B(再掲)。

### 6-2. クラウド各社の AI 売上と成長

| 事業者 | 指標 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|---|
| AWS | AI 事業の年換算売上 | $15B 超(2026 Q1、[W8] の再掲)→ $25B 超(2026 Q2)。定義が同じなら +67% 以上(算出: 25 ÷ 15 − 1)。前年比は 3 桁 | 2026 Q1→Q2 | [T4-20][W8-06] | 1*〜3* |
| AWS | 全体売上成長 / 受注残 | +36.7% / $496B | 2026 Q2 | [T4-20] | 1*/3* |
| Azure | Azure 等の成長率 | +38%(cc、FY26 Q2)→ 欠損(FY26 Q3)→ +43%(FY26 Q4)→ ガイダンス 約 45%(cc、FY27 Q1) | 2025-12 期→2026-06 期 | [T4-15] | 1*/3* |
| Azure | AI 事業の年換算売上 | 欠損(今回の検索で Microsoft 全体の AI run rate は見つからず) | — | — | — |
| Google Cloud | 売上成長 / 営業利益率 / 受注残 | +82% / 35.6% / $514B | 2026 Q2 | [T4-16] | 3* |
| Google Cloud | AI 売上の単独値 | 欠損 | — | [T4-16] | — |
| Nvidia | データセンター売上 | $89.0B(+117%) | 2026-07 期 | [T4-14] | 1*/3* |
| Oracle | OCI 売上 / RPO | $7.4B(+121%)/ $664B | 2026-08 期 | [T4-09] | 1* |

---

## 7. 食い違い(併記のみ。採否は決めない)

| # | 項目 | 値 A | 値 B | 違いの理由(分かる範囲) |
|---|---|---|---|---|
| 1 | OpenAI の年換算売上(2026 年 9〜10 月) | 約 $70B(Axios・Reuters の情報源、2026-09-29 前後の見出し) | 約 $50B(Bloomberg、2026-10-08「期待より小さい」)。2026-08 は $40B 超 | 未確認。一報道は「Anthropic との会計処理の違い(総額と純額?)で約 $20B 低くなった」と記述。OpenAI は公式に確認していない |
| 2 | OpenAI の 2025 末・2026 年の水準 | 2025 Q4 の年換算 $16B / 2026-03-31 $24B | 2025 年の run rate $20B 超 / 2026-07 約 $24B(一出典)/ [W3] 2026 年通期売上見通し $36B | run rate(時点値)と年間売上は別概念。2026-07 の約 $24B は 2026-08 の $40B 超と整合しない |
| 3 | Anthropic と OpenAI の大小 | 2026-03-31 に Anthropic が OpenAI を上回った(同じ出典で $24B) | 2026-07: Anthropic $65B、OpenAI 約 $24B〜$40B 超 | 売上の計上方法(クラウド経由の総額/純額)が異なる可能性。確認できず |
| 4 | ChatGPT の利用者 | 週間 9 億超(2026-02-27)→ 約 10 億(2026-07、OpenAI 広報) | 月間 10 億(2026-06、Reuters が Sensor Tower の推計を引用) | 週間と月間、会社発表と第三者推計。月間は週間以上のはずで、Sensor Tower と OpenAI の定義差 |
| 5 | Microsoft Foundry の年 1T トークン超の顧客 | 250 → 300 社超 = +20%(算出) | Futurum は「前四半期比 30% 加速」と記述 | 比較の基準(ペース見込みの顧客数 vs 実績)が異なる可能性。未確認 |
| 6 | 1T トークンの金額 | Tunguz 要約: 「$5/百万トークンで 1T トークンは年売上 $5b」 | 算出: 1T ÷ 1M × $5 = $5M | 要約の誤記または別の前提(顧客 1,000 社分の合計など)。採用しない |
| 7 | 2025 年の AI データセンター容量(McKinsey) | AI 学習+推論 44.0GW(AI workloads チャート、算出: 20.9 + 23.1) | 156 − 125 = 31GW(算出)、156 − 124 = 32GW(The Register の中位) | 「電力需要」と「AI 関連容量」で定義が異なる、または報告の版が違う可能性。未確認 |
| 8 | Morgan Stanley の米国電力ギャップ(2026〜2028) | 38GW(68 − 30、2026-08 の報道) | 総 57GW・純 32GW(別要約)。2025-11 版は 2028 年に 44GW、2025 年版は 55GW | 総/純(BTM 控除)、期間、版が異なる |
| 9 | Goldman の 2028 年の投資額 | $1.4T(成長率 12% に鈍化) | 総額 $2T(別報道)。算出: $1.2T → $1.4T は +16.7% で「12%」とも合わない | 範囲(米大手 5 社 vs 世界)や版の違いの可能性。2027 年のコンセンサスも $1.1T と 約 $920B に分かれる |
| 10 | 推論の比率(指標が別) | 電力 47.5%(2025)→ 60.0%(2030) | 支出: 2025 年に推論が上回り 2030 年 71.7%。計算量: 2025 年 約 1/2、2026 年 約 2/3。McKinsey の 2025 年は学習が電力で上回る | 電力(GW)、支出($)、計算量(FLOPs)の違い。Futurum の合計 $149B は大手の capex($1T 超)と範囲が別 |
| 11 | Oracle RPO の認識時期 | 「約半分が 36 か月以内」(一二次要約) | [W5] の 10-Q 要約: 約 13% が 12 か月以内。Q4 FY26 は 12 か月以内 12% + 13〜36 か月 34% = 46% | Q4 FY26 の 46% とは概ね整合。Q1 FY27 の 36 か月分は未確認 |
| 12 | OpenAI の計算への支出計画 | Altman の従来の約 $1.4T / 30GW | Reuters 報道: 約 $600B(2030 年まで、2026-02)。[W3] は契約集計 $1.15T〜$1.5T | 「契約額」「支出計画」「2030 年までの見込み」で範囲が異なる |
| 13 | Doubao の日次トークン | 120T 超(2026-03、Volcano Engine 発表の報道) | 180T 超(2026-06、集約サイト、未確認) | 時点が違う。後者は単一の低 Tier 出典 |
| 14 | OpenRouter の週間トークン | 週 90T 超(2026 年中盤、報道) | 113T(2026-08、技術者のグラフ) | 時点・集計の違い |
| 15 | Nvidia の「visibility」 | 今回の検索で「$1T の見通し」は確認できず | 一出典: 供給・容量義務 $105B。FY28 成長 70%(単一の中国語報道) | 未確認 |
| 16 | Microsoft の 2026 年 capex | 本調査: FY27(2026-07〜2027-06)約 $175B | [W3]: 暦年 2026 年 約 $190B | 期間の違い(会計年度と暦年) |
| 17 | AWS の AI 年換算売上 | $15B 超(Q1 2026、[W8]) | $25B 超(Q2 2026、本調査) | 定義が同じか未確認。Q1 は「最初の 3 年で」の文脈 |

---

## 8. 欠損と試した検索語

| 項目 | 状態 | 試した検索語(T4 番号) |
|---|---|---|
| Microsoft の総トークン量(四半期) | 欠損(1T トークン超の顧客数のみ) | 「Microsoft Foundry tokens processed trillion quarter Nadella earnings 2026 token volume」(T4-05) |
| Anthropic の総トークン量・API トークン | 欠損(売上のみ)。専用の検索は上限のため実施せず | 「Anthropic annualized revenue run rate 2026 billion Claude Code」(T4-04) |
| Meta のトークン量・Meta AI 利用者 | 欠損 | 「ByteDance Doubao daily tokens ... Meta AI monthly users tokens OpenRouter ...」(T4-24) |
| Azure / Microsoft の AI 売上の run rate | 欠損 | 「Microsoft Azure AI run rate capacity constrained through 2027 fiscal Q4 2026 Azure growth Hood」(T4-15) |
| Google Cloud の AI 売上の単独値 | 欠損 | 「Google Cloud Q2 2026 backlog revenue growth ...」(T4-16) |
| 推論だけの計算需要の年成長率(推論の FLOPs 年率) | 欠損 | 「inference share of AI compute demand 2025 2030 ...」(T4-02)、「Epoch AI inference compute demand growth ...」(T4-22) |
| Claude Code・エージェントの 1 タスクあたりトークンの実測(2026 年) | 欠損 | 「Anthropic multi-agent research system uses 15x ... Claude Code tokens per task ...」(T4-17) |
| 推論モデル/エージェントの倍率の 2026 年の再測定 | 欠損(2025 年前半の値のみ) | T4-06、T4-17 |
| Nvidia のソブリン AI 売上 | 欠損 | 「sovereign AI investment plans by country ... Nvidia sovereign AI revenue 2026」(T4-08)、「Nvidia Q2 fiscal 2027 results ... sovereign AI ...」(T4-14) |
| サウジ(Humain)の GW | 欠損($100B は Tier 4) | T4-08 |
| Oracle のサウジ・独・UAE のソブリン契約額 | 欠損(投資計画のみ。日本 $8B 超、独 $2B、蘭 $1B、英 $5B) | 「Oracle sovereign AI cloud contracts countries gigawatts Stargate UAE Saudi Japan Germany 2026」(T4-07)、「Oracle sovereign cloud investment billion Japan Germany ... 2026 announcement」(T4-18) |
| Oracle のソブリン案件単独の RPO | 欠損(Q1 FY27 の要約に sovereign の記載なし) | 「Oracle Q1 fiscal 2027 RPO remaining performance obligations multicloud sovereign September 2026」(T4-09) |
| Stargate UAE の稼働確認(200MW) | 欠損(2026 年末予定の発言のみ) | 「Stargate UAE 1 gigawatt 200MW 2026 OpenAI for Countries Norway India UK Korea ...」(T4-25) |
| OpenAI for Countries の他国案件(ノルウェー・インド・英・韓国) | 欠損 | T4-25 |
| IEA の 2026 年の改訂 | 欠損(2025-04 の数値のみ) | 「IEA Energy and AI 2026 data center electricity demand 2030 TWh forecast update」(T4-11) |
| McKinsey の 2026 年の改訂 | 欠損(2025-04 版のみ) | 「McKinsey AI data center capacity demand 2030 GW scenarios compute demand $ trillion 2026 update」(T4-10) |
| SemiAnalysis の 2026〜2028 年の GW | 欠損(有料。2024-03 の旧値のみ) | 「SemiAnalysis AI datacenter critical IT capacity forecast GW 2026 2027 2028 power constraint compute shortage」(T4-13) |
| Goldman・BofA の GW 予測 | 欠損(投資額のみ) | 「Goldman Sachs Morgan Stanley data center power demand gap GW 2028 2030 shortfall forecast 2026」(T4-12)、T4-23 |
| BofA の 2028 年の個別値 | 欠損($1T 超のみ) | T4-23 |
| 2031〜2032 年の GW・投資額 | 欠損(Goldman の累計 2031 年までのみ) | T4-23、T4-13 |
| 電力・変圧器・系統連系の追加データ | 今回は検索せず([W3] 再掲) | — |
| ソフトウェア(SaaS・エージェント)の売上成長 | 本テーマの範囲外のため収集せず | — |
| 供給が追いつく時期(GPU・電力単独の各社見解) | 欠損(メモリ中心の見解のみ) | 「when will AI compute shortage ease supply catch up demand 2027 2028 GPU memory HBM power ...」(T4-21) |

---

## 9. 出典一覧(URL。すべて検索の要約経由で、原本は未読)

- **[T4-01]** Google の月間トークン(I/O 2026): https://www.shacknews.com/article/149205/google-3-2-quadrillion-monthly-ai-tokens ; https://gigazine.net/gsc_news/en/20260520-google-monthly-tokens-processed/ ; https://blog.google/innovation-and-ai/sundar-pichai-io-2026/ ; https://businessengineer.ai/p/google-io-2026 ; https://techjacksolutions.com/ai-brief/google-reports-32-quadrillion-monthly-tokens-at-io-2026-the/ ; https://liveinthefuture.org/stories/google-190-billion-ai-capex-per-token-per-user-math 1*/3*
- **[T4-02]** 推論と学習の比率: https://www.mckinsey.com/featured-insights/charts/the-future-of-ai-workloads ; https://futurumgroup.com/press-release/inference-climbs-to-71-7-of-ai-platforms-infrastructure-spend-by-2030/ ; https://introl.com/blog/ai-inference-vs-training-infrastructure-economics-diverging-2025 3*/4*
- **[T4-03]** OpenAI の利用者・API: https://www.getpanto.ai/blog/openai-statistics ; https://searchlab.nl/en/statistics/openai-statistics-2026 ; https://quashbugs.com/blog/chatgpt-statistics-users-revenue-downloads-and-usage ; https://technologychecker.io/blog/chatgpt-statistics 4*(アグリゲーター)
- **[T4-04]** Anthropic の年換算売上: https://aiweekly.co/alerts/anthropic-hits-30b-run-rate-leads-cnbc-disruptor-50 ; https://aiweekly.co/alerts/anthropic-projects-first-operating-profit-in-q2-2026 ; https://www.kucoin.com/news/flash/anthropic-s-annualized-revenue-run-rate-surpasses-65-billion-ahead-of-ipo ; https://finance.yahoo.com/news/exclusive-anthropic-aims-nearly-triple-170234463.html ; https://www.getpanto.ai/blog/claude-ai-statistics 3*/4*
- **[T4-05]** Microsoft Foundry の 1T トークン顧客: https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/TranscriptQandAFY26q2 ; https://futurumgroup.com/insights/microsoft-q3-fy-2026-earnings-show-cloud-growth-with-capacity-still-tight/ ; https://tomtunguz.com/281b-from-one-customer/ 1*/3*
- **[T4-06]** 推論モデルの 1 タスク計算量: https://www.bigdatawire.com/2025/03/19/nvidia-preps-for-surge-in-inference-workloads-thanks-to-reasoning-ai-agents ; https://www.janushenderson.com/en-us/offshore/article/nvidia-gtc-2025-what-investors-should-know/ ; https://www.infotech.com/software-reviews/research/review-nvidia-gtc-2025-keynote ; https://www.bankinfosecurity.com/nvidias-huang-deepseek-fuels-explosion-in-ai-compute-needs-a-27610 3*
- **[T4-07]** Oracle の国別・OpenAI 契約(1 回目): https://www.theregister.com/2025/12/15/oracle_denies_openai_delays/ ; https://thearabianpost.com/openai-secures-massive-4-5-gw-cloud-power-from-oracle/ ; https://www.bankinfosecurity.net/oracle-lands-300b-openai-deal-its-day-in-sun-a-29491 3*
- **[T4-08]** ソブリン AI の各国計画: https://www.gpunex.com/blog/sovereign-ai-gpu-investment ; https://scenarica.substack.com/p/the-third-pole ; https://www.douwe.com/projects/the_world_this_wiki/topics/sovereign_ai ; https://www.raisesummit.com/de/post/sovereign-ai-compute-critical-infrastructure 4*
- **[T4-09]** Oracle Q1 FY27: https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/ ; https://quartr.com/events/oracle-corporation-orcl-q1-2027_3gvkOKJp ; https://beancount.io/blog/2026/09/13/oracle-fy2027-q1-earnings-analysis ; https://storagenewsletter.com/2026/09/23/oracle-fiscal-1q27-financial-results 1*/3*
- **[T4-10]** McKinsey「Cost of compute」: https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-cost-of-compute-a-7-trillion-dollar-race-to-scale-data-centers ; https://www.datacenterdynamics.com/en/news/ai-could-drive-67-trillion-investment-in-data-centers-maybe-claims-mckinsey ; https://www.theregister.com/2025/05/01/ai_dc_investment_gamble/ 3*
- **[T4-11]** IEA: https://w.media/data-center-power-demand-will-double-by-2030-iea/ ; https://spglobal.com/energy/en/news-research/latest-news/electric-power/041025-global-data-center-power-demand-to-double-by-2030-on-ai-surge-iea ; https://www.brusselstimes.com/business/1528980/data-centres-will-double-global-electricity-demand-by-2030-iea ; https://www.coradvisors.net/2026/06/ai-data-center-electricity-demand-forecast.html 2*/3*
- **[T4-12]** Morgan Stanley の電力ギャップ: https://cryptobriefing.com/morgan-stanley-ai-data-centers-38-gigawatt-power-gap/ ; https://www.kucoin.com/news/flash/morgan-stanley-reports-38-gigawatt-power-shortfall-for-ai-data-centers-by-2028 ; https://longportapp.cn/news/265596273 ; https://www.itiger.com/news/1130640716 3*/4*
- **[T4-13]** SemiAnalysis: https://www.semianalysis.com/p/datacenter-model ; https://newsletter.semianalysis.com/p/ai-datacenter-energy-dilemma-race ; https://www.theregister.com/2025/09/02/goldman_sachs_ai_datacenters/ 3*
- **[T4-14]** Nvidia FY27 Q2: https://www.storagenewsletter.com/2026/08/27/nvidia-fiscal-2q27-financial-results/ ; https://runtimewire.com/article/nvidia-hits-96-2-billion-revenue-as-data-center-demand-surges-117 ; https://theenergymag.com/news/market-news/nvidia-q2-revenue-hits-96-2-b-as-data-center-surges-117-and-vera-rubin-ramps ; https://www.webull.com/blog/304-Nvidia-Q2-FY2027-Earnings-Beats-Revenue-EPS-Estimates-Guides-Q3-to-108B ; https://eu.36kr.com/en/p/3957380273159302 1*/3*/4*
- **[T4-15]** Microsoft FY26 Q4: https://www.marketbeat.com/instant-alerts/microsoft-q4-earnings-call-highlights-2026-07-29/ ; https://www.nasdaq.com/articles/microsoft-q4-earnings-call-highlights ; https://www.fool.com/earnings/call-transcripts/2026/08/07/microsoft-msft-q4-2026-earnings-call-transcript/ ; https://futurumgroup.com/?p=93329 1*/3*
- **[T4-16]** Alphabet 2026 Q2: https://www.nasdaq.com/articles/alphabet-q2-earnings-call-highlights ; https://thenextweb.com/news/google-is-not-losing-the-ai-race-pichai-tells-doubters-as-cloud-jumps-82 ; https://www.beri.net/article/google-cloud-514b-backlog-enterprise-ai-not-optional ; https://www.beri.net/article/google-cloud-82-percent-growth-enterprise-ai-supply-constraints-2026 ; https://www.webpronews.com/googles-gemini-nears-1-billion-users-as-cloud-revenue-soars-in-q2-beat/ 1*/3*
- **[T4-17]** Anthropic のマルチエージェント: https://www.anthropic.com/engineering/multi-agent-research-system ; https://simonwillison.net/2025/Jun/14/multi-agent-research-system/ 1*/3*
- **[T4-18]** Oracle の国別投資(2 回目): https://www.fierce-network.com/cloud/oracle-plots-3b-european-expansion ; https://telecomreviewamericas.com/articles/cloud-and-enterprise-business/oracle-pledges-usd-8-billion-to-bolster-cloud-and-ai-in-japan ; https://www.oracle.com/a/ocom/docs/cloud/oracle-alloy-your-brand-your-cloud-your-revenue.pdf ; https://futurumgroup.com/insights/oracle-q3-fy-2026-earnings-driven-by-oci-ai-infrastructure-demand/ ; https://btw.media/zh/oracle-uk-sovereign-cloud-ai-control-test ; https://www.barchart.com/story/news/35346870/oracle-just-teamed-up-with-softbank-should-you-buy-sell-or-hold-orcl-stock-now 1*/3*
- **[T4-19]** OpenAI の計算 GW・支出: https://www.techcentral.ie/openai-achieves-record-revenue-thanks-to-tripled-computing-capacity ; https://www.business-standard.com/world-news/openai-expects-600-bn-in-compute-spending-through-2030-ahead-of-ipo-126022100286_1.html ; https://gigazine.net/gsc_news/en/20260410-anthropic-openai-compute-capacity ; https://storyboard18.com/digital/openai-revenue-tops-20-billion-as-computing-capacity-triples-87898.htm ; https://finviz.com/news/317824/openai-tempers-compute-spending-target-to-600-billion-projects-280-billion-revenue-by-2030-as-mega-funding-round-nears-report 3*
- **[T4-20]** AWS 2026 Q2: https://vectorshift.ai/research/companies/amazon-com/earnings/2026-q2 ; https://techstock01.substack.com/p/amazon-2q26-after-google-and-microsoft ; https://tomtunguz.com/aws-answers-the-cloud-race/ ; https://eu.36kr.com/en/p/3919205336903303 1*/3*
- **[T4-21]** 供給が追いつく時期: https://www.thediligencestack.com/p/2027-peak-year-of-constraint ; https://www.aol.com/articles/memory-chip-shortage-end-140002615.html ; https://www.networkworld.com/article/4231781/amd-to-ramp-cpu-gpu-supply-in-2027-as-ai-demand-surges.html ; https://tweaktown.com/news/111454/microns-ceo-says-ai-memory-demand-is-just-in-its-first-innings-and-memory-supply-is-already-insufficient/index.html ; https://www.softwareseni.com/when-will-the-memory-shortage-end-and-what-the-fab-timelines-actually-tell-us/ ; https://noqta.tn/en/blog/ai-compute-crunch-gpu-power-shortage-enterprise-2026 3*/4*
- **[T4-22]** Epoch AI: https://epoch.ai/blog/power-demands-of-frontier-ai-training ; https://epoch.ai/blog/can-ai-scaling-continue-through-2030 ; https://epoch.ai/data/trends ; https://epoch.ai/topics/data-centers 3*
- **[T4-23]** Goldman・BofA の投資額: https://www.pymnts.com/?p=4233514 ; https://seekingalpha.com/news/4501906-us-hyperscalers-capex-to-almost-triple-to-14t-by-2027-goldman-sachs-says ; https://www.roic.ai/news/goldman-sachs-sees-ai-capex-at-12-trillion-by-2027-fueling-debt-financed-buildout-09-25-2026 ; https://fourweekmba.com/ai-goldman-sachs-hyperscaler-capex-trillion-ai-supercycle/ ; https://cryptobriefing.com/goldman-sachs-ai-infrastructure-capex-2027/ ; https://www.itiger.com/news/1153929987 3*/4*
- **[T4-24]** Doubao・OpenRouter: https://technode.com/2026/04/07/doubao-surpasses-120-trillion-daily-tokens-as-usage-doubles-in-three-months/ ; https://axis-intelligence.com/doubao-statistics/ ; https://cryptobriefing.com/openrouter-9000x-token-usage-growth/ ; https://digg.com/tech/2bc6wpy0 ; https://digg.com/tech/mkb3c0uc 3*/4*
- **[T4-25]** Stargate UAE: https://www.datacenterdynamics.com/en/news/companies-behind-uae-stargate-offer-additional-details/ ; https://techcrunch.com/2025/05/22/openai-teams-up-with-cisco-oracle-to-build-uae-data-center ; https://www.mitsloanme.com/article/from-oil-to-ai-uaes-stargate-campus-targets-200-mw-online-by-2026 ; https://www.intelligentcio.com/me/2025/05/23/g42-openai-oracle-nvidia-softbank-cisco-launch-stargate-uae-from-uae-us-ai-campus-in-abu-dhabi/ 3*
- **[T4-26]** OpenAI の年換算売上(extended): https://www.bloomberg.com/news/articles/2026-10-08/openai-s-annualized-revenue-nears-50-billion-ft-says ; https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html ; https://qz.com/openai-revenue-run-rate-70-billion-enterprise-sales-092926 ; https://cryptobriefing.com/openai-revenue-run-rate-nears-50-billion/ ; https://www.gradually.ai/en/openai-statistics/ ; https://www.useluminix.com/reports/company-overviews/openai-financial-fact-sheet-june-2026 3*/4*
- 既存調査の再掲: [W3] /tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research3/W3_industry_structure.md ; [W5] .../research3/W5_oracle_ai_economics.md ; [W8] .../research3/W8_aws_vs_commodity.md

### 検索の一覧(実行順、26 回)

| ID | 検索語(要旨) | mode |
|---|---|---|
| T4-01 | Google monthly tokens processed quadrillion 2026 Gemini | standard |
| T4-02 | inference share of AI compute demand 2025 2030 training vs inference forecast | standard |
| T4-03 | OpenAI weekly active users 2026 API tokens per minute annualized revenue | standard |
| T4-04 | Anthropic annualized revenue run rate 2026 billion Claude Code | standard |
| T4-05 | Microsoft Foundry tokens processed trillion quarter Nadella earnings 2026 token volume | standard |
| T4-06 | reasoning models agentic AI tokens per task multiple vs standard chatbot response 100x compute Nvidia Huang | standard |
| T4-07 | Oracle sovereign AI cloud contracts countries gigawatts Stargate UAE Saudi Japan Germany 2026 | standard |
| T4-08 | sovereign AI investment plans by country gigawatts Saudi Humain UAE Stargate India EU AI gigafactories Nvidia sovereign AI revenue 2026 | standard |
| T4-09 | Oracle Q1 fiscal 2027 RPO remaining performance obligations multicloud sovereign September 2026 | standard |
| T4-10 | McKinsey AI data center capacity demand 2030 GW scenarios compute demand $ trillion 2026 update | standard |
| T4-11 | IEA Energy and AI 2026 data center electricity demand 2030 TWh forecast update | standard |
| T4-12 | Goldman Sachs Morgan Stanley data center power demand gap GW 2028 2030 shortfall forecast 2026 | standard |
| T4-13 | SemiAnalysis AI datacenter critical IT capacity forecast GW 2026 2027 2028 power constraint compute shortage | standard |
| T4-14 | Nvidia Q2 fiscal 2027 results data center revenue guidance sovereign AI Blackwell Rubin visibility $ trillion | standard |
| T4-15 | Microsoft Azure AI run rate capacity constrained through 2027 fiscal Q4 2026 Azure growth Hood | standard |
| T4-16 | Google Cloud Q2 2026 backlog revenue growth capacity constrained Gemini Enterprise Pichai | standard |
| T4-17 | Anthropic multi-agent research system uses 15x more tokens than chat agents 4x; Claude Code tokens per task agentic coding token consumption | standard |
| T4-18 | Oracle sovereign cloud investment billion Japan Germany Netherlands Saudi Arabia UAE Stargate UAE Oracle OCI government regions 2026 announcement | standard |
| T4-19 | OpenAI compute capacity gigawatts 2026 end of year Altman annualized revenue August 2026 CNBC | standard |
| T4-20 | AWS Q2 2026 earnings backlog AI revenue run rate power capacity doubled 2027 Jassy Trainium demand exceeds supply | standard |
| T4-21 | when will AI compute shortage ease supply catch up demand 2027 2028 GPU memory HBM power analysts say shortage lasts | standard |
| T4-22 | Epoch AI inference compute demand growth frontier training compute 4-5x per year AI data center power 2030 projection | standard |
| T4-23 | Goldman Sachs BofA hyperscaler capex forecast 2027 2028 AI infrastructure spending cumulative trillion upgraded estimates 2026 | standard |
| T4-24 | ByteDance Doubao daily tokens trillion 2026 Meta AI monthly users tokens OpenRouter weekly token volume growth | standard |
| T4-25 | Stargate UAE 1 gigawatt 200MW 2026 OpenAI for Countries Norway India UK Korea sovereign data center gigawatts Oracle | standard |
| T4-26 | OpenAI annualized revenue run rate July August September 2026 billion ChatGPT subscribers enterprise Anthropic surpassed | extended |
