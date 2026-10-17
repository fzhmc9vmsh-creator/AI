# W4: 金利の現状・歴史・見通し(割引率の設定用、事実と出典のみ)

- 作成日: 2026-10-12 / 対象: Oracle(NYSE: ORCL)再評価、論点「AI クラウド事業の将来の利益率と価値」の割引率設定に必要な金利データ
- 投資判断・推奨・割引率の決定は書かない。数値の整理のみ。
- 取得: WebSearch のみ、18 回(上限に到達して打ち切り)。WebFetch は未使用。
- **全項目が検索要約経由**のため、Tier はすべて * 付き(原本未読)。原本の URL は §10 に記載したが、中身は開いていない。
- 表記: 欠損 = 見つからず(試した検索語は §9)。(算出) = 自分で計算(式を併記)。
- Tier: 1 = 会社開示・決算説明会 / 2 = 規制当局・中央銀行・公的統計・格付会社 / 3 = 報道・アナリスト・調査会社 / 4 = ブログ・SNS・販促・個人サイト。
- 既存との関係: Oracle の格付・CDS・満期ラダーは既存 R5 に詳しいため再掲しない。社債利回りは割引率(負債コスト)の入力として §7 に再掲し、既存 R5 §2-2・R7 §2-1 と照合した。

---

## 0. 要約(事実のみ、10 行以内)

1. FF 目標レンジは **3.75〜4.00%**。2026-09-16 FOMC で +25bp(12-0)、2023 年 7 月以来の初の利上げ(Tier 3*)。
2. 2026-09 SEP 中央値: 2026 年末 **4.1%**、2027 年 **4.1%**、2028 年 **3.9%**、2029 年 3.6%、長期 **3.2%**(3.25% 表記も 1 件)(Tier 4*/3*)。6 月 SEP 比で 2027 年 +0.5pt、長期 +0.1pt。
3. 市場織り込み(10-07 時点): 10 月利上げ確率 約 25%、12 月までに 25bp(Tier 4*)。2027 年半ばまでに利上げ 4 回の見方(Morningstar、Tier 3*)は FRB の中央値より高い。2026 年末・2027 年末の先物・OIS 水準は **欠損**。
4. 10 年国債利回り: 9-23 5.11%、9-30 5.29%、10-01 約 5.34%(2002 年以来の高水準)、10-06 5.27%(Tier 3*)。10-12 時点は **欠損**。9-23 時点で 2 年 4.85%、5 年 4.99%、30 年 5.40%(Tier 2*)。9-30 時点の 20 年 5.68%(Tier 3*)。
5. 10 年 TIPS 実質利回り **2.653%**(2026-09-17 入札、2008 年 10 月以来の高水準、Tier 2*)。10 年 BE 約 **2.30%**(算出: 4.95% − 2.653%)。5y5y は概算で約 2.3%(算出、精度不足)。
6. ACM 10 年タームプレミアム: 2026-01 **0.782%**(CEIC、Tier 2*/3*)。2026-04-30 は 0.73%(10 年 4.45% = 期待短期金利 3.72% + TP 0.73%、算出で一致)。2026-09/10 の値は **欠損**。
7. 10 年国債の年代平均(要約の年次値からの算出、未検証): 1960 年代(62〜69) 4.84%、70 年代 7.50%、80 年代 10.60%、90 年代 6.66%、00 年代 4.46%、10 年代 2.40%、20〜24 年 2.73%。1962 年以降の長期平均は一次表が取れず **欠損**(参考算出 約 5.85%、§4)。
8. 見通し: Reuters 債券ストラテジスト調査(10-07、30 人)は 10 年 3 か月後 **5.00%**、6 か月後 4.90%、12 か月後 4.75%(Tier 3*)。Livingston 調査(2026-06)は 2026 年末 4.30%、2027 年末 4.18%(Tier 2*)。CBO(2026-02 基準)は 10 年 2026 年約 4.1% → 2031 年約 4.4%(Tier 3*、年次 2027〜36 は **欠損**)。WSJ 調査・Blue Chip は **欠損**(未検出・未検索)。
9. ERP: Damodaran インプライド ERP(S&P 500)4.23%(2026-08 初、期待リターン 8.97%、Tier 3*)。Kroll 推奨 米国 ERP 5.0%(2026-09 据え置き、Tier 3*)。無リスク金利は Kroll 規則上「正規化 3.5% と 20 年国債スポットの高い方」(2025 年ガイダンス、2026 年の再確認は欠損)。
10. Oracle 社債(2026-09-25 推計、Tier 4*): 2051 年債 利回り 約 7.65%・国債比 **+213bp**、2061 年債 約 7.67%・**+218bp**。2035 年債の現在スプレッドは **欠損**(第三者推計 +205〜210bp、算出・未検証)。

---

## 1. 政策金利と FOMC(四半期表)

| 期間 | 項目 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|---|
| 2026Q1 | 市場の利下げ織り込み | 4 月初め時点で 2026 年の利下げはほぼ織り込まれず。4/29 会合の据え置き確率 99.5%。中東情勢と原油高が背景(要約) | 2026-04 初 | mexc 要約(CME FedWatch 引用) | 4* |
| 2026Q1 | SEP 長期中央値 | 3.1%(前回 3.0%) | 2026-03 | newsquawk 系要約 | 3* |
| 2026Q2 | 政策金利 | 3.50〜3.75%(据え置き。Warsh 議長の初回会合) | 2026-06-17 | Korea Times、KSL 要約 | 3* |
| 2026Q2 | SEP 中央値(6 月) | 2026 年末 3.8%、2027 年 3.6%、2028 年 3.4%、長期 3.1% | 2026-06-17 | newsquawk 表(要約) | 3* |
| 2026Q3 | 政策金利 | **+25bp → 3.75〜4.00%**(12-0)。2023 年 7 月以来の初の利上げ | 2026-09-16 | tmgm、Morningstar、KuCoin 要約 | 3* |
| 2026Q3 | SEP 中央値(9 月) | 2026 年末 **4.1%**、2027 年 **4.1%**、2028 年 **3.9%**、2029 年 3.6%、長期 **3.2%**(3.25% の表記あり、§8 #2) | 2026-09-16 | cryptobriefing、tmgm、KuCoin 要約 | 4*/3* |
| 2026Q3 | SEP の構成 | 18 名が提出(Warsh 議長は提出せず)。中央値は 2026 年に追加 1 回の利上げ、4 名は追加 2 回を適切と判断 | 2026-09-16 | tmgm 要約 | 3* |
| 2026Q3 | SEP の 6 月比(算出) | 2026 年末 +0.3pt(3.8 → 4.1)、2027 年 +0.5pt(3.6 → 4.1)、2028 年 +0.5pt(3.4 → 3.9)、長期 +0.1pt(3.1 → 3.2) | 算出(差分) | 上 2 行より | 算出 |
| 2026Q3 | 現在の中心と SEP 2026 末の差(算出) | 中心 3.875%(= (3.75 + 4.00) ÷ 2)。2026 年末中央値 4.1% との差 約 +22bp ≈ 25bp 利上げ 1 回分 | 算出 | 上 2 行より | 算出 |
| 2026Q3 | 実効 FF 金利 | **欠損** | — | §9 | — |
| 2026Q4 | 市場織り込み(短期) | 10 月利上げ確率 約 25%。12 月までに 25bp を織り込み | 2026-10-07 頃 | political.org、TradingEconomics 要約 | 4* |
| 2026Q4 | 市場織り込み(中期) | 2027 年半ばまでに利上げ 4 回(FRB 中央値を上回る)。(算出) 中心 3.875% + 0.75 = 4.63%(4 回のうち 1 回が 9 月分の場合)、または + 1.00 = 4.88%(9 月分を含まない場合) | 2026-09 下旬以降(日付不明) | Morningstar 要約 | 3* |
| 2026Q4 | 2026 年末・2027 年末の CME 先物・OIS | **欠損** | — | §9 | — |

---

## 2. 国債利回り(日付順)

| 日付 | 2 年 | 5 年 | 10 年 | 20 年 | 30 年 | 10 年 TIPS 実質 | 出典 | Tier |
|---|---|---|---|---|---|---|---|---|
| 2026-04-30 | 欠損 | 欠損 | 4.45% | 欠損 | 欠損 | 欠損 | eco3min(ACM 分解の基準日) | 4* |
| 2026-07-01 頃 | 欠損 | 欠損 | 4.45% | 欠損 | 欠損 | 欠損 | Damodaran 月次(要約) | 3* |
| 2026-07-31 | 欠損 | 欠損 | 4.74%(7 月中に 4.45 → 4.74) | 欠損 | 欠損 | 欠損 | Damodaran 要約 | 3* |
| 2026-08-31 | 欠損 | 欠損 | 4.75% | 欠損 | 欠損 | 欠損 | Reuters 債券調査の要約(roic.ai) | 3* |
| 2026-09-17 | 欠損 | 欠損 | 4.95%(入札終了時) | 欠損 | 欠損 | **2.653%**(入札) | tipswatch(財務省入札結果) | 2*/4* |
| 2026-09-23 | **4.85%** | **4.99%** | **5.11%**(前日比 +15bp) | 欠損 | **5.40%** | 欠損 | statisticsoftheworld(財務省データ) | 2* |
| 2026-09-30 | 欠損 | 欠損 | **5.29%** | **5.68%** | 欠損 | 欠損 | StockMarketWatch 月次 | 3*/4* |
| 2026-10-01 | 欠損 | 欠損 | **約 5.34%**(2002 年以来の高値、その後反落) | 欠損 | 欠損 | 欠損 | Reuters 債券調査の要約 | 3* |
| 2026-10-05 | 欠損 | 欠損 | 5.33%(24 年高値、別報道)/ 5.310%(Tradeweb 経由) | 欠損 | 欠損 | 欠損 | insiderfinance、Dow Jones 要約 | 4*/3* |
| 2026-10-06 | 欠損 | 欠損 | **5.27%**(終値) | 欠損 | 欠損 | 欠損 | Reuters 債券調査の要約 | 3* |
| 2026-10-07 頃 | 欠損 | 欠損 | 5.307% | 欠損 | 5.653%(24 年近い高値、10 月初旬の報道時点) | 欠損 | political.org 要約 | 4* |
| 2026-10-12 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | 本検索では取得できず(§9 #3) | — |

- 10 年の高値は 10 月初旬。報道で 5.31〜5.34% と幅があるため、§8 #1 で併記した。

---

## 3. 実質金利・ブレークイーブン・タームプレミアム・r*

| 期間 | 指標 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|---|
| 2025Q4 | 10Y10Y TIPS(10 年先 10 年の実質金利) | 3% 強 | 2025Q4 | St. Louis Fed(2026-05 ノートの要約) | 2* |
| 2026Q1 | ACM 10 年タームプレミアム | **0.782%**(前月 0.770%) | 2026-01 | CEIC(NY Fed ACM 系列の転載) | 2*/3* |
| 2026Q2 | 10 年 TIPS 入札(5 月) | 実質 2.169%、BE 2.43% | 2026-05-21 | tipswatch(財務省入札結果) | 2*/4* |
| 2026Q2 | ACM 分解(10 年 4.45%) | 期待短期金利 3.72% + TP 0.73%(算出 check: 3.72 + 0.73 = 4.45) | 2026-04-30 | eco3min(ACM 推計) | 4* |
| 2026Q3 | 10 年 BE | 2.24% | 2026-07 中旬 | FRED T10YIE(要約) | 2* |
| 2026Q3 | 5 年実質 / 10 年実質(TIPS) | 約 2.2% / 約 2.4% | 2026-08 初 | Cresset Capital 要約 | 3* |
| 2026Q3 | 5 年 BE / 10 年 BE | 5 年は「約 2.3%」(正確値は欠損)、10 年 2.29%。両者はほぼ一致 | 2026-08 | Trading Economics、Cresset 要約 | 3* |
| 2026Q3 | 10 年 TIPS 入札 | **実質 2.653%**(2008 年 10 月以来の高水準)。BE 2.30%(算出: 4.95% − 2.653% = 2.297%) | 2026-09-17 | tipswatch(財務省入札結果) | 2*/4* |
| 2026Q3 | 5y5y フォワード BE | **欠損**。概算(算出): 2 × BE10 − BE5 ≈ 2 × 2.29% − 2.3% ≈ 2.28%(BE5 が丸め値のため参考) | 2026-08 | — | 算出 |
| 2026Q4 | 10 年 TIPS 実質・BE(10 月) | **欠損** | — | §9 #5, #6 | — |
| 2026Q2 | 実質 r*(HLW 推計) | 1.2%(2026-05、単一出典) | eco3min 要約 | 4* |
| 2026 | 実質 r*(HLW 推計、別出典) | 1.1〜1.5%(時点不明) | cryptobriefing 要約 | 4* |
| 2025Q2 | 実質 r*(HLW 推計) | 0.84% | Morningstar 要約 | 3* |
| 2025Q4 | 実質 r*(HLW 推計、最低の推計) | 1% 未満 | St. Louis Fed(2026-05 ノート要約) | 2* |
| 2021 頃〜2025 | 実質 r*(HLW)の推移 | 2021 年頃 約 1.3% のピーク → 2025 年に約 1% へ低下 | Purdue Daniels 要約 | 4* |
| 2026 | 名目 r*(NY Fed 推計) | 約 3.7%(信頼区間は広い) | cryptobriefing 要約 | 4* |
| 2026 | 整合チェック(算出) | 実質 1.2% + 目標インフレ 2.0% = 3.2%。名目 3.7% との差 0.5pt。差の理由は未確認 | 算出 | — | 算出 |

- FOMC の長期中央値(名目)の推移: 2026-03 3.1% → 2026-06 3.1% → 2026-09 3.2%(§1 参照)。

---

## 4. 歴史(10 年国債利回り、年代別・年次点)

| 期間 | 10 年国債利回り | 算出・直接 | 出典 | Tier |
|---|---|---|---|---|
| 1962(年) | 3.95% | 年次値(要約) | FRED 年次系列(要約) | 2* |
| 1960 年代(1962〜69 の 8 年) | 約 4.84% | 算出(要約の年次値の単純平均。年次表は未読) | macrotrends、FRED 系(要約) | 2*/4* |
| 1970 年代 | 約 7.50% | 算出(同上) | 同上 | 2*/4* |
| 1978(年) | 8.41% | 年次値(要約) | FRED 年次系列(要約) | 2* |
| 1980 年代 | 約 10.60% | 算出(同上) | 同上 | 2*/4* |
| 1990 年代 | 約 6.66% | 算出(同上) | 同上 | 2*/4* |
| 2000 年代 | 約 4.46% | 算出(同上) | 同上 | 2*/4* |
| 2010 年代 | 約 2.40% | 算出(同上) | 同上 | 2*/4* |
| 2020〜2024 年(5 年) | 約 2.73% | 算出(同上。2025〜26 は欠損) | 同上 | 2*/4* |
| 2023(年) | 3.96%(表 A)/ 3.68%(表 B) | 併記(§8 #12) | macrotrends 2 表 | 4* |
| 1962 年以降の長期平均(名目) | **欠損**(一次の年次表を取得できず) | 参考(算出): (8 × 4.84 + 10 × (7.50 + 10.60 + 6.66 + 4.46 + 2.40) + 5 × 2.73) ÷ 63 = 368.57 ÷ 63 ≈ **5.85%**(1962〜2024、年数加重)。入力が未検証のため参考値 | 算出 | 2*/4* |
| 1962 年以降の長期平均(実質、コア CPI 控除) | 約 2.3%(2020 年頃の投稿からの近似) | LPL Research 要約 | 4* |
| 2026 年 YTD 平均(名目) | **欠損** | — | — |
| 1980 年代前半の名目ピーク | **欠損**(未検索) | — | — |
| 10 年 TIPS 入札の実質利回りの歴史水準 | 2026-09-17 の 2.653% は 2008 年 10 月以来の高水準(=2008 年 10 月以降の 10 年 TIPS 入札の実質利回りはこれを上回らず) | tipswatch 要約 | 2*/4* |

- TIPS は 1997 年に発行開始(一般知識。検索では未確認のため出典なし)。それ以前の実質金利は TIPS ベースでは作れない。

---

## 5. 株式リスクプレミアム(ERP)と無リスク金利の扱い

| 項目 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Damodaran インプライド ERP(S&P 500) | **4.23%** | 2026-08 初(月次) | 月次更新の要約(stockwirex、Stocktwits、BVResources 系) | 3* |
| 同 期待リターン | 8.97% | 2026-08 初 | 同上 | 3* |
| 上記の検算(算出) | 8.97% − 4.23% = 4.74% = 10 年国債 7 月末の値(一致)。Damodaran は無リスク金利に 10 年国債を使っている可能性が高い | 算出 | 上 2 行より | 算出 |
| Damodaran ERP(前月) | 4.20%、期待リターン 8.65%、10 年 4.45% | 2026-07 初 | 同上 | 3* |
| 検算(算出) | 8.65% − 4.20% = 4.45% = 10 年国債 7 月初(一致) | 算出 | — | 算出 |
| Damodaran ERP(その他の時点) | 4.24%(2026-05-01、第三者サイト)/ 4.23%(2026-01、年次、trailing cash yield) | 2026-01、2026-05 | 第三者要約 | 3*/4* |
| Damodaran ERP(2026-09 / 10 月) | **欠損** | — | §9 #16 | — |
| Kroll 推奨 米国 ERP | **5.0%**(2025-04 に 5.5% → 2025-09-02 に 5.0% へ。2026-01 に据え置き確認、2026-09-16 に据え置き報道) | 2026-09-16 | BVResources(BVWire)要約、Kroll 2026-01 エグゼクティブサマリー(要約) | 3* |
| Kroll 無リスク金利の扱い | 「正規化 無リスク金利 3.5% と 20 年国債スポットの高い方」(2025-09 ガイダンス) | 2025-09 以降 | 同上 | 3* |
| 20 年国債スポット(Kroll 規則の入力候補) | 5.68% | 2026-09-30 | StockMarketWatch 月次 | 3*/4* |
| Kroll 規則の当てはめ(算出) | max(3.5%, 5.68%) = 5.68%(2026-09-30 時点、規則上の値) | 算出 | 上 2 行より | 算出 |
| Kroll 正規化無リスク金利 3.5% の 2026 年の再確認 | **欠損**(2025 年の資料のみ) | — | §9 #17 | — |
| Kroll 推奨 ユーロ圏 ERP | 5.0〜5.5%(2026-01-30 発効、参考) | 2026-01-30 | BVResources 要約 | 3* |

---

## 6. 見通し(予測の比較)

| 出典 | 時点 | 対象 | 値 | Tier |
|---|---|---|---|---|
| Reuters 債券ストラテジスト調査 | 2026-10-07(30 名) | 10 年 3 か月後 | **5.00%** | 3* |
| 同上 | 同上 | 10 年 6 か月後 | 4.90% | 3* |
| 同上 | 同上 | 10 年 12 か月後 | 4.75% | 3* |
| 同上 | 同上 | 2 年 3 / 6 / 12 か月後 | 4.70% / 4.60% / 4.25% | 3* |
| 同上 | 同上 | 出発点・リスクの向き | 10 年 5.27%(10-06)。30 名中 28 名が上振れリスクと回答 | 3* |
| 同 Reuters 調査(前回、旧) | 2026-09(31 名中 17 名が「3 か月以内に 5% 到達の可能性」) | 10 年 | 3 か月 中央値 4.50%、12 か月 4.34% の旧版あり | 3* |
| Livingston 調査(Philadelphia Fed) | 2026-06 | 10 年 2026 年末 | **4.30%** | 2* |
| 同上 | 同上 | 10 年 2027 年末 | **4.18%** | 2* |
| 同上 | 同上 | 10 年 2026-06 末 | 4.45%(前回 12 月調査 4.04%)。予測か実績かは要約から判別不能 | 2* |
| CBO 基準シナリオ | 2026-02 公表 | 10 年 2026 年 | 約 4.1%(CRFB 要約) | 3*(原典 2) |
| 同上 | 同上 | 10 年 2031 年 | 約 4.4%、以降はほぼ横ばい(CRFB 要約) | 3*(原典 2) |
| 同上 | 同上 | 10 年 2027〜2036 年の年次 | **欠損**(§9 #15) | — |
| Deloitte 要約 | 2026-02 | 次の 10 年平均 | 約 4.3%(2025 年並み) | 3* |
| CRFB 別稿(日付不明) | — | 実績と CBO 見通しの差 | 10 年実績が CBO の従前の見通しを 100bp 超上回る | 3* |
| Morningstar 自社見通し | 2026-09 以降(日付不明) | 2027 年の政策金利 | 利下げ(市場の織り込みと逆向き) | 3* |
| Wells Fargo(Alvarado) | 2026-09 会合前 | 政策金利 | 2026 年に 1 回、2027 年に 1 回の利上げ | 3*(出典 URL 特定不可) |
| WSJ エコノミスト調査 | — | 2026 末・2027 末の 10 年 | **欠損**(検索で未検出、§9 #12) | — |
| Blue Chip | — | 同上 | **欠損**(未検索、§9 #13) | — |
| 大手行ストラテジスト(Reuters 以外) | — | 同上 | **欠損**(未検索、§9 #14) | — |
| CME 先物・OIS による 2026 末・2027 末 | — | 政策金利 | **欠損**(§9 #1) | — |

---

## 7. Oracle 社債の利回り・スプレッド(負債コストの入力)

| 銘柄(クーポン・満期) | 発行時(日付) | 発行時スプレッド | 現在の利回り・スプレッド(時点) | 出典 | Tier |
|---|---|---|---|---|---|
| 3.90% 2035(5 月) | 2015 | +125bp | 欠損(第三者推計 利回り 約 7.18%、2026-09-25) | therighttrader 要約 | 4* |
| 5.20% 2035(9 月) | 2025-09 | **+105bp**(目論見補足書) | 第三者推計 利回り 約 7.21%、国債 5.13% 基準で **算出 +208bp(7.21 − 5.13 ≈ 2.08%)**(2026-09-25) | SEC FWP(発行、1*)、therighttrader(推計、4*) | 1*/4* |
| 5.50% 2035(8 月) | 2025-01 | +97bp | 第三者推計 利回り 約 7.23%、算出 +210bp(2026-09-25)。推計価格は利回りと整合しないとの注記あり | therighttrader 要約 | 4* |
| 4.95% 2031(2 月) | 2026-02-02 | +115bp(利回り 4.988%) | 2026-08 初: 利回り 6.23%、国債比 約 +180bp(既存 R7、算出 +65bp 拡大) | 既存 R7 [R7-36] | 3 |
| 5.35% 2033(5 月) | 2026-02 | +130bp(要約) | **欠損** | therighttrader 要約 | 4* |
| 5.70% 2036 | 2026-02-02 | +145bp(利回り 5.729%) | **欠損** | 既存 R7 [R7-35] | 4 |
| 3.95% 2051 | 発行日は欠損 | 算出 約 +155bp(= 213 − 58、発行後の拡大 58bp の記述から) | 利回り 約 7.65%、国債比 **+213bp**、比較国債 5.52%(2026-09-25) | therighttrader 要約 | 4* |
| 4.10% 2061 | 発行日は欠損 | 算出 +170bp(= 218 − 48、発行後の拡大 48bp の記述から) | 利回り 約 7.67%、国債比 **+218bp**(2026-09-25) | therighttrader 要約 | 4* |
| 5.50% 2064 | 2024-09 | +138bp | **欠損** | 既存 R5 / therighttrader | 4 |
| 6.70% 2056(2 月) | 2026-02-02 | **欠損** | 2026-09 下旬に利回り 8% 超との報道 1 件(**未確認**)。仮に 8.0% と国債 5.5% の差で見ると約 +250bp(算出・条件付き) | ms-aktuell(既存 R5) | 4* |
| 6.85% 2066(2 月) | 2026-02-02 | +195bp(利回り 6.864%) | **欠損** | 既存 R7 [R7-35] | 4 |
| 3.85% 2060 | 2020-03 | +250bp | 欠損 | therighttrader 要約 | 4* |

- 2051 年債と 2061 年債の 9 月下旬の水準は同じ推計ページの値。両銘柄の発行日は要約に無く、発行時スプレッドは算出のみ。
- 2026-09-25 時点の国債比較水準: 約 9 年国債 5.13%(算出の基準として使用)、2051 年債の比較国債 5.52%。

---

## 8. 食い違い(どちらかを採らず併記)

| # | 項目 | 値 A | 値 B | 扱い |
|---|---|---|---|---|
| 1 | 10 年国債の 10 月の高値 | 10-01 約 5.34%(Reuters 要約) | 10-05 5.33%(24 年高値、別報道)、10-05 5.310%(Tradeweb)、10-07 5.307%(political.org) | 併記。ピークの日付と値は媒体で不一致 |
| 2 | SEP 長期中立金利(2026-09) | 3.2%(cryptobriefing、KuCoin) | 3.25%(tmgm の別記述) | 併記。Fed の表は小数 1 桁が通例だが、原表未確認 |
| 3 | SEP 2029 年値(2026-09) | 3.6%(cryptobriefing) | 2029 年の比較値は tmgm に無し | 単一出典のため参考扱い |
| 4 | 9 月利上げの実施 | 3.75〜4.00%、12-0(tmgm、Morningstar、KuCoin) | 実施を確認できないとする記述 1 件(不動産系サイト要約) | 複数の二次情報で一致。一次文書は未読 |
| 5 | 2026 年の利上げ回数 | Morningstar: 2026 年に 2 回(9 月を含む) | tmgm: 9 月後の中央値は「もう 1 回」 | 整合(9 月分を含めれば同じ) |
| 6 | 2027 年の政策金利 | 市場織り込み: 2027 年半ばまでに利上げ 4 回(Morningstar) | FRB 中央値: 2027 年末 4.1%(横ばい)、Morningstar 自身の予想は 2027 年の利下げ | 3 者が異なる。併記 |
| 7 | 10 年 4.45% の時点 | 2026-04-30(eco3min) | 2026-07 初(Damodaran) | 同値の別時点。偶然か再掲かは未確認 |
| 8 | 9 月の 10 年水準 | 9-23 5.11%(財務省データ) | 「4.86% まで上昇」(旧 Reuters 調査の要約) | 時点違い。併記 |
| 9 | 10 年 BE | 9-17 2.30%(算出、入札時) | 8 月 2.29%(TE)、7 月中旬 2.24%(FRED) | 時点違い。併記 |
| 10 | ACM TP 水準 | 0.782%(2026-01、CEIC) | 0.73%(2026-04、eco3min)、「+30〜50bp(2025〜26)」(eco3min 別記事) | モデル・記事で不一致。NY Fed 原表は未読 |
| 11 | ACM の過去最低 | 2020-07 の −1.319%(CEIC) | 2020-03 頃 約 −100bp(eco3min) | 併記 |
| 12 | 2023 年の 10 年平均 | 3.96%(macrotrends 表 A) | 3.68%(macrotrends 表 B) | 併記 |
| 13 | 実質 r*(HLW) | 1.2%(2026-05、eco3min) | 1.1〜1.5%(cryptobriefing)、0.84%(2025-Q2、Morningstar)、1% 未満(2025-Q4、St. Louis Fed) | 時点が異なる。併記 |
| 14 | 名目 r* と実質 + インフレ | 名目 r* 3.7%(NY Fed、cryptobriefing) | 実質 1.2% + 2.0% = 3.2%(算出) | 未整合。0.5pt の差の理由は未確認 |
| 15 | 2026 末の 10 年金利の見通し | Livingston(2026-06): 4.30% | 実勢 5.27%(10-06)、Reuters 3 か月先 5.00% | 予測と実勢の乖離。併記 |
| 16 | CBO の 2026 年の 10 年金利 | CBO 基準 約 4.1%(2026-02) | 実勢 5.1〜5.3%(2026-09〜10)。CRFB は「100bp 超」と記載 | 乖離。CBO の年次表は未確認 |
| 17 | Reuters 調査の旧版と新版 | 2026-09 版: 3 か月中央値 4.50%、12 か月 4.34%(旧) | 2026-10-07 版: 3 か月 5.00%、12 か月 4.75% | 新版を採用、旧版は参考 |
| 18 | Damodaran ERP 4.23% | 2026-08 初(月次) | 2026-01(年次) | 同一値が 2 時点で出ている。取り違えの可能性を排除できず |
| 19 | Oracle 2056 の利回り 8% 超 | ms-aktuell(2026-09 下旬、既存 R5) | therighttrader の 49 銘柄の上限 8.08%(銘柄不明)、2051 年債は 7.65% | 8% 超の銘柄は特定できず。未確認として扱う |
| 20 | Oracle 2035 の現在利回り | 第三者推計 7.18〜7.23%(2026-09-25) | 実勢(TRACE 等)は欠損。推計は価格との整合が取れないとの注記あり | 参考値扱い |
| 21 | Kroll の無リスク金利 | 20 年国債スポット(2025-09 以降の運用) | 正規化 3.5%(2025 年ガイダンス)。2026 年の再確認は欠損 | 規則上は max(3.5%, スポット)。2026 年の正式確認は未了 |
| 22 | Oracle 2031 の利回り(既存 R7 との照合) | 2026-08 初: 6.23%、+180bp(既存 R7) | 今回の検索では確認できず | 既存数値の再掲。検証は未了 |

---

## 9. 欠損と試した検索語(今回の 18 回の範囲)

| # | 欠損項目 | 試した検索語・結果 | 次の手段 |
|---|---|---|---|
| 1 | 2026 末・2027 末の CME 先物・OIS 水準 | "fed funds futures pricing end of 2026 end of 2027 rate cut probability CME FedWatch October 2026"(2026-04 までの古い結果のみ)、"traders price Fed rate hikes 2027 fed funds futures after September 2026 FOMC Warsh terminal rate"(Morningstar の要約のみ) | CME FedWatch を直接参照。2026-12 / 2027-12 限月の価格 |
| 2 | 実効 FF 金利(EFFR) | 検索語に含めず(政策レンジのみ取得) | FRED EFFR |
| 3 | 2026-10-12 時点の 2 年・5 年・20 年・30 年 | "Treasury yields 2-year 5-year 10-year 30-year October 2026"(9-23 の財務省データまで)、"10-year Treasury yield 5.34% highest since 2002 October 2026"(10-07 まで) | 財務省 Daily Par Yield Curve |
| 4 | 2026-09 SEP の公式表(一次) | "Federal Reserve September 16 2026 projections median federal funds rate longer run 3.25 percent 2029 fomcprojtabl"(URL は取得したが本文未読) | federalreserve.gov の fomcprojtabl20260916(未読) |
| 5 | 5 年 BE・5y5y の正確値 | "10-year TIPS real yield breakeven inflation rate 5-year5-year forward October 2026"(9 月の入札まで) | FRED T5YIFR、T5YIE |
| 6 | 10 年 TIPS 実質の 2026-10 値 | 同上 | FRED DFII10 |
| 7 | ACM タームプレミアム 2026-09/10 の値 | "New York Fed ACM term premium 10-year Treasury 2026"(2026-04 が最新) | NY Fed term premia ページ(未読) |
| 8 | 1962 以降の年次表と長期平均(名目) | "10-year Treasury yield long-term average since 1962 percent real 10-year TIPS yield historical average"(一部年のみ) | FRED DGS10 の年次平均 |
| 9 | 年代別平均の一次表 | "10-year Treasury yield annual average by decade 1960s 1970s 1980s 1990s 2000s 2010s 2020s historical"(要約の断片のみ) | FRED 年次系列 |
| 10 | 2026 年 YTD 平均 | 未検索(上限) | FRED |
| 11 | 1980 年代前半の名目ピーク | 未検索(上限) | FRED |
| 12 | WSJ エコノミスト調査 | "Wall Street Journal economists survey 10-year Treasury yield forecast end of 2026 end of 2027"(Bankrate の旧調査のみ) | WSJ 原文(有料) |
| 13 | Blue Chip Economic Indicators | 未検索(上限) | Blue Chip 月次(有料) |
| 14 | 大手行ストラテジストの 10 年見通し(Reuters 以外) | 未検索(上限)。Reuters 調査のみ取得 | 各社リサーチ |
| 15 | CBO 2027〜2036 年次の 10 年金利 | "CBO Budget and Economic Outlook 2026 to 2036 projected 10-year Treasury interest rate by year 2027 2028 2036"(CRFB 要約のみ) | cbo.gov の経済見通し表(未読) |
| 16 | Damodaran の 2026-09・10 月の ERP | "Damodaran implied equity risk premium monthly update 2026 S&P 500"(2026-08 が最新) | NYU Stern の Damodaran ページ(未読) |
| 17 | Kroll の 2026 年の正規化無リスク金利 | "Kroll recommended US equity risk premium normalized risk-free rate 2026"(2025 年の 3.5% のみ) | Kroll Cost of Capital Navigator |
| 18 | Oracle 2035 の現在利回り(TRACE) | "Oracle bonds 2035 notes yield spread over Treasuries 2026"(第三者推計のみ) | TRACE、FINRA |
| 19 | Oracle 2050 年代の 8% 超の銘柄 | "Oracle 30-year bond yield 8% spread over Treasuries record September 2026 investors"(報道なし、bond データサイトのみ) | Bloomberg、Reuters の該当記事、TRACE |
| 20 | Oracle 2026-02 新発債の 2033 年債の発行利回り | 未検索(R5 の欠損を継続) | 424B2 の価格決定部分 |
| 21 | NY Fed r* の一次値(2026) | "New York Fed r-star longer-run neutral rate estimate 2026 Laubach Williams Holston"(一次の表は取れず) | NY Fed r* ページ(未読) |

---

## 10. 出典一覧

すべて検索要約経由。「未読」は URL のみ検索結果に出て、本文を読んでいないもの。

| 媒体・題名 | URL | 掲載日 | Tier | 用途 |
|---|---|---|---|---|
| tmgm「Fed raises 2026 interest rate forecast to 4.1%」 | https://www.tmgm.com/es/analysis/market-news/article/fed-raises-2026-interest-rate-forecast-to-41-lifts-pce-inflation-projections-202609161858 | 2026-09-16 | 3* | SEP、利上げ、構成 |
| KuCoin「September 2026 FOMC」 | https://www.kucoin.com/blog/september-2026-fomc-fed-hikes-25-bp-hawkish-dot-plot-is-this-a-new-hiking-cycle | 2026-09 | 4* | SEP、利上げ |
| cryptobriefing「Fed sees rates holding at 4.1%」 | https://cryptobriefing.com/fed-fomc-september-economic-projections-rate-hike/ | 2026-09 | 4* | SEP 中央値 |
| FOMC 投影表(未読) | https://federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm | 2026-09-16 | 2(未読) | 原典の参照先 |
| Morningstar「Warsh Pounds the Table…」 | https://www.morningstar.com/economy/warsh-pounds-table-inflation-fight-we-see-rate-cuts-2027 | 2026-09 下旬以降 | 3* | 市場織り込み、Morningstar の予想 |
| Korea Times「Fed begins Warsh era…」 | https://www.koreatimes.co.kr/amp/world/20260618/fed-begins-warsh-era-by-keeping-rates-on-hold-sees-one-hike-later-this-year | 2026-06-18 | 3* | 6 月 FOMC |
| KSL「Warsh-led Fed…」 | https://www.ksl.com/article/warsh-led-fed-expected-to-leave-interest-rates-unchanged/51512422 | 2026-06 | 3* | 6 月 FOMC |
| newsquawk「FOMC Summary of Economic Projections」 | https://www.newsquawk.com/headlines/fomc-summary-of-economic-projections-only-18-of-19-members-submitted-forecasts-expectations-were-for-warsh-to-not-submit-forecasts | 2026-06 | 3* | 6 月 SEP 表 |
| statisticsoftheworld(財務省データ) | https://statisticsoftheworld.com/news/2026-09-23 | 2026-09-23 | 2* | 2 年・5 年・10 年・30 年 |
| StockMarketWatch「Treasury Yields & Bond Market · October 2026」 | https://stockmarketwatch.com/bonds/reports/october-2026 | 2026-09-30 | 3* | 10 年 5.29%、20 年 5.68% |
| tipswatch「10-year TIPS reopening…」 | https://tipswatch.com/2026/09/17/10-year-tips-reopening-gets-real-yield-of-2-653-highest-in-nearly-18-years/ | 2026-09-17 | 2*(財務省入札、ブログ経由) | 実質 2.653% |
| tipswatch「10-year TIPS auction…」 | https://tipswatch.com/2026/05/21/10-year-tips-auction-gets-real-yield-of-2-169-to-soft-demand/ | 2026-05-21 | 2*/4* | 実質 2.169%、BE 2.43% |
| political.org「Treasury yields climb to 24-year highs…」 | https://political.org/2026/10/07/treasury-yields-climb-to-24-year-highs-as-markets-brace-for-39-billion-auction-and-fed-minutes/ | 2026-10-07 | 4* | 10 月高値、30 年 5.653%、利上げ確率 |
| TradingEconomics「10-Year Treasury Yield Softens from 24-Year High」 | https://tradingeconomics.com/united-states/government-bond-yield/news/589866 | 2026-10 | 3* | 10 月の水準 |
| insiderfinance「10-Year Treasury Yield Hits 24-Year High」 | https://www.insiderfinance.io/news/10-year-treasury-yield-hits-24-year-high | 2026-10-05 頃 | 4* | 5.33% |
| Reuters 債券調査(roic.ai 転載) | https://www.roic.ai/news/treasury-yields-seen-falling-but-forecasts-rise-sharply-reuters-poll-10-07-2026 | 2026-10-07 | 3* | 10 年・2 年の見通し、出発点 5.27% |
| Reuters 債券調査(Kitco 転載、未読) | https://www.kitco.com/news/off-the-wire/2026-10-07/lower-us-treasury-yield-view-persists-despite-biggest-quarterly-surge | 2026-10-07 | 3*(未読) | 同上 |
| bgov「US Benchmark 10-Year Yield Briefly Hits Highest Since 2002」 | https://news.bgov.com/insurance/treasury-10-year-yield-hits-highest-since-2002-on-rate-outlook | 2026-10 | 3* | 2002 年以来の高値 |
| CEIC「Treasury term premia」(ACM 系列) | https://www.ceicdata.com/en/united-states/treasury-term-premia | 2026-01 | 2*/3* | ACM 0.782% |
| eco3min「ACMTP10 term premium decomposition」 | https://eco3min.fr/en/acmtp10-term-premium-10-year-treasury-yield-decomposition/ | 2026-04 | 4* | ACM 分解 |
| eco3min「ACMTP10 dataset」 | https://eco3min.fr/en/us-term-premium-dataset/ | 2026 | 4* | ACM の範囲 |
| eco3min「Fed Funds and r-star」 | https://eco3min.fr/en/fedfunds-r-star-natural-rate-debate-fed-target/ | 2026-05 | 4* | HLW 1.2%、名目 r* |
| cryptobriefing「Williams neutral rate uncertainty」 | https://cryptobriefing.com/fed-williams-neutral-rate-uncertainty-crypto/ | 2026 | 4* | HLW 1.1〜1.5%、名目 3.7% |
| St. Louis Fed「Comparing the FOMC's Estimate of R-Star…」 | https://www.stlouisfed.org/on-the-economy/2026/may/comparing-fomc-estimate-r-star-alternative-estimates | 2026-05 | 2* | HLW 1% 未満(2025Q4)、10Y10Y TIPS 3% 超 |
| Morningstar「The Neutral Rate…」 | https://www.morningstar.com/economy/neutral-rate-what-it-is-why-it-matters-now | 2026 | 3* | HLW 0.84%(2025Q2) |
| Purdue Daniels「Twinkle twinkle r star」 | https://business.purdue.edu/daniels-insights/posts/2026/twinkle-twinkle-r-star.php | 2026 | 4* | HLW の推移 |
| FRED(10 年国債、年次) | https://fred.stlouisfed.org/data/RIFLGFCY10NA | — | 2*(要約) | 1962・1978 の年次値 |
| macrotrends「10 Year Treasury Rate - 54 Year Historical Chart」 | https://pro.macrotrends.net/2016/10-year-treasury-bond-rate-yield-chart | — | 4* | 年代平均(算出の入力)、2023 の 2 表 |
| multpl「10-year treasury rate by year」 | https://www.multpl.com/10-year-treasury-rate/table/by-year | — | 4* | 年次の候補(要約) |
| LPL Research(signature.esquirebank.com 転載) | https://signature.esquirebank.com/?p=3644 | 2020 頃 | 4* | 実質 2.3%(近似) |
| Philadelphia Fed「Livingston Survey June 2026」 | https://www.philadelphiafed.org/-/media/FRBP/Assets/Surveys-And-Data/livingston-survey/2026/livjun26.pdf | 2026-06 | 2* | 10 年 4.30%(2026 末)、4.18%(2027 末) |
| CRFB「CBO's February 2026 Budget and Economic Outlook」 | https://www.crfb.org/papers/cbos-february-2026-budget-and-economic-outlook | 2026-02 | 3* | CBO 10 年 4.1% → 4.4% |
| CRFB「CBO Finds Rising Rates Could Explode the Debt」 | https://www.crfb.org/blogs/cbo-finds-rising-rates-could-explode-debt | 日付不明 | 3* | 実績は CBO 見通しを 100bp 超上回る |
| Deloitte「Tax News and Views」 | https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/services/tax/us-tax-taxnewsandviews-260213.pdf | 2026-02-13 | 3* | 次の 10 年平均 約 4.3% |
| CBO「Testimony on The Budget and Economic Outlook: 2026 to 2036」(未読) | https://www.cbo.gov/publication/62207 | 2026-02 | 2(未読) | 原典の参照先 |
| stockwirex「What the Equity Risk Premium Says About US Stocks Right Now」 | https://stockwirex.com/education/equity-risk-premium-us-stocks/ | 2026-08 | 4* | Damodaran 4.23%、8.97% |
| Stocktwits(Damodaran 7 月の投稿要約) | https://stocktwits.com/news-articles/markets/equity/s-and-p-500-held-flat-last-month-despite-surging-10-y-treasury-yields-wall-street-s-dean-of-valuation-says-risk-math-hasn-t-changed/cZoT3EWRJ5z | 2026-07 末〜08 | 3* | 10 年 4.45% → 4.74% |
| BVResources(Damodaran 2026 年の更新) | https://bvresources.com/articles/bvwire/damodaran-posts-his-first-data-update-for-2026 | 2026-01 | 3* | ERP 4.23%(年次) |
| BVResources(Kroll 5.0% 据え置き) | https://www.bvresources.com/articles/bvwire/kroll-reaffirms-50-us-erp-sticks-with-treasury-risk-free-rate | 2026-09-16 | 3* | ERP 5.0%、20 年国債の扱い |
| Kroll「Cost of Capital Updates Jan26 Executive Summary」(転載) | https://edge.sitecorecloud.io/krollllc17bf0-kroll6fee-proda464-0e9b/media/Cost-of-Capital/kroll-cost-of-capital-updates-jan26-executive-summary.pdf | 2026-01 | 3* | ERP 5.0% 据え置き(2026-01) |
| therighttrader(Oracle 2035 の銘柄ページ) | https://therighttrader.com/bonds/oracle/3-9-2035 、/5-2-2035 、/5-5-2035 | 2026-09-25 付推計 | 4* | 2035 年債の発行スプレッド・推計利回り |
| therighttrader(Oracle 2051・2061・2064 ページ) | https://therighttrader.com/bonds/oracle/3-95-2051 、/4-1-2061 、/5-5-2064 | 2026-09-25 付推計 | 4* | 2051・2061 の利回りとスプレッド |
| SEC FWP(Oracle 2035 の発行条件) | https://www.sec.gov/Archives/edgar/data/1341439/000119312525215807/d49252dfwp.htm | 2025-09 | 1*(要約経由) | 5.20% 2035 の +105bp |
| ms-aktuell「Oracle-Kreditrisiko auf Rekordhoch」(既存 R5 から) | https://ms-aktuell.de/welt/oracle-kreditrisiko-rekordhoch-27-09-2026/ | 2026-09-27 | 4* | 2056 年債 8% 超の主張(未確認) |
| 既存 R5 / R7(本リポジトリ内) | research2/R5_credit.md、research2/R7_capital_power.md | 2026-10-12 | 既存 | 2031 年債の二次市場、2033・2036・2066 の発行条件 |
| NY Fed term premia ページ(未読) | https://www.newyorkfed.org/research/data_indicators/term-premia-tabs | — | 2(未読) | ACM 最新値の参照先 |
| Damodaran(未読) | NYU Stern の Damodaran ERP ページ | — | 3(未読) | 2026-09・10 の ERP 参照先 |
