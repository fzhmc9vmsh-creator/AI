# S3 スカットルバット/業界データ: Oracle (ORCL) OCI 事業

作成日: 2026-10-11 / 担当: 株式調査アシスタント(事実と出典の整理のみ。投資判断は含まない)

## 0. 調査の制約と読み方(必ず先に読むこと)

- 取得手段は WebSearch の要約結果のみ。WebFetch は全ドメインで DNS 解決に失敗(elpasomatters.org, epoch.ai, investor.oracle.com, investors.coreweave.com, silicondata.com で確認)し、原典本文は 1 件も直接読めていない。以下の数値はすべて「検索結果の要約に書かれていた内容」であり、原典との突合は未実施。
- WebSearch の回数上限(1ターン200回、全エージェント共有)に途中で到達し、追加検索ができなかった。このため、5節の CoreWeave/Nebius の受注残・capex、2節の各社の耐用年数(10-K値)、6節(求人・価格改定・DB値上げ・マルチクラウドDB・人員削減)は未調査または不十分。8節に列挙。
- Tier の付け方: 1=会社開示、2=規制当局・公的統計、3=報道・調査会社、4=ブログ・SNS・ベンダー販促ページ。会社開示や規制当局書類でも、今回は報道経由でしか見ていないものは「Tier 3(原典: Tier 1/2)」と表記した。
- 出典は [S番号] で 7 節の一覧に対応。出典間で数値が食い違う箇所は、片方を選ばず併記し、8 節にも再掲した。
- 検索結果の中には、日付が付いていない記事、他メディアの転載、ベンダー販促ページが含まれる。その場合は Tier 4 とし、信頼度が低いことを明記した。

---

## 1. GPU レンタル単価の推移(2024〜2026年)

### 1-1. Silicon Data 指数(H100 / H200 / B200)

| 項目 | 数値 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| H100 ハイパースケーラー中央値 | 約 $7.76/GPU時(2023年末)、$7.92(2024年1〜5月、レンジ $7.37〜8.24) | 2023年末〜2024年5月 | Silicon Data ブログ [S1](検索要約) | 3(原典: 調査会社の公表値) |
| H100 Silicon Data 指数 | $3.06 | 2024年9月 | Introl [S2](Silicon Data を引用) | 4 |
| H100 Silicon Data 指数 | $2.36(2024年9月比 -23%) | 2025年6月 | Introl [S2] | 4 |
| AWS H100 値下げ | 約 -44% | 2025年6月 | Introl [S2] | 4 |
| H100 ネオクラウド指数 | $2.00 → $2.20(4週間で +10%) | 2025-12-09 → 2026-01-06 | Silicon Data 要約 [S3] | 3 |
| H100 ネオクラウド指数 | $2.57 | 2026-05-04 | Silicon Data 2026-08-04 分析 [S4] | 3 |
| H100 ネオクラウド指数 | $2.75(6月に往復を挟んだ後) | 2026-07-27 | Silicon Data 分析 [S4] | 3 |
| H100 ネオクラウド / ハイパースケーラー | $2.80 / $7.19 | 2026-08-02 | 二次記事が Silicon Data を引用 [S3] | 3〜4 |
| H100 指数ページ表示値 | $2.53(日付表示なし) | 取得時点不明 | Silicon Data 指数ページ [S5] | 3 |
| H100(別報) | 「2026年1月に2ドル弱 → 3ドル近く」 | 2026-08-04 報道 | 科技新報 (technews.tw) [S6] | 3 |
| H200 指数 | $3.09(12週で +14.4%) | 2026-07-27 | Silicon Data [S4] | 3 |
| H200 指数 | $3.16(8月2日)/ $3.10(指数ページ、日付なし) | 2026-08-02 | [S3][S7] | 3 |
| B200 指数 | $5.66 | 2026-08-02 | [S3] | 3 |
| B200 指数(SDB200RT) | 9月初 $5.62(年初来 +27.6%)。8月の日次は $5.58〜5.69 の狭いレンジ | 2026-09 初 | Silicon Data 8月更新 [S8] | 3 |
| 第三者掲載値(方法論不明) | B200 $6.42 / H200 $4.55 / H100 $3.06 | 2026-09-06 | StockHub [S9] | 4(Silicon Data の値と不一致、参考扱い) |

### 1-2. SemiAnalysis・Ornn・その他

| 項目 | 数値 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| SemiAnalysis H100 1年契約指数 | 約 $1.70 → 約 $2.35(+約40%) | 2025年10月 → 2026年3月 | SemiAnalysis 指数ローンチ記事の要約 [S10][S11] | 3 |
| SemiAnalysis の説明(要約) | オンデマンド容量は全 GPU 種で売り切れ。H100 の契約は数年前の元の単価のまま更新され、一部は2028年まで延長。指数は100社超への月次調査 | 2026年初 | [S10] | 3 |
| Ornn B200 価格 | 約 $2.31(3月初)→ $4.95(4月下旬)。B200 と H200 の価格差 $0.28 → $1.80 | 2026-03〜04 | Tom Tunguz(Ornn データを使った解説)[S12] | 3〜4(予測部分は筆者の意見) |
| Ornn 指数(OCPI) | 約定ベースの現物取引から算出。Bloomberg Terminal に掲載(2026年4月)。ICE が OCPI 連動の現金決済 GPU 先物を予定(2026年5月発表、規制当局の承認待ち) | 2026-04〜05 | [S13][S14] | 3 |
| CME と Silicon Data | コンピュート先物で提携 | 2026年 | Silicon Data ページ [S1] | 3 |
| UOB リサーチ | レンタル単価は Blackwell/B200、H100/H200、A100 のすべてで上昇。A100 80GB PCIe は約 $1.44/時 | 2026年6月 | UOB「Compute is Revenue」[S15](検索要約) | 3 |
| H100 の全体レンジ | 2026年2Q は $1.80〜3.50/時(2024年初は $8〜10)。シングル GPU オンデマンドは $2〜7、中央値約 $3.37 | 2026年 | Akash(ベンダー)[S16]、Spendark [S17] | 4 |
| 最安提示 | H100 で $0.99〜1.00/時の提供者あり | 2025-12 | Introl [S2] | 4 |
| 中国市場 | H100 の3か月短期レンタルは受付、期間満了時に長期契約へ切り替える優先権あり(長期へ誘導) | 2026-07 | SMM [S18] | 3 |

### 1-3. GB200 / GB300(B300)

| 項目 | 数値 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| GB200 | GMI Cloud $8.00/GPU時(1構成のみ追跡) | 取得時点不明 | computeprices.com [S19] | 4 |
| GB200 | 最安オンデマンド $10.50/GPU時、8社平均約 $18 | 取得時点不明 | deploybase.ai [S20] | 4(上と食い違う) |
| GB200 NVL72 ラック | 1ラック $200〜300/時の推定(1GPUあたり約 $3〜4 に相当) | 2026-03 | ガイド記事 [S20] | 4(推定値) |
| B300(GB300級) | 67社・25か月の追跡で中央値 $8.23/時、最安 RunPod $6.94、NeevCloud DGX B300 は $5.00〜 | 2026年 | Cyfuture ブログ [S21] | 4(自社販促) |
| 検索で得られた総括 | GB200/GB300 級のネオクラウド オンデマンドは概ね $5〜10/GPU時(信頼度低)。GB300 NVL72 の1GPU時あたりの信頼できる基準値は見つからず | — | — | — |

### 1-4. 旧世代の再契約単価・中古価格

| 項目 | 数値 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| 再契約単価 | SemiAnalysis: 1年契約が上昇(上記)。UOB: A100 も上昇。Silicon Data: H100/H200 とも2026年に上昇 | 2026年 | [S10][S15][S4] | 3 |
| CoreWeave | 2026年7月に全 SKU で約25%値上げ(Q2決算説明会、8月11日に開示とされる)。さらに約10%の追加値上げが直近2〜3か月内にあったとの報道(1社のみ)。公開オンデマンド H100 は $6.16/GPU時 | 2026-07〜08 | Spheron [S22](競合の二次情報)、Insider Monkey [S23] | 4 |
| CoreWeave 公式PR | 6月30日以降、より高い価格で新規容量の契約を継続。Q3の3〜6か月の短期契約は約 $40M/MW(単位の詳細は未確認) | 2026-09-17 | CoreWeave IR [S24](検索要約のみ。原文は取得失敗) | 3(原典: Tier 1) |
| H100 中古価格 | 2023年末 約 $40,000 → 現在 $12,000〜22,000(Servnet)。$18,000〜22,000 で安定(GPUnex)。Exit Technologies のオークションで H100 SXM5 が2026年1月までに34%下落 | 2026年 | Servnet [S25]、GPUnex [S26] | 4(Exit のオークション値を引用した部分は参考価値あり) |
| 再生品 | 新品価格の約84〜85% で推移 | 2026年 | Servnet [S25] | 4 |
| 今後の見通し | Blackwell の一般提供で H100 中古価格がさらに10〜20%下落するとの見方 | 2026年 | Servnet [S25] | 4 |
| A100 80GB 中古 | $12,000〜18,000 | 2026年 | GPUnex [S26] | 4(裏付けなし、信頼度低) |

**事実要約(1節)**
- レンタル単価は、2024年初の $8 前後から2025年にかけて $2〜3 に下落した後、2025年10〜12月を底に2026年は上昇に転じている(H100 ネオクラウド指数 $2.00(2025-12)→ $2.75〜2.80(2026-07/08)、SemiAnalysis の1年契約指数 +約40%)。
- 旧世代(H100/H200/A100)も値上がりを示す報道が複数ある(Silicon Data、SemiAnalysis、UOB)。要因は需要超過と推論効率向上、新規容量のリードタイム長期化と説明されている。
- 一方、中古の売買価格は H100 で $40,000 → $12,000〜22,000 と大幅に下落したままで、レンタル単価の回復と中古価格は同じ方向に動いていない(Tier 4 中心のため精度は低い)。
- ハイパースケーラーのオンデマンド H100 は $7.19(2026-08-02)で、ネオクラウド $2.80 の約2.6倍。OCI の実際の契約単価は今回の調査では取得できていない。

---

## 2. OCI の AI レンタル事業の採算と耐用年数の議論

### 2-1. The Information 報道と会社側説明

| 項目 | 数値・内容 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| NVIDIA サーバーのレンタル売上 | 約 $9 億(2025年6〜8月の3か月)。1年で約3倍 | 2025-10-07 報道 | The Information(内部資料に基づく)を各紙が引用 [S27][S28][S29] | 3 |
| 同 売上総利益 | 約 $1.25 億(粗利率 14%) | 同上 | 同上 | 3 |
| 粗利率の過去推移 | 1年間で10%未満〜20%強、平均約16% | 同上 | [S27][S28] | 3 |
| 含まれる費用 | 人件費・電力・その他直接費・一部の減価償却。計上されていない減価償却を加えるとさらに約7ポイント低下 | 同上 | [S27] | 3 |
| Blackwell レンタルの損失 | 同四半期に約 $1 億近い損失(Sherwood の報道) | 同上 | [S30] | 3(上の粗利益プラスとの整合は未確認) |
| 当時の株価反応 | ORCL 約 -5%(取引時間中 -2.5%の報もあり) | 2025-10-07 | [S30][S31] | 3 |
| 会社側説明 | ラスベガスの投資家向けイベントで、6年・総額 $600 億の AI インフラ契約の例を示し、契約期間通算の粗利率を35%と説明。Magouyrk 共同CEOは「最大級の顧客にも当てはまる例示」と発言。Goldman Sachs も同水準(約35%)の分解を提示 | 2025年10月 | iTiger(要約)[S32] | 3(原典: Tier 1 の説明) |
| 会社側説明(その後) | AI アクセラレータの粗利率は30〜40%と、2026年3月・6月にも Magouyrk が言及 | 2026-03、2026-06 | 検索結果の要約 [S32][S33] | 3 |
| 備考 | 依頼文にあった「30〜35%」の表現は見つからず、見つかったのは「35%(例示)」と「30〜40%(レンジ)」。四半期の粗利率(14%)と契約期間通算の見込みは測る対象が異なり、直接比較できない | — | — | — |

### 2-2. 耐用年数・経済的寿命の議論

| 項目 | 数値・内容 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| Michael Burry の主張 | ハイパースケーラーは GPU/サーバーの耐用年数を、NVIDIA の2〜3年の製品サイクルに比べて長く設定し、利益を押し上げている(「資産寿命の延長は現代で最も一般的な不正の1つ」と X に投稿) | 2025-11 | Saxo [S34]、Techstrong [S35] | 3 |
| Burry の試算 | 2026〜2028年の減価償却の過小計上は累計 $1,760 億。2028年までに Oracle の利益は26.9%、Meta は20.8%過大 | 2025-11 | TipRanks [S36] | 3 |
| 名指し先 | Meta, Alphabet, Microsoft, Oracle, Amazon | 同上 | Techstrong [S35] | 3 |
| 各社の耐用年数(Burry のグラフの解説) | Microsoft は2025年までに6年へ延長。Amazon は逆に一部サーバーを5年に短縮(2025年) | 2025-11 | [S35] | 3 |
| 各社の耐用年数(Yardeni) | Amazon は4年前後、Meta は11〜12年と極端に長い、Microsoft・Google・Oracle は4〜5年 | 2025〜2026 | Yardeni Research [S37] | 3 |
| 食い違い | Microsoft は上で6年、Yardeni で4〜5年。Meta の「11〜12年」は設備区分が不明で、サーバーの値かは確認できない。10-K の原文での確認が必要 | — | — | — |
| 反論 | Motley Fool は「長めの償却だが不正とまでは言えない」。別の論者は「AI チップの使われ方は一様に短命ではない」と主張 | 2025-12 | [S38][S39] | 4 |
| Oracle の耐用年数 | 今回は未取得(10-K 未確認) | — | — | — |
| CoreWeave の耐用年数 | 今回は未取得 | — | — | — |

**事実要約(2節)**
- The Information は、Oracle の NVIDIA サーバー レンタルの粗利率を14%(2025年6〜8月、売上約 $9 億、粗利益約 $1.25 億)と報じ、減価償却を全額反映するとさらに約7ポイント下がると伝えた。
- 会社側は2025年10月に、6年・$600 億の契約例で通算35%の粗利率を示し、その後も30〜40%のレンジを維持している(2026年3月・6月)。この数字は契約期間全体の見込みで、四半期実績ではない。
- 2026年に H100 などの旧世代の単価が上昇している(1節)ことは、長めの耐用年数を支持する材料と、Burry 型の批判の双方に使われうるが、今回の調査ではその議論を直接扱った記事は確認できていない。
- 各社の耐用年数は情報源ごとに数値が食い違い、10-K での確認が必要。

---

## 3. データセンターと電力(制約の解放時期)

### 3-1. 拠点別一覧

| 拠点 | 所在 | 開発・資金パートナー | 計画容量 | 稼働(予定) | 遅延・問題報道 | 出典 | Tier |
|---|---|---|---|---|---|---|---|
| Abilene | テキサス州 | Crusoe(開発)。拡張分で Nvidia が Crusoe に $1.5 億の手付金(Bloomberg 報道) | 1.2GW(キャンパス全体)。最初の2棟で 200MW 超の IT 負荷 | 最初の2棟は稼働(Oracle の2026年3月の声明)。残り6棟は「2026年中頃」完成予定とされていた。最終棟は2029年末までかかる可能性との報道も | 2026年3月、Oracle と OpenAI が約600MW の拡張計画を取りやめたと報道(資金協議の決裂、OpenAI の容量見通し変更とされる)。Oracle は「事実と異なる」と反論し、拡張は最終合意に至っていないリースだったとの説明もある。Oracle は OpenAI 向けに追加 4.5GW のリース手配は完了済みで計画通りと主張 | [S40][S41][S42] | 3 |
| Shackelford County(Frontier) | テキサス州 | Vantage Data Centers。VoltaGrid の敷地内ガスマイクログリッド(系統接続なし) | IT 負荷 1.4GW(10棟、約370万平方フィート)。総電力容量は 2.58GW(Cleanview)。投資額は $250 億超 | 1棟目は2026年後半。全体は Epoch AI が2028年4Q(容量2GWと記載)、Baxtel は2029年 | 2026年10月8日の Bloomberg 報道で、Oracle が天然ガスをトラックで運び、パイプライン遅延に備えている先の1つとして挙がる | [S43][S44][S45][S46][S47] | 3 |
| Milam County | テキサス州 | SB Energy(SoftBank 子会社)が建設・運営。SoftBank と OpenAI が各 $5 億を SB Energy に出資 | 1.2GW | 第1期は 548,950 平方フィート・4データホール・推定費用 $4.7 億・完了期日は「10月15日」(テキサス州の届出、年は要確認)。Epoch AI は2028年4Qを予測、現時点の稼働容量は 0GW | 今回の調査では個別の遅延報道は未確認。OpenAI の2025年9月発表では SoftBank 側のサイトで、Oracle の直接のリース関与は今回の要約からは確認できない | [S48][S49][S45] | 3 |
| Doña Ana County(Project Jupiter) | ニューメキシコ州 Santa Teresa | BorderPlex Digital Assets と STACK Infrastructure(開発)。Oracle が18年リースのテナント。OpenAI が主要顧客。ローン約 $180 億(銀行団)。報道によっては Blue Owl 傘下がキャンパスの開発主体とされる | 約 2.45GW とする報道あり。Bloom Energy の燃料電池が最大 2.5GW。郡の産業収益債は最大 $1,650 億(30年)、最初の5年で $500 億の投資 | 当初は2026年4Q(または年末)に初期稼働と報じられた。現在は2028年開業が目標で、2028年を超えるリスクが報じられている | ・2026年9月: Oracle が開発者に不可抗力(force majeure)通知を送付。2028年に開業しない場合に家賃の支払い繰延(最大3年とする報道)を可能にする目的とされる。Oracle は「通知だけで遅延が確定するわけではない」、Blue Owl は「財政コミットメントに変更はない」とコメント<br>・ガスパイプライン(Green Chile、最大4億立方フィート/日)の稼働予定が2026年8月15日から2027年2月1日に延期(Energy Transfer 傘下 Transwestern の FERC への提出書類)。ニューメキシコ州土地局がルートを承認せず<br>・約 $180 億のローンが額面の89〜91%で取引(FT 報道を Reuters 等が転載)。S&P の格下げ(7月)も背景<br>・「事業は事実上停止(mothballed)」とする報道が1社のみあるが、他の報道では確認できず<br>・住民団体が債券・税控除の承認で郡を提訴 | [S50][S51][S52][S53][S54][S55][S56][S57][S58] | 3(原典: FERC 提出書類は Tier 2) |
| Lordstown | オハイオ州 | SoftBank(旧 Foxconn 工場を $3.75 億で購入。Foxconn が運営を継続する JV) | 容量の数値は今回未取得 | OpenAI の2025年9月23日の発表では「来年(2026年)稼働予定」 | 2026年の進捗報道は今回の検索では見つからず | [S59][S60] | 3 |
| Saline Township | ミシガン州 | Related Digital(開発)。DTE Energy が電力の100%を供給し、蓄電池を併設 | 「1GW 超」。1.4GW の記載は確認できなかった。敷地約250エーカー・3棟 | 具体的な稼働予定は今回未取得。Related の会長は「大規模な建設が進行中」と述べた | ・2025年12月: Blue Owl が約 $100 億案件への出資協議で条件が合わず離脱(Reuters)。Oracle は「Blue Owl を含まない形で協議は予定通り」と説明<br>・資金調達総額 $160 億(Related の株式と Blackstone 関連資金を含む)、Bank of America が $140 億の債券を販売し Pimco が $100 億を取得(DCD、Bloomberg 引用、日付は要確認) | [S61][S62][S63][S64] | 3 |
| Port Washington(Lighthouse) | ウィスコンシン州 | Vantage Data Centers | 約1GW(別報で 1.3GW)。4棟。総投資 $150 億超、第1期 $80 億 | 建設完了は2028年とする報道(2026年の進捗更新は見つからず) | 近隣住民が騒音・粉じんを苦情。2026年10月2日、Oracle が Point Beach の電力コスト上昇分 $3 億を地元住民の負担としないと表明(検索結果の要約、個別URLは特定できず) | [S65][S66][S67] | 3 |
| Salt Lake City 近郊 | ユタ州 | (不明) | (不明) | 稼働中 | Bloomberg: トラックで運ぶガスで1年超稼働を継続(パイプライン未完成のため) | [S46][S47] | 3 |

### 3-2. Oracle 全体の容量に関する開示・報道

| 項目 | 内容 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| OpenAI 向け追加リース | Oracle は OpenAI へのコミットを支えるため、追加 4.5GW 分のリース手配を完了したと主張 | 2026年3月(反論声明) | Tom's Hardware [S41] | 3 |
| 「一部の OpenAI 向け DC を2027年から2028年に延期」 | Bloomberg 報道。主因は労働力・資材の不足。Oracle 広報(Michael Egbert)は Reuters に対し「契約上の義務を満たすために必要なサイトに遅延はない」と説明。対象サイトは非公表 | 日付は検索結果に明記なし | DCD [S68]、Capital Brief [S69] | 3 |
| Stargate 全体の調整 | SoftBank と OpenAI の間で拠点・SB Energy の使用をめぐる対立(WSJ)。The Information は2026年2月時点で Stargate 合弁事業の開発は未着手と報道 | 2026年2月 | Gigazine [S70]、TipRanks [S71] | 3 |
| Oracle の総契約容量・稼働容量(GW) | 今回の調査では会社全体の開示値を取得できず | — | — | — |

**事実要約(3節)**
- 稼働が確認できるのは Abilene の最初の2棟(200MW 超)と、一部のトラックガス運用拠点のみ。ほかの拠点は「建設中」または「2026年後半以降の稼働予定」で、Epoch AI は Shackelford と Milam の完成を2028年4Qと見ている。
- 電力が最大の制約として報じられている。Shackelford は系統接続なしでガスマイクログリッド、Project Jupiter はガスパイプラインが2027年2月に延期(従来は2026年8月)、Oracle はトラック輸送のガスで凌ぐ方針を取っている。
- Project Jupiter では Oracle が不可抗力通知を出し、約 $180 億のローンが額面を割って取引されている。Oracle と開発者側は事業継続を主張している。
- Abilene の約600MW 拡張の中止、一部拠点の2027→2028年延期の報道に対し、Oracle は「契約上必要なサイトに遅延はない」「追加 4.5GW のリースは手配済み」と反論している。Oracle 全体の稼働 GW の開示値は今回未取得。

---

## 4. 上位顧客の支払能力

### 4-1. OpenAI

| 項目 | 数値 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| 年換算売上(run rate) | 2025年は200億ドル超(OpenAI 発言として報道)。2026年2月末に250億ドル超(2024年の37億ドルから) | 2026-02末 | The Information を techloy 等が引用 [S72] | 3 |
| 同 | 約 $400 億超 | 2026-08-13 | Bloomberg を letsdatascience が引用 [S73] | 3〜4 |
| 同 | 「約 $680 億〜700 億に迫る」(7月初から+70%超。企業向け売上が7月以降倍増) | 2026-09-29 | Axios / Reuters を roic.ai 等が引用 [S74] | 3 |
| 同(修正) | OpenAI が投資家に「約 $500 億」と説明。$680 億の数字は提携先経由の総売上を含むものだった(関係者の説明) | 2026-10-08 | FT が最初に報道、CNBC が引用 [S75][S76] | 3 |
| 市場反応 | 2026-10-08 に NVIDIA 約 -3%、Oracle 約 -5〜6%(終値約 $135.69 とする報道)、CoreWeave 約 -8% | 2026-10-08 | CNBC 等 [S75][S77] | 3 |
| 2026年の売上見通し | 約 $360 億(2030年 $3,500 億、累計 $8,400 億) | 2026-09-19 | FT を Reuters が要約(The Star が転載)[S78] | 3 |
| フリーキャッシュフロー見通し | 2026〜2030年累計で約 -$2,780 億(2026年5月時点は -$3,050 億) | 2026-09-19 | 同上、runtimewire [S78][S79] | 3 |
| コンピュート支出 | 2030年末までに約 $8,560 億(FT の社内資料報道) | 2026-09-19 | [S78][S79] | 3 |
| コンピュート支出(旧報道) | 2030年までに約 $6,000 億に下方修正(従来の約 $1.4 兆から)、2030年売上 $2,800 億見通し | 2026-02 | CNBC を finviz が転載 [S80] | 3(上と数値が異なる。時点の違い) |
| 資金調達 | $1,220 億、評価額 $8,520 億(ポスト)、2026-03-31 クローズ。当初コミット $1,100 億・プレ $7,300 億。Amazon $500 億、NVIDIA、SoftBank が参加とされる(投資家別の金額は OpenAI 側の発表では未開示とする記事もある) | 2026-03 | tech-insider [S81]、bitcoin.com [S82] | 4 |
| 資金の持続性 | FT: 調達資金は2028年までに枯渇する見込み。投資家と評価額約 $1.2 兆での協議 | 2026-09 | [S78][S79] | 3 |
| 損失・キャッシュバーン(2026年) | 約 $270 億とする記事あり | 2026年 | tech-insider [S81] | 4 |
| IPO | 2026-06-08 に S-1 を秘密裏に提出とする記事あり(他で裏付けなし)。別の記事は「Altman は2026年中に上場しない」と言及。Oracle 株が「OpenAI の IPO 延期で1週間に9%下落」とする報道が1件 | 2026年 | tech-insider [S81]、Invezz 等 [S83] | 4 |
| Oracle との契約 | 5年・$3,000 億(2027年開始)。Oracle の RPO の約45〜47%を占めると推計(Oracle は金額を確認していない) | 2025-09〜2026-10 | DCD [S84]、FX Leaders [S77]、Invezz [S83] | 3 |
| 契約の縮小・延期の報道 | Oracle 契約そのものの縮小・減額を報じた記事は今回の検索では見つからなかった。関連する報道は、(a)Abilene 約600MW 拡張の中止(2026年3月)、(b)一部 DC の2027→2028年延期(Bloomberg)、(c)Project Jupiter の不可抗力通知(2026年9月)、(d)OpenAI と SoftBank の対立(2026年2月) | — | 3節の出典 | 3 |
| 他社との契約総額(Microsoft, AWS, CoreWeave, Broadcom, AMD, NVIDIA 等) | 今回未取得 | — | — | — |

### 4-2. Meta・xAI・その他

| 項目 | 内容 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| Meta | 約 $200 億の複数年クラウド契約の協議(Llama の学習・運用向け)。金額は増える可能性があるとされた。今回の検索では「署名済み」の確認は取れず | 2025年 | DCD [S85]、TipRanks | 3 |
| Meta と Crusoe | Nvidia が Crusoe に $1.5 億の手付金を支払ったと報道されたが、Meta と Crusoe の合意は未確認 | 2026年3月前後 | [S41][S42] | 3 |
| xAI | Oracle は過去の開示で、Meta や xAI などの AI モデル開発企業との取引に言及。契約条件は取得できず | — | [S85] | 3 |
| その他の大口顧客 | 今回未取得 | — | — | — |

### 4-3. 参考: Oracle 自身の資金調達(顧客の支払能力と対になる制約)

| 項目 | 数値 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| Oracle Q1 FY2027 | RPO $6,640 億(前年比 +$2,090 億)。Q1 に $300 億超の AI クラウド契約を追加し、「資金調達計画への追加の影響なし」と説明。OCI 売上 $74 億(+121%)。総売上 $193 億(+30%)。クラウド合計 $116 億(+62%)。FCF は -$50 億。FY2027 の売上は $900 億以上の見込み | 2026-09-10 | Oracle IR(検索要約)[S86] | 1(要約経由) |
| FY2026 期末 RPO | $6,380 億(前年比 +363%、前四半期比 +$850 億) | 2026-05〜06 | Invezz [S83] | 3 |
| FY2026 の capex と FCF | capex 約 $557 億、FCF 約 -$240 億 | FY2026 | S&P 関連報道 [S87][S88] | 3 |
| FY2027 の capex | 報道により「$900 億〜950 億」または「純現金支出 約 $700 億」と食い違い | FY2027 見通し | [S87][S88] | 3 |
| S&P 格付け | BBB に BBB- へ(ジャンク水準の1段上)、短期格付けも A-3 に引き下げ、見通し安定。Moody's は見通しネガティブ | 2026-07-09 | TNW 等 [S87][S88][S89] | 3 |
| 資金調達計画 | 2026年に最大 $500 億(株式と社債でほぼ半々)。S&P は2026年2月発行の $50 億の強制転換優先株と $200 億の株式発行を一部の相殺要因として評価 | 2026年 | DCD [S90]、[S88] | 3 |
| 10年債利回り | 約6.5% | 2026-07 | [S88] | 3 |
| 負債総額 | $1,080 億〜1,300 億、または $1,670 億など、情報源で食い違い | 2026年 | [S88] | 3 |

**事実要約(4節)**
- OpenAI の年換算売上は、2026年2月末の約 $250 億から、9月末に $500 億(FT・OpenAI が投資家に説明)へ拡大した。9月29日に出回った $680 億〜700 億は提携先の総売上を含む数字で、10月8日の訂正報道で Oracle、NVIDIA、CoreWeave の株価が下落した。
- OpenAI の 2026〜2030年の累計 FCF は約 -$2,780 億、コンピュート支出は約 $8,560 億、調達済みの $1,220 億は2028年までに尽きる見込みと FT が伝えた。さらに評価額 $1.2 兆での資金調達協議があるとされる。
- Oracle の RPO $6,640 億の約45〜47%が OpenAI の約 $3,000 億とする推計がある(Oracle は金額を確認していない)。Oracle 契約そのものの縮小報道は今回の検索では確認できなかった。
- Meta と xAI の契約規模は、Meta の約 $200 億の協議報道(2025年)以外は今回未取得。

---

## 5. 競合の同じ KPI

### 5-1. ハイパースケーラー(2026年4〜6月期)

| 事業 | 売上・成長率 | 受注残 | 2026年 capex | 出典 | Tier |
|---|---|---|---|---|---|
| AWS | $422 億、前年比 +36.7%(約37%)。18四半期ぶりの高成長。営業利益 $166 億(営業利益率 約39%) | $4,960 億 | Amazon 全体の2026年の現金 capex 見通しを約 $2,200 億に引き上げ(従来 $2,000 億、メモリ価格上昇が理由)。直近12か月の FCF は約 -$76 億 | UpperEdge [S91]、4WeekMBA [S92]、Tom Tunguz [S93] | 3 |
| Azure(Microsoft FY4Q、〜6月30日) | Azure 等 +43%(定率換算)、前四半期は40% | 商業 RPO $6,780 億 | 四半期約 $410 億。暦年2026は約 $1,750 億の見通しを維持。FY2027 は $2,550 億〜2,600 億 | [S91][S92] | 3 |
| Google Cloud | 約 $248 億、前年比 +82%。営業利益 $88 億(営業利益率 約35.6%) | $5,140 億(前四半期比 +$500 億超) | 四半期 $449 億。2026年通年を $1,950 億〜2,050 億に引き上げ(従来 $1,800 億〜1,900 億)。2Q の FCF は -$59 億(上場以来初のマイナスとされる) | Crypto Briefing [S94]、tech-insider [S95]、[S91] | 3 |
| 備考 | 受注残の定義は各社で異なり、直接比較はできない。AWS の四半期 capex は $542 億とする二次情報があるが未確認 | | | | |
| Oracle(参考) | OCI 売上 $74 億(+121%)、RPO $6,640 億(2026-09-10) | | FY2027 capex は 4-3 参照 | [S86] | 1 |

### 5-2. ネオクラウド

| 事業 | 内容 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| CoreWeave | 2026年7月に約25%値上げ、6月30日以降も高い価格で新規契約(1節)。受注残・2026年 capex・顧客集中度は今回未取得 | 2026-07〜09 | [S22][S24] | 3〜4 |
| Nebius | 受注残・契約単価・capex とも今回未取得 | — | — | — |

**事実要約(5節)**
- 2026年4〜6月期は、Google Cloud が +82%、Azure が +43%(定率換算)、AWS が +37% で、いずれも成長が加速している。受注残は AWS $4,960 億、Azure(商業 RPO)$6,780 億、Google $5,140 億で、Oracle の RPO $6,640 億(OCI 売上は四半期 $74 億)はこれらと同規模。ただし定義は各社で異なる。
- 3社とも2026年の capex を引き上げており(AWS 約 $2,200 億、Google $1,950 億〜2,050 億、Microsoft 暦年約 $1,750 億)、AWS と Google は FCF が直近でマイナスに転じたと報じられている。
- CoreWeave と Nebius の受注残・顧客集中度は今回の調査で取得できていない(8節)。

---

## 6. その他の一次情報

今回は調査できていない項目が大半。得られたものだけを記す。

| 項目 | 内容 | 日付 | 出典 | Tier |
|---|---|---|---|---|
| 電力コストの住民転嫁回避 | Oracle が Wisconsin の Point Beach の電力コスト上昇分 $3 億を負担すると表明(Stargate サイト関連、Vantage・OpenAI と) | 2026-10-02 | 検索結果の要約(個別URL未特定)[S46] | 3 |
| ガスのトラック輸送 | Oracle がパイプライン完成前の DC にトラックで天然ガスを供給(Salt Lake City 近郊で1年超、Shackelford でも)。Project Jupiter でも検討中 | 2026-10-08 | Bloomberg ほか [S46][S47] | 3 |
| Oracle 求人動向(OCI・DC 建設) | 未調査 | — | — | — |
| OCI 価格表の改定 | 未調査 | — | — | — |
| Oracle Database のライセンス・サポート料の値上げ | 未調査 | — | — | — |
| マルチクラウド DB の顧客事例・導入数 | 未調査(Q1 FY2027 のプレスリリース要約には数値なし) | — | — | — |
| 従業員削減報道(2025〜2026年) | 未調査 | — | — | — |

**事実要約(6節)**
- 求人、価格表・ライセンス値上げ、マルチクラウド DB、人員削減の各項目は、検索回数の上限に到達したため調べられていない。
- 得られた2点はいずれも電力に関する一次情報に近い話で、パイプライン待ちの代替策(トラック輸送ガス)と、電力コストの住民転嫁を避ける表明。
- 後続の担当者は、6節の5項目を新規に調べる必要がある。

---

## 7. 出典一覧(URL は検索結果に表示されたもの)

GPU 価格
- [S1] Silicon Data: H100 rental price over time / 指数ページ — https://www.silicondata.com/blog/h100-rental-price-over-time , https://www.silicondata.com/products/silicon-index/h100
- [S2] Introl: GPU Cloud Prices Collapse (2025-12) — https://introl.com/blog/gpu-cloud-price-collapse-h100-market-december-2025
- [S3] Silicon Data H100 指数に関する二次記事・検索要約(2026-08-02 の値を含む)— https://akash.network/the-bid/h100-rental-price-2026-cost-per-hour/ , https://www.silicondata.com/products/silicon-index/h100
- [S4] Silicon Data: H200 vs H100 rental prices (May–July 2026) — https://www.silicondata.com/blog/h200-vs-h100-rental-prices-may-july-2026
- [S5] Silicon Data 指数 — https://www.silicondata.com/products/silicon-index?gpu=h100
- [S6] 科技新報 (2026-08-04) — https://finance.technews.tw/2026/08/04/nvidia-a100-h100-and-h200-gpu-rental-rates-continue-to-price-upwards/
- [S7] Silicon Data H200 指数 — https://www.silicondata.com/products/silicon-index/h200
- [S8] Silicon Data: B200 rental price August 2026 update — https://www.silicondata.com/blog/b200-rental-price-august-2026-update
- [S9] StockHub (2026-09-06) — https://stockhub.kr/en/news/news_f85b3c67b516
- [S10] SemiAnalysis: The Great GPU Shortage / H100 1 Year Rental Price Index — https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity
- [S11] iTiger(SemiAnalysis の要約)— https://www.itiger.com/news/1185188896
- [S12] Tom Tunguz: B200 GPU pricing — https://tomtunguz.com/b200-gpu-pricing-spot-market-model-releases/
- [S13] Ornn 指数の Bloomberg 掲載 — https://www.miningstockeducation.com/2026/04/ornn-compute-price-index-added-to-bloomberg-terminal/
- [S14] ICE と Ornn の GPU 先物 — https://finance.yahoo.com/markets/options/articles/ice-ornn-launch-gpu-compute-142609556.html ; https://theinnermostloop.substack.com/p/the-first-tradable-compute-price ; https://aiweekly.co/alerts/ornn-raises-33m-led-by-a16z-to-build-gpu-compute-futures-market
- [S15] UOB: Compute is Revenue (2026-06) — https://www.uob.com.sg/assets/web-resources/private/pdfs/compute-is-revenue.pdf
- [S16] Akash: H100 rental price 2026 — https://akash.network/the-bid/h100-rental-price-2026-cost-per-hour/
- [S17] Spendark: Cloud GPU price war 2026 — https://spendark.com/blog/cloud-gpu-price-war-2026/
- [S18] SMM Computing Power Daily — https://news.metal.com/en/newscontent/104021324-smm-computing-power-daily-h100-spot-rental-quotes-hit-a-new-high-of-85000-h20-and-a800-long-term-agreement-resources-ent
- [S19] computeprices.com GB200 — https://computeprices.com/providers/gmi-cloud/gpus/gb200
- [S20] deploybase.ai GB200 NVL72 — https://deploybase.ai/articles/nvidia-gb200-nvl72-cloud-pricing-where-to-rent-and-how
- [S21] Cyfuture: Rent NVIDIA B300 — https://cyfuture.cloud/blog/rent-nvidia-b300-gpu-the-complete-2026-guide-to-pricing-performance-and-provider-selection/
- [S22] Spheron: CoreWeave price increase 2026 — https://www.spheron.network/blog/coreweave-price-increase-2026-h100-h200-25-percent/
- [S23] Insider Monkey: CoreWeave raises prices twice — https://www.insidermonkey.com/news/coreweave-can-raise-prices-twice-in-three-months-can-it-afford-to-keep-building-1850325/
- [S24] CoreWeave IR (2026-09-17) — https://investors.coreweave.com/news/news-details/2026/CoreWeave-Continues-to-Contract-New-Compute-Capacity-at-Higher-Prices/default.aspx (本文は取得失敗、検索要約のみ)
- [S25] Servnet UK — https://www.servnetuk.com/insights/used-hopper-h100-h200-buy-second-hand-2026
- [S26] GPUnex — https://www.gpunex.com/blog/buying-selling-gpus-2026

OCI 採算・耐用年数
- [S27] Paul Kedrosky(The Information 報道の解説)— https://paulkedrosky.com/the-godfather-and-oracles-crap-gpu-rental-returns/
- [S28] 各紙の転載(Sherbrooke Record ほか)— https://business.sherbrookerecord.com/sherbrookerecord/article/marketminute-2025-10-7-oracles-ai-cloud-margins-squeezed-by-nvidia-chips-sparking-investor-jitters
- [S29] The Information 原題(Oracle assures investors on AI cloud margins)— https://feature.theinformation.com/articles/oracle-assures-investors-ai-cloud-margins-struggles-profit-older-nvidia-chips (有料、スラッグのみ確認)
- [S30] Sherwood — https://sherwood.news/markets/oracle-tumbles-after-report-that-its-lost-nearly-usd100-million-from-renting
- [S31] TradingView — https://tr.tradingview.com/news/tradingview:bac804d10094b:0-orcl-oracle-stock-sheds-2-5-after-internal-data-shows-ai-rentals-are-churning-out-losses
- [S32] iTiger: Oracle 35% gross margin — https://www.itiger.com/news/1108942484
- [S33] Finviz(Magouyrk の発言)— https://finviz.com/news/336098/oracle-co-ceo-clay-magouyrk-explains-whats-holding-back-the-companys-data-center-windfall-the-major-factor-limiting-even-stronger-profits-is
- [S34] Saxo — https://www.home.saxo/content/articles/equities/big-short-12112025
- [S35] Techstrong — https://techstrong.ai/features/tech-investor-michael-burry-alleges-accounting-irregularities-at-hyperscalers-in-pursuit-of-ai-boom/
- [S36] TipRanks — https://www.tipranks.com/news/michael-burry-sounds-alarm-on-176b-depreciation-gap-among-tech-giants
- [S37] Yardeni Research — https://www.yardeniquicktakes.com/deep-dive-the-debate-about-the-quality-of-ai-earnings/
- [S38] Motley Fool (2025-12-02) — https://www.fool.com/investing/2025/12/02/michael-burry-just-sent-a-warning-to-artificial-in
- [S39] DSHR(2026-02)— https://blog.dshr.org/2026/02/mind-gaap-again.html

データセンター
- [S40] DCD: Crusoe's Abilene data center officially live — https://www.datacenterdynamics.com/en/news/crusoes-abilene-data-center-officially-live-serving-oracle-and-openais-stargate/
- [S41] Tom's Hardware: Oracle rebuts incorrect reporting — https://tomshardware.com/tech-industry/oracle-rebuts-incorrect-reporting-on-stargate-expansion
- [S42] Tom's Hardware: Oracle and OpenAI scrap planned 600MW Abilene expansion — https://www.tomshardware.com/tech-industry/oracle-and-openai-scrap-planned-600mw-abilene-expansion
- [S43] DCD: Vantage breaks ground (Shackelford) — https://www.datacenterdynamics.com/en/news/vantage-breaks-ground-on-texas-gigawatt-data-center-campus-for-openai/
- [S44] Cleanview: Stargate Frontier — https://cleanview.co/reports/behind-the-meter-data-centers/full-report/stargate-frontier
- [S45] Epoch AI: OpenAI Stargate where the US sites stand — https://epoch.ai/blog/openai-stargate-where-the-us-sites-stand
- [S46] Bloomberg(2026-10-08)— https://www.bloomberg.com/news/articles/2026-10-08/oracle-moves-gas-by-trucks-to-avoid-data-center-power-delays
- [S47] InvestingLive — https://investinglive.com/news/oracle-trucks-in-natural-gas-to-keep-ai-data-centres-on-schedule-as-pipelines-lag ; TNW https://thenextweb.com/news/oracle-trucked-gas-data-centres-europe
- [S48] DCD: SB Energy Milam County — https://www.datacenterdynamics.com/en/news/softbanks-sb-energy-to-build-and-operate-openais-12gw-stargate-data-center-in-milam-county-texas/
- [S49] DCD: Milam Freebird first phase — https://www.datacenterdynamics.com/en/news/openai-stargates-milam-texas-freebird-data-center-to-span-548950-sq-ft-in-first-phase/
- [S50] Cleanview: Stargate Jupiter — https://cleanview.co/reports/behind-the-meter-data-centers/full-report/stargate-jupiter
- [S51] El Paso Matters(2026-09-24)— https://elpasomatters.org/2026/09/24/project-jupiter-rent-force-majeure-new-mexico-oracle-ai-el-paso-data-center/ (本文取得失敗、二次引用)
- [S52] TNW: Oracle force majeure — https://thenextweb.com/news/oracle-force-majeure-project-jupiter-new-mexico
- [S53] Bloomberg Government — https://news.bgov.com/artificial-intelligence/oracle-cites-force-majeure-to-shield-itself-on-big-data-center
- [S54] roic.ai(2026-09-24)— https://www.roic.ai/news/oracle-invokes-force-majeure-on-project-jupiter-as-ai-data-center-financing-stumbles-09-24-2026
- [S55] Source NM(2026-08-17、Transwestern の FERC 提出書類)— https://sourcenm.com/2026/08/17/proposed-gas-pipeline-for-project-jupiter-data-center-delayed-to-2027-filings-show/
- [S56] TNW: Green Chile pipeline delay — https://thenextweb.com/news/oracle-project-jupiter-green-chile-pipeline-delay
- [S57] KuCoin News(FT 報道の転載)— https://www.kucoin.com/news/flash/oracle-s-18b-ai-project-loan-trades-at-89-91-cents-on-the-dollar-amid-delays
- [S58] Crypto Briefing(mothballed)— https://cryptobriefing.com/oracle-project-jupiter-data-center-mothballed/
- [S59] OpenAI: Five new Stargate sites(2025-09-23)— https://openai.com/index/five-new-stargate-sites/
- [S60] Outlook Business(Foxconn・SoftBank の Ohio)— https://www.outlookbusiness.com/technology/foxconn-to-run-softbanks-ohio-site-paving-way-for-first-stargate-ai-manufacturing-hub
- [S61] DCD: Related Digital Michigan — https://www.datacenterdynamics.com/en/news/related-digitals-michigan-1gw-data-center-project-to-serve-openai-oracle/
- [S62] Baxtel: Blue Owl backs out — https://baxtel.com/news/blue-owl-backs-out-of-funding-oracle-s-10bn-michigan-facility
- [S63] Yahoo Finance(Reuters)— https://finance.yahoo.com/news/oracles-10-billion-michigan-data-132428847.html
- [S64] Verdict — https://www.verdict.co.uk/openai-oracle-related-digital-data-centre-michigan/
- [S65] Fox 11(Port Washington)— https://fox11online.com/news/business/port-washington-data-center-project-lighthouse-construction-open-house-neighbor-concerns-companies-representatives-vantage-oracle-openai
- [S66] Verdict(Vantage)— https://www.verdict.co.uk/openai-oracle-vantage-data-centre/
- [S67] ENR(2025-11-24)— https://digital.bnpmedia.com/article/PROJECT+DELIVERY/5074278/857075/article.html
- [S68] DCD: Oracle delays some OpenAI data centers 2027 to 2028 — https://www.datacenterdynamics.com/en/news/oracle-delays-some-of-its-openai-data-centers-from-2027-to-2028-report/
- [S69] Capital Brief — https://www.capitalbrief.com/briefing/oracle-pushes-back-some-openai-data-centre-projects-to-2028-bloomberg-cfd7a02c-64b4-48f4-94da-a9ab04376b9c/
- [S70] Gigazine(2026-02-24)— https://www.gigazine.net/gsc_news/en/20260224-stargate-delay
- [S71] TipRanks: OpenAI SoftBank pull back — https://www.tipranks.com/news/openai-softbank-pull-back-on-500b-stargate-project

顧客
- [S72] Techloy(OpenAI $25B)— https://www.techloy.com/openai-hits-25-billion-in-annualized-revenue-while-anthropic-surges-to-19-billion/
- [S73] Letsdatascience($40B)— https://letsdatascience.com/news/openai-revenue-run-rate-tops-40-billion-c7999365
- [S74] roic.ai($70B)— https://www.roic.ai/news/openai-annualized-revenue-run-rate-surges-past-70-in-q3-nears-70-billion-source-09-29-2026
- [S75] CNBC(2026-10-08)— https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html
- [S76] mlq.ai — https://mlq.ai/news/openai-tells-investors-its-annualized-revenue-is-nearing-50-billion/
- [S77] FX Leaders(2026-10-09/10)— https://www.fxleaders.com/news/2026/10/10/oracle-bearish-forecast-orcl-sinks-after-openai-clarifies-50-billion-revenue-run-rate/
- [S78] The Star(Reuters/FT、2026-09-19)— https://www.thestar.com.my/tech/tech-news/2026/09/19/openai-forecasts-cash-burn-near-280-billion-by-2030-ft-reports
- [S79] Runtimewire — https://runtimewire.com/article/openai-278b-cash-burn-1-2t-valuation
- [S80] Finviz(CNBC 転載、$6,000 億)— https://finviz.com/news/317824/openai-tempers-compute-spending-target-to-600-billion-projects-280-billion-revenue-by-2030-as-mega-funding-round-nears-report
- [S81] tech-insider — https://tech-insider.org/openai-122-billion-funding-round-852-billion-valuation-2026
- [S82] Bitcoin.com — https://news.bitcoin.com/chatgpt-maker-openai-valued-at-852b-after-record-122b-funding-round/?rand=52384
- [S83] Invezz(2026-07-08)— https://invezz.com/news/2026/07/08/oracles-record-backlog-is-booming-so-why-is-the-stock-down-50/
- [S84] DCD: OpenAI signs $300bn cloud deal with Oracle — https://www.datacenterdynamics.com/en/news/openai-signs-300bn-cloud-deal-with-oracle-report/
- [S85] DCD: Meta in talks $20bn Oracle — https://www.datacenterdynamics.com/en/news/meta-in-talks-to-sign-20bn-oracle-cloud-deal-report/
- [S86] Oracle IR: Q1 FY2027 プレスリリース(2026-09-10)— https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/ (本文取得失敗、検索要約に引用された原文を使用)
- [S87] TNW: S&P downgrade — https://thenextweb.com/news/oracle-sp-downgrade-ai-spending-junk-risk
- [S88] ppc.land: S&P cuts Oracle — https://ppc.land/s-p-cuts-oracle-to-bbb-as-ai-buildout-widens-cash-deficit-to-42bn/
- [S89] Computing.co.uk — https://www.computing.co.uk/news/2026/ai/oracle-under-pressure-after-ratings-downgrade-over-ai-expansion
- [S90] DCD: Oracle to raise up to $50bn — https://www.datacenterdynamics.com/en/news/oracle-to-raise-up-to-50bn-in-debt-and-equity-in-2026/

競合
- [S91] UpperEdge(Q2 2026 クラウド決算)— https://upperedge.com/cloud/aws-hits-37-growth-azure-tops-100b-gcp-launches-flexible-savings-plan-what-q2-2026-earnings-mean-for-enterprise-cloud-contracts/
- [S92] 4WeekMBA — https://fourweekmba.com/ai-google-cloud-aws-azure-q2-2026-ai-infrastructure/
- [S93] Tom Tunguz: AWS — https://tomtunguz.com/aws-answers-the-cloud-race/
- [S94] Crypto Briefing: Alphabet cloud backlog — https://cryptobriefing.com/alphabet-cloud-backlog-514b-revenue-growth/
- [S95] tech-insider: Google Cloud 82% — https://tech-insider.org/google-cloud-82-percent-growth-aws-earnings-2026/

---

## 8. 未確認事項・出典間の食い違い

### 8-1. 未調査(検索上限到達または取得不能)
1. 6節の全項目: Oracle の求人動向(OCI・DC 建設)、OCI 価格表の改定、Oracle Database のライセンス・サポート料の値上げ、マルチクラウド DB(Oracle Database@Azure/AWS/Google)の顧客事例・導入数、2025〜2026年の従業員削減報道。
2. 5節: CoreWeave の受注残・2026年 capex・顧客集中度(Microsoft・OpenAI・Meta の比率)、Nebius の受注残・契約単価・顧客集中度・capex、および両社の最新四半期の公表値。
3. 2節: Oracle・Microsoft・Alphabet・Meta・Amazon・CoreWeave の 10-K に記載のサーバー耐用年数。Oracle 自身の耐用年数・減価償却方針の変更有無。
4. 3節: Oracle の会社全体の契約容量・稼働容量(GW)の会社開示値。Lordstown の容量と稼働状況。Milam County で Oracle が直接リースしているかどうか。Saline Township の稼働予定。Port Washington の2026年進捗。
5. 4節: OpenAI の他社向けコンピュート契約の個別金額(Microsoft、AWS、CoreWeave、Broadcom、AMD、NVIDIA)。Meta の Oracle 契約が署名されたかどうか。xAI の Oracle 契約規模。その他の大口顧客。
6. 1節: OCI 自身の GPU 時間単価(価格表・契約単価)。GB300 の信頼できる時間単価。Ornn の H100 の直近値。

### 8-2. 出典間の食い違い(どちらかを採らずに併記)
1. OpenAI の年換算売上: 約 $680 億〜700 億(Axios/Reuters、2026-09-29)と約 $500 億(FT、OpenAI が投資家に説明、2026-10-08)。後者は前者が提携先の総売上を含むと説明している。
2. OpenAI のコンピュート支出: 2030年まで約 $6,000 億(CNBC、2026-02)と、2030年末までに約 $8,560 億(FT、2026-09)。時点・定義の違いの可能性があるが、検索結果からは確認できない。
3. Oracle の AI 粗利率: 14%(四半期実績、The Information)と、通算35%・30〜40%(会社側の見込み)。測る対象が異なる。Sherwood の「約 $1 億の損失」と、14%(粗利益プラス)の整合は未確認。
4. Project Jupiter の容量: 約 2.45GW(Bloomberg 系の報道)と、燃料電池最大 2.5GW(Bloom Energy)。開発主体: BorderPlex/STACK とする記事と、Blue Owl 傘下とする記事がある。稼働時期: 2026年4Q〜年末(当初)と2028年開業(現在)。「mothballed」は1社のみの報道。
5. Shackelford の容量・完成時期: IT 負荷 1.4GW、総電力 2.58GW(Cleanview)、2GW・2028年4Q(Epoch)、2029年(Baxtel)。
6. 耐用年数: Microsoft が6年(Burry のグラフ)か4〜5年(Yardeni)か。Meta の「11〜12年」の対象設備区分。
7. GB200 の単価: $8.00(computeprices)と最安 $10.50・平均約 $18(deploybase)。
8. H100 Silicon Data 指数: $2.53(日付なしページ)、$2.75(2026-07-27)、$2.80(2026-08-02)。StockHub の $3.06(2026-09-06)は方法論不明。
9. Abilene 拡張: 「約600MW 拡張の中止」(Tom's Hardware、DCD)と、Oracle の「最終合意に至っていないリースが不成立になっただけで、報道は不正確」という反論。Abilene の残り棟の完成時期(2026年中頃か、最終棟が2029年か)。
10. Oracle の FY2027 capex: 「$900 億〜950 億」と「純現金支出 約 $700 億」。負債総額: $1,080 億〜1,670 億。
11. Bloomberg の「2027→2028年延期」報道の日付が検索結果から特定できていない。Milam County の完了期日「10月15日」の年。Saline Township の $160 億・$140 億債券の報道日。Project Jupiter ローンの値付け報道の日付。
12. OpenAI の IPO: 「2026-06-08 に S-1 を秘密裏に提出」(tech-insider のみ)と「2026年中は上場しない」(Altman 発言とされる)、「Oracle 株が OpenAI の IPO 延期で1週間に9%下落」(1報道)は、いずれも単独ソースで裏付けなし。

### 8-3. 品質上の注意
- 本文の多くが Tier 3〜4 の二次・三次情報で、原典の突合ができていない。特に GPU 価格(1-3、1-4)、OpenAI の資金調達(tech-insider、bitcoin.com)、競合決算(UpperEdge、4WeekMBA、tech-insider)は、会社の決算資料・SEC 提出書類での確認を推奨する。
- Oracle の Q1 FY2027 数値(Tier 1)は検索要約に引用された原文であり、IR ページ本文の直接確認はできていない。
