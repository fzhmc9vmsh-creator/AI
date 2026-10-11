# ピア比較表 生データ（PEG計算の材料）

収集者: Haiku / 取得日: 2026-10-11
評価基準日: 2026-10-11（株価は 2026-10-09 終値を目標）

## 0. 収集条件と既知の制約

- 取得手段は WebSearch のみ（WebFetch・curl は未使用）。
- **WebSearch の利用上限（1ターン200回、エージェント間で共有）に到達したため、取得を途中で打ち切った。** 下表の「欠損」は未取得であり、推測値ではない。追加の検索は後続メッセージで再開できる。
- TradingView の直接取得は不可。`allowed_domains: ["tradingview.com"]` の検索は CHKP・TENB・S で試したが、個別の EPS・売上コンセンサス数値は出なかった。出た数値は古い Zacks 記事由来の FY+1 のみ。
- 「直近会計年度」は最新の完了済み会計年度。「次の3会計年度」は未完了の会計年度の先頭3年（12月期なら FY2026・FY2027・FY2028、1月期なら FY2027・FY2028・FY2029、GEN は FY2027・FY2028・FY2029）。
- 「直近12か月」（LTM）の SBC と売上成長率は、必要な8四半期を揃えられず全社で欠損。直近四半期の値は参考として括弧内に併記。
- 単独出典（要約サイト等）の数値は「単独」と明記。会社IR（プレスリリース・8-K）の数値は出典URLに IR 系を置いた。
- CHKP は規格どおり、ピアPEG（経路a）の参照用として表に含める。
- CYBR は Palo Alto Networks による買収済み（2026-02-11 完了）のため、規格どおり「買収済み・完了日」のみを記す。

## 1. 主表

| ティッカー | 決算期末月 | 株価（2026-10-09終値、または直近・日付） | 時価総額 | 希薄化後株数 | 直近会計年度の売上 | 直近会計年度の non-GAAP EPS | 次の3会計年度の non-GAAP EPS コンセンサス（FY+1, FY+2, FY+3） | 次の2会計年度の売上コンセンサス | 直近12か月のSBC | 直近12か月の売上成長率 | 出典URL |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CHKP | 12月 | 欠損（2026-10-09 未取得）。参考: 2026-10-01 終値 $130.73（単独） | 欠損 | 欠損。参考（算出・非開示）: 約109.9M（FY2025 非GAAP純利益 $1,307.2M ÷ EPS $11.89） | FY2025（2025-12期）$2,725M（+6%） | FY2025 **$11.89**（+30%。税制一時益 約$1.90/株を含む） | FY2026: 欠損（参考: Zacks の古いFY2026コンセンサス $10.44、単独）／FY2027: 欠損／FY2028: 欠損 | FY2026: 欠損（参考: Zacks 古いFY2026コンセンサス $2.89B、単独）／FY2027: 欠損 | 欠損（参考: 2026Q1 SBC $59.8M、前年同期 $41.2M。四半期値のみ） | 欠損（参考: 2026Q2 YoY +1%） | FY25: https://www.barchart.com/story/news/176082/check-point-software-reports-fourth-quarter-and-2025-full-year-results ／ 2026Q2: https://www.barchart.com/story/news/3546049/check-point-software-reports-2026-second-quarter-financial-results ／ 2026Q2 PR（IR）: https://www.checkpoint.com/press-releases/check-point-software-reports-2026-second-quarter-financial-results/ ／ コンセンサス（古い・単独）: https://www.tradingview.com/news/zacks:f84154b3a094b:0-check-point-software-q4-earnings-top-estimates-revenues-increase-y-y/ ／ SBC（6-K、Q1推定）: https://www.sec.gov/Archives/edgar/data/0001015922/000117891326002310/a2635159.htm ／ 株価（単独）: https://chartrow.com/quote/chkp/monthly-returns |
| S | 1月（FY2026 は 2026-01-31 期） | 欠損（2026-10-09 未取得）。参考: 2026-09-04 終値 $19.88（単独） | 欠損。参考: 2026-09-07 頃 約 $6.64B（単独） | 欠損。参考: FY27 非GAAP EPS 想定の希薄化株数 約352M（旧ガイダンス時点、出典要照合） | FY2026（1月期）$1,001.3M（+22%） | FY2026: 欠損（Q4 FY26 非GAAP EPS $0.07 は単独・未確定） | FY2027: 欠損（会社ガイダンス $0.30–0.32。コンセンサスではない）／FY2028: 欠損／FY2029: 欠損 | FY2027: 欠損（会社ガイダンス $1,202–1,207M）／FY2028: 欠損 | 欠損 | 欠損（参考: 2027Q2 YoY +21%） | FY26 8-K: https://www.sec.gov/Archives/edgar/data/1583708/000158370826000014/sentineloneq426exhibit991.htm ／ 2027Q2 PR: https://www.01net.it/sentinelone-announces-second-quarter-fiscal-year-2027-financial-results/ ／ 2027Q2 PR（IR PDF）: https://s28.q4cdn.com/399982429/files/doc_financials/2027/q2/SentinelOne-Q2-27-Earnings-Press-Release.pdf ／ 株価（単独）: https://www.alphaquery.com/stock/S/volatility-option-statistics/10-day/iv-mean ／ 時価総額（単独）: https://capital.com/en-int/markets/shares/sentinelone-inc-share-price/market-cap |
| TENB | 12月 | 欠損（2026-10-09 未取得）。参考: 2026-08-18 終値 $36.34（単独） | 欠損。参考: $4.00B（2026-08-18、Motley Fool。Morningstar は $4.19B、日付不明で不一致） | 欠損。参考: 約110.1M〜110.3M（日付不明、複数サイト） | FY2025 **$999.4M**（+11%） | FY2025 **$1.59**（前年 $1.29） | FY2026: $1.95（Zacks、81日前の記事、Q2決算前の可能性・単独）／FY2027: 欠損／FY2028: 欠損 | FY2026: 欠損（会社ガイダンス中値 約$1.08B。コンセンサスではない）／FY2027: 欠損 | 欠損 | 欠損（参考: 2026Q2 YoY +8.6%） | FY25 8-K: https://www.sec.gov/Archives/edgar/data/1660280/000166028026000004/q42025financialresults-ear.htm ／ 2026Q2 PR（IR）: https://investors.tenable.com/news-releases/news-release-details/tenable-announces-second-quarter-2026-financial-results ／ 2026Q2 8-K: https://www.sec.gov/Archives/edgar/data/0001660280/000166028026000032/q22026financialresults-ear.htm ／ コンセンサス（単独）: https://www.tradingview.com/news/zacks:044852928094b:0-is-tenb-stock-a-buy-now-or-fairly-valued-after-its-big-2026-rally/（要照合） ／ 株価・時価総額（単独）: https://www.fool.com/quote/nasdaq/tenable-holdings-inc/tenb/ |
| QLYS | 12月 | 欠損（2026-10-09 未取得） | 欠損 | 欠損 | FY2025 **$669.1M**（+10%。単独: Fintool 要約、会社PR原文未確認） | FY2025 **$7.07**（前年 $6.13。会社PR経由と記載、単独要約と併記） | FY2026: 欠損（参考: Fintool が伝える2026年2月時点ガイダンス $7.17–7.45、未確認）／FY2027: 欠損／FY2028: 欠損 | FY2026: 欠損（会社の上方修正ガイダンス $732.0–738.0M。コンセンサスではない）／FY2027: 欠損 | 欠損 | 欠損（参考: 2026Q2 YoY +11%） | FY25 PR: https://seekingalpha.com/pr/20390519 ／ 2026Q2 8-K: https://www.sec.gov/Archives/edgar/data/0001107843/000110784326000034/qlys-20260804xex991.htm ／ 単独要約: https://fintool.com/app/research/companies/QLYS |
| RBRK | 1月（FY2026 は 2026-01-31 期） | 欠損（2026-10-09 未取得） | 欠損 | 欠損 | FY2026（1月期）約 $1.32B（+48%。単独要約、未確認） | FY2026: 欠損（Q4 FY26 非GAAP EPS $0.04 は第三者サイト、通期 -$0.01 は GAAP/非GAAP 不明で未確定） | FY2027: 欠損（会社ガイダンス $0.47–0.53。コンセンサスではない）／FY2028: 欠損／FY2029: 欠損 | FY2027: 欠損（会社ガイダンス $1,685–1,693M）／FY2028: 欠損 | 欠損 | 欠損（参考: 2027Q2 YoY +38%） | FY26 Q4 8-K: https://www.sec.gov/Archives/edgar/data/1943896/000194389626000004/rubrikinc-991pressrelease1.htm ／ 2027Q2 PR（IR）: https://s203.q4cdn.com/667520861/files/content_files/Rubrik-Inc-99-1-Press-Release-7-31-2026-VFINAL.pdf ／ ガイダンス（単独）: https://www.webull.ca/news-detail/15476728333419520 |
| NTSK | 1月（FY2026 は 2026-01-31 期） | 欠損（2026-10-09 未取得） | 欠損 | 欠損 | FY2026（1月期）$709.0M（+32%） | FY2026: 欠損（Q4 FY26 非GAAP EPS $(0.04) のみ確認） | FY2027: 欠損（会社の通期非GAAP EPS 未取得）／FY2028: 欠損／FY2029: 欠損 | FY2027: 欠損（会社ガイダンス $888–892M）／FY2028: 欠損 | 欠損 | 欠損（参考: 2027Q2 YoY +29%） | FY26 PR: https://investors.netskope.com/news-releases/news-release-details/netskope-announces-strong-fourth-quarter-and-fiscal-year-2026 ／ FY26 8-K: https://www.sec.gov/Archives/edgar/data/2063196/000119312526102142/ck0002063196-ex99_1.htm ／ 2027Q2 PR（IR）: https://investors.netskope.com/news-releases/news-release-details/netskope-announces-strong-second-quarter-fiscal-2027-financial ／ 2027Q2 要約: https://pulse2.com/netskope-q2-fiscal-2027-revenue-rises-29-to-220-5-million-as-arr-reaches-899-million/ |
| VRNS | 12月 | 欠損（2026-10-09 未取得） | 欠損 | 欠損 | FY2025 **$623.5M**（+13%。FY2024 $551.0M） | FY2025: 欠損（Q4 2025 EPS $0.08 は基準不明のため不採用） | FY2026: 欠損／FY2027: 欠損／FY2028: 欠損 | FY2026: 欠損／FY2027: 欠損 | 欠損 | 欠損（参考: 2026Q2 YoY +18%） | FY25 PR: https://s203.q4cdn.com/582009126/files/doc_news/Varonis-Announces-Fourth-Quarter-2025-and-Full-Year-2025-Financial-Results-2026.pdf ／ 2026Q2 PR（IR）: https://s203.q4cdn.com/582009126/files/doc_news/Varonis-Announces-Second-Quarter-2026-Financial-Results-2026.pdf ／ 2026Q2 株価反応: https://www.barchart.com/story/news/3510772/varonis-systemss-nasdaqvrns-q2-cy2026-beats-on-revenue-but-stock-drops |
| RPD | 12月 | 欠損（2026-10-09 未取得） | 欠損 | 欠損 | FY2025 **$860M**（+2%） | FY2025 **$2.08**（単独: Fintool 要約、未確認） | FY2026: 欠損（会社ガイダンス $1.50–1.60。コンセンサスではない）／FY2027: 欠損／FY2028: 欠損 | FY2026: 欠損（会社ガイダンス $835–843M）／FY2027: 欠損 | 欠損 | 欠損（参考: 2026Q2 YoY -1.5%） | FY25 PR: https://s29.q4cdn.com/157304370/files/doc_news/Rapid7-Announces-Fourth-Quarter-and-Full-Year-2025-Financial-Results-2026.pdf ／ 2026Q2 8-K: https://www.sec.gov/Archives/edgar/data/0001560327/000156032726000043/q22026rapid78-kex991.htm ／ 2026Q2 EPS（単独）: https://247wallst.com/companies/rpd/earnings/2026/Q2 ／ FY25 要約（単独）: https://fintool.com/app/research/companies/RPD |
| SAIL | 1月（FY2026 は 2026-01-31 期） | 欠損（2026-10-09 未取得） | 欠損 | 欠損 | FY2026（1月期）**$1,071M**（+24%） | FY2026: 欠損（Q4 FY26 EPS $0.08 は基準不明） | FY2027: 欠損（会社ガイダンス $0.30–0.34、2026-09-09 に据え置き。コンセンサスではない）／FY2028: 欠損／FY2029: 欠損 | FY2027: 欠損（会社ガイダンス $1,260–1,270M）／FY2028: 欠損 | 欠損 | 欠損（参考: 2027Q2 YoY +17%） | FY26 8-K: https://www.sec.gov/Archives/edgar/data/2030781/000162828026019034/sailpointinc-20260131x991x.htm ／ 2027Q2 PR（IR経由）: https://finviz.com/news/390033/sailpoint-announces-fiscal-second-quarter-2027-results ／ 2027Q2 要約: https://quartr.com/events/sailpoint-inc-sail-q2-2027_F6IobL44 |
| CYBR | — | 買収済み・完了日 2026-02-11 | — | — | — | — | — | — | — | — | 10-Q（PANW、完了日記載）: https://www.sec.gov/Archives/edgar/data/1327567/000132756726000005/panw-20260131.htm ／ 完了報道: https://www.crnasia.com/news-network/2026/palo-alto-networks-completes-25b-acquisition-of-cyberark-for-identity-security-push |
| GEN | 3月末〜4月初（金曜日起算。FY2026 は 2026-04-03 終了） | 欠損（2026-10-09 未取得） | 欠損 | 欠損 | FY2026 **$5,000M**（+27%。買収寄与を含む。Q4 のプロフォーマ成長は +9%） | FY2026 **$2.56**（+15%） | FY2027: 欠損（会社ガイダンス $2.85–2.95。コンセンサスではない）／FY2028: 欠損／FY2029: 欠損 | FY2027: 欠損（会社ガイダンス $5,325–5,425M）／FY2028: 欠損 | 欠損 | 欠損（参考: FY26 +27%、Q4 プロフォーマ +9%） | FY26 8-K: https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000014/ex9901q4fy26.htm ／ FY26 PR（IR）: https://newsroom.gendigital.com/2026-05-07-Gen-Crosses-5B-in-FY26-Revenue-with-Growth-Accelerating-to-Double-Digits |
| AKAM | 12月 | 欠損（2026-10-09 未取得）。参考: 2026Q2 自社株買い平均単価 $134.54（終値ではない） | 欠損 | 欠損 | FY2025 **$4,208M**（+5%。FY2024 $3,991M） | FY2025 **$7.12**（+10%） | FY2026: 欠損／FY2027: 欠損／FY2028: 欠損 | FY2026: 欠損／FY2027: 欠損 | 欠損 | 欠損（参考: 2026Q2 YoY +5%。Q2 セキュリティ売上 $604M、+10%） | FY25 PR（IR）: https://www.ir.akamai.com/node/32741 ／ 2026Q2 PR（IR）: https://www.ir.akamai.com/node/33716 ／ 2026Q2 8-K: https://www.sec.gov/Archives/edgar/data/0001086222/000108622226000083/exhibit991-q22026.htm |

## 2. 直近四半期の実績（参考・確定済み）

| ティッカー | 直近四半期（期末） | 売上 | 売上 YoY | 非GAAP EPS | 出典 |
|---|---|---|---|---|---|
| CHKP | 2026Q2（2026-06-30） | $674M | +1% | $2.55（+8%） | https://www.barchart.com/story/news/3546049/check-point-software-reports-2026-second-quarter-financial-results |
| S | 2027Q2（2026-07-31） | $292M | +21% | $0.08（前年 $0.04） | https://www.01net.it/sentinelone-announces-second-quarter-fiscal-year-2027-financial-results/ |
| TENB | 2026Q2（2026-06-30） | $268.5M | +8.6% | $0.51（前年 $0.34） | https://investors.tenable.com/news-releases/news-release-details/tenable-announces-second-quarter-2026-financial-results |
| QLYS | 2026Q2（2026-06-30） | $182.2M | +11% | $1.98 | https://www.sec.gov/Archives/edgar/data/0001107843/000110784326000034/qlys-20260804xex991.htm |
| RBRK | 2027Q2（2026-07-31） | $427.3M | +38% | $0.20（前年 $(0.03)） | https://s203.q4cdn.com/667520861/files/content_files/Rubrik-Inc-99-1-Press-Release-7-31-2026-VFINAL.pdf |
| NTSK | 2027Q2（2026-07-31） | $220.5M | +29% | $(0.03)（前年 $(0.32)） | https://investors.netskope.com/news-releases/news-release-details/netskope-announces-strong-second-quarter-fiscal-2027-financial |
| VRNS | 2026Q2（2026-06-30） | $180.0M | +18% | $0.04（単独: Zacks） | https://s203.q4cdn.com/582009126/files/doc_news/Varonis-Announces-Second-Quarter-2026-Financial-Results-2026.pdf |
| RPD | 2026Q2（2026-06-30） | $210.9M | -1.5% | $0.44（単独: 247wallst、予想 $0.35） | https://www.sec.gov/Archives/edgar/data/0001560327/000156032726000043/q22026rapid78-kex991.htm |
| SAIL | 2027Q2（2026-07-31） | $308.8M | +17% | $0.09（単独要約。判定はガイダンス $0.07–0.08 比で上振れ） | https://finviz.com/news/390033/sailpoint-announces-fiscal-second-quarter-2027-results |
| GEN | FY2026Q4（2026-04-03） | $1,283M | +27%（プロフォーマ +9%） | $0.67（+14%） | https://www.sec.gov/Archives/edgar/data/0000849399/000084939926000014/ex9901q4fy26.htm |
| AKAM | 2026Q2（2026-06-30） | 約 $1.1B | +5% | $1.59（-8%） | https://www.ir.akamai.com/node/33716 |

## 3. 会社ガイダンス（参考。コンセンサスではない）

| ティッカー | 対象年度 | 売上ガイダンス | 非GAAP EPS ガイダンス | 出所日・出典 |
|---|---|---|---|---|
| CHKP | FY2026 | 欠損 | $10.05–10.85（経営陣レンジ、Zacks記事経由・単独） | https://www.tradingview.com/news/zacks:f84154b3a094b:0-check-point-software-q4-earnings-top-estimates-revenues-increase-y-y/ |
| CHKP | 2026Q3 | $665–685M | $2.43–2.53（単独要約） | https://www.webull.com/news/15364638754350080（要約、単独） |
| S | FY2027（1月期） | $1,202–1,207M | $0.30–0.32 | 2027Q2 PR、2026-08-27: https://www.01net.it/sentinelone-announces-second-quarter-fiscal-year-2027-financial-results/ |
| TENB | FY2026（12月期） | $1,075–1,081M | $1.95–2.00（上方修正後） | 2026Q2 PR、2026-07-29: https://investors.tenable.com/news-releases/news-release-details/tenable-announces-second-quarter-2026-financial-results |
| QLYS | FY2026（12月期） | $732.0–738.0M（上方修正） | 欠損（Feb 時点 $7.17–7.45 は単独・未確認） | 2026Q2 8-K、2026-08-04: https://www.sec.gov/Archives/edgar/data/0001107843/000110784326000034/qlys-20260804xex991.htm |
| RBRK | FY2027（1月期） | $1,685–1,693M（上方修正） | $0.47–0.53 | 2027Q2 PR（2026-08-27）／単独要約: https://www.webull.ca/news-detail/15476728333419520 |
| NTSK | FY2027（1月期） | $888–892M | 欠損 | 2027Q2 PR（2026-09-02）: https://investors.netskope.com/news-releases/news-release-details/netskope-announces-strong-second-quarter-fiscal-2027-financial |
| VRNS | FY2026（12月期） | 欠損（SaaS ARR $769–775M は売上ではない） | 欠損 | 2026Q2 PR: https://s203.q4cdn.com/582009126/files/doc_news/Varonis-Announces-Second-Quarter-2026-Financial-Results-2026.pdf |
| RPD | FY2026（12月期） | $835–843M | $1.50–1.60（2026-02 時点。Q2 更新は未確認） | FY25 PR（2026-02-10）: https://s29.q4cdn.com/157304370/files/doc_news/Rapid7-Announces-Fourth-Quarter-and-Full-Year-2025-Financial-Results-2026.pdf |
| SAIL | FY2027（1月期） | $1,260–1,270M | $0.30–0.34（2026-09-09 据え置き） | FY26 PR（2026-03-18）: https://www.sec.gov/Archives/edgar/data/2030781/000162828026019034/sailpointinc-20260131x991x.htm |
| GEN | FY2027（3月末〜4月初期） | $5,325–5,425M | $2.85–2.95（Q1 FY27: 売上 $1,300–1,325M、EPS $0.68–0.70） | FY26 PR（2026-05-07）: https://newsroom.gendigital.com/2026-05-07-Gen-Crosses-5B-in-FY26-Revenue-with-Growth-Accelerating-to-Double-Digits |
| AKAM | FY2026（12月期） | 欠損 | 欠損 | 未取得 |
| CYBR | — | — | — | 買収済みのため対象外 |

## 4. 出典が食い違った数値

1. **TENB 時価総額・株価**: Motley Fool は $36.34・時価総額 $4.00B（2026-08-18）。Morningstar は $36.70・$4.19B（日付不明）。Public.com は時価総額 $2.02B（2026-04-02）。日付がずれており未確定。
2. **S 2027Q2 の非GAAP EPS の判定**: 会社発表は $0.08。コンセンサスは $0.07（Zacks/Earnings Whispers）で、同じ記事で beat と miss が混在。数値は会社発表の $0.08 を採用。判定は未確定。
3. **S FY2026 売上**: Seeking Alpha は「コンセンサスをわずかに下回る」、別の要約は「コンセンサスと一致」と報じる。会社値 $1,001.3M は両者とも一致。
4. **CHKP 2025Q4 売上**: Zacks は beat、Seeking Alpha は $744.90M で $1.52M の未達。会社値は約 $745M。判定は未確定。
5. **RBRK FY2026 非GAAP EPS**: 第三者サイトは通期 -$0.01（GAAP/非GAAP の別が不明）、Q4 は $0.04（未確認）。未確定。
6. **NTSK 2027Q2 コンセンサス損失**: $(0.07)（Barchart 系）と $(0.26)（別プレビュー）。基準が違う可能性がある。会社値 $(0.03) を採用。
7. **CHKP 株価（参考）**: chartrow は 2026-10-01 終値 $130.73。equibles は $130.32（日付不明）。単独・未確認。
8. **QLYS FY2025 EPS 伸び率**: 会社PRの非GAAP純利益は +13%、EPS は +15%（$7.07 vs $6.13）。純利益と EPS の違いで、矛盾ではない。

## 5. 欠損の集計

- **株価（2026-10-09 終値）**: 全12社で欠損。
- **時価総額・希薄化後株数**: 全12社で欠損（CHKP の株数は算出値のみ）。
- **直近12か月の SBC**: 全12社で欠損。
- **直近12か月の売上成長率**: 全12社で欠損（直近四半期 YoY で代替参考）。
- **次の3会計年度の EPS コンセンサス・次の2会計年度の売上コンセンサス**: 全12社で欠損（CHKP・TENB の FY2026 のみ古い単独出典あり）。
- **直近会計年度の non-GAAP EPS**: 欠損は 5 社（S・RBRK・NTSK・VRNS・SAIL）。CHKP・TENB・QLYS・GEN・AKAM は取得済み、RPD は単独出典。
