# H5 欠損補完ログ (Oracle Corporation, NYSE: ORCL)

- 作成日: 2026-10-11 / 担当: データ収集 (H5)
- WebSearch 34/35 回を使用。WebFetch は未使用。
- 既存値は上書きせず、NA のセルのみ埋めた。数値の置換は 146 セル (年度 87、四半期 P&L 40、四半期 CF 19。年度・P&L の数には新区分列 15 セルを含む)。
- Tier: 1 = 10-K / 10-Q / 決算発表。検索要約経由で確認したもので、原本は開いていない。Tier 3 = 集計サイト・報道。「計」= 取得値からの計算値 (丸め誤差 ±0.1〜0.2)。
- 出典 ID (G01〜G35) は §7 に対応表あり。

## 1. 年度 (H1_annual.csv、USD bn。既存値は括弧で明記)

| 項目 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|
| 総売上 | 40.479 (T1) | 42.440 (T1) | 49.954 (T1) | 53.0 既存 (正値 52.961 T1) | 57.4 既存 (57.399 T1) | 67.4 既存 (67.357 T3) |
| 売上 YoY % | 4 (T1) | 5 (T1) | 17.7 計 | 6 既存 | 8 既存 | 17 既存 |
| CSLS (旧区分) | 28.700 (T1) | 30.174 (T1) | 35.307 (T1) | 39.383 (T1) | NA | NA |
| Cloud license + on-prem (旧区分) | 5.4 (T1 丸め) | 5.878 (T1) | 5.779 (T1) | 5.081 (T1) | NA | NA |
| Hardware | 3.359 (T1) | 3.183 (T1) | 3.274 (T1) | 3.066 (T1) | 2.936 (T3) | 3.084 (T3、決算 3.1 と整合) |
| Services | NA (残差 約3.0 は丸め込みのため不採用) | 3.205 (T1) | 5.594 (T1) | 5.431 (T1) | 5.233 (T3) | 5.743 (T3、決算 5.7 と整合) |
| Cloud (IaaS+SaaS、新区分) | - | - | - | 19.774 (T3) | 24.506 (T3) | 33.989 (T3、決算 34.0 と整合) |
| Software (新区分) | - | - | - | 24.690 (T3) | 24.724 (T3) | 24.541 (T3、決算 24.5 と整合) |
| GAAP 営業利益 | 15.213 (T1) | 10.926 (T1) | 13.093 (T1) | 15.353 (T1) | 17.7 (T1) | 20.6 (T1) |
| 非GAAP 営業利益 | 19.0 (T3) | 19.6 (T1) | 20.9 (T3) | 23.1 (T1) | 25.0 (T1) | 28.9 既存 |
| GAAP 純利益 | 13.746 (T1) | 6.717 (T1) | 8.503 (T1) | 10.467 (T1) | 12.4 既存 | 17.0 (T1、普通株主帰属) |
| GAAP EPS | 4.55 (T1、見出し値) | 2.41 (T1) | 3.07 (T3) | 3.71 (T1、見出し値) | 4.34 (T1) | 5.83 既存 |
| 非GAAP EPS | 4.67 (T3) | 4.90 (T1) | 5.12 (T3) | 5.56 (T1) | 6.00 既存 (6.03 T1 は §4) | 7.631 既存 |
| 営業CF | 15.887 (T1) | 9.539 (T1) | 17.165 (T1) | 18.673 (T1) | 20.8 既存 (20.821 T1) | 31.977 (T1、10-K MD&A 抽出) |
| Capex | 2.135 (T1) | 4.511 (T1) | 8.695 (T1) | 6.866 (T1) | 21.215 (T1) | 55.663 (T3、10-K 本文 55.7 と整合) |
| FCF (OCF − Capex) | 13.752 計 | 5.028 計 | 8.470 計 | 11.807 計 | −0.394 計 | −23.686 計 (会社発表 −23.7、T1) |
| SBC | 1.837 (T1) | 2.613 (T1) | 3.547 (T1) | 3.974 (T1) | 4.674 (T1) | 4.811 (T3、2社一致) |
| 減価償却費 (Depreciation) | 1.537 (T1) | 1.972 (T1) | 2.526 (T1) | 3.129 (T1) | 3.867 (T1) | 7.600 (T3) |
| 希薄化後加重平均株数 (百万株、列名は end) | NA | NA | NA | NA | 2,866 (T3) | 2,914 (T3) |

補足: 無形資産償却は FY21〜FY26 で 1.379 / 1.150 / 3.582 / 3.010 / 2.307 / 約1.694 (計)。FY26 の 1.694 は D&A 9.294 (T3) から dep 7.600 を引いた計算値。

## 2. 四半期 P&L (H1_quarterly_pl.csv、USD bn)

| 項目 | Q1 FY26 | Q2 FY26 | Q3 FY26 | Q4 FY26 | Q1 FY27 |
|---|---|---|---|---|---|
| GAAP 営業利益 | 4.3 (T1) | 4.7 (T1) | 5.5 (T1、約値) | 6.1 (T1) | 6.7 既存 (T1) |
| 非GAAP 営業利益 | 6.2 (T1) | 6.7 (T1) | 7.4 (T1) | 8.6 (T1) | 8.2 既存 |
| 非GAAP 営業利益率 % | 41.6 計 | 41.6 計 | 43.0 計 | 44.8 計 | 42.5 既存 |
| 希薄化後株数 (百万株) | 2,909 (T3) | NA | 2,912 (T3) | 2,915 (T1 決算表) | NA (NI÷EPS の計算示唆 約3.0B のみ、未採用) |
| Software (新区分) 売上 / YoY | 5.7 / −1% (T1) | 5.9 / −3% (T1) | 6.119 / +3% (T1) | 6.86 計 / NA | 5.55 / −3% (T3) |
| Hardware | 0.670 (T1 決算表) | 0.776 (T1 決算表) | 0.714 (T1 決算表) | 0.924 計 | 0.774 既存 (T3) |
| Services | 1.349 (T1 決算表) | 1.428 (T1 決算表) | 1.443 (T1 決算表) | 1.523 計 | 1.414 既存 (T3) |
| Cloud 合計 / YoY | 7.2 / +28% (T1) | 8.0 / +34% (T1) | 8.9 既存 (8.914 T1、§4) | 9.88 計 / NA | 11.6 既存 |
| IaaS (OCI) | 3.3 既存 | 4.1 / +68% (T1) | 4.9 既存 | 5.8 既存 | 7.4 既存 |
| SaaS | NA (計 約3.9) | 3.9 / +11% (T1) | 4.0 既存 | NA | 4.2 既存 |

計算の根拠: Q4 FY26 の Software 6.86 と Cloud 9.88 は FY26 通期 (G01 / G18) から Q1〜Q3 を差し引いた値。Q4 の Hardware 0.924 と Services 1.523 も同じ方法。Q1 FY26 の SaaS は Cloud 7.2 から IaaS 3.3 を引いた値 (約3.9) で、計算値のため NA のまま。

## 3. 四半期 CF (H1_quarterly_cf.csv、USD bn)

| 項目 | Q1 FY26 | Q2 FY26 | Q3 FY26 | Q4 FY26 | Q1 FY27 |
|---|---|---|---|---|---|
| 営業CF (四半期) | 8.140 (T1、10-Q 比較列) | 2.066 計 (既存 2.1 と整合) | 7.151 計 | 14.620 計 | 23.103 (T1 10-Q、既存 23 と整合) |
| Capex (四半期) | 8.502 (T1) | 12.033 計 (既存 12 と整合) | 18.635 計 | 16.493 計 | 28.499 (T1、既存 28.5 と整合) |
| FCF (四半期) | −0.362 計 | −9.967 計 (既存 −10 と整合) | −11.484 計 | −1.873 計 | −5.396 計 (既存 −5 と整合) |
| SBC (四半期) | 1.124 (T1) | 1.156 計 | NA | NA | 1.127 (T1) |
| 減価償却費 (四半期) | 1.351 (T1) | 1.704 計 | NA | NA | 3.156 (T1) |
| 営業CF TTM | NA | NA | NA | 31.977 (T1) | 46.940 計 |
| Capex TTM | NA | NA | NA | 55.663 (T3) | 75.660 計 (既存 75.7 と整合) |
| FCF TTM | NA | NA | NA | −23.686 計 (会社 −23.7、T1) | −28.720 計 (既存 −28.7 と整合) |

計算の根拠 (Tier 1 派生): 6か月累計 OCF 10.206・Capex 20.535・SBC 2.280・dep 3.055 (G10)。9か月累計 OCF 17.357・Capex 39.170 (G11)。FY26 通期 OCF 31.977 (G01)・Capex 55.663 (G18、T3)。Q3 OCF 7.151 は vcpscanner (G22、T3) の 7.15 と一致。

## 4. 既存値との差異・注意 (上書きせず併記)

1. FY2025 非GAAP EPS: 既存 6.00 (AI 要約・低信頼) に対し、決算発表は 6.03 (G27 T1)。既存値は残した。採用値の判断は後段に委ねる。
2. FY2024 売上: 既存 53.0 に対し 10-K は 52.961 (G04 T1)。丸め差で整合。既存維持。
3. Q3 FY26 Cloud 合計: 既存 8.9 (T3) に対し決算表 8.914 (G11 T1)。丸め差。既存維持。
4. Q2 FY26 CF: 既存注記 "すべて決算通話記録 [T3]" に対し、10-Q 派生値 (G10 T1) で既存の 2.1 / 12 / −10 と整合。既存注記は残した。
5. Q1 FY27 CF: 既存の 23 / 28.5 / −5 / 75.7 は 10-Q の 23.103 / 28.499 / −5.396 / 計 75.66 と整合。既存維持。
6. Q1 FY27 Software: 既存注記 5.5 (旧欄へ割当てず) に対し、新区分列に 5.55 (G17 T3)。新区分列 software_new_* を追加。
7. 列名 diluted_shares_end_m は値が加重平均 (weighted average) で、列名と実体が一致しない。
8. FY2026 GAAP 純利益 17.0 は普通株主帰属 (net income available to common)。
9. 年度 EPS の基本・希薄化区分: FY21・FY24・FY25・FY26 の GAAP EPS は見出し値で、basic / diluted の区分は未確認。FY25・FY26 は希薄化後株数 2,866・2,914 で NI÷株数と整合するため、希薄化後と推定。

## 5. Q1 FY27 顧客前払い (item 3) の計上区分

- 金額: 顧客前払い (重要な金融要素を含む前払い) は約 11.363 億ドル (G23 の reconciliation 表記、T1 候補・期間未確認。G24 (T3) は 11.3 と報道)。
- 計上区分: G23 の記述は「顧客前払い (重要な金融要素を含むもの) を GAAP キャッシュフロー計算書の営業活動に計上」と読める。G24 (T3) も、Q1 FY27 の営業CF 23.1 が前払い 11.3 の寄与で増えたと報じる。財務CFに計上したとする記述は見つからなかった。
- 注意: G23 は 000119312526265848 (2026-06 提出の 8-K) で、Q1 FY27 (2026-09 提出) の決算表ではない可能性がある。この記述の期間は未確認。Q1 FY27 10-Q (G09) のキャッシュフロー計算書の原本で要確認。
- 関連 (T3、G35): 前払いと短期 Capex 融資返済 0.83B を差し引いたネット Capex は約 17.97B (ctol.digital 報道)。ATM 純額は 19.909 百万 (G09 の 10-Q 要約 T1)、約 141 百万株 (G25 T3)。

## 6. まだ欠損の項目 (優先順)

年度:
- FY21: Services (残差約3.0 は丸め込みのため NA)、Cloud license の正確値 (5.4 は丸め)、希薄化後株数、GAAP EPS の basic / diluted 区分。
- FY22〜FY24: 希薄化後株数 (全年度 NA)。FY22 の GAAP EPS は確認済み (2.41) だが区分は未確認。
- FY23: GAAP EPS 3.07 と非GAAP 値 (5.12 / 20.9) は T3 のみで、10-K 原本で要照合。
- FY24: GAAP EPS 3.71 の basic / diluted 区分が未確認。
- FY25・FY26: 旧区分の CSLS・Cloud license は NA のまま (新区分へ移行)。
- 全年度: OCI・SaaS の年度値は NA。
- FY26: 減価償却費 7.600 と無形償却 1.694 (計) は T3 のみで、10-K で要確認。

四半期:
- 希薄化後株数: Q2 FY26 と Q1 FY27 が NA。
- Q3 FY26・Q4 FY26 の SBC と減価償却: 9か月累計 10-Q が未取得のため NA。
- Q4 FY26 の SaaS・Cloud の前年比、RPO の前年比: NA。
- Q1 FY26 SaaS (計 約3.9 のみ)、Q1 FY26・Q2 FY26・Q3 FY26 の GAAP 営業利益の前年比: NA。
- FY24 と FY25 の四半期 CF、および FY26 の四半期 TTM OCF と Capex (FY25 四半期が必要): NA。
- 配当・自社株買い: 全期間 NA (未検索)。
- Q1 FY27 の Hardware / Services / Software は T3 のみ (原本未確認)。

## 7. 出典 ID

| ID | 文書 | URL | Tier |
|---|---|---|---|
| G01 | Oracle FY26 10-K | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526277521/orcl-20260531.htm | 1 (検索抽出、原本未開封) |
| G02 | Oracle Q4 FY26 8-K Ex99.1 (2026-06-10) | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526265848/orcl-ex99_1.htm | 1 (検索要約) |
| G03 | Oracle Q4 FY25 8-K Ex99.1 (2025-06-11) | https://www.sec.gov/Archives/edgar/data/1341439/000095017025084831/orcl-ex99_1.htm | 1 |
| G04 | Oracle FY24 10-K | https://www.sec.gov/Archives/edgar/data/1341439/000095017024075605/orcl-20240531.htm | 1 |
| G05 | Oracle FY23 10-K | https://www.sec.gov/Archives/edgar/data/1341439/000095017023028914/orcl-20230531.htm | 1 |
| G06 | Oracle FY22 Q4 8-K Ex99.1 (2022-06-13) | https://www.sec.gov/Archives/edgar/data/1341439/000156459022023099/orcl-ex991_6.htm | 1 |
| G07 | Oracle FY21 決算発表 (2021-06-15) | https://www.sec.gov/Archives/edgar/data/1341439/000156459021032994/orcl-ex991_6.htm (URL は検索結果の候補。要照合) | 1 (検索要約) |
| G08 | Oracle FY22 10-K | https://www.sec.gov/Archives/edgar/data/1341439/000156459022023675/orcl-10k_20220531.htm | 1 |
| G09 | Oracle Q1 FY27 10-Q (2026-08-31 期末) | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm | 1 (検索要約。Q1 FY26 比較列を含む) |
| G10 | Oracle Q2 FY26 10-Q (2025-11-30 期末、6か月累計) | https://www.sec.gov/Archives/edgar/data/1341439/000119312525315925/orcl-20251130.htm | 1 (検索要約) |
| G11 | Oracle Q3 FY26 8-K Ex99.1 (2026-03-10、9か月累計 CF・区分売上) | https://www.sec.gov/Archives/edgar/data/1341439/000119312526100148/orcl-ex99_1.htm | 1 (検索要約) |
| G13 | Oracle Q2 FY26 決算表 PDF | https://s23.q4cdn.com/440135859/files/doc_earnings/2026/q2/supplemental-info/Q226_Form8K_Exhibit99-1_Earnings_Release_Tables-Final.pdf | 1 (検索要約) |
| G14 | Oracle Q1 FY26 決算表 PDF | https://s23.q4cdn.com/440135859/files/doc_financials/2026/q1/Q126_Form8K_Exhibit99-1_Earnings_Release_Tables-Final.pdf | 1 (検索要約) |
| G15 | Oracle Q4 FY26 決算表 PDF | https://s23.q4cdn.com/440135859/files/doc_earnings/2026/q4/supplemental-info/Q426_Form8K_Exhibit99-1_Earnings_Release_Tables-Final.pdf | 1 (検索要約) |
| G16 | Oracle Q1 FY27 決算発表 (2026-09-10) | https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/ | 1 (検索要約経由) |
| G17 | Verdict Q1 FY27 報道 | https://www.verdict.co.uk/oracle-q1-fy27-results/ | 3 |
| G18 | StockAnalysis (ORCL cash flow) | https://stockanalysis.com/stocks/orcl.prd/financials/cash-flow-statement/ | 3 |
| G19 | edgar.tools (ORCL) | https://app.edgar.tools/companies/ORCL | 3 |
| G20 | Futurum Research (FY21〜FY23 の年度値の引用) | https://futurumgroup.com/insights/oracle-revenue-up-5-for-q4-fy2022-as-cloud-sales-grow/ | 3 |
| G21 | TMGM 分析 (Q4 Capex 約16.5 など) | https://www.tmgm.com/en/analysis/market-insight/oracle-capex-boom-overshadows-strong-earnings | 3 |
| G22 | vcpscanner 四半期 CF | https://vcpscanner.com/stock/orcl/cash-flow/quarterly | 3 |
| G23 | Oracle 8-K Ex99.1 (顧客前払いの分類記述、期間未確認) | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526265848/orcl-ex99_1.htm | 1 候補 (期間未確認) |
| G24 | mitrade (2026-09-11、Q1 FY27 の OCF 報道) | https://www.mitrade.com/insights/news/live-news/article-3-2078592-20260911 | 3 |
| G25 | neoteo (Q1 FY27 の FCF・ATM) | https://www.neoteo.com/en/oracle-reports-5396-billion-in-negative-free-cash-flow-for-q1-fy2027 | 3 |
| G26 | Oracle FY25 10-K | https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/orcl-20250531.htm | 1 (検索抽出) |
| G27 | Oracle FY25 決算発表 (Seeking Alpha 掲載の PR) | https://seekingalpha.com/pr/20134119 | 1 (コピー) |
| G28 | Oracle FY24 8-K Ex99.1 (2024-06-11) | https://www.sec.gov/Archives/edgar/data/1341439/000095017024071916/orcl-ex99_1.htm | 1 (検索要約) |
| G29 | Oracle Q4 FY23 決算発表 (2023-06-12) | https://www.oracle.com/news/announcement/q4fy23-earnings-release-2023-06-12/ | 1 (検索要約) |
| G30 | opencapital.sh (ORCL 売上明細、新区分の年度値) | https://www.opencapital.sh/stocks/orcl/metrics/is_total_revenue | 3 |
| G31 | Oracle Q1 FY26 決算発表 (Seeking Alpha 掲載の PR) | https://seekingalpha.com/pr/20227035 | 1 (コピー) |
| G32 | Oracle Q2 FY26 決算発表 (Seeking Alpha 掲載の PR) | https://seekingalpha.com/pr/20335876 | 1 (コピー) |
| G33 | Oracle Q3 FY26 決算発表 (2026-03-10) | https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Fiscal-Year-2026-Third-Quarter-Financial-Results/default.aspx | 1 (検索要約) |
| G34 | alphaquery (ORCL 希薄化後加重平均株数) | https://www.alphaquery.com/stock/ORCL/fundamentals/annual/weighted-average-shares-outstanding-diluted | 3 |
| G35 | ctol.digital (Q1 FY27 のネット Capex 関連報道) | https://www.ctol.digital/news/oracle-q1-cash-outlay-hits-17-97b-70b-capex-plan-stays-on-track/ | 3 |

既存 ID (R01〜R32 等) は既存 CSV の source_ids をそのまま残し、新 ID を後ろに追記した。
