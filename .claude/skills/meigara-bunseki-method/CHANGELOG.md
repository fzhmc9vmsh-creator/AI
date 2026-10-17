# 改訂履歴(2026-10-17 第4.4版)— ORCL 資料への指摘を反映(経営者の評価・資料の型)

| 指摘 | 実際に起きた失敗 | 反映先 |
|---|---|---|
| CEO は経歴からその事業への経験等に鑑み経営能力を図る | 就任後の数字(capex の超過・報酬の設計)だけで評価し、誰が何を築いた人かを調べなかった | condition-guide 条件5(経歴台帳 → 事業との適合 → CEO の実績 → 規律) |
| 事業理解の根源を 1 枚で済ませた。新出の用語に注釈がない | 5W1H の表 1 枚だけ | report-design §1-16、§2 F24〜F26 |
| 会社の持つシナリオ・ストーリーの図がない | 採点表だけ | report-design §1-17、§2 F23(必須) |
| 関係図の配置・粒度・深さが足りない | 自社を 1 箱にした 5 箱の図、数量なし | report-design §1-18、invest-consulting-deck references/deck-rules-v2.md §3 |
| スキルを次回から違うセッションでも使えるように | 同期フォルダの編集は保存されない | リポジトリの .claude/skills/ に置き、CLAUDE.md で優先を明記。配布用は skills/*.skill |

# 改訂履歴(2026-10-16 第4.2版)— 品質確認(独立の監査と反証)で見つかった誤りを反映

| 見つかった誤り | 影響 | 反映先 |
|---|---|---|
| 非GAAP EPS に GAAP 基準の同業 PER を掛けた | 理論株価 +14 の過大 | growth-and-capex-valuation §11-1 |
| 借入で自社株を買い、株数を減らさなかった | EPS の延長と PEG 経路が歪む | §11-2 |
| 倒産確率を DCF 経路にしか掛けなかった | +12 の過大 | §11-3 |
| シナリオごとに同業 PER・PEG も動かした | 成長の二重計上 | §11-4 |
| エンジンの倍率をコンセンサス EPS に掛けた | FY29〜30 で約 10% 膨張 | §11-5 |
| 初年度の capex が会社ガイダンスを超えていた | FCF・格付けの経路が悪化 | §11-6 |
| 弱気で計画外の敷地の賃料を計上していた | 弱気 DCF が約 3 割過小 | §11-7 |
| 市場の暗黙確率を1つの定義で書いた | 頑健でない主張 | §11-8 |

# 改訂履歴(2026-10-15 第4版)— Oracle 第3版・第4版の評価への指摘を反映

| 指摘 | 実際に起きた失敗 | 反映先 |
|---|---|---|
| EPS・売上・営業利益の予想は TradingView から拾い、需給で検証して成長率に反映せよ | 自分のエンジンで EPS を作り、コンセンサスとの照合をしなかった | growth-and-capex-valuation §10-1 |
| 遠い未来は分からないので、FY35 など確度の低い予測の比重を軽くせよ | FY90 までの DCF を主評価にした | §10-2・3 |
| 弱気2つに強気1つは偏り | 片側だけに裾のシナリオを置いた | §10-4 |
| FY29→32 の伸びが低すぎる。逼迫から考えればありえない | 容量の追加が減る理由(電力・資金)を示さず、需要の減速と区別しなかった | §10-8 |
| SaaS の伸びは後半に大きくなる。製品の特性を見よ | 直近の伸びを延長した | §10-5 |
| (自己点検)PEG 経路が低成長で 0 倍に潰れる | 弱気の PER を不当に下げた | §10-7 |
| 市場との差分を確率だけで書いた | 市場の暗黙の PER と自分の経路を並べなかった | §10-6・9 |

# 改訂履歴(2026-10-12 第2版)— Oracle 第2版の評価への指摘を反映

## 1. 指摘と、分析で実際に起きた失敗

| 指摘 | 実際に起きた失敗(Oracle 第2版の評価) | 反映先 |
|---|---|---|
| AI クラウドの価値を低く見積もりすぎ。AWS も設備投資先行型だが今は超高収益 | AI 事業を「GPU の時間貸し」とみなし、AWS のように設備先行の後に高収益化する道筋を検討しなかった | 核心原則12・13、growth-and-capex-valuation §1・§4、business-core A21 |
| 今の粗利率と将来の粗利率は分けて捉える。古い GPU の再契約で値段が上がることも含め、将来の粗利率を深く考える。最終的には営業利益率で見る | 1GW あたり単価を横ばい、GPU を6年で残存価値ゼロにし、立ち上げ途中の粗利率を定常とみなした | 核心原則12、growth-and-capex-valuation §1・§2、business-core A19・A20 |
| 営業利益率は今より悪化するのか、なぜか | 全社営業利益率の経路を、構成比の効果と事業内の効果に分けて説明しなかった | growth-and-capex-valuation §7、business-core A23 |
| 金利は今後下がるのか上がるのか、いつか。割引率はそこから考える | 無リスク金利を 4.3% の固定値にした | 核心原則14、growth-and-capex-valuation §5、business-core A22 |
| 税引後営業利益で 19倍? 減価償却費は将来のキャッシュアウトではない。継続する事業に償却込みで見るのはどこまで正しい? ルール・オブ・40 は? | 立ち上げ途中の年度の NOPAT に倍率を当てて「19倍」と書いた。会計の償却と経済的な維持投資を比べなかった | growth-and-capex-valuation §3・§6、business-core A19 |
| バリューチェーン・競争優位・参入障壁・ファイブフォース・業界全体(DC の建設難易度・期間・量)・値下げ圧力・競争環境から倍率を導けるのか | 産業構造の数値から利益率と CAP を導かなかった。SaaS の現金で長期契約を引き受けられる優位を数値にしなかった | 核心原則13、growth-and-capex-valuation §4、business-core A21・A24 |
| Database@ は今後急拡大する | 採用曲線を置いたが、提携先の需要・移行倍率・AI 利用の根拠が薄かった | product-and-pnl-flow §4 の運用(追加調査)、growth-and-capex-valuation §2 の考え方を F22 にも適用 |

## 2. 新設したファイル
- `references/growth-and-capex-valuation.md`

## 3. 注意(指摘への補足として本スキルが採る立場)
- 減価償却は現金の支出ではないが、事業を続けるための維持投資の代理である。問うべきは「会計上の償却が経済的な維持費用と
  一致しているか」であり、償却を無視することではない(growth-and-capex-valuation §3)。
- ルール・オブ・40 は SaaS の経験則である。設備型には、成長投資と維持投資を分けたオーナー利益率で当てはめる(同 §6)。

---

# 改訂履歴(2026-10-12)— Oracle 分析への指摘を反映

## 1. 指摘と、分析で実際に起きた失敗

| 指摘 | 実際に起きた失敗(Oracle 報告書 2026-10-11) | 反映先 |
|---|---|---|
| PER15倍は日本企業の平均。事業と PER の相場を理解していない | 20%超で EPS が伸びる企業に PER 下限14倍・PEG 0.8〜0.95 を当て、成熟年度を日本平均並みにした | 核心原則9、intrinsic-valuation-credit §2・§5、valuation-model §3-3・§3-4、business-core A12 |
| 現在の株価に引っ張られすぎ。株価との整合ではなく、利益やリスクから逆算する | 逆算値を見てからコアの資本コストを選び、「株価と整合」を結論の根拠にした | 核心原則8、intrinsic-valuation-credit §1、SKILL Phase 5(事前登録)・Phase 6、business-core A11 |
| (同上から導いた規律)| 資本集約度を SOTP の capex 控除と PEG の割引で二重に数えた | 核心原則10、intrinsic-valuation-credit §3、business-core A13 |
| CF の黒字化位置と、それに伴う倒産確率の低減 | FCF・レバレッジ・倒産確率の経路を推計せず、低い PEG で代用した | intrinsic-valuation-credit §4(F21)、research-protocol L、business-core A17 |
| 5W1H で商品・サービスを分析する | エンジンの粒度でしか見ず、製品・顧客・用途・価格の台帳がなかった | 核心原則11、SKILL Phase 1.3、product-and-pnl-flow §1(L0)、business-core A14 |
| 画像(Palantir・Micron)のような収益分析 | 損益をセグメント→原価→粗利→営業費内訳→営業利益→営業外→税→純利益の流れで、前年比つきで見なかった | product-and-pnl-flow §2(F19)、research-protocol J、business-core A15 |
| 競合に対する優位を、サービスの質や価格の背景にあるバリューチェーンから分析する | 優位を 7 Powers の言葉で済ませ、品質と価格の比較と、それを支える活動を示さなかった | product-and-pnl-flow §3(F20)、business-core L7・A16、research-protocol K |
| AI を Oracle Database 上で動かす @(Database@AWS/Azure/Google)の事業価値 | 戦略施策を機構台帳の小さな1行(+$3.5)で済ませ、事業価値を試算しなかった | product-and-pnl-flow §4(F22)、SKILL Phase 2.7、business-core A18 |

## 2. 新設したファイル
- `references/intrinsic-valuation-credit.md`(valuation-model.md より優先)
- `references/product-and-pnl-flow.md`

## 3. 図表の追加
F19 損益フロー図(サンキー)、F20 品質×価格×バリューチェーン、F21 FCF・レバレッジ・倒産確率の経路、F22 戦略施策の事業価値。

---

# 改訂履歴(2026-10-11)

## 1. 参照ファイルの復元

原本の references/ 7本は消失していたため、次から復元した。
- 13条件の文言・S〜F評価スケール: invest-consulting-deck/references/stock-analysis.md
- 各ファイルの節構成・要件: 改訂前SKILL.mdの記述(Phase 1〜7の説明と品質ゲート)
- 図表の描き方: invest-consulting-deck/references/design-spec.md(T15〜T18)

【再設計】と印のある式・閾値は原本が残っておらず、復元時に設計したもの。
主なもの: 構造評価→許容PEGの出発点表、gが50%超の扱い、2軸マトリクスの境界、
エントリー3ゾーンの式とα、4フェーズの撤退条件。

## 2. 要求の対応表(この改訂を求めた会話での要求 → 反映先)

| 要求 | 反映先 |
|---|---|
| 収益構造の分析 | business-core L2・L3、structure-map-method §1 |
| 取引先依存度 | business-core L4(確率×影響−代替需要) |
| サイクル | business-core L4(サイクルの位置の判定)、§8 G |
| 売上の質 | business-core L4(需要の層・受注残の質)、L6 |
| 利益の質 | valuation-model §3-0・§3-1、business-core §5-2・§5-4 |
| CFの質 | business-core §5(確認層、FCFの3定義) |
| CF上のリスク | business-core §6(義務台帳、効果測定) |
| 楽観にも悲観にも偏らない分析 | business-core §1・§2、scenario-strategy §3(対称プレモーテム・参照クラス) |
| 株価に惑わされない理論株価 | valuation-model §3(事業実態EPS、4経路、許容PEG、成長の値段、リバースDCF) |
| 経営陣の優秀さ | business-core L9(仕組みづくり、ガイダンス達成率、言行一致、資本配分の効果、開示の読解) |
| タイツさん・五月さん・リンチ・会計専門家・大島さんの視点 | business-core §11 |
| 下振れ一辺倒の是正 | SKILL.md 核心原則3、business-core §2(A1・A8) |
| 目的は割安な優良企業の見極め | SKILL.md 核心原則1 |
| 販促なしのクロスセル・アップセル | business-core L2(増収の源泉分解、低コスト拡張の証拠) |
| 顧客単価・顧客数の伸び | business-core L2(エンジン式、ユニットエコノミクス) |
| 会計上の減耗と実際の減耗の乖離 | business-core L5、valuation-model §3-1 |
| 資産の外部化はROEを上げる工夫 | business-core L5、structure-thinking §2 |
| 旧世代GPUの高値での再契約 | business-core L5(更新時単価÷初回単価) |
| フローとストックの両輪 | business-core L6、L2(収益の多重性)、structure-thinking §2 |
| 評価の基準はビジネス、CFは確認 | SKILL.md 核心原則2、business-core §5 |
| MoM・TTM・YoYの改善 | business-core L10、research-protocol §1-C |
| 希薄化は影響で判断(5%希薄化でEPS成長+10pt) | business-core §6 |
| 破綻リスクも影響で判断 | business-core §6 |
| 市場の仮説の質を上回る | business-core §4・§3A |
| 制約の特定 | business-core L3 |
| 既存スキルの編集 | SKILL.md |

## 3. 採用しなかった提案

- 「PEGを適用条件付きのクロスチェックに格下げ」(事前調査の提案): 採用せず。PEG×EPSの枠組みは
  維持し、代わりに基準EPSを事業実態EPSにし、業種別の交差確認と成長の値段を加えた。

## 4. 変更したユーザー既定のルール

- Phase 3「迷ったら1段階低い方に倒す」→「迷ったら評価を動かさず、決め手の証拠を特定して
  追加調査。決まらなければ保留+確認KPI」。戻す場合はSKILL.md Phase 3とbusiness-core §2 A8を修正。
