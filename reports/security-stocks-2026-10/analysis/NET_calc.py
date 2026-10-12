"""Cloudflare(NET)の計算スクリプト。報告書 analysis/NET_report.md の数値はすべてこの出力と一致させる。

規約: 00_standard.md(§3 事業実態EPS、§3-1 株数、§3-2 定常状態経由の目標株価、§4 時間とバリュエーション)、
valuation-model.md、scenario-strategy.md §6。共通関数は build/valuation_lib.py。
取得日はすべて 2026-10-11。金額は US$ mn(明記がない限り)、株価・EPS は US$。
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import math
import sys

sys.path.insert(0, '/home/user/AI/reports/security-stocks-2026-10/build')
import valuation_lib as vl  # noqa: E402

OUT = '/home/user/AI/reports/security-stocks-2026-10/analysis'
P = print

# ---------------------------------------------------------------- 0. 基本入力
PRICE = 360.93            # 2026-10-09 終値(peer_peg_table.md、3出典一致)
SH_NOW = 374.0            # 現在の希薄化後株数(百万)。Q3 2026 ガイダンスの加重平均株数 約374M(Q2 2026 決算 8-K、Tier1)
SH_BASIC = 355.931        # 2026-06-30 の A+B 発行済株数(Q2 2026 10-Q、Tier1)
TAX = 0.22                # 共通基準の t。Q2 2026 の non-GAAP 純利益107.8 と営業利益96.1 から逆算した実効税率も約22%(下で検算)
SH_G = 0.02               # コンセンサス前提の株数の年増加率(非GAAP希薄化後株数 2024 約359M → 2026 約374M、年2.1%)
R = vl.COST_OF_CAPITAL
YIELD = 0.036             # 手元資金の利回り(仮定。Q2 2026 の逆算は年約4.0%)。感応度は §9
MCAP = PRICE * SH_NOW     # 希薄化後時価総額(百万ドル)

# 現金と転換社債(2026-06-30 は Tier1。8月の 2031 年債発行と 2026 年債の満期は推定を含む)
CASH_0630 = 4162.8
NOTES_2026 = 1293.75      # 2026-08-15 満期。元本は現金決済、超過分は株式と仮定(決済方法は未確認)
NOTES_2030 = 2000.0       # 転換価格 247.67、キャップ 469.73(8.1M株をカバー)
NOTES_2031 = 2175.0       # 転換価格 496.94、キャップ 854.12。手取り約2,140、キャップドコール 225.8
CASH_POST = CASH_0630 + (2140.0 - 225.8) - NOTES_2026 + 60.0   # 60 = 2026年7〜9月のFCFの仮定(下期は設備投資が集中)
NET_CASH = CASH_POST - NOTES_2030 - NOTES_2031
EV = MCAP - NET_CASH

# ---------------------------------------------------------------- 1. 四半期データ(検証済み)
Q = ['2024Q1', '2024Q2', '2024Q3', '2024Q4', '2025Q1', '2025Q2', '2025Q3', '2025Q4', '2026Q1', '2026Q2']
REV = dict(zip(Q, [378.6, 401.0, 430.1, 459.9, 479.1, 512.3, 562.0, 614.5, 639.8, 696.1]))
NG_OPI = dict(zip(Q, [42.4, 57.0, 63.5, 67.2, 56.0, 72.3, 85.9, 89.6, 73.1, 96.1]))
NG_EPS = dict(zip(Q, [0.16, 0.20, 0.20, 0.19, 0.16, 0.21, 0.28, 0.28, 0.25, 0.29]))   # 2026Q1 は 0.25(会社発表。Haiku表の0.27を訂正)
FCF = dict(zip(Q, [35.6, 38.3, 45.3, 47.7, 52.9, 33.3, 75.0, 99.4, 84.1, 56.4]))
# DNR(ドルベース純維持率): 10-Q/10-K の会社開示
DNR = {'2023Q4': 115, '2024Q1': 115, '2024Q2': 112, '2024Q3': 110, '2024Q4': 111, '2025Q1': 111, '2025Q2': 114,
       '2025Q3': 119, '2025Q4': 120, '2026Q1': 118, '2026Q2': 120}
DNR_OLD = {'2021Q4': 125, '2022Q1': 127, '2022Q4': 122, '2023Q1': 117, '2023Q2': 115, '2023Q3': 116}
LARGE = {'2021Q4': 1416, '2022Q4': 2042, '2023Q4': 2756, '2024Q4': 3497, '2025Q1': 3527, '2025Q2': 3712,
         '2025Q3': 4009, '2025Q4': 4298, '2026Q1': 4416, '2026Q2': 4698}
LARGE_SHARE = {'2024Q3': 0.67, '2025Q2': 0.71, '2025Q3': 0.73, '2026Q2': 0.73}   # 大口顧客の売上比率(会社・説明会)
CRPO_YOY = {'2025Q3': 0.30, '2025Q4': 0.34, '2026Q1': 0.34, '2026Q2': 0.35}
NG_GM = {'2024Q1': 0.795, '2024Q4': 0.776, '2025Q2': 0.763, '2025Q3': 0.753, '2025Q4': 0.749, '2026Q1': 0.728, '2026Q2': 0.731}
# SBC+関連給与税(調整後EPSから除外されている額): Q2 2026 140.6 / Q2 2025 132.0 / 6M 2026 268.05 / 6M 2025 237.9 / FY2025 489.9 / FY2024 356.4
SBCPT = {'2025Q1': 237.888 - 131.993, '2025Q2': 131.993, '2025H2': 489.9 - 237.888, '2026Q1': 268.050 - 140.593, '2026Q2': 140.593}
SBC_EXPT = {'2024': 338.5, '2025': 451.5, '2025Q1': 95.5, '2026Q1': 114.2}   # 給与税を除く SBC
FY_REV = {2023: 1296.7, 2024: 1669.6, 2025: 2167.9}
FY_NGOPI = {2024: 230.1, 2025: 303.8}
FY_NGNI = {2024: 269.0, 2025: 342.9}
FY_NGEPS = {2024: 0.75, 2025: 0.93}
FY_SBCPT = {2024: 356.4, 2025: 489.9}
FY_FCF = {2024: 166.9, 2025: 260.6}
FY_CAPEX = {2024: 213.5, 2025: 342.5}
FY_OCF = {2024: 380.4, 2025: 603.1}

GUIDE_2026 = dict(rev=(2864, 2870), opi=(443, 445), eps=(1.25, 1.26), sh=374)
GUIDE_Q3 = dict(rev=(736, 737), opi=(129, 130), eps=0.34)


def yoy(d, q, lag=4):
    i = Q.index(q)
    return d[q] / d[Q[i - lag]] - 1 if i >= lag else None


def sec(t):
    P('\n' + '=' * 100 + f'\n{t}\n' + '=' * 100)


sec('0. 基本入力と検算')
P(f'株価 {PRICE} / 希薄化後株数 {SH_NOW}M / 時価総額(希薄化後) {MCAP/1000:.1f}bn / 基本株数ベース {PRICE*SH_BASIC/1000:.1f}bn')
P(f'2026年8月の取引後の現金・投資(推定) {CASH_POST:,.0f} / 転換社債元本 {NOTES_2030+NOTES_2031:,.0f} / ネットキャッシュ {NET_CASH:,.0f} / EV {EV/1000:.1f}bn')
q2_int = 107.8 / (1 - TAX) - 96.1
P(f'Q2 2026: non-GAAP NI 107.8 = (営業利益96.1 + 受取利息等 I)×(1−22%) → I = {q2_int:.1f}/四半期(年率 {q2_int*4:.0f}、資金4.1bnに対し {q2_int*4/4100:.1%})')
P(f'  → 調整後EPSのうち受取利息の寄与(2026年、税引後): 約 {170*(1-TAX)/SH_NOW:.2f} ドル/株(調整後EPS 1.26 の {170*(1-TAX)/SH_NOW/1.26:.0%})')
P(f'Q2 2026 非GAAP希薄化後株数の逆算: 107.8/0.29 = {107.8/0.29:.0f}M(EPS丸めで ±7M)')
P(f'金利1pt低下の調整後EPSへの影響: 手元資金 {CASH_POST:,.0f} × 1% × (1−22%) ÷ {SH_NOW}M = −{CASH_POST*0.01*(1-TAX)/SH_NOW:.2f} ドル/株')

# ---------------------------------------------------------------- 2. 加速度表(F18)とエンジン照合
sec('1. 根幹KPIの加速度(F18)')
rows18 = []
prev_yoy = None
for q in Q:
    i = Q.index(q)
    qoq = (REV[q] / REV[Q[i - 1]]) ** 4 - 1 if i >= 1 else None
    y = yoy(REV, q)
    ttm = None
    if i >= 7:
        ttm = sum(REV[x] for x in Q[i - 3:i + 1]) / sum(REV[x] for x in Q[i - 7:i - 3]) - 1
    sd = (y - prev_yoy) if (y is not None and prev_yoy is not None) else None
    rows18.append(('売上(四半期, 百万ドル)', q, REV[q], qoq, ttm, sd))
    if y is not None:
        rows18.append(('売上前年比(四半期)', q, round(y, 4), None, None, sd))
    if y is not None:
        prev_yoy = y
    P(f'{q} 売上 {REV[q]:7.1f}  QoQ年率 {qoq if qoq is None else f"{qoq:6.1%}"}  YoY {y if y is None else f"{y:6.1%}"}  TTM YoY {ttm if ttm is None else f"{ttm:6.1%}"}  2階差分 {sd if sd is None else f"{sd*100:+.1f}pt"}')

dq = list(DNR.keys())
prev = None
for k in dq:
    i = dq.index(k)
    qoqd = DNR[k] - DNR[dq[i - 1]] if i >= 1 else None
    yoyd = DNR[k] - DNR[dq[i - 4]] if i >= 4 else None
    sd = (yoyd - prev) if (yoyd is not None and prev is not None) else None
    rows18.append(('DNR(%)', k, DNR[k], qoqd, yoyd, sd))
    if yoyd is not None:
        prev = yoyd
    P(f'{k} DNR {DNR[k]}%  前期差 {qoqd}  前年差 {yoyd}  2階差分 {sd}')

lq = ['2024Q4', '2025Q1', '2025Q2', '2025Q3', '2025Q4', '2026Q1', '2026Q2']
prev = None
for k in lq:
    i = lq.index(k)
    qa = (LARGE[k] / LARGE[lq[i - 1]]) ** 4 - 1 if i >= 1 else None
    yy = {'2025Q4': LARGE['2025Q4'] / LARGE['2024Q4'] - 1, '2026Q1': LARGE['2026Q1'] / LARGE['2025Q1'] - 1,
          '2026Q2': LARGE['2026Q2'] / LARGE['2025Q2'] - 1}.get(k)
    sd = (yy - prev) if (yy is not None and prev is not None) else None
    rows18.append(('大口顧客数(年10万ドル超)', k, LARGE[k], qa, yy, sd))
    if yy is not None:
        prev = yy
    P(f'{k} 大口顧客 {LARGE[k]}  QoQ年率 {qa if qa is None else f"{qa:.1%}"}  YoY {yy if yy is None else f"{yy:.1%}"}  2階差分 {sd if sd is None else f"{sd*100:+.1f}pt"}')

# 新規コホート売上 = 売上_t − 売上_{t-4} × DNR_t(DNR の定義上の近似。プロフェッショナルサービス等の除外は無視)
sec('2. 増収の源泉分解(既存顧客の拡張/新規コホート)とエンジン照合')
coh = {}
for q in Q[4:]:
    base = REV[Q[Q.index(q) - 4]]
    ex = base * DNR[q] / 100
    new = REV[q] - ex
    coh[q] = dict(base=base, expansion=base * (DNR[q] / 100 - 1), new=new, s=new / REV[q])
    inc = REV[q] - base
    P(f'{q} 売上 {REV[q]:6.1f} = 前年売上 {base:6.1f} + 既存拡張 {coh[q]["expansion"]:6.1f} + 新規コホート {new:6.1f}(売上比 {new/REV[q]:.1%})'
      f'  増収 {inc:6.1f} のうち 既存拡張 {coh[q]["expansion"]/inc:.0%}・新規 {new/inc:.0%}')
P(f'新規コホート売上 YoY: 2026Q1 {coh["2026Q1"]["new"]/coh["2025Q1"]["new"]-1:+.1%} / 2026Q2 {coh["2026Q2"]["new"]/coh["2025Q2"]["new"]-1:+.1%}')
# 照合: 前年同期の新規コホート比率 s を使って当期を予測し、報告売上と比べる(DNR は独立の開示値)
recon = {}
for q in ['2026Q1', '2026Q2']:
    s_prev = coh[Q[Q.index(q) - 4]]['s']
    pred = REV[Q[Q.index(q) - 4]] * DNR[q] / 100 / (1 - s_prev)
    recon[q] = (pred, pred / REV[q] - 1)
    P(f'エンジン照合 {q}: 前年売上×DNR÷(1−前年の新規比率 {s_prev:.1%}) = {pred:.1f}  報告 {REV[q]}  差 {pred/REV[q]-1:+.1%}')
# 大口顧客の単価
for q in ['2025Q2', '2026Q2']:
    arpu = REV[q] * LARGE_SHARE[q] * 4 / LARGE[q] * 1000
    P(f'{q} 大口顧客の年換算単価 {arpu:,.0f} 千ドル(売上 {REV[q]}×比率 {LARGE_SHARE[q]:.0%}×4 ÷ {LARGE[q]}社)')
arpu25 = REV['2025Q2'] * 0.71 * 4 / LARGE['2025Q2']
arpu26 = REV['2026Q2'] * 0.73 * 4 / LARGE['2026Q2']
lg_rev_g = (REV['2026Q2'] * 0.73) / (REV['2025Q2'] * 0.71) - 1
oth_g = (REV['2026Q2'] * 0.27) / (REV['2025Q2'] * 0.29) - 1
P(f'大口顧客売上 YoY {lg_rev_g:+.1%} = 社数 {LARGE["2026Q2"]/LARGE["2025Q2"]-1:+.1%} × 単価 {arpu26/arpu25-1:+.1%} / その他の有料顧客の売上 YoY {oth_g:+.1%}(有料顧客数は+74%)')
# 年次: 平均DNR と新規比率
for y, dn in [(2024, (115 + 112 + 110 + 111) / 4), (2025, (111 + 114 + 119 + 120) / 4)]:
    s = 1 - FY_REV[y - 1] * dn / 100 / FY_REV[y]
    P(f'FY{y}: 平均DNR {dn:.2f}% / 新規コホート比率(年次近似) {s:.1%} / 売上成長 {FY_REV[y]/FY_REV[y-1]-1:.1%}')

# SBC 比率
sec('3. SBC(+関連給与税)/売上の推移')
sbc_ratio_hist = {
    'FY2024': FY_SBCPT[2024] / FY_REV[2024], 'FY2025': FY_SBCPT[2025] / FY_REV[2025],
    '2025Q1': SBCPT['2025Q1'] / REV['2025Q1'], '2025Q2': SBCPT['2025Q2'] / REV['2025Q2'],
    '2025H2': SBCPT['2025H2'] / (REV['2025Q3'] + REV['2025Q4']),
    '2026Q1': SBCPT['2026Q1'] / REV['2026Q1'], '2026Q2': SBCPT['2026Q2'] / REV['2026Q2']}
for k, v in sbc_ratio_hist.items():
    P(f'{k}: SBC+給与税/売上 {v:.1%}')
P(f'給与税を除くSBC/売上: FY2024 {SBC_EXPT["2024"]/FY_REV[2024]:.1%} / FY2025 {SBC_EXPT["2025"]/FY_REV[2025]:.1%} / 2026Q1 {SBC_EXPT["2026Q1"]/REV["2026Q1"]:.1%}')
P(f'SBC+給与税の伸び: Q2 2026 {SBCPT["2026Q2"]/SBCPT["2025Q2"]-1:+.1%}(売上 {yoy(REV,"2026Q2"):+.1%}) / 上期 {268.05/237.888-1:+.1%}')

# EPS の対数分解
sec('4. EPS品質フォレンジック: 調整後EPS成長の対数分解')
sh24, sh25 = FY_NGNI[2024] / FY_NGEPS[2024], FY_NGNI[2025] / FY_NGEPS[2025]
d1 = vl.eps_log_decomposition(FY_REV[2024], FY_REV[2025], FY_NGNI[2024] / FY_REV[2024], FY_NGNI[2025] / FY_REV[2025], sh24, sh25)
ni26 = 1.255 * GUIDE_2026['sh']
d2 = vl.eps_log_decomposition(FY_REV[2025], 2867, FY_NGNI[2025] / FY_REV[2025], ni26 / 2867, sh25, GUIDE_2026['sh'])
for nm, d, e0, e1 in [('2024→2025', d1, 0.75, 0.93), ('2025→2026ガイダンス', d2, 0.93, 1.255)]:
    P(f'{nm}: ln(EPS比) {math.log(e1/e0):.3f} = 売上 {d["revenue"]:.3f} + 純利益率 {d["margin"]:+.3f} + 希薄化 {d["dilution"]:+.3f}(合計 {d["total"]:.3f})')
P(f'株数(逆算): 2024 {sh24:.0f}M / 2025 {sh25:.0f}M / 2026 {GUIDE_2026["sh"]}M')
P(f'非GAAP営業利益率: 2024 {FY_NGOPI[2024]/FY_REV[2024]:.1%} / 2025 {FY_NGOPI[2025]/FY_REV[2025]:.1%} / 2026ガイダンス {444/2867:.1%}; 増分利益率 2025 {(FY_NGOPI[2025]-FY_NGOPI[2024])/(FY_REV[2025]-FY_REV[2024]):.1%} / 2026 {(444-FY_NGOPI[2025])/(2867-FY_REV[2025]):.1%}')
q3g = GUIDE_Q3
q4_rev = 2867 - REV['2026Q1'] - REV['2026Q2'] - 736.5
q4_opi = 444 - NG_OPI['2026Q1'] - NG_OPI['2026Q2'] - 129.5
P(f'ガイダンスの含意: Q3 営業利益率 {129.5/736.5:.1%} / Q4 売上 {q4_rev:.1f}・営業利益率 {q4_opi/q4_rev:.1%}(人員削減後の出口)')
P(f'FCF: 2024 {FY_FCF[2024]/FY_REV[2024]:.1%} / 2025 {FY_FCF[2025]/FY_REV[2025]:.1%} / 2026上期 {(84.1+56.4)/(639.8+696.1):.1%}; SBC控除後FCF 2025 {FY_FCF[2025]-FY_SBCPT[2025]:.0f}')
P(f'capex/売上: 2024 {FY_CAPEX[2024]/FY_REV[2024]:.1%} / 2025 {FY_CAPEX[2025]/FY_REV[2025]:.1%}(ネットワークcapex 2026年 14〜15% 見通し)')
P(f'ガイダンス超過: Q1 {639.8/620.5-1:+.1%} / Q2 {696.1/664.5-1:+.1%}; 通期ガイダンス中央値 2,790→2,809→2,867')

# 四半期の増分営業利益率(前年同期比)と、会社目標(2028年末に年換算50億ドル)に必要な成長率
inc_q3 = (129.5 - NG_OPI['2025Q3']) / (736.5 - REV['2025Q3'])
inc_q4 = (q4_opi - NG_OPI['2025Q4']) / (q4_rev - REV['2025Q4'])
inc_q2 = (NG_OPI['2026Q2'] - NG_OPI['2025Q2']) / (REV['2026Q2'] - REV['2025Q2'])
P(f'増分営業利益率(前年同期比): 2026Q2 実績 {inc_q2:.1%} / Q3 ガイダンス {inc_q3:.1%} / Q4 含意 {inc_q4:.1%}')
need_g = (1250 / REV['2026Q2']) ** (1 / 2.5) - 1
P(f'2028年Q4に四半期売上12.5億ドル(年換算50億ドル)へ: 2026Q2 から年 {need_g:.1%} の成長で到達')
# F11 シナリオ採点(規模加重): 点数 +大=2、+中=1、+小=0.5、±/保留=0、−=−1
F11 = [('プール型の大型契約', 0.35, 2), ('大口顧客の獲得・パートナー経路', 0.25, 2), ('人員約20%削減・AIファースト運営', 0.15, 1),
       ('Workers 開発者基盤', 0.10, 1), ('Workers AI・AI Gateway', 0.05, 0), ('AIエージェントの課金', 0.05, 0),
       ('SASE/Zero Trust の束ね価格', 0.03, 0), ('0% 転換社債(2031年満期)', 0.02, 0.5)]
f11_score = sum(w * sc for _, w, sc in F11)
P(f'F11 規模加重スコア {f11_score:.2f}(+2〜−1 の尺度、重みの合計 {sum(w for _, w, _ in F11):.2f})')

# ---------------------------------------------------------------- 5. 経路モデル
YRS = list(range(2026, 2037))
FYE = {y: dt.date(y, 12, 31) for y in YRS}


def shares_t(y):
    return SH_NOW * (1 + SH_G) ** (y - 2026)


def run_path(name, rev, opm=None, adj_eps=None, sbc=None, sbc_usd=None, fcfm=None, int26=170.0):
    """経路ごとの年度別 損益→調整後EPS→事業実態EPS。

    rev: {年: 売上}、opm: {年: 非GAAP営業利益率}(adj_eps を与えた年は逆算)、sbc: {年: SBC+給与税/売上}、
    sbc_usd: {年: SBC+給与税の金額}(与えた年は優先)、fcfm: {年: FCF/売上}(現金残高→受取利息)。
    """
    out = {}
    cash_prev = CASH_POST
    for y in YRS:
        rv = rev[y]
        cash = cash_prev + fcfm[y] * rv * (1.0 if y > 2026 else 0.25)
        if y == 2030:
            cash -= NOTES_2030
        if y == 2031:
            cash -= NOTES_2031
        intr = int26 if y == 2026 else YIELD * (cash_prev + cash) / 2
        sh = shares_t(y)
        if adj_eps is not None and y in adj_eps:
            ni = adj_eps[y] * sh
            op = ni / (1 - TAX) - intr
            om = op / rv
        else:
            om = opm[y]
            op = om * rv
            ni = (op + intr) * (1 - TAX)
        ae = ni / sh
        s_usd = sbc_usd[y] if (sbc_usd and y in sbc_usd) else sbc[y] * rv
        bni = ni - s_usd * (1 - TAX)
        be = vl.business_eps_fixed_shares(ae, sh, s_usd, SH_NOW, TAX)
        assert abs(be - bni / SH_NOW) < 1e-9
        out[y] = dict(rev=rv, om=om, op=op, intr=intr, ni=ni, sh=sh, adj_eps=ae, sbc_usd=s_usd, sbc_r=s_usd / rv,
                      bni=bni, beps=be, cash=cash, fcf=fcfm[y] * rv)
        cash_prev = cash
    return out


def grow(base_year_val, start, rates):
    d = {start: base_year_val}
    v = base_year_val
    for i, r in enumerate(rates):
        v *= 1 + r
        d[start + 1 + i] = v
    return d


# --- コンセンサス経路: 売上 2026 2,867(ガイダンス中央値=コンセンサス2.87B)/2027 3,690/2028 4,600/2029 5,750(以後は延長)
rev_c = {2026: 2867.0, 2027: 3690.0, 2028: 4600.0, 2029: 5750.0}
for y, r in zip(range(2030, 2037), [0.22, 0.20, 0.18, 0.16, 0.14, 0.12, 0.10]):
    rev_c[y] = rev_c[y - 1] * (1 + r)
eps_c = {2026: 1.26, 2027: 1.67, 2028: 2.20, 2029: 2.70}
# 基準のSBC比率パス(コンセンサス経路と共通): 2026 19.0%(上期20.1%、人員削減後の下期 約18%)→ 毎年1.5〜2pt 低下 → 9%で漸近
sbc_base = {2026: 0.190, 2027: 0.165, 2028: 0.145, 2029: 0.130, 2030: 0.115, 2031: 0.105, 2032: 0.095, 2033: 0.090,
            2034: 0.085, 2035: 0.085, 2036: 0.085}
fcf_c = {2026: 0.08, 2027: 0.15, 2028: 0.18, 2029: 0.21, 2030: 0.23, 2031: 0.25, 2032: 0.26, 2033: 0.27, 2034: 0.28, 2035: 0.28, 2036: 0.28}
tmp = run_path('consensus', rev_c, opm={y: 0.20 for y in YRS}, adj_eps=eps_c, sbc=sbc_base, fcfm=fcf_c)  # 2029年までの含意利益率の逆算用
opm_c = {y: tmp[y]['om'] for y in eps_c}
for y in range(2030, 2037):
    opm_c[y] = min(opm_c[y - 1] + 0.015, 0.28)
CONS = run_path('consensus', rev_c, opm=opm_c, adj_eps=eps_c, sbc=sbc_base, fcfm=fcf_c)

# --- 事業エンジン経路: 売上_q = 売上_{q-4} × DNR_q ÷(1 − 新規コホート比率 s_q)
dnr_path = {  # 四半期 DNR の仮定
    '2026Q3': 1.20, '2026Q4': 1.195,
    2027: [1.185, 1.18, 1.175, 1.17], 2028: [1.165, 1.16, 1.155, 1.15], 2029: [1.145, 1.14, 1.14, 1.135],
    2030: [1.135, 1.13, 1.13, 1.125], 2031: [1.125, 1.12, 1.12, 1.12]}
s_path = {'2026H2': 0.11, 2027: 0.105, 2028: 0.10, 2029: 0.095, 2030: 0.09, 2031: 0.085}
qrev = {('2025', i + 1): REV[f'2025Q{i+1}'] for i in range(4)}
qrev.update({('2026', 1): REV['2026Q1'], ('2026', 2): REV['2026Q2']})
qrev[('2026', 3)] = qrev[('2025', 3)] * dnr_path['2026Q3'] / (1 - s_path['2026H2'])
qrev[('2026', 4)] = qrev[('2025', 4)] * dnr_path['2026Q4'] / (1 - s_path['2026H2'])
for y in range(2027, 2032):
    for i in range(4):
        qrev[(str(y), i + 1)] = qrev[(str(y - 1), i + 1)] * dnr_path[y][i] / (1 - s_path[y])
rev_e = {y: sum(qrev[(str(y), i)] for i in range(1, 5)) for y in range(2026, 2032)}
for y, r in zip(range(2032, 2037), [0.21, 0.195, 0.175, 0.155, 0.135]):
    rev_e[y] = rev_e[y - 1] * (1 + r)
q4_runrate_e = {y: qrev[(str(y), 4)] * 4 for y in range(2026, 2032)}
opm_e = {2026: None, 2027: 0.195, 2028: 0.225, 2029: 0.25, 2030: 0.27, 2031: 0.285, 2032: 0.295, 2033: 0.305,
         2034: 0.31, 2035: 0.315, 2036: 0.32}
opm_e[2026] = (444 + (rev_e[2026] - 2867) * 0.40) / rev_e[2026]   # ガイダンス超過分の増分利益率40%
sbc_usd_e = {2026: 0.19 * rev_e[2026]}
for y, g in zip(range(2027, 2037), [0.09, 0.09, 0.09, 0.09, 0.08, 0.08, 0.08, 0.07, 0.07, 0.07]):
    sbc_usd_e[y] = sbc_usd_e[y - 1] * (1 + g)
fcf_e = {2026: 0.08, 2027: 0.16, 2028: 0.20, 2029: 0.24, 2030: 0.27, 2031: 0.29, 2032: 0.30, 2033: 0.31, 2034: 0.31, 2035: 0.31, 2036: 0.31}
ENG = run_path('engine', rev_e, opm=opm_e, sbc={}, sbc_usd=sbc_usd_e, fcfm=fcf_e)

# --- 会社シナリオ経路: 2027 Rule of 50+(成長30%超・営業利益率 約20%)、2028年末までに年換算50億ドル、長期 営業利益率30%超・FCF率30〜35%超
rev_m = grow(2890.0, 2026, [0.30, 0.28, 0.26, 0.24, 0.22, 0.20, 0.18, 0.16, 0.14, 0.12])
opm_m = {2026: 0.156, 2027: 0.205, 2028: 0.235, 2029: 0.265, 2030: 0.29, 2031: 0.305, 2032: 0.315, 2033: 0.325,
         2034: 0.33, 2035: 0.33, 2036: 0.33}
sbc_m = {2026: 0.188, 2027: 0.155, 2028: 0.13, 2029: 0.11, 2030: 0.095, 2031: 0.085, 2032: 0.08, 2033: 0.075, 2034: 0.07, 2035: 0.07, 2036: 0.07}
fcf_m = {2026: 0.08, 2027: 0.17, 2028: 0.22, 2029: 0.26, 2030: 0.29, 2031: 0.31, 2032: 0.32, 2033: 0.33, 2034: 0.33, 2035: 0.33, 2036: 0.33}
COMP = run_path('company', rev_m, opm=opm_m, sbc=sbc_m, fcfm=fcf_m)
q4_runrate_m_2028 = None  # 年次モデルのため四半期は持たない(2028年の売上 rev_m[2028] から確認)

# --- 弱気パス: プール型契約の前倒し消費の反動でDNRが2024年の谷(110%)へ回帰、新規比率9%→、粗利率は下限70%、SBC比率の低下が鈍い
rev_b = grow(2880.0, 2026, [0.22, 0.18, 0.155, 0.135, 0.12, 0.11, 0.10, 0.09, 0.08, 0.07])
# 経営陣の反応(二次の効果): 成長が鈍れば2026年5月と同様に費用とSBCを削る。それでも利益率とSBC比率の改善は会社計画より遅い
opm_b = {2026: 0.155, 2027: 0.17, 2028: 0.185, 2029: 0.20, 2030: 0.215, 2031: 0.225, 2032: 0.235, 2033: 0.245,
         2034: 0.25, 2035: 0.255, 2036: 0.26}
sbc_b = {2026: 0.19, 2027: 0.18, 2028: 0.165, 2029: 0.15, 2030: 0.135, 2031: 0.125, 2032: 0.115, 2033: 0.11, 2034: 0.105, 2035: 0.10, 2036: 0.10}
fcf_b = {2026: 0.07, 2027: 0.12, 2028: 0.14, 2029: 0.16, 2030: 0.17, 2031: 0.18, 2032: 0.19, 2033: 0.20, 2034: 0.21, 2035: 0.21, 2036: 0.21}
BEAR = run_path('bear', rev_b, opm=opm_b, sbc=sbc_b, fcfm=fcf_b)

PATHS = {'consensus': CONS, 'company': COMP, 'engine': ENG, 'bear': BEAR}
JP = {'consensus': 'コンセンサス', 'company': '会社シナリオ', 'engine': '事業エンジン', 'bear': '弱気'}

sec('5. 経路別の年度別モデル(FY12月期。2030年以降は延長部分)')
for k, d in PATHS.items():
    P(f'--- {JP[k]}経路')
    P('年度  売上    成長率  営業利益率  受取利息  調整後NI  調整後EPS  SBC+税/売上  事業実態NI  事業実態EPS  現金')
    for y in YRS:
        g = d[y]['rev'] / (d[y - 1]['rev'] if y > 2026 else 2167.9) - 1
        P(f'{y} {d[y]["rev"]:8,.0f} {g:6.1%} {d[y]["om"]:8.1%} {d[y]["intr"]:8.0f} {d[y]["ni"]:8,.0f} {d[y]["adj_eps"]:8.2f} '
          f'{d[y]["sbc_r"]:9.1%} {d[y]["bni"]:9,.0f} {d[y]["beps"]:9.2f} {d[y]["cash"]:8,.0f}')
P(f'エンジン経路: 2026年の四半期売上 Q3 {qrev[("2026",3)]:.1f}(ガイダンス736.5比 {qrev[("2026",3)]/736.5-1:+.1%})、Q4 {qrev[("2026",4)]:.1f}(含意794.6比 {qrev[("2026",4)]/q4_rev-1:+.1%})')
P('エンジン経路の Q4 年換算売上: ' + ', '.join(f'{y} {v/1000:.2f}bn' for y, v in q4_runrate_e.items()))
P(f'会社シナリオ経路: 2028年売上 {rev_m[2028]:,.0f}(Q4年換算はおよそ年売上×1.1 = {rev_m[2028]*1.1/1000:.2f}bn と見積り。目標50億ドル)')
P('コンセンサス経路の含意営業利益率: ' + ', '.join(f'{y} {opm_c[y]:.1%}' for y in range(2026, 2030)))
P('コンセンサスの含意DNR(新規比率10%と仮定): ' + ', '.join(
    f'{y} {(rev_c[y]/rev_c[y-1])*(1-0.10):.3f}' for y in range(2027, 2030)))

# ---------------------------------------------------------------- 6. 許容PEG と年度別評価(F13)
PEG_RANGE = {  # 年度別の許容PEG(x〜y)。根拠は報告書9章・Appendix B
    'consensus': {2026: (1.6, 1.8), 2027: (1.6, 1.8), 2028: (1.5, 1.7), 2029: (1.5, 1.7), 2030: (1.4, 1.6), 2031: (1.4, 1.6), 2032: (1.3, 1.5), 2033: (1.3, 1.5)},
    'company': {2026: (1.6, 1.8), 2027: (1.6, 1.8), 2028: (1.5, 1.7), 2029: (1.5, 1.7), 2030: (1.4, 1.6), 2031: (1.4, 1.6), 2032: (1.3, 1.5), 2033: (1.3, 1.5)},
    'engine': {2026: (1.6, 1.8), 2027: (1.6, 1.8), 2028: (1.5, 1.7), 2029: (1.5, 1.7), 2030: (1.4, 1.6), 2031: (1.4, 1.6), 2032: (1.3, 1.5), 2033: (1.3, 1.5)},
    'bear': {2026: (1.1, 1.3), 2027: (1.1, 1.3), 2028: (1.0, 1.2), 2029: (1.0, 1.2), 2030: (1.0, 1.2), 2031: (1.0, 1.2), 2032: (1.0, 1.1), 2033: (1.0, 1.1)},
}
sec('6. 年度別適正株価(F13)。g = 当該年度から3年先までの事業実態EPS CAGR(50%で頭打ち)')
f13 = []
for k, d in PATHS.items():
    P(f'--- {JP[k]}経路')
    for y in range(2026, 2034):
        e0, e3 = d[y]['beps'], d[y + 3]['beps']
        g = vl.cagr(e0, e3, 3) if (e0 > 0 and e3 > 0) else float('nan')
        lo, hi = PEG_RANGE[k][y]
        if e0 > 0 and not math.isnan(g):
            fl, fh = vl.fair_per(lo, g), vl.fair_per(hi, g)
            pl, ph = fl['capped'] * e0, fh['capped'] * e0
            pul, puh = fl['uncapped'] * e0, fh['uncapped'] * e0
        else:
            fl = fh = {'capped': float('nan'), 'uncapped': float('nan')}
            pl = ph = pul = puh = float('nan')
        ext = y >= 2030 if k == 'consensus' else y >= 2030
        f13.append(dict(fy_end=str(FYE[y]), path=k, business_eps=round(e0, 3), g_3y=round(g, 4) if not math.isnan(g) else '',
                        peg_low=lo, peg_high=hi, fair_per_low=round(fl['capped'], 1) if e0 > 0 else '', fair_per_high=round(fh['capped'], 1) if e0 > 0 else '',
                        fair_price_low=round(pl, 1) if e0 > 0 else '', fair_price_high=round(ph, 1) if e0 > 0 else '',
                        fair_price_low_uncapped=round(pul, 1) if e0 > 0 else '', fair_price_high_uncapped=round(puh, 1) if e0 > 0 else '',
                        is_extension=ext))
        P(f'{y} 事業実態EPS {e0:6.2f}  g {g if math.isnan(g) else f"{g:6.1%}"}  PEG {lo}〜{hi}  妥当PER {fl["capped"]:6.1f}〜{fh["capped"]:6.1f}  '
          f'適正株価 {pl:7.1f}〜{ph:7.1f}(頭打ちなし {pul:7.1f}〜{puh:7.1f}){"  ※延長" if ext else ""}')
with open(f'{OUT}/NET_F13.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(f13[0].keys()))
    w.writeheader()
    w.writerows(f13)

# ---------------------------------------------------------------- 7. 12か月目標株価(2本)
sec('7. 12か月目標株価: (1)規約どおり NTM事業実態EPS×妥当PER、(2)定常状態経由(§3-2)')
EXIT_PEG = {'consensus': 1.5, 'company': 1.8, 'engine': 1.6, 'bear': 1.2}
tgt = {}
for k, d in PATHS.items():
    eps_fy = {FYE[y]: d[y]['beps'] for y in YRS}
    ntm0 = vl.ntm_eps(eps_fy, vl.TARGET_DATE)
    ntm3 = vl.ntm_eps(eps_fy, dt.date(2030, 10, 11))
    g = vl.cagr(ntm0, ntm3, 3) if ntm0 > 0 else float('nan')
    lo, hi = PEG_RANGE[k][2028]
    pegm = (lo + hi) / 2
    if ntm0 > 0:
        t_lo, t_hi, t_mid = vl.target_price(ntm0, lo, g), vl.target_price(ntm0, hi, g), vl.target_price(ntm0, pegm, g)
    else:
        t_lo = t_hi = t_mid = {'price': 0.0, 'per': float('nan'), 'price_uncapped': 0.0}
    e30, e33 = d[2030]['beps'], d[2033]['beps']
    gx = vl.cagr(e30, e33, 3)
    ss = vl.steady_state_target(e30, FYE[2030], EXIT_PEG[k], gx)
    ss_lo = vl.steady_state_target(e30, FYE[2030], max(1.0, EXIT_PEG[k] - 0.2), gx)
    ss_hi = vl.steady_state_target(e30, FYE[2030], min(2.0, EXIT_PEG[k] + 0.2), gx)
    tgt[k] = dict(ntm=ntm0, g=g, conv=t_mid['price'], conv_lo=t_lo['price'], conv_hi=t_hi['price'], conv_per=t_mid['per'],
                  conv_uncapped=t_mid['price_uncapped'], e30=e30, gx=gx, ss=ss['target'], ss_lo=ss_lo['target'], ss_hi=ss_hi['target'],
                  per_exit=ss['per_exit'], yrs=ss['years_discounted'], peg_exit=EXIT_PEG[k])
    P(f'{JP[k]:6s}: NTM事業実態EPS(2027-10〜) {ntm0:.3f}  g {g:.1%}(頭打ち{min(g,0.5):.0%})  PEG {pegm:.1f} → 妥当PER {t_mid["per"]:.0f} → 目標 {t_mid["price"]:.1f}'
          f'(PEG{lo}〜{hi}: {t_lo["price"]:.1f}〜{t_hi["price"]:.1f}、頭打ちなし {t_mid["price_uncapped"]:.1f})')
    P(f'        定常状態経由: FY2030 事業実態EPS {e30:.2f}、出口g(2030→33) {gx:.1%}、出口PEG {EXIT_PEG[k]} → 出口PER {ss["per_exit"]:.1f} → '
      f'2030年末価値 {ss["value_at_exit"]:.1f} → {ss["years_discounted"]:.2f}年割引 → 目標 {ss["target"]:.1f}(出口PEG±0.2: {ss_lo["target"]:.1f}〜{ss_hi["target"]:.1f})')

# 交差確認: 各目標株価が 2027-10-11 時点で含意する EV/NTM売上(売上倍率)
P('--- 交差確認: 目標株価の含意 EV/NTM売上(2027-10〜2028-09)')
XCHK = {}
for k, d in PATHS.items():
    ntm_rev_t = d[2027]['rev'] * 3 / 12 + d[2028]['rev'] * 9 / 12
    nc = d[2027]['cash'] - NOTES_2030 - NOTES_2031
    for lab, t in (('定常状態経由', tgt[k]['ss']), ('規約どおり', tgt[k]['conv'])):
        evs = (t * SH_NOW - nc) / ntm_rev_t
        XCHK[(k, lab)] = evs
        P(f'{JP[k]:6s} {lab}: 目標 {t:6.1f} → EV/NTM売上 {evs:5.1f}倍(NTM売上 {ntm_rev_t:,.0f}、売上成長 {d[2028]["rev"]/d[2027]["rev"]-1:.0%})')
P(f'参考: 現在の EV/NTM売上 {EV/(2867*3/12+3690*9/12):.1f}倍')
# 弱気パスの交差確認: 調整後EPS(市場の慣行)に低成長ピアの倍率を当てる。AKAM 調整後PER 16.1倍(peer_peg_table.md)
AKAM_PER = 16.1
ntm_adj_bear = vl.ntm_eps({FYE[y]: BEAR[y]['adj_eps'] for y in YRS}, vl.TARGET_DATE)
g_adj_bear = vl.cagr(BEAR[2027]['adj_eps'], BEAR[2030]['adj_eps'], 3)
P(f'弱気の交差確認: NTM調整後EPS(2027-10〜) {ntm_adj_bear:.2f} × AKAM 調整後PER {AKAM_PER} = {ntm_adj_bear*AKAM_PER:.1f}; '
  f'× 調整後PEG 1.0×g({g_adj_bear:.1%}) = {ntm_adj_bear*g_adj_bear*100:.1f}')

# 交差確認(統括レビュー指摘3): SBC を現金費用とみなす DCF(所有者キャッシュフロー)
#   CF_t = FCF_t − SBC(給与税を除く分を SBC+給与税の92%と仮定)×(1−t) − 受取利息×(1−t)(ネットキャッシュは別に加える)
#   明示期間 2027〜2036年(2027年は 2027-10-11 以降の1/4のみ)、以後は永久成長 g_T。割引は各年の期末日から 2027-10-11 まで 9%。
def dcf_value(d, g_t=0.04, r=R, at=vl.TARGET_DATE):
    pv = 0.0
    for y in range(2027, 2037):
        cf = d[y]['fcf'] - d[y]['sbc_usd'] * 0.92 * (1 - TAX) - d[y]['intr'] * (1 - TAX)
        if y == 2027:
            cf *= 0.25
        t = (FYE[y] - at).days / 365.25
        pv += cf / (1 + r) ** t
    y = 2036
    cf36 = d[y]['fcf'] - d[y]['sbc_usd'] * 0.92 * (1 - TAX) - d[y]['intr'] * (1 - TAX)
    tv = cf36 * (1 + g_t) / (r - g_t)
    t = (FYE[y] - at).days / 365.25
    pv_tv = tv / (1 + r) ** t
    nc = d[2026]['cash'] - NOTES_2030 - NOTES_2031
    eq = pv + pv_tv + nc
    return dict(per_share=eq / SH_NOW, pv_explicit=pv, pv_tv=pv_tv, tv_share=pv_tv / (pv + pv_tv), cf36=cf36)


P('--- 交差確認: SBC を費用とみなす DCF(12か月後の価値、明示期間 2027〜36年、永久成長 g_T)')
DCF = {}
for k, d in PATHS.items():
    res = {gt: dcf_value(d, gt) for gt in (0.03, 0.04, 0.05)}
    DCF[k] = res
    P(f'{JP[k]:6s}: g_T 3% {res[0.03]["per_share"]:6.1f} / 4% {res[0.04]["per_share"]:6.1f} / 5% {res[0.05]["per_share"]:6.1f}'
      f'(4% のとき 終価の比率 {res[0.04]["tv_share"]:.0%}、2036年CF {res[0.04]["cf36"]:,.0f}、FCF率 {d[2036]["fcf"]/d[2036]["rev"]:.0%}・SBC比率 {d[2036]["sbc_r"]:.1%})')
P('  資本コスト感応度(エンジン、g_T 4%): ' + ', '.join(f'{rr:.0%}: {dcf_value(ENG, 0.04, rr)["per_share"]:.1f}' for rr in (0.08, 0.10)))


# 株価(12か月後 = 株価×1.09)を DCF で正当化する、エンジン経路の売上の上乗せ(2027〜2036年の年成長率への一律加算)
def dcf_scaled(add_g):
    rv = {2026: rev_e[2026]}
    for y in range(2027, 2037):
        rv[y] = rv[y - 1] * (rev_e[y] / rev_e[y - 1] + add_g)
    sb = {y: sbc_usd_e[y] * rv[y] / rev_e[y] for y in YRS}
    d = run_path('dcfv', rv, opm=opm_e, sbc={}, sbc_usd=sb, fcfm=fcf_e)
    return dcf_value(d, 0.04)['per_share'], d


lo_a, hi_a = 0.0, 0.40
for _ in range(60):
    mid = (lo_a + hi_a) / 2
    if dcf_scaled(mid)[0] < PRICE * (1 + R):
        lo_a = mid
    else:
        hi_a = mid
dcf_add = (lo_a + hi_a) / 2
_, dd = dcf_scaled(dcf_add)
cagr_need = (dd[2036]['rev'] / dd[2026]['rev']) ** (1 / 10) - 1
P(f'DCF で株価を正当化するには、エンジン経路の年成長率に +{dcf_add*100:.1f}pt が要る → 2026→36年の売上CAGR {cagr_need:.1%}(エンジン {(rev_e[2036]/rev_e[2026])**0.1-1:.1%})、'
  f'2036年売上 {dd[2036]["rev"]/1000:.0f}bn(エンジン {rev_e[2036]/1000:.0f}bn)')

# 統括レビュー指摘1: 下値の床(1株当たり定常状態価値)と PER 下限の確認
_ss_om = 0.73 - 0.12 - 0.08 - 0.09
ss_ps = (rev_e[2026] * (_ss_om - 0.09) * (1 - TAX) + NET_CASH * YIELD * (1 - TAX)) / R / SH_NOW
P(f'下値の床(00_standard §3-3): 1株当たり定常状態価値 {ss_ps:.1f}ドル。弱気の12か月目標 {tgt["bear"]["ss"]:.1f} は床を上回る → {"条件を満たす" if tgt["bear"]["ss"] >= ss_ps else "床を適用"}')
P(f'妥当PERの下限 11.1倍が効いた年度・経路: ' + (', '.join(f'{r["path"]} {r["fy_end"]}' for r in f13 if r['fair_per_low'] != '' and r['fair_per_low'] <= 11.12) or 'なし'))

ADOPT = 'ss'   # 採用: 定常状態経由(理由は報告書10章)
T12 = {k: tgt[k][ADOPT] for k in PATHS}
gaps = {k: vl.gap(T12[k], PRICE) for k in PATHS}
P('採用(定常状態経由)の12か月目標株価: ' + ', '.join(f'{JP[k]} {T12[k]:.1f}({gaps[k]:+.1%})' for k in PATHS))

# ---------------------------------------------------------------- 8. 現在の倍率、成長の値段、市場の含意
sec('8. 現在の倍率・成長の値段・株価が織り込む前提')
eps_fy_c = {FYE[y]: CONS[y]['adj_eps'] for y in YRS}
ntm_adj_now = vl.ntm_eps({FYE[y]: CONS[y]['adj_eps'] for y in YRS}, dt.date(2026, 10, 11))
ntm_bus_now_c = vl.ntm_eps({FYE[y]: CONS[y]['beps'] for y in YRS}, dt.date(2026, 10, 11))
ntm_bus_now_e = vl.ntm_eps({FYE[y]: ENG[y]['beps'] for y in YRS}, dt.date(2026, 10, 11))
ntm_rev = 2867 * 3 / 12 + 3690 * 9 / 12
adj_cagr3 = vl.cagr(CONS[2026]['adj_eps'], CONS[2029]['adj_eps'], 3)
bus_cagr3_c = vl.cagr(CONS[2026]['beps'], CONS[2029]['beps'], 3)
per_adj = PRICE / ntm_adj_now
per_bus_c = PRICE / ntm_bus_now_c
fcf_ttm = FCF['2025Q3'] + FCF['2025Q4'] + FCF['2026Q1'] + FCF['2026Q2']
rev_ttm = REV['2025Q3'] + REV['2025Q4'] + REV['2026Q1'] + REV['2026Q2']
ntm_fcf = 0.08 * 2867 * 3 / 12 + 0.15 * 3690 * 9 / 12
mult = dict(per_business_ntm=per_bus_c, per_adj_ntm=per_adj, peg_business_3y=per_bus_c / (min(bus_cagr3_c, vl.G_CAP) * 100),
            peg_adj_3y=per_adj / (adj_cagr3 * 100), ev_sales_ntm=EV / ntm_rev, ev_fcf_ntm=EV / ntm_fcf,
            fcf_margin_ttm=fcf_ttm / rev_ttm, sbc_to_revenue_ttm=(SBCPT['2026Q1'] + SBCPT['2026Q2'] + SBCPT['2025H2']) / rev_ttm)
for k, v in mult.items():
    P(f'{k}: {v:.3f}')
P(f'NTM(2026-10〜)調整後EPS {ntm_adj_now:.2f} / 事業実態EPS(コンセンサス) {ntm_bus_now_c:.3f}・(エンジン) {ntm_bus_now_e:.3f}; 調整後EPS CAGR 2026→29 {adj_cagr3:.1%}; 事業実態 {bus_cagr3_c:.1%}')
P(f'TTM 売上 {rev_ttm:.1f} / FCF {fcf_ttm:.1f} / Rule of 40(売上成長 Q2 YoY + TTM FCF率) {yoy(REV,"2026Q2")*100 + fcf_ttm/rev_ttm*100:.1f}')

# 定常状態利益(成長投資を止めた場合): 2026年エンジン売上 × 非GAAP営業利益率(定常)− SBC(定常)
SS = dict(gm=0.73, sm_maint=0.12, rd_maint=0.08, ga=0.09, sbc=0.09)
ss_om = SS['gm'] - SS['sm_maint'] - SS['rd_maint'] - SS['ga']
ss_pre = ss_om - SS['sbc']
ss_earn = rev_e[2026] * ss_pre * (1 - TAX) + NET_CASH * YIELD * (1 - TAX)
split = vl.steady_state_split(ss_earn, MCAP)
P(f'定常状態: 非GAAP営業利益率 {ss_om:.0%}(粗利率73%−維持S&M12%−維持R&D8%−G&A9%)− SBC9% = {ss_pre:.0%} → 税引後利益 {ss_earn:,.0f}')
P(f'定常状態価値 {split["steady_state_value"]/1000:.1f}bn / 時価総額 {MCAP/1000:.1f}bn / 成長の値段 {split["growth_price"]/1000:.1f}bn({split["growth_share_of_mcap"]:.1%})')
for lab, om in [('定常利益率35%', 0.35), ('定常利益率50%', 0.50), ('会社の長期目標30%', 0.30)]:
    e = rev_e[2026] * (om - SS['sbc']) * (1 - TAX) + NET_CASH * YIELD * (1 - TAX)
    s2 = vl.steady_state_split(e, MCAP)
    P(f'  感応度 {lab}: 定常状態価値 {s2["steady_state_value"]/1000:.1f}bn・成長の値段の比率 {s2["growth_share_of_mcap"]:.1%}')
for rr in (0.08, 0.10):
    s3 = vl.steady_state_split(ss_earn, MCAP, rr)
    P(f'  資本コスト {rr:.0%}: 定常状態価値 {s3["steady_state_value"]/1000:.1f}bn')

# 株価が織り込む FY2030 事業実態EPS(12か月後の価値 = 株価×1.09 を、2030年末から割り戻す)
yrs_ex = (FYE[2030] - vl.TARGET_DATE).days / 365.25
need_val_2030 = PRICE * (1 + R) * (1 + R) ** yrs_ex
for per in (60, 80, 100):
    P(f'株価を正当化する FY2030 事業実態EPS(出口PER {per}倍): {need_val_2030/per:.2f}(エンジン経路 {ENG[2030]["beps"]:.2f}、会社 {COMP[2030]["beps"]:.2f})')


# 市場の含意成長率: 会社経路の利益率・SBC で、売上成長率(2027〜2033 一定、その後減速)を解き、定常状態目標(出口PEG 2.0)= 株価×1.09 とする
def implied_target(g_rev, peg=2.0):
    rv = {2026: 2890.0}
    for y in range(2027, 2037):
        gg = g_rev if y <= 2033 else max(g_rev - 0.04 * (y - 2033), 0.10)
        rv[y] = rv[y - 1] * (1 + gg)
    d = run_path('impl', rv, opm=opm_m, sbc=sbc_m, fcfm=fcf_m)
    gx = vl.cagr(d[2030]['beps'], d[2033]['beps'], 3)
    return vl.steady_state_target(d[2030]['beps'], FYE[2030], peg, gx)['target'], d


lo_g, hi_g = 0.10, 0.80
for _ in range(60):
    mid = (lo_g + hi_g) / 2
    if implied_target(mid)[0] < PRICE * (1 + R):
        lo_g = mid
    else:
        hi_g = mid
impl_g = (lo_g + hi_g) / 2
it, idd = implied_target(impl_g)
implied_rev30 = idd[2030]['rev']
P(f'株価が織り込む売上成長率(2027〜2033年一定、会社経路の利益率・SBC、出口PEG 2.0): {impl_g:.1%}/年 → 2030年売上 {idd[2030]["rev"]/1000:.1f}bn・2033年 {idd[2033]["rev"]/1000:.1f}bn')
lo_g, hi_g = 0.10, 0.80
for _ in range(60):
    mid = (lo_g + hi_g) / 2
    if implied_target(mid, 1.6)[0] < PRICE * (1 + R):
        lo_g = mid
    else:
        hi_g = mid
impl_g16 = (lo_g + hi_g) / 2
P(f'  同(出口PEG 1.6): {impl_g16:.1%}/年')

# ---------------------------------------------------------------- 9. 感応度(F12): 芯 × 芯
sec('9. 感応度(F12): 2027〜2031年の DNR の水準差 × 2030年の SBC 比率 → 定常状態経由の目標株価(エンジン経路を基準)')


def engine_variant(dnr_shift=0.0, sbc30=None, om_shift=0.0, peg=1.6, yld=YIELD):
    global YIELD
    old = YIELD
    YIELD = yld
    qr = {k: v for k, v in qrev.items() if k[0] in ('2025', '2026')}
    for y in range(2027, 2032):
        for i in range(4):
            qr[(str(y), i + 1)] = qr[(str(y - 1), i + 1)] * (dnr_path[y][i] + dnr_shift) / (1 - s_path[y])
    rv = {y: sum(qr[(str(y), i)] for i in range(1, 5)) for y in range(2026, 2032)}
    for y, r in zip(range(2032, 2037), [0.21, 0.195, 0.175, 0.155, 0.135]):
        rv[y] = rv[y - 1] * (1 + r + dnr_shift * 0.5)
    om = {y: (opm_e[y] + (om_shift if y >= 2027 else 0)) for y in YRS}
    if sbc30 is None:
        d = run_path('v', rv, opm=om, sbc={}, sbc_usd=sbc_usd_e, fcfm=fcf_e)
    else:
        # 2026 19% → 2030 sbc30 へ線形、その後 年0.9pt 低下(下限6%。基準のエンジン経路の2030→33年の低下幅 約1pt/年に合わせる)
        sr = {2026: 0.19}
        for y in range(2027, 2031):
            sr[y] = 0.19 + (sbc30 - 0.19) * (y - 2026) / 4
        for y in range(2031, 2037):
            sr[y] = max(sr[y - 1] - 0.009, 0.06)
        d = run_path('v', rv, opm=om, sbc=sr, fcfm=fcf_e)
    YIELD = old
    gx = vl.cagr(d[2030]['beps'], d[2033]['beps'], 3)
    return vl.steady_state_target(d[2030]['beps'], FYE[2030], peg, gx)['target'], d


f12 = []
dnr_shifts = [-0.06, -0.03, 0.0, 0.03, 0.06]
sbc30s = [0.06, 0.08, 0.10, 0.12, 0.15]
P('DNR差\\SBC比率2030 ' + ' '.join(f'{s:>8.0%}' for s in sbc30s))
for ds in dnr_shifts:
    line = []
    for s30 in sbc30s:
        t, _ = engine_variant(ds, s30)
        f12.append(dict(dnr_shift_pt=round(ds * 100), sbc_ratio_2030=s30, target=round(t, 1), gap=round(t / PRICE - 1, 3)))
        line.append(t)
    P(f'{ds*100:+.0f}pt      ' + ' '.join(f'{t:8.1f}' for t in line))
P('--- 営業利益率(2027年以降の水準差) × 出口PEG')
for oms in (-0.04, 0.0, 0.04):
    P(f'営業利益率 {oms*100:+.0f}pt: ' + ', '.join(f'PEG{pg}: {engine_variant(0.0, None, oms, pg)[0]:.1f}' for pg in (1.2, 1.6, 2.0)))
P('--- 金利(手元資金の利回り)感応度: ' + ', '.join(f'{y:.1%}: {engine_variant(0.0, None, 0.0, 1.6, y)[0]:.1f}' for y in (0.026, 0.036, 0.046)))
sens1 = {}
for nm, kw in [('DNR ±3pt', dict(dnr_shift=0.03)), ('DNR −3pt', dict(dnr_shift=-0.03)), ('SBC比率2030 8%', dict(sbc30=0.08)),
               ('SBC比率2030 14%', dict(sbc30=0.14)), ('営業利益率 +3pt', dict(om_shift=0.03)), ('営業利益率 −3pt', dict(om_shift=-0.03)),
               ('出口PEG 2.0', dict(peg=2.0)), ('出口PEG 1.2', dict(peg=1.2))]:
    sens1[nm] = engine_variant(**kw)[0]
base_t = engine_variant()[0]
P(f'基準 {base_t:.1f}; ' + ', '.join(f'{k}: {v:.1f}({v-base_t:+.1f})' for k, v in sens1.items()))
# 新規コホート比率 s の水準差(2027〜2031年)の感応度
def engine_s_variant(ds):
    qr = {k: v for k, v in qrev.items() if k[0] in ('2025', '2026')}
    for y in range(2027, 2032):
        for i in range(4):
            qr[(str(y), i + 1)] = qr[(str(y - 1), i + 1)] * dnr_path[y][i] / (1 - (s_path[y] + ds))
    rv = {y: sum(qr[(str(y), i)] for i in range(1, 5)) for y in range(2026, 2032)}
    for y, r in zip(range(2032, 2037), [0.21, 0.195, 0.175, 0.155, 0.135]):
        rv[y] = rv[y - 1] * (1 + r)
    d = run_path('v', rv, opm=opm_e, sbc={}, sbc_usd=sbc_usd_e, fcfm=fcf_e)
    gx = vl.cagr(d[2030]['beps'], d[2033]['beps'], 3)
    return vl.steady_state_target(d[2030]['beps'], FYE[2030], 1.6, gx)['target']


P('新規コホート比率の水準差: ' + ', '.join(f'{ds*100:+.0f}pt: {engine_s_variant(ds):.1f}' for ds in (-0.02, -0.01, 0.01, 0.02)))
# AIの収益化(Monetization Gateway・Pay per crawl・AI Gateway)のオプション: 2030年に売上 X、限界利益率60%
for x in (150, 300, 600):
    de = x * 0.60 * (1 - TAX) / SH_NOW
    val = de * tgt['engine']['per_exit'] / (1 + R) ** tgt['engine']['yrs']
    P(f'AI収益化オプション: 2030年売上 {x}百万ドル → 事業実態EPS +{de:.2f} → 12か月目標 +{val:.1f}ドル(出口PER {tgt["engine"]["per_exit"]:.1f}倍)')
# 障害の反復: DNR −2pt(2027〜2031年)
P(f'障害の反復でDNR −2pt: {engine_variant(-0.02)[0]:.1f}({engine_variant(-0.02)[0]-base_t:+.1f})')
# 欧州の罰金(イタリア 1,420万ユーロ、1ユーロ=1.08ドルと仮定)の1株当たり
P(f'イタリアの制裁金 1,420万ユーロ ≒ {14.2*1.08:.1f}百万ドル = 1株 {14.2*1.08/SH_NOW:.3f}ドル')

with open(f'{OUT}/NET_F12.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(f12[0].keys()))
    w.writeheader()
    w.writerows(f12)

# 資本コスト感応度(採用目標)
P('--- 資本コスト 8%/10% での定常状態経由の目標(エンジン): ' + ', '.join(
    f'{rr:.0%}: {vl.steady_state_target(ENG[2030]["beps"], FYE[2030], 1.6, tgt["engine"]["gx"], r=rr)["target"]:.1f}' for rr in (0.08, 0.10)))

# ---------------------------------------------------------------- 10. 期待値・非対称性・エントリー・判断
sec('10. 確率加重・非対称性・エントリー価格帯・2軸マトリクス')
PROB = {'bear': 0.25, 'consensus': 0.30, 'engine': 0.30, 'company': 0.15}
ev = vl.expected_value(T12, PROB, PRICE)
down = T12['bear'] / PRICE - 1
up = T12['company'] / PRICE - 1
ratio = (T12['company'] - PRICE) / (PRICE - T12['bear'])
RATING = 'A'
ALPHA = 0.20
EDGE = True
z = vl.zones(B=T12['engine'], U=T12['company'], L=T12['bear'], alpha=ALPHA, price=PRICE, edge=EDGE)
dec = vl.decision(RATING, gaps['engine'], EDGE)
P(f'確率加重の適正価値 {ev["expected_price"]:.1f} / 現在株価との確率加重の乖離 {ev["expected_return"]:+.1%}(12か月の株価予想ではない。00_standard §3-3)')
P(f'下値(弱気) {down:+.1%} / 上値(会社シナリオ) {up:+.1%} / 上値÷下値 {ratio:.2f} → 凸性 {"あり" if up > 0 and ratio > 1 else "なし"}')
P(f'エントリー: α {ALPHA:.0%}  Z1 {z["Z1"]:.1f}  Z2 {z["Z2"]:.1f}  現在 {PRICE} → {z["zone"]}')
P(f'2軸マトリクス: 構造評価 {RATING} × 乖離(事業エンジン) {gaps["engine"]:+.1%} → {dec}')
for k in PATHS:
    P(f'  乖離 {JP[k]}: {gaps[k]:+.1%} → {vl.decision(RATING, gaps[k], EDGE)}')
# 規約どおりの方法での参考
P('規約どおり(NTM×妥当PER)の目標: ' + ', '.join(f'{JP[k]} {tgt[k]["conv"]:.1f}' for k in PATHS))

# 価値の時間分布: エンジン経路の 2027〜2029 年の事業実態EPS の現在価値 ÷ 株価
pv3 = sum(ENG[y]['beps'] / (1 + R) ** (y - 2026 + 0.22) for y in (2027, 2028, 2029))
P(f'価値の時間分布(株価に対する比率): 3年以内(2027〜29年の事業実態EPSの現在価値) {pv3:.2f} ドル = {pv3/PRICE:.1%} / それ以降 {1-pv3/PRICE:.1%}')
pv3_t = pv3 / (T12['engine'] / (1 + R)) if T12['engine'] > 0 else float('nan')
P(f'  (エンジン経路の価値に対しては 3年以内 {pv3_t:.1%})')

# 増分ROIC(粗い推計): 過去12か月の純増年換算売上 ÷ S&M(非GAAP、推定 売上の31%)
nn_arr = (REV['2026Q2'] - REV['2025Q2']) * 4
sm_ttm = 0.31 * rev_ttm
magic = nn_arr / sm_ttm
contrib = 0.73 - 0.20            # 粗利率73% − 維持費用(R&D・G&Aの配賦 20%)
inv = 1.0 + 0.4                  # S&M 1ドル + 新規売上1ドル当たりのネットワーク設備 約0.4ドル(capex/売上14%×回転の仮定)
roic_pre = magic * contrib * (1 - TAX) / inv
roic_post = magic * (contrib - 0.18) * (1 - TAX) / inv
P(f'マジックナンバー(純増年換算売上÷S&M) {magic:.2f} / 増分ROIC(SBC前) {roic_pre:.0%}・(SBC控除後) {roic_post:.0%}  ※粗い推計')

# ---------------------------------------------------------------- 11. CSV(F18, F10)と summary.json
with open(f'{OUT}/NET_F18.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['kpi', 'period', 'value', 'qoq_annualized', 'ttm_yoy', 'second_diff'])
    for r in rows18:
        w.writerow([r[0], r[1], r[2]] + [('' if v is None else round(v, 4)) for v in r[3:]])
    for k, v in NG_GM.items():
        w.writerow(['非GAAP粗利率', k, v, '', '', ''])
    for k, v in sbc_ratio_hist.items():
        w.writerow(['SBC+関連給与税/売上', k, round(v, 4), '', '', ''])
    for k, v in CRPO_YOY.items():
        w.writerow(['cRPO前年比', k, v, '', '', ''])
    for q in Q[4:]:
        w.writerow(['新規コホート売上(百万ドル)', q, round(coh[q]['new'], 1), '', '', ''])
with open(f'{OUT}/NET_F10.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['period', 'line', 'revenue_usd_mn'])
    for q in Q[4:]:
        w.writerow([q, '前年同期の既存顧客売上', round(coh[q]['base'], 1)])
        w.writerow([q, '既存顧客の拡張(DNR−100%)', round(coh[q]['expansion'], 1)])
        w.writerow([q, '新規コホート(過去12か月の獲得)', round(coh[q]['new'], 1)])
with open(f'{OUT}/NET_F10b.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['period', 'line', 'revenue_usd_mn'])
    for q, s in LARGE_SHARE.items():
        w.writerow([q, '大口顧客(年10万ドル超)', round(REV[q] * s, 1)])
        w.writerow([q, 'その他の有料顧客', round(REV[q] * (1 - s), 1)])

summary = {
    'ticker': 'NET', 'company': 'Cloudflare, Inc.', 'price': PRICE, 'price_date': '2026-10-09',
    'market_cap_usd_bn': round(MCAP / 1000, 1), 'diluted_shares_mn': SH_NOW, 'fy_end_month': 12,
    'net_cash_usd_bn': round(NET_CASH / 1000, 2),
    'structure_rating': RATING,
    'condition_ratings': {'1': 'A', '2': 'B', '3': 'B', '4': 'S', '5': 'A', '6': 'D', '7': 'C', '8': 'A', '9': 'B', '10': 'B',
                          '11': 'A', '12': 'A', '13': 'A'},
    'condition9_applicable': True,
    'rules_fired': ['致命条件の拒否権: 非発動(E以下なし)', '条件6-7の対評価: 発動(PEGは低くなく、条件6のSは存在しない。高い理由は陳腐化capexではなく成長の持続年数への期待)',
                    'C×4上限: 非発動(Cは1条件)', '対象外(N/A): なし(条件9は適用)'],
    'archetype': 'ORCL型寄り(従量・プール型契約、停めない運用の通信路)。ただしSBCが調整後利益の大半を吸収',
    'business_model_types': ['B(従量課金のネットワーク型インフラ: アプリケーション・ネットワークサービス)', 'A(ストック型: Zero Trust/SASE)', 'C的なcapex(ネットワーク・GPU、売上の14〜15%)'],
    'core_variables': [
        {'name': '既存顧客の拡張(DNR)と新規コホート比率(=成長の持続年数)',
         'market_implied': f'株価は会社経路の利益率でも2027〜33年に年{impl_g*100:.0f}%の売上成長(2030年売上{implied_rev30/1000:.0f}bn)を要する。コンセンサスは2027年DNR 約116%相当',
         'our_estimate': f'DNR 2027年 117〜118%→2030年 113%、新規比率 10.5%→9%。売上成長 2027年{(rev_e[2027]/rev_e[2026]-1)*100:.0f}%・2030年{(rev_e[2030]/rev_e[2029]-1)*100:.0f}%',
         'advantage_type': '分析(DNRと新規コホートへの増収分解、プール型契約の消費速度)'},
        {'name': 'SBC(+関連給与税)/売上の低下経路',
         'market_implied': 'コンセンサス(調整後EPS)はSBCを除外。株価はSBC比率が成熟同業並み(4〜11%)へ下がる前提でないと説明できない',
         'our_estimate': f'2026年 19%→2030年 {ENG[2030]["sbc_r"]*100:.0f}%→2033年 {ENG[2033]["sbc_r"]*100:.0f}%(SBC金額は年8〜9%増)',
         'advantage_type': '分析(Q2 2026 のSBC+給与税 +6.5% と売上 +36% の差、人員2割削減)'},
        {'name': '競争優位期間(出口PEG)と定常状態の営業利益率',
         'market_implied': '株価は2030年の事業実態EPS 5〜9ドル(エンジン経路の1.6〜2.6倍)を要する',
         'our_estimate': f'CAP 約12年(出口PEG 1.6)、非GAAP営業利益率 2027年19.5%→2030年27%→2033年30.5%',
         'advantage_type': '時間軸(人員削減の効果は2027年に出る)。持続年数そのものは予測可能性が低い'}],
    'edge': {'exists': True,
             'statement': (f'短期は事業エンジン経路がコンセンサスを上回る(2027年売上 {rev_e[2027]:,.0f}百万ドル vs 3,690、調整後EPS {ENG[2027]["adj_eps"]:.2f} vs 1.67)。'
                           f'しかし株価は2033年まで年{impl_g*100:.0f}%の売上成長を織り込み、事業エンジン経路の価値({T12["engine"]:.0f}ドル)の{PRICE/T12["engine"]:.1f}倍にある。'
                           '差分は割安ではなく「株価が事業の上振れの先まで先取りしている」方向にある'),
             'advantage_type': '分析(増収分解とSBC控除後の利益からの逆算)。長期の持続年数は予測可能性が低く、優位は限定的',
             'kpi': 'DNR・新規コホート売上・SBC+関連給与税/売上・非GAAP営業利益率',
             'threshold': 'DNR 115%未満が2四半期連続、または2027年ガイダンスの売上成長25%未満で株価の前提が崩れる。DNR 122%超かつ営業利益率20%超が続けば会社シナリオ経路へ',
             'timing': '2026年Q3決算(2026年10月末〜11月上旬の見込み)〜2027年Q2決算', 'value_per_share_if_resolved': round(T12['engine'], 1)},
    'eps_definition': '事業実態EPS = (調整後EPS×株数_t − (SBC+関連給与税)×(1−22%)) ÷ 現在の希薄化後株数374M(00_standard §3-1)。調整後EPSは会社定義のnon-GAAP希薄化後EPS(税率は約22%で正規化済みと逆算)',
    'base_business_eps': {'fy': 'FY2026(12月期、コンセンサス)', 'value': round(CONS[2026]['beps'], 3)},
    'eps_paths': {p: {f'FY{y}': round(PATHS[p][y]['beps'], 3) for y in range(2026, 2034)} for p in PATHS},
    'adj_eps_consensus': {'FY2026': 1.26, 'FY2027': 1.67, 'FY2028': 2.2, 'FY2029': 2.7},
    'sbc_to_revenue_path': {f'FY{y}': round(ENG[y]['sbc_r'], 3) for y in range(2026, 2034)},
    'allowed_peg': {'path_a': [3.4, 9.9], 'path_b': [1.5, 2.0], 'path_c': [1.4, 1.8], 'adopted': [1.4, 1.8],
                    'note': ('経路aは調整後PEGのピア実勢(NETは9.9で最上位)であり許容値の根拠にしない。年度別PEG: 2026〜27年 1.6〜1.8 → 2030年 1.4〜1.6 → 2032〜33年 1.3〜1.5。'
                             '出口PEG: 事業エンジン1.6・会社1.8・コンセンサス1.5・弱気1.2。12か月目標は定常状態経由(採用)と規約どおりの両方を計算: '
                             + '; '.join(f'{JP[k]} 定常状態経由 {tgt[k]["ss"]:.1f} / 規約どおり {tgt[k]["conv"]:.1f}' for k in PATHS))},
    'targets_12m': {k: round(T12[k], 1) for k in PATHS},
    'adopted_path': 'engine',
    'cross_check_dcf': {k: round(DCF[k][0.04]['per_share'], 1) for k in PATHS},
    'steady_state_value_per_share': round(ss_ps, 1), 'gaps': {k: round(gaps[k], 3) for k in ('consensus', 'company', 'engine')},
    'probabilities': PROB, 'expected_price': round(ev['expected_price'], 1), 'expected_return': round(ev['expected_return'], 3),
    'asymmetry': {'downside_pct': round(down, 3), 'upside_pct': round(up, 3), 'ratio': round(ratio, 2), 'convex': False},
    'decision': dec,
    'entry_zones': {'alpha': ALPHA, 'Z1': round(z['Z1'], 1), 'Z2': round(z['Z2'], 1), 'zone': z['zone']},
    'steady_state': {'steady_earnings_usd_mn': round(ss_earn, 0), 'steady_state_value_usd_bn': round(split['steady_state_value'] / 1000, 1),
                     'growth_price_usd_bn': round(split['growth_price'] / 1000, 1), 'growth_share': round(split['growth_share_of_mcap'], 3)},
    'value_time_split': {'within_3y': round(pv3 / PRICE, 3), 'beyond_3y': round(1 - pv3 / PRICE, 3)},
    'cap_years': 12, 'incremental_roic': f'SBC前 約{roic_pre:.0%}・SBC控除後 約{roic_post:.0%}(マジックナンバー{magic:.2f}からの粗い推計)。資本コスト9%を上回る',
    'current_multiples': {k: round(v, 3) for k, v in mult.items()},
    'growth': {'revenue_yoy_latest_q': round(yoy(REV, '2026Q2'), 3), 'arr_or_proxy_yoy': 0.35, 'arr_proxy_name': 'cRPO(12か月以内に計上予定の残存履行義務)の前年比',
               'nnarr_or_proxy_yoy': round(coh['2026Q2']['new'] / coh['2025Q2']['new'] - 1, 3),
               'eps_cagr_3y_consensus': round(adj_cagr3, 3), 'eps_cagr_5y_engine': round(vl.cagr(ENG[2026]['beps'], ENG[2031]['beps'], 5), 3)},
    'rule_of_40': round(yoy(REV, '2026Q2') * 100 + fcf_ttm / rev_ttm * 100, 1),
    'triggers': {'upgrade': ['株価が分割エントリー圏の上限(Z2)以下に下落', 'DNR 122%以上かつ非GAAP営業利益率20%以上が2四半期続き、2027年ガイダンスが売上成長30%超(会社シナリオ経路の確度上昇)',
                             'SBC+給与税/売上が2027年に15%未満'],
                 'downgrade': ['DNR 115%未満が2四半期連続', '新規コホート売上の前年比がマイナス', '非GAAP粗利率が70%を下回る', 'SBC+給与税/売上が再び20%を超える'],
                 'exit': ['保有している場合: 株価が会社シナリオ経路の目標を上回ったまま、DNRが115%未満に低下', '大規模障害の再発で大口顧客の純増が2四半期連続で200社未満']},
    'one_line': (f'Cloudflare は既存顧客の拡張(DNR 120%)と新規コホートの二つのエンジンで年7億ドル規模でも成長を加速させる優良企業(構造評価A)だが、'
                 f'株価360.93ドルは事業エンジン経路の価値({T12["engine"]:.0f}ドル)の{PRICE/T12["engine"]:.1f}倍で、2033年まで年{impl_g*100:.0f}%の売上成長を織り込む。'
                 f'判断は「監視」。Z2({z["Z2"]:.0f}ドル)以下で分割エントリーを検討し、DNR・SBC比率・営業利益率で四半期ごとに確度を更新する'),
    'data_corrections': 9, 'known_constraints': 12,
}
with open(f'{OUT}/NET_summary.json', 'w') as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
P('\nsummary.json / F13 / F18 / F10 / F10b / F12 を書き出した')
