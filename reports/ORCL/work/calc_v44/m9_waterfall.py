# 第4.3版 → 第4.4版の理論株価(確率加重)の変化を、変更を1つずつ足して分解する
import json, copy
import model9 as M
import m9_engine_fwd as F
import m9_fair as FR

OLD_PLAN = {27: 4.7, 28: 7.4, 29: 11.5, 30: 14.0, 31: 16.0, 32: 18.0}
NEW_PLAN = dict(M.AI_BASE['gw_plan'])
rf_new = M.rf_path
rf_old = lambda kind='market': (lambda y: 0.050 if y <= 28 else (0.0525 if y <= 31 else (0.054 if y <= 36 else 0.056))) if kind == 'market' else rf_new(kind)


def scen_mod(st):
    def mod(q):
        nm = q['name']
        s = {'強気': 0.15, '弱気': -0.15}.get(nm, 0.0)
        plan = NEW_PLAN if st['plan'] else OLD_PLAN
        d = {y: v * M.SC_MULT(y, s) for y, v in plan.items()}
        q['ai'].update(gw_plan=d, sites_committed=dict(plan) if nm == '弱気' else dict(d))
        if not st['econ']:
            g = {'強気': 1.065, '弱気': 1.035}.get(nm, 1.05)
            q['ai'].update(contract_len=6, gen_price=lambda y, g=g: 11.5 * g ** max(0, y - 27), gen_capex=lambda y: 30.0 * 1.04 ** max(0, y - 27))
        if not st['xcost']:
            q['ai'].update(gen_xcost=None)
        if not st['fund']:
            q.update(cust_fund={27: 0.24}, cust_fund_tight=0.24, eq_raise=None, bb_start=0)
    return mod


def value(st):
    M.rf_path = rf_new if st['mkt'] else rf_old
    mod = scen_mod(st)
    keep = copy.deepcopy(M.BASE)
    mod(M.BASE)
    swm = M.calibrate_sw_to_guidance()
    M.BASE.clear(); M.BASE.update(keep)
    A = {}
    for sc in (M.BASE, M.BULL, M.BEAR):
        q = F.setup(sc); mod(q)
        r, f = F.forward_values(q, swm)
        A[sc['name']] = dict(vps=r['vps'], f=json.loads(json.dumps(f, default=float)), seg_ev={k: r['seg_val'][k]['ev'] for k in M.SEGS})
    FR.A = A
    FR.PRICE = 139.56 if st['mkt'] else 143.20
    FR.T0 = 0.584 if st['mkt'] else 0.622
    rf_e = 0.0502 if st['mkt'] else 0.052
    r_e = rf_e + FR.r_equity(FR.PRICE)[2] * 0.0423
    if not st['mkt']:
        FR.CONS.update({27: 8.06, 28: 10.93, 29: 15.78, 30: 20.53})
    else:
        FR.CONS.update({27: 8.14, 28: 10.99, 29: 15.77, 30: 20.53})
    tot, vals = FR.weighted(r_e=r_e, eps_src='company' if st['eps'] else 'cons')
    dcf = 0.5 * A['ベース']['vps'] + 0.25 * A['強気']['vps'] + 0.25 * A['弱気']['vps']
    return tot, vals, dcf, r_e


steps = [('第4.3版の再現', {}), ('株価・金利・日付(139.56、10年 5.02%)', dict(mkt=1)), ('会社の容量計画(FY28 末 8.7GW、FY30 9.5GW)', dict(plan=1)),
         ('会社の 1GW 例の単価・capex・BYOH 20%・契約 5 年', dict(econ=1)), ('粗利率 35% に合う現金費用', dict(xcost=1)),
         ('資金(前払い 17%→10%・株式 100 億ドル・買い戻しは FY31 から)', dict(fund=1)), ('EPS の起点をコンセンサスから会社の見通しへ', dict(eps=1))]
st = dict(mkt=0, plan=0, econ=0, xcost=0, fund=0, eps=0)
rows, prev = [], None
for lab, ch in steps:
    st.update(ch)
    tot, vals, dcf, r_e = value(st)
    d = None if prev is None else (tot - prev[0], dcf - prev[1])
    rows.append(dict(step=lab, total=tot, base=vals['ベース'], bull=vals['強気'], bear=vals['弱気'], dcf=dcf, r_e=r_e,
                     d_total=d[0] if d else 0.0, d_dcf=d[1] if d else 0.0))
    print('%-52s 加重 %6.1f(%+5.1f)ベース %6.1f 強気 %6.1f 弱気 %6.1f | DCF %6.1f(%+5.1f) r_e %.2f%%' % (
        lab, tot, d[0] if d else 0, vals['ベース'], vals['強気'], vals['弱気'], dcf, d[1] if d else 0, r_e * 100))
    prev = (tot, dcf)
json.dump(rows, open('out/m9_waterfall.json', 'w'), ensure_ascii=False, indent=1)
