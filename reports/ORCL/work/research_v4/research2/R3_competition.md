# R3: Oracle の「価格」と「品質」の競合比較と、その差が出るバリューチェーン上の活動(Oracle / NYSE: ORCL)

作成日: 2026-10-12 / 担当: 株式調査アシスタント(事実・数値・出典の整理と、出典間の食い違いの指摘のみ。投資判断は含まない)
前提: 決算期末は5月31日。最新の報告済み四半期は Q1 FY2027(2026-08-31 終了、2026-09-10 発表)。

---

## 0. 読み方と制約(先に読むこと)

1. **取得手段は WebSearch の要約のみ。28 回を使い切った**(すべて standard。extended は 0 回)。WebFetch は使えず、Oracle の価格表・SLA 文書・Gartner の MQ 本文・SemiAnalysis の ClusterMAX 本文は**一度も直接読めていない**。数値はすべて「検索要約に書かれていた内容」である。
2. **Tier**: 1=会社開示・決算説明会、2=規制当局・格付会社・公的統計、3=報道・アナリスト・調査会社、4=ブログ・SNS・販促ページ・ライセンス助言会社。`*` は「一次書類・公式ページだが検索要約経由でしか見ていない(要原典確認)」を意味する。Oracle 自身の PR・ブログは Tier 1 とするが、**自社に有利な前提の販促・自己評価**であり、独立した検証ではない。
3. **価格の注意**: 掲載価格は「定価(オンデマンド)または第三者の集計」で、顧客の実支払額ではない。大口契約・確約割引は交渉による。価格比較の第三者記事の多くは Tier 4(販促・ライセンス助言会社・競合のブログ)で、同じ SKU でも出典で数値が割れる(5 節に一覧)。
4. **「(算出)」は調査者の計算**で式を併記した。会社や第三者の主張ではない。
5. **出典 ID**: `[C01]`〜`[C23]` は本書 6 節の一覧(今回の検索)。`[既S1]` `[既S2]` `[既S3]` `[既S4]` は `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research/` の既存調査、`[既R2]` は `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research2/R2_products_5w1h.md`、`[既H3]` は `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/data/H3_obligations.md`。重複調査は避け、既存の数値は再掲に留めた。
6. **検索要約の性質**: 1 回の検索要約は複数サイトを統合して書かれ、個々の数値がどの URL 由来かを特定できない場合が多い。その場合は出典 ID を「URL 群」に付け、本文に「個別の URL は特定できず」と書いた。
7. 欠損は「欠損」と書き、試した検索語は 7 節に残した。英語の発言は和訳主体。

---

## 1. 事実要約(10 行。評価・推奨は含まない)

1. **GPU の定価**: OCI の H100 は 1 GPU 時 $10.00(別資料 $10.75)。AWS(2025 年 6 月の値下げ後)$6.88 の 1.45 倍、CoreWeave $6.16 の 1.62 倍、Google Cloud $11.06 の 0.90 倍(算出)。GB200 は OCI $16.00 が CoreWeave $10.50 の 1.52 倍、Azure $27.04 の 0.59 倍(算出)。**GPU で OCI が最安とする出典は見つからなかった**(いずれも Tier 4)。
2. **GPU 以外の定価**: 汎用計算・ブロックストレージ・データ転送は OCI が大幅に安い。2 vCPU・8GB の月額は OCI $38.69 に対し AWS・Azure $70.08(OCI は 44.8% 安い。算出)、ブロック容量単価は gp3 の約 32%(算出)、外向き通信は月 10TB 無料+$0.0085/GB で、月 50TB なら AWS の 1/12.6(算出)。いずれも Tier 4 で、世代・性能条件が揃っていない。
3. **Oracle DB の持込(BYOL)**: OCI は x86 で「1 Processor ライセンス = 2 OCPU(= 4 vCPU)」、AWS・Azure は「2 vCPU = 1 Processor ライセンス」。同じ物理コア数なら OCI は必要ライセンスが半分(算出)。Google Cloud の扱いは出典が割れる。
4. **規模の主張**: OCI Supercluster は最大 131,072 基の Blackwell GPU(2024-09)、Zettascale10 は最大 80 万基(2025-10、2026 年後半提供予定。GA は未確認)。いずれも Oracle の発表値。MLPerf への OCI の提出は最大 128 GPU(Training v4.0、Oracle ブログ)にとどまる。
5. **第三者の GPU クラウド評価**: SemiAnalysis ClusterMAX は、v2.0(2025-11)も v3.0(2026-09-23)も Oracle は Gold(要約経由、Tier 3〜4)。Platinum は v2.0 で CoreWeave のみ、v3.0 で CoreWeave と Nebius。
6. **SLA**: OCI Compute は 99.99%(AD 冗長)/ 99.95%(FD 冗長)/ 99.9%(単一)。AWS EC2 は 99.99%(複数 AZ)/ 99.5%(単一)、Azure VM は 99.99%(ゾーン)/ 99.95%(可用性セット)/ 99.9%(単一)。Autonomous Database は 99.995%(Data Guard 有効)/ 99.95%(無効)で、計画メンテナンスを含む。いずれも契約上の返金条件であり、実績ではない。
7. **Gartner**: Strategic Cloud Platform Services の MQ(2025 年版)は Oracle が 3 年連続で Leader(Oracle の発表)。Cloud DBMS の MQ(2024 年版、2025-01 発表)も Leader。2026 年版の Oracle の位置は未確認。IaaS の市場シェア(2024、Gartner)は Amazon 37.7%・Microsoft 23.9%・Google 9.0%・Alibaba 7.2%・Huawei 4.1%で、**Oracle は上位 5 社に入らない**(= 4.1% 未満。算出)。
8. **シェアの別の見方**: Synergy(2026 年 4〜6 月期、市場 $143B)は Amazon 28%・Microsoft 20%・Google 15%。Oracle は成長の速い「第 2 グループ」に分類され、シェア値は要約に出ない。前年(2025 年 7〜9 月期)は Oracle 3.1%(+1pt)。Oracle 自身の IaaS 売上から算出した比率(3.8%〜5.9%、3 通り。3-6 節)とは定義・期間が違い、一致しない。
9. **DBMS**: Gartner のランキングは 2022 年以降 AWS、Microsoft、Oracle、Google、IBM の順(2025 年分まで)。市場規模は 2024 年 $119.7B(+13.4%)。Oracle は「ゆっくり侵食されている」(Register、2026-04-21)。Oracle 単独の 2024・2025 年の DBMS 売上とシェアは欠損。
10. **バリューチェーン**: 裏付けの数字があるのは**資金調達と DC 保有の構造**(顧客前払い・持込 $75B、確保容量の 90% 超がパートナー資金、未開始リース $288B)と**マルチクラウドの成長率**。一方、**価格・品質の差を生む原価の数字**(1MW あたりの建設費、リース料率、電力単価、仮想化による売れる計算量の増分)は見つからなかった。

---

## 2. 価格比較表

共通の注: 価格は米ドル、オンデマンド定価(米国リージョン)が基本。OCI の 1 OCPU は x86 で 2 vCPU([C05]、Oracle の説明)。

### 2-1. 汎用計算(vCPU 時間単価)

| 項目 | OCI | AWS | Azure | Google Cloud | 出典 / Tier |
|---|---|---|---|---|---|
| 公表単価(OCPU 時) | E5.Flex $0.03/OCPU 時+メモリ $0.002/GB 時。E4.Flex $0.025(別資料は約 $0.048。食い違い)。Arm A1 $0.01 | 欠損(型名つきの単価は今回出ず) | 欠損 | 欠損 | [C05] T4、[既R2] §3② T4 |
| vCPU 時あたり(算出) | E5: $0.03 ÷ 2 = **$0.015**。E4: $0.025 ÷ 2 = $0.0125 | 2 vCPU・8GB が月 $70.08 → $70.08 ÷ 730 時 = $0.096/時 → $0.048/vCPU 時(型名は出典に記載なし) | 同左($70.08) | 月 $71.90 → $0.0985/時 → $0.049/vCPU 時(算出: 71.90 ÷ 730 ÷ 2) | [C05] T4 |
| 2 vCPU・8GB の月額(第三者比較、型名不明) | **$38.69** | $70.08 | $70.08 | $71.90 | [C05] Finout T4 |
| OCI の差(算出) | 1 − 38.69 ÷ 70.08 = **44.8% 安い**(Finout 本文は「45%」) | — | — | 1 − 38.69 ÷ 71.90 = 46.2% 安い | 算出 |
| Oracle・助言会社の主張 | 「AWS より最大 50% 低い」(Oracle の主張)。「30〜50% 安い」(第三者ガイド) | — | — | — | [C05] T1(販促)/T4 |

**注意**: (a) Finout の OCI $38.69 は、E5.Flex の単価から算出した 1 OCPU+8GB の月額 $33.58((0.03 + 0.002 × 8) × 730)と一致しない。世代・リージョン・時間数の前提が出典に書かれていない。(b) AWS・Azure・GCP の型名が出典に無く、世代差(旧世代 vs 新世代)の影響を除けない。(c) 確約割引(Savings Plans、Reserved、Universal Credits)後の価格は未取得。

### 2-2. GPU インスタンス(1 GPU 時あたり、オンデマンド定価)

| GPU | OCI | AWS | Azure | Google Cloud | CoreWeave | Nebius | 実勢指数(Silicon Data、2026-08-02) |
|---|---|---|---|---|---|---|---|
| H100 | **$10.00**($80/ノード時、8GPU 裸金属)。別資料 $10.75 | **$6.88**(p5.48xlarge $55.04/時 ÷ 8。2025-06 の値下げ前は $98.32/時 = $12.29/GPU)。別資料に「約 $3.90」の記述あり(食い違い) | **$6.98**(NC40ads_H100_v5 単体、East US)。別資料に ND96 の 8GPU $98.32/時($12.29/GPU)があるが AWS の旧価格と同額で転記誤りの疑い。別の記述は $40〜56/時(= $5.0〜7.0/GPU) | **$11.06**(a3-highgpu-8g $88.49/時 ÷ 8)。別資料 $10.98($87.83/時)。さらに別の記述は $44〜64/時(= $5.5〜8.0/GPU) | **$6.16**($49.24/ノード時 ÷ 8)。スポット $2.46。2026-07 に約 25% 値上げの報道([既S3])。上記の値が値上げ前後どちらかは不明 | **$2.00**(13 社比較)/ **$2.95**(安定したオンデマンドの目安)/ **$3.85**(競合ブログ)。プリエンプティブ $2.15 | ハイパースケーラー中央値 **$7.19**、ネオクラウド **$2.80**([既S3]) |
| H200 | **$10.00**($80/ノード時)。別資料 約 $12.25([既R2]) | 欠損 | 欠損 | 欠損 | 欠損 | $4.50(プリエンプティブ $2.45。2026-06 の第三者比較) | $3.16 |
| B200 | **$14.00**($112/ノード時、[既R2]) | 欠損 | 欠損 | 欠損 | 欠損 | 欠損 | $5.66。別の指数は $2.12〜6.04(提供者・契約期間で幅) |
| GB200 | **$16.00**($64/4GPU 時) | 掲載なし | **$27.04**($108.16/4GPU 時。スポットも同額) | 掲載なし | **$10.50**($42.00/4GPU 時) | 個別交渉(非公表) | 欠損(GB200/GB300 は信頼できる指数なし。[既S3]) |
| 出典 / Tier | [C03][既R2] T4 | [C04] T4 | [C02][C03] T4 | [C02][C04] T4 | [C02][C03] T4 | [C02][C03] T4 | [既S3] T3(Silicon Data を二次記事が引用) |

**算出(OCI 定価と他社の比)**

| # | 内容 | 式 | 結果 |
|---|---|---|---|
| a | H100: OCI ÷ AWS | 10.00 ÷ 6.88 | 1.45 倍 |
| b | H100: OCI ÷ CoreWeave | 10.00 ÷ 6.16 | 1.62 倍 |
| c | H100: OCI ÷ Google Cloud | 10.00 ÷ 11.06 | 0.90 倍 |
| d | H100: OCI ÷ Azure(単体 VM) | 10.00 ÷ 6.98 | 1.43 倍 |
| e | H100: OCI ÷ Nebius | 10.00 ÷ 3.85、10.00 ÷ 2.00 | 2.60〜5.00 倍 |
| f | H100: OCI ÷ ハイパースケーラー中央値、ネオクラウド指数 | 10.00 ÷ 7.19、10.00 ÷ 2.80(10.75 の場合 1.50、3.84) | 1.39 倍、3.57 倍 |
| g | GB200: OCI ÷ CoreWeave、OCI ÷ Azure | 16.00 ÷ 10.50、16.00 ÷ 27.04 | 1.52 倍、0.59 倍 |
| h | AWS の値下げ幅 | (98.32 − 55.04) ÷ 98.32 | 44.0%(Spheron の「約 44%」と整合) |

**事実要約**
- 定価ベースで OCI の GPU は、AWS(値下げ後)・CoreWeave・Nebius より**高く**、Google Cloud(H100)・Azure(GB200)より**低い**。「OCI の GPU は他社より安い」という主張を支える定価データは今回の検索では見つからなかった。
- OCI の実際の大口契約単価は非開示([既S4]、[既R2])。会社が示す価格関連の数字は、更新時の「従来契約比 +20%」(Q1 FY27)と、契約期間通算の粗利率 30〜40%(6 年・$60B の例で 35%)である([既S1][既S4])。
- H100 の実勢はネオクラウド $2.80 とハイパースケーラー $7.19 で 2.6 倍の開きがあり、OCI の定価はそのどちらよりも高い([既R2] §4 項目 11 と同旨)。
- 出典の信頼度: GPU 価格の集計サイトの多くは日付なし・方法論なしで、競合(Spheron は GPU レンタル事業者)のブログも含む。

### 2-3. データ転送(外向き通信、egress)

| 項目 | OCI | AWS | Azure | Google Cloud | 出典 / Tier |
|---|---|---|---|---|---|
| 月間無料枠 | **10TB**(OCI テナンシーあたり、標準サービスの一部) | 100GB(全 AWS サービス合算) | 100GB(請求アカウントあたり) | Standard Tier のみリージョン・SKU あたり 200GiB(出典間で階層と無料枠の記述が割れる) | [C01] T4 |
| 従量単価($/GB) | **約 $0.0085**(無料枠超過分) | 約 $0.09(最初の 10TB)、約 $0.085(次の 40TB) | 約 $0.087(最初の 10TB) | Premium 約 $0.12(最初の 1TB)、Standard 約 $0.085 | [C01] T4 |
| 付随費用 | 欠損 | NAT Gateway の処理料 $0.045/GB、AZ 間通信 $0.01/GB | 欠損 | 欠損 | [C01] T4 |

**算出(月間の外向き通信料。1TB = 1,000GB と仮定、無料枠控除は OCI のみ、他社の 100GB 無料枠は無視)**

| 月間転送量 | OCI | AWS | Azure | 比(AWS ÷ OCI) |
|---|---|---|---|---|
| 10TB | (10,000 − 10,000) × 0.0085 = **$0** | 10,000 × 0.09 = $900(100GB 無料を引くと $891) | 10,000 × 0.087 = $870 | OCI は無料 |
| 20TB | 10,000 × 0.0085 = $85 | 10,000 × 0.09 + 10,000 × 0.085 = $1,750 | 欠損(次の帯の単価なし) | 20.6 倍 |
| 50TB | 40,000 × 0.0085 = **$340** | 10,000 × 0.09 + 40,000 × 0.085 = **$4,300** | 欠損 | **12.6 倍** |

- 超過後の単価だけを比べると AWS $0.09 ÷ OCI $0.0085 = 10.6 倍(算出)。
- 要約自身が「OCI の 10TB 無料枠が全サービスに適用されるかは確認していない」「公式価格表と照合していない」と注記している。1TB の定義(1,000GB か 1,024GB)も未確認。

### 2-4. ブロックストレージ

| 項目 | OCI | AWS EBS gp3 | Azure Premium SSD | Google | 出典 / Tier |
|---|---|---|---|---|---|
| 容量単価($/GB 月) | 約 **$0.0255**(Block Volume。オブジェクト・ストレージ標準も約 $0.0255) | **$0.08** | 約 **$0.12** | 欠損(「OCI は Google より定価で 75〜85% 安い」とする 1 社の記述のみ) | [C06] T4、[既R2] §3② |
| 性能の扱い | 出典が割れる。(i)「基準の 10 VPU/GB が追加料金なしで含まれ gp3 並み」/(ii)「既定は約 2 IOPS/GB・最大 3,000 IOPS、Balanced(10 VPU)は +$0.0017/GB 月」/(iii)「VPU は 1 VPU・GB・月あたり $0.0015〜0.002」 | gp3 の基準は 3,000 IOPS・125MB/s | 欠損 | 欠損 | [C06] T4 |
| Oracle の自社比較 | 「gp3(100GB・6K IOPS)より 82% 安い」 | — | — | — | [C06] Oracle の経済性ページ(販促、日付 2024-06-05、検索結果は転載サイト経由)T1(販促)* |

**算出**: OCI ÷ gp3(容量単価のみ)= 0.0255 ÷ 0.08 = 0.319 → **68.1% 安い**。OCI ÷ Azure Premium SSD = 0.0255 ÷ 0.12 = 0.2125 → 78.8% 安い。Oracle の「82%」は性能条件(6K IOPS)込みで、VPU の扱いが出典で割れるため再現できなかった。

### 2-5. Oracle DB のライセンスを他社クラウドで使う場合の条件(BYOL)

| 環境 | 数え方(Processor ライセンス) | 補足 | 出典 / Tier |
|---|---|---|---|
| **OCI(x86)** | **1 ライセンス = 2 OCPU**(Oracle のコア係数表の記述) | 1 OCPU は 1 物理コア(= 2 vCPU)なので、1 ライセンスは 2 コア = 4 vCPU(算出) | [C07] Oracle 係数表 PDF T1* |
| **OCI(Ampere Arm)** | 1 ライセンス = 4 OCPU | — | [C07] T1* |
| **AWS(EC2・RDS)・Azure** | **2 vCPU = 1 ライセンス**(ハイパースレッド有効)。無効なら 1 vCPU = 1 ライセンス。**コア係数表は適用されない** | 1 ライセンスは 1 物理コア(2 vCPU)。AWS はハイパースレッド既定有効、Azure は無効との記述あり(1 社)。Standard Edition は AWS・Azure とも 16 vCPU まで、SE2・SE One は 8 vCPU まで(Oracle の現行方針と要約が記述。原文未確認) | [C09] T1*/T4、[C07] T4 |
| **Google Cloud** | **出典が割れる**。(a) 助言会社 1 社: Oracle の「認可クラウド環境」リストに GCP は無く、オンプレ規則(物理ホスト全体、コア係数表を適用)。(b) 別の要約: 新しい版の方針に GCP が認可環境として載る | 原文未確認。**結論は保留** | [C07] T4、[C09] T4 |
| **オンプレ / 認可外クラウド** | コア係数表(x86 は一般に 0.5)を適用。係数表そのものは今回取得できず | 本調査では未確認 | — |

**算出(同じ物理コア数で必要なライセンス数)**: OCI(x86)は 1 コアあたり 0.5 ライセンス(1 ÷ 2)、AWS・Azure は 1 コアあたり 1.0 ライセンス(2 vCPU ÷ 2 vCPU)。同じコア数なら OCI は必要ライセンスが半分。サポート料(ライセンス額の年 22% との記述、[既R2] §3⑫)も同じ比率で減る(推論。実際の保有ライセンスと契約条件に依存)。

**Autonomous Database(ECPU 課金)の BYOL**

| 項目 | 内容 | 出典 / Tier |
|---|---|---|
| 現行 FAQ の要約 | ADW・ATP の License Included $0.336/ECPU 時。**BYOL $0.0807/ECPU 時**。BYOL は Enterprise Edition の Processor ライセンス 1 個あたり**最大 8 ECPU** | [C08] Oracle ECPU FAQ T1* |
| 旧 FAQ(2023 版)の要約 | ADW $0.25、ATP $0.67 / ECPU 時。BYOL は ADW $0.06、ATP $0.1608。1 ライセンスあたり**最大 4 ECPU** | [C08] T1* |
| 助言会社の数字(矛盾) | 2026 年の ADW・ATP は License Included $1.34、BYOL $0.336 | [C08] T4 |
| Database@Azure の Autonomous(Exadata 上) | License Included $1.55〜1.80、BYOL $0.52〜0.65 /ECPU 時(別製品・別クラウド) | [C08] T4 |
| Exadata Database Service | ECPU の BYOL / License Included の SKU がある。数字は今回取得できず。Oracle のページは AWS・Azure・Google 上でも OCI と同じ価格と説明([既R2] §3⑤⑥) | [C08] T1* |

**算出**: BYOL の値引き率 = 1 − 0.0807 ÷ 0.336 = **76.0%**(License Included は BYOL の 4.16 倍)。旧 FAQ の 1 ライセンス 4 ECPU から現行 8 ECPU への変化は、要約の記述どおりなら 1 ライセンスで使える ECPU が 2 倍になったことを意味する(原文未確認)。

**食い違い**: [既R2] §3④ は同じ FAQ から「$0.0807 = JSON・APEX の価格」と記載したが、今回の要約は「$0.0807 = ADW・ATP の BYOL 価格」と記述する。同一 PDF の読み方が割れており、原典で確認が必要。

---

## 3. 品質比較表

### 3-1. GPU クラスタの規模とネットワーク

| 項目 | Oracle(OCI) | 競合 | 出典 / Tier |
|---|---|---|---|
| 単一クラスタの最大規模(2024-09 発表) | **最大 131,072 基の Blackwell GPU、最大 2.4 zettaFLOPS**。「Frontier の 3 倍超、他のハイパースケーラーの 6 倍超」(Oracle の主張。比較表は競合を CSP 1〜3 と匿名化。「UltraClusters」列は 20,000 基の H100 / 20,736 基の GB200 と記載。どの社かは特定できない) | AWS・Azure・CoreWeave の最大クラスタ規模は今回取得できず(欠損) | [C13] T1/T3 |
| Zettascale10(2025-10-14 発表) | **最大 80 万基の NVIDIA GPU、最大 16 zettaFLOPS(ピーク)**。複数 DC をまたぐ構成。Acceleron ネットワーク。Abilene で最初に展開。注文受付中、**2026 年後半提供予定(GA は未確認)** | 欠損 | [C13][既R2] §3① T1*/T3 |
| 規模の比(算出) | 800,000 ÷ 131,072 = 6.1 倍(GPU 数)。16 ÷ 2.4 = 6.7 倍(ピーク性能)。数値精度(FP4 等)の前提は要約に記載なし | — | 算出 |
| ネットワーク方式 | RoCEv2(ConnectX-7 NIC / ConnectX-8 SuperNIC)または Quantum-2 InfiniBand。Zettascale10 は RoCEv2 系の Acceleron | 欠損 | [C13] T1 |
| 「非ブロッキング(oversubscription なし)」 | 第三者ガイドが「全ノード間が最小の遅延・オーバーサブスクリプションなし」と記述。ベンチマークの引用なし | 欠損 | [C14] T4 |
| off-box 仮想化 | Gen2 は仮想化(ストレージ・ネットワーク)をサーバー外の専用ハード(Cloud Control Computer)に出す。後継の Acceleron Converged NIC はホスト NIC と CCC を 1 チップに統合。**Oracle 自身が「off-box 方式ではパケットが実質二度処理され、帯域と効率に限界が生じる」と認めている**(FAQ の要約) | 欠損 | [C14] T1 |
| 稼働規模の主張 | Magouyrk 共同 CEO: Abilene の SuperCluster は「約 20 万基の NVIDIA GPU」、クラウドリージョンは稼働 147・開発中 64(いずれも Techstrong の要約。日付不明) | — | [C23] T3 |
| Abilene の稼働(既存調査) | 最初の 2 棟で 200MW 超が稼働(Oracle の 2026-03 声明)。Q1 FY27 に 850MW・30 万基超の GPU を納入(四半期) | — | [既S3][既S4] |

### 3-2. ベンチマーク

| 項目 | Oracle(OCI) | 競合 | 出典 / Tier |
|---|---|---|---|
| MLPerf 提出歴(Oracle ブログ) | Inference v3.1(H100)、Training v4.0(H100 を 8 基・64 基、H200 を 128 基)、Inference v5.0(BM.GPU.H200.8 = H200 8 基)。Oracle の自己評価は「競合と同等以上」「線形にスケール」 | AWS・Azure・Google・CoreWeave・Nebius の提出との比較は取得できず(欠損) | [C12] T1 |
| GB200 / 2026 年の OCI 提出 | **検索で見つからず** | — | [C12](検索結果に無し) |
| 提出規模と主張規模の差(算出) | 提出の最大は 128 GPU(Training v4.0)。主張は 131,072 GPU → 131,072 ÷ 128 = **1,024 倍** | — | 算出 |
| SemiAnalysis ClusterMAX v1(2025-04) | CoreWeave が首位。Oracle の階級は今回取得できず | CoreWeave Platinum | [C15] T3 |
| ClusterMAX v2.0(2025-11、Hedgehog の要約) | **Gold: Oracle**、Crusoe、Nebius、Azure、Together AI、LeptonAI。Platinum は CoreWeave のみ | 84 社を評価(前回 26 社) | [C15] T4 |
| ClusterMAX v3.0(2026-09-23) | **Gold: Oracle と Google Cloud**(イタリア語要約。直接の表は未確認)。Azure は Silver、Crusoe は Bronze | **Platinum: CoreWeave と Nebius**。77 社評価、メダル付与は 19 社。評価基準は 10 項目、5 段階(Platinum / Gold / Silver / Bronze / Underperforming) | [C15] T3/T4 |

### 3-3. SLA(契約上の保証。実績ではない)

| サービス | OCI | AWS | Azure | 出典 / Tier |
|---|---|---|---|---|
| 計算(VM) | AD 冗長 **99.99%** / FD 冗長 **99.95%** / 単一インスタンス **99.9%**(Oracle SLA ページの要約。表が一部文字化け) | リージョン(複数 AZ)**99.99%** / 単一インスタンス **99.5%**(2026 年の比較記事) | 単一 VM(Premium SSD)**99.9%** / 可用性セット **99.95%** / 可用性ゾーン **99.99%** | [C10] T1*、[C11] T4 |
| 性能の保証 | Compute performance **99.9%**、Network performance は「90% 超の性能を 99.9% の時間」(Oracle SLA ページの要約)。Oracle は「可用性・管理性・性能」の 3 本柱と主張 | EC2・Azure VM に計算性能の SLA は見つからず(古い Columbia 大の資料。Tier 4) | 同左 | [C10] T1*、[C11] T4 |
| Autonomous Database | **99.995%**(Autonomous Data Guard 有効時)/ **99.95%**(無効時)。計画メンテナンスを含む。99.995% は月約 132 秒(Oracle 文書)、99.95% は約 22 分(算出: 30 日 × 24 × 60 × 0.0005 = 21.6 分) | 欠損(DB の SLA は未検索) | 欠損 | [C10] T1 |

**食い違い**: (a) OCI の VM を 99.9% とする比較サイトと、99.99%(マルチ AD)/ 99.9%(単一)とする別の表がある。(b) Oracle 作成の PDF は Dedicated Region の可用性を 99.95% と記載。この 99.95% が公開リージョンの SLA かは確認できていない。

### 3-4. 障害の実績

| 日付 | 事象 | 出典 / Tier |
|---|---|---|
| 2026-01-13 | 米 SouthWest1(Phoenix)で 1 時間 23 分。Lessonly(OCI 上の SaaS)のステータスページ。Oracle は OCI 基盤の問題を解決と説明 | [C16] pingoru T4 |
| 2026-01 下旬 | OCI London で「揺らぎ」。読者の報告では Fusion 本番が約 10 分未満落ち、その後低速。Oracle のステータスページに障害の記載なし、会社はコメントせず | [C16] Register(2026-01-28)T3 |
| 2026-03-23 | OCI Pod1 で検索サービスの障害 1 時間 30 分(RFPIO のステータスページ) | [C16] T4 |
| 2026-06-08 | Amsterdam で Oracle 関連の接続問題、30 分未満で復旧(1 社の報告) | [C16] T4 |
| 2025-05 | 欧州で約 6 時間の障害。OCI の ID 基盤に影響、Frankfurt から Amsterdam へのフェイルオーバーが失敗(DCD)。月・日は要約に無い | [C16] T3 |
| 日付不明 | 「Oracle Cloud と NetSuite が世界規模で障害」(Techzine)。年月は要約に無く、2026 年の事象か未確認 | [C16] T3 |

- 2026 年について、複数時間に及ぶリージョン全体の障害として確認できたものは**なかった**(検索 1 回)。報告されたのは 10 分〜1.5 時間の短い事象で、出所の多くは OCI 上の SaaS 事業者のステータスページ(Tier 4)。
- **競合の障害実績との比較は今回行っていない**(検索枠の制約)。したがって「OCI の障害が多い / 少ない」を判断する材料はない。

### 3-5. アナリスト評価(Gartner)

| 評価 | Oracle の位置 | 競合の位置 | 出典 / Tier |
|---|---|---|---|
| Magic Quadrant: Strategic Cloud Platform Services(2025 年版。Gartner 報告書の日付 2025-08-04、Oracle の発表 2025-08-08) | **Leader(3 年連続)**。Oracle は「200 超の AI・クラウドサービスをエッジ・顧客 DC・マルチクラウド・パブリッククラウドで提供できる唯一のハイパースケーラー」と主張(Oracle の意見) | AWS・Microsoft・Google の 2025 年の位置は今回の要約に無い(欠損) | [C17] T1 |
| 同(2026 年版) | **Oracle の位置は未確認**。AWS が 2026 年版で Leader と告知している事実のみ確認 | AWS: Leader(AWS の告知) | [C17] T1(AWS) |
| Magic Quadrant: Cloud Database Management Systems(2024 年版、Oracle の発表 2025-01-21) | **Leader**。Oracle は「統合データベース構造、革新の速さ、マルチクラウド」が評価されたと主張(Oracle の説明。Gartner の文言ではない) | 他社の位置は要約に無い(欠損) | [C18] T1/T3 |
| 同(2025 年版以降) | **見つからず** | — | [C18] |
| 縦軸・横軸の座標(実行力・ビジョンの完全性) | **欠損**(MQ 本文は有料。いずれも未読) | — | — |

### 3-6. 市場シェア

**IaaS**

| 出典 | 対象期間 | 市場規模 | Amazon | Microsoft | Google | Oracle | 出典 / Tier |
|---|---|---|---|---|---|---|---|
| Gartner(IaaS 公開クラウド、2025-08-06 発表) | 2024 暦年 | $171.8B(+22.5%) | 37.7% | 23.9% | 9.0%(Alibaba 7.2%、Huawei 4.1%) | **上位 5 社に入らない**。「その他」は $30.8B(17.9%)。Oracle の値は要約に無い。上位 5 社の第 5 位が 4.1% なので Oracle は 4.1% 未満(算出) | [C19] T3 |
| Gartner(2024-07-22 発表) | 2023 暦年 | 欠損(伸び率 16.2%) | 欠損 | 欠損 | 8.2%(第 3 位に浮上)。上位 5 社の合計 82% | 欠損 | [C19] T3 |
| Synergy(CIO Dive の要約) | 2025 年 7〜9 月 | $107B | 欠損 | 欠損 | 欠損 | **3.1%**(+1pt、7 四半期連続で上昇。要約は「cloud and software share」と記述しており、定義は要確認) | [C22] T3 |
| Synergy | 2026 年 1〜3 月 | $129B(年換算 $500B 超) | 欠損 | 欠損 | 欠損 | 欠損 | [C21] T3 |
| Synergy | 2026 年 4〜6 月 | $143B(+43%、8 年ぶりの高成長) | **28%** | **20%** | **15%**(3 社計 63%。算出: 28 + 20 + 15) | **シェア値は要約に無い**。成長の速い「第 2 グループ」(CoreWeave、OpenAI、Oracle、Crusoe、Nebius、Anthropic、Nscale)に分類。ネオクラウド 9 社が上位 40 に入る | [C21][既R2] §3① T3 |
| Canalys / Omdia | 2026 年 | **取得できず** | — | — | — | — | — |

**Oracle 自社の IaaS 売上との照合(算出。定義・期間が一致しない)**

| 内容 | 式 | 結果 |
|---|---|---|
| Q2 FY26(〜2025-11)の IaaS $4.1B ÷ Synergy 2025 年 7〜9 月の市場 $107B | 4.1 ÷ 107 | 3.8%(Synergy の 3.1% は 3.1% × 107 = $3.3B に相当。差 $0.8B) |
| Q1 FY27(〜2026-08)の IaaS $7.4B ÷ Synergy 2026 年 4〜6 月の市場 $143B | 7.4 ÷ 143 | 5.2%(期間が 2 か月ずれる) |
| FY25 の IaaS 約 $10.2B([既R2] §1 の算出)÷ Gartner 2024 年の市場 $171.8B | 10.2 ÷ 171.8 | 5.9%(Gartner の「4.1% 未満」と矛盾。会計年度のずれと、Oracle の IaaS 区分に DB クラウドサービス等が含まれる可能性による) |

**DBMS**

| 出典 | 内容 | 出典 / Tier |
|---|---|---|
| Gartner(2024 年、要約) | 市場規模 **$119.7B(+13.4%)**。クラウドが支出の 64%、オンプレが 36%(算出: クラウド $76.6B、オンプレ $43.1B) | [C20] T3 |
| Gartner のランキング(2011〜2025、Register 2026-04-21) | **AWS、Microsoft、Oracle、Google Cloud、IBM の順が 2022 年以降続く**。Gartner の Ronthal: 2011 年の首位グループ(Oracle・IBM・Microsoft・SAP)で、15 年間にシェアを伸ばしたのは Microsoft のみ。Oracle は「ゆっくり侵食されている」(Register の表現) | [C20] T3 |
| Gartner 2023 年(itmarketstrategy の要約) | AWS $27.2B、Microsoft 約 $25B、Google は初めて $10B 超。**Oracle は +4.5% で、Microsoft との差が $7.3B、Google との差が $7.5B** | [C20] T3 |
| 算出(2023 年の Oracle) | Microsoft 約 $25B − $7.3B = 約 $17.7B。Google $10B 超 + $7.5B = $17.5B 超。→ **約 $17.5〜17.7B**。2023 年市場 = $119.7B ÷ 1.134 = 約 $105.6B。→ Oracle シェア **約 16.6〜16.8%** | 算出(桁の目安。Gartner 本表の値ではない) |
| Oracle の 2024・2025 年の DBMS 売上とシェア | **欠損**(Gartner 本表は有料) | — |
| IDC の DBMS シェア | **欠損** | — |

---

## 4. バリューチェーン上の活動 × 効果 × 証拠

「会社・報道が挙げる理由」を活動別に並べ、どの数字・事実が裏付けか、何が裏付けになっていないかを分けた。**証拠の強さ**は、A=会社開示 T1/規制当局 T2 の数字で、価格または品質への効果が確認できる、B=数字は T1〜T3 だが効果への因果は未検証、C=会社の主張と定価差のみ(因果は未検証)、D=未確認。

| # | 活動 | 会社・報道の説明(主張される効果) | 裏付けになる数字・事実 | 裏付けになっていない点・反証 | 強さ | 出典 |
|---|---|---|---|---|---|---|
| V1 | **off-box 仮想化**(Gen2 の Cloud Control Computer、後継の Acceleron Converged NIC) | 仮想化をホスト CPU から外し、「顧客は払った処理能力の 100% を使える」。裸金属を提供でき、隔離を保てる(Oracle ブログの主張)。→ 同じハードで売れる計算量が増え、単価を下げられる | 計算の定価: OCI E5 $0.015/vCPU 時 vs 第三者比較の AWS 級 $0.048/vCPU 時(3.2 倍。算出: 0.048 ÷ 0.015)。2 vCPU・8GB の月額 -44.8%(算出)。Oracle 自身が off-box 方式の限界(二重処理)を認め、1 チップ統合へ移行 | 価格差の**原因**が仮想化方式かを示す原価の数字はない。比較は世代・メモリ単価が揃わない。**GPU 単価は OCI の方が高い**(2-2)。独立の性能計測なし | C | [C05][C14] |
| V2 | **フラットな(非ブロッキングの)ネットワーク設計**、RoCEv2 | 全ノード間が最小遅延・過剰契約なし(第三者ガイドの記述)。大規模クラスタが組める。外向き通信を安くできる | Supercluster 最大 131,072 GPU(2024-09)、Zettascale10 最大 80 万 GPU(2025-10)は Oracle の発表値。egress 10TB 無料+$0.0085/GB(AWS の約 1/10.6)。ClusterMAX Gold(v2.0・v3.0 要約) | 非ブロッキングの**独立検証なし**。Zettascale10 の GA は未確認。MLPerf の提出は最大 128 GPU。ClusterMAX は Platinum でない(CoreWeave・Nebius が上位) | B(規模は発表値)/ C(品質の因果) | [C01][C13][C15][C12] |
| V3 | **自社設計の Exadata**(DB 専用のエンジニアド・システム) | X11M は X10M 比で最大 1.25 倍の同時トランザクション(Oracle の主張)。Exascale で公開クラウド側の入口価格を下げる。同じ Exadata を OCI・Azure・Google・AWS 内で同一価格で提供([既R2]) | Cloud DBMS の MQ で Leader(2024 年版)。Hardware 売上 FY26 $3.1B(+5%)。DBMS ランキング 3 位(2025 年まで) | 他社 DBaaS(Aurora 等)との**独立ベンチマーク・価格比較は今回未取得**。Oracle の DBMS シェアは緩やかに低下(Gartner/Register)。Exadata 単独の売上は欠損 | B(評価)/ D(性能・価格優位) | [C18][C20][既R2] |
| V4 | **Autonomous による運用自動化** | 自己チューニング・自己修復で運用工数を減らし、高い可用性を保つ | SLA: 99.995%(Data Guard 有効)/ 99.95%(無効)、計画メンテナンス込み(T1)。ADW・ATP は $0.336/ECPU 時(License Included) | 顧客の運用工数・人件費の削減額の数字は**未取得**。AWS・Azure の DB の SLA は未検索で比較不能。SLA は返金条件で実績ではない | C | [C10][C08] |
| V5 | **開発業者が建てる DC をリースで使う** | 建物・電力設備の資金を開発業者・貸し手が負担。Oracle の自己資金負担を圧縮し、供給を速める。「資本ライト」の会社の逐語は未確認([既S1]) | Abilene=Crusoe、Shackelford・Port Washington=Vantage、Jupiter=STACK(Oracle は 18 年リースのテナント)、Saline=Related([既S3])。Q3 FY26 の説明: 確保した 10GW 超の**90% 超がパートナー資金**([既S2])。未開始リース $99.8B(2025-08)→ $288B(2026-08)、期間 15〜19 年([既S4])。認識済みリース負債 $37.89B(2026-05)。S&P は未開始リースを調整後負債の予測に算入 | リース料率($/kW 月、$/MW 年)は**未取得**。顧客契約 5〜6 年とリース 15〜19 年で期間差 9〜14 年(算出。[既S4])。Jupiter では賃料開始の繰延は免除でなく、Oracle はリースを解約できないと Reuters の関係者が説明。**価格を下げる効果を示す数字はない** | A(構造)/ D(価格への効果) | [既S2][既S3][既S4][既H3] |
| V6 | **顧客資金の前払い・持込 GPU(BYOH)** | 顧客が GPU 代金を前払いするか、自ら購入して Oracle に提供。Oracle の資金負担と GPU 調達リスクを減らす。Magouyrk: BYOH・前払い契約に粗利率の劣化はない | 前払い・顧客提供ハードの累計 **$75B**(2026-06 プレス)。Q4 FY26 の新規 $67B の大半。Q1 FY27 の顧客前払い(重要な金融要素あり)**$11.4B**(10-Q)。FY27 capex は総額 $90〜95B のうち自社の現金負担は最大 $70B。Q1 FY27 は capex $28.5B に対し net 現金 $18B([既S1][既S2]) | 価格への効果(顧客に安く提供できるか)を示す数字なし。粗利率の「劣化なし」は会社の説明で、数値(Q4・Q1 の AI 容量粗利率)は見つからず([既S4])。FCF は 6 四半期連続マイナス(Q1 FY27 -$5.4B) | A(資金構造)/ D(価格) | [既S1][既S2][既S4] |
| V7 | **建設速度** | Magouyrk: Abilene のクラスタ(約 20 万 GPU)を根拠に「月単位で、年単位でなく」大規模案件を実行できる。DC 納入は Q1 FY27 に 850MW・30 万基超 | Q1 FY27 の納入 850MW・GPU 30 万基超(Q4 の約 3 倍)。GPU 稼働率 97.9%([既S4])。Abilene 最初の 2 棟 200MW 超が稼働(2026-03) | Bloomberg: 一部の OpenAI 向け DC を 2027 → 2028 に延期(労働力・資材不足)。Oracle 広報は「契約上必要なサイトに遅延なし」。Jupiter は不可抗力通知(2026-09)、ガスパイプライン稼働予定が 2026-08-15 → 2027-02-01。Abilene の 600MW 拡張の中止報道(Oracle は否定)。CBRE: 一般的な DC 建設は 2〜6 年。Q4 時点の見込み(約 1GW)に対し 850MW(算出: 850 < 約 1,000、「約」の幅は不明)。**他社との建設期間の比較は見つからず** | B(部分的)/ D(競合比) | [C23][既S3][既S4] |
| V8 | **電力の確保** | 電力が最大の制約で、確保が納期と容量を決める | Q3 FY26: 10GW 超を確保。敷地内ガスのマイクログリッド(Shackelford、VoltaGrid)、トラック輸送ガス(Salt Lake City 近郊で 1 年超)、Bloom 燃料電池(Jupiter、最大 2.5GW)、DTE が電力 100% 供給(Saline)。Oracle は Point Beach の電力コスト上昇分 $3 億を住民に負担させないと表明(2026-10-02)([既S2][既S3]) | 電力単価($/MWh)、契約電力の GW 別内訳は**未取得**。競合との確保量の比較なし。パイプライン遅延で代替策(トラック輸送)に依存 | B(事実)/ D(競合比) | [既S2][既S3] |
| V9 | **マルチクラウド(他社 DC 内に Oracle の DB を置く)** | 顧客が他社クラウドに置いたアプリの近くで Oracle DB を使える。移設不要。Azure の MACC 充当可 | Azure 28 リージョン(1 社の記述)、AWS 20(AWS 公式 2026-05-29)、Google 約 15。売上 +353%・顧客数 +180%(Q1 FY27。Quartr の単一出典で裏取り未了、[既S4])、過去 +531%(Q3 FY26)・+404%(Q4 FY26)。価格は OCI の Exadata Database Service と同じと Oracle ページが説明([既R2] §3⑥) | **絶対額は非開示**(成長率は基数効果で逓減)。マルチクラウドの価格が他社 DBaaS より安いかの比較は未取得。Oracle のハード・運用は Oracle 負担で、場所・電力・ネットワークは提携先が負担する分担の詳細は未確認 | B(成長・拠点)/ D(価格優位) | [既R2] §3⑥ |
| V10 | **価格設計(単一価格表、低い転送料、低い計算・ストレージ単価)** | 転送料が安く、OCI は計算とストレージが他社より安い(Oracle の主張) | 2-1・2-3・2-4 の定価差(計算 -44.8%、容量 -68%、転送 月 50TB で 1/12.6。いずれも算出) | すべて Tier 4。**GPU は逆**(2-2)。定価差が原価の低さによるか、戦略的な価格設定かは判断材料がない | C | [C01][C05][C06] |

**関連する会社の数字(再掲。価格を下げられる余地の目安)**: 6 年・$60B の AI インフラ契約の例で通算粗利率 35%、コスト構成は土地・DC・電力・人員が約 35%、計算・ネットワークが約 65%([既S4] §4-3 に引用された FAM の例示)。AI 容量の粗利率は Q3 FY26 で 32%(ガイダンス 30%)、契約期間通算の目標は 30〜40%。The Information の報道は 2025 年 6〜8 月に 14%([既S3][既S4])。**競合(AWS・Azure・Google・CoreWeave・Nebius)の同じ指標は今回未取得**。

---

## 5. 出典間の食い違い(どちらかを採らず併記)

| # | 項目 | 食い違い | 所見 |
|---|---|---|---|
| 1 | AWS の H100 | $6.88(p5.48xlarge $55.04 ÷ 8、2025-06 値下げ後)/ 約 $3.90 / 値下げ前 $12.29 | 約 $3.90 の根拠(割引後かスポットか)が要約に無い。$6.88 は Holori(2026-09 更新)と値下げ率(44%)で整合 |
| 2 | Azure の H100 | $6.98(単体 VM)/ $98.32 ÷ 8 = $12.29 / 8GPU で $40〜56 時 | $98.32 は AWS の旧価格と同額で転記誤りの疑い(要約も指摘)。型・リージョンが揃わない |
| 3 | Google の H100 | $11.06($88.49/時)/ $10.98($87.83/時)/ $44〜64 時(= $5.5〜8.0/GPU) | リージョン差・日付差の可能性 |
| 4 | Nebius の H100 | $2.00 / $2.95 / $3.85 | $3.85 は GPU レンタル競合(Spheron)のブログ。要約自身が低めの重み付けを勧める |
| 5 | OCI の H100・H200 | H100 $10.00 と $10.75。H200 $10.00 と約 $12.25 | [既R2] §4 項目 4 の再掲 |
| 6 | GB200 の価格帯 | OCI $16.00 / CoreWeave $10.50 / Azure $27.04([C03])。[既S3] は GMI Cloud $8.00・最安 $10.50・8 社平均約 $18 | 事業者・日付が異なり、直接比較不能(いずれも Tier 4) |
| 7 | OCI の VM SLA | 99.9% / 99.95% / 99.99%(構成別) | 構成(AD / FD / 単一)別の表を要約したもの。Oracle の SLA 原文は未読 |
| 8 | OCI ブロックの VPU | 基準 10 VPU が無料 / Balanced は +$0.0017/GB 月 / VPU は $0.0015〜0.002 | 性能条件の比較ができない |
| 9 | $0.0807/ECPU 時 | [既R2]: JSON・APEX の価格 / 今回: ADW・ATP の BYOL 価格 | 同一 PDF の読み。原典確認が必要 |
| 10 | BYOL の ECPU 換算 | 現行 8 ECPU/ライセンス、旧版 4 ECPU/ライセンス。助言会社は ADW・ATP の License Included を $1.34、BYOL を $0.336 とし、Oracle FAQ と矛盾 | 助言会社の数字は Oracle FAQ と整合せず、採用しない |
| 11 | Google Cloud の認可状況 | 助言会社 1 社「認可環境リストに無い」/ 別の要約「新しい版で GCP を認可環境に追加」 | 方針の版により異なる可能性。保留 |
| 12 | Finout の OCI 月額 | $38.69 / E5.Flex 単価からの算出 $33.58 | 型名・メモリ・時間数の前提が出典に無い |
| 13 | Oracle のシェア | Gartner 2024: 上位 5 社外(4.1% 未満)/ Synergy 2025 年 7〜9 月: 3.1% / Oracle 自社 IaaS 売上からの算出: 3.8%〜5.9% | 定義(IaaS のみか、DB サービス・PaaS 等を含むか)と期間が違う。同一基準の比較はできない |
| 14 | Abilene の規模 | 「約 20 万基の GPU」(Magouyrk 発言の要約)/「最初の 2 棟で 200MW 超が稼働」([既S3])/ Q1 FY27 の納入 30 万基超(四半期、全拠点) | 時点・範囲が異なる可能性。照合は未実施 |
| 15 | Gartner MQ の年版 | Strategic Cloud Platform Services は「2025 年版」(報告書日付 2025-08-04)。Cloud DBMS は「2024 年版」(Oracle の発表は 2025-01-21) | 年版名の付け方が MQ ごとに異なる。2026 年版の Oracle の位置は未確認 |
| 16 | 競合の Silicon Data 指数との関係 | ハイパースケーラー中央値 $7.19([既S3])と、AWS $6.88・Azure $6.98 は近い。Google $11.06・OCI $10.00 は高い | 指数の構成社・SKU は未取得 |

---

## 6. 出典一覧

Tier の `*` は、一次書類・公式ページだが検索要約経由でしか見ていないことを示す。掲載日は検索結果に表示があったものだけ記載し、無いものは「不明」とした。

### 6-1. 既存調査(再掲元)

| ID | 内容 | パス |
|---|---|---|
| 既S1 | 経営陣シナリオ(BYOH・前払い・資金調達) | `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research/S1_management_scenario.md` |
| 既S2 | 市場の仮説(Q3 FY26 の 10GW 超・パートナー資金 90% 超ほか) | 同 `S2_market_hypothesis.md` |
| 既S3 | スカットルバット(GPU 単価指数、拠点、CoreWeave 値上げ) | 同 `S3_scuttlebutt.md` |
| 既S4 | 芯の追加事実(GPU 更新、粗利率、リース、契約期間) | 同 `S4_core_variables.md` |
| 既R2 | 製品棚卸し(OCI・ECPU・Exadata の価格、マルチクラウド) | `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research2/R2_products_5w1h.md` |
| 既H3 | 負債・リース・コミットメント | `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/data/H3_obligations.md` |

### 6-2. 今回の検索で得た出典

| ID | 媒体・内容 | URL | 掲載日 | Tier |
|---|---|---|---|---|
| C01 | 外向き通信の比較(Finout、Opsio、Rackdog、Ecorpit、CloudToolStack、oraclelicensingexperts、Akave。要約が統合しており、数値の個別 URL は特定できず) | https://finout.io/blog/cloud-storage-pricing-comparison 、https://opsiocloud.com/blogs/cloud-pricing-comparison-aws-azure-gcp-2026/ 、https://rackdog.com/blog/egress-fees-index 、https://ecorpit.com/cloud-egress-fees-ai-inference-bill-comparison-2026/ 、https://cloudtoolstack.com/blog/cloud-egress-cost-optimization 、https://oraclelicensingexperts.com/blog/oracle-cloud-egress-interconnect-cost/ 、https://oraclelicensingexperts.com/blog/oracle-egress-costs-hyperscaler/ 、https://akave.com/blog/cloud-egress-fees-explained-azure-vs-google-cloud-vs-akave | 2026 年とされるが個別日付は不明 | 4 |
| C02 | H100 レンタル価格の比較(IntuitionLabs、Spheron の Nebius・CoreWeave 記事、Thunder Compute、keenable の分析 4 本) | https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison 、https://spheron.network/blog/nebius-h100-h200-pricing-2026 、https://spheron.network/blog/coreweave-h100-h200-pricing-2026 、https://thundercompute.com/blog/nvidia-h100-pricing 、https://select.keenable.ai/r/nvidia-h100-cloud-pricing-real-gpu-hour/BTu87SL0hHuowSFpemeY8g 、https://select.keenable.ai/r/real-h100-cloud-cost-compute-discounts-egress-availability/zIIR2YalYLMWP0wK4wbdmw | 2026 年中頃(要約の記述) | 4 |
| C03 | GB200・H200・B200 の価格(getdeploying、IntuitionLabs の 2026 年 GPU 価格 PDF、Spheron) | https://getdeploying.com/gpus/nvidia-gb200-vs-nvidia-h200 、https://intuitionlabs.ai/pdfs/data-center-gpu-pricing-2026.pdf 、https://spheron.network/blog/nebius-h100-h200-pricing-2026 | 不明(getdeploying は日付なしと要約が注記)。Nebius H200 は 2026-06 の比較 | 4 |
| C04 | AWS p5 の価格(Holori の価格ページ、Spheron、io.net、Lyceum、Hostinger、GMI Cloud) | https://calculator.holori.com/aws/ec2/p5.48xlarge 、https://spheron.network/blog/aws-h100-pricing-2026 、https://io.net/p/nvidia-h100-on-aws-complete-guide-70-cheaper-alternatives-2026 | Holori は 2026-09 更新。値下げは 2025-06 | 4 |
| C05 | OCI の計算価格・競合比較(Finout、DEV Community、vpsranking、CloudToolStack、Oracle ブログ) | https://www.finout.io/blog/oci-costs-overview 、https://dev.to/manishpcp/comprehensive-guide-to-cloud-service-pricing-aws-azure-gcp-and-oci-comparison-4pc4 、https://vpsranking.com/oci/ 、https://cloudtoolstack.com/learn/multi-cloud-cost-comparison-guide 、https://blogs.oracle.com/cloud-infrastructure/oci-vs-azure-serverless-container-instances-best | 不明 | 4(Oracle ブログは T1 販促) |
| C06 | ブロックストレージの価格(oraclelicensingexperts、Redress、EaseCloud、Oracle の経済性ページ。転載サイト経由) | https://oraclelicensingexperts.com/blog/oracle-oci-storage-pricing/ 、https://redresscompliance.com/oracle-oci-vs-aws-vs-azure-pricing-comparison.html 、https://blog.easecloud.io/ai-cloud/oci-vs-aws-vs-azure/ 、https://dcmpx.remotevs.com/com/oracle/www/SL/cloud/economics | 経済性ページは 2024-06-05(要約の記述) | 4(Oracle ページは T1 販促*) |
| C07 | Oracle のコア係数表(OCI の 2 OCPU / 4 OCPU)と、AWS・Azure の数え方を述べる助言会社 | https://www.oracle.com/contracts/docs/processor-core-factor-table-070634.pdf 、https://redresscompliance.com/oracles-processor-core-factor-table-and-aws-licensing 、https://oraclelicensingexperts.com/oracle-licensing-policies | 不明 | 1*/4 |
| C08 | ECPU の BYOL(Oracle の ECPU FAQ、Oracle の価格ページ、Redress、oraclelicensingexperts) | https://oracle.com/a/ocom/docs/autonomous-database-ecpu-faq.pdf 、https://www.oracle.com/cloud/aws/pricing 、https://www.oracle.com/autonomous-database/autonomous-database-on-dedicated-infrastructure/pricing/ 、https://redresscompliance.com/oracle-autonomous-database-licensing 、https://oraclelicensingexperts.com/blog/oracle-database-at-azure-pricing-benchmarks/ 、https://oraclelicensingexperts.com/blog/oracle-autonomous-database-licensing/ | 不明(FAQ の版は現行と 2023 年版の 2 種) | 1*/4 |
| C09 | Oracle「クラウド環境での Oracle ソフトウェアのライセンス」方針(Oracle の PDF、Redress、DSP、Version 1)。AWS・Azure の 2 vCPU = 1 ライセンス、SE の vCPU 上限 | https://oracle.com/a/ocom/docs/cloud-licensing.pdf 、https://oracle.com/a/ocom/docs/cloud-licensing-070579.pdf 、https://redresscompliance.com/licensing-oracle-software-in-the-cloud-computing-environment 、https://content.dsp.co.uk/licensing-oracle-software-in-the-cloud-computing-environment 、https://www.version1.com/Licensing-Oracle-Software-in-the-C/ | 版により異なる(日付不明) | 1*/4 |
| C10 | Oracle の SLA(OCI SLA ページ、Autonomous Database の SLA ブログ・文書) | https://www.oracle.com/it/cloud/sla/ 、https://blogs.oracle.com/autonomous-ai-database/autonomous-database-updated-sla 、https://blogs.oracle.com/datawarehousing/post/autonomous-database-updated-sla 、https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbdn | 不明 | 1* |
| C11 | SLA の比較(vpsranking、CloudToolStack、Opsio、Columbia 大の資料、Oracle 作成の OCI vs Azure PDF) | https://vpsranking.com/public_cloud/ 、https://cloudtoolstack.com/tools/multi-cloud-sla-compare 、https://opsiocloud.com/knowledge-base/vad-ar-azure-sla/ 、https://www.cs.columbia.edu/~salman/presentations/slas-baset-pres-open.pdf 、https://www.oracle.com/ca-en/a/ocom/docs/cloud/oci-vs-azure.pdf | 不明(Opsio は「2026 年の比較」と要約) | 4(Oracle の PDF は T1 販促) |
| C12 | OCI の MLPerf(Oracle ブログ: Inference 5.0、Training v4.0、GH200 ほか) | https://blogs.oracle.com/cloud-infrastructure/post/mlperf-inference-5-exceptional-performance 、https://blogs.oracle.com/cloud-infrastructure/post/mlperf-training-v4-results-oci-gpu-superclusters 、https://blogs.oracle.com/cloud-infrastructure/post/benchmark-results-nvidia-gh200-superchip-oci | 不明(v4.0 は 2024 年、v5.0 は 2025 年。要約に日付なし) | 1(自己評価) |
| C13 | OCI Supercluster・Zettascale(Oracle ブログ、Oracle の AI World 総括、TipRanks / The Fly、AIwire、HPCwire) | https://blogs.oracle.com/cloud-infrastructure/post/worlds-largest-ai-supercomputer-in-the-cloud 、https://www.oracle.com/cloud/ai-world-oci-roundup/ 、https://www.tipranks.com/news/the-fly/oracle-announces-zettascale-cloud-computing-clusters-accelerated-by-nvidia 、https://aiwire.net/2024/09/11/oracle-unveils-cloud-computing-cluster-with-up-to-131072-nvidia-blackwell-gpus 、https://www.hpcwire.com/?p=175505 | 2024-09-11(131,072 GPU)、2025-10-14(Zettascale10) | 1/3 |
| C14 | OCI Gen2・off-box 仮想化・Acceleron(Oracle ブログ、Acceleron FAQ、Brainbound) | https://blogs.oracle.com/cloud-infrastructure/first-principles-oracle-acceleron-nic-for-ai 、https://www.oracle.com/cloud/networking/acceleron/faq/ 、https://www.brainbound.blog/oci-oracle-gen2-enterprise-guide | 不明 | 1/4 |
| C15 | SemiAnalysis ClusterMAX(3.0 の記事、v2.0 の Hedgehog 要約、remio.ai の 3.0 要約、CoreWeave のブログ、Blocks & Files の v1 記事) | https://newsletter.semianalysis.com/p/clustermax-30-the-industry-standard 、https://hedgehog.cloud/blog/the-sell-math-how-clustermax-2.0-ratings-translate-into-revenue 、https://www.remio.ai/post/clustermax-3-0-ratings-return-and-cheap-gpu-clouds-face-a-harder-test 、https://coreweave.com/blog/coreweave-becomes-the-only-provider-to-earn-three-consecutive-platinum-clustermax-tm-ratings 、https://blocksandfiles.com/2025/04/03/clustermax-gpu-cloud-ratings-and-storage/ | v1: 2025-04-03、v2.0: 2025-11、v3.0: 2026-09-23 | 3/4(3.0 の本文はペイウォール、未読) |
| C16 | OCI の障害(The Register、pingoru のステータス履歴、DCD、Techzine) | https://www.theregister.com/2026/01/28/oci_access_complaints/ 、https://pingoru.io/providers/lessonly/incidents/18795 、https://pingoru.io/providers/rfpio/outage-history 、https://pingoru.io/providers/tenable/incidents/689985 、https://www.datacenterdynamics.com/en/news/oracle-cloud-experiences-outage-in-europe-users-say/ 、https://www.techzine.eu/news/infrastructure/102112/oracle-cloud-and-netsuite-hit-by-global-outage/ | Register 2026-01-28。他は事象日付のみ(2026-01-13、2026-03-23、2026-06-08、2025-05)。Techzine は不明 | 3/4 |
| C17 | Gartner MQ: Strategic Cloud Platform Services(Oracle の発表、Oracle の MQ ページ、AWS の 2026 年版告知) | https://www.oracle.com/news/announcement/oracle-recognized-as-a-leader-in-the-2025-gartner-magic-quadrant-for-strategic-cloud-platform-services-2025-08-08/ 、https://www.nasdaq.com/press-release/oracle-recognized-leader-2025-gartnerr-magic-quadranttm-strategic-cloud-platform 、https://www.oracle.com/cloud/gartner-mq-strategic-cloud-platform-services-leader/ 、https://aws.amazon.com/resources/analyst-reports/gartner/global-mq-ardm-26-magic-quadrant-for-strategic-cloud-platform-services/ | 2025-08-08(Oracle 発表)。2026 年版の告知日は不明 | 1(Oracle の自己発表。Gartner 本文は未読) |
| C18 | Gartner MQ: Cloud Database Management Systems(Oracle の発表、DBTA、SDxCentral) | https://www.oracle.com/news/announcement/oracle-named-leader-in-gartner-magic-quadrant-for-cloud-database-management-systems-2025-01-21/ 、https://www.dbta.com/Editorial/News-Flashes/Oracle-Named-a-Leader-in-the-2024-Gartner-Magic-Quadrant-for-Cloud-Database-Management-Systems-167660.aspx 、https://www.sdxcentral.com/news/oracle-database-recognized-as-leader-in-2024-gartner-magic-quadrant/ | 2025-01-21 | 1/3 |
| C19 | Gartner IaaS 市場シェア(2024 年・2023 年) | https://www.gartner.com/en/newsroom/press-releases/2025-08-06-gartner-says-worldwide-iaas-public-cloud-services-market-grew-22-point-5-percent-in-2024 、https://www.gartner.com/en/newsroom/press-releases/2024-07-22-gartner-says-worldwide-iaas-public-cloud-services-revenue-grew-16-point-2-percent-in-2023 、https://cxotoday.com/press-release/gartner-says-worldwide-iaas-public-cloud-services-market-grew-22-5-in-2024/ | 2025-08-06、2024-07-22 | 3(Gartner の発表。要約経由) |
| C20 | DBMS 市場(The Register、Red Gate、CRN Australia、Gartner の概要ページ、itmarketstrategy、SDxCentral) | https://www.theregister.com/2026/04/21/gartner_bamboozling_dbms_chart_shows/ 、https://www.red-gate.com/simple-talk/databases/what-are-the-top-database-platforms-in-2026-a-look-at-the-latest-data/ 、https://crn.com.au/news/aws-oracle-google-microsoft-top-cloud-dbms-market-gartner-605261 、https://www.gartner.com/en/documents/6494271 、https://itmarketstrategy.com/2024/04/20/dbms-market-in-2023-transition-continues/ 、https://itmarketstrategy.com/2024/05/31/dbms-market-2023-more-momentum-shifts | Register 2026-04-21。itmarketstrategy 2024-04-20、2024-05-31 | 3 |
| C21 | Synergy Research(Q2 2026 の記事、The Register、DCD、RCR Wireless、「Big Three 63%」記事、Q1 2026 の DCD 記事) | https://www.srgresearch.com/articles/q2-cloud-market-passes-143-billion-highest-growth-rate-in-eight-years 、https://www.theregister.com/a/5281835 、https://www.datacenterdynamics.com/en/news/enterprise-cloud-infrastructure-spending-hits-143-billion-report/ 、https://www.rcrwireless.com/20260602/telco-cloud/ai-cloud-synergy 、https://srgresearch.com/articles/cloud-market-share-trends-big-three-together-hold-63-while-oracle-and-the-neoclouds-inch-higher 、https://www.datacenterdynamics.com/en/news/synergy-research-cloud-spending-hits-129bn-in-q1-2026-ninth-consecutive-quarter-of-growth | 2026-06-02(RCR)。Q2 の記事は 2026 年 7〜8 月頃(日付不明) | 3 |
| C22 | CIO Dive / Channel Dive(Oracle の capex 急増。Synergy の Oracle 3.1% を引用)と Oracle の Q2 FY26 決算発表 | https://www.ciodive.com/news/oracle-capex-spike-cloud-ai-data-center/807721 、https://www.oracle.com/es/news/announcement/q2fy26-earnings-release-2025-12-10/ | 2025-12 頃 | 3/1* |
| C23 | 建設速度・遅延(Techstrong、MarketScreener / Bloomberg、Construction Dive / CBRE、3DTested、cnyes、Fortune) | https://techstrong.ai/articles/oracle-denies-delays-in-openai-data-center-construction/ 、https://www.marketscreener.com/news/due-to-shortages-oracle-delays-several-data-centers-intended-for-openai-until-2028-ce7d50d8db80f62c 、https://www.constructiondive.com/news/oracle-data-center-expansion/710199/ 、https://www.3dtested.com/tech-industry/oracle-and-openai-scrap-planned-600mw-abilene-expansion 、https://news.cnyes.com/news/id/6373645 、https://fortune.com/2025/09/24/openai-stargate-puts-on-texas-size-show-oracle-murdoch | Fortune 2025-09-24。他は不明(2026 年前半) | 3 |

---

## 7. 未確認事項と検索ログ

### 7-1. 未確認事項(欠損)

| # | 項目 | 試した検索(要旨) | 結果 |
|---|---|---|---|
| 1 | Oracle・AWS・Azure・GCP の汎用計算の、型名つき公式単価(vCPU 時) | #5 | 型名不明の月額比較のみ。公式価格表は読めず |
| 2 | OCI・AWS・Azure・GCP の H200・B200 の公式単価、AWS の GB200、Google の GB200 | #2、#3 | OCI の H200・B200 は [既R2] の値のみ。AWS・Google は掲載なし |
| 3 | OCI の GPU の大口契約単価、CoreWeave・Nebius の契約単価 | #2、#3(および [既S3]) | 欠損。定価と契約単価は別物 |
| 4 | 確約割引(Universal Credits、Savings Plans)後の価格 | #5 | 欠損 |
| 5 | 競合の ブロックストレージ(Google)・転送(Azure・GCP の 10TB 超の帯)の単価 | #1、#6 | 一部のみ |
| 6 | Oracle の Exadata Database Service の BYOL 価格、AWS・Azure・GCP の RDS for Oracle の BYOL 規則の原文 | #21、#28 | 数字は取得できず。AWS・Azure の数え方は Oracle 方針の要約(原文未読) |
| 7 | Google Cloud が Oracle の認可クラウド環境かどうか | #4、#28 | 出典が割れた(5 節 11)。保留 |
| 8 | OCI のコア係数表(オンプレ向けの全体)と、認可外クラウドでの扱い | #4 | OCI 部分(2 OCPU / 4 OCPU)のみ |
| 9 | AWS・Azure・GCP・CoreWeave の最大クラスタ規模 | #23 | Oracle の匿名比較表のみ。名指しの数字は欠損 |
| 10 | MLPerf の競合提出との比較、OCI の GB200 提出、2026 年の OCI 提出 | #8 | 見つからず。MLCommons の結果ページは未確認 |
| 11 | ClusterMAX の AWS・Google の階級、v3.0 の Oracle の階級の一次確認、v1 の Oracle の階級 | #18、#27 | v3.0 の Oracle Gold は 1 社の要約のみ。本文はペイウォール |
| 12 | 競合(AWS・Azure・Google・CoreWeave・Nebius)の障害実績、AWS・Azure の DB の SLA | 検索せず(枠の制約) | 欠損。OCI の障害の多寡は判断不能 |
| 13 | OCI の SLA 原文(表の全項目、返金クレジット率) | #7、#24 | 要約で一部文字化け |
| 14 | Gartner MQ の 2025 年版 SCPS の他社位置、2026 年版 SCPS の Oracle の位置、Cloud DBMS の 2025 年版以降、軸の座標 | #9、#10、#13、#25 | 欠損(MQ 本文は有料) |
| 15 | Oracle の DBMS 売上・シェア(2024・2025)、IDC の DBMS シェア | #11、#14、#26 | 欠損。2023 年の目安のみ(算出) |
| 16 | Canalys / Omdia のクラウド市場シェア、Gartner の 2025 年 IaaS シェア(2026 年発表分)、Synergy の 2026 年の Oracle のシェア値 | #12、#15、#16 | 見つからず(Gartner の最新は 2024 年分) |
| 17 | 原価の数字: 1MW あたりの建設費、リース料率、電力単価、仮想化で増える売れる計算量 | #17、#20 | 見つからず(バリューチェーンの効果を数量で結べない) |
| 18 | 他社との建設期間・納入速度の比較、競合の capex 当たりの GW | #20 | 独立比較なし |
| 19 | 運用自動化(Autonomous)の人件費削減額・顧客事例の定量値 | 検索せず(枠の制約) | 欠損 |
| 20 | Oracle が「GPU 単価が競合より安い」と主張した一次発言の有無 | #2、#3 | 見つからず(存在しないことの確認ではない) |

### 7-2. 検索ログ(28 回。すべて mode: standard)

| # | 検索語(要旨) | 主な成果 |
|---|---|---|
| 1 | OCI vs AWS vs Azure vs GCP の egress 価格、10TB 無料 | 無料枠・従量単価 |
| 2 | H100 の GPU 時単価、OCI・AWS・Azure・GCP・CoreWeave・Nebius | H100 の各社単価 |
| 3 | B200・GB200・H200 の GPU 時単価、各社 | GB200 の OCI・CoreWeave・Azure |
| 4 | Oracle DB のライセンス、AWS・Azure・GCP、2 vCPU、コア係数、OCI の OCPU | OCI の 2 OCPU / 4 OCPU、AWS・Azure の規則 |
| 5 | 汎用計算の vCPU 時単価、OCI vs AWS vs Azure vs GCP | Finout の月額比較 |
| 6 | OCI のブロックストレージ、VPU、gp3 | $0.0255 vs $0.08、VPU の食い違い |
| 7 | OCI の SLA、AWS EC2 99.99%、Azure VM | 構成別 SLA |
| 8 | OCI の MLPerf 提出 | v3.1・v4.0・v5.0 |
| 9 | Gartner MQ SCPS 2025 の Oracle の位置 | Leader(3 年連続) |
| 10 | Gartner MQ Cloud DBMS の Oracle の位置 | Leader(2024 年版) |
| 11 | Gartner DBMS の市場シェア 2025 | 順位(AWS、Microsoft、Oracle、Google) |
| 12 | Gartner IaaS 2025・Canalys・Omdia の Oracle のシェア | Synergy の 3.1%(2025 年 7〜9 月) |
| 13 | 2026 年版 Gartner MQ SCPS の Oracle | AWS の 2026 年版告知のみ |
| 14 | The Register の Gartner DBMS 記事 | 「侵食」の記述、2024 年 $119.7B |
| 15 | Synergy 2026 年 4〜6 月、Oracle のシェア | 28 / 20 / 15%、Oracle は第 2 グループ |
| 16 | Gartner 2025 年の IaaS シェア | 2024 年分の 37.7 / 23.9 / 9.0% |
| 17 | OCI Gen2・off-box・フラットネットワーク | Acceleron、CCC、Oracle の自認 |
| 18 | SemiAnalysis ClusterMAX の Oracle | v2.0 の Gold、v3.0 の存在 |
| 19 | OCI の障害 2026 | London、Phoenix、Pod1、Amsterdam、2025-05 欧州 |
| 20 | Oracle の建設速度、Abilene、コスト/GW | Magouyrk の主張、遅延報道、CBRE |
| 21 | Oracle の BYOL、ECPU、1 ライセンス = 4 ECPU | $0.336 / $0.0807、8 ECPU / 4 ECPU |
| 22 | AWS p5・Azure ND H100・Google a3 の価格 | $55.04/時、$98.32 の混在 |
| 23 | 最大 GPU クラスタ、OCI 131,072 GPU vs 競合 | 匿名の比較表 |
| 24 | OCI SLA(Compute 99.95%、Autonomous 99.995%) | 構成別の SLA、ADB の SLA |
| 25 | Cloud DBMS の MQ(2025 年版・2026 年版)の Oracle | 新しい版は見つからず |
| 26 | DBMS 市場 2025、itmarketstrategy の Oracle のシェア | 2023 年の金額差 |
| 27 | ClusterMAX 3.0(2026-09)の Oracle の階級 | Gold(1 社の要約) |
| 28 | 「クラウド環境での Oracle ソフトウェアのライセンス」方針、2 vCPU、GCP | AWS・Azure の規則、GCP の記述が割れる |
