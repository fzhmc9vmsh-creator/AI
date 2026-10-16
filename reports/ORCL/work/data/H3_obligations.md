# Oracle (NYSE: ORCL) 負債・リース・コミットメント・資本調達 データ表 (H3)

- 取得日: 2026-10-11
- 対象期間: FY2025 Q4 (2025-05-31) 〜 FY2027 Q1 (2026-08-31)
- 単位: 百万USD (特記を除く)。株式数は百万株。
- 表記: 「欠損」= 未取得 (推測で埋めていない)。「算出」= 公表値の加減算・逆算。

## 取得上の注意 (必読)

1. WebFetch は sec.gov に接続できない (`getaddrinfo ENOTFOUND www.sec.gov`)。10-Q / 10-K / 8-K の本文は直接確認しておらず、WebSearch の抜粋と二次情報に依拠した。SEC 由来の値も「一次文書の二次抜粋」扱いで、Tier は 1 としつつ備考に明記している。
2. WebSearch は本ターンの上限 (200回/ターン、他エージェントと共有) に達し、約27回で打ち切られた。以降は検索していない。残りの欠損は追加検索が必要。
3. 矛盾する値は表内に併記した。採用した値は備考欄に記載。
4. Tier: 1 = 会社開示 / 2 = 規制当局・格付会社 (二次経由を含む) / 3 = 報道・アナリスト / 4 = ブログ・SNS・集約サイト。

---

## 表A: 有利子負債の残高推移

定義: 総有利子負債 = Notes payable and other borrowings (流動 + 非流動)、リース負債は含まない。
純有利子負債 = 総有利子負債 − 現金及び短期投資。MS が未取得の時点は現金同等物のみで控除 (備考に明記)。

| 時点 | 総有利子負債 | 現金及び短期投資 | 純有利子負債 | 自己資本 | 備考 | 出典 |
|---|---|---|---|---|---|---|
| FY2025 Q4 (2025-05-31) | 92,568 (算出: 流動 7,271 + 非流動 85,297) | 10,786 (現金同等物のみ, MS 欠損) | 81,782 (算出, 現金のみ控除) | 20,969 (10-K 記載の株主資本合計; NCI 内訳は未確認) | — | S05 |
| FY2026 Q1 (2025-08-31) | 91,315 (算出: 流動 9,079 + 非流動 82,236) | 11,005 (算出: 現金 10,445 + MS 560) | 80,310 (算出) | 24,154 (Oracle 株主; 総計 24,666、NCI 512) | — | S04 |
| FY2026 Q2 (2025-11-30) | 約105,000 (二次報道の「約$105bn」、概算のみ) | 約19,200 (現金のみ、二次) | 約85,800 (算出・概算) | 欠損 | 正確値は Q2 10-Q で要確認 | S49, S48 |
| FY2026 Q3 (2026-02-28) | 134,605 (算出: 流動 9,887 + 非流動 124,718) | 38,455 (現金同等物のみ, MS 欠損) | 96,150 (算出, 現金のみ控除) | 欠損 | 2026年2月の社債 $25bn 発行を含む | S03 |
| FY2026 Q4 (2026-05-31) | 129,541 (流動 7,199 [第三者表] + 非流動 122,342 [XBRL抽出]。帳簿価額 = 額面 130,105 − 割引・発行費 564 と整合) | 31,894 (現金 + MS、10-Q 流動性表の比較列) | 97,647 (算出) | 42,508 (Oracle 株主); 総計 43,056 (NCI 548) | 流動部分は第三者表のみ | S02, S01, S46 |
| FY2027 Q1 (2026-08-31) | 125,337 (算出: 流動 7,625 + 非流動 117,712。二次サイトの「約125.3bn」と一致) | 37,077 (現金 36,369 + MS 708。10-Q 流動性表 37,077 と一致) | 88,260 (算出) | 欠損 | 2026年6-8月に普通株 ATM 約 $20bn 完了 (表B) | S07, S01, S39 |

**参考指標 (同じ期間)**

- FY2026 通期 (10-K 抜粋): 営業CF 31,977 / 設備投資 55,663 / FCF −23,686。FY2025 通期 FCF −394。(S02; 決算要約 S43 と整合)
- FY2027 Q1 (二次情報): 営業CF 約23bn (前年比 +184%)、FCF 約 −5bn (別情報では −5.4bn)、設備投資 約28.5bn (単一の二次情報のみ)。(S40, S42; Tier 3-4)
- 負債指標 (Reuters 引用, 二次): 2026-05-31 時点で借入 / EBITDA 約4.4倍、リース負債込みで約5.7倍。(S36; Tier 3)

**欠損一覧 (表A)**

- 自己資本: 2025-11-30 / 2026-02-28 / 2026-08-31 (10-Q 株主資本計算書の抜粋では合計を確認できず)
- 現金 + MS の内訳: 2025-05-31 (MS)、2025-11-30 (MS)、2026-02-28 (MS)
- 総有利子負債の正確値: 2025-11-30 (Q2 FY26 10-Q 未確認)
- 試した検索語 (ヒットせず): "Oracle quarterly balance sheet total debt cash ... February 28 2026 November 30 2025"、"Oracle total stockholders equity August 31 2026 balance sheet Q1 fiscal 2027"

**出典一覧 (表A)**

| ID | 出典 | URL | 掲載・提出日 | Tier |
|---|---|---|---|---|
| S01 | Oracle 10-Q (2026-08-31期) | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm | 2026-09 (推定) | 1 (抜粋のみ) |
| S02 | Oracle 10-K FY2026 | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526277521/orcl-20260531.htm | 2026-06 (推定) | 1 (抜粋のみ) |
| S03 | Oracle 10-Q (2026-02-28期) | https://www.sec.gov/Archives/edgar/data/1341439/000119312526101045/orcl-20260228.htm | 2026-03 (推定) | 1 (XBRL R2 抜粋) |
| S04 | Oracle 10-Q (2025-08-31期) | https://www.sec.gov/Archives/edgar/data/1341439/000119312525200095/orcl-20250831.htm | 2025-09 (推定) | 1 (抜粋) |
| S05 | Oracle 10-K FY2025 | https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/orcl-20250531.htm | 2025-06 (推定) | 1 (抜粋) |
| S06 | Oracle 10-Q (2025-11-30期) | https://www.sec.gov/Archives/edgar/data/1341439/000119312525315925/orcl-20251130.htm | 2025-12 (推定) | 1 (未直接参照) |
| S07 | Oracle Q1 FY27 決算 Ex 99.1 (8-K) | https://s23.q4cdn.com/440135859/files/content_files/Q127_Form8K_Exhibit99-1_Earnings_Release_Tables_Final_V2.pdf | 2026-09-10 | 1 (列見出し文字化け) |
| S08 | Oracle Q1 FY27 プレスリリース | https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/ | 2026-09-10 | 1 (本文未取得) |
| S36 | Reuters 引用 (CoStar 掲載) | https://www.costar.com/article/606433792/oracle-on-the-hook-for-248-billion-in-data-center-leases-a-move-some-analysts-call-risky | 2026-08 頃 | 3 |
| S39 | sec-api Insights (Q1 FY27 分析) | https://sec-api.io/insights/financial-analysis-of-oracle-q1-fy2027-cloud-backlog-capital-spending-and-scenarios-to-fy2030 | 2026-10-06 | 4 |
| S40 | Beancount blog (Q1 FY27) | https://beancount.io/blog/2026/09/13/oracle-fy2027-q1-earnings-analysis | 2026-09-13 | 4 |
| S42 | Verdict (Q1 FY27 結果) | https://www.verdict.co.uk/oracle-q1-fy27-results/ | 2026-09-10 | 3 |
| S43 | Constellation Research (Q4 FY26) | https://www.constellationr.com/insights/news/oracle-delivers-strong-q4-ai-infrastructure-kills-free-cash-flow | 2026-06-10 | 3 |
| S46 | last10k.com (10-K 転載) | https://last10k.com/sec-filings/orcl/0001193125-26-277521.htm | — | 4 |
| S48 | Fintel / VCP Scanner (四半期 BS) | https://fintel.io/bs/gb/0r1z 、https://www.vcpscanner.com/stock/orcl/balance-sheet/quarterly | 日付不明 | 4 |
| S49 | cryptobriefing (Bloomberg 引用 「約$105bn」) | https://cryptobriefing.com/oracle-shares-debt-load-ai-infrastructure/ | 日付不明 | 3 |

---

## 表B: 2025年以降の資金調達イベント一覧

凡例: 金額は百万USD。「調達主体」はOracle本体か SPV・パートナーか。

| 日付 | 種類 | 金額 | 条件 | 調達主体 | 使途 | 出典 |
|---|---|---|---|---|---|---|
| 2025-09-24 (価格決定・報道日) | 社債 (シニア無担保) | 18,000 | 6トランシェ (報道により差異あり)。40年債は国債比 T+137bp (当初 IPT T+165bp)。変動金利1本は組成中に除外。3年 $3.0bn (2030年9月満期、二次情報)。他のクーポン・スプレッドは欠損。応募ピーク約88bn (Bloomberg) / 約90bn (別解説) | Oracle 本体 | 未確認 | S16, S17 |
| 2026-02 (発表 2026-02-01、価格決定日は欠損) | 社債 (シニア無担保、IG) | 25,000 | 8トランシェ。満期 2029〜2066年 (3〜40年)。応募ピーク約129.45bn (約4.3倍) / 最終約108.64bn (単一トレード報道、未確認)。新発コンセッション −0.86bp (単一情報源)。Fitch 新発債 BBB (2026-02-02)。トランシェ別クーポン・スプレッドは欠損 | Oracle 本体 | GCP (Fitch 要約: 設備投資・借入返済・買収を含む) | S13, S14, S15, S28, S29 |
| 2026-02-01 (発表) / 2026-02-05 (定款届出) | 強制転換優先株 6.50% Series D Mandatory Convertible Preferred (預託株 Depositary Shares) | 5,000 (額面。50,000株 × 100,000 の清算優先権から算出) / 手取り 4,953.6 | 年率 6.50%、配当は 1/15・4/15・7/15・10/15 (2026-04-15 〜 2029-01-15)。転換比率 499.8126〜624.7657 普通株/優先株1株。預託株 100,000,000 口 × $50。主幹事は Citigroup (二次)。 | Oracle 本体 | GCP (Fitch 要約) | S11, S09, S28, S29 |
| 2026-02-02 (契約) → 2026年6-8月 (完了) | 普通株 ATM プログラム (上限) | 20,000 (上限。完了額 $20bn は二次報道、10-Q の株主資本計算書では ATM 発行 19,909) | 上限 $20bn、手数料は売却額の最大 0.5%。エージェントは Citigroup (二次)。Q1 FY27 で完了。発行株数は欠損 | Oracle 本体 | OCI 容量拡大 | S12, S58, S09, S01 |
| 2026-02-01 (発表) | 資金調達計画 (暦年 2026) | 45,000〜50,000 (総額・グロス) | 約半分が株式・株式連動、残りが債務。2026年中の社債発行は今回の1回のみで追加予定なし。取締役会承認。IG 格付の維持を明言。 | Oracle 本体 | OCI 容量拡大 | S09 (本文未取得、検索抜粋) |
| 2026-06-10 (Q4 FY26 決算) | 資金調達計画 (FY2027) | 40,000 (うち ATM 20,000) | 債務 + エクイティの合計。残り 20,000 の内訳は欠損 | Oracle 本体 | 欠損 | S10 (抜粋未取得), S43 |
| 2025-01 (報道) | 銀行ローン (JPMorgan 建設融資、Blue Owl 系ベンチャー、テキサス州 Abilene) | 2,300 (報道) | 欠損 (JPMorgan 建設融資) | SPV・パートナー (Blue Owl / Crusoe) | データセンター建設 | S19, S20 |
| 日付不明 (報道) | プロジェクトファイナンス: Vantage (ウィスコンシン州 Port Washington、OpenAI Stargate 向け、Oracle がテナントとの報道) | 38,000 (報道、大口シンジケート) | 主幹事 JPMorgan・MUFG。参加 Wells Fargo、BNP Paribas、Goldman、SMBC、SocGen。当初価格は米国ベンチマーク +約2.5pp。初報時点で銀行・Oracle・OpenAI は未確認 | SPV・デベロッパー (Vantage) | データセンター建設 | S18 |
| 日付不明 (報道) | プロジェクトファイナンス: Crusoe Abilene (テキサス州)、Oracle がテナントとの報道 | 11,600 (Crusoe の負債 + 株式、報道) | 欠損。Blue Owl JV 3,400 は別途報道 | Crusoe / Blue Owl JV の SPV | データセンター建設 | S20, S19 |
| 2025-12-17 (CNBC 報道) | プロジェクト (Michigan、Saline Township、約 $10bn / 1GW、OpenAI 向け) | 10,000 (プロジェクト規模。融資は未確定) | Blue Owl が出資見送り (債務条件)。Blackstone との交渉を報道、合意なし。Oracle は報道内容を否定 | 欠損 (出資者未確定) | データセンター建設 | S21, S22 |
| 2026-09-24 (Bloomberg 報道、二次) | プロジェクト (New Mexico、Project Jupiter、Doña Ana County、$18bn 規模。開発 Stack Infrastructure (Blue Owl 系)、Oracle がテナント) | 18,000 (プロジェクト規模。融資額 $18bn は Tier 4 のブログ) | Oracle が電力遅延を理由に不可抗力通知 (報道)。Oracle は「計画どおり」と発言 (二次)。融資の条件は欠損 | SPV (Stack / Blue Owl 系) | データセンター建設 | S23, S24 |
| 2025-12 (アナリスト推計) | 借入の推計 (KeyBanc) | 100,000 (推計の上限。実績ではない) | 欠損 | Oracle 本体 (推計) | 建設資金 | S49 |

**注記**
- FY2026 中の社債発行 $43.0bn (10-K 抜粋) は、2025-09 の $18bn と 2026-02 の $25bn の合計と整合する (算出)。
- 2026-02 の普通株 ATM 完了 ($20bn) と MCP ($5bn) を足すと、暦年 2026 計画の株式側 約 $25bn、債務側 $25bn で計 約 $50bn となる (算出。Oracle の公式な総括ではない)。
- 「2026年9月に 100mln 預託株の発行」とする二次サイトの見出しは、上記 Feb 2026 の MCP 預託株と同一のものと判断した。日付は誤記と思われる。

**欠損一覧 (表B)**

- 2025-09 および 2026-02 の社債: トランシェ別のクーポン・スプレッド・年限別金額 (424B2 の価格決定補足書で要確認)
- 2026-02 社債の正確な価格決定日
- ATM の発行株数・平均価格 (Q1 FY27)
- MCP の価格条件 (Oracle 文書の本文未取得)
- Oracle 本体の 2026 年銀行ローン (有無を含む)
- Vantage の完了状況、Michigan の出資者、Jupiter の融資条件・期間
- FY2027 $40bn のうち債務 / 株式の内訳
- Q1 FY27 中の社債発行の有無

試した検索語 (ヒットせず): "Oracle pricing supplement 424B2 senior notes due 2029 2031 2036 2046 2066 coupon" (検索上限のため未実施)、"Project Jupiter New Mexico $18 billion loan Stack Infrastructure" (同上)、"Vantage Frontier Shackelford ... debt closed 2026" (同上)

**出典一覧 (表B)**

| ID | 出典 | URL | 掲載日 | Tier |
|---|---|---|---|---|
| S09 | Oracle 財務計画プレスリリース | https://www.oracle.com/news/announcement/oracle-announces-equity-and-debt-financing-plan-2026-02-01/ | 2026-02-01 | 1 (本文未取得) |
| S10 | Oracle Q4 FY26 決算プレスリリース | https://s23.q4cdn.com/440135859/files/doc_earnings/2026/q4/earnings-result/4q26-pressrelease-final.pdf | 2026-06 | 1 (未取得、Constellation 経由) |
| S11 | Oracle 8-K (MCP 定款届出) | https://www.sec.gov/Archives/edgar/data/1341439/000119312526039344/d63638d8k.htm | 2026-02-05 頃 | 1 (抜粋) |
| S12 | Oracle 424B5 (ATM 目論見書補足) | https://www.sec.gov/Archives/edgar/data/1341439/000119312526037818/d60756d424b5.htm | 2026-02 | 1 (検索ヒット、本文未確認) |
| S13 | Freshfields ニュース | https://www.freshfields.com/en/our-thinking/news/news-search/2026/02/freshfields-advises-oracle-on-$50bn-in-sec-registered-offerings | 2026-02 | 3 |
| S14 | Simpson Thacher ニュース | https://www.stblaw.com/about-us/news/view/2026/02/09/simpson-thacher-represents-underwriters-and-agents-in-$50-billion-of-debt-and-equity-offerings-by-oracle-corporation | 2026-02-09 | 3 |
| S15 | トレード報道 (オーダーブック、単一ソース) | https://informaconnect.com/igm/article/big-volume-from-a-thin-calendar (出典の特定は推定) | 日付不明 | 3 (未確認) |
| S16 | Bloomberg 記事 | https://www.bloomberg.com/news/articles/2025-09-24/oracle-looks-to-raise-15-billion-from-corporate-bond-sale | 2025-09-24 | 3 |
| S17 | Treasury & Risk 記事 | https://www.treasuryandrisk.com/amp/2025/09/24/oracle-raises-18-billion-in-second-biggest-bond-sale-this-year/ | 2025-09-24 | 3 |
| S18 | DCD (JPMorgan・MUFG 主幹事 $38bn) | https://www.datacenterdynamics.com/en/news/jpmorgan-chase-and-mitsubishi-ufj-lead-38bn-debt-package-for-oracle-linked-data-centers-report/ | 日付不明 | 3 |
| S19 | DCD (Crusoe・Blue Owl JV $3.4bn) | https://www.datacenterdynamics.com/en/news/crusoe-signs-34bn-joint-venture-with-blue-owl/ | 日付不明 | 3 |
| S20 | Nasdaq (Crusoe $11.6bn) | https://www.nasdaq.com/articles/startup-crusoe-nets-116b-fresh-financing-massive-new-openai-data-center | 日付不明 | 3 |
| S21 | CNBC (Blue Owl Michigan 見送り) | https://www.cnbc.com/2025/12/17/oracle-stock-blue-owl-michigan-data-center.html | 2025-12-17 | 3 |
| S22 | DCD (Michigan 見送り) | https://www.datacenterdynamics.com/en/news/blue-owl-opts-not-to-fund-oracles-10bn-michigan-data-center/ | 日付不明 | 3 |
| S23 | progressiverobot (Jupiter 不可抗力、Bloomberg 引用) | https://www.progressiverobot.com/2026/09/25/oracle-blue-owl-project-delay-ai-financing/ | 2026-09-25 | 4 |
| S24 | r40 (Jupiter 融資の引用) | https://r40.io/news/orcl-18bn-jupiter-loan-is-the-landlords/ | 日付不明 | 4 |
| S58 | techi (ATM 完了の Oracle 引用) | https://www.techi.com/oracle-backlog-664-billion-equity-funding-reversal/ | 日付不明 | 3 |
| S49 | cryptobriefing (KeyBanc 推計) | https://cryptobriefing.com/oracle-shares-debt-load-ai-infrastructure/ | 日付不明 | 3 |

---

## 表C: 満期ラダー

10-K FY2026 の債務注記にある将来元本支払の表は未取得。以下は二次情報・第三者表からの断片のみ。

| 年度 (FY, 6/1〜5/31) | 満期を迎える元本 | 備考 | 出典 |
|---|---|---|---|
| FY2027 | 欠損 | 流動部分 7,199 (2026-05-31 時点、第三者表。利息・その他借入を含む可能性あり) | S02 / S46 (第三者表) |
| FY2028 | 欠損 | — | — |
| FY2029 | 欠損 | 2028年8月満期 1,500 (FY2025 発行分、二次情報・未確認) | 二次 (出典特定不足) |
| FY2030 | 欠損 | 2029年9月満期 1,500 (FY2025 発行分、二次情報・未確認) | 二次 (出典特定不足) |
| FY2031 | 欠損 | 2030年9月満期 3,000 (2025-09 発行分、二次情報・未確認) | S16, S17 (二次) |

**欠損一覧 (表C)**: FY2027〜FY2031 の正式な元本表。検索語 "Oracle 10-K 2026 scheduled maturities of notes payable ... principal payments table" はヒットせず。

**出典一覧 (表C)**: S02 (Tier 1、抜粋未確認)、S46 (Tier 4)、S16・S17 (Tier 3、満期の記載は確認できず)。

---

## 表D: リース関連

| 時点 | オペレーティングリース負債 | ファイナンスリース負債 | 未開始リース総額 | 期間・開始時期 | 出典 |
|---|---|---|---|---|---|
| 2025-08-31 | 欠損 | 欠損 | 99,800 (二次。10-Q 記載とされる) | 欠損 | S36, S37 (二次) |
| 2025-11-30 | 欠損 | 欠損 | 約248,000 (Bloomberg 2025-12 報道、10-Q 記載とされる) | 欠損 | S35 |
| 2026-05-31 | 約30,189 (算出・要確認: Reuters 引用の総額 37,890 − ファイナンス 7,701。総額の解釈に依存) | 7,701 (10-K 抜粋) | 260,000 (10-K 記載。ほぼ全てデータセンター) | 開始は 2026年 Q1 FY27 〜 FY2029、期間 15〜19年。保証 (借入の保証、最大 3,300、2026年9月満期、10-K 記載) | S02, S36, S38 |
| 2026-08-31 | 34,621 (10-Q 抜粋) | 9,185 (10-Q 抜粋) | 288,000 (10-Q 記載、二次) | 開始は 2026年 Q2 FY27 〜 FY2029、期間 15〜19年。貸借対照表に計上されない | S01, S37, S39 |

**参考 (総額・RPO)**

- 認識済みリース負債 総額: 2026-05-31 37,890 (Reuters 引用、Tier 3) / 2026-08-31 43,806 (算出: 34,621 + 9,185。第三者分析 43.81bn と一致)
- 残存履行義務 (RPO、purchase obligations ではない): 2025-08-31 455,000 (10-Q の前年比較、二次) / 2026-08-31 664,000 (10-Q・プレス、二次)。出典 S01, S07, S41

**purchase obligations (非解約購入債務)**: 欠損。(試した検索語 "Oracle purchase obligations 10-K 2026 non-cancelable commitments" は未実施。検索上限)

**欠損一覧 (表D)**

- オペレーティングリース負債: 2025-08-31、2025-11-30、2026-02-28、2026-05-31 (正式値)
- ファイナンスリース負債: 2025-08-31、2025-11-30、2026-02-28
- 未開始リースの 2026-02-28 時点の値
- 2026-08-31 の 10-Q 原文の未確認 (10-Q 抜粋の 288,000 は二次情報。10-K 260,000 と比べ増加だが、一部の二次情報は 248,000 を「前の 10-Q の値」とするなど不一致あり)
- 3,300 の保証が 10-Q に残るか: 一つの情報源は「10-Q に記載なし」、別の情報源は「含まれる」としており不一致

**出典一覧 (表D)**

| ID | 出典 | URL | 掲載日 | Tier |
|---|---|---|---|---|
| S01 | Oracle 10-Q (2026-08-31期) | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm | 2026-09 (推定) | 1 (抜粋) |
| S02 | Oracle 10-K FY2026 | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526277521/orcl-20260531.htm | 2026-06 (推定) | 1 (抜粋) |
| S07 | Oracle Q1 FY27 決算 Ex 99.1 | https://s23.q4cdn.com/440135859/files/content_files/Q127_Form8K_Exhibit99-1_Earnings_Release_Tables_Final_V2.pdf | 2026-09-10 | 1 |
| S35 | Advisor Perspectives (Bloomberg 引用) | https://www.advisorperspectives.com/articles/2025/12/17/oracles-248-billion-rent-ai-bombshell | 2025-12-17 | 3 |
| S36 | CoStar (Reuters 引用) | https://www.costar.com/article/606433792/oracle-on-the-hook-for-248-billion-in-data-center-leases-a-move-some-analysts-call-risky | 2026-08 頃 | 3 |
| S37 | The Star (Reuters 引用) | https://www.thestar.com.my/tech/tech-news/2026/08/05/ai-data-centre-race-builds-1-trillion-lease-burden-for-big-tech | 2026-08-05 | 3 |
| S38 | r40 (10-K のリース引用) | https://r40.io/blog/orcl-260bn-of-leases-off-the-balance-sheet/ | 日付不明 | 4 |
| S39 | sec-api Insights | https://sec-api.io/insights/financial-analysis-of-oracle-q1-fy2027-cloud-backlog-capital-spending-and-scenarios-to-fy2030 | 2026-10-06 | 4 |
| S41 | cryptobriefing (Q1 FY27、RPO 664bn) | https://cryptobriefing.com/oracle-q1-fy27-earnings-revenue-rpo/ | 2026-09-10 以降 | 3 |

---

## 表E: 格付・クレジット指標

### 格付

| 日付 | 機関 | 指標 | 格付・見通し | 変更内容 | 出典 |
|---|---|---|---|---|---|
| 2026-02-02 | Fitch | 長期 IDR / 短期 IDR | BBB / F2、見通し Stable | 新発社債に BBB を付与、IDR を据え置き (affirm) | S28, S29 (Tier 2・二次経由) |
| 2026-07-09 | S&P | 長期 ICR / 短期 | BBB- (BBB から引き下げ) / A-3 (A-2 から)、見通し Stable | AI 投資に伴う引き下げ。S&P のアナリストは「レバレッジが 4.5 倍超で継続すれば再引き下げの可能性」と指摘 | S25, S26 (Tier 2・二次経由) |
| 2026-09 頃 (推定、日付未確定) | Moody's | 長期 | Baa2、見通し Negative | 株式発表に伴う格付確認。見通しは Negative のまま | S27 (Tier 2・二次経由) |
| 欠損 | S&P | 長期 | BBB (引き下げ前)、見通し欠損 | 引き下げ前の見通し欠損 | — |
| 欠損 | Moody's | 長期 | 見通し Negative への変更日欠損 | 変更理由・前の見通し欠損 | S52 (Tier 3、記事本文未確認) |
| 欠損 | Fitch | 長期 | 2025 年以前の格付・見通し欠損 | — | — |

- S&P 2026-07 の注記: S&P は FY2027 の FOCF 赤字を約 $42bn と予想、調整後レバレッジは FY2027 約 4.4 倍 (S25、S36)。
- Moody's の注記: レバレッジは一時的に 5 倍近くまで上がり得る (Bloomberg 経由、S52)。
- Fitch の注記: FY2026 のレバレッジ見通しは 3.5 倍超、FY2027〜2028 は低下見込み。FCF 見通し (配当前) は FY2026 −26bn 超、FY2027 −18bn (二次、S28・S29)。実績 FY2026 FCF は −23.7bn。

### 5年 CDS スプレッド (bp、ICE データを引用する二次情報)

| 日付 | 水準 (bp) | 備考 | 出典 |
|---|---|---|---|
| 2025-09 | 欠損 | — | — |
| 2025-11 上旬 (記事により相違) | 約80 / 約108 | 80 は 11-20 記事、108 は Spinel。未確定 | S30, S34 |
| 2025-11 下旬 | 約125 | 2022 年以来の高水準 (ICE、Bloomberg 経由) | S59, S60 |
| 2026-01-01 (年初) | 約144 | 年初水準 (二次) | S32 (Tier 4) |
| 2026-03-27 | 198.18 | 当時の過去最高 (二次) | S32, S33 |
| 2026-04 (頃) | 約198 | 記録 (Spinel)。日付は 03-27 と食い違う | S34 |
| 2026-07-17 | 198.23 | 過去最高の終値 (金曜) | S33 |
| 2026-07-20 | 約203 (約2.03%) | 2008年のデータ開始以来の最高 (ICE、Bloomberg 経由)。KuCoin は 07-24 と表記 | S32, S33 |

- 2025 年 7 月 (2025 年中頃) との比較は「約 4 倍」という定性記述のみ。数値は欠損。

**欠損一覧 (表E)**: Moody's の格付履歴 (2025 年以降の変更日)、S&P の引き下げ前の見通し、Fitch の 2025 年以降の変更履歴、CDS の 2025-09 水準、2026-01-01 の正確な値、Moody's 見通しの変更日

**出典一覧 (表E)**

| ID | 出典 | URL | 掲載日 | Tier |
|---|---|---|---|---|
| S25 | ppc.land (S&P 引き下げ) | https://ppc.land/s-p-cuts-oracle-to-bbb-as-ai-buildout-widens-cash-deficit-to-42bn/ | 2026-07 (記事内 07-09) | 4 |
| S26 | computing.co.uk (格付引き下げ) | https://www.computing.co.uk/news/2026/ai/oracle-under-pressure-after-ratings-downgrade-over-ai-expansion | 2026 (日付不明) | 3 |
| S27 | Newsquawk (Moody's 確認) | https://www.newsquawk.com/headlines/moodys-affirms-oracles-orcl-baa2-rating-on-equity-announcement-outlook-remains-negative | 2026-09 頃 (推定) | 2 (二次経由) |
| S28 | Newsquawk (Fitch BBB、Stable) | https://www.newsquawk.com/headlines/fitch-rates-oracles-orcl-senior-notes-offering-bbb-and-affirms-idr-with-outlook-stable | 2026-02-02 頃 | 2 (二次経由) |
| S29 | Teleborsa (Fitch 確認) | https://www.teleborsa.it/News/2026/02/02/oracle-accelera-nel-premarket-su-conferma-rating-da-parte-di-fitch-nonostante-maxi-bond-per-cloud-e-ai-107.html | 2026-02-02 | 2 (二次経由) |
| S30 | Treasury & Risk (CDS 市場) | https://www.treasuryandrisk.com/amp/2025/11/20/boom-in-oracle-cds-market-shows-investors-want-hedge-against-ai-crash/ | 2025-11-20 | 3 |
| S32 | StartupFortune (CDS 記録) | https://startupfortune.com/oracles-default-insurance-costs-just-beat-its-2008-financial-crisis-record/ | 2026-07-21 | 4 |
| S33 | KuCoin flash (CDS 記録) | https://www.kucoin.com/news/flash/oracle-s-5-year-cds-hits-record-high-sparking-investor-concern | 2026-07-24 (記載) | 4 |
| S34 | Spinel Substack (CDS) | https://spinelcapital.substack.com/p/oracle-ai-credit | 2026-07 頃 | 4 |
| S52 | Bloomberg Law (Moody's、格付関連の要約) | https://news.bloomberglaw.com/financial-accounting/oracle-risks-falling-behind-in-ai-race-as-spending-binge-bites | 日付不明 | 3 |
| S59 | TechSpot (CDS 3年高値) | https://www.techspot.com/news/110441-oracle-credit-risk-hits-three-year-high-ai.html | 2025-11 頃 | 3 |
| S60 | FX Leaders (CDS 11-27) | https://www.fxleaders.com/news/2025/11/27/oracle-faces-193-rout-as-traders-bet-big-on-default-protection-echoing-morgan-stanleys-alarm/ | 2025-11-27 | 4 |

---

## 表F: 株式数・株主還元

### 加重平均株式数・株式報酬

| 期間 | 指標 | 値 | 単位 | 出典 | Tier | 備考 |
|---|---|---|---|---|---|---|
| FY2024 | 加重平均株式数 | 2,823 | 百万株 | S47 | 4 | 基本・希薄化の区別が不明 |
| FY2025 | 加重平均株式数 (希薄化後) | 2,866 | 百万株 | S47, S46 | 4 | — |
| FY2026 | 加重平均株式数 (基本) | 2,860 | 百万株 | S47, S46 | 4 | — |
| FY2026 | 加重平均株式数 (希薄化後) | 2,914 | 百万株 | S47, S46 | 4 | — |
| 2025-08-31 期 (FY2026 Q1) | 希薄化後株数 (算出) | 約 2,901 | 百万株 | S42 | 3 | 算出: 普通株主帰属純利益 2,930 ÷ 希薄化後 EPS 1.01 |
| 2026-08-31 期 (FY2027 Q1) | 希薄化後株数 (算出) | 約 3,000 | 百万株 | S42, S07 | 3 | 算出: 普通株主帰属純利益 4,680 ÷ 希薄化後 EPS 1.56 (端数の影響あり) |
| FY2024 | SBC (キャッシュフロー加算項目) | 3,974 | 百万USD | S47, S46 | 4 | — |
| FY2025 | SBC | 4,674 | 百万USD | S47, S46 | 4 | — |
| FY2026 | SBC | 4,811 | 百万USD | S47, S46 | 4 | — |

**欠損**: 四半期別の基本・希薄化後株数 (FY2025 Q1 〜 FY2027 Q1)、期末発行済株式数、四半期 SBC。

### 配当・自社株買い・新株発行

| 日付・期間 | 項目 | 値 | 出典 | Tier | 備考 |
|---|---|---|---|---|---|
| 2026-03-10 発表 (支払 2026-04-24、基準日 04-09) | 普通株 配当 | 0.50 / 株 (四半期) | S45 | 4 | FY2026 Q4 |
| 2026-07 (基準日 07-10、支払 07-24) | 普通株 配当 | 0.50 / 株 | S46 | 4 | FY2027 Q1 |
| 2026-09 発表 (基準日 10-09、支払 10-23) | 普通株 配当 | 0.50 / 株 (宣言済み) | S01 | 1 | FY2027 Q2 |
| 2026年の各四半期 | 強制転換優先株 配当 | 1,625 / 優先株 1 株 (四半期) | S01 | 1 | 6.50% × 100,000 ÷ 4 (算出と一致) |
| FY2027 Q1 (2026-06〜08) | 自社株買い | 0 (株) | S01 | 1 | 期中の買戻しなし |
| FY2026 Q1 (前年同期比較) | 自社株買い | 0.4 百万株 / 93 百万USD | S01 | 1 | 10-Q の前年比較 |
| 2026-08-31 時点 | 自社株買い残枠 | 約 6,300 | S01 | 1 | 期限なし |
| FY2027 Q1 (2026-02-02 契約) | 普通株 ATM 発行 | 20,000 (総額、手数料前) / 19,909 (株主資本計算書) | S01, S58, S12 | 1 / 3 | 発行株数は欠損 |
| 2026-02 (発行) | 強制転換優先株 (MCP) | 50,000 株 (預託株 100,000,000 口) | S02, S11 | 1 | 手取り 4,953.6 |
| 転換時 (算出) | MCP 転換による普通株 | 約 24.99 〜 31.24 百万株 | S11 (転換比率から算出) | 1 (算出) | 50,000 × 499.8126 〜 50,000 × 624.7657。転換日は欠損 (最終配当日 2029-01-15 と関連の可能性、未確認) |

**欠損**: FY2026 の通期自社株買い総額、FY2026 の配当総額、ATM の発行株数・平均価格、四半期配当の FY2026 Q1〜Q3 (個別の確認は未実施)

**出典一覧 (表F)**

| ID | 出典 | URL | 掲載・提出日 | Tier |
|---|---|---|---|---|
| S01 | Oracle 10-Q (2026-08-31期) | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm | 2026-09 (推定) | 1 (抜粋) |
| S02 | Oracle 10-K FY2026 | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526277521/orcl-20260531.htm | 2026-06 (推定) | 1 (抜粋) |
| S07 | Oracle Q1 FY27 Ex 99.1 | https://s23.q4cdn.com/440135859/files/content_files/Q127_Form8K_Exhibit99-1_Earnings_Release_Tables_Final_V2.pdf | 2026-09-10 | 1 (列見出し文字化け) |
| S11 | Oracle 8-K (MCP 定款) | https://www.sec.gov/Archives/edgar/data/1341439/000119312526039344/d63638d8k.htm | 2026-02-05 頃 | 1 (抜粋) |
| S12 | Oracle 424B5 (ATM) | https://www.sec.gov/Archives/edgar/data/1341439/000119312526037818/d60756d424b5.htm | 2026-02 | 1 (検索ヒット) |
| S42 | Verdict (Q1 FY27 EPS) | https://www.verdict.co.uk/oracle-q1-fy27-results/ | 2026-09-10 | 3 |
| S45 | MarketBeat (配当) | https://www.marketbeat.com/instant-alerts/oracle-corporation-nyseorcl-announces-quarterly-dividend-of-050-2026-03-11/ | 2026-03-11 | 4 |
| S46 | last10k.com (10-K 転載) | https://last10k.com/sec-filings/orcl/0001193125-26-277521.htm | — | 4 |
| S47 | AlphaQuery (株式数・SBC) | https://www.alphaquery.com/stock/ORCL/fundamentals/annual/weighted-average-shares-outstanding-diluted | 日付不明 | 4 |
| S58 | techi (ATM 完了の引用) | https://www.techi.com/oracle-backlog-664-billion-equity-funding-reversal/ | 日付不明 | 3 |

---

## 表G: 有形固定資産と減価償却の会計方針

### サーバー・ネットワーク機器の耐用年数の変更履歴

| 変更日 (期首) | 変更前 | 変更後 | 営業費用への影響 (減価償却) | 純利益への影響 | 出典 | Tier |
|---|---|---|---|---|---|---|
| FY2023 期首 (2022-06-01) | 4 年 | 5 年 (サーバー) | −434 (FY2023 の営業費用を減少) | 欠損 | S05 (FY2025 10-K の記載)、S51 (FY2023 Financial Report) | 1 (抜粋) |
| FY2025 期首 (2024-06-01、Q1 FY25 に評価完了) | 5 年 | 6 年 (サーバー・ネットワーク機器) | −733 | +573 (希薄化後 1 株あたり +0.20) | S05 | 1 (抜粋) |
| FY2026 / FY2027 | 欠損 | 欠損 (変更の有無を検索で確認できず) | 欠損 | 欠損 | — | — |

- 営業利益への影響: 減価償却費は営業費用に計上されるため、営業費用の減少額がそのまま営業利益の増加になる (会計上の帰結による算出)。原文で営業利益への影響を明記しているかは未確認。

### 建物・PP&E

| 項目 | 値 | 出典 | Tier | 備考 |
|---|---|---|---|---|
| 建物の耐用年数 | 欠損 | — | — | 未検索 |
| PP&E 総額・純額 (2025-05-31 〜 2026-08-31) | 欠損 | — | — | 未検索 |
| 設備投資 (キャッシュフロー計算書、年度) | FY2026: 55,663 (10-K 抜粋) / FY2025: 約21.2bn (二次) | S02, S44 | 1 / 3 | FY2027 ガイダンス 90〜95bn (二次、S25・S42) |

**欠損一覧 (表G)**: 建物の耐用年数、PP&E 総額・純額の推移、FY2026・FY2027 の耐用年数変更の有無、FY2023 の変更時点での純利益への影響額

**出典一覧 (表G)**

| ID | 出典 | URL | 掲載日 | Tier |
|---|---|---|---|---|
| S05 | Oracle 10-K FY2025 | https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/orcl-20250531.htm | 2025-06 (推定) | 1 (抜粋) |
| S51 | Oracle 10-K FY2023 (Financial Report) | https://www.sec.gov/Archives/edgar/data/1341439/000095017023028914/Financial_Report.xlsx | 2023-06 (推定) | 1 (抜粋) |
| S02 | Oracle 10-K FY2026 | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526277521/orcl-20260531.htm | 2026-06 (推定) | 1 (抜粋) |
| S44 | Fortune (FCF、設備投資の報道) | https://fortune.com/2026/03/10/oracle-best-quarter-negative-free-cash-flow-ai-spending/ | 2026-03-10 | 3 |

---

## 全体の欠損サマリー

- 表A: 自己資本 3時点、現金+MS 3時点、Q2 FY26 の正確な負債
- 表B: 社債のトランシェ別クーポン・スプレッド、2026-02 の価格決定日、ATM 株数、MCP 条件、Vantage・Michigan・Jupiter の完了状況・条件
- 表C: 満期ラダー (10-K 注記) 全体
- 表D: オペレーティングリース (2026-05-31 正式値)、purchase obligations 全体、2025-08 〜 2026-02 の一部
- 表E: Moody's の格付履歴、S&P 引き下げ前の見通し、Fitch 2025 年以降、CDS 2025-09
- 表F: 四半期株式数、期末発行済株式、四半期 SBC、FY2026 の自社株買い・配当総額、ATM 株数
- 表G: 建物耐用年数、PP&E 総額・純額、FY2026・FY2027 の耐用年数変更の有無
