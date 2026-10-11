# サイバーセキュリティ業界の構造と動向(定性調査)

評価基準日: 2026-10-11 / 取得日(すべての出典): 2026-10-11 / 作成: Sonnet 調査担当 / 状態: **部分完了(WebSearch 14回の上限を使い切った。8節のうち、数値の裏付けが取れたのは一部)**

## 0. 読み方と既知の制約

- **取得手段**: WebSearch のみ(共通基準 §2)。検索結果は「要約文+出典URL」であり、ページ本文は開いていない。そのため、数値の多くは「検索要約が引用した値」で、原文での再確認はしていない。
- **Tier の付け方**(research-protocol §2): Tier 1=会社開示(決算発表、IR、SEC提出書類、会社のプレスリリース)、Tier 2=公的統計・業界団体、Tier 3=主要報道・調査会社・アナリスト、Tier 4=ブログ・SNS・まとめサイト・ベンダーのマーケティング記事。調査会社 Gartner の公式発表は Tier 3 のうち「発表主体の一次資料」として扱う。
- **「単独出典」の印**: 他の出典で裏取りできていない数値。統括は本文の根拠にせず、会社IRか Gartner 原本で確認すること。
- **食い違い**は両論併記し「未確定」と書いた。欠損は「欠損」と書き、推測で埋めていない。
- **検索予算の使い方**: 14回(複合クエリ、extended)。節ごとの到達度は次のとおり。

| 節 | 到達度 | 主な欠損 |
|---|---|---|
| 1 市場規模 | 総額は取得(Gartner 2025・2026・2027)。セグメント別は一部 | クラウド・アイデンティティ・SecOps/SIEM・データの各セグメント、IT予算比率、IDC |
| 2 利益プール | Palo Alto の粗利率・営業利益率のみ | 他5社の利益率、セグメント別の市場規模・成長率 |
| 3 統合とM&A | Wiz・CyberArk・Armis の完了を取得 | Chronosphere・Protect AI・Red Canary・Splunk の状態、顧客のベンダー数削減の調査 |
| 4 Microsoft | 顧客数の開示のみ | 最新のセキュリティ売上、E5の動向、専業への影響の定量分析 |
| 5 AIの影響 | (b)(c)は良好。(a)(d)は薄い | (a)の製品別の売上規模、(d)のOktaへの影響 |
| 6 株価・バリュエーション | ETF騰落とイベントを取得 | セクター倍率と過去平均の比較、BUGの年初来 |
| 7 規制 | CISA 2015・CIRCIA・SEC規則のみ | NIS2、DORA、CISA予算、ゼロトラスト指令 |
| 8 大規模事件 | 事件の概要を取得 | 需要・競争への影響、2025年11〜12月のCloudflare障害、CrowdStrike障害の後日談 |

## 1. セキュリティ支出は2026年に約2,400〜2,500億ドルへ、年率10%台前半で伸びると予測されている

**用語**: エンドユーザー支出=企業・組織が実際に支払う金額(ベンダーの売上とは範囲が異なる)。

| 項目 | 数値 | 出典名 | 出典URL | 出典日 | Tier | 備考 |
|---|---|---|---|---|---|---|
| 2025年の世界の情報セキュリティ支出 | 2,130億ドル(表題に記載) | Gartner プレスリリース | https://www.gartner.com/en/newsroom/press-releases/2025-07-29-gartner-forecasts-worldwide-end-user-spending-on-information-security-to-total-213-billion-us-dollars-in-2025 | 2025-07-29 | 3(調査会社一次発表) | 2025年7月時点の予測値 |
| 2026年(2025年7月版) | 約2,400億ドル。内訳はセキュリティソフトウェア約1,210億ドル、セキュリティサービス約930億ドル、ネットワークセキュリティ約260億ドル | 同上(検索要約が引用) | 同上 | 2025-07-29 | 3 | 内訳の端数は検索要約の「約」。原本で確認が必要 |
| 2026年(2025年第3四半期更新) | 2,442億ドル、為替一定ベースの成長率11.6% | Gartner 文書名 "Forecast: Information Security, Worldwide, 2023-2029, 3Q25 Update"(文書そのものは本文未取得)/ 数値は二次ブログ | https://www.gartner.com/en/documents/6998666 / https://softwarestrategiesblog.com/2026/03/24/information-security-spending-2026/ | 2026-03-24(ブログ) | 4(数値は二次) | Gartner 原本の数値は未確認 |
| 2026年(2026年第2四半期更新) | 2,489億ドル、為替一定ベースで+12.7%。2030年に3,726億ドル | Software Strategies Blog | https://softwarestrategiesblog.com/2026/07/06/gartner-2q26-information-security-forecast-securing-ai-2030/ | 2026-07-06 | 4 **単独出典** | Gartner 自身のサイトでは確認できなかったと検索要約が明記 |
| 2027年 | 前年比+12.5%(総額は欠損) | 同上(検索要約) | 同上 | 2026-07-06 | 4 **単独出典・未確認** | 2027年の総額は公表値を見つけられなかった |
| AIのセキュリティ(securing AI)支出 | 2026年28.35億ドル → 2027年47.83億ドル(+68.7%) | Software Strategies Blog(Gartner予測の引用) | https://softwarestrategiesblog.com/2026/07/06/gartner-2q26-information-security-forecast-securing-ai-2030/ | 2026-07-06 | 4 **単独出典** | 5節(a)の別予測と食い違う。同節参照 |

- **なぜ予測が上方修正されたか(2層)**: 2026年の値は、2025年7月版2,400億ドル → 2025年第3四半期更新2,442億ドル → 2026年第2四半期更新2,489億ドルと、版を重ねるごとに上がっている(後の2版は二次出典)。検索要約は修正の理由まで書いておらず、理由は欠損。
- **欠損**: クラウドセキュリティ、アイデンティティ、SecOps/SIEM、データセキュリティの各セグメント額と成長率、IT予算全体に占める比率、IDC の予測(Worldwide Security Spending Guide)。いずれも今回の検索では出てこなかった。
- **別の観察**: 2026年の「AI搭載のセキュリティ」市場は、Gartner 予測として2026年490億ドル → 2030年2,040億ドルと報じられている(二次ブログ、単独出典)。https://softwarestrategiesblog.com/2026/08/17/gartner-ai-amplified-security-forecast-204b-2030/ (2026-08-17、Tier 4)。この数字は「既存のセキュリティ支出がAI搭載製品に移る」ものと説明されており、1節の総額に含まれる分を別の切り口で切ったものと読める(ブログの説明。重複計上に注意)。

## 2. 利益プールは、Palo Alto の開示以外は欠損である

**用語**: non-GAAP=株式報酬や買収関連費用などを除いた会社定義の利益。粗利率=売上総利益÷売上。営業利益率=営業利益÷売上。

| 企業 | 期間 | 粗利率 | 営業利益率 | 出典URL | 出典日 | Tier | 備考 |
|---|---|---|---|---|---|---|---|
| Palo Alto Networks | 2026年度第4四半期(2026年7月31日終了) | non-GAAP 74.8% | non-GAAP 29.6%(営業利益10.11億ドル。前年同期は7.68億ドル) | https://investors.paloaltonetworks.com/static-files/8864c425-7c5d-4471-85c9-cdbf9072cfe5 / https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-reports-fiscal-fourth-quarter-and-fiscal-10 / https://www.sec.gov/Archives/edgar/data/0001327567/000132756726000019/ex991q426earningsrelease.htm | 2026年8月(月日は本文未取得) | 1 | 同じ資料内で営業利益率が29.6%と29.5%の2通りに書かれている(検索要約)。**未確定**。29.5%はガイダンス欄の値とも読めるが、対象年度は要確認 |
| CrowdStrike | 直近12か月(LTM、取得時点は約2026年4月) | 73.5% | 欠損 | https://www.tikr.com/blog/crowdstrike-vs-palo-alto-networks-which-cybersecurity-leader-deserves-a-premium-valuation | 約2026-04(検索要約の「163日前」から逆算) | 4 **単独出典** | 会社IRで要確認 |
| Fortinet・Zscaler・Okta・Cloudflare | - | 欠損 | 欠損 | - | - | - | 検索で出てこなかった |

- **規模の参考値(Tier 4、出典間で食い違い)**: 2026年度(CrowdStrike と Okta は2026年1月期、Zscaler は2026年7月期)の売上として、ある一覧は CrowdStrike 約48.1億ドル、Okta 約29.2億ドル、Zscaler 約33.5億ドルと書き、別の一覧は「セキュリティ売上」として約45億・28億・27億ドルと書く。どちらも会社決算の原本ではなく、出典間の差は定義の違いと読めるが理由は確認できていない。**未確定**。候補出典: https://programs.com/resources/largest-cybersecurity-companies/ 、https://atlantsecurity.com/blog/top-cybersecurity-companies (どちらの数値かは検索要約から特定できない)。
- **欠損**: セグメント別(ファイアウォール、SASE/SSE、EDR/XDR、SIEM、IAM、CDN/WAF)の市場規模と成長率。Dell'Oro のファイアウォール・SASE 市場の数値は検索結果に出てこなかった。
- **用語定義**: SASE=ネットワークとセキュリティをクラウドで一体提供する仕組み。SSE=そのうちセキュリティ部分。EDR=端末の侵入検知・対応。XDR=端末以外にも広げた版。SIEM=ログを集めて脅威を検知する基盤。IAM=ID・アクセス管理。WAF=Web アプリへの攻撃を防ぐ装置。

## 3. 大型買収の完了で、プラットフォーム統合は「実行段階」に入った

| 買収 | 状態 | 金額 | 出典URL | 出典日 | Tier | 備考 |
|---|---|---|---|---|---|---|
| Google による Wiz | **2026年3月に完了と報じられている** | 320億ドル(当初提示額に対し39%の上乗せと報じられている) | https://www.feinternational.com/blog/cybersecurity-ma / https://www.calcalistech.com/ctechnews/article/bjo5eucewl | 2026年 | 3〜4 | Google・Wiz の発表原本は未取得。**Tier 1 での確認が必要** |
| Palo Alto による CyberArk | **完了(会社発表は2026-02-11付)** | 約250億ドル(別の出典は246億ドル)。対価は現金約23億ドルと株式約1.12億株(SEC提出書類) | https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-cyberark-to-secure-the-ai-era / https://www.sec.gov/Archives/edgar/data/1327567/000132756726000005/panw-20260131.htm | 2026-02-11 | 1(完了と対価)/ 3(総額250億ドル) | 総額は出典間で250億ドルと246億ドルに割れる。**未確定**。株数1.12億株は Palo Alto の希薄化に直結するため、統括は10-Q原本で確認すること |
| ServiceNow による Armis | **完了(会社発表は2026年4月)** | 77.5億ドル(Fortune は「約80億ドル」) | https://www.businesswire.com/news/home/20260419639334/en/ServiceNow-completes-Armis-acquisition-closing-the-gap-between-asset-visibility-and-cyber-risk / https://fortune.com/2026/08/19/armis-wiz-8-billion-cybersecurity-acquisition-servicenow-saaspocalypse/ | 2026-04 / 2026-08-19 | 1 / 3 | Fortune は「ServiceNow の株価が SaaSpocalypse の懸念に逆らった買収」として扱う |
| Palo Alto による Chronosphere | 完了の確認なし | 約33億ドルの合意(検索要約) | https://www.feinternational.com/blog/cybersecurity-ma | 2026年 | 4 **単独出典** | 完了したかは**欠損** |
| CrowdStrike による SGNL(アイデンティティ新興企業) | 完了の確認なし | 7.4億ドル、2026年1月 | https://www.feinternational.com/blog/cybersecurity-ma | 2026年 | 4 **単独出典** | 完了したかは**欠損** |
| Palo Alto による Protect AI、Zscaler による Red Canary、Cisco による Splunk、CrowdStrike のその他(Onum、Pangea 等) | **欠損** | **欠損** | - | - | - | 検索結果に出てこなかった |

- **市場全体の件数(集計方法で大きく変わる)**: Momentum Cyber は2026年上半期に219件、公表額91億ドル(発表済みの巨額案件を除く)。Windsor Drake は2026年第1四半期に約470億ドル・108件。SecurityWeek は2026年3月だけで38件。いずれも Tier 3〜4。https://windsordrake.com/cybersecurity-ma-report/ 、https://www.securityweek.com/cybersecurity-ma-roundup-38-deals-announced-in-march-2026/ 、https://windsordrake.com/market-intelligence/reports/cybersecurity-ma-activity-q2-2026
- **関連**: 3件の巨額買収(Wiz、CyberArk、Armis)に関し、イスラエルの従業員に約20億ドルが流れると報じられた。https://www.calcalistech.com/ctechnews/article/bjo5eucewl (Tier 3)。人材流出・再投資の観点は統括が判断する。
- **欠損**: 顧客のベンダー数削減の調査データ(Gartner、Forrester 等の「ベンダー統合」調査)。今回の検索で出てこなかった。

## 4. Microsoft のセキュリティ事業は、売上額の最新開示を取れなかった

| 項目 | 数値 | 出典URL | 出典日 | Tier | 備考 |
|---|---|---|---|---|---|
| Entra(アイデンティティ製品)の月間アクティブユーザー | 10億人 | https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q1 | 2026年度第1四半期(2025年9月期)の決算説明会(2025年10月) | 1 | 検索要約が決算説明から引用 |
| Sentinel(SIEM)の顧客数 | 4万社 | 同上 | 同上 | 1 | 同上 |
| 「セキュリティの全カテゴリでシェアを取った」という会社の発言 | - | 同上 | 同上 | 1 | 定性のみ |
| セキュリティ顧客数 | 約150万社 | https://www.nasdaq.com/articles/microsoft-expands-security-offering-it-next-revenue-pillar | 日付不明 | 3(Zacks配信) | 日付スタンプが不揃い(検索要約) |
| 2026年度(2026年6月期)の全社売上 | 3,318億ドル、+18% | https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast | 2026年7月 | 1 | セキュリティの内訳なし |
| セキュリティ事業の年間売上 | 「200億ドル超」という記述が2系統ある | https://www.govinfosecurity.com/microsoft-security-sales-hit-20b-as-consolidation-increases-a-21015 (2023年1月の報道とされる)/ https://promptedportfolio.substack.com/p/infosec-saas-ranking-growth-ai-and (2026年9月下旬の記事) | 2023-01 / 2026-09 | 3 / 4 | **未確定**。2023年の報道は「2022年に200億ドルを超えた(前年比+33%)」。2026年の記事は「200億ドル超で、2年でほぼ倍」。両者は両立しにくい(2023年に200億ドルなら、2年で倍なら2026年は400億ドル規模になる)ため、2026年の記事は単独出典として扱い、Microsoft の決算発表原本で確認が必要 |
| 端末保護のシェア(2021年) | Microsoft 11.2%、CrowdStrike 12.6% | 同上(2023年の報道) | 2023-01 | 3 | 古い。2026年の値は欠損 |
| Security Copilot の価格 | 従量課金で1 SCU 時間あたり4ドルから。E5/E7 に含まれる枠あり | https://underdefense.com/blog/ai-soc-pricing-guide/ | 2026年 | 4 | ベンダーのブログ。E7 という上位ライセンスの存在は検索要約の記述 |

- **用語**: E5=Microsoft 365 の上位ライセンスで、Defender(端末・クラウド保護)、Entra(ID管理)、Purview(データ保護)、Sentinel 連携などを束ねる。SCU=Security Copilot の計算単位。
- **専業ベンダーへの影響**: 定量分析は見つからなかった。2023年の報道が、Microsoft の CEO の発言として「顧客はリスク・複雑性・コストを減らすため Microsoft のセキュリティ群に統合している」と引用している(Tier 3)。2026年についての調査・報道は**欠損**。
- **欠損**: 2026年度の Defender、Entra、Sentinel の個別の成長率と売上、E5 の価格改定・採用率。

## 5. AIの影響は両方向に出ており、2026年は「ソフトウェア全体の下落の中でセキュリティ株が相対的に持ちこたえ、8月に急騰した」

### 5(a) AIのセキュリティという新市場の規模は、出典によって10倍近く開く

| 予測 | 数値 | 出典URL | 出典日 | Tier | 備考 |
|---|---|---|---|---|---|
| Gartner 予測(2026年第2四半期更新)の securing AI | 2030年に376億ドル、新規支出は219億ドル | https://softwarestrategiesblog.com/2026/07/06/gartner-2q26-information-security-forecast-securing-ai-2030/ | 2026-07-06 | 4 | 二次ブログ |
| Gartner 予測の securing AI | 2030年に164億ドル | https://softwarestrategiesblog.com/2026/08/17/gartner-ai-amplified-security-forecast-204b-2030/ | 2026-08-17 | 4 | 同じブログの別記事。**上と食い違う。未確定** |
| Gartner 予測の securing AI(2026→2027) | 28.35億ドル → 47.83億ドル | 1節の表 | 2026-07-06 | 4 | 単独出典 |
| 「AI搭載のセキュリティ」(既存支出の移行) | 2026年490億ドル → 2030年2,040億ドル | 1節参照 | 2026-08-17 | 4 | 範囲が広い |
| AIサイバーセキュリティ市場(市場調査会社) | Mordor: 2025年309億ドル → 2030年863億ドル(年率22.8%)/ Strategic Market Research: 2024年192億ドル → 2030年645億ドル / Statista: 2030年に約1,340億ドル | https://www.mordorintelligence.com/industry-reports/ai-cybersecurity-solutions-market 、https://www.strategicmarketresearch.com/market-report/ai-in-cybersecurity-market 、https://www.statista.com/statistics/1450963/global-ai-cybersecurity-market-size/ | 2025〜2026年 | 4 | 「AIで防御する製品」と「AIを守る製品」を混ぜた定義。比較不可 |
| 生成AIのセキュリティ / エージェント型AIのセキュリティ | 2026年11.7億ドル → 2030年24.6億ドル(年率20.5%)/ 2025年18.3億ドル → 2030年78.4億ドル | https://www.thebusinessresearchcompany.com/report/generative-artificial-intelligence-in-security-global-market-report ほか | 2026年 | 4 | 市場調査会社の推計 |

- **用語の区別**: 「AIを守る」(securing AI=AIアプリ・エージェント・モデルの保護)と「AIで守る」(AI搭載のセキュリティ)は別物。出典によって混ざっているため、統括は市場規模を比べる前に定義をそろえること。
- **主な製品**: 今回の検索では Palo Alto の Prisma AIRS、CrowdStrike、Zscaler、Cloudflare の製品を確認できなかった(**欠損**)。市場調査会社の主要プレイヤー一覧に CrowdStrike・Palo Alto・SentinelOne・Darktrace・Vectra AI が載る程度。各社の個別分析の担当者が一次資料で補う。
- **関連事実**: CrowdStrike の脅威報告は、攻撃者が90社超で生成AIツールに悪意あるプロンプトを注入し、AI開発基盤も悪用したと記述(Tier 1、ベンダー自身の調査。下記(b))。

### 5(b) 攻撃側のAI活用は、報告された数字で急増している(ただし出所はセキュリティ会社自身)

| 項目 | 数値 | 出典URL | 出典日 | Tier | 備考 |
|---|---|---|---|---|---|
| AIを使う攻撃者による攻撃(2025年) | 前年比+89% | https://www.crowdstrike.com/en-us/press-releases/2026-crowdstrike-global-threat-report/ | 2026-02-24 | 1(CrowdStrike自身の発表) | 「攻撃」「活動」「作戦」と媒体で言い方が割れ、定義に注意 |
| eCrime(金銭目的の犯罪)の平均ブレイクアウト時間(侵入後に横展開するまでの時間) | 29分(2024年は48分とする出典あり)。最速は27秒。速度は+65% | https://www.crowdstrike.com/en-us/press-releases/2026-crowdstrike-global-threat-report/ ほか(https://www.crnasia.com/news/2026/cybersecurity/ai-cuts-cyberattack-breakout-time-to-29-minutes-reveals-crowdstrike-report) | 2026-02-24 | 1 / 3 | 48分→29分は時間で約40%減、速度では約65%増という算術と整合する |
| 公開前に悪用された脆弱性の比率 | 約42% | https://www.intelligentciso.com/2026/02/24/2026-crowdstrike-global-threat-report-ai-accelerates-adversaries-and-reshapes-the-attack-surface/ | 2026-02-24 | 3 | |
| AIが攻撃の道具として使われた例 | ロシア関連の FANCY BEAR が LLM 搭載マルウェア(LAMEHUG)で偵察・文書収集、PUNK SPIDER がAI生成スクリプトで認証情報の窃取と痕跡消去 | 同上 | 2026-02-24 | 1 / 3 | |

- **欠損**: Verizon DBIR 2026(データ侵害調査報告)、Mandiant M-Trends 2026、IBM のデータ侵害コスト調査。いずれも今回の検索で出てこなかった。
- **留意**: 上の数字はすべて CrowdStrike 自身の調査であり、同社の製品の需要を説明する立場にある。独立した統計(Tier 2)は欠損。

### 5(c) 「AIがSaaSを代替する」懸念で2026年第1四半期にソフトウェア株が急落し、セキュリティ株はそれに連れて売られたあと、8月に反発した

**用語**: SaaS=ネット経由で提供する業務ソフト。IGV=iShares のソフトウェア ETF。SaaSpocalypse=「SaaS の終末」を意味する俗称で、AIエージェントが業務ソフトを置き換えるという懸念による株価下落を指す。

| 時点 | 事実 | 出典URL | 出典日 | Tier |
|---|---|---|---|---|
| 2026年2月 | 下落の起点は、Anthropic が Claude のエージェント機能を発表し、AIエージェントが業務ソフトのワークフローを置き換えるとの懸念が強まったこと | https://finance.yahoo.com/markets/stocks/articles/3-software-etfs-buy-saaspocalypse-123300355.html | 2026-09下旬 | 3 |
| 2026年第1四半期 | IGV は-24%。2008年以来で最悪の四半期 | 同上 | 2026-09下旬 | 3 |
| 2026年4月安値 → 9月 | IGV は4月の安値から40%超上昇 | 同上 | 2026-09下旬 | 3 |
| 2026-05-08 | IGV は年初来-14% | https://www.cnbc.com/2026/05/08/some-software-stocks-are-breaking-out-of-the-ai-driven-saaspocalypse-jpmorgan-likes-these-names.html | 2026-05-08 | 3 |
| 時期不明(Anthropic のコード検査ツールの登場時) | 下落率: CrowdStrike -19%、Zscaler -17.2%、Okta -16.8%、Palo Alto -10.4%(期間は出典に明記なし) | https://stocktwits.com/news-articles/markets/equity/crwd-panw-zs-other-cybersecurity-stocks-fall-hard-on-new-ai-scare-but-wall-street-isnt-panicking-yet/cZRtaWhR4U1 | 2026年(日付未確認) | 4 **単独出典** |
| 時期不明(1週間の下落) | Palo Alto と Zscaler が各10%超下落。SailPoint -10.8%、CrowdStrike と Cloudflare は-9.6%。Palo Alto は四半期利益の未達と2026年の利益見通しの引き下げも重なった | 検索要約が引用した記事(URL未特定) | 2026年(日付未確認) | 3〜4 **単独出典** |
| 2026年5月下旬 | Zscaler の売上見通しが弱く、Palo Alto -4.2%、CrowdStrike -3.3%(寄り付き前) | https://www.cmelitegroup.com/trends-and-insights/palo-alto-and-crowdstrike-drop-on-zscaler-miss/ | 2026年5月下旬 | 3 |
| 2026年5月 | Palo Alto と CrowdStrike は12月以来の高値で引けた | CNBC(同上、5月8日付) | 2026-05-08 | 3 |
| 2026年9月 | CrowdStrike が最高値。Zscaler と SentinelOne が2桁上昇 | 検索要約が引用した記事(URL未特定。上のYahoo Finance記事とは別) | 2026-09 | 3 **単独出典** |

- **対比の結論(出典が示す範囲)**: セキュリティ株も2026年の初めにAI懸念で売られたが、5月以降は Palo Alto と CrowdStrike が高値圏に戻り、ソフトウェア全体(IGV)より回復が強いと報じられている。ただし、2026年通期でセキュリティ各社を IGV と直接比べた出典は見つからなかった(検索要約が明記)。
- **Okta**: ある記事は「Okta はグループの遅れた銘柄」と書く(プラットフォーム大手がアイデンティティも束ねるため、専業は優位を示し続ける必要があるという論調。https://marketwise.com/investing/best-cybersecurity-stocks-2026/ 、Tier 4)。ただし2026年8月末の決算後に Okta は急騰した(6節)。
- **意見記事**: Motley Fool(2026-04-14)は「SaaSpocalypse はサイバーセキュリティに近年最良の買い場を作った」と主張(https://www.fool.com/investing/2026/04/14/saaspocalypse-create-buy-opportunity-cybersecurity/ 、Tier 3〜4の意見)。事実ではなく主張として扱う。

### 5(d) AIによるSOC自動化は課金モデルを「席数」から「量・成果」へ動かしているが、実際の採用はまだ初期である

**用語**: SOC=セキュリティ運用センター(監視・対応を行う部門)。シート課金=利用者数に応じた課金。

- 課金の実態(いずれもベンダーのブログ、Tier 4): AI SOC は「アラート量、データ取り込み量、アナリスト席数のいずれか、またはその組み合わせ」で課金される。Dropzone AI は年3.6万ドルで4,000件の調査(1件約9ドル)で、席数課金ではなく調査件数課金。CrowdStrike の Charlotte AI は Falcon に上乗せで端末あたり年8〜14ドルと推計される。Microsoft Security Copilot は従量課金。https://underdefense.com/blog/ai-soc-pricing-guide/ 、https://www.blinkops.com/blog/top-10-ai-soc-vendors-in-2026-a-practitioners-comparison
- 採用状況: ベンダーのマーケティング記事が Gartner を引用し、「AI SOC エージェントは導入が1〜5%の黎明期で、3年以内にSOC業務の60%を担う」と書く。ベンダー記事経由の**単独出典**であり、Gartner 原本は未確認。どの検索結果ページの記述かは要約から特定できなかった(候補: https://underdefense.com/blog/managed-siem-trends-2026/ 、Tier 4)。
- **欠損**: Okta など「人(ユーザー)に課金する」会社への影響の論調、AIエージェントのID(非人間ID)への課金。今回の検索では何も出てこなかった。

## 6. 株価は2026年に大きく戻しており、8月のブラックハット後と8月下旬の決算で最高値圏に入った。バリュエーションの水準比較は欠損

**用語**: ETF=指数に連動する上場投資信託。CIBR=First Trust のサイバーセキュリティ ETF(時価総額加重)。HACK=Amplify の同種 ETF。BUG=Global X の同種 ETF(約25銘柄の純粋なセキュリティ企業中心)。YTD=年初来。PER=株価÷1株利益。ブラックハット=ラスベガスで毎年8月に開く、世界最大級のセキュリティ会議。

| 項目 | 数値 | 出典URL | 出典日 | Tier | 備考 |
|---|---|---|---|---|---|
| CIBR の年初来の総合リターン | +49.55%(2026-10-07時点)。純資産173.2億ドル。直近実績PER 36.45倍 | https://finance.yahoo.com/quote/CIBR/performance/ | 2026-10-07 | 3 | 最も新しい数値。HACK と BUG は同ページにない |
| 6月時点(2026年6月初旬) | CIBR +32%、HACK +28%、BUG +27%。BUG の1年リターンは+10%で CIBR・HACK を大きく下回る | https://247wallst.com/investing/2026/06/04/after-reviewing-every-cybersecurity-etf-these-3-capture-the-full-stack-most-investors-miss/ | 2026-06-04 | 3 | |
| 7月10日時点 | HACK +35.44%、CIBR +28.62%。HACK が先行した理由として、記事は防衛銘柄(General Dynamics 5.11%、Northrop Grumman 4.56%)の組み入れを挙げる | https://247wallst.com/investing/etf/2026/07/10/cibr-vs-hack-which-cybersecurity-etf-is-the-smarter-way-to-play-digital-defense/ | 2026-07-10 | 3 | |
| 日付不明のデータ | CIBR +46.92%、HACK +53.14%(年初来) | https://portfolioslab.com/tools/stock-comparison/CIBR/HACK | 日付不明 | 4 | 参考。日付がなく上と整合するか不明 |
| ブラックハット後(2026-08-10の週明け) | CrowdStrike と Palo Alto が5%超上昇して最高値。BTIG が「AIエージェントが脅威の状況を根本的に変えた」として両社の目標株価を引き上げ | https://qz.com/crowdstrike-palo-alto-networks-stock-black-hat-ai-security-081026 | 2026-08-10 | 3 | URL の末尾が日付を示唆(0810、26) |
| 2026-08-27(決算後の反応) | CrowdStrike は過去最高の上昇日(CNBC は+20%、24/7 Wall St. は取引中に+13%)。Okta は約+29%(CNBC)/+22%(24/7 Wall St.)。Palo Alto、SailPoint、Zscaler、Rubrik も10%以上上昇 | https://www.cnbc.com/2026/08/27/okta-skyrockets-20percent-and-crowdstrike-surges-15percent-leading-cyber-rally.html / https://247wallst.com/investing/2026/08/27/cybersecurity-stocks-rally-on-twin-earnings-beats-okta-spikes-22-crowdstrike-jumps-13/ | 2026-08-27 | 3 | 数値は測定時刻の違いで割れる。CNBC の見出しは「Okta 約20%、CrowdStrike 約15%」と本文の「Okta 29%、CrowdStrike 20%」でも揺れている。**未確定**(終値ベースは会社IR/株価データで確認) |
| CrowdStrike の倍率 | 予想PER約208倍・売上高倍率約49倍(Benzinga)/ 予想PER192倍(別記事、コンセンサス目標株価234.35ドルより高い) | https://www.benzinga.com/trading-ideas/long-ideas/26/09/62081742/ai-cybersecurity-stocks-rally | 2026-09 | 3 | 2つの値が食い違う。**未確定** |

- **株価水準の食い違い(警告)**: CrowdStrike の株価は、ある記事が2026-08-27に213.70ドル、他は213〜264ドル台と書き、別の記事(Yahoo系)は701.09ドルと書く。株式分割の有無を含め、**会社IRで確認するまで株価水準を使わない**こと。倍率(PER、売上高倍率)の比較にも影響する。
- **欠損**: セクターの売上高倍率・PER と過去平均の比較(今回の検索では、ソフトウェア全体との比較を含めて出典が出てこなかった)。BUG の最新の年初来、HACK の10月時点の年初来。
- **構造の注記**: 3つの ETF は構成が違う(CIBR は時価総額加重、HACK は調整時価総額加重で防衛銘柄を含む、BUG は修正等ウェイトの約25銘柄)。年初来の差は、純粋なセキュリティ企業の動きだけでは説明できない。

## 7. 規制・制度は、米国で緩和・延長の揺れがあり、欧州の動きは今回の検索で取れなかった

| 項目 | 事実 | 出典URL | 出典日 | Tier | 備考 |
|---|---|---|---|---|---|
| CISA 2015(サイバーセキュリティ情報共有法。注: 政府機関 CISA とは別物) | 2026年2月の歳出パッケージで2026-09-30まで延長 | https://www.hunton.com/privacy-and-cybersecurity-law-blog/congress-extends-cybersecurity-information-sharing-act-of-2015-through-september-2026 | 2026-02 | 3 | 基準日(2026-10-11)は期限後。**その後の再承認は欠損** |
| CIRCIA(重要インフラの事案報告法)の規則 | CISA が規則策定を再開し、業界の意見を募集。実施見込みが2026年5月に延びたとの記述 | https://www.bytebacklaw.com/2026/02/navigating-cyber-disclosures-in-2026-a-limited-renewal-of-cisa-2015-and-take-two-on-finalizing-circias-reporting-regulations/ | 2026-02 | 3 | 5月に実施されたかは**欠損** |
| SEC のサイバー開示規則 | 2023-07-26採択。重大インシデントは Form 8-K の Item 1.05 で4営業日以内に開示。SolarWinds/CISO 訴訟は2025-11-20に再提訴不可で棄却 | https://wiki.el-doradocapital.com/16-regulation | 不明(2025-11以降) | 4 **単独出典** | SEC 原本で要確認。2026年の改正・緩和の動きは**欠損** |
| NIS2(EUの重要事業者向けサイバー指令)、DORA(EUの金融機関向けデジタル運用レジリエンス規則) | 義務の一般的な説明のみ(登録、重大事案の報告、研修)。国内法化の進捗と執行事例は**欠損** | https://thecompliancedigest.com/eu-cybersecurity-regulatory-update-for-2026-and-beyond/ ほか | 2026年 | 4 | |
| CISA(米サイバーセキュリティ・インフラセキュリティ庁)の予算・人員、連邦ゼロトラスト指令 | **欠損** | - | - | - | 今回の検索では出てこなかった |

## 8. 大規模事件は多発したが、需要・競争への影響を示す出典は取れなかった

| 事件 | 概要 | 出典URL | 出典日 | Tier | 備考 |
|---|---|---|---|---|---|
| Jaguar Land Rover(2025年8月下旬) | 攻撃でシステムを停止し、週5,000台の生産を約5週間止めた。被害は約19億ポンド(Inc は「25億ドル」と見出し)。2026年度に3.5億ドルの損失を計上したとの報道。ロシア系という報道は未確定 | https://en.wikipedia.org/wiki/Jaguar_Land_Rover_cyberattack / https://www.inc.com/kevin-haynes/inside-the-2-5-billion-cyberattack-that-shut-down-jaguar-land-rover/91366720 / https://www.ien.com/operations/article/22950925/as-jaguar-land-rover-struggles-to-restart-production-stellantis-faces-breach-linked-to-salesforce | 2025〜2026年 | 3〜4 | 被害額は出典間で割れる。**未確定** |
| Salesforce 関連のデータ窃取 | ShinyHunters による社会工学・Salesforce 連携経由の窃取。Stellantis も関連。集計サイトは McGraw Hill で1,350万件のメール、Canvas/Instructure の約2.75億件(約9,000校)を挙げる | https://socradar.io/resources/radar/major-cyber-attacks/ 、https://www.westcomnetworks.co.uk/news/general/the-worst-cyberattacks-of-2026-so-far/ | 2026年 | 4 | 集計サイトの数字。**要裏取り** |
| Salt Typhoon(中国系) | 広域のスパイ活動から、北米の重要インフラへの長期潜伏へ重心を移したとの記述。過去に Cisco IOS XE の欠陥で世界の通信網に侵入 | https://www.westcomnetworks.co.uk/news/general/the-worst-cyberattacks-of-2026-so-far/ | 2026年 | 4 | |
| Cloudflare の障害(2月20日) | 自動化された内部保守作業のバグで、顧客のIPアドレス広告を意図せず取り下げた | https://www.networkworld.com/article/4113326/2026-network-outage-report-and-internet-health-check.html | 2026年版の障害報告 | 3 | 年は要約に明記なし(報告書名から2026年と推定。未確認) |
| Cloudflare の障害(9月22日) | ロサンゼルス拠点中心の約1時間の障害。原因の記述なし | 同上 | 同上 | 3 | |
| Cloudflare が防いだ最大のDDoS攻撃 | 22.2 Tbps(40秒)と、31.4 Tbps の2通りが出る | https://gcn.com/22-2-terabit-flood-junk-data/22315 / https://shattered.io/cloudflare-2026-threat-report/ | 不明 / 2026年 | 3 / 4 | **食い違い。未確定**(Cloudflare の公式脅威報告に当たること) |
| Salesforce の障害(9月16日) | 内部ログインサービスでリクエストが滞留 | 上記 networkworld | 同上 | 3 | |

- **用語**: DDoS=大量の通信を送りつけてサービスを止める攻撃。Tbps=毎秒1兆ビット。ShinyHunters=データ窃取と恐喝を行う犯罪集団。
- **欠損**: これらの事件が需要を押し上げた、または競争を変えたことを示す出典。2024年7月の CrowdStrike 障害の後日談(補償、解約、競争への影響)。2025年11〜12月の Cloudflare の大規模障害(今回の検索では出てこなかった)。

## 9. 追加検索ができる場合の優先順位(欠損の穴埋め用)

1. Gartner 2026〜2027年の情報セキュリティ支出のセグメント別内訳(`allowed_domains: gartner.com`)。クラウド・アイデンティティ・SecOps・データの各額。
2. IDC のセキュリティ支出予測と、Dell'Oro のファイアウォール・SASE 市場の数値。
3. Microsoft 2026年度第4四半期決算説明のセキュリティ発言(`allowed_domains: microsoft.com`)。
4. Chronosphere、Protect AI、Red Canary、Splunk、CrowdStrike の買収の完了状況(会社発表)。
5. Zscaler・Fortinet・Okta・Cloudflare・CrowdStrike の最新四半期の粗利率・営業利益率(各社IR)。
6. セクターの売上高倍率とPERの過去平均との比較(Morningstar、FactSet、ETF運用会社)。
7. NIS2・DORA の執行状況、CISA の2027年度予算、連邦ゼロトラスト、CISA 2015 の再承認(2026-09-30以降)。
8. 顧客のベンダー統合調査(Gartner、Forrester)と、Okta・非人間ID の課金の論調。
9. Verizon DBIR 2026、IBM のデータ侵害コスト調査。

## 10. 統括向けの要点(事実のみ。評価は含まない)

- 世界のセキュリティ支出は、Gartner の予測で2025年2,130億ドル → 2026年約2,400〜2,490億ドル(版により上方修正)。2027年は+12.5%との報道があるが、単独出典。
- 大型統合は完了した: Palo Alto–CyberArk(2026-02-11発表、約250億ドル)、Google–Wiz(2026年3月、320億ドルと報道)、ServiceNow–Armis(2026年4月、77.5億ドル)。Chronosphere・SGNL の完了は未確認。
- 2026年第1四半期に IGV は-24%(2008年以来の最悪)。セキュリティ株も売られたが、5月以降に Palo Alto と CrowdStrike が高値を回復し、8月のブラックハット後と8月27日の決算後に急伸した。CIBR の年初来は+49.55%(2026-10-07、Yahoo Finance)。
- 攻撃側のAI活用は、CrowdStrike 自身の報告でAIを使う攻撃者の活動が+89%、平均ブレイクアウト時間が29分。
- 最も重い欠損: セクター倍率の過去平均比較、Microsoft の最新のセキュリティ売上、ベンダー統合の調査、EU規制と CISA 予算。CrowdStrike の株価水準が出典間で大きく食い違うため、分割の有無を会社IRで確認すること。
