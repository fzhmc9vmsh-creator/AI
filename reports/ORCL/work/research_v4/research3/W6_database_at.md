# W6: Database@(マルチクラウド DB)と AI Database の成長の材料(絶対額・提携先発言・顧客・移行倍率・インストールベース・AI 指標・脅威)

- 作成日: 2026-10-12 / 対象: Oracle(NYSE: ORCL)再評価の論点「AI クラウド事業の将来の利益率と価値」のうち、データベース事業の成長材料
- 目的: 事実・数値・出典の整理と、出典間の食い違いの指摘のみ。**投資判断・推奨・評価は書かない。**
- 取得手段: WebSearch のみ。**24 回 / 上限 24 回(standard 20、extended 4)を使い切った。** WebFetch は使えない。**会社の原文(10-K、8-K、プレスリリース、説明会の逐語、FAM 資料 PDF)は 1 件も直接開いていない。数値はすべて検索ツールの要約に書かれた内容で、本書の全項目の Tier に `*` が付く。**
- Tier: 1=会社開示・決算説明会(提携先の公式文書を含む)、2=規制当局・格付会社・中央銀行・公的統計、3=報道・アナリスト・調査会社、4=ブログ・SNS・販促・助言会社の資料。`*` は「原本を読まず検索要約経由」。
- 「(算出)」は調査者の計算で、式を併記した。
- 出典 ID `[W6-nn]` は 10 節の一覧に対応する。1 回の要約が複数サイトを統合しているため、個別の数値がどの URL 由来かを特定できないものがある。
- 既存調査(特に `/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research2/R4_database_at.md`)で確認済みの内容は再掲に留め、R4 の欠損を埋める検索に使った。R4 の出典は `[R4-nn]` と表記する。

---

## 0. 要約(事実のみ、10 行)

1. **移行で顧客 1 社あたりの売上が何倍になるか**: 会社の発言として「3 倍」(Q2 FY24 = 2023-12、Ellison とされる)と「サポート売上に対し年間売上が 3〜5 倍」(Q2 FY26 = 2025-12、経営陣)を伝える要約が extended 検索 1 回に出たが、後続の 3 回(standard 2、extended 1)で再現できず、**逐語は未確認・単一系統**(T3\*)。
2. **FY26 10-K**: 過去 3 会計年度に、年間ソフトウェア・サポート契約を持つ顧客のクラウド移行で、年換算クラウド売上が **+$5.4B** 増えた。FY25 10-K と SEC 往復書簡(2025)は **+$4.3B**。差は +$1.1B、+25.6%(算出: 5.4−4.3、5.4÷4.3−1)。置き換わったサポート売上は非開示(T1\*)。
3. **マルチクラウド DB 売上**: Q4 FY25(2025-05 期)に **前期比 +115%**(5 本の要約で一致。R4 の欠損 12 を埋めた)→ 前年比 +1,529%(Q1 FY26)→ +353%(Q1 FY27)。**絶対額・年換算額は今回も欠損**。経営陣は FY26 に「3 桁成長が続く」と説明(T3\*)。
4. **拠点**: Q4 FY25 に稼働 23 + 今後 12 か月で 47 を追加(= 70、算出)。Q1 FY27 に 70 リージョン・119 AZ。**AWS は 2026-08-13 時点で 22 リージョン**(Oracle・Amazon の同日発表)。Azure は Oracle の年末レビューで「14 → 34」(別の Oracle ブログは 33)(T1\*)。
5. **提携先の発言**: Microsoft の Nadella は 2023-09 の発表時に「顧客がこの選択肢を求めた」「クラウド移行を根本的に加速する」と述べ、2023-10 の決算でも Azure 再加速の 3 要因の最初に Oracle を挙げたと報じられた(T3\*)。AWS は 2026-08-13 に Oracle との**長期の戦略的協業契約を拡大**(財務条件は非開示)。**Google 経営陣、AWS の Jassy・Garman の「需要・顧客数」の発言は欠損。**
6. **顧客事例**: MSCI(Azure、2025-10)、84.51°(Azure、Q1 FY27)、CJ Olive Young・Kobalt Music Group・バルセロナ都市交通局(AWS、2026-08)。**顧客数の絶対数は欠損**(Q1 FY27 は前年比 +180% の伸びのみ)。
7. **AI**: Q1 FY27 説明会の要約で「本番稼働の AI エージェント 2,300 超(前期比 +90%)、実行回数 350 万回超(前期比でほぼ倍増)」(複数の説明会本文サイトで一致、T3\*)。ベクトル検索など AI 機能は 26ai に追加費用なし。**FY30 の DB $20B の内訳は欠損。**
8. **インストールベース**: DB 顧客数は欠損。古い値は「Oracle ソフトウェア全体で 430,000 顧客」(2018 年の報道、DB 限定でない)、「Exadata 1,000 台目」(2011)。クラウド移行率(%)は分母が非開示で欠損。
9. **シェア**: Gartner の 2024 年 DBMS 市場は **$119.7B(+13.4%)**。上位 5 社は AWS、Microsoft、Oracle、Google、IBM の順(2022 年から不変)。2011 年の首位群(Oracle、IBM、Microsoft、SAP)で市場シェアを伸ばしたのは Microsoft のみ(Gartner の Ronthal)。**Oracle の 2025 年 DBMS 売上・シェア % は欠損。**
10. **脅威**: PostgreSQL への移行を示す独立した定量調査(Gartner 以外の移行件数や率)は見つからず、助言会社・ベンダーの主張のみ(「TCO 70〜90% 減」、「PL/SQL の自動変換は 50〜70%」、T4)。Aurora・Azure SQL の価格比較の一次データは欠損。

---

## 1. 移行時の顧客 1 社あたり売上の倍率(年代を問わず)

### 1-A. 倍率に関する発言と開示(年代順)

| 時点 | 話者・文書 | 内容 | 性質 | 出典・Tier |
|---|---|---|---|---|
| 2020-09 | Catz(FY21 Q1 の報道) | Exadata の需要を「顧客から Oracle へのコミットメント」と説明。クラウド価格や売上倍率の言及は確認できず | 倍率なし | [W6-19] T3\* |
| 2023-12-12(Q2 FY24 説明会) | Catz、Ellison(説明会本文の抜粋) | 「オンプレ DB がクラウドへ移行するにつれ、クラウド DB サービスは戦略的 SaaS と Gen2 OCI に並ぶ**第 3 の成長の柱**になる」。同期: Exadata クラウド・サービス +40%、Autonomous DB +26%、Gen2 インフラ(レガシー・ホスティング除く)+55%・年換算 $6B、RPO $65B 超 | 倍率なし(定性) | [W6-09] T1\*(説明会本文の抜粋を要約経由で確認) |
| 2023-12(Q2 FY24 説明会) | Ellison(とされる) | 「オンプレの DB ワークロードを OCI に移すと売上が **3 倍**になる」という趣旨(要約は「将来の見込み」と表記)。**別の検索(Q2 FY24 の本文抜粋)では確認できず** | **未確認** | [W6-09] T3\*(extended 検索 1 件のみ) |
| 2025-12-10(Q2 FY26 説明会) | 経営陣(話者の特定なし) | 「顧客をクラウドに移すだけで、サポート売上に比べ年間売上が **3〜5 倍**になる」という趣旨。**同じ検索語の再検索(standard 1、extended 1)で再現できず** | **未確認** | [W6-10] T3\*(extended 検索 1 件のみ) |
| 2024-02 | Ellison(The Register の報道) | ライセンスをオンプレでもクラウドでも使え、クラウドで大きな割引が得られると説明(値上げの主張とは逆向き) | 定性 | [W6-19] T3\* |
| 2024-02 | The Register の記事(専門家の見方) | Oracle のライセンス換算は「マルチスレッド有効なら 2 vCPU = Processor ライセンス 1」。ライセンスを Azure に移すと 2 倍払う場合があるとの見方。**対象が Database@Azure か、Azure の VM へのライセンス持ち込みかは要約から不明** | 反証側(コスト増の見方) | [W6-19] T3\* |
| 日付不明 | Oracle の移行ページ(Support Rewards) | OCI に **$1 使うごとにオンプレの技術サポート料が $0.25 減り**、「ゼロまで下がり得る」。R4 の [R4-23](TechTarget)と整合 | 制度 | [W6-11] T1\*、[R4-23] T3 |

- Ellison、Catz、Hurd、Magouyrk の過去の発言を年代を問わず探したが、**倍率を数値で述べた発言で逐語まで確認できたものは 0 件**。Hurd の発言は今回の検索結果に出なかった(欠損)。

### 1-B. 10-K が開示する「移行による年換算クラウド売上の増加」

| 開示 | 対象期間 | 値 | 文言(要約) | 出典・Tier |
|---|---|---|---|---|
| FY2025 10-K、SEC 往復書簡(2025) | FY23〜FY25 の 3 会計年度 | **+$4.3B** | 年間ライセンス・サポート契約を持つ顧客のクラウド移行が、年換算クラウド**サービス**売上の増加に寄与 | [W6-11] T1\*(R4 の [R4-30] と同一) |
| FY2026 10-K(FY 末 2026-05-31) | FY24〜FY26 の 3 会計年度 | **+$5.4B** | 年間**ソフトウェア**・サポート契約を持つ顧客のクラウド移行が、年換算クラウド売上の増加に寄与 | [W6-11] T1\* |
| 差(算出) | — | +$1.1B、+25.6% | 5.4−4.3 = 1.1、5.4÷4.3−1 = 0.256。期間の窓が 1 年ずれ、文言(license/software、cloud services/cloud)も異なる | — |

- どちらの開示も、**置き換わったサポート売上を示さない**ため、10-K の数字だけから倍率は出せない(検索要約で「どちらも倍率を支持しない」と明記された)。

### 1-C. 参考の算術(算出・条件付き。倍率が未確認のため仮定を置く)

| 項目 | 式・前提 | 値 |
|---|---|---|
| 移行元サポート売上の目安(倍率 3 倍と仮定) | 5.4 ÷ 3 | $1.8B |
| 移行元サポート売上の目安(倍率 5 倍と仮定) | 5.4 ÷ 5 | $1.08B |
| 注意 | $5.4B は DB 以外のソフトウェア(アプリ等)の移行を含み、「3〜5 倍」の対象が DB か全製品か不明。倍率が「総額」か「純増」かも不明 | — |
| Support Rewards を考慮した顧客の Oracle への支払い合計(サポート料 S、OCI 支出 = m×S、サポートは全てオンプレ継続、控除 = 0.25×OCI 支出、控除はサポート料まで) | 合計 = m×S + max(0, S − 0.25×m×S) | m=3 → 3.25S(3+0.25)、m=4 → 4.00S(4+0)、m=5 → 5.00S(5+0)。**控除に上限があるか、2026 年の現行条件かは未確認** |

---

## 2. マルチクラウド DB と周辺指標の時系列

### 2-A. マルチクラウド DB 売上の成長(R4 の表に Q4 FY25 を追加)

| 四半期(期末) | 成長率 | 倍率(算出: 1+成長率) | 備考 | 出典・Tier |
|---|---|---|---|---|
| Q4 FY25(2025-05-31) | **前期比 +115%**(Q3→Q4) | 2.15 倍 | Amazon・Google・Azure 向け DB 売上。稼働 23 データセンター、今後 12 か月で 47 を追加(合計 70、算出: 23+47)。経営陣は「マルチクラウド売上は 3 桁成長が続く」、OCI 成長は FY26 に 70% 超へ加速と説明 | [W6-07] T3\*(Constellation、Futurum、Barchart、Nasdaq、Zacks の要約で一致) |
| Q1 FY26(2025-08-31) | 前年比 +1,529% | 16.29 倍 | R4 の再掲。Oracle は「ドル建ての run-rate は出さなかった」と要約。FAM 資料では同じ数字が「Consumption(消費量)」の表記 | [R4-01] T1\*、[W6-08] T3\*、[W6-16] T3\* |
| Q2 FY26(2025-11-30) | 前年比 +817% | 9.17 倍 | R4 の再掲。**本回の要約は「consumption(消費量)+817%」と表記** | [R4-02]、[W6-10] T3\* |
| Q3 FY26(2026-02-28) | 前年比 +531% | 6.31 倍 | R4 の再掲 | [R4-03] |
| Q4 FY26(2026-05-31) | 前年比 +404% | 5.04 倍 | R4 の再掲(名称は「Multicloud AI Database」) | [R4-05] |
| Q1 FY27(2026-08-31) | 前年比 +353%、顧客数 前年比 +180% | 4.53 倍 | 複数の説明会本文サイト(stockanalysis、alphaspread、gurufocus、roic.ai、Fool、Benzinga、equibles、alphastreet、BigGo)の一覧に出た。「Oracle AI Database を主要クラウドのすべてに置く」「顧客はオンプレの Oracle DB を簡単にクラウドへ移したい」(Sicilia とされる) | [W6-12] T3\*、[R4-06] |

### 2-B. クラウド DB 関連の他の指標

| 時点 | 指標 | 値 | 出典・Tier |
|---|---|---|---|
| Q2 FY24(2023-11-30) | Exadata クラウド・サービス / Autonomous DB | +40% / +26% | [W6-09] T1\* |
| Q1 FY26(2025-08-31) | クラウド・データベース・サービス | +32%、年換算 約 $2.8B(既存 S4 と一致) | [W6-08] T3\* |
| Q2 FY26(2025-11-30) | クラウド・データベース・サービス / Autonomous DB | +30% / +43% | [W6-10] T3\*(出所サイトは要約から特定できず) |
| Q3 FY26(2026-02-28) | Oracle Cloud Database(IaaS) | +35%(R4) | [R4-03] |
| Q1 FY27(2026-08-31) | Oracle Cloud Database(IaaS)、Autonomous | 欠損 | 試した検索語は 9 節 |

### 2-C. 拠点数(会社別・時点つき)

| 時点 | 内容 | 出典・Tier |
|---|---|---|
| 2025-05(Q4 FY25) | 稼働 23 + 今後 12 か月で 47 = 70(算出) | [W6-07] T3\* |
| 2025 年(年末レビュー) | Database@Azure の対象を **14 → 34 リージョン**に拡大(別の Oracle ブログは **33**)。Base Database、OCI GoldenGate を追加 | [W6-14] T1\* |
| 2026 年前半(Google) | Osaka、Delhi、London、Milan を追加(2026 年前半)。2026-05 末に Melbourne と Milan のゾーンを Exadata・Base Database・GoldenGate に追加 | [W6-04] T1\* |
| 2026-03(Q3 FY26 の CEO ブログ。R4) | Azure 33、Google 14、AWS 8(目標 22) | [R4-04] |
| 2026-08-13 | **AWS は 22 リージョン**(アジア太平洋、欧州、米州) | [W6-03] T1\* |
| 2026-09-10(Q1 FY27) | 計 70 リージョン・119 AZ | [W6-12] T3\* |
| 合計の突き合わせ(算出) | Azure 34 + Google 14 + AWS 22 = **70**。Azure 33 + Google 15 + AWS 22 = **70**。Azure 33 + Google 14 + AWS 22 = **69**。どの組み合わせが正しいかは未確認 | — |

---

## 3. 提携先(Microsoft・AWS・Google)の発言とマーケットプレイスでの扱い

| 提携先 | 時点 | 話者・文書 | 内容 | 出典・Tier |
|---|---|---|---|---|
| Microsoft | 2023-09-14(発表) | Nadella(発表時の声明) | 「顧客から、既存の取り組みに加えてこの選択肢が欲しいと言われた」「クラウドへの移行を根本的に加速する」。Azure は OCI 以外で Oracle の DB サービスを動かす唯一のクラウドになった(発表当時、Nadella の声明の要約) | [W6-01] T3\*(TechCrunch、Yahoo、MS Dynamics World) |
| Microsoft | 2023-10(FY24 Q1 決算) | Nadella(決算説明会とされる) | Azure 再加速の **3 つの理由の最初に Oracle との提携**を挙げた。同期 Microsoft Cloud 売上は +24%、$31.8B と要約。論評は「Oracle DB へのマルチクラウド接続のため顧客が Azure 支出を増やした」と解釈。**発表時の声明と決算説明会の発言が要約内で混在しており、どの場の発言かは未確認** | [W6-01] T3\*(Acceleration Economy、Futurum) |
| Microsoft | 2023-12 〜 | Oracle・Microsoft の告知 | 米国東部が 2023-12 に GA、欧州はフランクフルトが 2 番目。のち「6 リージョン、さらに 15 を計画」(日付不明) | [W6-14] T3\*(DBTA、Convergedigest) |
| Microsoft | 2025-10 | 共同の発表 | MSCI などがデータベース@Azure を採用。**顧客数の開示なし** | [W6-14] T3\*(Malaya) |
| Microsoft | 2026 年 | 決算説明会・Ignite | **欠損**(2026 年の発言を検索で確認できず) | 9 節 |
| AWS | 2024-09-09(発表) | Ellison、Garman(CloudWorld 共同登壇) | Ellison「マルチクラウドを使いたい顧客から巨大な需要を見ている」。Oracle 側の主張で独立した需要の測定ではない | [W6-02] T1\* |
| AWS | 2025-12(re:Invent) | Oracle ブログ | TDE の鍵管理で AWS KMS と統合、Exadata on AWS のセッションを多数。**Jassy・Garman の基調講演の発言は確認できず** | [W6-02] T1\* |
| AWS | 2026-08-13 | Oracle・Amazon の共同プレスリリース | Oracle と AWS が**拡大した長期の戦略的協業契約**に署名。22 リージョン。**Exadata Database Service on Exascale Infrastructure** が一般提供(従量課金)。分析・AI サービスとの統合。AWS の DB サービス担当 VP が「過去 1 年の採用拡大は、顧客が Oracle AI Database のワークロードを動かす価値の表れ」と述べた(氏名は要約に出ず)。**財務条件は非開示** | [W6-03] T1\* |
| AWS | 販売方法 | AWS Marketplace | R4 のとおり: AWS Marketplace の単一請求書、AWS のコミットメントと Oracle Support Rewards に算入(AWS 文書) | [R4-21] T1\* |
| Google | 2024-06(発表) | Oracle・Google | 初期は米国東部(Ashburn)、米国西部(Salt Lake City)、英国(London)、ドイツ(Frankfurt)の 4 リージョン。GA は 2024-09(R4) | [W6-04] T3\*、[R4-17] |
| Google | 2026 年 | Google 製品文書(リリースノート) | リージョン・ゾーンの追加のみ(上記 2-C)。**Google 経営陣(Kurian、Pichai)の「需要・顧客数」の発言は欠損** | [W6-04] T1\* |
| Google | 2026 年 | Oracle の Google Cloud Next 2026 資料 | Oracle 側の販促(Google の声明ではない) | [W6-04] T1\* |
| 参考 | 2018〜2019 | Kurian(Google Cloud 責任者)の経歴 | Oracle に 20 年以上在籍し製品開発の責任者。報道では、Oracle のソフトを AWS・Azure など他社クラウドで動かす案を主張し Ellison と衝突したとされる | [W6-21] T3\* |

---

## 4. 顧客事例・顧客数・消費量の伸び

| 時点 | 提携先 | 顧客・指標 | 内容 | 出典・Tier |
|---|---|---|---|---|
| 2025-10 | Azure | MSCI | Database@Azure を採用した組織の例として告知 | [W6-14] T3\* |
| 2026-09(Q1 FY27 の顧客事例ページ) | Azure | 84.51° | Oracle AI Database@Azure(Exadata Database Machine)を選び、大きなハードウェア更改なしに主要 DB ワークロードをオンプレの外へ移した。**売上額の記載なし** | [W6-15] T1\* |
| 2026-08-13 | AWS | CJ Olive Young、Kobalt Music Group、バルセロナ都市交通局 | 基幹業務のワークロードを Oracle AI Database@AWS で稼働 | [W6-03] T1\* |
| 日付不明 | (26ai の事例) | Outline Global(豪州) | AI Vector Search で「売上 +30%」と Oracle が記載。単一の事例で、導入数の指標ではない | [W6-17] T1\* |
| 四半期 | 全社 | マルチクラウド顧客数 | Q1 FY27 は前年比 **+180%**。**絶対数は欠損** | [W6-12] T3\* |
| 四半期 | 全社 | 消費量・売上 | 2-A の系列。**顧客 1 社あたり売上は欠損** | — |

---

## 5. インストールベースの規模とクラウド移行率

| 項目 | 値 | 性質・注意 | 出典・Tier |
|---|---|---|---|
| Oracle DB を使う大企業 | Fortune Global 100 の 97%(Oracle の説明) | R4 の再掲 | [R4-25] T1\* |
| Oracle ソフトウェアの顧客数 | **430,000**(2018 年の Next Platform の記事) | **DB 限定ではなく全ソフトウェア**。出典の filing は不明、8 年前の値 | [W6-18] T3\* |
| Exadata の導入台数(古い値) | 2011 年に **1,000 台目**(67 か国、23 業種) | 15 年前の値。現在の台数は欠損 | [W6-18] T3\* |
| Exadata の利用企業数(第三者の推計) | 2,464 社、別サイトで 5,893 社 | 営業データ会社が収集・推計した値で、Oracle の開示ではない。2 つの値が割れている | [W6-18] T4\* |
| DB の顧客総数・Exadata 台数(現在) | **欠損** | 会社の文言は「数千の Exadata サイト」(R4) | 9 節 |
| クラウド移行の実績(年換算クラウド売上) | FY23〜25 で +$4.3B、FY24〜26 で +$5.4B | 1-B のとおり | [W6-11] T1\* |
| クラウドへの移行率(%) | **欠損**(分母の既存サポート契約の規模が非開示) | 参考: FY25 の「ライセンス・サポート(全製品)」≈ $19.5B(R4 の算出: 44.0−24.5) | [R4-28] |
| 経営陣の見通し | 「顧客はオンプレの Oracle DB を簡単にクラウドへ移したい」(Q1 FY27、Sicilia とされる)。移行率の目標は未確認 | — | [W6-12] T3\* |

---

## 6. AI Database(26ai)・ベクトル検索・AI Data Platform の採用指標と売上目標

| 項目 | 値 | 性質・注意 | 出典・Tier |
|---|---|---|---|
| 本番稼働の AI エージェント数 | **2,300 超、前期比 +90%**(Q1 FY27) → 前期の水準 約 1,211(算出: 2,300÷1.9) | 複数の説明会本文サイトの要約で一致(R4 では単一系統だった)。**どの種類のエージェントか(DB 内か、アプリか)は未確認** | [W6-12] T3\* |
| AI エージェントの実行回数 | **350 万回超**、前期比でほぼ倍増(Q1 FY27) | 同上 | [W6-12] T3\* |
| 経営陣の方針 | 「Oracle AI Database を主要クラウドのすべてに置く」(Sicilia とされる) | 同上 | [W6-12] T3\* |
| AI Vector Search の提供開始時期 | 26ai に挙がる機能の大半は **23ai(2024-05)で提供済み**との分析(1 本) | 26ai は 23ai の長期サポート版後継(R4) | [W6-17] T3\* |
| 課金 | AI Vector Search など高度な AI 機能は**追加費用なし**、無料ティアあり | R4 の再掲 | [W6-17] T1\* |
| AI Database 単独の売上 | **欠損** | 課金が DB 利用量に組み込まれる形(R4 の解釈) | 9 節 |
| ベクトル検索の本番導入社数、26ai の採用社数 | **欠損** | 試した検索語は 9 節 | 9 節 |
| AI Data Platform | Q1 FY27 のプレスリリースに「新しい Oracle AI Data Platform と enterprise ontology generation」の節がある。**採用指標は要約の末尾が切れて取得できず** | — | [W6-13] T1\* |
| 市場規模の主張 | Futurum の記事の見出し: 「Oracle は AI Database 26ai を **$1.2 trillion** 市場で首位に位置づける」。本文は未読で、数字の定義は不明 | 見出しのみ | [W6-17] T3\* |
| FY30 の DB 売上目標 | **$20B**(AI Database と AI Data Platform)、年平均成長率 約 53%。根拠は「プライベート・データのベクトル化とマルチクラウド提携」(CreditSights) | R4 の再掲。**内訳(Autonomous、Exadata、Cloud@Customer、マルチクラウド、AI Data Platform)は欠損**。FAM 資料 PDF は URL が出たが、一部の抜粋しか返らず、全文は未読 | [W6-16] T3\* |
| FAM 資料の記載 | 「1,529% YoY MultiCloud Consumption Growth」の記載あり(文脈は不明) | R4 の食い違い 9 と同じ | [W6-16] T3\* |

---

## 7. 脅威: 競合 DB・移行・シェア

### 7-A. DBMS 市場とシェア(Gartner など)

| 時点 | 項目 | 値 | 出典・Tier |
|---|---|---|---|
| 2022 | DBMS 市場(Merv Adrian) | 「$90B 超」、前年比 +$11B 超。Oracle $17.5B、AWS は要約に「$23B 超」とある(表記が崩れており未確認) | [W6-06] T3\* |
| 2022 の Oracle 比率(算出) | 17.5 ÷ 90 | 19.4% 以下(分母が「90 超」のため上限) | — |
| 2023 | DBMS 市場(Adrian) | 「$100B の図」でハイパースケーラーが支配、Snowflake・MongoDB が好調 | [W6-06] T3\* |
| 2024 | DBMS 市場(Gartner) | **$119.7B、前年比 +13.4%**。成長の大半はクラウド・プラットフォーム | [W6-05] T3\* |
| 2023 の逆算(算出) | 119.7 ÷ 1.134 | $105.6B | — |
| 2025 | DBMS 市場(Gartner) | 総額は**欠損**。別の調査会社(Spherical Insights)は $130.90B(定義が異なる) | [W6-06] T3\* |
| 2022〜2025 | 上位 5 社の順位(Gartner、売上順) | AWS、Microsoft、**Oracle(3 位)**、Google Cloud、IBM。**2022 年から不変** | [W6-05] T3\* |
| 2011〜2025 | 市場シェアの変化(Gartner の Ronthal) | 2011 年の首位群(Oracle、IBM、Microsoft、SAP)で**シェアを伸ばしたのは Microsoft のみ**。ほかは Amazon、Google Cloud、Snowflake、Databricks、MongoDB などに譲った。「上位 17 社の順位の入れ替わりは過去 2 年なし」 | [W6-05] T3\*(The Register、Red Gate) |
| 計測の範囲 | PostgreSQL、MySQL、Cassandra などのオープンソースは**単独では計測されず**、商用サービスの一部としてのみ計上 | [W6-05] T3\* |
| Oracle の DBMS 売上・シェア % (2023〜2025) | **欠損**(Gartner のグラフは Ronthal の LinkedIn に掲載とされるが、値は取得できず) | 9 節 |

### 7-B. PostgreSQL などへの移行

| 項目 | 内容 | 性質 | 出典・Tier |
|---|---|---|---|
| 移行の動機(2026 年) | ライセンス費用の上昇、サポート方針の硬直、ベンダーロックインの回避 | ベンダー・助言会社・実務者の記述 | [W6-20] T4\* |
| 助言会社の TCO 主張 | Oracle Licensing Experts の白書(2026-06 更新): Oracle から PostgreSQL への移行で **DB の TCO が 70〜90% 低下**したとの報告。PL/SQL は **50〜70% しか自動変換できず**、手作業の書き換えが実コスト | **買い手側助言会社(移行案件に商業上の利害)**、独立調査ではない | [W6-20] T4\* |
| Hexaware(Microsoft Marketplace の掲載) | 「ライセンスと運用コストを 50〜70% 削減」 | 販促 | [W6-20] T4\* |
| 前提の例(Oracle Licensing Experts) | Oracle Enterprise Edition の定価は **x86 コア当たり 約 $23,750** + 年間サポート 22%。Aurora はライセンス料ゼロ。年 $800K を払う想定の事業所が、移行費 $900K + Aurora 年 $250K で回収 約 1.6 年(**仮想の例**) | 助言会社の例示で実測ではない | [W6-20] T4\* |
| 別の例 | Oracle EE を 16 vCPU の EC2 で動かすと年 約 $72,240、Aurora PostgreSQL で年 約 $20,322 | 古い第三者の分析をパートナーのブログが引用。インスタンス種別が古く、未検証 | [W6-20] T4\* |
| DB-Engines | 古い記事は「Oracle から PostgreSQL への移行の流れが明確」とし、**PostgreSQL が 2025 年頃に Oracle を抜く**と外挿 | 外挿であり、実績ではない。**現在の DB-Engines のスコアは取得できず** | [W6-20] T4\* |
| 独立した移行件数・率の調査 | **欠損**(2026 年の企業調査、Aurora 固有のデータは見つからず) | — | 9 節 |
| Oracle 側のコスト反論 | 同じ助言会社は、Exadata Cloud@Customer の 5 年 TCO が自社保有のオンプレ Exadata より**中央値で 34% 高い**、OCI Dedicated Region は **41% 高い**とモデル化 | 助言会社の推計(T4)。マルチクラウド DB ではなくクラウド@顧客と専用リージョンの話 | [W6-19] T4\* |

### 7-C. AWS Aurora・Azure SQL

| 項目 | 内容 | 出典・Tier |
|---|---|---|
| Aurora の価格 | ライセンス料ゼロ(助言会社の記述)。**AWS 公式の価格表・Oracle との比較は取得できず** | [W6-20] T4\* |
| Azure SQL Managed Instance の価格・機能 | **欠損** | 9 節 |
| AWS が公表する Oracle からの移行件数(DMS、SCT) | **欠損**。移行ツールは AWS Schema Conversion Tool と Database Migration Service(助言会社の記述) | [W6-20] T4\* |
| 提携と自社 DB の併存(一般知識。本回の検索では Azure SQL の価格・機能を確認できていない) | AWS は Database@AWS(Oracle)と Aurora(自社)の両方を提供し、Microsoft も Database@Azure と自社の SQL 製品を持つ。事実の併記のみで、競合か補完かの評価は書かない | [W6-02][W6-20] |
| Amazon・Google の自社 DB の位置 | Gartner の順位で AWS が 1 位、Google が 4 位(7-A) | [W6-05] T3\* |

---

## 8. 出典間の食い違い(事実の指摘のみ)

| # | 項目 | 食い違い | 所見 |
|---|---|---|---|
| 1 | 移行の倍率「3 倍」「3〜5 倍」 | extended 検索 1 回の要約は両方を会社の発言として記載。後続の検索(Q2 FY24 の本文、Q2 FY26 の本文、倍率の言い回しの再検索)では抜粋が途中で切れる、または該当語が出ず、**再現不能** | 逐語を確認するまで採用不可。原本候補: Fool の Q2 FY24 と Q2 FY26 の逐語 URL(10 節 W6-09、W6-10) |
| 2 | 「3 倍」の性質 | 要約は「将来の見込み」と書く。「3〜5 倍」は「サポート売上に対する年間売上の倍率」と書く | 前者は期待値、後者は実績か見込みか不明 |
| 3 | 10-K の移行寄与 | FY25 は $4.3B(license support、cloud services)、FY26 は $5.4B(software support、cloud revenue) | 期間の窓が 1 年ずれ、用語も異なる。同一定義かは未確認 |
| 4 | Azure のリージョン数 | Oracle の 2025 年末レビューは 34、同日の Oracle の別ブログは 33(R4 の CEO ブログも 33)。Microsoft 側(2026-01)は 31 または「30 超」 | 時点差の可能性。2-C の突き合わせ参照 |
| 5 | 合計 70 | 34+14+22 = 70、33+15+22 = 70、33+14+22 = 69 | 内訳が未確認 |
| 6 | 1,529%・817% の定義 | Oracle のプレスリリースは「revenue」、FAM 資料と本回の Q2 FY26 の要約は「consumption」 | R4 の食い違い 9 と同じ。売上と消費量が同じか不明 |
| 7 | Nadella の発言の場 | 要約は 2023-09 の発表時の声明と 2023-10 の決算説明会を混在 | どの引用がどの場かは未確認 |
| 8 | Exadata の規模 | Oracle「数千のサイト」(R4)/ 営業データ会社 2,464 社と 5,893 社 / 2011 年 1,000 台目 | 定義が異なり比較不能 |
| 9 | DBMS 市場の総額 | Gartner 2024: $119.7B / Adrian 2023: 「$100B の図」/ Spherical Insights 2025: $130.90B | 調査会社ごとに定義が異なる。同じ系列として並べない |
| 10 | Adrian の AWS 売上 | 要約は「$23B 超」と書くが表記が崩れている | 未確認 |
| 11 | Ellison の移行の説明 | Ellison は「クラウドで大きな割引」と説明(The Register)/ 同記事の専門家は「ライセンス換算で 2 倍払う場合がある」/ 経営陣の「3〜5 倍」(未確認) | 対象(BYOL の VM か、Database@ か)が異なる可能性 |
| 12 | 2,300 エージェント | R4 は「単一系統・裏取り不成立」。本回の検索 16 では複数の説明会本文サイトで一致 | R4 の評価を更新。ただし内容(エージェントの種類)は未確認 |
| 13 | Q2 FY26 の Cloud Wars 記事 | 要約は「記事は Catz 時代の古い Q2 を扱っている」と書くが、URL の見出しは Microsoft・Google・AWS との契約を指す | 年度が特定できないため、Q2 FY26 の数値の出所としては使わない |

---

## 9. 欠損と試した検索語

| # | 欠損 | 試した検索語・結果 |
|---|---|---|
| 1 | マルチクラウド DB の売上の絶対額・年換算額(2026 年のアナリスト推計) | "Oracle multicloud database revenue estimate annualized run-rate analyst 2026 Database@Azure billion"(standard)。run-rate の記載なし。Q1 FY26 の「クラウド DB サービス 年換算 約 $2.8B」のみ |
| 2 | FY30 $20B の内訳 | "Oracle financial analyst meeting October 2025 database $20 billion fiscal 2030 breakdown multicloud Autonomous Exadata Cloud@Customer AI Data Platform slides"(standard)。CreditSights の 53% CAGR のみ。FAM 資料 PDF は全文を取得できず |
| 3 | Microsoft の 2024〜2026 年の発言(需要・顧客数) | "Nadella Oracle Database@Azure customers demand Microsoft earnings call Oracle database Azure"(standard)、"Oracle Database@Azure 2026 Microsoft announcement customers adoption Ignite expansion Fabric integration number of customers"(standard)。2023 年の発言と 2025 年の事例のみ |
| 4 | AWS の Jassy・Garman による需要・顧客数の発言 | "Oracle Database@AWS Garman OR Jassy customers demand Oracle Exadata AWS re:Invent keynote"(standard)。2024-09 の Ellison の発言と 2026-08 の AWS VP の声明のみ |
| 5 | Google の Kurian・Pichai による需要・顧客数の発言 | "Thomas Kurian Oracle Database@Google Cloud customers demand Oracle Database Google Cloud Next"(standard)、"Google Cloud Oracle Database@Google Cloud customers Kurian OR Pichai OR "Google Cloud" executive says demand Oracle partnership 2026 multicloud"(standard)、"Oracle Database@Google Cloud customers 2026 Google Cloud Next ..."(standard)。リリースノートのリージョン追加のみ |
| 6 | 移行倍率の逐語(Ellison・Catz・Hurd・Magouyrk) | "Ellison Oracle customers moving to cloud pay more revenue multiple "times" Exadata Cloud ..."(standard)、"Oracle customer migrates on-premises Oracle Database to Autonomous OR Exadata cloud ... "times" more per customer ..."(extended)、"Oracle Q2 2026 earnings call transcript moving customer to cloud "three to five" ..."(standard)、"Oracle Q2 fiscal 2024 earnings call Ellison Database@Azure ... 3x uplift customers"(standard)、"Oracle executives say customer moving on-premises database to Oracle cloud generates "three to five times" ..."(extended)。extended の 1 回目の要約にだけ出て、他は再現できず。Hurd の発言は出ず |
| 7 | マルチクラウド顧客の絶対数、Database@ 顧客の名前の一覧 | "Oracle Q1FY27 earnings customer highlights Oracle AI Database@Azure Database@Google Cloud Database@AWS customers selected migrate"(standard)。84.51° など個別のみ |
| 8 | DB 顧客総数、Exadata の現在の台数、クラウド移行率 | "Oracle number of customers installed base database "customers" 430,000 OR "organizations" ... 10-K"(standard)。2018 年と 2011 年の古い値のみ |
| 9 | ベクトル検索の本番導入社数、26ai の採用社数、AI Database 単独の売上、AI Data Platform の採用指標 | "Oracle AI Database 26ai adoption AI Vector Search production customers number agents Q4 fiscal 2026 earnings call database"(extended)、"Oracle AI Data Platform adoption customers vector search AI Database revenue Q1 fiscal 2027 earnings call Magouyrk Ellison"(standard)。単一事例(Outline Global)のみ |
| 10 | Oracle の DBMS 売上・シェア % (Gartner 2023〜2025) | "Gartner DBMS market share 2025 Oracle Microsoft AWS Google revenue share ..."(standard)、"Register Gartner DBMS chart 2026 Oracle market share percent revenue 2025 PostgreSQL Ronthal"(standard)、"Merv Adrian DBMS market 2025 Oracle revenue billion share Gartner ..."(standard)。順位と 2024 年の総額のみ |
| 11 | PostgreSQL 移行の独立した件数・率、DB-Engines の現在のスコア | "Oracle to PostgreSQL migration trend enterprises 2026 Aurora PostgreSQL replace Oracle savings survey DB-Engines ranking Oracle PostgreSQL"(standard)。ベンダー・助言会社の記述のみ |
| 12 | Aurora・Azure SQL の公式価格、AWS の移行件数 | "Aurora PostgreSQL vs Oracle Database pricing cost comparison AWS claims customers migrated off Oracle number of databases migrated AWS DMS Azure SQL Managed Instance price"(standard)。助言会社の例のみ |
| 13 | Oracle とハイパースケーラーの取り分、Google Cloud Marketplace の扱い | 今回は検索せず(R4 で試行済み。Google は未確認のまま) |
| 14 | Q1 FY27 の Cloud Database(IaaS)・Autonomous の成長率 | 今回の検索 16、11 でも要約に出ず |
| 15 | 全ての原本(10-K、プレスリリース、説明会の逐語、FAM 資料) | 検索要約経由のみ |

---

## 10. 出典一覧

| ID | 内容 | URL | 日付 | Tier |
|---|---|---|---|---|
| W6-01 | Nadella の Oracle Database@Azure に関する発言(発表時、FY24 Q1 決算) | https://techcrunch.com/2023/09/14/oracle-brings-its-database-infrastructure-to-microsoft-azure 、https://finance.yahoo.com/news/oracle-brings-database-infrastructure-microsoft-205619966.html 、https://accelerationeconomy.com/?p=59776 、https://accelerationeconomy.com/?p=59759 、https://futurumgroup.com/insights/we-are-live-talking-microsoft-oracle-arm-apple-salesforce-and-adobe/ 、https://msdynamicsworld.com/node/33873 | 2023-09-14、2023-10 | T3\* |
| W6-02 | Oracle・AWS の戦略提携の発表、CloudWorld 共同登壇、re:Invent 2025 | https://press.aboutamazon.com/aws/2024/9/oracle-and-amazon-web-services-announce-strategic-partnership 、https://www.oracle.com/news/announcement/ocw24-oracle-and-amazon-web-services-announce-strategic-partnership-2024-09-09/ 、https://thestack.technology/the-larry-and-matt-show-oracle-aws-team-up-set-to-share-stage 、https://blogs.oracle.com/cloud-infrastructure/aws-reinvent-2025-accelerating-multicloud-innovation | 2024-09-09、2025-12 | T1\* |
| W6-03 | Oracle・AWS の拡大した協業契約(22 リージョン、Exascale、顧客名) | https://press.aboutamazon.com/aws/2026/8/oracle-and-aws-deepen-strategic-collaboration-as-enterprise-adoption-of-oracle-ai-database-aws-accelerates 、https://www.oracle.com/jp/news/announcement/oracle-and-aws-deepen-strategic-collaboration-as-enterprise-adoption-of-oracle-ai-database-at-aws-accelerates-2026-08-13/ 、https://www.oracle.com/africa/news/announcement/oracle-ai-database-at-aws-helps-organizations-across-the-word-bring-ai-to-mission-critical-data-2026-08-13/ 、https://www.channelinsider.com/ai/oracle-ai-database-aws-cloud-migration-expansion/ 、https://www.vermoegenszentrum.ch/en/stock-exchange-and-markets/news/oracle-and-aws-expand-their-collaboration-oracle-ai-databaseaws | 2026-08-13 | T1\*、T3\* |
| W6-04 | Oracle Database@Google Cloud のリリースノート、初期計画 | https://docs.cloud.google.com/oracle/database/docs/release-notes 、https://www.datacenterdynamics.com/en/news/oracle-to-colocate-database-services-and-network-interconnect-in-google-data-centers/ 、https://convergedigest.com/?p=96279 | 2024-06、2026 年 | T1\*、T3\* |
| W6-05 | Gartner の DBMS 市場(2011〜2025 の順位、2024 年 $119.7B) | https://www.theregister.com/2026/04/21/gartner_bamboozling_dbms_chart_shows/ 、https://www.red-gate.com/simple-talk/featured/what-are-the-top-database-platforms-in-2026-a-look-at-the-latest-data/ 、https://www.gartner.com/en/documents/6494271 | 2026-04-21 | T3\* |
| W6-06 | Merv Adrian の DBMS 売上分析、Spherical Insights | https://itmarketstrategy.com/2023/05/07/dbms-2022-revenue-up-14/ 、https://itmarketstrategy.com/category/microsoft/ 、https://www.sphericalinsights.com/blogs/top-15-companies-in-global-database-management-system-dbms-market-statistics-report-till-2035 | 2023-05 〜 | T3\* |
| W6-07 | Q4 FY25 のマルチクラウド DB 前期比 +115%、拠点 23 + 47 | https://www.constellationr.com/insights/news/oracle-clouds-annual-revenue-run-rate-exiting-q4-nears-27-billion 、https://futurumgroup.com/insights/oracle-delivers-q4-fy-2025-results-with-27-cloud-growth-rpo-hits-138-billion 、https://www.barchart.com/story/news/32837570/oracle-s-cloud-revenue-jumps-27-in-its-fiscal-2025-q4 、https://www.nasdaq.com/articles/oracles-cloud-revenue-jumps-27-its-fiscal-2025-q4 、https://www.zacks.com/stock/news/2764835/oracles-multi-cloud-push-intensifies-a-key-driver-of-cloud-demand 、https://www.barchart.com/story/news/34458238/oracle-cloud-expansion-in-focus-a-key-to-future-momentum | 2025-06 | T3\* |
| W6-08 | Q1 FY26 説明会の要約(クラウド DB サービス +32%、年換算 約 $2.8B) | https://www.marketbeat.com/earnings/reports/2025-9-9-oracle-co-stock 、https://allmind.ai/earnings/event/bt_ORCL_2026_Q1 | 2025-09-09 | T3\* |
| W6-09 | Q2 FY24 説明会の逐語・要約(第 3 の成長の柱、Exadata +40%、Autonomous +26%) | https://www.fool.com/earnings/call-transcripts/2023/12/12/oracle-orcl-q2-2024-earnings-call-transcript/ 、https://www.barchart.com/story/news/22652851/oracle-orcl-q2-2024-earnings-call-transcript 、https://www.roic.ai/quote/ORCL/transcripts/2024-year/2-quarter 、https://www.theregister.com/2023/12/12/oracle_shares_hit_as_it/ | 2023-12-12 | T1\*、T3\* |
| W6-10 | Q2 FY26 説明会の逐語・要約(Autonomous +43%、クラウド DB サービス +30%、「3〜5 倍」の候補) | https://www.fool.com/earnings/call-transcripts/2025/12/10/oracle-orcl-q2-2026-earnings-call-transcript/ 、https://www.aol.com/finance/oracle-orcl-q2-2026-earnings-232232703.html 、https://allmind.ai/earnings/event/bt_ORCL_2026_Q2 、https://cloudwars.com/cloud/oracle-cloud-database-q2-revenue-surges-powered-by-breakthrough-deals-with-microsoft-google-cloud-aws | 2025-12-10 | T3\* |
| W6-11 | Oracle FY2026 10-K(+$5.4B)、SEC 往復書簡(+$4.3B)、Oracle の移行ページ(Support Rewards) | https://www.sec.gov/Archives/edgar/data/0001341439/000119312526277521/orcl-20260531.htm 、https://www.sec.gov/Archives/edgar/data/0001341439/000119312525233320/filename1.htm 、https://www.oracle.com/database/cloud-migration/ | FY26: 2026-05-31 期、2025 | T1\* |
| W6-12 | Q1 FY27 説明会の逐語・要約(+353%、顧客 +180%、70 リージョン、2,300 エージェント、350 万回) | https://stockanalysis.com/stocks/orcl/transcripts/689425-q1-2027/ 、https://www.alphaspread.com/security/nyse/orcl/investor-relations/earnings-call/q1-2027 、https://www.gurufocus.com/stock/ORCL/transcripts/9076583 、https://www.roic.ai/quote/ORAC.TO/transcripts/2027-year/1-quarter 、https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/ 、https://www.benzinga.com/news/26/09/61729962/oracle-reports-q1-2027-results-full-earnings-call-transcript 、https://equibles.com/stocks/orcl/calls/2027-q1 、https://news.alphastreet.com/oracle-corporation-orcl-q1-2027-earnings-call-transcript/ 、https://finance.biggo.com/quote/ORCL/earnings-call/US_ORCL_2026-09-10 | 2026-09-10 | T3\* |
| W6-13 | Q1 FY27 プレスリリース(AI Data Platform の節、RPO $664B)、要約 | https://www.oracle.com/sg/news/announcement/q1fy27-earnings-release-2026-09-10/ 、https://www.placera.se/pressmeddelanden/oracle-announces-q1-results-driven-by-triple-digit-growth-in-cloud-infrastructure-revenues-20260910 、https://www.businessinsider.jp/article/2609-earnings-oracle-corporation-q1-2027-earnings-call-summary/ 、https://quartr.com/events/oracle-corporation-orcl-q1-2027_3gvkOKJp | 2026-09-10 | T1\*、T3\* |
| W6-14 | Oracle Database@Azure の 2025 年ハイライト(14 → 34 リージョン)、MSCI の事例、DBTA | https://blogs.oracle.com/cloud-infrastructure/oracle-databaseazure-2025-highlights 、https://malaya.com.ph/info-tech/tech-industry-info-tech/global-organizations-adopt-oracle-to-accelerate-cloud-migrations 、https://www.dbta.com/Editorial/News-Flashes/Microsoft-and-Oracle-Expand-Partnership-to-Extend-Oracle-Database-at-Azure-Worldwide-163106.aspx 、https://convergedigest.com/?p=97687 | 2025-10、2025 年末 | T1\*、T3\* |
| W6-15 | Oracle Q1 FY27 の顧客事例ページ(84.51°) | https://www.oracle.com/asean/customers/earnings/ | 2026-09 | T1\* |
| W6-16 | CreditSights の FAM 要約($20B、53% CAGR)、FAM 資料 PDF(未読)、FAM 告知 | https://know.creditsights.com/insights/oracle-top-10-takeaways-from-2025-analyst-meeting/ 、https://www.oracle.com/a/ocom/docs/corporate/financial-analyst-meeting-2025-magouyrk.pdf 、https://investor.oracle.com/investor-news/news-details/2025/ORACLE-FINANCIAL-ANALYST-MEETING-TO-BE-HELD-OCTOBER-16-2025/default.aspx | 2025-10-16 | T3\*、T1\* |
| W6-17 | 26ai(Oracle のページ、Futurum「$1.2 trillion」の見出し、Outline Global の事例、jamsql、John Foley の Substack) | https://www.oracle.com/database/ai-vector-search/ 、https://www.oracle.com/news/announcement/ai-world-database-26ai-powers-the-ai-for-data-revolution-2025-10-14/ 、https://futurumgroup.com/insights/oracle-positions-ai-database-26ai-to-lead-1-2-trillion-market-by-bridging-the-agentic-reasoning-gap/ 、https://jamsql.com/blog/2026-08-27-whats-new-oracle-26ai/ 、https://clouddb.substack.com/p/the-rise-of-ai-databases-oracle-microsoft | 2025-10 〜 2026-08 | T1\*、T3\*、T4\* |
| W6-18 | インストールベース(Next Platform 2018、DBTA 2011、Landbase) | https://www.nextplatform.com/2018/03/22/turbulence-and-opportunity-ahead-in-the-oracle-sparc-base/ 、https://dbta.com/Editorial/Think-About-It/Oracle-Announces-1000th-Installation-of-Oracle-Exadata-Database-Machine-76439.aspx 、https://data.landbase.com/technology/oracle-exadata/ | 2011、2018 | T3\*、T4\* |
| W6-19 | The Register(Oracle DB の Azure ライセンス、2024-02)、HPCwire(2020 Exadata)、Oracle Licensing Experts(Cloud@Customer の TCO)、Constellation | https://www.theregister.com/2024/02/05/oracle_database_deal_in_azure/ 、https://www.hpcwire.com/bigdatawire/2020/09/14/oracle-touts-an-exadata-backlog/ 、https://oraclelicensingexperts.com/research/oracle-cloud-at-customer-lockin-cost-2026/ 、https://www.constellationr.com/insights/news/oracles-q2-results-key-customer-takeaways | 2020-09、2024-02、2026 | T3\*、T4\* |
| W6-20 | Oracle から PostgreSQL・Aurora への移行(助言会社、ベンダー) | https://oraclelicensingexperts.com/white-papers/oracle-postgresql-migration-tco-model/download/ 、https://oraclelicensingexperts.com/compare/oracle-to-aurora/ 、https://oraclelicensingexperts.com/compare/oracle-database-vs-postgresql/ 、https://redresscompliance.com/oracle-postgresql-migration-download 、https://www.enterprisedb.com/index.php/blog/why-and-how-switch-oracle-postgresql 、https://blog.clearscale.com/master-your-oracle-to-aurora-postgresql-migration-journey/ 、https://marketplace.microsoft.com/en-ca/product/hexawaretechnologiesltd-nj1734355056208.modernize-oracle-db-to-postgres-assessment | 2026 年(白書は 2026-06 更新) | T4\* |
| W6-21 | Kurian の経歴(TechTarget) | https://www.techtarget.com/searchcloudcomputing/blog/The-Troposphere/Oracle-vet-Kurian-will-make-Google-Cloud-more-enterprise-savvy | 2018 | T3\* |
| 未読の候補 | 見出しだけ検索結果に出た資料(本文は取得できず): theCUBE Research「Cloud Database Migration Costs: AWS RDS for Oracle vs. Oracle ATP」、UpperEdge「Autonomous Database: How Oracle is Seeding its Customer Base」 | https://thecuberesearch.com/cloud-database-migration-costs-aws-rds-oracle-vs-oracle-atp/ 、https://upperedge.com/oracle/autonomous-database-how-oracle-is-seeding-its-customer-base/ | — | 未読 |
| 既存 | R4(`/tmp/claude-0/-home-user-AI/dc835e23-63d2-59ca-97e5-1016f0daf3fe/scratchpad/orcl/research2/R4_database_at.md`)と、その出典 [R4-01]〜[R4-35] | — | — | — |

---

## 11. 既存調査 R4 への追記・更新の候補

1. R4 の欠損 12(Q4 FY25 のマルチクラウド成長率「前期比 +115%」)は、本回の 5 本の要約で一致し、**採用可能**に更新できる(T3\*)。
2. R4 の 10-K の移行寄与 $4.3B は、FY26 10-K で **$5.4B** に更新されている(T1\*)。
3. R4 の「2,300 エージェント」(単一系統)は、本回に複数の説明会本文サイトの要約で一致し、「実行回数 350 万回超」も併記された。
4. R4 のリージョン: AWS は 2026-08-13 に **22** に到達(R4 の目標 22 と一致)。Azure は 34 と 33 が併存。
5. R4 の「移行倍率 欠損」は、**「3 倍」「3〜5 倍」という発言の候補が 1 回の要約に出た**ため、「欠損 → 未確認の候補あり」に変わる。逐語照合が残る。

---

## 12. 検索ログ(24 回 / 上限 24 回。standard 20、extended 4)

| # | モード | 目的 |
|---|---|---|
| 1 | standard | Nadella の Database@Azure 発言 |
| 2 | standard | AWS(Jassy・Garman)の発言 |
| 3 | standard | Kurian の発言 |
| 4 | standard | マルチクラウド DB の売上推計 |
| 5 | standard | 2026-08 の Oracle・AWS 協業 |
| 6 | standard | Google のリージョン・顧客(2026) |
| 7 | standard | Gartner の DBMS シェア |
| 8 | standard | Ellison・Catz の移行倍率(1 回目) |
| 9 | standard | The Register の Gartner 記事 |
| 10 | standard | PostgreSQL 移行の動向 |
| 11 | standard | AI Data Platform・ベクトル検索の採用(Q1 FY27) |
| 12 | standard | FAM の DB $20B の内訳 |
| 13 | standard | Merv Adrian の DBMS 売上 |
| 14 | extended | 移行時の顧客あたり売上の倍率(「3 倍」「3〜5 倍」が出た検索) |
| 15 | standard | Azure の 2026 年の動向 |
| 16 | extended | Q1 FY27 説明会の逐語(DB、エージェント) |
| 17 | standard | Q2 FY26 説明会の「3〜5 倍」の確認 |
| 18 | standard | Q2 FY24 説明会の「3 倍」の確認 |
| 19 | standard | インストールベース・顧客数 |
| 20 | extended | 26ai の採用指標 |
| 21 | extended | 「3〜5 倍」の再確認(10-K の $5.4B が出た検索) |
| 22 | standard | Q1 FY27 の顧客事例 |
| 23 | standard | Aurora・Azure SQL の価格と移行件数 |
| 24 | standard | Google 経営陣の発言(再試行) |
