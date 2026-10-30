# U4 Oracle 資金調達と FCF ブリッジ(事実と出典のみ)

調査日: 2026-10-30 / 方法: WebSearch(standard / extended)の要約。sec.gov・investor.oracle.com・q4cdn・prnewswire・stockanalysis と、roic.ai・thenextweb・wsau の本文は直接読めなかった(WebFetch は名前解決できず)。このため全ての数値は「検索要約が引用した二次情報」であり、一次資料(8-K Ex.99.1、10-Q、スライド、トランスクリプト)での照合は未了。

凡例: [一次引用] = 検索要約が Oracle の 8-K / 決算資料の文言として引用したもの。[二次] = 報道・ブログ・アナリスト要約。

---

## 1. FCF の定義

| 項目 | 内容 | 出典 | 区分 |
|---|---|---|---|
| FCF の式 | 営業CF − capex(capex は投資CF計上額)。過去の 10-Q(FY2019 11月期、FY2021 8月期など)で同じ 2 行構成。FY21 8月期の例: 営業CF 15,325百万 − capex 2,761百万 = FCF 12,564百万 | sec.gov 10-Q 各期(検索要約) https://www.sec.gov/Archives/edgar/data/1341439/000156459021047772/orcl-10q_20210831.htm | 一次(過去 10-Q の要約) |
| Q1 FY27 の適用 | 営業CF 約 231億ドル − capex 285億ドル = FCF −54億ドル(Oracle の定義=営業CF−capex と明記) | sec-api.io https://sec-api.io/insights/oracle-corporation-orcl-financial-and-ratio-analysis-q1-fy2027-filings-cloud-backlog-debt-and-capital-spending-scenarios-to-fy2030 | 二次 |
| 顧客の前払いの扱い | 営業CFに含まれる。Q1 FY27 の営業CF 231億ドルのうち 113.6億ドルが「significant financing component を持つ顧客前払い」(前受収益の増加)。前払いを除く営業CFは 117億ドル | sec-api.io(上記)、Reuters 系報道(「capex 285億ドルのうち約 113.6億ドルは顧客前払いで賄われた」)https://www.stocktitan.net/articles/oracle-stock-investor-day-2026-20-billion-funding-cap 周辺の報道要約 | 二次 |
| ファイナンス・リース元本返済 | FCF の式に含まれない(財務CF区分)。ただしこれは「式が capex しか引かない」ことからの検索要約側の推論で、Oracle が「除く」と明記した文言は not found | 10-Q 要約(同上) | 推論(未確認) |
| 純現金 capex(別指標) | 「capex − capex に関連する短期ファイナンスCF − significant financing component を持つ顧客前払い」。非 GAAP。FY27 は ≤ 700億ドル(総 capex 900〜950億ドル)。Q1 FY27 は 180億ドル(総 285億ドル) | Oracle 8-K Ex.99.1 の定義文言として検索要約が引用(https://www.sec.gov/Archives/edgar/data/0001341439/000119312526435853/d75538dex991.htm)、Q1 FY27 スライド https://s23.q4cdn.com/440135859/files/content_files/Q1-FY27-Oracle-Earnings-Slides.pdf の「18B」(検索要約) | 一次引用 |
| ベンダー金融・GPU リースの扱い(FCF 上) | not found(FCF 定義の中での明示なし)。純債務の定義には「借入、ベンダー金融、オペレーティングおよびファイナンス・リース負債 − 現金・有価証券」が含まれる | 8-K Ex.99.1(検索要約)。Morgan Stanley(Sanjit Singh)「ベンダー金融は純債務に算入される」https://www.tipranks.com/news/article/now-comes-the-hard-part-says-morgan-stanley-about-oracle-stock | 一次引用 / 二次 |
| Investor Day での FCF 定義の説明 | not found(検索結果はいずれも「FCF の定義は示されていない」。FY29 の $30B+ が GAAP/非 GAAP か、前払い・ベンダー金融の控除後かも不明) | 複数 | - |
| 会社の文言 | 「vendor financing, customer-provided hardware and customer prepayments are expected to reduce upfront cash requirements through the transition to positive free cash flow」 | 8-K Ex.99.1 / https://investor.oracle.com/investor-news/news-details/2026/Oracle-Investor-Day-2026-Accelerating-Value-Creation/default.aspx(検索要約) | 一次引用 |

---

## 2. 資金の外部化の仕組み

### 2-1 顧客の前払い・BYOH
| 項目 | 数値 | 日付 | 出典 / 発言者 | 区分 |
|---|---|---|---|---|
| 前払い+顧客持込ハードの合計(大型 AI 契約) | 750億ドル(「prepaid and customer supplied hardware portions of our large AI contracts now total $75 billion」) | Q4 FY26 決算(2026-06-10) | Oracle 8-K Ex.99.1 https://www.sec.gov/Archives/edgar/data/0001341439/000119312526265848/orcl-ex99_1.htm、CEO Clay Magouyrk | 一次引用 |
| 同四半期の新規 AI インフラ契約 | 670億ドル、過半が BYOH または前払い | 2026-06 | Magouyrk(erp.today 要約)https://erp.today/oracle-q4-2026-earnings-ai-cloud-backlog-funding/ | 二次 |
| BYOH 契約の利益率 | 「no degradation in margin」(finsee.ai は「equal or better」と強い表現=不一致。後者は原文より強い可能性) | 2026-06 | Magouyrk | 二次 |
| BYOH の比率(契約額・capex 比) | not found(RPO 6,640億ドル中の BYOH 割合の開示は見つからず) | - | - | - |
| Q1 FY27 の顧客前払い | 113.6億ドル(営業CFに算入) | 四半期末 2026-08-31(発表 2026-09-10) | sec-api.io / Reuters 系 | 二次 |
| 前払い累計 | 営業CF 469億ドル(LTM)に前払い 160億ドルを含み、前受収益 308億ドル、との分析あり。期間(FY26+Q1 FY27 か)は要確認 | 2026-08 | sec-api.io(検索要約) | 二次・期間不明 |
| 前受収益の残高 | 不一致: beancount.io は 99.16億→146.86億ドル(5/31→8/31)、sec-api.io 系は 308億ドル。定義(流動のみか全体か)が違う可能性。10-Q の流動/非流動内訳は not found | 2026-05/08 | https://beancount.io/blog/2026/09/13/oracle-fy2027-q1-earnings-analysis | 二次・不一致 |
| FY27 の「前払い+タイミング効果」 | 200〜250億ドル(総 capex 900〜950億ドルと純現金 capex ≤ 700億ドルの差) | 2026-06-10 | CFO Hilary Maxson(Reuters/Nasdaq 要約)https://www.nasdaq.com/articles/oracle-q4-earnings-call-highlights | 二次 |
| JPMorgan の見方 | 新規契約は主に前払いまたは BYOH で追加現金不要、純現金 capex 上限 700億ドル=200〜250億ドルの前払い・サプライヤー金融の相殺 | 2026-09 | JPMorgan(erp.today 要約)https://erp.today/oracle-q1-fy27-results-664b-backlog-ai-contracts/ | 二次 |
| Michael Burry の批判 | 「顧客を貸し手に変える」「financing gross-up, manufactured by the structure rather than by usage」 | 2026-09 | erp.today(要約) | 二次(批判) |
| OpenAI 集中度 | RPO の約半分が OpenAI(erp.today)。OpenAI は稼働後に支払い開始との報道 | 2026-09 | erp.today / 各報道 | 二次 |

### 2-2 ベンダー金融・GPU リース・SPV
| 項目 | 内容 | 日付 | 出典 | 区分 |
|---|---|---|---|---|
| ベンダー金融(NVIDIA 等)の額 | not found(延払い額・条件の開示なし)。Morgan Stanley の 1GW 例: ベンダー金融 70% なら初期 2 年の資金負担が約 370億→約 180億ドル | 2026-10-28/29 | MS(TipRanks 経由の検索要約)https://www.tipranks.com/news/article/now-comes-the-hard-part-says-morgan-stanley-about-oracle-stock | 二次(アナリスト例示) |
| ベンダー金融の混合比率 | 会社は内訳を示していない(MS の指摘) | 2026-10 | 同上 | 二次 |
| GPU リース SPV | Apollo・Goldman と交渉中。投資家が出資する別会社がチップを購入し Oracle にリースする、バランスシート外の枠組み。1GW のデータセンター用ハード。金額は報道なし。成約の確認なし | 2026-10 上旬 | WSJ(二次要約)https://www.tikr.com/blog/oracle-courts-apollo-and-goldman-for-ai-chip-financing-as-debt-tops-169-billion | 二次・交渉段階 |
| TD Cowen のチャネルチェック | NVIDIA が一部データセンター・リースに信用補完している可能性。両社とも未確認 | 2026 年内(事前) | https://www.tikr.com/blog/oracle-is-down-more-than-a-third-in-2026-even-as-td-cowen-flags-possible-nvidia-support-heres-where-the-stock-could-go-by-2031 | 二次・未確認 |
| 会社のコメント | 「オフバランス」の構造に関する Oracle の公式説明は not found | - | - | - |

### 2-3 データセンター開発事業者・プロジェクトファイナンス
| 案件 | 額 | 日付 | 内容 | 出典 | 区分 |
|---|---|---|---|---|---|
| Vantage(テキサス・ウィスコンシン) | 総額約 380億ドル(テキサス 232.5億、ウィスコンシン 147.5億)。JPMorgan・MUFG が主幹事、Wells Fargo・BNP・Goldman・SMBC・SocGen が参加。期間 4 年(+1 年延長 2 回)、基準金利+約 2.5%、建設中は利払いのみ、稼働後に償却。テナントは Oracle(OpenAI 向け) | 2025-10 の Bloomberg 報道 | 開発事業者が借り手、Oracle はリース借り手 | https://datacenterdynamics.com/en/news/jpmorgan-chase-and-mitsubishi-ufj-lead-38bn-debt-package-for-oracle-linked-data-centers-report/ | 二次 |
| 同上のシンジケーション | 6 か月超を要し、残り 10億ドル未満を売却中。銀行が単一取引先のエクスポージャー限界に近づいたとの報道 | 2026 年(時期は要確認) | 売却難航 | https://aiweekly.co/alerts/banks-still-working-off-oracles-38b-ai-data-center-loan | 二次 |
| ミシガン州 Saline(Related Digital) | 約 160億ドルのキャンパス。2025-12 に Blue Owl の離脱報道(Related Digital は「Blue Owl が撤退は事実無根」と反論)。2026-04 に Related Digital と Blackstone が資金調達完了: 株式+PIMCO 運用ファンド主導の固定金利長期債。BofA が 140億ドルの債券を販売との報道 | 2025-12 / 2026-04 | 開発事業者主導 | https://www.datacenterdynamics.com/en/news/blue-owl-opts-not-to-fund-oracles-10bn-michigan-data-center/ ほか | 二次 |
| Abilene(Crusoe / Blue Owl) | Blue Owl が Crusoe のアビリーン・キャンパス(Oracle にリース)を支援。債務額は not found | - | 同上検索結果 | 二次 |
| 各四半期(2026 年)ごとの外部化額 | 四半期別の一覧は not found。判明分: Q2 FY26(2025-11 期)capex 120億・FCF −100億、Q1 FY27 前払い 113.6億・純現金 capex 180億 | - | - | - |

### 2-4 会社自身の資本調達
| 項目 | 額 | 日付 | 出典 |
|---|---|---|---|
| 2026 年暦年の調達計画 | 450〜500億ドル、株式と債務ほぼ半々。債券(Goldman 主幹事)+強制転換優先株+ATM 最大 200億ドル(Citigroup) | 2026-02-01 | https://www.theregister.com/2026/02/02/oracle_cloud_expansion_investment_plan/ ほか(二次) |
| FY27 の調達 | 約 400億ドル(債務+株式、前述 ATM 200億ドル含む) | 2026-06-10 | CFO Maxson(要約) |
| ATM 200億ドル | Q1 FY27(〜2026-08-31)に完了 | 2026-09 | https://storagenewsletter.com/2026/09/23/oracle-fiscal-1q27-financial-results(二次) |
| Investor Day の追加調達上限 | FY27〜FY30 の新規資本市場調達は 200億ドル(株式 100億+総額債務 100億)、借換え除く。Maxson「the final amount needed to fund the remainder of this cycle」。ベンダー金融・顧客持込・顧客前払いは上限の対象外(Financefeeds) | 2026-10-28 | 8-K Ex.99.1(一次引用)、Maxson(roic.ai / 報道)。不一致: 200億ドルの時期を Reuters 系は「FY27 の残り」と書くが、Oracle の文言は「FY27〜FY30」 |

---

## 3. capex の経路

| 項目 | 数値 | 出典 / 発言者 | 区分 |
|---|---|---|---|
| FY26 実績 | capex 557億ドル(FY25 は 212億ドル)、営業CF 320億ドル、FCF −237億ドル | Q4 FY26 発表 https://s23.q4cdn.com/440135859/files/doc_earnings/2026/q4/earnings-result/4q26-pressrelease-final.pdf(検索要約) | 一次引用 |
| FY27 会社見通し | 総 capex 900〜950億ドル、純現金 capex 約 700億ドル(≤700億)。Q1 FY27 でも据置き | Maxson(2026-06-10)、Q1 FY27(2026-09-10) | 二次 |
| FY27 のコンセンサス | 当時 676.6億ドル(LSEG)。別の報道は 919億ドル(+65%) | LSEG / 報道 | 二次・不一致 |
| FY27〜FY28 | 「peak capex」、FY29 は「step-down」。FY28 の会社数値は not found | 8-K Ex.99.1(一次引用)https://investor.oracle.com/investor-news/news-details/2026/Oracle-Investor-Day-2026-Accelerating-Value-Creation/default.aspx | 一次引用 |
| FY28 コンセンサス | 1,060億ドルでピーク、FY30 に 860億ドル(事前) | Investor Day 前の報道(検索要約) | 二次 |
| FY28 Wells Fargo | 1,640億ドル、FY30 まで近い水準(事前推計。Michael Turrin、Overweight、目標 280→250 ドル) | https://www.tipranks.com/news/article/oracles-investor-day-is-coming-heres-the-answer-wells-fargo-wants-on-the-stock | 二次 |
| 残り約 6GW の総 capex | 約 2,200億ドル(Q2 FY27〜Q4 FY28)、うち約半分をベンダー金融・前払い・顧客持込で賄う想定。帰属が不一致: Morgan Stanley / Proactive は「Oracle が示した」、Proactive は「Guggenheim(John DiFucci)の推計」とも書く。Street の事前想定は約 1,710億ドル(TipRanks) | https://www.proactiveinvestors.com/companies/news/1100945/oracle-analyst-day-eases-funding-concerns-and-bolsters-growth-outlook-1100945.html、TipRanks(MS) | 二次・帰属不一致 |
| FY30 までの追加総 capex | 約 1,500億ドル(Guggenheim 推計。会社数値ではない) | Proactive | 二次 |
| 容量 | FY26 末 約 3GW → FY28 末 約 10GW(約 7GW 追加) | MS / Melius / Invezz | 二次 |
| FY29 の step-down 幅 | not found | - | - |
| 純現金 capex(前払い控除後)の FY28・FY29 見通し | not found | - | - |
| Q1 FY27 実績 | capex 285億ドル(前年同期 85億ドル)、純現金 capex 180億ドル | Q1 FY27 スライド | 二次 |

---

## 4. 営業CFの経路

| 項目 | 数値 | 出典 | 区分 |
|---|---|---|---|
| FY26 | 営業CF 320億ドル(+54%) | Q4 FY26 発表 | 一次引用 |
| LTM(〜2026-08) | 営業CF 約 470億ドル、capex 約 760億ドル、FCF −287億ドル | https://knowyourinvestments.substack.com/p/oracles-investor-day-the-funding | 二次 |
| Q1 FY27 | 231億ドル(前年比 +184%)、うち前払い 113.6億ドル | sec-api.io | 二次 |
| FY27 FCF(コンセンサス) | 約 −350億ドル。FY28 も同程度(FactSet、CNBC 経由)。FY29 は Investor Day 前は赤字想定。黒字化まで 2 年で 650億ドル超の改善が必要との試算 | https://stocktwits.com/news-articles/markets/equity/oracle-forecasts-30-b-cash-flow-by-fy-29-helping-calm-ai-capex-concerns-pushing-orcl-stock-to-its-best-day-in-five-months/cZU9sPFR9GF ほか | 二次 |
| FY28・FY29 の営業CF 推計 | not found | - | - |
| FY28 の FCF | 会社: 下期に黒字化(「ahead of Street by more than 12 months」と Jefferies) | Reuters / Seeking Alpha https://seekingalpha.com/news/4660354-oracle-outlines-cleaner-path-to-cash-flow-but-execution-remains-key-analysts | 二次 |
| FY29 FCF | 300億ドル以上(「at least」。報道により「$30B」「exceed $30B」と表記ゆれ) | 8-K Ex.99.1 | 一次引用 |
| FY29 以降の前払いの寄与額 | not found | - | - |
| FY30 | 売上 2,250億ドル以上、非 GAAP 営業利益率 40% 以上、非 GAAP EPS 21 ドル以上、FY26〜FY30 売上 CAGR 35% 超 | 8-K Ex.99.1 | 一次引用 |

---

## 5. 負債

| 項目 | 数値 | 時点 | 出典 | 区分 |
|---|---|---|---|---|
| 借入(notes payable and other borrowings) | 流動 76.25億ドル + 非流動 1,177.12億ドル = 1,253億ドル | 2026-08-31 | 10-Q https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm(検索要約) | 一次(要約) |
| 同上(前期) | 流動 71.99億ドル + 非流動 1,223.42億ドル(2026-05-31) | 2026-05-31 | 同上 | 一次(要約) |
| リース負債(開始済み) | オペレーティング 346.21億ドル + ファイナンス 91.85億ドル = 約 438億ドル | 2026-08-31 | 同上 | 一次(要約) |
| 「総債務 1,691億ドル」 | 借入 1,253億+リース 438億=1,691億(私の足し算で一致)。出典の定義は借入+リースとみられるが明記は未確認。Bloomberg は「長期債務 1,600億ドル超」 | 2026-08 | https://www.tikr.com/blog/oracle-courts-apollo-and-goldman-for-ai-chip-financing-as-debt-tops-169-billion | 二次・定義不一致の可能性 |
| 未開始リース | 2,880億ドル(ほぼ全てデータセンター。FY27 Q2〜FY29 に開始予定。期間 15〜19 年との二次情報)。前期(2026-05)は 2,600億ドル、2025-11 は 2,480億ドル | 2026-08-31 | 10-Q(検索要約)、https://digg.com/world-business/n2py988v | 一次引用+二次 |
| 借入+全リース請求 | 約 4,570億ドル(RPO 6,640億ドルとの対比)。第三者の足し上げ | 2026-08 | https://www.useluminix.com/reports/company-overviews/oracle-ai-debt-openai-contract/source/2 | 二次 |
| 満期構成・平均金利 | not found(10-Q の債務注記を未確認) | - | - | - |
| 現金・短期投資 | 371億ドル | 2026-08 | tikr(二次) | 二次 |
| 純債務/調整後EBITDA | FY29 に 3.5 倍未満(確認)。純債務の定義は借入・ベンダー金融・オペレーティング/ファイナンス・リース負債 − 現金・有価証券(未開始リースが含まれるかは not found)。調整後EBITDA の脚注定義は途中で切れ未確認。「成長は FY29 から自己資金」も同文 | 2026-10-28 | 8-K Ex.99.1 / newsquawk 等 | 一次引用 |
| 格付け | S&P: BBB-(BBB から引下げ、2026-07-09、見通し安定、レバレッジ予想 4.8 倍、引下げ基準 4 倍)。Moody's: Baa2 / 見通しネガティブ(レバレッジが一時 5 倍近くまで上昇し得ると言及)。Fitch: BBB、安定。Investor Day 後の格付け行動は not found | 2026-07〜10 | https://ppc.land/s-p-cuts-oracle-to-bbb-as-ai-buildout-widens-cash-deficit-to-42bn/ ほか | 二次 |
| 5 年 CDS | 約 203bp(約 18 年ぶりの高水準)、10 月上旬 約 261bp との報道 | 2026-07〜10 | chartmill ほか | 二次・不一致(時期違い) |

---

## 6. アナリストの指摘

| 主体 | 内容 | 日付 | 出典 | 区分 |
|---|---|---|---|---|
| Morgan Stanley(Sanjit Singh、Equal Weight、目標 210 ドル) | 「Now comes the hard part」。ベンダー金融は純債務に残る、顧客持込は 1GW あたり売上が少ない。売上は着工から約 4 四半期後に始まり、建設遅延は売上と現金転換を遅らせる。40% 近い利益率の維持と FY28 末 約 10GW を確認したい。ベンダー金融等の内訳を会社は示さず | 2026-10-29 | https://www.tipranks.com/news/article/now-comes-the-hard-part-says-morgan-stanley-about-oracle-stock | 二次 |
| Wells Fargo(Turrin、Overweight、目標 250 ドル維持) | 事前: 開示されるべき事項を指摘、CoreWeave の債務利回り・CDS を警戒。事後: ベンダー金融が短期の現金需要を減らす。BYOH で 1GW あたり売上 約 59億ドル(標準契約 約 173億ドル)、capex は約 60億ドル以下(同氏の推計であり会社開示ではない)。1GW の営業利益率 約 34% は 40% 目標より低い | 2026-10 | https://seekingalpha.com/news/4660354-oracle-outlines-cleaner-path-to-cash-flow-but-execution-remains-key-analysts | 二次 |
| RBC | Hold、目標 165 ドル。「incrementally positive rather than thesis-changing」 | 2026-10-28/29 | https://www.tipranks.com/news/oracle-stock-orcl-forecast-heres-how-analysts-reacted-to-strong-fy30-outlook | 二次 |
| Oppenheimer / Baird / Melius | 資金調達の明確化を肯定(Oppenheimer 目標 275、Baird 215、Melius 170)。Jefferies: FCF 黒字化は Street より 12 か月以上早い | 2026-10-29 | https://www.investing.com/news/analyst-ratings/oppenheimer-reiterates-oracle-stock-rating-on-capex-funding-clarity-93CH-4982920 ほか | 二次(擁護) |
| Guggenheim(DiFucci、Buy、目標 400) | FY28 までに約 2,200億ドルの capex、約半分は前払い等。FY30 まで追加の総 capex 約 1,500億ドル | 2026-10 | Proactive(上記) | 二次 |
| Evercore ISI | 追加資金需要を 500〜600億ドルと推計(Investor Day 前)。Street の事前想定 約 500億ドル | 2026-10 | https://www.thestreet.com/investing/oracle-ai-cloud-funding-gap-google-nvidia | 二次・事前 |
| Bloomberg Intelligence(Anurag Rana) | 「could ease concern about elevated capital spending beyond the next two years」 | 2026-10-28 | thenextweb / stocktwits | 二次 |
| 報道上の留意 | 前払いが営業CFを押し上げている(Q1 FY27)。ATM 200億ドルは希薄化。上限 200億ドルはリース未開始分(2,880億ドル)に言及していない(StockTitan)。FY29 の FCF が GAAP/非 GAAP か不明 | 2026-09〜10 | https://www.stocktitan.net/articles/oracle-stock-investor-day-2026-20-billion-funding-cap | 二次 |
| Bernstein | 事前(2026-02): 約 450〜500億ドルの調達計画が長期の財務健全性を損ない、投資適格割れのリスクを高めるとの懸念(TMGM 要約)。Investor Day 後のノートは not found | 2026-02 | https://www.tmgm.com/es/analysis/market-insight/oracle-surges-amid-funding-relief-and-doubts | 二次 |
| Barclays / Moody's / S&P / その他クレジット | 「FCF 目標がリース・ベンダー金融で見かけを良くしている」と明言した批判: not found(Investor Day 後)。Barclays は事前に目標 252 ドル(tikr) | - | - | - |
| 株価反応 | 2026-10-28: +10.73%(終値 144.54 ドル、BigGo)。報道により +8.6〜14% の intraday 幅。10-29: 約 −4%(Invezz、Benzinga) | 2026-10-28/29 | https://finance.biggo.com/news/eebcbdbc-a31f-4a8b-8cf3-a57290c1c785 | 二次。Investing.com の intraday 値は不一致 |

---

## 7. 1GW あたりの経済性

| 項目 | 数値 | 出典 / 発言者 | 区分 |
|---|---|---|---|
| 1GW の capex | 約 370億ドル(契約総額の 50% 弱)。前年は約 100億ドル/GW と説明 | CFO Maxson(stockanalysis トランスクリプトの引用を含む検索要約)https://stockanalysis.com/stocks/orcl/transcripts/780561-investor-day-2026/、cryptobriefing https://cryptobriefing.com/oracle-80b-ai-infrastructure-investor-day/ | 二次(引用) |
| 1GW の売上 | 約 160億ドル/年(ランプ後、年換算)。コストプラス価格設定のため売上は変わり得るが、利益率と ROI は維持 | Maxson | 二次(引用) |
| 1GW の RPO | 約 800億ドル、平均契約期間 5 年 | cryptobriefing | 二次 |
| 利益率 | 粗利率 約 35%、プロジェクト段階の営業利益率 約 34% | Maxson(「While our gross margin is at around 35%, operating margin at the project level is around 34%」) | 二次(引用)。注: Seeking Alpha は 34% を「Wells Fargo の例示」と書く=帰属の不一致 |
| ROI | 約 28%(定義: 年間 NOPAT+減価償却 ÷ 累計 capex)。Q4 FY26 では「定常状態で high-20s の ROIC」(CFO) | 同上、Dolphin Research | 二次(引用) |
| 前提 | 代表的 1GW は、データセンターの建屋・電力設備を Oracle が「リース」する前提 | cryptobriefing | 二次 |
| BYOH 時の Oracle 負担 | Oracle: 「BYOH では売上が下がり利益率が上がる。自己資金・ベンダー金融では総 capex とプロジェクト経済性は概ね同じ」。BYOH 時の Oracle 負担額を Oracle が数値で示したかは not found。Wells Fargo の推計は上表(売上 約 59億、capex 約 60億ドル以下) | Maxson / Wells Fargo | 二次 |
| MS の 1GW 例 | capex 約 370億ドル。ベンダー金融 70% なら初期 2 年の資金負担は 約 370億→約 180億ドル | TipRanks | 二次(アナリスト例示) |
| 確認結果 | 「37B/GW」「16B/GW」「ROI 28%」はすべて確認できた(上記)。ただしいずれも二次情報の引用で、スライド原本は未確認 | - | - |
| 混同注意 | NVIDIA の「約 400億ドル/GW」は NVIDIA の売上機会で、Oracle の支払額ではない | 検索要約 | 二次 |

---

## 会社の FY29 FCF 300 億ドルを説明する要素(一覧)

額が not found の行は、額を推測で埋めていない。

| 要素 | 額 | 出典 | 確度 |
|---|---|---|---|
| (1) FY29 の capex 減少(FY27〜28 がピーク) | 方向のみ。FY28・FY29 の会社 capex 額は not found。事前コンセンサスは FY28 1,060億→FY30 860億ドル(Wells Fargo は FY28 1,640億ドルで高止まり)=不一致 | 8-K Ex.99.1(一次引用)、報道 | 方向: 高(会社明言)/ 額: 低 |
| (2) 売上・利益の拡大(FY30 売上 2,250億ドル以上、営業利益率 40% 以上、CAGR 35% 超) | FY29 の売上・営業CF額は not found | 8-K Ex.99.1 | 高(目標値)/ FY29 の中間値: not found |
| (3) 稼働済み容量の利益(約 3GW→約 10GW、1GW あたり売上約 160億ドル・営業利益率約 34%) | 10GW×約 160億=約 1,600億ドル/年は私の掛け算であり、出典に無い。Oracle は FY29 に向けた GW 別内訳を示していない(not found) | Maxson(引用)、MS / Seeking Alpha | 中(単位経済)/ 合算: 推測につき採用せず |
| (4) 顧客前払い(営業CFに算入される) | Q1 FY27 は 113.6億ドル。FY27 は 200〜250億ドル(純現金 capex との差)。FY28・FY29 の額は not found。FCF の式(営業CF−capex)の中で前払いは営業CFに入る | sec-api.io、Maxson、10-Q 式 | 中(FY27 まで)/ FY29: not found |
| (5) ベンダー金融・顧客持込ハード(BYOH)による現金 capex の圧縮 | 残り約 6GW・総 2,200億ドルの約半分を外部化(約 1,100億ドル相当)との報道。帰属不一致(Oracle / Guggenheim)。ベンダー金融は純債務に残る(MS) | Proactive、TipRanks | 中〜低(帰属不明) |
| (6) リース構造(開始前は capex に計上されない。FCF の式はリース元本を差し引かない) | 未開始リース 2,880億ドル(2026-08-31)。式が元本返済を控除しない点は検索要約側の推論で、Oracle の明示文言は not found | 10-Q(検索要約) | 中(数値)/ 低(FCF への影響の説明) |
| (7) 開発事業者・プロジェクト債(Vantage 約 380億ドル、Saline 約 160億ドル等) | 開発事業者が借り手。Oracle の capex には計上されないとみられるが、Oracle の会計処理の明示は not found | DCD、Bloomberg 要約 | 中(額)/ 低(会計) |
| (8) 追加の資本市場調達 200億ドルの上限(株 100億・債 100億、借換え除く)+ATM 200億ドル完了(Q1 FY27) | 財務CFであり FCF の構成要素ではない。ただし「自己資金で成長」への橋渡しとして会社が提示 | 8-K Ex.99.1 | 高(会社明言) |
| (9) 未確定の補完策: GPU リース SPV(Apollo・Goldman) | 額 not found、交渉段階 | WSJ(二次要約) | 低 |
| (10) 外部の FCF 見通しとの差 | FY27・FY28 の外部 FCF は各 約 −350億ドル(FactSet、CNBC 経由)。会社目標 FY29 +300億ドルとの差は、2 年で 650億ドル超の改善に相当 | CNBC / stocktwits | 中 |

## 未解決(not found)の主な項目
- Investor Day での FCF 定義の説明、GAAP / 非 GAAP の別、前払い・ベンダー金融の扱い
- FY28・FY29 の会社 capex 額、純現金 capex、営業CF、前払いの寄与
- BYOH の契約比率・額(Oracle 負担額の数値)
- 借入の満期構成・平均金利、ベンダー金融の残高
- GPU リース(ファイナンス / オペレーティング)の内訳、SPV の額
- 2026 年の四半期別の外部化額(Q3 FY26 の営業CF・capex も未取得)
- Investor Day 後の Moody's / S&P / Barclays / Bernstein のコメント
- 一次資料(8-K Ex.99.1、スライド `6-Hilary_Wednesday-AM.pdf`、トランスクリプト)の本文照合
