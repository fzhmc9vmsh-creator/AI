# 第4.4版の補足計算: 変更の分解(第4.3版→第4.4版)、感応度(更新・逼迫・容量・費用・金利)、確率、条件6、3経路の乖離、エントリー、CDS
import json, copy, math
import model9 as M
import m9_engine_fwd as F
import m9_fair as FR
A0 = json.load(open('out/m9_all.json')); swm = A0['swm']
PRICE = FR.PRICE
out = {}


def build_A(mod_all=None, mods=None):
    A = {}
    for sc in (M.BASE, M.BULL, M.BEAR):
        q = F.setup(sc)
        if mod_all:
            mod_all(q)
        if mods and sc['name'] in mods:
            mods[sc['name']](q)
        r, f = F.forward_values(q, swm)
        A[sc['name']] = dict(vps=r['vps'], f={k: {int(kk): vv for kk, vv in v.items()} for k, v in json.loads(json.dumps(f, default=float)).items()},
                             seg_ev={k: r['seg_val'][k]['ev'] for k in M.SEGS}, path=r['path'])
    return A


def weighted_with(A, r_e=None, **kw):
    keep = FR.A
    FR.A = A
    tot, vals = FR.weighted(r_e=r_e, **kw)
    dcf = 0.5 * A['ベース']['vps'] + 0.25 * A['強気']['vps'] + 0.25 * A['弱気']['vps']
    FR.A = keep
    return tot, vals, dcf


F9 = json.load(open('out/m9_fair.json'))
TOT, DCF = F9['total'], F9['dcf']
# 1. 感応度(全シナリオに同じ変更を加え、理論株価と DCF を出し直す)
sens = {}
cases = [
    ('契約後の更新単価 +20%(会社: 4年前の GPU を +20% で更新)', lambda q: q['ai'].update(post_rho_tight=1.2, post_rho_loose=q['ai']['post_rho_loose'] * 1.2)),
    ('契約後の更新単価 −20%', lambda q: q['ai'].update(post_rho_tight=0.8, post_rho_loose=q['ai']['post_rho_loose'] * 0.8)),
    ('逼迫の終わり +2年', lambda q: q['ai'].update(Y_star=q['ai']['Y_star'] + 2)),
    ('逼迫の終わり −2年', lambda q: q['ai'].update(Y_star=q['ai']['Y_star'] - 2)),
    ('契約期間 6年(第4.3版)', lambda q: q['ai'].update(contract_len=6)),
    ('追加費用なし(粗利率 35% を使わない)', lambda q: q['ai'].update(gen_xcost=None)),
    ('BYOH 0%(全て自己資金)', None),
    ('容量: FY30 売上 225 に合わせる(FY29 9.2・FY30 11.0・FY31 13.0・FY32 15.0GW)', 'plan_co'),
    ('容量: 第4.3版の計画(FY29 11.5・FY30 14・FY31 16・FY32 18GW)', 'plan_43'),
    ('容量: FY30 以降 年 3.5GW 追加', 'plan_35'),
    ('前払い: FY28 以降 5%', lambda q: q.update(cust_fund={27: 0.24, 28: 0.05}, cust_fund_tight=0.05)),
    ('株式調達なし', lambda q: q.update(eq_raise=None)),
]
PLANS = {'plan_co': {27: 4.7, 28: 8.7, 29: 9.2, 30: 11.0, 31: 13.0, 32: 15.0},
         'plan_43': {27: 4.7, 28: 8.7, 29: 11.5, 30: 14.0, 31: 16.0, 32: 18.0},
         'plan_35': {27: 4.7, 28: 8.7, 29: 9.0, 30: 12.5, 31: 16.0, 32: 19.5}}


def byoh0(q):
    rev, K = 16.0, 37.0
    X = 16.0 * 0.65 - 37.0 / 6 - 2.7
    P = rev / 0.975
    g = 0.03
    q['ai'].update(gen_price=lambda y: P * (1 + g) ** max(0, y - 28), gen_capex=lambda y: K * (1 + g) ** max(0, y - 28),
                   gen_xcost=lambda v: X * 1.025 ** (v - 27) if v >= 27 else 0.0)


for lab, mod in cases:
    if mod is None:
        mod = byoh0
    elif isinstance(mod, str):
        d = PLANS[mod]

        def mod(q, d=d, k=mod):
            s = 1.0
            nm = q['name']
            if nm == '強気':
                d2 = {y: v * M.SC_MULT(y, 0.15) for y, v in d.items()}
            elif nm == '弱気':
                d2 = {y: v * M.SC_MULT(y, -0.15) for y, v in d.items()}
            else:
                d2 = dict(d)
            q['ai'].update(gw_plan=d2, sites_committed=dict(d) if nm == '弱気' else dict(d2))
    A = build_A(mod)
    tot, vals, dcf = weighted_with(A)
    P = {x['year']: x for x in A['ベース']['path']}
    eps = A['ベース']['f']['eps']
    sens[lab] = dict(total=tot, dcf=dcf, base=vals['ベース'], d_total=tot - TOT, d_dcf=dcf - DCF,
                     rev30=P[30]['rev'], fcf29=P[29]['fcf'], eps30=eps[30], fcf33=P[33]['fcf'])
    print('%-58s 加重 %.1f(%+.1f)DCF %.1f(%+.1f)| ベース FY30 売上 %.0f EPS %.2f FY29 FCF %.0f FY33 FCF %.0f' % (
        lab, tot, tot - TOT, dcf, dcf - DCF, P[30]['rev'], eps[30], P[29]['fcf'], P[33]['fcf']))
out['sens'] = sens
# 2. シナリオ確率
v = F9['vals']
prob = {}
for pb in (0.15, 0.25, 0.35, 0.50, 0.75):
    rest = 1 - pb
    w = rest * (2 / 3) * v['ベース'] + rest * (1 / 3) * v['強気'] + pb * v['弱気']
    prob[pb] = w
    print('弱気 %.0f%%: 理論株価 %.1f(株価比 %+.0f%%)' % (pb * 100, w, (w / PRICE - 1) * 100))
out['prob'] = prob
# 3. 条件6: 事業実態 EPS の5年 CAGR(3経路)
nongC, coreC = FR.eps_paths('ベース', 'company')
nongS, coreS = FR.eps_paths('ベース', 'cons')
eng = A0['ベース']['f']
eng_core = {int(k): x for k, x in eng['eps_core'].items()}
c6 = {}
for lab, e in (('会社', coreC), ('コンセンサス', coreS), ('需給エンジン', eng_core)):
    cagr = (e[32] / e[27]) ** (1 / 5) - 1
    per = PRICE / e[27]
    c6[lab] = dict(e27=e[27], e32=e[32], cagr=cagr, per=per, peg=per / (cagr * 100))
    print('条件6 %-8s 事業実態EPS FY27 %.2f → FY32 %.2f CAGR %.1f%% PER %.1f PEG %.2f' % (lab, e[27], e[32], cagr * 100, per, per / (cagr * 100)))
out['c6'] = c6
# 4. 3経路の乖離
gaps = dict(company=TOT, consensus=FR.weighted(eps_src='cons')[0], engine=FR.weighted(eps_src='engine')[0], dcf=DCF)
for k, x in gaps.items():
    print('乖離 %-10s %.1f → %+.0f%%' % (k, x, (x / PRICE - 1) * 100))
out['gaps'] = gaps
# 5. エントリー(構造評価 B: α = 25%)
B, U, L = F9['res']['ベース']['value'], F9['res']['強気']['value'], F9['res']['弱気']['value']
a = 0.25
z1 = min(B * (1 - a), L * (1 + a / 2)); z2 = B * (1 - a / 2)
zone = '見送り圏' if PRICE > z2 else ('分割エントリー圏' if PRICE > z1 else '即エントリー圏')
out['entry'] = dict(B=B, U=U, L=L, alpha=a, Z1=z1, Z2=z2, zone=zone, z1a=B * (1 - a), z1b=L * (1 + a / 2))
print('エントリー: B %.1f U %.1f L %.1f | Z1 = min(%.1f, %.1f) = %.1f | Z2 = %.1f | 株価 %.2f → %s' % (B, U, L, B * (1 - a), L * (1 + a / 2), z1, z2, PRICE, zone))
# 6. 信用: CDS 277bp(2026-10-28)のリスク中立の倒産確率と、モデルの倒産確率
h = 0.0277 / 0.6
pd5_cds = 1 - math.exp(-5 * h)
surv = {int(k): x for k, x in A0['ベース']['f']['surv'].items()}
pd5_model = 1 - surv[31]
out['credit'] = dict(cds=277, hazard=h, pd5_cds=pd5_cds, pd5_model=pd5_model, pd45_model=1 - surv[45])
# CDS の倒産確率をそのまま使うと(5年)、全シナリオの1株価値(存続時)に掛ける
vgc = {n: None for n in ('ベース', '強気', '弱気')}
dcf_cds = 0.0
for sc in (M.BASE, M.BULL, M.BEAR):
    q = F.setup(sc); q['sw_margin'] = swm
    r = M.run(q)
    after = (1 - r['pd_cum']) / (1 - pd5_model if sc is M.BASE else 1 - (1 - {x['year']: x for x in r['path']}[31]['surv']))
    vgc[sc['name']] = r['vps_gc'] * (1 - pd5_cds) * after
    dcf_cds += vgc[sc['name']] * sc['prob']
out['credit'].update(dcf_cds=dcf_cds)
print('CDS 277bp: リスク中立の5年倒産確率 %.1f%%(モデル %.1f%%、FY45 まで %.1f%%)→ DCF 加重 %.1f(モデル %.1f)' % (
    pd5_cds * 100, pd5_model * 100, (1 - surv[45]) * 100, dcf_cds, DCF))
json.dump(out, open('out/m9_extra.json', 'w'), ensure_ascii=False, indent=1, default=float)
