# 資料の部品(scripts/)

ORCL 資料(2026-10)で使った部品。新しい案件では作業フォルダに写して使う。

| ファイル | 役割 |
|---|---|
| lib.js | デザインの部品(見出し帯・表・チャート・関係図 flowMap・仕組みパネル・時間軸など)。座標と色の正 |
| meta.example.js | 章・節・テーマ・なぜ・タイトル・順番の一括管理(ORCL の例)。`meta.js` に名前を変えて案件に合わせて書き換える |
| audit_deck.py | 機械監査(範囲・余白・配色・フォント・文字の収まり・重なり・改行・見出し帯・出所) |
| one.js | 1 枚だけ作って監査と画像化: `node one.js 08b` → tmp/s08b.jpg |
| build.js | meta.js の順に全スライドを組み立てる: `node build.js` |
| examples/s08b.js | 関係図の手本(事業どうしの関係)。関係図はこの密度と書き方を基準にする |

準備:
```
mkdir deck && cd deck && cp <この scripts>/* . && mv meta.example.js meta.js && mkdir -p slides tmp
npm i pptxgenjs@3.12.0      # lib.js は ./node_modules/pptxgenjs を読む
pip install python-pptx     # audit_deck.py 用
```
画像化には LibreOffice(soffice)と pdftoppm が要る。スライドは `slides/<id>.js` に `module.exports = function build(pres, L) { … }` の形で書く。
