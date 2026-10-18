"""SOFI 第2版(Opus、2026-10-18): 成長段階の尺度 G1〜G7、販促費の裁量性、確率の節点ツリー、構造評価 B での再評価。
手法: meigara-bunseki-method 第4.5版 growth-stage-evaluation.md。入力の出所は research_r3/(R10・R11・R12)と既存の research/・research_r2/。
すべて WebSearch の要約経由。出力: out/growth_v2.json。
"""
import itertools
import json
import os

import val_model as vm

OUT = os.path.join(os.path.dirname(__file__), "out")

# ---------------------------------------------------------------- 入力: 四半期の時系列(R10 §1、百万ドル・千人・千件)
Q = ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
SM = [167.3, 184.8, 214.9, 229.3, 238.1, 264.7, 286.9, 305.6, 335.5, 392.4]
NET_MEM = [622, 643, 756, 785, 800, 850, 905, 1000, 1100, 1100]
NET_PROD = [989, 946, 1100, 1100, 1200, 1260, 1400, 1600, 1800, 2200]
CROSS = [None, None, None, 0.33, 0.36, 0.35, 0.40, 0.40, 0.43, 0.51]
# 調整後純収益(百万ドル): Q3'25 962(R3b 見出し値)、Q4'25 約 1,013(+37%)、Q1'26 1,087.2(R10)、Q2'26 1,205.6(R3b)、Q2'25 = 1,205.6/1.40
REV_4Q = [962.0, 1013.0, 1087.2, 1205.6]
REV_Q2_25 = 1205.6 / 1.40
PRETAX_Q2, REV_GAAP_Q2, SM_Q2 = 204.3, 1218.7, 392.4      # Q2'26 GAAP(F19 の損益フロー)
RWA, TAX = 48.68e3, 0.23                                   # 百万ドル


def g1_unit_economics():
    rows = []
    for i, q in enumerate(Q):
        new_prod = NET_PROD[i] * (1 - CROSS[i]) if CROSS[i] is not None else None
        rows.append(dict(q=q, sm=SM[i], per_member=round(SM[i] / NET_MEM[i] * 1e3), per_product=round(SM[i] / NET_PROD[i] * 1e3),
                         new_member_product=round(SM[i] / new_prod * 1e3) if new_prod else None, cross=CROSS[i]))
    coe = vm.COE
    pre_sm_margin = (PRETAX_Q2 + SM_Q2) / REV_GAAP_Q2                    # 販促費控除前の税引前利益率 49%
    ann_rev = REV_GAAP_Q2 * 4
    cap_charge = 0.145 * RWA / ann_rev * coe                              # 収益 1 ドル当たりの資本コスト(必要資本 14.5% × RWA)
    econ_margin = (pre_sm_margin - cap_charge) * (1 - TAX)               # 資本コスト・税控除後の経済的利益率
    inc_rev = (REV_4Q[-1] - REV_Q2_25) * 4                                # 1 年間に増えた年換算収益
    sm_4q = sum(SM[-4:])
    maint = 0.16 * sum(REV_4Q)                                            # 維持水準の販促費(定常状態の前提 16%、§3)
    growth_sm = sm_4q - maint
    annual_profit = inc_rev * econ_margin
    out = dict(rows=rows, pre_sm_margin=pre_sm_margin, cap_charge=cap_charge, econ_margin=econ_margin, inc_rev=inc_rev,
               sm_4q=sm_4q, maint_sm=maint, growth_sm=growth_sm, annual_profit=annual_profit, cases=[])
    # 経済的 LTV/CAC(資本コスト控除・COE 割引): LTV = 年間利益 ÷ (1 + r − 残存率)
    for basis, cac in (("成長分の販促費", growth_sm), ("販促費の全額", sm_4q)):
        for keep in (0.85, 0.90, 0.95):
            ltv = annual_profit / (1 + coe - keep)
            out["cases"].append(dict(basis=basis, keep=keep, ltv_cac=round(ltv / (cac * (1 - TAX)), 2),
                                     payback=round(cac * (1 - TAX) / annual_profit, 1)))
    # 製品単位の検算: 製品当たり年収益 × 経済的利益率 ÷ 製品当たり販促費
    rev_per_prod = ann_rev / 24.4e3 * 1e3                                  # ドル(製品 2,440 万)
    prod_profit = rev_per_prod * econ_margin
    out["product_check"] = dict(rev_per_product=round(rev_per_prod), profit_per_product=round(prod_profit, 1),
                                cac_per_product=rows[-1]["per_product"],
                                ltv_cac_q90=round(prod_profit / (1 + coe - 0.90) / (rows[-1]["per_product"] * (1 - TAX)), 2),
                                payback=round(rows[-1]["per_product"] * (1 - TAX) / prod_profit, 1))
    return out


def g2_discretionary(base):
    """販促費の裁量部分と、成長投資控除前 EPS。EPS の成長の分解(エンジン 2026→2029)。"""
    rev26, sh26 = 4.80e9, vm.SH_DIL_26
    res = {}
    for m in (0.13, 0.16, 0.19):
        disc = (0.32 - m) * rev26
        res[f"maint_{int(m*100)}"] = dict(discretionary=disc, eps_add=disc * (1 - 0.22) / sh26)
    per_pt = 0.01 * rev26 * (1 - 0.22) / sh26                               # 販促費率 1pt = EPS
    # 2026 の運営方針: 売上の上方修正 +1.45 億ドル(中央)を利益に積まず再投資(R10 §4-2)
    reinvest_26 = 0.145e9 * (1 - 0.22) / sh26
    # EPS 成長の分解: 販促費率を 32% で据え置いたエンジン経路と比べる
    flat = vm.engine(sm=[0.32] * 5)
    e29, f29, e26 = base[2029]["eps"], flat[2029]["eps"], base[2026]["eps"]
    share_sm = (e29 - f29) / (e29 - e26)
    return dict(levels=res, eps_per_pt=per_pt, reinvest_2026=reinvest_26, eps29=e29, eps29_sm_flat=f29,
                share_of_growth_from_sm=share_sm)


def g5_self_sufficiency():
    """自己資本の自給率(上期 2026): 資本の生成 ÷ 成長に必要な資本の増加。"""
    gen = 0.336e9 + 0.2258e9                    # TBV の増加 Q1 +3.36 億・Q2 +2.258 億(R12)
    need = 0.145 * (48.68e9 - 37.23e9)          # RWA の増加 × 14.5%(R7)
    return dict(generation=gen, need=need, ratio=gen / need,
                lpb_share=dict(zip(["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"], [0.291, 0.343, 0.453, 0.493, 0.361, 0.290])),
                fee_share=dict(zip(["Q2 25", "Q4 25", "Q1 26", "Q2 26"], [0.440, 0.438, 0.356, 0.392])))


def g4_embedded(members=15.8e6):
    """既存会員の追加製品が生む将来の利益(1 株当たり)。+0.3 製品/会員 × FS 製品収益 88 ドル × 貢献利益率 46%。"""
    add = 0.3 * members
    profit = add * 88 * 0.46 * (1 - TAX)
    ltv = profit / (1 + vm.COE - 0.90)
    return dict(add_products=add, annual_profit=profit, value=ltv, per_share=ltv / vm.SH_DIL_26)


def g7_sofiusd():
    """SoFiUSD: 自社カードの決済 年 250 億ドル(予測)、流通 3 億ドル(Q2 末)。費用削減と運用益の感応度(算術のみ)。"""
    vol, float_ = 25e9, 0.3e9
    rows = [dict(bp=bp, saving=vol * bp / 1e4, eps=vol * bp / 1e4 * (1 - TAX) / vm.SH_DIL_26) for bp in (1, 3, 5)]
    flt = [dict(float=f, spread=s, income=f * s, eps=f * s * (1 - TAX) / vm.SH_DIL_26) for f in (0.3e9, 3e9, 10e9) for s in (0.01,)]
    return dict(card_saving=rows, float_income=flt)


# ---------------------------------------------------------------- 構造評価 B での許容 PEG(prereg の表: B 1.0〜1.3、年度で狭いレンジの中央 → 下限)
PEG_B = {2026: 1.15, 2027: 1.10, 2028: 1.05, 2029: 1.00}

# ---------------------------------------------------------------- 節点ツリー(growth-stage-evaluation §9)
# 振れ幅は対称(成功 = 基準 + Δ、失敗 = 基準 − Δ)。確率は基準率と先行指標から(下の NODES の根拠)。
NODES = {
    # 確率は「基準(事業エンジン)より良い側に振れる確率」。基準はエンジンの中央の見積りなので出発点は 50%、
    # そこから先行指標で上下させる(growth-stage-evaluation §9。参照クラスは振れの重さの根拠に使う)。
    "N1": dict(name="獲得効率(会員の伸び・販促費率・NIM が基準より良い)",
               base_rate=0.50, adj=+0.02,
               why_base="基準: 会員純増 年 460→400 万人、販促費率 30%→25.5%(2027→30)",
               why_adj="+ クロスバイ 35→51%・製品当たり販促費 −15%・認知度 10.4%、− 会員当たり販促費 +17%(前期比)・FS 貢献利益率 −6pt"),
    "N2": dict(name="資本の転換(LPB が基準より伸び、資本の上限を超えた分を受ける)",
               base_rate=0.50, adj=-0.10,
               why_base="基準: LPB 年 +12〜15%、資本の上限を超えた個人ローンの 30% を LPB で組成",
               why_adj="− LPB 組成 37→31 億ドル、自社保有へ配分 49→29%、金利上昇、買い手は衝撃時に 3 回中 2 回引いた(LendingClub 2016・2023、Upstart 2022)、+ 契約 100 億ドル超・私募クレジットの資金シェア 6→25%"),
    "N3": dict(name="信用(all-in 貸倒率が基準 3.7% より良い)",
               base_rate=0.50, adj=-0.10,
               why_base="基準: all-in 3.7% が続く。良い側 3.2%、悪い側 4.2%(公正価値の損失前提 4.8% の内側)",
               why_adj="− 失業率 4.2%、TransUnion の個人ローン延滞 3.81%(前年 3.37%)、金利は上昇方向、+ all-in は直近改善"),
    "N4": dict(name="新しい収益線(Tech Platform の伸びが基準 8〜10% を上回る、SoFiUSD)",
               base_rate=0.50, adj=0.0,
               why_base="基準: Tech Platform 年 +8〜10%、SoFiUSD の収益 0",
               why_adj="+ 前期比 +12.5%・新規 13 社・SoFi Money の自社コア移行、− 貢献利益率 16→14%、大口除外後の伸び 12%(目標 20%)"),
}
COND = {("N2", "N3"): (0.55, 0.30), ("N1", "N3"): (0.62, 0.45)}   # P(Nx が良い側 | N3 良い側), P(Nx | N3 悪い側)


def node_p(k):
    """無条件の確率。N1・N2 は N3 との条件付きから合成する。"""
    if k in ("N1", "N2"):
        p3 = NODES["N3"]["base_rate"] + NODES["N3"]["adj"]
        a, b = COND[(k, "N3")]
        return p3 * a + (1 - p3) * b
    n = NODES[k]
    return n["base_rate"] + n["adj"]


SHOCKS = {
    "N1": dict(mem_add=([4.3, 5.0, 5.0, 4.8, 4.6], [4.3, 4.2, 3.8, 3.6, 3.4]),
               sm=([0.32, 0.29, 0.27, 0.255, 0.24], [0.32, 0.31, 0.30, 0.285, 0.27]),
               nim=([0.0600, 0.0600, 0.0595, 0.0590, 0.0585], [0.0600, 0.0570, 0.0555, 0.0540, 0.0535])),
    "N2": dict(lpb_g_base=([None, 0.22, 0.25, 0.25, 0.22], [None, 0.02, 0.05, 0.05, 0.02]),
               spill_conv=(0.55, 0.05)),
    "N3": dict(credit_shock=(-0.005, 0.005)),
    "N4": dict(tp_g=([None, 0.18, 0.20, 0.20, 0.20], [None, -0.02, 0.0, 0.0, 0.0]),
               extra_rev=([0, 0.01e9, 0.02e9, 0.03e9, 0.04e9], [0, 0, 0, 0, 0])),
}


def tree(eng_mult):
    combos = []
    p3 = node_p("N3")
    for s in itertools.product([1, 0], repeat=4):
        st = dict(zip(["N1", "N2", "N3", "N4"], s))
        kw = {}
        for k, ok in st.items():
            for var, (succ, fail) in SHOCKS[k].items():
                kw[var] = succ if ok else fail
        path = vm.engine(**kw)
        _, val = vm.fair_path(vm.eps_of(path), eng_mult)
        # 同時確率: N3 → N1・N2 は N3 に条件付き、N4 は独立
        p = p3 if st["N3"] else 1 - p3
        for k in ("N1", "N2"):
            pc = COND[(k, "N3")][0 if st["N3"] else 1]
            p *= pc if st[k] else 1 - pc
        p *= node_p("N4") if st["N4"] else 1 - node_p("N4")
        combos.append(dict(state=st, p=p, value=val, eps={y: round(path[y]["eps"], 3) for y in vm.YEARS},
                           cap_ratio_2028=path[2028]["cap_ratio"]))
    ev = sum(c["p"] * c["value"] for c in combos)
    var = sum(c["p"] * (c["value"] - ev) ** 2 for c in combos)
    allok = [c for c in combos if all(c["state"].values())][0]
    allng = [c for c in combos if not any(c["state"].values())][0]
    # 3 つの束: 強気(うまくいった場合)= 獲得効率と資本の転換がともに良い側、弱気 = ともに悪い側、ベース = 片方だけ
    bull = [c for c in combos if c["state"]["N1"] and c["state"]["N2"]]
    bear = [c for c in combos if (not c["state"]["N1"]) and (not c["state"]["N2"])]
    basec = [c for c in combos if c not in bull and c not in bear]

    def bundle(cs):
        p = sum(c["p"] for c in cs)
        return dict(p=p, value=sum(c["p"] * c["value"] for c in cs) / p)
    return dict(combos=combos, expected=ev, sd=var ** 0.5, all_success=allok, all_fail=allng,
                bundles=dict(bull=bundle(bull), base=bundle(basec), bear=bundle(bear)))


def run():
    base = vm.engine()
    ev = vm.engine_value(base)
    eng_mult = {t: ev * (1 + vm.COE) ** (t - 2026 + 0.2) / base[t + 1]["eps"] for t in [2026, 2027, 2028, 2029]}
    out = {}
    out["g1"] = g1_unit_economics()
    out["g2"] = g2_discretionary(base)
    out["g4"] = g4_embedded()
    out["g5"] = g5_self_sufficiency()
    out["g7"] = g7_sofiusd()

    # 第1版(構造 C の PEG)と第2版(構造 B の PEG)の 3 経路
    paths = {"consensus": vm.CONS, "company": vm.COMP, "engine": vm.eps_of(base)}
    vals = {}
    for label, peg in (("v1_C", dict(vm.PEG)), ("v2_B", PEG_B)):
        vm.PEG = peg
        vals[label] = {k: round(vm.fair_path(e, eng_mult)[1], 2) for k, e in paths.items()}
        vals[label + "_rows_engine"] = [{kk: (round(vv, 2) if isinstance(vv, float) else vv) for kk, vv in r.items()}
                                        for r in vm.fair_path(paths["engine"], eng_mult)[0]]
        t = tree(eng_mult)
        vals[label + "_tree"] = dict(expected=round(t["expected"], 2), sd=round(t["sd"], 2),
                                    bundles={k: dict(p=round(v["p"], 3), value=round(v["value"], 2)) for k, v in t["bundles"].items()},
                                    all_success=dict(p=round(t["all_success"]["p"], 3), value=round(t["all_success"]["value"], 2), eps=t["all_success"]["eps"]),
                                    all_fail=dict(p=round(t["all_fail"]["p"], 3), value=round(t["all_fail"]["value"], 2), eps=t["all_fail"]["eps"]))
        if label == "v2_B":
            out["tree_combos"] = [dict(state="".join("○" if c["state"][k] else "×" for k in ["N1", "N2", "N3", "N4"]),
                                       p=round(c["p"], 3), value=round(c["value"], 2), eps2028=c["eps"][2028]) for c in t["combos"]]
            b = t["bundles"]
            # 市場の暗黙の強気確率(弱気の確率を固定し、強気とベースの間で株価に合う比率)
            pb = b["bear"]["p"]
            rest = 1 - pb
            x = (vm.PRICE - pb * b["bear"]["value"] - rest * b["base"]["value"]) / (b["bull"]["value"] - b["base"]["value"])
            out["implied_bull_p"] = round(x, 3)
            # 感応度: N1・N2 の確率を ±10pt
            sens = []
            for d1 in (-0.10, 0.0, 0.10):
                row = []
                for d2 in (-0.10, 0.0, 0.10):
                    COND[("N1", "N3")] = (0.62 + d1, 0.45 + d1); COND[("N2", "N3")] = (0.55 + d2, 0.30 + d2)
                    tt = tree(eng_mult)
                    row.append(dict(ev=round(tt["expected"], 2), p_bull=round(tt["bundles"]["bull"]["p"], 3)))
                    COND[("N1", "N3")] = (0.62, 0.45); COND[("N2", "N3")] = (0.55, 0.30)
                sens.append(dict(dN1=d1, values=row))
            out["tree_sens"] = sens
    vm.PEG = dict(PEG_B)
    out["values"] = vals
    # エントリー価格帯(構造 B: α 20〜25% の中央 22.5%)
    a = 0.225
    B = vals["v2_B"]["engine"]
    L = vals["v2_B_tree"]["bundles"]["bear"]["value"]
    U = vals["v2_B_tree"]["bundles"]["bull"]["value"]
    out["entry"] = dict(alpha=a, B=B, U=U, L=L, Z1=round(min(B * (1 - a), L * (1 + a / 2)), 2), Z2=round(B * (1 - a / 2), 2),
                        up_down=round((U - vm.PRICE) / (vm.PRICE - L), 2) if vm.PRICE > L else None)
    out["nodes"] = {k: dict(name=v["name"], p=round(node_p(k), 2), base_rate=v["base_rate"], adj=v["adj"], why_base=v["why_base"], why_adj=v["why_adj"])
                    for k, v in NODES.items()}
    out["cond_p"] = {f"{a}|{b}": v for (a, b), v in COND.items()}
    with open(os.path.join(OUT, "growth_v2.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, default=float)
    return out


if __name__ == "__main__":
    o = run()
    g1 = o["g1"]
    print("G1 rows", [(r["q"], r["per_member"], r["per_product"], r["new_member_product"]) for r in g1["rows"]])
    print(f"G1 pre-SM margin {g1['pre_sm_margin']:.3f} capcharge {g1['cap_charge']:.3f} econ {g1['econ_margin']:.3f} incRev {g1['inc_rev']:.0f} SM4Q {g1['sm_4q']:.0f} maint {g1['maint_sm']:.0f} growthSM {g1['growth_sm']:.0f} annProfit {g1['annual_profit']:.0f}")
    for c in g1["cases"]:
        print("  ", c)
    print("  product check", g1["product_check"])
    print("G2", {k: (round(v['discretionary']/1e9, 2), round(v['eps_add'], 3)) for k, v in o["g2"]["levels"].items()},
          "per pt", round(o["g2"]["eps_per_pt"], 4), "reinvest26", round(o["g2"]["reinvest_2026"], 3),
          "eps29", round(o["g2"]["eps29"], 3), "flat", round(o["g2"]["eps29_sm_flat"], 3), "share", round(o["g2"]["share_of_growth_from_sm"], 3))
    print("G4", {k: round(v, 3) if isinstance(v, float) else v for k, v in o["g4"].items()})
    print("G5", round(o["g5"]["ratio"], 2), o["g5"]["generation"] / 1e9, o["g5"]["need"] / 1e9)
    print("G7", o["g7"])
    print("values", json.dumps(o["values"], ensure_ascii=False, indent=0)[:3000])
    print("implied bull", o["implied_bull_p"])
    print("sens", o["tree_sens"])
    print("entry", o["entry"])
    for c in o["tree_combos"]:
        print(c)
