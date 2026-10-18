# W8: AWS の競争優位の形成と、AI インフラが「AWS 型」か「GPU 時間貸し型」かの材料

- 作成日: 2026-10-12(各表の「時点」欄がデータ基準時点)/ 対象: Oracle(NYSE: ORCL)再評価の論点「AI クラウド事業の将来の利益率と価値」
- 目的: 事実・数値・出典の整理と、出典間の食い違いの指摘のみ。**投資判断・推奨・評価は書かない。** 「AWS 型になる」「コモディティになる」のどちらの結論も本書は出さない。
- 取得手段: WebSearch のみ。**24 回 / 上限 24 回を使い切った(standard 24、extended 0)。** WebFetch は使えない。
- **原本(10-K、決算説明会の書き起こし、調査会社のレポート本文、Stratechery の記事本文、SemiAnalysis の本文)は 1 件も直接読めていない。** 数値は検索ツールの要約に書かれていた内容で、本書の外部数値は原則すべて `*` 付き。SemiAnalysis・McKinsey・Stratechery は本文が有料または未取得で、要約の記述のみ。
- Tier: 1=会社開示・決算説明会、2=規制当局・格付会社・中央銀行・公的統計、3=報道・アナリスト・調査会社、4=ブログ・SNS・販促・集約サイト。`*` は検索要約経由で原本未読。
- 「(算出)」は調査者の計算で式を併記した。丸め値(「約」「≈」)から計算した値は丸め誤差を含む。
- 出典 ID `[W8-nn]` は「nn 番目の検索の要約」(末尾に URL 一覧)。1 回の要約が複数サイトを統合しているため、個別の数値がどの URL 由来かを特定できない場合がある。`[W1]` `[W2]` `[W3]` `[W5]` `[W6]` は同じ research3 フォルダの既存調査、`[R3]` `[R4]` `[R5]` `[R7]` は research2、`[S1]` `[S4]` は research の既存調査。既存と重複する事実は再掲に留め、「(再掲)」と書いた。
- パス: research3 = `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research3/`、research2 = `.../orcl/research2/`、research = `.../orcl/research/`。

---

## 0. 要約(事実のみ、10 行)

1. **AWS の営業利益率**は 2014 年 10.0% → 2015 年 19.1% → 2016 年 25.5% → 2018 年 28.4% → 2023 年 27.1% → 2024 年 37.0% → 2026 年 Q2 39.3%(Q2 の前年同期は 33.0%)。2024 年の +9.9pt の要因分解を示す資料は見つからなかった。2024 年は Amazon のサーバー耐用年数が 5→6 年に延長された年で、減価償却の減少 $3.2B(Amazon 全社)が全額 AWS に配分されたとしても最大 3.0pt(算出)。(再掲 [W1]、Tier 1*)
2. **値下げ**: S3 は 2006 年の $0.15/GB・月から 2016 年 12 月の $0.0230(米国東部)で −84.7%(算出)。AWS 自身は「10 年で 80% 引下げ」。値下げ回数は出典で 40 回(2012 年頃)、約 30 回(2016 年)、62 回(2017 年)と割れる。GPU では p5(H100)を 2025 年 6 月に −44%($12.29 → $6.88 /GPU 時、再掲 [R3])。(Tier 1*〜4*)
3. **自社チップ**: AWS によれば Graviton は新規 CPU 容量の過半を 3 年連続で占め、上位 1,000 EC2 顧客の 98% が利用。Jassy は「x86 比で最大 40% の価格性能」と書いた(AWS の主張で独立検証なし)。2026 年 Q2 の説明会で自社チップ事業は「年換算売上 $25B 超」(Q1 は $20B 超)。Nitro の原価低減額は欠損。(Tier 1*)
4. **AWS の AI の利益率**: Jassy は 2026 年 Q2 に「AI 事業は中核事業と同じ利益率の軌道で、やや先行」と説明。Q1 には「Trainium は推論で数百ベーシスポイントの営業利益率の優位をもたらす見込み」(将来の見込み)。AWS の 2026 年 Q2 は営業利益 $16.6B・率 39.3%(算出)。(Tier 1*〜3*)
5. **転送料・乗り換え**: AWS は 2024-03 に「全データを移して契約を終了する顧客」の転送料を免除(60 日以内、条件付き)。英 CMA は 2025-07 に AWS・Microsoft に「重要な市場支配力」があると認定し、2026-03-31 に両社の自主的約束(乗り換え期間 180 日以上の egress 免除など)を受理して SMS 調査は開始せず。乗り換えコストの金額・顧客調査は欠損。(Tier 2*〜3*)
6. **CoreWeave**(GPU 貸しの代表例): FY2025 売上 約 $5.13B、営業損失 $46M(−0.9%、算出)、調整後 EBITDA $3.09B(60.2%、算出)、純損失 $1.17B。2026 年 Q2 は調整後営業利益率 5.0%、GAAP 営業利益率 −1.9%、純支払利息は売上の 24.9%(再掲 [R7])。同期間の AWS は 39.3%。調整後 EBITDA と調整後営業利益の差は売上の 53.7%(算出。減価償却等の代理)。(Tier 1*〜3*)
7. **ハイパースケーラーの説明**: Microsoft Cloud の粗利率は FY2026 Q3 に 66%(前年 69%)で、「Azure と M365 の効率化を AI インフラ投資と AI 製品の利用増が上回った」。Google Cloud は 2026 年 Q2 に営業利益率 35.6%(前年同期 20.7%)で、会社の説明は売上の増加への言及が中心(費用側の定量説明は欠損)。増分営業利益率は Google Cloud 53.7%、AWS 56.6%(いずれも算出)。(Tier 1*〜3*)
8. **識者**: Morgan Stanley(2026-07)は GPU リース ROIC 約 31%(前提: GB300 $8.50/時、稼働率 75%)、自社インフラ API 約 46%、第三者計算 API 約 25%。トークン価格が 1 百万トークン $1 未満、または稼働率 70% 未満で ROIC が急低下とする。McKinsey 引用の「GPU 貸しの粗利率 14〜16%」。SemiAnalysis の H100 1 年契約指数は $1.70(2025-10)→ $2.35(2026-03)。Thompson は「モジュラー部分はコモディティ化、統合部分に利益」と述べる(要約)。(Tier 3*)
9. **Oracle の位置(事実)**: Q1 FY27(2026-06〜08)の売上 $19.3B のうち OCI(IaaS)$7.4B(38.3%、算出)。経営陣は「更新を高い価格で実施、フリートはほぼ満稼働」と説明。**AI 容量の顧客が DB・アプリ・AI サービスも買っている証拠は、今回の検索でも見つからなかった**(マルチクラウド DB 売上 +353%、顧客数 +180% は成長率のみ)。推論比率の会社開示は欠損。(Tier 1*〜3*)
10. **資金面(事実)**: Oracle の FY26 FCF は −$23.7B、Q1 FY27 は −$5.4B(再掲 [S1])。未開始リース約束は 2026-05-31 に約 $260B(期間 15〜19 年)、2026-08-31 に約 $288B。S&P BBB-、Moody's Baa2(ネガティブ)、Fitch BBB。CoreWeave の GPU 担保ローンは SOFR+2.25%(Moody's A3)、無担保債は 9.6〜9.75%(再掲 [R7])。リース調達における Oracle の信用力の寄与を定量化した資料は欠損。(Tier 1*〜3*)

---

## 1. AWS の高収益化: 要因別の事実

**先に**: AWS の営業利益率を「規模の経済」「自社チップ」「上位サービス」「値下げ」などに分解した資料(会社・調査会社・報道)は、今回の 24 回の検索では 1 件も見つからなかった(欠損)。以下は要因ごとの事実を別々に並べたもので、寄与度は不明。

### 1-1. AWS の利益率の時系列(再掲 [W1] と今回の追加)

| 時点 | 売上 | 営業利益 | 営業利益率 | 売上前年比 | 出典 | Tier |
|---|---|---|---|---|---|---|
| 2014(年) | ≈$4.6B | $458M | ≈10.0%(算出) | ≈+48%(算出) | [W1] 再掲 | 4*/3* |
| 2015 | ≈$7.9B | $1,507M | ≈19.1%(算出) | ≈+72%(算出) | [W1] 再掲 | 4*/3* |
| 2016 | ≈$12.2B | $3,108M | ≈25.5%(算出) | ≈+54%(算出) | [W1] 再掲 | 1*/3* |
| 2017 | ≈$17.5B | $4,331M | ≈24.7%(算出) | ≈+43% | [W1] 再掲 | 1*/3* |
| 2018 | ≈$25.7B | $7,296M | ≈28.4%(算出) | ≈+47% | [W1] 再掲 | 1*/3* |
| 2021 | ≈$62B(下限) | $18,532M | ≈29.9%(算出、分母は下限) | 欠損 | [W1] 再掲 | 1*/4* |
| 2022 | ≈$80B(下限) | $22,841M | ≈28.6% 以下(算出) | ≈+29%(概算) | [W1] 再掲 | 1*/4* |
| 2023 | $90,757M | $24,631M | 27.1%(算出) | ≈+13% | [W1] 再掲 | 1* |
| 2024 | $107,556M | $39,834M | 37.0%(算出) | +18.5%(算出) | [W1] 再掲 | 1* |
| 2025 | ≈$128.7B | ≈$45.6B | ≈35.4%(算出) | ≈+19.7%(算出) | [W1] 再掲 | 1*/3*/4* |
| 2026 Q1 | $37.6B | $14.2B | 37.7%(要約記載。算出 37.8%) | +28% | [W1] 再掲 | 1*/3* |
| 2026 Q2 | $42.2B | $16.6B | 39.3%(算出: 16.6 ÷ 42.2。CFO は「39%」) | +36.7% | [W8-06][W8-15] | 1*/3* |

追加の事実(2026 年 Q2、AWS CFO Olsavsky の説明を伝える要約):
- 営業利益率は前年同期比 **+650bp**。1 回限りの派生商品(エネルギー契約)の会計上の利益を除くと **+520bp**。[W8-06] Tier 3*
- 年換算売上 約 $169B(算出: 42.2 × 4 = 168.8)、受注残 $496B。[W8-15] Tier 3*
- 全社の設備投資(Amazon)の 2026 年見通し 約 $220B。Q2 の全社 FCF は約 −$7.6B(要約)。[W8-15] Tier 3*

算出 1(増分営業利益率、2026 年 Q2 の前年同期との差):
- AWS: (16,600 − 10,200) ÷ (42,200 − 30,900) = 6,400 ÷ 11,300 = **56.6%**(算出。前年同期の値は [W1] が前年比から逆算した値で、丸め誤差と 1 回限りの利益を含む)。
- Google Cloud: (8,814 − 2,826) ÷ (24,768 − 13,624) = 5,988 ÷ 11,144 = **53.7%**(算出。値は [W8-05] の要約記載)。

算出 2(2024 年の +9.9pt と耐用年数の関係):
- 2024 − 2023 = 37.0% − 27.1% = +9.9pt(算出)。
- Amazon の 2024 年の耐用年数変更(サーバー 5→6 年)による減価償却の減少 $3.2B([W1] 再掲、Amazon 全社の値)÷ AWS 2024 年売上 $107.556B = 最大 **3.0pt**(算出。全額が AWS に配分されたと仮定した上限。配分額は未確認)。2025 年は一部を 6→5 年に戻し、減価償却 +$1.4B(主に AWS、[W1] 再掲)。

### 1-2. 値下げの回数と幅の歴史

| 項目 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| S3 の発売価格 | $0.15 /GB・月 | 2006 | AWS ブログ(2016 年の記事) | 1* |
| S3 の米国東部・標準(最初の 50TB) | $0.0230 /GB・月 | 2016-12 | AWS ブログの地域別価格表 | 1* |
| 同上の下落率 | 0.0230 ÷ 0.15 − 1 = **−84.7%**(算出)。AWS の記述は「10 年で GB あたり 80% 引下げ」 | 2006→2016 | [W8-01] | 1*/算出 |
| アイルランドの S3 | 2007 年の開始時 $0.18 → $0.023(約 90% 減、要約の記述)。算出: 0.023 ÷ 0.18 − 1 = −87.2% | 2007→2017 | [W8-01] | 4* |
| 値下げ回数 | 40 回(Computerworld、2012 年頃)/ 約 30 回(2016 年の記事)/ 62 回(2017 年の記事)。範囲(全サービスか一部か)が異なる可能性。現在までの累計は**欠損** | 2012〜2017 | [W8-01] | 3*〜4* |
| 現在の S3 標準の単価 | **欠損**(今回の検索で出ず) | — | — | — |
| H100 搭載 p5.48xlarge | $98.32/時($12.29/GPU)→ $55.04/時($6.88/GPU)。−44.0%(再掲 [R3]、算出: (98.32 − 55.04) ÷ 98.32) | 2025-06 | [R3] 再掲 | 4 |
| AWS の H100 スポット価格 | ある地域で最大 −88%($105.20 → $12.16、単位の記載なし)。Cast の分析を引く二次情報 | 2024-01 → 2025-09 | [W8-14] | 4* |
| 2025-10 以降の GPU 時間単価 | 上昇(SemiAnalysis の H100 1 年契約指数 $1.70 → $2.35、2026-03)。2-2 節 | 2025-10〜2026-03 | [W8-08] | 3* |

### 1-3. 自社チップ(Graviton・Nitro・Trainium)

| 項目 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| Graviton の割合 | 新規 CPU 容量の**過半**を 3 年連続で占める。上位 1,000 EC2 顧客の 98% が利用 | 2025-12-03(Graviton5 発表) | AWS の発表(Business Wire)[W8-02] | 1* |
| 価格性能 | Jassy の 2025 年株主向け書簡: 「他の x86 より最大 40% 良い価格性能」。**AWS の主張で独立検証は見つからず** | 2026 年 | [W8-02] | 1* |
| Graviton5 | 192 コア、前世代比で最大 25% 高性能(AWS の主張) | 2025-12 | [W8-02] | 1* |
| 需要 | 大口顧客 2 社が「2026 年の Graviton 容量の全量を買いたい」と申し出て AWS は断った(Jassy の書簡) | 2026 年 | [W8-02] | 1* |
| Nitro の起源 | 2012 年にハイパーバイザー機能と認証機能をサーバー CPU から切り離す必要が認識され、Nitro に発展。最初の Nitro 世代の C5 は一般提供 2017-11-06 | 2012〜2017 | [W8-19] | 4* |
| Nitro の効果 | AWS の求人文面に「サーバーのほぼ全資源を顧客インスタンスへ渡せる」。**原価低減の額・率は欠損** | — | [W8-19] | 4* |
| 自社チップ事業の規模 | 年換算売上 $20B 超(Q1 2026、株主向け資料の要約。[W1] 再掲)→ **$25B 超**(Q2 2026 の説明会の要約)。Anthropic・OpenAI と複数年・複数ギガワットの契約 | 2026 Q1→Q2 | [W8-06] | 3* |
| Trainium の経済 | Jassy(2026 年 Q1): 「規模が出れば、Trainium は年間で設備投資を数百億ドル節約し、推論で他社チップに頼る場合より**数百ベーシスポイントの営業利益率の優位**をもたらす見込み」(将来の見込み。実績ではない) | 2026-04 | [W8-06][W8-18] | 3* |

### 1-4. 乗り換えコスト・データの重力・転送料・規制

| 項目 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| AWS の転送料免除 | 2024-03、AWS から退出する顧客の転送料を免除。条件: 全データを移して AWS 環境を閉じる、60 日以内、サポートへ申請、良好な口座、CloudFront・Direct Connect 等は対象外。AWS は「顧客の 90% 超はもともと月 100GB の無料枠で追加費用なし」と主張。Google が先に実施 | 2024-03 | [W8-20] | 3* |
| 動機 | EU データ法(切替の障害の除去)が引用される | 2024 | [W8-20] | 3* |
| 英 CMA の市場調査の最終報告 | 2025-07。egress 料金・相互運用性・ソフトのライセンスに懸念。AWS と Microsoft に**重要な市場支配力**があり、egress 料金と相互運用性の障壁が切替と複数クラウド利用を制約すると認定。市場調査の枠では救済策を提案せず | 2025-07 | [W8-09] | 2* |
| CMA の決定 | 2026-03-31、戦略的市場地位(SMS)調査は開始せず、AWS と Microsoft の**自主的約束**を受理。内容: 切替を決めた時点から 180 日以上の egress 免除、複数クラウド間の転送料引下げ、他社クラウドとの直接接続。6 か月後に委員会で見直し | 2026-03-31 | [W8-09] | 2* |
| 英国のシェア(Google の主張) | Google 5〜10%、AWS+Microsoft 60〜70%。解説記事の引用で CMA の数字ではない | 古い(日付不明) | [W8-09] | 4* |
| 価格比較(再掲) | 外向き通信の超過単価 AWS $0.09/GB ÷ OCI $0.0085/GB = 10.6 倍(算出)。OCI は月 10TB 無料 | 2026 年 | [R3] 再掲 | 4 |
| データの重力・ロックインの顧客調査(移行率、切替の費用) | **欠損** | — | — | — |

### 1-5. 設備投資と ROIC の推計

| 項目 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| AWS のセグメント設備投資(P&E 追加額) | 2023 年 $24.8B → 2024 年 $53.3B → 2025 年 $96.5B。売上比 27.4% → 49.5% → 75.0%(算出) | 2023〜2025 | [W1] 再掲 | 1* |
| 3 年累計(算出) | 24.8 + 53.3 + 96.5 = **$174.6B** | 2023〜2025 | 算出 | — |
| 粗い比率 1(算出) | 2025 年の AWS 営業利益 $45.6B ÷ 3 年累計の設備投資 $174.6B = 26.1%。**ROIC ではない**(税引前、累計の追加額で減価償却控除前、建設中の資産を含む) | — | 算出 | — |
| 粗い比率 2(算出) | (2025 年 $45.6B − 2022 年 $22.841B)÷ $174.6B = 13.0%。**増分の収益性ではない**(設備投資と売上の時間差、2020〜2022 年の投資を含まない) | — | 算出 | — |
| Amazon 全社の ROIC | 2018〜2025 年の平均 17%(Piper Sandler)。Wolfe は ROIC が 2027 年頃に底打ち、2029 年頃から改善と予想。Wolfe は 2024〜2030 年の設備投資を約 $1 兆(大半が AWS)と推計 | 2026 年 | [W8-15] | 3* |
| **AWS 単独の ROIC の推計** | **欠損**(会社は非開示。アナリストの AWS 単独値は今回の検索で出ず) | — | — | — |
| Morgan Stanley の枠組み(2026-07) | 3-1 節 | 2026-07 | [W8-11] | 3* |
| 見方の違い | UBS は 2026 年の設備投資ガイドから「2 年で AWS の売上と営業利益が倍増し得る」。他のアナリストは「経営陣は長期の投資収益に自信があるが、先の見通しが不透明」「メモリ価格上昇と Azure・Google の競争で AWS の利益率が圧迫され得る」 | 2026 年 | [W8-15] | 3* |

### 1-6. AWS 売上の構成(上位サービスの比率)

- 公式なサービス別売上は**開示なし**(再掲 [W1]: 2021 年推定で EC2 が 50% 超)。今回の検索でも構成比は出なかった(欠損)。
- AWS の AI 事業: 年換算売上 $15B 超(2026 年 Q1 の説明会で「最初の 3 年で」)。Bedrock の利益率は欠損(成長率と利用量のみ)。Jassy は「AWS は自社の最先端モデルなしでも成功できる。Bedrock の強みは選択肢の広さ、ガバナンス、セキュリティ」と述べた(2026 年 Q2)。[W8-06] Tier 3*

---

## 2. GPU の時間貸しの経済性

### 2-1. CoreWeave の利益構造

| 時点 | 項目 | 値 | 出典 | Tier |
|---|---|---|---|---|
| FY2024 | 営業利益 / 調整後 EBITDA / 純損失 / 売上原価 | +$324M / $1.22B / −$863M / $493M | [W8-03] | 3* |
| FY2025 | 売上 | 約 $5.13B | [W8-03] | 3* |
| FY2025 | 売上原価(集約サイトの値。技術・インフラ費用は別行) | $1,453M。売上原価 ÷ 売上 = 28.3%(算出: 1,453 ÷ 5,130)。売上 − 売上原価 = 71.7%(算出)。**会社報告の粗利率ではない** | [W8-03] | 3*〜4* |
| FY2025 | 営業損益 | −$46M。営業利益率 −0.9%(算出: −46 ÷ 5,130) | [W8-03] | 3* |
| FY2025 | 調整後 EBITDA | $3.09B。率 60.2%(算出: 3,090 ÷ 5,130) | [W8-03] | 3* |
| FY2025 | 純損失 | $1.17B(率 −22.8%、算出: −1,170 ÷ 5,130) | [W8-03] | 3* |
| FY2025 Q4 | 調整後営業利益 | $88M(前年同期 $121M。インフラの先行展開が主因と説明) | [W8-03] | 3* |
| FY2025 | 通期の調整後営業利益・支払利息 | **欠損** | — | — |
| 2026 Q2(~06-30) | 売上 / 調整後 EBITDA / 調整後営業利益 / GAAP 営業損益 / 純損失 / 純支払利息 | $2,575M(+112%)/ $1,510M(58.6%)/ $128M(5.0%)/ −$49M(−1.9%)/ −$626M / $640M(売上の 24.9%)(再掲 [R7]。[W8-10] の要約と一致。売上は $2.58B と $2.6B の記載差) | [R7][W8-10] | 1*/3* |
| 2026 Q2 | 売上 − 売上原価(技術・インフラ費用の前) | 約 65.9%。**集約サイトの算出値で会社報告の粗利率ではない**。FY2025 の 71.7%(算出)との差は −5.8pt(算出) | [W8-10] | 4* |
| 2026 Q2 | 調整後 EBITDA − 調整後営業利益 | 1,510 − 128 = $1,382M = 売上の **53.7%**(算出: 1,382 ÷ 2,575)。減価償却・償却を主とする調整項目の代理値(株式報酬等も含み得る。D&A の行は未取得) | 算出 | — |
| 2026 Q2 | 調整後営業利益率 5.0% と GAAP 営業利益率 −1.9% の差 | 6.9pt(算出: 5.0 − (−1.9))= 株式報酬等の調整 | 算出 | — |
| 2026 Q3 見通し | 売上 / 調整後営業利益 / 支払利息 | $3.45〜3.6B / $200〜260M / $860〜940M。調整後営業利益率 5.8〜7.2%(算出: 200 ÷ 3,450、260 ÷ 3,600)。支払利息(中央値 $900M)÷ 調整後営業利益(中央値 $230M)= 3.9 倍(算出) | [W8-10] | 3* |
| 2026 Q4 見通し | 調整後営業利益率 | 「10%台前半」(経営陣の発言の要約) | [W8-10] | 3* |
| 2026 通期見通し | 売上 / 調整後営業利益 / 設備投資 / 年末の年換算売上 | $12.4〜13.2B / $960M〜1.15B / $35〜39B / $18.5〜19.5B。調整後営業利益率 7.7〜8.7%(算出: 960 ÷ 12,400、1,150 ÷ 13,200)。設備投資 ÷ 売上 2.7〜3.1 倍(算出: 35 ÷ 13.2 〜 39 ÷ 12.4) | [W8-10] | 3* |
| 価格・更新(再掲) | 2026-07 に全 SKU で約 25% 値上げの報道、A100 契約(2029 年まで)を「attractive price」で締結、旧世代 SKU の価格は「数年前と同等以上」 | 2026-07〜08 | [W2][S3] 再掲 | 3* |

### 2-2. GPU 貸しの利益率・価格動向の第三者の見方

| 出典 | 内容 | 時点 | Tier |
|---|---|---|---|
| McKinsey「The evolution of neoclouds and their next moves」[W8-07] | 「一部の報告では GPU 貸し事業の粗利率は人件費・電力・減価償却後で **14〜16%**」。ハイパースケーラーはネオクラウドの最大顧客群で、「すぐ使える容量」にプレミアムを払い、**ネオクラウドの貸借対照表を使って自社の資産を減らす**用意がある。契約の価値は単体の収益性より、稼働率の保証と投資家への信用力にある(McKinsey の記述の要約) | 日付不明 | 3* |
| SemiAnalysis(H100 1 年契約指数)[W8-08] | $1.70(2025-10)→ $2.35(2026-03)、約 +40%。**オンデマンドはどの GPU も売り切れ**。数年前の価格での H100 契約の更新が、一部 2028 年まで延びている。2023〜2024 年のピークから 60% 超下落した流れの反転 | 2025-10〜2026-03 | 3* |
| 同上(別記事の要約)[W8-08] | 2025-05〜2026-05 に約 $1.95 → $2.65(+36%)。2026 年央の解説は「スポットと旧世代 Hopper は軟化、プレミアム・長期契約・Blackwell は堅調または上昇」 | 2026-05〜06 | 4* |
| SemiAnalysis「AI Neocloud Playbook and Anatomy」[W8-08] | 所有コストとリターンを扱う(2024-10)。本文は有料で未取得。利益率の数字は要約に出ず | 2024-10 | 3*(本文未読) |
| Bernstein(Rasgon)[W8-11] | GPU 貸し価格は「循環ではなく体制変化」。1 時間 $4 前後が基準になり得る。2026-04-14 のノートで、その水準が年末まで続けば CoreWeave の年換算 EBITDA が約 $1.2B 増える(**信頼性の低い媒体経由。原文未確認**) | 2026-04 | 4* |
| 反対の見方[W8-07][W8-14] | 「H100 の貸出料はピークから 60〜75% 下落」(ブログ)。「2026 年の H100 平均オンデマンド $3.61/GPU 時、42 社」(集約サイト)。H100 の価格の方向は出典により逆 | 2026 年 | 4* |
| 需給の逸話 | 容量ブローカーの話として「需要が供給の 50 倍」(逸話)。顧客が短い契約を求め始めたとの指摘 | 2026 年 | 4* |
| 世代別の価格(再掲 [W2]) | Blackwell 指数 $2.75(2026-02)→ $4.08(2026-04-13)、Silicon Data B200 $5.66(2026-08-02) | 2026 年 | 3* |

### 2-3. ハイパースケーラーの AI 事業の利益率: 会社の説明

| 会社 | 時点 | 内容 | 出典 | Tier |
|---|---|---|---|---|
| Microsoft | FY2026 Q1(2025-09 期、2025-10-29) | Hood: Microsoft Cloud の粗利率は約 66% の見込みで前年比低下。「AI への継続投資と Azure への構成変化」が理由。Nadella: 「フリートは**代替可能(fungible)**で継続的に更新」。内部指標は「ドル・ワット当たりのトークン数」。GPT-4.1・GPT-5 の GPU 当たりのトークン処理量は同四半期に 30% 超増 | [W8-04][W8-16] | 1*〜3* |
| Microsoft | FY2026 Q2(2025-12 期、2026-01-28) | 全社粗利率 68%(前年比やや低下)、Microsoft Cloud 67% とする記載もあり(指標が異なる可能性)。AI のコストと利用増が効率化を上回る、と Hood。通期の営業利益率は小幅上昇の見込み。効率化で一部容量を Azure に再配分 | [W8-04][W8-16] | 1*〜3* |
| Microsoft | FY2026 Q3(2026-03 期、2026-04-29) | Microsoft Cloud 粗利率 66%(想定よりやや良いが前年比低下。前年は 69% とする出典)。「Azure と M365 商用クラウドの効率化を、AI インフラ投資と AI 製品の利用増が上回った」。次四半期は約 64% とする AI 要約があるが**未確認** | [W8-04] | 3* |
| Microsoft(再掲) | FY2025 69%、FY2026 66%、FY2026 Q4 65% | [W1] 再掲 | 1* |
| Microsoft の「AI 容量の粗利率が低く、効率化で改善する」という会社の直接説明 | **見つからず**(欠損)。見つかったのは、Azure AI サービス(OpenAI 推論など)は低利益率で自社 AI と GPU を取り合う、という単一の調査会社の見解のみ(会社開示ではない) | — | [W8-16] | 4* |
| Google Cloud | 2026 Q1 | 売上 $20.0B(+63%)、営業利益 $6.6B、率 33.0%(算出。要約は約 33%、前年 18%) | [W8-23] | 3* |
| Google Cloud | 2026 Q2(2026-07 下旬) | 売上 $24.768B(+81.8%、算出)、営業利益 $8.814B、率 35.6%(算出: 8.814 ÷ 24.768)、前年同期 20.7%(算出: 2.826 ÷ 13.624)。増分営業利益率 53.7%(算出) | [W8-05][W8-23] | 3* |
| Google Cloud の理由 | CFO Ashkenazi は売上増の要因として「中核 GCP、企業向け AI、AI インフラ」を挙げた。「売上の伸びが費用の伸びを大きく上回った(営業レバレッジ)」は要約者の推論で、会社の定量説明は**欠損**。今後は減価償却とデータセンター運営費(電力)が利益を圧迫し続ける、第三者の容量を使う Q3 は「小幅な利益率の圧力」、Wiz 買収費用も。TPU システムを顧客のデータセンターへ販売する収益を初めて計上 | 2026-07 | [W8-05][W8-23] | 3* |
| Google の耐用年数 | サーバー・ネットワーク機器は約 6 年 | 2026 年 | [W8-23] | 3* |
| AWS | 2026 Q2(2026-07-30) | Jassy: 「AI 事業は中核事業と同じ利益率の軌道で、やや先行」。理由として効率化、容量の最適化、固定費の管理。「利益率は変動し得る」。AI が利益率を押し下げているか、という質問に「今のところ押し下げていない」 | [W8-06] | 3* |
| AWS | 2026 年 Q2 までの説明 | Jassy: 「AWS は設備を先に買う。需要が速く伸びるほどデータセンター・チップ・ハードウェアが要る。AI チップは CPU チップよりずっと高い。その資産は何年も使える」。「中核 AWS の初期と同じパターンを見込む」「推論が最適化され稼働率が上がると価格は正常化する」。AI インフラの最大費用はデータセンターとチップで、時間とともに安くなる見込み | [W8-18] | 3* |
| AWS の AI 単独の営業利益率の数字 | **欠損** | — | — | — |

### 2-4. 同じ期間(2026 年 4〜6 月、Oracle のみ別期間)の利益率の並置

| 会社・事業 | 指標 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|---|
| AWS | 営業利益率 | 39.3% | 2026 Q2 | [W1][W8-06] | 1*/3* |
| Google Cloud | 営業利益率 | 35.6% | 2026 Q2 | [W8-05] | 3* |
| Microsoft Cloud | 粗利率(営業利益率ではない) | 65% | FY2026 Q4(~06-30) | [W1] | 1* |
| CoreWeave | 調整後営業利益率 / GAAP 営業利益率 / 調整後 EBITDA 率 | 5.0% / −1.9% / 58.6% | 2026 Q2 | [R7][W8-10] | 1*/3* |
| Oracle(全社) | 非 GAAP 営業利益率 | 42% | Q1 FY27(2026-06〜08) | [W5] 再掲 | 3* |
| Oracle(AI 容量) | 調整後粗利率(納入済み容量) | 32%(ガイダンス 30%)。会社の目標: 契約期間通算で 30〜40% | Q3 FY26(2025-12〜2026-02) | [W5] 再掲 | 3*(原典 1*) |
| 算出(差) | AWS − CoreWeave(調整後)/ AWS − CoreWeave(GAAP) | 39.3 − 5.0 = 34.3pt / 39.3 − (−1.9) = 41.2pt(算出) | 2026 Q2 | 算出 | — |

注: 指標の定義が揃わない(営業利益率、粗利率、調整後)。期間も Oracle だけ異なる。

### 2-5. 契約の長さを示す指標(受注残 ÷ 年換算売上、算出)

| 会社 | 受注残 | 年換算売上(直近四半期 × 4) | 倍率(算出) | 注 | 出典 |
|---|---|---|---|---|---|
| AWS | $496B(2026 Q2) | $168.8B(42.2 × 4) | 2.9 倍 | 期間の分布は非開示 | [W8-15][W1] |
| Oracle | RPO $664B(Q1 FY27) | $77.2B(19.3 × 4) | 8.6 倍 | RPO は全社(ソフトウェア等を含む)。OpenAI 向けが過半([R5] 再掲) | [W8-17][R5] |
| CoreWeave | $104B(2026-06-30、[R7]) | $10.3B(2.575 × 4) | 10.1 倍 | 受注残の定義は会社による | [R7][W8-10] |

---

## 3. 識者・調査会社の見方

### 3-1. 見解の一覧(要約経由。本文は未読)

| 発信者 | 内容 | 根拠として示された数値 | 時点 | 出典 | Tier |
|---|---|---|---|---|---|
| Stratechery(Ben Thompson)| 「利益はモジュラーな(コモディティ化した)部分から離れ、統合された(差別化された)部分に流れる」。2026-07 の記事で「コモディティ市場では利益率は優れた費用構造から生まれ、先頭のモデル提供者がその優位を持つと見込む」。「Agents Over Bubbles」(2026-03): エージェントの台頭を理由に「バブルではない。設備投資は正当化される。Anthropic と OpenAI は以前より堅固」。ハイパースケーラーの設備投資は供給を大きく上回る需要への対応と述べる。Oracle について(2025-09): OpenAI 中心の RPO で株価が急騰、「大きなリスクだが Oracle は活かす位置にある」。別記事は「AI 契約に負債が必要で、AI バブルの転換点になり得る」。2026-03 の決算評価は「AI の波に乗り、強い位置」 | 数値は要約に出ず | 2025-09〜2026-07 | [W8-22] | 3*(記事本文未読。検索結果の 1 件は日付が誤っている旨の注記) |
| SemiAnalysis | 2-2 節。「売り手市場の希少な容量であり、コモディティのスポット市場ではない」という解説あり | H100 1 年指数 $1.70 → $2.35 | 2025-10〜2026-03 | [W8-08] | 3*〜4* |
| Morgan Stanley(Brian Nowak チーム)| 3 つの枠組み。**ハイパースケーラーの GPU リース ROIC 約 31%**(前提: GB300 $8.50/時、稼働率 75%、増分 EBIT 率 約 67%)/ **自社インフラの API サービス 約 46%** / **第三者計算の API 約 25%**。「トークン価格が 1 百万トークン $1 未満(オープンソースとの競争や価格競争)、または稼働率 70% 未満で営業利益率と ROIC が急速に消える」。見方は「安いトークンは需要を拡大し、単価が下がっても総利益を増やす」(2026-08-15 の Amazon・Alphabet の Overweight 再確認)。リスク指標は GPU 供給の正常化とオンプレへの回帰 | ROIC の幅は報道で 25〜40%、25〜50%、31/46/25% と割れる | 2026-07〜08 | [W8-11] | 3*(原文未確認) |
| Bernstein(Rasgon)| 2-2 節。$4/時が基準になり得る | CoreWeave の EBITDA 増 約 $1.2B | 2026-04 | [W8-11] | 4* |
| McKinsey | 2-2 節。14〜16% | 同左 | 日付不明 | [W8-07] | 3* |
| a16z | 「LLMflation」(2024): 固定の性能の価格は約 10 倍/年、3 年で約 1,000 倍(100 万トークン当たり $60 → $0.06)の下落。**a16z 自身の記事は取得できず、二次ブログ経由**。a16z のインフラ利益率に関する見解は欠損 | 約 10 倍/年(a16z とされる)、Epoch の中央値 約 50 倍/年(引用元不明)[再掲 W3: 9〜900 倍/年の幅] | 2024〜2026 | [W8-14] | 4* |
| Contrary Research | 表題「Why 20% of neoclouds won't survive the AI boom」。本文・数値は要約に出ず | 欠損 | 日付不明 | [W8-07] | 4(表題のみ) |
| Creative Strategies | 表題「Neoclouds vs hyperscalers: a shift from access to platform」。本文・数値は要約に出ず | 欠損 | 日付不明 | [W8-07] | 4(表題のみ) |
| Pebblous 分析(Together AI)| 「モデル層がコモディティ化すると、その下の層に資金が流れる」(単一ブログの主張。利益率データなし) | なし | 2026 年 | [W8-14] | 4* |
| Piper Sandler / Wolfe / UBS | 1-5 節 | ROIC・設備投資 | 2026 年 | [W8-15] | 3* |

### 3-2. 推論の比率とトークン価格

| 項目 | 内容 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| 推論の比率(計算量) | 約 3 分の 2(Deloitte TMT Predictions 2026 の引用。2023 年は約 3 分の 1)。Macquarie の引用では 2025 年に半分 | 2026 | [W8-21] | 4*(同一の予測の転載が多く独立の確認ではない) |
| 推論の比率(支出) | 2026 年に AI 最適化インフラ支出の 55%(Gartner の引用)、2029 年に 65% 超 | 2026〜2029 | [W8-21] | 3*〜4* |
| 推論 vs 学習 | 推論が CY2024 に並び CY2025 に上回った(Futurum)。CY2030 の基本シナリオで推論 71.7%・学習 28.3% | 2024〜2030 | [W8-21] | 3*(プレスリリース) |
| モデルの生涯コスト | 推論 80〜90%、学習 10〜20%(ベンダー・ブログの推計) | — | [W8-21] | 4* |
| **Oracle / OCI の推論と学習の実績比率** | **欠損**(Ellison の「推論市場は学習市場より遥かに大きい」(2025-09、[W5] 再掲)は市場予測で OCI の実績ではない) | — | — | — |
| トークン価格の下落と GPU 時間単価の上昇が同時に起きている事実 | トークン価格(同じ性能)は年 10〜50 倍の速度で下落(上記)。H100 の 1 年契約指数は 2025-10 → 2026-03 に +38.2%(算出: 2.35 ÷ 1.70 − 1)([W2] 再掲)。両者の関係(推論需要の拡大が上回っているか)を示す定量資料は欠損 | 2025-10〜2026-03 | [W8-14][W2] | 3*〜4* |

### 3-3. 「AWS の形成要因」と「現在の AI 側」の事実の並置(評価は書かない)

| AWS で観察される事実 | AI インフラ側で観察される事実 | 出典 |
|---|---|---|
| 値下げを繰り返した。S3 −84.7%(2006→2016、算出)。2025-06 に H100 インスタンス −44% | 2025-10〜2026-08 に GPU 時間単価は上昇(H100 1 年指数 +38%)、CoreWeave は 2026-07 に約 25% 値上げの報道。一方トークン単価は下落 | [W8-01][W8-08][W2][S3] |
| 自社チップ: Graviton が新規 CPU の過半。Trainium で推論の営業利益率に数百 bp の優位(見込み) | Oracle の自社設計 GPU/チップは今回の検索では確認できず(欠損)。CoreWeave は NVIDIA GPU の購入と記述([W2]) | [W8-02][W8-06] |
| 設備投資の大半を自己資金で賄う。ただし 2026 Q2 の Amazon 全社 FCF は約 −$7.6B | Alphabet の FCF は会社史上初の負([W3] 再掲)。CoreWeave の純支払利息は売上の 24.9%(2026 Q2)。Oracle の FY26 FCF −$23.7B | [W8-15][W3][R7][S1] |
| 転送料・相互運用性が切替を制約(CMA 認定)。それでも AWS は約束により 180 日以上の免除 | GPU 貸しの乗り換えコスト(移行の費用、学習済みデータの移動、ソフトの互換)を示す資料は欠損。契約期間は 5〜6 年(再掲 [S4]) | [W8-09][S4] |
| 上位サービス(Bedrock など)で選択肢・ガバナンス・セキュリティを訴求。売上比は非開示 | Oracle: マルチクラウド DB 売上 +353%(Q1 FY27)、本番稼働の AI エージェント 2,300 超(再掲 [W6])。OCI の上位サービスの売上比は欠損 | [W8-06][W6] |
| 営業利益率: 2014 年 10.0%、2015 年 19.1%、2016 年 25.5%(売上 +72%、+54% の局面) | CoreWeave: 売上 +112%(2026 Q2)の局面で調整後営業利益率 5.0%、会社見通しで Q4 に 10% 台前半 | [W1][W8-10] |

---

## 4. Oracle の位置

### 4-1. 直近の実績と構成(Q1 FY27、2026-06〜08、発表 2026-09-10)

| 項目 | 値 | 出典 | Tier |
|---|---|---|---|
| 総売上 | $19.3B(+30%) | Oracle 決算プレスリリース [W8-17] | 1* |
| クラウド合計 | $11.6B(+62%)。売上比 60.1%(算出: 11.6 ÷ 19.3) | [W8-17] | 1* |
| クラウドインフラ(IaaS) | $7.4B(+121%、定率 +120%)。売上比 38.3%(算出: 7.4 ÷ 19.3)、クラウド合計比 63.8%(算出: 7.4 ÷ 11.6) | [W8-17] | 1* |
| クラウドアプリ(SaaS) | $4.2B(+10%)。売上比 21.8%(算出: 4.2 ÷ 19.3) | [W8-17] | 1* |
| ソフトウェア売上 | $5.55B(−3%)(第三者の分析) | [W8-17] | 3* |
| 非 GAAP EPS | $1.92(前年 $1.47、+30%) | [W8-17] | 3* |
| RPO | $664B(前年比 +$209B) | [W8-17] | 1* |
| 共同 CEO Magouyrk | 「顧客は新規契約を結び、**高い価格で容量を更新し、フリートをほぼ満稼働で使っている**」 | Futurum の要約 [W8-17] | 3* |
| 更新の数値(再掲) | 更新期の GPU は従来契約比 +20% で更新または再販、過半は 4 年以上前、稼働率 97.9% | [W5][W2] 再掲 | 3* |
| 営業CF / capex / FCF(再掲) | $23.1B / $28.5B / −$5.4B(6 四半期連続の負) | [S1][S2] 再掲 | 1* |

### 4-2. 「AI 容量の顧客が DB・アプリ・AI サービスも買っている証拠」

| 確認できたこと | 確認できなかったこと |
|---|---|
| Q3 FY26(2026-03-10): Magouyrk は「AI の採用が DB のクラウド需要を押し上げる。顧客は新しい AI 機能を使いたく、データをエージェントと同じ場所に置く必要がある」と説明。マルチクラウド DB 売上 +531%、AI インフラ売上 +243%、「両方とも需要が供給を上回る」 [W8-12] Tier 3* | **同一顧客が AI インフラ(GPU 容量)と DB・アプリを併せて契約している件数・金額・比率: 欠損** |
| マルチクラウド DB 売上の前年比: +1,529%(Q1 FY26)→ +817% → +531% → +404% → +353%(Q1 FY27)、顧客数 +180%(Q1 FY27)。絶対額は欠損([R4][W6] 再掲) | AI 容量の大口顧客(OpenAI 等)が Oracle DB を使っているという会社開示: 欠損 |
| 本番稼働の AI エージェント 2,300 超(前期比 +90%)、実行 350 万回超(Q1 FY27、[W6] 再掲 Tier 3*) | Oracle AI Database 26ai の採用数・売上・顧客数: **欠損**([W8-24]。OCI で 2025-10、オンプレで 2026-01 に提供開始。ベクトル検索など AI 機能は追加費用なし([W6] 再掲)。エージェントはデータベース内で動く設計。これらは製品の説明で、採用の証拠ではない) |
| OpenAI 以外の受注残が過去 1 年で 2 倍超、Q1 FY27 に新規 $30B 超([W5] 再掲、金額は二次報道) | OCI の上位サービス(Generative AI サービス、Data Platform 等)の売上・比率: **欠損** |
| パートナークラウド内のリージョン: Microsoft 33、Google 14、AWS は Q4 FY26 末に 22 を予定(Q3 FY26 の説明) [W8-12]。Q1 FY27 に合計 70 リージョン・119 AZ([W6] 再掲) | 推論 vs 学習の比率: **欠損**(4-3) |

### 4-3. 推論比率と上位サービス

- OCI の推論と学習の実績比率: 会社開示なし(欠損)。市場全体の比率は 3-2 節(推論は計算量の約 3 分の 2 とする予測が複数、独立の確認ではない)。
- 利益率の区分(再掲 [W5]): FAM(2025-10-16)で非 GAAP 粗利率 エンタープライズ 65〜80%、分散クラウド(マルチクラウド)40〜60%、AI インフラ 30〜40%。マルチクラウド DB の粗利率を Magouyrk が 60〜80% と述べたとする二次報道もある([R4] 再掲、T3、出典確認不能)。

### 4-4. 「SaaS で稼いだ現金で長期契約を引き受けられる」ことの材料

| 項目 | 値 | 時点 | 出典 | Tier |
|---|---|---|---|---|
| FY26 営業CF / capex / FCF | $32B(+54%)/ $55.7B / −$23.7B | FY26(~2026-05-31) | [S1] 再掲 | 1* |
| Q1 FY27 | 営業CF $23.1B / capex $28.5B / FCF −$5.4B。純現金 capex 約 $18B | 2026-06〜08 | [S1][S2] 再掲 | 1*/3* |
| FY27 capex 見通し | 総額 $90〜95B、純額 約 $70B(顧客の前払い等を控除) | 2026-09-10 | [W3] 再掲 | 1* |
| 顧客からの前払い | 「重要な金融要素を含む前払い」$11.4B(Q1 FY27、前年同期ゼロ)。前払い・顧客持込(BYOH)の累計 $75B([W5] 再掲)。**この前払いが営業CFに含まれるかどうかの分類は未確認** | Q1 FY27 | [W5] 再掲 | 1* |
| 支払利息 | FY25 $3,578M → FY26 $4,599M → Q1 FY27 $1,428M(前年同期 $923M)。Q1 FY27 の売上比 7.4%(算出: 1,428 ÷ 19,300)。CoreWeave の 2026 Q2 は 24.9% | — | [R5][R7] 再掲 | 1*/3* |
| 未開始リース約束(Oracle の 10-K) | **約 $260B**(2026-05-31)。ほぼすべてがデータセンター関連、開始は FY27 Q1〜FY29、期間 15〜19 年。貸手の借入に対する**最大 $3.3B の保証**を含むリースがある(借入は 2026-09 満期、貸手名は非開示) | 2026-05-31 | [W8-13] | 1* |
| 同 | 約 **$288B**(2026-08-31 の 10-Q)。前年同期(2025-08-31)は **$99.8B**(第三者の分析)。増加倍率 2.9 倍(算出: 288 ÷ 99.8) | 2026-08-31 | [W8-13] | 1*/3* |
| 認識済みのリース負債 | $37.89B。未開始約束($260B)は約 6.9 倍(算出: 260 ÷ 37.89)。未開始約束は割引前で、負債に単純加算できない | 2026-05-31 | [W8-13] | 3* |
| 別の数字 | Bloomberg Tax の題名に「$248 billion rent」(日付・基準は要約に出ず) | 日付欠損 | [W8-13] | 3 |
| 契約期間とリース期間の並置 | 顧客契約は OpenAI 5 年(WSJ)、FAM 例示 6 年([S4] 再掲)。リース 15〜19 年(10-K)。Oracle は「リースの期間・更新条件・価格が顧客契約と一致しない可能性」をリスクとして開示 | — | [S4][W8-13] | 1*/3* |
| 格付 | S&P BBB-(2026-07-09 に BBB から引下げ、安定)/ Moody's Baa2(ネガティブ)/ Fitch BBB(安定)。S&P は未開始リース $260B を調整後負債の予測に算入、FY27 の調整後レバレッジ 約 4.4 倍 | 2026-07〜08 | [R5][S4] 再掲 | 3* |
| CDS(5 年) | 約 227bp(2026-09-25、単一の小規模媒体) | 2026-09-25 | [R5] 再掲 | 3* |
| CoreWeave の資金調達 | 無担保債 9.750%(2031)・9.625%(2032)。GPU 担保ローン DDTL 4.0 は SOFR+2.25%(Moody's A3)。Oracle の同満期の新発債は 4.988% で、差 約 4.8pp(算出) | 2026-03〜06 | [R7] 再掲 | 1* |
| 比較: 他社の FCF | Amazon 全社 2026 Q2 約 −$7.6B(AWS の設備投資を含む全社)。Alphabet は会社史上初の負 | 2026-07 | [W8-15][W3] | 3* |
| **リース調達における Oracle の信用力の寄与(貸手の資金調達コスト、スプレッド)** | **欠損**(開発業者の資金調達コストの資料は出ず)。「投資適格の信用がオフバランスのリースを可能にする」という因果を述べた資料も見つからず | — | [W8-13] | — |

### 4-5. Oracle の市場シェア(再掲 [R3])

- IaaS の市場シェア(Gartner、2024): Amazon 37.7%、Microsoft 23.9%、Google 9.0%、Alibaba 7.2%、Huawei 4.1%。Oracle は上位 5 社に入らない(= 4.1% 未満、算出)。
- Synergy(2026 年 4〜6 月、市場 $143B): Amazon 28%、Microsoft 20%、Google 15%。Oracle は成長の速い「第 2 グループ」で、シェア値は要約に出ない。

---

## 5. 食い違い(どちらも採らず併記)

| # | 項目 | A | B | 備考 |
|---|---|---|---|---|
| 1 | AWS の値下げ回数 | 40 回(Computerworld、2012 年頃)/ 62 回(2017 年) | 約 30 回(2016 年の記事) | 範囲(全サービスか一部か)が異なる可能性。現在までの累計は欠損 [W8-01] |
| 2 | S3 の下落率 | AWS の記述「10 年で 80%」 | 算出 −84.7%(0.15 → 0.0230)。アイルランド版は −87.2%(0.18 → 0.023) | 地域・階層の違い。AWS の「80%」は丸めの可能性 [W8-01] |
| 3 | AWS 2026 Q2 の営業利益率 | 39.3%(算出)/ 39.4%(別の要約)/ 39%(CFO) | 36.8%(CNBC、[W1] 再掲) | 派生商品の 1 回限り利益の扱いで +650bp(含む)と +520bp(除く)が併存 [W6][W1] |
| 4 | AWS 自社チップ事業の規模 | $20B 超(Q1 2026) | $25B 超(Q2 2026) | 時点の違いの可能性。「Trainium 事業」と「自社チップ全体」の範囲の違いも否定できない [W8-06] |
| 5 | Microsoft FY26 Q2 の粗利率 | 全社 68% | Microsoft Cloud 67% | 指標が異なる可能性。FY26 Q3 の前年比較も 69% とする出典のみ [W8-04] |
| 6 | Microsoft FY26 Q4 | 次四半期ガイド 約 64%(AI 要約、未確認) | 実績 65%([W1] 再掲) | ガイドと実績の違い |
| 7 | Alphabet の利益率 | Cloud Q1 2026 約 33% | 全社 36.1%(Q1 の別の記載)。別の要約は全社 34%(前年 32%)、営業利益 $31.3B → $40.8B と記す | 事業と全社の区別。34% と $31.3B → $40.8B は整合しない(未解決)[W8-05][W8-23] |
| 8 | Google Cloud の利益率上昇の理由 | 売上増(+82%)による営業レバレッジ(要約者の推論) | 減価償却・電力・第三者容量・Wiz の費用は今後の圧力(会社の発言) | 費用側の定量説明は欠損 [W8-05][W8-23] |
| 9 | CoreWeave の Q2 売上 | $2,575M([R7]) | $2.58B / $2.6B | 丸め [W8-10] |
| 10 | CoreWeave の粗利率 | 売上原価ベース 71.7%(FY2025、算出)/ 65.9%(2026 Q2、集約サイトの算出) | 会社報告の粗利率は未取得 | 技術・インフラ費用(減価償却を含むと見られる)を除いた値。定義は未確認 [W8-03][W8-10] |
| 11 | H100 の価格の方向 | ピークから 60〜75% 下落(ブログ)。2026 年平均 $3.61(集約サイト) | SemiAnalysis の 1 年指数は 2025-10 → 2026-03 に +38% | 系列の定義と時点が異なる。スポットと長期契約で逆方向の記述もある [W8-07][W8-08][W8-14] |
| 12 | Blackwell 世代の時間単価 | Morgan Stanley の前提 GB300 $8.50/時 | Ornn Blackwell 指数 $4.08(2026-04-13)、Silicon Data B200 $5.66(2026-08-02)、Bernstein の「$4/時が基準」 | SKU(GB300 と B200)、契約形態、定義が異なり直接比較不能 [W8-11][W2] |
| 13 | Morgan Stanley の ROIC | 25〜40% | 25〜50%、または 31%/46%/25% | 報道ごとに範囲が異なる。原文未確認 [W8-11] |
| 14 | Microsoft の egress 免除 | 実施していないとする報道 | 実施を発表したとする報道 | 報道時点の違いの可能性 [W8-20] |
| 15 | 推論の比率 | 計算量の約 3 分の 2(2026、Deloitte 引用) | 支出の 55%(Gartner 引用)。2025 年に半分(Macquarie 引用)。CY2025 に学習を上回る(Futurum) | 計算量と支出、年の違い。転載が多く独立性は低い [W8-21] |
| 16 | Oracle のリース約束の額 | $248B(Bloomberg Tax の題名) | $260B(10-K、2026-05-31)/ $288B(10-Q、2026-08-31) | 日付・基準が異なる可能性。未開始約束は割引前 [W8-13] |
| 17 | Oracle の「更新の価格」 | 「高い価格で更新」(Futurum の要約) | +20% のプレミアム([W5]、複数媒体)/ CoreWeave は「元の価格の 95% で再契約」(CNBC 報道、日付不明、[W2] 再掲) | 会社・世代・契約が異なる。Oracle の更新のみの単価は非開示 |

---

## 6. 欠損と試した検索語

| # | 欠損項目 | 試した検索語(今回) | 備考 |
|---|---|---|---|
| 1 | AWS の営業利益率の要因分解(規模・チップ・上位サービス・値下げの寄与) | 「Jassy AI infrastructure margins early AWS days...」「AWS return on invested capital estimate...」 | 分解した資料なし |
| 2 | AWS の現在の S3 標準単価、値下げの累計回数 | 「AWS price reductions history number of price cuts since 2006...」 | 2016〜2017 年の記事のみ |
| 3 | Nitro の原価低減額・率 | 「AWS Nitro System offload hypervisor James Hamilton cost per server...」 | 起源と時期のみ。Hamilton の講演・論文の数字は出ず |
| 4 | Graviton の独立ベンチマーク、収益への寄与額 | 「Graviton Nitro AWS cost advantage share of new CPU capacity...」 | AWS の主張のみ |
| 5 | AWS 単独の ROIC、AWS の回収期間 | 「AWS return on invested capital estimate AWS ROIC analysts capex payback...」 | Amazon 全社の ROIC(Piper)のみ |
| 6 | AWS のサービス別売上(コンピュート・ストレージ・DB・上位サービス) | 同上 | 開示なし |
| 7 | AWS の AI 事業・Bedrock 単独の営業利益率 | 「Jassy AWS AI business margins Trainium Bedrock operating margin earnings call 2026」 | 「中核と同じ軌道」の定性のみ |
| 8 | 乗り換えコストの金額、データの重力に関する顧客調査 | 「AWS free data transfer out when leaving AWS 2024... data gravity switching cost cloud customers survey lock-in percent」 | 政策と規制の事実のみ |
| 9 | CoreWeave の FY2025 通期の調整後営業利益・支払利息、会社報告の粗利率、減価償却費 | 「CoreWeave 2025 full year results cost of revenue...」「CoreWeave Q2 2026 results gross margin...」 | 集約サイトの売上原価のみ |
| 10 | CoreWeave 以外のネオクラウド(Nebius・Lambda 等)の利益率 | 今回は未検索(上限のため) | 既存 [R7] に Nebius の一部あり |
| 11 | ネオクラウドの粗利率の一次情報(McKinsey の 14〜16% の原典) | 「Stratechery Ben Thompson AI infrastructure commodity...」「SemiAnalysis neocloud GPU rental commodity margins TCO...」 | McKinsey 内の「一部の報告」という二次引用 |
| 12 | Microsoft の「AI 容量の粗利率が低く、効率化で改善する」という会社の直接説明、Azure AI の粗利率 | 「Amy Hood AI gross margin...」「Nadella fungible fleet token factory Azure AI margin...」 | 全社・Microsoft Cloud の粗利率と一般的な説明のみ |
| 13 | Google Cloud の利益率上昇理由の会社の定量説明 | 「Google Cloud operating margin rose despite AI capex depreciation reason...」「Alphabet Google Cloud operating income increase driven by revenue growth...」 | 10-Q の MD&A の文言は出ず |
| 14 | Stratechery の記事本文(AWS 型かコモディティかの論点) | 「Stratechery Ben Thompson...」(2 回、うち 1 回は stratechery.com に限定) | 表題と要約のみ |
| 15 | Bernstein の原文、a16z の原文(インフラ利益率) | 「Bernstein OR Morgan Stanley analyst AI infrastructure commoditization...」「a16z GPU cloud commoditization...」 | 低信頼の媒体・二次ブログのみ |
| 16 | 推論 vs 学習の Nvidia・Epoch・Morgan Stanley の推計 | 「inference share of AI compute demand 2026 percent...」 | Deloitte・Gartner・Futurum の引用のみ |
| 17 | OCI の推論比率、OCI の上位サービスの売上・比率 | 「Oracle OCI inference vs training mix Magouyrk...」「Oracle Q1 fiscal 2027 results cloud infrastructure revenue OCI growth non-AI customers...」 | 開示なし |
| 18 | AI 容量の顧客が DB・アプリ・AI サービスも買っている証拠 | 「Oracle AI customers database co-located data AI agents Autonomous AI Database 26ai...」 | 製品説明と成長率のみ。顧客重複データなし |
| 19 | Oracle AI Database 26ai の採用数・売上 | 同上 | 欠損 |
| 20 | リース調達に対する Oracle の信用力の寄与、開発業者の資金調達コスト | 「Oracle data center lease commitments developers Vantage Related Digital financing cost investment grade credit...」 | リース約束の額と保証のみ |
| 21 | Oracle の IaaS の市場シェアの最新値 | 今回は未検索([R3] 再掲のみ) | — |
| 22 | 契約更新時の価格の一次データ(Oracle の更新のみの単価、CoreWeave の「95%」の日付) | 今回は未検索([W2] で試行済み) | — |

---

## 7. 出典一覧

出典 ID は検索番号(24 回)。1 回の要約が複数サイトを統合しているため、数値と URL の対応は特定できない場合がある。Tier は本文の各行を参照。

- **[W8-01]** AWS の値下げの歴史: https://aws.amazon.com/blogs/aws/aws-storage-update-s3-glacier-price-reductions 、https://www.architecting.it/?p=508 、https://www.computerworld.com/article/1387541/amazon-moves-to-next-generation-compute-instances.html 、https://comparethecloud.net/news/10-years-aws-emea 、https://www.computerfellows.com/2016/12/amazon-web-services-lowers-storage-prices/ 、https://www.telecoms.com/public-cloud/aws-melts-glacier-prices-to-continue-race-to-the-bottom 、https://www.journaldunet.com/cloud/1188411-amazon-web-services-continue-de-casser-ses-prix/ 、https://datahub.io/technology/cloud-providers-pricing
- **[W8-02]** Graviton: https://www.businesswire.com/news/home/20251203228412/en/AWS-Introduces-Graviton5%E2%80%94the-Company%E2%80%99s-Most-Powerful-and-Efficient-CPU 、https://www.sec.gov/Archives/edgar/data/1018724/000110465926041034/tm263815d3_ex99-1.htm 、https://www.marketscreener.com/news/aws-introduces-graviton5-the-company-s-most-powerful-and-efficient-cpu-ce7d51dfd089f624 、https://www.lemondeinformatique.fr/actualites/lireamp-les-commandes-d-instances-graviton-et-trainium-explosent-chez-aws-99909.html 、https://xenospectrum.com/en/amazon-ec2-cpu-capacity/
- **[W8-03]** CoreWeave FY2025: https://app.edgar.tools/companies/CRWV 、https://weissratings.com/en/stock/crwv-nasdaq/income-statement/quarterly 、https://www.theenergymag.com/news/market-news/core-weave-reports-full-year-2025-revenue-of-5-1-billion 、https://www.verdict.co.uk/coreweave-q4-2025-results/ 、https://www.datacenterdynamics.com/en/news/coreweave-expects-capex-in-q4-2025-to-exceed-previous-three-quarters-combined/ 、https://bitcoinminingstock.io/earnings/calls/CRWV/q4-fy2025
- **[W8-04]** Microsoft の粗利率: https://www.fool.com/earnings/call-transcripts/2026/01/28/microsoft-msft-q2-2026-earnings-call-transcript/ 、https://www.fool.com/earnings/call-transcripts/2026/04/29/microsoft-msft-q3-2026-earnings-transcript/ 、https://www.fool.com/earnings/call-transcripts/2025/10/29/microsoft-msft-q1-2026-earnings-call-transcript 、https://www.moomoo.com/community/feed/microsoft-q3-fy2026-earnings-conference-call-116490123870213
- **[W8-05]** Google Cloud 2026 Q2: https://thenextweb.com/news/alphabet-q2-2026-capex-205bn-cloud-82 、https://xenospectrum.com/en/alphabet-cloud-ai-capex-returns/ 、https://www.fierce-network.com/cloud/google-cloud-surges-alphabets-ai-capex-problem-grows 、https://www.datacenterdynamics.com/en/news/google-increases-2026-capex-195-205bn-as-it-accelerates-ai-data-center-buildout/ 、https://www.futuriom.com/articles/news/google-raises-capex-wall-street-sells/2026/07
- **[W8-06]** Jassy・AWS 2026 Q1/Q2: https://www.gurufocus.com/news/8993599/ 、https://www.tikr.com/blog/amazon-beat-q1-2026-earnings-on-every-line-the-bigger-story-is-the-chip-business-inside-aws 、https://www.webpronews.com/amazons-hidden-chip-empire-20-billion-run-rate-fuels-aws-ai-surge/ 、https://vectorshift.ai/research/companies/amazon-com/earnings/2026-q1
- **[W8-07]** ネオクラウド(McKinsey 等): https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-evolution-of-neoclouds-and-their-next-moves 、https://research.contrary.com/report/why-20-of-neoclouds-wont-survive-the-ai-boom 、https://creativestrategies.com/research/neoclouds-vs-hyperscalers-a-shift-from-access-to-platform/ 、https://www.trendingtopics.eu/neoclouds-challenge-the-hyperscalers-in-big-bets-on-ai-infrastructure/ 、https://theheatformula.beehiiv.com/p/the-100-billion-moat
- **[W8-08]** SemiAnalysis: https://newsletter.semianalysis.com/p/ai-neocloud-playbook-and-anatomy 、https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity 、https://www.itiger.com/news/1185188896 、https://cryptobriefing.com/nvidia-h100-gpu-rental-costs-surge/ 、https://spendark.com/blog/cloud-gpu-price-war-2026/ 、https://measuredai.substack.com/p/neoclouds-ai-middle-layer
- **[W8-09]** 英 CMA: https://www.steptoe.com/en/news-publications/stepahead-antitrust-and-competition-insights/uk-competition-and-markets-authority-accepts-voluntary-commitments-to-address-cloud-market-concerns.html 、https://digitalpolicyalert.org/event/38888-competition-and-markets-authority-published-commitments-by-amazon-web-services-and-microsoft-to-reduce-egress-fees-and-improve-interoperability-in-uk-cloud-markets 、https://www.techradar.com/pro/google-microsoft-and-aws-trade-blame-as-uk-watchdog-investigates-cloud-competition
- **[W8-10]** CoreWeave 2026 Q2: https://quartr.com/events/coreweave-inc-crwv-q2-2026_F6huCJA4 、https://www.marketbeat.com/instant-alerts/coreweave-q2-earnings-call-highlights-2026-08-11/ 、https://beancount.io/blog/2026/09/22/coreweave-fy2026-q2-earnings-analysis 、https://dashboard.channelchek.com/?p=104902 、https://www.indmoney.com/blog/us-stocks/crwv-stock-jumps-coreweave-q2-earnings-analysis
- **[W8-11]** Morgan Stanley・Bernstein: https://www.kucoin.com/news/flash/morgan-stanley-ai-infrastructure-roic-reaches-up-to-46-cloud-vendors-maintain-overweight-rating 、https://newsable.asianetnews.com/markets/amzn-googl-msft-ai-capex-plans-why-morgan-stanley-says-the-spending-will-pay-off-articleshow-i14bz6v 、https://stockwirex.com/?p=37816 、https://tech-insider.org/nvidia-blackwell-gpu-rental-price-surge-ornn-index-2026/ 、https://www.webpronews.com/morgan-stanley-spots-ai-money-shift-hyperscalers-poised-to-steal-spotlight-from-chip-stocks/ 、https://www.edgen.tech/news/post/morgan-stanley-urges-buying-ai-infrastructure-dip-after-7-slide
- **[W8-12]** Oracle Q3 FY26 の説明: https://www.marketbeat.com/instant-alerts/oracle-q3-earnings-call-highlights-2026-03-10/ 、https://www.oracle.com/a/ocom/docs/corporate/financial-analyst-meeting-2025-magouyrk.pdf 、https://www.techloy.com/oracle-reports-strongest-growth-since-2009-as-ai-infrastructure-revenue-surges/ 、https://ceointerviews.ai/quote/multicloud-database-revenue-grew-531-yearoveryear-ai-infrastructure-MTA1MzgwNg/
- **[W8-13]** Oracle のリース: https://www.sec.gov/Archives/edgar/data/0001341439/000119312526277521/orcl-20260531.htm 、https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm 、https://www.sec.gov/Archives/edgar/data/1341439/000119312526101045/orcl-20260228.htm 、https://www.hudson-labs.com/research/oracle-data-center-leases-orcl 、https://news.bloombergtax.com/financial-accounting/oracles-248-billion-rent-is-next-ai-bombshell-chris-bryant 、https://mtsobserver.substack.com/p/oracles-commercial-real-estate-problem 、https://www.datacenterdynamics.com/en/news/oracle-denies-openai-data-center-delays/
- **[W8-14]** トークン価格・GPU 価格の二次情報: https://voxbooster.com/blog/ai-inference-cost-statistics-2026 、https://blog.pebblous.ai/blog/together-ai-neocloud-8-3b-valuation/en/ 、https://deploybase.ai/articles/gpu-cloud-pricing-war-who-is-winning-in-2026 、https://www.traeai.com/articles/3c264537-5f40-4862-94df-44be8264c964(a16z「Intelligence is getting cheaper」の AI 要約)
- **[W8-15]** AWS の ROIC・設備投資: https://www.tikr.com/blog/amazon-is-spending-220-billion-this-year-the-aws-numbers-suggest-its-worth-it 、https://www.tmgm.com/en-eu/analysis/market-insight/wolfe-amazon-price-target-255-aws-ai-growth 、https://www.newsquawk.com/headlines/sell-side-on-amazon-amzn-shares-hit-as-another-mega-cap-name-hikes-fy26-capex-although-revenue-beat-expectations 、https://media.quilter.com/search/2026/amazon-bets-on-going-big-or-going-home-and-the-market-doesnt-like-it/ 、https://nasdaq.com/articles/should-you-worry-about-trend-amazon-1-metric-offers-compellingly-clear-answer
- **[W8-16]** Microsoft(Nadella・Hood): https://www.fool.com/earnings/call-transcripts/2025/10/29/microsoft-msft-q1-2026-earnings-call-transcript 、https://siliconangle.com/2026/02/01/microsoft-investors-fret-capital-spending-azure-growth-decouple/ 、https://futurumgroup.com/insights/microsoft-q2-fy-2026-cloud-surpasses-50b-azure-up-38-cc 、https://www.globaldatacenterhub.com/p/microsoft-q1-fy2026-the-35-billion 、https://www.crnasia.com/news-network/2025/microsoft-q1-earnings-ceo-nadella-says-fungible-asset-stra(URL は検索結果で途中までの表示)
- **[W8-17]** Oracle Q1 FY27: https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/ 、https://futurumgroup.com/insights/oracle-q1-fy-2027-ai-infrastructure-contracts-convert-into-growth/
- **[W8-18]** Jassy の AI 投資の説明: https://www.mobileworldlive.com/ai-cloud/amazon-ceo-talks-ai-investments/ 、https://cloudwars.com/innovation-leadership/amazon-sets-world-record-for-capex-spending-and-ceo-andy-jassy-is-delighted/ 、https://techcrunch.com/?p=2992158
- **[W8-19]** Nitro: https://semiconductor.substack.com/p/on-the-origins-of-aws-custom-silicon 、https://www.datacenterdynamics.com/en/news/aws-takes-on-colo-providers-with-bare-metal-instances/ 、https://hidekazu-konishi.com/entry/aws_history_and_timeline_aws_silicon.html 、https://www.weka.io/article/get-more-out-of-aws-custom-silicon
- **[W8-20]** egress 免除: https://www.techradar.com/pro/aws-follows-google-cloud-drops-egress-fees-when-moving-data-out-of-its-system 、https://www.infoq.com/news/2024/03/aws-egress-fees/ 、https://fierce-network.com/data-center/aws-ditches-egress-fees-customers-who-leave 、https://computing.co.uk/news/4182204/aws-scraps-egress-fees-for-cloud-migration 、https://cloudzero.com/blog/aws-egress-costs
- **[W8-21]** 推論の比率: https://metavert.io/ai-inference-vs-ai-model-training 、https://www.macquariedatacentres.com/blog/from-training-to-inference-the-quiet-shift-redrawing-the-ai-map/ 、https://futurumgroup.com/?p=93565 、https://fourweekmba.com/qualcomm-inference-fabric-inference-shift
- **[W8-22]** Stratechery: https://stratechery.com/2026/agents-over-bubbles/ 、https://stratechery.com/2026/frontier-overhangs/ 、https://stratechery.com/2025/oracle-pops-from-databases-to-ai-oracle-and-openai/ 、https://stratechery.com/company/oracle/ 、https://stratechery.com/2025/tech-philosophy-and-ai-opportunity/
- **[W8-23]** Alphabet(Google Cloud): https://www.tikr.com/blog/alphabet-stock-hits-109-9b-in-q1-revenue-as-cloud-tops-20b-for-first-time 、https://www.cnhinews.com/news/article_e3220c1b-dca0-5369-ae1d-54f65c6ea076.html 、https://fool.com/investing/2026/07/30/alphabet-will-spend-as-much-as-205-billion-this-ye 、https://parameter.io/alphabet-googl-earnings-preview-can-ai-spending-and-profitability-coexist/ 、https://xenospectrum.com/en/alphabet-cloud-ai-capex-returns/
- **[W8-24]** Oracle AI Database 26ai: https://blogs.oracle.com/database/oracle-announces-oracle-ai-database-26ai 、https://infoworld.com/article/4072128/oracle-targets-agentic-use-cases-with-ai-database-26ai.html 、https://futurumgroup.com/the-no-compromise-ai-foundation-oracle-reimagines-the-database-for-the-agentic-era-3/ 、https://www.datavail.com/blog/oracle-ai-database-26ai-evolving-enterprise-data-and-ai/

既存調査(再掲元):
- [W1] `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research3/W1_cloud_margin_history.md`
- [W2] `.../research3/W2_gpu_economic_life.md`
- [W3] `.../research3/W3_industry_structure.md`
- [W5] `.../research3/W5_oracle_ai_economics.md`
- [W6] `.../research3/W6_database_at.md`
- [R3] `.../research2/R3_competition.md`、[R4] `.../research2/R4_database_at.md`、[R5] `.../research2/R5_credit.md`、[R7] `.../research2/R7_capital_power.md`
- [S1] `.../research/S1_management_scenario.md`、[S2] `.../research/S2_market_hypothesis.md`、[S3] `.../research/S3_scuttlebutt.md`、[S4] `.../research/S4_core_variables.md`
