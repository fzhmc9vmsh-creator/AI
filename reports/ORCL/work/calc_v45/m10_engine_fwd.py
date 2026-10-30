# -*- coding: utf-8 -*-
"""第4.4版: 株式の調達(FY28)を株数と年度末の価値に入れる。
第4.3版(前払いの請求権を追加)/ 第4.2版: 年度末の1株価値と EPS を、株数の推移(超過 FCF での自社株買いを公正価値で実行)込みで出す。
品質確認 F1/M3: 第4.1版は買い戻しの借入利息だけ EPS から引き、株数を 3.05 で固定していた。"""
import copy, json
import model10 as M

SBC0, SBC_G = 4.6, 0.06


def setup(q):
    return copy.deepcopy(q)          # 第4.5版: 立ち上げの前提は model10 の AI_BASE が正


def forward_values(p, swm, t_last=35):
    p = copy.deepcopy(p); p['sw_margin'] = swm
    r = M.run(p)
    P = {x['year']: x for x in r['path']}
    surv = {x['year']: x['surv'] for x in r['path']}
    eq = {}
    for t in range(27, t_last + 1):
        val = 0.0
        for k in M.SEGS:
            rf = M.coc_fn(p, k)
            last = M.YAI if k == 'ai' else M.YN
            acc = 1.0
            for y in range(t + 1, last + 1):
                rr = rf(y)
                val += r['seg'][k][y]['fcff'] * acc / (1 + rr) ** 0.5
                acc /= (1 + rr)
            val += r['seg_val'][k]['tv'] * acc
        # 第4.3版: 受け取り済みで t より後に取り崩す前払い(現金を伴わない売上)を請求権として引く
        tr = [(M.BS['prepay'], 28)] + [(P[y]['prepay_in'] * (M.STUB if y == M.Y0 else 1.0), y + 1) for y in range(27, t + 1)]
        r_ai = M.coc_fn(p, 'ai')
        pv_pre = 0.0
        for amt, st in tr:
            for k in range(st, st + 5):
                if k > t:
                    pv_pre += amt / 5 / (1 + r_ai(k)) ** (k - t - 0.5)
        e = val + r['shield'] - P[t]['nd'] - M.BS['pref'] - pv_pre
        eq[t] = e * surv[45] / surv[t]                      # t 以降の倒産確率を反映(t までは呼び出し側で)
    # 株数の推移: 年度末に、買い戻し前の1株価値で買い戻す(価値中立)
    # 第4.4版: 株式の調達(年 yr、額 amt、株価 px)。発行前の年度末は調達する現金を足し、発行する株も数える(完全希薄化)
    yr, amt, px = p.get('eq_raise') or (None, 0.0, 1.0)
    N = {26: M.BS['shares']}
    vps = {}
    for t in range(27, t_last + 1):
        bb = P[t]['buyback']
        if yr and t < yr:
            eq[t] += amt / (1 + M.coc_fn(p, 'ai')(yr)) ** (yr - t - 0.5)
        n_prev = N[t - 1] + (amt / px if yr and t == yr else 0.0)
        V = (eq[t] + bb) / n_prev
        N[t] = n_prev - (bb / V if V > 0 else 0.0)
        vps[t] = eq[t] / (N[t] + (amt / px if yr and t < yr else 0.0))
    eps, eps_core = {}, {}
    for y in range(27, t_last + 1):
        x = P[y]; sbc = SBC0 * (1 + SBC_G) ** (y - 27)
        n_avg = (N[y - 1] + N[y]) / 2
        eps[y] = ((x['ebit'] + sbc - x['interest'] + 1.05) * 0.80 - M.BS['pref_div']) / n_avg
        eps_core[y] = ((x['ebit'] - x['interest'] + 1.05) * 0.80 - M.BS['pref_div']) / n_avg     # 事業実態 EPS(株式報酬を費用)
    return r, dict(vps=vps, shares=N, eps=eps, eps_core=eps_core, surv=surv, eq=eq)


if __name__ == '__main__':
    pass                                  # 第4.5版: 立ち上げは AI_BASE のまま
    swm = M.calibrate_sw_to_guidance()
    out = {}
    for sc in (M.BASE, M.BULL, M.BEAR):
        r, f = forward_values(setup(sc), swm)
        P = {x['year']: x for x in r['path']}
        out[sc['name']] = dict(vps=r['vps'], vps_gc=r['vps_gc'], pd=r['pd_cum'], f=f,
                               path={y: dict(rev=P[y]['rev'], ebit=P[y]['ebit'], ebitda=P[y]['ebitda'], da=P[y]['da'], capex=P[y]['capex'],
                                             op=P[y]['op_margin'], fcf=P[y]['fcf'], bb=P[y]['buyback'], nd=P[y]['nd'],
                                             adj=P[y]['adj_lev'], rating=P[y]['rating'], surv=P[y]['surv'], pin=P[y]['prepay_in'])
                                     for y in range(27, 46)},
                               seg_ev={k: r['seg_val'][k]['ev'] for k in M.SEGS}, ev=r['ev'], shield=r['shield'], claims=r['claims'])
        print(sc['name'], 'DCF %.1f PD %.1f%%' % (r['vps'], r['pd_cum'] * 100))
        print('  EPS   ', ' '.join('%d:%.2f' % (y, f['eps'][y]) for y in range(27, 36)))
        print('  core  ', ' '.join('%d:%.2f' % (y, f['eps_core'][y]) for y in range(27, 36)))
        print('  vps   ', ' '.join('%d:%.0f' % (t, f['vps'][t]) for t in range(27, 32)), ' shares', ' '.join('%.2f' % f['shares'][t] for t in range(27, 36)))
        print('  rating', ' '.join(P[y]['rating'] for y in range(27, 36)), ' FCF', ' '.join('%.0f' % P[y]['fcf'] for y in range(27, 33)))
    out['swm'] = swm
    json.dump(out, open('out/m10_all.json', 'w'), ensure_ascii=False, indent=1, default=float)
