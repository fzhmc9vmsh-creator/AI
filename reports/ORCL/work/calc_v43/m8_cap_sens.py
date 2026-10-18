# 第4.2版の感応度: FY30〜32 も年 3.5GW を追加(15/18.5/22GW)した場合。ベースだけ差し替え、同じ式で評価
import json, copy
import model8 as M
import m8_engine_fwd as F
import m8_fair as FR
M.BASE['ai']['lag'] = 0.30
swm = json.load(open('out/m8_all.json'))['swm']
q = F.setup(M.BASE)
plan = {27: 4.7, 28: 7.4, 29: 11.5, 30: 15.0, 31: 18.5, 32: 22.0}
q['ai']['gw_plan'] = dict(plan); q['ai']['sites_committed'] = dict(plan)
r, f = F.forward_values(q, swm)
P = {x['year']: x for x in r['path']}
A0 = copy.deepcopy(FR.A)
FR.A['ベース'] = dict(FR.A['ベース'], vps=r['vps'], f=json.loads(json.dumps(f, default=float)))
FR.A['ベース']['f'] = {k: {int(kk): vv for kk, vv in v.items()} for k, v in FR.A['ベース']['f'].items()}
# eps_paths は「シナリオ ÷ ベース」の比を使うので、ベースを差し替えるとコンセンサス FY27〜30 はそのまま、FY31 以降の伸びだけ変わる
v_alt = FR.fair('ベース')[0]
FR.A = A0
v_base = FR.fair('ベース')[0]
print('ベース %.1f → 3.5GW 継続 %.1f(%+.1f)、DCF %.1f → %.1f' % (v_base, v_alt, v_alt - v_base, A0['ベース']['vps'], r['vps']))
print('FCF', ' '.join('FY%d %.0f' % (y, P[y]['fcf']) for y in range(27, 33)), ' 格付', ' '.join(P[y]['rating'] for y in range(27, 33)))
print('EPS(エンジン)', ' '.join('%d:%.2f' % (y, f['eps'][y]) for y in range(29, 35)))
