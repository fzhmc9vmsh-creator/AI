# R3b 経営陣の成長シナリオ・公約と実績(SoFi Technologies, NASDAQ: SOFI / CIK 0001818874)

取得日: 2026-10-18 / 作成: R3b担当 / 範囲: 経営陣シナリオ、数値目標、ピース一覧、公約vs実績、資本配分、報酬、開示変更。分析・結論は含まない。

## 0. 取得環境の制約(最初に読むこと)

| 項目 | 状況 |
|---|---|
| WebFetch | 全ホストで `getaddrinfo ENOTFOUND`(sec.gov, investors.sofi.com, bullfincher.io, en.wikipedia.org で確認)。使えない |
| curl(proxy経由) | sec.gov, investors.sofi.com, fool.com, nasdaq.com, mitrade.com, seekingalpha.com, businesswire.com はすべて 403(egress policyで拒否)。迂回は行っていない |
| WebSearch | 約35回で「このターンの検索予算(200回、全エージェント共有)を使い切った」と拒否。以降の検索は不可 |
| 帰結 | **全数値・全引用は WebSearch が返した要約文(中身はT1ページの抜粋・要約)に依拠。T1の原文(PDF/HTM)は一度も直接開いていない。** URLは検索結果に表示された一次資料のURL |

表記ルール:
- **[S]** = WebSearch要約経由。出所URLはT1(SEC/IR)だが原文未照合。数値は要約者の書き写しなので、最終利用前に原文で照合が必要。
- **[R]** = 姉妹エージェントR1aのノート(`/tmp/claude-0/-home-user-AI/73833936-79f8-51ae-b2cd-a06ac0cb76aa/scratchpad/research/notes_R1a.md`, `notes_raw.md`)経由。これも原典はWebSearch抽出で、私は再検証していない。
- **[T3]** = 報道・個人ブログ・集計サイト。
- 「(派生)」= 私が取得済みの数値から単純計算した値。公式値ではない。
- 引用は英語原文を短く+和訳。トランスクリプトPDFとの照合は未実施。

---

## 1. シナリオの骨格(経営陣が繰り返す言葉)

### 1-1. 繰り返し語の取得状況

| 語 | 取得状況 | 出所 |
|---|---|---|
| Financial Services Productivity Loop(FSPL) | 確認。2025年1月(Q4'24コール)で「満足した会員がより多くの製品を使うフライホイール」と説明。Q2'26リリース本文にも登場 | [S] Q2'26 8-K 検索結果 / [T3] Medium, Fool Q4'24 |
| "Acquire, cross-sell, reinvest, innovate, repeat" | Noto発言として抜粋が表示(Q4'24コール) | [S] https://www.fool.com/earnings/call-transcripts/2025/01/27/sofi-technologies-sofi-q4-2024-earnings-call-trans/ |
| "everything app" | Q2'26コールでNotoが既存会員の製品追加(51%)の説明に使用 | [S] Q2'26コール要約 |
| Rule of 40 | Q1'26: 18期連続・スコア72(売上+41%、EBITDAマージン31%)。Q2'26: 19期連続・スコア70(売上+40%、EBITDAマージン30%) | [S] Q1'26/Q2'26コール要約 |
| メンバー数×1人当たり製品数×製品当たり収益 | Q2'26でNotoが成長ドライバーとして提示 | [S] Q2'26コール要約 |
| "one-stop shop" / "top 10 financial institution" | **検索結果の要約内では確認できなかった**(「未取得」。存在しないことの証明ではない) | — |
| AI(Cash Coach等)、国際展開 | **未取得** | — |
| クリプト/SoFiUSD/SoFi Pay | 断片のみ(§3参照)。Q3'25コールの見出しに "accelerating investment in AI, crypto, and SoFi Pay" | [T3] https://seekingalpha.com/news/4509620-sofi-outlines-36-percent-revenue-growth-target-for-2025-while-accelerating-investment-in-ai (日付未確認。36%は$3.54B÷2024年$2.6B(派生)と整合するのでQ3'25の可能性) |

### 1-2. 直近4四半期+αの発言・主要KPI(時系列)

| 日付 | 資料(URL) | 発言/記述(原文短く) | 和訳 | 主要数値 |
|---|---|---|---|---|
| 2025-01-27 | Q4'24コール https://www.fool.com/earnings/call-transcripts/2025/01/27/sofi-technologies-sofi-q4-2024-earnings-call-trans/ [S] | "remain confident in delivering 2026 EPS in the range of $0.55 to $0.80 per share" / medium-term "20% to 25% compounded annual revenue growth through 2026" を上回る見込み | 2026年EPSが1株$0.55〜0.80の範囲になる確信は変わらない/中期の年平均売上成長20〜25%(2026年まで)を上回る見込み | 2024年: 新製品の30%が既存会員、新会員の約40%が30日以内に2つ目の製品。2025年の増分EBITDAマージン約30%、正常化税率約26% |
| 2025-10-28 | Q3'25 8-K/IRリリース https://www.sec.gov/Archives/edgar/data/1818874/000181887425000204/a2025q3earningsrelease.htm [S][R] | (引用未取得) | — | 会員12.6M(+35%、+905k)、製品18.6M(+36%)、既存会員による新製品比率40%、純収益$962M(リリース見出しの表記。調整後かは未確認)、純利益$139M、2025年ガイダンス引上げ(下記§2) |
| 2026-01-30 | Q4'25コール https://s27.q4cdn.com/749715820/files/doc_financials/2025/q4/SoFi-Q4-FY-2025-Earnings-Conference-Call-Transcript.pdf [S] | "...we expect to deliver compounded annual adjusted net revenue growth of at least 30% from 2025 to 2028." / "Given the investments we've made to date, we see opportunities to accelerate growth in 2027 and 2028 across several products that are just beginning to scale." / "Adjusted net revenue was a record at over $1 billion, up 37% year-over-year, marking our first billion-dollar quarter." | 2025〜2028年に調整後純収益で年平均30%以上の成長を見込む(話者はInvesting.comがCFO Lapointeと表記、未確定)/これまでの投資により2027〜28年に成長を加速できる製品がある(要約はクリプト、ブローカレッジ、住宅ローン、学生ローンを挙げる)/初の10億ドル四半期 | 会員13.7M(+35%)、製品20.2M(+37%)[R]、調整後純収益>$1.0B(+37%)、調整後EBITDA $318M(+60%)、純利益$174M、手数料ベース収益$443.3M(+53%)[S] |
| 2026-04-29 | Q1'26コール https://s27.q4cdn.com/749715820/files/doc_financials/2026/q1/SoFi-Q1-2026-Transcript-docx.pdf [S] | 18期連続Rule of 40(72)。2四半期連続で現金収益$1B超。SoFi Plusを4/1に有料のみのサブスクとして再開 | (要約の言い換え。原文引用は未取得) | 会員14.7M(+35%)、製品22.2M(+39%)、既存会員による新製品比率43%(Q4'25 40%、Q1'25 36%)、個人ローン組成$8.3B(過去最高) |
| 2026-07-29 | Q2'26コール https://s27.q4cdn.com/749715820/files/doc_financials/2026/q2/SoFi-2Q-2026-Earnings-Transcript_FINAL.pdf [S] | "too many large attractive growth areas for us to invest versus adding even more profitability"(EBITDA見通しを上げず再投資する理由。話者は経営陣、個人は未確定) | 投資すべき大きな成長領域が多すぎて、利益率をさらに上げるより投資を選ぶ | 会員15.8M(+35%、+1.1M)、製品24.4M(+42%)、既存会員による新製品比率51%(前年35%)、調整後純収益$1.2B(+40%)、調整後EBITDA $358M(+44%) |
| 2026-07-29(同) | 同上 [S] | SMB融資: "one that we think we can be incredibly competitive on, similar to personal loans and credit cards"(Noto) | SMB融資は個人ローンやカードと同様に十分競争できる領域 | Big Business Banking(法人向け)を開始、LPBを中小企業向け・ホームエクイティ向けに拡張、Basepoint Capitalと3年・$3Bの契約 |
| 2026-07-29(同) | 同上 [S] | 金利見通し: "1 to 2 hikes in 2026, versus the expectation of 2 rate cuts when we first provided our 2026 guidance" | 2026年は1〜2回の利上げを想定(当初ガイダンス時は2回の利下げ想定) | EPSガイダンスの税率前提を22%に(当初比+700bp) |
| 2026-07-29 | Q2'26リリース https://www.businesswire.com/news/home/20260729569583/en/ [S] | FSPLが「会員エンゲージメントと製品採用を高める効果を増している」と記述 | — | SoFi Plus加入者20万超、SoFi Plus加入の既存会員の25%が別製品を追加 |

その他の経営陣発言(T3、日付未確認):
- Noto: SoFi Plusが「1年後に100万会員・年間収益$120M」に届かなければ失望する旨。"just a matter of when, not if"(2028年までの利益目標について)。[T3] https://247wallst.com/investing/2026/05/29/down-30-from-its-highs-sofi-is-speeding-toward-aggressive-long-term-profits/
- Yahoo見出し「SoFi CEO Anthony Noto Calls 2026 A 'Defining Year' Amid Guidance Raise」(本文未取得)[T3] https://finance.yahoo.com/markets/stocks/articles/sofi-ceo-anthony-noto-calls-123614698.html

### 1-3. 四半期KPIの推移(上記コール・リリースより)

| 四半期 | 発表日 | 会員 | 製品 | 既存会員による新製品比率 | 調整後純収益 | 調整後EBITDA | GAAP純利益 |
|---|---|---|---|---|---|---|---|
| Q3'25 | 2025-10-28 | 12.6M(+35%) | 18.6M(+36%) | 40% | 純収益$962M(見出し表記、調整後かは未確認) | (未取得) | $139M |
| Q4'25 | 2026-01-30 | 13.7M(+35%) | 20.2M(+37%) | 40% | >$1.0B(+37%) | $318M(+60%) | $174M |
| Q1'26 | 2026-04-29 | 14.7M(+35%) | 22.2M(+39%) | 43% | $1,087M(+41%)[R] | $339.9M(+62%、31%)[R] | $166.7M[R] |
| Q2'26 | 2026-07-29 | 15.8M(+35%) | 24.4M(+42%) | 51% | $1,205.6M(+40%)[R] | $357.8M(+44%)[R] | $156.6M[R] |

注: Q4'25の1株利益は要約間で不一致($0.12と$0.13)。未解決。

---

## 2. 数値目標

### 2-1. 2026年ガイダンス(期初→修正)

| 項目 | 期初(2026-01-30、Q4'25リリース) | 修正(2026-07-29、Q2'26リリース) | 出所 |
|---|---|---|---|
| 調整後純収益 | 約$4.655B(約+30%) | **$4.75〜4.85B(+32〜35%)に引上げ** | [S] https://www.sec.gov/Archives/edgar/data/1818874/000181887426000008/a2025q4earningsrelease.htm / https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000050/a2026q2earningsrelease.htm |
| 調整後EBITDA | 約$1.6B(マージン約34%) | 約$1.6B据え置き(マージン33〜34%) | 同上 |
| 調整後純利益 | 約$825M | 約$825M据え置き(マージン約17%、期初は約18%と表示) | 同上 |
| 調整後EPS | 約$0.60 | 約$0.60据え置き。**税率22%前提(当初比+700bp)**。中堅の税率ならば約$0.65[R] | 同上 + [R] |
| 会員増 | 前年比30%以上 | 前年比30%以上 | 同上 |
| Q1'26ガイダンス(1月時点)[R] | 調整後純収益約$1.04B、EBITDA約$300M、EPS約$0.12 | 実績: 調整後純収益$1,087M、EBITDA$339.9M、調整後EPS$0.12 | [R] |
| Q2'26ガイダンス(4月時点) | 調整後純収益約$1.115B、EPS約$0.10〜0.11 | 実績: 調整後純収益$1,205.6M、調整後EPS$0.12 | [S] https://seekingalpha.com/news/4581783-sofi-forecasts-q2-2026-adjusted-net-revenue-of-1_115b-and-eps-of-0_10-0_11-while-expanding / [R] |

経営陣の説明(Q2'26): 収益を上げた一方EBITDA・EPSを上げなかった理由は再投資(上掲引用)。EPSは22%税率で据え置き(税率が当初想定並みなら約$0.65[R])。「$0.05の税率影響」は、要約間で四半期影響($0.005説/$0.05説)が食い違う。通期影響とすれば$0.60→$0.65と整合する(派生の推測、未検証)。

### 2-2. 中期目標・2027年以降

| 目標 | 内容 | 定義・期限 | 発表日/出所 |
|---|---|---|---|
| 2025〜2028 調整後純収益CAGR | 年平均30%以上 | 2025年から2028年 | 2026-01-30 Q4'25コール/リリース [S] |
| 2025〜2028 調整後EPS CAGR | 年平均38〜42% | 同上。調整後EPS | 同上 [S](話者は未確認) |
| 2027〜28年の成長加速 | 「いくつかの製品で成長を加速できる」 | クリプト、ブローカレッジ、住宅ローン、学生ローンが対象と要約 | 同上 [S] |
| 旧: 中期売上CAGR | 年平均20〜25%(2026年まで)を上回る見込み | 2026年まで | 2025-01-27 Q4'24コール [S] |
| 旧: 2026年EPS | $0.55〜0.80 | 2026年。基準(GAAP/調整後)は要約で不明 | 2025-01-27 Q4'24コール [S]。Yahoo記事(JPMorgan会議、約521日前=2025年初)でもNotoが再確認 [T3] https://finance.yahoo.com/news/sofi-targets-30-member-growth-200601286.html |
| ROTCE目標 | **未取得** | — | — |
| 2027年の個別ガイダンス | **未取得**(公式の2027年数値は確認できず) | — | — |

Investor Day: 2025〜2026年に専用のInvestor Dayは**検索で確認できなかった**(不在の証明ではない)。2028年目標は2026-01-30の決算コールで提示されている。

### 2-3. 2025年ガイダンスの推移(参考。§4の実績と対応)

| 時点 | 調整後純収益 | 調整後EBITDA | 純利益/EPS | 会員増 | 出所 |
|---|---|---|---|---|---|
| 2025-01 期初(Q4'24リリース) | $3.200〜3.275B | $845〜865M | GAAP純利益$285〜305M、GAAP EPS $0.25〜0.27 | 2.8M以上(+28%) | [S] https://www.sec.gov/Archives/edgar/data/1818874/000181887425000006/q42024earningsrelease.htm |
| 2025 Q2リリース | (未取得) | (未取得) | (未取得) | 3.0M以上 | [S] |
| 2025-10 Q3リリース | 約$3.54B(前回約$3.375B) | 約$1.035B(前回$960M) | 調整後EPS 約$0.37(前回$0.31) | 3.5M以上(約+34%) | [S] https://www.sec.gov/Archives/edgar/data/1818874/000181887425000204/a2025q3earningsrelease.htm / Q3'25投資家資料 https://s27.q4cdn.com/749715820/files/doc_financials/2025/q3/2025-Q3-Investor-Presentation-v_Final.pdf |

---

## 3. ピース一覧

| ピース | 発表/完了日 | 目的(経営陣説明) | 規模 | 現在の進捗を示す数値 | 出所 |
|---|---|---|---|---|---|
| 銀行免許: Golden Pacific Bancorp | 契約 2021-03-08、FRB承認 2022-01-18、完了 2022-02-02 | 全国規模のデジタル銀行事業。Golden Pacificのコミュニティ銀行事業は維持 | 現金対価$22.3M(Sacramento、資産約$150M)。OCC条件で初期払込資本$750M以上、SoFiは$750M拠出予定 | 預金 $45.5B(2026-06-30、前期比+$5.3B)、2025-12-31は$37.5B。ブローカー預金$4.5B。預金金利はウェアハウス調達より156bp低く年間節約額約$712.6M。NIM 5.98%。預金は平均負債の90%超[R]。総自己資本比率18.8%(要件10.5%、二次情報)[R] | [S] https://www.sec.gov/Archives/edgar/data/1818874/000181887422000010/exhibit991_8-k222022.htm / https://www.sec.gov/Archives/edgar/data/1818874/000181887424000107/sofitechnologies2023arsvf.pdf / [R] |
| Galileo | 発表 2020-04-07、完了 2020-05-14 | 消費者中心から機関向けPlatform-as-a-Serviceへ多角化 | 現金+株式 総額$1.2B | §3-1参照 | [S] 同上10-K/S-1抜粋 |
| Technisys | 発表 2022-02-22、完了 2022-03 | 完全統合型の多製品デジタルバンキング技術。「AWS of fintech」。自社を複数の第三者コアから単一コアへ移行 | 約$1.1B、全額株式(約84M株、完全希薄化後の10%未満) | §3-1参照 | [S] https://www.sec.gov/Archives/edgar/data/1818874/000181887422000014/exhibit991_8-k2222022.htm / https://www.sec.gov/Archives/edgar/data/1818874/000181887422000029/q42021earningsrelease.htm |
| Wyndham Capital Mortgage / 住宅ローン | **未取得**(買収の発表日・規模) | — | — | 住宅ローン組成: Q3'25約$945M(うちHEL $352M)、2025年通期$3.4B、Q1'26 $1.2B(+137%)、Q2'26 $1.4B(+74%)[R] | [R] |
| Loan Platform Business(LPB) | 開始時期・Blue Owl/Fortressの契約は**未取得**。Basepoint Capitalと3年$3B契約(Q2'26コールで言及) | 他社資金で融資を組成し手数料収益化(手数料ベース収益の拡大) | Q3'25: LPB組成$3.4B、連結調整後純収益への寄与$167.9M。Q4'25: LPB調整後純収益$194M(年率$775M)。Q1'26: LPB向け個人ローン$3.0B。Q2'26: LPB向け個人ローン$3.1B、連結調整後純収益寄与$143.3M[R] | 手数料ベース収益 $472.3M(総収益の39%、Q2'26)[R]。Q1'26はLPBへ個人ローン+住宅ローン計$3.8Bを売却/移管[R] | [R] / [S] Q2'26コール要約 |
| クリプト再開、ステーブルコイン、ブロックチェーン送金 | **未取得**(再開日・SoFiUSD開始日・SoFi Pay詳細) | — | — | Q1'26のSeeking Alpha見出しに「SoFiUSDとBig Business Bankingの拡大」。Q4'25コールで「クリプト」を2027〜28年の加速対象に挙げたとの要約 | [T3] https://seekingalpha.com/news/4581783-sofi-forecasts-q2-2026-adjusted-net-revenue-of-1_115b-and-eps-of-0_10-0_11-while-expanding / [S] |
| SoFi Invest(私募ファンド・オプション等) | **未取得** | — | — | 会員内訳(Q2'26): Money 約7.9M、Invest 約3.9M、FS製品21.3M[R] | [R] |
| クレジットカード、Smart Card、ホームエクイティ | **未取得**(個別の開始日・規模) | — | — | HEL Q3'25 $352M[R]。LPBのホームエクイティ拡張(Q2'26) | [R] |
| SoFi Plus | 2026-04-01に有料のみのサブスクとして再開 | 会員のエンゲージメントと製品追加 | 加入者20万超。Notoは100万会員・年$120Mに届かなければ失望と発言[T3] | 加入した既存会員の25%が別製品を追加(Q2'26リリース) | [S] / [T3] |
| Big Business Banking | Q2'26で開始 | 法人顧客への展開 | (規模未取得) | — | [S] Q2'26コール要約 |
| AI関連(Cash Coach等)、国際展開 | **未取得** | — | — | — | — |
| 増資・転換社債・優先株償還 | §5参照 | §5参照 | §5参照 | §5参照 | §5参照 |

### 3-1. Tech Platform(Galileo+Technisys)の数値推移と、買収時の約束

| 期間 | セグメント純収益 | 貢献利益(率) | 総アカウント数 | 出所 |
|---|---|---|---|---|
| 2022通期 | $315.1M(Technisysは2022年3月から計上) | $76.5M | 130.7M | [S] 10-K FY2024 https://www.sec.gov/Archives/edgar/data/1818874/000181887425000016/sofi-20241231.htm |
| 2023通期 | $352.3M(+12%) | $94.8M(+24%) | 145.4M | 同上 |
| 2024通期 | $395.2M(+12%) | $127.0M | 167.7M(+15%) | 同上 |
| Q1'25 | $103.4M(+10%) | $30.9M(30%) | 158.4M(+5%) | [S] Q1'25 8-K https://www.sec.gov/Archives/edgar/data/1818874/000181887425000068/a2025q1earningsrelease.htm |
| Q2'25 | $109.8M(+15%) | $33.2M(30%) | 約160M(+1%) | [S] |
| Q3'25 | $114.6M(+12%) | $32.4M(28%) | 約158M | [S][R] |
| Q4'25 | $122M(+19%) | $48M(39%)? | — | [R](貢献利益の帰属は「要確認」と注記あり) |
| 2025通期(派生) | 約$449.8M(Q1〜Q4の単純合計。Q4は[R]) | — | — | 私の算術。公式通期値は未取得 |
| Q1'26 | $75.1M(**-27%**) | $12.0M(16%、前年30%) | 約133M(派生) | [R] / [S] |
| Q2'26 | $84.5M(**-23%**、前期比+13%) | $11.8M(14%、前年30%、貢献利益-65%[R]) | 135M(**-16%**) | [S] https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000050/a2026q2earningsrelease.htm |

- 減収の理由(会社説明): 「大口顧客が2025年12月31日までに完全にプラットフォームから移行した」 [S]。顧客名は**未取得**。
- 注: 総アカウント数にはGalileo上のSoFi自社(会社間)アカウントが含まれる旨が10-Q/10-Kに記載 [S]。
- Technisys買収時(2022-02-22)の約束 [S]: (a) 2025年末までに累計の増分収益$500〜800M(Technisysの基礎収益+垂直統合による収益シナジー)、(b) 2023〜2025年に累計コスト削減$75〜85M、以降は年$60〜70M。実績の開示(Technisys単体収益、削減額の累計)は**未取得**。FY2024年次報告書は「ほぼ統合済み」とし、累計の対比は載せていないと要約 [S]。

---

## 4. 公約と実績(2021〜2026)

### 4-1. SPAC時の予測(2021年) vs 実績

出所: S-4/A(2021-02-10付)の経営陣予測表 https://www.sec.gov/Archives/edgar/data/1818874/000162828021001825/ipoe-20210210.htm [S]。投資家向け資料(2021-01、"Project Lightning" PIPE) https://s27.q4cdn.com/749715820/files/doc_presentation/2021/Project-Lightning_PIPE-Investor-Presentation_-SoFi-FINAL-(01.06.2021)2.pdf (本文は未参照、URLのみ確認)。

| 年 | 予測: 調整後純収益 | 予測: 調整後EBITDA | 実績: 調整後純収益 | 実績: 調整後EBITDA | 結果 |
|---|---|---|---|---|---|
| 2021 | $980M | $27M | **未取得**(Q2'21時点で据え置き。H2の学生ローン借換え収益見込みを$40M下方修正した旨が記載) | 未取得 | 未取得 |
| 2022 | $1,500M | $254M | 未取得 | 未取得 | 未取得 |
| 2023 | $2,106M | $484M | 約$2.06B(派生: 2024年$2.6B÷1.26) | 未取得 | 収益はほぼ予測並み(派生・要確認) |
| 2024 | $2,808M | $788M | 約$2.6B(+26%)[S] | 約$0.70B(派生: 2025年$1.1B÷1.58) | **未達**(収益約-7%、EBITDA約-11%、派生値) |
| 2025 | $3,669M | $1,177M | 約$3.6B(+38%)[S] | 約$1.1B(+58%、マージン29%)[S] | 収益ほぼ並み(約-2%)、EBITDAは$1B超だが予測に約-7% |

- 経営陣の言(2021年のディール関連コール): 2021年に成長率を58%へ加速、2025年に売上$3.7B・調整後EBITDA>$10億になる [S]。
- 実績の出所: FY2024は10-K/ARS https://www.sec.gov/Archives/edgar/data/1818874/000181887425000062/sofitechnologies2024ars.pdf、FY2025はQ4'25コール(Quartr要約 https://quartr.com/events/sofi-technologies-inc-sofi-q4-2025_3YiUNvGe)。Q4'25コールの文字起こしでは「$3.6B」が"tangible revenue"と誤記されており、調整後純収益か総収益かは未確認 [S]。

### 4-2. 公約→期限→結果

| # | 公約(発表日・出所) | 期限 | 結果 | 備考 |
|---|---|---|---|---|
| 1 | 四半期GAAP黒字化(Q4'22リリース、2023-02、2023-08に再確認)[S] https://www.sec.gov/Archives/edgar/data/1818874/000181887423000005/q42022earningsrelease.htm | 2023年Q4 | **達成(期限どおり)**: Q4'23 GAAP純利益$47.9M(EPS $0.02) | 2023年通期は純損失(のれん減損を除くと-$53.6M)。Q4'24リリースは「5四半期連続・初の通期GAAP黒字」と記載 [S] |
| 2 | 2024年通期GAAP純利益$95〜105M(Q4'23リリース)[S] | 2024年 | 通期実績は**未取得**。Q4'24単独GAAP純利益$332.5M(うち評価性引当金解除$258.4M)[R] | 税効果で基準が変わる。調整後純利益Q4'24 $61.0M(調整後EPS $0.05)[R] |
| 3 | 2025年期初ガイダンス(2025-01)[S] | 2025年 | **前倒し/上振れ**: 調整後純収益 $3.2〜3.275B→約$3.6B、調整後EBITDA $845〜865M→約$1.1B、純利益 $285〜305M→$481M、EPS $0.25〜0.27→$0.39 | 年内に3回引上げ。EPS/純利益は期初GAAP基準、後に調整後基準へ(§7)。基準差の影響は未検証 |
| 4 | 2025年の会員増2.8M以上(+28%)(2025-01) | 2025年 | **前倒し**: 3.0M以上→3.5M以上に引上げ。YE25会員13.7M(+35%)から逆算で約3.55M増(派生) | |
| 5 | 中期の売上CAGR 20〜25%(2026年まで)(2025-01-27)[S] | 2026年 | 2026年ガイダンスは+32〜35%(**上回る見込み**、進行中) | |
| 6 | 2026年EPS $0.55〜0.80(2025-01-27)[S] | 2026年 | ガイダンス約$0.60(範囲内、下側)。進行中 | 税率22%前提。基準(調整後/GAAP)は不明 |
| 7 | Technisys: 累計増分収益$500〜800M、累計コスト削減$75〜85M(2022-02-22)[S] | 2025年末 | **検証不能(開示未取得)** | Tech Platform全体の収益は§3-1。Technisys単体は未取得 |
| 8 | Tech Platform成長(2024年ガイダンス「低〜高10%台の増収」との要約あり、原文未確認)[S] | 2024年 | 2024年+12%(要約) | 2025年はQ1〜Q4が+10/+15/+12/+19%、2026年Q1〜Q2は-27/-23%(大口顧客離脱) |
| 9 | 2025〜2028 売上CAGR30%以上、EPS CAGR 38〜42%(2026-01-30)[S] | 2028年 | 進行中(2026年はQ2時点で売上ガイダンスを引上げ) | 2025年EPS $0.39→2026年ガイダンス約$0.60(派生で+54%、基準が異なる可能性あり) |
| 10 | Q1'26ガイダンス(2026-01)[R] | 2026年Q1 | 売上・EBITDA上振れ、EPSは一致 | 数値は§2-1 |
| 11 | Q2'26ガイダンス(2026-04)[S] | 2026年Q2 | 売上は上振れ(約$1.115B→$1,205.6M)、EPS上振れ($0.10〜0.11→$0.12) | |

---

## 5. 資本配分

### 5-1. 資本イベント一覧

| 日付 | 種別 | 価格 | 株数/金額 | 経営陣の説明(目的) | その後の指標 | 出所 |
|---|---|---|---|---|---|---|
| 2021-09-29 | 0%転換社債(2026年満期)の発行・上限引上げ | 転換価格は未取得 | $1.1B。キャップドコール費用約$104.3M。満期2026-10-15 | 一般事業目的 | 2026-03-31時点で潜在転換株数19,096,202株(10-Q)。**2026-10-15満期を経過。償還/転換の結果は未取得** | [S] https://www.sofi.com/newsroom/sofi-increases-size-offering/ / 10-Q https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000037/sofi-20260331.htm |
| 2022-02/03 | Technisys買収(株式対価) | — | 約84M株、約$1.1B | §3 | — | [S] |
| 2024-03 | 2029年満期転換社債 | — | $750M→オプション行使で$862.5M | 12.5% Series 1優先株の償還、高コスト債務の返済、一般事業目的。同時に2026年満期債$600Mを普通株と交換 | 当時のアナリストメモは、この交換でTBVPSが約+10%と見積り(2024年、[T3]) | [S] https://s27.q4cdn.com/749715820/files/doc_news/SoFi-Technologies-Inc.-Announces-Proposed-Convertible-Senior-Notes-Offering-Due-2029-2024.pdf / https://www.moomoo.com/community/feed/sofi-s-750m-convertible-notes-offering-sparks-optimism-analysts-see-bullish-turn |
| 2025-07-29 | 普通株の公募 | **$20.85** | 71,942,450株(約$1.5B)+グリーンシュー10,791,367株全行使=82,733,817株(2025-07-31クローズ)。82,733,817×$20.85=約$1.725B(派生)、10-Q記載の純受取は約$1.7B | 一般事業目的(運転資金、その他の事業機会)。10-Qは「資金の一部で高コスト債務を削減」と記載 | TBVPS(2025-06-30) $4.72は増資前の値 | [S] https://www.sec.gov/Archives/edgar/data/1818874/000181887425000160/ex992pricingpressrelease.htm / 10-Q https://www.sec.gov/Archives/edgar/data/1818874/000181887425000180/sofi-20250630.htm |
| 2025-12-04 | 普通株の公募 | **$27.50**(前日終値約$29.60より約7%安) | 54,545,454株(約$1.5B)。グリーンシュー部分行使を含め合計57,754,660株(派生で約$1.59B) | 一般事業目的。資本ポジションの強化、選択肢・資本管理の効率の向上、追加成長・事業機会への資金 | 下記TBV推移 | [S] https://www.sec.gov/Archives/edgar/data/1818874/000181887425000225/ex992pricingpressreleasede.htm / https://www.businesswire.com/news/home/20251204760313/en/SoFi-Technologies-Inc.-Announces-Pricing-of-Public-Offering-of-Common-Stock |
| 2026年 | 新規の増資・転換社債・優先株 | — | **検索では確認できず** | 二次情報1件: 経営陣は「ガイダンス期間と中期計画では資金調達不要(自己資金)」と示した(どの記事か特定できず。Q2'26関連のTBV検索結果に含まれていた記述で、原文未確認) | — | [T3] 出所特定不可 |

### 5-2. TBV・EPS・株数

| 時点 | TBV | TBVPS | 株数関連 | EPS | 出所 |
|---|---|---|---|---|---|
| 2025-06-30 | 約$5.3B(派生: $9.5B÷1.8) | $4.72 | 希薄化後加重平均 1,182,877千株(Q2'25) | GAAP希薄化後 $0.08(Q2'25)[R] | [S] Q2'26リリース / 10-Q Q2'26 https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000054/sofi-20260630.htm |
| 2026-06-30 | **$9.5B(+80%)** | **$7.34(+56%)** | 希薄化後加重平均 1,351,990千株(+14%)。TBV÷TBVPSから約1.29B株(派生)、前年約1.12B株 | GAAP希薄化後 $0.12(Q2'26、前年$0.08)、調整後EPS $0.12 | 同上 |
| FY2025 | — | — | — | EPS $0.39(純利益$481M)。希薄化後株数は約1.23B株(派生) | [S] Q4'25コール |

- 通期2025年の純利益合計(Q1 $71.5M[R]+Q2 $97M+Q3 $139M+Q4 $174M=約$481M)は報告値$481Mと整合(派生)。
- その他の期のTBVPS(2021〜2025の年末値): **未取得**。GuruFocusの断片に「Tangible Book per Share $6.90」「Book Value per Share $8.58」があるが日付不明のため採用しない。

### 5-3. Notoの自社株買い(公開市場、Form 4)

| 日付 | 株数 | 価格 | 金額 | 出所 |
|---|---|---|---|---|
| 2024-05-03 / 05-23 / 05-24 / 06-14 | 各約$200,000 | $6.50〜6.92 | 各約$200K(合計約$0.8M、派生) | [T3] https://www.secform4.com/insider-trading/1613438.htm |
| 2026-03-02 | 56,000 | 約$17.88 | 約$1.0M | [T3] https://www.tradingview.com/news/tradingview:4f62f1897418c:0-sofi-technologies-ceo-anthony-noto-buys-56-000-shares/ |
| 2026-03-17 | 28,900 | $17.32 | 約$500.5K | [T3] SecForm4 |
| 2026-05-08 | 15,878 | $15.73 | 約$249.8K | [T3] |
| 2026-05-11 | 15,545 | $16.00 | 約$248.8K | [T3] |
| 2026-06-16 | 13,888 | $18.06 | 約$250.8K | [T3] https://www.stocktitan.net/sec-filings/SOFI/form-4-so-fi-technologies-inc-insider-trading-activity-f798db743c79.html |

- 2026年合計: 約130,211株・約$2.25M(5取引、[T3]集計)。2021〜2023年の購入履歴: **未取得**。
- 保有(Form 4の直接保有): 2026-03-16 11,915,196株、2026-06-16後 約11.96M株、2026-09-14後 12,276,337株(同日の取引はオプション行使と源泉徴収分の処分約188,259株@$17.32で、買いではない)。Form 4原本 https://www.sec.gov/Archives/edgar/data/0001818874/000161343826000022/wk-form4_1789602225.xml / https://www.sec.gov/Archives/edgar/data/0001818874/000161343826000008/wk-form4_1773879399.xml [S]
- 株価水準メモ: 2025-12の増資時約$29.6、2026年のNoto買付は$15.73〜18.06。24/7 Wall St.は2026-10-15付で「2026年に急落」と表現 [T3] https://247wallst.com/investing/2026/10/15/sofi-technologies-imploded-in-2026-a-wall-street-pro-predicts-it-will-double-in-2027/。Q2'26決算翌日に株価約-9% [T3] https://www.fool.com/investing/2026/07/30/sofis-tangible-book-value-grew-80-in-a-year-yet-th/

---

## 6. 報酬(DEF 14A)

出所: 2026年DEF 14A(2026-04-30付、年次総会2026-06-17)https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000032/sofi-20260430.htm / 2025年DEF 14A https://www.sec.gov/Archives/edgar/data/1818874/000181887425000060/sofi-20250415.htm / 2024年 https://www.sec.gov/Archives/edgar/data/1818874/000181887424000105/sofi-20240408.htm / 2023年 https://www.sec.gov/Archives/edgar/data/1818874/000181887423000069/sofi-20230428.htm 。いずれも[S](抜粋のみ)。

### 6-1. Noto報酬の構成

| 項目 | 2024年 | 2025年 |
|---|---|---|
| Summary Compensation Table合計 | 約$28.07M(前年比+54%、[T3] https://www.panabee.com/news/sofi-ceo-s-pay-jumps-54-to-28-million-amid-shift-to-performance-based-compensation) | **$30,275,733**(AFL-CIO PayWatchは中央値従業員の248倍 https://aflcio.org/paywatch/SOFI) |
| Stock awards(RSU+PSU、付与日公正価値) | — | $25,308,941(合計の84%) |
| 非株式インセンティブ(年次現金賞与) | — | $2,760,000(9%) |
| その他 | — | $1,206,792(個人用航空機約$744K、関連税調整約$55K、個人警護約$408K) |
| 年次現金賞与の目標 | — | 基本給の200%。2026年DEF 14Aで閾値〜最大の目標値と実績を全面開示するようになったと記載 |
| 年次株式報酬の目標額 | PSU 25%・RSU 75%(2024年2月付与: PSU 726,217、RSU 2,178,650) | **目標額$29.5M、PSU 50%・RSU 50%** |
| 2025年付与の内訳(2025-03-11) | — | RSU約$11.58M、PSU約$13.73M(付与日公正価値)。PSU目標1,027,983株/最大1,927,468株、最大達成時の価値$25,750,974 |
| 2026年付与 | — | PSUは同じ50/50を継続。RSUは4年間四半期ベスト。PSUは2026-01-01から3年間 |

2025年の賞与の指標: 「財務目標3つ+運営目標1つ」とのみ取得(個別の指標名・ウェイト・実績は**未取得**)。
2025年say-on-pay賛成率: 約76.2%([T3]集計サイト、未検証)。2026年年次総会: Notoの取締役選任は賛成約381.2M票・保留約9.6M票(2026-06のForm 8-K https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000043/sofi-20260617.htm)[S]。

### 6-2. 業績連動(PSU)の指標

| 項目 | 内容 | 種別 |
|---|---|---|
| 主指標 | **Absolute Growth in Tangible Book Value(TBVの絶対額の成長)**。支払い0〜150% | **総額指標**(1株当たりではない、と要約は記述) |
| TSR | 相対TSRは独立の加重指標ではなく**修正係数**: ±25%、上限187.5%。絶対TSRがマイナスなら目標(100%)で頭打ち。2026年付与から目標水準は比較群の**55パーセンタイル**以上の成績が必要 | 株価連動(修正係数のみ) |
| 資本条件 | 総リスク加重資本比率が10.5%を下回った時点で全PSU没収 | 規制資本 |
| 期間 | 2024年付与: 2024-01-01〜2026-12-31。2025年付与: 2025-01-01〜2027-12-31。2026年付与: 2026-01-01から3年 | — |
| TBVの定義 | 2025年PSU契約書は、直近の監査済財務諸表に基づくTBV成長で、**「資本調達、買収、無形価値、のれんの影響を除く」**と要約が記述。**この除外が増資分を除外する意味か、原文での正確な文言は要確認(最優先の原文確認事項)** | — |
| 目標値 | 2025年付与の表に閾値$1.36B。2024年付与について$1.05B(閾値)・$1.2B(目標)との断片。**表の整合は未確認** | — |
| 過去の株価ハードル型 | 2021〜2026の間、株価が$25/$35/$45を90日以上維持で計6.4M株を付与する旨([T3]、X投稿)。権利確定の状況は**未取得** | 株価連動 |

出所: [S] 2026 DEF 14A、2025 PSU契約書様式 https://www.sec.gov/Archives/edgar/data/1818874/000181887425000049/formofpsuawardagreement-ex.htm 、8-K https://www.sec.gov/Archives/edgar/data/1818874/000181887425000049/sofi-20250321.htm 、[T3] https://x.com/EverythingSOFI/status/1686353175463227392?lang=en

### 6-3. Notoの保有株数

- Form 4上の直接保有: 12,276,337株(2026-09-14取引後)。
- 委任状説明書の「Security Ownership」表(オプション・RSU等を含む受益所有、持株比率): **未取得**。

---

## 7. 経営陣の交代・開示の変化

| 項目 | 内容 | 出所 |
|---|---|---|
| CFO | Chris LapointeがQ4'25〜Q2'26コールでCFOとして登場(Q2'26コール: 「CEO Anthony Noto and CFO Chris Lapointe」)。就任日・前任者・他の経営陣交代は**未取得** | [S] |
| ガイダンスの基準 | 2025年期初(2025-01): **GAAP純利益($285〜305M)とGAAP EPS($0.25〜0.27)**。2025年Q3引上げ時と2026年ガイダンス: **調整後EPS・調整後純利益**($0.37、$0.60、$825M)。基準の変更時点はQ2〜Q3'25の間と推定(未確認) | [S] Q4'24リリース / Q3'25リリース / Q4'25リリース |
| 税率前提 | 2025年: 正常化税率約26%(Q4'24コール)。2026年: 22%前提で期初比+700bp(Q2'26)。期初の2026年前提は約15%前後と読めるが数値は**未取得** | [S] |
| 2024年Q4の評価性引当金解除 | GAAP純利益$332.5M(うち$258.4M)。通期の税効果合計は資料により$265.3M〜$271M | [R] |
| 新規KPI・強調指標 | 手数料ベース収益(Q4'25 $443.3M・Q2'26 $472.3M=総収益の39%)、「現金収益」$1B超(Q1'26)、Rule of 40スコア、LPB調整後純収益(年率$775M、Q4'25)、既存会員による新製品比率(Q1'25 36%→Q2'26 51%)、1会員当たり製品数(Q2'26 1.54) | [S][R] |
| Tech Platformの会計開示 | 総アカウント数に会社間(SoFi自社)アカウントを含むことを10-Q/10-Kで注記 | [S] |
| 報酬開示 | 2026年DEF 14Aで年次賞与の閾値〜最大の目標と実績を全面開示 | [S] |
| 次回開示 | Q3'26決算は2026-10-27(火)7am ET発表、8am ETコール(未発表) | [R] https://secure.businesswire.com/news/home/20260929120531/en/SoFi-Schedules-Conference-Call-to-Discuss-Q3-2026-Results |

---

## 取れなかった項目

原因は§0の環境制約(WebFetch全滅、curl 403、WebSearch予算枯渇)。次の段階で原文を直接開ける環境なら、下記URLから取得できる。

| 区分 | 未取得の内容 | 原文URL(検索結果に表示されたもの) |
|---|---|---|
| 発言原文 | 直近4四半期のNoto/Lapointeの発言の原文(特に"one-stop shop"、"top 10 financial institution"、AI、国際展開、クリプト、ステーブルコイン、国際送金への言及)。確認できた引用は§1-2の数件のみ | Q2'26 https://s27.q4cdn.com/749715820/files/doc_financials/2026/q2/SoFi-2Q-2026-Earnings-Transcript_FINAL.pdf / Q1'26 https://s27.q4cdn.com/749715820/files/doc_financials/2026/q1/SoFi-Q1-2026-Transcript-docx.pdf / Q4'25 https://s27.q4cdn.com/749715820/files/doc_financials/2025/q4/SoFi-Q4-FY-2025-Earnings-Conference-Call-Transcript.pdf / Q3'25 は https://seekingalpha.com/article/4834022-sofi-technologies-inc-sofi-q3-2025-earnings-call-transcript |
| 株主への手紙 | 2025年次報告書の株主への手紙(Technisys・Tech Platformの進捗記述の確認用) | https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000034/sofitech2025ars.pdf |
| 目標 | ROTCE目標、2027年の個別ガイダンス、「2026年EPS $0.55〜0.80」の基準(GAAP/調整後)と最初の発表日、Investor Dayの有無の確定 | Q4'24リリース https://www.sec.gov/Archives/edgar/data/1818874/000181887425000006/q42024earningsrelease.htm |
| ピース | Wyndham Capital Mortgage買収の詳細、LPBの開始時期とBlue Owl/Fortress契約の条件、クリプト再開日、SoFiUSD、SoFi Pay、SoFi Investの拡充、カード/Smart Card、AI(Cash Coach)、国際展開、Technisys単体の収益と削減額の実績 | 各8-K/プレスリリース |
| 実績 | 2021〜2023年の調整後純収益・調整後EBITDAの実績値(2023年は派生のみ)、2024年の調整後EBITDA実績、2024年通期GAAP純利益、2022〜2024年の期初ガイダンス全般(2024年のGAAP純利益$95〜105Mのみ取得) | Q4'21 https://www.sec.gov/Archives/edgar/data/1818874/000181887422000029/q42021earningsrelease.htm / Q4'22 https://www.sec.gov/Archives/edgar/data/1818874/000181887423000005/q42022earningsrelease.htm / Q4'23 https://www.sec.gov/Archives/edgar/data/1818874/000181887424000004/q42023earningsrelease.htm |
| 資本配分 | 各資本イベント前後のTBVPS・EPS(2021〜2025年末値)、2021年転換社債の転換価格と2026-10-15満期の決着(償還/株式発行の有無・株数)、Notoの2021〜2023年の購入履歴 | 10-K各期、Form 4原本 |
| 報酬 | 受益所有表(Notoの保有比率)、PSUのTBV目標値の正確な表、TBV定義の「資本調達の影響を除く」文言の原文、年次賞与の指標名・ウェイト・実績、2026年付与の目標株数 | 2026 DEF 14A(上記URL) |
| 経営陣交代 | CFOの就任日・前任者、その他の役員交代、Tech Platformの大口顧客名 | 8-K(Item 5.02)、10-Q Q1'26/Q2'26 |
| 不一致の未解決 | Q4'25の1株利益($0.12/$0.13)、Q2'26の税率影響($0.005/$0.05)、2025年通期の$3.6Bが調整後純収益か総収益か、Q4'25 Tech Platformの貢献利益($48M・39%)の帰属 | 原文照合が必要 |
