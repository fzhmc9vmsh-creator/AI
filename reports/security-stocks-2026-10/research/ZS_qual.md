# Zscaler(ZS)定性調査 一次整理(再開版・検索18回で打ち切り)

評価基準日: 2026-10-11 / 決算期末: 7月31日(FY2026 = 2025年8月〜2026年7月) / 作成: Sonnet(調査担当)

## 0. 本書の状態と読み方

- 初版(検索2本で上限到達)を、再開後の18回の WebSearch で全面更新した。**取れたもの**: 決算後の論調、強気・弱気の証券会社と目標株価、株価の主要イベント、Investor Day(2026-10-06)の中期目標、買収の一覧、営業トップの交代、ガイダンス、訴訟の状況、Gartner の位置。**取れなかったもの**は各節に「欠損」と書いた(末尾 H に一覧)。
- 数値別担当の領域(四半期業績・KPI)は追っていない。ここに出る数値は、定性の文脈を理解するために必要な範囲のみ。
- **すべての出典は検索ツールの要約文経由**で、8-K・IR・トランスクリプトの本文は直接読んでいない。Tier 1 と書いても「本文未確認」である。逐語の引用は、検索結果が引用符つきで返した断片に限り、和訳を主に原文を括弧で添えた。それ以外は要旨(言い換え)と明記した。
- **初版からの訂正**: (1) 初版は「CFO の氏名不明」としたが、CFO は Kevin Rubin(2025-05 就任)。(2) 初版の「株価上昇を示唆」は誤りに近く、Q4 決算翌日(2026-09-04)の株価は約 4% 下落した(B-5)。(3) 依頼文の「ARR 50 億ドル目標」は確認できなかった。実際の目標は FY2031 に ARR 80 億ドル超(基本シナリオ)・100 億ドル(上振れ)(A-2)。

用語(初出の定義): **ARR** = 年間経常収益(契約済みの継続収益の年換算額)。**NNARR** = 純新規 ARR(期中に純増した ARR)。**GAAP / non-GAAP** = 米国会計基準 / 株式報酬などを除外した会社独自の指標。**FCF** = フリーキャッシュフロー(営業CF − 設備投資)。**capex** = 設備投資。**SSE** = セキュリティ・サービス・エッジ(クラウド経由でウェブ・SaaS・社内アプリの通信を検査する層)。**SASE** = SSE にネットワーク機能を合わせた枠組み。**SOC** = セキュリティ運用センター。**MDR** = 検知・対応の運用代行サービス。**SBC** = 株式報酬費用。**PSU** = 業績連動型の株式報酬。**TCV** = 契約総額。**ACV** = 年換算の契約額。

---

## 要点(Opus 向け、事実のみ)

1. 2026-05-27、Q3 FY2026 決算で株価が 1 日に 31.5% 下落して 126.41 ドル。決算自体は予想超えで、原因は FY2027 の ARR 成長率ガイダンスが 16〜17% と市場予想を下回ったこと、営業幹部 2 名の退社、FCF マージン見通しの引き下げ(capex 増)。背景に、ソフトウェア株全般への「AI による事業モデル破壊」懸念がある。
2. 株価はその後 213 ドル前後(2026-10-06〜07 頃)まで戻した。Q4 決算(2026-09-03)で FY2027 ガイダンスは変わらず(売上成長 16.6〜17.5%)、Investor Day(2026-10-06)で FY2031 の ARR 目標を提示。上昇の理由は、検索結果の範囲では「AI セキュリティの需要」と「目標株価の相次ぐ引き上げ」。
3. 経営陣のシナリオは、ゼロトラスト(通信を常に検証する設計)の本業に、①AI を守る製品(Security for AI)、②Red Canary を軸にした AI 運用(Agentic SecOps)、③席数に依存しない課金の拡大、を重ねて ARR を成長させるというもの。ただし AI 関連の ARR は FY2026 末で約 7,000 万ドルと小さい。

---

## A. 経営陣シナリオの一次情報

### A-1. 経営陣の発言

| 時点 | 発言者 | 内容(和訳。逐語は括弧) | 出典・Tier | なぜ重要か |
|---|---|---|---|---|
| Q3 FY2026 決算リリース(2026-05-26) | Jay Chaudhry(CEO・会長・創業者) | 「当社の取り組みが響いていることを、新規顧客の獲得と既存顧客の拡張が示している。長期の成長には十分な余地があると見ている」(原文: "Our results demonstrate that our approach is resonating as we attract new customers and expand with our existing customers, and we see ample runway for long-term growth.") | 8-K https://www.sec.gov/Archives/edgar/data/0001713683/000171368326000095/zs-04302026_991.htm の内容を引いた報道 / Tier 1(要約経由) | 株価が 31% 下落した日の公式の立場。「新規顧客が足りない」という懸念への会社の反論になっている |
| Q3 決算説明会(2026-05-26) | CFO Kevin Rubin | FY2027 のガイダンスは、営業幹部の交代期の混乱を見込んだ「慎重なアプローチ(prudent approach)」である | https://finance.yahoo.com/markets/stocks/articles/zscaler-stock-plunges-weak-guidance-163702184.html ほか / Tier 3 | ガイダンスの減速を「保守性」と説明する会社側の論理。実際に保守的だったかは FY2027 の実績で検証される |
| Q3 決算説明会 | CEO | AI 需要の影響は Q4 には織り込まず、FY2027 に表れると見る(要旨) | https://www.investing.com/news/transcripts/earnings-call-transcript-zscaler-beats-q3-2026-forecasts-stock-rises-93CH-4710950 / Tier 3(話者ラベルが乱れた転載、要照合) | AI 需要の収益化は FY2027 以降という会社自身の時間軸 |
| Q4 FY2026 決算説明会(2026-09-03) | CEO | AI エージェント製品について「非常に強気(very bullish)」で、長期的により大きな ARR の機会になりうると見る | https://theoutpost.ai/news-story/zscaler-beats-q4-earnings-with-898-m-revenue-as-ai-security-demand-surges-25-30461/(CNBC 由来の転載) / Tier 3(**単独出典**) | 新エンジンを第 2 の柱と位置づける発言 |
| 同上 | CEO | 「Zero Trust Everywhere が当社の販売の多くを牽引している」(原文: "Zero Trust Everywhere has been driving a lot of our sales.") | https://finance.yahoo.com/quote/ZS/earnings/ZS-Q4-2026-earnings_call-680670.html の抜粋 / Tier 3(話者名に誤記のある転載。**要照合**) | Zero Trust Everywhere(ZS が掲げる、ユーザー通信から支店・クラウド・工場設備まで拡張する戦略)が営業の主力になっているという会社側の主張 |
| 同上 | CEO | 営業を「案件主導」から「アカウント(顧客単位)主導」に切り替えた。Q4 の結果はその変更が機能していることを示す(要旨) | https://www.benzinga.com/news/26/09/61619149/zscaler-reports-q4-2026-results-full-earnings-call-transcript / Tier 3 | 2026 年の営業体制見直しの意図。営業幹部の離職とセットで評価すべき点 |
| 同上 | CEO | AI エージェントは、データの持ち出し・データ悪用・過剰な権限によるデータアクセスという新しい種類のリスクをもたらす(要旨) | Yahoo の同トランスクリプト抜粋 / Tier 3 | データセキュリティと AI 保護を結びつける論理 |
| 同上 | CEO / CFO | 人員の約 3% を削減する再編を行い、AI への投資に資源を振り向ける。浮いた資金は、専門営業チーム、地域の営業網、小規模な大企業向け営業に充てる(要旨) | https://www.bankinfosecurity.com/zscaler-to-lay-off-3-staff-as-shifts-spend-to-sales-a-32746 / Tier 3 | 削減の目的は「AI による自動化」ではなく「営業への再配分」と会社が説明している点が事実 |
| 同上 | CFO Rubin | FY2026 は 4 年で最良の営業生産性。FY2027 のガイダンスは営業トップ交代に要する時間と、統合 SecOps 製品の浸透速度を考慮。解約(churn)は高めで、Red Canary は FY2027 に単独の NNARR 貢献を見込まない(要旨) | https://cryptobriefing.com/zscaler-arr-growth-fiscal-2027-guidance-slows/ ほか / Tier 3 | 弱気論点(営業の混乱、解約、買収の貢献の薄さ)に対する会社側の認識 |

### A-2. 数値目標(定義・期限)

| 目標 | 内容 | 出典・Tier | 注記 |
|---|---|---|---|
| FY2031 の ARR | 基本シナリオで 80 億ドル超。エージェント型 AI の急速な普及で最大約 20 億ドルの上振れがあり、100 億ドルを目標とする | 会社の Investor Day リリース(2026-10-06)https://www.zscaler.com/press/zscaler-hosts-2026-investor-day-reaffirms-first-quarter-and-fiscal-2027-guidance、https://www.marketbeat.com/instant-alerts/event-zscaler-investor-day-maps-ai-security-path-to-8b-arr-with-10b-upside-2026-10-06/ / Tier 1(リリース本文未確認)+Tier 3 | 80 億ドルへの年平均成長率は、報道では「約 17%」。筆者計算では FY2026 末 37.7 億ドルから 5 年で約 16.2%、100 億ドルは約 21.5%(要約の「約 17%」と若干ずれる。起点を 38 億ドルと丸めた差か) |
| FY2027 ガイダンス | 売上 39.08〜39.38 億ドル(前年比 +16.6〜17.5%)、ARR 43.96〜44.26 億ドル(+16.6〜17.4%)、Q1 売上 9.35〜9.39 億ドル(約 +19%)、non-GAAP 営業利益 9.24〜9.32 億ドル(営業利益率約 23%)、FCF マージン約 23.0〜23.5%、non-GAAP EPS 4.86〜4.90 ドル | 売上・ARR: https://cryptobriefing.com/zscaler-arr-growth-fiscal-2027-guidance-slows/ ほか複数。EPS: Benzinga(単独)/ Tier 3 | 売上と ARR の範囲は複数の報道で一致。**営業利益と FCF マージンは MarketBeat 経由**。Investor Day (10-06) で再確認(reaffirm)された |
| capex | FY2028 まで高水準で、その後は売上の 1 桁後半 % に向かう | MarketBeat(上記)/ Tier 3(単独) | Q3 で FY2026 の capex を「現在の価格を確定させるために前倒し」と CFO が説明した(Investing.com のトランスクリプト、要照合) |
| 長期の営業利益率・FCFマージン | **欠損。** FY2027 を超える長期の目標数値は検索結果に出なかった。Investor Day 資料本体(ir.zscaler.com)で要確認 | | |

注: 依頼文の「ARR 50 億ドル目標」は今回の検索では確認できなかった(旧目標か別の定義かは不明)。

### A-3. ピース一覧(買収・製品・営業体制・契約形態・資本政策)

| ピース | 目的(会社の説明が確認できたもの) | 発表日 | 規模 | 進捗 | 出典・Tier |
|---|---|---|---|---|---|
| Avalor | データ基盤(セキュリティデータのファブリック)。Risk360 などデータ主導の製品の土台 | 2024-03 | 10-K の現金対価 2億5,670万ドル(報道は 3.1 億・3.5 億ドルと食い違うため 10-K を採用) | 取得済み | 10-K https://www.sec.gov/Archives/edgar/data/0001713683/000171368326000157/zs-20260731.htm の要約 / Tier 1(要約経由) |
| Airgap Networks | 工場・OT(制御機器)向けのエージェント不要なネットワーク分割 | 2024-04 | 非公開 | 取得済み | 検索要約 / Tier 3 |
| Red Canary | SOC 向けの検知・対応(MDR)。Agentic SecOps(AI による運用自動化)の足場 | 2025-05(正確な日は未確認) | 発表時は現金 6.75 億ドル。FY2026 Q1 の 10-Q では現金対価の合計 6億5,140万ドル | 2025-08-01 に完了(別事業部として運営)。FY2026 末の ARR 寄与は 1.41 億ドル | https://www.zscaler.com/press/zscaler-completes-acquisition-red-canary-accelerate-innovations-agentic-ai-driven-security(Tier 1)、https://www.cybersecuritydive.com/news/zscaler-buy-red-canary/749147/(Tier 3)、10-Q https://www.sec.gov/Archives/edgar/data/1713683/000171368325000205/zs-20251031.htm |
| SPLX | AI 資産の発見とリスク評価、AI の自動レッドチーム(模擬攻撃)による脆弱性の修復。Security for AI の中核 | 2025-11 | 非公開 | 取得済み。AI のライフサイクル全体の保護を掲げる | https://www.securityweek.com/zscaler-acquires-ai-security-company-splx/(Tier 3)、https://www.techzine.eu/news/security/135977/zscaler-protects-the-entire-ai-lifecycle-after-acquiring-splx/ |
| SquareX | ブラウザのセキュリティ | 2026-02(完了 2026-02-05) | 非公開 | 完了 | https://www.securityweek.com/zscaler-acquires-browser-security-firm-squarex/amp/(Tier 3) |
| Zero Trust Everywhere | ユーザー通信から支店・クラウド・工場へ拡張する戦略。CEO は販売の牽引役と説明 | (戦略名。発表日は未取得) | 規模の開示値は**欠損** | A-1 参照 | Tier 3 |
| 営業体制の変更 | 「案件主導」から「アカウント主導」へ。2026 年に営業幹部が相次いで退社し、CRO の交代に至った(A-4) | 2026 年 | (A-4) | 進行中 | A-1、A-4 |
| 人員再編 | 約 3% の削減(8,700 人超のうち約 261 人、筆者計算)。一時費用 3,000〜3,300 万ドル(大半が FY2027 上期) | 2026-09-01 に計画を決定、09-03 に公表 | 一時費用 3,000〜3,300 万ドル | 実行中 | 8-K https://www.sec.gov/Archives/edgar/data/0001713683/000171368326000156/zs-20260901.htm の要約(Tier 1、要約経由)、https://www.bankinfosecurity.com/zscaler-to-lay-off-3-staff-as-shifts-spend-to-sales-a-32746 |
| 契約形態: Z-Flex | 非席課金の契約形態と見られる(定義は**未取得**) | — | FY2026 の Z-Flex の TCV は 17 億ドル超 | — | https://www.fool.com/earnings/call-transcripts/2026/09/09/zscaler-zs-q4-2026-earnings-call-transcript/ の要約 / Tier 3 |
| 非席課金の比率 | 従量(メーター制)の非席課金は Q3 FY2026 の新規 ACV の 30% 強、その ARR は前年比 +100% 超 | 2026-05-26 | — | — | Fool の Q3 トランスクリプト要約 https://www.fool.com/earnings/call-transcripts/2026/05/26/zscaler-zs-q3-2026-earnings-call-transcript/ / Tier 3 |
| 資本政策(転換社債・自社株買い) | **欠損(未調査)** | | | | |
| ARR 開示への切り替え | **欠損(経緯の資料は未取得)** | | | | |

### A-4. 営業トップの交代(2026 年)

- Q3 FY2026 の期中に営業幹部 2 名が退社(CRO 配下)。1 名分は社内で後任が決まっていると説明(Tier 3 要約)。
- **2026-09-24**: CRO の Mike Rich が個人的な理由で辞任。後任に Ross Tackett(それまで全世界営業の責任者)。**2026-10-01 付**。Rich は 2026-12-31 まで顧問として残り、退職金を受け取る見込み(8-K)。出典: https://www.sec.gov/Archives/edgar/data/0001713683/000171368326000193/zs-09242026_991.htm、https://www.marketscreener.com/news/zscaler-inc-chief-revenue-officer-changes-effective-october-1-2026-ce785adfdb8cfe2c(Tier 1+3)。
- 株価の反応: 一部の訴訟告知記事によると 2026-09-25 に 10.06%(21.59 ドル)下落して 193.05 ドル(Tier 4、**単独出典**)。

### A-5. 過去 3 年のガイダンス達成状況

**欠損(期初 vs 実績の表は作れていない)。** 確認できた断片のみ:
- Q3 FY2026(2026-05): 売上と non-GAAP EPS のガイダンスを引き上げたが、FY2026 の FCF マージンを 26.5〜27% から 22.8〜23.3% に引き下げた(capex の増加)。Evercore ISI の格下げの直接の理由(Tier 3、複数)。
- Q3 FY2026 の実績: non-GAAP EPS 1.08 ドル、売上 8.5 億ドル(予想超え)。
- Q4 FY2026: 売上 8億9,820万ドル、non-GAAP EPS 1.19 ドル(予想 1.08〜1.09 ドル)。
- 過去 3 年の「期初ガイダンス vs 年間実績」は FY2024・FY2025 の資料が未取得のため**欠損**。数値別担当の資料と合わせて作成すること。

### A-6. 経営陣の経歴・在任・報酬

- Jay Chaudhry: CEO・会長・創業者(2026-09-03 付リリースの肩書き)。創業者経営。経歴の詳細は**欠損**。
- CFO Kevin Rubin: 2025-05-29 に就任発表(前任 Remo Canessa)。前職は Alteryx と BetterUp の CFO。出典: https://ir.zscaler.com/news-releases/news-release-details/kevin-rubin-joins-zscaler-chief-financial-officer-drive(Tier 1)、https://www.govconwire.com/articles/kevin-rubin-zscaler-cfo(Tier 3)。
- 営業トップ: A-4。
- **報酬制度(2025 年の委任状説明書、2025-11 提出。Tier 1、要約経由)**: 年次の現金賞与は売上・請求額(billings)・non-GAAP 営業利益で原資が決まる。長期の株式報酬(PSU)は**複数年の ARR 成長目標**に連動し、対象の経営陣の PSU の目標は FY2024 の ARR の約 160% から始まる。出典: https://www.stocktitan.net/sec-filings/ZS/def-14a-zscaler-inc-definitive-proxy-statement-a67459364bf8.html(Tier 3)、https://www.sec.gov/Archives/edgar/data/1713683/000171368325000198/zs-20251121.htm。**KPI の単位は ARR 総額で、1 株当たりではない**(希薄化が目標達成の妨げにならない設計)。2026 年版の委任状説明書は未提出(通例 11 月)。
- 経営陣の株式売却: G 参照。

---

## B. 市場の仮説の出典

### B-1. 直近 2 回の決算説明会でアナリストが繰り返した質問

話者の名前は、検索結果のトランスクリプトの話者ラベルが乱れており(例: 人名の誤記)**確認できなかった**。質問の趣旨のみ記す。

| 回 | 質問の趣旨 | 出典・Tier |
|---|---|---|
| Q3 FY2026(2026-05-26) | ①営業幹部の離職は自発か非自発か、どの階層か。②FY2027 の初期見通しが保守的すぎないか(新規顧客獲得と統合 SecOps 製品の浸透速度の不確実性)。③FCF マージン引き下げ・capex 増の理由 | https://www.fool.com/earnings/call-transcripts/2026/05/26/zscaler-zs-q3-2026-earnings-call-transcript/、Investing.com / Tier 3(要約) |
| Q4 FY2026(2026-09-03) | ①前四半期に話した営業の離職が、生産性にどう影響するか、2027 年に向けて安定したと言えるか(原文: "how are we thinking about the impact of some of the sales churn here that we talked about last quarter in terms of productivity, and do we feel like the sales churn here is stabilized as we go into 2027?")。②ガイダンスの減速の理由。③Red Canary の貢献 | Yahoo のトランスクリプト抜粋 https://finance.yahoo.com/quote/ZS/earnings/ZS-Q4-2026-earnings_call-680670.html / Tier 3 |

CFO の回答の要旨は A-1(営業トップ交代の時間、統合 SecOps の浸透速度、解約は高め、Red Canary の単独貢献は見込まない)。**会社が答えた「解約が高め」の内訳(顧客の解約か、席数の縮小か)は未取得。**

### B-2. 強気派の主要論点(Q4 決算後〜Investor Day 後)

| 証券会社 | アナリスト | 格付・目標株価 | 論拠(検索要約の範囲) | 出典・Tier |
|---|---|---|---|---|
| Needham | Mike Cikos | Buy、180 → 215 ドル | Q4 の予想超えと FY2027 見通し | https://www.benzinga.com/analyst-stock-ratings/price-target/26/09/61627559/zscaler-analysts-boost-their-forecasts-after-better-than-expected-q4-earnings / Tier 3 |
| Stephens & Co. | Todd Weller | Overweight、200 → 225 ドル | 同上 | 同上 |
| Barclays | Peter Weed | Overweight、192 → 200 ドル | 同上 | 同上 |
| Scotiabank | Patrick Colville | Sector Outperform、175 → 200 ドル(その後 240 → 255 ドルの引き上げもあるとの記載) | 同上 | 同上、https://stockanalysis.com/stocks/zs/ |
| Truist | (氏名未取得) | Buy、200 → 250 ドル | (論拠は未取得) | StockAnalysis / Tier 3 |
| Jefferies | (氏名未取得) | 目標 250 ドルに引き上げ(格付は未取得) | 100 億ドル目標は野心的としつつ、AI 需要を評価 | https://www.proactiveinvestors.com/companies/news/1099763/zscaler-s-10-billion-long-term-arr-target-looks-ambitious-says-jefferies-1099763.html / Tier 3 |
| (集計) | — | Investor Day 後、8 社が目標を 185〜275 ドルに引き上げ。8 社中 7 社が Buy または Overweight。StockAnalysis の目標株価の平均は 232.13 ドル(取得日 2026-10-11 前後) | AI セキュリティ需要、非席課金の拡大、営業利益率の過去最高水準 | https://247wallst.com/investing/2026/10/07/wall-street-sees-29-upside-for-zscaler-as-eight-firms-raise-price-targets/ / Tier 3 |

強気論調の骨格(複数の見出しに共通): 「決算は予想超え、AI セキュリティの需要が伸びている」「ガイダンスは保守的」。Q3 後の下落局面でも Wedbush(300 → 220 ドル、Outperform 維持)、Canaccord(275 → 210 ドル、Buy 維持)、Cantor Fitzgerald(300 → 225 ドル、Overweight 維持、capex を懸念)は格付を維持した(Tier 3)。

### B-3. 弱気・慎重派の主要論点

| 証券会社 | アナリスト | 格付・目標株価(時点) | 論拠 | 出典・Tier |
|---|---|---|---|---|
| Evercore ISI | (氏名未取得) | Outperform → In-Line に格下げ、225 → 155 ドル(2026-05-27 頃) | FCF マージン見通しの引き下げ(capex の増加) | https://www.benzinga.com/analyst-stock-ratings/price-target/26/05/52814578/zscaler-guidance-overshadows-q3-beat-analysts-cut-forecasts ほか / Tier 3 |
| Morgan Stanley | Meta Marshall | Hold(Equal Weight)、155 → 145 ドル(Q3 後)。Investor Day 後も Equal Weight で目標 185 ドル(現在の株価より下) | 「SecOps 製品の浸透の裏付けが出るまで "ペナルティボックス" に置く」(要旨)。前月に格下げ済み | https://www.tipranks.com/news/analysts-hit-zscaler-stock-zs-with-price-target-cuts-post-earnings、24/7 Wall St. / Tier 3 |
| BTIG | (氏名未取得) | 2026-04-09 に Neutral へ格下げ | 見出しは「サイバーセキュリティのブームは株価に織り込み済みか」。本文の論拠は**未取得** | https://247wallst.com/investing/2026/04/09/btig-cuts-zscaler-to-neutral-has-the-cybersecurity-boom-already-been-priced-into-this-stock/ / Tier 3(見出しのみ) |
| Freedom Broker | (氏名未取得) | Buy 維持、270 → 230 ドル | 競争リスクの高まりを理由に中期予想を引き下げ(競合名は未取得) | https://m.investing.com/news/analyst-ratings/zscaler-stock-price-target-lowered-to-230-by-freedom-broker-on-growth-concerns-93CH-4712707?ampMode=1 / Tier 3 |
| Jefferies | — | (強気側にも掲載)Investor Day 後に「2026 年度上期に顧客・従業員の離脱がありうる」「100 億ドルは野心的」 | 目標の達成可能性 | proactiveinvestors(上記)/ Tier 3 |
| BofA | — | 基本シナリオの数値は見出しの野心より低い、との指摘 | 同上 | 24/7 Wall St. / Tier 3 |

弱気論調の骨格: ①営業幹部の離職と CRO 交代(執行リスク)、②FY2027 の成長が 25% から 17% 前後に減速、③capex 増による FCF の低下、④統合 SecOps(Red Canary 由来)の浸透が未確認、⑤AI による既存事業の置き換え懸念(B-4)。

### B-4. 報道のナラティブ: 「AI によるソフトウェア・セキュリティ株の代替」懸念

- 2026-02-20: Anthropic が Claude Code Security(AI によるコード脆弱性の検出ツール)を発表し、サイバー株が下落。Bloomberg によると ZS は 5.5% 下落、CrowdStrike 8%、Cloudflare 8.1%、Okta 9.2%、SailPoint 9.4%。Global X Cybersecurity ETF は 4.9% 下落し、2023-11 以来の安値(Wedbush のメモでは ZS が約 11.3% 下落と記載があり、数値が出典間で割れる)。出典: https://www.bloomberg.com/news/articles/2026-02-20/cyber-stocks-slide-as-anthropic-unveils-claude-code-security、https://finance.yahoo.com/news/anthropic-claude-code-security-launch-200400637.html(Tier 3)。
- 反論側: Wedbush は「過剰反応」、Baird の Shrenik Kothari は「パニック主導の大幅な売りと、支配的なナラティブ」、Forrester は「センチメントの伝染」と評した(同上)。BofA は主にコード検査ツールが脅かされるとの見方。ZS のような通信の検査を担う製品への直接の影響は限定的、との論調。
- 2026-04: 後続モデル(Claude Mythos)で再びサイバー株が下落(Forbes、2026-04-14。ZS 個別の下落率は未取得)。https://www.forbes.com/sites/jonmarkman/2026/04/14/how-claude-mythos-wiped-billions-out-of-cybersecurity-stocks/(Tier 3)。
- Q3 後の見出し: 「Zscaler 株が弱いガイダンスで急落。投資家が AI の黙示録を心配したのは正しかったかもしれない」(Yahoo Finance / Motley Fool 系。見出しのみ)https://finance.yahoo.com/markets/stocks/articles/zscaler-stock-plunges-weak-guidance-163702184.html。
- **席課金(席数=従業員数に比例する課金)への懸念**: 検索結果に ZS を名指しした論点は出なかった。一般論(AI が従業員の作業を代替すると、価格決定力が買い手に移る)が Tier 4 の SNS 系ニュースレターに出るのみ。会社側の応答は、非席課金の拡大(A-3: 新規 ACV の 30% 強、Security for AI)。

### B-5. 株価の推移の要点(直近 1 年)

| 日付 | 出来事 | 株価の反応 | 出典・Tier |
|---|---|---|---|
| 2026-02-20 | Claude Code Security の発表 | −5.5%(Bloomberg)〜約 −11%(Wedbush) | B-4 |
| 2026-03-10 | Oppenheimer が目標を 250 ドルに引き下げ | (反応は未取得) | https://www.marketbeat.com/instant-alerts/zscaler-nasdaqzs-price-target-cut-to-25000-by-analysts-at-oppenheimer-2026-03-10/(URL・見出しのみ) |
| 2026-04-09 | BTIG が Neutral に格下げ | (反応は未取得) | B-3 |
| 2026-04-14 | Claude Mythos の報道 | (個別は未取得) | B-4 |
| 2026-05-27 | Q3 決算の翌日 | **−31.52%(−58.19 ドル)、126.41 ドルで引け。過去最悪の 1 日**(直前の終値は筆者計算で 184.60 ドル) | https://www.globenewswire.com/news-release/2026/10/06/3376112/1087/en/investor-alert-pomerantz-law-firm-investigates-claims-on-behalf-of-investors-of-zscaler-inc-zs.html ほか訴訟告知 / Tier 4。「30% 超の下落・過去最悪」は CNBC https://www.cnbc.com/2026/05/27/zscaler-zs-earnings-q3-2026.html の要約で補強(Tier 3) |
| 2026-09-04 | Q4 決算の翌日 | 約 −4%(Benzinga: −4.1% で 170.56 ドル。Investing.com: 日中 −4.25% で 170.25 ドル)。Vantage Markets は寄り付き直後に +0.13%(177.88 ドル)と記載(時点の違いと判断) | https://www.cnbc.com/2026/09/03/zscaler-zs-q4-earnings-2026.html(見出し: 予想超え・前向きなガイダンスでも株価は下落)、Benzinga、Investing.com / Tier 3。Traders Union の「+4.29%・201.41 ドル」は日付不明で採用しない |
| 2026-09 中旬 | 目標株価の引き上げが相次ぎ株価が回復 | 約 200 ドル台へ(出典により 201 ドル前後) | Tier 4 の複数サイト。**単独出典扱い** |
| 2026-09-25 | CRO 交代(09-24 公表)の翌日 | −10.06% で 193.05 ドル(直前は筆者計算で 214.64 ドル) | A-4(Tier 4、単独出典) |
| 2026-10-06 | Investor Day | 当日 約 +5%。その後の記事で 213.01 ドル | Yahoo Finance、24/7 Wall St. / Tier 3 |

注: 各日の終値の確定値は未取得(別担当の株価表を優先すること)。

### B-6. 空売りレポート・著名な弱気論者

**検索では確認できず(専用の検索は未実施のため「存在しない」とは言えない)。** 代わりに、Q3 後の下落を受けた株主訴訟の告知が出ている(G 参照)。

---

## C. 一次情報(スカットルバット)

| # | 観察 | 内容 | 出典・Tier | 構造仮説への含意 |
|---|---|---|---|---|
| C-1 | Gartner マジック・クアドラント | 2026 年版 SSE の MQ は 2026-07-29 公開。評価対象は Broadcom、Cisco、Cloudflare、iboss、Netskope、Palo Alto Networks、Skyhigh Security、Zscaler の 8 社。Zscaler は SASE プラットフォームと SSE の両方で Leader(SSE は 5 年連続)と自社が発表(2026-08-04)。Netskope も 5 年連続の Leader。Palo Alto Networks も Leader で、Gartner は統一コンソールの改善を評価する一方、Prisma Access のライセンスは「複雑で分かりにくい」との顧客の声を記載(要約)。**出典間の食い違い**: 比較サイト(Tier 4)は ZS を SASE で "Visionary" としているが、会社リリースと矛盾するため、リリースを採る(Gartner 本文での確認は未了)。また PANW が「前年は Challenger」との要約は、SDxCentral の過去の見出し(PANW が Leader 入り)と矛盾する可能性があり**要照合** | https://ir.zscaler.com/news-releases/news-release-details/zscaler-recognized-leader-both-2026-gartnerr-magic-quadranttm(Tier 1)、https://www.gartner.com/en/documents/8192429、https://www.paloaltonetworks.com/sase/gartner-sse-mq-leader-2026、https://www.netskope.com/why-netskope/gartner-magic-quadrant-for-security-service-edge(Tier 1、競合の自社発表)、https://www.sdxcentral.com/analysis/palo-alto-networks-joins-netskope-zscaler-as-leaders-in-gartner-sse-magic-quadrant/ | SSE は上位 3 社(ZS・Netskope・PANW)が横並びの Leader。**単一ベンダー SASE への移行**で PANW が追い上げる構図の裏付け(位置づけの変化は要確認) |
| C-2 | 価格・ライセンス体系 | 課金は原則ユーザー単位の年額で、Business / Business Plus / Transformation / Unlimited の階層。ZIA(インターネット接続の保護)と ZPA(社内アプリへのアクセス)は別ライセンスだが束ねて売られることが多い。**席に依存しない通信量課金**の価格表がある(GSA 価格表: デバイス通信が約 15.75 ドル/GB、サーバー・IoT 通信が約 18 ドル/GB。いずれも 1 GB/月の年額換算の掲載値。リセラー経由の参考値) | GSA 価格表 https://static.carahsoft.com/concrete/files/4516/4743/9721/Zscaler_GSA_1.pdf(Tier 3)。階層・割引は第三者ガイド https://redresscompliance.com/zscaler-enterprise-licensing-guide.html、https://www.bestnegotiationconsultingfirms.com/blog/zscaler-enterprise-licensing-pricing.html(Tier 4。1,000 ユーザー超で約 34〜35% 割引、30〜40% の割引が一般的との記載。**信頼性が低く数値の根拠にはしない**) | 席課金が主で、非席(通信量)課金は価格表に存在する。席数が減る環境(AI による従業員の代替)で売上が減る構造は残る。会社は非席の比率拡大(新規 ACV の 30% 強)で対応 |
| C-3 | 契約形態の利用統計(会社開示) | Z-Flex の TCV は FY2026 に 17 億ドル超。Security for AI の予約は Q4 に前期比 +50% 超。Security for AI の案件の 70% がデータセキュリティ製品を併せて契約 | Fool の Q4 トランスクリプト要約、Investing.com / Tier 3(要照合) | 席に依存しない契約形態と AI 保護の拡大を数字で裏付ける会社発言 |

**要件(最低 3 件)について**: C-1・C-2 は第三者または公的に近い情報。C-3 は会社の開示で、純粋なスカットルバットではない。**求人動向、顧客の評価、チャネル・パートナーの声、競合の決算での ZS への言及、トラフィック処理量、SSE 市場規模は欠損。** 構造仮説の裏付けは弱いと評価すべき。

---

## D. 競争と業界の構造

- SSE/SASE は ZS・Netskope・PANW が Leader に並ぶ(C-1)。Cloudflare、Cisco、Broadcom も評価対象。ZS は 2 つの MQ で Leader と自己申告。
- PANW は SSE の統合コンソールを改善したと Gartner が評価(要約)。「単一ベンダー SASE」を掲げる PANW・Cisco・Cloudflare に対し、ZS は専業の優位(クラウドネイティブ)を主張すると見られるが、会社発言は未取得。
- Freedom Broker が 2026-05 に「競争リスクの高まり」で中期予想を引き下げた(競合名は未取得)。
- 席課金の弱点: 検索結果に ZS を名指しした分析はなし(B-4)。会社の回答は非席課金の拡大。
- Netskope の上場後の開示、価格圧力、セキュリティ予算の動向、SSE の市場規模は**欠損**。

## E. 異常値の候補

| # | 数字 | 問い(答えは未調査) |
|---|---|---|
| 1 | 見出しの ARR 成長 +25% に対し、Red Canary を除く有機成長は +20%(Q3 は +21%)。NNARR の伸びは +17% | なぜ見出しの成長率と有機成長の差が約 5 ポイントあり、有機の ARR 成長は Q3 から Q4 に減速しているのか。CEO が言う「Red Canary を除く成長が Q4 に 17% へ加速」はどの指標か(NNARR と思われるが表現が曖昧) |
| 2 | Q4 の営業キャッシュフロー 2.79 億ドルに対し FCF は 6,080 万ドル(差 約 2.2 億ドル)。FY2026 の FCF マージン見通しは 26.5〜27% から 22.8〜23.3% へ引き下げ | なぜ capex が売上の 1 桁後半 % に膨らむのか。何を「現在の価格を確定させるために前倒し」したのか(データセンター機器か) |
| 3 | GAAP 営業赤字 1,550 万ドルに対し non-GAAP 営業利益 2.18 億ドル(差 売上比 約 26 ポイント) | なぜ GAAP と non-GAAP の差が売上の 4 分の 1 以上なのか(SBC と買収無形資産の償却の内訳は) |
| 4 | FY2027 売上ガイダンスの成長が +16.6〜17.5% で、Q4 の +25% から急減速。Q3 時点の初期見通し(ARR +16〜17%)から Q4 でも変わらず、Investor Day でも再確認 | なぜ 2 回の決算と Investor Day を経ても数字が動かないのか(保守的な設定か、営業の混乱を織り込んだ実力値か) |
| 5 | 株価は 2026-05-27 の 126.41 ドルから 213 ドル前後へ約 +68%(筆者計算)戻ったが、ガイダンスは変わっていない | なぜガイダンスが不変のまま、4 か月余りで株価が 7 割戻ったのか(何を市場は織り込み直したのか) |
| 6 | Security for AI の ARR は FY2026 末で約 7,000 万ドル(総 ARR 37.7 億ドルの約 1.9%、筆者計算)。一方で FY2031 の上振れ分は約 20 億ドルを AI に帰属させる | なぜ 1.9% の事業から 5 年で約 20 億ドルの上振れを見込めるのか(単価、導入率、席に依存しない課金の前提は) |
| 7 | 人員を約 3% 削減しながら、営業と AI に再配分。同時に営業幹部の離職と CRO 交代 | なぜ営業の離職と人員削減を同時に行うのか(生産性を上げるための組織変更か、離職の予防か) |

注: 1・2・3 の ARR・FCF 数値は初版の出典(8-K 要約・Benzinga)に基づく。差額・比率はすべて筆者計算。

## F. 条件9(AIの停めない運用)に関わる事実

- **AI を守る製品(Security for AI)**: ARR は FY2026 末で約 7,000 万ドル(Investor Day 報道、Tier 3 の MarketBeat・Yahoo)。Q4 の予約は前期比 +50% 超。案件の 70% がデータセキュリティ製品を併せて契約(Tier 3、要照合)。
- 製品の中身: SPLX(2025-11 買収)による AI 資産の発見・リスク評価・自動レッドチーム。SquareX(2026-02 買収)はブラウザ上の AI 利用の制御に関係すると推定されるが、製品の説明は未取得。「生成 AI アプリの利用制御」の製品名・採用社数は**欠損**。
- **AI で動く製品**: Red Canary を軸にした Agentic SecOps(AI による運用の自動化)は、FY2027 下期から貢献、FY2028 に本格化との要約(Tier 3、**単独出典**)。Rubin は FY2027 に Red Canary の単独 NNARR 貢献を見込まないと発言。
- CEO の位置づけ: 「エージェント型 AI の脅威の対処と、AI エージェント・AI モデルの安全な導入を支援する立場にある」(要旨、2026-09-03 のリリース)。
- 条件9の適用: AI を守る製品は存在するが、ARR は総 ARR の約 2%。AI 推論基盤を自社で運営する事業ではない。関与の売上規模は小さいので、判定は Opus に委ねる。
- 欠損: AI 関連 ARR の定義、FY2027 の AI 関連の見通し、AI エージェント向け製品の価格体系。

## G. リスク事象

- **株主訴訟・調査(2026-05-27 の下落後)**: Pomerantz(2026-10-06 の告知)が、証券詐欺の可能性を調査と発表。Faruqi & Faruqi も調査。Bronstein, Gewirtz & Grossman は対象期間を 2025-07-18〜2026-04-28、**主任原告の申立期限を 2026-10-05**と掲載(期限があることから訴状の提出が示唆されるが、裁判所の記録での確認は未了)。The Gross Law Firm は別の対象期間(2021-05-27〜2026-05-27)を掲載しており、**出典間で食い違い**。出典: https://www.globenewswire.com/news-release/2026/10/06/3376112/1087/en/investor-alert-pomerantz-law-firm-investigates-claims-on-behalf-of-investors-of-zscaler-inc-zs.html、https://bgandg.com/cases/zscaler-inc-zs-class_action_lawsuit/、https://www.morningstar.com/news/pr-newswire/20260609ny79101/zs-deadline-the-gross-law-firm-reminds-zscaler-inc-investors-of-upcoming-securities-class-action-deadline、https://www.newsfilecorp.com/release/304727/ZS-CLASS-ACTION-INVESTIGATION-Faruqi-Faruqi-LLP-Investigates-Claims-on-Behalf-of-Investors-of-Zscaler(Tier 4。原告側弁護士の宣伝文で、事実認定ではない)。
- **経営陣の株式売却**: CFO Kevin Rubin が 2026-08-25 に 87,210 ドル分、2026-09-25 頃に 519 株を売却(Rule 10b5-1 の計画売却と報じられている。いずれも少額)。https://www.investing.com/news/insider-trading-news/zscaler-cfo-kevin-rubin-sells-87210-of-zs-common-stock-93CH-4879404、https://www.gurufocus.com/news/9100849/zscaler-zs-cfo-kevin-rubin-sells-519-shares-as-stock-trades-below-gf-value(Tier 3)。CEO Chaudhry が 2,852 株を売却したとの断片があるが、日付・金額は未確認(Tier 4、**単独出典**)。大口売却の有無は**欠損**(Form 4 の確認が必要)。
- **営業の執行リスク**: CRO の辞任・営業幹部 2 名の退社・人員 3% 削減・解約が高め(A-1、A-4)。アナリストは「コスト削減と戦略の転換は、AI 投資が約束どおりの成果を出さなければ執行リスクを露わにする」と指摘(Traders Union 経由、Tier 4)。
- **障害・規制・会計上の論点**: 2026 年の大規模障害は検索結果に出なかった(専用検索は未実施)。会計上の論点(買収の会計、SBC、Red Canary の収益認識など)は**欠損**。

---

## H. 欠損と、あれば確認すべき項目(優先順)

1. 8-K・IR・10-K 本文での照合: FY2027 ガイダンスの全項目(EPS、FCF)、ARR の定義、100 万ドル超顧客、DBNRR、RPO、Red Canary の寄与。
2. 過去 3 年のガイダンス達成状況(FY2024・FY2025 の期初ガイダンスと実績)。
3. アナリスト名・質問者名が入った逐語のトランスクリプト(Q3・Q4)。
4. Investor Day 資料の長期の営業利益率・FCFマージン・非席課金の目標。
5. 求人動向、顧客の評価、チャネル・パートナーの声、競合(Netskope・PANW・Cloudflare・Cisco)の決算での ZS への言及、トラフィック処理量、SSE 市場規模。
6. 空売りレポート、2026 年の大規模障害、Form 4(CEO の売却)、転換社債・自社株買いの状況。
7. BTIG の格下げ理由、Evercore 等のアナリスト氏名、Truist・Jefferies の論拠。

## I. 出典一覧(いずれも検索ツールの要約経由。取得日 2026-10-11)

| URL | 区分 | 使った節 |
|---|---|---|
| https://www.sec.gov/Archives/edgar/data/0001713683/000171368326000156/zs-07312026_991.htm | Tier 1(Q4 FY2026 決算 8-K。本文未読) | A |
| https://www.sec.gov/Archives/edgar/data/0001713683/000171368326000095/zs-04302026_991.htm | Tier 1(Q3 FY2026 決算 8-K。本文未読) | A-1 |
| https://www.sec.gov/Archives/edgar/data/0001713683/000171368326000156/zs-20260901.htm | Tier 1(人員再編の 8-K) | A-3 |
| https://www.sec.gov/Archives/edgar/data/0001713683/000171368326000193/zs-09242026_991.htm | Tier 1(CRO 交代の 8-K) | A-4 |
| https://www.sec.gov/Archives/edgar/data/0001713683/000171368326000200/zsinvestordaypressrelease.htm、https://www.zscaler.com/press/zscaler-hosts-2026-investor-day-reaffirms-first-quarter-and-fiscal-2027-guidance | Tier 1(Investor Day リリース) | A-2 |
| https://www.sec.gov/Archives/edgar/data/0001713683/000171368326000157/zs-20260731.htm | Tier 1(10-K FY2026) | A-3 |
| https://ir.zscaler.com/news-releases/news-release-details/zscaler-recognized-leader-both-2026-gartnerr-magic-quadranttm | Tier 1 | C-1 |
| https://www.fool.com/earnings/call-transcripts/2026/09/09/zscaler-zs-q4-2026-earnings-call-transcript/ ほか Yahoo・Benzinga・Investing.com のトランスクリプト | Tier 3(話者ラベルの誤記あり) | A-1、B-1 |
| https://www.benzinga.com/analyst-stock-ratings/price-target/26/09/61627559/zscaler-analysts-boost-their-forecasts-after-better-than-expected-q4-earnings、https://www.benzinga.com/analyst-stock-ratings/price-target/26/05/52814578/zscaler-guidance-overshadows-q3-beat-analysts-cut-forecasts | Tier 3 | B-2、B-3 |
| https://247wallst.com/investing/2026/10/07/wall-street-sees-29-upside-for-zscaler-as-eight-firms-raise-price-targets/、https://www.proactiveinvestors.com/companies/news/1099763/zscaler-s-10-billion-long-term-arr-target-looks-ambitious-says-jefferies-1099763.html | Tier 3 | B-2、B-3 |
| https://www.bloomberg.com/news/articles/2026-02-20/cyber-stocks-slide-as-anthropic-unveils-claude-code-security | Tier 3 | B-4 |
| https://www.cnbc.com/2026/09/03/zscaler-zs-q4-earnings-2026.html、https://www.cnbc.com/2026/05/27/zscaler-zs-earnings-q3-2026.html | Tier 3 | B-5 |
| https://www.globenewswire.com/news-release/2026/10/06/3376112/1087/en/investor-alert-pomerantz-law-firm-investigates-claims-on-behalf-of-investors-of-zscaler-inc-zs.html ほか訴訟告知 | Tier 4(原告側弁護士の告知) | B-5、G |
| https://www.cybersecuritydive.com/news/zscaler-buy-red-canary/749147/、https://www.securityweek.com/zscaler-acquires-ai-security-company-splx/ | Tier 3 | A-3 |
