"""交差確認(DCF・SOTP)、成長の値段、価値感度(芯)、エントリー価格帯、非対称性(Opus 2026-10-18)"""
import json, copy, importlib
import model as M

def dcf(eps_path, coc, tg, payout):
    """簡易DCF: 配当(EPS×配当性向)の現在価値 + 最終年EPS×(1+tg)/(coc-tg)の現在価値。
    1年目を0.5年後とみなす(期中)。成長企業の内部留保は成長投資に回り、その効果はEPS経路に含まれる前提。"""
    v = 0.0
    for i, e in enumerate(eps_path):
        v += e * payout / (1 + coc) ** (i + 0.5)
    tv = eps_path[-1] * (1 + tg) / (coc - tg)
    v += tv / (1 + coc) ** (len(eps_path) - 0.5)
    return v

R = M.run()
out = {}
# ---- DCF交差確認(中心経路=事業エンジン)
cfg = {'nittobo': dict(coc=.08, tg=.03, payout=.25),
       'mitsui': dict(coc=.08, tg=.025, payout=.35),
       'cotech': dict(coc=.09, tg=.015, payout=.50)}
for k in ['nittobo', 'mitsui', 'cotech']:
    out[k] = {'dcf': {}}
    for p in ['engine', 'company', 'bear', 'consensus']:
        path = [v['eps'] for v in R[k]['paths'][p].values()]
        out[k]['dcf'][p] = round(dcf(path, **cfg[k]))
# GS経路(金居、2029以降は2028横ばい)
gs = [9.98, 26.51, 42.58, 42.58, 42.58, 42.58]
out['cotech']['dcf']['gs'] = round(dcf(gs, **cfg['cotech']))

# ---- 三井金属 SOTP(FY28の事業エンジン経常益、税後0.78、事業別PER)
m28 = R['mitsui']['paths']['engine']['FY28']
sotp = [
  ('銅箔(MicroThin・VSP・FaradFlex)', m28['foil'], 22, 'ROIC52%・シェア95%・CAP10年超、利益成長年12%'),
  ('その他機能材料(触媒・機能粉等)', 185, 12, '貴金属価格の影響が大きい'),
  ('金属(製錬・リサイクル)', m28['metals'], 8, '景気循環。正規化経常益'),
  ('自動車部品・調整', -45, 10, '赤字のドアロック等'),
]
tot = sum(o * 0.78 * per for _, o, per, _ in sotp)
net_debt = 574  # 億円: 有利子負債1,157億円−現金同等物583億円(2026/3末、research/52)
equity = tot - net_debt
out['mitsui']['sotp'] = dict(rows=[dict(seg=a, ordinary=o, np=round(o * .78), per=per, value=round(o * .78 * per), note=n) for a, o, per, n in sotp],
                             total=round(tot), net_debt=net_debt, equity=round(equity),
                             per_share=round(equity / M.MIT['shares'] * 100), per_share_fy28=True)

# ---- 成長の値段: 定常状態利益(成長投資を止めた場合)÷資本コスト
# 定常状態EPS【推定】: 日東紡=FY27事業エンジンEPSに成長向け費用(増産立上げ・R&D増分 約15億円の税後)を戻す
ss = {'nittobo': (119.6 + 15 * 0.67 / M.NIT['shares'] * 100, .08),
      'mitsui': (141.3 + 10 * 0.78 / M.MIT['shares'] * 100, .08),   # 銅箔増強の立上げ費用 約10億円
      'cotech': (9.62 + 60 * 0.8 / M.CT['shares'], .09)}             # 三廠立上げ費用 約60百万TWD【推定】
for k, (e, c) in ss.items():
    price = R[k]['meta']['price']
    ssv = e / c
    out[k]['growth_price'] = dict(ss_eps=round(e, 2), ss_value=round(ssv), price=price,
                                  growth_value=round(price - ssv), growth_share=round((price - ssv) / price, 3))

# ---- 価値感度(芯の特定): 事業エンジン経路の変数を現実的な幅で動かし、DCF価値の変化率を測る
def sens_nittobo():
    base_fn = M.nittobo
    res = []
    def val(mod):
        src = open('model.py').read()
        return None
    # 直接パラメータを差し替えるため、関数内の辞書を再定義する簡易版
    import types
    def run_with(tv_mult=1.0, tp_shift=0.0, nv_shift=0.0, dep_mult=1.0, Tshare=1.0):
        P = dict(tv=[1.20, 1.80, 2.60, 3.10, 3.55, 3.90], tp=[1, 1.00, 1.00, 0.97, 0.94, 0.92],
                 nv=[0, .15, .12, .08, .08, .06], npx=[1, 1, 1, .97, .94, .92], dep=[0, 20, 45, 60, 70, 75])
        T_rev27, T_var, T_fix27 = 350.0 * Tshare, 0.40, 30.0 * Tshare
        N_rev27, N_var, N_fix27 = 830 - 350.0 * Tshare, 0.60, 72.0
        eps = []; N_vol = 1.0
        for i in range(6):
            tv = (1.2 + (P['tv'][i] - 1.2) * tv_mult) / 1.2
            tp = P['tp'][i] + (tp_shift * min(i, 3) / 3 if i >= 2 else 0)
            T_rev = T_rev27 * tv * tp
            T_op = T_rev - T_var * T_rev27 * tv - T_fix27 - P['dep'][i] * dep_mult * .75
            N_vol *= (1 + P['nv'][i] + (nv_shift if i else 0))
            N_rev = N_rev27 * N_vol * P['npx'][i]
            N_op = N_rev - N_var * N_rev27 * N_vol - N_fix27 - P['dep'][i] * dep_mult * .25
            op = T_op + N_op + 37 + 2 * i - 17
            if i == 0: op = 320.0
            eps.append((op + 5) * .67 / M.NIT['shares'] * 100)
        return dcf(eps, **cfg['nittobo'])
    b = run_with()
    tests = [('T-glassの実効数量の伸び(能力立上げ)', dict(tv_mult=0.7), dict(tv_mult=1.2)),
             ('FY29以降のT-glass価格(他社認定の時期)', dict(tp_shift=-0.15), dict(tp_shift=+0.08)),
             ('電子材料に占めるT系の比率', dict(Tshare=0.75), dict(Tshare=1.25)),
             ('NE・その他の数量成長', dict(nv_shift=-0.06), dict(nv_shift=+0.04)),
             ('増産投資の償却負担', dict(dep_mult=1.4), dict(dep_mult=0.8))]
    for name, lo, hi in tests:
        res.append(dict(var=name, low=round(run_with(**lo) / b - 1, 3), high=round(run_with(**hi) / b - 1, 3)))
    return round(b), sorted(res, key=lambda r: -(abs(r['low']) + abs(r['high'])))

def sens_cotech():
    def run_with(v_mult=1.0, p_shift=0.0, base_m=0.0, opex_m=1.0):
        v = [120, 445, 700, 800, 850, 900]; p = [1050, 1100, 1100, 1000, 950, 930]; cc = [255, 250, 245, 240, 240, 240]
        br = [10450, 10500, 10500, 10300, 10300, 10300]; bm = [.265, .27, .26, .24, .23, .23]
        eps = []
        for i in range(6):
            vv = v[0] + (v[i] - v[0]) * v_mult
            pp = p[i] + (p_shift if i >= 2 else 0)
            gp = vv * 12 * (pp - 380 - cc[i]) / 1000 + br[i] * (bm[i] + (base_m if i else 0))
            op = gp - 330 * 1.1 ** i * opex_m
            eps.append(op * .8 / M.CT['shares'])
        return dcf(eps, **cfg['cotech'])
    b = run_with()
    tests = [('HVLP4の加工費(2028年以降の価格)', dict(p_shift=-150), dict(p_shift=+200)),
             ('HVLP3+4の数量(三廠の立上げ)', dict(v_mult=0.7), dict(v_mult=1.4)),
             ('汎用銅箔の粗利率', dict(base_m=-0.04), dict(base_m=+0.03)),
             ('販管費', dict(opex_m=1.3), dict(opex_m=0.8))]
    res = [dict(var=n, low=round(run_with(**lo) / b - 1, 3), high=round(run_with(**hi) / b - 1, 3)) for n, lo, hi in tests]
    return round(b), sorted(res, key=lambda r: -(abs(r['low']) + abs(r['high'])))

def sens_mitsui():
    def run_with(foil_g=0.0, met=0.0, ofm=0.0, per_foil=22):
        foil = [640, 740, 840, 930, 1010, 1080]
        foil = [foil[0]] + [f * (1 + foil_g) ** i for i, f in enumerate(foil[1:], 1)]
        o = [180, 185, 190, 195, 200, 205]; m = [265, 330, 320, 320, 320, 320]
        eps = [((foil[i] + o[i] + ofm + m[i] + (met if i else 0) - 45) * .78) / M.MIT['shares'] * 100 for i in range(6)]
        return dcf(eps, **cfg['mitsui'])
    b = run_with()
    tests = [('銅箔の利益成長(能力増と値上げ)', dict(foil_g=-0.04), dict(foil_g=+0.03)),
             ('金属事業の正規化利益', dict(met=-130), dict(met=+120)),
             ('触媒・機能粉', dict(ofm=-40), dict(ofm=+30))]
    res = [dict(var=n, low=round(run_with(**lo) / b - 1, 3), high=round(run_with(**hi) / b - 1, 3)) for n, lo, hi in tests]
    return round(b), sorted(res, key=lambda r: -(abs(r['low']) + abs(r['high'])))

out['nittobo']['sens'] = sens_nittobo()
out['cotech']['sens'] = sens_cotech()
out['mitsui']['sens'] = sens_mitsui()

json.dump(out, open('valuation2.json', 'w'), ensure_ascii=False, indent=1)
for k, v in out.items():
    print('=====', k)
    print(' DCF', v['dcf'])
    print(' 成長の値段', v['growth_price'])
    print(' 感度 base', v['sens'][0])
    for r in v['sens'][1]: print('   ', r)
print('SOTP', json.dumps(out['mitsui']['sotp'], ensure_ascii=False))
