"""1周目 v2: 必要資本ベースのFCFE(株主への配分可能額)モデル。超過資本は配分可能とみなす。"""
BASE = dict(
    rev26=4.80e9, ni26=0.825e9, tbv_end26=9.9e9, shares0=1.375e9,
    mem_g=[0.25, 0.20, 0.16, 0.12], fade_to=0.04, rpm_g=0.04,
    m_ss=0.26, coe=0.12, dil=0.02,
    cap26=1.55, cap_ss=1.25,   # 必要有形資本 ÷ 売上(2026→2030で低下: LPB・手数料比率上昇)
    nco_shock=0.0, dep_shock=0.0, lpb_extra=0.0, g_inf=0.03,
)

def value(p, detail=False):
    rev, sh = p["rev26"], p["shares0"]
    m26 = p["ni26"] / rev
    req = p["cap26"] * rev
    excess0 = p["tbv_end26"] - req
    g_path = list(p["mem_g"])
    last = g_path[-1]
    g_path += [last + (p["fade_to"] - last) * (i + 1) / 5 for i in range(5)]
    adj = -0.056 * p["nco_shock"] * 100 - 0.036 * (p["dep_shock"] / 0.005)
    pv, disc, eps, rotce = 0.0, 1.0, {2026: p["ni26"] / sh}, {}
    for t, g in enumerate(g_path, start=1):
        rev *= (1 + g) * (1 + p["rpm_g"])
        f = min(t / 4, 1.0)
        m = m26 + (p["m_ss"] - m26) * f + adj * f
        ni = rev * m + p["lpb_extra"] * p["rev26"] * 0.45 * f * (1 + g) ** t
        c = p["cap26"] + (p["cap_ss"] - p["cap26"]) * f
        req_new = c * rev
        fcfe = ni - (req_new - req)
        rotce[2026 + t] = ni / ((req + req_new) / 2)
        req = req_new
        sh *= 1 + p["dil"]
        eps[2026 + t] = ni / sh
        disc /= 1 + p["coe"]
        pv += fcfe * disc
    # 終価: 永続成長 g_inf、必要資本は売上に比例
    fcfe_next = ni * (1 + p["g_inf"]) - c * rev * p["g_inf"]
    pv += fcfe_next / (p["coe"] - p["g_inf"]) * disc
    v = (pv + excess0) / p["shares0"]
    if detail:
        return v, eps, rotce, excess0
    return v

if __name__ == "__main__":
    v, eps, rotce, ex = value(BASE, True)
    print(f"base value/sh={v:.2f} excess0={ex/1e9:.2f}B")
    print("EPS", {k: round(x, 2) for k, x in eps.items()})
    print("ROTCE(req)", {k: f"{x:.0%}" for k, x in rotce.items()})
    tests = [
        ("会員成長 ±5pp/年(2027-30)", "mem_g", [g - 0.05 for g in BASE["mem_g"]], [g + 0.05 for g in BASE["mem_g"]]),
        ("会員当たり収益の伸び 1%↔7%", "rpm_g", 0.01, 0.07),
        ("定常純利益率 22%↔30%", "m_ss", 0.22, 0.30),
        ("資本コスト 13%↔11%", "coe", 0.13, 0.11),
        ("個人ローンNCO +1pp↔-0.5pp", "nco_shock", 0.01, -0.005),
        ("預金コスト +50bp↔-25bp", "dep_shock", 0.005, -0.0025),
        ("必要資本/売上(定常) 1.5↔1.0", "cap_ss", 1.5, 1.0),
        ("LPB追加規模 0↔+15%", "lpb_extra", 0.0, 0.15),
        ("成長収束先 2%↔6%", "fade_to", 0.02, 0.06),
    ]
    rows = []
    for name, k, lo, hi in tests:
        vl, vh = value(dict(BASE, **{k: lo})), value(dict(BASE, **{k: hi}))
        rows.append((abs(vh - vl), name, vl, vh))
    for sw, name, vl, vh in sorted(rows, reverse=True):
        print(f"{name:32s} low={vl:6.2f} high={vh:6.2f} swing={sw:5.2f}")
