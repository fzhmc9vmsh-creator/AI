"""3社の事業エンジン経路・3経路バリュエーション(Opus作成 2026-10-18)
前提はすべてこのファイルに固定する。単位: 日本=億円・円、台湾=百万TWD・TWD。
出所の詳細は research/40〜42, data/*.md。【推定】はOpusの推定。"""
import json, math

def cagr(a, b, n):
    return (b / a) ** (1 / n) - 1 if a > 0 and b > 0 else float('nan')

# ---------------------------------------------------------------- 日東紡 3110
NIT = dict(price=2989, price_date='2026-10-16', shares=182.0,   # 百万株(自己株除く平均、松井EPSから逆算)
           eps_fy26_norm=85.0, eps_fy26_norm_range=(80, 103),  # 土地売却益341億円を除く正規化(研究40 §1-3)
           coc=0.08)
def nittobo(path):
    # FY27(=2027/3期)の電子材料を T-glass系 と NE・その他 に分解【推定】
    # FY27: 電子材料売上830、うちT系350(OP180)、NE他480(OP120)。非電子OP37、本社-17。
    T_rev27, T_var, T_fix27 = 350.0, 0.40, 30.0
    N_rev27, N_var, N_fix27 = 480.0, 0.60, 72.0
    yrs = ['FY27', 'FY28', 'FY29', 'FY30', 'FY31', 'FY32']
    P = {
      # T系の実効出荷指数(FY26=1.0)、T価格指数、NE数量成長、NE価格指数、追加償却
      'engine':   dict(tv=[1.20, 1.80, 2.60, 3.10, 3.55, 3.90], tp=[1, 1.00, 1.00, 0.97, 0.94, 0.92],
                       nv=[0, .15, .12, .08, .08, .06], npx=[1, 1, 1, .97, .94, .92], dep=[0, 20, 45, 60, 70, 75]),
      'company':  dict(tv=[1.20, 2.00, 3.00, 3.40, 3.80, 4.10], tp=[1, 1.00, 1.00, 1.00, 0.98, 0.96],
                       nv=[0, .15, .12, .10, .08, .06], npx=[1, 1, 1, 1, .98, .96], dep=[0, 22, 50, 62, 70, 75]),
      'bear':     dict(tv=[1.15, 1.60, 2.20, 2.50, 2.70, 2.85], tp=[1, 0.97, 0.88, 0.78, 0.74, 0.72],
                       nv=[0, .08, .00, .00, .03, .03], npx=[1, .97, .90, .85, .83, .82], dep=[0, 20, 45, 60, 65, 68]),
    }[path]
    out = {}
    N_vol = 1.0
    for i, y in enumerate(yrs):
        tv = P['tv'][i] / 1.20
        T_rev = T_rev27 * tv * P['tp'][i]
        T_op = T_rev - T_var * T_rev27 * tv - T_fix27 - P['dep'][i] * 0.75
        N_vol *= (1 + P['nv'][i])
        N_rev = N_rev27 * N_vol * P['npx'][i]
        N_op = N_rev - N_var * N_rev27 * N_vol - N_fix27 - P['dep'][i] * 0.25
        other = 37 + 2 * i
        op = T_op + N_op + other - 17
        if path == 'engine' and y == 'FY27':
            op = 320.0          # 会社予想300×保守性(過去3期の最終実績は最終修正比+10〜15%)の一部を反映
        if path == 'company' and y == 'FY27':
            op = 300.0          # 会社予想(2026/8/5修正)
        ordinary = op + 5
        np_ = ordinary * 0.67   # 純利益/経常 = 会社予想200/300
        out[y] = dict(T_rev=round(T_rev), N_rev=round(N_rev), op=round(op, 1), np=round(np_, 1),
                      eps=round(np_ / NIT['shares'] * 100, 1))
    return out

def nittobo_consensus():
    # FY27: kabuyoho 経常コンセンサス313.28億(2026-09-28)→純利益×0.67。FY28以降は欠損→Opus延長:
    # 市場の仮説(TrendForce「T-glass不足は2027年から緩和」)に沿い、増益率をFY28 +15%、FY29 +6%、FY30 0%、FY31 0%、FY32 0%
    eps27 = 313.28 * 0.67 / NIT['shares'] * 100
    g = [None, .15, .06, .0, .0, .0]
    out, e = {}, eps27
    for i, y in enumerate(['FY27', 'FY28', 'FY29', 'FY30', 'FY31', 'FY32']):
        if i: e *= 1 + g[i]
        out[y] = dict(eps=round(e, 1), note='実績コンセンサス' if i == 0 else 'Opus延長(市場仮説)')
    return out

# ---------------------------------------------------------------- 三井金属 5706
MIT = dict(price=2659, price_date='2026-10-09', shares=574.0, coc=0.08)
def mitsui(path):
    yrs = ['FY27', 'FY28', 'FY29', 'FY30', 'FY31', 'FY32']
    # 経常利益の積み上げ: 銅箔(MicroThin+VSP+FaradFlex)、その他機能材料(触媒・機能粉等)、金属、自動車部品・調整
    P = {
      'engine':  dict(foil=[640, 740, 840, 930, 1010, 1080], ofm=[180, 185, 190, 195, 200, 205], met=[265, 330, 320, 320, 320, 320]),
      'company': dict(foil=[600, 700, 790, 880, 980, 1050], ofm=[180, 185, 190, 195, 200, 205], met=[265, 305, 325, 345, 360, 360]),
      'bear':    dict(foil=[620, 660, 680, 690, 700, 700], ofm=[175, 170, 170, 170, 170, 170], met=[230, 200, 200, 200, 200, 200]),
    }[path]
    out = {}
    for i, y in enumerate(yrs):
        ordinary = P['foil'][i] + P['ofm'][i] + P['met'][i] - 45
        np_ = ordinary * 0.78
        out[y] = dict(foil=P['foil'][i], metals=P['met'][i], ordinary=round(ordinary), np=round(np_),
                      eps=round(np_ / MIT['shares'] * 100, 1))
    return out

def mitsui_consensus():
    # FY27: kabuyoho 経常コンセンサス1,153〜1,167億(2026-08〜10)→純利益894億(2026-08-20)。FY28以降欠損→Opus延長:
    # 中計見直し(経常FY28 1,150、FY31 1,500)の伸び率を当てる
    eps27 = 894.38 / MIT['shares'] * 100
    g = [None, .06, .09, .09, .08, .05]
    out, e = {}, eps27
    for i, y in enumerate(['FY27', 'FY28', 'FY29', 'FY30', 'FY31', 'FY32']):
        if i: e *= 1 + g[i]
        out[y] = dict(eps=round(e, 1), note='実績コンセンサス' if i == 0 else 'Opus延長(中計の伸び率)')
    return out

# ---------------------------------------------------------------- 金居 8358
CT = dict(price=461.5, price_date='2026-10-15', shares=252.6, coc=0.09, copper=380.0)  # 銅地金TWD/kg【推定】
def cotech(path):
    yrs = ['2026', '2027', '2028', '2029', '2030', '2031']
    P = {
      # HVLP3+4 平均月産(t)、HVLP価格(TWD/kg、銅込み)、加工原価(TWD/kg)、汎用事業 売上・粗利率
      'engine':  dict(v=[120, 445, 700, 800, 850, 900], p=[1050, 1100, 1100, 1000, 950, 930], cc=[255, 250, 245, 240, 240, 240],
                      br=[10450, 10500, 10500, 10300, 10300, 10300], bm=[.265, .27, .26, .24, .23, .23]),
      'company': dict(v=[120, 500, 1000, 1150, 1250, 1300], p=[1050, 1150, 1180, 1150, 1100, 1080], cc=[255, 250, 240, 235, 235, 235],
                      br=[10450, 10300, 9600, 9300, 9300, 9300], bm=[.265, .27, .27, .26, .25, .25]),
      'bear':    dict(v=[120, 380, 600, 650, 700, 700], p=[1050, 1080, 960, 820, 760, 740], cc=[255, 252, 248, 245, 245, 245],
                      br=[10450, 10300, 10000, 9800, 9800, 9800], bm=[.265, .26, .22, .20, .19, .19]),
    }[path]
    out = {}
    opex = 330.0
    for i, y in enumerate(yrs):
        gp_kg = P['p'][i] - CT['copper'] - P['cc'][i]
        h_t = P['v'][i] * 12
        h_rev = h_t * P['p'][i] / 1000      # 百万TWD(t×TWD/kg×1000kg÷1e6)
        h_gp = h_t * gp_kg / 1000
        b_gp = P['br'][i] * P['bm'][i]
        op = h_gp + b_gp - opex * (1.10 ** i)
        np_ = op * 0.80
        out[y] = dict(hvlp_t_mo=P['v'][i], hvlp_rev=round(h_rev), rev=round(h_rev + P['br'][i]), op=round(op),
                      np=round(np_), eps=round(np_ / CT['shares'], 2), hvlp_share=round(h_rev / (h_rev + P['br'][i]), 3))
    return out

def cotech_consensus():
    # 台湾国内報道 2026 10.0、2027 17.70(経済日報)。2028以降欠損→Opus延長: 市場仮説(MS: HVLP4+不足は2027年31%→2028年20%に縮小)
    out = {'2026': dict(eps=10.0, note='実績コンセンサス'), '2027': dict(eps=17.7, note='実績コンセンサス')}
    e = 17.7
    for y, g in [('2028', .15), ('2029', .03), ('2030', .0), ('2031', .0)]:
        e *= 1 + g
        out[y] = dict(eps=round(e, 2), note='Opus延長(市場仮説)')
    return out

GS_COTECH = {'2026': 9.98, '2027': 26.51, '2028': 42.58}   # ゴールドマン・サックス(2026-08-12報道)、外部の強気見解として併記

# ---------------------------------------------------------------- 年度別評価(F13)
def f13(path_eps, years, peg_lo, peg_hi, coc, g_cap=0.50):
    """年度別評価。妥当PER = max(PEG×g, 定常状態PER)。定常状態PER = 1/資本コスト。
    ただし3年先のEPSが当年を下回る(利益の山)場合は、定常状態の利益を3年先EPSに置き換える(ピークにPERを掛けない)。"""
    rows = []
    for i, y in enumerate(years[:-3]):
        e0, e3 = path_eps[y], path_eps[years[i + 3]]
        g = cagr(e0, e3, 3)
        g_used = max(min(g, g_cap), 0.0) if not math.isnan(g) else 0.0
        lo, hi = peg_lo[i], peg_hi[i]
        per_lo, per_hi = lo * g_used * 100, hi * g_used * 100
        ss_eps = min(e0, e3)                      # 定常状態の利益(山の後の水準)
        ss_val = ss_eps / coc
        p_lo, p_hi = max(per_lo * e0, ss_val), max(per_hi * e0, ss_val)
        rows.append(dict(year=y, eps=e0, g=round(g, 4), peg=(lo, hi), per=(round(per_lo, 1), round(per_hi, 1)),
                         ss_floor=round(ss_val), floor_used=(per_lo * e0 < ss_val),
                         price=(round(p_lo), round(p_hi)), price_mid=round((p_lo + p_hi) / 2)))
    return rows

def run():
    R = {}
    # 日東紡
    yrsJ = ['FY27', 'FY28', 'FY29', 'FY30', 'FY31', 'FY32']
    n = {p: nittobo(p) for p in ['engine', 'company', 'bear']}
    n['consensus'] = nittobo_consensus()
    # 許容PEG(年度別、狭いレンジ): 構造評価B→1.0〜1.3出発。CAP長(次世代T-glass、認定障壁)+0.1、成熟に向け逓減
    peg_n = ([1.10, 1.05, 1.00], [1.30, 1.25, 1.20])
    R['nittobo'] = dict(meta=NIT, paths=n,
        f13={p: f13({y: n[p][y]['eps'] for y in yrsJ}, yrsJ, *peg_n, NIT['coc']) for p in n})
    # 三井金属
    m = {p: mitsui(p) for p in ['engine', 'company', 'bear']}
    m['consensus'] = mitsui_consensus()
    # 構造評価B→出発1.0〜1.3。MicroThinのCAP(10年超、シェア95%)とROIC52%で+0.2、ただし金属の景気循環で-0.0(SOTPで別途確認)
    peg_m = ([1.25, 1.25, 1.20], [1.50, 1.45, 1.40])
    R['mitsui'] = dict(meta=MIT, paths=m,
        f13={p: f13({y: m[p][y]['eps'] for y in yrsJ}, yrsJ, *peg_m, MIT['coc']) for p in m})
    # 金居
    yrsT = ['2026', '2027', '2028', '2029', '2030', '2031']
    c = {p: cotech(p) for p in ['engine', 'company', 'bear']}
    c['consensus'] = cotech_consensus()
    # 構造評価C→出発0.8〜1.0。CAP短(中国勢の認定2027-28)・景気循環で-0.1
    peg_c = ([0.70, 0.70, 0.65], [0.90, 0.90, 0.85])
    R['cotech'] = dict(meta=CT, paths=c, gs=GS_COTECH,
        f13={p: f13({y: c[p][y]['eps'] for y in yrsT}, yrsT, *peg_c, CT['coc']) for p in c})
    return R

if __name__ == '__main__':
    R = run()
    json.dump(R, open('/home/user/AI/growth-deck/analysis/results.json', 'w'), ensure_ascii=False, indent=1)
    for k in ['nittobo', 'mitsui', 'cotech']:
        print('=====', k, R[k]['meta']['price'])
        for p, d in R[k]['paths'].items():
            print(f"  {p:9s}", '  '.join(f"{y}:{v['eps']}" for y, v in d.items()))
        for p, rows in R[k]['f13'].items():
            print(f"  F13 {p:9s}", ' | '.join(f"{r['year']} g={r['g']:.1%} PER{r['per']} 床{r['ss_floor']} 価{r['price']}" for r in rows))
