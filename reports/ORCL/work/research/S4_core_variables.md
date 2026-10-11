# S4 芯(価値を最も動かす変数)の追加事実: Oracle (NYSE: ORCL)

調査日: 2026-10-11 / 担当: 株式調査アシスタント(事実・数値・出典の整理と食い違いの指摘のみ。投資判断は含まない)
前提: S1(経営陣シナリオ)・S3(スカットルバット)を先読み済み。重複は避け、S1/S3 の「未確認」を埋めることを優先した。

---

## 0. 読み方(必ず先に読むこと)

1. **取得手段は WebSearch の要約のみ(45回使用、上限到達)。** WebFetch は使っていない。SEC 提出書類・決算説明会トランスクリプトの本文は1件も直接読めていない。数値・引用はすべて「検索要約に書かれていた内容」。
2. **Tier 表記:** 1=会社開示、2=規制当局・格付会社、3=報道・アナリスト、4=ブログ・AI生成要約等。
   `T1*` = 会社の一次書類(プレス/10-K/10-Q/DEF 14A/決算説明会)だが、今回は検索要約経由でしか見ていないもの。**要原典確認。**
3. **「算出」と付いた数値は調査者の計算**(計算式を併記)。会社・第三者の主張ではない。
4. 英語の発言は和訳主体。逐語確認できたものは原文を括弧で最小限添えた。確認できないものは「(要約)」と明記。
5. 出典IDは本書末尾の出典一覧に対応([A1] など)。S1/S3 の ID は「S1:」「S3:」と接頭して区別する。
6. **S1 の未確認事項のうち、本書で解消したもの:** FY26 非GAAP EPS $7.63 の一時益の中身(Ampere 売却益 + Bloom ワラント益、金額・四半期。5章)、FY26 総売上 $67.4B(7章の DEF 14A 経由)、Q2 FY26 の売上・OCI 売上(8章)、共同CEOの報酬 KPI(7章)、CFO Maxson の就任時期(2026年4月と報道。7章)。

---

## 1. GPU の更新(再契約)データ

### 1-1. 事実表

| 項目 | 内容 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| Q4 FY26 の更新実績(文言) | 「Q4 に更新時期を迎えたのは 59 顧客・3.5 万 GPU。**顧客の 49% が、GPU の 92% を更新した**」("In Q4, 35,000 GPUs from 59 separate customers were up for renewal. 49% of those customers renewed for 92% of those GPUs.")。話者は Magouyrk と報じられた。**逐語は二次報道の引用であり、公式トランスクリプトでは未照合** | 2026-06-10 | [A1][A2] | 3(原典 T1*) |
| 更新されなかった GPU | 「更新されなかった GPU の大半は、同四半期中に他の顧客へ再販された」(ポッドキャスト要約)。Dolphin Research は「残り 8% が同四半期に再販」と要約 | 2026-06 | [A4][A3] | 4 |
| 更新単価(Q4) | **Q4 の説明会に関する検索結果には、初回比の単価変化(%)・契約期間・GPU 世代の記述が見つからなかった**(3回検索) | — | — | — |
| Q1 FY27 の続報(文言) | 「Q1 に更新時期を迎えた GPU の全量が、**従来契約比 20% のプレミアム**で更新または再販された。それらの GPU の過半は 4 年以上前のもの」("Of all the GPUs that came up for renewal in Q1, that capacity was renewed or resold at a 20% premium to prior contracts. The majority of those GPUs are 4 years or older.") | 2026-09-10 | [A7][A8](Constellation Research と Longbridge が同一文を引用)、Zacks [A10] | 3(原典 T1*) |
| Q1 FY27 の数量 | 更新対象の GPU 数・顧客数・更新率は**開示が見つからない**(Q4 のような 35,000/59 の形では報じられていない) | — | — | — |
| 稼働率 | GPU 稼働率: Q4 FY26 97.5%(S1)、**Q1 FY27 97.9%** | 2026-06 / 09 | [A7][A9] | 3 |
| 納入量(Q1 FY27) | 四半期中に 30 万基超の GPU と 850MW を納入(「Q4 全体の約3倍」)。参考: Q4 時点の説明では、FY26 通年の納入が 1.2GW 超、Q1 FY27 の納入は約 1GW に近づく見込みとされていた(1社の要約)。実績 850MW は当時の見込み(約 1GW)をやや下回る(算出: 850MW < 約 1,000MW。ただし「約」の幅は不明) | 2026-06 / 09 | [A9][A7][B7] | 3 |
| 市場価格との並置 | H100 ネオクラウド指数 $2.00(2025-12)→ $2.75〜2.80(2026-07/08)= 約 +38〜40%(算出)。SemiAnalysis の H100 1年契約指数 +約40%(2025-10 → 2026-03)。**Oracle の +20%(契約比)と指数の上昇率は基準が異なり、直接比較できない** | 2026 | S3 の 1-1・1-2 | 3 |

### 1-2. 算出(Oracle のサンプルの大きさ)

| # | 内容 | 算出 |
|---|---|---|
| a | Q4 に更新された GPU は約 32,200 基、更新した顧客は約 29 社 | 35,000 × 0.92 = 32,200、59 × 0.49 = 28.9 |
| b | 1顧客あたりの更新対象は平均約 590 基(小口の顧客が中心) | 35,000 ÷ 59 = 593 |
| c | Q4 の更新対象 3.5 万基は、Q1 FY27 の1四半期の納入量(30 万基超)の約 12%。異なる四半期の比較なので目安 | 35,000 ÷ 300,000 = 11.7% |
| d | Q1 FY27 時点で「4 年以上前」の GPU は 2022-09 以前の調達分。A100(2020〜)と初期 H100 が該当しうる(**世代は会社が明示していない。推定**) | 2026-09 − 4年 |

### 1-3. 事実要約

- 会社が定量開示した更新データは2点のみ。Q4: 顧客 49%・GPU 92% が更新(単価・期間・世代は開示なし)。Q1 FY27: 全量が更新または再販され、従来契約比 +20%(対象の過半は 4 年以上前の GPU)。
- 「+20%」は更新と再販を合算した数値で、更新だけの単価変化は分からない。Q1 FY27 は対象 GPU 数が非開示。Q4 の対象は平均 590 基/顧客で、数十万基規模の大型契約とは性格が異なる(算出)。
- **食い違い:** (i) Moomoo の AI 要約は「92% の更新率」と書くが、92% は GPU 基準・49% は顧客基準で、単位が混同されている。(ii) Crypto Briefing は「失効する全容量」と書くが、発言は「更新**または再販**」。(iii) 非更新分の扱いは「大半が再販」(ポッドキャスト)と「残り 8% が再販」(Dolphin)で表現が異なる。

---

## 2. AI インフラの粗利率の四半期推移

### 2-1. 事実表

| 項目 | 内容 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| Q3 FY26 の AI 容量の粗利率 | **32%**(ガイダンス 30%)。「Q3 に納入した AI 容量の粗利率は 32%で、会社のガイダンス 30% を上回った」(Magouyrk)。同じ説明会でアクセラレータの粗利率は 30〜40% の見通しを再確認、周辺サービスは AI データセンター支出の 10〜20% 程度を占めうると説明 | 2026-03-10 | [B1][B2][B3][B4] | 3(原典 T1*) |
| 「ガイダンス 30%」の出所 | どの説明会でガイドしたものかは**今回確認できず** | — | — | — |
| Q4 FY26 の AI 容量の粗利率 | **数値が見つからない**(2回検索)。Magouyrk は、前払い・顧客持込(BYOH)契約($75B)について「他の契約と比べて**粗利率の劣化はない**」と説明("no degradation in margin")。Maxson は定常状態のプロジェクトレベル ROIC を「20% 台後半」と見込むと報じられた(要約、1社のみ) | 2026-06-10 | [A6][A5][B7] | 3〜4 |
| Q1 FY27 の AI 容量の粗利率 | **数値が見つからない**(3回検索)。決算スライドには「契約上のマージンは維持・改善している」旨の記載があると要約されている(スライド本文は未読) | 2026-09-10 | [B8](検索要約) | 1*(要約) |
| 全社粗利率 FY26 | 通期で**約5ポイント低下**(「想定どおり」)。要因は DC の立上げとインフラ売上の加速。Q4 は営業費の対売上比低下がこれを上回り、営業利益率は小幅上昇 | 2026-06-10 | [B5][A2] | 3〜4 |
| 全社粗利率 FY27 の見通し | 「FY27 は DC プロジェクト立上げのタイミングとミックスにより粗利率が**段階的に低下**」(Maxson)。別の要約は「DC が契約どおりの売上に達すれば、インフラの粗利率は急速に改善」と補足 | 2026-06-10 | [B5][B6] | 3 |
| 全社粗利率 Q1 FY27 | 10-Q: 売上に対するマージン(total margin)は、インフラ投資増により前年比(定率)で低下。**百分率の値は検索で取得できず**。S1 の「60.03%(第三者算出、8四半期で最低)」は今回も裏取りできなかった | 2026-09 | [B10] | 1* |
| Q1 FY27 のコスト増 | クラウド&ソフトウェアの売上原価が前年比 +77%(beancount.io の分析、**10-Q 照合なし**)。同区分の売上は +33%($17.2B)(10-Q 要約) | 2026-09 | [B9][B10] | 4 / 1* |
| 営業利益率 Q1 FY27 | GAAP 35%(前年同期 29%)、非GAAP 約 42%(前年と同水準)。GAAP 営業利益 $6.73B(+57%)、非GAAP 営業利益 $8.2B(+31%) | 2026-09-10 | [B11][B12] | 3〜4 |
| 稼働前コスト(減価償却・リース)の具体額 | **今回の検索で数値は見つからなかった**(「立上げ費用が粗利を押し下げる」という定性説明のみ) | — | — | — |
| 参考(S3 から) | The Information: 2025年6〜8月の NVIDIA レンタル粗利率 14%(未計上の減価償却を加えるとさらに約7ポイント低下)。会社は 6年・$60B の例で通算 35% と説明 | 2025-10 | S3 2-1 | 3 |

### 2-2. 算出

| # | 内容 | 算出 |
|---|---|---|
| a | Q1 FY27 の GAAP 営業利益率は +6 ポイント(29%→35%)だが、全社粗利率は低下している(10-Q)。したがって営業費の対売上比が大きく低下している | 10-Q の定性記述と営業利益率から |
| b | Q3 FY26 の 32% は「ガイダンス +2 ポイント」。この水準が Q4・Q1 FY27 で維持されたかは数値上の裏付けがない | — |

### 2-3. 事実要約

- 会社が AI 容量の粗利率を数値で示したのは Q3 FY26(32%、ガイダンス 30%)のみ。Q4 FY26・Q1 FY27 は数値が見つからず、「劣化なし」「契約上のマージンは維持・改善」という定性表現(要約経由)にとどまる。
- 全社粗利率は FY26 通期で約5ポイント低下し、FY27 もさらに低下する見通しと会社が説明。Q1 FY27 の10-Q も低下を記載。営業利益率は営業費の低下で上昇している。
- 稼働前の減価償却・リース費用の具体額は見つからなかった。**AI 容量の粗利率(契約が稼働している部分)と、全社粗利率(立上げ中の拠点費用を含む)は測る対象が異なる**ため、32% と全社粗利率の低下は矛盾しない(会社の説明の構造)。

---

## 3. 会計上の耐用年数

### 3-1. 事実表

| 企業 | サーバー・ネットワーク機器の耐用年数 | 変更・影響額 | 出典 | Tier |
|---|---|---|---|---|
| **Oracle FY2025 10-K** | サーバー・ネットワーク機器を **5年 → 6年**(FY2025 期初=2024-06-01 に遡及せず将来に向けて適用) | FY25 通期: 営業費用 **-$733M**、純利益 **+$573M**(基本 +$0.21/希薄化後 +$0.20)。Q1 FY25 だけで営業費用 -$197M(同四半期の決算説明会) | [C1][C3] | 1* |
| **Oracle FY2026 10-K** | PP&E 表の最大耐用年数は 40年(建物)。サーバー・ネットワーク機器の脚注は **6年**。FY26 の減価償却費 **$7.6B**(FY25 は $3.9B)、PP&E 総額 $122.7B、減価償却累計額 $22.7B(2026-05-31) | **FY26 に新たな耐用年数の変更は検索で見つからず**(未確認) | [C2] | 1* |
| CoreWeave | GPU を含む技術設備 **6年**(2025年 10-K)。2023年初に5年から6年へ変更。平均契約期間は約5年、直近の大型契約は5〜6年と説明(2026-03 の投資家資料の二次報道) | 変更は上場前 | [C6] | 3(10-K は T1*) |
| Microsoft | クラウドのサーバー・ネットワーク機器を **4年 → 6年**(2022年、FY2023 適用)。FY23 営業利益 約 +$3.7B(CFO 説明) | 10-K の直近記載は**未確認** | [C4] | 3 |
| Alphabet | サーバーを **4年 → 6年**、一部ネットワーク機器を 5年 → 6年(2023年適用)。2023年の減価償却 -$3.9B | 直近 10-K は**未確認** | [C4] | 3 |
| Meta | 大半のサーバー・ネットワーク資産を **5.5年**(従来 4〜5年)に延長、2025-01-01 適用。2025年の減価償却 **-$2.92B**、純利益 **+$2.59B**(+$1.00/株)(Meta 2025 年 10-K の要約) | 2025年に実施 | [C4] | 3(10-K は T1*) |
| Amazon | 一部のサーバー・ネットワーク機器を **6年 → 5年**に短縮、2025-01-01 適用。純利益への影響 **-$298M(2025年Q3の3か月)、-$677M(9か月)**(Amazon の 10-Q の要約) | 他社と逆方向の変更 | [C5] | 3〜4(10-Q は T1*) |
| 2026年の変更 | Meta・Amazon・Alphabet・Microsoft の**2026年4〜6月期 10-Q での耐用年数変更は検索で見つからなかった**(未確認) | — | — | — |
| Burry の主張(S3) | 2026〜2028年の減価償却の累計過小計上 $176B。2028年までに Oracle の利益 26.9% 過大 | 2025-11 | S3 2-2 | 3 |

### 3-2. 算出

| # | 内容 | 算出 |
|---|---|---|
| a | Oracle の 5→6年変更の FY25 営業費用軽減 $733M は、同期の EPS で約 $0.20(希薄化後)。FY25 非GAAP EPS に対する比率は未算出(FY25 非GAAP EPS の値を今回取得していない) | 10-K 記載値 |
| b | 並置: Q1 FY27 に更新された GPU の過半は 4 年以上前(1章)。Oracle の会計上の耐用年数は 6年、CoreWeave の平均契約は約5年 | 1章・3章の事実の並置(評価はしない) |

### 3-3. 事実要約

- Oracle は FY2025 に、サーバー・ネットワーク機器の耐用年数を5年から6年に延長した(FY25 の営業費用 -$733M、EPS 約 +$0.20)。FY2026 の 10-K でも6年(新たな変更は見つからず)。
- 比較対象の現状は、CoreWeave 6年、Microsoft 6年(2022年〜)、Alphabet 6年(2023年〜)、Meta 5.5年(2025年〜)、Amazon 一部5年(2025年に短縮)。Microsoft・Alphabet の直近 10-K 文言は未確認。
- **食い違い:** Yardeni(S3)は Amazon 4年前後・Meta 11〜12年・Microsoft/Google/Oracle 4〜5年とするが、10-K 要約に基づく本表(Oracle・Microsoft・Alphabet 6年、Meta 5.5年)と一致しない。Yardeni の対象設備区分が不明で、本書は 10-K 要約側を採った(要原典確認)。

---

## 4. 契約の条件と期間のミスマッチ

### 4-1. OpenAI 契約の性質

| 項目 | 内容 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| 規模・期間 | 約 $300B・5年・4.5GW・2027年開始(WSJ 報道)。**Oracle は金額を確認していない** | 2025-09 | [D1](S3 の DCD も同旨) | 3 |
| take-or-pay・解約条項・前払い | **公開情報なし。検索で確認できなかった。** Gartner のアナリストは「金額は初日から固定ではなく、段階的な増量スケジュール、リージョン配分、最低利用の階層、適用除外、再交渉ゲートを含むのが通例。いずれも非公開」と説明(推測を含む) | 2025-09 | [D1] | 3 |
| 契約上の確実性 | 解説記事は「法的に解約不能でも、経済的に保証されているとは限らない」と指摘(一般論) | 2026 | [D3] | 3 |
| 会社の説明 | Oracle は「すべての契約上のマイルストーンは達成されており、納期は契約後に OpenAI と共同で検証した」と遅延報道を否定 | 2025-09 以降 | [D2] | 3 |
| 資金面 | KeyBanc: Oracle は今後4年で最大 $100B の債務調達が必要になりうる | 2025-09 | [D1] | 3 |
| RPO 内の比率 | S&P は OpenAI を $638B の約半分と推定。S3 では 45〜47%(推計) | 2026-07 | [D6] | 3 |
| 前払い・顧客持込 | 前払い・顧客提供ハード部分 $75B(プレス)。10-Q: 重要な金融要素を含む顧客前払い $11.4B。**OpenAI 向けがどの程度かは非開示** | 2026-06 / 09 | S1 | 1* |

### 4-2. 10-K/10-Q のリスク記述(顧客集中・RPO)

| 項目 | 内容 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| RPO の増加理由 | FY26 末 RPO $638B(FY25 末 $138B)。増加は主に「期中に締結した特定の大型クラウド契約」による(10-K) | 2026-05-31 | [C2](要約) | 1* |
| 顧客の支払能力 | 「一部の顧客は高レバレッジで、自社の事業・規制リスクにさらされている」「与信審査を行っても不払い・不履行のリスクがある」(10-K の二次引用) | FY26 | [D3] | 1*(二次引用) |
| OpenAI の名指し・解約権の記述 | **10-K が OpenAI を名指しするか、顧客の解約権・RPO 取消しに関する文言があるかは確認できなかった** | — | — | — |
| リースと顧客契約の整合性 | Reuters は「Oracle は、データセンター・リースの期間・更新条件・価格が顧客契約と整合しない可能性があり、顧客が更新しない場合や履行できない場合に影響を受けうると警告している」と報道。**本文の再確認は失敗**(検索の要約のみ) | 2026-08-04 | [D4] | 3(原典 T1*) |

### 4-3. データセンター・リース(未開始コミット)と顧客契約の期間

| 項目 | 内容 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| 未開始リース・コミットの推移 | $99.8B(2025年8月 10-Q)→ $248B(2025年11月)→ $261B(2026年2月)→ $260B(2026-05-31 時点、Reuters)→ **$288B(2026-08-31)**。ほぼ全てがデータセンター関連。開始時期は FY27 Q2〜FY29。**期間 15〜19年**。貸借対照表に未計上 | 2025-08〜2026-08 | [D5][D4] | 1*(10-Q 要約) |
| Oracle の認識済みリース負債 | $37.89B。未開始 $260B は認識済みの約7倍(Reuters)。5社(Microsoft・Meta・Oracle・Amazon・Alphabet)の未開始合計 約 $1.09T、認識済み 約 $285B | 2026-08-04 | [D4] | 3 |
| 格付会社 | S&P: 2026-07-09 に BBB → **BBB-**(見通し安定)、短期格付 A-3。未開始リース $260B を調整後負債の予測に算入し、FY27 のレバレッジ約 4.4倍と予測(要約)。FOCF 赤字は FY27 がピークで 2029年に黒字化と想定。AI インフラの収益性を「不透明」と評価。OpenAI がつまずいた場合に容量が遊休化するリスクに言及。Moody's: 見通しネガティブ。2026-02 に未開始リースを「implicit debt」と扱う警告 | 2026-07〜02 | [D6][D7] | 2〜3(S&P 本文は未読) |
| 顧客契約の期間 | OpenAI 5年(WSJ)。FAM(2025-10)の例示は 6年・1GW・$60B・粗利率約35%(S1)。CoreWeave は平均5年・直近5〜6年(3章) | 2025〜2026 | S1、[C6] | 3 |

算出: リース期間 15〜19年 − 顧客契約 5〜6年 = **差 9〜14年**(15−6=9、19−5=14)。FAM の 6年例示のコスト構成(土地・DC・電力・人員 約35%、計算・ネットワーク 約65%)は契約期間内のモデルで、契約終了後のリース期間の扱いが会社資料でどう示されているかは**確認できなかった**。

### 4-4. Project Jupiter(ニューメキシコ)の不可抗力通知

| 項目 | 内容 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| 通知 | Oracle が Blue Owl 傘下の開発者側に不可抗力(force majeure)通知を送付。**電力確保の遅れの可能性**が理由 | 2026-09-23〜24 | [D8](Reuters 系) | 3 |
| 賃料繰延の条件 | 通知の目的は、遅延が生じた場合に**賃料の支払い開始を繰り延べる**こと。関係者によれば最大3年(電力コミットを満たせず 2028年開業が不成立の場合)。**自動ではなく、双方が「電力コミットの履行に関わる不可抗力事由が発生した」と合意した場合に限り**繰延が成立しうる | 2026-09 | [D8](Bloomberg 発の匿名情報) | 3 |
| 繰延の性質 | 繰延中も他の費用は支払う。賃料は支払い開始後に**リース期間全体にわたり負担**する(免除ではない) | 2026-09 | [D8] | 3 |
| 解約・デフォルト | Reuters の関係者: Oracle は**いかなる場合もリースを解約できない**。Blue Owl の出資は約 $3B で、Oracle が債務コストを負担。通知は融資契約上のデフォルト事由に**当たらない** | 2026-09 | [D8] | 3 |
| 当事者の説明 | Oracle: 「通知だけで遅延や納期の変更が確定するわけではない」「計画どおり」。Blue Owl: 「このプロジェクトに対する財務コミットメントに変更はない」 | 2026-09 | [D8] | 3 |
| 周辺事実(S3 再掲) | 約 $180 億のローンが額面の 89〜91%で取引(FT)。ガスパイプラインの稼働予定が 2026-08-15 → 2027-02-01 に延期。ニューメキシコ州土地局が経路を2度却下。リースは18年(S3) | 2026-08〜09 | S3 3-1 | 3 |
| リース契約書本文 | **非公開。条文は確認できていない**(上記はすべて報道の要約) | — | — | — |

### 4-5. 事実要約

- OpenAI 契約の take-or-pay・解約条項・前払いの有無は、公開情報では確認できない。確認できるのは報道ベースの規模(約 $300B・5年・4.5GW)と、アナリストの一般論のみ。
- 未開始リースは $99.8B(2025年8月)から $288B(2026年8月)へ1年で約2.9倍に増え、期間は 15〜19年。顧客契約は 5〜6年規模の例が多く、期間差は 9〜14年(算出)。Reuters は Oracle 自身が期間・更新・価格の不整合リスクを開示していると報じたが、本文は未確認。
- Project Jupiter の不可抗力通知は「賃料の開始を最大3年繰り延べる」ための手続きと報じられ、解約や免除ではなく、条件も双方の合意に依存する。リース条文は非公開。

---

## 5. 一時要因(FY26 非GAAP EPS $7.63)

### 5-1. 事実表

| 項目 | 内容 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| FY26 通期 EPS | 非GAAP EPS **$7.631**(+27%)。一時的な投資益を除くと **$6.83** | 2026-06-10 | [B13] | 1* |
| Q4 FY26 EPS | 非GAAP EPS **$2.111**(+24%)。一時的な投資益を除くと **$2.03**(+20%)。GAAP EPS $1.45 | 2026-06-10 | [B13] | 1* |
| プレスの文言 | 「Q4 と FY26 の結果には、特定の取引による一時的な純投資益が含まれる」。FY27 の非GAAP EPS 成長率は「同じ投資益を除くと 18%」 | 2026-06-10 | [B13] | 1* |
| **Ampere 売却益** | **$2.7B(税引前)**、**Q2 FY26(2025-09〜11月期)**に計上。会社は「GAAP・非GAAP の両方の EPS にプラス」と説明。Q2 FY26 の GAAP EPS $2.10・非GAAP EPS $2.26 | 2025-12-10 | [E1] | 1* |
| 10-K の記載 | FY26 の営業外収益(純額)は前年比 **+$3.5B**。主因は Ampere 売却益 $2.7B と「その他の投資益」$380M | FY26 | [C2](要約) | 1* |
| **Bloom Energy ワラント** | 2025年10月に Bloom が Oracle に最大 3,531,073 株・行使価格 $113.28 のワラントを付与。Bloom の会計上の評価額は付与時 $251.6M(誘因株を含め約 $323.9M)。Oracle は **2026-05-01** にキャッシュレス行使(Bloom が純 1,905,433 株 + 誘因株 248,798 株を発行)。CNBC は 2026年4月に **約 $316M の含み益**と報道。**Oracle が実際に計上した利益額は確認できなかった** | 2025-10〜2026-05 | [E3] | 3 |
| Q1 FY27 の一時益 | **Q1 FY27 の非GAAP EPS $1.92 に一時益が含まれるとする記述は見つからなかった**。Q1 FY27 のプレスにも、Q1 の一時益の注記は検索結果に出ていない。ガイダンス(2026-06)は $1.71〜1.75、実績は $1.92、コンセンサスは $1.73〜1.74。**上振れ要因は確認できず** | 2026-09-10 | [E4] | 1*〜3 |
| Q1 FY27 の非GAAP税率 | **見つからなかった**(3回検索) | — | — | — |
| Q2 FY27 ガイダンス | 非GAAP EPS **$1.83〜1.91(定率)/ $1.85〜1.93(USD)**。「Q2 FY26 の一時益を除いた」比較基準が付される。一時益を含めれば前年比は減少 | 2026-09-10 | [E4] | 1*〜3 |

### 5-2. 算出

| # | 内容 | 算出 |
|---|---|---|
| a | FY26 の一時益の EPS 寄与は **$0.80**(報告ベースの約 10.5%) | 7.631 − 6.83 = 0.801、0.801 ÷ 7.631 = 10.5% |
| b | Q4 FY26 の一時益は **$0.08/株**(Bloom ワラント関連とみられるが、**会社は内訳を明示していない。推定**) | 2.111 − 2.03 = 0.081 |
| c | Q2 FY26(Ampere)の寄与は **$0.72/株**(Q1・Q3 に一時益がないと仮定) | 0.801 − 0.081 = 0.72 |
| d | 四半期の検算: Q1 $1.47 + Q2 $2.26 + Q3 $1.79 + Q4 $2.11 = $7.63(報告値と一致) | 合計 |
| e | 一時益を除いた Q2 FY26 の EPS は約 **$1.54**(Q1・Q3 に一時益なしと仮定) | 2.26 − 0.72 = 1.54、または 6.83 − 1.47 − 1.79 − 2.03 = 1.54 |
| f | 整合チェック: Ampere $2.7B(税引前)÷ 希薄化後株数 約29億株(**仮定、未確認**)= 約 $0.93/株(税引前)。税率 20%台前半なら約 $0.72 で c と整合 | 2.7 ÷ 2.9 × (1 − 0.23) ≈ 0.72 |
| g | FY27 EPS $8.10 の増減: 一時益除く FY26($6.83)比 **+18.6%**($8.05 なら +17.9% で会社の「18%」と一致)、報告ベース($7.631)比 **+6.1%** | 8.10 ÷ 6.83 − 1、8.10 ÷ 7.631 − 1 |
| h | FY27 の残り3四半期の EPS 合計は $6.18(平均 $2.06)。Q2 ガイド中央値(USD)$1.89 を引くと Q3+Q4 で約 $4.29(平均約 $2.15) | 8.10 − 1.92 = 6.18、6.18 − 1.89 = 4.29 |

### 5-3. 事実要約

- FY26 非GAAP EPS $7.631 のうち $0.80 が一時的な投資益。内訳は、Q2 FY26 の Ampere 売却益($2.7B 税引前、EPS 寄与は算出で約 $0.72)と、Q4 FY26 の投資益 $0.08(Bloom ワラント関連と推定)。
- 会社が「FY27 の成長は +18%」と言うのは、一時益を除いた $6.83 が基準。報告ベースの $7.631 からは約 +6%。
- Q1 FY27 の $1.92 に一時益が含まれるという記述、非GAAP 税率、上振れ要因はいずれも検索で見つからなかった(未確認)。

---

## 6. 既存事業

### 6-1. 事実表

| 項目 | 内容 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| Software 売上 | Q1 FY27 **$5,550M(-3% USD・定率とも)**。前年同期 $5,721M。売上構成比 29%(前年 38%)。会社の説明: 「顧客のオンプレミス・ソフトからクラウドへの移行を反映」 | 2026-09-10 | [E4][E5] | 1* |
| 内訳(ライセンス・サポート) | **クラウドライセンス&オンプレ・ライセンスとライセンス・サポートの内訳は取得できなかった**(2回検索) | — | — | — |
| 他区分 | Services $1.4B(+5%)、Hardware $0.8B(+15%)。Cloud 全体 $11.6B(+62%)= IaaS $7.4B(+121%)+ SaaS $4.2B(+10%) | 2026-09-10 | [E4] | 1* |
| クラウド比率 | 売上に占めるクラウド比率 60%(前年同期 48%)。会社は「この傾向が続く」と記載 | 2026-09 | [B10] | 1* |
| データベース・サポートの更新率 | **見つからなかった** | — | — | — |
| Oracle Health | **見つからなかった**(個別の売上・成長率の記述なし) | — | — | — |
| マルチクラウド DB | 売上成長率 Q1 FY27 **+353%、顧客数 +180%**(Quartr のみ、単一出典)。Q3 FY26 +531%(S1)。**年換算額の開示は見つからず**。古い参考値として、Q1 FY26 のクラウド・データベース・サービスは +32% で年換算約 $2.8B 近く | 2026-09 / 2025-09 | [B11](+353%・顧客+180%)、[E6](Q1 FY26 の年換算。検索要約) | 4 / 1* |

### 6-2. 算出

| # | 内容 | 算出 |
|---|---|---|
| a | Software の前年差は **-$171M**(-3%)。SaaS は +約 $0.38B(Q1 FY26 約 $3.8B → $4.2B)。Software+Cloud Apps の合計は小幅増 | 5,550 − 5,721 = −171 |
| b | 区分の合計検算: 11.6(Cloud)+ 5.55(Software)+ 1.4(Services)+ 0.8(Hardware)= 19.35 = 総売上 $19.345B | 合計 |

### 6-3. 事実要約

- Software は Q1 FY27 に $5.55B(-3%)。会社はクラウド移行の反映と説明するが、ライセンスとサポートの内訳、DB サポートの更新率は今回確認できなかった。
- 総売上に占める Software は 38% → 29%、クラウドは 48% → 60%。ミックスは IaaS($7.4B、+121%)に大きく傾いている。
- マルチクラウド DB は成長率(+353%、顧客 +180%)のみで、売上の絶対額・年換算額は未開示または未確認。Oracle Health の数値も未確認。

---

## 7. DEF 14A(委任状説明書)の業績連動報酬

### 7-1. 事実表

| 項目 | 内容 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| 書類 | FY2026 DEF 14A(提出 2026-09 下旬)。FY2025 DEF 14A は 2025-09 | 2026-09 | [F1][F2] | 1 |
| 共同CEOの付与(2025-09-24) | Magouyrk: オプション $250M 相当、Sicilia: $100M 相当(付与額)。**80% は時間ベース(4年で権利確定)、20% は業績ベースのストックオプション(PSO)** | 2025-09-24 | [F3] | 1* |
| **PSO の KPI** | **FY2028 の非GAAP「総売上(Total Revenues)」**。測定期間は 2025-06-01〜2028-05-31(3年)。**1株当たり指標でも、株価、EPS、OCI 売上でもない** | 2026-09 | [F1](要約)、[F4][F5] | 1* |
| 権利確定の水準 | 総売上 < $100B(閾値)= 0% / $100B = **80%** / $125B(目標)= **100%** / $250B 以上(最大)= **200%**。閾値〜目標、目標〜最大の間は線形補間。上限 200% | 同上 | [F1](要約) | 1* |
| 進捗 | FY26 の非GAAP 総売上 $67.4B。PSO は完全に未獲得。委員会は目標を「FY25 比で売上が2倍超にならないと目標に届かない水準」と説明 | 2026-09 | [F1](要約)[F4] | 1* |
| 報酬額 | Magouyrk の付与日公正価値 $621.7M、FY26 の総報酬 $627.5M(Fortune)。Sicilia $248.7M(Fortune)/ $257M(Panabee)。CEO 対従業員中央値の報酬比率 6,623 対 1(中央値 $94,740) | 2026-09 | [F6][F7] | 3 |
| 行使価格 | **$308.46**(付与日終値)。2026-10-08 終値 約 $135.69(S3)はこれを下回る(算出: 135.69 < 308.46)。Ellison の付与(2025-10)は評価額 $117.8M・行使価格 $280 | 2025-09〜2026-10 | [F6][F8] | 3 |
| CFO | Hilary Maxson が **2026年4月**に就任と報じられた。新設の「Equity Choice Program」(時間ベースの株式報酬をオプション・RSU・併用から選択)を選択。CFO の業績 KPI の詳細は**未確認** | 2026-04 | [F6][F9] | 3 |
| Catz | Executive Vice Chair に異動。FY25 総報酬 $1.1M とする報道(Forbes 系) | 2025-09 | [F7] | 3 |

### 7-2. 算出

| # | 内容 | 算出 |
|---|---|---|
| a | FY2028 の PSO 閾値 $100B は、FY27 ガイダンス「$90B 以上」の **+11%**。目標 $125B は +39%、最大 $250B は +178% | 100/90 − 1、125/90 − 1、250/90 − 1 |
| b | FY26 実績 $67.4B から FY28 閾値 $100B への2年 CAGR は **+21.8%**、目標 $125B へは **+36.2%** | (100/67.4)^(1/2) − 1、(125/67.4)^(1/2) − 1 |
| c | FY30 目標 $225B(S1)は PSO の最大水準 $250B(FY28)より低い。年度が違うため直接比較ではない | — |

### 7-3. 事実要約

- 共同CEOの業績連動部分は、報酬の 20% を占める PSO で、KPI は FY2028 の非GAAP 総売上(絶対額)だけ。閾値 $100B(80%)・目標 $125B(100%)・最大 $250B(200%)。EPS・株価・OCI 売上・1株当たり指標は KPI ではない(要約経由)。
- 残り 80% は時間ベースのオプションで、行使価格 $308.46 は直近株価を上回る。業績に連動しない部分が大きい。
- 食い違い: 共同CEOの報酬額は Fortune($621.7M/$248.7M)と Panabee($628M/$257M)で異なる。Fortune は「Oracle の整理では4オプション=1株」と注記。DEF 14A 原文は未読。

---

## 8. OCI 売上見通しの更新

### 8-1. 事実表

| 項目 | 内容 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| 2025-09 の見通し | OCI 売上 FY26 $18B、FY27 $32B、FY28 $73B、FY29 $114B、FY30 $144B(FAM 2025-10 で FY30 を $166B に引上げ) | 2025-09-09 / 10-16 | S1 | 3 |
| **その後の更新・再確認** | **FY27 $32B・FY28 $73B・FY29 $114B を明示的に再確認または更新した2026年の記述は、検索で見つからなかった。** Q3 FY26 の Yahoo/Motley Fool 記事は同じ $18B→$32B→$73B→$114B→$144B を「再掲」しているが、会社の再確認ではない。Q4 FY26 の説明会報道は capex・調達が中心で OCI の年度目標への言及なし | 2026 | [G1][G2] | 3 |
| FY30 の再確認(S1) | Q4 FY26 に Analyst Day の長期目標(売上CAGR 31%、EPS CAGR 28%)を再確認と報じられた(S1、T4)。Q1 FY27 での再確認は**未確認** | 2026-06 | S1 | 4 |
| FY27 売上全体 | FY27「$90B 以上」(Q1 FY27)。OCI 単体の FY27 見通しの更新は見つからず | 2026-09 | [E4] | 1* |
| Q1 FY26 | 総売上 $14.93B、OCI **$3.3B**(+54%) | 2025-09-09 | S1 | 1* |
| **Q2 FY26** | 総売上 **$16.06B(+14% USD/+13% cc)**、予想を約 $134M 下回った。OCI(IaaS)**$4.1B(+68% USD/+66% cc)**。クラウド全体 $8.0B(+34%)、RPO $523B、GAAP EPS $2.10、非GAAP EPS $2.26。説明会で GPU 関連売上 +177% | 2025-12-10 | [E1][G3] | 1* |
| Q3 FY26 | 総売上 $17.19B、OCI $4.9B(+84%) | 2026-03-10 | S1 | 1* |
| Q4 FY26 | 総売上 $19.18B、OCI $5.8B(+93%) | 2026-06-10 | S1 | 1* |
| Q1 FY27 | 総売上 $19.345B(+30%)、OCI $7.4B(+121%) | 2026-09-10 | [E4] | 1* |
| FY26 総売上 | **非GAAP $67.4B**(DEF 14A)。FY26 ガイダンス $67B とほぼ一致 | 2026-09 | [F1](要約) | 1* |

### 8-2. 算出

| # | 内容 | 算出 |
|---|---|---|
| a | **FY26 の OCI 売上は約 $18.1B**(ロードマップ $18B と整合)。S1 で「Q2 未確認」だった欄を埋める | 3.3 + 4.1 + 4.9 + 5.8 = 18.1(Q1 の丸めを含む) |
| b | Q2 FY27 のクラウド売上は約 $13.2〜13.7B(Q2 FY26 の $8.0B に、ガイダンス +65〜71%(USD)を適用) | 8.0 × 1.65、8.0 × 1.71 |
| c | Q2 FY26 の SaaS は約 $3.9B(クラウド $8.0B − IaaS $4.1B)。+10% なら Q2 FY27 は約 $4.3B。**この仮定のもとで Q2 FY27 の OCI は約 $8.9〜9.4B** | 13.2 − 4.3、13.7 − 4.3(SaaS +10% は仮定) |
| d | 上記 c が成り立てば、FY27 上期の OCI は約 $16.3〜16.8B(Q1 $7.4B + Q2)。FY27 $32B まで残る下期は約 $15.2〜15.7B(四半期平均 $7.6〜7.9B)で、これは Q1($7.4B)をわずかに上回る程度、c で置いた Q2 の水準($8.9〜9.4B)より低い。すなわち 2025-09 のロードマップの FY27 $32B は、Q2 ガイダンスから逆算した四半期ペースに対して低めに見える(SaaS +10% の仮定に依存。会社は年度目標を更新していない) | 7.4 + 8.9〜9.4 = 16.3〜16.8、32 − 16.3〜16.8 = 15.2〜15.7、÷2 = 7.6〜7.9 |
| e | FY27 総売上「$90B 以上」に必要な下期は、Q2 の総売上を +30〜34%(Q2 FY26 $16.06B 基準)で $20.9〜21.5B と置くと、上期合計 $40.2〜40.8B → 下期 **$49.2〜49.8B(四半期平均 $24.6〜24.9B)**。下期は FY26 下期($17.19B + $19.18B = $36.37B)比で **約 +35〜37%** | 90 − 40.8〜40.2、49.2 ÷ 36.37 − 1 |
| f | 2025-09 のロードマップの FY27→FY30 の年平均成長率は +73%(S1)。FY26 実績 $18.1B → FY27 $32B は +77% | 32/18.1 − 1 |

### 8-3. 事実要約

- FY26 の OCI 売上は四半期合算で約 $18.1B(Q1 $3.3B・Q2 $4.1B・Q3 $4.9B・Q4 $5.8B)で、2025-09 のロードマップ $18B と整合。Q2 FY26 の総売上は $16.06B(予想未達)。
- FY27 $32B・FY28 $73B・FY29 $114B の年度別 OCI 見通しを、2026年の決算で更新または再確認したという記述は見つからなかった。Q1 FY27 は OCI $7.4B、Q2 のクラウド成長ガイダンスから逆算した OCI は約 $9B 前後(仮定付き)。
- 総売上「$90B 以上」には下期の前年比 約+35〜37%(算出)が必要。この前提は S1 の「残り3四半期で約+35%」と整合。

---

## 9. 出典間の食い違い(まとめ。どちらかを採らず併記)

| # | 内容 | 扱い |
|---|---|---|
| 1 | GPU 更新の「92%」: Moomoo の AI 要約は更新率 92% と書くが、92% は GPU 基準・49% は顧客基準 | 発言は「顧客の 49% が GPU の 92% を更新」。Moomoo は単位混同 |
| 2 | Q1 FY27 の「20% プレミアム」: Crypto Briefing は「全失効容量が20%高い単価で更新」、発言は「更新**または再販**」 | 発言側(Constellation/Longbridge の引用)を採用。更新のみの単価は不明 |
| 3 | 非更新 GPU: ポッドキャスト「大半が再販」、Dolphin「残り 8% が同四半期に再販」 | 表現差。公式トランスクリプトで確認要 |
| 4 | 未開始リース: Reuters 2026-05-31 時点 $260B と、2026-02 の 10-Q $261B。2026-08 は $288B | 1か月差または丸め。10-Q で確認要 |
| 5 | S&P のレバレッジ予測 約4.4倍(FY27)と CreditSights の 3.7倍(FY28、S1) | 年度・調整方法が異なる。比較不可 |
| 6 | 耐用年数: Yardeni(S3)の Oracle・Microsoft・Google 4〜5年、Meta 11〜12年と、10-K 要約の Oracle・Microsoft・Alphabet 6年、Meta 5.5年 | 10-K 要約側を採用。Yardeni は設備区分不明 |
| 7 | Amazon の短縮時期: 2025-01-01 適用(10-K)と「2024年」とする記事 | 適用日は 2025-01-01、決定は 2024年 Q4 説明会の可能性。原典確認要 |
| 8 | 共同CEOの報酬額: Fortune $621.7M/$248.7M、Panabee $628M/$257M、付与額 $250M/$100M、Forbes Italy「合計約 $900M」 | 定義(付与額か公正価値か、オプション数の換算)が異なる。DEF 14A 確認要 |
| 9 | Q2 FY27 EPS ガイダンス: $1.83〜1.91(定率)、$1.85〜1.93(USD)。Quartr は $1.83〜1.93 と併記 | 定率と USD の2系列で両立。S1 の「cc 64〜70% / USD 65〜71%」の食い違いも同じ構造 |
| 10 | FY27 EPS $8.05(2026-06)と $8.10(2026-09): Verdict の2記事が別々の値 | 時点の違い(Q4→Q1 で引上げ)。矛盾ではない |
| 11 | S1 の「Q1 FY27 売上 FY27 見通しの『引上げ』」 | 数値 $90B は不変、表現が "at least"。EPS のみ $8.05 → $8.10 |

---

## 10. 出典一覧

### 1章(GPU 更新)
- [A1] Converge Digest「Oracle's AI infrastructure business drives 93% IaaS growth」 https://convergedigest.com/oracles-ai-infrastructure-business-drives-93-iaas-growth/ (2026-06) T3
- [A2] Moomoo「Oracle Q4 FY2026 earnings conference call」(AI 生成要約) https://www.moomoo.com/community/feed/oracle-q4-fy2026-earnings-conference-call-116727818420629 (2026-06) T4
- [A3] Dolphin Research(Longport) https://longportapp.cn/topics/41705023 (2026-06) T4
- [A4] Beta Finch「Oracle Q4 2026 Earnings Analysis」(ポッドキャスト要約) https://www.audible.co.uk/podcast/Beta-Finch-Oracle-ORCL-EN/episodes/B0GMWVX7X3 (2026-06) T4
- [A5] Nasdaq「Oracle Q4 earnings call highlights」 https://www.nasdaq.com/articles/oracle-q4-earnings-call-highlights (2026-06) T3
- [A6] erp.today「Oracle's Q4 2026 Earnings Call: $638B Backlog Turns AI Cloud Growth into Funding Test」 https://erp.today/oracle-q4-2026-earnings-ai-cloud-backlog-funding/ (2026-06) T3
- [A7] Constellation Research「Oracle Q1 strong and so is capital expenditures」 https://www.constellationr.com/insights/news/oracle-q1-strong-and-so-capital-expenditures (2026-09) T3(説明会の引用あり)
- [A8] Longbridge(説明会の引用) https://longbridge.com/news/298820115 (2026-09) T3〜4
- [A9] DCD「Oracle delivered 300,000 GPUs in Q1 FY2027」 https://www.datacenterdynamics.com/en/news/oracle-delivered-300000-gpus-in-q1-fy2027/ (2026-09) T3
- [A10] Zacks https://www.zacks.com/stock/news/2988428/ (2026-09) T3
- [A11] Crypto Briefing「Oracle renews expiring AI contracts at 20% higher rates」 https://cryptobriefing.com/oracle-ai-contracts-renew-higher-rates/ (2026-09) T4
- [A12] The Next Platform「Despite hefty capital investments, the cloud starts paying off for Oracle」 https://nextplatform.com/cloud/2026/09/14/despite-hefty-capital-investments-the-cloud-starts-paying-off-for-oracle/5296362 (2026-09-14) T3

### 2章(粗利率)・5章・6章・8章の会社資料
- [B1] Seeking Alpha「Oracle targets rapid AI infrastructure expansion with $553B RPO and 32% gross margin in Q3 2026」 https://seekingalpha.com/news/4562986-oracle-targets-rapid-ai-infrastructure-expansion-with-553b-rpo-and-32-percent-gross-margin-in (2026-03) T3
- [B2] Verdict「Oracle Q3 FY26 results」 https://www.verdict.co.uk/oracle-q3-fy26-results/ (2026-03) T3
- [B3] AOL「Oracle (ORCL) Q3 2026 Earnings Call Transcript」 https://www.aol.com/finance/oracle-orcl-q3-2026-earnings-223334292.html (2026-03) T1*相当(転載)
- [B4] MarketBeat「Oracle Q3 earnings call highlights」 https://www.marketbeat.com/instant-alerts/oracle-q3-earnings-call-highlights-2026-03-10/ (2026-03-10) T3
- [B5] Briefing.com「Oracle falls as AI backlog soars but investors wanted better guidance, margins」 https://www.briefing.com/story-stocks/archive/2026/6/11/oracle-falls-as-ai-backlog-soars-but-investors-wanted-better-guidance-margins-(orcl) (2026-06-11) T3
- [B6] Outlook Business「Oracle forecasts $95 bn in capex for FY27」 https://www.outlookbusiness.com/corporate/oracle-forecasts-95-bn-in-capex-for-fy27-plans-to-raise-40-bn-in-debt-and-equity (2026-06) T3
- [B7] GuruFocus「Oracle Q4 FY26 transcript」 https://www.gurufocus.com/stock/ORCL/transcripts/8911132 (2026-06) T3
- [B8] Oracle「Q1 FY27 Oracle Earnings Slides」 https://s23.q4cdn.com/440135859/files/content_files/Q1-FY27-Oracle-Earnings-Slides.pdf (2026-09-10) T1(本文未読。検索要約のみ)
- [B9] beancount.io「Oracle FY2027 Q1 earnings analysis」 https://beancount.io/blog/2026/09/13/oracle-fy2027-q1-earnings-analysis (2026-09-13) T4
- [B10] Oracle 10-Q(2026-08-31 終了四半期) https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm (2026-09) T1(要約のみ)
- [B11] Quartr「Oracle (ORCL) Q1 2027 earnings summary」 https://quartr.com/events/oracle-corporation-orcl-q1-2027_3gvkOKJp (2026-09-13) T4
- [B12] MarketBeat「Transcript: Oracle Q1 earnings call highlights」 https://www.marketbeat.com/instant-alerts/transcript-oracle-q1-earnings-call-highlights-2026-09-10/ (2026-09-10) T3
- [B13] Oracle Q4/FY26 決算プレス https://s23.q4cdn.com/440135859/files/doc_earnings/2026/q4/earnings-result/4q26-pressrelease-final.pdf 、https://www.oracle.com/news/announcement/q4fy26-earnings-release-2026-06-10/ (2026-06-10) T1(検索要約)

### 3章(耐用年数)
- [C1] Oracle FY2025 10-K https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/orcl-20250531.htm (2025-06) T1(要約)
- [C2] Oracle FY2026 10-K https://www.sec.gov/Archives/edgar/data/0001341439/000119312526277521/orcl-20260531.htm (2026-06) T1(要約)
- [C3] MarketBeat「Oracle Q1 2025 earnings call transcript」 https://www.marketbeat.com/earnings/reports/2024-9-9-oracle-co-stock (2024-09-09) T1*相当
- [C4] Accounting Today / The Stack / Bloomberg Tax(Meta、Microsoft、Alphabet の耐用年数) https://accountingtoday.com/articles/metas-accounting-move-on-ai-servers-to-boost-profit 、https://www.thestack.technology/meta-extends-server-life-again-saving-it-2-9-billion/ (2025〜2026) T3
- [C5] Dave Friedman「The $176 billion accounting question」ほか(Amazon の短縮) https://davefriedman.substack.com/p/the-176-billion-accounting-question (2025-11) T4
- [C6] MarketBeat(CoreWeave 会議、2026-03-08)https://www.marketbeat.com/instant-alerts/coreweave-conference-insatiable-ai-demand-leaves-2026-compute-capacity-broadly-sold-out-2026-03-08/ 、Nasdaq/Motley Fool(CoreWeave 6年)https://www.nasdaq.com/articles/michael-burrys-latest-warning-could-be-bad-news-coreweave T3

### 4章(契約・リース・Jupiter)
- [D1] Fierce Network https://www.fierce-network.com/cloud/oracles-massive-openai-deal-raises-equally-big-questions 、DCD(KeyBanc)https://www.datacenterdynamics.com/en/news/oracle-may-need-to-borrow-100bn-for-openai-efforts-says-keybanc-capital-markets/ 、CIO https://www.cio.com/article/4056139/what-oracles-300b-openai-deal-means-for-enterprise-cloud-strategy.html (2025-09) T3
- [D2] MarketScreener「Oracle denies any delay in OpenAI partnership」 https://www.marketscreener.com/news/oracle-denies-any-delay-in-openai-partnership-after-stock-pullback-ce7d50d8dc88f225 T3
- [D3] Nasdaq「Oracle's backlog: potential windfall or ticking time bomb」 https://www.nasdaq.com/articles/oracles-backlog-potential-windfall-or-ticking-time-bomb 、Motley Fool https://www.fool.com/investing/2026/07/07/oracle-stock-plummeted-by-25-in-the-first-half-of/ (2026-07) T3
- [D4] Reuters「AI data-centre race builds $1 trillion lease burden for Big Tech」 https://www.thestar.com.my/tech/tech-news/2026/08/05/ai-data-centre-race-builds-1-trillion-lease-burden-for-big-tech 、https://www.streetinsider.com/Reuters/AI+data-centre+race+builds+%241+trillion+lease+burden+for+Big+Tech/26864683.html (2026-08-04) T3
- [D5] Oracle 10-Q: 2025-08 https://www.sec.gov/Archives/edgar/data/1341439/000119312525200095/orcl-20250831.htm 、2025-11 https://www.sec.gov/Archives/edgar/data/1341439/000119312525315925/orcl-20251130.htm 、2026-02 https://www.sec.gov/Archives/edgar/data/1341439/000119312526101045/orcl-20260228.htm 、2026-08 は [B10]。解説: Advisor Perspectives https://www.advisorperspectives.com/articles/2025/12/17/oracles-248-billion-rent-ai-bombshell 、Digg https://digg.com/world-business/n2py988v T1(要約)/T3
- [D6] S&P 格下げの報道: iTiger https://www.itiger.com/news/2653248061 、ppc.land https://ppc.land/s-p-cuts-oracle-to-bbb-as-ai-buildout-widens-cash-deficit-to-42bn/ 、Crypto Briefing https://cryptobriefing.com/oracle-ai-expansion-funding-challenges/ (2026-07-09) T3(S&P 本文は未読)
- [D7] Moody's の警告(IDN Financials)https://www.idnfinancials.com/jp/news/61677/moodys-warns-hyperscalers-about-us1-trillion-data-center-rent (2026-02) T3
- [D8] Project Jupiter: CTV News(Reuters)https://www.ctvnews.ca/business/article/oracle-triggers-force-majeure-on-data-centre-project-over-power-delays-source-says/ 、Bloomberg Government https://news.bgov.com/artificial-intelligence/oracle-cites-force-majeure-to-shield-itself-on-big-data-center 、Insurance Journal https://www.insurancejournal.com/news/west/2026/09/25/886812.htm 、roic.ai https://www.roic.ai/news/oracles-force-majeure-notice-on-new-mexico-ai-data-center-rattles-investors-09-24-2026 (2026-09-24/25) T3

### 5章・6章・8章
- [E1] Oracle Q2 FY26 決算プレス https://www.oracle.com/news/announcement/q2fy26-earnings-release-2025-12-10/ 、Seeking Alpha PR https://seekingalpha.com/pr/20335876 (2025-12-10) T1(要約)
- [E3] Bloom ワラント: New Mexico NewsPort https://newmexiconewsport.com/?p=29399 、Sherwood https://www.sherwood.news/markets/bloom-energy-spikes-expanding-fuel-cell-power-deal-oracle-warrants/ 、Yahoo Finance(CNBC)https://finance.yahoo.com/markets/stocks/articles/oracles-bloom-bet-already-316-161027061.html (2025-10〜2026-05) T3
- [E4] Oracle Q1 FY27 決算プレス https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/ 、https://s23.q4cdn.com/440135859/files/content_files/1q27-pressrelease-September_FINAL.pdf 、Q1 ガイダンス調整表 https://s23.q4cdn.com/440135859/files/doc_financials/2026/q4/1q27guidance-gaap-to-non-gaap-recons_FINAL.pdf 、Newsquawk https://www.newsquawk.com/headlines/oracle-orcl-q1-2027-usd-adj-eps-192-exp-173-revenue-193bln-exp-1913bln- (2026-09-10) T1(要約)/T3
- [E6] Oracle Q1 FY26 決算プレス(クラウド・データベース・サービス +32%、年換算約 $2.8B)https://www.oracle.com/news/announcement/q1fy26-earnings-release-2025-09-09/ (2025-09-09) T1(検索要約)
- [E5] Storage Newsletter「Oracle Fiscal 1Q27 financial results」 https://storagenewsletter.com/2026/09/23/oracle-fiscal-1q27-financial-results (2026-09-23) T3
- [G1] Yahoo Finance / Motley Fool(OCI ロードマップの再掲)https://finance.yahoo.com/news/why-oracle-no-brainer-growth-093000030.html (2025-09-11) T3
- [G2] Nasdaq「Oracle Q4 earnings call highlights」([A5] と同一)
- [G3] roic.ai Q2 FY26 トランスクリプト https://www.roic.ai/quote/ORCL/transcripts/2026-year/2-quarter (2025-12) T3

### 7章(DEF 14A)
- [F1] Oracle FY2026 DEF 14A https://www.sec.gov/Archives/edgar/data/0001341439/000119312526402816/orcl-20260925.htm (2026-09) T1(検索要約のみ。本文未読)
- [F2] Oracle FY2025 DEF 14A https://www.sec.gov/Archives/edgar/data/1341439/000119312525220801/d72066ddef14a.htm (2025-09) T1(未読)
- [F3] Oracle 8-K(共同CEO任命・付与)https://www.sec.gov/Archives/edgar/data/1341439/000119312525210089/d921500d8k.htm (2025-09) T1(要約)
- [F4] Calcalist https://www.calcalistech.com/ctechnews/article/clab37g3t (2026-09) T3
- [F5] Panabee https://www.panabee.com/news/oracle-executive-compensation-2026 (2026) T3〜4
- [F6] Fortune「Oracle Larry Ellison CEO pay」 https://fortune.com/2026/09/26/oracle-larry-ellison-ceo-pay/ (2026-09-26) T3
- [F7] People Matters / Forbes 系 https://www.peoplematters.in/news/compensation-benefits/oracle-filing-shows-ceo-earned-6623-times-more-than-median-employee-52392 (2026-09) T3
- [F8] Bitcoin.com News(オプションが行使価格割れ)https://news.bitcoin.com/featured/oracle-gave-larry-ellison-and-his-co-ceos-nearly-1-billion-in-stock-options-by-year-end-every-single-one-was-underwater-49201/ (2026) T4
- [F9] Yahoo Finance「Oracle's CFO got $26M stock」 https://finance.yahoo.com/markets/stocks/articles/oracles-cfo-got-26m-stock-184500098.html (2026) T3

---

## 11. 未確認事項(優先順)

1. **GPU 更新:** Q4 FY26 説明会の公式トランスクリプトでの文言照合。更新時の単価変化(%)、契約期間、GPU の世代(A100/H100 の別)。Q1 FY27 の更新対象数(GPU 数・顧客数)と更新のみの単価変化(更新と再販の内訳)。CoreWeave の A100 契約が 2029 年まで延長されたとする記事(blockspace.media、xenospectrum。タイトルのみ確認、本文未読)。
2. **粗利率:** Q4 FY26・Q1 FY27 の AI 容量の粗利率の数値。全社粗利率の四半期推移(Q1 FY26〜Q1 FY27)の公式値(10-Q/10-K の損益計算書から取るべき)。S1 の 60.03%(Q1 FY27)の裏取り。立上げ中拠点の減価償却・リース費用の金額。Q3 FY26 の「ガイダンス 30%」の出所。
3. **耐用年数:** Microsoft・Alphabet の直近 10-K の文言、Meta・Amazon・Alphabet・Microsoft の2026年 10-Q での変更の有無。Oracle の FY26 10-K の PP&E 注記全文(耐用年数の表)。Yardeni の食い違い(Meta 11〜12年)の対象設備。
4. **契約条件:** OpenAI 契約の take-or-pay・解約・前払い。10-K/10-Q のリスク要因に OpenAI の名指しがあるか、RPO の取消し・解約権に関する文言。Reuters が報じた「リースと顧客契約の期間・更新・価格の不整合」の10-Q 原文。S&P の格下げ文書の原文(リース $260B の扱い、レバレッジ 4.4倍)。Jupiter のリース条文(不可抗力条項、賃料繰延の条件、3年の根拠)。
5. **一時要因:** Bloom ワラントで Oracle が実際に計上した利益額と計上四半期の公式値。Q1 FY27 の非GAAP EPS $1.92 に一時益が含まれるか、上振れ要因、非GAAP 税率(Q1 実績・Q2 ガイダンスの前提)。希薄化後株数(5-2 の f で29億株を仮定)。
6. **既存事業:** Q1 FY27 のライセンス/サポートの内訳、DB サポートの更新率、Oracle Health の売上、マルチクラウド DB の絶対額・年換算額と +353% の裏取り(単一出典)。
7. **DEF 14A:** 原文での PSO の定義(非GAAP 総売上の調整方法)、Ellison・Maxson の業績 KPI、FY2025 DEF 14A との比較、報酬額の正確な数値。
8. **OCI 見通し:** FY27・FY28・FY29 の OCI 見通しの2026年時点の再確認有無(説明会トランスクリプトの全文確認が必要)。FY30 目標($225B/$21/$166B)の Q1 FY27 での再確認。
9. **検索上限:** 本調査は 45/45 回を使い切った。原典(SEC EDGAR の 10-K/10-Q/DEF 14A、Oracle IR の決算説明会トランスクリプト・スライド)の直接閲覧が最優先。
