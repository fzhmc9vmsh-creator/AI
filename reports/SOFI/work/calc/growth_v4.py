"""SOFI 第4版(Opus、2026-10-28): Q3 2026 決算と 2027 年見通しを反映した評価。
手法は第3版と同じ(meigara-bunseki-method 第5.2版: 妥当 PER = 許容 PEG × 当該年度から 3 年の g、構造の点数で PEG・α、
節点ツリーの組み合わせごとの構造と PEG)。事業エンジンは 2026 年の更新ガイダンス(調整後純収益 50.4 億ドル、純利益 約 8.4 億、EPS 約 0.61)と
2027 年見通し(64 億ドル、純利益 12.8 億、EPS 0.90)に較正し、2028 年以降はエンジンの動き(資本の上限・LPB・手数料)で延ばす。
入力: research_r5/(R18〜R22c、Q3_datasheet.md)。すべて WebSearch の要約経由。出力: out/growth_v4.json。
"""
import itertools
import json
import os

import val_model as vm
import growth_v2 as g2
import growth_v3 as g3

OUT = os.path.join(os.path.dirname(__file__), "out")

PRICE = 14.55            # 最後に確認できた終値(2026-10-16)。10/27 は決算で日中 +11〜14% と報道(終値は未取得)
PRICE_ALT = 16.5         # 決算後の株価の目安(14.55 × 1.13、推定)。乖離の感応度にだけ使う

# ---------------------------------------------------------------- Q3 2026 の実績(Q3_datasheet、要約経由)
Q3 = dict(rev=1385.1, nii=929.5, nim=0.0614, ebitda=469.8, ni=241.0, eps=0.18, sm=444.0, members=17.1, products=26.7,
          net_mem=1.2, net_prod=2.2, cross=0.51, deposits=51.3, spread_bp=145, savings=745.0, fee=570.6, fee_share=0.42,
          lending=821.3, lending_cp=454.9, fs=525.1, fs_cp=261.0, tp=87.4, tp_cp=14.2, tp_ex_large=0.18,
          pl_orig=12.6, lpb=3.6, sl_orig=2.9, hl_orig=1.4, nco=0.0226, allin=0.034, sl_nco=0.0063,
          disc_pl=0.0556, disc_sl=0.0511, tcr=0.170, cet1=0.169, t1lev=0.150, rwa=56.2, tbvps=7.48)
Q2 = dict(rev=1218.7, nii=788.2, nim=0.0598, ni=156.6, eps=0.12, sm=392.4, members=15.8, products=24.4, net_mem=1.1, net_prod=2.2,
          cross=0.51, deposits=45.5, spread_bp=156, savings=712.6, fee=472.3, fee_share=0.392, tp=84.5, tp_cp=11.8, allin=0.037,
          nco=0.0262, disc_pl=0.0497, disc_sl=0.0429, tcr=0.188, rwa=48.68, lpb=3.1, pl_orig=10.7)
Q3_25 = dict(rev=961.6, members=12.6, products=18.6, net_mem=0.905, net_prod=1.4, deposits=32.9, sm=286.9, fee=None)

GUIDE = {2026: dict(rev=5.04e9, ebitda=1.66e9, ni=0.84e9, eps=0.61), 2027: dict(rev=6.40e9, ebitda=2.24e9, ni=1.28e9, eps=0.90)}
GUIDE_PRE = {2026: dict(rev=4.80e9, ni=0.825e9, eps=0.60)}      # 第3版の時点(Q2 後)のガイダンス

# ---------------------------------------------------------------- 事業エンジン(第4版の較正)
ENG4 = dict(
    rev26=5.04e9, iea_avg26=57.0e9, iea_end26=66.0e9, cap_end26=9.55e9 + 0.26e9 + 0.07e9,
    mem0=14.0, mem_add=[4.3, 4.6, 4.4, 4.2, 4.0],
    nim=[0.0605, 0.0600, 0.0590, 0.0580, 0.0575],
    bs_growth_want=[None, 0.30, 0.25, 0.22, 0.20],
    fs_g=[None, 0.45, 0.32, 0.25, 0.20], tp_g=[None, 0.15, 0.18, 0.15, 0.12],
    lpb_g_base=[None, 0.15, 0.15, 0.15, 0.12], gains_g=[None, 0.15, 0.15, 0.12, 0.10],
    sm=[0.32, 0.30, 0.285, 0.27, 0.255], tpd=[0.155, 0.148, 0.140, 0.133, 0.128],
    ops=[0.3105, 0.296, 0.288, 0.282, 0.278], tax=[0.22, 0.22, 0.23, 0.23, 0.23],
    sh_g_list=[None, 0.031, 0.015, 0.015, 0.015],
)
SH26 = 1.377e9


def engine4(**kw):
    p = dict(ENG4)
    for k, v in kw.items():
        p[k] = v
    return vm.engine(sh=SH26, **p)


# ---------------------------------------------------------------- 3 経路の EPS
def paths():
    base = engine4()
    e = vm.eps_of(base)
    cons = {2026: 0.61, 2027: 0.90}
    cons[2028] = round(0.90 * 1.08 / 0.83, 3)     # 決算前コンセンサスの 2027→2028 の伸び(+30%)
    cons[2029] = round(cons[2028] * 1.32 / 1.08, 3)
    cons[2030] = round(cons[2029] * 1.18, 3)
    comp = {2026: 0.61, 2027: 0.90, 2028: round(0.39 * 1.42 ** 3, 3)}   # 中期目標(2025→2028 EPS CAGR 42% の上端)
    comp[2029] = round(comp[2028] * 1.25, 3)
    comp[2030] = round(comp[2029] * 1.22, 3)
    return base, {"engine": e, "consensus": cons, "company": comp}


# ---------------------------------------------------------------- 構造評価(第4版)
GRADES_V4 = {1: "B", 2: "B", 3: "A", 4: "S", 5: "B", 6: "A", 7: "A", 8: "B", 10: "B", 11: "B", 12: "B", 13: "B"}
LINKS4 = {"N1": [1, 8, 11], "N2": [12, 13], "N4": []}      # 条件3 は現在 A(N4 の失敗で B に戻す)


def scenario_grades4(state, rotce2028):
    g = dict(GRADES_V4)
    for node, conds in LINKS4.items():
        for c in conds:
            g[c] = g3.UP[g[c]] if state[node] else g3.DOWN[g[c]]
    g[3] = "A" if state["N4"] else "B"
    g[2] = "A" if rotce2028 >= vm.COE else ("B" if rotce2028 >= 0.11 else "C")
    return g


def roe4(path):
    tbv = 7.48 * 1.32e9 + 0.26e9          # 2026 年末の TBV(Q3 の TBV/株 × 基本株数 + Q4 の純利益)
    out = {2026: path[2026]["ni"] / (tbv - 0.13e9)}
    for y in vm.YEARS[1:]:
        start = tbv
        tbv += path[y]["ni"] + 0.27e9
        out[y] = path[y]["ni"] / ((start + tbv) / 2)
    return out


def self_suff4(path):
    out = {}
    iea_prev = ENG4["iea_end26"]
    for y in vm.YEARS[1:]:
        iea_end = 2 * path[y]["iea_avg"] - iea_prev
        need = 0.145 * (iea_end - iea_prev) * 0.92
        out[y] = path[y]["ni"] / need if need > 0 else None
        iea_prev = iea_end
    return out


# ---------------------------------------------------------------- 節点ツリー(基準は第4版のエンジン = 会社の見通しに較正)
NODES_V4 = {
    "N1": dict(cond=(0.68, 0.52), why="+ ガイダンスの上方修正の記録(2025 年 3 回、2026 年は収益を 2 回)、会員純増 120 万・製品 220 万(過去最高)、"
                                     "製品 前年比 +44%、収益 +44%、− 会員当たり販促費 357 → 370 ドル・製品当たり 178 → 202 ドル、クロスバイ 51% で横ばい"),
    "N2": dict(cond=(0.57, 0.32), why="+ LPB 31 → 36 億ドル(+16%)、手数料型の比率 39 → 42%、− 個人ローンの LPB の割合は 29% のまま、総自己資本比率 −1.8pt"),
    "N3": dict(p=0.45, why="基準は Q3 の all-in 3.4%。+ 純償却 2.62 → 2.26%、− 失業率 4.2%、同業のカードの延滞の上昇(COF 30 日 3.39 → 3.74%)"),
    "N4": dict(p=0.55, why="基準は Tech Platform 2027 年 +15%。+ 大口を除き +18%、貢献利益率 14 → 16%、− 新規契約の数字は未取得"),
}


def tree4(eng_mult=None, cond=None, p3=None):
    c1 = cond or {"N1": NODES_V4["N1"]["cond"], "N2": NODES_V4["N2"]["cond"]}
    p3 = NODES_V4["N3"]["p"] if p3 is None else p3
    p4 = NODES_V4["N4"]["p"]
    combos = []
    for s in itertools.product([1, 0], repeat=4):
        st = dict(zip(["N1", "N2", "N3", "N4"], s))
        kw = {}
        for k, ok in st.items():
            for var, (succ, fail) in g2.SHOCKS[k].items():
                kw[var] = succ if ok else fail
        # SHOCKS は第2版の基準の値なので、第4版の基準との差(NIM・TP・販促費)を足し直す
        if "nim" in kw:
            kw["nim"] = [a + (b - c) for a, b, c in zip(kw["nim"], ENG4["nim"], [0.0600, 0.0585, 0.0575, 0.0565, 0.0560])]
        if "tp_g" in kw:
            kw["tp_g"] = [None] + [a + (b - c) for a, b, c in zip(kw["tp_g"][1:], ENG4["tp_g"][1:], [0.08, 0.10, 0.10, 0.10])]
        path = engine4(**kw)
        rot = roe4(path)
        sg = scenario_grades4(st, rot[2028])
        gr = g3.grade_of(sg)
        _, val = g3.fair_path_skill(vm.eps_of(path), gr["peg"])
        p = p3 if st["N3"] else 1 - p3
        for k in ("N1", "N2"):
            pc = c1[k][0 if st["N3"] else 1]
            p *= pc if st[k] else 1 - pc
        p *= p4 if st["N4"] else 1 - p4
        combos.append(dict(state=st, p=p, value=val, eps=vm.eps_of(path), rotce2028=rot[2028], letter=gr["letter"], avg=gr["avg"], peg26=gr["peg"][2026]))
    ev = sum(c["p"] * c["value"] for c in combos)
    sd = sum(c["p"] * (c["value"] - ev) ** 2 for c in combos) ** 0.5
    bull = [c for c in combos if c["state"]["N1"] and c["state"]["N2"]]
    bear = [c for c in combos if not c["state"]["N1"] and not c["state"]["N2"]]
    basec = [c for c in combos if c not in bull and c not in bear]

    def bundle(cs):
        p = sum(c["p"] for c in cs)
        return dict(p=p, value=sum(c["p"] * c["value"] for c in cs) / p, eps2028=sum(c["p"] * c["eps"][2028] for c in cs) / p)
    pn = {k: sum(c["p"] for c in combos if c["state"][k]) for k in ["N1", "N2", "N3", "N4"]}
    return dict(combos=combos, ev=ev, sd=sd, bundles=dict(bull=bundle(bull), base=bundle(basec), bear=bundle(bear)), p_nodes=pn)


# ---------------------------------------------------------------- 交差確認(DCF・TBV)
def dcf4(path):
    req_prev = 0.145 * ENG4["iea_end26"] * 0.92
    excess0 = ENG4["cap_end26"] - req_prev
    pv, iea_prev = 0.0, ENG4["iea_end26"]
    for i, y in enumerate(vm.YEARS[1:], start=1):
        iea_end = 2 * path[y]["iea_avg"] - iea_prev
        req = 0.145 * iea_end * 0.92
        pv += (path[y]["ni"] - (req - req_prev)) / (1 + vm.COE) ** i
        req_prev, iea_prev = req, iea_end
    tv = vm.theory_per(vm.G_LR, 0.18) * path[2030]["ni"] * 1.12
    pv += tv / (1 + vm.COE) ** 4
    return (pv + excess0) / SH26


def run():
    out = {"q3": Q3, "q2": Q2, "guide": {str(k): v for k, v in GUIDE.items()}}
    base, P = paths()
    out["paths"] = {k: {str(y): round(v, 3) for y, v in e.items()} for k, e in P.items()}
    out["engine"] = {str(y): dict(rev=base[y]["rev"], ni=base[y]["ni"], eps=base[y]["eps"], shares=base[y]["shares"], members=base[y]["members"],
                                  nii_share=base[y]["nii"] / base[y]["rev"], cap_ratio=base[y]["cap_ratio"]) for y in vm.YEARS}
    out["growth"] = {k: {"y%d" % y: e[y] / e[y - 1] - 1 for y in range(2027, 2031)} for k, e in P.items()}
    out["cagr"] = {k: dict(c26_29=vm.cagr(e[2026], e[2029], 3), c26_28=vm.cagr(e[2026], e[2028], 2), c25_28=vm.cagr(0.39, e[2028], 3),
                           c26_30=vm.cagr(e[2026], e[2030], 4)) for k, e in P.items()}
    out["rotce"] = roe4(base)
    out["self_suff"] = self_suff4(base)
    gr = g3.grade_of(GRADES_V4)
    out["grade"] = gr
    peg = gr["peg"]
    out["values"] = {k: g3.fair_path_skill(e, peg)[1] for k, e in P.items()}
    out["rows"] = {k: g3.fair_path_skill(e, peg)[0] for k, e in P.items()}
    out["values_peg10"] = {k: g3.fair_path_skill(e, {y: 1.0 for y in vm.YEARS})[1] for k, e in P.items()}
    t = tree4()
    out["tree"] = dict(ev=t["ev"], sd=t["sd"], bundles=t["bundles"], p_nodes=t["p_nodes"],
                       combos=[dict(state="".join("○" if c["state"][k] else "×" for k in ["N1", "N2", "N3", "N4"]), p=c["p"], value=c["value"],
                                    eps2028=c["eps"][2028], letter=c["letter"], peg26=c["peg26"]) for c in t["combos"]])
    sens = []
    for d1 in (-0.10, 0.0, 0.10):
        row = []
        for d2 in (-0.10, 0.0, 0.10):
            c = {"N1": tuple(x + d1 for x in NODES_V4["N1"]["cond"]), "N2": tuple(x + d2 for x in NODES_V4["N2"]["cond"])}
            tt = tree4(cond=c)
            row.append(dict(ev=tt["ev"], p_bull=tt["bundles"]["bull"]["p"]))
        sens.append(dict(dN1=d1, row=row))
    out["tree_sens"] = sens
    # 株価が示す PEG と恒常の損失率
    def implied_peg(price):
        lo, hi = 0.2, 1.8
        for _ in range(60):
            mid = (lo + hi) / 2
            pg = {y: mid - 0.05 * i for i, y in enumerate([2026, 2027, 2028, 2029])}
            if g3.fair_path_skill(P["engine"], pg)[1] > price:
                hi = mid
            else:
                lo = mid
        return (lo + hi) / 2

    def implied_loss(price):
        lo, hi = 0.0, 0.08
        for _ in range(60):
            mid = (lo + hi) / 2
            if g3.fair_path_skill(vm.eps_of(engine4(credit_shock=mid)), peg)[1] > price:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2
    out["implied"] = {str(pr): dict(peg=implied_peg(pr), loss=implied_loss(pr)) for pr in (PRICE, PRICE_ALT)}
    # 信用と資本の感応度
    cc = {}
    for lab, sh in (("+0.5pt", 0.005), ("+1.0pt", 0.010), ("+2.0pt", 0.020)):
        pth = engine4(credit_shock=sh)
        cc[lab] = dict(value=g3.fair_path_skill(vm.eps_of(pth), peg)[1], eps2027=pth[2027]["eps"], eps2028=pth[2028]["eps"])
    raise_sh = 1.0e9 / PRICE
    v = out["values"]["engine"]
    cc["raise_1b"] = (v * SH26 + 1.0e9) / (SH26 + raise_sh)
    cc["excess_capital"] = (Q3["tcr"] - 0.14) * Q3["rwa"] * 1e9
    cc["quarters_to_floor"] = (Q3["tcr"] - 0.14) / (Q2["tcr"] - Q3["tcr"])
    # 金利 +100bp(NIM 1 年目 −、信用 +0.1pt、資本コスト +1pt、評価減の純額 −1.5 億)と 3 つ同時
    nim_d1 = -77.6e6 * 1.35 / base[2027]["iea_avg"]
    up = engine4(nim=[a + d for a, d in zip(ENG4["nim"], [0, nim_d1, nim_d1 / 2, 0, 0])], credit_shock=0.001)
    coe0 = vm.COE
    vm.COE, vm.FLOOR = coe0 + 0.01, 1 / (coe0 + 0.01)
    v_up = g3.fair_path_skill(vm.eps_of(up), peg)[1] - 0.15e9 * 0.78 / 1.42e9
    up3 = engine4(nim=[a + d for a, d in zip(ENG4["nim"], [0, nim_d1, nim_d1 / 2, 0, 0])], credit_shock=0.011)
    v3 = g3.fair_path_skill(vm.eps_of(up3), peg)[1] - 0.15e9 * 0.78 / 1.42e9
    vm.COE, vm.FLOOR = coe0, 1 / coe0
    cc["rate_up100"] = v_up
    cc["all_three"] = (v3 * SH26 + 1.0e9) / (SH26 + raise_sh)
    out["credit_capital"] = cc
    out["cross"] = dict(dcf=dcf4(base), terminal_per=vm.theory_per(vm.G_LR, 0.18))
    a = gr["alpha"]
    B, L, U = out["values"]["engine"], t["bundles"]["bear"]["value"], t["bundles"]["bull"]["value"]
    out["entry"] = dict(alpha=a, B=B, U=U, L=L, Z1=min(B * (1 - a), L * (1 + a / 2)), Z2=B * (1 - a / 2),
                        up_down={str(pr): (U - pr) / (pr - L) if pr > L else None for pr in (PRICE, PRICE_ALT)})
    out["gap"] = {str(pr): {k: v / pr - 1 for k, v in list(out["values"].items()) + [("ev", t["ev"])]} for pr in (PRICE, PRICE_ALT)}
    # 単位当たりの経済性(Q3)
    out["unit"] = dict(sm_per_member=Q3["sm"] / Q3["net_mem"], sm_per_product=Q3["sm"] / Q3["net_prod"],
                       sm_per_member_q2=Q2["sm"] / Q2["net_mem"], sm_per_product_q2=Q2["sm"] / Q2["net_prod"],
                       rev_per_member=Q3["rev"] * 4 / ((Q3["members"] + Q2["members"]) / 2),
                       rev_per_member_q2=Q2["rev"] * 4 / ((Q2["members"] + 14.7) / 2),
                       sm_ratio=Q3["sm"] / Q3["rev"], sm_ratio_q2=Q2["sm"] / Q2["rev"],
                       ppm=Q3["products"] / Q3["members"], dep_per_member=Q3["deposits"] * 1e3 / Q3["members"],
                       dep_per_member_q2=Q2["deposits"] * 1e3 / Q2["members"])
    with open(os.path.join(OUT, "growth_v4.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, default=float)
    return out


if __name__ == "__main__":
    o = run()
    for k, e in o["paths"].items():
        print(k, e, {a: round(b * 100, 1) for a, b in o["cagr"][k].items()})
    print("growth", {k: {a: round(b * 100, 1) for a, b in v.items()} for k, v in o["growth"].items()})
    print("engine", {y: (round(r["rev"] / 1e9, 2), round(r["ni"] / 1e9, 3), round(r["eps"], 3), r["cap_ratio"] and round(r["cap_ratio"], 3)) for y, r in o["engine"].items()})
    print("rotce", {y: round(v, 3) for y, v in o["rotce"].items()}, "ss", {y: v and round(v, 2) for y, v in o["self_suff"].items()})
    g = o["grade"]; print("grade", g["letter"], round(g["avg"], 3), round(g["pos"], 3), {y: round(v, 3) for y, v in g["peg"].items()}, round(g["alpha"], 4))
    print("values", {k: round(v, 2) for k, v in o["values"].items()}, "peg10", {k: round(v, 2) for k, v in o["values_peg10"].items()})
    for k, rows in o["rows"].items():
        print(" rows", k, [(r["year"], round(r["eps"], 3), round(r["g"] * 100, 1), round(r["peg"], 3), round(r["per"], 1), r["how"], round(r["price"], 1), round(r["pv"], 1)) for r in rows])
    t = o["tree"]; print("tree ev", round(t["ev"], 2), "sd", round(t["sd"], 2), "pn", {k: round(v, 3) for k, v in t["p_nodes"].items()})
    print("bundles", {k: {a: round(b, 3) for a, b in v.items()} for k, v in t["bundles"].items()})
    for c in t["combos"]:
        print("  ", c["state"], round(c["p"], 3), round(c["value"], 1), round(c["eps2028"], 3), c["letter"], round(c["peg26"], 3))
    print("sens", [[(round(x["ev"], 1), round(x["p_bull"] * 100)) for x in s["row"]] for s in o["tree_sens"]])
    print("implied", {k: {a: round(b, 4) for a, b in v.items()} for k, v in o["implied"].items()})
    print("cc", {k: (round(v, 3) if isinstance(v, float) else v) for k, v in o["credit_capital"].items()})
    print("cross", {k: round(v, 2) for k, v in o["cross"].items()})
    print("entry", {k: (round(v, 2) if isinstance(v, float) else v) for k, v in o["entry"].items()})
    print("gap", {k: {a: round(b * 100, 1) for a, b in v.items()} for k, v in o["gap"].items()})
    print("unit", {k: round(v, 3) for k, v in o["unit"].items()})
