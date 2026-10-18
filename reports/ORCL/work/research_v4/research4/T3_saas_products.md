# T3: Oracle アプリ(SaaS)の製品特性と今後の成長の要因(利用者の見方「SaaS の需要は後半にかけて大きくなる」の根拠と反証)

- 作成日: 2026-10-15 / 対象: Oracle(NYSE: ORCL、決算期末 5 月末。FY27 = 2026-06〜2027-05)
- 範囲: 事実・数値・出典の整理のみ。投資判断・推奨・評価は書かない。
- 取得手段: WebSearch のみ。24 回 / 上限 24 回を使い切った(standard 20 回、extended 4 回)。WebFetch は使えない。
- **原本(Oracle の決算説明会の書き起こし、決算発表の全文、10-Q、各社のプレスリリース全文、Gartner の報告書本文)は 1 件も直接開いていない。数値はすべて検索ツールの要約に書かれていた内容。** そのため会社開示由来でも Tier に `*` を付ける。検索要約は複数サイトを統合しており、個々の数値がどの URL 由来かを特定できない場合がある。
- Tier: 1=会社開示, 2=公的統計, 3=報道・アナリスト・データ会社, 4=ブログ・SNS。`*`=検索要約経由。「(算出)」は調査者の計算(式を併記)。「欠損」は見つからなかったもの(試した検索語は 7 節)。
- 出典 ID `[T3-nn]` は「nn 番目の検索」(8 節に URL)。`[R2]` `[H1]` `[T4]` `[S1]` などは /tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/ の既存調査(再掲のみ)。
- 会計年度: Oracle の FY26 = 2025-06〜2026-05。Q1 FY27 = 2026-06〜08(決算発表 2026-09-10)。他社は各社の呼称どおり(Workday FY27 Q2 = 2026-05〜07、Salesforce FY27 Q2 = 2026-05〜07)。

---

## 0. 要約(事実のみ、10 行)

1. **SaaS 全体の成長は直近 5 四半期で 10〜13% の範囲**: Q1 FY26 $3.8B(+11%)、Q2 $3.9B(+11%)、Q3 $4.0B(+13%)、Q4 $4.1B(+10%、定率 +9%)、Q1 FY27 $4.2B(+10%、定率 +10%)。FY26 通期 $15.9B(+11%)。四半期売上は毎期 約 $0.1B ずつ増えている(算出)。Q1 FY27 時点で加速は数値に現れていない。(1*)
2. **ERP 系の伸びは鈍化方向**: Fusion ERP は +22%(Q4 FY25)→ +17% → +18% → +17%(Q3 FY26)。NetSuite は +18% → +16% → +13% → +14%(Q3 FY26)。Q4 FY26 のスライドの文字列(文字化けあり)では Fusion Back-Office $1.5B +12%、NetSuite $1.1B +9%。Q1 FY27 は Fusion ERP・NetSuite の公式値が欠損。Q1 FY27 の説明会要約は「Fusion と業種別アプリは 10% を大きく上回る」(未確認)。(1*, 3*)
3. **先行指標(支持側)**: Q4 FY26 の SaaS 繰延収益は +16%(説明会の要約、売上 +10% を上回る)。ただし 1 件の要約のみで第二の確認なし。アプリ別の RPO・受注は欠損。(3*)
4. **AI エージェント**: AI Agent Studio(2025-03-20 発表)は追加費用なしと会社が説明。AI World 2025-10 時点で組込みエージェント・アシスタント 600 超(Fusion 400、業種別 200)。Fusion Agentic Applications は 2026-03-24(CX 版は 2026-04-09)に発表。供給網エージェントは「既存顧客に追加費用なし」(2026-02-10)。**「本番稼働 2,300 超」は 2 回の検索で出典なし(欠損)**。一方、第三者(Redress Compliance、Tier 4)は Fusion の AI をプール方式の従量(1 単位 1 セント)と記述し、食い違う。(1*, 4*)
5. **AI Data Platform(Enterprise Ontology)と新 EHR(Agentic)の顧客・稼働時期は欠損**。Oracle Health の売上推移も欠損。VA の EHR 導入は 2026-04 に再開(Michigan 4 拠点、2026-06-07 に Ohio・Kentucky 4 拠点、2026-08 に Indiana 3 拠点予定、Cleveland・Anchorage は 2026-10 予定)。(3*)
6. **FAM(2025-10-16)の目標**: FY30 の総売上 $225B・OCI $166B・EPS $21。OCI は総売上の約 74%、OCI 以外は $59B(算出: 225 − 166、74% = 166 ÷ 225)。**アプリ売上の FY30 目標は欠損**。経営陣の「アプリの成長が加速する」旨の逐語発言も見つからなかった。経営陣発言で拾えたのは「$4.1B の四半期で 2 桁成長はアプリとして悪くない」趣旨(Q4 FY26、要約)。(1*, 3*)
7. **オンプレ → Fusion の移行**: Software 売上は Q4 FY26 $6.8B(−2%、会社は「顧客のクラウド移行」と説明)、Q1 FY27 $5.55B(−3%)。旧来 ERP の顧客 8,500 社のうち Fusion ERP へ移行済みは約 1,000 社との CEO 発言(時点不明、出典の特定が未確認)。**移行後に顧客あたり売上が何倍になるかは欠損**(コンサル系ブログの「実装費 3〜5 倍」は出典不明で不採用)。(1*, 3*, 4*)
8. **比較(2026 年の最新四半期)**: SAP 2026 Q2 は現在のクラウド受注残 €22.9B(+27%)、クラウド売上 +22%(定率 +24%)、Cloud ERP Suite +25%。Workday 2026-07 期は購読売上 +13.9%、ServiceNow 2026 Q2 は購読売上 +24.5%・cRPO +21%、Salesforce 2026-07 期は売上 +11%・cRPO +14%(定率)。Oracle SaaS +10% は SAP・ServiceNow・Workday より低く、Salesforce(+11%)とほぼ同水準(数値の並置、定義の違いあり)。(1*)
9. **エージェント型 AI のソフトウェア支出予測**: Gartner(2026-02-17、抄録のみ)は 2030 年に $985B、2025〜2030 年の年平均成長率 62.7%。Gartner の供給網ソフト(エージェント AI 付き)は 2025 年 $2B 未満 → 2030 年 $53B。IDC の予測は欠損。ブログ記載の「2026 年 $201.9B」は Gartner 抄録の成長率からの逆算(約 $141B)と合わず未解決。(1*, 3*)
10. **反証側**: 2026-02 初めの「SaaSpocalypse」(AI エージェントが席課金を侵食するとの懸念)で software 株が急落した旨の報道。Oracle Fusion への影響を分析した独立した調査は見つからなかった(欠損)。Oracle の HCM は従業員数、ERP はユーザー数に連動する課金(既存調査 [R2]、Tier 4)。(3*, 4*)

---

## 1. 四半期別の成長率(直近 8 四半期: Q2 FY25〜Q1 FY27)

### 1-1. Cloud Applications(SaaS)全体と Fusion ERP・NetSuite

数値は Oracle の決算発表(検索要約経由)。単位は US$B。YoY は USD ベース。括弧内は定率(cc)で、記載があったものだけ。

| 四半期(期末 / 発表日) | SaaS 売上 | SaaS YoY | Fusion Cloud ERP | NetSuite Cloud ERP | 出典 | Tier |
|---|---|---|---|---|---|---|
| Q2 FY25(2024-11 / 2024-12) | 欠損 | 欠損 | 欠損 | 欠損 | 試行: T3-22 | - |
| Q3 FY25(2025-02 / 2025-03-10) | 欠損(単独値は見つからず) | 欠損 | $0.9B、+16%(cc +18%) | $0.9B、+16%(cc +17%) | [T3-22] | 1* |
| Q4 FY25(2025-05 / 2025-06-11) | $3.7B | +12% | $1.0B、+22% | $1.0B、+18% | [T3-22] | 1* |
| Q1 FY26(2025-08 / 2025-09-09) | $3.8B | +11% | $1.0B、+17%(cc +16%) | $1.0B、+16%(cc +15%) | [T3-01] | 1* |
| Q2 FY26(2025-11 / 2025-12-10) | $3.9B | +11%(cc +11%) | $1.1B、+18% | $1.0B、+13% | [T3-06] | 1* |
| Q3 FY26(2026-02 / 2026-03-10) | $4.0B | +13% | $1.1B、+17%(cc +14%) | $1.1B、+14%(cc +11%) | [T3-02] | 1* |
| Q4 FY26(2026-05 / 2026-06-10) | $4.1B | +10%(cc +9%) | 区分変更の可能性あり。スライド文字列: 「Fusion Back-Office」$1.5B、+12% | $1.1B、+9%(スライド文字列) | [T3-03][T3-05][T3-24] | 1*(Q4 スライドは文字化け) |
| Q1 FY27(2026-08 / 2026-09-10) | $4.2B | +10%(cc +10%) | 欠損(説明会要約「Fusion +14%」は既存調査 [R2] の再掲、未確認) | 欠損(「意思決定サイクルが長く、他の SaaS より成長が鈍い」との言及のみ) | [T3-04][T3-07] | 1*, 3* |

- FY26 通期の SaaS は $15.9B(+11% USD、+10% cc)(Oracle Q4 FY26 発表、2026-06-10)。[T3-03] 1*
- 為替の影響(算出): Q3 FY26 の Fusion ERP は USD +17% に対し cc +14%(差 3pt)、NetSuite は USD +14% に対し cc +11%(差 3pt)。Q4 FY26 の SaaS は USD +10% に対し cc +9%(差 1pt)。Q1 FY27 は USD・cc とも +10%。
- 四半期売上の積み上がり(算出): $3.8B → $3.9B → $4.0B → $4.1B → $4.2B(Q1 FY26〜Q1 FY27)。毎期 約 +$0.1B。FY26 の 4 四半期合計は 3.8 + 3.9 + 4.0 + 4.1 = $15.8B(丸めのため通期 $15.9B と 0.1 差)。
- Q4 FY26 のスライドの数字から(算出): SaaS $4.1B − Fusion Back-Office $1.5B − NetSuite $1.1B = $1.5B が、それ以外(業種別アプリ、CX、Oracle Health など。内訳の定義は欠損)。丸め誤差 ±0.15B 程度。
- 備考: 既存調査 [H1] は Q1 FY27 の Fusion ERP を $1.1B(+17%)、NetSuite を $1.1B(+14%)としていたが、本調査で Q3 FY26 の値と一致することが分かった(第 6 節の食い違い参照)。Q4 FY26 の発表要約(T3-03)には ERP 別の行が見当たらなかった(検索要約の見落としの可能性あり)。

### 1-2. Fusion HCM・SCM・CX、業種別アプリ、Oracle Health、アプリの RPO・受注

| 項目 | 取れた値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Fusion HCM・SCM・CX の個別売上・成長率 | 欠損(Oracle の最近の決算発表の要約には ERP 2 行のみ。Q4 FY26 は「Fusion Back-Office」の 1 行) | - | T3-02, T3-03, T3-05 | - |
| 業種別アプリの成長率 | 「業種別アプリ +20% 超」(Q1 FY27 説明会の要約、既存調査 [R2] の再掲)。本調査では確認できず。Q1 FY27 説明会の別の要約は「Fusion と業種別アプリは 10% を大きく上回る」 | 2026-09-10 | [R2]、T3-07 | 3* |
| Oracle Health の売上・成長率 | 欠損(Q1 FY27・Q4 FY26 とも要約に値なし) | - | T3-07, T3-12 | - |
| 業種別アプリと Fusion の相互牽引 | Sicilia「業種別アプリが Fusion を牽引する、または逆の案件が増えている」(Q2 FY26、2025-12-10、要約)。既存調査 [S1] の再掲 | 2025-12-10 | [S1] | 1* |
| SaaS 繰延収益 | Q4 FY26 は前年比 +16%(説明会の要約。売上 +10% を上回る) | 2026-05 末 | T3-05(Yahoo / Investing.com の書き起こし要約) | 1* |
| 同上の第二の確認 | 取れず(Q4 FY26 の発表・説明会ハイライトの検索 T3-24 では 16% の記載が出なかった) | - | T3-24 | - |
| Fusion の本番稼働(go-live)数 | Q4 FY26 に「Fusion だけで 300 超の顧客が稼働開始」(要約は文面が崩れている) | 2026-05 期 | T3-05 | 1* |
| アプリ別の RPO・受注の伸び | 欠損。会社が開示する RPO は全社合計のみ | - | - | - |
| 全社 RPO(再掲) | $455B(2025-08 末)→ $523B(2025-11 末、+438%)→ $553B(2026-02 末)→ $638B(2026-05 末、+363%)→ $664B(2026-08 末、前年差 +$209B)。大半は OCI | 各四半期末 | T3-01, T3-05, T3-06, T3-23。[H1] | 1* |

---

## 2. AI エージェント(Fusion への組込み、課金、AI Data Platform、Oracle Health の新 EHR、経営陣発言、FAM)

### 2-1. エージェントの発表・課金・稼働の時系列

| 日付 | 事実 | 出典 | Tier |
|---|---|---|---|
| 2025-03-20 | Oracle AI Agent Studio for Fusion Applications を発表。Fusion に組込みのエージェント 50 超。追加費用なしと説明。テスト・検証・セキュリティ機能、複数の LLM を選べる | T3-08(Oracle 発表、CXToday、erp.today) | 1* |
| 2025(日付は未確認。AI World の基調講演の報道) | AI World の基調講演の報道: 組込みの AI エージェント・アシスタントは 600 超(Fusion 400、業種別 200)。顧客として Milwaukee Tool、BHE Energy が展開中。Fusion の役割別アクセス制御がエージェントにも適用、顧客データは LLM の学習に使わない | T3-10(Oracle ブログ) | 1* |
| 2026-02-10 | AI World(ムンバイ)で供給網のエージェントを発表。Oracle AI Agent Studio で構築、OCI 上で稼働、既存顧客に追加費用なし | T3-11 | 1* |
| 2026-03-24 | AI World(ロンドン)で Fusion Agentic Applications を発表。専門エージェントの協調チームで業務プロセス内の判断・実行を行う。「copilot や AI アドオンと違い、取引システムに組込み」と説明 | T3-11 | 1* |
| 2026-04-09 | AI World Tour(ニューヨーク)で CX 向け Fusion Agentic Applications を発表(営業・サービス・マーケティング) | T3-11 | 1* |
| 2026-05 期(Q4 FY26) | Fusion の go-live が 300 超(要約、文面崩れ) | T3-05 | 1* |
| 2026-09-10(Q1 FY27 説明会の要約) | 「NetSuite Next」を 10,000 顧客が AI コネクタ経由で採用(別の要約、未確認)。Sicilia: AI 支援でヘルスケアのアプリの go-live が「2 桁月」から「1 桁月」へ。NetSuite は「2 桁月」から「1 桁週」へ(別の検索 T3-14 の要約)。AI 組込み・顧客作成エージェント・AI 支援の導入がアプリ成長を支える旨の要約(AI 要約、逐語未確認) | T3-07, T3-09, T3-14 | 3* |
| 「本番稼働 2,300 超」 | **欠損**(2 回検索: T3-08 は「50 超」のみ、T3-10 は「600 超」のみ。2,300 の出典は見つからず) | T3-08, T3-10 | - |

### 2-2. 課金方式(追加料金の有無)

| 内容 | 出典 | Tier |
|---|---|---|
| Agent Studio は追加費用なし(2025-03 の発表)。供給網エージェントは既存顧客に追加費用なし(2026-02) | T3-08, T3-11 | 1* |
| Fusion の AI は「席」ではなく「メーター」: プールされた単位残高から、質問応答や文書生成などの動作ごとに 1 単位 1 セントで消費する従量制、AI 用のユーザー席は設けない、との記述(Redress Compliance の解説記事) | T3-21 | 4* |
| Fusion Agentic Applications(2026-03〜04)の価格・課金方式 | 欠損(発表の要約に価格の記載なし) | T3-11 |
| 追加費用なしと従量制の食い違い | 第 6 節の食い違い 4 | - |

### 2-3. AI Data Platform(Enterprise Ontology)・Oracle Health の新 EHR

| 項目 | 取れた事実 | 出典 | Tier |
|---|---|---|---|
| AI Data Platform、Enterprise Ontology | **欠損**(T3-11 と T3-23 の検索語に含めたが、要約に言及なし) | T3-11, T3-23 | - |
| Oracle Health の新 EHR(Agentic)の顧客・稼働時期 | **欠損**。要約に出たのは VA の導入再開のみ(VA が新 EHR かは未確認) | T3-12 | - |
| VA の EHR 導入の再開 | 3 年の中断(2023〜)の後、2026-04 に Michigan 4 拠点。2026-06-07 に Cincinnati・Chillicothe・Dayton・Fort Thomas の 4 拠点。Indiana 3 拠点(Fort Wayne、Marion、Roudebush)は 2026-08 予定。Cleveland・Anchorage は 2026-10 予定(以前の報道)。2026 年に 13 の VA 医療センターが稼働予定(Becker's の見出し)。残り 145 拠点は 2031 年までに到達予定(1 件の報道)。現在の VA との契約は 2028-05 に満了(1 件の報道)。2018-05 に $10B で締結 | T3-12(Becker's Hospital Review) | 3* |
| Oracle Health の売上推移 | 欠損。既存調査 [S1] は「Oracle Health の個別数値は未確認」 | T3-12 | - |
| Oracle Health の導入期間の短縮 | Sicilia「ヘルスケアの go-live が 2 桁月から 1 桁月へ」(Q1 FY27 説明会の要約) | T3-07, T3-14 | 3* |

### 2-4. 経営陣の「アプリの成長が加速する」趣旨の発言と FAM の目標

| 発言・目標 | 日時・場面 | 出典 | Tier |
|---|---|---|---|
| 「$4.1B の四半期で 2 桁成長はアプリとして悪くない」趣旨(Sicilia、要約) | Q4 FY26、2026-06-10 | T3-05(erp.today) | 3* |
| 「クラウドアプリは +10%、Fusion と業種別アプリはそれを大きく上回る」(説明会の要約) | Q1 FY27、2026-09-10 | T3-07 | 3* |
| 「総クラウド(アプリ + インフラ)の成長率は FY25 の 24% から FY26 に 40% 超へ」(CEO 発言、Q4 FY25 発表)。FY26 の実績は総クラウド $34.0B、+39%(算出ではなく Oracle 発表の値) | 2025-06-11 / 2026-06-10 | T3-22, T3-03 | 1* |
| 2024 年のアナリスト説明会のメモに「市場での地位により、持続的な low-to-mid teens の SaaS 成長を見通せる」との記載(古い見通し、出典の特定は未確認) | 2024 | T3-14 | 3* |
| 「アプリの成長が加速する」旨の明示的な発言 | **欠損**(試した検索語は 7 節) | - | - |
| FAM(2025-10-16)の FY30 目標: 総売上 $225B、OCI $166B(総売上の約 75% と報じられた)、EPS $21 | 2025-10-16 | T3-13(Reuters 配信、CreditSights) | 3* |
| 同上の内訳(算出) | OCI 以外 = 225 − 166 = $59B。OCI の割合 = 166 ÷ 225 = 約 74% | (算出) | - |
| 同 FAM のアプリ(SaaS)の売上目標 | **欠損**(CreditSights の要約は「アプリのスイートが競争力を支える」とのみ、数値なし。Kehring の資料は検索で入口(セーフハーバー部分)しか出ず) | T3-13, T3-14 | - |
| FAM: AI Database 売上は FY30 で約 $20B(CreditSights の要約) | 2025-10-20 付のメモ | T3-13 | 3* |
| 参考の算出(目標ではない): FY26 SaaS $15.9B が年 10% で 4 年伸びると FY30 = 15.9 × 1.10^4 = 約 $23.3B。年 12% なら約 $25.0B、年 15% なら約 $27.8B | (算出、仮定による) | - | - |
| Larry Ellison の「ERP 売上は $30B に届き得る」(Cloud Wars の見出しのみ。本文・日付は未確認) | 日付不明 | T3-02 | 3* |
| FY27 ガイダンス: 総売上 $90B 以上(+34% 超)、非 GAAP EPS $8.10、設備投資 $90〜95B。Q2 FY27 の総クラウド売上は定率 +64〜70%。**SaaS 単独のガイダンスは欠損** | 2026-09-10 | T3-04, T3-23 | 1*, 3* |

---

## 3. オンプレの業務アプリ(E-Business Suite・PeopleSoft・JD Edwards)から Fusion への移行

| 項目 | 取れた事実 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| 移行元の顧客規模 | CEO が決算説明会で「旧来 ERP(EBS・JD Edwards・PeopleSoft)の購入顧客は 8,500 社、Fusion ERP へ移行済みは約 1,000 社、残り 7,500 社が有力な見込み客」と発言したとの記述。**発言者・時点は検索要約から特定できず**(同じ検索結果に diginomica 2018-06-07 の記事があるが、引用元かは未確認) | 不明(古い可能性) | T3-15 | 3*(時点不明) |
| 旧来アプリの保守料 | ライセンス価格の約 22%/年(複数のコンサル系サイトの記述) | 2025〜2026 | T3-15(Redress Compliance、Oracle Licensing Experts) | 4* |
| 保守の期限(Oracle の公表日とされるもの) | EBS は 2034 年まで、PeopleSoft は 2034 年まで、JD Edwards EnterpriseOne は 2033 年まで | 2026 | T3-15 | 3*, 4* |
| 移行を反映するとされる Software 売上の減少 | Q4 FY26 の Software 売上は $6.8B、−2%。Oracle は「顧客がオンプレソフトからクラウドへ移行しているため」と説明 | 2026-06-10 | T3-03 | 1*, 3*(Verdict) |
| 同 Q1 FY27 | Software 売上 $5.55B、−3% | 2026-09-10 | T3-04(Verdict) | 3* |
| FY26 の Software 売上 | $24,541M で小幅減(第三者の分析。定義は未確認) | FY26 | T3-14 | 3* |
| 移行で顧客あたり売上が何倍になるか | **欠損**。要約では「Fusion のサブスクは 1 ユーザーあたりの単価が大幅に高い」とのコンサル系の主張のみで数値なし。「実装費が 3〜5 倍」「費用超過 40〜60%」はコンサル系で出典不明のため不採用 | - | T3-15 | 4* |
| 価格の目安(再掲) | HCM は定価 $54〜100/人月(実勢 $22〜50)、ERP は定価 $625/ユーザー月(別資料 $175〜625)。いずれも助言会社のブログ | 2024〜2026 | [R2](既存調査) | 4 |
| AI による導入期間の短縮 | NetSuite の go-live が 2 桁月から 1 桁週へ、ヘルスケアが 2 桁月から 1 桁月へ(Sicilia、要約) | 2026-09〜 | T3-07, T3-14 | 3* |

---

## 4. 比較: SAP・Workday・ServiceNow・Salesforce(2026 年の最新四半期)

| 会社(最新四半期、発表日) | 売上・成長率 | 受注残・先行指標 | AI の材料 | 出典 | Tier |
|---|---|---|---|---|---|
| **Oracle**(Q1 FY27、2026-09-10) | SaaS $4.2B、+10%(cc +10%)。総売上 $19.3B、+30% | RPO $664B(全社)。SaaS 繰延収益 +16%(Q4 FY26) | Agent Studio・Agentic Apps(発表時期は 2-1) | T3-04, T3-05 | 1*, 3* |
| **SAP**(2026 Q2、2026-07-23) | クラウド売上 +22%(cc +24%)。Cloud ERP Suite +25%(cc +27%)。総売上 +9%(cc +11%) | 現在のクラウド受注残 €22.9B、+27%(cc +26%)。Reltio の初めての算入で cc 成長率へ 1pt 未満の寄与。受注残の伸びとクラウド売上の伸びの差 = 27 − 22 = 5pt(算出) | 2026 年のクラウド売上ガイダンス €25.8〜26.2B、+23〜25%(Quartr の要約)。2026 年の非 IFRS 営業利益ガイダンス €11.8〜12.2B。AI 固有の指標は未取得 | T3-16(SAP の発表、Barchart、Quartr) | 1*, 3* |
| **Workday**(FY27 Q2、2026-07-31 期末、2026-08-27 発表) | 総売上 $2.649B、+12.8%。購読売上 $2.471B、+13.9%。FY27 購読売上ガイダンス $9.940〜9.950B(約 +13%) | 受注残の数値は未取得 | AI は新規 ACV の 25% 超。自社エージェントを 1 つ以上使う顧客は 5,500 超(前四半期比 +35% 超)。席課金の変更への言及は見つからず | T3-17(Workday 発表、Pulse 2.0) | 1*, 3* |
| **ServiceNow**(2026 Q2、2026-07-22 発表) | 購読売上 $3,877M、+24.5%(cc +23%)。別の報道は総売上 $3.99B、+24% | cRPO $13.20B、+21%(cc +21.5%)。cRPO の伸びは購読売上の伸びより小さい(21.5 対 23、いずれも cc、算出)。100 万ドル超の純新規 ACV の取引 123 件(約 +40%)。500 万ドル超の顧客 658 社(約 +23%) | CEO「エージェント型の ServiceNow AI の展開が 9 ヶ月で 9 倍」。Now Assist の ACV 値は今期分を取れず。株価は 2026 年初から 38% 下落(247wallst の見出し、2026-07-22) | T3-19(SEC 8-K、ServiceNow 発表、247wallst) | 1*, 3* |
| **Salesforce**(FY27 Q2、2026-07-31 期末、2026-08-26 発表) | 売上 $11.3B、+11%(USD・cc とも)。Informatica の寄与 $456M を含む。FY27 売上ガイダンス $46.1〜46.4B(+$200M 引上げ) | RPO $66.3B、+11%。cRPO $33.5B、+14%(cc) | Agentforce の ARR は取れず(欠損)。有機成長率(Informatica 除く)は、前年同期売上が未取得のため算出できず | T3-20(Salesforce 発表、Barchart) | 1*, 3* |

- 2026 年の成長率の並置(算出、最新四半期のみ): SAP クラウド +22%(cc +24%)、ServiceNow 購読 +24.5%、Workday 購読 +13.9%、Salesforce 売上 +11%、Oracle SaaS +10%。SaaS の対象範囲(ERP、HCM、CX の比率)が会社ごとに異なるため同条件の比較ではない。
- AI による加速の材料(各社の開示にあるもの): Workday は新規 ACV の 25% 超が AI 関連、ServiceNow はエージェント展開 9 倍。いずれも売上成長の加速を示す数値は同じ要約に出ていない(Workday は通期ガイダンス約 13% に対し当四半期 +13.9%)。
- 減速の材料: ServiceNow の株価 −38%(年初来)は、市場が成長の持続に疑問を持っていることを示す報道の見出し(要約)。

### 4-2. エージェント型 AI のソフトウェア支出予測(2026〜2030 年)

| 予測 | 数値 | 出典 | Tier |
|---|---|---|---|
| Gartner: エージェント型 AI ソフトウェアの支出 | 2030 年に $985B、2025〜2030 年の年平均成長率 62.7%(2026-02-17 公開の抄録。本文は有料) | T3-18(Gartner のドキュメント 7455226) | 1* |
| 同(算出) | 2025 年の水準 = 985 ÷ 1.627^5 = 約 $86B。2026 年の推定 = 86.4 × 1.627 = 約 $141B | (算出) | - |
| Gartner: 供給網管理ソフト(エージェント AI 付き) | 2025 年 $2B 未満 → 2030 年 $53B(2026-04-07 の Gartner プレスリリース)。年平均成長率(算出: (53 ÷ 2)^(1/5) − 1 = 約 93%。2025 年を $2B と置いた上限的な値) | T3-18 | 1* |
| Gartner を引くブログ: 企業ソフトに組込まれたエージェント機能を含む 2026 年の支出 | $201.9B(Gartner 自身の資料では未確認)。スタンドアロン市場は約 $7〜8.5B との別の推計と対比 | T3-18(Software Strategies Blog) | 4* |
| Gartner の世界の AI 支出(参考) | 2026 年 $2.7T(Techstrong の見出し)、別のブログは $5.95T(年・範囲の記載不明) | T3-18 | 3*, 4* |
| IDC・Forrester・McKinsey のエージェント型ソフト支出予測 | **欠損**(IDC は検索していない。検索数の上限のため) | - | - |

---

## 5. 反証: 「AI がシート課金の SaaS を食う」懸念と Oracle のアプリへの影響の材料

| 項目 | 取れた事実 | 出典 | Tier |
|---|---|---|---|
| 懸念の発生 | 2026-02 初めに software 株が急落。ある出典は「2026-02-03 に 1 日でセクターが 13% 下落」と記述。下落額は出典により $285B、約 $1T、IGV が年初来 −23% と食い違い(未検証) | T3-21(Forbes 2026-02-06、tech-insider ほか) | 3*, 4* |
| 論拠(懸念側) | AI エージェントで 1 人が複数人分の業務を処理でき、席の購入数が減る(Forbes) | T3-21 | 3* |
| 論拠(反論側) | BofA の Vivek Arya「売り込みは過剰で論理的に一貫しない」。エージェントも Salesforce・Slack・Microsoft 365 などのツール経由で動くため席の価値は残る(Dave Michels)。Goldman は「ファンダメンタルズの急変ではなくセンチメントの急変」 | T3-21 | 3* |
| 課金の移行 | Goldman の言う「Results-as-a-Service」。Forrester の調査として席課金の採用率が 12 か月で 21% から 15% へ(ブログ経由、出典未検証) | T3-21 | 4* |
| Oracle の Fusion の課金は席ではなくメーター | 「Microsoft や Salesforce が先に選んだ席ではなく、Oracle はメーターを選んだ」(Redress Compliance)。プール残高から 1 単位 1 セントで消費 | T3-21 | 4* |
| Oracle の収益のうち席に連動する部分 | 欠損。HCM は従業員数×月額、ERP はユーザー×月額の価格体系(既存調査 [R2]、助言会社のブログ)。会社の開示で席連動の割合は取れず | [R2] | 4 |
| Oracle のアプリへの影響を分析した調査・アナリストノート | **欠損**(T3-21 では見つからず) | T3-21 | - |
| Oracle の人員削減 18%(2026 年初め) | 品質の低いブログの記述、確認できず。不採用 | T3-21 | 4*(不採用) |
| 実績としての SaaS 成長 | Q1 FY26〜Q1 FY27 の 5 四半期で +10〜13%(第 1 節)。Q4 FY26 の NetSuite +9%(スライド文字列)。「NetSuite は意思決定サイクルが長く成長が鈍い」との言及 | T3-05, T3-07 | 1*, 3* |
| 1 人あたりの単価の構造 | SaaS 売上 $4.2B(Q1 FY27、+10%)は、席・ユーザー数と単価の分解が欠損 | - | - |

### 5-2. 「SaaS の需要は後半にかけて大きくなる」への根拠と反証(事実のみの整理、判断なし)

| 区分 | 事実 | 節 |
|---|---|---|
| 根拠側 | Q4 FY26 の SaaS 繰延収益が +16%(売上 +10% より高い)。ただし 1 件の要約のみ | 1-2 |
| 根拠側 | Fusion Agentic Applications の発表は 2026-03-24(Q4 FY26 期中)、CX 版は 2026-04-09。Q1 FY27(2026-06〜08)は発表後の最初の通しの四半期(期間の比較)で、売上への寄与の数値は出ていない | 2-1 |
| 根拠側 | Q1 FY27 の説明会要約で「Fusion と業種別アプリは 10% を大きく上回る」。Fusion +14%(既存調査の要約) | 1-1 |
| 根拠側 | Software 売上の減少(−2%、−3%)を会社は「クラウド移行」と説明 | 3 |
| 根拠側 | SAP のクラウド受注残の伸び(+27%)がクラウド売上の伸び(+22%)を 5pt 上回る(同業の先行指標の例) | 4 |
| 根拠側 | AI 支援の導入で go-live が「2 桁月から 1 桁月」へ(収益の認識の開始が早まる可能性。会社の説明) | 2-1, 3 |
| 反証側 | SaaS の YoY は直近 5 四半期で 11% → 11% → 13% → 10% → 10% と加速していない | 1-1 |
| 反証側 | Fusion ERP は +22%(Q4 FY25)から Q3 FY26 +17%、NetSuite は +18% から +14%、Q4 FY26 のスライド文字列で +12%・+9% | 1-1 |
| 反証側 | 経営陣の発言は「2 桁成長は悪くない」(Q4 FY26)で、アプリの加速を明示した発言は見つからず | 2-4 |
| 反証側 | FAM の目標は OCI が中心(OCI $166B = 約 74%)。アプリの目標は欠損 | 2-4 |
| 反証側 | 2024 年の「low-to-mid teens の SaaS 成長」見通しの記述に対し実績は 10% 前後(古い見通し、未確認) | 2-4 |
| 反証側 | AI エージェントは「追加費用なし」とする発表がある(2025-03、2026-02)。売上の押し上げ要因として価格が設定されているかは、課金方式の食い違い(第 6 節)により未確定 | 2-2 |
| 反証側 | 席課金への懸念(2026-02)。Oracle への影響は未分析 | 5 |

---

## 6. 食い違い

| # | 項目 | A | B | 判定・メモ |
|---|---|---|---|---|
| 1 | Q1 FY27 の Fusion ERP・NetSuite | 既存調査 [H1]: Fusion ERP $1.1B(+17%)、NetSuite $1.1B(+14%) | 本調査: Q3 FY26 の Oracle 発表が Fusion ERP $1.1B(+17%)、NetSuite $1.1B(+14%)(T3-02)。Q1 FY27 の発表要約(T3-04)には ERP 2 行なし | [H1] の Q1 FY27 値は Q3 FY26 の値と同じため誤帰属の可能性が高い(算出ではなく数値の一致)。**未解決**。Q1 FY27 の公式値は欠損 |
| 2 | Q4 FY26 の Fusion の区分 | 「Fusion Back-Office $1.5B、+12%」(スライド文字列、T3-05) | 以前の四半期は「Fusion Cloud ERP $1.0〜1.1B」(T3-02, T3-06) | 区分が変わった可能性(ERP + HCM + SCM か)。スライドの文字は文字化けありで未確認。**未解決** |
| 3 | Q4 FY26 の NetSuite | 事前の予想はミドル〜ハイティーン(GPUSmith、2026-05-28、Tier 4、予想) | スライド文字列 +9%(T3-05) | 予想と実績の差であって数値の食い違いではない。実績 +9% も文字化けスライド由来で要確認 |
| 4 | Fusion の AI の課金 | Oracle: Agent Studio は追加費用なし(2025-03)、供給網エージェントは既存顧客に追加費用なし(2026-02)(T3-08, T3-11、Tier 1*) | Redress Compliance: プール残高から 1 単位 1 セントの従量(T3-21、Tier 4*) | 対象のエージェントや時期が異なる可能性。**未解決**。Agentic Applications の価格は欠損 |
| 5 | Cloud Wars の「Fusion ERP +46%、Fusion HCM +35%、NetSuite +26%」 | Cloud Wars の記事(T3-02): Q4 の Fusion ERP が +46%(Q3 は +30%)、HCM +35%、NetSuite +26%(Q3 は +24%)。Safra Catz を CEO と呼ぶ | Oracle の発表(T3-22): Q4 FY25 の Fusion ERP +22%、NetSuite +18% | 記事は古い年度(FY25 より前)の別指標の可能性。時点・指標とも不明のため不採用 |
| 6 | Q1 FY27 の SaaS | 一部の二次情報は $4.0B(+13%)(既存調査 [H1] が不採用と判定) | 本調査: $4.2B、+10%(Verdict、Benzinga、chartmill、Oracle 発表の要約。T3-04, T3-09, T3-23) | $4.0B(+13%)は Q3 FY26 の値と一致。$4.2B(+10%)を採用。解決 |
| 7 | Gartner の 2026〜2030 年のエージェント AI 支出 | 抄録: 2030 年 $985B、年平均成長率 62.7%(逆算で 2026 年 約 $141B、(算出)) | ブログ: 企業ソフト組込み分を含む 2026 年 $201.9B。別のブログは 2030 年に $1T 超 | 範囲(組込み分を含むか)が違う可能性。ブログの数値は Gartner 資料で未確認。**未解決** |
| 8 | ソフトウェア株の下落規模 | $285B | 約 $1T、IGV 年初来 −23%、1 日で −13%(Feb 3) | 出典間で不一致。いずれも検証なし。**未解決** |
| 9 | ServiceNow の売上 | 購読売上 $3,877M、+24.5%(8-K 要約) | 別の報道は総売上 $3.99B、+24% | 購読売上と総売上の違いの可能性。購読売上を採用 |
| 10 | 旧来 ERP 顧客 8,500 社 / 1,000 社の時点 | 検索要約: CEO が決算説明会で発言 | 発言者・時点は不明 | **時点は欠損**。古い可能性があるため現在値としては使えない |

---

## 7. 欠損と検索語

検索語は 8 節の検索番号に対応。

| # | 欠損した項目 | 試した検索語(番号) | 状態 |
|---|---|---|---|
| 1 | Q2 FY25 の SaaS・Fusion ERP・NetSuite、Q3 FY25 の SaaS 単独値 | T3-22「Oracle fiscal 2025 quarterly cloud application SaaS revenue growth Q2 FY25 Q3 FY25 Q4 FY25 Fusion Cloud ERP NetSuite」 | 欠損。丸め値からの逆算は誤差が大きいため行わず |
| 2 | Q4 FY26 の Fusion ERP・NetSuite の確定値、スライドの正確な表記 | T3-02, T3-03, T3-05(「Q4 FY26 Fusion ERP NetSuite」) | スライド文字列のみ(文字化け) |
| 3 | Q1 FY27 の Fusion ERP・NetSuite・Oracle Health の公式値 | T3-01, T3-04, T3-07, T3-09, T3-23 | 欠損 |
| 4 | Fusion HCM・SCM・CX の四半期別成長 | T3-02, T3-03, T3-05(上記検索の副次) | 欠損。会社は ERP 2 行(後に Back-Office 1 行)のみ開示 |
| 5 | 業種別アプリの四半期別成長 | T3-07, T3-09 | 「10% を大きく上回る」の要約のみ |
| 6 | Oracle Health の売上・成長率 | T3-12「Oracle Health new EHR agentic AI customers go-live 2026 Oracle Health revenue decline VA rollout」、T3-07 | 欠損 |
| 7 | アプリ別の RPO・受注 | T3-05, T3-24(「SaaS deferred revenue」) | 全社 RPO と SaaS 繰延収益(1 件)のみ |
| 8 | 「本番稼働 2,300 超」 | T3-08「AI Agent Studio Fusion applications 2,300 agents production no additional charge」、T3-10「Oracle Fusion AI agents "2,300" production customers Agent Studio 2026」 | **欠損**(出典なし) |
| 9 | Fusion Agentic Applications の価格 | T3-11 | 欠損 |
| 10 | AI Data Platform、Enterprise Ontology | T3-11「Oracle AI World 2026 Fusion Agentic Applications ... Enterprise Ontology AI Data Platform」、T3-23 | 欠損 |
| 11 | Oracle Health の新 EHR(Agentic)の顧客・稼働時期 | T3-12 | 欠損(VA のみ) |
| 12 | FAM のアプリ(SaaS)売上目標 | T3-13「Oracle financial analyst meeting October 2025 applications revenue target fiscal 2030 ...」、T3-14(extended) | 欠損 |
| 13 | 経営陣の「アプリの成長が加速する」明示の逐語発言 | T3-07, T3-09, T3-14, T3-24 | 欠損 |
| 14 | 移行後の顧客あたり売上の倍率 | T3-15「Oracle E-Business Suite PeopleSoft JD Edwards customers migrate to Fusion Cloud revenue multiple per customer times larger」 | 欠損 |
| 15 | 8,500 社 / 1,000 社の発言の時点 | T3-15 | 欠損 |
| 16 | SAP のクラウド受注残以外の AI 指標、Workday の受注残 | T3-16, T3-17 | 欠損 |
| 17 | Salesforce の Agentforce ARR、有機成長率 | T3-20 | 欠損 |
| 18 | ServiceNow の Now Assist ACV(今期分) | T3-19 | 欠損 |
| 19 | IDC の予測、Gartner の本文 | T3-18(Gartner のみ検索。IDC は未検索) | 欠損(IDC は検索数の上限のため未着手) |
| 20 | Oracle のアプリへの席圧縮の影響の分析 | T3-21「AI agents threaten seat-based SaaS 2026 software selloff Oracle applications Fusion exposure analysts per-seat pricing」 | 欠損 |
| 21 | Oracle の SaaS の席・単価の分解 | T3-21 | 欠損 |
| 22 | Oracle Fusion の顧客数 | (本調査では検索せず。既存 [R2] も欠損) | 欠損 |

---

## 8. 出典一覧(検索 24 回、standard 20 回・extended 4 回)

検索要約に表示された URL。1 回の要約が複数サイトを統合しているため、個々の数値がどの URL 由来かは特定できないものがある。

| ID | 検索の趣旨(mode) | 主な URL | Tier |
|---|---|---|---|
| T3-01 | Q1 FY27 の SaaS・Fusion ERP・NetSuite(standard)。返ったのは Q1 FY26 の発表 | https://www.oracle.com/news/announcement/q1fy26-earnings-release-2025-09-09/ | 1* |
| T3-02 | Q4 FY26 の Fusion ERP・NetSuite(standard)。Q3 FY26 の 8-K と Cloud Wars が返る | https://www.sec.gov/Archives/edgar/data/1341439/000119312526100148/orcl-ex99_1.htm 、https://www.nasdaq.com/articles/oracles-netsuite-division-focus-will-it-boost-revenue-growth 、https://cloudwars.com/oracle/larry-ellison-oracle-erp-revenue-could-reach-30b/ 、https://gpusmith.com/articles/oracle-q4-fy2026-earnings-netsuite-ai-analysis 、https://www.houseblend.io/articles/en/resultats-oracle-t4-exercice-2026-analyse-netsuite-ia | 1*, 3*, 4* |
| T3-03 | Q4 FY26 の発表(standard) | https://www.oracle.com/news/announcement/q4fy26-earnings-release-2026-06-10/ 、https://seekingalpha.com/pr/20547657 、https://www.verdict.co.uk/?p=402027 | 1*, 3* |
| T3-04 | Q1 FY27 の発表(standard) | https://www.verdict.co.uk/oracle-q1-fy27-results/ 、https://www.benzinga.com/node/61728003 、https://storagenewsletter.com/2026/09/23/oracle-fiscal-1q27-financial-results 、https://www.chartmill.com/news/external/152712/oracle-q1-earnings-beat-estimates-cloud-growth-accelerates | 3* |
| T3-05 | Q4 FY26 の説明会(extended) | https://erp.today/oracle-q4-2026-earnings-ai-cloud-backlog-funding/ 、https://s23.q4cdn.com/440135859/files/doc_financials/2026/q4/Q4-FY26-Oracle-Earnings-Slides.pdf 、https://finance.yahoo.com/quote/ORCL/earnings/ORCL-Q4-2026-earnings_call-592465.html 、https://www.investing.com/news/transcripts/earnings-call-transcript-oracle-q4-2026-earnings-beat-expectations-despite-stock-dip-93CH-4736322 、https://www.cnbc.com/2026/06/10/oracle-orcl-q4-earnings-report-2026.html | 1*, 3* |
| T3-06 | Q2 FY26 の発表(standard) | https://www.oracle.com/news/announcement/q2fy26-earnings-release-2025-12-10/ 、https://seekingalpha.com/pr/20335876 | 1* |
| T3-07 | Q1 FY27 の説明会(extended) | https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/ 、https://www.gurufocus.com/stock/XKAZ:ORCL_KZ/transcripts/9076583 、https://www.benzinga.com/news/26/09/61729962/oracle-reports-q1-2027-results-full-earnings-call-transcript 、https://equibles.com/stocks/orcl/calls/2027-q1 、https://stockanalysis.com/stocks/orcl/transcripts/689425-q1-2027/ | 3* |
| T3-08 | AI Agent Studio・追加費用・2,300(standard) | https://www.oracle.com/news/announcement/oracle-introduces-ai-agent-studio-2025-03-20/ 、https://www.cxtoday.com/?p=68653 、https://erp.today/oracle-unveils-ai-agent-studio-for-fusion-cloud-applications/ | 1*, 3* |
| T3-09 | Q1 FY27 の説明会の語句検索(standard) | https://cryptobriefing.com/oracle-q1-fy27-earnings-revenue-rpo/ 、https://www.tradingkey.com/news/transcripts/262162053-tradingkey 、https://www.chartmill.com/news/external/152712/oracle-q1-earnings-beat-estimates-cloud-growth-accelerates | 3* |
| T3-10 | 「2,300」本番稼働(standard) | https://blogs.oracle.com/fusioninsider/apps-2025-update-ai-agents-ai-marketplace-and-more 、https://www.oracle.com/news/announcement/blog/oracle-sets-the-standard-in-enterprise-ai-2025-09-18/ | 1* |
| T3-11 | AI World 2026・Fusion Agentic Applications(standard) | https://www.oracle.com/news/announcement/oracle-introduces-fusion-agentic-applications-2026-03-24/ 、https://www.oracle.com/news/announcement/oracle-introduces-fusion-agentic-applications-for-cx-2026-04-09/ 、https://www.nasdaq.com/articles/oracle-unveils-ai-agents-fusion-apps-will-it-boost-prospects | 1*, 3* |
| T3-12 | Oracle Health・VA(standard) | https://www.beckershospitalreview.com/healthcare-information-technology/ehrs/va-deploys-oracle-health-ehr-at-4-more-sites/ 、https://www.beckershospitalreview.com/healthcare-information-technology/ehrs/va-to-resume-oracle-health-ehr-rollout-in-waves/ 、https://www.beckershospitalreview.com/healthcare-information-technology/ehrs/13-va-medical-centers-to-go-live-with-oracle-ehr-in-2026/ 、https://www.beckershospitalreview.com/healthcare-information-technology/ehrs/va-to-restart-oracle-health-ehr-at-4-michigan-hospitals/ | 3* |
| T3-13 | FAM のアプリ目標(standard) | https://de.tradingview.com/news/reuters.com%2C2025%3Anewsml_L6N3VX11P%3A0-oracle-expects-cloud-sales-of-166-billion-by-2030-as-business-expands 、https://know.creditsights.com/insights/oracle-top-10-takeaways-from-2025-analyst-meeting/ 、https://www.oracle.com/a/ocom/docs/corporate/financial-analyst-meeting-2025-kehring.pdf | 1*, 3* |
| T3-14 | FAM のアプリ目標・Sicilia(extended) | https://cloudwars.com/cloud-wars-minute/oracle-on-fire-fy30-rev-225b/ 、https://finance.yahoo.com/markets/stocks/articles/oracle-corp-orcl-q1-2027-090101356.html 、https://www.moatexplorer.com/oracle/the-future-bets/225-billion-by-fiscal-2030/ | 3*, 4* |
| T3-15 | EBS・PeopleSoft・JDE から Fusion への移行(standard) | https://diginomica.com/2018/06/07/oracle_erp_soar_cloud/ 、https://accelerationeconomy.com/?p=18805 、https://oraclelicensingexperts.com/blog/oracle-erp-cloud-migration-licensing/ 、https://redresscompliance.com/cio-playbook-transition-from-oracle-on-premise-applications-to-oracle-fusion-cloud 、https://www.erpresearch.com/pages/en-gb/peoplesoft-to-oracle-erp-cloud | 3*, 4* |
| T3-16 | SAP 2026 Q2(standard) | https://www.sap.com/docs/download/investors/2026/sap-2026-q2-statement.pdf 、https://news.sap.com/2026/07/sap-announces-q2-and-half-year-2026-results/ 、https://www.barchart.com/story/news/3434684/sap-quarterly-statement-q2-2026 、https://quartr.com/events/sap-se-sap-q2-2026_3elEDXgy | 1*, 3* |
| T3-17 | Workday FY27 Q2(standard) | https://newsroom.workday.com/2026-08-27-Workday-Announces-Fiscal-2027-Second-Quarter-Financial-Results 、https://investor.workday.com/news-and-events/press-releases/news-details/2026/Workday-Announces-Fiscal-2027-Second-Quarter-Financial-Results/default.aspx 、https://pulse2.com/workday-ai-drives-more-than-25-of-new-acv-as-agent-customers-jump-more-than-35-sequentially/ | 1*, 3* |
| T3-18 | Gartner のエージェント AI 支出予測(standard) | https://www.gartner.com/en/documents/7455226 、https://www.gartner.com/en/newsroom/press-releases/2026-04-07-gartner-forecasts-supply-chain-management-software-with-agentic-ai-will-grow-to-53-billion-in-spend-by-2030 、https://softwarestrategiesblog.com/2026/08/05/gartner-5-95-trillion-ai-forecast-chatbot-era-2027-deadline/ 、https://techstrong.ai/agentic-ai/gartner-forecasts-worldwide-ai-spending-to-surge-to-2-7-trillion-in-2026/ | 1*, 3*, 4* |
| T3-19 | ServiceNow 2026 Q2(standard) | https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000072/erq2fy26.htm 、https://investor.servicenow.com/news/news-details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx 、https://247wallst.com/investing/2026/07/22/live-will-servicenows-q2-earnings-tonight-drive-a-rebound-after-38-ytd-decline/liveupdates/4/ | 1*, 3* |
| T3-20 | Salesforce FY27 Q2(standard) | https://investor.salesforce.com/news/news-details/2026/Salesforce-Delivers-Record-Second-Quarter-Fiscal-2027-Results/ 、https://www.salesforce.com/news/press-releases/2026/08/26/fy27-q2-earnings/ 、https://www.barchart.com/story/news/4134578/salesforce-delivers-record-second-quarter-fiscal-2027-results | 1*, 3* |
| T3-21 | 席課金への AI の影響・Oracle の露出(extended) | https://www.forbes.com/sites/petercohan/2026/02/06/saaspocalypse-now-ai-is-disrupting-saas---but-not-all-software-is-doomed/ 、https://redresscompliance.com/oracle-fusion-ai-agents-licensing-pillar-2026 、https://tech-insider.org/saas-stock-crash-ai-agents-2-trillion-2026/ 、https://helply.com/blog/per-seat-saas-pricing-dying 、https://www.taskade.com/blog/great-saas-unbundling | 3*, 4* |
| T3-22 | Oracle FY25 の四半期(standard) | https://www.oracle.com/news/announcement/q4fy25-earnings-release-2025-06-11/ 、https://www.sec.gov/Archives/edgar/data/1341439/000095017025084831/orcl-ex99_1.htm 、https://www.sec.gov/Archives/edgar/data/1341439/000095017025036295/orcl-ex99_1.htm | 1* |
| T3-23 | Q1 FY27 の説明会ハイライト(standard) | https://quartr.com/events/oracle-corporation-orcl-q1-2027_3gvkOKJp 、https://seekingalpha.com/pr/20647809 | 1*, 3* |
| T3-24 | Q4 FY26 の SaaS 繰延収益・加速(standard) | https://www.nasdaq.com/articles/oracle-q4-earnings-call-highlights 、https://www.oracle.com/news/announcement/q4fy26-earnings-release-2026-06-10/ | 1*, 3* |

既存調査(/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/)から再掲のみ: research/S1_management_scenario.md(Sicilia 発言、FAM)、research2/R2_products_5w1h.md(Fusion・NetSuite の価格、Q1 FY27 の「Fusion +14%」)、data/H1_quarterly_pl.csv(四半期の SaaS・RPO)、research4/T4_ai_demand.md(RPO・AI 需要)。
