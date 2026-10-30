# S1 経営陣の成長シナリオと実行実績(Oracle / NYSE: ORCL)

調査日: 2026-10-11 / 対象: FY2024 〜 Q1 FY2027(2026-08-31 終了、2026-09-10 発表)
役割: 一次情報に基づく事実整理と明らかな食い違いの指摘まで。投資判断(買い/売り)は含まない。

---

## 0. 調査の制約と読み方(最初に必ず読むこと)

1. **ページ本文を直接取得できていない。** WebFetch は DNS エラーまたは 403、curl もプロキシで遮断された。本書の内容はすべて WebSearch が返した検索結果の要約・抜粋に基づく。
2. **検索回数の上限(1ターン200回、他エージェントと共有)に途中で達した。** 追加検索はしていない。そのため 3.(FY2024〜FY2025 の履歴)、5.(役員報酬KPI)、サプライヤ関係(NVIDIA/AMD/Ampere)、「AI Database」「訓練→推論」「資本ライトDC」の経営陣発言は**未調査または未確認**。8章に列挙した。
3. **Tier 表記:**
   - `T1*` = 会社開示(決算プレス/8-K/10-Q/決算説明会トランスクリプト)だが、原典は未取得で検索結果の要約・引用経由。数値・引用は要原典確認。
   - `T3` = 報道・アナリスト(Reuters, Bloomberg, Verdict, Futurum 等)。
   - `T4` = ブログ・AI生成要約・個人発信。
4. 英語発言は「和訳(主)+原文要所」。検索ツールが要約した文言を含むため、**逐語引用でないものは「(要約)」と明記**した。
5. **「算出」と付いた数値は調査者による計算**であり、会社・第三者の主張ではない。計算式を併記した。
6. 出典IDは7章の一覧に対応([S1]〜)。

---

## 1. 骨格と数値目標

### 1-1. FY2030 目標(2025-10-16 Financial Analyst Meeting / Oracle AI World)

| 項目 | 数値 | 定義・補足 | 出典 / Tier |
|---|---|---|---|
| 総売上 FY2030 | **$225B**(5年CAGR 31%) | 事前コンセンサスは $198.4B(LSEG)。FY25 約$57B 基準(31% CAGR からの逆算と整合) | [S10][S11] T3(原典 [S9] 未読) |
| 非GAAP EPS FY2030 | **$21**(CAGR 28%) | "adjusted"/非GAAP。事前コンセンサス $18.92(LSEG) | [S10][S12] T3 |
| OCI売上 FY2030 | **$166B**(2025-09 時点の $144B から引上げ) | 総売上の約74〜75%(算出: 166/225 = 73.8%)。5年CAGR 約75% | [S10][S11][S12] T3 |
| AIインフラの粗利率 | **30〜40%**(Magouyrk: "eventually")。契約期間を通じ概ね安定と説明 | 大型AI案件の例示として「6年・1GW・$60B」のモデルで約35%(コスト構成: 土地・DC・電力・人員 約35%、計算・ネットワーク・ストレージ 約65%) | [S10] T3、[S13] T3(要約) |
| 非AI(従来型クラウドSW/企業向けインフラ)の粗利率 | 65〜80% | 同上 | [S10] T3 |
| 直近の新規コミット | 「前四半期中の30日間で OCI が $65B の新規コミットを獲得、うち Meta $20B」 | Magouyrk 発言(Reuters 要約) | [S10] T3 |
| RPO | 「$500B 超」 | 発表時点 | [S10] T3 |
| FCF(会社の言及ではなくアナリストノート) | FY26〜28 は赤字見込み。RPO の約2/3が OpenAI | 会社数値ではない | [S10]系の要約 T3 |

**2025-09-09(Q1 FY26)に示された OCI 売上ロードマップ**([S8] T1*、[S27] T3):

| FY26 | FY27 | FY28 | FY29 | FY30 |
|---|---|---|---|---|
| $18B(+77%) | $32B | $73B | $114B | $144B → FAM(2025-10)で **$166B** に引上げ |

- FY27〜FY29 の年度別見通しが後の決算で更新されたかは**未確認**(検索で更新値の公式記述は見つからず)。
- 2026-06 の Q4 FY26 で CFO Maxson が「Analyst Day の長期目標(売上CAGR 31%、EPS CAGR 28%)を再確認」([S28] T4 経由の要約)。2026-09(Q1 FY27)での再確認の有無は**未確認**。

### 1-2. 決算ごとのガイダンス・実績の推移

| 四半期(発表日) | 総売上 | OCI(IaaS)売上 | RPO(前期比増) | capex / FCF | ガイダンス・計画の更新 | 出典 |
|---|---|---|---|---|---|---|
| Q1 FY26(2025-09-09) | $14.93B(+11% cc) | $3.3B(+54%) | $455B(+$317B、YoY +359%) | FY26 capex 約$35B に上方(CreditSights が言及) | OCI ロードマップ(上表) | [S8][S27] T1*/T3 |
| Q2 FY26(2025-12-10) | 未確認(報道は「売上ミス」) | 未確認 | $523B(+$68B、YoY +438%) | Q2 capex $12.0B、Q2 FCF -$10B。FY26 capex 見通し 約$50B(従来比 約+$15B) | FY27 売上 +$4B(RPO の売上化が早まるため)。FY26 売上 $67B は据置 | [S7][S30] T1*/T3 |
| Q3 FY26(2026-03-10) | $17.19B(+22% USD / +18% cc)。コンセンサス $16.91B | $4.9B(+84%) | $553B(+$29B、YoY +325%) | 未確認 | FY27 売上 **$90B**(前回比 約+$1B)。EPS $1.79(コンセンサス $1.70)。調達計画(下記)の進捗報告 | [S6][S29] T1*/T3 |
| Q4 FY26(2026-06-10) | $19.18B(+21%)。コンセンサス $19.09B | $5.8B(+93%) | $638B(+$85B、YoY +363%) | **FY26 capex $55.7B**(FY25 $21.2B)、FY26 営業CF $32B(+54%)、FCF **-$23.7B** | FY27: 売上 $90B、非GAAP EPS **$8.05**、**純現金capex 約$70B**(顧客前払い等 $20〜25B を除く)→総額 約$90〜95B、調達 約$40B、**2026暦年中の追加債券発行なし**。FY30 目標を再確認 | [S4][S5][S22][S23] T1*/T3 |
| Q1 FY27(2026-09-10) | $19.3B(+30%) | $7.4B(+121%、cc +120%) | **$664B**(前期比 +$26B、YoY +$209B) | 四半期 capex 約$28〜28.5B、営業CF $23B、FCF 約-$5B(-$5.4B とする報道あり)、純現金capex 約$18B | FY27: 売上 **"at least $90B"**(+34%)、EPS **$8.10**、capex $90〜95B(純現金 $70B 以下)。Q2 ガイド(下記) | [S1][S3][S16][S17][S18] T1*/T3 |

Q1 FY27 の補足(いずれも [S1][S16][S17][S19][S21]):
- 総クラウド売上 $11.6B(+62%)、Cloud Apps(SaaS)$4.2B(+10%)、GAAP EPS $1.56(+55%)、非GAAP EPS $1.92(+30%、コンセンサス $1.74)。非GAAP営業利益率 42%(第三者要約)。
- 四半期中に **$30B 超**の追加AIクラウド契約を獲得。**850MW** のDC容量と **30万基超**のGPUを納入(Q4末以降)。
- 2026-09-10 の発表時点で **$20B の ATM(市場売出し型増資)を完了**(Q3 FY26 時点では未開始)。
- Q2 FY27 ガイダンス: 総売上 +30〜34%、総クラウド +65〜71%(USD。別の要約は cc で 64〜70%)、非GAAP EPS $1.83〜1.91(cc)。
- Maxson: RPO の**約半分が今後36か月で売上化**(要約)[S3]。

### 1-3. シナリオの整合性を見る逆算(算出)

| # | 内容 | 算出 |
|---|---|---|
| a | FY26 総売上は約 $67.4B | Gate.com の見出し「capex が売上の82.6%」[S23]から 55.7 ÷ 0.826。FY26 ガイダンス $67B とほぼ一致。**FY26 実績の公式値は未取得** |
| b | FY27 "at least $90B" を満たすには、Q1(+30%)以外の残り3四半期で**約+35%**が必要 | (90 − 19.3) ÷ (67.4 − 14.93) − 1 = +34.7%。Q1 の +30% および Q2 ガイド +30〜34% より高い |
| c | FY27 → FY30 の必要成長率: 売上 年+35.7%、EPS 年+37.4% | (225/90)^(1/3) − 1、(21/8.10)^(1/3) − 1 |
| d | OCI: 2025-09 ロードマップの FY27 $32B → FY30 $166B は年+73% | (166/32)^(1/3) − 1。FY27 OCI の更新値は未確認 |
| e | FY27 OCI $32B 達成には Q2〜Q4 平均 $8.2B/四半期 | (32 − 7.39) ÷ 3。Q1 は $7.39B |
| f | FY27 EPS の「+18%」は**一時的な投資益を除いた FY26 EPS($6.83)基準** | $8.05 ÷ 6.83 = +17.9%。報告ベース FY26($7.63)比では $8.10 ÷ 7.63 = **+6.1%** |
| g | OCI の売上構成比: Q1 FY27 で 38%(7.39/19.35)。FY30 目標は 74% | ミックスの大変動を前提にした目標 |

### 1-4. RPO の推移と四半期ごとの増加幅(算出含む)

| 期 | RPO | 前期比増 | メモ |
|---|---|---|---|
| Q4 FY25 | 約$138B(455 − 317) | — | 逆算 |
| Q1 FY26 | $455B | +$317B | |
| Q2 FY26 | $523B | +$68B | Meta、NVIDIA ほか新規 |
| Q3 FY26 | $553B | +$29B | 大型AI契約が大半 |
| Q4 FY26 | $638B | +$85B | Q4 の新規AI契約 $67B(Magouyrk、要約) |
| Q1 FY27 | $664B | +$26B | 新規AI契約 $30B 超。売上化による減少を差し引いた純増 |

### 1-5. 経営陣がシナリオを説明する言葉(日付つき)

| # | 日付 | 話者・媒体 | 内容(和訳が主) | 出典 / Tier |
|---|---|---|---|---|
| 1 | 2025-09-09 | Catz(Q1 FY26 決算説明会) | OpenAI、xAI、Meta、NVIDIA、AMD ほかの「AI界の顔ぶれ」と大型クラウド契約を締結("the who's who of AI")(要約) | [S8] T1* |
| 2 | 2025-10-16 | Magouyrk(Analyst Meeting) | AIデータセンター事業(主に NVIDIA GPU のレンタル)は、最終的に**粗利率30〜40%**を生む("will eventually generate a gross profit margin of 30% to 40%")(Reuters 要約) | [S10] T3 |
| 3 | 2025-10-16 | Magouyrk | 前四半期中の30日間で OCI は $65B の新規コミットを獲得、うち Meta $20B(Reuters 要約) | [S10] T3 |
| 4 | 2025-12-10 | 経営陣(Q2 FY26 決算説明会。話者は検索結果から特定できず) | 「FY2027 に **$4B の追加売上**を見込む。FY2026 の売上見通し $67B は不変」("we now expect $4 billion of additional revenue in FY 2027. Our full-year FY 2026 revenue expectation of $67 billion remains unchanged") | [S7] T1* |
| 5 | 2025-12-10 | Sicilia(Q2 FY26) | 業界別アプリが Fusion を牽引する、あるいは Fusion が業界別アプリを牽引する案件が増えている("more and more deals where our industry apps are pulling Fusion or the Fusion apps are pulling the industry apps")(要約) | [検索要約] T1*(原典 URL 未特定) |
| 6 | 2026-06-10 | 決算プレスリリース | Q3・Q4 の RPO 増加の大半は大型AI契約で、顧客が GPU 購入代金を**前払い**するか、顧客が GPU を**購入して Oracle に提供**する形("the customer prepaid Oracle for the purchase of the GPUs, or the customer bought and supplied the GPUs to Oracle")。この前払い・顧客提供ハードの部分は合計 **$75B**("now total $75 billion") | [S4] T1 |
| 7 | 2026-06-10 | Magouyrk(Q4 FY26) | 四半期中に $67B のAIインフラ契約を獲得、大半は BYOH(顧客持込ハード)か前払い。capex 増は部品価格ではなく「主にタイミング」。コストが確定している場合(スペース・電力・人員・部品)は固定価格契約、不確実な場合は避ける(要約) | [S5] T3(T1 の要約) |
| 8 | 2026-09-10 | 決算プレスリリース | ほぼすべての企業顧客は、AIに自社の**プライベートデータ**を推論させたいと考えている("virtually all of Oracle's enterprise customers want to use AI to reason on their private data")。発言者は特定できず、文が途中で切れている | [S1] T1(部分) |
| 9 | 2026-09-10 | Maxson(Q1 FY27) | 粗利率は「想定どおり低下」。要因は DC の立上げと AI インフラ売上の加速。各プロジェクトは立ち上がれば強い FCF 創出を見込む設計(要約) | [S3][S16] T1*/T3 |
| 10 | 2026-09-10 | Q1 FY27 報道 | 契約の構造化(前払い・BYOH)が**資金調達計画に追加の影響を与えない**("no incremental impact on capital raising plans") | [S21] T3 |

**見つからなかった発言(未確認):** 「AI Database」、「訓練から推論へ」、「資本ライトなDC(開発事業者が建物を保有する構図)」を会社がどの表現で説明したかは、今回の検索で逐語を確認できていない。

---

## 2. シナリオを構成するピース

| ピース | 目的 | 現状数値 | 最新動向 | 出典 / Tier |
|---|---|---|---|---|
| **OpenAI(Stargate)** | RPO と OCI 成長の中核。4.5GW の追加容量 | **約$300B / 約5年、2027年開始**は WSJ 報道。OpenAI は 2025-07 に 4.5GW を確認したが**総額は非開示**(DCD)。年間 $30B 超の契約を Oracle が開示(報道)。RPO に占める割合: BofA 推定で**$638B の半分超**(決算前の推定)。FAM 時点のアナリストノートでは約2/3 | **Abilene(TX)**: 1.2GW 全稼働は 2026 Q4 目標(Epoch)、2026-05-20 時点で 42% 納入(二次情報)。**600MW 拡張は 2026-03-06 Bloomberg が「中止」と報道**、Oracle は「誤りで不正確」と否定し 4.5GW は計画どおりと説明。OpenAI の Katti は「さらに拡張も検討したが他の拠点に振り向けた」と発言(Tom's Hardware)。Meta がその拡張候補地のリースを検討との報道。**Shackelford(TX)** 2.0GW 想定、完了目標 2028 Q4。**Saline Township(MI)** 契約電力 1.38GW、3棟、建設中、資金調達は未解決(トラッカー)。**Port Washington(WI)** 2026-03 に初の鉄骨、初期建設。**Doña Ana(NM)** 建設中、容量不明。Lordstown(OH)・Milam County(TX)は**未確認**。経営陣は「OpenAI 以外の RPO は前年比2倍超」と説明(24/7 Wall St の要約) | [S27] T3、[S25] T3、[S26] T3/T4、[S20] T3 |
| **Meta** | 大口AI顧客の分散 | FAM で $20B(Magouyrk 発言、Reuters 要約)。Q2 FY26 の RPO 増加に「Meta、NVIDIA ほかの新規コミット」(プレス) | 期間・総額の詳細は**未確認** | [S10] T3、[S7] T1* |
| **xAI / NVIDIA / AMD / その他** | 顧客基盤の拡大 | 顧客として名指し(Catz、2025-09-09)。金額・期間は**未確認**。Anthropic との契約は**今回の検索で根拠なし** | Q1 FY27 に $30B 超の新規。内訳は**未確認** | [S8] T1*、[S21] T3 |
| **マルチクラウド・データベース**(AWS/Azure/Google 内の Oracle Database@) | OCI 外にDB収益を広げ、データ層を押さえる | マルチクラウドDB売上の成長率: Q1 FY26 +1529%(T4)→ Q3 FY26 +531%(Verdict)→ Q4 FY26 +404%、予約 +325%(AlphaSense 要約)→ Q1 FY27 **+353%、顧客数 +180%**(Quartr、単一出典)。Oracle Cloud Database(IaaS)Q3 FY26 +35%。**稼働リージョン数は未確認** | 成長率は基数効果で逓減。CEO は MSFT/Google/Amazon との提携が需要とリージョン追加を押し上げたと説明(Q3 FY26、Verdict) | [S16] T3、[S17][S32][S19] T3/T4 |
| **AI Database / Autonomous Database / AI Data Platform** | プライベートデータ上でのAI推論を取り込む | 売上・顧客数は**未確認**。Q1 FY27 プレスで「企業顧客のほぼ全員が自社データでAI推論を望む」と説明 | Futurum は Q1 FY27 で「エージェント型データとヘルスケア製品」を収益化の追加経路として言及(詳細なし) | [S1] T1、[S17] T3 |
| **アプリケーション**(Fusion, NetSuite, 業界別, Oracle Health) | 安定収益。AIエージェントで付加価値 | Cloud Apps(SaaS)Q4 FY26 $4.1B(+10%)、Q1 FY27 **$4.2B(+10%)**。Q1 FY26 は $3.8B(+11% USD)、Fusion ERP $1.0B(+17%)。NetSuite、Oracle Health の個別数値は**未確認** | OCI(+121%)と比べ成長は横ばい圏。AIエージェントの具体的な数値は**未確認** | [S1][S5][S8] T1*/T3 |
| **顧客持込 / 前払い(BYOC/BYOH)** | Oracle の現金支出を抑え、GPU調達リスクを顧客に移す | 前払い・顧客提供ハード部分 **$75B**(プレス)。Q4 FY26 の新規 $67B の大半(要約)。Q1 FY27 10-Q: 重要な金融要素を含む顧客前払い **$11.4B** | 純現金capex($70B 以下)を新規開示し、総額 $90〜95B と区別。Q1 FY27 は「調達計画への追加影響なし」と説明 | [S4][S2][S5][S21] T1*/T3 |
| **サプライヤ(NVIDIA, AMD)/ Ampere 売却** | GPU 確保、自社チップ事業の整理 | NVIDIA・AMD は**顧客として**言及。サプライヤ条件・Ampere 売却の詳細は**今回未調査** | FY26 の非GAAP EPS $7.63 に「一時的な投資益」が含まれ、除くと $6.83(Nasdaq 要約)。**投資益の中身(Ampere 売却益か否か)は未確認** | [S5] T3 |
| **資金調達** | capex を賄う(下表) | FY26: 債券 $43B + 株式 $5B。FY27 計画 約$40B(うち $20B ATM は Q1 FY27 に完了)。2026暦年は追加債なし | 2026-02 に最大 $45〜50B の調達計画を公表、数日で $30B(投資適格債 + 強制転換優先株)。S&P は BBB- に格下げ(時期は未確認)。Q1 FY27 の Oracle リース未開始コミットは CreditSights が $248B と報じた(見出しのみ) | [S6][S24][S22][S36] T1*/T3 |
| **AIレンタルの粗利率報道** | シナリオの収益性の検証点 | The Information(2025-10): NVIDIA チップのレンタルで、8月までの3か月に売上約$9億、粗利約$1.25億(約14%)。5四半期平均で約16%、一部は損失(Blackwell で約$1億の損失との報道)。全社粗利は約70% | 会社は当初コメントせず(Reuters)。2025-10-16 に 30〜40%(契約期間を通じ概ね安定)と説明。Q1 FY27 の全社粗利率は 60.03% と第三者が算出(8四半期で最低)。Morgan Stanley は GPUaaS の粗利率の改善傾向を指摘 | [S14] T3、[S13] T3、[S15] T4、[S33] T4 |
| **供給・稼働** | 容量とGPUの稼働率で「需要が供給を上回る」を裏付け | Q1 FY27: 850MW、30万基超のGPU納入。Q4 FY26: GPU 稼働率 97.5%。更新時期の 35,000 GPU(59顧客)のうち、**49%の顧客が92%のGPUを更新** | 更新価格は上昇傾向と経営陣が説明(要約) | [S5][S21] T3 |

### 2-1. 資金調達の時系列(会社の説明に基づく部分と推計を分離)

| 時期 | 内容 | 出典 / Tier |
|---|---|---|
| 2025-09(推計) | 債券 $18B(FY26 債券 $43B から 2026-02 の $25B を引いた逆算。**一次確認なし**) | 算出 |
| 2026-02 | 暦年2026に最大 **$45〜50B** の調達計画。数日で **$30B** を調達(投資適格債 + 強制転換優先株)、応募超過 | [S6][S24] T1*/T3 |
| 2026-03-10(Q3) | ATM($20B)は未開始。2026暦年は追加の債券発行なしと説明 | [S6] T1* |
| 2026-06-10(Q4) | FY26: 債券 $43B + 株式 $5B。FY27: **約$40B**(債券と株式、うち $20B ATM)。2026暦年は追加債なし | [S22] T3 |
| 2026-09-10(Q1) | **$20B ATM 完了**(株数・平均価格は**未確認**) | [S1][S3] T1*/T3 |
| 参考 | FY27 の残り約 $20B(2027年前半の債券か株式か)の内訳は**未確認** | — |

---

## 3. 実行実績(L9: 経営と組織)

### 3-1. ガイダンス対実績

| 項目 | 約束(時点) | 実績 | 判定 | 出典 / Tier |
|---|---|---|---|---|
| FY26 capex | 約$25B(2025-06、**今回の検索で根拠なし。参考のみ**)→約$35B(2025-09)→約$50B(2025-12) | **$55.7B**(FY25 は $21.2B) | **超過**。最新見通し比 +11%、2025-09 比 +59%、FY25 比 2.6倍(算出) | [S23][S7] T1*/T3 |
| FY26 売上 | $67B(2025-12 時点で据置と発言) | 約$67.4B(逆算。公式値未取得) | **ほぼ達成**(要確認) | [S7][S23] |
| FY26 OCI 売上 | $18B(+77%、2025-09) | Q1 $3.3B + Q3 $4.9B + Q4 $5.8B = $14.0B。Q2 は**未確認**(Q2 が約$4.1B なら $18.1B になる計算だが、Q2 値は本調査で未取得) | **未確認** | [S8] |
| FY27 売上 | 約$85B(逆算: 2025-12 の +$4B 前)→$89B(2025-12)→$90B(2026-03)→$90B 維持(2026-06)→"at least $90B"(2026-09) | 進行中 | **一貫して上方または維持**。Q4 FY26 の表現が「維持」か「引上げ」かは要約間で食い違い | [S7][S29][S16] |
| FY27 EPS | $8.05(2026-06)→$8.10(2026-09) | 進行中 | **小幅引上げ** | [S16] |
| FY27 capex | 純約$70B + 前払い $20〜25B = 総額 $90〜95B(2026-06)→ 維持(2026-09) | Q1 $28〜28.5B(総額)。アナリスト予想は約$67.7B(Reuters 系要約) | **事前予想を超過**。維持 | [S22][S18] |
| Q1 FY27 | 売上 +27〜29%、総クラウド +58〜64%、EPS $1.72〜1.76(2026-06) | 売上 +30%、総クラウド +62%、EPS **$1.92** | 売上・EPS は**上振れ**、クラウドはレンジ内。EPS の上振れ要因は**未確認**(税・一時益の可能性を要確認) | [S4][S16] |
| Q4 FY26 | — | EPS $2.11(予想 $1.89〜1.96)、売上 $19.18B(予想 $19.09B)、RPO $638B(予想 $601B) | 上振れ。ただし株価は -8〜-11% | [S22][S28] |
| Q3 FY26 | — | EPS $1.79(予想 $1.70)、売上 $17.19B(予想 $16.91B) | 上振れ | [S29] |
| Q2 FY26 | — | 売上は予想未達と報道、capex $12.0B、FCF -$10B | **売上ミス**(数値は未取得) | [S30] |
| Q1 FY26 | — | EPS $1.47(予想比 -$0.01)、売上 $14.93B | 小幅未達 | [S8] 系要約 T4 |
| FY30 目標 | 売上 $225B、EPS $21、OCI $166B(2025-10) | 2026-06 に再確認 | 検証は先 | [S28] T4 |
| FCF の黒字化時期 | 未提示。Q1 FY27 でも時期を示さず | FY26 -$23.7B、Q1 FY27 約-$5B | **約束なし** | [S3][S33] |
| FY24〜FY25 の期初・四半期ガイダンスと実績 | — | **未調査**(検索上限)。参考: Q1 FY25 売上 $13.3B(+8%)、RPO $99B(+52%)(MarketBeat、T4) | **未確認** | [S34] |

### 3-2. 言行一致リスト

| # | 言ったこと | 結果 | 評価 |
|---|---|---|---|
| 1 | OCI 成長率が加速する | 前年比: Q1 FY26 +54% → Q3 +84% → Q4 +93% → Q1 FY27 +121%(Q2 FY26 は未確認) | **言行一致**(加速は実現) |
| 2 | 「需要が供給を上回る」 | Q4 FY26 GPU 稼働率 97.5%、更新率 92%(GPU基準)。RPO は 4四半期で $455B → $664B | **整合**。ただし四半期純増は +$317B → +$68B → +$29B → +$85B → +$26B と不安定 |
| 3 | FY26 capex は抑えめ(期初約$25B。要確認) | 最終 $55.7B | **不一致**(ただし資金は前払いで補填する構造と説明) |
| 4 | AIインフラ粗利率 30〜40% | AI単体の粗利率は未開示。全社粗利率は低下(60.03%、第三者)。経営陣は「想定どおり」と説明 | **検証不能**。報道の 14〜16% との差が説明できるかが論点 |
| 5 | 2026暦年に追加債券を出さない | 2026-06 発言。2026暦年が終わるまで検証できない | **未検証**(ATM で $20B 株式は実行済み) |
| 6 | Abilene 拡張は「報道は誤り」 | OpenAI 側は「拡張を検討したが他拠点に振り向けた」と発言 | **食い違いの疑い**(Oracle は 4.5GW 契約は維持と説明) |
| 7 | 契約の前払い・BYOH で自社資金負担を軽減 | 純現金capex 約$70B、総額 $90〜95B。FCF は赤字継続 | **部分的に整合**。FCF 黒字化の時期は未提示 |
| 8 | FY27 売上 $90B | 段階的に上方・維持。Q1 は +30%、通年必要は残り3Q で約+35%(算出) | **進行中**。加速が前提 |

### 3-3. 数字・記述の食い違い(出典間)

| # | 食い違い | 内容 | 扱い |
|---|---|---|---|
| 1 | Q2 FY27 総クラウド成長率 | cc で 64〜70% と USD で 65〜71% の2種類の記載 | 通貨基準の違いの可能性。プレスで確認 |
| 2 | Q1 FY27 capex | $28.0B と $28.5B。純現金capex $17.96B と $18B | 丸めまたは定義差。10-Q で確認 |
| 3 | $67B と $75B | $67B は Q4 に新規獲得した AI インフラ契約(大半が BYOH/前払い)。$75B は前払い・顧客提供ハード部分の**累計** | 別概念。両方とも二次要約 |
| 4 | Q4 FY26 の FY27 売上 | 「$90B を維持」(Verdict)と「$90B に引上げ」(別の要約) | Q3 時点で既に $90B のため「維持」が妥当とみられるが、プレスで確認 |
| 5 | Q1 FY27 の FY27 売上 | 数値は $90B で不変、表現が "at least"。複数媒体は「上方修正」と表現 | 実質は据置、EPS のみ $8.05 → $8.10 |
| 6 | The Information の数値 | 売上約$9億・粗利約$1.25億(約14%)と、5四半期平均約16% | 期間が異なる。両方報道 |
| 7 | OpenAI 比率 | BofA「半分超」(決算前推定)と、経営陣「OpenAI 以外が前年比2倍超」 | 両立しうる。割合の会社開示は未確認 |
| 8 | FY26 EPS | $7.63(一時的な投資益込み)と $6.83(除外) | FY27 の +18% は後者基準。報告ベース比は +6% |
| 9 | Abilene 拡張 | Bloomberg「中止」、Oracle「誤り」、OpenAI「他拠点へ」 | 未解決 |

---

## 4. 開示の変化

| 区分 | 内容 | 時期 | 出典 / Tier |
|---|---|---|---|
| 新規に開示 | OCI 年度別売上ロードマップ(FY26〜FY30) | 2025-09 | [S8] T1* |
| 新規に開示 | AIインフラの粗利率レンジ(30〜40%)とそれ以外(65〜80%) | 2025-10 | [S10] T3 |
| 新規に開示 | 「前払い・顧客提供ハード」部分の RPO 内訳($75B) | 2026-06 | [S4] T1 |
| 新規に開示 | **純現金capex**(顧客前払い等を除く)と総額の区別 | 2026-06 | [S22] T3 |
| 新規に開示 | 四半期の新規AI契約額($67B、$30B 超) | 2026-06 / 09 | [S5][S1] |
| 新規に開示 | 納入容量(850MW)、納入GPU(30万基超)、GPU稼働率 97.5%、更新率 | 2026-06 / 09 | [S5][S21] |
| 新規に開示 | RPO の売上化時期(12か月内 約33%、36か月内 約半分) | 2026-03 / 09 | [S3] T1*、ブログ T4 |
| 新規に開示 | マルチクラウドDBの売上・予約・顧客数の成長率、AIインフラ売上成長率(Q3 FY26 +243%) | 2026-03 以降 | [S16][S19] |
| 新規に開示 | 10-Q: 重要な金融要素を含む顧客前払い $11.4B | 2026-09 | [S2] T1* |
| 非GAAP EPS の一時益の開示 | FY26 EPS $7.63 は一時的な投資益込み、除くと $6.83 | 2026-06 | [S5] T3 |
| 開示をやめた KPI | **未確認** | — | — |
| セグメント区分の変更 | **未確認**(「Cloud Infra (IaaS)」「Cloud Apps (SaaS)」の表記は継続) | — | [S1] |
| 経営体制 | 共同CEO(Magouyrk、Sicilia)+ CFO Hilary Maxson。FAM(2025-10)の財務説明は Doug Kehring。**CFO 交代の日付は未確認**。diginomica は Q4 FY26 決算を「Ellison 不在の新トライアンビレート」と表現(見出しのみ) | 2025-10 → 2026-06 | [S9][S35] |

---

## 5. 役員報酬の業績KPI(proxy statement)

**未確認。** 今回の検索では FY2026 の proxy statement(DEF 14A)の報酬体系(総額指標か1株当たり指標か、PSU/PSO の業績条件、共同CEOの報酬)に到達できなかった。次回調査で DEF 14A の Compensation Discussion and Analysis を直接確認する必要がある。

---

## 6. 経営陣による「意図」の説明(借入・株式・リース・顧客集中)

| テーマ | 日付 | 話者 | 説明(和訳が主) | 出典 / Tier |
|---|---|---|---|---|
| 借入・株式 | 2026-02 | 会社発表 | 暦年2026に最大 $50B を債券と株式で調達。数日で $30B(投資適格債 + 強制転換優先株)。ATM は未開始 | [S6][S24] T1*/T3 |
| 借入 | 2026-06-10 | CFO Maxson | FY27 に約 $40B を債券と株式で調達(うち $20B ATM)。**2026暦年は追加の債券を発行しない**(要約) | [S22] T3 |
| 資金負担の転嫁 | 2026-06-10 | プレス | 大型AI契約では、顧客が GPU を前払いするか、自ら購入して提供する。前払い・顧客提供の部分は $75B | [S4] T1 |
| 資金負担の転嫁 | 2026-09-10 | 報道 | これらの契約構造は、資金調達計画に追加の影響を与えない | [S21] T3 |
| capex の増額理由 | 2026-06-10 | Magouyrk | 増加は部品価格ではなく「主にタイミング」。固定価格契約はコストが確定している場合に限る | [S5] T3 |
| 収益性 | 2026-09-10 | Maxson | 粗利率の低下は想定どおり。DC の立上げと AI インフラ売上の加速が要因。各プロジェクトは立ち上がれば強い FCF を生む設計 | [S3][S16] T1*/T3 |
| 粗利率 | 2025-10-16 | Magouyrk | AIインフラは最終的に 30〜40%、契約期間を通じ概ね安定 | [S10] T3 |
| 顧客集中 | 2026-09-10 | 経営陣(要約) | OpenAI 以外の RPO は前年比2倍超。新規 $30B 超は OpenAI 以外を含む | [S20] T3 |
| 需要の根拠 | 2026-09-10 | プレス | 企業顧客のほぼ全員が、AIに自社のプライベートデータを推論させたい | [S1] T1 |
| **リース** | — | — | **経営陣自身の説明は今回の検索で確認できず**。CreditSights は 10-Q の未開始リース・コミットを $248B と報じた(見出しのみ)。純リース調整後レバレッジは FY28 に 3.7倍と予測(CreditSights、第三者) | [S36] T3 |

注: 上表の「意図」は会社の説明を要約したもの。**何を取りに行くための借入か**(例: OpenAI 向け容量の確保、相場上昇前のGPU確保、AI Database 市場の獲得)について、経営陣が逐語で語った文言は今回確認できていない。

---

## 7. 出典一覧

| ID | 媒体 / 内容 | URL | 日付 | Tier |
|---|---|---|---|---|
| S1 | Oracle Q1 FY27 決算プレス | https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/(複製: https://seekingalpha.com/pr/20647809 、https://www.placera.se/pressmeddelanden/oracle-announces-q1-results-driven-by-triple-digit-growth-in-cloud-infrastructure-revenues-20260910) | 2026-09-10 | T1* |
| S2 | Oracle Q1 FY27 10-Q | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm | 2026-09 | T1*(未読) |
| S3 | Q1 FY27 決算説明会トランスクリプト(Motley Fool 他) | https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/ | 2026-09-10/11 | T1* |
| S4 | Oracle Q4 FY26 決算プレス / 8-K Ex.99.1 | https://www.oracle.com/news/announcement/q4fy26-earnings-release-2026-06-10/ 、https://www.sec.gov/Archives/edgar/data/0001341439/000119312526265848/orcl-ex99_1.htm | 2026-06-10 | T1* |
| S5 | Nasdaq「Oracle Q4 earnings call highlights」 | https://www.nasdaq.com/articles/oracle-q4-earnings-call-highlights | 2026-06 | T3 |
| S6 | Oracle Q3 FY26 決算プレス / 8-K Ex.99.1 | https://www.oracle.com/news/announcement/q3fy26-earnings-release-2026-03-10/ 、https://www.sec.gov/Archives/edgar/data/1341439/000119312526100148/orcl-ex99_1.htm | 2026-03-10 | T1* |
| S7 | Q2 FY26 決算説明会トランスクリプト | https://www.fool.com/earnings/call-transcripts/2025/12/10/oracle-orcl-q2-2026-earnings-call-transcript/ 、https://www.marketbeat.com/earnings/reports/2025-12-10-oracle-co-stock/ | 2025-12-10 | T1* |
| S8 | Oracle Q1 FY26 決算プレス / トランスクリプト | https://www.oracle.com/ua/news/announcement/q1fy26-earnings-release-2025-09-09/ 、https://www.marketbeat.com/earnings/reports/2025-9-9-oracle-co-stock | 2025-09-09 | T1* |
| S9 | Oracle Financial Analyst Meeting 2025 | https://www.oracle.com/events/financial-analyst-meeting-2025/ 、https://www.oracle.com/a/ocom/docs/corporate/financial-analyst-meeting-2025-kehring.pdf | 2025-10-16 | T1(未読) |
| S10 | Reuters(TradingView 経由)「Oracle expects cloud sales of $166 billion by 2030」 | https://de.tradingview.com/news/reuters.com%2C2025%3Anewsml_L6N3VX11P%3A0-oracle-expects-cloud-sales-of-166-billion-by-2030-as-business-expands | 2025-10-16 | T3 |
| S11 | Yahoo Finance「Oracle stock jumps 4% ...」 | https://finance.yahoo.com/news/oracle-stock-jumps-4-as-company-says-cloud-revenue-will-skyrocket-to-166b-by-2030-182501729.html | 2025-10-16 | T3 |
| S12 | Morningstar / CreditSights(Analyst Meeting) | https://www.morningstar.com/stocks/oracle-earnings-skyrocketing-ai-data-center-demand-fuels-outlook 、https://know.creditsights.com/insights/oracle-top-10-takeaways-from-2025-analyst-meeting/ | 2025-10 | T3(CreditSights は有料、プレビューのみ) |
| S13 | Sherwood News「Oracle jumps as it says AI cloud gross margins can reach 35%」 | https://www.sherwood.news/markets/oracle-jumps-as-it-says-ai-cloud-gross-margins-can-reach-35-predicts-usd166/ | 2025-10 | T3 |
| S14 | The Information 報道の二次報道(Reuters、Seeking Alpha、Sherwood) | https://il.tradingview.com/news/reuters.com%2C2025%3Anewsml_L3N3VO0YP%3A0-oracle-falls-on-report-of-razor-thin-gross-profit-margins-in-cloud-business 、https://seekingalpha.com/news/4502414-oracles-documents-show-financial-challenges-of-renting-out-nvidias-chips 、https://sherwood.news/markets/oracle-tumbles-after-report-that-its-lost-nearly-usd100-million-from-renting 、原典(有料・題名のみ): https://feature.theinformation.com/articles/oracle-assures-investors-ai-cloud-margins-struggles-profit-older-nvidia-chips | 2025-10 | T3 |
| S15 | TIKR「Bad Timing: Oracle Locked in Fixed Margin Cloud Deals ...」 | https://www.tikr.com/blog/bad-timing-oracle-locked-in-fixed-margin-cloud-deals-just-before-gpu-prices-soared-heres-how-things-could-get-ugly | 2026 | T4 |
| S16 | Verdict(Q3 FY26、Q4 FY26、Q1 FY27) | https://www.verdict.co.uk/oracle-q3-fy26-results/ 、https://www.verdict.co.uk/oracle-q4-fy26-net-income-increases-23-to-4-2bn/ 、https://www.verdict.co.uk/oracle-q1-fy27-results/ | 2026-03 / 06 / 09 | T3 |
| S17 | Futurum(Q1 FY27、Q4 FY26) | https://futurumgroup.com/insights/oracle-q1-fy-2027-ai-infrastructure-contracts-convert-into-growth/ 、https://futurumgroup.com/insights/oracle-q4-fy-2026-ai-workloads-accelerate-cloud-and-database-growth/ | 2026-09-14 / 06 | T3 |
| S18 | Constellation Research「Oracle Q1 strong and so is capital expenditures」 | https://www.constellationr.com/insights/news/oracle-q1-strong-and-so-capital-expenditures | 2026-09 | T3 |
| S19 | Quartr Q1 FY27 要約 | https://quartr.com/events/oracle-corporation-orcl-q1-2027_3gvkOKJp | 2026-09-13 | T4(AI要約) |
| S20 | 24/7 Wall St | https://247wallst.com/investing/2026/09/11/oracle-weakens-bear-case-with-broader-ai-customer-base-and-664-billion-backlog/ | 2026-09-11 | T3 |
| S21 | Crypto Briefing | https://cryptobriefing.com/oracle-30b-ai-cloud-contracts-q1/ | 2026-09 | T3 |
| S22 | Stocktwits / Outlook Business(Q4 FY26 の capex・調達) | https://stocktwits.com/news-articles/markets/equity/oracle-backlog-swells-above-google-microsoft-ceo-defends-95-b-capex-fresh-debt-raise-as-stock-tumbles/cZKTLhRR7cM 、https://www.outlookbusiness.com/corporate/oracle-forecasts-95-bn-in-capex-for-fy27-plans-to-raise-40-bn-in-debt-and-equity | 2026-06-11 | T3 |
| S23 | TNW / Gate.com / Morningstar(FY26 capex $55.7B) | https://thenextweb.com/news/oracle-q4-fy2026-capex-55-billion-ai-data-center-openai 、https://www.gate.com/news/detail/oracle-reports-557b-capex-consuming-826-of-revenue-in-fiscal-2026-23140237 、https://www.morningstar.com/stocks/oracle-earnings-hefty-capital-expenditure-is-burden-rapid-growth | 2026-06 | T3/T4 |
| S24 | The Next Platform「Oracle's financing primes the OpenAI pump」 | https://www.nextplatform.com/compute/2026/02/03/oracles-financing-primes-the-openai-pump/4092157 | 2026-02-03 | T3 |
| S25 | Bloomberg / Tom's Hardware(Abilene 拡張) | https://bloomberg.com/news/articles/2026-03-06/oracle-and-openai-end-plans-to-expand-flagship-data-center 、https://www.tomshardware.com/tech-industry/oracle-and-openai-scrap-planned-600mw-abilene-expansion 、https://www.tomshardware.com/tech-industry/oracle-rebuts-incorrect-reporting-on-stargate-expansion | 2026-03-06 | T3 |
| S26 | Epoch AI / Stargate トラッカー | https://epoch.ai/publications/openai-stargate-where-the-us-sites-stand 、https://stargate.how/location | 2026(トラッカーは 2026-09-18 時点) | T3/T4 |
| S27 | DatacenterDynamics(OpenAI $300B 報道、RPO $455B) | https://www.datacenterdynamics.com/en/news/openai-signs-300bn-cloud-deal-with-oracle-report/ 、https://www.datacenterdynamics.com/en/news/oracle-has-455bn-in-remaining-performance-obligations-at-end-of-q1-2026/ | 2025-09 | T3 |
| S28 | TIKR(Q4 FY26) | https://www.tikr.com/blog/oracle-stock-q4-2026-beats-estimates-as-oci-revenue-surges-93-year-over-year | 2026-06 | T4 |
| S29 | erp.today / Yahoo-Reuters(Q3 FY26) | https://erp.today/oracle-beats-estimates-as-ai-cloud-demand-surges-lifts-2027-revenue-outlook-to-90b/ 、https://finance.yahoo.com/news/oracle-beats-quarterly-revenue-estimates-200839907.html | 2026-03 | T3 |
| S30 | SiliconANGLE(Q2 FY26) | https://siliconangle.com/2025/12/10/shares-oracle-slide-10-revenue-miss-rising-capital-expenditures/ | 2025-12-10 | T3 |
| S31 | Invezz「記録的な backlog なのになぜ株価は50%下落」 | https://invezz.com/in/news/2026/07/08/oracles-record-backlog-is-booming-so-why-is-the-stock-down-50percent/ | 2026-07-08 | T3 |
| S32 | AlphaSense Q4 要約(マルチクラウド +404%) | https://www.alpha-sense.com/earnings/orcl | 2026-06 | T4(Futurum 検索結果経由) |
| S33 | SaaS Intelligence ほか(FCF・粗利率の第三者分析) | https://saasintelligence.substack.com/p/oracles-ai-boom-runs-on-negative | 2026-09 | T4 |
| S34 | MarketBeat Q1 FY25 | https://www.marketbeat.com/earnings/reports/2024-9-9-oracle-co-stock | 2024-09-09 | T4 |
| S35 | diginomica「Ellison in absentia ...」 | https://diginomica.com/ellison-absentia-oracles-new-triumvirate-releases-strong-full-year-numbers-apps-and-infrastructure | 2026-06 | T3(見出しのみ) |
| S36 | CreditSights(10-Q、FAQ) | https://know.creditsights.com/insights/oracle-10q-cut-248-bn-lease-commits/ 、https://know.creditsights.com/insights/oracle-top-20-client-faqs/ | 2025-12 〜 2026 | T3(有料、プレビューのみ) |

---

## 8. 未確認事項(次回調査の優先順)

1. **一次文書の直接確認**: Q1 FY27 プレスと 10-Q、Q4 FY26 の 8-K Ex.99.1、FAM 2025 のスライド(S9)。本書の数値はいずれも検索要約経由。
2. **FY2024〜FY2025 の期初・四半期ガイダンスと実績**(RPO、OCI成長率、総売上成長率、capex)。FY26 期初の capex ガイダンス(約$25B)の根拠。
3. **FY26 の確定値**: 総売上、OCI 売上、Q2 FY26 の売上と OCI 売上。
4. **FY27 以降の OCI 年度別見通し**(FY27 $32B、FY28 $73B、FY29 $114B の更新有無)、FCF 黒字化の時期、FY30 目標が Q1 FY27 で再確認されたか。
5. **役員報酬の業績KPI**(FY2026 DEF 14A)。総額指標か1株当たり指標か。共同CEOの報酬条件。
6. **経営陣の逐語**: 「AI Database」、「訓練から推論へ」、「資本ライトなデータセンター」、BYOH の目的。**リース**(未開始コミット $248B)に関する経営陣の説明。
7. **サプライヤ関係**: NVIDIA・AMD の調達契約、Ampere 売却の条件と会計処理、FY26 EPS の「一時的な投資益」の中身。
8. **顧客契約**: Meta の期間・総額、xAI・NVIDIA・AMD の金額、Anthropic の有無、OpenAI の RPO 比率の会社開示、Lordstown(OH)・Milam County(TX)の状況。
9. **マルチクラウド**: 稼働リージョン数、AWS/Azure/Google 別の成長率、Q1 FY27 の +353%・顧客 +180%(単一出典)の裏取り。
10. **アプリ**: NetSuite、Oracle Health(Cerner)、AIエージェントの数値。
11. **開示の変化**: 廃止した KPI、セグメント区分の変更の有無。CFO 交代(Kehring → Maxson)の日付。
12. **財務リスクの会社説明**: S&P 格下げ(BBB-)の時期、ATM の平均価格と発行株数、FY27 残り約$20B の調達手段。
13. **食い違いの決着**: 3-3 の #1〜#9。特に Q4 FY26 の FY27 売上の表現、Abilene 拡張の事実関係、Q1 FY27 の EPS 上振れ要因。
