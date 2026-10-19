# 全銘柄一次ふるいパイプライン

楽天証券で扱う銘柄を、構造A+・成長A+ の足切り(一次ふるい)で審査する。仕様は `SPEC.md`。

## 構成と実行

```
universe.py  →  fetch.py  →  screen.py        (run_all.sh が順に実行)
 銘柄リスト      数値取得      一次ふるい
```

```bash
pip install yfinance pandas xlrd openpyxl   # 依存関係(xlrd は JPX の .xls 読み込みに必要)
./run_all.sh              # 実データ(Yahoo / JPX / 楽天へ接続できる環境)
./run_all.sh --offline    # モックデータ(ネットワーク不要)
```

段階ごとに実行することもできる。`screen.py` は `data/` を読むだけでネットワークを使わない。

```bash
python3 universe.py [--offline]
python3 fetch.py [--offline] [--limit N]
python3 screen.py
```

ネットワークが拒否されている環境で `--offline` を付けずに実行すると、`check_network()` が
接続先と理由を表示して終了コード 2 で止まる。

## 出力

| ファイル | 内容 |
|---|---|
| `data/universe.csv` | ticker, name, market, source |
| `data/cache/<ticker>.json` | 銘柄ごとの取得結果(24時間以内は再取得しない) |
| `data/fx.json` | 為替。`rates[通貨]` = 1 USD あたりの現地通貨額 |
| `data/errors.csv` | 取得失敗と一部欠損の記録(fetch 段階) |
| `data/errors_universe.csv` | ユニバース段階の警告 |
| `out/pass.csv` | 合格銘柄(PEG 昇順) |
| `out/borderline.csv` | 境界銘柄(PEG 昇順) |
| `out/all_scored.csv` | 全銘柄の数値・判定・不合格/欠損の理由 |
| `out/summary.md` | 市場別件数、上位50社、不合格理由、欠損・取得失敗の一覧 |

金額の列名には単位と通貨を入れている(例: `mcap_local_mn` は現地通貨の百万単位、`mcap_usd_mn` は百万USD)。

## 判定ロジック

- EPS成長 `g2 = (EPS_+1y平均 / 実績年EPS)^(1/2) - 1`。実績年は 0y 行の `yearAgoEps`。
- PEG `= 予想PE / (g2 × 100)`
- **合格**: g2 ≥ 31% かつ PEG ≤ 0.75
- **境界**: g2 ≥ 25% かつ PEG ≤ 0.90(合格を除く)
- **共通の必須条件**: 実績EPS > 0、予想EPS(0y・+1y) > 0、時価総額 ≥ 2億USD、アナリスト数(+1y) ≥ 1
- 必須条件を満たさない銘柄は不合格。判定に必要な値が欠けている銘柄は「欠損」として別に数える。
- **循環フラグ** `cyclical_flag=1`: Energy / Basic Materials、業種に bank・insurance・auto・steel・chemical・memory・construction・shipping・airline などを含む、不動産開発。除外はせず印だけ付ける。

仕様の解釈として決めた点:
- 境界は合格と別枠で、合格銘柄も境界条件に当てはまるが `pass.csv` のみに入る。
- 境界の必須条件(EPS・時価総額・アナリスト)は合格と同じ。
- 0y 行の `yearAgoEps` を実績年EPSとして使う。基準EPS ≤ 0 の銘柄は CAGR が計算できないため不合格。

## ユニバースの作り方

- **日本**: JPX の `data_j.xls`(公開ページからリンクを抽出)。ETF・REIT・優先株を名称と市場区分のキーワードで除外する。ティッカーは `XXXX.T`。
- **米国**: `data/rakuten/US.csv`(楽天証券の取扱銘柄を保存したもの)があればそれを使う。無ければ NASDAQ Trader の全上場ファイル(Nasdaq / NYSE)を使う。
- **その他**(HK・SH・SG・ID・TH・MY): `data/rakuten/<市場>.csv` が必要。無い場合は `errors_universe.csv` に記録して飛ばす。接尾辞は HK=.HK, SH=.SS, SG=.SI, ID=.JK, TH=.BK, MY=.KL。

楽天証券の取扱銘柄 CSV の URL は確認できていないため、スクリプトは自動取得しない。
ブラウザで保存した CSV を `data/rakuten/<市場>.csv` に置く。列名はコードと名称を自動判定する(コード列: コード/code/symbol、名称列: 名/name)。

## モックデータ(`tests/mock/`)

架空の値。`raw/<ticker>.json` が yfinance の出力の代わり、`universe_mock.csv` が銘柄一覧、`fx.json` が為替。

| 区分 | 銘柄 |
|---|---|
| 合格 | 9001.T, 9003.T(循環), 9011.T(循環・メモリ), 9012.T(循環・銀行), 8001.HK, MOCKA, MOCKC(循環) |
| 境界 | 9002.T(PEG 0.80), 9004.T(循環・g2 27%), 8003.HK(PEG 0.88), MOCKB(g2 26%), MOCKE(循環・g2 29%) |
| 不合格 | 9005.T(成長不足), 9006.T(赤字), 9008.T(時価総額 < 2億USD), 9009.T(アナリスト0), 9013.T(PEG 1.2), MOCKD(赤字) |
| 欠損 | 9007.T(予想PEなし), 8002.HK(アナリスト数なし) |
| 取得失敗 | 9010.T(モックで HTTP 404 を模擬) |

`--offline` の実行結果の例は `out/summary.md` を参照。

## 注意と未検証の点

- **実データ経路は未検証**。この作業環境では Yahoo・JPX・楽天証券への接続が拒否されたため、オンライン経路は一度も実行していない。特に次の点は実機で確認すること: JPX ページの `data_j.xls` リンクの抽出、yfinance の `earnings_estimate` / `growth_estimates` / `revenue_estimate` の列名、NASDAQ Trader ファイルの解析。
- 為替は取得時点の値を使う(`data/fx.json` の `as_of` を参照)。
- 循環フラグは業種名による機械的判定。メモリ半導体などは人が個別に見直すこと。
- 429 応答は指数バックオフで最大 5 回再試行する。並列は最大 4、1銘柄ごとに 0.3〜0.6 秒待つ。
