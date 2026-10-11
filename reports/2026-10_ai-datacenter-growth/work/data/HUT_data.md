# Hut 8 Corp. (NASDAQ: HUT) データ収集表

- 作成日: 2026-10-11
- 手段: WebSearch のみ (mode は全て standard、合計34回)。WebFetch と curl は未使用。
- 注記: SEC 8-K/10-Q の本文は検索スニペット経由でのみ確認できたものが大半。二次情報 (ニュース・集計サイト) に基づく値は出所欄に「二次」と明記した。出所間で食い違う値は両方の値を併記し、「不一致」と書いた。
- 「欠損」= 検索で値を取得できなかった項目。推測では埋めていない。
- 「(算出: 式)」= 取得済みの値から計算した値。

---

## 表1 基本情報

| 項目 | 値 | 時点 | 出所 |
|---|---|---|---|
| 法人設立州(本籍) | Delaware | 10-Q表紙 (Q1 2026 提出, 株式数基準日 2026-05-04) | 10-Q Q1 2026 (表紙は boardroomalpha 転記で確認): https://www.boardroomalpha.com/sec/hut-10-q-2026-05-06-0001104659-26-055891 / SEC: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926055891/hut-20260331x10q.htm |
| 本社所在地 | 1101 Brickell Avenue, Suite 1500, Miami, Florida 33131 | 10-Q表紙 (Q1 2026) | 同上 |
| 上場市場 | NASDAQ (ティッカー: HUT)。TSX(トロント)上場にも言及あり(二次) | 2026-10 時点の表示 | https://www.marketbeat.com/stocks/NASDAQ/HUT/chart |
| 決算期末 | 12月31日 | 2026-06-30 (Q2 2026 10-Q の期間末) | 10-Q Q2 2026: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926090025/hut-20260630x10q.htm |
| 直近終値 | $89.63 (2026-10-02 終値) | 2026-10-02 | https://www.marketbeat.com/stocks/NASDAQ/HUT/chart ／ 2026-10-09前後の終値: 欠損 (検索で取得できず) |
| 直近終値の参考 (採用せず) | InvestSmart 表示 144.53 (2026-09-24 終値)、Syfe 表示 $93.55 (「Sep 4」・年表記なし) | 上記の時点 | 採用せず: InvestSmart は豪州サイトかつ TSX 銘柄ページのため通貨が米ドルでない可能性あり(推定)。https://www.investsmart.com.au/security/tse/hut/hut-8-corp/share-price ／ https://www.syfe.com/stocks/us/HUT |
| 時価総額 | 約$11.05B (算出: 89.63 × 123,259,468株 = 約11.05B。MarketBeat の表示 $11.05B とも一致) | 2026-10-02 | https://www.marketbeat.com/stocks/NASDAQ/HUT/chart |
| 発行済株式数 | 123,259,468株 | 2026-07-31 (Q2 2026 10-Q 表紙) | 10-Q Q2 2026 表紙 (boardroomalpha 転記): https://www.boardroomalpha.com/sec/hut-10-q-2026-08-04-0001104659-26-090025 ／ SEC: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926090025/hut-20260630x10q.htm 。参考: 貸借対照表上 2026-06-30 時点 123,190,559株 (三次情報、STOCK TITAN 系要約) |
| 希薄化後株式数 | 欠損 | — | — |
| 52週高値・安値 | 高値 $140.80 ／ 安値 $31.67 | 2026-10-02 時点の52週レンジ (高値の日付: 欠損) | https://www.marketbeat.com/stocks/NASDAQ/HUT/chart 。注: 2026-07 時点の別スナップショットに安値 $18.68 があるが、古い期間の値のため採用せず |
| Google 等に発行したワラントの株数 | 欠損 | — | 検索範囲で Hut 8 による Google 向けワラント発行は確認できず。River Bend について、Benchmark のアナリスト見解として「Google の支払い保証により、ワラント等のエクイティ上乗せなしで完全な経済的持分を保持」との記述あり (分析者の見解であり開示事項ではない): https://finance.yahoo.com/news/hut-8-ai-data-center-141338282.html 。TeraWulf・Cipher の Google ワラント事例は他社のため除外 |
| ATM (随時増資) プログラムの枠 | 2025 ATM: $1.0B (2025-08-22 設定。2024 ATM $500M を置換) | 2026-06-30 | 10-Q Q2 2026: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926090025/hut-20260630x10q.htm |
| ATM の使用額 | 2026年 Q1: 2,101,363株、グロス $120.9M、発行費用 $0.8M。2026年上半期も同額で、Q2 の追加売却は確認できず。(算出: 1,000 − 120.9 = 879.1百万ドル。Q2 以降の売却有無は未確認) | 2026-03-31 (上半期の数値も同一) | 10-Q Q1 2026: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926055891/hut-20260331x10q.htm 。別主体: 子会社 American Bitcoin (ABTC) の 2026年上半期 Class A ATM は 7,755,671株、グロス $144.7M: https://www.sec.gov/Archives/edgar/data/0001755953/000119312526329472/abtc-20260630.htm |

---

## 表2 四半期業績 (2024年Q1〜2026年Q2、最新が一番下)

単位: 百万ドル (EPS を除く)。2024年の数値は 2025年版の決算リリースに含まれる前年同期比較値 (再表示後の値) を優先した。

| 四半期 | 総売上 | うちHPC/AIリース・コロケーション売上 | うちビットコイン採掘売上 | その他 | 売上総利益または売上原価 | 営業損益 | 純損益(GAAP) | 希薄化後EPS | 調整後EBITDA(会社定義) | 希薄化後株式数(加重平均) | 出所 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2024Q1 | 約51.9 (算出: 21.8÷(1−0.58)。2025年Q1比で−58%) | 欠損 | 欠損 | Compute 32.1 (前年同期比較値) | 欠損 | 欠損 | 250.7 | 欠損 | 297.0 | 欠損 | 2025 Q1 8-K: https://www.sec.gov/Archives/edgar/data/1964789/000155837025006847/hut-20250508xex99d1.htm |
| 2024Q2 | 35.2 (2025 Q2 リリースの前年同期値) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | −72.2 (2025 Q2 リリースの前年同期値。2024年当時の初出値は −71.9) | 欠損 | −57.5 | 欠損 | 2025 Q2 8-K: https://www.sec.gov/Archives/edgar/data/1964789/000155837025010632/hut-20250807xex99d1.htm ／ 初出値: https://www.theblock.co/news/business/2024-08-13-bitcoin-miner-hut-8-net-loss-in-q2-310966 |
| 2024Q3 | 約43.7 (算出: 83.5÷1.91。2025年Q3比で+91%) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 0.9 (二次: 2025 Q3 比較値) | 欠損 | 5.6 (二次: 2025 Q3 比較値) | 欠損 | 2025 Q3 8-K: https://www.sec.gov/Archives/edgar/data/1964789/000110465925105883/hut-20251104xex99d1.htm ／ 二次: https://www.zacks.com/stock/news/2785897/hut-8-q3-earnings-beat-estimates-revenues-up-y-y-shares-up |
| 2024Q4 | 31.7 (二次: 2025 Q4 記事の前年同期値) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 152.0 (算出: FY2024 331.4(二次) − Q1 250.7 − Q2(−72.2) − Q3 0.9) | 欠損 | 310.6 (算出: FY2024 555.7(二次) − Q1 297.0 − Q2(−57.5) − Q3 5.6) | 欠損 | FY2024 10-K: https://www.sec.gov/Archives/edgar/data/1964789/000155837025001996/hut-20241231x10k.htm (FY売上 162,385千ドルを確認。FY純損益・EBITDA は二次情報) ／ 31.7: https://finviz.com/news/323881/hut-8-q4-earnings-surpass-estimates-revenues-increase-yy |
| 2025Q1 | 21.8 | 欠損 | 欠損 | Compute 16.1 (セグメント)。Power・Digital Infrastructure は減少と記載のみ (数値欠損) | 欠損 | 欠損 | −134.3 | −1.09 (二次: トランスクリプトサイト。市場予想 −0.20) | −117.7 | 欠損 | 2025 Q1 8-K: https://www.sec.gov/Archives/edgar/data/1964789/000155837025006847/hut-20250508xex99d1.htm |
| 2025Q2 | 41.3 | 欠損 | 欠損 | Compute 34.3 ／ Power 5.5 ／ Digital Infrastructure 1.5。デジタル資産利益 217.6 ／ 損失 71.8 | 欠損 | 欠損 | 137.5 | 1.34 (二次: Seeking Alpha) | 221.2 (旧定義。2026年の新定義での比較値は 4.2) | 欠損 | 2025 Q2 8-K: https://www.sec.gov/Archives/edgar/data/1964789/000155837025010632/hut-20250807xex99d1.htm |
| 2025Q3 | 83.5 | 欠損 | 欠損 | Compute 約70 (二次)。デジタル資産利益 76.6 (二次) | 欠損 | 72.6 (二次) | 50.6 | 不一致: 0.43 (Fintool) ／ −0.07 (Zacks) ／ −0.046 (S&P)。未解決 | 109.0 | 欠損 | 2025 Q3 8-K: https://www.sec.gov/Archives/edgar/data/1964789/000110465925105883/hut-20251104xex99d1.htm ／ 二次: https://www.zacks.com/stock/news/2785897/hut-8-q3-earnings-beat-estimates-revenues-up-y-y-shares-up |
| 2025Q4 | 88.5 (算出: FY2025 235.1(二次) − Q1 21.8 − Q2 41.3 − Q3 83.5。二次の 88.49 と一致) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | −301.8 (継続事業ベース・二次。算出: FY −248.0(二次) − (−134.3 + 137.5 + 50.6)。AP 系の −279.7 とは不一致) | 不一致: 0.36 (Zacks) ／ −2.63 ／ −2.66。未解決 | −347.9 (算出: FY −135.4(二次) − (−117.7 + 221.2 + 109.0)) | 欠損 | 2026-02-25 8-K: https://www.sec.gov/Archives/edgar/data/1964789/000110465926019443/hut-20260225x8k.htm ／ 二次: https://www.nasdaq.com/articles/hut-8-posts-loss-q4 |
| 2026Q1 | 約71 (二次: 「about $71M」。正確値は欠損) | 欠損 | 欠損 | Compute 約66 (二次・前年 16.1)。Power 3.74 (前年 4.38、二次) | 欠損 (Compute の粗利率 約64% との二次記載あり。定義未確認) | 欠損 | 総額 −253.1 (10-Q 調整表)。株主帰属分 −219.8 (AP) | 不一致: −1.98 (AP、株主帰属) ／ −0.12 (調整後、二次)。未解決 | −250.5 (10-Q 調整表の先頭列と思われるが列見出し未確認。旧定義の可能性) | 欠損 | Q1 2026 8-K: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926055894/hut-20260506xex99d1.htm ／ 10-Q Q1 2026: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926055891/hut-20260331x10q.htm ／ AP: https://wtop.com/news/2026/05/hut-8-q1-earnings-snapshot/ |
| 2026Q2 | 74.9 (多くの記事。MarketBeat のみ 72.66 と記載し不一致) | 1.3 (連結コロケーション売上・二次)。別途 27.0 は持分法損益 (King Mountain JV 関連、二次) | 欠損 | Compute 72.5 ／ Power 1.2 ／ Digital Infrastructure 1.3 (二次: Quartr 要約) | 欠損 (粗利率は不一致: 47%(前年 64%) と 64%(前年 47%) の二種の二次記述) | 欠損 | −177.1 (連結)。うち未実現デジタル資産損失 −138.6 | 不一致: −1.27 (Blockspace、Benzinga) ／ −0.26 (Earnings Whispers) ／ −1.78 (別記事)。未解決 | 10.4 (BTC 時価評価を除外する新定義) ／ 参考: 新定義での前年同期 4.2。BTC 時価評価を含めた値 −94.6 (二次) | 欠損 | Q2 2026 8-K: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926090041/tm2621890d1_ex99-1.htm ／ 二次: https://blockspace.media/insight/hut-8-q2-2026-earnings-revenue-miss/ ／ https://quartr.com/events/hut-8-corp-hut-q2-2026_ojCm5Qqj |

補足 (表2): 2026年上半期 (算出・二次の値と整合): 売上 約146.0 (二次: 146.0)、純損益 −430.3 (二次) / (算出: −253.1 + −177.1 = −430.2)。

---

## 表3 キャッシュフロー・資本支出

単位: 百万ドル。上半期・通期の行は一部のみ取得。

| 期間 | 営業CF | 設備投資(capex) | 株式報酬(SBC) | 株式発行による調達 | 借入による調達 | 期末現預金 | 出所 |
|---|---|---|---|---|---|---|---|
| 2026Q1 (3か月、期末 2026-03-31) | −27.2 (10-Q: 営業活動による資金支出 27,222千ドル) | 欠損 (投資CF合計は −51.2 と確認。capex 内訳は未確認) | 約50.9 (10-Q 記載) | 普通株 ATM 約120.1 (10-Q 記載) ／ 約120.9 (ATM 記述のグロス値) ・ 子会社 ABTC の Class A ATM 約110.5 | 欠損 (Q1 中の借入は確認できず。River Bend ノートは 2026-04-30 クロージング=Q2) | 欠損 | 10-Q Q1 2026: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926055891/hut-20260331x10q.htm |
| 2026Q2 (3か月、期末 2026-06-30) | 欠損 (二次の FCF −523.9 は期間・定義不明のため不採用。出所: https://www.stocktaper.com/earningsCallSummary/HUT/2026/Q2 ) | 欠損 | 欠損 | 普通株 ATM: Q2 売却は確認できず。ABTC 上半期 Class A ATM 144.7 のうち Q2 分 (算出: 144.7 − Q1 110.5 = 34.2、ABTC 側) | 2026-04-30 River Bend ノート 元本 3,250 ／ 2026年6月 Beacon Point ノート 元本 4,250 (算出: 合計 7,500。元本ベース、手数料控除前) | 流動性 約8.1B (算出なし。Q2 PR 文言: 現金・制限付現金・現金同等物・ビットコイン保有の合計。うち Hut 8 帰属 7.6B、ABTC 帰属 0.4972B) ／ 不一致: 二次要約は「現金・制限付現金 8.1B」と記載 ／ 別の二次では約7B | 8-K Q2 2026: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926090041/tm2621890d1_ex99-1.htm ／ River Bend 8-K: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926049810/tm2612880d1_ex99-1.htm ／ Beacon Point PR: https://hut8.com/news-insights/press-releases/hut-8-closes-usd4-25-billion-of-investment-grade-senior-secured-notes-for-beacon-point-data |
| 2026年上半期 (1〜6月) | 欠損 | 欠損 | 欠損 | 普通株 ATM: 2026年上半期合計 120.9 (グロス、Q1 のみ) ／ ABTC Class A ATM 144.7 | 7,500 (算出: 3,250 + 4,250、元本) | 欠損 | 10-Q Q2 2026: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926090025/hut-20260630x10q.htm |
| 2025年通期 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 未取得 (FY2025 10-K の CF 計算書を未確認) |

---

## 表4 負債の明細 (直近期末 2026-06-30)

| 証券・借入 | 元本 | 金利 | 満期 | 担保・リコース | 転換価格(転換社債) | 出所 |
|---|---|---|---|---|---|---|
| 上級担保付ノート (River Bend、発行体 Hut 8 DC LLC。2026-04-27 プライシング、04-30 クロージング) | 3,250百万ドル | 表面利率 6.192%。会計上の実効金利 6.41% (10-Q) | 2042年 (16.5年で完全償却。15年リースに整合) | 発行体の実質全資産に第1順位担保。Hut 8 Corp. へはノンリコース。格付け BBB− (S&P・Fitch) | 該当なし | 報道 (2026-04-27): https://www.theenergymag.com/news/2026-04-27/hut-fluidstack-ai-louisiana ／ 8-K: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926049810/tm2612880d1_ex99-1.htm ／ 10-Q Q2 2026 (実効金利): https://www.sec.gov/Archives/edgar/data/0001964789/000110465926090025/hut-20260630x10q.htm |
| 上級担保付ノート (Beacon Point、発行体 Beacon Point DC LLC。2026-06-09 プライシング) | 4,250百万ドル | 6.129% (年率、半年払い) | 2042年11月30日 | 第1順位担保。Hut 8 へはノンリコース。格付け Baa2 (Moody's) | 該当なし | プレス: https://hut8.com/news-insights/press-releases/hut-8-closes-usd4-25-billion-of-investment-grade-senior-secured-notes-for-beacon-point-data ／ 価格決定: https://www.benzinga.com/node/53020821 |
| 転換社債 (Coatue ファンド保有分の記載あり。発行日 2024-06-28、発行体 Hut 8 Corp.) | 当初元本 150.0百万ドル。現残高は欠損 (PIK 利息で元本が増加しうる) | 8.00% (四半期払い。PIK または現金) | 当初5年 (算出: 2024-06 + 5年 = 2029年6月頃。延長オプション 最大3年)。二次推定 | 無担保・シニア (10-Q 2026-06-30 の記載) | 16.395ドル (転換株数 最大 9,149,131株) | 2024 8-K: https://www.sec.gov/Archives/edgar/data/1964789/000155837024009418/hut-20240621x8k.htm ／ 二次: https://www.tipranks.com/news/hut-8-nasdaqhut-slips-amid-150m-convertible-note-offering 。2026-06-30 時点の償還・転換・買戻しの有無: 欠損 (10-Q は過去形で記載) |
| その他 (Bitcoin 担保借入ほか) | 欠損 | 借入コストは 9.0% から 7.0% へ低下 (Q1 2026 リファイナンス、二次・PR 要約) | 欠損 | 欠損。Q1 2026 リファイナンスで約3,300 BTC 分の流動性が解放 (二次) | 該当なし | Q1 2026 PR (要約): https://seekingalpha.com/pr/20502566 ／ 二次: https://www.techflowpost.com/en-US/newsletter/121773 |
| River Bend 建設ローン (2025-12 発表時の報道) | 欠損 | 欠損 | 欠損 | 欠損 | 該当なし | 報道 (2025-12): https://decrypt.co/352755/bitcoin-miner-hut-8-stock-soars-7-billion-google-backed-ai-deal |

---

## 表5 AI/HPC の容量と契約 (KPI 時系列)

### 5-A 時系列 (各時点は「開示日」を基準に記載)

| 時点 (開示日) | 稼働中(エネルギー供給済み)のIT容量MW | 建設中MW | 契約済みMW | 契約済み収益総額 | 主要テナント | 年換算契約収益 | 電力の確保量(総MW) | 出所 |
|---|---|---|---|---|---|---|---|---|
| 2025-11-04 (Q3 2025 決算) | 欠損 | 欠損 | 欠損 (AI/HPC リースの記載は確認できず) | 欠損 | 欠損 | 欠損 | 欠損 | https://www.sec.gov/Archives/edgar/data/1964789/000110465925105883/hut-20251104xex99d1.htm |
| 2025-12-17 〜 2026-02-25 (River Bend リース公表。Q4 決算 2026-02-25 時点) | 欠損 | 欠損 | 245 (River Bend) | 7.0B (base term、15年) | Fluidstack (Google LLC が賃料等を支払い保証。報道では Anthropic との提携関連) | 約0.47B/年 (算出: 7.0÷15、単純均等割) | 欠損 (8,500MW は 2025-12-31 時点の開発パイプラインであり確保量ではない) | 8-K 2026-02-25: https://www.sec.gov/Archives/edgar/data/1964789/000110465926019443/hut-20260225x8k.htm ／ リース公表: https://www.datacenterdynamics.com/en/news/hut-8-signs-245mw-capacity-deal-with-fluidstack-as-part-of-multi-gigawatt-partnership-with-anthropic |
| 2026-05-06 (Q1 2026 決算、Beacon Point Phase 1 公表) | 欠損 | 欠損 | 597 (Q1 PR 記載。内訳: 245 + 352 = 597、算出) | 16.8B (算出: 7.0 + 9.8) | Fluidstack (River Bend)。Beacon Point Phase 1 は非公開の高格付け投資適格テナント | 約1.12B/年 (算出: 16.8÷15) | 欠損 | Q1 8-K: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926055894/hut-20260506xex99d1.htm ／ Beacon Point: https://irei.com/news/hut-8-commercializes-first-phase-of-1-gw-beacon-point-ai-data-center-campus-with-15-year-352-mw-it-lease-with-base-term-contract-value-of-9-8b/ |
| 2026-07-20 (Beacon Point 第2リース公表) | 欠損 | 欠損 | 949 (算出: 245 + 704。704 = 352 × 2) | 26.6B (算出: 7.0 + 9.8 + 9.8。二次の 26.6 と一致) | Fluidstack (River Bend)。Beacon Point は同一の非公開テナント (報道で Nvidia との指摘あり・未確認) | 約1.77B/年 (算出: 26.6÷15) | 欠損 (Beacon Point の系統容量 1,000MW は全量契約済みと記載。AEP Texas との相互接続合意) | https://theblock.co/post/408920/hut-8-fully-commercializes-1-gw-texas-ai-campus-with-second-9-8b-lease-as-iren-signs-2-8b-in-contracts-shares-climb-double-digits ／ Nvidia 指摘 (未確認・二次): https://www.marketbeat.com/instant-alerts/price-hut-8-nasdaq-hut-shares-down-76-time-to-sell-2026-09-14/ |
| 2026-08-04 (Q2 2026 決算) | 欠損 (初期データホール納入の目標時期のみ記載: River Bend 2027年Q2、Beacon Point 初期 energization 2027年Q1 (7月PR) / 初期データホール 2027年Q3 (二次要約)) | 1,330 (二次: River Bend と Beacon Point の合計、Quartr 要約。系統容量との関係は未確認) | 949 | 26.6B (算出、同上) | 同上 | 約1.77B/年 (算出、同上) | 欠損 | 8-K Q2 2026: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926090041/tm2621890d1_ex99-1.htm ／ 二次: https://quartr.com/events/hut-8-corp-hut-q2-2026_ojCm5Qqj |

### 5-B 各リース契約ごとの行

| 契約名/拠点 | テナント | MW | 期間 | 契約総額 | 稼働開始時期 | 信用補完 | 建設費(1MWあたり) | 出所 |
|---|---|---|---|---|---|---|---|---|
| River Bend (ルイジアナ州) 15年リース (2025-12-17 公表) | Fluidstack | 245 (IT) | 15年 (base term)。更新オプション込みで総額 $17.7B | 7.0B (base term) | 初期データホール 2027年Q2 (目標) | Google LLC による賃料等の財務債務の支払い保証 (保証上限額は未確認)。Google (Alphabet) は AA+/Aa2 (Barchart の PR 転載による)。別途、運営サービス契約での Google の支払い保証が報じられているが未確定 | 欠損 (プロジェクト費用の公表なし。参考・概算: 3.25B ÷ 0.95 (「資金調達が約95%」との報道) ≈ 3.42B、÷ 245MW ≈ 約13.96百万ドル/MW (算出)) | DCD: https://www.datacenterdynamics.com/en/news/hut-8-signs-245mw-capacity-deal-with-fluidstack-as-part-of-multi-gigawatt-partnership-with-anthropic ／ Barchart PR: https://www.barchart.com/story/news/36663812/hut-8-signs-15-year-245-mw-ai-data-center-lease-at-river-bend-campus-with-total-contract-value-of-7-0-billion ／ 95%: https://www.theenergymag.com/news/2026-04-27/hut-fluidstack-ai-louisiana |
| Beacon Point (テキサス州ヌェセス郡) Phase 1 (2026-05-06 公表) | 非公開 (プレスでは "high-investment-grade" と記載) | 352 (IT) | 15年。トリプルネット (NNN)。更新 5年×3回 | 9.8B (base term) | 初期 energization 2027年Q1 (7月 PR で予定どおりと記載) | 欠損 (テナント非開示。Beacon Point ノートは Baa2、非リコース) | 欠損 (参考・算出: 調達額 4.25B ÷ 352MW ≈ 約12.07百万ドル/MW。建設費ではなく調達額ベース) | https://irei.com/news/hut-8-commercializes-first-phase-of-1-gw-beacon-point-ai-data-center-campus-with-15-year-352-mw-it-lease-with-base-term-contract-value-of-9-8b/ ／ Q1 PR: https://hut8.com/news-insights/press-releases/hut-8-reports-first-quarter-2026-results |
| Beacon Point Phase II (第2リース、2026-07-20 公表) | Phase 1 と同一テナント (同条件) | 352 (IT) | 15年。NNN。更新 5年×3回 | 9.8B (base term)。キャンパス全体の更新込み潜在額 $50.2B | 初期データホール 2028年Q2 (目標) | 欠損 | 欠損 | https://theblock.co/post/408920/hut-8-fully-commercializes-1-gw-texas-ai-campus-with-second-9-8b-lease-as-iren-signs-2-8b-in-contracts-shares-climb-double-digits |

---

## 表6 ビットコイン採掘 KPI (直近6四半期: 2025Q1〜2026Q2)

採掘量・電力コストは全期間で欠損。以下は取得できた断片のみ。

| 四半期 | 採掘BTC数 | ハッシュレート(EH/s) | 1BTCあたり電力コスト | 出所 |
|---|---|---|---|---|
| 2025Q1 (期末 2025-03-31) | 欠損 | 9.3 (期末時点のデプロイ済み; ASIC 更新で Q 比 +79%) | 欠損 | Q1 2025 8-K: https://www.sec.gov/Archives/edgar/data/1964789/000155837025006847/hut-20250508xex99d1.htm ／ 運用更新: https://www.barchart.com/story/news/31744715/hut-8-operations-update-for-march-2025 。保有 BTC 10,264 (期末、二次) |
| 2025Q2 (期末 2025-06-30) | 欠損 | 欠損 | 欠損 | 保有 BTC 10,667 (期末、市場価値 $1.1B、二次): https://www.aap.com.au/aapreleases/globenewswire9507902/ |
| 2025Q3 (期末 2025-09-30) | 欠損 (追跡サイトに 2025年9月の単月 5.0 BTC のみ。低信頼) | 不一致: 26.8 (二次: 合併後の合計と記載) ／ 1.8 (追跡サイト、2025-09-30 時点)。未解決 | 欠損 | 追跡サイト: https://bitcoinminingstock.io/company/hut ／ 保有 BTC 13,696 (2025-09-30、二次): https://www.theblock.co/post/377607/hut-8-joins-rank-top-10-largest-public-bitcoin-holders-over-13000-btc |
| 2025Q4 (期末 2025-12-31) | 欠損 | 欠損 | 欠損 | 保有 BTC 約10,278 (2025-12-31、追跡サイト・二次): https://bitcoinminingstock.io/company/HUT |
| 2026Q1 (期末 2026-03-31) | 欠損 (二次: 採掘の拡大との記載のみ) | 欠損 | 欠損 | 欠損。Q1 2026 PR・10-Q を確認できず: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926055891/hut-20260331x10q.htm |
| 2026Q2 (期末 2026-06-30) | 欠損 | 欠損 | 欠損 | 欠損。Q2 2026 10-Q を確認できず: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926090025/hut-20260630x10q.htm |

---

## 表7 会社ガイダンス・目標 (直近の発表)

売上・EBITDA の通期ガイダンスは検索範囲で確認できず (全行で欠損)。

| 発表日 | 内容 (売上・EBITDA・容量・稼働時期の目標) | 出所 |
|---|---|---|
| 2026-02-25 (Q4 / FY2025 決算) | 売上・EBITDA ガイダンス: 欠損。River Bend (245MW) の納入を 2027年Q2 から開始する目標。開発パイプライン 8,500MW (2025-12-31 時点)。Vega Tier I (205MW) に言及 (稼働時期は欠損) | 8-K: https://www.sec.gov/Archives/edgar/data/1964789/000110465926019443/hut-20260225x8k.htm ／ 二次: https://www.ariva.de/aktien/hut-8-corp-aktie/news/hut-8-reports-fourth-quarter-and-full-year-2025-results-11920586 |
| 2026-05-06 (Q1 2026 決算) | 売上・EBITDA ガイダンス: 欠損。Beacon Point Phase 1 (352MW、$9.8B) を契約、契約済み合計 597MW。River Bend ノート $3.25B がクロージング (期末後)。借入コストを 9.0% から 7.0% へ低下。River Bend の初期データホール目標 2027年Q2 | Q1 PR: https://seekingalpha.com/pr/20502566 ／ https://hut8.com/news-insights/press-releases/hut-8-reports-first-quarter-2026-results |
| 2026-07-20 (Beacon Point 第2リース) | 352MW 追加 (Beacon Point 計 704MW、契約済み合計 949MW)。Beacon Point の初期 energization 2027年Q1。Phase II の初期データホール 2028年Q2。キャンパス全体の更新オプション込み潜在契約額 $50.2B | https://theblock.co/post/408920/hut-8-fully-commercializes-1-gw-texas-ai-campus-with-second-9-8b-lease-as-iren-signs-2-8b-in-contracts-shares-climb-double-digits |
| 2026-08-04 (Q2 2026 決算) | 売上・EBITDA ガイダンス: 欠損。二次要約では River Bend の初期データホール 2027年Q2、Beacon Point 2027年Q3 (7月 PR の energization 2027年Q1 と不一致)。建設中 1,330MW (二次) | 8-K: https://www.sec.gov/Archives/edgar/data/0001964789/000110465926090041/tm2621890d1_ex99-1.htm ／ 二次: https://quartr.com/events/hut-8-corp-hut-q2-2026_ojCm5Qqj |

---

## 表8 株価・コンセンサス

### 8-A 予想値 (出所サイトごと)

| 出所サイト | 年度 | 売上予想平均 | EPS予想平均 | EBITDA予想 | アナリスト数 | 時点 | 出所URL |
|---|---|---|---|---|---|---|---|
| FactSet (鉅亨網経由、中央値) | 2026 | 欠損 | −4.40 | 欠損 | 12 | 欠損 (記事日付不明) | https://news.cnyes.com/news/id/6563269 |
| FactSet (同上) | 2027 | 約571 (中央値、二次) | −2.77 | 欠損 | 12 | 欠損 (記事日付不明) | https://news.cnyes.com/news/id/6563269 |
| Simply Wall St | 2026 | 296 (US$百万) | −5.34 | 欠損 | 14 | 2026年8月の格下げ後 (記事日付は欠損) | https://simplywall.st/stocks/us/software/nasdaq-hut/hut-8/news/things-look-grim-for-hut-8-corp-nasdaqhut-after-todays-downg |
| Tickflow | 2026 | 351 (百万ドル、11社) | −1.00 (7社) | 欠損 | 7 (EPS) / 11 (売上) | 欠損 (スナップショット日不明) | https://tickflow.io/stock/HUT/forecast |
| Tickflow | 2027 | 欠損 | 欠損 (四半期別、各1社のみ) | 欠損 | 1 | 欠損 | https://tickflow.io/stock/HUT/forecast |
| Benzinga | 2026 (Q3 / Q4) | 欠損 | Q3 −1.00 ／ Q4 −1.21 | 欠損 | 欠損 | 2026-10-06 更新 | https://www.benzinga.com/quote/HUT/earnings-forecasts |
| Benzinga | 2027 (Q1 / Q2) | 欠損 | Q1 −1.33 ／ Q2 −2.00 | 欠損 | 欠損 | 2026-10-06 更新 | https://www.benzinga.com/quote/HUT/earnings-forecasts |
| MarketBeat (Maxim Group 単独) | 2026 | 欠損 | −3.69 | 欠損 | 1 | 2026-07-28 | https://www.marketbeat.com/instant-alerts/what-is-maxim-groups-estimate-for-hut-8-q2-earnings-2026-07-28/ |
| MarketBeat (Maxim Group 単独) | 2027 | 欠損 | −14.81 | 欠損 | 1 | 2026-07-28 | https://www.marketbeat.com/instant-alerts/what-is-maxim-groups-estimate-for-hut-8-q2-earnings-2026-07-28/ |
| MarketBeat (別表示・TSE 上場株。不一致) | 2026 / 2027 | 欠損 | −5.27 ／ −20.88 | 欠損 | 1 | 2026-07-28 頃 | https://www.marketbeat.com/instant-alerts/what-is-maxim-groups-forecast-for-hut-8-q2-earnings-2026-07-28/ |
| Zacks (独自コンセンサス) | — | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 未取得 (zacks.com で要確認) |

### 8-B 平均目標株価・レーティング分布

- 平均目標株価 $143.95 (2026-10-02 頃の表示。出所は同時期の MarketBeat 系表示): https://marketchameleon.com/Overview/HUT/Summary/ ／ https://www.marketbeat.com/stocks/NASDAQ/HUT/chart
- 平均目標株価 $144.89、コンセンサス "Buy"、アナリスト 20名 (Strong Buy / Buy) (2026-09-11): https://www.marketbeat.com/instant-alerts/price-hut-8-nasdaq-hut-trading-up-88-heres-why-2026-09-11/
- 平均目標株価 $144.89、内訳 Strong Buy 1 / Buy 17 / Hold 1 (2026-08-14): https://www.marketbeat.com/instant-alerts/hut-8-nasdaqhut-trading-3-higher-heres-why-2026-08-14/
- 平均目標株価 $137.20 (2026-07-28): https://www.marketbeat.com/instant-alerts/hut-8-nasdaqhut-price-target-raised-to-15700-2026-07-28/
- "Moderate Buy"、アナリスト 19名 (Buy 18 / Sell 1)、平均目標株価 $133.10 (2026-07-26): https://www.marketbeat.com/instant-alerts/hut-8-corp-nasdaqhut-receives-consensus-rating-of-moderate-buy-from-analysts-2026-07-26/
- 目標株価の高値 $226.00 ／ 安値 $30.00、コンセンサス "Moderate Buy" (評価スコア 2.89/4)。表示日 2026-07-01: https://www.marketbeat.com/stocks/NYSE/HUT/price-target/

### 8-C 直近の目標株価変更・レーティング変更

| 証券会社 | 変更内容 | 日付 | 出所 |
|---|---|---|---|
| Keefe, Bruyette & Woods | 目標 $138 → $157、Outperform 維持 | 2026-07-28 | https://www.marketbeat.com/instant-alerts/hut-8-nasdaqhut-price-target-raised-to-15700-2026-07-28/ |
| Canaccord | 目標 $70 → $130、Buy 維持 (前回は 2025-12 の $62) | 欠損 (「4週間前」との表示のみ) | https://stockanalysis.com/stocks/HUT (二次) |
| Needham | 目標 $128 → $145、Buy | 欠損 | https://stockanalysis.com/stocks/HUT (二次) |
| Compass Point | 目標 $195 を設定 | 2026-07-22 (二次)。MarketBeat は同額 $195 を Benchmark の引き上げとして記載 (不一致・未解決) | https://stockanalysis.com/stocks/HUT (二次) ／ https://www.marketbeat.com/instant-alerts/price-hut-8-nasdaq-hut-trading-up-88-heres-why-2026-09-11/ |
| Rosenblatt | Buy 維持、目標 $124 | 2026-07-21 | https://stockanalysis.com/stocks/HUT (二次) |
| Piper Sandler | 目標 $93 → $127 | 2026-05-06 | https://stockanalysis.com/stocks/HUT (二次) |
| Benchmark | 目標 $85 を維持、Buy (CFO 面談後) → その後 $195 へ引き上げとの MarketBeat 記載あり (日付欠損・不一致) | 2026-03-24 ／ 欠損 | https://stockanalysis.com/stocks/HUT (二次) ／ https://www.marketbeat.com/instant-alerts/price-hut-8-nasdaq-hut-trading-up-88-heres-why-2026-09-11/ |
| Arete Research | カバレッジ開始 (評価・目標は欠損) | 2026-03-23 | https://www.marketbeat.com/instant-alerts/hut-8-nasdaqhut-coverage-initiated-by-analysts-at-arete-research-2026-03-23/ |
| Maxim Group | 目標株価: 欠損 (EPS 推定のみ、8-B 参照) | 2026-07-28 | https://www.marketbeat.com/instant-alerts/what-is-maxim-groups-estimate-for-hut-8-q2-earnings-2026-07-28/ |
| Weiss Ratings | "sell (d+)" → "sell (d−)" (レーティングのみ) | 2026-05-07 | https://weissratings.com/en/instant-news-alerts/hut-8-corp-hut-down-5-4-is-it-time-to-protect-capital (二次) |
| 不明 (証券会社名欠損) | アナリストによる格下げ (見出しのみ) | 2026-08-07 | https://www.marketbeat.com/instant-alerts/hut-8-nasdaqhut-trading-down-23-on-analyst-downgrade-2026-08-07/ |

---

## 表9 2026年の株価の大きな変動

騰落率の表記は MarketBeat 系見出しの形式に従った。見出しの「up 106」「down 73」などは小数点が省略されている形式と推定し、「(表記 xx、小数点省略と推定)」と記載した。理由は出所に記載がある場合のみ記載し、ない場合は欠損とした。

| 日付 | 騰落率 | 理由 | 出所 |
|---|---|---|---|
| 2026-02-05 | 欠損 (ギャップダウン、幅は欠損) | 欠損 | https://www.marketbeat.com/instant-alerts/hut-8-nasdaqhut-shares-gap-down-heres-what-happened-2026-02-05/ |
| 2026-02-25 (Q4 / FY2025 決算) | 欠損 (見出しは "pops") | 決算。AI 転換の強調 (見出し) | https://finviz.com/news/321949/hut-8-stock-pops-as-earnings-highlight-ai-pivot |
| 2026-03-23 | +10.6% (表記 "up 106"、小数点省略と推定) | 欠損 (同日に Arete Research のカバレッジ開始の記事あり。因果は未確認) | https://www.marketbeat.com/instant-alerts/hut-8-nasdaqhut-shares-up-106-time-to-buy-2026-03-23/ |
| 2026-05-06 (Q1 決算・Beacon Point Phase 1 公表) | +30% (二次の見出し値。終値ベースか未確認) | Beacon Point 352MW / $9.8B のリース。ただし見出しは "second" lease と記載しており、出所の記述に不一致あり | https://www.theenergymag.com/news/2026-05-06/hut-ai-beacon-point |
| 2026-05-19 (低品質サイト) | +9.07% (終値 $105.26 と記載) | 欠損 (暗号資産関連株への関心と記載。確認不可) | https://blissfieldlibrary.org/first-dry/Hut-8-Corp-HUT-Surges-Over-9-as-BitcoinRelated-Momentum-Builds-19-9725 |
| 2026-05-26 (低品質サイト) | +8.9% (終値 $115.33 と記載) | 欠損 | https://fccollege.ac.in/first-dry/Hut-8-HUT-Surges-89-as-Momentum-Builds-Toward-Key-Resistance-23-5439 |
| 2026-05-28 (低品質サイト) | +6.71% (終値 $125.53 と記載) | 欠損 | https://kanyathon.ifim.edu.in/expert-time/Hut-8-Corp-HUT-Surges-Over-6-as-Bullish-Momentum-Builds-23-12789 |
| 2026-07-15 | +6.4% (表記 "up 64"、小数点省略と推定) | 欠損 | https://www.marketbeat.com/instant-alerts/hut-8-nasdaqhut-trading-up-64-still-a-buy-2026-07-15/ |
| 2026-07-27 | −7.3% (表記 "down 73"、小数点省略と推定) | 欠損 | https://www.marketbeat.com/instant-alerts/hut-8-nasdaqhut-trading-down-73-heres-what-happened-2026-07-27/ |
| 2026-07-28 | −3.3% (表記 "down 33"、小数点省略と推定) | 欠損 (同日に KBW の目標引き上げ $138 → $157 の記事あり。因果は未確認) | https://www.marketbeat.com/instant-alerts/hut-8-nasdaqhut-stock-price-down-33-heres-what-happened-2026-07-28/ |
| 2026-07-29 | −12.8% (表記 "down 128"、小数点省略と推定) | 欠損 | https://www.marketbeat.com/instant-alerts/hut-8-nasdaqhut-shares-down-128-heres-why-2026-07-29/ |
| 2026-08-07 | −2.3% (表記 "down 23"、小数点省略と推定) | アナリストによる格下げ (見出し。証券会社名は欠損) | https://www.marketbeat.com/instant-alerts/hut-8-nasdaqhut-trading-down-23-on-analyst-downgrade-2026-08-07/ |
| 日付欠損 (低品質サイト) | −10.16% (終値 $85.57 と記載。オンチェーン系の速報) | 欠損 | https://www.kucoin.com/news/flash/hut-8-corp-hut-shares-drop-10-16-to-85-57 |
| 2026-08-13 | −8.6% (表記 "down 86"、小数点省略と推定) | 欠損 | https://www.marketbeat.com/instant-alerts/hut-8-nasdaqhut-trading-down-86-heres-what-happened-2026-08-13/ |
| 2026-08-14 | +3% (表記 "3 higher") | 欠損 | https://www.marketbeat.com/instant-alerts/hut-8-nasdaqhut-trading-3-higher-heres-why-2026-08-14/ |
| 2026-08-21 | −8.8% (表記 "down 88"、小数点省略と推定) | 欠損 | https://www.marketbeat.com/instant-alerts/hut-8-nasdaqhut-stock-price-down-88-heres-what-happened-2026-08-21/ |
| 2026-08-24 | −1.6% (表記 "down 16"、小数点省略と推定) | 欠損 (Weiss Ratings はインサイダー売却 (直近3か月で約570万ドル) を下落要因の一つとして挙げる。日付は欠損) | https://www.marketbeat.com/instant-alerts/hut-8-nasdaqhut-shares-down-16-heres-why-2026-08-24/ ／ https://weissratings.com/en/instant-news-alerts/hut-8-corp-hut-down-5-4-is-it-time-to-protect-capital |
| 2026-09-09 | −3.6% (表記 "down 36"、小数点省略と推定) | 欠損 | https://www.marketbeat.com/instant-alerts/price-hut-8-nasdaq-hut-shares-down-36-heres-why-2026-09-09/ |
| 2026-09-11 | +8.8% (表記 "up 88"、小数点省略と推定) | 欠損 | https://www.marketbeat.com/instant-alerts/price-hut-8-nasdaq-hut-trading-up-88-heres-why-2026-09-11/ |
| 2026-09-14 | −7.6% (日中、$91.13。出来高は平均比 約30% 増と記載) | 本文の記載: インサイダー売却と直近決算の未達 (特定の材料は未確認) | https://www.marketbeat.com/instant-alerts/price-hut-8-nasdaq-hut-shares-down-76-time-to-sell-2026-09-14/ |

参考: 2026年の断片的な終値 (出所間でばらつきあり)
- 2026-06-13: $118.68 (Motley Fool Australia): https://www.fool.com.au/tickers/nasdaq-hut/
- 2026-07-02: $97.14 (Equibles)。2026-07-15: $87.13 (MarketBeat)。2026-07-21: $105.70 (Robinhood)。2026-07-31: $107.63 (Market Chameleon)
- 2026-09-04 頃: $93.55 (Syfe、年表記なし)
- 2026-10-02: $89.63 (MarketBeat)

---

## データ品質メモ (出所間の不一致・未解決)

1. 2026Q2 EPS: −1.27 (Blockspace、Benzinga) ／ −0.26 (Earnings Whispers) ／ −1.78 (別記事)。
2. 2026Q2 売上: 74.9 (多数) ／ 72.66 (MarketBeat)。
3. 2026Q1 EPS: −1.98 (AP、株主帰属) ／ −0.12 (調整後) ／ +0.10 (Seeking Alpha 表示)。
4. 2025Q4 EPS: 0.36 (Zacks) ／ −2.63 ／ −2.66。2025Q4 純損失: −301.8 (継続事業、二次) ／ −279.7 (AP 系スナップショット)。
5. 2025Q3 EPS: 0.43 ／ −0.07 ／ −0.046。
6. 調整後 EBITDA の定義変更: 2026年の開示では BTC 時価評価を除外。2025年の比較値は旧定義 (Q2 2025: 221.2) と新定義 (4.2) で大きく異なる。
7. 2026Q2 粗利率: 47% (前年 64%) と 64% (前年 47%) の二種の記述。
8. 2026-06-30 流動性: 約8.1B (Q2 PR 文言: BTC を含む) ／ 8.1B を現金・制限付現金とする二次要約 ／ 約7B (別の二次)。
9. 株数: 2026-07-31 表紙 123,259,468 ／ 2026-06-30 貸借対照表 123,190,559。
10. Beacon Point の初期稼働時期: 2027年Q1 energization (7月 PR) ／ 2027年Q3 データホール (Q2 二次要約)。
11. 目標株価 $195: Benchmark (MarketBeat 記載) ／ Compass Point (二次記載)。
12. 52週安値: $18.68 (2026-07 スナップショット) ／ $31.67 (2026-10-02)。後者を採用。
13. 株価 $144.53 (InvestSmart、2026-09-24) と $89.63 (MarketBeat、2026-10-02) の不一致は、通貨・上場所の違いによる可能性が高い (推定)。
14. Maxim の 2026 EPS: −3.69 ／ −5.27 (別上場表示)。FactSet 中央値 −4.40。
15. 騰落率の一部は見出しの小数点省略形式と推定 (表9 参照)。

---

## 取得できなかった重要項目 (要約)

- 10/9 前後の終値、希薄化後株数、表2 の売上総利益・営業損益・加重平均株数、表2 の HPC/コロケーション売上 (四半期別)。
- 2026Q2 の営業CF・capex・SBC、期末現預金の内訳、FY2025 の CF 計算書。
- 2026Q1・Q2 の採掘 BTC 数・ハッシュレート・電力コスト (表6 は全期間で欠損)。
- 稼働中 IT MW・建設中 MW の時系列 (表5)、River Bend の保証上限額、プロジェクト建設費。
- 2026年の売上・EBITDA ガイダンス (表7)。
- Zacks の独自コンセンサス、2026年の株価の大きな変動の理由の大半 (表9)。
- Google 向けワラントの有無 (表1)。
- Coatue 転換社債の現残高と 2026-06-30 時点の状況。
