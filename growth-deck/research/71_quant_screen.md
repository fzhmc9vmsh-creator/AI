# 71 定量一次ふるい(米国・欧州・日本・インド・中南米) / 2026-10-19

担当: 中位判断・調査(Sonnet)。基準: `70_company_first_screen_brief.md`。
足切り(一次ふるい版) = コンセンサスEPSの3年CAGR >= 30% かつ 予想PER÷CAGR(PEG) <= 0.8、時価総額10億ドル以上。
検索45回(WebSearchのみ、WebFetch不可)を使い切った。既審査の不通過銘柄(日東紡、三井金属、金居、TeraWulf、Cipher、Hut 8、Core Scientific、Applied Digital、Galaxy、IREN、NEXTDC)は調査していない。

## 0. 先に結論(重要な限界)
1. 「CAGR>=30% かつ PEG<=0.8」を、複数ソースで裏づけて明確に満たした会社は1社もない。最も近いのは MercadoLibre、Nu Holdings、SoFi、Affirm(数値の信頼度低)、Reddit(境界)、AppLovin(CAGR 26%)。
2. 構造が「高」の会社(Adyen、dLocal、ラクス)は、EPS成長が年20〜24%で、30%に届かない。PEGは0.6〜0.9。成長条件(31%以上)を満たさないので、Opusの足切り基準どおりなら成長側で落ちる可能性が高い。
3. 成長が30%を超える会社(MELI、NU、Affirm、SoFi、Reddit)は、構造が「中」(与信を自社で抱える、広告が景気に連動、など)にとどまる。構造「高」と成長30%超を両立する会社は、この検索では見つからなかった。
4. 汎用のPEGスクリーナー記事(Zacks、Finviz系、Sure Dividend、fffinstill、日本の株探・みんかぶ系)は、景気循環の素材・エネルギー・保険・半導体メモリ(CF Industries、Micron、Vistra、Nucor、Travelers、SMCI など)ばかりが上位に並び、足切りの構造要件に合う銘柄はほぼ出なかった。日本・インドの成長株ランキング記事は、本文に個別銘柄の数値が出てこなかった。
5. 数値の信頼度は銘柄ごとに大きく違う。MarketScreener、Seeking Alpha、kabuyoho(株予報)の日付つきスナップショットは信頼度「中〜高」。tickflow、therighttrader、Simply Wall St、stockhub.kr、vcpscannerは信頼度「低〜中」(アナリスト数が少ない、日付不明、ソース間で食い違い)。表では出所と信頼度を明記した。「推定」は私の算術であり、公表値ではない。
6. カバー範囲の限界: 欧州はAdyen・Wise・Spotifyしか数値を取れていない。インドはBSE・MCX・Angel One・Bajaj Financeのみ(Eternal、Info Edge、CAMS、CDSLは数値を取れず)。中南米はNU・MELI・dLocal・StoneCoのみ(Inter&Co、XPは取れず)。日本はラクス、Appier、メルカリ、GMO-PG、JMDC、ビジョナルのみ(マネーフォワード、Sansan、ANYCOLORは取れず)。

## 凡例
- 為替は 1ドル=150円で概算。時価総額で「推定」と書いたものは、株価×発行株式数(私の記憶ベース)の概算で、出典の数値ではない。
- PEG = 予想PER ÷ EPS CAGR(%)。どの年度のPERを使ったかは列に書いた。
- 構造A+の可能性は、brief の観点(従量・継続課金・テイクレート・長期契約が収益の過半か、乗り換えコスト、自社が陳腐化設備を抱えないか)による仮置き。

## A. 通過または近い銘柄(13社)

| 会社 | ティッカー(市場) | 業種 | 時価総額 | 予想PER(年度) | EPS 3年CAGR(出所) | PEG | 収益の性格 | 構造A+の可能性 | 業種の需要・途上・未注目の一言 | 出典URL・日付 |
|---|---|---|---|---|---|---|---|---|---|---|
| MercadoLibre | MELI (NASDAQ) | EC・決済・与信(中南米) | 約$90B(推定。MarketScreenerの87,631は単位未確認) | 2026年 45.3倍 / 2027年 30.9倍 / 2028年 21.8倍(2026-10-01) | 2026-28の2年CAGR 約44%(MarketScreener PERから逆算、推定)。コンセンサスEPS 2026 $38.13 → 2027 $55.23 → 2028 $77.62(therighttrader、信頼度低〜中)。Simply Wall Stは年24.6%(2026-07-27) | 2027年PER÷44 = 0.70(推定)。2026年PERで割ると1.03。2026年EPSは物流・与信への先行投資で低い可能性があり、CAGRが過大に出る恐れ | 販売手数料・広告・決済手数料(テイクレート)が主。与信は自社の貸借対照表を使う。物流は自社設備が重い | 中 | 中南米のEC・金融の浸透は途上。米国の機関投資家には既知で、未注目ではない | https://uk.marketscreener.com/quote/stock/MERCADOLIBRE-INC-57732089/valuation/ (2026-10-01時点の記載) / https://therighttrader.com/earnings-calendar/meli / https://simplywall.st/stocks/it/retail/bit-1meli/mercadolibre-shares/future (2026-07-27) |
| Nu Holdings | NU (NYSE) | デジタルバンク(ブラジル・メキシコ・コロンビア) | 約$68.6B(2026-08-28)〜$70.5B | 2026年 19.5〜20.3倍(Yahoo 前方PER 19.68、2026-05-04。MarketScreener 2026年20.3倍) | 2026-29の3年CAGR 約27%(EPS $0.86 → $1.11(+31.7%) → +29.4% → +23.2%、stockalarm/tickflow、信頼度中)。2026-28の2年では約30.5% | 19.5÷27 = 0.72(推定)。Yahoo 5年PEG 0.83(2026-05-04)、Zacks系 0.55〜0.57(日付ばらつき) | 利息・手数料収入。顧客あたり費用が低い一方、与信リスクは自社が負う | 中 | 中南米の口座・与信の浸透は途上。米国機関には既知 | https://pro.stockalarm.io/quote/NU/analysts / https://finance.yahoo.com/quote/nu/ (2026-05-04) / https://www.valueresearchonline.com/stocks/298146/nu-holdings-ltd-nu/key-ratios/ (2026-08-28) |
| AppLovin | APP (NASDAQ) | 広告配信ソフト(アプリ向け) | 約$94B(推定。株価$277 × 約3.4億株) | 2026年 17.7倍 / 2027年 13.9倍 / 2028年 11.1倍(株価約$277、2026-10-09) | 2026-28の2年CAGR 約26%(PERから逆算、推定)。EPS 2026 $15.66(tickflow、2026-08-01)。Simply Wall Stは年23.3% | 2027年PER÷26 = 0.53 / 2026年PER÷26 = 0.68(推定)。CAGRは30%に届かない | 広告主の支出に対する手数料(オークションの取り分)。従量型だが広告予算は景気連動。プラットフォーム依存あり | 中 | AI広告の需要は強い。2026年に株価が$386 → $277へ下落し、見方が割れている(価格日付が混在、要確認) | https://ca.marketscreener.com/quote/stock/APPLOVIN-CORPORATION-121407289/valuation/ (2026-10-09) / https://www.tickflow.io/stock/APP/forecast (2026-08-01) / https://simplywall.st/stocks/ch/software/vtx-app/applovin-shares/future |
| SoFi Technologies | SOFI (NASDAQ) | ネット銀行・貸出・手数料事業 | 約$22〜25B(推定。株価$18.91) | 2026年 29.9倍 / 2027年 21.75倍 / 2028年 16.91倍(2026-08-21) | 2026-28の2年CAGR 約33%(Seeking Alpha: 2027年 +37.5%、2028年 +28.6%)。FY2027 EPS 約$0.82(24/7 Wall St、2026-09-03) | 2027年PER÷33 = 0.66(推定)。2026年PER基準では0.9。PEG 0.883という引用あり(24/7 Wall St、2026-08-11) | 利息・手数料。銀行免許つきで、貸借対照表と与信リスクが重い | 低 | 米国の個人金融の置き換えは途上だが、既に注目度は高い | https://seekingalpha.com/symbol/SOFI/valuation/price-earnings-peg-ratios (2026-08-21) / https://247wallst.com/investing/2026/09/03/price-prediction-sofis-price-target-for-2027-may-surprise-investors/ |
| Affirm | AFRM (NASDAQ) | 後払い(BNPL)・加盟店決済 | 約$15〜30B(推定、株価未確認) | 約22倍(stockhub、2026-07。年度基準が不明) | FY2027(6月期) EPS $1.91 → FY2028 $2.87(+50%) → FY2029 $3.86(+34%)(therighttrader)。FY27-29の2年CAGR 約42%(推定)。ただしtickflowは別数値($1.62 / $0.88)で、ソース間の食い違いが大きい。信頼度低 | 22÷42 = 0.52(推定。信頼度低) | 加盟店手数料+貸付金利。貸出資金は自社で調達し、与信リスクを負う | 中 | 米国BNPLの浸透は途上。次回決算 2026-11-05 | https://therighttrader.com/earnings-calendar/afrm / https://tickflow.io/stock/AFRM/forecast / https://seekingalpha.com/symbol/AFRM/valuation/price-earnings-peg-ratios (2026-01時点で古い) |
| Reddit | RDDT (NYSE) | SNS・広告・データ提供 | 約$34B(推定。株価約$180、時期不明) | 2027年 約29倍 / 2026年 約43倍(推定。株価$180をtickflowのEPS合計で割った私の計算) | 2026-28の2年CAGR 約37%(推定)。EPS 2026 約$4.14 → 2027 約$6.16 → 2028 約$7.76(tickflowの四半期合計、私の算術、信頼度低) | 2027年PER÷37 = 0.79 / 2026年PERでは1.18(推定。境界) | 広告収入が主で、データ提供の長期契約が一部。景気連動 | 中 | 利用者基盤の収益化は途上。株価と推定が日付不明のため要確認 | https://tickflow.io/stock/RDDT/forecast / https://www.stockhub.kr/en/stock/RDDT |
| Oracle | ORCL (NYSE) | クラウド基盤・データベース・SaaS | 約$410B(推定。株価約$144) | FY2027(5月期) 約22.5倍(2026-08の第三者ページ。株価約$144と整合) | FY2027 EPS $6.39 → FY2028 $8.67(+36%)(第三者ページ、2026-08、信頼度低)。経営陣目標はFY2030に非GAAP EPS $21、年28%成長 | 22.5÷28 = 0.80(推定。経営陣目標ベース。コンセンサスの3年CAGRは未確認) | 長期契約の利用料(RPO)と従量のクラウド。ただしデータセンターの設備投資・借入が非常に重い | 中(高寄り) | AI基盤需要は強い。brief の条件13の基準企業だが、自社がcapexを負う面は賃貸業審査で既に論点化済み | https://tickerleague.com/companies/ORCL/price-target / https://www.barchart.com/story/news/518001/why-oppenheimer-says-oracle-stock-can-gain-25-from-here / https://terminal.159.65.128.240.sslip.io/name-ORCL.html |
| Uber Technologies | UBER (NYSE) | 配車・配達プラットフォーム | 約$150〜200B(推定、未確認) | 非GAAP予想PER 38倍(TipRanks、日付不明)/ 現会計年度EPSの33.4倍(Zacks、日付不明) | 3〜5年コンセンサスCAGR 46%(TipRanks経由、日付不明、信頼度低) | 0.83(TipRanks)〜1.23(Zacks)。ソース間で食い違う | 乗客・配達の取扱高に対する手数料(テイクレート)。ネットワーク効果あり。自動運転による代替リスクあり | 中 | 世界の移動・配達の需要は大きいが既に有名 | https://www.nasdaq.com/articles/uber-lyft-or-dash-which-mobility-delivery-company-offers-best-investment-potential / https://fullratio.com/stocks/nyse-uber/peg-ratio |
| Adyen | ADYEN (アムステルダム) | 決済処理(企業向け一括プラットフォーム) | 約€30〜34bn(Stockopedia) | 2026年 約22〜28倍 / 2027年 約18〜22倍(価格€855.5〜€1,074から推定) | コア EPS 2026 €38.58 → 2027 €47.84(+24%)(BMO、2026-05)。コンセンサス 2026 €38.44〜38.69(Stockopedia)。2028年は未確認 | 0.75〜0.93(推定)。成長が24%で30%に届かない | 処理額に対する手数料(テイクレート)。乗り換えコストが高い。自社の陳腐化設備はほぼ無い | 高 | 世界の決済のオンライン化は継続。ただし欧州大型株で既知 | https://www.placera.se/telegram/adyen-adyen-reaffirmed-at-outperform-as-bmo-highlights-stable-q1-trends-20260507 / https://www.stockopedia.com/share-prices/adyen-n-v-AMS:ADYEN/ / https://www.simplywall.st/company/id/7df1eb38-60e0-450a-92de-5190919722f4/valuation |
| dLocal | DLO (NASDAQ) | 新興国向け決済(越境・現地決済) | 約$4.5B(推定。株価$15.36 × 約2.9億株) | 2027年 約14.1倍(株価$15.36、2026-08-26) | EPS 2026 $0.81 → 2027 $1.09(+35%) → 2028 $1.23(+13%)(therighttrader、アナリスト2〜3名)。2026-28の2年CAGR 約23%(推定)。Simply Wall Stは3年20% | 14.1÷23 = 0.61(推定)。成長は30%に届かない。直近四半期は予想未達(EPS $0.18 vs $0.20、2026-08) | 処理額に対する手数料(テイクレート)。多通貨・多国の接続で乗り換えコストが高い。自社の陳腐化設備は小さい | 高 | 新興国の越境EC・決済は途上。時価総額が比較的小さく未注目度は高い。カバレッジ薄(アナリスト2〜3名)で数値の信頼度低 | https://therighttrader.com/earnings-calendar/dlo / https://tickflow.io/stock/DLO/forecast / https://stockhub.kr/en/stock/DLO (2026-07) |
| ラクス | 3923 (東証) | SaaS(経費精算など) | 約¥2,100億 = 約$1.4B(推定) | 来期(2027年3月期) 15.1倍(株価¥1,071.5、2026-10-07。会社予想EPS ¥71.2) | 経常利益コンセンサス ¥215億(+23.5%、2026-09-16)、営業利益 ¥211億(+21.9%)。3年CAGRは未確認で、1年成長で代用 | 15.1÷23.5 = 0.64(推定)。成長が30%に届かない | 継続課金(SaaS)。解約率が低く、乗り換えコストが高い。陳腐化設備は無い | 高 | 国内中小企業のDX・インボイス対応は継続。「SaaSの死」(AIによるSaaS懸念)で2026年に売られ割安に見える点は未注目寄り | https://kabuyoho.jp/reportAnalyst?bcode=3923 / https://scouter.monex.co.jp/report/index/3923 / https://gendai.media/articles/-/162349 |
| Appier Group | 4180 (東証) | AI広告・マーケティングSaaS(台湾・アジア) | 約$0.85〜1.1B(推定。10億ドル前後で要確認) | 28.0〜37.9倍(掲載日による差、日付不明) | 営業利益 2026年12月期 ¥50.3億(+69.1%)、2023年 ¥8.0億から3年CAGR 約84%(営業利益。EPSではない。私の計算)。EPSのコンセンサスCAGRは未確認 | 営業利益成長で割ると約0.4〜0.5(推定)だが、EPSベースでは未検証。信頼度低 | ソフトウェア利用料(サブスクと従量の混在)。顧客の広告予算に連動 | 中 | アジアのAI広告は成長中。時価総額が小さく未注目。10億ドル条件の確認が必要 | https://kabuyoho.jp/reportAnalyst?bcode=4180 / https://scouter.monex.co.jp/report/zaimu/4180 / https://finboard.jp/companies/JP%3A4180/income-statement |
| メルカリ | 4385 (東証) | フリマ・フィンテック | 約¥6,100億 = 約$4B(推定) | 12か月先アナリストPER 15.6倍(株価¥3,699、2026-09-18) | 来期(2027年6月期)経常利益コンセンサス ¥524億(+18.7%、2026-10-08)。2026年6月期は ¥442億 | 15.6÷18.7 = 0.83(推定)。成長が30%に届かない | 販売手数料(テイクレート)+決済・与信。ネットワーク効果あり | 中 | 国内CtoCの成熟市場で、成長は鈍化しつつある | https://kabuyoho.jp/report?bcode=4385 (2026-10-08) / https://kabuyoho.jp/reportAnalyst?bcode=4385 |

## B. 確認したが足切りに届かない銘柄(14社)

| 会社 | ティッカー(市場) | 業種 | 時価総額 | 予想PER(年度) | EPS成長・CAGR(出所) | PEG | 収益の性格 | 構造A+の可能性 | 不通過の理由(一言) | 出典URL・日付 |
|---|---|---|---|---|---|---|---|---|---|---|
| Sea Limited | SE (NYSE) | EC・ゲーム・フィンテック(東南アジア) | 約$62B(推定) | 21.8倍(2026-07中旬、株価$103) / 別ソース40倍(2026-08-06) | 年19.2%(Simply Wall St、2026-03) | 約1.1(推定) | 手数料+ゲーム+与信 | 中 | 成長が20%弱でPEG>1 | https://www.stockhub.kr/en/stock/SE / https://simplywall.st/stocks/br/retail/bovespa-s2ea34/sea-shares/future |
| Wise | WISE (LSE) | 国際送金 | 約£9.9bn(推定) | 23.6倍(2027・2028年、株価973.2p、2026-09上旬) | 会社目標FY27 EPS 約+24%、Simply Wall St 8〜15.5%/年 | 2.1(Seeking Alpha引用) | 送金額への手数料(テイクレート)。構造は高 | 高 | 成長12〜24%でPEG>2。構造は良いが成長側で落ちる | https://uk.marketscreener.com/quote/stock/WISE-PLC-124542474/finances/ / https://simplywall.st/stocks/us/diversified-financials/nasdaq-wse/wise-group/future |
| Spotify | SPOT (NYSE) | 音楽・音声配信 | 約$80B(推定) | 27倍(2026-07、stockhub) | FY2026 EPS $14.46 → FY2027 Erste予想 $17.60(約+22%、MarketBeat 2026-07-29) | 約1.2(推定) | 継続課金(サブスク) | 高 | 成長22%でPEG>1 | https://www.marketbeat.com/instant-alerts/research-analysts-set-expectations-for-spot-fy2027-earnings-2026-07-29/ |
| Robinhood | HOOD (NASDAQ) | ネット証券・暗号資産 | 約$70B(推定) | 2027年 約30倍(推定、株価$79前後 2026-05) / Zacks 74倍 | 2026 $2.08 → 2027 約$2.65(約+27%、tickflow、私の合計) | 4.24(Zacks、日付不明) | 取引手数料+金利収入。市況連動 | 中 | PEGが高く、市況に左右される | https://www.tickflow.io/stock/HOOD/forecast / https://www.tikr.com/blog/robinhood-stock-is-down-30-in-2026-heres-why-analysts-still-sees-125-fair-value |
| Interactive Brokers | IBKR (NASDAQ) | ネット証券 | 約$150B(推定) | 2026年 約36倍 / 2027年 約32倍(MarketScreener、株価$90.81) | EPS $2.50 → $2.87 → $3.19(各年+11〜15%) | 約2.4(推定) | 取引手数料+金利収入 | 中 | 成長13%程度でPEG>2 | https://in.marketscreener.com/quote/stock/INTERACTIVE-BROKERS-GROUP-50014/valuation/ |
| BSE Ltd | BSE (インドNSE/BSE) | 取引所(株式・デリバティブ手数料) | 約$15B(推定。株価₹3,278) | FY27 約41倍(株価₹3,278 ÷ EPS ₹79.65、2026-10-09) | FY26 ₹60.61 → FY27 ₹79.65(+31.4%)。FY28は未確認 | 約1.3(推定) | 取引手数料(従量)。構造は高 | 高 | PERが約41倍でPEG>1。FY28コンセンサスが取れず3年CAGR未確認 | https://sharpely.in/stocks/bse/forecast / https://univest.in/blogs/bse-share-price-target-2027 (2026-10-09) |
| Multi Commodity Exchange | MCX (インド) | 商品取引所 | 約$8.7B(₹73,758億、2026-04-28) | 2027年 約42〜51倍(価格が旧水準のため参考) | EPS ₹193.5 → ₹235.9 → ₹276.5(MarketScreener、株式分割前の可能性、約+22%、+17%) | 約2〜3(推定) | 取引手数料(従量)。構造は高 | 高 | 成長17〜22%でPERが高い。分割の有無が未確認で数値の信頼度低 | https://in.marketscreener.com/quote/stock/MULTI-COMMODITY-EXCHANGE--10315042/ / https://uk.marketscreener.com/quote/stock/MULTI-COMMODITY-EXCHANGE--10315042/valuation-dividend/ |
| Angel One | ANGELONE (インド) | ネット証券 | 約$2.7B(推定) | FY27 約17〜18倍(JM: FY27e EPS ₹141、株価約₹2,500、2026-05) | FY28 EPSはMotilal Oswalが21倍で目標₹3,400(2026-01)。成長は約15%と推定 | 約1.2(推定) | 取引手数料。市況連動 | 中 | 成長15%程度。コンセンサスの3年CAGR未確認 | https://www.business-standard.com/amp/markets/news/angel-one-gets-buy-call-what-makes-jm-financial-bullish-after-20-pc-ytd-fall-stock-market-125090800143_1.html |
| Bajaj Finance | BAJFINANCE (インド) | ノンバンク貸出 | 約$76B(推定) | 実績PER 34.5倍(2026-07) | FY27 EPS ₹40(+29.4%) | 約1.2(推定) | 貸出金利。貸借対照表が重い | 低 | PER34倍でPEG>1。貸出業で構造も弱い | https://sharpely.in/stocks/bajfinance/forecast |
| GMOペイメントゲートウェイ | 3769 (東証) | 決済処理 | 約$5〜6B(推定) | 31.6倍(2026-07-10) | 営業利益 2023年9月期 ¥203億 → 2026年9月期予想 ¥376億(年約23%、営業利益ベース) | 約1.4(推定) | 処理額への手数料。構造は高 | 高 | 成長23%でPEG>1 | https://kabuyoho.jp/report?bcode=3769 |
| Palantir | PLTR (NASDAQ) | データ分析ソフト | 約$480B(推定) | 85.7倍(株価約$201、2026-10-15) | 2025-28のEPS CAGR 約55%(TheStreet Pro、2026-05) | 1.3倍(2027年EPS $1.94基準、TheStreet)。Yahoo 5年PEG 2.49 | 継続課金+政府・企業契約 | 高 | PERが高すぎてPEG>1 | https://iocharts.io/de/aktie/PLTR (2026-10-15) / https://pro.thestreet.com/portfolio/palantirs-nonsensical-pullback-after-earnings-is-missing-the-point |
| StoneCo | STNE (NASDAQ) | 決済・与信(ブラジル) | 約$3.9B(推定) | 約7〜9倍(株価$14.29、2026-03) | FY2026 EPS ガイダンス $2.00〜2.11 → FY2027 $2.19〜2.48(約+8〜10%、MarketBeat 2026-03-05) | 約1.0(推定) | 決済手数料+与信 | 中 | PERは低いが成長が1桁で足切り外 | https://www.marketbeat.com/instant-alerts/stoneco-nasdaqstne-updates-fy-2026-earnings-guidance-2026-03-05/ |
| JMDC | 4483 (東証) | ヘルスケアデータ | 約$1〜1.5B(推定、要確認) | 31.9倍(2026-09-09、株価¥3,460) / 34.3倍(株価¥3,720) | 経常利益 会社予想 +10.4%、コンセンサス +13.9% | 約2.5〜3.4(推定) | データ利用料・サブスク | 高 | 成長10%台でPEG>2 | https://kabuyoho.jp/reportDisclose?bcode=4483 / https://www.traders.co.jp/stocks/61_4483/achievement |
| ビジョナル | 4194 (東証) | HR SaaS(ビズリーチ) | 約$2.5B(推定) | 21.4倍(株価¥9,824、2026-10-09) | 経常利益コンセンサス +5.1%(2026-10-09)。9月時点の+8.1%から低下 | 約4(推定) | 継続課金+成功報酬 | 高 | 成長5%でPEG>2 | https://kabuyoho.jp/report?bcode=4194 |
| DoorDash | DASH (NASDAQ) | 配達プラットフォーム | 約$100B(推定) | 114倍(Zacks系、日付不明) | 信頼できるコンセンサス3年CAGRを取得できず(vcpscannerの独自モデルは信頼不可) | 0.4(実績ベースの計算サイト、2026Q1。前方ではない) | 取扱高への手数料 | 中 | 前方PERが高く、データ不十分で保留 | https://www.opencapital.sh/stocks/dash/metrics/peg_ratio / https://www.vcpscanner.com/valuation/dash/estimates |

(注: 表Bの「Bajaj Finance」「MCX」「Angel One」の時価総額は価格が日付ごとに大きくずれるため、桁感のみ。)

## C. Opusが二次審査に回すべき上位10社
並び順は指示どおり「構造の可能性が高で、PEGが低い順」を優先し、その後に構造「中」をPEG順に並べた。成長条件(CAGR>=30%)を満たすかは別の列で明記した。

| 順位 | 会社 | 構造 | PEG(推定) | EPS CAGR | 二次審査に回す理由と、確認すべき点 |
|---|---|---|---|---|---|
| 1 | dLocal (DLO) | 高 | 0.61 | 約23%(2027年+35%、2028年+13%) | テイクレート型で、新興国の多通貨・多国接続が乗り換えコストになる。陳腐化設備もほぼ無い。時価総額約$4.5Bと小さく、アナリスト2〜3名で未注目。弱点は成長が30%に届かない点と、2028年成長の鈍化。EPS予想の信頼度が低いので、最新コンセンサスの再取得が必要 |
| 2 | ラクス (3923) | 高 | 0.64 | 経常 約+23.5%(1年) | 継続課金SaaSで、PER 15倍、時価総額約$1.4B。「SaaSの死」で売られたあとの割安さが未注目の根拠。弱点は成長20%台でCAGR 30%に届かない点。3年CAGR(会社中計・コンセンサス)の確認が必要 |
| 3 | Adyen (ADYEN) | 高 | 0.75〜0.93 | 約24%(2027年) | 構造は今回の中で最も良い(処理額手数料、乗り換えコスト高、設備軽い)。弱点は成長24%と、欧州大型株で既知である点。2028年のコンセンサス取得と、価格日付の確定が必要 |
| 4 | AppLovin (APP) | 中 | 0.53〜0.68 | 約26%(2026-28) | PEGが最も低い部類。2026年に株価が下落(約$386 → $277)し、市場の見方が割れている点が「見落とし」候補か、構造的な懸念かを二次審査で見極める。広告予算の景気連動とプラットフォーム依存が構造の論点 |
| 5 | Nu Holdings (NU) | 中 | 0.72 | 約27〜30% | 3年CAGRが30%近辺で、PEGは0.7台。ARPACの増加と低コスト運営。与信リスクを自社で負う点が条件12・13で論点。時価総額約$69B |
| 6 | MercadoLibre (MELI) | 中 | 0.70(2027年PER基準)/ 1.03(2026年PER基準) | 約44%(2026-28、低い基準年の影響あり) | 成長条件を最も明確に満たす。ただし2026年EPSが投資で一時的に低く、CAGRが過大の恐れ。2025年実績を基準にした3年CAGRの確認が必要。物流・与信は自社資産が重い |
| 7 | Affirm (AFRM) | 中 | 約0.52(信頼度低) | 約42%(FY27-29) | 成長条件は満たす可能性がある。ただしEPS予想がソース間で矛盾し、株価も未確認。まずコンセンサスと株価の確定が先。与信を自社で負う点が構造の論点 |
| 8 | Reddit (RDDT) | 中 | 0.79(2027年PER)/ 1.18(2026年PER) | 約37% | 境界。EPSは推定の合計であり、価格日付も不明。データ提供の長期契約の比率を確認する価値がある |
| 9 | Oracle (ORCL) | 中(高寄り) | 約0.80 | 経営陣目標 年28%(コンセンサスは未確認) | brief の条件13の基準企業。ただし自社がデータセンターcapexと借入を負う面が重い。コンセンサスの3年CAGRと現在株価の確認が必要 |
| 10 | Uber (UBER) | 中 | 0.83〜1.23(ソース間で食い違い) | 3〜5年 46%(信頼度低) | テイクレート型でネットワーク効果あり。EPSが非GAAP/GAAPで大きく違うため、基準の統一が先 |

補欠: Appier(営業利益成長が大きいが、EPSベースのCAGR・時価総額の確認が必要)、メルカリ(PEG 0.83、成長19%で足切り外れ)、SoFi(2026-28のEPS CAGR 約33%・PEG 0.66で数値は通過するが、銀行型の貸借対照表で構造は低)。

## D. 次にやるべきこと(提案)
- 上位候補(MELI、NU、AFRM、RDDT、DLO)は、TradingViewのコンセンサス(スキルで定める手段)かMarketScreenerの年度別EPS表で、同一日付の株価とEPS(2026〜2029年)を取り直す。今回は複数ソースの混在で、PEGの精度は粗い。
- 構造が高(Adyen、dLocal、ラクス、Wise、BSE、Palantir、JMDC)でも、成長30%超とPEG 0.8以下を同時に満たす会社は今回の範囲では無かった。足切りの成長条件を再検討するか、対象を広げる(未調査: 台湾・韓国、欧州の中小型、日本の新興SaaS、インドの小型株)必要がある。
- 今回取れなかった候補(Eternal、Info Edge、CAMS、CDSL、Inter&Co、XP、マネーフォワード、Sansan、ANYCOLOR、Nemetschek、Evolution など)は追加検索の候補。
