# サイバーセキュリティ業界の構造と動向(定性調査)

評価基準日: 2026-10-11 / 作成: Sonnet 調査担当 / 状態: **未完了(WebSearch の予算枯渇により、出典付きの事実を1件も取得できていない)**

## 0. 本書の状態と、なぜこうなったか

- **結論**: 本書には出典付きの数値が1つもない。8節すべてが「欠損」である。
- **原因(2層)**:
  1. 検索ツールが「1ターンあたり WebSearch 200回(全エージェント共有)の予算を使い切った」として、最初の4件の検索(Gartner 2026 支出予測、Gartner 2027 予測、IDC 支出ガイド、Google の Wiz 買収の完了状況)をすべて実行せずに拒否した。
  2. 統括の指示と共通基準 §2 は WebSearch 以外の取得手段(WebFetch・curl)を禁じ、検索結果の要約を迂回する手段(curl での検索エンジン照会、第三者の読み取り・中継・アーカイブ経由の取得)は拒否メッセージ自体が禁じている。このため、取得を迂回する選択肢はない。
- **訓練知識で埋めなかった理由**: 共通基準 §2「数値を推測で埋めない」と research-protocol §2「最新の決算・株価・ガイダンスは必ずWeb検索で取得する(訓練知識のまま書かない)」に従った。評価基準日(2026-10-11)は私の知識の期限(2026年6月)より後であり、2026年後半の事象(ブラックハット後の上昇、各社の最新決算、買収の完了状況)は記憶では確認できない。
- **未確認の既存資料**: `research/`、`data/`、`analysis/` はいずれも空で、他の担当者が取得済みの情報の流用もできなかった(2026-10-11 時点で確認)。
- **再開の条件**: 検索予算が復活したら(利用者が追加メッセージを送るか、環境変数 `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` を引き上げる)、下の各節の「再実行用クエリ」をそのまま実行すれば埋められる。節の表の枠は用意してある。

## 記録様式(再開時に使う)

各数値は次の形で書く。Tier は research-protocol §2 に従う(1=会社開示、2=公的統計・業界団体、3=主要報道・アナリスト、4=ブログ・SNS・空売りレポート)。

| 項目 | 数値 | 単位・期間 | 出典名 | 出典URL | 出典日 | 取得日 | Tier | 備考(単独出典・推定・食い違い) |
|---|---|---|---|---|---|---|---|---|

Gartner・IDC は調査会社の発表で Tier 3 に当たる。ただし、同社のプレスリリース(gartner.com/en/newsroom)は発表主体の一次資料なので、Tier 3 のうち最上位として扱い、備考に「調査会社の一次発表」と書く。

## 1. 市場規模と成長 — 欠損

- 取得できたもの: なし。
- 欲しいデータ:
  - Gartner の世界の情報セキュリティ(information security)エンドユーザー支出予測: 2025・2026・2027年の総額、前年比、セグメント別(ネットワークセキュリティ、エンドポイント保護、クラウドセキュリティ、アイデンティティ・アクセス管理、セキュリティ運用(SecOps)・SIEM、データセキュリティ、セキュリティサービス)。
  - IDC の Worldwide Security Spending Guide(世界のセキュリティ支出予測)。
  - IT予算全体に占めるセキュリティの比率(Gartner の IT 支出予測、Gartner/IDC の CIO 調査、または業界団体の調査)。
- 再実行用クエリ(いずれも `allowed_domains` に `gartner.com` を付けた版と付けない版を試す):
  - `Gartner forecasts worldwide end-user spending on information security 2026`
  - `Gartner information security spending 2027 forecast segment`
  - `IDC Worldwide Security Spending Guide 2026 forecast`
  - `security spending percent of IT budget 2026 survey`
- 注意: Gartner は年に複数回、予測を改訂する。複数版が見つかったら、発表日の新しい版を採り、旧版との差を備考に残す。

## 2. セグメント別の利益プール — 欠損

- 取得できたもの: なし。
- 欲しいデータ:
  - 6セグメント(ファイアウォール、SASE/SSE、EDR/XDR、SIEM、IAM、CDN/WAF)の市場規模と成長率(IDC、Gartner、Dell'Oro、Omdia など。Dell'Oro はファイアウォールと SASE の追跡で知られる)。
  - 代表企業の粗利率と営業利益率(GAAP と non-GAAP を分けて書く): 直近の四半期・年度の会社開示(Tier 1)から。
    - ファイアウォール: Palo Alto Networks、Fortinet、Check Point(参照用)
    - SASE/SSE: Zscaler、Netskope、Palo Alto(Prisma)、Cloudflare
    - EDR/XDR: CrowdStrike、SentinelOne、Microsoft
    - SIEM: Splunk(Cisco)、Microsoft Sentinel、Google SecOps
    - IAM: Okta、Microsoft Entra、CyberArk(Palo Alto による買収後は開示が変わる点に注意)、Ping Identity(非上場)
    - CDN/WAF: Cloudflare、Akamai
- 再実行用クエリ:
  - `Gartner Magic Quadrant market share firewall SASE 2025 Dell'Oro`
  - `Dell'Oro network security market 2026 firewall SASE revenue growth`
  - `Fortinet gross margin operating margin Q2 2026 results`(各社について繰り返す。会社IRの決算発表を `allowed_domains` で指定: investor.fortinet.com、investors.paloaltonetworks.com、ir.crowdstrike.com、ir.zscaler.com、investors.okta.com、cloudflare.net)

## 3. 統合(プラットフォーム化)とM&A — 欠損

- 取得できたもの: なし(金額・完了日・出典の確認はゼロ)。
- 調査対象の案件名(**検索の手がかりとして書いたもので、事実としての確認はない**。金額・完了日・状態はすべて要検索):
  - Google による Wiz の買収(完了状況、金額、規制当局の承認)
  - Palo Alto Networks による CyberArk、Chronosphere、Protect AI の買収(各社の完了日と対価)
  - Cisco による Splunk の買収(完了日)
  - CrowdStrike の買収(Onum、Pangea、SGNL 等を含む。2025〜2026年に発表されたものすべて)
  - Zscaler による Red Canary の買収
  - ServiceNow による Armis の買収
  - その他: 2024〜2026年に発表された10億ドル超のセキュリティ買収(Thoma Bravo など投資ファンドによる非公開化を含む)
- 顧客のベンダー数削減の調査データ: Gartner の「ベンダー統合」調査、Palo Alto・CrowdStrike・Zscaler の決算説明でのプラットフォーム化の説明、アナリスト調査(例: 顧客がセキュリティベンダー数を減らす意向の比率)。
- 再実行用クエリ:
  - `Google completes acquisition of Wiz` / `Wiz acquisition closed 2026 price`
  - `Palo Alto Networks completes acquisition CyberArk` / `Palo Alto Networks Chronosphere acquisition completed` / `Palo Alto Networks Protect AI acquisition`
  - `CrowdStrike announces acquisition 2026` / `CrowdStrike to acquire 2025`
  - `Zscaler completes acquisition Red Canary`
  - `ServiceNow Armis acquisition completed`
  - `cybersecurity M&A 2026 largest deals first half`
  - `security vendor consolidation survey 2026 percent organizations reduce vendors`

## 4. Microsoft のセキュリティ事業 — 欠損

- 取得できたもの: なし。
- 欲しいデータ:
  - セキュリティ事業の年間売上の開示(年間200億ドル超という開示があるかの確認、時期と文言)。決算説明・株主向け書簡・Microsoft Secure 等のイベントの発表。
  - E5(Microsoft 365 E5。Defender・Entra・Purview・Sentinel を束ねた上位ライセンス)の価格改定、採用率、バンドル戦略の動き。
  - Defender(エンドポイント・クラウド)、Entra(アイデンティティ)、Sentinel(SIEM)の成長率・顧客数の開示。
  - 専業ベンダー(CrowdStrike、Okta、Zscaler、SentinelOne 等)への影響に関する報道・アナリスト調査・顧客調査(「Microsoft への置き換え」「価格圧力」の論調)。
- 再実行用クエリ:
  - `Microsoft security business annual revenue $20 billion earnings call`
  - `Microsoft E5 security bundle impact CrowdStrike Okta Zscaler analyst`
  - `Microsoft Defender Sentinel Entra growth fiscal 2026 fourth quarter`
  - `Microsoft Sentinel data lake SIEM pricing competition Splunk`

## 5. AIの影響(両方向) — 欠損

### 5(a) AIエージェント・生成AIアプリのセキュリティという新市場 — 欠損
- 欲しいデータ: 市場規模予測(Gartner の "AI security" / "AI TRiSM"〔AI の信頼・リスク・セキュリティ管理〕予測など)、主要製品(Palo Alto の Prisma AIRS、CrowdStrike の AI 関連製品、Zscaler の AI セキュリティ、Cloudflare の AI Gateway・Firewall for AI など、各社の発表で確認すること)、関連の新興企業と買収。
- クエリ: `AI security market size forecast 2026 2030`、`Gartner AI TRiSM spending forecast`、`AI agent security product launch 2026 Palo Alto CrowdStrike Zscaler Cloudflare`

### 5(b) 攻撃側のAI活用による脅威の増加 — 欠損
- 欲しいデータ: CrowdStrike Global Threat Report、Verizon DBIR(データ侵害調査報告)、Mandiant M-Trends、IBM のデータ侵害コスト調査、Anthropic・OpenAI・Google の脅威レポートなど、AI を使った攻撃の増加を示す統計(Tier 1〜3)。
- クエリ: `AI-powered cyberattacks increase 2026 report statistics`、`CrowdStrike Global Threat Report 2026 AI`、`Verizon DBIR 2026 AI`、`Mandiant M-Trends 2026`

### 5(c) 「AIがSaaSを代替する」懸念によるソフトウェア株の下落(いわゆる SaaSpocalypse)とセキュリティ株の値動きの対比 — 欠損
- 欲しいデータ: 下落の時期・幅(IGV〔ソフトウェアETF〕等の騰落)、きっかけとなった出来事、セキュリティ株(CRWD・PANW・ZS・NET・FTNT・OKTA)の同期間の騰落。一般ソフトウェア株と対比して、どのセキュリティ銘柄が売られ、どれが耐えたか。
- クエリ: `SaaSpocalypse software stocks selloff AI 2026`、`software stocks AI disruption fears cybersecurity stocks performance 2026`、`IGV vs CIBR 2026 year to date`

### 5(d) AIによるSOC自動化が人員課金・シート課金に与える影響の論調 — 欠損
- 欲しいデータ: SOC(セキュリティ運用センター)の AI 自動化(Charlotte AI、Cortex AgentiX、Google の SecOps エージェント、Microsoft Security Copilot 等)の論調。課金モデル(ユーザー数課金〔シート課金〕から、利用量・成果ベースへの移行)に関する、会社発言とアナリスト分析。Okta のように人(ユーザー)に課金する会社への影響が焦点。
- クエリ: `AI SOC automation seat-based pricing impact cybersecurity vendors analyst`、`agentic SOC pricing model consumption outcome-based 2026`

## 6. 株価とバリュエーションの状況 — 欠損

- 取得できたもの: なし。
- 欲しいデータ:
  - 2026年のサイバーセキュリティ ETF(CIBR、HACK、BUG)の年初来騰落と、2026-10-09 時点の水準。S&P 500、IGV(ソフトウェア)との比較。
  - セクターの株価売上倍率(EV/売上、PSR)と PER の水準。過去平均・10年平均との比較(出典明記。推定値は推定と記す)。
  - 主要イベント: 2026年8月のブラックハット(米国のセキュリティ会議)後の上昇とその原因、主要銘柄の決算前後の大幅変動。
- クエリ: `CIBR HACK BUG ETF 2026 performance year to date`、`cybersecurity stocks valuation EV/sales premium historical average 2026`、`cybersecurity stocks rally Black Hat August 2026`、`cybersecurity ETF October 2026`
- 注意: ETF の騰落は、ETF 運用会社(First Trust、Global X、Amplify)の公式ページを優先し、ニュースサイトの要約は Tier 3 として扱う。

## 7. 規制・制度 — 欠損

- 取得できたもの: なし。
- 欲しいデータ(上向き・下向きの両方向を書く):
  - SEC のサイバー開示規則(2023年採択。重大インシデントの Form 8-K 開示と、年次のリスク管理開示): 現在の運用・改正・緩和の動き。
  - EU: NIS2 指令(重要・基幹事業者のサイバー義務の拡大)の加盟国での国内法化の進捗と執行、DORA(EUの金融機関向けデジタル運用レジリエンス規則。2025年1月適用)。Cyber Resilience Act。
  - 米国連邦政府: ゼロトラスト指令(OMB M-22-09)の進捗、2025〜2026年の政策変更、CISA(サイバーセキュリティ・インフラセキュリティ庁)の予算・人員の削減や再編、CISA 2015(情報共有法)の期限と再承認、FedRAMP の改革。
  - 日本・英国などの制度(任意)。
- クエリ: `SEC cybersecurity disclosure rule 2026 changes`、`NIS2 transposition status 2026 enforcement`、`DORA enforcement 2026 ICT third-party`、`CISA budget fiscal 2027 cuts`、`federal zero trust OMB 2026 CISA workforce cuts cybersecurity information sharing act reauthorization`

## 8. 大規模事件 — 欠損

- 取得できたもの: なし。
- 欲しいデータ(2025〜2026年に、需要または競争に影響したもの):
  - 事件・障害の概要、日付、被害規模、受益・損失を受けたベンダー。
  - 例として調べる範囲: 2025年のサプライチェーン攻撃、SaaS 連携トークン経由の大規模データ窃取、ランサムウェアによる大手小売・自動車・製造業の停止、国家支援の攻撃(Salt Typhoon 等)、2024年7月の CrowdStrike 障害の後日談(補償・解約・競争への影響。2025〜2026年の更新があるか)、Cloudflare 等のインフラ障害(2025年に複数件の報道。日付と原因は要検索)。
  - 事件が需要を押し上げた(例: 侵害後の追加投資)か、競争を変えた(例: 障害による顧客の乗り換え)かの区別。
- クエリ: `biggest cyberattacks 2026 so far`、`major cyber incidents 2025 year in review`、`outage Cloudflare 2026 cause`、`CrowdStrike outage aftermath customers 2026`、`ransomware attack 2026 retailer manufacturing shutdown`

## 9. 再開時の優先順位(検索を最小回数で埋める手順)

予算が復活した場合、重要度の高い順に次の12件で足りる。

1. Gartner 情報セキュリティ支出予測(最新版)
2. IDC セキュリティ支出予測
3. Google・Wiz の完了状況
4. Palo Alto・CyberArk の完了状況
5. Microsoft セキュリティ売上の開示
6. SaaSpocalypse とセキュリティ株の対比
7. CIBR・HACK・BUG の2026年騰落
8. セクターのバリュエーション倍率
9. AIセキュリティ市場の予測
10. AI を使った攻撃の統計
11. SEC・NIS2・CISA 予算の最新
12. 2025〜2026年の大規模事件

追加で、CrowdStrike・Zscaler・ServiceNow の買収(節3)と、ファイアウォール・SASE の市場規模(節2)を補う。

## 10. 統括への依頼

- 検索予算が復活しない場合、本書の8節は埋まらない。業界節は「欠損」として扱い、各社の個別分析(PANW・CRWD・FTNT・NET・ZS・OKTA)が各社の一次資料で取得する業界情報(市場規模、競合、買収)に頼るのが次善策である。
- 追加の検索予算を割り当てる場合は、利用者が追加メッセージを送る必要がある(または環境変数の引き上げ)。割り当て後は、本書の節ごとのクエリをそのまま使える。
