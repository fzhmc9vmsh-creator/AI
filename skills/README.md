# 銘柄分析・資料作成スキル(2026-11-18 改修: 5 工程の構成)

claude.ai の「スキル」にアップロードして使う。`dist/` の zip をそのままアップロードする(既存の同名スキルを置き換える)。

| スキル | 改修の中身 |
|---|---|
| bcg-slide-method | 銘柄分析の資料を 5 工程(0 会社と業界の前提 → 1 現在の構造 → 2 将来の構造 → 3 リスク → 4 今の値段 → 5 判定と行動)で組む。設計書の検査に「説明してから使う(introduces・uses)」「用語(glossary)」「比較の設計(benchmarks)」「目標の年(horizon)」「工程ごとの必須ページ」を追加。pptx の検査に社内記号・タイトルの数字・略語の注釈を追加。部品 L.bubbleMatrix(製品ポートフォリオ・確度×影響度・リスクマトリクス)と L.termNotes(用語の注釈)。手本 c05・c06・storyline_stock_v3_anthropic.json |
| meigara-bunseki-method(第10版) | 分析側の台帳を 5 工程に合わせた: 製品ポートフォリオ × PLC × 現金の役割、現金の創出と投下と時間軸、業界・用語(business_map.json)、将来の構造・リスク・今の値段・比較の設計(outlook.json と gate.py outlook)、計算機に今の値段(今の PER・今の PEG・株価が前提にする成長率)、報告書の章立てを 5 工程に |

自己テスト: `python3 meigara-bunseki-method/scripts/selftest.py`、資料の作業フォルダで `python3 bcg-slide-method/scripts/selftest_deck.py`。
