# B群 半導体ボトルネック(B1 先端パッケージ材料・基板 / B2 光インターコネクト / B3 テスト・検査) 調査メモ

作成日: 2026-10-11 / 作成者: アナリスト補佐(判断材料の収集のみ。投資判断は行わない)

---

## 0. 調査上の制約(必ず先に読むこと)

1. **取得経路はすべて WebSearch の要約テキスト**。WebFetch・curl は遮断のため、決算短信・IR資料・株価ページの原文は開いていない。「出所URL」は検索結果に表示されたURLで、要約がそのページを根拠にしていると推定されるもの。ページ内容そのものは未確認。
2. **WebSearch の予算(1ターン200回、全エージェント共有)が途中で枯渇**した。約45回で打ち切られ、以下は未取得のまま残っている。
   - B1: 受注残、リードタイム(週)、前払い・長期契約の実例、1年騰落・年初来騰落率(年初価格が取れなかった)、ETF、レゾナック・ディスコ・米国銘柄(Amkor/Onto等)の個別数値
   - **B2: LITE・COHR 以外のほぼ全て**(Fabrinet・Credo・AAOI・Ciena・Corning、古河電工・フジクラ・住友電工等の日本銘柄、株価・PER・時価総額、2030年市場規模、弱気材料の詳細)
   - **B3: アドバンテスト以外のほぼ全て**(プローブカード、Teradyne、FormFactor、東京精密、HBM特化のテスト需要、市場規模、リードタイム、弱気材料)
   - 続きが必要なら、上限緩和(環境変数 CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION)後に再実行するか、次のターンで追加調査を依頼すること。
3. **株式分割で株価が不連続**。株価・時価総額・目標株価は分割調整の有無で桁が変わる。
   - 日東紡(3110): 2026-07-01 に 1→5 分割
   - イビデン(4062): 2026-01-01 に 1→2 分割、2026-10-01 に 1→2 分割(9/29 が権利落ち日とみられる)
   - 三井金属(5706): 1→10 分割(発表は業績修正と同時。効力発生日は未確認。9/25→9/29 の株価推移から 9/29 までに効力発生とみられる)
4. 検索要約は日付・年・単位を誤ることがある(例: イビデン営業利益「900億→1.27兆円」は単位誤りで、1,270億円の意味と読むのが自然)。**単一出所の数値には「単一」と記した**。二次情報(ブログ・アグリゲータ)は「二次」と記した。
5. 訓練知識由来の記述は「訓練知識・未検証」と明記した。

### 横断で気づいた点(判断材料)
- 本メモで取得できた日本の素材3社(日東紡・味の素・三井金属)は、**会社予想ベースでは今期が減益**(日東紡 純利益-52%、味の素 純利益-8.3%、三井金属 経常利益-26.9%)。原因(前期の一過性益か、保守的ガイダンスか)は未確認のため、PEG は会社予想では定義できない。
- 株価は銘柄間で明暗が分かれる。イビデンは年初来+292%(6/26時点)でさらに上昇、日東紡は5/7高値から約半値(推計)。
- 2026-06-26 のロイター: 日経平均は年初来+37%、半導体関連が日経平均の時価総額の約25%を占め、集中がリスクと指摘。

---

## B1 AI半導体の先端パッケージ材料・基板

### B1-1 需要の強烈さの証拠

| 項目 | 数値・内容 | 出所ID・公表日 | 信頼度 |
|---|---|---|---|
| T-glass 需給ギャップ | 2026年は10%超(2025年より悪化) | S1 Counterpoint 2026-03-11 | 調査会社のチャネルチェック。原本は未開封 |
| T-glass 供給 | 需要の約70%にとどまる状態が2027年まで続く、Nvidia向けが優先配分 | S4 Fusion Worldwide Greensheet 2026-05 | 二次(業界ニュースレター)。他で未確認 |
| ABF基板 需給ギャップ | 2026年下期に約10%、2027年に約20%まで拡大(新設能力が立ち上がるまで) | S1/S2 Counterpoint 2026-03-11(S2は再掲、2026-08) | 調査会社 |
| 新設(グリーンフィールド)能力 | 2027年まで来ない | S1 | 同上 |
| ABF基板 価格 | 2026上期は前期比+3〜5%/四半期(Counterpoint予想)。標準ABF基板は2026下期に+5〜10%、スポットは+30%超。年平均+15〜20%、一部特殊品は+40%超 | S1、S29(onmsft、Taiwan News) | 予想・推計。実績の公表価格ではない |
| ABFフィルム 価格(味の素) | 基板メーカーに+30%超の値上げを通知、2026年Q3から(DigiTimes報道)。ただし他報道は「検討中」。基板コストへの影響は約3〜6%の推計 | S21 DigiTimes 2026-05-13 他 | 主に単一(DigiTimes、有料壁)。会社の公式確認なし |
| 味の素の対応 | 一律値上げには慎重、一部製品の値上げには前向き。2026-06-30に電子材料事業の説明会を開催。能力拡大で2030年までの需要を満たせる見通しとWSJ経由で報道 | S22 Gigazine 2026-06-15(WSJ引用)、the-shashi | 二次。説明会の具体数値は未確認 |
| T-glass 価格(日東紡) | 計画済みの値上げは**ほぼ完了、追加値上げの予定なし**(エネルギー高止まりなら再検討の余地)。別の二次報道は「今年少なくとも+25%」 | S3 TrendForce 2026-08-06(日経報道引用)。+25%は ldaily.ua(低信頼) | 一次は日東紡の発言(報道経由) |
| 銅張積層板(CCL) 価格 | 2026上期に等級別で+20%〜40%超 | S25 サプライヤー側の情報(nextpcb/webull) | 二次 |
| HVLP銅箔 需給 | HVLP4は2027年に31%、2028年に20%の供給不足(Morgan Stanley推計とされる)。2026年のAIサーバー向けHVLP需要は約2.4万トン、前年比+260% | S25 36kr(日付不明、2026年とみられる) | 二次・単一 |
| HVLP銅箔 寡占 | 高階HVLPは三井金属・Circuit Foil(ルクセンブルク)・金居(台湾)で有効供給の8〜9割(業界関係者の推計) | S24 CTEE 2026-07-22 | 推計 |
| CoWoS 需給 | 供給不足は現在約20%→2026年末に約10%へ縮小の見込み。Nvidiaが能力の過半を確保(年間80〜85万枚の予約とされる) | S27 EDN報道の再掲(digitalcitizen/Wccftech) | 二次 |
| 顧客の前払い・長期契約・顧客負担の増産投資 | **B1では実例を確認できなかった**。Counterpointは「AI企業は多年度の能力契約でT-glassの優先権を確保すべき」と推奨している(推奨であり事実の報告ではない) | S1 | 未確認 |
| リードタイム(週) | **T-glassクロス自体の値は取得できず**。川下の参考: Lattice社の製品で44週超、44週未満で発注する場合は短納期手数料(Greensheet 2026-02/05) | S4 | 二次。ガラスクロスのリードタイムではない点に注意 |
| 受注残 | **取得できず**(日東紡・イビデン・味の素とも) | - | 未取得 |

**個社の実績(需要の証拠として)**

| 企業 | 内容 | 出所ID・公表日 |
|---|---|---|
| 日東紡 | 2027年3月期Q1(2026/4-6月): 売上340.33億円(+20.6%)、営業利益79.43億円(+84.8%)、営業利益率15.2%→23.3%。通期経常利益予想を260億→300億円へ上方修正(+15.4%)。TrendForceは通期売上1,410億円・営業利益300億円・純利益200億円(各+40億/+40億/+30億円の上方修正、純利益は前期比-52%)と報道 | S7 JPX(2026-08-05)、S8 kabutan(2026-08-05)、S3 TrendForce(2026-08-06) |
| イビデン | 2026年3月期: 売上4,162億円(+12.7%)、営業利益620億円(+30.3%)、電子事業の営業利益452億円(+68.5%)。2027年3月期Q1: 売上1,232億円(+26.4%)、営業利益269億円(+52.4%)。通期予想を引き上げ(営業利益900億→約1,270億円と報道。kabuyohoは経常利益1,270億円・前期比+108.8%・Q1進捗21.6%。**指標は要原文確認**)、純利益580億→840億円。8/5はストップ高(+24.49%、終値20,330円)と報道 | S12 tousaiblog(2026-05-11、2026-08-04)、S13 technews(2026-05-12)、S15 kabuyoho、S17 traders |
| イビデン 増産投資 | 2026-02-04に2026〜28年度の3年間で電子事業に5,000億円の投資を決議(初期2,200億円は既存工場で2027年度から順次稼働)。2/26に大野事業場を中心に2,800億円の追加投資(2027年度以降量産)。単年度の設備投資は2027年3月期に2,100億円計画 | S12、S13(technews 2026-02-04) |
| 味の素 電子材料 | 2026年3月期: 売上+31%、営業利益546億円(営業利益率50%超、全社営業利益の約3割)。2027年3月期は売上+10%の見通し。2025-03に250億円を投じABF原料の能力を5割増強(10年内に同規模を追加投資) | S20 technews(2026-06-23、2025-03-31) |
| 三井金属 | 2027年3月期の連結予想を上方修正: 売上8,300→8,500億円、営業利益910→940億円、純利益750→800億円。理由は極薄銅箔・AIサーバー向け電解銅箔の販売増。2026年3月期Q3累計の営業利益は717億円(+27.6%)。1→10株の株式分割も同時発表 | S24 松井証券ニュース、gyokaidigest |

### B1-2 途上性

| 項目 | 内容 | 出所ID・公表日 |
|---|---|---|
| 市場規模(現在→2030) | 先端ICパッケージ基板(有機AICS+ガラスコア+SLP+埋め込みダイ)は2030年に約310億ドル(Yole)。有機AICSは2024年に約142億ドル。Yoleの2026年版ページは年平均成長率9%と12%が併記され、**内部で不整合**。Counterpoint: AI用途が2030年に基板市場の金額の過半、AIチップ1個で従来PC用チップの約10倍のABFを消費 | S26 Yole、S1 Counterpoint(2026-03-11) |
| CoWoS 能力 | 2026年末に月12〜14万枚、2027年に約17万枚、2028年末に約26万枚(2028年までに倍増)。TSMCの2026年設備投資は600〜640億ドル(7月決算、別の出所では520〜560億ドルで食い違い) | S27 TrendForce(2026-09-14)他 |
| ガラスコア基板の量産時期 | 商用量産を確認した企業はない。SKC/Absolics: 2026年末の初出荷観測もあるが、7月決算説明会で台湾でのパッケージ級信頼性試験中、結果は年内。当初目標は2024年上期でスリップ済み。サムスン電機: 2027年下期。LGイノテック: 2028年。TSMC CoPoS: 最速2028年。インテル: 自社導入は2030年頃にずれ込み。Goldman(2026-07-08): 市場は本格採用を2030年以降と見ておりABFが当面主流 | S28 Tom's Hardware、TrendForce、S10 longbridge(2026-07-08) |
| T-glass の世代交代 | 日東紡は2028年の次世代T-glassを計画、顧客候補にNvidia・Appleなど(報道) | S11 TrendForce(2026-02-04) |
| T-glass 供給能力の増設と解消時期 | 福島事業センターに新工場棟(投資約150億円)、生産開始は2027年1〜3月。台湾紙は「最大3倍」と報じたが、全量を先端ロジック向けT布に充てた場合の数字。日経報道を引いた台湾紙は、需給の改善は2027年下半期の新能力稼働後と報じる。別の見方では2027年の新能力で増加は約20%にとどまる | S5 newswitch、S6 udn(日付不明)、S8の二次記事 |
| ABF基板の増設 | イビデン: 2027年度から順次稼働(S12)。ユニミクロン(台湾): 2026年1月の稼働率90%超、2026年設備投資の約70%がABF拡張(S29)。需給の解消は2027年以降(Counterpointは2027年に新設が立ち上がるまでギャップ拡大)との見方(S1/S2) | S12、S29、S1/S2 |
| HVLP銅箔の増設 | 三井金属ほか各社が拡張しても、2026年の能力はAIサーバー需要の約半分にとどまる(台湾報道)。三井金属は2026年8月にマレーシアで新用地を取得、2031年以降に新拠点(VSP・MicroThin)を設ける計画 | S25、S24(logi-today 2026-08) |

### B1-3 投資家の認知度

| 銘柄 | 株価動向 | 予想PER | アナリスト | 報道の扱い |
|---|---|---|---|---|
| イビデン(4062) | 年初来+292%(2026-06-26時点、ロイター)。その後も上昇: 9/18終値19,555円→9/24に+14.57%の22,405円(原因は不明、Nvidiaの新規受注は未確認)→9/25に23,345円(1/1分割後・10/1分割前の基準)。52週高値27,480円(7/1)。2月の5,000億円投資発表時に-12.7%(予想が市場期待を下回ったため)。新株発行(約525億円)の発表後に-9.1%との報道(時期は要約に明記なし、2026年とみられる)。2025年末の価格が取れず、**年初来・1年騰落率は自前では算出不能** | 65.0倍(9/18)→77.6倍(9/25)。EPS会社予想300.7円、1年後コンセンサス388.9円 | 12人。平均4.75(強気10、やや強気1、中立1)。目標株価コンセンサス23,783円(9/25の株価は目標水準に到達) | 「PER100倍超の是非」(semi-connect)、NVIDIA依存度への注意。ロイターは日本のAI関連株の高騰を報道 |
| 日東紡(3110) | 10/1: 3,350円。52週高値6,580円(5/7、分割調整後と推定)から約-49%(推計)。6/29に急騰後、7/1(-8.5%)、7/2(-8%)と下落。8/5決算(上方修正)の翌日に「材料出尽くし」で売られた。2025年8月にも「4倍近くまで急騰後、決算で急落」との記事。年初来・1年は算出不能 | 30.5倍(10/1、モネックス)、27.4倍(9/24、別ソース) | 7人。平均4.43。目標株価平均4,484円。Goldmanが7/8に「買い」へ引き上げ(目標株価は未確認) | 乱高下が大きい銘柄(台湾紙は「爆単で大幅上昇」と報道) |
| 味の素(2802) | 9/25終値5,051円。年初来高値6,166円(6/22)、安値3,270円(1/8)。安値比+54%(「年初来騰落率」ではない) | 39.1倍(9/25)。サイトにより38.1〜42.2倍 | 平均4.22。目標株価平均5,961円。Morningstar(日付不明)は「ワイドモート、価格決定力が強い、株価は概ね適正」 | Palliser Capital(英アクティビスト)が2026-03-31にABF価格の30%超値上げと電子材料の独立を要求。「味の素が95%超のシェア」説は根拠不明 |
| 三井金属(5706) | 10/5: 2,647.5円(分割後)。年初来安値は17,995円(1/5、分割前)で、分割調整後の1,799.5円から**約+47%**(「年初来騰落率」ではなく安値比) | 18.9倍(10/5、会社予想純利益800億円ベースとみられる)。9月下旬は16.2倍 | 目標株価コンセンサス4,577円(分割調整の有無は不明)。会社予想経常利益1,000億円(-26.9%)、コンセンサス約1,153億円(-15.7%) | 極薄銅箔(MicroThin)でほぼ独占的との記述(gendai.media) |

- **テーマETFの有無**: 未取得。
- **PEGの概算**: イビデンのみ試算可能。会社予想EPS300.7円→1年後コンセンサス388.9円(+29%)を成長率に使うと、PEGは約2.1〜2.7(PER60〜78倍÷29)。**成長率の定義が粗い参考値**。日東紡(純利益-52%)、味の素(純利益-8.3%)、三井金属(経常利益-26.9%)は会社予想が減益のため算出不能。
- **日本のAI関連株の全体感**: 2026-06-26のロイターは「日経平均は年初来+37%、太陽誘電+438%、村田製作所+268%、イビデン+292%」と報じ、半導体関連の集中リスクに触れている。第一生命経済研究所のレポートは、AIブームは「期待」から「収益化」を問われる転換点にあると分析(日付は不明)。

### B1-4 代表銘柄(日本または米国に本籍かつ主上場)

| 銘柄 | コード | 時価総額 | 直近売上成長(YoY) | 純度(テーマ売上比の目安) | 予想PER | 備考・出所 |
|---|---|---|---|---|---|---|
| イビデン | 4062 | 約6.6兆円(9/25、分割前) | 2027年3月期Q1: +26.4%。2026年3月期: +12.7% | 電子事業は売上の約58%(2,433億÷4,162億円、本メモで算出)、営業利益の約73%(452億÷620億円)。ただし電子事業にはAI基板以外も含む | 77.6倍(9/25) | NVIDIA依存。S12、S13、S15 |
| 日東紡 | 3110 | 6,319億円(10/1) | 2027年3月期Q1: +20.6% | **未取得**(スペシャルガラスが利益を牽引としか確認できず。T-glassの世界シェアは90%超との報道あり) | 30.5倍(10/1) | S7、S9。純利益は前期比-52%予想 |
| 味の素 | 2802 | 約4.94兆円(9/25) | 2027年3月期予想: 売上+9.4%。電子材料: 2026年3月期+31% | 営業利益の約3割(売上比は未取得) | 39.1倍(9/25) | S20、S23。純利益は前期比-8.3%予想 |
| 三井金属 | 5706 | 約1.52兆円(10/5) | **未取得**(2027年3月期売上予想8,500億円) | **未取得**(機能材料セグメント。極薄銅箔が主力) | 18.9倍(10/5) | S24。営業利益の前期比は資料間で食い違い |
| (未調査・候補) | レゾナック4004、ディスコ6146、TOWA 6315、古河電工5801(銅箔)、住友ベークライト4203、有沢製作所5208、日本電気硝子5214、AGC 5201、大日本印刷7912、TOPPAN HD 7911、Amkor(AMKR)、Onto Innovation(ONTO)、Entegris(ENTG)、Corning(GLW)、TTM(TTMI) | - | - | - | - | **訓練知識・未検証。検索予算枯渇により未調査**。新光電気(6967)は2025年にJIC連合のTOBで非上場化したとの記憶があるが未検証 |

**参考(ゲート外: 他国本籍・ADR)**: ユニミクロン、南亜電路板(Nan Ya PCB)、台湾玻璃(台玻)、建榮、金居(以上台湾)、Circuit Foil(ルクセンブルク)、Kingboard、SKC/Absolics、サムスン電機、LGイノテック(以上韓国)、BOE(中国)、TSMC(台湾、ADRあり)。いずれも出所内の言及のみで、数値は未取得。

### B1-5 弱気材料

| 材料 | 内容 | 出所ID・公表日 |
|---|---|---|
| 値上げの打ち止め | 日東紡は「計画済みのT-glass値上げはほぼ完了、追加予定なし」。決算翌日(8/6)は材料出尽くしで売られた | S3(2026-08-06)、S8の二次記事 |
| 株価の乱高下と高値からの下落 | 日東紡は5/7高値から約-49%(推計)。価格上昇だけでなく数量・利益の持続が問われる局面 | S9(10/1) |
| 会社予想が減益 | 日東紡の純利益-52%、味の素-8.3%、三井金属の経常利益-26.9%。一過性の要因かどうかは未確認 | S3、S23、S24 |
| 味の素のABF値上げ姿勢 | 一律値上げには慎重(アクティビストの要求と温度差)。能力拡大を優先する方針 | S22(2026-06-15) |
| 価格転嫁が一対一ではない | ABFフィルム+30%でも、基板コストへの影響は約3〜6%の推計 | S21 |
| 供給過剰化の芽(本補佐の解釈) | イビデン5,000億円、味の素+50%、ユニミクロンの増設、CoWoSの2028年倍増など、2027〜2028年に供給が一斉に立ち上がる。需要側の失速と重なれば需給が反転する可能性がある。**出所に明示された予測ではなく解釈** | S12、S20、S27 |
| ガラスコア基板の遅れ | 量産は2027〜2028年以降、Goldmanは2030年以降。ガラスコア関連の期待は後ろ倒し。一方でABF需要の延命要因にもなる | S28、S10 |
| 評価の高さ・集中 | イビデンはPER65〜78倍、NVIDIA依存。日経平均の約25%が半導体関連でロイターが集中リスクを指摘。新株発行の発表後に株価-9.1%(時期不明) | S15、S19、C1 |
| 非AI用途の圧迫 | 材料のAI向け優先配分でBT基板・中低位ABFが圧迫される(Counterpoint)。供給制約が成長の上限にもなる | S1 |
| ダブルオーダー・在庫調整の兆候 | **B1では確認できなかった**(未調査を含む) | - |

### B1 出所一覧(ID: URL / 公表日 / 種別)

- S1: https://counterpointresearch.com/de/reports/From-T-Glass-Crisis-Capacity-Erosion-The-Multi-Year-Substrate-Shortage / 2026-03-11 / 調査会社(要約のみ閲覧)
- S2: https://www.bestpcbs.com/blog/2026/08/abf-substrate-shortage/ / 2026-08 / 二次(S1の再掲)
- S3: https://www.trendforce.com/news/2026/08/06/news-nittobo-raises-fy2027-net-profit-forecast-by-jpy-3b-no-further-t-glass-price-hikes-planned/ / 2026-08-06 / 報道(日経引用)
- S4: https://info.fusionww.com/blog/the-greensheet-february-2026 、https://info.fusionww.com/blog/the-greensheet-may-2026 / 2026-02、2026-05 / 二次
- S5: https://newswitch.jp/p/47097 / 日付不明 / 報道
- S6: https://udn.com/news/story/7240/8972038 / 日付不明 / 台湾紙
- S7: https://www2.jpx.co.jp/disc/31100/081220260805509788_tse-qcedjpsm-31100-20260805331100-ixbrl.htm / 2026-08-05 / 決算短信(要約経由)
- S8: https://s.kabutan.jp/stocks/3110/news/k202608050138/ 、https://limo.media/articles/-/134583 / 2026-08-05前後 / 報道
- S9: https://scouter.monex.co.jp/report/chart/3110 、https://kabuyoho.jp/reportTarget?bcode=3110 、https://www.traders.co.jp/stocks/61_3110/ / 2026-10-01時点 / 株価サイト
- S10: https://longbridge.com/en/news/292008120.md / 2026-07-08 / 報道
- S11: https://www.trendforce.com/news/2026/02/04/news-nittobo-reportedly-plans-2028-next-gen-t-glass-customers-may-include-nvidia-apple-and-others/ / 2026-02-04 / 報道(噂ベース含む)
- S12: https://www.tousaiblog.org/ibiden-kessan 、https://www.logi-today.com/916977 、https://www2.jpx.co.jp/disc/40620/081220260731504718_tse-qcedjpsm-40620-20260804340620-ixbrl.htm / 2026-05-11、2026-08-04 / 個人ブログ・物流ニュース・決算短信(要約経由)
- S13: https://finance.technews.tw/2026/02/04/ibiden-plans-500-billion-investment-to-expand-ai-ic-substrate/ 、https://finance.technews.tw/2026/05/12/ibiden-profit-jumps-90-shares-hit-record-high/ / 2026-02-04、2026-05-12 / 報道
- S15: https://kabuyoho.jp/reportTarget?bcode=4062 、https://scouter.monex.co.jp/report/index/4062 / 2026-09-18〜25 / 株価サイト
- S16: https://www.jpx.co.jp/news/2020/20260915-01.html 、https://www.jpx.co.jp/news/2020/20251215-01.html / 2026-09-15、2025-12-15 / JPX(分割案内、内容は要約のみ)
- S17: https://traders.co.jp/premium/wadai / 2026-08-05前後 / 株価サイト(ストップ高・MS MUFGの格上げ(Underweight→Overweight、目標13,000→27,500円)の出所は特定できず)
- S18: https://www.debelegger.nl/post/er-kruipt-een-addertje-door-de-koerssprong-van-ibiden-en-het-heet-de-zwakste-schakel-van-nvidia / 2026-09-24前後 / ブログ(9/24の+14.57%は前営業日終値19,555円からの計算で整合)
- S19: https://semi-connect.net/ibiden-stock-investment-analysis-2026/ / 2026 / 個人ブログ
- S20: https://finance.technews.tw/2026/06/23/abf-drives-strong-performance-brokers-raise-target-prices-ajinomoto-consecutive-record-highs/ 、https://finance.technews.tw/2026/05/30/from-table-seasoning-to-monopolizing-95-ai-chip-materials-key-secrets-centennial-ajinomotos-cross-industry-dominance/ 、https://finance.technews.tw/2025/03/31/ajinomoto-increases-abf-substrate-raw-material-production-capacity-by-50/ / 2026-06-23、2026-05-30、2025-03-31 / 報道
- S21: https://www.digitimes.com/news/a20260513PD230.html 、https://wccftech.com/msg-maker-ajinomoto-to-raise-prices-as-abf-substrate-supply-demand-gap-extends-to-2027/amp/ 、https://www.taiwannews.com.tw/en/news/6359120 、https://atlaspcb.com/news/news-ajinomoto-abf-substrate-price-increase-2026 、https://www.digitalcitizen.life/ajinomoto-may-raise-abf-film-prices-as-ai-server-demand-tightens-supply/ / 2026-05-13前後 / 報道・二次
- S22: https://www.gigazine.net/news/20260615-ajinomoto-abf-product-more/ 、https://the-shashi.com/tse/2802/decisions/palliser-ajinomoto-abf-2026/ 、https://finance.technews.tw/2026/04/01/british-investment-fund-stakes-ajinomoto-demands-30-percent-abf-price-hike/ / 2026-06-15、2026-04-01 / 報道・分析
- S23: https://kabuyoho.jp/reportTarget?bcode=2802 、https://finance.matsui.co.jp/stock/2802/index 、https://www.kabutore.biz/pbrperhikaku/2802_per.html / 2026-09-25 / 株価サイト
- S24: https://finance.matsui.co.jp/news/606649/index 、https://gendai.media/articles/-/139457 、https://www.logi-today.com/989470 、https://www.ctee.com.tw/news/20260722700191-439901 、https://www.gyokaidigest.com/companies/mitsui-kinzoku/report/2026-Q3 、https://scouter.monex.co.jp/report/index/5706 / 2026-07〜10-05 / 報道・株価サイト
- S25: https://eu.36kr.com/en/p/3984081016470532 、https://www.moneyweekly.com.tw/_Article?AID=227371 、https://www.webull.ca/news-detail/15399957527356416 、https://www.nextpcb.com/blog/pcb-shortage-2026-price-lead-time / 2026 / 二次
- S26: https://www.yolegroup.com/press-release/pushed-by-glass-core-and-high-end-ics-substrates-for-ai-the-advanced-ic-substrate-market-reaches-31-billion-by-2030/ 、https://www.yolegroup.com/product/report/status-of-the-advanced-ic-substrate-industry-2026/ / 2025、2026 / 調査会社
- S27: https://www.trendforce.com/news/2026/09/14/news-tsmc-reportedly-targets-22-2nm-16-3nm-capacity-boost-by-mid-2027-cowos-to-double-by-2028/ 、https://www.digitalcitizen.life/tsmc-reportedly-plans-to-double-cowos-capacity-by-2028-as-ai-packaging-demand-keeps-rising/ 、https://www.tipranks.com/news/tsmc-expands-ai-chip-packaging-as-supply-limits-shift / 2026-09-14前後 / 報道
- S28: https://tomshardware.com/tech-industry/manufacturing/glass-substrate-roadmap-examined 、https://www.trendforce.com/news/?p=64462 、https://www.itiger.com/news/1110725196 / 2026 / 報道
- S29: https://www.trendforce.com/news/?p=42467 、https://www.taiwannews.com.tw/news/6277173 、https://onmsft.com/?p=59050 、https://news.tvbs.com.tw/english/3179482 / 2026 / 報道

---

## B2 光インターコネクト

**注意: 本テーマは検索予算の枯渇により、Lumentum と Coherent の決算、InP供給、CPO時期、市場規模の一部しか取得できていない。日本銘柄・株価・弱気材料は大部分が未取得。**

### B2-1 需要の強烈さの証拠

| 項目 | 数値・内容 | 出所ID・公表日 | 信頼度 |
|---|---|---|---|
| Lumentum 売上 | 2026年度Q4(2026-06-27終了): 売上10.063億ドル(前年同期比+109.3%、前期比+24.5%)。2026年度通期は約30.1億ドル。2027年度Q1ガイダンスは12.25〜12.75億ドル、非GAAP営業利益率39.5〜40.5%。現金等27億ドル | T1 SEC 8-K(2026-08)、T2 | 一次(8-K、要約経由) |
| Lumentum の供給不足 | CEOは2026年7月、EMLとポンプレーザーの出荷が顧客需要を**30%超下回る**と発言(TrendForce経由)。NvidiaやハイパースケーラーからのEML要求量は、従来の通信顧客の「数百個」から「数億個」規模へ。2026年末までにEML能力を2025年末比で50%超増強 | T3 TrendForce(2026-08-06) | 二次(報道引用)。数値は他で未確認 |
| Nvidia の増産支援 | 2026年3月、Nvidiaが2社の主要サプライヤーに各20億ドルをコミットし長期供給契約を締結(**社名は検索結果上では特定できず**)。これは「顧客負担の増産投資」の実例 | T3 | 二次・単一 |
| Coherent 売上 | 2026年度Q4(2026-06-30終了、8/12発表): 売上20.5億ドル(+34%、プロフォーマ+42%)、非GAAP粗利益率40.2%、非GAAP EPS 1.74ドル。データセンター・通信16.2億ドル(+58.6%、売上の79%)、産業4.305億ドル(-15.8%)。2027年度Q1ガイダンスは22〜24億ドル | T4 SEC 8-K(2026-08-12)、T5 | 一次(要約経由) |
| Coherent の受注状況 | 2027年度はほぼ完売(二次の光学専門サイトの記述)。800G販売は伸び続け、1.6Tは2026〜2027年に急増する見通し | T6 photoncap、T5 Futurum | 二次・単一 |
| EML供給の逼迫 | Yole: EML能力は大口顧客に事前割当され、リードタイムが延び、モジュールメーカーとクラウド事業者が代替設計を探している。**リードタイムの週数は取得できず**(定性的記述のみ) | T7 Yole | 調査会社 |
| 受注残 | **LITE・COHRとも取得できず** | - | 未取得 |
| 価格改定 | **取得できず** | - | 未取得 |

### B2-2 途上性

| 項目 | 内容 | 出所ID・公表日 |
|---|---|---|
| 市場規模(現在) | AI向け光トランシーバ市場は2025年に165億ドル→2026年に260億ドル(+57%)(TrendForce、naddod経由)。LightCounting: 800G出荷は2026年に倍増以上、1.6Tの売上は初めて20億ドル超 | T8 naddod(日付不明)、T9 LightCounting |
| 市場規模(2030) | **2030年値は取得できず**。LightCountingの2024年見通しでは1.6T+3.2T(LPO・CPO含む)が2029年に約100億ドル(古い) | T9、T10 Lightwave |
| 世代交代: 1.6T | 2026年に商用化。EMLが200G/レーンの1.6Tプラガブルの主光源。**Lumentumは200G/レーンEMLの唯一の量産出荷者**との記述(二次・単一) | T7、T11 xenospectrum |
| 世代交代: CPO | Nvidiaは2026年7月下旬までにSpectrum-X CPOスイッチを一部パートナーへ出荷開始、Broadcomは51.2T「Bailly」を限定出荷、102.4Tの「Tomahawk 6-Davisson」はサンプル出荷(TrendForce 2026-07-27)。スケールアウト向けCPOの売上は2026年下期(Coherent)、スケールアップ向けは2027年(Coherent)/量産出荷2027年下期・顧客導入2028年(Lumentum)。Cignal AIはスケールアップ向けCPOの展開を2028年末〜2029年初と予想 | T12 TrendForce(2026-07-27)、T13 Cignal AI(2026-04)、T14 onmsft |
| CPOの浸透度 | AI光通信モジュールに占めるCPOの比率は2026年に約0.5%、2030年に3割台との試算(複数の調査会社とされるが出所は特定できず)。2026年の主役は800G〜1.6Tプラガブル | T15 penchan |
| 供給能力の増設と解消時期 | Lumentum: 2026年末にEML能力+50%超(2025年末比)。Coherent: 6インチInPへ移行中(テキサス・スウェーデン)、社内InP能力を2027年末までにさらに2倍超、基板等の重要資材は確保済み。アナリストは需給の不均衡が2027年以降も続くと見る。Nvidiaが出資した別の1社は6インチウェハ能力を2倍にし2027年末までに再拡張、もう1社は6インチ設備を改修し2028年に量産 | T3、T4/T5 |
| ボトルネックの移動 | シリコンフォトニクスは制約をEMLからCWレーザー、SiPhファウンドリ歩留まり、KGDテスト、光結合、実装へ移すだけ(ブログ記述、低信頼) | T16 borecraft |

### B2-3 投資家の認知度

**取得できず。** 代表銘柄の過去1年・年初来の株価騰落率、予想PER、EPS成長率、PEG、アナリストカバー数、テーマETFの有無、報道の「過熱」「バブル」言及は、今回の検索では確認できなかった。

- 参考: 2026-06-26のロイターは、日本の半導体関連が日経平均の時価総額の約25%を占め、集中がリスクと指摘(C1)。光関連の個別言及は確認できていない。ただし、Reutersのこの記事が古河電工(5801)のページにも掲載されている(言及内容は未確認)。
- 参考: Lumentumの2026年度Q4は、転換社債の株式転換に伴う72億ドルの純損失(うち78億ドルが債務消滅に伴う非現金費用)を計上(T1)。希薄化・会計上の変動に注意。

### B2-4 代表銘柄(日本または米国に本籍かつ主上場)

| 銘柄 | コード/ティッカー | 時価総額 | 直近売上成長(YoY) | 純度(テーマ売上比の目安) | 予想PER | 備考・出所 |
|---|---|---|---|---|---|---|
| Lumentum | LITE(Nasdaq) | **未取得** | 2026年度Q4: +109.3% | **未取得**(クラウド・AI向けが急増している旨のみ確認) | **未取得** | T1。GAAP純損失72億ドルは転換社債の転換による一過性 |
| Coherent | COHR(NYSE) | **未取得** | 2026年度Q4: +34%(プロフォーマ+42%) | データセンター・通信が売上の79%(通信を含むため純度の上限値) | **未取得** | T4。産業は-15.8% |
| (未調査・候補・米国) | Fabrinet(FN、NYSE上場だがケイマン籍で本籍の扱いに注意)、Credo(CRDO、同じくケイマン籍で要注意)、Applied Optoelectronics(AAOI)、Ciena(CIEN)、Corning(GLW)、Broadcom(AVGO)、Marvell(MRVL)、Astera Labs(ALAB)、MACOM(MTSI) | - | - | - | - | **訓練知識・未検証。未調査** |
| (未調査・候補・日本) | 古河電工(5801)、フジクラ(5803)、住友電工(5802)、住友大阪セメント(5232、光変調器)、santec(6777)、浜松ホトニクス(6965)、アンリツ(6754)、SWCC(5805) | - | - | - | - | **訓練知識・未検証。未調査** |

**参考(ゲート外: 他国本籍・ADR)**: 検索結果内で具体名は確認できていない。候補は中国のInnolight・Eoptolink・Accelink、台湾の光デバイス各社(訓練知識・未検証)。

### B2-5 弱気材料

| 材料 | 内容 | 出所ID・公表日 |
|---|---|---|
| 需要反転リスクの注意 | LightCounting(2024年のニュースレター): NvidiaやクラウドによるOptics購入が鈍れば市場の力学が反転しうる | T9(日付は2024-09) |
| 技術代替(EML回避) | EML能力が事前割当で逼迫し、モジュールメーカー・クラウド事業者が**代替設計**(シリコンフォトニクス等)を探している | T7 Yole |
| 技術代替(CPO) | CPOは2026年にはAI光モジュールの約0.5%だが、2030年に3割台との試算が事実なら、従来プラガブル中心のトランシーバ企業の収益源を長期では侵食しうる(**本補佐の解釈**) | T15 |
| CPOの時期の不確実性 | 2025年のBofAはNvidiaのEthernet CPOを2027年下期と予想(今回の2026年出荷開始は前倒し)。2025年4月のBenzingaはNvidiaのCPO推進に遅れの可能性を報じていた。時期は何度も動いている | T14、T17 Benzinga(2025-04) |
| 事業構成の弱さ | Coherentの産業向けは-15.8% | T4 |
| 需要量の見かけの膨張(解釈) | 要求量が「数百個」から「数億個」へ跳ね上がっている点は、ダブルオーダーの可能性を検討すべき材料(**出所は事実のみを述べており、ダブルオーダーとは書いていない**) | T3 |
| 価格下落・在庫調整・供給過剰 | **取得できず** | - |

### B2 出所一覧

- T1: https://www.sec.gov/Archives/edgar/data/0001633978/000162828026055726/lite_ex991xq4fy26.htm 、https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Fourth-Quarter-and-Full-Fiscal-Year-2026-Results/default.aspx / 2026-08-11前後 / 一次(要約経由)
- T2: https://www.kucoin.com/news/flash/lumentum-q4-2026-revenue-hits-1-01-billion-up-109-3-yoy / 2026-08 / 二次
- T3: https://trendforce.com/news/2026/08/06/news-inp-shortage-emerges-as-ai-optical-interconnect-bottleneck/ 、https://www.ledinside.com/news/2026/08/2026_08_06_01 / 2026-08-06 / 報道
- T4: https://www.sec.gov/Archives/edgar/data/0000820318/000119312526346860/d128030dex991.htm 、https://www.coherent.com/news/press-releases/fourth-quarter-and-fiscal-year-2026-results / 2026-08-12 / 一次(要約経由)
- T5: https://futurumgroup.com/insights/coherent-q4-fy-2026-earnings-1-6t-transceivers-ramp-cpo-revenue-approaches/ 、https://www.sdxcentral.com/news/coherent-q4-financials-see-supply-chain-wins-and-scale-across-opportunity/ / 2026-08 / 二次
- T6: https://photoncap.net/p/coherent-fq4-2026-inp-capacity-cponpo / 2026-08 / 二次(個人系)
- T7: https://www.yolegroup.com/strategy-insights/opinion-optical-transceivers-at-the-chokepoint-of-ai-growth-and-supply-chain-constraints/ / 2026 / 調査会社
- T8: https://www.naddod.com/pt/blog/ai-boom-fuels-optical-transceiver-surge / 日付不明 / 二次(ベンダーブログ)
- T9: https://lightcounting.com/document/march-2026-ethernet-optics/382/toc 、https://www.lightcounting.com/newsletter/en/september-2024-ethernet-optics-296 / 2026-03、2024-09 / 調査会社(目次・要約のみ)
- T10: https://www.lightwaveonline.com/home/article/55130661/ethernet-optical-transceivers-for-ai-to-double-in-2024 / 2024 / 報道
- T11: https://xenospectrum.com/en/lumentum-inp-ai-optics-shortage/ / 2026 / 二次
- T12: https://trendforce.com/presscenter/news/20260727-13151.html / 2026-07-27 / 報道
- T13: https://cignal.ai/2026/04/cpo-and-elsfp-1q26-update/ / 2026-04 / 調査会社(有料壁)
- T14: https://onmsft.com/?p=60157 、https://www.digitalcitizen.life/nvidia-optics-partners-say-co-packaged-optics-rollout-remains-on-track/ / 2026 / 二次
- T15: https://penchan.co/en/market/ai/supply-chain/cpo/ / 日付不明 / 二次
- T16: https://borecraft.com/?p=14842 / 日付不明 / ブログ(低信頼)
- T17: https://www.benzinga.com/25/04/44653936/broadcom-and-marvell-poised-for-growth-as-nvidias-cpo-push-faces-delays-analyst-reveals?nid=44665469 / 2025-04 / 報道

---

## B3 半導体テスト・プローブカード・検査装置

**注意: 本テーマは検索予算の枯渇により、アドバンテスト(6857)の決算と株価しか取得できていない。プローブカード、HBM特化の需要、米国銘柄、市場規模、弱気材料の詳細は未取得。**

### B3-1 需要の強烈さの証拠

| 項目 | 数値・内容 | 出所ID・公表日 | 信頼度 |
|---|---|---|---|
| アドバンテスト 2027年3月期Q1(2026/4-6月) | 売上3,675億円(+39.3%)、営業利益1,900億円(+53.3%)、営業利益率約51.7%(本メモで算出)。四半期の過去最高。税引前利益・純利益には戦略投資に関連する金融商品の評価益が含まれる(本業は営業利益で見るべきとの指摘) | U1 minkabu/gyokaidigest(2026-07-29)、U2 会社資料 | 決算要約(原本未開封) |
| 通期予想の上方修正 | 売上1兆7,140億円、営業利益8,460億円(発表前のコンセンサス営業利益は約6,926億円)。修正理由は推論用AI半導体向けのテスト需要が想定を大きく上回ること | U1、U2(2026-07-29) | 同上 |
| 経営陣の発言 | 決算説明会で「GPU・カスタムASIC・CPU全般でSoCテスタ需要が非常に強い。今年中も来年も持続する見通し」。テスタ市場は過去最大規模、SoC・メモリ両方で4月時点の想定を上回る。**能力増強を加速、当初計画を前倒し** | U3 会社Q&A資料(2026-07-29)ほか | 要約(Q&A原文は未開封) |
| 受注残・リードタイム・価格改定・前払い | **取得できず** | - | 未取得 |
| HBM向けテスト | **取得できず**。メモリ価格の逆風に言及する市場要約があるのみ | - | 未取得 |
| プローブカード(日本マイクロニクス・日本電子材料・FormFactor・Technoprobe) | **未調査** | - | 未取得 |

### B3-2 途上性

**取得できず**(市場規模の現在値・2030年見通し、世代交代、供給能力増設の計画は未取得)。アドバンテストが能力増強を前倒ししていること、テスタ市場が過去最大規模になる見通しであることのみ確認(U2、U3)。

### B3-3 投資家の認知度

| 銘柄 | 株価動向 | 予想PER | アナリスト・報道 |
|---|---|---|---|
| アドバンテスト(6857) | 7/29決算後に+11%の27,935円(Reuters要約の記述。元記事URLは特定できず、U5周辺)。9/28終値33,730円、9/29 33,280円、**10/2 38,630円**(単一出所)。決算後の27,935円から10/2まで約+38%。年初来・1年騰落率は算出不能(年初価格未取得) | 36.5倍(9/29、会社予想EPS 911.1円)→**42.4倍**(10/2、時価総額28.28兆円)。コンセンサスEPS(2027/3期)928.4円 | 目標株価コンセンサス42,787円(株価は10/2時点で目標を下回る)。2025年10月の報道は「PER44倍でNVIDIAの31倍を上回る」とAIバブル論を紹介。Reutersは半導体関連の集中リスクに言及 |

- 10/2の38,630円は9/29から3営業日で+16%。**株探(kabuyoho)の単一出所のため、要確認**。
- PEG: 前期EPSが未取得のため**算出不能**。

### B3-4 代表銘柄(日本または米国に本籍かつ主上場)

| 銘柄 | コード/ティッカー | 時価総額 | 直近売上成長(YoY) | 純度(テーマ売上比の目安) | 予想PER | 備考・出所 |
|---|---|---|---|---|---|---|
| アドバンテスト | 6857 | 約28.3兆円(10/2)。9/29は約24.4兆円 | 2027年3月期Q1: +39.3% | テスタ専業に近い(AI向け比率は**未取得**) | 42.4倍(10/2) | U1、U4、U5。営業利益+53.3%。純利益は評価益込み |
| (未調査・候補・日本) | 日本マイクロニクス(6871、プローブカード)、日本電子材料(6855、プローブカード)、東京精密(7729、プローバ)、東京エレクトロン(8035、プローバは一部)、ヨコオ(6800、ソケット)、エンプラス(6961、ソケット)、山一電機(6941)、レーザーテック(6920、検査)、SCREEN HD(7735) | - | - | - | - | **訓練知識・未検証。未調査** |
| (未調査・候補・米国) | Teradyne(TER)、FormFactor(FORM)、Cohu(COHU)、Aehr Test Systems(AEHR)、Onto Innovation(ONTO)、KLA(KLAC) | - | - | - | - | **訓練知識・未検証。未調査** |

**参考(ゲート外: 他国本籍・ADR)**: Technoprobe(イタリア)、Camtek・Nova(イスラエル)、MPI・CHPT・Chroma・KYEC(台湾)、Hanmi Semiconductor・Leeno・ISC(韓国)(**訓練知識・未検証。未調査**)。

### B3-5 弱気材料

| 材料 | 内容 | 出所ID・公表日 |
|---|---|---|
| 評価の高さと「AIバブル」論 | 2025年10月時点でアドバンテストのPERは44倍とNVIDIAの31倍を上回り、AIバブルの議論が出ていた。10/2の予想PERは42.4倍 | U6 longportapp(2025-10)、U4 |
| 市場全体の調整懸念 | 大手銀行が株式市場の調整を警戒してアドバンテストが-7%となった日がある(Reuters、11月5日、**年は不明**) | U7 stockopedia |
| 供給側の対応 | アドバンテスト自身が能力増強を前倒し。需要が鈍れば固定費負担になりうる(本補佐の解釈) | U3 |
| メモリ価格の逆風 | 利益率は高いがメモリ価格の逆風があるとの市場要約(具体的出所は特定できず) | U2周辺の市場要約 |
| 利益の質 | 純利益には戦略投資の評価益が含まれる | U1 |
| 半導体集中リスク | 半導体関連が日経平均の約25%(ロイター2026-06-26) | C1 |
| 在庫調整・ダブルオーダー・価格下落・技術代替 | **取得できず** | - |

### B3 出所一覧

- U1: https://www.gyokaidigest.com/companies/advantest/report/2027-Q1 、https://minkabu.jp/stock/6857/settlement 、https://scouter.monex.co.jp/news/detail/6857_20260729_act_20260729_153012_6 / 2026-07-29 / 決算要約
- U2: https://www.advantest.com/en/news/2026/qnpuno0000000cqk-att/E_Info_20260729.pdf 、https://www.advantest.com/document/ja/investors/ir-library/result/JE_BIZ_260729_note.pdf / 2026-07-29 / 会社資料(要約経由、原本未開封)
- U3: https://www.advantest.com/document/ja/investors/ir-library/result/JE_BIZ_260729_QA.pdf / 2026-07-29 / 会社Q&A(要約経由)
- U4: https://scouter.monex.co.jp/report/index/6857 、https://kabuyoho.jp/sp/report?bcode=6857 / 2026-09-29、2026-10-02 / 株価サイト
- U5: https://www.stockopedia.com/share-prices/advantest-PNK:ATEYY/news/advantest-raises-full-year-operating-profit-forecast-by-24-on-strong-ai-demand-019e69d7-5988-7ef3-bf4f-dead2773ea4b/ / 2026(日付不明) / Reuters再掲。通期営業利益予想の引き上げ幅は見出しで24%、別の要約では35%と食い違う(本メモは会社資料ベースの8,460億円を採用)。「営業利益3,000億円vs2,420億円」の記述は年ラベルが誤りとみられ不採用。7/29決算後に+11%で27,935円との記述はReuters要約によるが、元記事URLは特定できず
- U6: https://longportapp.cn/news/262528639 / 2025-10 / 報道
- U7: https://www.stockopedia.com/share-prices/advantest-PNK:ATEYY/news/japan-apos-s-nikkei-falls-2-to-track-wall-street-apos-s-sharp-decline-019e69f3-1912-7784-9ce6-d4d5a8c23a95/ / 年不明 / Reuters再掲

### 共通出所

- C1: https://www.nst.com.my/amp/business/corporate/2026/06/1473119/nikkeis-record-rally-shifts-gears-investors-chase-next-ai / 2026-06-26 / Reuters(Junko Fujita)再掲

---

## 付録: 次に取るべき追加調査(優先順)

1. **B3**: プローブカード各社(日本マイクロニクス・日本電子材料・FormFactor・Technoprobe)の受注・稼働率・HBM/GPU向け比率、Teradyne・FormFactorの直近決算、HBMテスト市場規模(2030年)、バーンイン需要
2. **B2**: Fabrinet・Credo・AAOI・Ciena・Corning・Broadcom/Marvellの直近決算と株価指標、古河電工・フジクラ・住友電工の光事業比率と受注、2030年の光トランシーバ市場規模、LPO/CPOによる代替の定量評価、Innolight等の価格競争
3. **B1**: 日東紡・イビデン・味の素の受注残とリードタイム(IR資料)、年初来・1年騰落率の実測、レゾナック・ディスコ・日本電気硝子・大日本印刷・Amkor・Ontoの個別数値、顧客の前払い・長期契約の実例
4. 全テーマ: テーマETFの有無、アナリストカバー数(米国銘柄)、予想EPS成長率とPEGの再計算
