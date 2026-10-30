# Oracle(ORCL) 2026年10月 Investor Day(Oracle AI World 2026)調査メモ

調査日: 2026-10-30 / 方法: WebSearch のみ(WebFetch 不可。SEC・stockanalysis・oracle.com への直接取得も proxy で 403/301 のため不可)。
注意: 数値は検索要約(二次)経由。一次資料(8-K Ex.99.1、investor.oracle.com のプレスリリース、q4cdn のスライド PDF)の URL は特定できたが、本文は直接読めていない。評価・意見は書かない。

## 0. イベントの有無と基本情報

| 項目 | 内容 | 発言者 | 日付 | 出典URL |
|---|---|---|---|---|
| 開催の有無 | あった。名称は "Oracle Investor Day 2026: Accelerating Value Creation"(Financial Analyst Meeting ではなく Investor Day)。Oracle AI World 期間中、ラスベガス。ライブ配信あり | 会社 | 2026-10-28(AI World は 10/25〜28) | https://investor.oracle.com/investor-news/news-details/2026/Oracle-Investor-Day-2026-Accelerating-Value-Creation/default.aspx |
| 開催告知 | 「Investor Day Meeting を 2026-10-28 に Oracle AI World 中に開催」 | 会社 | 2026 年 10 月(告知日は未特定) | https://investor.oracle.com/investor-news/news-details/2026/ORACLE-INVESTOR-DAY-MEETING-TO-BE-HELD-OCTOBER-28-2026/default.aspx |
| 登壇者 | Clay Magouyrk(co-CEO)、Mike Sicilia(co-CEO)、Hilary Maxson(CFO、2026-04 就任)が発表・質疑。Ellison の登壇・発言は確認できず(not found) | 会社 8-K | 2026-10-28 | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526435853/d75538dex991.htm |
| 一次資料 | 8-K Ex.99.1(上記 SEC URL)、PR Newswire 版、スライド(CFO 資料 PDF) | 会社 | 2026-10-28 | https://www.prnewswire.com/news-releases/oracle-investor-day-2026-accelerating-value-creation-302922564.html / https://s23.q4cdn.com/440135859/files/doc_downloads/2026/10/Oracle-Investor-Day-Meeting/6-Hilary_Wednesday-AM.pdf |
| 書き起こし(第三者) | stockanalysis.com に Investor Day 2026 の transcript あり(断片・一部乱れ、と検索要約は注記) | - | 2026-10-28 | https://stockanalysis.com/stocks/orcl/transcripts/780561-investor-day-2026/ |
| AI World 同週の製品発表 | 10/26 Fusion Agentic Applications、10/27 OpenAI 連携・外部シリコン 5 種(下記 6 参照) | 会社 | 2026-10-26〜27 | 下記 6 参照 |

## 1. 長期目標の更新

| 項目 | 数値・内容 | 発言者 | 日付 | 出典URL |
|---|---|---|---|---|
| FY30 売上 | $225B 以上(FY26 からの CAGR 35% 超)。前年 FAM と同額=据え置き(同額の再提示) | 会社(プレスリリース) | 2026-10-28 | https://www.stocktitan.net/news/ORCL/oracle-investor-day-2026-accelerating-value-josi685spepl.html ; https://www.sec.gov/Archives/edgar/data/0001341439/000119312526435853/d75538dex991.htm |
| FY30 非GAAP 営業利益率 | 40% 以上(今回の開示。前年 FAM の要約には営業利益率目標の記載を確認できず → 前年側は not found) | 会社 | 2026-10-28 | 同上 |
| FY30 非GAAP EPS | $21 以上(前年 $21 と同額=据え置き) | 会社 | 2026-10-28 | 同上 |
| FY30 OCI 売上 | not found(プレスリリース要約に OCI 単独の FY30 目標なし。前年は $166B)。TradingView の個人投稿に OCI 系列の数字があるが出所不明のため採用しない | - | - | - |
| FY27 ガイダンス | 売上 $90B 以上を再確認。非GAAP EPS は報道で食い違い: プレスリリース要約は「$8.10」、SEC 8-K 系の別要約は「$8.05 に引き上げ」 → **不一致**(どの 8-K の記述かは未確認) | 会社 | 2026-10-28 / 9-10 | https://investinglive.com/stocks/icymi-oracle-jumps-around-11-on-225bn-2030-revenue-goal-and-20bn-cap-on-new-funding/ ; https://www.sec.gov/Archives/edgar/data/0001341439/000119312526265848/orcl-ex99_1.htm |
| FY27 Q2 ガイダンス | 売上成長 30〜34%(Q1 決算時の開示)。クラウド成長率ガイドは 64〜71% / 65〜71% で報道不一致 | 会社 | 2026-09-10 | https://quartr.com/events/oracle-corporation-orcl-q1-2027_3gvkOKJp |
| FCF | 黒字化は FY28 下期(2027-12〜2028-05)。FY29 に FCF $30B 以上 | Maxson(CFO) | 2026-10-28 | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526435853/d75538dex991.htm ; https://kfgo.com/2026/10/28/oracle-expects-to-turn-cash-flow-positive-in-second-half-of-fiscal-2028/ |
| capex | FY27〜FY28 がピーク、FY29 に減少(絶対額の FY30 目標は not found)。FY27 capex $90〜95B・純現金 capex $70B 以下という数字は tradingkey 要約のみ、別要約は FY27 $91.9B(+65%)、FY26 実績 $55.7B。FY27 の幅は **不一致/未確認** | 会社 | 2026-10-28 | https://www.tradingkey.com/analysis/stocks/us-stocks/262239077-orcl-oracle-ai-spacex-openai-ai-world-tradingkey |
| 純債務/EBITDA | FY29 に 3.5 倍未満(単一の検索要約のみ。要確認) | 会社 | 2026-10-28 | https://www.roic.ai/news/oracle-shares-surge-on-long-term-guidance-financing-clarity-10-28-2026 |
| 資本配分の優先順位 | 投資適格格付けの維持、配当、成長投資(8-K 文言の要約) | 会社 | 2026-10-28 | https://investor.oracle.com/investor-news/news-details/2026/Oracle-Investor-Day-2026-Accelerating-Value-Creation/default.aspx |
| FY31/FY32 への延長 | not found(FY30 のまま) | - | - | - |

## 2. AI 容量の経済性

| 項目 | 数値・内容 | 発言者 | 日付 | 出典URL |
|---|---|---|---|---|
| 粗利率・プロジェクト営業利益率 | 「粗利率は約 35%、OpEx が軽いモデルのためプロジェクトレベルの営業利益率は約 34%」(transcript 抜粋。前年は AI DC 粗利 30〜40% レンジ) | 経営陣(話者名は抜粋から特定できず) | 2026-10-28 | https://stockanalysis.com/stocks/orcl/transcripts/780561-investor-day-2026/ |
| 会社全体の粗利率 61.93% | データサイトの別計算値で、上記と定義が異なる(混同注意)。**不一致** | - | - | 同上(検索要約) |
| BYOH(顧客持込) | 「BYOH では売上は下がるが利益率は上がる」と説明(比率は not found)。前払い・顧客持込 GPU 価値 $75B(FY26 Q4 時点)という二次報道あり(Q4 FY26 リリースの記述とされる、未確認) | 経営陣 | 2026-10-28 / FY26 Q4 | https://stockanalysis.com/stocks/orcl/transcripts/780561-investor-day-2026/ ; https://calcalistech.com/ctechnews/article/vh1b41rqk(ベンダーファイナンス・顧客持込・前払いで初期現金を減らす、と報道) |
| 1GW あたり経済性 | capex 約 $37B、満稼働時の年間売上約 $16B、ROI 約 28%(cryptobriefing と transcript 抜粋に由来する二次情報。「約 $80B の AI 契約」との記述もあり、単一サイト/契約の数字か 1GW 一般か不明)。別の Substack は「7GW 追加に最低 $350B(約 $50B/GW)、ただし Oracle がチップを買う場合」 → **不一致** | 経営陣 | 2026-10-28 | https://cryptobriefing.com/oracle-80b-ai-infrastructure-investor-day/ ; https://knowyourinvestments.substack.com/p/oracles-investor-day-the-funding |
| GPU 更新・再販単価、契約期間 | not found | - | - | - |
| 顧客基盤 | AI インフラの顧客は 1,000 社超(transcript 抜粋) | 経営陣 | 2026-10-28 | https://stockanalysis.com/stocks/orcl/transcripts/780561-investor-day-2026/ |

## 3. 容量と電力

| 項目 | 数値・内容 | 発言者 | 日付 | 出典URL |
|---|---|---|---|---|
| 大型サイト | 建設中の大型 5 サイト合計約 5GW、各約 1GW(±数百 MW)、Abilene は完成間近。うち 4 サイトが暦年 2027 にサービス開始(transcript 抜粋) | 経営陣 | 2026-10-28 | https://stockanalysis.com/stocks/orcl/transcripts/780561-investor-day-2026/ |
| 追加容量 | 「約 7GW を今後数年で顧客へ提供」。FY28 末に総容量 10GW 超、との報道あり(Substack)。別の要約は「FY28 末に約 10GW」 → 7GW(増分)と 10GW(総量)は別概念の可能性、一部**不一致の余地** | 経営陣 / 報道 | 2026-10-28 | https://knowyourinvestments.substack.com/p/oracles-investor-day-the-funding ; https://invezz.com/news/2026/10/29/oracle-stock-falls-4-why-experts-arent-bothered/ |
| 7GW の FCF | 「約 7GW のプロジェクトは比較的早く FCF の貢献に転じる」(transcript 要約) | 経営陣 | 2026-10-28 | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526435853/d75538dex991.htm(検索要約経由) |
| 初回納入の試金石 | Shackelford(テキサス)と Doña Ana(New Mexico、Project Jupiter)が 2027 年前半に顧客納入開始予定(Jefferies ノート経由の報道) | Jefferies / 報道 | 2026-10-29 | https://invezz.com/news/2026/10/29/oracle-stock-falls-4-why-experts-arent-bothered/ |
| Project Jupiter | 9 月に force majeure(不可抗力)通知の報道で株価約 4% 下落(2026-09-24 前後)。Oracle は「遅延に備えた保護措置で、キャンセルではない」と説明と報道 | 報道 | 2026-09-24 | https://www.tikr.com/blog/oracle-stock-fell-nearly-4-on-its-project-jupiter-notice-the-2028-target-lands-where-the-street-sees-cash-flow-turning |
| 電力(燃料電池) | Bloom Energy と最大 2.8GW の調達枠(うち 1.2GW 契約済み)。Project Jupiter は最大 2.45GW の Bloom 燃料電池で給電。※Investor Day 当日の発言ではなく 4 月の発表 | 会社 / Bloom | 2026-04-13〜27 | https://www.bloomenergy.com/news/bloom-energy-and-oracle-expand-strategic-partnership-to-deploy-up-to-2-8-gw-to-accelerate-ai-infrastructure-build-out/ ; https://www.oracle.com/news/announcement/oracle-borderplex-and-bloom-energy-to-power-project-jupiter-with-fuel-cell-technology-2026-04-27/ |
| 稼働 GW(現在値) | 「850MW・約 30 万 GPU・稼働率約 98%」という二次報道あり(時点不明、要確認) | 報道 | 不明 | https://www.investing.com/analysis/oracle-backlog-of-553b-raises-questions-around-future-revenue-scale-200679538 の周辺要約 |
| 年ごとの追加計画、Michigan・Wisconsin の進捗、ガス・原子力 | not found(Investor Day 資料の本文を読めていない) | - | - | - |
| 2030〜34 年の追加 | 経営陣は「2030〜2034 に 90GW 追加は不可能と思う」と発言(transcript 抜粋、文脈不明) | 経営陣 | 2026-10-28 | https://stockanalysis.com/stocks/orcl/transcripts/780561-investor-day-2026/ |

## 4. 受注残(RPO)と顧客

| 項目 | 数値・内容 | 発言者 | 日付 | 出典URL |
|---|---|---|---|---|
| RPO | $664B(FY27 Q1 末=2026-08-31)。90% 超がインフラ事業。FY26 末は $638B との別報道あり(基準差) | 経営陣 / 会社 | 2026-09-10 / 10-28 | https://finance.yahoo.com/technology/ai/articles/oracle-orcl-reports-664-billion-002207397.html ; https://erp.today/oracle-q1-fy27-results-664b-backlog-ai-contracts/ |
| 36 か月以内の認識 | 約半分が 36 か月以内に売上化(二次報道) | 経営陣 | 2026-10-28 | https://finance.yahoo.com/technology/ai/articles/oracle-orcl-reports-664-billion-002207397.html(検索要約経由) |
| OpenAI の比率 | 公式値 not found。Cantor 経由で約 5 割(Barron's 報道)、別報道で 45〜50% → 推計。古い 54%($553B 時点)は陳腐化 | 外部推計 | 2026 年 | https://www.investing.com/analysis/oracle-backlog-of-553b-raises-questions-around-future-revenue-scale-200679538 |
| 新規大型契約 | Investor Day での新規名指しは not found。Meta とのクラウド契約は存在確認のみ(規模非開示)。xAI も過去に名指し。10/27 に外部シリコン契約(下記 6) | 会社 | - | https://www.oracle.com/news/announcement/ai-world-oracle-reinvents-enterprise-computing-for-the-ai-era-with-openai-2026-10-27/ |

## 5. 資金計画

| 項目 | 数値・内容 | 発言者 | 日付 | 出典URL |
|---|---|---|---|---|
| 新規資本市場調達の上限 | FY27〜FY30 の投資サイクルで追加調達 $20B まで(リファイナンス除く)。内訳想定は株式 $10B + 総額債務 $10B。Street 想定は約 $50B と報道 | 会社 / Maxson | 2026-10-28 | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526435853/d75538dex991.htm ; https://www.stocktitan.net/articles/oracle-stock-investor-day-2026-20-billion-funding-cap |
| Maxson の言い回し | 「FY27 の残りに up to $20B」「このサイクルを賄う最終的な額」と引用する報道あり。上限が FY30 まで(会社文言)か FY27 残り(引用)かで**表現不一致** | Maxson | 2026-10-28 | https://calcalistech.com/ctechnews/article/vh1b41rqk ; https://aiweekly.co/alerts/oracle-projects-30b-fcf-by-fy2029-caps-fundraising-at-20b |
| ATM | FY27 Q1(〜2026-08-31)に ATM を使い切り、141M 株・純 $19.9B。上記上限とは別枠 | 会社(10-Q) | 2026-09 | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm |
| 自己資金化 | FY29 から成長は自己資金で賄う | Maxson(Reuters) | 2026-10-28 | https://www.globalbankingandfinance.com/oracle-eases-ai-spending-worries-plan-turn-cash-flow/ |
| 財務数値(参考) | FY26 FCF -$23.7B、FY26 capex $55.7B。FY27 Q1 FCF -$5.4B(営業CF $23.1B)。2026-08-31 時点 借入 $125.34B、現金 約 $36.37B | 会社 | 2026-06〜10 | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm ; https://aiweekly.co/alerts/oracle-projects-30b-fcf-by-fy2029-caps-fundraising-at-20b |
| 格付け方針 | 「投資適格の維持」を資本配分の優先事項に記載(8-K 文言の要約)。格付会社の動きは not found | 会社 | 2026-10-28 | https://investor.oracle.com/investor-news/news-details/2026/Oracle-Investor-Day-2026-Accelerating-Value-Creation/default.aspx |
| 配当・自社株買い | 配当は優先事項に記載のみ。額・自社株買いは not found | - | - | - |
| 補足 | Ellison が最大 5,000 万株($7.5B)の売却計画を取り消し(9 月報道) | 報道 | 2026-09 | https://arynews.tv/larry-ellison-cancels-plan-to-sell-oracle-stock |

## 6. 製品

| 項目 | 数値・内容 | 発言者 | 日付 | 出典URL |
|---|---|---|---|---|
| マルチクラウド DB | FY27 Q1: マルチクラウド DB 売上 +353% YoY、顧客 +180%。マルチクラウド DB リージョン 70(AWS は 22 リージョン)。前四半期は +531% | 会社(Q1 決算) | 2026-09-10 | https://quartr.com/events/oracle-corporation-orcl-q1-2027_3gvkOKJp |
| FY27 Q1 概況 | 売上約 $19.3B(+30%)、OCI 売上 $7.4B(+121%) | 会社 | 2026-09-10 | 同上 |
| Fusion | 10/26: Fusion Agentic Applications(Fusion Claw 基盤、ERP/HCM/SCM/CX で 25 の agentic アプリ)、Fusion Agentic Home / Companion | 会社 | 2026-10-26 | https://www.oracle.com/news/announcement/ai-world-oracle-advances-outcome-driven-ai-across-fusion-applications-2026-10-26/ |
| データ/信頼 | Deep Trust AI Architecture、Autonomous AI Lakehouse の拡張、Business Semantic Layer | 会社 | 2026-10-26 | https://www.channelinsider.com/infrastructure/oracle-ai-world-ai-trust-lakehouse-announcements/ |
| OpenAI 連携 | OpenAI モデル・ChatGPT・Codex を Oracle のアプリ・データ・クラウドに統合。AI SMB Bundle(年 $12,000 のクレジット) | 会社 | 2026-10-27 | https://www.oracle.com/news/announcement/ai-world-oracle-reinvents-enterprise-computing-for-the-ai-era-with-openai-2026-10-27/ ; https://www.cnbc.com/2026/10/27/oracle-openai-chatgpt-codex-google-tpus.html |
| マルチシリコン | OCI に外部シリコン 5 種(NVIDIA Vera Rubin、Google TPU、Cerebras、SambaNova、Intel Diamond Rapids)。Google とは複数年・複数 GW の立ち上げ、提供は暦年 2027 | 会社 | 2026-10-27 | https://futurumgroup.com/insights/oracle-makes-the-supercluster-multi-silicon-at-ai-world-2026/ |
| AI Database 26ai / NetSuite / ソブリンクラウド / OCI リージョン総数 | not found | - | - | - |

## 7. 経営陣の発言(和訳)

| 発言者 | 内容(和訳。原文は要所のみ) | 日付 | 出典URL |
|---|---|---|---|
| Maxson | 「成長は FY29 から自己資金で賄う」「FCF は FY28 下期に黒字化し、FY29 は $30B 超」(Reuters 要約の言い換え) | 2026-10-28 | https://kfgo.com/2026/10/28/oracle-expects-to-turn-cash-flow-positive-in-second-half-of-fiscal-2028/ |
| Maxson | 「FY27 の残りに最大 $20B」「このサイクルを賄うのに必要な最終的な額」(引用報道。原文 "the final amount needed to fund the remainder of this cycle"。ただし二次引用) | 2026-10-28 | https://calcalistech.com/ctechnews/article/vh1b41rqk |
| 経営陣(話者不明) | 「粗利率は約 35%、OpEx が軽いモデルのためプロジェクトレベルの営業利益率は約 34%」(原文 "operating margin at the project level is around 34% due to that OpEx-light business model") | 2026-10-28 | https://stockanalysis.com/stocks/orcl/transcripts/780561-investor-day-2026/ |
| 経営陣(話者不明) | 「RPO $664B は業界最大級で、90% 超がインフラ事業」 | 2026-10-28 | 同上 |
| 経営陣(話者不明) | 「BYOH では売上は下がるが利益率は上がる」 | 2026-10-28 | 同上 |
| Magouyrk | 9 月決算での発言(Investor Day ではない): BYOH を説明。「前払いで設備投資が不要になる、とは言っていない(追加 capex は必要)」 | 2026-09-10 | https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/ |
| Sicilia、Ellison | 当日の発言 not found | - | - |

## 8. 株価と主要アナリスト

| 項目 | 数値・内容 | 日付 | 出典URL |
|---|---|---|---|
| 当日(10/28) | 終値 $144.54、+10.73%(場中最大 +12.6%、TNW は最大 +14% と報道 → 不一致。TMGM は +9.64% と報道 → 不一致)。5 か月ぶりの最大上昇日(Stocktwits)。時価総額 +$40B 超 | 2026-10-28 | https://www.fool.com/coverage/stock-market-today/2026/10/28/stock-market-today-oct-28-oracle-surges-on-fiscal-2030-revenue-guidance-of-usd225-billion/ ; https://thenextweb.com/news/oracle-30b-free-cash-flow-2029-shares-jump |
| 翌日(10/29) | 終値約 $139.56、-3.45%(前日比 -$4.98)。日中 $136.59〜$144.61。Investing.com は $140.90 → **不一致**。理由は Alphabet の AI 費用超過が背景、または AI/クラウド株全般の売り(報道で食い違い、会社の説明なし) | 2026-10-29 | https://www.marketbeat.com/instant-alerts/price-oracle-nyse-orcl-stock-price-down-35-whats-next-2026-10-29/ ; https://invezz.com/news/2026/10/29/oracle-stock-falls-4-why-experts-arent-bothered/ |
| 前日(10/27)水準 | 約 $126(Goldman 目標引下げ記事 10/26 時点)。逆算 $144.54/1.1073 ≒ $130.5 → 水準に差(要確認) | 2026-10-26〜27 | https://www.tikr.com/blog/oracle-heads-into-investor-day-as-goldman-cuts-its-target-to-206-heres-where-the-stock-could-go-by-2031 |
| Goldman Sachs(事前) | 目標 $240 → $206。FY28〜30 目標の達成可能性に疑問 | 2026-10-26 | 同上 |
| Bank of America | Buy 継続、目標 $240 | 2026-10-28〜29 | https://www.proactiveinvestors.com/companies/news/1100945/oracle-analyst-day-eases-funding-concerns-and-bolsters-growth-outlook-1100945.html |
| Guggenheim | Buy、目標 $400、"Best Idea" | 同上 | https://www.tipranks.com/news/oracle-stock-orcl-forecast-heres-how-analysts-reacted-to-strong-fy30-outlook |
| Oppenheimer | Outperform、目標 $275 | 同上 | https://www.benzinga.com/trading-ideas/movers/26/10/62704989/oracle-stock-slides-whats-going-on |
| Piper Sandler | Overweight、目標 $225 | 同上 | 同上 |
| Wells Fargo | Overweight、目標 $280 → $250。capex を FY28 約 $164B(コンセンサスは約 $106B)と見ているとの報道(検索間で裏付け揺れ、要確認) | 同上 | https://www.tikr.com/blog/wells-fargo-is-bullish-on-oracle-expects-the-cloud-infrastructure-stock-to-gain-50 |
| Baird | Buy、目標 $215 | 同上 | https://www.tipranks.com/news/oracle-stock-orcl-surged-11-as-investor-day-eased-spending-fears-and-set-solid-fy30-outlook |
| RBC | Hold、目標 $165(資金コミットが市場の懸念より小さい点を指摘) | 同上 | 同上 |
| Bernstein | Buy、目標 $325(10/29 時点で維持と報道) | 2026-10-29 | https://www.marketbeat.com/instant-alerts/price-oracle-nyse-orcl-stock-price-down-35-whats-next-2026-10-29/ |
| Jefferies | 契約残が約 7GW の増分容量を支える、との見方(目標変更は not found) | 2026-10-29 | https://invezz.com/news/2026/10/29/oracle-stock-falls-4-why-experts-arent-bothered/ |
| コンセンサス目標 | $248.04(Benzinga) / $243.86(TipRanks) → **不一致** | 2026-10-29 | 上記 Benzinga / TipRanks |
| LSEG コンセンサス | FY30 売上 約 $224.2B(会社目標とほぼ同水準) | 2026-10-28 | https://www.tikr.com/blog/oracle-soars-12-after-pairing-its-225-billion-target-with-a-funding-cap |
| 注意 | 上記の目標株価は検索要約経由で、各社ノートの原文は未確認。TheFly 系記事(Barclays $202、TD Cowen $190、Jefferies $190 等)は日付不明のため Investor Day の反応とは扱わない。Bernstein の「希薄化約 5%・四半期利息 $1.6B」は 2026 年前半の調達計画時のもので、今回の反応ではない | - | https://www.investing.com/news/stock-market-news/oracle-stock-bernstein-looks-at-the-financial-impact-of-the-capital-raise-4493824 |

## 前年 FAM(2025-10-16)からの変更点

| 項目 | 前年 FAM(2025-10-16) | 今回 Investor Day(2026-10-28) | 変化 |
|---|---|---|---|
| FY30 売上 | $225B | $225B 以上(CAGR 35% 超 / FY26 比) | 据え置き(文言が「以上」) |
| FY30 OCI 売上 | $166B | not found | 不明 |
| FY30 非GAAP EPS | $21 | $21 以上 | 据え置き |
| 営業利益率 | 前年は目標の記載を確認できず | FY30 非GAAP 40% 以上 | 今回明示(前年は not found) |
| AI DC 粗利 | 30〜40% | 粗利約 35%、プロジェクト営業利益率約 34% | 範囲内(点推計) |
| FCF | 目標の開示なし(要確認) | FY28 下期に黒字化、FY29 に $30B 以上 | 新規開示 |
| capex | 前年の capex 目標は not found | FY27〜28 ピーク、FY29 減少 | 新規(形状のみ) |
| 資金計画 | 目標に資金上限なし | 追加調達 $20B 上限(株式 $10B + 債務 $10B)、FY29 から自己資金化 | 新規 |
| ATM | - | FY27 Q1 に $19.9B 使い切り(上限とは別) | 新規 |
| RPO | 約 $455B(2025-09 末) | $664B(2026-08 末) | 増加 |
| 容量 | - | 約 7GW 追加、FY28 末に 10GW 超(報道) | 新規(要確認) |
| 株価反応 | 前日比の反応は報道で -7% 前後(検索要約)、終値水準は not found | 当日 +10.7%($144.54)、翌日 -3.45%($139.56) | 反対方向 |
| 期間延長 FY31/32 | - | not found | - |

## 未発見項目の一覧

- FY30 OCI 売上目標(今回の有無)、FY30 の capex 絶対額・FCF 以外の年次 capex 表
- GPU の更新・再販単価、契約期間の平均、BYOH・前払いの比率
- 稼働 GW(現在)・年次の追加 GW 計画、Michigan・Wisconsin・Abilene 以外のサイト別進捗、ガス/原子力の具体
- OpenAI の公式な RPO 比率、新規大型顧客の名指し(Meta・xAI の新契約)
- 配当・自社株買いの額、格付会社の対応
- AI Database 26ai、NetSuite、ソブリンクラウド、OCI リージョン総数の Investor Day 内の数値
- Sicilia・Ellison の当日発言、Magouyrk の当日の直接引用
- Investor Day 後に出た目標株価変更の原文ノート(BofA 以外の上げ下げ)
- 8-K Ex.99.1 とスライド PDF の本文(直接取得できず。次の担当は SEC 8-K と q4cdn PDF を読むこと)
