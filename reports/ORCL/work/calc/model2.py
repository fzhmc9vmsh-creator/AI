# -*- coding: utf-8 -*-
"""model.py の拡張: PEG 3経路・年度別評価(F13)・感応度(F12)・OpenAI 不払いの効果測定・エントリー価格帯・CSV 出力"""
import copy, json, os, csv, math
import model as M

I = M.I
S = copy.deepcopy(M.SOTP)
S['wacc_core'] = 0.080            # コア: データベース保守中心の安定事業(β≈1.0)。感応度で 7.75〜9.5% を併記
S['cip_ai'] = 35.0                # 建設仮勘定 48.5(H4)のうち AI 容量向け(推定)= 既に支出済みの capex
S_BULL = copy.deepcopy(S); S_BULL.update(m=0.33, pr=0.8, Lr=3, wacc_ai=0.095, growth_gw_per_yr=2.5, growth_prob=0.6, core_g5=0.07)
S_BEAR = copy.deepcopy(S); S_BEAR.update(m=0.18, pr=0.0, Lr=0, idle_after=True, wacc_ai=0.11, growth_prob=0.0,
                                          gw_contracted_total=7.0, core_g5=0.045, wacc_core=0.09)

def sotp2(s, eng):
    r = M.sotp(s, eng)
    add = s.get('cip_ai', 0.0) * s['build_disc']
    if s.get('gw_contracted_total', 10.2) < 10.2:
        add *= 0.6   # 不払いで建設途中の一部が座礁(弱気)
    r['cip_addback'] = add
    r['ai_ev'] += add; r['ev'] += add; r['equity'] += add
    r['per_share'] = r['equity'] / I['shares_now']
    return r

def openai_default(relet_ratio, gap_years, default_fy_offset=3.0, remaining_years=3, rev_per_yr=60.0, wacc=0.10,
                   ebitda_margin=0.85):
    """OpenAI が契約途中で支払不能になった場合の1株当たり価値の減少(前払い・再販を考慮)
    rev_per_yr: 約$300B/5年。gap_years: 再販までの空白。relet_ratio: 再販単価/当初単価。"""
    lost = 0.0
    for k in range(remaining_years):
        if k < gap_years:
            l = rev_per_yr * ebitda_margin
        else:
            l = rev_per_yr * (1 - relet_ratio)
        lost += l * (1 - M.TAX) / (1 + wacc) ** (default_fy_offset + k)
    return lost, lost / I['shares_now']

def extend(path_eps, g_after):
    e = list(path_eps)
    for g in g_after:
        e.append(e[-1] * (1 + g))
    return e   # FY27..FY32 + 延長

def run():
    R = M.run()
    eng = R['engine']
    for k, s in [('base', S), ('bull', S_BULL), ('bear', S_BEAR)]:
        R['sotp'][k] = sotp2(s, eng)
    # ---------- 芯の価値感度(再計算: コア WACC 8.0%、CIP 足し戻し後)
    tests = [
        ('経済的寿命×更新単価(契約後の残存価格比 pr と年数)', 'pr', 0.0, 0.9),
        ('コアの資本コスト', 'wacc_core', 0.095, 0.0775),
        ('AI容量の利益率(EBIT)', 'm', 0.18, 0.35),
        ('GW あたり売上(単価)', 'R', 9.0, 12.0),
        ('コアの成長率(5年)', 'core_g5', 0.04, 0.08),
        ('AI の資本コスト', 'wacc_ai', 0.115, 0.085),
        ('未契約の成長(GW/年)', 'growth_gw_per_yr', 0.0, 3.0),
        ('GW あたり Oracle 負担 capex', 'K', 28.0, 20.0),
    ]
    base_ps = R['sotp']['base']['per_share']
    rows = []
    for label, key, lo, hi in tests:
        a = copy.deepcopy(S); a[key] = lo
        b = copy.deepcopy(S); b[key] = hi
        if key == 'pr':
            a['Lr'] = 0; a['idle_after'] = True; b['Lr'] = 3
        rows.append(dict(label=label, lo=lo, hi=hi, v_lo=sotp2(a, eng)['per_share'], v_hi=sotp2(b, eng)['per_share']))
    # OpenAI の支払能力: 不払い(再販 40%・空白2年)〜 全額履行
    lost_bad, ps_bad = openai_default(0.4, 2)
    rows.append(dict(label='受注残上位顧客(OpenAI)の支払能力', lo='不払い(再販40%・空白2年)', hi='全額履行',
                     v_lo=base_ps - ps_bad, v_hi=base_ps))
    # 電力・建屋の制約の解放時期: 1年遅延 = 未建設契約分の NPV と稼働中の追加分の現金が1年後ろ倒し
    g = M.gw_npv(S)
    delay_cost = ((S['gw_contracted_total'] - S['gw_inservice']) * (g['npv'] + 0) * S['build_disc'] * (1 - 1 / 1.10)
                  + 2.0 * 10.0 * 0.85 * (1 - M.TAX) * 0.5)  # 1年遅延: NPV の時間価値 + 遅延年の逸失 EBITDA の半分(賃料繰延で一部相殺)
    rows.append(dict(label='電力・建屋の制約の解放時期', lo='1年遅延', hi='計画どおり', v_lo=base_ps - delay_cost / I['shares_now'], v_hi=base_ps))
    for r_ in rows:
        r_['swing'] = abs(r_['v_hi'] - r_['v_lo'])
    rows.sort(key=lambda x: -x['swing'])
    R['tornado2'] = dict(base=base_ps, rows=rows)
    R['openai_default'] = {
        'mild(再販70%・空白1年)': openai_default(0.7, 1),
        'severe(再販40%・空白2年)': openai_default(0.4, 2),
        'renegotiate(単価-20%・空白0)': openai_default(0.8, 0),
    }
    # ---------- リバース(コア WACC 8.0%、CIP 足し戻し後)
    lo, hi = 0.0, 0.7
    for _ in range(60):
        mid = (lo + hi) / 2; s = copy.deepcopy(S); s['m'] = mid
        lo, hi = (mid, hi) if sotp2(s, eng)['per_share'] < I['price'] else (lo, mid)
    R['implied_m2'] = mid
    lo, hi = 0.0, 1.5
    for _ in range(60):
        mid = (lo + hi) / 2; s = copy.deepcopy(S); s['pr'] = mid; s['Lr'] = 3
        lo, hi = (mid, hi) if sotp2(s, eng)['per_share'] < I['price'] else (lo, mid)
    R['implied_pr_Lr3'] = mid
    # ---------- PEG 経路(5年 CAGR、事業実態EPS)と年度別評価(F13)
    paths = R['paths']
    ext = {'コンセンサス': [0.09, 0.08, 0.07, 0.06, 0.05], '会社シナリオ': [0.12, 0.10, 0.08, 0.07, 0.06],
           '事業エンジン': [0.07, 0.06, 0.05, 0.05, 0.04], '弱気': [0.03, 0.03, 0.03, 0.03, 0.03]}
    peg_rng = {  # 年度別 PEG レンジ(9章の3経路収束による)
        'FY27': (0.80, 0.95), 'FY28': (0.85, 1.00), 'FY29': (0.90, 1.05), 'FY30': (0.95, 1.10), 'FY31': (1.00, 1.15), 'FY32': (1.00, 1.20)}
    per_floor = 14.0
    f13 = {}
    for k, v in paths.items():
        e = extend(v['eps_br'], ext[k])
        rows_ = []
        for i, y in enumerate(M.YEARS):
            g = (e[i + 5] / e[i]) ** (1 / 5) - 1
            lo_, hi_ = peg_rng[y]
            per_lo = max(per_floor, lo_ * g * 100); per_hi = max(per_floor, hi_ * g * 100)
            rows_.append(dict(year=y, eps_br=e[i], g5=g, peg_lo=lo_, peg_hi=hi_, per_lo=per_lo, per_hi=per_hi,
                              px_lo=per_lo * e[i], px_hi=per_hi * e[i], px_mid=(per_lo + per_hi) / 2 * e[i]))
        f13[k] = rows_
    R['f13'] = f13
    tgt = {k: f13[k][0]['px_mid'] for k in f13}
    tgt['弱気'] = (R['sotp']['bear']['per_share'] + max(per_floor, 0) * paths['弱気']['eps_br'][0] * 0 + 13 * paths['弱気']['eps_br'][0]) / 2
    R['targets'] = tgt
    R['deviation'] = {k: (v / I['price'] - 1) for k, v in tgt.items()}
    # ---------- F12: 経路 × PEG(FY27 事業実態EPS × PEG × g5)
    pegs = [0.6, 0.8, 0.9, 1.0, 1.2, 1.5]
    R['f12_path_peg'] = {k: [f13[k][0]['eps_br'] * p * f13[k][0]['g5'] * 100 for p in pegs] for k in f13}
    R['f12_pegs'] = pegs
    # F12b: 芯 × 芯(SOTP 1株価値): 行 = 残存価格比 pr(経済的寿命×更新単価)、列 = AI EBIT 利益率 m
    prs = [0.0, 0.3, 0.6, 0.9, 1.1]; ms = [0.18, 0.24, 0.29, 0.33, 0.37]
    mat = []
    for pr in prs:
        row = []
        for m in ms:
            s = copy.deepcopy(S); s['pr'] = pr; s['m'] = m
            if pr == 0.0:
                s['Lr'] = 0; s['idle_after'] = True
            else:
                s['Lr'] = 3 if pr >= 0.9 else 2
            row.append(sotp2(s, eng)['per_share'])
        mat.append(row)
    R['f12b'] = dict(prs=prs, ms=ms, mat=mat)
    # ---------- 期待値・非対称性
    probs = {'弱気': 0.25, '事業エンジン': 0.45, 'コンセンサス': 0.20, '会社シナリオ': 0.10}
    ev = sum(probs[k] * tgt[k] for k in probs)
    R['expected'] = dict(probs=probs, ev=ev, ev_dev=ev / I['price'] - 1,
                         down=tgt['弱気'] / I['price'] - 1, up=tgt['会社シナリオ'] / I['price'] - 1)
    # ---------- エントリー価格帯(B 評価: α=22.5%)
    B = tgt['事業エンジン']; U = tgt['会社シナリオ']; L = tgt['弱気']; a = 0.225
    Z1 = min(B * (1 - a), L * (1 + a / 2)); Z2 = B * (1 - a / 2)
    R['entry'] = dict(B=B, U=U, L=L, alpha=a, Z1=Z1, Z2=Z2, price=I['price'],
                      zone='見送り圏' if I['price'] > Z2 else ('分割エントリー圏' if I['price'] > Z1 else '即エントリー圏'),
                      ratio_at_Z1=(U - Z1) / (Z1 - L))
    # ---------- 契約裏付け率・希薄化の反実仮想
    rpo_conv = I['rpo'] * 0.5 / 3
    lease_pay = 5.0 + I['lease_unc'] / 17
    R['coverage'] = dict(rpo_conv_per_yr=rpo_conv, interest=6.0, lease_pay=lease_pay,
                         ratio=rpo_conv / (6.0 + lease_pay))
    atm_sh = 0.141; dil = atm_sh / 2.914
    eps_dil = -dil / (1 + dil)
    debt_alt = -(20.0 * 0.065 * (1 - M.TAX)) / (I['g27_eps'] * 3.03)
    R['dilution'] = dict(atm_dilution=dil, eps_effect_equity=eps_dil, eps_effect_debt_alt=debt_alt)
    return R

if __name__ == '__main__':
    R = run()
    P = lambda x: round(x, 2) if isinstance(x, float) else x
    for k in ['base', 'bull', 'bear']:
        s = R['sotp'][k]
        print('SOTP', k, {kk: P(s[kk]) for kk in ['core_ev', 'pv_inservice', 'pv_contracted', 'pv_growth', 'cip_addback', 'ai_ev', 'ev', 'equity', 'per_share', 'pv3_share']}, 'NPV/GW', P(s['gw']['npv']), 'IRR', P(s['gw']['irr']))
    print('TORNADO2 base', P(R['tornado2']['base']))
    for t in R['tornado2']['rows']:
        print('  ', t['label'], t['lo'], t['hi'], P(t['v_lo']), P(t['v_hi']), P(t['swing']))
    print('OpenAI default', {k: (P(v[0]), P(v[1])) for k, v in R['openai_default'].items()})
    print('implied m', P(R['implied_m2']), 'implied pr(Lr3)', P(R['implied_pr_Lr3']))
    for k, rows in R['f13'].items():
        print('F13', k)
        for r in rows:
            print('   ', {kk: P(v) for kk, v in r.items()})
    print('targets', {k: P(v) for k, v in R['targets'].items()})
    print('deviation', {k: P(v) for k, v in R['deviation'].items()})
    print('F12 path×PEG', R['f12_pegs'], {k: [P(x) for x in v] for k, v in R['f12_path_peg'].items()})
    print('F12b', R['f12b']['ms'], [[P(x) for x in r] for r in R['f12b']['mat']])
    print('expected', {k: P(v) if not isinstance(v, dict) else v for k, v in R['expected'].items()})
    print('entry', {k: P(v) for k, v in R['entry'].items()})
    print('coverage', {k: P(v) for k, v in R['coverage'].items()})
    print('dilution', {k: P(v) for k, v in R['dilution'].items()})
    def conv(x):
        if isinstance(x, float): return round(x, 4)
        if isinstance(x, dict): return {str(k): conv(v) for k, v in x.items()}
        if isinstance(x, (list, tuple)): return [conv(v) for v in x]
        return x
    json.dump(conv(R), open(os.path.join(M.OUT, 'results2.json'), 'w'), ensure_ascii=False, indent=1)
