# U3 業界の需給(AI 容量事業): 2026 年 10 月更新

作成日: 2026-10-30 / 担当: 業界調査 / 方針: 事実と出典のみ。評価・意見は書かない。

## 取得上の制約(先に読むこと)
- 本文の数値は WebSearch の要約結果が根拠。WebFetch は aiweekly.co・geekwire.com・webpronews.com で名前解決に失敗し、一次資料(決算 PDF・8-K・書き起こし)を直接開けていない。つまり「一次資料での照合」は未実施。
- 出典の種別を各行に付けた: [一次]=企業・規制当局・指数提供者の自社ページ(検索結果に出た範囲、本文は未取得)、[報道]=報道機関、[集約]=アグリゲーター/ブログ/個人サイト(信頼度低)。
- 数字が食い違うものは「不一致」と明記。見つからないものは「not found」。

---

## 1. 大手クラウド 2026 年 7〜9 月期決算

### 1-1 Microsoft(FY27 Q1、2026-10-28 発表)
| 項目 | 値 | 出典 |
|---|---|---|
| 売上 | $92.3B(+19%)、Microsoft Cloud $63.9B(+30%) | [集約] https://aiweekly.co/alerts/microsoft-q1-revenue-hits-923b-azure-up-48-as-capex-jumps-to-394b-with-175b / [報道] https://finance.biggo.com/news/US_MSFT_2026-10-28 |
| Azure 伸び率 | +48%(Azure 売上 $33.2B)。7月時点の会社ガイダンスは定為替 +44〜45%(Coffee and Earnings の記述)。次四半期(FY27 Q2)ガイダンスは定為替 +49〜50% | [報道] https://www.cnbc.com/2026/10/28/microsoft-msft-q1-earnings-report-2027.html / [集約] https://coffeeandearnings.substack.com/p/microsoft-alphabet-and-stellantis / https://tech-insider.org/microsoft-azure-48-percent-33-2b-cash-flow-ai-spending-fears-2026/ |
| capex(四半期) | 不一致: $45.2B(ファイナンスリース含む、前年比約 +30%、市場予想約 $50B を下回る。第三者の容量納入の遅れが理由)[CNBC・書き起こし要約] / $39.4B(前年の 2 倍超)[aiweekly・247wallst・Motley Fool 系要約]。定義差かどうかは未確認 | https://www.cnbc.com/2026/10/28/microsoft-msft-q1-earnings-report-2027.html / https://singjupost.com/transcript-microsoft-q1-2027-earnings-call/ / https://247wallst.com/cards/microsoft-q1-2027-earnings-msft-01m6223bcjxyqzvby9cw8yzzqb |
| capex の見通し | FY27 Q2 は $50B 超。暦年 2027 は約 $170B(CNBC 系の要約)。不一致: aiweekly は「$175B」を CY2026 のガイドとしている(リース分類変更後)。Microsoft の旧ページには約 $190B の記載もあり(古い可能性。検索側の注記) | https://finance.biggo.com/news/US_MSFT_2026-10-28 / https://aiweekly.co/alerts/microsoft-q1-revenue-hits-923b-azure-up-48-as-capex-jumps-to-394b-with-175b / https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3 |
| 容量の制約 | 「需要は供給を超え続ける」(4 四半期連続との記述あり)。今四半期の主な制約は第三者 GPU 容量。FY27 Q2 に入る予定だった供給の一部が下期へ後ろ倒し。Q2 のガイダンス達成には効率化の追加が必要(Hood)。当四半期に 24 データセンター追加(GuruFocus) | https://www.simpletechtrend.com/en/post/microsoft-q1-fy2027-earnings-azure-48-capex-en / https://www.tradingkey.com/news/transcripts/262249601-tradingkey / https://www.gurufocus.com/news/9151744/microsoft-msft-reports-strong-fy27-start-with-azure-growth-and-positive-outlook |
| 契約残(商業 RPO) | 2026-09-30 時点 $677B(+73%)。2026-06-30 は $677B または $678B(出典で不一致)。約 30% が 12 か月以内に認識。OpenAI を除くと前年比 +25%(Hood、Motley Fool 系要約) | https://phemex.com/news/article/microsoft-q1-fy2027-revenue-hits-923b-as-azure-grows-48-yoy-101615 / https://fourweekmba.com/ai-microsoft-backlog-holds-at-677b-12-month-slice-is-203b/ |
| 備考 | リース会計: データセンター等の見積耐用年数を 15 年→25 年に延長し、ファイナンスリースからオペレーティングリースへ移る比率が増える(capex 表示に影響) | https://mezha.net/eng/?p=3215699 |

### 1-2 Alphabet(Q3、2026-10-28 または 29 発表。出典で日付が不一致)
| 項目 | 値 | 出典 |
|---|---|---|
| 売上 | $127.6B(+25%) | [集約] https://aiweekly.co/alerts/alphabet-posts-1276b-q3-with-google-cloud-up-103-to-307b-as-2027-capex-set-to |
| Google Cloud | 売上 $30.7B(+103%)、営業利益率 36.2%(前年 23.7%)。TPU システム販売が「成長への有意な寄与」(リリース記述。TPU 売上の個別開示なし) | https://fourweekmba.com/ai-google-cloud-revenue-doubles-to-30-7b-as-capex-hits-51-4b/ / https://www.gurufocus.com/news/9149651/alphabet-inc-goog-q3-2026-earnings-call-highlights-cloud-revenue-doubles-gemini-hits-1-billion-users-and-capex-surges-toward-205-billion |
| 受注残 | 不一致(軽微): $561B(CFO 発言として報道。約 55% を 24 か月で収益化)/ 10-Q 系: 総受注残 $567.7B、うち Cloud $560.8B(Blackstone との関連当事者 JV「Crux AI」向け $16.8B を含む)。Q2 は $514B | https://sec-api.io/insights/alphabet-googl-q3-2026-earnings-sec-filing-analysis (結果の要約) / https://www.gurufocus.com/news/9149651/... |
| capex | Q3 $51.4B、四半期 FCF -$9.1B。2026 年通期ガイド $195〜205B(Q1 の $180〜190B から引上げ済み。Q3 で据置とする要約と「$205B に向かう」とする見出しが併存) | https://fourweekmba.com/ai-google-cloud-revenue-doubles-to-30-7b-as-capex-hits-51-4b/ |
| 2027 capex | 会社発言: 「2027 年に capex は有意に増加する見込み。詳細は Q4 決算で」。「2027 年に $300B 超」は見出しの数字で、会社の発言としては確認できず(not found) | https://www.gurufocus.com/news/9149651/... / https://aiweekly.co/alerts/alphabet-posts-1276b-q3-with-google-cloud-up-103-to-307b-as-2027-capex-set-to |
| 容量の制約 | AI 需要は利用可能な計算容量を上回り続ける。第三者容量の利用が Q3 の利益率をわずかに圧迫(S&P Global の要約) | https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/07/alphabet-postq-ai-growth-accelerates-as-spending-weighs-on-cash-flow (※URL は 7 月付の記事。10 月分の要約と混在の可能性、日付は未確認) |
| 株価反応 | 約 -10% とする SNS 要約のみ。未確認 | 同上 aiweekly 記事の記述 |

### 1-3 Amazon(Q3、2026-10-29 発表)
| 項目 | 値 | 出典 |
|---|---|---|
| 売上 | $201.9B(+12%)。EPS $1.89 は予想を下回る。純利益 $20.7B | https://www.financialcontent.com/article/bizwire-2026-10-29-amazoncom-announces-third-quarter-results / https://www.geekwire.com/2026/aws-growth-hits-39-its-fastest-in-nearly-five-years-as-amazon-misses-on-earnings/ |
| AWS | 売上 $46.0B、+39%(+39.3% とする出典あり)。約 5 年ぶりの高い伸び。営業利益 $17.8B(前年 $11.4B)。Q2 は $42.2B、+36.7% | https://www.unite.ai/amazon-q3-operating-income-climbs-61-as-aws-sales-jump-39/ / https://www.tradingkey.com/news/transcripts/262256105-tradingkey |
| 受注残 | $578B(前四半期比 +$82B、前年比で 3 桁成長)。Q2 は $496B | https://www.gurufocus.com/news/9154009/amazoncom-inc-amzn-q3-2026-earnings-call-highlights-record-139-operating-margin-aws-surges-39-and-backlog-hits-578-billion |
| capex | Q3 $77.3B。2026 年通期は約 $220B。2027 年は「有意に(meaningfully)高くなる」(Jassy) | https://www.andnowuknow.com/shop-talk/amazon-announces-third-quarter-results-andy-jassy-shares/anuk-staff/107854(検索要約) / https://www.webpronews.com/aws-39-percent-growth-amazon-q3-2026-earnings-capex(見出しのみ) |
| 見通し | AWS の伸びは 2027・2028 年とも 40% 超(Jassy。単一の要約) | 同上 andnowuknow の要約 |
| 容量 | 「$220B を投じても需要を満たす容量はない」(Jassy、要約の引用)。顧客が数百 MW〜1 GW を数年先まで予約し、2027・2028・2029 年の一部まで見通しが立つ。10/23 のポッドキャストで 2027 年の AWS 容量は大半が予約済み、2028 年容量も「相当量」販売済みとの報道 | https://www.gurufocus.com/news/9154009/... / https://247wallst.com/investing/2026/10/24/amazons-aws-has-already-sold-a-good-chunk-of-2028-capacity/ |
| Trainium | Bedrock の利用の大半が Trainium 上。Trainium の AWS 外販売を「2027 年後半」に開始する方針。Q2 時点: チップ事業の年換算 $20B 超($25B 超とする要約あり=不一致)、Anthropic は最大 5 GW、OpenAI は約 2 GW の Trainium を契約(OpenAI は 2027 年に立ち上がり) | https://www.techtimes.com/articles/329735/20261030/amazon-commits-selling-trainium-chips-outside-aws-late-2027-target-set.htm / https://www.theregister.com/2026/04/29/amazon_chips_20b_business/ / https://vectorshift.ai/research/companies/amazon-com/earnings/2026-q2 |
| 株価反応 | 時間外で約 -7%(-8〜11% とする出典もあり=不一致) | https://finance.yahoo.com/markets/stocks/live/amazon-earnings-live-q3-earnings-miss-sends-stock-lower-203345870.html |

### 1-4 Meta(Q3、2026-10-21 発表)
| 項目 | 値 | 出典 |
|---|---|---|
| 売上 | $64.6B(+26%) | https://www.winzheng.com/en/article/meta-q3-2026-capex-exceeds-operating-cash-flow |
| capex | Q3 $34.9B(営業 CF $32.8B を上回る、FCF -$2.1B)。2026 年通期ガイド $135〜145B(従来 $130〜145B。下限引上げ) | https://www.sec.gov/Archives/edgar/data/0001326801/000162828026066700/meta-09302026xexhibit991.htm / https://letsdatascience.com/news/meta-narrows-2026-capital-spending-range-to-135-billion-145-46f12e07 |
| 2027 capex | 具体額は示さず(Li 氏「2027 年の capex は現時点で見通しを示さない。来年の予算・容量計画はまだ初期」)。「積極的な投資は 2027 年も続く」との要約あり。アナリスト予想(会社の数字ではない): コンセンサス約 $193B、BofA $205B | https://finance.yahoo.com/markets/article/one-line-from-metas-earnings-call-that-ensured-the-stock-will-likely-stay-dead-money-134542007.html / https://news.ifyouspent.com/en/news/meta-earnings-what-to-watch-october-2026 |
| 外部クラウドの利用 | 自社構築はリードタイムが長いため、第三者クラウド契約で補完(Li 氏。フォローアップコールの書き起こし、一部文字化けのため要確認)。計算資源の環境は逼迫が続く | https://s21.q4cdn.com/399680738/files/content_files/META-Q3-2026-Follow-Up-Call-Transcript.pdf |
| 外部契約の例 | CoreWeave と $21B(2032 年まで、2026-04)。Nebius と $27B・5 年(専用容量 $12B+オプション $15B と報じられ、確定額が $12B か $27B かは出典で不一致) | https://theenergymag.com/news/2026-04-09/coreweave-ai-meta-debt / https://www.theenergymag.com/news/market-news/nebius-signs-27-billion-ai-infrastructure-deal-with-meta |
| 契約・リース残 | 不一致: 解約不能契約約 $455B+未開始リース約 $356B / 解約不能契約 $349.31B / Reuters 引用で将来支出約 $825B | https://www.globaldatacenterhub.com/p/meta-q3-2026-earnings-capex-cash-equity-raise (検索要約) |

---

## 2. GPU の計算単価

### 2-1 Ornn(OCPI、出来高加重・取引ベース)[一次: data.ornn.com、検索結果に表示された値]
| 日付 | H100 SXM | H200 | B200 | 出典 |
|---|---|---|---|---|
| 10/4 | $2.59 | $5.57 | $7.71 | https://data.ornn.com/ |
| 10/19 | $2.98 | $6.35 | $8.41 | https://data.ornn.com/gpu-cloud-price-comparison |
| 10/23 | $3.17 | $5.74 | $9.58 | https://data.ornn.com/markets |
| 10/25 | $3.03(a16z 関連記事) | $6.30(同) | $9.70 | https://data.ornn.com/markets/b200 / https://xenospectrum.com/en/a16z-gpu-rental-premium-ornn-index/ |
| 10/29(最新) | $2.92 | $5.96 | $9.83 | https://data.ornn.com/ |

- 10 月中の変化(10/4→10/29): H100 +12.7%、H200 +7.0%、B200 +27.5%(上表の値から算出)。
- 9 月からの変化: 月次の 9 月末値は not found。ただし単一の集約記事に「OCPI-H100 は 10/1 に $2.92、30 日で +3.2%、9/7 までの 1 か月で +22%」とあり、10/4 の $2.59 と矛盾(不一致)。ページのキャッシュ時刻が異なる可能性。 https://explainx.ai/blog/nvidia-h100-gpu-rental-price-45-percent-since-december-silicon-data-chamath-claimed-vs-verified-2026
- 参考(春〜初夏): B200 は 3 月初 $2.31→$4.95(Tom Tunguz、Ornn 引用)、5/30 $6.11→6/21 $4.22(World Journal)。 https://tomtunguz.com/b200-gpu-pricing-spot-market-model-releases/ / https://www.worldjournal.com/wj/story/121208/9583823

### 2-2 Silicon Data(ネオクラウド系の指数)
| 日付 | H100 | H200 | B200 | B300 | 出典 |
|---|---|---|---|---|---|
| 9/29〜9/30 | $2.75(9/30) | not found | $5.88(9/29)・$5.78(9/30) | not found | https://www.silicondata.com/products/silicon-index/h100 / https://www.silicondata.com/products/silicon-index/b200 |
| 10/10 | $2.82 | $3.43 | $5.93 | $6.71 | https://intuitionlabs.ai/articles/nvidia-ai-gpu-pricing-guide (10/10 改訂、[集約]) |
| 10/24 | $2.88(旧基準 2025-12-09 の $2.00 比で約 +44%) | $3.48 | not found | not found | https://explainx.ai/blog/...(上記)[集約] |
| 10/28 | not found | not found | $6.47 | not found | https://www.silicondata.com/products/silicon-index/b200 (FAQ 記載) |

- 9/30 から 10 月下旬への変化(上表から算出): H100 $2.75→$2.88(+4.7%)、B200 $5.78→$6.47(+11.9%)。
- 不一致: 同ページに「現在 $2.53(H100)」「$5.45(B200)」「H200 $3.10」の日付なし表示あり。Ornn と Silicon Data は水準が大きく異なる(10/29 B200: Ornn $9.83 / Silicon Data 10/28 $6.47)。方法の違い(Ornn=取引の出来高加重、Silicon Data=ネオクラウド系)。
- 出典: Silicon Data 指数ページは [一次]、その他は [集約]。

### 2-3 その他の指数・価格
| 項目 | 値 | 出典 |
|---|---|---|
| オンデマンド標準価格の中央値(10/7、Uvik) | H100 SXM $4.20、H200 $5.70、B200 $8.19、B300 $9.50 | https://uvik.net/blog/gpu-price-index/ [集約] |
| 27〜12 社平均(9/13、Mercatus) | H100 $3.84、H200 $4.43、B200 $6.39 | https://www.mercatus-ai.com/blog/gpu-rental-prices [集約] |
| SemiAnalysis(9 月下旬、二次引用) | B200 $8.01/時、3 か月で +79%(月次ではない) | https://shattered.io/nvidia-b200-cloud-price-79-percent-surge-2026/ [集約] |
| H100 1 年契約(SemiAnalysis 指数) | $1.70(2025-10)→$2.35(2026-03)、約 +40%。2026-10 の値は not found。「2026-08〜09 までに立ち上がる容量は予約済み」(3 月時点) | https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity / https://www.itiger.com/news/1185188896 |
| 1 年契約の他の報道 | H100 1 年契約が 2〜3 月に月 +15〜20%(単一の要約、本文は慎重扱いと付記あり)。Nvidia CFO が「2026 年に H100 賃料 +20%、A100 +15%」と述べたとの報道(ミラーサイト経由、書き起こし未照合) | https://www.kavout.com/market-lens/why-are-nvidia-h100-gpu-rental-prices-surging-by-40 / https://finance.yahoo.com/sectors/technology/articles/nvidia-cfo-just-revealed-gpu-164322619.html |
| Hyperbolic の H100 SXM | $1.50(6 月)→$3.19(その後) | https://www.spheron.network/blog/gpu-price-increase-2026-hyperbolic-h100/ [集約] |
| 値上げ・値下げの報道 | 値上げ: 上記。H200 賃料が 1 月から約 +160% の報道(日付・基準は未確認)。Nebius の Blackwell 容量オークションが過去最高値を 15% 上回る価格で成立(Seoul Economic Daily 引用のブログ)。値下げ: 2025 年に H100 賃料が 2023〜24 年のピークから 60% 超低下(Introl)、2025 年の AWS の H100/H200/A100 インスタンス値下げ(最大 45%)。2026 年 10 月の値下げ報道は not found | https://cryptobriefing.com/nvidia-h200-rental-costs-rise-160-percent/ / https://introl.com/blog/gpu-cloud-price-collapse-h100-64-percent-drop-2025 |

---

## 3. ネオクラウド(10 月)

| 社 | 10 月の動き | 出典 |
|---|---|---|
| CoreWeave | 10/6 AdaniConneX と提携、インド・ナビムンバイで 240 MW。10/27 デンマークの容量が稼働、世界ネットワークバックボーン発表(フルループは 2027 年中頃目標)。10/28 株価は約 +7%(終値 $63.93 とする記事。日付が混在しており概算)。Q3 決算は 2026-11-10 17:00 ET(会社発表。別サイトは 11/16 と記載=不一致、会社発表を採用)。10 月の新規契約・資金調達の発表は not found | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Announces-Date-of-Third-Quarter-2026-Financial-Results-and-Conference-Call/default.aspx / https://www.coreweave.com/news/coreweave-enters-india-expanding-ai-cloud-platform-with-adaniconnex / https://www.coreweave.com/news/coreweave-expands-global-ai-cloud-platform-with-new-capacity-in-denmark-and-first-ai-network-backbone / https://fool.com/coverage/stock-market-today/2026/10/28/stock-market-today-oct-28-coreweave-surges-on-denmark-ai-capacity-going-live |
| CoreWeave(直近の財務) | Q2 時点の受注残 $104B(Investing.com の記載。$99.4B とする別記事あり=不一致)。総債務 $35B 超(Q2 末)。2026-08 に $2.6B の DDTL 5.5(SOFR+5.50%、満期 2031-09-01)を完了、Anthropic・Jane Street・Hudson River Trading 向けの容量と報道。2026-03 に $8.5B の DDTL 4.0(投資適格格付け)。OpenAI との契約総額約 $22.4B | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Closes-2-6-Billion-Loan-Facility-Expanding-Financing-Flexibility-for-AI-Infrastructure/default.aspx / https://theenergymag.com/news/2026-08-11/coreweave-ai-2-6-billion-wider-spread/ / https://investing.com/equities/coreweave-earnings |
| Nebius | 10/22 Citi と $3.5B の担保付きファシリティ(期間 364 日、Term SOFR+2.75%、上限 3.50%)。長期契約 $40B 超(投資適格顧客)。2026 年 capex は $20〜25B(Q2 決算で再確認と報じられ、見出しは「$25B」=不一致)。年末 ARR 目標 $7〜9B。Q3 決算日は not found(Q3 2025 は 11/11、2026 年 Q2 は 8/12)。Meta $27B・Microsoft 契約は上記の通り | https://cloudnews.tech/nebius-secures-3-5-billion-from-citi-for-data-centers-and-gpus/ / https://finder.techleap.nl/news/feed/nebius-hikes-2026-capex-guidance-to-25b-signs-27b-meta-deal / https://www.benzinga.com/quote/NBIS/earnings |
| Lambda | 10/6 WSJ/Reuters 報道: 上場前の最終ラウンドで最大 $4B を調達、評価額は調達前 $14.5B。確定ではない(交渉・計画段階)。Microsoft 向け GB300 の数万台規模契約(2025-11 拡大)。IPO の申請は not found | https://www.thestar.com.my/tech/tech-news/2026/10/07/nvidia-backed-lambda-targets-4-billion-raise-ahead-of-planned-ipo-wsj-reports / https://letsdatascience.com/news/lambda-pursues-4-billion-pre-ipo-funding-round-909f4022 |

---

## 4. 部材と電力

| 項目 | 事実 | 出典 |
|---|---|---|
| NVIDIA Rubin の出荷時期 | 会社の目標は 2026 年下期(秋に最初のクラウド顧客群という記述、10/26 のブログ=[集約])。Huang 氏は 7/15 に「量産中」「遅延せず」と発言(顧客納入日は示さず)。KeyBanc は放熱部品と SK hynix の HBM4 認定の遅れで「わずかな遅れ」の可能性を指摘(B300 の増出荷で相殺と予想)。量産の立ち上がりは 2026 年 Q4、拡大は 2027 年上期とする記述あり。10 月の確定した顧客納入日は not found | https://winbuzzer.com/2026/07/18/nvidia-ceo-says-vera-rubin-is-in-production-denies-delay-xcxwbn/ / https://www.digitalcitizen.life/nvidia-confirms-vera-rubin-launch-for-q3-as-blackwell-demand-keeps-climbing/ / https://kucoin.com/news/flash/nvidia-announces-vera-rubin-ai-platform-production-timeline-for-fall-2026 |
| HBM(SK hynix、10/28 決算) | DRAM・HBM は長期契約+交渉中分を合わせ「2029 年まで事実上完売」、供給不足は 2030 年まで続く見通し。Q4 に HBM4 の出荷量・売上が HBM3E を上回る見込み。Q3 売上 104.6 兆ウォン、営業利益 83.3 兆ウォン(営業利益率約 80%、監査前) | https://www.koreatimes.co.kr/business/companies/20261028/sk-hynix-logs-record-q3-operating-profit-of-628-bil (URL 名の数字と本文要約の数字が異なる=不一致、要確認) / https://stockhub.kr/en/insights/view_1793152574975_d6cb11f87d-20261028-000660-cy26q3-earnings-call / https://letsdatascience.com/news/sk-hynix-posts-record-q3-profit-and-100-trillion-won-payout-1458a688 |
| DRAM 契約価格(TrendForce) | 不一致: 2026 Q4 は前四半期比約 +20%(10/20 の要約)/ 汎用 +10〜15%、HBM 含む +15〜20%(9/30 の予測)。Q2 約 +80%、Q3 約 +40%。10/21 の週報は「ベンダーが Q4 の契約見積りで値上げ幅を拡大」。2027 年は HBM 価格が大幅上昇との予想(2026-06) | https://www.trendforce.com/research/download/RP261021BP / https://www.stockhub.kr/en/news/news_b7244c205001 / https://borecraft.com/2026/06/02/tight-dram-supply-gives-suppliers-greater-pricing-power-in-hbm-with-hbm-contract-prices-expected-to-surge-multiples-higher-in-2027-says-trendforce/ |
| ガスタービン(GE Vernova Q3、10/28) | ガス機器の受注残+スロット予約 116→122 GW(年末に 130 GW 以上の見通し)。四半期で新規契約 11 GW、スロット予約から受注への転換 13 GW、出荷 5 GW。確定受注 53→64 GW、スロット予約 63→58 GW。総受注残 $197B、電化機器受注残 $42.2B(前年比 +60%)。新規受注の納入は 2031 年(2026-08 の業界報道)、年間タービン生産能力を 2030 年までに 20→30 GW へ。Siemens Energy のタービン受注残 69 GW、三菱重工(大型)35 GW | https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000162/gevpressrelease3q26.htm / https://www.gevernova.com/news/ge-vernova-reports-strong-third-quarter-2026-financial-performance / https://www.euci.com/?p=190165 |
| 変圧器の納期 | Wood Mackenzie(2025 年 Q2): 電力用変圧器 128 週、発電機昇圧用(GSU)143〜144 週、配電用 30 週。2026 年値: GSU が 2026 Q1 に 160 週超(ブログ経由で Reuters 引用、未確認)。米国で最大 4 年とする見出し(pv magazine 2026-05)。10 月の新しい納期データは not found | https://powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/ / https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market/ / https://explainx.ai/blog/transformer-lead-times-160-weeks-ai-data-centers-grid-equipment-shortage-2026 |
| PJM | 市場監視機関: データセンター負荷増が容量市場の逼迫・高値の主因。2028/29 年度オークションは信頼性要件を 6.8 GW 下回り(結果の要約では総額 $16.4B のうちデータセンター寄与 38〜40%、出典で不一致)。供給確保のための一回限りの信頼性バックストップオークション(9/30〜10/21 の計画、最終状態は未確認)。データセンター等の大口負荷は 2038 年までに最大 +70 GW(PJM 推計) | https://www.power-eng.com/business/pjm-capacity-auction-hits-price-cap-again-as-region-falls-short-of-reliability-target/ / https://www.utilitydive.com/news/pjm-backstop-capacity-auction-ferc-data-centers/826792/ / https://btw.media/en/pjm-monitor-attributes-us-6-3bn-auction-charges-to-data-centres |
| ERCOT | 大口負荷の接続待ち約 474 GW(うち約 90% がデータセンター、2026-07 の議会証言。S&P の 10/8 記事は「500 GW に接近」)。8/3 に知事が PUCT・ERCOT へ、待ち行列のデータセンター全件の監査を指示(対象 250〜300 件の Batch Zero、報告期限 2026-12-10)。ERCOT は大規模計算負荷の通電承認を停止中と PUCT に伝達。不一致: SB6 のフィルター後は 243 GW(系統約 85 GW に対し)とする Substack 分析 | https://www.ercot.com/files/docs/2026/07/29/ERCOT-Senate-July-29-Panel-1-Assessing-The-Grid.pdf / https://www.spglobal.com/energy/en/technology-ai-research-insights/blogs/the-texas-data-center-boom / https://computeheatrate.substack.com/p/the-queue-survived-even-thrived-with |

---

## 5. AI 研究所の需要

| 社 | 事実(10 月分を優先。10 月でないものは日付を明記) | 出典 |
|---|---|---|
| Anthropic | 10/26 に S-1 を SEC へ提出と報道(原本は未取得)。報道ベースの契約額: Amazon・Google・Microsoft 向けの計は $265B(1 件)/ 少なくとも $269.4B(別出典)。内訳は不一致: Google $111.1B vs 少なくとも $114.5B、Amazon 少なくとも $110B、Microsoft $31.4B vs $44.9B。Broadcom リース約 $161.2B、SpaceX 向け最大 $120.5B(別報道 $84.5B)で、総額を $518B とする報道(9/29 付)。約 80% が解約不能との記述。Oracle 向け契約は検索結果に記載なし(not found)。売上ランレート: 2026 年 7 月末に $65B 超(2025 年末 $9B、5 月 $47B)。10 月は推定のみ(Sacra 約 $70B、SemiAnalysis 約 $74B)、FT は 10 月の投資家会合で更新なしと報道 | https://www.fxstreet.com/analysis/anthropic-pledged-270-billion-to-amazon-google-and-microsoft-heres-who-actually-gets-paid-202610271751 / https://ppc.land/amazon-google-and-microsoft-hold-269bn-of-anthropic-compute-contracts/ / https://fourweekmba.com/ai-anthropic-518b-prospectus-leak-google-amazon-80-percent-lock/ / https://www.businessday.co.za/world/international-companies/2026-09-29-anthropic-plans-518bn-ai-infrastructure-spend-80-non-cancellable/ / https://sec-api.io/insights/anthropic-ant-s-1-ipo-sec-filing-analysis / https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai |
| Anthropic(それ以前の契約) | 2026-04 Google・Broadcom と複数 GW の TPU(Broadcom 経由で約 3.5 GW、2027 年開始)。Colossus 1(SpaceX/xAI 系)の全容量(300 MW 超)を利用。CoreWeave(2026-08 の DDTL の用途と報道)。Azure $30B(2025 年後半) | https://www.anthropic.com/news/google-broadcom-partnership-compute / https://sacra.com/chat/h/31205144-57d0-41dc-b5dd-c54c1688cd88/ |
| OpenAI | 10 月の新規計算容量契約は not found。年換算売上: 9 月末に「50B ドルに近づく」(投資家向け説明の報道)、年末の投資家基準の目標 $70B(Bloomberg 10/9、1 件の要約)。計算コミットメント: Altman 氏 約 $1.4T(8 年)/ 一部報道は約 $600B で不一致。週間利用者: 2026-08 に 10 億人とする出典と、年末 10 億人の社内目標未達とする WSJ 要約が併存(不一致)。2026-04 WSJ: 売上・利用者の社内目標未達、CFO がデータセンター契約の履行を懸念。AMD 6 GW・Nvidia 10 GW・Broadcom 10 GW(2025 年発表、約 26 GW) | https://www.datacenterdynamics.com/en/news/openai-missed-revenue-and-user-targets-faces-internal-concern-over-meeting-data-center-spend-commitments-report/ / https://aimagazine.com/news/openais-billion-users-us852bn-valuation-and-stargate / https://www.trendforce.com/news/2025/10/15/news-openai-ramps-up-global-compute-power-with-nvidia-amd-and-broadcom-securing-26-gw-of-ai-infrastructure/ |
| OpenAI × Oracle | Abilene は 1.2 GW の計画。2026-03 に 600 MW の増設を取りやめと Bloomberg・Reuters が報道、Oracle は「スケジュール通り」「4.5 GW 契約は継続」と反論(不一致)。10 月時点の状況は not found。Stargate UK を 2026-04 に停止との記述(1 件) | https://www.tomshardware.com/tech-industry/oracle-and-openai-scrap-planned-600mw-abilene-expansion / https://tomshardware.com/tech-industry/oracle-rebuts-incorrect-reporting-on-stargate-expansion / https://intuitionlabs.ai/pdfs/openai-stargate-datacenter-details-389752b6aa7deb7a.pdf |
| xAI | 10 月の容量・資金調達は not found。2026-01 に Series E $20B。Colossus 2 は約 2 GW を目標(1 GW 超が稼働)。Colossus 1 の容量を Anthropic に貸出 | https://en.ain.ua/2026/01/07/xai-raises-20b-for-colossus-supercomputer/ / https://sacra.com/chat/h/31205144-57d0-41dc-b5dd-c54c1688cd88/ |
| Meta | 上記 1-4 の通り(CoreWeave $21B、Nebius $27B、第三者クラウドで補完) | 同上 |
| 推論トークン量 | Google: 月 3.2 京(quadrillion)トークン超(2026 年 I/O 時点、2025 年 480 兆、2024 年 9.7 兆)。10 月の決算での更新値は not found。Microsoft・Amazon・Meta の 10 月の公表値も not found | https://www.shacknews.com/article/149205/google-3-2-quadrillion-monthly-ai-tokens |

---

## 6. バブル・減速の懸念を示す材料と、その反証

### 6-1 懸念を示す材料(事実のみ)
| 材料 | 内容 | 出典 |
|---|---|---|
| OpenAI の社内目標未達 | 2026-04 WSJ: 売上・週間利用者の目標未達、CFO がデータセンター契約の履行を懸念。AI 関連株が下落し、Oracle・CoreWeave も下落(報道) | https://www.datacenterdynamics.com/en/news/openai-missed-revenue-and-user-targets-faces-internal-concern-over-meeting-data-center-spend-commitments-report/ / https://neuronfeed.com/news/openai-misses-revenue-and-user-targets-as-investors-dump-ai-stocks |
| FCF のマイナス | Alphabet Q3 FCF -$9.1B、Meta Q3 FCF -$2.1B(capex が営業 CF を上回る)。Meta は新株売却($37.5B とする見出し、本文未確認) | 上記 1-2、1-4 / https://www.globaldatacenterhub.com/p/meta-q3-2026-earnings-capex-cash-equity-raise |
| 決算後の株価 | Amazon 時間外 約 -7%(出典間で不一致)、Alphabet 約 -10%(SNS 要約)、Microsoft 約 +4%。Meta の反応は信頼できる日付確認ができず not found | 上記 |
| capex の未達(供給側) | Microsoft は第三者容量の納入遅れで capex が予想を下回った(需要減ではなく納入の遅れ、との報道) | https://www.cnbc.com/2026/10/28/microsoft-msft-q1-earnings-report-2027.html |
| 契約の取り消し・縮小 | Microsoft のデータセンター・リース解約・繰延べ(TD Cowen が「供給過剰」と解釈、記事日付は不明=2025 年の可能性)。Abilene 600 MW 増設の中止(2026-03、Oracle は反論)。2026 年に開業予定の米データセンターの約半数が中止・遅延との投稿(フォーラム経由、未確認)。中国で新設容量の最大 80% が未使用で GPU 賃料下落(Data Center Knowledge、日付未確認) | https://capacitymedia.com/article/microsoft-ditches-more-ai-data-centre-leases-as-spending-bubble-looms / https://www.datacenterknowledge.com:443/ai-data-centers/tumbling-prices-end-china-s-ai-data-center-binge |
| 契約集中・解約不能 | Anthropic の契約の約 80% が解約不能(報道)。Meta の解約不能契約は約 $349〜455B(不一致) | 上記 5、1-4 |
| 電力・許認可 | ERCOT の通電承認停止と監査(12/10 報告)。PJM の信頼性要件割れ | 上記 4 |
| 10 月の GPU 余剰の報道 | 2026 年 10 月の GPU 余剰・値下がりの報道は not found(検索で「Blackwell 賃料が下落」の 2026 年の信頼できる報道は見つからず) | https://cryptobriefing.com/nvidia-h100-gpu-rental-costs-surge/ ほか |

### 6-2 反証となる材料(同じ範囲の事実)
| 材料 | 内容 | 出典 |
|---|---|---|
| 受注残の積み上がり | Microsoft RPO $677B、Google Cloud $561B(Q2 $514B)、AWS $578B(Q2 $496B) | 上記 1 |
| 全社が供給制約と発言 | Microsoft(需要が供給超)、Alphabet(需要が容量超)、Amazon($220B でも不足)、Meta(計算環境は逼迫) | 上記 1 |
| 2027 年の capex の方向 | Alphabet「有意に増加」、Amazon「有意に高く」、Microsoft 暦年 2027 約 $170B(要約)、Meta は具体額なし(積極投資継続との要約) | 上記 1 |
| 賃料の上昇 | Ornn 10/4→10/29 で B200 +27.5%、Silicon Data 9/30→10 月下旬で B200 +11.9%、H100 1 年契約は 2025-10→2026-03 で約 +40% | 上記 2 |
| 部材・電力の逼迫 | SK hynix は 2029 年まで完売、GE Vernova のガス機器受注残は増加(122 GW)、ERCOT の接続待ち 474 GW | 上記 4 |
| 先行予約 | AWS は 2027 年容量の大半・2028 年容量の相当量を販売済み(Jassy 発言の報道) | https://247wallst.com/investing/2026/10/24/amazons-aws-has-already-sold-a-good-chunk-of-2028-capacity/ |
| AI 研究所の売上 | Anthropic の売上ランレート $65B 超(2026-07 末)。OpenAI 年換算売上は 50B ドルに近づく(9 月末) | 上記 5 |

---

## 未取得・要確認の一覧
- 一次資料(Microsoft・Alphabet・Amazon・Meta の 8-K/書き起こし、Ornn・Silicon Data の原データ、Anthropic S-1)での照合は未実施(WebFetch が対象ホストに到達不可)。
- Alphabet の発表日(10/28 か 10/29)、Microsoft の capex($39.4B か $45.2B)と暦年見通し($170B と $175B の対象年)、Ornn の 9 月末値、Silicon Data の H200 の日付、CoreWeave の Q2 受注残($104B か $99.4B)。
- not found: 2026-10 の H100 1 年契約単価、10 月の OpenAI・xAI の新規容量契約、10 月の推論トークン量(各社決算)、Nebius の Q3 決算日、変圧器の 10 月の納期データ、Rubin の確定納入日。
