# Applied Digital Corporation (NASDAQ: APLD) データ収集表

- 作成日: 2026-10-11
- 決算期末: 5月31日 (FY2026 = 2025-06-01〜2026-05-31 / FY2027 Q1 = 2026-06-01〜2026-08-31)
- 取得方法: WebSearch のみ (合計33回)。WebFetch / curl は未使用。本文は閲覧しておらず、数値は検索結果の抜粋に基づく。
- 判断・評価は含めていない。

## 凡例
- **欠損**: 検索で取得できず。推測での補完はしていない。
- **(算出: 式)**: 取得値からの計算値。
- **(二次情報)**: 企業の一次開示 (8-K / 10-Q / 10-K) ではない記事・集計サイトの値。
- **(候補URL)**: 出所URLが検索結果上の候補で、該当数値の記載は未確認。
- 損失は負値 (−) で表記。単位 $M = 百万米ドル。株式数は百万株または株で明記。

## 注記 (基準の混在・矛盾の記録)
1. **基準の混在**: クラウド事業 (ChronoScale 等) を継続事業外として扱う再表示が入っているため、FY2024〜FY2025 Q3 の原報告値 (クラウド含む) と、FY2025 Q4 以降・FY2026 の再表示値 (継続事業ベース) が混在する。前年比の基準も四半期ごとに一致しない (例: FY2025 Q4 の前年比は FY2024 Q4 原報告 43.7 ではなく 26.9 を基準)。
2. **合計の不整合**: FY2026 四半期売上の合計 (64.2 + 126.6 + 126.6 + 258.7 = 576.1) は通期 611.3 (リリース) と一致しない。FY2026 四半期純損失の合計 (27.8 + 31.2 + 100.9 + 110.6 = 270.5) は通期 249.2 と一致しない。FY2025 四半期売上の合計 (60.7 + 63.9 + 52.9 + 38.0 = 215.5) は再表示の通期 144.2 と一致しない。
3. **FY2026 Q2 と Q3 の総売上がともに $126.6M**。両方とも検索結果の記載どおり。要確認。
4. **FY2025 通期純損失**: 二次情報で 161 / 前年比 +118% とあるが、前年 FY2024 通期 −149.7 との比較では +118% にならない。不整合のため通期値は参考扱い。
5. **決算発表日**: FY2027 Q1 は 2026-10-07 大引け後 (8-K 日付)。Investing.com の「2026-10-14」表記は不採用。
6. 「2024年Q1〜」は会計年度 (FY2024 Q1 = 2023-08-31 期) として扱った。暦年ベースの場合は別途対応が必要。
7. 2025年12月の下落 (−12.35%, $24.42) は2025年のため表9の対象外。

---

## 表1 基本情報

| 項目 | 値 | 時点 | 出所 |
|---|---|---|---|
| 法人設立州 (本籍) | ネバダ州 (Nevada) | 2026-05-31 (FY2026 10-K 表紙) | https://www.sec.gov/Archives/edgar/data/0001144879/000114487926000048/apld-20260531.htm |
| 本社所在地 | 3811 Turtle Creek Boulevard, Suite 2100, Dallas, Texas 75219 (米国) | 2026-05-31 (10-K 表紙) | 同上 |
| 上場市場 | NASDAQ (ティッカー APLD)。上場区分 (Global Select 等) は欠損 | 2026-10-05 (Google Finance 表示) | https://www.google.com/finance/quote/APLD:NASDAQ?hl=en |
| 決算期末 | 5月31日 (FY2026 は 2026-05-31 期末) | 2026-05-31 | https://www.sec.gov/Archives/edgar/data/0001144879/000114487926000044/apldq426earningsreleaseasf.htm |
| 直近終値 | $23.81 (2026-10-07 終値、前日比 −6.04%)。2026-10-08 / 10-09 の終値は欠損 | 2026-10-07 | 二次情報 (記事URL未特定) |
| 時間外 (参考) | 2026-10-07 時間外 $24.04 (+0.96%) (二次情報) | 2026-10-07 | 二次情報 (記事URL未特定) |
| 時価総額 | 約 $6.94B (算出: 発行済株式数 291,469,112 × 終値 $23.81) | 2026-10-07 | 算出 (株式数: 10-K URL / 終値: 二次情報) |
| 時価総額 (参考・二次) | $8.31B (2026-08-19 終値 $28.23 時点の集計値) | 2026-08-19 | https://equibles.com/stocks/APLD (候補URL) |
| 発行済株式数 (直近10-Q表紙) | 欠損 (最新確認済み10-Qは 2026-02-28 期、2026-04-08 提出。表紙値は未取得) | 2026-02-28 | https://www.sec.gov/Archives/edgar/data/1144879/000114487926000030/apld-20260228.htm (候補URL) |
| 発行済株式数 (代替: 10-K 表紙) | 291,469,112 株 | 2026-07-28 | https://www.sec.gov/Archives/edgar/data/0001144879/000114487926000048/apld-20260531.htm |
| 発行済株式数 (参考・未検証) | 285,769,539 (集計サイト、基準日不明) / 約2.82億 (2026-02-28 期末、Macrotrends) / 279,585,823 (Form 144、2026-01) | 各時点 | https://www.macrotrends.net/stocks/charts/APLD/applied-digital/shares-outstanding |
| 希薄化後株式数 | 欠損 | — | — |
| 52週高値 | 約 $50.70〜50.73 (日中高値。2026-08 時点の集計値。発生日は欠損) | 2026-08 時点 | https://www.investing.com/equities/applied-blockchain (候補URL) |
| 52週安値 | 欠損 (ソース間で不一致: $9.02 (日付不明) / $12.35 (2026-08-02 時点) / $13.17 (2026-08-10 時点)。2026-10-09 時点は未確定) | — | https://equibles.com/stocks/APLD (候補URL) |
| ワラント (CoreWeave) | 8,393,611 株 / 行使価格 $10.75 (2025-08-28 発行。PF1 Building 4 リース締結に伴う。その後 Jane Street Global Trading, LLC へ譲渡) | 2025-08-28 | https://www.sec.gov/Archives/edgar/data/1144879/000149315225012458/form8-k.htm (候補URL) |
| ワラント (Macquarie 系投資家) | 2,400,000 株 / 行使価格 $8.29 (PF1 資金 $450M 拠出で行使可能化) | 2025-10-06 | https://www.sec.gov/Archives/edgar/data/1144879/000149315225020389/forms-3asr.htm (候補URL) |
| ワラント (Google 等) | 未発見 (検索結果に Google 宛ワラントの記載なし) | — | — |
| ATM (随時増資) 枠 | 最新確認分: $200M (2025-06-02 登録。Northland / Wells Fargo が販売代理) | 2025-06-02 | https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001641172-25-013328/forms-3asr.htm |
| ATM 使用額 | 欠損 | — | — |
| ATM (2026 年の新規枠) | 未発見 (欠損) | — | — |
| 参考: 過去の ATM | 2023 Craig-Hallum $125M / 2024-05 Roth $25M / 2024-07 5社 $125M。手数料 3.0% | 各時点 | https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001144879-23-000166/apld-preliminaryprospectus.htm 、https://www.sec.gov/Archives/edgar/data/0001144879/000114487924000106/apld-20240506.htm 、https://www.sec.gov/Archives/edgar/data/1144879/000114487924000186/apld-20240709.htm (いずれも候補URL) |

---

## 表2 四半期業績 (会計年度ベース、FY2024 Q1 〜 FY2027 Q1 (最新))

| 四半期 (期末日) | 総売上 | うちHPC/AIリース・コロケーション売上 | うちビットコイン採掘売上 | その他 | 売上総利益または売上原価 | 営業損益 | 純損益(GAAP) | 希薄化後EPS | 調整後EBITDA(会社定義) | 希薄化後株式数(加重平均・百万株) | 出所 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2024 Q1 (2023-08-31) | 36.3 | 欠損 | 欠損 | 欠損 | 売上原価 24.4 | 欠損 (営業費用 17.1) | −11.9 (SEC 原リリース。別集計 −9.6 は不採用) | −0.12 | +10.0 | 100.5 | https://www.sec.gov/Archives/edgar/data/1144879/000189884423000007/apld1q24earningsrelease.htm |
| FY2024 Q2 (2023-11-30) | 42.2 | 欠損 | 欠損 | 欠損 | 売上原価 29.2 | 欠損 | −10.5 | 欠損 (調整後 −0.05) | +10.6 | 欠損 | https://www.stocktitan.net/news/APLD/applied-digital-reports-fiscal-second-quarter-2024-xoys2085jsmb.html (候補URL) / https://www.sec.gov/Archives/edgar/data/1144879/000114487924000004/apld2q24earningsrelease.htm (候補URL) |
| FY2024 Q3 (2024-02-29) | 43.3 (原報告。後の再表示で 40.3) | 欠損 | 欠損 | 欠損 | 欠損 (増加のみ記載) | 欠損 | −62.8 (二次情報。別集計 −100.9 / 売上 126.6 は不整合) | 欠損 | −2.3 | 欠損 | https://www.sec.gov/Archives/edgar/data/1144879/000114487924000077/apld3q24earningsrelease.htm |
| FY2024 Q4 (2024-05-31) | 43.7 (原報告。FY2025 Q4 比較では 26.9 に再表示) | 欠損 | 欠損 | 欠損 | 売上原価 46.3 | 欠損 | −64.8 | 欠損 | +4.8 | 欠損 | https://www.sec.gov/Archives/edgar/data/1144879/000114487924000210/apldq424earningsrelease.htm |
| FY2025 Q1 (2024-08-31) | 60.7 | 欠損 | 欠損 | クラウド 25.9 / DCH 34.8 | 売上原価 61.1 | 欠損 | −4.2 | −0.03 | +20.0 | 欠損 | https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001144879-24-000251/apldq125earningsrelease.htm |
| FY2025 Q2 (2024-11-30) | 63.9 | 欠損 | 欠損 | クラウド 27.7 / DCH 36.2 | 売上原価 52.4 | 欠損 | −138.7 (うちデット公正価値変動損 −87.2、転換損 −25.4) | −0.66 | +21.4 | 210.2 (算出: 138.7 ÷ 0.66) | https://www.sec.gov/Archives/edgar/data/1144879/000114487925000005/apldq225earningsrelease.htm |
| FY2025 Q3 (2025-02-28) | 52.9 | 欠損 | 欠損 | クラウド 17.8 / DCH 35.2 | 売上原価 49.1 | 欠損 | −36.1 | −0.16 | +10.0 | 225.6 (算出: 36.1 ÷ 0.16) | https://www.sec.gov/Archives/edgar/data/1144879/000162828025017683/apldq325earningsrelease.htm |
| FY2025 Q4 (2025-05-31) | 38.0 (継続事業ベース) | 欠損 | 欠損 | 欠損 | 欠損 (SG&A 28.1) | 欠損 | −26.6 | −0.12 | ≈ +1 (二次・概数) | 221.7 (算出: 26.6 ÷ 0.12) | https://www.sec.gov/Archives/edgar/data/1144879/000114487925000019/apldq425earningsrelease.htm |
| FY2026 Q1 (2025-08-31) | 64.2 (継続事業ベース。前年比 +84% は前年 34.8) | 欠損 (うちテナント fit-out 26.3) | 欠損 | 欠損 | 売上原価 55.6 | 欠損 | −27.8 | −0.11 | +0.5 (別集計 5.0 / 0.537 は不採用) | 252.7 (算出: 27.8 ÷ 0.11) | https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001144879-25-000068/apldq126earningsrelease.htm |
| FY2026 Q2 (2025-11-30) | 126.6 (前年比 +250%) | 85.0 (うち fit-out 約73 / 賃料 約12) | 欠損 | DCH 41.6 | 売上原価 100.6 | 欠損 | −31.2 | −0.11 | +20.2 | 283.6 (算出: 31.2 ÷ 0.11、丸め誤差大) | https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001144879-26-000002/apldq226earningsrelease.htm |
| FY2026 Q3 (2026-02-28) | 126.6 (HPC 71.0 + DCH 37.5 + クラウド 18.1 の合算。前年比 +139%) | 71.0 | 欠損 | DCH 37.5 / クラウド 18.1 | 欠損 | HPC セグメント 17.6 / DCH 13.9 / クラウド −52.2 (減損 −59.7 含む)。連結計は欠損 | −100.9 (プレスリリース。二次要約の transcript では EPS −0.60 と記載あり) | −0.36 (二次要約 −0.60) | +44.1 (前年 6.26) | 280.3 (算出: 100.9 ÷ 0.36) | https://www.sec.gov/Archives/edgar/data/1144879/000114487926000029/apldq326earningsrelease.htm |
| FY2026 Q4 (2026-05-31) | 258.7 (前年比 +407%。調整後売上 240.4) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 (非GAAP の Net operating income 39.9) | −110.6 (別集計 −111.6) | −0.39 | +42.4 | 283.6 (算出: 110.6 ÷ 0.39) | https://www.sec.gov/Archives/edgar/data/0001144879/000114487926000044/apldq426earningsreleaseasf.htm |
| FY2027 Q1 (2026-08-31) | 341.9 (前年比 +322%。サービス収入 262.8 / データセンター賃貸他 79.1 / 調整後売上 300.4) | 欠損 (HPC セグメント営業利益 33.4 のみ) | 欠損 | 欠損 | 欠損 | 欠損 (非GAAP の Net Operating Income 58.8) | −221.0 (継続事業帰属。8-K 記載の二次要約。別集計 −237.1 / 純損失 −184.1 は不採用) | −0.76 (別集計 −0.82) | +64.4 (前年 0.5) | 290.8 (算出: 221.0 ÷ 0.76) | https://www.sec.gov/Archives/edgar/data/0001144879/000114487926000057/apldq127earningsrelease.htm |

**通期参考 (表2 下の補足)**
- FY2024 通期 (2024-05-31): 売上 165.6 (DCH 136.6 / クラウド 29.0) / 純損失 −149.7 (二次の見出し −149.3 と不一致) / EPS −1.31 / 調整後EBITDA 24.5。出所: https://www.sec.gov/Archives/edgar/data/1144879/000114487924000210/apldq424earningsrelease.htm
- FY2025 通期 (再表示): 売上 144.2 (+6%) / 純損失 −161 (二次。前年比 +118% は前年 −149.7 と不整合) 。出所: https://www.stocktitan.net/news/APLD/applied-digital-reports-fiscal-fourth-quarter-and-full-year-2024-m3sewu4lbl8a.html (候補URL) / 二次情報
- FY2026 通期 (2026-05-31): 売上 611.3 (+167%) / 純損失 −249.2 (帰属) / 調整後EBITDA 107.2 (二次) / 調整後純利益 36.1 (二次)。出所: https://www.sec.gov/Archives/edgar/data/0001144879/000114487926000044/apldq426earningsreleaseasf.htm
- FY2026 Q4 補足: 調整後純利益 +12.9、調整後EPS +0.04 (非GAAP)。出所: 同上

---

## 表3 キャッシュフロー・資本支出 (四半期または年度)

| 期間 | 営業CF | 設備投資(capex) | 株式報酬(SBC) | 株式発行による調達 | 借入による調達 | 期末現預金 | 出所 |
|---|---|---|---|---|---|---|---|
| FY2025 Q1 (2024-08-31) | 欠損 | 欠損 | 欠損 | 私募 $160M (NVIDIA を含む。2024-09-09 完了、四半期後の完了) | 欠損 | 現金+制限付 $86.6M / 総負債 $143.6M | https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001144879-24-000251/apldq125earningsrelease.htm |
| FY2025 Q2 (2024-11-30) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 現金+制限付 $314.6M / 総負債 $479.6M | https://www.sec.gov/Archives/edgar/data/1144879/000114487925000005/apldq225earningsrelease.htm |
| FY2026 Q1 (2025-08-31) | 欠損 | 欠損 | 16.6 (Q1 SG&A 内の株式報酬の増加分として記載) | 欠損 (期末後に Macquarie 優先株 $112.5M 引出し) | 欠損 | 現金 $114.1M / 総負債 $687.3M (期末後調達 $362.5M は除く) | https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001144879-25-000068/apldq126earningsrelease.htm |
| FY2026 Q1 (参考) | FCF −331.4 (二次情報。定義不明) | — | — | — | — | — | https://www.tipranks.com/stocks/apld/financials/cash-flow |
| FY2026 Q2 (2025-11-30) | 欠損 | 欠損 | 欠損 | Macquarie 優先株 $562.5M 引出し (二次) | 2.35B シニア担保付社債 (二次。総負債 約 2.6B) | 現金+制限付 約 $2.3B (二次) | https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001144879-26-000002/apldq226earningsrelease.htm |
| FY2026 Q3 (2026-02-28) | FCF −720.2 (二次情報。記事内で「第1四半期」と表記) | 欠損 | 欠損 | 欠損 | 欠損 (総負債 約 2.7B、二次) | 現金 約 $2.1B (二次) | https://stocks.observer-reporter.com/observerreporter/article/stockstory-2026-4-14-why-applied-digital-apld-stock-is-up-today |
| FY2026 通期 (2026-05-31) | 欠損 (候補値: +89.7 (Investing 二次) / −36.0 (TTM 2026-02, Chartmill 二次) / −115.4 (FY2025 の可能性)。採用不可) | 欠損 (候補値: −198.3 (VCP TTM、時点不明) / −1,770 (TTM 2026-02、Chartmill)。採用不可) | 欠損 (候補値: 107.2 (VCP TTM)。採用不可) | 欠損 | 欠損 (Bridge 残高 $300M、表4 参照) | 無制限 $1.6B + 制限付 $2.6B = 4.2 (算出) | https://www.sec.gov/Archives/edgar/data/0001144879/000114487926000048/apld-20260531.htm |
| FY2027 Q1 (2026-08-31) | 欠損 | 約 −2,070 (二次: 約 $2.07B、同四半期) | 欠損 | 欠損 | 1,590 (7.000% 2031 年債、PF1 の建物向け。二次) | 欠損 | 総負債 $6.4B (二次): https://moneycheck.com/?p=187218 / capex: https://247wallst.com/cards/applied-digital-q1-2027-earnings-apld-01m4c1yz8n3e757hmdzsq1qbv1 |

---

## 表4 負債の明細 (直近期末: 2026-05-31 を基本。最新 2026-08-31 の明細は未取得、総額 $6.4B のみ二次情報)

| 証券・借入 | 元本 | 金利 | 満期 | 担保・リコース | 転換価格(転換社債) | 出所 |
|---|---|---|---|---|---|---|
| 2.75% 転換社債 (Convertible Senior Notes) | 450 (2026-05-31 残高。10-K 二次データ。$375M 基本額 + $75M 追加オプション全額行使と推定、要確認) | 2.75% | 2030-06-01 | 欠損 | 約 $9.75 (102.5431 株 / $1,000 元本)。キャップドコール上限 $14.72 | https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001493152-24-043119/0001493152-24-043119.pdf (候補URL) / https://www.sec.gov/Archives/edgar/data/1144879/000149315224043604/form8-k.htm (候補URL) |
| シニア担保付社債 (APLD ComputeCo LLC) | 2,350 (発行意向の表記。最終価格は未確認) | 欠損 (9.25% は未確認) | 2030 (表題より) | シニア担保付 (表題より)。他は欠損 | — | https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001493152-25-021400/0001493152-25-021400.pdf (候補URL) |
| シニア担保付社債 (APLD ComputeCo 2 / PF2) | 2,150 | 6.750% | 2031 | シニア担保付。発行価格 98% | — | https://ir.applieddigital.com/news-events/press-releases/detail/146 |
| シニア担保付社債 (PF1 の建物向け) | 1,590 | 7.000% | 2031 | 欠損 (建物向けと記載。発行時期・「第3棟」「第4棟」表記は不一致) | — | https://www.barchart.com/story/news/2388252/applied-digital-announces-pricing-of-1-59-billion-of-senior-secured-notes-to-fund-the-fourth-building-at-polaris-forge-1 |
| ブリッジ (借入) | 300 (2026-05-31 残高。10-K 二次データ) | 欠損 | 欠損 | 欠損 | — | https://www.sec.gov/Archives/edgar/data/0001144879/000114487926000048/apld-20260531.htm |
| Macquarie 優先株式 (債務ではない・参考) | 引出し累計 約 1,010 (算出: 112.5 + 562.5 + 337.5)。枠 $5B | 欠損 | 永久 (perpetual) | 欠損 | — | https://www.nasdaq.com/press-release/applied-digital-reports-fiscal-second-quarter-2026-results-2026-01-07 (候補URL) |
| Macquarie Equipment Capital 開発ローン (参考) | 初期 100 | 欠損 | 欠損 | 欠損 | — | 上記と同じ (候補URL) |
| 信用枠 (Revolver) | 欠損 (見出しでは $350M、URL 上は $550M の表記で不一致) | 欠損 | 欠損 | 欠損 | — | https://www.theenergymag.com/news/market-news/applied-digital-finalizes-550-million-credit-facility-for-ai-data-center-growth (候補URL) |
| 総負債 (参考) | 2026-08-31: 約 6,400 (二次) / 2026-02-28: 約 2,700 (二次) / 2025-11-30: 約 2,600 (二次) / 2025-08-31: 687.3 | — | — | — | — | https://moneycheck.com/?p=187218 (候補URL) |

---

## 表5 AI/HPC の容量と契約 (KPI時系列)

### 5-A. KPI 時系列 (直近6四半期と現在)

| 時点 | 稼働中(エネルギー供給済み)IT容量 MW | 建設中 MW | 契約済み MW | 契約済み収益総額 | 主要テナント | 年換算契約収益 | 電力の確保量(総MW) | 出所 |
|---|---|---|---|---|---|---|---|---|
| 2025-08-31 (FY26 Q1) | 欠損 | 欠損 | 欠損 (PF1 は 150MW 追加契約後に満室と記載) | 約 $11B (CoreWeave PF1 の見込み契約収益総額。二次要約) | CoreWeave | 欠損 | 欠損 | https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001144879-25-000068/apldq126earningsrelease.htm |
| 2025-11-30 (FY26 Q2) | 欠損 (DCH の旧数値: Jamestown 106 / Ellendale 180。2025-02 時点の記載、最新未確認) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | https://www.sec.gov/Archives/edgar/data/1144879/000162828025017683/apldq325earningsrelease.htm (候補URL) |
| 2026-02-28 (FY26 Q3) | 100 (第1 HPC 棟 フル四半期稼働と記載。二次) | 欠損 | 欠損 | 欠損 | CoreWeave (他は欠損) | 約 176.4 (算出: 基本賃料 44.1 × 4、参考値) | 欠損 | https://www.sec.gov/Archives/edgar/data/1144879/000114487926000029/apldq326earningsrelease.htm |
| 2026-05-31 (FY26 Q4 / 10-K) | PF1 250 (第2 フェーズ 75MW 追加で累計 250MW。二次情報、時点は 2026 年夏頃と推定) | 約 PF1 150 (第3棟、2027 RFS) / PF2 200 (初期、2026-2027 立上げ) | 約 1,200 (2026-05 発表の4キャンパス合計) | 約 $36B (初期基本契約期間ベース、Q4 FY26 call 時点) | CoreWeave (PF1)、投資適格ハイパースケーラー (匿名、PF2/PF3/DF2) | 約 2.4 ($B、算出: 36 ÷ 15年、全リースの期間15年と仮定した単純換算) | 欠損 | https://www.nasdaq.com/articles/applied-digital-q4-earnings-call-highlights (候補URL) |
| 2026-06 以降 (DF2 締結後) | 欠損 | 欠損 | 1,410 (Q4 FY26 call 記載の 1.41GW。内訳合計 400+200+300+300+210 = 1,410 (算出)) | 約 $36B | 同上 | 同上 | 欠損 | https://www.nasdaq.com/articles/applied-digital-q4-earnings-call-highlights (候補URL) |
| 2026-08-31 (FY27 Q1) | 欠損 | 欠損 | 1,410 (二次) | 約 $36B (二次) | 同上 | 同上 | 欠損 | https://www.sec.gov/Archives/edgar/data/0001144879/000114487926000057/apldq127earningsrelease.htm |

### 5-B. 各リース契約ごとの行

| 契約名 / 拠点 | テナント | MW | 期間 | 契約総額 | 稼働開始時期 | 信用補完 | 建設費 (1MWあたり) | 出所 |
|---|---|---|---|---|---|---|---|---|
| CoreWeave リース群 / PF1 Ellendale ND (PF1 合計 400 MW) | CoreWeave | 400 (うち稼働 250。第3棟 150 は建設中) | 約15年 (二次) | 約 $11B (二次) | 稼働 250 MW 済 / 第3棟 2027 RFS | 既存リース: CoreWeave Inc. の springing guarantee、$50M 信用状 (8-K 二次要約) | 欠損 | https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001144879-25-000068/apldq126earningsrelease.htm / https://www.stocktitan.net/sec-filings/APLD/8-k-applied-digital-corporation-reports-material-event-a3dfa078a6f7.html (候補URL) |
| PF2 リース / Harwood ND | 投資適格ハイパースケーラー (匿名) | 200 (初期) | 約15年 (二次) | 約 $5B (2025-10-22 発表、二次) | 2026 年に初期稼働、2027 年に全容量 (二次) | 欠損 | 算出候補: PF2 キャンパス費用 約 $3B (二次) ÷ 200 MW = 約 $15M/MW (280MW 前提なら約 $10.7M/MW。二次の表記が不一致) | https://finviz.com/news/200016/applied-digital-announces-5-billion-ai-factory-lease-with-us-based-investment-grade-hyperscaler-at-polaris-forge-2-nd-campus |
| PF3 リース (2026年5月頃の発表、二次) | 投資適格ハイパースケーラー (匿名) | 300 | 15年 (二次) | 約 $7.5B (二次) | 2027-08 (二次) | 欠損 | 欠損 | https://theenergymag.com/news/market-news/applied-digital-inks-7-5-billion-lease-for-300-mw-at-polaris-forge-3-expanding-ai-factory-footprint |
| Delta Forge 1 (430MW キャンパス、重要IT負荷上限 300MW) | 欠損 (匿名の投資適格ハイパースケーラーと記載の可能性。未確認) | 300 (重要IT) | 欠損 | 欠損 | 2027 年中盤 (二次) | 欠損 | 欠損 | https://www.nasdaq.com/articles/applied-digital-q4-earnings-call-highlights (候補URL) |
| Delta Forge 2 (2026-06 締結) | 投資適格 tier-one ハイパースケーラー (二次) | 210 | 15年 (二次) | 欠損 (算出参考: 全体 36 − 11 − 5 − 7.5 = 12.5、DF1 と DF2 の合計。内訳は未確認) | 欠損 | 欠損 | 欠損 | 出所URL未特定 (検索結果の要約。候補: https://www.nasdaq.com/articles/applied-digital-q4-earnings-call-highlights) |
| PF2 拡張交渉 (参考) | 既存の投資適格顧客2社 | 約 250 (うち PF2 100 を含む) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | https://www.nasdaq.com/articles/applied-digital-q4-earnings-call-highlights (候補URL) |

---

## 表6 ビットコイン採掘 KPI (直近6四半期)

| 四半期 | 採掘BTC数 | ハッシュレート(EH/s) | 1BTCあたり電力コスト | 出所 |
|---|---|---|---|---|
| FY2025 Q4 (2025-05-31) | 欠損 | 欠損 | 欠損 | — |
| FY2026 Q1 (2025-08-31) | 欠損 | 欠損 | 欠損 | — |
| FY2026 Q2 (2025-11-30) | 欠損 | 欠損 | 欠損 | — |
| FY2026 Q3 (2026-02-28) | 欠損 | 欠損 | 欠損 | — |
| FY2026 Q4 (2026-05-31) | 欠損 | 欠損 | 欠損 | — |
| FY2027 Q1 (2026-08-31) | 欠損 | 欠損 | 欠損 | — |

注: 検索結果に APLD の 2026 年の採掘数量・ハッシュレート・電力単価の記載なし。二次情報 (2023年の記事) では、同社は自社採掘ではなく他社機器のホスティングと記載されている。出所: https://decrypt.co/202590 (2023年記事、候補URL)

---

## 表7 会社ガイダンス・目標 (直近の発表)

| 発表日 | 内容 (売上・EBITDA・容量・稼働時期の目標) | 出所 |
|---|---|---|
| 2026-10-07 (FY27 Q1 決算) | FY2027 の売上・EBITDA の公式ガイダンス数値は未取得 (欠損)。決算は Q1 実績のみ確認 | https://www.sec.gov/Archives/edgar/data/0001144879/000114487926000057/apldq127earningsrelease.htm |
| 2026-07-27 (FY26 Q4 決算) | 数値ガイダンスは未取得 (欠損)。経営陣発言 (二次): 全建設プロジェクトは計画どおり・予算内。契約容量 1.41GW | https://www.sec.gov/Archives/edgar/data/0001144879/000114487926000044/apldq426earningsreleaseasf.htm / https://www.nasdaq.com/articles/applied-digital-q4-earnings-call-highlights (候補URL) |
| 2026-05 頃 (PF3 リース発表、二次) | PF3 300MW の初期稼働 2027-08 (二次) | https://theenergymag.com/news/market-news/applied-digital-inks-7-5-billion-lease-for-300-mw-at-polaris-forge-3-expanding-ai-factory-footprint |
| 2026-07-27 時点 (Q4 call、二次) | DF1 の初期稼働 2027 年中盤 (二次)。PF1 第3棟 (150MW) の RFS 2027 | https://www.nasdaq.com/articles/applied-digital-q4-earnings-call-highlights (候補URL) |
| 2025-08 (Zacks、二次) / 2026 (B. Riley 現地視察メモ、二次) | PF2: 初期 2026 年稼働、2027 年フル稼働 (Zacks)。B. Riley メモ: 第1データホール 2026 Q4、全容量 2027 Q4 (ただし 300MW と記載の箇所あり、不一致) | https://www.kapitalmarktexperten.de/applied-digital-aktie-polaris-forge-2-soll-q4-2027-laufen/ (候補URL) |
| 2026-04-08 (FY26 Q3 決算、二次) | 「弱い業績見通し」との記載あり (数値ガイダンスは欠損) | https://stocks.observer-reporter.com/observerreporter/article/stockstory-2026-4-14-why-applied-digital-apld-stock-is-up-today |

---

## 表8 株価・コンセンサス

| 出所サイト | 年度 | 売上予想平均 | EPS予想平均 | EBITDA予想 | アナリスト数 | 時点 | 出所URL |
|---|---|---|---|---|---|---|---|
| Tickflow | FY2027 (FYE 2027-05-31) | 702 (レンジ 514〜807) | −0.47 (レンジ −2.70〜+2.05) | 欠損 | 売上 4 / EPS 3 | 2026-07-31 | https://tickflow.io/stock/APLD/forecast |
| Tickflow | FY2028 以降 | 欠損 | 欠損 | 欠損 | 欠損 | — | https://tickflow.io/stock/APLD/forecast |
| Google Finance | FY2027 (売上・EPS・EBITDA は欠損) | 欠損 | 欠損 | 欠損 | 9 (Buy 7 / Hold 2) | 2026-10-05 | https://www.google.com/finance/quote/APLD:NASDAQ?hl=en |
| 参考 (非コンセンサス・出所不明) | FY2027 | 360 | −0.27 (信頼度 44/100) | 欠損 | 欠損 | 欠損 | https://www.vcpscanner.com/valuation/apld/estimates (候補URL) |
| 参考 (古い・2025年発表) | FY2027 | 欠損 | 0.04 (HC Wainwright) / 0.12 (Roth) | 欠損 | 欠損 | 2025 | https://www.marketbeat.com/instant-alerts/hc-wainwright-comments-on-applied-digital-fy2027-earnings-2025-08-26 (候補URL) |
| 参考 (年度ラベル不整合) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 7月 (日付不明) | https://stocksguide.com/en/forecast/Applied-Digital-US0381692070 (候補URL) |

**平均目標株価・レーティング分布**
- 平均目標株価: $60.07 (レンジ $22〜$83)。レーティング分布: Buy 7 / Hold 2 (計9名)。時点 2026-10-05、Google Finance 表示。株価は同時点 $24.70 (表示値)。

**直近の目標株価変更 (証券会社・前後・日付)**
- UBS: 開始 (initiation) $38。前後・日付は欠損 (Google Finance の直近動向欄に記載)。
- Rothschild Redburn: $22 (Hold)。日付は欠損 (同上)。
- Morgan Stanley: $37.50 (Hold、継続)。日付は欠損 (同上)。
- B. Riley / Northland / Needham: $75〜$83 (2026-08 時点の記載、二次)。日付の細部は欠損。
- Craig-Hallum: $37 → $39 (2025 年、新規 $5B リース後。日付は欠損)。出所: https://www.tipranks.com/news/apld-stock-rally-sends-applied-digital-to-a-new-52-week-high (候補URL)
- 出所URL (Google Finance): https://www.google.com/finance/quote/APLD:NASDAQ?hl=en

---

## 表9 2026年の株価の大きな変動

| 日付 | 騰落率 | 理由 | 出所 |
|---|---|---|---|
| 2026-03 頃 (記事上は「3月」。日付は推定) | −6.9% | $2.15B シニア担保付社債 (PF2 向け) の発行による負債懸念 (二次) | https://simplywall.st/stocks/us/software/nasdaq-apld/applied-digital/news/why-applied-digital-apld-is-down-69-after-215-billion-ai-dat/amp |
| 2026-04-09 頃 (推定: 04-14 の 5 営業日前) | −5.6% | 現金消耗 (FCF −720.2) と弱い業績見通しへの懸念。FY26 Q3 決算 (2026-04-08) 後 (二次) | https://stocks.observer-reporter.com/observerreporter/article/stockstory-2026-4-14-why-applied-digital-apld-stock-is-up-today |
| 2026-04-09 頃 (推定。見出しのみ) | −7% | 見出し: 売上 $126.6M (+139%) にもかかわらず下落。理由は見出しの範囲のみ (二次) | https://finder.techleap.nl/news/feed/applied-digital-shares-drop-7-despite-139-revenue-surge-to-126-6m |
| 2026-04-14 | +14.8% (終値 $31.68) | Bloom Energy と Oracle の提携を契機とする AI インフラ銘柄の上昇 (二次) | https://stocks.observer-reporter.com/observerreporter/article/stockstory-2026-4-14-why-applied-digital-apld-stock-is-up-today |
| 2026-07-27 (時間外) | +6% (時間外) | FY26 Q4 売上 $258.7M・約 $20B のバックログ積み増し (二次) | https://stocktwits.com/news-articles/markets/equity/apld-q4-revenue-quadruples-on-20-b-backlog/cZZxMX8R76M |
| 2026-09-28 | 欠損 (下落の記事見出しのみ確認) | 欠損 (本文未確認) | https://www.financialcontent.com/article/stockstory-2026-9-28-why-applied-digital-apld-stock-is-trading-lower-today |
| 2026-10-07 (大引け前) | −6.04% (終値 $23.81) | 欠損 (決算は大引け後発表。当日下落の要因は未確認) | 二次情報 (記事URL未特定) |
| 2026-10-08 (取引日) | 欠損 | Q1 FY27 決算 (売上 $341.9M、+322%) への反応は未取得 | — |

**補足**: 2026年の52週高値 $50.7 の発生日は欠損 (表1 参照)。2026-10-07 以降の株価 (10-08, 10-09) は未取得。

---

## 取得できなかった重要項目 (まとめ)

1. 2026-10-08 / 10-09 の終値と、FY27 Q1 決算後の株価反応
2. 52週安値 (2026-10 時点) と 52週高値の発生日
3. 直近10-Q (2026-08-31 期) の表紙の発行済株式数、希薄化後株式数
4. Google 宛のワラント、および Google 関連の信用補完 (未発見)
5. 2026 年の ATM 新規枠と使用額
6. 営業CF・capex・SBC・株式発行・借入の年度/四半期値 (表3。大部分欠損、FY2026 通期は候補値が不一致)
7. 表2 のHPC / DCH / 営業損益 / 希薄化後株式数の多くの欄 (FY2024 Q2〜FY2026 Q4 の一部、FY2027 Q1 の売上原価・営業損益・株式数)
8. 表4: 2.35B 社債の利率 (9.25% は未確認)、ブリッジの満期・担保、信用枠の金額 ($350M / $550M で不一致)、2026-08-31 時点の負債明細
9. 表5: 2025-08 〜 2026-02 の稼働・建設・契約 MW の具体値、電力確保量の総MW、PF1 / DF1 の建設費 (1MWあたり)、PF3 / DF2 の契約額、信用補完 (PF2 / PF3 / DF1 / DF2)
10. 表6: ビットコイン採掘 KPI 全期間 (自社採掘の有無も未確認)
11. 表7: FY2027 の売上・EBITDA 数値ガイダンス
12. 表8: 決算後 (2026-10-07 以降) のコンセンサス、EBITDA 予想、FY2028 以降の予想、各目標株価の日付
13. 表9: 2026-10-08 以降の大幅変動、2026-09-28 の下落理由
14. 本社・設立州以外の表1 項目の一次確認 (上場区分、決算日の公式発表は 8-K 本文未確認)
