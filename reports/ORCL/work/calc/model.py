# -*- coding: utf-8 -*-
"""
Oracle (ORCL) 事業エンジン・モデル / バリュエーション計算(2026-10-11 時点)
- 前提は INPUTS / BASE / SCEN に集約し、出所をコメントで併記する。結果は out/ に JSON と CSV で出力。
- 単位: 金額 B$(10億ドル)、株数 B株(10億株)、EPS ドル/株。会計年度は5月末(FY27 = 2026-06〜2027-05)。
- 経路: コンセンサス / 会社シナリオ / 事業エンジン / 弱気(独立)。EPS は非GAAP と事業実態(SBC控除後)の2定義。
"""
import json, math, os, csv, copy

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)
YEARS = ['FY27', 'FY28', 'FY29', 'FY30', 'FY31', 'FY32']
TAX = 0.20  # 非GAAP 税率(Q1 FY26 実績 20.5%, H1)

# ================================================================ 前提(出所)
I = dict(
    price=141.40, price_date='2026-10-09',     # MarketBeat 速報(単一出典)。10-08 終値 135.69(FT 報道日、複数出典)
    shares_now=3.05,                            # Q1 FY27 希薄化後 3.00(期中平均, H6)+ ATM 141百万株の期末効果(H5)
    debt=125.3, cash=37.1,                      # 2026-08-31(H3: 10-Q 経由)
    fin_lease=9.2, op_lease=34.6, lease_unc=288.0,  # 同(H3)
    pref=5.0, prepay_fin=11.4, deferred=30.8,   # 優先株(H3)、金融要素を含む前払い(10-Q, S1)、前受収益(H4)
    rpo=664.0,
    fy26_rev=67.4, fy26_ngop=28.9, fy26_ngeps=7.631, fy26_ngeps_ex=6.83, fy26_gaapeps=5.83,
    fy26_sbc=4.811, fy26_da=7.6, fy26_ocf=31.977, fy26_capex=55.663, fy26_shares=2.914,
    fy26_software=24.54, fy26_saas=15.9, fy26_oci=18.1, fy26_hw=3.08, fy26_svc=5.74,
    fy26_oci_ai=7.2,     # 推定: The Information(Q1 FY26 GPU レンタル 0.9)、Q2 GPU関連 +177%、Q3 AIインフラ +243% から逆算
    q1_rev=19.345, q1_oci=7.4, q1_oci_ai=4.1, q1_ngop=8.2,   # Q1 FY27(H1/S4)。AI分割は推定
    g27_rev=90.0, g27_eps=8.10, g30_rev=225.0, g30_eps=21.0, g30_oci=166.0,  # 会社ガイダンス・目標(S1)
    cons_eps={'FY27': 8.05, 'FY28': 10.78},     # Non-GAAP 系コンセンサス(tickerleague 25名 / TickFlow 16名, H6)
    cons_rev={'FY27': 90.5, 'FY28': 130.6, 'FY29': 183.2},   # Yahoo / TickFlow(H6)
    sbc27=4.6, sbc_g=0.06,                      # Q1 FY27 SBC 1.127×4(H5)
)

# ================================================================ 事業エンジン経路(ベース)
BASE = dict(
    name='事業エンジン',
    software_g=-0.03,
    saas_g=[0.10, 0.10, 0.09, 0.09, 0.08, 0.08],
    oci_nonai_g=[0.30, 0.25, 0.20, 0.18, 0.15, 0.12],
    hw=3.1, svc_g=0.03,
    core_margin=0.48,                       # 非GAAP(SBC 除く)。Q1 FY27 照合で較正
    gw_end={'FY26': 1.7, 'FY27': 5.0, 'FY28': 8.0, 'FY29': 10.5, 'FY30': 12.0, 'FY31': 13.0, 'FY32': 13.8},
    rev_per_gw=[8.0, 9.5, 10.0, 10.5, 10.5, 10.5],   # B$/GW-年。会社例示 6年$60B/GW=10、OpenAI 4.5GW $300B/5年=13.3
    ai_ebit=[0.16, 0.23, 0.27, 0.29, 0.30, 0.30],    # AI容量の粗利率(Q3 FY26 32%)−立上げ費用−営業費3%
    openai_share=0.45, openai_real=1.0,     # AI売上に占める OpenAI 分(RPO の45〜50%, S2/S3)と実現率
    net_int=[4.4, 5.8, 6.4, 6.2, 5.6, 5.0],
    other=0.4, pref_div=0.325,
    shares=[3.03, 3.08, 3.12, 3.13, 3.14, 3.15],
)


def path_engine(p):
    rows = []
    sw = I['fy26_software']; saas = I['fy26_saas']; ocin = I['fy26_oci'] - I['fy26_oci_ai']
    svc = I['fy26_svc']; sbc = I['sbc27'] / (1 + I['sbc_g']); gwp = p['gw_end']['FY26']
    for i, y in enumerate(YEARS):
        sw *= 1 + p['software_g']; saas *= 1 + p['saas_g'][i]; ocin *= 1 + p['oci_nonai_g'][i]
        svc *= 1 + p['svc_g']; sbc *= 1 + I['sbc_g']
        core = sw + saas + ocin + p['hw'] + svc
        gwe = p['gw_end'][y]; gwa = (gwp + gwe) / 2; gwp = gwe
        ai = gwa * p['rev_per_gw'][i]
        if i >= 1:
            ai *= 1 - p['openai_share'] * (1 - p['openai_real'])
        cop = core * p['core_margin']; aop = ai * p['ai_ebit'][i]
        op = cop + aop
        pt = op - p['net_int'][i] + p['other']
        ni = pt * (1 - TAX) - p['pref_div']
        sh = p['shares'][i]
        rows.append(dict(year=y, software=sw, saas=saas, oci_nonai=ocin, core_rev=core, gw_avg=gwa, gw_end=gwe,
                         ai_rev=ai, oci=ocin + ai, rev=core + ai, core_op=cop, ai_op=aop, ng_op=op,
                         ng_margin=op / (core + ai), ni=ni, sbc=sbc, shares=sh,
                         eps_ng=ni / sh, eps_br=(ni - sbc * (1 - TAX)) / sh))
    return rows


def sbc_ps(i, shares):
    return I['sbc27'] * (1 + I['sbc_g']) ** i * (1 - TAX) / shares


def path_consensus(eng):
    """コンセンサス経路: FY27・FY28 は EPS コンセンサス。FY29 はコンセンサス売上 183.2 を事業エンジンの利益率で
    EPS に変換(延長)。FY30 以降は売上成長 +20%/+13%/+9% とエンジンの利益率で延長(延長部分と明記)"""
    out = []
    rev = {'FY29': I['cons_rev']['FY29']}
    rev['FY30'] = rev['FY29'] * 1.20; rev['FY31'] = rev['FY30'] * 1.13; rev['FY32'] = rev['FY31'] * 1.09
    for i, y in enumerate(YEARS):
        e = eng[i]
        if y in I['cons_eps']:
            eps = I['cons_eps'][y]; src = 'コンセンサス'
            r = I['cons_rev'].get(y)
        else:
            r = rev[y]
            ai = r - e['core_rev']
            op = e['core_op'] + ai * BASE['ai_ebit'][i]
            ni = (op - BASE['net_int'][i] + BASE['other']) * (1 - TAX) - BASE['pref_div']
            eps = ni / e['shares']; src = '延長(コンセンサス売上×エンジン利益率)' if y == 'FY29' else '延長(売上成長仮定×エンジン利益率)'
        out.append(dict(year=y, rev=r, eps_ng=eps, eps_br=eps - sbc_ps(i, e['shares']), src=src))
    return out


def path_company(eng):
    """会社シナリオ経路: FY27 $8.10 → FY30 $21(幾何補間)。FY31・FY32 は +20%・+15% で延長"""
    g = (I['g30_eps'] / I['g27_eps']) ** (1 / 3)
    eps = {'FY27': I['g27_eps'], 'FY28': I['g27_eps'] * g, 'FY29': I['g27_eps'] * g * g, 'FY30': I['g30_eps']}
    eps['FY31'] = eps['FY30'] * 1.20; eps['FY32'] = eps['FY31'] * 1.15
    rev = {'FY27': 90.0, 'FY30': 225.0}
    rg = (225.0 / 90.0) ** (1 / 3)
    rev['FY28'] = 90 * rg; rev['FY29'] = 90 * rg * rg; rev['FY31'] = 225 * 1.18; rev['FY32'] = rev['FY31'] * 1.13
    out = []
    for i, y in enumerate(YEARS):
        out.append(dict(year=y, rev=rev[y], eps_ng=eps[y], eps_br=eps[y] - sbc_ps(i, eng[i]['shares']),
                        src='会社目標' if y in ('FY27', 'FY30') else ('補間' if y in ('FY28', 'FY29') else '延長')))
    return out


BEAR = copy.deepcopy(BASE)
BEAR.update(name='弱気',
            gw_end={'FY26': 1.7, 'FY27': 4.5, 'FY28': 6.5, 'FY29': 8.0, 'FY30': 9.0, 'FY31': 9.5, 'FY32': 9.5},
            rev_per_gw=[8.0, 9.0, 9.0, 9.0, 8.5, 8.0],
            ai_ebit=[0.14, 0.17, 0.18, 0.18, 0.17, 0.16],
            openai_real=0.5,                     # FY28 以降、OpenAI 分の半分が不払い・縮小(代替需要で一部再販済みを含む純額)
            net_int=[4.6, 6.6, 7.8, 8.2, 8.0, 7.6],
            shares=[3.06, 3.20, 3.30, 3.35, 3.36, 3.37],  # 低株価での追加増資
            core_margin=0.475)


def cagr(a, b, n):
    if a <= 0 or b <= 0:
        return float('nan')
    return (b / a) ** (1 / n) - 1


# ================================================================ SOTP(事業別価値)と GW あたり経済性
SOTP = dict(
    wacc_core=0.085, wacc_ai=0.10,
    core_nopat27=None,          # 下で計算(コア非GAAP営業利益−SBC)×(1−税)
    core_g5=0.06, core_gT=0.025, core_roic=0.35,
    R=10.0, m=0.29, K=25.0, L=6, pr=0.6, Lr=2, fac_share=0.35, gm_ref=0.32,
    gw_inservice=2.55, age_inservice=1.0,
    gw_contracted_total=10.2,   # AI の RPO 約$560B ÷($10B/GW-年×5.5年)
    build_disc=0.85,            # 未建設分の NPV を建設時期で割引(1〜3年先)
    growth_gw_per_yr=1.5, growth_years=5, growth_npv_haircut=0.7, growth_prob=0.5, growth_start_disc=0.62,
    idle_after=False,
)


def gw_npv(s, tax=TAX):
    """1GW の新規案件(Oracle 調達の GPU)の NPV と内訳"""
    R, m, K, L, r = s['R'], s['m'], s['K'], s['L'], s['wacc_ai']
    D = K / 6.0
    cash = R * m * (1 - tax) + D
    ann = sum(1 / (1 + r) ** t for t in range(1, L + 1))
    pv_op = cash * ann
    F = s['fac_share'] * (1 - s['gm_ref']) * R
    res_cash = (R * s['pr'] - F - 0.03 * R * s['pr']) * (1 - tax)
    pv_res = sum(res_cash / (1 + r) ** t for t in range(L + 1, L + 1 + s['Lr'])) if s['Lr'] > 0 else 0.0
    pv_idle = 0.0
    if s.get('idle_after'):
        idle = -0.5 * F * (1 - tax)
        pv_idle = sum(idle / (1 + r) ** t for t in range(L + 1 + s['Lr'], 18))
    irr = irr_calc([-K] + [cash] * L + ([res_cash] * s['Lr']))
    return dict(npv=pv_op - K + pv_res + pv_idle, pv_op=pv_op, pv_res=pv_res, pv_idle=pv_idle,
                cash_per_yr=cash, res_cash=res_cash, irr=irr)


def irr_calc(cfs):
    lo, hi = -0.9, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        v = sum(c / (1 + mid) ** t for t, c in enumerate(cfs))
        if v > 0:
            lo = mid
        else:
            hi = mid
    return mid


def sotp(s, eng_rows=None, core_nopat=None, verbose=False):
    eng_rows = eng_rows or path_engine(BASE)
    if core_nopat is None:
        core_nopat = (eng_rows[0]['core_op'] - I['sbc27']) * (1 - TAX)
    # コア: 2段階 DCF
    wc, g5, gT, roic = s['wacc_core'], s['core_g5'], s['core_gT'], s['core_roic']
    pv = 0.0; nopat = core_nopat
    for t in range(1, 6):
        if t > 1:
            nopat *= 1 + g5
        pv += nopat * (1 - g5 / roic) / (1 + wc) ** t
    nT = nopat * (1 + gT)
    tv = nT * (1 - gT / roic) / (wc - gT)
    core_ev = pv + tv / (1 + wc) ** 5
    core_pv3 = sum(core_nopat * (1 + g5) ** (t - 1) * (1 - g5 / roic) / (1 + wc) ** t for t in range(1, 4))
    # AI: 稼働中(建設済み、残存期間の現金)+ 契約済み未建設(NPV)+ 未契約の成長オプション
    g = gw_npv(s)
    r = s['wacc_ai']
    rem = s['L'] - s['age_inservice']
    ann_rem = sum(1 / (1 + r) ** t for t in range(1, int(rem) + 1))
    res_rem = sum(g['res_cash'] / (1 + r) ** t for t in range(int(rem) + 1, int(rem) + 1 + s['Lr']))
    pv_inservice = s['gw_inservice'] * (g['cash_per_yr'] * ann_rem + res_rem)
    gw_future = s['gw_contracted_total'] - s['gw_inservice']
    pv_contracted = gw_future * g['npv'] * s['build_disc']
    pv_growth = (s['growth_gw_per_yr'] * s['growth_years'] * g['npv'] * s['growth_npv_haircut']
                 * s['growth_prob'] * s['growth_start_disc'])
    ai_ev = pv_inservice + pv_contracted + pv_growth - I['prepay_fin']
    # AI 3年以内の現金(時間分布用)
    ai_pv3 = s['gw_inservice'] * g['cash_per_yr'] * sum(1 / (1 + r) ** t for t in range(1, 4))
    ev = core_ev + ai_ev
    claims = I['debt'] - I['cash'] + I['fin_lease'] + I['pref']
    eq = ev - claims
    ps = eq / I['shares_now']
    res = dict(core_nopat=core_nopat, core_ev=core_ev, gw=g, pv_inservice=pv_inservice, pv_contracted=pv_contracted,
               pv_growth=pv_growth, ai_ev=ai_ev, ev=ev, claims=claims, equity=eq, per_share=ps,
               pv3_share=(core_pv3 + ai_pv3) / ev)
    return res


# ================================================================ 実行
def run():
    R = {}
    eng = path_engine(BASE); bear = path_engine(BEAR)
    cons = path_consensus(eng); comp = path_company(eng)
    R['engine'] = eng; R['bear'] = bear; R['consensus'] = cons; R['company'] = comp

    # Q1 FY27 照合(エンジン式の再構成)
    core_q1 = I['q1_rev'] - I['q1_oci_ai']
    R['q1_check'] = dict(core_q1=core_q1, model_op=core_q1 * BASE['core_margin'] + I['q1_oci_ai'] * 0.18,
                         actual_op=I['q1_ngop'])
    R['q1_check']['diff_pct'] = (R['q1_check']['model_op'] / I['q1_ngop'] - 1) * 100

    # 事業実態EPS(FY26 実績・FY27 基準)
    fy26_br = I['fy26_ngeps_ex'] - I['fy26_sbc'] * (1 - TAX) / I['fy26_shares']
    fy27_base_br = I['g27_eps'] - sbc_ps(0, 3.03)
    R['br'] = dict(fy26_br=fy26_br, fy27_base_br=fy27_base_br, sbc_ps27=sbc_ps(0, 3.03),
                   ramp_uplift_ps=(0.28 - BASE['ai_ebit'][0]) * eng[0]['ai_rev'] * (1 - TAX) / 3.03,
                   life4_down_ps=-(77.8 / 4 - 77.8 / 6) * (1 - TAX) / 3.03)

    # EPS 成長(対数分解)FY25→FY26(非GAAP、一時益除く)
    R['logdecomp'] = dict(
        rev=math.log(67.4 / 57.4), shares=-math.log(2.914 / 2.866),
        margin_ex=math.log((6.83 * 2.914 / 67.4) / (6.03 * 2.866 / 57.4)),
        total_ex=math.log(6.83 / 6.03))

    # 経路別 CAGR と PEG(現株価)
    paths = {'コンセンサス': cons, '会社シナリオ': comp, '事業エンジン': eng, '弱気': bear}
    pe = {}
    for k, v in paths.items():
        br = [x['eps_br'] for x in v]; ng = [x['eps_ng'] for x in v]
        g5 = cagr(br[0], br[5], 5); g3 = cagr(br[0], br[3], 3)
        per = I['price'] / br[0]
        pe[k] = dict(eps_br=br, eps_ng=ng, g5=g5, g3=g3, per_br=per, peg5=per / (g5 * 100) if g5 > 0 else float('nan'),
                     per_ng=I['price'] / ng[0], g5_ng=cagr(ng[0], ng[5], 5))
    R['paths'] = pe
    R['fy26_br'] = fy26_br

    # SOTP: ベース・強気・弱気
    s_base = copy.deepcopy(SOTP)
    s_bull = copy.deepcopy(SOTP); s_bull.update(m=0.33, pr=0.8, Lr=3, wacc_ai=0.095, growth_gw_per_yr=2.5, growth_prob=0.6,
                                                 core_g5=0.07)
    s_bear = copy.deepcopy(SOTP); s_bear.update(m=0.18, pr=0.0, Lr=0, idle_after=True, wacc_ai=0.11, growth_prob=0.0,
                                                 gw_contracted_total=7.0, core_g5=0.045, wacc_core=0.09)
    R['sotp'] = {'base': sotp(s_base, eng), 'bull': sotp(s_bull, eng), 'bear': sotp(s_bear, eng)}

    # 価値感度分析(芯の特定): ベース SOTP から1変数ずつ現実的な幅で動かす
    tests = [
        ('AI容量の利益率 m(EBIT)', 'm', 0.18, 0.35),
        ('経済的寿命×更新単価(残存価格比 pr・年数)', 'pr', 0.0, 0.9),
        ('受注済み容量の実現(OpenAI 分の不払い)', 'gw_contracted_total', 7.0, 10.2),
        ('AI の資本コスト', 'wacc_ai', 0.115, 0.085),
        ('コアの資本コスト', 'wacc_core', 0.095, 0.0775),
        ('コアの成長率(5年)', 'core_g5', 0.04, 0.08),
        ('GW あたり売上(単価)', 'R', 9.0, 12.0),
        ('GW あたり Oracle 負担 capex', 'K', 28.0, 20.0),
        ('未契約の成長(GW/年)', 'growth_gw_per_yr', 0.0, 3.0),
    ]
    base_ps = R['sotp']['base']['per_share']
    tor = []
    for label, key, lo, hi in tests:
        a = copy.deepcopy(SOTP); a[key] = lo
        b = copy.deepcopy(SOTP); b[key] = hi
        if key == 'pr':
            a['Lr'] = 0; a['idle_after'] = True; b['Lr'] = 3
        va = sotp(a, eng)['per_share']; vb = sotp(b, eng)['per_share']
        tor.append(dict(label=label, key=key, lo=lo, hi=hi, v_lo=va, v_hi=vb, swing=abs(vb - va)))
    tor.sort(key=lambda x: -x['swing'])
    R['tornado'] = dict(base=base_ps, rows=tor)

    # リバース: 現株価に一致する m(他はベース)
    lo, hi = 0.0, 0.6
    for _ in range(60):
        mid = (lo + hi) / 2
        s = copy.deepcopy(SOTP); s['m'] = mid
        if sotp(s, eng)['per_share'] < I['price']:
            lo = mid
        else:
            hi = mid
    R['implied_m'] = mid
    # 現株価に一致する コア WACC(AI はベース)
    lo, hi = 0.06, 0.14
    for _ in range(60):
        mid = (lo + hi) / 2
        s = copy.deepcopy(SOTP); s['wacc_core'] = mid
        if sotp(s, eng)['per_share'] > I['price']:
            lo = mid
        else:
            hi = mid
    R['implied_wacc_core'] = mid

    # 成長の値段(定常状態価値)
    core_ss = R['sotp']['base']['core_nopat'] + 1.5          # 成長目的の S&M/R&D 削減分(推定 $1.5B 税後)
    ai_ss = 5.0 * 10.0 * 0.29 * (1 - TAX)                     # FY27 末に稼働済み 5.0GW の定常 NOPAT
    int_after = 6.2 * (1 - TAX)
    ss_earn = core_ss + ai_ss - int_after
    coe = 0.095
    ss_val = ss_earn / coe
    mcap = I['price'] * I['shares_now']
    R['growth_price'] = dict(core_ss=core_ss, ai_ss=ai_ss, interest=int_after, ss_earn=ss_earn, coe=coe,
                             ss_value=ss_val, ss_ps=ss_val / I['shares_now'], mcap=mcap,
                             growth_price=mcap - ss_val, growth_share=(mcap - ss_val) / mcap)
    return R


if __name__ == '__main__':
    R = run()
    def p(x):
        if isinstance(x, float):
            return round(x, 3)
        if isinstance(x, dict):
            return {k: p(v) for k, v in x.items()}
        if isinstance(x, list):
            return [p(v) for v in x]
        return x
    print('Q1照合', p(R['q1_check']))
    print('BR', p(R['br']))
    print('logdecomp', p(R['logdecomp']))
    for y in R['engine']:
        print('ENG', p({k: y[k] for k in ['year', 'core_rev', 'gw_avg', 'ai_rev', 'oci', 'rev', 'ng_op', 'ng_margin', 'eps_ng', 'eps_br']}))
    for y in R['bear']:
        print('BEAR', p({k: y[k] for k in ['year', 'rev', 'ai_rev', 'ng_margin', 'eps_ng', 'eps_br']}))
    for y in R['consensus']:
        print('CONS', p(y))
    for y in R['company']:
        print('COMP', p(y))
    for k, v in R['paths'].items():
        print('PATH', k, p({kk: v[kk] for kk in ['g5', 'g3', 'per_br', 'peg5', 'per_ng', 'g5_ng']}))
    for k, v in R['sotp'].items():
        print('SOTP', k, p({kk: v[kk] for kk in ['core_nopat', 'core_ev', 'pv_inservice', 'pv_contracted', 'pv_growth', 'ai_ev', 'ev', 'claims', 'equity', 'per_share', 'pv3_share']}), p(v['gw']))
    print('TORNADO base', round(R['tornado']['base'], 1))
    for t in R['tornado']['rows']:
        print('  ', t['label'], t['lo'], t['hi'], round(t['v_lo'], 1), round(t['v_hi'], 1), round(t['swing'], 1))
    print('implied m', round(R['implied_m'], 3), 'implied core wacc', round(R['implied_wacc_core'], 4))
    print('growth price', p(R['growth_price']))
    json.dump(p(R), open(os.path.join(OUT, 'results.json'), 'w'), ensure_ascii=False, indent=1, default=str)
