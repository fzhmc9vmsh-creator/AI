# 指示書: 第3章 13条件の構造分析(s16〜s29)

先に spec/common.md を読む。手本は `/home/user/AI/reports/ORCL/work/deck/slides/` の指定ファイル。
担当: s17・s18・s19・s21・s23・s24・s26・s28 = Sonnet(関係図)。s16・s22・s29 = Haiku。

関係図の共通(Sonnet):
- `L.flowMap` + `L.mechPanel`。kind は手本と同じ意味(unit = 自社の事業・機能、self = 自社の成果、key = 柱、ok = 強み、risk = 弱み・脅威、無指定 = 外部)。
- 評価 B のスライドは手本 ORCL s17〜s19 の高さ(timeBand があれば h 3.75、無ければ h 5.0、mechPanel bottom 6.66)。
- 評価 C のスライドは手本 ORCL s23・s24 と同じく flowMap h 4.66、mechPanel bottom 6.32、下端に `L.kpiBand`。
- 箱の sub は削ってよいが数値は残す。線のラベルが重なるときは、ラベルを短くするか番号だけにする(数量のある線のラベルは残す)。
- 上がる条件・下がる条件は mechPanel の up / down に入れる(文頭の「上がる条件」は lib が付ける)。

---------------------------------------------------------------------
## s16 中扉(Haiku。手本 ORCL s16)
- `return L.agenda(pres, 2);`

---------------------------------------------------------------------
## s17 条件1 競争優位の持続(評価 B。Sonnet。手本 ORCL s17)
- contentSlide: kicker `左から: 会員 → SoFi の事業 → 優位の源泉 ← 競合の圧力。下: 優位が続く期間。①〜⑥ は右と対応。数値は Q2 2026`、source `会社開示(Q2 2026 決算)、research_r2/R7_funding_rates_capital.md・R9_products_people.md、research/R4_scuttlebutt.md(各社 APY・価格表の第三者集計)`、grade `B`、condNo `1`
- flowMap: name `s17`、h 3.75、cols [1.45, 1.4, 1.45, 1.3]、rows 3、nodeH 0.72
- lanes: `会員`(c0)/ `SoFi の事業と優位の源泉`(c1〜c2、self)/ `競合`(c3)
- groups: `事業`(c1、r0〜r2)、`優位の源泉`(c2、r0〜r2)
- nodes(12):
  - c0 r0 `dd` `給与振込の会員` sub `預金の約 9 割\n普通預金 3.30%`
  - c0 r1 `borrow` `借りる会員` sub `FICO 746\n金利を比べて選ぶ`
  - c0 r2 `inv` `投資・カードの会員` sub `Invest 390 万口座\nPlus 有料 20.6 万人`
  - c1 r0 `dep`(unit)`SoFi Money(預金)` sub `455 億ドル\n平均 3.07%`
  - c1 r1 `bs`(unit)`B/S 貸出` sub `APR 6.99〜35.49%\nNIM 5.98%`
  - c1 r2 `cross`(unit)`クロスバイ` sub `新製品の 51% は既存会員\n1 会員 1.54 製品`
  - c2 r0 `fund`(ok)`銀行免許と安い資金` sub `倉庫ラインより 1.56pt 安い\n(前年 1.87pt)`、tag `{ text: '縮小中', tone: 'amber' }`
  - c2 r1 `price`(risk)`価格の優位` sub `APR 帯は競合と重なる`、tag `{ text: 'なし', tone: 'red' }`
  - c2 r2 `brand`(ok)`ブランドと関係` sub `想起 10.4%(+1.9pt)\n販促費 3.9 億ドル/四半期`、tag `{ text: '販促次第', tone: 'amber' }`
  - c3 r0 `banks`(risk)`オンライン銀行` sub `Chime 3.75%・Amex 3.90%\nCapital One 3.50%`
  - c3 r1 `lenders`(risk)`ローン専業` sub `LightStream 6.49〜25.39%\nLendingClub 5.96〜35.99%`
  - c3 r2 `neo`(risk)`Robinhood・Chime` sub `給与振込と会員を\n取りに来る`
- edges:
  - dd → dep `給与振込` money n1
  - fund → dep `安く集める` ctrl n2
  - dep → bs `安い資金` money n3
  - borrow → bs `利息 13%` money
  - lenders → price `同じ価格帯` risk n4、price → bs `市場並みの価格` ctrl
  - inv → cross `製品を足す` money、brand → cross `定着させる` ctrl n5
  - banks → fund `高い金利で引き抜く` risk n6、neo → brand `会員の奪い合い` risk
- 左下 `L.text(s, '優位が続く期間', …)` と `L.timeBand`(手本と同じ x 0.5, y 5.5, w 8.55, h 1.1。from 2026, to 2036, step 2, name `s17tb`, fmt は年の数字のまま):
  - `銀行免許` 2026〜2036 dark `10 年超`
  - `給与振込の関係(安い資金)` 2026〜2034 primary `7〜10 年(差は縮小中)`
  - `ブランド` 2026〜2030 light `販促を続ける限り`
- mechPanel(bottom 6.66、mechH は手本どおり 2.0 から文字量で調整):
  1. `給与振込の会員が預金の約 9 割。普通預金 3.30% は Chime 3.75%・Amex 3.90% より低いのに預金が残る`
  2. `銀行免許で集めた預金は倉庫ラインより 1.56pt 安い。ただし前年の 1.87pt から縮んだ`
  3. `安い資金が B/S の貸出を支え、NIM は 5.98%`
  4. `個人ローンの APR 6.99〜35.49% は LightStream・LendingClub と重なり、価格では勝っていない`
  5. `ブランド(非助成想起 10.4%)とクロスバイ 51% で会員当たり 1.54 製品。販促費は四半期 3.9 億ドル(+48%)`
  6. `Robinhood・Chime も給与振込と会員を取りに来ており、資金の差を縮める圧力が続く`
  - reason `優位は価格ではなく、給与振込の関係が\n生む安い資金。7〜10 年続くと見るが、\n差は縮小中で圧倒的ではないため B`
  - up `倉庫ライン比の差が 1.5pt 以上を保ち、\n給与振込の預金が貸出と同じ速さで伸びれば A`
  - down `差が 1.2pt を割れば C`

---------------------------------------------------------------------
## s18 条件2 コア事業の稼ぐ力と資本(評価 C。Sonnet。手本 ORCL s18 の配置 + ORCL s23 の高さと kpiBand)
- contentSlide: kicker `左から: 資金の出し手 → SoFi の資本の源 → 使い道と結果 → 評価。①〜⑥ は右と対応。数値は Q2 2026(2026-06-30)と需給エンジン`、source `会社開示(10-Q Q2 2026、自己資本比率の表)、research_r2/R7_funding_rates_capital.md、calc/out/val.json(engine_detail・steady_state・rotce)`、grade `C`、condNo `2`
- flowMap: name `s18`、h 4.66、cols [1.35, 1.45, 1.45, 1.35]、rows 4
- lanes: `資金の出し手`(c0)/ `SoFi`(c1〜c2、self)/ `評価`(c3)
- groups: `資本の源`(c1、r0〜r3)、`使い道と結果`(c2、r0〜r3)
- nodes(14):
  - c0 r0 `eq` `株主` sub `2025 年に 33 億ドル増資\n(20.85・27.50 ドル)`
  - c0 r1 `dep` `預金者` sub `455 億ドル`
  - c0 r2 `mem` `借りる会員` sub `組成 107 億ドル/四半期\n(+54%)`
  - c0 r3 `buyers` `ローンの買い手` sub `LPB 契約\n100 億ドル超`
  - c1 r0 `cap`(key)`自己資本` sub `91.7 億ドル\n総自己資本比率 18.8%`
  - c1 r1 `ni`(unit)`利益` sub `2026 年 8.3 億ドル\n(エンジン)`
  - c1 r2 `sbc`(unit)`株式報酬` sub `年 2.6 億ドル\n(資本に加わる)`
  - c1 r3 `floor`(risk)`運用の下限` sub `比率 14〜15%\n(10% 台前半〜半ば)`
  - c2 r0 `rwa`(risk)`リスク資産(RWA)` sub `372 → 487 億ドル\n(半年で +31%)`
  - c2 r1 `bs`(unit)`B/S 貸出` sub `NIM 5.98%`
  - c2 r2 `lpb`(ok)`LPB` sub `資本を使わない\n手数料 4.6%`
  - c2 r3 `steady`(unit)`定常の稼ぐ力` sub `成長を止めれば\n純利益 約 15 億ドル`
  - c3 r0 `rotce`(risk)`ROTCE` sub `2026 年 7〜9%\n資本コスト 13.9%`
  - c3 r2 `tbv` `TBVPS` sub `7.34 ドル\n(増資で +56%)`
- edges:
  - eq → cap `増資 33 億` money n1
  - ni → cap `年約 11 億(株式報酬込み)` money n2、sbc → ni(ラベルなし)money
  - dep → bs `預金` money、mem → bs `利息` money
  - bs → rwa `貸出が増える` goods n3、rwa → cap `必要資本 年約 30 億` risk n3
  - cap → floor `2027 年に下限` risk n4
  - bs → lpb `抱えきれない分` goods n5、lpb → buyers `引き渡し` goods
  - steady → rotce `成長の先行費用` ctrl n6、cap → tbv(ラベルなし)ctrl
  - 線が混む場合は sbc → ni と cap → tbv を消してよい
- mechPanel(bottom 6.32):
  1. `2025 年の増資 33 億ドルで総自己資本比率は 22.9% に。TBVPS は 7.34 ドル`
  2. `自前の資本生成は、利益と株式報酬で年約 11 億ドル`
  3. `上期の貸出の伸びが続くと、必要資本は年約 30 億ドルで自前の約 3 倍。比率は半年で 22.9% → 18.8%`
  4. `このままでは 2027 年に運用の下限(14〜15%)に当たる`
  5. `その先は資本を使わない LPB に回すか増資。CFO は「現行計画では増資は不要」`
  6. `今の規模で成長を止めれば純利益は約 15 億ドル(1 株 9.06 ドル)。今は成長の先行費用で ROTCE 7〜9%`
  - reason `定常なら稼ぐが、成長が資本を食う。\nROTCE が資本コスト 13.9% を超えるのは\n2029〜30 年のため C`
  - up `ROTCE 12% 以上と比率 16% 以上を保ち、\nLPB の比率が上がれば B`
  - down `ROTCE 9% 未満が続くか、比率 15% 未満・\n増資なら D`
- kpiBand: `総自己資本比率 16% 未満で警戒・14% 未満で D 候補 / ROTCE 12% 以上で B 候補・9% 未満が 2 四半期続けば D 候補 / 増資の発表で D 候補(毎四半期)`

---------------------------------------------------------------------
## s19 条件3 資産の転用(評価 B。Sonnet。手本 ORCL s19)
- contentSlide: kicker `左から: 既存の資産 → 転用の経路 → 新しい収益 ← 外部。①〜④ は右と対応。数値は Q2 2026`、source `会社開示(Q2 2026 決算・説明会)、research_r2/R9_products_people.md、research/R1b_kpi.md・R4_scuttlebutt.md`、grade `B`、condNo `3`
- flowMap: name `s19`、h 5.0、cols [1.35, 1.4, 1.4, 1.25]、rows 4、nodeH 0.8
- lanes: `既存の資産`(c0)/ `SoFi の転用と成果`(c1〜c2、self)/ `外部`(c3)
- groups: `転用の経路`(c1、r0〜r3)、`新しい収益`(c2、r0〜r3)
- nodes(14):
  - c0 r0 `mem`(ok)`会員 1,580 万人` sub `+35%\n1 会員 1.54 製品`
  - c0 r1 `orig`(ok)`組成の能力` sub `個人ローン組成\n107 億ドル/四半期`
  - c0 r2 `charter`(ok)`銀行免許と預金` sub `455 億ドル`
  - c0 r3 `tech` `技術基盤` sub `Galileo・Technisys`
  - c1 r0 `cross`(unit)`クロスバイ` sub `新製品の 51% は\n既存会員`
  - c1 r1 `lpbc`(unit)`LPB 契約` sub `Blue Owl 最大 50 億ドル\nほか 100 億ドル超`
  - c1 r2 `chain`(unit)`銀行の新商品` sub `暗号資産 2025-11 再開\nSoFiUSD 2026-05`
  - c1 r3 `ext`(unit)`外販` sub `他社に口座基盤を提供`
  - c2 r0 `fs`(self)`FS 手数料` sub `0.87 億ドル\n(+81%)`
  - c2 r1 `lpb`(self)`LPB` sub `年 5.6 億ドル\n(+11%)`
  - c2 r2 `newb`(self)`新領域` sub `SoFiUSD 流通 約 3 億ドル\n中小企業ローン 2026-06〜`
  - c2 r3 `gal`(risk)`Galileo` sub `収益 −23%\n大口顧客が離脱`
  - c3 r1 `buyers` `ローンの買い手` sub `Blue Owl・Fortress・\nBasePoint(3 年 30 億ドル)`
  - c3 r3 `chime`(risk)`Chime` sub `自社基盤へ移行\n解約料 1,800 万ドル`
- edges:
  - mem → cross `既存会員` ctrl n1、cross → fs `手数料` money
  - orig → lpbc `組成して渡す` goods n2、lpbc → lpb `手数料 4.6%` money、buyers → lpb `額面+手数料` money
  - charter → chain `銀行が発行` ctrl n3、chain → newb `流通` money
  - tech → ext ctrl、ext → gal `処理料` money n4、chime → gal `離脱` risk
- mechPanel(bottom 6.66):
  1. `会員 1,580 万人に製品を足す。新製品の 51% は既存会員が開き、FS 手数料は 0.87 億ドル(+81%)`
  2. `組成の能力を他社の資金に貸す。LPB 契約は 100 億ドル超、手数料は年 5.6 億ドル(+11%)`
  3. `銀行免許の上に暗号資産(2025-11 再開)と SoFiUSD(2026-05)を載せた。流通は約 3 億ドルでまだ小さい`
  4. `技術基盤の外販は、大口顧客(Chime)が自社基盤へ移り −23%。転用の失敗例`
  - reason `会員と組成の基盤の転用は成果が出たが、\n新領域はまだ小さく、技術基盤の外販は\n縮んでいるため B`
  - up `LPB 手数料が年 7 億ドルを超え、\nFS 手数料が +40% 以上を保てば A`
  - down `LPB 組成が四半期 30 億ドルを割り、\nGalileo の流出が続けば C`

---------------------------------------------------------------------
## s21 条件5 経営者の能力(評価 B。Sonnet。手本 ORCL s21 と deck/examples/s21_condition5_career.js)
- contentSlide: kicker `左から: 経歴(どこで何を築いたか)→ 現職 → 担う事業 → 結果。①〜⑤ は右と対応。経歴は会社発表・報道の要約に基づく`、source `research/R3b_management.md、research_r2/R9_products_people.md(会社発表・DEF 14A・Form 4 の要約)`、grade `B`、condNo `5`
- flowMap: name `s21`、h 5.0、cols [1.5, 1.45, 1.4, 1.45]、rows 4、nodeH 0.82
- lanes: `経歴`(c0)/ `経営陣と担う事業`(c1〜c2、self)/ `結果`(c3)
- nodes(13〜14。手本の並べ方: c0 経歴、c1 人、c2 担う事業、c3 結果):
  - c0 r0 `gs`(ok)`Goldman Sachs` sub `Noto: 1999〜、2004 パートナー\nTMT 投資銀行の共同責任者`
  - c0 r1 `tw` `NFL・Twitter の CFO` sub `Noto: NFL 2008〜10\nTwitter CFO 2014〜17・COO`
  - c0 r2 `uber` `Goldman・Uber` sub `Lapointe: GS 2012〜15\nUber 2015〜18`
  - c0 r3 `cons`(ok)`消費者金融・資産運用` sub `JPM 住宅ローン CFO・Capital One・\nCitizens/Schwab・JPM`
  - c1 r0 `noto`(self)`Noto\n(CEO)` sub `2018-02 就任\nWest Point・Wharton`
  - c1 r1 `lap`(self)`Lapointe\n(CFO)` sub `2018 入社\n2020-09 CFO`
  - c1 r2 `sch`(self)`Schuppenhauer\n(貸出の責任者)` sub `2024-08 入社`
  - c1 r3 `keo`(self)`Keough\n(FS の責任者)` sub `2023-03 入社`
  - c2 r0 `bank`(unit)`銀行化と資本` sub `免許・増資・資本配分`
  - c2 r1 `fin`(unit)`財務とガイダンス` sub `利益計画・開示`
  - c2 r2 `lend`(unit)`個人・学生・住宅ローン` sub `与信と SoFi Bank`
  - c2 r3 `fsb`(unit)`預金・投資・保険` sub `Spend・Invest・Protect・Save`
  - c3 r0 `res1`(ok)`銀行免許 2022 年\nGAAP 黒字 Q4 2023` sub `約束した時期どおり`
  - c3 r1 `res2`(ok)`2025 年は計画超え` sub `EPS 計画 0.25〜0.27\n→ 実績 0.39`
  - c3 r2 `res3`(risk)`未達と未検証` sub `上場時の 2024 年予測に収益 −7%\nTechnisys の効果は未検証`
  - 箱が 15 を超えるので、c3 は 3 箱にし、res3 を c3 r2.5(rs 1)にするか、r3 にまとめる。合計 15 になる場合は gs と tw を 1 箱(`Goldman・NFL・Twitter`)にまとめて 14 にする
- edges: gs → noto `資本市場`、tw → noto `上場企業の財務`、uber → lap `財務・成長`、cons → sch `消費者金融`、cons → keo `資産運用`、noto → bank n1、lap → fin n2、sch → lend n3、keo → fsb n4、bank → res1、fin → res2、lend → res3(すべて ctrl。番号は手本どおり右の仕組みと対応させる)
- mechPanel(bottom 6.66):
  1. `Noto は GS で資本市場、Twitter で上場企業の財務を担った。銀行免許(2022)と GAAP 黒字(Q4 2023)を約束どおり達成`
  2. `Lapointe は GS・Uber で財務を担い、2025 年は利益計画(EPS 0.25〜0.27)を上回る 0.39`
  3. `貸出は JPM 住宅ローン CFO・Capital One・Citizens の消費者金融を経た Schuppenhauer が率いる`
  4. `預金・投資・保険は Schwab・JPM で資産運用を担った Keough が率いる`
  5. `報酬の PSU は TBV の総額の伸びに連動し、1 株当たりではない。増資で総額は伸びる。CEO は 2026 年に約 225 万ドル(15.73〜18.06 ドル)を買い増し、1,228 万株を保有`
  - reason `その事業を築いた経験の持ち主が\n貸出と預金を率い、約束の実行力は高い。\n報酬が 1 株当たりでない点で B`
  - up `報酬を 1 株当たりの指標に切り替え、\nROTCE 目標の時期を示せば A`
  - down `利益計画の下方修正か、\n低い株価での増資なら C`

---------------------------------------------------------------------
## s22 条件6 成長と割安度(評価 B。Haiku。手本 ORCL s22 を写経: 表 + 箇条書き + 縦棒 + t15Side)
- contentSlide: kicker `条件6 3 年 EPS 成長率で PEG<1(EPS CAGR 30% 前後)。EPS は調整後(会社定義)。PER は株価 14.55 ドル ÷ 2026 年 EPS 0.60`、source `コンセンサス(research_r2/R8_peers_consensus.md)、会社の中期目標(2025〜28 年の調整後 EPS CAGR 38〜42%、2026-01-30。上端 42% を 2028 年まで使い、以降は +32%・+25%)、需給エンジン(calc/out/val.json の paths)`、grade `B`、condNo `6`(title・page は書かない)
- 表(手本と同じ位置・列幅): 見出し `['経路', '2026', '2029', '3 年 CAGR', 'PER', 'PEG']`
  - `['コンセンサス', '0.60', '1.32', '30.1%', '24.3', '0.81']`
  - `['会社の目標(42%)の延長', '0.60', '1.47', '34.9%', '24.3', '0.70']`
  - `['需給エンジン', '0.60', '1.35', '31.1%', '24.3', '0.78']`
- bullets(手本の位置):
  - `年ごとの伸びはエンジンで +41% → +31% → +22% → +23%、コンセンサスで +38% → +30% → +22% → +18%。2029 年以降は 20% 台`
  - `5 年(2025 年 0.39 ドル → 2030 年)ではコンセンサス 32.0%、エンジン 33.6%。2025 年の低い起点が率を押し上げている`
  - `条件7 が C(安い理由の主因は実在のリスク)のため、規則により B が上限`
- 縦棒(手本の chart_cagr と同じ位置): labels `['コンセンサス', '会社の目標の延長', '需給エンジン']`、values `[30.1, 34.9, 31.1]`、valAxis 0〜40。注記 `閾値 30%`(手本と同じ置き方)
- t15Side: evidence [`PER 24.3 倍 = 14.55 ÷ 2026 年 EPS 0.60`, `3 年 CAGR は 2026 → 2029 年`, `コンセンサスとエンジンの差は 2029 年で 0.03 ドル(EPS に差分なし)`]、reason `数値は PEG<1 を満たすが、余裕が小さく\n条件7 と対で評価して B`

---------------------------------------------------------------------
## s23 条件7 安い理由の検証(評価 C。Sonnet。手本 ORCL s23)
- contentSlide: kicker `左から: 市場の懸念(出所)→ 懸念の対象 → 事実 → 判定。①〜④ は右と対応。株価は 2026 年 EPS の 24.3 倍、2027 年の 17.2 倍`、source `research/R3a_market_hypothesis.md(Muddy Waters・KBW・Morgan Stanley・BofA の要約)、research_r2/R5_credit_fv.md・R7_funding_rates_capital.md・R6_pnl_margin.md`、grade `C`、condNo `7`
- flowMap: name `s23`、h 4.66、cols [1.5, 1.4, 1.6, 1.1]、rows 4
- lanes: `市場の懸念`(c0)/ `SoFi(懸念の対象)`(c1、self)/ `事実`(c2)/ `判定`(c3)
- nodes(14):
  - c0 r0 `d1` `会計への疑い(MW)` sub `実質の貸倒 6.1%\n未計上の債務 3.12 億ドル`
  - c0 r1 `d2`(risk)`金利と公正価値(KBW)` sub `Q3 に 10 億ドル超の逆風`
  - c0 r2 `d3`(risk)`資本を食う成長(MS)` sub `成長が資本集約的`
  - c0 r3 `d4`(risk)`利益が付いてこない(BofA)` sub `売上は上方修正\n利益計画は据え置き`
  - c1 r0 `o1`(unit)`貸倒と損失の前提` sub `公正価値の損失前提 4.8%`
  - c1 r1 `o2`(unit)`ローンの評価` sub `マーク 個人 104.7%`
  - c1 r2 `o3`(unit)`自己資本` sub `比率 18.8%`
  - c1 r3 `o4`(unit)`下期の利益計画` sub `通期 EPS 0.60 ドル`
  - c2 r0 `e1`(ok)`前提 4.8% > all-in 3.7%` sub `売却した延滞債権を\n足し戻しても内側`
  - c2 r1 `e2`(risk)`割引率が薄い` sub `個人 4.97%・学生 4.29%\nQ3 ヘッジ前 −4.5〜6.5 億ドル`
  - c2 r2 `e3`(risk)`比率の低下` sub `半年で 22.9% → 18.8%`
  - c2 r3 `e4`(risk)`下期に高い増分利益率` sub `増分 EBITDA 率 53〜64%\n(前年は 36%)`
  - c3 r0 `v1`(ok)`会計の不正は\n裏付けが弱い`
  - c3 r2(rs 2 にできれば 2 行分)`v2`(risk)`金利・資本・信用は\n実在のリスク`
- edges:
  - d1 → o1 `疑い` risk n1、o1 → e1 ctrl、e1 → v1 ctrl
  - d2 → o2 `疑い` risk n2、o2 → e2 ctrl、e2 → v2 ctrl
  - d3 → o3 risk n3、o3 → e3 ctrl、e3 → v2 ctrl
  - d4 → o4 risk n4、o4 → e4 ctrl、e4 → v2 ctrl
- mechPanel(bottom 6.32):
  1. `MW は実質の貸倒 6.1% を主張。会社の公正価値の損失前提 4.8% は、売却した延滞債権を足し戻した all-in 3.7% より高く、利益の水増しの裏付けは弱い`
  2. `ただし割引率は個人 4.97%・学生 4.29% と薄い。Q3 の金利上昇(+55〜60bp)でヘッジ前 −4.5〜6.5 億ドルの評価減を見込む`
  3. `資本比率は半年で 4.1pt 下がった。成長を続けるには LPB か増資が要る`
  4. `下期の利益計画は増分 EBITDA 率 53〜64% を要し、前年の 36% より高い`
  - reason `安さの主因は見落としではなく、\n金利・資本・信用という実在のリスク。\n会計の疑いは弱いため C`
  - up `Q3 のマークが 104% 以上、all-in 貸倒率 4.0% 以下、\n下期の計画を達成すれば B`
  - down `マークが 103% 未満、all-in 4.8% 超、\n再表示があれば D`
- kpiBand: `個人ローンのマーク 104% 以上で B 候補・103% 未満で D 候補 / all-in 貸倒率 4.0% 以下で確度を上げ・4.8% 超で D 候補(損失前提を超える)/ 再表示・当局の調査で E 候補(毎四半期)`

---------------------------------------------------------------------
## s24 条件8 コモディティ性(評価 C。Sonnet。手本 ORCL s24)
- contentSlide: kicker `左から: 借り手 → SoFi の事業 → ローンの買い手 ← 価格の基準。①〜⑤ は右と対応。収益の内訳は Q2 2026`、source `会社開示(Q2 2026 決算・10-Q)、research_r2/R9_products_people.md(各社の価格表)、research/R4_scuttlebutt.md(LPB 契約・プライベートクレジット)`、grade `C`、condNo `8`
- flowMap: name `s24`、h 4.66、cols [1.2, 1.45, 1.4, 1.35]、rows 3
- lanes: `借り手`(c0)/ `SoFi の事業`(c1、self)/ `ローンの買い手`(c2)/ `価格の基準`(c3)
- nodes(12):
  - c0 r0 `borrow` `借りる会員` sub `FICO 746\n金利を比べて選ぶ`
  - c0 r1 `rel`(ok)`会員との関係` sub `クロスバイ 51%\n1 会員 1.54 製品`
  - c0 r2 `dd`(ok)`給与振込の預金` sub `平均 3.07%`
  - c1 r0 `nii`(unit)`貸出の利ざや` sub `収益の 65%\nNIM 5.98%`、tag `{ text: '商品', tone: 'red', above: true }`
  - c1 r1 `lpb`(unit)`LPB・売却益` sub `収益の 24%`、tag `{ text: '商品', tone: 'red', above: true }`
  - c1 r2 `fee`(unit)`手数料・会費` sub `収益の 11%`、tag `{ text: '差別化', tone: 'green', above: true }`
  - c2 r0 `bo` `Blue Owl・Fortress` sub `LPB 契約\n100 億ドル超`
  - c2 r1 `pc`(risk)`プライベートクレジット` sub `個人ローン組成の約 1/4\nに資金(前年 6%)`
  - c2 r2 `bank` `銀行・ABS の投資家` sub `全額売却 106.5%\n(Q4 2025)`
  - c3 r0 `apr`(risk)`競合の APR` sub `LendingClub 5.96〜35.99%\nLightStream 6.49〜25.39%`
  - c3 r1 `par`(risk)`売却の価格` sub `ほぼ額面 + 手数料 4.6%`
  - c3 r2 `brand`(ok)`ブランド` sub `想起 10.4%`
- edges:
  - borrow → nii `利息 13%` money n1、apr → borrow `比べる` risk
  - nii → lpb `抱えきれない分` goods n2、lpb → bo `引き渡し` goods、par → lpb `価格の上限` risk n3
  - pc → bo(ラベルなし)risk n4
  - rel → fee `製品を足す` money n5、dd → nii `安い資金` ctrl、brand → rel ctrl
- mechPanel(bottom 6.32):
  1. `借り手は FICO 746 の優良層で、金利を比べて選ぶ。APR 帯は LendingClub・LightStream と重なる`
  2. `抱えきれないローンは LPB と売却で他社に渡す。収益の 24%`
  3. `買い手はほぼ額面と手数料 4.6% で買う。市場で値の付く商品で、上乗せは小さい`
  4. `プライベートクレジットは 2025 年の個人ローン組成の約 1/4 に資金を出し(前年 6%)、競合にも同じ資金が回る`
  5. `差別化は会員との関係(クロスバイ 51%)と安い預金。商品の部分が収益の約 6 割を占める`
  - reason `ローンは市場で値の付く商品。\n差別化は会員との関係と預金にあり、\n収益の約 6 割が商品の性格のため C`
  - up `NIM 5.8% 以上と LPB 手数料率 4.5% 以上を\n保てば B`
  - down `NIM 5.3% 未満か、手数料率 3.5% 未満なら D`
- kpiBand: `NIM 5.8% 以上で B 候補・5.3% 未満で D 候補 / LPB の手数料率 4.5% 以上で確度を上げ・3.5% 未満で D 候補(毎四半期)`

---------------------------------------------------------------------
## s26 条件10・11 模倣困難性と陳腐化(評価 B・B。Sonnet。手本 ORCL s26)
- contentSlide: kicker `左から: 再現に時間がかかる資産 / 陳腐化しうる資産 ← 競合の動き。下: 資産ごとの持ちの長さ。①〜⑤ は右と対応`、source `会社開示(Q2 2026 決算)、research/R4_scuttlebutt.md(Chime の S-1、Robinhood・LendingClub の Q2 2026 決算)、research_r2/R9_products_people.md`、grade `B`、condNo `'10・11'`
- flowMap: 手本と同じ name `s26`、y 1.66、h 3.75、cols [1.45, 1.55, 1.35, 1.45]、rows 3、nodeH 0.74
- lanes: `再現に時間がかかる資産(条件11)`(c0〜c1)/ `陳腐化しうる資産(条件10)`(c2、self)/ `競合の動き`(c3)
  - 手本の lane12 などの通路計算は、使わなければ消してよい
- nodes(12):
  - c0 r0 `charter`(ok)`銀行免許` sub `2022 年に銀行を買収\n審査に約 1 年`
  - c0 r1 `mem`(ok)`会員 1,580 万人` sub `1 会員 1.54 製品`
  - c0 r2 `dep`(ok)`預金 455 億ドル` sub `給与振込が約 9 割`
  - c1 r0 `brand`(ok)`ブランド` sub `想起 10.4%\n(販促が必要)`
  - c1 r1 `data`(ok)`信用データ` sub `組成の実績\n(個人ローンの損失履歴)`
  - c1 r2 `lpbn`(unit)`LPB の買い手の網` sub `100 億ドル超の契約`
  - c2 r0 `tech`(risk)`技術基盤` sub `Galileo・Technisys\n(買収 約 23 億ドル)`
  - c2 r1 `app`(unit)`アプリ・製品` sub `機能は真似されやすい`
  - c2 r2 `gal`(risk)`Galileo の外販` sub `収益 −23%`
  - c3 r0 `chime`(risk)`Chime` sub `自社基盤 ChimeCore へ\n解約料 1,800 万ドル`
  - c3 r1 `rh`(risk)`Robinhood` sub `銀行業務 入金 30 億ドル超\nGold 480 万人`
  - c3 r2 `lc` `LendingClub` sub `預金 102 億ドル\n借り手が新規口座の 15% 超`
- edges:
  - chime → gal `内製化で離脱` risk n1、tech → gal ctrl
  - rh → app `同じ機能` risk n2、rh → mem `給与振込を取りに来る` risk
  - lc → dep `貸し手 + 預金の型` risk n3
  - charter → dep ctrl n4、mem → brand ctrl n5
  - 線が混む場合は rh → mem と mem → brand を消してよい
- 下に `L.text(s, '資産ごとの持ちの長さ', …)` と `L.timeBand`(手本と同じ x 0.5, y 5.5, w 8.55, h 1.1。from 2026, to 2036, step 2, name `s26tb`, fmt は年の数字):
  - `銀行免許` 2026〜2036 dark `10 年超`
  - `会員と預金` 2026〜2034 primary `7〜10 年`
  - `ブランド` 2026〜2030 light `販促が続く限り`
  - `技術基盤` 2026〜2030 amber `3〜5 年で更新が要る`
- mechPanel(bottom 6.66):
  1. `Chime は自社基盤へ移り、解約料 1,800 万ドルを払って Galileo を離れた。技術基盤の外販は内製化で陳腐化しうる`
  2. `Robinhood は銀行業務(入金 30 億ドル超、給与振込の設定 約 4 割)を始め、アプリの機能は真似されやすい`
  3. `LendingClub は貸し手と預金を組み合わせた同じ型(預金 102 億ドル)。型そのものは独占ではない`
  4. `銀行免許は買収と審査に約 1 年(2021-03 契約 → 2022-02 完了)。給与振込の預金 455 億ドルは短期に再現できない`
  5. `会員 1,580 万人とブランドは、販促を続ける限り積み上がる`
  - reason `免許・会員・預金は再現に数年かかる(11 B)。\n技術基盤の外販は内製化で陳腐化しうる(10 B)`
  - up `Galileo の外販が増収に戻り、\n会員当たりの製品が 1.7 を超えれば A`
  - down `他のフィンテックの銀行免許取得が続き、\n資金の差が 1.2pt を割れば C`

---------------------------------------------------------------------
## s28 条件12 収益の性格(評価 B。Sonnet。関係図。配置は手本 ORCL s19 の 3 列 + 外部 1 列を流用)
- contentSlide: kicker `左から: 収益の源 → SoFi の収益の種類 → ストックとフロー → 続く条件。①〜④ は右と対応。金額は Q2 2026(百万ドル)`、source `会社開示(Q2 2026 決算、損益計算書)、deck/assets/data/f19_sankey_nodes.csv、research_r2/R5_credit_fv.md(期前返済率)`、grade `B`、condNo `12`
- flowMap: name `s28`、h 5.0、cols [1.35, 1.45, 1.4, 1.3]、rows 4、nodeH 0.8
- lanes: `収益の源`(c0)/ `SoFi の収益`(c1〜c2、self)/ `続く条件`(c3)
- groups: `収益の種類`(c1、r0〜r3)、`性格`(c2、r0〜r3)
- nodes(13):
  - c0 r0 `loans` `B/S のローン` sub `個人 261・学生 161 億ドル`
  - c0 r1 `acct` `会員の口座` sub `預金 455 億ドル\nInvest 390 万口座`
  - c0 r2 `orig` `新しい組成` sub `107 億ドル/四半期`
  - c0 r3 `b2b` `Galileo の顧客` sub `口座 1.35 億`
  - c1 r0 `nii`(key)`純金利収益` sub `788.2(収益の 65%)`
  - c1 r1 `fee`(unit)`継続手数料` sub `86.7(7%)\nインターチェンジ・Plus`
  - c1 r2 `flow`(unit)`売却益・LPB` sub `売却益 150.4(12%)\nLPB 140.9(12%)`
  - c1 r3 `tp`(unit)`Tech Platform` sub `52.5(4%)`
  - c2 r0.5(rs 1 で 2 行分にできれば)`stock`(self)`ストック型 約 76%` sub `残高・口座に課金`
  - c2 r2 `flowk`(risk)`フロー型 約 24%` sub `組成のたびに発生`
  - c2 r3 `runoff`(risk)`残高の目減り` sub `期前返済 年 25.8%\n個人ローンは 2〜3 年`
  - c3 r1 `cond1`(ok)`会員と預金が増える` sub `会員 +35%`
  - c3 r2 `cond2`(risk)`組成を続ける` sub `組成が止まれば\n残高が減る`
- edges:
  - loans → nii `利息` money n1、acct → fee `会費・手数料` money n2、orig → flow `売る・渡す` goods n3、b2b → tp `処理料` money
  - nii → stock ctrl、fee → stock ctrl、tp → stock ctrl、flow → flowk ctrl
  - runoff → nii `目減り` risk n4、cond2 → orig(線が遠回りになるなら省略)
- mechPanel(bottom 6.66):
  1. `B/S のローン残高に利息が付く純金利収益が 788.2 百万ドルで収益の 65%`
  2. `会員の口座に付く継続手数料と Tech Platform を足すと、ストック型は約 76%`
  3. `売却益と LPB は組成のたびに生じるフロー型で、約 24%`
  4. `ただし個人ローンは期前返済が年 25.8% と速く、2〜3 年で返済される。残高を保つには組成を続ける必要がある`
  - reason `収益の約 4 分の 3 は残高に課金する\nストック型。ただし残高は 2〜3 年で\n入れ替わるため B`
  - up `Plus の有料会員が 100 万人を超え、\n継続手数料が収益の 15% を超えれば A`
  - down `組成の減速で B/S の残高が\n減り始めれば C`
- 期前返済 25.8% は research_r2/R5_credit_fv.md §3-1(2026-06-30 の CPR)

---------------------------------------------------------------------
## s29 条件13 アーキタイプ照合(評価 C。Haiku。手本 ORCL s29 を写経: flow + 表 + t15Side)
- contentSlide: kicker `条件13(総合)アーキタイプ照合: ORCL 型(継続課金・低い陳腐化)か MU 型(景気循環)・VRT 型・AVGO 型か`、source `会社開示(Q2 2026 決算)、research_r2/R5_credit_fv.md、calc/out/val.json`、grade `C`、condNo `13`(title・page は書かない)
- flow(手本と同じ 5 列):
  - `{ head: '原型', boxes: [{ text: 'ORCL 型', tone: 'key', h: 0.9 }] }`
  - `{ head: 'A', boxes: [{ text: '預金・FS 手数料', tone: 'on', h: 0.9 }] }`
  - `{ head: 'B', boxes: [{ text: 'LPB(資本を\n使わない手数料)', tone: 'on', h: 0.9 }] }`
  - `{ head: 'C', boxes: [{ text: '学生ローン(B/S)', tone: 'in', h: 0.9 }] }`
  - `{ head: 'D', boxes: [{ text: '個人ローン(B/S)', tone: 'off', h: 0.9 }] }`
- 表(手本と同じ位置・列幅): `['観点', 'ORCL 型の要素', 'MU 型の要素']`
  - `['課金', '預金の利ざや・継続手数料(収益の約 76%)', '売却益は組成と市況で変わる(約 24%)']`
  - `['信用の損失', 'LPB は損失を買い手が負う', '個人ローン組成の 71% を自社で保有\n(Q4 2025 は 51%)']`
  - `['資本', 'LPB と手数料は資本を使わない', '貸出の伸びが資本を食い、比率は半年で −4.1pt']`
  - `['技術', '会員の基盤は長く使える', 'Galileo は内製化で縮小(AVGO 型の商品化)']`
- t15Side: evidence [`個人ローン組成のうち自社で保有する比率 51% → 71%(Q4 2025 → Q2 2026。B/S 保有の組成 38 → 76 億ドル)`, `all-in 貸倒率 3.7%。景気後退で +0.75pt なら理論株価 −1.9 ドル`, `ROTCE が資本コストを超えるのは 2029〜30 年`]、reason `原型は ORCL 型に近いが、自社で抱える\n個人ローンの比率が上がり MU 型に寄るため C`、kpi `個人ローン組成の自社保有の比率 65% 未満で B 候補・75% 超で D 候補(毎四半期)`
