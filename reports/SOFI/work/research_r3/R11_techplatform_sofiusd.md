# R11: SoFi (SOFI) テクノロジー・プラットフォームの底打ちと SoFiUSD によるコスト削減

調査日 2026-10-18 / 最新確定四半期 Q2 2026(2026-07-29 発表)/ 担当: 株式調査 R3 周

## 要点(8 行)

1. **売上と口座は Q1'26 で底、Q2'26 は反発。** セグメント収益 $75.1M → $84.5M(前期比 +12.5%、会社表示 +13%)、総アカウント 132.9M → 134.8M(+1.9M)。ただし反発は 1 四半期だけで、前年比は −23%、−16% のまま。
2. **貢献利益は底打ちしていない。** Q1 $12.0M → Q2 $11.8M、率 16% → 14%(前年 30%)。売上が +$9.4M 増えても貢献利益は −$0.2M。理由の開示は未取得。
3. **回復の根拠は報道要約のみ(原文未閲覧)。** 新規 13 社が Q1 に収益化、米大手通信ブランドとの提携が 2026 年内に開始、中期目標は 20〜25% 成長、2026 年は +20%(離脱顧客を除く、Q4'25 コール要約)。Q1 の同条件成長は約 12% で、20% に届いていない。
4. **下期の水準は低い可能性。** 2026 通期 $325M(T4 ブログ。会社値か未確認)が正しければ、下期は四半期平均 $82.7M で Q2($84.5M)以下(私の計算)。
5. **SoFi 自身の移行。** SoFi Money を新クラウド型コアへ移行開始(Q2'26 コール要約)。時期・進捗率・削減額は未取得。Peach Finance を 2026 年 5 月下旬に買収(条件非開示)、全体を「SoFi Technology Solutions(STS)」に統合。
6. **前年比が楽になる時期。** Q1'26 が大口顧客なしの最初の四半期なので、Q1'27(2027 年 4〜5 月発表)から素の成長率に戻る(私の推定)。Q4'25 の貢献利益 $48M は一時要因を含む可能性があり、未確認。
7. **SoFiUSD の実績。** 2025-12-18 発表、2026-05-27 会員向け開始、流通残高は Q2 末で約 $3 億(報道のみ)。2026-09-22 に自社カード(年 $250 億超の見込み)の Mastercard 決済を SoFiUSD に切替。Galileo 顧客への展開は「予定」で、採用を公表した銀行は無し。
8. **コスト削減額と運用益は会社が数字を出していない。** 1 件当たり費用、削減額、利ざやは未取得。GENIUS 法は 2025-07-18 成立、OCC の最終規則は 2026 年 10 月末の目標。競合は JPM Coin、PYUSD(約 $41 億)、Circle(信託銀行認可)。

**調べ方の限界**: WebFetch と curl は遮断(DNS 失敗・プロキシ 403)。値はすべて WebSearch の要約から取った。信頼度の T1 は「情報源の種類が会社開示・SEC」の意味で、原本を私が読んだ意味ではない(検索要約経由)。逐語の引用は、検索結果が引用符つきで返したものだけに限り、他は「要約」と明記した。計算は「私の計算」と書いた。WebSearch は 30 回すべて使用。

信頼度: T1 = 会社開示・SEC / T2 = 当局 / T3 = 報道・アナリスト / T4 = 集計サイト・ブログ

---

## A-1. 四半期推移(Q1 2024〜Q2 2026)と前期比(QoQ)

| 四半期 | 収益 $M | 前年比 | 前期比(私の計算) | 貢献利益 $M(率) | 総アカウント(M) | 出所 / 信頼度 |
|---|---|---|---|---|---|---|
| Q1'24 | 94.4 | +21% | 未算出(Q4'23 未取得) | 未取得 | 151.0(Q4'23 は 145.4) | 8-K https://www.sec.gov/Archives/edgar/data/1818874/000181887424000115/q12024earningsrelease.htm / T1。口座: https://www.galileo-ft.com/news/galileo-tops-150-million-accounts-in-another-strong-quarter / T3(会社運営サイト) |
| Q2'24 | 95.4 | +9% | +1.1% | 31.2(32.7%、計算) | 158.5(Q2'25 の前年値) | 8-K https://www.sec.gov/Archives/edgar/data/1818874/000181887424000169/q22024earningsrelease.htm / T1 |
| Q3'24 | 102.5 | +14% | +7.4% | 約 33.1(Q3'25 の −2% から逆算) | 160.2(+17%) | 8-K https://www.sec.gov/Archives/edgar/data/1818874/000181887424000229/q32024earningsrelease.htm / T1。口座: https://tech.sofi.com/news/galileo-q3-2024-earnings-accounts-pass-160-million/ / T3 |
| Q4'24 | 102.8 | +6% | +0.3% | 32.1(31.2%) | 167.7(通期 10-K。**要検証**) | 10-K https://www.sec.gov/Archives/edgar/data/1818874/000181887425000016/sofi-20241231.htm / T1。R1b・R3b の既得値 |
| Q1'25 | 103.4 | +10% | +0.6% | 30.9(29.9%) | 158.4 | Q1'26 10-Q の前年値 https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000037/sofi-20260331.htm / T1 |
| Q2'25 | 109.8 | +15% | +6.2% | 33.2(30.2%) | 160.0 | Q2'26 10-Q https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000054/sofi-20260630.htm / T1 |
| Q3'25 | 114.6 | +12% | +4.4% | 32.4(28.3%) | 約 158 | R1b の既得値(Q3'25 8-K・10-Q) / T1 |
| Q4'25 | 約 122 | +19% | +6.5% | 約 48(約 39%)。**要確認** | **未取得** | Q4'25 コール要約 / T3。8-K https://www.sec.gov/Archives/edgar/data/1818874/000181887426000008/a2025q4earningsrelease.htm |
| **Q1'26** | **75.1** | **−27%** | **−38.4%** | **12.0(16.0%)**。前年 30.9 から −61% | **132.9**(−16%) | Q1'26 10-Q(上記) / T1。8-K https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000020/a2026q1earningsrelease.htm |
| **Q2'26** | **84.5** | **−23%** | **+12.5%**(会社 +13%) | **11.8(14.0%)**。前年比 −65% | **134.8**(134,804,238。−16%、前期比 +1.9M = +1.4%) | Q2'26 10-Q・8-K https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000050/a2026q2earningsrelease.htm / T1 |

**底打ちの判定(私の整理)**

| 指標 | 判定 | 根拠 |
|---|---|---|
| 収益 | 底を打った可能性が高い(1 点のみ) | Q1'26 $75.1M が底、Q2'26 は前期比 +12.5%。会社は「既存顧客の収益化の進展と新規顧客の寄与」と説明(コール要約 T3) |
| 総アカウント | 底打ち(1 点のみ) | 132.9M → 134.8M。ただし前年比 −16% は変わらず |
| 貢献利益 | **未底打ち** | $12.0M → $11.8M、率 16% → 14%。上半期合計 $23.8M(前年比 −63%、10-Q)。固定費が従来の売上規模に合わせた水準のまま残っている可能性があるが、開示は未取得 |

**注意点**
- 口座数の定義: Q4'25 のリリースは、Galileo の PaaS 上の SoFi 自社口座を「総アカウント」に含めると説明した(検索要約 T1)。Q4'24 の 167.7M と Q1'25 の 158.4M の間に断絶があり、定義差の可能性がある。時系列の比較は Q1'25 以降を使うのが安全。
- 口座数の減少: Q3'25 約 158M → Q1'26 132.9M で約 25M 減(私の計算)。Q4'25 の口座数が未取得のため、大口顧客の分とその他の要因を分けられない。
- Q4'25 の貢献利益 $48M: 前期比 +$15.6M に対し売上は +$7.4M。大口顧客との契約終了に伴う一時的な収益を含む可能性があるが、**確認できていない**(仮説)。含むなら Q4'25 の +19% は膨らんでいる。

---

## A-2. 新規顧客・パイプライン・ガイダンス・経営陣の発言

| 項目 | 内容 | 日付 | 出所 / 信頼度 |
|---|---|---|---|
| 新規顧客数 | Q1'26 に収益を出し始めた新規クライアントが 13 社(前年同期は収益なし)。社名は未取得 | Q1'26 コール(2026-04 下旬〜05 上旬) | https://www.tikr.com/blog/sofi-technologies-beat-earnings-and-still-fell-13-is-sofi-stock-a-buy-in-2026 / T3(二次要約)。原文: https://s27.q4cdn.com/749715820/files/doc_financials/2026/q1/SoFi-Q1-2026-Transcript-docx.pdf(未閲覧) |
| 大型提携 | 米国の通信大手 3 社に入るブランドとの提携が 2026 年内に開始予定。社名・規模は未取得 | 同上 | 同上 / T3 |
| 2026 年ガイダンス(Tech Platform) | 成長率 +20%(移行した大口顧客を除く)。ほかに Financial Services 40% 超、Lending 23% | Q4'25 コール(2026-01-30) | https://www.stocktaper.com/earningsCallSummary/SOFI/2025/Q4 / T3(要約。原文は未閲覧) |
| 同条件の実績 | Q1'26 は大口顧客を除くと前年比 約 +12%。ガイダンス +20% より低い | Q1'26 | https://www.heygotrade.com/en/blog/sofi-stock-drops-12-q1-2026-buy-dip-cut-loss/ / https://finance.yahoo.com/markets/stocks/articles/sofi-slides-9-q1-earnings-125023553.html / T3 |
| 2026 通期の収益 | 約 $325M との記述。会社ガイダンスか、ブログの推計かは**未確認**。H1 実績は $159.6M なので、$325M なら H2 は $165.4M(四半期平均 $82.7M)で Q2 水準を下回る(私の計算) | Q1'26 後 | https://www.heygotrade.com/en/blog/sofi-stock-drops-12-q1-2026-buy-dip-cut-loss/ / T4 |
| 中期目標 | 20〜25% の複利成長に戻す(期限なし) | Q1'26 | TIKR(上記) / T3 |
| 会社全体のガイダンス | 2026 調整後純収益 $4.75〜4.85B(Q2 で上方修正)。セグメント別の更新は見つからず(Q2 の Tech Platform ガイダンスは**未取得**) | 2026-07-29 | Q2'26 8-K(上記) / T1 |
| 2027 年の見通し | **未取得** | — | — |
| ブランド統合 | Galileo・Technisys・(買収分)を「SoFi Technology Solutions」に統合。処理・銀行コア・決済・リスクの一体提供 | Q1'26 コールほか | TIKR(上記) / T3。公式サイト https://tech.sofi.com/platform/ / T1 |
| 買収 | Peach Finance(融資管理・サービシング、カード・与信枠・BNPL・分割払いの基盤)を 2026 年 5 月下旬に買収、価格非開示。STS に統合。同年の買収はほかに Composer、PrimaryBid | 2026-05 下旬 | https://ibsintelligence.com/ibsi-news/sofi-acquires-peach-finance-to-expand-lending-capabilities/ / https://pulse2.com/sofi-acquires-peach-to-expand-lending-infrastructure/ / https://www.pymnts.com/?p=3759312 / https://www.nasdaq.com/articles/sofi-technologies-q2-earnings-call-highlights / T3 |
| 過去の新規契約 | 2024-10-16: SoFi 自身が Cyberbank Core を採用(商業決済のスポンサーバンク・プログラム。デビット・プリペイド・ACH・ワイヤ)。Banco Nación(アルゼンチン)が Cyberbank Digital を選定(日付不明) | 2024-10 | https://s27.q4cdn.com/749715820/files/doc_news/SoFi-Technologies-to-Adopt-Galileos-Cyberbank-Core-for-New-Commercial-Payment-Services-Sponsor-Banking-Program-2024.pdf / https://finextra.com/pressarticle/102777/sofi-adopts-galileos-cyberbank-core / T1。Banco Nación: https://tech.sofi.com/platform/ / T1(会社サイト) |
| 2025〜2026 の銀行・大企業との個別契約の発表 | **未取得**(2026 年の Cyberbank Core 新規顧客の発表は検索で見つからず) | — | — |

**経営陣の発言(原文は未閲覧。英語は検索要約の言い換えで、逐語ではない)**

| 日付 | 内容(英語の要約) | 和訳 | 出所 / 信頼度 |
|---|---|---|---|
| 2026-07-29(Q2'26 10-Q の文言。引用符つきで返却) | "a large client which fully transitioned off our platform prior to December 31, 2025" | 「2025 年 12 月 31 日より前にプラットフォームから完全に移行した大口顧客」 | https://www.sec.gov/Archives/edgar/data/0001818874/000181887426000054/sofi-20260630.htm / T1 |
| 2026-07-29(Q2'26 コール) | Segment growth came from "further monetization of existing clients as well as contributions from new clients"(要約) | 既存顧客の収益化の進展と、新規顧客の寄与(による伸び) | https://www.fool.com/earnings/call-transcripts/2026/08/07/sofi-sofi-q2-2026-earnings-call-transcript/ 、会社の原文 https://s27.q4cdn.com/749715820/files/doc_financials/2026/q2/SoFi-2Q-2026-Earnings-Transcript_FINAL.pdf(未閲覧) / T3 |
| 2026-01-30(Q4'25 コール) | Tech Platform +20% in 2026, excluding the transitioned client(要約) | 2026 年は移行した顧客を除き +20% | Stocktaper(上記) / T3 |
| 2026 年 Q1 コール | Management is determined to return the segment to 20–25% compounding growth over time(要約) | 時間をかけて 20〜25% の複利成長に戻す | TIKR(上記) / T3 |

---

## A-3. SoFi 自身のシステムを Galileo・Technisys へ移す取り組み

| 項目 | 内容 | 時期 | 出所 / 信頼度 |
|---|---|---|---|
| 目的(買収時) | 複数の第三者コアから単一の自社コアへ移行し、完全統合型の銀行技術基盤を持つ。地域銀行・信用組合への外販 | 2022-02 発表 | https://www.spglobal.com/market-intelligence/en/news-insights/articles/2022/2/sofi-aims-to-build-core-banking-solutions-for-community-banks-in-technisys-deal-69017826 / T3。Technisys 取得は R3b(約 $1.1B、全額株式) |
| 買収時の約束 | 2025 年末までの累計増分収益 $500〜800M、累計コスト削減 $75〜85M(2023〜25)。実績の対比は**未取得** | 2022-02 | R3b の既得値(8-K) / T1 |
| Cyberbank Core の自社採用 | 商業決済のスポンサーバンク・プログラムに Cyberbank Core を採用 | 2024-10-16 | 上記 2024 年プレスリリース / T1 |
| AI アシスタント | SoFi が Cyberbank Konecta(AI 仮想バンキング助手)を導入、応答の高速化とチャット離脱の低下と Noto が説明 | 2025 | 検索要約のみ(出所の URL なし) / T3 |
| **SoFi Money の新コア移行** | Q2'26 に、新しいクラウドネイティブのバンキングコアへ SoFi Money の移行を開始。コアは STS が自社開発。「近く他の銀行・金融機関・ブランドパートナーも利用可能になる」との説明(要約)。自社を最初の顧客にして、大手機関への販売の実績にする狙いと解説(アナリスト) | 2026-07-29 | https://www.theglobeandmail.com/investing/markets/stocks/SOFI/pressreleases/3729955/sofi-sofi-q2-2026-earnings-call-transcript/ / https://www.fool.com/earnings/call-transcripts/2026/08/07/sofi-sofi-q2-2026-earnings-call-transcript/ / T3 |
| 和訳(要約) | 「SoFi Money を、STS が完全に自社開発した新しい最新のクラウドネイティブ・バンキングコアへ移し始めた。このプラットフォームは近く他の銀行、金融機関、ブランドパートナーも使えるようになる」 | | 同上 / T3(逐語ではない) |
| デビット・当座・預金・カードなど他の領域の移行、完了時期、進捗率、コスト削減額 | **未取得** | — | — |
| ステーブルコインの Galileo 展開 | Mastercard との提携(2026-03)で、Galileo が発行銀行にカード決済を SoFiUSD で行う選択肢を最初に提供する会社の 1 つになる見込み。2026-09 時点で他行の採用の公表なし | 2026-03〜09 | https://www.fintechfutures.com/blockchain-crypto-digital-assets/mastercard-integrates-sofiusd-for-stablecoin-settlement / https://cryptobriefing.com/sofi-stablecoin-settlement-mastercard-sofiusd/ / T3 |

---

## A-4. 大口顧客離脱の影響が一巡する時期

| 項目 | 内容 | 出所 / 信頼度 |
|---|---|---|
| 離脱の経緯 | Chime の S-1 は、Galileo との契約の修正を記載: 最低月額支払いの廃止と、**$18M の解約料を 2026 年 3 月に支払う**(S-1 の文言として検索要約が返却)。修正前は 2026-06-30 前は理由がある場合に限り Galileo 側から解約できた。Chime は ChimeCore へ移行。SoFi の 10-Q は顧客名を出さず、「2025-12-31 より前に完全に移行」と記載 | 検索結果 https://fintechdd.substack.com/p/galileos-total-accounts-drop-explained 、https://sacra.com/chat/h/fcab73a0-19a6-44f9-8642-3ea5ef685757/ / T3〜T4(S-1 の原本は未閲覧)。10-Q は T1 |
| 解約料の会計処理 | どの四半期の収益に計上されたかは**未取得**。Q4'25 の貢献利益 $48M(上記)との関係は仮説 | — |
| 大口顧客の規模(概算) | Q1'26 の同条件成長が約 +12% なら、Q1'25 の大口顧客以外の収益は $75.1M ÷ 1.12 ≈ $67M。差は約 $36M(Q1'25 の約 35%、年換算 約 $145M)。**私の概算**で、Q1'26 に一時収益が含まれると崩れる | 計算(根拠: TIKR の「約 12%」T3) |
| 前年比が楽になる時期 | Q1'26 が大口顧客なしの最初の四半期。**Q1'27(2027 年 4〜5 月発表)から**前年同期も大口顧客なしで、素の成長率が見える。Q2'26〜Q3'26 の前年比は −20% 台のまま続く可能性が高い。Q4'25 に残りの大口顧客収益や一時収益があれば、Q4'26 は前年比が楽にならない(私の推定) | 計算・推定 |
| 2027 年の成長 | 会社の数値は未取得 | — |

---

## B-5. SoFiUSD の仕組み・用途・流通残高

| 項目 | 内容 | 日付 | 出所 / 信頼度 |
|---|---|---|---|
| 発行と準備 | SoFi Bank, N.A.(国法銀行)が発行する全額準備のステーブルコイン。連邦準備の口座に現金で準備を置き、流動性・信用リスクを排除し、運用益をパートナーと保有者に還元可能と説明。1:1 で償還可能。Ethereum と Solana | 2025-12-18 発表 | https://www.businesswire.com/news/home/20251218701481/en/SoFi-Launches-Fully-Reserved-Stablecoin-to-Power-Financial-Infrastructure-for-Banks-Fintechs-and-Enterprise-Partners / T1。https://theblock.co/post/383146/sofi-launches-sofi-usd-stablecoin / T3 |
| 準備の構成(不一致) | Börse Express は「短期米国債 85%・現金 15%」と報じる。会社の発表要約は「連邦準備の口座の現金」。**未解消** | 2026-05 | https://www.boerse-express.com/news/articles/sofi-aktie-166-kurssprung-nach-stablecoin-start-911922 / T3〜T4 |
| 会員向け開始 | アプリで売買・保有・交換が可能。次の段階はトークン化預金への交換(利息と FDIC 保険)。最初の中央集権型取引所の提携先は Bullish(機関投資家向け)。一部報道は「全会員に公開は 6 月」 | 2026-05-27 | https://secure.businesswire.com/news/home/20260527091798/en/SoFiUSD-Becomes-the-First-Stablecoin-Issued-by-a-US-National-Bank-to-Launch-on-a-Banking-Platform / https://www.nasdaq.com/press-release/sofiusd-becomes-first-stablecoin-issued-us-national-bank-launch-banking-platform-2026 / T1。「6 月」: https://www.chartmill.com/news/external/133459/sofi-technologies-stablecoin-push-can-sofiusd-scale-payments / T3 |
| BitGo | BitGo Bank & Trust をステーブルコイン発行基盤(Stablecoin-as-a-Service)に選定 | 2026-03-05 | https://www.tikr.com/blog/sofi-is-up-8-this-week-after-mastercard-and-bitgo-expand-its-stablecoin-network / T3 |
| Mastercard との提携 | Mastercard 網の決済に SoFiUSD を利用可能にする契約 | 2026-03 | https://www.theblock.co/amp/post/391974/sofi-and-mastercard-to-enable-sofiusd-stablecoin-settlement-across-global-payments-network / T3 |
| **自社カードの決済切替** | 自社のデビット・クレジット全体を SoFiUSD で Mastercard 決済に切替。**年 $250 億超**を見込む(予測であり実績ではない)。取引は 70% が Solana との見出しもあり。日中・週末・祝日の決済に対応。加盟店は SoFiUSD を保有する必要なし。従来のカード決済は 1〜2 営業日で週末・祝日は止まる | 2026-09-22 | https://fintech.global/2026/09/23/sofi-brings-stablecoin-settlement-to-mastercard-network/ / https://cryptobriefing.com/sofi-stablecoin-settlement-mastercard-sofiusd/ / https://solanacompass.com/news/sofi-becomes-first-nationally-chartered-us-bank-live-with-stablecoin-settlement-on-mastercard-70-running-on-solana / https://genfinity.io/2026/09/22/sofi-stablecoin-settlement-mastercard-solana/ / T3(会社のプレスリリース原本は未取得) |
| 法人向け | Big Business Banking が Q2'26 に SoFi Exchange Network 上で取引処理を開始、法人顧客が SoFiUSD でリアルタイム決済。初期参加に Mastercard と BitGo と報道。API 提供は 2026-07-01(R9 の既得値) | 2026-Q2 | https://thedefiant.io/news/tradfi-and-fintech/sofi-says-sofiusd-settlement-now-live-on-q2-earnings-call / T3 |
| Galileo 顧客の決済 | 展開は「予定」。他行が公式に採用を表明した例は無し | 2026-09 | https://cryptobriefing.com/sofi-stablecoin-settlement-mastercard-sofiusd/ / T3 |
| **流通残高** | Q2 末(2026-06-30)に **約 $3 億**。会社の開示では確認できず、ZACKS 系の分析記事と Crypto Briefing が同じ値を引用 | 2026-06-30 | https://www.chartmill.com/news/external/133459/sofi-technologies-stablecoin-push-can-sofiusd-scale-payments / https://cryptobriefing.com/sofi-stablecoin-settlement-mastercard-sofiusd/ / T3 |
| 残高の推移(Q1'26、Q3'26) | **未取得** | — | — |
| 規模の目安(私の計算) | 年 $250 億 ÷ 365 日 ≒ 日 $6,800 万。Q2 末の残高 $3 億は約 4.4 日分。世界のステーブルコイン総額は約 $3,000 億台(T4)なので、SoFiUSD は約 0.1% | 計算 |

---

## B-6. 従来の送金網を置き換えるコスト削減の説明・試算

| 項目 | 内容 | 出所 / 信頼度 |
|---|---|---|
| 会社の試算(1 件当たり費用・削減額) | **未取得**。数値の説明は見つからず(複数の検索で確認) | — |
| 会社の定性的な説明 | 「24 時間・ほぼ即時の決済を、1 セント未満の料金で」(パートナー向け。"near-instant settlement at fractional-cent pricing around the clock" の要約)。国際送金は「従来の金融網より遅延が少なく費用が低い」 | 2025-12-18 発表 https://www.businesswire.com/news/home/20251218701481/en/SoFi-Launches-Fully-Reserved-Stablecoin-to-Power-Financial-Infrastructure-for-Banks-Fintechs-and-Enterprise-Partners / T1(要約) |
| 経営陣の発言(2026-03) | SoFiUSD は、世界中の人が「より速く、安く、安全に」お金を動かす戦略の中心(要約。逐語ではない) | https://www.fintechfutures.com/blockchain-crypto-digital-assets/mastercard-integrates-sofiusd-for-stablecoin-settlement / T3 |
| カード決済のコスト | 発行銀行・加盟店の費用削減額は**未取得**。便益として確認できたのは、決済の時間短縮(1〜2 営業日 → 日中・週末も可)のみ | https://cryptobriefing.com/sofi-stablecoin-settlement-mastercard-sofiusd/ / T3 |
| SoFi Pay の国際送金 | Lightspark の Universal Money Address を使い、米ドルをビットコインに換えて Lightning Network で送り、受取側の通貨に換えて銀行口座へ入金。メキシコで開始、後に 30 か国超と報道。**手数料表・取扱額・件数は未取得**。「従来の送金事業者より低い手数料」と会社が主張 | 2025-08-19 https://www.businesswire.com/news/home/20250819638580/en/SoFi-Partners-with-Lightspark-to-Power-Blockchain-Enabled-International-Money-Transfers / T1。https://www.theblock.co/post/367506/sofi-taps-lightspark-as-it-looks-to-use-bitcoin-lightning-for-an-international-money-transfer-service / T3。30 か国超: https://www.nasdaq.com/articles/fintech-stock-sofi-technologies-just-proved-ultimate-cryptocurrency-has-clear-use-case-0 / T3 |
| ステーブルコイン経由かの区別 | SoFi Pay の国際送金は Lightning(ビットコイン)で、SoFiUSD とは別の仕組み(検索要約)。SoFiUSD を送金に使う計画はあるが、実績は未取得 | 同上 / T3 |
| 参考: 暗号資産取引 | Q2'26 の暗号資産取引収益 $134.3M、取引コスト $133.1M、差し引き $1.2M | https://theblock.co/post/410053/sofi-crypto-transaction-revenue-grows-to-134-million-second-quarter / T3 |

---

## B-7. 規制と競合

| 項目 | 内容 | 日付 | 出所 / 信頼度 |
|---|---|---|---|
| GENIUS 法 | 2025-07-18 成立。決済用ステーブルコインの発行者は 1:1 の準備(現金・保険付き預金・短期米国債)。施行日は **2027-01-18 か、最終規則から 120 日後のいずれか早い方** | 2025-07-18 | https://stablecoininsider.org/q3-2026-stablecoin-trends-to-expect-genius-act-bank-stablecoins-and-the-1-trillion-race.md / https://en.cryptonomist.ch/2026/08/20/genius-act-crypto-regulation/ / T3〜T4(法文は未閲覧) |
| OCC の規則 | 2026-02-25 に提案(準備、資本、監査、監督。376 ページとの報道)。Gould 長官は **2026 年 10 月末までに最終化**と発言(従来は 11 月)。新規発行者の最低資本 $5M との要約は未検証 | 2026-02-25 / 2026-10 | https://occ.gov/news-issuances/news-releases/2026/nr-occ-2026-9.html / T2。https://www.kucoin.com/news/flash/occ-aims-to-finalize-genius-act-stablecoin-rules-by-october-31 / https://lcx.com/en/cryptonews/occ-head-promises-final-genius-rules-by-november / T3 |
| 利息(利回り)の扱い | 検索では確認できず。**私の知識(未検証)**: GENIUS 法は発行者が保有者に利息・利回りを払うことを禁じる。SoFi は保有者への還元を「トークン化預金への交換」で行う計画と読める。PayPal の PYUSD 報酬(3.7〜4% と報道が割れる)が OCC の審査対象との報道あり | 2026 | PayPal: https://stablecoininsider.org/pyusd-q1-2026-stablecoin-report/ / T4 |
| 競合: 大手行 | JPMorgan の JPM Coin(預金トークン JPMD)を Base 上で機関投資家向けに提供(2025-11)。Citi が法人向けのトークンサービスを稼働(1 報道)。JPM・BofA・Citi・Wells の共同発行の協議(2025 年報道、2026 年の状況は未確認) | 2025〜2026 | https://eco.com/support/en/articles/15275171-bank-issued-stablecoins-2026-sofi-jpm-coin-and-the-new-wave / T4 |
| 競合: 既存の大手 | 市場総額 約 $3,000 億〜$3,220 億、USDT 約 $1,890 億、USDC 約 $780 億(2026-05 のブログ。1 件のみ)。Circle は国法信託銀行の認可を取得(2026-05 のブログ) | 2026-05 | https://blockeden.xyz/zh/blog/2026/05/12/post-genius-act-stablecoin-issuance-race/ / T4 |
| 競合: PayPal | PYUSD の時価総額 約 $41 億(2026-03、Paxos 発行) | 2026-03 | https://stablecoininsider.org/pyusd-q1-2026-stablecoin-report/ / T4 |
| 位置づけ | SoFiUSD は「国法銀行が公共ブロックチェーン上で発行し、銀行基盤に載せた最初のステーブルコイン」と会社が主張(5 月発表の見出し) | 2026-05-27 | Nasdaq プレスリリース(上記) / T1 |

---

## B-8. 準備資産から得る運用益と手数料の見込み

| 項目 | 内容 | 出所 / 信頼度 |
|---|---|---|
| 収益の仕組み | Noto は 2026-05-19 の J.P. Morgan 会議で、連邦準備のマスター口座にある残高から純金利収益を得ると説明。流動性・信用・デュレーションのリスクは無い(アナリスト記事の言い換え。原文は未閲覧) | https://www.tikr.com/blog/sofi-stock-is-down-32-in-2026-while-building-a-stablecoin-bank-that-the-market-isnt-pricing / T3 |
| 式 | 年間の運用益 = 流通残高 × (連邦準備口座の金利 − 保有者・パートナーへの還元率)。**金利・還元率・パートナーとの分配比率は未取得**。式の感度(算術のみ): 残高 $10 億に利ざや 1% で年 $1,000 万。Q2 末の残高 $3 億 × 1% なら年 $300 万 | 計算 |
| 預金調達コストへの効果 | アナリスト(Kalkine)の見方: 暗号資産取引所や他のステーブルコインに流れる預金を取り込めば、低コストの調達源になりうる。会社の数値ではない | https://kalkine.com/news/financial/sofiusd-stablecoin-2026-inside-the-first-bank-issued-digital-dollar-and-what-it-means-for-deposit-funding-and-fintech-competition / T3 |
| 手数料の見込み | Galileo・STS の手数料収入を強める可能性との分析(定量なし)。パートナー向けの料金表は**未取得** | https://www.webull.com/news/14973644449077248 / T3 |
| 会社の目標残高・収益目標 | **未取得** | — |
| 株価の反応 | 発表後に +16.6%(Börse Express)。TIKR は「市場が値付けしていない」と論じるが、これは見解 | Börse Express(上記)/ TIKR(上記) / T3 |

---

## 取れなかった項目

| # | 項目 | 状況 |
|---|---|---|
| 1 | Q4'25 の総アカウント数 | 未取得(8-K・10-K の Table 6 を見られなかった) |
| 2 | Q1'24 の貢献利益、Q3'24 の貢献利益の公式値 | 未取得(Q3'24 は逆算の約 $33.1M) |
| 3 | Q4'24 の 167.7M と Q1'25 の 158.4M の断絶の原因 | 未解消(定義差の可能性) |
| 4 | Q4'25 の貢献利益 $48M の中身、$18M の解約料の計上四半期 | 未取得。一時要因は仮説 |
| 5 | Chime の S-1 原文、解約料が実際に支払われた確認 | 原本未閲覧。二次情報のみ |
| 6 | 貢献利益率が Q1 → Q2 で下がった理由(費用の内訳) | 未取得 |
| 7 | 2026 年 Tech Platform の通期ガイダンスの更新(Q2 時点)、2027 年の見通し | 未取得。$325M は T4 のみ |
| 8 | 2025〜2026 の銀行・フィンテック・大企業との個別契約(社名・規模)、通信大手の社名、新規 13 社の内訳、パイプラインの数値 | 未取得 |
| 9 | 経営陣の発言の原文(Q1'26・Q2'26 のコール) | 会社公表の原文 PDF の URL は特定したが閲覧できず。英語は要約の言い換え |
| 10 | SoFi Money 以外のシステム(デビット・当座・預金・カード)の移行の時期・進捗・削減額 | 未取得 |
| 11 | Technisys 単体の収益、累計削減額の実績(約束との比較) | 未取得 |
| 12 | SoFiUSD の流通残高の推移(Q1'26、Q3'26)、会社の開示値 | 未取得。$3 億は報道のみ |
| 13 | SoFiUSD の準備資産の構成(現金か短期国債か) | 報道が不一致 |
| 14 | 1 件当たり費用、既存の送金網との比較、削減額の見通し(会社の試算) | 未取得 |
| 15 | SoFi Pay の国際送金の取扱額・件数・手数料表、SoFiUSD を使った送金の実績 | 未取得 |
| 16 | 9 月の Mastercard 決済切替の会社プレスリリース原本、Galileo 顧客の採用 | 未取得。報道のみ |
| 17 | 運用益の金利・還元率・パートナーとの分配、会社の収益目標 | 未取得 |
| 18 | GENIUS 法の法文、利息禁止条項と SoFi の還元設計の整合、OCC 最終規則の内容 | 未確認(利息禁止は私の知識) |
| 19 | 競合のステーブルコインの正確な規模(PYUSD、Circle、JPM Coin) | T4 のみ。一次データ(発行者の証明書、DefiLlama)は未取得 |
| 20 | Peach Finance の買収価格 | 非開示(報道) |
