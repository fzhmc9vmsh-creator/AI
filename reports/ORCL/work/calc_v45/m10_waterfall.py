# 第4.4版 → 第4.5版の分解(後ろから 1 つずつ外す)
import json, copy
import model10 as M, m10_engine_fwd as F, m10_fair as FR
PLAN44 = {27: 4.7, 28: 8.7, 29: 9.0, 30: 9.5, 31: 12.0, 32: 14.0}
RHO = {'ベース': (0.60, 0.15), '強気': (0.70, 0.10), '弱気': (0.50, 0.20)}
ERPK = {'ベース': -1.0, '強気': -2.0, '弱気': 1.0}
def mod(st):
    def m(q):
        nm = q['name']
        if not st['dg']:
            q['ai'].update(post_rho_loose=RHO[nm][0], post_dec_loose=RHO[nm][1])
        if not st['erp']:
            M.erp_boost(q, ERPK[nm])
        if not st['ramp']:
            s = {'強気': 0.15, '弱気': -0.15}.get(nm, 0.0)
            d = {y: v * M.SC_MULT(y, s) for y, v in PLAN44.items()}
            q['ai'].update(lag=0.30, ramp1=1.0, ramp_cost=False, ramp_dep=False, gw_plan=d, sites_committed=dict(PLAN44) if nm == '弱気' else dict(d))
    return m
def value(st):
    m = mod(st)
    keep = copy.deepcopy(M.BASE); m(M.BASE); swm = M.calibrate_sw_to_guidance(); M.BASE.clear(); M.BASE.update(keep)
    A = {}
    for sc in (M.BASE, M.BULL, M.BEAR):
        q = F.setup(sc); m(q)
        r, f = F.forward_values(q, swm)
        A[sc['name']] = dict(vps=r['vps'], f=json.loads(json.dumps(f, default=float)), seg_ev={k: r['seg_val'][k]['ev'] for k in M.SEGS})
    FR.A = A
    tot, vals = FR.weighted()
    return tot, 0.5 * A['ベース']['vps'] + 0.25 * A['強気']['vps'] + 0.25 * A['弱気']['vps'], vals
rows = []
for lab, st in [('第4.4版の再現', dict(dg=0, erp=0, ramp=0)), ('売上・費用・償却の 2 年の立ち上げと容量の時期', dict(dg=0, erp=0, ramp=1)),
                ('ERP・業務アプリの OCI 移行の加速', dict(dg=0, erp=1, ramp=1)), ('推論とデータの重力(緩和後の再契約 70%・下落 12%)', dict(dg=1, erp=1, ramp=1))]:
    tot, dcf, vals = value(st)
    rows.append(dict(step=lab, total=tot, dcf=dcf, base=vals['ベース'], bull=vals['強気'], bear=vals['弱気']))
    print('%-40s 加重 %.1f DCF %.1f(%.1f / %.1f / %.1f)' % (lab, tot, dcf, vals['ベース'], vals['強気'], vals['弱気']))
json.dump(rows, open('out/m10_waterfall.json', 'w'), ensure_ascii=False, indent=1)
