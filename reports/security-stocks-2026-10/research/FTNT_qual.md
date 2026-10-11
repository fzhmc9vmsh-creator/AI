# Fortinet(FTNT)定性調査 一次整理(Phase 1・部分完了)

- 評価基準日: 2026-10-11 / 決算期末: 12月31日 / 取得日: 2026-10-11(すべての出典の取得日)
- 担当: Sonnet(調査)。評価・投資判断は行わない。事実・出典・「なぜ重要か」の注記のみ。

## 0. 調査状況の宣言(最初に読むこと)

**この調査は途中で止まっている。** WebSearch の予算(1ターン200回、全エージェント共有)が上限に達し、
本調査で成功した検索は **4件だけ**だった(Q2 2026 決算、Q2 2026 説明会、Q1 2026 説明会、Q4 2025 決算)。
指示では「検索予算を回避する手段を取らない」ことになっているため、curl 等の迂回はしていない。

| 節 | 取得状況 |
|---|---|
| A-1 経営陣の発言 | 部分(2026 Q1・Q2 の断片のみ。2025 Q3・Q4 の発言、Investor Day は欠損) |
| A-2 数値目標 | 部分(2026年のガイダンスのみ。中期目標・SASE/SecOps 目標は欠損) |
| A-3 ピース一覧 | 部分(SP6 の Intel 協業、Moody's 格上げのみ。更新サイクル規模・買収・capex・自社株買いは欠損) |
| A-4 ガイダンス達成状況 | 部分(2025年通期の billings のみ。2023〜2024年の経緯は欠損) |
| A-5 経営陣・報酬 | 部分(CFO・COO の氏名のみ。経歴・報酬 KPI・交代は欠損) |
| B 市場の仮説 | ほぼ欠損(Q1後の株価反応1件が単独出典で得られただけ) |
| C スカットルバット | 欠損(0件。最低3件の要件は未達) |
| D 競争と業界構造 | 欠損 |
| E 異常値の候補 | 取得済み数値から5候補を作成(要件の3つは満たす。ただし裏付けの深掘りは未了) |
| F 条件9 | 部分(SP6 協業、「AI-driven」の発言、AI対応製品数のみ。AIデータセンター需要は欠損) |
| G リスク事象 | 欠損 |

**読み手への注意**
1. 以下の数値はすべて「検索結果の要約文」を経由したもので、**会社IRの原文(PDF/HTML)そのものは読めていない**。
   会社IRのURLは確認できているが、中身の確認は要追加調査。
2. 検索要約には AI 生成の要約サイト(Stock Taper、Bullfincher 等)が含まれる。これらは Tier 4 の単独出典として扱う。
3. 検索ツール自身が「出典間で数値が食い違う」と警告したものは §H の食い違い表に分けた。
4. 末尾の §I に、予算が回復したときにそのまま実行できる検索クエリ(優先順)を置いた。

### 用語の一言定義(初出)
- **billings(請求額)**: 売上+繰延収益の増減。期間契約(サービス)を前払いで請求した分も含むため、将来売上の先行指標になる。
- **繰延収益**: 先に請求・入金したが、まだ売上に計上していないサービス契約の残高。
- **non-GAAP**: 株式報酬・買収無形資産の償却などを除いた会社独自定義の利益。GAAP は米国会計基準の利益。
- **FCF(フリーキャッシュフロー)**: 営業キャッシュフロー − 設備投資。
- **ASIC**: 特定用途向けに設計した半導体。Fortinet は自社設計のセキュリティ専用チップ(FortiASIC、世代名 SP5・SP6 等)をファイアウォールに載せる。
- **FortiOS**: Fortinet の製品群を貫く単一の基本ソフト。
- **SASE(サシー)**: ネットワークとセキュリティ機能をクラウド経由で一体提供する方式。SD-WAN(拠点間回線の制御)と SSE(クラウド型セキュリティ)の組み合わせ。Fortinet は「Unified SASE」と呼ぶ。
- **SecOps**: セキュリティ運用(検知・調査・対応)。Fortinet では FortiSIEM、FortiXDR 等の「AI-driven security operations」。
- **OT**: 工場・プラント等の制御系の機器とネットワーク。
- **ガイダンス**: 会社が四半期・通期について事前に出す売上・利益等の見通し。
- **Tier**: 情報源の格付け。Tier 1=会社開示、2=公的統計、3=主要報道・アナリスト、4=ブログ・SNS・自動要約。

---

## A. 経営陣シナリオの一次情報

### A-1. 直近の決算説明会での経営陣の発言(取得できた範囲)

**取得できた発言は断片のみで、シナリオの骨格を語る全文は欠損。** 以下は検索要約中の引用である(和訳が主、原文は括弧)。

| 時期 | 話者 | 発言(和訳) | 骨格のどの部分か | 出典 / Tier |
|---|---|---|---|---|
| 2026 Q2(2026-07-29) | Ken Xie(創業者・会長・CEO) | 「第2四半期は極めて良い結果で、大変満足している」。長期の成長は「AI主導のセキュリティ需要」と、「統合され高速化された SASE ファイアウォール基盤」に結びつけた(原文の語句: "AI-driven security demand", "integrated and accelerated SASE firewall platform solution") | AI需要+SASEと機器の一体化 | [Allmind(説明会の冒頭発言抜粋)](https://allmind.ai/earnings/event/2937992) / Tier 4(要約サイト) |
| 2026 Q2 | Ken Xie | 国・地域の主権要件を満たす「ソブリンSASE」を、クラウド専用の方式よりはるかに大きな機会になり得ると位置づけた | SASE(主権・ローカル運用) | [Stock Taper の自動要約](https://stocktaper.com/earningsCallSummary/FTNT/2026/Q2) / Tier 4・単独出典・要原文確認 |
| 2026 Q1(2026-05-06) | Ken Xie | SASE ファイアウォールは、中核機能を単一のOSに native に統合することで「複雑さを大きく減らす」(原文: "significantly reduce[s] complexity")。Unified SASE は現在 billings の「約25%」(原文: "about 25% of billing right now") | FortiOS単一OSによる統合、SASEの比重 | [検索要約(Insider Monkey 等の Q1 転載)](https://www.insidermonkey.com/blog/fortinet-inc-nasdaqftnt-q1-2026-earnings-call-transcript-1756043/) / Tier 3 |
| 2026 Q1 | Ken Xie | セキュリティ運用(SecOps)の billings は23%増。「20を超えるAI対応ソリューション」を背景に、顧客のベンダー統合・運用簡素化が進んでいる | SecOps、AI(FortiAI) | 同上 / Tier 3 |
| 2026 Q1 | Ken Xie | 同日、新ファイアウォール FortiGate 3500G と 400G を発表。従来世代より性能が大きく向上 | 自社ASICによる価格性能、更新サイクル | 同上 / Tier 3 |
| 2026 Q1 | Christiane Ohlgart(CFO) | 「SD-WAN と SASE のサービス束(バンドル)を新たに導入し、採用を広げ、時間をかけてサービス売上を支える」 | サービス売上の底上げ | 同上 / Tier 3 |
| 2026 Q1 | 経営陣 | OT(制御系)セキュリティの billings が70%超の伸び。Secure networking の billings は32%増 | OT、ファイアウォール更新 | 同上 / Tier 3 |

- 説明会の出席者(2026 Q2): Ken Xie(創業者・会長・CEO)、CFO Christiane Ohlgart、COO John Whittle
  ([Allmind 要約より](https://allmind.ai/earnings/event/2937992) / Tier 4)。Michael Xie(CTO)の発言は未取得。
- **欠損**: 2025 Q3・2025 Q4 の説明会の発言。直近の Investor Day / アナリスト説明会の発言。ファイアウォール更新サイクルを経営陣がどう語ったか。
  転記の場所は検索結果に出ている(ROIC.ai、Bullfincher、Insider Monkey、Seeking Alpha に全文転記あり)が、全文は読めていない:
  [ROIC.ai](https://www.roic.ai/quote/FTNT/transcripts)、[Bullfincher Q2](https://bullfincher.io/companies/fortinet/earnings-call/fy2026-q2)、[Bullfincher Q1](https://bullfincher.io/companies/fortinet/earnings-call/fy2026-q1)

**なぜ重要か**: シナリオ骨格(機器の価格性能 → 単一OS統合 → SASE/SecOps への拡張)のうち、
「機器が先に伸び、サービスは遅れて追随する」構造(§E-2)を経営陣がどう説明するかが、成長の持続性の判断軸になる。

### A-2. 数値目標とその定義・期限

**取得できたのは年次ガイダンスのみ。中期目標(売上・営業利益率)、SASE・SecOps の目標は欠損。**

| 項目 | 内容 | 出典 / Tier | 状態 |
|---|---|---|---|
| FY2026 売上ガイダンス(2026-07-29 時点) | 前年比19%増に引き上げ。レンジ 80億2,000万〜81億8,000万ドル | [会社IRのプレスリリース(静的ファイル)](https://fortinet.gcs-web.com/static-files/e4ffcc79-194e-4ca3-9a69-8a51bd0a6314)の要約を [mfn.se](https://mfn.se/one/a/fortinet/fortinet-reports-strong-second-quarter-2026-financial-results-c7dd36df) 経由で確認 / Tier 1(原文未読) | 取得 |
| 2026 Q3 売上ガイダンス | 20億1,000万〜21億ドル | 同上 | 取得 |
| FY2026 billings ガイダンス(2026-02-05 時点) | 84億〜86億ドル(前年比約13%増の中央値)。粗利率80〜81%、営業利益率30〜32%を目標とする、という要約 | [Vectorshift の説明会要約](https://vectorshift.ai/research/companies/fortinet/earnings/2025-q4) / Tier 4・**単独出典**。正式な根拠は [8-K 別添99.1](https://www.sec.gov/Archives/edgar/data/1262039/000126203926000003/ftntq4-2025ex991.htm)(未読)。営業利益率が GAAP か non-GAAP かは未確定 | 部分 |
| 中期目標・SASE/SecOps 目標 | - | - | **欠損** |

**なぜ重要か**: 年初の billings ガイダンス(約13%増)と、実績の Q1 +31%・Q2 +33%(§E)の乖離が大きい。
ガイダンスが保守的だったのか、年中に需要が変わったのかで、残りの期の見方が変わる。

### A-3. ピース一覧

| ピース | 目的(会社の説明) | 発表日 | 規模・進捗の数値 | 出典 / Tier | 状態 |
|---|---|---|---|---|---|
| 次世代チップ SP6(Intel と協業) | Fortinet 固有のセキュリティ処理チップの設計力と、Intel の先端設計・パッケージ・製造力を組み合わせる(原文: "combining Fortinet's proprietary, purpose-built security processor expertise with Intel's advanced design, development, packaging, and manufacturing capabilities") | 2026-07-29(Q2決算と同日に発表) | 規模・時期・製造委託先の詳細は欠損 | 会社IRの要約 [mfn.se](https://mfn.se/one/a/fortinet/fortinet-reports-strong-second-quarter-2026-financial-results-c7dd36df) / Tier 1(原文未読) | 部分 |
| 新ファイアウォール FortiGate 3500G / 400G | 従来世代より性能を大きく向上 | 2026-05-06 | 性能値は欠損 | Q1説明会の要約 / Tier 3 | 部分 |
| SD-WAN+SASE のサービス束 | 採用拡大とサービス売上の底上げ | 2026-05(Q1説明会) | 数値は欠損 | 同上 | 部分 |
| 信用格付け | Moody's が無担保シニア債を Baa1 から A3 に引き上げ。「公開サイバーセキュリティ企業で最高の格付け」と会社が表現 | 2026-07-29 | A3 | 会社IRの要約 / Tier 1(原文未読) | 取得 |
| ファイアウォール更新サイクル(2026年にサポート終了する機種の規模) | - | - | - | - | **欠損** |
| FortiASIC の世代(SP5 等)の詳細 | - | - | - | - | **欠損** |
| 買収(Lacework、Next DLP 等) | - | - | - | - | **欠損** |
| データセンター・本社の不動産投資(capex) | - | - | - | - | **欠損** |
| 自社株買い | - | - | - | - | **欠損** |
| SASE・SecOps 製品の個別開示 | 2026 Q1: SASE が billings の約25%、SecOps 23%増(§A-1) | - | - | Tier 3 | 部分 |

### A-4. 過去3年のガイダンス達成状況

- 取得できたのは **2025年通期の billings のみ**: 実績は **75億5,000万ドル(前年比16%増)**。
  FY2025 の FCF は 22億1,000万ドル。第4四半期 billings は23億7,000万ドル(18%増)で、会社のガイダンスの上限を上回った
  ([MarketBeat/報道の要約](https://www.marketbeat.com/instant-alerts/fortinet-q4-earnings-call-highlights-2026-02-05/?.tsrc=rss)、
  [Barchart に転載の会社プレスリリース](https://www.barchart.com/story/news/57297/fortinet-reports-strong-fourth-quarter-and-full-year-2025-financial-results) / Tier 1 転載、原文未読)。
- 期中の見通し: Seeking Alpha の見出しに「2025年の billings の見通しを74億7,500万ドルに引き上げ」とある
  ([見出しのみ](https://seekingalpha.com/news/4480880-fortinet-raises-2025-billings-outlook-to-7_475b-while-advancing-sase-ai-and-cloud-innovation) / Tier 3)。
  日付と、74億7,500万ドルがレンジの中央値か上限かは未確認。これが事実なら、実績75億5,000万ドルはこの見通しを約1%上回る。
- 2026年: 期初の billings ガイダンス84〜86億ドル(単独出典、§A-2)に対し、上半期の実績は Q1 20億9,000万ドル(単独出典)+Q2 23億7,000万ドル=約44億6,000万ドル(Q1は食い違いあり、§H)。通期ガイダンスの再提示は未取得。
- **欠損**: 2023〜2024年の在庫調整・billings 減速期の経緯と経営陣の説明、過去の約束とその結果。最低3年分の期初 vs 実績の表は作れていない。

### A-5. 経営陣の経歴・在任・報酬

- 取得: Ken Xie は創業者・会長・CEO([Allmind 要約](https://allmind.ai/earnings/event/2937992) / Tier 4)。CFO は Christiane Ohlgart、COO は John Whittle(同上)。
- **欠損**: 経歴の詳細、Michael Xie(CTO)の現職、報酬制度の KPI(委任状説明書 DEF 14A)、経営陣の交代、
  CFO・COO の就任時期。株式報酬の KPI が「総額」か「1株当たり」かは未確認。

---

## B. 市場の仮説の出典

**ほぼ欠損。** 取得できたのは次の1件のみ(単独出典)。

| 事実 | 出典 / Tier | 状態 |
|---|---|---|
| Q1 2026 決算(2026-05-06)を受けて株価が約20%上昇した、と報じる記事がある | 検索要約が「ある集計サイト」の記述として示したもので、**サイト名・URLを特定できていない**(Q1検索の結果リストの一つ)。Tier 3〜4・**単独出典**・日付と終値は未確認 | 要確認(使用不可の水準) |
| Q1説明会でアナリストが注目した項目: 3500G/400G ハードウェア群の展開 | Q1説明会の要約 / Tier 3 | 部分 |

- B-1(アナリストの繰り返した質問)、B-2(強気・弱気の主要論点、証券会社・アナリスト名・目標株価、「ハードウェア企業=景気循環株」の見方の有無)、
  B-3(空売り・著名な弱気論者の主張と会社の反論)、B-4(報道のナラティブ、2026年の「AIによるソフトウェア代替」懸念のセキュリティ株への影響)、
  B-5(直近1年の株価の主要イベント、2025年8月の決算後の急落とその理由): **すべて欠損**。
- **なぜ重要か**: 本メソッド(business-core §4)は「市場の仮説の特定」から差分を宣言する。ここが空のままでは差分を出典付きで宣言できない。
  最優先で再開する項目(§I の 1〜6)。

---

## C. 一次情報(スカットルバット)

**0件(要件は最低3件)。** 価格表・値上げ、Gartner Peer Insights、Gartner マジック・クアドラント、IDC 出荷シェア、
チャネルパートナーの声、半導体の調達・在庫、競合(PANW・Cisco・Check Point)の開示、業界統計(ファイアウォール・SD-WAN・OT 市場規模)は、
いずれも検索できていない。構造仮説の裏付けは未了であり、研究プロトコル §7 の「最低2件」を満たしていない。
これは**既知の制約**として分析報告書に記載が必要。

---

## D. 競争と業界の構造

**欠損。** ファイアウォール市場の成熟度、SASE への移行が既存機器需要を食う程度、価格競争、中小企業向けの強さ、セキュリティ予算の動向は未取得。

取得した事実から言えること(事実のみ):
- 2026 Q1 に Secure networking billings が32%増、Q2 に製品売上が52%増。「機器需要が弱い」「SASE が機器を食う」という見方と並べると、
  直近2四半期の数字は逆向きに見える(§E-1)。ただし、これが更新需要・価格・案件の特殊要因のどれなのかは、現時点で出典がない。

---

## E. 異常値の候補(市場のナラティブと合わない数字)

使用した数値は、いずれも検索要約経由の会社IR(Tier 1・原文未読)または報道(Tier 3)。「逆算」は自分で計算した値。

| # | 異常値の候補 | 数値と出典 | 問い(答えは未調査) |
|---|---|---|---|
| E-1 | **製品売上の急加速** | Q2 2026 の製品売上は7億7,300万ドル、**前年比52%増**([会社IR要約 mfn.se](https://mfn.se/one/a/fortinet/fortinet-reports-strong-second-quarter-2026-financial-results-c7dd36df))。前年同期は逆算で約5億900万ドル。Q1 2026 は Secure networking billings 32%増、OT billings 70%超増 | 「ハードウェア企業は成熟」という見方に反して、なぜ機器が52%増なのか。更新需要か、価格か、AI/データセンター案件か、前年の基準が低いだけか |
| E-2 | **売上・billings の加速**と、サービス売上の安定のずれ | 売上成長: Q4 2025 +15% → Q1 2026 +20% → Q2 2026 +26%。billings: Q4 2025 +18% → Q1 2026 +31%(単独出典)→ Q2 2026 +33%。一方サービス売上は Q2 +14%(12億7,000万ドル、[Nasdaq の説明会要約](https://www.nasdaq.com/articles/fortinet-q2-earnings-call-highlights) / Tier 3) | 機器の販売が先に立ち、サービス売上(繰延収益から数年かけて計上)が遅れて追随する構造なのか。それとも新規のサービス契約が少ないのか |
| E-3 | **営業利益率の高さと年初ガイダンスの乖離** | Q2 2026 non-GAAP 営業利益率38%・GAAP 34%、Q1 は non-GAAP 36%・GAAP 31%。年初の通期目標は営業利益率30〜32%(単独出典・GAAP/non-GAAPは未確定、[Vectorshift](https://vectorshift.ai/research/companies/fortinet/earnings/2025-q4)) | なぜ実績がガイダンスを大きく上回るのか。製品比率の上昇か、粗利率か、部品コスト(メモリ等)の影響が想定より小さいのか |
| E-4 | **FCF が non-GAAP 営業利益を上回る** | Q2 2026 FCF 9億6,600万ドル(営業CF 10億4,000万ドル)。Q2 の non-GAAP 営業利益は概算で約7億8,000万ドル(売上20億5,000万ドル×38%、逆算)。FCF/営業利益は約1.2倍。Q1 FCF 10億1,000万ドル(単独出典)と合わせた上半期 FCF は約19億8,000万ドルで、FY2025 通期の22億1,000万ドルに迫る | なぜ現金が利益を上回るのか。繰延収益の前受け、税の時期、設備投資の時期のどれか。持続するのか |
| E-5 | **通期ガイダンスと半期実績の関係** | FY2026 売上ガイダンス中央値は約81億ドル。H1(Q1 約18億5,000万ドル(単独出典)+Q2 約20億5,000万ドル)約39億ドルを引くと H2 は約42億ドル。Q3 ガイダンス中央値は約20億5,500万ドルで Q2 実績とほぼ同水準(逆算) | 第3四半期ガイダンスが前四半期とほぼ横ばいなのは、保守的な設定か、需要の一時的な前倒しの反動を織り込んだものか |

---

## F. 条件9(AIの停めない運用)に関わる事実

| 事実 | 出典 / Tier | 状態 |
|---|---|---|
| Ken Xie が Q2 2026 説明会で長期成長を「AI主導のセキュリティ需要」と結びつけた | [Allmind](https://allmind.ai/earnings/event/2937992) / Tier 4 | 部分 |
| SecOps 製品は「20を超えるAI対応ソリューション」(2026 Q1)。SecOps billings 23%増 | Q1説明会の要約 / Tier 3 | 取得(売上は非開示の可能性) |
| Intel との協業で次世代セキュリティ処理チップ SP6 を開発 | 会社IR要約 / Tier 1 | 取得(AI処理との関係は未確認) |
| AIを守る製品・AIデータセンター向け高速ファイアウォールの需要、AI関連の売上開示値 | - | **欠損** |

---

## G. リスク事象

**欠損。** 自社製品の重大脆弱性(FortiOS 等の CVE)の頻度と顧客への影響、訴訟、規制、会計上の論点、経営陣の株式売却は未取得。
取得できた財務面の事実は、Moody's による格上げ(Baa1 → A3、2026-07-29、会社IR要約)のみ。

---

## H. 出典間の食い違い・未確定事項

| 項目 | 食い違い | 暫定扱い |
|---|---|---|
| Q1 2026 売上 | 18億5,000万ドル(前年比20%増)と報じる記事がある([securitymea](https://securitymea.com/2026/05/19/fortinet-q1-revenue-jumps-20-year-on-year-to-1-85-billion/))。会社IRの原文は未確認 | 単独出典。20億9,000万ドルは billings の値とみられ、売上と混同しない |
| Q1 2026 billings | 20億9,000万ドル(31%増、ガイダンス上限超え)とする集計サイトがある(サイト名は検索要約で特定できず) | 単独出典。会社IRで確認が必要 |
| Q2 2026 non-GAAP EPS | 検索要約の表記は0.901ドル(小数3桁) | IR原文で桁を確認 |
| FY2026 営業利益率目標 | 30〜32%(GAAP/non-GAAP不明) | 単独出典 |

## I. 予算回復後に実行する検索クエリ(優先順)

1. `Fortinet stock plunge August 2025 earnings firewall refresh guidance` / `FTNT shares fall Q2 2025 billings`
2. `Fortinet analyst price target raised July 2026` / `Fortinet downgrade 2026` / `FTNT Morgan Stanley Goldman Wells Fargo price target`
3. `Fortinet earnings call Q&A analyst questions Q2 2026 firewall refresh memory DRAM pricing`
4. `Fortinet short seller report` / `Fortinet bear case hardware cyclical`
5. `software stocks AI disruption 2026 cybersecurity stocks Fortinet` / `cybersecurity stocks selloff AI agents 2026`
6. `Fortinet stock jump May 2026 earnings` / `Fortinet 52-week high 2026`
7. `Fortinet firewall refresh cycle 2026 end of support installed base` / `Fortinet 2026 refresh 8 million units`(数値は検索で確認)
8. `Fortinet Investor Day analyst day long-term targets operating margin` / `Fortinet 2025 analyst day`
9. `Fortinet Q3 2025 earnings call transcript` / `Fortinet Q4 2025 earnings call transcript Ken Xie`
10. `Fortinet Lacework acquisition Next DLP acquisition` / `Fortinet SP5 SP6 FortiASIC Intel`
11. `Fortinet share repurchase authorization 2026` / `Fortinet capex data center headquarters Sunnyvale`
12. `Fortinet proxy statement 2026 executive compensation performance metrics`
13. `Gartner Magic Quadrant network firewall 2025 Fortinet` / `Gartner Magic Quadrant SD-WAN 2025` / `Gartner Magic Quadrant single-vendor SASE 2025`
14. `IDC firewall market share Q2 2026 Fortinet Palo Alto` / `Dell'Oro network security appliance market 2026`
15. `FortiGate price increase 2026` / `Fortinet distributor Exclusive Networks Ingram Micro Fortinet comments`
16. `Fortinet FortiOS vulnerability CISA KEV 2026` / `Fortinet class action lawsuit` / `Fortinet insider selling Ken Xie 2026`
17. `Palo Alto Networks firewall competition Fortinet earnings call 2026` / `Cisco firewall refresh Fortinet`
18. `Fortinet AI data center firewall demand` / `FortiAI` / `Fortinet 2023 inventory adjustment billings miss Q3 2023`
19. 会社IR原文: `fortinet.gcs-web.com` と `investor.fortinet.com` の2026 Q1・Q2・2025 Q3・Q4 プレスリリース(allowed_domains 指定)

## J. 出典一覧(本ファイルで使ったもの。取得日はすべて 2026-10-11)

| 出典 | 日付 | Tier | 読了状況 |
|---|---|---|---|
| [Fortinet IR Q2 2026 プレスリリース(静的ファイル)](https://fortinet.gcs-web.com/static-files/e4ffcc79-194e-4ca3-9a69-8a51bd0a6314) | 2026-07-29 | 1 | 検索要約のみ(原文未読) |
| [mfn.se(プレスリリース配信)](https://mfn.se/one/a/fortinet/fortinet-reports-strong-second-quarter-2026-financial-results-c7dd36df) | 2026-07-29 | 1(配信) | 検索要約のみ |
| [Nasdaq: Q2 earnings call highlights](https://www.nasdaq.com/articles/fortinet-q2-earnings-call-highlights) | 2026-07 | 3 | 検索要約のみ |
| [Allmind: Q2 2026 説明会](https://allmind.ai/earnings/event/2937992) | 2026-07-29 | 4 | 検索要約のみ |
| [Stock Taper: Q2 2026](https://stocktaper.com/earningsCallSummary/FTNT/2026/Q2) | 2026-07 | 4(自動要約) | 検索要約のみ |
| [Insider Monkey: Q1 2026 トランスクリプト](https://www.insidermonkey.com/blog/fortinet-inc-nasdaqftnt-q1-2026-earnings-call-transcript-1756043/) | 2026-05-06 | 3 | 検索要約のみ |
| [securitymea: Q1 2026](https://securitymea.com/2026/05/19/fortinet-q1-revenue-jumps-20-year-on-year-to-1-85-billion/) | 2026-05-19 | 3 | 検索要約のみ |
| [Barchart: Q4 2025 プレスリリース転載](https://www.barchart.com/story/news/57297/fortinet-reports-strong-fourth-quarter-and-full-year-2025-financial-results) | 2026-02-05 | 1(転載) | 検索要約のみ |
| [SEC 8-K 別添99.1(Q4 2025)](https://www.sec.gov/Archives/edgar/data/1262039/000126203926000003/ftntq4-2025ex991.htm) | 2026-02-05 | 1 | URL確認のみ |
| [Vectorshift: Q4 2025 要約](https://vectorshift.ai/research/companies/fortinet/earnings/2025-q4) | 2026-02 | 4 | 検索要約のみ |
| [MarketBeat: Q4 call highlights](https://www.marketbeat.com/instant-alerts/fortinet-q4-earnings-call-highlights-2026-02-05/?.tsrc=rss) | 2026-02-05 | 3 | 検索要約のみ |
| [Seeking Alpha 見出し: 2025 billings 見通し引き上げ](https://seekingalpha.com/news/4480880-fortinet-raises-2025-billings-outlook-to-7_475b-while-advancing-sase-ai-and-cloud-innovation) | 日付未確認 | 3 | 見出しのみ |
