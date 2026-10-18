# W7: 長期契約インフラ・ネオクラウド・データセンター取引の評価倍率と、成長企業の評価指標(ルール・オブ・40)

- 作成日: 2026-10-12 / 担当: 収集 W7(Oracle の AI クラウド事業を評価するときの外部の物差し)
- 範囲: 事実・数値・出典の整理のみ。投資判断・推奨は書かない。
- 取得手段: WebSearch のみ 26 回(上限 26 回を使い切った。standard 26 回、extended 0 回)。WebFetch なし。**会社の原文(8-K、S-1/A、決算説明会、IR 資料)も証券会社のレポートも 1 件も直接開いていない。** 数値はすべて検索ツールの要約に書かれていた内容で、原典未照合。そのため会社開示でも Tier に * を付ける(Tier 3 相当として扱うこと)。
- 表記: 「欠損」= 見つからなかった。「(算出)」= 調査者の計算(式を併記)。Tier は 1=会社開示・決算説明会、2=規制当局・格付会社・中央銀行・公的統計、3=報道・アナリスト・調査会社、4=ブログ・SNS・販促・集約サイト。
- 出典 ID `[W7-xx]` は本書末尾の出典一覧(xx = 検索の通し番号。1 件の検索で複数 URL を使った場合は同じ番号にまとめた)。既存調査(S1〜S4、R1〜R7、W1〜W6)とは、今回のテーマ(取引倍率・ネオクラウド評価・ルール・オブ・40・SOTP 倍率)で重なる記述を grep で確認したが見つからなかったため、再掲はない。
- 注意: 集約サイト(opencapital.sh、GuruFocus、MarketScreener、datacentres.com 等)の倍率は、同じ銘柄でも時点・EV の定義・EBITDA の定義が違い、検索ツール自身が「相互に矛盾する」と注記した箇所が多い。本書は採否を決めず併記する。

---

## 0. 要約(事実のみ。10 行)

1. **DC 取引の EV/EBITDA(確認できたのは 2021〜22 年の取引のみ)**: Switch 31.3x(EV $11,000M、FactSet 調整後 EBITDA)、CyrusOne 25.5x(EV $15,000M、2022-03)または 26.0x(LTM)、QTS 27.6x(EV/LTM EBITDA、2021-06-07、プレミアム 21%)。Cartica 8-K(2024)と Switch DEFA14A(2022)の比較表。[W7-06] T3*/T1*
2. **2024〜25 年の大型取引は EBITDA 倍率を確認できなかった**: Aligned は EV 約 $40B(2025-10 発表、完了済み)で、1MW あたり約 $6.25M〜$8.0M(算出)。AirTrunk は EV A$24B 超(2024-09)で、別時点の EBITDA A$600M を使うと約 40x(算出、基礎が不一致で参考値)。datacentres.com の 2026 年の倍率レンジ(22〜28x 等)は同サイト内で QTS 4.1x など矛盾する数値があり、Tier 4 として併記のみ。[W7-01][W7-02][W7-05][W7-24]
3. **キャップレート(安定稼働・投資適格テナントのハイパースケール DC)**: 5.0〜6.0%(datacentres.com ガイド)、5.1〜5.6%(同サイト、2026-05 時点)、5.5〜6.5%(APERS 経由で JLL Q1 2026 を引用)。Digital Realty が Blackstone 資産取得で示した初期の安定化後キャップレートは 6.5% 超。逆数は 15.4〜20.0 倍(算出)。すべて Tier 3〜4*、一次の CBRE/JLL 原本は未確認。[W7-07]
4. **CoreWeave の Q2 2026(2026-06 期、2026-08 発表)**: 調整後 EBITDA $1,510M(マージン 59%、前年 $753M・62%)、調整後営業利益 $128M(5%、前年 $200M・16%)、純支払利息 $640M(前年 $267M)、capex $9.4B、バックログ $104B(前年比 +246%)。会社 IR。[W7-22] T1*
5. **CoreWeave の評価倍率は時点と基礎で 2 倍以上ずれる**: EV $95,222M(2026-09-10)で、直近 EV/EBITDA 23.98x(2026-08-22)、EV/売上 約 12.6x(GuruFocus)。MarketScreener の 2026 年 2 月頃のスナップショットは予想ベースで EV/EBITDA 10.8x(2026 年)・7.1x(2027 年)、EV/売上 7.3x(2026 年)。[W7-08] T4*
6. **Nebius の Q2 2026(2026-08-12 発表)**: 売上 $582.3M(前年比 +454%)、調整後 EBITDA $236.2M(41%)、capex $5.7B(別報道は $5.6B)、ARR $3.0B。2026 年ガイダンスは売上 $3.0〜3.4B、ARR $7〜9B、調整後 EBITDA マージン約 40%、capex $20〜25B。検証済みの現行 EV は欠損で、公開されている倍率は 4.8x〜12x と幅がある。[W7-09][W7-23] T1*/T3*
7. **契約単位の回収期間**: CoreWeave の S-1/A(2025 年)は「2024-12-31 時点の確定契約ベースで、前受金を含む平均現金回収期間は約 2.5 年」(調整後 EBITDA で GPU 等の投資を回収する時間)と記載。契約単位の IRR の会社開示は欠損。第三者の仮定モデルでは 5 年契約・売上回収 2.25 年・無レバレッジ IRR 目標 20%。[W7-16][W7-10] T1*/T4
8. **ルール・オブ・40**: Aventis Advisors(2026、上場 SaaS 55 社)で EV/売上との相関は FCF 基準 約 0.49、EBITDA 基準 約 0.23。中央値は FCF 基準 39%、EBITDA 基準 23%、EV/売上 3.6x。設備型企業への標準的な当てはめ方は確認できず、定義(EBITDA / 営業利益 / FCF / capex 控除)で CoreWeave の Q2 2026 のスコアは約 +109〜+170 から約 -197 まで動く(算出、§3.4)。[W7-12][W7-20] T3*/T4
9. **ハイパースケーラーの事業別評価**: BofA(2026-01)は AWS を 2027 年売上の 10x で評価し、Amazon 全体では 2027 年 EBITDA の約 13x に相当(株価 $303 の目標)。無名の SOTP は AWS を営業利益の 20x。Google Cloud の SOTP は無名文書の EV/売上 15x のみ、Azure は証券会社の SOTP 倍率が欠損。[W7-13][W7-18][W7-14][W7-15] T3*/T4
10. **長期契約型インフラ**: タワー(集約サイト、2026 Q1)AMT 13.4x・SBAC 18.6x・CCI 25.2x(EBITDA 減少で高め)、ミッドストリーム KMI 13.9x・WMB 16.6x・EPD 15.2x(ただし各社別の別ソースで 10.5x〜18.0x)、規制公益 前向き EV/EBITDA 11〜14x(銀行業界ガイド)、Damodaran(2026-01)の REIT 19.87x・ソフトウェア 24.48x。光ファイバーは専用検索を行えず欠損。[W7-17][W7-21][W7-25] T3*/T4

---

## 1. データセンターの取引とキャップレート

### 1.1 取引一覧

| 取引 | 時点 | EV | EV/EBITDA | 基礎 | 出典・Tier |
|---|---|---|---|---|---|
| Switch(DigitalBridge・IFM が非公開化) | 2022 年発表(Cartica 資料は 2024) | $11,000M(Reuters も $11B、債務込み、$34.25/株) | 31.3x | FactSet の調整後 EBITDA | Cartica 8-K ex99-2 の比較表 [W7-06] T3*、teiss [W7-06] T3* |
| CyrusOne(KKR・GIP) | 2022-03(完了) | $15,000M(株式は Reuters で $11.49B) | 25.5x | FactSet の調整後 EBITDA | Cartica 8-K [W7-06] T3* |
| CyrusOne(同上、Switch 側の比較表) | 2021〜22 | (表に記載なし) | 26.0x | LTM EBITDA | Switch DEFA14A [W7-06] T1* |
| QTS(Blackstone) | 2021-06-07 | 約 $10B(Reuters) | 27.6x | EV/LTM EBITDA、プレミアム 21% | Switch DEFA14A [W7-06] T1* |
| AirTrunk(Blackstone・CPP Investments) | 2024-09 | A$24B 超(債務と確定プロジェクトの capex を含む) | 欠損 | - | Blackstone 発表 [W7-02] T1*、Macquarie 発表 [W7-05] T1* |
| Aligned Data Centers(AIP・MGX・BlackRock の GIP) | 2025-10 発表(日付は依頼文の記述。検索結果では未確認)、完了済み | 約 $40B(株式 100%、全額エクイティとする報道あり) | 欠損 | - | DCD [W7-01]、pulse2 [W7-01]、完了発表 [W7-01] T3* |

補足(AirTrunk)
- 売り手は Macquarie Asset Management と PSP Investments(合計 88%)。買い手側は Blackstone の複数ファンドと CPP Investments(12% を共同出資)。[W7-02][W7-05] T1*
- 売却プロセスの当初目標は約 A$15B(Reuters を引用した別媒体)。[W7-02] T3*
- 確定済み契約容量は 800MW 超、将来用地 1GW 超。Macquarie の説明として総容量 1.8GW 超との報道もある(450MW から拡大)。[W7-02] T3*
- 倍率の手がかり: IPO 検討時に A$10B の評価額と、EBITDA 約 A$600M という記述(Startup Daily、日付不明)。(算出)A$24,000M ÷ A$600M = 約 40.0x。分子と分母の時点・定義が一致しない可能性があり、参考値。[W7-05] T3*
- 米ドル換算の表記は $16.6B と $16.1B で媒体間にずれがある(§6)。

補足(Aligned)
- 追加で $5B の成長資金を拠出する報道。売り手は Macquarie Asset Management と共同投資家。[W7-01] T3*
- 完了時の発表: 51 キャンパス、運用中と計画中を合わせ 6.4GW 超。発表時の見出しは 5GW(運用中と計画中)。[W7-01] T3*
- (算出)$40B ÷ 6.4GW = $6.25M/MW、$40B ÷ 5GW = $8.0M/MW。VanEck の Matthew Sigel は約 $8M/MW と指摘し、上場マイナーの約 $3M/MW と対比。別の報道は「総容量(パイプライン含む)あたり約 $20M/MW」と記載(§6)。[W7-04] T3*
- EBITDA・売上の公表値は今回の検索では見つからなかった。multiples.vc の Aligned ページは存在するが内容未確認。[W7-04] T4

### 1.2 datacentres.com の 2026 年のレンジ(信頼性が低い。併記のみ)

同サイト(Datacentres.com Research)の 2026-05〜08 の記事群が、互いに矛盾する数値を載せている。検索ツール自身が「同サイトの記述は互いに矛盾し、一次情報で確認すべき」と注記した。[W7-03][W7-24] T4*

| 項目 | 記載値 | 備考 |
|---|---|---|
| ハイパースケーラーのアンカーテナントまたはコンソーシアム関与の取引 | 22〜28x EV/EBITDA | 純粋な REIT 取得は 18〜21x |
| 市場全体の中央値 | 18.2x(2025 上期 19.8x から低下) | |
| 電力を確保済みの事業者 | 20〜24x | グリッド待ち・送電増強待ちは 14〜16x |
| AI 対応 Tier-1 施設 | 18.2〜20.1x | 従来型コロケーション 12.3〜14.6x |
| ハイパースケーラー向け資産 | 14.2〜17.3x | |
| A グレード事業者 | 6.2〜7.1x | 他の値と桁が合わない |
| QTS(Blackstone、2026 年初と記述) | $15.3B、4.1x | 2021-06 の $10B・27.6x(§1.1)と矛盾 |
| CyrusOne(Microsoft が $18.2B、負債 $4.1B 引受、2026E EBITDA $2.16B で 8.4x と記述) | 別記事では Amazon が $18.5B で取得と記述 | 2022 の KKR・GIP 取得(§1.1)と整合せず、記事間でも買い手が食い違う |

### 1.3 安定稼働したハイパースケール DC のキャップレート

| 区分 | キャップレート | 時点 | 出典・Tier |
|---|---|---|---|
| 安定稼働・投資適格テナントの米国主要市場のハイパースケール | 5.1〜5.6% | 2026-05(「CBRE と JLL の資本市場デスク」と曖昧に帰属) | datacentres.com の市況記事 [W7-07] T4* |
| 安定稼働ハイパースケール | 5.5〜6.5%(コロケーションは 6〜7%) | JLL Q1 2026 を引用 | APERS の解説ページ [W7-07] T4*(一次は T3) |
| 単一テナント・15 年超リースのハイパースケール | 5.0〜6.0%。投資適格のハイパースケーラーのリースは格付なしより 100〜200bp 低い | 2026 年 | datacentres.com ガイド [W7-07] T4* |
| Digital Realty が Blackstone から取得した N. バージニア資産 | 完全稼働後の初期の安定化キャップレートが 6.5% 超 | 時点未確認 | 検索要約(出典名の特定不可)[W7-07] T3* |

- (算出)キャップレートの逆数 = 純営業収益の倍率: 5.0% = 20.0x、5.5% = 18.2x、6.0% = 16.7x、6.5% = 15.4x、7.0% = 14.3x。不動産の NOI と事業会社の EBITDA は定義が異なり、§1.1 の倍率とは単純比較できない。
- JLL の 2026 年中間報告として、空室率が 3 年連続で 1% 前後、賃料の年平均上昇率 9% という記述(地域は要約に明記なし)。[W7-07] T3*
- Realty Income が $6B のハイパースケール DC ベンチャーを支援(CRE Daily の見出しのみ。条件は未確認)。[W7-07] T3*

### 1.4 上場 DC REIT の EV/EBITDA

| 銘柄 | 値 | 時点 | 出典・Tier |
|---|---|---|---|
| Equinix | 28.9x(前年同期 28.5x) | 2026 Q1 | opencapital.sh [W7-25] T4* |
| Equinix | 31.6x(5 年中央値 27.7x) | 時点不明(スナップショット) | VCP Scanner [W7-25] T4* |
| Equinix | 前向き AFFO 18.4x、NAV の 86% | 2025-12 | Seeking Alpha [W7-25] T3* |
| Digital Realty | 20.1x(前年 25.2x) | 2025 Q4 | opencapital.sh [W7-25] T4* |

- DLR の前向き 2026 年 EV/EBITDA のコンセンサスは欠損。Motley Fool(2026-07-15)の前向き PER 3 値(85.5x・58.9x・32.7x)は、どれがどの銘柄か要約から判別できず採用しない。[W7-25]

---

## 2. ネオクラウド(CoreWeave・Nebius)の評価と契約経済性

### 2.1 CoreWeave の四半期の事実(Q2 2025 と Q2 2026)

| 項目 | Q2 2025 | Q2 2026(2026-06 期、2026-08 発表) | 出典・Tier |
|---|---|---|---|
| 売上 | (算出)約 $1,215M = 753 ÷ 0.62 | 約 $2.6B(報道)、(算出)約 $2,559M = 1,510 ÷ 0.59 | [W7-10][W7-22] T1*/T3* |
| 調整後 EBITDA | $753M(62%) | $1,510M(59%) | 会社 IR [W7-22] T1* |
| 調整後営業利益 | $200M(16%) | $128M(5%) | 会社 IR [W7-22] T1* |
| GAAP 営業利益 | 欠損 | -$49M | [W7-22] T1* |
| 純支払利息 | $267M | $640M | [W7-22] T1* |
| 純損失 | 欠損 | -$626M | [W7-22] T1* |
| 四半期 capex | 欠損 | $9.4B(約 500MW の稼働電力を追加) | [W7-22] T1* |
| バックログ | (算出)約 $30.1B = 104 ÷ 3.46 | $104B(前年比 +246%)。Q3 の序盤に純額 $25B 超の新規コミットが別途 | [W7-22] T1* |
| 年間見通し | - | 売上と営業利益を引き上げ。理由は「展開の加速、価格上昇、新規契約のマージン拡大」。建設予算は約 $40B との第三者コメント(会社の原文未確認) | [W7-22] T1*/T3* |

(算出)
- 調整後 EBITDA − 調整後営業利益: Q2 2026 = 1,510 − 128 = $1,382M、Q2 2025 = 753 − 200 = $553M。両指標が同じ調整項目を除くなら、この差が減価償却等の概算。
- 調整後 EBITDA ÷ 純支払利息: Q2 2026 = 1,510 ÷ 640 = 2.4x。Q2 2025 = 753 ÷ 267 = 2.8x。
- 四半期 capex ÷ 調整後 EBITDA(Q2 2026)= 9,400 ÷ 1,510 = 6.2x。
- 調整後営業利益率は前年比 11 ポイント低下(16% → 5%)、調整後 EBITDA マージンは 3 ポイント低下(62% → 59%)。会社は「新規契約のマージン拡大」とも述べており、同じ四半期の中で逆向きの記述が併存する(世代別・契約別の内訳は欠損)。

### 2.2 Nebius の四半期の事実

| 項目 | 値 | 時点 | 出典・Tier |
|---|---|---|---|
| 売上 | $582.3M(前年比 +454%)。AI クラウドは $575M(98%) | Q2 2026(2026-08-12 発表) | quartr、w.media [W7-23] T3* |
| 調整後 EBITDA(グループ) | $236.2M、マージン 41% | 同上 | [W7-23] T3* |
| AI クラウドの調整後 EBITDA マージン | 49.7%(2025-12 期は 24%) | 同上 | [W7-23] T3* |
| capex | $5.7B(別報道の見出しは $5.6B)。上期の合計 $8.1B 超 | Q2 2026 | [W7-23] T3* |
| 顧客前受金 | capex の 50〜70% を賄う(1 報道)。別見出しは「前受金は 60% のみ」 | 2026 | [W7-23] T3* |
| 営業キャッシュフロー | $2.3B | Q2 2026 | [W7-23] T3* |
| 現金 | $8B | 2026-06 末 | [W7-23] T3* |
| ARR | $3.0B(2026-03 末 $1.9B から +56%)。定義は直近月の AI クラウド売上 × 12 | 2026-06 末 | [W7-23][W7-09] T1*/T3* |
| 2026 年ガイダンス | 売上 $3.0〜3.4B、ARR(年末)$7〜9B、調整後 EBITDA マージン約 40%、capex $20〜25B。契約電力の目標を 5GW に引き上げ | 2026-08(再確認、引き上げなし) | 6-K、quartr [W7-09][W7-23] T1*/T3* |
| H100 のオンデマンド価格 | 1 GPU 時間 $3.85 → $4.50(+17%)、2026-10-01 から | 2026-09〜10 の報道 | [W7-11] T4* |

(算出)
- Q2 capex ÷ 売上 = 5,700 ÷ 582.3 = 9.8x。
- Q2 営業キャッシュフロー − capex = 2,300 − 5,700 = -$3,400M。営業キャッシュフロー $2.3B は調整後 EBITDA $236.2M の約 9.7 倍(前受金の影響が大きいことが示唆されるが、内訳は欠損)。
- 調整後 EBITDA マージンの高さについて、「高い減価償却が見かけの 50% マージンを損なう」とする分析が 1 件ある(出典名の特定不可)。[W7-23] T4*

### 2.3 評価倍率

| 対象 | 倍率 | 時点 | 出典・Tier |
|---|---|---|---|
| CoreWeave | EV $95,222M | 2026-09-10 | GuruFocus [W7-08] T4* |
| CoreWeave | EV/EBITDA 23.98x(直近、EBITDA 約 $3.9B)。同サイトは「中央値より 19% 低い」と表示 | 2026-08-22 | GuruFocus [W7-08] T4* |
| CoreWeave | EV/売上 約 12.6x(直近売上 約 $7.6B) | 2026-08〜09 | GuruFocus [W7-08] T4* |
| CoreWeave | 予想 EV/EBITDA 10.8x(2026 年)・7.1x(2027 年)、EV/売上 7.3x(2026 年)。EV 88,214(百万ドル)、2026 年 EBITDA 約 $8.2B、売上 約 $12.0B | 2026 年 2 月頃のスナップショット | MarketScreener [W7-08] T4* |
| CoreWeave | EV/FY26E 売上 7.66x、2026 年末 ARR の 5.18x | 2026 年 | Seeking Alpha [W7-08] T3* |
| CoreWeave | EV/EBIT(CY2026)約 41x(Barclays の格下げ時) | 2025-05 | Seeking Alpha [W7-08] T3* |
| CoreWeave | EV/売上 12.4x、EV/EBITDA 16.9x(EV 約 CAD 133B、カナダ上場ライン) | 時点不明 | StockAnalysis [W7-08] T4*(通貨・EV が異なり比較不可) |
| Nebius | 時価総額 約 $61.5B。売上のコンセンサス 2026 年 約 $3.4B → 2027 年 約 $11B → 2028 年 約 $21B | 2026-06 | TIKR [W7-09] T3* |
| Nebius | 現在(NTM)EV/売上 約 12x | 2026-06 | TIKR(ドイツ語版)[W7-09] T3* |
| Nebius | EV/ARR 約 8.5x、2027 年 EV/売上 6.2x | 日付不明 | Seeking Alpha [W7-09] T3* |
| Nebius | 前向き売上倍率 5.6x(CoreWeave 2.2x と対比) | 日付不明 | Seeking Alpha [W7-09] T3* |
| Nebius | EV 25,220(2026 年)・37,050(2027 年)、EV/売上 7.3x(2026 年)・4.76x(2027 年) | 株価約 $87.69 の時点 | MarketScreener [W7-09] T4*(2026-06 の株価約 $240 と大きく乖離し、古い) |

(算出、いずれも時点・基礎が混在するため参考値)
- CoreWeave: EV $95.2B ÷ バックログ $104B = 0.92x。EV $95.2B ÷ Q2 2026 売上の年率換算($2.6B × 4 = $10.4B)= 9.2x。EV $95.2B ÷ Q2 2026 調整後 EBITDA の年率換算($1,510M × 4 = $6,040M)= 15.8x。
- Nebius: 時価総額 $61.5B ÷ 2026 年コンセンサス売上 $3.4B = 18.1x。÷ 2027 年 $11B = 5.6x。÷ ARR $3.0B = 20.5x(時価総額ベース、ネット現金 約 $8B 等は未調整、EV ではない)。

### 2.4 契約単位の回収期間・IRR・世代別の利益率

| 項目 | 内容 | 時点 | 出典・Tier |
|---|---|---|---|
| CoreWeave の平均現金回収期間 | 「2024-12-31 に有効な確定契約を基礎に、前受金を含む平均現金回収期間は約 2.5 年と見込む。現金回収期間は、GPU 等の有形固定資産への投資を調整後 EBITDA で回収するのに要する時間」 | S-1/A(2025 年。アクセッション番号 0001193125-25-052207) | SEC 提出書類 [W7-16] T1* |
| 契約単位の IRR | 会社開示は見つからなかった(欠損) | - | [W7-10][W7-16] |
| 会社の説明 | 典型的な 5 年契約でその配備に係る資産レベルの負債を返済し、引き受け時の想定リターンを得る。CFO「再販または更新はすべて、当初期間内で得たリターンの上に積み上がる増分」 | 2026 年 | Blockspace [W7-10] T3* |
| 契約期間の食い違い | 新設の $2.6B DDTL 5.5 の満期は 5 年だが、顧客契約の平均は約 3 年 | 2026 年 | Motley Fool の論評 [W7-10] T3* |
| 更新・再販の実例 | A100 の契約が 2029 年まで延長(顧客・GPU 数・金額は非開示)。2020 年の GPU を 2029 年まで使う | Q2 2026 の説明会 | letsdatascience、Blockspace [W7-10] T3* |
| 前受金 | Q2 の 4 件の契約が各 $1B 超、うち 70% が前受(二次情報) | 2026 Q2 | [W7-11] T4* |
| 第三者モデル(Rittenhouse Research) | 100MW・5 年契約・売上回収 2.25 年・無レバレッジ IRR 目標 20%、GPU capex $2.7B の 75% を DDTL(年率約 8%)で調達、稼働率 85%。「CoreWeave は主要な現金支出が高い確度で予測でき、望む IRR を得るよう契約を値付けできる」と仮定 | 2026 年 | Substack [W7-10] T4 |
| 第三者モデル(VC のデューデリジェンス資料) | H100、混合単価 $1.54/時、稼働率 70% で粗利率 76.4%。稼働率 50% で粗利率 68.8%・現金回収 83.9 か月、90% で 80.6%・39.8 か月 | 2026 年 | k-dense.ai [W7-11] T4(販促色、前提未検証) |
| 損益分岐の稼働率 | 負債調達のクラスターで約 70% | 2026 年 | moduledge.com [W7-16] T4* |
| 低価格帯の GPU 単価 | 2026 年初に 1 GPU 時間 $2.85〜3.50、64〜75% 低下(Silicon Data 2026 を引用) | 2026 年初 | moduledge.com [W7-16] T4* |
| 定価 | CoreWeave の H100 約 $6.16/時、B200 約 $8.60/時。予約契約は最大 60% 割引(営業経由のみ)。Nebius の H100 は $3.85(別ガイドは $2.95)、B200 $5.50(同) | 2026 年 | CloudZero、deploybase、spheron [W7-11] T4* |
| 世代別の利益率(会社開示) | 欠損 | - | [W7-11] |
| 更新後の GPU 経済性 | Clouded Judgement 2026-05-29「The Second Life of a GPU」が検索に出たが、本文は未読 | 2026-05-29 | [W7-16] T3*(見出しのみ) |

(算出)
- S-1/A の 2.5 年は、5 年契約なら契約期間の 50%、3 年契約なら 83%(2.5 ÷ 5、2.5 ÷ 3)。契約期間の前提が 5 年か 3 年かで、回収後に残る契約期間の比率が変わる。契約期間の食い違いは §6。
- 定義の注意: 回収期間は「調整後 EBITDA」で測っており、支払利息(Q2 2026 で調整後 EBITDA の 42% = 640 ÷ 1,510)と運転資本は含まない。IRR や NPV とは別の指標。

---

## 3. ルール・オブ・40

### 3.1 定義の種類

| 定義 | 内容 | 使われ方 | 出典・Tier |
|---|---|---|---|
| 売上成長率 + EBITDA マージン | 実務で最も一般的。証券会社のレポートや決算コメントで多い | | Aventis Advisors [W7-12] T3* |
| 売上成長率 + FCF マージン | FCF = 営業キャッシュフロー − capex。投資家の多くが好む(操作しにくい)という見解。EBITDA 基準との差は主に株式報酬 | | Aventis、tickerleague [W7-12] T3*/T4* |
| 売上成長率 + 営業利益率(EBIT) | Princeton の学位論文(北米 SaaS、2015〜2025)で EBITDA・EBIT マージンはほとんどのグループで頑健な予測変数、大きい企業では FCF マージンの重要度が上がる | | Princeton [W7-12] T3* |
| capex を控除した版(EBITDA − capex) | 標準定義は見つからなかった。検索要約が「実務では EBITDA から capex を引く方法もある」と示唆したが、調査者の提案であり確立した慣行ではない | | [W7-20] T4* |

### 3.2 上場ソフトウェアのスコアと評価倍率の関係

| 項目 | 値 | 時点・標本 | 出典・Tier |
|---|---|---|---|
| EV/売上との相関(FCF 基準のルール・オブ・40) | 約 0.49 | 2026、上場 SaaS 55 社 | Aventis Advisors [W7-12] T3* |
| EV/売上との相関(EBITDA 基準) | 約 0.23 | 同上 | 同上 |
| 外れ値 7 社を除くと関係が強まる | 具体値は要約が途切れて欠損 | 同上 | 同上 |
| 中央値 | FCF 基準 39%、EBITDA 基準 23%、EV/売上 3.6x | 同上 | 同上 |
| 全体の EV/NTM 売上の中央値 | 4.1x(約 10 年ぶりの低さ) | 2026-01-30 | Clouded Judgement [W7-19] T3* |
| 成長調整後の売上倍率(EV/NTM 売上 ÷ NTM 成長率) | 0.35x(コロナ前の平均 0.28x) | 2026-01-30 | 同上 |
| FCF 倍率の中央値 | 18.9x | 2026-01-30 | 同上 |
| NTM 成長率 22% 超 | EV/NTM 売上の中央値 14.6x | 2025-12-26 | Clouded Judgement [W7-19] T3* |
| NTM 成長率 15〜22% | 7.7x | 同上 | 同上 |
| NTM 成長率 15% 未満 | 3.7x | 同上 | 同上 |
| NTM 成長率の中央値 / FCF マージンの中央値 | 12% / 19% | 同上 | 同上 |
| 2026 年中盤の EV/NTM 売上の中央値 | 4〜5x(Clouded Judgement・Meritech を引用)と 約 6.8x(2026-05、BVP・Clouded Judgement を引用)が併存 | 2026 年 | valueaddvc.com 2 記事 [W7-19] T4* |

(算出)中央値の和 12% + 19% = 31(2025-12 の成長率中央値と FCF マージン中央値の単純合計。各社のスコアの中央値ではない)。Aventis の FCF 基準の中央値 39% とは標本が違う(§6)。

### 3.3 設備型・低粗利企業への当てはめに関する議論

- ルール・オブ・40 は SaaS 向けに作られた指標で、他の業種に当てはめると誤解を招くという記述(用語集・ガイド)。資本集約的・低マージンの事業では成長と利益のトレードオフが成り立ちにくいとされる。[W7-20] T4*
- 粗利率 30% の企業では、成長と利益を交換する余地が小さく、ルール・オブ・40 が同じようには機能しないという主張が 1 件。[W7-20] T4*
- FCF マージンは capex の先送りで見かけ上改善できる。capex が大きく不規則なネオクラウドでは歪みが起きうる。[W7-20] T4*
- 資本集約的なソフトウェアでは、EBITDA 基準と FCF 基準でスコアが大きく分かれる。純粋な SaaS では差は通常小さい。[W7-20] T4*
- ネオクラウドや AI インフラにルール・オブ・40 を適用した公表分析は、今回の検索では見つからなかった(欠損)。

### 3.4 定義別スコアの(算出)

事実の整理であり、どの定義が妥当かの判断は含まない。成長率はマージン(整数%に丸め)からの逆算で、誤差がある。

| 企業・期間 | 成長率(前年比) | 調整後 EBITDA マージン | 調整後営業利益率 | GAAP 営業利益率 | 四半期 capex |
|---|---|---|---|---|---|
| CoreWeave Q2 2026 | (算出)約 +111%(式: 1,510 ÷ 0.59 = 2,559 ÷(753 ÷ 0.62 = 1,215)= 2.11。マージンの丸めで +107〜+114%) | 59% | 5% | (算出)-1.9%(= -49 ÷ 2,559) | $9.4B |
| Nebius Q2 2026 | +454% | 41%(AI クラウド 49.7%) | 欠損 | 欠損 | $5.7B |

| 定義 | CoreWeave Q2 2026 | Nebius Q2 2026 |
|---|---|---|
| 成長率 + 調整後 EBITDA マージン | (算出)111 + 59 = 約 170 | (算出)454 + 41 = 495 |
| 成長率 + 調整後営業利益率 | (算出)111 + 5 = 約 116 | 欠損 |
| 成長率 + GAAP 営業利益率 | (算出)111 +(-1.9)= 約 109 | 欠損 |
| 成長率 +(調整後 EBITDA − 四半期 capex)÷ 売上(非標準の定義) | (算出)111 + (1,510 − 9,400) ÷ 2,559 × 100 = 111 − 308 = 約 -197 | (算出)454 + (236.2 − 5,700) ÷ 582.3 × 100 = 454 − 938 = 約 -484 |
| 成長率 + FCF マージン | 欠損(CoreWeave の FCF は今回の検索で未取得) | 欠損(営業キャッシュフロー $2.3B − capex $5.7B = -$3.4B は §2.2) |

注: 四半期の capex は先行投資で、同じ四半期の売上に対応しない。成長率が極端に大きい企業では、定義に関係なくスコアの絶対値は意味を持ちにくい。

---

## 4. ハイパースケーラーの事業別評価(SOTP)

### 4.1 AWS(Amazon)

| 内容 | 倍率 | 時点 | 出典・Tier |
|---|---|---|---|
| BofA(Justin Post): 買い推奨、目標 $303。AWS を 2027 年売上の 10x、第一者小売 1.1x、第三者小売 2.5x、広告 5.0x で評価。全体では売上倍率 3.7x、2027 年 EBITDA 13x、2027 年 EPS 33x に相当 | AWS = EV/2027 売上 10x | 2026-01(Benzinga 配信を Webull が転載) | [W7-13] T3* |
| 同じ BofA ノート: 株価約 $250 のとき Amazon は Street の 2027 年 EBITDA の約 11x | 全体 EV/EBITDA 約 11x(2027 年) | 2026-01 | [W7-13][W7-18] T3* |
| 無名の SOTP 枠組み: AWS 営業利益の 20x、広告 EBITDA の 18x、小売の利益 12〜15x で公正価値 $270〜$310 | AWS = 営業利益 20x | 2026 年 | MEXC ブログ [W7-18] T4* |
| Amazon 全体の NTM EV/EBITDA | 10.96x。NTM PER 27.08x | 2026 年 | TIKR [W7-13] T3* |
| AWS の事業実績: 2026 Q1 売上 $37.6B、営業利益 $14.2B、直近 12 か月の営業利益 $48.2B | - | 2026 Q1(TIKR 更新 2026-06-24) | TIKR [W7-13][W7-18] T3* |
| SOTP に別の売上ベースを使う例: 公正価値 約 $2.6T(株価約 $207 の時点)、2027 年に $3〜3.6T(株価 最大 $340) | 売上倍率 | 2026 年 | TIKR [W7-13] T3* |

(算出)AWS 2026 Q1 営業利益率 = 14.2 ÷ 37.6 = 37.8%。AWS 営業利益 $48.2B(直近 12 か月)× 20 = $964B(MEXC の 20x を直近 12 か月の営業利益にあてた参考値。MEXC 自身がこの基礎を使ったかは不明)。AWS の 2027 年売上の予想値は今回の検索で取得できず、BofA の 10x の金額換算は欠損。

### 4.2 Google Cloud(Alphabet)

| 内容 | 値 | 時点 | 出典・Tier |
|---|---|---|---|
| Insider Monkey: Cloud の 2026 Q2 売上 $24.77B、営業利益 $8.81B(約 35.6%)。営業利益の年率ペースに 20x・30x・40x を掛けると EV $705B・$1.06T・$1.41T | 20〜40x は仮定の感度で、証券会社の見解ではない | 2026 Q2 | [W7-14] T3* |
| 無名・日付なしの Google ドキュメント: Cloud に EV/売上 15x を、直近売上 $43.2B に適用して約 $648B。Alphabet 全体 EV 約 $2.93T、1 株 約 $248(現株価の 20% 安と記述) | 15x | 日付不明 | [W7-14] T4* |
| Cloud の 2025 年売上 $58.7B、営業利益 $13.9B(2 倍超) | - | 2025 年 | ドイツ語の記事(boerse-express か TIKR ドイツ語版のどちらか。要約から特定不可)[W7-14][W7-26] T3* |
| Cloud の受注残 $462B 超(TIKR 見出し) | - | 2026 年 | [W7-26] T3*(見出しのみ) |
| Mizuho(Lloyd Walmsley): 目標 $420(旧 $410)、Cloud 売上が 2027 年に $149B に達しうる。Evercore ISI(Mahaney): $400。Wolfe: $360(旧 $390)。JP Morgan: 2026 年のトップピック、目標 $460 | SOTP の倍率は要約に記載なし | 2026 年 | Yahoo Finance、TIKR [W7-26] T3* |
| Wiz 買収による Cloud の営業利益率への逆風が 2026 年の残りにある。2027 年の capex は $180〜190B 超に増加の見通し | - | 2026 Q1 後 | TIKR [W7-14] T3* |

(算出)$8.81B × 4 = $35.24B。× 20 = $704.8B、× 30 = $1,057B、× 40 = $1,410B(Insider Monkey の数値と整合)。無名文書の「直近売上 $43.2B」は 2026 Q2 の年率 $24.77B × 4 = $99.1B と合わず、古い売上に倍率を掛けている可能性がある(§6)。

### 4.3 Azure(Microsoft)

| 内容 | 値 | 時点 | 出典・Tier |
|---|---|---|---|
| 証券会社が Azure に付ける EV/EBIT・EV/売上の SOTP 倍率 | 欠損 | - | [W7-15] |
| Azure の年間売上が FY2026 に $100B を超える。次四半期の成長率ガイダンスは約 45%。FQ3 FY26 は +40%(BNP Paribas は固定為替で 39%) | - | 2026-04〜08 | TIKR、Benzinga [W7-15] T3* |
| Microsoft 全体: NTM PER 24.5x、直近 12 か月の EBIT マージン 46.8% | - | 2026-08 | TIKR [W7-15] T3* |
| 証券会社の目標株価の平均 $561(56 社、レンジ $400〜$870)。前向き PER 約 22x(5 年平均 約 31x) | - | 2026-06 | 報道 [W7-15] T3* |

---

## 5. 長期契約型インフラの EV/EBITDA

### 5.1 セクター別

| 区分 | EV/EBITDA | 時点 | 出典・Tier |
|---|---|---|---|
| REIT(広義。タワー、DC を含む) | 19.87x | 2026-01 | Damodaran(NYU)[W7-17] T3*(学術公開データ) |
| ソフトウェア | 24.48x | 2026-01 | 同上 |
| 半導体 | 34.75x | 2026-01 | 同上 |
| バイオ | 15.78x | 2026-01 | 同上 |
| 石油・ガス(上流) | 5.15x | 2026-01 | 同上 |
| 規制公益 | 前向き EV/EBITDA 11〜14x | 2026 年 | 銀行業界ガイド [W7-17] T4* |
| 総合電気通信 | 6.39x | 日付不明 | 同じ検索の表 [W7-17] T4* |
| 無線通信 | 9.59x | 日付不明 | 同上 |

### 5.2 タワー

| 銘柄 | EV/EBITDA | 時点 | 備考・出典・Tier |
|---|---|---|---|
| American Tower | 13.4x(前年同期 16.5x) | 2026 Q1 | opencapital.sh [W7-21] T4* |
| American Tower | - | - | 2026 年の調整後 EBITDA のガイダンス $7,240〜7,310M(Q2 2026 の 8-K)[W7-21] T1* |
| SBA Communications | 18.6x | 日付不明 | opencapital.sh [W7-21] T4* |
| Crown Castle | 25.2x | 2026 Q1 | EBITDA が前年比 -8.7% で分母が縮小。opencapital.sh [W7-21] T4* |

### 5.3 ミッドストリーム(パイプライン)

| 銘柄 | EV/EBITDA | 時点 | 出典・Tier |
|---|---|---|---|
| Kinder Morgan | 13.9x(2026 Q1)/ 14.74x(直近、別ソース) | 2026 | opencapital.sh、別ソース [W7-21] T4* |
| Williams | 16.6x / 18.04x(別ソース) | 2026 | 同上 |
| Enterprise Products | 15.2x(2026 Q1)/ 10.48x(Zacks、直近)/ 11.70x(ミッドストリーム比較) | 2026 | 同上 |

- opencapital.sh の過去値には KMI 2025 年 54.4x など非現実的な値があり、検索ツールが信頼しないよう注記した。YCharts の前向き EV/EBITDA ページは値を返さなかった。[W7-21] T4*

### 5.4 光ファイバー

- 欠損。専用の検索(取引倍率、Verizon・Frontier や AT&T の光ファイバー取引など)は検索上限のため実施できなかった。

---

## 6. 食い違い(どちらも採らず併記)

| 項目 | A | B | 備考 |
|---|---|---|---|
| AirTrunk の米ドル表記 | $16.6B(Blackstone 他の報道) | $16.1B | 為替レートの違いと推測されるが、要約に根拠なし。A$24B 自体は一致 |
| Aligned の 1MW あたり | 約 $8M(VanEck、$40B ÷ 5GW = $8.0M と整合) | 約 $20M(総容量、パイプライン含むとの記述) | 完了時の発表は 6.4GW 超で、(算出)$40B ÷ 6.4GW = $6.25M。容量の基礎が運用中・計画中・パイプラインで異なる |
| Aligned の容量 | 5GW(発表時の見出し) | 6.4GW 超(完了時の発表) | 時点が違う(発表時と完了時) |
| QTS の倍率 | 27.6x(2021-06、EV/LTM EBITDA、Switch DEFA14A) | 4.1x(datacentres.com、2026 年初の $15.3B 取得と記述) | 後者は取引内容自体が既知の事実(2021 年の約 $10B)と合わない記述。Tier 4 |
| CyrusOne の倍率 | 25.5x(Cartica / FactSet、調整後 EBITDA、EV $15,000M) | 26.0x(Switch DEFA14A 側の表、LTM) | EBITDA の定義の違い |
| CyrusOne の買い手 | KKR・GIP(2022、SEC 資料) | Microsoft($18.2B、8.4x)または Amazon($18.5B)(datacentres.com の記事間で食い違う) | 後者は Tier 4 で記事間でも不一致 |
| DC M&A の中央値 | 18.2x(datacentres.com) | 22〜28x(アンカーテナント付き取引、同サイト) | 取引区分が違うと同サイトが説明するが、同サイト内に 4.1x〜28x が併存 |
| 2026 H1 の DC M&A 総額 | $85B 超 | $127B、$185B、$187B(datacentres.com の記事間) | 取引の定義の差と思われるが要約に根拠なし |
| CoreWeave の EV/EBITDA | 7.1x〜10.8x(予想、MarketScreener、2026 年 2 月頃) | 約 24x(直近、GuruFocus、2026-08) / 16.9x(StockAnalysis、CAD ベース) | 分母が予想か直近か、EV が USD か CAD か、時点が違う |
| CoreWeave の EV/売上 | 7.3x(予想 2026 年) / 7.66x(Seeking Alpha) | 約 12.6x(直近) / 12.4x(CAD ベース) | 同上 |
| CoreWeave の契約期間 | 典型は 5 年(CoreWeave の説明、Blockspace) | 顧客契約の平均は約 3 年(Motley Fool) | 平均と典型の違いの可能性。契約期間の分布は欠損 |
| Nebius の売上倍率 | 4.76x(2027 年、MarketScreener、古い株価) / 5.6x / 6.2x(2027 年) | 約 12x(NTM、TIKR、2026-06) | 株価が約 $87.69 → 約 $240 と大きく動いた時点の違い。現行 EV は欠損 |
| Nebius の capex | $5.7B(複数) | $5.6B(Webull の見出し) | 丸めまたは定義の差 |
| Nebius の前受金のカバー率 | capex の 50〜70% | 60%(Webull の見出し) | 範囲内 |
| H100 の価格(Nebius) | $3.85 → $4.50(+17%、2026-10-01 から) | $2.95(別ガイド) | 日付・種別(オンデマンド / 契約)の違い |
| ルール・オブ・40 の中央値 | 39%(FCF 基準、Aventis、SaaS 55 社) | (算出)31 = 12% + 19%(Clouded Judgement の 2025-12 の中央値の和) | 標本・時点・集計方法(中央値の和か、各社のスコアの中央値か)が違う |
| 上場 SaaS の EV/NTM 売上の中央値(2026) | 4.1x(2026-01-30、Clouded Judgement) / 3.6x(Aventis、EV/売上) / 4〜5x | 約 6.8x(2026-05、BVP・Clouded Judgement を引用) | 前向きか直近か、標本が違う。いずれも原典未照合 |
| Amazon の目標株価 | コンセンサス 約 $312 | 平均 $280.47(62 社) | 時点・集計の差 |
| Google Cloud の売上基礎 | 2026 Q2 の年率 $99.1B(算出)/ 2025 年 $58.7B | 無名文書の直近売上 $43.2B | 無名文書は古い売上の可能性 |
| タワーの EV/EBITDA | AMT 13.4x(2026 Q1) | 同じ集約サイトの過去値に非現実的な値 | 集約サイトの信頼性 |
| ミッドストリームの EV/EBITDA | EPD 15.2x(2026 Q1) | 10.48x(Zacks)/ 11.70x | EV と EBITDA の定義・期間の差 |
| DLR / EQIX の前向き PER | 85.5x・58.9x(Motley Fool) | 32.7x(セクター基準と読める) | 銘柄の対応が要約から不明で不採用 |

---

## 7. 欠損と試した検索語

### 7.1 欠損項目

| 項目 | 状況 | 試した検索(通し番号) |
|---|---|---|
| Aligned の EBITDA・EV/EBITDA | 欠損。EV・容量・1MW あたりのみ | 1, 4 |
| AirTrunk の発表時点の EV/EBITDA | 欠損。別時点の EBITDA A$600M から(算出)約 40x のみ | 2, 5 |
| 2024〜26 年の DC 取引の信頼できる倍率(一次) | 欠損。2021〜22 年の 3 件のみ。2026 年は datacentres.com の矛盾した記述のみ | 3, 6, 24 |
| 安定稼働ハイパースケール DC のキャップレートの一次(CBRE・JLL・Cushman・Newmark の原本) | 欠損。二次・三次のみ | 7 |
| CoreWeave の契約単位の IRR | 欠損 | 10, 11, 16 |
| ネオクラウドの世代別(H100・H200・B200・GB200)の粗利率・EBITDA マージン | 欠損 | 11, 16, 22, 23 |
| CoreWeave の Q2 2026 の前年比売上成長率、FCF | 欠損(売上成長率はマージンから逆算の(算出)のみ) | 22 |
| Nebius の検証済みの現行 EV・EV/EBITDA | 欠損 | 9, 23 |
| Azure の SOTP 倍率(証券会社) | 欠損 | 15 |
| Google Cloud の SOTP 倍率(証券会社名つき) | 欠損 | 14, 26 |
| AWS の EV/EBIT・EV/EBITDA の証券会社の SOTP 倍率 | 欠損。BofA の EV/売上 10x のみ | 13, 18 |
| ルール・オブ・40 と EV/売上の関係の Meritech・Bessemer の調査結果(R² 等) | 欠損。Aventis の相関係数のみ | 12, 19 |
| ネオクラウド・AI インフラにルール・オブ・40 を当てはめた公表分析、capex 控除版の標準 | 欠損 | 12, 20 |
| 光ファイバーの EV/EBITDA、パイプラインの取引倍率、規制公益の一次データ | 欠損。光ファイバーは専用検索なし | 17, 21 |
| タワーの取引倍率(会社の開示、一次の EV/EBITDA) | 欠損。集約サイトのみ | 21 |

### 7.2 検索ログ(26 回、すべて standard)

| 通し番号 | 検索語 |
|---|---|
| 1 | Aligned Data Centers $40 billion acquisition BlackRock GIP MGX AIP EV/EBITDA multiple |
| 2 | AirTrunk Blackstone A$24 billion EBITDA multiple data center acquisition valuation |
| 3 | data center M&A EV/EBITDA multiples 2025 2026 Switch QTS CyrusOne transaction multiple |
| 4 | Aligned Data Centers deal valuation times EBITDA analysts multiple Macquarie sale "EBITDA" |
| 5 | AirTrunk Blackstone "times EBITDA" OR "x EBITDA" OR "EBITDA multiple" Macquarie PSP sale |
| 6 | Switch Inc DigitalBridge IFM $11 billion take-private EBITDA multiple; CyrusOne KKR GIP $15 billion EBITDA multiple; QTS Blackstone $10 billion multiple |
| 7 | hyperscale data center cap rate stabilized 2026 CBRE OR JLL OR Cushman OR Newmark cap rates leased hyperscale |
| 8 | CoreWeave EV/EBITDA EV/revenue 2026 valuation multiple analysts enterprise value |
| 9 | Nebius Group EV/sales 2026 2027 valuation multiple enterprise value ARR guidance |
| 10 | CoreWeave contract payback period cash payback IRR per contract GPU cluster Intrator "payback" years |
| 11 | Nebius OR CoreWeave unit economics per GPU hour H100 B200 contract margin by GPU generation adjusted EBITDA margin payback |
| 12 | Rule of 40 definition revenue growth plus free cash flow margin vs EBITDA margin median public SaaS EV/revenue multiple correlation |
| 13 | Amazon sum-of-the-parts AWS valuation multiple EV/EBIT EV/EBITDA analyst price target 2026 AWS valued at |
| 14 | Alphabet sum-of-the-parts Google Cloud valuation multiple EV/sales EV/EBIT analyst 2026 Google Cloud valued |
| 15 | Microsoft sum-of-the-parts Azure intelligent cloud valuation multiple analyst 2026 EV/EBIT Azure valued at |
| 16 | neocloud GPU contract cash payback "2.5 years" OR "30 months" OR "two and a half years" take-or-pay IRR GPU lease economics |
| 17 | EV/EBITDA multiples by sector 2026 cell towers American Tower SBA pipelines midstream regulated utilities Digital Realty Equinix enterprise value to EBITDA |
| 18 | AWS SOTP "EV/EBIT" OR "EBIT multiple" AWS valued analyst note Amazon sum of parts 2026 Morgan Stanley OR Jefferies OR Wolfe OR Bernstein |
| 19 | Clouded Judgement 2026 median EV/NTM revenue public software growth-adjusted multiple regression revenue growth free cash flow margin |
| 20 | Rule of 40 capital intensive businesses limitations capex depreciation adjusted "rule of 40" infrastructure cloud neocloud applying |
| 21 | American Tower SBA Crown Castle EV/EBITDA 2026 tower valuation multiple; Kinder Morgan Williams Enterprise Products EV/EBITDA 2026 midstream |
| 22 | CoreWeave second quarter 2026 results adjusted operating income margin adjusted EBITDA interest expense backlog capex guidance |
| 23 | Nebius second quarter 2026 results adjusted EBITDA margin capex ARR guidance 2026 Nebius AI cloud revenue |
| 24 | data center platform acquisitions priced at 25x 30x EBITDA hyperscale developers valuation premium Breakingviews OR Reuters OR Bloomberg 2025 2026 multiple |
| 25 | Digital Realty Equinix EV/EBITDA forward 2026 multiple data center REIT valuation versus history |
| 26 | Alphabet SOTP Google Cloud worth analyst "Google Cloud" valued multiple of operating income OR revenue Mizuho OR Evercore OR "Morgan Stanley" OR Wedbush 2026 sum-of-the-parts |

---

## 8. 出典一覧

(すべて検索結果の要約経由。原本は未開封。URL は検索結果に出たもの)

- [W7-01] Aligned 取引: https://pulse2.com/aip-mgx-and-blackrocks-gip-to-buy-aligned-data-centers-in-40-billion-deal / https://datacenterdynamics.com/en/news/aligned-data-centers-sold-to-blackrock-and-mgx-in-record-breaking-40bn-deal / https://www.01net.it/aip-mgx-and-blackrocks-gip-close-acquisition-of-aligned-data-centers/ / https://www.3dtested.com/tech-industry/artificial-intelligence/groups-including-blackrock-microsoft-nvidia-and-xai-join-forces-to-acquire-aligned-data-centers-usd40b-deal-delivers-5gw-of-operational-and-planned-data-center-capacity T3*
- [W7-02] AirTrunk 取引: https://www.blackstone.com/news/press/blackstone-announces-agreement-to-acquire-airtrunk-in-a-a24b-transaction/ (T1*) / https://bnnbloomberg.ca/business/2024/09/04/blackstone-to-buy-australias-airtrunk-in-a24-billion-deal / https://mingtiandi.com/real-estate/data-centres/blackstone-cppib-to-buy-data-centre-giant-airtrunk-in-16b-deal / https://capacityglobal.com/news/blackstone-buys-airtrunk-in-a-deal-valued-at-over-a-24-billion/ (T3*)
- [W7-03] DC M&A 2026(信頼性低): https://www.datacentres.com/news/data-centre-m-a-reaches-187b-in-2026-as-hyperscalers-fuel-consolidation-wave-slot1-2026-06-09 / https://www.datacentres.com/news/data-centre-m-a-hits-127b-in-h1-2026-as-hyperscalers-consolidate-power-assets-slot1-2026-07-14 / https://www.datacentres.com/news/data-centre-m-a-hits-87b-in-h1-2026-as-hyperscalers-reshape-portfolio-architectu-slot1-2026-08-04 / https://www.datacentres.com/news/data-centre-m-a-hits-185b-in-2026-as-hyperscalers-drive-consolidation-wave-slot1-2026-07-21 / https://multiples.vc/data-centers-valuation-multiples T4*
- [W7-04] Aligned 評価: https://forklog.com/en/blackrock-nvidia-and-microsoft-to-acquire-data-centre-owner-for-40-billion/ / https://multiples.vc/private-comps/aligned / https://www.datacentres.com/news/aligned-40b-acquisition-record T3*/T4*
- [W7-05] AirTrunk 売却: https://www.macquarie.com/au/en/about/news/2024/macquarie-asset-management-and-psp-investments-announce-sale-of-airtrunk.html (T1*) / https://archive.startupdaily.net/?p=120328 / https://datacenterdynamics.com/en/news/blackstone-and-cpp-to-acquire-apac-data-center-firm-airtrunk-for-au24bn (T3*)
- [W7-06] Switch・CyrusOne・QTS: https://www.sec.gov/Archives/edgar/data/1848437/000110465924074337/tm2417925d1_ex99-2.htm(Cartica 8-K、FactSet 表、T3*) / https://www.sec.gov/Archives/edgar/data/1710583/000119312522200502/d387598ddefa14a.htm(Switch DEFA14A、T1*) / https://teiss.co.uk/news/digitalbridge-buys-data-center-company-switch-for-11-billion-10046 (T3*)
- [W7-07] キャップレート: https://www.datacentres.com/news/daily-market-update-slot2-2026-06-07 / https://www.datacentres.com/guides/sale-leaseback-data-centres / https://apers.app/learn/asset-classes/industrial/data-centers-power-pricing-pue-hyperscaler (T4*) / https://www.credaily.com/?p=219695 / https://www.datacenterdynamics.com/en/news/jll-data-center-demand-exceeds-expectations-doubles-year-over-year/ (T3*)
- [W7-08] CoreWeave 評価: https://www.marketscreener.com/quote/stock/COREWEAVE-INC-185380761/valuation/ / https://www.gurufocus.com/term/enterprise-value/CRWV / https://www.gurufocus.com/term/enterprise-value-to-ebitda/CRWV / https://stockanalysis.com/quote/tsx/CRWV/statistics/ (T4*) / https://seekingalpha.com/article/4788910-coreweave-just-changed-the-game / https://seekingalpha.com/news/4452505-coreweave-downgraded-by-barclays-to-equal-weight (T3*)
- [W7-09] Nebius 評価: https://www.sec.gov/Archives/edgar/data/0001513845/000110465926059872/tm2614392d1_ex99-2.htm(6-K、T1*) / https://www.tikr.com/blog/nbis-has-gained-167-in-2026-the-revenue-chart-explains-why / https://seekingalpha.com/article/4915974-nebius-the-road-to-400 / https://seekingalpha.com/article/4936102 (T3*) / https://in.marketscreener.com/quote/stock/NEBIUS-GROUP-8037501/valuation/ (T4*)
- [W7-10] CoreWeave 回収・契約: https://rittenhouseresearch.substack.com/p/coreweave-unit-economics-margin-profile (T4) / https://blockspace.media/insight/coreweave-a100-contract-challenges-gpu-depreciation-model/ / https://letsdatascience.com/news/coreweave-secures-nvidia-a100-contract-through-2029-b3a23ed2 (T3*)
- [W7-11] GPU 単価・単位経済: https://www.k-dense.ai/use-cases/coreweave-vc-due-diligence / https://www.cloudzero.com/blog/coreweave-pricing/ / https://deploybase.ai/articles/nebius-gpu-cloud-pricing-complete-guide-vs-hr-for-every-gpu / https://www.spheron.network/blog/coreweave-vs-nebius-h100-and-h200-pricing-2026/ (T4*)
- [W7-12] ルール・オブ・40: https://aventis-advisors.com/rule-of-40-in-saas-2026/ / https://theses-dissertations.princeton.edu/entities/publication/8958c795-8b22-4aa6-80b9-837f2dc205a1/full (T3*) / https://tickerleague.com/learn/rule-of-40-explained (T4*)
- [W7-13] Amazon SOTP: https://finance.yahoo.com/news/bank-america-resets-amazon-stock-043300969.html / https://www.webull.co.th/en/news-detail/14190908598600704 / https://www.tikr.com/blog/amazons-aws-hit-37-6-billion-in-q1-2026-heres-what-that-means-for-2027 (T3*)
- [W7-14] Google Cloud: https://www.insidermonkey.com/news/how-much-must-google-cloud-be-worth-to-justify-alphabets-valuation-1847253/ (T3*) / https://docs.google.com/document/d/1PX4FIrb1a4nBeKj3L7HanoYBfG6hSwOS/export?format=pdf (T4*) / https://www.tikr.com/blog/alphabet-stock-hits-109-9b-in-q1-revenue-as-cloud-tops-20b-for-first-time (T3*)
- [W7-15] Azure: https://www.tikr.com/blog/microsoft-stock-was-down-19-before-azure-hit-100-billion-the-ai-bet-is-paying-off / https://letsdatascience.com/news/microsoft-stock-price-forecasts-target-2026-2027-2030-7a3a92f6 (T3*) / https://deepresearchglobal.substack.com/p/microsoft-msft-fundamental-analysis-report (T4*、倍率の記載なし)
- [W7-16] 回収期間・GPU 第二の人生: https://www.sec.gov/Archives/edgar/data/1769628/000119312525052207/d899798ds1a.htm(CoreWeave S-1/A、T1*) / https://cloudedjudgement.substack.com/p/clouded-judgement-52926-the-second(見出しのみ、T3*) / https://moduledge.com/blog/neocloud (T4*)
- [W7-17] セクター別倍率: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/vebitda.html (T3*) / https://ibinterviewquestions.com/guides/energy-investment-banking/energy-public-market-multiples-2026 / https://interfinancial.com.au/wp-content/uploads/2026/04/InterFinancial-Dashboard_TMT_April_2026.pdf (T4*)
- [W7-18] AWS の EV/EBIT 検索: https://blog.mexc.com/?p=330523 (T4*) / https://www.tikr.com/blog/amzn-how-to-value-amazon-stock-why-a-sum-of-the-parts-approach-is-the-only-honest-way (T3*)
- [W7-19] Clouded Judgement と中央値: https://cloudedjudgement.substack.com/p/clouded-judgement-13026-software / https://cloudedjudgement.substack.com/p/clouded-judgement-122625-exuberance (T3*) / https://valueaddvc.com/blog/ntm-revenue-vs-arr-which-saas-multiple-matters-more-for-valuation / https://valueaddvc.com/blog/saas-comps-guide-how-to-find-and-use-public-saas-comparables-for-valuation (T4*)
- [W7-20] ルール・オブ・40 の限界: https://vectorshift.ai/glossary/rule-of-40 / https://www.cloudzero.com/blog/rule-of-40/ / https://escalon.services/blog/finance/the-saas-rule-of-40-what-it-means-and-how-to-achieve-it / https://en.wikipedia.org/wiki/Rule_of_40 (T4*)
- [W7-21] タワー・ミッドストリーム: https://www.sec.gov/Archives/edgar/data/0001053507/000105350726000131/pressreleaseq22026.htm(AMT 8-K、T1*) / https://www.opencapital.sh/stocks/amt/metrics/ev_to_ebitda / https://www.opencapital.sh/stocks/cci/metrics/ev_to_ebitda / https://www.opencapital.sh/stocks/kmi/metrics/ev_to_ebitda / https://www.opencapital.sh/stocks/epd/metrics/ev_to_ebitda / https://ycharts.com/companies/EPD/ev_ebitda (T4*)
- [W7-22] CoreWeave Q2 2026: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Second-Quarter-2026-Results/ (T1*) / https://www.marketbeat.com/instant-alerts/coreweave-q2-earnings-call-highlights-2026-08-11/ / https://longyield.substack.com/p/coreweave-books-104-billion-it-also (T3*/T4*)
- [W7-23] Nebius Q2 2026: https://quartr.com/events/nebius-group-n-v-nbis-q2-2026_ozKEzQzr / https://www.storagenewsletter.com/?p=304756 / https://w.media/nebius-group-revenue-surges-on-the-back-of-ai-cloud-business-growth/ / https://www.webull.com/news/15394228445193216 (T3*)
- [W7-24] DC 取引の 25〜30x 検索: datacentres.com の同一記事群(§W7-03 と同じ URL 群、T4*)
- [W7-25] DLR・EQIX: https://seekingalpha.com/article/4852707-ditch-digital-realty-for-equinix (T3*) / https://vcpscanner.com/stock/eqix / https://www.opencapital.sh/stocks/dlr/metrics/ev_to_ebitda / https://www.opencapital.sh/stocks/eqix/metrics/ev_to_ebitda / https://www.fool.com/coverage/better-buy/2026/07/15/digital-realty-trust-vs-equinix-which-real-estate-stock-is-a-better-buy-in-2026/ (T4*/T3*)
- [W7-26] Alphabet の目標株価・受注残: https://www.tikr.com/blog/jp-morgan-named-alphabet-its-top-pick-for-2026-heres-what-the-460-target-means-for-investors / https://finance.yahoo.com/markets/stocks/articles/analysts-love-alphabet-stock-just-151528287.html / https://www.tikr.com/de/blog/google-cloud-just-crossed-462-billion-in-backlog-heres-what-it-means-for-googl (T3*)
