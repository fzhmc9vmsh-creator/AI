"""SOFI バリュエーション(Opus、2026-10-18)。
前提は calc/prereg.md に固定。入力の出所は research/ と research_r2/(すべて WebSearch 要約経由)。
出力: out/val.json(スライドの数値の正)。
"""
import json
import math
import os

OUT = os.path.join(os.path.dirname(__file__), "out")
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- 入力(出所)
PRICE = 14.55                 # 2026-10-16 終値(R2)
SH_BASIC = 1.2903e9           # 2026-06-30 発行済(R2, Q2'26 8-K)
SH_DIL_26 = 1.375e9           # 2026 希薄化後(ガイダンス 825M / 0.60、R1a)
TBV0, TBVPS0 = 9.5e9, 7.34    # 2026-06-30(R7)
CAP_TOTAL0, RWA0 = 9.169e9, 48.68e9   # 総自己資本・RWA 2026-06-30(R7)

# 株主資本コスト(prereg): rf 10年 5.2%(R7: 9/23 5.11%、10/14 約5.3%)、β=平均(SOFI 2.2, 同業 NU 0.95・HOOD 2.35 の中央 1.65)=1.93、ERP 4.5%
RF, BETA, ERP = 0.052, (2.2 + (0.95 + 2.35) / 2) / 2, 0.045
COE = RF + BETA * ERP
G_LR = 0.05                   # 成熟後の永続成長(名目)

YEARS = [2026, 2027, 2028, 2029, 2030]

# コンセンサス(調整後EPS = GAAPに近い。R2/R8)。2030 は 2029→2030 +18%(減速の延長、明記)
CONS = {2026: 0.60, 2027: 0.83, 2028: 1.08, 2029: 1.32}
CONS[2030] = round(CONS[2029] * 1.18, 3)

# 会社シナリオ: 2025 EPS 0.39(R3b)、2025→2028 EPS CAGR 38〜42% の上限側 + 2026 は ガイダンス 0.60
COMP = {2026: 0.60}
COMP[2028] = round(0.39 * 1.42 ** 3, 3)
COMP[2027] = round(math.sqrt(COMP[2026] * COMP[2028]), 3)
COMP[2029] = round(COMP[2028] * 1.32, 3)     # 売上 CAGR 30% 以上 + 営業レバレッジ(会社は 2027-28 に加速と発言)
COMP[2030] = round(COMP[2029] * 1.25, 3)


# ---------------------------------------------------------------- 事業エンジン
def engine(sh=None, **kw):
    """会員 × 2つのエンジン(B/S貸出・手数料)× 費用率。資本比率の下限で B/S の伸びを律速。
    kw で変数を上書き(強気・弱気・感応度)。"""
    p = dict(
        mem_add=[4.3, 4.6, 4.4, 4.2, 4.0],       # 年間の会員純増(百万)。2026 は H1 2.1 + H2 2.2
        mem0=13.7,
        nim=[0.0600, 0.0585, 0.0575, 0.0565, 0.0560],
        iea_avg26=54.5e9,                         # 2026 平均利付資産(Q2 52.9B、年末 ~62B)
        rwa_iea=0.92,                             # RWA / 利付資産(48.7/52.9)
        bs_growth_want=[None, 0.32, 0.25, 0.22, 0.20],   # 資本が許せば B/S を伸ばしたい率
        cap_floor=0.14,                           # 総自己資本比率の運用下限(low-to-mid teens)
        lpb=[0.58e9], lpb_g_base=[None, 0.12, 0.15, 0.15, 0.12],
        fs_fee=[0.31e9], fs_g=[None, 0.40, 0.30, 0.25, 0.20],
        tp=[0.32e9], tp_g=[None, 0.08, 0.10, 0.10, 0.10],
        gains=[0.38e9], gains_g=[None, 0.15, 0.15, 0.12, 0.10],
        elim=-0.20e9,
        sm=[0.32, 0.30, 0.285, 0.27, 0.255],      # 販促費 / 売上
        tpd=[0.16, 0.150, 0.142, 0.135, 0.13],    # 技術・製品開発 / 売上
        ops=[0.30, 0.293, 0.287, 0.282, 0.278],   # 運営・一般管理(引当・償却含む) / 売上
        credit_shock=0.0,                         # 個人ローン NCO の恒常変化(pp)。個人ローン残高比 ~48% × iea
        tax=[0.22, 0.23, 0.23, 0.23, 0.23],
        sh_g=0.015, conv_extra=0.03e9,            # SBC 等の年率希薄化、2029 以降の転換社債の追加株(キャップ超)
    )
    p.update(kw)
    out = {}
    mem = p["mem0"]
    iea_avg = p["iea_avg26"]
    iea_end_prev = 62.0e9                         # 2026 年末の利付資産(推定)
    cap = CAP_TOTAL0 + 0.50e9 + 0.13e9            # 2026 年末の資本: H2 純利益 + SBC
    lpb, fs, tp, gains = p["lpb"][0], p["fs_fee"][0], p["tp"][0], p["gains"][0]
    shares = sh or SH_DIL_26
    for i, y in enumerate(YEARS):
        mem_prev = mem
        mem = mem + p["mem_add"][i]
        if i > 0:
            # B/S の伸び: 希望 vs 資本の上限(年末の総自己資本比率 ≥ cap_floor)
            want_end = iea_end_prev * (1 + p["bs_growth_want"][i])
            cap_room_end = cap / p["cap_floor"] / p["rwa_iea"]          # 期首資本で見た上限(保守的)
            # 期中の利益を加えた上限
            iea_end = min(want_end, max(cap_room_end, iea_end_prev))
            spill = max(want_end - iea_end, 0.0)                       # 資本で持てない分は LPB へ
            iea_avg = (iea_end_prev + iea_end) / 2
            iea_end_prev = iea_end
            lpb = lpb * (1 + p["lpb_g_base"][i]) + spill * 0.30 * 0.046  # 溢れた個人ローン相当の3割を組成、手数料 4.6%
            fs *= 1 + p["fs_g"][i]
            tp *= 1 + p["tp_g"][i]
            gains *= 1 + p["gains_g"][i]
        else:
            spill = 0.0
        nii = iea_avg * p["nim"][i]
        credit = -p["credit_shock"] * 0.48 * iea_avg                    # 個人ローン ~48%
        rev = nii + lpb + fs + tp + gains + p["elim"]
        if i == 0:
            rev_scale = 4.80e9 / rev                                     # 2026 をガイダンス中央に較正
        rev *= rev_scale
        pretax = rev * (1 - p["sm"][i] - p["tpd"][i] - p["ops"][i]) + credit
        ni = pretax * (1 - p["tax"][i])
        if i > 0:
            shares *= 1 + p["sh_g"]
            if y >= 2029:
                shares += p["conv_extra"] if y == 2029 else 0
        cap += ni + 0.27e9 if i > 0 else 0
        out[y] = dict(members=round(mem, 2), rev=rev, nii=nii * rev_scale, lpb=lpb * rev_scale,
                      ni=ni, eps=ni / shares, shares=shares, iea_avg=iea_avg,
                      cap_ratio=cap / (iea_end_prev * p["rwa_iea"]) if i > 0 else None, spill=spill)
    return out


def eps_of(path):
    return {y: path[y]["eps"] for y in YEARS}


# ---------------------------------------------------------------- 妥当 PER と年度別理論株価
PEER_PER = 13.6      # 成長と ROTCE の近い消費者金融: NU 16x・LC 11.2x の平均(R8)。S&P500 19.0x、低成長の銀行 7〜8x
PEG = {2026: 0.90, 2027: 0.85, 2028: 0.80, 2029: 0.80}   # 構造評価 C の出発 0.8〜1.0、年度で狭いレンジの中央
FLOOR = 1 / COE


def cagr(a, b, n):
    return (b / a) ** (1 / n) - 1 if a > 0 and b > 0 else 0.0


def ext(eps, y):
    """2030 より先は 2029→2030 の伸びを毎年 3pt ずつ減速させて延長(延長部分と明記)。"""
    e = dict(eps)
    g = e[2030] / e[2029] - 1
    for k in range(2031, 2035):
        g = max(g - 0.03, G_LR)
        e[k] = e[k - 1] * (1 + g)
    return e


def theory_per(g, roe, r=None, gl=G_LR):
    """成熟年度: PER ≒ (1 − g/ROE) ÷ (r − g)。r は呼び出し時の COE。"""
    r = COE if r is None else r
    return (1 - gl / roe) / (r - gl)


def fair_path(eps, engine_mult=None, surv=0.985):
    """年度末 t の理論株価 = 妥当PER_t × EPS_{t+1}。妥当PER = 平均(a 同業, b PEG×g(下限1/r), c エンジン倍率)。"""
    e = ext(eps, 2030)
    rows = []
    for t in [2026, 2027, 2028, 2029]:
        nxt = e[t + 1]
        g3 = cagr(e[t + 1], e[t + 4], 3)
        b = max(PEG[t] * g3 * 100, FLOOR)
        a = PEER_PER
        c = engine_mult[t] if engine_mult else None
        per = (a + b + c) / 3 if c else (a + b) / 2
        target = per * nxt
        yrs = (t - 2026) + (12 - 9.5) / 12            # 2026-10 中旬から年度末まで
        pv = target / (1 + COE) ** yrs * surv
        rows.append(dict(year=t, eps_next=nxt, g3=g3, a=a, b=b, c=c, per=per, target=target, pv=pv))
    w = [0.4, 0.3, 0.2, 0.1]
    val = sum(r["pv"] * wi for r, wi in zip(rows, w))
    return rows, val


# ---------------------------------------------------------------- エンジン DCF(必要資本ベースの FCFE)→ 年度ごとの倍率
def engine_value(path):
    """株主への配分可能額 = 純利益 − 必要資本の増分。必要資本 = 14.5% × RWA。超過資本は配分可能。"""
    req_prev = 0.145 * 48.68e9 * 62.0 / 52.9      # 2026 年末の必要資本(RWA を年末 IEA で伸ばす)
    excess0 = (CAP_TOTAL0 + 0.63e9) - req_prev
    pv = 0.0
    vals = {}
    iea_prev = 62.0e9
    for i, y in enumerate(YEARS[1:], start=1):
        ni = path[y]["ni"]
        iea_end = 2 * path[y]["iea_avg"] - iea_prev
        req = 0.145 * iea_end * 0.92
        fcfe = ni - (req - req_prev)
        req_prev, iea_prev = req, iea_end
        pv += fcfe / (1 + COE) ** i
    # 終価(2030 末): 成熟 PER の理論式 × 2031 純利益相当
    ni31 = path[2030]["ni"] * 1.12
    tv = theory_per(G_LR, 0.18) * ni31
    pv += tv / (1 + COE) ** 4
    v = (pv + excess0) / SH_DIL_26
    return v


# ---------------------------------------------------------------- 金融の交差確認(TBV × ROTCE)
def tbv_check(rotce_ss, g=G_LR, r=None):
    r = COE if r is None else r
    tbvps_27 = TBVPS0 + 0.36 + 0.83 * 0.5                       # 2027 年央の TBVPS 概算(留保利益)
    return tbvps_27 * (rotce_ss - g) / (r - g) / (1 + r) ** 0.7


def run():
    global COE, FLOOR
    base = engine()
    bull = engine(mem_add=[4.3, 5.0, 5.0, 4.8, 4.6], sm=[0.32, 0.29, 0.27, 0.255, 0.24],
                  nim=[0.0600, 0.0600, 0.0595, 0.0590, 0.0585], credit_shock=-0.0075)
    bear = engine(mem_add=[4.3, 4.2, 3.8, 3.6, 3.4], sm=[0.32, 0.31, 0.30, 0.285, 0.27],
                  nim=[0.0600, 0.0570, 0.0555, 0.0540, 0.0535], credit_shock=0.0075)
    paths = {"consensus": CONS, "company": COMP, "engine": eps_of(base), "bull": eps_of(bull), "bear": eps_of(bear)}

    # エンジン倍率(c): エンジン価値 ÷ エンジン翌年度 EPS を、年度末ごとに価値を COE で前進させて近似
    ev = engine_value(base)
    eng_mult = {}
    for t in [2026, 2027, 2028, 2029]:
        v_t = ev * (1 + COE) ** (t - 2026 + 0.2)
        eng_mult[t] = v_t / base[t + 1]["eps"] if t + 1 in base else v_t / (base[2030]["eps"] * 1.12)

    res = {}
    for k, e in paths.items():
        rows, val = fair_path(e, eng_mult)
        res[k] = dict(eps={y: round(e[y], 3) for y in YEARS}, rows=rows, value=val, gap=val / PRICE - 1)

    w_val = 0.25 * res["bull"]["value"] + 0.5 * res["engine"]["value"] + 0.25 * res["bear"]["value"]
    # 株価に一致する弱気の確率(強気:ベース = 1:2 固定、2点(ベース・弱気)の2定義)
    vb, ve, vbr = res["bull"]["value"], res["engine"]["value"], res["bear"]["value"]
    # 定義1: 強気25%固定、ベースと弱気で残り75%
    p1 = (0.25 * vb + 0.75 * ve - PRICE) / (0.75 * (ve - vbr)) * 0.75 if ve != vbr else None
    # 定義2: ベースと弱気の2点
    p2 = (ve - PRICE) / (ve - vbr) if ve != vbr else None

    # 交差確認
    tbv = {r: tbv_check(r) for r in (0.12, 0.15, 0.18, 0.20)}

    # 定常状態価値(成長投資を止めた場合): 販促 16%・技術 14%・運営 29% → 税前 41%、税 23%
    ss_ni = 4.80e9 * (1 - 0.16 - 0.14 - 0.29) * 0.77
    ss_val = ss_ni / COE
    excess = (CAP_TOTAL0 + 0.63e9) - 0.145 * 48.68e9 * 62.0 / 52.9
    ss_ps = (ss_val + excess) / SH_DIL_26
    growth_price = PRICE - ss_ps

    # 感応度(F12): 芯 = 信用(NCO)× 販促費率の経路
    sens = []
    for cs in (-0.0075, 0.0, 0.0075, 0.015):
        row = []
        for dsm in (-0.02, 0.0, 0.02):
            pth = engine(credit_shock=cs, sm=[0.32] + [x + dsm for x in [0.30, 0.285, 0.27, 0.255]])
            _, v = fair_path(eps_of(pth), eng_mult)
            row.append(round(v, 2))
        sens.append(dict(credit_shock_pp=cs * 100, values=row))
    # 金利(COE)感応度 ±100bp
    rate_sens = {}
    base_coe = COE
    for d in (-0.01, 0.0, 0.01):
        COE = base_coe + d
        FLOOR = 1 / COE
        ev_d = engine_value(base)
        em = {t: ev_d * (1 + COE) ** (t - 2026 + 0.2) / base[t + 1]["eps"] for t in [2026, 2027, 2028, 2029]}
        _, v = fair_path(eps_of(base), em)
        rate_sens[round(d * 1e4)] = dict(value=round(v, 2), dcf=round(ev_d, 2))
    COE, FLOOR = base_coe, 1 / base_coe

    # ROTCE の経路(エンジン): 純利益 ÷ 平均有形自己資本(期首 TBV 2026末 ≈ 9.5 + 0.50 + 0.13)
    tbv_run = 9.5e9 + 0.63e9
    rotce = {}
    for y in YEARS[1:]:
        ni = base[y]["ni"]
        rotce[y] = round(ni / (tbv_run + ni / 2 + 0.135e9), 3)
        tbv_run += ni + 0.27e9
    # 株価に一致する強気の確率(ベースと強気の2点)
    p_bull = (PRICE - res["engine"]["value"]) / (res["bull"]["value"] - res["engine"]["value"])
    # EPS の対数分解(2025→2026): 売上・税引前利益率・税・希薄化(調整後ベース)
    import math as _m
    rev25, ni25, sh25, tax25 = 3.60e9, 0.481e9, 0.481e9 / 0.39, 0.13
    rev26, ni26, sh26, tax26 = 4.80e9, 0.825e9, SH_DIL_26, 0.22
    dec = dict(total=_m.log(0.60 / 0.39), revenue=_m.log(rev26 / rev25),
               pretax_margin=_m.log((ni26 / (1 - tax26) / rev26) / (ni25 / (1 - tax25) / rev25)),
               tax=_m.log((1 - tax26) / (1 - tax25)), dilution=-_m.log(sh26 / sh25))

    out = dict(
        inputs=dict(price=PRICE, coe=COE, rf=RF, beta=BETA, erp=ERP, peer_per=PEER_PER, peg=PEG, floor=FLOOR),
        engine_detail={y: {k: (round(v / 1e9, 3) if isinstance(v, float) and abs(v) > 1e6 else (round(v, 4) if isinstance(v, float) else v))
                           for k, v in base[y].items()} for y in YEARS},
        bull_detail={y: round(bull[y]["eps"], 3) for y in YEARS},
        bear_detail={y: round(bear[y]["eps"], 3) for y in YEARS},
        engine_value_dcf=ev, engine_mult=eng_mult,
        paths={k: dict(eps=v["eps"], value=round(v["value"], 2), gap=round(v["gap"], 3),
                       rows=[{kk: (round(vv, 3) if isinstance(vv, float) else vv) for kk, vv in r.items()} for r in v["rows"]])
               for k, v in res.items()},
        weighted_value=round(w_val, 2), weighted_gap=round(w_val / PRICE - 1, 3),
        implied_bear_prob=dict(def1=p1, def2=p2),
        tbv_check={f"{int(k*100)}%": round(v, 2) for k, v in tbv.items()},
        steady_state=dict(ni=ss_ni, value=ss_val, excess=excess, per_share=round(ss_ps, 2), growth_price=round(growth_price, 2),
                          growth_share=round(growth_price / PRICE, 3)),
        sens_credit_x_sm=sens, rate_sens=rate_sens, rotce=rotce, implied_bull_prob=p_bull, eps_decomp=dec,
    )
    with open(os.path.join(OUT, "val.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, default=float)
    return out


if __name__ == "__main__":
    o = run()
    print(f"COE={o['inputs']['coe']:.4f}  beta={o['inputs']['beta']:.3f}  floor PER={o['inputs']['floor']:.1f}")
    for y, d in o["engine_detail"].items():
        print(y, d)
    print("bull", o["bull_detail"])
    print("bear", o["bear_detail"])
    print("engine DCF value/sh", round(o["engine_value_dcf"], 2), "mult", {k: round(v, 1) for k, v in o["engine_mult"].items()})
    for k, v in o["paths"].items():
        print(f"{k:10s} EPS {v['eps']}  value {v['value']}  gap {v['gap']:+.1%}")
        for r in v["rows"]:
            print("   ", r)
    print("weighted", o["weighted_value"], o["weighted_gap"])
    print("implied bear prob", o["implied_bear_prob"])
    print("TBV check", o["tbv_check"])
    print("steady", o["steady_state"])
    print("sens credit x sm", o["sens_credit_x_sm"])
    print("rate sens", o["rate_sens"])
    print("rotce", o["rotce"], "p_bull", round(o["implied_bull_prob"],3))
    print("decomp", {k: round(v,3) for k,v in o["eps_decomp"].items()})
