"""Okta(OKTA)の計算スクリプト。報告書 OKTA_report.md の数値はすべてこの出力に一致させる。

実行: python3 analysis/OKTA_calc.py   (作業ルートから。CSV と summary.json を analysis/ に書き出す)
規約: 00_standard.md(§3 事業実態EPS、§3-1 株数、§3-2 定常状態経由、§4 12か月目標株価)、valuation_lib.py。
決算期末: 1月31日。FY2027 = 2026-02-01〜2027-01-31。
入力の出所は各定数の横に記す(取得日はすべて 2026-10-11)。
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import math
import os
import sys

sys.path.insert(0, '/home/user/AI/reports/security-stocks-2026-10/build')
import valuation_lib as vl  # noqa: E402

ROOT = '/home/user/AI/reports/security-stocks-2026-10'
OUT = os.path.join(ROOT, 'analysis')

# ----------------------------------------------------------------------------------------------
# 0. 検証済みの入力(出所: IR=会社IR/SEC、T3=主要報道・集計サイト)
# ----------------------------------------------------------------------------------------------
PRICE = 232.13                 # 2026-10-09 終値(統括が Morningstar・CNBC で確認、Macrotrends と一致)
BASIC_SH = 174.82              # 2026-08-24 の発行済株式(10-Q 表紙 Class A+B、IR)
DIL_SH_GAAP = 178.808          # FY27 Q2 の GAAP 希薄化後加重平均株数(10-Q、IR)= 事業実態EPSの分母(§3-1)
NONGAAP_SH_FY27 = 184.0        # FY27 通期 non-GAAP EPS ガイダンスの前提株数(IR 2026-08-26)
NONGAAP_SH_Q2 = 194 / 1.05     # FY27 Q2 の non-GAAP 純利益 194 ÷ EPS 1.05(IR)≒184.8
CASH = 2299.0                  # 現金+短期投資 2026-07-31(IR)。2026年満期転換社債 350 は 2026-06 に現金決済、有利子負債なし
TAX = 0.21                     # non-GAAP 長期税率(FY27 から 26%→21%、IR 2026-05-28)
R = vl.COST_OF_CAPITAL         # 9%
SH_GROWTH = -0.005             # non-GAAP 希薄化後株数の年変化(Q2FY26 185.7→Q2FY27 184.8 ≒ −0.5%)

MCAP_BASIC = PRICE * BASIC_SH / 1000     # US$ bn
MCAP_DIL = PRICE * DIL_SH_GAAP / 1000
EV_DIL = MCAP_DIL - CASH / 1000

FY = {y: dt.date(2000 + y, 1, 31) for y in range(25, 39)}   # FY25 → 2025-01-31

# 年度実績(IR): 売上、non-GAAP EPS、SBC
ACT = {
    25: dict(rev=2610, adj_eps=2.81, sbc=565, fcf=730),
    26: dict(rev=2919, adj_eps=3.50, sbc=544, fcf=863, nongaap_oi=766),
}

# 四半期(IR。* は前年比・通期合計からの逆算値で、報告書で明記)
Q = [
    # period, rev, sub, crpo, rpo, sbc, fcf, adj_eps, nrr, cust100k, newprod_share
    ('FY25Q1', 617, None, 1953.5, 3375, None, None, None, 111, None, None),   # rev* crpo* rpo*
    ('FY25Q2', 646, None, 2004.4, 3519, None, None, None, None, None, None),  # rev* crpo* rpo*
    ('FY25Q3', 665, 651.2, 2060.2, 3668, None, None, None, None, None, None), # rev* sub(推計) crpo* rpo*
    ('FY25Q4', 682, 667.9, 2248, 4215, 131, 284, 0.78, 107, None, None),      # sub(推計)
    ('FY26Q1', 688, 673, 2227, 4084, 128, 238, 0.86, 106, None, None),
    ('FY26Q2', 728, 711, 2265, 4152, 144, 162, 0.91, 106, 4958, None),        # cust100k*(Q2FY27 +6% から逆算)
    ('FY26Q3', 742, 724, 2328, 4292, 138, 211, 0.82, 106, None, None),
    ('FY26Q4', 761, 747, 2513, 4827, 134, 252, 0.90, 106, 5100, None),
    ('FY27Q1', 765, 750, 2499, 4719, 117, 271, 0.91, None, None, 0.25),       # 新製品比率は二次情報
    ('FY27Q2', 805, 793, 2585, 4858, 114, 227, 1.05, 107, 5255, 0.30),        # 新製品比率は説明会要約
]
GUIDE_Q3_CRPO = (2590, 2600)   # IR 2026-08-26
GUIDE_FY27 = dict(rev=(3216, 3226), eps=(3.90, 3.94), oi=(830, 840), fcf=(910, 930))

# コンセンサス(統括の検証値。TradingView 直接取得不可): 調整後EPS、売上
CONS_EPS = {27: 3.93, 28: 4.36, 29: 4.89}
CONS_REV = {27: 3221.0, 28: 3550.0, 29: 3905.0}   # FY27=ガイダンス中央、FY28=Yahoo(古い可能性)、FY29=欠損→FY28比+10%の仮定


def fmt(x, n=2):
    return f'{x:,.{n}f}'


print('=' * 100)
print('OKTA 計算ログ  基準日 2026-10-11 / 株価 2026-10-09 終値', PRICE)
print(f'時価総額(基本株数)= {MCAP_BASIC:.2f} bn / 時価総額(GAAP希薄化後)= {MCAP_DIL:.2f} bn / '
      f'ネットキャッシュ = {CASH/1000:.2f} bn / EV(希薄化後)= {EV_DIL:.2f} bn')

# ----------------------------------------------------------------------------------------------
# 1. 根幹KPIの加速度(F18)
# ----------------------------------------------------------------------------------------------
f18 = []
idx = {p[0]: i for i, p in enumerate(Q)}
names = ['rev', 'sub', 'crpo', 'rpo', 'sbc', 'fcf', 'adj_eps', 'nrr', 'cust100k', 'newprod']
series = {n: [q[i + 1] for q in Q] for i, n in enumerate(names)}
periods = [q[0] for q in Q]


def yoy(arr, i):
    if i < 4 or arr[i] is None or arr[i - 4] is None:
        return None
    return arr[i] / arr[i - 4] - 1


def ttm(arr, i):
    if i < 3 or any(arr[j] is None for j in range(i - 3, i + 1)):
        return None
    return sum(arr[i - 3:i + 1])


def qoq_ann(arr, i):
    if i < 1 or arr[i] is None or arr[i - 1] is None:
        return None
    return (arr[i] / arr[i - 1]) ** 4 - 1


rows18 = []
# 売上(フロー): TTM YoY と単四半期 YoY
for k, label in [('rev', '売上高'), ('sub', 'サブスクリプション売上')]:
    arr = series[k]
    prev = None
    for i, p in enumerate(periods):
        if arr[i] is None:
            continue
        q_yoy = yoy(arr, i)
        t_now, t_prev = ttm(arr, i), (ttm(arr, i - 4) if i >= 4 else None)
        t_yoy = (t_now / t_prev - 1) if (t_now and t_prev) else None
        sd = (q_yoy - prev) if (q_yoy is not None and prev is not None) else None
        rows18.append((label, p, arr[i], qoq_ann(arr, i), q_yoy, t_yoy, sd))
        prev = q_yoy if q_yoy is not None else prev
# cRPO・RPO(ストック): 水準の YoY と QoQ年率(季節性あり)
for k, label in [('crpo', 'cRPO'), ('rpo', 'RPO')]:
    arr = series[k]
    prev = None
    for i, p in enumerate(periods):
        q_yoy = yoy(arr, i)
        sd = (q_yoy - prev) if (q_yoy is not None and prev is not None) else None
        rows18.append((label, p, arr[i], qoq_ann(arr, i), q_yoy, q_yoy, sd))
        prev = q_yoy if q_yoy is not None else prev
# cRPO の純増(季節性を前年同期比で除く)
crpo = series['crpo']
nn = {}
for i, p in enumerate(periods):
    if i >= 1:
        nn[p] = crpo[i] - crpo[i - 1]
ttm_nn = {}
for i, p in enumerate(periods):
    if i >= 4:
        ttm_nn[p] = crpo[i] - crpo[i - 4]
prev = None
for i, p in enumerate(periods):
    if p in ttm_nn and periods[i - 4] in ttm_nn:
        g = ttm_nn[p] / ttm_nn[periods[i - 4]] - 1
    else:
        g = None
    if p in ttm_nn:
        sd = (g - prev) if (g is not None and prev is not None) else None
        rows18.append(('cRPO 純増(TTM)', p, ttm_nn[p], None, g, g, sd))
        prev = g if g is not None else prev
# NRR、SBC/売上、FCFマージン、10万ドル超顧客、新製品比率
prev = None
for i, p in enumerate(periods):
    v = series['nrr'][i]
    if v is None:
        continue
    sd = (v - prev) / 100 if prev is not None else None
    rows18.append(('NRR(TTM、%)', p, v, None, None, None, sd))
    prev = v
prev = None
for i, p in enumerate(periods):
    s, r_ = series['sbc'][i], series['rev'][i]
    if s is None:
        continue
    ratio = s / r_
    t_s, t_r = ttm(series['sbc'], i), ttm(series['rev'], i)
    t_ratio = t_s / t_r if t_s else None
    sd = (ratio - prev) if prev is not None else None
    rows18.append(('SBC/売上(単四半期)', p, ratio, None, (s / series['sbc'][i - 4] - 1) if (i >= 4 and series['sbc'][i - 4]) else None, t_ratio, sd))
    prev = ratio
for i, p in enumerate(periods):
    t_f, t_r = ttm(series['fcf'], i), ttm(series['rev'], i)
    if t_f:
        rows18.append(('FCFマージン(TTM)', p, t_f / t_r, None, None, None, None))
for i, p in enumerate(periods):
    v = series['cust100k'][i]
    if v:
        rows18.append(('ACV10万ドル超の顧客数', p, v, None, None, None, None))
for i, p in enumerate(periods):
    v = series['newprod'][i]
    if v:
        rows18.append(('新製品の契約獲得比率', p, v, None, None, None, None))

print('\n[F18] 根幹KPIの加速度(QoQ年率は季節性を含む。cRPO は Q4 が季節的に高い)')
for r_ in rows18:
    print('  ', r_[0], r_[1], fmt(r_[2], 3) if isinstance(r_[2], float) else r_[2],
          'QoQ年率=' + (f'{r_[3]*100:.1f}%' if r_[3] is not None else '-'),
          'YoY=' + (f'{r_[4]*100:.1f}%' if r_[4] is not None else '-'),
          'TTM=' + (f'{r_[5]*100:.1f}%' if r_[5] is not None else '-'),
          '2階差分=' + (f'{r_[6]*100:+.1f}pt' if r_[6] is not None else '-'))

with open(os.path.join(OUT, 'OKTA_F18.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['kpi', 'period', 'value', 'qoq_annualized', 'ttm_yoy', 'second_diff', 'single_q_yoy'])
    for r_ in rows18:
        w.writerow([r_[0], r_[1], round(r_[2], 4) if isinstance(r_[2], float) else r_[2],
                    None if r_[3] is None else round(r_[3], 4), None if r_[5] is None else round(r_[5], 4),
                    None if r_[6] is None else round(r_[6], 4), None if r_[4] is None else round(r_[4], 4)])

# ----------------------------------------------------------------------------------------------
# 2. 収益ラインの時系列(F10)と、増収の源泉分解・エンジン式の照合
# ----------------------------------------------------------------------------------------------
f10 = []
for i, p in enumerate(periods):
    if series['sub'][i] is None:
        continue
    f10.append((p, 'サブスクリプション', series['sub'][i]))
    f10.append((p, 'プロフェッショナルサービス他', round(series['rev'][i] - series['sub'][i], 1)))
with open(os.path.join(OUT, 'OKTA_F10.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['period', 'line', 'revenue_usd_mn', 'note'])
    for p, line, v in f10:
        note = '推計(FY25のサブスク比率97.9%で按分)' if p in ('FY25Q3', 'FY25Q4') else 'IR'
        w.writerow([p, line, v, note])

sub = series['sub']
ttm_sub_now = ttm(sub, idx['FY27Q2'])          # Q3FY26〜Q2FY27
ttm_sub_prev = ttm(sub, idx['FY26Q2'])         # Q3FY25〜Q2FY26(Q3/Q4 FY25 は推計)
nrr = 1.07
expansion = ttm_sub_prev * (nrr - 1)
new_logo = ttm_sub_now - ttm_sub_prev * nrr
print(f'\n[増収の源泉分解] TTMサブスク {ttm_sub_prev:.0f}→{ttm_sub_now:.0f}(+{(ttm_sub_now/ttm_sub_prev-1)*100:.1f}%)'
      f' / 既存顧客の純拡張(NRR107%)= +{expansion:.0f}({expansion/ttm_sub_prev*100:.1f}pt)'
      f' / 新規顧客(残差)= +{new_logo:.0f}({new_logo/ttm_sub_prev*100:.1f}pt)')

# 受注残の転換係数 k = 翌4四半期のサブスク売上 ÷ 期末cRPO(エンジン式の照合: 受注残×転換係数)
k_q2fy25 = (651.2 + 667.9 + 673 + 711) / 2004.4
k_q2fy26 = ttm_sub_now / 2265
pred_q2fy26 = 2265 * k_q2fy25
print(f'[エンジン式の照合] k(Q2FY25)={k_q2fy25:.3f}, k(Q2FY26)={k_q2fy26:.3f}。'
      f'Q2FY26 cRPO×k(前年)= {pred_q2fy26:.0f} vs 実績 {ttm_sub_now:.0f}(差 {(pred_q2fy26/ttm_sub_now-1)*100:+.1f}%)')
ntm_from_crpo = {kk: 2585 * kk for kk in (1.30, k_q2fy26, k_q2fy25)}
for kk, v in ntm_from_crpo.items():
    print(f'   Q2FY27 cRPO 2,585 × k {kk:.3f} = 翌12か月サブスク {v:.0f}(TTM比 +{(v/ttm_sub_now-1)*100:.1f}%)')
ENGINE_CHECK_DIFF = pred_q2fy26 / ttm_sub_now - 1

# 原子単位: 10万ドル超顧客 5,255 社が ACV の約85%
acv_proxy = 793 * 4
acv_100k = acv_proxy * 0.85 / 5255 * 1000
acv_other = acv_proxy * 0.15 / (20000 - 5255) * 1000
print(f'[原子単位] サブスク年換算 {acv_proxy}、10万ドル超顧客の平均ACV ≈ {acv_100k:,.0f} 千ドル、その他 ≈ {acv_other:,.0f} 千ドル(総顧客2万社超で計算)')

# ユニットエコノミクス(推計)
sm_ann = 241 * 4                      # non-GAAP S&M 年換算(Q2FY27)
net_new_arr = ttm_sub_now - ttm_sub_prev
for churn in (0.05, 0.08):
    gross_new = net_new_arr + ttm_sub_prev * churn
    magic = net_new_arr * 0.819 / sm_ann
    print(f'[ユニットエコノミクス] 解約率{churn:.0%}: 総新規ACV≈{gross_new:.0f}、S&M年換算{sm_ann}、'
          f'総新規ACV/S&M={gross_new/sm_ann:.2f}、マジックナンバー(純増×粗利/S&M)={magic:.2f}')
# 増分ROIC(経済的損益): 成長S&M 1ドルが生む ACV と、その寿命
growth_sm_share = 0.6           # S&M のうち新規・拡張向けの比率(推計。残りは更新・既存管理)
acv_per_growth_dollar = (net_new_arr + ttm_sub_prev * 0.065) / (sm_ann * growth_sm_share)
contrib_margin = 0.819 - 0.10 - 0.10 - 0.07 - 0.06   # 粗利 − 維持S&M − 維持R&D − G&A − 定常SBC
life_churn = 0.065
for lbl, a in [('中央', acv_per_growth_dollar)]:
    roic = a * contrib_margin * (1 - TAX) - life_churn * 1.0
    print(f'[増分ROIC] 成長S&M 1ドル当たりACV={a:.2f}、寄与率{contrib_margin:.1%}、税後寄与={a*contrib_margin*(1-TAX):.2f}/年、'
          f'寿命の減耗{life_churn:.1%} → 増分ROIC ≈ {roic*100:.0f}%(推計)')
INCR_ROIC = acv_per_growth_dollar * contrib_margin * (1 - TAX) - life_churn

# ----------------------------------------------------------------------------------------------
# 3. EPS品質フォレンジック: FY26→FY27(コンセンサス)の対数分解
# ----------------------------------------------------------------------------------------------
ni26 = 3.50 * 185.5            # FY26 non-GAAP 純利益(株数は Q2FY26 の 185.7 前後で近似)
ni27 = CONS_EPS[27] * NONGAAP_SH_FY27
pt26, pt27 = ni26 / (1 - 0.26), ni27 / (1 - TAX)
oi26, oi27 = 766.0, 835.0
oth26, oth27 = pt26 - oi26, pt27 - oi27
d = vl.eps_log_decomposition(2919, 3221, ni26 / 2919, ni27 / 3221, 185.5, NONGAAP_SH_FY27)
tax_eff = math.log((1 - TAX) / (1 - 0.26))
opm_eff = math.log((oi27 / 3221) / (oi26 / 2919))
pretax_eff = math.log((pt27 / oi27) / (pt26 / oi26))
print(f'\n[EPS対数分解 FY26→FY27] 合計 {d["total"]*100:.1f}% = 売上 {d["revenue"]*100:.1f} + 純利益率 {d["margin"]*100:.1f}'
      f'(うち 営業利益率 {opm_eff*100:.1f} / 営業外 {pretax_eff*100:.1f} / 税率 {tax_eff*100:.1f}) + 株数 {d["dilution"]*100:.1f}')
print(f'   営業外収益(推計): FY26 {oth26:.0f} → FY27 {oth27:.0f}(自社株買い・社債償還で受取利息が減少)')
LOGDEC = dict(total=d['total'], revenue=d['revenue'], margin=d['margin'], opm=opm_eff, other=pretax_eff, tax=tax_eff, shares=d['dilution'])

# ----------------------------------------------------------------------------------------------
# 4. 経路の構築(コンセンサス/会社シナリオ/事業エンジン/弱気)
# ----------------------------------------------------------------------------------------------
SBC27 = 231 + 2 * 117           # H1 実績 231 + H2 推計(Q2 114・Q1 117 の水準)
SBC27_RATIO = SBC27 / CONS_REV[27]
print(f'\n[SBC] FY27 推計 {SBC27} = 売上比 {SBC27_RATIO*100:.1f}%(FY25 21.6%、FY26 18.6%、TTM 16.4%、Q2FY27 14.2%)')


def shares_ng(y):
    return NONGAAP_SH_FY27 * (1 + SH_GROWTH) ** (y - 27)


def other_income(y, bear=False):
    if bear:
        return 75.0
    return {27: 78.0}.get(y, 78.0 + 8.0 * (y - 27) + (0 if y < 28 else 0))


def path_from_drivers(rev27, growth, opm, sbc, extra=None, bear=False):
    """売上×営業利益率+営業外 → 税引後 = non-GAAP 純利益。SBC 控除後を GAAP 希薄化後株数で割る(§3-1)。"""
    out = {}
    rev = rev27
    for y in range(27, 39):
        if y > 27:
            rev = rev * (1 + growth[y])
        add = (extra or {}).get(y, 0.0)
        tot = rev + add
        oi = tot * opm[y]
        ni = (oi + other_income(y, bear)) * (1 - TAX)
        sbc_v = tot * sbc[y]
        adj = ni / shares_ng(y)
        be = vl.business_eps_fixed_shares(adj, shares_ng(y), sbc_v, DIL_SH_GAAP, TAX)
        out[y] = dict(rev=tot, core=rev, agent=add, opm=opm[y], ni=ni, sbc=sbc_v, sbc_ratio=sbc[y], adj=adj, be=be,
                      ext=False)
    return out


def interp(d0, keys):
    return {k: d0[k] for k in keys}


YRS = list(range(27, 39))

# --- コンセンサス経路: FY27〜FY29 はコンセンサス EPS、FY30 以降は延長(売上+10→7.5%、純利益率+0.5pt/年)
sbc_cons = {27: SBC27_RATIO, 28: 0.130, 29: 0.120, 30: 0.110, 31: 0.100, 32: 0.090, 33: 0.085, 34: 0.080, 35: 0.075,
            36: 0.07, 37: 0.07, 38: 0.07}
cons = {}
for y in (27, 28, 29):
    ni = CONS_EPS[y] * shares_ng(y)
    sbc_v = CONS_REV[y] * sbc_cons[y]
    cons[y] = dict(rev=CONS_REV[y], core=CONS_REV[y], agent=0, ni=ni, sbc=sbc_v, sbc_ratio=sbc_cons[y], adj=CONS_EPS[y],
                   be=vl.business_eps_fixed_shares(CONS_EPS[y], shares_ng(y), sbc_v, DIL_SH_GAAP, TAX), ext=(y == 29 and False),
                   opm=None)
nim = cons[29]['ni'] / cons[29]['rev']
rev = cons[29]['rev']
g_ext = {30: 0.10, 31: 0.095, 32: 0.09, 33: 0.085, 34: 0.08, 35: 0.075, 36: 0.07, 37: 0.065, 38: 0.06}
for y in range(30, 39):
    rev *= 1 + g_ext[y]
    nim += 0.005
    ni = rev * nim
    sbc_v = rev * sbc_cons[y]
    adj = ni / shares_ng(y)
    cons[y] = dict(rev=rev, core=rev, agent=0, ni=ni, sbc=sbc_v, sbc_ratio=sbc_cons[y], adj=adj,
                   be=vl.business_eps_fixed_shares(adj, shares_ng(y), sbc_v, DIL_SH_GAAP, TAX), ext=True, opm=None)

# --- 事業エンジン経路: cRPO+14%・新製品の上乗せ・NRR 107% を根拠に売上 +12%前後、営業レバレッジ、SBC比率の低下
eng = path_from_drivers(
    3240.0,
    growth={28: 0.120, 29: 0.125, 30: 0.120, 31: 0.115, 32: 0.110, 33: 0.10, 34: 0.09, 35: 0.08, 36: 0.07, 37: 0.065, 38: 0.06},
    opm={27: 0.265, 28: 0.275, 29: 0.290, 30: 0.305, 31: 0.315, 32: 0.325, 33: 0.335, 34: 0.34, 35: 0.345, 36: 0.35, 37: 0.35, 38: 0.35},
    sbc={27: SBC27_RATIO, 28: 0.125, 29: 0.110, 30: 0.100, 31: 0.090, 32: 0.080, 33: 0.075, 34: 0.070, 35: 0.065, 36: 0.06, 37: 0.06, 38: 0.06},
)
for y in range(33, 39):
    eng[y]['ext'] = True

# --- 会社シナリオ経路: 中核 +13%前後 + エージェント単位の課金(FY32 に約9.5億ドル)。経営陣の「エージェント向け市場は IAM を超えうる」を翻訳
agent = {27: 0, 28: 30, 29: 120, 30: 300, 31: 600, 32: 950, 33: 1300, 34: 1650, 35: 2000, 36: 2300, 37: 2550, 38: 2750}
comp = path_from_drivers(
    3240.0,
    growth={28: 0.13, 29: 0.13, 30: 0.13, 31: 0.125, 32: 0.12, 33: 0.11, 34: 0.10, 35: 0.09, 36: 0.08, 37: 0.07, 38: 0.06},
    opm={27: 0.265, 28: 0.285, 29: 0.305, 30: 0.325, 31: 0.34, 32: 0.35, 33: 0.36, 34: 0.365, 35: 0.37, 36: 0.37, 37: 0.37, 38: 0.37},
    sbc={27: SBC27_RATIO, 28: 0.125, 29: 0.110, 30: 0.095, 31: 0.085, 32: 0.075, 33: 0.07, 34: 0.065, 35: 0.06, 36: 0.06, 37: 0.06, 38: 0.06},
    extra=agent,
)
for y in range(33, 39):
    comp[y]['ext'] = True

# --- 弱気パス: Microsoft のバンドル+顧客の人員削減(座席の縮小)+統合プラットフォームとの競争で成長が 8%→5.5% へ減速。
#     経営陣の反応(成長向けS&Mの削減)で利益率は緩やかに上がるが、SBC 比率の低下は遅い(人材の引き留め)
bear = path_from_drivers(
    3221.0,
    growth={28: 0.080, 29: 0.070, 30: 0.065, 31: 0.060, 32: 0.055, 33: 0.05, 34: 0.05, 35: 0.045, 36: 0.04, 37: 0.04, 38: 0.035},
    opm={27: 0.260, 28: 0.265, 29: 0.275, 30: 0.285, 31: 0.295, 32: 0.305, 33: 0.31, 34: 0.315, 35: 0.32, 36: 0.32, 37: 0.32, 38: 0.32},
    sbc={27: SBC27_RATIO, 28: 0.140, 29: 0.135, 30: 0.130, 31: 0.125, 32: 0.120, 33: 0.115, 34: 0.11, 35: 0.105, 36: 0.10, 37: 0.10, 38: 0.10},
    bear=True,
)
for y in range(33, 39):
    bear[y]['ext'] = True
for y in range(30, 33):
    pass

PATHS = {'consensus': cons, 'company': comp, 'engine': eng, 'bear': bear}
JP = {'consensus': 'コンセンサス', 'company': '会社シナリオ', 'engine': '事業エンジン', 'bear': '弱気'}

print('\n[経路別 年度EPS](調整後EPS / 事業実態EPS / 売上 / SBC比率)。FY30 以降は延長部分(コンセンサス経路)')
for k, p in PATHS.items():
    print('  ', JP[k])
    for y in range(27, 36):
        e = p[y]
        print(f'     FY{2000+y}: 売上 {e["rev"]:,.0f}(うちエージェント {e["agent"]:,.0f})、調整後EPS {e["adj"]:.2f}、'
              f'事業実態EPS {e["be"]:.2f}、SBC比率 {e["sbc_ratio"]*100:.1f}%' + (' [延長]' if e['ext'] else ''))


def be_map(p):
    return {FY[y]: p[y]['be'] for y in YRS}


def adj_map(p):
    return {FY[y]: p[y]['adj'] for y in YRS}


# ----------------------------------------------------------------------------------------------
# 5. 許容PEG(3経路)と年度別PEGレンジ
# ----------------------------------------------------------------------------------------------
PEG_A = (5.1, 6.1)        # 同一基準ピアの実勢(調整後PEG、peer_peg_table.md)。許容値の根拠には使わない
PEG_B = (1.0, 1.4)        # 慣行: 1〜1.5。3年 g の一部が SBC 比率の低下(有限の源泉)なので上限を 1.4 に置く
PEG_C = (1.15, 1.5)       # 構造評価B(1.0〜1.3)+CAP約10年(+0.1)+ストック比率・定常状態利益率との差(+0.1)+エージェントの選択肢(+0.05)−下振れ機構(−0.05)
PEG_ADOPT = (1.2, 1.45)
# 年度別PEG(質の高い成長源への移行に合わせて緩やかに上げる)
PEG_BY_FY = {
    'consensus': {27: (1.10, 1.30), 28: (1.20, 1.40), 29: (1.25, 1.45), 30: (1.30, 1.50), 31: (1.30, 1.50), 32: (1.30, 1.50)},
    'engine': {27: (1.10, 1.30), 28: (1.20, 1.45), 29: (1.25, 1.50), 30: (1.30, 1.55), 31: (1.35, 1.60), 32: (1.35, 1.60)},
    'company': {27: (1.20, 1.40), 28: (1.30, 1.55), 29: (1.40, 1.65), 30: (1.45, 1.70), 31: (1.50, 1.75), 32: (1.50, 1.80)},
    'bear': {27: (0.80, 1.00), 28: (0.85, 1.00), 29: (0.85, 1.05), 30: (0.90, 1.05), 31: (0.90, 1.10), 32: (0.90, 1.10)},
}
PEG_12M = {'consensus': (1.20, 1.45), 'engine': (1.20, 1.45), 'company': (1.35, 1.65), 'bear': (0.85, 1.05)}

# ----------------------------------------------------------------------------------------------
# 6. 年度別適正株価(F13)と 12か月目標株価(規約どおり / 定常状態経由)
# ----------------------------------------------------------------------------------------------
# --- 下値の床(00_standard §3-3): 1株当たり定常状態価値 = 定常状態利益 ÷ 9% ÷ 希薄化後株数 + 1株当たり純現金
#     中央: 定常状態の営業利益率42%(SBC控除後)。弱気: 36%(Microsoft のバンドルによる長い尾の値下げ −3pt、
#     防衛的な維持費の増加 −3pt)かつ売上の基盤 −2%(顧客の人員削減による座席の縮小)。
SS_M_CENTRAL, SS_M_BEAR, BEAR_SEAT_LOSS = 0.42, 0.36, 0.02


def ss_floor(rev, margin):
    return vl.steady_state_value_per_share(rev * margin * (1 - TAX), DIL_SH_GAAP) + CASH / DIL_SH_GAAP


def floor_for(k, rev):
    if k == 'bear':
        return ss_floor(rev * (1 - BEAR_SEAT_LOSS), SS_M_BEAR)
    return ss_floor(rev, SS_M_CENTRAL)


FLOOR_NOW = {k: floor_for(k, 3221.0) for k in ('consensus', 'company', 'engine', 'bear')}
print(f'\n[下値の床 §3-3] 定常状態価値/株(FY27売上3,221基準・現金込み): 中央42% = {FLOOR_NOW["consensus"]:.1f}、'
      f'弱気36%・座席−2% = {FLOOR_NOW["bear"]:.1f}(現金を除くと {FLOOR_NOW["consensus"]-CASH/DIL_SH_GAAP:.1f} / {FLOOR_NOW["bear"]-CASH/DIL_SH_GAAP:.1f})')
bear_ss_earn = 3221 * (1 - BEAR_SEAT_LOSS) * SS_M_BEAR * (1 - TAX)
cen_ss_earn = 3221 * SS_M_CENTRAL * (1 - TAX)
print(f'   定常状態利益: 中央 {cen_ss_earn:.0f} → 弱気 {bear_ss_earn:.0f}(差 {bear_ss_earn-cen_ss_earn:.0f}: 値下げ {-3221*0.03*(1-TAX):.0f}、'
      f'維持費 {-3221*0.03*(1-TAX):.0f}、座席 {-(3221*0.02)*SS_M_BEAR*(1-TAX):.0f})')

f13 = []
for k, p in PATHS.items():
    for y in range(27, 33):
        e0, e3 = p[y]['be'], p[y + 3]['be']
        g = vl.cagr(e0, e3, 3)
        lo, hi = PEG_BY_FY[k][y]
        fp_lo, fp_hi = vl.fair_per(lo, g)['capped'], vl.fair_per(hi, g)['capped']
        fl = floor_for(k, p[y]['rev'])
        pr_lo, pr_hi = fp_lo * e0, fp_hi * e0
        f13.append(dict(fy_end=FY[y].isoformat(), path=JP[k], business_eps=round(e0, 3), g_3y=round(g, 4), peg_low=lo, peg_high=hi,
                        fair_per_low=round(fp_lo, 1), fair_per_high=round(fp_hi, 1), fair_price_low=round(max(pr_lo, fl), 1),
                        fair_price_high=round(max(pr_hi, fl), 1), is_extension=bool(p[y]['ext'] or p[y + 3]['ext']),
                        peg_price_low=round(pr_lo, 1), peg_price_high=round(pr_hi, 1), floor_price=round(fl, 1),
                        floor_applied=bool(pr_lo < fl)))
with open(os.path.join(OUT, 'OKTA_F13.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(f13[0].keys()))
    w.writeheader()
    w.writerows(f13)
print('\n[F13] 年度別適正株価(その年度の事業実態EPS × PEG × 3年 g)')
for r_ in f13:
    print(f'   {r_["path"]} {r_["fy_end"]}: EPS {r_["business_eps"]:.2f} g {r_["g_3y"]*100:.1f}% PEG {r_["peg_low"]}〜{r_["peg_high"]}'
          f' PER {r_["fair_per_low"]}〜{r_["fair_per_high"]} PEG価格 {r_["peg_price_low"]}〜{r_["peg_price_high"]} 床 {r_["floor_price"]}'
          f' → 適正株価 {r_["fair_price_low"]}〜{r_["fair_price_high"]}' + (' [床適用]' if r_['floor_applied'] else '') + (' [延長含む]' if r_['is_extension'] else ''))

T12 = {}
print('\n[12か月目標株価] 規約: 2027-10-11 の NTM 事業実態EPS × PEG × g(同時点から3年の事業実態EPS CAGR)')
for k, p in PATHS.items():
    m = be_map(p)
    ntm0 = vl.ntm_eps(m, vl.TARGET_DATE)
    ntm3 = vl.ntm_eps(m, dt.date(2030, 10, 11))
    g = vl.cagr(ntm0, ntm3, 3)
    lo, hi = PEG_12M[k]
    mid = (lo + hi) / 2
    tp = {x: vl.target_price(ntm0, x, g) for x in (lo, mid, hi)}
    # 定常状態経由: FY32(FY+5)の事業実態EPS × 出口PER を 2027-10-11 まで割り引く
    g_exit = vl.cagr(p[32]['be'], p[35]['be'], 3)
    peg_exit = {'consensus': 1.5, 'engine': 1.5, 'company': 1.7, 'bear': 1.2}[k]
    ss = vl.steady_state_target(p[32]['be'], FY[32], peg_exit, g_exit)
    T12[k] = dict(ntm=ntm0, ntm3=ntm3, g=g, peg=(lo, mid, hi), per_mid=tp[mid]['per'], std_lo=tp[lo]['price'], std_mid=tp[mid]['price'],
                  std_hi=tp[hi]['price'], g_exit=g_exit, peg_exit=peg_exit, ss=ss['target'], per_exit=ss['per_exit'],
                  val_exit=ss['value_at_exit'], per_uncapped=tp[mid]['per_uncapped'])
    print(f'   {JP[k]}: NTM={ntm0:.2f} g3={g*100:.1f}% PEG {lo}〜{hi} → PER {tp[mid]["per"]:.1f}(中央) '
          f'目標 {tp[lo]["price"]:.0f}〜{tp[hi]["price"]:.0f}(中央 {tp[mid]["price"]:.1f}) | 定常状態経由: FY32 EPS {p[32]["be"]:.2f}'
          f' 出口g {g_exit*100:.1f}% 出口PEG {peg_exit} 出口PER {ss["per_exit"]:.1f} → {ss["target"]:.1f}')

# 採用: 規約どおりの値(中央)と定常状態経由の値の平均ではなく、どちらかを選ぶ(00_standard §3-2)。
# OKTA は FY+1 の事業実態EPSが調整後EPSの約5割残り、規約どおりの方法が安定する → 規約どおり(中央)を採用。定常状態経由は交差確認。
RULE_MID = {k: T12[k]['std_mid'] for k in PATHS}
ADOPT = {k: max(T12[k]['std_mid'], FLOOR_NOW[k]) for k in PATHS}
FLOOR_HIT = {k: T12[k]['std_mid'] < FLOOR_NOW[k] for k in PATHS}
print('   PEG法の値(PER下限11.1倍込み):', {JP[k]: round(v, 1) for k, v in RULE_MID.items()})
print('   床(§3-3):', {JP[k]: round(v, 1) for k, v in FLOOR_NOW.items()}, '→ 床が効いた経路:', [JP[k] for k, v in FLOOR_HIT.items() if v])
print('   採用(規約どおり・中央):', {JP[k]: round(v, 1) for k, v in ADOPT.items()})

# ----------------------------------------------------------------------------------------------
# 7. 交差確認: 事業実態利益の DCF(FY28〜FY38+永続成長3%)と、リバースDCF
# ----------------------------------------------------------------------------------------------
def dcf_value(p, at=vl.TARGET_DATE, r=R, g_term=0.03, net_cash=CASH):
    v = 0.0
    for y in range(28, 39):
        t = (FY[y] - at).days / 365.25
        if t <= 0:
            continue
        frac = 1.0
        if y == 28:  # 2027-10-11 以降の FY28 は4か月分
            frac = 4 / 12
        bni = p[y]['be'] * DIL_SH_GAAP
        v += frac * bni / (1 + r) ** t
    tv = p[38]['be'] * DIL_SH_GAAP * (1 + g_term) / (r - g_term)
    v += tv / (1 + r) ** ((FY[38] - at).days / 365.25)
    return (v + net_cash) / DIL_SH_GAAP


DCF = {k: dcf_value(p) for k, p in PATHS.items()}
print('\n[交差確認: 事業実態利益のDCF(r=9%、永続3%、2027-10-11時点)]', {JP[k]: round(v, 1) for k, v in DCF.items()})
DCF_now = {k: dcf_value(p, at=vl.VALUATION_DATE) for k, p in PATHS.items()}
# DCF の前提感応度と終価の比率(事業エンジン経路、2027-10-11 時点)
DCF_R = {r_: dcf_value(eng, r=r_) for r_ in (0.08, 0.09, 0.10)}
DCF_GT = {gt: dcf_value(eng, g_term=gt) for gt in (0.02, 0.03)}
_tv = eng[38]['be'] * DIL_SH_GAAP * 1.03 / (R - 0.03) / (1 + R) ** ((FY[38] - vl.TARGET_DATE).days / 365.25)
TV_SHARE = _tv / (DCF['engine'] * DIL_SH_GAAP)
print('   事業エンジンDCFの感応度: r', {k: round(v, 1) for k, v in DCF_R.items()}, '/ 永続成長', {k: round(v, 1) for k, v in DCF_GT.items()},
      f'/ 終価の比率 {TV_SHARE*100:.0f}%')
print('   同(2026-10-11 時点)', {JP[k]: round(v, 1) for k, v in DCF_now.items()})


def reverse_dcf(target_price):
    """エンジン経路の利益率・SBC比率の軌跡を固定し、FY28〜FY37 の一定の売上成長率を逆算(基準日時点)。"""
    lo, hi = 0.0, 0.40
    for _ in range(80):
        mid = (lo + hi) / 2
        gmap = {y: mid for y in range(28, 38)}
        gmap[38] = 0.03
        p = path_from_drivers(3240.0, gmap, {y: eng[y]['opm'] for y in YRS}, {y: eng[y]['sbc_ratio'] for y in YRS})
        v = dcf_value(p, at=vl.VALUATION_DATE)
        if v > target_price:
            hi = mid
        else:
            lo = mid
    return mid


RDCF_G = reverse_dcf(PRICE)
RDCF_G_hi_margin = None
# 利益率をより高く(FY32 以降 営業利益率40%、SBC 5%)置いた場合
def reverse_dcf2(target_price, opm_t=0.40, sbc_t=0.05):
    lo, hi = 0.0, 0.40
    opm = {y: min(opm_t, 0.267 + (opm_t - 0.267) * (y - 27) / 5) for y in YRS}
    sbc = {y: max(sbc_t, SBC27_RATIO - (SBC27_RATIO - sbc_t) * (y - 27) / 5) for y in YRS}
    for _ in range(80):
        mid = (lo + hi) / 2
        gmap = {y: mid for y in range(28, 38)}
        gmap[38] = 0.03
        p = path_from_drivers(3240.0, gmap, opm, sbc)
        v = dcf_value(p, at=vl.VALUATION_DATE)
        if v > target_price:
            hi = mid
        else:
            lo = mid
    return mid


RDCF_G2 = reverse_dcf2(PRICE)
print(f'[リバースDCF] 現在株価 {PRICE} が織り込む FY28〜FY37 の売上成長率(年率): {RDCF_G*100:.1f}%(エンジン経路の利益率・SBC比率)'
      f' / {RDCF_G2*100:.1f}%(営業利益率40%・SBC5%を FY32 までに達成する楽観的な利益率)')

# ----------------------------------------------------------------------------------------------
# 8. 成長の値段・価値の時間分布
# ----------------------------------------------------------------------------------------------
SS_MARGIN = (0.36, 0.42, 0.48)  # 定常状態の営業利益率(SBC控除後)。粗利82%−維持S&M 10〜12%−維持R&D 9〜10%−G&A 7%−定常SBC 6%=約45%、競争上の維持費を見込み 42% を中央
ss = {}
for m in SS_MARGIN:
    earn = 3221 * m * (1 - TAX)
    split = vl.steady_state_split(earn / 1000, MCAP_DIL - CASH / 1000)
    ss[m] = dict(earn=earn, ssv_ops=split['steady_state_value'], ssv_total=split['steady_state_value'] + CASH / 1000,
                 per_share=(split['steady_state_value'] + CASH / 1000) * 1000 / DIL_SH_GAAP,
                 growth_price=MCAP_DIL - (split['steady_state_value'] + CASH / 1000))
    ss[m]['growth_share'] = ss[m]['growth_price'] / MCAP_DIL
for m, v in ss.items():
    print(f'[成長の値段] 定常状態営業利益率 {m:.0%}: 定常状態利益 {v["earn"]:.0f} → 事業価値 {v["ssv_ops"]:.1f}bn + 現金 {CASH/1000:.1f}'
          f' = {v["ssv_total"]:.1f}bn(1株 {v["per_share"]:.0f})/ 成長の値段 {v["growth_price"]:.1f}bn(時価総額の {v["growth_share"]*100:.0f}%)')
SSC = ss[0.42]
for r_alt in (0.08, 0.10):
    print(f'   資本コスト {r_alt:.0%}: 定常状態価値(1株)= {(SSC["earn"]/1000/r_alt + CASH/1000)*1000/DIL_SH_GAAP:.0f}')

# 価値の時間分布(エンジン経路 DCF、基準日時点): 3年以内(FY28〜FY30)の利益の現在価値と、それ以降
def time_split(p, at=vl.VALUATION_DATE):
    near, far = 0.0, 0.0
    for y in range(28, 39):
        t = (FY[y] - at).days / 365.25
        pv = p[y]['be'] * DIL_SH_GAAP / (1 + R) ** t
        if y <= 30:
            near += pv
        else:
            far += pv
    tv = p[38]['be'] * DIL_SH_GAAP * 1.03 / (R - 0.03) / (1 + R) ** ((FY[38] - at).days / 365.25)
    far += tv
    near += CASH
    tot = near + far
    return near / tot, far / tot


TS = {k: time_split(p) for k, p in PATHS.items()}
print('[価値の時間分布] 3年以内(現金を含む)/ それ以降:', {JP[k]: (round(a, 2), round(b, 2)) for k, (a, b) in TS.items()})

# ----------------------------------------------------------------------------------------------
# 9. 芯の特定: 価値感度分析(エンジン経路、定常状態経由の目標とDCFの両方で測る)
# ----------------------------------------------------------------------------------------------
base_g = {28: 0.120, 29: 0.125, 30: 0.120, 31: 0.115, 32: 0.110, 33: 0.10, 34: 0.09, 35: 0.08, 36: 0.07, 37: 0.065, 38: 0.06}
base_opm = {y: eng[y]['opm'] for y in YRS}
base_sbc = {y: eng[y]['sbc_ratio'] for y in YRS}


def value_of(growth=None, opm=None, sbc=None, extra=None, peg_exit=1.5):
    p = path_from_drivers(3240.0, growth or base_g, opm or base_opm, sbc or base_sbc, extra=extra)
    g_exit = vl.cagr(p[32]['be'], p[35]['be'], 3)
    sst = vl.steady_state_target(p[32]['be'], FY[32], peg_exit, g_exit)['target']
    return sst, dcf_value(p)


v0_ss, v0_dcf = value_of()
sens = []
sens.append(('売上成長率(FY28〜32、±3pt)', value_of(growth={y: v + (0.03 if y <= 32 else 0) for y, v in base_g.items()}),
             value_of(growth={y: v - (0.03 if y <= 32 else 0) for y, v in base_g.items()})))
sens.append(('エージェント課金の売上(FY32に0→10億ドル、以降も拡大)', value_of(extra={y: v for y, v in agent.items()}), (v0_ss, v0_dcf)))
sens.append(('営業利益率(FY32時点 ±4pt)', value_of(opm={y: v + 0.04 * min(1, max(0, (y - 27) / 5)) for y, v in base_opm.items()}),
             value_of(opm={y: v - 0.04 * min(1, max(0, (y - 27) / 5)) for y, v in base_opm.items()})))
sens.append(('SBC/売上(FY32時点 ±3pt)', value_of(sbc={y: v - 0.03 * min(1, max(0, (y - 27) / 5)) for y, v in base_sbc.items()}),
             value_of(sbc={y: v + 0.03 * min(1, max(0, (y - 27) / 5)) for y, v in base_sbc.items()})))
sens.append(('出口PEG(CAP。1.5→1.8/1.2)', value_of(peg_exit=1.8), value_of(peg_exit=1.2)))
print(f'\n[価値感度分析] 基準(エンジン経路): 定常状態経由 {v0_ss:.1f} / DCF {v0_dcf:.1f}')
SENS = []
for name, up, dn in sens:
    SENS.append(dict(name=name, up_ss=up[0] - v0_ss, dn_ss=dn[0] - v0_ss, up_dcf=up[1] - v0_dcf, dn_dcf=dn[1] - v0_dcf))
    print(f'   {name}: 定常状態経由 {up[0]-v0_ss:+.1f}/{dn[0]-v0_ss:+.1f}  DCF {up[1]-v0_dcf:+.1f}/{dn[1]-v0_dcf:+.1f}')

# F12: シナリオ × PEG 感応度(NTM 事業実態EPS × PEG × g)と、SBC比率 × 売上成長 の DCF マトリクス
print('\n[F12] 経路 × PEG(12か月目標株価)')
F12 = {}
for k in PATHS:
    row = {}
    for peg in (1.0, 1.25, 1.5, 2.0, 3.0):
        row[peg] = vl.target_price(T12[k]['ntm'], peg, T12[k]['g'])['price']
    F12[k] = row
    print('   ', JP[k], {pk: round(v, 0) for pk, v in row.items()})
# 株価232ドルを正当化する PEG
PEG_IMPLIED = {k: PRICE / (T12[k]['ntm'] * T12[k]['g'] * 100) for k in PATHS}
print('   現在株価を正当化する PEG(2027-10 の NTM 事業実態EPS 基準):', {JP[k]: round(v, 2) for k, v in PEG_IMPLIED.items()})
print('[F12b] SBC比率(FY32)× 売上成長(FY28〜32 一律)の DCF 価値(2027-10-11、1株)')
F12b = {}
for sbc32 in (0.05, 0.08, 0.11, 0.14):
    row = {}
    for gg in (0.08, 0.11, 0.14, 0.17):
        sb = {y: (SBC27_RATIO + (sbc32 - SBC27_RATIO) * min(1, (y - 27) / 5)) for y in YRS}
        gm = {y: (gg if y <= 32 else base_g[y]) for y in base_g}
        p = path_from_drivers(3240.0, gm, base_opm, sb)
        row[gg] = dcf_value(p)
    F12b[sbc32] = row
    print(f'   SBC {sbc32:.0%}:', {f'{gg:.0%}': round(v, 0) for gg, v in row.items()})

# ----------------------------------------------------------------------------------------------
# 10. 最終判断: 2軸マトリクス・確率・非対称性・エントリー価格帯
# ----------------------------------------------------------------------------------------------
RATING = 'B'
EDGE = True   # 差分は「市場の過大評価」側(分析の優位)。即エントリー圏は理論上設けるが、現在株価からは遠い
GAPS = {k: vl.gap(ADOPT[k], PRICE) for k in PATHS}
PROBS = {'bear': 0.25, 'consensus': 0.35, 'engine': 0.30, 'company': 0.10}
EV_ = vl.expected_value(ADOPT, PROBS, PRICE)
ADOPTED_PATH = 'engine'
DEC = vl.decision(RATING, GAPS[ADOPTED_PATH], EDGE)
alpha = sum(vl.ALPHA_BY_RATING[RATING]) / 2
Z = vl.zones(B=ADOPT['engine'], U=ADOPT['company'], L=ADOPT['bear'], alpha=alpha, price=PRICE, edge=EDGE)
down = ADOPT['bear'] / PRICE - 1
up = ADOPT['company'] / PRICE - 1
print('\n[最終判断]')
print('   乖離:', {JP[k]: f'{v*100:+.1f}%' for k, v in GAPS.items()})
print(f'   確率 {PROBS} → 確率加重の適正価値 {EV_["expected_price"]:.1f}、確率加重の乖離 {EV_["expected_return"]*100:+.1f}%')
print(f'   非対称性: 下値 {down*100:+.1f}% / 上値(会社シナリオ) {up*100:+.1f}% → 凸性なし')
print(f'   判断(構造評価{RATING}×事業エンジン経路の乖離): {DEC}')
print(f'   エントリー価格帯: α={alpha:.3f} Z1={Z["Z1"]:.1f} Z2={Z["Z2"]:.1f} 現在株価のゾーン={Z["zone"]}')
# DCF 交差確認でも判断が変わらないか
GAPS_DCF = {k: DCF[k] / PRICE - 1 for k in PATHS}
EV_DCF = vl.expected_value(DCF, PROBS, PRICE)
print('   (参考)DCF値での乖離:', {JP[k]: f'{v*100:+.1f}%' for k, v in GAPS_DCF.items()},
      f'確率加重の乖離 {EV_DCF["expected_return"]*100:+.1f}% → 判断 {vl.decision(RATING, GAPS_DCF[ADOPTED_PATH], EDGE)}')
Z_DCF = vl.zones(B=DCF['engine'], U=DCF['company'], L=DCF['bear'], alpha=alpha, price=PRICE, edge=EDGE)
print(f'   (参考)DCF値でのエントリー価格帯: Z1={Z_DCF["Z1"]:.1f} Z2={Z_DCF["Z2"]:.1f}')

# ----------------------------------------------------------------------------------------------
# 11. 現在の倍率・成長・効果測定(自社株買い・SBC)
# ----------------------------------------------------------------------------------------------
ntm_be_now = vl.ntm_eps(be_map(cons), vl.VALUATION_DATE)
ntm_adj_now = vl.ntm_eps(adj_map(cons), vl.VALUATION_DATE)
ntm_be_3 = vl.ntm_eps(be_map(cons), dt.date(2029, 10, 11))
ntm_adj_3 = vl.ntm_eps(adj_map(cons), dt.date(2029, 10, 11))
g_be = vl.cagr(ntm_be_now, ntm_be_3, 3)
g_adj = vl.cagr(ntm_adj_now, ntm_adj_3, 3)
ntm_rev = (3221 * 4 + 3550 * 8) / 12
ntm_fcf = (920 * 4 + 3550 * 0.285 * 8) / 12
ttm_rev = 742 + 761 + 765 + 805
ttm_fcf = 211 + 252 + 271 + 227
ttm_sbc = 138 + 134 + 117 + 114
MULT = dict(per_business_ntm=PRICE / ntm_be_now, per_adj_ntm=PRICE / ntm_adj_now,
            peg_business_3y=(PRICE / ntm_be_now) / (g_be * 100), peg_adj_3y=(PRICE / ntm_adj_now) / (g_adj * 100),
            ev_sales_ntm=EV_DIL * 1000 / ntm_rev, ev_fcf_ntm=EV_DIL * 1000 / ntm_fcf, fcf_margin_ttm=ttm_fcf / ttm_rev,
            sbc_to_revenue_ttm=ttm_sbc / ttm_rev)
print('\n[現在の倍率]', {k: round(v, 3) for k, v in MULT.items()}, f'(事業実態g3={g_be*100:.1f}%、調整後g3={g_adj*100:.1f}%)')
print(f'   NTM 事業実態EPS {ntm_be_now:.2f} / NTM 調整後EPS {ntm_adj_now:.2f} / NTM売上 {ntm_rev:.0f} / NTM FCF {ntm_fcf:.0f}')
print(f'   EV/(FCF−SBC) TTM = {EV_DIL*1000/(ttm_fcf-ttm_sbc):.1f}倍、TTM FCF {ttm_fcf}、TTM SBC {ttm_sbc}')

# 自社株買いの効果(§6): 2026-01〜07 に 5.44百万株を 445百万ドル(平均 約82ドル)で買い戻し
bb_sh = 0.875150 + 4.569262
bb_amt = 79 + 366
bb_avg = bb_amt / bb_sh
for v_int in (DCF['engine'], ADOPT['engine'], SSC['per_share']):
    print(f'[自社株買いの効果] 平均取得単価 {bb_avg:.1f} vs 内在価値 {v_int:.0f}: 1株価値への純効果 = '
          f'{(v_int - bb_avg) * bb_sh / (DIL_SH_GAAP):+.2f} ドル/株(買い戻し株数 {bb_sh:.2f}百万)')
# 今後: 現在株価で残枠 555 を使った場合
for v_int in (DCF['engine'], ADOPT['engine']):
    sh_ = 555 / PRICE
    print(f'   残枠 555 を {PRICE} で執行した場合: 内在価値 {v_int:.0f} なら 1株価値への効果 {(v_int - PRICE) * sh_ / DIL_SH_GAAP:+.2f} ドル/株')
# SBC の希薄化を自社株買いがどこまで相殺したか(GAAP 希薄化後株数 180.966 → 178.808)
dil_change = DIL_SH_GAAP / 180.966 - 1
print(f'[SBCの相殺] GAAP希薄化後株数 FY26Q2 180.966 → FY27Q2 {DIL_SH_GAAP}({dil_change*100:+.1f}%)。'
      f'同期間の買い戻し {bb_sh:.2f}百万株(期首株数の {bb_sh/180.966*100:.1f}%)→ SBC 等による発行は約 {(bb_sh/180.966+dil_change)*100:.1f}%')
SBC_SHARES_AT_PRICE = 465 / PRICE
print(f'   FY27 SBC 465 を現在株価で株数換算すると {SBC_SHARES_AT_PRICE:.2f}百万株(株数の {SBC_SHARES_AT_PRICE/DIL_SH_GAAP*100:.1f}%)。'
      f'株価が82ドルなら {465/82:.2f}百万株({465/82/DIL_SH_GAAP*100:.1f}%)→ 株価上昇が SBC の株数負担を下げる(再帰性)')
# 金利感応度
print(f'[金利感応度] 受取利息 −100bp(現金 {CASH:.0f})→ 税引後 {CASH*0.01*(1-TAX):.1f} → 事業実態EPS {-CASH*0.01*(1-TAX)/DIL_SH_GAAP:+.3f}')

# 事業実態EPS の補正内訳(FY27、コンセンサス)
adjni27 = CONS_EPS[27] * NONGAAP_SH_FY27
print(f'\n[事業実態EPSの補正内訳 FY27] non-GAAP 純利益 {adjni27:.1f}(3.93×184)− SBC {SBC27}×(1−0.21)= {SBC27*(1-TAX):.1f}'
      f' → {adjni27 - SBC27*(1-TAX):.1f} ÷ {DIL_SH_GAAP} = {cons[27]["be"]:.3f}(調整後EPSの {cons[27]["be"]/CONS_EPS[27]*100:.0f}%)')
peer_style = CONS_EPS[27] - 0.186 * 3220 * (1 - 0.22) / DIL_SH_GAAP
print(f'   参考: ピア表の簡易値(SBC比率18.6%一定・税22%)= {peer_style:.2f}。差 {cons[27]["be"]-peer_style:+.2f}(SBC比率の低下と税率21%)')
ttm_be = ((152 + 0.90 * 185.5 + 0.91 * 185 + 194) - ttm_sbc * (1 - TAX)) / DIL_SH_GAAP
print(f'   TTM 事業実態EPS ≈ {ttm_be:.2f}(non-GAAP 純利益 TTM − SBC TTM 503×0.79)')

# ----------------------------------------------------------------------------------------------
# 12. CSV・JSON の書き出し
# ----------------------------------------------------------------------------------------------
paths_out = {}
for k, p in PATHS.items():
    paths_out[k] = {f'FY{2000+y}': round(p[y]['be'], 2) for y in range(27, 33)}
adj_out = {k: {f'FY{2000+y}': round(p[y]['adj'], 2) for y in range(27, 33)} for k, p in PATHS.items()}
summary = {
    'ticker': 'OKTA', 'company': 'Okta, Inc.', 'price': PRICE, 'price_date': '2026-10-09',
    'market_cap_usd_bn': round(MCAP_BASIC, 2), 'diluted_shares_mn': DIL_SH_GAAP, 'fy_end_month': 1,
    'net_cash_usd_bn': round(CASH / 1000, 2),
    'structure_rating': RATING,
    'condition_ratings': {'1': 'B', '2': 'A', '3': 'C', '4': 'S', '5': 'C', '6': 'D', '7': 'D', '8': 'B', '9': 'C', '10': 'B',
                          '11': 'B', '12': 'B', '13': 'B'},
    'condition9_applicable': True,
    'rules_fired': ['致命条件の拒否権: 非発動(E以下なし)', '条件6-7の対評価: D/Dで整合(安くない理由はAIエージェントへの再分類)',
                    'C×4上限: 非発動(C は条件3・5・9の3つ)', '対象外(N/A): なし'],
    'archetype': 'ORCL型寄りのストック型SaaS(従量ではなく座席課金)。SSO/MFA層はバンドルによるコモディティ化圧力(AVGO型の要素)',
    'business_model_types': ['A(ストック型SaaS: Workforce・Customer Identity)', 'A→B候補(エージェント接続数による課金、早期アクセスのみ)'],
    'core_variables': [
        {'name': '中核の売上成長率の持続(cRPO・NRRの再加速、新製品のクロスセル)',
         'market_implied': f'リバースDCFで FY28〜FY37 年率 {RDCF_G*100:.0f}%(エンジン経路の利益率前提)',
         'our_estimate': '年率11〜12.5%(cRPO+14%・新製品30%・NRR107%)、FY33以降は10%→6%へ減衰', 'advantage_type': '分析'},
        {'name': 'AIエージェントのアイデンティティが独立した課金単位になる時期と規模',
         'market_implied': '新しい原子単位として売上の倍増級を織り込む(会社シナリオでも FY32 に約9.5億ドルで株価に届かない)',
         'our_estimate': 'FY29 までは人間の座席への上乗せ・同梱が中心。独立課金は早期アクセスの接続数課金のみ', 'advantage_type': '分析'},
        {'name': 'SBC/売上の低下と営業レバレッジ(事業実態利益への転換率)',
         'market_implied': '調整後EPSで評価(SBCを無視)', 'our_estimate': f'FY27 {SBC27_RATIO*100:.1f}%→FY32 8%。事業実態EPSは FY27 約2.0ドル(ピア表の簡易値1.31より高い)',
         'advantage_type': '分析'},
    ],
    'edge': {
        'exists': True,
        'statement': ('市場はOktaを「AIエージェントのアイデンティティで成長が再加速する急成長株」に分類し直し、年初来約2.8倍に買い上げた。'
                      '事業エンジンで見ると、再加速の実体は既存顧客へのIGA・PAMのクロスセル(新製品が契約獲得の約30%、上乗せ約40%)で、'
                      'エージェントは人間の座席への上乗せ・同梱として値付けされ新しい原子単位になっていない。現在株価は売上の年率'
                      f'{RDCF_G*100:.0f}%成長を10年織り込むが、NRR107%+新規4pt前後のエンジンでは11〜12.5%が上限であり、株価は事業価値を上回る。'),
        'advantage_type': '分析',
        'kpi': 'NRR(TTM)、cRPO成長率、エージェント製品の売上開示・独立課金の価格表',
        'threshold': 'NRR 110%以上かつcRPO成長15%以上を2四半期連続、またはエージェント関連の売上が年1億ドル超と開示',
        'timing': 'FY27 Q3(2026年12月初旬)〜FY28 Q2(2027年8月)の決算',
        'value_per_share_if_resolved': round(ADOPT['engine'], 1),
    },
    'eps_definition': ('事業実態EPS =(会社定義の non-GAAP 希薄化後EPS × non-GAAP 株数_t − SBC_t×(1−21%))÷ GAAP 希薄化後株数 178.808百万株'
                       '(00_standard §3・§3-1。税率は会社の non-GAAP 長期税率21%)'),
    'base_business_eps': {'fy': 'FY2027(2027-01期、コンセンサス基準)', 'value': round(cons[27]['be'], 2)},
    'eps_paths': paths_out,
    'adj_eps_consensus': {'FY2027': 3.93, 'FY2028': 4.36, 'FY2029': 4.89},
    'adj_eps_paths': adj_out,
    'sbc_to_revenue_path': {f'FY{2000+y}': round(sbc_cons[y], 3) for y in range(27, 33)},
    'allowed_peg': {'path_a': list(PEG_A), 'path_b': list(PEG_B), 'path_c': list(PEG_C), 'adopted': list(PEG_ADOPT),
                    'note': ('経路aはピアの調整後PEG(OKTA 5.1、6社中央値約6.1)で「市場の実勢」であり許容値の根拠にしない。'
                             '経路bは3年gの一部がSBC比率の低下(有限の源泉)であるため1.0〜1.4。経路cは構造評価Bの1.0〜1.3にCAP約10年・ストック比率・'
                             '定常状態利益率との差・エージェントの選択肢を加点。採用1.2〜1.45(会社シナリオ1.35〜1.65、弱気0.85〜1.05)。'
                             f'現在株価を正当化するPEGは {PEG_IMPLIED["engine"]:.1f}(事業エンジン)〜{PEG_IMPLIED["consensus"]:.1f}(コンセンサス)')},
    'targets_12m': {k: round(v, 1) for k, v in ADOPT.items()},
    'targets_12m_note': ('採用は規約どおりの方法(2027-10-11のNTM事業実態EPS×PEG×g、PEG中央、PER下限11.1倍)に、§3-3の床(1株当たり定常状態価値+純現金)を適用。'
                         'PEG法の値: ' + ', '.join(f'{JP[k]} {RULE_MID[k]:.1f}' for k in PATHS) +
                         '。床: ' + ', '.join(f'{JP[k]} {FLOOR_NOW[k]:.1f}' for k in PATHS) +
                         '(弱気は営業利益率42%→36%・座席−2%で定常状態利益1,069→' + f'{bear_ss_earn:.0f}' + '百万ドル)。'
                         'コンセンサスにも同じ理由で床を適用(PEG法70.8は定常状態価値を下回り事業本体と整合しない)。定常状態経由: ' +
                         ', '.join(f'{JP[k]} {T12[k]["ss"]:.1f}' for k in PATHS) +
                         '。交差確認(事業実態利益のDCF、r=9%・永続3%): ' + ', '.join(f'{JP[k]} {DCF[k]:.1f}' for k in PATHS) +
                         '。DCF値でも全経路で現在株価を下回り、判断(見送り)は変わらない'),
    'adopted_path': ADOPTED_PATH,
    'gaps': {k: round(GAPS[k], 3) for k in ('consensus', 'company', 'engine')},
    'probabilities': PROBS,
    'expected_price': round(EV_['expected_price'], 1), 'expected_return': round(EV_['expected_return'], 3),
    'expected_return_dcf_reference': round(EV_DCF['expected_return'], 3),
    'floors_steady_state_per_share': {k: round(v, 1) for k, v in FLOOR_NOW.items()},
    'targets_peg_method_before_floor': {k: round(v, 1) for k, v in RULE_MID.items()},
    'asymmetry': {'downside_pct': round(down, 3), 'upside_pct': round(up, 3),
                  'ratio': round((ADOPT['company'] - PRICE) / (PRICE - ADOPT['bear']), 3), 'convex': False},
    'decision': DEC,
    'entry_zones': {'alpha': alpha, 'Z1': round(Z['Z1'], 1), 'Z2': round(Z['Z2'], 1), 'zone': Z['zone'],
                    'Z1_dcf_reference': round(Z_DCF['Z1'], 1), 'Z2_dcf_reference': round(Z_DCF['Z2'], 1)},
    'steady_state': {'steady_earnings_usd_mn': round(SSC['earn'], 0), 'steady_state_value_usd_bn': round(SSC['ssv_total'], 2),
                     'growth_price_usd_bn': round(SSC['growth_price'], 2), 'growth_share': round(SSC['growth_share'], 3)},
    'value_time_split': {'within_3y': round(TS['engine'][0], 3), 'beyond_3y': round(TS['engine'][1], 3)},
    'cap_years': 10, 'incremental_roic': f'約{INCR_ROIC*100:.0f}%(成長S&Mを顧客寿命で資産化した推計。前提の幅で20〜35%)',
    'current_multiples': {k: round(v, 3) for k, v in MULT.items()},
    'growth': {'revenue_yoy_latest_q': round(805 / 728 - 1, 3), 'arr_or_proxy_yoy': round(2585 / 2265 - 1, 3), 'arr_proxy_name': 'cRPO',
               'nnarr_or_proxy_yoy': round(ttm_nn['FY27Q2'] / ttm_nn['FY26Q2'] - 1, 3), 'eps_cagr_3y_consensus': round(vl.cagr(3.50, 4.89, 3), 3),
               'eps_cagr_5y_engine': round(vl.cagr(eng[27]['be'], eng[32]['be'], 5), 3)},
    'rule_of_40': round((805 / 728 - 1 + ttm_fcf / ttm_rev) * 100, 1),
    'triggers': {
        'upgrade': ['株価が Z2(約' + f'{Z["Z2"]:.0f}' + 'ドル)以下に下落(規約どおりの目標株価基準)。DCF基準では約' + f'{Z_DCF["Z2"]:.0f}' + 'ドル以下で分割エントリーを検討',
                    'NRR 110%以上かつcRPO成長15%以上が2四半期連続(事業エンジン経路→会社シナリオ経路への確度移動)',
                    'エージェント製品の独立した価格表(エージェント数・接続数課金)と売上の開示'],
        'downgrade': ['cRPO成長が10%を割る(Q3 ガイダンス11〜12%を下回る)', 'NRRが105%以下に低下', 'SBC/売上が四半期で16%超に再上昇'],
        'exit': ['保有していないため該当なし(見送り)。保有者は NRR 105%以下かつ cRPO 成長10%未満の同時発生、または重大な侵害の再発を撤退条件とする'],
    },
    'one_line': ('事業は改善している(cRPO+14%、新製品30%、SBC比率14%へ低下)が、232ドルは事業エンジンの価値(規約約' +
                 f'{ADOPT["engine"]:.0f}' + 'ドル、DCF約' + f'{DCF["engine"]:.0f}' +
                 'ドル)を大きく上回り、AIエージェントが新しい課金単位になる前提を先取りしている。見送り。'),
    'data_corrections': 9,
    'known_constraints': 12,
}
with open(os.path.join(OUT, 'OKTA_summary.json'), 'w') as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print('\nwrote OKTA_summary.json, OKTA_F13.csv, OKTA_F18.csv, OKTA_F10.csv')
