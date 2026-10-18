# R8: 参照クラス(ピア・市場平均)とSOFIコンセンサス全年度(取得日 2026-10-18、SOFI株価 $14.55 = 2026-10-16終値)

## 0. 取得方法・Tier定義・読み方(必読)

- 使えたのは WebSearch のみ(40回使用)。**全数値は検索結果の要約文(要約モデルが各ページ断片から作った文章)経由の二次アクセス**。ページ本文は読んでいない。桁・日付は一次ページで要再確認。
- Tier(元データの性質で付与。アクセス経路は全て検索要約):
  - **T1**: 会社の一次開示(SEC 8-K、決算リリース)
  - **T2**: 機関・データベンダーの公式資料(FactSet Earnings Insight、S&P Global MI、Mercer Capital)
  - **T3**: データ集約サイト・メディアの自動生成/記事(MarketBeat、StockAnalysis、Yahoo、Benzinga、Tickflow、TIKR、Zacks系)
  - **T4**: 個人ブログ・学習サイト・AI生成ページ・独自モデル出力(VCP Scanner、FIG学習サイト、simianx 等)
- 「計算」は私の算術(式明記)。出所の値ではない。
- **日付が揃っていない**: ピアの株価は 2026-10-08〜10-17 のMarketBeat記事(前営業日終値を「opened at」と表記する慣行。下表は記事日を明記)、LC・CHYMは古い。同一出典・同一日のピア表は作れなかった(StockAnalysis/Finviz は検索で当日値を返さなかった)。
- MarketBeat の P/E・PEG は**直近4四半期(GAAP)ベースのトレーリング**で、日ごとに値が動く(COFで 9.70〜12.25)。予想PERではない。予想PERは各社の会社ガイダンス/コンセンサスEPSで私が割った「計算」値を併記した。
- 1周目(R2_market.md)で取得済みの SOFI 市場データ・年度別EPS(Yahoo/StockAnalysis/Chartmill/WSZ 等)は再掲を最小限にした。

---

## バリュエーションに直結する事実 5点

1. **SOFI は $14.55 で P/TBV 1.98x(計算: 14.55 ÷ TBVPS $7.34、2026-06-30)。TIKR は 2.18x(2026-09-29)、前年同日(2025-09-30)は 5.65x と記載。** 一方、ROE 7.1%(TIKR、トレーリング)、ROTCE 7.1%(Investing.com、2026Q2)で、会社の長期目標は ROTCE 20〜30%。TIKRは ROTCE を 8〜9%と自己推計。(T3、§4)
2. **同じ P/TBV の物差しで置いたピア**: JPM は約 2.98x(計算: $336 ÷ TBVPS $112.64)、ROTCE 20%(調整後 21%、2026Q3、SEC 8-K、T1)。ALLY は約 0.93〜0.95x(P/B 0.95〔6/30〕、P/TBV 0.93〔日付不明〕)、LC は約 1.54x(計算: $19.21 ÷ TBVPS $12.49)で LC の ROTCE は 11.9%(2025Q4)。(§1)
3. **ピアの予想PER(今期EPSで割った計算値)**: COF 約8.4x、ALLY 約7.3〜7.4x、SLM 約7.1x、LC 約11.2x、JPM 約13.3x、AXP 約17.8x、NU 約16x(StockAnalysis表示)、HOOD 約39〜50x(StockAnalysis表示)、SOFI 23.9〜24.7x(今期)/ 17.3〜17.7x(来期)。成長・ROE が高い NU(会社報告ROE 33%、PEG 0.45〜0.64)と HOOD(ROE 23.6%、PEG 2.1〜2.7)で倍率が大きく分かれる。(§1)
4. **S&P 500 の12か月先予想PER は 19.0倍(FactSet 2026-10-16版)。5年平均 19.8、10年平均 19.1。** Q3 2026 の前年比EPS成長率の見通しは +29.6%(10/9版)、CY2027成長は旧版で +17.4%。銀行セクターは Mercer Capital によると 2026年の株価上昇の約80%がP/E拡大由来(2025末→2026-08-24、298行の中央値で+20%)。(§2)
5. **SOFI のコンセンサスEPS(調整後)**: 2026 = 0.59〜0.61、2027 = 0.82〜0.84、2028 = 1.08(範囲0.95〜1.27)、2029 = 1.32(Tickflow、4名、1.15〜1.54。**列見出しが要約に出ておらず未確認**)。四半期は Q3'26 = 0.17、Q4'26 = 0.19、Q1'27 = 0.18、Q2'27 = 0.20(Benzinga)。$14.55 で割ると 24.3x → 17.5x → 13.5x → 11.0x(計算、中央値)。2030年は取れず。(§3)

---

## 1. ピア比較表

### 1-1. 価格・時価総額・倍率(出所と日付つき)

| 銘柄 | 株価(基準日) | 時価総額 | MarketBeat等のトレーリングP/E・PEG | 今期EPS(出所) | 予想PER 今期(計算) | 来期EPS・予想PER(計算) | 出所 |
|---|---|---|---|---|---|---|---|
| **SOFI** | $14.55(10/16) | $18.79B | - | 0.59〜0.61(§3) | 23.9〜24.7x | 0.82〜0.84 → 17.3〜17.7x | R1、§3 |
| **COF** | $201.72(10/17付記事、=10/16終値と推定) | $123.75B | P/E 9.92、PEG 0.96(10/17)。同サイトで 10/16: 9.70 / 0.94、10/14: 12.25 / 0.74 | FY1 EPS $23.88(成長+16.86%)、Dividend.com 2026-08-19 | 8.45x(計算: 201.72 ÷ 23.88。EPSの日付は8月で価格は10月) | 未取得 | MarketBeat https://www.marketbeat.com/instant-alerts/filing-capital-one-financial-corporation-cof-stock-annex-advisory-services-llc-reduces-stake-2026-10-17/ ; Dividend.com(検索要約) |
| **AXP** | $313.47(10/17付記事、=10/16終値と推定)。10/16付記事は $313.61 | $211.79B(10/16付記事、$313.61時点) | P/E 19.03、PEG 1.31 | 2026ガイダンス $17.30〜17.90(最新四半期EPS $4.53、予想$4.41) | 17.5〜18.1x(計算: 313.47 ÷ 17.90〜17.30。中央17.8x) | 未取得 | MarketBeat https://www.marketbeat.com/instant-alerts/filing-american-express-company-axp-stock-mather-group-llc-raises-holdings-2026-10-16/ |
| **ALLY** | $37.45(10/9付記事)、$37.63(10/7付記事) | $11.39B(10/9) | P/E 8.88、PEG 0.24(10/9)。0.23(10/7) | 当期コンセンサス 5.05(10/9)/ 5.16(10/7) | 7.3〜7.4x(計算: 37.45 ÷ 5.05、37.63 ÷ 5.16) | 未取得 | MarketBeat https://www.marketbeat.com/instant-alerts/analyst-ally-financial-nyse-ally-stock-rating-upgraded-by-ubs-group-2026-10-07/ ; …royal-bank-of-canada-2026-10-09/ |
| **NU** | $14.89(10/15付記事)。8/28 は $14.30 | $72.29B(10/15)。MarketBeatページ $70.78B | P/E 20.12、PEG 0.64(10/15)。ページ値 19.70 / 0.61 | 未取得 | StockAnalysis表示の forward P/E 15.99〜16.29(スナップショット、価格は$15.58等で日付不一致) | 未取得 | MarketBeat https://www.marketbeat.com/instant-alerts/consensus-nu-holdings-ltd-nyse-nu-stock-rated-moderate-buy-by-wall-street-brokerages-2026-10-15/ ; StockAnalysis https://stockanalysis.com/stocks/nu/ |
| **HOOD** | $109.22(10/13付記事)。10/2 は約$115.78 | $98.20B(10/13) | P/E 48.11、PEG 2.13(10/13)。10/2: 50.82 / 2.35 | 未取得 | StockAnalysis表示の forward P/E 38.93($98.87時点)/ 49.55($119.40時点)。価格が一致しない2枚 | 未取得 | MarketBeat(Oct 13記事、Truist目標$134)、StockAnalysis https://stockanalysis.com/stocks/hood/statistics/ |
| **LC** | $19.21(2026-08の記事。10月値は未取得) | $2.22B(8月) | P/E 12.89(8月) | FY2026 会社ガイダンス $1.65〜1.80、コンセンサス 1.71(5月) | 11.2x(計算: 19.21 ÷ 1.71。価格は8月) | 未取得 | MarketBeat(2026-08-03/08-13記事)、goldesel.de |
| **SLM** | $22.17(10/15付記事) | 未取得 | 未取得 | FY2026 ガイダンス $3.10〜3.20、コンセンサス 3.12 | 7.1x(計算: 22.17 ÷ 3.12) | FY2027(MarketBeat「next fiscal year」)3.41 → 6.5x(計算) | MarketBeat https://www.marketbeat.com/instant-alerts/upcoming-slm-slm-set-to-announce-earnings-on-thursday-2026-10-15/ |
| **UPST** | $22.60(10/15付記事) | $2.20B | P/E 46.20、PEG 0.84(10/15) | TIKR: 2026年 約$2、2027年 約$3(日付不明)。SA(3/31)2026 = 2.27 | 約11.3x(計算: 22.60 ÷ 2.0。EPS定義不明) | 約7.5x(計算: 22.60 ÷ 3.0) | MarketBeat(Oct 15記事)、TIKR https://www.tikr.com/blog/upstart-bank-charter-application-targets-a-26-upside-gap-in-upst-stock |
| **CHYM** | $27.93(10/8付記事)。10/2終値 $27.25 | $10.57B(10/8) | P/E -398.94(トレーリング、GAAP赤字) | Q3'26(11/4発表)コンセンサスEPS $0.08(6名) | 通期EPS未取得 | 2027年 利益 $267M(Simply Wall St、16名、2026-04更新)→ 約39.6x(計算: $10.57B ÷ $267M。日付混在) | MarketBeat(Oct 8記事)、Simply Wall St https://simplywall.st/stocks/us/diversified-financials/nasdaq-chym/chime-financial/future |
| **JPM** | 約$336(10/13寄り付き付近) | 未取得 | トレーリング P/E 14.25(決算前の記事、陳腐) | 2026 コンセンサス 約25.33(出所は要約中「別の情報源」) | 約13.3x(計算: 336 ÷ 25.33) | 未取得 | beinsure/Morningstar 検索要約(下記) |

### 1-2. P/TBV(またはP/B)、ROTCE(またはROE)、成長率

| 銘柄 | P/TBV・P/B(出所・日付) | ROTCE・ROE(出所・日付) | EPS成長・PEG | Tier |
|---|---|---|---|---|
| **SOFI** | P/TBV 1.98x(計算 10/16)。TIKR 2.18x(9/29)。P/B 1.70x(計算: 14.55 ÷ BVPS $8.58) | ROTCE 7.1%(Investing.com 2026Q2)。ROE 7.1%(TIKR)。TIKR推計 ROTCE 8〜9% | 来期成長 +37.7〜39.0%(計算、R1)。会社: 2028まで EPS CAGR 38〜42% | T1(TBVPS)/ T3 |
| **COF** | P/B 1.10x(Yahoo、2026-06-30)、前期 1.01x。P/TBV 1.92(StockAnalysis、**2025年7月の古いページ**)。**2026年のTBVPSは未取得** | ROTCE 未取得。ROE 0.08(TipRanks、日付不明) | FY1 成長 +16.86%(Dividend.com 8/19)。PEG 0.96(MarketBeat)。Yahoo forward P/E 10.82(6/30)。ValueInvesting forward P/E 8.77(日付不明) | T3 |
| **AXP** | P/B 6.17(StockAnalysis、**653日前のページ**で陳腐)。2026年値は未取得 | ROE 34.38%(同、陳腐) | PEG 1.31(MarketBeat 10/16)。forward P/E 16.89(StockAnalysis、121日前、価格$313.59) | T3 |
| **ALLY** | P/B 0.95(Yahoo 2026-06-30)。P/TBV 0.93(roic.ai、日付不明)。Seeking Alpha 3/31: P/B 0.89、forward P/B 0.80 | 未取得(Q3は10/20発表予定。Benzinga予想 $1.35 / Earnings Whispers $1.43) | Yahoo: forward P/E 6.55(6/30)、PEG(5年予想)0.38。別ページ 8.30 / 0.49。MarketBeat PEG 0.24 | T3 |
| **NU** | P/B 4.98(StockAnalysis、古い)、5.3(Value Research 8/28)。P/TBV 6.06(roic.ai、日付不明) | **ROE 33%(会社、2026Q2、2026-08-13発表。純利益$1.1B、+49%)**。StockAnalysis ROE 26.65〜30.05% | PEG 0.45〜0.48(StockAnalysis)、0.61〜0.64(MarketBeat) | T1/T3 |
| **HOOD** | P/B 11.32(StockAnalysis $119.40時点)、10.79(TSX上場ページ) | ROE 23.62%(StockAnalysis) | PEG 2.67(StockAnalysis)、2.13(MarketBeat 10/13)。beta 2.35 | T3 |
| **LC** | **TBVPS $12.49(2026-03-31、前期$12.30、前年$11.22)** → P/TBV 1.54x(計算: 19.21 ÷ 12.49。価格は8月) | ROTCE 11.9%(2025Q4)。14.5%(2026Q1と報じる独語記事。期間不明、要確認) | 会社ガイダンス FY26 EPS $1.65〜1.80。実効税率 約24% | T1(TBVPS、SEC 8-K/10-Q)/ T3 |
| **SLM** | 未取得(TBVPS不明。roic.ai BVPS 約$10.46、列の対応不明) | ROE 33.81%(MarketBeat)、31.16%(MarketInOut)、0.28(TipRanks) | EPS $3.12 → $3.41(+9.3%、計算) | T3 |
| **UPST** | P/B 3.47(Yahoo、約2026-07-30) | ROE 6.67%(Macrotrends、2026-03-31までの四半期) | Yahoo forward P/E 33.67(約7/30、時価総額$2.55B)。MarketScreener 2026年 44.8x、2027年 16.5x(価格$6.38と記載で不整合) | T3 |
| **CHYM** | P/B 約5.65(別ページ、$21.68時点)、8.92($33.15時点)。現在値は未取得 | 未取得 | forward P/E 13.22($21.68時点)、43.48($33.15時点) | T3 |
| **JPM** | **TBVPS $112.64、BVPS $132.30(2026Q3、前年比+7%)** → P/TBV 約2.98x、P/B 約2.54x(計算: 336 ÷ 各値) | **ROTCE 20%(報告ベース)、21%(有価証券損$658M控除後)**。EPS $5.57(調整後$5.75)、純利益$15.3B | 2026 EPS 約25.33。simianx(2026-08): $359で P/TBV 3.17x、Q2調整後ROTCE 23%。Morningstar 公正価値 $330 | T1(8-K)/ T3 |

出所URL(上表の補足):
- JPM 2026Q3 8-K: https://www.sec.gov/Archives/edgar/data/0000019617/000162828026065616/a3q26_earningsxpresentat.htm 、Pulse2 https://pulse2.com/jpmorgan-chase-q3-2026-results 、価格・Morningstar https://www.morningstar.com/stocks/jpmorgan-earnings-solid-results-despite-capital-markets-softening
- LC Q1 2026 8-K: https://www.sec.gov/Archives/edgar/data/0001409970/000140997026000059/q126exhibit991er.htm
- COF Yahoo: https://finance.yahoo.com/quote/COF/key-statistics/ 、ValueInvesting https://valueinvesting.io/COF/metric/forward-pe
- ALLY Yahoo: https://finance.yahoo.com/quote/ALLY/key-statistics/ 、roic.ai https://www.roic.ai/quote/ALLY/statistics 、Seeking Alpha https://seekingalpha.com/symbol/ALLY/valuation/metrics
- NU 2026Q2: https://goldesel.de/aktien/news/nu-holdings-schlagt-q2-gewinn-und-umsatzschatzungen-deutlich-roe-steigt-auf-33 、Value Research https://www.valueresearchonline.com/stocks/298146/nu-holdings-ltd-nu/key-ratios/
- UPST ROE: https://www.macrotrends.net/stocks/charts/UPST/upstart-holdings/roe
- 比較ページ(Walnut Invest、2026年7月スナップショット): https://walnutinvest.com/stocks/compare/nu-vs-sofi 、https://walnutinvest.com/stocks/compare/hood-vs-sofi

### 1-3. 単一出典・単一日付の比較(7月スナップショットのみ)

| 銘柄 | forward P/E | P/B | trailing P/E | 出所 |
|---|---|---|---|---|
| NU | 約11.6x | 約5.2 | 20.6 | Walnut Invest(2026年7月、価格日不明、T3〜T4) |
| SOFI | 約22.2x | 約2.1 | 40.1 | 同上 |
| HOOD | 約36.7x | 約10.5 | 52.7 | 同上(beta: HOOD 2.35 / NU 0.95) |

注: NU の forward P/E は StockAnalysis 系(15.99〜16.29)と約4.5ポイント食い違う(§6)。

### 1-4. ピアの決算日程(10/18時点でQ3未発表のもの)

| 銘柄 | Q3 2026 発表予定 | 出所 |
|---|---|---|
| ALLY | 2026-10-20 寄り前(7:30 ET) | Ally IR(placera/finviz 転載) |
| SLM | 10/22 引け後(MarketBeat)/ 10/26 引け後(Earnings Whispers) | 食い違い |
| AXP | 2026-10-23 7:00 ET | Business Wire |
| SOFI | 2026-10-27 | R1 |
| NU | 2026-11-12(StockAnalysis) | StockAnalysis |
| CHYM | 2026-11-04 | 検索要約(Benzinga系) |
| JPM | 発表済(2026-10-13頃) | SEC 8-K |

---

## 2. 市場平均

### 2-1. S&P 500(FactSet Earnings Insight、T2)

| 発行日 | 12か月先予想PER | 5年平均 | 10年平均 | 備考 |
|---|---|---|---|---|
| 2026-10-16(Earnings Season Update) | **19.0** | 19.8 | 19.1 | 「5年平均・10年平均を下回る」。Q3末(9/30)から不変 |
| 2026-10-09 | 19.1(別検索の要約) | 5年平均を下回ると記載(数値は要約に出ず) | 出ず | Q3 2026 前年比EPS成長見通し **+29.6%**(10/2版 29.5%、9/4版 28.5%、6/30版 26.7%) |
| 2026-10-02 | 19.0 | 19.8 | 19.1 | - |
| 2026-09-25 | 19.2 | 5年平均を下回ると記載 | - | - |
| 2026-08-07 | 20.0 | 19.9 | 19.0 | 5年平均・10年平均を上回る |
| 2026-06-26 | 20.1 | 19.9 | 19.0 | - |
| 2026-03-27 | 19.9 | 19.9 | 18.9 | - |

- 成長率: CY2026 EPS成長 +32.4%(FactSetのプレビュー記事、**発行日不明**)。CY2027 EPS成長 +17.4%、売上成長 +8.2%(**約100日前の版**、10月版の値は取れず)。
- 出所: https://insight.factset.com/sp-500-earnings-season-update-october-16-2026 、https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_100926.pdf 、…/EarningsInsight_100226.pdf 、…/EarningsInsight_080726.pdf (いずれも検索要約経由)
- 参考(T3): MercoPress 2026-10-12 は forward P/E 20.0、5年平均19.9、10年平均19.0と記載(= FactSet 8月版の値で、10月値とは別)。

### 2-2. 銀行セクター

| 項目 | 値 | 基準日 | 出所・Tier |
|---|---|---|---|
| 公開銀行298行の株価上昇率(中央値) | +20%(2025年末〜2026-08-24)。うち約20%が2026・2027年EPS予想の上方修正、約80%がP/E倍率の拡大 | 2026-08-24 | Mercer Capital Bank Watch 2026-08 https://mercercapital.com/media/ax3brwvg/mercer-capital_bank-watch_2026-8.pdf (T2) |
| P/TBV 125%超の銀行の割合 | 43%(2025年末)→ 70%(2026-08-24)。AOCI除く | 2026-08-24 | 同上 |
| Texas Bank Index の P/TBV | 145%(8/27版)、153%(7/29版) | 2026-08-27 | Mercer Capital Texas版(S&P Global MI) (T2) |
| Community Bank Index の P/TBV | 138%(8/27版)、137%(7/29版) | 同上 | 同上 |
| 米銀中央値 P/調整後TBV | 約1.46x(「今春」) | 2026年春 | FIG学習サイト ibinterviewquestions.com(S&P Global MIを引用と記載、**未検証**)(T4) |
| 大手行 P/TBV(同サイト、2026年初) | JPM 約2.6x、BAC 約1.1x、C 約0.6x | 2026年初 | 同上(T4) |
| KBW Regional Banking Index(KRX)の予想PER | 約11x(2026年初)、長期平均を28%下回る | 2026年初 | Angel Oak Capital https://angeloakcapital.com/bigger-led-smaller-could-run-the-case-for-regional-banks/ (T3) |
| KBW Bank Index(BKX)の2025年リターン | +32.57% | 2025 | 同上 |
| KBWB(BKX連動ETF)トレーリングP/E | 15.78(2026-07-31)。別の GuruFocus スナップショット P/E 13.06、P/B 1.47(日付不明) | 2026-07 | StockAnalysis https://stockanalysis.com/etf/kbwb/ 、GuruFocus (T3) |
| KRX指数水準 | 135.17(2026-10-15) | 2026-10-15 | Nasdaq https://indexes.nasdaqomx.com/Index/Overview/KRX |
| **KBW Bank Index(BKX)の予想PER・P/TBV(2026-10)** | **未取得** | - | - |

---

## 3. SOFI のコンセンサス(全年度)

### 3-1. 年度別EPS・売上

TradingView の forecast ページは検索要約に出ず(allowed_domains指定でも TradingView News の記事のみ)。以下は他出典。R1の表(Yahoo、StockAnalysis、Chartmill、WSZ)に追加した分のみ載せる。

| 年度 | EPS | 売上 | 出所・日付・Tier |
|---|---|---|---|
| FY2026 | 0.59〜0.61(R1)。Ticker League: 13名、範囲 0.57〜0.62、平均 0.60。Seeking Alpha: 0.61。**Zacks: 前年比 +51.3%、売上成長 +30.8%** | $4.87〜5.0B(R1) | Ticker League https://tickerleague.com/companies/SOFI/price-target ; Seeking Alpha https://seekingalpha.com/symbol/SOFI/earnings/estimates ; Zacks(TradingView News経由) https://www.tradingview.com/news/zacks:36cf38e1e094b:0-should-you-buy-hold-or-fold-sofi-technologies-stock-post-q2-earnings/ (T3) |
| FY2027 | 0.82〜0.84(R1)。「0.8240 vs 2026年 0.5947」(2026年夏の分析記事、出所名なし)。Benzinga四半期: Q1'27 0.18 + Q2'27 0.20(H1計 0.38) | $6.1〜6.16B(R1)。Simply Wall St: **$5.75B**。別ページ $5.9B | Benzinga https://www.benzinga.com/quote/SOFI/earnings-forecasts ; Simply Wall St https://simplywall.st/stocks/de/diversified-financials/etr-6b0/sofi-technologies-shares/future (T3) |
| FY2028 | 1.08(R1: Chartmill、WSZ。WSZ範囲 0.95〜1.27) | $7.58B(R1 Chartmill)。Simply Wall St **$7.04B**(9名)。別ページ $7.1B | 同上 (T3) |
| **FY2029** | **平均 $1.32、範囲 $1.15〜$1.54、4名**(Tickflowの2029-12-31行「$1.15 / $1.32 / $1.54 / 4」を縦線区切りで表示。**列見出しは要約に出ず、低/平均/高/人数と推定。未確認**)。Seeking Alpha: 2029年コンセンサスEPS成長 約28.8%(ドル値は出ず)。Stockalarm: FY2029 EPS成長 +30.40%、売上成長 +8.81%(ドル値は出ず) | 別ページ $7.9B(成長は一桁台後半〜低い二桁と記載、出所名なし) | Tickflow https://www.tickflow.io/stock/SOFI/forecast ; Seeking Alpha https://seekingalpha.com/symbol/SOFI/valuation/price-earnings-peg-ratios ; Stockalarm https://pro.stockalarm.io/quote/SOFI/analysts (T3) |
| **FY2030** | **未取得** | **未取得** | - |
| (参考・コンセンサスではない) | VCP Scanner独自モデル: EPS 2027 = 0.63、2028 = 0.70、2029 = 0.78(同サイトは直近を「コンセンサス0.60と整合」と記載) | モデル売上 2027 $5.5B、2028 $6.1B、2029 $6.6B(出所の対応が不明確) | https://www.vcpscanner.com/valuation/sofi/estimates (T4) |
| (参考・古い) | 24/7 Wall St(2025-08)の自社予測表: 2029 = 1.02、2030 = 1.10(コンセンサスではなく古い) | - | https://247wallst.com/forecasts/2025/08/01/sofi-technologies-sofi-price-prediction-and-forecast-2025-2030/ (T3) |

計算(コンセンサス中央値に対する $14.55 の倍率): 2026 = 14.55 ÷ 0.60 = 24.3x、2027 = 14.55 ÷ 0.83 = 17.5x、2028 = 14.55 ÷ 1.08 = 13.5x、2029 = 14.55 ÷ 1.32 = 11.0x。
計算(成長率): 2028→2029 = 1.32 ÷ 1.08 − 1 = +22.2%(Seeking Alpha 28.8%、Stockalarm 30.4%と一致しない。§6)。

### 3-2. 四半期EPS・売上

| 四半期 | EPS予想 | 売上予想 | 出所 |
|---|---|---|---|
| Q3 2026(10/27発表) | **$0.17** | $1.26B(Benzinga英語版)/ $1.25B(韓国語版)。R1: $1.25〜1.278B | Benzinga https://www.benzinga.com/quote/SOFI/earnings-forecasts (T3) |
| Q4 2026 | **$0.19** | 未取得 | 同上。検算: 0.12 + 0.12 + 0.17 + 0.19 = 0.60(計算。会社ガイダンス約0.60と一致) |
| Q1 2027 | $0.18 | 未取得 | 同上 |
| Q2 2027 | $0.20 | 未取得 | 同上 |
| 実績 Q2 2026 | $0.12(予想$0.11)。調整後純収益 約$1.21B(+40%)、Zacks予想 $1.11B | - | TradingView News/Zacks |

### 3-3. 会社ガイダンスの前提(Q2 2026決算、2026-07-29)

| 項目 | 値 | 出所 |
|---|---|---|
| 調整後純収益 | $4.75〜4.85B(+32〜35%) | R1、TradingView News/Zacks |
| 調整後EPS | 約$0.60(据置) | 同上 |
| 調整後EBITDA | 約$1.6B(マージン33〜34%) | 同上 |
| 調整後純利益 | 約$825M | 同上 |
| **実効税率** | **約22%(当初ガイダンス比 約+700bp)** | TradingView News(Zacks系)の要約。T3、8-Kで要確認 |
| **金利前提** | **2026年中に利上げ1〜2回(年初は利下げ2回を前提)** | 同上。T3、8-Kで要確認 |
| 中期 | 2025〜2028 調整後純収益 CAGR 30%超、EPS CAGR 38〜42% | R1(SEC 8-K) |
| (古い・矛盾) | 「2026年EPS $0.68(中央値)、以後 CAGR 20〜25%」とする記事が複数あり | 検索要約。現行ガイダンス($0.60、38〜42%)と矛盾するため旧ガイダンス(2025年)と判断、採用せず |

---

## 4. SOFI の過去のPER・P/TBV

### 4-1. P/TBV

| 時点 | 値 | 出所・Tier |
|---|---|---|
| 2026-10-16 | 1.98x(計算: 14.55 ÷ TBVPS $7.34) | R1、SEC 8-K Q2 2026(T1+計算) |
| 2026-09-29 | **2.18x** | TIKR https://www.tikr.com/blog/what-would-have-to-go-right-for-sofi-to-earn-20-to-30-returns-heres-the-answer (T3) |
| 2026-08-06 | 2.79x(TBVPS 6.99と記載。8-K値$7.34と不整合) | Eulerpool https://eulerpool.com/stock/SoFi-Technologies-Stock-US83406F1021/ptbv (T3) |
| 2026-07-30頃 | 約2倍。TBVPS $7.34(前年$4.72) | Motley Fool/Nasdaq https://www.fool.com/investing/2026/07/30/sofis-tangible-book-value-grew-80-in-a-year-yet-th/ |
| 2025-09-30 | **5.65x** | TIKR(同上) |
| 2025-08頃 | 5.11x(Eulerpoolの「前年」) | Eulerpool |
| 過去7年(〜2025-04) | 最高 4.33、最低 1.44、中央値 3.36 | GuruFocus https://gurufocus.com/term/price-to-tangible-book/SOFI (T3)。**この「最高4.33」は2025-09の5.65xより低く、7年の窓が2025-04時点のもの** |
| TBVPS 推移 | 2023末 $3.61 → 2024末 $4.47 → 2025-06-30 $4.72 → 2026-06-30 $7.34 | SEC 8-K Q4 2024(https://www.sec.gov/Archives/edgar/data/1818874/000181887425000006/q42024earningsrelease.htm)、R1 (T1) |

### 4-2. P/B(年末)

| 年末 | P/B | 出所 |
|---|---|---|
| 2022 | 0.8x | Ticker League https://tickerleague.com/companies/SOFI/financials/pb-ratio (T3) |
| 2023 | 1.7x | 同上 |
| 2024 | 2.6x | 同上 |
| 2025 | 3.1x | 同上 |
| 2026-10-16 | 1.70x(計算) | R1 |

### 4-3. PER(スナップショットのみ。過去3〜5年のレンジ表は取れなかった)

| 時点 | forward P/E | 出所 |
|---|---|---|
| 2025-10-28/29 | 28.83(trailing 38.66) | MarketBeat https://www.marketbeat.com/instant-alerts/sofi-technologies-nasdaqsofi-trading-down-24-time-to-sell-2025-10-29/ |
| 2026-03 | 29.40(R1: StockAnalysis ratios) | R1 |
| 2026-07中旬 | 21.54(trailing 38.79) | StockHub https://www.stockhub.kr/en/stock/SOFI |
| 2026-07末 | 21.59(R1: StockAnalysis統計) | R1 |
| 2026-08-04 | 51.35(Eulerpool。他と大きく乖離、定義不明) | https://eulerpool.com/stock/SoFi-Technologies-Stock-US83406F1021/forwardpe |
| 2026-10-16 | 23.9〜24.7(今期)/ 17.3〜17.7(来期)(計算、R1) | R1 |
| Zacks記事内のSOFI forward P/E | 24.15x(業界16.46x)、26.6x、28.8x、34x、42x(業界22.5x)。記事日付は不明 | Zacks/Nasdaq記事(検索要約) |

YCharts の SOFI forward P/E ページ(https://ycharts.com/companies/SOFI/forward_pe_ratio)は5年の最高・最低・平均の欄があるが値が要約に出なかった。

---

## 5. 株価が織り込む前提を扱った資料(R2_market.md の§6にないもの)

| 資料 | 内容 | 基準 | 出所・Tier |
|---|---|---|---|
| TIKR「What Would Have to Go Right for SoFi to Earn 20% to 30% Returns?」 | SOFI の trailing ROE 7.1%、会社目標 ROTCE 20〜30%。ROTCE は ROE より高めに出る(ROEは総簿価)。収益/有形自己資本 約0.5倍 × ガイダンス上のマージン約17% → ROTCE 約8〜9%と自己推計。P/TBV 5.65x(2025-09-30)→ 2.18x(2026-09-29) | 2026-09-29 | https://www.tikr.com/blog/what-would-have-to-go-right-for-sofi-to-earn-20-to-30-returns-heres-the-answer (T3) |
| Morgan Stanley(Jeffrey Adelson)、TipRanks経由 | 当時の株価は ROTCE 30%超を織り込む、2026年E で 15% が現実的、とする見解(**2024年の古い資料**)。MSは現在 Underweight、目標$15(R1) | 2024 | https://www.tipranks.com/news/article/sofi-stock-why-morgan-stanley-says-its-time-to-sell (T3) |
| Ticker League リバースDCF | 株価 $17.07、割引率15%、永久成長率2.5%で、織り込みFCF成長 年65.5%。FCFは銀行モデルに不向き、株価も陳腐 | 不明(株価$17.07) | https://tickerleague.com/companies/SOFI/fair-value (T3) |
| 銀行の P/TBV と ROTCE の関係 | ROTCE が資本コスト(10〜12%)を上回る銀行は P/TBV プレミアム、下回ると割引。ポスト金融危機の P/TBV 低下の大半は ROTCE 低下で説明できる(Treasury系の旧リサーチノート)。**実データの回帰は見つからず**。IB面接ガイドの例式 P/TBV = 0.10 × ROTCE − 0.20 は説明用で実データではない | - | https://ibinterviewquestions.com/guides/fig-investment-banking/roe-ptbv-regression-fair-value-analysis (T4) |
| JPM の ROTCE と P/TBV | simianx「JPMorgan Stock 2026: 23% ROTCE vs a 3.2x Book Premium」: $359 で P/TBV 3.17x、Q2調整後ROTCE 23% | 2026-08 | https://www.simianx.ai/stories/jpmorgan-stock-2026-earnings-growth-valuation-and-risks (T4、AI系ページ) |

---

## 6. 取れなかった項目

1. **TradingView の SOFI forecast ページ**(年度別EPS・売上の平均/最高/最低/人数、2026〜2030年): 検索で本文が出ず。TradingView News の記事のみ。
2. **2030年のEPS・売上コンセンサス**。2029年も Tickflow の1行のみで列見出し未確認。
3. **KBW Bank Index(BKX)の予想PER・P/TBV(2026-10)**: KBWBのトレーリングP/E(7/31)、Mercerの地域別P/TBV(8月)、KRXの予想PER(年初)しか取れず。
4. **SOFIの過去3〜5年の PER レンジ(平均・最高・最低)**: スナップショットのみ。YCharts/GuruFocus の履歴表は値が出ず。
5. **ピア全社の同日・同一出典の表**: StockAnalysis/Finviz の当日値は検索で出ず。基準日は 10/8〜10/17 と 8月が混在。LC の10月株価、HOOD・NU・CHYM・UPST の今期/来期コンセンサスEPS、NU/HOOD/CHYM の予想成長率(3〜5年)も未取得。
6. **COF**: 2026年の TBVPS・ROTCE(Q2 8-K に載るはずだが要約に出ず)、Q3発表日。**AXP**: 現行ROE・P/B(取れたのは653日前の古いページ)。**ALLY**: TBVPS・core ROTCE(Q3は10/20発表で未出)。**SLM**: TBVPS。**NU**: 現行の TBV。**CHYM**: 簿価。
7. **FactSet 10/9版・10/16版の CY2026・CY2027 EPS成長率**(取れたのは発行日不明の 32.4% と約100日前の 17.4%)。
8. **「P/TBV と ROTCE から逆算した織り込み成長」を実データで示した資料**(§5のとおり存在せず)。
9. SOFI のガイダンスの実効税率22%・利上げ前提の8-K一次確認。

## 7. 出典間の食い違い

| 項目 | 食い違い |
|---|---|
| S&P 500 forward P/E(10月) | 19.0(FactSet 10/2版、10/16版)/ 19.1(10/9版と書く要約)/ 20.0(MercoPress 10/12、FactSet 8月版の値) |
| S&P 500 の5年平均・10年平均 | 5年: 19.8(10月版)/ 19.9(3月・6月・8月版)。10年: 19.1(10月版)/ 19.0(6月・8月版)/ 18.9(3月版) |
| SOFI P/TBV | 1.98x(計算、10/16)/ 2.18x(TIKR 9/29)/ 2.79x(Eulerpool 8/6、TBVPS 6.99)。Eulerpool の TBVPS は 8-K の $7.34 と不整合 |
| SOFI forward P/E | 21.5(StockHub)/ 21.59(StockAnalysis)/ 28.83(2025-10)/ 51.35(Eulerpool 8/4)/ 24.15〜42(Zacks各記事) |
| SOFI FY2029 EPS | 1.32(Tickflow、列見出し未確認)/ Seeking Alpha 成長28.8%・Stockalarm 成長30.4%を FY2028 EPS 1.08 に掛けると約1.39〜1.41(計算)/ VCP独自モデル 0.78 / 24/7 の2025年表 1.02 |
| SOFI 売上 | FY2027: $5.75B(Simply Wall St)/ $5.9B / $6.1〜6.16B(R1各社)。FY2028: $7.04B / $7.1B / $7.58B |
| SOFI 旧ガイダンス | 「2026年 EPS $0.68、以後CAGR 20〜25%」(複数記事)vs 現行「約$0.60、2028までCAGR 38〜42%」。旧ガイダンスと判断 |
| COF のトレーリングP/E | 9.92(10/17)/ 9.70(10/16)/ 12.25(10/14)。MarketBeat内で日ごとに変動、定義が動いている |
| COF の予想PER | Yahoo 10.82(6/30)/ Dividend.com 9.24(8/19、FY1)/ ValueInvesting 8.77(日付不明)/ 計算 8.45 |
| ALLY | 株価 $37.45〜37.63(MarketBeat 10月)vs $43.73(Earnings Whispers、日付不明)。forward P/E 6.55(Yahoo 6/30)vs 8.30(Yahoo別ページ)。Q3予想 $1.35(Benzinga)vs $1.43(Earnings Whispers)。当期EPS 5.05(10/9)vs 5.16(10/7) |
| NU の forward P/E | 15.99〜16.29(StockAnalysis)/ 11.6(Walnut Invest 7月)。ROE: 26.65% / 30.05%(StockAnalysis)/ 33%(会社Q2)/ 約56%(roic.ai、不自然) |
| HOOD | StockAnalysis内で $119.40(統計ページ)と $98.87(株価ページ)が併存。MarketBeat は $109.22(10/13)。PEG 2.67 / 2.13 |
| CHYM | forward P/E 13.22($21.68時点)vs 43.48($33.15時点)。時価総額 $8.26B(古い)vs $10.57B(10/8) |
| UPST | forward P/E 33.67(Yahoo)vs MarketScreener 2026年 44.8x・2027年 16.5x(価格$6.38と記載で不整合)。EPS: SA 2.27 / TIKR 約2 / VCP独自モデル 0.92 |
| SLM | Q3発表日 10/22(MarketBeat)vs 10/26(Earnings Whispers)。Q3 EPS予想 $0.17 vs $0.40。ROE 33.81% / 31.16% / 0.28 |
| JPM | Q3 EPS予想: $5.85(LSEG)/ $5.90 / $5.92。トレーリングP/E 14.25(決算前の記事)。P/TBV: 約2.98x(計算、$336)/ 3.17x(simianx 8月、$359)/ 約2.6x(FIG学習サイト、年初) |
| KBWB | トレーリングP/E 15.78(StockAnalysis 7/31)vs 13.06(GuruFocus、日付不明) |
| LC の ROTCE | 11.9%(2025Q4)vs 14.5%(2026Q1と報じる独語記事、期間不明) |
