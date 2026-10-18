# R1a SoFi Technologies (SOFI) 財務データ収集 — 部分完了版

- 作成日・取得日: **2026-10-18**(本書の全数値の取得日)
- 作成者の位置づけ: 調査担当(分析・結論なし。事実と数値のみ)
- **完了度: 約15〜20%。調査項目1〜8のうち、直近3四半期(Q4'25・Q1'26・Q2'26)の見出し数値と2026年ガイダンスのみ取得。残りは「未取得」。**

---

## 0. 取得手段の制約(必読。数値の信頼度に直結)

| 項目 | 状況 |
|---|---|
| WebFetch | 全ホストで `getaddrinfo ENOTFOUND`(sec.gov, investors.sofi.com, nasdaq.com, rttnews.com, stockanalysis.com 等)。本文取得は不可 |
| curl(Bash) | プロキシが sec.gov / data.sec.gov / investors.sofi.com / s27.q4cdn.com / businesswire.com / stockanalysis.com / macrotrends.net / wikipedia.org に 403(`connect_rejected`)。到達できたのは github.com のみ。回避策は取っていない |
| WebSearch | 約17回実行した時点で「1ターンあたり200回の上限(全エージェント共有)を使い切った」と拒否され、以降の検索は不可。上限を回避する手段(curl検索・外部リーダー等)は使っていない |
| 結果の性質 | WebSearchの出力は**検索ツールが生成した要約文**であり、8-K/10-Kの表そのものではない。表形式の明細(P/L全行・B/S・株数・SBC・借入明細)は要約に出てこなかった |

**含意**: 下表の数値はすべて「SEC/IR資料の内容を引いた、とされる要約文」からの転記であり、原文(8-K Exhibit 99.1の表)での目視確認は**していない**。出所URLは、要約がその数値の根拠として挙げた(または検索結果に出た)資料のURL。各行の「Tier」は資料本体のTier(T1=会社開示)だが、実際の取得経路は要約経由のため、**確度は「T1(要約経由・原文未確認)」と読むこと**。

### 追加取得のための依頼先(ユーザー側アクション)
1. 環境のネットワーク許可に `www.sec.gov`, `data.sec.gov`, `investors.sofi.com`, `s27.q4cdn.com`, `www.businesswire.com` を追加(設定手順: https://code.claude.com/docs/en/cloud-environments#network-access)。これらが開けばWebFetch/curlで8-K Exhibit 99.1の表とXBRL(Financial_Report.xlsx)を直接取れる。
2. もしくは `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` を引き上げる、または続きの調査を新しいメッセージで依頼する。

---

## 1. Q3 2026 決算の発表状況(最初に確認した項目)

| 項目 | 内容 | 出所(資料名+URL) | Tier | 取得日 |
|---|---|---|---|---|
| Q3 2026決算 | **未発表**(2026-10-18時点) | 下記 | T1 | 2026-10-18 |
| 発表予定 | 2026-10-27(火)午前7時(ET)頃にIRサイトで公表、電話会議は同日午前8時(ET) | BusinessWire「SoFi Schedules Conference Call to Discuss Q3 2026 Results」(2026-09-29付) https://secure.businesswire.com/news/home/20260929120531/en/SoFi-Schedules-Conference-Call-to-Discuss-Q3-2026-Results ; 告知PDF: https://s27.q4cdn.com/749715820/files/doc_news/SoFi-Schedules-Conference-Call-to-Discuss-Q3-2026-Results-2026.pdf | T1 | 2026-10-18 |
| 注意 | 検索で出る「Q3 売上$961.60M・EPS$0.11」(RTTNews)は**Q3 2025**の数値でありQ3 2026ではない | https://www.rttnews.com/3586730/sofi-technologies-inc-q3-profit-increases-beats-estimates.aspx | T3 | 2026-10-18 |

→ **最新の確定四半期は Q2 2026(2026-06-30終了、2026-07-29発表)**。

---

## 2. 項目1: 四半期P/L(取得できた範囲)

単位: 百万ドル(特記なき限り)。「GAAP」=SoFiの連結「Total net revenue」、「調整後」=会社定義のAdjusted net revenue(非GAAP)。EPSはGAAP希薄化後、調整後EPSは会社定義(非GAAP)。

### 2-1. 連結ヘッドライン

| 四半期 | GAAP総純収益 | 調整後純収益 | 調整後EBITDA | GAAP純利益 | GAAP希薄化後EPS | 調整後EPS | 出所 |
|---|---|---|---|---|---|---|---|
| Q1 2024 | 約645(丸め) | 未取得 | 未取得 | 約88(丸め) | 未取得 | 未取得 | stockanalysis.com 経由の要約 https://stockanalysis.com/stocks/sofi/financials/ (T3、丸め値) |
| Q2 2024 | 未取得 | 未取得 | 未取得 | 未取得 | 未取得 | 未取得 | — |
| Q3 2024 | 697.12(Q3'25記事中の前年比較値) | 未取得 | 未取得 | 約61(丸め) | 未取得 | 未取得 | RTTNews https://www.rttnews.com/3586730/... (T3); NIはstockanalysis要約(T3) |
| Q4 2024 | 734.1 | 739.1(前年同期594.2、+24%) | 198.0(マージン27%) | 332.5 | 0.29 | 0.05(繰延税金便益を除く。調整後純利益61.0) | Q4'24決算PR https://www.businesswire.com/news/home/20250127863954/en/ ; 8-K https://www.sec.gov/Archives/edgar/data/1818874/000181887425000006/q42024earningsrelease.htm ; 10-K https://www.sec.gov/Archives/edgar/data/1818874/000181887425000016/sofi-20241231.htm (T1・要約経由) |
| Q1 2025 | 771.759 | 770.720 | 210.3 | 未取得(「Q1'26は倍増以上」との記述のみ) | 0.06 | 0.06(調整後希薄化後普通株主帰属純利益 71.455) | Q1'26決算の前年比較値 https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000020/a2026q1earningsrelease.htm (T1・要約経由) |
| Q2 2025 | 854.9 | 858.230 | 249.083 | 97.263 | 0.08 | 0.08(Q2'26が「前年比+50%」で0.12のため逆算=計算、未確認) | Q2'26決算の前年比較値 https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000050/a2026q2earningsrelease.htm (T1・要約経由) |
| Q3 2025 | 961.6(+37.9%) | 未取得 | 未取得 | 未取得 | 0.11 | 未取得 | RTTNews https://www.rttnews.com/3586730/... (T3) |
| Q4 2025 | 「$1.0B」(前年比+40%と記述) / 別報道は「$1.01B」→**食い違い、正確値未取得** | 約1,013(+37%) | 317.6(前年198.0、+60%、マージン31%) | 173.5 | 0.13 | 未取得 | Q4'25決算 8-K https://www.sec.gov/Archives/edgar/data/1818874/000181887426000008/a2025q4earningsrelease.htm ; PR https://www.businesswire.com/news/home/20260130224251/en/ ; Yahoo Scorecard https://finance.yahoo.com/news/scorecard-graded-sofi-technologies-sofi-171053937.html (T1/T3・要約経由) |
| Q1 2026 | 1,100.368(前年771.759、+43%) | 1,087.232(+41%) | 339.9(前年210.3、+62%、マージン31%) | 166.7(「10四半期連続GAAP黒字」) | 0.12(前年0.06) | 0.12(前年0.06)。調整後普通株主帰属純利益(希薄化後)167.075(前年71.455、+134%) | Q1'26 8-K https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000020/a2026q1earningsrelease.htm (T1・要約経由) |
| Q2 2026 | 約1,2xx(「$1.2B、前年854.9から+43%」。要約中に「約1,218.7」との記述があるが**未検証**) | 1,205.550(前年858.230、+40%) | 357.821(前年249.083、+44%) | 156.592(前年97.263、+61%) | 0.12(前年0.08) | 0.12。調整後純利益160.406 | Q2'26 8-K https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000050/a2026q2earningsrelease.htm ; PDF https://investors.sofi.com/files/doc_financials/2026/q2/2026-Q2-Earnings-Release.pdf ; 10-Q https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000054/sofi-20260630.htm (T1・要約経由) |

- 計算: 調整後EBITDAマージン Q2'26 = 357.821 / 1,205.550 = 29.7%(会社は「30%」)。Q1'26 = 339.9 / 1,087.232 = 31.3%(会社は「31%」)。
- Q2'26の調整後EPSには「税率が想定より高かったことによる約0.5セントの押し下げ」があると経営陣が説明(Q2'26決算説明会要約: https://www.fool.com/earnings/call-transcripts/2026/08/07/sofi-sofi-q2-2026-earnings-call-transcript/ , T3)。

### 2-2. 純金利収益(NII)・非金利収益(連結)

| 四半期 | 連結NII | 連結非金利収益 | 備考 |
|---|---|---|---|
| Q1 2026 | 未取得 | 未取得 | Lendingセグメントは「NII前年比+39%(平均貸出残高+40%)」の記述のみ(Q1'26 8-K 要約) |
| Q2 2026 | **未取得(連結)** | **未取得(連結)** | Financial ServicesセグメントのNIIは249.1(+29%)、同セグメント非金利収益217.2(要約)。経営陣はコール内で「キャッシュ収益ベースのNII 7.9億ドル」と述べたとされる(要約。定義不明、連結NIIと照合できず) |
| その他 | 未取得 | 未取得 | — |

- 手順上の注意: Q2'26の10-Q要約に出る「Total net revenue 466.3 / 894.8(3か月/6か月)」は**Financial Servicesセグメント**の純収益(計算: Q1'26 FS 428.5 + Q2'26 FS 466.3 = 894.8 で一致)。連結ではない。

### 2-3. セグメント別(Lending / Technology Platform / Financial Services)

単位: 百万ドル。

| セグメント | 指標 | Q1 2026 | Q2 2026 | 出所 |
|---|---|---|---|---|
| Lending | GAAP純収益 | 642.4(+55%) | 未取得 | Q1'26 8-K(要約) |
| Lending | 調整後純収益 | 629.3(+53%) | 711.7(+59%) | Q1'26 / Q2'26 8-K(要約) |
| Lending | 貢献利益 | 382.4(前年238.9、+60%) | 399(+63%) | 同上 |
| Lending | 貢献利益率 | 61%(調整後、会社値) | 56.1%(**計算** 399/711.7。会社値は未取得) | 同上 |
| Financial Services | 純収益 | 428.5(+41%) | 466.3(+29%) | Q1'26 10-Q https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000037/sofi-20260331.htm ; Q2'26 10-Q |
| Financial Services | 貢献利益 | 195.6(+32%) | 212.7(前年比+24.4) | 同上 |
| Financial Services | 貢献利益率 | 45.6%(**計算** 195.6/428.5) | 46%(会社値、前年比-6pt) | 同上 |
| Financial Services | NII / 非金利収益 | 未取得 | 249.1(+29%) / 217.2 | Q2'26 10-Q(要約) |
| Technology Platform | 純収益 | 75.1(前年比-27%) | 84.5(前四半期比+13%、前年比-23%) | Q1/Q2'26 |
| Technology Platform | 貢献利益 | 12.0(前年30.9) | 11.8(前年比-65%) | 同上 |
| Technology Platform | 貢献利益率 | 16%(前年30%) | 14%(前年30%) | 同上 |
| FS+TP合算 | 純収益 | 未取得 | 550.8(前年比+17%) | Q2'26(要約) |

- Technology Platform減収の理由(会社記述): 「a large client which fully transitioned off the platform prior to December 31, 2025」(大口顧客が2025年12月31日までにプラットフォームから完全移行)。Q1'26は同要因除くと「like-for-like成長 約12%」(会社説明。Q1'26要約)。
- Loan Platform Business(LPB): Q1'26で連結調整後純収益に140.8を寄与(要約)。Q2'26でパーソナルローン31億ドルをLPB経由で移転、BasePoint Capitalと3年・30億ドルの契約(Q2'26コール要約: https://finance.yahoo.com/markets/stocks/articles/sofi-q2-earnings-call-highlights-140000352.html , T3)。
- 計算(参考): セグメント合計は連結調整後純収益を上回る。Q1'26: 629.3+428.5+75.1 = 1,132.9 vs 連結調整後1,087.232(差 -45.7)。Q2'26: 711.7+466.3+84.5 = 1,262.5 vs 1,205.550(差 -57.0)。差の内訳(セグメント間消去・その他)は**未確認**。
- Q4'25以前のセグメント値: **未取得**。

### 2-4. 株式数(加重平均・期末)

| 項目 | 状況 |
|---|---|
| 加重平均株式数(基本・希薄化後)、期末発行済株式数 | **全四半期 未取得**(要約に出ず) |
| 参考の間接推定(**計算・概算**) | 会社開示のTBV「約$9.5B」÷ TBVPS「$7.34」= 約12.9億株(Q2'26期末の概算。TBVが丸めのため誤差あり)。2026年ガイダンス調整後純利益約$825M ÷ 調整後EPS約$0.60 = 約13.75億株(通期の加重平均希薄化後株式数の概算、ガイダンスが「約」のため誤差あり)。いずれも会社開示株数ではない |

---

## 3. 項目2: 一時要因

| 時期 | 項目 | 金額 | EPSへの影響 | 出所 | 備考 |
|---|---|---|---|---|---|
| Q4 2024 | 税の評価性引当金の戻入 | 258.4(Q4'24中に戻入)。決算説明会では「非経常税便益 計271」。10-K通期では265.3 | GAAP EPS 0.29 vs 調整後EPS 0.05 → 差 0.24(**計算**。調整後は繰延税金便益を除外) | Q4'24 PR https://www.businesswire.com/news/home/20250127863954/en/ ; 10-K https://www.sec.gov/Archives/edgar/data/1818874/000181887425000016/sofi-20241231.htm ; Q4'24 transcript https://s27.q4cdn.com/749715820/files/doc_financials/2024/q4/SOFI-Q4-FY-2024-Earnings-Conference-Call.pdf | 戻入後も一部州・海外で評価性引当金30.7が残存。271/265.3/258.4の差は定義差の可能性(未確認) |
| Q2 2026 | 実効税率が想定超 | 金額未取得 | 調整後EPSで約-0.005(経営陣説明) | Q2'26 コール要約(Fool) | 通期ガイダンスは実効税率約22%前提(当初比+700bp)。当初の税率水準は「mid-teens(10%台半ば)」 |
| Q3 2023(範囲外・参考) | のれん減損 | 金額未取得 | GAAP EPS -0.29 | stockanalysis要約(T3) | 2024年以降ではない |
| 優先株償還、借入消滅損益、ワラント評価損益、その他 | — | **未取得** | **未取得** | — | — |

---

## 4. 項目3: 費用ライン(四半期)

| 四半期 | S&M | 技術・製品開発(T&PD) | 運営費(Cost of ops) | G&A | 総非金利費用 | SBC | 出所 |
|---|---|---|---|---|---|---|---|
| Q1 2025 | 未取得 | 未取得 | 未取得 | 未取得 | 686.3 | 未取得 | Q1'26 10-Q要約の前年比較値 |
| Q1 2026 | 335.5(+41%) | 187.7 | 171.1 | 197.6 | 891.9(+30%) | 未取得 | Q1'26 10-Q https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000037/sofi-20260331.htm (T1・要約経由) |
| Q2 2026 | 未取得 | 前年比+39.1(+26%)(金額未取得) | 未取得 | 未取得 | 前年比+267.9(+37%)。6か月は+473.5(+33%)(金額未取得) | 未取得 | Q2'26 10-Q https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000054/sofi-20260630.htm |

- 計算: Q1'26の4項目合計 335.5+187.7+171.1+197.6 = 891.9 で総非金利費用と一致。よって「貸倒引当金繰入」がこの総額に含まれるか、別建てかは**未確認**(要原文)。
- 上記以外の四半期の費用ライン、SBCは**未取得**。

---

## 5. 項目4: 年次(2021〜2025)

| 年 | 調整後純収益 | 調整後EBITDA | GAAP純利益 | GAAP希薄化後EPS | 期初ガイダンス→修正→実績 | 出所 |
|---|---|---|---|---|---|---|
| 2021 | 未取得 | 未取得 | 未取得 | 未取得 | 未取得 | — |
| 2022 | 未取得 | 未取得 | 未取得 | 未取得 | 未取得 | — |
| 2023 | 未取得 | 未取得 | -300.74(GAAP売上 2,068) | 未取得 | 未取得 | stockanalysis.com(T3、要約)。他出典と食い違いの可能性が指摘されていた(下記) |
| 2024 | 未取得 | 未取得 | 498.67(GAAP売上 2,643) | 0.39(要約。**要検証**) | 未取得 | stockanalysis.com(T3) |
| 2025 | 約3,600(「$3.6B、+38%」) | 約1,050(「$1.05B、+58%」) | 481.32(GAAP売上 3,583) | 0.39(要約。**要検証**) | 未取得 | 調整後: 2025年年次株主レター/ARS要約 https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000034/sofitech2025ars.pdf (T1・要約経由)。GAAP: stockanalysis.com https://stockanalysis.com/stocks/sofi/financials/ (T3) |

- 2025年・2024年の期初ガイダンス/中間修正/実績の突合は**全く未取得**(2025年各四半期の8-K URLは検索結果に出たが本文は未取得。URL一覧は§10)。

---

## 6. 項目5: 2026年ガイダンスの推移

| 時点 | 調整後純収益 | 調整後EBITDA | 調整後純利益 | 調整後EPS | 会員純増 | その他 | 出所 |
|---|---|---|---|---|---|---|---|
| 期初(2026年1月、Q4'25決算) | 約4,655(約+30%) | 約1,600(マージン約34%) | 約825(マージン約18%) | 約0.60 | 会員数 前年比+30%以上 | Q1'26見通し: 調整後純収益約1,040 / 調整後EBITDA約300 / 調整後純利益約160 / 調整後EPS約0.12 | Q4'25 8-K https://www.sec.gov/Archives/edgar/data/1818874/000181887426000008/a2025q4earningsrelease.htm (T1・要約経由) |
| 4月(Q1'26決算) | **改定の有無を確認できず**(要約は「Q1決算は通期目標として4,655/1,600/825/0.60を保持」と読める記述だが断定できない) | 同左 | 同左 | 同左 | 未取得 | Q1実績: 調整後純収益1,087.232(見通し約1,040)、調整後EBITDA339.9(見通し約300)、調整後EPS0.12(見通し約0.12) | Q1'26 8-K(要約) |
| 7月(Q2'26決算、2026-07-29) | **4,750〜4,850に引き上げ(+32〜35%。従来は約+30%)** | 約1,600据え置き(マージン33〜34%) | 約825据え置き(マージン約17%) | 約0.60据え置き | 会員数 前年比+30%以上(据え置き) | 税率前提: 実効税率約22%(当初比+700bp)。CFO発言「当初のmid-teens税率なら新ガイダンスは0.65だった」(要約)。経営陣は「利益率改善より成長投資を優先」と説明(要約) | Q2'26 8-K / 説明会 https://s27.q4cdn.com/749715820/files/doc_financials/2026/q2/SoFi-2Q-2026-Earnings-Transcript_FINAL.pdf ; Fool https://www.fool.com/earnings/call-transcripts/2026/08/07/sofi-sofi-q2-2026-earnings-call-transcript/ ; Qz https://qz.com/sofi-record-revenue-full-year-forecast-raised-072926 (T1/T3・要約経由) |
| 10月 | 未発表(Q3決算は2026-10-27予定) | — | — | — | — | — | — |

- GAAP純利益ガイダンス、製品純増、ROTCE目標: **未取得**(取得した要約には出現せず)。
- 中期目標: 「2025年→2028年に調整後純収益の年平均成長率30%以上」(2025年次レター/ARSの要約。T1・要約経由)。以前の「2026年EPS $0.55〜0.80」目標の現在の扱い、2027年以降の目標、ROTCE目標は**未取得**。
- Q2'26説明会発言(要約): 「リスクベース自己資本比率は長期的にはlow-to-mid teensが適切」(Noto)、「現行の運営計画で自己資金賄い(self-funded)」(Lapointe)。

---

## 7. 項目6: B/S(取得できた範囲)

| 項目 | 2025-12-31 | 2026-06-30 | 出所 |
|---|---|---|---|
| 預金合計 | 37,505.395(百万ドル) | 45,543.160(うちブローカード預金 4,533.210) | Q2'26 10-Q https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000054/sofi-20260630.htm (T1・要約経由) |
| 有形自己資本(TBV、会社値) | 未取得 | 約9,500(「$9.5B」) | Q2'26 8-K(要約) |
| 1株当たりTBV(TBVPS、会社値) | 未取得 | **$7.34**(前年同期$4.72、+56%) | Q2'26 8-K(要約) |
| 総自己資本比率 | 未取得 | 18.8%(要求水準10.5%)※第三者のレビュー記事。会社開示ではない(T4) | Yahoo Finance記事等(要約) |
| CET1比率 | 未取得 | 未取得 | — |
| ROTCE(会社値) | 未取得 | 未取得 | — |
| 総資産 | 未取得 | 絶対額未取得。「総資産は+72億ドル(貸出増と現金・有価証券増)」との説明会要約あり(比較期間が不明確) | Q2'26コール要約 |
| 貸出金(個人/学生/住宅別、公正価値/償却原価別) | 未取得 | 未取得。ただし説明会要約: パーソナルローン評価掛け目104.7%(前四半期比-71bp)、学生ローン104.4%(同-85bp) | Q2'26コール要約 |
| 借入(倉庫ライン、証券化、転換社債の銘柄別額・満期・転換価格) | 未取得 | 未取得 | — |
| 自己資本(総額) | 未取得 | 未取得 | — |

- 他の断片(未検証・T4): GuruFocus「Tangible Book per Share $6.90」(時点不明) https://www.gurufocus.com/term/tangibles-book-per-share/SOFI ; Yahoo Finance記事「SoFi's Tangible Book Value Grew 80% in a Year. Yet the Stock Fell 9%」(時点不明) https://finance.yahoo.com/markets/stocks/articles/sofis-tangible-book-value-grew-184300748.html 。どの四半期か未確認のため数値としては採用しない。

---

## 8. 項目7: 資本調達・希薄化の履歴

**数値はすべて未取得。** 手掛かりとして検索結果に現れた書類(内容は未確認):

| 書類 | URL | 示唆(推測を含まず、書類名のみ) |
|---|---|---|
| 424B3(目論見書)「sofijuly2025primary-prelim」 | https://www.sec.gov/Archives/edgar/data/1818874/000181887425000157/sofijuly2025primary-prelim.htm | 2025年7月付の一次募集関連の目論見書が存在。規模・価格・株数は未取得 |
| 「sofi-20260430」(書式不明) | https://www.sec.gov/Archives/edgar/data/1818874/000181887426000032/sofi-20260430.htm | 2026-04-30付とみられる提出書類。内容未確認 |

- 公募増資(2021〜2026)、転換社債の発行・買戻し・転換、優先株償還、自社株買い、SPAC時のワラント、年末発行済株式数の推移: **未取得**。

---

## 9. 項目8: キャッシュフロー

営業CF(2023〜2025、直近四半期累計)、capex: **未取得**。

---

## 10. 次回取得時の一次資料URL一覧(検索結果に出現。本文は未取得)

| 期 | 8-K Exhibit 99.1(決算PR) | 10-Q / 10-K |
|---|---|---|
| Q1 2024 | https://www.sec.gov/Archives/edgar/data/1818874/000181887424000115/q12024earningsrelease.htm | — |
| Q2 2024 | https://www.sec.gov/Archives/edgar/data/1818874/000181887424000169/q22024earningsrelease.htm | — |
| Q3 2024 | https://www.sec.gov/Archives/edgar/data/1818874/000181887424000229/q32024earningsrelease.htm | 10-Q https://www.sec.gov/Archives/edgar/data/1818874/000181887424000233/sofi-20240930.htm |
| Q4 2023(参考) | https://www.sec.gov/Archives/edgar/data/1818874/000181887424000004/q42023earningsrelease.htm | — |
| Q4 2024 | https://www.sec.gov/Archives/edgar/data/1818874/000181887425000006/q42024earningsrelease.htm ; PDF https://s27.q4cdn.com/749715820/files/doc_financials/2024/q4/Q4-2024-Earnings-Release-6.pdf | 10-K https://www.sec.gov/Archives/edgar/data/1818874/000181887425000016/sofi-20241231.htm ; XBRL https://www.sec.gov/Archives/edgar/data/1818874/000181887425000016/Financial_Report.xlsx |
| Q1 2025 | https://www.sec.gov/Archives/edgar/data/1818874/000181887425000068/a2025q1earningsrelease.htm | — |
| Q2 2025 | https://www.sec.gov/Archives/edgar/data/1818874/000181887425000148/a2025q2earningsrelease.htm | — |
| Q3 2025 | https://www.sec.gov/Archives/edgar/data/1818874/000181887425000204/a2025q3earningsrelease.htm | 10-Q https://www.sec.gov/Archives/edgar/data/1818874/000181887425000210/sofi-20250930.htm |
| Q4 2025 | https://www.sec.gov/Archives/edgar/data/1818874/000181887426000008/a2025q4earningsrelease.htm | ARS https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000034/sofitech2025ars.pdf |
| Q1 2026 | https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000020/a2026q1earningsrelease.htm ; PDF https://s27.q4cdn.com/749715820/files/doc_financials/2026/q1/2026-Q1-Earnings-Release_FINAL.pdf | 10-Q https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000037/sofi-20260331.htm |
| Q2 2026 | https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000050/a2026q2earningsrelease.htm ; PDF https://investors.sofi.com/files/doc_financials/2026/q2/2026-Q2-Earnings-Release.pdf | 10-Q https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000054/sofi-20260630.htm |

トランスクリプト/資料: Q1'26 https://s27.q4cdn.com/749715820/files/doc_financials/2026/q1/SoFi-Q1-2026-Transcript-docx.pdf ; Q2'26 https://s27.q4cdn.com/749715820/files/doc_financials/2026/q2/SoFi-2Q-2026-Earnings-Transcript_FINAL.pdf ; Q2'26投資家向け資料 https://s27.q4cdn.com/749715820/files/doc_financials/2026/q2/2026-Q2-Investor-Presentation.pdf

---

## 11. 取れなかった項目(リスト)

1. 項目1: Q1 2024〜Q3 2025の大半(調整後純収益、NII、非金利収益、セグメント別、普通株主帰属純利益、加重平均株式数(基本・希薄化後)、期末発行済株式数)。Q4'25以前のセグメント別、Q2'26連結の正確なGAAP総純収益・連結NII・非金利収益。Q2 2024、Q3 2025(調整後系)、Q1 2025のGAAP純利益。
2. 項目2: 優先株償還・借入消滅損益・のれん減損(2024以降)・ワラント評価損益・その他一過性の金額とEPS影響(Q4'24の評価性引当金戻入と、Q2'26の税率要因を除く)。
3. 項目3: Q4'24〜Q4'25とQ2'26の費用ライン(S&M、T&PD、G&A、Cost of ops)、全四半期のSBC。
4. 項目4: 2021〜2024の調整後純収益・調整後EBITDA・GAAP純利益・EPS、2025年のGAAP希薄化後EPSの確認値、全年の期初ガイダンス→中間修正→実績。
5. 項目5: 2026年4月時点の改定有無、GAAP純利益ガイダンス、製品純増ガイダンス、ROTCE目標、旧「2026年EPS $0.55〜0.80」目標・2027年以降目標の現在の扱い、10月改定(Q3決算は10/27予定で未発表)。
6. 項目6: 総資産、貸出金(種類別・公正価値/償却原価別)、借入明細(倉庫ライン・証券化・転換社債の額・満期・転換価格)、自己資本総額、CET1、ROTCE、Q2'26以外のTBV/TBVPS・預金(直近6四半期のB/S全般)。
7. 項目7: 公募増資・転換社債・優先株・自社株買い・ワラント・年末株式数の全履歴。
8. 項目8: キャッシュフロー全体(営業CF、capex)。

## 12. 出典間で食い違った(または要検証の)数値

| # | 項目 | 食い違い | 採用/扱い |
|---|---|---|---|
| 1 | Q2'26 GAAP総純収益 | 「$1.2B(+43%、前年854.9)」vs 要約中の「約1,218.7」(未検証)vs MarketScreenerの「1,140.5」(https://www.marketscreener.com/news/sofi-technologies-inc-reports-earnings-results-for-the-second-quarter-and-six-months-ended-june-30-ce7f51d2d08eff26 、T3) | 会社の見出し「$1.2B、+43%」を採用。1,140.5は+33%となり会社の+43%と整合しないため不採用。正確値は要原文 |
| 2 | Q2'26 10-Qの「Total net revenue 466.3 / 894.8」 | 連結ではなくFinancial Servicesセグメントの値(計算: 428.5+466.3=894.8)。連結総純収益($1.2B)と混同しない | セグメント値として使用 |
| 3 | Q2'26 NII | 10-Q「NII +29%、249.1」はFSセグメント値。説明会の「キャッシュ収益ベースNII 7.9億」と連結値が不整合/未照合 | 連結NIIは未取得 |
| 4 | Q4'25 GAAP総純収益 | 「$1.0B(前年734.1から+40%)」vs Yahoo Scorecardの「$1.01B」。734.1×1.40≒1,028、1.01B/734.1=+37.6%でどちらとも微妙に合わない(**計算**) | 正確値未取得。調整後1,013(+37%)のみ採用 |
| 5 | Q4'24 税便益 | 評価性引当金戻入258.4 / 説明会の非経常税便益271 / 10-K通期265.3 | 定義差の可能性。並記 |
| 6 | FY2024・FY2025のGAAP希薄化後EPS | stockanalysis.comがともに$0.39と要約。要約者自身が「FY2024・FY2023の純利益は会社の四半期報告と整合しないように見える」と注記 | T3のため不採用扱い(参考値)。8-K/10-Kで確認要 |
| 7 | Q2'26 Lending貢献利益率 | 計算値56.1%(399/711.7)は、Q1'26会社値61%から5pt低下。会社値が未取得のため分母(調整後 vs GAAP)の違いの可能性 | 要原文確認 |
| 8 | 総自己資本比率18.8% | 会社開示ではなく第三者記事(T4)。CET1は未取得 | 参考値 |
| 9 | Q4'25決算の発表日 | BusinessWire URLの日付接頭辞は20260130。正式な発表日は未確認 | 要確認 |
| 10 | 総資産「+72億ドル」 | 説明会要約の記述で、比較期間(前四半期比か前年末比か)が不明 | 不採用 |
