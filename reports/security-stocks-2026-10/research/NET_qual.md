# Cloudflare(NET)定性調査 一次整理【未完成版: 検索上限により A〜G の大半が欠損】

評価基準日 2026-10-11 / 決算期末 12月31日 / 調査担当: Sonnet / 取得日はすべて 2026-10-11

## 0. 本書の状態(最初に読むこと)

- **本書は未完成である。** WebSearch の呼び出し上限(1ターン200回、全エージェント共有)がすでに使い切られており、
  実行できた検索は2件のみ(下記 §0-3)。3件目以降は「検索は実行されなかった」という応答が返った。
  応答は「上限に達したので追加検索をせず、利用者に追加の依頼か上限の引き上げを求めよ」という指示だったため、
  curl・第三者の閲覧サービス・アーカイブ経由の迂回は行っていない。
- 検索結果は「要約文と出典URL」のみで、決算説明会のトランスクリプト(発言録)・委任状説明書・10-K/10-Qの本文は
  **1件も読めていない**。したがって A の「経営陣の発言の引用」、B の「アナリストの質問・強気弱気」、
  C〜G の大半は**欠損**である。推測では埋めていない(00_standard.md §2)。
- 収集できた事実は §0-2 の表のみ。すべて「検索エンジンの要約文経由」であり、原文(8-K 本文)は未確認。
  Tier 1(会社開示)の URL が示されていても、本書の数値は要約文からの転記であり、原文照合は未了と読むこと。
- 再開の方法: 利用者が追加メッセージを送るか、環境変数 `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` を引き上げたうえで、
  §9 の検索クエリ案を優先順に実行する。

### 0-1. 親(Opus 統括)の前提との食い違い候補(要確認)

- 依頼文は「年換算売上50億ドルの目標時期」を問うているが、今回の検索ではこの目標を**確認できなかった**。
  逆に、Seeking Alpha の決算説明会ページ一覧(page=2)に
  「Cloudflare outlines $3B annualized revenue target for Q4 2026 as enterprise momentum accelerates」
  (和訳: 大企業向けの勢いが強まる中、2026年第4四半期に年換算売上30億ドルの目標を示す)という**見出し**があった
  (出典: https://seekingalpha.com/symbol/NET/earnings/transcripts?page=2 、Tier 3、取得 2026-10-11)。
  どの回の説明会の見出しか、本文の定義(年換算=四半期売上×4か、総額か)は**未確認**。
- 整合性の確認(独自計算、下記の要約値が正しいと仮定した場合のみ成立):
  Q3 2026 ガイダンス中央値 736.5 百万ドル ×4 = 約29.5億ドル。通期ガイダンス中央値 2,867 百万ドルから
  Q1(639.8)・Q2(696.1)・Q3(736.5)を引いた第4四半期の暗黙値は約794.6 百万ドル、×4 = 約31.8億ドル。
  つまり「年換算30億ドル」は2026年内に到達する水準であり、「年換算50億ドル」とは別の(より遠い)目標でない限り、
  依頼文の前提とは時期が合わない。**目標の数値・定義・期限は一次資料で確認が必要。**

### 0-2. 収集できた事実(2026年第2四半期の決算発表、2026-08-06)

| 項目 | 値 | 出典(Tier)・注記 |
|---|---|---|
| 発表日 | 2026-08-06 | 会社の決算発表(Business Wire 版)。Tier 1 |
| 売上 | 696.1 百万ドル、前年同期比 +36% | 同上。要約文経由 |
| GAAP 営業損失 | 205.7 百万ドル(売上比 約-29.6%、独自計算) | SEC 8-K 別紙 99.1 の要約。Tier 1(要約経由) |
| 調整後(non-GAAP、株式報酬・買収無形資産の償却などを除いた会社定義)営業利益 | 96.1 百万ドル(売上比 約13.8%、独自計算) | 同上 |
| GAAP 粗利率 | 71.8% | 同上 |
| 調整後粗利率 | 73.1% | 同上 |
| GAAP 純損失・1株損益 | 純損失 170.0 百万ドル、-0.48 ドル/株 | 報道(fbroker.kz)の単独出典。Tier 3〜4。印: 単独出典 |
| 調整後 EPS | 0.29 ドル | 同上。単独出典 |
| cRPO(12か月以内に計上予定の残存履行義務) | 前年同期比 +35% | 同上。単独出典 |
| 市場予想(発表前の暫定) | 売上 約664.7 百万ドル、調整後EPS 0.27 ドル | earningswhispers.com。Tier 4。単独出典 |
| 売上の予想超過幅 | 約 +4.7%(696.1÷664.7、独自計算) | 予想値が Tier 4 のため暫定 |
| 第3四半期ガイダンス | 売上 736〜737 百万ドル | 報道の要約。単独出典。会社の原文未確認 |
| 通期2026ガイダンス | 売上 2,864〜2,870 百万ドル、調整後EPS 1.25〜1.26 ドル | 同上。単独出典 |
| 会社コメント(要約) | 有料顧客数・大口顧客数・開発者数が過去最高の伸び | 検索ツールの要約文。原文未確認 |

出典URL(いずれも 2026-10-11 取得):
- SEC 8-K 別紙 99.1: https://www.sec.gov/Archives/edgar/data/0001477333/000147733326000053/q226exhibit991.htm
- Business Wire: https://secure.businesswire.com/news/home/20260806407787/en/Cloudflare-Announces-Second-Quarter-2026-Financial-Results
- 会社IR(PDF): https://cloudflare.net/files/doc_financials/2026/q2/Q2-26-Exhibit-99-1.pdf
- 報道(単独出典): https://fbroker.kz/en/news/51380-cloudflare-otcitalas-za-2-i-kv-vyse-ozidanii-ru-2
- 予想値(Tier 4): https://earningswhispers.com/epsdetails/NET/202606
- 注意: 同じ検索で出た `furlio19.duckdns.org` は会社プレスリリースの複製を名乗る個人ドメインで、信頼できない。使用しない。

### 0-3. 実行できた検索(2件)と、見つかったが未読の資料

1. 「Cloudflare second quarter 2026 financial results revenue」: 上記 §0-2 の根拠。
2. 「Cloudflare Q2 2026 earnings call transcript Matthew Prince」: **第2四半期(2026-08)の説明会録は見つからなかった。**
   見つかった未読資料:
   - 第1四半期 2026 説明会録(2026-05-07 17:00 米東部時間、FactSet 校正版、会社IRに掲載。Tier 1):
     https://cloudflare.net/files/doc_financials/2026/q1/CORRECTED-TRANSCRIPT-Cloudflare-Inc-NET-US-Q1-2026-Earnings-Call-7-May-2026-5-00-PM-ET.pdf
   - 第4四半期 2025 説明会録(2026-02-10、Seeking Alpha。Tier 3): https://seekingalpha.com/article/4868435-cloudflare-inc-net-q4-2025-earnings-call-transcript
   - 第1四半期 2026 の売上 639.8 百万ドル、前年同期比 +34%(bullfincher.io に転載された経営陣の冒頭発言とされる。Tier 4、単独出典)
     https://bullfincher.io/companies/cloudflare/earnings-call
   - Cloud Wars の「CEOの名言」記事は、前年同期比 +54% の回の話で年代が合わない。**使用しない。**

---

## A. 経営陣シナリオの一次情報【欠損: 発言録未読】

### A-1. 直近4回の説明会(2025 Q3〜2026 Q2)での経営陣の発言【欠損】
- 発言の引用は **0件**。上記 §0-3 の未読資料(Q1 2026 録、Q4 2025 録)を読むことが最短の補完手段。
- 2025 Q3(2025-10 末)の説明会録、2026 Q2(2026-08-06)の説明会録、直近の Investor Day は、URL も未特定。

### A-2. 数値目標【一部のみ・要確認】
- 年換算売上の目標: §0-1 のとおり、見出しは「2026年第4四半期に年換算30億ドル」を示唆。**50億ドルは未確認。**
  定義・期限・発言者は欠損。
- 長期の営業利益率目標、capex/売上の目安: **欠損**。

### A-3. ピース一覧【欠損】
製品(Workers AI、AI Gateway、R2、SASE、Email Security)、買収、営業組織の変更、プール型の大型契約、転換社債の発行・償還:
いずれも発表日・規模・出典を**取得できていない**。§0-2 の「有料顧客数・大口顧客数・開発者数が過去最高の伸び」だけが
会社コメントとして確認できた(要約経由)。

### A-4. 過去3年のガイダンス達成状況【欠損】
- 今回確認できた期初 vs 実績は **1組だけ**: Q2 2026 の売上 696.1 百万ドルは、発表前の暫定予想 約664.7 百万ドルを上回った
  (会社の期初ガイダンスそのものは未取得。予想値は Tier 4)。過去3年分の期初ガイダンス表は**欠損**。

### A-5. 経営陣の経歴・在任・報酬KPI・交代【欠損】
- 今回の結果から確認できたのは、Matthew Prince が共同会長・共同創業者・CEO の肩書で第1四半期 2026 録に載っていること
  (検索ツールの要約、FactSet 校正版録の参加者欄。Tier 1 だが要約経由)のみ。
- Michelle Zatlyn の現職、CFO の現職と在任、デュアルクラス株式の構造、委任状説明書の報酬KPI: **欠損**。

## B. 市場の仮説の出典【欠損】

- B-1 アナリストの質問、B-2 強気・弱気各3件以上(証券会社名・アナリスト名・目標株価)、B-3 空売りレポート、
  B-4 報道のナラティブ(AIによる代替懸念、Cloudflare は AI 受益者か)、B-5 直近1年の株価イベント: **すべて欠損。**
- 手掛かりは 1 件のみ: Seeking Alpha の見出し(§0-1)が「大企業向けの勢い(enterprise momentum)」という語を使っている。
  これは報道側が使うナラティブの語であり、強気派の論点の種として記録するにとどめる。

## C. 一次情報(スカットルバット)【欠損: 0件。最低3件の要件を満たせていない】

価格表の改定、ネットワーク規模、Cloudflare Radar、顧客評価、Gartner の位置、求人、競合の開示、2025年の大規模障害の事実:
いずれも**取得できていない**。構造仮説の裏付けは現時点でゼロ件であり、Opus は B 型の構造仮説を一次情報で裏付けられていない前提で扱うこと。

## D. 競争と業界の構造【欠損】

CDN・WAF・Zero Trust・開発者プラットフォーム・AI推論の各市場の競争、ハイパースケーラーとの関係、価格の決まり方、
ネットワーク原価の推移: **欠損**。

## E. 異常値の候補(§0-2 の数字から作れる3つ。いずれも市場ナラティブとの照合は未了)

| # | 候補 | 根拠の数字(出典) | なぜこの数字なのか(問い) |
|---|---|---|---|
| E1 | 売上成長率が約7億ドル規模で加速している | 第1四半期 +34%(639.8 百万ドル、単独出典 Tier 4)→ 第2四半期 +36%(696.1 百万ドル、Tier 1 要約)。前期比は約 +8.8%(独自計算) | なぜ規模が大きくなっても成長率が上がるのか。新規顧客か、既存顧客の利用量か、大型契約か |
| E2 | GAAP と調整後の営業損益の差が売上の約43% | GAAP 営業損失 -205.7 百万ドル、調整後営業利益 +96.1 百万ドル、差 約301.8 百万ドル(独自計算、Tier 1 要約) | なぜこれほど大きいのか。株式報酬(SBC)の水準か、買収関連・一時費用か。内訳は未取得のため、中身の確認が先 |
| E3 | 第2四半期の売上が予想を約4.7%上回った | 実績 696.1 百万ドル対 暫定予想 約664.7 百万ドル(予想側は Tier 4、単独出典) | なぜ予想がこれだけ外れたのか。アナリストの慎重さか、会社のガイダンス運用(ガイダンスが低めに置かれる傾向)か。過去4四半期の超過幅の系列が必要 |

補足: 粗利率(GAAP 71.8%、調整後 73.1%)は取得したが、**過去との比較がないため「低下」「上昇」の判断はできない。**
DNR(既存顧客の売上継続率)、大口顧客の伸び、RPO の伸び、capex/売上は**欠損**(RPO は cRPO +35% のみ、単独出典)。

## F. 条件9(AIの停めない運用)に関わる事実【欠損】

Workers AI、AI Gateway、AIクローラー対策、Pay per crawl、AIエージェント関連の製品の利用量・顧客数の開示値: **取得できていない。**
売上規模の開示があるかどうかも未確認。

## G. リスク事象【欠損】

大規模障害(2025年を含む)、訴訟、各国の規制、会計上の論点、経営陣の株式売却: **取得できていない。**
(E2 の GAAP と調整後の差は会計上の論点の入口になりうるが、内訳が未取得。)

---

## 8. 既知の制約(Opus 向けのまとめ)

1. WebSearch 上限到達により、検索2件で停止。3件目以降は未実行。
2. トランスクリプト・委任状説明書・10-K/10-Q の本文は未読。§0-2 の数値は要約文の転記で、原文照合は未了。
3. 単独出典の数値(純損失、調整後EPS、cRPO、ガイダンス、予想値、第1四半期売上)は、会社IRに当たり直すまで「未確定」。
4. 「年換算50億ドル」は確認できず、「年換算30億ドル(2026年第4四半期)」の見出しのみ(本文未確認)。

## 9. 再開用の検索クエリ案(優先順。Opus が使える検索枠で実行する場合の順)

1. Cloudflare Q2 2026 earnings call transcript(Q2 録。cloudflare.net / Seeking Alpha / Motley Fool / Investing.com)
2. Cloudflare "annualized revenue" target $3 billion OR $5 billion Prince Seifert(目標の定義・期限・発言者。許可ドメイン cloudflare.net)
3. Cloudflare Q1 2026 earnings call transcript prepared remarks Seifert dollar-based net retention large customers RPO(DNR・大口顧客・RPO)
4. Cloudflare Q3 2025 earnings call transcript(2025-10 末)、Cloudflare Q4 2025 earnings call(2026-02-10)
5. Cloudflare Investor Day OR "analyst day" 2026 long-term targets operating margin capex
6. Cloudflare analyst price target NET upgrade OR downgrade 2026(証券会社名・目標株価。強気弱気各3件)
7. Cloudflare short seller OR bearish valuation price-to-sales 2026
8. Cloudflare stock AI beneficiary OR "AI disruption" software selloff 2026
9. Cloudflare outage November 2025 OR December 2025 post-mortem(大規模障害の事実)
10. Cloudflare Workers AI usage OR customers OR "AI Gateway" OR "Pay per crawl" 2026(条件9)
11. Cloudflare proxy statement 2026 executive compensation metrics dual class
12. Cloudflare convertible notes 2026 issuance OR repurchase
13. Cloudflare acquisition 2026 OR 2025(買収一覧)
14. Cloudflare pricing change 2026 Workers pricing OR plan changes(価格表)
15. Gartner Magic Quadrant Cloudflare 2026(SSE・WAAP)
16. Cloudflare copyright lawsuit OR regulatory OR Ofcom OR Italy "Piracy Shield" 2026(訴訟・規制)
17. Cloudflare insider selling Form 4 Prince Seifert 2026(株式売却)
18. Cloudflare Radar report 2026 traffic share OR network capacity Tbps cities(ネットワーク規模)
19. Akamai OR Fastly OR Zscaler earnings Cloudflare competition 2026(競合の開示)
20. Cloudflare job postings sales hiring 2026(求人)
