# -*- coding: utf-8 -*-
"""
第4.5版(2026-10-30、利用者の指摘「売上見通しの数字がおかしい」): 立ち上げを 2 年に分ける(ramp1 = 2 年目の売上の比率)。
使用量に比例する費用(その他・追加費用)も同じ比率で立ち上げる(ramp_cost)。賃料と償却は引き渡しから全額。
第4.4版(2026-10-30): 世代ごとの追加の現金費用 X(会社の 1GW 例の粗利率 35% に較正)を持たせる。gen_xcost(年) で与える。
AI インフラのコホート(世代)経済性エンジン 第4.3版(2026-10-17、再検証の指摘 V42-3・6・7 を反映。第4版は F05)
第4版の変更: (1) リースする敷地は計画の最終年(FY32)までの目標容量に限る(計画外の仮想成長に敷地を借りない)。
(2) 緩和期に、借りたまま空いている敷地へ建てるかの判定では、賃料は埋没費用とし、転貸で得られたはずの賃料(sublease 分)だけを費用に数える。
追加: 現金費用を「賃料」と「その他(電力・運用)」に分け、Oracle の賃料は 15〜19 年の長期リースで固定(年 +e_lease)、
市場の賃料は逼迫期 rent_g_tight・緩和後 rent_g_loose で上がる。緩和後の新規単価は「限界的な供給者(市場賃料を払う)」の
損益分岐で決まり、Oracle はリースの賃料差の分だけ超過利益を得る(価値連鎖の優位: 逼迫前に長期で敷地を押さえた)。
変更点(第1版から):
- 新規契約の単価は「契約を結んだ年 = 稼働年 − sign_lag」の相場で決める(先行契約 95%、OpenAI は 2025 年締結・2027 年開始)
- 需給が緩んだ後の新規単価は、損益分岐単価(参照条件で計算し、シナリオの再契約前提とは切り離す)を基準に、
  緩和直後の trough_years 年は損益分岐 × trough_mult(値崩れの谷)、その後は損益分岐 + 長期超過 s_eq
  (trough_years = 0 のときは F 年かけてフェード)
- 稼働率: 契約期間 util_c、契約後は逼迫期 util_post_tight・緩和期 util_post_loose
- 緩和期の建設(成長・置き換えとも)は新規 NPV ≥ 0 のときだけ。リース済みの敷地(計画の最大値)が空けば遊休賃料
- 退役は最適停止(今置き換える価値 − 1年待つ価値 > 旧コホートの1年分の税引後現金)、赤字、上限 L_max
単位: 10億ドル、GW、年度は整数(27 = FY27)。
"""


def lease_mkt(y, p):
    g = 1.0
    for s_ in range(28, y + 1):
        g *= 1 + (p['rent_g_tight'] if s_ < p['Y_star'] else p['rent_g_loose'])
    return p['L0'] * g


def lease_or(y, p):
    if y > p['lease_end']:
        return lease_mkt(y, p)
    return p['L0'] * (1 + p['e_lease']) ** (y - 27)


def other_cost(y, p):
    return p['O0'] * (1 + p['cash_esc']) ** (y - 27)


def cost_or(y, p):
    return lease_or(y, p) + other_cost(y, p)


def cost_mkt(y, p):
    return lease_mkt(y, p) + other_cost(y, p)


def xcost(v, y, p):
    """第4.4版: 世代 v の追加の現金費用(1GW・年)。会社の 1GW 例(粗利率 35%)と、エンジンの賃料・電力の差"""
    f = p.get('gen_xcost')
    return f(v) * (1 + p['cash_esc']) ** max(0, y - v) if f else 0.0


def ramp(a, p):
    """第4.5版: 稼働 a 年目の売上の比率(満稼働 = 1)"""
    return (1 - p['lag']) if a == 0 else (p.get('ramp1', 1.0) if a == 1 else 1.0)


def dep_frac(a, p):
    """第4.5版: 償却の比率(K/acct を 1 とする)。ramp_dep なら稼働の割合に合わせて始め、合計 acct 年分で止める"""
    acct = p['acct_life']
    if not p.get('ramp_dep'):
        return (0.5 if a == 0 else 1.0) if a < acct else (0.5 if a == acct else 0.0)
    sched, tot, k = [], 0.0, 0
    while tot < acct - 1e-9:
        x = 0.5 * ramp(0, p) if k == 0 else (ramp(k, p) if k == 1 else 1.0)
        x = min(x, acct - tot); sched.append(x); tot += x; k += 1
    return sched[a] if a < len(sched) else 0.0


def crf(r, n):
    return r / (1 - (1 + r) ** -n) if r > 0 else 1 / n


def cohort_npv_at_price(P, K, y0, cost_fn, r, p, post_rho, post_dec, util_post):
    """単価 P で y0 年に稼働する新規コホート 1GW の NPV(稼働年の期首時点)。cost_fn(年) は 1GW の現金費用"""
    tax, u, Lc, Lmax, acct = p['tax'], p['util_c'], p['contract_len'], p['L_max'], p['acct_life']
    npv = -K * (1 + r) ** 0.5
    for a in range(0, Lmax + 1):
        w = 0.5 if a in (0, Lmax) else 1.0
        if a <= Lc:
            rev = P * u * w * ramp(a, p)
        else:
            price = P * post_rho * (1 - post_dec) ** (a - Lc - 1)
            if price * util_post < cost_fn(y0 + a):
                break
            rev = price * util_post * w
        cost = cost_fn(y0 + a) * w + (p['startup'] * cost_fn(y0) if a == 0 else 0.0)
        da = K / acct * (0.5 if a == 0 else 1.0) if a < acct else (K / acct * 0.5 if a == acct else 0.0)
        ebit = rev - cost - da
        npv += (ebit * (1 - tax) + da) / (1 + r) ** (a + 0.5)
    return npv


def breakeven_price(K, y0, r, p, excess=0.0):
    """限界的な供給者(市場賃料を払う)が、参照条件(緩和後の再契約 rho_ref・dec_ref・util_ref)で NPV = excess × K となる単価"""
    lo, hi = 0.1, 80.0
    cf = lambda yy: cost_mkt(yy, p) + xcost(y0, yy, p)          # 第4.4版: 追加費用も含める
    for _ in range(60):
        mid = (lo + hi) / 2
        if cohort_npv_at_price(mid, K, y0, cf, r, p, p['rho_ref'], p['dec_ref'], p['util_ref']) > excess * K:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def post_price(c, y, p):
    Lc = p['contract_len']
    a = y - c['v']
    if a <= Lc:
        return c['P']
    first = c['v'] + Lc + 1
    rho = p['post_rho_tight'] if first < p['Y_star'] else p['post_rho_loose']
    price = c['P'] * rho
    for s in range(first + 1, y + 1):
        price *= (1 - (p['post_dec_tight'] if s < p['Y_star'] else p['post_dec_loose']))
    return price


def util_at(c, y, p):
    a = y - c['v']
    if a <= p['contract_len']:
        return p['util_c']
    return p['util_post_tight'] if y < p['Y_star'] else p['util_post_loose']


def make_pricer(p, r_of_year):
    cache = {}

    def price_new(y):
        """y 年に稼働するコホートの契約単価・投資・現金費用"""
        if y in cache:
            return cache[y]
        C_y = cost_or(y, p)
        P_gen, K = p['gen_price'](y), p['gen_capex'](y)
        s = y - p['sign_lag']
        if s < p['Y_star']:
            P = P_gen
        else:
            r = r_of_year(y)
            k = s - p['Y_star']
            if p['trough_years'] > 0 and k < p['trough_years']:
                P = breakeven_price(K, y, r, p, 0.0) * p['trough_mult']
            else:
                seq = p['s_eq']
                if p.get('s_eq_years') is not None and k >= p['s_eq_years']:
                    seq = p.get('s_eq_after', 0.0)
                P_be = breakeven_price(K, y, r, p, seq)
                if p['trough_years'] == 0 and p['F'] > 0 and k < p['F'] and P_gen > P_be:
                    P = P_be + (P_gen - P_be) * (1 - (k + 1) / p['F'])
                else:
                    P = P_be
        cache[y] = (P, K, C_y)
        return cache[y]

    def new_npv(y):
        P, K, C_y = price_new(y)
        tight_after = (y + p['contract_len'] + 1) < p['Y_star']
        rho = p['post_rho_tight'] if tight_after else p['post_rho_loose']
        dec = p['post_dec_tight'] if tight_after else p['post_dec_loose']
        up = p['util_post_tight'] if tight_after else p['util_post_loose']
        return cohort_npv_at_price(P, K, y, lambda yy: cost_or(yy, p) + xcost(y, yy, p), r_of_year(y), p, rho, dec, up)

    def new_npv_sunk(y):
        """借りたまま空いている敷地に建てる場合: 賃料は埋没。機会費用は転貸で回収できた分(sublease)だけ"""
        P, K, C_y = price_new(y)
        tight_after = (y + p['contract_len'] + 1) < p['Y_star']
        rho = p['post_rho_tight'] if tight_after else p['post_rho_loose']
        dec = p['post_dec_tight'] if tight_after else p['post_dec_loose']
        up = p['util_post_tight'] if tight_after else p['util_post_loose']
        cf = lambda yy: (lease_or(yy, p) * p.get('sublease', 0.0) if yy <= p['lease_end'] else lease_or(yy, p)) + other_cost(yy, p) + xcost(y, yy, p)
        return cohort_npv_at_price(P, K, y, cf, r_of_year(y), p, rho, dec, up)
    def new_npv_mkt(y):
        """計画外の新しい敷地を y 年に市場賃料で借りて建てる場合(第4.3版)"""
        P, K, C_y = price_new(y)
        tight_after = (y + p['contract_len'] + 1) < p['Y_star']
        rho = p['post_rho_tight'] if tight_after else p['post_rho_loose']
        dec = p['post_dec_tight'] if tight_after else p['post_dec_loose']
        up = p['util_post_tight'] if tight_after else p['util_post_loose']
        cf = lambda yy: lease_mkt(y, p) * (1 + p['e_lease']) ** (yy - y) + other_cost(yy, p) + xcost(y, yy, p)
        return cohort_npv_at_price(P, K, y, cf, r_of_year(y), p, rho, dec, up)
    return price_new, new_npv, new_npv_sunk, new_npv_mkt


def run_ai(p, years, r_of_year):
    Lc, Lmax, acct, tax = p['contract_len'], p['L_max'], p['acct_life'], p['tax']
    plan = p['gw_plan']
    price_new, new_npv, new_npv_sunk, new_npv_mkt = make_pricer(p, r_of_year)
    npv_cache = {}
    sunk_cache = {}
    mkt_cache = {}
    tranches = []                                   # 第4.3版: 計画外に市場賃料で借りた敷地 (年, GW)

    def nnpv(y):
        if y not in npv_cache:
            npv_cache[y] = new_npv(y)
        return npv_cache[y]

    cohorts = [dict(v=v, gw=g, P=P, K=K, ret=None) for v, g, P, K in p['initial']]
    out = {}
    prev_target = sum(c['gw'] for c in cohorts)
    sites = prev_target
    first_plan_year = min(plan)
    for y in years:
        r = r_of_year(y)
        P_new, K_new, C_y = price_new(y)
        loose_sign = (y - p['sign_lag']) >= p['Y_star']
        # ---- 退役
        retire_gw = 0.0
        for c in cohorts:
            if c['ret'] is not None or c['v'] >= y:
                continue
            a = y - c['v']
            price = post_price(c, y, p)
            if p.get('rev_mod'):
                price = p['rev_mod'](c, y, price, p)
            u = util_at(c, y, p)
            reason = None
            if a >= Lmax:
                reason = 'L_max'
            elif a > Lc and price * u < (other_cost(y, p) + xcost(c['v'], y, p) + p.get('sublease', 0.0) * lease_or(y, p) if y <= p['lease_end'] else C_y + xcost(c['v'], y, p)):
                reason = '赤字'                      # 第4.3版: 賃料は埋没。回避できる費用で判定(建設の判定とそろえる)
            elif a > Lc and nnpv(y) > 0:
                m_old = (price * u - C_y - xcost(c['v'], y, p)) * (1 - tax)
                if nnpv(y) - nnpv(y + 1) / (1 + r) > m_old:
                    reason = '置換'
            if reason:
                c['ret'] = y
                c['why'] = reason
                retire_gw += c['gw']
        # ---- 建設
        if y in plan:
            target = plan[y]
        elif y > max(plan):
            target = prev_target * (1 + p['g_cap'](y))
        else:
            target = prev_target
        prev_target = target
        if y <= p['lease_end'] and y <= max(plan):
            sites = max(sites, target, p.get('sites_committed', {}).get(y, 0.0))   # 第4.3版: 契約済みの敷地も含める
        current = sum(c['gw'] for c in cohorts if c['ret'] is None and c['v'] <= y)
        builds = max(0.0, target - current)
        if y >= first_plan_year and builds > 0:
            in_site = min(builds, max(0.0, sites - current))              # 借りて空いている敷地に建てる分
            new_site = builds - in_site
            if loose_sign:
                if y not in sunk_cache:
                    sunk_cache[y] = new_npv_sunk(y)
                if y not in mkt_cache:
                    mkt_cache[y] = new_npv_mkt(y) if y > max(plan) else nnpv(y)
                in_site = in_site if sunk_cache[y] >= 0 else 0.0             # 賃料は埋没: 転貸の機会費用だけで判定
                new_site = new_site if mkt_cache[y] >= 0 else 0.0           # 新しい敷地: 計画外は市場賃料を払う前提で判定
                builds = in_site + new_site
            if y > max(plan) and new_site > 0 and y <= p['lease_end']:
                tranches.append((y, new_site))
                sites += new_site
            cohorts.append(dict(v=y, gw=builds, P=P_new, K=K_new, ret=None))
        alive_end = sum(c['gw'] for c in cohorts if c['ret'] is None and c['v'] <= y)
        out[y] = dict(year=y, P_new=P_new, K=K_new, C=C_y, builds=builds, retire=retire_gw, loose=y >= p['Y_star'], alive_end=alive_end,
                      loose_sign=loose_sign, r=r, target=target, sites=sites, npv_new=nnpv(y))
    for y in years:
        rev = cost = da = capex = gw_w = 0.0
        ages = []
        for c in cohorts:
            v, g = c['v'], c['gw']
            if g <= 0:
                continue
            if y == v - 1:
                capex += 0.5 * c['K'] * g
            if y == v:
                capex += 0.5 * c['K'] * g
            a = y - v
            end = c['ret']
            if a < 0 or (end is not None and y > end):
                continue
            w = 0.5 if a == 0 else 1.0
            if end is not None and y == end:
                w = 0.5
            price = c['P'] if a <= Lc else post_price(c, y, p)
            if p.get('rev_mod'):
                price = p['rev_mod'](c, y, price, p)
            lag = ramp(a, p)
            rev += price * util_at(c, y, p) * g * w * lag
            uf = lag if p.get('ramp_cost') else 1.0
            cost += (lease_or(y, p) + (other_cost(y, p) + xcost(v, y, p)) * uf) * g * w
            if a == 0:
                cost += p['startup'] * cost_or(y, p) * g
            da += c['K'] * g / acct * dep_frac(a, p)
            gw_w += g * w
            ages.append((a, g * w))
        # 次の年に稼働するコホートの前年 capex(計算期間の最終年の翌年分)
        plan_sites = max(p['gw_plan'].values())
        beyond = max(0.0, gw_w - max(plan_sites, max(p.get('sites_committed', {0: 0}).values())))
        extra_rent = 0.0
        for s_, g_ in tranches:
            if s_ > y or beyond <= 0 or y > p['lease_end']:
                continue
            take = min(g_, beyond)
            beyond -= take
            extra_rent += take * (lease_mkt(s_, p) * (1 + p['e_lease']) ** (y - s_) - lease_or(y, p))
        cost += extra_rent
        idle = max(0.0, out[y]['sites'] - out[y]['alive_end']) if y <= p['lease_end'] else 0.0
        idle_cost = idle * lease_or(y, p) * (1 - p.get('sublease', 0.0))
        cost += idle_cost
        ebit = rev - cost - da
        nopat = ebit * (1 - tax)
        out[y].update(rev=rev, cash_cost=cost, idle_cost=idle_cost, idle_gw=idle, da=da, ebit=ebit, ebitda=rev - cost,
                      nopat=nopat, capex=capex, fcf=nopat + da - capex, gw_in_service=gw_w,
                      margin=ebit / rev if rev else float('nan'),
                      avg_age=(sum(a * w for a, w in ages) / sum(w for _, w in ages)) if ages else 0.0)
    return out, cohorts


def cohort_life(c, p, r_of_year):
    Lc, acct, tax = p['contract_len'], p['acct_life'], p['tax']
    end = c['ret'] if c['ret'] is not None else c['v'] + p['L_max']
    cfs = [(c['v'] - 1, -0.5 * c['K']), (c['v'], -0.5 * c['K'])]
    rev_t = cost_t = da_t = 0.0
    for y in range(c['v'], end + 1):
        a = y - c['v']
        w = 0.5 if a == 0 or y == end else 1.0
        price = c['P'] if a <= Lc else post_price(c, y, p)
        if p.get('rev_mod'):
            price = p['rev_mod'](c, y, price, p)
        rev = price * util_at(c, y, p) * w * ramp(a, p)
        uf = ramp(a, p) if p.get('ramp_cost') else 1.0
        cost = (lease_or(y, p) + (other_cost(y, p) + xcost(c['v'], y, p)) * uf) * w + (p['startup'] * cost_or(y, p) if a == 0 else 0.0)
        da = c['K'] / acct * dep_frac(a, p)
        ebit = rev - cost - da
        cfs.append((y, ebit * (1 - tax) + da))
        rev_t += rev; cost_t += cost; da_t += da

    def npv(rate):
        return sum(cf / (1 + rate) ** (y - c['v']) for y, cf in cfs)
    lo, hi = -0.9, 2.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if npv(mid) > 0:
            lo = mid
        else:
            hi = mid
    cum, payback = 0.0, None
    for y, cf in cfs:
        cum += cf
        if payback is None and cum >= 0 and y >= c['v']:
            payback = y - c['v']
    return dict(v=c['v'], gw=c['gw'], P=c['P'], K=c['K'], life=end - c['v'], why=c.get('why'), irr=(lo + hi) / 2,
                npv_per_K=npv(r_of_year(c['v'])) / c['K'], margin_life=(rev_t - cost_t - da_t) / rev_t if rev_t else float('nan'),
                payback=payback)
