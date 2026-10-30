# -*- coding: utf-8 -*-
"""第4.4版(2026-10-30): EPS の起点を会社の見通し(FY27 8.10・FY30 21、Investor Day 2026-10-28)に変える。
FY28・29 はエンジンの形で補間、FY31 以降はエンジンの伸び。コンセンサス(説明会の前の値で遅れている)は比較に使う。
株価 139.56(2026-10-29 終値)、今日 → FY27 末 0.584 年、無リスク金利 5.02%。
第4.2版の年度別理論株価。品質確認(2026-10-16)の確定指摘を反映:
- M1: 経路 a・b は事業実態 EPS(非GAAP − 株式報酬の税引後)に掛ける。同業の PER は主に GAAP 基準(株式報酬を費用に含む)
- M5: 倍率(同業 23 倍・PEG 1.0)は全シナリオ共通。シナリオの差は EPS と需給エンジンの価値だけで出す
- M7/F07: 経路 c はエンジンの年度末1株価値そのもの(エンジン EPS で割った倍率をコンセンサス EPS に掛けない)
- M4: 倒産確率を全経路に反映(今日→t の生存確率。経路 a・b は t 以降の生存確率も)
- F1/M3: 株数は超過 FCF の自社株買いで減る(m8_engine_fwd)
- 小: FY27 の残り配当 1.00、今日→FY27 末 0.622 年、株主のβはレバレッジ込み
"""
import json, copy, sys
import model9 as M
from m9_engine_fwd import forward_values, setup, SBC0, SBC_G

A = json.load(open('out/m9_all.json'))
CONS = {27: 8.14, 28: 10.99, 29: 15.77, 30: 20.53}       # 非GAAP コンセンサス(説明会の前、U2。FY30 は T1)
CO_END = {27: 8.10, 30: 21.0}                             # 会社の見通し(8-K Ex.99.1、CFO 資料 p.4)
PRICE = 139.56                                           # 2026-10-29 終値
T0 = 0.584                                               # 2026-10-30 → 2027-05-31
W0 = {27: 0.40, 28: 0.30, 29: 0.20, 30: 0.10}
PEER, PEG = 23.0, 1.0
TAX_EPS = 0.20


def r_equity(price=PRICE):
    b = A['ベース']
    ev = b['seg_ev']; tot = sum(ev.values())
    beta_a = sum(M.BASE['beta'][k] * ev[k] for k in ev) / tot
    D = M.BS['debt'] + M.BS['fin_lease'] + M.BS['pref'] + M.BS['lease_liab']      # 第4.3版: 開始済みのリース負債を含める(信用判定と同じ扱い)
    E = price * M.BS['shares']
    beta_l = beta_a * (1 + (1 - 0.21) * D / E)
    return 0.0502 + beta_l * 0.0423, beta_a, beta_l, D / E


def company_path():
    """会社の EPS 経路(ベース): FY27 と FY30 は会社の数字。FY28・29 はエンジンのベースの形(対数の比率)で補間"""
    base = {int(k): v for k, v in A['ベース']['f']['eps'].items()}
    import math
    span = math.log(base[30] / base[27])
    co = {}
    for y in range(27, 31):
        w = math.log(base[y] / base[27]) / span
        co[y] = CO_END[27] * (CO_END[30] / CO_END[27]) ** w
    return co


def eps_paths(name, eps_src='company'):
    eng = {int(k): v for k, v in A[name]['f']['eps'].items()}
    base = {int(k): v for k, v in A['ベース']['f']['eps'].items()}
    sh = {int(k): v for k, v in A[name]['f']['shares'].items()}
    e = {}
    for y in range(27, 36):
        if y <= 30:
            if eps_src == 'cons':
                e[y] = CONS[y] * eng[y] / base[y]
            elif eps_src == 'company':
                e[y] = company_path()[y] * eng[y] / base[y]
            else:
                e[y] = eng[y]
        else:
            e[y] = e[y - 1] * eng[y] / eng[y - 1]
    core = {y: e[y] - SBC0 * (1 + SBC_G) ** (y - 27) * (1 - TAX_EPS) / ((sh[y - 1] + sh[y]) / 2) for y in e}
    return e, core


def fair(name, W=W0, peer=PEER, peg=PEG, r_e=None, eps_src='company', basis='core', eps_mult=1.0, surv_on=True, c_on=True):
    r_e = r_e or r_equity()[0]
    nong, core = eps_paths(name, eps_src)
    E = core if basis == 'core' else nong
    E = {y: v * eps_mult for y, v in E.items()}
    f = A[name]['f']
    vps = {int(k): v for k, v in f['vps'].items()}
    surv = {int(k): v for k, v in f['surv'].items()}
    rows, acc = [], 0.0
    totw = sum(W.values())
    for t in sorted(W):
        g3 = ((E[t + 4] / E[t + 1]) ** (1 / 3) - 1) * 100 if E[t + 1] > 0 and E[t + 4] > 0 else 0.0
        s_after = surv[45] / surv[t] if surv_on else 1.0
        s_to_t = surv[t] if surv_on else 1.0
        a = peer * E[t + 1] * s_after
        per_b = max(peg * max(min(g3, 35.0), 0.0), 1 / r_e)
        b = per_b * E[t + 1] * s_after
        c = vps[t]
        target = (a + b + c) / 3 if c_on else (a + b) / 2
        yrs = T0 + (t - 27)
        divs = 1.00 * s_to_t / (1 + r_e) ** (T0 / 2)
        divs += sum(2.0 * surv[k] / (1 + r_e) ** (T0 + (k - 27) - 0.5) for k in range(28, t + 1))
        pv = target * s_to_t / (1 + r_e) ** yrs + divs
        rows.append(dict(t=t, g3=g3, eps_next=E[t + 1], a=a, b=b, per_b=per_b, c=c, target=target, pv=pv, w=W[t] / totw,
                         per_implied=target / E[t + 1]))
        acc += pv * W[t] / totw
    return acc, rows


def weighted(**kw):
    vals = {n: fair(n, **kw)[0] for n in ('ベース', '強気', '弱気')}
    return 0.5 * vals['ベース'] + 0.25 * vals['強気'] + 0.25 * vals['弱気'], vals


if __name__ == '__main__':
    r_e, ba, bl, de = r_equity()
    print('株主資本コスト %.2f%%(資産β %.2f → 株主β %.2f、D/E %.2f)' % (r_e * 100, ba, bl, de))
    tot, vals = weighted()
    res = {}
    for n in ('ベース', '強気', '弱気'):
        v, rows = fair(n)
        res[n] = dict(value=v, rows=rows)
        print('=====', n, '%.1f' % v)
        for x in rows:
            print('  FY%d末: 事業実態EPS(翌年) %.2f 3年成長 %.1f%% | a %.0f / b %.0f(PER %.1f)/ c %.0f → 目標 %.0f(暗黙PER %.1f) → 今日 %.0f(重み %.0f%%)'
                  % (x['t'], x['eps_next'], x['g3'], x['a'], x['b'], x['per_b'], x['c'], x['target'], x['per_implied'], x['pv'], x['w'] * 100))
    print('\n確率加重 %.1f(株価 %.2f の %.2f 倍)' % (tot, PRICE, tot / PRICE))
    dcf = 0.5 * A['ベース']['vps'] + 0.25 * A['強気']['vps'] + 0.25 * A['弱気']['vps']
    print('照合 DCF 加重 %.1f(ベース %.1f、強気 %.1f、弱気 %.1f)' % (dcf, A['ベース']['vps'], A['強気']['vps'], A['弱気']['vps']))
    # 比較: 第4.1版の作り方に近い設定
    print('\n--- 感応度(加重)')
    sens = {}
    for lab, kw in [('同業 PER 20', dict(peer=20)), ('同業 PER 26', dict(peer=26)), ('PEG 0.8', dict(peg=0.8)), ('PEG 1.2', dict(peg=1.2)),
                    ('重み 均等', dict(W={27: .25, 28: .25, 29: .25, 30: .25})), ('重み FY27末のみ', dict(W={27: 1.0})), ('重み FY28末のみ', dict(W={28: 1.0})),
                    ('r_e 9.85%(第4.1版)', dict(r_e=0.09853)), ('r_e 12%', dict(r_e=0.12)), ('EPS −10%', dict(eps_mult=0.9)), ('EPS +10%', dict(eps_mult=1.1)),
                    ('EPS = 需給エンジン', dict(eps_src='engine')), ('EPS = コンセンサス(説明会の前)', dict(eps_src='cons')), ('非GAAP EPS に同業 PER(第4.1版の基準)', dict(basis='nongaap')),
                    ('倒産確率を経路 c だけ(第4.1版)', dict(surv_on=False)), ('経路 c を除く(a・b のみ)', dict(c_on=False))]:
        w, _ = weighted(**kw)
        sens[lab] = w
        print('  %-34s %.1f(%+.1f)' % (lab, w, w - tot))
    # 市場の暗黙確率(定義を3つ)
    print('\n--- 株価が示す弱気の確率')
    imp = {}
    for p in (PRICE, 130.53, 144.54):
        mix = (0.5 * vals['ベース'] + 0.25 * vals['強気']) / 0.75
        d1 = (mix - p) / (mix - vals['弱気'])
        d2 = (vals['ベース'] - p) / (vals['ベース'] - vals['弱気'])
        dmix = (0.5 * A['ベース']['vps'] + 0.25 * A['強気']['vps']) / 0.75
        d3 = (dmix - p) / (dmix - A['弱気']['vps'])
        r_e0 = r_equity(p)[0]
        per_mkt = (p * (1 + r_e0) ** T0 - 1.0) / eps_paths('ベース')[1][28]
        imp[p] = dict(d1=d1, d2=d2, d3=d3, per_mkt_core28=per_mkt)
        print('  株価 %.2f: 定義1(強気:ベース=1:2)%.0f%% / 定義2(ベースと弱気の2点)%.0f%% / 定義3(DCF の値で定義1)%.0f%% / FY27末の暗黙PER(事業実態 FY28 EPS 比)%.1f 倍'
              % (p, d1 * 100, d2 * 100, d3 * 100, per_mkt))
    json.dump(dict(total=tot, vals=vals, res=res, dcf=dcf, r_e=r_e, beta=(ba, bl, de), sens=sens, implied={str(k): v for k, v in imp.items()},
                   eps={n: dict(zip(('nongaap', 'core'), eps_paths(n))) for n in ('ベース', '強気', '弱気')}, company=company_path()),
              open('out/m9_fair.json', 'w'), ensure_ascii=False, indent=1, default=float)
