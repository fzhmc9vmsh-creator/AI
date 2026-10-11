# PANW 定性調査(Phase 1 一次整理・改訂版): 報告値の「+63%」の裏でQ2・Q3時点の有機成長は約28%にとどまり、FY27ガイダンスは+22〜23%へ減速する

- 対象: Palo Alto Networks(PANW、決算期末7月31日)
- 評価基準日: 2026-10-11 / 本ファイルの取得日: 2026-10-11(改訂。初版は検索予算切れで欠損が多かった)
- 担当: Sonnet(調査)。評価・投資判断は行わない。事実・出典・「なぜ重要か」の注記のみ。
- 数値データ(四半期業績・KPIの表)は別担当が収集するため、本書は定性情報に絞る。

## 0. 調査状態の開示

- 今回の再開で使った WebSearch は上限の18回すべて。**検索結果は要約文であり、決算説明会のトランスクリプト、10-K、10-Q、委任状説明書、ガートナーの原文は開いていない。** 引用は要約が示した抜粋で、前後の文脈は未確認。
- Tier の表記: Tier 1=会社開示(決算リリース、SEC提出書類、会社ブログ)、Tier 2=公的機関(政府のサイバー機関の警告)、Tier 3=主要報道・アナリスト・集計サイト、Tier 4=ブログ・Substack・AI生成記事サイト・個人投稿。
  「(要約経由)」とあるのは、Tier 1 の文書そのものではなく、検索ツールが返した要約を通じて知った内容。
- **決算日の訂正**: 依頼文の想定と異なり、FY2026 Q3 の発表は 2026-06-02、Q4 の発表は 2026-09-01(CyberArk 買収完了後の日程調整)。FY2027 Q1(2026年8〜10月期)は期末が 2026-10-31 のため基準日時点で**未発表**。
- 未取得(欠損のまま): Q1〜Q3 の説明会本編の質疑、Investor Day、強気・弱気各論者の論拠の詳細、空売りレポート、価格表・顧客評価・求人・パートナーの声、Gartner の支出予測、IDC の市場シェア、訴訟、役員の株式売却(Form 4)。

### 0-1. 出典一覧(以降は ID で参照)

| ID | 出典 | Tier | URL |
|---|---|---|---|
| S01 | PANW FY2026 Q4 決算リリース(会社サイト、2026-09-01) | 1(要約経由) | https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-reports-fiscal-fourth-quarter-and-fiscal-year-2026-financial-results |
| S02 | 同(IRサイト) | 1(要約経由) | https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-reports-fiscal-fourth-quarter-and-fiscal-10 |
| S03 | Form 8-K Ex.99.1(Q4 FY2026) | 1(要約経由) | https://www.sec.gov/Archives/edgar/data/0001327567/000132756726000019/ex991q426earningsrelease.htm |
| S04 | Form 8-K Ex.99.1(Q3 FY2026、2026-06-02) | 1(要約経由) | https://www.sec.gov/Archives/edgar/data/0001327567/000132756726000012/ex991q326earningsrelease.htm |
| S05 | PANW Q3 FY2026 決算リリース | 1(要約経由) | https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-reports-fiscal-third-quarter-2026-financial-results |
| S06 | PANW Q2 FY2026 決算リリース(2026-02-17) | 1(要約経由) | https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-reports-fiscal-second-quarter-2026-financial |
| S07 | Form 10-Q(2026-01-31期)/ 10-Q(2026-04-30期)/ 10-K(2026-07-31期) | 1(存在確認のみ。本文未読) | https://www.sec.gov/Archives/edgar/data/1327567/000132756726000005/panw-20260131.htm ; https://www.sec.gov/Archives/edgar/data/0001327567/000132756726000015/panw-20260430.htm ; https://www.sec.gov/Archives/edgar/data/0001327567/000132756726000023/panw-20260731.htm |
| S08 | DEF 14A(委任状説明書、2025-11-07提出) | 1(要約経由) | https://www.sec.gov/Archives/edgar/data/1327567/000130817925000624/panw-20251107.htm |
| S09 | Stock Titan による DEF 14A 要約 | 3 | https://www.stocktitan.net/sec-filings/PANW/def-14a-palo-alto-networks-inc-definitive-proxy-statement-d20df9b2653a.html |
| S10 | FY2024 年次報告書(ARS) | 1(要約経由) | https://www.sec.gov/Archives/edgar/data/1327567/000130817924000772/panw4345341-ars.pdf |
| S11 | Q4 FY2026 説明会トランスクリプト(Motley Fool、Benzinga、Yahoo、Investing.com、roic.ai 等。要約のみ閲覧) | 3 | https://www.fool.com/earnings/call-transcripts/2026/09/08/palo-alto-networks-panw-q4-2026-earnings-call-transcript/ ; https://www.investing.com/news/transcripts/earnings-call-transcript-palo-alto-networks-beats-q4-2026-estimates-shares-fall-93CH-4884701 |
| S12 | Investing.com 「Q4 FY2026 スライド: 記録的成長、マージン懸念」 | 3 | https://www.investing.com/news/company-news/palo-alto-networks-q4-fy2026-slides-record-growth-margin-concerns-93CH-4884708 |
| S13 | Yahoo Finance 「Q4 2026 説明会要約」(AI生成要約) | 4 | https://finance.yahoo.com/technology/ai/articles/palo-alto-networks-inc-q4-123000309.html |
| S14 | Globe and Mail 「説明会はAIへの自信を示す」 | 3 | https://www.theglobeandmail.com/investing/markets/stocks/PANW/pressreleases/4646816/palo-alto-networks-earnings-call-signals-confident-ai-push/ |
| S15 | Investing.com Q3 FY2026 トランスクリプト(「上回ったが株価は下落」) | 3 | https://www.investing.com/news/transcripts/earnings-call-transcript-palo-alto-networks-q3-2026-beats-expectations-but-stock-drops-93CH-4723135 |
| S16 | CNBC「Q3 決算」(2026-06-02) | 3 | https://www.cnbc.com/2026/06/02/palo-alto-networks-panw-q3-earnings-2026.html |
| S17 | CNBC「第3四半期の利益ガイダンスが届かず7%下落」(2026-02-17) | 3 | https://www.cnbc.com/2026/02/17/palo-alto-networks-panw-q2-2026-earnings.html |
| S18 | Investing.com「Q2 スライド: NGS ARR 33%増、株価5%下落」 | 3 | https://www.investing.com/news/company-news/palo-alto-networks-q2-2026-slides-ngs-arr-jumps-33-stock-falls-5-93CH-4511827 |
| S19 | Motley Fool「Q1 FY2026 決算: 売上は堅調でも株価は沈む」(2025-11-23)/ Q1 トランスクリプト(2025-11-19) | 3 | https://www.fool.com/investing/2025/11/23/palo-alto-stock-sinks-despite-solid-revenue-growth/ ; https://www.fool.com/earnings/call-transcripts/2025/11/19/palo-alto-networks-panw-earnings-transcript/ |
| S20 | CNBC「Anthropic の新ツールがAI代替懸念を煽りサイバー株が2日続落」(2026-02-23) | 3 | https://www.cnbc.com/2026/02/23/cybersecurity-stocks-anthropic-ai-crowdstrike.html |
| S21 | Yahoo「CrowdStrike と Palo Alto は上昇、AI株は下落」/ Yahoo「SaaS-pocalypse を生き残る(JPMorgan)」/ 24/7 Wall St.(2026-04-22)ほか(AIトレードの論調) | 3〜4 | https://finance.yahoo.com/technology/ai/articles/crowdstrike-palo-alto-rallied-while-211451001.html ; https://finance.yahoo.com/news/surviving-saas-pocalypse-jpmorgan-3-175621071.html ; https://247wallst.com/investing/2026/04/22/5-cybersecurity-stocks-most-likely-to-benefit-as-ai-threats-drive-budget-increases-in-2026/ |
| S22 | CME Elite Group「Zscaler の未達で Palo Alto と CrowdStrike も下落」 | 3〜4 | https://www.cmelitegroup.com/trends-and-insights/palo-alto-and-crowdstrike-drop-on-zscaler-miss/ |
| S23 | CNBC「AI主導のサイバー需要の強まりを受け目標株価を引き上げる」(2026-09-01) | 3 | https://www.cnbc.com/2026/09/01/were-lifting-our-price-target-on-palo-alto-networks-as-ai-driven-cyber-demand-intensifies.html |
| S24 | Benzinga アナリスト格付け一覧(目標株価の変更履歴) | 3(集計サイト、日付は未検証) | https://www.benzinga.com/quote/PANW/analyst-ratings?nid=42901348 |
| S25 | Investing.com コンセンサス / CNN(TipRanks 経由)/ StockAnalysis | 3(集計サイト) | https://www.investing.com/equities/palo-alto-netwrk-consensus-estimates ; https://www.cnn.com/markets/stocks/PANW ; https://stockanalysis.com/stocks/panw/forecast/ |
| S26 | Vantage Markets「PANW 年初来109%上昇、Q4決算当日」 | 4 | https://www.vantagemarkets.com/market-analysis/daily-trading-panw-stock-chart-q4-earnings-september-1-2026/ |
| S27 | TS2.tech「決算前に6.4%下落、200億ドル消失」 | 4 | https://ts2.tech/en/palo-alto-networks-stock-drops-6-4-erasing-20-billion-before-earnings/ |
| S28 | Tickeron「Q4 FY2026 決算まとめ」(粗利率・FCFマージンの記述は7本目の検索要約が引用した記事のいずれかで、個別の帰属は未特定) | 4 | https://tickeron.com/earnings/PANW/ |
| S29 | SentiSense / Pulse 2.0 / Tikr(初版の出典 S5/S7/S8 を再掲) | 3〜4 | https://app.sentisense.ai/stories/palo-alto-networks-posts-34-percent-revenue-surge-on-ai-security-demand-yet-stoc-09022026 ; https://pulse2.com/palo-alto-networks-q4-revenue-rises-34-to-3-41-billion-as-next-generation-security-arr-jumps-63-to-9-1-billion/ ; https://www.tikr.com/blog/palo-alto-networks-q4-earnings-crossed-20-billion-in-rpo-next-years-guide-tells-a-different-story |
| S30 | KeyBanc 格下げ(Yahoo Finance) | 3 | https://finance.yahoo.com/news/keybanc-downgrades-palo-alto-networks-145219495.html |
| S31 | Seeking Alpha「素晴らしい会社だが法外な価格では買うな(売りに格下げ)」 | 4 | https://seekingalpha.com/article/4919983-palo-alto-networks-great-stock-but-dont-buy-at-nosebleed-prices-rating-downgrade |
| S32 | FactorsToday「プラットフォームの勢いが1株当たりの証拠を上回る」 | 4 | https://www.factorstoday.com/research/PANW |
| S33 | Invest with Colby(Substack)「Q4 FY2026 説明会レビュー」 | 4 | https://investwithcolby.substack.com/p/palo-alto-networks-panw-q4-fy2026 |
| S34 | Console 買収: 会社プレスリリース / TechCrunch(2026-09-02) | 1(要約経由)/ 3 | https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-acquires-console-to-agentify-security ; https://techcrunch.com/2026/09/02/palo-alto-networks-paid-500m-for-thrive-backed-console-sources-say/ |
| S35 | Chronosphere 買収完了(会社プレスリリース)/ Tikr(発表時) | 1(要約経由)/ 4 | https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-chronosphere-acquisition--unifying-observability-and-security-for-the-ai-era ; https://tikr.com/blog/palo-alto-networks-falls-4-as-the-cybersecurity-giant-announces-3-35-billion-acquisition |
| S36 | CyberArk 買収の発表(会社)/ Form 425(SEC) | 1(要約経由) | https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-announces-agreement-to-acquire-cyberark--the-identity-security-leader ; https://www.sec.gov/Archives/edgar/data/1327567/000119312525168825/d67702d425.htm |
| S37 | Yahoo Finance(Bloomberg 転載)「Palo Alto CEOの報酬は約1億ドル、米国で最も反対される」/ Gloom | 3 / 4 | https://finance.yahoo.com/markets/stocks/articles/palo-alto-ceo-pay-now-121504850.html ; https://gloom.sh/stocks/panw/proxy/2025 |
| S38 | PANW ブログ「初のハイブリッドメッシュファイアウォールのマジック・クアドラントでリーダー」(2025-08)/ SDxCentral | 1(自社主張)/ 3 | https://www.paloaltonetworks.com/blog/2025/08/hybrid-mesh-firewall-magic-quadrant/ ; https://www.sdxcentral.com/news/fortinet-palo-alto-networks-top-gartners-hybrid-mesh-firewall-rankings/ |
| S39 | PAN-OS 脆弱性: シンガポールCSA / NHS England / The Hacker News / Unit 42 | 2 / 2 / 3 / 1 | https://www.csa.gov.sg/alerts-and-advisories/alerts/al-2026-064/ ; https://thehackernews.com/2026/05/palo-alto-pan-os-flaw-under-active.html ; https://thehackernews.com/2026/06/palo-alto-warns-of-active-exploitation.html ; https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/ |
| S41 | marketsupplychain「PANW: プラットフォーム賭け、CyberArkの請求書、6か月〜5年の強気・基準・弱気」 | 4 | https://marketsupplychain.com/posts/panw/ |
| S40 | Fortinet 2026年guidance上方修正(Yahoo Finance)/ プラットフォーム統合の論考(Substack) | 3 / 4 | https://finance.yahoo.com/technology/articles/fortinet-lifts-2026-guidance-firewall-145800016.html ; https://rahul31.substack.com/p/pooled-contracts-and-platform-consolidation |

---

## A. 経営陣シナリオの一次情報

### A-1. 経営陣は「AIが予算を押し上げ、プラットフォーム化が唯一の現実的な答えで、買収で製品を足す」と語っている

すべて決算説明会・決算リリースの発言を要約経由で確認したもの。話者名は要約が示したとおり。

| 時期 | 発言者 | 和訳(原文は括弧で最小限) | 出典 | 重要な理由 |
|---|---|---|---|---|
| 2026-09-01(Q4) | Nikesh Arora(会長兼CEO) | 「強いQ4で締めくくり、1四半期だけで純新規NGS ARRをほぼ10億ドル積み増した」(adding nearly $1 billion of Net New NGS ARR in a single quarter) | S01〜S03 | 成長の最重要KPIが「純新規NGS ARR」であることを示す |
| 同上 | Arora | 「AIの最新の進歩が、サイバーセキュリティをCIOの優先課題の最上位に引き上げている」 | S01〜S03 | 需要側の前提(会社の主張、独立検証なし) |
| 同上 | Arora | 「プラットフォーム化は、組織がAIの取り組みを本格運用に移すなかで、リアルタイム防御の唯一の現実的な戦略だ」(platformization is the only viable strategy for real time defense) | S11 | 「プラットフォーム化」=複数の個別製品を1社の統合基盤に集約すること。シナリオの中心概念 |
| 同上 | Arora | Chronosphere(可観測性=システムの稼働データを集めて監視する基盤)は「AI時代のデータ量のために作られ、主要な既存ベンダーより平均で30〜40%安い」 | S11 | 価格優位を明言。大手顧客の移行を引き込む理屈 |
| 同上 | Arora | 統合した買収事業のマージンは「約2四半期で単独時の水準に戻る」 | S11 | 買収の統合費用は一時的との主張。検証対象(FY27の粗利率・営業利益率) |
| 同上 | CFO Dipak Golechha | 「当社の収益性の枠組みは効果的に拡大を続けており、FY28に調整後FCFマージン40%を達成する確信を強めている」 | S01〜S03 | 利益面の中期目標の根拠 |
| 同上 | Golechha | クラウドのホスティング費用は、クラウド・SaaS構成比の上昇により「FY27は売上より速く増える」見通し | S11 | 粗利率の逆風を会社自身が予告 |
| 同上 | 経営陣 | プラットフォーム化の寄与で、受注の伸びは「プロフォーマ(買収分を合算した比較)で2四半期連続して加速した」 | S11 | 「有機成長の加速」の主張。有機分の開示は欠損 |
| 2026-06-02(Q3) | Arora | 「顧客がAIの導入を大規模に守るために当社を選び、有機的な受注の伸びが加速している」(accelerating organic bookings growth as customers turn to us to secure their AI deployments at scale) | S16 | AI需要と有機成長を結びつける発言 |
| 同上 | 経営陣 | 「これまでで最大の四半期上振れ。ガイダンスを上回った」(most significant quarterly outperformance to date) | S16 | |
| 同上 | CFO | 買収の統合は「計画より先行して進んでいる」(executing ahead of our M&A integration plans) | S04/S05の要約(Q3説明会での発言) | 統合進捗の会社説明 |
| Q4(2026-09-01) | 経営陣 | CyberArk 関連の統合効果と Console は FY27 ガイダンスに「重要な影響を与えない」 | S11/S13(AI要約) | FY27ガイダンスに新規買収の上積みを含めていない可能性。要確認 |

**欠損**: Q1・Q2 の経営陣発言、Investor Day、Q&Aの全文。「次世代ファイアウォール」のハードウェア更改についての発言は取得できていない(Q4の粗利率の説明で「メモリ・ストレージ費用がハードウェアの逆風」との言及のみ)。

### A-2. 数値目標とその定義・期限

| 目標 | 値 | 期限 | 出典 | 備考 |
|---|---|---|---|---|
| NGS ARR(次世代セキュリティの年間経常収益) | 200億ドル | FY30 | S01〜S03 | **以前の目標は「買収を除く単独で150億ドル」**(DEF 14A:取締役会がFY24の途中で加速的プラットフォーム化戦略を採用し、FY30に単独で150億ドルのNGS ARRを目指した)。200億ドルは買収を含む改定値。改定日は未確認 |
| 調整後FCFマージン | 40%以上 | FY28 | S01〜S03、S36 | 買収発表時に「CyberArk と Chronosphere を含めて40%以上を再確認」。CyberArk は1株当たりFCFへの上積み(アクレティブ)をFY28に見込む(買収発表時の会社説明) |
| FY27 NGS ARR | 110.75億〜111.75億ドル(+22〜23%) | FY27末 | S29(Pulse) | |
| FY27 売上高 | 141.0億〜142.0億ドル(+23〜24%)。**コンセンサス(137.9億ドル)を上回る** | FY27 | S23(CNBC) | 売上ガイダンスは超過、NGS ARR は「コンセンサス並み」(Cantor、初版で取得) |
| FY27 非GAAP営業利益率 | 29.5% | FY27 | S29 | |
| FY27 調整後FCFマージン | 37.5〜38%(出典により「38%」)| FY27 | S28、S29 | FY26実績38.4%から横ばい〜低下 |
| FY27 希薄化後株数 | 8.44億〜8.47億株 | FY27 | S33(Tier 4・単独) | 要確認 |
| ラベル不明の範囲 | 95.4億〜95.6億ドルという範囲が決算リリースの要約に存在 | 不明(FY27 Q1の可能性) | S02/S03の検索要約の注記 | 何の指標か不明。**未確認** |
| プラットフォーム化顧客数の目標 | 欠損 | — | — | 総数の開示も取得できず |

**用語**: NGS ARR は会社定義の「次世代セキュリティ」製品群の年間経常収益。**CyberArk の分は「サブスクリプション部分のみ」を PANW の売上ベース定義に合わせて算入**し、CyberArk 自身の受注ベースの定義より約2〜3%低くなる(Q3の会社説明、S04/S05要約)。定義の変更を伴う指標であることに注意。

### A-3. ピース一覧: 2026年だけで買収が7件に達し、AIセキュリティ・観測・アイデンティティの3領域に集中

TechCrunch は Console を「2026年で7件目の買収」と数えている(S34)。

| ピース | 区分 | 会社の説明する目的 | 発表日・完了日 | 規模・進捗の数値 | 出典 |
|---|---|---|---|---|---|
| CyberArk | 買収(アイデンティティ) | 次世代アイデンティティセキュリティ基盤の形成。**新製品名は「Idira」**(「AI時代の企業のための次世代アイデンティティセキュリティ基盤」) | 発表 2025年夏(日付は欠損。会社リリースのURLが2025年配下)/ 完了 **2026-02-11** | 対価は現金23億ドル+新株1.12億株(契約条件: CyberArk 1株につき現金45ドル+PANW株2.2005株、総額約250億ドル)。Q3の売上のうち CyberArk と Chronosphere の合計が3.88億ドル。**Idira の売上はプロフォーマで21%成長**(単独出典・Tier 4)。株式対価により株数は10%超増加(S33) | S36、S07、S11、S33 |
| Chronosphere | 買収(可観測性) | 可観測性とセキュリティの統合、AI時代のデータ量への対応 | 発表 2025年11月頃(Q1決算日 2025-11-19 と Tikr の記事から推定。株価は発表で約-4%)/ 完了 **2026-01-29** | 買収額33.5億ドル。**可観測性ARRは2四半期で倍増し5億ドル超**(Q4説明会)。Q4の純新規ARRには「大手LLM(大規模言語モデル)顧客が既存ベンダーから Chronosphere へ移行した、9桁(1億ドル以上)の寄与」が含まれた | S35、S11 |
| Koi | 買収(端末の姿勢管理) | エージェント型エンドポイントセキュリティを SecOps基盤に追加し、Prisma AIRS を強化 | 完了 **2026-04-14** | 規模は欠損 | 検索要約(10-K/10-Q・会社リリース由来。原文未確認) |
| Portkey | 買収(AIゲートウェイ) | Prisma AIRS の拡張 | 完了 **2026-05** | 規模は欠損 | 同上 |
| Embrace | 買収(デジタル体験監視と推定) | 可観測性基盤にデジタル体験モニタリングを追加(IRのリリース題名から推定) | 発表 2026-07 / 完了 **2026-08-27** | 規模は欠損。リリースとの対応は未確認 | 検索要約(会社リリース由来。原文未確認) |
| Console | 買収(エージェント型セキュリティ) | 「セキュリティのエージェント化」。Cortex のエージェント型機能の強化 | 発表・完了とも 2026-09-01 | **約5億ドル(現金と株式)との報道**(関係者2名、Tier 3)。FY27ガイダンスには重要な影響なしとの会社説明 | S34 |
| Protect AI | 買収(AIモデルの安全性) | — | **欠損(検索で確認できず)** | — | — |
| Talon、Dig Security | 買収(ブラウザ、データ) | — | **欠損** | — | — |
| 製品: Prisma AIRS(AIアプリ・エージェントの防御)、Cortex XSIAM(AIによるSOC=セキュリティ運用の自動化)、Prisma Access(SASE=ネットワークとセキュリティのクラウド統合) | 製品 | — | — | 数値は節F | — |
| 価格・契約形態の変更(無償期間・クレジット供与) | — | — | **欠損** | — | — |
| 資本政策(自社株買い・株式分割・転換社債) | — | — | **欠損**(CyberArk の対価に新株1.12億株を発行した事実のみ) | — | — |

### A-4. 過去の約束と結果: 直近のガイダンスは一貫して上振れだが、買収の算入で比較が崩れる

| 項目 | 期初・直前の約束 | 実績 | 差 | 出典・備考 |
|---|---|---|---|---|
| FY26 NGS ARR(期初。Q1決算時) | 70億〜71億ドル | 91.0億ドル | +20億ドル超 | 検索要約は発表時期を「Q1 FY26 説明会(2025-11)」とする。**期初ガイダンス後に CyberArk・Chronosphere が加わるため、比較は同条件ではない** |
| FY26 売上 | 105.0億〜105.4億ドル | 114.8億ドル | +9億ドル程度 | 同上(買収分を含む) |
| Q4 NGS ARR(Q3決算時) | 89.0億〜89.5億ドル(+59〜60%) | 91.0億ドル(+63%) | +1.5億〜2.0億ドル(+1.7〜2.2%) | S04/S05の要約。独自計算。買収後の見通しとして保守的だった |
| Q3 売上(Q2決算時) | 29.41億〜29.45億ドル | 30.0億ドル(CNBC: コンセンサス29.4億ドル) | 約+2% | S06、S16 |
| Q4 非GAAP EPS | ガイダンス上限+0.04ドルの超過 | 1.02ドル | +0.04ドル | S11要約 |
| Q3 非GAAP EPS | コンセンサス(LSEG)0.80ドル | 0.85ドル | +0.05ドル | S16 |

- FY24・FY25 の期初ガイダンスと実績、製品・時期の約束の履行は**欠損**。S08 によれば取締役会は FY24 の途中に「加速的プラットフォーム化戦略」を採用した。2024年2月の大幅下落(S29の株価記述で「2024年2月以来で最悪の2日間」)の経緯は取得できていない(節H)。
- 会社の説明: CFOはQ4を「ガイダンスを全項目で上回った」と述べた(S01〜S03)。ただし**四半期ガイダンスを保守的に置く傾向**は、上表の4件が示すにとどまる(サンプル不足)。

### A-5. 経営陣・報酬: 報酬は総額指標(受注成長率と相対TSR)で、株主の承認は半数を割った

| 項目 | 内容 | 出典・Tier |
|---|---|---|
| 現職 | Nikesh Arora=会長兼CEO、Dipak Golechha=CFO(Q4説明会で投資家対応はHamza Fodderwala) | S01〜S03、S11 |
| CEOの報酬(FY2025) | 総額 **99,736,336ドル**(FY2024は58,036,875ドル)。株式報酬が約9,490万ドル、給与100万ドル、非株式インセンティブ120万ドル | S08(要約経由)、Tier 1 |
| 報酬のKPI | FY2024の開示: CEOの業績連動株式(PSU)は3年後に確定し、**billings(請求額)の成長率**と**相対TSR(株主総利回り)**で決まる。単位は**総額の成長率と株価の相対順位**で、1株当たりFCF・EPSではない。FY2025の設計は未確認 | S10(要約経由)。S08の確認が必要 |
| 株主の評価 | 直近の報酬への株主承認投票(say-on-pay)は**半数を割った**(2025年12月と見られる)。ISSは直近11会計年度のうち8年(「3年を除く」)で反対を推奨 | S37(Tier 3) |
| 賃金比率 | CEOと従業員の中央値の比率 442対1(中央値報酬225,828ドル) | S37(Gloom、Tier 4) |

**なぜ重要か**: KPIが総額の受注成長なら、買収で株式を発行して総額を積み増しても報酬が増える。1株当たり価値との利害一致は検証が必要。FY2026 の報酬指標(委任状説明書は2026年11月提出予定)は未取得。

---

## B. 市場の仮説の出典

### B-1. アナリストが繰り返した質問(関心の所在)

Q4(2026-09-01)の質疑(S11、S12の要約。質問者名は取得できず):
1. **シェアシフトか、AIで市場が広がっただけか**: 「シェアを取っているのか、AIで市場そのものが大きくなっているだけか」という質問が出た。
2. **粗利率の低下**: Q4の総粗利率は74.8%、前年比100bp(1ポイント)低下。会社はSaaS(クラウド提供型ソフト)構成の上昇と、ハードウェア面のメモリ・ストレージ費用の上昇を挙げた。Investing.com の見出しは「記録的成長、マージン懸念」(S12)。
3. **純新規ARRの構成と来期の季節性**: 大手LLM顧客の Chronosphere への移行(9桁の寄与)がQ4に含まれ、FY27の季節性に影響すると会社が説明(S29/Tikrと整合)。
4. **既存ベンダーの置き換え(ディスプレイスメント)**: FY26の契約総額は4億ドル超で前年のほぼ倍。四半期の数字は「4億」「4.54億」「4.5億」と要約が食い違い**未確定**。

Q3(2026-06-02)の質疑: **欠損**。

### B-2. 強気派と弱気派

**強気派(目標株価は 2026-09 時点、変更前→変更後)**。論拠の詳細はほぼ取得できておらず、方向性のみ。

| 証券会社(アナリスト) | 格付け・目標株価 | 時期 | 論拠(取得できた範囲) | 出典 |
|---|---|---|---|---|
| RBC Capital | Outperform、434ドル→**475ドル** | 2026-09-02頃 | 論拠は欠損 | S24(集計サイト) |
| Oppenheimer | Outperform、400ドル→**450ドル** | 同上 | 欠損 | S24 |
| Jefferies(Joseph Gallo) | Buy、335ドル→**450ドル** | 決算前(〜2026-09-01) | 欠損 | S26(Tier 4経由) |
| Morgan Stanley(Meta Marshall) | Overweight、387→394ドル(9/2)、さらに394→**410ドル**(9/20〜21) | 同上 | 欠損 | S24、S25 |
| Piper Sandler | Overweight、345→**410ドル** | 2026-09-02頃 | 欠損 | S24 |
| Citigroup | Buy、400→**410ドル** | 同上 | 欠損 | S24 |
| JPMorgan(Brian Essex) | Overweight、326→**384ドル** | 決算前 | 欠損 | S26 |
| Barclays | Overweight、370→375ドル | 2026-09-02頃 | 欠損 | S24 |
| Wedbush | Outperform、**400ドル**で新規にカバレッジ開始 | 2026-09-10 | 欠損 | S25 |
| CNBC | 「AI主導のサイバー需要の強まりを受け目標株価を引き上げる」(見出し。売上ガイダンス141〜142億ドルがコンセンサス137.9億ドルを上回る) | 2026-09-01 | 売上ガイダンスの超過とAI需要 | S23 |

- 集計されたコンセンサス目標株価は約**395〜397ドル**(52人。S&P Global経由約396ドル、Investing.com 395.70ドル、別の集計395.38ドル=2026-09-22更新)。**単一の出所ではない集計サイトの数字で、日付も未検証**。

**弱気派・慎重派**

| 論者 | 内容 | 時期 | 出典 |
|---|---|---|---|
| Bernstein | **Market Perform(中立)に格下げ、目標株価351ドル** | 2026-09-17 | S24(集計サイト。論拠は欠損) |
| KeyBanc | Overweight から **Sector Weight(中立)に格下げ**。CyberArk 買収の戦略的な適合に疑問、株価は2026年FCFの約33倍で適正水準 | 2025-07末頃(検索要約が「約436日前」と記すことから推定) | S30(Tier 3) |
| Seeking Alpha(執筆者名は欠損) | 「売り」に格下げ。AI楽観と買収で株価が約2倍になり、有機成長から評価が乖離 | 日付欠損 | S31(Tier 4) |
| FactorsToday | FY2026の「通常FCFからSBC相当の調整を引いた額」は約24.0億ドル(前年20.8億ドル)で、総額は+15%、**1株当たりは+7%**。336.98ドル(2026-09-08)で「新規資金は見送り」 | 2026-09-08 | S32(Tier 4) |
| Invest with Colby | 株数は10%超増加(CyberArk が主に株式対価)。買収分の利益が希薄化を上回って伸びていない | 2026-09 | S33(Tier 4) |

- **反論側の会社説明**: CyberArk は FY28 に1株当たりFCFを押し上げる(アクレティブ)と会社は説明(S36)。

### B-3. 空売りレポート・著名な弱気論者
今回の検索では**確認できなかった**(PANW に対する空売りレポートは取得できず)。

### B-4. 報道のナラティブ

| 繰り返される言葉 | 見出しの例 | 出典 |
|---|---|---|
| **決算は上回っても株価は下がる** | 「Q3 は上回ったが株価は下落」(Investing.com)、「Q4 は上回り株価は下落」(同)、「売上34%増と記録的なセキュリティARR、それでも株価は13%下落」 | S15、S11、S29 |
| **AI需要/AI脅威が予算を押し上げる** | 「AI主導のサイバー需要の強まり」(CNBC)、「AIの脅威が予算増をもたらす」(24/7 Wall St. 2026-04-22) | S23、S21 |
| **来期の物語は別** | 「RPOが200億ドルを突破、来期のガイダンスは別の物語を語る」 | S29(Tikr) |
| **プラットフォームの勢いと1株当たりの証拠** | 「プラットフォームの勢いが1株当たりの証拠を上回る」、「プラットフォーム賭けとCyberArkの請求書」、「法外な価格では買うな」 | S32、S41、S31 |
| **決算の前に下げる** | 「決算前に6.4%下落し200億ドル消失」 | S27 |

**2026年のソフトウェア株の「AIによる代替」懸念とセキュリティ株への影響**
- 2026-02-23: Anthropic がコードの脆弱性を探して修正を提案するセキュリティ機能を限定公開すると、サイバー株が2日続落。CrowdStrike と Zscaler が各約10%、Netskope と Tenable が各約12%下落。**PANW は約3%下落**(同日のPANW自体の決算でQ3利益見通しが届かなかった要因も混在)(S20)。
- Barclays は下げを「不整合」と評した(Anthropic のツールは大手ベンダーの中核製品を直接は置き換えない)。JPMorgan は CrowdStrike・PANW・Zscaler を長期の勝者に挙げた(S20)。
- その後の論調は「AI代替の恐れ」から「AIが防御需要を押し上げる」へ転じ、PANW は2026-09-01時点で年初来**109%上昇**(S26)。「SaaS-pocalypse(ソフトウェアの終末)」という言葉がJPMorgan関連の記事で使われた(S21周辺、本文未確認)。
- 2026年5月下旬、Zscaler が決算と弱い見通しを受けて寄り付き前に24%下落し、PANW と CrowdStrike も連れ安した(S21、S22。Wedbush は「業界全体のシグナルではない」と評した)。

### B-5. 株価の推移: 年初来で倍増した後、決算で約13%下落し、その後は戻り基調

| 時期 | 出来事 | 出典・Tier |
|---|---|---|
| 2025-11(Q1 FY26) | 決算後、「売上は堅調でも株価は沈む」。Chronosphere 買収(33.5億ドル)の発表で約-4% | S19、S35(Tier 3〜4) |
| 2026-02-17(Q2 FY26) | **-5%(Investing.com)または-7%(CNBC)**。理由は第3四半期の利益ガイダンスが届かなかったこと(買収に伴う希薄化) | S17、S18 |
| 2026-02-23 | Anthropic のツールをきっかけにサイバー株が下落。PANW 約-3% | S20 |
| 2026-06-02(Q3 FY26) | 時間外で最大+12%、その後ほぼ横ばいに戻る。「上回ったが株価は下落」の見出しも | S16、S15 |
| 2026-09-01 | 決算の数時間前の取引価格 **382.14ドル**(年初来+109%)。同日、決算前に約-6.4%(約200億ドルの時価総額が消失)との記事もあり、382.14ドルが下落前か後かは未確認 | S26、S27(Tier 4) |
| 2026-09-02 | 決算後に約-8%。2営業日合計で**約-13.2%**(2024年2月以来最悪の2日間とされる)。**13.2%の一部(約6%)は決算発表前の下げ**で、決算後だけでは約8% | S28、S29(Tier 4・単独) |
| 2026-09-08 | **336.98ドル** | S32(Tier 4) |
| 2026-09-14 | 純粋サイバー株が「ここ数年で最高の1日」(半導体株の下落と同日)。出所の年は未確認 | S21(Tier 4) |

- 基準日の終値(2026-10-09)は欠損(別担当の定量データに委ねる)。

---

## C. 一次情報(スカットルバット)

最低3件の要件は、次の4件で満たす。ただし、価格表、顧客のレビュー、求人、パートナーの声は**依然として欠損**で、独立した顧客側の証拠は薄い。

| # | 観察 | 内容 | 出典・Tier | 構造仮説への意味 |
|---|---|---|---|---|
| C-1 | ガートナーのマジック・クアドラント(ハイブリッドメッシュファイアウォール、2025年8月、初回) | PANW は「リーダー」で、**ビジョンの完全性(Completeness of Vision)で最も右**(PANWの自社ブログによる)。Fortinet は実行力(Ability to Execute)が最高(SDxCentral)。Check Point もリーダー。**Cisco はビジョナリーへ後退**。ハイブリッドメッシュファイアウォールは「オンプレミス機器、仮想、クラウドを1つの管理基盤で運用する」製品区分 | S38(Tier 1自社主張/Tier 3) | 次世代ファイアウォールの優位は第三者評価でも維持。ただし実行力では Fortinet が上 |
| C-2 | 競合 Fortinet の2026年業績見通し | 2026年Q2決算で通期売上見通しを80.2億〜81.8億ドル(約+19%)に引き上げ(従前は77.1億〜78.7億ドル)。牽引役は**ファイアウォールの更改需要とSASE**。更改の波は2026〜27年に端末のサポート終了を迎えて成熟し、2027年に鈍る可能性。メモリ費用の上昇も警戒 | S40(Tier 3〜4) | ファイアウォール更改サイクルが PANW のハードウェア・サブスクにも追い風か。ただし FTNT 側に PANW への直接言及は確認できない |
| C-3 | 政府機関の脆弱性警告(PAN-OS の2件) | 2026年に PAN-OS の2件が実際に悪用されている(節G)。シンガポールCSA、NHS England が警告 | S39(Tier 2) | 自社製品の信頼性リスクの客観的な証拠 |
| C-4 | 顧客側の導入例(会社の説明) | 大手グローバル決済プラットフォームと**5,300万ドル**のプラットフォーム化契約(別に Prisma AIRS へ7桁後半を契約)。プラットフォーム化した顧客の**NRR(既存顧客の売上継続率)は120%超**。既存ベンダーの置き換えは契約総額4億ドル超 | S11(トランスクリプト要約、会社の主張) | **会社発表の数字であり独立した裏付けではない** |
| C-5 | 市場の統合圧力(論考) | CISOは40超の個別製品から3〜5の統合基盤へ減らす。Microsoft、CrowdStrike、PANW、Fortinet が新規の検知支出の大半を取る | S40(Substack、Tier 4) | プラットフォーム化の追い風を示す仮説だが、単独のブログ |

**欠損**: ガートナー ピアインサイツの評価、導入事例の定量効果、IDC の市場シェア、求人動向、チャネルパートナーの声、価格表・ライセンス変更、ファイアウォール・SASE・SIEM の市場規模と成長率。

## D. 競争と業界の構造

- **会社が開示する競合の動き**: PANW のSASE ARR は16億ドル(+40%、Q3、S16)。Zscaler(SSEの有力企業)は2026年5月下旬に決算後の寄り付き前取引で24%下落(S22)。Zscaler の有機成長はQ4 FY26に+17%(前年は7%、Tier 4・単独、数値の信頼性は低い)。CrowdStrike のARRは出典により「52.5億ドル(+24%)」と「48億ドル(+26%)」が食い違い**未確定**(CRWD担当が確認)。
- **新規の検知支出**: Microsoft、CrowdStrike、PANW、Fortinet がプラットフォーム統合のXDR(拡張検知・対応)で取る(S40・Tier 4)。Google+Wiz、Microsoft の価格圧力に関する情報は**欠損**。
- **ハードウェアの逆風**: メモリ・ストレージの費用上昇が、PANWの粗利率とFortinetの両方に言及(S11、S40)。
- **AIエージェントのセキュリティという新市場**: 市場規模の推計は取得できず。会社側の実績値は節F。
- **セキュリティ予算(Gartner の支出予測)**: 欠損。
- **大規模侵害が需要に与えた影響**: 欠損。

---

## E. 異常値の候補(取得した数値からの算出。いずれも「兆候であり判定ではない」)

丸めた開示値での概算。精密値は10-K・決算スライドで置き換えること。

### E-1. 報告のNGS ARR成長は+63%だが、有機成長は約28%で、FY27ガイダンスの+22〜23%はそれより低いのはなぜか
- 事実: Q2のNGS ARRは+33%(63億ドル)で、**有機では+28%**(S06、Chronosphere除く)。Q3は81億ドル(+60%)で、**CyberArk と Chronosphere 由来が16億ドル**(S04/S05)。Q4は91.0億ドル(+63%)。FY25末は55.8億ドル(S09の見出し)。
- 算出: Q3の買収除外ARR=81−16=65億ドル。前年Q3=81÷1.60≒50.6億ドルなので、有機成長は 65÷50.6−1≒**28%**。FY26の純増=91.0−55.8=**35.2億ドル**。このうちQ3時点の買収取り込み16億ドルを除くと約19.2億ドル(取り込み後の買収製品の成長を無視した粗い見積り)。FY27ガイダンスの純増は 110.75〜111.75−91.0=**19.8億〜20.8億ドル**で、買収除外のFY26純増と同水準。
- 問い: 市場が「+63%」で見た成長の実体は何か。FY27の+22〜23%は、有機成長(約28%)からの減速なのか、それとも買収前の基準が違うだけか。

### E-2. Q4の純新規NGS ARRはほぼ10億ドルだが、FY27通期のガイダンスは約20億ドル。Q4に大手LLM顧客の移行(9桁)が入るのはなぜか
- 事実: Q4の純新規ほぼ10億ドル(S01〜S03)。そのうち「大手LLM顧客が既存ベンダーから Chronosphere へ移行」した9桁(1億ドル以上)の寄与を会社が説明(S11、S40)。会社はこの一回限りの移行が FY27 の純新規ARRの季節性に影響し、第1四半期が通常より大きくなると説明したと要約は記す(S11系の要約。原文未確認)。
- 問い: Q4の10億ドルのうち、継続的に再現する部分はいくらか。特定のLLM顧客1社への依存はどの程度か。

### E-3. GAAPと非GAAPの営業利益の差が前年の約2.7億ドルから約8.3億〜10億ドルに広がったのはなぜか
- 事実: Q4のGAAP営業利益1.72億ドル(前年4.97億ドル)、非GAAP約10億ドル(前年7.68億ドル)。Q3はGAAP営業損失1.83億ドル、非GAAP営業利益8.14億ドル。
- 算出: 差額=Q4 FY25: 2.71億ドル(売上比約11%)、Q3 FY26: **約9.97億ドル(売上30億ドルの約33%)**、Q4 FY26: **約8.3億ドル(約24%)**。
- 問い: SBC(株式報酬)、買収無形資産の償却、買収関連費用の内訳は。SBCは事業実態EPSを直接動かす(00_standard.md §3)。

### E-4. 調整後FCFマージンはFY26の38.4%からFY27の37.5〜38%へ下がるのに、FY28は40%を目指すのはなぜか
- 事実: S01〜S03、S28、S29。CFOは「確信を強めている」と発言。FY27は粗利率の低下(-100bp)とクラウドホスティング費用の増加を会社自身が予告。
- 問い: FY28に+2〜2.5ポイント改善する具体的根拠。統合費用と買収事業のマージン回復(約2四半期で単独水準)の寄与。

### E-5. 売上ガイダンスはコンセンサスを約2.6%上回る(141〜142億ドル対137.9億ドル)のに、株価が下がったのはなぜか
- 事実: S23(CNBC)。NGS ARRのガイダンスはコンセンサス並み(Cantor)。決算前に株価は年初来+109%。決算前に約-6%、決算後に約-8%。
- 問い: 市場の期待は売上でなくNGS ARRの加速にあったのか。それは何を織り込んでいたのか。

### E-6. 1株当たりでは総額ほど伸びないのはなぜか(株数が10%超増えた)
- 事実: 希薄化後株数は非GAAP純利益8.53億ドル÷1株1.02ドル≒**約8.4億株**。CyberArk対価で新株1.12億株を発行。FY27ガイダンスは8.44億〜8.47億株(Tier 4)。FactorsTodayはFCF(SBC調整後)が総額+15%、1株+7%(Tier 4)。
- 問い: CyberArk が1株当たりFCFを押し上げるのはFY28との会社説明だが、FY26〜FY27に1株当たりでどれだけ希薄化されるか。前年同期の株数は欠損。

### E-7. 非GAAP EPS が Q2の1.03ドル → Q3の0.85ドル → Q4の1.02ドルと動いたのはなぜか
- 事実: Q2=1.03ドル(S06)、Q3=0.85ドル(S16)、Q4=1.02ドル(S01〜S03)。この間にCyberArk(2026-02-11完了)が入った。
- 問い: Q3の落ち込みは現金23億ドルの支出による受取利息減少、新株1.12億株、買収の統合費用のどれによるか。Q4での回復は何か。

### E-8. 総粗利率が前年比-100bp(74.8%)に下がったのはなぜか
- 事実: 会社の説明はSaaS構成の上昇とメモリ・ストレージ費用(S11、S12)。FY27はクラウドホスティング費用が売上より速く増える見通し。
- 問い: NGS ARRの成長が粗利率の低い製品(可観測性・クラウド提供)に偏るなら、定常状態の利益率は何%か。

### E-9. KPI定義の変更: CyberArk のARRを売上ベースに合わせると約2〜3%低くなる
- 事実: S04/S05の要約。
- 問い: 買収後のNGS ARR 91.0億ドルは受注ベースの旧来の定義と比べてどれだけ違い、FY27の+22〜23%の成長率はどの定義で測られるか。

### E-10. 目標株価を上げる証券会社が多い(RBC 475ドル、Oppenheimer 450ドルなど)のに、Bernstein は格下げし、株価は戻らないのはなぜか
- 事実: 節B-2。集計コンセンサス約395ドルは9月8日の336.98ドルを約17%上回る(独自計算)。
- 問い: 買い手と売り手が見ている変数(NGS ARRの有機成長、FCF/株、粗利率)は何が違うか。

---

## F. 条件9(AIの停めない運用)に関わる事実

AI関連の開示値は、**製品の売上規模はまだNGS ARR全体の一部**であることを示す。出典は説明会要約(S11、S14)で、数値は単独出典の場合がある。

| 製品 | 内容 | 開示値 | 出典・Tier |
|---|---|---|---|
| Prisma AIRS | AIアプリ・AIエージェントを守る製品(ランタイム防御、AIゲートウェイなど)。Koi(エージェント型エンドポイントの保護)と Portkey(AIゲートウェイ)の買収で拡張 | **一般提供から4四半期でARR 1億ドル超**、「会社史上で最も速く伸びた製品」、顧客**800社超**。決算説明会で、決済プラットフォーム1社が7桁後半(数百万ドル台後半)を契約したとの言及 | 検索要約(S11/S14等)。出所の個別特定不可、単独出典の数字を含む。**ARRの定義と正確な値は欠損** |
| Cortex XSIAM | AIでSOCの調査・対応を自動化する製品(SIEM=ログ集約と脅威検知の領域) | FY26に**ARR 7億ドル超**、前年比約+70%、顧客約**1,000社** | 検索要約(S11/S14等)。出所の個別特定不可 |
| Chronosphere | 可観測性。大手LLM顧客が移行(AI推論の大量データを扱う側) | 可観測性ARR 5億ドル超(2四半期で倍増) | S11 |
| Console | エージェント型セキュリティ | 約5億ドルで買収(報道) | S34 |

- 算出(独自): Prisma AIRS の1億ドル超÷NGS ARR 91.0億ドル=約**1.1%超**。XSIAM の7億ドル超÷91.0億ドル=約**7.7%超**。
- 条件9の最終判定に必要な「AIを守る製品のARR」の定義と内訳、AIを動かす側(LLM顧客)への依存度は、10-K・決算スライドで要確認。

## G. リスク事象

| 事象 | 内容 | 出典・Tier |
|---|---|---|
| **自社製品の重大脆弱性(2026年に2件が悪用中)** | ①**CVE-2026-0300**(2026年5月): PAN-OS の User-ID 認証ポータル(Captive Portal)のバッファオーバーフロー。認証なしで root 権限の遠隔コード実行(RCE)が可能。CVSS(深刻度スコア)9.3(出典により異なる)。**米国CISAが2026-05-06に「悪用が確認された脆弱性」カタログ(KEV)に追加**。PA/VMシリーズのCaptive Portal構成のみが対象。②**CVE-2026-0257**(GlobalProtect VPN): 認証バイパス。CISAがKEVに2026-05-29追加。CVSSは9.1(シンガポールCSA)と7.8(Infosecurity Magazine)で食い違い。Unit 42 は「侵入後の挙動・横展開は確認されていない」 | S39(Tier 1〜3) |
| GAAP純損失 | Q4のGAAP純損失2.82億ドル(▲0.35ドル/株)。Q3もGAAP営業損失1.83億ドル。原因の内訳は未確認(E-3) | S01〜S05 |
| 株主の反対 | CEO報酬への株主承認が半数割れ、ISSが長年反対 | S37 |
| 希薄化 | CyberArk 対価の新株1.12億株、株数10%超増 | S33、S36 |
| 空売り・訴訟・株式売却 | 訴訟(集団訴訟)と経営陣の株式売却(Form 4)は今回の検索でヒットせず**欠損**(「無い」の確認ではない) | — |
| 統合リスク | Console を含む7件の買収の統合。ある記事が CyberArk・Chronosphere・Console の統合の実行を注視点に挙げる(出所は特定不可、Tier 3〜4) | S28周辺 |

---

## H. 出典なしの手がかり(訓練知識。評価には使わない)

初版で挙げた項目のうち、**検索で裏付けられたものは本文へ移した**: CyberArk の条件(現金45ドル+2.2005株、約250億ドル、完了2026-02-11)、Chronosphere の33.5億ドル、旧FY30目標150億ドル(DEF 14A)。残りは未検証のまま:
- Protect AI 買収: 2025年に発表されたAIセキュリティ企業の買収(今回の検索で確認できず)。
- 2024年12月の1対2の株式分割(確認できず)。
- 2024年2月のガイダンス引き下げと株価急落の経緯(S29の「2024年2月以来で最悪」から、事象の存在のみ推定)。
- Nikesh Arora の CEO 就任時期(2018年と記憶)、CFO Golechha の在任期間(確認できず)。

---

## I. 次に必要な調査(優先順)

1. FY2026 Q4 説明会の全文と決算スライド(NGS ARR の有機・買収別、純新規ARRの四半期推移、プラットフォーム化顧客数、Prisma AIRS・XSIAMのARRの正確な値、ラベルなしの95.4億〜95.6億ドルの範囲)。
2. FY2026 10-K(買収の注記、株数、SBC、調整後FCFの定義、リスク要因、訴訟)。
3. 2026年の委任状説明書(FY26の報酬KPI)。Q1〜Q3 説明会の質疑。
4. 主要証券会社の決算後ノート原文(RBC、Oppenheimer、Bernstein の格下げ論拠)。
5. IDC・Gartner の市場規模と支出予測、価格表・顧客評価・求人。
6. 訴訟と経営陣の株式売却(Form 4)、空売りレポート。
