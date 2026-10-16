# ORCL データ収集 (H2): 市場データ・コンセンサス・ピア・株価推移

取得日: 2026-10-11 / 対象: Oracle (NYSE: ORCL), 決算期末 5月31日 / 最新報告済み: Q1 FY2027 (2026-09-10発表)

## 収集の注意 (先に読むこと)

- **WebSearch の上限に到達し、途中で検索を打ち切った。** 取得できたのは約28件分。ピア(表C)の大半と、表D の月末終値はほぼ未取得。
- WebFetch は tradingview.com / stockanalysis.com / marketbeat.com で DNS 失敗 (ENOTFOUND)。TradingView の NYSE-ORCL 予想ページは直接取得できず、検索結果からも拾えなかった。
- 検索の要約文は出典間で日付・値が食い違うものが多い。本表では **値の出典と掲載日を行ごとに併記** し、不一致は備考に残した。
- 「要確認」は単一出典または原文未確認の値。「欠損」は未取得または出典間で確定できなかった値。推測で埋めた値はない。
- 自己計算した値は「(自己計算)」と明記した。

---

## 表A: ORCL の市場データ

| 項目 | 値 | 基準日 | 出典 (URL) | 備考 |
|---|---|---|---|---|
| 株価 (終値) | 141.40 USD | 2026-10-09 | MarketBeat 速報 https://marketbeat.com/instant-alerts/price-oracle-nyse-orcl-shares-up-43-whats-next-2026-10-09 (検索要約経由) | **要確認**: 単一出典。原文を別検索で再確認できず。前日10/8は約5.5%下落 (TipRanks https://www.tipranks.com/news/why-oracle-stock-orcl-is-sinking-today-october-8-2026) |
| 10/10 日中レンジ | 136.50 - 142.90 USD | 2026-10-10 | 検索要約 (URL特定不可) | 終値ではない |
| 52週高値 | 欠損 | - | - | 検索で得た 345.72 は 2025-09-10 付近の高値。2026-10-09 時点の52週窓 (2025-10-09以降) からは外れるとみられる。窓内の正確な値は未取得 |
| 52週安値 | 114.50 USD (日付不明) | 2026-08下旬の表示 | Syfe https://www.syfe.com/stocks/us/ORCL | 別出典: 114.54 (Upstox, 2026-08 https://upstox.com/us-stocks/orcl-share-price/)、123.66 (2026-07-15, 単一要約)。出典間で不一致 |
| 2025年9月以降の最高値 | 日中 345.72 (表示値) / 終値最高 328.33 または 324.63 | 2025-09-10 付近 | 日中: Robinhood/Syfe の52週高値表示 (https://www.robinhood.com/stocks/ORCL) / 終値: ts2.tech https://ts2.tech/nl/oracles-ai-cloudbom-van-300-miljard-dollar-laat-orcl-aandeel-stijgen-wat-nu/ (Macrotrends引用), Capital.com https://capital.com/en-eu/analysis/oracle-orcl-stock-forecast | 終値は出典間で不一致 (328.33 vs 324.63) |
| 時価総額 | 421.9B USD (株価150.66時点) | 2026-08下旬 | Syfe https://www.syfe.com/stocks/us/ORCL | 2026-10-09 時点は欠損 (株数未確定)。参考: 409.26B (146.74時点, Upstox 2026-08)、381.76B (133.07時点, Robinhood 2026-07-15)、410.32B (Yahoo Current列) |
| 発行済株式数 (基本) | 欠損 | - | 参考のみ: Kuvera https://kuvera.in/us-stocks/oracle-corp-orcl (2.87B)、Angel One https://angelone.in/us-stocks/oracle-corp (2.76B) | 両方とも古いページ。Q1 FY27 に ATM で $20B の普通株を売却 (Oracle 発表, 2026-09-10) したため現在値はこれより多い可能性。10-Q 未取得 |
| 希薄化後株式数 | 欠損 | - | 参考: AlphaQuery FY2026 通期 diluted 加重平均 2.91B https://www.alphaquery.com/stock/ORCL/fundamentals/annual/weighted-average-shares-outstanding-diluted | Q1 FY27 の diluted 株数は未取得 (SEC EDGAR CIK 1341439 の 10-Q で要確認)。Q1 純利益 4.68bn ÷ EPS 1.56 ≈ 3.0B (自己計算, 参考) |
| 配当 (年額) | 2.00 USD ($0.50 x 4) | 2026-03 発表 | MarketBeat https://www.marketbeat.com/instant-alerts/oracle-corporation-nyseorcl-announces-quarterly-dividend-of-050-2026-03-11/、直近の落ち日 2026-07-10 (HL https://www.hl.co.uk/shares/shares-search-results/o/oracle-corp-comm-stock-us$0.01/dividends) | 10月分: 検索要約に「record 2026-10-09 / pay 2026-10-23」とあるが**要確認** (単一出典)。therighttrader は未宣言と表示 (古い) |
| 配当利回り | 1.2% (2026-03, 株価162.05時点) / 1.21% / 1.36% (trailing 12M) / 1.54% (2026-08) | 各掲載日 | MarketBeat (上記) / fullratio https://fullratio.com/stocks/nyse-orcl/dividend / HL (上記) / Walnut https://walnutinvest.com/stocks/orcl/dividend | 出典ごとに株価時点が異なる。自己計算: 2.00 / 141.40 = 1.41% (2026-10-09 時点, 参考) |
| 予想PER (今期・来期) | 今期・来期の区別は欠損。Forward P/E 17.64 (列の対応は推定) | 2026-08下旬 | Yahoo key-statistics https://finance.yahoo.com/quote/ORCL/key-statistics/ | Yahoo UK 18.25 (2026-07頃 https://uk.finance.yahoo.com/quote/ORCL)。Yahoo 表の列ラベルが要約から特定できず、Current列と推定 |
| 実績PER | 24.43 (trailing, Current列と推定) | 2026-08下旬 | Yahoo key-statistics (同上) | 列対応は要確認 |
| EV (企業価値) | 539.57B USD | 2026-08下旬 | Yahoo key-statistics (同上) | Yahoo UK 539.93B (2026-07頃) |
| 純有利子負債 | 97.6B USD | 最新決算年度末 (FY2026, 2026-05-31) | MarketScreener valuation (URL特定不可。検索結果の uk.marketscreener.com 系ページ) | 定義不明 (リース負債の扱い不明)。EV - 時価総額 (Yahoo) ≈ 129B (自己計算) と乖離。**要確認** |
| ベータ | 1.72 (5年月次, Yahoo US) / 1.60 (Yahoo UK) | 取得日不明 | https://finance.yahoo.com/quote/orcl/ / https://uk.finance.yahoo.com/quote/ORCL | 出典間で不一致 |
| 空売り比率 (% of float) | 2.7% (最新) | 2026-09下旬 | Benzinga sentiment https://www.benzinga.com/quote/ORCL/sentiment | 上昇傾向と表示。参考: 1.7% (50.1M株, 1.4日カバー, 2026-08-19, Equibles https://equibles.com/stocks/ORCL)。2026-03-31 は 27.67M株 (Equibles https://equibles.com/stocks/orcl/shortinterest)。MarketBeat 1.42% は 2025-09-15 時点で stale |
| アナリスト平均目標株価 (最新) | 237.97 (平均) / 400 (最高) / 110 (最低) / 41名 | 2026-09-19 (検証済み表示) | Bullstory https://bullstory.io/en/stocks/orcl/forecast/price-target | 最も新しい完全な組。評価は Buy |
| 同 (別出典) | 252 (平均) / 欠損 / 欠損 / 28名 | 2026-09-18 (株価147.61時点) | Benzinga https://kr.benzinga.com/quote/ORCL/price-targets | 同日に Freedom Broker が目標を205に引き下げ (2026-09-14)、Argus は225を維持 (同出典) |
| 同 (別出典) | 265.03 (平均) / 400 (最高) / 145 (最低) / 39名 | 掲載日不明 (2026-07下旬の可能性, 要確認) | MarketBeat https://www.marketbeat.com/stocks/NASDAQ/ORCL/forecast/ | 株価 116.43 表示。古い可能性 |
| 同 (別出典) | 237.97 (平均) / 欠損 / 欠損 / 43名 | 掲載日不明 | MarketScreener https://in.marketscreener.com/quote/stock/ORACLE-CORPORATION-120970792/consensus/ | 最終終値 137.79 と表示 (要約) |
| 同 (参考・古い) | 178.48 (平均) / 246 (最高) / 欠損 / 35名 | 2026年春と推定 (要確認) | Barchart 記事 (URL特定不可) | 21 Strong Buy / 14 Hold と表示 |
| 個別目標 | Mizuho 320 / Freedom Broker 205 / Argus 225 | Mizuho: 2026-09-08 報道 / FB, Argus: 2026-09-14 | Mizuho https://pulse.byoviral.com/trend/2026-09-08/mizuho-sees-oracle-at-320-as-ai-cloud-capacity-jumps 、 Benzinga (上記) | Mizuho は 2026-10 のトップ銘柄に選定との検索要約あり (要確認) |
| レーティング分布 (最新) | Strong Buy 1 / Buy 24 / Hold 3 / Sell 0 (計28名) | 2026-09-18 | Benzinga (上記) | |
| レーティング分布 (別) | Strong Buy 2 / Buy 28 / Hold 8 / Sell 1 (計39名, 総合 Moderate Buy) | 掲載日不明 | MarketBeat (上記) | |
| レーティング分布 (別) | Buy (内訳欠損) | 2026-09-19 | Bullstory (上記) | 41名 |

### 表A 欠損一覧
- 52週高値 (2026-10-09 時点の窓内の値)
- 52週安値の 2026-10-09 時点の窓内の値 (出典間で 114.50 / 114.54 / 123.66 が不一致)
- 2026-10-09 時点の時価総額、発行済株式数 (基本)、希薄化後株式数 (Q1 FY27)
- 今期・来期別の予想PER
- 平均目標の最高・最低 (Benzinga 2026-09-18、MarketScreener)
- 空売り比率 (2026-10 時点の値)

### 表A 出典一覧 (取得日 2026-10-11)
- Oracle Q1 FY27 発表 (2026-09-10): https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/ (掲載 2026-09-10)
- MarketBeat 速報 (2026-10-09): https://marketbeat.com/instant-alerts/price-oracle-nyse-orcl-shares-up-43-whats-next-2026-10-09
- TipRanks (2026-10-08): https://www.tipranks.com/news/why-oracle-stock-orcl-is-sinking-today-october-8-2026
- Bullstory (検証 2026-09-19): https://bullstory.io/en/stocks/orcl/forecast/price-target
- Benzinga (2026-09-18): https://kr.benzinga.com/quote/ORCL/price-targets / https://www.benzinga.com/quote/ORCL/sentiment
- MarketBeat (掲載日不明): https://www.marketbeat.com/stocks/NASDAQ/ORCL/forecast/
- MarketScreener (掲載日不明): https://in.marketscreener.com/quote/stock/ORACLE-CORPORATION-120970792/consensus/
- Syfe (2026-08下旬): https://www.syfe.com/stocks/us/ORCL
- Upstox (2026-08): https://upstox.com/us-stocks/orcl-share-price/
- Robinhood (表示 2026-07-15): https://www.robinhood.com/stocks/ORCL
- Yahoo Finance (2026-08下旬 / 2026-07頃): https://finance.yahoo.com/quote/ORCL/key-statistics/ , https://uk.finance.yahoo.com/quote/ORCL
- Equibles (2026-08-19 / 2026-03-31 データ): https://equibles.com/stocks/ORCL , https://equibles.com/stocks/orcl/shortinterest
- 配当: MarketBeat (2026-03-11) https://www.marketbeat.com/instant-alerts/oracle-corporation-nyseorcl-announces-quarterly-dividend-of-050-2026-03-11/ 、HL (取得時点) 、fullratio、Walnut (2026-08)
- Mizuho 報道 (2026-09-08): https://pulse.byoviral.com/trend/2026-09-08/mizuho-sees-oracle-at-320-as-ai-cloud-capacity-jumps

---

## 表B: ORCL のコンセンサス予想

| 年度 | EPS 平均 | EPS 最高 | EPS 最低 | アナリスト数 | EPSの定義 | 売上 平均 | 売上 最高 | 売上 最低 | 出典 (URL) | 掲載日 / 取得日 | 備考 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2027 | 7.98 | 8.32 | 7.33 | 23 | 不明 | 欠損 | 欠損 | 欠損 | Tickflow https://www.tickflow.io/stock/ORCL/forecast | 掲載日不明 / 2026-10-11 | FY28 と同ページ |
| FY2027 | 6.47 | 欠損 | 欠損 | 欠損 | 不明 (会社ガイダンス 8.10 と乖離 → GAAP 系の可能性, 未確認) | 欠損 | 欠損 | 欠損 | Barchart 決算プレビュー https://www.barchart.com/story/news/3478052/earnings-preview-what-to-expect-from-oracles-report | 2026-09 (Q1決算前) / 2026-10-11 | 平均 6.47 は Q1 決算前 |
| FY2027 | 6.34 (直前 6.40) | 欠損 | 欠損 | 40 | 不明 | 89.2B (決算前の数値) | 欠損 | 欠損 | Webull https://www.webull.ca/news-detail/15123152986760192 | 2026-06頃 (要確認) / 2026-10-11 | FY26 決算後の数値。EPS 修正 6.40 → 6.34 |
| FY2027 | 欠損 | 欠損 | 欠損 | 欠損 | - | 約90.5B | 欠損 | 欠損 | Yahoo Finance analysis https://finance.yahoo.com/quote/ORCL-PD/analysis/ | 2026-09-30 スナップショット / 2026-10-11 | EPS 欠損 |
| FY2027 | 7.75 (Q1 前の値, 出典1件) | 欠損 | 欠損 | 欠損 | 不明 | 89.5B (同上) | 欠損 | 欠損 | Oracle ガイダンス記事 https://www.thecerbatgem.com/?p=10386305 | 2026-09 / 2026-10-11 | **低品質ソース**。Q1 前の consensus と記載 |
| FY2027 | 6.39 | 欠損 | 欠損 | 欠損 | 不明 | 欠損 | 欠損 | 欠損 | 出典URL特定不可 (2026-08 表示の第三者サイト) | 2026-08 / 2026-10-11 | **低信頼**。参考 |
| FY2027 (非コンセンサス) | 7.60 | 欠損 | 欠損 | 欠損 | 独自モデル (diluted) | 欠損 | 欠損 | 欠損 | vcpscanner https://www.vcpscanner.com/valuation/orcl/estimates | 2026-10-11 | 出典自身が「コンセンサスを下回る」と表示 |
| FY2028 | 10.78 | 14.05 | 7.36 | 16 | 不明 | 欠損 | 欠損 | 欠損 | Tickflow (同上) | 掲載日不明 / 2026-10-11 | レンジが非常に広い |
| FY2028 | 8.78 | 欠損 | 欠損 | 欠損 | 不明 (FY27 比 +35.7%) | 欠損 | 欠損 | 欠損 | Barchart (同上) | 2026-09 / 2026-10-11 | Q1 決算前 |
| FY2028 (非コンセンサス) | 9.42 | 欠損 | 欠損 | 欠損 | 独自モデル | 欠損 | 欠損 | 欠損 | vcpscanner (同上) | 2026-10-11 | |
| FY2028 | 8.67 | 欠損 | 欠損 | 欠損 | 不明 | 欠損 | 欠損 | 欠損 | 出典URL特定不可 | 2026-08 / 2026-10-11 | **低信頼** |
| FY2028 | 欠損 | 欠損 | 欠損 | 欠損 | - | 約131.5B | 欠損 | 欠損 | Yahoo Finance analysis (同上) | 2026-09-30 / 2026-10-11 | 売上のみ |
| FY2029 | 欠損 | 欠損 | 欠損 | 欠損 | - | 欠損 | 欠損 | 欠損 | - | - | 未取得 |
| FY2030 | 欠損 | 欠損 | 欠損 | 欠損 | - | 欠損 | 欠損 | 欠損 | - | - | 未取得 |
| FY2031 | 欠損 | 欠損 | 欠損 | 欠損 | - | 欠損 | 欠損 | 欠損 | - | - | 未取得 |
| Q2 FY2027 (会社ガイダンス, コンセンサスではない) | 欠損 | 欠損 | 欠損 | 欠損 | non-GAAP | 欠損 | 欠損 | 欠損 | Oracle Q1 発表 https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/ | 2026-09-10 / 2026-10-11 | non-GAAP EPS **1.85 - 1.93** (USD)、売上成長率 30% - 34%、売上 20.9B - 21.5B (要約) |
| Q2 FY2027 (Q1 前のコンセンサス, 出典1件) | 1.82 | 欠損 | 欠損 | 欠損 | 不明 | 21.2B | 欠損 | 欠損 | https://www.thecerbatgem.com/?p=10386305 | 2026-09 / 2026-10-11 | **低品質**。Q1 後の更新値は未取得 |
| FY2027 ガイダンス (会社, コンセンサスではない) | 8.10 (非 GAAP) | - | - | - | non-GAAP | 90.0B 以上 | - | - | Oracle Q1 発表 (同上) | 2026-09-10 | **8.05 とする記事もあり (edgar.tools https://app.edgar.tools/news/topic/guidance_change)。要確認** |

### 表B 補足
- **Q1 FY27 実績 (参考):** 売上 約19.3B (+30%) / non-GAAP EPS 1.92 (+30%) / GAAP EPS 1.56 (+55%) / 非GAAP営業利益 8.2B / RPO 664B (+209B) / FCF -5B。出典: Oracle 発表 https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx 。決算前の売上コンセンサスは 19.13B (Yahoo 表, https://finance.yahoo.com/quote/ORCL-PD/analysis/)。Q1 の non-GAAP EPS 決算前コンセンサスは未取得。
- **直近3か月のコンセンサス EPS 修正方向:** 数値で確定できず。Webull の 6.40 → 6.34 は FY26 決算後の変化 (3か月窓ではない)。Barchart 6.47 (2026-09) との比較は定義・日付が揃わないため不採用。
- **EPS 定義の注意:** FY26 の実績 EPS が出典により 5.83 と 6.31 に分かれている (GAAP / non-GAAP の違いと推定, 未確認)。FY27 のコンセンサス 6.3 - 6.5 台 (Barchart, Webull) と会社の non-GAAP ガイダンス 8.10 は乖離しており、同一定義での比較はできない。
- **未採用の出典:** TradingView (ar. 地域版 NYSE-ORCL) は EPS 実績 2.11 vs 予想 1.96、次期 1.74 と表示するが、決算日を 2026-09-10 としており更新が止まっているため不採用 (https://ar.tradingview.com/symbols/NYSE-ORCL/forecast-price-target/)。TradingView (BOATS-ORCL, 時間外取引ライン) は平均目標 337.42 / 高 400 / 低 175.14 / 34名 だが取得時点不明で、株価と整合しないため不採用 (https://www.tradingview.com/symbols/BOATS-ORCL/forecast 相当の検索結果)。

### 表B 欠損一覧
- FY2029 - FY2031 の全項目
- FY2028 の EPS 平均・最高・最低 (Barchart, Tickflow 以外からの値なし)
- 各年度の売上 最高・最低
- 各年度のアナリスト数 (Barchart, Tickflow 以外)
- Q2 FY2027 のコンセンサス (Q1 後の更新値)
- 直近3か月の EPS 修正方向 (確定値)

### 表B 出典一覧 (取得日 2026-10-11)
- Tickflow: https://www.tickflow.io/stock/ORCL/forecast (掲載日不明)
- Barchart 決算プレビュー: https://www.barchart.com/story/news/3478052/earnings-preview-what-to-expect-from-oracles-report (2026-09)
- Webull: https://www.webull.ca/news-detail/15123152986760192 (2026-06頃, 要確認)
- Yahoo Finance: https://finance.yahoo.com/quote/ORCL-PD/analysis/ (2026-09-30 スナップショット)
- vcpscanner: https://www.vcpscanner.com/valuation/orcl/estimates
- Oracle Q1 FY27 発表: https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/ (2026-09-10)
- Oracle 投資家向け: https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx
- ガイダンス記事 (低品質): https://www.thecerbatgem.com/?p=10386305 、 https://app.edgar.tools/news/topic/guidance_change
- Seeking Alpha 成長率 (2026-01 スナップショット, 水準なし): https://seekingalpha.com/symbol/ORCL/valuation/price-earnings-peg-ratios

---

## 表C: ピア比較 (Microsoft, Amazon, Alphabet, Meta, CoreWeave, Nebius, SAP, ServiceNow, Salesforce, IBM)

注記: MSFT 以外はすべて未取得 (WebSearch 上限到達)。SAP / NOW / CRM / IBM は検索未実施。PEG と LTG は出典が示す値のみ。

| ティッカー | 株価 (日付) | 時価総額 | 予想PER (今期・来期) | コンセンサスEPS (今期・来期・2年後) | 3-5年EPS成長率 (LTG) | PEG | 出典URL | 備考 |
|---|---|---|---|---|---|---|---|---|
| MSFT | 499.70 USD (2026-09-04 終値) | 欠損 | 欠損 | 今期 (FY27, 6月期): 19.64 (平均, 単一の要約, 機関名不明) / 個別: Scotiabank 19.05 (2026-07-30) / Erste 19.46 (2026-07-30) / 来期 (FY28): 欠損 / 2年後: 欠損 | 欠損 | 欠損 | Benzinga https://www.benzinga.com/quote/MSFT/earnings-forecasts 、MarketBeat https://www.marketbeat.com/instant-alerts/fy2027-earnings-estimate-for-microsoft-issued-by-scotiabank-2026-07-30/ 、https://www.marketbeat.com/instant-alerts/microsoft-fy2027-eps-forecast-increased-by-erste-group-bank-2026-07-30/ 、https://www.webull.com/news/15327609602122752 (19.64 の出典、要確認) | 株価は出典間で不一致 (2026-07-30 MarketBeat 記事の 390.54 "opened at"、2026-08-14 Benzinga 495.40)。FY28 参考: 23.00 - 23.25 (出典不明, https://futuresearch.ai/app/p/a/msft-2027-08-04)。独自モデル 19.59 / 21.65 (vcpscanner https://vcpscanner.com/valuation/msft/estimates, 非コンセンサス) |
| AMZN | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | - | 未取得 (上限到達) |
| GOOGL | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | - | 未取得 (上限到達) |
| META | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | - | 未取得 (上限到達) |
| CRWV | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | - | 未取得 (上限到達) |
| NBIS | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | - | 未取得 (上限到達) |
| SAP | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | - | 未検索 |
| NOW | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | - | 未検索 |
| CRM | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | - | 未検索 |
| IBM | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | - | 未検索 |

### 表C 欠損一覧
- MSFT: 時価総額、予想PER (今期・来期)、来期 (FY28) と 2年後のコンセンサス EPS、LTG、PEG
- AMZN, GOOGL, META, CRWV, NBIS: 全項目
- SAP, NOW, CRM, IBM: 全項目 (未検索)

### 表C 出典一覧 (取得日 2026-10-11)
- Benzinga MSFT earnings forecasts: https://www.benzinga.com/quote/MSFT/earnings-forecasts
- MarketBeat (2026-07-20 / 07-30): https://www.marketbeat.com/instant-alerts/fy2027-eps-estimates-for-microsoft-cut-by-erste-group-bank-2026-07-20/ 、 https://www.marketbeat.com/instant-alerts/fy2027-earnings-estimate-for-microsoft-issued-by-scotiabank-2026-07-30/ 、 https://www.marketbeat.com/instant-alerts/microsoft-fy2027-eps-forecast-increased-by-erste-group-bank-2026-07-30/
- futuresearch (2026-08-04 表示): https://futuresearch.ai/app/p/a/msft-2027-08-04
- vcpscanner MSFT (独自モデル): https://vcpscanner.com/valuation/msft/estimates
- Webull MSFT: https://www.webull.com/news/15327609602122752

---

## 表D: ORCL の株価推移 (月末終値)

注記: 月末終値は、出典付きで確定できた値がなかった。下表は全行欠損。参考になる日次値は備考に残した。

| 月 | 月末終値 (USD) | 出典 | 備考 |
|---|---|---|---|
| 2025-01 | 欠損 | - | - |
| 2025-02 | 欠損 | - | - |
| 2025-03 | 欠損 | - | - |
| 2025-04 | 欠損 | - | - |
| 2025-05 | 欠損 | - | - |
| 2025-06 | 欠損 | - | - |
| 2025-07 | 欠損 | - | - |
| 2025-08 | 欠損 | - | - |
| 2025-09 | 欠損 | - | 2025-09-10 の終値最高 328.33 (ts2.tech) / 324.63 (Capital.com)。日次で月末ではない |
| 2025-10 | 欠損 | - | 2025-10-31 終値 262.61 が単一の検索要約に存在。出典URL特定不可のため欠損扱い (要確認) |
| 2025-11 | 欠損 | - | - |
| 2025-12 | 欠損 | - | - |
| 2026-01 | 欠損 | - | - |
| 2026-02 | 欠損 | - | - |
| 2026-03 | 欠損 | - | 2026-03-11 に株価 162.05 (MarketBeat 配当記事、日中の記述) |
| 2026-04 | 欠損 | - | - |
| 2026-05 | 欠損 | - | - |
| 2026-06 | 欠損 | - | 2026-06-11 決算後に 10% 超下落 (日中, sentisense 要約) |
| 2026-07 | 欠損 | - | 2026-07-15 安値 123.66 (単一要約) / 133.07 (Robinhood 表示)。2026-07-24 123.64 (Capital.com 要約) |
| 2026-08 | 欠損 | - | 2026-08 下旬 150.66 (Syfe 表示, 日付不明) |
| 2026-09 | 欠損 | - | 2026-09-04 158.78 / 2026-09-09 161.63 (日付ずれの指摘あり)。2026-09-18 147.61 (Benzinga)。2026-09-24 139.54 (日次, 3.47% 安) |
| 2026-10-09 | 141.40 | MarketBeat 速報 https://marketbeat.com/instant-alerts/price-oracle-nyse-orcl-shares-up-43-whats-next-2026-10-09 (検索要約) | **要確認**: 単一出典。月末ではなく当日終値 |

### 表D 欠損一覧
- 2025-01 から 2026-09 までの全月末終値 (21か月)
- 上記の日次値 (例: 2026-09-24 139.54) は月末ではないため本表に入れていない

### 表D 出典一覧 (取得日 2026-10-11)
- MarketBeat (2026-10-09): https://marketbeat.com/instant-alerts/price-oracle-nyse-orcl-shares-up-43-whats-next-2026-10-09
- TipRanks (2026-10-08): https://www.tipranks.com/news/why-oracle-stock-orcl-is-sinking-today-october-8-2026
- Capital.com (ATH/2026-07-24 関連): https://capital.com/en-eu/analysis/oracle-orcl-stock-forecast
- ts2.tech (2025-09 終値最高): https://ts2.tech/nl/oracles-ai-cloudbom-van-300-miljard-dollar-laat-orcl-aandeel-stijgen-wat-nu/
- Syfe (2026-08下旬): https://www.syfe.com/stocks/us/ORCL
- Robinhood (表示 2026-07-15): https://www.robinhood.com/stocks/ORCL
- MarketBeat 配当記事 (2026-03-11): https://www.marketbeat.com/instant-alerts/oracle-corporation-nyseorcl-announces-quarterly-dividend-of-050-2026-03-11/
- 日次 2026-09-24 139.54 と 2026-09-04 / 09-09 の値: 出典URL特定不可 (検索要約)

---

## 全体の出典注記
- 検索要約の一部は日付が前後しており、個別の値を引用する前に原典での確認が必要。
- 2026-10-11 時点の完全な値 (株価終値、52週レンジ、時価総額、株数) は、今回の検索では確定できなかった。Yahoo Finance、Nasdaq、Oracle IR (investor.oracle.com) での直接確認を推奨。
