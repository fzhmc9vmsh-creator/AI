# W1: クラウド事業の設備投資と利益率の時系列(AWS・Google Cloud・Microsoft)

- 作成日: 2026-10-12(各表の「時点」欄がデータ基準時点)
- 目的: 「設備投資先行型のクラウドが高収益化した経緯」の数値表。事実・数値・出典の整理のみ。投資判断・推奨は含まない。
- 取得手段: WebSearch のみ(20 回、上限に到達して終了)。WebFetch は未使用。
- **全数値は検索結果の要約経由で、原本(10-K、10-Q、決算資料)は未読。** そのため Tier はすべて * 付き。
- Tier 凡例: 1* = 会社開示(10-K・決算資料・決算説明会。要約経由) / 3* = 報道・集計サイト・アナリスト / 4* = ブログ・個人記事
- 「(算出)」は自分で計算した値。式を併記した。丸め値(「約」「≈」)から計算した値は丸めによる誤差を含む。
- 既存調査との重複は再掲に留めた(Oracle・Meta・CoreWeave・Yardeni は既存 S3/S4 の記載を参照。今回は再検索していない)。

---

## 0. 要約(事実のみ、10 行以内)

1. AWS 売上は 2018 年 ≈$25.7B(営業利益 $7.3B、率 28.4%(算出))から 2024 年 $107.6B(営業利益 $39.8B、率 37.0%(算出))へ拡大。2025 年は ≈$128.7B(営業利益 ≈$45.6B、率 ≈35.4%(算出))で、率は前年比 −1.6pt(算出)。
2. AWS のセグメント設備投資(P&E 追加額)は 2023 年 $24.8B → 2024 年 $53.3B → 2025 年 $96.5B。AWS 売上比は 27.4% → 49.5% → 75.0%(算出)。
3. AWS の 2026 年 Q1 は売上 $37.6B(+28%)、営業利益 $14.2B(率 37.7%)。Q2 は売上 $42.2B(+36.7%)、営業利益 $16.6B(率 39.3%(算出)。要約は 39.4%、CNBC は 36.8%)。
4. Amazon のサーバー耐用年数は 2020 年 3→4 年、2022 年 4→5 年(NW は 5→6 年)、2024 年 5→6 年、2025 年に一部 6→5 年。2022 年の D&A 減少 $3.6B、2024 年 $3.2B、2025 年の D&A 増加 $1.4B(主に AWS)。
5. Microsoft は FY2023 に 4→6 年(営業利益 +$3.7B)、Alphabet は 2023 年に 4→6 年(減価償却 −$3.9B)へ延長。Meta 2025 年 5.5 年、CoreWeave GPU 6 年、Nebius GPU 4 年(二次情報)。
6. Google Cloud の営業利益は 2020 年 ≈−$5.6B(集計、概数)、2021 年 −$3.1B、2022 年 −$1.9B(別出典 −$3.0B と食い違い)、2023 年 +$1.7B、2024 年 +$6.1B、2025 年 +$13.9B。2025 年の率は 23.7%(算出)。
7. Google Cloud の 2026 年 Q2 は売上 $24.8B(+82%)、営業利益 $8.8B(前年同期 $2.8B)、率 35.6%(要約。前年同期 20.7%)。バックログ $514B(要約)。
8. Microsoft Cloud 粗利率(10-K 記載)は FY2025 69%、FY2026 66%。四半期は FY2025 Q1 71% → Q4 68%、FY2026 Q1 68% → Q4 65%。FY2023〜24 の公式値は未取得。
9. Microsoft Intelligent Cloud は FY2024 売上 $87.5B・営業利益 $37.8B → FY2025 売上 $106.3B・営業利益 $44.6B。売上原価ベースの粗利率は ≈66.2% → ≈62.2%(算出)。
10. Amazon 全社の設備投資は 2025 年 $125B または $131.8B(食い違い)。2026 年見通しは約 $220B(従来約 $200B から引き上げ、2026-07-30 決算説明会)。AWS のサービス別売上比は公式開示なし(2021 年推定で EC2 が 50% 超)。

---

## 1. AWS 年度別の売上・営業利益・率(Amazon セグメント開示)

### 1-1. 年度別(暦年、12 月決算)

| 年度 | 売上 ($M) | 営業利益 ($M) | 営業利益率 | 売上前年比 | 出典 | Tier |
|---|---|---|---|---|---|---|
| 2013 | ≈3,100(丸め値) | 欠損 | 欠損 | — | ycharts AWS 売上系列(「DISCONTINUED」表示あり) | 3* |
| 2014 | ≈4,600 | 458 | ≈10.0%(算出: 458÷4,600) | ≈+48%(算出: 4.6÷3.1−1、丸め値) | electroiq(OI)、ycharts(売上) | 4*/3* |
| 2015 | ≈7,900 | 1,507 | ≈19.1%(算出: 1,507÷7,900) | ≈+72%(算出: 7.9÷4.6−1) | electroiq、ycharts | 4*/3* |
| 2016 | ≈12,200 | 3,108 | ≈25.5%(算出: 3,108÷12,200) | ≈+54%(算出: 12.2÷7.9−1) | FY2018 10-K(OI)、ycharts(売上) | 1*/3* |
| 2017 | ≈17,500 | 4,331 | ≈24.7%(算出: 4,331÷17,500) | ≈+43%(算出。10-K 記載 +43%) | FY2018 10-K、ycharts | 1*/3* |
| 2018 | ≈25,700 | 7,296 | ≈28.4%(算出: 7,296÷25,700) | ≈+47%(算出。10-K 記載 +47%) | FY2018 10-K、ycharts | 1*/3* |
| 2019 | 欠損 | 欠損 | 欠損 | 欠損 | 未取得(§8 参照) | — |
| 2020 | 欠損 | 13,531 | 欠損(売上が欠損のため算出不可) | 欠損 | FY2022 10-K(セグメント表) | 1* |
| 2021 | ≈62,000(要約の「620 億ドル超」) | 18,532 | ≈29.9%(算出: 18,532÷62,000。分母は要約の下限値) | 欠損(2020 売上欠損) | FY2022 10-K(OI)、FourWeekMBA(売上) | 1*/4* |
| 2022 | ≈80,000 以上(要約の「800 億ドル超」) | 22,841 | ≈28.6% 以下(算出: 22,841÷80,000。分母は下限値) | ≈+29%(算出: 80÷62−1。下限基準の概算) | FY2022 10-K(OI)、FourWeekMBA(売上) | 1*/4* |
| 2023 | 90,757 | 24,631 | 27.1%(算出: 24,631÷90,757) | ≈+13%(算出: 90.757÷80−1。2022 は下限値基準の概算) | FY2024 10-K 財務表(要約経由) | 1* |
| 2024 | 107,556 | 39,834 | 37.0%(算出: 39,834÷107,556) | +18.5%(算出: 107.556÷90.757−1。要約の記載は 19%) | FY2024 10-K 財務表(要約経由) | 1* |
| 2025 | ≈128,700 ※食い違い 147,000 の記載あり(§7 の 3) | ≈45,600 | ≈35.4%(算出: 45.6÷128.7) | ≈+19.7%(算出: 128.7÷107.556−1。要約の記載は +20%) | Amazon 2025 年次報告(要約)、last10k(3*)、beancount(4*) | 1*/3*/4* |

- 2024 → 2025 の率の変化: 35.4% − 37.0% = −1.6pt(算出)。
- 2013 年の営業利益、2019 年の売上・営業利益、2020 年の売上は未取得。

### 1-2. 四半期(2025 Q1・Q2 は前年比から逆算)

| 期間 | 売上 ($M) | 営業利益 ($M) | 営業利益率 | 売上前年比 | 出典 | Tier |
|---|---|---|---|---|---|---|
| 2025 Q1(前年同期、算出) | ≈29,400(算出: 37,600÷1.28) | 11,500 | ≈39.1%(算出: 11,500÷29,400。要約の記載も 39.1%) | — | Q1 2026 決算の前年比記載(要約) | 3* |
| 2025 Q2(前年同期、算出) | ≈30,900(算出: 42,200÷1.367) | 10,200 | ≈33.0%(算出: 10,200÷30,900。要約の記載は 32.9%) | — | Q2 2026 決算の前年比記載(要約) | 3* |
| 2026 Q1 | 37,600 | 14,200 | 37.7%(要約記載。算出 37.8%: 14,200÷37,600) | +28% | Amazon Q1 2026 決算(2026-04-29)。Investing.com、Quartz(要約) | 1*/3* |
| 2026 Q2 | 42,200 | 16,600 | 39.3%(算出: 16,600÷42,200。要約は 39.4%、CNBC は 36.8%。§7 の 1) | +36.7%(要約。前期比 +$4.6B) | Amazon Q2 2026 決算資料(要約)、CNBC(3*)、TradingView(4*) | 1*/3*/4* |

- 2026 Q2 の AWS 受注残(backlog): $496B(要約)。Tier 3*。
- 2026 Q2 の AWS 利益に派生商品会計の利益が含まれるという記述あり(beancount、4*)。派生商品利益を除くと率の改善幅は 520bp(要約。含めると 650bp)。AWS への配分額は未確認。
- 2026 Q2 の全社の一過性項目として、関税還付 約 $0.6B とエネルギー契約の公正価値調整 約 $0.6B が営業利益に含まれるとの要約あり(4*)。AWS への配分は未確認。

### 1-3. 参考: Amazon 全社(要約、Tier 1*)

| 期間 | 売上 ($B) | 営業利益 ($B) | 率 | 備考 |
|---|---|---|---|---|
| 2025 通期 | 欠損(要約に記載なし) | ≈80.0 | ≈11.2%(要約記載) | 前年 68.6 から増加(要約) |
| 2026 Q1 | 181.5(+17%) | 23.9(前年 18.4) | 13.1%(要約記載) | 純利益 $30.3B には Anthropic 投資の税引前利益 $16.8B を含む(要約) |
| 2026 Q2 | 200.6(+20%) | 27.5(+43%) | 13.7%(要約記載。前年 11.4%) | 純利益 $62.6B には非営業利益 $53.4B(主に Anthropic 投資)を含む(要約)。Q3 営業利益ガイダンス $22.5〜26.5B |

- 2025 通期の全社売上は要約に記載がなく欠損。

---

## 2. AWS セグメントの設備投資・減価償却と全社 capex

### 2-1. AWS セグメントの P&E 追加額(Amazon の「property and equipment additions」セグメント開示)

| 年度 | AWS P&E 追加額 ($M) | AWS 売上 ($M) | AWS P&E ÷ AWS 売上 | AWS P&E ÷ AWS 営業利益 | 出典 | Tier |
|---|---|---|---|---|---|---|
| 2023 | 24,843 | 90,757 | 27.4%(算出: 24,843÷90,757) | 1.01x(算出: 24,843÷24,631) | FY2025 10-K セグメント表(SEC、要約経由) | 1* |
| 2024 | 53,267 | 107,556 | 49.5%(算出: 53,267÷107,556) | 1.34x(算出: 53,267÷39,834) | 同上 | 1* |
| 2025 | 96,496 | ≈128,700 | ≈75.0%(算出: 96,496÷128,700) | ≈2.12x(算出: 96,496÷45,600) | 同上 | 1* |

- 注: 同じ表の 2025 年の他セグメントは、北米 $35,919M、国際 $7,617M、全社(Corporate) $2,320M。4 セグメント合計は $142,352M(算出: 96,496+35,919+7,617+2,320)。合計行は未確認。
- 2024 年の他セグメントは、北米 $24,348M、国際 $6,643M、全社 $1,494M(要約)。
- 注: この開示は非現金項目(未決済の取得)を含み、共有技術インフラは利用量で配分され、大半が AWS に配分される(10-K の記載、要約)。

### 2-2. AWS セグメントの減価償却費(D&A)

- 2023〜2025 年の AWS セグメント D&A は**欠損**(10-K 本文を未読)。
- 第三者サイトに「D&A が 2021 年 $9,234M → 2025 年 $15,503M」との記載があるが、区分(AWS・北米・全社のいずれか)が特定できず、10-K と照合できていないため採用しない(4*)。

### 2-3. Amazon 全社の設備投資(現金ベース、要約)

| 時点 | 値 | 出典 | Tier |
|---|---|---|---|
| 2023 年・2024 年 | 欠損 | 未取得(§8 参照) | — |
| 2025 年 | $125B(記事 A)または $131.82B(記事 B、同社の営業キャッシュフロー $139.51B と併記) | 別々の要約(個別 URL は特定できず) | 3*/4* |
| 2025 年の P&E 追加額(4 セグメント合計、算出) | $142.4B(算出: 2-1 の合計) | SEC 10-K 要約 | 1* |
| 2026 Q1 | $44.2B(Quartz)または $43.2B(TIKR)。前年同期 $25B(Quartz) | 3* / 4* |
| 2026 Q2 | $54.2B(前年同期比 +68%。算出: 前年同期 ≈$32.3B = 54.2÷1.68) | Q2 2026 決算(要約) | 3* |
| 2026 年見通し | 約 $220B(従来約 $200B から引き上げ。理由は「メモリ価格の上昇」と説明) | 2026-07-30 決算説明会(要約) | 1*/3* |
| 参考: Q1 2026 時点の TTM FCF | $1.2B(要約)。既存 S3 の「Q2 2026 TTM FCF −$7.6B」とは期間が異なる | Investing.com、Quartz(3*) | 3* |

---

## 3. サーバー・ネットワーク機器の耐用年数の変更と利益への影響

### 3-1. 変更の履歴

| 企業 | 変更の内容 | 適用開始 | 利益・償却への影響(開示値) | 出典 | Tier |
|---|---|---|---|---|---|
| Amazon | サーバー 3→4 年 | 2020-01-01 | 金額は未取得 | FY2020 10-K(要約) | 1* |
| Amazon | サーバー 4→5 年、ネットワーク機器 5→6 年 | 2022-01-01 | 2022 年 D&A −$3.6B、純損失 $2.8B 改善(EPS +$0.28)。FY2021 10-K の事前見積では 2022 年営業利益 +$3.1B | FY2021 10-K、FY2022 10-K(要約) | 1* |
| Amazon | サーバー 5→6 年 | 2024-01-01 | 2024 年 D&A −$3.2B | FY2024 10-K(要約) | 1* |
| Amazon | 一部のサーバー・ネットワーク機器 6→5 年(短縮) | 2025-01-01 | 2025 年 D&A **+$1.4B**、純利益 −$1.0B(主に AWS)。Q4 2024 時点の見積は 2025 年営業利益 約 −$0.7B。Q3 2025 10-Q の 9 か月は D&A +$889M、純利益 −$677M | FY2025 10-K、Q3 2025 10-Q(要約) | 1* |
| Microsoft | サーバー・ネットワーク機器 4→6 年 | FY2023(2022-07-01 開始年度。2022 年 7 月に決定) | 営業利益 **+$3.7B**、純利益 +$3.0B、EPS +$0.40(2022-06-30 時点の帳簿価額ベース)。FY2023 営業利益 $88,523M(FY2022 $83,383M) | FY2023 10-K(Change in Accounting Estimate、要約)、Hudson Labs(3*) | 1*/3* |
| Alphabet | サーバー 4→6 年、一部ネットワーク機器 5→6 年 | 2023 年(2023 年 1 月に評価完了) | 2023 年の減価償却 **−$3.9B**、純利益 +$3.0B(EPS +$0.24)。2023 年 1 月時点の見積は −$3.4B(2022-12-31 時点の資産のみ)。Q1 2023 は −$988M。2023 年の全社営業利益 $84,293M(2022 年 $74,842M) | FY2023 10-K(要約) | 1* |
| Meta(再掲) | 大半のサーバー・ネットワーク資産 4〜5 年 → 5.5 年 | 2025-01-01 | 2025 年の減価償却 −$2.92B、純利益 +$2.59B(+$1.00/株) | 既存 S4 [C4](本検索では未再確認) | 3(10-K は 1*) |
| CoreWeave | GPU を含む技術設備 6 年(直線法) | 2023 年初とされるが、変更前の年数が割れる(§7 の 12) | 2023 年の費用減少 $20M(GPU Insights の記載) | S-1・2025 10-K の記載(二次情報経由) | 3*/4* |
| Nebius | GPU 4 年(直線法) | 欠損(変更の時期・履歴は未確認) | 欠損 | 解説記事(2025-09) | 3*/4* |
| Oracle(再掲) | サーバー・ネットワーク 5→6 年 | FY2025 | 営業費用 −$733M、純利益 +$573M(希薄化後 EPS +$0.20) | 既存 S4 [C1][C3] | 1*(既存) |

- Nebius のデータセンター設備の耐用年数(3〜10 年)と CoreWeave(8〜12 年)は、GPU の値と区別して扱うべき別の資産区分(要約)。
- 2026 年 4〜6 月期の 10-Q における Microsoft・Alphabet・Amazon・Meta の耐用年数変更は**未検索**(検索上限)。既存 S4 も未確認としている。

### 3-2. 利益・償却への影響の比率(算出、上限)

| 変更 | 影響額 | 比較の基準 | 比率(算出) | 注記 |
|---|---|---|---|---|
| Amazon 2022(D&A −$3.6B) | 3.6 | AWS 営業利益 2022 $22.8B | 15.8%(算出: 3.6÷22.841) | 全額が AWS に配分されたと仮定した上限 |
| Amazon 2024(D&A −$3.2B) | 3.2 | AWS 営業利益 2024 $39.8B | 8.0%(算出: 3.2÷39.834) | 同上 |
| Amazon 2025(D&A +$1.4B) | 1.4(費用増) | AWS 営業利益 2025 ≈$45.6B / AWS 売上 ≈$128.7B | 3.1%(算出: 1.4÷45.6)/ 1.1pt(算出: 1.4÷128.7) | 「主に AWS」と記載。上限として扱う |
| Microsoft FY2023(営業利益 +$3.7B) | 3.7 | 全社営業利益 FY2023 $88.5B | 4.2%(算出: 3.7÷88.523) | 全社数値。要約の第三者計算も 4.2% |
| Alphabet 2023(減価償却 −$3.9B) | 3.9 | 全社営業利益 2023 $84.3B | 4.6%(算出: 3.9÷84.293) | 配分先は未開示。Google Cloud 営業利益 2023 $1.7B との比(算出 229%)は配分の前提がないため参考外 |

---

## 4. Google Cloud 年度別(Alphabet セグメント開示)

| 年度 | 売上 ($M) | 売上前年比 | 営業利益 ($M) | 営業利益率 | 出典 | Tier |
|---|---|---|---|---|---|---|
| 2019 | ≈8,918 | 欠損 | 欠損(通期未取得。Q4 2019 のみ −1,194) | 欠損 | ycharts(売上・Q4 OI) | 3*/4* |
| 2020 | ≈13,060 | ≈+46%(算出: 13.06÷8.918−1) | ≈−5,600(集計記事「約 56 億ドルの損失」) | ≈−42.9%(算出: −5,600÷13,060) | ycharts、集計記事 | 3* |
| 2021 | 19,206 | ≈+47%(算出: 19.206÷13.06−1) | −3,099 | −16.1%(算出: −3,099÷19,206) | stockanalysis | 3* |
| 2022 | 26,280 | ≈+37%(算出: 26.28÷19.206−1) | −1,900(FY2023 10-K の記載、要約)/ −2,968(stockanalysis)※食い違い | −7.2%(算出: −1,900÷26,280)/ −11.3%(算出: −2,968÷26,280) | FY2023 10-K(要約)、stockanalysis | 1*/3* |
| 2023 | 33,088 | ≈+26%(算出: 33.088÷26.28−1) | **+1,700**(FY2023 10-K、要約。2022 比 +3.6B) | 5.1%(算出: 1,700÷33,088) | FY2023 10-K(要約) | 1* |
| 2024 | ≈43,000(集計記事。Q2 は未取得) | ≈+30%(算出: 43÷33.088−1、概算) | **6,112**(2025 ARS の数値。四半期合計 900+1,172+1,947+2,093 = 6,112 とも一致、算出) | ≈14.2%(算出: 6,112÷43,000、概算) | Alphabet 2025 ARS(要約)、FY2024 10-K(2024 年は前年比 +$4.4B の記載、要約)、四半期 OI(3*) | 1*/3* |
| 2025 | ≈58,800(四半期合計、算出: 12.3+13.6+15.2+17.7 の各 B) | ≈+37%(算出: 58.8÷43−1、概算) | **13,910**(2025 ARS、要約) | ≈23.7%(算出: 13,910÷58,800) | Alphabet 2025 ARS(要約)、四半期売上(3*) | 1*/3* |
| 2026 Q2 | 24,800(+82%) | +82%(要約) | 8,800(前年同期 2,800) | 35.6%(要約。算出 35.5%: 8,800÷24,800。前年同期は要約 20.7%) | 2026-07-22 決算(要約)、Yahoo・Fool(3*) | 3* |

- 2026 Q2 の注記: TPU ハードウェアの販売(顧客データセンターへの納入)による収益を初めて計上した。経営陣は、この販売を除いても成長が維持されたと説明(要約)。
- バックログ: $514B(前期比 +$50B 超。約半分を 24 か月以内に収益化の見込み、要約)。2026 年 Q1 に 1 年以内の契約をバックログの定義に含める変更を行った(要約)。
- 2025 年の四半期売上(要約): Q1 $12.3B(+28%)、Q2 $13.6B(+32%)、Q3 $15.2B(+34%)、Q4 $17.7B(+48%)。

---

## 5. Microsoft(Microsoft Cloud 粗利率・Intelligent Cloud)

### 5-1. Microsoft Cloud 粗利率(10-K の記載率)

| 年度(6 月期) | Microsoft Cloud 粗利率 | 会社の説明(要約) | 出典 | Tier |
|---|---|---|---|---|
| FY2023 | 欠損(第三者トラッカーに 72% の記載あり。年度ラベルが不確実のため未採用) | — | 未取得 | 4* |
| FY2024 | 欠損(同上) | — | 未取得 | 4* |
| FY2025 | **69%**(前年から低下) | 「AI インフラ拡張の影響により低下。Azure の効率化により一部相殺」 | FY2025 10-K(要約) | 1* |
| FY2026 | **66%**(前年から低下) | 「AI インフラへの継続投資と AI 製品の利用拡大。Azure と Microsoft 365 Commercial クラウドの効率化で一部相殺」 | FY2026 10-K(要約) | 1* |

- 参考: FY2025 の Microsoft Cloud 売上 $168.9B(+23%、FY2025 10-K 要約)。FY2026 の同売上は未取得。

### 5-2. Microsoft Cloud 粗利率(四半期、決算説明会の記載)

| 四半期 | FY2025 | FY2026 |
|---|---|---|
| Q1 | 71%(前年同期比 −2pt) | 68%(前年比低下。AI 投資の一部を効率化で相殺) |
| Q2 | 70%(AI インフラ拡張の影響) | 67%(AI への継続投資の影響) |
| Q3 | 69%(AI インフラ拡張の影響) | 66%(AI への継続投資の影響) |
| Q4 | 68%(「予想をわずかに上回る」) | 65%(Azure の売上構成の変化と AI インフラ投資の継続) |

出典: Microsoft IR の FY2025 Q1〜Q4 および FY2026 Q1〜Q4 の決算資料・決算説明会(要約経由)。Tier 1*。

### 5-3. Intelligent Cloud セグメント(FY2025 Q4 のセグメント表、比較列の FY2024 を含む)

| 指標 | FY2024 | FY2025 | 前年比 |
|---|---|---|---|
| 売上 ($M) | 87,464 | 106,265 | +21.5%(算出: 106,265÷87,464−1) |
| 売上原価 ($M) | ≈29,600 | ≈40,200 | ≈+36%(算出: 40.2÷29.6−1) |
| 売上総利益率(算出) | ≈66.2%(算出: (87,464−29,600)÷87,464。要約は 66.1%) | ≈62.2%(算出: (106,265−40,200)÷106,265) | ≈−4.0pt(算出) |
| 営業費用 ($M) | ≈20,000 | ≈21,500 | ≈+7% |
| 営業利益 ($M) | 37,813 | 44,589 | +17.9%(算出: 44,589÷37,813−1) |
| 営業利益率(算出) | 43.2%(算出: 37,813÷87,464) | 42.0%(算出: 44,589÷106,265) | ≈−1.2pt(算出) |

- 出典: Microsoft IR の FY2025 Q4 セグメント表(要約経由)、FY2025 10-K。Tier 1*。
- 注: FY2024 は FY2025 の比較列であり、FY2024 当時の原表示との比較は未確認(区分の再表示の可能性)。
- FY2023 と FY2026 の Intelligent Cloud 数値は未取得(§8 参照)。
- 売上原価と営業費用は要約の丸め値。

### 5-4. Microsoft 全社(参考、要約経由)

| 指標 | FY2025 | FY2026 | 出典 | Tier |
|---|---|---|---|---|
| 売上 | $281.7B(+15%) | 欠損 | FY2025 10-K(要約) | 1* |
| 営業利益 | $128.5B(+17%) | 欠損 | 同上 | 1* |
| 売上総利益 | $193,893M | $225,465M(+16.3%、算出: 225,465÷193,893−1) | FY2026 10-K(要約) | 1* |
| 売上総利益率 | 欠損(分母の FY2026 売上を未取得) | 欠損 | — | — |

- FY2026 の全社粗利率について、要約は「前年比わずかに低下」と記載。

### 5-5. AI による粗利率低下の会社説明(原文の要旨、要約経由)

- FY2025 10-K: Microsoft Cloud 粗利率は「AI インフラ拡張の影響により 69% に低下。Azure の効率化により一部相殺」。
- FY2026 10-K: 「AI インフラへの継続投資と AI 製品の利用の増加により低下。Azure と Microsoft 365 Commercial クラウドの効率化で一部相殺」。
- 決算説明会(FY2026 Q4): Microsoft Cloud 粗利率 65% の低下要因として、Azure への売上構成変化と AI インフラ投資の継続を挙げた(要約)。

---

## 6. AWS の売上構成(EC2 等)— 公式開示なし

| 項目 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Amazon のサービス別売上・利益の開示 | なし(Amazon はサービス別の利益を開示していない) | 2021 年時点の記事 | CNBC(2021-09-05) | 3* |
| EC2 の売上比(推定) | 50% 超 | 2021 年推定(Corey Quinn の推定を引用) | CNBC(2021-09-05) | 3* |
| EC2+ストレージ+DB+データ転送の売上比(推定) | 70% 超 | 2021 年推定(同上) | CNBC(2021-09-05) | 3* |
| AWS Marketplace の売上(推定) | $1〜2B(2020 年 AWS 売上の約 3%) | 2020 年推定 | CNBC(2021-09-05) | 3* |
| AWS の AI 売上のランレート | $15B 超 | 2026 年 Q1 入り時点(ランレート。年間実績ではない) | Amazon 株主向け資料(要約) | 1* |
| 自社チップ(Graviton・Trainium・Nitro)のランレート | $20B 超(収益は EC2 経由のみと説明) | 2026 年時点 | Amazon 株主向け資料(要約) | 1* |
| DB・分析・AI サービスの売上比 | 欠損 | — | — | — |

- 注: チップの収益が EC2 経由で計上されるなら、「EC2 の比率」と「AI の比率」は重なるため加算できない(推論。出典の記述ではない)。
- 2021 年推定は古く、AI 需要の拡大前のデータ。

---

## 7. 食い違い(採らずに併記)

| # | 項目 | 出典 A | 出典 B | 扱い |
|---|---|---|---|---|
| 1 | AWS 2026 Q2 営業利益率 | 39.4%(TradingView 要約、4*)/ 算出 39.3%(16.6÷42.2) | 36.8%(CNBC、3*) | 両方を併記。分子・分母(16.6、42.2)は両出典で一致 |
| 2 | AWS 2026 Q1 営業利益率 | 37.7%(要約、3*) | 37.8%(算出: 14.2÷37.6) | 丸めの差。両方を併記 |
| 3 | AWS 2025 年売上 | ≈$128.7B(+20%)(Amazon 2025 年次報告の要約) | $147B(+28%)(別の集計サイト、3*)。整合しない | 両方を併記。§1 の表は $128.7B の要約値を使用しているが、$147B の記載があることを注記 |
| 4 | Amazon 2025 年の全社 capex | $125B(記事 A) | $131.82B(記事 B、OCF $139.51B と併記) | 両方を併記。定義の違い(非現金・リース)の可能性は未確認 |
| 5 | Amazon 2026 Q1 capex | $44.2B(Quartz、3*) | $43.2B(TIKR、4*) | 両方を併記 |
| 6 | Google Cloud 2022 年営業利益 | −$1.9B(FY2023 10-K の記載、要約、1*) | −$2.968B(stockanalysis、3*) | 両方を併記。CNBC の要約では、Alphabet がクラウド等の営業利益を再表示した旨の記述があり、差の原因の可能性(未確認) |
| 7 | Google Cloud 2020・2021 年営業利益 | 2020: ≈−$5.6B(集計、概数)、2021: −$3.099B(stockanalysis) | 単一の集計のみ。10-K 本文は未読 | 単一出典のまま記載 |
| 8 | Google Cloud 2025 年売上 | ≈$58.8B(四半期の合計、算出) | $58.7B(Wikipedia、4*) | 両方を併記。差 0.1B は丸めの可能性 |
| 9 | Google Cloud 2024 年売上 | ≈$43B(集計記事、3*) | 四半期は Q1・Q3・Q4 のみ確認可能(Q2 欠損) | 検証は不完全。概算として併記 |
| 10 | Microsoft Cloud 粗利率 FY2023〜24 | 72%(第三者トラッカー、4*、年度ラベル不確実) | 公式値は未取得 | 未採用。欠損として扱う |
| 11 | Microsoft Cloud 粗利率(FY2026) | 66%(10-K、1*) | Q4 FY2026 65%(決算説明会、1*) | 期間が異なるため矛盾ではない。両方を併記 |
| 12 | CoreWeave GPU 耐用年数の変更時期 | 4→6 年(2023 年 1 月、Substack、4*) | 5→6 年(2023 年 1 月 1 日、GPU Insights、4*。既存 S4 も 5→6 年) | 両方を併記。10-K 本文で要確認 |
| 13 | Amazon の耐用年数(Yardeni、既存 S3 再掲) | 「約 4 年」(Yardeni、3*) | サーバー 5〜6 年(10-K 要約、1*) | 既存 S4 で指摘済み。両方を併記。Yardeni の対象区分は不明 |
| 14 | Microsoft の耐用年数(Yardeni、既存 S3 再掲) | 4〜5 年(Yardeni、3*) | 6 年(FY2023 10-K 要約、1*) | 両方を併記。対象区分は不明 |
| 15 | Amazon 2018 年全社営業利益(二次情報) | $7.2B(SignHouse、4*) | $12.4B(FY2018 10-K 要約、1*) | 両方を併記。SignHouse の 2021 年 $18.5B は AWS セグメント値との記載あり |
| 16 | Microsoft Intelligent Cloud FY2024 売上 | $87,464M(FY2025 Q4 セグメント表の比較列、1*) | 当時の原表示は未確認 | 比較列の値のみ記載。原表示は欠損 |
| 17 | AWS 2024 年の売上成長率 | 19%(要約の 10-K 記載) | 18.5%(算出: 107.556÷90.757−1) | 丸めの差。両方を併記 |
| 18 | Amazon 2025 年の耐用年数変更の純利益影響 | Q3 2025 3 か月 −$298M(既存 S4、1*) | 9 か月 −$677M(本検索、1*)、通期 −$1.0B(FY2025 10-K 要約、1*) | 期間の違い。矛盾なし |

---

## 8. 欠損と試した検索語

| 欠損項目 | 試した検索語(WebSearch) | 結果 |
|---|---|---|
| AWS 2013 年の営業利益 | "AWS revenue 2013 2014 2015 2016 2017 2018 operating income annual history Amazon Web Services" | 未取得。2014 年以降の OI のみ得られた |
| AWS 2019 年の売上・営業利益 | "AWS annual revenue and operating income 2019 2020 2021 2022 2023 2024 segment table" | 未取得。FY2021 10-K(2019–2021 のセグメント)は未読 |
| AWS 2020 年の売上 | "AWS operating income 2020 2021 2022 $13.5 billion $18.5 billion $22.8 billion annual segment" | OI のみ取得(13,531)。売上は未取得 |
| AWS 2021・2022 年の売上(正式値) | 同上、および "AWS annual revenue ... segment table" | 要約の下限値(「620 億ドル超」「800 億ドル超」)のみ。正式値は未取得 |
| AWS セグメントの D&A(2023〜2025 年) | "Amazon 10-K 2025 AWS depreciation and amortization expense segment 'property and equipment additions' net additions by segment" | 未取得。P&E 追加額のみ得られた |
| Amazon 全社の設備投資(2023・2024 年) | "Amazon 2025 full year capital expenditures cash capex free cash flow 2026 capex guidance $200 billion" | 未取得。2025 年と 2026 年のみ |
| Amazon 全社 2025 年 capex の正式値 | 同上 | 2 つの数値で食い違い(§7 の 4) |
| AWS のサービス別売上比率(DB・分析・AI) | "AWS revenue mix EC2 compute share percentage storage database analytics AI services estimate of AWS revenue by service" | EC2 の 2021 年推定のみ。DB・分析・AI は未取得 |
| Microsoft Cloud 粗利率 FY2023・FY2024(公式値) | "Microsoft Cloud gross margin percentage fiscal year 2025 2024 2023 10-K" | FY2025 のみ(69%)。FY2023・FY2024 は未取得 |
| Microsoft Intelligent Cloud FY2023・FY2026 | (検索上限到達のため未検索) | 欠損 |
| Microsoft の 2026 年 4〜6 月期の耐用年数変更 | (検索上限到達のため未検索) | 欠損。既存 S4 も未確認 |
| Microsoft FY2024 10-K 原文の耐用年数 | "Microsoft changed useful life server network equipment 4 years to 6 years fiscal 2023 operating income impact 10-K" | FY2023 の 10-K 要約のみ。FY2024 は Hudson Labs の言及のみ(3*) |
| Google Cloud 2019 年の通期営業利益 | "Google Cloud segment operating income loss 2019 2020 2021 2022 2023 annual revenue 10-K" | 未取得(Q4 2019 の −1,194 のみ) |
| Google Cloud 2024 年の売上(正式値) | "Google Cloud revenue full year 2024 billion operating income $6.1 billion annual" | 集計の約 $43B と四半期の一部のみ。Q2 2024 は未取得 |
| Google Cloud 2025 年の通期売上 | "Google Cloud full year 2025 revenue operating income margin Alphabet fourth quarter 2025 results annual 2024 operating income" | 通期売上は未取得。四半期合計(算出)で代替 |
| Google Cloud 2026 Q2 の一次資料 | "Google Cloud second quarter 2026 revenue operating income margin 35.6% backlog" | 要約のみ。Q2 の 10-Q・決算資料は未読 |
| Alphabet 2023 年の減価償却変更の営業利益への効果 | "Alphabet changed useful life servers 4 to 6 years 2023 depreciation impact 10-K operating income" | 開示なし(減価償却の減少額・純利益の影響のみ) |
| Nebius の耐用年数の変更履歴・10-K 原文 | "CoreWeave GPU useful life six years Nebius GPU depreciation four years accounting policy 10-K" | 二次情報(4 年)のみ。変更時期は未確認 |
| Amazon 2020 年変更の金額 | "Amazon changed useful life servers networking equipment 5 years to 6 years 2024 10-K 2022 4 years to 5 years 2020 3 years to 4 years" | 2020 年の金額は未取得。2022 年・2024 年・2025 年の金額は取得 |

---

## 9. 出典一覧(すべて検索要約経由。原本未読)

| # | 出典 | URL | Tier | 主な用途 |
|---|---|---|---|---|
| S1 | Amazon 2025 Annual Report | https://s2.q4cdn.com/299287126/files/doc_financials/2026/ar/Amazon-2025-Annual-Report.pdf | 1* | AWS 2025 売上・営業利益 |
| S2 | Amazon FY2025 10-K(SEC) | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm | 1* | AWS P&E 追加額、耐用年数変更(2025) |
| S3 | Amazon FY2024 10-K 財務表(SEC) | https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/Financial_Report.xlsx | 1* | AWS 2023・2024 売上・営業利益 |
| S4 | Amazon FY2024 10-K(SEC) | https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/amzn-20241231.htm | 1* | 耐用年数変更(2024) |
| S5 | Amazon FY2022 10-K(SEC) | https://www.sec.gov/Archives/edgar/data/1018724/000101872423000004/amzn-20221231.htm | 1* | AWS 2020〜2022 営業利益、2022 年の D&A |
| S6 | Amazon FY2021 10-K(SEC) | https://www.sec.gov/Archives/edgar/data/1018724/000101872422000005/amzn-20211231.htm | 1* | 2022 年変更の事前見積 |
| S7 | Amazon FY2020 10-K(SEC) | https://www.sec.gov/Archives/edgar/data/1018724/000101872421000004/amzn-20201231.htm | 1* | 2020 年変更 |
| S8 | Amazon FY2018 10-K(SEC) | https://www.sec.gov/Archives/edgar/data/1018724/000101872419000004/amzn-20181231x10k.htm | 1* | AWS 2016〜2018 営業利益 |
| S9 | Amazon Q3 2025 10-Q(EDGAR 索引) | https://content.edgar-online.com/ExternalLink/EDGAR/0001018724-25-000123.html | 1* | 2025 年変更の 9 か月影響 |
| S10 | Amazon Q2 2026 決算資料(IR) | https://ir.aboutamazon.com/files/doc_earnings/2026/q2/earnings-result/AMZN-Q2-2026-Earnings-Release.pdf | 1* | AWS・全社 2026 Q2 |
| S11 | Amazon Q2 2026 決算説明会(Yahoo 記事経由) | https://finance.yahoo.com/quote/AMZN/earnings/AMZN-Q2-2026-earnings_call-657334.html | 1* | 2026 年 capex 見通し $220B |
| S12 | Amazon Q1 2026 決算(IR 発表) | https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-First-Quarter-Results/default.aspx | 1*(一覧のみ。要約は下記の記事経由) | AWS 2026 Q1 |
| S13 | Investing.com「Amazon Q1 2026 slides」 | https://www.investing.com/news/company-news/amazon-q1-2026-slides-aws-surges-28-record-margins-offset-by-capex-93CH-4647447 | 3* | AWS Q1 2026、TTM FCF |
| S14 | Quartz「Amazon Q1 2026 earnings」 | https://qz.com/amazon-q1-2026-earnings-aws-cloud-growth-042926 | 3* | AWS Q1 2026、capex $44.2B |
| S15 | TIKR「Amazon Q1 2026 beat」 | https://www.tikr.com/blog/amazon-q1-2026-beat-hides-its-most-exciting-new-revenue-engine | 4* | capex $43.2B |
| S16 | CNBC「AWS posts fastest growth since 2021」 | https://www.cnbc.com/2026/07/30/aws-earnings-q2-2026.html | 3* | AWS Q2 2026 利益率 36.8% |
| S17 | TradingView(Q2 2026 要約) | https://www.tradingview.com/news/leverage_shares:2508da40f094b:0-amazon-q2-2026-earnings-shows-aws-growth-accelerates/ | 4* | AWS Q2 2026 率 39.4% |
| S18 | beancount「Amazon Q2 2026」 | https://beancount.io/blog/2026/07/31/amazon-fy2026-q2-earnings-analysis | 4* | 派生商品利益、一過性項目 |
| S19 | beancount「Amazon FY2025 earnings」 | https://beancount.io/blog/2026/07/13/amazon-fy2025-earnings-analysis | 4* | AWS 2025 売上・OI |
| S20 | last10k(AMZN 10-K 索引) | https://last10k.com/sec-filings/amzn | 3* | AWS 2025 OI 45.6B |
| S21 | FourWeekMBA「AWS Revenues 2013-2025」 | https://fourweekmba.com/aws-revenues/ | 4* | AWS 2021・2022 売上(下限値) |
| S22 | ycharts「AWS Revenue」 | https://ycharts.com/indicators/the_amazoncom_inc_amzn_aws_revenue | 3* | AWS 2013〜2018 売上(丸め) |
| S23 | electroiq「AWS Statistics」 | https://electroiq.com/stats/aws-statistics/ | 4* | AWS 2014・2015 OI |
| S24 | CNBC「How Amazon Web Services makes money」(2021-09-05) | https://www.cnbc.com/2021/09/05/how-amazon-web-services-makes-money-estimated-margins-by-service.html | 3* | サービス別の推定比率 |
| S25 | Amazon 株主向け資料(AI 売上・チップのランレート、SEC 提出。個別の資料名は未特定。候補 URL は Amazon 2025 年 ARS) | https://www.sec.gov/Archives/edgar/data/1018724/000110465926041036/tm263815d4_ars.pdf | 1*(候補のみ) | AI ランレート $15B 超、チップ $20B 超 |
| S26 | Microsoft FY2023 10-K(SEC) | https://www.sec.gov/Archives/edgar/data/789019/000095017023035122/msft-20230630.htm | 1* | 耐用年数変更 4→6 年、FY2023 OI |
| S27 | Hudson Labs「Microsoft Extended Server Useful Life」 | https://hudson-labs.com/research/msft-server-useful-life | 3* | FY2023 の影響の第三者計算 4.2% |
| S28 | Microsoft FY2025 10-K(SEC) | https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm | 1* | Microsoft Cloud 粗利率 69%、Cloud 売上 $168.9B |
| S29 | Microsoft FY2026 10-K(SEC) | https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323660/msft-20260630.htm | 1* | Microsoft Cloud 粗利率 66%、全社粗利 |
| S30 | Microsoft IR FY2025 Q4 セグメント表 | https://www.microsoft.com/en-us/investor/earnings/fy-2025-q4/segment-revenues | 1* | Intelligent Cloud FY2024・FY2025 |
| S31 | Microsoft IR FY2025 Q4 Performance | https://www.microsoft.com/en-us/investor/earnings/fy-2025-q4/performance | 1* | FY2025 四半期の Microsoft Cloud 粗利率 |
| S32 | Microsoft IR FY2026 決算説明会(Q4) | https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4 | 1* | FY2026 四半期の Microsoft Cloud 粗利率 |
| S33 | Microsoft IR FY2026 Q1 Performance | https://www.microsoft.com/en-us/investor/earnings/fy-2026-q1/performance | 1* | FY2026 Q1 |
| S34 | Alphabet FY2023 10-K(SEC) | https://www.sec.gov/Archives/edgar/data/1652044/000165204424000022/goog-20231231.htm | 1* | 耐用年数変更 2023、Google Cloud 2023 OI、全社 OI |
| S35 | Alphabet FY2024 10-K(SEC) | https://www.sec.gov/Archives/edgar/data/1652044/000165204425000014/goog-20241231.htm | 1* | Google Cloud 2024 OI +$4.4B |
| S36 | Alphabet 2025 Annual Report(ARS) | https://www.sec.gov/Archives/edgar/data/0001652044/000130817926000344/goog014907-ars.pdf | 1* | Google Cloud 2024・2025 OI |
| S37 | Alphabet Q2 2026 決算説明会(Yahoo 記事経由) | https://finance.yahoo.com/quote/GOOG/earnings/GOOG-Q2-2026-earnings_call-657320.html | 1* | Google Cloud 2026 Q2 |
| S38 | Yahoo「Alphabet's Google Cloud Is Surging at 82%」 | https://finance.yahoo.com/technology/ai/articles/alphabets-google-cloud-surging-82-152000214.html | 3* | Google Cloud 2026 Q2 の 35.6% |
| S39 | Motley Fool「Sundar Pichai backlog $514B」 | https://www.fool.com/investing/2026/09/13/sundar-pichai-alphabets-backlog-514-billion/ | 3* | バックログ $514B |
| S40 | BigGo Finance「GOOG Q2 2026」 | https://finance.biggo.com/news/US_GOOG_2026-07-22 | 4* | Google Cloud 2026 Q2 |
| S41 | ycharts「Google Cloud Operating Income」 | https://ycharts.com/indicators/alphabet_inc_cl_a_googl_google_cloud_operating_income | 3* | Google Cloud 2019〜2020 売上・OI |
| S42 | stockanalysis「Alphabet Financials」 | https://stockanalysis.com/stocks/googl/financials/ | 3* | Google Cloud 2021・2022 OI(−2,968 の出典) |
| S43 | CNBC「Google's cloud business turns profitable」(2023-04-25、見出しのみ) | https://www.cnbc.com/2023/04/25/googles-cloud-business-turns-profitable-for-the-first-time-on-record.html | 3* | 2022 年の再表示の記述 |
| S44 | DCD「Google Cloud Q3 2024 revenue」 | https://www.datacenterdynamics.com/en/news/google-cloud-q3-2024-revenue-hits-114bn-data-center-spend-set-to-increase-in-2025/ | 3* | Google Cloud 2024 四半期売上 |
| S45 | ConstellationR「Google Cloud revenue up 30% in Q4」 | https://www.constellationr.com/blog-news/insights/google-cloud-revenue-30-q4-alphabet-results-mixed | 3* | Google Cloud 2024 Q4 |
| S46 | Bizety「GPU Depreciation: CoreWeave vs. Nebius」(2025-09-23) | https://bizety.com/2025/09/23/gpu-depreciation-coreweave-vs-nebius/ | 3* | Nebius 4 年、CoreWeave 6 年 |
| S47 | GPU Insights「Server Useful Life: What Five 10-Ks Disclose」 | https://gpuinsights.net/server-useful-life-gpu-depreciation-2026/ | 4* | CoreWeave 5→6 年、2023 年 $20M |
| S48 | Dave Friedman Substack「Two Ways to Finance the AI Boom」 | https://davefriedman.substack.com/p/two-ways-to-finance-the-ai-boom | 4* | CoreWeave 4→6 年(食い違い) |
| S49 | TIKR「Amazon Raised Its 2026 Capex Guide to $220 Billion」 | https://www.tikr.com/blog/amazon-raised-its-2026-capex-guide-to-220-billion-heres-what-drove-the-increase | 4* | 2026 capex $220B、メモリ価格 |
| S50 | Yahoo「Amazon Raised 2026 capex guide」 | https://finance.yahoo.com/markets/stocks/articles/amazon-raised-2026-capex-guide-114017457.html | 3* | 2026 capex $220B |

既存調査からの再掲(今回未再検索): Oracle FY2025 10-K(既存 S4 [C1][C2][C3])、Meta 2025 10-K 要約(既存 S4 [C4]、Accounting Today、The Stack)、Yardeni Research(既存 S3 [S37])。
