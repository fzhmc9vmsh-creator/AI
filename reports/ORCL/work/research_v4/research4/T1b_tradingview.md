# T1b: TradingView 掲載の Oracle (NYSE:ORCL) 予想値の確認

基準日: 2026-10-15。対象: Oracle (NYSE: ORCL)、決算期末 5 月末 (FY27 = 2026-06〜2027-05)。
出力: 事実・数値・出典の整理のみ。投資判断・推奨は含まない。
取得手段: WebSearch のみ (検索 12 回、上限到達)。WebFetch は未使用。
凡例: `*` = 検索要約 (WebSearch の結果テキスト) 経由。本文そのものは未確認。`(算出)` = 本調査での計算。`欠損` = 見つからず。

---

## 0. 要約

1. 前提の訂正: 既存 CSV には TradingView 由来の行が既に 4 件ある (行 109 BOATS-ORCL 目標株価 337.42、行 111 ar.NYSE-ORCL の直近 EPS 2.11・次期 1.74、行 112-113 ユーザー投稿アイデア FY28 EPS 15.19・売上 175.6)。「無いことの確認」は成立しないため、既存行は再掲に留め、新規値と並べて比較した。
2. NYSE-ORCL 予想ページ (in.tradingview.com 版、時点不明*): 目標株価 平均 241.68 USD、高 400、安 155、アナリスト 37 名 (1 年予想)。同系要約には 46 名 (過去 3 か月) の記載もある。
3. BOATS-ORCL 予想 (既存行 109 と同値を再確認*): 平均 337.42、高 400、安 175.14、45 名 (過去 3 か月窓)。NYSE 版との差は 95.74 (算出)、対 241.68 で +39.6% (算出)。
4. TradingView 掲載の別分析 (時点不明*): 45 名 (Buy 36 / Hold 8 / Sell 1)、平均 243.97。TradingView News の集計 (6 月終値基準の記述、推定 2026-06*): 平均 256〜257、37 名、範囲 155〜400。
5. NYSE:ORCL 本体の四半期欄 (2026-09-10 以降と推定*): 直近 EPS 1.92 (予想 1.74)、売上 19.34B (予想 19.13B)。次期 EPS 1.89、次期売上 21.31B。
6. 次期 Q2 FY27 の比較: EPS 1.89 は会社ガイダンス中点 1.89 と一致 (算出)。売上 21.31B はガイダンス中点 21.20 より +0.11 (+0.5%、算出) で、掲載元により食い違う。
7. FY27 EPS: TradingView 経由のコンセンサス 8.13* (Zacks 系、時点不明) は既存 CSV の 7.98〜8.06 より +0.07〜+0.15 高い (算出)。会社ガイダンス 8.10 (Tier 1 原典) とは +0.03 (算出)。
8. FY27 ガイダンス (Tier 1 原典の報道経由*): 売上 90.0B 以上、non-GAAP EPS 8.10、総 capex 90〜95B、純現金 capex 70B 以下。既存 CSV 行 32・34・102-103 と一致。
9. TradingView の FY28・FY29 年度別 EPS・売上は取得できず (欠損)。TradingView 掲載の FY27 売上コンセンサスも欠損 (ガイダンス下限のみ)。
10. 食い違いが大きい項目: 目標株価の安値 (110 / 155 / 175.14)、分析人数 (37 / 45 / 46)、直近 EPS の期 (2.11 = Q4 FY26 と 1.92 = Q1 FY27 が掲載元ごとに併存)。ページ日付がほぼ取れず、窓や時点の差は未解決。

---

## 1. 前提の確認と既存 CSV との関係

- 既存 `T1_consensus.csv` を Read した。TradingView 由来の行は次の 4 件:
  - 行 109: TradingView BOATS-ORCL forecast、目標株価 337.42、45 名、窓 = 過去 3 か月 (注記に「既存 H2 は 34 名」)。
  - 行 111: TradingView ar.NYSE-ORCL forecast-price-target、直近 EPS 2.11、予想 1.96、次期 1.74 (既存 H2 再掲)。
  - 行 112: TradingView ユーザー投稿アイデア、FY28 EPS 15.19 (2025 頃、Tier 4)。
  - 行 113: 同、FY28 売上 175.6 (Tier 4)。
- 今回の検索で、NYSE 本体の TradingView 予想ページ (年度別の表) の本文は取得できなかった。TradingView の検索結果は、ほぼ「掲載ページ名 + 要約の数値」のみ。

---

## 2. TradingView 掲載値 (今回取得分)

### 2-1 目標株価・アナリスト数

| # | 掲載 (ページ/記事) | 平均 | 高 | 安 | 人数・窓 | 時点 | 出典 | Tier | 備考 |
|---|---|---|---|---|---|---|---|---|---|
| T-1 | NYSE-ORCL 予想 (in.tradingview 版) | 241.68* | 400* | 155* | 37 名 (1 年予想)*; 46 名 (過去 3 か月)* | 不明 | https://in.tradingview.com/symbols/NYSE-ORCL/forecast/ | 3 | 同要約内に「最高・最安の記載は無い」との記述もあり、要確認 |
| T-2 | TradingView 掲載の分析 (掲載形式・URL 未特定) | 243.97* | 欠損 | 欠損 | 45 名 (Buy 36 / Hold 8 / Sell 1)* | 不明 | 欠損 (URL 未特定) | 3 (暫定) | 同分析は MarketBeat の 297 から 256 への変更にも言及* |
| T-3 | BOATS-ORCL 予想 (既存行 109、今回も再確認) | 337.42* | 400* | 175.14* | 45 名 (過去 3 か月窓)* | 不明 | https://in.tradingview.com/symbols/BOATS-ORCL/forecast | 3 | BOATS は NYSE 本体ではない別取引所コードの表示。窓や掲載日の違いが考えられるが未確認 |
| T-4 | NYSE:ORCL 本体・ar 版 forecast-price-target (要約) | 欠損 | 400* | 110* | 欠損 | 不明 | https://www.tradingview.com/symbols/NYSE-ORCL/ ; https://ar.tradingview.com/symbols/NYSE-ORCL/forecast-price-target/ | 3 | 要約には安値のみ。平均は欠損 |
| T-5 | TradingView News の 12 か月目標集計 (MarketBeat 系の自動記事を含む、個別 URL 未特定) | 256〜257* | 欠損 | 155〜400* | 37 名* | 「6 月終値基準」の記述から推定 2026-06* | https://www.tradingview.com/news/ (個別未特定) | 3 | 見出しで個別の 12 か月目標 $257.24 / $256.45 / $256.46 も確認 (見出しのみ、本文未確認) |

証券会社別の目標株価 (TradingView News の要約*、時点は 2026-06〜09 の決算前後と推定):

| 証券会社 | 目標 (USD) | 評価 | 前回 | 出典 | Tier |
|---|---|---|---|---|---|
| UBS | 285* | Buy* | 250* | TradingView News (要約、URL 未特定) | 3 |
| Barclays | 252* | Overweight* | 250* | TradingView News (要約、URL 未特定) | 3 |
| Wedbush | 240* | 欠損 | 275* | TradingView News (要約、URL 未特定) | 3 |
| Stifel | 200* | Buy* | 220* | TradingView News (要約、URL 未特定) | 3 |
| Mizuho | 320* | Outperform* | 欠損 | TradingView News (要約、URL 未特定)。既存 CSV 行 110 と同値 | 3 |

- 人数の併記: 37 名 (T-1 と T-5 の一部)、45 名 (T-2、T-3)、46 名 (T-1 の別要約)。
- 目標株価の平均は、TradingView 掲載値だけで 241.68〜337.42 に散らばる。

### 2-2 四半期 (直近・次期) の TradingView 掲載値

| 掲載 | 直近 EPS (予想) | 次期 EPS | 直近売上 (予想) | 次期売上 | 推定時点 | 出典 | Tier |
|---|---|---|---|---|---|---|---|
| NYSE:ORCL 本体 | 1.92* (1.74*) | 1.89* | 19.34B* (19.13B*) | 21.31B* | 2026-09-10 以降 (直近 = Q1 FY27 のため推定) | https://www.tradingview.com/symbols/NYSE-ORCL/ | 3 |
| SIX-ORCL | 2.11* | 1.73* | 19.18B* | 19.12B* | 2026-06〜09 (直近 2.11 = Q4 FY26 のため推定) | https://www.tradingview.com/symbols/SIX-ORCL/ | 3 |
| ar.NYSE-ORCL (既存行 111) | 2.11 (予想 1.96) | 1.74 | 欠損 | 欠損 | 2026-06〜09 (推定) | https://ar.tradingview.com/symbols/NYSE-ORCL/forecast-price-target/ | 3 |
| NYSE-ORCL 予想 (in 版) | 1.79* (予想 1.70*) | 1.95* | 欠損 | 欠損 | 不明 (どの四半期か未特定) | https://in.tradingview.com/symbols/NYSE-ORCL/forecast/ | 3 |

- 注記 (SIX 行): 要約は「2.11 は本体と同一期」と記すが、2.11 は Q4 FY26 (2026-06-10 報告、Benzinga 要約*) と読めるため、同一期との記述は誤りの可能性がある。
- 注記 (直近 EPS の基準): TradingView News の 10-Q 要約*では Q1 FY27 の GAAP EPS は 1.56。non-GAAP の 1.92 とは基準が違う (原典 SEC 10-Q は Tier 1、未確認)。
- Q1 FY27 ガイダンス (2026-06-10 時点、Benzinga 要約*、Tier 3): EPS 1.72〜1.76、中点 1.74 (算出)。Zacks 事前コンセンサス 1.74 (既存行 43) と一致。
- Q2 FY27 決算日 2026-12-09、EPS ガイダンス 1.85〜1.93 (TradingView 分析の要約*、Tier 3-4)。既存行 35 の中点 1.89 (算出) と一致。

### 2-3 通期・ガイダンス (TradingView 掲載、報道経由)

| 項目 | 値 | 対象 | 時点 | 出典 | Tier |
|---|---|---|---|---|---|
| 売上 (trailing 実績) | 67.36B* | FY26 | 2026-09 以降と推定 | NYSE:ORCL 本体 (要約) | 3 (原典は Oracle 決算 = Tier 1) |
| 基本 EPS (trailing) | 6.47* | FY26 | 同上 | 同上 | 3 (基準不明、non-GAAP とは比較不可) |
| 純利益 (trailing) | 17.09B* | FY26 | 同上 | 同上 | 3 |
| 売上ガイダンス | 90.0B 以上* | FY27 | 2026-09-10 (原典 Oracle Q1 FY27 報道; 既存行 34 と一致) | TradingView News (GuruFocus / Zacks 要約) | 1 (原典) / 3 (経由) |
| non-GAAP EPS ガイダンス | 8.10* | FY27 | 2026-09-10 (既存行 32 と一致) | TradingView News (要約) | 1 (原典) / 3 (経由) |
| 設備投資 (capex) | 総額 90〜95B*、純現金 capex 70B 以下* | FY27 | 2026-09 の Q1 コール で再確認 | TradingView News (Zacks 要約) | 1 (原典) / 3 (経由) |
| 残存履行義務 (RPO) | 664B* | 時点 欠損 | 不明 (要約の参照表記 6-5 / 6-6 は解釈不能) | TradingView News (Zacks 要約) | 3 |
| FY27 OCI 売上 (Piper Sandler 推計) | 41.1B* | FY27 | 不明 | TradingView News (GuruFocus 要約) | 3 |

FY27 EPS コンセンサス (TradingView 経由):

| 値 | 出典 | 時点 | Tier |
|---|---|---|---|
| 8.13* (増加率 +6.55%*) | Zacks コンセンサス (TradingView News 要約) | 不明 | 3 |
| 8.11* | TradingView News 要約 (日付表記「6-15」は解釈不能) | 不明 | 3 |
| 8.04 → 8.13* (30 日で上方 3、下方 0) | TradingView 掲載の分析 (要約) | 不明 | 4 |

FY28・FY29 の年度別 EPS・売上 (TradingView): 欠損。詳細は第 5 節。

### 2-4 株価・補助情報

| 項目 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| 株価 (Mizuho 記事の時点) | 134.06 USD* | 不明 | TradingView News (要約) | 3 |
| 1 週 / 1 年の騰落 | -8%* / -57%* | 不明 | NYSE:ORCL 本体 (要約) | 3 |
| 株価 (参考、TradingView 外) | 123.38 USD* | 2026-07-24 | https://capital.com/en-ae/analysis/oracle-orcl-stock-forecast | 3 |
| 株価 (参考、TradingView 外) | 116.43 USD* | 不明 | https://www.marketbeat.com/stocks/NYSE/ORCL/price-target/ | 3 |
| 2026-10-15 時点の株価 | 欠損 | - | 検索対象外 | - |

注: 直近の株価は本調査で確定できていない。目標株価との比率は算出していない。

### 2-5 参考日程 (未確認)

- Oracle Analyst Day 2026-10-16 (TradingView のアイデア投稿で言及*、Tier 4、公式確認なし)。基準日の翌日にあたるため、要確認。
- Q2 FY27 決算 2026-12-09 (2-2 節参照)。

---

## 3. 既存 CSV (Yahoo / FactSet / tickflow / Simply Wall St / MarketScreener) との比較

### 3-1 FY27 EPS

| 出典 (CSV 行) | 値 | 人数 | 時点 | Tier | TradingView 8.13* との差 (算出) |
|---|---|---|---|---|---|
| Yahoo (行 2) | 8.06 | 42 | 不明 (90 日前 8.03) | 3 | +0.07 (+0.9%) |
| tickflow (行 4) | 7.98 | 23 | 不明 | 3 | +0.15 (+1.9%) |
| FactSet 中央値 (行 8) | 8.00 | 欠損 | 不明 (年度表記未確認) | 3 | +0.13 (+1.6%) |
| 既存 calc/model.py (行 31) | 8.05 | 25 | 不明 | 3 | +0.08 (+1.0%) |
| Oracle ガイダンス (行 32) | 8.10 | - | 2026-09-10 | 1 | +0.03 (+0.4%) |

- 算出: 8.13 - 8.06 = 0.07、0.07 / 8.06 = 0.9%。8.13 - 7.98 = 0.15、0.15 / 7.98 = 1.9%。8.13 - 8.00 = 0.13、0.13 / 8.00 = 1.6%。8.13 - 8.05 = 0.08、0.08 / 8.05 = 1.0%。8.13 - 8.10 = 0.03、0.03 / 8.10 = 0.4%。
- Simply Wall St と MarketScreener は FY27 EPS を CSV に持たないため、比較対象外。

### 3-2 FY27 売上

| 出典 (CSV 行) | 値 (USD B) | 人数 | 時点 | Tier |
|---|---|---|---|---|
| TradingView 掲載 | コンセンサス: 欠損 / ガイダンス 90.0 以上* | - | 2026-09-10 (ガイダンス) | 1 / 3 |
| Yahoo 9 月末 (行 48) | 90.48 | 38 | 2026-09-30 (推定) | 3 |
| Simply Wall St (行 51) | 89.3 | 42 | 2026-08-13 | 3 |
| MarketScreener A (行 59) | 89.32 | - | 不明 | 3 |
| MarketScreener B (行 60) | 90.48 | - | 不明 | 3 |
| FactSet 中央値 (行 70) | 85.1 | - | 不明 | 3 |

### 3-3 FY28 EPS

- TradingView 掲載値: 欠損 (年度予想の表は取得できず)。
- 既存 CSV の参考値: Yahoo 10.93 (行 3、40 名)、tickflow 10.78 (行 5、16 名)、FactSet 中央値 10.65 (行 9、38 名)。
- TradingView のユーザー投稿アイデア 15.19 (行 112、Tier 4) は既存行の再掲のみ。他値との差は 15.19 - 10.93 = 4.26 (算出、+39.0%)。

### 3-4 次期四半期 (Q2 FY27)

| 項目 | TradingView 本体 (要約*) | 比較対象 (CSV) | 差 (算出) |
|---|---|---|---|
| 次期 EPS | 1.89 | ガイダンス中点 1.89 (行 35、算出 (1.85+1.93)/2) | 0.00 |
| 次期 EPS | 1.89 | Benzinga 1.81 (行 40) | +0.08 (+4.4%) |
| 次期売上 | 21.31B | ガイダンス中点 21.20 (行 36、算出 (20.9+21.5)/2) | +0.11 (+0.5%) |
| 次期売上 | 21.31B | Benzinga 21.15 (行 41) | +0.16 (+0.8%) |
| 次期売上 | 21.31B | thecerbatgem 21.2 (行 39、決算前) | +0.11 (+0.5%) |

### 3-5 Q1 FY27 (実績)

| 項目 | TradingView 本体 (要約*) | CSV | 差 (算出) |
|---|---|---|---|
| EPS (non-GAAP) | 1.92 | 1.92 (行 44) | 0.00 |
| 売上 | 19.34B | 19.35B (行 46、Yahoo 19.34 の注記あり) | -0.01 (丸め・ソース差) |

### 3-6 目標株価

- 既存 CSV の目標株価は行 109 (BOATS 337.42、TradingView) と行 110 (Mizuho 320、二次・日付不明) のみ。Mizuho 320 は今回も要約で確認 (2-1 節の証券会社別表、日付不明)。
- TradingView 掲載の平均 (241.68〜337.42) との差: 337.42 - 241.68 = 95.74 (算出)、対 241.68 で +39.6% (算出)。
- CSV 外の参考: MarketBeat 265.03 (39 名、高 400、安 145*、時点不明)、TipRanks 248.82 (28 Buy / 5 Hold、直近 3 か月*)、AlphaSpread 191.22 と 286 (2 つの時点、要約*)。

---

## 4. 食い違い (併記)

1. 目標株価の平均: 241.68 (NYSE in 版、T-1) / 243.97 (TradingView 分析、T-2) / 256〜257 (TradingView News 集計、T-5) / 337.42 (BOATS、T-3)。最大差 95.74 (算出、+39.6%)。
   - 窓 (過去 3 か月か 1 年か) と掲載日の違いが疑われるが、時点は確定できず。既存行 109 の注記 (H2 は 34 名) とも人数が合わない。
2. 目標株価の安値: 110 (NYSE 本体・ar 版、T-4) / 155 (NYSE in 版、T-1 と T-5) / 175.14 (BOATS、T-3)。差は最大 65.14 (算出)。
3. 分析人数: 37 (T-1 の 1 年予想、T-5) / 45 (T-2、T-3) / 46 (T-1 の 3 か月)。同一ページ要約内でも 37 と 46 が併記されている。
4. 直近四半期 EPS の期: 2.11 (SIX、ar 版) と 1.92 (本体) が併存。2.11 は Q4 FY26 (Benzinga 要約*: 報告 2026-06-10、予想 1.89)。ar 版の予想 1.96 と Benzinga の 1.89 も食い違う (期の対応、時点差は未確認)。
5. 直近 EPS の基準: 非 GAAP 1.92 (本体) と GAAP 1.56 (10-Q 要約*) が併存。比較時は基準を揃える必要あり。
6. in 版の直近 EPS 1.79 (予想 1.70) と次期 1.95: どの四半期か不明。1.79 はどの既知の FY27 四半期実績にも対応しない。
7. 次期 EPS: 本体 1.89 (ガイダンス中点と一致) / SIX 1.73 と ar 1.74 (Q1 FY27 の決算前コンセンサスと一致) / in 版 1.95。
8. 次期売上: 本体 21.31B vs ガイダンス中点 21.20 (算出) vs Benzinga 21.15 vs thecerbatgem 21.2。最大差 0.16 (算出、+0.8%)。
9. FY27 EPS コンセンサス: 8.13* (Zacks) / 8.11* (TradingView News) / 8.04→8.13* (分析) / 8.06 (Yahoo) / 8.05 (model.py) / 8.00 (FactSet) / 7.98 (tickflow)。範囲は 0.15 (算出)。
10. Benzinga の FY27 四半期コンセンサス (Q1 1.67、Q2 1.81、Q3 1.65、Q4 1.92、2026-06 時点*) の合計は 7.05 (算出)。FY27 の 8.05〜8.13 とは約 1.0 の差。Q1 の 1.67 (Benzinga) と 1.74 (Zacks 事前コンセンサス、既存行 43) は出典・時点が別。時点差の影響が大きいと考えられるが、未確認。
11. 基本 EPS 6.47 (本体の trailing 値*) は、既存行 14 の Barchart FY27 GAAP 系 6.47 と同値。trailing と forward は別物のため混同しないこと。
12. FY26 売上: 67.36B (本体の trailing*) / 67.4 (TradingView News 本文*) / 67.3 (S&P 経由 Visible Alpha の事前コンセンサス、既存行 74)。実績と事前コンセンサスの違いで、実質一致。
13. Q1 FY27 売上: 19.34B (本体*) / 19.35B (既存行 46)。0.01 差 (算出)、丸めかソース差。
14. Mizuho 目標 320 は既存行 110 と同値。TradingView News の要約*では「最新の引き下げ・据え置き」の文脈で、日付は不明のまま。

---

## 5. 欠損と検索語

| 項目 | 状況 | 試した検索語 (WebSearch、計 12 回) |
|---|---|---|
| TradingView の FY28 EPS (年度別予想表) | 欠損 | "tradingview Oracle EPS estimate 2028"; "tradingview ORCL estimates EPS revenue FY2028 forecast"; "NYSE-ORCL financials tradingview income statement forecast EPS 2028 revenue estimate" |
| TradingView の FY29 EPS・売上 | 欠損 | "tradingview NYSE-ORCL financials revenue forecast fiscal 2027 2028 2029" (domain 限定) |
| TradingView の FY27 売上コンセンサス | 欠損 (ガイダンス 90.0 のみ) | "tradingview ORCL revenue forecast next fiscal year" |
| TradingView 財務ページ (financials-earnings) の年度表 | 本文未取得 (URL は検索に出たのみ: https://www.tradingview.com/symbols/NYSE-ORCL/financials-earnings/) | "tradingview NYSE-ORCL financials earnings forecast EPS annual"; "Oracle Corporation Earnings and Revenue NYSE-ORCL annual EPS forecast next fiscal year tradingview" |
| 掲載ページの日付 (全般) | 欠損 (要約に日付なし) | "ORCL price target TradingView forecast analysts October 2026 update" |
| ar.NYSE-ORCL 版の平均目標 | 欠損 (要約は安値 110 と高値 400 のみ) | "tradingview NYSE:ORCL forecast"; "tradingview NYSE-ORCL forecast-price-target analysts average target" |
| 2026-10-15 時点の株価 | 欠損 (対象外として未検索) | - |
| FY27 EPS の年度単位の TradingView 表 | 欠損 | "ORCL Forecast Prediction for 2027 TradingView EPS forecast annual analysts" (domain 限定) |

- 検索結果の多くは TradingView の別上場 (VIE、BMV、BOATS、SIX、EUROTLX、MIL、Chile 等) で、NYSE-ORCL の年度表には到達できなかった。
- 欠損の扱い: 推測で埋めていない。FY28・FY29 の TradingView 値は既存 CSV の値 (行 112-113 のユーザー投稿を除く) とも突き合わせていない。

---

## 6. 出典一覧

Tier 3 = データ会社・報道 / Tier 4 = 個人投稿・ブログ / Tier 1 = 会社開示 (報道経由含む)。すべて検索要約経由 (`*`)。

TradingView (掲載ページ):
- https://in.tradingview.com/symbols/NYSE-ORCL/forecast/ (Tier 3、T-1、2-2 in 版)
- https://in.tradingview.com/symbols/BOATS-ORCL/forecast (Tier 3、T-3)
- https://ar.tradingview.com/symbols/NYSE-ORCL/forecast-price-target/ (Tier 3、T-4、既存行 111)
- https://www.tradingview.com/symbols/NYSE-ORCL/ (Tier 3、本体の四半期・trailing 値)
- https://www.tradingview.com/symbols/SIX-ORCL/ (Tier 3、SIX 行)
- https://www.tradingview.com/symbols/NYSE-ORCL/financials-earnings/ (Tier 3、本文未取得)
- https://www.tradingview.com/symbols/NYSE-ORCL/ideas/ (Tier 4、Analyst Day の言及元の一覧、個別未特定)
- https://www.tradingview.com/chart/ORCL/REAlVjRK-Oracle-Corporation-ORCL-Long-at-172-42/ (Tier 4、ユーザー投稿、既存行 112-113 と同系)

TradingView News (報道・要約):
- https://www.tradingview.com/news/tradingview:5be25c63a34a3:0-oracle-corp-q1-2027-revenue-19-35b-eps-1-56-10-q-summary/ (Tier 3、10-Q 要約、GAAP EPS 1.56)
- https://www.tradingview.com/news/zacks:cc275742c094b:0-oracle-q1-earnings-call-centers-on-ai-capacity-and-raised-outlook/ (Tier 3、Q1 コール)
- https://www.tradingview.com/news/gurufocus:824cdbbbc094b:0-oracle-cloud-revenue-could-beat-fiscal-2027-estimates/ (Tier 3、FY27 ガイダンス)
- https://www.tradingview.com/news/zacks:dab22189f094b:0-will-rising-capex-weigh-on-oracle-s-free-cash-flow-outlook/ (Tier 3、capex)
- https://www.tradingview.com/news/tradingview:f44ae96698d46:0-orcl-q4-25-earnings-eps-estimate-is-1-96-usd/ (Tier 3、EPS 予想 1.96 の見出し。期の対応は未確認)
- https://www.tradingview.com/news/stocktwits:99cd4c45b094b:0-orcl-stock-on-track-to-erase-pre-earnings-losses-barclays-says-growth-has-inflected/ (Tier 3、Barclays 関連)
- https://www.tradingview.com/news/gurufocus:af7978b7d094b:0-piper-sandler-issues-a-blunt-message-for-oracle-stock-fans/ (Tier 3、Piper Sandler)
- https://www.tradingview.com/news/tradingview:0442c0b43d805:0-oracle-corporation-stock-12-month-price-target-raised-to-257-24-implies-40-upside/ (Tier 3、見出しのみ)
- https://www.tradingview.com/news/tradingview:05f813bece447:0-oracle-corporation-stock-12-month-price-target-raised-to-256-45-implies-27-upside/ (Tier 3、見出しのみ)
- 個別 URL 未特定: UBS / Wedbush / Stifel / Mizuho の目標株価、Zacks FY27 8.13、TradingView 集計 256〜257 (37 名)、RPO 664B、FY27 capex (TradingView News 要約、Tier 3)

非 TradingView (参考、CSV 外):
- https://www.marketbeat.com/stocks/NYSE/ORCL/price-target/ (Tier 3、265.03 / 39 名 / 高 400 / 安 145 / 株価 116.43*、時点不明)
- https://alphaspread.com/security/nyse/orcl/analyst-estimates (Tier 3、191.22 と 286 の 2 時点*)
- https://www.tipranks.com/news/uncategorized/oracle-stock-price-forecast-2026-what-financial-analysts-expect-right-now (Tier 3、248.82*)
- https://capital.com/en-ae/analysis/oracle-orcl-stock-forecast (Tier 3、株価 123.38 (2026-07-24)*)
- https://www.benzinga.com/quote/ORCL/earnings-forecasts (Tier 3、Q4 FY26 結果 2.11 / 予想 1.89、Q1 FY27 ガイダンス 1.72〜1.76、FY27 四半期コンセンサス*)
- https://www.sec.gov/Archives/edgar/data/0001341439/000119312526265848/orcl-ex99_1.htm (Tier 1、Oracle 8-K FY2026 の検索結果に出たのみ。本文未確認)
