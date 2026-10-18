# T2 会社の中期目標・RPO・容量計画(Oracle / NYSE: ORCL)

調査日: 2026-10-13 / 対象: FAM(2025-10-16)〜 Q1 FY27(2026-08-31 終了、2026-09-10 発表)
役割: 事実・数値・出典の整理のみ。投資判断・推奨は書かない。

---

## 0. 要約(10 行)

1. FAM(2025-10-16)の FY30 目標は、総売上 $225B(5 年 CAGR 31%)、非 GAAP EPS $21(CAGR 28%)、OCI 売上 $166B(2025-09 の $144B から +$22B)。OCI の増額幅は FY27 +$2B、FY28 +$4B、FY29 +$15B、FY30 +$22B(CreditSights)なので、経路は $18B → $34B → $77B → $129B → $166B(算出)。[T2-01][T2-03][T2-04] T3*
2. FAM の短期 EPS 目標は FY26 $8.00、FY27 $10.65(Stifel/TheFly、基準は未確認)。FY26 実績は $7.63(一時益を除くと $6.83)、FY27 ガイダンスは $8.10 で、FY27 は FAM 目標比 -23.9%(算出: 8.10 ÷ 10.65 − 1)。[T2-06] T3*
3. FY30 目標の再確認は Q4 FY26(2026-06-10)の CFO Maxson の "full reconfirmation ... on the long term targets"(売上 CAGR 31%、EPS CAGR 28%)のみ確認。Q3 FY26 と Q1 FY27 の再確認・引上げ発言は欠損。FY27 売上は "at least $90B"(+34%)、EPS $8.05 → $8.10。[T2-23][T2-11] T1*/T3*
4. RPO $664B(2026-08-31)の売上化時期(10-Q 要約): 12 か月以内 約 13%($86.3B)、13〜36 か月 37%($245.7B)、37〜60 か月 34%($225.8B)、60 か月超 16%($106.2B、残差の算出)。36 か月以内は 50% で、前期の 46%(12% + 34%)から上昇。[T2-09][T2-10] T1*
5. 顧客別: OpenAI は約 $300B・約 5 年・2027 年開始(WSJ 報道、会社は金額非開示)で RPO の約 45%(算出: 300 ÷ 664)、Meta は $20B(FAM)。xAI・NVIDIA・AMD の金額は欠損。「OpenAI 以外が過去 1 年で 2 倍超」は 1 媒体のみ。
6. 納入容量: FY26 通期 >1.2GW、Q3 FY26 >400MW、Q1 FY27 850MW・30 万基超の GPU(Q4 の約 3 倍、前年度納入量の 73%)。Q4 FY26 時点の見通し "approaching one gigawatt" に対し 85%(算出)。[T2-12][T2-22] T3*
7. 需給: GPU 稼働率 97.9%、更新対象の GPU はすべて前契約比 +20% で更新または再販、制約は「GPU とファブから電力とデータセンターへ移った」(Magouyrk)。「需要が供給を上回る」の逐語は Q1 FY27 では未確認(Q3 FY26 に "outpacing supply" との要約が 1 件)。
8. 拠点: 6/8 棟・618MW(全体の 75%)を顧客に納入(キャンパス名は未特定、Abilene の可能性)、Shackelford は 115MW が通電済みで顧客納入は CY2027 上期、Jupiter(2.45GW)は 2026-09-24 に force majeure 通知。会社は NM・WI が FY27 ガイダンスに影響しないと説明。
9. 「10GW 超」は Q3 FY26(2026-03-10)の発言で「今後 3 年に稼働する電力・データセンター容量をパートナー経由で確保」、90% 超をパートナーが資金負担。capex は FY27 $90〜95B(純現金 $70B 以下)、FY28 は数値なし(FY27・FY28 がピークとの要約)。
10. GPU 調達: AMD MI450 5 万基は 2026 暦年 Q3 から初期展開(2025-10-14 発表)。NVIDIA 調達契約、MI450 の稼働実績、四半期ごとの GPU 納入数の内訳は欠損。

---

## 1. 読み方

- 取得手段は WebSearch のみ(26 回、上限まで使用)。全数値が検索要約経由で、原本(SEC 提出書類・説明会原文・FAM スライド)は未読。そのため Tier の後ろに `*` を付けた。
- Tier: 1 = 会社開示、2 = 規制当局・公的統計、3 = 報道・アナリスト・データ会社、4 = ブログ・SNS・AI 要約。「1*」は会社開示だが要約経由。
- 「(算出)」は本調査での計算。式を併記。
- 既存調査と重複する事実は「再掲」と書き、出典は既存ファイルのまま。既存ファイル: `research/S1_management_scenario.md`(S1)、`research/S3_scuttlebutt.md`(S3)、`research2/R7_capital_power.md`(R7)、`research3/W5_oracle_ai_economics.md`(W5)。

---

## 2. 年度×指標(FY26〜FY30)

単位: $B(特記以外)。FY = 5 月末決算。FY27 = 2026-06〜2027-05。

| 指標 | FY26 | FY27 | FY28 | FY29 | FY30 | 出典 / Tier |
|---|---|---|---|---|---|---|
| OCI 売上: 2025-09 経路(再掲) | 18 | 32 | 73 | 114 | 144 | S1 [Q1 FY26 説明会] 1*/3 |
| OCI 売上: FAM 後の経路(算出: 旧経路 + CreditSights の増額幅) | 18(増額なし) | 34(32 + 2) | 77(73 + 4) | 129(114 + 15) | **166**(144 + 22) | [T2-03][T2-04] 3* |
| OCI 前年比(FAM 後経路、算出) | +77%(会社値、再掲) | +89%(34 ÷ 18 − 1) | +126%(77 ÷ 34 − 1) | +68%(129 ÷ 77 − 1) | +29%(166 ÷ 129 − 1) | 算出。FY28 +126% は CreditSights も記述 |
| OCI 売上: 実績・進捗 | 約 18.1(算出: 3.3 + 4.1 + 4.9 + 5.8) | Q1 のみ 7.4(+121%) | — | — | — | S1・S4・T2-11 |
| FY27 OCI の Q2〜Q4 必要額(算出) | — | 経路 34 なら 26.6(平均 8.9/四半期、FY26 Q2〜Q4 の 14.8 比 +80%)。旧経路 32 なら 24.6(平均 8.2、+66%) | — | — | — | 算出: 34 − 7.4、32 − 7.4、FY26 Q2〜Q4 = 4.1 + 4.9 + 5.8 |
| FY27 の OCI 売上ガイダンス(会社) | — | **欠損**(下記 8 章) | — | — | — | — |
| 総売上 | 約 67.4(逆算、公式値未取得。会社見通し 67) | "at least 90"(+34%)。履歴 約85 → 89 → 90 → at least 90 | 欠損 | 欠損 | **225** | S1、[T2-11] 1*/3* |
| 非 OCI 売上(算出: 総売上 − OCI) | 約 49.3(67.4 − 18.1) | — | — | — | 59(225 − 166) | 算出。FY26→FY30 の年平均 +4.6%(算出: (59 ÷ 49.3)^(1/4) − 1)。AI Database $20B が OCI 内か非 OCI かは未確認 |
| 非 GAAP EPS($): FAM 時点の目標 | **8.00** | **10.65** | 欠損 | 欠損 | **21** | [T2-06] 3*(FY26・27)、[T2-01] 3*(FY30) |
| 非 GAAP EPS($): 実績・ガイダンス | 7.63(一時的投資益込み)/ 6.83(除外) | ガイダンス 8.05(2026-06)→ **8.10**(2026-09) | — | — | — | S1([S5]) 3 |
| EPS: 目標比(算出) | 7.63 ÷ 8.00 − 1 = -4.6%。6.83 基準なら -14.6% | 8.10 ÷ 10.65 − 1 = **-23.9%** | — | — | — | 算出。FAM の EPS 基準(非 GAAP か、希薄化後か)は未確認 |
| 必要 CAGR(算出) | — | FY27 ガイダンス → FY30: 売上 (225 ÷ 90)^(1/3) − 1 = +35.7%、EPS (21 ÷ 8.10)^(1/3) − 1 = +37.4%。FAM 目標 FY27 $10.65 → FY30 $21 なら +25.4% | — | — | — | 算出 |
| capex(総額) | **55.7**(実績、FY25 は 21.2) | **90〜95**(純現金 70 以下。差 20〜25 は顧客前払い等) | 数値なし(会社)。CreditSights は 85(2026-04 時点の予想、再掲 W5) | — | — | S1、[T2-17]、W5 |
| 納入容量(GW) | 1.2 超(Q4 FY26 説明会)。逆算 約 1.16(850 ÷ 0.73) | Q1 のみ 0.85。Q1 見通しは "approaching one gigawatt" | 「FY29 までの 3 年で 10GW 超を確保」(Q3 FY26 発言) | ← 同左 | — | [T2-12][T2-21][T2-22] 3* |
| FCF | -23.7 | Q1 約 -5(-5.4 とする報道あり)。時期の約束なし | 欠損 | 欠損 | 欠損 | S1、[T2-15] |

注: FY26 総売上 67.4 は S1 で capex 比率(82.6%)から逆算した値。公式の FY26 売上は本調査で未取得。

---

## 3. FAM(2025-10-16)の目標と、その後の発言

### 3-1. FAM の目標一覧

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| 総売上 FY30 | $225B、5 年 CAGR 31%。CFO Doug Kehring が提示。事前コンセンサス $198.4B(Reuters/LSEG)または $198.6B(TIKR) | [T2-01][T2-05][T2-08] 3* |
| EPS FY30 | $21(調整後)、CAGR 28%。事前コンセンサス $18.92(Reuters/LSEG)または $18.46(TIKR) | [T2-01][T2-08] 3* |
| EPS FY26・FY27 | $8.00、$10.65。Stifel(Brad Reback、Buy、PT $350)は「前倒しの規模拡大コストで予想をやや下回る」と説明。株価は時間外で下落 | [T2-06] 3* |
| OCI 売上 FY30 | $166B(従来 $144B)。総売上の約 74%(算出: 166 ÷ 225 = 73.8%)。5 年 CAGR 約 75%(Morningstar)。CreditSights は FY28 の成長率を +126% と記述 | [T2-03][T2-04] 3* |
| AI Database / AI データ・プラットフォーム FY30 | $20B(FY25 は $2.4B、FY26 は $3B 想定)。CAGR 53%(算出: (20 ÷ 2.4)^(1/5) − 1 = 52.8%) | [T2-04][T2-08] 3*(2 媒体) |
| 粗利率 | AI インフラ 30〜40%(Magouyrk、"eventually")、エンタープライズ・非 AI 65〜80%。例示: 6 年・1GW・$60B の契約で約 35% | [T2-01][T2-04] 3* |
| RPO(FAM 時点) | $500B 超。うち約 $300B が OpenAI 契約との報道(1 契約)。直近 30 日の新規コミット $65B(Meta $20B 含む、再掲 S1) | [T2-08]、S1 3* |
| アプリケーション(SaaS)の FY30 目標 | **欠損**。FAM の要約に事業別の売上目標は見つからなかった | 8 章 |
| マルチクラウド DB の FY30 目標 | **欠損**(AI Database $20B に含まれるかは未確認) | 8 章 |
| 営業利益率の FY30 目標 | **欠損**。FAM 要約に営業利益率の数値は見つからなかった。粗利率のレンジのみ | 8 章 |
| 市場反応(参考) | 発表日 +3〜4%、翌日 約 -7%(目標への懐疑) | [T2-07][T2-08] 3* |

### 3-2. 営業利益率の代替情報(算出)

会社の営業利益率目標が見つからないため、EPS 目標から逆算した参考値のみ置く。

| 項目 | 値 | 算出 / 注 |
|---|---|---|
| FY30 の純利益(非 GAAP)の目安 | 約 $63B | 21 × 3.0B 株 = 63。希薄化後株数 3,000 百万株は Q1 FY27 の値と記す 1 つの分析(出所特定不可、T4*)。強制転換優先株の転換と ATM で株数は増えうる |
| 売上に対する比率 | 28.0% | 63 ÷ 225。営業利益率ではなく純利益率の目安 |

### 3-3. FAM 後の目標・ガイダンスの更新(時系列)

| 日付 | 場面 | 内容 | 出典 / Tier |
|---|---|---|---|
| 2025-10-16 | FAM | 上表 | 上記 |
| 2025-12-10 | Q2 FY26 | FY27 売上に +$4B(RPO の売上化が早まるため)。FY26 売上 $67B は据置(再掲) | S1 1* |
| 2026-03-10 | Q3 FY26 | FY27 売上 $90B(前回比 約 +$1B)。AI 容量の粗利率 32%。10GW 超の確保を発言(5-3 章) | S1、[T2-21] 1*/3* |
| 2026-06-10 | Q4 FY26 | CFO Maxson: 長期目標(売上 CAGR 31%、EPS CAGR 28%)を「full reconfirmation from my side」と再確認。FY27 EPS $8.05、capex $90〜95B、調達約 $40B | [T2-23] 1*/4* |
| 2026-09-10 | Q1 FY27 | FY27 売上 "at least $90B"(+34%)、非 GAAP EPS $8.10(前回 $8.05)。FY30 目標の再確認発言は**確認できず** | [T2-11][T2-15] 1*/3* |
| 2026-09-10 | Q1 FY27 | CFO: 新規 RPO は FY28 以降まで capex にも売上にも影響しない(要約) | [T2-17] 3* |

要点: FY27 の売上ガイダンスは $85B 前後 → $89B → $90B → "at least $90B" と段階的に上がったが、EPS は FAM の $10.65 から $8.10 に下がった(目標とガイダンスで基準が同じかは未確認)。

---

## 4. RPO の中身

### 4-1. RPO の推移(再掲 + 新規)

| 期末 | RPO | 前期比 | 新規 AI 契約(会社発言) | 出典 / Tier |
|---|---|---|---|---|
| Q4 FY25(2025-05) | 約 $138B(逆算) | — | — | S1 |
| Q1 FY26(2025-08) | $455B | +$317B | OpenAI、xAI、Meta、NVIDIA、AMD 等 | S1 |
| FAM(2025-10-16 時点) | $500B 超 | — | 直近 30 日で $65B(うち Meta $20B) | [T2-08]、S1 |
| Q2 FY26(2025-11) | $523B | +$68B | Meta、NVIDIA ほか | S1 |
| Q3 FY26(2026-02) | $553B | +$29B | $29B 超(BYOH・前払い) | [T2-21]、S1 |
| Q4 FY26(2026-05) | $638B | +$85B | $67B(大半が BYOH・前払い) | [T2-22]、S1 |
| Q1 FY27(2026-08) | **$664B** | +$26B(前年比 +$209B) | $30B 超(追加の資本は不要と説明) | [T2-11][T2-12] |

- RPO ÷ FY27 売上ガイダンス = 664 ÷ 90 = 7.4 倍(算出)。
- 前払い・顧客提供ハード(BYOH)の累計: $75B(2026-06 のプレス、再掲 S1)。Q1 FY27 の 10-Q: 重要な金融要素を含む前払い $11.4B(再掲 W5)。
- 第三者のコンセンサス: Q1 FY27 の RPO 予想 約 $630.6B(1 媒体)に対し実績 $664B。[T2-18] 3*

### 4-2. 売上化の時期

| 区分 | Q4 FY26(2026-05-31) | Q1 FY27(2026-08-31) | 金額(Q1 FY27、算出: 664 × 比率) | 出典 / Tier |
|---|---|---|---|---|
| 12 か月以内 | 12%(約 $76.6B、算出) | **約 13%** | **$86.3B** | [T2-09][T2-10]、W5 1* |
| 13〜36 か月 | 34%(約 $216.9B、算出) | **37%** | **$245.7B**(24 か月で年平均 $122.8B) | [T2-09] 1* |
| 36 か月以内の合計 | 46%(約 $293.5B) | **50%**(13 + 37) | **$332.0B** | 会社発言「約半分が 36 か月以内」と整合 [T2-11][T2-10] |
| 37〜60 か月 | 欠損(Q4 は 37 か月以降 54%) | **34%** | **$225.8B**(24 か月で年平均 $112.9B) | [T2-09] 1*(1 回の検索要約のみ) |
| 60 か月超(算出: 100 − 13 − 37 − 34) | 欠損 | 16% | $106.2B | 算出 |
| 37 か月以降の合計(算出) | 54% | 50% | $332.0B | 算出 |

- 36 か月以内の比率の推移: 約 35%(前年同期、FinanceFeeds の記述)→ 46%(Q4 FY26)→ 50%(Q1 FY27)。[T2-10] 3*
- 12 か月以内の金額の増加: $86.3B − $76.6B = +$9.7B(算出、Q4 FY26 → Q1 FY27)。36 か月以内は +$38.5B(算出: 332.0 − 293.5)。
- 窓の対応(算出): 12 か月以内 = 2026-09〜2027-08、13〜36 か月 = 2027-09〜2029-08、37〜60 か月 = 2029-09〜2031-08。Oracle の年度(5 月末)とは 3 か月ずれる。
- 参考(算出): FAM 後の OCI 経路の FY28・FY29 平均 = (77 + 129) ÷ 2 = $103B。13〜36 か月の RPO の年平均 $122.8B は OCI 以外の契約を含み、窓も異なるため、直接の比較はできない。

### 4-3. 顧客別

| 顧客 | 金額・規模 | 期間・開始 | 備考 | 出典 / Tier |
|---|---|---|---|---|
| OpenAI | 約 $300B(WSJ 報道)。会社は金額を非開示。RPO に対し 300 ÷ 664 = 約 45%(算出) | 約 5 年、2027 年開始(WSJ)。容量 4.5GW(OpenAI が 2025-07 に確認) | S&P は「半分近く」、BofA は 2026-06 時点で $638B の「半分超」と推定(再掲)。会社の比率開示は未確認 | S1、W5、[T2-11] 3 |
| Meta | $20B(FAM、Magouyrk 発言) | 期間は欠損 | 2026-09 の RPO 貢献者として名前が挙がる(金額なし) | S1、W5 3 |
| xAI(SpaceX 傘下とする報道あり) | 欠損 | 欠損 | Q1 FY26 で「数十億ドル規模の契約」と報道(再掲 W5) | W5 3 |
| NVIDIA | 欠損 | 欠損 | 顧客として名指し(Catz、2025-09-09) | S1 |
| AMD | 欠損 | 欠損 | 顧客として名指し。別に Oracle が MI450 を購入する関係(5-5 章) | S1、[T2-20] |
| その他 | 欠損。2025-09〜10 の約 30 日で $65B の新規 AI 契約(内訳非開示) | — | Q4 FY26 の GPU 更新対象は 59 顧客・35,000 GPU(再掲) | S1、W5 |
| OpenAI 以外の合計 | 算出: 664 − 300 = 約 $364B。ただし $300B 全額が RPO 内という前提 | — | 会社の説明は「OpenAI 以外は過去 1 年で 2 倍超」(1 媒体の要約、金額非開示、公式資料では未確認) | [T2-22 検索 #22 の要約] 4* |

### 4-4. 契約条件(再掲 + 新規)

- 契約期間の例示: 6 年・1GW・$60B(粗利率 約 35%、年 $10M/MW)。OpenAI は約 5 年。[T2-01]、R7 3*
- 資金負担: 大型 AI 契約の大半が顧客の前払いまたは BYOH。Q1 FY27 の $30B 超は「Oracle の追加資本を必要としない」(Magouyrk/Maxson)。[T2-11][T2-12] 1*/3*
- take-or-pay、解約条項は公開情報なし(再掲 W5)。

---

## 5. 容量

### 5-1. 四半期ごとの納入

| 期間 | 納入容量 | GPU | 備考 | 出典 / Tier |
|---|---|---|---|---|
| FY26 通期 | **1.2GW 超**("delivered more than 1.2 gigawatts to customers") | 欠損 | 逆算: 850 ÷ 0.73 = 1,164MW(Q1 FY27 の「前年度の 73%」から)。1.2GW 超とやや食い違う | Q4 FY26 説明会の要約(検索 #19)、[T2-12] 3* |
| Q1 FY26〜Q2 FY26 | 欠損。残差は約 480〜520MW(算出: 1,164 または 1,200 − 400 − 283) | 欠損 | 四半期の公式値は未取得 | 算出 |
| Q3 FY26(〜2026-02) | **400MW 超**。委託容量の 90% を予定どおりまたは前倒しで納入 | 欠損 | DCD は「stood up 400MW」と表記(納入と稼働の区別は未確認) | [T2-21] 3* |
| Q4 FY26(〜2026-05) | 約 283MW(算出: 850 ÷ 3)。"almost three times" なので実際はやや多い | 欠損 | 公式の Q4 単独値は未取得 | 算出 |
| Q1 FY27 見通し(Q4 説明会) | "approaching one gigawatt" | — | 見通し | Q4 FY26 要約(検索 #19) 3* |
| Q1 FY27(〜2026-08) | **850MW**(見通し比 85%、算出: 850 ÷ 1,000) | **30 万基超** | Magouyrk: "almost three times what we delivered in all of Q4, and 73 percent of the total capacity delivered last fiscal year" | [T2-12][T2-13] 3* |
| 日当たり(算出) | 850MW ÷ 92 日 = 9.2MW/日(再掲 R7) | — | 納入の定義(施設ベースか IT ベースか)は未確認 | R7 |
| Q2 FY27 以降の見通し | **欠損**(数値の見通しは見つからず) | — | Magouyrk: 「1GW のサイトは 1 月に納入を始めても一度に 1GW にはならず、多数の四半期に分けて立ち上がる」(拠点名なし、要約) | 検索 #8 の要約 3* |

### 5-2. 拠点別

| 拠点 | 開発・資金 | 計画容量 | 最新の会社発言・状況(日付) | 稼働時期の見通し | 出典 / Tier |
|---|---|---|---|---|---|
| Abilene(TX) | Crusoe | キャンパス 1.2GW(再掲 S3)。Oracle 発言では 8 棟 | Q4 FY26(2026-06-10): 42% 納入、次の 90 日で 35% 追加、残りは次の四半期。Q1 FY27(2026-09-10): 8 棟中 6 棟・618MW・全体の 75% を顧客に納入(拠点名は要約に無く、Abilene と推定) | 全棟は 2026 年後半〜2027 年初(再掲 R7)。Epoch: IT 電力 421MW(2026-07)、843MW(2026 Q4 見込み) | Q4 要約(検索 #19)、[T2-13][T2-24] 3* |
| Shackelford County(TX) | Vantage、VoltaGrid の敷地内ガス | IT 1.4GW(再掲 S3)。Cleanview は総電力 2.58GW | Q4 FY26: 115MW の電力が予定より 1 か月以上早く通電、**顧客納入は CY2027 上期** | 全体は 2028 Q4(Epoch)〜2029(Baxtel) | Q4 要約(検索 #19) 3*、S3 |
| Doña Ana County / Project Jupiter(NM) | STACK/BorderPlex、Blue Owl 傘下とする報道あり。Oracle は 18 年リースのテナント(再掲 S3) | 2.45GW(Bloomberg)。Bloom 燃料電池 最大 2.5GW | Q1 FY27(2026-09-10): Magouyrk「建設は計画どおり、大気許可を Bloom の燃料電池で対応中」、NM と WI は FY27 の売上・利益見通しに影響しない。Maxson「FY27 見通しに織り込んだスケジュールに対して遅延と考える材料は今のところない」。2026-09-24: Oracle が force majeure 通知(Bloomberg) | 目標は 2028 開業。SemiAnalysis(第三者推計)は 2029 に遅延。ガスパイプラインは 2026-08-15 → 2027-02-01 に延期(FERC 提出書類、再掲 S3) | [T2-16][T2-24]、S3 3* |
| Port Washington(WI) | Vantage | 約 1GW(別報 1.3GW)、4 棟 | Q1 FY27: Wisconsin の遅延について Magouyrk は FY27 見通しに影響しないと回答。拠点別の稼働時期の更新は**欠損** | 完成は 2028 とする報道(再掲 S3) | [T2-16]、S3 3* |
| Saline Township(MI) | Related Digital、DTE が電力 100% | 「1GW 超」(S3)、契約電力 1.38GW(S1 の別報) | 本調査では拠点別の新規情報は**取得できず**(再掲のみ) | 欠損 | S3、S1 3 |
| Lordstown(OH) | SoftBank(旧 Foxconn 工場) | 欠損 | OpenAI は 2025-09 に「2026 年稼働予定」と発表(再掲)。Oracle との直接関係は未確認 | 欠損 | S3 3 |
| Milam County(TX) | SB Energy(SoftBank 子会社) | 1.2GW | Oracle が直接リースするかは未確認(再掲) | Epoch: 2028 Q4 | S3 3 |
| Salt Lake City 近郊 | 不明 | 欠損 | トラック輸送のガスで 1 年超稼働(Bloomberg、再掲) | 稼働中 | S3 3 |
| OpenAI 向け追加分 | — | 4.5GW(OpenAI が 2025-07 に確認) | Oracle は 2026-03 に「追加 4.5GW のリース手配は完了」と反論(Bloomberg の Abilene 600MW 拡張中止報道に対し、再掲) | — | S1・S3 3 |

Abilene の容量比較(算出): 618MW ÷ 0.75 = 約 824MW。これは「Oracle が数える Abilene の 8 棟分の総量」と読めるが、拠点名が要約に無いため確認できない。

### 5-3. 「今後 3 年で 10GW 超」の定義と時点

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| 発言時点 | Q3 FY26 説明会(2026-03-10)、Magouyrk | [T2-21] 3* |
| 発言内容(要約) | 「今後 3 年間で稼働する **10GW 超の電力とデータセンター容量**を確保した」。大半がパートナー経由 | [T2-21] 3* |
| 資金負担 | **90% 超**をパートナー(開発事業者・貸し手)が資金負担。残りの確保作業は「今月中」に完了予定と発言 | [T2-21] 3* |
| 期間 | 2026-03 から 3 年 = 2029-03 まで(算出)。FY では FY29 末(2029-05)にほぼ一致 | 算出 |
| 年平均(算出) | 10GW ÷ 3 年 = 3.3GW/年。FY26 の納入 約 1.2GW、Q1 FY27 の 0.85GW との対比 | 算出 |
| 定義の確認 | DCD の見出しは "secured 10GW of power"、トランスクリプト要約は "power and data center capacity"。契約の種類(電力契約、リース契約、土地)の内訳は**欠損**。10-K・10-Q の公式値も**欠損** | [T2-21]、R7 |
| Q1 FY27 での更新 | **確認できず**(10GW の再確認・増減の発言なし) | 検索 #5〜#9 |
| Bloom Energy | 初期 1.2GW・最大 2.8GW の燃料電池コミット(2026-04 報道、再掲) | R7 3 |

### 5-4. capex と資金(FY27・FY28)

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| FY26 capex | $55.7B(実績)。FY25 は $21.2B | S1 3 |
| FY27 capex(会社見通し) | **総額 $90〜95B**、**純現金 capex は $70B 以下**(顧客前払い等 $20〜25B を除く、算出: 90 − 70、95 − 70)。Q1 FY27 でも維持 | [T2-17]、S1 3* |
| Q1 FY27 実績 | capex 約 $28〜28.5B(28.499 とする報道あり)、営業 CF $23.1B、FCF 約 -$5B(-$5.4B とする報道あり) | [T2-15][T2-22] 3* |
| FY27 の倍率(算出) | 90 ÷ 55.7 = 1.62 倍 〜 95 ÷ 55.7 = 1.71 倍 | 算出 |
| FY28 capex | **数値なし**。要約: 経営陣は FY27・FY28 を capex のピーク年と位置づけたが、減少の時期・額は示さず。CFO: "next several quarters will show what it could look like" | [T2-17] 3* |
| FY28 の第三者予想 | $85B(CreditSights、2026-04 時点、再掲 W5)。Q4 FY26 の FY27 見通し更新より前の予想 | W5 3 |
| FCF 黒字化 | 時期は示さず。「立ち上がれば強い FCF を生む設計」(Maxson) | [T2-15][T2-17] 3* |
| 調達 | FY27 の調達計画 約 $40B(債券 + 株式、うち $20B の ATM は Q1 FY27 に完了)。2026 暦年は追加債券なし(再掲 S1) | S1 |
| 資金の出し手の補足 | 「サプライヤー金融、顧客前払い、BYOH により、成長の資金すべてを Oracle が負担しない構造」(要約) | [T2-17] 3* |

### 5-5. GPU 調達・価格・稼働

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| AMD MI450 | Oracle と AMD の発表(2025-10-14): OCI が **50,000 基の MI450** による公開 AI スーパークラスタを **2026 暦年 Q3 から**初期展開、2027 年以降に拡大。AMD Helios ラック、次世代 EPYC、Pensando ネットワーク。「公開で利用できる初のハイパースケーラーの AI スーパークラスタ」と Oracle が主張 | [T2-20] 1*/3* |
| MI450 の稼働実績 | **欠損**(Q1 FY27 の納入 30 万基超の内訳に MI450 が含まれるかは不明) | — |
| NVIDIA | Oracle の NVIDIA GPU 調達契約(数量・金額・世代)は**欠損**。Zettascale10 は NVIDIA GPU 最大 80 万基を目標(再掲 R2)、Abilene の最初のクラスタは約 20 万基(Magouyrk、再掲 W5)。Q4 FY26 の GPU 更新対象は 35,000 基・59 顧客 | R2、W5 |
| 納入 GPU | Q1 FY27: 30 万基超(850MW)。算出: 850MW ÷ 300,000 基 = 約 2.8kW/基(施設電力ベースの粗い目安、世代混在) | [T2-12] 3*。算出 |
| 稼働率 | Q4 FY26: 97.5%(グローバル、ポッドキャスト要約 T4*)、Q1 FY27: **97.9%** | 検索 #19(T4*)、[T2-12][T2-13] 3* |
| 更新時の価格 | Q4 FY26: 更新対象 35,000 基・59 顧客のうち、顧客の 49% が GPU の 92% を更新(再掲)。Q1 FY27: 更新対象はすべて **従来契約比 +20% の価格で更新または再販**、大半は 4 年以上前の GPU | [T2-13] 3* |
| 業界の部材制約(参考) | TrendForce: NVIDIA の高性能 GPU 出荷に占める Rubin は 2026 年に 22%(従来 29%)に低下、HBM4 の検証と電力・液冷の要件が背景。DRAM の逼迫は 2027 年、2028 年まで続くとの予測。Oracle 固有の調達数値ではない | [T2-25] 3* |

---

## 6. Q1 FY27 説明会(2026-09-10)の需給・納入・価格の発言

| テーマ | 発言・事実(要約が主、引用は検索要約中の英文) | 話者 | 出典 / Tier |
|---|---|---|---|
| 納入の加速 | 「Q1 に 850MW・30 万基超の GPU を納入。Q4 の約 3 倍、前年度納入量の 73%」("almost three times what we delivered in all of Q4, and 73 percent of the total capacity delivered last fiscal year") | Magouyrk | [T2-12][T2-13] 3* |
| 稼働率 | GPU 稼働率 97.9% | 経営陣 | [T2-12] 3* |
| 価格 | 更新・再販の対象 GPU はすべて前契約比 +20%(Zacks 経由) | Magouyrk | [T2-13] 3* |
| 制約の所在 | 「制約は時間とともに GPU とファブから、電力生成とデータセンターへ移った。世界は広く需要は大きい」(要約)。Oracle はあらゆる手段で容量を立ち上げていると発言 | Magouyrk | [T2-12] 3* |
| 需要の強さ | 追加の AI 契約 $30B 超を、Oracle の追加資本なしで契約。CFO の一語は "acceleration" | Magouyrk、Maxson | [T2-11][T2-12] 1*/3* |
| 「需要が供給を上回る」の逐語 | Q1 FY27 の要約には**見つからず**。Q3 FY26 については「Magouyrk が需要は供給を上回っていると述べた」という要約が 1 件(DCD 系の検索結果) | — | [T2-21] 3* |
| 拠点の遅延 | Mizuho の質問に対し、NM と WI は FY27 の売上・利益見通しに影響しない(Magouyrk)。「NM を含む他の拠点が見通しのスケジュールより遅れると考える材料は今のところない」(Maxson) | Magouyrk、Maxson | [T2-16] 3* |
| 売上化 | RPO の約半分が今後 36 か月で売上化。新規 RPO は FY28 以降まで capex にも売上にも影響しない | Maxson | [T2-11][T2-17] 1*/3* |
| ガイダンス | FY27 売上 "at least $90B"(+34%)、非 GAAP EPS $8.10、capex $90〜95B(純現金 $70B 以下) | Maxson | [T2-11][T2-17] |
| 企業向け AI の需要の根拠 | 「企業顧客のほぼ全員が自社のプライベートデータで AI に推論させたい」(プレス、再掲 S1) | プレス | S1 1 |

---

## 7. 食い違い(どちらも採らず併記)

| # | 論点 | 出典 A | 出典 B | 備考 |
|---|---|---|---|---|
| 1 | RPO の 12 か月以内の比率(Q1 FY27) | 10-Q 要約: 13%($86.3B) | S1 の開示変化欄: 「12 か月内 約 33%」(ブログ T4 経由) | 10-Q 要約の 13% が Q4 FY26 の 12% と連続。S1 の 33% は転記ミスの可能性があるが確認できていない |
| 2 | FAM 前のコンセンサス | Reuters/LSEG: 売上 $198.4B、EPS $18.92 | TIKR: 売上 $198.6B、EPS $18.46 | 出所と基準日が違う可能性 |
| 3 | FAM の EPS 目標と現ガイダンス | FAM: FY26 $8.00、FY27 $10.65(Stifel/TheFly) | 実績 FY26 $7.63(除外 $6.83)、FY27 ガイダンス $8.10 | TheFly の数値の基準(非 GAAP か GAAP か、株数)が未確認。1 媒体 |
| 4 | FY26 の納入容量 | Q4 FY26 説明会: 1.2GW 超 | 逆算(850 ÷ 0.73): 1.164GW | 丸めまたは「納入」の定義差 |
| 5 | Q1 FY27 の納入 | Q4 説明会の見通し: "approaching one gigawatt" | 実績 850MW | 見通しと実績の差(85%) |
| 6 | Abilene の容量 | キャンパス 1.2GW(施設ベース) | Oracle 発言の 618MW = 75%(逆算 824MW)。Epoch: IT 421MW(2026-07)、843MW(2026 Q4 見込み) | 定義が異なる。Q4 説明会の「42% + 35% = 77%」と Q1 の「75%」も近いが一致しない |
| 7 | Abilene の拡張 | Bloomberg: 600MW 拡張を中止 | Oracle: 誤り。OpenAI: 他拠点に振り向けた(再掲) | 未解決 |
| 8 | Jupiter の開業時期 | Oracle/Bloomberg: 2028 | SemiAnalysis: 2029 | 第三者推計。会社は FY27 に影響なしと説明 |
| 9 | Jupiter の売上影響 | Morningstar の見出し: force majeure は「$25B の売上遅延の可能性」を示唆(本文未読) | Pluang(Seeking Alpha ノートの要約): $25B は「売上リスク」で、遅延を予想するものではない | 本文未読。金額の算定根拠は不明 |
| 10 | OpenAI の RPO 比率 | S&P: 「半分近く」 | BofA: $638B の「半分超」(2026-06 推定)。算出: 300 ÷ 664 = 45% | 分子の $300B は報道値で会社は非開示 |
| 11 | 10GW の中身 | DCD 見出し: 10GW の「電力」 | トランスクリプト要約: 「電力とデータセンター容量」 | 契約種別の内訳が欠損 |
| 12 | 稼働率 | Q4 FY26: 97.5%(T4*) | Q1 FY27: 97.9% | 時点が異なる。Q4 値は T4 |
| 13 | Q1 FY27 の capex・FCF | $28.0B、FCF -$5B | $28.499B、FCF -$5.4B | 丸めまたは定義差(再掲 S1) |
| 14 | Q1 FY27 の RPO 予想 | 約 $630.6B(1 媒体) | 別の媒体: 事前予想は $600B 台前半 | 本調査で一致を確認できず |
| 15 | 「需要が供給を上回る」 | Q3 FY26: 要約に "outpacing supply" | Q1 FY27: 逐語を確認できず。稼働率と +20% の更新価格が間接証拠 | 逐語は原文で要確認 |

---

## 8. 欠損と検索語

| # | 欠損項目 | 試した検索語(要旨) |
|---|---|---|
| 1 | FAM の事業別目標(アプリ・マルチクラウド DB の FY30 売上) | 検索 #1、#2、#3、#23: "fiscal 2030 targets ... applications revenue ... multicloud database"。AI Database $20B のみ確認 |
| 2 | FAM の FY30 営業利益率目標 | 検索 #3、#23: "FY30 targets analyst day operating margin non-GAAP"。粗利率レンジのみ |
| 3 | FAM のスライド原本、FY27〜FY29 の総売上経路 | 検索 #1〜#3。原本 PDF(S1 の S9)は未読 |
| 4 | FAM 後の FY27・FY28 OCI 売上の会社更新値 | 検索 #5、#18、#26: "FY27 OCI revenue guidance"。更新値は見つからず |
| 5 | Q3 FY26・Q1 FY27 での FY30 目標の再確認 | 検索 #5、#26: "reaffirm fiscal 2030 targets"。Q4 FY26 のみ確認 |
| 6 | RPO の OpenAI・Meta・xAI・NVIDIA・AMD 別金額、OpenAI 以外の金額 | 検索 #11、#22: "RPO breakdown OpenAI Meta xAI contract value non-OpenAI" |
| 7 | 四半期ごとの総受注(RPO の純増ではなく総額) | 検索 #11。純増と新規 AI 契約の公表額のみ |
| 8 | 四半期ごとの GPU 納入数(Q4 FY26 以前) | 検索 #19: "Q4 FY26 capacity delivered megawatts GPUs delivered" |
| 9 | Saline Township・Port Washington・Lordstown・Milam County の最新の稼働時期 | 検索 #20: "Shackelford Michigan Wisconsin New Mexico sites delivery schedule"。WI・NM の遅延質問の回答のみ |
| 10 | 10GW の契約種別の内訳、10-K の公式値 | 検索 #17: "secured 10 gigawatts ... definition" |
| 11 | NVIDIA の調達契約(数量・金額)、Vera Rubin の割当 | 検索 #13: "Oracle NVIDIA GPU purchase 400,000 GB200 ... Zettascale10"、検索 #24: "Oracle procurement Nvidia GPUs GB300 Rubin allocation supplier financing" |
| 12 | MI450 の稼働状況 | 検索 #12 は 2025-10 の発表のみ |
| 13 | Q1 FY27 トランスクリプトの逐語(需給、価格) | 検索 #5〜#9、#15、#16、#25。Fool・Benzinga・stockanalysis 等のページは見つかったが本文は読めず、要約のみ |
| 14 | Morningstar の force majeure 記事の本文 | 検索 #21。見出しのみ |
| 15 | 契約の take-or-pay・解約条項 | 検索せず(再掲 W5 のとおり公開情報なし) |

### 検索一覧(26 回)

| # | 検索語(要旨) | 用途 |
|---|---|---|
| 1 | FAM 2025 fiscal 2030 targets $225B $21 OCI $166B applications multicloud operating margin | FAM 目標 |
| 2 | analyst meeting Kehring slides ... OCI path FY26 $18B ... FY29 $114B(extended) | OCI 経路 |
| 3 | FY30 targets analyst day operating margin non-GAAP ... segments | 営業利益率・事業別 |
| 4 | Stifel fiscal 2027 EPS $10.65 fiscal 2026 EPS $8 | EPS 目標 |
| 5 | Q1 FY27 transcript Maxson fiscal 2030 targets reiterate OCI $90B RPO 36 months(extended) | 目標の再確認 |
| 6 | Magouyrk Q1 2027 "850 megawatts" ... | 納入(無関係な結果) |
| 7 | Q1 FY27 call highlights 850MW 300,000 GPUs demand outstrips supply | 納入・需給 |
| 8 | fool.com Q1 2027 transcript supply demand gigawatts next three years(extended) | 納入・拠点 |
| 9 | "six of the eight" 618 megawatts 75% gigawatt site January | 拠点 |
| 10 | 10-Q 2026-08-31 RPO next 12 months 13% 13 to 36 months(extended) | RPO 売上化 |
| 11 | RPO $664B breakdown OpenAI Meta xAI non-OpenAI doubled(extended) | RPO 内訳 |
| 12 | OCI AMD MI450 50,000 GPUs Q3 2026 NVIDIA GB300 Vera Rubin | GPU 調達 |
| 13 | NVIDIA 400,000 GB200 Abilene Zettascale10 | GPU 調達(結果なし) |
| 14 | fiscal 2028 capex outlook Maxson Q1 FY27(extended) | capex |
| 15 | "Oracle Q1 Earnings Call Centers on AI Capacity and Raised Outlook" | 容量・見通し |
| 16 | marketbeat Q1 highlights demand supply GPU renewals 20% | 需給・価格 |
| 17 | Q3 FY26 call 10 gigawatts 400 megawatts 90% funded by partners | 10GW |
| 18 | Q4 FY26 call reaffirm FY30 targets FY27 OCI(extended) | 再確認 |
| 19 | Q4 FY26 capacity delivered MW Abilene 97.5% | Q4 の納入・拠点 |
| 20 | Sept 2026 call Shackelford Michigan Wisconsin New Mexico(extended) | 拠点・遅延 |
| 21 | Morningstar force majeure $25B revenue delay | Jupiter の影響 |
| 22 | Q1 FY27 RPO contributors Meta SpaceX xAI NVIDIA non-OpenAI | RPO 顧客 |
| 23 | 2025 FAM applications growth SaaS FY30 operating margin(extended) | アプリ・利益率 |
| 24 | Oracle procurement Nvidia GB300 Rubin supplier financing HBM | 調達(Oracle 固有情報なし) |
| 25 | Q1 2027 call demand exceed supply capacity constrained(extended) | 需給 |
| 26 | FY30 targets on track reaffirmed Q3 FY26 Q1 FY27(extended) | 再確認 |

---

## 9. 出典一覧

| ID | 媒体 / 内容 | URL | 日付 | Tier |
|---|---|---|---|---|
| T2-01 | Reuters(TradingView)「Oracle expects cloud sales of $166 billion by 2030」 | https://de.tradingview.com/news/reuters.com%2C2025%3Anewsml_L6N3VX11P%3A0-oracle-expects-cloud-sales-of-166-billion-by-2030-as-business-expands | 2025-10-16 | 3* |
| T2-02 | Reuters(Investing.com) | https://www.investing.com/news/stock-market-news/oracle-expects-cloud-infrastructure-revenue-to-be-166-billion-in-fy30-4292932 | 2025-10-16 | 3* |
| T2-03 | Morningstar「Another OCI Revenue Outlook Raise Shows Ability to Capture AI Momentum」 | https://www.morningstar.com/stocks/oracle-another-oci-revenue-outlook-raise-shows-ability-capture-ai-momentum | 2025-10 | 3* |
| T2-04 | CreditSights「Top 10 Takeaways from 2025 Analyst Meeting」(有料、プレビューの要約) | https://know.creditsights.com/insights/oracle-top-10-takeaways-from-2025-analyst-meeting/ | 2025-10 | 3* |
| T2-05 | Cloud Wars「Oracle on Fire! FY30 Rev. $225B!」 | https://cloudwars.com/cloud-wars-minute/oracle-on-fire-fy30-rev-225b/ | 2025-10 | 3* |
| T2-06 | TheFly(TipRanks)「Oracle likely to consolidate recent gains, says Stifel」 | https://www.tipranks.com/news/the-fly/oracle-likely-to-consolidate-recent-gains-says-stifel-thefly | 2025-10 | 3* |
| T2-07 | Yahoo Finance「Oracle stock jumps 4% as company says cloud revenue will skyrocket to $166B by 2030」 | https://finance.yahoo.com/news/oracle-stock-jumps-4-as-company-says-cloud-revenue-will-skyrocket-to-166b-by-2030-182501729.html | 2025-10-16 | 3* |
| T2-08 | iTiger / Webull / TIKR(FAM 後の反応、$20B AI Database、事前コンセンサス) | https://www.itiger.com/news/1178567425 、https://www.webull.com/news/13713627679100928 、https://www.tikr.com/blog/nyse-oracle-stock-falls-over-2-despite-strong-long-term-outlook | 2025-10 | 3*/4* |
| T2-09 | Oracle Form 10-Q(2026-08-31) | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm | 2026-09 | 1*(検索要約のみ) |
| T2-10 | FinanceFeeds「Oracle Q1: Half of $664B RPO Expected as Revenue in 3 Years」 | https://financefeeds.com/oracle-q1-fy27-rpo-664-billion-36-month-conversion/ | 2026-09 | 3* |
| T2-11 | Motley Fool Q1 FY27 決算説明会トランスクリプト(他に Benzinga、stockanalysis、Yahoo 掲載) | https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/ | 2026-09-10/11 | 1*(本文未読) |
| T2-12 | DCD「Oracle delivered 300,000 GPUs in Q1 FY2027」 | https://www.datacenterdynamics.com/en/news/oracle-delivered-300000-gpus-in-q1-fy2027/ | 2026-09 | 3* |
| T2-13 | MarketBeat「Transcript: Oracle Q1 earnings call highlights」、Zacks(GPU 更新 +20%) | https://www.marketbeat.com/instant-alerts/transcript-oracle-q1-earnings-call-highlights-2026-09-10/ | 2026-09-10 | 3* |
| T2-14 | TradingKey Q1 FY27 要約(AI 要約を含む) | https://www.tradingkey.com/news/transcripts/262162053-tradingkey | 2026-09 | 4* |
| T2-15 | Yahoo「Oracle Q1 Earnings Call Centers on AI Capacity and Raised Outlook」 | https://finance.yahoo.com/technology/ai/articles/oracle-q1-earnings-call-centers-140000080.html | 2026-09 | 3* |
| T2-16 | Yahoo / GuruFocus「Oracle Corp (ORCL) (Q1 2027) Earnings Call Highlights」(NM・WI の質疑) | https://finance.yahoo.com/markets/stocks/articles/oracle-corp-orcl-q1-2027-090101356.html | 2026-09 | 3* |
| T2-17 | scanx「Oracle CFO reaffirms $90B-$95B FY27 capex guidance」ほか(FY28 の言及) | https://scanx.trade/stock-market-news/companies/oracle-q1fy27-results-analyst-cites-compute-capital-constraints-ahead/50321457 | 2026-09 | 3*/4* |
| T2-18 | Motley Fool「Forget Oracle's Stock Price Swings. Its Backlog-to-Revenue Ratio Tells the Real Story.」 | https://www.fool.com/investing/2026/09/17/forget-oracles-stock-price-swings-its-backlog-to-r/ | 2026-09-17 | 3* |
| T2-19 | Crypto Briefing「Oracle books over $30B in AI cloud contracts in Q1」 | https://cryptobriefing.com/oracle-30b-ai-cloud-contracts-q1/ | 2026-09 | 3* |
| T2-20 | Oracle / AMD 発表「Oracle and AMD expand partnership」、DCD | https://oracle.com/news/announcement/ai-world-oracle-and-amd-expand-partnership-to-help-customers-achieve-next-generation-ai-scale-2025-10-14 、https://www.datacenterdynamics.com/en/news/oracle-to-deploy-cluster-of-50000-amd-instinct-mi450-gpus/ | 2025-10-14 | 1*/3* |
| T2-21 | DCD「Oracle stood up 400MW ... secured 10GW of power for the next three years」、MarketBeat Q3 highlights、Yahoo Q3 サマリー | https://datacenterdynamics.com/en/news/oracle-stood-up-400mw-of-data-center-capacity-in-latest-quarter-has-secured-10gw-of-power-for-the-next-three-years/ 、https://www.marketbeat.com/instant-alerts/oracle-q3-earnings-call-highlights-2026-03-10/ | 2026-03-10 | 3* |
| T2-22 | Nasdaq「Oracle Q4 earnings call highlights」、Fool Q4 トランスクリプト(Abilene 42%・Shackelford 115MW・1.2GW は検索 #19 の要約) | https://www.nasdaq.com/articles/oracle-q4-earnings-call-highlights 、https://www.fool.com/earnings/call-transcripts/2026/06/10/oracle-orcl-q4-2026-earnings-call-transcript/ | 2026-06-10 | 1*/3* |
| T2-23 | Q4 FY26: CFO の長期目標の再確認(Fool トランスクリプト、TIKR) | https://www.fool.com/earnings/call-transcripts/2026/06/10/oracle-orcl-q4-2026-earnings-call-transcript/ 、https://www.tikr.com/blog/oracle-stock-q4-2026-beats-estimates-as-oci-revenue-surges-93-year-over-year | 2026-06-10 | 1*/4* |
| T2-24 | CNBC「Oracle sends 'force majeure' notice」、Morningstar(見出しのみ)、Seeking Alpha、SemiAnalysis、Pluang | https://www.cnbc.com/2026/09/24/oracle-data-center-force-majeure.html 、https://www.morningstar.com/stocks/oracle-data-center-force-majeure-implies-possibility-25-bln-revenue-delay 、https://seekingalpha.com/article/4949492-wall-street-lunch-oracle-draws-line-on-ai-data-center-delays 、https://newsletter.semianalysis.com/p/stop-saying-half-of-2026-us-datacenter 、https://pluang.com/en/news-feed/oracle-beli-saat-pasar-salah-harga-risiko-penundaan | 2026-09-24 〜 | 3*/4* |
| T2-25 | TrendForce(Guru3D 経由)「Nvidia Rubin GPUs face delays due to memory shortages」 | https://www.guru3d.com/story/trendforce-nvidia-rubin-gpus-face-delays-due-to-memory-shortages/ | 2026 | 3* |
| 既存 | S1 `research/S1_management_scenario.md`、S3 `research/S3_scuttlebutt.md`、R2 `research2/R2_products_5w1h.md`、R7 `research2/R7_capital_power.md`、W5 `research3/W5_oracle_ai_economics.md`(いずれも /tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/ 配下) | — | — | 再掲 |
