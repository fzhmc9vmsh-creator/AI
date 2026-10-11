# Okta(OKTA)定性調査 一次整理 — 未完了版(検索予算の上限で中断)

- 対象: Okta, Inc.(NASDAQ-OKTA、決算期末 1月31日。FY2027 = 2026年2月〜2027年1月)
- 評価基準日: 2026-10-11。本書の取得日はすべて 2026-10-11。
- 担当範囲: 定性情報の収集と一次整理。評価・投資判断は含まない。

## 0. 本書の状態: 依頼項目 A〜G のうち、実質的に埋まったのは A の一部(直近2四半期の数値)だけである

**中断の理由。** WebSearch を 3 回実行した時点で、「このターンの検索予算(1ターン200回、全エージェント共有)を使い切った」というエラーが返り、以後の検索が実行されなかった。
回避策(curl、第三者の閲覧代行サービスなど)は取らなかった。
このため、**依頼の A 後半・B・C・D・E の一部・F・G は未調査(欠損)**である。

**本書の記載ルール。**
- 数値・発言は、今回の検索結果に現れたものだけを記録した。出典URLと Tier(情報源の信頼段階。会社IR > 公的統計 > 主要報道・アナリスト > ブログ・SNS)を付けた。
- モデルの記憶にある事項は、出典URLを付けられないため**一切入れていない**(推測で埋めない)。
- 検索結果は要約文であり、原ページ本文を直接読んだわけではない。会社IRのプレスリリースURLが検索結果に出ているが、**要約文経由の数値**である。分析の根拠に使う前に、原ページでの再確認が望ましい。

**再開の方法。** §9 に、残りの項目を埋めるための検索クエリの一覧を優先順で置いた。
検索予算が戻れば、そのまま実行できる。ユーザーは追送メッセージで続行を指示するか、`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` の引き上げが必要である。

---

## A. 経営陣シナリオの一次情報

### A-1. 直近4回の決算説明会(FY2026 Q3 〜 FY2027 Q2)

**状態: FY2027 Q2 と Q1 の「数値」のみ取得。発言の逐語引用は欠損。FY2026 Q3・Q4 は未検索。Investor Day / Oktane は未検索。**

#### FY2027 Q2(2026年7月31日終了。説明会は 2026-08-26)

用語: RPO(残存履行義務)= 契約済みで未計上の売上の総額。cRPO = そのうち12か月以内に売上計上される見込みの額。GAAP = 米国会計基準。non-GAAP = 会社が株式報酬などを除いて示す調整後の基準。FCF(フリーキャッシュフロー)= 営業キャッシュフロー − 設備投資。

| 項目 | 値 | 出典(Tier) |
|---|---|---|
| 売上高 | 8億500万ドル、前年同期比 +11% | 会社IR(Tier 1)・検索要約経由 |
| サブスクリプション売上 | 7億9300万ドル、+12% | 同上 |
| RPO | 48億5800万ドル、+17% | 同上 |
| cRPO | 25億8500万ドル、+14% | 同上 |
| GAAP営業利益 | 1億700万ドル(売上比 13%)。前年同期 4100万ドル | 同上 |
| non-GAAP営業利益 | 2億2600万ドル(売上比 28%) | 同上 |
| FCF | 2億2700万ドル(売上比 28%) | 同上 |
| 2026年満期の転換社債 | 残元本 3億5000万ドルを現金で償還 | 同上 |
| 次四半期(Q3)売上ガイダンス | 8億1300万〜8億1700万ドル | 同上 |
| FY2027 通期売上ガイダンス | 32億1600万〜32億2600万ドル(+10〜11%) | 同上 |
| non-GAAP 希薄化後EPS | 1.05ドル | 単独出典(Tier 3、決算説明会の要約記事)。要再確認 |
| 売上のコンセンサス(事前予想) | 7億9000万〜7億9500万ドル | Futurum Group の分析(Tier 3)。会社IRではない |
| FY2027 non-GAAP営業利益率ガイダンス | 26% | 単独出典(Tier 3、要約記事)。要再確認 |

出典URL(取得日 2026-10-11):
- 会社IR プレスリリース: https://www.okta.com/newsroom/press-releases/okta-announces-second-quarter-2027-financial-results/
- Business Wire 転載: https://www.01net.it/okta-announces-second-quarter-fiscal-year-2027-financial-results/
- Futurum Group 分析: https://futurumgroup.com/insights/okta-q2-fy-2027-earnings-beat-and-raise-on-core-identity-strength/
- トランスクリプト掲載ページ(第三者。内容は未読): https://bullfincher.io/companies/okta/earnings-call/fy2027-q2 ・ https://www.sahmcapital.com/news/content/okta-reports-q2-2027-results-full-earnings-call-transcript-2026-08-27

**経営陣の発言(検索要約経由。逐語ではなく要約の訳である点に注意)。**

| 発言者 | 内容(和訳) | 重要な理由の注記 | 出典(Tier) |
|---|---|---|---|
| Todd McKinnon(CEO、共同創業者) | 成長は、AIエージェントにもアイデンティティ(本人確認・権限管理)の統制が必要になることと結びついている | 経営陣が、AIエージェントを「需要の追加要因」として語っていることを示す。売上への寄与が数値で示されたかは未確認 | 会社IR要約(Tier 1) |
| Todd McKinnon | ACV(年間契約価値)の成長が、Workforce Identity(従業員向け)と Customer Identity(顧客向け、Auth0)の両方で加速した。Q2 は第4四半期を除いて過去最高の契約獲得(bookings)四半期だった | 売上成長率が11%でも、先行指標(新規契約)は強いと経営陣が主張している。「加速した」の基準期間は未確認 | 説明会の要約(Tier 3、出典: 上記トランスクリプト掲載ページ周辺の要約) |
| Todd McKinnon | AIセキュリティは初期段階の機会であり、AI関連の事業はまだ財務に実質的な影響を与えていない | 条件9(AIの停めない運用)を判断する材料。AI由来の売上がまだ小さいことを会社自身が認めている | 説明会の要約(Tier 3)。要原文確認 |
| Brett Tighe(CFO) | 新製品群が強く貢献し、Okta Identity Governance が牽引した(原文: "strong contributions from our portfolio of new products, led by Okta Identity Governance") | 新製品の寄与比率という異常値候補(§E)の入口。寄与の金額・比率は未取得 | 会社IR要約(Tier 1・検索要約経由) |

#### FY2027 Q1(2026年4月30日終了。決算発表 2026-05-28)

| 項目 | 値 | 出典(Tier) |
|---|---|---|
| RPO | 前年同期比 +16%(金額は検索結果に出ず) | 会社IR / Business Wire(Tier 1・検索要約経由) |
| cRPO | +12% | 同上 |
| FCF | 2億7100万ドル(売上比 35%)。前年同期 2億3800万ドル(35%) | 同上 |
| FY2027 FCF ガイダンス(Q1時点) | 8億5500万〜8億8500万ドル(売上比 27〜28%)。自社株買いと2026年満期債の現金償還により、受取利息が減る影響が約1ポイント含まれる | 同上 |
| Q2 売上ガイダンス | 7億9000万〜7億9400万ドル(+約9%) | 同上 |
| non-GAAP 税率 | 長期見通しを 26% から 21% に引き下げ(米国の税制改正法 "One Big Beautiful Bill Act" による。将来に向けて適用) | 同上 |

出典URL(取得日 2026-10-11):
- 会社IR: https://www.okta.com/newsroom/press-releases/okta-announces-first-quarter-2027-financial-results/
- Business Wire: https://www.businesswire.com/news/home/20260528809289/en/
- Q1 説明会の要約記事(Seeking Alpha、Tier 3。見出しは「Q2 FY2027 の売上成長9%、non-GAAP営業利益率26%を見込む」): https://seekingalpha.com/news/4598492-okta-expects-q2-fy2027-9-percent-revenue-growth-with-26-percent-non-gaap-operating-margin-as

**検索要約に混入した誤りの疑い(使用禁止)。** Q1 の検索要約には「Q2 の non-GAAP営業利益 8億600万〜8億2600万ドル」とあるが、同じ四半期の売上ガイダンス(7億9000万〜7億9400万ドル)より大きく、明らかに不整合である。数値は採用せず、「未確定」とする。会社IR原ページで再確認が必要。

**この節から言える計算(出典の数値同士の差)。**
- Q2 の売上実績 8億500万ドルは、Q1 時点のガイダンス上限 7億9400万ドルを 1100万ドル(約1.4%)上回った。下限との差は 1500万ドル(約1.9%)。
- cRPO の成長率は、Q1 の +12% から Q2 の +14% へ 2 ポイント上がった。売上成長率(+11%)より cRPO の成長率が高い状態になった。

#### FY2026 Q3・Q4 の説明会、直近の Investor Day / Oktane: **欠損(未検索)**

### A-2. 数値目標(中期の売上成長率・FCFマージン・営業利益率)

**状態: 通期ガイダンスのみ。中期目標は欠損。**
- FY2027 通期(会社ガイダンス): 売上 32億1600万〜32億2600万ドル(+10〜11%)。FCF 8億5500万〜8億8500万ドル(売上比 27〜28%、Q1 時点)。non-GAAP営業利益率 26%(単独出典)。
- 中期目標(FY2028 以降の成長率・FCFマージン・営業利益率の数値と期限): **欠損**。Investor Day の資料を未取得。

### A-3. ピース一覧(新製品、買収、営業組織、価格、提携、資本政策)

**状態: 資本政策の一部(転換社債の償還、自社株買いの存在)のみ。ほかは欠損。**

| ピース | 目的(会社の説明) | 発表日 | 規模・進捗の数値 | 出典 |
|---|---|---|---|---|
| 2026年満期の転換社債の現金償還 | 未取得(Q1 説明で、利息収入の減少として FCF ガイダンスに織り込みと記載) | 2026-08-26 の発表で「残元本の償還完了」 | 残元本 3億5000万ドルを現金で支払い | 会社IR要約(Tier 1) |
| 自社株買い | 未取得 | 未確認 | 金額・残枠・実施額は欠損。FCF ガイダンスに「自社株買いによる受取利息の減少」が含まれる(Q1) | 会社IR要約(Tier 1) |
| Okta Identity Governance(IGA。誰がどのアプリにアクセスできるかの棚卸し・承認を自動化する製品) | 未取得 | 未確認 | CFO は新製品群の寄与で「最も牽引」と言及(Q2)。寄与の金額は欠損 | 会社IR要約(Tier 1) |

依頼文に挙がっているが、**今回の検索で確認できていない**項目: Spera Security・Axiom Security の買収、Privileged Access、Identity Threat Protection、Auth for GenAI、Cross App Access、営業組織の専門化、公共部門、価格改定、提携。いずれも「欠損」。

### A-4. 過去3年のガイダンス達成状況、2022〜2023年のセキュリティ侵害と Secure Identity Commitment

**欠損(未検索)。** 上記の Q2 の対ガイダンス実績(売上 +1.4〜1.9% 超過)が1件あるのみ。

### A-5. 経営陣の経歴・在任・報酬KPI・交代

**欠損(未検索)。** 本書で確認できたのは、Todd McKinnon が CEO 兼共同創業者、Brett Tighe が CFO であること(説明会要約の記載)のみ。

---

## B. 市場の仮説の出典

### B-1. 直近2回の決算説明会でアナリストが繰り返した質問
**欠損(未検索)。** Q2 説明会のトランスクリプト掲載ページ(§A-1)に質疑応答があるはずだが、本文は未読。

### B-2. 強気派・弱気派の主要論点(各3件以上)
**欠損(未検索)。** 検索結果に Futurum Group の記事見出し「Okta Q2 FY 2027 Earnings Beat and Raise on Core Identity Strength」があり、同社の見方が「好決算・上方修正」であることだけは分かる(Tier 3、アナリスト名・目標株価は欠損)。

### B-3. 空売りレポート・著名な弱気論者
**欠損(未検索)。**

### B-4. 報道のナラティブ(AIによる代替懸念 / AIエージェント需要の増加)
**部分: 会社側の語り**のみ。経営陣は AIエージェントをアイデンティティ需要の追加要因として語る(§A-1)。報道・アナリスト側の両論は欠損。

### B-5. 株価の推移
**欠損(未検索)。** 2026-10-09 終値も未取得。

---

## C. 一次情報(スカットルバット) — 0 件(要件: 最低3件)

欠損(未検索)。取得すべき対象は §9 に列挙した。

## D. 競争と業界の構造

欠損(未検索)。

## E. 異常値の候補(最低3つ)— 今回取得できた数字だけから 5 つを立てた

答えは出さず、問いだけを置く。

| # | 異常値の候補 | 数字(出典は §A-1) | 問い |
|---|---|---|---|
| E1 | 売上成長率が10%台前半なのに、FCFマージンが27〜35%と高く、同時に自社株買いと転換社債の現金償還(3億5000万ドル)を行っている | 売上 +11%、FCF 売上比 28%(Q2)・35%(Q1)、FY2027 FCF ガイダンス 27〜28% | なぜ成長が鈍くても FCF が厚いのか(前受け金・SBC・利息収入のどれが寄与しているのか)。それは経営陣が語る成長シナリオと矛盾しないのか |
| E2 | cRPO の成長率が加速し、売上成長率を上回った | cRPO +12%(Q1)→ +14%(Q2)。RPO +17%。売上 +11% | なぜ先行指標が売上より速く伸びているのか(契約期間の長期化、新製品の上乗せ、AIエージェント関連のどれか)。それは将来の売上成長の加速を意味するのか |
| E3 | GAAP営業利益率と non-GAAP営業利益率の差が大きい | GAAP 13% に対し non-GAAP 28%(差 15 ポイント) | なぜ差が 15 ポイントもあるのか。株式報酬(SBC)と買収無形資産の償却のうち、どちらが主因で、近年縮んでいるのか |
| E4 | non-GAAP 税率の変更だけで、non-GAAP EPS が事業と無関係に上がる | 長期見通しを 26% から 21% へ(Q1発表) | なぜ会社は non-GAAP 税率を変えたのか。EPS の成長のうち、税率変更で説明できる部分は何割か |
| E5 | 自社株買いと債務償還による受取利息の減少が、FCF に約1ポイントの下押しとなる | FCF ガイダンスに約1ポイントの影響(Q1) | なぜ自社株買いを優先したのか。現金を持つ価値(利息収入)と買い戻す価値を、会社はどう比べたのか |

PER の低さ(依頼文の例示)は、株価が未取得のため候補にできていない。

## F. 条件9(AIの停めない運用)に関わる事実

**部分的。**
- 経営陣の発言(要約、Tier 1・3): 「AIエージェントにもアイデンティティの統制が必要」という需要論と、「AI関連の事業はまだ財務に実質的な影響を与えていない」という現状認識(§A-1)。
- AIエージェントの認証・認可製品の内容、顧客数、ARR(年間経常収益)、パイプライン: **欠損**。

## G. リスク事象

欠損(未検索)。セキュリティ侵害の再発、訴訟、規制、会計上の論点、経営陣の株式売却のいずれも未調査。

---

## 8. 出典台帳(今回の検索で実際に結果に現れたURL)

| Tier | 出典 | 日付 | 備考 |
|---|---|---|---|
| 1(会社IR) | https://www.okta.com/newsroom/press-releases/okta-announces-second-quarter-2027-financial-results/ | 2026-08-26(説明会日) | 検索要約経由。原ページ未読 |
| 1 | https://www.okta.com/newsroom/press-releases/okta-announces-first-quarter-2027-financial-results/ | 2026-05-28 | 同上 |
| 1(転載) | https://www.businesswire.com/news/home/20260528809289/en/ | 2026-05-28 | 同上 |
| 1(転載) | https://www.01net.it/okta-announces-second-quarter-fiscal-year-2027-financial-results/ | 2026-08 | 同上 |
| 3(アナリスト) | https://futurumgroup.com/insights/okta-q2-fy-2027-earnings-beat-and-raise-on-core-identity-strength/ | 2026-08 | コンセンサス範囲の出典 |
| 3(報道) | https://seekingalpha.com/news/4598492-okta-expects-q2-fy2027-9-percent-revenue-growth-with-26-percent-non-gaap-operating-margin-as | 2026-05 | Q1 説明会の要約 |
| 3(トランスクリプト) | https://bullfincher.io/companies/okta/earnings-call/fy2027-q2 | 2026-08 | 本文未読 |
| 3(トランスクリプト) | https://www.sahmcapital.com/news/content/okta-reports-q2-2027-results-full-earnings-call-transcript-2026-08-27 | 2026-08-27 | 本文未読 |

## 9. 再開用の検索計画(優先順)

検索ツールの制約: WebFetch・curl は使えない。WebSearch は 1 回で要約と URL を返す。以下は各項目で試す検索語の案である。

1. **A-1(最優先)**: 「Okta Q2 fiscal 2027 earnings call transcript」の全文(質疑応答を含む)/ 「Okta Q4 fiscal 2026 earnings call」/ 「Okta Q3 fiscal 2026 earnings call」/ 「Okta Oktane 2026 keynote」/ 「Okta investor day 2026 medium-term targets」。
2. **A-2**: 「Okta fiscal 2028 outlook free cash flow margin target」「Okta long-term operating margin target」。
3. **A-3**: 「Okta acquires Spera Security」「Okta acquires Axiom Security」「Okta Auth for GenAI」「Okta Cross App Access」「Okta Identity Threat Protection」「Okta privileged access general availability」「Okta share repurchase authorization 2026」「Okta public sector FedRAMP」。
4. **A-4・G**: 「Okta guidance beat history fiscal 2024 2025 2026」「Okta Secure Identity Commitment progress」「Okta 2023 support system breach lawsuit settlement」「Okta Form 4 McKinnon sale 2026」「Okta proxy statement 2026 executive compensation metrics」。
5. **B**: 「Okta price target raised analyst September 2026」「Okta downgrade analyst 2026」「Okta bear case Microsoft Entra bundling」「Okta stock 52-week high low 2026」「software stocks AI disruption fears Okta」「Okta short seller report」。
6. **C**: 「Okta Workforce Identity pricing per user 2026」「Auth0 pricing MAU 2026 change」「Gartner Magic Quadrant Access Management 2025 Okta」「Okta Gartner Peer Insights rating」「Okta jobs hiring sales engineers 2026」「Microsoft Entra Agent ID Okta」「SailPoint Ping Identity CyberArk Okta competitor 10-K」「identity access management market size CAGR 2026」。
7. **D**: 「Palo Alto Networks CyberArk acquisition completed identity」「non-human identity AI agents market 2026」「cybersecurity budget survey 2026 identity」。
8. **株価**: 「OKTA stock closing price October 9 2026」(TradingView は直接取得不可。allowed_domains を tradingview.com にした検索も併用)。
