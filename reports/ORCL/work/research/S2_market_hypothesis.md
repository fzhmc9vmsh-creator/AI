# Oracle (NYSE: ORCL) 市場の仮説 調査メモ(S2)

作成日: 2026-10-11 / 担当: 市場の仮説の収集(投資判断は含まない)

## 0. 調査の限界(最初に必ず読むこと)

- WebFetch は全ドメインで DNS 失敗(ENOTFOUND)。決算説明会の書き起こし全文・アナリストノート本文・各記事の本文は一度も開けていない。
- WebSearch は 1 ターン 200 回の共有上限に達し、調査の途中(強気派・弱気派の個別論点の深掘りの直前)で打ち切られた。空売り勢・著名投資家の個別検索、各社目標株価の根拠、EPS 予想修正、リバース DCF 系の記述は未調査または未取得。
- 以下の内容はすべて「検索ツールが返した、各ページの要約文」に基づく。要約は第三者転記・AI 生成物を含み、数字や人名が出典間で食い違う箇所がある(第9章に列挙)。原文の引用は、要約に含まれていた短いものに限る。
- 確度の記号: [◎]=Oracle の決算資料・SEC 提出資料に由来すると要約に明記 / [○]=複数の独立した出典で一致 / [△]=単一の二次出典または AI 要約 / [✕]=出典間で矛盾あり。
- 「算術」と書いた数字は、出典の数字を私が割り算しただけのもの(出典に書かれた主張ではない)。
- 経営陣名: CEO Clay Magouyrk、共同 CEO Mike Sicilia、CFO Hilary Maxson(2026年6月・9月の出典による)。2026年3月の出典は財務責任者を「Doug Kehring/Caring」など複数の綴りで記載しており、綴りは未確認。

---

## 1. 決算説明会でアナリストが繰り返した質問(テーマ別)

質疑応答(Q&A)の全文は入手できなかった。下表は、検索で返った書き起こし転記・要約から「質問者と要旨が読み取れたもの」だけを集計した。出現回数は「確認できた範囲」の件数であり、実際の質問数ではない。

### 1-1. テーマ別集計

| テーマ | 確認できた質問(質問者・所属・call) | 経営陣の回答要旨(確認できた範囲) | 確認件数 | 出典 |
|---|---|---|---|---|
| 資金調達・FCF・capex の持続性 | Q1 FY27(2026-09-10): Deutsche Bank のアナリスト(氏名は未確認)が「支出は今後2年を超えて減速し得るか」「FCF はいつプラスに戻るか」を質問 / Q3 FY26(2026-03-10): 氏名不明のアナリストが FY27 capex を質問 / Q4 FY26(2026-06-10): Deutsche Bank の Brad Zelnick(AI 生成スクリプトによる推定。未検証)が「巨額投資期のリターンをどう評価すべきか」を質問 | Q1 FY27: FCF の時期は「示していないし、本日も示す予定はない」。Magouyrk: 供給業者ファイナンス・顧客の前払い・顧客持込ハード(BYOH)により、全資本を Oracle が負担せずに成長できる。Q3 FY26: CFO は FY27 capex の詳細を決算期末後に回答すると延期し、capex と Oracle の自己資金負担が「分離(uncoupling)」していると説明、投資適格格付けの維持を再確認。Q4 FY26: capex 増加は部品価格ではなく大半がタイミングの問題(Equibles 転記の要約) | 3(3 call すべて) | [S4][S5][S6][S28 MarketBeat][S27 Equibles/moomoo] △ |
| AI クラウドのマージン・価格 | Q1 FY27: Barclays の Raimo Lenschow が「データセンター容量の価格は契約価格とスポット価格でどう動くか」「昨年示した粗利益率の枠組みは維持されるか」を質問 / Q4 FY26: BMO の Keith Bachman が価格と案件構造を質問(要旨のみ。回答不明) | Q1 FY27: 部品コストは上昇しているが、粗利益率を守るのに十分な値上げを見込む(Yahoo の要約)。CFO: 各拠点が契約どおりの売上水準に達すれば、利益率は「急速に」回復する(fourweekmba の要約)。Q4 FY26: 部品コスト等を顧客に転嫁する仕組みがある(moomoo の AI 要約) | 2 | [S4][S6][S9][S27] △ |
| データセンター建設進捗・電力・納期 | Q1 FY27: Mizuho の Siti Panigrahi が「(関係する)データセンターの納期にリスクはあるか。FY27 の売上予想を脅かさないか」を質問(要約中の「both sides」の相手方は不明) | 回答は取得できず。参考: Q4 FY26 で Magouyrk は FY26 中に 1.2GW を納入、FY27 第1四半期に約 1GW を見込むと説明。Abilene は 42% 納入済みで今後90日でさらに 35%(要約。どの call の発言かは不確か) | 1 | [S4][S27 DCD] △ |
| 契約構造(前払い/BYOH)と追加資本の要否 | Q1 FY27: 氏名不明のアナリストが「追加 capex を要しない契約」について質問。ある Substack は「質問者の誤解から始まった」と評している | Oracle の説明(JPMorgan 経由): 新規契約の構造化は資本調達計画に「追加の影響はない」。Q1 の AI 新規契約は >$30B で、追加資本を要しない。累計で $75B が前払いまたは顧客持込ハード(CFO) | 1〜2 | [S7][S11][S10] △ |
| カウンターパーティー・OpenAI の支払能力 | Q1 FY27: 取引先の信用に関する質問があった模様(氏名不明)。OpenAI の名指しの質問は、確認できた転記・要約中には見つからなかった | Magouyrk: 顧客はスタートアップから大手の投資適格企業まで幅広い(Substack の要約)。参考(2025年9月の発言): AI 顧客は 700 社超、単一顧客の需要が実現しなくても容量は数時間で他顧客へ振り向けられる | 1(OpenAI 名指しは0) | [S7][S22 の2025年資料] △ |
| 長期目標・RPO の売上転換時期 | Q4 FY26: Guggenheim の John DiFucci が長期目標を質問(回答不明) | Q1 FY27: CFO は RPO の約半分が今後36か月で売上化すると説明 | 1 | [S27 Equibles][S9] △ |
| AI がアプリ事業を脅かすか | Q3 FY26: JPMorgan の Mark Murphy が「AI がアプリケーションソフトを脅かすのでは」という投資家の疑問を質問 | 回答不明 | 1 | [S28 の検索要約] △ |
| 株式希薄化 | 該当する質問は確認できず | 事実のみ: Q1 FY27 に $20B の at-the-market(ATM)増資を全額完了。希薄化後加重平均株式数は前年比 +3%(約 30億株) | 0 | [S5][S2] ◎〜△ |

### 1-2. 経営陣が質問の前に自ら開示した主な数字(Q&A ではなく準備コメント)

| call | 開示内容 | 出典 |
|---|---|---|
| Q3 FY26 (2026-03-10) | RPO $553B。前回 call 以降 $29B 超の契約を BYOH・前払いで獲得。確保した 10GW 超の電力・容量の 90% 超はパートナー資金。AI 容量の粗利益率 32%(ガイダンス 30%)。2026年に最大 $50B の資金調達計画のうち $30B を調達済み(投資適格債・強制転換優先株) | [S28] △ |
| Q4 FY26 (2026-06-10) | RPO $638B。FY26 capex $55.7B、FCF -$23.7B。FY27 capex は総額 $90〜95B、うち自社の現金負担(net)は最大 $70B(顧客前払い $20〜25B を除く)。FY27 に債務と株式で約 $40B を調達(うち $20B は ATM)。Q4 に $67B の AI 契約(大半が BYOH または前払い)を獲得。粗利益率は約5pt 低下 | [S27] ○ |
| Q1 FY27 (2026-09-10) | 売上 $19.3B(+30%)、OCI $7.4B(+121%)、RPO $664B、非GAAP EPS $1.92。営業CF $23.1B、capex $28.5B、FCF -$5.4B(6四半期連続マイナス)。net 現金 capex は $18B。顧客前払い(重要な金融要素あり)は $11.4B。FY27 売上は「$90B 以上」(従来 $90B)、非GAAP EPS $8.10(従来 $8.05)。Q2 ガイド: 売上 +30〜34%、非GAAP EPS $1.83〜1.93。AI 容量 850MW・GPU 30万基超を納入、GPU 稼働率 97.9%。CFO は「この四半期を一言で言えば acceleration(加速)」と発言。FCF 黒字化の時期は示さず | [S1][S2][S3][S8][S10] ◎〜○ |

---

## 2. 強気派の論点

目標株価・レーティングは Benzinga 等の検索要約による。各社の売上・EPS・倍率の前提は、ほぼ取得できなかった(「取得不可」と記す)。右端の「FY27ガイドEPS(\$8.10)に対する単純倍率」は私の算術であり、各社がその年度のEPSで目標を算出したという意味ではない。

| 社・アナリスト | レーティング / 目標株価 / 日付 | 中心論点 | 数値前提 | 倍率(算術) | 出典 |
|---|---|---|---|---|---|
| Guggenheim・John DiFucci | Buy / $400(維持)/ 2026-09-11 付(7月17日にも $400 維持) | 論点の本文は取得不可。7月17日の記事見出しは「この会社は12か月で3倍になると見る」 | 取得不可 | 約49倍 | [S12][S18][S19] △ |
| Mizuho・Siti Panigrahi | Outperform / $320(維持)/ 決算前の 9/8、決算後の 9/15 に維持 | OCI が主要な成長の触媒。Oracle は市場予想を上回ると予想(決算前)。決算前の時点で FCF の黒字化は FY2029 まで来ないと見ていた | FCF 黒字化 FY2029(決算前) | 約39.5倍 | [S15][S16][S17] △ |
| Barclays・Raimo Lenschow | Overweight / $250→$252(引き上げ)/ 2026年9月(決算後) | $20B の ATM 増資を完了したことで、借入だけに頼らず投資する余地ができた。見出しは「成長は inflected(変曲した)」 | 取得不可 | 約31倍 | [S12][S13][S14] △ |
| JPMorgan(アナリスト名は検索で特定できず) | Overweight / $200 / 2026-09-11 のノート(2026-03-11 に Neutral から Overweight へ格上げ) | Q1 の新規契約 >$30B は主に前払い/BYOH で、Oracle に追加の現金を要しない。3月の格上げ理由は「売り込まれて risk-reward が改善した」。ただし顧客集中・資金調達へのアクセス・容量納入を下振れリスクとして挙げた | RPO $664B(前年比 +46%、前期比 +$26B) | 約24.7倍 | [S11][S20] ○ |
| UBS・Karl Keirstead | Buy / $245→$250(引き上げ)/ 2026-09-11 | 論点の本文は取得不可 | 取得不可 | 約30.9倍 | [S13][S12] △ |
| Stifel・Brad Reback | Buy / $220→$200(引き下げ)/ 決算後 | 「強い四半期」。FY27 売上 $90B 超のガイドは OCI 約 +120% 成長を意味する。短期の粗利益率は下がるが、OCI 成長の加速と営業費用の効率化で時間をかけて相殺できる。ただしバリュエーションには慎重(強気寄りだが目標は引き下げ) | OCI 成長 約+120%(FY27) | 約24.7倍 | [S14][S9] △(単一出典) |

その他の強気寄り(確認できた範囲): Cantor Fitzgerald・Thomas Blakey Overweight $284(決算後維持)、Jefferies・Brent Thill Buy $320→$290(9/2、決算前の引き下げ)、Evercore ISI・Kirk Materne Buy 再確認(9/24、目標株価不明)、Oppenheimer $275(9/8、レーティング不明)。出典: [S12][S13][S15][S17]。

---

## 3. 弱気派・慎重派の論点

| 主体 | 立場・日付 | 中心論点 | 数値 | 出典 |
|---|---|---|---|---|
| Morgan Stanley(アナリストは Sanjit Singh と報じられた。Keith Weiss とする別の報道もあり未確定) | Equal-Weight / $207→$210 / 2026-09-04(決算前)。決算後も $210 維持と報じられた | 「実行力は印象的だが、収益性への道筋が残る問い」。予想期間を通じて FCF が制約される。中心の懸念は capex $28.5B と FCF -$5.4B | 目標 $210 | [S13][S38] △ |
| Stephens・Brett Huff | Equal-Weight / $175(決算後維持) | 論点の本文は取得不可 | 目標 $175 | [S12] △ |
| BMO・Keith Bachman | Benzinga は「Outperform、$220→$195(引き下げ)」と報じるが、別の TipRanks/TheFly 見出しは「Market Perform、$175→$200」(日付不明) | レーティングと目標が出典間で矛盾 | $195 または $200 | [S12][S36 周辺] ✕ |
| S&P Global Ratings(格付会社) | 2026-07-09 に BBB から BBB- へ引き下げ(見通しは安定)。短期格付けは A-2 から A-3 | FY27 の営業FCF赤字を従来予想の約 -$24B から約 -$42B へ下方修正。OpenAI が契約債務の「ほぼ半分」を占めると名指し。レバレッジが 4.5 倍を超え続ければ再格下げもあり得る | FOCF -$42B(FY27 予想) | [S21] ○ |
| Moody's | 見通し「ネガティブ」。レバレッジが一時的に EBITDA の約5倍に近づき得ると警告 | 2025年にはこの構築を「巨大なプロジェクトファイナンスで、重大なカウンターパーティーリスクを伴う」と評した(どの記事か特定不可) | 5倍(一時的) | [S21][S22 の2025年資料] △ |
| Fitch | 格下げなし。無条件の賃料支払い約束のため、AI データセンター発行体の中で最上位の格付けを付与。ただし閾値を超えるレバレッジが続けば負の格付け行動もあり得ると警告 | 弱気というより「条件付き」 | — | [S21] △ |
| クレジット市場(CDS・社債) | 5年CDS: 2025年11月に 120〜150bp(OpenAI 契約前は 50bp 未満)→ 2026年7月に約 203bp(約18年ぶりの高水準)。Bloomberg 報道として 198bp が記録的水準とする記事、2026年8月初めに約 215bp とする記事もあり、時系列は未整理。2026-09-24 に過去最高との報道が1件 | 2025年9月発行の $18B 債は含み損約 $1.35B(2035年債のスプレッドは国債比 187bp) | 203bp / 198bp / 215bp / 187bp | [S21][S22][S32][S33] ✕(水準・日付が混在) |
| 弱気派アナリスト(Rothschild & Redburn・Alex Haissl) | 2025-09-25 に Sell で調査開始、目標 $175(当時の株価約 $308 に対し約 -40%)。現在の見解は未確認 | 市場は契約済みクラウド収益の価値を「大きく過大評価」している。単一テナント・大規模展開では、クラウド事業者というより金融業者に近い | 目標 $175 | [S23] ○(2025年の資料) |
| 構造的な弱気論(ブログ・分析記事) | 2026年 | FY26 期末の債務約 $129.5B ≒ EBITDA の 4.3 倍。長期のデータセンターリース約 $260B と、より短い顧客契約との期間のミスマッチ。「クラウド倍率をまとった OpenAI のクレジットストーリー」。TTM FCF は +$11.8B から -$24.7B へ | 債務 $129.5B、リース約 $260B | [S22 mitsloanme/arpu.hedder/Lex] △ |
| Paul Kedrosky(評論家) | 2025-12-18(Axios): Blue Owl 撤退を「警鐘(clanging bells)」と表現。「AI は過去のあらゆるバブルを全部合わせたもの」。2026年10月に Benzinga が「Oracle は4つのバブルリスクにさらされる」と題する記事を掲載(本文未取得) | 不動産、テクノロジー、特殊な資金調達構造 | — | [S24][S25] △ |
| 慎重論だが破綻は否定(参考) | D.A. Davidson・Gil Luria(日付不明): OpenAI 契約が消えれば Oracle は建設を縮小し、一部契約を償却し、債務の削減に入るが、デフォルトはしない | — | — | [S22 Khaleej Times] △ |

未調査(検索上限に達したため): 空売り勢の具体名(Michael Burry、Jim Chanos 等への言及)、個別の債券アナリスト(CreditSights、Bloomberg Intelligence 等)、Seeking Alpha 記事「Oracle: OpenAI Could Walk Away」(見出しのみ確認。著者・日付不明)の本文。

---

## 4. 報道のナラティブ年表

株価の数字は、検索要約に出てきたものだけを転記した。報道間で食い違う場合は併記した。

| 日付 | 株価の動き | 報道が挙げた理由(媒体・見出し) | 出典 |
|---|---|---|---|
| 2025-09-09/10 | 1日で約 +36%(1992年以来最大の1日上昇)。52週高値 $345.72、時価総額約 $877〜900B | FY26 Q1 決算で RPO が $455B(+359%)に急増。OpenAI との約 $300B・5年の契約が主因。Motley Fool「Why Oracle rallied in September」(2025-10-07) | [S31] ○ |
| 2025-09 中旬〜下旬 | 高値から約15%下落(9/12 週)。9/25〜26 に -4〜6% | RPO のうち約 $300B が OpenAI 1社と判明(WSJ 報道を引用した記事)。9/25 に Redburn が Sell・$175 で調査開始。Motley Fool「Why Oracle Stock Dropped Today」(2025-09-25) | [S31][S23] ○ |
| 2025-11 | 11/21 時点で9/10 比で時価総額が約3分の1減 | 5年CDS が急上昇(50bp 未満 → 120〜150bp)。9月発行の $18B 債の含み損。OpenAI 関連データセンターの遅延報道で社債が下落。BondBlox「Oracle's dollar bonds continue to slip」、Motley Fool 系「Here's Why Oracle Stock Got Hammered Last Month」 | [S32] ○ |
| 2025-12-10/11 | 決算後に約 -11%(時間外)。AP は一時 -13.4%。12/12 の週は7年超で最悪の週間下落(Seeking Alpha 12/13) | FY26 Q2: 売上 $16.06B が予想 $16.21B に未達、ソフトウェア売上 -3%、FCF 約 -$10B、FY26 capex 見通しを $35B から約 $50B へ引き上げ。RPO $523B。TIKR「Oracle stock plunges over 11% as fiscal Q2 revenue misses estimates」 | [S29] ○ |
| 2025-12-12〜17 | 約 -5%(Blue Owl 報道) | FT: Blue Owl が Michigan の $10B データセンター(1GW・OpenAI 向け)への出資協議から離脱(Oracle は反論)。Bloomberg: OpenAI 関連拠点の一部が2027年から2028年へ遅延(Oracle は「契約上必要な拠点に遅延はない」と否定)。Motley Fool「Why Oracle Stock Is Sinking Once Again」(12/17)、Axios「Why Oracle keeps sparking AI-bubble fears」(12/18) | [S29][S24] ○ |
| 2026-02-01/02 | 寄り前 -4〜6%、終値は報道により -3%〜小幅高と不一致。9月の高値から約 -50% | 2026年に $45〜50B を債務と株式で調達する計画(ATM で最大 $20B 増資、投資適格の優先債1本を含む)を発表。希薄化と債務が懸念。Bernstein は「債務と株式の組み合わせは投資適格格付けの維持に資する」。Reuters 系「Oracle shares fall as investors assess up to $50 billion AI funding plan」 | [S30] △(終値は✕) |
| 2026-03-10/11 | 決算後に +8〜9%(最大 +14% とする報道も)。前日終値 $149.40 | FY26 Q3: 売上 $17.19B(予想 $16.91B)、非GAAP EPS $1.79(予想 $1.71)、OCI +84%、FY27 売上目標を $90B に上方修正。「顧客持込チップ方式が機能している」。JPMorgan が Overweight へ格上げ。「SaaS 黙示録」懸念への反証とも報じられた。Motley Fool「Why Oracle stock is ripping higher in after hours」(3/10) | [S28] ○ |
| 2026-06-10/11 | 翌日の初回終値 -8.5%(-10% とする報道も) | FY26 Q4: 決算自体は好調(EPS $2.11、OCI +93%、RPO $638B)だが、FY27 capex $90〜95B(市場予想 $61.7B 近辺との報道)、約 $40B の追加調達、FCF -$23.7B、粗利益率低下が嫌気された。TIKR「Oracle stock fell 8% after a record quarter」、HL「Oracle shares drop despite record Q4 as guidance underwhelms」 | [S27] ○ |
| 2026-06-26(週) | 週間 -18.4%(終値 $148.53)。2001年8月以来最悪の週 | 債務約 $130B、FY26 capex 前年比 +162%、FCF の大幅マイナス、$40B 調達計画、RPO の50%超が OpenAI(BofA)。CNBC「Oracle stock has worst week since 2001 dot-com bust as AI financing concerns escalate」 | [S26] ○ |
| 2026-07-09 | 約 -4%(1年来安値)。CDS 約 203bp | S&P が BBB- に格下げ。OpenAI をリスクとして名指し。「Oracle Shares Fall 4% to One-Year Low: S&P Downgrades Credit Rating to BBB-, OpenAI Named as Risk」 | [S21] ○ |
| 2026-07-20/23 | 7/20 に52週安値(場中 $120.45)、7/23 に -4.6% | 一部アナリストは「下落で魅力的」としつつ下落継続。具体的な理由は取得不可(MarketBeat の定型記事) | [S37] △ |
| 2026-08〜09 初旬 | 8/3 に $142.33。8/12 に +5.9%(CoreWeave・Nebius の好決算に連れ高とされる)。9/3 時点でピークから約 -55%、9/5 に $120 台を維持 | 決算前のポジション調整。「3か月で -40%、9/10 の決算が分かれ目」(TIKR、9/1 付) | [S36 MarketBeat][S37] △ |
| 2026-09-10/11 | 時間外 +7%(Stocktwits)、翌日 +4.4%(Tiger)、9/11 は +2.5% の $157.18(Benzinga)。出典間で水準が異なる | FY27 Q1: 売上 +30%、OCI +121%、RPO $664B、FY27 売上「$90B 以上」へ上方修正。新規契約 >$30B は前払い/BYOH で追加資本不要。一方、FCF -$5.4B・capex $28.5B・粗利益率低下・FCF 黒字化時期の非開示は残る。Barclays「成長は inflected」 | [S1][S12][S14] ○(株価水準は✕) |
| 2026-09-24 | 約 -4〜5%。10年債・30年債利回りが 2007年・22年ぶりの高水準(30年債 5.44%) | Oracle が Blue Owl 傘下の主体に、ニューメキシコ州の Project Jupiter(2.45GW)の電力遅延を理由とする force majeure(不可抗力)通知を送付。賃料支払いの繰り延べが狙い(Bloomberg 系)。完成は約1年遅れるとの関係者証言。Oracle は2028年目標を維持と説明。同日、CDS が過去最高との報道が1件(未確認) | [S33] ○(CDS は△) |
| 2026-09-25〜28 | 9/25 終値 $137、9/28 に -3.3%(安値 $131.58、終値付近 $132.64) | 9/28 の下落理由は報道されていない(MarketBeat は定型記事)。50日・200日移動平均を下回る | [S34] ○ |
| 2026-10-08 | -5.2〜6%(終値 $135.69)。SoftBank は東京で約 -10%。Broadcom -4%、Nvidia -2% | FT 報道: OpenAI が投資家に示した年率売上は9月末で約 $50B で、従来報じられた約 $68〜70B を下回る(差は収益の計算方法の違い=パートナー分の総額計上が主因との解説もあり、売上喪失を意味しない)。Bloomberg 報道: Project Jupiter のガスパイプライン経路を州規制当局が却下し、稼働開始が2027年にずれ込む見通し。Oracle はガスのトラック輸送など暫定策を検討。債券利回りの上昇も重しに。TipRanks「Why Oracle Stock (ORCL) Is Sinking Today – October 8, 2026」 | [S35] ○ |

株価の推移の要約(出典に基づく): 2025年9月に 52週高値 $345.72 をつけた後、12月の決算(-11%)と Blue Owl 報道、2026年2月の資金調達発表を経て、3月の Q3 決算で一時反発(+8〜9%)。6月の Q4 決算(-8.5%)と翌週の週間 -18.4%、7月の S&P 格下げを経て、7月20日に場中 $120.45 の安値。9月の Q1 決算後は $157 まで戻したが、Project Jupiter の force majeure(9/24)と OpenAI 売上報道(10/8)で $135.69(10/8 終値)。ピークからの下落率は約 -61%(算術。Motley Fool の見出しは 9/17 に「-53%」、9/30 に「-60%」)。

---

## 5. 株価が織り込む前提(アナリスト・記事の記述)

リバース DCF として明示された記述は、検索では見つからなかった。EV/EBITDA の明示的な数字も取得できなかった。取得できた「織り込み」に近い記述は次のとおり。

| 項目 | 記述 | 出典 |
|---|---|---|
| PER | ある記事は、PER が9月のピーク時の 76 倍から約 22 倍へ低下したと記述(どの記事か特定不可。日付も不明、トレーリングベースと思われる) | [S37 周辺] △ |
| PER(算術) | $135.69(10/8 終値)÷ FY27 ガイダンス EPS $8.10 = 約 16.8 倍(コンセンサス FY27 EPS $8.14 とする記事では約 16.7 倍) | 算術 |
| 時価総額(算術) | $135.69 × 希薄化後株式数 約 30億株 = 約 $4,070億(ピーク時 $877〜900B) | 算術 |
| 割安度の指標 | GuruFocus の独自モデル「GF Value」$194.75 に対し株価 $135.69(10/8) | [S35 GuruFocus] △ |
| 売上の前提 | コンセンサス FY27 $90.48B、FY28 $131.45B(Yahoo Finance、日付不明)。Oracle ガイダンスは FY27 $90B 以上(+34%) | [S1] ◎ / Yahoo △ |
| FCF の前提 | Mizuho: FY2029 まで黒字化しない(決算前)。Morgan Stanley: 予想期間を通じて制約。S&P: FY27 の営業 FCF は約 -$42B。経営陣は黒字化時期を示さない | [S15][S13][S21][S4] ○ |
| 資金調達の前提 | FY27 に債務・株式で約 $40B(うち $20B の ATM は Q1 で完了)。FY27 の net 現金 capex は最大 $70B | [S27][S5] ○ |
| 売上転換 | RPO $664B の約半分が36か月で売上化(CFO)。OpenAI は約 $300B(RPO の約45%、S&P は「ほぼ半分」、BofA は2026年6月時点で RPO $638B の50%超と推定) | [S9][S21][S26][S35] ○ |
| 市場が重視する指標 | 「市場は12か月、需要ではなく資金調達を疑って株価を下げてきた」(Substack のレビュー)。「バックログが見出し、capex が本題」(fourweekmba) | [S7][S9] △ |
| 利益率 | 粗利益率は FY27 を通じて低下する見込み(CFO)。非GAAP 営業利益率は Q1 で 42% | [S1][S8] ○ |

---

## 6. 市場の見方の分布

### 6-1. レーティングと目標株価(データ源ごとに母集団が異なる)

| データ源・日付 | 母集団 | Buy / Hold / Sell | 平均目標 | 範囲 | 出典 |
|---|---|---|---|---|---|
| MarketBeat 2026-10-10 | 47人 | Buy 36(うち Strong Buy 1)/ Hold 9 / Sell 1 → Moderate Buy | $251.72 | — | [S36] ○ |
| StockAnalysis(S&P Global)10/8 時点 | 43人 | Buy | $237.97 | $110〜$400 | [S36] ○ |
| Investing.com 10/8 前後 | 41人(過去3か月) | Buy 35 / Hold 7 / Sell 1(合計43で母集団と不一致) | $237.97 | $110〜$400 | [S36] ✕ |
| CNN | 45人 | Buy 約80% / Hold 約18% / Sell 約2% | — | — | [S36] △ |
| WallStreetZen | 24人 | Strong Buy 13 | $243.38 | — | [S36] △ |

平均目標 $251.72 は 10/8 終値 $135.69 の約 1.86 倍(算術)。

### 6-2. 目標株価の時系列(平均値)

| 時点 | 平均目標 | 母集団 | 出典 |
|---|---|---|---|
| 2026-07-20(Investing.com) | $251.85 | 40人 | [S36] △ |
| 2026-07-27〜08-03(MarketBeat) | $265.03 | 39人(Buy 28、Strong Buy 2、Hold 8、Sell 1) | [S36] △ |
| 2026-09-08(決算前、parameter.io) | $261.68(範囲 $145〜$320) | 40人 | [S15] △ |
| 2026-09-28(MarketBeat) | $254.68 | — | [S34] ○ |
| 2026-10-10(MarketBeat) | $251.72 | 47人 | [S36] ○ |

平均目標は夏以降、緩やかな低下傾向($265 → $252)。ただしデータ源と母集団が違うため、厳密な比較はできない。

### 6-3. 直近の修正(決算前後・確認できたもの)

| 方向 | 事例(日付) |
|---|---|
| 引き上げ | Barclays $250→$252(決算後)、UBS $245→$250(9/11)、Morgan Stanley $207→$210(9/4・決算前) |
| 引き下げ | Stifel $220→$200(決算後)、BMO $220→$195(Benzinga。矛盾あり)、Jefferies $320→$290(9/2・決算前) |
| 維持 | Guggenheim $400、Mizuho $320、Cantor $284、Stephens $175、JPMorgan $200、Evercore(Buy 再確認 9/24) |

件数の整理(確認できた範囲): 引き上げ 3、引き下げ 3、維持 6 以上。方向は「小幅な混在」で、一方向の修正トレンドは確認できない。EPS 予想の修正方向を示す出典は取得できなかった(Oracle 自身の FY27 EPS ガイダンスは $8.05 から $8.10 へ引き上げ、決算前の市場予想 $8.07)。

---

## 7. 市場の仮説の要約(出典に基づく。私の意見ではない)

報道が伝える市場の中心的な争点は、RPO $664B の存在そのものよりも、その建設資金を Oracle が賄えるかどうかである(CNBC 2026-06-26、Motley Fool 系、Substack のレビュー)。弱気側の根拠は、OpenAI が RPO の約半分を占めること(S&P、BofA)、FCF が6四半期連続のマイナスで S&P は FY27 の営業 FCF を約 -$42B と予想していること、BBB- 格付けと 200bp 前後の CDS、Project Jupiter の電力・納期リスク(9/24 の force majeure 通知、10/8 の Bloomberg 報道)である。強気側の根拠は、Q1 の新規契約 >$30B が前払い/BYOH で Oracle に追加資金を要しないこと(JPMorgan、Oracle)、OCI +121% と FY27 売上ガイダンス「$90B 以上」・EPS $8.10 への上方修正(Oracle、Stifel)、$20B の ATM 完了で借入依存が下がったこと(Barclays)である。レーティングは Buy 系が約8割(MarketBeat: 47人中37人)で、平均目標 $252 は 10/8 終値 $135.69 の約1.9倍(算術)と大きく乖離しており、直近の下落(10/8 の約 -5.5%)は OpenAI の売上報道・Project Jupiter の遅延・債券利回り上昇に反応したものと報じられた(TipRanks、Mitrade/BeInCrypto、FX Leaders)。

---

## 8. 出典一覧

すべて、検索ツールが返したタイトル・URL。本文を直接開いたものはない。

- S1 Oracle, Press Release「Q1 FY27 Earnings」 2026-09-10 https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/
- S2 Oracle IR, 1Q27 press release PDF 2026-09-10 https://investor.oracle.com/files/content_files/1q27-pressrelease-September_FINAL.pdf ; SEC 8-K Ex.99.1 https://www.sec.gov/Archives/edgar/data/0001341439/000119312526387905/orcl-ex99_1.htm ; スライド https://s23.q4cdn.com/440135859/files/content_files/Q1-FY27-Oracle-Earnings-Slides.pdf
- S3 Quartr, Oracle Q1 2027 earnings summary https://quartr.com/events/oracle-corporation-orcl-q1-2027_3gvkOKJp
- S4 roic.ai, Q1 FY2027 transcript 2026-09-10 https://www.roic.ai/quote/ORAC.TO/transcripts/2027-year/1-quarter (Q&A: Panigrahi、Lenschow、FCF の質問)
- S5 Alpha Spread, ORCL Q1-2027 earnings call https://www.alphaspread.com/security/nyse/orcl/investor-relations/earnings-call/q1-2027
- S6 Yahoo Finance「Oracle Q1 Earnings Call Centers on AI Capacity and Raised Outlook」 https://finance.yahoo.com/technology/ai/articles/oracle-q1-earnings-call-centers-140000080.html
- S7 Substack レビュー: https://investwithcolby.substack.com/p/oracle-corporation-orcl-q1-fy2027 および https://nikhs.substack.com/p/oracles-1qfy27-earnings-what-oracle (どちらの記述か特定不可)
- S8 Constellation Research「Oracle Q1 strong and so is capital expenditures」 https://www.constellationr.com/insights/news/oracle-q1-strong-and-so-capital-expenditures
- S9 fourweekmba「Oracle's Q1 FY2027 Results: The Backlog Is the Headline, the Capex Is the Story」 https://fourweekmba.com/ai-oracle-q1-fy2027-backlog-capex-analysis/
- S10 erp.today「Oracle's $664 Billion Backlog Comes With a New Financing Model」 https://erp.today/oracle-q1-fy27-results-664b-backlog-ai-contracts/
- S11 TechFlow「JPMorgan: Oracle's backlog increases by 26 billion, funding path remains questionable」 2026-09-11 https://www.techflowpost.com/en-US/newsletter/136110
- S12 Benzinga「These Analysts Revise Their Forecasts On Oracle After Q1 Results」 2026-09 https://www.benzinga.com/analyst-stock-ratings/price-target/26/09/61739498/these-analysts-revise-their-forecasts-on-oracle-after-q1-results
- S13 TheStreet: Barclays https://www.thestreet.com/investing/stocks/barclays-oracle-stock-price-target-raised ; UBS https://www.thestreet.com/investing/stocks/5-star-analyst-resets-oracle-stock-price-target ; Morgan Stanley https://www.thestreet.com/investing/stocks/orcl-oracle-stock-price-target-morgan-stanley-maintains-equal-weight-after-q1-fiscal-2027-earnings
- S14 Stocktwits「ORCL Stock On Track To Erase Pre-Earnings Losses, Barclays Says Growth Has 'Inflected'」(Stifel の Reback コメントを含む) https://stocktwits.com/news-articles/markets/equity/oracle-stock-rebounds-barclays-growth-inflected/cZtXhI4RBGj
- S15 parameter.io(決算前の目標株価一覧、2026-09-08) https://parameter.io/oracle-orcl-stock-climbs-2-as-wall-street-analysts-update-targets-ahead-of-earnings/
- S16 EdgeX, Mizuho 決算前 https://pro.edgex.exchange/en-US/news/article/oracle-q1-2027-earnings-preview-oci-growth
- S17 Investing.com, ORCL consensus(Mizuho 9/15 維持) https://www.investing.com/equities/oracle-corp-consensus-estimates
- S18 Tickernerd(Guggenheim 9/11) https://tickernerd.com/stock/orcl-forecast/
- S19 24/7 Wall St. 2026-07-17 https://247wallst.com/investing/2026/07/17/oracle-is-falling-fast-heres-why-this-wall-street-firm-believes-the-stock-will-triple-in-12-months/
- S20 Seeking Alpha「Oracle surges after 'strong' Q3 and outlook, gets upgrade at J.P. Morgan」 2026-03 https://seekingalpha.com/news/4563089-oracle-surges-after-strong-q3-and-outlook-gets-upgrade-at-jp-morgan ; MarketBeat 2026-03-11 https://www.marketbeat.com/instant-alerts/oracle-nyseorcl-raised-to-overweight-at-jpmorgan-chase-co-2026-03-11/
- S21 S&P 格下げ関連: The Next Web https://thenextweb.com/news/oracle-sp-downgrade-ai-spending-junk-risk ; PPC Land https://ppc.land/s-p-cuts-oracle-to-bbb-as-ai-buildout-widens-cash-deficit-to-42bn/ ; Tiger https://www.itiger.com/hans/news/2653248061 ; ChartMill(CDS) https://www.chartmill.com/news/external/85445/oracle-s-credit-risk-nears-an-18-year-high-can-ai-backlog-save-stock
- S22 弱気論・クレジット: Pepperstone https://pepperstone.com/en-gb/insights/market-analysis/shares/oracle-earnings-miss-rising-capex-weak-cash-flow-and-higher-cds-spark-investor-concerns ; Lex(Substack) https://lex.substack.com/p/ai-oracles-credit-default-swaps-and-the-ai-hedge ; MIT Sloan ME https://www.mitsloanme.com/?p=13301 ; Khaleej Times https://www.khaleejtimes.com/business/tech/oracles-openai-reliance-faces-scrutiny-as-debt-fuelled-ai-buildout-raises-worries ; ARPU https://arpu.hedder.com/oracle-is-an-openai-credit-story/ ; Seeking Alpha https://seekingalpha.com/article/4946404-oracle-openai-could-walk-away ; 2025年のカウンターパーティー論(Moody's・BNP・TD Cowen・Bernstein)は AOL https://www.aol.com/finance/oracle-made-300-billion-bet-205441205.html と IG https://www.ig.com/uk/news-and-trade-ideas/Oracle-2Q26-earnings-preview-251209 のいずれか(特定不可)
- S23 Redburn: TipRanks/TheFly https://www.tipranks.com/news/the-fly/oracle-initiated-with-a-sell-at-rothschild-co-redburn-thefly ; Motley Fool 2025-09-25 https://www.fool.com/investing/2025/09/25/why-oracle-stock-dropped-today
- S24 Axios「Why Oracle keeps sparking AI-bubble fears」 2025-12-18 https://axios.com/2025/12/18/ai-oracle-stock-blue-owl
- S25 Benzinga「Oracle Exposed to 4 Key Bubble Risks, Paul Kedrosky Warns」 2026-10(見出しのみ) https://benzinga.com/markets/prediction-markets/26/10/62273895/oracle-4-bubble-risks-converge
- S26 CNBC「Oracle stock has worst week since 2001 dot-com bust as AI financing concerns escalate」 2026-06-26 https://www.cnbc.com/2026/06/26/oracle-stock-ends-worst-week-since-2001-as-investors-dwell-on-finances.html
- S27 Q4 FY26(2026-06-10): CNBC https://www.cnbc.com/2026/06/10/oracle-orcl-q4-earnings-report-2026.html ; SEC 8-K https://www.sec.gov/Archives/edgar/data/0001341439/000119312526265848/orcl-ex99_1.htm ; Equibles https://equibles.com/stocks/orcl/calls/2026-q4 ; Pulse2 https://pulse2.com/oracle-planned-capital-raise-expands-to-40-billion/ ; Finsee https://finsee.ai/earnings/orcl/2026/q4/en/ ; moomoo https://www.moomoo.com/community/feed/oracle-q4-fy2026-earnings-conference-call-116727818420629 ; DCD https://www.datacenterdynamics.com/en/news/oracle-cloud-infrastructure-revenue-up-93-as-firms-capex-keeps-climbing/ ; HL https://www.hl.co.uk/shares/stock-market-news/company--news/archive/oracle-shares-drop-despite-record-q4-as-guidance-underwhelms ; TIKR https://www.tikr.com/blog/oracle-stock-fell-8-after-a-record-quarter-heres-why-the-selloff-may-be-overblown ; erp.today https://erp.today/oracle-q4-2026-earnings-ai-cloud-backlog-funding/
- S28 Q3 FY26(2026-03-10): MarketBeat https://www.marketbeat.com/instant-alerts/oracle-q3-earnings-call-highlights-2026-03-10/ ; Motley Fool https://www.fool.com/investing/2026/03/10/why-oracle-stock-is-ripping-higher-in-after-hours/ ; Insider Monkey https://www.insidermonkey.com/blog/oracle-corporation-nyseorcl-q3-2026-earnings-call-transcript-1714572/ ; Torre News https://torre.news/oracle-stock-spikes-9-as-strong-q3-earnings-answer-wall-street-ai-build-out-concerns
- S29 2025年12月: TIKR https://www.tikr.com/blog/oracle-nyse-orcl-stock-plunges-over-11-as-fiscal-q2-revenue-misses-estimates ; TIKR(Blue Owl) https://www.tikr.com/blog/oracle-stock-fell-5-as-blue-owl-capital-pulls-out-of-10-billion-data-center-investment ; The Register 2025-12-15 https://www.theregister.com/2025/12/15/oracle_denies_openai_delays/ ; Motley Fool 2025-12-17 https://www.fool.com/investing/2025/12/17/why-oracle-stock-is-sinking-once-again/
- S30 2026年2月の調達計画: BusinessDay 2026-02-02 https://www.businessday.co.za/world/international-companies/2026-02-02-oracle-shares-fall-as-investors-assess-ai-funding-plan ; TIKR https://www.tikr.com/blog/oracle-nyse-orcl-stock-drops-3-after-plan-to-raise-50-billion-for-cloud-expansion ; btw.media https://btw.media/en/oracle-shares-rise-after-50-billion-data-center-funding-plan
- S31 2025年9月のピーク: Motley Fool 2025-10-07 https://www.fool.com/investing/2025/10/07/why-oracle-rallied-in-september/ ; TradingView https://vn.tradingview.com/chart/ORCL/8QCnOcvu-Oracle-ORCL-Stock-Price-Pulls-Back-After-Historic-Surge
- S32 2025年11月: BondBlox https://bondblox.com/news/oracles-dollar-bonds-continue-to-slip ; Nasdaq(Motley Fool 転載)https://www.nasdaq.com/articles/heres-why-oracle-stock-got-hammered-last-month
- S33 Project Jupiter / force majeure(2026-09-24): CP24 https://www.cp24.com/news/money/2026/09/24/oracle-triggers-force-majeure-on-data-centre-project-over-power-delays-source-says ; Finviz https://finviz.com/news/395340/oracle-stock-selloff-drags-nasdaq-triple-digits ; Propmodo https://propmodo.com/power-constraints-push-oracle-to-delay-18-billion-data-center-campus/
- S34 MarketBeat 2026-09-28 https://www.marketbeat.com/instant-alerts/price-oracle-nyse-orcl-shares-down-33-heres-why-2026-09-28/
- S35 2026-10-08: TipRanks https://www.tipranks.com/news/why-oracle-stock-orcl-is-sinking-today-october-8-2026 ; Mitrade(BeInCrypto 転載)https://www.mitrade.com/insights/news/live-news/article-3-2148826-20261009 ; FX Leaders https://www.fxleaders.com/news/2026/10/08/orcl-stock-tests-136-as-project-jupiter-delays-openai-revenue-concerns-threaten-growth/ ; GuruFocus https://www.gurufocus.com/news/9116249/a-look-at-oracle-corp-orcl-after-55-decline-gf-value-19475-vs-price-13569 ; Qatar Tribune https://www.qatar-tribune.com/article/231412/business/openai-growth-stumble-report-rattles-ai-stocks
- S36 分布: MarketBeat 2026-10-10 https://www.marketbeat.com/instant-alerts/consensus-oracle-corporation-nyse-orcl-stock-has-consensus-price-target-of-25172-according-to-analysts-2026-10-10/ ; MarketBeat forecast https://www.marketbeat.com/stocks/NASDAQ/ORCL/forecast/ ; StockAnalysis https://stockanalysis.com/stocks/orcl/forecast/ ; CNN https://www.cnn.com/markets/stocks/ORCL ; WallStreetZen https://www.wallstreetzen.com/stocks/us/nyse/orcl/stock-forecast
- S37 Motley Fool / Yahoo の「ピークから○%下落」系: 2026-07-06 https://www.fool.com/investing/2026/07/06/oracle-stock-is-down-58-from-its-peak-but-revenue/ ; 2026-09-30 https://www.fool.com/investing/2026/09/30/oracle-stock-is-down-60-from-its-high-heres-why-im/ ; Yahoo https://finance.yahoo.com/markets/stocks/articles/oracle-stock-down-64-10-184600990.html ; MarketBeat 7/20 https://www.marketbeat.com/instant-alerts/oracle-nyseorcl-hits-new-52-week-low-whats-next-2026-07-20/
- S38 Morgan Stanley / 慎重論の補足: Insider Monkey「Oracle's AI Earnings Story Is Improving, but the Cash Flow Test Remains」 https://www.insidermonkey.com/blog/oracles-ai-earnings-story-is-improving-but-the-cash-flow-test-remains-1834123/

---

## 9. 未確認事項・出典間の矛盾

### 9-1. 調査していない/取得できなかったもの
1. Q&A の全文。特に、(a) OpenAI の支払能力を名指しした質問と回答、(b) 質問者の正確な氏名(Q1 FY27 の Deutsche Bank、Q3 FY26 の capex 質問者、Q1 FY27 の「追加 capex 不要」質問者)、(c) 回答の逐語。Oracle の IR サイト、Motley Fool(2026-09-11, 2026-06-10, 2026-03-10)、Benzinga(Q4 FY26)、stockanalysis.com の書き起こしを直接読む必要がある。
2. 各強気派の論点の本文(Guggenheim、UBS、Cantor、Evercore、Jefferies、Oppenheimer、JPMorgan のアナリスト名)と数値前提(売上・EPS・マージン・倍率)。
3. 弱気派: 空売り勢、著名投資家(Burry、Chanos 等)、個別の債券アナリスト、HSBC(目標引き上げの見出しのみ。日付不明)、Redburn の現在のレーティング、Seeking Alpha「OpenAI Could Walk Away」の本文、Kedrosky の2026年10月の記事の本文。
4. リバース DCF の記述、EV/EBITDA の数字、FCF 前提の明示的な数値。
5. EPS 予想修正の方向(FY27・FY28 コンセンサス EPS の推移)。
6. 2026年10月9日以降の株価(Robinhood の断片に「金曜に約5%上昇」とあるが未確認)。
7. 2025年10月〜11月上旬の個別イベントの理由(10/20 の -4.9% などは見出しのみ)、2026年2〜3月の格下げ(MarketBeat の見出しのみ)、4〜5月の動き。
8. 2025年10月のアナリスト・デーでの Oracle の長期目標(FY30)は、今回の検索では取得していない。

### 9-2. 出典間の矛盾
1. Morgan Stanley のアナリスト: Sanjit Singh とする報道と、Keith Weiss とする検索結果が混在。Weiss の記事は古い(2025年)ものしか見つからなかった。
2. BMO の Keith Bachman: Outperform・$220→$195(Benzinga)と、Market Perform・$175→$200(TipRanks/TheFly、日付不明)。
3. Q1 FY27 の株価反応: 時間外 +7%(Stocktwits)、翌日 +4.37%(Tiger)、9/11 に +2.5% で $157.18(Benzinga)。一方、「時間外 -8.9%」とする記事(Outlook Business)があるが、内容が6月の Q4 決算(約 $40B 調達、capex $95B)と一致しており、日付の混同の疑いがある。
4. Q1 FY27 の数字: capex $28.0B/$28.5B、FCF -$5B/-$5.4B、売上 $19.18B/$19.3B/$19.34B。
5. CDS の水準と時期: 198bp(Bloomberg 報道)、約 203bp(2026年7月)、約 215bp(2026年8月初め)、2026-09-24 に過去最高(1件)。同一系列の時系列に整理できていない。
6. OpenAI の RPO に占める割合: 「ほぼ半分」(S&P)、50%超(BofA、$638B 時点)、約45%($300B÷$664B)。
7. OpenAI の年率売上: 約 $50B(FT、9月末)と約 $68〜70B(従来報道)。差は収益認識の違いとの解説と、実際の不足とする見方が混在。
8. 決算日: 9/5、9/7、9/8、9/10 と事前記事で食い違う。正しいのは Oracle の発表資料にある 2026-09-10。
9. PER 76 → 22 の記述の出典と日付が特定できない。
10. Q4 FY26 の FY27 capex: 総額 $90〜95B と net $70B 以下の2つの数字が併存(定義の違いと思われるが未確認)。市場予想 $61.7B は単一出典。
11. Q1 FY27 のアナリスト数: Investing.com は「41人」としつつ内訳合計は43。
