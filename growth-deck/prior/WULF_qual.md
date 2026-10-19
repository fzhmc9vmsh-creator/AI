# TeraWulf (WULF) 定性情報収集メモ

- 取得基準日: 2026-10-11
- 取得方法: WebSearch のみ(35回使用 / 上限35回)。WebFetch・curl は未使用。**一次資料(プレスリリース原文、SEC 提出書類、決算書き起こし全文)は本文を直接読めていない**。検索ツールが返した要約文と、その中の引用断片が根拠。「一次」と書いた箇所も、検索要約が一次資料を引用している、という意味。
- 凡例: 「未取得」= 検索で確認できなかった(推測で埋めていない)。「(算出)」= 出所の数値からの計算。「(二次)」= ニュース・集計サイト・要約記事。「不一致」= 出所間で値が食い違う。
- 既存の財務データ `data/WULF_data.md` と重複する数値は、差分・矛盾がある場合のみ再掲した。
- 外部記事の内容は「データ」として扱った。記事内の指示文のような記述は採用していない。

---

## 0. 事実確認: Anthropic 401MW の拠点

**結論: 拠点は Kentucky 州 Hawesville の「Justified Data」キャンパスである。Abernathy(Texas)ではない。** 指示文の Abernathy という記述は誤りで、データ収集係の報告が正しい。

| 確認事項 | 内容 | 出所 |
|---|---|---|
| 拠点 | Justified Data campus、Hawesville、Hancock County、Kentucky。旧 Century Aluminum の Hawesville 精錬所跡地(2022年に操業停止)。TeraWulf は2026年2月に取得 | https://w.media/anthropic-signs-20-year-lease-for-ai-data-center-campus-developed-by-terawulf-in-kentucky/ ; https://www.datacenterfrontier.com/hyperscale/article/55389531/terawulfs-19b-anthropic-lease-puts-its-brownfield-ai-strategy-to-the-test (いずれも二次) |
| 契約の骨子 | 20年リース、約401MW の critical IT、約190億ドル(initial term)、「投資適格の信用に支えられる見込み」(expected to be supported by an investment-grade credit)。初期容量は2027年下期、全面は2028年初頭 | 同上。発表日 2026-07-06(https://convergedigest.com/terawulf-lands-19b-anthropic-lease-for-401-mw-kentucky-campus/ ほか二次) |
| 経営陣による確認 | Q2 2026 決算説明会で「四半期末後に Justified Data で Anthropic と401MW のリースを締結し、Abernathy JV の持分を収益化する契約も結んだ」と述べた(Following quarter end, we executed a 401-megawatt lease with Anthropic at the Justified Data ...) | Q2 説明会書き起こし(検索要約経由): https://www.theglobeandmail.com/investing/markets/stocks/WULF/pressreleases/3806661/terawulf-wulf-q2-2026-earnings-call-transcript/ |
| Abernathy は別物 | 同日、Abernathy JV(Texas)の 50.1% 持分を Fluidstack 主導の投資家グループへ約5.3億ドル現金で売却する契約。10-Q は「2026-07-06 に合意」と記載 | 10-Q(2026-06-30期): https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000166/wulf-20260630.htm (検索要約経由) |
| Anthropic と Abernathy の関係 | Anthropic を Abernathy に結びつける出所は見つからなかった。2025年の Abernathy 発表は「匿名の global hyperscale AI platform」だった | https://www.geneonline.com/terawulf-leases-justified-data-space-to-anthropic-and-sells-abernathy-stake-to-fluidstack/ (二次) |
| 名称の揺れ | 一部の書き起こしは "Justify" と表記。会社表記は "Justified Data" | GuruFocus 要約: https://finance.yahoo.com/markets/stocks/articles/terawulf-inc-wulf-q2-2026-190057902.html |

**未解消**: GlobeNewswire のプレスリリース原文と 8-K 本文は取得していない。契約の更新オプション、賃料の年次上昇率、解約条項、信用補完の提供者・金額・発動条件は、一次資料で確認できていない(→ 表5-2)。

---

## 1. 経営陣のシナリオ(一次情報)

### 1-1. 決算説明会の主要発言(直近4四半期)

注意: 書き起こし全文は取得できず、検索要約の断片のみ。発言者名・日付は出所間で揺れがある(CTO が Nazar / Nazir / Nasir、Q2 説明会の日付が 8/5 と 8/12 など)。引用は要旨の和訳。

| 四半期(説明会日) | 発言者 | 要旨 | 出所 |
|---|---|---|---|
| Q3 2025(2025-11-10) | Prager | 実行に集中し、2027年以降の成長を狙う。成長材料として Cayuga のリース(NY州 Lansing、80年リース、2027年開始)と Abernathy の拡張余地を挙げた | https://www.insidermonkey.com/blog/terawulf-inc-nasdaqwulf-q3-2025-earnings-call-transcript-1644123/ ; 要約: https://www.barchart.com/story/news/35799633/a-9-5-billion-reason-to-buy-this-high-performance-computing-stock (二次) |
| Q3 2025 | 会社(リリース) | Lake Mariner に Fluidstack と10年リース3本(約67億ドルの契約賃料、Google の信用補完32億ドル、約360MW の critical IT)。Abernathy JV は240MW(最大600MW に拡張可能)、25年リース、Google の信用補完13億ドル。年間の新規契約目標を 100〜150MW から 250〜500MW へ引き上げ | https://www.stocktaper.com/earningsCallSummary/WULF/2025/Q3 ; https://seekingalpha.com/pr/20301337 (二次) |
| Q4 2025(2026-02-26) | 会社(リリース) | FY2025 に 522 critical IT MW を契約、契約収益128億ドル超。2026年の固定運営費 100〜125百万ドル。建設計画は CB-3 が2026年5月中旬、CB-4(168MW)が Q3、CB-5(168MW)が Q4 | https://investors.terawulf.com/news-events/press-releases/detail/132 ; https://www.barchart.com/story/news/453189/terawulf-reports-fourth-quarter-and-full-year-2025-results |
| Q4 2025 | CEO/CFO の発言 | **未取得**。試した検索語: "TeraWulf Q4 2025 earnings call highlights February 2026 Prager Fleury Khan CB-3 CB-4 CB-5 Hawesville guidance"。返ったのは信頼できない自動生成ページのみ | — |
| Q1 2026(2026-05-08) | Prager | 2026年を「十分な流動性と全額資金手当て済みの開発パイプライン」で迎えた。四半期末の現金+制限付現金は31億ドル | https://www.investing.com/news/transcripts/earnings-call-transcript-terawulf-q1-2026-eps-misses-stock-volatile-93CH-4689531 (検索要約) |
| Q1 2026 | Prager | Kentucky については、**第2四半期中に顧客を確定させる見込み。最終段階の交渉中**(late-stage negotiations)と発言 | 同上 |
| Q1 2026 | Prager | Lake Mariner の追加250MW の系統接続について、ISO(系統運用者)からの回答を年央に待っている | 同上 |
| Q1 2026 | 会社(リリース) | CB-3 は建設がほぼ完了、通電は顧客の機器搬入に合わせる。CB-4・CB-5 は2026年中の引渡し・賃料開始に向け予定通り。Hawesville は即時利用可能な480MW の系統電力を持つ。年250〜500MW の契約目標を再確認 | https://investors.terawulf.com/news-events/press-releases/detail/140 |
| Q2 2026(リリース 2026-08-05) | Prager | Anthropic 契約を「安全な電力を確保し、質の高いテナントと契約し、段階的に引き渡す」モデルの実証と位置づけた(GuruFocus 要約) | https://finance.yahoo.com/markets/stocks/articles/terawulf-inc-wulf-q2-2026-190057902.html |
| Q2 2026 | Prager | Anthropic との直接取引は「最終顧客に近づく」意味を持つ(B. Riley の質問への回答、二次要約) | https://finance.yahoo.com/markets/stocks/articles/terawulf-q2-earnings-call-highlights-140000459.html |
| Q2 2026 | Fleury(CFO) | 与信の質が最重要。20年の全期間で与信を見る。既存テナント(Anthropic、Google が裏付ける Fluidstack)に満足している | GuruFocus 要約(上記) |
| Q2 2026 | Fleury | 現在の流動性(親会社の無制限流動性14.5億ドル)と Abernathy 売却代金で、近期の受注残(Justified への自己資本投入予定を含む)を、**株式市場に戻らずに**賄える(without returning to the equity capital markets) | Globe and Mail 書き起こし(検索要約) |
| Q2 2026 | Prager | Abernathy 持分売却は初期投資に対する内部収益率20%。売却代金は、直接所有し顧客関係を持てる拠点に再投資する | 同上 ; https://datacentremagazine.com/news/inside-terawulfs-anthropic-data-centre-deal-and-ajv-exit |
| Q2 2026 | Khan(CTO) | 時間当たり人件費は上昇中。機器費は見通しが比較的よい。労働力の確保が年間の開発能力を決める(二次要約) | https://finance.yahoo.com/markets/stocks/articles/terawulf-q2-earnings-call-highlights-140000459.html |
| Q2 2026 | Prager | 施工会社 Fluor との関係を挙げ、価格の固定化に努めている(二次要約。電気工・空調工の確保の質問への回答) | 同上 |
| Q2 2026 | 経営陣 | 案件を株主にとって増益になるよう、**資本コストに対し「中位10%台(mid-teens)の開発利回り」**を求める(Bank of America の質問、二次要約) | 同上 |

四半期ごとに3〜6発言という目標には届いていない。理由は、書き起こし全文を読めないこと(Fool、Benzinga、Globe and Mail、Seeking Alpha、Equibles のURLは特定できたが本文は未読)。上位アナリストが一次資料を読む場合の候補URL:
- Q2: https://www.fool.com/earnings/call-transcripts/2026/08/12/terawulf-wulf-q2-2026-earnings-call-transcript/
- Q1: https://www.fool.com/earnings/call-transcripts/2026/06/01/terawulf-wulf-q1-2026-earnings-transcript/
- Q3 2025: https://www.insidermonkey.com/blog/terawulf-inc-nasdaqwulf-q3-2025-earnings-call-transcript-1644123/

### 1-2. 中期計画・Investor Day の数値目標

| 項目 | 内容 | 出所 |
|---|---|---|
| 年間の新規契約目標 | 年250〜500MW の critical IT を新規契約(2025-11 に 100〜150MW から引き上げ。Q1・Q2 2026 でも再確認) | https://investors.terawulf.com/news-events/press-releases/detail/140 |
| 管理パイプライン | 2.1GW(Q2 2026 で再掲) | https://theblock.co/post/410888/terawulf-hpc-leasing-revenue-jumps-52-widening-lead-over-bitcoin-mining (二次) |
| 2026年の固定運営費 | 100〜125百万ドル | https://www.barchart.com/story/news/453189/terawulf-reports-fourth-quarter-and-full-year-2025-results |
| Investor Day / 数値付き中期経営計画 | **未取得**。試した検索語: 決算説明会の要約検索(複数)。年250〜500MW 契約目標以外に、売上・EBITDA・利回りの期限付き中期数値は見つからなかった | — |
| 2026年通期の調整後EBITDA目標 | **未取得**(data/WULF_data.md でも欠損) | — |
| 開発利回りの目標 | 経営陣は「中位10%台」を求めると発言(二次要約)。会社が示す NOI・利回りの数値は未取得 | 上記 Yahoo 要約 |

### 1-3. 主要な買収・提携・設備投資・資金調達

| 日付 | 内容 | 会社が述べた目的 / 備考 | 出所 |
|---|---|---|---|
| 2025-08 | Fluidstack と Lake Mariner でリース、Google が信用補完(当初18億ドル、後に32億ドルへ増額と報道)。Google にワラント発行 | HPC への転換。ワラントは信用補完の対価 | 表5-2、本文 4. 参照 |
| 2025-08〜10 | 1.00% 転換社債10億ドル(2031年)、7.75% 担保付債32億ドル(2030年)、0.00% 転換社債10.25億ドル(2032年) | HPC 建設資金 | data/WULF_data.md 表4 |
| 2025-10 | Abernathy JV(Texas)を Fluidstack と設立 | 25年リース。約95億ドルの契約収益と Google の信用補完13億ドル(2025年報道) | https://www.theblock.co/amp/post/376561/terawulf-expands-ai-push-9-5-billion-usd-google-backed-fluidstack-joint-venture-stock-jumps (二次) |
| 2026-02頃 | Kentucky(Hawesville)と Maryland(Chesapeake)の拠点を取得。合計で約1.5GW の負荷容量、敷地内発電 | 日付は要確認(Hawesville は2026年2月取得と複数の二次情報) | https://investors.terawulf.com/news-events/press-releases/detail/129 |
| 2026-03-20 | Hawesville の電力供給契約(Big Rivers / Kenergy / TeraWulf、482MW)。Kentucky PSC 案件 2026-00115 | PSC は「消費者保護は十分」として承認(日付は未確認。地元住民は反対) | https://spectrumnews1.com/ky/lexington/news/2026/07/28/residents-oppose-hawesville-data-center-power-deal-at-psc-meeting (二次) ; PSC 提出書類: https://psc.ky.gov/pscecf/2026-00115/mkurtz@bkllawfirm.com/05272026041401/TeraWulf_Motion_Exp._Review__2026-00115.pdf |
| 2026-04-16 | 公募 47.4M株 @ $19.00(Morgan Stanley)、純額約10.0億ドル | 開発資金(data/WULF_data.md 表1) | https://www.boardroomalpha.com/sec/wulf-8-k-2026-04-16-0001104659-26-044387 |
| 2026年Q1 | 2.5億ドルの回転信用枠 | 流動性の補強 | https://investors.terawulf.com/news-events/press-releases/detail/140 |
| 2026-05 | Muskie(Eastern Kentucky)を取得。契約電力を500MW から1GW に拡大(最大2GW を検討)。Kentucky Power が765/345kV 変電所を建設。2期目500MW は2029年へ | 「段階的に AI/HPC キャンパスとして開発」 | https://pulse2.com/terawulf-expands-contracted-power-capacity-at-muskie-data-campus-to-1-gw ; https://fourweekmba.com/ai-terawulf-muskie-contracted-power-1-gw-kentucky-power-2029-ph/ (二次) |
| 2026-07-06 | Anthropic リース(Justified、401MW、20年、約190億ドル)と Abernathy 持分売却(約5.3億ドル) | 売却代金は、直接所有・顧客関係を持てる拠点に再投資 | 本文 0. 参照 |
| 2026年(予定) | Justified 向けに約35億ドルの債務調達(レバレッジドローンと高利回り債)。Morgan Stanley が主幹事、初のレバレッジドローン市場。CFO は「今年中に開始」と述べた | 価格・格付けは**未取得** | https://cointelegraph.com/news/terawulf-3-5-billion-debt-raise-anthropic-data-center ; https://www.itiger.com/news/1103173454 (二次。元は Bloomberg 報道) |

### 1-4. 過去の約束と結果(言行一致)

3年分のガイダンス実績は取得できていない。確認できた範囲のみ。

| 約束した内容(時点) | 結果 | 判定 | 出所 |
|---|---|---|---|
| 2025年中に Core42 向け HPC 72.5MW を提供(2025-05) | 2025年Q3 に HPC 22.5MW 稼働、2026-03-31 時点で 60MW 稼働。定義(gross と critical IT)の違いがありうる | 2025年内に完了せず、遅れの可能性が高い(要確認) | data/WULF_data.md 表5 ; https://investors.terawulf.com/news-events/press-releases/detail/140 |
| 2026年末までに 200〜250MW 稼働(2025-05) | 2026年Q2 末で稼働 81MW(data/WULF_data.md)、または 102MW(Q2 リリースの要約)。**不一致**。建設中336MW は2026年末〜2027年初に引渡し | 未達の公算が大きい。CB-5 が2027年初にずれるため(下行) | https://theblock.co/post/410888/terawulf-hpc-leasing-revenue-jumps-52-widening-lead-over-bitcoin-mining |
| CB-3 は2026年5月中旬に通電(2026-02) | Q1 リリースは「予定通り」。CB-3 の完了時期は**不一致**(5月とする要約と、7月初旬とする data/WULF_data.md) | 5月なら達成、7月なら約7週遅れ | https://investors.terawulf.com/news-events/press-releases/detail/140 |
| CB-4 は2026年Q3、CB-5 は2026年Q4(2026-02) | Q2 説明会で「更新された日程」。CB-4 の賃料開始は2026年下期、CB-5 は2027年初から段階引渡し | **CB-5 は約1四半期以上のずれ** | https://investors.terawulf.com/news-events/press-releases/detail/144 ; GuruFocus 要約 |
| Q1 2026 の売上30〜35百万ドル、調整後EBITDA 0〜3百万ドル(2026-04 の事前開示) | 売上34.0、調整後EBITDA −4.1 | 売上は達成、EBITDA はレンジ下限を割った | data/WULF_data.md 表7 |
| Kentucky の顧客を第2四半期中に確定(2026-05-08) | 2026-07-06 に Anthropic と契約(第2四半期末の6日後) | ほぼ達成(わずかに遅れ) | 上記 Q1・Q2 説明会 |
| 年250〜500MW の新規契約(2025-11) | FY2025 に 522MW を契約。2026年は Anthropic の 401MW(7月) | 達成(契約ベース) | https://investors.terawulf.com/news-events/press-releases/detail/132 |
| Q2 2026 の売上 | 44.8百万ドル。予想46.5(Investing.com)〜50.5(data/WULF_data.md)に対し未達 | 未達 | https://www.investing.com/news/transcripts/earnings-call-transcript-terawulf-posts-wider-q2-2026-loss-shares-slip-93CH-4837940 |
| 2023〜2024年の約束(Nautilus、Cayuga、Lake Mariner の時期など) | **未取得**。試した検索語: "TeraWulf Core42 Lake Mariner HPC delivery on schedule delayed 2025 energization ... Nautilus Cayuga"。過去の遅延を記録した出所は見つからなかった | — | — |

### 1-5. 経営陣の経歴・報酬・インサイダー売買

| 項目 | 内容 | 出所 |
|---|---|---|
| Paul Prager(共同創業者、会長兼CEO) | 2021年2月から会長兼CEO。米国海軍兵学校卒。海軍士官を務めた後、1980年代半ばに Wall Street で石油トレーダー(会社の公式略歴)。1990年からの前身を含む Beowulf Electricity & Data(非公開のエネルギー・デジタルインフラ企業)の創業者兼CEO。Brooklyn Marine & Oil(船舶)も創業。Direct Gas の元CEO | https://www.terawulf.com/leadership/ ; https://en.wikipedia.org/wiki/TeraWulf (二次) |
| Nazar Khan(共同創業者、COO/CTO) | Beowulf Energy の EVP を約20年務めた。それ以前は Evercore Partners | 同上 |
| Patrick Fleury(CFO) | 経歴・就任日は**未取得**(検索結果は取引追跡サイトのみ) | — |
| 報酬KPIの単位(1株当たりか総額か) | **未取得**。2026年の委任状(DEF 14A、2026-04-28、受付番号 0001083301-26-000077)の存在は確認したが、報酬表は読めていない | https://www.boardroomalpha.com/sec/wulf-def-14a-2026-04-28-0001083301-26-000077 |
| 株主総会 | 2026-06-09。議決権の約80.01% が出席、取締役9名を選任(Prager 賛成約2.70億票)。授権株式数の引上げ提案があったとの二次情報があるが、可決かは未確認 | https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000115/wulf-20260609.htm ; https://simplywall.st/stocks/us/software/nasdaq-wulf/terawulf/news/did-google-backed-32-billion-debt-deal-just-shift-terawulfs |
| インサイダー売買 | Prager が 333,300株を $25.17 で売却(約839万ドル)との集計(日付不明)。別の集計は 2026-04-27 に 56,909株(価格 $21.2)。**サイトにより不一致**。Fleury は2026-04-24 に業績連動RSU など。Benzinga は「直近30日は純売り越し」 | https://quantisnow.com/insiders/WULF ; https://us.trendlyne.com/us/equity/insider-trading/all/WULF/1555986/terawulf-inc (二次。SEC Form 4 で要確認) |
| 関連当事者取引 | Beowulf Electricity & Data(Prager 所有)への管理・サービス手数料が前年に2,030万ドル(Hunterbrook の調査)。ブログは1年弱で2.334億ドルの関連当事者取引と集計。10-Q は Beowulf との契約を関連当事者取引と記載 | https://hntrbrk.com/investigations/terawulf ; https://theinvestorchannel.substack.com/p/terawulf-how-ceo-paul-prager-turned (二次、ブログ集計は非公式) |

### 1-6. KPI の追加・停止・定義変更

確認できた範囲(いずれも断定ではない):
- 2025年7月から HPC 売上を別建てで開示(FY2025 10-K)。2026年Q2 は **HPC セグメント利益率 28%(開発前費用と開発費を除くと約80%)**を説明会で示した(GuruFocus 要約)。いつから開示かは未確認。
- 容量の単位が「critical IT MW」(契約MW・稼働MW・建設中MW)で、「総電力MW」(482MW など)と混在する。例: Hawesville は 482MW(gross)と 401MW(critical IT)。
- ビットコイン採掘のKPI(採掘BTC数、ハッシュレート、BTCあたり電力コスト)は、data/WULF_data.md で2025年Q3 以降ほぼ欠損。**開示停止か、検索で拾えていないだけかは区別できない**。
- 調整後EBITDAの定義変更は**未取得**。

---

## 2. 市場の仮説(出典つき)

### 2-1. アナリストの質問テーマ(直近2回: Q1・Q2 2026)

書き起こし全文を読めないため、**回数の集計は不可能**。検索要約で確認できた質問のみ列挙する。

| テーマ | Q1 2026(5/8) | Q2 2026(8月) | 出所 |
|---|---|---|---|
| Kentucky の顧客確定の時期 | あり(Prager が「Q2中、最終段階」と回答) | 契約後のため、財務・与信へ移行 | 上記 Q1 要約 |
| 系統接続(Lake Mariner の追加250MW、ISO の回答) | あり(年央に回答待ち) | 未確認 | 同上 |
| 公益事業者との提携の枠組み | 未確認 | あり(Nick Giles, B. Riley。Kentucky Power との電力供給契約を受けて) | https://finance.yahoo.com/markets/stocks/articles/terawulf-q2-earnings-call-highlights-140000459.html |
| テナントの与信 | 未確認 | あり(Giles。Fleury は長期の与信支援を強調) | 同上 |
| 労働力(電気工・空調工)と工事契約の固定 | 未確認 | あり(Tim Horan, Oppenheimer。Anthropic 契約を名指し) | 同上 |
| 建設費と開発利回り | 未確認 | あり(Bank of America。「中位10%台の利回り」を求めるとの回答) | 同上 |
| 資金調達・株式発行 | 流動性への言及 | Fleury が「株式市場に戻らず賄える」と回答 | Globe and Mail 書き起こし(検索要約) |

試した検索語: "TeraWulf Q2 2026 earnings call Q&A analysts asked ..."、"TeraWulf earnings call analyst question Knoblauch Giles Todaro Vafi ..."、"WULF Q1 2026 earnings call summary analysts asked ..."。Q1 の質疑応答は**ほぼ未取得**。

### 2-2. アナリストの強気論

| 証券会社 | 評価・目標株価 | 論点 | 出所 |
|---|---|---|---|
| Bernstein | Outperform、目標 $36(2026-07-07 維持。「現在値より71%高い」) | Anthropic リースは想定より良い経済性: IT 1MW 当たり年間利回り $2.4M(従来想定は $1.9M)。修正グロス型で粗利益率約85% とみなす。開発費は IT 1MW 当たり $10〜12M(Fluidstack 契約は $8〜10M)。ただし Abernathy JV 収益の喪失と相殺され、モデルは概ね不変。「暗号資産採掘企業の転換としては最長期間の契約」 | https://www.theblock.co/post/407429 (二次)。Q2 後も Outperform を再確認: https://theblock.co/post/410975/bernstein-reaffirms-terawulf-outperform-rating-as-hpc-revenue-hits-71-of-q2-total |
| Morgan Stanley(Stephen Byrd) | Overweight。目標 $72(従来 $66.50 から引上げ)との報道。**日付なし。data/WULF_data.md の $63 / 2026-03 開始 $37 と不一致** | 論点は未取得 | https://www.barchart.com/story/news/3165496/bernstein-sees-70-upside-in-terawulfs-stock の関連検索結果(二次) |
| UBS | Buy、目標 $24。現在の開発ポートフォリオが全て賃貸化されれば最大 $30/株の価値 | TeraWulf は3テナントと合計839MW を契約済み(報道) | https://goldesel.de/aktien/news/terawulf-ubs-startet-mit-buy-analysten-setzen-kursziele-von-15-bis-30-us-dollar (AI生成の独語記事。二次) |
| Jones Trading / Wells Fargo | Buy、各 $30(2026年9月末時点) | 論点は未取得 | data/WULF_data.md 表8 |
| 集計 | Benzinga: 28名、平均 $22、Buy。Investing.com: 24名、平均 約 $33.69(Strong Buy)。**平均目標が大きく不一致** | — | data/WULF_data.md 表8 |

### 2-3. アナリストの弱気論・慎重論

名指しの弱気アナリストは**1社のみ**確認できた(目標の3件以上には届いていない)。残りは「格付け会社・評価会社・批判者」の見解で、証券会社の弱気レポートではない。

| 主体 | 評価・指標 | 論点 | 出所 |
|---|---|---|---|
| Rothschild & Co Redburn | Neutral(Hold)、目標 $15(2026年9月21日ごろ開始) | **資金調達コストの上昇と、ハイパースケーラーの慎重姿勢が拡大を遅らせる可能性**(AI生成の独語記事の要約。Redburn のレポート本文は未取得) | https://goldesel.de/aktien/news/terawulf-ubs-startet-mit-buy-analysten-setzen-kursziele-von-15-bis-30-us-dollar (二次) |
| Fitch(Anubhav Arora の発言として引用) | 格付けの制約要因は建設段階 | 債権者が建設リスクを負う。**建設が180日超遅れても Google の保証が発動しないまま Fluidstack が解約できる**(Lake Mariner の債券に関する文脈) | 検索要約の出所は Zacks/Nasdaq 系記事: https://www.nasdaq.com/articles/should-investors-exit-wulf-stock-high-p-s-multiple-1824x ; 元記事の特定は未了 |
| Zacks/Nasdaq 記事 | 売上高株価倍率 18.24倍 | 重い負債(7.75% 担保付債32億ドル、2031・2032年満期の低利転換社債が合計20億ドル超) | 同上 |
| Weiss Ratings | — | 2026年Q1 売上は前期比 −5.1%、売上に対する資本消費が速い | https://weissratings.com/en/instant-news-alerts/terawulf-inc-wulf-down-5-3-do-i-close-the-trade |
| 空売り比率 | 浮動株の28.6%(2026年9月末ごろ、Benzinga)、減少傾向。2026-03-13 は 96.6M 株(Equibles) | — | https://www.benzinga.com/quote/WULF/short-interest ; https://equibles.com/stocks/wulf/shortinterest |

### 2-4. 空売りレポート・弱気論者の主張と会社の反論

| 主体 | 主張 | 会社の反論 | 出所 |
|---|---|---|---|
| Grizzly Research(2024年8月、X 投稿) | **TeraWulf は専らインサイダーの利益のために運営され、公開株主の不利益になっている**(exclusively run for the benefit of insiders and to the detriment of public shareholders)。Prager と友人らが、過去に失敗した事業(Beowulf)の資産を通じて上場会社から資金を吸い上げている。Barry Honig に連なる投資家が裏にいるとも主張 | **未取得**。試した検索語: "Grizzly Research TeraWulf short report Prager related-party transactions allegations company response"。会社の正式な反論は見つからなかった | https://twitter.com/ResearchGrizzly/status/1824081651267145772 (二次) |
| Hunterbrook(調査報道) | Beowulf Electricity & Data(Prager 所有)に前年2,030万ドルの手数料 | 未取得 | https://hntrbrk.com/investigations/terawulf (二次) |
| ブログ(Substack) | 1年弱で2.334億ドルの関連当事者取引 | 未取得(非公式の集計) | https://theinvestorchannel.substack.com/p/terawulf-how-ceo-paul-prager-turned |

2025〜2026年の空売りレポートは検索で見つからなかった(試した検索語: "TeraWulf short seller report short interest bear case WULF")。

### 2-5. 報道・SNS のナラティブと株価の大きな変動(直近1年)

見出しで繰り返される言葉(確認できた範囲): 「Google-backed」、「$19B Anthropic lease」、「AI landlord」(https://app.sentisense.ai/stories/terawulf-leases-ai-data-center-for-19b-and-rebrands-as-ai-landlord-07082026)、「HPC revenue surpasses mining」、「shares fall / slip」(決算後)。

| 日付 | 動き | 理由(出所に書かれたもの) | 出所 |
|---|---|---|---|
| 2025-08-14 | +59%(終値) | Fluidstack との HPC 契約(契約収益37億ドル)と Google の信用補完 | https://www.theblock.co/amp/post/376561/... ; 株価履歴の集計サイト(二次) |
| 2025-10-14 | +10.4% | データセンター向け32億ドル債の発行発表 | equibles.com の要約(二次) |
| 2026-05-08 前後 | 「shares fall」 | Q1 決算。売上は前期比減、純損失4.28億ドル、EPS が予想を下回る | https://tangem.com/en/news/investments/24042-terawulf-q1-hpc-revenue-surpasses-mining-shares-fall/ |
| 2026-07-06 | 約 +14% | Anthropic リース発表 | data/WULF_data.md 表9 |
| 2026-07-07 | 約 −8〜−9% | 複数の媒体が「利益確定売り」と説明 | https://www.theblock.co/post/407429 |
| 2026-08-05 | 「shares slip」 | Q2 の売上未達、調整後EBITDA −18.3百万ドル、非現金のワラント損失 | https://www.investing.com/news/transcripts/earnings-call-transcript-terawulf-posts-wider-q2-2026-loss-shares-slip-93CH-4837940 |
| 2026-10-06 | 終値 $14.97。直近1か月で −$2.89(約 −20.7%)。52週レンジ $10.47〜$29.84 | **理由は未取得**(試した検索語: "TeraWulf WULF stock why shares fell OR jumped October 2026")。2026-09-21 ごろの Redburn Neutral 開始($15)が同時期 | https://equibles.com/stocks/wulf/price ; https://markets.financialcontent.com/wss/quote/nq:wulf (二次) |
| 次回決算 | 2026-11-09 | — | 同上 |

注: 52週安値は出所により $4.64〜$10.47 とばらつく(data/WULF_data.md 表1 と本節)。窓の取り方の違いと思われる。

セクター要因(日付が不確実なため参考扱い):
- 「AI 信用リスクの拡大」の記事は、Applied Digital の2030年債が96ドルを割り込み、Oracle のCDS が拡大、CoreWeave・Nebius・Cipher・IREN が急落した、と伝える(日付は検索結果から特定できず)。https://sherwood.news/markets/nvidias-favorite-stocks-are-getting-shellacked-as-ai-credit-risk-spreads
- 「Microsoft が米欧の新規AIデータセンター投資を取りやめ、供給過剰を懸念」と報じられ、マイナー株が4〜12%下落。要約は2026年3月とするが、**同種の報道は2025年にもあり、日付は不確実**。https://cointelegraph.com/news/bitcoin-mining-stocks-down-after-microsoft-reportedly
- ビットコイン価格と WULF 株価の関係は**未取得**(BTC価格の検索は行っていない)。WULF の売上に占めるビットコイン採掘は、2026年Q2 で約12.9百万ドル / 44.8百万ドル(約29%、算出)まで低下している。

---

## 3. 一次情報(スカットルバット: 開示以外の観察)

| # | 観察 | 内容 | 含意 | 出所 |
|---|---|---|---|---|
| 1 | **規制当局の提出書類: Hawesville の電力供給** | 2026-03-20、Big Rivers・Kenergy・TeraWulf が482MW の電力供給契約を締結(Kentucky PSC 案件 2026-00115)。PSC は消費者保護が「十分」として承認。2026-07-28 の PSC 会合では地元住民が反対。TeraWulf のエネルギー計画の添付書類が2026-08-14 に提出された | 電力の確保量は書類で裏づく(供給サイドの需要・供給)。地元の反対は許認可・訴訟リスクの兆候だが、PSC の管轄は料金のみ(水利用・騒音・立地は対象外) | https://spectrumnews1.com/ky/lexington/news/2026/07/28/residents-oppose-hawesville-data-center-power-deal-at-psc-meeting ; https://psc.ky.gov/pscecf/2026-00115/mkurtz%40bkllawfirm.com/08142026011725/TeraWulf_Energy_Plan__Attachments.pdf |
| 2 | **テナントの資金調達(Fluidstack)** | Series A 8.3億ドル(評価額75億ドル、2026年1月クローズ)。2026年4月に Bloomberg が10億ドルで評価額180億ドルの協議を報道(ある出所は15億ドルでクローズとするが、**未確認**)。累計の株式調達は約26億ドル。Macquarie から最大100億ドルの債務枠(GPU担保、Sacra) | Fluidstack は Lake Mariner(10年リース3本)と Abernathy のテナント。株式26億ドルに対し、リース債務は数十億ドル規模。**Google の信用補完が決定的** | https://dealroom.co/news/139936-fluidstack-confirms-830m-series-a-at-7-5b-valuation-larger-than-earlier/ ; https://dealroom.co/news/127356-fluidstack-targets-18b-valuation-as-jane-street-leads-1b-raise/ ; https://www.sacra.com/c/fluidstack (二次) |
| 3 | **顧客側の開示(Anthropic)** | 2026-05-28 に Series H 650億ドルを調達、評価額9,650億ドル(post-money)。run-rate 売上は470億ドル超(5月、報道)。Q2 に初の黒字化を見込むとの報道。計算資源は Amazon と最大5GW、Google・Broadcom と TPU 5GW、SpaceX から GPU。2025-11 には Fluidstack と500億ドルの Texas・New York のデータセンター契約 | テナントの支払能力は強い。ただし**格付け・社債利回りは未取得**(Anthropic の格付けを示す出所は見つからなかった) | https://letsdatascience.com/news/anthropic-secures-65b-nears-1-trillion-valuation-c237d543 ; https://w.media/anthropic-valuation-touches-us-965-billion-surpassing-openai/ ; https://www.techmarketview.com/ukhotviews/archive/2026/05/29/anthropic-closes-in-on-a-trillion-dollar-valuation (二次) |
| 4 | **業界統計(CBRE 2026年上期)** | 北米で建設中容量の80.4% が賃貸済み(前年74.3%)。上期の純吸収は1,456.2MW(前年比 +11.7%)。Northern Virginia の空室率約0.24%。10MW超の要件の希望賃料は kW 月当たり $160〜185(供給が10.8MWのみ)。全ての導入規模帯で賃料が上昇。CBRE の見通し: 建設の遅れが米国の供給を2030年まで制約し、価格が過去最高水準になる | 賃料・空室の面で貸し手に有利。ただし TeraWulf のリースは**固定契約**で市況上昇の恩恵は更新時のみ | https://w.media/north-americas-data-center-growth-slows-as-capacity-runs-out-cbre/ ; https://www.cbre.com.au/insights/books/north-america-data-center-trends-h1-2026/northern-virginia-data-center-market (二次) |
| 5 | **施工・労務(電気工の不足)** | 電気工事はデータセンター建設費の45〜70%(ある分析)。建設業は2026年に34.9万人の純増員が必要。60MW施設の1か月の遅れは約1,420万ドル(一般的な推計) | TeraWulf の説明会でも人件費の上昇を認める(Khan)。1MW 当たり建設費の上振れ要因 | https://insightonbusiness.com/the-electrical-labor-shortage-is-delaying-projects-heres-how-to-stay-ahead/ ; https://www.classet.ai/blog/data-center-labor-shortage-2026 (二次、一般論) |
| 6 | **格付け会社の見解** | Fitch は Lake Mariner の債券について、建設段階が格付けの制約。Fluidstack に建設遅延(180日超)時の解約権(Google の保証は発動しない) | 弱気側の具体的な契約条項。**出所は検索要約で、元記事の特定は未了** | 2-3 参照 |
| 7 | **地元メディア** | Hancock Clarion は初期401MW の入居者が Anthropic 1社のみで、他テナントは将来の拡張次第と指摘 | 単一テナント集中 | https://www.hancockclarion.com/?p=72965 (二次) |

求人数の推移、価格表、競合の値上げ: **未取得**(検索していない)。

---

## 4. 競合と業界

### 4-1. 競合の同種KPI

取得できたのは Core Scientific のみ。他社は統括メモ(THEME_DECISION.md)の数値で、私は検証していない。

| 企業 | 売上(直近四半期) | 成長率 | 粗利率 | 受注残・契約 | 出所 |
|---|---|---|---|---|---|
| **Core Scientific**(2026年Q2、7/28発表) | 164.2百万ドル(前年同期 78.6百万ドル) | +109% | 粗利益 70.0百万ドル(売上比 約42.6%、算出)。前年は5.0百万ドル | 賃貸済み電力約1.1GW、潜在契約収益240億ドル超。課金対象437MW(7月中旬)。AMDと15年契約約530MW(5拠点)、基本契約収益140億ドル超。純損失11.55億ドル(ワラント公正価値の変動が主因)。調整後EBITDA 41.1百万ドル。コロケーション売上136.7百万ドル(83%) | https://secure.businesswire.com/news/home/20260727468665/en/Core-Scientific-Announces-Second-Quarter-2026-Results ; https://cointelegraph.com/markets/core-scientific-revenue-doubles-q2-ai-colocation-expansion-accelerate |
| TeraWulf(比較用) | 44.8百万ドル(前期比 +32%、前年同期 47.6百万ドルから −6%) | 前年比 −6% | HPC セグメント利益率 28%(約80% は開発前費用等を除く調整後) | 契約収益 約270億ドル(統括メモ)。Anthropic 190億ドル | 本文 1-1 |
| Hut 8 | **未取得** | — | — | 統括メモ: 2拠点949MW、契約収益266億ドル、River Bend 245MW・15年・基本期間70億ドル(Google が賃料を保証)。検索では「7月に98億ドルの新規リース(顧客非開示)」の記述あり | THEME_DECISION.md ; 上記 cointelegraph(二次) |
| Cipher Digital | **未取得** | — | — | 統括メモ: Q2 売上24.84百万ドル、AWS 300MW・15年・約55億ドル(二次)、Fluidstack 向けは Google が17.3億ドル保証 | THEME_DECISION.md |
| Applied Digital | **未取得** | — | — | 統括メモ: CoreWeave 400MW 約110億ドル、別のハイパースケーラー約50億ドル | THEME_DECISION.md |

試した検索語: "Q2 2026 results Cipher Digital Hut 8 Core Scientific Applied Digital revenue growth ..."(TeraWulf のみ返った)、"Core Scientific Cipher Digital Hut 8 second quarter 2026 results ..."(Core Scientific のみ)。シェアは**未取得**。

### 4-2. 業界の供給能力・価格・技術・参入障壁

| 項目 | 内容 | 出所 |
|---|---|---|
| 需要と供給 | 2025年の稼働容量は約8.9GWで、需要約21.1GWを大きく下回った(Jefferies、統括メモ経由) | THEME_DECISION.md |
| 空室・賃貸率・賃料 | 本文 3 の #4(CBRE H1 2026) | 同上 |
| 参入障壁 | 系統接続の審査(Dominion のバッチ処理など)、変圧器の納期(平均128週。統括メモ)、電気工の不足 | CBRE 上記 ; THEME_DECISION.md |
| TeraWulf の優位性の源泉 | 旧精錬所・採掘場の既存系統接続(Hawesville 約480MW、Lake Mariner)、段階的な電力確保(Muskie 1GW) | 本文 1-3 |
| 技術の世代交代 | **未取得**(GPU・冷却・ラック密度の世代交代が建屋の陳腐化に与える影響は検索していない)。統括メモは「GPUの陳腐化はテナントが負う」構造と整理 | — |
| ビットコイン採掘の位置づけ | 採掘売上は縮小(2026年Q2 で約29%)。マイナーは採掘コストが現物価格を上回る社が多く、BTC を売って AI 転換の資金にしている(whale-alert の記事、二次) | https://whale-alert.io/stories/e294014549085f/Public-Bitcoin-miners-are-selling-BTC-to-fund-large-AIHPC-and-hyperscaler-datacenter-pivots |

### 4-3. 顧客・サプライヤーの集中度

| 項目 | 内容 | 出所 |
|---|---|---|
| 顧客 | 3テナント(Anthropic、Fluidstack、Core42)に集中。契約済み839MW(UBS 関連の独語記事)。Justified の初期401MW は Anthropic 1社 | 本文 2-2、3 の #7 |
| 上位顧客比率(売上ベース) | **未取得**。2026年Q2 の HPC 売上31.9百万ドルは Core42(60MW 稼働)と Fluidstack(CB-3 完了後)の合算とみられるが、内訳は未取得 | — |
| 信用補完の依存 | Lake Mariner は Google の保証32億ドル(契約賃料約67億ドルの約48%、算出)。Abernathy は13億ドルだったが持分売却で TeraWulf の保有は解消 | 本文 1-1 |
| サプライヤー | 電力: Big Rivers / Kenergy(Hawesville)、Kentucky Power(Muskie)。施工: Fluor(二次要約)。その他(変圧器・発電機の調達先と納期)は**未取得** | 本文 1-3 |

---

## 5. 義務と資本

| 項目 | 内容 | 満期・条件 | 出所 |
|---|---|---|---|
| 1.00% 転換社債 | 10.0億ドル | 2031-09-01。転換価格約 $12.43。キャップドコール上限 $18.76(コスト1.006億ドル) | data/WULF_data.md 表4 ; 10-Q(2026-03期)の検索要約: https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000092/wulf-20260331.htm |
| 2.75% 転換社債 | 5.0億ドル(発行時) | 2030-02-01。転換価格約 $8.48(1,000ドル当たり117.9245株)。**2025年10月に「2030 Sale Price Conversion Event」の達成で保有者の選択で転換可能**になり、2025-12-31 と 2026-06-30 の貸借対照表で短期の転換社債に分類。転換時は現金または現金と株式の組合せを会社が選択。**株価 $14.97 での転換価値は約8.8億ドル(算出: 58.96M株 × $14.97)で、額面5.0億ドルとの差は約3.8億ドル**(未償還額が5.0億ドルのままと仮定。買戻しの有無は未確認) | 10-Q(2026-06-30期)の検索要約: https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000166/wulf-20260630.htm |
| 0.00% 転換社債 | 10.25億ドル | 2032年。転換価格約 $19.94(現在株価より高い) | data/WULF_data.md 表4 |
| 7.750% 担保付シニア債 | 32億ドル(WULF Compute LLC) | 2030-10-15。Google 保証のバックストップ関連の担保・保証。**リコース性は未取得** | data/WULF_data.md 表4 |
| 回転信用枠 | 2.5億ドル | 条件は未取得 | https://investors.terawulf.com/news-events/press-releases/detail/140 |
| 2025年12月の13億ドル | CFO が「前年12月に13億ドル」と述べた(中身は未取得) | **不明**(Abernathy 関連の資金調達の可能性があるが、出所なし) | https://cointelegraph.com/news/terawulf-3-5-billion-debt-raise-anthropic-data-center |
| Justified 向け計画債務 | 約35億ドル(未開始) | 総事業費は 401MW × $10〜12M(Bernstein)= 約40〜48億ドルとすると、借入比率は約73〜87%(算出)。GuruFocus 要約は「資本構成は自己資本32% / 債務68%、総事業費約910万ドル/MW」と記すが、**CB-4/CB-5(Lake Mariner)の記述か Justified かが不明** | 本文 1-3 ; https://finance.yahoo.com/markets/stocks/articles/terawulf-inc-wulf-q2-2026-190057902.html |
| Google ワラント | **73,580,000株、行使価格 $0.01**。行使開始は各リースの賃料開始日か目標開始日の180日後の早い方。満期は2030-08-13(41,011,803株)と2030-08-17(32,568,197株)。保証が発効するまで、ワラントは貸し手の利益のために担保差入れ。Google の持分は約8%→約14%(報道) | FY2025 10-K: https://www.sec.gov/Archives/edgar/data/1083301/000108330126000031/wulf-20251231.htm (検索要約) ; https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001104659-25-079463/tm2523651d3_8k.htm |
| 同ワラントの希薄化 | 73.58M株は直近の発行済み498.97M株の約14.7%、希薄化後ベース(498.97 + 73.58)の約12.9%(算出)。**ワラント公正価値は株価上昇で損失計上**(Q2 2026 で非現金損失7.557億ドル) | data/WULF_data.md |
| Google の信用補完額 | 当初18億ドル→32億ドル(報道)。Fluidstack の CB-3 完了で6億ドルの支援が発効(二次、data/WULF_data.md)。10-K 本文での32億ドルの確認は**未了**(検索要約に出なかった) | https://www.theblock.co/post/367257/googles-pro-forma-stake-in-fifth-largest-bitcoin-miner-terawulf-grows-to-14-as-the-miner-plans-400-million-fundraising-plan |
| ATM(随時増資) | 2026年の合意・使用額は**未取得**(data/WULF_data.md でも欠損)。Fleury は「株式市場に戻らない」と述べた | — |
| 流動性 | 現金+制限付現金 約30億ドル(2026-06-30)。親会社の無制限流動性 14.5億ドル。Abernathy 売却代金 約5.3億ドル(3回に分割、2027年4月まで) | Q2 説明会(検索要約) ; data/WULF_data.md 表4 |
| リース・購入コミットメント・長期供給契約・顧客の前払い | **未取得**。10-Q(2026-06-30期)の該当節は検索要約に出なかった | — |

---

## 6. 強気側の最強の論点3つ

### 強気1: Anthropic リースの契約条件と開発利回りが厚い
- 20年、約190億ドル、401MW、「投資適格の信用に支えられる見込み」。更新オプション5年×2回との報道(単一〜複数の二次、**一次未確認**)。(出所: https://w.media/anthropic-signs-20-year-lease-for-ai-data-center-campus-developed-by-terawulf-in-kentucky/ ; https://cointelegraph.com/news/terawulf-3-5-billion-debt-raise-anthropic-data-center)
- Bernstein: IT 1MW 当たり年間収益 $2.4M(従来想定の $1.9M を上回る)、粗利益率約85%、開発費 $10〜12M/MW。収益 $2.4M × 85% = $2.0M の NOI を $10〜12M で割ると**開発利回り約17〜20%(算出)**。経営陣が求める「中位10%台」を上回る。ただし年次上昇率が不明のため、初年度利回りはこれより低い可能性がある。(出所: https://www.theblock.co/post/407429 ; https://finance.yahoo.com/markets/stocks/articles/terawulf-q2-earnings-call-highlights-140000459.html)
- Abernathy 持分は IRR 20%、約5.3億ドル(投資額約4.5億ドル比 +18%、算出)で現金化。(出所: 10-Q https://www.sec.gov/Archives/edgar/data/0001083301/000108330126000166/wulf-20260630.htm ; https://datacentremagazine.com/news/inside-terawulfs-anthropic-data-centre-deal-and-ajv-exit)

### 強気2: 電力付き用地の希少性と、パイプラインの厚み
- Hawesville は482MW の電力供給契約を Kentucky PSC が承認。Muskie は契約電力を1GW に拡大(最大2GW を検討)。管理パイプライン2.1GW。(出所: https://spectrumnews1.com/ky/lexington/news/2026/07/28/residents-oppose-hawesville-data-center-power-deal-at-psc-meeting ; https://pulse2.com/terawulf-expands-contracted-power-capacity-at-muskie-data-campus-to-1-gw)
- CBRE 2026年上期: 建設中容量の80.4% が賃貸済み(前年74.3%)、Northern Virginia 空室0.24%、全規模帯で賃料上昇、供給は2030年まで制約される見通し。(出所: https://w.media/north-americas-data-center-growth-slows-as-capacity-runs-out-cbre/)
- 同業の Core Scientific は2026年Q2 の売上が前年同期比 +109%、コロケーション売上が136.7百万ドルまで立ち上がり、契約が売上に転化する経路を示している。(出所: https://secure.businesswire.com/news/home/20260727468665/en/Core-Scientific-Announces-Second-Quarter-2026-Results)

### 強気3: 資金手当てとテナントの支払能力
- 現金+制限付現金 約30億ドル、親会社の無制限流動性14.5億ドル、Abernathy 売却代金5.3億ドル。CFO は株式市場に戻らず近期の受注残を賄えると発言。2025年10月に32億ドルの担保付債を消化し、Justified の35億ドルは Morgan Stanley が主導。(出所: https://www.theglobeandmail.com/investing/markets/stocks/WULF/pressreleases/3806661/terawulf-wulf-q2-2026-earnings-call-transcript/ ; https://cointelegraph.com/news/terawulf-3-5-billion-debt-raise-anthropic-data-center)
- Anthropic は2026-05に650億ドルを調達(評価額9,650億ドル)、run-rate 売上は470億ドル超(報道)。Amazon・Google・Broadcom との大型計算契約。(出所: https://letsdatascience.com/news/anthropic-secures-65b-nears-1-trillion-valuation-c237d543)
- Lake Mariner は Google の信用補完とワラントで Google と利害が一致(Google の持分約14%)。(出所: https://www.theblock.co/post/367257/...)

---

## 7. 弱気側の最強の論点3つ

### 弱気1: 建設・資金調達の実行リスクが大きく、実績は積み上がっていない
- 売上は予想未達(Q2 44.8百万ドル vs 予想 46.5百万ドル)、調整後EBITDA −18.3百万ドル、GAAP純損失9.4億ドル(うち非現金ワラント損失7.557億ドル)。Q1 の調整後EBITDA は会社の事前レンジ(0〜3百万ドル)を下回った。(出所: https://www.investing.com/news/transcripts/earnings-call-transcript-terawulf-posts-wider-q2-2026-loss-shares-slip-93CH-4837940 ; data/WULF_data.md 表7)
- スケジュール: CB-5 は2026年Q4 から2027年初へ。Core42 向け72.5MW は2025年内の約束に対し、2026-03 末で60MW。Justified の初期稼働は2027年下期と、まだ先。時間当たり人件費は上昇中。(出所: 本文 1-4 ; https://finance.yahoo.com/markets/stocks/articles/terawulf-q2-earnings-call-highlights-140000459.html)
- 債務: 7.75% 担保付債32億ドル、転換社債合計約25億ドル、計画中の35億ドル(借入比率73〜87%、算出)。2030年転換社債は株価 $14.97 でも転換価値が額面を約3.8億ドル上回る(算出)。Fitch は、建設が180日超遅れると Google の保証が発動しないまま Fluidstack が解約できると指摘。Redburn は資金調達コストの上昇を懸念。(出所: 本文 5 ; https://www.nasdaq.com/articles/should-investors-exit-wulf-stock-high-p-s-multiple-1824x ; https://goldesel.de/aktien/news/terawulf-ubs-startet-mit-buy-analysten-setzen-kursziele-von-15-bis-30-us-dollar)

### 弱気2: テナントの信用と契約の集中
- Lake Mariner と(売却前の)Abernathy のテナント Fluidstack は非公開の新興企業。株式調達の累計は約26億ドル、評価額は75億ドルから180億ドル(未確認)へ急変。Google の保証32億ドルは契約賃料約67億ドルの約48%(算出)にとどまる。(出所: https://dealroom.co/news/139936-fluidstack-confirms-830m-series-a-at-7-5b-valuation-larger-than-earlier/ ; https://www.stocktaper.com/earningsCallSummary/WULF/2025/Q3)
- Anthropic リースの信用補完は「投資適格の信用」とあるだけで、**提供者・金額・発動条件が不明**。Anthropic 自身の格付けも見つからなかった。Justified の初期401MW は Anthropic 1社に集中。(出所: https://w.media/anthropic-signs-20-year-lease-for-ai-data-center-campus-developed-by-terawulf-in-kentucky/ ; https://www.hancockclarion.com/?p=72965)
- 業界では AI 信用リスクの拡大(Applied Digital の債券下落、Oracle のCDS 拡大)や供給過剰懸念の報道が出ている(日付は不確実)。Redburn は「ハイパースケーラーの慎重姿勢」を挙げる。(出所: https://sherwood.news/markets/nvidias-favorite-stocks-are-getting-shellacked-as-ai-credit-risk-spreads)

### 弱気3: 希薄化とガバナンス
- Google ワラント73.58M株(行使価格 $0.01)は発行済みの約14.7%。ワラント公正価値の変動が GAAP 損益を大きく振らす(Q2 −7.557億ドル、Q3 2025 −4.246億ドル)。2026年4月には $19.00 で約10億ドルの公募(現在株価 $14.97 は約21%下)、授権株式数の引上げ提案、空売り比率28.6%。(出所: FY2025 10-K https://www.sec.gov/Archives/edgar/data/1083301/000108330126000031/wulf-20251231.htm ; https://www.boardroomalpha.com/sec/wulf-8-k-2026-04-16-0001104659-26-044387 ; https://www.benzinga.com/quote/WULF/short-interest)
- CEO 関連の取引: Beowulf(Prager 所有)への手数料(前年2,030万ドル)、Grizzly Research の「インサイダーのために運営」との主張(2024年8月)。**会社の反論は見つからなかった**。(出所: https://hntrbrk.com/investigations/terawulf ; https://twitter.com/ResearchGrizzly/status/1824081651267145772)
- Prager の売却(約839万ドル、集計サイトにより不一致)と、直近30日の純売り越し。(出所: https://quantisnow.com/insiders/WULF ; https://www.benzinga.com/quote/WULF/short-interest)

---

## 8. 取得できなかった重要項目(まとめ)

1. **Anthropic リースの契約条項**: 賃料の年次上昇率、トリプルネットか、更新オプション(二次で「5年×2回」)、解約条項、信用補完の提供者・金額・期間・発動条件。Bernstein は修正グロス型とみなす(トリプルネットではない可能性)。プレスリリース原文・8-K 本文は未読。
2. **Google ワラント**の Anthropic 関連の有無(なし、と推定されるが出所なし)。Lake Mariner の Google 保証32億ドルの10-K 本文での確認。
3. **Anthropic・Fluidstack・Core42 の格付け、債券利回り**。
4. **決算説明会の書き起こし全文**: 各四半期3〜6発言、Q&A の回数集計。特に Q4 2025(2026-02)、Q1 2026 の質疑応答。
5. **Investor Day・期限付き中期数値目標**、2026年通期の調整後EBITDA目標、会社が示す NOI・目標IRR(Abernathy の IRR 20% を除く)。
6. **報酬KPIの単位**(委任状の報酬表)、Fleury の経歴、インサイダー売買の一次確認(Form 4)。
7. **過去3年(2023〜2024年を含む)のガイダンス実績**、Grizzly 等への会社の反論。
8. **Hut 8・Cipher・Applied Digital の直近四半期KPI**(売上成長率、粗利率)とシェア。
9. **ビットコイン価格と WULF 株価の関係**、直近の株価下落(2026-09〜10)の理由。
10. **求人数の推移、価格表、技術の世代交代の影響**(検索していない)。
11. **負債残高の最新値**(2030年転換社債の買戻し)、ATM の2026年状況、リース・購入コミットメント、顧客の前払い。
12. **Lake Mariner の稼働MW**: Q2 末81MW(data/WULF_data.md)か102MW(Q2 要約)か。CB-3 の完了月(5月か7月)。

検索回数: 35 / 35
