# 第6回 指示書: 条件スライドの関係図の作り直し(9 枚)

共通ルールは `spec/r6_common.md`。見本は `slides/s08b.js`。数値の正は第4.3版(旧指示書 `spec/ch3_conditions.md` の数値と同じ)。
各スライドは `L.contentSlide` → `L.flowMap` → `L.mechPanel`(→ C 以下は `L.kpiBand`)の順で作る。
箱の位置(c, r)は出発点。重なりの警告が出たら、行・列の入れ替え、空きセルの使い方、ラベルの位置(below・lpos・ldx/ldy)、番号だけの丸への切り替えで解消する。箱や仕組みを減らして解消しない。
既存のファイル(slides/s17.js など)は上書きしてよい(旧版は deck/ に lib_v3.js などと同様に残っているので不要)。

---

## s17 条件1 競争優位の持続(B)
- kicker: `左から: 顧客 → Oracle の事業 → 優位の源泉(壁)← 競合の圧力。下: 優位が続く期間。①〜④ は右と対応`
- source: `会社開示(Q1 FY27 説明会)、research4/T5_supply_components.md、research4/T3_saas_products.md、calc/prereg2.md §9(逼迫の終わり FY32)`
- grade 'B', condNo 1
- flowMap: h 3.75(下に時間軸を入れる)、cols [1.3, 1.45, 1.45, 1.35]、rows 3
  - lanes: `顧客`(c0)/ `Oracle の事業と優位の源泉`(c1〜c2, self)/ `競合・代替`(c3)
  - groups: `事業`(c1, r0〜r2)、`優位の源泉(壁)`(c2, r0〜r2)
  - nodes:
    - ent c0 r0 `DB の既存顧客` / `大企業・官公庁`
    - apps c0 r1 `業務アプリの顧客` / `ERP・人事`
    - lab c0 r2 `AI 研究所` / `OpenAI・Meta・xAI`
    - db c1 r0 unit `DB ライセンス・保守` / `保守は年 22%\nSoftware −3%`
    - saas c1 r1 unit `SaaS` / `+10%`
    - aicap c1 r2 unit `AI 容量` / `更新は従来比 +20%`
    - sw c2 r0 ok `切替コスト` / `データ移行と\nアプリ改修に数年` 、tag `数十年`(green)
    - erp c2 r1 ok `業務データの蓄積` / `移行は 8,500 社中\n約 1,000 社` 、tag `中`(amber)
    - tight c2 r2 risk `業界全体の逼迫` / `電力・部材の不足\n(自社の優位ではない)` 、tag `FY32 まで`(red)
    - hyper c3 r0 `AWS・Azure・Google` / `DB 移行サービス`
    - sap c3 r1 `SAP・Workday` / `クラウド ERP +25%`
    - neo c3 r2 risk `ネオクラウド・TPU` / `H100 実勢は\n約 2.6 倍安い`
  - edges:
    - ent → db `保守料`, money, n 1
    - apps → saas `購読料`, money, n 2
    - lab → aicap `容量料 +5%/年`, money, n 3(逼迫期の単価の伸び)
    - sw → db `顧客を囲う`, ctrl
    - erp → saas `移行を促す`, ctrl
    - tight → aicap `値上げを許す`, ctrl
    - hyper → sw `移行の誘い`, risk
    - sap → erp `乗り換えの誘い`, risk
    - neo → tight `緩和後の値下げ`, risk, n 4
- timeBand: x 0.5, y 5.5, w 8.55, h 1.1, from 2027, to 2047, step 5, fmt `t => 'FY' + (t % 100)`、bars:
  - `DB の切替コスト` 2027〜2047, color L.C.dark, text `数十年`
  - `AI 容量の単価優位` 2027〜2032, color L.C.red, text `逼迫が終わる FY32 まで`
  - `建屋の賃料の固定` 2027〜2047, color L.C.light, text `長期リースで FY47 まで`
- mechPanel(bottom 6.66):
  1. `DB の顧客はデータ移行とアプリ改修に数年かかり、保守料(年 22%)を払い続ける`
  2. `SaaS は旧 ERP 顧客の移行で伸びるが +10% で、SAP のクラウド ERP(+25%)より遅い`
  3. `AI 容量は更新期の GPU を全量 従来比 +20% で更新・再販。ただし業界全体の値上げ(AWS +15〜20%)の一部`
  4. `逼迫が緩む FY32 以降は、ネオクラウド・TPU との価格競争で超過利益はベースで 0%`
  - reason: `DB の優位は数十年続くが、価値の 45% を占める AI 容量の優位は逼迫が続く FY32 までに限られるため B`
  - up: `緩和の兆しが出ても AI 容量の更新プレミアムが正のまま続けば A`
  - down: `Software の減収が −5% を超えて加速すれば C`

## s18 条件2 コア事業の現金創出(B)
- kicker: `左から: 資金の出し手 → Oracle の資金の源 → 使い道 → 結果。①〜⑤ は右と対応。金額は FY27(需給エンジン第4.3版・会社開示)`
- source: `会社開示(Q1 FY27、10-Q)、需給エンジン第4.3版(calc/out/m8_all.json)、research2/R7_capital_power.md、S&P(2026-07)`
- grade 'B', condNo 2
- flowMap: h 5.0、cols [1.35, 1.45, 1.45, 1.35]、rows 4
  - lanes: `資金の出し手`(c0)/ `Oracle`(c1〜c2, self)/ `支払先・評価者`(c3)
  - groups: `資金の源`(c1, r0〜r3)、`使い道と結果`(c2, r0〜r3)
  - nodes:
    - cust c0 r0 `DB・SaaS の顧客` / `保守料・購読料`
    - lab c0 r1 `AI 研究所` / `GPU 代の前払い`
    - dev c0 r2 ok `DC 開発事業者` / `10GW の 90% 超の\n建屋を負担`
    - inv c0 r3 `社債・株式の投資家` / `社債 430 億ドル\n優先株 50 億・ATM 200 億`
    - core c1 r0 unit `コアの利益` / `税引後 230 億ドル`
    - prepay c1 r1 ok `前受収益` / `154 → 308 億ドル\n(1 年で倍増)`
    - lease c1 r2 ok `長期リース` / `未開始 2,880 億ドル\n15〜19 年`
    - debt c1 r3 risk `借入・株式` / `BBB−(S&P)`
    - capex c2 r0 rs 2 key `capex(FY27)` / `総額 900〜950 億ドル\n\n前払いが 約 24% を賄う\n\n純現金 700 億ドル以下\n(会社の見通し)`
    - rent c2 r2 risk `賃料` / `固定費として\n15〜19 年続く`
    - fcf c2 r3 risk `全社 FCF(エンジン)` / `FY27 −342 億\nFY29 −135 億ドル`
    - nv c3 r0 `NVIDIA・部材` / `GPU・網・メモリ`
    - sp c3 r3 `S&P` / `FY29 までの\nFOCF 黒字を要求`
  - edges:
    - cust → core `保守料・購読料`, money
    - core → capex, money, n 1(番号だけ)
    - lab → prepay `前払い`, money, n 2
    - prepay → capex, money, n 2(番号だけ)
    - dev → lease `建屋を賃貸`, goods, n 3
    - lease → rent, money
    - inv → debt `社債・株式`, money, n 4
    - debt → fcf, money(番号なし、ラベル `不足を埋める`)
    - capex → nv `GPU 代`, money
    - fcf → sp `格付けの条件`, ctrl, n 5
  - 線が交差・重なるときは、capex の行の範囲や rent・fcf の行を入れ替えて解消する
- mechPanel(bottom 6.66):
  1. `コアの利益(税引後 230 億ドル)が capex の自己資金の柱になる`
  2. `AI 研究所が GPU 代の約 24% を前払い。前受収益は 1 年で倍増(154 → 308 億ドル)`
  3. `建屋と電力は開発事業者が資金を出し、Oracle は 15〜19 年の賃料で借りる(未開始 2,880 億ドル)`
  4. `残りは社債・優先株・ATM で調達。全社 FCF はエンジンで FY29 まで赤字(FY29 −135 億ドル)`
  5. `S&P は FY29 までの FOCF 黒字化を格付け維持の条件にする。S&P とコンセンサスは FY29 に黒字`
  - reason: `コアの現金は潤沢で、投資の多くは外部化されている。ただし自己資金で賄えない期間が FY29 まで続くため B`
  - up: `前払いの比率が 30% を超え、FCF の黒字化が FY28 に早まれば A`
  - down: `FY29 の FCF が赤字のまま BB+ に格下げされれば C`

## s19 条件3 技術の AI 転用(A)
- kicker: `左から: 既存の資産 → 転用の経路 → 新しい収益 ← 顧客。①〜④ は右と対応。数値は Q1 FY27`
- source: `会社開示(Q1 FY27)、research3/W6_database_at.md、research3/W8_aws_vs_commodity.md、report/r3_sections_5w1h_f20.md §2-0`
- grade 'A', condNo 3
- flowMap: h 5.0、cols [1.4, 1.45, 1.45, 1.3]、rows 3
  - lanes: `既存の資産`(c0)/ `Oracle の転用と成果`(c1〜c2, self)/ `顧客`(c3)
  - groups: `転用の経路`(c1, r0〜r2)、`新しい収益`(c2, r0〜r2)
  - nodes:
    - dbt c0 r0 ok `Oracle Database` / `Exadata・Autonomous`
    - net c0 r1 ok `RDMA ネットワーク` / `Exadata 由来の\n低遅延の網`
    - data c0 r2 ok `既存顧客のデータ` / `DB 内の基幹データ`
    - dbat c1 r0 unit `Database@` / `他社の DC に\nExadata を設置`
    - cluster c1 r1 unit `GPU クラスタ` / `RDMA で GPU を\n大規模につなぐ`
    - aidb c1 r2 unit `AI Database 26ai` / `DB にベクトル検索・\nエージェントを内蔵`
    - rev1 c2 r0 self `マルチクラウド DB` / `売上 +353%\n顧客 +180%`
    - rev2 c2 r1 self `OCI` / `売上 74 億ドル\n(+121%)`
    - rev3 c2 r2 `企業 AI 推論` / `売上は非開示`
    - hyper c3 r0 `AWS・Azure・Google` / `70 リージョン\n119 AZ`
    - lab c3 r1 `AI 研究所` / `学習・推論`
    - ent c3 r2 `企業` / `自社データで推論`
  - edges:
    - dbt → dbat `そのまま提供`, goods, n 1
    - net → cluster `GPU 間の網に`, goods, n 2
    - data → aidb `AI を直結`, goods, n 3
    - dbat → rev1, money
    - cluster → rev2, money
    - aidb → rev3, money
    - hyper → rev1 `契約枠で購入`, money
    - lab → rev2 `容量料`, money, n 4
    - ent → rev3 `利用`, money
- mechPanel(bottom 6.66):
  1. `DB をそのまま他社の DC に置く(Database@)。追加の開発は小さく、売上 +353%`
  2. `Exadata 由来の RDMA 網で GPU を大規模につなぎ、OCI +121% の土台になった`
  3. `26ai は DB の中に AI 検索を内蔵し、企業データの AI 需要を DB に取り込む(売上は非開示)`
  4. `ただし OCI の伸びの主因は GPU の貸し出しで、DB の転用による収益が過半ではない`
  - reason: `転用先が全社の増収の主因になったため A。主因は GPU の貸し出しで、DB 転用の収益が過半ではないため S ではない`
  - up: `AI 容量の顧客が DB やアプリも買う証拠(クロスセル)が出れば S`
  - down: `Database@ の伸びが 100% を割り、OCI の伸びが AI 容量だけになれば B`

## s21 条件5 経営者の能力(B、A との境界)— 経歴から評価し直す
評価の軸を「経歴とその事業への経験」に置く。経歴の材料: `research4/T7_executives.md`(検索要約で一次資料は未照合。不一致の項目は幅で書く)。
- kicker: `左から: 経歴(どこで何を築いたか)→ 現職 → 担う事業 → 結果。①〜⑤ は右と対応。経歴は報道・会社発表の要約に基づく`
- source: `research4/T7_executives.md(Oracle 発表・8-K 2025-09-22・2026-04-06、Bloomberg・Reuters ほか)、DEF 14A(報酬)、会社開示(FY26〜27 のガイダンス)`
- grade 'B', condNo 5
- flowMap: h 5.0、cols [1.4, 1.4, 1.4, 1.4]、rows 4
  - lanes: `経歴`(c0)/ `経営陣と担う事業`(c1〜c2, self)/ `結果`(c3)
  - nodes:
    - aws c0 r0 `AWS(〜2014)` / `クラウド基盤の\n技術者 約 6〜7 年`
    - prim c0 r1 `Primavera(1993〜)` / `技術者 → CTO\n2008 年に Oracle が買収`
    - aes c0 r2 ok `AES・Schneider` / `電力・インフラ企業の\n財務 約 12 年・約 10 年`
    - found c0 r3 `Oracle 創業(1977)` / `DB 事業を起こす`
    - mag c1 r0 self `Magouyrk(共同 CEO)` / `2014 年に OCI を創設\nGen2 を設計・統括`
    - sic c1 r1 self `Sicilia(共同 CEO)` / `業種別事業を統括\nアプリを AI で再構築`
    - max c1 r2 self `Maxson(CFO)` / `2026-04 就任\nCEO に報告`
    - ell c1 r3 `Ellison(会長・CTO)` / `株式 約 41%\nキーパーソン`
    - oci c2 r0 unit `OCI・AI 容量` / `IaaS +121%`
    - app c2 r1 unit `アプリ・業種別` / `SaaS +10%\nOracle Health`
    - cap c2 r2 unit `capex と資金調達` / `FY27 総額\n900〜950 億ドル`
    - pay c2 r3 risk `業績連動の報酬(PSO)` / `KPI は FY28 総売上\n(1 株指標ではない)`
    - rpo c3 r0 ok `受注残 6,640 億ドル` / `GPU 更新 +20%`
    - va c3 r1 risk `VA の電子カルテ` / `2026-03 に全国障害\n上限 100 億ドルを早期消化`
    - over c3 r2 risk `capex の超過` / `FY26 見通し 350 → 500\n→ 実績 557 億ドル`
    - gap c3 r3 risk `1 株価値とのずれ` / `総額の拡大に\n報酬が連動`
  - edges(経歴 → 現職は ctrl、現職 → 事業は ctrl、事業 → 結果は goods / risk):
    - aws → mag `基盤の技術`, ctrl, n 1
    - prim → sic `業種別ソフト`, ctrl, n 2
    - aes → max `電力の財務`, ctrl, n 3
    - found → ell, ctrl
    - mag → oci, ctrl
    - sic → app, ctrl
    - max → cap, ctrl
    - ell → pay `取締役会`, ctrl
    - oci → rpo `受注と更新`, goods
    - app → va `導入の遅れ`, risk
    - cap → over, risk, n 4(番号だけでよい)
    - pay → gap, risk, n 5(番号だけでよい)
- mechPanel(bottom 6.66):
  1. `Magouyrk は AWS でクラウド基盤を担い、2014 年に OCI を創設。今の成長エンジンを設計した当事者`
  2. `Sicilia は Primavera の技術者から CTO。買収後は業種別アプリを統括。Oracle Health(VA)は障害と遅れが続く`
  3. `CFO の Maxson は電力会社 AES と Schneider で財務を約 22 年。設備と電力の資金計画に合うが、就任 6 か月`
  4. `capex は FY26 に見通し 350 → 500 → 実績 557 億ドル。共同 CEO の資本配分の実績はまだ 1 年`
  5. `業績連動の報酬の KPI は FY28 の総売上で、1 株当たりの指標ではない(80% は時間ベース)`
  - reason: `経歴と事業の適合は高い(A 相当)。ただし CEO としての資本配分の実績が 1 年と短く、capex の超過と総額 KPI の報酬が残るため B(A との境界)`
  - up: `FY27 の capex が見通しの範囲に収まり、FCF の黒字化の時期を示せば A`
  - down: `capex が再び見通しを 10% 超上回るか、VA の契約で損失が出れば C`

## s23 条件7 安い理由の検証(C)
- kicker: `左から: 市場の疑い → 疑いの対象 → 証拠 → 判定。①〜④ は右と対応。株価は事業実態 EPS の 15.7 倍(弱気シナリオ 13.6 倍寄り)`
- source: `research2/R5_credit.md、research4/T2_company_rpo_capacity.md、research3/W2_gpu_economic_life.md、Bloomberg(2026-10-08)、S&P(2026-07)`
- grade 'C', condNo 7
- flowMap: h 4.66(KPI の帯あり)、cols [1.4, 1.35, 1.65, 1.2]、rows 4
  - lanes: `市場の疑い`(c0)/ `Oracle(疑いの対象)`(c1, self)/ `証拠`(c2)/ `判定`(c3)
  - nodes(行ごとに 疑い → 対象 → 証拠 → 判定 が並ぶ):
    - d1 c0 r0 `GPU 寿命の悲観` / `「2〜3 年で陳腐化」`
    - d2 c0 r1 `FCF の J カーブ` / `FY29 まで赤字`
    - d3 c0 r2 risk `OpenAI への集中` / `受注残の約 45%`
    - d4 c0 r3 risk `信用リスク` / `CDS 227bp\n2056 年債 8% 超`
    - o1 c1 r0 unit `GPU(自社調達)` / `6 年償却`
    - o2 c1 r1 unit `capex` / `FY27 900〜950 億ドル`
    - o3 c1 r2 unit `受注残` / `6,640 億ドル`
    - o4 c1 r3 unit `借入と格付け` / `BBB−(S&P)`
    - e1 c2 r0 ok `更新・再販 +20%` / `H100 を元の 95% で\n再契約した例`
    - e2 c2 r1 `S&P・コンセンサス` / `FY29 に FCF 黒字\n(エンジンは −135 億)`
    - e3 c2 r2 risk `OpenAI の資金` / `2026〜30 年の FCF\n累計 −2,780 億ドル`
    - e4 c2 r3 risk `S&P の条件` / `FY29 までに FOCF 黒字で\nなければ再格下げ`
    - v1 c3 r0 ok `見落とし` / `機会`
    - v2 c3 r1 `一部見落とし` / `時期は不確か`
    - v3 c3 r2 risk `実在` / `罠`
    - v4 c3 r3 risk `実在` / `罠`
  - edges(各行で直線):
    - d1 → o1 `寿命を疑う`, risk / e1 → o1 は置かず、o1 → e1 `反証`, ctrl, n 1 / e1 → v1, ctrl
    - d2 → o2 `赤字を疑う`, risk / o2 → e2 `裏付け`, ctrl, n 2 / e2 → v2, ctrl
    - d3 → o3 `集中を疑う`, risk / o3 → e3 `支払いは調達頼み`, risk, n 3 / e3 → v3, risk
    - d4 → o4 `信用を疑う`, risk / o4 → e4 `債券も同じ見方`, risk, n 4 / e4 → v4, risk
- mechPanel(bottom 6.32):
  1. `GPU 寿命の悲観は、更新・再販 +20% と H100 の再契約(元の 95%)が反証する。市場の見落とし`
  2. `FCF の赤字は契約済み需要への先行投資(J カーブ)。ただし黒字化は FY29 で、時期の不確かさは実在`
  3. `受注残の約 45% は OpenAI。OpenAI の FCF は 2026〜30 年累計 −2,780 億ドルで、支払いは資金調達頼み`
  4. `CDS 227bp と S&P の条件は、債券市場も同じリスクを価格に入れている証拠`
  - reason: `安さの主因は実在のリスク(OpenAI 集中と信用)で、見落としで説明できるのは GPU 寿命と J カーブの一部に限られるため C`
  - up: `OpenAI の比率が 40% 未満に下がり、CDS が 200bp 未満に戻れば B`
  - down: `CDS が 300bp を超えるか、FY29 より前に BB+ になれば D 候補`
- kpiBand: `CDS 5年 200bp 未満で確度を上げ、300bp 超で D 候補 / FY29 より前の BB+ で D 候補 / OpenAI の比率 40% 未満で確度を上げ、契約変更・支払遅延の報道で E 候補`

## s24 条件8 コモディティ性(C)
- kicker: `左から: 供給者 → Oracle の事業(1 株価値の内訳)→ 買い手 ← 代替と価格の基準。①〜⑤ は右と対応`
- source: `需給エンジン第4.3版(セグメント価値)、research3/W3_industry_structure.md、ICE・CME の発表(2026-05)、Epoch AI、SemiAnalysis ClusterMAX v3.0`
- grade 'C', condNo 8
- flowMap: h 4.66、cols [1.3, 1.55, 1.35, 1.4]、rows 3
  - lanes: `供給者`(c0)/ `Oracle の事業`(c1, self)/ `買い手`(c2)/ `代替・価格の基準`(c3)
  - nodes:
    - dbtech c0 r0 ok `DB の技術` / `代替なし`
    - nv c0 r1 `NVIDIA` / `AI 計算の約 8 割`
    - mem c0 r2 risk `メモリ・電力` / `逼迫は 2028 年まで`
    - diff c1 r0 unit `DB 保守・SaaS・OCI 一般` / `1 株 120 ドル\n(45 + 44 + 31)`、tag `差別化`(green)
    - ai c1 r1 rs 2 unit `AI 容量` / `1 株 117 ドル\n(価値の 45%)\n\n差: 電力の確保・\nRDMA 網・品質 Gold`、tag `緩和後は商品`(red)
    - ent c2 r0 `企業` / `データの近くで推論`
    - lab c2 r1 `AI 研究所` / `最も安い容量を選ぶ`
    - hyper c3 r0 `大手クラウド` / `H100 実勢\n7.19 ドル/時`
    - neo c3 r1 risk `ネオクラウド` / `H100 実勢\n2.80 ドル/時`
    - fut c3 r2 risk `価格指数・先物` / `Silicon Data・Ornn\nICE・CME が準備`
  - edges:
    - dbtech → diff, goods
    - ai → nv `GPU 代`, money
    - mem → ai `原価の上昇`, risk
    - diff → ent `代替なし`, goods, n 1
    - ai → lab `GPU 時間`, goods, n 2
    - neo → lab `約 2.6 倍安い`, risk, n 3
    - hyper → ent `DB の移行`, risk
    - fut → ai `価格の標準化`, risk, n 4(c2 r2 は空けて線を通す)
- mechPanel(bottom 6.32):
  1. `DB・Database@ はデータのある場所で動く。代替がなく、価格は Oracle が決める`
  2. `AI 容量の買い手は最も安い容量を選ぶ。Oracle の差は電力の確保・RDMA 網・品質(ClusterMAX Gold)`
  3. `ネオクラウドの H100 実勢は大手の約 2.6 倍安い。需給が緩むと限界供給者の損益分岐が価格になる`
  4. `価格指数と現金決済の先物(ICE・CME)が整い、GPU 時間の価格が標準化しつつある`
  5. `推論トークンの価格は、同じ性能で年 9〜900 倍の速さで下がっている(Epoch)`
  - reason: `価値の 45% を占める AI 容量が、逼迫の緩和後に商品として値決めされる層にあるため C`
  - up: `AI 粗利率 35% 以上が続き、緩和期に入っても更新プレミアムが正なら B`
  - down: `AI 粗利率が 25% 未満か、更新プレミアムが 0% 以下なら D 候補`
- kpiBand: `AI 粗利率(最終開示 32%)が 25% 未満で D 候補・35% 以上で B 候補 / 更新プレミアム(+20%)が 0% 以下で D 候補 / H100 1 年契約の指数(2.65 ドル)が 2.00 ドル未満`

## s25 条件9 運用上の不可欠性(B)
- kicker: `左から: 供給の基盤 → Oracle → 顧客の運用 ← 代替。①〜④ は右と対応`
- source: `会社開示(Q4 FY26・Q1 FY27 説明会)、research4/T4_ai_demand.md(McKinsey)、report/r3_sections_5w1h_f20.md §3-4`
- grade 'B', condNo 9
- flowMap: h 5.0、cols [1.35, 1.4, 1.55, 1.4]、rows 3
  - lanes: `供給の基盤`(c0)/ `Oracle`(c1, self)/ `顧客の運用`(c2)/ `代替`(c3)
  - nodes:
    - power c0 r0 ok `電力付きの建屋` / `Q1 FY27 に\n850MW を納入`
    - gpu c0 r1 `GPU クラスタ` / `稼働率 97.9%`
    - db c0 r2 ok `Oracle DB` / `基幹データ`
    - oci c1 r0 rs 2 self `OCI(AI 容量)` / `学習・推論の容量\n\nQ4 FY26: 顧客の 49% が\nGPU の 92% を更新`
    - dbs c1 r2 unit `DB・Database@` / `基幹業務の DB`
    - train c2 r0 `AI 研究所の学習` / `止まると開発が遅れる`
    - inf c2 r1 `AI 研究所の推論(本番)` / `止まると売上が止まる`
    - ent c2 r2 `企業の基幹業務と AI` / `DB 内のデータで推論`
    - alt1 c3 r0 risk `他社クラウド・\nネオクラウド` / `乗り換えに\n数か月〜数年`
    - alt2 c3 r1 risk `TPU・自社チップ` / `Anthropic は TPU\n約 3.5GW(2027〜)`
    - alt3 c3 r2 risk `DB の移行` / `数年がかり`
  - edges:
    - power → oci `容量`, goods
    - gpu → oci, goods
    - db → dbs, goods
    - oci → train `計算容量`, goods
    - oci → inf `本番の推論`, goods, n 1
    - dbs → ent `データと推論`, goods, n 3
    - alt1 → train `乗り換え`, risk, n 2
    - alt2 → inf `代替の計算`, risk, n 4
    - alt3 → ent `移行`, risk
- mechPanel(bottom 6.66):
  1. `推論は本番の稼働で、止まると顧客の売上が止まる。推論の電力比率は 2025 年 47.5% → 2030 年 60%`
  2. `乗り換えには電力付きの容量の確保が要り、数か月〜数年かかる`
  3. `企業の AI は Oracle DB 内のデータで動く。DB の移行には数年かかる`
  4. `Q4 FY26 は顧客の 49% が GPU の 92% を更新。ただし他社クラウドや TPU という代替がある`
  - reason: `電力付きの容量と DB は止められない運用を支え更新率も高いが、代替のクラウドが存在するため B`
  - up: `大型顧客の更新率が 90% を超え、乗り換えの事例が出なければ A`
  - down: `大型顧客が TPU や自社チップへ移る事例が出れば C`

## s26 条件10 陳腐化リスク(B)
- kicker: `左から: 資産 → 回収の経路 ← 価値を下げる力。下: 資産ごとの寿命と契約の長さ。①〜⑤ は右と対応`
- source: `research3/W2_gpu_economic_life.md、会社開示(耐用年数の変更、Q1 FY27 説明会)、JPMorgan AM の試算、Amazon 10-K`
- grade 'B', condNo 10
- flowMap: h 3.75(下に時間軸)、cols [1.45, 1.55, 1.35, 1.45]、rows 3
  - lanes: `資産`(c0)/ `Oracle の回収`(c1〜c2, self)/ `価値を下げる力`(c3)
  - nodes:
    - intang c0 r0 ok `DB の技術・顧客関係` / `寿命は数十年`
    - soft c0 r1 `OCI のソフト` / `世代交代が速い`
    - gpu c0 r2 risk `GPU(自社調達)` / `6 年償却\n(5 → 6 年に延長)`
    - maint c1 r0 unit `保守・SaaS` / `継続課金`
    - first c1 r1 unit `最初の契約` / `5〜6 年\n契約 ≒ 償却期間`
    - renew c1 r2 unit `更新・再販` / `従来比 +20%\n(Q1 FY27)`
    - cust c2 r0 `DB・SaaS の顧客` / `保守料`
    - lab c2 r1 rs 2 `AI 研究所・企業` / `初回の契約料\n\n更新料`
    - nv c3 r0 risk `NVIDIA の新世代` / `Rubin は電力あたり\n約 10 倍`
    - used c3 r1 `中古 GPU 市場` / `中古 H100 は新品の\n61% → 69%`
    - amzn c3 r2 risk `Amazon の判断` / `サーバーの耐用年数を\n6 → 5 年に短縮`
  - edges:
    - intang → maint, goods, n 1
    - gpu → first, goods, n 2
    - gpu → renew, goods(番号なし)
    - cust → maint `保守料`, money
    - lab → first, money
    - lab → renew `+20%`, money, n 3
    - nv → gpu `置き換えを迫る`, risk, n 4(c1・c2 の行 0 を横切るときは fs/ts を調整するか、nv を r2 側に寄せる)
    - used → renew `再販の値`, ctrl
    - amzn → gpu `寿命の見方`, risk
- timeBand: x 0.5, y 5.5, w 8.55, h 1.1, from 2027, to 2047, step 5, fmt `t => 'FY' + (t % 100)`、bars:
  - `GPU の最初の契約` 2027〜2032, color L.C.primary, text `5〜6 年`
  - `GPU の償却` 2027〜2033, color L.C.amber, text `6 年`
  - `建屋のリース` 2027〜2045, color L.C.light, text `15〜19 年(GPU の 2〜3 世代分)`
  - `DB の技術・顧客関係` 2027〜2047, color L.C.dark, text `数十年`
- mechPanel(bottom 6.66):
  1. `DB の技術と顧客関係は数十年使われ、保守料で回収が続く`
  2. `GPU は最初の 5〜6 年の契約で償却の大半を回収する(契約期間 ≒ 償却期間)`
  3. `更新期の GPU は従来比 +20% で更新・再販。CoreWeave も H100 を元の 95% で再契約`
  4. `新世代(Rubin は電力あたり約 10 倍)が出ると、電力が限られる中で旧世代の置き換えを迫られる`
  5. `建屋のリースは 15〜19 年で GPU の 2〜3 世代分。需要が鈍れば固定費として残る`
  - reason: `経済的寿命が会計の耐用年数以上であることを示す証拠が優勢。ただし電力制約の下での世代交代の速さが残るため B`
  - up: `大型契約の更新(2031 年〜)で元の単価の 6 割以上が確認できれば A`
  - down: `更新プレミアムが 0% 以下に落ちれば C(3 年耐用なら EPS −17%、JPMorgan AM の試算)`

## s27 条件11 模倣困難性(B)
- kicker: `左から: Oracle の資産 → 再現に要るもの → 再現にかかる時間 ← 競合。①〜④ は右と対応`
- source: `research3/W3_industry_structure.md、research4/T5_supply_components.md、research4/T2_company_rpo_capacity.md、GE Vernova・PJM の開示`
- grade 'B', condNo 11
- flowMap: h 5.0、cols [1.45, 1.5, 1.2, 1.45]、rows 4
  - lanes: `Oracle の資産`(c0, self)/ `再現に要るもの`(c1)/ `時間`(c2)/ `競合`(c3)
  - nodes:
    - base c0 r0 ok `DB の顧客基盤` / `数十年の導入実績`
    - place c0 r1 ok `Database@ の配置` / `70 リージョン\n119 AZ`
    - cap c0 r2 unit `AI 容量` / `10GW 超を確保\n(FY29 まで)`
    - bld c0 r3 unit `電力付きの建屋` / `90% 超を\nパートナーが負担`
    - mig c1 r0 `データ移行・\nアプリ改修` / `顧客側に数年`
    - part c1 r1 `競合クラウドとの提携` / `AWS・Azure・Google\nの合意`
    - money c1 r2 `資本` / `1GW あたり\n数百億ドル`
    - grid c1 r3 risk `電力・系統` / `連系 約 40 か月\nタービンは 2031 年分を販売中`
    - t1 c2 r0 ok `10 年超` / `実質再現できない`
    - t2 c2 r1 ok `提携先次第` / ``
    - t3 c2 r2 risk `2〜4 年` / `資本があれば`
    - t4 c2 r3 risk `3〜4 年` / `電力の確保`
    - pg c3 r0 `他社 DB` / `PostgreSQL ほか`
    - hyp c3 r1 `大手クラウド` / `自社 DB を推す`
    - neo c3 r2 risk `ネオクラウド・大手` / `実際に建設中`
    - util c3 r3 `電力会社・開発事業者` / `ほかの顧客にも供給`
  - edges(行ごとに 資産 → 要るもの → 時間 ← 競合):
    - base → mig, ctrl, n 1 / mig → t1, ctrl / pg → t1 `追随できない`, risk
    - place → part, ctrl, n 2 / part → t2, ctrl / hyp → t2 `提携が要る`, risk
    - cap → money, ctrl, n 3 / money → t3, ctrl / neo → t3 `追随`, risk
    - bld → grid, ctrl, n 4 / grid → t4, ctrl / util → t4 `奪い合い`, risk
- mechPanel(bottom 6.66):
  1. `DB の顧客基盤は数十年の導入とデータ移行の重さで、資本があっても再現できない`
  2. `Database@ は競合クラウドの DC 内に置く提携で、他社が同じ配置を得るのは難しい`
  3. `AI 容量は資本と電力があれば 2〜4 年で再現できる。大手・ネオクラウドが実際に建設中`
  4. `障壁として効くのは電力。系統連系に約 40 か月、ガスタービンは 2031 年分を販売中`
  - reason: `DB と配置は模倣が難しいが、AI 容量の障壁は時間にすぎず、資本のある競合には破られるため B`
  - up: `FY30〜32 分の電力を確保し、競合に 3 年以上先行できれば A`
  - down: `競合の大型容量が 2027〜28 年に相次いで稼働し、AI 容量の単価が下がれば C`
