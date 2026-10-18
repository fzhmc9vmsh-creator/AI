"""SOFI 第3版(Opus、2026-10-18): 成長企業の評価のやり直し(meigara-bunseki-method 第5版 growth-stage-evaluation.md)。
§1 フェーズ → §2 二層の構造 → §3 KPI の率 → §4 EPS の四半期分解 → §5 フライホイール(数字の確かめ)→ §6 資本モデルの業界比較
→ §7 金利の両面と市場の織り込み → 条件6 の市場との乖離 → §12 節点ツリー(確率の更新)→ §13 価値評価 → エントリー。
入力: research_r4/(R13 同業の PEG・R14 四半期 EPS・R15 金利の両面・R16 体験と保有の業界比較)と既存の調査。すべて WebSearch の要約経由。
出力: out/growth_v3.json(第3版のスライドの数値の正)。
"""
import itertools
import json
import os

import val_model as vm
import growth_v2 as g2

OUT = os.path.join(os.path.dirname(__file__), "out")


def pct(a, b):
    return a / b - 1


# ---------------------------------------------------------------- §3 根幹 KPI の率(R1b・R10・R16)
QS = ["Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
MEMBERS = [8.77, 9.37, 10.13, 10.9, 11.7, 12.6, 13.7, 14.7, 15.8]          # 百万人(期末)
PRODUCTS = [12.8, 13.7, 14.7, 15.8, 17.1, 18.6, 20.2, 22.0, 24.4]          # 百万(期末)
NET_MEM = [643, 756, 785, 800, 850, 905, 1000, 1100, 1100]                  # 千人(四半期の純増)
NET_PROD = [946, 1100, 1100, 1200, 1260, 1400, 1600, 1800, 2200]
CROSS = [None, None, 0.33, 0.36, 0.35, 0.40, 0.40, 0.43, 0.51]
DEPOSITS = [None, None, 26.0, 27.3, 29.5, 32.9, 37.5, 40.2, 45.5]           # 十億ドル
REV_ADJ = {"Q3 24": 689.4, "Q4 24": 739.1, "Q1 25": 770.7, "Q2 25": 858.2, "Q3 25": 962.0, "Q4 25": 1013.0, "Q1 26": 1087.2, "Q2 26": 1205.6}
# セグメント(百万ドル): FS は NII・LPB 手数料・その他の手数料に分ける(R2・R1b。Q2'25 の LPB 手数料は差額 362.5 − 193.3 − 41.8)
FS = {"Q2 25": dict(total=362.5, nii=193.3, lpb=127.4, other=41.8), "Q2 26": dict(total=466.3, nii=249.1, lpb=140.9, other=76.3)}
LENDING = {"Q2 25": 447.6, "Q2 26": 711.7}
TP = {"Q2 25": 109.8, "Q1 26": 75.1, "Q2 26": 84.5}


def word(yoy_series):
    """前年比の率の推移から判定の言葉(§3)。直近 3 期の変化が ±2pt 以内なら維持。"""
    last3 = yoy_series[-3:]
    if max(last3) - min(last3) <= 0.02:
        return "高水準で維持" if last3[-1] >= 0.20 else "維持"
    if last3[-1] > last3[0]:
        return "加速"
    return "減速"


def kpi_rates():
    rows = []
    for i in range(4, len(QS)):
        r = dict(q=QS[i],
                 mem=MEMBERS[i], mem_qoq=pct(MEMBERS[i], MEMBERS[i - 1]), mem_qoq_ann=(MEMBERS[i] / MEMBERS[i - 1]) ** 4 - 1,
                 mem_yoy=pct(MEMBERS[i], MEMBERS[i - 4]), net_mem=NET_MEM[i], net_mem_yoy=pct(NET_MEM[i], NET_MEM[i - 4]),
                 prod=PRODUCTS[i], prod_qoq=pct(PRODUCTS[i], PRODUCTS[i - 1]), prod_yoy=pct(PRODUCTS[i], PRODUCTS[i - 4]),
                 net_prod_yoy=pct(NET_PROD[i], NET_PROD[i - 4]), ppm=PRODUCTS[i] / MEMBERS[i], cross=CROSS[i],
                 dep=DEPOSITS[i], dep_qoq=pct(DEPOSITS[i], DEPOSITS[i - 1]) if DEPOSITS[i - 1] else None,
                 dep_yoy=pct(DEPOSITS[i], DEPOSITS[i - 4]) if DEPOSITS[i - 4] else None)
        q4 = QS[i - 4]
        if QS[i] in REV_ADJ and q4 in REV_ADJ:
            r["rev_yoy"] = pct(REV_ADJ[QS[i]], REV_ADJ[q4])
        rows.append(r)
    words = dict(members=word([r["mem_yoy"] for r in rows]), products=word([r["prod_yoy"] for r in rows]),
                 revenue=word([r["rev_yoy"] for r in rows if "rev_yoy" in r]))
    seg = dict(
        lending_yoy=pct(LENDING["Q2 26"], LENDING["Q2 25"]),
        fs_yoy=pct(FS["Q2 26"]["total"], FS["Q2 25"]["total"]),
        fs_nii_yoy=pct(FS["Q2 26"]["nii"], FS["Q2 25"]["nii"]),
        fs_lpb_yoy=pct(FS["Q2 26"]["lpb"], FS["Q2 25"]["lpb"]),
        fs_other_yoy=pct(FS["Q2 26"]["other"], FS["Q2 25"]["other"]),
        fs_ex_lpb_yoy=pct(FS["Q2 26"]["total"] - FS["Q2 26"]["lpb"], FS["Q2 25"]["total"] - FS["Q2 25"]["lpb"]),
        tp_yoy=pct(TP["Q2 26"], TP["Q2 25"]), tp_qoq=pct(TP["Q2 26"], TP["Q1 26"]),
        fs_yoy_series=dict(zip(["Q3 25", "Q4 25", "Q1 26", "Q2 26"], [0.76, 0.78, 0.41, 0.286])),
    )
    return dict(rows=rows, words=words, seg=seg)


# ---------------------------------------------------------------- §4 EPS の四半期分解(R14 §1)
EPSQ = [  # 四半期, GAAP 収益, 税引前, 税, 純利益, 希薄化後株数(百万)
    ("Q1 25", 771.759, 79.782, 8.666, 71.116, 1185.466),
    ("Q2 25", 854.9, 112.2, 14.9, 97.263, 1182.877),
    ("Q3 25", 961.6, 148.551, 9.159, 139.392, 1291.011),
    ("Q4 25", 1027.0, 185.3, 11.8, 173.549, 1346.110),
    ("Q1 26", 1100.368, 199.552, 32.821, 166.731, 1378.011),
    ("Q2 26", 1218.7, 204.309, 47.717, 156.592, 1351.990),
]


def bridge(a, b):
    """EPS = 収益 × 税引前利益率 × (1 − 税率) ÷ 株数。順に置き換えた差(R14 と同じ順序)。"""
    _, r0, p0, t0, n0, s0 = a
    _, r1, p1, t1, n1, s1 = b
    m0, m1, k0, k1 = p0 / r0, p1 / r1, 1 - t0 / p0, 1 - t1 / p1
    e0 = r0 * m0 * k0 / s0
    e_rev = r1 * m0 * k0 / s0
    e_mar = r1 * m1 * k0 / s0
    e_tax = r1 * m1 * k1 / s0
    e1 = r1 * m1 * k1 / s1
    return dict(start=e0, revenue=e_rev - e0, margin=e_mar - e_rev, tax=e_tax - e_mar, shares=e1 - e_tax, end=e1,
                pretax_ps_growth=(p1 / s1) / (p0 / s0) - 1, pretax_growth=p1 / p0 - 1, rev_growth=r1 / r0 - 1)


def eps_quarterly():
    rows = [dict(q=q, rev=r, pretax=p, tax_rate=t / p, ni=n, shares=s, eps=n / s, pretax_margin=p / r, pretax_ps=p / s)
            for q, r, p, t, n, s in EPSQ]
    yoy = bridge(EPSQ[1], EPSQ[5])
    qoq = bridge(EPSQ[4], EPSQ[5])
    # 下期の暗黙の値(通期の調整後純利益 8.25 億ドル、税率 22%)
    h1_ni, h1_pt = 166.731 + 160.406, 199.552 + 204.309
    fy_pt = 825 / (1 - 0.22)
    h2 = dict(ni=825 - h1_ni, pretax=fy_pt - h1_pt, q3_eps=0.17, q4_eps=0.19,
              q3_pretax_needed=0.17 * 1352 / (1 - 0.22))
    h2["q3_pretax_qoq"] = h2["q3_pretax_needed"] / 204.309 - 1
    # Q3 の税引前の積み上げ(仮説): 販促費を Q2 の 392 → 330、増収 +50(増分利益率 50%)
    h2["bridge_sm_cut"] = 392.4 - 330
    h2["bridge_rev"] = 50 * 0.5
    h2["bridge_total"] = 204.309 + h2["bridge_sm_cut"] + h2["bridge_rev"]
    # 税の正常化の 1 回限りの影響: 税率 6% → 22% を 2026 の税引前に当てた額
    tax_step = dict(pretax_2026=fy_pt, eps_effect=fy_pt * (0.22 - 0.065) / 1375)
    return dict(rows=rows, yoy=yoy, qoq=qoq, h2=h2, tax_step=tax_step,
                dilution=dict(shares_yoy=1351.99 / 1182.877 - 1, raises=140.5, other=169.1 - 140.5, conv_2029=79, adj_excl=27.4))


# ---------------------------------------------------------------- §1 フェーズと §2 二層の構造
def roe_path(path):
    """TBV の積み上げで ROTCE を出す(配当・自社株買いなし、SBC を年 2.7 億ドル加算)。"""
    tbv = 9.5e9 + 0.50e9 + 0.13e9                      # 2026 年末
    out = {2026: path[2026]["ni"] / (9.5e9 + 0.25e9)}
    for y in vm.YEARS[1:]:
        start = tbv
        tbv += path[y]["ni"] + 0.27e9
        out[y] = path[y]["ni"] / ((start + tbv) / 2)
    return out


def self_suff(path):
    """自給率 = 純利益 ÷ 必要資本の増加(14.5% × RWA の増分)。年ごと。"""
    out = {}
    iea_prev = 62.0e9
    for y in vm.YEARS[1:]:
        iea_end = 2 * path[y]["iea_avg"] - iea_prev
        need = 0.145 * (iea_end - iea_prev) * 0.92
        out[y] = path[y]["ni"] / need if need > 0 else None
        iea_prev = iea_end
    return out


def structure(path):
    roe = roe_path(path)
    ss = self_suff(path)
    rows = {}
    for y in vm.YEARS:
        p = path[y]
        prev = path[y - 1] if y > 2026 else None
        rows[y] = dict(rev=p["rev"], rev_g=(p["rev"] / prev["rev"] - 1) if prev else 0.40, members=p["members"],
                       nii_share=p["nii"] / p["rev"], fee_share=1 - p["nii"] / p["rev"], eps=p["eps"], rotce=roe[y],
                       self_suff=ss.get(y), cap_ratio=p["cap_ratio"])
    return rows


def phase():
    base = vm.engine()
    st = structure(base)
    sm = dict(zip(vm.YEARS, [0.32, 0.30, 0.285, 0.27, 0.255]))
    # ④ への移行: 収益の伸び 20% 未満 かつ 販促費率 28% 以下 の最初の年(会員の伸び 20% 未満も併記)
    trans = None
    for y in vm.YEARS[1:]:
        mem_g = base[y]["members"] / base[y - 1]["members"] - 1
        if st[y]["rev_g"] < 0.20 and sm[y] <= 0.285:
            trans = dict(year=y, rev_g=st[y]["rev_g"], sm=sm[y], mem_g=mem_g)
            break
    company = dict(rev_yoy=0.405, mem_yoy=0.35, prod_yoy=0.427, sm_ratio=392.4 / 1218.7, tpd_ratio=189.5 / 1218.7,
                   pretax_margin=(0.131, 0.168), incr_pretax_margin=(204.309 - 112.2) / (1218.7 - 854.9),
                   rotce_q2=160.406 * 4 / 9.5e3, cap_ratio=0.188, cap_floor=0.14, label="③ スケール(上端。② との境界)")
    segments = [
        dict(name="Lending(貸出)", rev=711.7, yoy=0.59, cp_margin=0.56, phase="③ スケール", note="需要でなく自己資本が律速。保有 71% へ配分を戻して NII を積む", next="自給率 1 以上(資本の生成が必要資本の増加を賄う)"),
        dict(name="Financial Services(預金・証券・カード・Plus・LPB)", rev=466.3, yoy=0.286, cp_margin=0.46, phase="② → ③", note="LPB を除く手数料 +83%、NII +29%。貢献利益率 52 → 46% は投資(Plus・暗号資産・販促)", next="貢献利益率の底打ちと、有料会員・交換手数料の規模化"),
        dict(name="Technology Platform(Galileo・Technisys)", rev=84.5, yoy=-0.23, cp_margin=0.14, phase="回復期(失注 → 底打ち → 信頼獲得)", note="前期比 +12.5%、自社の預金基盤を移行、新規 13 社。貢献利益は未底打ち", next="前年比がプラスに戻る Q1'27、貢献利益率 20% 台への回復"),
    ]
    return dict(company=company, segments=segments, transition=trans, structure=st)


# ---------------------------------------------------------------- §6 資本モデルの業界比較(R16 C・R5)
def capital_model():
    coupon, cof, loss, opex = 0.129, 0.031, 0.037, 0.015      # 個人ローン(コア、Q2'26 経営陣)。運営・回収の費用 1.5% は推定
    cap, tax, coe = 0.145, 0.23, vm.COE
    spread = coupon - cof - loss - opex
    roe_hold = spread * (1 - tax) / cap
    loss_be = coupon - cof - opex - coe * cap / (1 - tax)      # 保有の ROE が株主資本コストに等しくなる年率損失
    fee = 0.046                                                 # LPB の手数料(組成額比、R4)
    peers = [
        dict(name="銀行(Discover の個人ローン・Capital One・Ally)", hold="ほぼ全額", sell="ほぼ 0", funding="預金", shock="—"),
        dict(name="SoFi(個人ローン)", hold="71%(4 四半期で 51〜71%)", sell="29%(29〜49%)", funding="預金 455 億ドル", shock="配分を四半期単位で変えられる"),
        dict(name="LendingClub", hold="21〜36%", sell="64〜79%", funding="預金(2021 年に銀行化)", shock="2016 年: 銀行の投資家の割合 43 → 12%。2023 年: 組成 −43%(預金で一部を保有して支えた)"),
        dict(name="Upstart", hold="未償還ローンの約 6%", sell="大半", funding="提携先・機関投資家", shock="2022 年 Q2: 機関投資家の資金 −40% 超で組成が急減"),
    ]
    pros = ["買い手が引いても組成を続けられる(LendingClub 2016・2023、Upstart 2022 の弱点がない)",
            f"保有 1 件の経済性が高い(配分した資本の ROE 約 {roe_hold*100:.0f}% > 株主資本コスト {coe*100:.1f}%)",
            "保有と売却の配分を、資本と買い手の価格で四半期ごとに変えられる(LPB 29〜49%)"]
    cons = ["信用の損失を負う(景気で振れる)。損益分岐の年率損失は約 {:.1f}%(現在 3.7%)".format(loss_be * 100),
            "自己資本を使う(自給率 0.34。成長には外部の資本か LPB が要る)",
            "公正価値の評価が金利で振れる(ヘッジで相殺。資本比率には一時的に効く)"]
    return dict(spread=spread, roe_hold=roe_hold, loss_breakeven=loss_be, lpb_fee=fee, lpb_fee_after_tax=fee * (1 - tax),
                hold_value_per_100=spread * (1 - tax) * 100 * 2.0, peers=peers, pros=pros, cons=cons,
                verdict="B(銀行の標準に近い保有 + 売却の選択肢。MU 型ではない)")


# ---------------------------------------------------------------- §7 金利の両面(+100bp、R15)と市場の織り込み
def rates_two_sided():
    sh = 1.396e9          # 2027 年の希薄化後株数(エンジン)
    tax = 0.22
    dep = 45.5e9
    yr1 = dict(
        loans_reprice=26.1e9 * 0.55 * 0.01 + 16.13e9 * 0.15 * 0.01,     # 個人は 1 年で約 55%、学生は約 15% が組成の入れ替えで再価格
        cash=6.6e9 * 0.01,                                                 # 現金・有価証券(全額変動の上限)
        deposits_lo=-dep * 0.60 * 0.01, deposits_hi=-dep * 0.85 * 0.01,   # 預金ベータ 0.60〜0.85(R15 §3-3)
    )
    yr1["nii_lo"] = yr1["loans_reprice"] + yr1["cash"] + yr1["deposits_hi"]
    yr1["nii_hi"] = yr1["loans_reprice"] + yr1["cash"] + yr1["deposits_lo"]
    nii_company = -77.6e6 * 1.25          # 会社の表(2025-09)を B/S の伸び +25% で拡大
    yr3 = dict(loans_reprice=26.1e9 * 0.01 + 16.13e9 * 0.45 * 0.01, cash=6.6e9 * 0.01,
               deposits_lo=-dep * 0.60 * 0.01, deposits_hi=-dep * 0.85 * 0.01)
    yr3["nii_lo"] = yr3["loans_reprice"] + yr3["cash"] + yr3["deposits_hi"]
    yr3["nii_hi"] = yr3["loans_reprice"] + yr3["cash"] + yr3["deposits_lo"]
    credit = dict(lo=0.0, mid=-26.1e9 * 0.0010, hi=-26.1e9 * 0.0025)    # 固定金利で返済額は変わらない。景気の経路のみ +0〜25bp
    mark_gross = dict(lo=-0.75e9, hi=-1.05e9)                            # 割引率 +100bp(R15 §8)
    hedge_ratio = dict(lo=0.70, hi=1.00)                                 # 上期は スワップ益 ≥ 評価減(前年比の変動要因ベース)
    mark_net = dict(best=mark_gross["lo"] * (1 - hedge_ratio["hi"]), mid=-0.15e9, worst=mark_gross["hi"] * (1 - hedge_ratio["lo"]))
    coe_effect = None
    # 1 株当たりの価値への効果
    eps_nii_y1 = nii_company * (1 - tax) / sh
    eps_nii_y2 = eps_nii_y1 * 0.5
    v_nii = eps_nii_y1 / (1 + vm.COE) + eps_nii_y2 / (1 + vm.COE) ** 2
    v_credit = credit["mid"] * (1 - tax) / sh * 14.0                     # 恒常の損失を妥当 PER 14 倍で資本化
    v_mark = mark_net["mid"] * (1 - tax) / sh                            # 一時。保有分は残存期間の利回りで戻る(資本と成長余力には効く)
    # 株主資本コスト +1pt の効果(第2版の感応度: 14.90 → 14.36)
    v_coe = 14.36 - 14.90
    total = v_nii + v_credit + v_mark + v_coe
    rng = dict(lo=total * 0.6, hi=total * 1.55)
    # 2026 年の金利の動き: FF +25bp、2 年債 約 +125bp、10 年債 約 +110bp → 平行移動の換算 約 +100bp
    ytd = dict(ff=0.25, y2=1.25, y10=1.10, parallel_equiv=1.0)
    econ_ytd = total * ytd["parallel_equiv"]
    market = dict(price_start=25.1, price_now=vm.PRICE, ytd_change=vm.PRICE - 25.1,
                  kbw_day=-0.067 * 15.6, kbw_gross_after_tax_ps=-1.0e9 * (1 - tax) / 1.352e9,
                  kbw_net_after_tax_ps=dict(best=0.0, worst=mark_net["worst"] * (1 - tax) / 1.352e9),
                  share_of_ytd=econ_ytd / (vm.PRICE - 25.1))
    # 預金の価格: 9/16 の利上げ後も基本 APY 3.30% を据え置き(ベータ 0)、FF の中央 3.875%、同業 Chime 3.75%・Amex 3.90%
    deposit = dict(apy=0.033, ff_mid=0.03875, peers=[0.0375, 0.039], avg_cost_h1=0.0307,
                   gap_vs_peers=(0.033 - 0.0375, 0.033 - 0.039),
                   value_per_10bp=dep * 0.001 * (1 - tax) / sh * 14.0)
    return dict(yr1=yr1, yr3=yr3, nii_company=nii_company, credit=credit, mark_gross=mark_gross, mark_net=mark_net,
                per_share=dict(nii=v_nii, credit=v_credit, mark=v_mark, coe=v_coe, total=total, range=rng),
                ytd=ytd, econ_ytd=econ_ytd, market=market, deposit=deposit,
                down100=dict(nii_company=126.7e6 * 1.25, note="−100bp は NII +1.27 億ドル(会社の表)。上げより下げが大きい非対称"))


# ---------------------------------------------------------------- 条件6: 市場・同業との乖離(R13、condition-guide 第5版)
def cond6():
    ntm_eps = 0.205 * 0.60 + 0.795 * 0.83
    ntm_pe = vm.PRICE / ntm_eps
    mkt = dict(pe=19.0, g=0.15, peg=19.0 / 15)
    peers = dict(NU=0.52, LC=0.33, HOOD=1.62, ALLY=0.33, COF=0.51)       # HOOD は 1.42〜1.82 の中央(27.4% 基準)
    growth_peers = ["NU", "LC", "HOOD"]
    gp = sorted(peers[k] for k in growth_peers)
    gp_med = gp[1]
    wide = sorted(peers.values())
    wide_med = wide[2]
    rows = []
    for name, e in (("コンセンサス", vm.CONS), ("会社目標の延長", vm.COMP), ("事業エンジン", vm.eps_of(vm.engine()))):
        g = (e[2028] / e[2026]) ** 0.5 - 1
        peg = ntm_pe / (g * 100)
        r = dict(path=name, cagr=g, peg=peg, peg_ratio=peg / mkt["peg"], growth_mult=g / mkt["g"],
                 vs_growth_peer_med=peg / gp_med, vs_wide_med=peg / wide_med)
        r["A_market"] = r["peg_ratio"] <= 0.6 and r["growth_mult"] >= 2.0
        r["A_peer"] = peg <= gp_med * 1.0
        r["A_peer_within_err"] = peg <= gp_med * 1.15                      # 同業 PEG の誤差 ±15%(R13)
        rows.append(r)
    n_market = sum(r["A_market"] for r in rows)
    n_strict = sum(r["A_market"] and r["A_peer"] for r in rows)
    n_err = sum(r["A_market"] and r["A_peer_within_err"] for r in rows)
    return dict(ntm_eps=ntm_eps, ntm_pe=ntm_pe, market=mkt, peers=peers, growth_peer_median=gp_med, wide_median=wide_med,
                rows=rows, n_market=n_market, n_strict=n_strict, n_within_err=n_err,
                grade="A", note="市場比は 3 経路とも A の基準。同業(成長の近い NU・LC・HOOD)の中央値 0.52 とは並び(会社目標の経路は以下、"
                                 "コンセンサスは 4% 上、誤差 ±15% の内側)。安さは SoFi 固有でなく消費者金融の群の安さ → 条件7 で扱う")


# ---------------------------------------------------------------- §12 節点ツリー(第3版の確率の更新)
NODES_V3 = {
    "N1": dict(adj_cond=+0.03, why="+ 製品の前年比 37 → 40 → 43% と加速、会員当たり製品 1.46 → 1.54、製品の純増が会員の 2 倍(初)、会員の前年比 35% を 4 期維持(§3 の読み直し)"
                                   "、− 会員当たり販促費 +17%(前期比)・FS 貢献利益率 −6pt。第2版より +3pt"),
    "N2": dict(adj_cond=0.0, why="変更なし。+ 経営陣は配分を 6〜8 四半期の NII で調整すると明言、LendingClub は投資家の需要が供給を上回ると発言、− Q3 の金利上昇で買い手の価格が下がる可能性"),
    "N3": dict(p=0.43, why="+ 会員の質(FICO 746・年収 16.9 万ドル)、報告ベースの純償却 2.62% は LendingClub 3.2%・Discover 4.21% より低い、90 日延滞 0.40%(−7bp)、"
                           "固定金利で利上げが返済額に効かない、− 失業率 4.2%・業界の個人ローン延滞の上昇。第2版 40% → 43%"),
    "N4": dict(p=0.50, why="変更なし"),
}
COND_V3 = {("N1", "N3"): (0.65, 0.48), ("N2", "N3"): (0.55, 0.30)}


def tree_v3(eng_mult, cond=None, p3=None):
    cond = cond or COND_V3
    p3 = NODES_V3["N3"]["p"] if p3 is None else p3
    p4 = NODES_V3["N4"]["p"]
    combos = []
    for s in itertools.product([1, 0], repeat=4):
        st = dict(zip(["N1", "N2", "N3", "N4"], s))
        kw = {}
        for k, ok in st.items():
            for var, (succ, fail) in g2.SHOCKS[k].items():
                kw[var] = succ if ok else fail
        path = vm.engine(**kw)
        _, val = vm.fair_path(vm.eps_of(path), eng_mult)
        p = p3 if st["N3"] else 1 - p3
        for k in ("N1", "N2"):
            pc = cond[(k, "N3")][0 if st["N3"] else 1]
            p *= pc if st[k] else 1 - pc
        p *= p4 if st["N4"] else 1 - p4
        stc = structure(path)
        combos.append(dict(state=st, p=p, value=val, eps2028=path[2028]["eps"], rotce2028=stc[2028]["rotce"],
                           fee2028=stc[2028]["fee_share"], ss2028=stc[2028]["self_suff"], members2028=path[2028]["members"]))
    ev = sum(c["p"] * c["value"] for c in combos)
    sd = sum(c["p"] * (c["value"] - ev) ** 2 for c in combos) ** 0.5
    bull = [c for c in combos if c["state"]["N1"] and c["state"]["N2"]]
    bear = [c for c in combos if not c["state"]["N1"] and not c["state"]["N2"]]
    basec = [c for c in combos if c not in bull and c not in bear]

    def bundle(cs):
        p = sum(c["p"] for c in cs)
        return dict(p=p, value=sum(c["p"] * c["value"] for c in cs) / p, eps2028=sum(c["p"] * c["eps2028"] for c in cs) / p)
    pn = {k: sum(c["p"] for c in combos if c["state"][k]) for k in ["N1", "N2", "N3", "N4"]}
    return dict(combos=combos, ev=ev, sd=sd, bundles=dict(bull=bundle(bull), base=bundle(basec), bear=bundle(bear)), p_nodes=pn)


# ---------------------------------------------------------------- §2 条件 × 現在 × 将来 × 実現確率 × 統合
def realization(t, rule):
    return sum(c["p"] for c in t["combos"] if rule(c))


def two_layer(t, base_st):
    fee26 = base_st[2026]["fee_share"]
    P = dict(
        n1=t["p_nodes"]["N1"], n2=t["p_nodes"]["N2"], n4=t["p_nodes"]["N4"],
        rotce_ge_coe=realization(t, lambda c: c["rotce2028"] >= vm.COE),
        rotce_ge_11=realization(t, lambda c: c["rotce2028"] >= 0.11),
        fee_up3=realization(t, lambda c: c["fee2028"] >= fee26 + 0.03),
    )
    rows = [
        dict(c=1, name="競争優位", now="B", fut="A", node="N1", P=P["n1"], lead="クロスバイ 35→51%(4 期上昇)、製品の伸びが加速(3 期)", lead_ok=True,
             now_why="主口座の関係(預金の約 9 割超が給与振込)、預金金利を同業より低く置いても預金 +54%、純償却が同業より低い。単品の価格優位はない",
             fut_why="2028 年に会員 2,700 万・会員当たり製品 1.7 前後で、製品当たり獲得費と資金コストの差が数字で続く"),
        dict(c=2, name="コア事業の CF", now="B", fut="B", node="N1・N2", P=P["rotce_ge_11"], lead="増分の税引前利益率 25%(平均 17%)", lead_ok=True,
             now_why="フェーズ ③: ROTCE 7% は販促費 32%・余剰資本の結果。定常 ROTCE 約 15%、保有ローンの資本 ROE 約 24%",
             fut_why=f"2028 年 ROTCE はエンジンで {base_st[2028]['rotce']*100:.1f}%(資本コスト {vm.COE*100:.1f}% の手前)。A には 2028 年に資本コスト超え({P['rotce_ge_coe']*100:.0f}%)が要る"),
        dict(c=3, name="資産の転用", now="B", fut="A", node="N4", P=P["n4"], lead="Tech Platform 前期比 +12.5%、自社の預金基盤を移行", lead_ok=False,
             now_why="Tech Platform は失注後の回復期、SoFiUSD は自社カードの決済で稼働",
             fut_why="Tech Platform の再成長(前年比 +15% 超)と SoFiUSD の収益化"),
        dict(c=8, name="コモディティでない", now="B", fut="A", node="N1", P=P["n1"], lead="同上(N1)", lead_ok=True,
             now_why="単品(個人ローン・預金)は市場の商品。束(会員の質・体験・預金・金利割引)で獲得費・貸倒・資金コストが同業より低い",
             fut_why="有料会員(Plus)と手数料の比率が上がり、束に値段が付く"),
        dict(c=11, name="模倣困難", now="B", fut="A", node="N1", P=P["n1"], lead="同上(N1)", lead_ok=True,
             now_why="再現に約 57 億ドルと数年(免許・販促・技術)。部品ごとには再現の例がある",
             fut_why="会員 2,700 万の主口座と、10 年分の信用データ"),
        dict(c=12, name="収益の性格", now="B", fut="A", node="N2・N4", P=P["fee_up3"], lead="LPB の配分 49 → 29%(逆方向)", lead_ok=False,
             now_why="残高に乗る NII と、利用に乗る手数料。手数料型の比率 44 → 39%",
             fut_why="手数料型の比率がエンジンの 2026 年比 +3pt 以上(LPB と新しい収益線)"),
        dict(c=13, name="アーキタイプ", now="B", fut="A", node="N2", P=P["fee_up3"], lead="同上", lead_ok=False,
             now_why="業界比較: 銀行の標準に近い保有 + 売却の選択肢。信用の保有は MU 型ではない",
             fut_why="資本を使わない収益(LPB・Tech Platform・Plus)の比率が上がり、会員型の基盤(ORCL 型)に寄る"),
    ]
    for r in rows:
        p = r["P"]
        if r["now"] == r["fut"]:
            r["integrated"] = r["now"]
            r["rule"] = "同じ"
        elif p >= 0.60 and r["lead_ok"]:
            r["integrated"] = r["now"]
            r["rule"] = "中間(1 段差は現在側に丸める)"
        elif p >= 0.40:
            r["integrated"] = r["now"] + "(上方の留保)"
            r["rule"] = "40〜60%: 上方の留保"
        else:
            r["integrated"] = r["now"]
            r["rule"] = "40% 未満: 現在のまま"
    return dict(P=P, rows=rows, fee26=fee26)


# ---------------------------------------------------------------- 13 条件(第3版)
COND13 = [
    (1, "競争優位", "B", "B", "B(上方の留保)"), (2, "コア事業の CF", "B(C との境界)", "B", "B"), (3, "資産の転用", "B", "B", "B(上方の留保)"),
    (4, "財務の健全性", "S", "S", "S"), (5, "経営者", "B", "B", "B"), (6, "EPS 成長と PEG", "B", "A", "A"),
    (7, "安い理由", "C", "B", "B"), (8, "コモディティでない", "C", "B", "B(上方の留保)"), (9, "停めない運用", "対象外", "対象外", "対象外"),
    (10, "無形資産の陳腐化", "B", "B", "B"), (11, "模倣困難", "B", "B", "B(上方の留保)"), (12, "収益の性格", "B", "B", "B(上方の留保)"),
    (13, "アーキタイプ", "C", "B", "B(上方の留保)"),
]


def run():
    out = {}
    out["kpi"] = kpi_rates()
    out["eps_q"] = eps_quarterly()
    ph = phase()
    out["phase"] = {k: v for k, v in ph.items() if k != "structure"}
    out["structure_base"] = {str(y): v for y, v in ph["structure"].items()}
    out["capital_model"] = capital_model()
    out["rates"] = rates_two_sided()
    out["cond6"] = cond6()

    vm.PEG = dict(g2.PEG_B)
    base = vm.engine()
    ev = vm.engine_value(base)
    eng_mult = {t: ev * (1 + vm.COE) ** (t - 2026 + 0.2) / base[t + 1]["eps"] for t in [2026, 2027, 2028, 2029]}
    paths = {"consensus": vm.CONS, "company": vm.COMP, "engine": vm.eps_of(base)}
    out["values"] = {k: round(vm.fair_path(e, eng_mult)[1], 2) for k, e in paths.items()}
    out["rows_engine"] = [{kk: (round(vv, 3) if isinstance(vv, float) else vv) for kk, vv in r.items()}
                          for r in vm.fair_path(paths["engine"], eng_mult)[0]]

    t = tree_v3(eng_mult)
    out["tree"] = dict(ev=t["ev"], sd=t["sd"], bundles=t["bundles"], p_nodes=t["p_nodes"],
                       combos=[dict(state="".join("○" if c["state"][k] else "×" for k in ["N1", "N2", "N3", "N4"]), p=c["p"], value=c["value"],
                                    eps2028=c["eps2028"], rotce2028=c["rotce2028"], fee2028=c["fee2028"]) for c in t["combos"]])
    out["nodes_v3"] = NODES_V3
    b = t["bundles"]
    pb = b["bear"]["p"]
    out["implied_bull_p"] = (vm.PRICE - pb * b["bear"]["value"] - (1 - pb) * b["base"]["value"]) / (b["bull"]["value"] - b["base"]["value"])
    # 感応度(N1・N2 ±10pt)
    sens = []
    for d1 in (-0.10, 0.0, 0.10):
        row = []
        for d2 in (-0.10, 0.0, 0.10):
            c = {("N1", "N3"): (0.65 + d1, 0.48 + d1), ("N2", "N3"): (0.55 + d2, 0.30 + d2)}
            tt = tree_v3(eng_mult, cond=c)
            row.append(dict(ev=tt["ev"], p_bull=tt["bundles"]["bull"]["p"]))
        sens.append(dict(dN1=d1, row=row))
    out["tree_sens"] = sens
    out["two_layer"] = two_layer(t, ph["structure"])
    out["cond13"] = [dict(c=c, name=n, v2=a, now=b_, integrated=i) for c, n, a, b_, i in COND13]

    # 金利 ±100bp のシナリオ(エンジンに入れた場合): NIM を 1 年目に会社の表の分だけ動かし、信用 +10bp、評価減(純額)、株主資本コスト
    r = out["rates"]
    nim_d1 = r["nii_company"] / base[2027]["iea_avg"]
    up = vm.engine(nim=[0.0600, 0.0585 + nim_d1, 0.0575 + nim_d1 / 2, 0.0565, 0.0560], credit_shock=0.0010)
    coe0 = vm.COE
    vm.COE, vm.FLOOR = coe0 + 0.01, 1 / (coe0 + 0.01)
    ev_up = vm.engine_value(base)
    em_up = {tt: ev_up * (1 + vm.COE) ** (tt - 2026 + 0.2) / base[tt + 1]["eps"] for tt in [2026, 2027, 2028, 2029]}
    v_up = vm.fair_path(vm.eps_of(up), em_up)[1] + r["mark_net"]["mid"] * 0.78 / 1.396e9
    vm.COE, vm.FLOOR = coe0, 1 / coe0
    out["rate_scenario"] = dict(base=out["values"]["engine"], up100=v_up, delta=v_up - out["values"]["engine"])

    # エントリー(構造 B: α 22.5%。第2版と同じ表)
    a = 0.225
    B = out["values"]["engine"]
    L, U = b["bear"]["value"], b["bull"]["value"]
    out["entry"] = dict(alpha=a, B=B, U=U, L=L, Z1=min(B * (1 - a), L * (1 + a / 2)), Z2=B * (1 - a / 2),
                        up_down=(U - vm.PRICE) / (vm.PRICE - L))
    out["gap"] = dict(engine=B / vm.PRICE - 1, ev=t["ev"] / vm.PRICE - 1)
    with open(os.path.join(OUT, "growth_v3.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, default=float)
    return out


if __name__ == "__main__":
    o = run()
    k = o["kpi"]
    for r in k["rows"]:
        print(f"{r['q']}: mem {r['mem']} qoq {r['mem_qoq']*100:.1f}% (ann {r['mem_qoq_ann']*100:.1f}) yoy {r['mem_yoy']*100:.1f}% netYoY {r['net_mem_yoy']*100:.0f}% | "
              f"prod qoq {r['prod_qoq']*100:.1f} yoy {r['prod_yoy']*100:.1f} netYoY {r['net_prod_yoy']*100:.0f} ppm {r['ppm']:.2f} | dep yoy {r['dep_yoy'] and round(r['dep_yoy']*100,1)} | rev yoy {r.get('rev_yoy') and round(r['rev_yoy']*100,1)}")
    print("words", k["words"]); print("seg", {kk: (round(v, 3) if isinstance(v, float) else v) for kk, v in k["seg"].items()})
    e = o["eps_q"]
    for r in e["rows"]:
        print(f"{r['q']}: rev {r['rev']:.0f} pretax {r['pretax']:.0f} m {r['pretax_margin']*100:.1f}% tax {r['tax_rate']*100:.1f}% sh {r['shares']:.0f} eps {r['eps']:.4f} ptps {r['pretax_ps']:.4f}")
    print("yoy", {kk: round(v, 4) for kk, v in e["yoy"].items()}); print("qoq", {kk: round(v, 4) for kk, v in e["qoq"].items()})
    print("h2", {kk: round(v, 3) for kk, v in e["h2"].items()}, "taxstep", e["tax_step"], "dil", e["dilution"])
    print("phase", o["phase"]["company"], o["phase"]["transition"])
    for y, s in o["structure_base"].items():
        print(y, {kk: (round(v, 3) if isinstance(v, float) else v) for kk, v in s.items()})
    cm = o["capital_model"]; print("cap model spread", round(cm["spread"], 4), "roe_hold", round(cm["roe_hold"], 3), "loss_be", round(cm["loss_breakeven"], 4))
    r = o["rates"]
    print("rates yr1", {kk: round(v / 1e6) for kk, v in r["yr1"].items()}, "yr3", {kk: round(v / 1e6) for kk, v in r["yr3"].items()})
    print("rates per share", {kk: (round(v, 3) if isinstance(v, float) else {a: round(b, 3) for a, b in v.items()}) for kk, v in r["per_share"].items()})
    print("market", r["market"], "econ_ytd", round(r["econ_ytd"], 2), "deposit", r["deposit"])
    c6 = o["cond6"]
    print("cond6 ntm pe", round(c6["ntm_pe"], 2), "gp med", c6["growth_peer_median"], "wide med", c6["wide_median"])
    for row in c6["rows"]:
        print("  ", {kk: (round(v, 3) if isinstance(v, float) else v) for kk, v in row.items()})
    print("n_market", c6["n_market"], "n_strict", c6["n_strict"], "n_err", c6["n_within_err"])
    print("values", o["values"]); print("tree ev", round(o["tree"]["ev"], 2), "sd", round(o["tree"]["sd"], 2), "pn", {kk: round(v, 3) for kk, v in o["tree"]["p_nodes"].items()})
    print("bundles", {kk: {a: round(b, 3) for a, b in v.items()} for kk, v in o["tree"]["bundles"].items()})
    print("implied bull", round(o["implied_bull_p"], 3))
    for s in o["tree_sens"]:
        print("  sens", s["dN1"], [(round(x["ev"], 2), round(x["p_bull"], 3)) for x in s["row"]])
    tl = o["two_layer"]; print("two-layer P", {kk: round(v, 3) for kk, v in tl["P"].items()}, "fee26", round(tl["fee26"], 3))
    for row in tl["rows"]:
        print("  ", row["c"], row["now"], row["fut"], round(row["P"], 3), row["integrated"], row["rule"])
    print("rate scenario", {kk: round(v, 2) for kk, v in o["rate_scenario"].items()})
    print("entry", {kk: round(v, 2) for kk, v in o["entry"].items()}, "gap", {kk: round(v, 3) for kk, v in o["gap"].items()})
    for c in o["tree"]["combos"]:
        print("  ", c["state"], round(c["p"], 3), round(c["value"], 2), round(c["eps2028"], 3), round(c["rotce2028"], 3), round(c["fee2028"], 3))
