"""PANW(Palo Alto Networks、決算期末 7月31日)の計算一式。

規約: 00_standard.md(§3 事業実態EPS、§3-1 株数、§3-2 定常状態経由、§4 目標株価)、valuation-model.md、
scenario-strategy.md §6。すべての報告書の数値はこのスクリプトの出力と一致させる。
入力の出所は各定数のコメントに記す(取得日はすべて 2026-10-11)。
実行: python3 analysis/PANW_calc.py  → 標準出力に要約、analysis/ に CSV と JSON を書く。
"""
import sys
import csv
import json
import math
import datetime as dt

sys.path.insert(0, '/home/user/AI/reports/security-stocks-2026-10/build')
import valuation_lib as vl  # noqa: E402

ROOT = '/home/user/AI/reports/security-stocks-2026-10'
T = 'PANW'

# ---------------------------------------------------------------- 1. 検証済み入力
PRICE = 418.78                 # 2026-10-09 終値(peer_peg_table.md、Yahoo・Seeking Alpha 一致)
PRICE_DATE = '2026-10-09'
SH_BASIC = 818.0               # 発行済(2026-08-31、10-K 表紙)
SH_DIL = 840.0                 # 希薄化後: Q1 FY27 ガイダンスの前提 837〜844 百万株の中央(8-K 2026-09-01)
TAX = 0.22                     # 会社の non-GAAP 長期税率
CASH_INV = 7906.0              # 現金同等物 2,514 + 投資 5,392(10-K FY2026、2026-07-31)
CONV_FV = 1774.0               # CyberArk 承継の 2030年満期交換社債(公正価値オプション、元本 12.5億ドル、残高約11億ドル)
NET_CASH = CASH_INV - CONV_FV  # 社債を公正価値で控除(保守側)
MCAP_BASIC = PRICE * SH_BASIC / 1000   # 十億ドル
MCAP_DIL = PRICE * SH_DIL / 1000
EV_DIL = MCAP_DIL - NET_CASH / 1000

# 実績(百万ドル)。出所: 8-K 決算リリース(FY25・FY26 Q4)、非GAAP 調整表、10-K FY2026
REV = {2023: 6893, 2024: 8028, 2025: 9221, 2026: 11480}
PRODUCT = {2025: 1802, 2026: 2280}
SUBSUP = {2025: 7419, 2026: 9200}
SBC_REL = {2023: 1145, 2024: 1162, 2025: 1386, 2026: 1712}   # 株式報酬関連費用(給与税込み、非GAAP 加算額)
SBC_ACCEL_FY26 = 177          # FY26 の SBC に含まれる買収関連の加速償却(10-K。CyberArk・Koi)
NG_OPM = {2025: 0.288, 2026: 0.292}   # non-GAAP 営業利益率(FY26 投資家資料、+40bp)
NG_GM = {2025: 0.764, 2026: 0.758}
ADJ_EPS_Q = {'FY25': [0.78, 0.81, 0.80, 0.95], 'FY26': [0.93, 1.03, 0.85, 1.02]}  # 分割後(2024-12-12 効力の2:1分割)
NG_NI_FY26 = 662 + 732 + 684 + 853      # 四半期の non-GAAP 純利益の和
OCF_FY26, CAPEX_FY26, ADJ_FCF_FY26 = 4553, 440, 4414   # 調整後FCF 4,414(38.4%、会社定義。HQ capex 91 等を加算)
FCF_FY25 = 3469                          # 営業CF 3,716 − capex 247
GAAP_NI_FY26, GAAP_EPS_FY26 = 307, 0.40

# 四半期(百万ドル)。売上は FY 合計(検証済み)と整合する四半期値。NGS ARR・RPO は十億ドル。
Q = [  # quarter, end, revenue, ngs_arr, rpo
    ('FY24Q4', '2024-07-31', 2190, 4.22, 12.7),
    ('FY25Q1', '2024-10-31', 2139, 4.50, 12.6),
    ('FY25Q2', '2025-01-31', 2257, 4.80, 13.0),
    ('FY25Q3', '2025-04-30', 2289, 5.09, 13.5),
    ('FY25Q4', '2025-07-31', 2536, 5.58, 15.8),
    ('FY26Q1', '2025-10-31', 2474, 5.85, 15.5),
    ('FY26Q2', '2026-01-31', 2594, 6.30, 16.0),
    ('FY26Q3', '2026-04-30', 3002, 8.10, 18.4),
    ('FY26Q4', '2026-07-31', 3410, 9.10, 21.2),
]
# FY24 の NGS ARR(前年比から逆算した派生値。FY25Q1 +40%、Q2 +37%、Q3 +34%)
NGS_FY24_DERIVED = {'FY24Q1': 4.50 / 1.40, 'FY24Q2': 4.80 / 1.37, 'FY24Q3': 5.09 / 1.34}
REV_FY24Q = {'FY24Q1': 1878, 'FY24Q2': 1975, 'FY24Q3': 1985}
# 買収分(CyberArk 2026-02-11 完了、Chronosphere 2026-01-29 完了)
ACQ_REV = {'FY26Q3': 388, 'FY26Q4': 470}       # Q3 は会社開示、Q4 は推定(Q3 の約1.2倍: 完全四半期化+成長)
ACQ_ARR = {'FY26Q2': 0.16, 'FY26Q3': 1.60, 'FY26Q4': 2.05}  # Q3 は会社開示、Q2・Q4 は推定(Idira 約1.55+可観測性 約0.5)

# ガイダンス・コンセンサス
GUIDE_FY27 = dict(rev=(14100, 14200), ngs=(11.075, 11.175), eps=(4.16, 4.19), shares=(844, 847), opm=0.295, fcf_m=0.38)
CONS_EPS = {2027: 4.19, 2028: 4.88, 2029: 5.45}      # Yahoo 53名 / StockAnalysis / Chartmill(peer_peg_table.md)
CONS_REV = {2027: 14170, 2028: 16230, 2029: 17500}   # FY27 ガイダンス中央付近 / Yahoo 47名 / Chartmill 17.29・MLQ 17.7 の平均
CONS_EXT_EPS_G = {2030: 0.12, 2031: 0.11, 2032: 0.10, 2033: 0.09, 2034: 0.08, 2035: 0.07}  # 延長(FY29 の +11.7% から逓減)
CONS_EXT_REV_G = {2030: 0.11, 2031: 0.10, 2032: 0.09, 2033: 0.08, 2034: 0.07, 2035: 0.06}

FYS = list(range(2027, 2036))
FY_END = {y: dt.date(y, 7, 31) for y in range(2024, 2037)}


def lst(xs):
    return dict(zip(FYS, xs))


# ---------------------------------------------------------------- 2. 事業エンジン(原子単位: プラットフォーム化顧客)
# NGS ARR の FY26 末構成(推定): 有機 7.05 のうちプラットフォーム化顧客 65%(会社資料「>65%」)、残り非プラットフォーム化。
# 買収分: Idira(CyberArk)約 1.55、可観測性(Chronosphere)約 0.50(Q4 説明会「5億ドル超」)。
ORG_FY26 = 9.10 - 2.05
PLAT0 = 0.65 * ORG_FY26
NONPLAT0 = ORG_FY26 - PLAT0
IDIRA0, OBS0 = 1.55, 0.50
PLAT_COUNT_FY26 = 1880   # Q2 約1,550(会社資料)+Q3 約110(Zacks)+Q4 約220(説明会)。定義はトップ5,000顧客内の ELA または SASE ARR 100万ドル超
LEGACY_FY26 = None       # 下で較正
R_NGS = 0.985            # NGS 売上 ≈ 平均 NGS ARR × 0.985(無償期間・立ち上がりの遅れ)


def ngs_engine(nrr, newplat, uplift, pre_arr, g_np, g_idira, g_obs):
    """NGS ARR(十億ドル)を原子単位(プラットフォーム化顧客)から積み上げる。"""
    plat, nonplat, idira, obs, cnt = PLAT0, NONPLAT0, IDIRA0, OBS0, PLAT_COUNT_FY26
    out = {}
    for i, y in enumerate(FYS):
        n_new = newplat[i] / 1000.0  # 千件
        exp_plat = plat * (nrr[i] - 1)
        new_up = n_new * uplift          # 十億ドル(uplift は百万ドル/件 → 千件×百万=十億)
        migr = n_new * pre_arr
        np_growth = nonplat * g_np
        d_idira = idira * g_idira[i]
        d_obs = obs * g_obs[i]
        plat = plat * nrr[i] + n_new * (uplift + pre_arr)
        nonplat = nonplat + np_growth - migr
        idira += d_idira
        obs += d_obs
        cnt += newplat[i]
        total = plat + nonplat + idira + obs
        out[y] = dict(ngs=total, plat=plat, nonplat=nonplat, idira=idira, obs=obs, plat_count=cnt,
                      d_expansion=exp_plat, d_newplat=new_up, d_nonplat=np_growth, d_migration=-migr,
                      d_idira=d_idira, d_obs=d_obs)
    return out


# 四半期平均 NGS ARR から FY25・FY26 の平均と、レガシー(ハード・付随サブスク・保守・PS)の残差を較正
def q_avg(vals):
    return sum((a + b) / 2 for a, b in zip(vals[:-1], vals[1:])) / (len(vals) - 1)


NGS_AVG_FY25 = q_avg([4.22, 4.50, 4.80, 5.09, 5.58])
NGS_AVG_FY26 = q_avg([5.58, 5.85, 6.30, 8.10, 9.10])
LEGACY_FY25 = REV[2025] / 1000 - R_NGS * NGS_AVG_FY25
LEGACY_FY26 = REV[2026] / 1000 - R_NGS * NGS_AVG_FY26

# 照合テスト(±5%): 年次の残差は定義上一致するため、独立の検証は四半期への適用と FY27 ガイダンスへの適用で行う
recon = {}
recon['Q4FY25'] = (R_NGS * (5.09 + 5.58) / 2 / 4 + LEGACY_FY25 / 4) * 1000 / 2536 - 1
recon['Q4FY26'] = (R_NGS * (8.10 + 9.10) / 2 / 4 + LEGACY_FY26 / 4) * 1000 / 3410 - 1
recon['Q2FY26'] = (R_NGS * (5.85 + 6.30) / 2 / 4 + LEGACY_FY26 / 4) * 1000 / 2594 - 1
# FY27 ガイダンス: Q1 ガイダンス 9.55、以後 Q4 11.125 へ線形 → 平均 NGS、レガシーを −10% と置いた場合
ngs_q27 = [9.10, 9.55, 10.08, 10.60, 11.125]
recon['FY27guide_legacy-10%'] = (R_NGS * q_avg(ngs_q27) + LEGACY_FY26 * 0.90) * 1000 / 14150 - 1
implied_legacy_fy27 = 14.150 - R_NGS * q_avg(ngs_q27)
implied_legacy_g = implied_legacy_fy27 / LEGACY_FY26 - 1


# ---------------------------------------------------------------- 3. 経路の定義
PATHS = {
    'engine': dict(
        nrr=[1.19, 1.17, 1.16, 1.15, 1.14, 1.13, 1.12, 1.11, 1.10],
        newplat=[600, 560, 520, 480, 440, 400, 360, 330, 300], uplift=1.2, pre_arr=0.6, g_np=0.03,
        g_idira=[0.20, 0.19, 0.18, 0.16, 0.14, 0.12, 0.11, 0.10, 0.09],
        g_obs=[0.40, 0.32, 0.26, 0.22, 0.18, 0.15, 0.13, 0.11, 0.10],
        legacy_g=[-0.10, -0.06, -0.04, -0.03, -0.02, -0.02, -0.01, -0.01, -0.01],
        opm=[0.295, 0.305, 0.315, 0.325, 0.335, 0.340, 0.345, 0.350, 0.350],
        other0=350, other_step=50,
        sbc=[0.140, 0.133, 0.126, 0.119, 0.112, 0.105, 0.098, 0.092, 0.086],
        mna_dil=0.003, fcf_m=[0.38, 0.40, 0.405, 0.41, 0.415, 0.42, 0.42, 0.42, 0.42]),
    'company': dict(
        nrr=[1.20, 1.18, 1.16, 1.15, 1.14, 1.13, 1.12, 1.11, 1.10],
        newplat=[650, 620, 580, 550, 500, 460, 420, 380, 340], uplift=1.2, pre_arr=0.6, g_np=0.04,
        g_idira=[0.22, 0.21, 0.19, 0.17, 0.15, 0.13, 0.12, 0.11, 0.10],
        g_obs=[0.50, 0.38, 0.28, 0.22, 0.18, 0.15, 0.13, 0.11, 0.10],
        legacy_g=[-0.08, -0.05, -0.03, -0.02, -0.01, -0.01, 0.0, 0.0, 0.0],
        opm=[0.297, 0.315, 0.330, 0.345, 0.355, 0.365, 0.370, 0.375, 0.380],
        other0=350, other_step=60,
        sbc=[0.138, 0.128, 0.118, 0.108, 0.098, 0.090, 0.083, 0.077, 0.072],
        mna_dil=0.0, fcf_m=[0.38, 0.40, 0.41, 0.42, 0.43, 0.43, 0.43, 0.43, 0.43]),
    'bear': dict(
        nrr=[1.16, 1.14, 1.12, 1.11, 1.10, 1.10, 1.09, 1.09, 1.08],
        newplat=[450, 420, 400, 380, 350, 320, 300, 280, 260], uplift=1.1, pre_arr=0.6, g_np=0.0,
        g_idira=[0.15, 0.13, 0.11, 0.10, 0.09, 0.08, 0.08, 0.07, 0.07],
        g_obs=[0.25, 0.15, 0.12, 0.10, 0.09, 0.08, 0.07, 0.07, 0.06],
        legacy_g=[-0.12, -0.10, -0.08, -0.06, -0.05, -0.04, -0.03, -0.03, -0.03],
        opm=[0.290, 0.293, 0.296, 0.300, 0.305, 0.310, 0.315, 0.320, 0.320],
        other0=330, other_step=30,
        sbc=[0.145, 0.143, 0.141, 0.139, 0.137, 0.135, 0.133, 0.131, 0.129],
        mna_dil=0.007, fcf_m=[0.37, 0.375, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38]),
}
SBC_BASE = PATHS['engine']['sbc']


def shares_adj(y):
    """コンセンサスが前提にする株数(FY27 ガイダンス中央 845.5、以後 年1%)。調整後EPS⇔純利益の換算にのみ使う。"""
    return 845.5 * 1.01 ** (y - 2027)


def build_driver_path(p):
    eng = ngs_engine(p['nrr'], p['newplat'], p['uplift'], p['pre_arr'], p['g_np'], p['g_idira'], p['g_obs'])
    rows = {}
    prev_ngs, legacy = 9.10, LEGACY_FY26
    for i, y in enumerate(FYS):
        ngs = eng[y]['ngs']
        legacy = legacy * (1 + p['legacy_g'][i])
        if y == 2027:
            ngs_avg = q_avg([9.10, 9.10 + (ngs - 9.10) * 0.22, 9.10 + (ngs - 9.10) * 0.48,
                             9.10 + (ngs - 9.10) * 0.74, ngs])  # Q1 の季節性(ガイダンス 0.45/2.0)を反映
        else:
            ngs_avg = (prev_ngs + ngs) / 2
        rev = (R_NGS * ngs_avg + legacy) * 1000
        op = rev * p['opm'][i]
        other = p['other0'] + p['other_step'] * i
        adj_ni = (op + other) * (1 - TAX)
        sbc = rev * p['sbc'][i]
        biz_ni = adj_ni - sbc * (1 - TAX)
        denom = SH_DIL * (1 + p['mna_dil']) ** (y - 2026)
        rows[y] = dict(ngs=ngs, ngs_avg=ngs_avg, legacy=legacy * 1000, rev=rev, opm=p['opm'][i], op=op, other=other,
                       adj_ni=adj_ni, adj_eps=adj_ni / shares_adj(y), sbc_ratio=p['sbc'][i], sbc=sbc,
                       biz_ni=biz_ni, denom=denom, biz_eps=biz_ni / denom, fcf_m=p['fcf_m'][i],
                       fcf_minus_sbc=rev * (p['fcf_m'][i] - p['sbc'][i]), plat_count=eng[y]['plat_count'],
                       d=eng[y])
        prev_ngs = ngs
    return rows


def build_consensus_path():
    rows = {}
    eps, rev = dict(CONS_EPS), dict(CONS_REV)
    for y in FYS:
        if y not in eps:
            eps[y] = eps[y - 1] * (1 + CONS_EXT_EPS_G[y])
            rev[y] = rev[y - 1] * (1 + CONS_EXT_REV_G[y])
    for i, y in enumerate(FYS):
        adj_ni = eps[y] * shares_adj(y)
        sbc = rev[y] * SBC_BASE[i]
        biz = vl.business_eps_fixed_shares(eps[y], shares_adj(y), sbc, SH_DIL, TAX)
        rows[y] = dict(rev=rev[y], adj_eps=eps[y], adj_ni=adj_ni, sbc_ratio=SBC_BASE[i], sbc=sbc,
                       biz_ni=biz * SH_DIL, denom=SH_DIL, biz_eps=biz, is_ext=(y > 2029),
                       fcf_m=PATHS['engine']['fcf_m'][i], fcf_minus_sbc=rev[y] * (PATHS['engine']['fcf_m'][i] - SBC_BASE[i]))
    return rows


P = {'consensus': build_consensus_path()}
for k in ('company', 'engine', 'bear'):
    P[k] = build_driver_path(PATHS[k])


# ---------------------------------------------------------------- 4. 目標株価(規約どおり)と定常状態経由
PEG_BY_FY = {  # 年度別 PEG レンジ(x〜y)。経路ごとに置く
    'consensus': {2027: (1.5, 1.7), 2028: (1.4, 1.7), 2029: (1.4, 1.6), 2030: (1.3, 1.5), 2031: (1.2, 1.5), 2032: (1.2, 1.4)},
    'engine':    {2027: (1.5, 1.7), 2028: (1.4, 1.7), 2029: (1.4, 1.6), 2030: (1.3, 1.5), 2031: (1.2, 1.5), 2032: (1.2, 1.4)},
    'company':   {2027: (1.6, 1.8), 2028: (1.5, 1.8), 2029: (1.5, 1.7), 2030: (1.4, 1.6), 2031: (1.3, 1.6), 2032: (1.3, 1.5)},
    'bear':      {2027: (1.0, 1.3), 2028: (1.0, 1.3), 2029: (1.0, 1.2), 2030: (0.9, 1.2), 2031: (0.9, 1.1), 2032: (0.9, 1.1)},
}
EXIT_PEG = {'consensus': 1.5, 'engine': 1.5, 'company': 1.7, 'bear': 1.2}


def eps_map(path, key='biz_eps'):
    return {FY_END[y]: P[path][y][key] for y in FYS}


def ntm_at(path, d, key='biz_eps'):
    return vl.ntm_eps(eps_map(path, key), start=d)


TARGET = {}
for k in P:
    ntm0 = ntm_at(k, vl.TARGET_DATE)
    ntm3 = ntm_at(k, dt.date(2030, 10, 11))
    g = vl.cagr(ntm0, ntm3, 3)
    lo, hi = PEG_BY_FY[k][2028]
    mid = (lo + hi) / 2
    t_lo, t_hi, t_mid = vl.target_price(ntm0, lo, g), vl.target_price(ntm0, hi, g), vl.target_price(ntm0, mid, g)
    # 定常状態経由(FY+5 = FY31)
    e31, e34 = P[k][2031]['biz_eps'], P[k][2034]['biz_eps']
    g_exit = vl.cagr(e31, e34, 3)
    ss = vl.steady_state_target(e31, FY_END[2031], EXIT_PEG[k], g_exit)
    TARGET[k] = dict(ntm=ntm0, ntm3=ntm3, g=g, peg=(lo, hi), per_mid=t_mid['per'], target=t_mid['price'],
                     target_lo=t_lo['price'], target_hi=t_hi['price'], target_uncapped=t_mid['price_uncapped'],
                     ss_target=ss['target'], ss_per_exit=ss['per_exit'], ss_g_exit=g_exit, eps_fy31=e31,
                     adj_ntm=ntm_at(k, vl.TARGET_DATE, 'adj_eps'))
ADOPTED = 'engine'
PROB = {'bear': 0.30, 'consensus': 0.35, 'engine': 0.25, 'company': 0.10}
EV = vl.expected_value({k: TARGET[k]['target'] for k in PROB}, PROB, PRICE)
EV_SS = vl.expected_value({k: TARGET[k]['ss_target'] for k in PROB}, PROB, PRICE)

# ---------------------------------------------------------------- 5. 現在のマルチプル
ntm_now_biz = ntm_at('engine', vl.VALUATION_DATE)
ntm_now_biz_cons = ntm_at('consensus', vl.VALUATION_DATE)
ntm_now_adj = ntm_at('consensus', vl.VALUATION_DATE, 'adj_eps')
biz_g3_cons = vl.cagr(P['consensus'][2027]['biz_eps'], P['consensus'][2030]['biz_eps'], 3)
adj_g3_cons = vl.cagr(CONS_EPS[2027], P['consensus'][2030]['adj_eps'], 3)
adj_g_2y = vl.cagr(CONS_EPS[2027], CONS_EPS[2029], 2)
per_biz_ntm = PRICE / ntm_now_biz_cons
per_adj_ntm = PRICE / ntm_now_adj
peg_biz = per_biz_ntm / (biz_g3_cons * 100)
peg_adj = per_adj_ntm / (adj_g3_cons * 100)
rev_ntm = (P['consensus'][2027]['rev'] * 9.5 + P['consensus'][2028]['rev'] * 2.5) / 12  # 2026-10〜2027-09(FY27 9.5か月相当)
rev_ntm = (P['consensus'][2027]['rev'] * 10 + P['consensus'][2028]['rev'] * 2) / 12
fcf_ntm = (P['consensus'][2027]['rev'] * 0.38 * 10 + P['consensus'][2028]['rev'] * 0.40 * 2) / 12
ev_sales = EV_DIL * 1000 / rev_ntm
ev_fcf = EV_DIL * 1000 / fcf_ntm
fcf_margin_ttm = ADJ_FCF_FY26 / REV[2026]
sbc_ttm = SBC_REL[2026] / REV[2026]

# ---------------------------------------------------------------- 6. EPS 品質フォレンジック
adj_eps_fy25, adj_eps_fy26 = sum(ADJ_EPS_Q['FY25']), sum(ADJ_EPS_Q['FY26'])
sh_fy25 = 2400 / adj_eps_fy25   # FY25 の non-GAAP 純利益(約24億ドル、四半期の和の概算)÷EPS
sh_fy26 = NG_NI_FY26 / adj_eps_fy26
ni_fy25 = 2400
dec_2526 = vl.eps_log_decomposition(REV[2025], REV[2026], ni_fy25 / REV[2025], NG_NI_FY26 / REV[2026], sh_fy25, sh_fy26)
ni_fy27g = 4.175 * 845.5
dec_2627 = vl.eps_log_decomposition(REV[2026], 14150, NG_NI_FY26 / REV[2026], ni_fy27g / 14150, sh_fy26, 845.5)
biz_eps_fy26 = adj_eps_fy26 - SBC_REL[2026] * (1 - TAX) / sh_fy26
biz_eps_fy26_norm = adj_eps_fy26 - (SBC_REL[2026] - SBC_ACCEL_FY26) * (1 - TAX) / sh_fy26
biz_eps_fy25 = adj_eps_fy25 - SBC_REL[2025] * (1 - TAX) / sh_fy25
# FCF の3定義(§5-2)と 1株当たり
fcf1 = OCF_FY26 - CAPEX_FY26
fcf3 = fcf1 - SBC_REL[2026]
fcf3_fy25 = FCF_FY25 - SBC_REL[2025]
fcf3_ps = (fcf3 / sh_fy26, fcf3_fy25 / sh_fy25)
# CyberArk の反実仮想(FY27): CyberArk 売上 約17.5億ドル・営業利益率 20% と置き、株式 1.12億株・現金 23億ドル(利回り 4%)が無かった場合
cybr_rev, cybr_opm = 1750, 0.20
fy27_ex_cybr_rev = 14150 - cybr_rev
fy27_ex_cybr_op = 14150 * 0.295 - cybr_rev * cybr_opm
fy27_ex_cybr_other = (ni_fy27g / (1 - TAX) - 14150 * 0.295) + 2308 * 0.04
fy27_ex_cybr_eps = (fy27_ex_cybr_op + fy27_ex_cybr_other) * (1 - TAX) / (845.5 - 112 - 1.6)
cybr_eps_effect = 4.175 / fy27_ex_cybr_eps - 1

# ---------------------------------------------------------------- 7. 成長の値段・定常状態・リバースDCF・時間分布
# 定常状態利益(FY27 ランレート): non-GAAP 営業利益率 29.5% + 新規獲得 S&M(売上比 約11.6pt)+新製品 R&D(約4.8pt)、
# 定常状態の SBC は売上比 8%(成熟同業 CHKP 約9%・FTNT 約4% の間)、受取利息 3.5億ドル、税率 22%
SS_REV = P['engine'][2027]['rev']
SS_OPM_PRE_SBC = 0.295 + 0.116 + 0.048
SS_SBC = 0.08
ss_earn = (SS_REV * (SS_OPM_PRE_SBC - SS_SBC) + 350) * (1 - TAX)
split = vl.steady_state_split(ss_earn / 1000, MCAP_DIL)
ss_earn_alt = (SS_REV * (SS_OPM_PRE_SBC - 0.14) + 350) * (1 - TAX)   # SBC が現状の 14% のまま
split_alt = vl.steady_state_split(ss_earn_alt / 1000, MCAP_DIL)


def dcf_per_share(path, r=0.09, g_term=0.04, at=dt.date(2026, 10, 11)):
    """FCF−SBC(事業実態FCF)の DCF。FY27〜FY35 の後は永久成長。年央割引は簡略化し期末で割り引く。"""
    pv, pv3 = 0.0, 0.0
    for y in FYS:
        t = (FY_END[y] - at).days / 365.25
        cf = P[path][y]['fcf_minus_sbc']
        pv += cf / (1 + r) ** t
        if y <= 2029:
            pv3 += cf / (1 + r) ** t
    t_last = (FY_END[2035] - at).days / 365.25
    tv = P[path][2035]['fcf_minus_sbc'] * (1 + g_term) / (r - g_term)
    pv_tv = tv / (1 + r) ** t_last
    total = pv + pv_tv + NET_CASH
    return dict(per_share=total / SH_DIL, within3=pv3 / (pv + pv_tv), beyond3=1 - pv3 / (pv + pv_tv),
                pv_tv_share=pv_tv / (pv + pv_tv))


DCF = {k: dcf_per_share(k) for k in P}
DCF_R = {r: dcf_per_share('engine', r=r)['per_share'] for r in (0.08, 0.09, 0.10)}


def reverse_dcf(r=0.09, g_term=0.04, years=10, base=None):
    """現在株価を正当化する FCF−SBC の年成長率(10年一定、その後永久成長)を二分法で求める。"""
    base = base if base is not None else P['engine'][2027]['fcf_minus_sbc']
    target = PRICE * SH_DIL - NET_CASH

    def val(g):
        pv, cf = 0.0, base
        for i in range(years):
            t = (FY_END[2027 + i] - dt.date(2026, 10, 11)).days / 365.25
            pv += cf / (1 + r) ** t
            cf_last = cf
            cf *= 1 + g
        t_last = (FY_END[2027 + years - 1] - dt.date(2026, 10, 11)).days / 365.25
        return pv + cf_last * (1 + g_term) / (r - g_term) / (1 + r) ** t_last

    lo, hi = 0.0, 0.8
    for _ in range(100):
        mid = (lo + hi) / 2
        if val(mid) < target:
            lo = mid
        else:
            hi = mid
    return mid


REV_DCF = {r: reverse_dcf(r=r) for r in (0.08, 0.09, 0.10)}
REV_DCF_PREFCF = reverse_dcf(base=P['engine'][2027]['rev'] * 0.38)   # SBC を控除しない調整後FCF基準(最も寛容)

# ---------------------------------------------------------------- 8. 価値感度分析(芯の特定)
def engine_target_with(**override):
    p = json.loads(json.dumps(PATHS['engine']))
    for k, v in override.items():
        p[k] = v
    rows = build_driver_path(p)
    m = {FY_END[y]: rows[y]['biz_eps'] for y in FYS}
    n0 = vl.ntm_eps(m, start=vl.TARGET_DATE)
    n3 = vl.ntm_eps(m, start=dt.date(2030, 10, 11))
    g = vl.cagr(n0, n3, 3)
    tgt = vl.target_price(n0, 1.55, g)['price']
    e31, e34 = rows[2031]['biz_eps'], rows[2034]['biz_eps']
    ss = vl.steady_state_target(e31, FY_END[2031], 1.5, vl.cagr(e31, e34, 3))['target']
    return tgt, ss, rows[2030]['ngs']


base_t, base_ss, base_ngs30 = engine_target_with()
E = PATHS['engine']
SENS = []


def sens(name, lo_kw, hi_kw, lo_lab, hi_lab):
    lo = engine_target_with(**lo_kw)
    hi = engine_target_with(**hi_kw)
    SENS.append(dict(name=name, lo_label=lo_lab, hi_label=hi_lab, lo=lo[0], hi=hi[0], lo_ss=lo[1], hi_ss=hi[1],
                     swing=abs(hi[0] - lo[0]), swing_ss=abs(hi[1] - lo[1])))


sens('プラットフォーム化顧客のNRR(毎年±2pt)', dict(nrr=[x - 0.02 for x in E['nrr']]), dict(nrr=[x + 0.02 for x in E['nrr']]), '−2pt', '+2pt')
sens('新規プラットフォーム化件数(±25%)', dict(newplat=[x * 0.75 for x in E['newplat']]), dict(newplat=[x * 1.25 for x in E['newplat']]), '−25%', '+25%')
sens('SBC/売上の低下速度(FY31 14%〜8.4%)', dict(sbc=[0.14] * 9), dict(sbc=[0.135, 0.12, 0.108, 0.096, 0.084, 0.078, 0.072, 0.068, 0.065]), '14%据え置き', 'FY31 8.4%')
sens('non-GAAP営業利益率(FY31 ±3pt)', dict(opm=[0.295] + [x - 0.03 * min(1, i / 4) for i, x in enumerate(E['opm'][1:], 1)]),
     dict(opm=[0.295] + [x + 0.03 * min(1, i / 4) for i, x in enumerate(E['opm'][1:], 1)]), '−3pt', '+3pt')
sens('レガシー売上の減少率(毎年±3pt)', dict(legacy_g=[x - 0.03 for x in E['legacy_g']]), dict(legacy_g=[x + 0.03 for x in E['legacy_g']]), '−3pt/年', '+3pt/年')
sens('Idira(CyberArk)の成長率(±5pt)', dict(g_idira=[max(0, x - 0.05) for x in E['g_idira']]), dict(g_idira=[x + 0.05 for x in E['g_idira']]), '−5pt', '+5pt')
sens('有機の成長(NRR±2pt と新規件数±25% の同時)', dict(nrr=[x - 0.02 for x in E['nrr']], newplat=[x * 0.75 for x in E['newplat']]),
     dict(nrr=[x + 0.02 for x in E['nrr']], newplat=[x * 1.25 for x in E['newplat']]), '弱い側', '強い側')
sens('株式対価の買収による希薄化(年0〜1%)', dict(mna_dil=0.0), dict(mna_dil=0.01), '0%', '1%/年')
SENS.sort(key=lambda r: -r['swing'])
# PEG(CAP の代理)の感度は別に: 1.2〜1.9
PEG_SENS = {peg: vl.target_price(TARGET['engine']['ntm'], peg, TARGET['engine']['g'])['price'] for peg in (1.0, 1.2, 1.55, 1.9, 2.0)}

# F12: 経路×PEG の感応度と、芯2変数(SBC 経路×営業利益率)の格子
F12_PEG = {k: {peg: vl.target_price(TARGET[k]['ntm'], peg, TARGET[k]['g'])['price'] for peg in (1.0, 1.3, 1.55, 1.8, 2.0)} for k in TARGET}
SBC_CASES = {'14%据え置き': [0.14] * 9, '基準(FY31 11.2%)': E['sbc'],
             '加速(FY31 8.4%)': [0.135, 0.12, 0.108, 0.096, 0.084, 0.078, 0.072, 0.068, 0.065]}
OPM_CASES = {'−3pt': [0.295] + [x - 0.03 * min(1, i / 4) for i, x in enumerate(E['opm'][1:], 1)], '基準': E['opm'],
             '+3pt': [0.295] + [x + 0.03 * min(1, i / 4) for i, x in enumerate(E['opm'][1:], 1)]}
F12_GRID = {sk: {ok: engine_target_with(sbc=sv, opm=ov)[0] for ok, ov in OPM_CASES.items()} for sk, sv in SBC_CASES.items()}

# ---------------------------------------------------------------- 9. 機構台帳の大きさ(Δ目標株価、事業エンジン経路基準)
def d_target(**kw):
    return engine_target_with(**kw)[0] - base_t


MECH = {
    'M1_NRR120維持': d_target(nrr=[1.20] * 4 + E['nrr'][4:]),
    'M2_SBC低下加速': d_target(sbc=[0.138, 0.126, 0.114, 0.102, 0.090, 0.084, 0.078, 0.073, 0.069]),
    'M3_FCF40%と利益率+1.5pt': d_target(opm=[0.295, 0.315, 0.33, 0.34, 0.35, 0.355, 0.36, 0.365, 0.365]),
    'M4_Idiraクロスセル+5pt': d_target(g_idira=[x + 0.05 for x in E['g_idira']]),
    'M6_LLM顧客の一過性(FY27 −0.1B)': d_target(g_obs=[0.20] + E['g_obs'][1:]),
    'M7_レガシー減少加速': d_target(legacy_g=[x - 0.03 for x in E['legacy_g']]),
    'M8_SBC14%据え置き': d_target(sbc=[0.14] * 9),
    'M9_株式対価M&A 年1%': d_target(mna_dil=0.01),
    'M10_粗利率圧力(営業利益率−1.5pt)': d_target(opm=[x - 0.015 for x in E['opm']]),
    'M12_競争でNRR−2pt・新規−20%': d_target(nrr=[x - 0.02 for x in E['nrr']], newplat=[x * 0.8 for x in E['newplat']]),
}
# 金利感応度: 現金・投資 79億ドル × 100bp × (1−t)
rate_eps = CASH_INV * 0.01 * (1 - TAX) / SH_DIL

# ---------------------------------------------------------------- 10. 判断・エントリー
RATING = 'A'
ALPHA = 0.20   # A の上限(長期の CAP と 7件の買収統合の不確かさ)
B, U, L = TARGET[ADOPTED]['target'], TARGET['company']['target'], TARGET['bear']['target']
Z = vl.zones(B, U, L, ALPHA, PRICE, edge=True)
GAPS = {k: vl.gap(TARGET[k]['target'], PRICE) for k in ('consensus', 'company', 'engine')}
DEC = vl.decision(RATING, GAPS[ADOPTED], edge=False)
DEC_ALL = {k: vl.decision(RATING, GAPS[k], edge=False) for k in GAPS}

# ---------------------------------------------------------------- 11. 出力: CSV
def wcsv(name, header, rows):
    with open(f'{ROOT}/analysis/{T}_{name}.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


f13 = []
for k in ('consensus', 'company', 'engine', 'bear'):
    for y in range(2027, 2033):
        e0 = P[k][y]['biz_eps']
        g3 = vl.cagr(e0, P[k][y + 3]['biz_eps'], 3)
        lo, hi = PEG_BY_FY[k][y]
        gc = min(g3, vl.G_CAP)
        f13.append([FY_END[y].isoformat(), k, round(e0, 3), round(g3, 4), lo, hi, round(lo * gc * 100, 1), round(hi * gc * 100, 1),
                    round(lo * gc * 100 * e0, 1), round(hi * gc * 100 * e0, 1), int(y > 2029)])
wcsv('F13', ['fy_end', 'path', 'business_eps', 'g_3y', 'peg_low', 'peg_high', 'fair_per_low', 'fair_per_high',
             'fair_price_low', 'fair_price_high', 'is_extension'], f13)

# F18: 根幹KPIの加速度
f18 = []


def kpi_rows(name, series):
    """series: list of (period, value) 古い順。前年比は4期前、前期比年率は1期前。"""
    vals = dict(series)
    periods = [p for p, _ in series]
    prev_yoy = None
    out = []
    for i, (p, v) in enumerate(series):
        qoq = (v / series[i - 1][1]) ** 4 - 1 if i >= 1 and series[i - 1][1] else None
        yoy = v / series[i - 4][1] - 1 if i >= 4 else None
        sd = (yoy - prev_yoy) if (yoy is not None and prev_yoy is not None) else None
        if yoy is not None:
            prev_yoy = yoy
        out.append([name, p, round(v, 4), None if qoq is None else round(qoq, 4), None if yoy is None else round(yoy, 4),
                    None if sd is None else round(sd, 4)])
    return out


ngs_series = [('FY24Q1', NGS_FY24_DERIVED['FY24Q1']), ('FY24Q2', NGS_FY24_DERIVED['FY24Q2']), ('FY24Q3', NGS_FY24_DERIVED['FY24Q3'])] + \
             [(q[0], q[3]) for q in Q]
org_ngs = dict((q[0], q[3]) for q in Q)
for k, v in ACQ_ARR.items():
    org_ngs[k] = org_ngs[k] - v
org_series = [(p, org_ngs.get(p, v)) for p, v in ngs_series]
rev_series = [(k, REV_FY24Q[k]) for k in ('FY24Q1', 'FY24Q2', 'FY24Q3')] + [(q[0], q[2]) for q in Q]
org_rev_series = [(p, v - ACQ_REV.get(p, 0)) for p, v in rev_series]
rpo_series = [('FY24Q3', 11.3)] + [(q[0], q[4]) for q in Q]
# 純新規 NGS ARR(有機、十億ドル)。前年比のみ意味があるので qoq は空欄
nn_q = []
for i in range(1, len(org_series)):
    nn_q.append((org_series[i][0], org_series[i][1] - org_series[i - 1][1]))
# 純新規は季節性が大きいので直近4四半期の合計(TTM)で見る
nn = [(nn_q[i][0], sum(v for _, v in nn_q[i - 3:i + 1])) for i in range(3, len(nn_q))]
f18 += kpi_rows('有機NGS ARR(買収除く・十億ドル)', org_series)
f18 += kpi_rows('報告NGS ARR(十億ドル)', ngs_series)
f18 += kpi_rows('有機売上(百万ドル)', org_rev_series)
f18 += kpi_rows('RPO(十億ドル)', rpo_series)
f18 += kpi_rows('有機の純新規NGS ARR(直近4四半期合計・十億ドル)', nn)
for r in f18:
    if r[0].startswith('有機の純新規'):
        r[3] = None   # TTM 合計の前期比年率は意味が薄いので空欄
wcsv('F18', ['kpi', 'period', 'value', 'qoq_annualized', 'ttm_yoy', 'second_diff'], [r for r in f18])

# F10: 収益ラインの時系列(百万ドル)
f10 = [
    ['FY25', '製品(ファイアウォール機器・ライセンス)', 1802, 0], ['FY25', 'サブスクリプション・保守', 7419, 0],
    ['FY26', '製品(ファイアウォール機器・ライセンス)', 2280, 0], ['FY26', 'サブスクリプション・保守', 9200, 0],
]
# 推定の内訳(NGS 由来売上 / レガシー / 買収)
f10b = [
    ['FY25', 'NGS由来(有機・推定)', round(R_NGS * NGS_AVG_FY25 * 1000), 0],
    ['FY25', 'レガシー(機器・付随サブスク・保守・推定)', round(LEGACY_FY25 * 1000), 0],
    ['FY26', 'NGS由来(有機・推定)', round(R_NGS * NGS_AVG_FY26 * 1000 - 858), 0],
    ['FY26', 'レガシー(機器・付随サブスク・保守・推定)', round(LEGACY_FY26 * 1000), 0],
    ['FY26', '買収(CyberArk・Chronosphere)', 858, 0],
]
e27 = P['engine'][2027]
e28 = P['engine'][2028]
acq27 = (e27['d']['idira'] + e27['d']['obs'] + IDIRA0 + OBS0) / 2 * R_NGS * 1000
acq28 = (e28['d']['idira'] + e28['d']['obs'] + e27['d']['idira'] + e27['d']['obs']) / 2 * R_NGS * 1000
f10b += [
    ['FY27E', 'NGS由来(有機・推定)', round(e27['rev'] - e27['legacy'] - acq27), 1],
    ['FY27E', 'レガシー(機器・付随サブスク・保守・推定)', round(e27['legacy']), 1],
    ['FY27E', '買収(CyberArk・Chronosphere)', round(acq27), 1],
    ['FY28E', 'NGS由来(有機・推定)', round(e28['rev'] - e28['legacy'] - acq28), 1],
    ['FY28E', 'レガシー(機器・付随サブスク・保守・推定)', round(e28['legacy']), 1],
    ['FY28E', '買収(CyberArk・Chronosphere)', round(acq28), 1],
]
order = ['NGS由来(有機・推定)', 'レガシー(機器・付随サブスク・保守・推定)', '買収(CyberArk・Chronosphere)']
f10b.sort(key=lambda r: (r[0], order.index(r[1])))
wcsv('F10', ['period', 'line', 'revenue_usd_mn', 'is_forecast'], f10b)
wcsv('F10b', ['period', 'line', 'revenue_usd_mn', 'is_forecast'], f10)

# ---------------------------------------------------------------- 12. 要約 JSON
summary = {
    'ticker': T, 'company': 'Palo Alto Networks', 'price': PRICE, 'price_date': PRICE_DATE,
    'market_cap_usd_bn': round(MCAP_BASIC, 1), 'diluted_shares_mn': SH_DIL, 'fy_end_month': 7,
    'net_cash_usd_bn': round(NET_CASH / 1000, 2),
    'structure_rating': RATING,
    'condition_ratings': {'1': 'A', '2': 'A', '3': 'A', '4': 'S', '5': 'A', '6': 'D', '7': 'D', '8': 'A', '9': 'B',
                          '10': 'B', '11': 'A', '12': 'A', '13': 'A'},
    'condition9_applicable': True,
    'rules_fired': ['致命条件の拒否権: 非発動(E以下なし)', 'C×4上限: 非発動(C評価0件)',
                    '条件6-7の対評価: 発動(PEGが高い理由は市場の楽観であり、安い理由の検証は成立しない。両条件ともD)',
                    'エッジなし(買い方向)のため買いは不可: 該当(乖離が負のため結果に影響なし)'],
    'archetype': 'ORCL型寄り(継続課金・プラットフォーム)+一部VRT型(機器の更新サイクル)',
    'business_model_types': ['A(NGS: SASE・SecOps・クラウド・Idira)', 'G(ファイアウォール機器)', 'B(可観測性・XSIAMのデータ量連動)'],
    'core_variables': [
        {'name': 'non-GAAP営業利益率の拡大ペース(FY28 調整後FCFマージン40%目標の確度)',
         'market_implied': '株価はFCF−SBCの10年間 年{:.1%}成長を要し、売上成長に加えて大幅な利益率拡大を暗に置く'.format(REV_DCF[0.09]),
         'our_estimate': '29.5%(FY27ガイダンス)→33.5%(FY31)、年+1pt。実績はFY25→FY27で年+0.35pt',
         'advantage_type': '分析(粗利率低下・クラウド原価・買収事業の利益率を分解)'},
        {'name': 'SBC/売上の低下経路',
         'market_implied': '調整後EPS(SBC除外)ベースでPER約{:.0f}倍。SBCを費用として織り込んでいない'.format(per_adj_ntm),
         'our_estimate': '14.0%(FY27)→11.2%(FY31)。実績はFY23 16.6%→FY26 14.9%(加速償却除き13.4%)',
         'advantage_type': '分析'},
        {'name': '競争優位期間(CAP)と高成長の持続年数',
         'market_implied': '10年超の20%台後半の1株当たり成長(リバースDCF)',
         'our_estimate': 'CAPは約12年あるが、事業実態EPS成長はFY27→FY30の年約24%からFY32以降13%前後へ逓減',
         'advantage_type': '分析(参照クラス)。予測可能性は低く確率で扱う'},
        {'name': '有機の成長(プラットフォーム化顧客のNRRと新規件数)',
         'market_implied': '報告NGS ARR +63%・純新規ほぼ倍増を成長の物差しにする',
         'our_estimate': '有機の純新規NGS ARR(直近4四半期)は14.7億ドルで前年比+8%(推定)。有機売上はFY26 +15%、FY27 +12〜13%',
         'advantage_type': '分析(有機・買収の分解)'},
    ],
    'edge': {'exists': True,
             'statement': '市場は報告NGS ARR+63%とAI需要を物差しに、調整後PER約{:.0f}倍(事業実態PER約{:.0f}倍)を払い、FCF−SBCの10年間年{:.0%}成長を織り込む。構造上は有機売上+12〜16%、営業利益率は年+0.4pt、SBC/売上は14〜15%で、FY27の調整後EPSは株数増で+9%にとどまる。FY27の有機売上・SBC/売上とFY28の調整後FCFマージン40%で確認でき、差が解消したときの1株当たり価値は約{:.0f}ドル(規約)、DCF交差確認で約{:.0f}ドル'.format(per_adj_ntm, per_biz_ntm, REV_DCF[0.09], B, DCF['engine']['per_share']),
             'advantage_type': '分析(有機・買収の分解、総額と1株当たりの分解、リバースDCF)',
             'kpi': '有機売上成長率・有機の純新規NGS ARR・SBC/売上・調整後FCFマージン',
             'threshold': '有機売上+18%以上が2四半期続けば差分は縮小(市場側が正しい)。+13%未満なら拡大',
             'timing': 'FY27 Q2〜Q4(2027-02〜2027-08)',
             'value_per_share_if_resolved': round(B, 1)},
    'eps_definition': '事業実態EPS = 調整後EPS − 株式報酬関連費用(給与税込み)×(1−22%)÷現在の希薄化後株数840百万株(§3-1)。買収無形償却は除外したまま',
    'base_business_eps': {'fy': 'FY26(2026-07期)', 'value': round(biz_eps_fy26_norm, 2)},
    'eps_paths': {k: {f'FY{y % 100}': round(P[k][y]['biz_eps'], 2) for y in range(2027, 2033)} for k in ('consensus', 'company', 'engine', 'bear')},
    'adj_eps_consensus': {f'FY{y % 100}': round(P['consensus'][y]['adj_eps'], 2) for y in range(2027, 2033)},
    'sbc_to_revenue_path': {f'FY{y % 100}': SBC_BASE[i] for i, y in enumerate(FYS[:6])},
    'allowed_peg': {'path_a': [3.4, 9.9], 'path_b': [1.0, 1.5], 'path_c': [1.4, 1.7], 'adopted': [1.4, 1.7],
                    'note': '経路aは市場が業界全体に付ける倍率(中央値約6.1)で許容値の根拠にしない。経路b(事業実態EPS成長約21%、慣行1〜1.5)と経路c(構造評価A=1.3〜1.6、CAP約12年とストック比率80%で+0.1、SBC・希薄化と負の非対称性で±0)の収束で1.4〜1.7(FY28基準)を採用'},
    'targets_12m': {k: round(TARGET[k]['target'], 1) for k in ('consensus', 'company', 'engine', 'bear')},
    'targets_note': '規約どおり(NTM事業実態EPS×PEG×g): ' + ', '.join(f"{k} {TARGET[k]['target']:.1f}" for k in TARGET) +
                    ' / 定常状態経由(FY31×出口PER、9%割引): ' + ', '.join(f"{k} {TARGET[k]['ss_target']:.1f}" for k in TARGET) +
                    '。FY27の事業実態EPSが調整後EPSの約57%残り近い年度のPEGが安定するため、規約どおりの値を採用',
    'adopted_path': ADOPTED, 'gaps': {k: round(v, 3) for k, v in GAPS.items()},
    'probabilities': PROB, 'expected_price': round(EV['expected_price'], 1), 'expected_return': round(EV['expected_return'], 3),
    'asymmetry': {'downside_pct': round(vl.gap(L, PRICE), 3), 'upside_pct': round(vl.gap(U, PRICE), 3),
                  'ratio': round(vl.gap(U, PRICE) / vl.gap(L, PRICE), 2), 'convex': False},
    'decision': DEC,
    'entry_zones': {'alpha': ALPHA, 'Z1': round(Z['Z1'], 1), 'Z2': round(Z['Z2'], 1), 'zone': Z['zone']},
    'steady_state': {'steady_earnings_usd_mn': round(ss_earn), 'steady_state_value_usd_bn': round(split['steady_state_value'], 1),
                     'growth_price_usd_bn': round(split['growth_price'], 1), 'growth_share': round(split['growth_share_of_mcap'], 3)},
    'value_time_split': {'within_3y': round(DCF['engine']['within3'], 3), 'beyond_3y': round(DCF['engine']['beyond3'], 3)},
    'cap_years': 12, 'incremental_roic': '有機の成長は前受金(繰延収益148億ドル)で賄われ増分ROICは非常に高い(拘束資本が負)。買収(約260億ドル)の増分ROICはFY27で約1〜2%、FY31でも約4%と資本コスト9%を下回る',
    'current_multiples': {'per_business_ntm': round(per_biz_ntm, 1), 'per_adj_ntm': round(per_adj_ntm, 1),
                          'peg_business_3y': round(peg_biz, 2), 'peg_adj_3y': round(peg_adj, 2),
                          'ev_sales_ntm': round(ev_sales, 1), 'ev_fcf_ntm': round(ev_fcf, 1),
                          'fcf_margin_ttm': round(fcf_margin_ttm, 3), 'sbc_to_revenue_ttm': round(sbc_ttm, 3)},
    'growth': {'revenue_yoy_latest_q': 0.34, 'arr_or_proxy_yoy': round(org_ngs['FY26Q4'] / org_ngs['FY25Q4'] - 1, 3),
               'arr_proxy_name': 'NGS ARR(有機・買収除く推定。報告値は+63%)',
               'nnarr_or_proxy_yoy': round(nn[-1][1] / nn[-5][1] - 1, 3),   # 有機の純新規 NGS ARR(直近4四半期合計)の前年比(推定) 'eps_cagr_3y_consensus': round(vl.cagr(adj_eps_fy26, CONS_EPS[2029], 3), 3),
               'eps_cagr_5y_engine': round(vl.cagr(biz_eps_fy26_norm, P['engine'][2031]['biz_eps'], 5), 3)},
    'rule_of_40': round(0.235 + 0.38, 3),
    'triggers': {
        'upgrade': ['株価が Z2 以下(約{:.0f}ドル)へ下落'.format(Z['Z2']), '有機売上成長+18%以上が2四半期連続かつSBC/売上12%以下',
                    'FY28 調整後FCFマージン40%の達成と FCF−SBC/株の+20%超'],
        'downgrade': ['有機の純新規NGS ARRが2四半期連続で前年割れ(LLM移行の一過性を除く)', 'プラットフォーム化顧客のNRRが115%未満',
                      '株式対価の大型買収(株数+3%超)'],
        'exit': ['保有時: 有機売上成長+10%未満、またはPAN-OSの重大脆弱性に起因する大口解約の開示']},
    'one_line': '事業はプラットフォーム化で継続課金80%・FCFマージン38%の優良構造(構造評価A)だが、株価は有機売上成長12〜16%に対し10年超の高成長を織り込み、規約上の12か月目標は{:.0f}〜{:.0f}ドル。監視とし、{:.0f}ドル以下で分割エントリーを検討'.format(L, U, Z['Z2']),
    'data_corrections': 6, 'known_constraints': 15,
}

if __name__ == '__main__':
    print('== 入力')
    print(f'時価総額 基本 {MCAP_BASIC:.1f}B / 希薄化 {MCAP_DIL:.1f}B / ネットキャッシュ {NET_CASH:.0f}M / EV {EV_DIL:.1f}B')
    print(f'NGS 平均 FY25 {NGS_AVG_FY25:.3f} FY26 {NGS_AVG_FY26:.3f} / レガシー FY25 {LEGACY_FY25:.3f} FY26 {LEGACY_FY26:.3f} (+{LEGACY_FY26/LEGACY_FY25-1:.1%})')
    print('照合:', {k: f'{v:+.1%}' for k, v in recon.items()}, f'FY27ガイダンス含意のレガシー {implied_legacy_fy27:.2f}B ({implied_legacy_g:+.1%})')
    print('== 経路')
    for k in ('consensus', 'company', 'engine', 'bear'):
        print(k)
        for y in FYS:
            r = P[k][y]
            extra = f" NGS {r['ngs']:.2f} 平均 {r.get('ngs_avg', 0):.2f} レガシー {r.get('legacy', 0):.0f} 件数 {r.get('plat_count', 0):.0f} opm {r.get('opm', 0):.3f}" if k != 'consensus' else ''
            print(f"  FY{y}: 売上 {r['rev']:.0f} 調整後EPS {r['adj_eps']:.2f} SBC比 {r['sbc_ratio']:.3f} 事業実態EPS {r['biz_eps']:.2f}{extra}")
    print('== 目標株価')
    for k, t in TARGET.items():
        print(f"{k}: NTM {t['ntm']:.3f} NTM+3 {t['ntm3']:.3f} g {t['g']:.3%} PEG {t['peg']} PER {t['per_mid']:.1f} 目標 {t['target']:.1f} ({t['target_lo']:.1f}〜{t['target_hi']:.1f}) "
              f"乖離 {vl.gap(t['target'], PRICE):+.1%} / 定常状態経由 {t['ss_target']:.1f} (出口PER {t['ss_per_exit']:.1f}, g_exit {t['ss_g_exit']:.1%}, FY31 EPS {t['eps_fy31']:.2f}) / 調整後NTM {t['adj_ntm']:.2f}")
    print('期待値', EV, '定常状態経由の期待値', EV_SS)
    print('判断', DEC, DEC_ALL, 'ゾーン', Z)
    print('== マルチプル')
    print(f'NTM事業実態EPS(コンセンサス) {ntm_now_biz_cons:.3f} (エンジン {ntm_now_biz:.3f}) PER {per_biz_ntm:.1f} / NTM調整後 {ntm_now_adj:.3f} PER {per_adj_ntm:.1f}')
    print(f'事業実態EPS 3年CAGR(コンセ) {biz_g3_cons:.3%} PEG {peg_biz:.2f} / 調整後 3年CAGR {adj_g3_cons:.3%} PEG {peg_adj:.2f} / 調整後2年 {adj_g_2y:.3%}')
    print(f'EV/売上 NTM {ev_sales:.1f} EV/FCF NTM {ev_fcf:.1f} 売上NTM {rev_ntm:.0f} FCF NTM {fcf_ntm:.0f}')
    print('== フォレンジック')
    print(f'調整後EPS FY25 {adj_eps_fy25:.2f} FY26 {adj_eps_fy26:.2f} 株数 FY25 {sh_fy25:.0f} FY26 {sh_fy26:.0f}')
    print('分解 FY25→26', {k: round(v, 3) for k, v in dec_2526.items()}, ' FY26→27(ガイダンス)', {k: round(v, 3) for k, v in dec_2627.items()})
    print(f'事業実態EPS FY25 {biz_eps_fy25:.2f} FY26 {biz_eps_fy26:.2f} 正規化 {biz_eps_fy26_norm:.2f}')
    print(f'FCF① {fcf1} ③(−SBC) {fcf3} FY25③ {fcf3_fy25} 1株 {fcf3_ps[0]:.2f} vs {fcf3_ps[1]:.2f} ({fcf3_ps[0]/fcf3_ps[1]-1:+.1%}) 総額 {fcf3/fcf3_fy25-1:+.1%}')
    print(f'CyberArk 反実仮想 FY27 EPS(CyberArk無し){fy27_ex_cybr_eps:.2f} vs 4.175 → 効果 {cybr_eps_effect:+.1%}')
    print('== 成長の値段')
    print(f'定常状態利益 {ss_earn:.0f}M 価値 {split["steady_state_value"]:.1f}B 成長の値段 {split["growth_price"]:.1f}B ({split["growth_share_of_mcap"]:.1%}) / SBC14%版 {ss_earn_alt:.0f}M {split_alt["steady_state_value"]:.1f}B ({split_alt["growth_share_of_mcap"]:.1%})')
    print('DCF(FCF−SBC)', {k: (round(v['per_share'], 1), round(v['within3'], 3), round(v['pv_tv_share'], 3)) for k, v in DCF.items()}, '資本コスト感応', {r: round(v, 1) for r, v in DCF_R.items()})
    print('リバースDCF(FCF−SBC 10年成長率)', {r: f'{v:.1%}' for r, v in REV_DCF.items()}, ' 調整後FCF基準', f'{REV_DCF_PREFCF:.1%}')
    print('== 感度(芯)')
    print(f'基準 目標 {base_t:.1f} 定常 {base_ss:.1f} FY30 NGS {base_ngs30:.2f}')
    for s in SENS:
        print(f"  {s['name']}: {s['lo_label']} {s['lo']:.1f} / {s['hi_label']} {s['hi']:.1f}  振れ {s['swing']:.1f} (定常 {s['lo_ss']:.1f}〜{s['hi_ss']:.1f} 振れ {s['swing_ss']:.1f})")
    print('PEG感度', {k: round(v, 1) for k, v in PEG_SENS.items()})
    print('F12 経路×PEG', {k: {p: round(v, 1) for p, v in d.items()} for k, d in F12_PEG.items()})
    print('F12 SBC×営業利益率', {k: {o: round(v, 1) for o, v in d.items()} for k, d in F12_GRID.items()})
    print('== 機構 Δ目標', {k: round(v, 1) for k, v in MECH.items()}, f'金利100bp EPS {rate_eps:.3f}')
    print('== エンジン内訳 FY27')
    print({k: round(v, 3) for k, v in P['engine'][2027]['d'].items()})
    print({k: round(v, 3) for k, v in P['engine'][2030]['d'].items()})
    with open(f'{ROOT}/analysis/{T}_summary.json', 'w') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print('summary.json 書き出し')
