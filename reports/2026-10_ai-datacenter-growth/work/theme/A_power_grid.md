# 投資テーマ・スクリーニング調査メモ A群(電力・グリッド系)

- 作成日: 2026-10-11 / 作成者: アナリスト補佐(判断材料の収集のみ。投資判断は行っていない)
- 対象: A1 グリッド機器 / A2 オンサイト発電+蓄電(BESS) / A3 原子力燃料サイクル・SMR・原子力サービス

---

## 0. 読む前に(データ取得の限界と記号の凡例)

### 0-1. 取得の限界(重要)
1. **WebFetch/curl は遮断**、WebSearch のみ使用。WebSearch は「ページ本文」ではなく**要約文+URL一覧**を返す仕様のため、本メモの数値は**検索結果の要約に書かれていた値**であり、リンク先の本文は一度も開いていない。要約者による転記ミス・取り違えの可能性がある。数値の採用前に一次資料(SEC 8-K/10-Q、会社IR、TDnet)での照合を推奨する。
2. **WebSearch の呼び出し上限(1ターン200回、全エージェント共有)に到達**し、A2の後半とA3の大半(Bloom/Caterpillar/Generac/三菱重工の追加調査、A3全銘柄の株価・時価総額・PER、ETF)が**未取得**。未取得は「未取得」と明記し、推測で埋めていない。追加調査が必要なら、上限引き上げ(`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`)またはフォローアップ指示が必要。
3. 株価・PER・時価総額は**取得日がバラバラ**(6月末〜10月8日)。必ず表の「時点」列を見ること。年初来(YTD)騰落率は多くの銘柄で**起点価格が取れず算出不可**。
4. 「訓練知識・未検証」と書いた箇所は検索で確認していない(本籍・事業構成比の目安など)。

### 0-2. 信頼度記号
- ★ = 企業の一次開示(SEC/TDnet/IRプレス)または公的機関・業界団体 / ☆ = 大手メディア・調査会社の報道(二次) / ▲ = ブログ、アグリゲータ、販促色の強い記事、日付不明(参考程度)
- 「(計算)」= 私が検索結果の数値から算出した値。「(推定)」= 根拠の薄い目安。

### 0-3. 本籍ゲートの扱い
- ゲート内 = 日本または米国に本籍かつ主上場。**本籍は検索で確認しておらず「訓練知識・未検証」**。米国上場でも他国本籍の可能性がある銘柄は「ゲート外の疑い」として別欄に置いた(例: Eaton)。

---

# A1. グリッド機器(送配電・変圧器・開閉装置・高圧ケーブル)

## A1-1. 需要の強烈さの証拠

### 受注残・受注(企業開示ベース)
| 企業 | 指標 | 数値 | 時点/公表日 | 出所 | 信頼度 |
|---|---|---|---|---|---|
| GE Vernova (電化セグメント) | 受注 | $6.3B、有機+66%、受注/売上 約1.7倍 | 2026年4-6月期 / 2026-07-22 | [GEV プレスリリース](https://www.gevernova.com/news/press-releases/ge-vernova-reports-second-quarter-2026-financial-results-raises-2026-financial) / [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000147/gevpressrelease2q26.htm) | ★(要約経由) |
| 同上 | 設備受注残 | $40.6B(前年比+$16.6B、+69%)。**うち約$5BはProlec GE買収分** | 同上 | 同上 | ★(要約経由) |
| 同上 | 電化セグメント売上 | $3.6B、+68%(有機では+29%。買収効果が大きい) | 同上 | 同上 | ★(要約経由) |
| GE Vernova 全社 | 受注残 | 約$176B、四半期で+$13.0B。全社受注$24.2B(有機+88%) | 同上 | [Pulse2.0](https://pulse2.com/ge-vernova-backlog-reaches-176-billion-as-power-and-electrification-demand-accelerates/) | ☆ |
| Eaton 電気Americas | 受注残 | $14,459M(前年比+44%)、受注/売上1.2 | 2026-03-31 / 10-Q | [SEC 10-Q](https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000013/etn-20260331.htm) | ★ |
| Eaton 2026年4-6月期 | 全社売上 | 約$8.5B、+21%(有機+14%)、調整後EPS $3.15。Americas受注/売上1.3(全社1.2)。Americas営業利益率27.5% | 2026-07-31 | [MarketBeat 決算要約](https://www.marketbeat.com/instant-alerts/eaton-q2-earnings-call-highlights-2026-07-31/) / [SEC 8-K Ex.99](https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000027/etn06302026exhibit99.htm) | ☆/★ |
| Eaton Electrical Global | 受注残 | 前年比+103%(**買収を含む**) | 同上 | 同上 | ☆ |
| Eaton 通期ガイダンス | 有機成長 | 11〜13%、調整後EPS $13.40〜13.60(中央値を+$0.22引き上げ) | 2026-07-31 | [MarketBeat](https://www.marketbeat.com/instant-alerts/eaton-nyseetn-updates-fy-2026-earnings-guidance-2026-07-31/) | ☆ |
| Vertiv | 受注残 | $15.0B(+109%)、受注/売上 約2.9倍 | **2025年10-12月期**(最新の受注系開示は取得できず) / 2026-02-11 | [SEC 8-K](https://www.sec.gov/Archives/edgar/data/1674101/000167410126000006/exhibit991vrt02112026.htm) | ★ |
| Vertiv 2026年4-6月期 | 売上 | $3.274B、+24%(有機+18%)、調整後営業利益率22.6%。**一部売上が期ずれ(複数フェーズ案件の進行、供給網の一時的混雑)**。通期売上ガイダンス約$14B(別記事は$13.75B=不一致) | 2026-07-29頃 | [Trefis 2026-09-30](https://www.trefis.com/articles/617134/should-you-think-about-vertiv-differently-now/2026-09-30) | ▲ |
| Hubbell | 売上 | $1.712B、+15%(有機+10%、買収+5pt)。送配電系(Grid Infrastructure)約+12%、Grid Automation 約+1%。**受注残の金額は取得できず**(経営陣は「受注は好調」と発言) | 2026-07-28 | [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0000048898/000162828026049934/exhibit991_07282026.htm) / [Nasdaq 要約](https://www.nasdaq.com/articles/hubbell-q2-earnings-call-highlights) | ★/☆ |
| Quanta Services | 受注残 | 過去最高 約$53.4B(うちRPO $33.6B)。売上$9.56B(+41%)、調整後EPS $4.24。通期ガイダンス売上$39.3〜39.7B、調整後EPS $16.45〜16.95。買収寄与は小さく有機中心 | 2026年4-6月期 / 2026-07-30 | [Quanta 決算サマリーPDF](https://investors.quantaservices.com/_assets/_9546050958577210325d4e87129a40ac/quantaservices/db/917/10536/operational_and_financial_commentary/PWR+06-30-2026+ER+Operational+and+Financial+Summary+vF.pdf) / [MarketBeat](https://www.marketbeat.com/instant-alerts/quanta-services-q2-earnings-call-highlights-2026-07-31/) | ★/☆ |
| Powell Industries | 受注残 | $2.4B(前年比+69%、前四半期比+35%=$1.8B→$2.4B)。受注$934.2M(+158%)、受注/売上3.0倍。**$400M超のデータセンター案件1件**を含む | 2026-06-30期(FQ3) / 2026-08-04頃 | [SEC 10-Q](https://www.sec.gov/Archives/edgar/data/0000080420/000008042026000107/powl-20260630.htm) / [MarketBeat](https://www.marketbeat.com/instant-alerts/powell-industries-q3-earnings-call-highlights-2026-08-04/) | ★/☆ |
| 日立製作所 全社 | 売上収益 | 2兆7,095億円(+20%)、調整後EBITA 3,235億円。4セクター全てが二桁成長、エネルギーとAXが牽引、通期予想を引き上げ。**エナジー単独の受注残は取得できず** | 2026年4-6月期 / 2026-07-29 | [マイナビニュース](https://news.mynavi.jp/techplus/article/20260729-4754214/) | ☆ |
| 日立エナジー(参考) | 受注残 | 世界受注残 約$43B(3年前は約$14B)との二次記事あり。**単一の調査ブログ由来で要照合** | 2026年初頭 | [調査ブログ](https://www.jaredwatkins.com/research/datacenters/power-infrastructure/hitachi-energy/) | ▲ |
| 日立エナジーインディア(上場子会社) | 受注残 | 3,222.2億ルピー(32,222 crore)、過去最高、データセンター向けが寄与 | 2026-06-30 | [TND India](https://www.tndindia.com/highest-ever-order-backlog-for-hitachi-energy-india/) | ☆ |
| Siemens Energy(参考) | 受注・受注残 | 受注 約€17.9B、受注残 過去最高 €162B、売上+17.5%(€11.45B)。Grid Technologiesが売上・受注の伸びを牽引(同部門の受注残は取得できず) | 2026年4-6月期 | [Blockspace](https://blockspace.media/insight/siemens-energy-q3-earnings-record-orders-2026/) / [Turbomachinery Mag 2026-08-06](https://www.turbomachinerymag.com/view/siemens-energy-posts-record-backlog-joining-ge-vernova-and-baker-hughes-in-a-record-quarter-for-gas-turbines) | ☆ |

### 日本の電線・電機(受注残は未取得、決算の伸びで代替)
| 企業 | 内容 | 公表日 | 出所 |
|---|---|---|---|
| フジクラ(5803) | 2027年3月期1Q 売上4,020億円(+50.1%)、営業利益1,048億円(+155.1%)、純利益804億円(+156.8%)。通期予想を6月→8月に連続引き上げ(売上1兆4,620億→1兆7,550億円、営業利益3,100億→4,320億円)。要因は情報通信(ハイパースケーラー向け光部品、売価上昇) | 2026-08-07 | [Monex スカウター](https://scouter.monex.co.jp/news/detail/5803_20260807_act_20260807_140039_2) / [EDINET DB](https://edinetdb.jp/company/E01334/earnings/FY2027-Q1) ☆ |
| 古河電工(5801) | 同1Q 売上3,652億円(+24.3%)、営業利益254億円(3.1倍)、純利益222億円(4.4倍)。通期予想を売上1兆4,600→1兆5,300億円、営業利益950→1,230億円に引き上げ。光ソリューション・情報コンポーネントが牽引。DC冷却機器に550億円投資(2026-04発表) | 2026-08-06 | [EDINET DB](https://edinetdb.jp/company/E01332/earnings/FY2027-Q1) / [Monex(投資メディア)](https://media.monex.co.jp/articles/-/25815) ☆ |
| 住友電工(5802) | ドイツ送電事業者向け大型案件 約3,600億円(同社過去最大と報道)。通期経常利益予想4,600億円(+6.7%) | 2026-05〜08 | [Monex スカウター](https://scouter.monex.co.jp/report/index/5802) / [Business Insider JP](https://www.businessinsider.jp/article/2606-major-three-wire-companies-stocks-buy-now/) ☆(3,600億円の個別記事URLは特定不可) |
| 三菱電機(6503) | 2027年3月期1Q 売上1兆4,971億円(前年同期比+1,842億円=+14.0%(計算))、営業利益1,395億円(+24.6%)、調整後営業利益1,443億円(前年938億円)。通期見通しを売上6兆2,700億円、調整後営業利益6,200億円に上方修正。**電力システム/変圧器・開閉装置の内訳は取得できず** | 2026-07-31 | [三菱電機 決算PDF](https://www.mitsubishielectric.co.jp/investors/data/management-report/pdf/financial-result/20260731.pdf) ★ |
| 明電舎(6508) | 1Q 売上734億円(+25.7%)、営業利益3億→46億円。電力インフラ(米国需要、インドの大型案件)が牽引。通期経常利益予想335億円(+20.1%)。FY2025(2026/3期)受注3,582億円、FY2026計画3,750億円 | 2026-07-31 | [Yahoo!ファイナンス](https://finance.yahoo.co.jp/quote/6508.T/financials) / [EDINET DB](https://edinetdb.jp/company/E01744/earnings/FY2027-Q1) ☆ |
| 東光高岳(6617) | 1Q 売上252.9億円(+9.5%)、通期売上予想1,150億円 | 2026-07〜08頃 | [asset-alive 他](https://www.asset-alive.com/thema/thema.php?tid=376) ▲(個別ページ特定不可) |

### リードタイム(週・年)
| 項目 | 数値 | 時点 | 出所 | 信頼度 |
|---|---|---|---|---|
| 米国 電力用変圧器 平均リードタイム | 128週。発電所昇圧用(GSU)144週 | WoodMac 2025年Q2調査 | [pv magazine USA 2026-05-11](https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/) | ☆ |
| GSUリードタイム | 2026年1Q に160週超(2024年平均143週) | 2026年1Q | 同上(Boucher引用) | ☆ |
| 大型変圧器 欧米メーカー | 2〜3年(2019年の約2倍)。変圧器・高圧遮断器とも | 2026年5月末 | [Rystad via pv magazine USA 2026-06-08](https://pv-magazine-usa.com/2026/06/08/global-grid-capex-to-surpass-650-billion-in-2026-says-rystad-energy/) | ☆ |
| 大型変圧器(IEA調査) | 調達に最大4年。ケーブル2〜3年、直流ケーブルは5年超 | IEA 2025年報告 | [IEA](https://www.iea.org/news/rising-component-prices-and-supply-chain-pressures-are-hindering-the-development-of-transmission-grid-infrastructure) | ★ |
| 高圧変圧器・開閉装置 | 80〜100週(別資料では36か月) | 2026年 | [Bernstein/Tribune India](https://www.tribuneindia.com/news/business/data-center-pipeline-faces-construction-delays-cancellations-to-mount-through-2027-bernstein/) 他 | ☆/▲ |
| 配電用変圧器 | 30か月超(DOE)との記載 | 2026年 | [TED Magazine](https://tedmag.com/trump-administration-increases-tariffs-on-certain-transformers/) | ▲ |

### 価格改定・コスト
- 2019年比の価格上昇: 電力用変圧器+77%、GSU+45%(WoodMac)。[pv magazine USA 2026-05-11](https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/) ☆
- IEA: ケーブル価格は2019年比でほぼ2倍、電力用変圧器は約+75%。[IEA](https://www.iea.org/news/rising-component-prices-and-supply-chain-pressures-are-hindering-the-development-of-transmission-grid-infrastructure) ★(2025年報告)
- 関税: 非米国産の鉄鋼・アルミ部材に50%(2025-08発効)、銅50%(Section 232)。方向性鋼板(GOES)の関税で芯材コスト+20〜25%との推計(単一出所)。[CRS R48933 2026-04-23](https://www.everycrsreport.com/files/2026-04-23_R48933_7b9be639e3196e5282d3817519df9f1ed2778302.pdf) ★ / [Transformer Technology](https://transformer-technology.com/article-hub/the-broader-impact-of-tariffs-on-the-power-sector-and-beyond/) ▲
- データセンター建設コスト: 1MWあたり2023年比+20〜25%(Bernstein)。[Tribune India](https://www.tribuneindia.com/news/business/data-center-pipeline-faces-construction-delays-cancellations-to-mount-through-2027-bernstein/) ☆
- **Rystadは「リードタイムと価格は横ばい(stagnated)」とし、これ以上の価格上昇は見込まない**(欧州の50〜100MVA案件で$30,000〜35,000/MVA)。→ 弱気材料にも入れた。

### 供給能力の不足量
- 米国の電力用変圧器の不足率 約30%、配電用変圧器 約10%(2025年推計)。輸入比率は大型電力用変圧器で約80%、配電用で約50%。[pv magazine USA 2026-05-11](https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/) ☆(**2025年値**。2026年版の不足率は見つからず)
- 需要の伸び(2019年→2025年): GSU +274%、変電所用電力変圧器 +116%(WoodMac)。同上
- Goldman Sachs: 米国の新増設で国内変圧器能力は2027〜28年に+2〜4%にとどまる一方、需要は+9〜12%。米国の需給ギャップは約60%(2028年に57%へ縮小の見通しを撤回)との報告。[Tiger Brokers 転載](https://www.itiger.com/news/1112652422) ▲ / [datacentres.com 2026-08-07](https://www.datacentres.com/news/36-month-lead-times-turn-transformer-shortage-into-data-centre-site-selection-ki-slot3-2026-08-07) ▲

### 顧客の前払い・長期契約
- 検索では**前払い・長期契約の具体的数値は取得できず**(未取得)。Powell/GEVの大型データセンター案件(>$400M)や、GEVの天然ガス「スロット予約」(A2参照)は、顧客が製造枠を先押さえする動きの例。

## A1-2. 途上性

- **市場規模(送配電網投資)**: Rystadは2026年の世界グリッド設備投資が**$650B超**(2020年の2倍超、前年比+5%)。[pv magazine USA 2026-06-08](https://pv-magazine-usa.com/2026/06/08/global-grid-capex-to-surpass-650-billion-in-2026-says-rystad-energy/) ☆
  IEAの数字は定義が異なる: World Energy Investment 2026 経由で2026年に$550B([Hanwha 解説](https://www.hanwha.com/newsroom/news/feature-stories/whats-in-a-number-5-insights-from-the-ieas-world-energy-investment-2026-report.do) ▲)、Electricity 2026 経由で現在約$400B・2030年までに約+50%([NextMSC](https://www.nextmsc.com/blogs/power-transmission-market-surges-as-global-grid-investment-grows-nextmsc) ▲)。**IEA一次資料は未確認**。2030年の確定値は取得できず。
- **S字カーブの位置(私の見立て)**: 受注が供給能力を上回る「拡大の初〜中期」。根拠: 受注/売上が1.2〜3.0倍、リードタイムが2019年比約2倍、Goldmanは2027〜28年も供給増<需要増。ただしRystadは「ピークのリードタイムは今後12か月で緩和し得る」としており、見方は分かれる。
- **供給能力の増設計画と解消時期**:
  - Rystad: 世界の変圧器能力は2028年までに**+10%超**。2026〜2028年に拡張の波。ただし「価格・リードタイムへの影響は不確実」と留保。[Rystad Grid Equipment Market Outlook](https://www.rystadenergy.com/insights/grid-equipment-market-outlook) ☆
  - 個別投資(いずれも稼働は2027〜28年以降が中心): Hitachi Energy 米国で$1B超(サウスボストン新工場は2028年稼働)/Siemens Energy 米ノースカロライナ$421M/GEV ベトナム工場$200M(2028年生産開始)/Prolec GE $300M超/HD現代エレクトリック アラバマ(米国生産+30%目標)。[pv magazine USA 2026-05-11](https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/) / [Power Magazine](https://powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/) ☆(個別金額の出所ページは特定不確実)
  - 日立エナジー: 2027年までに$6B規模の製造能力投資、$9B超のコミット(うち変圧器$1.5B)。[S&P Global 2026-01-05](https://www.spglobal.com/energy/en/news-research/latest-news/electric-power/010526-interview-no-peak-demand-in-sight-for-booming-power-grid-demand-hitachi-energy-ceo) ☆
  - 日本勢: 明電舎 沼津の変圧器工場に160億円、能力約1.5倍(2028年度稼働目標)/ダイヘン 三重に大形変圧器の新工場、約100億円規模(2025-12発表)。[SBBIT 2026-08-31](https://www.sbbit.jp/article/st/186626) ☆
  - 北米の変圧器製造能力 2023年200GVA→2027年260GVA超(単一・信頼性低)。[Energy Solutions](https://energy-solutions.co/supply-chain/manufacturers/north-america-transformer-refinery-0149) ▲
- **解消時期**: 多数の資料が「新ラインは2027〜28年以降」「ピークは緩和しても構造的不均衡は数年続く」。Rystadのみ「12か月内にピーク緩和の可能性」。

## A1-3. 投資家の認知度

| 銘柄 | 株価/時点 | 過去1年・2026年初来 | 予想PER | EPS成長率・PEG概算 | アナリスト数/目標株価 | 出所 |
|---|---|---|---|---|---|---|
| GE Vernova (GEV) | 史上最高値$1,174.86(2026-06-30)→約$912(8/31、約-22%)→約$996(7/29頃、StockHub) | 年初来: 起点約$650から**約+40%(8/31、検索要約者の推計)**。7/2時点では+70.5%(ChartRow)。10月の値は未取得 | 複数の値: 76.9(4/24 Yahoo)、37.6(7/29)、**44.7(9/21 TIKR、12か月平均56.3)**、約47(InsiderMonkey、日付「10月」とあるが詳細不明) | 成長率未取得→PEG算出不可。**2026年1Qの純利益$4.75Bに買収益$4.5B(税引前)が含まれ、見かけの利益は過大**(TIKR) | 34社、目標平均$1,250(StockHub)。高$1,450/低$580(MarketBeat)。次回決算10/28予定 | [TIKR](https://www.tikr.com/blog/ge-vernova-hit-a-record-1175-at-63x-forward-earnings-heres-what-has-to-go-right-in-2026) / [StockHub](https://stockhub.kr/en/stock/GEV) / [MarketBeat](https://www.marketbeat.com/stocks/NYSE/GEV/price-target/) / [ChartRow](https://chartrow.com/quote/gev/returns) / [TIKR 3月](https://www.tikr.com/blog/ge-vernova-is-up-34-year-to-date-heres-where-the-stock-could-go-in-2026) ☆/▲ |
| Eaton (ETN) | 時価総額約$163B(Stockopedia)。7/31の決算発表日に+7.3% | 年初来 +24%(6/11)→+25.9%(7/2)→+32%(Zacks、日付不明)。10月値未取得 | 約24.5〜30.8(ソースで差)、25.72(NTM、Tradersunion) | 予想EPS成長+14.3%(Tradersunion)→PEG概算 約1.8〜2.2(計算: 25.7/14.3、30.8/14.3)。MarketBeatはPEG>2。EPS: 2026ガイダンス$13.40〜13.60、Zacks推計 2027年$15.69/2028年$17.70 | 20社(Strong Buy 2/Buy 14/Hold 4)、目標平均$423 | [Tradersunion](https://tradersunion.com/stocks/earnings/eaton/) / [Chartmill/Zacks](https://www.chartmill.com/news/external/33724/eaton-rallies-32-ytd-should-investors-bet-on-the-stock-now) / [TIKR](https://www.tikr.com/blog/eaton-stock-is-up-24-year-to-date-heres-the-path-to-596-by-2028) / [Stockopedia](https://www.stockopedia.com/share-prices/eaton-NYQ:ETN/) / [MarketBeat](https://www.marketbeat.com/instant-alerts/zacks-research-has-positive-estimate-for-eaton-q4-earnings-2026-07-31/) ☆ |
| Vertiv (VRT) | $253.62、時価総額$97.64B(2026-10-05 Google)。52週レンジ約$118〜$380(高値から約-33%) | 年初来: +61.1%(8/19時点)、別スナップ+95.4%(日付不明・価格$316と不整合)→**10月の年初来は算出不可** | トレーリング57.4(10/5)。フォワード 31.7〜42(日付・出所でバラバラ)。NTM EV/EBITDA 約38倍 | 成長率未取得 | 20社(19が Buy/Strong Buy、1 Hold)、目標平均$335.44(現値比+32%) | [Google Finance](https://www.google.com/finance/labs/quote/VRT:NYSE) / [Yahoo](https://finance.yahoo.com/quote/VRT/key-statistics) / [Equibles](https://equibles.com/stocks/VRT) ☆/▲ |
| Hubbell (HUBB) | 終値$460.72(9/4)、時価総額約$24.3B | 年初来未取得 | 約22.6(計算: $460.72÷ガイダンス中央値$20.40。出所の表示は20.49) | 2026年調整後EPSガイダンス$20.25〜20.55(旧$19.30〜19.85から引上げ)。前年比成長率は未取得→PEG算出不可 | 未取得 | [Yahoo](https://finance.yahoo.com/quote/HUBB/key-statistics) / [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0000048898/000162828026049934/exhibit991_07282026.htm) ☆/★ |
| Quanta Services (PWR) | 時価総額 約$94〜98B(夏) | 年初来+82.4%(5月時点)。1年で+64%(TIKR、日付不明)。52週高値$788.72 | フォワード 33.3(6/30 Yahoo。3/31は51.8)、40.0(StockHub)、46.5(Dividend.watch)。トレーリング74〜90 | 2026年調整後EPSガイダンス$16.45〜16.95。前年比成長率は未取得→PEG算出不可 | 未取得 | [TIKR](https://www.tikr.com/blog/quanta-services-pwr-stock-valuation-2026) / [Yahoo](https://finance.yahoo.com/quote/PWR/key-statistics) / [StockHub](https://www.stockhub.kr/en/stock/PWR) ☆ |
| Powell (POWL) | 時価総額$7.70B(2026-08-04) | 年初来+61.9%(3/20時点)。10月値未取得 | **フォワード32.3 > トレーリング20.0(8/4)**。同一出所内の比較では、フォワードEPSが直近実績より低い=EPS減少を織り込む(私の推論) | EPSは減少見込みのためPEGは意味を持たない | 未取得 | [Yahoo UK](https://uk.finance.yahoo.com/quote/POWL) / [Dividend.watch](https://dividend.watch/symbol/POWL-NASDAQ) ▲(出所間で時価総額に不整合あり) |
| 日立製作所 (6501) | 5,510円、時価総額24兆9,909億円(2026-10-01) | 7/24 4,850円→9/7 5,357円→10/1 5,510円。年初来は未取得 | 27.5(10/1)。会社予想EPS 200.7円 | 成長率未取得 | 目標株価平均6,433円(+16.5%) | [Monex スカウター](https://scouter.monex.co.jp/report/index/6501) / [株予報](https://kabuyoho.jp/reportTarget?bcode=6501) ☆ |
| 三菱電機 (6503) | 5,126円、時価総額10兆8,323億円(2026-09-18)。6/25は6,069円(同12兆8,250億円)→**約-15.5%(計算)** | 年初来未取得 | 21.2(9/18)。6/25は26.1 | 成長率未取得 | 未取得 | [Monex スカウター](https://scouter.monex.co.jp/report/disclose/6503?page=2) ☆ |
| フジクラ (5803) | 5,512円、時価総額9兆7,848億円(2026-10-08)。9/14終値4,834円→**約+14%(計算)**。4月に株式分割 | 年初来未取得(分割調整が必要) | **28.0**(日経)。会社予想EPS 196.9円。みんかぶの調整後PERは58.1(基準が異なる) | 通期純利益予想: 6月に1,560億→2,290億円へ引上げ(Reuters経由)。8月にさらに上方修正(経常4,530億円)。前年実績が未取得のため成長率・PEGは算出不可 | 目標平均7,352円(現値比約+33%(計算))、コンセンサス「買い」 | [Matsui](https://finance.matsui.co.jp/stock/5803/index) / [日経](https://www.nikkei.com/nkd/company/?scode=5803) / [みんかぶ](https://minkabu.jp/stock/5803/analyst_consensus) ☆ |
| 古河電工 (5801) | 3,826円、時価総額2兆7,037億円(2026-09-25)。6/26は時価総額3兆1,694億円 | 年初来未取得。7/1に株式分割 | **25.6**(9/25)。6/26は38.5(**約-33%のマルチプル圧縮**) | 経常利益予想1,430億円(+88.5%)→単年PEG概算 約0.29(計算: 25.6/88.5。**単年の急増益ベースで外挿には不適**) | 未取得 | [株予報](https://kabuyoho.jp/reportAnalyst?bcode=5801) / [Monex](https://scouter.monex.co.jp/report/index/5801) ☆ |
| 住友電工 (5802) | 2,180円、時価総額6兆9,232億円(2026-08-28)。7/15は2,532円(同8兆410億円)→**約-14%(計算)** | 年初来未取得。7/1に株式分割 | **20.0**(8/28)。7/15は24.7 | 経常利益予想4,600億円(+6.7%)→単年PEG概算 約3.0(計算: 20.0/6.7) | 目標平均3,623円(現値比+66%、8/28時点) | [株予報](https://kabuyoho.jp/reportTarget?bcode=5802) / [Monex](https://scouter.monex.co.jp/report/index/5802) ☆ |
| 明電舎 (6508) | 11,720円、時価総額5,336億円(2026-08-28) | 年初来未取得 | 21.3 | 経常利益予想335億円(+20.1%)→単年PEG概算 約1.06(計算: 21.3/20.1) | 未取得 | [Monex](https://scouter.monex.co.jp/report/index/6508) / [株予報](https://kabuyoho.jp/report?bcode=6508) ☆ |

### テーマETF
- **GRID**(First Trust NASDAQ Clean Edge Smart Grid Infrastructure ETF): 純資産 約$11.6〜11.7B(2026-07-31〜08-28)。3月末〜4月初は$7.4〜7.7B → 約5か月で5割増。年初来リターン+19.3%(8/28)、1年+26.2%(7/31)。6/19時点で年初来の純流入 約€3.9B。経費率0.56%。主要構成にEaton、Johnson Controls、Schneider、ABB、Quantaなど。[Yahoo](https://finance.yahoo.com/quote/GRID/holders/)(年の記載なし、2026年と推定) / [StockAnalysis](https://stockanalysis.com/stocks/grid/) / [Trackinsight](https://www.trackinsight.com/en/fund/XNMS:GRID) / [Robinhood](https://robinhood.com/us/en/stocks/GRID) ☆

### 報道での扱われ方
- 「AI電力トレードで持つべき銘柄」「EatonとGE VernovaがAI半導体株を上回る」といった強気記事が目立つ。[247WallSt 2026-05-19](https://247wallst.com/investing/2026/05/19/forget-vistra-one-quarter-of-orders-at-ge-vernova-exceeded-all-of-last-year-that-is-the-ai-power-trade-worth-owning/) / [TIKR](https://www.tikr.com/blog/eaton-ge-vernova-beat-ai-chip-stocks) ▲(販促色あり)
- 割高感への言及: 「Vertivは良質だが安くない」「GE Vernovaが最も高いマルチプル」「Eatonのデータセンター成長は株価に織り込まれつつある」。**「バブル」を明言する大手機関の警告は、今回の検索では見つからなかった**。[Nasdaq](https://www.nasdaq.com/articles/5-stocks-solving-ai-power-crisis) / [Kavout](https://www.kavout.com/market-lens/eaton-s-etn-data-center-boom-faces-a-valuation-ceiling-despite-raised-guidance) / [Seeking Alpha](https://seekingalpha.com/article/4935565-eatons-data-center-growth-is-increasingly-reflected-in-valuation) ▲
- 日本の電線株: 「AI銘柄として長期の実需はあるが、短期の値動きはベンチャー株並み」「3社とも株価高騰で株式分割」。[Monex 2026-05](https://media.monex.co.jp/articles/-/25815) / [Business Insider JP 2026-06](https://www.businessinsider.jp/article/2606-major-three-wire-companies-stocks-buy-now/) ☆
- **認知度の総合所見(私見)**: 米国のGEV/ETN/VRT/PWRは「十分に認知済み」(アナリスト20〜34社、ETF資金の急増、AUM 5か月で5割増)。日本の電線・電機は6〜9月に**マルチプルが縮小**(古河電工PER 38.5→25.6、住友電工 24.7→20.0、三菱電機 26.1→21.2)しており、一巡後の調整局面とも読める。

## A1-4. 代表銘柄表(日本・米国 本籍かつ主上場)

| 銘柄 | コード | 時価総額(時点) | 直近売上YoY | 純度(概算) | 予想PER | 備考 |
|---|---|---|---|---|---|---|
| GE Vernova | GEV (NYSE) | 約$264B(8/3)〜$280B(8/13) [Robinhood](https://robinhood.com/stocks/GEV) / [Google](https://www.google.com/finance/beta/quote/GEV:NYSE)。10月値未取得 | 電化セグメント+68%(有機+29%)。全社売上YoYは未取得 | 電化は全社の一部。全社売上が未取得で比率は未算出(推定: 2〜3割。訓練知識・未検証)。ガス・風力等と合算の複合企業 | 44.7(9/21) | 受注残$176B。A2(ガスタービン)にも該当 |
| Quanta Services | PWR (NYSE) | 約$94〜98B(夏) | +41%(2026Q2) | 電力インフラ工事が主(推定: 7〜8割。訓練知識・未検証)。**機器メーカーではなく施工会社** | 33.3(6/30)〜46.5 | 受注残$53.4B |
| Hubbell | HUBB (NYSE) | 約$24.3B(9/4) | +15%(有機+10%) | 送配電+電気機器(推定: ほぼ全量が電力・電気系だが、DC比率は1割前後と推定。訓練知識・未検証) | 約22.6(計算) | NSI買収(約$3B)でレバレッジ2.9倍 |
| Powell Industries | POWL (Nasdaq) | $7.70B(8/4) | +9%(FQ3) | 配電盤・電力制御設備が中心(推定: 8割超。訓練知識・未検証) | 32.3(8/4) | 受注残$2.4B、受注/売上3.0倍 |
| Vertiv | VRT (NYSE) | $97.64B(10/5) | +24%(2026Q2、有機+18%) | データセンター電力・冷却(DC比率は高い。推定: 大半。訓練知識・未検証)。グリッド機器というよりDC内部設備 | 31.7〜42 | 受注残$15.0B(2025Q4) |
| 日立製作所 | 6501 | 24兆9,909億円(10/1) | +20%(1Q) | エナジー事業は全社の2割前後(推定。訓練知識・未検証)。ITやモビリティなどを含む複合 | 27.5 | 日立エナジーの親 |
| 三菱電機 | 6503 | 10兆8,323億円(9/18) | +14.0%(1Q、計算) | 電力システムは1割台(推定。訓練知識・未検証) | 21.2 | FA・パワー半導体等が主力 |
| フジクラ | 5803 | 9兆7,848億円(10/8) | +50.1%(1Q) | **グリッド機器としては低い**。主力はDC向け光ファイバ・コネクタ等(情報通信)。A1の「電力ケーブル」純度は低く、隣接テーマ(AIDC光配線)の色が強い | 28.0 | 年初来未取得 |
| 古河電工 | 5801 | 2兆7,037億円(9/25) | +24.3%(1Q) | 光・情報部材が牽引、電力ケーブルは一部(純度 低〜中。推定) | 25.6 | 7/1分割 |
| 住友電工 | 5802 | 6兆9,232億円(8/28) | 1Q未取得 | 送電ケーブル(独TSO案件約3,600億円)等。全体では自動車用ワイヤハーネスが大きく、グリッド比率は1割前後(推定。訓練知識・未検証) | 20.0 | 7/1分割 |
| 明電舎 | 6508 | 5,336億円(8/28) | +25.7%(1Q) | 電力インフラが主力(推定: 5割超。訓練知識・未検証) | 21.3 | 中規模・変圧器増産 |
| ダイヘン | 6622 | 未取得 | 未取得 | 変圧器+溶接ロボット等(推定: 約5割。訓練知識・未検証) | 18.77(2026-08-25、[Traders Web](https://www.traders.co.jp/stocks/6622/)。株価欄の表記が不自然でデータ品質に疑義) | 大形変圧器新工場(約100億円) |
| 東光高岳 | 6617 | 未取得 | +9.5%(1Q) | 電力機器・計測が中心(推定: 高。訓練知識・未検証) | 12.46(日付不明、▲) | 出所はasset-alive等 |

### 参考(ゲート外: ADR・他国本籍)
| 銘柄 | 上場 | 理由・数値 |
|---|---|---|
| Eaton (ETN) | NYSE | 米国上場だが**本籍はアイルランドの可能性が高い(訓練知識・未検証)**。ゲート判定は上位アナリストで要確認。時価総額約$163B、フォワードPER 約25〜31、20社カバー(上表参照) |
| Hitachi Energy | 非上場(日立の事業) / Hitachi Energy India (インド上場) | インド子会社の受注残3,222.2億ルピー(2026-06-30) |
| Siemens Energy | 独 | 受注残€162B、受注€17.9B(2026年4-6月期) |
| Schneider Electric, ABB, Prysmian, HD現代エレクトリック等 | 欧・韓 | 今回は数値未取得(GRIDの主要構成銘柄にSchneider/ABBが含まれる点のみ確認) |

## A1-5. 弱気材料(出所つき)

1. **データセンター案件の遅延・中止**: Bernsteinは世界の計画容量の35〜40%が遅延・中止リスクで、中止は2027年にかけて加速すると推計。Sightline Climateは2026年稼働予定の大型DCの30〜50%が遅延見込み(電力制約、設備不足、地元反対)。[Tribune India](https://www.tribuneindia.com/news/business/data-center-pipeline-faces-construction-delays-cancellations-to-mount-through-2027-bernstein/) / [Latitude Media](https://www.latitudemedia.com/news/up-to-half-of-the-worlds-data-centers-may-be-delayed-this-year/) ☆
   - 反論: SemiAnalysisは「50%中止・遅延」は初期段階の案件に偏った数字で、北米ハイパースケーラー自社建設の年末予測は6か月で約1%しか動いていないと主張。[SemiAnalysis](https://newsletter.semianalysis.com/p/stop-saying-half-of-2026-us-datacenter) ☆。CFRAは「ハイパースケーラーに後退の兆しなし、AIインフラ支出は2026年に$1兆超のペース」。[CFRA](https://www.cfraresearch.com/insights/beyond-the-buildout-separating-winners-from-losers-in-ai-infrastructure/) ☆
2. **供給の増加で価格・納期の正常化**: Rystadは価格・リードタイムが横ばい、2028年までに世界能力+10%超、ピークのリードタイムは12か月内に緩和し得ると予想。[pv magazine USA 2026-06-08](https://pv-magazine-usa.com/2026/06/08/global-grid-capex-to-surpass-650-billion-in-2026-says-rystad-energy/) ☆
3. **中国メーカーの輸出急増**: 10MVA超の変圧器輸出が2026年1-2月に前年比+61%(2025年通年+52%)、対米は+182%(Goldman Sachs由来)。需給が緩んだ場合の価格競争要因。逆に「米国需要の取り込み余地」ともとれる。[Tiger Brokers 転載](https://www.itiger.com/news/1112652422) ▲ / [Longbridge](https://longbridge.com/en/news/280755616) ▲。過剰供給を示す直接証拠は見つからなかった。
4. **「不足は調達側の問題」という少数意見**: 一部ブローカーは真の不足ではなく調達の盲点が危機の原因と主張(Power Magazine)。[Power Magazine](https://powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/) ☆(記事全文は未確認)
5. **バリュエーション**: Vertiv NTM EV/EBITDA約38倍(Schneider/Legrandの2倍超)で、ハイパースケーラー数社への依存度が高い。GEVは最高水準のマルチプル、利益に買収益が混入。Quantaはトレーリング74〜90倍。[Nasdaq](https://www.nasdaq.com/articles/5-stocks-solving-ai-power-crisis) / [TIKR](https://www.tikr.com/blog/ge-vernova-hit-a-record-1175-at-63x-forward-earnings-heres-what-has-to-go-right-in-2026) ☆/▲
6. **執行リスク**: Vertivは2026Q2で売上の一部が期ずれ、フリーキャッシュフローが弱いとの記事。[ainvest](https://www.ainvest.com/news/vertiv-q2-read-stumble-free-cash-flow-2609/) ▲。Hubbellは約$3BのNSI買収でレバレッジ2.9倍。
7. **政策**: 銅・鉄鋼関税でコスト上昇。DOEがGOES関税の12か月免除を検討との情報(未確認、信頼性低)。[Energy Solutions](https://energy-solutions.co/supply-chain/manufacturers/north-america-transformer-refinery-0149) ▲
8. **株価面の調整**: 日本の電線・電機は6月〜9月に下落(古河電工PER 38.5→25.6、住友電工 時価総額-14%、三菱電機 -15.5%)。GEVも6/30高値から8/31まで約-22%。

---

# A2. データセンター向けオンサイト発電(燃料電池・ガスエンジン/小型タービン)と蓄電(BESS)

> **取得状況**: 検索上限により、Bloom Energyの時価総額・PER・年初来、Caterpillar/Generac/三菱重工/川崎重工/日本ガイシ、BESS各社の株価・PERが**未取得**。以下は取得できた範囲のみ。

## A2-1. 需要の強烈さの証拠

| 項目 | 数値 | 時点/公表日 | 出所 | 信頼度 |
|---|---|---|---|---|
| GE Vernova ガス発電 設備受注残+スロット予約 | 100GW→116GW(四半期で+16GW)。うち確定受注残44→53GW、スロット予約56→63GW。年末までに125GW以上を見込む。**スロット予約は確定発注ではない**ため合算を「確定受注」と呼ぶのは不適切との指摘あり | 2026-07-22 | [Turbomachinery Mag](https://www.turbomachinerymag.com/view/ge-vernova-gas-turbine-backlog-hits-116-gw-as-power-orders-more-than-double) / [GEV プレスリリース](https://www.gevernova.com/news/press-releases/ge-vernova-reports-second-quarter-2026-financial-results-raises-2026-financial) / [Yahoo/247WallSt](https://finance.yahoo.com/sectors/technology/articles/forget-vistra-one-quarter-orders-170524858.html) | ★/☆ |
| GEV ガスタービン生産能力 | 年20GW(2026年Q3到達見込み)→2028年に24GW | 2026-07 | 同上 | ☆ |
| ガスタービン納期 | 受注残が2031年まで伸びているとの記事(二次) | 2026年 | [CryptoBriefing](https://cryptobriefing.com/gas-turbine-shortage-ai-constraint/) | ▲ |
| Wärtsilä(ゲート外) | 米オハイオのハイパースケール案件で412MW受注(設備は2028年初稼働)。米国DC向けエンジン容量は4案件で1.6GW超 | 2026年 | [POWER Engineering](https://www.power-eng.com/gas/data-center-power-crunch-lifts-engines-aeroderivatives-into-larger-role/) | ☆ |
| Caterpillar | 発電事業売上 2026年1Qに+41%(前年比)、$2.8B。主因はデータセンター向け大型エンジン・タービン。全社受注残は記事で**$63B(Motley Fool)と$72B(MarketsandMarkets)で不一致** | 2026-08-03 記事 | [Motley Fool](https://www.fool.com/investing/2026/08/03/caterpillars-order-backlog-hit-a-record-63-billion/) / [MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/data-center-onsite-behind-the-meter-power-market-129738654.html) | ☆/▲ |
| Bloom Energy 2026年4-6月期 | 売上 約$1.065B(+166%)。通期売上ガイダンスを$3.9〜4.2B(中央値で前年比+100%)に引上げ。非GAAP営業利益$800〜900M、非GAAP EPS $2.55〜2.85。**受注残の金額は取得できず**(「売上より速く増加」との経営陣発言) | 2026-07-28頃(出所間で日付が不一致) | [Nasdaq 決算要約](https://www.nasdaq.com/articles/bloom-energy-q2-earnings-call-highlights) / [Quartr](https://quartr.com/events/bloom-energy-corporation-be-q2-2026_3sJo92bV) / [Trefis 2026-09-30](https://www.trefis.com/articles/617129/should-bloom-energy-stock-investors-worry-about-its-record-quarter/2026-09-30) | ☆ |
| Bloom 長期契約・枠 | 25GW分の展開可視性。Oracleと2.8GW契約(2026-04)、Brookfield提携は$5B→$25Bに拡大。**いずれも枠組み合意であり確定売上ではない**。ハイパースケーラー全社+数十社のネオクラウド等が採用承認済みと経営陣 | 2026年 | [Sentisense 2026-08-18](https://app.sentisense.ai/stories/bloom-energy-reports-record-q2-revenue-and-25-gw-deployment-visibility-08182026) / [Stocktwits](https://stocktwits.com/news-articles/markets/equity/why-bloom-energy-may-be-emerging-as-the-power-layer-behind-ai-boom-5-takeaways-from-its-record-quarter/cZNRZchRJRJ) | ▲ |
| Fluence(BESS) 2026年4-6月期(FQ3) | 受注$1.44B(前年同期$509Mの約3倍)、受注残 過去最高$6.4B(前四半期比+14%、前年比+30%超)。データセンター関連が7月までに約$850M(うちハイパースケーラーから約$550M、初の大型BTM案件含む) | 2026-08-06頃 | [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001868941/000186894126000028/flncq3fy26earningspressrel.htm) / [Energy-Storage.news](https://www.energy-storage.news/fluence-books-first-big-data-centre-deals-but-manufacturing-ramp-up-delays-hit-revenues/) / [GuruFocus](https://www.gurufocus.com/news/9014297/fluence-energy-inc-flnc-q3-2026-earnings-call-highlights-record-orders-and-backlog-amid-production-delays) | ★/☆ |
| Fluence 前四半期の受注残 | $5.6B | 2026-05-08 | [ESS News](https://www.ess-news.com/2026/05/08/fluence-reports-5-6-billion-order-backlog-as-battery-pipeline-swells/) | ☆ |
| 三菱重工(7011)(参考) | 2026年3月期 受注高 約7.65兆円、受注残13兆円超、最終利益3,321億円(投資情報サイトの記事)。ガスタービン・コンバインドサイクル(GTCC)を含むエナジーの受注を上方修正との報道 | 2026-05頃 | [Newswitch](https://newswitch.jp/p/47552) / [ko-invest](https://ko-invest.net/7040/) ▲(個別記事の特定不可。今年度1Qは未取得) | ▲ |

### 供給能力の不足量
- Morgan Stanley: AIデータセンターの電力不足は2028年まで38GWとの報道(二次、公表日不明)。[CryptoBriefing](https://cryptobriefing.com/morgan-stanley-ai-data-centers-38-gigawatt-power-gap/) / [KuCoin](https://www.kucoin.com/news/flash/morgan-stanley-reports-38-gigawatt-power-shortfall-for-ai-data-centers-by-2028) ▲
- Jefferies: 2030年までにBTM(需要地内)容量+25GW、ただし「最長10年続く橋渡し」にとどまる。[Manufacturing Dive](https://www.manufacturingdive.com/news/natural-gas-equipment-generation-bottleneck-data-centers/813087/) ☆
- 前払い・長期契約: Bloomの枠組み合意、GEVのスロット予約(上記)。Centrusのような前払いの数値は未取得。

## A2-2. 途上性

- **BESS(蓄電)市場**(BloombergNEF): 2025年の新設は112GW/307GWh(電力ベースで前年比+48%)。2026年予測は158GW/459GWh(+41%)。2036年に年間約306〜308GW(出所間で差)、累計2.9TW/10.5TWh。**2030年の個別予測値は取得できず**。[Energy-Storage.news](https://www.energy-storage.news/?p=100799) / [pv magazine USA 2026-05-11](https://pv-magazine-usa.com/2026/05/11/bloombergnef-confirms-energy-storage-has-reached-the-100-gw-era) / [Energy-Storage.news(予測引上げ)](https://www.energy-storage.news/?p=101781) ☆
  - 一次記事に「158MW」と書かれた誤記あり(正しくは158GW)。
  - **私の計算**: 2026年158GW→2036年308GWの年平均成長率は約+6.9%。2025〜26年の+41%から**成長率が大きく鈍化する前提**=S字の変曲点を過ぎた後の姿。BESS全体は「成長中期〜成熟への移行」、DC向けBTMは立ち上がり初期、と区別して見るのが妥当(私見)。
- **オンサイト発電**: 「橋渡し」需要(Jefferies)、エンジン・航空転用型タービンがグリッド待ち・大型タービン待ちの代替(POWER Engineering)。Bloomの25GWは確定ではなく可視性。
- **供給増設**: GEVのタービン年20GW→24GW(2028年)。Fluenceは新規委託製造工場の立ち上がり遅れ(下記)。Wärtsilä/Caterpillar等の増設計画は未取得。
- 解消時期: タービンは受注残が2031年まで(二次)、DC向けは2028年稼働の案件が中心(Wärtsilä)。

## A2-3. 投資家の認知度

- **取得できたもの**: Bloomの決算後の反応は**+6.08%と-13%で出所が食い違う**(「慎重な見通しとマージン圧力」の指摘あり)。[Longport](https://longportapp.cn/news/294144287) / [Sentisense](https://app.sentisense.ai/stories/bloom-energy-reports-record-q2-revenue-and-25-gw-deployment-visibility-08182026) ▲
- 株価・年初来・予想PER・アナリスト数・テーマETF: **Bloom、Fluence、Caterpillar、Generacとも未取得**(検索上限)。
- テーマETF(訓練知識・未検証): クリーンエネルギー/蓄電の汎用ETFは存在するが、DCオンサイト電源に特化したETFは確認していない。上位アナリストは別途確認のこと。
- 報道での扱われ方: Bloomを「AIブームの電力レイヤー」と位置づける記事あり([Stocktwits](https://stocktwits.com/news-articles/markets/equity/why-bloom-energy-may-be-emerging-as-the-power-layer-behind-ai-boom-5-takeaways-from-its-record-quarter/cZNRZchRJRJ) ▲)。「過熱」「バブル」の明言は未確認。

## A2-4. 代表銘柄表(日本・米国 本籍かつ主上場)

| 銘柄 | コード | 時価総額 | 直近売上YoY | 純度(概算) | 予想PER | 備考・出所 |
|---|---|---|---|---|---|---|
| Bloom Energy | BE (NYSE) | **未取得** | +166%(2026Q2、約$1.065B) | 高(燃料電池専業。DC向け比率は大きいが数値未取得。推定。訓練知識・未検証) | **未取得**(非GAAP EPS通期ガイダンス$2.55〜2.85) | [Nasdaq](https://www.nasdaq.com/articles/bloom-energy-q2-earnings-call-highlights) |
| Fluence Energy | FLNC (Nasdaq) | **未取得** | Q3売上$649.8M(前年比は未取得)。通期ガイダンスを$3.2〜3.6B→**$2.9〜3.1Bに引き下げ**。純損失$44.3M(前年は黒字$6.9M) | 高(BESS専業。DC向けは受注の一部) | 未取得 | [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001868941/000186894126000028/flncq3fy26earningspressrel.htm)。本籍は米国と推定(Siemens/AESが主要株主。訓練知識・未検証) |
| Caterpillar | CAT (NYSE) | 未取得 | 発電事業+41%(2026Q1) | **低**(建機・資源が主体。発電は一部) | 未取得 | [Motley Fool](https://www.fool.com/investing/2026/08/03/caterpillars-order-backlog-hit-a-record-63-billion/) |
| GE Vernova | GEV | A1参照 | A1参照 | ガス発電は全社の主要事業の一つ | A1参照 | 116GWの受注残+予約 |
| Generac | GNRC | **未調査** | 未調査 | 未調査 | 未調査 | 候補(訓練知識・未検証) |
| 三菱重工 | 7011 | 未取得 | 未取得 | 複合(ガスタービン、原子力、防衛等) | 未取得 | 受注残13兆円超(2026/3期、▲) |
| 川崎重工 | 7012 | **未調査** | 未調査 | 未調査 | 未調査 | ガスエンジン/ガスタービンの候補(訓練知識・未検証) |
| 日本ガイシ | 5333 | **未調査** | 未調査 | 未調査 | 未調査 | NAS蓄電池の候補(訓練知識・未検証) |
| Eos Energy / FuelCell Energy / EnerSys 等 | EOSE, FCEL, ENS | **未調査** | 未調査 | 未調査 | 未調査 | 候補(訓練知識・未検証) |

### 参考(ゲート外)
| 銘柄 | 理由 |
|---|---|
| Wärtsilä(フィンランド) | 412MW受注、DC向けエンジン容量1.6GW超 |
| Siemens Energy(ドイツ) | ガスタービン受注残が記録的([Turbomachinery Mag 2026-08-06](https://www.turbomachinerymag.com/view/siemens-energy-posts-record-backlog-joining-ge-vernova-and-baker-hughes-in-a-record-quarter-for-gas-turbines))。詳細未取得 |
| Baker Hughes(上場市場・本籍は未確認) | 上記記事の見出しで、GEV・Siemens Energyとともに「ガスタービンの記録的四半期」に言及。詳細未取得 |

## A2-5. 弱気材料(出所つき)

1. **計画の投機性**: データセンター電力要求の多くは投機的とのインサイダー警告。タービンメーカーは増設に慎重。[CRE Daily](https://www.credaily.com/briefs/gas-turbine-shortage-threatens-data-center-power-plans/) ▲
2. **BTMは「橋渡し」**: Jefferiesは+25GW(2030年)としつつ、最長10年の暫定手段と位置づけ。系統接続が改善すれば需要は剥落し得る。[Manufacturing Dive](https://www.manufacturingdive.com/news/natural-gas-equipment-generation-bottleneck-data-centers/813087/) ☆
3. **Fluenceの執行リスク**: 新規委託製造工場の生産トラブルと米国新工場の建設遅れで約$400Mの納入がFY2027にずれ込み、通期売上ガイダンスを下方修正。受注は絶好調でも売上・利益が遅れる典型。[Energy-Storage.news](https://www.energy-storage.news/fluence-books-first-big-data-centre-deals-but-manufacturing-ramp-up-delays-hit-revenues/) / [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001868941/000186894126000028/flncq3fy26earningspressrel.htm) ★/☆
4. **Bloom**: 枠組み合意(Oracle 2.8GW、Brookfield $25B)は確定売上ではない。決算後に慎重な見通し・マージン圧力で売られたとの報道(出所間で不一致)。[Trefis](https://www.trefis.com/articles/617129/should-bloom-energy-stock-investors-worry-about-its-record-quarter/2026-09-30) ▲
5. **BESSの成長鈍化**: BNEFの2036年予測から計算すると2026年以降の成長は年+7%程度(上記)。コモディティ化で価格は予想より速く低下(BNEF)。[Energy-Storage.news](https://www.energy-storage.news/?p=101781) ☆
6. **スロット予約の解釈**: GEVの116GWは確定受注残(53GW)と予約(63GW)の合算。[Yahoo/247WallSt](https://finance.yahoo.com/sectors/technology/articles/forget-vistra-one-quarter-orders-170524858.html) ☆
7. **DC建設の遅延**(A1-5と共通): 立ち上がりが遅れると、オンサイト電源の売上計上も後ずれ。

---

# A3. 原子力燃料サイクル(濃縮・HALEU)、SMR、原子力サービス

> **取得状況**: 検索上限により、A3の**時価総額・PER・ETF・アナリスト数・Centrus/BWXTの株価が未取得**。取得できたのは、Centrus/BWXTの決算、濃縮供給、WNA見通し、SMR銘柄の株価の動き。

## A3-1. 需要の強烈さの証拠

| 項目 | 数値 | 時点/公表日 | 出所 | 信頼度 |
|---|---|---|---|---|
| Centrus 総受注残 | $4.5B(2026-06-30)、2025年末は$3.8B(**6か月で約+18%(計算)**)。2040年まで | 2026-08-05 | [SEC 10-Q](https://www.sec.gov/Archives/edgar/data/0001065059/000162828026053863/leu-20260630.htm) / [SEC 8-K Ex.99](https://www.sec.gov/Archives/edgar/data/0001065059/000162828026053433/ex991-10q2026_08x05.htm) | ★ |
| Centrus LEU部門の受注残 | 約$3.7B。うち約$3.0Bは条件付きのLEU/HALEU契約(その$2.4Bは確定契約下)。**ピケトン拡張の建設が前提** | 同上 | [Barchart/StockStory](https://www.barchart.com/story/news/3717543/leu-q2-deep-dive-backlog-growth-and-expansion-plans-meet-margin-pressures) | ★/☆ |
| Centrus 売上 | $176.1M(前年同期$154.5M、+14.0%(計算))。LEU部門+22%($153.4M)、技術サービス-21%。営業利益率5.9%(前年21.7%)。通期売上ガイダンス$450〜500M | 同上 | [SEC 8-K Ex.99](https://www.sec.gov/Archives/edgar/data/0001065059/000162828026053433/ex991-10q2026_08x05.htm) / [MarketBeat](https://www.marketbeat.com/instant-alerts/centrus-energy-q2-earnings-call-highlights-2026-08-08/) | ★/☆ |
| Centrus HALEU | DOEから$900MのHALEU濃縮契約。大規模な商用HALEU供給契約(前払いの可能性)。ピケトン商業生産は2029年目標、オークリッジの新遠心分離機1号機は2026年末完了予定 | 同上 | 同上 | ★/☆ |
| BWXT 受注残 | $8.4B(前年比+40%)、直近12か月の受注/売上1.7倍 | 2026-08-03 | [BWXT IR](https://investors.bwxt.com/news-releases/news-release-details/bwx-technologies-reports-second-quarter-2026-results) / [Business Wire](https://www.businesswire.com/news/home/20260803655700/en/BWX-Technologies-Reports-Second-Quarter-2026-Results) | ★ |
| BWXT 業績 | 売上約$902M(+18%、有機+9%)。2026年ガイダンス: 売上約$3.8B、調整後EBITDA $662〜672M、非GAAP EPS $4.70〜4.80、FCF $345〜360M。商業事業の成長率見通し約45%(政府事業は1桁後半)。医療事業を最大$800Mで売却、Precision Components Group買収(7/1完了) | 同上 | 同上 | ★ |
| 西側の濃縮供給 | Urenco米ニューメキシコ増設700,000SWUは2027年までに完成、4つ目のカスケードが2026年3月末に稼働(予定より前倒し)。別途、2032〜36年に約2.1M SWU/年の増設計画(アグリゲータ情報) | 2026-03〜 | [Northern Miner](https://www.northernminer.com/news/breaking-the-wests-enrichment-bottleneck/1003890718/) / [Threatcluster](https://threatcluster.io/cluster/urenco-expands-us-enrichment-capacity-amid-russian-uranium-b-95b93dbb) | ☆/▲ |
| ロシア依存 | 世界の濃縮能力の約44%、転換の約20%がロシア(EIA/DOE引用)。ロシア産ウラン輸入禁止の免除権限は2028-01-01に失効 | 2024〜26年 | [Eco3min](https://eco3min.fr/uranium-enrichissement-swu-goulot-russe-chaine-occidentale/) / [Mining.com](https://www.mining.com/web/senate-passes-russian-uranium-import-ban-sending-to-biden/) | ☆ |
| 米国の濃縮需要 | 米商業炉の事業者が2024年に15M SWU分を購入 | 2024 | [Power Magazine](https://www.powermag.com/americas-only-commercial-uranium-enricher-is-privately-building-a-new-plant-amid-a-widening-nuclear-fuel-supply-gap/) | ☆ |
| SWU価格 | **2026年の現物価格は取得できず**。2024年時点の現物$165/SWU(UxC)のみ(古い) | 2024 | [Mining.com](https://www.mining.com/web/senate-passes-russian-uranium-import-ban-sending-to-biden/) | ☆(古い) |

- リードタイム・価格改定・前払い: Centrusの商用HALEU契約に前払いが含まれる可能性(上記)。SWU/UF6の2026年価格、新規炉の燃料リードタイムは**未取得**。
- 業界の見方の割れ: 2026年3月のCERAWeekで「在庫枯渇で2030年代初頭に不足」と「公益事業は長期契約で2030年まで確保済み」の二論が併存。[Northern Miner](https://www.northernminer.com/news/breaking-the-wests-enrichment-bottleneck/1003890718/) ☆

## A3-2. 途上性

- **世界の原子力容量見通し**(WNA World Nuclear Outlook 2026): 2050年に1,457GWe(前年版は1,428GWe)、建設中82GWe(76から増)、計画114GWe(107から増)。3倍化目標には現在の約6倍の建設ペースが必要。中国と米国で見通しの過半。[WNA 2026版](https://world-nuclear.org/our-association/publications/world-nuclear-outlook-report/world-nuclear-outlook-report-2026-full-document) / [WNA 2025版](https://world-nuclear.org/our-association/publications/global-trends-reports/world-nuclear-outlook-report) ★
- ウラン需要は2040年まで年平均+5.3%、鉱山供給は短期は十分だが2030年以降に不足の恐れ(アグリゲータ転載)。[finanzen.ch](https://adnz-oufeuofqus.finanzen.ch/nachrichten/rohstoffe/uranium-demand-for-nuclear-power-set-to-surge-nearly-30percent-by-2030-report-14802110) ▲
- **2030年の濃縮(SWU)需要見通し**: 取得できず(WNA燃料報告書の本文を開けなかった)。
- **S字カーブの位置(私見)**:
  - 燃料(濃縮・HALEU): 新設需要の立ち上がりは2030年前後以降。当面は既存炉+ロシア代替需要。**供給側が増設に動き出した初期**(Urenco 2027、Centrus 2029、ロシア免除失効2028)。
  - SMR(Oklo/NuScale/NANO): **収益化前**。NuScaleの2026年Q2売上は前年比-99.1%、NANO Nuclearの2026年Q2売上は約$21万(予想未達)。
  - 原子力サービス(BWXT): 政府(海軍炉)が土台で、商業事業が急成長(+45%見通し)。成熟事業+成長オプション。
- **供給能力の増設計画と解消時期**: Urenco NM(+700k SWU)=2027年、Centrusピケトン商業生産=2029年目標、Urenco追加(約2.1M SWU)=2032〜36年。免除失効の2028年と、追加能力の本格稼働(2030年代)の間にギャップあり。

## A3-3. 投資家の認知度

- **SMR関連の純粋銘柄は2026年に大幅下落**(認知度は高いが、センチメントは逆風):
  | 銘柄 | 数値 | 時点 | 出所 |
  |---|---|---|---|
  | Oklo | 年初来-42%(7月中旬)、1か月で-28%。9/8に$43.99。2025年10月の最高値$193から**約-77%(計算)**。別記事(日付不明)では年初来-46%超 | 2026-07-16 / 09-08 | [247WallSt 7/16](https://247wallst.com/investing/2026/07/16/oklo-just-dropped-28-in-a-month-is-it-time-to-abandon-nuclear-stocks-like-oklo-nuscale-and-uranium-energy-corp/) / [247WallSt 9/8](https://247wallst.com/investing/2026/09/08/nuscale-power-spikes-13-oklo-climbs-7-is-the-nuclear-selloff-finally-exhausted/) |
  | NuScale (SMR) | 年初来-24%(9/8、$10.94、当日+13%)。別記事で年初来-44%超(日付不明)。ENTRA1提携を巡る集団訴訟 | 2026-09-08 | 同上 / [Stocktwits](https://stocktwits.com/news-articles/markets/equity/oklo-vs-smr-vs-nne-all-three-nuclear-stocks-got-a-price-target-cut-but-here-s-the-one-this-analyst-still-favors/cZYBWT4RJZv) |
  | NANO Nuclear (NNE) | 年初来-33%超(日付不明) | 不明 | 同上 |
  - 3銘柄とも目標株価の引き下げ。リテールのセンチメントは「弱気」(Stocktwits)。収益性のある原子力電力会社(CEG、VST)は下落を免れた(247WallSt)。
- 報道: 「原子力株の売りは出尽くしたか」(247WallSt、9/8)。**「バブル」の語での言及は見つからず**、むしろ「投機的な炉開発者・ウラン鉱山が大きくデレーティング」という文脈。
- Centrus、BWXT: **株価・年初来・PER・アナリスト数は未取得**。
- テーマETF: 未取得。ウラン/原子力ETFは存在するはず(例: URA、NLR、NUKZ。訓練知識・未検証)。AUM・年初来は上位アナリストが確認のこと。
- 予想EPS成長・PEG: BWXTは2026年非GAAP EPSガイダンス$4.70〜4.80(前年比成長率・PERは未取得)。Centrusは営業利益率が低下(5.9%)。PEGは**算出不可**。

## A3-4. 代表銘柄表(日本・米国 本籍かつ主上場)

| 銘柄 | コード | 時価総額 | 直近売上YoY | 純度(概算) | 予想PER | 備考・出所 |
|---|---|---|---|---|---|---|
| Centrus Energy | LEU (NYSE American, 訓練知識・未検証) | **未取得** | +14.0%(2026Q2、計算) | 高(濃縮・HALEU・燃料供給。LEU部門が売上の約87%(計算: 153.4/176.1)) | **未取得** | 受注残$4.5B。[SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001065059/000162828026053433/ex991-10q2026_08x05.htm) |
| BWX Technologies | BWXT (NYSE) | **未取得** | +18%(2026Q2、有機+9%) | 中〜高(海軍炉は政府事業が主。商業原子力は成長中。比率は未取得) | **未取得**(非GAAP EPS $4.70〜4.80ガイダンス) | 受注残$8.4B。[BWXT IR](https://investors.bwxt.com/news-releases/news-release-details/bwx-technologies-reports-second-quarter-2026-results) |
| NuScale Power | SMR (NYSE) | 未取得 | 2026Q2売上が前年比約-99.1% | 100%(SMR) | 赤字のため意味なし | 収益化前。9/8 $10.94 |
| Oklo | OKLO (NYSE) | 未取得 | 売上なし(収益化前) | 100%(先進炉+燃料リサイクル構想) | 赤字 | 9/8 $43.99。現金$25億・無借金との記事と$2.75億との記事があり不一致 |
| NANO Nuclear Energy | NNE (Nasdaq) | 未取得 | 2026Q2売上 約$21万 | 100% | 赤字 | |
| 三菱重工 | 7011 | 未取得 | 未取得 | 複合(原子力は一部) | 未取得 | 原子力発電所向けポンプ34台受注等の報道。▲ |
| IHI | 7013 | 未取得 | 未取得 | 複合 | 未取得 | NuScale出資(訓練知識・未検証)。4-6月期の純利益が原子力の原価算入で-37%との記事(時期不明、▲)。[Newswitch](https://newswitch.jp/p/47552) |
| 日本製鋼所 | 5631 | 未取得 | 未取得 | 未取得 | 未取得 | 検索に該当情報なし。候補(訓練知識・未検証) |
| Curtiss-Wright, Lightbridge, Fluor, UEC, Energy Fuels 等 | CW, LTBR, FLR, UEC, UUUU | **未調査** | 未調査 | 未調査 | 未調査 | 候補(訓練知識・未検証) |

### 参考(ゲート外)
| 銘柄 | 理由 |
|---|---|
| Cameco | カナダ本籍(訓練知識・未検証)。今回数値未取得 |
| Urenco(英独蘭・非上場)、Orano(仏) | 濃縮の主要供給者。Urenco米NM増設700k SWU(2027年) |
| 日立GEニュークリア | 日立製作所の一部(単独上場ではない)。「日立GEが初の商用化、SMR」の記事あり([Newswitch](https://newswitch.jp/p/47552) ▲、詳細未確認) |
| X-energy、TerraPower 等 | 非上場または未確認 |

## A3-5. 弱気材料(出所つき)

1. **政策・予算リスク(Centrus)**: 2027会計年度のDOE予算案にHALEUカスケードの追加運転資金がなく、DOEは現契約のオプションを行使しない意向。**技術サービスの受注残$0.8Bに影響**。LEU部門の受注残の約$3.0Bは条件付き(ピケトン建設が前提)。[SEC 10-Q](https://www.sec.gov/Archives/edgar/data/0001065059/000162828026053863/leu-20260630.htm) ★
2. **マージン悪化**: Centrusの営業利益率5.9%(前年21.7%)。技術サービス売上-21%。[SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001065059/000162828026053433/ex991-10q2026_08x05.htm) ★
3. **SMR銘柄のデレーティングと収益化前のリスク**: Oklo -42〜46%、NuScale -24〜44%、NNE -33%超(2026年初来)。NuScaleは集団訴訟、Q2売上-99.1%。NNEは売上が予想未達。[247WallSt](https://247wallst.com/investing/2026/09/08/nuscale-power-spikes-13-oklo-climbs-7-is-the-nuclear-selloff-finally-exhausted/) ☆
4. **濃縮の「供給ギャップ」論が割れている**: 「2030年代初頭に不足」と「2030年まで長期契約で確保済み」。Urenco増設(2027年)で短期の逼迫は緩む可能性。SWU現物の2026年値が取得できず、価格の裏づけが弱い。[Northern Miner](https://www.northernminer.com/news/breaking-the-wests-enrichment-bottleneck/1003890718/) ☆
5. **ロシア免除の失効(2028年)が政治判断に左右される**: 延長・撤廃されれば需給逼迫の見方は後退。[Mining.com](https://www.mining.com/web/senate-passes-russian-uranium-import-ban-sending-to-biden/) ☆
6. **見通しの集中リスク**: WNAは2050年見通しが少数の国(中国、米国で過半)に大きく依存と明記。[WNA](https://world-nuclear.org/our-association/publications/world-nuclear-outlook-report/world-nuclear-outlook-report-2026-full-document) ★
7. **BWXTの政府依存・買収統合**: 政府事業が土台。Precision Components Group買収(2026-07-01)の統合、医療事業売却(最大$800M)。[BWXT IR](https://investors.bwxt.com/news-releases/news-release-details/bwx-technologies-reports-second-quarter-2026-results) ★

---

# 付録

## 付録1. 出所間で数値が食い違った項目(上位アナリストの要照合リスト)
| 項目 | 食い違い |
|---|---|
| Vertiv 2025Q4 有機受注の伸び | +152% と +252% |
| Vertiv 2026年通期売上ガイダンス | 約$14B と $13.75B(後者は日付が不自然) |
| Eaton Electrical Americas 受注残の伸び | 1Q(10-Q)は+44%。2Q要約に「受注+41%/受注残+33%」の記載があるが、別期間の混入の可能性 |
| GEV 年初来 | +34%(3月)、+70.5%(7/2)、+75%(日付不明)。起点約$650は複数で整合 |
| GEV フォワードPER | 76.9 / 37.6 / 44.7 / 約47 / 71。日付と定義がバラバラ |
| Caterpillar 受注残 | $63B と $72B |
| Bloom 決算後の株価反応 | +6.08% と -13% |
| Oklo 現金 | $25億 と $2.75億 |
| BNEF 2026年BESS | 「158MW」(誤記)と158GW。2036年は306GWと308GW |
| IEA グリッド投資 | $550B(2026) と 約$400B(現在) |
| Hubbell フォワードPER | Yahoo表示20.49 と 私の計算22.6 |
| 大型変圧器リードタイム | 18〜30か月 / 80〜100週 / 2〜3年 / 4年 / 36〜60か月 |

## 付録2. 未取得項目(追加調査の優先順)
1. A3: Centrus、BWXT、(Cameco)の株価・時価総額・フォワードPER・アナリスト数。原子力/ウランETFのAUMと年初来。SWU・UF6の2026年価格。WNA燃料報告書の2030年SWU需要。
2. A2: Bloom Energyの時価総額・PER・年初来・受注残。Caterpillar/Generac/Cummins(発電)、三菱重工/川崎重工/日本ガイシの最新決算。BESS 2030年見通し($/kWh含む)。
3. A1: 日立エナジーの公式受注残(日立IR資料)、住友電工1Q、ダイヘン/日新電機/東光高岳の時価総額と受注残、GEV・Quanta・Hubbell・Eatonの10月時点の株価と年初来。EPS成長率(ガイダンス前年比)でPEGを再計算。
4. 全般: 日本株の年初来騰落率(分割調整後)。
5. 「訓練知識・未検証」とした本籍・事業構成比・ティッカーは、会社の有価証券報告書/10-Kで確認。

## 付録3. 私の所見(判断ではなく、論点の整理)
- A1は「需要の証拠が最も多面的に揃っている」一方、**認知度も最も高く、バリュエーションは高水準**(GEV 約45倍、Quanta 33〜46倍、日本は6〜9月に圧縮)。供給側の増設が2027〜28年から効いてくる点と、DC案件の遅延・中止推計(15〜50%と幅広)が論点。
- A2は「受注の強さ」と「売上の遅れ(Fluence)」「枠組み合意と確定売上の区別(Bloom、GEVの予約)」が同居。株価データが未取得のため認知度評価は保留。
- A3は燃料(Centrus、BWXT)の**受注残が伸びている一方、SMR銘柄は年初来で大幅安**と二極化。PER・時価総額が未取得のため、割高・割安の評価は不可能。
