# 外部資料(2026-10-29、Gemini 作成)の前提を、第4.5版の枠で 1 つずつ入れたときの理論株価(確率加重)
import json, copy
import model10 as M, m10_engine_fwd as F, m10_fair as FR
base_tot, vals = FR.weighted()
print('第4.5版 %.1f' % base_tot)
r_e0 = FR.r_equity()[0]
out = {}
def show(lab, v):
    out[lab] = v; print('%-52s %.1f(%+.1f)' % (lab, v, v - base_tot))
# 1. 株主資本コスト 9.20%(無リスク金利 4.20%・β 1.11・ERP 4.5%)
show('株主資本コスト 9.20%(外部資料)', FR.weighted(r_e=0.092)[0])
# 2. 許容 PEG 1.196(B 帯の位置 0.65)
show('許容 PEG 1.196(外部資料)', FR.weighted(peg=1.196)[0])
# 3. 外部資料の事業実態 EPS(FY27 6.92・FY28 9.70・FY29 12.97・FY30 16.23、FY31・32 は 5 年 CAGR 23.6% に合わせ延長)
ext = {27: 6.92, 28: 9.70, 29: 12.97, 30: 16.23}
ext[31] = ext[30] * 1.10; ext[32] = ext[31] * 1.08
_orig = FR.eps_paths
def eps_ext(name, eps_src='company'):
    nong, core = _orig(name, eps_src)
    nb, cb = _orig('ベース', eps_src)
    c2 = {}
    for y in core:
        e = ext.get(y, None)
        if e is None:
            e = ext[32] * (cb[y] / cb[32]) if y > 32 else core[y]
        c2[y] = e * core[y] / cb[y]           # シナリオ比は第4.5版のまま
    return nong, c2
FR.eps_paths = eps_ext
show('外部資料の事業実態 EPS の経路(電力 9 か月の遅れ)', FR.weighted()[0])
show('外部資料の EPS + 株主資本コスト 9.20% + PEG 1.196', FR.weighted(r_e=0.092, peg=1.196)[0])
FR.eps_paths = _orig
# 4. GPU の会計の耐用年数を 4 年に(EPS だけが動く。現金は同じ)
A = {}
swm = json.load(open('out/m10_all.json'))['swm']
for sc in (M.BASE, M.BULL, M.BEAR):
    q = F.setup(sc); q['ai']['acct_life'] = 4
    r, f = F.forward_values(q, swm)
    A[sc['name']] = dict(vps=r['vps'], f=json.loads(json.dumps(f, default=float)), seg_ev={k: r['seg_val'][k]['ev'] for k in M.SEGS})
keep = FR.A; FR.A = A
show('GPU の会計の耐用年数 4 年(エンジン EPS で)', FR.weighted(eps_src='engine')[0] - (FR.weighted(eps_src='engine')[0] - FR.weighted(eps_src='engine')[0]))
FR.A = keep
show('参考: 第4.5版のエンジン EPS', FR.weighted(eps_src='engine')[0])
json.dump(out, open('out/m10_gemini.json', 'w'), ensure_ascii=False, indent=1)
