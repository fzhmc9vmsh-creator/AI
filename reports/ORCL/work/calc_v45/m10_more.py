# 第4.4版: 金利の経路(s15)、営業利益率の分解とルール・オブ・40(s10)、容量の表(s13)
import json, copy
import model10 as M
import m10_engine_fwd as F
import m10_fair as FR
A0 = json.load(open('out/m10_all.json')); swm = A0['swm']
out = {}
r_e0, ba, bl, de = FR.r_equity()
def build_A(mod):
    A = {}
    for sc in (M.BASE, M.BULL, M.BEAR):
        q = F.setup(sc); mod(q)
        r, f = F.forward_values(q, swm)
        A[sc['name']] = dict(vps=r['vps'], f=json.loads(json.dumps(f, default=float)), seg_ev={k: r['seg_val'][k]['ev'] for k in M.SEGS})
    return A
rates = {}
for lab, (kind, erp, rf_e) in {'市場の曲線(ベース)': ('market', 0.0423, 0.0502), '予測どおり低下(5.2→4.2%、ERP 4.5%)': ('normalize', 0.045, 0.045), '高止まり(6.0%)': ('high', 0.0423, 0.060)}.items():
    M.ERP = erp
    A = build_A(lambda q, k=kind: q.update(rf=k))
    keep = FR.A; FR.A = A
    r_e = rf_e + bl * erp
    tot, vals = FR.weighted(r_e=r_e)
    FR.A = keep
    dcf = 0.5 * A['ベース']['vps'] + 0.25 * A['強気']['vps'] + 0.25 * A['弱気']['vps']
    rates[lab] = dict(r_e=r_e, weighted=tot, dcf=dcf)
    print('%-34s r_e %.2f%% 加重 %.1f DCF %.1f' % (lab, r_e * 100, tot, dcf))
M.ERP = 0.0423
out['rates'] = rates
q = F.setup(M.BASE); q['sw_margin'] = swm
r = M.run(q)
mb = M.margin_bridge(r, 27, 34)
for x in mb:
    print('FY%d 営業利益率 %.1f%% AI 構成比 %.0f%% AI 率 %.1f%%' % (x['year'], x['margin'] * 100, x['ai_share'] * 100, x['ai_margin'] * 100))
P = {x['year']: x for x in r['path']}
print('FY27 営業利益率 %.1f%% AI 構成比 %.0f%%' % (P[27]['op_margin'] * 100, P[27]['shares_rev']['ai'] * 100))
r40 = M.rule40(r)
for x in r40[:7]:
    print('FY%d 成長 %.0f%% R40(FCF) %.0f R40(オーナー) %.0f' % (x['year'], x['growth'] * 100, x['r40_fcf'] * 100, x['r40_owner'] * 100))
sbc = {y: F.SBC0 * (1 + F.SBC_G) ** (y - 27) for y in range(27, 35)}
for y in range(27, 33):
    print('FY%d 非GAAP 営業利益 %.1f 率 %.1f%%(GAAP 相当 %.1f%%)' % (y, P[y]['ebit'] + sbc[y], (P[y]['ebit'] + sbc[y]) / P[y]['rev'] * 100, P[y]['op_margin'] * 100))
out['margin'] = [dict(year=27, margin=P[27]['op_margin'], ai_share=P[27]['shares_rev']['ai'])] + [dict(year=x['year'], margin=x['margin'], ai_share=x['ai_share'], ai_margin=x['ai_margin']) for x in mb]
out['r40'] = r40[:7]
out['nongaap_op'] = {y: dict(op=P[y]['ebit'] + sbc[y], margin=(P[y]['ebit'] + sbc[y]) / P[y]['rev']) for y in range(27, 33)}
out['ai_gw'] = {y: r['seg']['ai'][y]['gw'] for y in range(27, 35)}
json.dump(out, open('out/m10_more.json', 'w'), ensure_ascii=False, indent=1, default=float)
