# 全銘柄一次ふるいパイプライン仕様(Opus / 2026-10-19)

ユーザー指示: 「楽天証券の取り扱いがあるもの全部」を、足切り(構造A+・成長A+)で審査する。
対象市場: 日本(東証全上場)、米国、香港、上海A株、シンガポール、インドネシア、タイ、マレーシア。

## 構成(Python 3、標準ライブラリ+yfinance+pandas。ネットワーク許可後に動かす)
1. `universe.py` — 対象銘柄リストを作る
   - 日本: JPX の上場銘柄一覧(https://www.jpx.co.jp/markets/statistics-equities/misc/01.html の data_j.xls)。ETF・REIT・優先株を除く。ティッカーは `XXXX.T`
   - 外国: 楽天証券の取扱銘柄一覧(www.rakuten-sec.co.jp の各市場の取扱銘柄ページ/CSV)。取れない場合のフォールバックは、Yahoo のティッカー体系で
     米国(Nasdaq/NYSE の全上場)、香港 `.HK`、上海 `.SS`、シンガポール `.SI`、インドネシア `.JK`、タイ `.BK`、マレーシア `.KL`
   - 出力: `data/universe.csv`(ticker, name, market, source)
2. `fetch.py` — yfinance で各銘柄の数値を取る(キャッシュ: `data/cache/<ticker>.json`、再実行時は24時間以内のキャッシュを使う)
   - 取得項目: marketCap, currency, forwardPE, trailingPE, trailingEps, forwardEps, sector, industry, longBusinessSummary,
     earnings_estimate(0y・+1y の avg と numberOfAnalysts、yearAgoEps)、growth_estimates(+5y があれば)、revenue_estimate(0y・+1y)
   - 取得失敗は `data/errors.csv` に記録して続行。並列は最大4、1銘柄ごとに0.3〜0.6秒の待ち、429 を受けたら指数バックオフ
3. `screen.py` — 一次ふるい
   - 通貨換算して時価総額(USD)を出す(為替は yfinance の `USDJPY=X` 等で当日値)
   - EPS成長: g2 = (EPS_+1y_avg / yearAgoEps)^(1/2) − 1(実績年→翌々年度の2年CAGR)。+5y があれば併記
   - PEG = forwardPE ÷ (g2×100)
   - 一次ふるい合格: g2 ≥ 0.31、PEG ≤ 0.75、EPS(実績・予想とも)> 0、時価総額 ≥ 2億USD、アナリスト数 ≥ 1
   - 補助枠(境界): g2 ≥ 0.25 かつ PEG ≤ 0.90 → `borderline`
   - 構造の機械的な除外(業種で一次判定。人が後で見直す): Energy / Basic Materials / 銀行 / 保険 / 不動産開発 / 自動車 / 鉄鋼・化学・非鉄 /
     メモリ半導体 / 建設・重機 / 海運・航空 を `cyclical_flag=1` とし、除外ではなく印だけ付ける
   - 出力: `out/pass.csv`、`out/borderline.csv`、`out/summary.md`(市場別の件数、通過・境界の件数、上位50社の表)
4. `run_all.sh` — 1→2→3 を順に実行し、進捗と所要時間を表示

## 品質の規律
- 失敗・欠損を握りつぶさない(件数を summary に出す)
- ネットワークが無い環境でも、`--offline` で小さなモックデータ(`tests/mock/`)を使って 3 段階が通ることを確認できるようにする
- 数値の単位と通貨を列名に明記する
