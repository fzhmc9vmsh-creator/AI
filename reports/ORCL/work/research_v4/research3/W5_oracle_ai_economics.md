# W5: Oracle(NYSE: ORCL)AI インフラ契約の経済性と、利益率についての会社の見通し

- 作成日: 2026-10-12 / 担当: 収集 W5(現在の粗利率と将来の粗利率を分ける材料)
- 範囲: 事実・数値・出典の整理のみ。投資判断・推奨は書かない。
- 取得手段: WebSearch のみ 26 回(上限 26 回を使い切った。standard 25 回、extended 1 回)。WebFetch なし。**会社の原文(決算説明会の書き起こし、スライド、10-K、10-Q、FAM 資料)は 1 件も直接開いていない。** 数値と発言はすべて検索ツールの要約に書かれていた内容で、原典で未照合。
- 表記: 「欠損」= 見つからなかった。「(算出)」= 調査者の計算(式を併記)。Tier は 1=会社開示・決算説明会、2=規制当局等、3=報道・アナリスト、4=ブログ・SNS・AI 要約・集約サイト。会社の原本でも検索要約経由なら「1*」(Tier 3 相当として扱うこと)。
- 出典 ID `[W5-xx]` は本書末尾の出典一覧。`[既S1]` `[既S3]` `[既S4]` は `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research/` の既存調査、`[既R5]` `[既R7]` は `.../research2/` の既存調査。既存と重複する事実は再掲に留め、「(再掲)」と書いた。
- 会計期間: Oracle の決算期末は 5/31。Q3 FY26 = 2025-12〜2026-02(2026-03-10 発表)、Q4 FY26 = 2026-03〜05(2026-06-10 発表)、Q1 FY27 = 2026-06〜08(2026-09-10 発表)。

---

## 0. 要約(事実のみ。10 行)

1. **粗利率の会社見通し(2025-10-16、FAM)**: AI クラウドインフラの調整後粗利率は 30〜40%、従来型(エンタープライズ)は 65〜80%。6 年・$60B・年間原価約 $6.4B の例示で粗利率約 35%(算出では 36.0%)。Reuters は「契約期間を通じて概ね一定(steady)」と報道。[W5-09][W5-13] T3
2. **「初期は低く後期は高い」という会社の定量説明は、今回の検索では見つからなかった。** Computer Weekly は「契約期間中に 30〜40% 上昇」と書き、Reuters の「一定」と食い違う(§10)。[W5-10] T3
3. **現在の AI 粗利率**: 会社が数値を示したのは Q3 FY26(2026-03-10)の「納入した AI 容量の粗利率 32%、ガイダンス 30%」のみ。Q4 FY26・Q1 FY27 の AI 粗利率の数値は**欠損**(定性表現のみ)。[W5-05][W5-06] T3
4. **全社粗利率と営業利益率**: FY26 の全社粗利率は約 5 ポイント低下(CFO「想定どおり」)。Q1 FY27 も低下。一方、非 GAAP 営業利益率は Q1 FY27 で 42%(前年同期並み)、営業費の対売上比低下が相殺。[W5-27][W5-02][W5-40] T3
5. **更新・再販**: Q1 FY27、更新期を迎えた GPU は「更新または再販」され、従来契約比 +20%、過半は 4 年以上前の GPU。GPU 稼働率 97.9%。複数媒体が同一数値を報じる(原典未照合)。[W5-43] T3/T4
6. **契約条件**: take-or-pay、解約条項、価格改定条項は公開情報で**確認できない**。確認できたのは前払い・顧客持込(BYOH)の累計 $75B と、Q1 FY27 に受領した「重要な金融要素を含む前払い」$11.4B(前年同期はゼロ)。[W5-22][W5-42] T1*
7. **第三者推計**: The Information(2025-06〜08)14%、5 四半期平均約 16%。Guggenheim は契約通算で約 25%、Goldman は典型契約で約 35%、Morgan Stanley は AI インフラ粗利率約 40%(2025-09)、EVR-ISI は FY29 の AI サービス約 30%。Jefferies・UBS・Barclays・Mizuho の年度別モデルは**欠損**。
8. **建設速度**: Abilene は整地開始 2024-05-31 から Building 1 稼働(2025-09-26〜30)まで約 16 か月、Building 2(2025-12-24)まで約 19 か月(算出)。全 8 棟は 2026 年後半〜2027 年にずれ込み(再掲)。会社は「着工〜稼働を短縮することが粗利率改善の最短路」と説明。[W5-30][W5-31][W5-32] T3
9. **OpenAI 以外**: Q1 FY27 に新規 $30B 超、経営陣は「OpenAI 以外の受注残が過去 1 年で 2 倍超」と説明(二次報道のみ。金額は欠損)。Meta は約 $20B の商談報道(2025-09)。xAI・NVIDIA・AMD の契約額は非開示。[W5-38][W5-44] T3
10. **推論と学習の比率**: 会社の開示は**欠損**。Ellison は 2025-09 に「AI 推論市場は学習市場より遥かに大きい」と発言(市場予測であり OCI の実績比率ではない)。推論向け単価・利益率の会社発言は見つからなかった。[W5-45] T3

---

## 1. 会社の発言: 粗利率・営業利益率(時系列)

### 1-1. 発言の一覧

| # | 日付 | 話者・場 | 内容(引用は検索要約中の英文。逐語の保証なし) | 文脈 | 出典 | Tier |
|---|---|---|---|---|---|---|
| 1 | 2025-10-16 | Magouyrk、FAM | 「AI クラウド計算インフラの提供で調整後粗利率 30%〜40%、従来型クラウドとビジネスインフラは 65%〜80%」(Reuters)。「契約期間を通じて概ね一定」(Reuters)。例示は 6 年・$60B の契約で年約 $6.4B の原価。Bloomberg はこれを粗利率 35% と報道。Magouyrk は「最大級の顧客にも当てはまる例示」と説明 | 例示は仮想契約 | [W5-09][W5-13] | 3 |
| 2 | 2025-10-16 | FAM 資料(Magouyrk 資料) | 非 GAAP 粗利率: エンタープライズ 65〜80%、分散クラウド 40〜60%、AI インフラ 30〜40%(検索要約。資料本体は未開) | OCI の区分別 | [W5-08][W5-11][W5-46] | 1*/3 |
| 3 | 2025-10-16 | 同上(Goldman の分解) | 6 年・$60B の注文: 土地・DC・電力が原価の 35%、計算・ネットワーク・ストレージが 65%、全体の粗利率約 35% | 証券会社による会社資料の整理 | [W5-13][W5-24](検索 #18 の要約) | 3 |
| 4 | 2026-03-10 | Magouyrk、Q3 FY26 | 「Q3 に納入した AI 容量の粗利率は 32%で、ガイダンス 30% を上回った」。OCI のデータベースサービスの粗利率はこれを大きく上回る。AI アクセラレータの粗利率 30〜40% を再確認(再掲 [既S4]) | 納入済み(稼働中)容量の粗利率 | [W5-05][W5-06][W5-07] | 3(原典 T1*) |
| 5 | 2026-03-10 | Magouyrk、Q3 FY26 | 「納入された容量は、すでに非常に収益性の高いレートで契約されている」「AI インフラの収益性は、プロジェクトが稼働するにつれて上昇し続ける見込み」(要約)。利益を抑える主因は「同時に多数の施設が建設中であること」で、費用が容量の稼働より先に発生する | 立ち上げ期の説明 | [W5-32] | 3 |
| 6 | 2026-03-10 | Magouyrk、Q3 FY26 | 「建設期間を短縮する」「より早く容量を稼働させることが、利益率改善の最短路」。ネットワーク・ハードウェア・電力のコストを最適化し、データセンターをより安く納入できるようになっている | 立ち上げ期の短縮と原価低減 | [W5-32][W5-33][W5-34] | 3 |
| 7 | 2026-03-10 | Magouyrk、Q3 FY26 | 顧客持込ハードと前払いを組み合わせる契約で $29B 超を獲得。「Oracle 側のキャッシュ流出はない」。数日以内に最大 $50B の調達計画のうち $30B を調達 | 資本負担の移転 | [W5-05] | 3 |
| 8 | 2026-06-10 | Maxson、Q4 FY26 | 「粗利率は想定どおり約 5 ポイント低下した。インフラ事業の立上げの影響が出始めている」。営業利益率は「粗利率の低下が営業費の減少で相殺され、小幅上昇」。非 GAAP 営業利益 $8.6B(+22%) | FY26 通期の全社粗利率 | [W5-27][W5-28] | 3(原典 T1*) |
| 9 | 2026-06-10 | Maxson、Q4 FY26(要約) | FY27 は DC プロジェクトの立上げ時期とミックスにより粗利率が段階的に低下する見通し。別要約は「DC が契約どおりの売上に達すれば、インフラの粗利率は急速に改善」「コストを顧客に転嫁する仕組みがある」(再掲 [既S4] の B5・B6 と同趣旨) | 将来 | [W5-28][W5-27] | 3/4 |
| 10 | 2026-06-10 | Magouyrk、Q4 FY26(AI 生成要約) | 四半期の AI インフラ契約 $67B の大半は BYOH か前払い。前払い・BYOH は累計 $75B で、他の契約と比べて「粗利率の劣化はない」。コストが確定している場合は固定価格契約とし、不確実な場合は避ける。**AI 生成の要約であり、書き起こしで未確認** | 契約種別と粗利率 | [W5-28][W5-29] | 4 |
| 11 | 2026-09-10 | Maxson、Q1 FY27 | 粗利率は DC の立上げとインフラ売上の比率上昇で低下。営業費の減少が相殺。非 GAAP 営業利益 $8.15B、営業利益率 42%(前年同期並み)。GAAP 営業利益率は 35%(+6 ポイント、再掲 [既S4]) | 全社粗利率は低下、営業利益率は維持 | [W5-02][W5-40] | 3 |
| 12 | 2026-09-10 | Q1 FY27(スライド、要約) | 「契約上のマージンは維持・改善」とする記載(再掲 [既S4]。今回の再検索 1 回では確認できず) | 契約ベース | [既S4] | 1*(要約) |

注 1: 非 GAAP 営業利益率 42%(算出: $8.15B ÷ 売上 $19.345B [既R1] = 42.1%)。
注 2: 「AI 粗利率の数値」は #4(Q3 FY26 の 32%)が最後。Q4 FY26 と Q1 FY27 の AI 粗利率の数値は 3 回の検索(§12)で見つからなかった。

### 1-2. 会社の説明の構造(発言を並べただけ。解釈は含まない)

| 測る対象 | 会社が言ったこと | 数値 |
|---|---|---|
| 稼働済み AI 容量 | 契約期間を通じ 30〜40%、Q3 FY26 の実績は 32% | 32%(1 四半期) |
| 全社 | 立上げ中の拠点の費用を含み、FY26 で約 5 ポイント低下、FY27 も低下見通し | 水準の絶対値は本書では欠損([既R1] の P&L 参照) |
| 営業利益率 | 営業費の対売上比低下で維持 | 非 GAAP 42%(Q1 FY27) |
| 将来 | 稼働の進展で収益性は上昇。時期・水準の数値は示されていない | 欠損 |

---

## 2. 契約例示の算数(FAM の 6 年・$60B)

| 項目 | 値 | 式・根拠 |
|---|---|---|
| 総売上 | $60B | 会社の例示(Reuters、Bloomberg) |
| 期間 | 6 年 | 同上 |
| 年間売上 | $10B | (算出)60 ÷ 6 |
| 年間原価 | 約 $6.4B | 会社の例示(Reuters) |
| 年間粗利益 | $3.6B | (算出)10 − 6.4 |
| 粗利率 | 36.0% | (算出)3.6 ÷ 10。Bloomberg の報道値は 35%(丸めの差と考えられるが、原資料未照合) |
| 原価のうち土地・DC・電力 | 約 $2.24B/年(35%) | (算出)6.4 × 0.35。35% は Goldman の整理 |
| 原価のうち計算・ネットワーク・ストレージ | 約 $4.16B/年(65%) | (算出)6.4 × 0.65 |
| 1GW あたりの年間売上 | $10B(= $10M/MW/年) | 例示が 1GW 規模の場合([既S1][既R7] に記載) |
| 毎年同じ原価という前提 | 会社の例示は「各年約 $6.4B」。原価に減価償却を含むか、GPU の更新(再購入)を含むかは**検索要約では不明** | 欠損 |

- 例示は「各年約 $6.4B の原価」という形で報じられている。検索要約には、初年度の立上げ費用(稼働前の賃料・電力)や期間後半の GPU 更新の扱いについての記述がない。会社資料の原本で要確認。

---

## 3. 立ち上げ費用(稼働前の賃料・電力・減価償却)の説明と会計

| # | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| 1 | Maxson: 粗利率の低下は「DC の立上げ(ramping up)」と「インフラ売上の加速」が要因 | 2026-06-10、2026-09-10 | [W5-27][W5-02] | 3 |
| 2 | Magouyrk: 同時に多数の施設を建設しているため、費用が容量の稼働より先に発生し、短期的に粗利率を押し下げる。納入後の容量は高収益のレートで契約済み | 2026-03-10 | [W5-32] | 3 |
| 3 | DCD: 社内資料によれば、チップがデータセンターに到着してから顧客が支払い始めるまでに空白期間があり、粗利率を押し下げる。Guggenheim の John DiFucci は、AI 学習案件では開始時に粗利率が低く、契約全体では約 25% になると見ていた | 2025-10 | [W5-18] | 3 |
| 4 | The Information: 14% は人件費・電力・その他の直接費と「一部の減価償却」を含む。未計上の減価償却を加えるとさらに約 7 ポイント低下。→(算出)125 ÷ 900 = 13.9%、13.9% − 7pt = 約 6.9% | 2025-10 | [W5-16][W5-17] | 3/4 |
| 5 | Seeking Alpha: Oracle はデータセンターの多くを賃借している。電力、サーバー更新、GPU レンタルの値引き、稼働率の変動がクラウド粗利率の重しになる | 2025-10 | [W5-19] | 3 |
| 6 | Trefis: FY26 に粗利率が約 5 ポイント低下し、営業利益率は 3 年連続で上昇。Abilene は直近の決算時点で容量の 42% を納入済み、残りは全額売上に寄与する前 | 2026-08-07 | [W5-20] | 3 |
| 7 | 未開始のリース契約(再掲): $99.8B(2025-08)→ $288B(2026-08)、期間 15〜19 年。顧客契約は 5〜6 年の例が多い | 2026-08 | [既S4] | 1*/3 |
| 8 | 10-Q(Q1 FY27)の無条件購入義務: 約 $34.15B(主にクラウドインフラ部品とデータセンター電力。固定または最低購入数量を含む)。OpenAI への言及や解約条項の記載は要約中になし | 2026-08-31 | [W5-22] | 1* |
| 9 | **リース開始日、減価償却の開始日、収益認識の開始日の関係(稼働前の費用をどこに計上するか)についての、会社の公式な会計説明は見つからなかった** | — | — | 欠損 |

- 14% の測り方: 売上約 $9 億・粗利益約 $1.25 億(2025 年 6〜8 月の 3 か月)= 13.9%(算出: 125 ÷ 900)。1 年の推移は 10% 未満〜20% 強で平均約 16%([W5-17][W5-18]、再掲 [既S3])。

---

## 4. 更新・再契約(+20%、稼働率)

### 4-1. 会社の発言

| 四半期 | 発言(英文は報道の引用) | 話者 | 数量 | 稼働率 | 出典 | Tier |
|---|---|---|---|---|---|---|
| Q4 FY26(2026-06-10) | "In Q4, 35,000 GPUs from 59 separate customers were up for renewal. 49% of those customers renewed for 92% of those GPUs."(再掲 [既S4]) | Magouyrk と報道 | 対象 35,000 GPU・59 顧客(顧客の 49% が GPU の 92% を更新) | 97.5%(再掲 [既S1]) | [既S4] | 3(原典 T1*) |
| Q1 FY27(2026-09-10) | "Of all the GPUs that came up for renewal in Q1, that capacity was renewed or resold at a 20% premium to prior contracts. The majority of those GPUs are 4 years or older."(Constellation Research・Longbridge の引用。再掲 [既S4]) | Magouyrk | 数量・顧客数・更新率は開示が見つからない | 97.9% | [W5-43][既S4] | 3/4 |

- 今回の再検索(1 回)で、+20% と「4 年以上」と稼働率 97.9% は、Cryptobriefing、KuCoin、DCD、Longbridge、Remio、solutions-numeriques など複数媒体で同一数値が報じられていることを確認した([W5-43])。ただしいずれも会社原本ではない。Q1 FY27 の最初の検索では、Betafinch の AI 生成要約にしか +20% が出ず、「第 2 の出典が見つからない」との結果も得ていた(§10 の食い違い)。
- 表現の差: 「全量(all)」「of all」「過半(majority)」の違いは報道間にある。発言の主語は「更新または再販」であり、「更新のみ」の単価ではない。

### 4-2. 稼働率 97.9% の文脈

- 97.9% は「GPU 稼働率」(utilization)として報道されたが、**分母・分子(納入済み GPU のうち課金中の割合か、使用率か)の定義は見つからなかった**(欠損)。[W5-43]
- Q4 FY26 97.5% → Q1 FY27 97.9%(+0.4 ポイント)。納入 GPU は Q1 FY27 に 30 万基超(前四半期の約 3 倍とする報道)、納入電力は約 850MW。[W5-36][W5-43][W5-04]

### 4-3. +20% を粗利率に当てはめた機械的な試算(算出。事実ではなく算数)

仮定: 原価は不変、全量が従来契約比 +20% の単価。式: 新粗利率 = 1 − (1 − 旧粗利率) ÷ 1.2

| 旧粗利率 | 新粗利率 | 備考 |
|---|---|---|
| 14% | 28.3% | The Information の 2025-06〜08 |
| 16% | 30.0% | 同 5 四半期平均 |
| 30% | 41.7% | 会社の Q3 FY26 ガイダンス |
| 32% | 43.3% | Q3 FY26 実績 |
| 35% | 45.8% | FAM の例示 |
| 40% | 50.0% | FAM の上限 |

- この試算が成り立たない要因(事実として確認できないもの): 更新対象の GPU の簿価・減価償却の残り、再販に要する営業費、更新期間、更新後の電力・賃料の変化、+20% の基準が時間当たり単価か総額か。いずれも欠損。
- 市場の並置(再掲 [既S4] 1章): H100 ネオクラウド指数 $2.00(2025-12)→ $2.75〜2.80(2026-07/08)= 約 +38〜40%(算出)。基準が異なり +20% と直接比較できない。

---

## 5. 契約の条件(take-or-pay・期間・解約・価格改定・前払い・BYOH・収益認識)

| 項目 | 判明していること | 欠損 | 出典 | Tier |
|---|---|---|---|---|
| take-or-pay(最低利用保証) | 会社の公開資料に記載は見つからなかった。Gartner の一般論(段階的増量、最低利用の階層、再交渉ゲートが通例)と、報道の「最低利用と再交渉ゲートの偶発条件」の指摘のみ(契約本文ではない) | OpenAI を含む個別契約の有無 | [既S4 D1]、[W5-52] | 3/4 |
| 契約期間 | 会社の例示は 6 年。OpenAI は約 5 年・約 $300B・2027 年開始と WSJ が報道(OpenAI は 4.5GW を確認、総額は非開示)。CoreWeave は平均約 5 年(再掲) | 個別契約の期間分布 | [W5-09][既S1][既S4] | 3 |
| 解約条件 | 公開情報なし。Reuters(2026-08-04)は「Oracle は、DC リースの期間・更新条件・価格が顧客契約と整合しない可能性があり、顧客が更新・履行しない場合に影響を受けうると警告」と報道(再掲 [既S4]、本文未確認) | 解約権、違約金、顧客の信用補完 | [既S4] | 3 |
| 価格改定条項 | Magouyrk(AI 要約): コストが確定している場合は固定価格、不確実な場合は避ける。別要約: コストを顧客に転嫁する仕組みがある | 電力・GPU 価格の転嫁条項の具体 | [W5-28][W5-27] | 4/3 |
| 前払い・BYOH | 前払い・顧客提供ハード部分は累計 $75B(会社発言)。Q3・Q4 の RPO 増の大半はこの型(会社発表)。Q3 FY26: $29B 超。Q4 FY26: $67B | 前払いの比率、返金条件、BYOH の保有者・所有権 | [W5-42][W5-05][W5-28] | 1*/3 |
| 前払いの金融要素 | 10-Q: Q1 FY27 に「重要な金融要素を含む前払い」を $11.4B 受領。前年同期はゼロ。判断要素は、支払時期、約束した対価と現金販売価格の差、市場金利。履行から支払いまで 1 年以内なら調整を省く実務上の便法を適用 | 金融要素の利率、利息費用の計上先、収益への加算額 | [W5-22] | 1* |
| 同 $11.4B の位置づけ | Q1 FY27 の営業 CF(約 $23B、再掲 [既S1])の約 50%(算出: 11.4 ÷ 23 = 49.6%)。「前払いによる営業 CF」と書く報道あり | 営業 CF の内訳(会社開示)の確認 | [W5-39][既S1] | 3/4 |
| 収益認識 | RPO の認識時期: Q4 FY26 は 12% が 12 か月以内、34% が 13〜36 か月(算出: 合計 46%、残り 54% は 37 か月以降)。Q1 FY27 は約 13% が 12 か月以内。金額換算(算出): $638B × 12% = $76.6B、$664B × 13% = $86.3B | 期間按分(定額)で認識する旨の会社の明示記述。BYOH 契約で売上に計上する範囲(ハード部分を除くか) | [W5-42][W5-22] | 1* |
| BYOH と粗利率 | Magouyrk(AI 要約): 前払い・BYOH 契約は他の契約と比べて粗利率の劣化なし | 率の水準 | [W5-28] | 4 |

---

## 6. 第三者の推計(粗利率・営業利益率)

### 6-1. 一覧

| 時点 | 出所 | 内容 | 対象 | 出典 | Tier |
|---|---|---|---|---|---|
| 2025-10-07 報道 | The Information(社内資料) | NVIDIA チップのレンタル: 2025-06〜08 の売上約 $9 億、粗利益約 $1.25 億(14%)。5 四半期平均約 16%、範囲は 10% 未満〜20% 強。減価償却を全額加えるとさらに約 7 ポイント低下。少量の新旧チップのレンタルで損失。(再掲 [既S3]) | レンタル事業の四半期 | [W5-16][W5-17][W5-18] | 3 |
| 2025-10 | Jensen Huang(NVIDIA) | 新技術の導入初期は収益性が低いのが通常で、ライフサイクル全体では大きな利益が出ると予想 | 一般論 | [W5-17] | 3/4 |
| 2025-10 | The Information(続報の見出し) | 「Oracle、AI クラウドの粗利率について投資家を安心させるが、旧世代 NVIDIA チップでは利益を出すのに苦戦」(見出しのみ確認。有料) | — | [W5-16] | 3 |
| 2025-10 | Guggenheim(John DiFucci) | AI 学習案件の開始時は粗利率が低く、契約全体で約 25% | 契約通算 | [W5-18] | 3 |
| 2025-10 | Goldman Sachs | 典型的な 6 年・$60B の OCI 契約で全体の粗利率約 35%。全社粗利率は約 72%(FY25)から約 58%(FY28)へ低下するとの記述あり(1 媒体のみ。再検索で再確認できず) | 契約例/全社 | [W5-13][W5-24] | 3(58% は 4 相当) |
| 2025-09 | Morgan Stanley(Weiss/Reynolds) | AI インフラの粗利率約 40%、オンプレ DB 約 97%、戦略的 SaaS 約 75%。OCI 売上は FY26 約 $18B から FY30 $144B。ミックス変化で全社利益率が悪化と指摘 | 事業別 | [W5-23] | 3 |
| 2026-09 | Morgan Stanley(Sanjit Singh、中立、目標株価 $210) | AI インフラの粗利率が、従来のソフトウェア事業のような高水準に達することは実証されていない(Q1 FY27 に関連する注記と要約) | 定性 | 検索 #9 の要約(URL 特定不可。W5-23 周辺) | 3 |
| 2025-10 以降 | EVR-ISI(Evercore) | 基本ケースで FY29 の粗利率: AI サービス約 30%、コア OCI 約 65%、DBaaS 約 75% | FY29 | [W5-25] | 3 |
| 日付不明 | KeyBanc | IaaS の非 GAAP 粗利率は現在 42.4%、GPU・AI へのシフトで低下を予想 | IaaS | 検索 #9 の要約(URL 特定不可。W5-23 周辺) | 3 |
| 2025-10 | CreditSights | FY30 売上 $225B(CAGR 31%)、OCI は FY30 売上の約 74%(算出: 166 ÷ 225 = 73.8%)、AI Database は FY30 に $20B。capex 予想は FY27 $67.5B(2026-04 時点)、FY28 $85B(再掲 [既R5] と整合) | 全社 | [W5-11][W5-49] | 3 |
| 2025-10 | UBS | 15 倍 FY30 EPS で割安との評価(粗利率の数値は要約になし) | — | [W5-50] | 3 |

### 6-2. 欠損

- Jefferies、UBS、Barclays、Mizuho の AI インフラ年度別粗利率・営業利益率のモデルは、2 回の検索(§12 #15、#9)で**見つからなかった**。
- Morgan Stanley・Goldman・Guggenheim の営業利益率モデル(年度別)も**欠損**。
- 2026 年に入ってからの The Information による 14% 報道の続報は**見つからなかった**(1 回の検索)。

---

## 7. 競争優位として会社・報道が挙げるもの

### 7-1. 一覧

| 項目 | 会社・報道の主張 | 検証できる数値 | 検証できなかったもの | 出典 | Tier |
|---|---|---|---|---|---|
| 建設速度 | Magouyrk(FAM、2025-10)は Abilene のスーパークラスタ(約 20 万基の NVIDIA GPU)を、大型案件を「数年でなく数か月」で納入できる証拠として挙げた | Abilene の着工〜稼働(下記 7-2)。FY26 に約 1.2GW を稼働、Q1 FY27 に約 850MW を納入(再掲 [既R7]) | 他社との同条件比較。Magouyrk の速度比較の発言は見つからなかった | [W5-34][W5-35](検索 #20 の要約) | 3 |
| 建設期間の短縮 | Magouyrk(2026-03): 建設中の期間を短縮することが利益率改善の最短路 | — | 短縮の実績(月数の推移) | [W5-32] | 3 |
| 原価低減 | Magouyrk(2026-03): ネットワーク・ハードウェア・電力のコストを最適化し、より安く納入 | 数値なし | 1MW あたり原価の推移 | [W5-33][W5-34] | 3 |
| 電力確保 | 今後 3 年(FY29 まで)で 10GW を確保。Q3 FY26 に 400MW を稼働(DCD 見出し) | 10GW、400MW | 確保の内訳(契約種別) | [W5-35] | 3 |
| 資本の出し手 | 容量の 90% 超はパートナー(開発事業者)が資金を負担(Magouyrk)。顧客持込・前払い・顧客が容量を借りる型もある。Oracle が先払いする型は最もキャッシュを要する | 90% 超(1 媒体の要約) | パートナーの賃料条件 | [W5-34][W5-05] | 3 |
| 賃借モデル | Oracle はデータセンターの大半を賃借し、自前建設は少ない | 未開始リース $288B(再掲 [既S4]) | リース期間中の解約条項 | [W5-34][既S4] | 3 |
| 資本コスト | 本調査では新規取得なし。Oracle の新発債スプレッド対ハイパースケーラーは [既R7] 2 章 | — | — | [既R7] | — |
| ネットワーク設計(Acceleron 等) | 本調査の検索では会社・報道の主張を取得できなかった(再掲 [既R3]) | — | 欠損 | — | — |
| 調達 | 本調査の検索では会社の調達優位(割当、価格)の主張を取得できなかった | — | 欠損 | — | — |

### 7-2. Abilene の着工から稼働までの月数

| 起点・到達点 | 日付 | 着工(2024-05-31)からの経過(算出) | 出典 | Tier |
|---|---|---|---|---|
| 北側 2 棟の整地開始 | 2024-05-31(Epoch AI) | 0 | [W5-30] | 3 |
| Building 1 が全面稼働(衛星画像による推定) | 2025-09-26 頃 | 483 日 = 約 15.9 か月 | [W5-30] | 3 |
| Crusoe が第 1 期を「稼働中」と発表(2 棟、98 万平方フィート、IT 電力 200MW 超、Oracle が OpenAI 向けに使用) | 2025-09-30 | 487 日 = 約 16.0 か月 | [W5-31] | 3 |
| Building 2 が全面稼働(衛星画像による推定) | 2025-12-24 頃 | 572 日 = 約 18.8 か月 | [W5-30] | 3 |
| IT 電力 421MW が稼働(再掲 [既R7]) | 2026-07 | 約 25 か月 | [既R7] | 3 |
| 全 8 棟(1.2GW)の完成 | 2026 年後半〜2027 年初め(再掲 [既R7]) | 約 31 か月以上 | [既R7] | 3 |

- Crusoe CEO は「100MW 以上のデータセンターとして最速の工程を狙った」と述べた(会社主張。独立比較ではない)。[W5-31]
- 食い違い: 「着工から 1 年以内に 2 棟が通電」とする出典と、上記の 15〜16 か月が合わない(§10)。
- 他拠点: Oracle は Bloomberg の「Stargate 一部拠点が 2027 年から 2028 年に延期」との報道を強く否定し、契約上必要な拠点に遅延はないと説明(2026 年)。[W5-37] 他拠点の遅れ(Project Jupiter、Shackelford 等)は再掲 [既R7] 3-2 節。

---

## 8. OpenAI 以外の大口顧客と受注残

### 8-1. 顧客別

| 顧客 | 契約額・規模 | 時点 | 備考 | 出典 | Tier |
|---|---|---|---|---|---|
| OpenAI | 約 $300B・約 5 年・2027 年開始(WSJ)。OpenAI は 4.5GW を確認、総額は非開示(再掲) | 2025-09 報道 | RPO に占める割合は S&P が「半分近く」、BofA が $638B の半分超(再掲) | [既S1][W5-39] | 3 |
| Meta | 約 $20B の複数年クラウド契約の商談(Bloomberg 発)。その後、Oracle が Meta との複数年契約を確認したとする媒体あり(CNBC 経由の 1 媒体) | 2025-09 | 学習とデプロイ向け。金額は非確認 | [W5-44] | 3 |
| Meta・SpaceX(xAI の親会社)・NVIDIA | RPO の貢献者として名前が挙がる(金額なし) | 2026-09 | Oracle は個別の契約額を公式に確認していない | [W5-38] | 3 |
| xAI・NVIDIA・AMD | Q1 FY26 の決算で「数十億ドル規模の契約」として言及(再掲 [既S1])。個別の金額は**欠損** | 2025-09 | Q1 FY26 は 4 件の数十億ドル契約・3 顧客と報道 | [W5-44][既S1] | 3 |
| 合計 | Oracle は約 30 日で $65B の新規 AI インフラ契約を獲得(2025 年) | 2025-09〜10 | 内訳は非開示 | [W5-13] | 3/4 |

### 8-2. 受注残(RPO)の伸びと OpenAI 以外

| 時点 | RPO | 前四半期差・前年差 | OpenAI 以外についての発言 | 出典 | Tier |
|---|---|---|---|---|---|
| Q4 FY26(2026-05-31) | $638B(10-K。前年は $138B。+363%) | 12% が 12 か月以内、34% が 13〜36 か月 | — | [W5-21][W5-42] | 1* |
| Q1 FY27(2026-08-31) | $664B(10-Q)。前年差 +$209B、前四半期差 +$26B | 約 13% が 12 か月以内。新規 AI 契約 $30B 超 | 経営陣は「OpenAI に帰属しない受注残が過去 1 年で 2 倍超」と説明(2 媒体の要約。書き起こし未確認、金額は非開示) | [W5-22][W5-38][W5-39] | 1*/3 |

- 「OpenAI 以外の受注残」の金額は**欠損**。「2 倍超」の起点と終点の金額が分からない。
- OpenAI の割合: S&P の格下げ時点で「半分近く」(再掲 [既R5])。Q1 FY27 時点の OpenAI 比率の会社開示は見つからなかった。

---

## 9. 推論(inference)と学習(training)

| 内容 | 時点 | 出典 | Tier |
|---|---|---|---|
| Ellison: 「AI 推論市場は学習市場よりはるかに大きい」(市場の予測。OCI の実績比ではない) | 2025-09(Q1 FY26 の決算) | [W5-45] | 3 |
| Catz: Oracle は AI 学習と推論の両方で選ばれるクラウド。Q3 FY25 の OCI 消費売上は AI 学習・GPU 需要で +57% | 2025-03 | 検索 #14 の要約(Marketbeat の Q3 FY25 書き起こし [W5-51] 等) | 3 |
| Oracle: 需要は AI 学習と推論の両方で供給を上回る(Q1 FY27 の報道要約。話者は特定されていない) | 2026-09 | 検索 #23 の要約(URL 特定不可) | 3 |
| FAM 資料: 区分はエンタープライズ/分散クラウド/AI インフラであり、推論と学習の区分はない | 2025-10 | [W5-08][W5-11] | 1*/3 |
| 推論と学習の比率、推論向けの単価・粗利率の会社発言 | — | **欠損** | — |

- 補足(再掲 [既S4]): Q3 FY26 の説明会で、周辺サービス(DB、ストレージ等)は AI データセンター支出の 10〜20% 程度を占めうると説明。AI Database の売上目標は FY30 に $20B(CreditSights 経由)。

---

## 10. 時系列表(四半期。AI・粗利率・利益率)

| 項目 | Q3 FY26(〜2026-02、発表 2026-03-10) | Q4 FY26(〜2026-05、発表 2026-06-10) | Q1 FY27(〜2026-08、発表 2026-09-10) |
|---|---|---|---|
| AI 容量の粗利率(会社) | **32%**(ガイダンス 30%) | 欠損(「劣化なし」の AI 要約のみ) | 欠損 |
| 全社粗利率の方向(会社) | 欠損(FY26 通期で約 5pt 低下) | FY26 通期 約 −5pt、「想定どおり」 | 低下(DC 立上げ、インフラ比率上昇) |
| 営業利益率 | 欠損 | 非 GAAP 営業利益 $8.6B(+22%)、営業利益率は小幅上昇 | 非 GAAP 42%(前年並み。算出 42.1%)、GAAP 35% |
| OCI 売上 | 欠損(AI インフラ売上 +243% 前年比) | $5.8B(+93%) | $7.4B(+121%) |
| RPO | $553B | $638B(+363%) | $664B(+$26B 前四半期比) |
| RPO の認識時期 | 欠損 | 12 か月以内 12%、13〜36 か月 34% | 12 か月以内 約 13% |
| 新規 AI 契約 | $29B 超(BYOH+前払い型) | $67B(大半が BYOH・前払い)、前払い・BYOH 累計 $75B | $30B 超。前払い(金融要素付き)$11.4B を受領 |
| GPU 更新 | 欠損 | 対象 35,000 GPU・59 顧客。顧客の 49% が GPU の 92% を更新 | 更新または再販で従来契約比 +20%、過半が 4 年以上前 |
| GPU 稼働率 | 欠損 | 97.5% | 97.9% |
| 納入量 | 欠損 | FY26 通期で約 1.2GW(finviz 要約。ラベル不正確の可能性、§11 #10) | 約 850MW、30 万基超の GPU |
| capex | 欠損 | FY26 通期 $55.6B(1 媒体) | Q1 約 $28.5B、FCF 約 −$5B、FY27 見通し $90〜95B(再掲) |
| 出典 | [W5-05] | [W5-21][W5-27][W5-42][W5-28] | [W5-02][W5-22][W5-38][W5-40][W5-43] |

- 注: DCD の見出し「直近の四半期に 400MW を稼働、今後 3 年で 10GW の電力を確保」[W5-35] は、どの四半期か特定できなかった(Q3 FY26 または Q4 FY26)。

---

## 11. 食い違い(どちらも採らず併記)

| # | 論点 | 出典 A | 出典 B | 備考 |
|---|---|---|---|---|
| 1 | 30〜40% の意味 | Reuters: 契約期間を通じ概ね一定(steady)、調整後粗利率 30〜40% [W5-09] | Computer Weekly: 契約期間中に OCI 粗利率が 30〜40% 上昇する見込み [W5-10] | 本文未確認。後者は水準を変化と誤読した可能性があるが、確認できない |
| 2 | 30〜40% の達成時期 | Reuters 要約: 「AI クラウド計算インフラの提供で」30〜40%(時期なし)。Sherwood: 「can reach 35%」 | 別の要約: 「2030 年までに」30〜40% | 時期の限定は 1 媒体のみ(検索 #15 の要約が Reuters の同一 URL に帰属させているが、他の要約には時期の記述がない) |
| 3 | 例示の粗利率 | Bloomberg: 35% | 算出: 60 − 6.4 × 6 = 21.6、21.6 ÷ 60 = 36.0% | 丸め、または原価に含まれる範囲の差。資料未照合 |
| 4 | The Information の 14% と 16% | 14%: 2025-06〜08 の四半期(売上 $9 億、粗利益 $1.25 億) | 16%: 5 四半期平均(DCD 見出し「AI クラウド案件の平均利益率 16%」)。DCD は「利益率」、他は「粗利率」と表記 | 期間の違い。定義(粗利/利益)の表記ゆれ |
| 5 | 14% と Sherwood の「約 $1 億の損失」 | 14%(粗利益プラス) | 一部サイズの小口レンタルで損失(Blackwell で約 $1 億の損失との報道、再掲 [既S1]) | 整合は未確認(再掲 [既S3]) |
| 6 | +20% の範囲 | 「更新または再販」の全量(Constellation 引用) | 「全容量が +20% で更新」(Crypto Briefing)、「過半は 4 年以上」と「全量」の表現差 | 更新のみの単価は不明 |
| 7 | +20% の第 2 出典 | 1 回目の検索: Betafinch の AI 生成要約にしか +20% が出ない | 再検索: Cryptobriefing、KuCoin、DCD、Longbridge 等が同一数値を報道 | 検索クエリの差。いずれも書き起こし未確認 |
| 8 | Abilene の稼働までの期間 | Epoch・Crusoe: 約 16 か月(2024-05/06 → 2025-09) | 別の出典: 「着工から 1 年以内に 2 棟が通電」 | 出典の言い回しが緩い |
| 9 | Goldman の全社粗利率 | Webull: FY25 約 72% → FY28 約 58% | 再検索では 58% を確認できず(約 35% の契約例のみ確認) | 単独の 4 相当の出典 |
| 10 | Q3 FY26 説明会の capex | finviz 要約: 「Q3 FY26 の説明会で FY26 の capex $55.6B、FY27 は $90〜95B」 | FY26 通期の確定値は Q4 FY26 後にしか出ない。FY27 の $90〜95B は Q1 FY27(再掲 [既S1]) | 要約の日付ラベルが不正確な可能性 |
| 11 | FY30 までの成長率 | 31%(5 年 CAGR、Reuters、CreditSights) | 35%(4 年 CAGR、UBS) | 期間の違い(年数が異なる) |
| 12 | 営業利益率の動き | 「42% で横ばい」(Futurum、ほか) | 「GAAP 営業利益率 +600bp で 35%」 | 非 GAAP と GAAP の基準差(再掲 [既S4]) |

---

## 12. 欠損と試した検索語

| # | 項目 | 結果 | 試した検索語(要旨) |
|---|---|---|---|
| 1 | Q4 FY26・Q1 FY27 の AI 粗利率の数値 | 欠損(Q4 は AI 要約の「劣化なし」のみ、Q1 は全社粗利率の低下説明のみ) | #1, #10, #11, #17 |
| 2 | 「初期は低く後期は高い」(契約初期と後期の粗利率の違い)の会社の定量説明 | 欠損。Reuters は「一定」 | #3, #4 |
| 3 | FY30 の全社営業利益率目標 | 欠損(FY30 売上 $225B・EPS $21・OCI $166B は確認) | #5, #26(extended) |
| 4 | OCI の長期営業利益率目標 | 欠損 | #4, #5, #26 |
| 5 | CFO・共同 CEO の「容量が成熟すると利益率が上がる」趣旨の逐語 | 要約のみ(§1-1 の #5、#9)。逐語は欠損 | #7, #10, #22 |
| 6 | 稼働前の賃料・電力・減価償却の会計処理の公式説明 | 欠損 | #7, #25 |
| 7 | take-or-pay、解約条項、価格改定条項 | 欠損 | #8, #21 |
| 8 | 収益認識(期間按分)、BYOH の売上計上範囲 | 欠損(RPO の認識時期のみ) | #8, #25 |
| 9 | +20% 更新の対象数量・顧客数・更新のみの単価、97.9% の定義 | 欠損 | #1, #19 |
| 10 | Jefferies、UBS、Barclays、Mizuho の AI インフラ年度別粗利率・営業利益率 | 欠損 | #9, #15, #18 |
| 11 | Morgan Stanley・Goldman・Guggenheim の年度別営業利益率 | 欠損 | #9, #18 |
| 12 | The Information の 2026 年の続報 | 欠損 | #6 |
| 13 | xAI・NVIDIA・AMD の契約額、OpenAI 以外の RPO の金額 | 欠損 | #13, #16, #24 |
| 14 | 推論と学習の比率、推論の単価・粗利率の会社発言 | 欠損 | #14, #23 |
| 15 | ネットワーク設計(Acceleron 等)、調達の優位の会社主張 | 欠損 | #20 |
| 16 | Oracle による建設速度の他社比較 | 欠損(Crusoe CEO の「最速を狙った」のみ) | #12, #20 |
| 17 | Q1 FY27 の「ROIC」「定常状態のプロジェクト収益率」の発言 | 検索では確認できず(再掲 [既S4] の「20% 台後半」は 1 社) | #11 |

---

## 13. 出典一覧

URL は検索結果に表示されたもの。個別の掲載日が表示されないものが多い。

### 会社の資料(検索要約経由、原本未開)

- [W5-08] Oracle「Financial Analyst Meeting 2025 — Magouyrk」資料 https://www.oracle.com/a/ocom/docs/corporate/financial-analyst-meeting-2025-magouyrk.pdf (2025-10-16) 1*(URL のみ確認、本文は未読)
- [W5-21] Oracle Form 10-K FY2026(RPO $638B、前年 $138B) https://www.sec.gov/Archives/edgar/data/0001341439/000119312526277521/orcl-20260531.htm (2026-05-31) 1*
- [W5-22] Oracle Form 10-Q(2026-08-31、無条件購入義務約 $34.15B、前払い $11.4B、RPO $664B・約 13%) https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm 1*
- [W5-41] Oracle Q1 FY27 決算発表 https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/ (2026-09-10) 1*
- [W5-42] Oracle Q4 FY26 決算発表 https://www.oracle.com/de/news/announcement/q4fy26-earnings-release-2026-06-10/ (2026-06-10) 1*(RPO の大半の増加は前払い・顧客提供 GPU、$75B)

### 決算説明会の書き起こし・要約(Tier 3〜4)

- [W5-01] Bullfincher Q1 FY27 https://bullfincher.io/companies/oracle-corporation/earnings-call/fy2027-q1 3
- [W5-02] The Cerbat Gem「Oracle Q1 Earnings Call Highlights」 https://www.thecerbatgem.com/?p=10389557 3
- [W5-03] Betafinch ORCL 2027 Q1(AI 生成要約) https://betafinch.com/episodes/ORCL_2027_Q1_en 4
- [W5-04] TradingKey Q1 FY27 書き起こし https://www.tradingkey.com/news/transcripts/262162053-tradingkey 3
- [W5-05] Insider Monkey Q3 FY26 書き起こし https://www.insidermonkey.com/blog/oracle-corporation-nyseorcl-q3-2026-earnings-call-transcript-1714572/ 3
- [W5-06] roic.ai Q3 FY26 書き起こし https://www.roic.ai/quote/ORCL/transcripts/2026-year/3-quarter 3
- [W5-07] ceointerviews.ai(Q3 FY26 の引用) https://ceointerviews.ai/quote/multicloud-database-revenue-grew-531-yearoveryear-ai-infrastructure-MTA1MzgwNg/ 4
- [W5-27] TIKR「Oracle Stock: Q4 2026 Beats Estimates as OCI Revenue Surges 93%」 https://www.tikr.com/blog/oracle-stock-q4-2026-beats-estimates-as-oci-revenue-surges-93-year-over-year 3
- [W5-28] Moomoo「Oracle Q4 FY2026 Earnings Conference Call」(AI 要約) https://www.moomoo.com/community/feed/oracle-q4-fy2026-earnings-conference-call-116727818420629 4
- [W5-29] ERP Today「Oracle Q4 2026 Earnings Call」 https://erp.today/oracle-q4-2026-earnings-ai-cloud-backlog-funding/ 3
- [W5-40] Futurum「Oracle Q1 FY 2027」 https://futurumgroup.com/insights/ai-platforms/oracle-q1-fy-2027-ai-infrastructure-contracts-convert-into-growth/ 3

### FAM(2025-10)と粗利率の報道

- [W5-09] Reuters(TradingView 転載)「Oracle expects cloud sales of $166 billion by 2030」 https://de.tradingview.com/news/reuters.com%2C2025%3Anewsml_L6N3VX11P%3A0-oracle-expects-cloud-sales-of-166-billion-by-2030-as-business-expands (2025-10-16) 3
- [W5-10] Computer Weekly「Oracle expects to increase OCI margins by 30-40%」 https://computerweekly.com/news/366636165/Oracle-expects-to-increase-OCI-margins-by-30-40 (2025-10) 3
- [W5-11] CreditSights「Oracle: Top 10 Takeaways from 2025 Analyst Meeting」 https://know.creditsights.com/insights/oracle-top-10-takeaways-from-2025-analyst-meeting/ (2025-10、冒頭のみ) 3
- [W5-12] Sherwood News https://www.sherwood.news/markets/oracle-jumps-as-it-says-ai-cloud-gross-margins-can-reach-35-predicts-usd166/ (2025-10) 3
- [W5-13] Tiger Brokers(Bloomberg 転載)「Oracle Anticipates 35% Gross Margin on AI Infrastructure」 https://www-web.itiger.com/news/1108942484 、同「Oracle Secures $65 Billion in Cloud Contracts Within a Month」 https://www-web.itiger.com/news/1188424182 3/4
- [W5-14] Motley Fool「Why Oracle Fell Hard Today」 https://www.fool.com/investing/2025/10/17/why-oracle-fell-hard-today/ (2025-10-17) 3
- [W5-15] Fortune「Oracle declines on concerns about fulfilling AI cloud demand」 https://www.fortune.com/2025/10/17/oracle-declines-on-concerns-about-fulfilling-ai-cloud-demand (2025-10-17) 3
- [W5-46] Tikr / Webull の FAM 要約 https://www.tikr.com/blog/nyse-oracle-stock-falls-over-2-despite-strong-long-term-outlook 3
- [W5-47] TipRanks「Oracle stock is winning the AI narrative but investors want proof not prophecy」 https://www.tipranks.com/news/oracle-stock-is-winning-the-ai-narrative-but-investors-want-proof-not-prophecy 3(共同 CEO が全契約期間 35% と説明、報道の 14% は初期の数値、との記述)
- [W5-51] Marketbeat「Oracle Q3 2025 Earnings Call Transcript」 https://www.marketbeat.com/earnings/reports/2025-3-10-oracle-co-stock (2025-03-10) 3
- [W5-52] Boldstart Fast Forward「Oracle's bright cloud future hinges on fulfilling massive AI deals」 https://fastforward.boldstart.vc/?p=801 4(契約に最低利用・再交渉ゲートなどの偶発条件があるとの記述)

### 第三者の粗利率推計

- [W5-16] The Information「Oracle Assures Investors on AI Cloud Margins, Struggles to Profit From Older Nvidia Chips」 https://feature.theinformation.com/articles/oracle-assures-investors-ai-cloud-margins-struggles-profit-older-nvidia-chips (有料、見出しのみ) 3
- [W5-17] Sherbrooke Record(MarketMinute)「Oracle's AI Cloud Margins Squeezed by Nvidia Chips」 https://business.sherbrookerecord.com/sherbrookerecord/article/marketminute-2025-10-7-oracles-ai-cloud-margins-squeezed-by-nvidia-chips-sparking-investor-jitters (2025-10-07) 4
- [W5-18] DCD「Internal documents show Oracle's average profit margin for AI cloud deals was 16%」 https://www.datacenterdynamics.com/en/news/internal-documents-show-oracles-average-profit-margin-for-ai-cloud-deals-was-16-report/ (2025-10) 3
- [W5-19] Seeking Alpha「Oracle's documents show financial challenges of renting out Nvidia's chips」 https://seekingalpha.com/news/4502414-oracles-documents-show-financial-challenges-of-renting-out-nvidias-chips (2025-10) 3
- [W5-20] Trefis「Oracle Stock Fell While Its Operating Margin Climbed For A Third Straight Year」 https://www.trefis.com/articles/610606/oracle-stock-fell-while-its-operating-margin-climbed-for-a-third-straight-year/2026-08-07 (2026-08-07) 3
- [W5-23] Longport「A Detailed Explanation of Oracle's Growth Model」(Morgan Stanley、KeyBanc) https://longportapp.cn/news/258646940 3
- [W5-24] Webull(Goldman の全社粗利率) https://www.webull.com/news/13713627679100928 、 https://www.webull.com/news/15575360941851648 3/4
- [W5-25] Finviz「Oracle Stock (ORCL): Analysts Say It's Officially the Fourth Hyperscaler」(EVR-ISI) https://finviz.com/news/104884/oracle-stock-orcl-analysts-say-its-officially-the-fourth-hyperscaler 3
- [W5-49] CreditSights FAQ・予想 https://know.creditsights.com/insights/oracle-top-20-client-faqs/ 、 https://know.creditsights.com/insights/oracle-april-2026-forecasts-upgrade-to-o-p/ 3
- [W5-50] StreetInsider「UBS says Oracle undervalued at 15x FY30 EPS」 https://www.streetinsider.com/Investing/UBS+says+Oracle+undervalued+at+15x+FY30+EPS+given+long-term+cloud+growth/25469459.html (2025-10) 3

### 建設速度・競争優位

- [W5-30] Epoch AI「OpenAI Stargate Abilene」 https://epoch.ai/data/ai-data-centers/directory/openai-stargate-abilene (2026-07-15 更新) 3
- [W5-31] DCD「Crusoe's Abilene data center officially live」 https://datacenterdynamics.com/en/news/crusoes-abilene-data-center-officially-live-serving-oracle-and-openais-stargate (2025-09-30) 3
- [W5-32] Finviz「Oracle co-CEO Clay Magouyrk explains what's holding back the company's data center windfall」 https://finviz.com/news/336098/oracle-co-ceo-clay-magouyrk-explains-whats-holding-back-the-companys-data-center-windfall-the-major-factor-limiting-even-stronger-profits-is (2026-03) 3
- [W5-33] AOL「Oracle tells investors not to worry about data center spending because it's 'very, very good' at cost-cutting」 https://www.aol.com/articles/oracle-tells-investors-not-worry-235112946.html (2026-03) 3
- [W5-34] LetsDataScience「Oracle Promises Lower Data Center Costs」 https://letsdatascience.com/news/oracle-promises-lower-data-center-costs-76fd8824 3/4
- [W5-35] DCD「Oracle stood up 400MW of data center capacity in latest quarter, has secured 10GW of power for the next three years」 https://datacenterdynamics.com/en/news/oracle-stood-up-400mw-of-data-center-capacity-in-latest-quarter-has-secured-10gw-of-power-for-the-next-three-years/ 3
- [W5-36] DCD「Oracle Cloud Infrastructure revenue up 93% as firm's capex keeps climbing」 https://www.datacenterdynamics.com/en/news/oracle-cloud-infrastructure-revenue-up-93-as-firms-capex-keeps-climbing/ 3
- [W5-37] Techstrong「Oracle denies delays in OpenAI data center construction」 https://techstrong.ai/articles/oracle-denies-delays-in-openai-data-center-construction/ 3

### 更新・稼働率・顧客

- [W5-43] Crypto Briefing https://cryptobriefing.com/oracle-ai-contracts-renew-higher-rates/ 、KuCoin https://kucoin.com/news/flash/oracle-renews-ai-gpu-contracts-at-20-higher-rates-amid-surging-demand 、Longbridge https://longbridge.com/news/298820115 、Remio https://www.remio.ai/post/oracle-gpu-utilization-hit-97-9-strengthening-nvidias-shortage-signal 、DCD「Oracle delivered 300,000 GPUs in Q1 FY2027」 https://www.datacenterdynamics.com/en/news/oracle-delivered-300000-gpus-in-q1-fy2027/ (2026-09) 3/4
- [W5-38] 24/7 Wall St「Oracle Weakens Bear Case With Broader AI Customer Base and $664 Billion Backlog」 https://247wallst.com/investing/2026/09/11/oracle-weakens-bear-case-with-broader-ai-customer-base-and-664-billion-backlog/ (2026-09-11) 3
- [W5-39] ai2.work「Oracle's AI Cloud Backlog Hits $664B」 https://ai2.work/blog/oracle-s-ai-cloud-backlog-hits-664b-as-oci-revenue-more-than-doubles 4
- [W5-44] DCD「Meta in talks to sign $20bn Oracle cloud deal」 https://www.datacenterdynamics.com/en/news/meta-in-talks-to-sign-20bn-oracle-cloud-deal-report/ (2025-09) 3。Nasdaq/Zacks https://www.nasdaq.com/articles/can-oracles-expanding-contract-pipeline-drive-its-next-growth-phase 3
- [W5-45] CRN Asia「Oracle Q1 earnings: Ellison says AI inferencing fuels company's monster pipeline」 https://www.crnasia.com/news-network/2025/oracle-q1-earnings-ellison-says-ai-inferencing-fuels-company (2025-09) 3
- 既存調査: [既S1] [既S3] [既S4] [既R5] [既R7](パスは冒頭に記載)

## 14. 検索ログ(26 回 / 上限 26 回。#26 のみ extended、他は standard)

| # | 検索語(要旨) | 主な収穫 |
|---|---|---|
| 1 | Oracle Q1 fiscal 2027 earnings call transcript Magouyrk Maxson gross margin AI infrastructure renewed 20% premium utilization 97.9% | 97.9%、850MW、30 万 GPU。+20% は AI 要約のみ |
| 2 | Oracle Q3 fiscal 2026 earnings call transcript gross margin 32% … | 32%・ガイダンス 30%、$29B、$30B 調達 |
| 3 | Oracle analyst meeting October 2025 OCI gross margin 30% to 40% over contract life six year $60 billion 35% … | 30〜40%、一定、$6.4B/年、Computer Weekly の食い違い |
| 4 | Oracle financial analyst meeting 2025 Magouyrk slides … $6.4 billion cost each year … | Bloomberg 35%、Magouyrk「最大級の顧客に当てはまる」 |
| 5 | Oracle FY2030 targets $225 billion revenue $21 EPS operating margin … | 営業利益率目標は見つからず |
| 6 | The Information Oracle Nvidia chip rental gross margin 14% follow-up 2026 … | 14%・16%・7pt。2026 年続報なし |
| 7 | Oracle Maxson gross margin decline data centers ramp "before revenue" lease costs … | Guggenheim 約 25%、DCD、Trefis |
| 8 | Oracle 10-K fiscal 2026 RPO OCI contracts termination cancellation take-or-pay … | RPO $638B、$75B。契約条件の記載なし |
| 9 | Morgan Stanley Oracle OCI gross margin estimate fiscal 2027 2028 … | MS 約 40%、Singh、Goldman 約 35%、KeyBanc 42.4% |
| 10 | Oracle Q4 fiscal 2026 earnings call June 2026 Maxson gross margin FY27 … | FY26 約 −5pt、$8.6B、RPO の認識時期 |
| 11 | Oracle Q1 FY27 Maxson ROIC project-level steady state … | 確認できず |
| 12 | Oracle Abilene groundbreaking to first building operational months … | 2024-05-31 → 2025-09-26/30 |
| 13 | Oracle RPO excluding OpenAI non-OpenAI backlog Meta xAI NVIDIA AMD … | 非 OpenAI 2 倍超、OpenAI 比率 |
| 14 | Oracle OCI inference vs training mix Magouyrk … | 比率の開示なし、$67B・BYOH |
| 15 | Jefferies OR UBS OR Barclays OR Mizuho OR Guggenheim Oracle AI infrastructure gross margin forecast … | EVR-ISI FY29、Goldman 58% |
| 16 | Oracle Q1 FY27 backlog not attributable to OpenAI more than doubled … | 2 倍超(2 媒体)、$30B 超 |
| 17 | Oracle Q1 FY27 earnings slides "contract margin" … | 確認できず |
| 18 | Goldman Sachs Oracle gross margin 58% FY2028 … | 58% は再確認できず、35% の分解 |
| 19 | Oracle "renewed or resold" 20% premium … four years or older … | 複数媒体で +20% を確認 |
| 20 | Magouyrk Oracle competitive advantage AI data centers build faster … Acceleron … | 建設短縮、原価低減、90% 超パートナー資金 |
| 21 | Oracle OpenAI contract terms minimum commitment take-or-pay termination … | 無条件購入義務 $34.15B。契約条件は不明 |
| 22 | Oracle co-CEO Magouyrk explains what's holding back data center windfall … | 同時建設で費用が先行 |
| 23 | Oracle Ellison inferencing larger than training … | Ellison の市場予測 |
| 24 | Oracle Meta $20 billion cloud contract xAI SpaceX NVIDIA AMD … | Meta 約 $20B(商談)、他は金額なし |
| 25 | Oracle 10-Q August 31 2026 customer prepayments significant financing component … | $11.4B、判断要素、便法 |
| 26 | CreditSights Oracle top 10 takeaways 2025 analyst meeting FY30 operating margin … (extended) | FY30 営業利益率は見つからず、capex 予想 |
