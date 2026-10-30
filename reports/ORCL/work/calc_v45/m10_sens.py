# 第4.5版: 利用者の指摘に対応する感応度(全シナリオに同じ変更)
import json, copy
import model10 as M
import m10_engine_fwd as F
import m10_fair as FR
A0 = json.load(open('out/m10_all.json')); swm = A0['swm']
F10 = json.load(open('out/m10_fair.json')); TOT, DCF = F10['total'], F10['dcf']


def build_A(mod):
    A = {}
    for sc in (M.BASE, M.BULL, M.BEAR):
        q = F.setup(sc); mod(q)
        r, f = F.forward_values(q, swm)
        A[sc['name']] = dict(vps=r['vps'], f=json.loads(json.dumps(f, default=float)), seg_ev={k: r['seg_val'][k]['ev'] for k in M.SEGS}, path=r['path'])
    return A


def plan_shift(d28, d29=0.0):
    def m(q):
        g = dict(q['ai']['gw_plan']); g[28] += d28; g[29] += d29
        q['ai'].update(gw_plan=g)
    return m


def add_list(key, add, i0, i1):
    def m(q):
        q[key] = [g + (add if i0 <= i <= i1 else 0.0) for i, g in enumerate(q[key])]
    return m


cases = [
    ('ERP・業務アプリの OCI 移行が後半に加速(OCI 一般 FY31〜40 +3pt、SaaS FY30〜35 +2pt)',
     lambda q: (add_list('g_ocin', 0.03, 4, 13)(q), add_list('g_saas', 0.02, 3, 8)(q))),
    ('企業向け OCI の利益率 FY32 に 45%(ベース 38%)', lambda q: q.update(m_ocin=(q['m_ocin'][0], q['m_ocin'][1] + 0.07, 5))),
    ('推論とデータの重力: 緩和後の再契約 75%・下落 10%/年・長期超過 +5pt', lambda q: q['ai'].update(post_rho_loose=0.75, post_dec_loose=0.10, s_eq=q['ai']['s_eq'] + 0.05)),
    ('経営者の発言どおり: 再契約は同じ単価(緩和後も 100%・下落 3%/年)', lambda q: q['ai'].update(post_rho_loose=1.0, post_dec_loose=0.03)),
    ('建設の遅れ: FY28 の追加のうち 1.5GW が 1 年遅れる', plan_shift(-1.5)),
    ('建設の遅れ: FY28 の追加 3.5GW がすべて 1 年遅れる', plan_shift(-3.5)),
    ('社債の金利 +1pt(新発の上乗せが続く)', lambda q: q.update(rate_debt=[x + 0.01 for x in q['rate_debt']])),
    ('社債の金利 +2pt', lambda q: q.update(rate_debt=[x + 0.02 for x in q['rate_debt']])),
]
out = {}
for lab, mod in cases:
    A = build_A(mod)
    keep = FR.A; FR.A = A
    tot, vals = FR.weighted()
    FR.A = keep
    dcf = 0.5 * A['ベース']['vps'] + 0.25 * A['強気']['vps'] + 0.25 * A['弱気']['vps']
    P = {x['year']: x for x in A['ベース']['path']}
    out[lab] = dict(total=tot, dcf=dcf, d_total=tot - TOT, d_dcf=dcf - DCF, rev30=P[30]['rev'], fcf29=P[29]['fcf'], eps30=A['ベース']['f']['eps']['30'],
                    rating_min=min((P[y]['rating'] for y in range(27, 33)), key=['BB', 'BB+', 'BBB-', 'BBB', 'BBB+'].index))
    print('%-62s 加重 %.1f(%+.1f)DCF %.1f(%+.1f)| FY30 売上 %.0f EPS %.2f FY29 FCF %.0f 最低格付け %s' % (
        lab, tot, tot - TOT, dcf, dcf - DCF, P[30]['rev'], A['ベース']['f']['eps']['30'], P[29]['fcf'], out[lab]['rating_min']))
json.dump(out, open('out/m10_sens.json', 'w'), ensure_ascii=False, indent=1, default=float)
