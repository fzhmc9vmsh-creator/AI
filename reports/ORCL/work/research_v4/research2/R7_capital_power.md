# R7: AI データセンター事業の「資本コスト・建設速度・電力確保・利益率」— Oracle 対 ハイパースケーラー 対 ネオクラウド

- 作成日: 2026-10-12 / 対象: Oracle(NYSE: ORCL、決算期末 5/31。最新の報告済み四半期は Q1 FY2027 = 2026-06〜08 月期、2026-09-10 発表)、Microsoft・AWS・Google・Meta、CoreWeave(CRWV)・Nebius(NBIS)・Crusoe
- 目的: 事実・数値・出典の整理と、出典間の食い違いの指摘。**投資判断(買い・売り)は含まない。**
- 取得手段: WebSearch のみ。**24 回を使い切った**(すべて mode "standard"、"extended" は 0 回)。WebFetch は使えず、**会社の原文(プレスリリース、10-Q、株主レター、目論見書)は 1 件も直接開いていない**。数値はすべて検索ツールの要約に書かれていた内容である。
- 表記: 「欠損」= 見つからなかった。「(算出)」= 調査者の計算(式を併記)。「*」= 会社の一次書類・公式ページだが検索要約経由でしか見ておらず、原典確認が必要(Tier 3 相当として扱うこと)。
- Tier: 1 = 会社開示・決算説明会、2 = 規制当局・格付会社・公的統計、3 = 報道・アナリスト・調査会社、4 = ブログ・SNS・販促ページ・データ集約サイト。
- 出典 ID: `[R7-xx]` は本書 8 節の一覧(今回の 24 回の検索)。`[既S1]` `[既S2]` `[既S3]` `[既S4]` は `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research/` の既存調査、`[既R2]` `[既R5]` は `.../orcl/research2/R2_products_5w1h.md` `R5_credit.md`、`[既H3]` `[既H4]` は `.../orcl/data/` の H3_*・H4_* ファイル。既存の数値は再調査せず引用に留めた。
- 重複回避: Oracle の格付・CDS・満期ラダー・平均調達金利は [既R5] に詳しいため、本書では新発債の条件と競合との比較に絞った。

---

## 0. 先に知っておくべき要約(12 項目。評価・推奨は含まない)

1. **新発債のスプレッド(Oracle 対 Alphabet、2026 年 2 月)**: Oracle の 2026-02-02 発行の 10 年債は国債 +145bp(利回り 5.729%)、40 年債(2066 年)は +195bp(同 6.864%)。Alphabet の 2026-02 の 10 年債は +63bp(クーポン 4.800%)、40 年債の最終は +95bp。差は 10 年で 82bp、40 年で 100bp(算出)。いずれも単独の Tier 3〜4 の出典。
2. **Oracle の二次市場**: 2031 年債(クーポン 4.95%)は発行時 +115bp・利回り 4.988% だったが、2026-08 初めの分析では利回り 6.23%・国債比 約 +180bp(算出: スプレッドは +65bp 拡大、利回りは +124bp 上昇)。この分析は、Oracle を除く他の 4 ハイパースケーラーのスプレッドは「AA 格の指数以下」と述べる。
3. **CoreWeave の無担保高利回り債**: 2026-04 に 9.750% 2031 年債 $1.75B(額面発行)、2026-06 に 9.625% 2032 年債 $1.25B と 8.500% ユーロ建 2032 年債 €2B。同じ 2031 年満期の Oracle 債(新発利回り 4.988%)とのクーポン差は約 4.8pp(算出: 9.750 − 4.988)。日付と基準国債が異なるため概算。
4. **CoreWeave の担保付き(GPU 担保・遅延引出し)ローン**: DDTL 4.0(2026-03-31 完了、$8.5B)は変動 SOFR+2.25%・固定 約 5.9%、Moody's A3・DBRS A(low) の「投資適格の GPU 担保融資」。無担保債(9.6〜9.75%)と約 3.7〜3.9pp の差(算出)。
5. **転換社債**: CoreWeave 1.75%(2032、$3.5B)・2.875%(2033、$3.7B、2026-09)。Nebius 1.250%(2031)・2.625%(2033)(2026-03、$4.0B 上振れ)、0.50%(2030)・4.50%(2034)(2026-08、$5.0B 上振れ、グリーンシュー後 約 $5.75B)。Oracle の強制転換優先株は配当 6.50%($5B、[既H3])。
6. **電力(確保)**: CoreWeave 稼働 1.5GW・契約済み 3.7GW(2026-06-30、8-K 要約)。Nebius は契約電力の年末目標を 5GW に引き上げ(従来 >4GW)。Oracle は「今後 3 年(FY2029 まで)で 10GW の電力を確保」(会社発言の要約)。AWS は直近 12 か月で 3.8GW を稼働(日付不明の Jassy 発言)。
7. **稼働の速度**: Oracle は Q1 FY27(2026-06〜08)に約 850MW・30 万 GPU 超を納入(共同 CEO 発言、報道)。これは FY26 通期の約 73%(850 ÷ 0.73 = 約 1,164MW、算出。[既H4] の FY26 1.2GW と整合)。CoreWeave は Q2 2026 に稼働電力を約 500MW 追加。Abilene(Crusoe/Oracle/OpenAI)は 2024-06 着工、2026-07 時点で IT 電力 421MW が稼働(Epoch AI)、建屋 7・8 の稼働見込みは 7 月から 11 月へ遅れ。
8. **利益率(CoreWeave、2026 Q2)**: 売上 $2,575M、調整後 EBITDA $1,510M(58.6%、会社は 59%)、調整後営業利益 $128M(5.0%)、GAAP 営業損失 $49M(−1.9%)、純損失 $626M、純支払利息 $640M(売上の 24.9%、調整後 EBITDA の 42.4%。算出)。
9. **利益率(Nebius、2026 Q2)**: 売上 $582.3M、調整後 EBITDA $236.2M(40.6%)、AI クラウド部門の EBITDA 率 49.7%、純損失(継続事業)$190.4M。営業利益率と売上総利益率は**欠損**。
10. **クラウドの営業利益率(2026 年 4〜6 月期)**: AWS 39.4%(営業利益 $16.6B ÷ 売上 $42.2B)、Google Cloud 35.6%($8.8B ÷ $24.8B)。Microsoft の Azure 単独の営業利益率は公表値が見つからず、Intelligent Cloud の営業利益も欠損。Oracle の AI 容量の粗利率は Q3 FY26 の 32% が最後の数値(Q4 FY26・Q1 FY27 は欠損)。
11. **単位経済(参考値、定義が揃わない)**: CoreWeave の受注残 $104B ÷ 契約電力 3.7GW = $28.1B/GW(算出)。Nebius の大型 4 案件の年間契約額は 1MW あたり $20〜25M(株主レターの要約)。Oracle の OpenAI 契約の推計は年 $13.3M/MW(約 $300B ÷ 5 年 ÷ 4.5GW、[既R2])。会社の例示は 6 年・1GW・$60B(年 $10M/MW)で粗利率約 35%([既S1][既S4])。
12. **顧客集中**: CoreWeave の最大顧客は 2025 年に売上の約 67%(Microsoft とする二次情報)、2026 Q1 に 45%、Q2 に 36%(第 2 位 26%、第 3 位 10%)と低下。2026 年の 10-Q では顧客名が匿名で、Microsoft・OpenAI・Meta への割り当ては**確認できない**。Nebius は Microsoft と Meta で契約額の約 8 割(算出元は Zacks の「約 $32B ÷ $40B」)。Oracle は OpenAI が RPO の約 45%〜50% 超([既S2])。

---

## 1. 比較の前提と注意(先に読むこと)

1. **データの日付**: CoreWeave は 2026 Q2(6/30 終了、8/11 発表)、Nebius は 2026 Q2(6/30 終了、8/12 発表)、AWS・Alphabet は 2026 Q2(6/30 終了、7 月下旬発表)、Microsoft は FY2026 Q4(6/30 終了、7/29 発表)、Oracle は FY2027 Q1(8/31 終了、9/10 発表)。**Oracle だけが 2 か月ずれる**。2026 年 7〜9 月期(カレンダー Q3)の結果は 10/12 時点でまだ出ていない。
2. **定義の違い**: (a)「電力」は施設電力(PUE を含む)と IT 電力で意味が違い、出典は区別しないことが多い。(b)「契約電力」は電力会社・用地との契約で、顧客契約とは別物。(c) Oracle の RPO はクラウド・ソフトウェアを含む全社値で、CoreWeave の受注残は計算容量の契約のみ。(d) 粗利率の原価に減価償却を含めるかが会社ごとに違う(4-2 節)。
3. **「発行時」と「現在」の区別**: 新発債の利回り・スプレッドは発行日の値で、市場の現在値ではない。米国債の水準が 2026 年に大きく変動した([既R5] は 10 年債 5.34% を記載)ため、利回りの比較は必ずスプレッドと併せて見ること。
4. **検索要約の性質**: 1 回の要約は複数サイトの統合で、数値がどの URL 由来かを特定できない場合がある。その場合は出典を「URL 群」と書いた。

---

## 2. 資本コスト

### 2-1. 発行体別の調達条件(新発債・ローン・転換証券)

| 発行体 | 商品 | 日付 | 金額 | 条件(クーポン・スプレッド) | 満期 | 格付・担保 | 出典 | Tier |
|---|---|---|---|---|---|---|---|---|
| Oracle | 無担保シニア債 5 年(4.95% 2031) | 2026-02-02 | 欠損(8 トランシェ合計 $25.0B) | 利回り 4.988%、国債 3.700% 2031-01 に対し **+115bp** | 2031 | BBB(Fitch)/Baa2(Moody's)/ S&P は 2026-07-09 に BBB− へ | [R7-35][既R5] | 4(スプレッド)/ 3 |
| Oracle | 同 10 年(5.70% 2036) | 2026-02-02 | 欠損 | 発行利回り 5.729%、国債 4.000% 2035-11 に対し **+145bp** | 2036 | 同上 | [R7-35] | 4 |
| Oracle | 同 20 年(6.55% 2046) | 2026-02-02 | 欠損 | 発行利回り 6.558%、国債 4.625% 2045-11 に対し **+170bp** | 2046 | 同上 | [R7-35] | 4 |
| Oracle | 同 40 年(6.85% 2066) | 2026-02-02 | 欠損 | 発行利回り 6.864%、国債 4.750% 2055-08 に対し **+195bp** | 2066 | 同上 | [R7-35] | 4 |
| Oracle | 同 3 年変動 | 2026-02 | $0.5B | Compounded SOFR + 1.11% | 2029 | 同上 | [既R5] | 3 |
| Oracle | 同 3 年固定(4.550%) | 2026-02 | $3.0B | クーポン 4.550%(スプレッドは欠損) | 2029-02-04 | 同上 | [既R5] | 1* |
| Oracle | 強制転換優先株 Series D | 2026-02 | $5.0B | 配当 6.50% | 〜2029 転換 | — | [既H3] | 1 |
| Oracle | 40 年債(前回、参考) | 2025-09-24 | $18.0B(6 トランシェ) | 40 年が T+137bp(当初想定 T+165bp) | 最大 40 年 | — | [既H3] | 3 |
| CoreWeave | 無担保シニア債 | 2026-04 | $1.75B(上振れ) | **9.750%**、額面発行 | 2031 | 発行体格付は**欠損** | [R7-14] | 1* |
| CoreWeave | 無担保シニア債(米ドル) | 2026-06 | $1.25B | **9.625%** | 2032 | 同上 | [R7-15] | 1* |
| CoreWeave | 無担保シニア債(ユーロ) | 2026-06 | €2.0B | **8.500%** | 2032-07-15 | 同上 | [R7-15] | 1* |
| CoreWeave | 転換社債 | 2026-04 | $3.5B(上振れ) | **1.75%** | 2032 | — | [R7-16] | 1* |
| CoreWeave | 転換社債 | 2026-09(決済 9/22) | $3.7B(上振れ、$3.0B から。追加購入権 $0.5B) | **2.875%**、利払いは 2027-04-01 開始 | 2033 | — | [R7-17] | 1* |
| CoreWeave | DDTL 4.0(GPU 担保、遅延引出しタームローン) | 2026-03-31 完了 | $8.5B(初期 約 $7.5B、資産の稼働に応じ $8.5B まで) | 変動 **SOFR+2.25%** と固定 **約 5.9%** | 2032-03 | **Moody's A3、DBRS A(low)**。借り手は CoreWeave Compute Acquisition Co. VIII, LLC(同社の実質全資産が担保)。「投資適格格付けを得た初の GPU 担保融資」(会社) | [R7-18] | 1* |
| Nebius | 転換社債 | 2026-03 | $4.0B(上振れ)+ 2031 年債に $337.5M の追加 | 2031 年債 **1.250%**($2.25B)、2033 年債 **2.625%**($1.75B) | 2031・2033 | — | [R7-25] | 1* |
| Nebius | 転換社債 | 2026-08 | $5.0B(上振れ)、グリーンシュー行使で 約 $5.75B | 2030 年債 **0.50%**($3.0B + $450M)、2034 年債 **4.50%**($2.0B + $300M) | 2030・2034 | — | [R7-25] | 1* |
| Nebius | 資産担保ファシリティ | 2026-07 | $775M | **SOFR+2.5%** | 欠損 | — | [R7-22 ほか URL 群] | 3〜4 |
| Alphabet | 米ドル建て債(7 トランシェ) | 2026-02(記事日 2/17) | $20B(目標 $15B から上振れ) | 10 年 **T+63bp**(クーポン 4.800%)、3 年 +27bp(別の記述)、40 年は当初 約 +120bp から最終 **+95bp** | 3〜40 年 | 高格付(要約は Microsoft を S&P AAA と記載。Alphabet 個別の格付は欠損) | [R7-34] | 3〜4 |
| Alphabet | ポンド建て 100 年債 | 2026-02 | 欠損 | ギルト比 **+120bp**(国債スプレッドではない) | 2126 | — | [R7-36] | 3 |
| Alphabet | 米ドル建て債(10 トランシェ) | 2026-08 | $25B | 40 年を 約 +155bp から **+130bp** に縮小。受注ピーク 約 $115B(約 4.6 倍)。**単一ブログ** | 2〜40 年 | — | [R7-34] | 4 |
| Meta | 米ドル建て債(最大 6 トランシェ) | 2026-04-30 | $20〜25B(予定) | 2066 年債の初回価格目安は国債 **+最大 180bp**。**最終スプレッドは欠損** | 〜2066 | — | [R7-34] | 3 |
| Meta | 米ドル建て債(前回、参考) | 2025-10 | 最大 6 トランシェ | 40 年は国債 約 +140bp の見込み(最終は欠損) | 5〜40 年 | — | [R7-34] | 3 |
| Amazon | 米ドル・ユーロ建て債 | 2026-03 | 約 $54B | トランシェ別の条件は**欠損** | 欠損 | — | [R7-34] | 3 |
| Microsoft | 社債 | — | — | 2026 年の発行は今回の検索で**確認できず**(S&P は AAA と要約に記載) | — | AAA(S&P、要約) | [R7-36] | 3 |

### 2-2. Oracle 対 ハイパースケーラー: 新発債スプレッドの並置

| 年限 | Oracle(2026-02-02) | Alphabet(2026-02) | 差(算出) | 備考 |
|---|---|---|---|---|
| 3 年 | 変動 SOFR+111bp(固定 4.550%、国債比は欠損) | +27bp(別の記述) | 比較不可(固定と変動の別) | Alphabet の +27bp は単一の要約 |
| 5 年 | +115bp(2031 年債) | 欠損 | — | |
| 10 年 | +145bp(利回り 5.729%) | +63bp(クーポン 4.800%) | **+82bp**(145 − 63) | 国債の水準が違う(Oracle のベンチマークは 4.000% 2035-11)ため利回りは直接比較できない |
| 20 年 | +170bp | 欠損 | — | |
| 40 年 | +195bp(利回り 6.864%) | +95bp(最終) | **+100bp**(195 − 95) | Meta の 2066 年債(2026-04)は初回目安が最大 +180bp。最終値は欠損 |

- 注: 発行日は Oracle が 2026-02-02、Alphabet が 2026-02 中旬(記事日 2026-02-17)で、数日〜2 週間の差がある。市場環境の変化は除けていない。
- 二次市場: Oracle の 2031 年債は 2026-08 初めに利回り 6.23%・国債比 約 +180bp([R7-36]、Tier 3)。発行時の +115bp からの拡大は +65bp(算出: 180 − 115)。2031 年債が同一銘柄かは未確認(両者とも 2031-02 満期とみられるが、要約は銘柄コードを示さない)。同じ分析は、Oracle を除く 4 ハイパースケーラーのスプレッドは 2025 年初から「AA 格の指数と同等かそれ以下」で比較的横ばい、と述べる。
- Oracle の 2051 年債は 2026-09-25 に利回り 7.65%・国債比 +213bp([既R5]、Tier 4)。Alphabet の 40 年債は 2026-08 に +130bp(単一ブログ)。年限・日付が違うため、現在値の直接比較は不可。
- Oracle の財務指標との並置(事実のみ): Oracle の負債資本倍率は約 4 倍、他の 4 社は 0.18〜0.51 倍([R7-36]、Tier 3)。オフバランス債務を含めると Meta は 0.36 倍から 2.08 倍に上がり、Alphabet・Microsoft・Amazon は約 1.0 倍([R7-36])。

### 2-3. CoreWeave・Nebius の金利負担

| 項目 | CoreWeave(2026 Q2) | Nebius(2026 Q2) | Oracle(参考) |
|---|---|---|---|
| 純支払利息 | **$640M**(前年同期 $267M)。Q3 の会社ガイダンスは $860〜940M | 欠損(今回の検索で見つからず) | FY26 $4,599M、Q1 FY27 $1,428M([既R5]) |
| 売上に対する利息 | 640 ÷ 2,575 = **24.9%**(算出)。Q3 は 860 ÷ 3,450 = 24.9% から 940 ÷ 3,600 = 26.1%(算出) | 欠損 | FY26 4,599 ÷ 67,400 = 6.8%(算出。売上は [既H1]) |
| 調整後 EBITDA に対する利息 | 640 ÷ 1,510 = **42.4%**(算出)。EBITDA ÷ 純支払利息 = 2.36 倍(算出) | 欠損 | FY26 EBITDA ÷ 支払利息 6.5 倍([既R5] 算出) |
| 総債務 | **欠損**(10-Q 未読) | 欠損 | $125.3B(2026-08-31、[既H3]) |
| 手元現金 | 欠損 | 約 $8B(2026-06-30、要約) | $37.1B(2026-08-31) |
| 出典 | [R7-01][R7-05][R7-08] | [R7-22] | [既R5] |

- 解釈上の注意(事実の整理): CoreWeave の資金調達コストは、(a) 無担保債 8.5〜9.75%、(b) GPU 担保ローン SOFR+2.25% または固定 約 5.9%、(c) 転換社債 1.75〜2.875%、の 3 層に分かれる。担保付きローンの A3 格付けは「借り手の SPV の資産と顧客契約」に対するもので、CoreWeave 社自体の格付けではない。
- DDTL 4.0 が特定顧客(Meta)の契約に紐づくかは**確認できない**。プレスリリースは「先端 AI 企業との既契約のクラウドサービス提供のための資金」と書き顧客名を出さない。Meta を主幹と書くのは 1 件のブログ([R7-19]、Tier 4)のみで、アンカー投資家は Blackstone との報道が 1 件ある。
- Oracle 関連のプロジェクト融資(既存、再掲): Vantage の Port Washington(WI)$38B は初回価格が「基準金利 +約 2.5pp」(JPMorgan・MUFG 主幹、報道、[既H3])。Stack の Project Jupiter(NM)$18B のローンが額面 89〜91 セントで取引と報じられた(Tier 4、[既H3])。これらは Oracle 本体ではなく開発者側 SPV の借入で、Oracle はテナント(報道)。担保付き GPU ローン(SOFR+2.25%)とは対象資産が違う(建物・土地 対 GPU)。

---

## 3. 電力・容量・建設期間

### 3-1. 確保・契約済み電力と稼働容量

| 会社 | 稼働(運用中)容量 | 確保・契約済み容量 | 時点 | 出典 | Tier |
|---|---|---|---|---|---|
| **Oracle** | Q1 FY27(2026-06〜08)に約 **850MW**・30 万 GPU 超を「納入」(共同 CEO Magouyrk: 「Q4 の約 3 倍、前年度に納入した総容量の 73%」)。FY26 通期の納入は 1.2GW([既H4])。Q3 FY26 は 400MW([既H4]) | 「FY2029 までの 3 年間で **10GW** の電力を確保」(会社発言の要約)。Bloom Energy の燃料電池は初期 1.2GW・最大 2.8GW([既H4])。Stargate 関連サイトの合計 約 8.1GW(Abilene+Shackelford 3.2GW、Doña Ana 2.2GW、Port Washington 1.3GW、Saline 1.4GW。1 件の分析) | 2026-09-10 | [R7-37][既H4][既S3] | 3(原典 1*) |
| **CoreWeave** | **1.5GW**(アクティブ電力。Q2 に 約 500MW 追加)。年末目標 >1.85GW(従来 1.7GW) | 契約電力 **3.7GW**(8-K 要約)。四半期末以降で 約 4.2GW とする二次報道あり(8-K でなく二次) | 2026-06-30 | [R7-02][R7-04] | 1*/3 |
| **Nebius** | 接続済み電力(connected)の最新値は**欠損**。目標は 2026 年末に 800MW〜1GW(Q4'25 の株主レター) | 契約電力の年末目標 **5GW**(従来 >4GW)。推移: >2.5GW(2025-11)→ >3GW(2026-02)→ >4GW(2026-05)→ 5GW(現在)。2027 年から年 >1GW の稼働を計画 | 2026-08-12 | [R7-21][R7-22] | 1*/3 |
| **AWS** | 直近 12 か月で **3.8GW** を稼働、さらに 4Q に 1GW を追加予定(Jassy 発言。**発言日は未確認**。Q2 2026 の会議で再確認はできず)。総容量は 2027 年末までに倍増と発言(同上) | 全体の容量は欠損。Q2 2026 の会議では「2026 年も 2027 年も需要に容量が追いつかない」と発言 | 日付不明 / 2026-07-30 | [R7-33] | 3 |
| **Microsoft** | 欠損(GW 値なし)。FY26 の設備投資は $145B 超、FQ4 は $41B(前年比 +70%)で、約 3 分の 2 が短寿命資産(CPU・GPU) | 欠損。CEO は「AI 容量を今年 80% 超増やし、2 年でデータセンター全体を倍増」と発言(**発言は 10 月の決算会議とあるが年が未確認**) | 2026-07-29 | [R7-32][R7-39] | 3 |
| **Google** | 欠損(GW 値なし)。2026 年設備投資ガイダンス $195〜205B(Q1 時点 $180〜190B から上方修正)、Q2 単独 $44.9B | 欠損 | 2026-07 | [R7-31] | 3 |
| **Meta** | 欠損(今回の検索では取得できず) | 原子力事業者 3 社と計 **6GW 超**の電力契約(2026-01-09)。Constellation と 1.1GW・20 年(2027 年開始)の契約 | 2026-01 | [R7-39] | 3〜4 |
| **Crusoe** | Abilene(Oracle/OpenAI 向け): IT 電力 421MW 稼働(2026-07 時点)。2026 Q4 に 843MW の見込み(Epoch AI) | Abilene キャンパスは 1.2GW(計画)。Crusoe 全体の GW は**欠損**(検索せず) | 2026-07 | [R7-38][既S3] | 3 |
| 業界全体 | 欠損 | 2026 年の四半期累計(7 月時点)で容量追加 2,100MW(出版元は内訳なし)。上位 4 社(AWS・Microsoft・Google・Meta)で計画 MW の約 58%。変圧器の納期は 36 か月(従来 18〜24 か月) | 2026-07 | [R7-39] | 3〜4 |

- **Oracle の 850MW と CoreWeave の約 500MW は直接比較できない**: Oracle の「納入」の定義(パートナーが建設した施設の引渡しを含むか、顧客に課金開始か)は未確認。CoreWeave の「アクティブ電力」は顧客に提供可能な電力(施設ベースか IT ベースかは不明)。
- Oracle の既存データとの整合: 「FY27 Q1 に 1GW の稼働予定」([既H4]、予定値)に対し、実績の納入は約 850MW。**予定の約 85%**(算出: 850 ÷ 1,000)。ただし 1GW 予定の定義(稼働か納入か)が未確認。
- 計算: Oracle の FY26 の納入容量 = 850 ÷ 0.73 = 約 1,164MW(算出)で、[既H4] の 1.2GW と整合。Q4 FY26 の納入 = 850 ÷ 約 3 = 約 283MW(算出、「約 3 倍」の言葉に基づく概算)。

### 3-2. 建設期間(着工から稼働まで)の事例

| 事例 | 着工 | 稼働・到達点 | 経過期間 | 遅延・備考 | 出典 | Tier |
|---|---|---|---|---|---|---|
| **Abilene(Crusoe/Oracle/OpenAI、TX)** | 2024-06 | 第 1 期(2 棟、IT 200MW 超)は 2025 年前半に通電する計画だった。2026-07 時点で IT 電力 **421MW** が稼働(Epoch AI)。2026 Q4 に 843MW の見込み | 2024-06 → 2026-07 = **25 か月**で 421MW(算出)。全 8 棟(1.2GW)は当初 2026 年中頃を目標だったが、地元報道では工事が **2027 年初めまで**続く(約 31 か月以上。算出: 2024-06 → 2027-01) | 建屋 7・8 の稼働見込みを 7 月から 11 月へ後ろ倒し(Epoch)。「1.2GW」は施設の計画値、「421MW」は IT 電力で、基準が違う | [R7-38][既S3] | 3 |
| Project Jupiter(Doña Ana、NM、Oracle がテナント、Stack 開発) | 欠損 | 当初は 2026 Q4 に初期稼働と報道 → 現在は **2028 年開業**が目標 | 欠損 | 2026-09 に Oracle が開発者へ不可抗力(force majeure)通知(電力供給の遅れ、報道)。Oracle は「スケジュールは維持」と説明 | [既S3][既H3] | 3 |
| Shackelford(Frontier、TX、Vantage、IT 1.4GW) | 欠損 | 1 棟目は 2026 年後半。全体は 2028 Q4(Epoch)〜 2029 年(Baxtel) | 欠損 | 敷地内ガスで稼働し、パイプライン遅延に備えガスをトラック輸送(Bloomberg 2026-10-08) | [既S3] | 3 |
| Port Washington(WI、Vantage) | 欠損 | 完成は 2028 年(報道) | 欠損 | 2026 年の進捗更新は見つからず | [既S3] | 3 |
| xAI Colossus 2 | 欠損 | 「12 か月で建設」と xAI が予定(Epoch AI の要約) | 12 か月(予定値、実績は欠損) | 実績は未確認 | [R7-38] | 3 |
| Epoch AI の追跡対象全体 | — | 着工から施設電力 1GW 到達まで **約 1〜3.6 年** | 12〜43 か月 | 本書の事例に限らない一般的な範囲 | [R7-38] | 3 |
| CoreWeave | — | 1 四半期で 約 500MW のアクティブ電力を追加(2026 Q2)= 約 5.5MW/日(算出: 500 ÷ 91 日)。個別サイトの着工〜稼働は**欠損** | — | 設備投資 $9.4B(Q2)。電力追加と設備投資の時期はずれる | [R7-02][R7-03] | 1*/3 |
| Oracle(全体) | — | 1 四半期で 約 850MW を納入(2026 Q1 FY27)= 約 9.2MW/日(算出: 850 ÷ 92 日) | — | 「納入」の定義は未確認(上の注記) | [R7-37] | 3 |
| Nebius | 欠損 | 欠損 | 欠損 | サイト別の着工〜稼働の事例は検索せず | — | — |
| Microsoft(Fairwater)・Meta(Prometheus、Hyperion) | 欠損 | 欠損 | 欠損 | 今回の検索では情報が出なかった | [R7-38] | — |

---

## 4. 利益率・単位経済

### 4-1. CoreWeave と Nebius の損益率(2026 年 Q2、単位: $M)

| 項目 | CoreWeave | Nebius | 出典 | Tier |
|---|---|---|---|---|
| 売上(前年同期) | 2,575(1,212)= +112% | 582.3(105.1)= +454% | [R7-01][R7-20] | 1* |
| 売上のうち AI クラウド | 全体 | 574.9(98%) | [R7-22][R7-23] | 3 |
| **調整後 EBITDA** | 1,510 | 236.2 | 同上 | 1* |
| **調整後 EBITDA 率** | **58.6%**(算出: 1,510 ÷ 2,575。会社は 59%、前年同期 62%) | **40.56%**(算出: 236.2 ÷ 582.3。会社・報道は約 41%、40.6%)。AI クラウド部門のみ **49.7%**(2025 Q4 は 24%)。差は Avride・TripleTen の初期投資と説明 | 同上 | 1*/3 |
| 調整後営業利益(率) | 128(**5.0%**、前年同期 200 = 16%) | 欠損 | [R7-01] | 1* |
| **GAAP 営業利益(率)** | **−49(−1.9%)**(前年同期 +19) | **欠損**(参考推計は下の注) | [R7-05] | 4 |
| 売上総利益率 | 欠損(会社は「売上総利益」を表示せず、cost of revenue と T&I を別行で表示)。参考値は 4-2 節 | **欠損** | — | — |
| 純損益 | −626(−24.3%、算出) | −190.4(継続事業、−32.7%、算出: 190.4 ÷ 582.3)。調整後純損益 −33.2 | [R7-01][R7-23][R7-24] | 1*/3 |
| 純支払利息 | 640 | 欠損 | [R7-01] | 1* |
| 減価償却費(D&A) | 約 1,382(算出: 調整後 EBITDA 1,510 − 調整後営業利益 128。両者の調整項目が同じと仮定) | 259.7 | [R7-01][R7-23] | 算出/3 |
| 株式報酬 | 欠損 | 102.5 | [R7-23] | 3 |
| 設備投資 | 9,400(Q2、要約) | 約 5,657〜5,700(Q2) | [R7-03][R7-22][R7-28] | 3 |
| 2026 年の会社ガイダンス | 売上 $12.4〜13.2B(要約) | 売上 $3.0〜3.4B、調整後 EBITDA 率 約 40%、設備投資 $20〜25B | [R7-04][R7-22] | 3 |
| 会社のランレート | — | 年換算 ARR $3.0B(6 月末。3 月末 $1.9B) | [R7-22] | 3 |

- **Nebius の営業利益率(参考推計、GAAP ではない)**: 調整後 EBITDA 236.2 − D&A 259.7 − 株式報酬 102.5 = −126.0、売上比 −21.6%(算出)。調整後 EBITDA がこの 2 項目以外も加算している場合は値が変わる。
- Nebius の純損失の前年同期値が出典で割れる(下の 6 節)。

### 4-2. CoreWeave の「売上総利益率」: 定義によって 7%〜66%

CoreWeave の 2026 Q2 の費用行(単位 $M、[R7-05] Beancount、Tier 4): 売上 2,575、cost of revenue 879、technology and infrastructure(T&I)1,507、GAAP 営業損失 −49。

| 定義 | 式 | 値 |
|---|---|---|
| (a) 売上 − cost of revenue のみ(減価償却の大半を含まない) | (2,575 − 879) ÷ 2,575 | **65.9%** |
| (b) さらに D&A 約 1,382 を原価に算入(D&A がすべて cost of revenue と T&I に含まれると仮定) | (2,575 − 879 − 1,382) ÷ 2,575 | **約 12.2%** |
| (c) さらに T&I 全額を原価に算入(人件費等を含むため下限の目安) | (2,575 − 879 − 1,507) ÷ 2,575 | **約 7.3%** |
| 参考: 暗黙の販管費等 | 2,575 − 879 − 1,507 − (−49) | 約 238(9.2%。他の費用科目がないと仮定) |

- 出典(Beancount)は「(a) の引き算は計算資産の減価償却の多くを含まず、真の総合粗利率ではない」と注記している。どの定義が Oracle の「AI 容量の粗利率 32%」と同じ原価範囲かは**確認できない**(Oracle が原価に減価償却・データセンターのリース費用を含める範囲の詳細は未確認、[既S4] 参照)。
- **Oracle の比較値(再掲)**: AI 容量の粗利率は Q3 FY26(2026-03-10 発表)に **32%**(ガイダンス 30%)。会社の長期レンジは 30〜40%、6 年・1GW・$60B の例示で通算 約 35%([既S1][既S4])。報道(The Information、2025-06〜08 の四半期)は Oracle の NVIDIA レンタルの粗利率を 14%(5 四半期平均 約 16%)と伝え、減価償却を全額反映するとさらに 約 7pt 低いとも報じた([既S3])。Q4 FY26・Q1 FY27 の AI 容量の粗利率の数値は**欠損**([既S4])。

### 4-3. ハイパースケーラーのクラウド事業の営業利益率

| 事業 | 期間 | 売上 | 営業利益 | 営業利益率 | 前年同期の率 | その他 | 出典 | Tier |
|---|---|---|---|---|---|---|---|---|
| **AWS** | 2026 Q2(4〜6 月) | $42.2B(+37%) | $16.6B(前年 $10.2B) | **39.4%**(算出: 16.6 ÷ 42.2 = 39.3%。報道は 39.4%) | 32.9% | 受注残 $496B。AWS は売上の 21.1% で全社営業利益の 60.5%。2026 年の設備投資は約 $220B(従来 $200B) | [R7-30][R7-33] | 1*/3 |
| **Google Cloud** | 2026 Q2 | $24.8B(+82%) | $8.8B | **35.6%**(算出: 8.8 ÷ 24.8 = 35.5%) | 20.7% | 受注残 $514B(Q1 は $462B)。Alphabet の Q2 設備投資 $44.9B、2026 年 $195〜205B。フリーキャッシュフロー −$5.9B | [R7-31] | 3 |
| **Microsoft(Azure)** | FY2026 Q4(4〜6 月) | Intelligent Cloud $39.3B(+32%)、Microsoft Cloud $59.3B(+27%) | **欠損**(Intelligent Cloud の営業利益は取得できず) | **Azure 単独の営業利益率は公表値が見つからず**(Microsoft が Azure 単独の営業利益を示していないとの調査者の理解だが、今回の出典では未確認)。Intelligent Cloud の率は欠損 | 欠損 | Azure の成長率は 43%(定率換算)とする報道と 41% とする見出しがある。設備投資 $41B(+70%) | [R7-32] | 3 |
| **Meta** | — | クラウド事業なし | — | — | — | 自社用 | — | — |
| **Oracle**(参考) | Q1 FY27 | 全社 | GAAP 営業利益率 **35%**(前年 29%)、非 GAAP 42% | 全社粗利率は低下中(FY26 通期で 約 5pt 低下、FY27 も低下見込み) | 29% | OCI 売上 +121%(Q1 FY27)。AI 容量の粗利率は 4-2 節 | [既S2][既S4] | 3 |

- 全社の営業利益率とクラウド部門の営業利益率は定義が違う。Oracle の全社営業利益率にはソフトウェア・サポート事業(粗利率 65〜80%、[既S1])が含まれ、AWS・Google Cloud のクラウド部門の率とは対応しない。
- EBITDA 率(参考): Oracle FY26 の EBITDA は $29.87B([既R5] 算出)、売上 $67.4B([既H1])で **44.3%**(算出: 29.87 ÷ 67.4)。CoreWeave の調整後 EBITDA 率 58.6%、Nebius の 40.6% とは、EBITDA の定義(調整項目)が違うため比較は参考扱い。

### 4-4. 単位経済(1MW・1GW あたり)— すべて参考値

| 項目 | 式・値 | 注意 | 出典 |
|---|---|---|---|
| **CoreWeave: 受注残 ÷ 契約電力** | 104,000 ÷ 3,700MW = **$28.1M/MW = $28.1B/GW**(算出)。四半期末以降の追加分と 4.2GW を使うと (104 + 25) ÷ 4.2 = $30.7B/GW(算出。$25B は「純増の新規コミット」で、4.2GW は二次報道) | 契約電力は電力会社・用地との契約で、顧客契約とは別。顧客未獲得の電力も含むため、分子と分母の時点・範囲が一致しない | [R7-01][R7-02] |
| CoreWeave: 受注残 ÷ アクティブ電力 | 104,000 ÷ 1,500MW = $69.3B/GW(算出) | 受注残は未稼働の容量分を含む。意味のある単価ではない(参考) | 同上 |
| CoreWeave: 売上 ÷ アクティブ電力(年換算) | 2,575 × 4 ÷ 1,500MW = **$6.9M/MW・年**(算出)。四半期の平均稼働を約 1.25GW(期末 1.5GW − 追加 約 0.5GW の半分)とすると $8.2M/MW・年(算出: 10,300 ÷ 1,250) | 期初の電力は「期末 − 約 500MW」から逆算した概算。電力は施設ベースかもしれない | [R7-01][R7-02] |
| CoreWeave: 設備投資 ÷ 追加電力 | 9,400 ÷ 500MW = $18.8M/MW(算出) | 設備投資は先行払い・前払いを含み、同じ四半期の追加電力とは対応しない。**粗い参考値** | [R7-03] |
| CoreWeave: 短期契約の単価 | 「Q3 の 3〜6 か月の短期契約は 約 $40M/MW」(CoreWeave IR 2026-09-17 の要約) | **単位が未確認**([既S3]・[既R2] も比較対象から除外) | [既S3] |
| **Nebius: 大型 4 案件の年間契約額** | 1MW あたり **$20〜25M**(株主レターの要約)。比較として「2026 年の容量全体では 約 $12M」とある | 4 案件の平均規模は $1B 超。「MW」が IT 電力か施設電力かは不明。「base of about $12M across its 2026 capacity」の意味は要約から曖昧 | [R7-21] |
| Nebius: RPO ÷ 契約電力(目標) | 37.5 ÷ 5GW = $7.5B/GW(算出) | 分母は用地・電力の確保で顧客契約と一致せず、**参考値にすら不適切**な可能性が高い | [R7-26][R7-22] |
| **Oracle: OpenAI 契約の年額** | 約 $300B ÷ 5 年 ÷ 4.5GW = **$13.3M/MW・年 = $13.3B/GW・年**(算出、[既R2]) | 総額は WSJ 報道、4.5GW は OpenAI が確認、総額は非開示。両者の対応は会社が確認していない | [既R2][既S2] |
| Oracle: 会社の例示 | 6 年・1GW・$60B = $10B/GW・年(**$10M/MW・年**)(算出)、粗利率 約 35% | 原価構成: 土地・DC・電力・人員 約 35%、計算・ネットワーク・ストレージ 約 65% | [既S1][既S4] |
| Oracle: RPO ÷ 確保電力 | 664 ÷ 10GW = $66.4B/GW(算出)。OpenAI のみなら 300 ÷ 4.5 = $66.7B/GW(算出) | RPO はクラウド・ソフトウェア全体で、10GW は将来 3 年の確保電力(顧客契約と一致しない)。CoreWeave の $28.1B/GW と**定義が違うため、差の大きさを解釈しない** | [R7-37][既R2] |

---

## 5. 顧客集中

### 5-1. CoreWeave

| 期間 | 最大顧客 | 第 2 位 | 第 3 位 | 備考 | 出典 | Tier |
|---|---|---|---|---|---|---|
| FY2025(通期) | 売上の **約 67%**(Microsoft とする二次情報。10-K で名指しとの記述が 1 件) | 欠損 | 欠損 | 複数の二次情報が 67% で一致 | [R7-09][R7-11] | 3〜4 |
| 2025 Q2(前年同期) | **71%**(「前年の 71% から 36% へ」とする二次情報) | 欠損 | 欠損 | 10-Q の確認なし | [R7-11] | 4 |
| 2026 Q1(3 月 31 日終了) | **45%** | 20%(TIKR の記述)。別の分析は Q2 の第 2 位を 26% とする。期間が違うため矛盾とは言えない | 欠損 | 匿名(Customer A 等) | [R7-09][R7-12] | 3 |
| 2026 Q2(6 月 30 日終了) | **36%** | **26%** | **10%**(上位 2 社で 62%。算出: 36 + 26。二次情報の「2 社で 62%」と一致) | 顧客名は 10-Q で匿名。別期間の同じ呼称が同一顧客とは限らない | [R7-09][R7-11] | 3〜4 |
| 契約(受注残の内訳ではない) | OpenAI: 総コミット **最大 約 $22.4B**(累計)。Meta: 当初 約 **$14.2B**(〜2031-12)、2026-03 に追加 約 **$21B**(〜2032-12)。10-Q 要約: 「2026 年 3 月に Meta は最大 約 $21B を支払うと当初コミットし、今後も重要な顧客になる」 | — | — | 受注残 $104B のうちの顧客別内訳は**欠損**。Microsoft の契約残高も欠損 | [R7-09][R7-10] | 1*/3 |
| 契約収益比率 | 2026 年上半期の売上の **98%** が確定契約から(sec-api.io の分析) | — | — | — | [R7-03] | 3 |

- 注: 5-1 節の 2025 Q2(71%)・2026 Q1(45%)・Q2(36%/26%/10%)の数値は、検索 5・21 の要約が複数の二次情報を統合しており、個別の URL を特定できない(R7-09・R7-11・R7-12 のいずれか、または複数)。10-Q 原文は未読。
- **「Microsoft・OpenAI・Meta の比率」は確認できない**: 2026 年の 10-Q の顧客は匿名で、名前と比率の対応は報道されていない。Meta の 2026-03 追加契約(約 $21B)と OpenAI の累計契約(約 $22.4B)から、Q2 の第 2・第 3 位に OpenAI や Meta が含まれる可能性はあるが**推測であり、出典では裏付けられない**。
- 受注残の上乗せ: 6 月末の $104B に含まれない「2026 Q3 初めの純増 $25B 超」が会社から開示されている([R7-01])。顧客名は書かれていない。

### 5-2. Nebius

| 項目 | 内容 | 出典 | Tier |
|---|---|---|---|
| Microsoft 契約 | 最大 **約 $17.4B〜19.4B**(5 年。別の記事は $17.3B〜19.4B)。2027 年から年間のフルランレート寄与の見込み | [R7-26][R7-27] | 3 |
| Meta 契約 | 2025 年 Q3 の当初契約 約 **$3B**(5 年)。2026-03 に **$27B・5 年**の AI インフラ契約とする報道。2026 Q1 に Meta の $12B の発注とする記述も(同じ契約の一部か別かは不明) | [R7-26][R7-27] | 3 |
| 契約額の集中 | Microsoft と Meta で 約 **$32B**(確定額)= 契約収益 約 $40B の **約 8 割**(Zacks)。「最大」の金額を全部足すと約 $49B(Investing.com の見出し) | [R7-26][R7-27] | 3 |
| RPO | 2026 年 3 月末 約 $34B → 6 月末 約 **$37.5B**。今後 2 年で売上化されるのは約 36% | [R7-26] | 3 |
| 売上に対する顧客別比率 | **欠損**(Microsoft の売上比率の記載を見つけられず) | — | — |
| Q2 の新規契約 | 大型 4 件(平均 $1B 超): Reflection、Cohere、米国の AI ラボ 1 社、クオンツ運用会社 1 社(Microsoft・Meta の名は要約に出ない) | [R7-22] | 3 |
| 前払い | 案件の約 70% で一部前払い。前払いが設備投資の 50〜60% を賄う(要約)。Q2 設備投資 $5.7B に対し前払いが約 60% とする見出しがある | 検索 4 の結果群(Webull 等。個別 URL 特定不可) | 3〜4 |

- 算出: Microsoft と Meta の確定額 $32B ÷ RPO $37.5B = 85.3%(算出)。Zacks の「$32B ÷ $40B = 80%」とは分母が違う(RPO と契約収益)。

### 5-3. Oracle(再掲、新規調査なし)

- OpenAI は RPO の **約 45%**(算出: 約 $300B ÷ $664B = 45.2%)。S&P は $638B のほぼ半分と推定、BofA は 2026 年 6 月時点で RPO $638B の 50% 超と推定([既S2])。
- 他の主要顧客: Meta・xAI・NVIDIA・AMD など(契約額は未取得、[既S3] の欠損一覧に記載)。

### 5-4. 並置(事実のみ)

| 会社 | 最大顧客の比率 | 基準 | 備考 |
|---|---|---|---|
| Oracle | OpenAI 約 45%〜50% 超 | RPO($664B) | 売上ではなく受注残 |
| CoreWeave | 36%(2026 Q2)、第 2 位 26% | 四半期売上 | 受注残の顧客別内訳は欠損。名前は匿名 |
| Nebius | Microsoft+Meta で 約 80〜85% | 契約額・RPO | 売上比率は欠損 |

基準が違う(受注残 対 売上)ため、数値の大小を直接比べることはできない。

---

## 6. 出典間の食い違い(どちらかを採らず併記)

| # | 項目 | 値 A | 値 B | 備考 |
|---|---|---|---|---|
| 1 | CoreWeave の契約電力 | 3.7GW(2026-06-30、8-K 要約) | 約 4.2GW(四半期末以降、二次報道) | 時点が違う可能性が高いが確認なし |
| 2 | CoreWeave の最大顧客比率 | 2026 Q2 は 36%(前年 71%) | Q1 は 45%、第 2 位は TIKR が 20%、別の分析が Q2 で 26% | 期間が違う。顧客名は匿名で同一顧客か不明 |
| 3 | CoreWeave の「2 社で 62%」 | 上位 2 社の合計(36 + 26 = 62) | 通期・半期の値とする解釈の余地 | 算出で四半期の上位 2 社と一致 |
| 4 | CoreWeave の DDTL 4.0 の顧客 | プレスリリースは顧客名なし | 1 件のブログが「Meta 主幹」と記述。別の報道は Blackstone がアンカー | Meta 紐づけは**未確認** |
| 5 | CoreWeave の年末目標(アクティブ電力) | >1.85GW(現行) | 1.7GW(従来) | 引き上げ後の値。日付は 2026-08 の会議 |
| 6 | Nebius の Meta 契約額 | 当初 約 $3B | 2026-03 に $27B(報道)/ 2026 Q1 に $12B の発注(記述) | 同一契約の拡張か別契約か未確認 |
| 7 | Nebius の Microsoft 契約額 | $17.4B〜19.4B | $17.3B〜19.4B | 下限が 0.1 異なる |
| 8 | Nebius の前年同期の純損益 | 純利益 $502.5M(継続事業) | 純利益 $584.4M(RTTNews) | 継続事業と全体の違いか、理由は未確認 |
| 9 | Nebius の調整後 EBITDA 率 | 40.6% | 41% | 丸め |
| 10 | Nebius の設備投資 | 約 $5.7B | $5,657.4M(sec-api の要約)/ 見出し 5.6B | 丸め |
| 11 | Azure の成長率 | 43%(定率換算とする複数の要約) | 41%(Constellation の見出し) | 定率換算と実額の違いの可能性(未確認) |
| 12 | Google Cloud の営業利益率 | 35.6% | 約 36% | 丸め |
| 13 | AWS の営業利益率 | 39.4% | 39%(別の丸め) | 16.6 ÷ 42.2 = 39.3% |
| 14 | Alphabet の 2026 年 2 月の 40 年債 | 当初 約 +120bp、最終 +95bp | 3 年債 +27bp(別の記述)との整合は未確認 | 複数の二次情報で数値が割れる |
| 15 | Alphabet の 40 年債(2 月 対 8 月) | 2026-02 は最終 +95bp | 2026-08 は +130bp(当初 +155bp)。単一ブログ | 別の発行。8 月分は Tier 4 のみ |
| 16 | Oracle の発行日 | 2026-02-02 に価格決定(IFR/複数要約) | [既H3] は発表 2026-02-01、価格決定日は NA | 本書は 2026-02-02 を採用(Tier 3) |
| 17 | Oracle の 2026 Q1 FY27 売上 | $19.18B(純利益 $4.76B) | $19.35B(純利益 $4.68B) | 本書の範囲外だが検索要約で割れた。公式値は Oracle の Exhibit 99.1 で確認が必要 |
| 18 | Oracle の FY27 Q1 の容量 | 「1GW 稼働予定」([既H4]、予定値) | 約 850MW を「納入」(実績、報道) | 定義(稼働か納入か)が未確認 |
| 19 | Abilene の完成時期 | 2026 年中頃(当初計画) | 2027 年初めまで(地元報道)。最終棟は 2029 年末とする報道も([既S3]) | 遅延が重なる。1.2GW は施設ベース、Epoch の 421MW は IT ベース |
| 20 | CoreWeave の「売上総利益率」 | 65.9%(cost of revenue のみ) | 約 12.2% / 約 7.3%(D&A や T&I を算入) | 4-2 節。公表の「粗利率」は存在しない |
| 21 | Oracle の AI 粗利率 | 会社: 32%(Q3 FY26)、30〜40%(長期) | The Information: 14%(2025-06〜08)、5 四半期平均 約 16% | 測る期間・対象が違う([既S3]) |
| 22 | Oracle の 5 年債の現在スプレッド | 発行時 +115bp | 2026-08 初めに 約 +180bp(Tier 3) | 発行時と二次市場の違い。銘柄の同一性は未確認 |

---

## 7. 未確認事項(欠損)と試した検索語

### 7-1. 欠損の一覧

| # | 項目 | 状態 | 試した検索語・理由 |
|---|---|---|---|
| 1 | CoreWeave の総債務・加重平均金利 | 欠損 | 検索 5・6・7 で 10-Q の債務注記に届かず |
| 2 | CoreWeave の発行体格付(Moody's・S&P・Fitch) | 欠損 | 検索せず(枠の制約) |
| 3 | CoreWeave の顧客名と比率の対応(Microsoft・OpenAI・Meta) | 確認不能 | 検索 5・21(10-Q は匿名)。受注残の顧客別内訳も欠損 |
| 4 | CoreWeave のデプリシエーション額・売上総利益 | 欠損(D&A は 4-1 節で算出) | 検索 14 |
| 5 | Nebius の売上総利益率・GAAP 営業利益率・純支払利息 | 欠損 | 検索 24: "Nebius Q2 2026 net loss operating loss cost of revenues depreciation gross profit interest expense" |
| 6 | Nebius の接続済み電力(MW)の最新値 | 欠損 | 検索 4: "Nebius Q2 2026 shareholder letter contracted power GW connected power MW ..." |
| 7 | Nebius の顧客別売上比率 | 欠損 | 検索 18 |
| 8 | Nebius のサイト別の着工〜稼働期間 | 欠損 | 検索せず |
| 9 | Meta の 2026-04 債の最終スプレッド、Amazon の 2026-03 債のトランシェ別条件 | 欠損 | 検索 11・22 |
| 10 | Microsoft の社債発行(2026 年) | 確認できず | 検索 9・11 |
| 11 | ハイパースケーラーの社債の現在の利回り(2026-09〜10) | 欠損 | 検索 9: "hyperscaler bond spreads September 2026 ..." |
| 12 | Microsoft の Intelligent Cloud 営業利益・Azure の営業利益率 | 欠損(Azure 単独の公表値も見つからず) | 検索 13・15 |
| 13 | Microsoft・Google・Meta の確保電力(GW)、Meta の Hyperion・Prometheus の稼働 | 欠損 | 検索 16・17 |
| 14 | AWS の GW 追加の最新値(2026 Q2 の会議) | 欠損。3.8GW は発言日不明 | 検索 17: "Jassy Amazon Q2 2026 earnings call gigawatts of power added ..." |
| 15 | Crusoe の資金調達・総 GW(2026) | 欠損(既存の H3 のみ) | 検索せず(枠の制約) |
| 16 | Microsoft Fairwater・Meta Prometheus の建設期間 | 欠損 | 検索 20 |
| 17 | Oracle の Q4 FY26・Q1 FY27 の AI 容量の粗利率 | 欠損 | [既S4] で 5 回検索済み |
| 18 | Oracle の「契約電力 10GW」の定義(10-K 値) | 欠損 | [既H4] の未取得項目 |
| 19 | 原文の確認 | **全項目未実施** | WebFetch 不可。8-K・10-Q・株主レター・プレスリリースは要約経由 |

### 7-2. 検索ログ(24 回。すべて mode "standard")

| # | 検索語(要点) | 用途 |
|---|---|---|
| 1 | CoreWeave second quarter 2026 results revenue backlog adjusted operating income adjusted EBITDA active power contracted power GW | CoreWeave 損益・受注残 |
| 2 | Nebius second quarter 2026 results revenue adjusted EBITDA margin contracted power GW connected power backlog Microsoft Meta | Nebius 損益・電力 |
| 3 | CoreWeave Q2 2026 earnings call active power MW contracted power GW customer concentration ... cost of revenue | 電力・顧客集中 |
| 4 | Nebius Q2 2026 shareholder letter contracted power GW connected power MW Microsoft Meta contract value ARR capex financing asset-backed loan | 株主レター |
| 5 | CoreWeave 10-Q June 30 2026 customer concentration Microsoft percent of revenue Customer A OpenAI Meta backlog percent | 顧客集中 |
| 6 | CoreWeave 2026 senior notes offering coupon priced delayed draw term loan DDTL 4.0 SOFR spread ... | 社債・DDTL |
| 7 | CoreWeave DDTL 4.0 delayed draw term loan facility billion SOFR plus basis points Meta contract investment grade secured 2026 | DDTL 4.0 |
| 8 | Nebius convertible senior notes 2026 priced coupon due 2031 2032 senior notes offering Nebius asset-backed financing SOFR ... | Nebius 転換社債 |
| 9 | hyperscaler bond spreads September 2026 Oracle vs Meta Alphabet Amazon Microsoft basis points over Treasuries ... | 社債スプレッド比較 |
| 10 | Oracle $25 billion bond February 2026 priced spread over Treasuries tranche 5-year 10-year 30-year 40-year yield T+ basis points | Oracle 新発債 |
| 11 | Meta Platforms bond sale 2026 priced tranches spread Treasuries Alphabet Amazon bond offering 2026 ... | Meta・Amazon・Alphabet 債 |
| 12 | AWS operating margin Q2 2026 Google Cloud operating income margin Q2 2026 Microsoft Azure growth ... | AWS 営業利益率 |
| 13 | Alphabet Q2 2026 results Google Cloud operating income margin backlog capex; Microsoft fiscal Q4 2026 Intelligent Cloud ... | Google Cloud |
| 14 | CoreWeave Q2 2026 gross margin cost of revenue technology and infrastructure depreciation GAAP operating margin ... | CoreWeave 費用構成 |
| 15 | Microsoft fiscal fourth quarter 2026 results Intelligent Cloud operating income Azure growth percent ... | Microsoft |
| 16 | gigawatts of power capacity added 2026 AWS Microsoft Google Meta hyperscaler total power capacity GW ... | ハイパースケーラー電力 |
| 17 | Jassy Amazon Q2 2026 earnings call gigawatts of power added AWS total capacity GW doubled by 2027 Trainium | AWS 電力 |
| 18 | Nebius Microsoft contract $17.4 billion Meta $27 billion Nebius customer concentration percent of revenue ... | Nebius 顧客 |
| 19 | Oracle Q1 fiscal 2027 earnings call gigawatts delivered capacity power secured build time months data center Abilene RPO $664 billion | Oracle 容量 |
| 20 | data center construction timeline groundbreaking to operational months Abilene Stargate Microsoft Fairwater Meta Prometheus xAI Colossus 2 Nebius New Jersey Crusoe weeks to build | 建設期間 |
| 21 | CoreWeave customer concentration 2026 Microsoft share of revenue declines OpenAI Meta largest customer percent 10-Q "Customer A" 2026 six months | CoreWeave 顧客比率 |
| 22 | Meta $25 billion bond priced April 30 2026 final spread 40-year 10-year Treasuries orders; Amazon March 2026 bond priced spread tranches | Meta・Amazon 債 |
| 23 | Alphabet 2026 dollar bond sale priced tranches spread over Treasuries; Meta Hyperion Beignet Investor bonds 6.58% 2049 ... | Alphabet 債(Meta Hyperion 債は出ず) |
| 24 | Nebius Q2 2026 net loss operating loss cost of revenues depreciation gross profit interest expense AI cloud segment adjusted EBITDA $236 million | Nebius 損益 |

---

## 8. 出典一覧

### 8-1. 今回の検索で得た出典(URL は検索結果に表示されたもの。個別の掲載日は表示がないものが多い)

| ID | 媒体・題名 | URL | 掲載日 | Tier |
|---|---|---|---|---|
| R7-01 | CoreWeave IR「CoreWeave Reports Strong Second Quarter 2026 Results」(要約経由) | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Second-Quarter-2026-Results/ | 2026-08-11 | 1* |
| R7-02 | SEC 8-K(CoreWeave 2Q26 決算プレス)(要約経由) | https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000362/coreweave2q26earningspress.htm | 2026-08(提出日は未確認) | 1* |
| R7-03 | MarketBeat「CoreWeave Q2 earnings call highlights」 | https://www.marketbeat.com/instant-alerts/coreweave-q2-earnings-call-highlights-2026-08-11/ | 2026-08-11 | 3 |
| R7-04 | americancompanies.com「CoreWeave earnings call highlights」 | https://americancompanies.com/news/coreweave-earnings-call-highlights-key-quarterly-results/ | 2026-08(日付未確認) | 3〜4 |
| R7-05 | Beancount「CoreWeave FY2026 Q2 earnings analysis」 | https://beancount.io/blog/2026/09/22/coreweave-fy2026-q2-earnings-analysis | 2026-09-22 | 4 |
| R7-06 | Quartr「CoreWeave (CRWV) Q2 2026 earnings summary」 | https://quartr.com/events/coreweave-inc-crwv-q2-2026_F6huCJA4 | 2026-08 | 3 |
| R7-07 | LongYield(Substack)「CoreWeave books $104 billion」 | https://longyield.substack.com/p/coreweave-books-104-billion-it-also | 2026-08 | 4 |
| R7-08 | Dolphin Research(LongPort)「CoreWeave: Margins inflect; interest expense rising」 | https://longportapp.cn/news/295587693 | 2026-08 | 3〜4 |
| R7-09 | sec-api.io「CoreWeave 2026 revenue analysis: top customer concentration」 | https://sec-api.io/insights/coreweave-crwv-2026-revenue-analysis-top-customer-concentration-exposure | 2026(日付未確認) | 3 |
| R7-10 | SEC 10-Q CoreWeave(2026-03-31 期)(要約経由) | https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000222/crwv-20260331.htm | 2026-05(推定) | 1* |
| R7-11 | Panabee「CoreWeave H1 revenue climbs 112% to $4.7 billion ...」 | https://www.panabee.com/news/coreweave-earnings-q2-2026-report | 2026-08 | 4 |
| R7-12 | TIKR「CoreWeave Revenue Doubled to $2.1 Billion Last Quarter ...」 | https://www.tikr.com/blog/coreweave-revenue-doubled-to-2-1-billion-last-quarter-with-99-billion-in-contracts-already-signed | 2026-05(推定) | 3 |
| R7-13 | SEC 10-Q CoreWeave(2026-06-30 期、損益計算書のみ要約で確認) | https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000366/crwv-20260630.htm | 2026-08 | 1* |
| R7-14 | CoreWeave IR「Upsize and Pricing of $1,750 Million of Senior Notes」 | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Announces-Upsize-and-Pricing-of-1750-Million-of-Senior-Notes/default.aspx | 2026-04 | 1* |
| R7-15 | BusinessWire「CoreWeave Announces Pricing of $1.25 Billion of Senior Notes and €2 Billion of Senior Notes」 | https://secure.businesswire.com/news/home/20260611950890/en/CoreWeave-Announces-Pricing-of-%241.25-Billion-of-Senior-Notes-and-%E2%82%AC2-Billion-of-Senior-Notes | 2026-06-11(URL の日付) | 1* |
| R7-16 | CoreWeave IR「Prices Upsized $3.5 Billion Convertible Senior Notes Offering」 | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Prices-Upsized-3-5-Billion-Convertible-Senior-Notes-Offering/default.aspx | 2026-04 | 1* |
| R7-17 | CoreWeave IR「Prices Upsized $3.7 Billion Convertible Senior Notes Offering」 | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Prices-Upsized-3-7-Billion-Convertible-Senior-Notes-Offering/default.aspx | 2026-09(決済 9/22) | 1* |
| R7-18 | BusinessWire / CoreWeave IR「CoreWeave Closes Landmark $8.5 Billion Financing Facility ...」 | https://www.businesswire.com/news/home/20260330529766/en/CoreWeave-Closes-Landmark-$8.5-Billion-Financing-Facility-Achieving-First-Investment-Grade-Rated-GPU-backed-Financing | 2026-03-30 〜 03-31 | 1* |
| R7-19 | Global Data Center Hub「Is CoreWeave's $8.5 Billion Deal the GPU Asset Class Moment?」 | https://www.globaldatacenterhub.com/p/is-coreweaves-85-billion-deal-the | 2026-03〜04 | 4 |
| R7-20 | Nebius Q2 2026 決算プレスリリース(Barchart 掲載) | https://www.barchart.com/story/news/3800918/nebius-reports-second-quarter-2026-financial-results | 2026-08-12 | 1* |
| R7-21 | Nebius Q2 2026 株主レター(PDF、抽出が部分的) | https://mms.businesswire.com/media/20260812963359/en/2874372/1/SHLQ226.pdf | 2026-08-12 | 1* |
| R7-22 | The Energy Mag「Nebius Group reports 454% revenue growth in Q2 2026, raises power guidance to 5 GW」 | https://theenergymag.com/news/market-news/nebius-group-reports-454-revenue-growth-in-q2-2026-raises-power-guidance-to-5-gw | 2026-08 | 3 |
| R7-23 | StorageNewsletter「Nebius: Fiscal 2Q26 Financial Results」 | https://www.storagenewsletter.com/2026/08/20/nebius-fiscal-2q26-financial-results/ | 2026-08-20 | 3 |
| R7-24 | Nasdaq / RTTNews「Nebius posts loss in Q2, revenues up 454%」 | https://www.nasdaq.com/articles/nebius-posts-loss-q2-revenues-454 | 2026-08 | 3 |
| R7-25 | Nebius 6-K / ニュースルーム(転換社債の価格決定、2026-03 と 2026-08) | https://nebius.com/newsroom/nebius-group-announces-proposed-private-offering-of-3-75-billion-of-convertible-senior-notes ; https://www.sec.gov/Archives/edgar/data/0001513845/000110465926098590/tm2623513d1_ex99-1.htm | 2026-03 / 2026-08 | 1* |
| R7-26 | Nasdaq / Zacks「Do Nebius Mega Deals Increase Customer Concentration Risk?」(RPO の記述は別記事の URL 群を含む) | https://www.nasdaq.com/articles/do-nebius-mega-deals-increase-customer-concentration-risk | 2026-01(URL の日付 260105)ほか | 3 |
| R7-27 | Investing.com「Nebius Just Locked Up $49B in AI Contracts」 | https://www.investing.com/analysis/nebius-just-locked-up-49b-in-ai-contracts-5-ways-to-play-the-neocloud-boom-200677144 | 2026(日付未確認) | 3 |
| R7-28 | 24/7 Wall St.「Wall Street Says Nebius Group ARR Can 10X in 4 Years」、sec-api.io「Nebius financial analysis」 | https://247wallst.com/investing/2026/08/21/wall-street-says-nebius-group-arr-can-10x-in-4-years/ ; https://sec-api.io/insights/nebius-financial-analysis | 2026-08-21 | 3 |
| R7-30 | Amazon「Second Quarter Results」(Nasdaq 掲載)、Quartz、FinanceBuzz | https://www.nasdaq.com/press-release/amazoncom-announces-second-quarter-results-2026-07-30 ; https://qz.com/amazon-q2-2026-earnings-aws-cloud-growth-073026 ; https://financebuzz.com/news/amazons-aws-record-profit-margin | 2026-07-30 | 1*/3 |
| R7-31 | The Next Web「Alphabet lifts capex guide to $205bn as Google Cloud jumps 82%」、AI Weekly、Fierce Network | https://thenextweb.com/news/alphabet-q2-2026-capex-205bn-cloud-82 ; https://aiweekly.co/alerts/alphabet-q2-cloud-jumps-82-to-248b-capex-hits-449b ; https://www.fierce-network.com/cloud/google-cloud-surges-alphabets-ai-capex-problem-grows | 2026-07(22〜23 日の決算) | 3 |
| R7-32 | Pulse 2、Redmondmag、Constellation Research(Microsoft FY26 Q4) | https://pulse2.com/microsoft-reports-revenue-of-90-billion-up-18-year-over-year-for-q4-2026/ ; https://redmondmag.com/articles/2026/07/30/microsoft-tops-90b-quarterly-revenue.aspx ; https://www.constellationr.com/insights/news/microsoft-azure-q4-revenue-surges-41-tops-100-billion-annual-revenue | 2026-07-29〜30 | 3 |
| R7-33 | Fortune「Andy Jassy Amazon capex demand」、The Next Platform「AWS bullish on homegrown Trainium」(Jassy の 3.8GW、日付未確認) | https://fortune.com/2026/07/30/andy-jassy-amazon-capex-demand-aws-pga-tour/ ; https://www.nextplatform.com/?p=146551 | 2026-07-30 / 日付未確認 | 3 |
| R7-34 | 債券: Meta「Looks to Raise as Much as $25 Billion With Jumbo Bond Sale」(Advisor Perspectives 転載、Bloomberg 系)、Alphabet 2026-02(Techloy、Minster Community Post)、Alphabet 2026-08(Advisor Perspectives 2026-08-06、ai2.work) | https://www.advisorperspectives.com/articles/2026/04/30/meta-raise-25-billion-jumbo-bond-sale ; https://www.techloy.com/alphabet-raises-20-billion-in-bond-sale-launches-first-tech-100-year-bond-since-1997/ ; https://business.minstercommunitypost.com/minstercommunitypost/article/marketminute-2026-2-17-ai-arms-race-triggers-record-demand-alphabet-secures-20-billion-in-oversubscribed-bond-sale ; https://www.advisorperspectives.com/articles/2026/08/06/alphabet-seeking-25-billion-bond-sale ; https://ai2.work/blog/alphabet-s-25b-ai-bond-sale-drew-115b-in-orders-what-it-means | 2026-04-30 / 2026-02 / 2026-08 | 3〜4 |
| R7-35 | Oracle 2026-02 債: TheRightTrader(4.95% 2031、5.70% 2036、6.55% 2046、6.85% 2066)、IFR「Oracle returns with another jumbo bond」 | https://therighttrader.com/bonds/oracle/4-95-2031 ; https://therighttrader.com/bonds/oracle/5-7-2036 ; https://therighttrader.com/bonds/oracle/6-55-2046 ; https://therighttrader.com/bonds/oracle/6-85-2066 ; https://www.ifre.com/bonds/2379081/oracle-returns-with-another-jumbo-bond-to-fund-ai-expansion | 2026-02-02 | 4(スプレッド)/ 3 |
| R7-36 | Advisor Perspectives「Is There Really Carnage in Hyperscaler Credit?」、Real Investment Advice(同題)、Advisor Perspectives「Hidden Debt」 | https://www.advisorperspectives.com/articles/2026/08/03/there-carnage-hyperscaler-credit ; https://realinvestmentadvice.com/resources/blog/carnage-in-hyperscaler-credit-really/ ; https://www.advisorperspectives.com/articles/2026/08/10/hidden-debt-hyperscaler-thesis-wrong | 2026-08-03 / 08-10 | 3 |
| R7-37 | DCD「Oracle delivered 300,000 GPUs in Q1 FY2027」、The Next Platform(2026-09-14)、Oracle 決算プレス(Seeking Alpha 掲載)、ERP Today | https://www.datacenterdynamics.com/en/news/oracle-delivered-300000-gpus-in-q1-fy2027/ ; https://nextplatform.com/cloud/2026/09/14/despite-hefty-capital-investments-the-cloud-starts-paying-off-for-oracle/5296362 ; https://seekingalpha.com/pr/20647809 ; https://erp.today/oracle-beats-estimates-as-ai-cloud-demand-surges-lifts-2027-revenue-outlook-to-90b/ | 2026-09-10〜14 | 1*/3 |
| R7-38 | Epoch AI(Abilene 衛星エクスプローラー 2026-07-27/28 更新、建設速度のデータ)、KTXS(Abilene 工事は 2027 年初めまで)、DCD(Crusoe Abilene 第 2 期) | https://epoch.ai/data/data-centers/satellite-explorer/OpenAIStargateAbilene ; https://epoch.ai/data-insights/data-centers-buildout-speeds ; https://ktxs.com/news/local/lancium-crusoe-executives-brief-abilene-leaders-on-major-northside-investment ; https://datacenterdynamics.com/en/news/crusoe-begins-construction-on-second-phase-of-abilene-texas-data-center-campus-will-add-six-buildings | 2026-07 | 3 |
| R7-39 | 業界電力: Data Center Knowledge、Datacentres.com(2026-05-25・07-13)、Opus.pro、Whoisatlas(Substack)、CIO Dive、ABI Research(個別の数値の帰属は URL 群のみ) | https://www.datacenterknowledge.com/hyperscalers/hyperscalers-in-2026-what-s-next-for-the-world-s-largest-data-center-operators- ; https://www.datacentres.com/news/hyperscaler-capex-surge-pushes-global-data-centre-capacity-to-50-gw-as-power-con-slot1-2026-07-13 ; https://www.opus.pro/blog/ai-infrastructure-news-april-2026 | 2026-04〜07 | 3〜4 |

### 8-2. 既存調査の出典(再掲元)

| ID | 内容 | ファイル |
|---|---|---|
| 既S1 | 経営陣のシナリオ(AI 粗利率 30〜40%、6 年・$60B の例) | `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research/S1_management_scenario.md` |
| 既S2 | 市場の仮説(RPO、OpenAI 比率) | `.../orcl/research/S2_market_hypothesis.md` |
| 既S3 | スカットルバット(拠点別一覧、CoreWeave 値上げ、The Information の 14%) | `.../orcl/research/S3_scuttlebutt.md` |
| 既S4 | 核心変数(AI 容量の粗利率 32%、耐用年数) | `.../orcl/research/S4_core_variables.md` |
| 既R2 | 製品の 5W1H(OpenAI 契約の年額推計) | `.../orcl/research2/R2_products_5w1h.md` |
| 既R5 | 信用面(格付、CDS、社債利回り、平均調達金利) | `.../orcl/research2/R5_credit.md` |
| 既H3 | 債務・調達イベント | `.../orcl/data/H3_financing_events.csv` ほか |
| 既H4 | 容量(Q3 FY26 400MW、FY26 1.2GW、Bloom 1.2〜2.8GW) | `.../orcl/data/H4_capacity.csv` |
| 既H1 | 年次損益(FY26 売上 $67.4B) | `.../orcl/data/H1_annual.csv` |

---

## 9. 次に確認すべき原典(取得できたら本書の値を置き換える)

1. CoreWeave 10-Q(2026-06-30 期、`crwv-20260630.htm`)の顧客集中注記・債務注記・損益計算書の費用行。
2. CoreWeave 8-K(`coreweave2q26earningspress.htm`)の電力・受注残・調整表。
3. Nebius の Q2 2026 株主レター(`SHLQ226.pdf`)と 6-K の損益計算書(営業損失・売上原価・支払利息)。
4. Oracle の 2026-02 債の 424B2(トランシェ別の金額・国債スプレッド)と、Alphabet・Meta・Amazon の 2026 年債の 424B2(最終スプレッド)。
5. Oracle の Q1 FY27 決算説明会の原文(850MW の「納入」の定義、AI 容量の粗利率、10GW の確保の定義)。
6. Microsoft の FY26 Q4 の 10-K/10-Q 注記(Intelligent Cloud の営業利益)。
