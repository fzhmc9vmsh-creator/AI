# ORCL データ収集 H6: 欠損補完ログ

取得日: 2026-10-11 / 対象: ORCL (決算期末 5月31日, 最新報告 Q1 FY2027 = 2026-09-10) とピア
更新先: H2_consensus.csv, H2_market.csv, H2_price_monthly.csv, H2_peers.csv (既存の値は消さず、追記・NA の置換のみ)

## 作業の前提と注意

- WebSearch: 33回 / 上限35回. WebFetch: 0回 (使用せず).
- すべての値は WebSearch の要約経由. 原ページは直接開いていない. 要約の数値は出典ごとに掲載日がばらつくため、各行に掲載日・取得日を併記した.
- 2026-10-10 は土曜日 (NYSE 休場). 2026-10-09 は金曜日. 「2026-10-10 の終値」は存在しない.
- 「要確認」: 単一出典、掲載日不明、年度・定義が未確定、または出典間で不一致の値.
- 「自己計算」: 取得済みの値から計算した値. 入力の出典を併記.

## 1. 今回埋めた値の一覧 (項目 / 値 / 出典)

### 1-1. ORCL コンセンサス (H2_consensus.csv)

| 項目 | 値 | 出典 | 掲載日・状態 |
|---|---|---|---|
| FY2027 EPS (非GAAP系の可能性, 年度は推定) | 平均 8.05 / 最高 8.15 / 最低 7.82 / 25名 | https://tickerleague.com/companies/ORCL/price-target (検索要約) | 掲載日不明. ページは "next fiscal year" と表記. FY27 と推定 (要確認). 会社ガイダンス 8.10 に近い |
| FY2028 売上 (平均・高・低) | 129.79 / 130.14 / 129.44 B USD / 35社 | https://www.tickflow.io/stock/ORCL/forecast (検索要約) | 掲載日不明. Yahoo 131.5 (2026-09-30) と不一致 (要確認) |
| FY2029 売上 (平均・高・低) | 183.24 / 185.60 / 176.05 B USD / 17社 | 同上 | 掲載日不明. EPS は未取得 |
| FY2029 EPS (独自モデル, 非コンセンサス) | 9.37 | https://www.vcpscanner.com/valuation/orcl/estimates | 出典自身がコンセンサス未満と表示. 参考のみ |
| FY2030 EPS (独自モデル, 非コンセンサス) | 10.52 | 同上 | 同上 |
| FY2030 会社目標 (コンセンサスではない) | non-GAAP EPS 21 / 売上 225 B USD | Oracle アナリストデー報道 (検索要約, URL特定不可) | 2025-10頃. 年率28% |
| FY2030 古い参考 (現行ではない) | EPS 18.92 / 売上 198.4 B USD | LSEG データ引用 (検索要約, URL特定不可) | アナリストデー前 (2025-10頃). 採用せず参考 |

### 1-2. ORCL 市場データ (H2_market.csv)

| 項目 | 値 | 出典 | 掲載日・状態 |
|---|---|---|---|
| 52週安値 (2026年内の安値, 窓内と判断) | 114.51 USD | https://www.investsmart.com.au/security/nyse/orcl/oracle-corp/share-price (検索要約) | 2026-09-05 表示. 別出典 Upstox 114.54 (2026-08-08) と一致 |
| 希薄化後株式数 (Q1 FY27 加重平均 diluted) | 3000 百万株 | Oracle Q1 FY27 決算発表 (placera.se 再掲) https://www.placera.se/pressmeddelanden/oracle-announces-q1-results-driven-by-triple-digit-growth-in-cloud-infrastructure-revenues-20260910 | 2026-09-10. 単位 (百万株) は表の桁からの推定 (要確認). 前年同期 2909. 10-Q 原文 (https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm) は未確認 |
| 基本加重平均株数 (参考, 期末株数ではない) | 2966 百万株 | 同上 | 2026-09-10 |
| 時価総額 (2026-10-09) | 419.4 B USD (自己計算) | 141.40 x 2966 百万株 | 加重平均株数で代用. 期末発行株数ではない |
| 予想PER 今期 (自己計算) | 17.7 | 141.40 / 7.98 (TickFlow FY27 平均) | 入力の EPS は掲載日不明 |
| 予想PER 来期 (自己計算) | 13.1 | 141.40 / 10.78 (TickFlow FY28 平均) | 入力の EPS は掲載日不明. FY28 レンジ 7.36-14.05 と広い |
| 予想PER 会社ガイダンス基準 (自己計算) | 17.5 | 141.40 / 8.10 (Oracle 2026-09-10 ガイダンス) | コンセンサスではない |

### 1-3. ORCL 月末終値 (H2_price_monthly.csv)

出典: Digrin ORCL 月次表の real 列 https://www.digrin.com/stocks/detail/ORCL/price (検索要約経由).
real 列を月末終値とみなした根拠: 2025-10 の real 値 262.61 が TipRanks の 2025-10-31 終値 262.61 と一致. 原表の直接確認は未実施.

| 月 | 終値 (USD) | 備考 |
|---|---|---|
| 2025-01 | 170.06 | |
| 2025-02 | 166.06 | |
| 2025-03 | 139.81 | |
| 2025-04 | 140.72 | |
| 2025-05 | 165.53 | |
| 2025-06 | 218.63 | |
| 2025-07 | 253.77 | |
| 2025-08 | 226.13 | |
| 2025-09 | 281.24 | 日次の最高終値 (2025-09-10) は 324.63 / 328.33 で月末ではない |
| 2025-10 | 262.61 | 2出典一致 (Digrin / TipRanks) |
| 2025-11 | 201.95 | |
| 2025-12 | 194.91 | Fund Library 194.91 と一致. Macrotrends/Capital.com 194.39 とは不一致 (要確認) |
| 2026-01 | 164.58 | 2026-01-26 終値 182.44 (別ページ) より低い. 要確認 |
| 2026-02 | 145.40 | 2026-02-06 終値 142.62 (Macrotrends) と整合的 |
| 2026-03 | 147.11 | adjusted 146.09 |
| 2026-04 | 161.39 | adjusted 160.83 |
| 2026-05 | 225.78 | adjusted 225.00. 2026-06-03 終値 230.33 (StockAnalysis) と整合的 |
| 2026-06 | NA | Digrin は adjusted 146.04 のみ. real 列未取得のため欠損のまま |
| 2026-07 | 129.87 | adjusted 同値 |
| 2026-08 | 144.50 | Digrin の表示 (月末性の明示なし, 要確認). 8/19 終値 143.81 / 8/26 終値 148.85 と整合的 |
| 2026-09 | NA | 9/30 終値は未取得 |

### 1-4. ピア (H2_peers.csv)

| ティッカー | 株価 (日付) | 時価総額 | 予想PER | EPS / PEG | 出典 |
|---|---|---|---|---|---|
| MSFT | 499.70 (2026-09-04, 既存). 501.61 (2026-09-21, ts2.tech 単一) は備考 | 3.71 T USD (自己計算: 499.70 x 7.43B株) | 今期 25.4 / 来期 21.6 (自己計算: 499.70 / 19.64 および / 23.18) | EPS FY27 19.59 / FY28 23.18 (MarketBeat 2026-09-04 掲載ページ). PEG 1.60 (Yahoo 5年 expected, 掲載日不明) | MarketBeat, Yahoo Finance key-statistics, blockchain.news |
| AMZN | 254.46 (2026-09-24 記事, "約") | NA (株数の出典なし) | 来期 24.3 (自己計算: 254.46 / 10.47) | 2027 EPS 10.47 (要確認: 52社, 出典URL特定不可) | 247wallst 2026-09-24 |
| GOOGL | 343.50 (2026-10-02, 出典URL特定不可) | NA | 今期 21.87 (GuruFocus, 2026-09-04) | PEG 0.58 (FullRatio, 2026-06-10). 成長率の基準が他社と不整合 (要確認) | GuruFocus, FullRatio, Benzinga |
| META | 616.77 (2026-09-04; Yahoo と blockchain.news の2出典一致) | 1.57 T USD (blockchain.news / 自己計算: 616.77 x 2.538B株) | 今期 16.84 (GuruFocus 2026-08-21, ドイツ上場 FRA:FB2A の値) | PEG 1.24 (Stockopedia, 掲載日不明) | Yahoo Finance history, blockchain.news, GuruFocus, Stockopedia |
| CRWV | 87.59 (2026-09-25, 中国語記事, 単一出典) | 48.3 B USD (自己計算: 87.59 x 551.5M株) | NM (赤字. Seeking Alpha 2026-04-02) | 算出不能 | 10jqka 記事, fundlibrary, Seeking Alpha |
| NBIS | NA | NA | NM (Seeking Alpha 2026-03-18) | NA | Seeking Alpha |
| SAP | 216.43 (2026-08-19, GuruFocus) | NA | 今期 21.10 (Yahoo key-statistics, 掲載日不明) | 5年 expected PEG 1.55 (Yahoo, 掲載日不明) | GuruFocus, Yahoo |
| NOW | 132.53 (2026-09-12, investsmart, 単一) | NA | NA | NA | investsmart |
| CRM | NA (採用できる日付付きの値なし) | NA | NA | NA | 全値が掲載日不明で不一致 |
| IBM | 233.87 (2026-09-01, GuruFocus) | NA | NA (実績 PER 20.75 は備考) | PEG 2.42 (GuruFocus 2026-08-22). 基準は 5年 EBITDA 成長 8.10% で予想EPS成長ではない (要確認) | GuruFocus |

LTG (3〜5年EPS成長率) は全社 NA. 出典の値はいずれも年次の予想成長率か、後ろ向きの実績で、LTG として採用できなかった.

## 2. 既存の値に対する注意・訂正 (値は消さず、備考で注記)

1. ORCL 日中レンジ 136.50-142.90 (2026-10-10): 土曜日のため取引なし. 無効の可能性が高い. 行は残し備考に注記.
2. ORCL 株価 2026-10-09 終値 141.40: 単一出典 (MarketBeat). 3回の検索で2出典目を確認できず. 要確認のまま.
3. FY2028 売上: TickFlow 129.79 と Yahoo 131.5 (2026-09-30) が不一致.
4. 52週高値: 既存の 345.72 は 2025-09-10 付近で窓外. 窓内 (2025-10-09 以降) の最高値は未確定. 下限 311.01 (2025-10-15 日中, MarketBeat 検索要約, 要確認).
5. 2025-12 月末終値: 194.91 (Digrin / Fund Library) と 194.39 (Macrotrends / Capital.com) が不一致.
6. 2026-01 月末終値 164.58 は 1/26 終値 182.44 より低く、月末性を要確認.
7. MSFT の既存 EPS 19.64 は単一の要約. MarketBeat の 19.59 (2026-09-04 掲載ページ) とは 0.05 差.
8. 2026-09 の既存日次値: 9/4 158.78 (H2 既存表記) と investsmart の 5 Sep 158.78 で日付が不一致.

## 3. 採用しなかった値 (不採用の理由)

- AMZN 時価総額 自己計算 2.73T: 株数の出典がないため不採用.
- AMZN 予想PER 27.19 (stockanalysis) / 31.15 (dividend.watch): 掲載日不明.
- NBIS 株価 286.69 / 時価総額 $53.25bn (Stockopedia): 掲載日不明.
- NBIS 次期 EPS -2.45 (Stockopedia): 年度と日付が不明.
- CRM 株価 293.92: 掲載日不明の記事.
- ORCL Q1 FY27 決算前 non-GAAP EPS コンセンサス 1.74: 出典URL特定不可. 参考候補のみ.
- ORCL FY27 売上 86.32 / 86.61 B (2026-03 頃 上方修正前): 古い. 参考のみ.
- ORCL Yahoo 予想 EPS 成長 (2024-05 時点の 5年 10.08%): 古い.
- Seeking Alpha の FY28-FY30 EPS 成長率 (35.85% / 45.74%): 水準ではなく成長率で、基準値が不明.
- GOOGL Stockopedia PEG 2.23 / Bullfincher 0.12, META Zacks PEG 1.73, IBM Zacks PEG 2.58-4.25: 掲載日不明で出典間不一致.

## 4. まだ欠損の項目

### ORCL
- FY2027 売上: Q1 後のドル建てコンセンサスなし (会社ガイダンス 90B 以上のみ). FY27 売上 最高・最低 NA.
- FY2028 EPS: 平均 10.78 (TickFlow) は既存. 最高・最低は TickFlow の 14.05 / 7.36 のみ (既存).
- FY2029 EPS: 現行のコンセンサス NA.
- FY2030 EPS・売上: 現行のコンセンサス NA (古い LSEG 値と独自モデル値のみ).
- FY2031: 全項目 NA.
- 52週高値 (窓内): NA (下限 311.01 のみ).
- 2026-10-09 終値: 2出典目なし.
- 2026-06 月末終値: real 列未取得. 2026-09 月末終値: 未取得.
- 2025-2026 月末値: 原表 (Digrin / Yahoo / StockAnalysis) の直接照合は未実施.
- 発行済株式数 (期末時点): NA. 10-Q 原文の照合は未実施.
- 配当 10月分 (record 2026-10-09 / pay 2026-10-23): 単一出典のまま.
- Q2 FY27 コンセンサス (Q1 後): NA.
- 直近3か月のコンセンサス EPS 修正方向: NA.

### ピア
- 時価総額: AMZN, GOOGL, NOW, CRM, IBM, NBIS, SAP は NA. CRWV と MSFT META は自己計算.
- 予想PER 今期/来期: NOW, CRM, IBM (予想), NBIS (NM のみ), AMZN 今期, GOOGL 来期, META 来期, CRWV (NM) で欠損.
- EPS 今期/来期/2年後: AMZN 今期, GOOGL 全項目, META 全項目, CRWV, NBIS, SAP, NOW, CRM, IBM で欠損.
- LTG: 全社 NA.
- PEG: AMZN, NOW, CRM, NBIS, CRWV で欠損. 掲載日つきの値は GOOGL (2026-06-10) のみ. 他は掲載日不明.
- 株価の日付: NBIS, CRM に日付付きの株価なし. 全社で 2026-10-09 時点の値なし (最新は GOOGL 2026-10-02).

## 5. 自己計算の内訳 (再計算用)

- ORCL 時価総額 419.4 = 141.40 x 2966 (百万株) / 1000 (B USD)
- ORCL 予想PER: 141.40 / 7.98 = 17.7; 141.40 / 10.78 = 13.1; 141.40 / 8.10 = 17.5
- ORCL Q1 FY27 EPS 検算: 4,679 / 3,000 = 1.56 (既存の diluted EPS 1.56 と一致)
- MSFT 時価総額 3.71 T = 499.70 x 7.43B. PER: 499.70 / 19.64 = 25.4; 499.70 / 23.18 = 21.6; 499.70 / 19.59 = 25.5 (参考)
- AMZN 来期PER 24.3 = 254.46 / 10.47
- GOOGL 次の4四半期 EPS 合計 12.95 = 3.00 + 3.31 + 3.24 + 3.40 (Benzinga). NTM PER 26.5 = 343.50 / 12.95 (参考, 表には未採用)
- META 時価総額 1.57 T = 616.77 x 2.538B (Equibles 株数)
- CRWV 時価総額 48.3 B = 87.59 x 551.5M (fundlibrary 株数)

## 6. 取得件数

- WebSearch 33回 (上限35回). WebFetch 0回.
- 新規に値を埋めた項目: 57 (ORCL コンセンサス 7行, 市場データ 6項目, 月末終値 19か月, ピア 25項目).
