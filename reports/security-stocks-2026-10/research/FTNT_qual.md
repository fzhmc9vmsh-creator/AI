# Fortinet(FTNT)定性調査 一次整理(Phase 1・第2版)

- 評価基準日: 2026-10-11 / 決算期末: 12月31日 / 取得日: 2026-10-11(すべての出典)
- 担当: Sonnet(調査)。評価・投資判断は行わない。事実・出典・「なぜ重要か」の注記のみ。
- 第2版: 検索予算が回復し、再開で 18 回の WebSearch を使い切った(初回 4 回と合わせて 22 回)。数値データ(四半期業績・KPI)は別担当のため追っていない。

## 0. 調査状況

| 節 | 取得状況 |
|---|---|
| A-1 経営陣の発言 | 部分。2026 Q2・Q1 の要旨と、2025年8月の更新サイクル説明、2026年の Goldman 講演は取れた。2025 Q3・Q4 の発言本文、Investor Day は欠損(見出しのみ) |
| A-2 数値目標 | 部分。2026年のガイダンスと、2025年8月時点の「12%の複利成長」目標は取れた。指標の定義と SASE/SecOps の目標は欠損 |
| A-3 ピース一覧 | 部分。更新サイクルの規模、SP6/Intel、価格改定、FortiOS 8.0 は取れた。買収・capex・自社株買いは欠損 |
| A-4 ガイダンス達成状況 | 部分。2023年11月、2025年8月、2025年通期は取れた。2024年の経緯、期初 vs 実績の3年表は欠損 |
| A-5 経営陣・報酬 | 部分。役員構成と DEF 14A の所在は取れた。報酬 KPI の中身は欠損 |
| B 市場の仮説 | 概ね取得。強気の具体名は 2026年で 2 件(BTIG、TD Cowen)にとどまり、要件の 3 件に 1 件足りない。各社の「現在の格付け」は未確認 |
| C 一次情報 | 3件(Gartner MQ、価格改定、メモリ価格)。ただし IDC 出荷シェア、チャネルの声、半導体の調達は欠損。要件の「最低3件」は形式上満たすが、いずれも裏付けは弱い(§C) |
| D 競争・業界 | 部分。市場規模の統計は欠損 |
| E 異常値の候補 | 9候補 |
| F 条件9 | 部分。AI データセンター向け需要の開示値は欠損 |
| G リスク事象 | 部分。脆弱性は取得。訴訟は存在のみ。会計・規制・経営陣の株式売却は欠損 |

**読み手への注意**
1. 数値・発言はすべて検索要約経由で、会社IRの原文(PDF/HTML)は読めていない。会社IRのURLは §J に記した。
2. 転記サイトの説明会の本文は、話者ラベルが乱れ、文が壊れている箇所がある(検索ツールの警告)。発言は「要旨」として扱い、引用する前に IR 原文で確認すること。
3. 出典間で食い違う項目は §H に集めた。
4. 株価の水準は出典間で食い違い、2026-10-09 の終値は取れていない(§B-5)。株価は別担当の値を使うこと。

### 用語の一言定義(初出)
- **billings(請求額)**: 売上+繰延収益の増減。サービス契約を前払いで請求した分を含み、将来売上の先行指標になる。
- **繰延収益**: 先に請求・入金したが、まだ売上に計上していないサービス契約の残高。
- **non-GAAP**: 株式報酬・買収無形資産の償却などを除いた会社独自定義の利益。GAAP は米国会計基準の利益。
- **FCF(フリーキャッシュフロー)**: 営業キャッシュフロー − 設備投資。
- **ASIC**: 特定用途向けに設計した半導体。Fortinet は自社設計のセキュリティ専用チップ(世代名 SP5、次が SP6)をファイアウォールに載せる。
- **ASP**: 製品1台あたりの平均販売価格。
- **FortiOS**: Fortinet の製品群を貫く単一の基本ソフト。
- **SASE(サシー)**: ネットワークとセキュリティ機能をクラウド経由で一体提供する方式。SD-WAN(拠点間回線の制御)と SSE(クラウド型セキュリティ)の組み合わせ。Fortinet は「Unified SASE」と呼ぶ。
- **SecOps**: セキュリティ運用(検知・調査・対応)。**OT**: 工場・プラント等の制御系。
- **ハイブリッド・メッシュ・ファイアウォール(HMF)**: 拠点・データセンター・クラウドに散らばるファイアウォールを一元管理する枠組み。Gartner が 2025年に新設したマジック・クアドラント(MQ)の対象。
- **KEV**: 米国 CISA(サイバーセキュリティ・インフラ安全保障庁)が公表する「悪用が確認された脆弱性」の一覧。
- **Tier**: 情報源の格付け。1=会社開示、2=公的統計・規制当局、3=主要報道・アナリスト、4=ブログ・SNS・自動要約・集計サイト。

---

## A. 経営陣シナリオの一次情報

### A-1. 決算説明会・講演での経営陣の発言(和訳が主、原文は括弧で最小限)

| 時期 | 話者 | 発言の要旨(和訳) | 骨格のどの部分か | 出典 / Tier |
|---|---|---|---|---|
| 2025-08(Q2 2025 説明会) | Christiane Ohlgart(CFO) | 「2026年の更新サイクルは、残っている稼働中の機器とサービス契約から見て、第2四半期末時点でおよそ40〜50%まで進んだと見ている」(原文: "approximately 40% to 50% of the way through the 2026 upgrade cycle") | ファイアウォール更新サイクル | [Zacks/Nasdaq](https://www.nasdaq.com/articles/will-fortinets-firewall-upgrade-cycle-continue-power-top-line-growth)、[Fortinet IR: Q2 2025 準備原稿](https://investor.fortinet.com/static-files/5a5d281a-78fa-4ec3-a23f-9305a187de2d)(本文未読) / Tier 3 |
| 2025-08 | 経営陣 | 2026年に保守サポートが終わる機器は約65万台、2027年に低価格帯の約35万台が続く。更新サイクルは少なくとも今後4〜6四半期は続くと見る。2027年の群は単価が低い(Ken Xie) | 更新サイクルの規模 | [Barchart](https://www.barchart.com/story/news/34071991/fortinet-stock-is-plunging-on-refresh-cycle-woes-should-you-buy-the-ftnt-dip)、[The Stack](https://www.thestack.technology/fortinets-one-million-end-of-life-firewalls-has-investors-freaking-out-a-bit/)、[SDxCentral](https://www.sdxcentral.com/news/fortinet-financials-float-sase-trajectory-and-firewall-fears/) / Tier 3 |
| 2025-08 | 経営陣 | 更新サイクルが成熟するにつれ、成長の重心は SASE と SecOps に移す。今後3〜5年の複利成長率12%の目標は維持(指標が売上か billings かは未確認) | SASE/SecOps、中期目標 | 同上 / Tier 3 |
| 2026-05-06(Q1 2026 説明会) | Ken Xie | SASE ファイアウォールは、中核機能を単一のOSに native に統合し、複雑さを大きく減らす。Unified SASE は現在 billings の約25% | 単一OS統合、SASE | [Insider Monkey](https://www.insidermonkey.com/blog/fortinet-inc-nasdaqftnt-q1-2026-earnings-call-transcript-1756043/)、[Motley Fool Q1](https://www.fool.com/earnings/call-transcripts/2026/05/06/fortinet-ftnt-q1-2026-earnings-transcript/)(本文未読) / Tier 3 |
| 2026-05-06 | Ken Xie | SecOps の billings が23%増。「20を超えるAI対応ソリューション」。新ファイアウォール FortiGate 3500G・400G を同日発表 | SecOps、AI、自社ASICの価格性能 | 同上 / Tier 3 |
| 2026-05-06 | Ken Xie / 経営陣 | 2024年から2025年初めは「消化(digestion)」の時期だったが、それでもシェアは取れた。今は先食い(pull forward)はあまり見えず、需要は強い。チャネル在庫は会社が管理できる | 2023〜2025年の説明、在庫 | [Investing.com: Q1 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-fortinet-exceeds-q1-2026-forecasts-with-strong-growth-93CH-4665847) の検索要約 / Tier 3 |
| 2026-05-06 | Ohlgart | 前年の billings がマイナスだったことが、サービスの付帯率(機器に付くサービス契約の割合)の低下を通じて今のサービス売上に響いている | 機器→サービスの時間差 | 同上 / Tier 3 |
| 2026(Goldman Sachs 講演) | Ken Xie | 約5年前の供給網の混乱期は先食いが多く、顧客側も含めて在庫が積み上がった。今はチャネル在庫を注視し、パートナーに値引きや奨励金での在庫積み増しを促さない。機器を購入してからサービス登録できる期間を、かつての最長1年から90日に短縮した | チャネル在庫の統制 | [Investing.com: Goldman 講演](https://www.investing.com/news/transcripts/fortinet-at-goldman-sachs-conference-ai-security-drives-growth-93CH-4892267) の検索要約 / Tier 3 |
| 2026-07-29(Q2 2026 説明会) | Ken Xie | 「第2四半期は極めて良い結果」。差別化した戦略と幅広い需要の成果。SASE ファイアウォールを約20年前の次世代ファイアウォール(NGFW)への移行になぞらえ、より大きな市場を持つ機会と位置づけた。AI・SASE・量子耐性の高成長領域に当たる。FortiSASE の売上は前年比で2倍超 | SASE ファイアウォール、AI | [Investing.com: Q2 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-fortinet-tops-q2-2026-forecasts-and-shares-jump-93CH-4821909)、[Motley Fool Q2](https://www.fool.com/earnings/call-transcripts/2026/08/07/fortinet-ftnt-q2-2026-earnings-call-transcript/) の検索要約 / Tier 3 |
| 2026-07-29 | Ken Xie | 構内設置型の「ソブリンSASE」の対象市場は、クラウド専用のSASEの2〜3倍 | SASE(主権・ローカル運用) | [Vectorshift 要約](https://vectorshift.ai/research/companies/fortinet/earnings/2026-q2-summary) / Tier 4・要原文確認 |
| 2026-07-29 | Ken Xie | AIはネットワークとセキュリティの融合を加速する。AIはトラフィックを大きく増やす(機械同士の通信量が人間の通信量を初めて上回ったという調査を引いた)。自社ASICでセキュリティ製品を作る唯一の企業である | AI、自社ASIC | 同上、[Yahoo 転載](https://finance.yahoo.com/quote/FTNT/earnings/FTNT-Q2-2026-earnings_call-661676.html) / Tier 3〜4 |
| 2026-07-29 | Ken Xie | 部品(メモリ等)のコストに合わせて、価格をほぼ即時に調整している。事業への影響は1桁% | 価格・部品コスト | 同上 / Tier 3 |
| 2026-07-29 | Ohlgart | 製品の伸びは FortiGate の出荷台数の増加と ASP の上昇が牽引。チャネルに過剰在庫や先食いは見ていない(ある転記の記述)。下期の billings 見通しには価格改定の「1桁後半%」の影響を織り込み済み。すべての製品・サービスに値上げが及ぶわけではなく、製品構成に依存する。サービス売上の伸びは、製品の加速につれて下期に上向く | 更新サイクル、ASP、サービスの時間差 | Fortinet IR 準備原稿 [Q2 2026](https://investor.fortinet.com/static-files/92543183-3383-4279-a3a4-13c7db91fcbb)(本文未読・要約経由 / Tier 1)と上記転記 / Tier 3 |

- 説明会の出席者(2026 Q2): Ken Xie(創業者・会長・CEO)、CFO Christiane Ohlgart、COO John Whittle。Michael Xie(社長兼CTO)の発言は未取得。
- **欠損**: 2025 Q3(Investing.com の見出し「予想を上回るがストック(株価)は小幅下落」)、2025 Q4(同「EPSは予想超え、株価は小幅下落」)の発言本文。直近の Investor Day / アナリスト説明会の発言。

**なぜ重要か**: 2025年8月に経営陣は「2026年の更新サイクルは約半分まで進んだ」と説明し、市場は「残りが少ない」と受け取った。
ところが 2026年Q2 の製品売上は+52%。この間に何が起きたか(更新の取りこぼしが戻った、価格と ASP が上がった、AI 向け需要が足された、のどれか)が、成長の持続性の判断軸になる。

### A-2. 数値目標とその定義・期限

| 項目 | 内容 | 出典 / Tier | 状態 |
|---|---|---|---|
| FY2026 売上ガイダンス(2026-07-29) | 前年比19%増に引き上げ。80億2,000万〜81億8,000万ドル | [Fortinet IR プレスリリース](https://fortinet.gcs-web.com/static-files/e4ffcc79-194e-4ca3-9a69-8a51bd0a6314)の要約を [mfn.se](https://mfn.se/one/a/fortinet/fortinet-reports-strong-second-quarter-2026-financial-results-c7dd36df) 経由で確認 / Tier 1(原文未読) | 取得 |
| FY2026 billings ガイダンス(2026-07-29) | 93億5,000万〜95億5,000万ドル。下期は四半期ごとに管理 | [Fortinet IR Q2 2026 準備原稿](https://investor.fortinet.com/static-files/92543183-3383-4279-a3a4-13c7db91fcbb)の要約 / Tier 1(原文未読)。単独の要約経由 | 取得 |
| FY2026 利益ガイダンス(2026-07-29) | non-GAAP 粗利率79〜81%、non-GAAP 営業利益率35〜37%、non-GAAP EPS 3.41〜3.47ドル(希薄化後株数7億4,100万〜7億4,500万株) | 転記([Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-fortinet-tops-q2-2026-forecasts-and-shares-jump-93CH-4821909)、[Benzinga](https://www.benzinga.com/analyst-stock-ratings/price-target/26/07/60794454/these-analysts-boost-their-forecasts-on-fortinet-following-upbeat-q2-earnings)) / Tier 3 | 取得 |
| 2026 Q3 売上ガイダンス | 20億1,000万〜21億ドル | Fortinet IR プレスリリースの要約 / Tier 1 | 取得 |
| FY2026 billings ガイダンス(期初、2026-02-05) | 84億〜86億ドル(約13%増)。粗利率80〜81%、営業利益率30〜32%の要約 | [Vectorshift](https://vectorshift.ai/research/companies/fortinet/earnings/2025-q4) / Tier 4・**単独出典**。根拠となる [SEC 8-K](https://www.sec.gov/Archives/edgar/data/1262039/000126203926000003/ftntq4-2025ex991.htm) は未読。営業利益率が GAAP か non-GAAP かは未確定 | 部分 |
| 中期目標 | 「今後3〜5年で複利成長12%」(2025年8月時点で維持。指標は売上か billings か未確認) | [Barchart/Yahoo の転載要約](https://finance.yahoo.com/news/analysts-cut-fortinet-rating-shares-152147416.html) / Tier 3 | 部分 |
| 中期の営業利益率目標、SASE・SecOps の売上目標 | - | - | **欠損** |

**期初 vs 現在のガイダンス(billings)**: 84〜86億 → 93.5〜95.5億ドル。中央値は85億 → 94.5億で約11%の上方修正(逆算)。
FY2025 実績75.5億ドルに対し、期初は+13%、現在は+25%(中央値、逆算)。2025年8月の「中期12%成長」は実績から大きく外れた。

### A-3. ピース一覧

| ピース | 目的(会社の説明) | 発表日 | 規模・進捗の数値 | 出典 / Tier |
|---|---|---|---|---|
| 2026年のサポート終了(更新)対象 | 更新需要の源泉 | 2025-08 | 約65万台が2026年に終了、2027年に低価格帯約35万台が続く。2025年Q2末で2026年分の40〜50%が進捗。KeyBanc は更新機会を4億〜4億5,000万ドルと見積もった(当初) | [Barchart](https://www.barchart.com/story/news/34071991/fortinet-stock-is-plunging-on-refresh-cycle-woes-should-you-buy-the-ftnt-dip)、[The Stack](https://www.thestack.technology/fortinets-one-million-end-of-life-firewalls-has-investors-freaking-out-a-bit/) / Tier 3。2026年の進捗の更新値は欠損 |
| 次世代チップ SP6(Intel と協業) | 暗号化通信の検査、侵入防止、AI 脅威検知を担う Fortinet 固有のASIC。設計・パッケージ・製造に Intel の力を使う | **2026-07-21**(両社発表。2026-07-29 の Q2 決算でも言及) | Intel の製造ノード「Intel 4」を使う(最先端の18Aではない)。Intel 4 の初の外部ファウンドリ顧客。出荷時期は後日発表。契約額・ウェハ量は非開示。他の自社チップにも広げ得る | [SiliconANGLE](https://siliconangle.com/2026/07/21/intel-manufacture-firewall-chips-fortinet/)、[The Register](https://www.theregister.com/systems/2026/07/21/intel-fortifies-foundry-with-an-actual-customer-fortinet/5275374)、[Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/intel-4-gets-its-first-foundry-customer-in-fortinet-three-years-after-intel-scoped-the-node-to-meteor-lake) / Tier 3 |
| 次世代チップ SP5 | SP6 の前世代 | - | 詳細は欠損 | - |
| 新ファイアウォール FortiGate 3500G / 400G | 従来世代より性能を大きく向上 | 2026-05-06 | 性能値は欠損 | Q1説明会の要約 / Tier 3 |
| FortiOS 8.0 と価格改定 | 「コンバージェンス(融合)」戦略の再確認 | 2026(Accelerate 2026) | 内容は欠損 | [Yahoo 見出し](https://finance.yahoo.com/news/fortinet-reaffirms-convergence-strategy-accelerate-004438576.html) / Tier 3 |
| 価格改定(list price) | 部品(メモリ)コストの転嫁 | 2026-03-02 発効 | 一部製品で約5〜20%(パートナーのブログ。局所的にはさらに大きい例も)。既存見積は30日有効。更新・サポートにも適用との記述 | [ST Digital](https://st.digital/en/blog/st-digital-s-blog-1/new-fortinet-pricing-grid-what-changes-on-march-2-2026-527) / Tier 4 |
| SD-WAN+SASE のサービス束 | 採用拡大とサービス売上の底上げ | 2026-05 | 数値は欠損 | Q1説明会 / Tier 3 |
| 信用格付け | Moody's が Baa1 から A3 に引き上げ | 2026-07-29 | A3 | Fortinet IR 要約 / Tier 1 |
| 買収(Lacework、Next DLP 等) | - | - | **欠損** | - |
| データセンター・本社の不動産投資(capex) | - | - | **欠損** | - |
| 自社株買い | - | - | **欠損**(決算書は [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001262039/000126203926000021/ftnt-20260630.htm) に所在あり、未読) | - |

### A-4. 過去3年のガイダンス達成状況

| 時期 | 事実 | 経営陣の説明 | 出典 / Tier |
|---|---|---|---|
| 2023年11月(Q3 2023) | 第4四半期の billings と売上の見通しがアナリスト予想を下回り、株価は寄り付き前に約18〜23%下落(出典で幅)。billings は予想未達。TD Cowen のアナリストは、機器売上が上場以来初めて前年を下回った点を指摘 | Ken Xie: 2年間の高成長のあと、需要が正常な水準に戻った | [Investing.com](https://www.investing.com/news/stock-market-news/fortinet-plunges-18-on-lowered-fullyear-guidance-432SI-3220172)、[News on Invest](https://newsoninvest.com/fortinet-plunges-as-network-firewall-market-turns-down/) / Tier 3 |
| 2024年〜2025年初め | 「消化(digestion)」の時期。前年の billings はマイナス(Ohlgart) | 2026年に Ken Xie が振り返って説明 | Q1 2026 説明会の要約 / Tier 3。**2024年のガイダンス vs 実績は欠損** |
| 2025年8月(Q2 2025) | 売上16億3,000万ドルは予想並み、調整後EPS 0.64ドルは予想0.59ドルを上回った。第3四半期の売上ガイダンス16億7,000万〜17億3,000万ドルの中央値が予想17億1,000万ドルを下回り、株価は8月7日に20%超下落。通期 billings 見通しは73億3,000万〜74億8,000万ドルに引き上げ | §A-1 の更新サイクル説明 | [Yahoo](https://finance.yahoo.com/news/analysts-cut-fortinet-rating-shares-152147416.html)、[Seeking Alpha](https://seekingalpha.com/news/4481339-fortinet-receives-swath-of-downgrades-on-firewall-refresh-revelation) / Tier 3 |
| 2025年通期 | billings 実績75億5,000万ドル(+16%)。上記の見通しの上限74億8,000万ドルを約1%上回った。FCF 22億1,000万ドル | - | [Barchart(会社PR転載)](https://www.barchart.com/story/news/57297/fortinet-reports-strong-fourth-quarter-and-full-year-2025-financial-results) / Tier 1 転載 |
| 2026年 | 期初 billings 84〜86億ドル(単独出典)→ Q1 で売上ガイダンスを引き上げ → Q2 で売上19%増・billings 93.5〜95.5億ドルに引き上げ | - | §A-2 |

- 達成傾向(取得範囲内): 2025年第4四半期以降は、直近のガイダンスを上回る実績が続いた(2025年第4四半期の billings、2026年 Q1・Q2 とも「ガイダンス上限超え」と報じられた。2025年第3四半期は本文未取得)。
  一方、2023年11月と2025年8月は、好決算でも「次の期のガイダンス」と「需要の持続性の説明」で株価が20%前後下落した。
- **欠損**: 2023〜2024年の期初 vs 実績の表。2024年2月(Q4 2023)の株価反応は検索結果に出ず未確認。

### A-5. 経営陣の経歴・在任・報酬

- 役員(2026年の委任状説明書 DEF 14A が対象とする 2025年の主要役員5名): Ken Xie(CEO・会長・創業者)、Michael Xie(社長兼CTO)、Christiane Ohlgart(CFO)、Keith Jensen(前CFO)、John Whittle(COO)。
  出典: [SEC DEF 14A(2026)](https://www.sec.gov/Archives/edgar/data/0001262039/000207709626000106/ea0287420-01.htm) の検索要約 / Tier 1(原文未読)。
- CFO が Keith Jensen から Christiane Ohlgart に替わった。交代時期は未確認。
- 報酬: 委任状説明書は「業績連動」を掲げ、業績指標を含む。**個別の KPI(売上、営業利益、1株当たり指標か総額か)は欠損**。
  [Gloom(第三者の要約)](https://gloom.sh/stocks/ftnt/proxy/2026)は、Ken Xie の2025年の報酬総額を約1,150万ドル(前年比約13%減、約89%が株式報酬)、CEO と従業員中央値の報酬比を約75対1としている(Tier 4・要検証)。
- 創業者経営の経歴の詳細は欠損。

---

## B. 市場の仮説の出典

### B-1. 決算説明会でアナリストが繰り返した質問

| 説明会 | 質問の主題(アナリスト名は転記から特定できず) | 出典 / Tier |
|---|---|---|
| Q2 2026(2026-07-29) | (1) 部品コスト上昇を背景にした価格改定が、下期の製品成長にどう効くか(CFO: 1桁後半%を織り込み済み)。(2) 顧客は Fortinet を PANW や CRWD のようなプラットフォームと見ているか(CFO: 妥当な見方)。(3) OT の成長は持続するか(OT billings は+56%)。(4) Intel との協業は ASIC 開発・収益性にどう効くか | [Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/08/07/fortinet-ftnt-q2-2026-earnings-call-transcript/)、[Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-fortinet-tops-q2-2026-forecasts-and-shares-jump-93CH-4821909) の要約 / Tier 3 |
| Q1 2026(2026-05-06) | 新ファイアウォール群(3500G・400G)の展開が優先事項か、先食い・チャネル在庫(Ken Xie が「あまり見えない」と回答) | Q1説明会の要約 / Tier 3。質疑の全体は欠損 |
| 2025年8月(参考) | 更新サイクルの残り(40〜50%進捗)、更新を除く製品売上の伸び | Tier 3 |

**読み取り**: 関心は「更新サイクルの先」(価格・ASP・チャネル在庫)から、「プラットフォームとしての評価」(SASE・SecOps・OT)に移っている。

### B-2. 強気派と弱気派の主要論点

**強気派(2026年)**

| 証券会社・アナリスト | 格付け・目標株価 | 論拠 | 出典 / Tier |
|---|---|---|---|
| BTIG、Gray Powell | Buy。目標を186ドル → 203ドル(2026年7月、Q2後) | Q2 の billings・売上の上振れ、通期ガイダンス引き上げ(論拠の細部は欠損) | [Benzinga](https://www.benzinga.com/analyst-stock-ratings/price-target/26/07/60794454/these-analysts-boost-their-forecasts-on-fortinet-following-upbeat-q2-earnings) / Tier 3 |
| TD Cowen | Buy。目標215ドル(「強い需要」を理由に引き上げ。日付は未確認、9月に再確認との記述) | 強い需要 | [Investing.com](https://www.investing.com/news/analyst-ratings/td-cowen-raises-fortinet-stock-price-target-to-215-on-strong-demand-93CH-4787788) / Tier 3 |
| Freedom Broker(2025年) | Buy を維持(目標は引き下げ) | 経営陣の成長見通しへの信頼 | [Morgan Stanley 記事周辺の要約](https://www.investing.com/news/analyst-ratings/morgan-stanley-downgrades-fortinet-stock-on-firewall-refresh-concerns-93CH-4218623) / Tier 3 |
| (参考)Barclays、Saket Kalia | 中立(Equal-Weight)。目標170 → 190ドル | 目標引き上げだが格付けは中立 | Benzinga / Tier 3 |
| (参考)Bernstein | 中立(Market Perform)。目標102 → 145ドル(2026-09-17、TipRanks 要約) | 目標引き上げだが現株価を下回る | [TipRanks](https://www.tipranks.com/stocks/ftnt) の要約 / Tier 3 |

- 強気の具体名は 2026年で BTIG と TD Cowen の2件。要件の3件には届かない。
- 報道の論調(Q1後): 「AIセキュリティ需要が焦点に戻った」([ts2.tech](https://ts2.tech/en/fortinet-stock-surges-12-as-q1-beat-and-2026-guidance-put-ai-security-demand-back-in-focus/))、「第1四半期は予想を大きく上回りガイダンスを引き上げ」([Seeking Alpha](https://seekingalpha.com/news/4587479-fortinet-rockets-after-q1-results-and-guidance-blast-expectations)、[SiliconANGLE](https://siliconangle.com/2026/05/06/fortinet-shares-surge-first-quarter-earnings-beat-raised-outlook/))。Q2後も「株価は過去最高値圏」と報じられた([ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/fortinet-inc-stock-trades-near-record-high-as-analysts-back-innovation-push/70109912) / Tier 4)。

**弱気派・慎重派(2025年の格下げと2026年の論調)**

| 証券会社 | 内容 | 論拠 | 出典 / Tier |
|---|---|---|---|
| KeyBanc(2025-08) | Overweight → Sector Weight に格下げ | 更新を除く製品売上は2025年上期に横ばいから減少。更新機会は当初の4億〜4億5,000万ドルほど大きくない可能性。2026年は利益率の圧縮も懸念 | [Yahoo](https://finance.yahoo.com/news/analysts-cut-fortinet-rating-shares-152147416.html)、[TipRanks/TheFly](https://www.tipranks.com/news/the-fly/fortinet-downgraded-to-sector-weight-from-overweight-at-keybanc-thefly) / Tier 3 |
| Morgan Stanley(2025-08 → 2025-09) | Overweight → Equal-weight → 9月に Underweight、目標67ドル | 更新サイクルが想定より小さければ2026・2027年の予想が下がる。更新後は1桁後半の成長企業になり得るのに、FCF倍率が20倍台前半〜半ば | [Investing.com](https://www.investing.com/news/analyst-ratings/morgan-stanley-downgrades-fortinet-stock-on-firewall-refresh-concerns-93CH-4218623) / Tier 3 |
| Piper Sandler(2025-08) | Neutral に格下げ | 「複数四半期にわたって実績を見る局面(show-me)」 | [Yahoo](https://finance.yahoo.com/news/analysts-cut-fortinet-rating-shares-152147416.html) / Tier 3 |
| Wedbush(2026年) | 株価は強い年初来の上昇で、すでに最良のシナリオを織り込んでいるという見方(アナリスト名・時期は未確認) | 評価の高さ | ad-hoc-news 系の検索要約 / Tier 4 |
| Wedbush(2026-01) | メモリ価格の高騰でファイアウォールの価格が上がり、Fortinet・Check Point・PANW はコスト転嫁で最も苦労し得る | 部品コスト | [The Register](https://www.theregister.com/2026/01/12/no_fire_sale_on_firewalls/) / Tier 3 |
| Wells Fargo、Mizuho | 「Underweight または類似」との記述 | 未確認(1件の要約のみ) | Tier 4・要確認 |

- 慎重派の中核論点: ①「更新サイクルを除く製品の伸びは弱い」②「サイクルは前半に集中し、ピークを過ぎる」③「ハードウェア依存の戻りは限られる」
  ([Simply Wall St](https://simplywall.st/stocks/us/software/nasdaq-ftnt/fortinet/future) の見出し: "Hardware Exposure And Softer 2026 Refresh Cycle Will Pressure Returns" / Tier 4)。
  Yahoo の分析は、Q1後も「ハードウェアの更新サイクルへの依存と、サイクル後の製品成長の鈍化リスクは未解決」と指摘([Yahoo](https://finance.yahoo.com/markets/stocks/articles/why-fortinet-ftnt-6-7-131919576.html) / Tier 3〜4)。
- **コンセンサス**: 集計元と時点によって異なる。MarketBeat は Hold、平均目標155.37ドル(高215・低80、38人)。StockAnalysis は Hold、164.32ドル(44人)。TipRanks は170.59ドル(31人)。別の集計は150.91ドル(低104・高220)。
  平均目標が現株価(§B-5)を下回る状態が続いている。
- **「ハードウェア企業=景気循環株」の見方**: 「景気循環株」という語そのものは出典に出ない。ただし、同じ構造を示す語は多い。
  ①2023年11月: 機器売上が上場以来初めて前年割れ、需要の「正常化」。②2025年8月: 「更新サイクル(リフレッシュ)」で株価が20%超下落。
  ③Morgan Stanley: 更新後は「1桁後半の成長」になり得るとして倍率に疑問。つまり市場は、機器を**周期的な更新需要**として見る。

### B-3. 空売りレポート・著名な弱気論者

- 空売りレポートは検索結果に出なかった(欠損)。
- 近い性質の主張: 米国の投資家訴訟の訴状(Robbins Geller)は、更新サイクルの規模と時期が過大に伝えられたと主張している([訴状 PDF](https://www.rgrdlaw.com/assets/htmldocuments/Fortinet/complaint.pdf) / 原告の主張であり事実認定ではない。事件の現状は未確認)。会社の反論は欠損。

### B-4. 報道のナラティブ

- 2025年8月: 「更新サイクルの不発」「更新の"啓示"で格下げが相次ぐ」(Seeking Alpha)。「投資家の欺瞞か記録的な更新成長か」という論調も一部あり([TradingView/11thestate](https://tr.tradingview.com/news/11thestate%3A334c67d83094b%3A0-fortinet-s-record-refresh-cycle-growth-story-or-investor-deception))。
- 2026年2月のAI懸念: Anthropic が 2026-02-19〜20 に「Claude Code Security」(コードの脆弱性を自動で探し修正案を出す道具)を公開し、セキュリティ株が急落。CrowdStrike は約11.6%安、Zscaler は約11.3%安、PANW は約3.2%安(ある報道)。**Fortinet の下落率は出典に出ない**。
  Baird の Shrenik Kothari は「パニック主導の物語先行の売り」、Wedbush は「過剰反応」、Hargreaves Lansdown は「対象は応用ソフトの安全性検査という小さな領域で、エンドポイント・ネットワーク・クラウドの実行時基盤は代替しにくい」と評した。2月4日の Claude Cowork 公開後にはソフトウェア株全般が下落し「SaaSpocalypse」と呼ばれた。
  出典: [Benzinga](https://www.benzinga.com/markets/tech/26/02/50834000/cybersecurity-stocks-fall-anthropic-claude-code-security-buy-opportunity)、[Yahoo/Proactive](https://finance.yahoo.com/news/anthropic-claude-code-security-launch-200400637.html) / Tier 3。
  **含意(事実のみ)**: AI 代替懸念の対象は主にコード検査やソフトウェア全般で、物理機器とASICを持つ Fortinet が同じ売りを受けたかは未確認。
- 2026年5月以降: 「AIセキュリティ需要が戻った」「ガイダンスが予想を大きく上回る」。Q2後は「株価は過去最高値圏」。

### B-5. 株価の推移の要点(直近1年+過去の大きな下落)

| 時期 | イベント | 値動き(出典間で幅) | 理由 | 出典 / Tier |
|---|---|---|---|---|
| 2023-11 | Q3 2023 決算 | 約-18〜-23% | §A-4 | Tier 3 |
| 2025-08-07 | Q2 2025 決算 | 約-12%(時間外)〜-26%(日中)。8月7日の終値は20%超下落との報道が多い | 更新サイクルが40〜50%進捗と判明。Q3売上ガイダンス中央値が予想未達。KeyBanc・MS・Piper が格下げ | [Yahoo](https://finance.yahoo.com/news/analysts-cut-fortinet-rating-shares-152147416.html)、[Invezz](https://invezz.com/news/2025/08/07/fortinet-stock-plunges-25-despite-strong-q2-earnings-analysts-point-to-this-red-flag/)、[IndexBox](https://www.indexbox.io/blog/fortinet-stock-drops-20-due-to-firewall-upgrade-concerns/) / Tier 3 |
| 2025-09 | Morgan Stanley が Underweight、目標67ドル | - | §B-2 | Tier 3 |
| 2025-11・2026-02 | Q3・Q4 2025 決算 | 小幅下落(見出し「株価は小幅安」) | 本文未取得 | [Investing.com Q3](https://www.investing.com/news/transcripts/earnings-call-transcript-fortinet-beats-q3-2025-forecasts-stock-dips-93CH-4335830)、[Q4](https://www.investing.com/news/transcripts/earnings-call-transcript-fortinet-q4-2025-beats-eps-forecasts-stock-dips-93CH-4489180) / Tier 3 |
| 2026-02 | AI 代替懸念の急落(Claude Code Security) | Fortinet の値は欠損 | §B-4 | Tier 3 |
| 2026-05-06 | Q1 2026 決算 | **約+12%〜+21%**(StockTitan は当日+20.0%、Alpha Spread は朝方+21%超・約109ドル、ts2.tech は+12%、Yahoo は+6.7%(期間不明))。確定終値は未確認 | billings 31%増(単独出典)、製品売上+41%、FCF 10億ドル、ガイダンス引き上げ | [StockTitan](https://www.stocktitan.net/news/FTNT/fortinet-reports-strong-first-quarter-2026-financial-aiqf1lc64cd7.html)、[Alpha Spread](https://www.alphaspread.com/market-news/earnings/fortinet-stock-jumps-after-q1-earnings-beat-and-higher-2026-outlook) / Tier 3〜4 |
| 2026-07-21 | Intel との SP6 発表 | Intel 株は約+5%(Fortinet 側は欠損) | §A-3 | [BigGo](https://finance.biggo.com/news/e8b7bd02-86a7-4394-af8f-1e27cd69eb34) / Tier 4 |
| 2026-07-29/30 | Q2 2026 決算 | 「株価は急伸」。+8.8%の記述あり(期間不明) | 売上26%増、製品52%増、ガイダンス引き上げ | [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-fortinet-tops-q2-2026-forecasts-and-shares-jump-93CH-4821909)、[Yahoo](https://finance.yahoo.com/technology/ai/articles/fortinet-ftnt-8-8-raising-091220169.html) / Tier 3 |
| 2026-09 | 水準 | 9月15日終値172.37ドル、9月18日終値169.41ドルで「過去最高値の直下」との記述(ad-hoc-news 系、Tier 4)。一方 StockAnalysis は「直近の株価は約189ドル、52週高値は192.41ドル」(日付不明) | - | [StockAnalysis](https://stockanalysis.com/stocks/ftnt/) / Tier 3〜4 |

- **未確定**: 現在の株価水準(約170ドルか約190ドルか)は出典間で食い違い、2026-10-09 の終値は取れていない。株価は別担当の値を使うこと。
- 参考の並び: 2025年9月の Morgan Stanley の目標67ドル、2026年5月の約109ドル(Alpha Spread)、2026年9月の約170〜190ドル。時点と種類(目標・日中値・終値)が異なるため厳密な比較ではないが、2025年8月の急落後から2026年9月までに株価が大きく上昇したことは確かである。

---

## C. 一次情報(スカットルバット)

| # | 観察 | 内容 | 構造仮説との関係 | 出典 / Tier |
|---|---|---|---|---|
| C-1 | Gartner マジック・クアドラント(HMF) | Fortinet は 2025年に新設された「ハイブリッド・メッシュ・ファイアウォール」の Gartner MQ で**リーダー**。「実行能力(Ability to Execute)」で最高位と会社が主張。Gartner の MQ は計12本でリーダー評価と会社が記載。2026年版の HMF MQ(2026-09-07)が Fortinet の分析資料ページに載るとの記述あり(未検証)。SDxCentral によれば、ネットワーク・ファイアウォールの MQ のリーダーは Fortinet・PANW・Check Point(版の年次は要確認) | 機器+SASE+SD-WAN の一体化が第三者評価で裏付けられるか | [Fortinet IR](https://investor.fortinet.com/news-releases/news-release-details/fortinet-named-leader-2025-gartnerr-magic-quadranttm-hybrid-mesh)(Tier 1・自社発表)、[SDxCentral](https://www.sdxcentral.com/news/fortinet-palo-alto-networks-top-gartners-hybrid-mesh-firewall-rankings/)(Tier 3) |
| C-2 | 価格改定 | 2026-03-02 に list price を一部製品で約5〜20%引き上げ(パートナーのブログ)。Q2説明会では「価格をほぼ即時に調整」「下期 billings に1桁後半%を織り込み」(経営陣) | ASP と製品売上の加速の一因。価格転嫁力の証拠 | [ST Digital](https://st.digital/en/blog/st-digital-s-blog-1/new-fortinet-pricing-grid-what-changes-on-march-2-2026-527)(Tier 4)、Q2説明会(Tier 3) |
| C-3 | 半導体(メモリ)の調達・価格 | DRAM 不足で、Wedbush はファイアウォールのコスト上昇を予想し、Fortinet・Check Point・PANW が最も影響を受け得ると指摘(2026-01)。Fortinet の粗利率は以前から低下傾向と報じられた。TrendForce は 2026年第4四半期のDRAM契約価格を前期比+10〜15%、供給逼迫は2027年まで続くと予測(2026-09-30) | 価格改定の背景。粗利率ガイダンス(79〜81%)の下振れ要因 | [The Register](https://www.theregister.com/2026/01/12/no_fire_sale_on_firewalls/)(Tier 3)、[TrendForce](https://www.trendforce.com/presscenter/news/20260930-13258.html)(Tier 3) |
| C-4 | チャネル在庫・登録期間 | サービス登録の期限を最長1年から90日に短縮し、在庫積み増しの誘因を減らした(Ken Xie、Goldman 講演)。TIKR はQ1にチャネル在庫は横ばいで、成長は再在庫でなく需要だったと分析 | 2021〜22年型の先食い・在庫調整の再発を防ぐ統制 | [Investing.com](https://www.investing.com/news/transcripts/fortinet-at-goldman-sachs-conference-ai-security-drives-growth-93CH-4892267)(Tier 3)、[TIKR](https://www.tikr.com/blog/why-fortinet-stock-could-fall-even-as-ai-demand-accelerates)(Tier 4) |
| C-5 | IDC の出荷シェア | **欠損**。「FortiGate がグローバルで50%超」と書くブログはあるが、IDC 自身のデータではなく単独の二次情報(使用不可) | - | - |
| C-6 | チャネル(ディストリビューター)の声、求人 | **欠損** | - | - |
| C-7 | 競合の開示で FTNT に触れたもの、業界統計の市場規模 | **欠損** | - | - |

**既知の制約として記載が必要**: C-1(自社発表、Gartner 原文は未読)、C-2(パートナーのブログ)、C-3(報道)はいずれも二次的な観察で、
顧客・流通側の声(C-6)と出荷シェア(C-5)は取れていない。構造仮説の裏付けとしては弱い。

---

## D. 競争と業界の構造

- **ファイアウォール市場の成熟度と更新需要**: 機器は5年程度の周期で更新される。Fortinet の説明では、2026年の対象約65万台、2027年は低価格帯約35万台(§A-3)。
  市場は「更新サイクルのピーク」を懸念した(§B-2)が、2026年上期の製品売上は+41%(Q1)、+52%(Q2)と加速した。
- **SASE が既存機器需要を食う程度**: 食う度合いを測る第三者データは欠損。会社は「SASE ファイアウォール」という名で、**機器とクラウドを同じ基盤に束ねる**方針をとり(Ken Xie: 約20年前のNGFW移行に匹敵)、
  SASE と Secure Networking の billings が同時に伸びている(Q2: Unified SASE +35%、Secure Networking +34%)。食い合いよりも抱き合わせとして語られている。
- **価格競争**: メモリ高騰で業界全体の機器価格が上がる局面(Wedbush)。値上げが需要に与える影響は、Fortinet の下期見通しに織り込まれた(1桁後半%)。競合の値動きは欠損。
- **競合**: Gartner の HMF/ネットワーク・ファイアウォール MQ のリーダーは Fortinet・PANW・Check Point(C-1)。競合の開示で Fortinet に触れたものは欠損。
- **中小企業向けの強さ**: 欠損(2027年の群が「低価格帯」という説明のみ)。
- **セキュリティ予算の動向**: 欠損。

---

## E. 異常値の候補(市場のナラティブと合わない数字)

「逆算」は私の計算(前回版の再掲を含む)。数値の出典は §A、§J。

| # | 異常値の候補 | 数値と出典 | 問い(答えは未調査) |
|---|---|---|---|
| E-1 | **製品売上の急加速** | Q1 2026 +41%(6億4,500万ドル)、Q2 2026 +52%(7億7,300万ドル。前年同期は逆算で約5億900万ドル)。2025年8月に「更新は40〜50%進捗」で株価が20%超下落した | 更新が半分まで進んだと言った1年後に、なぜ製品が+52%なのか。残りの更新が前倒しされたのか、ASPが上がったのか、AI需要が足されたのか |
| E-2 | **下期のサービス売上の遅れと billings の乖離** | 売上成長 +15%(Q4 2025)→ +20%(Q1)→ +26%(Q2)。billings +18% → +31% → +33%。サービス売上は Q2 +14%。経営陣は「サービスは下期に上向く」と説明 | なぜサービスは製品に1年近く遅れるのか(前年の billings マイナスが付帯率を下げた、との CFO 説明)。billings の伸びが売上に反映される時期はいつか |
| E-3 | **billings ガイダンスの大幅な上方修正** | 期初84〜86億ドル(単独出典)→ 93.5〜95.5億ドル(中央値で約11%上方)。2025年8月の「中期12%成長」と、2026年の billings ガイダンス+25%(逆算) | 年初のガイダンスが保守的だったのか、年中に需要の質が変わったのか |
| E-4 | **営業利益率の高さ** | Q1 non-GAAP 36%(GAAP 31%)、Q2 non-GAAP 38%(GAAP 34%)。FY2026 non-GAAP 営業利益率ガイダンスは35〜37%。年初の目標30〜32%(単独出典)。粗利率ガイダンスは79〜81% | メモリ高騰が粗利率を押し下げる局面で、なぜ営業利益率は上がるのか。ASP の上昇と製品比率が先に効いたのか。ガイダンスの粗利率80〜81% → 79〜81% の下限引き下げの意味は |
| E-5 | **FCF が non-GAAP 営業利益を上回る** | Q2 FCF 9億6,600万ドル(営業CF 10億4,000万ドル)。Q2 non-GAAP 営業利益は概算約7億8,000万ドル(売上20億5,000万ドル×38%)。Q1 FCF は10億1,000万ドル(単独出典)。上半期 FCF は約19億8,000万ドルで、FY2025 通期の22億1,000万ドルに迫る | なぜ現金が利益を上回るのか(繰延収益の前受け、税の時期、設備投資の時期)。持続するのか |
| E-6 | **OT の成長率の低下と評価** | OT billings: Q1 2026 +70%超 → Q2 2026 約+55〜56%。アナリストは OT の持続性を質問 | 成長の鈍化は母数の拡大か、特定案件の一巡か |
| E-7 | **平均目標が株価を下回るコンセンサス** | コンセンサス Hold、平均目標約151〜171ドル(§B-2)に対し、株価は約170〜190ドルと報じられる。主要な2025年の弱気(KeyBanc・MS・Piper)の現在の格付けは未確認 | 市場は「更新の先」を信じて買っているのか、アナリストが追随していないだけか |
| E-8 | **重大脆弱性の頻発と成長の両立** | 2025-12 〜 2026-07 に少なくとも4件の悪用事案(§G)。それでも billings は+31〜33% | 脆弱性は買い替え・更新を促す側に働くのか(パッチ適用のための入れ替え)、顧客離れの先行指標なのか |
| E-9 | **通期ガイダンスと半期実績の関係** | FY2026 売上ガイダンス中央値は約81億ドル。H1 約39億ドル(Q1 約18億5,000万ドルは単独出典)を引くと H2 は約42億ドル。Q3 ガイダンス中央値は約20億5,500万ドルで Q2 実績とほぼ同水準。Q3 から逆算した Q4 は約21億4,500万ドル。billings ガイダンス中央値94.5億ドルから H1(約44億6,000万ドル)を引くと H2 は約49億9,000万ドル(いずれも逆算) | 第3四半期が前四半期とほぼ横ばいなのは保守的か、需要の前倒しの反動を見込むのか。non-GAAP 営業利益率の通期35〜37%に対し H1 実績は約37%で、H2 は35%前後に下がる設計なのはなぜか |

---

## F. 条件9(AIの停めない運用)に関わる事実

| 事実 | 出典 / Tier | 状態 |
|---|---|---|
| Ken Xie: 長期成長を「AI主導のセキュリティ需要」と結びつけた(2026 Q2)。AIはトラフィックを増やし、ネットワークとセキュリティの融合を加速する。機械同士の通信が人間の通信を上回った | [Allmind](https://allmind.ai/earnings/event/2937992)(Tier 4)、Q2説明会の要約(Tier 3) | 取得(定量値なし) |
| Ohlgart: 製品の成長を、AI ワークロードに備える顧客の更新に結びつけた(準備原稿の要約) | Fortinet IR 準備原稿の要約 / Tier 1 | 部分(要原文確認) |
| SecOps は「20を超えるAI対応ソリューション」。SecOps billings は Q1 +23%、Q2 +25% | Q1・Q2説明会 / Tier 3 | 取得 |
| SP6 は暗号化通信の検査、侵入防止、AI脅威検知を担う。報道は SP6 と AI データセンター需要の関係を明示していない(「消費電力・冷却の低減」は分析者の推測) | [The Register](https://www.theregister.com/systems/2026/07/21/intel-fortifies-foundry-with-an-actual-customer-fortinet/5275374) / Tier 3 | 取得 |
| 「AIに特化した新ファイアウォールを投入」との見出し(2026年Q2直後) | [Yahoo](https://finance.yahoo.com/technology/ai/articles/fortinet-ftnt-8-8-raising-091220169.html) の見出しのみ / Tier 3 | 見出しのみ |
| AIデータセンター向けの高速ファイアウォール需要の売上、AIを守る製品の売上 | - | **欠損(開示値なし)** |

---

## G. リスク事象

### G-1. 自社製品の重大脆弱性

| 時期 | 事象 | 内容 | 出典 / Tier |
|---|---|---|---|
| 2025-12 | FortiOS SSL VPN の2要素認証(2FA)回避の悪用 | Fortinet が悪用中と警告 | [The Hacker News](https://thehackernews.com/2025/12/fortinet-warns-of-active-exploitation.html) / Tier 3 |
| 2026-01-27/28 | CVE-2026-24858(FortiCloud SSO の認証バイパス、CVSS 9.4) | 2026年1月から悪用。CISA が KEV に追加 | [CISA](https://www.cisa.gov/news-events/alerts/2026/01/28/fortinet-releases-guidance-address-ongoing-exploitation-authentication-bypass-vulnerability-cve-2026) / Tier 2 |
| 2026-03 | 古い SSL VPN の脆弱性(CVE-2024-21762、CVE-2023-27997)が引き続き悪用 | 勧告に列挙 | [OP-C](https://op-c.net/blog/critical-fortinet-vulnerabilities-under-active-exploitation/) / Tier 4 |
| 2026-06 | 「FortiBleed」: インターネットに面した FortiGate の管理者認証情報の流出。報告で約7万4,000〜8万6,644台。CISA が緊急勧告(6/18 か 6/20、出典で不一致)。新たな脆弱性ではなく既定の認証情報の悪用との分析もある | [Cloud Security Alliance](https://labs.cloudsecurityalliance.org/research/csa-research-note-fortibleed-default-credentials-20260620-cs/) / Tier 4、[Penligent](https://www.penligent.ai/hackinglabs/fortibleed-cve/) / Tier 4 | 要原文確認 |
| 2026-07-28 | CVE-2025-68686(FortiOS の SSL VPN シンボリックリンク永続化のパッチ回避)が KEV に追加。連邦機関の対応期限は8月10日 | [Cybersecurity News](https://cybersecuritynews.com/fortinet-fortios-vulnerability-exploited/)、[FortiGuard PSIRT FG-IR-25-934](https://fortiguard.fortinet.com/psirt/FG-IR-25-934) / Tier 1・3 | 取得 |

- 頻度: 2025年12月〜2026年7月に、悪用が確認された事案が少なくとも4件。顧客への影響(被害件数、解約、補償)の定量値は欠損。

### G-2. 訴訟・規制・会計・株式売却

- **訴訟**: 2025年8月の株価急落を受け、更新サイクルの規模と時期を過大に伝えたとの投資家の訴え(訴状: [Robbins Geller](https://www.rgrdlaw.com/assets/htmldocuments/Fortinet/complaint.pdf) / 原告の主張)。事件番号・現状・会社の反論は欠損。
- **経営陣の株式売却**: Simply Wall St の見出し「最近の格下げとインサイダー売却は転機を示すか」([Simply Wall St](https://simplywall.st/stocks/us/software/nasdaq-ftnt/fortinet/news/do-recent-analyst-downgrades-and-insider-sales-hint-at-shift))があるが、売却者・数量・時期は欠損。
- **規制・会計上の論点**: 欠損。

---

## H. 出典間の食い違い・未確定事項

| 項目 | 食い違い | 暫定扱い |
|---|---|---|
| Q1 2026 売上 | 18億5,000万ドル(前年比20%増)と報じる記事。会社IR原文は未確認 | 単独出典。billings の20億9,000万ドルと混同しない |
| Q1 2026 billings | 20億9,000万ドル(31%増)とする集計サイトがある(サイト名は特定できず) | 単独出典 |
| Q1 2026 売上ガイダンス | 「1.5%」(Alpha Spread)と「約15%、最大78億7,000万ドル」(StockTitan) | 15%が妥当に見えるが未確認(Q2で19%に引き上げ済み) |
| Q1 2026 株価反応 | +6.7%、+12%、+20.0%、+21%超(約109ドル) | 確定終値は未確認 |
| 現在の株価水準 | 約169〜172ドル(9/15〜9/18の終値とする記述)vs 約189ドル・52週高値192.41ドル | 未確定。2026-10-09 終値は別担当 |
| 2025年8月の下落率 | 約12%(時間外)、20%超(8/7終値)、22%、26%(日中) | 「20%前後」とする |
| 2023年11月の下落率 | 約18%(見出し)と23%(本文) | 「18〜23%」とする |
| FortiSASE の導入率 | 準備原稿は「大企業の既存顧客の19%」、転記は「90%」 | 準備原稿の19%が妥当に見えるが原文未確認 |
| FY2026 営業利益率 | 期初30〜32%(単独出典)vs 現ガイダンス35〜37%(non-GAAP) | GAAP/non-GAAP の別を含め未確定 |
| コンセンサス目標株価 | 150.91〜170.59ドル(集計元で異なる) | 範囲で記録 |
| Bernstein の目標引き上げの日付 | 初回検索は日付なし、再検索で2026-09-17 | 後者を暫定採用 |
| FortiBleed の CISA 勧告日 | 6/18 と 6/20 | 未確定 |

## I. 検索予算が回復したときに実行する検索(優先順)

1. `Fortinet Q4 2025 earnings call Q&A refresh 2026 progress` / `Fortinet Q3 2025 earnings call transcript refresh halfway`
2. `Fortinet Investor Day analyst day long-term targets`、会社IR原文(`investor.fortinet.com` を allowed_domains に指定)
3. `Fortinet insider selling Form 4 Ken Xie 2026`、`Fortinet class action Robbins Geller case status`
4. `IDC worldwide quarterly security appliance tracker 2026 Fortinet share`、`Dell'Oro network security 2026`
5. `Gartner Magic Quadrant SD-WAN 2025 Fortinet`、`Gartner Magic Quadrant single-vendor SASE 2025 Fortinet`
6. `Fortinet distributor Exclusive Networks Ingram Micro Westcon 2026 channel inventory`
7. `Fortinet proxy statement 2026 annual incentive metrics billings operating income`
8. `Fortinet Lacework Next DLP acquisition`、`Fortinet share repurchase 2026`、`Fortinet capex 2026`
9. `Fortinet short interest short seller`、`Palo Alto Networks firewall Fortinet displacement 2026`、`Fortinet AI data center firewall demand`
10. `Fortinet Wells Fargo Mizuho Morgan Stanley rating October 2026`、`FTNT closing price October 9 2026`

## J. 出典一覧(取得日はすべて 2026-10-11)

| 区分 | 出典 | 日付 | Tier | 読了状況 |
|---|---|---|---|---|
| 決算(会社IR) | [Fortinet IR Q2 2026 プレスリリース](https://fortinet.gcs-web.com/static-files/e4ffcc79-194e-4ca3-9a69-8a51bd0a6314)、[mfn.se](https://mfn.se/one/a/fortinet/fortinet-reports-strong-second-quarter-2026-financial-results-c7dd36df) | 2026-07-29 | 1 | 要約のみ |
| 決算(会社IR) | [Fortinet IR Q2 2026 準備原稿](https://investor.fortinet.com/static-files/92543183-3383-4279-a3a4-13c7db91fcbb)、[Q2 2025 準備原稿](https://investor.fortinet.com/static-files/5a5d281a-78fa-4ec3-a23f-9305a187de2d) | 2026-07-29 / 2025-08 | 1 | 要約のみ |
| 決算(会社IR) | [SEC 8-K 別添99.1(Q4 2025)](https://www.sec.gov/Archives/edgar/data/1262039/000126203926000003/ftntq4-2025ex991.htm)、[Q1 10-Q](https://www.sec.gov/Archives/edgar/data/0001262039/000126203926000013/ftnt-20260331.htm)、[Q2 10-Q](https://www.sec.gov/Archives/edgar/data/0001262039/000126203926000021/ftnt-20260630.htm)、[DEF 14A](https://www.sec.gov/Archives/edgar/data/0001262039/000207709626000106/ea0287420-01.htm) | 2026 | 1 | URLのみ |
| 説明会の転記 | [Motley Fool Q2](https://www.fool.com/earnings/call-transcripts/2026/08/07/fortinet-ftnt-q2-2026-earnings-call-transcript/)、[Investing.com Q2](https://www.investing.com/news/transcripts/earnings-call-transcript-fortinet-tops-q2-2026-forecasts-and-shares-jump-93CH-4821909)、[Yahoo Q2](https://finance.yahoo.com/quote/FTNT/earnings/FTNT-Q2-2026-earnings_call-661676.html)、[Insider Monkey Q1](https://www.insidermonkey.com/blog/fortinet-inc-nasdaqftnt-q1-2026-earnings-call-transcript-1756043/)、[Motley Fool Q1](https://www.fool.com/earnings/call-transcripts/2026/05/06/fortinet-ftnt-q1-2026-earnings-transcript/)、[Investing.com Q1](https://www.investing.com/news/transcripts/earnings-call-transcript-fortinet-exceeds-q1-2026-forecasts-with-strong-growth-93CH-4665847)、[Goldman 講演](https://www.investing.com/news/transcripts/fortinet-at-goldman-sachs-conference-ai-security-drives-growth-93CH-4892267) | 2026-05〜08 | 3 | 要約のみ |
| 要約サイト | [Allmind](https://allmind.ai/earnings/event/2937992)、[Stock Taper](https://stocktaper.com/earningsCallSummary/FTNT/2026/Q2)、[Vectorshift](https://vectorshift.ai/research/companies/fortinet/earnings/2026-q2-summary)、[Vectorshift Q4](https://vectorshift.ai/research/companies/fortinet/earnings/2025-q4) | 2026 | 4 | 要約のみ |
| 2025年8月・2023年11月 | [Yahoo](https://finance.yahoo.com/news/analysts-cut-fortinet-rating-shares-152147416.html)、[Seeking Alpha](https://seekingalpha.com/news/4481339-fortinet-receives-swath-of-downgrades-on-firewall-refresh-revelation)、[Barchart](https://www.barchart.com/story/news/34071991/fortinet-stock-is-plunging-on-refresh-cycle-woes-should-you-buy-the-ftnt-dip)、[The Stack](https://www.thestack.technology/fortinets-one-million-end-of-life-firewalls-has-investors-freaking-out-a-bit/)、[SDxCentral](https://www.sdxcentral.com/news/fortinet-financials-float-sase-trajectory-and-firewall-fears/)、[Nasdaq/Zacks](https://www.nasdaq.com/articles/will-fortinets-firewall-upgrade-cycle-continue-power-top-line-growth)、[Investing.com: MS](https://www.investing.com/news/analyst-ratings/morgan-stanley-downgrades-fortinet-stock-on-firewall-refresh-concerns-93CH-4218623)、[Investing.com: 2023](https://www.investing.com/news/stock-market-news/fortinet-plunges-18-on-lowered-fullyear-guidance-432SI-3220172)、[News on Invest](https://newsoninvest.com/fortinet-plunges-as-network-firewall-market-turns-down/)、[Invezz](https://invezz.com/news/2025/08/07/fortinet-stock-plunges-25-despite-strong-q2-earnings-analysts-point-to-this-red-flag/)、[IndexBox](https://www.indexbox.io/blog/fortinet-stock-drops-20-due-to-firewall-upgrade-concerns/) | 2023-11 / 2025-08〜09 | 3 | 要約のみ |
| アナリスト・株価 2026 | [Benzinga](https://www.benzinga.com/analyst-stock-ratings/price-target/26/07/60794454/these-analysts-boost-their-forecasts-on-fortinet-following-upbeat-q2-earnings)、[TD Cowen](https://www.investing.com/news/analyst-ratings/td-cowen-raises-fortinet-stock-price-target-to-215-on-strong-demand-93CH-4787788)、[TipRanks](https://www.tipranks.com/stocks/ftnt)、[MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/FTNT/)、[StockAnalysis](https://stockanalysis.com/stocks/ftnt/)、[StockTitan Q1](https://www.stocktitan.net/news/FTNT/fortinet-reports-strong-first-quarter-2026-financial-aiqf1lc64cd7.html)、[Alpha Spread](https://www.alphaspread.com/market-news/earnings/fortinet-stock-jumps-after-q1-earnings-beat-and-higher-2026-outlook)、[SiliconANGLE Q1](https://siliconangle.com/2026/05/06/fortinet-shares-surge-first-quarter-earnings-beat-raised-outlook/)、[Simply Wall St](https://simplywall.st/stocks/us/software/nasdaq-ftnt/fortinet/future)、[ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/fortinet-inc-stock-trades-near-record-high-as-analysts-back-innovation-push/70109912) | 2026-05〜09 | 3〜4 | 要約のみ |
| AI 代替懸念 | [Benzinga](https://www.benzinga.com/markets/tech/26/02/50834000/cybersecurity-stocks-fall-anthropic-claude-code-security-buy-opportunity)、[Yahoo/Proactive](https://finance.yahoo.com/news/anthropic-claude-code-security-launch-200400637.html) | 2026-02 | 3 | 要約のみ |
| SP6・価格・メモリ | [SiliconANGLE](https://siliconangle.com/2026/07/21/intel-manufacture-firewall-chips-fortinet/)、[The Register: Intel](https://www.theregister.com/systems/2026/07/21/intel-fortifies-foundry-with-an-actual-customer-fortinet/5275374)、[The Register: DRAM](https://www.theregister.com/2026/01/12/no_fire_sale_on_firewalls/)、[ST Digital](https://st.digital/en/blog/st-digital-s-blog-1/new-fortinet-pricing-grid-what-changes-on-march-2-2026-527)、[TrendForce](https://www.trendforce.com/presscenter/news/20260930-13258.html) | 2026-01〜09 | 3〜4 | 要約のみ |
| Gartner | [Fortinet IR](https://investor.fortinet.com/news-releases/news-release-details/fortinet-named-leader-2025-gartnerr-magic-quadranttm-hybrid-mesh)、[SDxCentral](https://www.sdxcentral.com/news/fortinet-palo-alto-networks-top-gartners-hybrid-mesh-firewall-rankings/) | 2025-08-27 | 1・3 | 要約のみ |
| 脆弱性 | [CISA](https://www.cisa.gov/news-events/alerts/2026/01/28/fortinet-releases-guidance-address-ongoing-exploitation-authentication-bypass-vulnerability-cve-2026)、[FortiGuard PSIRT](https://fortiguard.fortinet.com/psirt/FG-IR-25-934)、[The Hacker News](https://thehackernews.com/2025/12/fortinet-warns-of-active-exploitation.html)、[Cybersecurity News](https://cybersecuritynews.com/fortinet-fortios-vulnerability-exploited/)、[CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-fortibleed-default-credentials-20260620-cs/) | 2025-12〜2026-07 | 1〜4 | 要約のみ |
| 訴訟 | [Robbins Geller 訴状](https://www.rgrdlaw.com/assets/htmldocuments/Fortinet/complaint.pdf) | 2025年下期 | 4(原告主張) | 要約のみ |
