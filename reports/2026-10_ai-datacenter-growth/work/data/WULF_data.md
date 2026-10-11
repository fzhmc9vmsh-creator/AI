# TeraWulf Inc. (NASDAQ: WULF) データ収集表

- 取得基準日: 2026-10-11
- 取得方法: WebSearch のみ (使用 32 回 / 上限 34 回)。WebFetch・curl は未使用。本文の数値は検索結果の抜粋・要約に基づく。
- 凡例:
  - 欠損 = 検索で値を確認できなかった (推測で埋めていない)
  - (算出: 式) = 出所の数値から計算した値
  - (二次情報) = 決算プレスリリース・SEC 本文以外の要約サイト・ニュース記事からの値
  - 不一致 = 複数ソースの値が食い違う (併記)
  - 損失はマイナス表記 (表2 の損益項目)。単位は特記なき限り百万米ドル (M)
- 指示文との相違 (事実の訂正): 指示文の「Anthropic 向け 401MW」の拠点は、検索結果によれば Kentucky 州 Hawesville の Justified campus であり、Abernathy (テキサス州) ではない。Google の信用補完は Lake Mariner (Fluidstack リース) に関するもの。

---

## 表1 基本情報

| 項目 | 値 | 時点 | 出所 |
|---|---|---|---|
| 法人設立州 (本籍) | Delaware (2021年2月設立) | FY2025 10-K 時点 | https://www.sec.gov/Archives/edgar/data/1083301/000108330126000031/wulf-20251231.htm |
| 本社所在地 | 9 Federal Street, Easton, Maryland 21601 (ニューヨーク市の拠点記載は FY2022 10-K にあり、FY2025 10-K では Easton のみ) | FY2025 10-K 時点 | https://www.sec.gov/Archives/edgar/data/1083301/000108330126000031/wulf-20251231.htm |
| 上場市場 | NASDAQ (ティッカー WULF)。2021年12月14日より取引開始 | 10-Q 表紙 (2026-06-30 期) | https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000166/wulf-20260630.htm |
| 決算期末 | 12月31日 | FY2025 10-K | https://www.sec.gov/Archives/edgar/data/1083301/000108330126000031/wulf-20251231.htm |
| 直近終値 (2026-10-09 前後) | 欠損。取得できた最新値は $16.48 (2026-09-04 時点の日中スナップショット、レンジ $15.94–16.63。終値との区別は不明) | 2026-09-04 | https://robinhood.com/us/en/stocks/WULF/ (二次情報) |
| 時価総額 | 欠損 (2026-10-09 時点)。取得できた最新値 $8.24B (2026-09-04、Robinhood)。参考: (算出: 498,968,677株 × $16.48 ≈ $8.22B) | 2026-09-04 | https://robinhood.com/us/en/stocks/WULF/ (二次情報) |
| 発行済株式数 (直近 10-Q 表紙) | 498,968,677 株 (2026-07-31 時点の発行済普通株) | 10-Q (2026-06-30 期) 表紙 | https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000166/wulf-20260630.htm |
| 希薄化後株式数 | 欠損 (加重平均希薄化後株式数は未確認。10-Q の損益計算書/EPS 注記で確認要) | 2026-06-30 期 | https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000166/wulf-20260630.htm |
| 52週高値・安値 | 高値: $29.83–29.84 (3 社で一致)。安値: $4.64–8.60 (不一致。Robinhood 8.60 / Upstox 5.04 / Coinglass 4.64。時点により窓が移動するため、各社の取得日時点の値) | 2026-07-26 〜 2026-09-04 | Robinhood https://robinhood.com/us/en/stocks/WULF/ ; Upstox https://upstox.com/us-stocks/wulf-share-price/ ; Coinglass https://www.coinglass.com/pt/stocks/WULF (いずれも二次情報) |
| Google 等に発行したワラント株数 | 当初 (2025年8月、Lake Mariner / Fluidstack バックストップ) 約4,100万株 (二次情報、pro forma 約8%)。増枠後 (Fluidstack 拡張時) の株数は欠損 (pro forma 約14%と報道) | 2025年8月 〜 2025年後半 | https://carboncredits.com/bitcoin-miner-terawulf-wulf-stock-rallies-as-google-backs-3-2b-ai-infrastructure-expansion ; https://www.theblock.co/post/367257/googles-pro-forma-stake-in-fifth-largest-bitcoin-miner-terawulf-grows-to-14-as-the-miner-plans-400-million-fundraising-plan (いずれも二次情報) |
| ATM (随時増資) プログラムの枠 | 2026年の ATM 合意は検索で確認できず。既存の sales agreement (Cantor / B. Riley / D.A. Davidson 等) は枠 $200M (2025年 prospectus supplement、prospectus 日付 2025-01-16) | 2025年 | https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001628280-25-024284/terawulf424b5.htm (二次情報の参照) |
| ATM の使用額 | 欠損 | — | — |
| (参考) 2026年4月の大型公募 | Morgan Stanley 引受け、47,400,000株 @ $19.00 (グリーンシュー 7,110,000株)。2026-04-16 クローズ。純額 約$1,004.3M (ATM ではない) | 2026-04-16 | https://www.boardroomalpha.com/sec/wulf-8-k-2026-04-16-0001104659-26-044387 (二次情報の参照) |

---

## 表2 四半期業績 (2024年Q1〜2026年Q2、最新が一番下)

損失はマイナス表記。HPC 売上は 2025年7月開始 (FY2025 10-K) のため、それ以前の HPC 売上は 0 と記載。

| 四半期 | 総売上 | うちHPC/AIリース・コロケーション売上 | うちビットコイン採掘売上 | その他 | 売上総利益または売上原価 | 営業損益 | 純損益(GAAP) | 希薄化後EPS | 調整後EBITDA(会社定義) | 希薄化後株式数(加重平均) | 出所 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2024年Q1 | 42.4 | 0 | 欠損 | 欠損 | 総利益 28.0 / 原価 14.4 (減価償却除く) | 欠損 | 欠損 | −0.03 (二次情報) | 32.0 | 欠損 | 決算リリース: https://markets.financialcontent.com/pennwell.oilgasjournal/article/gnwcq-2024-5-13-terawulf-reports-first-quarter-2024-financial-results ; 8-K: https://www.sec.gov/Archives/edgar/data/1083301/000108330124000102/aex991xearningsreleasexq12.htm |
| 2024年Q2 | 35.6 | 0 | 欠損 | 欠損 | 総利益 21.7 / 原価 13.9 (算出: 35.6−21.7) | 欠損 | 欠損 | −0.03 (二次情報: Benzinga) | 19.5 | 欠損 | 8-K: https://www.sec.gov/Archives/edgar/data/1083301/000108330124000122/wulf-20240812.htm ; https://markets.financialcontent.com/pennwell.oilgasjournal/article/gnwcq-2024-8-12-terawulf-reports-second-quarter-2024-financial-results |
| 2024年Q3 | 27.1 | 0 | 欠損 | 欠損 | 欠損 | 欠損 | 不一致: −23.0 (決算コール要約) / −43.2 (別要約) | −0.06 (二次情報: Benzinga) | 6.0 | 欠損 | 8-K: https://www.sec.gov/Archives/edgar/data/1083301/000108330124000145/aex991xearningsreleasexq.htm ; https://itiger.com/news/2483768250 ; https://itiger.com/news/1160381030 |
| 2024年Q4 | 35.0 (算出: FY 140.1 − Q1〜Q3 105.1; 要約では「約35」) | 0 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 2.5 (二次情報) | 欠損 | FY2024 決算リリース: https://www.sec.gov/Archives/edgar/data/1083301/000108330125000013/a_wulfformearningsrelease2.htm |
| 2025年Q1 | 34.4 | 0 | 欠損 | 欠損 | 原価 24.6 (減価償却除く、前年 14.4) | 欠損 | −61.4 (算出: 6ヶ月 −79.8 − Q2 −18.4。二次情報) | −0.16 (二次情報) | −4.7 | 欠損 | 8-K: https://www.sec.gov/Archives/edgar/data/1083301/000108330125000033/a_wulfformearningsreleas.htm ; 10-Q: https://www.sec.gov/Archives/edgar/data/1083301/000108330125000038/wulf-20250331.htm ; EPS: https://www.itiger.com/news/1155098322 |
| 2025年Q2 | 47.6 | 0 | 欠損 | 欠損 | 原価 22.1 (減価償却除く, 22,094千ドル) | 欠損 | −18.4 (二次情報) | −0.05 (二次情報: 247Wallst) | 14.5 | 欠損 | 8-K: https://www.sec.gov/Archives/edgar/data/1083301/000108330125000058/a_wulfformearningsreleaseq.htm ; 10-Q: https://www.sec.gov/Archives/edgar/data/1083301/000108330125000061/wulf-20250630.htm ; https://simplywall.st/stocks/us/software/nasdaq-wulf/terawulf/news/are-terawulfs-wulf-widening-losses-reshaping-its-long-term-p |
| 2025年Q3 | 50.6 | 7.2 | 43.4 | 0 (算出: 50.6 − 7.2 − 43.4) | 欠損 | 欠損 | 約 −455 (二次情報。うち非現金のワラント/デリバティブ損失 −424.6) | 不一致: 調整後 −0.07 (Zacks) / −0.04 (Seeking Alpha) | 18.1 | 欠損 | 8-K: https://www.sec.gov/Archives/edgar/data/1083301/000110465925102858/tm2529509d1_ex99-2.htm ; https://www.zacks.com/stock/news/2789393/terawulf-q3-loss-wider-than-expected-revenues-increase-yy |
| 2025年Q4 | 35.8 | 9.7 | 26.1 | 0 (算出: 35.8 − 9.7 − 26.1) | 欠損 | 欠損 | 約 −127 (算出: FY −661.4 − (Q1 −61.4 + Q2 −18.4 + Q3 約−455)。Q3 が概数のため粗い) | −0.27 (二次情報: Seeking Alpha。247Wallst は −1.66 で不一致) | −50.9 (算出: FY −23.1 − (Q1 −4.7 + Q2 14.5 + Q3 18.1) = −51.0。2026年Q1要約の前期値 −50.9 と整合) | 欠損 | 決算リリース: https://investors.terawulf.com/news-events/press-releases/detail/132 ; https://www.sec.gov/Archives/edgar/data/1083301/000108330126000031/wulf-20251231.htm ; https://seekingalpha.com/pr/20416548 |
| 2026年Q1 | 34.0 | 21.0 | 約13.0 (二次情報・算出: 34.0 − 21.0) | 欠損 | 原価 2.4 (減価償却除く、二次情報。前期 18.9 から −88%) | 欠損 | −427.6 (二次情報) | 不一致: −1.01 / −0.92 (集計サイト) | −4.1 (二次情報。4月の事前開示レンジ 0〜3 を下回る) | 欠損 | 8-K: https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000083/a_wulfearningsreleaseq1202.htm ; 要約: https://finance.yahoo.com/markets/stocks/articles/terawulf-q1-earnings-call-highlights-080704337.html |
| 2026年Q2 | 44.8 (44.77) | 31.9 | 約12.9 (算出: 44.8 − 31.9。会社開示は未確認) | 欠損 | 欠損 | −140.5 (二次情報・要確認。別検索では営業損失の記載を確認できず) | −939.9 (親会社株主帰属。うち非現金のワラント公正価値損失 −755.7) | −1.94 (二次情報: 集計サイト) | −18.3 | 欠損 | 8-K: https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000162/a_wulfearningsreleaseq22026.htm ; リリース: https://investors.terawulf.com/news-events/press-releases/detail/144 ; 10-Q: https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000166/wulf-20260630.htm |

---

## 表3 キャッシュフロー・資本支出

| 期間 | 営業CF | 設備投資(capex) | 株式報酬(SBC) | 株式発行による調達 | 借入による調達 | 期末現預金 | 出所 |
|---|---|---|---|---|---|---|---|
| 2025年Q3 (7〜9月) | 欠損 | 欠損 | 欠損 | 欠損 | 2025-08-20 発行: 1.00%転換社債 (2031年満期) 元本 1,000.0 (純額 約975.3) | 712.8 (2025-09-30、現金+制限付現金。二次情報) | https://www.theenergymag.com/news/2025-08-19/terawulf-convertible-hpc ; https://www.zacks.com/stock/news/2789393/terawulf-q3-loss-wider-than-expected-revenues-increase-yy |
| 2025年Q4 (10〜12月) | 欠損 | 欠損 | 欠損 | 欠損 | 2025-10: 7.750%担保付シニア債 (2030年満期) 元本 3,200.0 / 2025-10-31: 0.00%転換社債 (2032年満期) 元本 1,025.0 | 3,722.8 (2025-12-31、現金・同等物+制限付現金。不一致: 別ソースで 142.9) | FY2025 決算: https://investors.terawulf.com/news-events/press-releases/detail/132 ; 10-K: https://www.sec.gov/Archives/edgar/data/1083301/000108330126000031/wulf-20251231.htm ; 8-K: https://investors.terawulf.com/news-events/press-releases/detail/119/terawulf-inc-announces-pricing-of-3-2-billion-of-senior/ |
| 2025年通期 | 欠損 | 欠損 | 欠損 | 欠損 | 上記に同じ | 3,722.8 (同上) | 10-K (同上) |
| 2026年Q1 (1〜3月) | 欠損 | 欠損 | 欠損 | 欠損 | 250 の回転信用枠を締結 (借入額は欠損) | 約3,100 (現金+制限付現金、二次情報含む) | https://investors.terawulf.com/news-events/press-releases/detail/140 |
| 2026年上期 (1〜6月) | −154.3 (二次情報: 2025年上期は +1.7) | 欠損 | 欠損 | 2026-04-16 クローズの公募: 純額 約1,004.3 (47.4M株 @ $19.00 + グリーンシュー) | 欠損 | — | https://www.tradingkey.com/news/earnings/262077885-tradingkey (二次情報) ; https://www.boardroomalpha.com/sec/wulf-8-k-2026-04-16-0001104659-26-044387 |
| 2026年Q2 (4〜6月) | 欠損 (四半期単独値は未確認) | 欠損 (注: 336MW 建設は「既存コスト見積もり 8〜10 百万ドル/MW 内」との 8-K 記述。支出額ではない) | 83.9 (2025年Q2は 1.3)。別途 慈善寄付 (株式) 14.4 (二次情報) | 1,004.3 (上記の公募) | 欠損 | 約3,000 (2026-06-30、現金+制限付現金) | 8-K: https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000162/a_wulfearningsreleaseq22026.htm ; https://www.tradingkey.com/news/earnings/262077885-tradingkey (二次情報) |

---

## 表4 負債の明細

直近期末 (2026-06-30) の残高・転換・買戻しの状況は未確認。下記は発行時点の条件。

| 証券・借入 | 元本 | 金利 | 満期 | 担保・リコース | 転換価格(転換社債) | 出所 |
|---|---|---|---|---|---|---|
| 1.00% 転換社債 (2031年満期) | 1,000.0 (追加購入分を含む。発行時点) | 1.00% (3/1・9/1 払い) | 2031-09-01 | 無担保シニア (リコース性は欠損) | 約 $12.43 (1,000ドル当たり 80.4602 株)。キャップドコール上限 $18.76 | https://www.theenergymag.com/news/2025-08-19/terawulf-convertible-hpc ; https://seekingalpha.com/news/4486805-terawulf-prices-850m-convertible-debt-offering (二次情報) |
| 2.75% 転換社債 (2030年満期) | 500.0 (うち 75.0 は追加購入分) | 2.75% (5/1・11/1 払い、実効 3.3%) | 2030-02-01 | 欠損 | 約 $8.48 (1,000ドル当たり 117.9245 株) | https://www.sec.gov/Archives/edgar/data/1083301/000095014224002636/eh240549125_8k.htm ; FY2025 10-K: https://www.sec.gov/Archives/edgar/data/1083301/000108330126000031/wulf-20251231.htm |
| 7.750% 担保付シニア債 (WULF Compute LLC 発行) | 3,200.0 (2025年10月 発行、Rule 144A) | 7.750% (4/15・10/15 払い) | 2030-10-15 | 担保: Google から受領したワラント等を担保として差入れ (二次情報)。保証: La Lupa Data LLC / Akela Data Holdings LLC / Akela Data LLC。リコース性は欠損。クローズ日は不一致 (10-K: 10-22 / 8-K: 10-23) | 転換価格: 該当なし | https://www.sec.gov/Archives/edgar/data/1083301/000110465925100142/tm2528904d1_ex99-1.htm ; https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000092/wulf-20260331.htm |
| 0.00% 転換社債 (2032年満期) | 1,025.0 (2025-10-31 完了) | 0.00% | 2032 (月日は欠損) | 欠損 | 約 $19.94 (1,000ドル当たり 50.1567 株) | FY2025 10-K (二次情報の参照): https://www.sec.gov/Archives/edgar/data/1083301/000108330126000031/wulf-20251231.htm |
| 回転信用枠 | 250 (枠) | 欠損 | 欠損 | 欠損 | 該当なし | 2026年Q1 決算: https://investors.terawulf.com/news-events/press-releases/detail/140 |
| (参考) Abernathy JV 50.1% 持分の売却 (負債ではない) | 約530 (売却代金。報道では3回分割、2027年4月までの支払い) | — | — | — | — | https://theenergymag.com/news/market-news/terawulf-anthropic-ai-data-center-stake-fluidstack (二次情報) |

---

## 表5 AI/HPC の容量と契約

### 5-1 時系列 (直近6四半期と現在)

| 時点 | 稼働中(エネルギー供給済み)のIT容量MW | 建設中MW | 契約済みMW | 契約済み収益総額 | 主要テナント | 年換算契約収益 | 電力の確保量(総MW) | 出所 |
|---|---|---|---|---|---|---|---|---|
| 2025-03-31 (2025年Q1) | HPC 0。ビットコイン採掘を含む総容量 245 | 欠損 | 欠損 | 欠損 | Core42 (72.5 MW のHPC提供を2025年中に予定) | 欠損 | 欠損 | 8-K: https://www.sec.gov/Archives/edgar/data/1083301/000108330125000033/a_wulfformearningsreleas.htm |
| 2025-06-30 (2025年Q2) | HPC 0 (HPC 提供は 2025年7月開始)。採掘 欠損 | 欠損 | 欠損 (Fluidstack 200+ MW の合意を開示) | 約3,700 (Fluidstack 分。延長行使で最大 8,700) | Fluidstack、Core42 | 欠損 | 欠損 | 8-K: https://www.sec.gov/Archives/edgar/data/1083301/000108330125000058/a_wulfformearningsreleaseq.htm ; https://www.marketbeat.com/earnings/reports/2025-8-8-terawulf-inc-stock |
| 2025-09-30 (2025年Q3) | HPC 22.5 (Lake Mariner) / 採掘 245 | 欠損 | 520+ (長期 HPC リース、二次情報) | 欠損 | 企業・ハイパースケール顧客 (個別名は欠損。Lake Mariner の既知テナントとして Core42) | 欠損 | 欠損 | https://www.zacks.com/stock/news/2789393/terawulf-q3-loss-wider-than-expected-revenues-increase-yy ; 8-K: https://www.sec.gov/Archives/edgar/data/1083301/000110465925102858/tm2529509d1_ex99-2.htm |
| 2025-12-31 (2025年Q4) | 欠損 | 378 (算出: CB-3 42 + CB-4 168 + CB-5 168。2026年2月時点の建設計画) | 522 (critical IT MW) | 12,800 超 (FY2025 決算時点) | Fluidstack、Core42 等 | 欠損 | 欠損 | https://www.barchart.com/story/news/453189/terawulf-reports-fourth-quarter-and-full-year-2025-results ; https://investors.terawulf.com/news-events/press-releases/detail/132 |
| 2026-03-31 (2026年Q1) | 60 (Lake Mariner、Core42 向けに稼働) | 欠損 | 欠損 (250〜500 MW/年の新規契約目標を再確認。2.1 GW の管理パイプラインは別概念) | 欠損 | Core42、Fluidstack | 欠損 | 欠損 | https://investors.terawulf.com/news-events/press-releases/detail/140 ; 8-K: https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000083/a_wulfearningsreleaseq1202.htm |
| 2026-06-30 (2026年Q2) | 81 (Lake Mariner、収益計上中) | 336 (CB-4 および CB-5) | 欠損 | 欠損 | Fluidstack、Core42 | 欠損 | 欠損 | https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000162/a_wulfearningsreleaseq22026.htm ; https://www.theenergymag.com/news/market-news/terawulf-anthropic-ai-data-center-stake-fluidstack |
| 現在 (2026-10-11 時点、CB-3 完了後) | 102 (CB-3 完了は 2026年7月初旬。二次情報含む) | 336 (CB-4 は 2026年下期の賃料開始見込み、CB-5 は 2027年初頭からの段階引渡し見込み) | 欠損 (2026年7月に Anthropic 401 MW を追加。他契約との合算は未確認) | Anthropic 分 約19,000 (初期期間) | Anthropic、Fluidstack、Core42 | 欠損 (Anthropic 分のみ (算出: 19,000 ÷ 20年 ≈ 950/年、単純平均)) | 482 MW (Kentucky 規制当局の承認を報じた断片情報。Justified campus 向け、要確認) | https://www.theenergymag.com/news/market-news/terawulf-anthropic-ai-data-center-stake-fluidstack ; https://www.theenergymag.com/news/2025-08-19/terawulf-convertible-hpc ; https://www.datacenterdynamics.com/en/news/anthropic-signs-19bn-20-year-lease-for-kentucky-data-center-with-terawulf/ |

### 5-2 リース契約ごとの行

| 契約名/拠点 | テナント | MW | 期間 | 契約総額 | 稼働開始時期 | 信用補完 (Googleの保証額など) | 建設費 (1MWあたり) | 出所 |
|---|---|---|---|---|---|---|---|---|
| Justified campus, Hawesville, Kentucky (Anthropic 向け) | Anthropic | 401 (critical IT) | 20年 (初期期間) | 約 19,000 (初期期間、二次情報) | 初期 2027年下期、全面 2028年初頭 | 投資適格の信用補完 (金額・提供者は欠損) | 欠損 | https://www.datacenterdynamics.com/en/news/anthropic-signs-19bn-20-year-lease-for-kentucky-data-center-with-terawulf/ ; 発表日は 2026-07-06 (二次情報) : https://app.sentisense.ai/stories/terawulf-announces-major-19b-anthropic-lease-expands-ai-operations-07062026 |
| Lake Mariner, Barker, New York (Core42) | Core42 | 72.5 (gross HPC 提供インフラ。2026年Q1 時点で 60 MW 稼働) | 10年 (二次情報) | 1,000 超 (二次情報) | 2025年 (段階的。2026年Q1 に稼働開始) | 欠損 | 欠損 | FY2024 決算要約: https://www.mexc.com/news/814097 (二次情報) ; Q1 2026: https://investors.terawulf.com/news-events/press-releases/detail/140 |
| Lake Mariner, CB-3 / CB-4 / CB-5 (Fluidstack) | Fluidstack | 200 以上 (2025年8月の合意) → 約 360 (増枠後、二次情報) | 欠損 | 3,700 (2025年8月時点。延長行使で最大 8,700) | CB-3 (42 MW) 2026年7月に完了。CB-4 2026年下期。CB-5 2027年初頭 (段階引渡し) | Google バックストップ: 当初 1,800 → 増枠後 3,200 (二次情報)。CB-3 完了で 600 の支援が発効 (二次情報) | 8〜10 (百万ドル/MW。8-K 記載の既存コスト見積もり。集計サイトの 80〜100 は 8-K 記述と不一致のため不採用) | https://www.theblock.co/post/367257/googles-pro-forma-stake-in-fifth-largest-bitcoin-miner-terawulf-grows-to-14-as-the-miner-plans-400-million-fundraising-plan ; https://carboncredits.com/bitcoin-miner-terawulf-wulf-stock-rallies-as-google-backs-3-2b-ai-infrastructure-expansion ; https://www.marketbeat.com/earnings/reports/2025-8-8-terawulf-inc-stock ; 8-K (2026-08): https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000162/a_wulfearningsreleaseq22026.htm |
| Abernathy JV, Abernathy, Texas (Fluidstack JV) | Fluidstack (JV パートナー) | 168 (critical IT、JV) | 欠損 | 欠損 | 欠損 | 約 1,300 の Google 支援と Sacra 要約に記載 (Abernathy 向け。出所の信頼性は低く要確認) | 欠損 | https://www.sacra.com/c/fluidstack (二次情報) ; https://theenergymag.com/news/market-news/terawulf-anthropic-ai-data-center-stake-fluidstack (二次情報: 50.1% 持分の売却 約530 を 2026-08 時点で合意) |

---

## 表6 ビットコイン採掘 KPI (直近6四半期)

| 四半期 | 採掘BTC数 | ハッシュレート(EH/s) | 1BTCあたり電力コスト | 出所 |
|---|---|---|---|---|
| 2025年Q1 | 欠損 | 12.2 (自社採掘、前年比 +52.5%) | 欠損 | https://www.sec.gov/Archives/edgar/data/1083301/000108330125000033/a_wulfformearningsreleas.htm |
| 2025年Q2 | 485 | 12.8 (前年比 +45.5%) | 45,555 USD (前年 22,954) | https://www.sec.gov/Archives/edgar/data/1083301/000108330125000058/a_wulfformearningsreleaseq.htm ; https://247wallst.com/companies/wulf/earnings/2025/Q2 |
| 2025年Q3 | 欠損 | 欠損 | 欠損 (採掘容量 245 MW 稼働は確認) | https://www.zacks.com/stock/news/2789393/terawulf-q3-loss-wider-than-expected-revenues-increase-yy |
| 2025年Q4 | 欠損 | 欠損 | 欠損 (デジタル資産売上 26.1、減少要因は生産量と BTC 価格) | https://www.sec.gov/Archives/edgar/data/1083301/000108330126000031/wulf-20251231.htm |
| 2026年Q1 | 欠損 (2026年3月の月次 56.0 BTC のみ確認) | 7.9 稼働 / 10.9 設置 (2026-03-31、集計サイトの値・未確認) | 欠損 (売上原価 2.4 と需要応答収入 14.1 は二次情報) | https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000083/a_wulfearningsreleaseq1202.htm ; https://bitcoinminingstock.io/company/wulf (二次情報) |
| 2026年Q2 | 欠損 | 欠損 | 欠損 | https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000162/a_wulfearningsreleaseq22026.htm |

---

## 表7 会社ガイダンス・目標 (直近の発表)

| 発表日 | 内容 (売上・EBITDA・容量・稼働時期の目標) | 出所 |
|---|---|---|
| 2025-05-09 (Q1 2025) | 2025年に Core42 向け HPC 72.5 MW を提供。2026年末までに 200〜250 MW 稼働 (当時の目標。後続の更新は未確認) | https://www.quantisnow.com/insight/terawulf-reports-first-quarter-2025-results-6029105 ; 8-K: https://www.sec.gov/Archives/edgar/data/1083301/000108330125000033/a_wulfformearningsreleas.htm |
| 2025-08-08 (Q2 2025) | SG&A ガイダンスを 40〜45 から 50〜55 に引上げ (HPC 拡大のため)。Fluidstack 200 MW 超、契約収益 3,700 | https://www.sec.gov/Archives/edgar/data/1083301/000108330125000058/a_wulfformearningsreleaseq.htm |
| 2025-11-10 (Q3 2025) | HPC の新規契約目標を年 250〜500 MW に引上げ (従来 100〜150 MW)。事前開示 (2025-10-28): Q3 売上 48〜52、調整後EBITDA 15〜19 | https://www.zacks.com/stock/news/2789393/terawulf-q3-loss-wider-than-expected-revenues-increase-yy ; 8-K: https://www.sec.gov/Archives/edgar/data/1083301/000110465925102858/tm2529509d1_ex99-2.htm |
| 2026-02-26 (Q4/FY2025) | 2026年の固定運営費 100〜125。2026年末まで年 250〜500 MW の新規 critical IT 納入目標。建設計画 (二次情報): CB-3 42 MW (2026年5月中旬)、CB-4 168 MW (2026年Q3)、CB-5 168 MW (2026年Q4) | https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001083301-26-000026/a_wulfearningsrelease2026-.htm ; https://www.barchart.com/story/news/453189/terawulf-reports-fourth-quarter-and-full-year-2025-results |
| 2026-04 (Q1 2026 事前開示) | Q1 2026 売上 30〜35、調整後EBITDA 0〜3 (実績 −4.1 は下限を下回る) | https://investors.terawulf.com/news-events/press-releases/detail/134 |
| 2026-05-08 (Q1 2026) | 年 250〜500 MW の契約目標を再確認。Lake Mariner で 60 MW を稼働。250 の回転信用枠をクローズ。2.1 GW の管理パイプライン | https://investors.terawulf.com/news-events/press-releases/detail/140 ; 8-K: https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000083/a_wulfearningsreleaseq1202.htm |
| 2026-08-05 (Q2 2026) | CB-4 の賃料開始は 2026年下期、CB-5 は 2027年初頭から段階引渡し (二次情報)。Justified (Anthropic) は初期 2027年下期、全面 2028年初頭 (二次情報)。Muskie は 2028年Q4 の初期供用、Chesapeake は 2030年の見込み (規制承認待ち、二次情報)。既存流動性と Abernathy 売却代金で近期の義務を賄えるとの見解 (二次情報) | https://investors.terawulf.com/news-events/press-releases/detail/144 ; https://quartr.com/events/terawulf-inc-wulf-q2-2026_F97bGNTj |
| 2026年 通期の調整後EBITDA目標 | 欠損 (未確認) | — |

---

## 表8 株価・コンセンサス

| 出所サイト | 年度 | 売上予想平均 | EPS予想平均 | EBITDA予想 | アナリスト数 | 時点 | 出所URL |
|---|---|---|---|---|---|---|---|
| Investing.com | 欠損 (2026年度以降の予想値は未取得) | 欠損 | 欠損 | 欠損 | 24 (評価 Strong Buy) | 2026年9月末 | https://uk.investing.com/equities/ikonics-corp-consensus-estimates (URL の旧社名表記に注意) |
| Benzinga | 欠損 | 欠損 | 欠損 | 欠損 | 28 (評価 Buy。空売り比率 28.6%) | 2026年9月末前後 | https://benzinga.com/quote/WULF/analyst-ratings |
| MarketBeat | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 (評価 Moderate Buy) | 2026年3月 | https://www.marketbeat.com/stocks/NASDAQ/WULF/price-target/ |
| Investing.com (参考) | 欠損 | 欠損 | 欠損 | 欠損 | 18 | 2026年7月頃 | https://uk.investing.com/equities/ikonics-corp-consensus-estimates |

平均目標株価・レーティング・目標株価変更:

- 平均目標株価 (2026年9月末、Investing.com): 約 $33.69 (レンジ $15〜62.5)。Benzinga の平均は $22 (不一致)。MarketBeat (2026年3月) は $21.29。Investing.com (2026年7月頃) は $38.39。
- レーティング分布: 欠損 (件数は未取得。評価の種類のみ: Buy 中心、Hold 1 件 (Rothschild Redburn))。
- 直近の目標株価変更 (確認できたもの):
  - Bernstein: Outperform 維持、目標 $36 (Anthropic 契約発表後、2026年7月。二次情報)
  - Morgan Stanley: 目標 $63 (Benzinga の高値。日付は欠損)。2026年3月に Overweight で開始、目標 $37 (MarketBeat)
  - Rothschild Redburn: Hold、目標 $15 (2026年9月末時点)
  - Jones Trading: Buy、目標 $30 (同時点)
  - Wells Fargo: Buy、目標 $30 (同時点)
  - UBS: Buy、目標 $24 (同時点)
  - 注: Benzinga の $3 (Stifel) は 2023年10月の古い値のため除外

---

## 表9 2026年の株価の大きな変動

| 日付 | 騰落率 | 理由 | 出所 |
|---|---|---|---|
| 2026-03-13 | 欠損 (水準のみ: 約 $14.60) | 欠損 | 集計サイトの価格スナップショット (個別 URL は特定できず。二次情報・要確認) |
| 2026-04-16 (公募クローズ) | 欠損 (公募価格 $19.00) | Morgan Stanley 引受けによる 47.4M 株の公募 | https://www.boardroomalpha.com/sec/wulf-8-k-2026-04-16-0001104659-26-044387 |
| 2026-05-08〜 (Q1 2026 決算後) | 欠損 (「shares fall」との見出しのみ) | Q1 決算。HPC 売上が BTC 売上を上回った一方、純損失 −427.6 (二次情報) | https://tangem.com/en/news/investments/24042-terawulf-q1-hpc-revenue-surpasses-mining-shares-fall/ |
| 2026-06-23 | 欠損 (終値 $28.78) | 欠損 | https://www.marketbeat.com/stocks/NASDAQ/WULF/options/ (二次情報) |
| 2026-07-06 (Anthropic 契約発表日) | 約 +14% (終値ベースの報道。寄り前は +15〜17%) | 20年・約190億ドル (19B) の Anthropic リース (Kentucky, Justified) と Abernathy JV 持分売却 | https://decrypt.co/372810/bitcoin-mining-stocks-jump-terawulf-19-billion-lease-anthropic ; https://oodaloop.com/briefs/technology/terawulf-shares-soar-after-anthropic-leases-data-center-in-kentucky/ (いずれも二次情報) |
| 2026-07-07 (翌営業日) | 約 −8〜−9% (報道) | 初期の上昇の反落 (理由の記載は欠損) | https://app.sentisense.ai/stories/terawulf-announces-major-19b-anthropic-lease-expands-ai-operations-07062026 (二次情報) |
| 2026-07-24 または 07-25 (前営業日) | −7.93% (日付は不確定) | 欠損 | https://www.coinglass.com/pt/stocks/WULF (二次情報) |
| 2026-07-26 | 水準 $18.46 | 欠損 | https://www.coinglass.com/pt/stocks/WULF (二次情報) |
| 2026-08-05 (Q2 2026 決算) | 欠損 | 売上 44.8 は予想 約 50.5 を下回る (約 11% 未達、二次情報)。調整後EBITDA −18.3。GAAP 純損失 −939.9 (非現金ワラント損失 −755.7) | https://investors.terawulf.com/news-events/press-releases/detail/144 ; https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000162/a_wulfearningsreleaseq22026.htm |
| 2026-08-11 | −4.98% (日中・水準 $16.20) | 欠損 | https://upstox.com/us-stocks/wulf-share-price/ (二次情報) |
| 2026-09-04 | 日中レンジ $15.94〜16.63 (終値は欠損) | 欠損 | https://robinhood.com/us/en/stocks/WULF/ (二次情報) |
| 2026-10-09 〜 10-11 | 欠損 | 欠損 (当日の値動きと理由は取得できず) | — |

---

## 取得できなかった重要項目 (まとめ)

1. 直近終値 (2026-10-09 前後) と時価総額の正確な値 (最新取得は 2026-09-04)
2. 加重平均・希薄化後株式数 (全四半期)。10-Q の損益計算書で確認要
3. 2024年Q4 〜 2025年Q4 の GAAP 純損益・EPS の一部 (2024年Q1/Q2/Q4、2025年Q3 GAAP EPS、2025年Q4 の確定値)
4. セグメント別売上 (BTC 採掘売上) の 2024年〜2025年Q2 と 2026年Q2 の確定値
5. 売上総利益・営業損益 (大半の四半期)。2026年Q2 の営業損失 −140.5 は単一の二次情報
6. 営業CF・capex・借入・株式発行の四半期別値 (2026年Q2 単独の営業CF と capex を含む)
7. 2026-06-30 時点の負債残高、2030年転換社債の残高・買戻し状況、7.750% 債の非リコース性
8. ATM 2026 年の合意・使用額。Google ワラントの現在の株数 (増枠後)
9. 2026年通期の調整後EBITDA 目標。2026年・2027年の売上・EPS の予想平均 (コンセンサス)
10. 採掘BTC数・電力コスト (2025年Q1、Q3、Q4、2026年Q1・Q2 の確定値)
11. 契約ごとの年換算収益・電力確保量の総計、Fluidstack / Core42 のリース期間の確定値、建設費の確定値
12. 2026年の株価変動のうち、日付・騰落率・理由が確定したもの (特に 2026年5月の Q1 決算後の下落幅、2026年6月〜7月の下落理由)
13. 2026年 Anthropic 契約の正式な発表日 (7月6日は二次情報)。Justified の信用補完の提供者と金額
