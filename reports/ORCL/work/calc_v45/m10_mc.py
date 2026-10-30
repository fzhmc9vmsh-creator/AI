# 第4.5版: 主な不確実性を同時に動かすモンテカルロ。AI の循環の共通因子 z で相関を持たせる。
# 出力: 1 株価値(DCF、倒産確率込み)の分布、FY29 FCF・調整後レバレッジ・格付けの分布、株価との比較
import json, copy, math, random, sys
import model10 as M
swm = json.load(open('out/m10_all.json'))['swm']
PRICE = 139.56
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
rnd = random.Random(20261030)
ORDER = ['BB', 'BB+', 'BBB-', 'BBB', 'BBB+']


def draw():
    z = rnd.gauss(0, 1)                                   # AI の循環(需要・資金)の共通因子
    e = [rnd.gauss(0, 1) for _ in range(6)]
    d = {}
    # 1. 逼迫の終わる年(Y*): z の分位で FY30(25%)/FY32(50%)/FY34(25%)
    d['Y_star'] = 30 if z < -0.674 else (34 if z > 0.674 else 32)
    # 2. 契約後の再契約の単価(緩和後): 中心 0.70、z と固有の揺れ
    zr = 0.6 * z + 0.8 * e[0]
    d['rho'] = min(1.0, max(0.45, 0.70 + 0.15 * zr))
    d['dec'] = min(0.20, max(0.03, 0.12 - 0.04 * zr))
    # 3. OpenAI: 深刻(10%、FY29〜30 に 60% 分が 5 割払い)/ 見直し(15%、85% 払い)/ なし。z の下側に置く
    d['oai'] = 'severe' if z < -1.2816 else ('mild' if z < -0.6745 else 'none')
    # 4. 建設の遅れ(独立): なし 40% / FY28 の 1.5GW が 1 年 40% / 3.5GW が 1 年 20%
    u = rnd.random(); d['delay'] = 0.0 if u < 0.4 else (1.5 if u < 0.8 else 3.5)
    # 5. FY31〜32 の容量の追加(z と相関): 年 +1.0GW 30% / +2.0GW 50% / +3.5GW 20%
    zc = 0.7 * z + 0.714 * e[1]
    d['add'] = 1.0 if zc < -0.524 else (3.5 if zc > 0.842 else 2.0)
    # 6. ERP・業務アプリの OCI 移行(独立): なし 25% / ベース 50% / 倍 25%
    u = rnd.random(); d['erp'] = -1.0 if u < 0.25 else (1.0 if u > 0.75 else 0.0)
    # 7. 新規契約の単価の伸び(z と相関): 3% ± 1.5pt
    d['pg'] = 0.03 + 0.015 * max(-1.5, min(1.5, 0.7 * z + 0.7 * e[2]))
    # 8. 金利(独立): 市場の曲線 60% / 低下 20% / 6% 高止まり 20%
    u = rnd.random(); d['rf'] = 'market' if u < 0.6 else ('normalize' if u < 0.8 else 'high')
    d['z'] = z
    return d


def build(d):
    q = copy.deepcopy(M.BASE); q['sw_margin'] = swm; q['rf'] = d['rf']
    a = q['ai']
    plan = dict(a['gw_plan']); plan[28] -= d['delay']
    plan[31] = plan[30] + d['add']; plan[32] = plan[31] + d['add']
    a.update(gw_plan=plan, sites_committed=dict(plan), Y_star=d['Y_star'], post_rho_loose=d['rho'], post_dec_loose=d['dec'],
             gen_price=M.gen_price_v44(d['pg']))
    if d['oai'] == 'severe':
        a['rev_mod'] = M.openai_mod(0.60, 0.50, 29, 31)
    elif d['oai'] == 'mild':
        a['rev_mod'] = M.openai_mod(0.60, 0.85, 29, 31)
    if d['erp']:
        M.erp_boost(q, d['erp'])
    if d['Y_star'] <= 30 or d['oai'] == 'severe':
        q['sp_c_year'] = 29                               # AI への否定的な見方(S&P のトリガー c)
    return q


rows = []
for i in range(N):
    d = draw()
    r = M.run(build(d))
    P = {x['year']: x for x in r['path']}
    m = M.multiples(r)
    rows.append(dict(d, vps=r['vps'], vps_gc=r['vps_gc'], pd=r['pd_cum'], fcf29=P[29]['fcf'], fcf28=P[28]['fcf'],
                     lev_max=max(P[y]['adj_lev'] for y in range(27, 33)), lev29=P[29]['adj_lev'],
                     rmin=min((P[y]['rating'] for y in range(27, 36)), key=ORDER.index), eps30=m['ng30'], rev30=P[30]['rev']))
    if (i + 1) % 250 == 0:
        print(i + 1, file=sys.stderr)
json.dump(rows, open('out/m10_mc.json', 'w'), default=float)
v = sorted(x['vps'] for x in rows)
q = lambda p: v[min(len(v) - 1, int(p * len(v)))]
mean = sum(v) / len(v)
print('N %d 平均 %.1f 中央 %.1f | 5%% %.1f 10%% %.1f 25%% %.1f 75%% %.1f 90%% %.1f 95%% %.1f' % (N, mean, q(.5), q(.05), q(.10), q(.25), q(.75), q(.90), q(.95)))
print('P(価値 < 株価 %.2f) = %.1f%% / 株価の分位 %.1f%%' % (PRICE, 100 * sum(x < PRICE for x in v) / N, 100 * sum(x < PRICE for x in v) / N))
print('P(FY29 FCF ≤ 0) %.1f%% / P(FY29 FCF < 30) %.1f%% / P(レバレッジ最大 > 4.5) %.1f%% / P(BB+ 以下) %.1f%% / P(BB) %.1f%% / 平均 PD(FY45) %.1f%%' % (
    100 * sum(x['fcf29'] <= 0 for x in rows) / N, 100 * sum(x['fcf29'] < 30 for x in rows) / N, 100 * sum(x['lev_max'] > 4.5 for x in rows) / N,
    100 * sum(ORDER.index(x['rmin']) <= 1 for x in rows) / N, 100 * sum(x['rmin'] == 'BB' for x in rows) / N, 100 * sum(x['pd'] for x in rows) / N))
