# 第4.3版の補足計算: 金利の経路、シナリオ確率、条件6 の3経路、容量感応度の加重効果、最終判断の3経路の乖離
import json, copy
import model8 as M
import m8_engine_fwd as F
import m8_fair as FR
M.BASE['ai']['lag'] = 0.30
A0 = json.load(open('out/m8_all.json')); swm = A0['swm']
PRICE = FR.PRICE
out = {}

def build_A(mod):
    A = {}
    for sc in (M.BASE, M.BULL, M.BEAR):
        q = F.setup(sc); mod(q)
        r, f = F.forward_values(q, swm)
        A[sc['name']] = dict(vps=r['vps'], f={k: {int(kk): vv for kk, vv in v.items()} for k, v in json.loads(json.dumps(f, default=float)).items()},
                             seg_ev={k: r['seg_val'][k]['ev'] for k in M.SEGS})
    return A

def weighted_with(A, r_e):
    keep = FR.A
    FR.A = A
    tot, vals = FR.weighted(r_e=r_e)
    dcf = 0.5 * A['ベース']['vps'] + 0.25 * A['強気']['vps'] + 0.25 * A['弱気']['vps']
    FR.A = keep
    return tot, vals, dcf

# 1. 金利の経路(株主資本コストもそろえる)
r_e0, ba, bl, de = FR.r_equity()
cases = {'市場の曲線(ベース)': ('market', 0.0423, 0.052), '予測どおり低下(5.2→4.2%、ERP 4.5%)': ('normalize', 0.045, 0.045), '高止まり(6.0%)': ('high', 0.0423, 0.060)}
rates = {}
for lab, (kind, erp, rf_e) in cases.items():
    M.ERP = erp
    A = build_A(lambda q, k=kind: q.update(rf=k))
    r_e = rf_e + bl * erp
    tot, vals, dcf = weighted_with(A, r_e)
    rates[lab] = dict(r_e=r_e, weighted=tot, base=vals['ベース'], bull=vals['強気'], bear=vals['弱気'], dcf=dcf)
    print('%-34s r_e %.2f%% 加重 %.1f(ベース %.1f 強気 %.1f 弱気 %.1f)DCF 加重 %.1f' % (lab, r_e * 100, tot, vals['ベース'], vals['強気'], vals['弱気'], dcf))
M.ERP = 0.0423
out['rates'] = rates
# 2. シナリオ確率(強気:ベース = 1:2 固定で弱気の確率を動かす)
F8 = json.load(open('out/m8_fair.json'))
v = F8['vals']
prob = {}
for pb in (0.15, 0.25, 0.35, 0.50, 0.75):
    rest = 1 - pb
    w = rest * (2 / 3) * v['ベース'] + rest * (1 / 3) * v['強気'] + pb * v['弱気']
    prob[pb] = w
    print('弱気 %.0f%%: 理論株価 %.1f(株価比 %+.0f%%)' % (pb * 100, w, (w / PRICE - 1) * 100))
out['prob'] = prob
# 3. 条件6: 事業実態 EPS の5年 CAGR と PEG(3経路)
nong, core = FR.eps_paths('ベース')
eng = A0['ベース']['f']
eng_core = {int(k): x for k, x in eng['eps_core'].items()}
sh = {int(k): x for k, x in eng['shares'].items()}
# 会社経路: FY27 ガイダンス 8.10、FY30 目標 21(非GAAP)。FY28・29 は幾何補間、FY31 以降はエンジンの伸び
co = {27: 8.10, 30: 21.0}
gm = (21.0 / 8.10) ** (1 / 3)
co[28] = 8.10 * gm; co[29] = co[28] * gm
engn = {int(k): x for k, x in eng['eps'].items()}
co[31] = co[30] * engn[31] / engn[30]; co[32] = co[31] * engn[32] / engn[31]
co_core = {y: co[y] - F.SBC0 * (1 + F.SBC_G) ** (y - 27) * 0.8 / ((sh[y - 1] + sh[y]) / 2) for y in co}
c6 = {}
for lab, e in (('コンセンサス', core), ('会社', co_core), ('需給エンジン', eng_core)):
    cagr = (e[32] / e[27]) ** (1 / 5) - 1
    per = PRICE / e[27]
    c6[lab] = dict(e27=e[27], e32=e[32], cagr=cagr, per=per, peg=per / (cagr * 100))
    print('条件6 %-8s 事業実態EPS FY27 %.2f → FY32 %.2f CAGR %.1f%% PER %.1f PEG %.2f' % (lab, e[27], e[32], cagr * 100, per, per / (cagr * 100)))
out['c6'] = c6
# 4. 最終判断の3経路(加重)と DCF
ren = FR.weighted(eps_src='engine')[0]
gaps = dict(consensus=F8['total'], engine=ren, dcf=F8['dcf'])
# 会社経路: FY27〜30 を会社シナリオの EPS に置き換え(シナリオ比は維持)
keep = FR.CONS.copy()
FR.CONS.update({27: co[27], 28: co[28], 29: co[29], 30: co[30]})
gaps['company'] = FR.weighted()[0]
FR.CONS.update(keep)
for k, x in gaps.items():
    print('乖離 %-10s %.1f → %+.0f%%' % (k, x, (x / PRICE - 1) * 100))
out['gaps'] = gaps
json.dump(out, open('out/m8_extra.json', 'w'), ensure_ascii=False, indent=1, default=float)
