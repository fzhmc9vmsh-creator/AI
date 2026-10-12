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
