# CrowdStrike(CRWD)定性調査 — 一次整理(第2版: 再開調査18回で更新)

作成: Sonnet 調査担当 / 評価基準日 2026-10-11 / 取得日 2026-10-11(すべて WebSearch の検索要約経由)

## 0. この文書の読み方と既知の制約

- 役割は事実・出典・「なぜ重要か」の注記の収集であり、評価はしない。出典は Tier で表記する(Tier 1=会社IR・SEC提出書類、Tier 2=公的統計、Tier 3=主要報道・アナリスト・文字起こしサイト、Tier 4=ブログ・個人投稿・集約サイト)。
- **検索要約経由のため、会社IR原文・決算説明会トランスクリプト・SEC書類の本文は1件も精読していない。** 発言は「要約された趣旨」であり、逐語の引用ではない(和訳は要約文の和訳)。逐語が必要な箇所は、各節末の「原文確認先」を開くこと。
- 検索要約同士で数値が食い違う箇所は両論併記し「未確定」とした。単独出典の数値は「単独」と印を付けた。
- **株価の表記**: 2026-07-02 に 4:1 の株式分割が実施された(Investing.com の分割履歴と価格サイトの要約。依頼側メモは 07-01 で、1日の差は未確定)。**分割前の価格・目標株価には「(分割前)」と付し、÷4 した分割後換算値を併記する。** 7月以降の価格は分割後。
- 「欠損」は未取得を意味し、存在しないことを意味しない。定量の四半期データは別担当(`data/CRWD_data.md`)であり、本書では追わない。
- 独自計算には「計算」と明記した(出典の数値ではない)。

用語(初出時): ARR=年間経常収益。NNARR(純新規ARR)=期中のARRの純増額。cRPO=12か月以内に計上予定の残存履行義務。FCF=営業CFから設備投資等を引いた自由に使える現金。調整後(non-GAAP)=SBC(株式報酬)や買収関連費用などを除いた会社定義。EDR=端末(エンドポイント)上の脅威の検知と対応。SIEM=ログを集めて脅威を検知する基盤。SOC=セキュリティ運用センター。SOAR=対応手順の自動化。Falcon Flex=契約時に確保した支出枠を、顧客が追加する Falcon 製品の分だけ引き出していく契約形態(Fal.Con 2026 報道の要約。契約条項の詳細は欠損)。AIDR=AI の検知・対応(AI Detection and Response)。TSR=株主総利回り。

---

## 1. 結論の骨格(分析者への一次整理)

1. **シナリオの骨格**: 会社は「端末(EDR)で入り込み、Falcon Flex の支出枠でクラウド・アイデンティティ・Next-Gen SIEM・露出管理・AI保護のモジュールを顧客内で積み増し、2026年春の『Mythos の瞬間』(後述)で高まった『AIを使うほど守りが要る』需要を AIDR とエージェント型SOCで取り込む」と語っている。その成果指標は NNARR の再加速(FY27 Q2 は前年同期比 +51%)と、長期目標(ARR 100億ドルを FY2030 に前倒し)である。
2. **市場の見方は二分**: 強気は「AI時代に必要性が増す明確な勝者」(Morgan Stanley)、弱気は「売上倍率が部門平均の数倍以上で、完璧さを織り込んでいる」(Berenberg、DZ Bank)。2026-10-09 の終値 275.04ドルは、集計された平均目標株価(256.17ドル、別集計では 235.67ドル)を上回る。
3. **株価は半年で約3倍**: 52週安値 85.68ドルから 275.04ドルへ(計算で約3.2倍)。同じ「Mythos」が3〜4月は株価を押し下げる材料(AIによる代替・脆弱性露出の懸念)だったのに、6〜8月には成長の根拠として語られた。**ナラティブが反転した事実そのものが、市場の仮説の不安定さを示す。**

---

## B. 市場の仮説の出典

### B1. 直近2回の決算説明会でアナリストが繰り返した質問(関心の所在)

| 回 | 質問者 | 質問の内容 | 経営陣の回答の趣旨(要約) | 出典 / Tier |
|---|---|---|---|---|
| FY27 Q2(2026-08-26) | Saket Kalia(Barclays) | 春の「Mythos の瞬間」の後、Q2 の上振れは何が牽引したか | カーツ氏は、クラウド、アイデンティティ、Next-Gen SIEM、露出管理が牽引し、エンドポイントも加速していると回答。この傾向は、顧客がAIを増やしたいが安全性・コンプライアンス・データ保護を要するので持続的、と述べたと要約されている | Investing.com の文字起こし要約(Tier 3)。https://www.investing.com/news/transcripts/earnings-call-transcript-crowdstrike-tops-q2-2027-estimates-shares-jump-10-93CH-4878036 |
| 同上 | Adam Tindle(所属は出典に記載なし) | AIDR をコアのプラットフォームから切り分けてどう見るか | カーツ氏は「AIDR が将来コアのEDR事業を上回りうる」と述べたと要約されている(AI生成の要約。**逐語未確認**) | Yahoo Finance 要約(Tier 3〜4)。https://finance.yahoo.com/technology/ai/articles/crowdstrike-holdings-inc-q2-2027-123000320.html |
| 同上 | (質問者名なし) | Falcon Flex の商業モデル、Next-Gen SIEM、露出管理 | 当四半期の大型案件はすべて Flex 契約。Flex の新規顧客ARRが当期NNARRの34%(記録)という文字起こし抜粋がある(**単独**)。すべての顧客は、データが既にプラットフォームにあるため Next-Gen SIEM を使える状態にある、と要約 | 同上(Tier 3〜4) |
| 同上 | (質問者名なし) | ガイダンスの根拠 | ポドベア氏は、引き上げの根拠として Q3 の過去最高のパイプライン(商談の積み上がり)を挙げたと要約(**逐語の引用は未確認**) | Futunn 経由の智通(Tier 4)、Globe and Mail 文字起こし要約 |
| FY27 Q1(2026-06-03) | (名前なし) | 通期NNARR成長率を引き上げた要因は何か | ポドベア氏は、モジュール採用、継続率、過去最高の Q2 パイプライン、「Mythos の瞬間」を挙げた。AIの追い風は成績にまだ出始めたばかり、と述べたと要約 | Yahoo Finance 要約(Tier 3)。https://finance.yahoo.com/markets/stocks/articles/crowdstrike-holdings-inc-q1-2027-001844681.html |

- **繰り返された関心は3つ**: (1) 上振れの持続性(一過性か構造か)、(2) Flex が新規獲得なのか既存顧客の契約の付け替えなのか、(3) AIDR とエージェント保護が本物の新市場か。
- 重要性の注記: 質問が「持続性」に集まるのは、NNARR の+51% が過去数四半期の再加速の延長線上なのか、2026年春の特需なのかを市場が判別できていないため。
- 原文確認先: Motley Fool Q2 文字起こし https://www.fool.com/earnings/call-transcripts/2026/08/31/crowdstrike-crwd-q2-2027-earnings-call-transcript/ 、Q1 https://www.fool.com/earnings/call-transcripts/2026/06/03/crowdstrike-crwd-q1-2027-earnings-transcript/

### B2. 強気派の主要論点(目標株価は発表時点。分割後換算済みの値のみ)

| 証券会社 / アナリスト | 評価 | 目標株価 | 論拠(出典に書かれている範囲) | 日付 / 出典 / Tier |
|---|---|---|---|---|
| Morgan Stanley | Overweight | 238ドル(227ドルから) | CrowdStrike を「明確な長期的勝者」と評価。詳細な論拠は欠損 | 2026-08(Q2後)。TheStreet(Tier 3)https://www.thestreet.com/investing/stocks/crwd-crowdstrike-stock-price-target-morgan-stanley-august-2026-after-historic-q2-earnings |
| Truist / Junaid Siddiqui | Buy | 245ドル(187.50ドルから) | 決算前の引き上げ。論拠の詳細は欠損 | 2026-08-19。24/7 Wall St.(Tier 3)https://247wallst.com/investing/2026/08/19/crowdstrike-sinks-7-despite-truist-price-target-raise-to-245-palo-alto-networks-falls-5/ |
| RBC Capital | (評価欠損) | 260ドル(256ドルから) | 欠損 | 2026-08-27。Benzinga の一覧を引く daytraders.com(Tier 4)https://daytraders.com/news/2026/08/27/crowdstrike-stock-best-day-ever-analyst-price-targets |
| UBS、Rosenblatt、Scotiabank、Needham | (欠損) | いずれも 250ドル | 欠損。同日に11社が目標を引き上げた | 同上 |
| DA Davidson | (欠損) | 245ドル | 欠損 | 同上 |
| Needham | Buy | 310ドル(250ドルから) | 欠損 | 2026-10-09頃。Stocktwits(Tier 4)、Investing.com 系の集約 |
| StoneX | (欠損) | 325ドル(250ドルから) | 見出しは「AI成長を背景に」 | 2026-10。https://www.investing.com/news/analyst-ratings/stonex-raises-crowdstrike-stock-price-target-to-325-on-ai-growth-93CH-4934841 (Tier 3) |
| BMO | (欠損) | 295ドル(235ドルから) | 欠損 | 2026-10。TipRanks 系の要約(Tier 4) |
| TD Cowen | (欠損) | 280ドル | 見出しは「強い需要を背景に」 | 2026-10。https://www.investing.com/news/analyst-ratings/td-cowen-raises-crowdstrike-stock-price-target-on-strong-demand-93CH-4929295 (Tier 3) |

- 集計: TipRanks の要約で、38人の平均 256.17ドル、最高 425ドル、最低 132ドル(過去3か月)。https://www.tipranks.com/stocks/crwd/forecast (Tier 4)。**別の集計サイトは平均 235.67ドル**(基準株価 272.67ドル、乖離-13.6%)と示し、集計間で食い違う(未確定)。
- 計算: 2026-10-09 終値 275.04ドルは、256.17ドルを約7%、235.67ドルを約17%上回る。**株価が平均目標を上回る状態**であり、目標株価の追随的な引き上げ(10月に Needham、StoneX、BMO、TD Cowen)が続いている。
- 重要性の注記: 目標株価は株価に遅れて動く傾向がある。10月の引き上げは Q2 後の株価上昇を追認したもので、独立した新情報とは限らない。

### B3. 弱気派・慎重派の主要論点

| 出所 | 評価 | 論点 | 日付 / 出典 / Tier |
|---|---|---|---|
| DZ Bank | Sell | 目標 500ドル(分割前。分割後換算 125ドル)。割高なバリュエーション、同業との競争の激しさ、2024年7月の障害が企業の調達に残す影。ある二次出典は当時の EV/売上(企業価値÷売上)を38〜45倍と記載 | 2026-05-19。https://247wallst.com/investing/2026/05/19/dz-bank-just-slapped-crowdstrike-with-a-sell-rating-is-the-700-bull-case-falling-apart/ (Tier 3) |
| Berenberg | Hold(買いから格下げ) | バリュエーション。今後12か月予想の EV/売上が約30倍で、部門平均 5.2倍の約5.6倍(「460%のプレミアム」と表現)。同時に目標株価は 720ドル(分割前。分割後 180ドル)に引き上げ | 2026-06頃(日付は要確認)。https://www.investing.com/news/analyst-ratings/berenberg-downgrades-crowdstrike-stock-rating-to-hold-on-valuation-93CH-4727894 (Tier 3)。別の要約は「後に買いへ戻した」と記すが**単独・未確認** |
| KeyBanc | Sector Weight(中立) | 2026年のセキュリティ予算見通しがより慎重、株価のプレミアムに懸念 | 日付は欠損(検索要約の記述)。Tier 3 |
| Seeking Alpha の寄稿者(個人) | 売り・保有への格下げ | 今後の調整後EPSの約128倍、予想売上の約27倍で「投機的水準」。上昇余地は織り込み済みとの見方 | 日付・株価水準は欠損。https://seekingalpha.com/article/4921215-crowdstrike-valuation-reaching-speculative-levels-despite-ai-tailwinds-downgrade (Tier 4) |
| GuruFocus | (モデル値) | 同社の「GF Value」は 138.02ドルで、2026-10-07 終値 265.44ドルは大幅な割高と判定 | 2026-10-07頃。https://www.gurufocus.com/news/9114130/a-look-at-crowdstrike-holdings-inc-crwd-after-48-decline-gf-value-13802-vs-price-26544 (Tier 4。機械的モデル) |

- 計算(独自): 時価総額 約2,693億ドル(価格サイトの値。第三者提供で近似)÷ 期末ARR 58.4億ドル ≒ **約46倍**。FCF倍率は定量担当に委ねる(欠損)。Berenberg の「30倍」時の株価は分割後換算で約180ドル。2026-10-09 の終値はその約1.5倍で、その間の売上予想の上方修正はそれより小さいと見られるため、**倍率は当時より高い可能性が高い**(この推論は予想売上を確認していないため未検証)。
- 重要性の注記: 弱気派のうち格下げ時の株価は現在より大幅に低い。**それでも「割高」と言っていた**点が、現在の株価水準での議論の出発点になる。
- 弱気の価格シナリオ(参考。Tier 4 の個人モデル): 118ドル(売上倍率の圧縮)、200〜240ドル(成長鈍化と訴訟リスク)。日付と株価基準が混在しており信頼度は低い。

### B4. 空売りレポート・著名な弱気論者

- 空売りレポート: 検索では**確認できなかった**(「存在しない」とは確認していない)。空売り比率は欠損。
- 唯一の「声が大きい」弱気は上記の格付け(DZ Bank の Sell)。

### B5. 報道のナラティブ(2026年のAI代替懸念)

| 日付 | 出来事 | 出典 / Tier |
|---|---|---|
| 2026-01 | ソフトウェアETF(IGV)が約15%下落し、2008年以来最悪の月 | Axios https://www.axios.com/2026/02/03/ai-software-anthropic-stock-market (Tier 3) |
| 2026-02-23 | Anthropic の新しいAIセキュリティツールを受けて、CrowdStrike と Zscaler が各約10%下落。カーツ氏は競争上の堀を擁護 | CNBC https://www.cnbc.com/2026/02/23/cybersecurity-stocks-anthropic-ai-crowdstrike.html (Tier 3) |
| 2026-02-24 | Anthropic が提携を発表し、ソフトウェア株は反発 | CNBC https://www.cnbc.com/2026/02/24/software-stocks-anthropic-ai.html (Tier 3) |
| 2026-03-27 | Anthropic が強力な新モデル「Mythos」を試験中との報道。iShares サイバーセキュリティETFが-4.5%、CRWD・PANW・ZS が各約-6% | CNBC https://www.cnbc.com/2026/03/27/anthropic-cybersecurity-stocks-ai-mythos.html (Tier 3) |
| 2026-04-09 | Mythos を広く公開しない方針(隠れた脆弱性を暴く懸念)。Cloudflare、Okta、CrowdStrike、SentinelOne が-4.9〜-6.5% | CNBC/Yahoo の要約(Tier 3) |
| 2026-04 | S&P 500 ソフトウェア・サービス指数が年初来-25.5%(ロイター) | Yahoo Finance の要約(Tier 3) |
| 2026-06以降 | 会社は Mythos を「需要拡大の転換点」と位置づけ(「Mythos の瞬間」)、株価も反発 | Q1/Q2 説明会の要約(上記) |

- 繰り返された見出しの言葉: 「AIによる破壊」「ソフトウェアの物語が崩れる」「(AIモデルが)脆弱性を暴く」。
- 反論側: Wedbush は「売りは行き過ぎ」と評価(2026-02、Tier 3)。
- 重要性の注記: セキュリティ株が AI代替懸念で売られる論理は「AIが脅威検知を代替する」だが、会社と強気派の論理は「AIが攻撃を増やし、防御の需要を増やす」。**同一の事象が両方向に解釈されている**ため、どちらの機構が数字に先に出るかが論点になる。

### B6. 株価推移の要点(分割後換算、直近約1年)

| 日付 | 出来事 | 出典 / Tier |
|---|---|---|
| 2025-09-18 | Investor Day で長期目標(FY2031にARR100億ドル)。株価は約+13% | CNBC https://www.cnbc.com/2025/09/18/crowdstrike-investor-day-stock.html (Tier 3) |
| 2026-02〜04 | 上記のAI代替懸念で下落。52週安値は 85.68ドル(日付欠損) | GuruFocus(Tier 4) |
| 2026-03-03 | Q4 FY26 発表。時間外で約-4%(分割前 368.99ドル、換算 約92ドル) | Investing.com(Tier 3) |
| 2026-06-03 | Q1 FY27 発表。「予想を上回るが株価は下落」の見出し | Investing.com(Tier 3) |
| 2026-06 | 分割前 667〜754ドル(換算 約167〜189ドル)でインサイダー売却が申告される | SEC Form 4(Tier 1。後述 G) |
| 2026-07-02 | 4:1 の株式分割 | Investing.com 分割履歴(Tier 3) |
| 2026-08-19 | 決算前に-7%(Palo Alto も-5%)。Truist は目標を引き上げたが下落 | 24/7 Wall St.(Tier 3)。原因は見出しからは不明 |
| 2026-08-27 | Q2 発表の翌日、早朝取引で最大+19.7%。「最高の日」と報道 | Motley Fool、daytraders.com(Tier 3〜4)。終値の騰落率は欠損 |
| 2026-10-07 | -4.8% で終値 265.44ドル(会社IRの過去価格照会に同値) | GuruFocus、ir.crowdstrike.com(Tier 1 を要約経由で確認) |
| 2026-10-08 | 終値 263.01ドル | heygotrade(Tier 4) |
| **2026-10-09** | **終値 275.04ドル(+12.03ドル、+4.57%)** | heygotrade、CNBC 相場ページ(Tier 3〜4)。52週レンジ 85.68〜286.99ドル |

- 計算: 3/3 の換算価格(約92ドル)から 10/9 の終値まで約3.0倍。

---

## A. 経営陣シナリオの一次情報

### A1. 経営陣の発言(FY27 Q2、2026-08-26)—要約の和訳

以下は文字起こしの**要約**であり、逐語ではない。
- カーツ氏は説明会の冒頭で、「Mythos の瞬間」(原文ママ)から数週間の期間と位置づけ、サイバーセキュリティの転換点と述べた(Webull の文字起こし要約、Tier 4)。https://www.webull.com/news/15474227996476416
- 「AIエージェントが市場の新たな敵対者になった」(roic.ai の文字起こし要約、Tier 3〜4)。エージェントが暴走する事例に触れ、AIDR は好調だったと述べた。
- Q2 を「会社史上最高の四半期」と表現(複数の要約が一致、Tier 3)。
- Flex が成長の中核。51%の顧客が6モジュール以上を採用(Futunn 見出し、Tier 4。**母数の定義が未確認**)。https://news.futunn.com/en/th/post/78352303/crowdstrike-q2-earnings-call-the-mythos-moment-for-ai-is
- Q3 の期末ARRガイダンスは 61.84〜61.88億ドル(前年同期比+26%)(Globe and Mail の文字起こし、Tier 3)。
- 原文確認先: roic.ai https://www.roic.ai/quote/CRWD/transcripts/2027-year/2-quarter 、Globe and Mail https://www.theglobeandmail.com/investing/markets/stocks/CRWD/pressreleases/4355978/crowdstrike-crwd-q2-2027-earnings-call-transcript/

### A2. 数値目標とその定義・期限

| 時期 | 目標 | 出典 / Tier |
|---|---|---|
| 2025-09-18 Investor Day | ARR 100億ドルを FY2031(2031年1月期)までに、200億ドルを FY2036 までに。FY2029 に営業利益率 28〜32%、FCFマージン 34〜38% | CNBC https://www.cnbc.com/2025/09/18/crowdstrike-looks-out-10-years-at-its-investor-day-and-the-cybersecurity-stock-soared.html (Tier 3)。利益率の定義(non-GAAP か)は**未確認** |
| 2026-09 Fal.Con 投資家向け説明(ポドベア氏) | **100億ドルを FY2030 に前倒し、200億ドルを FY2035 に前倒し**。200億ドルの約30%に到達済み。AIセキュリティの市場規模を2034年に2,150億ドルと主張 | Investing.com https://www.investing.com/news/transcripts/crowdstrike-at-falcon-investor-briefing-ai-push-lifts-growth-outlook-93CH-4886858 (Tier 3)。同説明で利益率目標が更新されたかは**欠損** |
| FY2027 通期 NNARR | 成長率ガイダンス 22.5%(期初)→27.7%(Q1で+520bp)→34.0%(Q2で+630bp)。中央値は 13.55億ドル(レンジ 13.50〜13.59億ドル) | 会社IR(Tier 1 を要約経由で確認)。期初は Q4 FY26 発表時に 12.13〜12.64億ドル(前年比+20〜25%) |

- ARR の定義(10-K の要約): 12か月以内に失効する契約は、既存条件で更新されるものと仮定してARRに含める。更新交渉中の失効済み契約の売上も、交渉が続く間はARRに残る。重要性の注記: **ARR は更新の失敗を遅れて反映する定義**であり、継続率の確認には別指標が要る。
- 計算(独自): FY2026 期末ARR 52.5億ドルから FY2030 末に 100億ドルへは、年率約17.5%の成長でよい。FY2031 目標なら約13.8%、FY2035 の200億ドルは約16.0%。**足元のARR成長(+25%前後)より低い**(E5で扱う)。
- 計算(独自): ガイダンスの内訳から逆算した Q4 FY27 NNARR は約 4.21億ドル(13.55 − Q1 2.56 − Q2 3.33 − Q3 3.45)。前年同期の 3.31億ドルに対し約+27%。Q3 は約3.45億ドルで、逆算した前年同期 約2.65億ドルに対し約+30%。**H2 の成長率は、Q2 の+51% より低く置かれている。**

### A3. ピース一覧

| ピース | 目的(会社の説明) | 発表日・規模 | 進捗を示す数値 | 出典 / Tier |
|---|---|---|---|---|
| **Falcon Flex** | 支出枠を先に確保し、顧客が Falcon 製品を追加するたびに引き出す | 開始時期は欠損 | Flex 採用顧客のARR: Q4 FY26 16.9億ドル(**単独**、swotpal、Tier 4)→Q1 FY27 19億ドル超(+99%、Flex口座の四半期純増300社超)→Q2 22.9億ドル超(+101%)。全社ARRに占める割合は 約32%→約34%→約39%(計算) | Fool の Q1 文字起こし(Tier 3)、会社IR(Q2) |
| Flex for Services | サービス契約の消費型。プラットフォーム契約とは独立 | 2026-03(日付欠損) | 欠損 | CrowdStrike プレスリリース(Tier 1)https://www.crowdstrike.com/en-us/press-releases/crowdstrike-launches-flex-for-services-bringing-flexible-cybersecurity-services-consumption-to-the-agentic-era/ |
| **SGNL**(アイデンティティ) | 継続的で文脈に応じた認可。「常時の特権を持たせない」 | 発表 2026-01-08、完了 2026-02-20。見出し価格 7.4億ドル | 10-K: 現金 6.279億ドル(取得現金 940万ドル控除後)+代替株式報酬の公正価値 890万ドル。**見出しの7.4億ドルとの差は出典内で説明なし** | CNBC https://www.cnbc.com/2026/01/08/crowdstrike-ai-cybersecurity-sgnl-acquisition.html 、10-K(Tier 1) |
| **Seraphic**(ブラウザ保護) | ブラウザ内のランタイム保護を Falcon に追加 | 完了 2026-02-03。約4.2億ドル | 欠損 | SecurityWeek https://www.securityweek.com/crowdstrike-to-acquire-browser-security-firm-seraphic-for-420-million/ 、10-K |
| **Pangea**(AIアプリ保護) | 生成AIアプリのガードレール | 2.6億ドル(Yahoo Finance、Tier 3。発表日は欠損) | AIDR との関係は**未確認**。AIDR のARRは Q1 で前期比+250%超、Q2 でほぼ3倍 | Yahoo Finance |
| **Onum**(データパイプライン) | Next-Gen SIEM へのデータ取り込み(「ネットワークデータ・インテリジェンス」) | 2.9億ドル(Yahoo Finance)。発表日は欠損 | 欠損 | 同上、8-K(2026-04-16)の要約 |
| **Adaptive Shield**(SaaS保護) | SaaS の設定不備・体制の管理 | 約3億ドル(推定のみ。公式価格は未確認、Tier 4)。2024年 | 欠損 | Richmond Advisory(Tier 4) |
| **Charlotte AI** | 生成AIの助手→エージェント型SOC | 2026-09-02: 資格を満たすモジュールの契約者に「月次クレジット付きの標準権利」として提供。高度機能(エージェント型の検知選別・対応)は有料のCharlotte AIモジュールのまま | 顧客数・ARRは欠損 | SiliconANGLE https://siliconangle.com/2026/09/02/crowdstrike-gives-ai-agents-an-identity-provider-parallel-soc-investigations-and-package-blocking/ (Tier 3) |
| Fal.Con 2026 の新製品 | AIエージェントの保護と運用 | SafeMind、Falcon Guardian、Agentic Identity Provider(AIエージェント用のID基盤)を発表 | 欠損 | Investing.com(Tier 3)、SiliconANGLE |

- 買収4件(Pangea、Onum、SGNL、Seraphic)の見出し価格合計: 約17.1億ドル(計算。Adaptive Shield の推定約3億ドルを足すと約20億ドル)。重要性の注記: 買収の対価の大半は現金だが、SBC・株数への影響は欠損。
- **CCP(2024年7月障害後の顧客支援パッケージ)の設計と終了時期、AWS・Google・NVIDIA 等の提携、資本政策(自社株買い・負債)は、今回の検索では取得できなかった。欠損。**
- 注: 依頼文の買収先4社のうち、SGNL・Pangea・Onum・Adaptive Shield は確認。**Seraphic は依頼文になかったが出典で確認した追加分。**

### A4. ガイダンス達成状況・過去の約束

- 直近(FY27)のNNARR成長率ガイダンスは、期初の 22.5%から 34.0%へ2回上方修正された(合計 +11.5ポイント)。Q2 のNNARRはガイダンス上限を 4,500万ドル超えた。会社は**期初を低めに置き、四半期ごとに引き上げている**。
- FY2026: NNARR は通期で過去最高の 10.1億ドル(初の10億ドル超)。Q4 FY26 は 3.31億ドル(+47%)、期末ARR 52.5億ドル(+24%)、売上 13.1億ドル(+23%)(会社IR、Tier 1 を要約経由で確認)。
- **FY2024〜FY2025 の期初ガイダンスと実績の比較、および「下期のNNARR再加速」の約束とその結果は、取得できなかった。欠損。** 間接的には FY26 Q4 の NNARR が+47% であり、再加速は数字に出ている。
- 重要性の注記: ガイダンスの保守性(期初低め)が3四半期連続の「上振れ」を作る構造なら、上振れ自体は先行指標としての情報価値が小さい。ただし FY2024〜25 の比較が欠損なので判断不能。

### A5. 経営陣の経歴・在任・報酬

- CEO ジョージ・カーツ、CFO バート・ポドベア。マイケル・セントナス氏(役職は出典の要約に記載なし)。経歴・在任年数・交代は**欠損**。
- 報酬(2026 年の PRE 14A、Tier 1 を要約経由で確認): FY2026 の基本給はカーツ氏 110万ドル(従来100万ドル)、セントナス氏 87.5万ドル、ポドベア氏 70万ドル。カーツ氏は 2025年12月に**相対TSR(他社比の株主総利回り)に連動する業績連動株式**を付与された。セントナス氏には、株価の相対的な優位と「ARR200億ドル」の構想に連動する特別な付与が取締役会で承認された(8-K)。
- 年次報酬で使う指標の種類は non-GAAP 指標という以外は**欠損**。NNARR や FCF が KPI かどうかは未確認。
- 重要性の注記: TSR は1株当たりの収益率を測る単位であり、総額の指標(総ARR・総利益)より1株当たり価値と整合しやすい。ただし対象の報酬に占める割合は欠損。
- 出典: https://www.sec.gov/Archives/edgar/data/1535527/000110465926046009/tm2532333-1_pre14a.htm

---

## C. 一次情報(スカットルバット)

| # | 観察 | 内容 | 出典 / Tier | 独立性 |
|---|---|---|---|---|
| C1 | Falcon Flex の契約実態 | Flex は確保した支出枠から製品追加時に引き出す形。Q2 の大型案件はすべて Flex。Flex 新規顧客のARRが当期NNARRの34%(**単独**)。Flex 採用顧客のARRの四半期増加分(約3.9億ドル。Q1 の「19億ドル超」を下限として計算)は、当期の全社NNARR(3.33億ドル)を**上回る**ので、増加分の一部は既存ARRが Flex 口座に付け替わった結果と推定される | Fal.Con 報道(Tier 3)、会社IR、上記計算 | 会社開示の再掲。独立ではない |
| C2 | Gartner マジック・クアドラント(エンドポイント保護) | 2026年版(2026-05-26付)でCrowdStrikeはリーダー(連続7回目、会社ブログの記載)。Trend もリーダー。Bitdefender はビジョナリー。SentinelOne の位置は要約に記載なし | https://www.crowdstrike.com/en-us/blog/crowdstrike-leader-in-2026-gartner-magic-quadrant-for-endpoint-protection/ (ベンダー発信、Tier 4)。**Gartner原文で確認が必要** | 独立(評価者はGartner)だが転載はベンダー |
| C3 | Gartner Peer Insights(利用者レビュー) | エンドポイント保護部門で CrowdStrike Falcon、Sophos、SentinelOne が最高評価の群に入る。点数は欠損 | https://www.gartner.com/reviews/market/endpoint-protection-platforms (Tier 3) | 独立(顧客) |
| C4 | Delta 航空の訴訟 | 2025-05、ジョージア州フルトン郡上級裁判所(エラービー判事)は、故意の虚偽表示・不告知による詐欺の主張を除き、過失とコンピュータ侵入の主張を継続させた。Delta は損失を約5億ドル(収益減3.8億ドル+費用1.7億ドル)と主張。会社側は、契約上の上限により賠償は個位数百万ドルにとどまるか、無効と見込む。**2026年の判断・和解は検索で見つからず** | The Register https://www.theregister.com/security/2025/05/21/deltas-lawsuit-against-crowdstrike-given-go-ahead/273034 、Transportation Today(Tier 3) | 独立 |
| C5 | 乗客の集団訴訟(連邦) | 一部は棄却、契約違反(払い戻し不履行)やモントリオール条約違反は継続 | BankInfoSecurity(Tier 3) | 独立 |
| C6 | 障害後の顧客離脱 | 離脱率・総継続率(GRR)は**欠損**。間接証拠: 期末ARR+25%、NNARR過去最高 | — | — |

- 最低3件の一次情報の要件: **独立した一次情報として確保できたのは C2、C3、C4 の3件(いずれも市場のナラティブを補強する弱い裏付け)。求人動向、チャネルの声、競合(SentinelOne、Microsoft、Palo Alto)の発言、MITRE 評価、IDC のシェアは今回取得できなかった。欠損。**
- 重要性の注記: 最大の構造仮説(Flex が純増ではなく付け替えを含む)を裏付ける独立した一次情報は未取得。C1 は会社開示からの推論にとどまる。

---

## D. 競争と業界の構造【大半が欠損】

- エンドポイント: Gartner MQ でリーダーの群(Trend、CrowdStrike 等)。市場成熟度、シェアは欠損(IDC 未取得)。
- SIEM: カーツ氏は「すべての顧客は Next-Gen SIEM を使える状態にある」と述べたと要約された。Splunk からの置き換え件数・ARRは欠損。
- Microsoft のバンドル圧力: 検索では弱気の論拠として確認できなかった(DZ Bank は「同業との競争の激しさ」と記すのみ)。
- セキュリティ予算: KeyBanc が「2026年は予算見通しがより慎重」と評価(日付欠損)。Gartner の支出予測は欠損。
- AIエージェント時代の新市場: 会社は AIセキュリティの市場規模を 2034 年に 2,150 億ドルと主張(Investing.com の Fal.Con 要約、会社の主張。第三者の裏付けなし)。

---

## E. 異常値の候補(市場のナラティブと合わない数字。答えは未調査)

| # | 異常値の候補 | なぜこの数字なのか(問い) |
|---|---|---|
| E1 | NNARR +51%(Q2)に対し売上+26%・期末ARR+25%超 | NNARR の伸びのうち、新規顧客・追加モジュール・Flex への付け替え・CCP 終了の影響は何割か |
| E2 | Flex 採用顧客のARR(22.9億ドル、+101%、全社ARRの約39%)の四半期増加が全社NNARRを上回る | 倍増の何割が新規の消費で、何割が既存契約の Flex への付け替えか。付け替えなら純増はどれだけか |
| E3 | 営業CF 5.30億ドルに対し FCF 3.77億ドル(差は営業CFの約29%) | 差は設備投資・資本化ソフト・リース返済のどれか |
| E4 | 調整後営業利益 3.716億ドル(前年同期 2.550億ドル、**+46%**)が売上+26%を大きく上回る | 利益率の拡大のうち、SBC を除外した部分と実体の効率化の部分はどれだけか(SBC額は欠損) |
| E5 | 長期目標(ARR 100億ドルを FY2030)が示す必要成長率は年約17.5%で、足元のARR成長(+25%前後)より低い。一方で株価は ARR の約46倍 | 目標は意図的に保守的か。それとも会社は成長の鈍化(ARRが大きくなる効果)を織り込んでいるのか |
| E6 | 通期ガイダンスが逆算で Q4 NNARR 約+27%(Q2 は+51%)と、H2 の成長率を Q2 より低く置く | 保守的なガイダンスか、前年Q4(+47%)の高い比較基準か、Q2 の一部が一時的な要因か |
| E7 | SGNL の見出し価格 7.4億ドルと、10-K の現金対価 約6.28億ドルの差 | 差額は繰延・業績連動の対価か。株数や費用化に影響するか |
| E8 | 株価が平均目標株価(256ドル、別集計で236ドル)を上回る | 目標株価が株価を追随しているだけか。独立した新情報はあるのか |

---

## F. 条件9(AIの停めない運用)に関わる事実

- **AIを守る製品**: AIDR(AIの検知・対応)。ARRは Q1 で前期比+250%超(Q2 のパイプラインが 5,000万ドル超という記載もあるが、AIDR のものか**未確認**)、Q2 でほぼ3倍(いずれも成長率のみ。**金額は欠損**)。カーツ氏は「AIDR が将来コアのEDRを上回りうる」と発言(要約、逐語未確認)。Fal.Con 2026 で SafeMind、Falcon Guardian、Agentic Identity Provider を発表。Pangea(AIアプリのガードレール、2.6億ドル)を取得。
- **AIで動く製品**: Charlotte AI。エージェント型SOC(複数エージェントが端末・ID・SaaS・クラウド・ネットワークを並行調査)、Charlotte Agentic SOAR、AgentWorks、Falcon Foundry。人の承認が要る段階から完全自律までを、手順ごとに設定できる。第三者エージェントは MCP(AIエージェントとツールをつなぐ標準規格)で双方向に接続。Charlotte AI は資格のあるモジュールの契約者に月次クレジットを付与(標準権利化)。https://www.crowdstrike.com/en-us/press-releases/crowdstrike-unveils-next-evolution-of-the-agentic-soc/ (Tier 1)
- 顧客数・利用社数・Charlotte AI の売上は**欠損**。条件9の関与度合いと売上規模は判定不能。
- 重要性の注記: Charlotte AI を標準権利にしたことは、AI機能を別売ではなく Flex・モジュール採用の促進に使う設計と読めるが、その解釈は出典になく**推測**。

---

## G. リスク事象

| 事象 | 内容 | 出典 / Tier |
|---|---|---|
| 2024年障害の訴訟 | Delta(C4)と乗客集団訴訟(C5)が継続。2026年の進展は取得できず | 上記 |
| AI代替・脆弱性露出のイベントリスク | 2026-02〜04に4回、1日で5〜10%下落。会社は後に需要の追い風と位置づけたが、下落機構は消えていない | B5 |
| 経営陣の株式売却 | SEC Form 4 に、2026年6月(分割前 667〜754ドル)、8月(212〜220ドル、8月3日は193〜203ドル)、9月21日(238〜250ドル)の市場売却が申告されている。**売り手(誰か)、株数、10b5-1(事前計画売却)の有無は取得できず**。カーツ氏、ポドベア氏、セントナス氏の売却かは未確認 | SEC EDGAR の Form 4 一覧(Tier 1)https://www.sec.gov/Archives/edgar/data/0001535527/000177856426000168/form4-09222026_080903.xml ほか |
| 会計上の論点 | ARRの定義(失効契約を更新とみなす)。SGNL の対価の内訳。SBC・GAAP数値は欠損 | 10-K(Tier 1 を要約経由) |
| 規制 | 検索では確認できず。欠損 | — |
| 再障害 | 欠損(検索せず) | — |

---

## 付録1. 取得できなかった項目(次の検索があれば優先)

1. Q3・Q4 FY26 と Q1 FY27 の説明会のアナリスト質問(質問者名)と経営陣の逐語。Q2 のトランスクリプト原文(Fool/roic.ai)。
2. CCP(顧客支援パッケージ)の設計・終了時期・FY27 NNARR への影響。
3. AWS・Google・NVIDIA 等の提携、資本政策(自社株買い・負債・転換社債)。
4. 過去3年の期初ガイダンスと実績。「下期再加速」の約束の原文。
5. 委任状説明書(最終版 DEF 14A)の報酬KPI、セントナス氏の役職、経営陣の経歴。
6. 空売りレポート、空売り比率。
7. IDC のシェア、MITRE 評価、求人、チャネルの声、Microsoft・SentinelOne・Palo Alto の CRWD への言及。
8. 経営陣の株式売却の売り手・株数・計画の有無(個別の Form 4 の本文)。
9. Gartner のセキュリティ支出予測。
10. Q2 の GAAP 損益・SBC・RPO(定量担当が `data/CRWD_data.md` に記載予定)。

## 付録2. 主な出典URL一覧(取得日 2026-10-11)

- 会社IR Q2 FY27: https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-reports-second-quarter-fiscal-year-2027-financial
- 会社IR Q1 FY27: https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-reports-first-quarter-fiscal-year-2027-financial
- 会社IR Q4 FY26: https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-reports-fourth-quarter-and-fiscal-year-2026
- 8-K(Q2 FY27 決算): https://www.sec.gov/Archives/edgar/data/0001535527/000153552726000029/crwd-20260826xex991.htm
- 10-K FY2026: https://www.sec.gov/Archives/edgar/data/1535527/000153552726000010/crwd-20260131.htm
- 会社IR 過去価格照会: https://ir.crowdstrike.com/stock/historical-price-lookup
- 株価・分割: https://www.heygotrade.com/en/us-stock/crwd/ 、https://www.investing.com/equities/crowdstrike-holdings-inc-historical-data-splits
- Fal.Con 投資家向け説明: https://www.investing.com/news/transcripts/crowdstrike-at-falcon-investor-briefing-ai-push-lifts-growth-outlook-93CH-4886858
