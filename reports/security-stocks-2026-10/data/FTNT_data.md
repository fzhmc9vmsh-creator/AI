# FTNT(Fortinet)定量データ表

- 収集者: Haiku / 取得日: 2026-10-11(第2回更新: 同日、検索上限回復後)
- 評価基準日: 2026-10-11 / 株価基準日: 2026-10-09(**未確定**: 194.75 は単一の二次出典。§2 #1)
- 単位: 金額 US$ mn、EPS US$、比率 %。決算期末 12月31日。
- 記号: **※** = 出典が概数(四捨五入)のまま。**(算出)** = 出典値からの計算(丸め誤差あり)。**(単独)** = 単一出典。**(二次)** = 報道・データサイト等の要約。IR・SEC 本文は未読で、数値は検索要約から採取。**未確定** = 出典間で食い違い、§2 参照。
- CSV (`FTNT_quarterly.csv`) には開示値(※・単独・二次を含む)のみを入れ、(算出)値は空欄にしている。

---

## 0. 取得の制約と更新履歴

- 取得手段は WebSearch のみ。WebFetch・curl は使っていない。
- **SEC・IR の一次文書本文は読めていない。** 数値はすべて検索要約または転載からの採取。ただし "Financial_Report" や 10-K の財務表の抜粋が要約に含まれた項目がある(§6 の注)。
- 第1回: WebSearch 約24回で上限到達。
- 第2回(上限回復後、12回まで): 株価・コンセンサス・SBC・バランスシート・FY2022〜2025 年度・ARR・2026 初期 EPS ガイダンス・自社株買いを検索。**12回で上限に到達**し、以降の検索を停止した。
- 未検索のまま残った項目: 2021 年度の全項目、2022 年度の売上・営業利益率、2024 年の初期ガイダンス、買収、中期目標、2026Q2 の ARR 実額と FortiGate 更新サイクル、2026年の希薄化株数、2026Q2 の senior notes の帳簿価額。

---

## 1. 欠損項目一覧(第2回時点、重要度順)

1. **2026-10-09 終値の確定**: 194.75 は単一出典で、日中高値の記録と矛盾する(§2 #1)。確定値を要確認。
2. **希薄化後株数(四半期の直接値)**: 2026Q2 の直接値は未開示のため、算出(約739mn株)のみ。期末株数(2024・2025 年度)は欠損。
3. **2021〜2022 年度の売上・billings・non-GAAP 値・営業CF・capex・FCF**: 未検索。2022 年度は GAAP 純利益と EPS のみ(§6)。
4. **粗利率(製品・サービス)**の全期間: 欠損。
5. **GAAP 純利益・GAAP EPS**: 2024Q1〜Q4、2025Q1・Q3・Q4 の純利益、2026Q1 の純利益は欠損。
6. **non-GAAP EPS**: 2024Q1(単独)・Q2・Q3 は欠損。2024Q4 は 0.74(二次)。
7. **営業CF・capex**: 2024Q1・Q3、2026Q1・Q2、2025Q4 以外は欠損。2024Q4 の CF は欠損。
8. **ARR(Unified SASE・SecOps)**: 2026Q1・Q2 の実額・前年比は欠損。2025Q4 は二次出典のみ(§2 #20)。**FortiGate 更新サイクルの進捗**: 2026 年の値は欠損。**$1M超案件**: 件数は欠損(増加率のみ)。
9. **繰延収益**: 2024Q1・Q3・Q4、2025Q1〜Q4 の総額は欠損。**RPO**: 2026Q2 は単独・未確定、他の大半は欠損。
10. **コンセンサス**: 2026年の売上は単独(§8)。2027・2028 年の売上・EPS は出典間で不一致。2029 年は単独。2030 年は全項目欠損。アナリスト数の一部のみ。
11. **買収(2024〜2026: Lacework、Next DLP 等)、中期目標、2024年の初期ガイダンス**: 未検索。
12. **バランスシート**: 2026-06-30 の社債の帳簿価額、リース負債、購入コミットメント、のれん・無形資産、株主資本は欠損。2025-12-31 の長期繰延収益は欠損。
13. **自社株買い額**: 2024・2025 年度の年間実績は欠損(§6)。

---

## 2. 出典間で食い違った数値(未確定を含む)

| # | 項目 | 出典A | 出典B | 扱い |
|---|---|---|---|---|
| 1 | 2026-10-09 終値と日中高値 | 終値 194.75(Zacks 系・単独。前日比 +2.99% は 10-08 の約 189.1 と整合)(S29) | 日中の「史上最高値」192.55(投資家向け見出し。日付不明。S31)。終値 194.75 より低く、同日なら不整合 | **未確定**。194.75 を暫定採用。10-02 の「記録的 182.09」は日中値なら終値 180.95 と両立しうるが、記事の曜日が不整合(前回からの持ち越し) |
| 2 | 2026Q2 サービス売上 | 1.27bn(10-Q 要約。S03。6か月差分とも整合) | 1.28bn(Quartr 要約。S09) | **未確定**。表2は 1,270 |
| 3 | 2026Q2 RPO | 7.73bn(Panabee 単独。S09) | 10-Q 本文で確認できず | **未確定**。CSV は空欄 |
| 4 | 2025Q2 ARR 伸び率 | Unified SASE ARR +22%、SecOps ARR +35%(S14) | Unified SASE billings +21%、SecOps billings +31%(別要約) | **未確定**。CSV は空欄 |
| 5 | 2025Q4 FCF | 577.4(開示 FCF。S11・S12) | 589(調整後FCF。コール要約) | 両方記載。CSV は 577.4 |
| 6 | 2025Q4 EPS のラベル | 非GAAP 0.81(市場予想を 0.07 上回る。S12) / GAAP 0.68(二次。S45) | 第2回: 非GAAP 0.81 と FY 2.76 の記述と整合 | **解消**。非GAAP 0.81・GAAP 0.68 として採用 |
| 7 | 2025Q3 サービス売上 | 約1.17bn(単独。S13 系) | 1,720 − 559.3 = 約1,161(算出。丸め範囲 1,156〜1,166) | **未確定**。表2は「≈1,170(単独)」 |
| 8 | 2026Q3 決算日 | 2026-10-28(会社告知 2026-10-02。S20) | 2026-11-05(Trendlyne 予定表。S20) | 会社告知を採用 |
| 9 | FY2026 の「引き上げ前」売上ガイダンス | 7.71〜7.87bn(Q1 リリース。S06) | 約8.0〜8.2bn(MarketBeat の Q2 要約。S08) | 7.71〜7.87bn を採用 |
| 10 | FY2026 の初期 non-GAAP EPS | 2.94〜3.00(TradingView 系要約。S46) | 2.94〜3.00(Q4 2025 要約。S45 等) | **二次2件で一致**。一次(リリース本文)は未確認 |
| 11 | 2026Q2 non-GAAP EPS | 0.901(S08) | 0.90(S07・S01 転載) | 同一値の丸め差。0.901 を採用 |
| 12 | 2026Q2 GAAP 純利益 | 606.3(単独。前年 440.1。S09 系) | 10-Q 本文で確認できず | **単独・未確定**。EPS 0.82 と整合 |
| 13 | コンセンサス評価 | 最新: Hold(MarketBeat 2026-10-01、36人: Buy 12・Hold 19・Sell 5。S37)。Benzinga 5 Buy / 15 Hold / 3 Sell(S39) | 2026-09 初旬の Benzinga 表示は「Buy」(22人。S24) | 最新2件は **Hold**。古い Buy 表示は日付差として **未確定** |
| 14 | アナリスト目標株価平均 | 152.79(MarketBeat 2026-10-01。S37)、156.83(WallStreetZen、表示日不明。S32)、140(Benzinga。S39) | 142.28(StreetInsider 7月末。S25)、114.74(TradingView、ラベル「2027」、日付不明。S26) | **未確定**。評価日と集計元が異なる |
| 15 | 2024Q1 non-GAAP EPS 0.43 | 市場記事(非GAAPと明記なし。S19 系) | 他に出典なし | **単独・非GAAP未確認** |
| 16 | 2026Q1 自社株買い額 | 827(10.6mn株。S06 系要約) | 823.0(10-Q のキャッシュフロー表。S48 系の要約) | **未確定**。計上基準の違いと推定 |
| 17 | 9M SBC | 9M 2025 209.0 / 9M 2024 193.7(費用科目別。S47 要約) | 9M 2025 207.0 / 9M 2024 192.1(キャッシュフロー表。同要約) | **未確定**。表2は費用科目ベース(209.0)を採用。FY(279.5/257.9)の基準も未確認 |
| 18 | FY2026 売上コンセンサス | 8.3bn 平均(StockGuide、9月表示。S33) | 7.81bn 平均(Yahoo、3月表示。S34)。会社ガイダンス 8.02〜8.18 | 日付が異なる。参考。下の表 8 に併記 |
| 19 | FY2028 コンセンサス | EPS 4.41、売上 約10.3bn(WallStreetZen、8-9 表示。S32。売上は整形不良) | EPS 3.93、売上 9.73bn(Chartmill、6月。S35。アナリスト数なし) | **未確定** |
| 20 | 2025Q4 Unified SASE の伸び率 | ARR +11%、ARR $1.28bn(二次。S45) | 2025Q4 Unified SASE billings +40%(前回の別要約)。2025Q2 の ARR +22% | **未確定**。指標の混在と推定。CSV には 11 を入れ、md で注記 |

---

## 3. 表1 基本情報

| 項目 | 値 | 基準日 | 出典 | 備考 |
|---|---|---|---|---|
| 株価(2026-10-09 終値) | **194.75(未確定)** | 2026-10-09 | S29(Zacks 系、単独) | 出典URLは要約から特定できず。§2 #1 |
| 株価(直近の終値、確認済み扱い) | 189.28 | 2026-10-07 | S30(stockanalysis、二次) | |
| 株価(その他の終値) | 180.95(10-02)、173.46(09-25)、156.34(09-04) | 各日 | S30・S21・S22 | 10-08 は日中 189.15 のみ |
| 時価総額 | **約142,897(算出)** = 194.75 × 733.71mn株 | 2026-10-09 | 算出(株数は S21) | 10-09 時点の株数は未確認 |
| 時価総額(参考) | 127,270 | 2026-09-25 | S21(二次) | 173.46 × 733.71 と整合 |
| 発行済株式数(基本) | 733.71 mn株 | 2026-09-25 | S21(二次) | 別値: 732.65mn株(2026-07-17) |
| 希薄化後株数(直近四半期 2026Q2) | **欠損**(算出参考: 約739mn株 = 606.3 ÷ 0.82) | 2026Q2 | S02・S09(算出) | 直接値は未開示。Q3 2026 会社ガイダンス: 741〜745mn株(S08) |
| 52週高値 | **未確定**(日中 192.55 の見出しがあるが日付不明。10-09 の終値 194.75 が正しければ 194.75 以上) | — | S31 | §2 #1 |
| 52週安値 | 73.55(2026-09-25 時点の値。10-09 時点は欠損) | 2026-09-25 | S21 | 窓が動いている可能性 |
| CEO | Ken Xie(Founder, Chairman & CEO) | 2026-07-29 決算コール | S07(二次) | |
| CFO | Christiane Ohlgart | 2026-07-29 決算コール | S07(二次) | COO は John Whittle |
| 直近決算発表日 | 2026-07-29(2026年Q2) | — | S02(転載)・S08 | 2026Q1 は 2026-05-06 |
| 次回決算予定日 | 2026-10-28(水)13:30 PT(2026年Q3) | 告知 2026-10-02 | S20 | Trendlyne の 11-05 は不採用(§2 #8) |
| 買収(2024〜2026: Lacework、Next DLP 等) | **欠損** | — | — | 未検索 |

---

## 4. 表2 四半期業績(2024Q1 〜 2026Q2)

2026Q3 は 2026-10-28 発表予定のため**未発表**。SBC は費用科目別ベース(負債分類の株式報酬を含む)。(算出)値は SBC の一部も含む(§4 注)。

| 四半期 | 期末日 | 総売上 | 製品売上 | サービス売上 | billings | GAAP粗利率 | 製品粗利率 | サービス粗利率 | GAAP営業利益率 | non-GAAP営業利益率 | GAAP純利益 | GAAP希薄化後EPS | non-GAAP希薄化後EPS | SBC | 営業CF | capex | FCF | 希薄化後株数(mn) | 出典 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2024Q1 | 2024-03-31 | 1,350※ | 409※ | 944.4 | 欠損 | 欠損 | 欠損 | 欠損 | 23.7 | 28.5 | 欠損 | 欠損 | 0.43(単独) | 欠損(Q1・Q2 の合計 127.3 は算出) | 830 | 221(算出) | 609 | 欠損 | S19(二次) |
| 2024Q2 | 2024-06-30 | 1,434.3 | 451.9 | 982.4 | 1,540※(前年横ばい) | 欠損 | 欠損 | 欠損 | 30.5 | 35.1 | 欠損 | 欠損 | 欠損 | 欠損(上記合計に含む) | 342 | 欠損 | 欠損 | 欠損 | S18(二次) |
| 2024Q3 | 2024-09-30 | 1,510※ | 473.9 | 1,030※ | 1,580※(+6%、コール) | 欠損 | 欠損 | 欠損 | 31.2 | 36.1 | 欠損 | 欠損 | 欠損 | **66.4** | 608.1 | 36.3(算出) | 571.8 | 欠損 | S17・S47 |
| 2024Q4 | 2024-12-31 | 1,660※ | 574 | 1,086(算出) | 2,000※(+7.4%) | 欠損 | 欠損 | 欠損 | 欠損 | 39(記録的) | 欠損 | 欠損 | 0.74(二次) | 64.2(算出。FY 257.9 − 9M 193.7 ※基準未確定) | 欠損 | 欠損 | 欠損 | 775.2(Q4 加重平均) | S16・Last10K |
| 2025Q1 | 2025-03-31 | 1,540※ | 459 | 1,080※(二次) | 1,600※(+14%) | 欠損 | 欠損 | 欠損 | 欠損 | 34.2 | 欠損 | 0.56 | 0.58 | 66.9(算出 = 6M 136.8 − Q2 69.9) | 欠損 | 欠損 | 782.8 | 欠損 | S15・S48 |
| 2025Q2 | 2025-06-30 | 1,630※ | 欠損(算出 ≈509) | 欠損 | 1,780※(+15%) | 欠損 | 欠損 | 欠損 | 28 | 33 | 欠損 | 0.57(S03 比較値) | 0.64(単独) | **69.9** | 欠損 | 欠損 | 欠損 | 欠損 | S14・S03 |
| 2025Q3 | 2025-09-30 | 1,720※ | 559.3 | ≈1,170(単独・未確定) | 1,810※(+14%) | 81.6(単独) | 欠損 | 欠損 | 32 | 36.9(単独) | 欠損 | 欠損 | 0.74 | **72.2** | 欠損 | 欠損 | 欠損 | 欠損 | S13・S47 |
| 2025Q4 | 2025-12-31 | 1,910※ | 691 | 1,219(算出) | 2,370※(+18%) | 79.6 | 66.9 | 86.8 | 33 | 37(Zacks: 37.3) | 欠損 | **0.68(二次)** | 0.81(非GAAP。S12) | 70.5(算出 = FY 279.5 − 9M 209.0 ※基準未確定) | 620.2 | 42.8(算出) | 577.4(調整後 589・未確定) | 欠損 | S11・S12・S45 |
| 2026Q1 | 2026-03-31 | 1,850※ | 645 | 1,210※(+11%) | 2,090※(+31%) | 欠損 | 欠損 | 欠損 | 31.4 | 35.8 | 欠損 | 0.72 | 0.82 | 73.2(算出 = 6M 154.0 − Q2 80.8) | **1,080**(一次の見出し) | 70(算出) | 1,010※(過去最高) | 欠損 | S04・S06・S49 |
| 2026Q2 | 2026-06-30 | 2,050※ | 773.0 | 1,270(10-Q。未確定 §2 #2) | 2,370※(+33%) | 80.2(non-GAAP 80.9) | 欠損 | 欠損 | 34 | 38(記録的) | 606.3(単独) | 0.82 | 0.901 | **80.8**(前年同期 69.9。6M 154.0) | 1,040※ | 74(算出) | 966 | 欠損(算出 ≈739) | S01・S02・S03・S07・S08・S09 |

**表2の注記**
- 2026Q2 の 6か月 SBC は 154.0(前年 136.8)。費用科目別の内訳は Q2 2026: 販売・マーケ 36.7、R&D 26.9、G&A 8.5、サービス原価 8.1、製品原価 0.6(S03 要約)。
- 2026Q2 の税効果: SBC 関連の税便益 17.7(前年 15.3)(S03)。
- 2026Q1 の営業CF 1.08bn は SEC 8-K Ex99.1 の見出し「Record operating cash flow of $1.08 billion」から採取(S49)。本文は未読。
- 2024Q2 の営業CF 342 は単一の要約から。
- 2024Q1 の SBC 合計は算出のみ(6か月 127.3 = 9M 193.7 − Q3 66.4)。個別の Q1・Q2 は欠損。

---

## 5. 表3 根幹KPI

KPI の定義変更: 2026年の要約では **Unified SASE・SecOps の ARR の記載が見当たらず、billings の伸び率のみ**。2025Q4 の要約では ARR の記載がある(S45)。2026Q2 は「SASE Firewall」を経営側の括りとして新設し、secure networking と Unified SASE を合算して「2 billion 超、+34%」(S10)。ARR を開示停止したかは**未確認**。

| 四半期 | Unified SASE の ARR(前年比) | SecOps の ARR(前年比) | FortiGate 更新サイクル(会社の数値) | $1M超案件 | 繰延収益(総額) | RPO | 製品売上前年比 | 出典 |
|---|---|---|---|---|---|---|---|---|
| 2024Q1 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | −18.3% | S19 |
| 2024Q2 | 欠損 | 欠損 | 欠損 | 欠損 | 5,900(+15.0%) | 欠損 | −4.4% | S18 |
| 2024Q3 | 欠損(+14%、コール要約。billings か ARR かは不明) | 欠損(+32%、同上) | 欠損 | 欠損 | 欠損 | 6,100(+15%) | +1.7% | S17 |
| 2024Q4 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | +18% | S16 |
| 2025Q1 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | +12% | S15 |
| 2025Q2 | 22%(**未確定**、§2 #4) | 35%(**未確定**、§2 #4) | 「2026年の更新サイクルの 40〜50% を消化」(2025Q2 時点の経営発言。二次) | 件数 +29%、金額 +51% | 欠損 | 6,640(current 3,450。Zacks 系) | 欠損 | S14・S28 |
| 2025Q3 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | +18% | S13 |
| 2025Q4 | **11%(ARR $1.28bn。二次・未確定 §2 #20)** | **21%(ARR $491mn。二次)** | 欠損 | 30%超(下限。CSV は空欄) | 欠損 | 欠損 | +20% | S45・S12・S28 |
| 2026Q1 | 欠損 | 欠損 | 欠損 | 欠損 | 7,350(current 3,726.3) | 欠損 | +41% | S09・S05 |
| 2026Q2 | 欠損(billings +35%) | 欠損(billings +25%) | 欠損 | 欠損 | 7,680(current 3,840) | 7,730(**単独・未確定**。CSV は空欄) | +52% | S03・S09・S10 |

**表3の注記**
- SecOps の billings: 2025Q3 +33%、2025Q4 +6%、2025年度 +22%(S45 系。二次)。
- 2025年度の製品売上は +16%(S11 系)。
- 2026Q2 の CFO 発言として、後半の billings に価格改定で「高い一桁%」の上乗せが入りうる(S07 要約)。
- 2026 年の FortiGate 更新サイクルの進捗値は、検索した範囲では見つからなかった。

---

## 6. 表4 年度業績(2021〜2025)

| 項目 | 2021 | 2022 | 2023 | 2024 | 2025 | 出典 |
|---|---|---|---|---|---|---|
| 総売上 | 欠損 | 欠損 | 5,300※(+20%) | 5,960※(+12%) | 6,800※(+14%) | S44・S16・S11 |
| 製品売上 | 欠損 | 欠損 | 1,927(四半期合計・算出。Q4 2023 は 488.1 等) | 1,909(四半期合計・算出。開示: −1%) | 2,218(四半期合計・算出。開示 +16% と整合) | 算出・S44・S16 |
| サービス売上 | 欠損 | 欠損 | 3,380※(+28%) | 4,050※(+20%) | 4,581(算出 = 総売上 − 製品。丸め ±5) | S44・S16 |
| billings | 欠損 | 欠損 | 6,400※(+14%) | 欠損(開示の伸び率 +2.1% のみ) | 7,550※(+16%) | S44・S16・S11 |
| GAAP営業利益率 | 欠損 | 欠損 | 23.4(GAAP 営業利益 1.24bn) | 欠損 | 31※(二次) | S44・S11 |
| non-GAAP営業利益率 | 欠損 | 欠損 | 28.4(non-GAAP 営業利益 1.51bn) | 35 | 35 | S44・S16・S11 |
| GAAP純利益 | 欠損 | 856.6 | 1,147.8 | 1,745.2 | 1,853.4 | S43・S40(10-K 財務表の要約) |
| GAAP希薄化後EPS | 欠損 | 1.06 | 1.46 | 2.26 | 2.42 | S43・S40 |
| non-GAAP希薄化後EPS | 欠損 | 欠損 | 1.63 | 2.37(二次) | 2.76(二次。Q4 プレゼン原稿の記載。四半期合計 2.77 は丸め差) | S44・S43・S41 |
| SBC | 欠損 | 欠損 | 欠損 | 257.9※(基準未確定) | 279.5※(基準未確定) | S40・S43(二次) |
| 営業CF | 欠損 | 欠損 | 1,935.5 | 2,258.1 | 約2,590.6(算出 = 2024 + 増加 332.5。開示は「約2.59bn」) | S43・S40・S11 |
| capex(本社・DC用不動産を含む) | 欠損 | 欠損 | 約205(算出 = OCF − FCF) | 約378(算出 = 2,258.1 − 1,880) | 約381(算出 = 約2,590.6 − 2,210。丸め ±10) | 算出 |
| FCF | 欠損 | 欠損 | 1,730※ | 1,880※ | 2,210※(定義: 営業CF − 有形固定資産の購入) | S44・S16・S11 |
| FCFマージン | 欠損 | 欠損 | 32.6%(算出) | 31.5%(算出) | 32.5%(算出。開示 33%) | 算出 |
| 期末希薄化後株数 | 欠損 | 欠損 | 欠損(NI÷EPS の算出 ≈786 は加重平均の近似) | 771.9(加重平均・GAAP。期末値は欠損) | 764.6(加重平均・非GAAP計算用。期末値は欠損) | S43・S41 |
| 自社株買い額 | 欠損 | 欠損 | 欠損 | 欠損(2024年10月に $1.0bn 増額、期限 2026-02-28、総枠 $8.25bn。実績額は欠損) | 欠損(2025年8月と2026年1月に各 $1.0bn 増額。2025年4〜5月初旬に 4.6mn株・$401.1mn。年間実績は欠損) | S46(10-Q 要約)・S48 |

**表4の注記**
- 2022 年度の GAAP 純利益・EPS は 10-K 財務表の 3 年目列(S43)。
- 2023 年度の FCF 1.73bn・営業CF 1.94bn は 2024 年 2月 6 日の決算リリース(S44)。
- 2026Q1 の自社株買いは 10.6mn株・$827mn(S06 系)。キャッシュフロー表では $823.0mn(§2 #16)。
- 2025 年度: 「Rule of 45」を 6 年連続で超えたと会社が記載(S11)。

---

## 7. 表5 ガイダンス履歴

### 7-1. 年度ガイダンス

| 年度 | 公表時点 | 売上 | billings | サービス売上 | non-GAAP営業利益率 | non-GAAP EPS | 最終実績 | 出典 |
|---|---|---|---|---|---|---|---|---|
| 2024 | 初期 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | — | 未検索 |
| 2024 | Q2 決算時(日付未確認)で引き上げ | 欠損 | — | — | 引き上げ(数値は欠損) | — | — | S18 |
| 2024 | Q3 決算時(2024-11-07)で引き上げ | 5,856〜5,916 | — | — | — | — | 売上 5,960※、non-GAAP OM 35、FCF 1,880、non-GAAP EPS 2.37(二次) | S17・S43 |
| 2025 | 初期(2025-02-06) | 6,650〜6,850 | 7,200〜7,400 | 欠損 | 欠損 | 2.41〜2.47 | — | S16 |
| 2025 | Q1(2025-05-07)で更新 | 6,650〜6,850 | 7,200〜7,400 | 4,575〜4,725 | 欠損 | 2.43〜2.49 | — | S15 |
| 2025 | Q2 決算時(日付未確認)で更新 | 6,675〜6,825 | 7,325〜7,475 | 4,550〜4,650(二次) | 欠損 | 2.47〜2.53 | — | S14 |
| 2025 | Q3(2025-11-05)で更新 | 6,720〜6,780 | 7,370〜7,470 | 4,575〜4,595 | 欠損 | 2.66〜2.70 | 売上 6,800※、billings 7,550※、non-GAAP EPS **2.76**(二次) | S13・S41 |
| 2026 | 初期(2026-02-05) | 7,500〜7,700 | 8,400〜8,600 | 5,050〜5,150 | 33〜36(二次・単独) | **2.94〜3.00(二次2件一致)** | — | S11・S12・S45・S46 |
| 2026 | Q1(2026-05-06)で更新 | 7,710〜7,870 | 8,800〜9,100 | 欠損 | 欠損 | 3.10〜3.16 | — | S04・S06 |
| 2026 | Q2(2026-07-29)で更新 | 8,020〜8,180 | 9,350〜9,550 | 5,180〜5,220 | 35.0〜37.0(期間が不明確) | 3.41〜3.47 | 未確定(通期は未了) | S01・S08 |

2026 年の売上成長見通しは約 19%(中央値)(S02)。

### 7-2. 四半期ガイダンスと実績

| 四半期 | 公表時点 | 売上 | billings | non-GAAP営業利益率 | non-GAAP EPS | 実績(売上 / billings / non-GAAP EPS) | 出典 |
|---|---|---|---|---|---|---|---|
| 2025Q1 | 2024 Q4 決算時(2025-02-06) | 1,500〜1,560 | 1,520〜1,600 | 欠損 | 0.52〜0.54 | 1,540※ / 1,600※ / 0.58 | S16 |
| 2025Q2 | 2025 Q1 決算時(2025-05-07) | 1,590〜1,650 | 1,685〜1,765 | 欠損 | 0.58〜0.60 | 1,630※ / 1,780※ / 0.64(単独) | S15 |
| 2025Q3 | 2025 Q2 決算時 | 1,670〜1,730 | 欠損 | 欠損 | 0.62〜0.64 | 1,720※ / 1,810※ / 0.74 | S14 |
| 2025Q4 | 2025 Q3 決算時(2025-11-05) | 1,825〜1,885 | 2,185〜2,285 | 欠損 | 0.73〜0.75 | 1,910※ / 2,370※ / 0.81(非GAAP) | S13・S12 |
| 2026Q1 | 2025 Q4 決算時(2026-02-05) | 1,700〜1,760 | 1,770〜1,870 | 30〜32 | 欠損 | 1,850※ / 2,090※ / 0.82(non-GAAP OM 35.8) | S11・S06 |
| 2026Q2 | 2026 Q1 決算時(2026-05-06) | 1,830〜1,930 | 2,090〜2,190 | 欠損 | 0.72〜0.76 | 2,050※ / 2,370※ / 0.901 | S04・S08 |
| 2026Q3 | 2026 Q2 決算時(2026-07-29) | 2,010〜2,100 | 2,250〜2,350 | 35〜37 | 0.83〜0.87 | **未発表**(2026-10-28 予定) | S08 |

- 2026Q3 ガイダンスの前提: 税率 18%、希薄化後株数 741〜745mn株(S08)。
- 中期目標(期限・定義): **欠損**(未検索)。

---

## 8. 表6 コンセンサス

TradingView 直接取得は不可。第2回で WallStreetZen、StockGuide、Yahoo(3月表示)、Chartmill(6月表示)、Trefis(7月) を確認した。**表示日付が要約と食い違うものがあり、日付は表示どおり記載する。**

| 会計年度(12月期) | 売上コンセンサス(平均 / 高 / 低) | non-GAAP EPS コンセンサス(平均 / 高 / 低) | アナリスト数 | 出典 | 出典日付 |
|---|---|---|---|---|---|
| 2026 | **8,300※**(平均)/ 8,700 / 7,900(StockGuide、**単独・未確定**)。参考: 7,810 / 8,030 / 7,770(Yahoo、40人、3月。古い) | **3.51 / 3.68 / 3.34**(WallStreetZen。表示 8-2) 参考: 3.16 / 3.37 / 3.11(Yahoo、41人、3月) | 47(WSZ 表示)/ 41(Yahoo 3月) | S32・S33・S34 | WSZ 表示 8-2(2026年8月頃と推定。要約の「約5日前」と不整合)、StockGuide 9-8〜9-10、Yahoo 3-8〜3-13 |
| 2027 | 参考: 8,640 / 9,020 / 8,350(Yahoo、42人、3月。古い)。WSZ の 9.2bn 表示は整形不良で不採用 | **3.87 / 4.78 / 3.46**(WSZ。表示 8-8)。参考: 3.85(Zacks 系、+11%、単独)、3.43 / 3.93 / 2.99(Yahoo、42人、3月)、3.42(Trefis、7月、人数不明) | 欠損(Yahoo 3月は 42) | S27・S32・S34・S36 | WSZ 表示 8-8 |
| 2028 | **9,730※**(Chartmill、6月、単独)。WSZ の 10.3bn は整形不良で **未確定** | **4.41 / 5.80 / 3.90**(WSZ、表示 8-9)vs **3.93**(Chartmill、6月、単独)。**未確定**(§2 #19) | 欠損 | S32・S35 | WSZ 8-9、Chartmill 6-7 |
| 2029 | 10,840※(Chartmill、6月、単独) | 3.68(Chartmill、単独。2028 より低く、基準不整合の疑い) | 欠損 | S35 | Chartmill 6-8 |
| 2030 | 欠損 | 欠損 | 欠損 | — | — |

**アナリスト目標株価・レーティング**

| 出典 | 日付 | 人数 | レーティング | 平均 | 高 | 低 | 備考 |
|---|---|---|---|---|---|---|---|
| MarketBeat(S37) | 2026-10-01 | 36 | Hold(Buy 10・Strong Buy 2・Hold 19・Sell 5) | 152.79 | 欠損 | 欠損 | 記事の株価 178.76 |
| Stock Observer(S38) | 2026-10-04 | 欠損 | 欠損 | 152.79(MarketBeat と同値) | 欠損 | 欠損 | 二次の転載 |
| WallStreetZen(S32) | 表示日不明(要約「約5日前」) | 23(目標) | 欠損 | 156.83 | 215 | 75 | 株価 184.13 |
| Benzinga(S39) | 日付不明(表示なし) | 23 | Hold(5 Buy・15 Hold・3 Sell) | 140 | 欠損 | 欠損 | 2026-09 初旬の 22人・Buy 表示(S24)と比較して **未確定**(§2 #13) |
| 個別目標(検索要約) | 2026-07 | — | — | Morgan Stanley 183(120 から引き上げ、7-21)、Bernstein 145(Market Perform、102 から)、Wedbush 155(Neutral、新規)、Citi 185(Neutral、7-30)、Susquehanna 160(Neutral、7-31) | — | — | 出典URLは特定できず(MarketBeat 系と推定)。Citi・Susquehanna は S25 |
| StreetInsider(S25) | 2026-07 末 | 欠損 | NEUTRAL | 142.28(12か月) | 欠損 | 欠損 | |
| TradingView(S26) | 日付不明(ラベル「2027」) | 欠損 | 欠損 | 114.74 | 180 | 70 | 不採用候補(§2 #14) |
| 高値・安値の記録(S24) | 2026-08-11 | 31 | Buy | 140 | 215(TD Cowen) | 75(JP Morgan) | 古い |
| StockScan(S50) | 2026-10 表示 | — | — | 154.65〜166.59(モデル予測) | — | — | 集計ではないので不採用 |

- 総合コンセンサス: **Hold が最新2件で一致**。古い Buy 表示は §2 #13 のとおり未確定。
- レーティング分布の最新値: MarketBeat(10 Buy + 2 Strong Buy / 19 Hold / 5 Sell)、Benzinga(5 / 15 / 3)。

---

## 9. 表7 バランスシート(2026-06-30)

| 項目 | 2026-06-30 | 2025-12-31(比較) | 2026-03-31(比較) | 出典 | 備考 |
|---|---|---|---|---|---|
| 現金・現金同等物 | 2,934.9 | 2,495.3 | 欠損 | S02・S09(決算リリース、二次要約) | |
| 短期投資 | 1,134.7(算出 = 1,533.8 − 長期投資 399.1。要約は 1.13bn) | 1,090(要約、1.09bn) | 欠損 | S09・S03 | |
| 長期投資 | 399.1 | 339.7 | 欠損 | S09 | |
| 現金・短期投資・長期投資(合計) | 4,468.7(算出。要約 4.47bn と整合) | 約3,925(算出) | 3,630(Q1 10-Q 要約) | S03・S09 | |
| 投資の公正価値(10-Q 注記) | 1,533.8 | 欠損 | 欠損 | S03 | 短期 + 長期の合計 |
| 社債 残高(元本) | **500.0**(2.2%・2031年3月15日満期。2026-03-15 に 1.0%・500.0 を償還済み) | 1,000.0(元本。未償却 3.7 差し引き。うち流動 499.7 → 長期 約496.6 算出) | 欠損 | S05(Q1 10-Q 要約)・S46 | 2026-06-30 の帳簿価額は欠損(約 496〜497 と推定できるが未確認) |
| オペレーティングリース負債 | 欠損 | 欠損 | 欠損 | — | 未検索 |
| 繰延収益(総額) | 7,680 | 欠損 | 7,350 | S09(二次) | |
| 繰延収益(短期) | 3,840 | 3,636.0(要約。日付を推定) | 3,726.3 | S09・S05 | 2025-12 は未確定(§2 なし。日付推定) |
| 繰延収益(長期) | 3,840(算出 = 総額 − 短期) | 欠損 | 3,624(算出 = 7,350 − 3,726.3) | 算出 | |
| 在庫(純額) | 426.3 | 399.5 | 欠損 | S09・S03 | 評価引当金: 122.8(2026-06)、137.5(2025-12)(S03 注記) |
| 購入コミットメント(製造委託先への発注) | 欠損 | 欠損 | 欠損 | — | 未検索 |
| のれん・無形資産 | 欠損 | 欠損 | 欠損 | — | 未検索 |
| 株主資本 | 欠損 | 欠損 | 欠損 | — | 未検索 |

---

## 10. 出典一覧

すべての出典は検索結果からの URL。**(一次)** = SEC・IR の文書。本文は未読で、要約を使った。**(二次)** = 報道・データサイト等の要約。

| ID | 内容 | URL | 種別 |
|---|---|---|---|
| S01 | 2026Q2 決算 8-K Ex99.1 | https://www.sec.gov/Archives/edgar/data/0001262039/000126203926000018/ftntq2-2026ex991.htm | 一次(本文未読) |
| S02 | 2026Q2 決算リリース転載 / IR 掲載 PDF | https://mfn.se/all/a/fortinet/fortinet-reports-strong-second-quarter-2026-financial-results-c7dd36df ・ https://fortinet.gcs-web.com/static-files/e4ffcc79-194e-4ca3-9a69-8a51bd0a6314 | 一次の転載(二次) |
| S03 | 2026Q2 10-Q(SBC の費用科目別、現金・投資、棚卸資産、繰延収益の要約) | https://www.sec.gov/Archives/edgar/data/0001262039/000126203926000021/ftnt-20260630.htm | 一次(本文未読。要約のみ) |
| S04 | 2026Q1 決算 8-K Ex99.1 | https://www.sec.gov/Archives/edgar/data/0001262039/000126203926000010/ftntq1-2026ex991.htm | 一次(本文未読) |
| S05 | 2026Q1 10-Q(債務表、繰延収益) | https://www.sec.gov/Archives/edgar/data/0001262039/000126203926000013/ftnt-20260331.htm | 一次(要約のみ) |
| S06 | 2026Q1 決算要約・FY26 引き上げ | https://finance.yahoo.com/sectors/technology/articles/fortinet-raises-full-outlook-strong-161700176.html ・ https://marketchameleon.com/articles/b/2026/5/7/fortinet-2026-guidance-revenue-growth-free-cash-flow | 二次 |
| S07 | 2026Q2 決算コール要約(CEO・CFO・COO) | https://bullfincher.io/companies/fortinet/earnings-call/fy2026-q2 ・ https://www.marketbeat.com/instant-alerts/fortinet-q2-earnings-call-highlights-2026-07-29/ | 二次 |
| S08 | 2026Q2 決算ヘッドライン・Q3 ガイダンス | https://www.marketbeat.com/instant-alerts/fortinet-nasdaqftnt-releases-earnings-results-beats-estimates-by-015-eps-2026-07-29/ ・ https://beta.earningswhispers.com/epsdetails/FTNT | 二次 |
| S09 | 2026Q2 10-Q 要約(現金・投資・繰延収益・RPO) | https://quartr.com/events/fortinet-inc-ftnt-q2-2026_3gFVkl44 ・ https://www.panabee.com/news/fortinet-earnings-q2-2026-report | 二次(RPO は Panabee 単独) |
| S10 | 2026Q2 KPI 要約(SASE Firewall、billings) | https://pulse2.com/fortinet-fortisase-billings-more-than-double-as-sase-firewall-business-tops-2-billion/ ・ https://vectorshift.ai/research/companies/fortinet/earnings/2026-q2 | 二次 |
| S11 | 2025Q4 決算リリース(SA・Barchart 転載) | https://seekingalpha.com/pr/20390557 ・ https://www.barchart.com/story/news/57297/fortinet-reports-strong-fourth-quarter-and-full-year-2025-financial-results | 一次の転載 |
| S12 | 2025Q4 要約・FY26 初期ガイダンス | https://www.zacks.com/stock/news/2836970/fortinet-q4-earnings-&-revenues-beat-estimates,-increase-y/y ・ https://cfotech.com.au/story/fortinet-lifts-outlook-as-sase-growth-usd-1bn-buyback ・ https://www.stocktaper.com/earningsCallSummary/FTNT/2025/Q4 | 二次 |
| S13 | 2025Q3 決算リリース / 要約 | https://seekingalpha.com/pr/20295326 ・ https://vectorshift.ai/research/companies/fortinet/earnings/2025-q3-summary | 一次の転載・二次 |
| S14 | 2025Q2 決算リリース / 要約 / KPI | https://www.sec.gov/Archives/edgar/data/0001262039/000126203925000025/ftntq2-2025ex991.htm ・ https://www.nasdaq.com/articles/fortinet-q2-earnings-surpass-estimates-sales-increase-y-y ・ https://fintool.com/app/research/companies/FTNT/earnings/Q2%202025 | 一次(本文未読)・二次 |
| S15 | 2025Q1 要約 | https://securitybrief.co.nz/story/fortinet-first-quarter-revenue-surges-to-usd-1-54-billion ・ https://itwire.com/guest-articles/company-news/fortinet-reports-positive-first-quarter-2025-financial-results | 二次 |
| S16 | 2024Q4 / FY2024 決算リリース | https://www.sec.gov/Archives/edgar/data/1262039/000126203925000007/ftntq4-2024ex991.htm ・ https://www.stocktitan.net/news/FTNT/fortinet-reports-fourth-quarter-and-full-year-2024-financial-0q2n0bbsirdl.html ・ https://last10k.com/sec-filings/ftnt/0001262039-25-000007.htm | 一次(本文未読)・二次 |
| S17 | 2024Q3 決算リリース / コール要約 | https://www.sec.gov/Archives/edgar/data/0001262039/000126203924000040/ftntq3-2024ex991.htm ・ https://www.fool.com/earnings/call-transcripts/2024/11/07/fortinet-ftnt-q3-2024-earnings-call-transcript/ | 一次(本文未読)・二次 |
| S18 | 2024Q2 決算リリース / 要約 | https://www.sec.gov/Archives/edgar/data/1262039/000126203924000032/ftntq2-2024ex991.htm ・ https://itbrief.com.au/story/fortinet-sees-record-margins-higher-service-revenue-in-q2-2024 | 一次(本文未読)・二次 |
| S19 | 2024Q1 決算リリース / 要約 | https://www.sec.gov/Archives/edgar/data/1262039/000126203924000017/ftntq1-2024ex991.htm ・ https://securitybrief.co.uk/story/fortinet-s-q1-2024-results-show-7-increase-in-total-revenue | 一次(本文未読)・二次 |
| S20 | 2026Q3 決算日の告知 / 食い違い先 | https://finviz.com/news/398289/fortinet-to-announce-third-quarter-2026-financial-results ・ https://us.trendlyne.com/us/equity/board-meeting/FTNT/1552814/fortinet-inc-board_meeting/ | 告知の転載(二次)・予定表 |
| S21 | 株価・時価総額・株式数・52週(2026-09-25 時点) | https://www.google.com/finance/quote/FTNT:NASDAQ | 二次 |
| S22 | 株価(2026-09-04 終値) | https://www.investsmart.com.au/security/nasdaq/ftnt/fortinet/share-price ・ https://www.digrin.com/stocks/detail/FTNT/price | 二次 |
| S23 | 「史上最高値 182.09」の記事(URL 未特定・候補) | https://parameter.io/cybersecurity-giant-fortinet-ftnt-sees-billings-jump-2-37b-ahead-of-earnings/ | 二次(未確定) |
| S24 | アナリスト評価(Benzinga 2026-09 初旬・2026-08-11 の sentiment) | https://kr.benzinga.com/quote/FTNT/price-targets ・ https://kr.benzinga.com/quote/FTNT/sentiment | 二次 |
| S25 | アナリスト評価(StreetInsider・Stockalarm・TipRanks・Barchart 系) | https://www.streetinsider.com/rating_history.php?q=FTNT ・ https://pro.stockalarm.io/quote/FTNT/analysts ・ https://www.tipranks.com/stocks/FTNT/forecast ・ https://www.tradingview.com/news/barchart:e404b3b11094b:0-what-are-wall-street-analysts-target-price-for-fortinet-stock/ | 二次 |
| S26 | TradingView 予想ページ(FY2027 ラベル) | https://www.tradingview.com/symbols/NASDAQ-FTNT/forecast/ | 二次(日付不明) |
| S27 | FY2027 EPS コンセンサス(Zacks 系。記事は未特定・候補) | https://www.tradingview.com/news/zacks:bb0a9b652094b:0-fortinet-securing-the-ai-revolution/ | 二次(単独) |
| S28 | 2025Q2 KPI(refresh cycle、$1M 案件)・2025Q4 $1M 案件 | https://fintool.com/app/research/companies/FTNT/earnings/Q2%202025 ・ https://www.marketbeat.com/instant-alerts/fortinet-q4-earnings-call-highlights-2026-02-05/ | 二次 |
| S29 | 2026-10-09 終値 194.75(Zacks 系。記事 URL 未特定) | (要約のみ。URL 未特定) | 二次(単独) |
| S30 | 株価履歴(10-02、10-07 の終値) | https://stockanalysis.com/stocks/ftnt/ | 二次 |
| S31 | 「史上最高値 192.55(日中)」の見出し | https://www.investing.com/news/company-news/fortinet-stock-hits-alltime-high-at-19255-usd-93CH-4941285 | 二次(日付不明) |
| S32 | コンセンサス(WallStreetZen。売上・EPS・目標株価) | https://www.wallstreetzen.com/stocks/us/nasdaq/ftnt/stock-forecast | 二次 |
| S33 | コンセンサス(StockGuide。FY2026 売上) | https://stocksguide.com/en/forecast/Fortinet-Inc-US34959E1091 | 二次 |
| S34 | コンセンサス(Yahoo Finance 分析ページ。3月表示の値を含む) | https://finance.yahoo.com/quote/FTNT/analysis/ | 二次(古い) |
| S35 | コンセンサス(Chartmill。FY2028–2029 の単独値) | https://www.chartmill.com/stock/quote/FTNT/analyst-ratings | 二次(単独) |
| S36 | 予測モデル(Trefis、7月) | https://www.trefis.com/data/companies/FTNT | 二次(参考) |
| S37 | 目標株価平均・評価分布(MarketBeat、2026-10-01) | https://www.marketbeat.com/instant-alerts/consensus-fortinet-inc-nasdaq-ftnt-stock-has-average-target-price-of-15279-according-to-analysts-2026-10-01/ | 二次 |
| S38 | 目標株価平均(Stock Observer、2026-10-04) | https://www.thestockobserver.com/2026/10/04/fortinet-inc-nasdaqftnt-stock-has-consensus-price-target-of-152-79.html | 二次 |
| S39 | 目標株価・評価分布(Benzinga 価格目標ページ) | https://www.benzinga.com/quote/FTNT/price-targets | 二次 |
| S40 | FY2025 10-K(GAAP 純利益・EPS・SBC の要約) | https://www.sec.gov/Archives/edgar/data/1262039/000126203926000007/ftnt-20251231.htm | 一次(本文未読) |
| S41 | Q4 2025 プレゼン原稿(非GAAP EPS 2.76、希薄化株数 764.6) | https://investor.fortinet.com/static-files/6e0774bc-f44b-4f53-be97-c302d6664d71 | 一次(要約で採取) |
| S42 | Q4 2025 決算リリース(IR) | https://investor.fortinet.com/news-releases/news-release-details/fortinet-reports-strong-fourth-quarter-and-full-year-2025 | 一次(本文未読) |
| S43 | FY2024 10-K 財務表(Financial_Report。FY2022〜2024 の NI・EPS・OCF・SBC) | https://www.sec.gov/Archives/edgar/data/1262039/000126203925000011/Financial_Report.xlsx | 一次の財務表(要約で採取) |
| S44 | FY2023 Q4 決算リリース(売上・billings・EPS・CF) | https://investor.fortinet.com/news-releases/news-release-details/fortinet-reports-fourth-quarter-and-full-year-2023-financial/ | 一次(要約で採取) |
| S45 | 2025Q4 要約(ARR・GAAP EPS・SecOps billings) | https://vectorshift.ai/research/companies/fortinet/earnings/2025-q4-summary ・ https://quartr.com/events/fortinet-inc-ftnt-q4-2025_3gF6SAvd | 二次 |
| S46 | 自社株買い・社債(10-Q 要約、2025Q1・2026Q1) | https://www.sec.gov/Archives/edgar/data/1262039/000126203925000017/ftnt-20250331.htm ・ https://www.sec.gov/Archives/edgar/data/0001262039/000126203926000013/ftnt-20260331.htm | 一次(要約で採取) |
| S47 | 2025Q3 10-Q(SBC の 3か月・9か月の費用科目別) | https://www.sec.gov/Archives/edgar/data/1262039/000126203925000039/ftnt-20250930.htm | 一次(要約で採取。列の位置合わせ未確認) |
| S48 | 2026Q1 10-Q のキャッシュフロー表(自社株買い 823.0) | https://www.sec.gov/Archives/edgar/data/0001262039/000126203926000013/ftnt-20260331.htm | 一次(要約で採取) |
| S49 | 2026Q1 決算 8-K Ex99.1(見出し「営業CF 1.08bn」) | https://www.sec.gov/Archives/edgar/data/1262039/000126203926000010/ftntq1-2026ex991.htm | 一次(見出しのみ採取) |
| S50 | 予測モデル(StockScan) | https://stockscan.io/stocks/FTNT/forecast | 二次(集計ではない) |

S-ID の番号は元の表の付番を維持し、第2回で増えた分を S29 以降に追加した。
