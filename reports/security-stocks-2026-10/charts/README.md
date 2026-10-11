# 図表ツールキット(chartkit)

投資分析報告書(Word 埋め込み用)の PNG を描くツールキット。`charts/chartkit.py` を import して使う。

```python
import sys; sys.path.insert(0, "/home/user/AI/reports/security-stocks-2026-10/charts")
import chartkit as ck
```

依存: python3、matplotlib、numpy(PIL があれば PNG を RGB・dpi メタデータ付きに保存)。pandas は不要(DataFrame も渡せる)。

## 出力の共通仕様

- PNG、幅 **1260px = 16cm 相当 × dpi 200**、白背景、高さは図ごとに自動(`height=` で上書き可)。Word には `Cm(16)` 幅で貼ると原寸になる(dpi メタデータ入り)。
- 日本語フォントは IPAGothic(`/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf`)を明示登録。IPAGothic に無い字(`≤` `≥`)は使わず「以下」「超」と書く。`$` は数式扱いしない設定済み。
- 配色は dataviz スキルの検証済みパレット(blue `#2a78d6`、orange `#eb6834`、aqua `#1baf7a`)。**色は実体に固定**: コンセンサス=青(●)、会社シナリオ=橙(■)、事業エンジン=緑(◆)、弱気=無彩色(▼)。弱気を4色目の hue にしないのは、重なる図では4色目(黄)が橙と見分けにくい(3色までが全組合せ検証済み)ため。形(●■◆▼)でも区別でき、色だけに頼らない。
- 予測・延長は実績と区別: **破線・白抜きマーカー・薄い帯**(F13 の `is_extension=1`、F10 の予測期)。
- 系列は最大4本。F10 は5本以上なら小さい順に「その他」(無彩色)へ畳む。F18 は KPI を最大4パネル。
- すべての図の下に **「単位 / 期間 / 出所」** を小さく注記する。`period=` を省略すると CSV から自動で入る。**`source=` は必ず渡す**(省略すると `DEFAULT_SOURCE` の汎用文になる)。全図の既定は `ck.set_default_source("出所: 各社IR、TradingView(2026-10-09取得)")` で変更できる。
- 共通キーワード引数(全関数): `unit=`、`period=`、`source=`、`subtitle=`(タイトル下の1行)、`fictional=True`(「架空データ」の透かしと注記。試験専用)、`height=`(インチ)。
- タイトルは「主張を含む完全文」で渡す(1〜2行に自動折り返し)。
- 入力は CSV パスのほか、dict のリスト・DataFrame でもよい。比率は小数(0.25=25%)。値が欠損(空欄・NA)の点は飛ばす。必須列が無ければ日本語のエラーで止まる。

## 関数

### `plot_f13(csv_path, out_png, title, price_now, *, price_label=None, ...)` 年度別適正株価パス
CSV 列: `fy_end,path,business_eps,g_3y,peg_low,peg_high,fair_per_low,fair_per_high,fair_price_low,fair_price_high,is_extension`

- 描画に使う列は `fy_end`(`2027-07-31` 形式。「2027年\n7月期」と表示)、`path`、`fair_price_low`、`fair_price_high`、`is_extension`。他の列は読まれるだけ(欠けていてもよい)。
- `path` は `consensus` / `company` / `engine` / `bear`(日本語名「コンセンサス」「会社シナリオ」「事業エンジン」「弱気」も可)。
- 各経路を `fair_price_low〜high` の帯+中央線(=low と high の平均)で描き、現在株価(`price_now`)を黒の水平線で示す。右余白に各経路の最終年度の中央値を直接ラベル(衝突時は引き出し線)。`is_extension=1` の年度は破線・白抜き・薄い帯。
- 必要なら `price_label="現在株価 $300(2026-10-09終値)"` で水平線のラベルを差し替える。

```python
ck.plot_f13("analysis/PANW_F13.csv", "charts/PANW_F13.png",
            "PANW:年度別適正株価は2029年7月期までに現在株価を上回る",
            price_now=187.5, price_label="現在株価 $187.5", source="出所: Opus 分析(valuation_lib)、TradingView コンセンサス(2026-10-09取得)")
```

### `plot_f18(csv_path, out_png, title, *, ratio=True, ...)` 根幹KPIの加速度
CSV 列: `kpi,period,value,qoq_annualized,ttm_yoy,second_diff`

- `kpi` ごとに小パネル(最大4。5個以上なら先頭4個と警告)。**棒=`ttm_yoy`(前年比)、折れ線=`qoq_annualized`(前期比年率)**。同じ単位(%)なので1軸。パネルごとに縦軸は別。
- パネル見出しに最新期の前年比・前期比年率・加速度(▲加速/▼減速、`second_diff` を pt 表示)。**`second_diff` は `ttm_yoy` の前期差(成長率の変化)で、`ttm_yoy` と同じ単位**を想定。`value`(KPI の水準)は描かない。
- `ratio=True`(既定): 値は小数。既に % 単位なら `ratio=False`。行は古い期から新しい期の順に並べる。

### `plot_f10(csv_path, out_png, title, ...)` 収益ミックスの時系列
CSV 列: `period,line,revenue_usd_mn`(任意: `is_forecast`)

- 積み上げ棒(2px 相当の白い隙間)+各期の合計ラベル。最終期の帯内に構成比(収まる場合のみ)。積み上げ順・色の順は `line` の初出順(下から上。大きいラインを先に書く)。
- 予測期は薄い色: `is_forecast=1`、または `period` が `E` / `予` で終わる(例 `2027Q3E`)。
- 単位は百万USD(`unit=` で変更可)。

### `plot_f7(summary_json_path, out_png, title, ...)` エントリー価格ゾーン
`analysis/{T}_summary.json`(または同じ構造の dict)から `price`、`price_date`、`entry_zones`(`Z1`,`Z2`,`zone`)、`targets_12m`(`consensus`,`company`,`engine`,`bear`)を使う。

- 上段の帯が「即エントリー圏(Z1以下)」「分割エントリー圏(Z1〜Z2)」「見送り圏(Z2超)」(緑・黄・灰の淡色+文字ラベル)。下段に現在株価と4つの目標株価を行ごとのマーカーで載せ、現在株価からの乖離率を併記。
- **`Z1` が null なら即エントリー圏を描かず**、分割エントリー圏を左端〜Z2 とし、サブタイトルに「Z1 は算定対象外」と出す。`Z2` も null ならゾーン帯なし(「エントリー圏の算定なし」)。null/欠損の目標は行ごと省く。
- `entry_zones.zone`(現在の判定)をサブタイトルに自動表示(`subtitle=` で上書き可)。

### 横比較(rows は dict のリスト。キー名は引数で変更可)

| 関数 | 既定の rows キー | 内容 |
|---|---|---|
| `plot_scatter_growth_valuation(rows, out_png, title, *, y_key="per", x_key="growth", x_label=..., y_label=None, ratio=True)` | `name`, `growth`, `per`, `peg` | x=成長率(%)、y=PER(`y_key="per"`)または PEG(`y_key="peg"`、PEG=1 の線つき)。点に銘柄名(重ならないよう自動配置)。y が欠損・0以下の銘柄は非表示にして注記。 |
| `plot_ranking_bars(rows, out_png, title, *, value_key="expected_return", decision_key="decision")` | `name`, `expected_return`, `decision` | 期待リターンの横棒、降順、0線。正=青・負=赤(発散配色)。`decision` があれば右端に「最終判断」列。 |
| `plot_rule40(rows, out_png, title, *, growth_key="revenue_growth", margin_key="fcf_margin")` | `name`, `revenue_growth`, `fcf_margin` | 売上成長率(青)+FCFマージン(橙)の積み上げ横棒、合計の降順、40%の基準線。FCF が負なら 0 から左へ描き、合計は両者の和。 |
| `plot_sbc_vs_eps(rows, out_png, title, *, adj_key="adj_eps", biz_key="business_eps")` | `name`, `adj_eps`, `business_eps` | 調整後EPS(青)と事業実態EPS(橙)の並び棒。銘柄名の下に「事業実態÷調整後」の比率。負の EPS も可。 |

名前は `name`(無ければ `ticker`)を使う。

```python
rows = [dict(name="PANW", growth=0.22, per=48.0, peg=2.2, expected_return=0.11, decision="買い検討",
             revenue_growth=0.15, fcf_margin=0.38, adj_eps=3.9, business_eps=3.1), ...]
ck.plot_scatter_growth_valuation(rows, "charts/X_scatter_peg.png", "…", y_key="peg",
                                 x_label="事業実態EPSの3年CAGR(%)", source="出所: …")
ck.plot_ranking_bars(rows, "charts/X_ranking.png", "…", source="出所: …")
ck.plot_rule40(rows, "charts/X_rule40.png", "…", source="出所: …")
ck.plot_sbc_vs_eps(rows, "charts/X_sbc_vs_eps.png", "…", period="次期(FY+1)", source="出所: …")
```

## 試験

`python3 charts/_test/run_tests.py` で、架空データ(銘柄A〜F、すべて「架空」と注記・透かし入り)から `charts/_test/*.png`(全関数+端ケース: 経路欠損・KPI 1/3個・Z1/Z2 null・5ライン畳み込み・予測期・PER 欠損・判断なし)を出力する。入力 CSV/JSON は `_test/data/`。試験 PNG は報告書に使わない。

## 実装メモ(dataviz スキルとの対応)

- 検証: `validate_palette.js` で blue/orange/aqua の3色は全組合せ(`--pairs all`)で CVD ΔE 9.2 以上・通常視 24.0 以上で合格。無彩色の弱気を足した4本でも CVD・通常視の床は合格(chroma 床だけ「灰色」ゆえ不合格=意図どおり)。aqua は白地でコントラスト 2.8:1 のため、ラベル・凡例・形で補う(relief rule)。
- 二重軸なし(F18 は同単位の % を1軸)。グリッドは実線のヘアライン。数値は全点に付けず、末端・合計・最終期に限る。文字は系列色にせず、色は隣のマークで伝える。
- 棒の角丸(4px)は未実装(matplotlib の標準棒を使用)。
