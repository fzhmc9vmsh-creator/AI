# 手本: 東邦化学工業(4409)、2027年3月期第2四半期の決算後

| ファイル | 中身 |
|---|---|
| series.json → lenses.json・lenses.md | 時系列の入力と、`lenses.py` が出した示唆の種(17 本のレンズの復元した量と旗) |
| hypotheses.json | 着手の宣言、調査の波 0〜5、仮説 15 個(棄却・一部・立て直しつき)、**示唆のカード 7 個(深さ 2〜5。深さ 4 以上が 5 個、深さ 5 が 2 個)**、**投資仮説 thesis**(一文・差分の表 4 行・価値の芯・撤回の線 3 本・判断)、**弱気の反論 8 個**(逆 2・正しい 2・一部 3・未決 1。正しい反論で定常 ROE を下げ、判断が買い→買い検討に変わった) |
| business_map.json | 製品群の地図(15 品目)と、バリューチェーン 2 本 |
| change_map.json | 変化の評価表(15 項目を過去・現在・将来で対比) |
| valuation.json | 計算機の出力(thesis の芯の感応度・判断・理論株価の照合に使う) |
| facts.json | 上のファイルが根拠に使う台帳の行だけを抜き出したもの(全体は約 650 行) |

読み方: まず hypotheses.json の `thesis` と `insights`(深さ 4・5 のカード)を読み、次に `rebuttals` の `reflected` を読む。誤りと立て直しの経過は references/analysis-playbook.md §9。
検査: `python3 scripts/gate.py hypotheses examples/toho4409`・`map`・`change`・`lenses`・`thesis` が PASS する。
