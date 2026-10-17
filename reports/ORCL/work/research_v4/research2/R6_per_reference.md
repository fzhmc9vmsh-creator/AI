# R6 PER の相場観(参照クラス) データ収集

- 作成日: 2026-10-12
- 対象時点: 2026年9〜10月の値を優先。取れなければ最新の値と日付を記載。
- 取得方法: WebSearch のみ。WebFetch は利用不可のため、すべての値は検索要約経由で、原文ページは開いていない。
- WebSearch は 24 回 (上限) を使い切った。これ以上の検索は行っていない。
- 既存データ (data/H2_peers.csv, data/H2_market.csv 等) は重複調査を避けて参照し、「既存転記」と明記した。
- CSV 版: `R6_per_reference.csv` (143 行、列 name,metric,value,date,source)
- 本ファイルは事実・数値・出典の整理のみ。投資判断は含まない。

## 0. 凡例

- **Tier**: 1 = 会社開示・決算資料 / 2 = 規制当局・取引所・公的統計・格付会社 / 3 = 報道・証券会社や運用会社のレポート・金融データ提供会社 (FactSet, LSEG 等の引用を含む) / 4 = ブログ・SNS・自動生成の相場ページ・販促ページ・AI 生成サイト・シンジケート記事
- **(算出)**: 式を併記した自前計算。
- **掲載日不明**: 値の時点を確認できないもの。原則として採用せず「参考」と表記した。
- **予想PER**: 12か月先 (NTM) または特定年度の予想 EPS に基づく値。EPS の基準年度は出典ごとに異なるため、食い違いは第7節で扱う。
- 出典番号 [Sxx] は第9節の一覧に対応する。

---

## 1. 要点 (最重要の発見)

1. **S&P 500**: 予想PER は 2026-09-30 時点で約 19 倍 [S01]。FactSet 引用の 2026-01 時点では 22.1 倍、10年平均は 18.8 倍 [S02]。Yardeni は年末 2026 の予想PER を 18.6 倍と置いている [S03]。10年平均は 2024 年掲載の旧値 17.8 倍 [S04] と 2026-01 の 18.8 倍で異なる。
2. **Oracle**: 予想PER は LSEG データで 16.9 倍 (2026-08-31) [S16]。同じ LSEG 基準の過去5年 (2021-08〜2026-08) は中央値 19.2 倍、平均 20.7 倍 [S16]。現在値は中央値比 -12.0% (算出)。**10年平均は欠損**。実績PERの5年平均 (31.5〜34.4) は予想PERと別の指標のため比較不可 [S19][S20]。
3. **日経平均**: 予想PER 18.33 倍 (2026-07-07, 予想EPS 3,723.78 円) [S09]。同じ 7 月の別の算出法では、加重平均 17.93 倍、指数ベース 23.75 倍 [S09]。予想EPS は 2025 年末 2,650.84 円から +40.5% (算出)。**TOPIX** の PER は 17 倍台 [S07]。**東証プライム平均PERは欠損**。
4. **日本企業全体**: 2027年3月期の純利益の増益率は、8月時点 +11.7% (555社集計) [S12]、5月時点 +7.7% (1,046社) [S13]。対象と方法が異なり、EPS の平均成長率ではない。
5. **個別大型株**: 予想PERが出典間で大きく割れる銘柄が多い。ServiceNow は 11.5〜14.8 倍 (算出) から 107.9 倍まで、Alphabet は 21.9 倍と 29 倍、Meta は 16.8 倍と 23 倍、NVIDIA は 23.2 倍と 35 倍の値がある。**3〜5年 EPS 成長率のコンセンサスは全銘柄で欠損**。PEG から逆算した参考値のみ取得できた。
6. **REIT**: Equinix の 2026 年 AFFO/株ガイダンスは 42.69〜43.29 ドル (中央値 42.99 ドル、算出) [S33]。9 月 11 日終値 1,037.72 ドルで P/AFFO は 24.1 倍 (算出) [S34]。Digital Realty の P/AFFO 2026E 26.3 倍はシンジケート記事で、日付不明 [S37]。**DLR の 9 月株価と 2027E の P/AFFO は欠損**。
7. **ネオクラウド**: CoreWeave の EV/売上 2026E は 7.9 倍、2027E は 4.9 倍。EV/EBITDA は 2026E 11.6 倍、2027E 6.9 倍 (いずれも算出)。EV は単一出典 [S40]、売上・EBITDA は日付不明のコンセンサス [S41]。Nebius は 6 月時点の時価総額で算出すると 2026E 約 18〜19 倍、2027E 約 5.6〜5.9 倍 (算出)。**9 月の値は欠損**。

---

## 2. 指数

| 指数 | 指標 | 値 | 時点 | 出典 (Tier) | 備考 |
|---|---|---|---|---|---|
| S&P 500 | 予想PER (12か月先) | 約19倍 | 2026-09-30 | [S01] (Tier3) | FactSet 帰属は記事に明記なし |
| S&P 500 | 予想PER (12か月先) | 22.1倍 | 2026-01 データ | [S02] (Tier3) | FactSet 引用。9 月以前の値のため参考 |
| S&P 500 | 予想PER 10年平均 | 18.8倍 | 2026-01 データ | [S02] (Tier3) | FactSet 引用 |
| S&P 500 | 予想PER 10年平均 (旧版) | 17.8倍 | 2024 掲載 | [S04] (Tier3) | 古いため参考のみ |
| S&P 500 | 年末 2026 の予想PER (Yardeni 前提) | 18.6倍 | 2026-09-16 | [S03] (Tier3) | 前回 19.8 から引き下げ。目標値の前提であり実績ではない |
| S&P 500 | 年末目標 7,900 / 2027 EPS 425 | 18.6倍 (算出) | 2026-09-16 | [S03] (Tier3) | 7900/425 = 18.59。Yardeni 記載値と一致 |
| S&P 500 | 2027 EPS 推計 (Yardeni) | 425 | 2026-09-16 | [S03] (Tier3) | 据え置き |
| S&P 500 | EPS 成長 2026 年上期 (累計 YoY) | +39% | 2026-10-05 | [S01] (Tier3) | 単一出典。定義を要確認 |
| S&P 500 | EPS 成長 2026 年下期 見込み (YoY) | +26% | 2026-10-05 | [S01] (Tier3) | 単一出典。定義を要確認 |
| S&P 500 | 今期・来期・3〜5年の EPS 成長率 | 欠損 | - | - | 2026年EPSの基準値なし |
| Nasdaq-100 | 予想PER (NTM) | 27.44倍 | 2026-01-01 | [S05] (Tier3) | 2026-09 の値は欠損 |
| Nasdaq-100 | 予想PER (NTM) | 28.09倍 | 2025-09-30 | [S05] (Tier3) | 参考 |
| Nasdaq-100 | 予想EPS (NTM) / 2025 年末 trailing EPS | 214.27 / 181.93 | 2026-01-01 | [S05] (Tier3) | 予想EPS は trailing より 17.8% 高い (算出) |
| Nasdaq-100 | 保有銘柄加重の予想PER (QQQM) | 21.5〜22.1倍 | 掲載日不明 | [S06] (Tier3) | 別手法。12か月 to 2027-08-31 基準。参考 |
| Nasdaq-100 | 保有銘柄加重の予想EPS 成長 (QQQM) | 13.0% / 23.7% | 掲載日不明 | [S06] (Tier3) | 2 つの値が混在。定義が不統一 |
| TOPIX | 予想PER (12か月先) | 17倍台 | 2026-07-31 / 08-12 | [S07] (Tier3) | 数値は記事本文の「17倍台」のみ。過去レンジ上方 |
| TOPIX | 12か月先予想EPS (2026 年末想定) | 約240 | 2026-02-20 | [S08] (Tier3) | 想定値。市場実績ではない。2026年末PER 約17倍も想定 |
| TOPIX | 予想EPS 成長率・10年平均PER | 欠損 | - | - | 未取得 |
| 日経平均 | 予想PER (予想EPS 3,723.78円基準) | 18.33倍 | 2026-07-07 | [S09] (Tier3) | 2 次集計。出典 URL 特定不可 |
| 日経平均 | 予想PER 加重平均ベース | 17.93倍 | 2026-07-21 | [S09] (Tier3) | 算出法が異なる |
| 日経平均 | 予想PER 指数ベース | 23.75倍 | 2026-07-21 | [S09] (Tier3) | 同上。加重平均ベースとの差に注意 |
| 日経平均 | 予想PER (2026年度予想EPS基準) | 19.3倍 | 2026-07 | [S10] (Tier3) | 野村アセットマネジメント資料。URL 未確定 |
| 日経平均 | 過去30年の年平均EPS成長率 | 7.7% | 2026-07 | [S10] (Tier3) | 同上 |
| 日経平均 | 予想EPS 2025 年末 / 2026-07-07 | 2,650.84 / 3,723.78 | 2025-12-31 / 2026-07-07 | [S09] (Tier3) | 変化率 +40.5% (算出)。年間成長率予想ではない |
| 日経平均 | 予想EPS (大和総研・参考) | 年初2,190 → 直近2,925 | 2026-06 | [S11] (Tier3) | 2025 年末 2,650.84 とEPS基準が不一致 |
| 日経平均 | 予想PER 10年平均・今期来期 EPS 成長 | 欠損 | - | - | 未取得 |
| 東証プライム | 平均PER (加重/単純, 予想) | 欠損 | - | - | JPX の市場統計に到達できず |
| 東証プライム | 予想EPS 成長率 平均 | 欠損 | - | - | 未取得 |
| 日本上場企業全体 | 2027年3月期 純利益 増益率 (8月時点) | +11.7% (純利益 64兆6,185億円) | 2026-08-06 | [S12] (Tier3) | SMBC日興集計、555社 (集計対象の49.9%)。EPS 平均ではない |
| 日本上場企業全体 | 2027年3月期 純利益 増益率 (5月時点) | +7.7% (純利益 52兆3,419億円) | 2026-05-22 | [S13] (Tier3) | 1,046社。8月時点と対象・方法が異なる |
| 個別参考 (市場平均ではない) | 予想PER: MS-Japan 22.6 / TKC 15.8 / トクヤマ 11.3 | 個別値 | 2026-09-30 / 10-07 / 掲載日不明 | [S14] (Tier3) | 個別銘柄。平均の代わりにはならない |
| MSCI World | 予想PER・10年平均 | 欠損 | - | - | 2026 年の指数値なし。MSCI Inc. 社株の予想PER (25.7〜29.8) は別物のため不採用 |
| MSCI Europe | 予想PER | 12.7倍 (参考) | 2023-12 下旬 | [S15] (Tier3) | 2023 年の値。現在値は欠損 |
| MSCI ACWI | 予想PER | 16.5倍 (参考) | 2023-12 下旬 | [S15] (Tier3) | 同上 |
| 米国 (Yardeni 指数) | 予想PER | 19.8倍 (参考) | 2023-12 下旬 | [S15] (Tier3) | 同上 |

---

## 3. Oracle の過去平均と現在の予想PER

| 指標 | 値 | 時点 | 出典 (Tier) | 備考 |
|---|---|---|---|---|
| 予想PER 現在 (LSEG) | 16.9倍 | 2026-08-31 | [S16] (Tier3) | LSEG データ |
| 予想PER 過去5年 中央値 (LSEG) | 19.2倍 | 2021-08〜2026-08 | [S16] (Tier3) | 同上 |
| 予想PER 過去5年 平均 (LSEG) | 20.7倍 | 2021-08〜2026-08 | [S16] (Tier3) | 同上 |
| 現在 対 5年中央値 (算出) | -12.0% | 2026-08-31 | (算出) 16.9/19.2-1 | 同一基準同士 |
| 現在 対 5年平均 (算出) | -18.4% | 2026-08-31 | (算出) 16.9/20.7-1 | 同上 |
| 予想PER 過去10年 平均・中央値 | 欠損 | - | - | 10年の予想PER履歴は未発見 |
| 予想PER (GuruFocus) | 18.7倍 | 2026-08 中旬 | [S17] (Tier3) | 同記事の実績PER 25.8 / 5年中央値 32.3 は実績ベース |
| 予想PER (dividend.watch) | 16.08倍 | 2026-08-04 | [S18] (Tier4) | 参考 |
| 予想PER (Yahoo key-statistics, 既存転記) | 17.64倍 | 2026-08 下旬 | [S21] (Tier3) | 既存 data/H2_market.csv。列対応は推定 |
| 実績PER 5年平均 (参考) | 34.43倍 | 掲載日不明 | [S19] (Tier4) | 実績PER。予想PERではない |
| 実績PER 10年平均 (参考) | 29.63倍 | 掲載日不明 | [S19] (Tier4) | 同上 |
| 実績PER 5年平均 (別出典, 参考) | 31.5倍 | 2026-06-05 頃 | [S20] (Tier4) | 同上 |

- 予想PER の現在値は出典間で 16.1〜18.7 倍に分布する (日付と基準がずれている)。

---

## 4. 個別大型株・ソフトウェア

| 銘柄 | 指標 | 値 | 時点 | 出典 (Tier) | 備考 |
|---|---|---|---|---|---|
| Microsoft (MSFT) | 予想PER FY2027 (6月期) | 25.4倍 (算出) | 2026-09-04 | 499.70 / 19.64 (算出) [S22][S21] (Tier3/4) | 株価 499.70 は既存転記。株価は出典間で不一致 |
| Microsoft | 予想PER FY2028 | 21.6倍 (算出) | 2026-09-04 | 499.70 / 23.18 (算出) [S22] (Tier4) | FY28 EPS 23.18 |
| Microsoft | 予想PER 集計サイト (参考) | 21.2倍 | 2026-08 頃 (URL から推定) | 集計サイト (スペイン語記事、URL 特定不可) (Tier4) | PEG 1.52、1年 EPS 成長 +19.3% |
| Microsoft | 予想PER Yahoo (参考) | 24.94倍 | 掲載日不明 | [S21] (Tier3) | 既存転記 |
| Microsoft | EPS 成長 5年 (PER/PEG 逆算) | 15.6% (算出) | 掲載日不明 | 24.94/1.60 (算出) [S21] | 参考値。コンセンサスではない |
| Microsoft | 3〜5年 EPS 成長 コンセンサス | 欠損 | - | - | 未取得 |
| Alphabet (GOOGL) | 予想PER 今期 | 21.87倍 | 2026-09-04 | [S23] (Tier3) | 既存転記 (GuruFocus)。株価 343.50 (10-02) と日付差あり |
| Alphabet | 予想PER 2026 年 EPS 基準 | 29倍 | 2026-09-30 | 投資記事 URL 特定不可 (Tier3/4) [S30] | GuruFocus 値と基準が不一致 (要確認) |
| Alphabet | EPS 成長 (PER/PEG 逆算) | 10.8% (算出) | 掲載日不明 | 24.08/2.23 (算出) [S24] | Stockopedia 既存転記 |
| Alphabet | EPS 成長 (FullRatio, 参考) | 46.1% | 2026-06-10 | [S25] (Tier4) | 上の 10.8% と不一致 |
| Alphabet | 3〜5年 EPS 成長 コンセンサス | 欠損 | - | - | 未取得 |
| Amazon (AMZN) | 予想PER 2027 年 | 24.3倍 (算出) | 2026-09-24 | 254.46 / 10.47 (算出) [S31] | 2027 EPS 10.47 は出典 URL 特定不可 (既存転記) |
| Amazon | 予想PER 2026 年 (一時益を除く) | 約30倍 | 2026-09-30 | [S30] (Tier3/4) | Anthropic 関連の一時益を除外 |
| Amazon | 3〜5年 EPS 成長 コンセンサス | 欠損 | - | - | 未取得 |
| Meta (META) | 予想PER 今期 (GuruFocus, FRA:FB2A) | 16.84倍 | 2026-08-21 | [S23] (Tier3) | ドイツ上場銘柄の値 (要確認) |
| Meta | 予想PER (Stockopedia) | 22.02倍 | 掲載日不明 | [S24] (Tier3) | EPS 成長 21.51% (同ページ) |
| Meta | 予想PER (2026-04 記事, Bloomberg 引用) | 約23倍 | 2026-04 | [S30] (Tier3) | trailing か forward か不明 |
| Meta | EPS 成長 2026 年 | 21.72% | 掲載日不明 | [S24] (Tier3) | 予想か実績か要確認 |
| Meta | EPS 成長 (PER/PEG 逆算) | 17.8% (算出) | 掲載日不明 | 22.02/1.24 (算出) [S24] | 参考 |
| Meta | 3〜5年 EPS 成長 コンセンサス | 欠損 | - | - | 未取得 |
| NVIDIA (NVDA) | 予想PER | 23.2倍 | 2026-07-11 | [S26] (Tier3) | Motley Fool |
| NVIDIA | 予想PER | 約35倍 | 2026-08-05 | [S27] (Tier4) | 前年同時点 57.58。Q2 決算 (8/26) 前の値 |
| NVIDIA | 予想PER (掲載日不明の候補) | 45〜58倍 | 掲載日不明 | 採用せず | 日付不明のため不採用 |
| NVIDIA | FY2027 EPS 平均 (MarketBeat 表) | 6.52 | 掲載日不明 | [S22] (Tier4) | 表の Q1 平均 1.51 は古い。実績 1.87 と不整合 |
| NVIDIA | EPS 8.69→11.67 の成長 (算出) | 34.3% | 掲載日不明 | 11.67/8.69-1 (算出) [S22] | 年度不明。上の 6.52 とは基準が異なる |
| NVIDIA | 3〜5年 EPS 成長 コンセンサス | 欠損 | - | - | 未取得 |
| SAP | 予想PER 今期 (Yahoo, 既存転記) | 21.10倍 | 掲載日不明 (株価 216.43 は 2026-08-19) | [S21][S23] (Tier3) | 株価は GuruFocus |
| SAP | EPS 成長 5年 (PER/PEG 逆算) | 13.6% (算出) | 掲載日不明 | 21.10/1.55 (算出) [S21] | 5年 expected PEG 1.55 |
| SAP | 3〜5年 EPS 成長 コンセンサス | 欠損 | - | - | 未取得 |
| Salesforce (CRM) | 予想PER (TIKR, 候補) | 13.9倍 | 掲載日不明 | [S28] (Tier4) | 日付不明のため採用見送り |
| Salesforce | 予想PER (valueinvesting.io, 候補) | 24.88倍 | 掲載日不明 | [S29] (Tier4) | 同上。同サイトの他の値も日付不明 |
| Salesforce | 3〜5年 EPS 成長 コンセンサス | 欠損 | - | - | 未取得 |
| ServiceNow (NOW) | 予想PER (株価 132.53 / EPS 8.93) | 14.8倍 (算出) | 株価 2026-09-12 / EPS 年度不明 | [S32] + [S22] (Tier3/4) | 株価 investsmart 単一出典 |
| ServiceNow | 予想PER (株価 132.53 / EPS 11.49) | 11.5倍 (算出) | 同上 | [S32] + [S22] | 同上 |
| ServiceNow | 予想PER (TIKR, 候補) | 21.05倍 | 掲載日不明 | [S28] (Tier4) | 5年平均 59.51 |
| ServiceNow | 予想PER (GuruFocus, 候補) | 53.63倍 | 掲載日不明 | [S23] (Tier3) | 「for today」表記のみ |
| ServiceNow | 予想PER (valueinvesting.io, 候補) | 61.86倍 | 掲載日不明 | [S29] (Tier4) | - |
| ServiceNow | 予想PER (MarketBeat, 2025 年末基準の古い版) | 107.86倍 | 2025-12-31 基準 | [S22] (Tier4) | 古い版のため不採用 |
| ServiceNow | 次期 EPS 成長 (MarketBeat) | 28.67% | 掲載日不明 | [S22] (Tier4) | EPS 8.93→11.49 (算出 11.49/8.93-1 = 28.7%) |
| ServiceNow | 3〜5年 EPS 成長 コンセンサス | 欠損 | - | - | 未取得 |
| Adobe (ADBE) | 予想PER (2025-12 スナップショット) | 16.8倍 | 2025-12 (株価約 344) | 集計ページ URL 特定不可 (Tier4) | 古い。予想EPS 20.55 (35名) |
| Adobe | 予想PER (2025-09 決算後) | 20.02倍 | 2025-09 | 同上 (Tier4) | 古い |
| Adobe | 2026-09/10 の予想PER・3〜5年 EPS 成長 | 欠損 | - | - | 未取得 |
| IBM | 予想PER 2026-09 | 欠損 | - | - | 既存の株価 233.87 (2026-09-01) はあるが、日付付きの予想EPS がない。Zacks 20.1〜24.8 は日付不明で採用せず |
| IBM | PEG (GuruFocus, 5年 EBITDA 基準, 参考) | 2.42 | 2026-08-22 | [S23] (Tier3) | 基準は EPS ではなく 5年 EBITDA 成長 8.10% |
| IBM | 3〜5年 EPS 成長 コンセンサス | 欠損 | - | - | 未取得 |

---

## 5. REIT (Equinix, Digital Realty)

| 銘柄 | 指標 | 値 | 時点 | 出典 (Tier) | 備考 |
|---|---|---|---|---|---|
| Equinix (EQIX) | AFFO/株 2026 年 ガイダンス | 42.69〜43.29 USD | 2026-07-29 | [S33] (Tier1) | 第2四半期決算。検索要約経由 (原文未確認)。2 回目の上方修正 |
| Equinix | AFFO/株 ガイダンス 中央値 | 42.99 USD (算出) | 2026-07-29 | (算出) (42.69+43.29)/2 | - |
| Equinix | AFFO/株 成長率 2026 年 (正常化・恒常為替) | 10〜12% | 2026-07-29 | [S33] (Tier1) | Quartr 要約は 11〜13% (Tier4) と不一致 |
| Equinix | AFFO/株 成長率 2026〜2029 年平均 | 9〜12% | 2026-07-29 | [S33] (Tier1) | 企業の長期見通し |
| Equinix | 株価 (2026-09-11 終値) | 1,037.72 USD | 2026-09-11 | [S34] (Tier3) | Yahoo Finance 検索要約 |
| Equinix | P/AFFO 2026E | 24.1倍 (算出) | 2026-09-11 | 1,037.72/42.99 (算出) | 範囲 (下限/上限) では 24.3 / 24.0 |
| Equinix | P/AFFO 2026E (株価 9/28 近似) | 23.5倍 (算出) | 2026-09-28 (近似) | 1,011.07/42.99 (算出) [S35] | Trade Ideas 掲載の近似値 |
| Equinix | 株価 9/2 (近似) | 1,019.00 USD | 2026-09-02 | [S35] (Tier4) | P/AFFO 23.7 (算出) |
| Equinix | P/AFFO 参考 (2026-04 記事) | 28.7倍 | 2026-04-22 | [S36] (Tier4) | trailing か forward か不明。同一文が多数ドメインに重複 |
| Equinix | P/AFFO 2027E | 欠損 | - | - | 2027 AFFO コンセンサス未取得 |
| Digital Realty (DLR) | P/AFFO 2026E (予想) | 26.3倍 | 掲載日不明 (2026 年春と推定) | [S37] (Tier4) | 5年平均 22.3 倍の 18% 上 (算出 26.3/22.3-1 = +17.9%)。複数ドメインの同一文 |
| Digital Realty | P/FFO (Core FFO 2026E) | 17.8倍 | 2026-05 (株価 150.42 は 2026-04-30) | [S38] (Tier4) | FFO 基準。P/AFFO ではない |
| Digital Realty | AFFO/株 2026年上期 (6か月, diluted non-GAAP) | 4.39 USD | 2026-06-30 | 出典 URL 特定不可 (Tier 不明) | 年換算 8.78 (算出) |
| Digital Realty | AFFO/株 2026E・2027E (独自モデル) | 10.02 / 10.81 | 掲載日不明 | [S39] (Tier4) | 信頼度 65/100。上期実績の年換算と乖離するため不採用を推奨 |
| Digital Realty | P/AFFO 2027E (モデル値, 参考) | 16.2倍 (算出) | 掲載日不明 | 174.90/10.81 (算出) [S39] | 株価 174.90 は同ページの日付不明な値 |
| Digital Realty | P/AFFO 上期年換算 (参考) | 19.9倍 (算出) | 掲載日不明 | 174.90/(4.39×2) (算出) | 単純年換算 |
| Digital Realty | 株価 2026-09 | 欠損 | - | - | 9 月の値は未取得 |

---

## 6. ネオクラウド (CoreWeave, Nebius)

| 銘柄 | 指標 | 値 | 時点 | 出典 (Tier) | 備考 |
|---|---|---|---|---|---|
| CoreWeave (CRWV) | 株価 (終値) | 80.92 USD | 2026-09-15 | [S40] (Tier4) | AI 補助作成と明記のサイト。既存 H2_peers に 9/8 99.83, 9/16 83.35, 9/17 79.88, 9/23 86.90 |
| CoreWeave | EV | 95.2 十億 USD | 2026-09-15 | [S40] (Tier4) | 負債・株数の内訳は未確認。単一出典 |
| CoreWeave | EV/売上 2026E | 7.9倍 (算出) | 2026-09-15 EV 基準 | 95.2/12.045 (算出) [S41] (Tier3) | 別ページの売上 12.46 では 7.6 倍。売上の日付不明 |
| CoreWeave | EV/売上 2027E | 4.9倍 (算出) | 同上 | 95.2/19.523 (算出) [S41] | 別ページの売上 23.17 では 4.1 倍。SA (2026-04) は 2027 年売上 30 億ドル超の見方 |
| CoreWeave | EV/EBITDA 2026E | 11.6倍 (算出) | 同上 | 95.2/8.204 (算出) [S41] | 日付不明の EBITDA |
| CoreWeave | EV/EBITDA 2027E | 6.9倍 (算出) | 同上 | 95.2/13.711 (算出) [S41] | 同上 |
| CoreWeave | EV/売上 トレーリング | 12.54倍 | 2026-09-15 | [S40] (Tier4) | 実績ベース |
| CoreWeave | EV/EBITDA トレーリング | 24.14倍 | 2026-09-15 | [S40] (Tier4) | 実績ベース |
| CoreWeave | EV/EBITDA トレーリング (24/7 Wall St) | 23.94倍 | 2026-08-03 | [S31] (Tier3) | 同記事の P/S 6.29 倍 (EV/売上ではない) |
| CoreWeave | EV/売上・EV/EBITDA トレーリング (DefiLlama, 参考) | 13.7倍 / 28.3倍 | 掲載日不明 | [S43] (Tier4) | 参考 |
| CoreWeave | 売上 2026E / 2027E (コンセンサス) | 12.045 / 19.523 十億 USD | 掲載日不明 | [S41] (Tier3) | 列対応は推定 |
| CoreWeave | EBITDA 2026E / 2027E (コンセンサス) | 8.204 / 13.711 十億 USD | 掲載日不明 | [S41] (Tier3) | 同上 |
| Nebius (NBIS) | EV/売上 2026E (MarketScreener, 参考) | 7.3倍 | 掲載日不明 | [S42] (Tier3) | EV 25.2 十億。株価 87.69 は他出典より低く古い可能性 |
| Nebius | EV/売上 2027E (MarketScreener, 参考) | 4.76倍 | 掲載日不明 | [S42] (Tier3) | EV 37.1 十億。売上 7.8 十億 (算出) は TIKR の 11 十億と不一致 |
| Nebius | EV/売上 2027E (Seeking Alpha 記事) | 6.2倍 | 掲載日不明 | 記事 URL 特定不可 (Tier4) | EV/ARR 8.5 倍も記載 |
| Nebius | EV/売上 2026E (算出, 6月時価総額基準) | 約18〜19倍 (算出) | 2026-06-28 頃 | (61.5〜64.0+0.4)/3.4 (算出) [S44] | 純負債 0.4 十億は検索ツールの仮定 (要確認) |
| Nebius | EV/売上 2027E (算出, 6月時価総額基準) | 約5.6〜5.9倍 (算出) | 2026-06-28 頃 | (61.5〜64.0+0.4)/11.0 (算出) [S44] | 売上 11.0 は TIKR |
| Nebius | 売上 2026E / 2027E (TIKR) | 3.4 / 11.0 十億 USD | 2026-06-28 | [S44] (Tier4) | 同日の時価総額 61.5 十億 |
| Nebius | EV/EBITDA 2026E・2027E | 欠損 | - | - | 未取得 |
| Nebius | 株価・EV 2026-09 | 欠損 | - | - | 既存の 286.69 / 53.25 十億 は掲載日不明のため不採用 |

---

## 7. 出典間の食い違い

1. **S&P 500 予想PER**: 約19倍 (2026-09-30) [S01] / 22.1倍 (2026-01, FactSet) [S02] / 年末 18.6 倍 (Yardeni 前提) [S03] / 約 20 倍 (日付なし、TradingView 投稿) の 4 種類。日付と定義が異なり、直接比較はできない。
2. **S&P 500 10年平均**: 17.8倍 (2024 掲載) [S04] と 18.8倍 (2026-01 データ) [S02]。計算期間が異なるため、新しい値を採用した。
3. **Nasdaq-100 予想PER**: 27.44倍 (Siblis, 2026-01-01) [S05] と 21.5〜22.1倍 (Trefis, 保有銘柄加重, 掲載日不明) [S06]。算出法が違う可能性がある (原因は未確認)。
4. **日経平均 予想PER**: 2026-07-21 の同日でも 17.93倍 (加重平均) と 23.75倍 (指数ベース) で大きく異なる [S09]。予想 EPS の基準も、2025 年末 2,650.84 (2026-07 の集計) と年初 2,190 (大和総研) で食い違う [S09][S11]。
5. **TOPIX**: 17 倍台 (野村, 2026-07/08) [S07] と 2026 年末想定の 17 倍 [S08]。両者は概ね整合するが、後者は想定値。
6. **Oracle 予想PER (現在)**: 16.08 (2026-08-04) [S18] / 16.9 (2026-08-31, LSEG) [S16] / 17.64 (2026-08 下旬, Yahoo) [S21] / 18.7 (2026-08 中旬, GuruFocus) [S17]。日付と基準が異なる。
7. **Oracle 実績PER と予想PER**: 実績PER の 5年平均 31.5〜34.4 [S19][S20] と、予想PER の 5年中央値 19.2 [S16] は指標が別で、比較に使うと誤読が生じる。
8. **ServiceNow 予想PER**: 算出値 11.5〜14.8 倍 (株価 132.53 基準、EPS 年度不明) [S32][S22] / TIKR 21.05 [S28] / GuruFocus 53.63 [S23] / valueinvesting.io 61.86 [S29] / MarketBeat 107.86 (古い版) [S22]。EPS 基準と日付が揃っていない。既存の Zacks 年次 EPS 13.87 を使うと 9.6 倍 (算出)。
9. **Alphabet 予想PER**: 21.87 倍 (GuruFocus, 2026-09-04) [S23] と 29 倍 (2026 年 EPS 基準, 2026-09-30) [S30]。EPS 基準が違う可能性がある。EPS 成長も 10.8% (Stockopedia 逆算) [S24] と 46.1% (FullRatio) [S25] で不一致。
10. **Meta 予想PER**: 16.84 倍 (GuruFocus, ドイツ上場銘柄) [S23] / 22.02 倍 (Stockopedia) [S24] / 約 23 倍 (2026-04 記事) [S30] / 28.59 倍 (Zacks, 日付不明、採用せず)。
11. **NVIDIA 予想PER**: 23.2 倍 (2026-07-11) [S26] / 約 35 倍 (2026-08-05) [S27] / 45〜58 倍 (日付不明、採用せず)。FY2027 EPS は 6.52 (MarketBeat 表) [S22] と、8.69→11.67 (年度不明) [S22] で基準が異なる。
12. **Microsoft 株価**: 2026-07-30 の 390.54 / 2026-08-14 の 495.40 / 2026-09-04 の 499.70 が既存データにあり、出典間で不一致。予想PER は 24.9 (Yahoo) [S21]、21.2 (集計サイト) [S22]、25.4 (算出) で、基準が異なる。
13. **Equinix P/AFFO**: 28.7 倍 (2026-04 記事, 基準不明) [S36] と 24.1 倍 (2026-09, ガイダンス中央値による算出) [S33][S34]。分母と株価の基準が異なる。
14. **CoreWeave 売上**: 2026E 12.0 / 12.5 十億 USD (別ページ) [S41]、2027E 19.5 / 23.2 十億 USD [S41]、2027E 30 億ドル超 (SA 2026-04 の見方、データなし)。コンセンサス間の差が大きい。
15. **Nebius 2027 売上**: MarketScreener の EV と倍率から逆算すると 7.8 十億 USD [S42]、TIKR のコンセンサスは 11.0 十億 USD [S44]。不一致。
16. **Digital Realty P/AFFO**: 26.3 倍 (シンジケート記事) [S37]、P/FFO 17.8 倍 (2026-05) [S38]、モデル値による 16.2 倍 (2027, 算出) [S39]、上期年換算による 19.9 倍 (算出)。株価も 150.42 (2026-04-30) [S38]、174.90 (モデル) [S39]、約 200 (HSBC 記事, 日付不明) で異なる。
17. **日本企業の増益率**: +7.7% (5月, 1,046社) [S13] と +11.7% (8月, 555社) [S12]。対象社数と方法が違い、時点の差だけではない。
18. **Equinix 2026 AFFO 成長率**: 10〜12% (企業ガイダンス, Tier1) [S33] と 11〜13% (Quartr 要約, Tier4)。正常化・為替の扱いの違いと推定 (未確認)。

---

## 8. 欠損一覧 (試した検索語)

| 欠損項目 | 試した検索 (要約) | 結果 |
|---|---|---|
| S&P 500 の FactSet 10年平均 (2026-10 時点) | 'S&P 500 forward P/E ratio October 2026 FactSet 10-year average earnings growth 2027' / 'S&P 500 forward P/E September 2026 ... Yardeni' | 2026-01 と 2024 の値のみ |
| S&P 500 の今期・来期 EPS 成長 (コンセンサス) | 上と同じ | 未取得 (Yardeni 2027 EPS 425 のみ) |
| Nasdaq-100 の 2026-09 予想PER・10年平均 | 'Nasdaq-100 forward P/E ratio September 2026 valuation earnings growth estimate' / 'Nasdaq-100 QQQ forward P/E ratio 2026 September October ... FY2027 consensus' | 2026-01 と 2025-09 の値のみ |
| TOPIX の予想EPS 成長・10年平均PER | 'TOPIX 予想PER 2026年10月 東証 プライム 平均 PER 予想EPS 成長率' / 'TOPIX 2027年度 予想 増益率 EPS 成長率 2026年9月 ...' | 2025-08 の古い見立てのみ |
| 日経平均の今期・来期 EPS 成長・10年平均PER | '日経平均 予想PER 2026年9月 日経 予想EPS 増益率 今期 来期' | 5〜7月の値のみ |
| 東証プライム平均PER (予想) | '東証 プライム市場 平均 PER 2026年 上場企業 株価収益率 加重平均 単純平均 予想' / '日本企業 平均 PER 2026年 予想 EPS 成長率 ...' | 個別銘柄のみ。JPX 統計は未到達 |
| MSCI World の予想PER・10年平均 | 'MSCI World forward P/E September 2026 MSCI Europe forward price-to-earnings' / 'MSCI World index forward price-earnings ratio 2026 Europe STOXX 600 ...' / 'MSCI ワールド 予想PER 2026年 欧州 ...' | MSCI Inc. 社株の値と 2023 年の Yardeni 値のみ |
| Oracle の 10年平均 予想PER | 'Oracle ORCL forward P/E 5-year average 10-year average historical forward price to earnings 2026' / 'Oracle ORCL forward P/E historical median 5 year 10 year gurufocus 2026' | 5年 (LSEG) のみ。10年の予想PER 未発見 |
| Oracle の 3〜5年 EPS 成長 (コンセンサス) | (未検索。枠の制約により省略) | 欠損。既存 data/H2_consensus.csv の参照を推奨 |
| NVIDIA の 3〜5年 EPS 成長 | 'NVIDIA NVDA forward P/E September 2026 FY2028 EPS consensus long-term EPS growth 3-5 year' | 未取得 |
| Microsoft / Alphabet / Amazon / Meta の 3〜5年 EPS 成長 | 'Microsoft Alphabet Amazon Meta long-term EPS growth rate consensus 3-5 year analysts 2026 forward P/E comparison' | 未取得 (1年値・PEG 逆算のみ) |
| Salesforce の 2026-09 予想PER・EPS 成長 | 'Salesforce CRM forward P/E ratio ServiceNow NOW forward P/E September 2026 consensus EPS growth' | 日付のない候補値のみ |
| ServiceNow の 2026-09 予想PER (日付付き) | 同上 | 日付付き値なし |
| Adobe の 2026-09 予想PER・EPS 成長 | 'Adobe ADBE forward P/E 2026 consensus EPS growth long-term September 2026' | 2025 年の値のみ |
| SAP の 3〜5年 EPS 成長 | (個別検索は未実施。枠の制約) | 欠損 (PEG 逆算のみ) |
| IBM の 2026-09 予想PER | (個別検索は未実施。既存データの範囲) | 欠損 |
| Equinix の P/AFFO 2027E | 'Equinix P/AFFO 2026 price to AFFO multiple estimate' / 'Equinix 2026 AFFO per share guidance raised ...' | 2027 は未取得 |
| Digital Realty の 2026-09 株価・2027E P/AFFO | 'Digital Realty DLR P/AFFO 2026 price to AFFO multiple 2027 estimate' / 'Equinix EQIX Digital Realty DLR stock price close September 2026 ...' | DLR の 9 月株価は未取得 |
| CoreWeave の 2026-09 EV/EBITDA (予想・日付付き) | 'CoreWeave CRWV EV/sales EV/EBITDA 2026 2027 multiple September 2026' | 日付付きの予想倍率は未取得 (算出のみ) |
| Nebius の 2026-09 EV/売上・EV/EBITDA | 'Nebius NBIS EV/sales forward 2026 2027 valuation multiple enterprise value revenue estimate' | 6 月時点の算出のみ |

---

## 9. 出典一覧

| ID | 媒体・資料 | URL | 掲載日・データ日 | Tier |
|---|---|---|---|---|
| S01 | FT Portfolios 'Market Minute - October 2026' | https://www.ftportfolios.com/Commentary/Insights/2026/10/5/market-minute---october-2026 | 2026-10-05 | 3 |
| S02 | Yahoo Finance 'stock market crash 2026 fed' (FactSet 引用) | https://finance.yahoo.com/news/stock-market-crash-2026-fed-090000556.html | 掲載日不明 (データ 2026-01) | 3 |
| S03 | Advisor Perspectives (Yardeni Research 引用) | https://www.advisorperspectives.com/articles/2026/09/16/stocks-bull-yardeni-cuts-s-p-500-7-900-downturn-risks | 2026-09-16 | 3 |
| S04 | Motley Fool (FactSet 引用) | URL 特定不可 (検索要約) | 2024 | 3 (参考) |
| S05 | Siblis Research 'nasdaq 100 pe ratio' | https://siblisresearch.com/data/nasdaq-100-pe-ratio/ | データ 2026-01-01 | 3 |
| S06 | Trefis 'Invesco NASDAQ 100 ETF (QQQM)' | https://www.trefis.com/data/etfs/qqqm | 掲載日不明 | 3 |
| S07 | 野村証券 市場戦略・解説 | URL 特定不可 (候補 https://www.nomura.co.jp/wealthstyle/article/0833/) | 2026-07-31 / 2026-08-12 | 3 |
| S08 | 三井住友DS アセットマネジメント 市況レポート | https://www.smd-am.co.jp/market/ichikawa/2026/02/irepo260220/ | 2026-02-20 | 3 |
| S09 | 日経平均 予想PER・EPS の 2 次集計 | URL 特定不可 (候補 https://media.moneyforward.com/articles/10408 ; https://www.radionikkei.jp/marketreview/docs/guest_260708.pdf) | 2026-07-07 / 07-21 | 3 |
| S10 | 野村アセットマネジメント 2026年7月資料 | URL 未確定 (候補 https://www.nomura-am.co.jp/news/20260717VJXQDV0U.pdf) | 2026-07 | 3 |
| S11 | 大和総研 マクロ資料 | URL 特定不可 | 2026-06 | 3 |
| S12 | SMBC日興証券 集計 (OANDA Japan 記事) | https://www.oanda.jp/lab-education/market_news/kn_2026080601002281/ | 2026-08-06 | 3 |
| S13 | さきがけ「上場企業、7年連続最高益へ」 | https://www.sakigake.jp/news/article/20260522CO0113/ | 2026-05-22 | 3 |
| S14 | マネックス証券 銘柄スカウター | https://scouter.monex.co.jp/report/theoryDps/6539 (他 9746, 4043) | 2026-09-30 / 10-07 | 3 |
| S15 | Yardeni Research チャート | 候補 https://archive.yardeni.com/pub/mscipe.pdf | 2023-12 下旬 | 3 (参考) |
| S16 | Capital.com (LSEG データ) 'Oracle ORCL stock forecast' | https://capital.com/en-eu/analysis/oracle-orcl-stock-forecast | 2026-08-31 | 3 |
| S17 | GuruFocus 'Oracle Corp shares fall 3.6%' | https://www.gurufocus.com/news/9035678/oracle-corp-orcl-shares-fall-36-what-gf-score-of-90-tells-investors | 2026-08 中旬 (推定) | 3 |
| S18 | dividend.watch ORCL | https://dividend.watch/symbol/ORCL-NYSE | 2026-08-04 | 4 |
| S19 | Wisesheets ORCL P/E | https://www.wisesheets.io/pe-ratio/ORCL | 掲載日不明 | 4 |
| S20 | Tickerleague ORCL P/E | https://tickerleague.com/companies/ORCL/financials/pe-ratio | 2026-06-05 頃 | 4 |
| S21 | Yahoo Finance key-statistics (ORCL / MSFT / SAP, 既存転記) | https://finance.yahoo.com/quote/ORCL/key-statistics/ ; https://finance.yahoo.com/quote/msft/key-statistics ; https://finance.yahoo.com/quote/sap/key-statistics | 掲載日不明 | 3 |
| S22 | MarketBeat (MSFT / NVDA / NOW 系, 既存転記) | https://www.marketbeat.com/instant-alerts/fy2027-earnings-estimate-for-microsoft-issued-by-scotiabank-2026-07-30/ ; https://www.marketbeat.com/stocks/nasdaq/nvda/earnings/ ; https://www.marketbeat.com/stocks/NYSE/NOW | 2026-07-30 / 09-04 ほか | 4 |
| S23 | GuruFocus forward P/E (GOOGL / META / NOW / SAP / IBM, 既存転記) | https://www.gurufocus.com/term/forward-pe-ratio/MIC:GOOGL ; https://www.gurufocus.com/term/forward-pe-ratio/FRA:FB2A ; https://m.gurufocus.com/term/forwardPE/NOW ; https://www.gurufocus.com/term/pe-ratio/SAP ; https://www.gurufocus.com/term/peg-ratio/IBM | 2026-08〜09 (各行に記載) | 3 |
| S24 | Stockopedia (META / MSFT / GOOGL, 既存転記) | https://www.stockopedia.com/permalink/stock-report/26733 ほか | 掲載日不明 | 3 |
| S25 | FullRatio GOOGL PEG (既存転記) | https://fullratio.com/stocks/nasdaq-googl/peg-ratio | 2026-06-10 | 4 |
| S26 | Motley Fool 'NVIDIA's forward P/E has actually fallen' | https://www.fool.com/investing/2026/07/11/nvidias-forward-pe-has-actually-fallen-as-its-stoc/ | 2026-07-11 | 3 |
| S27 | 集計サイト NVDA 予想PER (候補) | https://ycharts.com/companies/NVDA/forward_pe_ratio_1y (候補) | 2026-08-05 | 4 |
| S28 | TIKR ブログ 'Salesforce vs. ServiceNow' (ドイツ語) | https://www.tikr.com/de/blog/salesforce-vs-servicenow-which-enterprise-software-stock-wins-over-the-next-5-years | 掲載日不明 | 4 |
| S29 | valueinvesting.io (CRM / NOW forward P/E) | https://valueinvesting.io/CRM/metric/forward-pe ; https://valueinvesting.io/NOW/metric/forward-pe | 掲載日不明 | 4 |
| S30 | 投資記事 (GOOGL 29 倍 / AMZN 約 30 倍 / META 約 23 倍) | URL 特定不可 (検索要約) | 2026-09-30 / 2026-04 | 3〜4 |
| S31 | 24/7 Wall St (AMZN 株価, CRWV 倍率) | https://247wallst.com/investing/2026/09/24/amazon-stock-could-have-another-big-run-ahead-heres-my-2027-price-prediction/ ; https://247wallst.com/investing/2026/08/03/price-prediction-coreweave-will-trade-at-this-price-in-2027/ | 2026-09-24 / 2026-08-03 | 3 |
| S32 | investsmart ServiceNow 株価 (既存転記) | https://www.investsmart.com.au/security/nyse/now/servicenow-inc/share-price | 2026-09-12 | 3 |
| S33 | Equinix Q2 2026 決算プレスリリース | https://investor.equinix.com/news-events/press-releases/detail/1114/equinix-reports-second-quarter-results-raises-2026 | 2026-07-29 | 1 |
| S34 | Yahoo Finance EQIX 終値 | 候補 https://finance.yahoo.com/quote/EQIX/holders/ | 2026-09-11 | 3 |
| S35 | Trade Ideas EQIX / money365 (近似値) | https://www.trade-ideas.com/stock-info/EQIX/ ; money365 (URL 候補 https://www.money365.market/news/latest/equinix-inc-eqix-trades-near-1-038-as-analyst-sees-7fb744d2) | 2026-09-24 / 09-28 | 4 |
| S36 | Equinix 割高性の記事 (P/AFFO 28.7, 同一文の重複) | URL 特定不可 (検索要約) | 2026-04-22 | 4 |
| S37 | Digital Realty P/AFFO 26.3 の記事 (同一文の重複) | URL 特定不可 (検索要約) | 掲載日不明 | 4 |
| S38 | Digital Realty 2026-05 ノート (P/FFO 17.8) | URL 特定不可 (検索要約) | 2026-05 | 4 |
| S39 | vcpscanner DLR 推定モデル | https://www.vcpscanner.com/valuation/dlr/estimates | 掲載日不明 | 4 |
| S40 | npinvestor.dk CoreWeave (AI 補助作成と明記) | https://npinvestor.dk/aktier/coreweave/ | 2026-09-15 | 4 |
| S41 | MarketScreener CoreWeave valuation | https://www.marketscreener.com/quote/stock/COREWEAVE-INC-185380761/valuation/ (別: https://ae.marketscreener.com/quote/stock/COREWEAVE-INC-185380761/) | 掲載日不明 | 3 |
| S42 | MarketScreener Nebius valuation | https://in.marketscreener.com/quote/stock/NEBIUS-GROUP-8037501/valuation/ | 掲載日不明 | 3 |
| S43 | DefiLlama CoreWeave dashboard | https://defillama.com/pro/crwv-revenue-streams-and-p-e-ennlo2 | 掲載日不明 | 4 |
| S44 | TIKR ブログ 'NBIS has gained 167% in 2026' | https://www.tikr.com/blog/nbis-has-gained-167-in-2026-the-revenue-chart-explains-why | 2026-06-28 | 4 |

- 既存データ (data/H2_peers.csv, data/H2_market.csv) の出典 URL は、上記の該当 ID に含めた。
- 検索要約の REMINDER 行などは本文の出典として扱っていない。

---

## 10. 補足

- 本ファイルの値は WebSearch の要約から取った。原文の表・記事は未確認のため、重要な値 (Equinix ガイダンス、FactSet 系の 10 年平均など) は一次資料での再確認を推奨する。
- Nasdaq-100 の Siblis 表の EPS (214.27 / 181.93) は、同表内の関係から取り出した値である。
- 算出値の検算は `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/r6_work/calc.py` で行った。
