# R4 スカットルバット調査: SoFi Technologies (NASDAQ: SOFI)

調査日: 2026-10-18 / 調査担当: R4(会社開示以外の一次情報・業界・競合・規制)

## 0. 調査の限界(必読)

| 項目 | 内容 |
|---|---|
| 取得手段 | WebSearchのみ。WebFetchはDNS解決エラー(ENOTFOUND)で全URL不可。curl直取得はプロキシが403で拒否(www.newyorkfed.org等)。迂回はしていない |
| 数値の性格 | 全数値はWebSearchの結果要約(検索側モデルによる要約)経由。原典PDF/HTMLの本文は未確認。「Tier」は出所URLの種別で付与し、原典を直接読んだ意味ではない |
| 検索上限 | 共有の検索枠(200回/ターン)が途中で枯渇し、以降の検索は不可。このため項目8(採用)、項目1の競合比較、項目3の競合金利レンジ等が未取得 |
| 矛盾の扱い | 情報源間で食い違う数値は両方を併記し「矛盾」と明記。推定は「推定」と明記 |
| Tier | T1=会社開示(競合社自身の開示を含む)、T2=規制当局・公的統計、T3=主要報道・業界レポート・法律事務所・学術、T4=ブログ・SNS・空売りレポート・個人サイト |

---

## 最重要の発見(先に要点)

| # | 発見 | 出所Tier |
|---|---|---|
| 1 | 2026-03-17にMuddy WatersがSoFiの空売りレポート公開。論点は「$312M(JPMorgan向け)のローン売却が実は借入ではないか」「学生ローンの割引率」「純償却率(会社3%超 vs MW算出6.1%)」「2025年調整後EBITDAの水増し」。3-30に第2弾で最大約$10億のEBITDA取消リスクを主張。SoFiは「不正確」と反論し法的措置を検討と表明。会計の争点は本調査時点で未解決(再表示・規制当局対応の報道なし) | T4/T3 |
| 2 | Technology Platform(Galileo)は大口顧客の完全離脱で減収。Q1'26売上$75.1M(-27%)、Q2'26 $84.5M(-23%、貢献利益-65%)。顧客名は10-Qで非開示だが、複数の二次報道がChimeと指摘。Chime S-1は2026-03に$18Mの解約料支払い、自社基盤ChimeCoreへ移行と記載 | T1/T3 |
| 3 | 個人ローンのLPB(第三者資金)が急拡大。Q2'26個人ローン組成$10.7B(+54%)のうち第三者向け$3.1B。2026-03-26にさらに$3.6B超の新契約(大手銀行>$10億、金融・保険グループ$6億/12か月、世界トップ5のPEマネジャー最大$20億/2年=条件合意段階)。2025年のLPB契約総額は$100億超 | T1(会社発表) |
| 4 | 米マクロは「雇用緩み+個人ローン延滞は緩やかに上昇、カードは横ばい」。失業率4.2%(2026-09、+29k雇用)。TransUnion個人ローン60日超延滞(借り手ベース)3.81%(前年3.37%)、残高は過去最高$281B(+9.6%)。NY Fed 2026Q2は総延滞4.73%(Q1 4.76%) | T2/T3 |
| 5 | 学生ローン制度変更は2026-07-01発効(Grad PLUS新規廃止、大学院$20,500/年・$100,000、専門職$50,000/年・$200,000、Parent PLUS $20,000/年・$65,000/学生)。SoFiの学生ローン組成はQ1'26 $2.6B、Q2'26 $2.7B(+170%)と過去最高だが、会社側はQ1の増加を借換需要と説明。Grad PLUS廃止による民間市場拡大の試算はNBER約$8B/年のギャップ、Sallie Mae約$5B機会など | T1/T3 |

補足: SoFi株は2026年初来で約-39%〜-41%(T3要約、3-17の空売りレポートと4-29のQ1決算後の約-9〜-13%下落が重なる)。Q3決算は10-27(Wall Street Horizon、未確認の予測)または11-02(Earnings Whispers)。

---

## 1. アプリ(App Store / Google Play)

| 指標 | 値 | 日付 | Tier | 出所 |
|---|---|---|---|---|
| App Store (iOS) 平均評価 | 4.7 | 2026-07時点 | T3 | AppFollow https://apps.appfollow.io/ios/sofi-bank-invest-crypto/1191985736?country=us |
| App Store 総レビュー数 | 385,575件 | 同上 | T3 | 同上 |
| Google Play 評価 | 3.8(52,850 ratings) | 取得日不詳 | T3 | Tech Dev Notes https://techdevnotes.com/apps/android/sofi-bank-investing-crypto/com.sofi.mobile |
| Google Play 別スナップショット | レビュー21,037件、DL約6.8M、カテゴリFinance | 取得日不詳 | T3 | https://techdevnotes.com/apps/android/sofi/com.sofi.mobile (矛盾: 上の52,850と件数が異なる。指標定義の違いの可能性) |
| Google Play インストール階層 | 5M+ | 同上 | T3 | 同上 |
| 米App Store 金融カテゴリ順位 | #32(米国 金融) | 2025-03 | T3 | Similarweb https://similarweb.com/pt/app/apple/1191985736 (古い。現在値は未取得) |
| Sensor Tower DL推定 | Apple 約200K、Android 約90K(期間単位は要約に記載なし) | 2024-10 | T3 | 検索結果群(例: https://sofihouse.substack.com/p/sofi-alt-data-tracker-update 、https://letsdatascience.com/news/sensor-tower-reveals-2025-mobile-app-trends-f9e35c94)。どのページが直接の出所か特定できず。約2年前の値 |
| 2026年のDL推定・順位推移 | 未取得 | - | - | - |

競合(Chime、Robinhood、Cash App、Ally)のアプリ評価・順位・DL比較は未取得。

---

## 2. 預金金利の比較

### 2-1. SoFi 普通預金(Savings/Vaults)APYの推移と現在

| 時点 | APY | 条件 | Tier | 出所 | 備考 |
|---|---|---|---|---|---|
| 2025-08頃 | 約4.60%(推定) | - | T4 | PriceWorld https://priceworld.com/savings/sofi/ | ページは「2026-02時点で3.80%、2025-08比-0.80%」と記載。4.60%は逆算による推定で、ページ自体には書かれていない |
| 〜2025-12-22 | 3.80% | 直接振込等 | T4 | Financer https://financer.com/personal-finance/sofis-high-yield-savings-account/ | |
| 2025-12-23〜 | 3.30% | Eligible Direct Deposit | T3/T4 | Yahoo Finance(例 https://finance.yahoo.com/personal-finance/banking/article/best-high-yield-savings-interest-rates-today-tuesday-april-7-2026-100000962.html)、Financer(上記) | 3.80%→3.30%への引き下げは2025-12-23。当時のブーストは+0.70%(Yahoo) |
| 2026-09-23時点(現在) | 3.30%(ベース) | Eligible Direct Deposit | T3 | Money.com https://money.com/alexpetrakieva/savingsaccounts/ | |
| 同上 | 最大4.20%(3.30%+0.90%ブースト、最大6か月) | 初のSoFi Checking+Savings開設後、直接振込または31日ごとに$5,000の適格入金、期限2026-12-31 | T3 | Motley Fool https://www.fool.com/money/banks/articles/top-savings-account-rates-today-oct-8-2026/ (10月の他日付ページも同内容) | |
| 同上 | 直接振込なし: 0.80%(Money.com)/ 1.00%(Financer) | - | T3/T4 | 上記2サイト | 矛盾(0.80% vs 1.00%) |
| 参考 | SoFi Plus会員は一時ブーストで4.00%まで | 2026-12-31までに加入 | T4 | Financer | |
| 2024年〜2025年前半の推移 | 未取得 | - | - | - | 2024〜2025-08のAPY履歴は検索で取れず |

直接振込条件: Eligible Direct Deposit(給与等の適格直接入金)、または31日ごとに$5,000以上の適格入金のどちらか(Fool)。詳細定義はSoFi公式ページ未確認。

### 2-2. 競合の現在APY(取得日・条件に不確実性あり。いずれも2026年中盤〜10月の二次情報)

| 銀行 | APY | 条件・備考 | Tier | 出所 |
|---|---|---|---|---|
| Chime | 3.75%(Prime、月$3,000以上の直接振込)/ 2.75%(Plus)/ 0.75%(標準) | Chime自社ブログ(2026-04-28付) | T4 | https://www.chime.com/blog/best-high-yield-savings-accounts/ |
| Capital One 360 | 3.50%(別リストで3.80%、矛盾) | 手数料・最低残高なし | T3/T4 | Lendedu https://lendedu.com/blog/best-savings-accounts |
| American Express HYSA | 3.90% | 最低残高なし | T4 | work-club https://work-club.com/best-high-yield-savings-accounts-2026/ |
| Wealthfront | 4.20%(最初の3か月の販促)→ 以降3.30% | | T4 | 同上 |
| Ally | 4.00%(別リスト)/ 最大4.50%(freenance)/ 3%(動画要約)で矛盾 | 現在値の確定不可 | T4 | https://freenance.io/products/high-yield-savings-ally/ ほか |
| Marcus (Goldman) | 3.40% | 現在値として確実な出所なし | T4 | work-club(上記) |
| 市場の上位水準 | 「最大5.00% APY」(他行) | 2026-10-05〜09の見出し | T3 | Motley Fool https://www.fool.com/money/banks/articles/top-savings-account-rates-today-oct-5-2026/ |

注: 競合APYは取得日が不統一で、SoFiとの厳密な同日比較はできない。政策金利は2026-09-16に3.75-4.00%へ引き上げ(下記11-3、未確認)。

---

## 3. 個人ローン市場

| 指標 | 値 | 日付 | Tier | 出所 |
|---|---|---|---|---|
| 無担保個人ローン残高 | 過去最高 $281B(前年比+9.6%) | 2026Q2 | T3 | TransUnion Q2 2026 CIIR(Barchart配信 https://www.barchart.com/story/news/3687356/more-americans-have-access-to-credit-while-debt-growth-has-moderated 、インフォグラフィック https://media.transunion.com/content/dam/transunion/us/business/collateral/infographic/q2-2026-ciir-consumer-lending-infographic.pdf) |
| 同 借り手ベース60日超延滞 | 3.81%(前年同期3.37%) | 2026Q2 | T3 | 同上 |
| 延滞の方向 | 口座数・借り手数ベースで前年比上昇、残高ベースの影響は限定的 | 2026Q2 | T3 | TransUnionインフォグラフィック(上記) |
| 組成の伸び | 「originations up 19.5%」との要約。対象商品(個人ローンかどうか)は要約から特定不可 | 2026Q2 | T3 | StockTitan https://www.stocktitan.net/news/TRU/more-americans-have-access-to-credit-while-debt-growth-has-jllagbaxev22.html |
| 個人ローン残高/組成/延滞の2025〜2026推移(四半期系列) | 未取得 | - | - | - |
| SoFi市場シェア推定 | 未取得(業界組成総額の取得なく算出不可)。参考として、SoFi個人ローン組成 Q1'26 $8.3B、Q2'26 $10.7B(+54%、うち第三者向け$3.1B) | 2026Q1/Q2 | T1 | SoFi 8-K https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000050/a2026q2earningsrelease.htm |
| 競合 LendingClub 組成 | Q2'26 $3.1B(+29%)、HFI純償却率3.2%(前年3.8%)、通期組成ガイダンス$12.2〜12.6B | 2026Q2 | T3(二次要約) | MarketBeat https://www.marketbeat.com/instant-alerts/lendingclub-q2-earnings-call-highlights-2026-07-27/ |
| 競合の金利レンジ(LendingClub、Upstart、Prosper、Discover等) | 未取得 | - | - | - |
| Experianレポート | 未取得 | - | - | - |
| SoFi個人ローン純償却率 | 2.62%(前年比-21bp、前期比-41bp) | 2026Q2 | T1(要約経由) | SoFi Q2発表のBusinessWire要約 https://www.businesswire.com/news/home/20260729569583/en/ |

---

## 4. 学生ローン

### 4-1. 制度変更(One Big Beautiful Bill Act)

| 項目 | 内容 | 発効日 | Tier | 出所 |
|---|---|---|---|---|
| Grad PLUS | 新規借入者への提供を全面廃止。2026-07-01前に連邦ローンの貸出済みの既存学生は、最大3学年または課程修了までのいずれか早い方まで旧上限を維持(レガシー規定)。課程変更・休学で資格を失う可能性 | 2026-07-01 | T3(大学の奨学金窓口。法令の原典はED) | Washington State Univ. https://financialaid.wsu.edu/2025/11/10/one-big-beautiful-bill-act-2026-27-changes-to-federal-financial-aid/ 、Palm Beach Atlantic https://www.pba.edu/financial-aid/policies/one-big-beautiful-bill-act/ ほか複数校 |
| 大学院(Direct Unsub) | 年$20,500、通算(大学院)$100,000 | 2026-07-01 | T3 | 同上 |
| 専門職学位 | 年$50,000、通算$200,000 | 2026-07-01 | T3 | 同上 |
| 全連邦ローン通算上限 | $257,500(Parent PLUS除く)。1校は「$257,000」と記載(誤記の可能性、要確認) | 2026-07-01 | T3 | 同上 |
| Parent PLUS | 年$20,000、学生1人あたり通算$65,000(両親合算) | 2026-07-01 | T3 | 同上 |
| その他 | ハーフタイム未満は在籍負荷に比例して按分、新規借入者はハーフタイム以上が必要 | 2026-07-01 | T3 | 同上 |
| 返済プラン | 新規ローンのデフォルトは新Repayment Assistance Plan(RAP)。既存借り手も選択可。IBRは旧IDRとして唯一新規加入を受付 | 2026-07-01 | T3 | Tate Law https://www.tateesq.com/learn/student-loan-repayment-options 、Finnita https://finnita.com/blog/idr-plans-after-save-shutdown-2026/ (ブログ/商用サイト混在、T3-T4) |
| SAVE終了 | 連邦裁(ミズーリ東部地区)が2026-03-10に無効化したとする情報、EDが2026-03-27に移行方針を発表(1ソース)。別情報では2026-07-01が失効日で、7月以降サービサーが借り手へ順次通知し、各90日で新プラン選択。未選択者は標準または段階標準プランへ自動編入、自動編入開始は約2026-10-01(1ガイド) | 2026-03〜10 | T2/T3/T4 | ED https://www.ed.gov/about/news/press-release/us-department-of-education-announces-next-steps-borrowers-enrolled-unlawful-save-plan 、College Help Guide https://www.collegehelpguide.com/blog/save-plan-ending-july-2026-borrowers-must-act/ (日付の食い違いあり) |

### 4-2. 返済・延滞の状況

| 指標 | 値 | 日付 | Tier | 出所 |
|---|---|---|---|---|
| 連邦学生ローン残高 | $1.651T(前期比-$7B) | 2026Q2 | T2(要約経由) | NY Fed https://www.newyorkfed.org/newsevents/news/research/2026/20260811 、ABA Banking Journal https://bankingjournal.aba.com/2026/08/new-york-fed-household-debt-dipped-to-18-8t-in-q2/ |
| 学生ローン90日超延滞残高比率 | 約10.6%(Q1 10.3%)。2020Q1以来の高水準。NY Fedはデフォルト債権の再報告再開が主因と説明 | 2026Q2 | T2(要約経由) | NY Fed(上記)の二次要約 |
| 学生ローン 重度延滞への流入率 | 7.83%(前年12.88%) | 2026Q2 | T3 | Sovereign Magazine https://sovereignmagazine.com/article/us-household-debt-fell-q2-2026-student-loans (注: 上の「90日超残高比率」とは別指標。再報告による歪みと注記) |
| 賃金差押 | EDが差押通知を送付開始(最大賃金の15%)。通知は初期段階で約1,000件、デフォルト借り手は500万人超 | 記事日付不詳(2026年内) | T3 | Scripps News https://www.scrippsnews.com/us-news/education/millions-of-student-loan-borrowers-face-new-repayment-rules-as-garnishments-restart |
| Treasury Offset(2026年) | 未取得 | - | - | - |

### 4-3. 民間市場への影響試算・市場規模

| 試算 | 値 | 日付 | Tier | 出所 |
|---|---|---|---|---|
| 融資ギャップ(Grad PLUS廃止) | 年約$8B、影響借り手約37万人。民間が埋められるかを論じる | 2026 | T3(学術WP) | NBER Working Paper w35683 (Sarah Turner) https://www.nber.org/papers/w35683 |
| Sallie Mae | Grad PLUS関連機会は完全稼働時で約$5B。CEO Witterは数年で年間組成$4.5〜5B増。2026年の民間組成ガイダンス+12〜14% | 2026-02時点 | T3 | MarketBeat https://www.marketbeat.com/instant-alerts/slm-eyes-next-growth-phase-as-grad-plus-reforms-fuel-12-14-origination-outlook-2026-02-11/ 、Cobalt https://newsletter.cobaltintelligence.com/p/sallie-mae-targets-5-billion-a-year-as-washington-exits-graduate-lending |
| 民間学生ローン市場規模 | College Ave試算: $13B → $24B(ほぼ倍増)。別資料: 約$15B/年の連邦市場が民間・州へ | 2026 | T3/T4 | HelloWarrant https://www.hellowarrant.com/blog/the-future-of-graduate-financing-and-the-10-billion-marketing-opportunity 、Cobalt(上記) |
| SoFiの取り分(アナリスト試算) | BofA: プライベート化したGrad PLUS市場でさらに10ポイントのシェアを取ると新規組成約$1.4B(2025年のBenzinga記事、会社ガイダンスではない) | 2025 | T3 | Benzinga https://benzinga.com/z/46352055 |
| 同 大学側の動き | Yale大学の大学院・専門職向け案内でSoFiを最初の代替として提示(2026-27学年から) | 2026 | T3 | Yale Financial Aid https://financialaid.yale.edu/yales-graduate-professional-student-loan-option |
| 業界全体の在学中民間ローン2026-27予測(単一の権威ある数値) | 未取得(上の試算は定義が異なり比較不可) | - | - | - |

### 4-4. SoFi経営陣の発言・実績

| 項目 | 内容 | 日付 | Tier | 出所 |
|---|---|---|---|---|
| 学生ローン組成 | Q2'26 $2.7B(前年比+170%、過去最高四半期)。Q1'26 $2.6B(前年比2.2倍) | 2026Q1/Q2 | T1(要約経由) | SoFi 8-K https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000050/a2026q2earningsrelease.htm |
| 増加の要因(会社説明) | 10-QはQ1の増加を「借換と、高金利環境での期間延長」と説明 | 2026Q1 | T1 | SoFi 10-Q https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000037/sofi-20260331.htm |
| Noto発言 | 「政府が在学中ローン、Grad PLUS等から手を引くなら、その機会を確実に取りにいく」。検索結果は「4月下旬の決算後コール」としたが、年は未確認でGOP法案審議中の記事(2025年)と同時期の可能性が高い。2026年Q2コールでのGrad PLUS/OBBBA言及は検索で見つからず | 2025-04頃(推定) | T3 | Sherwood News https://www.sherwood.news/markets/sofi-soars-as-gop-cuts-to-federal-student-loans-move-toward-passage 、Stock Taper https://www.stocktaper.com/earningsCallSummary/SOFI/2026/Q1 |
| Q2'26コールの発言原文 | 未取得(トランスクリプト本文を読めず)。トランスクリプトの所在: https://s27.q4cdn.com/749715820/files/doc_financials/2026/q2/SoFi-2Q-2026-Earnings-Transcript_FINAL.pdf | - | T1 | - |
| 他の民間貸し手(Sallie Mae Q2'26実績、College Ave、Navient等) | 未取得 | - | - | - |

---

## 5. LPB(Loan Platform Business)とプライベートクレジット

### 5-1. SoFiと第三者の契約一覧

| 日付 | 相手先 | 規模・条件 | Tier | 出所 |
|---|---|---|---|---|
| 2024-10 | Fortress | 個人ローン購入$2B(フォワードフロー型として記述する二次情報もあり、会社はLPB契約と表記) | T3 | Covenant Lite #38 https://covenantlite.substack.com/p/covenant-lite-38-fortress-and-blue |
| 2025-01-16 | PGIM Fixed Income | $525M の証券化契約 | T1 | BusinessWire https://www.businesswire.com/news/home/20250116388146/en/ |
| 2025-03-13 | Blue Owl funds | 最大$5B、2年契約、個人ローン。資本軽量・手数料型収益へのシフトと説明 | T1 | BusinessWire https://www.businesswire.com/news/home/20250313368726/en/SoFi-Expands-Loan-Platform-Business-with-$5-Billion-Agreement-with-Blue-Owl-Capital-Funds |
| 2025-04-17 | Fortress、Edge Focus | $3.2B拡大(Fortress $2B延長で同社の総コミットは$5B超) | T1 | BusinessWire https://www.businesswire.com/news/home/20250417276382/en/ |
| 2026-03-26 | ①グローバル大手銀行 ②金融・保険グループ ③世界トップ5のプライベート資産運用会社 | ①>$1B(成約) ②$600M/12か月(成約) ③最大$2B/2年(条件合意、未成約)。合計>$3.6B。2025年のLPB契約累計は>$10B | T1 | https://investors.sofi.com/news/news-details/2026/SoFi-Expands-Loan-Platform-Business-with-Multiple-New-Agreements-Totaling-Over-3-6-Billion/default.aspx |
| 条件の一般形 | SoFiは組成・紹介手数料と、サービシング手数料を得る。パートナーは通常、組成の数日以内にパー近傍で購入 | - | T3 | Covenant Lite(上記)、Alternatives Watch https://www.alternativeswatch.com/2025/03/13/blue-owl-backs-sofi-loan-platform-fintech-private-credit/ |

### 5-2. LPBの実績(会社開示、参照用)

| 指標 | 値 | 日付 | Tier | 出所 |
|---|---|---|---|---|
| LPB組成(個人ローン) | Q2'26 $3.1B、手数料収益$140.9M(サービシングキャッシュフロー込みで連結調整後売上に$143.3M) | 2026Q2 | T1 | SoFi 10-Q https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000054/sofi-20260630.htm |
| 個人ローン組成 | Q1'26 $8.3B(前年比+51%、うち第三者向けの増加が$3.0B)、Q2'26 $10.7B(+54%) | 2026Q1/Q2 | T1 | SoFi 10-Q(Q1) https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000037/sofi-20260331.htm |
| 総組成 | Q2'26 $14.8B(+69%)、内訳 貸借対照表側$11.7B + LPB $3.1B | 2026Q2 | T1 | SoFi 8-K(上記) |

### 5-3. 2026年の消費者ローン向けプライベートクレジット(報道)

| 項目 | 内容 | 日付 | Tier | 出所 |
|---|---|---|---|---|
| 規模 | プライベートクレジットの消費者ローン残高 約$350B(2019年は$200B未満)。2025年に組成された個人ローンの約4分の1がプライベートクレジットのフォワードフローで調達(前年は約6%)。Jefferies推計、WSJ報道経由 | 2026-04 | T3 | PYMNTS https://www.pymnts.com/news/investment-tracker/2026/private-credits-consumer-debt-holdings-jump-150-billion-since-2019/ |
| Blue Owl | 2025年に約$18Bのフォワードフロー契約(PayPal、SoFi、LendingClub等)。Pagayaから$2.4Bの消費者ローン購入契約 | 2025〜2026 | T3 | 同上、Alternatives Watch(上記) |
| 価格・スプレッド | Morgan Stanley 2026年中間見通し: テック向けアンダーライティング減速とBDC等の純流出が新規ローンのスプレッド拡大に寄与、貸し手はリスクに見合う報酬を再び得ている。消費者ローンのフォワードフロー個別の価格条件は未取得 | 2026年中盤 | T3 | https://www.morganstanley.com/im/en-us/individual-investor/insights/outlooks/private-credit-midyear-outlook-2026.html |
| ストレス兆候 | Stone Ridgeの一部プライベートクレジットファンドが償還請求の11%のみ履行(2026-03)。保有にAffirm、LendingClub、Upstart等のフィンテック債権 | 2026-03 | T3 | PYMNTS https://www.pymnts.com/loans/2026/private-credit-rewards-distribution-as-liquidity-tightens/ |
| 規制当局の注意喚起 | FSBがプライベートクレジットの脆弱性報告で、資産運用会社が銀行等から新規組成ローンを継続購入するフォワードフローと、組成プラットフォーム自体の取得に言及 | 2026-05-06 | T2/T3 | FSB https://www.fsb.org/uploads/P060526.pdf |
| 空売り筋の論点 | Muddy Waters: JPMorgan向け$312Mの売却取引は借入として計上すべき(UCC届出を根拠)。SoFiは否定 | 2026-03 | T4/T3 | 下記10-4 |

---

## 6. 証券化(SoFi Consumer Loan Program 等)

| 案件・指標 | 内容 | 日付 | Tier | 出所 |
|---|---|---|---|---|
| SCLP 2026-2 | $688.5M。BofA Securities主幹事。4クラス全て固定金利。Class A $515.9M(Fitch・S&P: AAA)。信用補完 A 31.67% / B 23.32% / C 14.89% / D 8.66%。初期オーバーコラテラル8.2%(2021-1は7.0%)。法的最終 2036-03-25。Class A〜Dはスプレッド・クーポン未取得 | 2026年(月は要約から特定不可。法的最終2036-03から2026-03頃の可能性があるが推定) | T3 | Asset Securitization Report https://asreport.americanbanker.com/news/sofi-raises-688-5-million-from-consumer-abs |
| 直近案件(約$460M、固定金利4クラス、Fitch/S&P: AAA/AA/A/BBB) | 記事は「SCLP 2026-3と比較」と記載。案件名は不明(2026-4の可能性、推定)。クラスA〜Dの格付はAAA/AA/A/BBB | 2026年(記事は約31日前) | T3 | Asset Securitization Report https://asreport.americanbanker.com/news/sofis-latest-consumer-loan-abs-raising-460-million-has-higher-earners (今回の再検索では内容を再確認できず) |
| SCLP 2025-4 格付変更 | Fitchが Class BをAA+、Class CをA+へ格上げ、Class AはAAA、Class DはBBBを据え置き | 日付不詳 | T3 | TradersUnion https://tradersunion.com/news/financial-news/show/3574840-fitch-upgrades-sofi-loan-notes/ |
| 共同拠出(co-contributor)型証券化 | Q1'26: LPB経由ローンの $919M。Q2'26: 2件で合計 $1.4B | 2026Q1/Q2 | T1 | SoFi 8-K(Q1) https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000020/a2026q1earningsrelease.htm 、(Q2) 上記 |
| 参考: SCLP 2025-1 | $697.6M、2025-02-28成約、35投資家、Goldman Sachs構造化、BofA共同主幹事。加重平均スプレッド87bp、オールイン利回り5.10%(1アウトレット報道) | 2025-03-03公表 | T1/T3 | SoFi https://www.sofi.com/press/sofi-closes-697-6-million-securitization-loan-platform-business-volume/ |
| 参考: SCLP 2025-2 | $690.3M、借り手加重平均所得$179,588、FICO750(DBRS) | 2025年 | T3 | Asset Securitization Report https://asreport.americanbanker.com/news/sofis-pool-of-consumer-loans-secures-690-3-million-in-abs |
| SoFi Professional Loan Program(学生ローン)2026年の案件 | 未取得(検索で2026-A/Bの存在確認できず) | - | - | - |
| 2026年の各案件のスプレッド | 未取得(2026-2を含めて非掲載) | - | - | - |

---

## 7. テクノロジープラットフォーム競合

### 7-1. SoFi Technology Platform(Galileo/Technisys)の最新

| 指標 | Q1'26 | Q2'26 | Tier | 出所 |
|---|---|---|---|---|
| セグメント純収益 | $75.1M(前年比-27%) | $84.5M(前年比-23%、前期比+13%) | T1 | SoFi 10-Q Q1 https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000037/sofi-20260331.htm 、8-K Q2 https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000050/a2026q2earningsrelease.htm |
| 貢献利益 | $12.0M(-61%) | $11.8M(-65%)、マージン14%(前年30%) | T1 | 同上 |
| 対応口座数 | 133M(前年158M) | 134.8M(前年160.0M、-16%)。SoFi自社口座をPaaS分として算入する定義に変更済みで連続性なし | T1 | 同上 |
| 減収の理由 | 2025-12-31前に完全移行した大口顧客の離脱。Q2は技術サービス手数料が$76.3M減(半期) | | T1 | SoFi 10-Q(Q2) https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000054/sofi-20260630.htm |
| 経営陣の説明 | 離脱顧客を除く前年比(like-for-like)で約+12%。Q1に新規13社が収益化。Galileo/TechnisysをSoFi Technology Solutionsに統合 | 2026Q1 | T1/T3 | Motley Fool Q1'26コール https://www.fool.com/earnings/call-transcripts/2026/04/29/sofi-sofi-q1-2026-earnings-call-transcript/ |

### 7-2. 離脱した顧客と競合の動き

| 項目 | 内容 | 日付 | Tier | 出所 |
|---|---|---|---|---|
| 顧客名 | SoFiの10-Qは非開示。Simply Wall StとYahoo FinanceがChimeと指摘(二次推定) | 2026 | T3/T4 | Simply Wall St https://simplywall.st/community/narratives/us/diversified-financials/nasdaq-sofi/sofi-technologies/c1wqpv3a-sofi-record-everything-down-13percentthe-galileo-wound-the-muddy-waters-shadow-and-a-business-growing-too-fast-for-its-own-stock-price 、Yahoo https://finance.yahoo.com/markets/stocks/articles/sofis-tech-platform-revenue-quiet-045000270.html |
| Chime側の事情 | S-1: Galileo契約改定で最低月額支払いを撤廃し、2026-03に$18Mの解約料を支払う。2026-06-30までGalileo側は有因解約のみ可。自社プロセッサChimeCoreへ移行。別要約は一時費用$33Mとし矛盾 | S-1(2025) | T1(Chime)/T3 | Substack解説 https://fintechdd.substack.com/p/galileos-total-accounts-drop-explained 、Sacra https://sacra.com/chat/h/fcab73a0-19a6-44f9-8642-3ea5ef685757/ |
| Marqeta Q2'26 | TPV約$120B(+32%)、純収益$176M(+17%)、粗利$122M(69%)、GAAP純利益$8M、調整後EBITDA$37M(+31%)。下期は減速、通期純収益成長12〜13%の見通し。CEO Gardnerが交代の意向と報道 | 2026-08-04 | T1(Marqeta)/T3 | SEC 8-K https://www.sec.gov/Archives/edgar/data/0001522540/000152254026000061/mqearningsrelease-q2x2026.htm 、MarketBeat https://www.marketbeat.com/instant-alerts/marqeta-q2-earnings-call-highlights-2026-08-04/ 、Digital Transactions https://www.digitaltransactions.net/marqeta-posts-big-numbers-as-ceo-gardner-says-hes-moving-out-of-his-ceo-role/ |
| 市場構造 | 旧来型プロセッサ(FIS、Fiserv、TSYS等)がカード取扱高の大半(80〜90%との未検証推定)。モダン系(Stripe、Marqeta、Lithic等)は$1.5B→$7.5Bに成長との予測(Totavi)。米国発行プロセッサ市場は2035年に$16.8B | 2026 | T4 | Sacra https://sacra.com/chat/h/db3649d1-34eb-4bdb-8121-1b9c00989ada/ 、Totavi要約 https://www.webull.com/news/15667363933012992 (信頼度低) |
| i2c、Lithic、FISの個別実績、Galileoの2026年の顧客獲得・離脱の個別報道 | 未取得(Chime以外の離脱報道、2026年の新規契約発表は見つからず) | - | - | - |

---

## 8. 採用

| 項目 | 内容 |
|---|---|
| SoFiの求人数の推移(LinkedIn等) | 未取得 |
| 人員削減(レイオフ)の有無 | 未取得(検索枠枯渇のため調査できず。検索結果の範囲では2026年のSoFiのレイオフ報道は目に入っていないが、これは調査していないことの裏返しで「無い」ことの確認ではない) |

---

## 9. 競合KPI(最新、各社の2026Q2決算)

| 会社 | 指標 | 値 | 日付 | Tier | 出所 |
|---|---|---|---|---|---|
| Nubank (Nu Holdings) | 顧客数 | 139M(ブラジル約118M、メキシコ15.8M)。Q2に約4M純増 | 2026-08-13決算 | T1/T3 | 6-K https://www.sec.gov/Archives/edgar/data/0001691493/000129281426004222/nupr2q26_6k.htm 、決算要約 https://www.allinvestview.com/earnings/NU/q2-2026/ |
| 同 | ARPAC | 約$17(過去最高と報道) | 同上 | T3 | 同上、https://www.dgabc.com.br/Noticia/4341081/nubank-tem-lucro-liquido-recorde-de-us-1-1-bi-no-2-tri-alta-de-49-ante-2-tri-de-2025 |
| 同 | 純金利マージン | 22.9%(前期21.1%、前年18.8%、ブラジル報道。公式値は未確認) | 同上 | T3 | 同上 |
| 同 | 預金 | 約$45.3B(+18% FXニュートラル)。売上$5.9B、純利益約$1.1B(+49%)、効率性19.5% | 同上 | T3 | 同上 |
| 同 | 資金コスト | 未取得 | - | - | - |
| Robinhood | 資金入り顧客(Funded Customers) | 28.4M(前年比+1.9M、+7%) | 2026-07-29決算 | T1 | https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-second-quarter-2026-results |
| 同 | Goldサブスクライバー | 4.8M(+39%)、資金入り顧客の17% | 同上 | T1 | 同上 |
| 同 | 純入金 | Q2 $21.7B(見出しは$22B)、直近12か月 $75.7B | 同上 | T1 | 同上 |
| 同 | Robinhood Banking | 入金$3B超、利用顧客24万人超、約40%が給与振込を設定(6月末)。開始時期は今回の検索では不明(Q2の新規ローンチではなく既に稼働中の扱い) | 同上 | T1 | 同上 |
| 同 | 売上・EBITDA・ARPU | 売上$1.31B(+32%)、調整後EBITDA $741M(+35%)、ARPU $187(+24%) | 同上 | T1 | 同上 |
| Chime | アクティブ会員 | 10.4M(+20%)、Q2純増約0.2M、直近1年で+1.7M | 2026-08-05決算 | T1 | https://www.sec.gov/Archives/edgar/data/0001795586/000179558626000046/ex991q226.htm 、BusinessWire https://www.businesswire.com/news/home/20260805473866/en/ |
| 同 | ARPAM | $260(+6%) | 同上 | T1 | 同上 |
| 同 | 売上・利益・見通し | 売上約$670M(+27%)、粗利$595M、純利益$28M(2四半期連続GAAP黒字)。Q3売上ガイダンス$680〜690M、通期$2.725〜2.745B、調整後EBITDA$465〜475M、2026年純増1.8M(従来1.4M) | 同上 | T1 | 同上 |
| LendingClub | 組成額 | Q2'26 $3.1B(+29%)。通期ガイダンス$12.2〜12.6B | 2026-07-27決算 | T3(二次要約) | MarketBeat(上記) |
| 同 | 預金 | Q1'26 $10.2B(+14%)。Q2の値は未取得 | 2026Q1 | T3 | 247WallSt https://247wallst.com/companies/lc/earnings/ ほか |
| 同 | 収益性・信用 | 税前利益$76M(過去最高)、EPS $0.50(+52%)、HFI純償却率3.2%(前年3.8%)、通期EPSガイダンス$1.80〜1.90 | 同上 | T3 | MarketBeat(上記) |
| 同 | LevelUp | 個人ローン借り手が新規預金口座の15%超(Q1)、LevelUp Checking顧客の60%が借り手 | 2026Q1 | T3 | PYMNTS https://www.pymnts.com/earnings/2026/lendingclub-grows-levelup-base-as-loan-originations-rise/ |

(参考) SoFi自社 2026Q2: 会員15.8M(+35%)、商品24.4M(+42%)、預金$45.5B(四半期で+$5.3B)、NIM 5.98%、純利益$157M、調整後純収益$1.2B(+40%)、調整後EBITDA $358M(+44%)、2026年通期調整後純収益ガイダンス$4.75〜4.85B(上方修正)。EBITDAガイダンスは据え置き。CFOは2026年に1〜2回の利上げ想定(当初の2回利下げ想定から変更)(T1の要約経由)。出所: SoFi 8-K(上記)、Nasdaq https://www.nasdaq.com/articles/sofi-technologies-q2-earnings-call-highlights

---

## 10. 規制・訴訟

### 10-1. SoFi Bank

| 項目 | 内容 | 日付 | Tier | 出所 |
|---|---|---|---|---|
| 監督当局 | OCC(National Bank)。2022-01に買収(Golden Pacific Bank)とバンク設立を条件付承認、払込資本$750M等の条件 | 2022-01 | T3(二次要約) | Troutman https://www.troutman.com/insights/sofi-gets-occ-approval-to-acquire-national-bank-but-must-stay-away-from-crypto 、Mondaq https://mondaq.com/unitedstates/financial-services/1153074/occ-conditionally-approves-fintech-company-applications-to-charter-national-bank |
| 暗号資産制限 | 承認時にOCC事前不異議なしでの暗号資産業務を禁止(運営協定の期間中)。現在の協定の状況は未確認 | 2022 | T3 | 同上 |
| 資本増強 | 最大$360Mの資本注入をOCCが条件付承認(2024)。12 USC 1818で執行可能な条件 | 2024 | T2 | OCC https://occ.gov/topics/charters-and-licensing/interpretations-and-actions/2024/ca1326.pdf |
| 2026年の行政処分(同意命令、CFPB措置等) | 検索結果の範囲では確認できず(網羅的な否定確認ではない) | - | - | OCC執行措置データベース、CFPB執行ページ、SoFiの10-Qの訴訟欄は未確認 |

### 10-2. CFPB

| 項目 | 内容 | 日付 | Tier | 出所 |
|---|---|---|---|---|
| 資金・人員 | 代行長官Vought。Fedに第2会計四半期分$145Mを要請(2025-12-30の裁判所命令を受けて)。人員は約1,700→約1,300(2025-12初)。NTEU v. Vought(大量解雇の差止め)はD.C.巡回区控訴裁のフルコート審理(2026-02に口頭弁論) | 2026-01〜04 | T3 | Covington https://www.cov.com/-/media/files/corporate/publications/2026/01/funding-haze-and-deregulatory-pursuits-the-cfpb-in-2026.pdf 、Banking Dive https://www.bankingdive.com/news/vought-concedes-cfpb-funding-fed-powell-nteu-jackson/809349/ |
| 規則制定 | Reg B、1071、1033(オープンバンキング)が優先。ノンバンクの大規模参加者の定義を4市場(自動車金融、信用情報、債権回収、国際送金)で見直し。個人ローンは対象外。提案は2026-08〜09の予定(公表有無は未確認) | 2026-07 | T3 | PwC https://www.pwc.com/us/en/financial-services/regulatory-services/publications/assets/pwc-finreg-our-take-july-24-2026.pdf |
| 人事 | 常任長官候補Brian Johnsonの上院銀行委員会公聴会 2026-07-23 | 2026-07 | T3 | PwC(上記) |
| D.C.巡回区控訴裁の判断結果 | 未取得 | - | - | - |

### 10-3. ステーブルコイン(GENIUS Act)とSoFiの対応

| 項目 | 内容 | 日付 | Tier | 出所 |
|---|---|---|---|---|
| GENIUS Act施行 | 最終規則公表から120日後または2027-01-18の早い方。規則制定の法定期限は2026-07-18 | - | T3 | Chapman GENIUS Act Tracker https://www.chapman.com/publication-genius-act-rulemaking-tracker |
| OCC | 2026-02に規則案。Comptroller Gouldが2026-08-19に「11月までに最終規則」と表明。2026-10-18時点で最終規則公表の確認なし | 2026-08 | T3 | PYMNTS https://www.pymnts.com/legal/2026/occ-promises-final-rule-for-genius-act-by-november/ |
| Treasury(AML/制裁) | 提案2026-04公表、コメント期限2026-06-09 | 2026-04 | T3 | Chapman(上記) |
| SoFiの対応 | 暗号資産取引を2025-11に再開(段階展開)。SoFiUSD(銀行発行ステーブルコイン)を2026-06に消費者向けにローンチとするLoeb & Loebの分析(アプリ内で保有・送金・24/7出金、Ethereum/Solana)。一方Cointelegraphは「社内決済のみ稼働」とし矛盾 | 2026-06 | T3 | Loeb https://www.loeb.com/en/insights/passle/2026/06/sofi-launches-first-bankissued-stablecoin-sofiusd-on-consumer-banking-app 、Cointelegraph https://cointelegraph.com/news/sofi-us-dollar-stablecoin-bank-fintechs |
| 利回り規制との関係 | GENIUS Actは許可決済ステーブルコイン発行者による保有者への利息・利回りの支払いを禁止。そのためSoFiUSDは無利息。今後はSoFiUSDからトークン化預金(利息あり、FDIC保険)への交換を計画し、2026Q3導入予定(Cryptometer)。他行・フィンテック向けの白ラベル提供も計画(Coin360、信頼度低) | 2026 | T3/T4 | Loeb(上記)、Cryptometer https://www.cryptometer.io/news/sofi-expands-stablecoin-access-to-15-million-users-in-major-crypto-push/ 、Coin360 https://coin360.com/news/sofi-launches-sofiusd-bank-issued-stablecoin-public-blockchain |
| 準備資産 | 「Fed預け金に1:1」(Stablecoininsider)と「高品質流動資産、現金・要求払預金を含みうる」(Loeb、SoFi規約の読み)で食い違い | 2026 | T3/T4 | 同上 |

### 10-4. 空売り・訴訟・株価材料

| 日付 | 事象 | Tier | 出所 |
|---|---|---|---|
| 2026-03-17 | Muddy Watersが空売りレポート公開。(a) $312Mのローンパッケージを売却したと主張しているが実際は財務構造でオンバランス維持(未計上債務の疑い)、(b) 学生ローンに誤った割引率を使用(2025年の不当な公正価値益$259M)、(c) 純償却率: 会社約3%(Q4)に対しMW算出6.1%、(d) 2025年調整後EBITDA $1.05Bは約90%水増しで真の値は$103M。「Enron」に例える。SoFiに送付した11の質問に回答なしと主張 | T4(利害関係者) | Muddy Waters 11 Questions資料 https://muddywatersresearch.com/wp-content/uploads/2026/03/MWR_SOFI_11QUESTIONS_0200321.pdf 、Fortune https://www.fortune.com/2026/03/25/muddy-waters-sofi-stock-accounting 、Yahoo Finance https://finance.yahoo.com/markets/stocks/articles/sofi-technologies-calls-muddy-waters-153105389.html |
| 2026-03-17 | SoFiが同日に反論「財務諸表への根本的な理解不足」「不正確」、Muddy Watersに対する法的措置を検討 | T1/T3 | SoFi https://s27.q4cdn.com/749715820/files/doc_news/SoFi-Responds-to-Inaccurate-Short-Seller-Report-2026.pdf 、Seeking Alpha https://seekingalpha.com/news/4565743-sofi-calls-short-report-inaccurate-explores-legal-action |
| 2026-03-30 | MW第2弾: UCC届出(ユタ州)に基づき$312MをJPMorgan向けの借入と主張。再表示があれば約$1BのEBITDA消失と資本比率低下のリスク | T4/T3 | Stocktwits https://stocktwits.com/news-articles/markets/equity/sofi-stock-worst-quarter-muddy-waters-jpmorgan-warning-1b-ebitda-risk/cZEPV9IRINx |
| 2026-03〜 | 市場反応: 当初は小幅下落(Fortune)。Mizuho Dolev「詳細だが重要事実を誤解」。Barclays目標株価$28→$18(Hold維持)。Goldman Sachsも目標引下げ。1Q'26に株価-32%との要約も | T3 | Fortune(上記)、Yahoo、TipRanks https://www.tipranks.com/news/sofi-stock-price-forecast-what-financial-analysts-expect-right-now |
| 2026-03、05-09、05-12 | Noto CEOが公開市場で自社株購入 | T3 | TIKR https://www.tikr.com/blog/sofi-stock-slips-4-after-muddy-waters-report-heres-what-happens-next |
| 2026-04-29 | Q1決算後に株価約-9〜-13%。Tech Platform減収と通期ガイダンス据置が材料 | T3 | Yahoo https://finance.yahoo.com/markets/stocks/articles/sofi-slides-9-q1-earnings-125023553.html |
| 2026-05-04 | Block & Leviton が証券法違反の調査を告知(募集であり訴訟提起ではない) | T3 | MarketScreener https://www.marketscreener.com/news/sofi-technologies-inc-alert-securities-fraud-investigation-by-block-leviton-could-allow-investo-ce7f58dfdb8cf220 |
| 2026-06-27 | Signal Law Groupが投資家向け注意喚起(不正の認定ではない) | T3 | https://www.2news.com/online_features/press_releases/signal-law-group-issues-vrs-bulletin-on-sofi-technologies-inc-sofi/article_d4b5fe1d-be52-5593-a4f7-44bbf456d11d.html |
| 提起済み証券集団訴訟 | 検索範囲では未確認(PACER/Stanford SCAでの確認が必要) | - | - |
| 5月以降のMW・SoFiの追加動向 | 未取得(7〜9月の新展開は検索で見つからず) | - | - |
| 資本面の論点 | 過去に約$3Bの増資があり希薄化懸念、2025-12の公募価格から40%超下落との要約。EBITDA/金利感応度の指摘もあり目標株価$15の例 | T3/T4 | TIKR https://www.tikr.com/blog/sofi-stock-is-down-over-40-from-its-december-offering-price-heres-the-path-to-27-by-2028 、Quiver https://www.quiverquant.com/news/SoFi+slips+after+price-target+cut+highlights+capital+concerns+ahead+of+earnings |

---

## 11. マクロ消費者信用

### 11-1. 米失業率

| 時点 | 値 | Tier | 出所 |
|---|---|---|---|
| 2026-09(2026-10-02公表) | 4.2%(非農業雇用 +29k)。失業者約710万人。2026-03以降4.1〜4.3%のレンジ | T2 | BLS https://www.bls.gov/news.release/archives/empsit_10022026.htm (要約経由) |
| 2026-08 | 4.1%。8月雇用は+133kに改定(二次情報) | T3 | NCH stats https://nchstats.com/?p=13175 |
| 2026-06 | 4.2%(5月4.3%)。6月雇用+57k、労働参加率61.5%(ポスト・パンデミック最低) | T3 | TrendForce/Walnut Invest等(検索要約。AI生成要約が混在し信頼度低) |
| 次回公表 | 2026-11-06 | T3 | 同上 |
| 完全な月次系列(2026-01〜09)、2025年系列 | 未取得 | - | - |

### 11-2. NY Fed 家計債務・信用レポート 2026Q2(2026-08-11公表)

| 指標 | 2026Q2 | 比較 | Tier | 出所 |
|---|---|---|---|---|
| 家計債務総額 | $18.771T(-$13B、-0.1%、2020年以来初の減少) | 主因は住宅ローン-$74B(2013Q2以来最大の減少) | T2(要約経由) | NY Fed https://www.newyorkfed.org/newsevents/news/research/2026/20260811 、Tribune India https://www.tribuneindia.com/news/business/us-household-debt-drops-by-usd-13-bn-to-usd-18-8-tn-in-q2-2026-federal-reserve-bank-of-new-york/ 。Cryptobriefingは「+$18B」と反対方向の報告で矛盾(外れ値) |
| クレジットカード残高 | $1.263T(+$21B) | | T2/T3 | 同上 |
| 自動車ローン残高 | $1.713T(+$28B) | | T2/T3 | 同上 |
| 全債務の延滞(何らかの段階)比率 | 4.73% | Q1 4.76% | T2/T3 | 同上、ABA Banking Journal(上記) |
| 重度延滞への流入率(全体) | 2.57% | 前年2.91% | T2/T3 | Sovereign Magazine(上記) |
| クレジットカード 重度延滞への流入率 | 6.97% | 前年6.93% | T2/T3 | 検索要約(NY Fed表への参照。早期/後期の区分は要約間で食い違い、確認要) |
| カード残高の90日超比率 | 12.9% | 前年12.2% | T2/T3 | 同上 |
| 自動車ローン 重度延滞流入率 | 3.00% | 前年2.93% | T2/T3 | 同上 |
| 住宅ローン 重度延滞流入率 | 1.52% | 前年1.29% | T2/T3 | 同上 |
| HELOC 重度延滞率 | 1.15% | 横ばい | T2/T3 | 同上 |
| 学生ローン | 上記4-2参照 | | | |
| 個人ローン(NY Fedの「その他」区分含む) | 未取得 | | | TransUnionの個人ローン延滞は上記3 |

### 11-3. 金利環境

| 項目 | 内容 | 日付 | Tier | 出所 |
|---|---|---|---|---|
| FF金利 | 2026-09-16のFOMCで25bp利上げ、3.75〜4.00%(12-0の全会一致、2023-07以来初の利上げ、議長Warsh、年末までにもう1回の利上げ想定)。公式のFOMC声明は未確認で、全て二次情報 | 2026-09-16 | T3 | Admiral Markets https://admiralmarkets.com/analytics/traders-blog/fed-raised-interest-rates 、Forex Fundamentals https://forexfundamentals.com/economic-calendar/fomc/2026-09-16 |
| 直前の水準 | 3.50〜3.75%(2025-12から据置)。2026-07は9対3で据置、反対3名は利上げ派 | 2026-07 | T3 | KuCoin https://www.kucoin.com/blog/september-2026-fomc-decision-will-the-fed-hike-rates-or-hold 、FutureSearch |

---

## 取れなかった項目

| # | 項目 | 状況 |
|---|---|---|
| 1 | アプリ: 競合(Chime、Robinhood、Cash App、Ally)との評価・順位・DL比較、SoFiの現在の金融カテゴリ順位、2026年のSensor Tower/Appfiguresによる推移 | 未取得。取得できたのはSoFiのiOS評価4.7(385,575件)とGoogle Play評価3.8、古い順位(2025-03)と2024-10のSensor Tower値のみ |
| 2 | 預金: SoFiの2024〜2025前半のAPY履歴、各競合の同日APY(取得日が不統一で矛盾あり)、SoFi直接振込条件の公式定義 | 一部のみ。SoFi公式サイトを読めていない |
| 3 | 個人ローン: Experianレポート、TransUnionの個人ローン残高・組成・延滞の2025〜2026四半期系列、SoFiの市場シェア推定、競合(LendingClub、Upstart、Prosper等)の金利レンジ | 未取得または単一時点のみ |
| 4 | 学生ローン: SoFi経営陣の2026年コールでのGrad PLUS/OBBBA発言原文、Sallie Mae等の2026Q2実績、業界全体の2026-27民間在学中ローン予測の単一権威値、Treasury Offsetの2026年状況、制度日付の原典(ED/FSA)確認、SAVE無効化の日付の食い違い解消 | 未取得または二次情報のみ |
| 5 | LPB/プライベートクレジット: 消費者ローンのフォワードフロー個別の価格・条件、Fortress関連の2026年の動向、JPMorgan取引($312M)の会社側説明(10-Q注記等) | 未取得 |
| 6 | 証券化: 2026年各案件(SCLP 2026-1〜4)の名称・日付・スプレッド・クーポン、KBRA/Moody's/DBRSの格付、SoFi Professional Loan Program(学生ローン)の2026年案件 | 未取得。2026-2の構造と信用補完のみ取得 |
| 7 | テック競合: i2c、Lithic、FISの実績、Galileoの2026年の新規契約・Chime以外の離脱報道、Chime=離脱顧客の一次確認(SoFi側は非開示) | 未取得または二次推定のみ |
| 8 | 採用: SoFiの求人数推移(LinkedIn等)、人員削減の有無 | 全く未取得(検索枠枯渇) |
| 9 | 競合KPI: Nubankの資金コスト、LendingClubのQ2預金、各社の原典(決算PDF)確認 | 未取得 |
| 10 | 規制: SoFi Bankへの2026年OCC/CFPB措置の網羅的な否定確認、D.C.巡回区控訴裁の判断、SoFi運営協定(暗号資産制限)の現状、提起済み集団訴訟の有無、2026-05以降のMuddy Waters/SoFiの動き | 未取得 |
| 11 | マクロ: 失業率の2026年の完全な月次系列、NY Fedの個人ローン区分の延滞、Fed政策金利の公式声明確認 | 一部のみ |
| 共通 | WebFetchとcurlで原典を直接読めなかったため、全数値が検索要約経由。後続の分析で使う前に、NY Fed、BLS、TransUnion、SoFi 10-Q/8-K、Muddy Watersレポートの原典での再確認を推奨 | |
