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
SBC = {2025: 685.5, 2026: 841.6}           # 株式報酬+関連給与税(会社の調整表)
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

# ---------------------------------------------------------------------------
# 1. 事業実態EPS(基準EPS)と EPS 対数分解
# ---------------------------------------------------------------------------
def biz_ni(adj_ni, sbc, tax=TAX):
    return adj_ni - sbc * (1 - tax)


BEPS_FY26 = biz_ni(NG_NI[2026], SBC[2026]) / SH_NOW
BEPS_FY25 = biz_ni(NG_NI[2025], SBC[2025]) / SH_NOW
logdec = vl.eps_log_decomposition(REV[2025], REV[2026], NG_NI[2025] / REV[2025], NG_NI[2026] / REV[2026], SH_FY25, SH_FY26)
opm25, opm26 = NG_OPI[2025] / REV[2025], NG_OPI[2026] / REV[2026]

# ---------------------------------------------------------------------------
# 2. 経路モデル(年度 FY27〜FY34。FY31 = FY+5、FY34 = FY+8)
# ---------------------------------------------------------------------------
YEARS = list(range(2027, 2035))
K27, K = 0.959, 0.962          # 売上 ÷ 期首期末平均ARR(FY27 ガイダンスと FY26 実績 0.974 から設定)
ARR26 = 3771.0
NNARR26_ORG = 615 + (141 - 98)  # 有機の純新規ARR(Red Canary 除く 615 + 取得後の Red Canary の純増 43)= 658
INT_FY27, INT_FY28 = 140.7, 140.0   # 受取利息(FY27 ガイダンス・FY28 コンセンサスから逆算)
YIELD = 0.035                  # FY29 以降: (純現金 + 事業実態純利益の累計)× 3.5%(転換社債は 2028-07 に現金償還と仮定)


def fy_end(y):
    return dt.date(y, 7, 31)


def run_path(name, arr27, nn_growth, opm, sbc_ratio, rev_override=None, adj_eps_override=None, exit_peg=1.5):
    """年度別の ARR・売上・調整後純利益・SBC・事業実態EPS を返す。"""
    arr = {2026: ARR26}
    nn = {2027: arr27 - ARR26}
    arr[2027] = arr27
    rows = {}
    cum_biz = 0.0
    for i, y in enumerate(YEARS):
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
    return dict(name=name, rows=rows, exit_peg=exit_peg)


def lin(start, step, y0=2027):
    return {y: start + step * (y - y0) for y in YEARS}


def grow(seq):
    return {y: g for y, g in zip(range(2028, 2035), seq)}


SBC_BASE = lin(0.241, -0.010)      # FY26 25.1% から年 −1.0pt(過去3年の実績 −0.3〜−0.5pt/年より速い前提)
SBC_FAST = lin(0.236, -0.015)      # 会社シナリオ: 年 −1.5pt
SBC_SLOW = lin(0.246, -0.005)      # 弱気: 年 −0.5pt(株価下落局面のリテンション付与で高止まり)

PATHS = {}
PATHS['consensus'] = run_path(
    'コンセンサス経路', 4411, grow([None, 0.05, 0.05, 0.05, 0.03, 0.03, 0.03]),
    {**lin(0.0, 0.0), **{y: 0.245 + 0.0075 * (y - 2028) for y in YEARS if y >= 2029}}, SBC_BASE,
    rev_override={2027: {'rev': 3930.0}, 2028: {'rev': 4580.0, 'arr': 2 * 4580.0 / K - 4411}},
    adj_eps_override={2027: 4.91, 2028: 5.60}, exit_peg=1.5)
PATHS['company'] = run_path(
    '会社シナリオ経路', 4411, grow([0.15, 0.15, 0.15, 0.15, 0.10, 0.10, 0.10]),
    lin(0.2365, 0.015), SBC_FAST, exit_peg=1.8)
PATHS['engine'] = run_path(
    '事業エンジン経路', 4450, grow([0.09, 0.06, 0.04, 0.03, 0.02, 0.02, 0.02]),
    lin(0.237, 0.010), SBC_BASE, exit_peg=1.5)
PATHS['bear'] = run_path(
    '弱気パス', 4396, grow([-0.05, -0.05, -0.05, -0.05, -0.03, -0.03, -0.03]),
    lin(0.235, 0.005), SBC_SLOW, exit_peg=1.0)
# コンセンサス FY29 以降の営業利益率(FY28 の逆算値から年 +0.75pt)を再計算
c28 = PATHS['consensus']['rows'][2028]['opm']
PATHS['consensus'] = run_path(
    'コンセンサス経路', 4411, grow([None, 0.05, 0.05, 0.05, 0.03, 0.03, 0.03]),
    {y: c28 + 0.0075 * (y - 2028) for y in YEARS}, SBC_BASE,
    rev_override={2027: {'rev': 3930.0}, 2028: {'rev': 4580.0, 'arr': 2 * 4580.0 / K - 4411}},
    adj_eps_override={2027: 4.91, 2028: 5.60}, exit_peg=1.5)

# 年度別PEGレンジ(9章で導出。採用 1.1〜1.4 を年度別に配分)
PEG_BY_YEAR = {2027: (1.0, 1.2), 2028: (1.1, 1.3), 2029: (1.1, 1.4), 2030: (1.2, 1.4), 2031: (1.2, 1.5)}
PEG_ADOPT = (1.1, 1.4)


def g3(path, y):
    r = path['rows']
    a, b = r[y]['biz_eps'], r[y + 3]['biz_eps']
    return vl.cagr(a, b, 3) if a > 0 and b > 0 else float('nan')


def targets(path):
    r = path['rows']
    eps = {fy_end(y): r[y]['biz_eps'] for y in YEARS}
    ntm = vl.ntm_eps(eps)                                # 2027-10-11 時点の NTM
    g = vl.cagr(r[2028]['biz_eps'], r[2031]['biz_eps'], 3)
    conv = {p: vl.target_price(ntm, p, g) for p in PEG_ADOPT}
    g_exit = vl.cagr(r[2031]['biz_eps'], r[2034]['biz_eps'], 3)
    ss = vl.steady_state_target(r[2031]['biz_eps'], fy_end(2031), path['exit_peg'], g_exit)
    return dict(ntm=ntm, g=g, conv_low=conv[PEG_ADOPT[0]]['price'], conv_high=conv[PEG_ADOPT[1]]['price'],
                conv_mid=vl.target_price(ntm, sum(PEG_ADOPT) / 2, g)['price'],
                g_exit=g_exit, ss=ss, ss_target=ss['target'])


def dcf_value(path, at=vl.TARGET_DATE, g_term=0.04, r=vl.COST_OF_CAPITAL, fade_to=2044):
    """交差確認: 事業実態純利益の DCF(FY34 の成長率から FY44 にかけて g_term へ線形に減衰、以後永続)。"""
    rows = path['rows']
    cf = {y: rows[y]['biz_ni'] for y in YEARS}
    g34 = rows[2034]['biz_ni'] / rows[2033]['biz_ni'] - 1
    last = cf[2034]
    for i, y in enumerate(range(2035, fade_to + 1)):
        gy = g34 + (g_term - g34) * (i + 1) / (fade_to - 2034)
        last *= 1 + gy
        cf[y] = last
    tv = cf[fade_to] * (1 + g_term) / (r - g_term)
    pv = 0.0
    for y, v in cf.items():
        t = (fy_end(y) - at).days / 365.25
        if t < 0:
            t_frac = 0
            continue
        pv += v / (1 + r) ** t
    t_last = (fy_end(fade_to) - at).days / 365.25
    pv += tv / (1 + r) ** t_last
    return pv / SH_NOW


RES = {k: targets(p) for k, p in PATHS.items()}
DCF = {k: dcf_value(p) for k, p in PATHS.items()}

# ---------------------------------------------------------------------------
# 3. 定常状態利益と成長の値段(FY26 実績ベース。SBC を含む全費用で計算)
# ---------------------------------------------------------------------------
GM_NG = 2691.6 / REV[2026]          # non-GAAP 粗利率 80.3%
SBC_COGS = 87.5 / REV[2026]         # 売上原価の SBC 2.6%
# non-GAAP 営業費用の内訳(推定: FY25 GAAP 内訳 S&M 47.1%・R&D 25.1%・G&A 9.4% から SBC 推定額を除いて FY26 に適用)
OPEX_NG = {'S&M': 0.355, 'R&D': 0.160, 'G&A': 0.059}
SBC_OPEX = {'S&M': 0.100, 'R&D': 0.095, 'G&A': 0.030}   # 計 22.5%(+COGS 2.6% = 25.1%)
MAINT = {'S&M': 0.35, 'R&D': 0.55, 'G&A': 1.00}       # 成長投資を止めても残る比率(推定)


def steady_state(maint=MAINT, rev=REV[2026]):
    cogs_all = (1 - GM_NG) + SBC_COGS
    opex_all = sum((OPEX_NG[k] + SBC_OPEX[k]) * maint[k] for k in OPEX_NG)
    margin = 1 - cogs_all - opex_all
    pretax = rev * margin + NET_CASH * YIELD
    return dict(margin=margin, earnings=pretax * (1 - TAX))


SS_BASE = steady_state()
SS_LOW = steady_state({'S&M': 0.45, 'R&D': 0.65, 'G&A': 1.0})
SS_HIGH = steady_state({'S&M': 0.25, 'R&D': 0.45, 'G&A': 0.9})
SPLIT = {k: vl.steady_state_split(v['earnings'] / 1000, MCAP) for k, v in
         {'base': SS_BASE, 'low': SS_LOW, 'high': SS_HIGH}.items()}

# 増分の経済性(1ドルの純新規ARRの獲得費用と生涯価値。推定)
growth_cost = sum((OPEX_NG[k] + SBC_OPEX[k]) * (1 - MAINT[k]) for k in OPEX_NG) * REV[2026]
CAC_PER_ARR = growth_cost / NNARR26_ORG
LTV = {gc: SS_BASE['margin'] * (1 - TAX) / (vl.COST_OF_CAPITAL + gc - 0.03) for gc in (0.02, 0.04)}
INCR_ROIC = SS_BASE['margin'] * (1 - TAX) / CAC_PER_ARR

# 価値の時間分布(事業実態純利益の現在価値: 3年以内 vs それ以降、エンジン経路)
def time_split(path):
    rows = path['rows']
    pv3 = sum(rows[y]['biz_ni'] / (1.09 ** (y - 2026 - 0.2)) for y in (2027, 2028, 2029))
    total = dcf_value(path, at=vl.VALUATION_DATE) * SH_NOW
    return pv3 / total, 1 - pv3 / total, total


TS = time_split(PATHS['engine'])

# ---------------------------------------------------------------------------
# 4. 価値感度分析(事業エンジン経路の定常状態経由の目標株価を ±で動かす)
# ---------------------------------------------------------------------------
def engine_variant(nn=None, sbc_shift=0.0, opm_shift=0.0, peg=1.5, tax=None, refi=False):
    global TAX, YIELD
    old_tax = TAX
    if tax is not None:
        TAX = tax
    nn = nn or [0.09, 0.06, 0.04, 0.03, 0.02, 0.02, 0.02]
    sbc = {y: SBC_BASE[y] + sbc_shift * (y - 2026) / 5 for y in YEARS}
    opm = {y: 0.237 + 0.010 * (y - 2027) + opm_shift * (y - 2026) / 5 for y in YEARS}
    p = run_path('v', 4450, grow(nn), opm, sbc, exit_peg=peg)
    if refi:  # 転換社債を借り換えて受取利息が残る場合(+60百万ドル/年)
        for y in YEARS:
            if y >= 2029:
                r = p['rows'][y]
                r['adj_ni'] += 60 * (1 - TAX)
                r['biz_ni'] += 60 * (1 - TAX)
                r['biz_eps'] = r['biz_ni'] / SH_NOW
    t = targets(p)['ss_target']
    TAX = old_tax
    return t


BASE_T = engine_variant()
SENS = [
    ('有機の純新規ARRの伸び(FY28〜31、年 ±5pt)', engine_variant(nn=[0.04, 0.01, -0.01, -0.02, -0.03, -0.03, -0.03]),
     engine_variant(nn=[0.14, 0.11, 0.09, 0.08, 0.05, 0.05, 0.05])),
    ('SBC/売上(FY31 時点 ±3pt)', engine_variant(sbc_shift=+0.03), engine_variant(sbc_shift=-0.03)),
    ('調整後営業利益率(FY31 時点 ±3pt)', engine_variant(opm_shift=-0.03), engine_variant(opm_shift=+0.03)),
    ('出口PEG(±0.3、競争優位期間)', engine_variant(peg=1.2), engine_variant(peg=1.8)),
    ('税率(±2pt)', engine_variant(tax=0.23), engine_variant(tax=0.19)),
    ('転換社債の借り換え(受取利息の残存)', BASE_T, engine_variant(refi=True)),
]
SENS.sort(key=lambda s: -(s[2] - s[1]))

# F12: SBC/売上(FY31)× 調整後営業利益率(FY31)の感応度マトリクス(事業エンジン経路)
F12 = []
for sbc_s in (+0.03, 0.0, -0.03, -0.06):
    F12.append([engine_variant(sbc_shift=sbc_s, opm_shift=o) for o in (-0.03, 0.0, +0.03, +0.06)])

# 逆算: 株価 233.73 を正当化する FY31 の「SBC控除後営業利益率」(事業エンジンの売上経路で)
def solve_owner_margin(target=PRICE):
    lo, hi = -0.20, 0.40
    for _ in range(60):
        mid = (lo + hi) / 2
        t = engine_variant(sbc_shift=-mid)
        lo, hi = (mid, hi) if t < target else (lo, mid)
    return mid


REQ_SBC_CUT = solve_owner_margin()
r31 = PATHS['engine']['rows'][2031]
REQ_OWNER_M31 = r31['opm'] - (r31['sbc_ratio'] - REQ_SBC_CUT)

# ---------------------------------------------------------------------------
# 5. 判断(構造評価・PEG・2軸・エントリー・期待値)
# ---------------------------------------------------------------------------
RATINGS = {'1': 'C', '2': 'B', '3': 'B', '4': 'S', '5': 'B', '6': 'D', '7': 'C', '8': 'B', '9': 'C',
           '10': 'B', '11': 'C', '12': 'B', '13': 'B'}
STRUCT = 'B'
EDGE = True   # 差分あり(方向は下: 市場は SBC 控除前の FCF で評価)
ADOPTED = 'engine'
T12 = {k: RES[k]['ss_target'] for k in RES}
PROB = {'bear': 0.20, 'consensus': 0.30, 'engine': 0.35, 'company': 0.15}
EVAL = vl.expected_value(T12, PROB, PRICE)
GAPS = {k: vl.gap(T12[k], PRICE) for k in ('consensus', 'company', 'engine')}
DEC = vl.decision(STRUCT, GAPS[ADOPTED], EDGE)
ALPHA = 0.25
ZONES = vl.zones(B=T12['engine'], U=T12['company'], L=T12['bear'], alpha=ALPHA, price=PRICE, edge=EDGE)

# 現在の倍率
NTM_ADJ_NOW = vl.ntm_eps({fy_end(2027): 4.91, fy_end(2028): 5.60}, start=dt.date(2026, 10, 11))
NTM_BIZ_NOW = vl.ntm_eps({fy_end(y): PATHS['consensus']['rows'][y]['biz_eps'] for y in (2027, 2028)}, start=dt.date(2026, 10, 11))
NTM_REV = 3930 * 10 / 12 + 4580 * 2 / 12
NTM_FCF = NTM_REV * 0.2325
ADJ_CAGR_2Y = vl.cagr(4.21, 5.60, 2)
BIZ_CAGR_3Y_C = vl.cagr(PATHS['consensus']['rows'][2027]['biz_eps'], PATHS['consensus']['rows'][2030]['biz_eps'], 3)


def fmt(x, d=2):
    return f'{x:,.{d}f}'


if __name__ == '__main__':
    print('== 基本 ==')
    print(f'株価 {PRICE} / 株数 {SH_NOW} / 時価総額 {MCAP:.2f}bn / 純現金 {NET_CASH:.0f} / EV {EV:.2f}bn')
    print(f'株数: Q4FY26 {SH_Q4_26:.1f}, FY25 {SH_FY25:.1f}, FY26 {SH_FY26:.1f}, FY27 {SH_FY27}')
    print(f'SBC/売上 FY25 {SBC[2025]/REV[2025]:.3f} FY26 {SBC[2026]/REV[2026]:.3f}')
    print(f'事業実態EPS FY25 {BEPS_FY25:.3f} FY26 {BEPS_FY26:.3f}  (調整後 3.28 / 4.21)')
    print(f'FCF−SBC FY25 {FCF[2025]-SBC[2025]:.1f} FY26 {FCF[2026]-SBC[2026]:.1f}; FCF−SBC(純SBC 815) {FCF[2026]-815:.1f}')
    print(f'EPS対数分解 FY25→26: 売上 {logdec["revenue"]:.3f} 利益率 {logdec["margin"]:.3f} 希薄化 {logdec["dilution"]:.3f} 計 {logdec["total"]:.3f} (ln(4.21/3.28)={math.log(4.21/3.28):.3f})')
    print(f'  営業利益率 {opm25:.3f}->{opm26:.3f} ln比 {math.log(opm26/opm25):.3f}')
    print()
    for k, p in PATHS.items():
        print(f'== {p["name"]} ==')
        print('| FY | ARR | 純新規ARR | 売上 | 調整後営業利益率 | 受取利息 | 調整後EPS | SBC/売上 | SBC控除後営業利益率 | 事業実態純利益 | 事業実態EPS |')
        print('|---|---|---|---|---|---|---|---|---|---|---|')
        for y, r in p['rows'].items():
            print(f'| FY{y} | {r["arr"]:,.0f} | {r["nnarr"]:,.0f} | {r["rev"]:,.0f} | {r["opm"]*100:.1f}% | {r["interest"]:.0f} | {r["adj_eps"]:.2f} | {r["sbc_ratio"]*100:.1f}% | {r["owner_margin"]*100:.1f}% | {r["biz_ni"]:,.0f} | {r["biz_eps"]:.2f} |')
        t = RES[k]
        print(f'NTM(2027-10) 事業実態EPS {t["ntm"]:.2f} / g(FY28→31) {t["g"]*100:.1f}% / 規約どおり目標 {t["conv_low"]:.1f}〜{t["conv_high"]:.1f}(中央 {t["conv_mid"]:.1f})')
        print(f'定常状態経由: FY31 EPS {p["rows"][2031]["biz_eps"]:.2f} × 出口PER {t["ss"]["per_exit"]:.1f}(PEG {p["exit_peg"]}, g_exit {t["g_exit"]*100:.1f}%)= {t["ss"]["value_at_exit"]:.1f} → 割引 {t["ss_target"]:.1f}')
        print(f'DCF 交差確認(2027-10-11 時点): {DCF[k]:.1f}')
        print()
    print('== 定常状態 ==')
    for k, v in {'base': SS_BASE, 'low': SS_LOW, 'high': SS_HIGH}.items():
        s = SPLIT[k]
        print(f'{k}: 定常状態利益率 {v["margin"]*100:.1f}% 利益 {v["earnings"]:.0f} → 定常状態価値 {s["steady_state_value"]:.2f}bn ({s["steady_state_value"]*1000/SH_NOW:.1f}/株) 成長の値段 {s["growth_price"]:.2f}bn ({s["growth_share_of_mcap"]*100:.1f}%)')
    print(f'成長投資(SBC込み)FY26 {growth_cost:.0f} / 純新規ARR {NNARR26_ORG} → 1ドル当たり獲得費用 {CAC_PER_ARR:.2f}; 増分ROIC {INCR_ROIC*100:.1f}%; LTV(解約2%/4%) {LTV[0.02]:.2f}/{LTV[0.04]:.2f}; LTV/CAC {LTV[0.02]/CAC_PER_ARR:.2f}/{LTV[0.04]/CAC_PER_ARR:.2f}')
    print(f'価値の時間分布(エンジン、事業実態純利益の PV): 3年以内 {TS[0]*100:.1f}% / それ以降 {TS[1]*100:.1f}% / 総PV {TS[2]/1000:.1f}bn')
    print()
    print('== 価値感度(事業エンジン経路・定常状態経由の目標株価、基準 %.1f) ==' % BASE_T)
    for name, lo, hi in SENS:
        print(f'| {name} | {lo:.1f} | {hi:.1f} | {hi-lo:.1f} |')
    print()
    print('== F12 SBC/売上(行: FY31 シフト +3,0,−3,−6pt)× 調整後営業利益率(列: −3,0,+3,+6pt) ==')
    for row in F12:
        print(' | '.join(f'{x:.0f}' for x in row))
    print(f'株価を正当化する FY31 SBC控除後営業利益率: {REQ_OWNER_M31*100:.1f}%(エンジン経路の FY31 は {r31["owner_margin"]*100:.1f}%、SBC を {REQ_SBC_CUT*100:.1f}pt 追加で下げる必要)')
    print()
    print('== 判断 ==')
    print('12か月目標(採用=定常状態経由):', {k: round(v, 1) for k, v in T12.items()})
    print('乖離:', {k: round(v * 100, 1) for k, v in GAPS.items()})
    print('期待値:', {k: round(v, 3) for k, v in EVAL.items()})
    print('判断:', DEC, '/ ゾーン:', ZONES)
    print(f'現在倍率: NTM調整後EPS {NTM_ADJ_NOW:.2f} PER {PRICE/NTM_ADJ_NOW:.1f}; NTM事業実態EPS {NTM_BIZ_NOW:.2f} PER {PRICE/NTM_BIZ_NOW:.0f}; '
          f'EV/売上 {EV*1000/NTM_REV:.1f}; EV/FCF {EV*1000/NTM_FCF:.1f}; 調整後2年CAGR {ADJ_CAGR_2Y*100:.1f}% PEG {PRICE/NTM_ADJ_NOW/(ADJ_CAGR_2Y*100):.2f}; 事業実態3年CAGR {BIZ_CAGR_3Y_C*100:.1f}% PEG {PRICE/NTM_BIZ_NOW/(min(BIZ_CAGR_3Y_C,0.5)*100):.1f}')
