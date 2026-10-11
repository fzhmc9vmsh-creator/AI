"""CrowdStrike (CRWD) の計算一式(報告書 analysis/CRWD_report.md の数値はすべてこの出力に一致させる)。

決算期末 1月31日。FY2027 = 2026-02-01〜2027-01-31。株数・EPS・株価はすべて 4:1 分割後(2026-07-01 取引終了後に実施)。
入力の出所は報告書 Appendix B・F。取得日 2026-10-11。金額は百万ドル(US$ mn)、EPS はドル。
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import math
import sys

sys.path.insert(0, '/home/user/AI/reports/security-stocks-2026-10/build')
import valuation_lib as vl  # noqa: E402

ROOT = '/home/user/AI/reports/security-stocks-2026-10'
OUT = f'{ROOT}/analysis'

# ---------------------------------------------------------------------------
# 0. 入力(検証済みの値。出所は報告書 Appendix B / F)
# ---------------------------------------------------------------------------
PRICE = 275.04            # 2026-10-09 終値(Yahoo Finance。前日 263.01 は CNBC・Heygotrade で一致)
DIL = 1044.469            # Q2 FY27 非GAAP 希薄化後加重平均株数(会社決算リリース、分割後)
DIL_YAGO = 999.634        # Q2 FY26 同(分割後換算)
BASIC = 1018.3            # 基本株数(2026-05-28 の 254.56M ×4、10-Q 表紙)
CASH = 5013.8             # 現金及び現金同等物 2026-07-31(10-Q 要約)
DEBT = 750.0              # 3.00% シニアノート 2029年2月満期(額面)
NET_CASH = CASH - DEBT
MCAP = PRICE * DIL        # 百万ドル(希薄化後)
EV = MCAP - NET_CASH
T_SBC = 0.22              # 共通基準 §3: 非GAAP 長期税率が不明のため 22%
T_ADJ = 0.23              # 調整後EPSの再現用(FY27 ガイダンス 1.25〜1.26 と営業利益から逆算した実効税率)
SHARE_G = 0.02            # 共通基準 §3-1: 過去2年の希薄化後株数の年増加率(FY25 平均 1,005.7 → Q2 FY27 1,044.5 で年約2%)
R = vl.COST_OF_CAPITAL

FYS = list(range(2027, 2040))          # FY2027〜FY2039(FY2032 以降は延長部分)
FY_END = {y: dt.date(y, 1, 31) for y in FYS}
LAST_CONSENSUS_EPS_FY = 2028            # コンセンサス EPS は FY28 まで(Yahoo 53名)。FY29 以降は延長
LAST_CONSENSUS_REV_FY = 2031            # 売上コンセンサスは FY31(TIKR、3名)まで。FY29・FY30 は補間
SEASON = [0.189, 0.246, 0.255, 0.310]   # FY27 の四半期 NNARR 構成(256 / 332.8 / 345 / 421 の中央値ベース)

# ---------------------------------------------------------------------------
# 1. 実績(四半期)。None = 欠損。派生値は報告書で明記
# ---------------------------------------------------------------------------
Q = [
    # q, rev, sub, arr, nnarr, nongaap_opinc, sbc(給与税込み), ocf, fcf, flex_arr, rpo
    ('FY25Q1', 921.0, 872.2, 3650, 211.7, 198.7, None, None, 322, None, None),
    ('FY25Q2', 963.9, 918.3, 3860, 217.6, None, None, None, 272, None, None),
    ('FY25Q3', 1010.2, 962.7, 4020, 153.0, 200.7, None, 326, 231, None, None),
    ('FY25Q4', 1060, 1010, 4240, 224.3, 224.8, None, 345.7, None, None, 6500),
    ('FY26Q1', 1100, 1050, 4440, 193.8, 201.1, 265.6, 384, 279, None, 6800),
    ('FY26Q2', 1170, 1100, 4660, 221.1, 255.0, 276.7, 332.4, 288.6, 1139, None),
    ('FY26Q3', 1230, 1170, 4920, 265.3, 264.6, 294.2, 398, 296, 1350, None),
    ('FY26Q4', 1310, 1240, 5250, 331.0, 325.8, 294.1, 497.9, 376.4, 1690, 9000),
    ('FY27Q1', 1390, None, 5510, 256.0, 325.7, 317.6, 591, 468, 1900, 8800),
    ('FY27Q2', 1470.9, 1400.3, 5840, 332.8, 371.6, 399.0, 530, 377, 2290, 10700),
]
KEYS = ['q', 'rev', 'sub', 'arr', 'nnarr', 'opinc', 'sbc', 'ocf', 'fcf', 'flex', 'rpo']
QD = [dict(zip(KEYS, row)) for row in Q]
FY_ACT = {  # 年度実績
    2025: dict(rev=3953.6, arr=4240, nnarr=806.6, opinc=879.9, adj_ni=814.6, adj_eps=3.24 / 4, sbc=865.4, ocf=1381.7, fcf=1070),
    2026: dict(rev=4810, arr=5250, nnarr=1011.2, opinc=1050.0, adj_ni=956.6, adj_eps=3.73 / 4, sbc=1130.6, ocf=1612.3, fcf=1240),
}


def p(*a):
    print(*a)


# ---------------------------------------------------------------------------
# 2. 確認層: TTM・異常値の計算
# ---------------------------------------------------------------------------
def ttm(key, upto=9):
    vals = [QD[i][key] for i in range(upto - 3, upto + 1)]
    return None if any(v is None for v in vals) else sum(vals)


TTM_REV = ttm('rev')
TTM_SBC = ttm('sbc')
TTM_FCF = ttm('fcf')
TTM_OCF = ttm('ocf')
TTM_NNARR = ttm('nnarr')
p('== 2. TTM(Q3 FY26〜Q2 FY27) ==')
p(f'売上 {TTM_REV:.1f} / SBC {TTM_SBC:.1f}({TTM_SBC/TTM_REV:.1%}) / 営業CF {TTM_OCF:.1f} / FCF {TTM_FCF:.1f}({TTM_FCF/TTM_REV:.1%})'
  f' / FCF−SBC {TTM_FCF-TTM_SBC:.1f}({(TTM_FCF-TTM_SBC)/TTM_REV:.1%}) / NNARR {TTM_NNARR:.1f}')
q2 = QD[9]
p(f'Q2 FY27: SBC/売上 {q2["sbc"]/q2["rev"]:.1%}、FCF−SBC {q2["fcf"]-q2["sbc"]:.1f}、capex {q2["ocf"]-q2["fcf"]:.0f}({(q2["ocf"]-q2["fcf"])/q2["rev"]:.1%})')
p(f'H1 FY27 SBC/売上 {(317.6+399.0)/(1390+1470.9):.1%}  FY26 {1130.6/4810:.1%}  FY25(10-K 純SBC) {865.4/3953.6:.1%}')

# 異常値 E1: NNARR の2年複利
p('== 異常値 E1: NNARR の前年比と2年複利 ==')
for i in range(8, 10):
    a, b, c = QD[i]['nnarr'], QD[i - 4]['nnarr'], QD[i - 8]['nnarr']
    p(f'{QD[i]["q"]}: NNARR {a} 前年比 {a/b-1:+.1%} / 2年前比 {a/c-1:+.1%}(年率 {math.sqrt(a/c)-1:+.1%})')
p(f'年度: FY25 {806.6} → FY26 {1011.2}({1011.2/806.6-1:+.1%}) → FY27ガイド中央 1355({1355/1011.2-1:+.1%})、FY25→FY27 年率 {math.sqrt(1355/806.6)-1:+.1%}')

# 異常値 E2: Flex ARR の増分と NNARR(付け替えの推計)
p('== 異常値 E2: Flex ARR の分解(推計) ==')
d_flex_y = 2290 - 1139
nn_y = sum(QD[i]['nnarr'] for i in range(6, 10))
nonflex_now, nonflex_yago = 5840 - 2290, 4660 - 1139
p(f'Flex ARR 1年増分 {d_flex_y}(前年 1,139 は 2,290÷2.01 の逆算)/ 同期間 NNARR {nn_y:.1f} → 比 {d_flex_y/nn_y:.0%}')
p(f'非Flex ARR: {nonflex_yago} → {nonflex_now}({nonflex_now/nonflex_yago-1:+.1%})')
FLEX_SCEN = {}
for label, newlogo_share, reflex in [('低', 0.25, 120), ('中', 0.30, 175), ('高', 0.34, 230)]:
    N = newlogo_share * nn_y               # Flex 経由の新規顧客 ARR
    A = (d_flex_y - N - reflex) / 1.40     # 既存の非Flex ARR から付け替えられた額(転換時 +40% の上乗せ)
    uplift = 0.40 * A
    flex_net_new = N + uplift + reflex
    FLEX_SCEN[label] = dict(N=N, A=A, uplift=uplift, reflex=reflex, flex_net_new=flex_net_new,
                            relabel_share_of_dflex=A / d_flex_y, flex_share_of_nnarr=flex_net_new / nn_y,
                            uplift_share_of_nnarr=uplift / nn_y, pool_conv_rate=A / nonflex_yago)
    p(f'[{label}] 新規Flex {N:.0f} / 付け替え {A:.0f}(ΔFlexの {A/d_flex_y:.0%})/ 上乗せ {uplift:.0f}(NNARRの {uplift/nn_y:.0%})'
      f' / 再Flex {reflex} / Flex起因の純増 {flex_net_new:.0f}(NNARRの {flex_net_new/nn_y:.0%})/ 非Flexプールの年転換率 {A/nonflex_yago:.1%}')

# NRR と新規の分解(FY26・FY27)
p('== 増収の源泉分解(ARR ベース) ==')
for fy, nn, arr_prev, nrr in [(2026, 1011.2, 4240, 1.15), (2027, 1355.0, 5250, 1.17)]:
    exp_net = (nrr - 1) * arr_prev
    churn = 0.03 * arr_prev
    newlogo = nn - exp_net
    p(f'FY{fy}: NNARR {nn:.0f} = 既存の純拡張 {exp_net:.0f}(NRR {nrr:.0%}、うち解約 −{churn:.0f}、総拡張 {exp_net+churn:.0f})+ 新規 {newlogo:.0f}({newlogo/nn:.0%})')

# EPS 対数分解 FY26 → FY27(調整後)
p('== EPS 対数分解 FY26→FY27(調整後、分割後) ==')
sh26 = 956.6 / (3.73 / 4)
rev27, eps27 = 6001.0, 1.255
sh27 = 1046.0
ni27 = eps27 * sh27
dec = vl.eps_log_decomposition(4810, rev27, 956.6 / 4810, ni27 / rev27, sh26, sh27)
p(f'FY26 株数 {sh26:.1f} / FY27 {sh27} / 調整後純利益率 {956.6/4810:.1%} → {ni27/rev27:.1%}')
p(f'ln分解: 売上 {dec["revenue"]:+.3f} / 純利益率 {dec["margin"]:+.3f} / 希薄化 {dec["dilution"]:+.3f} / 合計 {dec["total"]:+.3f}(実 {math.log(eps27/(3.73/4)):+.3f})')
op26, op27 = 1050.0 / 4810, 1518.0 / rev27
p(f'  純利益率の内訳: 営業利益率 {op26:.1%}→{op27:.1%}(ln {math.log(op27/op26):+.3f})、営業外・税の寄与 {dec["margin"]-math.log(op27/op26):+.3f}')

# ---------------------------------------------------------------------------
# 3. 経路モデル(コンセンサス / 会社シナリオ / 事業エンジン / 弱気)
# ---------------------------------------------------------------------------
K_REV = 6001.0 / (sum([(5250 + 5510) / 2, (5510 + 5840) / 2, (5840 + 6186) / 2, (6186 + 6607.5) / 2]) / 4)


def arr_to_rev(arr_begin, nnarr):
    q = [arr_begin]
    for s in SEASON:
        q.append(q[-1] + nnarr * s)
    mean_avg = sum((q[i] + q[i + 1]) / 2 for i in range(4)) / 4
    return K_REV * mean_avg, q[-1]


PATHS = {
    # nrr / new: 既存顧客の純拡張率(NRR−1)と新規ARR÷期初ARR。FY28〜FY39(延長を含む)
    'engine': dict(
        nrr=[1.160, 1.150, 1.140, 1.130, 1.120, 1.110, 1.100, 1.090, 1.085, 1.080, 1.075, 1.070],
        new=[0.078, 0.070, 0.063, 0.056, 0.050, 0.045, 0.040, 0.035, 0.032, 0.030, 0.028, 0.026],
        opm=[0.253, 0.275, 0.295, 0.310, 0.325, 0.335, 0.345, 0.355, 0.365, 0.375, 0.385, 0.395, 0.40],
        sbc=[0.255, 0.245, 0.230, 0.215, 0.200, 0.185, 0.170, 0.155, 0.140, 0.130, 0.120, 0.110, 0.10],
        fcfm=[0.31, 0.33, 0.35, 0.36, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37],
        peg_exit=1.6),
    'company': dict(
        nrr=[1.185, 1.180, 1.165, 1.150, 1.140, 1.130, 1.120, 1.110, 1.100, 1.090, 1.085, 1.080],
        new=[0.090, 0.085, 0.078, 0.070, 0.062, 0.055, 0.048, 0.042, 0.037, 0.033, 0.030, 0.028],
        opm=[0.253, 0.285, 0.320, 0.330, 0.340, 0.350, 0.360, 0.370, 0.380, 0.390, 0.400, 0.410, 0.42],
        sbc=[0.255, 0.235, 0.215, 0.195, 0.175, 0.155, 0.135, 0.120, 0.110, 0.100, 0.095, 0.090, 0.085],
        fcfm=[0.31, 0.34, 0.38, 0.385, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39],
        peg_exit=1.8),
    'bear': dict(
        nrr=[1.130, 1.120, 1.110, 1.100, 1.095, 1.090, 1.085, 1.080, 1.075, 1.070, 1.065, 1.060],
        new=[0.067, 0.058, 0.050, 0.044, 0.039, 0.035, 0.031, 0.028, 0.026, 0.024, 0.022, 0.020],
        opm=[0.253, 0.265, 0.280, 0.285, 0.290, 0.295, 0.300, 0.305, 0.310, 0.315, 0.320, 0.325, 0.33],
        sbc=[0.255, 0.260, 0.255, 0.245, 0.235, 0.225, 0.215, 0.205, 0.195, 0.185, 0.175, 0.165, 0.155],
        fcfm=[0.31, 0.31, 0.32, 0.33, 0.33, 0.33, 0.33, 0.33, 0.33, 0.33, 0.33, 0.33, 0.33],
        peg_exit=1.2),
    'consensus': dict(
        # 売上はコンセンサス(FY27 ガイド中央 6,001 / FY28 7,360 / FY31 12,950、FY29・FY30 は等比補間)。FY32 以降は延長
        rev_growth_ext=[0.170, 0.155, 0.140, 0.125, 0.115, 0.105, 0.095, 0.090],
        opm=[0.253, 0.270, 0.300, 0.310, 0.320, 0.330, 0.340, 0.350, 0.355, 0.365, 0.375, 0.385, 0.39],
        sbc=[0.255, 0.245, 0.230, 0.215, 0.200, 0.185, 0.170, 0.155, 0.140, 0.130, 0.120, 0.110, 0.10],
        fcfm=[0.31, 0.33, 0.35, 0.36, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37, 0.37],
        peg_exit=1.5),
}
CONS_ADJ_EPS = {2027: 1.26, 2028: 1.61}
M_AND_A = 600.0      # 年間の買収支出(FY27: SGNL 6.28億+Seraphic 約4.2億の後、年6億ドルを想定)
INT_RATE = 0.035     # 現金利回り
OTHER_FY27 = 187.0   # FY27 営業外収益(ガイダンスから逆算)


def build_path(name):
    P = PATHS[name]
    out = {}
    arr = 6607.5
    cash = CASH + 0.5 * 0  # FY27 末の現金は下で更新
    cash = 5400.0          # FY27 末の現金の見込み(7月末 5,014 + 下期 FCF 約 9.5億 − 社債以外の支出)
    for i, y in enumerate(FYS):
        shares_t = 1046.0 * (1 + SHARE_G) ** (y - 2027)
        if y == 2027:
            rev, nn, arr_end = 6001.0, 1356.3, 6607.5
            other = OTHER_FY27
        else:
            if name == 'consensus':
                if y == 2028:
                    rev = 7360.0
                elif y <= 2031:
                    g = (12950.0 / 7360.0) ** (1 / 3)
                    rev = 7360.0 * g ** (y - 2028)
                else:
                    rev = out[y - 1]['rev'] * (1 + P['rev_growth_ext'][y - 2032])
                nn, arr_end = None, None
            else:
                j = y - 2028
                nn = (P['nrr'][j] - 1 + P['new'][j]) * arr
                rev, arr_end = arr_to_rev(arr, nn)
                arr = arr_end
            other = INT_RATE * cash - 22.5 * (y <= 2029)
        opm = P['opm'][i]
        sbc_r = P['sbc'][i]
        opinc = opm * rev
        adj_ni = (opinc + other) * (1 - T_ADJ)
        if name == 'consensus' and y in CONS_ADJ_EPS:
            adj_ni = CONS_ADJ_EPS[y] * shares_t
        adj_eps = adj_ni / shares_t
        sbc = sbc_r * rev
        biz_ni = adj_ni - sbc * (1 - T_SBC)
        biz_eps = vl.business_eps_fixed_shares(adj_eps, shares_t, sbc, DIL, T_SBC)
        fcf = P['fcfm'][i] * rev
        if y > 2027:
            cash = cash + fcf - M_AND_A
        out[y] = dict(rev=rev, nnarr=nn, arr_end=arr_end, opm=opm, opinc=opinc, other=other, adj_ni=adj_ni,
                      shares_t=shares_t, adj_eps=adj_eps, sbc_ratio=sbc_r, sbc=sbc, biz_ni=biz_ni, biz_eps=biz_eps,
                      fcf=fcf, owner=biz_ni - M_AND_A, ext=(y > (LAST_CONSENSUS_EPS_FY if name == 'consensus' else 2027)))
    return out


MODEL = {n: build_path(n) for n in ['consensus', 'company', 'engine', 'bear']}

p('== 3. 経路別の年度パス(売上・ARR・調整後EPS・SBC比率・事業実態EPS) ==')
for n, m in MODEL.items():
    p(f'-- {n}')
    for y in range(2027, 2036):
        r = m[y]
        arr_s = f'{r["arr_end"]:,.0f}' if r['arr_end'] else '   -  '
        nn_s = f'{r["nnarr"]:,.0f}' if r['nnarr'] else '  -  '
        p(f'FY{y}: 売上 {r["rev"]:8,.0f} ARR末 {arr_s:>7} NNARR {nn_s:>6} 営業利益率 {r["opm"]:.1%} 調整後EPS {r["adj_eps"]:.2f}'
          f' SBC {r["sbc_ratio"]:.1%} 事業実態EPS {r["biz_eps"]:.3f}')

# ---------------------------------------------------------------------------
# 4. 目標株価: ①規約どおり(NTM×PEG×g) ②定常状態経由
# ---------------------------------------------------------------------------
PEG12 = {'consensus': (1.4, 1.6), 'company': (1.5, 1.7), 'engine': (1.4, 1.6), 'bear': (1.1, 1.3)}


def eps_dict(m, key='biz_eps'):
    return {FY_END[y]: m[y][key] for y in FYS}


def ntm_at(m, d, key='biz_eps'):
    return vl.ntm_eps(eps_dict(m, key), start=d)


RESULT = {}
p('== 4. 目標株価 ==')
for n, m in MODEL.items():
    ntm0 = ntm_at(m, vl.TARGET_DATE)
    ntm3 = ntm_at(m, dt.date(2030, 10, 11))
    g3 = vl.cagr(ntm0, ntm3, 3)
    lo, hi = PEG12[n]
    t_lo, t_hi = vl.target_price(ntm0, lo, g3), vl.target_price(ntm0, hi, g3)
    reg_mid = (t_lo['price'] + t_hi['price']) / 2
    # 定常状態経由: FY31(FY+5)の事業実態EPS、出口 g = FY31→FY34
    e31, e34 = m[2031]['biz_eps'], m[2034]['biz_eps']
    g_exit = vl.cagr(e31, e34, 3)
    ss = vl.steady_state_target(e31, FY_END[2031], PATHS[n]['peg_exit'], g_exit)
    RESULT[n] = dict(ntm=ntm0, g3=g3, peg=(lo, hi), regular=(t_lo['price'], t_hi['price']), regular_mid=reg_mid,
                     regular_uncapped=(t_lo['price_uncapped'], t_hi['price_uncapped']),
                     e31=e31, g_exit=g_exit, peg_exit=PATHS[n]['peg_exit'], per_exit=ss['per_exit'],
                     value_exit=ss['value_at_exit'], ss_target=ss['target'], years=ss['years_discounted'])
    p(f'{n:9s}: NTM事業実態EPS(2027-10) {ntm0:.3f} g3 {g3:.1%} PEG {lo}〜{hi} → 規約 {t_lo["price"]:.1f}〜{t_hi["price"]:.1f}'
      f'(頭打ちなし {t_lo["price_uncapped"]:.1f}〜{t_hi["price_uncapped"]:.1f})| 定常状態: FY31 EPS {e31:.3f} 出口g {g_exit:.1%}'
      f' 出口PEG {PATHS[n]["peg_exit"]} 出口PER {ss["per_exit"]:.1f} FY31末価値 {ss["value_at_exit"]:.1f} → 割引後 {ss["target"]:.1f}({ss["years_discounted"]:.2f}年)')

# ---------------------------------------------------------------------------
# 5. 交差確認: 長期の所有者利益DCF(事業実態純利益 − 買収支出、FY39 以降は 4% 成長)
# ---------------------------------------------------------------------------
G_T = 0.04


def dcf_value(m, at=vl.VALUATION_DATE, r=R, g_t=G_T):
    pv = 0.0
    for y in range(2028, 2040):
        t = (FY_END[y] - at).days / 365.25
        if t <= 0:
            continue
        pv += m[y]['owner'] / (1 + r) ** t
    tv = m[2039]['owner'] * (1 + g_t) / (r - g_t)
    t39 = (FY_END[2039] - at).days / 365.25
    pv += tv / (1 + r) ** t39
    # FY27 残り(2026-10〜2027-01)の所有者利益は小さいので含めない。純現金を加える
    return (pv + NET_CASH) / DIL, tv / (1 + r) ** t39 / DIL


p('== 5. 交差確認: 所有者利益DCF(1株、評価日 2026-10-11) ==')
DCF = {}
for n, m in MODEL.items():
    v, tv = dcf_value(m)
    v12 = dcf_value(m, at=vl.TARGET_DATE)[0]
    DCF[n] = dict(now=v, at_target=v12, tv_share=tv / v)
    p(f'{n:9s}: 1株価値 {v:.1f}(うち終価 {tv/v:.0%})/ 2027-10-11 時点 {v12:.1f}')
for rr in (0.08, 0.10):
    p(f'  資本コスト {rr:.0%}: engine {dcf_value(MODEL["engine"], r=rr)[0]:.1f} / company {dcf_value(MODEL["company"], r=rr)[0]:.1f}')


# リバースDCF: 株価 275.04 を正当化する ARR 成長率(FY28〜FY37 一定、以後 FY39 まで 8%→、終価 4%)
def path_flat_growth(g):
    m = {}
    arr = 6607.5
    cash = 5400.0
    E = PATHS['engine']
    for i, y in enumerate(FYS):
        if y == 2027:
            m[y] = dict(MODEL['engine'][2027])
            continue
        gy = g if y <= 2037 else 0.08
        nn = gy * arr
        rev, arr_end = arr_to_rev(arr, nn)
        arr = arr_end
        other = INT_RATE * cash
        opinc = E['opm'][i] * rev
        adj_ni = (opinc + other) * (1 - T_ADJ)
        sbc = E['sbc'][i] * rev
        biz_ni = adj_ni - sbc * (1 - T_SBC)
        cash += E['fcfm'][i] * rev - M_AND_A
        m[y] = dict(owner=biz_ni - M_AND_A, rev=rev, arr_end=arr_end)
    return m


def implied_growth(target_price):
    lo, hi = 0.0, 0.8
    for _ in range(60):
        mid = (lo + hi) / 2
        v, _ = dcf_value(path_flat_growth(mid))
        if v < target_price:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


G_IMPL = implied_growth(PRICE)
m_impl = path_flat_growth(G_IMPL)
p(f'== リバースDCF: 株価 {PRICE} が織り込む ARR 年成長率(FY28〜FY37 一定)= {G_IMPL:.1%}'
  f' → FY37 末 ARR {m_impl[2037]["arr_end"]/1000:,.0f} 十億ドル(会社目標 FY35 200億ドル)')
G_IMPL_8 = None
# 資本コスト 8% での織り込み成長率
_save = R


def implied_growth_r(target_price, r):
    lo, hi = 0.0, 0.8
    for _ in range(60):
        mid = (lo + hi) / 2
        v, _ = dcf_value(path_flat_growth(mid), r=r)
        if v < target_price:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


G_IMPL_8 = implied_growth_r(PRICE, 0.08)
p(f'   資本コスト 8% なら {G_IMPL_8:.1%}')

# ---------------------------------------------------------------------------
# 6. 成長の値段と価値の時間分布
# ---------------------------------------------------------------------------
ARR_NOW = 5840.0
SS = {}
for label, opm_ss, sbc_ss in [('低', 0.45, 0.10), ('中', 0.49, 0.08), ('高', 0.53, 0.06)]:
    pre = (opm_ss - sbc_ss) * ARR_NOW + INT_RATE * NET_CASH
    earn = pre * (1 - T_SBC)
    split = vl.steady_state_split(earn, MCAP)
    SS[label] = dict(opm=opm_ss, sbc=sbc_ss, earnings=earn, **split)
    p(f'定常状態[{label}]: 非GAAP営業利益率 {opm_ss:.0%}・SBC {sbc_ss:.0%} → 定常状態利益 {earn:,.0f} 価値 {split["steady_state_value"]/1000:.1f}十億 成長の値段 {split["growth_price"]/1000:.1f}十億({split["growth_share_of_mcap"]:.0%})')

# 価値の時間分布(事業エンジン経路のDCF)
m = MODEL['engine']
pv3 = sum(m[y]['owner'] / (1 + R) ** ((FY_END[y] - vl.VALUATION_DATE).days / 365.25) for y in (2028, 2029, 2030))
v_total = dcf_value(m)[0] * DIL - NET_CASH
TIME_SPLIT = dict(within_3y=pv3 / v_total, beyond_3y=1 - pv3 / v_total)
p(f'価値の時間分布(engine): 3年以内 {TIME_SPLIT["within_3y"]:.1%} / それ以降 {TIME_SPLIT["beyond_3y"]:.1%}')

# ---------------------------------------------------------------------------
# 7. 価値感度分析(芯の特定): engine の定常状態経由目標と DCF の変化
# ---------------------------------------------------------------------------


def engine_variant(**kw):
    base = PATHS['engine']
    saved = {k: base[k] for k in kw}
    for k, v in kw.items():
        base[k] = v
    mm = build_path('engine')
    for k, v in saved.items():
        base[k] = v
    return mm


def ss_target(mm, peg=None):
    peg = peg or PATHS['engine']['peg_exit']
    e31, e34 = mm[2031]['biz_eps'], mm[2034]['biz_eps']
    return vl.steady_state_target(e31, FY_END[2031], peg, vl.cagr(e31, e34, 3))['target']


E = PATHS['engine']
base_ss = ss_target(MODEL['engine'])
base_dcf = dcf_value(MODEL['engine'])[0]
SENS = []


def add_sens(name, lo_m, hi_m, rng):
    lo_ss, hi_ss = ss_target(lo_m), ss_target(hi_m)
    lo_d, hi_d = dcf_value(lo_m)[0], dcf_value(hi_m)[0]
    SENS.append(dict(var=name, range=rng, ss_lo=lo_ss, ss_hi=hi_ss, dcf_lo=lo_d, dcf_hi=hi_d,
                     swing_ss=abs(hi_ss - lo_ss), swing_dcf=abs(hi_d - lo_d)))


add_sens('NRR(既存顧客の純拡張)', engine_variant(nrr=[x - 0.03 for x in E['nrr']]), engine_variant(nrr=[x + 0.03 for x in E['nrr']]), '各年 ±3pt')
add_sens('新規ARR率', engine_variant(new=[x * 0.7 for x in E['new']]), engine_variant(new=[x * 1.3 for x in E['new']]), '各年 ±30%')
sbc_slow = [E['sbc'][0]] + [min(0.255, E['sbc'][i] + 0.01 * i) for i in range(1, 13)]
sbc_fast = [E['sbc'][0]] + [max(0.06, E['sbc'][i] - 0.007 * i) for i in range(1, 13)]
add_sens('SBC/売上の低下速度', engine_variant(sbc=sbc_slow), engine_variant(sbc=sbc_fast), '年 −0.5pt 〜 −2.2pt')
add_sens('非GAAP営業利益率', engine_variant(opm=[E['opm'][0]] + [x - 0.03 for x in E['opm'][1:]]),
         engine_variant(opm=[E['opm'][0]] + [x + 0.03 for x in E['opm'][1:]]), 'FY28以降 ±3pt')
lo_m = MODEL['engine']
SENS.append(dict(var='競争優位期間(出口PEG)', range='出口PEG 1.3〜1.9', ss_lo=ss_target(lo_m, 1.3), ss_hi=ss_target(lo_m, 1.9),
                 dcf_lo=dcf_value(lo_m, g_t=0.03)[0], dcf_hi=dcf_value(lo_m, g_t=0.05)[0],
                 swing_ss=abs(ss_target(lo_m, 1.9) - ss_target(lo_m, 1.3)),
                 swing_dcf=abs(dcf_value(lo_m, g_t=0.05)[0] - dcf_value(lo_m, g_t=0.03)[0])))
SENS.append(dict(var='資本コスト', range='8%〜10%', ss_lo=vl.steady_state_target(lo_m[2031]['biz_eps'], FY_END[2031], 1.6, vl.cagr(lo_m[2031]['biz_eps'], lo_m[2034]['biz_eps'], 3), r=0.10)['target'],
                 ss_hi=vl.steady_state_target(lo_m[2031]['biz_eps'], FY_END[2031], 1.6, vl.cagr(lo_m[2031]['biz_eps'], lo_m[2034]['biz_eps'], 3), r=0.08)['target'],
                 dcf_lo=dcf_value(lo_m, r=0.10)[0], dcf_hi=dcf_value(lo_m, r=0.08)[0], swing_ss=0, swing_dcf=abs(dcf_value(lo_m, r=0.08)[0] - dcf_value(lo_m, r=0.10)[0])))
SENS[-1]['swing_ss'] = abs(SENS[-1]['ss_hi'] - SENS[-1]['ss_lo'])
SENS.sort(key=lambda d: -d['swing_dcf'])
p(f'== 7. 価値感度(engine 基準: 定常状態目標 {base_ss:.1f} / DCF {base_dcf:.1f}) ==')
for s in SENS:
    p(f'{s["var"]:22s} {s["range"]:18s} 定常状態 {s["ss_lo"]:.1f}〜{s["ss_hi"]:.1f}(振れ {s["swing_ss"]:.1f})/ DCF {s["dcf_lo"]:.1f}〜{s["dcf_hi"]:.1f}(振れ {s["swing_dcf"]:.1f})')

# F12: 感応度マトリクス(SBC/売上の FY31 水準 × 出口PEG)と(NRR シフト × 営業利益率シフト)
p('== F12a: FY31 の SBC/売上 × 出口PEG → 定常状態経由の目標株価(engine) ==')
F12A = {}
for sbc31 in (0.12, 0.16, 0.20, 0.24):
    # FY28→FY31 を線形に置き換え、以後 −1.5pt/年で 10% まで
    path = [0.255]
    for k in range(1, 5):
        path.append(0.255 + (sbc31 - 0.255) * k / 4)
    for k in range(5, 13):
        path.append(max(0.10, sbc31 - 0.015 * (k - 4)))
    mm = engine_variant(sbc=path)
    row = []
    for peg in (1.2, 1.5, 1.8, 2.0):
        row.append(ss_target(mm, peg))
    F12A[sbc31] = row
    p(f'SBC {sbc31:.0%}: ' + ' / '.join(f'PEG {pg}: {v:.1f}' for pg, v in zip((1.2, 1.5, 1.8, 2.0), row)))
p('== F12b: NRR シフト × 営業利益率シフト → DCF 1株価値(engine) ==')
F12B = {}
for dn in (-0.03, 0.0, 0.03, 0.06):
    row = []
    for do in (-0.03, 0.0, 0.03, 0.06):
        mm = engine_variant(nrr=[x + dn for x in E['nrr']], opm=[E['opm'][0]] + [x + do for x in E['opm'][1:]])
        row.append(dcf_value(mm)[0])
    F12B[dn] = row
    p(f'NRR {dn:+.0%}: ' + ' / '.join(f'opm {do:+.0%}: {v:.1f}' for do, v in zip((-0.03, 0.0, 0.03, 0.06), row)))

# 株価 275 を定常状態経由で正当化する FY31 事業実態EPS
need_v31 = PRICE * (1 + R) ** RESULT['engine']['years']
p(f'株価 {PRICE} を正当化する FY31 末価値 {need_v31:.1f} → 出口PER 100(PEG 2.0×g 50%)なら FY31 事業実態EPS {need_v31/100:.2f}、出口PER 50 なら {need_v31/50:.2f}')

# ---------------------------------------------------------------------------
# 8. 現在の倍率
# ---------------------------------------------------------------------------
cm = MODEL['consensus']
ntm_adj_now = vl.ntm_eps(eps_dict(cm, 'adj_eps'), start=vl.VALUATION_DATE)
ntm_biz_now = vl.ntm_eps(eps_dict(cm, 'biz_eps'), start=vl.VALUATION_DATE)
ntm_adj_3 = vl.ntm_eps(eps_dict(cm, 'adj_eps'), start=dt.date(2029, 10, 11))
ntm_biz_3 = vl.ntm_eps(eps_dict(cm, 'biz_eps'), start=dt.date(2029, 10, 11))
g_adj3 = vl.cagr(ntm_adj_now, ntm_adj_3, 3)
g_biz3 = vl.cagr(ntm_biz_now, ntm_biz_3, 3)
ntm_rev = vl.ntm_eps({FY_END[y]: cm[y]['rev'] for y in FYS}, start=vl.VALUATION_DATE)
ntm_fcf = vl.ntm_eps({FY_END[y]: cm[y]['fcf'] for y in FYS}, start=vl.VALUATION_DATE)
CUR = dict(per_business_ntm=PRICE / ntm_biz_now, per_adj_ntm=PRICE / ntm_adj_now,
           peg_business_3y=(PRICE / ntm_biz_now) / (min(g_biz3, 9.99) * 100), peg_adj_3y=(PRICE / ntm_adj_now) / (g_adj3 * 100),
           ev_sales_ntm=EV / ntm_rev, ev_fcf_ntm=EV / ntm_fcf, fcf_margin_ttm=TTM_FCF / TTM_REV, sbc_to_revenue_ttm=TTM_SBC / TTM_REV)
p('== 8. 現在の倍率(コンセンサス経路) ==')
p(f'時価総額 {MCAP/1000:.1f}十億(希薄化後)/ 基本株数ベース {PRICE*BASIC/1000:.1f}十億 / 純現金 {NET_CASH/1000:.2f}十億 / EV {EV/1000:.1f}十億 / EV÷期末ARR {EV/5840:.1f}倍')
p(f'NTM 調整後EPS {ntm_adj_now:.3f} → PER {CUR["per_adj_ntm"]:.0f} / 3年g {g_adj3:.1%} → PEG {CUR["peg_adj_3y"]:.2f}')
p(f'NTM 事業実態EPS {ntm_biz_now:.3f} → PER {CUR["per_business_ntm"]:.0f} / 3年g {g_biz3:.1%} → PEG {CUR["peg_business_3y"]:.2f}')
p(f'EV/NTM売上 {CUR["ev_sales_ntm"]:.1f} / EV/NTM FCF {CUR["ev_fcf_ntm"]:.0f} / FCFマージン TTM {CUR["fcf_margin_ttm"]:.1%} / SBC/売上 TTM {CUR["sbc_to_revenue_ttm"]:.1%}')
RULE40 = (1470.9 / 1170 - 1) + TTM_FCF / TTM_REV
p(f'Rule of 40(Q2 売上成長+TTM FCFマージン)= {RULE40*100:.1f}')
# 条件6: 5年CAGR
for n in ('consensus', 'engine', 'company', 'bear'):
    mm = MODEL[n]
    ca = vl.cagr(mm[2027]['adj_eps'], mm[2032]['adj_eps'], 5)
    cb = vl.cagr(mm[2027]['biz_eps'], mm[2032]['biz_eps'], 5)
    pa = (PRICE / mm[2027]['adj_eps']) / (ca * 100)
    pb = (PRICE / mm[2028]['biz_eps']) / (min(cb, 0.5) * 100)
    p(f'条件6 {n:9s}: 調整後EPS 5年CAGR(FY27→32){ca:.1%} PEG {pa:.1f} / 事業実態EPS 5年CAGR {cb:.1%}(FY28基準PER÷頭打ち50%の PEG {pb:.1f})')

# ---------------------------------------------------------------------------
# 9. 採用目標・確率・期待値・ゾーン・判断
# ---------------------------------------------------------------------------
ADOPT = 'ss'   # 定常状態経由を採用(理由は報告書 10章)
TGT = {n: (RESULT[n]['ss_target'] if ADOPT == 'ss' else RESULT[n]['regular_mid']) for n in RESULT}
PROB = {'bear': 0.25, 'consensus': 0.30, 'engine': 0.30, 'company': 0.15}
ev = vl.expected_value(TGT, PROB, PRICE)
STRUCT = 'A'
ALPHA = 0.20
EDGE = True
Z = vl.zones(B=TGT['engine'], U=TGT['company'], L=TGT['bear'], alpha=ALPHA, price=PRICE, edge=EDGE)
GAPS = {n: vl.gap(TGT[n], PRICE) for n in ('consensus', 'company', 'engine')}
DEC = vl.decision(STRUCT, GAPS['engine'], EDGE)
p('== 9. 採用目標(定常状態経由)と判断 ==')
for n in ('consensus', 'company', 'engine', 'bear'):
    p(f'{n:9s}: 目標 {TGT[n]:.1f}(規約どおり {RESULT[n]["regular"][0]:.1f}〜{RESULT[n]["regular"][1]:.1f})乖離 {vl.gap(TGT[n], PRICE):+.1%} / DCF交差 {DCF[n]["at_target"]:.1f}')
p(f'期待株価 {ev["expected_price"]:.1f} 期待リターン {ev["expected_return"]:+.1%}')
p(f'ゾーン: α {ALPHA} Z1 {Z["Z1"]:.1f} Z2 {Z["Z2"]:.1f} → {Z["zone"]}  上値/下値比 {Z["upside_downside_ratio"]}')
p(f'判断(構造 {STRUCT}、乖離 {GAPS["engine"]:+.1%}、エッジ {EDGE}): {DEC}')
down = (TGT['bear'] - PRICE) / PRICE
up = (TGT['company'] - PRICE) / PRICE
p(f'非対称性: 下値 {down:+.1%} / 上値 {up:+.1%}')

# DCF ベースの代替(併記用)
DCF_TGT = {n: DCF[n]['at_target'] for n in DCF}
ev_dcf = vl.expected_value(DCF_TGT, PROB, PRICE)
p(f'代替(DCF 2027-10-11 時点)の期待株価 {ev_dcf["expected_price"]:.1f}({ev_dcf["expected_return"]:+.1%})')

# 増分ROIC(経済的損益、FY27)
growth_sm = (0.27 - 0.10) * 6001
growth_rd = (0.17 - 0.12) * 6001
growth_sbc = (0.255 - 0.08) * 6001
growth_capex = 0.04 * 6001
growth_ma = 1050
invest = growth_sm + growth_rd + growth_sbc + growth_capex + growth_ma
inc_earn = 1356.3 * (0.49 - 0.08) * (1 - T_SBC)
p(f'== 増分ROIC(FY27、推計): 成長投資 {invest:,.0f}(S&M {growth_sm:.0f}・R&D {growth_rd:.0f}・成長人員のSBC {growth_sbc:.0f}・capex {growth_capex:.0f}・買収 {growth_ma})'
  f' / NNARR 1,356 の定常状態税引後利益 {inc_earn:.0f} → 増分ROIC {inc_earn/invest:.1%}(買収除き {inc_earn/(invest-growth_ma):.1%})')
INC_ROIC = (inc_earn / invest, inc_earn / (invest - growth_ma))

# ---------------------------------------------------------------------------
# 10. CSV 出力(F13・F18・F10)
# ---------------------------------------------------------------------------
PEG_BY_FY = {  # 年度別 PEG レンジ(報告書 Appendix B に根拠)
    'consensus': {2027: (1.3, 1.5), 2028: (1.4, 1.6), 2029: (1.4, 1.6), 2030: (1.5, 1.7), 2031: (1.5, 1.7), 2032: (1.5, 1.7), 2033: (1.5, 1.7), 2034: (1.5, 1.7), 2035: (1.4, 1.6)},
    'engine': {2027: (1.3, 1.5), 2028: (1.4, 1.6), 2029: (1.4, 1.6), 2030: (1.5, 1.7), 2031: (1.5, 1.7), 2032: (1.6, 1.8), 2033: (1.6, 1.8), 2034: (1.5, 1.7), 2035: (1.5, 1.7)},
    'company': {2027: (1.4, 1.6), 2028: (1.5, 1.7), 2029: (1.5, 1.7), 2030: (1.6, 1.8), 2031: (1.7, 1.9), 2032: (1.7, 1.9), 2033: (1.7, 1.9), 2034: (1.6, 1.8), 2035: (1.6, 1.8)},
    'bear': {2027: (1.0, 1.2), 2028: (1.1, 1.3), 2029: (1.1, 1.3), 2030: (1.1, 1.3), 2031: (1.1, 1.3), 2032: (1.1, 1.3), 2033: (1.1, 1.3), 2034: (1.0, 1.2), 2035: (1.0, 1.2)},
}
F13_ROWS = []
with open(f'{OUT}/CRWD_F13.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['fy_end', 'path', 'business_eps', 'g_3y', 'peg_low', 'peg_high', 'fair_per_low', 'fair_per_high',
                'fair_price_low', 'fair_price_high', 'is_extension'])
    for n in ('consensus', 'company', 'engine', 'bear'):
        mm = MODEL[n]
        for y in range(2027, 2036):
            e0, e3 = mm[y]['biz_eps'], mm[y + 3]['biz_eps']
            g = vl.cagr(e0, e3, 3)
            lo, hi = PEG_BY_FY[n][y]
            fl, fh = vl.fair_per(lo, g)['capped'], vl.fair_per(hi, g)['capped']
            ext = (y > 2028) if n == 'consensus' else (y > 2027)
            row = [FY_END[y].isoformat(), n, round(e0, 3), round(g, 3), lo, hi, round(fl, 1), round(fh, 1),
                   round(fl * e0, 1), round(fh * e0, 1), int(ext)]
            w.writerow(row)
            F13_ROWS.append(row)
p('== F13(engine の抜粋) ==')
for r in F13_ROWS:
    if r[1] == 'engine':
        p(r)

with open(f'{OUT}/CRWD_F18.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['kpi', 'period', 'value', 'qoq_annualized', 'ttm_yoy', 'second_diff'])
    F18 = {}
    for key, name in [('arr', 'ending_arr_usd_mn'), ('nnarr', 'net_new_arr_usd_mn'), ('rev', 'total_revenue_usd_mn'),
                      ('flex', 'flex_arr_usd_mn'), ('sbc_ratio', 'sbc_to_revenue'), ('fcf_margin', 'fcf_margin')]:
        prev_yoy = None
        for i, d in enumerate(QD):
            if key == 'sbc_ratio':
                v = d['sbc'] / d['rev'] if d['sbc'] else None
            elif key == 'fcf_margin':
                v = d['fcf'] / d['rev'] if d['fcf'] else None
            else:
                v = d[key]
            if v is None:
                continue
            qoq = None
            if i >= 1 and key in ('arr', 'rev', 'flex'):
                pv_ = QD[i - 1][key]
                if pv_:
                    qoq = (v / pv_) ** 4 - 1
            yoy = None
            if key == 'arr' and i >= 4:
                yoy = v / QD[i - 4]['arr'] - 1
            elif key in ('nnarr', 'rev') and i >= 7:
                cur = sum(QD[k][key] for k in range(i - 3, i + 1))
                old = sum(QD[k][key] for k in range(i - 7, i - 3))
                yoy = cur / old - 1
            elif key == 'flex' and d['q'] in ('FY26Q3', 'FY26Q4', 'FY27Q1', 'FY27Q2'):
                yoy = {'FY26Q3': 2.00, 'FY26Q4': 1.20, 'FY27Q1': 0.99, 'FY27Q2': 1.01}[d['q']]
            elif key in ('sbc_ratio', 'fcf_margin') and i >= 4:
                pq = QD[i - 4]
                pv2 = (pq['sbc'] / pq['rev']) if key == 'sbc_ratio' and pq['sbc'] else ((pq['fcf'] / pq['rev']) if key == 'fcf_margin' and pq['fcf'] else None)
                yoy = (v - pv2) if pv2 is not None else None  # 比率は前年差(pt)
            sd = (yoy - prev_yoy) if (yoy is not None and prev_yoy is not None) else None
            prev_yoy = yoy if yoy is not None else prev_yoy
            fmt = lambda x: '' if x is None else round(x, 4)
            w.writerow([name, d['q'], round(v, 4) if isinstance(v, float) else v, fmt(qoq), fmt(yoy), fmt(sd)])
            F18.setdefault(name, []).append((d['q'], v, qoq, yoy, sd))
        # 単四半期の前年比(NNARR)を別に出す
    for i, d in enumerate(QD):
        if i >= 4:
            yoy = d['nnarr'] / QD[i - 4]['nnarr'] - 1
            w.writerow(['net_new_arr_single_q_yoy', d['q'], round(yoy, 4), '', '', ''])
        if i >= 4:
            yoy = d['arr'] / QD[i - 4]['arr'] - 1
            w.writerow(['ending_arr_yoy', d['q'], round(yoy, 4), '', '', ''])
p('== F18(ARR・NNARR・SBC比率) ==')
for k in ('ending_arr_usd_mn', 'net_new_arr_usd_mn', 'sbc_to_revenue', 'fcf_margin', 'flex_arr_usd_mn'):
    for row in F18.get(k, []):
        p(k, row[0], round(row[1], 3) if isinstance(row[1], float) else row[1],
          *(None if x is None else round(x, 3) for x in row[2:]))

with open(f'{OUT}/CRWD_F10.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['period', 'line', 'revenue_usd_mn'])
    for d in QD:
        if d['sub'] is not None:
            w.writerow([d['q'], 'subscription', d['sub']])
            w.writerow([d['q'], 'professional_services', round(d['rev'] - d['sub'], 1)])
        else:
            w.writerow([d['q'], 'subscription_and_services_total(内訳欠損)', d['rev']])
    # ARR の製品ライン構成(Q2 FY26 は成長率からの逆算、Q2 FY27 は会社資料の「超」表記の下限)
    lines = {'cloud_security_arr': (905, 0.29), 'next_gen_identity_arr': (585, 0.33), 'next_gen_siem_arr': (695, 0.60)}
    core_now = 5840 - sum(v for v, _ in lines.values())
    core_yago = 4660 - sum(v / (1 + g) for v, g in lines.values())
    for ln, (v, g) in lines.items():
        w.writerow(['FY26Q2', ln, round(v / (1 + g), 0)])
        w.writerow(['FY27Q2', ln, v])
    w.writerow(['FY26Q2', 'endpoint_and_other_arr(残差)', round(core_yago, 0)])
    w.writerow(['FY27Q2', 'endpoint_and_other_arr(残差)', round(core_now, 0)])
p(f'== F10: 新興3ライン ARR {sum(v for v,_ in lines.values())}(前年 {sum(v/(1+g) for v,g in lines.values()):.0f}、+{sum(v for v,_ in lines.values())/sum(v/(1+g) for v,g in lines.values())-1:.0%})'
  f' / 残差(エンドポイント等){core_yago:.0f} → {core_now:.0f}({core_now/core_yago-1:+.1%})')

# 経路別のパス表(Appendix B 用)を JSON で残す
with open(f'{OUT}/CRWD_paths.json', 'w') as f:
    json.dump({n: {str(y): {k: (round(v, 4) if isinstance(v, float) else v) for k, v in MODEL[n][y].items()} for y in FYS}
               for n in MODEL}, f, ensure_ascii=False, indent=1)

# ---------------------------------------------------------------------------
# 11. summary.json
# ---------------------------------------------------------------------------
summary = {
    'ticker': 'CRWD', 'company': 'CrowdStrike Holdings, Inc.', 'price': PRICE, 'price_date': '2026-10-09',
    'market_cap_usd_bn': round(MCAP / 1000, 1), 'diluted_shares_mn': DIL, 'fy_end_month': 1,
    'net_cash_usd_bn': round(NET_CASH / 1000, 2),
    'structure_rating': STRUCT,
    'condition_ratings': {'1': 'A', '2': 'B', '3': 'B', '4': 'S', '5': 'A', '6': 'D', '7': 'D', '8': 'A', '9': 'B',
                          '10': 'B', '11': 'A', '12': 'A', '13': 'A'},
    'condition9_applicable': True,
    'rules_fired': ['対象外(N/A)なし(条件9は適用)', '致命条件の拒否権: 非発動(E以下なし)', '条件6-7の対評価: 発動(PEGは全経路で1を大きく超え、安い理由の検証は前提不成立)',
                    'C×4上限: 非発動(C評価0)'],
    'archetype': 'ORCL型寄り(継続課金・業務停止不可の運用基盤)。ただしSBCが重く1株当たりの所有者利益が薄い',
    'business_model_types': ['A(ストック型SaaS: Falconサブスクリプション)', 'B(Flex: 契約枠からの引き出し型。Next-Gen SIEMはデータ量課金)'],
    'core_variables': [
        {'name': 'SBC/売上の低下経路', 'market_implied': '株価275ドルは、SBC控除後の所有者利益で見ると、SBC比率がFY31までに10%前後へ下がりARRが年30%前後で10年続くことと整合(リバースDCF)。コンセンサスはSBCを除外して見ている',
         'our_estimate': 'FY27 25.5%(Q2単独27.1%と上昇中)→FY31 20.0%→FY35 14.0%(ServiceNowの年−0.5〜−1.5ptを参照)', 'advantage_type': '分析(SBC控除後の事業実態EPS・所有者利益での再計算)'},
        {'name': 'NNARRの持続(既存顧客の純拡張と新規)', 'market_implied': 'コンセンサス売上FY28 7,360(NNARR横ばい相当)〜FY31 12,950。株価はそれを大きく上回る成長を織り込む',
         'our_estimate': 'FY28 NNARR 約1,580(NRR 116%・新規7.8%)、ARR FY31 約145億ドル。Flex転換の上乗せ(+40%)はNNARRの約15%で、非Flexプール(35.5億ドル)の縮小とともに年1割程度ずつ薄れる', 'advantage_type': '分析(Flex ARRの付け替え分解とコホートの再Flex)'},
        {'name': '競争優位期間(出口倍率)', 'market_implied': '出口PER換算で100倍超を要する', 'our_estimate': 'CAP 12年前後、出口PEG 1.6(出口PER 約' + f"{RESULT['engine']['per_exit']:.0f}" + '倍)', 'advantage_type': '分析'},
    ],
    'edge': {'exists': True,
             'statement': '市場はAI時代の勝者として調整後EPS・FCF(SBC足し戻し後)で値付けし、株価は売上コンセンサスがほぼ動かない中で年初来2.5倍になった。SBCを費用として扱うと、株価275ドルはARRが年約' + f'{G_IMPL:.0%}' + 'で10年続くこと(会社目標の約2倍のペース)を要する。差は、SBC/売上が下がらない(FY27は25%超へ上昇)ことと、FY28のNNARR成長が20%前後に落ち着くことで確認される',
             'advantage_type': '分析', 'kpi': 'SBC/売上(四半期)とNNARR前年比', 'threshold': 'SBC/売上が2四半期連続で24%以上かつFY28 NNARRガイダンスが+20%程度(>25%でない)',
             'timing': 'Q3 FY27(2026年12月上旬)〜Q4 FY27とFY28ガイダンス(2027年3月上旬)', 'value_per_share_if_resolved': round(TGT['engine'], 1)},
    'eps_definition': '事業実態EPS = (調整後EPS×株数_t − SBC(雇用主給与税込み)×(1−22%))÷現在の希薄化後株数1,044.469百万株。分割後',
    'base_business_eps': {'fy': 'FY2027(1月期、コンセンサス調整後EPS 1.26)', 'value': round(MODEL['consensus'][2027]['biz_eps'], 3)},
    'eps_paths': {n: {f'FY{y}': round(MODEL[n][y]['biz_eps'], 3) for y in range(2027, 2036)} for n in ('consensus', 'company', 'engine', 'bear')},
    'adj_eps_consensus': {f'FY{y}': round(MODEL['consensus'][y]['adj_eps'], 3) for y in range(2027, 2032)},
    'sbc_to_revenue_path': {f'FY{y}': PATHS['engine']['sbc'][y - 2027] for y in range(2027, 2036)},
    'allowed_peg': {'path_a': [3.4, 9.9], 'path_b': [1.3, 1.8], 'path_c': [1.4, 1.8], 'adopted': [1.4, 1.7],
                    'note': '経路aは6社の調整後PEG(市場が業界に付ける倍率で許容値ではない)。採用は年度別に1.4〜1.7(engine)、出口PEGは1.6。'
                            f"12か月目標: 規約どおり(NTM事業実態EPS×PEG×g)= engine {RESULT['engine']['regular'][0]:.1f}〜{RESULT['engine']['regular'][1]:.1f}、"
                            f"consensus {RESULT['consensus']['regular'][0]:.1f}〜{RESULT['consensus']['regular'][1]:.1f}、company {RESULT['company']['regular'][0]:.1f}〜{RESULT['company']['regular'][1]:.1f}、bear {RESULT['bear']['regular'][0]:.1f}〜{RESULT['bear']['regular'][1]:.1f}。"
                            f"定常状態経由(採用)= engine {TGT['engine']:.1f}、consensus {TGT['consensus']:.1f}、company {TGT['company']:.1f}、bear {TGT['bear']:.1f}。"
                            f"交差確認の所有者利益DCF(2027-10-11)= engine {DCF['engine']['at_target']:.1f}、company {DCF['company']['at_target']:.1f}"},
    'targets_12m': {n: round(TGT[n], 1) for n in ('consensus', 'company', 'engine', 'bear')},
    'adopted_path': 'engine',
    'gaps': {n: round(GAPS[n], 3) for n in GAPS},
    'probabilities': PROB,
    'expected_price': round(ev['expected_price'], 1), 'expected_return': round(ev['expected_return'], 3),
    'asymmetry': {'downside_pct': round(down, 3), 'upside_pct': round(up, 3), 'ratio': None, 'convex': False},
    'decision': DEC,
    'entry_zones': {'alpha': ALPHA, 'Z1': round(Z['Z1'], 1), 'Z2': round(Z['Z2'], 1), 'zone': Z['zone']},
    'steady_state': {'steady_earnings_usd_mn': round(SS['中']['earnings'], 0), 'steady_state_value_usd_bn': round(SS['中']['steady_state_value'] / 1000, 1),
                     'growth_price_usd_bn': round(SS['中']['growth_price'] / 1000, 1), 'growth_share': round(SS['中']['growth_share_of_mcap'], 3)},
    'value_time_split': {'within_3y': round(TIME_SPLIT['within_3y'], 3), 'beyond_3y': round(TIME_SPLIT['beyond_3y'], 3)},
    'cap_years': 12, 'incremental_roic': f'約{INC_ROIC[0]:.0%}(買収を含む)〜{INC_ROIC[1]:.0%}(買収除き)。資本コスト9%を上回るが、SBCを成長投資に含めると高くはない',
    'current_multiples': {k: round(v, 3) for k, v in CUR.items()},
    'growth': {'revenue_yoy_latest_q': round(1470.9 / 1170 - 1, 3), 'arr_or_proxy_yoy': round(5840 / 4660 - 1, 3), 'arr_proxy_name': '期末ARR',
               'nnarr_or_proxy_yoy': round(332.8 / 221.1 - 1, 3), 'eps_cagr_3y_consensus': round(vl.cagr(MODEL['consensus'][2027]['adj_eps'], MODEL['consensus'][2030]['adj_eps'], 3), 3),
               'eps_cagr_5y_engine': round(vl.cagr(MODEL['engine'][2027]['biz_eps'], MODEL['engine'][2032]['biz_eps'], 5), 3)},
    'rule_of_40': round(RULE40 * 100, 1),
    'triggers': {
        'upgrade': ['株価が事業エンジン経路の分割エントリー圏上限(Z2)以下に下がる',
                    'SBC/売上が2四半期連続で前年比2pt以上低下し、FY28ガイダンスが営業利益率30%以上',
                    'FY28 NNARRガイダンス+25%以上かつ再Flex顧客の拡張率+25%以上の維持'],
        'downgrade': ['GRRが96%以下に低下', 'NNARRが2四半期連続で前年割れ(一時要因で説明できない)', 'SBC/売上がFY28も25%以上'],
        'exit': ['保有していないため該当なし(監視)。保有中なら: Flex顧客ARRの前年比が+40%を下回り、かつNNARRが前年割れ']},
    'one_line': '事業はA評価の優良企業だが、株価275ドルはSBC控除後の所有者利益に対してARR年約' + f'{G_IMPL:.0%}' + '成長が10年続く前提を要し、事業エンジン経路の12か月目標' + f"{TGT['engine']:.0f}" + 'ドルを大きく上回るため監視(買付は' + f"{Z['Z2']:.0f}" + 'ドル以下、確認KPIはSBC/売上とNNARR)',
    'data_corrections': 14, 'known_constraints': 12,
}
with open(f'{OUT}/CRWD_summary.json', 'w') as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
p('summary.json written')
