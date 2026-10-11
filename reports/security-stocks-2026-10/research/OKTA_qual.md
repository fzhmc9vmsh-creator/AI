# Okta(OKTA)定性調査 一次整理(再開版)

- 対象: Okta, Inc.(NASDAQ-OKTA、決算期末 1月31日。FY2027 = 2026年2月〜2027年1月)
- 評価基準日: 2026-10-11。本書の取得日はすべて 2026-10-11。
- 担当範囲: 定性情報の収集と一次整理。評価・投資判断は含まない。数値データ(四半期業績・KPI)は別担当が集めるため、ここでは定性の理解に必要な最小限だけを載せた。

## 0. 本書の状態と取り扱い上の注意

**検索の実績。** 初回に3回、再開で18回(上限)を使い切った。再開版の検索は、市場の仮説(B)、経営陣シナリオ(A)、一次情報(C)の順に配分した。

**情報源の Tier(信頼段階)。**
- Tier 1 = 会社IR・SEC 提出書類。Tier 2 = 公的統計。Tier 3 = 主要報道・アナリスト・決算説明会の書き起こし・データサイト(MarketBeat、TipRanks、GuruFocus、Stock Titan など)。Tier 4 = 個人ブログ・投稿サイト・レビューサイト・SNS。

**重要な限界。**
1. 検索結果は要約文であり、**原ページ本文を直接読んでいない**。会社IRや SEC のURLが検索結果に出ていても、数値は「検索要約経由」である。分析の根拠に使う前に、原ページで再確認すること。
2. 決算説明会の発言は、第三者の要約に基づく和訳である。**逐語の引用ではない**(括弧で原文を付けたものだけが、要約中に引用符つきで現れた文言)。
3. 重要な数値が2つ以上の出典で食い違う場合は、両論併記し「未確定」と書いた。
4. モデルの記憶にある事項は、出典URLを付けられないため入れていない。見つからなかった項目は「欠損」とした。

**用語(初出での一言定義)。**
- ARR = 年間経常収益。ACV = 年間契約価値。RPO = 残存履行義務(契約済みで未計上の売上の総額)。cRPO = そのうち12か月以内に売上計上される見込みの額。bookings = 新規・更新を含む契約獲得額。
- GAAP = 米国会計基準。non-GAAP = 株式報酬などを除いた会社定義の調整後基準。FCF = フリーキャッシュフロー(営業キャッシュフロー − 設備投資)。SBC = 株式報酬費用。
- IAM = アイデンティティ・アクセス管理(誰が何にアクセスできるかを管理すること)。IGA = アイデンティティ・ガバナンス(アクセス権の棚卸し・承認の自動化)。PAM = 特権アクセス管理(管理者権限など強い権限の管理)。ITDR = アイデンティティ脅威の検知と対応。
- 10b5-1 計画 = 株式売却を事前に決めた計画に従って実行する制度。

---

## A. 経営陣シナリオの一次情報

### A-0. 確認できた範囲でのシナリオの骨格(各要素の確認状況つき)

経営陣のシナリオは、次の組み立てとして語られている。各要素の根拠は A-1〜A-3 に置いた。

| 要素 | 経営陣の主張(要約) | 確認状況 |
|---|---|---|
| 2本柱 | Workforce Identity(従業員向け)と Customer Identity(顧客向け、Auth0)の両方で ACV の成長が加速した(Q2 FY27) | 説明会要約で確認(Tier 3)。加速の基準期間は未確認 |
| 新製品 | 新製品が Q2 の契約獲得の約30%を占め、Identity Governance が牽引。新製品を含む案件の ACV 上乗せは平均約40% | 説明会要約で確認(Tier 3) |
| 特権アクセス・脅威検知 | Spera Security(2024年2月完了)と Axiom Security(2025年9月完了)を買収し、ITDR と Privileged Access を拡張 | 会社IR・10-K 要約で確認(Tier 1) |
| AIエージェント | 「Okta for AI Agents」を提供。AIエージェントにもアイデンティティの統制が必要になる。ただし AI 案件は売上にまだ実質的な影響がない | 確認(Tier 1・3)。売上規模は欠損 |
| 営業・販売の体制 | パートナー経由の案件は大型化し成約率が上がる。上位20案件はすべてパートナーが関与。プロフェッショナルサービスをパートナーへ移す | 説明会要約で確認(Tier 3) |
| 公共部門 | CEO は「公共部門全体が非常に重要」と発言 | 要約のみ(Tier 3)。具体数値は欠損 |
| 利益率とFCF | FY2027 の non-GAAP 営業利益率 26%、FCFマージン 28〜29% | 説明会要約で確認(Tier 3) |
| 資本政策 | 2026年満期の転換社債を現金で完済。自社株買いを実施(受取利息の減少として FCF ガイダンスに織り込み) | 会社IR要約で確認(Tier 1)。自社株買いの規模は欠損 |

### A-1. 直近の決算説明会と Oktane 投資家向け説明会での経営陣の発言

**取得範囲。** FY2027 Q2(2026-08-26)、Q1(2026-05-28)、FY2026 Q3(2025-12-02)、Q4(2026年3月初旬)、Oktane 2026 投資家向け説明会(2026年9月下旬)。いずれも要約経由で、書き起こしの全文は未読。

#### FY2027 Q2(2026年7月31日終了、説明会 2026-08-26)

| 発言者 | 内容(和訳。要約経由) | 重要な理由の注記 | 出典(Tier) |
|---|---|---|---|
| Todd McKinnon(CEO、共同創業者) | 成長は、AIエージェントにもアイデンティティの統制が必要になることと結びついている | 経営陣が AIエージェントを需要の追加要因として語っている | 会社IR要約(Tier 1) |
| McKinnon | ACV の成長が Workforce と Customer の両方で加速した。Q2 は第4四半期を除いて過去最高の契約獲得の四半期だった | 売上成長が11%でも先行指標は強いという主張。加速の基準は未確認 | 説明会要約(Tier 3) |
| McKinnon | 最大の競合は「混乱」である(原文の趣旨: "the biggest competitor is confusion") | 競合の製品ではなく、標準・価格・エージェント数の定義が定まらない状況が、導入の遅れの主因だと言っている。Microsoft との直接比較を避けた発言でもある | 説明会要約(Tier 3) |
| McKinnon | 大企業向けでは、年間契約100万ドル超の顧客が22%増(別の要約では「600社超、20%超の増加」) | 大口顧客の拡張が成長の中身であることを示す。20%と22%の食い違いは未確定 | 説明会要約(Tier 3)・2つの要約で数値差 |
| McKinnon | Microsoft・Salesforce・ServiceNow など特定プラットフォームの会社は、競合するクラウドやモデルをまたいでエージェントを統治する中立性を欠く。Okta は他社の管理画面と連携する「停止スイッチ(kill switch)」兼制御層になる | アナリストの「重なり」の質問への回答。中立性が優位の源泉だという主張 | 説明会要約(Tier 3) |
| McKinnon | ある顧客では AIエージェント(Claude のエージェント)が数週間で50インスタンスから約1,500に増えた | AIエージェント数の増加を示す顧客事例。顧客名・契約額は欠損 | 説明会要約(Globe and Mail、Tier 3) |
| McKinnon | AI 案件は売上にまだ実質的な影響がない。一方でパイプライン(商談の見込み)は過去最高で、AI 案件の1件あたり金額は会社平均より大きい傾向。Q2 に数十件の AI 案件が成約し、数百万ドル規模の契約を含む | 条件9の判断材料。売上は小さいが、先行指標は強いと会社は言っている | 説明会要約(Tier 3)。金額は欠損 |
| McKinnon | AIエージェント向けの価格は、既存の1ユーザー当たり料金への上乗せで、顧客が予測しやすいため好まれている | 価格の単位が「ユーザー課金」の延長であることを示す | 説明会要約(Tier 3) |
| Brett Tighe(CFO) | 新製品群が強く貢献し、Okta Identity Governance が牽引した(原文: "strong contributions from our portfolio of new products, led by Okta Identity Governance") | 新製品の寄与が契約獲得の約30%。売上に出るまでの時間差が論点 | 会社IR要約(Tier 1) |
| Tighe | FY27 通期は、売上成長 10〜11%、non-GAAP 営業利益率 26%、FCFマージン 28〜29%(原文: "total revenue growth of 10% to 11%, non-GAAP operating margin of 26% and a free cash flow margin of 28% to 29%") | Q1 時点の FCF ガイダンス(27〜28%)から1ポイント引き上げ | 説明会要約(Tier 3) |

質疑応答で名前が確認できたアナリスト: Jonathan Ho(William Blair)。ほかの質問者は要約に名前が出なかった(§B-1)。

#### FY2027 Q1(2026年4月30日終了、説明会 2026-05-28)

| 発言者 | 内容(和訳。要約経由) | 重要な理由の注記 | 出典(Tier) |
|---|---|---|---|
| McKinnon | 市場が「ファンダメンタルズ(実績)重視」に戻ったことはアイデンティティ・セキュリティに追い風だが、エージェント向けアイデンティティの需要には、まだ表れていない | 5月時点では AI 需要を数字で示せていなかった。Q2 で「数十件の AI 案件」に進んだ | 説明会要約(Tier 3) |
| McKinnon | AIエージェント製品は事業に「実質的に寄与していない」 | Q1・Q2 とも同じ認識 | 説明会要約(Tier 3) |
| 会社(CFO) | 通期ガイダンスには、売上・FCFマージンそれぞれ約1ポイントの下押しを織り込み(プロフェッショナルサービスをパートナーへ移すこと、受取利息の減少) | 会社が自ら成長率を約1ポイント下げる選択をしている。パートナー移管は売上を下げる代わりに利益率を守る意図と読める(意図の解読は分析者に委ねる) | 説明会要約(Tier 3)・会社IR要約(Tier 1) |

Q1 説明会で名前が確認できたアナリスト: Brian Essex(JPMorgan)、Adam Tindle(Raymond James)。

#### FY2026 Q3(2025年10月31日終了、説明会 2025-12-02)

- 売上 7億4200万ドル(+12%)、non-GAAP EPS 0.82ドル(事前予想 0.76ドル、売上予想 7億3000万ドル)。通期ガイダンスは引き上げたが、**次年度(FY2027)の初期ガイダンスを示さなかった**。株価は下落した。(CNBC、2025-12-02、Tier 3)
- McKinnon は、大企業顧客の強さ、Identity Governance など新製品の採用、強いキャッシュフローを成長の要因に挙げた。(同、Tier 3)
- URL: https://www.cnbc.com/2025/12/02/okta-q3-earnings-report-2026.html

#### FY2026 Q4(説明会は2026年3月初旬。検索結果の記載は3月4日)

- Q4 売上 7億6100万ドル(+11%)。Q4 ガイダンス(7億4800万〜7億5000万ドル)を上回った。cRPO の成長率は+12%で、事前予想の+9%を上回った(D.A. Davidson の見方、Tier 3)。
- FY2027 の初期売上ガイダンスは約31.7億ドルから(上限は検索結果で切れており欠損)。Q1 FY2027 の売上ガイダンスは7億4900万〜7億5300万ドル(+約9%)。報道は「好決算だがガイダンスは弱く、AI の圧力を示す」と評した(TechBuzz、Tier 4)。
- URL(会社IR・SEC): https://www.sec.gov/Archives/edgar/data/1660134/000166013426000016/okta-1312026_ex991.htm

#### Oktane 2026 投資家向け説明会(2026年9月下旬)

| 項目 | 内容(要約経由) | 出典(Tier) |
|---|---|---|
| 新たな中期目標 | 示されなかった。アナリストの一部は、新しい財務ガイダンスや長期目標が出なかったことに失望した | Investing.com・Yahoo Finance の要約(Tier 3) |
| 市場の見方 | McKinnon は「エージェント向けセキュリティ市場は、いずれ現在のIAM市場を上回りうる」と述べた。ただし導入には時間がかかり、競争も強まると認めた | 同上 |
| 位置づけ | Okta はAIエージェントのアイデンティティの制御層を目指す。「Okta for AI Agents」は現時点で市場で唯一の一般提供(GA)製品だと会社は主張 | 同上(会社の主張) |
| 価格 | ユーザー単位の課金から、エージェント単位の課金へ移ると予想 | 同上 |
| 競合として名指し | Microsoft、IBM、ServiceNow | 同上 |
| 導入の足かせ | 標準・価格・エージェント数の定義の混乱が、近い将来の導入の足かせ | 同上 |
| 製品枠組み | 「安全なエージェント型企業のための青写真(Blueprint)」: エージェントの登録簿、権限とガバナンス、実行時の監視、停止スイッチ(kill switch)による対応 | 同上 |

URL: https://www.investing.com/news/transcripts/okta-at-oktane-call-2026-investor-summit-betting-on-agentic-ai-93CH-4913776 / https://finance.yahoo.com/technology/ai/articles/okta-sees-ai-agent-identity-210208369.html / 書き起こし掲載: https://stockanalysis.com/stocks/okta/transcripts/752297-the-oktane-call-2026-investor-summit/

### A-2. 数値目標(中期の売上成長率・FCFマージン・営業利益率)

- **中期目標は確認できなかった(欠損)。** Oktane 2026 投資家向け説明会でも新たな長期目標は出なかったと報じられている(§A-1)。過去の Investor Day の目標(FY2028 以降の成長率・FCFマージン・営業利益率)は未取得。
- **通期ガイダンスの推移(FY2027、会社発表)。**

| 時点 | 売上ガイダンス | FCFマージン | 出典(Tier) |
|---|---|---|---|
| FY2026 Q4 発表(2026年3月初旬) | 約31.7億ドルから(上限欠損) | 欠損 | SEC 8-K 要約(Tier 1) |
| Q1 発表(2026-05-28) | 31億8500万〜32億500万ドル(+9〜10%) | 27〜28%(8億5500万〜8億8500万ドル) | 会社IR要約(Tier 1) |
| Q2 発表(2026-08-26) | 32億1600万〜32億2600万ドル(+10〜11%) | 28〜29% | 会社IR・説明会要約(Tier 1・3) |

non-GAAP 営業利益率は FY2027 通期で 26%(Q2 説明会、Tier 3)。ただし Q2 単独の実績は 28%(non-GAAP 営業利益 2億2600万ドル)。
- 定義の注意: ガイダンスの FCF は「non-GAAP FCF」(会社定義)。税率は non-GAAP 長期税率を 26% から 21% に引き下げた(Q1、米国税制改正法による)。

### A-3. ピース一覧

| ピース | 目的(会社の説明) | 発表日 | 規模・進捗の数値 | 出典(Tier) |
|---|---|---|---|---|
| Okta Identity Governance(IGA) | アクセス権の棚卸し・承認の自動化。新製品群の牽引役 | 以前に発売(日付欠損) | 新製品群は Q2 の契約獲得の約30%。新製品を含む案件の ACV 上乗せは平均約40% | 説明会要約(Tier 3) |
| Spera Security 買収 | ITDR とセキュリティ姿勢管理・攻撃対象領域の管理を拡張(Tel Aviv 拠点) | 2023-12-19 発表、2024年2月完了 | 取得額は検索結果に出ず(欠損) | Okta ブログ(Tier 1): https://www.okta.com/blog/identity-security/okta-acquisition-advances-identity-powered-security/ |
| Axiom Security 買収 | Okta Privileged Access に統合。データベース、Kubernetes、クラウド基盤、SaaS への特権アクセスを管理 | 2025年8月下旬に正式契約発表(日付は X 投稿IDからの推定)、2025-09-04 完了 | 取得対価 5400万ドル(現金、FY2026 10-K)。報道の推定は約1億ドル(非公式)。10-K を採用 | X(会社公式、Tier 4): https://x.com/okta/status/1960309105391726704 / 10-K(Tier 1・検索要約経由): https://www.sec.gov/Archives/edgar/data/1660134/000166013426000020/okta-20260131.htm / 報道 https://www.ynetnews.com/business/article/skd50m2fee(Tier 3) |
| Okta for AI Agents | AIエージェントのアイデンティティ統制。Agent Gateway(停止スイッチ)、Configuration Designer、12社の Blueprint Alliance | Oktane 2026(2026年9月下旬) | 売上への寄与は実質ゼロと会社が認める。数十件の案件が Q2 に成約 | 報道要約(Tier 3)。詳細は §F |
| パートナー経由の販売 | パートナー関与の案件は大型化し、成約率が上がる | Q2 説明会 | 上位20案件すべてにパートナーが関与。最大案件はパートナー起点 | 説明会要約(Tier 3) |
| プロフェッショナルサービスのパートナー移管 | 会社は自社でサービスを提供せず、パートナーへ移す | Q1 説明会 | 売上の約1ポイントの下押しとして通期ガイダンスに織り込み | 説明会要約(Tier 3) |
| 2026年満期の転換社債の償還 | 残元本を現金で完済 | 2026-08-26 時点で完了 | 残元本 3億5000万ドルを現金で支払い | 会社IR要約(Tier 1) |
| 自社株買い | 未取得(会社の説明は欠損) | 未確認 | 金額・残枠・実施額は欠損。FCF ガイダンスに「自社株買いによる受取利息の減少」を約1ポイント織り込み | 会社IR要約(Tier 1) |
| non-GAAP 税率の変更 | 米国税制改正法(One Big Beautiful Bill Act)への対応 | Q1(2026-05-28) | 26% → 21%。将来に向けて適用 | 会社IR要約(Tier 1) |

**今回の検索では確認できなかったピース(欠損)。** Identity Threat Protection の売上寄与、Auth for GenAI、Cross App Access、価格改定、営業組織の専門化の具体策、公共部門の数値(FedRAMP 等)、提携の詳細(Anthropic・AWS・ServiceNow・Dell との提携は、Perplexity Finance の要約(Tier 4)に名前があるのみで未検証)。

### A-4. 過去のガイダンス達成状況(最低3年分のうち、確認できた直近分)

**確認できたのは FY2026 Q3 以降の約4四半期分。FY2024・FY2025 は欠損。**

| 四半期 | 期初ガイダンス(売上) | 実績 | 差 | 出典(Tier) |
|---|---|---|---|---|
| FY2026 Q4 | 7億4800万〜7億5000万ドル | 7億6100万ドル | 上限比 +1100万ドル(+1.5%) | Q3 発表(Tier 1・3)・Q4 発表要約 |
| FY2027 Q1 | 7億4900万〜7億5300万ドル(+約9%) | 前年同期比 +11%(金額は欠損) | 成長率で約2ポイント上 | Q4 発表要約(Tier 1)・Q1 見出し(Tier 3) |
| FY2027 Q2 | 7億9000万〜7億9400万ドル(+約9%) | 8億500万ドル(+11%) | 上限比 +1100万ドル(+1.4%) | Q1・Q2 発表要約(Tier 1) |
| FY2027 Q2 の non-GAAP 営業利益 | 1億9600万〜2億ドル(売上比 24〜25%) | 2億2600万ドル(28%) | 上限比 +2600万ドル | Stock Titan の Q1 発表要約(Tier 3)。会社IRで要確認 |
| FY2026 通期 | 29億600万〜29億800万ドル(Q3 時点) | 約29億1900万ドル(9か月累計 21億5800万ドル + Q4 7億6100万ドルの合算。検索ツールによる計算、通期の公式値で要確認) | 約+1100万ドル | Q3 発表・Q4 発表(Tier 1) |

- **読み取れる型(事実のみ)。** 直近4四半期で、実績は常にガイダンスの上限を上回り(売上で約1.4〜1.5%)、FY2027 の通期売上ガイダンスは3月→5月→8月と2回引き上げられた。FCFマージンのガイダンスも27〜28%から28〜29%へ上がった。
- **注意。** FY2026 Q3 時点で、次年度の初期ガイダンスを出さなかった(株価は下落)。保守的に出して上回る型かどうかは、FY2024・FY2025 の期初ガイダンスとの比較が欠損のため、3年では確認できていない。
- **検索結果の混入に注意。** Quiver Quant の見出しは「Q2 の売上はわずかに未達」と読める記述だが、会社発表(8億500万ドル)とコンセンサス(7億9000万〜7億9500万ドル)に反するため採用しない。

### A-5. 2022〜2023年のセキュリティ侵害と Secure Identity Commitment

**欠損。** 今回の検索でこの項目に当たる結果は得られなかった。2023年のサポートシステム侵害の経緯、訴訟の帰結、Secure Identity Commitment(会社が侵害後に公表した、自社と顧客の安全を高める約束)の実施状況は、いずれも未確認。再開時の最優先の検索項目とする(§9)。

### A-6. 経営陣の経歴・在任・報酬KPI・交代

**確認できたこと。**
- Todd McKinnon は CEO 兼共同創業者(説明会の記載)。Brett Tighe は CFO。Eric Kelleher は社長兼 COO(Form 4 報道)。
- **委任状説明書(DEF 14A、2026-05-07 提出、Tier 1・検索要約経由)。** 年次賞与の指標は、売上 60%・non-GAAP 営業利益 40% の配分(第三者の要約。Tier 3-4)。支払いの下限は、売上目標の90%未満、または non-GAAP 営業利益目標の80%未満なら支払いなし(委任状の文言として要約に現れた)。長期の株式報酬は、Nasdaq 総合指数に対する相対 TSR(株主総利回り)を使う PSU(業績連動株式)で、1・2・3年の区分。
- **報酬指標の単位。** 売上と non-GAAP 営業利益はいずれも**総額**であり、1株当たりの指標ではない。株主還元(自社株買い)や希薄化は、相対 TSR 以外では報酬に直接は入っていない(要約に基づく。委任状本文で要確認)。
- McKinnon の FY2026 報酬は 3680万ドル(前年 2330万ドル、+58%)。株式報酬が97%(第三者サイト。委任状の別の要約では「CEO の PSU 割合 60%」とあり、測り方の違いと思われるが未確定)。株主総会では報酬への賛成(say-on-pay、勧告的投票)が承認された。
- 委任状は「AI時代の戦略、取締役会の刷新、経営陣報酬」を含む(Stock Titan 見出し、Tier 3)。取締役の入れ替えの内容は欠損。
- URL: https://www.sec.gov/Archives/edgar/data/0001660134/000166013426000036/okta-20260507.htm / https://www.stocktitan.net/sec-filings/OKTA/def-14a-okta-inc-definitive-proxy-statement-9902a55c1803.html / https://www.panabee.com/news/okta-executive-compensation-2026

**欠損。** 経営陣の経歴の詳細、在任期間、2025〜2026年の役員交代(CFO・CRO など)。

---

## B. 市場の仮説の出典

### B-1. 直近2回の説明会でアナリストが繰り返した質問

名前が確認できた質問者は少数にとどまる(書き起こし全文は未読)。

| 説明会 | 質問者(所属) | 質問の趣旨 | 出典(Tier) |
|---|---|---|---|
| Q2 FY27(2026-08-26) | 名前なし(要約) | AIエージェントで、Microsoft・Salesforce・ServiceNow の製品と Okta はどこまで重なるか | 説明会要約(Tier 3) |
| Q2 FY27 | Jonathan Ho(William Blair) | 競合の力学(回答は McKinnon の「最大の競合は混乱」) | roic.ai 書き起こし要約(Tier 3) |
| Q1 FY27(2026-05-28) | Brian Essex(JPMorgan) | 内容は要約に出ず | 書き起こし掲載ページ(Tier 3) |
| Q1 FY27 | Adam Tindle(Raymond James) | 内容は要約に出ず | 同上 |

**繰り返されたテーマ(要約から読み取れる範囲)。**
1. AIエージェント向けの需要が売上にいつ出るか(Q1 は「まだ表れていない」、Q2 は「パイプラインは最高だが売上は小さい」)。
2. Microsoft などプラットフォーム各社との重なりと、価格・バンドルの圧力。
3. 成長の再加速が可能か(Mizuho の指摘。§B-2)。
4. 座席(シート)数の伸びについての質問は、今回の要約には現れなかった(欠損)。

書き起こし全文の所在: https://s205.q4cdn.com/566291348/files/doc_financials/2027/q2/Okta-Q2-FY27-Earnings-Call_Transcript.pdf(会社IR、未読) / https://www.fool.com/earnings/call-transcripts/2026/08/31/okta-okta-q2-2027-earnings-call-transcript/ / https://www.roic.ai/quote/OKTA/transcripts/2027-year/2-quarter / https://www.fool.com/earnings/call-transcripts/2026/05/28/okta-okta-q1-2027-earnings-call-transcript/

### B-2. 強気派と弱気派の主要論点

#### 強気派(証券会社名・目標株価・論拠)

| 証券会社(アナリスト名) | 評価・目標株価(日付) | 論拠(要約) | 出典(Tier) |
|---|---|---|---|
| Morgan Stanley(名前欠損) | Overweight、目標株価 245ドル(200ドルから、2026-09-29) | エージェント型AIによるアイデンティティ需要。ただし株価がすでに約140%上昇しており、期待は高いと同社自身が注記 | Yahoo Finance(Tier 3): https://finance.yahoo.com/markets/stocks/articles/morgan-stanley-resets-okta-stock-192343050.html |
| Scotiabank(名前欠損) | 目標株価 245ドル(190ドルから、2026年9月下旬) | Oktane 2026 でのAIエージェントへの強い関心 | Parameter・Startup Fortune 等の要約(Tier 3-4): https://parameter.io/okta-okta-stock-surges-4-on-bullish-ai-agent-forecasts-from-wall-street/ |
| Needham(名前欠損) | 目標株価 230ドル(2026-09-23)。8月27日には200ドル(140ドルから、当時の最高値) | 新しいアイデンティティ製品の早期の顧客採用 | StocksToTrade・Yahoo Finance(Tier 3): https://stockstotrade.com/news/okta-inc-okta-news-2026_09_23/ / https://finance.yahoo.com/markets/stocks/articles/okta-stock-just-got-street-201450706.html |
| Stephens(名前欠損) | 目標株価 240ドル(190ドルから、2026-09-25) | 論拠は要約に出ず | TipRanks 要約(Tier 3) |
| KeyBanc、Baird | 2026-09-24 に目標引き上げ(金額欠損)。Oktane 後に6社が215〜240ドルへ引き上げ、いずれも買い相当の評価を維持 | 論拠は要約に出ず | TipRanks 要約(Tier 3) |
| RBC、Citizens、Guggenheim | RBC 195ドル、Citizens 180ドル、Guggenheim 188ドル(162ドルから)。いずれも 2026-08-27 の Q2 決算後 | 決算の上振れと上方修正 | Yahoo Finance(Tier 3) |

- 集計: TipRanks のコンセンサス平均目標は約215ドル(直近3か月、35人)、最高245ドル。格付けの内訳は買い73・中立18・売り0(内訳の人数と件数の関係は不明。TipRanks の集計方法で要確認)。Tier 3、単独出典。https://www.tipranks.com/stocks/okta/forecast
- Futurum Group の見方: Q2 は「好決算と上方修正(Beat and Raise)」(Tier 3)。https://futurumgroup.com/insights/okta-q2-fy-2027-earnings-beat-and-raise-on-core-identity-strength/

#### 弱気派・中立派

| 証券会社(アナリスト名) | 評価・目標株価(日付) | 論拠(要約) | 出典(Tier) |
|---|---|---|---|
| Mizuho(Gregg Moskowitz) | Outperform から Neutral へ引き下げ。目標株価 125ドル(110ドルから、2026-06-02)。発表直後、寄り付き前に株価は約8%下落 | 現在の水準では株価評価が十分に織り込まれている。エージェント型AIの恩恵を受ける位置にあるが、時期と規模は初期段階で不確か。**近い将来から中期で成長を大きく再加速できると、まだ確信できない** | GuruFocus・Investing.com(Tier 3): https://www.gurufocus.com/news/8896279/okta-downgraded-by-mizuho-price-target-raised-to-125 / https://www.investing.com/news/analyst-ratings/mizuho-downgrades-okta-stock-rating-on-valuation-concerns-93CH-4722447 |
| Bernstein(名前欠損) | Outperform から Market Perform へ引き下げ。目標株価 174ドル(143ドルから、2026-09-17) | 急騰後の株価評価(二次情報。個別のレポートは未確認) | MarketBeat の表・Quiver Quant(Tier 3): https://www.quiverquant.com/news/Okta+Slides+as+Analyst+Downgrade+Pressures+Cybersecurity+Shares |
| BofA(Tal Liani) | Neutral、目標株価 220ドル(200ドルから) | 論拠は要約に出ず | TipRanks 要約(Tier 3、単独出典。他で未確認) |
| Seeking Alpha の個人寄稿者 | Hold へ引き下げ(2026-10-05)。「サイバーセキュリティ業界は過熱している」 | 年初来約150%上昇し、株価評価が高すぎる。TAM 800億ドル・高い20%台の営業利益率を引用しつつ、競争の激しさと希薄化への懸念 | Seeking Alpha(Tier 4): https://seekingalpha.com/article/4952045-okta-the-cybersecurity-sector-is-overheated-downgrade |
| TIKR のブログ | 「利益率はようやく拡大している。株価評価が先に追いついたかもしれない」(見出しのみ) | 内容は未読 | Tier 4: https://www.tikr.com/blog/oktas-margins-are-finally-expanding-the-valuation-may-have-gotten-there-first |

- 比較の事実: Bernstein の目標株価 174ドルは、COO の売却価格帯(2026-09-18 に 181.70〜188.56ドル)より低い。Mizuho の 125ドルは、6月2日の役員売却価格(134.13ドル)より低い。
- 会社自身も、AI の寄与は FY2027 では実質的な影響がない(immaterial)と述べている(24/7 Wall St.、Tier 3: https://247wallst.com/investing/2026/09/25/half-a-dozen-analysts-have-a-buy-signal-on-okta/)。

### B-3. 論点別の見方の有無

| 見方 | 有無 | 内容と出典 |
|---|---|---|
| 「成長が鈍化した低成長株」 | あり | Mizuho が「成長の再加速にまだ確信がない」(2026-06-02)。売上成長は約10〜12%台(Q3 FY26 +12%、Q4 +11%、Q2 FY27 +11%)。FY2027 初期ガイダンスは約9%(Q4 発表要約) |
| 「Microsoft Entra ID のバンドルに負ける」 | 比較記事では存在、アナリストの明示は未確認 | Entra ID P1 は Microsoft 365 の E3・Business Premium などに含まれ、P2 は E5 に含まれる。E5 を契約済みなら Entra の限界費用はほぼゼロに見える(Tier 4 ブログ)。Okta は多様な環境(Google Workspace、AWS、Salesforce 等)で強いと各比較記事が述べる(§C) |
| 「シート数(従業員数)の伸び鈍化」 | 今回の検索では確認できず(欠損) | 説明会の要約にシート数の開示はなかった。AIエージェント向けの価格が「ユーザー課金への上乗せ」であることは確認(§A-1) |
| 「AIによる代替(ソフトウェア全体への売り)」 | あり | 2026年2月、Anthropic が Claude 向けコードセキュリティツールを公開したことを契機に、ソフトウェア株が売られ、Okta は2月に14.2%下落(§B-5) |
| 「AIエージェント時代にアイデンティティ需要が増える」 | あり | 経営陣・Morgan Stanley・Needham・Scotiabank・Stephens など(§B-2)。Okta は「エージェント向けセキュリティ市場は現在のIAM市場を上回りうる」と主張(§A-1) |

### B-4. 空売りレポート・著名な弱気論者

**今回の検索では確認できず(欠損)。** 空売りレポートは見つからなかった。弱気論は §B-2 の証券会社(Mizuho、Bernstein)と Seeking Alpha 寄稿者(Tier 4)にとどまる。会社の反論も欠損。

### B-5. 報道のナラティブと株価の推移

**ナラティブ(見出しで繰り返される言葉)。**
- 下落局面(2026年2月): 「ソフトウェア終末(software apocalypse)」「AI による代替」。例: "Okta Stock Is Down 20% in 2026. Can It Survive the Software Apocalypse?"(Yahoo Finance、Tier 3)、"Okta Beats Q4 Estimates But Weak Guidance Signals AI Pressure"(TechBuzz、Tier 4)。
- 上昇局面(8〜9月): 「AIエージェント(の統制)」「停止スイッチ」「ウォール街がAIエージェントに全面賭け」。例: "Okta ships an AI agent kill switch and Wall Street immediately raises its price target"(Startup Fortune、Tier 4)、"Okta Triples Valuation After AI Security Rally"(SaaSrise、Tier 4)。
- 現在: 「すでに織り込み済みか」。例: "Is the Stock Already Pricing It In?"(Insider Monkey、Tier 4)、Morgan Stanley の「期待は高い」。

**株価の推移(検索結果から確認できた主要イベント。株価の値は報道ごとに食い違いがあり、終値の精度は保証しない)。**

| 日付 | 出来事 | 株価・変化 | 出典(Tier) |
|---|---|---|---|
| 2026年初 | 年初の水準は、約83ドルと逆算(2月23日の安値68.77ドルが年初来 −16.99% という報道からの計算) | 約83ドル(逆算、要確認) | Yahoo Finance(Tier 3)から計算 |
| 2026-02-20・23 | Anthropic の Claude 向けコードセキュリティツール公開を契機に、ソフトウェア株が売られる。2/20 に −9.2%、2/23 は日中 −6.4%。52週安値 68.77ドル(2/23)。2月全体で −14.2% | 68.77ドル | Motley Fool(2026-03-08)ほか(Tier 3): https://www.fool.com/investing/2026/03/08/why-oktas-shares-tumbled-14-last-month/ |
| 2026年3月初旬 | Q4 FY26 決算。cRPO +12%(予想 +9%)だが、FY2027 の初期ガイダンスは「弱い」と報じられた | 欠損 | D.A. Davidson の見方・TechBuzz |
| 2026-06-02 | Mizuho が格下げ(Neutral、125ドル)。寄り付き前に約 −8% | 約134ドル(同日の役員売却価格) | GuruFocus(Tier 3) |
| 2026-07-08 | CEO が10b5-1計画で売却 | 約145〜149ドル | Stock Titan(Tier 3) |
| 2026-08-26/27 | Q2 決算。翌日に1日で約+19%(新製品が契約獲得の約30%、非Q4で過去最高の契約獲得)。年初来高値を更新 | 欠損(目標株価 180〜200ドルの引き上げが続く) | Investing.com・Invezz(Tier 3): https://invezz.com/au/news/2026/08/27/analysts-see-further-upside-as-okta-stock-hits-ytd-high-on-q2-earnings/ |
| 2026-09-17〜18 | Bernstein が格下げ。COO が売却 | 181.70〜188.56ドル | Quiver Quant・Investing.com(Tier 3) |
| 2026-09-22〜25 | Oktane 2026。9/23 に +4.45%。9/25 に −5.5% で終値 195.19ドル | 195.19ドル | StocksToTrade・CoinCentral(Tier 3-4) |
| 2026-09-29 | Morgan Stanley・Scotiabank が目標を引き上げ | 202.18ドル(日中、+4%) | Yahoo Finance・MoneyCheck(Tier 3) |
| 年初来 | 約+140%(Morgan Stanley の指摘)、約+150%(2026-10-05 の Seeking Alpha) | | 同上 |

- **食い違い(未確定)。** ある記事は「52週安値は4月」と書き、別の記事は「安値は2月23日の68.77ドル」と書く。TipRanks の目標株価の上値余地から逆算した株価(約131ドル)と、Perplexity Finance の約182ドルも食い違う(後者は古い画面の可能性)。**2026-10-09 の終値は欠損**。別担当の価格データを使うこと。

---

## C. 一次情報(スカットルバット)— 5件(いずれも強度は限定的)

| # | 一次情報 | 観察できること | 出典(Tier) |
|---|---|---|---|
| C1 | Gartner マジック・クアドラント(Access Management)2025年11月版: Okta は9年連続でリーダー。評価対象は13社・15の評価基準 | 製品の評価は維持されている。Microsoft の位置づけは今回の要約に出ず(欠損)。会社のプレスリリース経由で、Gartner 原本は未確認 | 会社IR(Tier 1): https://www.okta.com/newsroom/press-releases/okta-named-a-leader-in-2025-gartner-magic-quadrant/ |
| C2 | Gartner Peer Insights「顧客の声: Access Management」で Okta は6年連続の Customers' Choice(2025) | 顧客評価が維持されている。評点の数値は欠損 | 同上(会社発表、Tier 1) |
| C3 | PeerSpot の市場シェア(閲覧比率)スナップショット(2026年8月): Microsoft Entra ID 5.8%(前年 14.8%)、Okta Platform 4.4%(前年 5.7%)、Ping Identity を含む比較 | 両者とも比率が低下。カテゴリ内の他製品の増加が理由と思われるが、原因は出典に説明なし。財務の指標ではない | PeerSpot(Tier 4): https://www.peerspot.com/products/comparisons/microsoft-entra-id_vs_okta-platform_vs_ping-identity-platform |
| C4 | 価格の比較: Microsoft Entra ID P1 は1ユーザー月7ドル、Okta Starter は月6ドル(同等の機能比較ではない)。Entra P1 は Microsoft 365 E3・Business Premium に、P2 は E5 に含まれる | バンドルの圧力の構造。Okta の標準価格表の改定や Auth0 の MAU(月間アクティブユーザー)課金の改定は未確認(欠損) | 比較ブログ(Tier 4): https://www.siit.io/tools/comparison/microsoft-entra-id-vs-okta / https://softwarepricingguide.com/okta-vs-microsoft-entra-id-pricing-2026-the-real-cost-of-identity-sso-mfa-and-governance/ |
| C5 | Palo Alto Networks の 10-Q: CyberArk の取得対価は現金23億ドル+PANW 株式1億1200万株。2026-02-11 に取得完了 | 競合の開示でアイデンティティを「中核の柱」と位置づけた。Okta への直接の言及は要約になし | Palo Alto Networks 10-Q(Tier 1・検索要約経由): https://www.sec.gov/Archives/edgar/data/1327567/000132756726000005/panw-20260131.htm |

**欠損(取得できなかった一次情報)。** 求人動向(営業・導入支援)、IAM 市場規模・成長率の公的統計、従業員数(シート数)の伸び鈍化のシート課金への影響、SailPoint・Ping Identity・CrowdStrike Identity の開示で Okta に触れたもの、Okta 自身の価格表の改定履歴。再開時の検索項目に入れた(§9)。

## D. 競争と業界の構造

| 論点 | 確認できた事実 | 出典(Tier) |
|---|---|---|
| アイデンティティ市場の統合 | Palo Alto Networks が CyberArk の買収を 2026-02-11 に完了。人間・機械・エージェントのアイデンティティを統合して守ると説明。CyberArk 製品は単独のプラットフォームとしても提供を継続。Palo Alto Networks は Protect AI の買収にも合意(報道で5億ドル超) | 会社IR(Tier 1): https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-cyberark-to-secure-the-ai-era |
| Microsoft のバンドル圧力 | Entra ID の上位プランが Microsoft 365 の上位ライセンスに含まれる(C4)。McKinnon はエージェント統治で「プラットフォーム特化の会社は中立性を欠く」と反論 | Tier 4・3 |
| AIエージェント(非人間アイデンティティ)の新市場 | 会社は「エージェント型セキュリティ市場は現在のIAM市場を超えうる」と主張。競合として Microsoft・IBM・ServiceNow を名指し。市場規模の公的統計は取得できず(欠損) | Oktane 要約(Tier 3) |
| 価格の単位の変化 | ユーザー課金から、エージェント課金への移行を会社は予想 | Oktane 要約(Tier 3) |
| セキュリティ予算の動向 | 欠損 | |

---

## E. 異常値の候補(8つ)

答えは出さず、問いだけを置く。出典は §A〜§B。

| # | 異常値の候補 | 数字 | 問い |
|---|---|---|---|
| E1 | 売上成長が10%台前半なのに FCFマージンが高く、同時に自社株買いと転換社債の現金償還を行っている | 売上 +11%、FCF 売上比 28%(Q2)・35%(Q1)、FY2027 ガイダンス 28〜29%、転換社債 3億5000万ドルを現金償還 | なぜ成長が鈍くても FCF が厚いのか(前受け収入、SBC、受取利息のどれが寄与するか) |
| E2 | cRPO の成長率が加速し、売上成長率を上回った | cRPO +12%(Q4 FY26)→ +12%(Q1)→ +14%(Q2)。RPO +17%。売上 +11% | なぜ先行指標が売上より速く伸びているのか(契約期間の長期化か、新製品の上乗せか) |
| E3 | GAAP と non-GAAP の営業利益率の差が大きい | GAAP 13%、non-GAAP 28%(Q2、差15ポイント) | なぜ差が15ポイントもあるのか(SBC と買収無形資産の償却の内訳) |
| E4 | non-GAAP 税率の変更だけで non-GAAP EPS が上がる | 26% → 21%(Q1 発表) | EPS の成長のうち、税率変更で説明できる部分は何割か |
| E5 | 自社株買いと債務償還による受取利息の減少が FCF を下押しする | 約1ポイント(Q1) | 現金を持つ価値(利息収入)より買い戻しを優先した根拠は何か |
| E6 | 新製品が契約獲得の約3割を占めるのに、売上成長は10%台前半にとどまる | 新製品が Q2 契約獲得の約30%、売上 +11% | なぜ新製品の寄与が売上に出ていないのか(時間差か、既存製品の縮小・値引きか) |
| E7 | AI の寄与が実質ゼロなのに、株価は年初来で2倍超になった | AI は売上に実質影響なし(Q1・Q2)。株価は約83ドル(逆算)→ 202ドル(9/29)、年初来 +140% | なぜ市場は売上ではなくAIエージェントの期待に価格をつけたのか。2月の安値(68.77ドル)は何を織り込んでいたのか |
| E8 | 会社自身が売上成長を約1ポイント下げる選択をしている | プロフェッショナルサービスのパートナー移管で売上に約1ポイントの下押し(Q1) | なぜ成長率を下げてまで移管するのか。利益率やFCFには何が起きるのか |

PER の低さ(依頼文の例示)は、株価・EPS を別担当が収集するため、本書では候補にしていない。

## F. 条件9(AIの停めない運用)に関わる事実

| 項目 | 開示内容 | 出典(Tier) |
|---|---|---|
| 製品 | 「Okta for AI Agents」: Agent Gateway(停止スイッチ。エージェントの動作を止める制御)、Configuration Designer、エージェントの登録簿、権限とガバナンス、実行時の監視、停止スイッチによる対応。「安全なエージェント型企業のための青写真」と、12社の Blueprint Alliance | Oktane 要約(Tier 3) |
| 提供状況 | 会社は「市場で唯一の一般提供(GA)製品」と主張(会社の主張。検証なし) | 同上 |
| 価格 | 既存の1ユーザー当たり料金への上乗せ。将来はエージェント単位の課金に移ると会社は予想 | Q2・Oktane 要約(Tier 3) |
| 売上規模 | AI 案件は売上にまだ実質的な影響がない(Q1・Q2)。金額は欠損 | 説明会要約(Tier 3) |
| 商談 | パイプラインは過去最高。AI 案件の1件当たり金額は会社平均より大きい傾向。Q2 に数十件が成約し、数百万ドル規模を含む | Q2 要約(Tier 3) |
| 顧客事例 | ある顧客で Claude のエージェントが数週間で約50から約1,500に増加(顧客名は欠損) | Globe and Mail の Q2 要約(Tier 3) |
| 提携 | Anthropic、AWS、ServiceNow、Dell との提携(Perplexity Finance の要約。**未検証**) | Tier 4 |
| 顧客数・ARR | 欠損 | |

**条件9の判断に使う事実の整理(判定は分析者が行う)。** Okta は AI を「守る・止める」側の製品(停止スイッチ、権限管理)を売っており、AI 推論基盤を提供する会社ではない。AI 関連の売上は実質ゼロと会社が認めている。

## G. リスク事象

| 区分 | 確認できた事実 | 出典(Tier) |
|---|---|---|
| 経営陣の株式売却 | 全て 10b5-1 計画(事前計画)に基づく売却と報じられている。CEO McKinnon: 2026-07-08 に Class A 株 68,936株を約145〜149ドルで売却(計画の採択は 2026-04-08)。COO Eric Kelleher: 2026-09-18 に 6,395株を181.70〜188.56ドルで売却(計画の採択は 2026-06-12、約117万ドル)。Larissa Schwartz(役職は未確認): 2026-06-02 に 24,971株を平均134.13ドルで売却(保有が51%超減少)。MarketBeat は 2026-09-15 に 42万9633.95ドルの売却も報じた(売り手は未確認) | MarketBeat・Stock Titan・Investing.com・SEC Form 4(Tier 1・3): https://www.marketbeat.com/instant-alerts/insider-selling-okta-nasdaqokta-insider-sells-24971-shares-of-stock-2026-06-04/ / https://www.stocktitan.net/sec-filings/OKTA/form-4-okta-inc-insider-trading-activity-a8e721f9249a.html / https://www.investing.com/news/insider-trading-news/okta-coo-eric-kelleher-sells-117m-in-company-stock-93CH-4918886 |
| 株価評価・希薄化 | Seeking Alpha 寄稿者が株価評価の過熱と希薄化を指摘(Tier 4)。SBC の水準は別担当の数値データで確認 | |
| 会計上の論点 | non-GAAP 税率を 26% から 21% に変更(§E4)。Q2 売上についての「未達」報道は会社発表と矛盾し不採用(§A-4) | 会社IR要約(Tier 1) |
| 競争・規制・セキュリティ侵害の再発・訴訟 | **欠損**。2023年の侵害に関する訴訟の帰結、2025〜2026年の新たな侵害、規制対応は、今回の検索で確認できなかった | |

---

## 8. 出典台帳(今回の検索で結果に現れ、本書で使ったURL)

| Tier | 出典 | 日付 | 備考 |
|---|---|---|---|
| 1 | https://www.okta.com/newsroom/press-releases/okta-announces-second-quarter-2027-financial-results/ | 2026-08-26 | 検索要約経由。原ページ未読 |
| 1 | https://www.okta.com/newsroom/press-releases/okta-announces-first-quarter-2027-financial-results/ | 2026-05-28 | 同上 |
| 1 | https://www.sec.gov/Archives/edgar/data/1660134/000166013426000016/okta-1312026_ex991.htm | 2026-03 | Q4 FY26 決算(8-K 別添)。同上 |
| 1 | https://s205.q4cdn.com/566291348/files/doc_financials/2027/q2/Okta-Q2-FY27-Earnings-Call_Transcript.pdf | 2026-08-26 | Q2 書き起こし(会社IR)。**未読。次に読むべき** |
| 1 | https://s205.q4cdn.com/566291348/files/doc_financials/2027/q2/Q2FY27PostedCommentaryforwebsite.pdf | 2026-08-26 | Q2 の CFO 解説資料。**未読** |
| 1 | https://www.sec.gov/Archives/edgar/data/0001660134/000166013426000069/okta-20260731.htm | 2026-09 | Q2 FY27 の 10-Q。**未読** |
| 1 | https://www.sec.gov/Archives/edgar/data/1660134/000166013426000020/okta-20260131.htm | 2026-03 | FY2026 の 10-K。Axiom の取得対価 |
| 1 | https://www.sec.gov/Archives/edgar/data/0001660134/000166013426000036/okta-20260507.htm | 2026-05-07 | DEF 14A(委任状説明書) |
| 1 | https://www.okta.com/newsroom/press-releases/okta-named-a-leader-in-2025-gartner-magic-quadrant/ | 2025-11-18 | Gartner MQ(会社発表) |
| 1 | https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-cyberark-to-secure-the-ai-era | 2026-02-11 | PANW の CyberArk 取得完了 |
| 1 | https://www.sec.gov/Archives/edgar/data/1327567/000132756726000005/panw-20260131.htm | 2026-02 | PANW 10-Q |
| 3 | https://www.cnbc.com/2025/12/02/okta-q3-earnings-report-2026.html | 2025-12-02 | Q3 FY26 |
| 3 | https://www.fool.com/earnings/call-transcripts/2026/08/31/okta-okta-q2-2027-earnings-call-transcript/ | 2026-08-31 | Q2 書き起こし(第三者) |
| 3 | https://www.investing.com/news/transcripts/okta-at-oktane-call-2026-investor-summit-betting-on-agentic-ai-93CH-4913776 | 2026-09 | Oktane 投資家説明会 |
| 3 | https://finance.yahoo.com/markets/stocks/articles/morgan-stanley-resets-okta-stock-192343050.html | 2026-09-29 | Morgan Stanley |
| 3 | https://www.gurufocus.com/news/8896279/okta-downgraded-by-mizuho-price-target-raised-to-125 | 2026-06-02 | Mizuho |
| 3 | https://www.tipranks.com/stocks/okta/forecast | 2026-09 | 目標株価の集計。単独出典 |
| 3 | https://futurumgroup.com/insights/okta-q2-fy-2027-earnings-beat-and-raise-on-core-identity-strength/ | 2026-08 | Futurum Group |
| 3 | https://www.fool.com/investing/2026/03/08/why-oktas-shares-tumbled-14-last-month/ | 2026-03-08 | 2月の下落 |
| 4 | https://seekingalpha.com/article/4952045-okta-the-cybersecurity-sector-is-overheated-downgrade | 2026-10-05 | 個人寄稿者 |
| 4 | https://www.peerspot.com/products/comparisons/microsoft-entra-id_vs_okta-platform_vs_ping-identity-platform | 2026-08 | レビューサイト |

## 9. 残りの欠損と、再開用の検索計画(優先順)

次の検索予算が使える場合の優先項目。

1. **Q2 FY27 書き起こし全文(会社IR の PDF)の質疑応答**: アナリスト名と質問・回答の逐語、シート数・価格・Entra に関する発言、新製品の寄与の金額。
2. **2023年のサポートシステム侵害の経緯、訴訟の帰結、Secure Identity Commitment の実施状況**(A-5、G)。
3. **過去のガイダンスの達成履歴**: FY2024・FY2025 の期初ガイダンスと実績。
4. **中期目標**: 過去の Investor Day(2024〜2025)の FY2028 以降の目標。Oktane 2026 の書き起こしの原文。
5. **自社株買い**: 承認枠・実施額・残枠。
6. **C の追加**: Okta・Auth0 の価格表の改定、求人動向、IAM 市場規模の統計、Microsoft Entra Agent ID、SailPoint・Ping Identity・CrowdStrike の開示。
7. **空売りレポート、経営陣の交代、取締役会の刷新の内容**。
8. **2026-10-09 の終値**(別担当の価格データで補う)。
