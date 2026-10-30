# U5 Oracle 会社の年度別見通し(Investor Day 2026-10-28)調査メモ
調査日: 2026-10-30 / 方針: 事実と出典のみ。評価は書かない。見つからない項目は not found。

## 0. 調査の限界(先に)
- sec.gov / investor.oracle.com / q4cdn / prnewswire / stockanalysis は直接読めない。さらに WebFetch は marketbeat・proactiveinvestors・gurufocus・stockanalysis で名前解決に失敗(このセッションの許可ドメイン外)。したがって全ての内容は WebSearch の要約文で確認したもので、原文ページは開いていない。
- 最重要の一次資料は CFO Hilary Maxson のスライド(q4cdn の `6-Hilary_Wednesday-AM.pdf`)と 8-K 別紙 99.1。検索要約では「PDF の抽出が崩れて読めない」とされた。年度別の数字があるとすればここにある可能性が高いが、今回は確認できていない。
- 結論(確認できた範囲): 会社の公式リリース(8-K / PR Newswire の要約)が示す年度別の数字は FY27(売上・EPS)、FY29(FCF・capex の方向・自己資金化・ネットデット/EBITDA)、FY30(売上・営業利益率・EPS)に限られる。FY28・FY29 の売上・EPS・営業利益率・OCI 売上・クラウド売上・営業CF、FY31・FY32 の目標は、検索した範囲では not found。「FY28 EPS 目標」「FY29 EPS 目標」は会社発表としては見つからなかった(複数の検索で「FY29 EPS target は無い」との回答)。

## 1. 年度×指標の表(会社の見通し)

凡例: 会社=Oracle 発表(二次報道経由)。S=出典番号(末尾の出典一覧)。

| 指標 | FY27 | FY28 | FY29 | FY30 | FY31/FY32 |
|---|---|---|---|---|---|
| 総売上 | **900 億ドル以上**(at least $90B)。再確認(2026-10-28)。[S1,S2,S3] | not found(会社)。Stocktitan の比較表は「FY28 売上: リリースに記載なし」[S4] | not found | **2,250 億ドル以上**、FY26→FY30 の年平均成長率 35% 超 [S1,S2,S5] | not found |
| OCI(クラウドインフラ)売上 | not found(FY27 の OCI 目標は 2026 年版では未確認)。参考: Q1 FY27 実績 74 億ドル、前年比 +121% [S6] | not found | not found | **not found**(2026 年版の FY30 OCI 目標を示す記事は見つからず。複数の検索が「見つからない」と回答)。参考: 2025-10 の目標は 1,660 億ドル [S7] | not found |
| クラウド全体売上 | Q2 FY27 ガイダンス: クラウド売上 +65〜71%(米ドル)/ +64〜70%(定率)[S6,S8]。通期は not found | not found | not found | not found | not found |
| 非GAAP EPS | **8.10 ドル**(6月 8.05 → 9/10 に 8.10 → 10/28 再確認)[S6,S9,S3] | **not found** | **not found** | **21 ドル以上** [S1,S2,S5] | not found |
| GAAP EPS | not found | not found | not found | not found | not found |
| 非GAAP 営業利益率 | not found(通期)。Maxson は Q1 call で「今年は粗利率が低下、今後数年で横ばいになる」と発言(数値なし)[S10] | not found | not found | **40% 以上** [S1,S2,S5] | not found |
| 営業CF | not found(Q1 FY27 実績: 営業CF 231 億ドル)[S11] | not found | not found | not found | not found |
| capex | **900〜950 億ドル**、うち現金ベースの純 capex は 700 億ドル以下(Q1 call 時点のガイダンス)[S10,S12]。Q1 FY27 実績 285 億ドル [S11] | FY27 とともに**ピーク**(金額は not found)[S1,S2] | **減少に転じる**(金額は not found)[S1,S2] | not found | not found |
| FCF | 赤字(会社の金額は not found)。Q1 FY27 実績 -54 億ドル [S11]。FY26 実績 約 -237 億ドル(複数の二次情報)[S13] | **下期(2H)に黒字化**(通期金額は not found)[S1,S2,S14] | **300 億ドル以上** [S1,S2,S14] | not found | not found |
| 資金調達 | 追加の資本市場調達は FY27〜FY30 で合計上限 200 億ドル(株式 100 億 + 総額ベースの債務 100 億、借換えを除く)[S1,S2] | 同左 | FY29 から成長は自己資金でまかなう。ネットデット/調整後 EBITDA は 3.5 倍未満 [S2,S15] | 同左 | — |

補足(会社発表の周辺事実)
- 上限 200 億ドルの外側: ベンダーファイナンス、顧客持ち込みハードウェア、顧客の前払い。FY27 第1四半期に完了した 200 億ドルの ATM 株式売出しも別枠 [S16,S17]。
- 非GAAP の定義: 減価償却とオペレーティングリースの費用を戻した数値(8-K の脚注)[S18]。
- 営業利益率の不一致: 公式要約は FY30「40% 以上」。CryptoBriefing は「約 34%」と記載(別の要約はこれを他の指標との取り違えの可能性とした)[S19]。
- 発言者: 共同CEO の Clay Magouyrk(綴りは Magouryk とする記事もある)と Mike Sicilia、CFO Hilary Maxson が登壇 [S5,S20]。年度別の発言の引用は取得できていない。Doug Kehring は 2025-10 の会議の登壇者で、2026 年の登壇者としては確認できなかった [S21]。
- キャパシティ: FY26 末で約 3GW、FY28 末までに約 10GW(Melius は新規約 7GW)。Morgan Stanley の Singh が言及 [S22,S23]。会社のスライド原文は未確認。
- 契約関連: 2026-09 時点の RPO は 6,640 億ドル(前年比 +2,090 億ドル)。新規バックログの大半は前払いまたは BYO ハードウェアで、capex・売上への影響は FY28 以降(Maxson, Q1 call)[S10,S6]。
- CryptoBriefing は Investor Day で「AI インフラ契約の RPO 約 800 億ドル、対応する capex 約 370 億ドル」と報じた。他に裏付けなし、種類不明(低信頼)[S24]。

### FY27 ガイダンスの変更の経緯(8.05 と 8.10 の関係)
| 時点 | 売上 | 非GAAP EPS | 出典 |
|---|---|---|---|
| 2025-10-16(Financial Analyst Meeting) | not found | 8.00 ドル(Stocktitan の比較表。原表は Oracle の CFO 資料 2025-10-16 とされる)| S4 |
| 2026-06-10(Q4 FY26 決算) | 900 億ドル(従来ガイダンスの確認) | 8.05 ドル(FY26 の一時要因を除き +18%) | S9 |
| 2026-09-10(Q1 FY27 決算) | 900 億ドル以上(+約 34%) | 8.10 ドル(Q1 実績 1.92 ドル、会社ガイダンス 1.72〜1.76、コンセンサス 1.74)| S6 |
| 2026-10-28(Investor Day) | 900 億ドル以上を再確認 | 8.10 ドルを再確認 | S1,S2,S3 |
- Q2 FY27 ガイダンス: 総売上 +30〜34%、非GAAP EPS 1.85〜1.93 ドル(米ドルでの EPS 成長 21〜25% は前年の Ampere 一時益を除く)[S8]。
- つまり FY27 は Investor Day で変更されず(6月 8.05 → 9月 8.10 の変更は Investor Day より前)。
- capex は、June の情報に差がある。「純現金 capex 約 700 億ドル」「約 400 億ドルを債務・株式で調達」と書く二次情報あり [S12]。「FY27 capex 350〜400 億ドル」と書く低品質ソースもあり、他と不一致(未確認)。
- Q4 FY26 実績(二次情報): 売上 192 億ドル(+21%)、OCI 58 億ドル(+93%)、RPO 6,380 億ドル、FY26 capex 557 億ドル [S9,S25]。

## 2. 前年 FAM(2025-10-16 Financial Analyst Meeting)との対照

| 項目 | 2025-10-16 FAM | 2026-10-28 Investor Day | 変化の事実 / 出典 |
|---|---|---|---|
| FY30 売上 | 2,250 億ドル(年平均成長率 31%、FY25 の 574 億ドルが起点)[S21,S26] | 2,250 億ドル以上(年平均成長率 35% 超、FY26 起点)[S1,S5] | 金額は同じ。表現が「以上」に。成長率の起点年が違う(FY25→FY26)。Stocktitan は「2030 目標を据え置き」[S4]。Moomoo は「前年と同じ」[S27] |
| FY30 EPS | 21 ドル(Stocktitan 表:21.00)[S4,S21] | 21 ドル以上 | 表現が「以上」に。上方修正の数値は無し。 |
| FY30 営業利益率 | 目標なし(Stocktitan の整理:2025-10 は利益率目標無し、40% は 2026 で初出)[S4] | 40% 以上 | 単一ソース。他のソースは「据え置き」と記載(不一致:Stocktitan は同じ記事内で「据え置き」とも書き、利益率は初出とも読める)。要原文確認 |
| FY30 OCI 売上 | 1,660 億ドル(総売上の約 75%)。それ以前は 1,440 億ドル [S7,S21,S28] | not found | 2026 の目標は見つからず。OCI 目標の変更有無は不明 |
| OCI 年度別の道筋 | Cloud Wars: FY25 100 億 / FY26 150 億 / FY27 340 億 / FY28 770 億 / FY29 1,290 億 / FY30 1,660 億ドル [S28]。別の要約(TradingView 系、日付不明)は FY26 180 / FY27 320 / FY28 730 / FY29 1,140 / FY30 1,440 億ドル [S28 検索結果内] | not found | **不一致**:同じ 2025 年の OCI 年度系列が 2 通り。後者は FY30=1,440 億ドルなので、1,660 億ドルに上方修正される前(2025-09 時点)の系列の可能性があるが、日付は未確認 |
| FY27 EPS | 8.00 ドル(Stocktitan 表)[S4] | 8.10 ドル | +0.10。うち 8.05→8.10 は 9/10 の変更 |
| FY27 売上 | not found | 900 億ドル以上 | — |
| データベース / AI データ基盤 | CreditSights: AI Database + AI Data Platform が FY30 に 200 億ドル [S29]。Cloud Wars: データベース事業は FY30 に 200 億ドルに到達しうる、マルチクラウド分がそれに近い規模(Ellison の発言)[S28] | not found | 2026 年版の目標は見つからず |
| アプリ(SaaS)/ ライセンス・サポート | not found | not found | セグメント別の年度目標は両年とも見つからず |
| FCF | 2025-10 時点の FCF 目標: not found | FY28 下期に黒字化、FY29 300 億ドル以上 | **新規の項目**(2025 年版に同等の目標を示す記事は見つからず)。Bloomberg:FY29 の FCF はマイナス想定が市場に残っていた [S14] |
| 資金調達の上限 | not found | 追加 200 億ドル(FY27〜FY30)| 新規。Proactive: 市場の想定は約 500 億ドル [S17] |
| capex | not found | FY27〜28 ピーク、FY29 減少 | 新規(金額なし)|
| ネットデット/EBITDA | not found | FY29 に 3.5 倍未満 | 新規 [S15] |

- 「会社説明で EPS を含む見通しが大きく変わった」という利用者の指摘について: 今回確認できた範囲では、会社の EPS の数字(FY27 8.10、FY30 21 ドル以上)に大きな変更は見つからなかった。変わったと報じられている点は、FCF の時期と額、資金調達の上限、capex のピーク時期、利益率目標(単一ソース)。年度別 EPS(FY28/FY29)の変更は、スライドを読めなかったため未確認。

## 3. アナリストの予想変更・反応

### 3-1. EPS 予想(確認できたもの)
| 主体 | 年度 | 数値 | 時点・内容 | 出典 |
|---|---|---|---|---|
| Melius(Ben Reitzes) | FY29 | **16.76 ドル** | Investor Day 後に Buy・目標株価 170 ドルを再確認。170 ドル ≒ FY29 EPS の約 10 倍(EV/売上 約 3.5 倍も言及)。**変更前の FY29 EPS は not found**(上げたか下げたかは確認できず) | S23,S30 |
| コンセンサス(TIKR 経由 Yahoo、正規化 EPS) | FY27 / FY28 / FY29 | 8.14 / 10.99 / 15.77 ドル | Investor Day 前(10/27 付記事)| S31 |
| Oppenheimer 記事内のコンセンサス | FY27 / FY28 | 8.14 / 10.99 ドル(3 か月前は 8.05 / 10.89)| 10/29 付。3 か月で +0.09 / +0.10 | S32 |
| Yahoo 分析ページ | FY28 | 平均 10.99 ドル、39 人、レンジ 9.00〜13.30 | 日付未確認。直近 30 日でほぼ変化なし | S33 |
| Erste Group | FY28 | 9.32 ドル(従来 9.27)| 10/21(Investor Day 前)| S34 |
| 第三者モデル(vcpscanner) | FY26A〜FY30E の希薄化後 EPS | 5.83 / 7.90 / 9.84 / 10.07 / 11.23 ドル | コンセンサスではない・種類不明(信頼度低)。FY30E 11.23 は会社目標 21 ドルと大きく離れる | S35 |
- Investor Day 後に FY28・FY29・FY30 の EPS 予想を上げた・下げたと明記した報道: **not found**(複数回検索)。
- FY30 EPS のコンセンサス: not found。

### 3-2. 売上・FCF・capex の市場予想(Investor Day 前の比較値)
- FY28 売上: 1,317.9 億ドル(Yahoo/TIKR 系)、1,314.5 億ドル、約 1,314 億ドル(Simply Wall St、39 人)、約 1,300 億ドル(Stocktitan)。FY29 売上: 1,838.1 億ドル。FY27 売上: 約 904.8 億ドル [S36,S37,S28]。
- FY30 売上: LSEG 集計の予想 2,242 億ドル。会社目標はこれをわずかに上回る [S38]。CNBC 要約には「LSEG は FY27 の成長率 8% を予想」とあるが、FY27 の 900 億ドルガイダンス(+約 34%)と整合しない記述(原文未確認)[S39]。
- FCF: FactSet(CNBC 経由)で FY27・FY28 ともに約 -350 億ドル。ある分析は「会社の黒字化時期は市場想定より 12 か月以上早い」[S39,S14]。FY29 の FCF の市場予想は **不一致**:Bloomberg「マイナス想定」、TIKR「+59 億ドル」[S14,S40]。
- capex: Wells Fargo(Turrin)の FY28 予想 1,640 億ドル。コンセンサスは FY28 が 1,060 億ドルでピーク、FY30 に 860 億ドル [S41]。
- S&P は 2026-07 に BBB- へ格下げし、FY27 の営業FCF赤字を約 420 億ドルと予想 [S42]。

### 3-3. 格付け・目標株価(Investor Day 後、EPS 変更の記載なし)
- Jefferies: Buy・290 ドル(維持)[S43]。BNP Paribas(Slowinski): Outperform・248 ドル、200 億ドルを超える追加資本は不要との見方 [S43]。Oppenheimer(Schwartz): Outperform・275 ドル(10/29)[S32]。TD Cowen: Buy・240 ドル(10/29)[S44]。Guggenheim: Buy [S27]。Morgan Stanley(Singh): Equal-weight・210 ドル、FY28 までの約 10GW と、拡大期にも利益率が 40% 付近を保つことの確認が必要と発言 [S22]。RBC: Hold 相当・165 ドル [S30]。Goldman: Investor Day 前に目標を 206 ドルへ引き下げ(Investor Day 後の更新は not found)[S45]。
- 集計値の不一致:平均目標株価 235.80 ドル(S30)/ 237.36 ドル(S&P Global, 43 人)/ 248.41 ドル・249.52 ドル(MarketBeat)[S30,S33,S46]。

### 3-4. 株価反応の理由として報道が挙げた内容
- 10/28 終値 144.54 ドル、+10.73%(日中は約 12%)、出来高 7,910 万株。5 か月で最大の上げ(2026 年 5 月以来)[S39,S14]。報道によっては +9〜10%(GuruFocus)、+14% まで(daily.dev)と幅がある(不一致)[S47]。
- 理由として挙げられた点: (a) 追加資金調達の上限 200 億ドル(市場想定は約 500 億ドル)、(b) FCF が FY28 下期に黒字化・FY29 に 300 億ドル以上、(c) capex が FY27〜28 でピーク、(d) FY30 売上 2,250 億ドル以上(ただし市場予想 2,242 億ドルとほぼ同水準と複数の記事が記述)[S17,S39,S14,S2]。
- 「見通しの変化」の内容として報じられたのは主に FCF の時期・金額、調達上限、capex 方向、ネットデット/EBITDA。EPS や売上の目標が上方修正されたという報道は見つからなかった。
- 10/29 は約 -4%(ハイテク株安、Nasdaq -1.38%)。アナリストが挙げたリスクは実行、電力、許認可 [S48]。

## 4. not found 一覧(推測で埋めていない)
- FY28・FY29 の 売上 / OCI 売上 / クラウド売上 / 非GAAP EPS / GAAP EPS / 営業利益率 / 営業CF / capex 金額(会社)
- FY31・FY32 の全項目
- 2026 年版の FY30 OCI 売上目標、アプリ・データベース(マルチクラウド)・ライセンス&サポートの年度別目標・CAGR
- Investor Day 後に FY28/FY29/FY30 EPS を上げた・下げたアナリストの具体例(Melius の変更前の値を含む)
- スライド原文(Maxson 資料、各セグメント責任者の資料)・書き起こしの本文(stockanalysis の書き起こしは存在するが未読)
- 次の一手(利用者側で可能なら): `s23.q4cdn.com/440135859/files/doc_downloads/2026/10/Oracle-Investor-Day-Meeting/` 配下の各 PDF と stockanalysis の書き起こし(`stockanalysis.com/stocks/orcl/transcripts/780561-investor-day-2026/`)を直接開いて、FY28/FY29 の数字の有無を確認する。

## 出典一覧(いずれも検索結果の要約で確認。原文は未読)
S1 PR Newswire / Oracle IR: https://www.prnewswire.com/news-releases/oracle-investor-day-2026-accelerating-value-creation-302922564.html , https://investor.oracle.com/investor-news/news-details/2026/Oracle-Investor-Day-2026-Accelerating-Value-Creation/default.aspx
S2 SEC 8-K 別紙 99.1: https://www.sec.gov/Archives/edgar/data/0001341439/000119312526435853/d75538dex991.htm
S3 Investing News: https://investingnews.com/oracle-investor-day-2026-accelerating-value-creation/
S4 Stocktitan(比較表・資金上限): https://www.stocktitan.net/articles/oracle-stock-investor-day-2026-20-billion-funding-cap
S5 Stocktitan(リリース要約): https://www.stocktitan.net/news/ORCL/oracle-investor-day-2026-accelerating-value-josi685spepl.html ; Investing.com: https://www.investing.com/news/stock-market-news/oracle-shares-jump-as-longterm-outlook-targets-225-billion-in-revenue-4980445
S6 r40.io Q1 FY27 分析: https://r40.io/news/orcl-q1-fy2027-reported-earnings-analysis/ ; Oracle Q1 リリース: https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/ ; Tradingkey: https://www.tradingkey.com/news/transcripts/262162053-tradingkey
S7 Reuters(Investing.com 転載): https://www.investing.com/news/stock-market-news/oracle-expects-cloud-infrastructure-revenue-to-be-166-billion-in-fy30-4292932
S8 thestockobserver: https://www.thestockobserver.com/2026/09/12/oracle-nyseorcl-releases-q2-2027-earnings-guidance.html ; TIKR: https://www.tikr.com/blog/oracle-soars-12-after-pairing-its-225-billion-target-with-a-funding-cap
S9 Oracle Q4 FY26 リリース: https://www.oracle.com/news/announcement/q4fy26-earnings-release-2026-06-10/ ; 8-K: https://www.sec.gov/Archives/edgar/data/0001341439/000119312526265848/orcl-ex99_1.htm
S10 Q1 FY27 call 書き起こし: https://www.alphaspread.com/security/nyse/orcl/investor-relations/earnings-call/q1-2027 ; https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/
S11 Terrain Labs: https://terrainlabs.substack.com/p/orcl-oracle-new-debt-20ji ; BigGo: https://finance.biggo.com/news/08238759-5fd0-44b6-b29d-195d8a9e6849
S12 Tradingkey Q4 FY26: https://www.tradingkey.com/analysis/stocks/us-stocks/262124382-oracle-orcl-q4-fy2026-19-2b-revenue-oci-5-8b-93-rpo-638b-fy2027-90b-capex-financing-risk-tradingkey
S13 24/7 Wall St: https://247wallst.com/investing/2026/10/29/oracle-just-promised-30-billion-in-free-cash-flow-after-capping-new-borrowing-at-20-billion/ ; vcpscanner/TIKR 等
S14 Bloomberg: https://www.bloomberg.com/news/articles/2026-10-28/oracle-projects-30-billion-free-cash-flow-in-fiscal-2029 ; Investing.com(Reuters): https://www.investing.com/news/stock-market-news/oracle-expects-to-turn-cash-flow-positive-in-second-half-of-fiscal-2028-4980458
S15 StreetInsider: https://www.streetinsider.com/Corporate+News/Oracle+sets+%24225+billion+revenue+target+for+FY30+at+investor+day/27248381.html
S16 Nodiligence: https://nodiligence.substack.com/p/day-41-oracle-caps-new-market-funding
S17 Proactive Investors: https://www.proactiveinvestors.com/companies/news/1100945/oracle-analyst-day-eases-funding-concerns-and-bolsters-growth-outlook-1100945.html
S18 Globe and Mail(リリース転載): https://www.theglobeandmail.com/investing/markets/stocks/ORCL-N/pressreleases/8536378/oracle-unveils-ambitious-long-term-growth-and-profit-targets/
S19 CryptoBriefing: https://cryptobriefing.com/oracle-fy30-outlook-225b-revenue-21-eps/
S20 CNBC: https://www.cnbc.com/2026/10/28/oracle-forecast-growth-2030.html
S21 Oracle Kehring 資料(2025): https://www.oracle.com/a/ocom/docs/corporate/financial-analyst-meeting-2025-kehring.pdf
S22 TipRanks(Morgan Stanley): https://www.tipranks.com/news/article/now-comes-the-hard-part-says-morgan-stanley-about-oracle-stock
S23 Investing.com(Melius): https://www.investing.com/news/analyst-ratings/melius-reiterates-buy-on-oracle-stock-citing-ai-infrastructure-path-93CH-4982635
S24 CryptoBriefing: https://cryptobriefing.com/oracle-80b-ai-infrastructure-investor-day/
S25 Tikr Q4: https://www.tikr.com/blog/oracle-stock-q4-2026-beats-estimates-as-oci-revenue-surges-93-year-over-year
S26 Yahoo(2025-10 後の株価): https://finance.yahoo.com/markets/stocks/articles/oracle-heads-investor-day-goldman-012417326.html
S27 Moomoo: https://www.moomoo.com/community/feed/market-take-oracle-investor-day-three-numbers-that-could-change-117523233832966
S28 Cloud Wars: https://cloudwars.com/cloud-wars-minute/oracle-road-to-225bai-everywhere/
S29 CreditSights: https://know.creditsights.com/insights/oracle-top-10-takeaways-from-2025-analyst-meeting/
S30 beinsure: https://beinsure.com/news/oracle-stock-price-forecast-analysts-see-63-upside/
S31 Yahoo/TIKR: https://finance.yahoo.com/markets/stocks/articles/oracle-stock-down-55-bargain-160902042.html
S32 TIKR(Oppenheimer): https://www.tikr.com/blog/oracle-has-lost-half-its-value-oppenheimer-still-sees-275 ; https://finance.yahoo.com/markets/stocks/articles/oracle-lost-half-value-oppenheimer-185522031.html
S33 Yahoo 分析ページ: https://finance.yahoo.com/quote/ORCL/analysis/ ; StockAnalysis: https://stockanalysis.com/stocks/orcl/forecast/
S34 MarketBeat(Erste): https://www.marketbeat.com/instant-alerts/estimates-fy2028-eps-estimates-for-oracle-raised-by-erste-group-bank-2026-10-23/
S35 vcpscanner: https://vcpscanner.com/valuation/orcl/estimates
S36 Simply Wall St: https://simplywall.st/stocks/us/software/nyse-orcl/oracle/future
S37 Moatexplorer / Cloud Wars 等(FY27/FY28 コンセンサス): https://www.moatexplorer.com/oracle/the-future-bets/225-billion-by-fiscal-2030/
S38 BigGo(LSEG FY30 2,242 億ドル): https://finance.biggo.com/news/eebcbdbc-a31f-4a8b-8cf3-a57290c1c785
S39 CNBC / TipRanks: https://www.tipranks.com/news/oracle-stock-orcl-surged-11-as-investor-day-eased-spending-fears-and-set-solid-fy30-outlook
S40 TIKR FCF: https://www.tikr.com/blog/oracle-is-up-12-in-a-week-is-its-free-cash-flow-plan-really-that-good
S41 TipRanks(Wells Fargo preview): https://www.tipranks.com/news/article/oracles-investor-day-is-coming-heres-the-answer-wells-fargo-wants-on-the-stock
S42 Nodiligence(S&P): 同 S16 ; Globe and Mail: https://www.theglobeandmail.com/business/article-oracle-earnings-profit-ai-maxson/
S43 Benzinga 系(BNP, Jefferies): https://www.tradingview.com/news/benzinga:a95591957094b:0-oracle-s-ai-spending-spree-may-finally-have-an-end-in-sight/
S44 Yahoo(TD Cowen): https://finance.yahoo.com/quote/ORCL/
S45 Yahoo(Goldman): 同 S26
S46 MarketBeat: https://www.marketbeat.com/stocks/NYSE/ORCL/forecast/
S47 GuruFocus: https://www.gurufocus.com/news/9150510/oracle-orcl-surges-10-after-analyst-day-reassuring-investors-on-ai-costs ; daily.dev: https://daily.dev/posts/oracle-targets-30b-in-free-cash-flow-by-fiscal-2029-and-shares-jump-as-much-as-14--uhxkh3zle
S48 Invezz: https://invezz.com/news/2026/10/29/oracle-stock-falls-4-why-experts-arent-bothered/
