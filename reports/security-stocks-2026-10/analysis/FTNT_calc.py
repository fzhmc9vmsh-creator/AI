"""FTNT(Fortinet、12月決算)の計算スクリプト。報告書 analysis/FTNT_report.md の数値はすべてこの出力と一致させる。

実行: python3 analysis/FTNT_calc.py  → 標準出力に全結果、analysis/FTNT_F13.csv・F18.csv・F10.csv・FTNT_calc_out.json を書き出す。
規約: 00_standard.md(§3 事業実態EPS、§3-1 株数、§3-2 定常状態経由、§4 12か月目標株価)、valuation_lib.py。
入力の出所は報告書 Appendix B・F。取得日はすべて 2026-10-11。
"""
import sys
import csv
import json
import math
import datetime as dt

import numpy as np

sys.path.insert(0, '/home/user/AI/reports/security-stocks-2026-10/build')
import valuation_lib as vl  # noqa: E402

OUT = '/home/user/AI/reports/security-stocks-2026-10/analysis/'
R = vl.COST_OF_CAPITAL
TAX = 0.18          # 会社の non-GAAP 税率(2026年ガイダンスの前提 18%)
PRICE = 194.75      # 2026-10-09 終値(Yahoo・CNN。統括確認)
BASIC_SH = 733.6    # 2026-06-30 発行済株式数(10-Q)
DIL_NOW = 743.0     # 希薄化後株数: 2026Q3 ガイダンス 741〜745 の中央値
CASH_INV = 4468.7   # 2026-06-30 現金+短期・長期投資(10-Q 要約、二次)
DEBT = 500.0        # 2.2% 2031年満期社債(元本)
NET_CASH = CASH_INV - DEBT
MCAP = PRICE * BASIC_SH
EV = MCAP - NET_CASH
FY = lambda y: dt.date(y, 12, 31)  # noqa: E731

def p(*a):
    print(*a)

def hdr(t):
    print('\n' + '=' * 8 + ' ' + t + ' ' + '=' * 8)

# ---------------------------------------------------------------------------
# A. 年度データ(US$ mn)。2021・2022 は会社リリース(2023-02)、2019 は会社リリース、2023〜2025 は会社リリース・10-K 要約
# ---------------------------------------------------------------------------
hdr('A. 年度データ')
ann = {
    2019: dict(prod=788.5),
    2021: dict(prod=1260.0, serv=2090.0, rev=3342.0, bill=4180.0),
    2022: dict(prod=1780.0, serv=2640.0, rev=4417.0, bill=5590.0),
    2023: dict(prod=1927.0, rev=5305.0, bill=6400.0, eps_adj=1.63, om_adj=0.284, fcf=1730.0),
    2024: dict(prod=1909.0, rev=5956.0, bill=6534.0, eps_adj=2.37, sbc=260.2, fcf=1880.0, sh=771.9),
    2025: dict(prod=2218.2, rev=6800.0, bill=7550.0, eps_adj=2.76, sbc=282.1, fcf=2210.0, sh=764.6, ocf=2590.6),
}
for y in (2023, 2024, 2025):
    ann[y]['serv'] = ann[y]['rev'] - ann[y]['prod']
DR_END = {2025: 7115.8}  # 2025-12-31 繰延収益(流動 3,636.0 + 固定 3,479.8、Q2 2026 リリース)
for y in (2025, 2024, 2023):  # 恒等式 DR_{t-1} = DR_t − (billings_t − 売上_t)
    DR_END[y - 1] = DR_END[y] - (ann[y]['bill'] - ann[y]['rev'])
for y in sorted(ann):
    p(y, {k: round(v, 1) for k, v in ann[y].items()})
p('繰延収益(期末、算出):', {k: round(v) for k, v in sorted(DR_END.items())})

# 製品売上のサイクル(2019年起点の長期トレンドとの比較)
prod_hist = {y: ann[y]['prod'] for y in (2019, 2021, 2022, 2023, 2024, 2025)}
xs = np.array(list(prod_hist.keys()), dtype=float)
ys = np.log(np.array(list(prod_hist.values())))
b, a = np.polyfit(xs, ys, 1)
trend = {y: math.exp(a + b * y) for y in range(2019, 2032)}
p(f'製品売上の対数線形トレンド(2019・2021〜2025、2020は欠損): 年率 {math.exp(b)-1:.1%}')
for y in (2019, 2021, 2022, 2023, 2024, 2025):
    p(f'  {y}: 実績 {prod_hist[y]:.0f} / トレンド {trend[y]:.0f} / 乖離 {prod_hist[y]/trend[y]-1:+.1%}')
PROD26 = {'engine': 2960.0, 'consensus': 3000.0, 'company': 3000.0, 'bear': 2940.0}
p(f'  2026E(エンジン) 製品 {PROD26["engine"]:.0f} / トレンド {trend[2026]:.0f} / 乖離 {PROD26["engine"]/trend[2026]-1:+.1%}')
# 2019→2025 の製品CAGR(サイクルを1周含む)
p(f'製品CAGR 2019→2025: {vl.cagr(788.5, 2218.2, 6):.1%}、2019→2024(谷の年): {vl.cagr(788.5, 1909.0, 5):.1%}、'
  f'2022→2024(前回の消化期): {vl.cagr(1780, 1909, 2):.1%}')
# 前回サイクルの形: 2021 +?、2022 +41.9%、2023 +8.3%、2024 −0.9%
for y in (2022, 2023, 2024, 2025):
    prev = ann[y - 1]['prod']
    p(f'  製品成長 {y}: {ann[y]["prod"]/prev-1:+.1%}')
# 2026 年ガイダンスが含意する製品売上(売上中央値 − サービス中央値)
g_rev_mid, g_serv_mid = 8100.0, 5200.0
h1_prod, h1_serv = 645.0 + 773.0, 1204.5 + 1274.9
p(f'2026年ガイダンス含意: 製品 {g_rev_mid-g_serv_mid:.0f}(+{(g_rev_mid-g_serv_mid)/2218.2-1:.1%})、'
  f'下期製品 {g_rev_mid-g_serv_mid-h1_prod:.0f}(前年下期 {559.3+691.0:.0f} 比 {(g_rev_mid-g_serv_mid-h1_prod)/(559.3+691.0)-1:+.1%})')

# 更新サイクル(EoS コホート)の金額規模(Rosenblatt 2025-08: 65万台で4.5億ドル、40〜50%消化)
eos_total = 450.0
eos_left_2026 = eos_total * (1 - 0.45)
p(f'2026年 EoS コホートの残り(推計): {eos_left_2026:.0f}(2026年製品増分 {PROD26["engine"]-2218.2:.0f} の {eos_left_2026/(PROD26["engine"]-2218.2):.0%})')

# ---------------------------------------------------------------------------
# B. サービスのエンジン式(導入基盤→サービス請求→繰延収益→サービス売上)と再構成テスト
# ---------------------------------------------------------------------------
hdr('B. サービスのエンジン式')
# 2026E はガイダンス中央値(billings 9,450、サービス売上 5,200)と製品 2,950 を校正点に使う
cal = {
    2023: dict(P=ann[2023]['prod'], Sr=ann[2023]['serv'], Sb=ann[2023]['bill'] - ann[2023]['prod']),
    2024: dict(P=ann[2024]['prod'], Sr=ann[2024]['serv'], Sb=ann[2024]['bill'] - ann[2024]['prod']),
    2025: dict(P=ann[2025]['prod'], Sr=ann[2025]['serv'], Sb=ann[2025]['bill'] - ann[2025]['prod']),
    2026: dict(P=2950.0, Sr=5200.0, Sb=9450.0 - 2950.0),
}
for y, d in cal.items():
    p(y, {k: round(v) for k, v in d.items()}, f'サービス請求の伸び {d["Sb"]/cal[y-1]["Sb"]-1:+.1%}' if y - 1 in cal else '')
# (1) サービス請求 = k1 × 前年サービス売上 + k2 × 当年製品売上(2024〜2026E の最小二乗)
A = np.array([[cal[y - 1]['Sr'], cal[y]['P']] for y in (2024, 2025, 2026)])
yb = np.array([cal[y]['Sb'] for y in (2024, 2025, 2026)])
(k1, k2), *_ = np.linalg.lstsq(A, yb, rcond=None)
# (2) サービス売上 = c × (前期末繰延収益 + 当年サービス請求)(2024・2025 の平均)
cs = {y: cal[y]['Sr'] / (DR_END[y - 1] + cal[y]['Sb']) for y in (2023, 2024, 2025)}
c = (cs[2024] + cs[2025]) / 2
p(f'k1(既存サービス基盤の請求係数)={k1:.3f}、k2(製品1ドル当たりのサービス請求)={k2:.3f}、c(認識率)={c:.4f}')
p('c の年次:', {y: round(v, 4) for y, v in cs.items()})
# 再構成テスト: 前年の係数で当年のサービス売上・総売上を再構成(±5%以内が合格)
recon = {}
for y, cy in ((2024, cs[2023]), (2025, cs[2024])):
    sr = cy * (DR_END[y - 1] + cal[y]['Sb'])
    tot = sr + cal[y]['P']
    recon[y] = dict(serv_model=sr, serv_actual=cal[y]['Sr'], err_serv=sr / cal[y]['Sr'] - 1,
                    rev_model=tot, rev_actual=ann[y]['rev'], err_rev=tot / ann[y]['rev'] - 1)
    p(f'再構成 {y}: サービス {sr:.0f} vs 実績 {cal[y]["Sr"]:.0f}({sr/cal[y]["Sr"]-1:+.1%})、総売上 {tot:.0f} vs {ann[y]["rev"]:.0f}({tot/ann[y]["rev"]-1:+.1%})')
# 2026E をエンジン式(2025年の係数)で予測した値とガイダンスの比較(サンプル外)
sb26 = k1 * cal[2025]['Sr'] + k2 * 2950.0
sr26 = c * (DR_END[2025] + sb26)
p(f'2026E 予測: サービス請求 {sb26:.0f}(ガイダンス含意 6,500)、サービス売上 {sr26:.0f}(ガイダンス 5,180〜5,220)')
# 導入基盤の利回り(直近4年の製品売上 × 利回り)
ib4 = {y: sum(ann[z]['prod'] for z in range(y - 3, y + 1)) for y in (2024, 2025)}
p('4年導入基盤の利回り:', {y: round(ann[y]['serv'] / ib4[y], 3) for y in ib4})

# ---------------------------------------------------------------------------
# C. 四半期 KPI(F18・F10)
# ---------------------------------------------------------------------------
hdr('C. 四半期 KPI')
Q = ['2024Q1', '2024Q2', '2024Q3', '2024Q4', '2025Q1', '2025Q2', '2025Q3', '2025Q4', '2026Q1', '2026Q2']
prod_q = [409.0, 451.9, 473.9, 574.0, 459.0, 508.9, 559.3, 691.0, 645.0, 773.0]
tot_q = [1353.4, 1434.3, 1508.2, 1660.1, 1538.9, 1630.0, 1724.8, 1906.3, 1849.5, 2047.9]
serv_q = [t - pq for t, pq in zip(tot_q, prod_q)]
bill_q = [1414.0, 1540.0, 1580.0, 2000.0, 1600.0, 1780.0, 1810.0, 2370.0, 2090.0, 2370.0]
om_q = [28.5, 35.1, 36.1, 39.0, 34.2, 33.0, 36.9, 37.0, 35.8, 38.0]

def kpi_rows(name, vals, seasonal=True):
    rows = []
    for i, qn in enumerate(Q):
        v = vals[i]
        qoq = ((v / vals[i - 1]) ** 4 - 1) if i >= 1 else None
        yoy = (v / vals[i - 4] - 1) if i >= 4 else None
        ttm = (sum(vals[i - 3:i + 1]) / sum(vals[i - 7:i - 3]) - 1) if i >= 7 else None
        prev_yoy = (vals[i - 1] / vals[i - 5] - 1) if i >= 5 else None
        d2 = (yoy - prev_yoy) if (yoy is not None and prev_yoy is not None) else None
        rows.append(dict(kpi=name, period=qn, value=round(v, 1),
                         qoq_annualized=None if qoq is None else round(qoq, 4),
                         yoy=None if yoy is None else round(yoy, 4),
                         ttm_yoy=None if ttm is None else round(ttm, 4),
                         second_diff=None if d2 is None else round(d2, 4)))
    return rows

f18 = []
for nm, vals in (('製品売上', prod_q), ('サービス売上', serv_q), ('billings', bill_q), ('総売上', tot_q)):
    f18 += kpi_rows(nm, vals)
# 営業利益率は水準と前年差(pp)のみ
for i, qn in enumerate(Q):
    f18.append(dict(kpi='non-GAAP営業利益率(%)', period=qn, value=om_q[i], qoq_annualized=None,
                    yoy=None if i < 4 else round((om_q[i] - om_q[i - 4]) / 100, 4), ttm_yoy=None,
                    second_diff=None if i < 5 else round(((om_q[i] - om_q[i - 4]) - (om_q[i - 1] - om_q[i - 5])) / 100, 4)))
# 繰延収益(開示のある時点のみ)
dr_pts = [('2025Q2', 7675.7 / 1.17), ('2025Q4', 7115.8), ('2026Q1', 7350.0), ('2026Q2', 7675.7)]
for qn, v in dr_pts:
    f18.append(dict(kpi='繰延収益(期末)', period=qn, value=round(v, 1), qoq_annualized=None,
                    yoy=0.17 if qn == '2026Q2' else (0.15 if qn == '2026Q1' else None), ttm_yoy=None, second_diff=None))
with open(OUT + 'FTNT_F18.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['kpi', 'period', 'value', 'qoq_annualized', 'yoy', 'ttm_yoy', 'second_diff'])
    w.writeheader()
    w.writerows(f18)
for r_ in f18:
    if r_['period'] in ('2025Q4', '2026Q1', '2026Q2'):
        p(r_)
with open(OUT + 'FTNT_F10.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['period', 'line', 'revenue_usd_mn'])
    for i, qn in enumerate(Q):
        w.writerow([qn, '製品(FortiGate機器・ソフトライセンス)', round(prod_q[i], 1)])
        w.writerow([qn, 'サービス(FortiGuard・FortiCare・SASE・SecOps)', round(serv_q[i], 1)])
    for y in (2021, 2022, 2023, 2024, 2025):
        w.writerow([f'FY{y}', '製品(FortiGate機器・ソフトライセンス)', round(ann[y]['prod'], 1)])
        w.writerow([f'FY{y}', 'サービス(FortiGuard・FortiCare・SASE・SecOps)', round(ann[y]['serv'], 1)])
p('製品比率 2026Q2:', round(prod_q[-1] / tot_q[-1], 3), ' 2025Q2:', round(prod_q[5] / tot_q[5], 3))
# 営業レバレッジ: 増収分のうち増益に落ちた比率(non-GAAP 営業利益、前年同期比)
for i in (8, 9):
    d_rev = tot_q[i] - tot_q[i - 4]
    d_oi = tot_q[i] * om_q[i] / 100 - tot_q[i - 4] * om_q[i - 4] / 100
    p(f'{Q[i]} 増収 {d_rev:.0f} → 増益 {d_oi:.0f}(限界利益率 {d_oi/d_rev:.0%})')
# 2026Q2 の製品・サービス粗利率(GAAP、リリース)
p(f'2026Q2 粗利率: 製品 {539.2/773.0:.1%}、サービス {1104.0/1274.9:.1%}')
# 上期の FCF と non-GAAP 営業利益
h1_fcf = 1010.0 + 966.0
h1_oi = 1849.5 * 0.358 + 2047.9 * 0.380
p(f'2026上期 FCF {h1_fcf:.0f} vs non-GAAP 営業利益 {h1_oi:.0f}(比 {h1_fcf/h1_oi:.2f})、繰延収益の増加 {7675.7-7115.8:.0f}')
fcf_ttm = (2210.0 - 782.8 - 577.4 - 300.0) + 577.4 + 1010.0 + 966.0  # 2025Q3 は通期から差し引き(2025Q2 を約300と推計)
rev_ttm = sum(tot_q[-4:])
sbc_ttm = 72.2 + 73.1 + 73.2 + 80.8
p(f'TTM: 売上 {rev_ttm:.0f}、FCF(推計) {fcf_ttm:.0f}(マージン {fcf_ttm/rev_ttm:.1%})、SBC {sbc_ttm:.1f}(売上比 {sbc_ttm/rev_ttm:.2%})')
p(f'FY2025: FCF マージン {2210/6800:.1%}、SBC控除後 FCF {2210-282.1:.0f}({(2210-282.1)/6800:.1%})')

# ---------------------------------------------------------------------------
# D. EPS 品質フォレンジック(対数分解、non-GAAP)
# ---------------------------------------------------------------------------
hdr('D. EPS 対数分解')
ni = {y: ann[y]['eps_adj'] * ann[y]['sh'] for y in (2024, 2025)}
dec = vl.eps_log_decomposition(ann[2024]['rev'], ann[2025]['rev'], ni[2024] / ann[2024]['rev'], ni[2025] / ann[2025]['rev'],
                               ann[2024]['sh'], ann[2025]['sh'])
p('2024→2025:', {k: round(v, 4) for k, v in dec.items()}, ' ln(EPS比)=', round(math.log(2.76 / 2.37), 4))
ni26 = 3.51 * 743.0
dec2 = vl.eps_log_decomposition(6800, 8250, ni[2025] / 6800, ni26 / 8250, 764.6, 743.0)
p('2025→2026E(コンセンサス):', {k: round(v, 4) for k, v in dec2.items()}, ' ln(EPS比)=', round(math.log(3.51 / 2.76), 4))
# 受取利息の寄与(2026E: 純受取利息 約150 を仮定)
p(f'受取利息の EPS 寄与(2026E): {150*(1-TAX)/743:.3f} ドル(調整後EPSの {150*(1-TAX)/743/3.51:.1%})、金利 −100bp で {-CASH_INV*0.01*(1-TAX)/743:.3f}')

# ---------------------------------------------------------------------------
# E. 経路別のEPS(コンセンサス/会社シナリオ/事業エンジン/弱気)
# ---------------------------------------------------------------------------
hdr('E. 経路別EPS')
YEARS = list(range(2026, 2035))   # 2032〜2034 は g(3年)計算用の延長
SH_G = (764.6 / 786.2) ** 0.5 - 1  # 過去2年の希薄化後株数の年変化率(00_standard §3-1)
shares = {2026: 743.0}
for y in YEARS[1:]:
    shares[y] = shares[y - 1] * (1 + SH_G)
p(f'株数の年変化率(2023 786.2 → 2025 764.6): {SH_G:.2%}', {y: round(v, 1) for y, v in shares.items() if y <= 2031})
SBC_RATIO = {2026: 0.039, 2027: 0.039, 2028: 0.0385, 2029: 0.038, 2030: 0.0375, 2031: 0.037, 2032: 0.037, 2033: 0.037, 2034: 0.037}

def sbc_path(rev):
    out, prev = {}, 282.1
    for y in YEARS:
        v = max(SBC_RATIO[y] * rev[y], prev * 1.05)
        out[y] = v
        prev = v
    return out

def engine_model(prod_g, k1m=1.0, opex_g=None, gm_p=None, gm_s=0.875, other=150.0, p26=2960.0, k1_drift=0.0):
    """製品の成長率パス → サービス請求 → 繰延収益 → サービス売上 → 粗利 → 営業利益 → 調整後EPS → 事業実態EPS。"""
    P, Sb, Sr, DR, rev, opex, oi, adj, bus = {}, {}, {}, {}, {}, {}, {}, {}, {}
    sr_prev, dr_prev, op_prev = cal[2025]['Sr'], DR_END[2025], None
    for i, y in enumerate(YEARS):
        P[y] = p26 if y == 2026 else P[y - 1] * (1 + prod_g[y])
        kk = k1 * k1m * (1 + k1_drift) ** max(0, y - 2026)
        Sb[y] = kk * sr_prev + k2 * P[y]
        Sr[y] = c * (dr_prev + Sb[y])
        DR[y] = dr_prev + Sb[y] - Sr[y]
        rev[y] = P[y] + Sr[y]
        gp = P[y] * gm_p[y] + Sr[y] * gm_s
        opex[y] = 3615.0 if y == 2026 else op_prev * (1 + opex_g[y])
        oi[y] = gp - opex[y]
        adj[y] = (oi[y] + other) * (1 - TAX) / shares[y]
        sr_prev, dr_prev, op_prev = Sr[y], DR[y], opex[y]
    sbc = sbc_path(rev)
    for y in YEARS:
        bus[y] = vl.business_eps_fixed_shares(adj[y], shares[y], sbc[y], shares[y], tax=TAX)
    om = {y: oi[y] / rev[y] for y in YEARS}
    return dict(P=P, Sb=Sb, Sr=Sr, DR=DR, rev=rev, opex=opex, oi=oi, om=om, adj=adj, sbc=sbc, bus=bus,
                bill={y: P[y] + Sb[y] for y in YEARS})

# 製品成長率のパス(価格・構成・台数の分解は報告書 3章・10章)
PG = {
    'engine':  {2027: -0.06, 2028: 0.05, 2029: 0.08, 2030: 0.08, 2031: 0.07, 2032: 0.06, 2033: 0.05, 2034: 0.05},
    'company': {2027: 0.06, 2028: 0.09, 2029: 0.10, 2030: 0.10, 2031: 0.09, 2032: 0.08, 2033: 0.07, 2034: 0.06},
    'bear':    {2027: -0.18, 2028: -0.03, 2029: 0.05, 2030: 0.06, 2031: 0.06, 2032: 0.05, 2033: 0.04, 2034: 0.04},
}
OPEX_G = {
    'engine':  {y: 0.09 for y in YEARS[1:]},
    'company': {y: 0.105 for y in YEARS[1:]},
    'bear':    {2027: 0.05, 2028: 0.05, **{y: 0.07 for y in YEARS[3:]}},
}
GMP = {
    'engine':  {2026: 0.695, 2027: 0.685, 2028: 0.68, **{y: 0.68 for y in YEARS[3:]}},
    'company': {2026: 0.70, 2027: 0.70, 2028: 0.695, **{y: 0.69 for y in YEARS[3:]}},
    'bear':    {2026: 0.69, 2027: 0.66, 2028: 0.66, **{y: 0.67 for y in YEARS[3:]}},
}
M = {
    'engine': engine_model(PG['engine'], opex_g=OPEX_G['engine'], gm_p=GMP['engine'], p26=PROD26['engine']),
    'company': engine_model(PG['company'], opex_g=OPEX_G['company'], gm_p=GMP['company'], p26=PROD26['company'], k1_drift=0.01),
    'bear': engine_model(PG['bear'], k1m=0.98, opex_g=OPEX_G['bear'], gm_p=GMP['bear'], p26=PROD26['bear']),
}
for nm, m in M.items():
    p(f'--- {nm}')
    for y in YEARS[:6]:
        p(f'  {y}: 製品 {m["P"][y]:.0f} サービス {m["Sr"][y]:.0f}({m["Sr"][y]/(m["Sr"][y-1] if y>2026 else cal[2025]["Sr"])-1:+.1%}) '
          f'売上 {m["rev"][y]:.0f}({m["rev"][y]/(m["rev"][y-1] if y>2026 else 6800)-1:+.1%}) billings {m["bill"][y]:.0f} '
          f'OM {m["om"][y]:.1%} 調整後EPS {m["adj"][y]:.2f} SBC {m["sbc"][y]:.0f} 事業実態EPS {m["bus"][y]:.2f}')

# コンセンサス経路(調整後EPS: 2026 3.51 / 2027 3.87 / 2028 4.41。WallStreetZen・StocksGuide、2026-08〜09表示)
CONS_ADJ = {2026: 3.51, 2027: 3.87, 2028: 4.41}
CONS_REV = {2026: 8250.0, 2027: 9000.0, 2028: 9900.0}
# 2029 以降は延長: 事業エンジン経路の調整後EPS・売上の成長率で延ばす(延長部分と明記)
for y in YEARS:
    if y > 2028:
        CONS_ADJ[y] = CONS_ADJ[y - 1] * M['engine']['adj'][y] / M['engine']['adj'][y - 1]
        CONS_REV[y] = CONS_REV[y - 1] * M['engine']['rev'][y] / M['engine']['rev'][y - 1]
cons_sbc = sbc_path(CONS_REV)
CONS_BUS = {y: vl.business_eps_fixed_shares(CONS_ADJ[y], shares[y], cons_sbc[y], shares[y], tax=TAX) for y in YEARS}
p('--- consensus')
for y in YEARS[:6]:
    p(f'  {y}: 売上 {CONS_REV[y]:.0f} 調整後EPS {CONS_ADJ[y]:.2f} SBC {cons_sbc[y]:.0f}({cons_sbc[y]/CONS_REV[y]:.2%}) 事業実態EPS {CONS_BUS[y]:.3f}'
      f'({CONS_BUS[y]/CONS_ADJ[y]:.0%}){" *延長" if y > 2028 else ""}')
# 代替コンセンサス(StockAnalysis: 2026 3.45 / 2027 3.78)
alt = {2026: 3.45, 2027: 3.78}
p('代替コンセンサス事業実態EPS:', {y: round(vl.business_eps_fixed_shares(alt[y], shares[y], cons_sbc[y], shares[y], tax=TAX), 3) for y in alt})

PATHS = {'consensus': {'adj': CONS_ADJ, 'bus': CONS_BUS, 'rev': CONS_REV, 'sbc': cons_sbc}}
for nm in ('company', 'engine', 'bear'):
    PATHS[nm] = {'adj': M[nm]['adj'], 'bus': M[nm]['bus'], 'rev': M[nm]['rev'], 'sbc': M[nm]['sbc']}
p('\n事業実態EPS÷調整後EPS(2026):', {k: round(v['bus'][2026] / v['adj'][2026], 3) for k, v in PATHS.items()})
p('エンジン vs コンセンサス(事業実態EPS):', {y: f'{M["engine"]["bus"][y]/CONS_BUS[y]-1:+.1%}' for y in (2026, 2027, 2028)})
p('エンジン vs コンセンサス(売上):', {y: f'{M["engine"]["rev"][y]/CONS_REV[y]-1:+.1%}' for y in (2026, 2027, 2028)})

# ---------------------------------------------------------------------------
# F. 許容PEG・年度別適正株価(F13)・12か月目標株価
# ---------------------------------------------------------------------------
hdr('F. PEG・F13・目標株価')
PEG_BY_FY = {2026: (1.5, 1.8), 2027: (1.4, 1.7), 2028: (1.5, 1.8), 2029: (1.5, 1.8), 2030: (1.4, 1.7), 2031: (1.3, 1.6)}
PEG_ADOPT = (1.4, 1.8)
f13 = []
for nm, pth in PATHS.items():
    for y in range(2026, 2032):
        e0, e3 = pth['bus'][y], pth['bus'][y + 3]
        g3 = vl.cagr(e0, e3, 3)
        lo, hi = PEG_BY_FY[y]
        fl, fh = vl.fair_per(lo, g3), vl.fair_per(hi, g3)
        f13.append(dict(fy_end=f'{y}-12-31', path=nm, business_eps=round(e0, 3), g_3y=round(g3, 4), peg_low=lo, peg_high=hi,
                        fair_per_low=round(fl['capped'], 1), fair_per_high=round(fh['capped'], 1),
                        fair_price_low=round(fl['capped'] * e0, 1), fair_price_high=round(fh['capped'] * e0, 1),
                        is_extension=(nm == 'consensus' and y + 3 > 2028) or y + 3 > 2031))
with open(OUT + 'FTNT_F13.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(f13[0].keys()))
    w.writeheader()
    w.writerows(f13)
for r_ in f13:
    p(r_)

# 12か月目標株価: 2027-10-11 時点の NTM 事業実態EPS × 妥当PER(PEG × g)。g は NTM(2027-10) → NTM(2030-10) の CAGR
TGT = {}
for nm, pth in PATHS.items():
    eps_map = {FY(y): pth['bus'][y] for y in YEARS}
    ntm27 = vl.ntm_eps(eps_map, dt.date(2027, 10, 11))
    ntm30 = vl.ntm_eps(eps_map, dt.date(2030, 10, 11))
    g = vl.cagr(ntm27, ntm30, 3)
    lo = vl.target_price(ntm27, PEG_ADOPT[0], g)
    hi = vl.target_price(ntm27, PEG_ADOPT[1], g)
    mid = vl.target_price(ntm27, sum(PEG_ADOPT) / 2, g)
    adj_map = {FY(y): pth['adj'][y] for y in YEARS}
    TGT[nm] = dict(ntm=ntm27, g=g, per=mid['per'], price=mid['price'], low=lo['price'], high=hi['price'],
                   price_uncapped=mid['price_uncapped'], gap=vl.gap(mid['price'], PRICE),
                   ntm_adj=vl.ntm_eps(adj_map, dt.date(2027, 10, 11)))
    p(f'{nm}: NTM事業実態EPS(2027-10) {ntm27:.3f}、g {g:.1%}、妥当PER {mid["per"]:.1f}(PEG 1.6)、目標 {mid["price"]:.1f}'
      f'(1.4〜1.8: {lo["price"]:.1f}〜{hi["price"]:.1f})、乖離 {vl.gap(mid["price"], PRICE):+.1%}、NTM調整後EPS {TGT[nm]["ntm_adj"]:.2f}')

# 定常状態経由の目標株価(00_standard §3-2): FY+5 = FY2031、出口g = FY2031→FY2034 の CAGR、出口PEG 1.0〜2.0(CAP根拠で 1.6)
SST = {}
for nm, pth in PATHS.items():
    g_exit = vl.cagr(pth['bus'][2031], pth['bus'][2034], 3)
    res = {pe: vl.steady_state_target(pth['bus'][2031], FY(2031), pe, g_exit) for pe in (1.0, 1.6, 2.0)}
    SST[nm] = dict(eps2031=pth['bus'][2031], g_exit=g_exit, **{f'peg{pe}': res[pe]['target'] for pe in res},
                   per_exit=res[1.6]['per_exit'])
    p(f'定常状態経由 {nm}: EPS2031 {pth["bus"][2031]:.2f}、出口g {g_exit:.1%}、出口PER(PEG1.6) {res[1.6]["per_exit"]:.1f}、'
      f'目標 PEG1.0 {res[1.0]["target"]:.1f} / 1.6 {res[1.6]["target"]:.1f} / 2.0 {res[2.0]["target"]:.1f}')

# ---------------------------------------------------------------------------
# G. 交差確認: DCF(オーナー利益=事業実態純利益)、リバースDCF、市場が暗に置く値
# ---------------------------------------------------------------------------
hdr('G. DCF・リバースDCF')

def dcf_value(bus_eps: dict, fade_to=0.03, fade_end=2041, term_g=0.03, r=R, at=dt.date(2027, 10, 11), net_cash_ps=NET_CASH / DIL_NOW):
    """事業実態EPS(=1株当たりオーナー利益、SBC控除後)を 2031 まで経路どおり、以後 fade_end まで成長率を線形に fade_to へ下げ、
    以後は永久成長。各年の利益は年央受取として at 時点に割り引く。純現金を加える。"""
    eps = dict(bus_eps)
    g31 = eps[2031] / eps[2030] - 1
    for y in range(2032, fade_end + 1):
        w = (y - 2031) / (fade_end - 2031)
        eps[y] = eps[y - 1] * (1 + g31 + (fade_to - g31) * w)
    val = 0.0
    for y in range(2027, fade_end + 1):
        t_mid = (dt.date(y, 7, 1) - at).days / 365.25
        if y == 2027:
            frac = (dt.date(2027, 12, 31) - at).days / 365.0
            val += eps[y] * frac / (1 + r) ** max(t_mid, 0.1)
        else:
            val += eps[y] / (1 + r) ** t_mid
    t_end = (dt.date(fade_end, 12, 31) - at).days / 365.25
    val += eps[fade_end] * (1 + term_g) / (r - term_g) / (1 + r) ** t_end
    return val + net_cash_ps

DCF = {}
for nm, pth in PATHS.items():
    DCF[nm] = dcf_value({y: pth['bus'][y] for y in YEARS})
    p(f'DCF 価値(2027-10-11 時点、1株): {nm} {DCF[nm]:.1f}(現在価値に直すと {DCF[nm]/(1+R):.1f})')
# 株価 194.75 の現在(2026-10-11)価値を 2027-10 時点に置き直すと 194.75×1.09 = 212.3
need = PRICE * (1 + R)
p(f'株価を 2027-10 時点に置き直した必要価値: {need:.1f}')

# リバースDCF: 2026年の事業実態EPS(コンセンサス)から一定成長 g を N 年 → 以後 3% 永久成長。現在(2026-10-11)価値 = 株価 − 純現金
def rev_dcf(g, n, e0=CONS_BUS[2026], r=R, term_g=0.03):
    val, e = 0.0, e0
    for t in range(1, n + 1):
        e *= (1 + g)
        val += e / (1 + r) ** (t - 0.5)
    val += e * (1 + term_g) / (r - term_g) / (1 + r) ** n
    return val + NET_CASH / DIL_NOW

def solve_g(n):
    lo, hi = -0.05, 0.6
    for _ in range(100):
        mid = (lo + hi) / 2
        if rev_dcf(mid, n) < PRICE:
            lo = mid
        else:
            hi = mid
    return mid

RDCF = {n: solve_g(n) for n in (5, 10, 15)}
p('株価が織り込む事業実態EPSの成長率(その後3%永久):', {n: f'{g:.1%}' for n, g in RDCF.items()})

# 市場が暗に置く値(芯ごと): エンジン式の他の前提を固定し、DCF 価値 = 株価(2027-10 換算)になる値を解く
def solve_param(fn, lo, hi, target=need, increasing=True):
    for _ in range(80):
        mid = (lo + hi) / 2
        v = fn(mid)
        if (v < target) == increasing:
            lo = mid
        else:
            hi = mid
    return mid

def v_prod_long(gl):
    pg = dict(PG['engine'])
    for y in range(2028, 2035):
        pg[y] = gl
    m = engine_model(pg, opex_g=OPEX_G['engine'], gm_p=GMP['engine'], p26=PROD26['engine'])
    return dcf_value(m['bus'])

def v_k1(mult):
    m = engine_model(PG['engine'], k1m=mult, opex_g=OPEX_G['engine'], gm_p=GMP['engine'], p26=PROD26['engine'])
    return dcf_value(m['bus'])

def v_opex(og):
    m = engine_model(PG['engine'], opex_g={y: og for y in YEARS[1:]}, gm_p=GMP['engine'], p26=PROD26['engine'])
    return dcf_value(m['bus'])

imp_prod = solve_param(v_prod_long, 0.0, 0.40)
imp_k1 = solve_param(v_k1, 0.9, 1.4)
imp_opex = solve_param(v_opex, -0.05, 0.12, increasing=False)
m_imp = engine_model(PG['engine'], k1m=imp_k1, opex_g=OPEX_G['engine'], gm_p=GMP['engine'], p26=PROD26['engine'])
m_opx = engine_model(PG['engine'], opex_g={y: imp_opex for y in YEARS[1:]}, gm_p=GMP['engine'], p26=PROD26['engine'])
p(f'市場が暗に置く値: 製品の長期成長率(2028〜34) {imp_prod:.1%}(エンジン 5〜8%)')
p(f'  サービス請求係数の倍率 {imp_k1:.3f} → サービス売上 CAGR 2026→31 {vl.cagr(m_imp["Sr"][2026], m_imp["Sr"][2031], 5):.1%}'
  f'(エンジン {vl.cagr(M["engine"]["Sr"][2026], M["engine"]["Sr"][2031], 5):.1%})')
p(f'  費用の伸び {imp_opex:.1%}/年 → 2031年の営業利益率 {m_opx["om"][2031]:.1%}(エンジン {M["engine"]["om"][2031]:.1%})')

# ---------------------------------------------------------------------------
# H. 価値感度分析(芯の特定)— DCF 価値(2027-10、1株)の変化
# ---------------------------------------------------------------------------
hdr('H. 価値感度分析')
base_v = DCF['engine']
sens = []

def add(name, lo_v, hi_v, rng):
    sens.append((name, lo_v - base_v, hi_v - base_v, rng))

def run(pg=None, k1m=1.0, og=None, gmp=None, other=150.0, sbc_shift=0.0, fade_end=2041, term_g=0.03):
    m = engine_model(pg or PG['engine'], k1m=k1m, opex_g=og or OPEX_G['engine'], gm_p=gmp or GMP['engine'], other=other, p26=PROD26['engine'])
    bus = dict(m['bus'])
    if sbc_shift:
        for y in YEARS:
            bus[y] -= sbc_shift * m['rev'][y] * (1 - TAX) / shares[y]
    return dcf_value(bus, fade_end=fade_end, term_g=term_g)

pg_lo = dict(PG['engine']); pg_lo[2027] = -0.18
pg_hi = dict(PG['engine']); pg_hi[2027] = 0.06
add('2027年の製品売上(−18%〜+6%、基準−6%)', run(pg=pg_lo), run(pg=pg_hi), '−18%/+6%')
pg_l2 = dict(PG['engine']); pg_h2 = dict(PG['engine'])
for y in range(2029, 2035):
    pg_l2[y] = 0.03; pg_h2[y] = 0.12
add('製品の長期成長率 2029〜34(3%〜12%、基準5〜8%)', run(pg=pg_l2), run(pg=pg_h2), '3%/12%')
add('サービス請求係数 k1(±5%: サービス成長 ±約2pt/年)', run(k1m=0.95), run(k1m=1.05), '0.95/1.05')
add('費用の伸び(年+11%〜+7%: 営業利益率 ±約4pt)', run(og={y: 0.11 for y in YEARS[1:]}), run(og={y: 0.07 for y in YEARS[1:]}), '11%/7%')
add('競争優位期間(成長が3%に収束する年 2036〜2046)', run(fade_end=2036), run(fade_end=2046), '2036/2046')
add('永久成長率(2%〜4%)', run(term_g=0.02), run(term_g=0.04), '2%/4%')
add('SBC/売上(±0.5pt)', run(sbc_shift=0.005), run(sbc_shift=-0.005), '+0.5/−0.5pt')
add('受取利息(金利 ±100bp)', run(other=150.0 - 45.0), run(other=150.0 + 45.0), '−/+100bp')
gm_lo = {y: v - 0.03 for y, v in GMP['engine'].items()}
gm_hi = {y: v + 0.03 for y, v in GMP['engine'].items()}
add('製品粗利率(±3pt: メモリ価格)', run(gmp=gm_lo), run(gmp=gm_hi), '−3/+3pt')
sens.sort(key=lambda s: -(abs(s[1]) + abs(s[2])))
p(f'基準 DCF 価値(エンジン、2027-10): {base_v:.1f}')
for s in sens:
    p(f'  {s[0]}: {s[1]:+.1f} / {s[2]:+.1f}(幅 {abs(s[1])+abs(s[2]):.1f}、{(abs(s[1])+abs(s[2]))/base_v:.0%})')
# 12か月目標株価(規約)への感度: 2027年製品
for lab, pg in (('製品2027 −18%', pg_lo), ('製品2027 +6%', pg_hi)):
    m = engine_model(pg, opex_g=OPEX_G['engine'], gm_p=GMP['engine'], p26=PROD26['engine'])
    em = {FY(y): m['bus'][y] for y in YEARS}
    n27 = vl.ntm_eps(em, dt.date(2027, 10, 11)); n30 = vl.ntm_eps(em, dt.date(2030, 10, 11))
    p(f'  規約目標(PEG1.6) {lab}: NTM {n27:.2f} g {vl.cagr(n27, n30, 3):.1%} → {vl.target_price(n27, 1.6, vl.cagr(n27, n30, 3))["price"]:.1f}')

# ---------------------------------------------------------------------------
# I. 成長の値段・価値の時間分布・増分ROIC
# ---------------------------------------------------------------------------
hdr('I. 成長の値段')
# 定常状態利益: 2026年の正規化売上(製品をトレンド水準へ)× 定常状態の営業利益率(成長投資を止めた場合 50%、SBC 3.9% 控除)
prod_norm26 = trend[2026]
rev_norm26 = prod_norm26 + M['engine']['Sr'][2026]
ss_om = 0.50
ss_earn = (rev_norm26 * (ss_om - 0.039) + 150.0) * (1 - TAX)
split = vl.steady_state_split(ss_earn, MCAP)
p(f'正規化製品 {prod_norm26:.0f}、正規化売上 {rev_norm26:.0f}、定常状態利益 {ss_earn:.0f}、定常状態価値 {split["steady_state_value"]:.0f}、'
  f'成長の値段 {split["growth_price"]:.0f}({split["growth_share_of_mcap"]:.1%})')
# 参考: 2026年の事業実態純利益をそのまま資本化
bus_ni26 = CONS_BUS[2026] * 743.0
split2 = vl.steady_state_split(bus_ni26, MCAP)
p(f'参考: 2026E 事業実態純利益 {bus_ni26:.0f} → 定常状態価値 {split2["steady_state_value"]:.0f}、成長の値段 {split2["growth_share_of_mcap"]:.1%}')
for rr in (0.08, 0.10):
    p(f'  資本コスト {rr:.0%}: 定常状態価値 {ss_earn/rr:.0f}、成長の値段の比率 {1-ss_earn/rr/MCAP:.1%}')
# 価値の時間分布(エンジン DCF のうち 3 年以内=2027-10〜2030-10 の利益の現在価値)
eps_e = M['engine']['bus']
pv3 = sum(eps_e[y] / (1 + R) ** ((dt.date(y, 7, 1) - dt.date(2027, 10, 11)).days / 365.25) for y in (2028, 2029, 2030)) + eps_e[2027] * 0.22
p(f'価値の時間分布(エンジン DCF {base_v:.1f} 中): 3年以内 {pv3:.1f}({pv3/base_v:.1%})+純現金 {NET_CASH/DIL_NOW:.1f}、それ以降 {base_v-pv3-NET_CASH/DIL_NOW:.1f}')
within3 = (pv3 + NET_CASH / DIL_NOW) / base_v
# 増分ROIC(推計): 2024→2026E の事業実態NOPAT増分 ÷ 増分投下資本
nopat24 = (5956 * 0.341 - 260.2) * (1 - TAX)
nopat26 = (M['engine']['oi'][2026] - M['engine']['sbc'][2026]) * (1 - TAX)
d_cap = (378 + 381 + 300) - 3 * 180 + 450 - (DR_END[2025] - DR_END[2023] + 1300)   # capex − 減価償却 + 運転資本(在庫・債権)− 前受金の増加
p(f'事業実態NOPAT 2024 {nopat24:.0f} → 2026E {nopat26:.0f}(増分 {nopat26-nopat24:.0f})、増分投下資本(推計) {d_cap:.0f}')
d_cap_norm = 2 * ((380 - 180) + 200 - 500)
p(f'前受金の増加を平年並み(年500)に置いた増分投下資本 {d_cap_norm:.0f} → 増分ROIC {"算出不能(資本が減る)" if d_cap_norm <= 0 else f"{(nopat26-nopat24)/d_cap_norm:.0%}"}')
d_cap_norm2 = 2 * ((380 - 180) + 200 - 250) + 2 * 300  # 研究開発費の資本化分(年+300)を投下資本に含める保守的な版
p(f'保守的な版(R&D資本化+前受金の増加 年250): 増分投下資本 {d_cap_norm2:.0f} → 増分ROIC {(nopat26-nopat24)/d_cap_norm2:.0%}')

# ---------------------------------------------------------------------------
# J. 現在の倍率・成長
# ---------------------------------------------------------------------------
hdr('J. 現在の倍率')
cb = {FY(y): CONS_BUS[y] for y in YEARS}
ca = {FY(y): CONS_ADJ[y] for y in YEARS}
ntm_now_b = vl.ntm_eps(cb, dt.date(2026, 10, 11))
ntm_now_a = vl.ntm_eps(ca, dt.date(2026, 10, 11))
g_b3 = vl.cagr(CONS_BUS[2026], CONS_BUS[2029], 3)
g_a3 = vl.cagr(CONS_ADJ[2026], CONS_ADJ[2029], 3)
rev_ntm = CONS_REV[2026] * 3 / 12 + CONS_REV[2027] * 9 / 12
fcf_ntm = 3000.0
mult = dict(per_business_ntm=PRICE / ntm_now_b, per_adj_ntm=PRICE / ntm_now_a,
            peg_business_3y=PRICE / ntm_now_b / (g_b3 * 100), peg_adj_3y=PRICE / ntm_now_a / (g_a3 * 100),
            ev_sales_ntm=EV / rev_ntm, ev_fcf_ntm=EV / fcf_ntm, fcf_margin_ttm=fcf_ttm / rev_ttm, sbc_to_revenue_ttm=sbc_ttm / rev_ttm)
p(f'時価総額 {MCAP:.0f}、純現金 {NET_CASH:.0f}、EV {EV:.0f}')
p(f'NTM(2026-10) 事業実態EPS {ntm_now_b:.3f}、調整後 {ntm_now_a:.3f}; g3 事業実態 {g_b3:.1%}、調整後 {g_a3:.1%}')
p({k: round(v, 3) for k, v in mult.items()})
g5_cons = vl.cagr(CONS_BUS[2026], CONS_BUS[2031], 5)
g5_eng = vl.cagr(M['engine']['bus'][2026], M['engine']['bus'][2031], 5)
g5_comp = vl.cagr(M['company']['bus'][2026], M['company']['bus'][2031], 5)
g5_bear = vl.cagr(M['bear']['bus'][2026], M['bear']['bus'][2031], 5)
p(f'5年CAGR(事業実態EPS 2026→2031): コンセンサス(延長含む) {g5_cons:.1%}、会社 {g5_comp:.1%}、エンジン {g5_eng:.1%}、弱気 {g5_bear:.1%}')
for nm, g5 in (('consensus', g5_cons), ('company', g5_comp), ('engine', g5_eng)):
    p(f'  条件6 PEG(現在のNTM事業実態PER ÷ 5年CAGR) {nm}: {mult["per_business_ntm"]/(g5*100):.2f}')
cagr3_adj_cons = vl.cagr(3.51, 4.41, 2)
p(f'調整後EPS CAGR 2026→2028(コンセンサス): {cagr3_adj_cons:.1%}')
rule40 = 0.26 + mult['fcf_margin_ttm']
p(f'Rule of 40(直近四半期の売上成長 26% + TTM FCFマージン): {rule40:.2f}; FY2025 基準: {0.14+0.325:.2f}')

# ---------------------------------------------------------------------------
# K. 判断: 2軸マトリクス・エントリー価格帯・確率加重・非対称性
# ---------------------------------------------------------------------------
hdr('K. 判断')
RATING = 'A'
EDGE = True   # 市場との差分あり(方向は株価に対して弱気側。報告書 2章・10章)
ADOPT = 'engine'
for nm in TGT:
    p(f'{nm}: 目標 {TGT[nm]["price"]:.1f}、乖離 {TGT[nm]["gap"]:+.1%}、判断(この経路を採用した場合) {vl.decision(RATING, TGT[nm]["gap"], EDGE)}')
DEC = vl.decision(RATING, TGT[ADOPT]['gap'], EDGE)
ALPHA = 0.20
Z = vl.zones(B=TGT[ADOPT]['price'], U=TGT['company']['price'], L=TGT['bear']['price'], alpha=ALPHA, price=PRICE, edge=EDGE)
p(f'最終判断: {DEC}(構造評価 {RATING}、採用経路 {ADOPT})')
p(f'エントリー価格帯(α={ALPHA}): Z1 {Z["Z1"]:.1f}、Z2 {Z["Z2"]:.1f}、現在 {PRICE} → {Z["zone"]}')
PROBS = {'bear': 0.25, 'consensus': 0.25, 'engine': 0.40, 'company': 0.10}
ev_ = vl.expected_value({k: TGT[k]['price'] for k in PROBS}, PROBS, PRICE)
p(f'確率 {PROBS} → 期待株価 {ev_["expected_price"]:.1f}、期待リターン {ev_["expected_return"]:+.1%}')
down = vl.gap(TGT['bear']['price'], PRICE)
up = vl.gap(TGT['company']['price'], PRICE)
p(f'非対称性(規約の目標株価): 下値 {down:+.1%}、上値 {up:+.1%}')
# 市場倍率での現実的なシナリオ(交差確認): 2027-10 時点の NTM 調整後EPS × 経路ごとの調整後PER
MKT_PER = {'bear': 30.0, 'engine': 42.0, 'consensus': 48.0, 'company': 55.0}
mk = {k: TGT[k]['ntm_adj'] * MKT_PER[k] for k in MKT_PER}
p('市場倍率シナリオ(NTM調整後EPS × 調整後PER):', {k: f'{v:.0f}({v/PRICE-1:+.0%}、PER {MKT_PER[k]:.0f})' for k, v in mk.items()})
ev_m = sum(mk[k] * PROBS[k] for k in PROBS)
p(f'  市場倍率シナリオの確率加重 {ev_m:.0f}({ev_m/PRICE-1:+.1%})、上値/下値 {(mk["company"]-PRICE)/(PRICE-mk["bear"]):.2f}')

# ---------------------------------------------------------------------------
# L. F12 感応度マトリクス(2027年の製品成長 × PEG → 12か月目標株価)、SBC 比率の軸も
# ---------------------------------------------------------------------------
hdr('L. F12')
f12 = {}
for pg27 in (-0.18, -0.06, 0.0, 0.06):
    pg = dict(PG['engine']); pg[2027] = pg27
    m = engine_model(pg, opex_g=OPEX_G['engine'], gm_p=GMP['engine'], p26=PROD26['engine'])
    em = {FY(y): m['bus'][y] for y in YEARS}
    n27 = vl.ntm_eps(em, dt.date(2027, 10, 11)); n30 = vl.ntm_eps(em, dt.date(2030, 10, 11))
    g = vl.cagr(n27, n30, 3)
    row = {peg: vl.target_price(n27, peg, g)['price'] for peg in (1.2, 1.6, 2.0, 3.0)}
    f12[pg27] = dict(ntm=n27, g=g, **row)
    p(f'製品2027 {pg27:+.0%}: NTM {n27:.2f}、g {g:.1%}、PEG1.2 {row[1.2]:.0f} / 1.6 {row[1.6]:.0f} / 2.0 {row[2.0]:.0f} / 3.0 {row[3.0]:.0f}')
# PEG がいくつなら株価を正当化するか(エンジン・コンセンサス)
for nm in ('engine', 'consensus', 'company'):
    peg_needed = PRICE / TGT[nm]['ntm'] / (TGT[nm]['g'] * 100)
    p(f'株価 194.75 を 2027-10 の NTM で正当化する PEG({nm}): {peg_needed:.2f}')
for sr in (0.035, 0.039, 0.045):
    bus = {FY(y): CONS_ADJ[y] - sr * CONS_REV[y] * (1 - TAX) / shares[y] for y in YEARS}
    n27 = vl.ntm_eps(bus, dt.date(2027, 10, 11)); n30 = vl.ntm_eps(bus, dt.date(2030, 10, 11))
    p(f'SBC/売上 {sr:.1%}(コンセンサス): NTM {n27:.3f}、g {vl.cagr(n27, n30, 3):.1%}、目標(PEG1.6) {vl.target_price(n27, 1.6, vl.cagr(n27, n30, 3))["price"]:.1f}')

# ---------------------------------------------------------------------------
# M. 出力(報告書・summary.json 用)
# ---------------------------------------------------------------------------
out = dict(price=PRICE, mcap=MCAP, ev=EV, net_cash=NET_CASH, k1=k1, k2=k2, c=c, recon=recon, trend_growth=math.exp(b) - 1,
           paths={nm: {'adj': {y: PATHS[nm]['adj'][y] for y in range(2026, 2032)}, 'bus': {y: PATHS[nm]['bus'][y] for y in range(2026, 2032)},
                       'rev': {y: PATHS[nm]['rev'][y] for y in range(2026, 2032)}, 'sbc_ratio': {y: PATHS[nm]['sbc'][y] / PATHS[nm]['rev'][y] for y in range(2026, 2032)}}
                  for nm in PATHS},
           engine_detail={k: {y: M['engine'][k][y] for y in range(2026, 2032)} for k in ('P', 'Sr', 'Sb', 'DR', 'rev', 'om', 'bill')},
           bear_detail={k: {y: M['bear'][k][y] for y in range(2026, 2032)} for k in ('P', 'Sr', 'rev', 'om')},
           company_detail={k: {y: M['company'][k][y] for y in range(2026, 2032)} for k in ('P', 'Sr', 'rev', 'om')},
           targets=TGT, sst=SST, dcf=DCF, rdcf=RDCF, implied=dict(prod_long=imp_prod, k1=imp_k1, opex=imp_opex),
           sens=[(s[0], s[1], s[2]) for s in sens], ss=dict(earn=ss_earn, value=split['steady_state_value'], growth=split['growth_price'],
                                                           share=split['growth_share_of_mcap'], rev_norm=rev_norm26, prod_norm=prod_norm26),
           within3=within3, mult=mult, g5=dict(consensus=g5_cons, company=g5_comp, engine=g5_eng, bear=g5_bear),
           decision=DEC, zones=Z, probs=PROBS, ev=ev_, down=down, up=up, mkt=mk, ev_mkt=ev_m, f12=f12, rule40=rule40,
           cagr_adj_cons=cagr3_adj_cons, nopat=(nopat24, nopat26))
with open(OUT + 'FTNT_calc_out.json', 'w') as f:
    json.dump(out, f, ensure_ascii=False, indent=1, default=lambda o: str(o))
p('\n書き出し: FTNT_F13.csv, FTNT_F18.csv, FTNT_F10.csv, FTNT_calc_out.json')
