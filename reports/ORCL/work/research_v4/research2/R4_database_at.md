# Oracle(ORCL)マルチクラウド DB(Database@Azure / @AWS / @Google Cloud)と AI Database(26ai)の事業価値の見積り用ファクト R4

- 作成日: 2026-10-12 / 担当: R4(マルチクラウド DB と AI Database)
- 最新の報告済み四半期: Q1 FY2027(2026-08-31 終了、2026-09-10 発表)
- 取得方法: WebSearch のみ。**28 回 / 上限 28 回(standard 12、extended 16)**。WebFetch は不使用。**原本(8-K、10-K、決算説明会の逐語、Oracle のプレスリリース)は一度も開いておらず、すべて検索要約経由。** 原本照合は未了。
- 表記: `[出典ID·Tier]`。Tier 1=会社開示・決算説明会、2=規制当局・格付会社・公的統計、3=報道・アナリスト・調査会社、4=ブログ・SNS・販促ページ。**T1\*** は「会社開示の文書だが、検索要約を通してしか読んでいない」の意味(既存調査と同じ表記)。「(算出)」は自分で計算した値で式を併記。
- 投資判断(買い・売り)は書かない。事実・数値・出典・食い違いの整理だけ。
- 既存調査(S1〜S4、H1〜H6、R1〜R3)で確認済みの内容は繰り返さず、足りない部分を埋めた。

---

## 0. 最重要の発見(各 1 行)

1. **マルチクラウド DB の売上成長率(前年同期比)は 5 四半期で +1,529% → +817% → +531% → +404% → +353%。** 各値は Oracle の決算プレスリリース(Q1〜Q4 FY26)の文言を検索要約で確認(T1\*)。Q1 FY27 の +353% と顧客数 +180% は決算説明会の要約のみ(T3、複数の要約サイトで一致)。
2. **売上の絶対額・年換算額は、会社も報道もアナリストも出していない(欠損)。** 手がかりは「Azure が大半」(Ellison)、FY25 の DB 全体の基数 $2.4B(FAM 報道、定義は未確認)、Q4 時点のクラウド DB 全体の年換算 $2.6B 程度(1 社)だけ。
3. **稼働リージョンは Q3 FY26 時点で Azure 33 + Google 14 + AWS 8 = 55(算出)、Q1 FY27 で「合計 70 リージョン・119 AZ、Azure と AWS の計画拡張は完了」(単一系統の要約)。** 既存 R2 の「Azure 28」は古い値と見られる。
4. **課金は各ハイパースケーラーのマーケットプレイス経由で、顧客のハイパースケーラーへの確約支出(Azure の MACC、AWS のコミット)に充当できる。** Exadata は OCI が運用し、ハイパースケーラーのデータセンター内に置かれる。**Oracle とハイパースケーラーの取り分、ハードウェアの会計上の所有者は欠損。**
5. **マルチクラウド DB の粗利率について、CEO の Magouyrk が Q3 FY26 の説明会で「60〜80% のレンジ」と述べたと複数の二次媒体が報じる(T3)。** ただし別の検索ではこの数字の出典を確認できず、Oracle 側の原文は未読。AI インフラ(GPU 貸し)は 30〜40%、Q3 FY26 の実績は 32%。
6. **既存 S1 の「予約 +325%」は誤帰属の可能性が高い。** +325% は Q3 FY26 の RPO(受注残)$553B の前年比であり、Q4 FY26 の RPO は $638B(+363%)。マルチクラウド DB の予約成長率は今回の検索では見つからず(欠損)。

---

## 1. 開示(成長率・予約・顧客数・リージョン・絶対額)

### 1-A. マルチクラウド DB 売上の成長率の時系列

| 四半期(期末) | 発表日 | 前年同期比(USD) | 前年同期に対する倍率(算出: 1+成長率) | 会社の文言(要点) | 出典・Tier |
|---|---|---|---|---|---|
| Q1 FY26(2025-08-31) | 2025-09-09 | **+1,529%** | 16.29 倍 | Ellison「Amazon、Google、Microsoft からのマルチクラウド DB 売上は Q1 に 1,529% という驚異的な率で成長した」。「今後数年、四半期ごとに大きく伸びる。3 つのハイパースケーラー向けにさらに 37 のデータセンターを引き渡し、合計 71 になる」 | [R4-01] Oracle プレスリリース T1\*。FAM の資料では同じ 1,529% を「MultiCloud **Consumption** Growth」と表記(売上ではなく消費量の可能性。下記 6 節の食い違い 9) [R4-12] T3 |
| Q2 FY26(2025-11-30) | 2025-12-10 | **+817%** | 9.17 倍 | 「マルチクラウド DB は最も速く成長している事業。Q2 に +817%」。「Amazon、Google、Microsoft のクラウドに埋め込む 72 のマルチクラウド・データセンターの建設は半分を超えた」 | [R4-02] Oracle プレスリリース T1\*(10-K 検索の要約にも同文) |
| Q3 FY26(2026-02-28) | 2026-03-10 | **+531%**(Oracle Cloud Database(IaaS)は +35%) | 6.31 倍 | プレスリリースの見出し項目として記載。CEO Magouyrk「マルチクラウド DB と AI インフラは非常に速く伸びており、どちらも需要が供給を上回る」 | [R4-03] Oracle プレスリリース T1\*、[R4-04] Oracle CEO ブログ T1\*、[R4-14] Verdict T3 |
| Q4 FY26(2026-05-31) | 2026-06-10 | **+404%** | 5.04 倍 | 「Oracle **Multicloud AI Database** は Q4 に +404%。当社史上最速で成長する事業」(名称が「Multicloud AI Database」に変わっている) | [R4-05] Oracle プレスリリース T1\* |
| Q1 FY27(2026-08-31) | 2026-09-10 | **+353%**、**顧客数 +180%** | 4.53 倍 | 「マルチクラウド DB 売上は前年比 +353%、マルチクラウド顧客は前年比 +180%」。「Azure と AWS の計画していたリージョン拡張を完了し、70 リージョン・119 アベイラビリティゾーン」。「Oracle Interconnect for AWS が一般提供」(1 社のみ) | [R4-06] Alpha Spread、Yahoo、Quartr、TradingKey、BigGo、Motley Fool 等の説明会要約 T3(複数で一致、逐語は未読) |

- 2 年間の累積倍率(算出): Q1 FY26 の前年比 16.29 倍 × Q1 FY27 の前年比 4.53 倍 = **約 73.8 倍(Q1 FY25 → Q1 FY27)**。売上額が不明なので、この倍率は基数の小ささを示すだけで、絶対額の手がかりにはならない。
- 成長率は 5 四半期連続で逓減している(+1,529 → +817 → +531 → +404 → +353)。会社は「基数効果」とは説明していないが、前年同期の基数が急拡大した結果と整合する(解釈)。
- **予約(bookings)・受注残のマルチクラウド DB 単独の成長率: 欠損。** 既存 S1 が引いた「予約 +325%(AlphaSense、Q4 FY26)」は、今回の検索では Q3 FY26 の RPO +325%($553B)と一致し、マルチクラウド予約の値とは確認できなかった(6 節の食い違い 1)。
- 顧客数の絶対数: **欠損**(+180% の伸びのみ)。顧客名の開示も確認できず。

### 1-B. 稼働リージョン数(会社・クラウド別、時点つき)

| 時点 | Azure(Microsoft) | Google Cloud | AWS | 合計・備考 | 出典・Tier |
|---|---|---|---|---|---|
| 2025-09(Q1 FY26 説明会) | — | — | — | 目標: 3 社に 37 を追加し **計 71** | [R4-01] T1\* |
| 2025-12(Q2 FY26) | — | — | — | 「72 のマルチクラウド・データセンターのうち半分超を建設」。ライブ 45 + 計画 27(1 社の要約、出典未特定) | [R4-02] T1\*、[R4-10] T3 |
| 2026-01 | **31**(+2 を 3 か月以内に予定)/「30 超」 | — | — | Microsoft の投稿。日付は要約に出ず(Brazil Southeast と West Europe の追加を告知) | [R4-16] Microsoft Tech Community T1\*(提携先) |
| 2026-01 頃(Oracle の一覧) | **33**(一覧の個数を数えた。算出) | — | — | Oracle 側の一覧に Canada、米国、欧州、UAE、豪州、インド、日本、東南アジア、ブラジルなど 33 件 | [R4-16] T1\*(算出は自分の数え上げ) |
| 2026-02-28(Q3 FY26 末) | **33** | **14** | Q3 期首 2 → 期末 **8**(Q4 末目標 **22**) | 3 社合計は **55**(算出: 33+14+8)。需要が供給を上回る | [R4-04] Oracle CEO ブログ T1\*、[R4-14] Verdict T3 |
| 2026-02 〜 05(AWS 発表) | — | — | 2026-02 に 7、2026-04 に 12、**2026-05-29 に 20** | AWS の発表(既存 R2 の W24) | 既存 R2 [W24] T1\*(提携先) |
| 日付不明(DCD) | — | **約 15**(+2 予定) | 20 | 既存 H4 の S10・S11 | 既存 H4 T3 |
| 2026-09-10(Q1 FY27 説明会) | (Azure と AWS の計画拡張は完了) | — | — | **合計 70 リージョン・119 AZ**(算出の突合: 33+15+22=70 は成り立つが、AWS 20・Google 14 なら 67〜68。内訳は未確認) | [R4-06] T3(単一系統) |
| 参考(Google の過去) | — | GA 時(2024-09)は 4 リージョン(米・欧)。その後「7 リージョン」の告知(日付不明) | — | — | [R4-17] DCD、Oracle ブログ T3/T1\* |

- 時点の推移(算出): Q2 FY26 ライブ 45(1 社の要約)→ Q3 FY26 末 55 → Q1 FY27 70。Q3 FY26 末から Q1 FY27 で +27%(70÷55)。
- 計画の単位が「データセンター 71〜72」と「リージョン 70」で混在しており、同じ単位かは未確認。

### 1-C. 売上の絶対額・年換算額(開示・報道・アナリスト推定)

| 項目 | 値 | 性質 | 出典・Tier |
|---|---|---|---|
| マルチクラウド DB の四半期売上・年換算 | **欠損**(会社は成長率と顧客数の伸びだけ開示) | — | 試した検索語: "multicloud database revenue run rate billion estimate analyst"(extended)、"Oracle financial analyst meeting multicloud database revenue target"、"Q1 fiscal 2027 multicloud database revenue" 系 |
| 内訳(Azure / Google / AWS) | **欠損**。Ellison の発言: 成長の大半は最初の提携先である Microsoft(Azure)。Google と AWS は「Azure の規模にはまだ遠く及ばない」 | 経営陣の定性発言(2025-09 の Q1 FY26 後。日付は要約に出ず) | [R4-07] Cloud Wars T3 |
| クラウド DB 全体の年換算 | 約 **$2.6B**(Q4 時点。どの Q4 かは要約に出ず)。既存 S4 は Q1 FY26 のクラウド・データベース・サービスが +32%、年換算約 $2.8B | 分析記事(マルチクラウド単独ではない) | [R4-08] io-fund T3、既存 S4 |
| FAM(2025-10)の DB 売上の基数 | FY25 **$2.4B**、FY26 **$3B**(FY26 の $3B は 1 社のみ、会社目標か推定か不明) | 「AI データベースと AI データ・プラットフォーム」の売上と報じられる。**マルチクラウドを含むか、Autonomous・Cloud@Customer を含むかは未確認** | [R4-09] Cloud Computing News T3 |
| FY30 の DB 目標 | **$20B**(FY25 の $2.4B から)。年平均成長率 約 53%(CreditSights)。算出: (20÷2.4)^(1/5)−1 = **52.8%**。FY26 の $3B を起点にすると (20÷3)^(1/4)−1 = 60.7%(算出) | 経営陣目標の報道(原資料 FAM 資料 PDF は未読) | [R4-09] T3、[R4-12] CreditSights T3 |

---

## 2. 経済性(誰が課金するか、取り分、インフラ、粗利率、顧客あたり売上)

| 論点 | 判明した事実 | 欠損・未確認 | 出典・Tier |
|---|---|---|---|
| 誰が顧客に課金するか(Azure) | **Azure 経由**。Microsoft の文書:「請求と支払いは Azure を通じて行われる」。Oracle の営業が **Azure Marketplace に Private Offer** を作成して顧客に提示する。Oracle のページ:「価格は OCI 上の Exadata Database Service と同じ」 | Oracle の請求書が別に出るか(会計上の売上計上が総額か純額か)は未確認 | [R4-18] Microsoft Learn T1\*(提携先)、[R4-19] Oracle ドキュメント T1\* |
| 誰が課金するか(AWS) | **AWS 経由**。Oracle のドキュメント:「請求と支払いは AWS を通じて行われる」。AWS は「AWS Marketplace の単一請求書。AWS のコミットメントと Oracle Support Rewards に算入」。Oracle が顧客のアカウント宛てに Private Offer を作り、顧客が Marketplace で承諾する。**価格は契約期間、支出コミット額、Exadata の配備台数で決まる** | — | [R4-20] Oracle ドキュメント T1\*、[R4-21] AWS ドキュメント T1\*(提携先) |
| 顧客のハイパースケーラーへの確約支出を Oracle DB に使えるか | **使える**。Azure: Microsoft Azure Consumption Commitment(MACC)に算入(Microsoft・Oracle 双方の記述)。AWS: AWS のコミットメントに算入(Oracle・AWS 双方の記述) | Google Cloud 側の確約支出への算入は今回の検索では未確認。MACC の個別適格性は顧客ごとに確認が必要(既存 R2 の助言会社の注記) | [R4-18]〜[R4-21] T1\* |
| Oracle と各社の取り分(収益分配) | **欠損**。10-K の収益認識の記述、収益分配、ホスティング料(スペース・電力)を探したが、見つからなかった | 総額計上か純額計上か。ハイパースケーラーに払う手数料・コロケーション費用の有無 | 試した検索語: "Oracle 10-K multicloud arrangements Microsoft Google Amazon colocation fee revenue recognized marketplace"、"hyperscaler revenue share fee Oracle keeps revenue" |
| インフラ(Exadata)の所有者・運用者 | **運用は OCI**。AWS の文書:「AWS データセンター内の、OCI が管理する Oracle Exadata インフラ」。Oracle:「Microsoft のデータセンターに併設された OCI」で、Oracle のチームがパッチ適用・インフラ更新を行う。Ellison は「3 つのハイパースケーラー向けにデータセンターを引き渡す」「ハイパースケーラーのクラウドに埋め込む Oracle のデータセンター」と表現 → **Oracle が機器を調達・設置している**(発言からの解釈) | 機器の会計上の所有者、土地・建物・電力・冷却の費用負担は未確認 | [R4-21] AWS T1\*(提携先)、[R4-19] Oracle T1\*、[R4-01][R4-02] T1\* |
| 資本集約度の見方(解釈) | アナリスト(1 社、T4)は「土地・建物ではなく計算・ストレージに資本を使う型」と解釈。Zacks 系の記事は「パートナー施設での配備は資本集約度を高める」と指摘 | **どちらも契約条件に基づく記述ではない** | [R4-22] Substack T4、[R4-15] Yahoo/Zacks T3 |
| 粗利率への影響(経営陣の説明) | **マルチクラウド DB の粗利率は「60〜80%のレンジ」**(Magouyrk、Q3 FY26 説明会、2026-03-10)。AI インフラは「30〜40%」が従来の説明で、Q3 FY26 に納入した AI 容量の実績は **32%** | **会話の逐語は未読。** 別の検索では 60〜80% の出典を確認できないとの結果が返った。GuruFocus 系の要約は「マルチクラウド DB が収益性に寄与」としか書かない。Oracle CEO ブログ(T1\*)は検索要約では粗利率の節まで読めなかった | [R4-13] TIKR T3、Finviz・AOL T3、ceointerviews.ai T4。反証側: [R4-04][R4-14] |
| 全社粗利率の参考値(算出) | GAAP の売上から 3 つの直接費(Cloud and software、Hardware、Services)を引いた値。**Q1 FY27: 60.0%**(算出: (19,345−7,733)÷19,345。直接費 7,733 = 6,400+281+1,052)。Q1 FY26: 67.3%(算出: (14,926−4,884)÷14,926)。Q4 FY26: 65.2%(算出: (19,184−6,672)÷19,184) | マルチクラウド DB 単独の粗利は開示なし。上記の「60〜80%」は全社 GAAP 粗利 60% の水準と同程度かそれ以上という算術上の位置関係だけが言える | 既存 R1 の費用表 T1\*(下記 7 節の修正提案 2 を参照) |
| オンプレ DB からクラウド DB へ移ると顧客 1 社あたりの Oracle 売上が何倍になるか | **欠損**。会社説明・アナリスト推定のどちらも見つからず。「4 倍」「5 倍」などの言い回しを探したが出典なし | — | 試した検索語: "customer moves to cloud Oracle revenue per customer multiple … 4 times OR three to four times OR 5x Catz Magouyrk"、"migrating on-prem Oracle support to Exadata cloud spends multiple times more … analyst" |
| 移行の誘因・値引き(参考) | **Oracle Support Rewards**: OCI の Universal Credits に使った **$1 につき 25 セント以上**、オンプレ保守料から値引き(インストールベース限定)。年間保守料は基本ライセンス費用の **22%** | 現在の条件(2026 年)は未確認。記事の日付は要約に出ず | [R4-23] TechTarget T3 |
| BYOL の場合の二重払い | BYOL(ライセンス持ち込み)ではクラウド移行後も別にサポート料が続く。License Included は ECPU 課金(Oracle が説明)。**売上の倍率は課金方式で変わるため、単一の倍率は置けない**(解釈) | 倍率は欠損のまま | [R4-24] Redress Compliance T4 |

---

## 3. 規模(インストールベース、保守売上、Exadata、クラウド移行率、見通し)

| 項目 | 値 | 性質・注意 | 出典・Tier |
|---|---|---|---|
| Oracle DB を使う大企業の割合 | **Fortune Global 100 の 97% が Oracle DB に依拠**(Oracle の説明) | 会社の主張。顧客数の絶対数ではない | [R4-25] Oracle 26ai ページ(検索要約)T1\* |
| DB 顧客の総数 | **欠損** | — | 試した検索語: "Oracle database installed base customers migrated percent …"、"Exadata installed base number of customers …" |
| Exadata の台数・顧客数 | **欠損**。Oracle の文書は「世界の数千の基幹系 Exadata サイト」と記述するだけ。Autonomous AI Database も「数千の顧客」との表現 | 数字は桁の目安のみ(定義不明) | [R4-26] Oracle の Exadata Cloud@Customer 資料 T1\*、[R4-27] Oracle Autonomous ページ T1\* |
| オンプレのライセンスとサポートの売上規模(会社全体) | FY25: 「クラウド・サービスとライセンス・サポート」計 **$44.0B**(Zacks 引用)。FY25 の Cloud(IaaS+SaaS)は $24.5B(既存 H5 の集計)。よって **ライセンス・サポート(全製品)≈ $19.5B**(算出: 44.0−24.5)。クロスチェック: FY25 の Software $24.724B(R1)から、クラウド/オンプレ・ライセンス $5.2B(Zacks)を引くと 19.5(算出) | **DB に限った保守売上は開示なし**(E-Business Suite、PeopleSoft、ミドルウェア等を含む)。$44.0B と $5.2B は Zacks 経由 T3 | [R4-28] Zacks/Stockanalysis T3、既存 R1・H5 |
| 直近の Software 売上 | FY26 **$24.5B(前年比 −1%)**(FY25 は $24.72B)。Q1 FY27 は $5.55B(R1、Q1 FY26 は約 $5.7B)。「Cloud license and on-prem license」は FY26 で約 $5.2B(Stockanalysis、前年比 −2.4%)だが、年度表記が Zacks の FY25 $5.2B と食い違い、列の整合が怪しい | 旧区分(License support / Cloud license)の FY26 実額は取得できず(R1 も同様) | [R4-29] Verdict T3、Stockanalysis T3、既存 R1 |
| クラウドへの移行実績 | **FY25 の 10-K: 過去 3 会計年度に、年間ライセンス・サポート契約を持つ顧客が Oracle Cloud へ移行したことで、年換算のクラウド・サービス売上が $4.3B 増えた。** 同 10-K は既存顧客基盤の移行が「初期段階」だと述べる。クラウド・サービスの売上構成比は FY23 32% → FY24 37% → FY25 43% | **「何 % が移行済みか」は分母が非開示のため欠損**。$4.3B は移行で増えたクラウド売上であり、失ったサポート売上は含まない | [R4-30] FY25 10-K(検索要約)T1\* |
| 移行の見通し(会社の発言) | Ellison は「他社クラウドに閉じ込められていた Oracle DB 利用者」の需要が背景だと述べる。Magouyrk は Q3 FY26 に「需要が供給を上回る」。1-A のとおり、Ellison は「数年、四半期ごとに大きく伸びる」と述べた(2025-09) | 移行率の目標・年次見通しは未確認 | [R4-07] Cloud Wars T3、[R4-01] T1\*、[R4-04] T1\* |
| アナリストの見方(移行のペース) | Substack の分析(T4)は「レガシーのライセンス事業は急速に食われておらず、移行は段階的」と解釈。Futurum(Q2 FY26)は「マルチクラウド DB の勢いと AI データ・プラットフォーム戦略で、OCI とパートナー・クラウドでの付随利用と定着が高まる」 | 数値の裏付けなし | [R4-22] T4、[R4-10] Futurum T3 |

---

## 4. AI Database(26ai)

| 項目 | 内容 | 出典・Tier |
|---|---|---|
| 発表 | **2025-10-14**、Oracle AI World(ラスベガス)で「Oracle AI Database 26ai」を発表。23ai の**長期サポート版後継**。2025 年 10 月のリリース更新(RU)を適用すれば 23ai から 26ai になる(フルアップグレード・再認証は不要と Oracle が説明) | [R4-25] Oracle ニュース T1\*、Oracle ブログ T1\* |
| 提供開始(オンプレ) | Linux x86-64 のオンプレ版は **2026-01** に一般提供(第三者のブログ。Oracle の一次確認なし) | [R4-31] jamsql 等 T4 |
| 機能 | **AI Vector Search**(HNSW インデックス、DML 対応は 26ai で改善との実務者の記述)、**Unified Hybrid Vector Search**(ベクトルとリレーショナル・テキスト・JSON・グラフ・空間の述語を 1 クエリで併用)、**Select AI Agent**(DB 内のエージェント枠組み。独自・既製ツール、REST、MCP サーバー対応)、MCP サーバー。InfoWorld や Futurum は「エージェントを DB の一級市民にする」と評価 | [R4-25] T1\*、[R4-32] InfoWorld T3、[R4-10] Futurum T3 |
| 先行予告 | Ellison は **2025-09-09(Q1 FY26)** に、AI Database のサービスを予告:「Gemini や ChatGPT などの LLM を Oracle DB の上で直接動かせる」 | [R4-01] Oracle プレスリリース T1\* |
| マルチクラウドとの関係 | Q4 FY26 の会社の指標名は **「Multicloud AI Database」**。Oracle のドキュメントも「Oracle AI Database@Azure」「Autonomous AI Database」と改称。Q1 FY27 の説明会では「Oracle AI Database を主要クラウドのすべてに置く」と発言 | [R4-05] T1\*、[R4-19] T1\*、[R4-06] T3 |
| 課金の仕方 | **AI Vector Search など高度な AI 機能は 26ai に追加費用なしで含まれる**。無料ティアあり(Oracle の説明)。第三者の価格解説は「Exadata では既存の DB ライセンスに対して追加 $0 のことが多い」(T4、参考値) → **AI 機能そのものは別売上として開示されず、DB の利用量(ECPU 課金)・クラウド移行・Exadata 販売を通じて収益化される形**(解釈) | [R4-25] T1\*、[R4-33] T4 |
| 採用事例・導入数 | **欠損。** ベクトル検索の本番導入社数、26ai の採用社数、AI Database 単独の売上は見つからず。Q1 FY27 の要約には「顧客のもとで **2,300 超の AI エージェントが本番稼働、前四半期比 +90%**」とあるが、(a) 何のエージェントか(DB 内か、アプリか)が不明、(b) 後続の検索では裏取りできず、単一系統 | [R4-06] Yahoo 系要約 T3。反証側: [R4-34](該当語なし) |
| 経営陣の説明(Q1 FY27 の声明) | 企業顧客の**大半**が自社の非公開データで AI を使い、AI エージェントで業務プロセスを自動化したがっている(Verdict の要約)。既存 S1 は「ほぼ全員(nearly all)」と記載しており、**「大半(most)」と「ほぼ全員」で語が異なる**。プレスリリースの逐語は未読 | [R4-35] Verdict T3、既存 S1 |
| Ellison の売上期待 | 「DB 事業は 5 年で $20B に届くか」との問いに前向き。理由は AI Database とマルチクラウド提携。「マルチクラウドだけでもほぼその額に寄与し得る」との報道(Cloud Wars の解釈を含む) | [R4-07] Cloud Wars T3、[R4-09] T3 |

---

## 5. 経営陣の数値目標とアナリストの見方

### 5-A. 経営陣の目標(FAM 2025-10 を中心に)

| 項目 | 値 | 出典・Tier |
|---|---|---|
| FY30 総売上 | $225B、非 GAAP EPS $21(アナリスト予想は売上 $198.4B、EPS $18.92) | [R4-11] Reuters 系報道・Cloud Computing News T3 |
| FY30 OCI(クラウドインフラ)売上 | $166B(総売上の約 75%) | [R4-11] T3 |
| FY30 DB(AI データベースと AI データ・プラットフォーム) | **$20B**(FY25 $2.4B から。年平均 約 53%)。「AI 向けのプライベート・データのベクトル化とマルチクラウド提携」が根拠と CreditSights が要約 | [R4-12] CreditSights T3、[R4-09] T3 |
| マルチクラウドの市場規模(TAM) | **欠損**。FAM 関連の報道・Cloud Wars の見出し・FAM 資料の検索要約のいずれにも、マルチクラウド DB の TAM 数値は出てこなかった | 試した検索語: "financial analyst meeting 2025 multicloud database revenue target fiscal 2030"、"…AI Database AI Data Platform $20 billion…" |
| 成長見通し(定性) | 「数年、四半期ごとに大きく伸びる」(Ellison、2025-09)。「需要が供給を上回る」(Magouyrk、2026-03) | [R4-01][R4-04] T1\* |
| 供給計画 | 3 社に計 71 〜 72 の拠点。Q1 FY27 に Azure・AWS の計画拡張を完了(70 リージョン・119 AZ) | [R4-01][R4-02][R4-06] |
| FAM 資料そのもの | Oracle の FAM 資料 PDF(Magouyrk 分)は検索結果に URL が出たが**未読** | https://www.oracle.com/a/ocom/docs/corporate/financial-analyst-meeting-2025-magouyrk.pdf |

### 5-B. アナリスト・調査会社の見方(数値のあるものは少ない)

| 見方 | 内容 | 出典・Tier |
|---|---|---|
| Futurum(Q2 FY26) | マルチクラウド DB の勢いと AI データ・プラットフォーム戦略が、OCI とパートナー・クラウドでの付随利用と定着を高める位置にある | [R4-10] T3 |
| Futurum(AI World 2025) | 「データベースは再び AI 宇宙の中心か」と題し、DB 内のエージェント枠組みをエージェント AI のライフサイクルを DB エンジンに組み込むものと評価 | [R4-10] T3 |
| dbInsight(Tony Baer、InfoWorld 引用) | AI エージェントを DB 内の一級市民にする | [R4-32] T3 |
| Zacks(Q1 FY27 後) | 「DB 事業は長期に粗利率を維持できるか」。従量課金は入口価格を下げ、パートナー施設での配備は資本集約度を高める。全社の非 GAAP 営業利益率は約 42%。Capex $28.5B、フリーキャッシュフロー約 −$5B | [R4-15] Yahoo/Zacks、Globe and Mail T3 |
| Substack の分析 | 仮説として、マルチクラウドは資本を土地・建物ではなく計算・ストレージに振り向ける。既存のサポート基盤をクラウドへ移すのを早める。レガシー・ライセンスは急速に食われない | [R4-22] T4 |
| 証券会社(Morgan Stanley、UBS、Jefferies、BofA 等)の推定 | **欠損**。マルチクラウド DB の売上規模・Azure 比率・粗利率の個別推定は見つからず(検索 1 回) | 試した検索語: "multicloud database analyst estimate Q1 FY27 Morgan Stanley OR UBS OR Jefferies OR Bank of America multicloud database revenue size Azure share margin" |

---

## 6. 出典間の食い違い(事実の指摘のみ)

| # | 項目 | 食い違い | 所見 |
|---|---|---|---|
| 1 | 「予約 +325%」 | 既存 S1 は Q4 FY26 のマルチクラウド予約 +325%(AlphaSense、T4)。今回の検索では **+325% は Q3 FY26 の RPO $553B の前年比**。Q4 FY26 は RPO $638B、+363% | S1 の値は RPO の誤帰属の可能性が高い。マルチクラウド単独の予約成長率は欠損 |
| 2 | Q1 FY27 の成長率 | 既存 H1 は +531%(備考 10)。今回、+531% は **Q3 FY26**(Oracle プレスリリース)と確認。Q1 FY27 は +353% | 既存 R2 の指摘どおり H1 の修正が必要 |
| 3 | +353% と顧客 +180% の一次性 | 複数の説明会要約で一致するが、Oracle のプレスリリース(Verdict、Benzinga、Zacks の要約)の抜粋には現れない | 説明会の発言と推定される。逐語は未読 |
| 4 | 粗利率「60〜80%」 | 検索 1(TIKR、Finviz、AOL、ceointerviews.ai)は Magouyrk の発言と報告。検索 2(同じ主題)は「この数字の出典は見つからない」。GuruFocus 系は「30〜40% の AI 資産」と「32%」だけ記載 | 二次媒体の一致はあるが、Oracle の原文は未確認。**逐語確認が必要** |
| 5 | Azure のリージョン数 | 既存 R2: 28(単一出典・日付不明)/ Microsoft(2026-01): 31 または「30 超」/ Oracle の CEO ブログと Oracle の一覧(2026-03 頃): 33 | 時期の違いと見られる。最新側の 33 が妥当(算出: Oracle の一覧の個数) |
| 6 | Google のリージョン数 | Oracle の CEO ブログ(2026-03): 14 / DCD(日付不明): 約 15(+2 予定) | 時点差の可能性 |
| 7 | AWS のリージョン数 | Oracle の CEO ブログ(2026-02 末): 8、目標 22 / AWS 発表: 2026-02 に 7、2026-04 に 12、2026-05-29 に 20 | 7 と 8 は日付差の可能性。目標 22 に対し AWS の発表は 20(2026-05-29 時点) |
| 8 | 総拠点数 | 計画: 71(Q1 FY26)→ 72(Q2 FY26、「データセンター」)/ 実績: 70 リージョン・119 AZ(Q1 FY27) | 単位(データセンター、リージョン)の違い。33+15+22=70 は成立するが未確認 |
| 9 | 1,529% の定義 | Oracle のプレスリリースは「multicloud database **revenue**」。FAM 資料の表は「MultiCloud **Consumption** Growth」 | 売上と消費量が同じか不明 |
| 10 | $20B の範囲 | Cloud Wars の問答では「DB 事業」が 5 年で $20B / Cloud Computing News と CreditSights は「AI データベースと AI データ・プラットフォーム」が FY30 に $20B | 同じ目標か、範囲が異なるかは未確認 |
| 11 | 「AI の企業顧客」の言い回し | S1: 「ほぼ全員」/ Verdict: 「大半」 | 逐語未読 |
| 12 | FY25 の $2.4B | FAM の基数 FY25 $2.4B / io-fund の「Q4 の年換算 $2.6B」/ S4 の「Q1 FY26 年換算約 $2.8B」 | 順に上昇する関係で矛盾はないが、$2.4B が何の売上かの定義(マルチクラウドを含むか)は不明 |
| 13 | Cloud Database(IaaS)+35% | Oracle のプレスリリースでは **Q3 FY26** の値。既存 H1 は Q1 FY27 の値と記載 | 時点が割れている(既存 R2 の指摘どおり)。Q1 FY27 の値は今回も未確認 |
| 14 | 経営陣の肩書 | 説明会の要約で CEO の表記が割れる(Magouyrk、Sicilia が併記、「Co-CEO」の表記も)。CFO は Maxson | 呼称の確認が必要(本調査の数値には影響しない) |

---

## 7. 既存調査への修正提案

1. **S1・H1 の値**: 上記 6 節の食い違い 1・2・13 のとおり修正または注記。
2. **R1 の費用表の誤記の可能性**: Q1 FY27 の「C&S + HW + Services 合算」は **7,733**(算出: 6,400+281+1,052)であり、R1 の本文は「8,733」と記載している。営業費用合計 12,617(=7,733+1,811+2,401+376+202+94)と一致するのは 7,733 の方。粗利率 60.0% の算出にも 7,733 を使った。
3. **R2 のリージョン**: Azure 28 → 33(Oracle CEO ブログ、2026-03)、Google 約 15 → 14(同)に更新が望ましい。70 リージョンは単一系統の要約のままで確認度は変わらない。

---

## 8. 未確認事項と試した検索語

| # | 欠損・未確認 | 試した検索語・状況 |
|---|---|---|
| 1 | マルチクラウド DB の売上の絶対額・年換算、Azure / Google / AWS の内訳 | "multicloud database revenue run rate billion estimate analyst Database@Azure AWS Google annualized"(extended)ほか。見つからず |
| 2 | マルチクラウド DB の予約・受注残の成長率 | "Oracle Q4 fiscal 2026 … multicloud database revenue 404% bookings 325%"。+325% は RPO と一致 |
| 3 | Oracle と各ハイパースケーラーの取り分、収益の総額・純額計上、機器の会計上の所有者 | "Oracle 10-K fiscal 2026 multicloud arrangements … colocation fee revenue recognized marketplace"、"hyperscaler revenue share fee Oracle keeps revenue …"。10-K の URL は出たが本文は読めず |
| 4 | マルチクラウド DB の粗利率の Oracle 原文(60〜80%) | "multicloud database gross margin 60% to 80% Magouyrk"、"From the Q3 Earnings Call … gross margin"。Oracle の CEO ブログは粗利率の節まで読めず |
| 5 | オンプレ→クラウド移行時の顧客あたり売上の倍率 | 2 回(会社説明・アナリストとも出典なし) |
| 6 | DB の顧客数、Exadata の台数・顧客数、クラウド移行率(%)、DB 単独の保守売上 | 2 回(Exadata installed base、10-K support revenue)。Oracle の語は「数千」のみ、97% of Fortune Global 100 のみ |
| 7 | マルチクラウドの TAM、マルチクラウド単独の FY30 目標 | FAM 関連 2 回。FAM 資料 PDF は未読 |
| 8 | 26ai の採用社数、ベクトル検索の本番導入、AI Database 単独の売上、AI Data Platform の価格、Autonomous AI Database での追加費用の有無 | 3 回。見つからず。2,300 エージェントの裏取りも不成立 |
| 9 | 証券会社のマルチクラウド DB の個別推定 | 1 回。見つからず |
| 10 | Q1 FY27 の Oracle Cloud Database(IaaS)成長率、Q1 FY27 の Software の内訳(ライセンス・サポート) | 見つからず |
| 11 | Database@Azure、@AWS、@Google の GA 日(Azure、AWS)。Google の GA は 2024-09(要約) | Azure と AWS の GA 日は今回未取得(欠損) |
| 12 | Q4 FY25 のマルチクラウド成長率(前期比 +115% という言及が検索要約に 1 回出たが、出典が特定できず) | 未採用 |
| 13 | 全ての Oracle 原文(プレスリリース、CEO ブログ、10-K、説明会逐語、FAM 資料) | 検索要約経由のみ。原本照合は未了 |

---

## 9. 出典一覧

| ID | 内容 | URL | 日付 | Tier |
|---|---|---|---|---|
| R4-01 | Oracle Q1 FY26 決算プレスリリース(Ellison: 1,529%、71 拠点、AI Database 予告) | https://www.oracle.com/news/announcement/q1fy26-earnings-release-2025-09-09/ 、https://investor.oracle.com/investor-news/news-details/2025/Oracle-Announces-Fiscal-Year-2026-First-Quarter-Financial-Results/default.aspx | 2025-09-09 | T1\* |
| R4-02 | Oracle Q2 FY26 決算プレスリリース(+817%、72 拠点) | https://www.oracle.com/news/announcement/q2fy26-earnings-release-2025-12-10/ 、https://seekingalpha.com/pr/20335876 | 2025-12-10 | T1\* |
| R4-03 | Oracle Q3 FY26 決算プレスリリース・8-K Ex99.1(+531%、Cloud Database(IaaS)+35%) | https://www.sec.gov/Archives/edgar/data/1341439/000119312526100148/orcl-ex99_1.htm 、https://www.oracle.com/lt/news/announcement/q3fy26-earnings-release-2026-03-10/ | 2026-03-10 | T1\* |
| R4-04 | Oracle CEO ブログ「From the Q3 Earnings Call: Scaling Multicloud Database and AI Infrastructure to Meet Surging Demand」(Microsoft 33、Google 14、AWS 2→8、目標 22) | https://blogs.oracle.com/ceo/from-the-q3-earnings-call | 2026-03 頃(日付は要約に出ず) | T1\* |
| R4-05 | Oracle Q4 FY26 決算プレスリリース(Multicloud AI Database +404%) | https://www.oracle.com/news/announcement/q4fy26-earnings-release-2026-06-10/ 、https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/default.aspx | 2026-06-10 | T1\* |
| R4-06 | Q1 FY27 説明会の要約・逐語(+353%、顧客 +180%、70 リージョン・119 AZ、Interconnect for AWS、2,300 エージェント) | https://www.alphaspread.com/security/nyse/orcl/investor-relations/earnings-call/q1-2027 、https://finance.yahoo.com/markets/stocks/articles/oracle-q1-earnings-call-highlights-230310387.html 、https://quartr.com/events/oracle-corporation-orcl-q1-2027_3gvkOKJp 、https://www.tradingkey.com/news/transcripts/262162053-tradingkey 、https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/ 、https://www.cnbc.com/2026/09/10/oracle-orcl-q1-earnings-report-2027.html | 2026-09-10 〜 11 | T3 |
| R4-07 | Cloud Wars「Larry Ellison sees Oracle multicloud boom as Google, Amazon customers jump aboard」(Azure が大半、$20B の問答) | https://cloudwars.com/cloud/larry-ellison-sees-oracle-multicloud-boom-as-google-amazon-customers-jump-aboard/ | 2025-09 頃(日付は要約に出ず) | T3 |
| R4-08 | io-fund「Can Oracle Become the Next $1 Trillion AI Stock?」(クラウド DB の年換算 $2.6B) | https://io-fund.com/ai-stocks/oracle-stock-1t-outlook | 日付不明 | T3 |
| R4-09 | Cloud Computing News「Oracle bets big on cloud as it targets $225b in sales by 2030」(DB $20B、FY25 $2.4B、FY26 $3B) | https://www.cloudcomputing-news.net/news/oracle-bets-big-on-cloud-as-it-targets-225b-in-sales-by-2030/ | 2025-10 | T3 |
| R4-10 | Futurum(Q2 FY26 / AI World 2025) | https://futurumgroup.com/insights/oracle-q2-fy-2026-cloud-grows-capex-rises-for-ai-buildout/ 、https://futurumgroup.com/insights/oracle-ai-world-2025-is-the-database-the-center-of-the-ai-universe-again/ | 2025-10 〜 12 | T3 |
| R4-11 | Reuters 系「Oracle expects cloud sales of $166 billion by 2030」 | https://de.tradingview.com/news/reuters.com%2C2025%3Anewsml_L6N3VX11P%3A0-oracle-expects-cloud-sales-of-166-billion-by-2030-as-business-expands 、https://sundayguardianlive.com/feature/oracle-expects-cloud-sales-of-166-billion-by-2030-as-business-expands-2-156347/ | 2025-10 | T3 |
| R4-12 | CreditSights「Oracle: Top 10 Takeaways from 2025 Analyst Meeting」、Cloud Wars「Oracle on Fire! FY30 Rev. $225B!」 | https://know.creditsights.com/insights/oracle-top-10-takeaways-from-2025-analyst-meeting/ 、https://cloudwars.com/cloud-wars-minute/oracle-on-fire-fy30-rev-225b/ | 2025-10 | T3 |
| R4-13 | TIKR、Finviz、AOL、ceointerviews.ai(Magouyrk: マルチクラウド DB の粗利率 60〜80%) | https://www.tikr.com/blog/oracle-stock-what-the-q3-earnings-beat-says-about-orcls-path-to-624 、https://finviz.com/news/336098/oracle-co-ceo-clay-magouyrk-explains-whats-holding-back-the-companys-data-center-windfall-the-major-factor-limiting-even-stronger-profits-is 、https://www.aol.com/articles/oracle-co-ceo-clay-magouyrk-043017875.html 、https://ceointerviews.ai/quote/multicloud-database-revenue-grew-531-yearoveryear-ai-infrastructure-MTA1MzgwNg/ | 2026-03-10 〜 | T3 / T4 |
| R4-14 | Verdict「Oracle Q3 FY26 results」、Yahoo/GuruFocus の Q3 FY26 説明会要約 | https://www.verdict.co.uk/oracle-q3-fy26-results/ 、https://finance.yahoo.com/news/oracle-corp-orcl-q3-2026-030115242.html | 2026-03 | T3 |
| R4-15 | Zacks「Can Oracle's Database Business Sustain Margins over the Long Term?」 | https://finance.yahoo.com/markets/stocks/articles/oracles-database-business-sustain-margins-100700369.html 、https://www.theglobeandmail.com/investing/markets/stocks/ORCL/pressreleases/4927407/can-oracles-database-business-sustain-margins-over-the-long-term/ | 2026-09 頃 | T3 |
| R4-16 | Microsoft Tech Community「Oracle Database@Azure」(31 リージョン、30 超)。Oracle の Azure 一覧(33) | https://techcommunity.microsoft.com/blog/oracleonazureblog/-/4479671 、https://blogs.oracle.com/cloud-infrastructure/oracle-multicloud-whats-new-blog | 2026-01 頃 | T1\*(提携先 / Oracle) |
| R4-17 | Google Cloud の Oracle Database 提供リージョン、DCD「Oracle Database@Google Cloud now generally available」 | https://docs.cloud.google.com/oracle/database/docs/regions-and-zones 、https://datacenterdynamics.com/en/news/oracle-databasegoogle-cloud-now-generally-available | 2024-09(GA) | T1\* / T3 |
| R4-18 | Microsoft Learn「Overview - Oracle AI Database@Azure」 | https://learn.microsoft.com/en-us/azure/oracle/oracle-db/database-overview | 日付不明 | T1\*(提携先) |
| R4-19 | Oracle ドキュメント「Oracle AI Database@Azure」、サービスページ(価格は OCI の Exadata と同じ、MACC 算入) | https://docs.oracle.com/en-us/iaas/Content/database-at-azure/oaa.htm 、https://www.oracle.com/cloud/azure/oracle-database-at-azure/services/ | 日付不明 | T1\* |
| R4-20 | Oracle ドキュメント「Private Offer」(Database@AWS: AWS 経由の請求、AWS コミットに算入) | https://docs.oracle.com/en-us/iaas/Content/database-at-aws/oaaws-gs-private-offer.htm | 日付不明 | T1\* |
| R4-21 | AWS ドキュメント「What is Oracle Database@AWS?」「Onboarding」、AWS Database Blog | https://docs.aws.amazon.com/odb/latest/UserGuide/what-is-odb.html 、https://docs.aws.amazon.com/odb/latest/UserGuide/setting-up.html 、https://aws.amazon.com/blogs/database/getting-started-with-oracle-databaseaws-a-complete-onboarding-guide | 日付不明 | T1\*(提携先) |
| R4-22 | Substack「Beyond Hyperscalers: Oracle's Bet to Dominate the Era of Data」 | https://equityanalysiseng.substack.com/p/beyond-hyperscalers-oracles-bet-to | 日付不明 | T4 |
| R4-23 | TechTarget「Oracle offers on-premise support discount for cloud buyers」 | https://www.techtarget.com/it-infrastructure/news/252502870/Oracle-offers-on-premise-support-discount-for-cloud-buyers | 日付不明 | T3 |
| R4-24 | Redress Compliance「Oracle Autonomous Database Licensing: UCC and BYOL Options」 | https://redresscompliance.com/oracle-autonomous-database-licensing-in-the-cloud/ | 日付不明 | T4 |
| R4-25 | Oracle「Oracle AI Database 26ai Powers the AI for Data Revolution」、ブログ、製品ページ(97% of Fortune Global 100 を含む) | https://www.oracle.com/news/announcement/ai-world-database-26ai-powers-the-ai-for-data-revolution-2025-10-14/ 、https://blogs.oracle.com/database/oracle-announces-oracle-ai-database-26ai 、https://www.oracle.com/database/ai-native-database-26ai/ | 2025-10-14 | T1\* |
| R4-26 | Oracle「Exadata Database Service on Cloud@Customer X11M」データシート(「数千の基幹系 Exadata サイト」) | https://www.oracle.com/a/ocom/docs/engineered-systems/exadata/exadb-cc-x11m-ds.pdf | 日付不明 | T1\* |
| R4-27 | Oracle「Autonomous AI Database」ページ | https://www.oracle.com/autonomous-database/ | 日付不明 | T1\* / T4 |
| R4-28 | Verdict(FY26 Software $24.5B)、Stockanalysis(Cloud license and on-prem license)、Zacks(FY25 の $44.0B、$5.2B) | https://www.verdict.co.uk/?p=402027 、https://stockanalysis.com/stocks/orcl.prd/financials/metrics/ | 2026-06 〜 | T3 |
| R4-29 | 同上(Software の前年比 −1%) | 同上 | 2026-06 | T3 |
| R4-30 | Oracle FY2025 10-K(移行による年換算クラウド売上 +$4.3B、クラウド比率 43/37/32%)。FY2026 10-K の URL も出たが本文は未読 | https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/orcl-20250531.htm 、https://www.sec.gov/Archives/edgar/data/0001341439/000119312526277521/orcl-20260531.htm | FY25: 2025-06 提出 | T1\* |
| R4-31 | jamsql「What's New in Oracle 26ai (and Where 23ai Went)」ほか実務者ブログ | https://jamsql.com/blog/2026-08-27-whats-new-oracle-26ai/ | 2026-08-27 | T4 |
| R4-32 | InfoWorld「Oracle targets agentic use cases with AI Database 26ai」 | https://www.infoworld.com/article/4072128/oracle-targets-agentic-use-cases-with-ai-database-26ai.html | 2025-10 | T3 |
| R4-33 | 第三者の価格解説(Exadata でのベクトル検索の追加費用)、Forbes(26ai とエンタープライズ AI のデータ問題) | https://www.forbes.com/sites/stevemcdowell/2026/01/27/how-oracle-database-26ai-addresses-enterprise-ai-data-paradox/ | 2026-01-27 | T3 / T4 |
| R4-34 | 2,300 エージェントの裏取りを試みた検索(該当なし) | — | — | — |
| R4-35 | Verdict「Oracle Q1 FY27 results」(企業顧客が非公開データで AI を使いたい) | https://www.verdict.co.uk/oracle-q1-fy27-results/ | 2026-09 | T3 |
| 既存 | 既存調査 S1、S4、H4、H5、R1、R2、R3 | `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research/` と `/data/`、`/research2/` | — | — |

---

## 10. 検索ログ(28 回 / 上限 28 回)

| # | モード | 目的 |
|---|---|---|
| 1 | extended | Q1 FY27 説明会(+353%、顧客 +180%、リージョン) |
| 2 | standard | Q4 FY26(+404%、予約 +325% の確認) |
| 3 | extended | Q1 FY27 の AI Database・非公開データの発言 |
| 4 | standard | Q1 FY27 プレスリリース |
| 5 | standard | Q2 FY26(+817%) |
| 6 | standard | Q3 FY26(+531%、リージョン、粗利率) |
| 7 | standard | 粗利率 60〜80% の確認 |
| 8 | standard | Q1 FY26(+1,529%) |
| 9 | extended | 絶対額・年換算額 |
| 10 | standard | FAM 2025-10 の目標 |
| 11 | extended | FAM の DB $20B |
| 12 | standard | Cloud Wars の Ellison 発言 |
| 13 | extended | Azure の経済性・Exadata の所有 |
| 14 | standard | AWS の課金・確約支出 |
| 15 | extended | 10-K のマルチクラウド取引の会計 |
| 16 | extended | オンプレ→クラウドの顧客あたり売上の倍率 |
| 17 | extended | インストールベース・移行率 |
| 18 | standard | 10-K のサポート売上 |
| 19 | extended | 26ai の機能・提供開始・課金 |
| 20 | extended | Q1 FY27 の AI Database 関連発言 |
| 21 | standard | Q1 FY27 プレスリリースの逐語 |
| 22 | standard | Azure・Google のリージョン数 |
| 23 | extended | アナリストの見方 |
| 24 | extended | Q4 FY26 説明会の DB 関連 |
| 25 | extended | Oracle CEO ブログ(Q3 FY26) |
| 26 | extended | Exadata のインストールベース |
| 27 | extended | 26ai の採用・価格 |
| 28 | extended | 収益分配・顧客あたり売上の倍率(再試行) |
