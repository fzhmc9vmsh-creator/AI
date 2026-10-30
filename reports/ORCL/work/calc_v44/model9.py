# -*- coding: utf-8 -*-
"""
第4.4版(2026-10-30、Investor Day 2026-10-28 の会社資料を反映)。変更点は prereg2.md §9。
Oracle (ORCL) 本源的価値モデル 第3版・検証反映(2026-10-12、R3-4)。変更点は prereg2.md §9
- 前提は prereg2.md(事前登録 第2版)。株価・予想PERは入力に使わない。株価との比較は compare() のみ。
- AI インフラはコホート(世代)経済性(ai_cohort.py)。経済的耐用年数は内生、需給の逼迫が解けた後は単価がフェード。
- 割引率は年度ごとの金利(期間構造)+ ERP × 資産ベータ。明示期間 FY27〜FY45(AI は FY60 まで + 定常の永続価値)。
- リスクを数える場所: 資本集約度 = capex と更新投資 / 倒産 = 確率加重 / 顧客集中 = 弱気シナリオ / 希薄化 = SBC を費用・株数固定。
単位: 10億ドル、株数 10億株。会計年度は5月末。評価基準日 2026-08-31。FY27 は残り 0.75 年分を数える。
"""
import json, math, os, copy
from ai_cohort5 import run_ai, cohort_life, crf, lease_mkt, lease_or

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)
Y0, YN = 27, 45                      # 非 AI 事業の明示期間
YAI = 90                             # AI の明示期間(検証: 永続価値の窓の影響を消すため FY90 まで)
STUB = 0.75

BOND_MV = 0.92                       # 社債の時価/簿価(検証: 市場金利で負債を時価評価)
BS = dict(debt=125.3, fin_lease=9.2, cash=37.1, pref=5.0, prepay=11.4, shares=3.05, min_cash=30.0,
          dps=2.00, pref_div=0.325, lease_liab=34.6, lease_unc_pv=177.0, lease_exp0=5.5, lease_exp_unc=16.9, lev_floor=2.0)
FY26 = dict(sw=24.5, saas=15.9, ocin=10.4, mc=0.5, hw=3.1, svc=5.7)
Q1 = dict(rev_sw=5.55, rev_saas=4.2, rev_ocin=3.1, rev_mc=0.2, rev_ai=4.1, rev_hw=0.774, rev_svc=1.414, ebit_adj=6.728 + 0.202 + 0.094)
PD = {'BBB+': 0.0015, 'BBB': 0.0027, 'BBB-': 0.0055, 'BB+': 0.0090, 'BB': 0.012, 'B': 0.033}

# ---------------------------------------------------------------- 金利(検証反映: 市場の利回り曲線。予測の低下はシナリオ)
ERP = 0.0423                          # Damodaran のインプライド ERP(2026-08)。同時点の金利と組にする


def rf_path(kind='market'):
    if kind == 'market':      # 現在の曲線(2年 4.85、5年 4.99、10年 5.1〜5.3、20年 5.66、30年 5.44)から近似したフォワード
        # 第4.4版: 10年金利 5.02%(2026-10-29)。第4.3版の曲線から一律 −0.10pt
        return lambda y: 0.049 if y <= 28 else (0.0515 if y <= 31 else (0.053 if y <= 36 else 0.055))
    if kind == 'normalize':   # 予測どおり低下(第3版の当初のベース): 5.2 → 4.8 → 4.5 → 4.3 → 4.2
        d = {27: 0.052, 28: 0.048, 29: 0.045, 30: 0.043}
        return lambda y: d.get(y, 0.042)
    if kind == 'high':
        return lambda y: 0.060
    raise ValueError(kind)


def disc_factors(r_of_year, years):
    """評価基準日(FY27 の Q1 末)からの割引係数。年央の現金に対して。FY27 は残り 0.75 年の中央"""
    df = {}
    acc = 1.0
    for y in years:
        r = r_of_year(y)
        if y == Y0:
            df[y] = 1 / (1 + r) ** (STUB / 2)
            acc = 1 / (1 + r) ** STUB
        else:
            df[y] = acc / (1 + r) ** 0.5
            acc = acc / (1 + r)
        df[('end', y)] = acc
    return df


# ---------------------------------------------------------------- ベースの前提(prereg2)
def gen_price_factory(P27, P28, P29, g):
    return lambda y: {27: P27, 28: P28, 29: P29}.get(y, P29 * (1 + g) ** max(0, y - 29)) if y >= 27 else P27


def gen_capex_factory(K27, K28, K29, g):
    return lambda y: {27: K27, 28: K28, 29: K29}.get(y, K29 * (1 + g) ** max(0, y - 29)) if y >= 27 else K27


# 第4.4版: 会社の 1GW 例(CFO 資料 p.15〜20)。自己資金: 年換算売上 16・capex 37・粗利率 35%。BYOH: 売上 11・capex 6・粗利率 35% 超。
# 新しい容量の 20% を BYOH とみなす(資金の橋渡し p.26: 約 6GW のうち BYOH で 350〜400 億ドル減 ≈ 1.2GW)。混合: 売上 15.0・capex 30.8。
# 粗利率 35% に合う現金費用(自己資金 4.23、BYOH は粗利率 40% で 5.6)と、エンジンの賃料・電力 2.7 の差を追加費用 X とする。
CO_SHARE_BYOH = 0.20
CO_REV = (1 - CO_SHARE_BYOH) * 16.0 + CO_SHARE_BYOH * 11.0                 # 満稼働の年換算売上 /GW
CO_K = (1 - CO_SHARE_BYOH) * 37.0 + CO_SHARE_BYOH * 6.0                    # 2年の capex /GW
_cash_self = 16.0 * 0.65 - 37.0 / 6
_cash_byoh = 11.0 * 0.60 - 6.0 / 6
CO_X = (1 - CO_SHARE_BYOH) * _cash_self + CO_SHARE_BYOH * _cash_byoh - 2.7   # 追加の現金費用 /GW(FY27 価格)
CO_P = CO_REV / 0.975                                                     # 契約単価(稼働率 97.5% で年換算売上)


def gen_price_v44(g):
    return lambda y: CO_P * (1 + g) ** max(0, y - 28)


def gen_capex_v44(g):
    return lambda y: CO_K * (1 + g) ** max(0, y - 28)


AI_BASE = dict(tax=0.17, util_c=0.975, util_post_tight=0.95, util_post_loose=0.85, contract_len=5, L_max=10, acct_life=6,
               cash_esc=0.025, C0=2.7, L0=1.6, O0=1.1, e_lease=0.025, rent_g_tight=0.06, rent_g_loose=0.03,
               lag=0.30, startup=0.3,
               initial=[(25, 0.5, 10.0, 24.0), (26, 1.2, 10.0, 24.0)],
               # 第4.4版: 会社の容量計画(総容量 FY26 約 3GW → FY28 末 約 10GW、FY30 約 10GW)から AI 以外の約 1.3GW を除く。
               # FY31 以降は自己資金での成長(会社は数値なし)。第4.3版の後半と同じ年 +2.5・+2.0GW(FY31 12.0、FY32 14.0)、以後 g_cap
               gw_plan={27: 4.7, 28: 8.7, 29: 9.0, 30: 9.5, 31: 12.0, 32: 14.0},
               sites_committed={27: 4.7, 28: 8.7, 29: 9.0, 30: 9.5, 31: 12.0, 32: 14.0},
               g_cap=lambda y: 0.08 if y <= 35 else (0.04 if y <= 40 else 0.02),
               gen_price=gen_price_v44(0.03), gen_capex=gen_capex_v44(0.03),
               gen_xcost=lambda v: CO_X * 1.025 ** (v - 27) if v >= 27 else 0.0,
               sign_lag=2, Y_star=32, trough_years=0, trough_mult=1.0, s_eq=0.0, F=2,
               rho_ref=0.60, dec_ref=0.15, util_ref=0.85,
               post_rho_tight=1.00, post_dec_tight=0.03, post_rho_loose=0.60, post_dec_loose=0.15,
               lease_per_gw=1.65, lease_end=47, sublease=0.4, s_eq_years=None, s_eq_after=0.0)

BASE = dict(
    name='ベース', prob=0.50, rf='market', sp_c_year=None,
    beta=dict(sw=0.80, saas=0.95, ocin=1.00, mc=1.00, anc=1.00, ai=1.10, hw=1.00, svc=1.00),
    rd=0.072, tax=0.17,
    # 第4版: SaaS は加速を織り込む(根拠: 繰延収益 +16% > 売上 +10%、Fusion ERP +17%・NetSuite +14% が全体より速い、
    # エージェント型 AI のソフト支出 2030 年 $985B(Gartner)、SAP クラウド ERP +25%。反証: エージェントは追加料金なし、席数の圧縮)
    g_sw=-0.03, g_saas=[0.10, 0.12, 0.13, 0.14, 0.14, 0.13, 0.12, 0.10, 0.09, 0.08] + [0.06] * 5 + [0.04] * 4,
    g_ocin=[0.22, 0.20, 0.18, 0.15, 0.13, 0.11, 0.09, 0.08, 0.07, 0.06] + [0.04] * 9,
    g_hw=0.02, g_svc=0.03,
    m_saas=(0.26, 0.32, 5), m_ocin=(0.30, 0.38, 5), m_mc=(0.40, 0.45, 4), m_hw=0.08, m_svc=0.03,
    s2c=dict(saas=3.0, ocin=1.0, mc=1.5, anc=1.0, hw=5.0, svc=5.0),
    da=dict(sw=0.02, saas=0.03, ocin=0.10, mc=0.08, anc=0.10, hw=0.02, svc=0.02),
    term=dict(sw=(-0.02, None), saas=(0.03, 0.40), ocin=(0.03, 0.25), mc=(0.03, 0.30), anc=(0.03, 0.25), hw=(0.01, 0.20), svc=(0.01, 0.20)),
    anc_a=0.05,
    mc_mig=0.70, g_sw_base=-0.02,
    mc_D0=11.0, mc_h=0.50, mc_A=0.40, mc_m=2.5, mc_u=0.06, mc_u_late=0.03, mc_run0=0.8,
    mc_shape=[0.09, 0.14, 0.19, 0.24, 0.28, 0.31, 0.33, 0.34, 0.35, 0.35], mc_loss_margin=0.70,
    ai=AI_BASE, ai_tv_g=0.02,
    cust_fund={27: 0.24, 28: 0.17}, cust_fund_tight=0.10, cust_fund_loose=0.05,   # 第4.4版: FY28 は資金の橋渡し(p.26)の前払い 約 17%、以後 10%
    eq_raise=(28, 10.0, 139.56), bb_start=31,          # 第4.4版: 追加調達のうち株式 100 億ドル(FY28 に株価 139.56 で発行と仮定)
    rate_debt=[0.045, 0.048, 0.050, 0.051, 0.052] + [0.053] * 14,
    cash_yield=0.035, shield_term_haircut=0.5, sw_margin=0.70,
)


def openai_mod(share, pay, start=29, resume=31, gap_tight=1):
    """OpenAI 向けとみなす容量(FY26〜29 稼働分の share)が start〜resume−1 年は支払い pay 割。
    resume 年から再販: その年が逼迫期なら元の単価で(他の顧客が吸収)、緩和期なら緩和後の再契約相場で"""
    def f(c, y, price, p):
        if c['v'] in (26, 27, 28, 29) and y >= start:
            a = y - c['v']
            if y < resume:
                return price * (1 - share * (1 - pay))
            if resume < p['Y_star']:
                resale = c['P'] if y < p['Y_star'] else c['P'] * p['post_rho_loose'] * (1 - p['post_dec_loose']) ** (y - p['Y_star'])
            else:
                resale = c['P'] * p['post_rho_loose'] * ((1 - p['post_dec_loose']) ** (y - resume))
            if a <= p['contract_len']:
                return price * (1 - share) + resale * share
        return price
    return f


# 第4版: シナリオは対称(強気 25%・ベース 50%・弱気 25%)。強気と弱気は同じ変数を同じ幅だけ逆に動かす
BASE['prob'] = 0.50
BULL = copy.deepcopy(BASE)
BULL.update(name='強気', prob=0.25, anc_a=0.10,
            g_saas=[g + 0.02 for g in BASE['g_saas']], g_ocin=[g + 0.03 for g in BASE['g_ocin']],
            m_ocin=(0.30, 0.42, 5), mc_case='bull')
SC_MULT = lambda y, s: 1.0 if y <= 27 else (1 + s / 2 if y == 28 else 1 + s)    # 第4.2版: FY27 は建設中のため動かさない
BULL['ai'] = dict(AI_BASE, gw_plan={y: v * SC_MULT(y, 0.15) for y, v in AI_BASE['gw_plan'].items()},
                  sites_committed={y: v * SC_MULT(y, 0.15) for y, v in AI_BASE['sites_committed'].items()},
                  gen_price=gen_price_v44(0.045), Y_star=AI_BASE['Y_star'] + 2, s_eq=0.05,
                  rent_g_tight=0.08, rent_g_loose=0.04, post_rho_loose=0.70, post_dec_loose=0.10, util_post_loose=0.90)

BEAR = copy.deepcopy(BASE)
BEAR.update(name='弱気', prob=0.25, anc_a=0.0, g_sw_base=-0.03,
            g_saas=[g - 0.02 for g in BASE['g_saas']], g_ocin=[g - 0.03 for g in BASE['g_ocin']],
            m_ocin=(0.30, 0.34, 5), mc_case='bear')
BEAR['ai'] = dict(AI_BASE, gw_plan={y: v * SC_MULT(y, -0.15) for y, v in AI_BASE['gw_plan'].items()},
                  sites_committed=dict(AI_BASE['sites_committed']),
                  gen_price=gen_price_v44(0.015), Y_star=AI_BASE['Y_star'] - 2, s_eq=-0.05, s_eq_years=6,
                  rent_g_tight=0.04, rent_g_loose=0.02, post_rho_loose=0.50, post_dec_loose=0.20, util_post_loose=0.80,
                  rev_mod=openai_mod(0.60, 0.85, 29, 31))
BEAR['sp_c_year'] = 29                       # 第4.2版: S&P のトリガー (c)(AI 業界への否定的な見方)を弱気で復活
BEAR['ai']['sites_committed'] = dict(AI_BASE['sites_committed'])   # 第4.3版: 弱気でもベースの計画分の敷地は契約済み
DEEP = copy.deepcopy(BEAR)
DEEP.update(name='深い弱気(参考)', prob=0.0)

SEGS = ('sw', 'saas', 'ocin', 'mc', 'anc', 'ai', 'hw', 'svc')


def coc_fn(p, seg):
    rf = rf_path(p['rf'])
    return lambda y: rf(y) + p['beta'][seg] * ERP


def ramp(a, b, k, i):
    return a + (b - a) * min(i, k) / k


MC_CASES = {'base': (0.45, 0.05, 0.03), 'bull': (0.45, 0.035, 0.04), 'bear': (0.45, 0.08, 0.02)}


def mc_path(p, n):
    """検証反映+利用者の指摘: マルチクラウド DB の売上を、実績の成長率の減速の仕方から延長する。
    前年比倍率 16.3→9.2→6.3→5.0→4.5 倍 = 四半期の伸び 101→74→58→50→46%(減速幅 27→16→9→4pt)。
    Q1 FY27 の年換算 0.8B(推定、0.4〜1.5B)を起点に、四半期の伸びを毎期 d ずつ下げ、下限 floor で止める。
    共食い(失うサポート売上)は 売上の増分 ÷ 倍率 m で数える。"""
    q0, d, floor = MC_CASES[p.get('mc_case', 'base')]
    run0 = p['mc_run0'] / 4
    qrev = [run0]
    k = 1
    while len(qrev) < 4 * n:
        g = max(q0 - d * k, floor)
        qrev.append(qrev[-1] * (1 + g))
        k += 1
    # 会計年度に集計(FY27 = Q1 FY27 実績相当 + Q2〜Q4)
    rev = [sum(qrev[4 * i:4 * i + 4]) for i in range(n)]
    # FY36 以降は年 3% に上限
    for i in range(10, n):
        rev[i] = min(rev[i], rev[i - 1] * (1 + p['mc_u_late']))
    base0 = p['mc_run0']
    loss = [p['mc_mig'] * max(0.0, (r - base0)) / p['mc_m'] for r in rev]   # 移行分のみ共食い(残りは新規の利用)
    A = [r / (p['mc_D0'] * p['mc_h'] * p['mc_m']) for r in rev]     # 参考: 採用率に換算
    return A, rev, loss, base0 / (p['mc_D0'] * p['mc_h'] * p['mc_m'])


def calib_sw_margin(p):
    a = p['ai']
    old_K = sum(g * K for _, g, _, K in a['initial'])
    new_gw_avg = 0.425                                  # Q1 に 0.85GW を納入 → 期中平均 0.425GW
    da_q = (old_K + new_gw_avg * a['gen_capex'](27)) / a['acct_life'] / 4
    cost_q = (1.7 + new_gw_avg) * a['C0'] / 4 + 0.85 * a['startup'] * a['C0'] / 4
    ai_ebit_q = Q1['rev_ai'] - da_q - cost_q
    others = (Q1['rev_saas'] * p['m_saas'][0] + Q1['rev_ocin'] * p['m_ocin'][0] + Q1['rev_mc'] * p['m_mc'][0]
              + Q1['rev_hw'] * p['m_hw'] + Q1['rev_svc'] * p['m_svc'] + ai_ebit_q)
    return (Q1['ebit_adj'] - others) / Q1['rev_sw'], ai_ebit_q


def run(p):
    tax = p['tax']
    swm_q1, ai_q1 = calib_sw_margin(p)
    swm = p['sw_margin'] if p['sw_margin'] is not None else swm_q1
    years = list(range(Y0, YN + 1))
    n = len(years)
    A, mc_rev, mc_loss, a0 = mc_path(p, n)
    # ---------------- AI(コホート)
    r_ai = coc_fn(p, 'ai')
    ai_out, cohorts = run_ai(p['ai'], range(25, YAI + 1), r_ai)
    ai_rev = {y: ai_out[y]['rev'] for y in ai_out}
    # ---------------- 非 AI 事業
    prev = dict(FY26)
    prev['anc'] = p['anc_a'] * ai_out[26]['rev']
    seg = {k: {} for k in SEGS}
    for i, y in enumerate(years):
        sw_rev = FY26['sw'] * (1 + p['g_sw_base']) ** (i + 1) - mc_loss[i]
        r = dict(sw=sw_rev, saas=prev['saas'] * (1 + p['g_saas'][i]), ocin=prev['ocin'] * (1 + p['g_ocin'][i]),
                 mc=mc_rev[i], anc=p['anc_a'] * ai_rev[y], hw=prev['hw'] * (1 + p['g_hw']), svc=prev['svc'] * (1 + p['g_svc']))
        m = dict(sw=swm, saas=ramp(*p['m_saas'][:2], p['m_saas'][2], i), ocin=ramp(*p['m_ocin'][:2], p['m_ocin'][2], i),
                 mc=ramp(*p['m_mc'][:2], p['m_mc'][2], i), hw=p['m_hw'], svc=p['m_svc'])
        m['anc'] = m['ocin']
        for k in ('sw', 'saas', 'ocin', 'mc', 'anc', 'hw', 'svc'):
            ebit = r[k] * m[k]
            da = r[k] * p['da'][k]
            net_inv = 0.0 if k == 'sw' else max(r[k] - prev[k], 0) / p['s2c'][k]
            nopat = ebit * (1 - tax)
            seg[k][y] = dict(rev=r[k], ebit=ebit, margin=m[k], da=da, capex=da + net_inv, nopat=nopat, fcff=nopat - net_inv)
            prev[k] = r[k]
    for y in range(Y0, YAI + 1):
        a = ai_out[y]
        seg['ai'][y] = dict(rev=a['rev'], ebit=a['ebit'], margin=a['margin'], da=a['da'], capex=a['capex'], nopat=a['nopat'],
                            fcff=a['fcf'], gw=a['gw_in_service'], ebitda=a['ebitda'], P_new=a['P_new'], avg_age=a['avg_age'],
                            builds=a['builds'], retire=a['retire'], idle_cost=a['idle_cost'], idle_gw=a['idle_gw'],
                            npv_new=a['npv_new'])
    # ---------------- 事業別の価値
    seg_val = {}
    for k in SEGS:
        r_fn = coc_fn(p, k)
        last = YAI if k == 'ai' else YN
        yrs = list(range(Y0, last + 1))
        df = disc_factors(r_fn, yrs)
        pv = sum(seg[k][y]['fcff'] * (STUB if y == Y0 else 1) * df[y] for y in yrs)
        rT = r_fn(last)
        if k == 'ai':
            g = p['ai_tv_g']
            avg = sum(seg[k][y]['fcff'] for y in range(last - 9, last + 1)) / 10
            tv = avg * (1 + g) / (rT - g) * (1 + rT) ** 0.5
            tv_note = '直近10年の平均 FCF の永続成長(年央補正)'
        else:
            g, roic = p['term'][k]
            nT1 = seg[k][last]['nopat'] * (1 + g)
            reinv = 0.0 if (roic is None or g < 0) else g / roic
            tv = nT1 * (1 - reinv) / (rT - g) * (1 + rT) ** 0.5
            tv_note = '(1 − g/ROIC)÷(r − g)(年央補正)'
        pv_tv = tv * df[('end', last)]
        seg_val[k] = dict(pv_fcff=pv, tv=tv, pv_tv=pv_tv, ev=pv + pv_tv, r27=r_fn(Y0), rT=rT, tv_note=tv_note)
    # ---------------- 会社全体の経路(FY27〜FY45)と信用
    yrs = years
    nd = BS['debt'] + BS['fin_lease'] - BS['cash']
    prepay = [(BS['prepay'], 28)]
    lev_hist, rating_prev, surv = [], 'BBB-', 1.0
    fcf_hist, last_change = [], 26
    path = []
    for i, y in enumerate(yrs):
        ebit = sum(seg[k][y]['ebit'] for k in SEGS)
        da = sum(seg[k][y]['da'] for k in SEGS)
        ebitda = ebit + da
        capex = sum(seg[k][y]['capex'] for k in SEGS)
        rev = sum(seg[k][y]['rev'] for k in SEGS)
        gross = nd + BS['min_cash']
        interest = p['rate_debt'][i] * gross
        int_inc = p['cash_yield'] * BS['min_cash']
        ctax = tax * max(ebit - interest + int_inc, 0)
        pin = p['cust_fund'].get(y, p['cust_fund_tight'] if y < p['ai']['Y_star'] else p['cust_fund_loose']) * seg['ai'][y]['capex']
        prepay.append((pin * (STUB if y == Y0 else 1.0), y + 1))   # 第4.3版: FY27 は残り期間分だけ受け取る(現金と取り崩しをそろえる)
        pdraw = sum(amt / 5 for amt, st in prepay if st <= y < st + 5)
        ocf = ebitda - ctax - interest + int_inc + pin - pdraw
        fcf = ocf - capex
        div = BS['dps'] * BS['shares'] + BS['pref_div']
        frac = STUB if y == Y0 else 1.0
        nd_new = nd - (fcf - div) * frac
        if p.get('eq_raise') and y == p['eq_raise'][0]:
            nd_new -= p['eq_raise'][1]                  # 第4.4版: 株式での調達
        floor = BS['lev_floor'] * ebitda - BS['min_cash']
        bb = 0.0
        if fcf - div > 0 and nd_new < floor and y >= p.get('bb_start', 0):     # 第4.4版: 会社の優先順位(投資適格・配当・成長)に合わせ FY31 から
            bb = min(floor - nd_new, (fcf - div) * frac)      # 第4.2版: 買い戻しは超過 FCF の範囲だけ(借り増ししない)
            nd_new = nd_new + bb
        gw_lease = seg['ai'][y]['gw']
        f_l = max(0.0, (gw_lease - 1.7) / (12.0 - 1.7))
        lease_liab = BS['lease_liab'] + BS['lease_unc_pv'] * f_l
        lease_exp = BS['lease_exp0'] + BS['lease_exp_unc'] * f_l
        adj = (nd_new + BS['min_cash'] + lease_liab) / (ebitda + lease_exp)
        lev_hist.append(adj)
        # 第4.3版: S&P の記載(2026-07)に合わせる。格下げ (a) 調整後レバレッジ 4.5 倍超が2年続く、(b) FY29 までに FOCF が黒字化しない、
        # (c) AI 戦略・業界への否定的な見方(弱気シナリオで FY29)。投機的(BB+)から投資適格(BBB-)へ戻るのは、黒字 FCF が2年続き
        # 調整後 4.5 倍以下になった年。投資適格の中の格上げは FY29 以降・1年に1ノッチ・黒字 FCF 2年・閾値(BBB 3.5 倍、BBB+ 2.5 倍)以下。
        # 投資適格の中の格下げは閾値超えが2年続いたら1ノッチ。BB(5.5 倍超)は S&P に記載のない仮定
        fcf_hist.append(fcf)
        pos2 = len(fcf_hist) >= 2 and fcf_hist[-1] > 0 and fcf_hist[-2] > 0
        order = ['BB', 'BB+', 'BBB-', 'BBB', 'BBB+']
        thr = {'BBB-': 4.5, 'BBB': 3.5, 'BBB+': 2.5}
        k = order.index(rating_prev)
        if adj > 5.5:
            rt = 'BB'
        elif (p.get('sp_c_year') and y == p['sp_c_year']) or (adj > 4.5 and len(lev_hist) >= 2 and lev_hist[-2] > 4.5) \
                or (y == 29 and fcf <= 0):
            rt = order[min(k, 1)]                    # 悪い方を採る(BB は BB のまま)
        elif k <= 1:
            rt = order[k + 1] if (pos2 and adj <= 4.5 and y > last_change) else rating_prev
        else:
            rt = rating_prev
            nxt = order[k + 1] if k < 4 else None
            if nxt and pos2 and y >= 29 and y > last_change and adj <= thr[nxt]:
                rt = nxt                             # 1年に1ノッチ
            elif len(lev_hist) >= 2 and adj > thr[rating_prev] and lev_hist[-2] > thr[rating_prev] and y > last_change:
                rt = order[k - 1]                    # 閾値超えが2年続けば1ノッチ下げる
        if rt != rating_prev:
            last_change = y
        rating_prev = rt
        surv *= (1 - PD[rt] * frac)               # 検証反映: FY45 まで数える
        # 営業利益率の分解用
        shares_rev = {k: seg[k][y]['rev'] / rev for k in SEGS}
        margins = {k: (seg[k][y]['ebit'] / seg[k][y]['rev'] if seg[k][y]['rev'] else 0.0) for k in SEGS}
        # オーナー利益: EBITDA − 維持投資(AI は稼働容量の取得原価 ÷ 経済的耐用年数の近似 = 10 年、非 AI は償却)− 現金税
        ai_fleet_cost = seg['ai'][y]['gw'] * p['ai']['gen_capex'](y)
        maint = ai_fleet_cost / 9.0 + sum(seg[k][y]['da'] for k in SEGS if k != 'ai')
        owner = ebitda - maint - tax * max(ebit, 0)
        path.append(dict(year=y, rev=rev, ebit=ebit, ebitda=ebitda, da=da, capex=capex, interest=interest, ctax=ctax,
                         prepay_in=pin, prepay_draw=pdraw, ocf=ocf, fcf=fcf, nd=nd_new, gross_debt=nd_new + BS['min_cash'],
                         buyback=bb, adj_lev=adj, rating=rt, surv=surv, op_margin=ebit / rev, shares_rev=shares_rev,
                         margins=margins, owner=owner, maint=maint,
                         ni_br=(ebit - interest + int_inc) * (1 - tax) - BS['pref_div'], net_int=interest - int_inc))
        nd = nd_new
    # ---------------- APV 合計
    rd = p['rd']
    sh = 0.0
    acc = 1.0
    for i, y in enumerate(yrs):
        t = STUB / 2 if y == Y0 else STUB + (i - 1) + 0.5
        sh += tax * max(path[i]['net_int'], 0) * (STUB if y == Y0 else 1) / (1 + rd) ** t
    sh += p['shield_term_haircut'] * tax * path[-1]['gross_debt'] / (1 + rd) ** (STUB + len(yrs) - 1)
    ev = sum(v['ev'] for v in seg_val.values())
    claims = BS['debt'] * BOND_MV + BS['fin_lease'] + BS['pref'] + BS['prepay'] - BS['cash']
    eq_gc = ev + sh - claims
    pd_cum = 1 - surv
    new_sh = 0.0
    if p.get('eq_raise'):
        yr, amt, px = p['eq_raise']
        eq_gc += amt / (1 + coc_fn(p, 'ai')(yr)) ** (STUB + (yr - Y0) - 0.5)     # 第4.4版: 調達する現金(年央)
        new_sh = amt / px
    eq = eq_gc * (1 - pd_cum)
    # F22 純増
    r_sw = coc_fn(p, 'sw')
    df_sw = disc_factors(r_sw, yrs)
    loss_pv = sum(mc_loss[i] * p['mc_loss_margin'] * (1 - tax) * (STUB if y == Y0 else 1) * df_sw[y] for i, y in enumerate(yrs))
    loss_pv += mc_loss[-1] * p['mc_loss_margin'] * (1 - tax) * 0.98 / (r_sw(YN) + 0.02) * df_sw[('end', YN)]
    f22 = dict(rev={y: mc_rev[i] for i, y in enumerate(yrs)}, adoption={y: A[i] for i, y in enumerate(yrs)}, a0=a0,
               gross=seg_val['mc']['ev'], cannibal=loss_pv, net=seg_val['mc']['ev'] - loss_pv)
    # コホート表
    lives = [cohort_life(c, p['ai'], r_ai) for c in cohorts if c['gw'] > 0 and c['v'] <= 45]
    return dict(name=p['name'], prob=p['prob'], seg=seg, seg_val=seg_val, path=path, shield=sh, ev=ev, claims=claims,
                eq_gc=eq_gc, pd_cum=pd_cum, eq=eq, vps=eq / (BS['shares'] + new_sh), vps_gc=eq_gc / (BS['shares'] + new_sh), new_sh=new_sh, f22=f22,
                cohorts=cohorts, lives=lives, sw_margin=swm, sw_margin_q1=swm_q1, ai_q1=ai_q1, ai_out=ai_out)


def margin_bridge(r, y0=27, y1=None):
    """全社営業利益率の前年差を、構成比の効果と事業内の効果に分ける(Σ Δs·m̄ と Σ s̄·Δm)"""
    rows = []
    P = {q['year']: q for q in r['path']}
    for y in range(y0 + 1, (y1 or 45) + 1):
        a, b = P[y - 1], P[y]
        mix = sum((b['shares_rev'][k] - a['shares_rev'][k]) * (a['margins'][k] + b['margins'][k]) / 2 for k in SEGS)
        within = {k: (a['shares_rev'][k] + b['shares_rev'][k]) / 2 * (b['margins'][k] - a['margins'][k]) for k in SEGS}
        rows.append(dict(year=y, margin=b['op_margin'], delta=b['op_margin'] - a['op_margin'], mix=mix,
                         within_ai=within['ai'], within_other=sum(v for k, v in within.items() if k != 'ai'),
                         ai_share=b['shares_rev']['ai'], ai_margin=b['margins']['ai']))
    return rows


def rule40(r):
    out = []
    P = r['path']
    for i in range(1, len(P)):
        a, b = P[i - 1], P[i]
        g = b['rev'] / a['rev'] - 1
        out.append(dict(year=b['year'], growth=g, fcf_m=b['fcf'] / b['rev'], ebitda_m=b['ebitda'] / b['rev'],
                        owner_m=b['owner'] / b['rev'], r40_fcf=g + b['fcf'] / b['rev'], r40_ebitda=g + b['ebitda'] / b['rev'],
                        r40_owner=g + b['owner'] / b['rev']))
    return out


def multiples(r):
    P = {q['year']: q for q in r['path']}
    v = r['vps_gc']
    ng = lambda y, sbc: ((P[y]['ebit'] + sbc - P[y]['interest'] + 1.05) * 0.80 - BS['pref_div']) / BS['shares']   # 第4.2版: 優先株配当を控除
    out = dict(per_co27=v / 8.10, per_cons28=v / 10.78, ng27=ng(27, 4.6), ng28=ng(28, 4.9), ng30=ng(30, 5.5),
               br28=P[28]['ni_br'] / BS['shares'], br30=P[30]['ni_br'] / BS['shares'], br32=P[32]['ni_br'] / BS['shares'])
    out.update(per_ng27=v / out['ng27'], per_ng28=v / out['ng28'], per_br30=v / out['br30'], per_br32=v / out['br32'],
               ev_ebitda28=r['ev'] / P[28]['ebitda'], ev_ebitda30=r['ev'] / P[30]['ebitda'])
    # AI: 正規化した利益(FY32 の容量 × 定常の単位経済)に対する倍率
    ai = r['seg']['ai']
    out['ai_ev'] = r['seg_val']['ai']['ev']
    out['ai_ev_ebitda32'] = out['ai_ev'] / ai[32]['ebitda']
    norm_nopat = sum(ai[y]['nopat'] for y in range(32, 42)) / 10
    out['ai_ev_norm_nopat'] = out['ai_ev'] / norm_nopat
    out['ai_norm_margin'] = sum(ai[y]['ebit'] for y in range(32, 42)) / sum(ai[y]['rev'] for y in range(32, 42))
    return out


SCENS = None


def calibrate_sw_to_guidance(target=8.10):
    lo, hi = 0.50, 0.95
    for _ in range(30):
        mid = (lo + hi) / 2
        q = copy.deepcopy(BASE); q['sw_margin'] = mid
        if multiples(run(q))['ng27'] < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def scens():
    return (BASE, BULL, BEAR)


def weighted(mod=None):
    tot = 0.0
    for sc in scens():
        q = copy.deepcopy(sc)
        if mod:
            mod(q)
        tot += run(q)['vps'] * q['prob']
    return tot


def tornado(level='base'):
    base = run(BASE)['vps'] if level == 'base' else weighted()
    cases = []

    def val(mod):
        if level == 'base':
            q = copy.deepcopy(BASE); mod(q); return run(q)['vps']
        return weighted(mod)

    def add(label, lo_mod, hi_mod, lo_lab, hi_lab):
        cases.append(dict(label=label, lo=val(lo_mod) - base, hi=val(hi_mod) - base, lo_lab=lo_lab, hi_lab=hi_lab))
    add('金利の経路', lambda q: q.update(rf='high'), lambda q: q.update(rf='normalize'), '6.0%一定', '予測どおり4.2%へ低下')
    add('需給逼迫の終わる年(Y*)', lambda q: q['ai'].update(Y_star=q['ai']['Y_star'] - 2), lambda q: q['ai'].update(Y_star=q['ai']['Y_star'] + 2), '−2年', '+2年')
    add('新規契約の単価', lambda q: q['ai'].update(gen_price=lambda y, f=q['ai']['gen_price']: f(y) - 1.0),
        lambda q: q['ai'].update(gen_price=lambda y, f=q['ai']['gen_price']: f(y) + 1.0), '−1.0B/GW', '+1.0B/GW')
    add('1GW あたり投資', lambda q: q['ai'].update(gen_capex=lambda y, f=q['ai']['gen_capex']: f(y) + 3.0),
        lambda q: q['ai'].update(gen_capex=lambda y, f=q['ai']['gen_capex']: f(y) - 3.0), '+3B', '−3B')
    add('長期の超過 NPV(投資比)', lambda q: q['ai'].update(s_eq=q['ai']['s_eq'] - 0.05), lambda q: q['ai'].update(s_eq=q['ai']['s_eq'] + 0.10), '−5pt', '+10pt')
    add('緩和後の再契約(単価・下落・稼働率)', lambda q: q['ai'].update(post_rho_loose=0.45, post_dec_loose=0.25, util_post_loose=0.75),
        lambda q: q['ai'].update(post_rho_loose=0.75, post_dec_loose=0.08, util_post_loose=0.92), '0.45・−25%・75%', '0.75・−8%・92%')
    add('値崩れの谷', lambda q: q['ai'].update(trough_years=2, trough_mult=0.85), lambda q: q['ai'].update(trough_years=0, F=4), '2年・損益分岐の85%', '4年でフェード')
    add('AI 付随サービス(AI 売上比)', lambda q: q.update(anc_a=0.0), lambda q: q.update(anc_a=0.10), '0%', '10%')
    add('マルチクラウド DB(F22)', lambda q: q.update(mc_case='bear'), lambda q: q.update(mc_case='bull'), '減速が速い', '減速が遅い')
    add('マルチクラウドの起点(年換算)', lambda q: q.update(mc_run0=0.4), lambda q: q.update(mc_run0=1.5), '0.4B', '1.5B')
    add('市場の賃料上昇(Oracle の固定リースとの差)', lambda q: q['ai'].update(rent_g_tight=0.025, rent_g_loose=0.025),
        lambda q: q['ai'].update(rent_g_tight=0.09, rent_g_loose=0.04), '差なし(2.5%)', '逼迫期 9%・緩和後 4%')
    add('OCI 一般の利益率(FY32)', lambda q: q.update(m_ocin=(0.30, 0.33, 5)), lambda q: q.update(m_ocin=(0.30, 0.42, 5)), '33%', '42%')
    add('ソフト保守の減少率(移行分を除く)', lambda q: q.update(g_sw_base=-0.04), lambda q: q.update(g_sw_base=0.0), '−4%', '0%')
    add('マルチクラウドの移行倍率 m', lambda q: q.update(mc_m=2.0), lambda q: q.update(mc_m=4.0), '2.0倍', '4.0倍')
    add('ソフト保守の利益率', lambda q: q.update(sw_margin=0.625), lambda q: q.update(sw_margin=0.80), '62.5%', '80%')
    global ERP
    e0 = ERP
    ERP = e0 + 0.005; lo = (run(BASE)['vps'] if level == 'base' else weighted()) - base
    ERP = e0 - 0.005; hi = (run(BASE)['vps'] if level == 'base' else weighted()) - base
    ERP = e0
    cases.append(dict(label='株式リスクプレミアム', lo=lo, hi=hi, lo_lab='+0.5pt', hi_lab='−0.5pt'))
    cases.sort(key=lambda c: -abs(c['hi'] - c['lo']))
    return base, cases


def print_scen(r):
    print('\n=====', r['name'], '確率', r['prob'])
    print('年度  売上  AI売上 AI_GW AI率   全社営業率 EBITDA capex  FCF  調整後 格付  新規単価 新規NPV 遊休GW')
    for q in r['path']:
        y = q['year']
        if y > 40 and y % 5:
            continue
        a = r['seg']['ai'][y]
        print('FY%d %6.1f %6.1f %5.1f %6.1f%% %6.1f%% %6.1f %6.1f %6.1f %5.2f %-5s %5.1f %+6.1f %4.1f' % (
            y, q['rev'], a['rev'], a['gw'], a['margin'] * 100, q['op_margin'] * 100, q['ebitda'], q['capex'], q['fcf'],
            q['adj_lev'], q['rating'], a['P_new'], a['npv_new'], a['idle_gw']))
    for k in SEGS:
        v = r['seg_val'][k]
        print('  %-5s EV %7.1f /株 %7.2f  r %.2f%%→%.2f%%  TV比率 %.0f%%' % (
            k, v['ev'], v['ev'] / BS['shares'], v['r27'] * 100, v['rT'] * 100, v['pv_tv'] / v['ev'] * 100 if v['ev'] else 0))
    print('  事業価値 %.1f  節税 %.1f  負債等 %.1f  存続時 /株 %.2f  累積PD(FY45) %.2f%% → /株 %.2f' % (
        r['ev'], r['shield'], r['claims'], r['vps_gc'], r['pd_cum'] * 100, r['vps']))
    f = r['f22']
    print('  F22: 総価値 %.1f 共食い %.1f 純増 %.1f(/株 %.2f) 売上 FY30 %.1f・FY36 %.1f・FY45 %.1f' % (
        f['gross'], f['cannibal'], f['net'], f['net'] / BS['shares'], f['rev'][30], f['rev'][36], f['rev'][45]))
    print('  コホート: ' + ' | '.join('FY%d %.1fGW 単価%.1f IRR %.0f%% 寿命%d年(%s) 一生の利益率 %.0f%% NPV/投資 %+.0f%%' % (
        L['v'], L['gw'], L['P'], L['irr'] * 100, L['life'], L['why'], L['margin_life'] * 100, L['npv_per_K'] * 100)
        for L in r['lives'] if L['v'] in (25, 27, 29, 31, 33, 35, 38)))
    m = multiples(r)
    print('  倍率: 会社FY27 EPS→%.1f倍、非GAAP FY27 %.2f→%.1f倍、FY28 %.2f→%.1f倍、事業実態 FY30 %.2f→%.1f倍、EV/EBITDA FY28 %.1f' % (
        m['per_co27'], m['ng27'], m['per_ng27'], m['ng28'], m['per_ng28'], m['br30'], m['per_br30'], m['ev_ebitda28']))


if __name__ == '__main__':
    swc = calibrate_sw_to_guidance()
    for sc in (BASE, BULL, BEAR, DEEP):
        sc['sw_margin'] = round(swc, 3)
    print('ソフト保守の利益率を FY27 非GAAP EPS ガイダンス 8.10 に較正: %.1f%%' % (swc * 100))
    res = {s_['name']: run(s_) for s_ in scens()}
    b = res['ベース']
    print('ソフト保守の利益率: 採用 %.1f%% / Q1 FY27 単独の較正 %.1f%% / 直近4四半期の較正 約 69〜70%%' % (b['sw_margin'] * 100, b['sw_margin_q1'] * 100))
    for r in res.values():
        print_scen(r)
    w = sum(r['vps'] * r['prob'] for r in res.values())
    print('\n確率加重の本源的価値 /株 %.2f' % w)
    print('\n営業利益率の分解(ベース): 年度 率 前年差 = 構成比 + AI内 + 他事業内')
    for q in margin_bridge(b, 27, 40):
        print('  FY%d %.1f%% %+5.1fpt = %+5.1f %+5.1f %+5.1f  (AI 構成比 %.0f%%, AI 率 %.1f%%)' % (
            q['year'], q['margin'] * 100, q['delta'] * 100, q['mix'] * 100, q['within_ai'] * 100, q['within_other'] * 100,
            q['ai_share'] * 100, q['ai_margin'] * 100))
    print('\nルール・オブ・40(ベース)')
    for q in rule40(b)[:8]:
        print('  FY%d 成長 %4.0f%%  FCF %+5.0f → %4.0f | EBITDA %4.0f → %4.0f | オーナー %4.0f → %4.0f' % (
            q['year'], q['growth'] * 100, q['fcf_m'] * 100, q['r40_fcf'] * 100, q['ebitda_m'] * 100, q['r40_ebitda'] * 100,
            q['owner_m'] * 100, q['r40_owner'] * 100))
    bt, cases = tornado('base')
    print('\n感応度(ベース %.2f からの差)' % bt)
    for c in cases:
        print('  %-28s %s: %+6.1f   %s: %+6.1f' % (c['label'], c['lo_lab'], c['lo'], c['hi_lab'], c['hi']))
