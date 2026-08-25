# -*- coding: utf-8 -*-
"""
Lemonade (LMND) バリュエーション計算
銘柄分析メソッド Phase 5 / 5.5 / 6 の計算根拠。
すべての入力値は report 内 Appendix B の出所一覧に対応する。
基準日: 2026-08-25
"""

# ---------------- 前提 ----------------
PRICE      = 53.89      # 2026-08-25 終値ベース (USD)
SHARES_OUT = 77.326718  # 百万株, 2026/6/30 発行済
MCAP       = PRICE * SHARES_OUT
EQUITY     = 499.5      # 百万USD, 2026/6/30 株主資本
DISC       = 0.10       # 割引率(ベース)
YEARS_TO_2030 = 4.35    # 2026/8/25 → 2030/12/31

def f(x, n=1): return round(x, n)

print("="*72)
print("0. 現在の価格前提")
print("="*72)
print(f"株価 ${PRICE} / 発行済 {SHARES_OUT}百万株 / 時価総額 ${MCAP/1000:.2f}十億")
print(f"BPS ${EQUITY/SHARES_OUT:.2f} / PBR {PRICE/(EQUITY/SHARES_OUT):.1f}x")
print(f"PSR(FY26E売上1,215) {MCAP/1215:.2f}x / P/IFP(FY26E 1,635) {MCAP/1635:.2f}x")

# ---------------- Q2 2026 実績と営業レバレッジ分解 ----------------
print("\n"+"="*72); print("1. Q2 2026 営業レバレッジ分解 (百万USD)"); print("="*72)
gep_q2, gep_q2_py   = 332.4, 252.3      # 総収入保険料(GEP)
rev_q2, rev_q2_py   = 294.4, 164.1      # 売上
gp_q2,  gp_q2_py    = 113.0, 64.2       # 粗利 (+76%)
ebi_q2, ebi_q2_py   = -19.0, -41.0      # 調整後EBITDA
opex_q2             = 182.0             # 営業費用合計 (+41%)
print(f"GEP     +{gep_q2-gep_q2_py:.1f} (+{(gep_q2/gep_q2_py-1)*100:.0f}%)")
print(f"売上    +{rev_q2-rev_q2_py:.1f} (+{(rev_q2/rev_q2_py-1)*100:.0f}%)  ※出再率低下による見かけの押し上げを含む")
print(f"粗利    +{gp_q2-gp_q2_py:.1f} (+{(gp_q2/gp_q2_py-1)*100:.0f}%)")
print(f"調整後EBITDA +{ebi_q2-ebi_q2_py:.1f}")
print(f"レバレッジ(粗利増/GEP増)        = {(gp_q2-gp_q2_py)/(gep_q2-gep_q2_py)*100:.0f}%")
print(f"レバレッジ(EBITDA増/GEP増)      = {(ebi_q2-ebi_q2_py)/(gep_q2-gep_q2_py)*100:.0f}%")
print(f"レバレッジ(EBITDA増/売上増)     = {(ebi_q2-ebi_q2_py)/(rev_q2-rev_q2_py)*100:.0f}%")

# 過年度発生損害の戻入(PYD)正規化
pyd_pt = 0.07
pyd_amt = gep_q2 * pyd_pt
print(f"\n[正規化] 有利なPYD {pyd_pt*100:.0f}pt = ${pyd_amt:.1f}  → 事故年ベース損害率 67%")
print(f"  正規化粗利 ≈ {gp_q2-pyd_amt:.1f} (粗利率 {(gp_q2-pyd_amt)/rev_q2*100:.0f}%)")
print(f"  正規化調整後EBITDA ≈ {ebi_q2-pyd_amt:.1f}")

# ---------------- 3経路 EPS パス ----------------
print("\n"+"="*72); print("2. 年度別EPSパス (百万USD / 百万株)"); print("="*72)
years = [2026, 2027, 2028, 2029, 2030]

paths = {
 # (IFP期末, 売上, 純利益, 期中平均株式数)
 "コンセンサス経路(ベース)": {
    2026: (1635, 1215, -130, 76.5),
    2027: (2093, 1580,  -53, 79.5),
    2028: (2595, 1975,   59, 82.5),
    2029: (3140, 2385,  155, 85.5),
    2030: (3705, 2815,  255, 88.5)},
 "会社シナリオ経路(強気)": {
    2026: (1639, 1220, -125, 76.5),
    2027: (2163, 1630,  -30, 79.5),
    2028: (2812, 2140,  110, 82.5),
    2029: (3600, 2760,  250, 85.5),
    2030: (4536, 3480,  400, 88.5)},
 "弱気パス": {
    2026: (1620, 1205, -140, 76.5),
    2027: (1976, 1500,  -95, 80.0),
    2028: (2312, 1780,  -40, 84.0),
    2029: (2613, 2020,   20, 88.0),
    2030: (2874, 2240,   80, 92.0)},
}
eps_tbl = {}
for name, d in paths.items():
    print(f"\n--- {name} ---")
    print(f"{'FY':<6}{'IFP':>8}{'IFP成長':>9}{'売上':>8}{'売上成長':>9}{'純利益':>8}{'純利率':>8}{'EPS':>8}")
    prev_ifp = 1240; prev_rev = 737.9
    eps_tbl[name] = {}
    for y in years:
        ifp, rev, ni, sh = d[y]
        eps = ni/sh; eps_tbl[name][y] = eps
        print(f"{y:<6}{ifp:>8}{(ifp/prev_ifp-1)*100:>8.0f}%{rev:>8}{(rev/prev_rev-1)*100:>8.0f}%{ni:>8}{ni/rev*100:>7.1f}%{eps:>8.2f}")
        prev_ifp, prev_rev = ifp, rev

# ---------------- 妥当PEG と 年度別適正株価 ----------------
print("\n"+"="*72); print("3. 妥当PEG → 年度別妥当PER → 適正株価"); print("="*72)
# 正規化成長率 g: 黒字転換直後のEPS成長率は異常値のため、
# 「売上成長率 + マージン拡大寄与」で正規化した持続成長率を使う
g_norm = {2028: 0.20, 2029: 0.21, 2030: 0.22}   # ベース経路
peg    = {2028: (0.90, 1.00), 2029: (1.00, 1.15), 2030: (1.05, 1.25)}

print(f"{'FY':<6}{'EPS':>7}{'正規化g':>9}{'PEG(低-高)':>13}{'PER(低-高)':>14}{'適正株価(低-高)':>20}{'現在価値@10%':>14}")
base = eps_tbl["コンセンサス経路(ベース)"]
disc_yrs = {2028: 2.35, 2029: 3.35, 2030: 4.35}
for y in [2028, 2029, 2030]:
    lo, hi = peg[y]; g = g_norm[y]*100
    per_lo, per_hi = lo*g, hi*g
    p_lo, p_hi = base[y]*per_lo, base[y]*per_hi
    pv_lo, pv_hi = p_lo/(1+DISC)**disc_yrs[y], p_hi/(1+DISC)**disc_yrs[y]
    print(f"{y:<6}{base[y]:>7.2f}{g:>8.0f}%{lo:>7.2f}-{hi:<5.2f}{per_lo:>7.1f}-{per_hi:<6.1f}{p_lo:>11.1f}-{p_hi:<8.1f}{pv_lo:>8.1f}-{pv_hi:<6.1f}")

# ---------------- 目標株価(3シナリオ) ----------------
print("\n"+"="*72); print("4. 目標株価(FY2030適正株価の現在価値, 割引率10%)"); print("="*72)
def target(eps2030, g, pegv, floor_pb=None, bps2030=None):
    per = g*100*pegv
    p30 = eps2030*per
    if floor_pb and bps2030:
        p30 = max(p30, floor_pb*bps2030)
    return p30, p30/(1+DISC)**YEARS_TO_2030

t_base = target(eps_tbl["コンセンサス経路(ベース)"][2030], 0.22, 1.10)
t_bull = target(eps_tbl["会社シナリオ経路(強気)"][2030], 0.26, 1.15)
# 弱気: PEG機械適用(0.90x15%=13.5倍)は黒字企業として過度に低いため、
# PER下限18倍(=低成長黒字保険会社の実勢)とPBR2.0倍のいずれか高い方を下限とする
_p30_bear = max(eps_tbl["弱気パス"][2030]*18.0, 2.0*7.0)
t_bear = (_p30_bear, _p30_bear/(1+DISC)**YEARS_TO_2030)
for nm,(p30,pv) in [("ベース(コンセンサス)",t_base),("強気(会社シナリオ)",t_bull),("弱気",t_bear)]:
    print(f"{nm:<24} FY2030適正株価 ${p30:6.1f} → 現在価値 ${pv:6.1f}  乖離 {(pv/PRICE-1)*100:+6.1f}%")

print("\n[2030年時点のPSR換算クロスチェック]")
for nm,(p30,pv),rev30_,ni30_ in [("ベース",t_base,2815,255),("強気",t_bull,3480,400),("弱気",t_bear,2240,80)]:
    mc = p30*88.5
    print(f"  {nm:<4} 2030時価総額 ${mc/1000:.2f}十億 → PSR {mc/rev30_:.2f}x / PER {mc/ni30_:.1f}x")

w = {"base":0.50, "bull":0.30, "bear":0.20}
wavg = w["base"]*t_base[1] + w["bull"]*t_bull[1] + w["bear"]*t_bear[1]
print(f"\n確率加重(ベース50%/強気30%/弱気20%) = ${wavg:.1f}  乖離 {(wavg/PRICE-1)*100:+.1f}%")
print(f"12ヶ月換算目標(ベース経路 FY2030値を3.35年割引) = ${t_base[0]/(1+DISC)**3.35:.1f}")
print(f"[感応度] 割引率12%の場合のベース現在価値 = ${t_base[0]/(1.12)**YEARS_TO_2030:.1f}")

# ---------------- 逆算:現在株価が織り込む前提 ----------------
print("\n"+"="*72); print("5. 現在株価$53.89が織り込む前提(逆算)"); print("="*72)
req_p30 = PRICE*(1+DISC)**YEARS_TO_2030
for pegv, g in [(1.10, 0.22), (1.20, 0.24)]:
    per = g*100*pegv
    req_eps = req_p30/per
    req_ni  = req_eps*88.5
    print(f"PEG {pegv}, g {g*100:.0f}% (PER {per:.1f}x) → 必要FY2030 EPS ${req_eps:.2f} / 純利益 ${req_ni:.0f}M")
    for rev in [2815, 3480]:
        print(f"    売上${rev}Mなら必要純利率 {req_ni/rev*100:.1f}%")

# ---------------- 感応度マトリクス(F12) ----------------
print("\n"+"="*72); print("6. 感応度マトリクス:FY2030純利率 × 妥当PEG (現在価値, USD)"); print("="*72)
margins = [0.06, 0.08, 0.09, 0.11, 0.13]
pegs    = [0.90, 1.00, 1.10, 1.20, 1.30]
rev30, sh30, g30 = 2815, 88.5, 0.22
hdr = "純利率\\PEG " + "".join(f"{p:>9.2f}" for p in pegs)
print(hdr)
for m in margins:
    eps = rev30*m/sh30
    row = f"{m*100:>7.0f}%   "
    for p in pegs:
        pv = eps*(g30*100*p)/(1+DISC)**YEARS_TO_2030
        mark = "*" if abs(pv-PRICE)/PRICE < 0.10 else " "
        row += f"{pv:>8.1f}{mark}"
    print(row)
print("(* = 現在株価±10%圏)")

# ---------------- エントリー価格帯(3ゾーン) ----------------
print("\n"+"="*72); print("7. エントリー価格帯(3ゾーン)"); print("="*72)
base_t, bull_t, bear_t = t_base[1], t_bull[1], t_bear[1]
alpha = 0.25
z_imm = base_t*(1-alpha)
print(f"即エントリー圏      : ${z_imm:.1f} 以下 (ベース目標 ${base_t:.1f} に対し安全余裕α=25%)")
print(f"分割エントリー圏    : ${z_imm:.1f} 〜 ${base_t:.1f}")
print(f"見送り/様子見圏     : ${base_t:.1f} 超")
print(f"→ 現在株価 ${PRICE} は「見送り/様子見圏」(ベース目標比 {(PRICE/base_t-1)*100:+.0f}%)")
print(f"参考:確率加重目標 ${wavg:.1f} / アナリスト平均目標 $59.56 / 弱気目標 ${bear_t:.1f}")

# ---------------- 資本余力 ----------------
print("\n"+"="*72); print("8. 資本余力チェック(GWP/資本 6:1 基準)"); print("="*72)
for y,(ifp,rev,ni,sh) in paths["コンセンサス経路(ベース)"].items():
    need = ifp/6.0
    print(f"FY{y}: GWP≈IFP ${ifp}M → 必要資本 ${need:.0f}M  (2026/6末 株主資本 ${EQUITY}M, 規制上の必要余剰 $330M)")
