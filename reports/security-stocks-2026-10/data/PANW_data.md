# PANW 定量データ表

収集者: Haiku / 取得日: 2026-10-11
対象: Palo Alto Networks(PANW、NASDAQ)/ 決算期末 7月31日 / 評価基準日 2026-10-11
単位: 金額は US$ 百万(特記を除く)、EPS はドル、比率は %。
「約」は出典が四捨五入して示した値(概ね ±50 百万ドル)。
出典は [S##] で示し、末尾の出典一覧に URL を置く。取得日はすべて 2026-10-11。

---

## 0. 取得状況と欠損の概要

### 取得方法と制約
- WebSearch のみで取得した(WebFetch・curl は未使用)。
- 一次資料(8-K 決算リリース、10-K、10-Q)は URL が検索結果に出たが、本文は取得していない。数値は検索結果の要約・スニペットに基づく。一次資料との照合は未了。
- WebSearch の回数上限に到達し、途中で検索を打ち切った。ツールから上限到達の通知が出ている。
  このため、表6の詳細(目標株価・レーティング・年度別の平均/高/低)、表7(バランスシート)、表1の株価確定は未取得。
  続きが必要なら後続メッセージで検索を再開できる。

### 欠損の多い項目
- 表1: 株価(2026-10-09 終値)、時価総額、希薄化後株数(直近四半期)、その他 2025〜2026 年の買収の対価
- 表2: 製品売上・S&S 売上、GAAP 粗利率、GAAP 営業利益(Q4 のみ取得)、SBC、営業CF(Q4 のみ概算)、capex、希薄化後株数
- 表3: cRPO、billings、プラットフォーム化顧客数(全期間)、FY24 Q3 の NGS ARR
- 表4: FY2022・FY2023 の全項目、SBC、GAAP 営業利益、非GAAP営業利益率、FY2026 の通期 GAAP EPS・非GAAP EPS、capex(FY2025 以外)、期末希薄化後株数
- 表5: FY2024・FY2025・FY2026 の期初ガイダンス、FY2027 の FCF マージン見通し
- 表6: 売上・EPS のコンセンサスの平均/高/低(FY2027 売上平均は推計のみ)、FY2029〜FY2031、アナリスト数、目標株価、レーティング分布
- 表7: 全項目

### 出典間で食い違った数値(両論併記・未確定)
- CyberArk の買収対価: 発表時の headline $25B(S54)と、10-Q の確定値 $21,061M(S28)。
- Chronosphere の金額: 発表時 $3.35B(S32、S33)と、完了時の報道では「非開示」(S31 系の要約)。
- FY2026 通期売上ガイダンス(Q3 時点): 11,415〜11,425(S09)と 11,420〜11,430(S11)。
- FY2027 非GAAP EPS 見通し: 4.16〜4.19 は検索要約の複数サイトで一致(S04)。原典の 8-K は未確認。
- FY2027 EPS コンセンサス: 平均 約4.11(Fiscal.ai 経由、S04)と 2.01(Benzinga、S44)。後者は誤記の疑い。
- 株価(直近値): 400〜423 のばらつき。表示日付が不明、または土曜日(2026-10-10)の表示もある(表1参照)。
- 52週安値 139.57(S36、S40 で一致)。ただし前年 2025-10-09 の終値 215.17(S46)との整合は未確認。
- FY2024 Q3 の NGS ARR: 第三者の 4.52B(FY2024 通期 4.22B と矛盾するため不採用)。
- FY2024 Q3 の RPO: 公式要約 11.3B(S25)と、第三者 12.6B。公式を採用し未確定とする。
- FY2026 Q1 の NGS ARR: 5.9B(リリース要約、S16)と 5.85B(決算トランスクリプト、S17)。
- FY2026 Q3 の NGS ARR: 8.1B(S08)と 8.13B(別要約)。
- 発行済株式数: 818M(2026-08-31、10-K 表紙、S27)、815M(2026-05-26、10-Q、S28)、816M(2026-02-11、10-Q、S29)。
  日付不明のアグリゲータ値 811M は不採用。
- CFO の就任時期: 2020(S47 系)と 2021-03-16(S43 系)。
- 2:1 株式分割(2024年12月効力)前に公表された EPS: FY24 Q3、FY24 Q4、FY25 Q1。表2で分割前・分割後を分けて記録。

### 会社IRで確認できなかった重要数値
- 2026-10-09 の終値(確定できず)
- FY2026 通期の GAAP EPS・非GAAP EPS・営業CF・capex・SBC・自社株買い
- FY2027 非GAAP EPS 見通しの原典(8-K)での確認
- FY2027 の FCF マージン見通し
- Q4 FY2026 の希薄化後株数、GAAP 粗利率
- 次回決算日 2026-11-19(第三者カレンダーのみ。会社発表は未確認)

---

## 表1 基本情報

| 項目 | 値 | 出典 | 備考 |
|---|---|---|---|
| 株価(2026-10-09 終値) | **欠損** | — | 参考値のみ: 418.78(TradingView、24時間で +5.09%、日付不明)[S37]。419.00(Robinhood、表示日付 2026-10-10 は土曜のため信頼性低)[S36]。422.83(Tradersunion、日付不明)[S38]。407.96[S51]。405.94[S50]。400.22(Investing.com、101日前の表示で古い)[S52]。取得できた直近値は 400〜423 のレンジ。確定には日次の終値データが必要 |
| 時価総額 | **欠損** | — | 株価未確定のため算出不可。参考: 2026-07-24 終値 323.76 の時点で時価総額 約 263.9B(古い参考値)[S40] |
| 発行済株式数(基本) | 818 百万株 | [S27] | 2026-08-31 時点(10-K 表紙)。参考: 815(2026-05-26、10-Q)[S28]、816(2026-02-11、10-Q)[S29] |
| 希薄化後株数(直近四半期) | **欠損** | — | 直近四半期の希薄化後株数は未取得。参考: FY2027 ガイダンスの前提は 844〜847 百万株(希薄化後)[S04] |
| 52週高値 | 432.33 | [S36][S37] | 2026-10-06 の高値(TradingView 要約、S37)。Robinhood の 52 週レンジ上限とも一致(S36) |
| 52週安値 | 139.57 | [S36][S40] | 2 出典で一致。日付は未確認。前年 2025-10-09 終値 215.17 [S46] とは別の時点と思われる |
| CEO | Nikesh Arora(Chairman & CEO) | [S34][S35] | 会社の経営陣ページ(S34)で確認 |
| CFO | Dipak Golechha | [S34][S47] | 就任時期は出典間で不一致(2020 と 2021-03-16) |
| 直近決算発表日 | 2026-09-01(FY2026 Q4 および通期) | [S01][S03][S05] | 事前の報道では引け後発表。当日の株価反応は S05 で確認 |
| 次回決算予定日 | 2026-11-19(FY2027 Q1、予定) | [S41][S42][S43] | 第三者カレンダーのみ。会社発表は未確認 |
| CyberArk 買収: 発表日 | 2025-07-30 | [S54] | 現金と株式による買収、headline 価値 約 $25B |
| CyberArk 買収: 完了日 | 2026-02-11 | [S30][S28] | 完了発表の日付(S30 の報道、10-Q の XBRL 日付と一致) |
| CyberArk 買収: 対価の条件 | CYBR 1株あたり 現金 $45 + PANW 株 2.2005 株 | [S30] | 26% のプレミアム(S30 の記載) |
| CyberArk 買収: 対価(headline) | 約 25,000 | [S54][S30] | 発表時の総額。確定会計値とは別 |
| CyberArk 買収: 対価(会計上の確定値) | 21,061 | [S28] | 10-Q(2026-04-30 期): 現金 2,308、普通株 18,488(112 百万株)、置換株式報奨 265。headline との差は未確定(株価換算の違いと推測。推測は未検証) |
| CyberArk 買収: 発行株数 | 112 百万株 | [S28] | 10-Q の記載 |
| CyberArk 買収: 取得 PPA(のれん・無形資産) | **欠損** | — | 未取得。10-Q/10-K の買収注記で確認要 |
| Chronosphere 買収: 発表日 | 2025-11-19(推定) | [S32][S33] | Q1 FY2026 決算と同日発表との記載。日付は当該決算日からの推定 |
| Chronosphere 買収: 完了日 | 2026-01-29 | [S31] | 会社リリース(投資家サイト)の記載 |
| Chronosphere 買収: 金額 | 3,350(発表時) | [S32][S33] | 完了時の報道では「非開示」との記載あり(不一致)。現金と置換株式報奨を含む総額と報道 |
| Protect AI 買収 | 対価 **欠損** | [S28] | 2025 年に取得(10-Q 内の取得 PPA 表に記載あり。取得日・対価は未確認) |
| QRadar SaaS 取得(IBM から) | 対価 **欠損** | [S22] | 2024 年。NGS ARR 寄与は約 74(百万ドル、FY25 Q1 時点) |
| その他 2025〜2026 年の買収 | **欠損** | — | 未検索 |

---

## 表2 四半期業績(直近10四半期)

単位: US$ 百万。EPS はドル。「分割前」は 2024年12月の 2:1 株式分割前の公表値。
「約」の売上は四捨五入値。FCF は会社の定義する調整後 FCF(GAAP 由来の FCF ではない)。

| 四半期 | 期末日 | 総売上 | 製品売上 | S&S売上 | GAAP粗利率 | non-GAAP営業利益率 | GAAP営業利益 | GAAP純利益 | GAAP EPS | non-GAAP EPS | SBC | 営業CF | capex | FCF(調整後) | 希薄化後株数 | 備考 | 出典 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY24 Q3 | 2024-04-30 | 約2,000(前年比 +15%) | 欠損 | 欠損 | 欠損 | 26(%、リリース記載。第三者計算は 25.6) | 欠損 | 278.8 | 0.79(分割前)/ 0.39(分割後) | 1.32(分割前)/ 0.66(分割後) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | non-GAAP 純利益 454.9。通期 non-GAAP EPS ガイダンス(分割前)5.56〜5.58 | [S25][S20] |
| FY24 Q4 | 2024-07-31 | 約2,200(前年比 +12%) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 357.7 | 1.01(分割前) | 1.51(分割前) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | non-GAAP 純利益 522.2。FY25 Q1 の non-GAAP EPS ガイダンス(分割前)1.47〜1.49 | [S24][S18] |
| FY25 Q1 | 2024-10-31 | 約2,100(前年比 +14%) | 欠損 | 欠損 | 欠損 | 28.8 | 欠損 | 350.7 | 0.99(分割前) | 1.56(分割前)/ 0.78(分割後) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | QRadar SaaS 由来 NGS ARR 約 74 | [S22][S16] |
| FY25 Q2 | 2025-01-31 | 約2,300(前年比 +14%) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 267(前年 Q2 の比較値)※当期は下記 | 0.38 | 0.81 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | non-GAAP 純利益 約 600(四捨五入値) | [S21][S13] |
| FY25 Q3 | 2025-04-30 | 約2,300(前年比 +15%) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損(約 300) | 0.37 | 0.80 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | non-GAAP 純利益 約 600(四捨五入値) | [S20] |
| FY25 Q4 | 2025-07-31 | 約2,500(前年比 +16%) | 欠損 | 欠損 | 欠損 | 欠損(計算: 約 31%、非掲載) | 497(前年 Q4 の比較値 ※下記注) | 253.8 | 0.36 | 0.95 | 欠損 | 約 1,000 | 欠損 | 954 | 欠損 | non-GAAP 営業利益 768、non-GAAP 純利益 673.0 | [S18][S01] |
| FY26 Q1 | 2025-10-31 | 約2,500(前年比 +16%) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 334 | 0.47 | 0.93 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | non-GAAP 純利益 662。Q2 ガイダンス EPS 0.93〜0.95 | [S16][S17] |
| FY26 Q2 | 2026-01-31 | 約2,600(前年比 +15%) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 432 | 0.61 | 1.03 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | non-GAAP 純利益 732。前年 GAAP 純利益 267 / EPS 0.38 | [S13][S14] |
| FY26 Q3 | 2026-04-30 | 約3,000(前年比 +31%。うち買収寄与 388) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | -177 | -0.22 | 0.85 | 欠損 | 欠損 | 欠損 | 910 | 欠損 | non-GAAP 純利益 684。Zacks コンセンサス 0.81 | [S08][S10] |
| FY26 Q4 | 2026-07-31 | 3,410(前年比 +34%) | 欠損 | 欠損 | 欠損 | 欠損 | 172(前年 497) | -282 | -0.35 | 1.02 | 欠損 | 約 1,400 | 欠損 | 約 1,300 | 欠損 | non-GAAP 営業利益 約 1,000(前年 768)。non-GAAP 純利益 853。コンセンサス EPS 0.98、売上 3,350 | [S01][S02][S03] |

注記
- FY25 Q4 の GAAP 営業利益 497 は、FY26 Q4 の比較値として S01 に記載。FY25 Q4 の当期値は未確認。
- FY25 Q2 の GAAP 純利益 267 は、FY26 Q2 リリースの前年比較値(S13)。FY25 Q2 の当期値は表記されたが、本表では比較値と併記している。
- 営業CF(Q4 FY25 約 1,000、Q4 FY26 約 1,400)は四捨五入値。調整後 FCF(Q4 FY25 954、Q4 FY26 約 1,300)は会社の定義。
- non-GAAP 営業利益率の計算値(例: FY26 Q4 は約 1,000 ÷ 3,410 ≈ 29%)は公表値ではないため表には入れていない。
- 希薄化後株数の計算値(non-GAAP 純利益 ÷ non-GAAP EPS: FY26 Q3 は約 805、FY26 Q4 は約 836)は公表値ではないため表には入れていない。
- FY24 Q3〜FY25 Q1 の EPS は分割前の公表値を主に記録し、分割後の値は出典がある場合のみ併記。

---

## 表3 根幹KPI(直近10四半期)

| 四半期 | NGS ARR(次世代セキュリティARR、百万ドル) | NGS ARR 前年比 | RPO(残存履行義務) | RPO 前年比 | cRPO | 総請求額(billings) | プラットフォーム化顧客数 | その他プラットフォーム指標 | 出典 |
|---|---|---|---|---|---|---|---|---|---|
| FY24 Q3 | 欠損(公式未取得。第三者 4,520 は不採用。前年比からの逆算は約 3,800 だが公表値ではない) | 欠損 | 11,300 | +23% | 欠損 | 欠損 | 欠損 | 欠損 | [S25] |
| FY24 Q4 | 4,220 | +43% | 12,700 | +20% | 欠損 | 欠損 | 欠損 | 欠損 | [S24][S57] |
| FY25 Q1 | 4,500 | +40% | 12,600 | +20% | 欠損 | 欠損 | 欠損 | QRadar SaaS 由来 NGS ARR 約 74 | [S22][S23] |
| FY25 Q2 | 4,800 | +37% | 13,000 | +21% | 欠損 | 欠損 | 欠損 | 欠損 | [S21] |
| FY25 Q3 | 5,100(第三者 5,090) | +34% | 13,500 | +19% | 欠損 | 欠損 | 欠損 | 欠損 | [S20][S56] |
| FY25 Q4 | 5,600 | +32% | 15,800 | +24% | 欠損 | 欠損 | 欠損 | 「プラットフォーム型の新規取引の記録更新」(定性)。プラットフォーム型顧客の NRR 120%(定性、低単位の解約率) | [S18][S19] |
| FY26 Q1 | 5,900(トランスクリプト 5,850) | +29% | 15,500 | +24% | 欠損 | 欠損 | 欠損 | 欠損 | [S16][S17] |
| FY26 Q2 | 6,300 | +33% | 16,000 | +23% | 欠損 | 欠損 | 欠損 | 欠損 | [S13][S14] |
| FY26 Q3 | 8,100(別要約 8,130) | +60% | 18,400 | +36% | 欠損 | 欠損 | 欠損 | 買収寄与: NGS ARR 1,600、RPO 1,800、売上 388(CyberArk・Chronosphere)。有機的 NGS ARR 成長は約 28%(第三者要約) | [S08][S10] |
| FY26 Q4 | 9,100 | +63% | 21,200 | +34% | 欠損 | 欠損 | 欠損 | 当四半期の NGS ARR 純増は約 1,000(百万ドル単位ではなく「約 10 億ドル」) | [S01][S02] |

注記
- KPI の定義変更や開示停止は、検索結果からは確認できず。
- FY26 Q3 以降の NGS ARR と RPO には買収分が含まれる。有機的成長率は第三者要約のみ。
- cRPO、billings、プラットフォーム化顧客数は、検索結果のどの出典にも記載がなく、全期間欠損。

---

## 表4 年度業績(FY2022〜FY2026)

決算期末: FY2022 2022-07-31、FY2023 2023-07-31、FY2024 2024-07-31、FY2025 2025-07-31、FY2026 2026-07-31。

| 項目 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | 出典 | 備考 |
|---|---|---|---|---|---|---|---|
| 総売上 | 欠損 | 欠損 | 約 8,030 | 9,220 | 約 11,480 | FY24: [S57]、FY25: [S01]、FY26: [S01][S11] | FY2024 は年次報告書の値(S57)。FY2026 は二次要約 |
| 製品売上 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | — | 未取得 |
| S&S売上 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | — | 未取得 |
| GAAP 営業利益 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | — | 未取得 |
| non-GAAP 営業利益率 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | — | FY2024 は「前年比 300bp 超の改善」(定性、S24 系) |
| GAAP 純利益 | 欠損 | 欠損 | 約 2,580(集計サイト) | 約 1,100(集計サイト、四捨五入) | 欠損 | [S49][S48] | 単独の集計サイト値。一次資料未確認。FY2026 の四半期合計は 307(計算値、公表値ではない) |
| GAAP EPS | 欠損 | 欠損 | 7.28(分割前) | 欠損 | 欠損 | [S24] | FY2024 の GAAP EPS は分割前。FY2025 通期は未取得 |
| non-GAAP EPS | 欠損 | 欠損 | 欠損 | 欠損(四半期合計は 3.34、計算値) | 欠損(四半期合計は 3.83、計算値) | [S16][S18][S20][S21][S08][S10][S01] | 通期の公表値は未取得。FY2026 通期ガイダンス 3.77〜3.79 [S09] |
| SBC | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | — | 未取得 |
| 営業CF | 欠損 | 約 2,780(集計サイト) | 約 3,260(集計サイト) | 約 3,716 | 欠損(Q4 のみ約 1,400) | [S49][S48] | 集計サイトの値。一次資料未確認 |
| capex | 欠損 | 欠損 | 欠損 | 約 246〜247(集計サイト) | 欠損 | [S48] | 集計サイトの値 |
| FCF | 欠損 | 欠損 | 約 3,100(集計サイトの OCF − capex) | 約 3,469〜3,500(集計サイト) | 欠損 | [S49][S48] | FY2026 の調整後 FCF は下記 |
| FCF マージン | 欠損 | 欠損 | 欠損(計算値 約 38.6%) | 約 37.6%(集計サイト) | 調整後 FCF マージン 38.4%(会社) | [S48][S01][S03] | FY2026 は会社の調整後指標。GAAP ベースの FCF マージンではない |
| 期末希薄化後株数 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | — | FY2027 ガイダンス前提は 844〜847 百万株 [S04] |
| 自社株買い額 | 欠損 | 250.0(3.6 百万株) | 566.7(4.0 百万株) | 欠損(集計サイトは 0 と表示、未確認) | 欠損 | [S26][S45] | FY2023・FY2024 は FY2025 の 10-K(S26)から。FY2025 の 0 は単独の集計サイト値 |

---

## 表5 ガイダンス履歴

単位: 売上・NGS ARR・RPO は百万ドル、EPS はドル(分割前は注記)。

| 年度 | 時点 | 売上 | NGS ARR | RPO | 非GAAP EPS | FCF マージン | 出典 | 備考 |
|---|---|---|---|---|---|---|---|---|
| FY2024 | 期初(2023-08) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | — | 未取得 |
| FY2024 | Q3 時点(2024-05) | 7,990〜8,010 | 欠損 | 欠損 | 5.56〜5.58(分割前) | 欠損 | [S25] | 通期 |
| FY2024 | 最終実績 | 約 8,030 | 4,220 | 12,700 | 欠損 | 集計サイトで 38.0〜39.0% のガイダンス(FY2024 の実績は未確認) | [S57][S24][S49] | |
| FY2025 | 期初(2024-08) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | — | 未取得。FY2025 Q1 の non-GAAP EPS ガイダンス(四半期、分割前)1.47〜1.49 [S24] |
| FY2025 | Q1 時点(2024-11) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | [S22] | 「三項目とも引き上げ」(定性)。数値は未取得 |
| FY2025 | Q2 時点(2025-02) | 欠損 | 欠損 | 欠損 | 3.18〜3.24(分割後、第三者要約) | 欠損 | [S21] | 第三者要約のため未検証。Q3 の NGS ARR ガイダンス 5,030〜5,080、RPO 13,500〜13,600 |
| FY2025 | Q3 時点(2025-05) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | [S56] | 「FY2025 ガイダンスを引き上げ」(見出し)。数値は未取得 |
| FY2025 | Q4 ガイダンス(四半期) | 2,490〜2,510 | 5,520〜5,570 | 欠損 | 0.87〜0.89 | 欠損 | [S19] | 実績: 売上 約 2,500、NGS ARR 5,600、EPS 0.95(上回る) |
| FY2025 | 最終実績 | 9,220 | 5,600 | 15,800 | 欠損(四半期合計は 3.34、計算値) | 約 37.6%(集計サイト) | [S01][S18][S48] | |
| FY2026 | 期初(2025-08) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | — | 未取得 |
| FY2026 | Q1 時点(2025-11) | 欠損 | 7,000〜7,100 | 18,600〜18,700 | 欠損 | 欠損 | [S17] | 通期の目標(トランスクリプトの記載) |
| FY2026 | Q2 時点(2026-02) | 11,280〜11,310 | 欠損 | 欠損 | 欠損 | 欠損 | [S15] | 第三者要約(売上の引き上げ) |
| FY2026 | Q3 時点(2026-05) | 11,415〜11,425(S09)/ 11,420〜11,430(S11) | 8,900〜8,950 | 欠損 | 3.77〜3.79 | 欠損 | [S09][S11][S08] | 売上ガイダンスは出典で不一致(未確定)。NGS ARR の大幅引き上げは買収分を含む(S08 の買収寄与 1,600 との対応) |
| FY2026 | Q4 ガイダンス(Q3 時点) | 3,345〜3,355 | 欠損 | 欠損 | 0.96〜0.98 | 欠損 | [S08][S09] | 実績: 売上 3,410、EPS 1.02(上回る) |
| FY2026 | Q2 ガイダンス(Q1 時点、四半期) | 欠損 | 6,110〜6,140 | 15,750〜15,850 | 0.93〜0.95 | 欠損 | [S16][S17] | 実績: NGS ARR 6,300、RPO 16,000、EPS 1.03(上回る) |
| FY2026 | 最終実績 | 約 11,480 | 9,100 | 21,200 | 欠損(四半期合計は 3.83、計算値) | 調整後 38.4% | [S01][S03] | |
| FY2027 | 期初(2026-09-01) | 14,100〜14,200(前年比 +23〜24%) | 11,075〜11,175(前年比 +22〜23%) | 欠損 | 4.16〜4.19(原典未確認) | 欠損 | [S01][S04][S06] | 非GAAP 営業利益率の目標 29.5%(記事が途切れ、全文未確認)[S04] |
| FY2027 | Q1 ガイダンス(2026-09-01) | 3,300〜3,310 | 9,540〜9,560(前年比 +63%) | 欠損 | 0.96〜0.98 | 欠損 | [S01][S04] | |
| FY2027 | 前提 | 欠損 | 欠損 | 欠損 | 希薄化後株数 844〜847 百万株 | 欠損 | [S04] | 非GAAP の除外項目: SBC 関連費用、買収関連費用、無形資産償却など |

中期目標
- FY2030 NGS ARR 200億ドル(20B)。CEO が言及(S01)。NGS ARR の定義・期限(FY2030 年 7 月期)は要約からの推定。定義の詳細は未確認。
- 調整後 FCF マージン 40% を FY2028 に達成する目標(S01)。

---

## 表6 コンセンサス(FY2027〜FY2031)

TradingView の直接取得は不可(WebFetch・curl 不可)。TradingView の要約(allowed_domains 指定の検索)と第三者要約で補った。

| 会計年度 | 売上コンセンサス(平均・高・低) | non-GAAP EPS コンセンサス(平均・高・低) | アナリスト数 | 出典 | 出典の日付 |
|---|---|---|---|---|---|
| FY2027(2027-07 期) | 平均: 欠損。参考: Zacks 推計の成長率 +23.4%(TradingView 要約の計算、約 14.2B)。高・低: 欠損 | 平均 約 4.11(Fiscal.ai 経由)。高・低: 欠損 | 欠損 | [S11][S04] | 2026-09 上旬(記事日付は未確認) |
| FY2028 | 平均: 欠損。参考: 成長率 +15.1%(Zacks 推計、約 16.3B、TradingView 要約の計算)。高・低: 欠損 | 欠損 | 欠損 | [S11] | 2026-09 上旬 |
| FY2029 | 欠損 | 欠損 | 欠損 | — | — |
| FY2030 | 欠損 | 欠損 | 欠損 | — | — |
| FY2031 | 欠損 | 欠損 | 欠損 | — | — |

補足
- 次の四半期(Q1 FY2027)のコンセンサス: 売上 約 3,310、EPS 0.97(TradingView 要約)[S11]。
- FY2027 NGS ARR の成長率コンセンサス: 22.1%(FactSet 経由、会社ガイダンスの成長率と整合)[S04]。
- 誤記の疑い: Benzinga の FY2027 EPS コンセンサス 2.01(S44)。他の出典(4.11)と乖離するため不採用。
- アナリスト目標株価(平均・高・低): **欠損**(未取得、検索上限に到達)。
- レーティング分布(買い・ホールド・売り): **欠損**(未取得)。

---

## 表7 バランスシート(直近四半期末 = 2026-07-31)

検索結果からは、いずれの項目の数値も取得できなかった。以下は確認先。

| 項目 | 値 | 出典 | 備考 |
|---|---|---|---|
| 現金 | **欠損** | — | 確認先: FY2026 10-K(S27) |
| 短期投資 | **欠損** | — | 同上 |
| 長期投資 | **欠損** | — | 同上 |
| 有利子負債(転換社債の残高・満期) | **欠損** | — | 同上。転換社債・買収資金の借入の有無は未確認 |
| オペレーティングリース負債 | **欠損** | — | 同上 |
| 繰延収益(短期・長期) | **欠損** | — | 同上 |
| 購入コミットメント | **欠損** | — | 同上 |
| のれん・無形資産 | **欠損** | — | 同上。CyberArk・Chronosphere の PPA を含む |
| 株主資本 | **欠損** | — | 同上 |

---

## 出典一覧(取得日 2026-10-11)

一次資料の URL は、本文を取得していないものを含む(注: 本文は未取得)。

| ID | 内容 | URL | 種別 |
|---|---|---|---|
| S01 | Pulse 2.0、FY2026 Q4 要約 | https://pulse2.com/palo-alto-networks-q4-revenue-rises-34-to-3-41-billion-as-next-generation-security-arr-jumps-63-to-9-1-billion/ | 二次 |
| S02 | SEC 8-K、FY2026 Q4 決算リリース(本文未取得) | https://www.sec.gov/Archives/edgar/data/0001327567/000132756726000019/ex991q426earningsrelease.htm | 一次(URL のみ確認) |
| S03 | Placera、FY2026 Q4 リリース転載 | https://www.placera.se/pressmeddelanden/palo-alto-networks-reports-fiscal-fourth-quarter-and-fiscal-year-2026-financial-results-20260901 | 一次転載 |
| S04 | Stocktwits、FY2026 Q4 と FY2027 ガイダンス記事 | https://stocktwits.com/news-articles/markets/equity/panw-stock-in-focus-palo-alto-networks-tops-q4-estimates-issues-upbeat-fy27-guidance/cZsoxeoRJMM | 二次 |
| S05 | Invezz、2026-09-02 の株価反応 | https://invezz.com/au/news/2026/09/02/palo-alto-crushes-earnings-expectations-stock-is-down-8percent-heres-why/ | 二次 |
| S06 | AskTraders、Q4 分析 | https://www.asktraders.com/analysis/palo-alto-networks-beats-q4-estimates-and-raises-guidance-despite-tech-sell-off/ | 二次 |
| S07 | Chartmill、Q4 分析 | https://www.chartmill.com/news/external/142557/panw-q4-earnings-beat-estimates-on-platformization-strength | 二次 |
| S08 | Dukascopy(TipRanks 系)、FY2026 Q3 要約 | https://www.dukascopy.com/swiss/english/marketwatch/market-news/Expert-Commentary/155156 | 二次 |
| S09 | TradingView(Zacks)、FY2026 Q3 決算要約と通期ガイダンス | https://www.tradingview.com/news/zacks:94e74b9a6094b:0-palo-alto-networks-q3-earnings-and-revenues-surpass-estimates/ | 二次(TradingView) |
| S10 | SEC 8-K、FY2026 Q3 決算リリース(本文未取得) | https://www.sec.gov/Archives/edgar/data/0001327567/000132756726000012/ex991q326earningsrelease.htm | 一次(URL のみ確認) |
| S11 | TradingView、PANW Q4'26 EPS 推計とコンセンサス要約 | https://www.tradingview.com/news/tradingview:598a4d54d732c:0-panw-q4-26-earnings-eps-estimate-is-0-98-usd/ | 二次(TradingView) |
| S13 | PANW 投資家向けリリース、FY2026 Q2 | https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-reports-fiscal-second-quarter-2026-financial-results | 一次(リリース) |
| S14 | Barchart、FY2026 Q2 リリース転載 | https://www.barchart.com/story/news/265551/palo-alto-networks-reports-fiscal-second-quarter-2026-financial-results | 一次転載 |
| S15 | Value the Markets、FY2026 Q2 要約 | https://value-the-markets-production-butx6j.laravel.cloud/news/palo-alto-networks-q2 | 二次 |
| S16 | PANW リリース、FY2026 Q1 | https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-reports-fiscal-first-quarter-2026-financial-results | 一次(リリース) |
| S17 | SEC 8-K、FY2026 Q1 と決算トランスクリプト(AOL) | https://www.sec.gov/Archives/edgar/data/1327567/000132756725000032/ex991q126earningsrelease.htm / https://www.aol.com/articles/palo-alto-networks-panw-earnings-224759858.html | 一次 / 二次 |
| S18 | PANW リリース、FY2025 Q4 と通期 | https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-reports-fiscal-fourth-quarter-and-fiscal-year-2025-financial-results / https://www.sec.gov/Archives/edgar/data/1327567/000132756725000024/ex991q425earningsrelease.htm | 一次 |
| S19 | Futurum、FY2025 Q4 分析(Q4 ガイダンス) | https://futurumgroup.com/insights/palo-alto-networks-q4-fy-2025-earnings-show-16-growth-strong-arr-momentum | 二次 |
| S20 | PANW リリース、FY2025 Q3 と Futurum Q3 分析 | https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-reports-fiscal-third-quarter-2025-financial-results / https://futurumgroup.com/insights/palo-alto-networks-q3-2025-results-indicate-sustained-platform-and-ai-momentum | 一次 / 二次 |
| S21 | SEC 8-K、FY2025 Q2 と fintool 要約 | https://www.sec.gov/Archives/edgar/data/1327567/000132756725000006/ex991q225earningsrelease.htm / https://fintool.com/app/research/companies/PANW/earnings/Q2%202025 | 一次 / 二次 |
| S22 | SEC 8-K、FY2025 Q1 | https://www.sec.gov/Archives/edgar/data/1327567/000132756724000036/ex991q125earningsrelease.htm | 一次 |
| S23 | Benzinga、FY2025 Q1 要約 | https://www.benzinga.com/news/earnings/earnings-beats/24/11/42116266/palo-alto-networks-posts-q3-beat-analysts-are-most-impressed-by-platform-acceleratio | 二次 |
| S24 | SEC 8-K、FY2024 Q4 と通期 | https://www.sec.gov/Archives/edgar/data/1327567/000132756724000023/ex991q424earningsrelease.htm | 一次 |
| S25 | SEC 8-K、FY2024 Q3 と Yahoo(Zacks)要約 | https://www.sec.gov/Archives/edgar/data/1327567/000132756724000015/ex991q324earningsrelease.htm / https://malaysia.news.yahoo.com/palo-alto-panw-q3-earnings-133400273.html | 一次 / 二次 |
| S26 | 10-K、FY2025(2025-08-29 提出) | https://www.sec.gov/Archives/edgar/data/1327567/000132756725000027/panw-20250731.htm | 一次(本文未取得、スニペットのみ) |
| S27 | 10-K、FY2026 | https://www.sec.gov/Archives/edgar/data/0001327567/000132756726000023/panw-20260731.htm | 一次(スニペットのみ) |
| S28 | 10-Q、2026-04-30 期(FY2026 Q3) | https://www.sec.gov/Archives/edgar/data/0001327567/000132756726000015/panw-20260430.htm | 一次(スニペットのみ) |
| S29 | 10-Q、2026-01-31 期(FY2026 Q2) | https://www.sec.gov/Archives/edgar/data/1327567/000132756726000005/panw-20260131.htm | 一次(スニペットのみ) |
| S30 | CRN Asia、CyberArk 買収完了 | https://www.crnasia.com/news-network/2026/palo-alto-networks-completes-25b-acquisition-of-cyberark-for-identity-security-push | 二次 |
| S31 | PANW 投資家向けリリース、Chronosphere 買収完了 | https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-completes-chronosphere-acquisition-unifying | 一次(リリース) |
| S32 | SecurityWeek、Chronosphere 買収 $3.35B | https://securityweek.com/palo-alto-networks-to-acquire-observability-platform-chronosphere-in-3-35-billion-deal/ | 二次 |
| S33 | Security Boulevard、Chronosphere 買収(2025-11) | https://securityboulevard.com/2025/11/palo-alto-networks-to-acquire-ai-era-observability-platform-chronosphere-for-3-35-billion/ | 二次 |
| S34 | PANW 経営陣ページ | https://paloaltonetworks.com/about-us/management | 一次 |
| S35 | Carnegie、Nikesh Arora プロフィール(2026-06) | https://carnegie.org/?p=44399 | 二次 |
| S36 | Robinhood、PANW 株価ページ | https://robinhood.com/stocks/panw | 集計サイト |
| S37 | TradingView、NASDAQ-PANW | https://www.tradingview.com/symbols/NASDAQ-PANW/ | 集計サイト |
| S38 | Tradersunion、株価記事 | https://tradersunion.com/news/stocks/show/3682745-palo-alto-networks-rises-3-95percent/ | 二次 |
| S39 | InvestSmart、株価(2026-08-19 終値 374.14) | https://www.investsmart.com.au/security/nasdaq/panw/palo-alto-networks-inc/share-price | 集計サイト |
| S40 | ChartRow、PANW(2026-07-24 終値、株式数) | https://chartrow.com/quote/panw | 集計サイト |
| S41 | Trendlyne、取締役会・決算日程 | https://us.trendlyne.com/us/equity/board-meeting/PANW/1554502/palo-alto-networks-inc-board_meeting/ | 第三者カレンダー |
| S42 | AJ Bell、会社情報(決算日) | https://www.ajbell.co.uk/market-research/sub/NASDAQ:PANW/company-info | 第三者カレンダー |
| S43 | MarketScreener、決算カレンダー | https://in.marketscreener.com/quote/stock/PALO-ALTO-NETWORKS-INC-11067980/calendar/ | 第三者カレンダー |
| S44 | Benzinga、業績予想ページ(誤記の疑い) | https://kr.benzinga.com/quote/PANW/earnings-forecasts | 集計サイト |
| S45 | Equibles、自社株買い | https://equibles.com/stocks/panw/buybacks | 集計サイト |
| S46 | TipRanks、株価履歴(2025-10-09 終値 215.17 を含む) | https://www.tipranks.com/stocks/panw/historical-prices | 集計サイト |
| S47 | Yahoo Finance、PANW プロフィール | https://finance.yahoo.com/quote/PANW/profile | 集計サイト |
| S48 | ChartRow、FY2025 キャッシュフロー / StockAnalysis(TSX 上場ページ) | https://chartrow.com/quote/panw/cash-flow / https://stockanalysis.com/quote/tsx/PANW/financials/ | 集計サイト |
| S49 | AlphaQuery(FY2024 FCF)と moomoo(キャッシュフロー) | https://alphaquery.com/stock/PANW/fundamentals/annual/free-cash-flow / https://www.moomooapp.com/stock/PANW-US/financial/cash-flow | 集計サイト |
| S50 | Pluang、PANW 株価 | https://pluang.com/en/asset/usstock/PANW/10240 | 集計サイト |
| S51 | Kraken、PANW 株価 | https://www.kraken.com/stocks/panw | 集計サイト |
| S52 | Investing.com、PANW 株価(表示が古い) | https://www.investing.com/equities/palo-alto-netwrk | 集計サイト |
| S54 | Click On Detroit(AP)、CyberArk 買収発表(2025-07-30) | https://www.clickondetroit.com/business/2025/07/30/palo-alto-networks-buying-cyberark-in-cash-and-stock-deal-valued-at-about-25-billion/ | 二次(AP) |
| S56 | iTiger、FY2025 Q3(ガイダンス引き上げ見出し) | https://www.itiger.com/news/2537230086 | 二次 |
| S57 | 年次報告書(ARS)FY2024 | https://www.sec.gov/Archives/edgar/data/1327567/000130817924000772/panw4345341-ars.pdf | 一次(スニペットのみ) |

注: S12、S53、S55 などの欠番は取得段階で使わなかった ID。

---

## 追加の制約メモ
- TradingView の直接取得は不可(ネットワーク方針)。TradingView 関連の数値は検索要約からのみ。
- 集計サイトの値(S36〜S52)は Tier 3〜4 の扱い。一次資料と食い違う場合は一次資料を優先する。
- 本ファイルの数値は、検索結果の要約・スニペットに基づく。一次資料(8-K・10-K・10-Q)の本文照合は未了。
