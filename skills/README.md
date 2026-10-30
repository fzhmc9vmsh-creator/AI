# アップロード用のスキル

このフォルダの `*.skill`(zip)は、claude.ai のアカウントにアップロードするための配布版です。
編集の正はリポジトリの `.claude/skills/`(このリポジトリを開いたセッションでは自動で読み込まれる)。

| ファイル | 中身 |
|---|---|
| meigara-bunseki-method.skill | 銘柄分析メソッド |
| invest-consulting-deck.skill | 投資資料のパワポ(第2版の必須事項と部品 scripts/ を含む) |
| bcg-slide-method.skill | スライドの一般規範(references は代替版) |

アカウントの同名スキルを置き換えるには、claude.ai の設定 → Skills から各 .skill をアップロードする(セッションの中からは書き換えられない)。
