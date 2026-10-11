"""Zscaler (ZS) 計算スクリプト(Opus 分析者)。

規約: 00_standard.md §3・§3-1・§3-2・§4、valuation-model.md、scenario-strategy.md §6。
評価基準日 2026-10-11、株価は 2026-10-09 終値。金額は百万ドル、EPS はドル。
出力: 標準出力(報告書に転記する表)、analysis/ZS_F13.csv、ZS_F18.csv、ZS_F10.csv、ZS_F12.csv、ZS_summary.json
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import math
import os
import sys

sys.path.insert(0, '/home/user/AI/reports/security-stocks-2026-10/build')
import valuation_lib as vl  # noqa: E402

OUT = '/home/user/AI/reports/security-stocks-2026-10/analysis'

# ---------------------------------------------------------------------------
# 0. 入力(出所は報告書 Appendix B・F。取得日 2026-10-11)
# ---------------------------------------------------------------------------
PRICE = 233.73                 # 2026-10-09 終値(Yahoo・StockAnalysis 一致、peer_peg_table)
SH_NOW = 170.0                 # 現在の希薄化後株数(Q1 FY27 ガイダンスの non-GAAP 希薄化後 約170百万株)
SH_Q4_26 = 198.2 / 1.19        # Q4 FY26 実績の non-GAAP 希薄化後株数(非GAAP純利益÷EPS)= 166.6
SH_FY25 = 534.8 / 3.28         # 163.0
SH_FY26 = 704.2 / 4.21         # 167.3
SH_FY27 = 173.0                # FY27 ガイダンスの前提株数
TAX = 0.21                     # 会社の non-GAAP 税率(FY27 ガイダンス 21%)
CASH = 3474.2                  # 現金・短期投資(2026-07-31)
CONVERT = 1725.0               # 0% 転換社債 額面(満期 2028-07-15)
NET_CASH = CASH - CONVERT      # 1,749.2
MCAP = PRICE * SH_NOW / 1000   # 十億ドル
EV = MCAP - NET_CASH / 1000

# 実績(FY = 7月末)
REV = {2024: 2167.8, 2025: 2673.1, 2026: 3352.6}
SBC = {2025: 661.35, 2026: 821.9}          # 株式報酬+関連給与税(Q4 FY26 リリースの GAAP 調整表、Tier 1)
SBC_ALT = {2025: 685.5, 2026: 841.6}       # Haiku の四半期調整表の合計(差 約20〜24、未解決。感応度で扱う)
NG_NI = {2025: 534.8, 2026: 704.2}         # non-GAAP 純利益
NG_EPS = {2025: 3.28, 2026: 4.21}
NG_OPI = {2025: 580.1, 2026: 767.1}
GAAP_NI = {2025: -41.5, 2026: -63.2}
OCF = {2025: 972.5, 2026: 1129.7}
FCF = {2025: 726.7, 2026: 779.1}
CAPEX = {2025: 245.8, 2026: 350.6}
DEF_REV = {2025: 2468.0, 2026: 2925.8}

# 四半期 KPI(ARR は Red Canary を除く有機。d=逆算値)
Q = ['FY24Q4', 'FY25Q1', 'FY25Q2', 'FY25Q3', 'FY25Q4', 'FY26Q1', 'FY26Q2', 'FY26Q3', 'FY26Q4']
ARR_TOTAL = {'FY24Q4': 2471, 'FY25Q1': 2553, 'FY25Q2': 2685, 'FY25Q3': 2817, 'FY25Q4': 3015,
             'FY26Q1': 3204, 'FY26Q2': 3359, 'FY26Q3': 3525, 'FY26Q4': 3771}
RC = {'FY26Q1': 98, 'FY26Q2': 114, 'FY26Q3': 127, 'FY26Q4': 141}
ARR_ORG = {q: ARR_TOTAL[q] - RC.get(q, 0) for q in Q}
REVQ = {'FY24Q4': 592.9, 'FY25Q1': 628.0, 'FY25Q2': 647.9, 'FY25Q3': 678.0, 'FY25Q4': 719.2,
        'FY26Q1': 788.1, 'FY26Q2': 815.8, 'FY26Q3': 850.5, 'FY26Q4': 898.2}
SBCQ = {'FY25Q1': 160.6, 'FY25Q2': 176.3, 'FY25Q3': 167.8, 'FY25Q4': 180.8,
        'FY26Q1': 193.8, 'FY26Q2': 220.3, 'FY26Q3': 212.3, 'FY26Q4': 215.2}
FCFQ = {'FY24Q4': 136.3, 'FY25Q1': 291.9, 'FY25Q2': 143.4, 'FY25Q3': 119.5, 'FY25Q4': 171.9,
        'FY26Q1': 413.3, 'FY26Q2': 169.1, 'FY26Q3': 136.0, 'FY26Q4': 60.8}
NGOPQ = {'FY24Q4': 127.5, 'FY25Q1': 134.1, 'FY25Q2': 140.5, 'FY25Q3': 146.7, 'FY25Q4': None,
         'FY26Q1': 171.9, 'FY26Q2': 181.0, 'FY26Q3': 195.8, 'FY26Q4': 218.4}
NGOPQ['FY25Q4'] = NG_OPI[2025] - (134.1 + 140.5 + 146.7)   # 逆算 158.8

# Red Canary の四半期売上(推定: 期首期末平均ARR × 0.98 ÷ 4。取得時 ARR は投資家資料の 83)
RC_OPEN = 83.0
RC_REVQ = {}
_prev = RC_OPEN
for _q in ('FY26Q1', 'FY26Q2', 'FY26Q3', 'FY26Q4'):
    RC_REVQ[_q] = 0.98 * (_prev + RC[_q]) / 2 / 4
    _prev = RC[_q]

# ---------------------------------------------------------------------------
# 1. 事業実態EPS(基準EPS)と EPS 対数分解
# ---------------------------------------------------------------------------
def biz_ni(adj_ni, sbc, tax=None):
    t = TAX if tax is None else tax
    return adj_ni - sbc * (1 - t)


BEPS_FY26 = biz_ni(NG_NI[2026], SBC[2026]) / SH_NOW
BEPS_FY25 = biz_ni(NG_NI[2025], SBC[2025]) / SH_NOW
BEPS_FY26_ALT = biz_ni(NG_NI[2026], SBC_ALT[2026]) / SH_NOW
logdec = vl.eps_log_decomposition(REV[2025], REV[2026], NG_NI[2025] / REV[2025], NG_NI[2026] / REV[2026], SH_FY25, SH_FY26)
opm25, opm26 = NG_OPI[2025] / REV[2025], NG_OPI[2026] / REV[2026]
# 純利益率の内訳: 営業利益率の寄与と、その他(受取利息・税)の寄与
LOG_OPM = math.log(opm26 / opm25)
LOG_OTHER = logdec['margin'] - LOG_OPM

# ---------------------------------------------------------------------------
# 2. 経路モデル(年度 FY27〜FY34。FY31 = FY+5、FY34 = FY+8)
# ---------------------------------------------------------------------------
YEARS = list(range(2027, 2035))
K27, K = 0.959, 0.962          # 売上 ÷ 期首期末平均ARR(FY27 ガイダンス 0.959、FY26 実績 0.974)
ARR26 = 3771.0
NNARR26_ORG = 615 + (141 - 98)  # 有機の純新規ARR(Red Canary 除く 615 + 取得後の Red Canary の純増 43)= 658
INT_FY27, INT_FY28 = 140.7, 140.0   # 受取利息(FY27 ガイダンス・FY28 コンセンサスから逆算)
YIELD = 0.035                  # FY29 以降: (純現金 + 事業実態純利益の累計)× 3.5%(転換社債は 2028-07 に現金償還と仮定)


def fy_end(y):
    return dt.date(y, 7, 31)


def run_path(name, arr27, nn_growth, opm, sbc_ratio, rev_override=None, adj_eps_override=None,
             exit_peg=1.5, fade_to=2038, refi=False):
    """年度別の ARR・売上・調整後純利益・SBC・事業実態EPS を返す。"""
    arr = {2026: ARR26, 2027: arr27}
    nn = {2027: arr27 - ARR26}
    rows = {}
    cum_biz = 0.0
    for y in YEARS:
        if y > 2027:
            if rev_override and y in rev_override and 'arr' in rev_override[y]:
                arr[y] = rev_override[y]['arr']
                nn[y] = arr[y] - arr[y - 1]
            else:
                nn[y] = nn[y - 1] * (1 + nn_growth[y])
                arr[y] = arr[y - 1] + nn[y]
        k = K27 if y == 2027 else K
        rev = k * (arr[y - 1] + arr[y]) / 2
        if rev_override and y in rev_override and 'rev' in rev_override[y]:
            rev = rev_override[y]['rev']
        interest = INT_FY27 if y == 2027 else INT_FY28 if y == 2028 else YIELD * (NET_CASH + cum_biz)
        if refi and y >= 2029:
            interest += 60.0
        shares = SH_FY27 * (1.03 ** (y - 2027))
        if adj_eps_override and y in adj_eps_override:
            adj_ni = adj_eps_override[y] * shares
            op_m = (adj_ni / (1 - TAX) - interest) / rev
        else:
            op_m = opm[y]
            adj_ni = (rev * op_m + interest) * (1 - TAX)
        sbc = rev * sbc_ratio[y]
        bni = biz_ni(adj_ni, sbc)
        cum_biz += bni
        rows[y] = dict(arr=arr[y], nnarr=nn[y], rev=rev, opm=op_m, interest=interest, adj_ni=adj_ni,
                       shares=shares, adj_eps=adj_ni / shares, sbc_ratio=sbc_ratio[y], sbc=sbc,
                       biz_ni=bni, biz_eps=bni / SH_NOW, owner_margin=op_m - sbc_ratio[y])
    return dict(name=name, rows=rows, exit_peg=exit_peg, fade_to=fade_to)


def lin(start, step, y0=2027):
    return {y: start + step * (y - y0) for y in YEARS}


def grow(seq):
    return {y: g for y, g in zip(range(2028, 2035), seq)}


# SBC/売上(FY25 24.7% → FY26 24.5%、実績の低下は年 −0.2pt)
SBC_BASE = lin(0.235, -0.010)      # 年 −1.0pt(実績より速い。FY27 の人員3%削減と成長減速による付与の伸びの鈍化)
SBC_FAST = lin(0.230, -0.015)      # 会社シナリオ: 年 −1.5pt
SBC_STICKY = lin(0.240, -0.005)    # 弱気の変形: 年 −0.5pt(株価下落局面のリテンション付与で高止まり)
SBC_PIVOT = lin(0.225, -0.020)     # 弱気の変形: Okta 型の利益転換(年 −2pt)

NN_ENGINE = [0.09, 0.06, 0.04, 0.03, 0.02, 0.02, 0.02]
NN_COMPANY = [0.15, 0.15, 0.15, 0.15, 0.10, 0.10, 0.10]
NN_BEAR = [-0.05, -0.05, -0.05, -0.05, -0.03, -0.03, -0.03]
CONS_OVR = {2027: {'rev': 3930.0}, 2028: {'rev': 4580.0, 'arr': 2 * 4580.0 / K - 4411}}
CONS_EPS = {2027: 4.91, 2028: 5.60}


def consensus_path(**kw):
    tmp = run_path('tmp', 4411, grow([None, 0.05, 0.05, 0.05, 0.03, 0.03, 0.03]), lin(0.24, 0.0), SBC_BASE,
                   rev_override=CONS_OVR, adj_eps_override=CONS_EPS)
    c28 = tmp['rows'][2028]['opm']
    return run_path('コンセンサス経路', 4411, grow([None, 0.05, 0.05, 0.05, 0.03, 0.03, 0.03]),
                    {y: c28 + 0.0075 * (y - 2028) for y in YEARS}, SBC_BASE,
                    rev_override=CONS_OVR, adj_eps_override=CONS_EPS, exit_peg=1.5, fade_to=2038, **kw)


PATHS = {
    'consensus': consensus_path(),
    'company': run_path('会社シナリオ経路', 4411, grow(NN_COMPANY), lin(0.2365, 0.015), SBC_FAST, exit_peg=1.8, fade_to=2042),
    'engine': run_path('事業エンジン経路', 4460, grow(NN_ENGINE), lin(0.237, 0.010), SBC_BASE, exit_peg=1.5, fade_to=2038),
    'bear': run_path('弱気パス', 4396, grow(NN_BEAR), lin(0.235, 0.010), SBC_BASE, exit_peg=1.0, fade_to=2034),
}
VARIANTS = {
    'bear_sticky': run_path('弱気(SBC高止まり・利益率停滞)', 4396, grow(NN_BEAR), lin(0.235, 0.005), SBC_STICKY, exit_peg=1.0, fade_to=2034),
    'bear_pivot': run_path('弱気(Okta型の利益転換)', 4396, grow(NN_BEAR), lin(0.235, 0.020), SBC_PIVOT, exit_peg=1.0, fade_to=2034),
    'company_10b': run_path('会社の上振れ(FY31 ARR 100億ドル)', 4411, grow([0.33, 0.33, 0.33, 0.33, 0.12, 0.12, 0.12]), lin(0.2365, 0.015), SBC_FAST, exit_peg=1.8, fade_to=2042),
}

# 年度別PEGレンジ(9章で導出。採用 1.1〜1.4 を年度別に配分)
PEG_BY_YEAR = {2027: (1.0, 1.2), 2028: (1.1, 1.3), 2029: (1.1, 1.4), 2030: (1.2, 1.4), 2031: (1.2, 1.5)}
PEG_ADOPT = (1.1, 1.4)


def g3(path, y):
    r = path['rows']
    a, b = r[y]['biz_eps'], r[y + 3]['biz_eps']
    return vl.cagr(a, b, 3) if a > 0 and b > 0 else float('nan')


def dcf_value(path, at=vl.TARGET_DATE, g_term=0.04, r=vl.COST_OF_CAPITAL):
    """交差確認: 事業実態純利益の DCF。FY34 の伸びから、競争優位期間の終わり(fade_to)にかけて g_term へ線形に減衰。"""
    rows = path['rows']
    fade_to = path['fade_to']
    cf = {y: rows[y]['biz_ni'] for y in YEARS}
    g34 = rows[2034]['biz_ni'] / rows[2033]['biz_ni'] - 1
    last = cf[2034]
    end = max(fade_to, 2035)
    n = end - 2034
    for i, y in enumerate(range(2035, end + 1)):
        gy = g34 + (g_term - g34) * (i + 1) / n if fade_to > 2034 else g_term
        last *= 1 + gy
        cf[y] = last
    tv = cf[end] * (1 + g_term) / (r - g_term)
    pv = 0.0
    for y, v in cf.items():
        t = (fy_end(y) - at).days / 365.25
        if t <= 0:
            continue
        pv += v / (1 + r) ** t
    pv += tv / (1 + r) ** ((fy_end(end) - at).days / 365.25)
    return pv / SH_NOW


def targets(path):
    r = path['rows']
    eps = {fy_end(y): r[y]['biz_eps'] for y in YEARS}
    ntm = vl.ntm_eps(eps)                                # 2027-10-11 時点の NTM
    g = vl.cagr(r[2028]['biz_eps'], r[2031]['biz_eps'], 3)
    g_exit = vl.cagr(r[2031]['biz_eps'], r[2034]['biz_eps'], 3)
    ss = vl.steady_state_target(r[2031]['biz_eps'], fy_end(2031), path['exit_peg'], g_exit)
    return dict(ntm=ntm, g=g,
                conv_low=vl.target_price(ntm, PEG_ADOPT[0], g)['price'],
                conv_high=vl.target_price(ntm, PEG_ADOPT[1], g)['price'],
                conv_mid=vl.target_price(ntm, sum(PEG_ADOPT) / 2, g)['price'],
                conv_mid_uncapped=vl.target_price(ntm, sum(PEG_ADOPT) / 2, g)['price_uncapped'],
                g_exit=g_exit, ss=ss, ss_target=ss['target'], dcf=dcf_value(path))


RES = {k: targets(p) for k, p in PATHS.items()}
RES_V = {k: targets(p) for k, p in VARIANTS.items()}

# ---------------------------------------------------------------------------
# 3. 定常状態利益と成長の値段(FY26 実績ベース。SBC を含む全費用で計算)
# ---------------------------------------------------------------------------
GM_NG = 2691.6 / REV[2026]          # non-GAAP 粗利率 80.3%
SBC_COGS = 87.5 / REV[2026]         # 売上原価の SBC 2.6%(10-K の粗利調整)
# non-GAAP 営業費用の内訳(推定: FY25 GAAP 内訳 S&M 47.1%・R&D 25.1%・G&A 9.4% から SBC・償却の推定額を除き FY26 に適用)
OPEX_NG = {'S&M': 0.355, 'R&D': 0.160, 'G&A': 0.059}
SBC_OPEX = {'S&M': 0.097, 'R&D': 0.093, 'G&A': 0.029}   # 計 21.9%(+売上原価 2.6% = 24.5%)
MAINT = {'S&M': 0.35, 'R&D': 0.55, 'G&A': 1.00}       # 成長投資を止めても残る比率(推定)


def steady_state(maint=MAINT, rev=REV[2026]):
    cogs_all = (1 - GM_NG) + SBC_COGS
    opex_all = sum((OPEX_NG[k] + SBC_OPEX[k]) * maint[k] for k in OPEX_NG)
    margin = 1 - cogs_all - opex_all
    pretax = rev * margin + NET_CASH * YIELD
    return dict(margin=margin, earnings=pretax * (1 - TAX))


SS = {'base': steady_state(), 'low': steady_state({'S&M': 0.45, 'R&D': 0.65, 'G&A': 1.0}),
      'high': steady_state({'S&M': 0.25, 'R&D': 0.45, 'G&A': 0.9})}
SPLIT = {k: vl.steady_state_split(v['earnings'] / 1000, MCAP) for k, v in SS.items()}

# 増分の経済性(1ドルの純新規ARRの獲得費用と生涯価値。推定)
growth_cost = sum((OPEX_NG[k] + SBC_OPEX[k]) * (1 - MAINT[k]) for k in OPEX_NG) * REV[2026]
CAC_PER_ARR = growth_cost / NNARR26_ORG
LTV = {gc: SS['base']['margin'] * (1 - TAX) / (vl.COST_OF_CAPITAL + gc - 0.03) for gc in (0.02, 0.04)}
INCR_ROIC = SS['base']['margin'] * (1 - TAX) / CAC_PER_ARR


def time_split(path):
    """価値の時間分布: 事業実態純利益の現在価値のうち FY27〜FY29(3年以内)の比率。"""
    rows = path['rows']
    pv3 = sum(rows[y]['biz_ni'] / (1.09 ** ((fy_end(y) - vl.VALUATION_DATE).days / 365.25)) for y in (2027, 2028, 2029))
    total = dcf_value(path, at=vl.VALUATION_DATE) * SH_NOW
    return pv3 / total, 1 - pv3 / total, total


TS = time_split(PATHS['engine'])

# ---------------------------------------------------------------------------
# 4. 価値感度分析(事業エンジン経路。定常状態経由の目標株価と DCF の両方で測る)
# ---------------------------------------------------------------------------
def engine_variant(nn=None, sbc_shift=0.0, opm_shift=0.0, peg=1.5, tax=None, refi=False, fade_to=2038, sbc_level=0.0):
    global TAX
    old = TAX
    if tax is not None:
        TAX = tax
    nn = nn or NN_ENGINE
    sbc = {y: SBC_BASE[y] + sbc_level + sbc_shift * (y - 2026) / 5 for y in YEARS}
    opm = {y: 0.237 + 0.010 * (y - 2027) + opm_shift * (y - 2026) / 5 for y in YEARS}
    p = run_path('v', 4460, grow(nn), opm, sbc, exit_peg=peg, fade_to=fade_to, refi=refi)
    t = targets(p)
    TAX = old
    return t['ss_target'], t['dcf']


BASE_T, BASE_D = engine_variant()
SENS_DEF = [
    ('SBC/売上の低下速度(FY31 時点 ±3pt)', dict(sbc_shift=+0.03), dict(sbc_shift=-0.03)),
    ('調整後営業利益率の拡大(FY31 時点 ±3pt)', dict(opm_shift=-0.03), dict(opm_shift=+0.03)),
    ('競争優位期間(出口PEG ±0.3/DCF の減衰終了 ±4年)', dict(peg=1.2, fade_to=2034), dict(peg=1.8, fade_to=2042)),
    ('有機の純新規ARRの伸び(FY28〜34、年 ±5pt)', dict(nn=[x - 0.05 for x in NN_ENGINE]), dict(nn=[x + 0.05 for x in NN_ENGINE])),
    ('税率(±2pt)', dict(tax=0.23), dict(tax=0.19)),
    ('SBC の基準値(821.9 か 841.6 か: +0.6pt)', dict(sbc_level=+0.006), dict()),
    ('転換社債の借り換え(受取利息の残存)', dict(), dict(refi=True)),
]
SENS = []
for name, lo, hi in SENS_DEF:
    a, b = engine_variant(**lo), engine_variant(**hi)
    SENS.append((name, a[0], b[0], a[1], b[1]))
SENS.sort(key=lambda s: -abs(s[2] - s[1]))

# F12: SBC/売上(FY31)× 調整後営業利益率(FY31)の感応度マトリクス(事業エンジン経路、定常状態経由)
F12_SBC = [+0.03, 0.0, -0.03, -0.06]
F12_OPM = [-0.03, 0.0, +0.03, +0.06]
F12 = [[engine_variant(sbc_shift=s, opm_shift=o)[0] for o in F12_OPM] for s in F12_SBC]


def solve(fn, target=PRICE, lo=-0.20, hi=0.40):
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if fn(mid) < target else (lo, mid)
    return mid


r31 = PATHS['engine']['rows'][2031]
REQ_CUT_SS = solve(lambda x: engine_variant(sbc_shift=-x)[0])
REQ_CUT_DCF = solve(lambda x: engine_variant(sbc_shift=-x)[1])
REQ_OWNER_SS = r31['owner_margin'] + REQ_CUT_SS
REQ_OWNER_DCF = r31['owner_margin'] + REQ_CUT_DCF
# 逆算: 会社の SBC・利益率の経路のまま、株価を正当化する NNARR の伸び(定常状態経由)
REQ_NN = solve(lambda x: targets(run_path('v', 4411, grow([x] * 4 + [0.10] * 3), lin(0.2365, 0.015), SBC_FAST, exit_peg=1.8))['ss_target'], lo=-0.1, hi=0.8)

# ---------------------------------------------------------------------------
# 5. 判断(構造評価・PEG・2軸・エントリー・期待値)
# ---------------------------------------------------------------------------
RATINGS = {'1': 'C', '2': 'B', '3': 'B', '4': 'S', '5': 'B', '6': 'D', '7': 'C', '8': 'B', '9': 'C',
           '10': 'B', '11': 'C', '12': 'B', '13': 'B'}
STRUCT = 'B'
EDGE = True   # 差分あり(方向は下: 市場は SBC 控除前の FCF・調整後EPS で評価している)
ADOPTED = 'engine'
T12 = {k: RES[k]['ss_target'] for k in RES}
T12_DCF = {k: RES[k]['dcf'] for k in RES}
T12_CONV = {k: RES[k]['conv_mid'] for k in RES}
PROB = {'bear': 0.20, 'consensus': 0.30, 'engine': 0.35, 'company': 0.15}
EVAL = vl.expected_value(T12, PROB, PRICE)
EVAL_DCF = vl.expected_value(T12_DCF, PROB, PRICE)
GAPS = {k: vl.gap(T12[k], PRICE) for k in ('consensus', 'company', 'engine')}
GAPS_DCF = {k: vl.gap(T12_DCF[k], PRICE) for k in ('consensus', 'company', 'engine', 'bear')}
DEC = vl.decision(STRUCT, GAPS[ADOPTED], EDGE)
DEC_DCF = vl.decision(STRUCT, GAPS_DCF[ADOPTED], EDGE)
ALPHA = 0.25
ZONES = vl.zones(B=T12['engine'], U=T12['company'], L=T12['bear'], alpha=ALPHA, price=PRICE, edge=EDGE)
ZONES_DCF = vl.zones(B=T12_DCF['engine'], U=T12_DCF['company'], L=T12_DCF['bear'], alpha=ALPHA, price=PRICE, edge=EDGE)
DOWN = (T12['bear'] - PRICE) / PRICE
UP = (T12['company'] - PRICE) / PRICE

# 現在の倍率
NTM_ADJ_NOW = vl.ntm_eps({fy_end(2027): 4.91, fy_end(2028): 5.60}, start=dt.date(2026, 10, 11))
NTM_BIZ_NOW = vl.ntm_eps({fy_end(y): PATHS['consensus']['rows'][y]['biz_eps'] for y in (2027, 2028)}, start=dt.date(2026, 10, 11))
NTM_REV = 3930 * 10 / 12 + 4580 * 2 / 12
NTM_FCF = NTM_REV * 0.2325
ADJ_CAGR_2Y = vl.cagr(4.21, 5.60, 2)
BIZ_CAGR_3Y_C = vl.cagr(PATHS['consensus']['rows'][2027]['biz_eps'], PATHS['consensus']['rows'][2030]['biz_eps'], 3)
BIZ_CAGR_5Y_E = vl.cagr(BEPS_FY26, PATHS['engine']['rows'][2031]['biz_eps'], 5)
BIZ_CAGR_5Y_C = vl.cagr(BEPS_FY26, PATHS['consensus']['rows'][2031]['biz_eps'], 5)
PER_BIZ_NTM = PRICE / NTM_BIZ_NOW
PEG_BIZ_3Y = PER_BIZ_NTM / (min(BIZ_CAGR_3Y_C, 0.5) * 100)
PEG_ADJ = PRICE / NTM_ADJ_NOW / (ADJ_CAGR_2Y * 100)
EV_SALES = EV * 1000 / NTM_REV
EV_FCF = EV * 1000 / NTM_FCF
FCF_M_TTM = FCF[2026] / REV[2026]
SBC_R_TTM = SBC[2026] / REV[2026]
ORG_REV_YOY_Q4 = (REVQ['FY26Q4'] - RC_REVQ['FY26Q4']) / REVQ['FY25Q4'] - 1
ORG_REV_YOY_FY = (REV[2026] - sum(RC_REVQ.values())) / REV[2025] - 1
# 市場が置く価格(目標株価の中央値と、株価下落時点)
MAY_LOW = 126.41
EV_SALES_MAY = (MAY_LOW * 168.0 / 1000 - NET_CASH / 1000) * 1000 / (3899 * 10 / 12 + 4500 * 2 / 12)


# ---------------------------------------------------------------------------
# 6. 出力
# ---------------------------------------------------------------------------
def write_csvs():
    # F13 年度別適正株価パス
    with open(os.path.join(OUT, 'ZS_F13.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['fy_end', 'path', 'business_eps', 'g_3y', 'peg_low', 'peg_high', 'fair_per_low', 'fair_per_high',
                    'fair_price_low', 'fair_price_high', 'is_extension'])
        for k, p in PATHS.items():
            for y in range(2027, 2032):
                e = p['rows'][y]['biz_eps']
                g = g3(p, y)
                lo, hi = PEG_BY_YEAR[y]
                pl, ph = vl.fair_per(lo, g)['capped'], vl.fair_per(hi, g)['capped']
                ext = y >= 2029   # コンセンサスの最終年度(FY28)より先は延長部分
                w.writerow([fy_end(y).isoformat(), k, round(e, 3), round(g, 4), lo, hi, round(pl, 1), round(ph, 1),
                            round(pl * e, 1), round(ph * e, 1), ext])
    # F18 根幹KPI加速度
    rows = []
    prev_yoy = None
    for i, q in enumerate(Q):
        v = ARR_ORG[q]
        qa = (v / ARR_ORG[Q[i - 1]]) ** 4 - 1 if i > 0 else None
        yoy = v / ARR_ORG[Q[i - 4]] - 1 if i >= 4 else None
        sd = (yoy - prev_yoy) * 100 if (yoy is not None and prev_yoy is not None) else None
        rows.append(['有機ARR(Red Canary除く、百万ドル)', q, v, qa, yoy, sd])
        if yoy is not None:
            prev_yoy = yoy
    nn = {Q[i]: ARR_ORG[Q[i]] - ARR_ORG[Q[i - 1]] for i in range(1, len(Q))}
    nn['FY25Q4'] = 198.0  # 会社開示(232 ÷ 1.17)
    nn['FY25Q3'] = ARR_ORG['FY25Q3'] - ARR_ORG['FY25Q2']
    prev = None
    for q in Q[1:]:
        yoy = nn[q] / nn[Q[Q.index(q) - 4]] - 1 if Q.index(q) >= 5 else None
        sd = (yoy - prev) * 100 if (yoy is not None and prev is not None) else None
        rows.append(['有機の純新規ARR(百万ドル、四半期)', q, round(nn[q], 1), None, yoy, sd])
        if yoy is not None:
            prev = yoy
    prev = None
    for i, q in enumerate(Q):
        if i < 4:
            continue
        org = REVQ[q] - RC_REVQ.get(q, 0)
        yoy = org / REVQ[Q[i - 4]] - 1
        sd = (yoy - prev) * 100 if prev is not None else None
        rows.append(['有機売上成長率(前年同期比)', q, round(org, 1), None, yoy, sd])
        prev = yoy
    prev = None
    for q in Q:
        if q in SBCQ:
            r = SBCQ[q] / REVQ[q]
            sd = (r - prev) * 100 if prev is not None else None
            rows.append(['SBC/売上(四半期、Haiku の調整表値)', q, round(r, 4), None, None, sd])
            prev = r
    prev = None
    for q in Q:
        r = NGOPQ[q] / REVQ[q]
        sd = (r - prev) * 100 if prev is not None else None
        rows.append(['調整後営業利益率', q, round(r, 4), None, None, sd])
        prev = r
    prev = None
    for i, q in enumerate(Q):
        if i < 3:
            continue
        ttm = sum(FCFQ[Q[j]] for j in range(i - 3, i + 1)) / sum(REVQ[Q[j]] for j in range(i - 3, i + 1))
        sd = (ttm - prev) * 100 if prev is not None else None
        rows.append(['FCFマージン(TTM)', q, round(ttm, 4), None, None, sd])
        prev = ttm
    for q, v in (('FY25Q1', 1.14), ('FY25Q3', 1.14), ('FY26Q1', 1.15), ('FY26Q2', 1.15), ('FY26Q3', 1.15), ('FY26Q4', 1.15)):
        rows.append(['NRR(既存顧客の売上継続率、TTM)', q, v, None, None, None])
    with open(os.path.join(OUT, 'ZS_F18.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['kpi', 'period', 'value', 'qoq_annualized', 'ttm_yoy', 'second_diff'])
        for r in rows:
            w.writerow([r[0], r[1], r[2]] + [('' if x is None else round(x, 4)) for x in r[3:]])
    # F10 収益ミックスの時系列(四半期、百万ドル)
    with open(os.path.join(OUT, 'ZS_F10.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['period', 'line', 'revenue_usd_mn'])
        for q in Q:
            rc = RC_REVQ.get(q, 0.0)
            w.writerow([q, 'Zero Trust Exchange 有機(ユーザー課金+成長エンジン)', round(REVQ[q] - rc, 1)])
            w.writerow([q, 'Red Canary(MDR・SecOps、ARRから推定)', round(rc, 1)])
    # F12
    with open(os.path.join(OUT, 'ZS_F12.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['sbc_ratio_fy31', 'opm_fy31', 'owner_margin_fy31', 'target_usd'])
        for i, s in enumerate(F12_SBC):
            for j, o in enumerate(F12_OPM):
                sr, om = r31['sbc_ratio'] + s, r31['opm'] + o
                w.writerow([round(sr, 3), round(om, 3), round(om - sr, 3), round(F12[i][j], 1)])
    return rows


def write_summary():
    e, c = PATHS['engine']['rows'], PATHS['consensus']['rows']
    s = {
        'ticker': 'ZS', 'company': 'Zscaler, Inc.', 'price': PRICE, 'price_date': '2026-10-09',
        'market_cap_usd_bn': round(MCAP, 2), 'diluted_shares_mn': SH_NOW, 'fy_end_month': 7,
        'net_cash_usd_bn': round(NET_CASH / 1000, 3),
        'structure_rating': STRUCT, 'condition_ratings': RATINGS, 'condition9_applicable': True,
        'rules_fired': ['C評価4条件(1・7・9・11)→総合はB以上にしない(発動)', '致命条件の拒否権(E以下なし、非発動)',
                        '条件6-7の対評価(6=D・7=C: 安さの見かけは SBC 除外による)', '条件9は適用(AIトラフィックの制御・Security for AI)'],
        'archetype': 'ORCL型寄り(継続課金のインライン基盤)だが席課金とSBC依存。MU/VRT/AVGO型ではない',
        'business_model_types': ['A(ユーザー席課金の Zero Trust Exchange)', 'B(Z-Flex・非席の従量課金: 新規ACVの約30%)', 'A+MDR(Red Canary)'],
        'core_variables': [
            {'name': 'SBC控除後営業利益率(調整後営業利益率−SBC/売上)の FY31 水準',
             'market_implied': f'約{REQ_OWNER_SS*100:.0f}%(定常状態経由)/約{REQ_OWNER_DCF*100:.0f}%(DCF)',
             'our_estimate': f'{r31["owner_margin"]*100:.1f}%(FY26 実績 {(opm26-SBC_R_TTM)*100:.1f}%)',
             'advantage_type': '分析(会計による歪み: SBC を費用として扱う)'},
            {'name': '競争優位期間(CAP)', 'market_implied': '15年超(出口PEG 2.0 超に相当)', 'our_estimate': '10〜12年',
             'advantage_type': '分析(増分シェアの低下: PANW SASE +35〜40%、Netskope +27%、ZS 有機 +20%)'},
            {'name': '有機の純新規ARRの伸び', 'market_implied': 'FY28 +9%(コンセンサス売上の逆算)',
             'our_estimate': 'FY27 +5%、FY28 +9%、その後 +2〜6%', 'advantage_type': 'エッジなし(感度が低い)'}],
        'edge': {'exists': True,
                 'statement': '市場は調整後EPS(PER 47倍)とSBC控除前のFCF(EV/FCF 40倍)で評価し、ガイダンスの保守性とAI需要を上振れ要因と見ている。SBCを費用とみなすとオーナー利益はほぼゼロで、株価はFY31にSBC控除後営業利益率 約20%(現在 −1%)を要求する。SBC/売上は過去2年で年 −0.2pt しか下がっておらず、株価は過大。',
                 'advantage_type': '分析(会計による歪み)', 'kpi': 'SBC/売上(通期)と SBC控除後営業利益率',
                 'threshold': 'FY27 で SBC/売上 ≤22%(差分の否定側)/ ≥24%(差分の確認側)', 'timing': 'FY27 Q2〜Q4 決算(2027年2〜9月)',
                 'value_per_share_if_resolved': round(T12['engine'], 1)},
        'eps_definition': '事業実態EPS = (調整後純利益 − SBC(関連給与税込み)×(1−21%))÷ 現在の希薄化後株数 170百万株。買収無形資産償却は除外したまま',
        'base_business_eps': {'fy': 'FY2026', 'value': round(BEPS_FY26, 3)},
        'eps_paths': {k: {f'FY{y}': round(p['rows'][y]['biz_eps'], 3) for y in YEARS} for k, p in PATHS.items()},
        'adj_eps_consensus': {'FY2027': 4.91, 'FY2028': 5.60},
        'sbc_to_revenue_path': {f'FY{y}': round(SBC_BASE[y], 3) for y in YEARS},
        'allowed_peg': {'path_a': [3.39, 9.90], 'path_b': [1.0, 1.5], 'path_c': [1.1, 1.4], 'adopted': list(PEG_ADOPT),
                        'note': '経路aは調整後EPS基準のピア実勢(業界全体の期待の高さ)で、許容値の根拠に使わない。事業実態EPS基準の ZS の PER は FY27 で約400倍超で比較不能。採用は b と c の重なり 1.1〜1.4。出口PEGは CAP に応じて 1.0(弱気)〜1.8(会社)'},
        'targets_12m': {k: round(T12[k], 1) for k in ('consensus', 'company', 'engine', 'bear')},
        'targets_12m_note': {
            'adopted_method': '定常状態経由(00_standard §3-2 の2)。近い年度の事業実態EPSがほぼゼロで、規約どおりの方法は不安定',
            'conventional_ntm_x_per': {k: round(T12_CONV[k], 1) for k in T12_CONV},
            'steady_state_route': {k: round(T12[k], 1) for k in T12},
            'dcf_cross_check': {k: round(T12_DCF[k], 1) for k in T12_DCF}},
        'adopted_path': ADOPTED, 'gaps': {k: round(v, 3) for k, v in GAPS.items()},
        'probabilities': PROB, 'expected_price': round(EVAL['expected_price'], 1), 'expected_return': round(EVAL['expected_return'], 3),
        'asymmetry': {'downside_pct': round(DOWN, 3), 'upside_pct': round(UP, 3),
                      'ratio': round(abs(UP / DOWN), 3) if UP > 0 else 0.0, 'convex': False},
        'decision': DEC,
        'entry_zones': {'alpha': ALPHA, 'Z1': round(ZONES['Z1'], 1), 'Z2': round(ZONES['Z2'], 1), 'zone': ZONES['zone']},
        'steady_state': {'steady_earnings_usd_mn': round(SS['base']['earnings'], 0),
                         'steady_state_value_usd_bn': round(SPLIT['base']['steady_state_value'], 2),
                         'growth_price_usd_bn': round(SPLIT['base']['growth_price'], 2),
                         'growth_share': round(SPLIT['base']['growth_share_of_mcap'], 3)},
        'value_time_split': {'within_3y': round(TS[0], 3), 'beyond_3y': round(TS[1], 3)},
        'cap_years': 11, 'incremental_roic': f'約{INCR_ROIC*100:.0f}%(SBC込みの成長投資に対する定常状態の税引後利益。推定)',
        'current_multiples': {'per_business_ntm': round(PER_BIZ_NTM, 0), 'per_adj_ntm': round(PRICE / NTM_ADJ_NOW, 1),
                              'peg_business_3y': round(PEG_BIZ_3Y, 2), 'peg_adj_3y': round(PEG_ADJ, 2),
                              'ev_sales_ntm': round(EV_SALES, 2), 'ev_fcf_ntm': round(EV_FCF, 1),
                              'fcf_margin_ttm': round(FCF_M_TTM, 3), 'sbc_to_revenue_ttm': round(SBC_R_TTM, 3)},
        'growth': {'revenue_yoy_latest_q': round(REVQ['FY26Q4'] / REVQ['FY25Q4'] - 1, 3), 'arr_or_proxy_yoy': 0.25,
                   'arr_proxy_name': 'ARR(Red Canary 込み 25%、有機 20%)', 'nnarr_or_proxy_yoy': 0.17,
                   'eps_cagr_3y_consensus': round(ADJ_CAGR_2Y, 3), 'eps_cagr_5y_engine': round(BIZ_CAGR_5Y_E, 3)},
        'rule_of_40': round(REV[2026] / REV[2025] - 1 + FCF_M_TTM, 3),
        'triggers': {
            'upgrade': ['SBC/売上が通期で 21%以下に低下し、調整後営業利益率 25%以上と同時に達成(SBC控除後営業利益率 ≥4%)',
                        '有機の純新規ARRが2四半期連続で前年比 +15%以上', '株価が分割エントリー圏の上限 Z2 以下'],
            'downgrade': ['有機の純新規ARRが前年比マイナスを2四半期連続', 'NRR が 112% 以下', 'SBC/売上が 25% 超に再上昇'],
            'exit': ['保有しない(見送り)。保有中なら: SBC控除後営業利益率が FY27 にマイナスのまま、かつ有機NNARRが減少']},
        'one_line': f'見送り: 調整後PEGは6社で最も低いが、SBC(売上の約25%)を費用とみなすとオーナー利益はほぼゼロ。株価はFY31 ARR 80億ドル超とSBC比率の急低下の両方を織り込み、事業エンジン経路の目標 {T12["engine"]:.0f} ドルを大きく上回る。Z2({ZONES["Z2"]:.0f}ドル)以下で再検討。',
        'data_corrections': 3, 'known_constraints': 12,
    }
    with open(os.path.join(OUT, 'ZS_summary.json'), 'w') as f:
        json.dump(s, f, ensure_ascii=False, indent=2)
    return s


def path_table(p):
    out = ['| 年度 | ARR | 純新規ARR | 売上 | 調整後営業利益率 | SBC/売上 | SBC控除後営業利益率 | 調整後EPS | 事業実態純利益 | 事業実態EPS |',
           '|---|---|---|---|---|---|---|---|---|---|']
    for y, r in p['rows'].items():
        out.append(f'| FY{y} | {r["arr"]:,.0f} | {r["nnarr"]:,.0f} | {r["rev"]:,.0f} | {r["opm"]*100:.1f}% | {r["sbc_ratio"]*100:.1f}% | '
                   f'{r["owner_margin"]*100:.1f}% | {r["adj_eps"]:.2f} | {r["biz_ni"]:,.0f} | {r["biz_eps"]:.2f} |')
    return '\n'.join(out)


if __name__ == '__main__':
    print('== 基本 ==')
    print(f'株価 {PRICE} / 株数 {SH_NOW} / 時価総額 {MCAP:.2f}bn / 純現金 {NET_CASH:.0f} / EV {EV:.2f}bn')
    print(f'株数: Q4FY26 {SH_Q4_26:.1f}, FY25 {SH_FY25:.1f}, FY26 {SH_FY26:.1f}, FY27 {SH_FY27}')
    print(f'SBC/売上 FY25 {SBC[2025]/REV[2025]:.4f} FY26 {SBC[2026]/REV[2026]:.4f}(別系列 {SBC_ALT[2025]/REV[2025]:.4f}/{SBC_ALT[2026]/REV[2026]:.4f})')
    print(f'事業実態EPS FY25 {BEPS_FY25:.3f} FY26 {BEPS_FY26:.3f}(別系列 {BEPS_FY26_ALT:.3f})(調整後 3.28 / 4.21)')
    print(f'FCF−SBC FY25 {FCF[2025]-SBC[2025]:.1f} FY26 {FCF[2026]-SBC[2026]:.1f}; FCF−SBC/売上 FY26 {(FCF[2026]-SBC[2026])/REV[2026]*100:.1f}%')
    print(f'調整後営業利益率 FY25 {opm25*100:.1f}% FY26 {opm26*100:.1f}% → SBC控除後 {(opm25-SBC[2025]/REV[2025])*100:.1f}% / {(opm26-SBC_R_TTM)*100:.1f}%')
    print(f'EPS対数分解 FY25→26: 売上 {logdec["revenue"]:.3f} 利益率 {logdec["margin"]:.3f}(うち営業利益率 {LOG_OPM:.3f}、受取利息・税 {LOG_OTHER:.3f}) 希薄化 {logdec["dilution"]:.3f} 計 {logdec["total"]:.3f}')
    print(f'RC 売上推定 {[round(v,1) for v in RC_REVQ.values()]} 計 {sum(RC_REVQ.values()):.1f}; 有機売上成長 FY26 {ORG_REV_YOY_FY*100:.1f}% Q4 {ORG_REV_YOY_Q4*100:.1f}%')
    print(f'Δ繰延収益 FY26 {DEF_REV[2026]-DEF_REV[2025]:.0f}; capex/売上 FY25 {CAPEX[2025]/REV[2025]*100:.1f}% FY26 {CAPEX[2026]/REV[2026]*100:.1f}%; OCF/売上 FY26 {OCF[2026]/REV[2026]*100:.1f}%')
    print()
    for k, p in {**PATHS, **VARIANTS}.items():
        t = RES.get(k) or RES_V.get(k)
        print(f'== {p["name"]} ==')
        print(path_table(p))
        print(f'NTM(2027-10) 事業実態EPS {t["ntm"]:.2f} / g(FY28→31) {t["g"]*100:.1f}% / 規約どおり目標 {t["conv_low"]:.1f}〜{t["conv_high"]:.1f}(中央 {t["conv_mid"]:.1f}、頭打ちなし {t["conv_mid_uncapped"]:.1f})')
        print(f'定常状態経由: FY31 EPS {p["rows"][2031]["biz_eps"]:.2f} × 出口PER {t["ss"]["per_exit"]:.1f}(PEG {p["exit_peg"]}, g_exit {t["g_exit"]*100:.1f}%)= {t["ss"]["value_at_exit"]:.1f} → 割引 {t["ss_target"]:.1f}')
        print(f'DCF 交差確認(2027-10-11 時点、減衰終了 FY{p["fade_to"]}): {t["dcf"]:.1f}')
        print()
    print('== 年度別適正株価(F13) ==')
    for k, p in PATHS.items():
        cells = []
        for y in range(2027, 2032):
            e = p['rows'][y]['biz_eps']; g = g3(p, y); lo, hi = PEG_BY_YEAR[y]
            cells.append(f'FY{y}: EPS {e:.2f} g {g*100:.0f}% PER {vl.fair_per(lo,g)["capped"]:.0f}〜{vl.fair_per(hi,g)["capped"]:.0f} → {vl.fair_per(lo,g)["capped"]*e:.0f}〜{vl.fair_per(hi,g)["capped"]*e:.0f}')
        print(k, ' / '.join(cells))
    print()
    print('== 定常状態 ==')
    for k, v in SS.items():
        s = SPLIT[k]
        print(f'{k}: 定常状態利益率 {v["margin"]*100:.1f}% 利益 {v["earnings"]:.0f} → 定常状態価値 {s["steady_state_value"]:.2f}bn ({s["steady_state_value"]*1000/SH_NOW:.1f}/株) 成長の値段 {s["growth_price"]:.2f}bn ({s["growth_share_of_mcap"]*100:.1f}%)')
    print(f'成長投資(SBC込み)FY26 {growth_cost:.0f} / 純新規ARR {NNARR26_ORG} → 1ドル当たり獲得費用 {CAC_PER_ARR:.2f}; 増分ROIC {INCR_ROIC*100:.1f}%; LTV(解約2%/4%) {LTV[0.02]:.2f}/{LTV[0.04]:.2f}; LTV/CAC {LTV[0.02]/CAC_PER_ARR:.2f}/{LTV[0.04]/CAC_PER_ARR:.2f}')
    print(f'価値の時間分布(エンジン、事業実態純利益の PV): 3年以内 {TS[0]*100:.1f}% / それ以降 {TS[1]*100:.1f}% / 総PV {TS[2]/1000:.1f}bn ({TS[2]/SH_NOW:.0f}/株)')
    print()
    print(f'== 価値感度(事業エンジン経路。基準: 定常状態経由 {BASE_T:.1f} / DCF {BASE_D:.1f}) ==')
    print('| 変数 | 定常(下) | 定常(上) | 幅 | DCF(下) | DCF(上) | 幅 |')
    for name, a, b, c, d in SENS:
        print(f'| {name} | {a:.1f} | {b:.1f} | {b-a:.1f} | {c:.1f} | {d:.1f} | {d-c:.1f} |')
    print()
    print('== F12 SBC/売上(行)× 調整後営業利益率(列)、FY31 ==')
    print('SBC行', [round(r31['sbc_ratio'] + s, 3) for s in F12_SBC], 'OPM列', [round(r31['opm'] + o, 3) for o in F12_OPM])
    for row in F12:
        print(' | '.join(f'{x:.0f}' for x in row))
    print(f'株価を正当化する FY31 SBC控除後営業利益率: 定常状態経由 {REQ_OWNER_SS*100:.1f}% / DCF {REQ_OWNER_DCF*100:.1f}%(エンジン経路 {r31["owner_margin"]*100:.1f}%)')
    print(f'会社の利益率・SBC経路のまま株価を正当化する NNARR 伸び(FY28-31 毎年): {REQ_NN*100:.1f}%')
    print()
    print('== 判断 ==')
    print('12か月目標(採用=定常状態経由):', {k: round(v, 1) for k, v in T12.items()})
    print('規約どおり(NTM×PER):', {k: round(v, 1) for k, v in T12_CONV.items()})
    print('DCF:', {k: round(v, 1) for k, v in T12_DCF.items()})
    print('乖離:', {k: round(v * 100, 1) for k, v in GAPS.items()}, 'DCF乖離:', {k: round(v * 100, 1) for k, v in GAPS_DCF.items()})
    print('期待値:', {k: round(v, 3) for k, v in EVAL.items()}, 'DCF期待値:', {k: round(v, 3) for k, v in EVAL_DCF.items()})
    print('判断:', DEC, '/ DCF での判断:', DEC_DCF)
    print('ゾーン:', {k: (round(v, 1) if isinstance(v, float) else v) for k, v in ZONES.items()})
    print('ゾーン(DCF):', {k: (round(v, 1) if isinstance(v, float) else v) for k, v in ZONES_DCF.items()})
    print(f'下値 {DOWN*100:.1f}% 上値 {UP*100:.1f}%')
    print(f'現在倍率: NTM調整後EPS {NTM_ADJ_NOW:.2f} PER {PRICE/NTM_ADJ_NOW:.1f}; NTM事業実態EPS {NTM_BIZ_NOW:.2f} PER {PER_BIZ_NTM:.0f}; '
          f'EV/売上 {EV_SALES:.1f}(5月安値時 {EV_SALES_MAY:.1f}); EV/FCF {EV_FCF:.1f}; 調整後2年CAGR {ADJ_CAGR_2Y*100:.1f}% PEG {PEG_ADJ:.2f}; '
          f'事業実態3年CAGR {BIZ_CAGR_3Y_C*100:.1f}% PEG {PEG_BIZ_3Y:.1f}; 事業実態5年CAGR エンジン {BIZ_CAGR_5Y_E*100:.1f}% コンセンサス {BIZ_CAGR_5Y_C*100:.1f}%')
    print(f'条件6: 5年PEG(FY26事業実態EPS基準 PER {PRICE/BEPS_FY26:.0f}) = {PRICE/BEPS_FY26/(BIZ_CAGR_5Y_E*100):.1f}(エンジン)')
    write_csvs()
    s = write_summary()
    print('CSV・summary を出力')
