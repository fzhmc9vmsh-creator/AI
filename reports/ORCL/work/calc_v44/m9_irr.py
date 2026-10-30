# 会社の 1GW 例(CFO 資料 p.15〜20)の IRR。四半期で計算: 契約 T0、capex は T+2Q〜T+7Q に均等(計 37)、
# 初回の提供 T+4Q、満稼働 T+8Q(T+4Q〜T+7Q は線形に立ち上げ)、契約 5 年(満稼働換算 20 四半期分)、年換算売上 16、
# 粗利率 35%(償却 6 年 → 現金費用 = 16×0.65 − 37/6)、R&D・営業 1%、税 17%。更新は契約後に単価 × 倍率で n 年
import json
def irr(cfs):
    lo, hi = -0.5, 1.0
    for _ in range(200):
        m = (lo + hi) / 2
        v = sum(c / (1 + m) ** (i / 4) for i, c in enumerate(cfs))
        lo, hi = (m, hi) if v > 0 else (lo, m)
    return (lo + hi) / 2
def case(capex=37.0, rev=16.0, renew_years=0, renew_mult=1.0, gm=0.35, life=6):
    dep_y = capex / life
    cash = rev * (1 - gm) - dep_y                      # 現金費用 /年(満稼働)
    n = 4 * (1 + 5 + renew_years) + 8
    cfs = [0.0] * n
    for q in range(2, 8):
        cfs[q] -= capex / 6
    served = 0.0
    q = 4
    cum_rev_q = 0.0
    while served < 20 and q < n:
        ramp = min(1.0, (q - 3) / 4)
        r = rev / 4 * ramp
        cfs[q] += (r - cash / 4 * ramp) * (1 - 0.17) - 0.01 * r * (1 - 0.17)
        served += ramp
        q += 1
    for k in range(4 * renew_years):
        if q >= n:
            break
        r = rev / 4 * renew_mult
        cfs[q] += (r - cash / 4) * (1 - 0.17)
        q += 1
    # 減価償却の節税
    for k in range(4 * life):
        if 4 + k < n:
            cfs[4 + k] += capex / life / 4 * 0.17
    return irr(cfs)
rows = [('更新なし(5 年で終わる)', case()), ('2 年更新・単価 60%', case(renew_years=2, renew_mult=0.6)),
        ('2 年更新・単価 120%(会社: 4 年前の GPU +20%)', case(renew_years=2, renew_mult=1.2)),
        ('capex +10%・更新なし', case(capex=40.7)), ('BYOH(capex 6・売上 11・粗利率 40%)', case(capex=6.0, rev=11.0, gm=0.40))]
for k, v in rows:
    print('%-40s IRR %.1f%%' % (k, v * 100))
json.dump(dict(rows), open('out/m9_irr.json', 'w'), ensure_ascii=False, indent=1)
