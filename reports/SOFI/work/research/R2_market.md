# R2: SOFI 市場データ・コンセンサス(取得日 2026-10-18、基準日=直近取引日 2026-10-16(金)終値)

## 0. 取得方法と信頼度の注意(必読)

- **WebFetchは全ドメインで `getaddrinfo ENOTFOUND`(DNS解決不可)で使えなかった**(tradingview.com, stockanalysis.com, finance.yahoo.com, tickflow.io, 247wallst.com, federalreserve.gov で確認)。Bash(curl)経由は egress proxy が stockanalysis.com を403拒否(許可ホスト外)。回避は試みていない。
- したがって**全数値は WebSearch の検索結果要約(検索ツール内の要約モデルが各ページ断片から作った文章)経由の二次情報**。ページ本文を直接読んだものではない。各行の「出所」は検索結果に現れたURL。数値の桁・日付は一次ページで要再確認(特に TradingView の年度別EPSは取れていない)。
- 途中で WebSearch の1ターン上限(200回、他エージェントと共有)に達し、**ピア比較・金利環境は未取得**(§4, §5)。
- 「計算」と書いたものは私の算術。出所の値ではない。
- 株価の基準: **2026-10-16(金)終値 $14.55**(§1)。

---

## 1. SOFI 市場データ

| 項目 | 値 | 基準日 | 出所 |
|---|---|---|---|
| 直近終値 | **$14.55**(前日比 -$0.54 / -3.58%)。寄り $15.08、日中 $14.33–15.54。時間外 $14.46(別表記 $14.44) | 2026-10-16 | HeyGoTrade https://www.heygotrade.com/en/us-stock/sofi/ 、StockAnalysis https://stockanalysis.com/stocks/sofi/ 、Yahoo(検索要約で「両者が14.55」と記載) |
| 前日終値 | $15.09(+6.12%、+$0.87)。日中安値 $13.86(52週安値更新)〜高値 $15.13 | 2026-10-15 | HeyGoTrade https://www.heygotrade.com/en/news/sofi-sofi-stock-news-october-16-2026/ (見出し「Oct 16: SOFI Rises 6.1% to $15.09」は実際は10/15の動き) |
| 前々日終値 | $14.22(-6.69%)。「予想より強いインフレ指標で金利上昇懸念が再燃」「銀行株の弱さ」と報道 | 2026-10-14 | HeyGoTrade https://www.heygotrade.com/en/news/sofi-sofi-stock-news-october-15-2026/ 、Motley Fool https://www.fool.com/coverage/stock-market-today/2026/10/14/stock-market-today-oct-14-sofi-technologies-falls-on-banking-weakness/ |
| 時価総額 | **約 $18.79B** | 2026-10-16終値ベース | StockAnalysis https://stockanalysis.com/stocks/sofi/ (検索要約) |
| 発行済株式数 | **1,290,312千株(約12.90億株)** 2026-06-30時点 | 2026-06-30 | SoFi 2026Q2決算リリース(8-K)の調整表 https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000050/a2026q2earningsrelease.htm (検索要約経由) |
| 時価総額の検算 | 1.2903B株 × $14.55 = **$18.77B**(計算)。StockAnalysis値と整合 | - | 計算 |
| 発行済株式の増加率 | 前年比 +14.49%(増資の影響) | 約2026-07末のスナップショット | StockAnalysis https://stockanalysis.com/stocks/sofi/statistics/ |
| 52週高値 / 安値 | **$32.73 / $13.86**。高値は2025年11月(別ソースでは「2025年10月高値」とも。食い違い参照)。安値は2026-10-15日中 | 2026-10-16 | StockAnalysis(検索要約)、Yahoo/Motley Fool系記事 |
| 現在値の52週レンジ内位置 | 高値比 -55.6%、安値比 +5.0%(計算) | - | 計算 |
| 年初来騰落率 | **-44.4%**(計算: 14.55 / 2026-01-01の$26.18 − 1)。StockAnalysis表示は「約-42%」(日付不明)。24/7 Wall St.(10/15)は$14.22で約-46%(計算でも -45.7%で整合) | 2026-10-16 | MarketBeat($26.18の根拠)https://www.marketbeat.com/stocks/NASDAQ/SOFI/ ; StockAnalysis ; 24/7 https://247wallst.com/investing/2026/10/15/sofi-technologies-imploded-in-2026-a-wall-street-pro-predicts-it-will-double-in-2027/ |
| 出来高 | 10/16: 59,268,765株(StockAnalysis)。10/15: 62.8M(30日平均45.0Mの+39.6%) | 2026-10-15/16 | StockAnalysis; HeyGoTrade |
| 平均出来高 | 45.0M(30日平均、HeyGoTrade 10/15)/ 54M(Morningstar「60M / 54M」)/ 63.66M(MarketBeat、日付不明) | 2026-10 | 上記各社 https://www.morningstar.com/stocks/xnas/sofi/quote 、MarketBeat |
| 空売り(株数) | 188.98M株 = **発行済株式の14.63%**、days to cover 約4.7 | 約2026-07末(StockAnalysis統計ページ、検索ツールで「約81日前」) | https://stockanalysis.com/stocks/sofi/statistics/ |
| 空売り(浮動株比) | **未取得**(浮動株数・直近の空売り残高とも)。補足: 「空売り残高は直近2回の報告期間で+21%」(HeyGoTrade 10/15要約) | - | https://www.heygotrade.com/en/news/sofi-sofi-stock-news-october-15-2026/ |
| 次回決算 | 2026-10-27(寄り前)。Q3 2026 | - | MarketBeat https://www.marketbeat.com/earnings/reports/2026-10-27-sofi-technologies-inc-stock/ 、TipRanks |

### 1-2. 過去12か月(2025-10〜2026-10)の主な株価イベント

| 日付 | イベント | 株価反応 | 出所 |
|---|---|---|---|
| 2025-10-28 | Q3 2025決算。調整後EPS $0.11(予想$0.083)、売上$961.6M(予想$895M)、2025通期ガイダンス引上げ(調整後純収益約$3.54B) | 翌日+5.5%($30.00→$31.66、FXEmpire)。のちZacks「決算後約14%下落」(期間不明) | https://ar.fxempire.com/stocks/sofi/earnings ; Zacks/Barchart(検索要約) |
| 2025-10〜11 | 史上最高値圏。52週高値$32.73(2025年11月とする記事が多い) | - | Yahoo/Motley Fool系(検索要約) |
| 2025-12中旬 | **$1.5B公募増資**。54,545,454株を**$27.50**で価格決定(直前終値約$29.60)。グリーンシュー行使後の合計57,754,660株、2026年1月初旬完了。主幹事GS/BofA/Citi/DB/Mizuho | 発表後 -6〜-8% | SoFi IR https://investors.sofi.com/news/news-details/2025/SoFi-Technologies-Inc--Announces-Pricing-of-Public-Offering-of-Common-Stock-31dc08070/default.aspx ; Investing.com ; Motley Fool 2025-12-13 |
| 2025-12〜2026-01 | 12月に約20%下落、1月に約17%下落 | 同左 | Yahoo/TIKR(検索要約) |
| 2026-01(Q4 2025決算) | 初の売上$1B超(調整後純収益約$1.0B、+37%)、調整後EPS $0.13(予想$0.11〜0.12)、純利益$174M。2026ガイダンス: 調整後純収益約$4.655B、調整後EBITDA約$1.6B、調整後純利益約$825M、調整後EPS約$0.60。中期: 2025〜2028の調整後純収益CAGR 30%以上、EPS CAGR 38〜42% | 反応は出所間で不一致(時間外+4.3%→$25.40とする記事、1/30に-6%超とする記事) | SEC 8-K https://www.sec.gov/Archives/edgar/data/1818874/000181887426000008/a2025q4earningsrelease.htm ; Crowdfund Insider ; MarketBeat |
| 2026-03-17 | **Muddy Waters空売りレポート**。個人ローン実質チャージオフ約6.1%(会社開示2.89%)、未計上債務$312M以上、公正価値手法を指摘。会社は「事実誤認」と反論。CEO Notoが約$50万相当を約$17で買付(TIKR) | 日中-6%、終値$17.37(-1.47%)。3月は月間-10.6%。2026-03-30に高値から-52.96%の最大ドローダウン | Nasdaq/Motley Fool https://www.nasdaq.com/articles/why-sofi-technologies-stock-slipped-last-month ; TIKR https://www.tikr.com/blog/sofi-technologies-beat-earnings-and-still-fell-13-is-sofi-stock-a-buy-in-2026 |
| 2026-04-29 | Q1 2026決算。売上$1.1B、純利益$167M、希薄化後EPS $0.12。技術プラットフォーム部門の弱さ・ガイダンス据置 | **-12.9%**(TIKR) | SEC 8-K https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000020/a2026q1earningsrelease.htm ; TIKR |
| 2026-05 | Citi目標を$37→$30に引下げ | - | MarketBeat https://www.marketbeat.com/instant-alerts/citigroup-has-lowered-expectations-for-sofi-technologies-nasdaqsofi-stock-price-2026-05-04/ |
| 2026-07-29 | Q2 2026決算。調整後純収益$1.22B(+43%)、GAAP純利益$156.6M、GAAP希薄化後EPS $0.12、調整後EPS $0.12(予想$0.11)。純収益ガイダンスを$4.655B→$4.75〜4.85Bに上方修正、調整後EPS約$0.60は据置。技術プラットフォーム収入 -23%(大口顧客離脱)、マーケ費用増 | **約-9〜-10%**(終値約$15.15、sentisense)。ガイダンス据置と高い期待が理由 | BusinessWire https://www.businesswire.com/news/home/20260729569583/en/ ; Invezz https://invezz.com/en-ae/news/2026/07/29/why-did-sofi-stock-fall-despite-earnings-beat-and-higher-2026-outlook/ ; sentisense |
| 2026-10-12〜16 | KBW目標引下げ($16→$15、Q3で$1B超のヘッドウィンド警告)、Goldman目標$18→$15、Benchmark格上げ、Form 144(内部者売却予定)。10/14 -6.7%→10/15 +6.1%→10/16 -3.6% | 52週安値$13.86を10/15に付けて反発 | StocksToTrade https://stockstotrade.com/news/sofi-technologies-inc-sofi-news-2026_10_16/ ; MarketBeat |
| 指数採用・除外 | **未取得**(過去12か月の指数イベントは検索で確認できず) | - | - |

注: 2025-07-31クローズの$1.5B増資($20.85、71,942,450株)は12か月窓の外。

---

## 2. コンセンサス

### 2-0. EPS定義(最重要)

- 会社ガイダンス・コンセンサスは**「調整後EPS(Adjusted EPS)」**。SoFiの調整後EPS定義(検索要約): 普通株主帰属純利益から「取引関連費用、リストラ費用、のれん減損、再発しない一部の税効果」を除外して算出。**株式報酬は除外項目に入っていない**(定義の記載に株式報酬が無い。一次の8-Kで要確認)。
- 実績比較: 2026Q2 GAAP希薄化後EPS $0.12 = 調整後EPS $0.12(調整後純利益$160.4M vs GAAP純利益$156.6M)。2026Q1 GAAP希薄化後EPS $0.12。つまりGAAPと調整後の差は現状小さい。
- StockAnalysis は「EPSとForward PEは非GAAP調整後ベース」と明記。Zacksは「調整後EPS」と明記。TradingViewの定義は**未確認**(ページ未取得)。
- 食い違い: Zacks系記事の一つは2026ガイダンスを「GAAP EPS約$0.60」と表記、Barchartは「調整後EPS約$0.60」。会社の8-K文言は「adjusted EPS of approximately 60 cents」(検索要約)なので調整後が正。

### 2-1. 年度別EPSコンセンサス(出典を並べる)

| 出典 | FY2026 | FY2027 | FY2028 | 備考(アナリスト数・レンジ) | 基準日 | URL |
|---|---|---|---|---|---|---|
| **TradingView** | **未取得** | **未取得** | **未取得** | ページ本文は読めず。検索要約から判明: 直近四半期EPS $0.12(予想$0.11)、次四半期予想$0.17(別ページ・古いスナップショットでは$0.11)、目標株価レンジ$12〜$30(23アナリスト、平均は要約に出ず) | スナップショット日不明 | https://www.tradingview.com/symbols/NASDAQ-SOFI/forecast/ |
| Yahoo Finance(Analysis) | 0.59(レンジ0.56〜0.63) | 0.82(レンジ0.78〜0.88) | 未取得 | EPS 9アナリスト。キャッシュで日付不明 | 不明(2026-10頃) | https://finance.yahoo.com/quote/SOFI/analysis/ |
| StockAnalysis(S&P Global) | 0.60(前年0.37) | 0.83 | 未取得(2028は出ない) | ページ更新日が古い可能性(ツール表示「約113日前」) | 不明 | https://stockanalysis.com/stocks/sofi/forecast/ |
| Chartmill | 0.61 | 0.84 | **1.08** | 更新「約11日前」(約2026-10-07) | 約2026-10-07 | https://www.chartmill.com/stock/quote/SOFI/estimates |
| WallStreetZen | 0.61(レンジ0.55〜0.68。利益ベース$706M〜$881M) | 0.84(レンジ0.74〜0.94) | **1.08**(最小0.95、最大1.27) | 約29アナリスト(EPS・売上の平均)。ページは9月スナップショットとの記載も | 約2026-09〜10-03 | https://www.wallstreetzen.com/stocks/us/nasdaq/sofi/stock-forecast |
| Zacks(Yahoo記事経由) | 0.60 / 0.59(記事により) | 0.81 / 0.78(記事により) | 未取得 | Zacks Rank #3。FY2027成長+36.1% | 記事日不明 | https://finance.yahoo.com/markets/stocks/articles/investors-heavily-search-sofi-technologies-120005687.html |
| 24/7 Wall St.(Yahoo転載) | 0.59 | 0.82(+39%) | 未取得 | コンセンサス引用 | 2026-10-06 | https://247wallst.com/investing/2026/10/06/sofis-next-growth-engine-could-surprise-wall-street/ |
| Barchart | 0.59 | 0.80 | 未取得 | 決算前記事 | 2026-07 | https://www.barchart.com/story/news/3528189/dear-sofi-stock-fans-mark-your-calendars-for-july-29 |
| Tickflow | 0.61 | 未取得 | 未取得 | 21アナリスト、Hold | 2026-07-31 | https://tickflow.io/stock/SOFI/forecast |
| Valueinvesting.io | 未取得 | 0.8(レンジ0.7〜0.9) | 未取得 | - | 不明 | https://valueinvesting.io/SOFI/estimates |
| 個別: Piper Sandler | 0.63 | 0.88 | 未取得 | 2026-08 カバレッジ開始時 | 2026-08-17 | https://www.webull.ca/news-detail/15418981152343040 |
| 個別: Hated Moats(Substack) | - | - | 1.03 | 価格$15.92時点の引用。出所不明 | 不明 | https://hatedmoats.substack.com/p/sofi-dcf-valuation |
| **会社ガイダンス** | **調整後EPS 約$0.60**(調整後純利益約$825M) | - | - | 中期: EPS CAGR 38〜42%(〜2028年) | 2026-07-29 | SEC 8-K Q2 2026 |

**出典を横断した幅(計算でなく読み取り)**: FY2026 = 0.59〜0.61、FY2027 = 0.78〜0.84(最新2ソースは0.84)、FY2028 = 1.08(2ソース。他に1.03)。

### 2-2. 売上コンセンサス

| 出典 | FY2026 | FY2027 | FY2028 | 基準日 |
|---|---|---|---|---|
| Yahoo | $4.88B | $6.1B | 未取得 | 不明 |
| StockAnalysis | $4.89B(前年$3.58B) | $6.16B | 未取得 | 不明 |
| Chartmill | 約$4.965B | 約$6.148B | 約$7.578B | 約2026-10-07 |
| WallStreetZen | 約$5.0B | 約$6.1B | 約$7.6B | 約2026-09〜10 |
| Zacks(Yahoo記事経由) | $4.87B | $5.85B | 未取得 | 不明 |
| Valueinvesting.io | - | $5.8B | - | 不明 |
| Piper Sandler(個別) | - | $6.14B | - | 2026-08 |
| 会社ガイダンス | 調整後純収益 $4.75〜4.85B(+32〜35%) | - | - | 2026-07-29 |

- 売上の最高/最低レンジは**未取得**。
- 注: コンセンサス売上(約$4.9〜5.0B)は会社ガイダンスの「調整後純収益」($4.75〜4.85B)より高い。定義(総純収益 vs 調整後純収益、データベンダー差)の違いの可能性。出所で未確認。

### 2-3. 四半期EPS

| 四半期 | EPS予想 | 売上予想 | 出所/基準日 |
|---|---|---|---|
| Q3 2026(10/27発表) | **$0.17**(前年同期比+54.5%) | $1.25B(TipRanks, MarketBeat)〜$1.278B(Chartmill) | TipRanks https://www.tipranks.com/stocks/sofi/earnings ; Chartmill https://www.chartmill.com/stock/quote/SOFI/estimates ; 2026-10上旬 |
| Q4 2026 | **未取得** | 未取得 | - |
| (参考・計算)Q4 2026の逆算 | 0.60 − Q1 0.12 − Q2 0.12 − Q3 0.17 = **約0.19** | - | 計算。Q1の調整後EPSは未確認でGAAP値0.12を仮置き。低信頼 |

過去実績: Q2 2026 調整後EPS $0.12(予想$0.11)。直近4四半期で3回上振れ・1回下振れ(TipRanks要約)。

### 2-4. 目標株価コンセンサス(出典間で食い違いが大きい)

| 出典 | 平均 | 最高 | 最低 | 中央値 | アナリスト数 | レーティング | 基準日 |
|---|---|---|---|---|---|---|---|
| StockAnalysis(S&P Global) | $20.34(+20.78%、逆算価格$16.84)/ 別ページ$20.36(25名) | $30 | $12 | $19 | 26 | Hold | 不明(株価$16.84は10月前の可能性)。URL https://stockanalysis.com/stocks/sofi/forecast/ |
| MarketBeat | **$22.20** | $35 | $15 | - | 24 | Hold(Strong Buy 2 / Buy 9 / Hold 11 / Sell 3) | 2026-10-16 https://www.marketbeat.com/instant-alerts/consensus-sofi-technologies-inc-nasdaq-sofi-stock-has-consensus-target-price-of-2220-according-to-analysts-2026-10-16/ |
| TipRanks | $20.37(株価ページ)/ $20.57・$20.67(記事) | - | - | - | 17(株価ページ)/ 記事では Buy7・Hold7・Sell3 | Hold | 2026-10中旬 https://www.tipranks.com/stocks/sofi |
| WallStreetZen | $21.07 | $30(Citi) | $15(Morgan Stanley) | - | 15 | Hold(Strong Buy 3 / Buy 3 / Hold 7 / Sell 1 / Strong Sell 1) | 約2026-09 |
| Benzinga記事 | $21.82(14名)/ $19(22名) | $30 | - | - | 14 / 22(Buy・Strong Buy 9、Hold 9、残り4が売り系=計算) | - | 2026-10上旬 https://www.benzinga.com/analyst-stock-ratings/initiation/26/10/62324182/sofi-stock-is-cheap-now-stonex-says-after-40-drop |
| TradingView | 平均未取得 | $30 | $12 | - | 23 | 未取得 | 不明 |
| Tickflow | $21.40 | - | - | - | 21 | Hold | 2026-07-31 |

計算: $14.55に対する平均目標乖離 = StockAnalysis +39.8%、MarketBeat +52.6%、WSZ +44.8%、Benzinga(19ドル) +30.6%。

---

## 3. アナリスト

### 3-1. レーティング分布(各社、異なる集計)

MarketBeat 2026-10-16: Strong Buy 2 / Buy 9 / Hold 11 / Sell 3(24名)。同社の予測ページ別版は Strong Buy 1(Benchmarkの格上げ前後の差)。他社は §2-4。

### 3-2. 直近3か月(2026-07-18〜10-18)の目標株価・格付変更

| 日付 | 会社 | アナリスト | 格付 | 目標株価(旧→新) | 出所 |
|---|---|---|---|---|---|
| 2026-10-13 | Goldman Sachs | Michael Ng(MarketBeat)/ Will Nance(別ソース)← 要確認 | Neutral | $18 → **$15** | MarketBeat forecast / TipRanks(検索要約) |
| 2026-10-12(Mon) | Benchmark | 不明 | **格上げ→Strong Buy(MarketBeat表記)** | 目標株価不明 | https://www.marketbeat.com/instant-alerts/analyst-sofi-technologies-nasdaq-sofi-upgraded-at-benchmark-2026-10-14/ (記事日は10/14、表上の日付は10/12) |
| 2026-10-12頃 | Keefe, Bruyette & Woods | Tim Switzer | Underperform(Sell) | $16 → **$15** | TipRanks https://www.tipranks.com/news/sofi-stock-forecast-kbw-analyst-stays-bearish-ahead-of-q3-earnings-on-oct-27-heres-why ; StocksToTrade |
| 2026-10(日付未確認) | StoneX | 不明 | **新規 Buy** | **$25** | Benzinga(上記URL) |
| 2026-10-06 | TD Cowen | Moshe Orenbuch | Hold | $18 → **$17.50** | TipRanks/Benzinga(検索要約) |
| 2026-09-09(MarketBeatでは09-08) | Loop Capital | 不明 | 新規 Hold | **$22** | Benzinga ratings https://www.benzinga.com/stock/SOFI/ratings |
| 2026-09-02 | Scotiabank | 不明 | 新規 Sector Outperform | **$25**(Benzinga 10月記事では$17.50と食い違い) | MarketBeat https://www.marketbeat.com/instant-alerts/analyst-sofi-technologies-nasdaq-sofi-now-covered-by-analysts-at-scotiabank-2026-09-02/ |
| 2026-08-17 | Piper Sandler | 不明 | 新規 Overweight | **$22**(EPS予想 2026: 0.63 / 2027: 0.88) | Webull/Benzinga |
| 2026-08-12 | Truist | Matthew Coad | Hold | $18 → **$19** | Benzinga ratings |
| 2026-07-31 | Mizuho | Dan Dolev | Outperform | $29 → **$22** | Benzinga ratings; MarketBeat https://www.marketbeat.com/instant-alerts/mizuho-lowers-sofi-technologies-nasdaqsofi-price-target-to-2200-2026-07-31/ |
| 2026-07-31 | Citi | Peter Christiansen | Buy | $30 維持(5月に$37→$30) | TipRanks forecast(検索要約) |
| 2026-07-30 | Morgan Stanley | 不明 | Underweight(Sell) | $16 → **$15** | Benzinga ratings; MarketBeat |
| 2026-07-30 | Wells Fargo | 不明 | Equal-Weight | $18 → **$17** | 同上 |
| 2026-07-30 | Needham | 不明 | Buy | **$24**(旧値不明) | MarketBeat(検索要約) |

注: 上記はMarketBeat/Benzinga/TipRanksの検索要約から拾った範囲で、**網羅ではない**。全社の完全な履歴表は未取得。

---

## 4. ピア比較(NU, HOOD, ALLY, COF, AXP, LC, UPST, CHYM, AFRM, JPM)

**未取得**。WebSearch上限到達(および WebFetch不通)のため、10社とも株価・時価総額・予想PER・EPS成長率・PEG・P/TBV・ROEを取得できていない。推測では埋めていない。

### 4-1. SOFI 行(単独。ピアと揃えた日付ではない点に注意)

| 項目 | 値 | 区分 / 出所 |
|---|---|---|
| 株価 | $14.55(2026-10-16) | §1 |
| 時価総額 | $18.79B | StockAnalysis |
| 予想PER 今期(FY2026) | 24.7x(EPS 0.59) / 24.3x(0.60) / 23.9x(0.61) | 計算: 14.55 ÷ 各コンセンサス |
| 予想PER 来期(FY2027) | 17.7x(0.82) / 17.5x(0.83) / 17.3x(0.84) | 計算 |
| FY2028 PER | 13.5x(EPS 1.08) | 計算 |
| EPS成長率(FY26→FY27) | +39.0%(0.59→0.82)/ +38.3%(0.60→0.83)/ +37.7%(0.61→0.84) | 計算 |
| EPS成長率(FY27→FY28) | +28.6%(0.84→1.08) | 計算(Chartmill/WSZ) |
| EPS CAGR(FY26→FY28、2年) | +33.1%((1.08/0.61)^0.5−1) | 計算 |
| PEG(出典値) | **0.56**、forward PE 21.59、trailing PE 33.21 | StockAnalysis統計ページ、約2026-07末スナップショット。定義・成長率期間は未確認。https://stockanalysis.com/stocks/sofi/statistics/ |
| PEG(自己計算) | 0.72 = 今期PER 23.85 ÷ 2年CAGR 33.1(%)。別法: 今期PER 24.25 ÷ FY26→27成長38.3(%) = 0.63 | 計算(式明記)。出典の3〜5年成長率は未取得 |
| 参考 forward PE(別スナップショット) | 29.40(2026-03、ratios)/ 28.24(FY2026)/ 約21倍(24/7 Wall St. 10/15記事) | StockAnalysis ratios; 24/7 |
| P/TBV | **1.98x**(14.55 ÷ TBVPS $7.34) | 計算。TBVPS $7.34(2026-06-30、前年同期$4.72、+56%)は2026Q2 8-K |
| P/B | 1.70x(14.55 ÷ BVPS $8.58) | 計算。BVPS $8.58(前年$6.16) |
| 有形自己資本 | 約$9.47B(約$9.5B、四半期で約+$226M) | 8-K / Investing.com |
| ROTCE | **7.1%**(2026Q2、Investing.com単独。8-K要約では確認できず)。自己計算: GAAP純利益$156.6M×4 ÷ 有形自己資本$9.47B = 6.6%(期末ベース) | https://www.investing.com/news/company-news/sofi-q2-2026-slides-record-growth-meets-investor-caution-on-spending-93CH-4820546 |
| 会社の長期ROTCE目標 | 20〜30% | 同上 |
| ROE | 未取得 | - |
| 自己資本比率 | 総資本比率18.8%(規制下限10.5%) | Investing.com |
| 2026ガイダンス逆算(計算) | 調整後純利益$825M ÷ EPS 0.60 = 希薄化後株数 約13.75億株(基本株12.90億株より多い) | 計算 |

---

## 5. 金利環境

**未取得**(FF誘導目標、米2年・10年利回り、CME FedWatch、直近FOMC決定、いずれも取れていない)。

取れた定性情報のみ:
- 2026-10-14のSOFI -6.7%は「予想より強いインフレ指標で金利上昇懸念が再燃」「銀行株の弱さ」と報道(HeyGoTrade 10/15、Motley Fool 10/14)。数値(CPI等)は未取得。
- KBWは「公正価値会計・金利上昇・バランスシート急拡大」でQ3に$1B超のヘッドウィンドと推定(TipRanks/StocksToTrade、2026-10)。
- Q2決算後(7月)に「Fedの金利方針の不確実性」を下落要因とする報道(Webull/Barchart要約)。

---

## 6. リバースDCF・織り込み成長率に関する記事(T3/T4候補。個人ブログ・投稿記事)

| 記事 | 内容 | 基準 | 出所 |
|---|---|---|---|
| Seeking Alpha「SoFi: Lackluster Fundamentals And Tough Valuations Vs Oversold Stock」 | 株価は**5年EPS CAGR約42%**を織り込む(直近の利益成長は20%未満)。1年先PER 23.9x | 公開は約5か月前(2026-05頃)。当時の株価水準は記事依存 | https://seekingalpha.com/article/4906004-sofi-lackluster-fundamentals-and-tough-valuations-vs-oversold-stock |
| Hated Moats(Substack)「SoFi: DCF Valuation」 | 株価$15.92で売上・利益率パスを固定し逆算した**割引率約14.5%**(CAPM 14.1%)。$15.92はFY2028 EPS $1.03の15.5倍、当期PERは21.9x | 株価$15.92時点(9月〜10月初旬と推定) | https://hatedmoats.substack.com/p/sofi-dcf-valuation |
| A.L. Capital Advisory | DCFレンジ$10〜$26(株価$17.85で安全余裕+1%) | 株価$17.85時点 | https://alcapitaladvisory.com/research/equities/sofi.html |
| Alpha Spread | ベースケース$19.16(株価$16.73、約13%割安)。売上成長16.3%、割引率8.3%の前提 | 株価$16.73時点 | https://www.alphaspread.com/security/nasdaq/sofi/dcf-valuation |
| Cycledesk(Substack)「Best Growth in Fintech, Worst Stock in Fintech」 | 内容は未確認(タイトルのみ) | - | https://cycledesk.substack.com/p/sofi-technologies-sofi-best-growth |
| 24/7 Wall St. 2026-10-15 | Citi $30(10/15時点で約+111%)は「全てがうまくいく外れ値」。SOFIは約21倍の先行PER。会社は2028年までEPS CAGR 38〜42%をガイド | 株価$14.22時点 | https://247wallst.com/investing/2026/10/15/sofi-technologies-imploded-in-2026-a-wall-street-pro-predicts-it-will-double-in-2027/ |

注: どれも前提(株価日付、割引率、利益率パス)が異なる。株価が$14.55の現在値で再計算した値ではない。

---

## 7. 取れなかった項目

1. **TradingView 年度別EPS/売上(平均・最高・最低・アナリスト数)と目標株価平均**: ページ本文を取得できず。判明したのは目標株価レンジ$12〜$30(23名)と直近/次四半期EPSの断片のみ。TradingViewのEPS定義も未確認。
2. **ピア比較全体**(NU, HOOD, ALLY, COF, AXP, LC, UPST, CHYM, AFRM, JPM): WebSearch上限到達で未着手。
3. **金利環境全体**(FF誘導目標、2年・10年利回り、FedWatch、直近FOMC)。
4. Q4 2026のEPS・売上コンセンサス、売上の最高/最低、FY2028のアナリスト数。
5. 浮動株比の空売り比率と最新の空売り残高(取れたのは約7月末時点の発行済株式比14.63%のみ)。
6. 過去12か月の指数採用・除外イベント。
7. Benchmarkの目標株価、StoneXの正確な日付、各アナリストの完全履歴表。
8. SOFIの現時点のROE、PEGの出典定義(成長率の年数)、ROTCE 7.1%の一次確認。

追加検索が必要なら、WebSearch上限の引上げ(CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION)後に、ピアと金利を優先して再実行するのが効率的。

## 8. 出典間で食い違った数値

| 項目 | 食い違い |
|---|---|
| FY2026 EPS | 0.59(Yahoo, 24/7, Barchart, Zacks一部)/ 0.60(StockAnalysis, Zacks一部, 会社ガイダンス)/ 0.61(Chartmill, WallStreetZen, Tickflow) |
| FY2027 EPS | 0.78(Zacks一部)/ 0.80(Barchart, Valueinvesting)/ 0.81(Zacks)/ 0.82(Yahoo, 24/7)/ 0.83(StockAnalysis)/ 0.84(Chartmill, WSZ) |
| FY2028 EPS | 1.08(Chartmill, WSZ)/ 1.03(Hated Moats、出所不明) |
| FY2026 売上 | $4.87B(Zacks)/ $4.88B(Yahoo)/ $4.89B(StockAnalysis)/ 約$4.965B(Chartmill)/ 約$5.0B(WSZ)。ガイダンスは調整後純収益$4.75〜4.85B。Tickflowの$4.66Bは旧ガイダンス水準で古い可能性 |
| FY2027 売上 | $5.8B(Valueinvesting)/ $5.85B(Zacks)/ $6.1B(Yahoo, WSZ)/ $6.148B(Chartmill)/ $6.16B(StockAnalysis) |
| 目標株価平均 | $19(Benzinga 22名)/ $20.34〜20.36(StockAnalysis)/ $20.37〜20.67(TipRanks)/ $21.07(WSZ)/ $21.40(Tickflow 7/31)/ $21.82(Benzinga 14名)/ $22.20(MarketBeat) |
| 目標株価の最高・最低 | 最高 $30(多数)vs $35(MarketBeat)。最低 $12(StockAnalysis, TradingView)vs $15(MarketBeat, WSZ, KBW/MS/GSの$15) |
| アナリスト数 | 9(Yahoo EPS)/ 14 / 15 / 17 / 21 / 22 / 23 / 24 / 25 / 26 / 約29 |
| Strong Buy数(MarketBeat) | 1(予測ページ)vs 2(10/16記事、Benchmark格上げ後) |
| 52週高値の時期 | 2025年11月(複数)vs 「2025年10月高値」(Seeking Alpha系・TIKR系の記載) |
| 平均出来高 | 45.0M(HeyGoTrade 30日)/ 54M(Morningstar)/ 63.66M(MarketBeat) |
| 10/16終値 | $14.55(HeyGoTrade, StockAnalysis, Yahoo)vs $14.39(StocksToTrade、15:02 ET時点の途中値。採用せず) |
| YTD | -42%(StockAnalysis)/ -44.4%(計算)/ 約-46%(24/7、$14.22時点) |
| 時価総額 | $18.79B(10/16)/ $20.37B(約7月末スナップショット)/ $21.27B(2026-06-12、株価$16.58) |
| forward PE(SOFI) | 21.59(StockAnalysis 約7月末)/ 28.24〜29.40(StockAnalysis 3月)/ 約21倍(24/7)/ 計算値は 23.9〜24.7(今期)・17.3〜17.7(来期) |
| Q3 2026 EPS予想 | $0.17(TipRanks, Chartmill, 他)vs $0.11(TradingView古いスナップショット、陳腐化と判断) |
| Benchmark格上げの日付 | 10/12(MarketBeat表)vs 10/14(記事日) |
| Goldman担当アナリスト | Michael Ng vs Will Nance |
| Scotiabank新規目標 | $25(MarketBeat, Benzinga表)vs $17.50(Benzinga 10月記事、TD Cowenとの混同の可能性) |
| ガイダンスのEPS定義 | 「GAAP約$0.60」(Zacks系記事の一部)vs 「調整後EPS約$0.60」(会社8-K要約, Barchart)。後者を採用 |
