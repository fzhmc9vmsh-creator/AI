"""共通バリュエーション関数(6社で同じ計算規約を使うための共有ライブラリ)。

規約の出所: 00_standard.md §3〜§4、valuation-model.md §3〜§4、scenario-strategy.md §6。
会計年度は「期末日」で識別する(例: PANW FY2027 = date(2027, 7, 31))。
"""
from __future__ import annotations

import datetime as dt
import math

VALUATION_DATE = dt.date(2026, 10, 11)
TARGET_DATE = dt.date(2027, 10, 11)  # 12か月目標株価の評価時点
COST_OF_CAPITAL = 0.09
G_CAP = 0.50  # g が 50% を超える年度は頭打ち(valuation-model.md §3-4)

RATING_ORDER = ["S", "A", "B", "C", "D", "E", "F"]
ALPHA_BY_RATING = {"S": (0.10, 0.15), "A": (0.15, 0.20), "B": (0.20, 0.25), "C": (0.25, 0.35)}
PEG_START_BY_RATING = {"S": (1.6, 2.0), "A": (1.3, 1.6), "B": (1.0, 1.3), "C": (0.8, 1.0)}


def _month_index(d: dt.date) -> int:
    return d.year * 12 + (d.month - 1)


def fy_months(fy_end: dt.date) -> range:
    """会計年度がカバーする12か月の月インデックス。"""
    end = _month_index(fy_end)
    return range(end - 11, end + 1)


def ntm_eps(eps_by_fy_end: dict[dt.date, float], start: dt.date = TARGET_DATE, months: int = 12) -> float:
    """start の月から先 months か月の EPS を、会計年度EPSの月数按分で求める。

    各月に「その月を含む会計年度の EPS / 12」を割り当てて合計する。季節性は無視する。
    必要な年度が欠けていれば ValueError。
    """
    s = _month_index(start)
    total = 0.0
    for m in range(s, s + months):
        fy = next((fe for fe in eps_by_fy_end if m in fy_months(fe)), None)
        if fy is None:
            y, mo = divmod(m, 12)
            raise ValueError(f"{y}-{mo + 1:02d} を含む会計年度の EPS がない")
        total += eps_by_fy_end[fy] / 12.0
    return total


def cagr(v0: float, v1: float, years: float) -> float:
    if v0 <= 0 or v1 <= 0:
        raise ValueError("CAGR は正の値どうしでのみ計算する(赤字年度は別途扱う)")
    return (v1 / v0) ** (1.0 / years) - 1.0


def fair_per(peg: float, g: float, cap: float = G_CAP) -> dict:
    """妥当PER = PEG × g×100。頭打ちあり・なしの両方を返す。"""
    return {"capped": peg * min(g, cap) * 100.0, "uncapped": peg * g * 100.0, "g_capped": min(g, cap)}


def peg_of(price: float, eps: float, g: float) -> float:
    """現在の PEG = (株価 ÷ EPS) ÷ (g×100)。"""
    return (price / eps) / (g * 100.0)


def target_price(ntm: float, peg: float, g: float, cap: float = G_CAP) -> dict:
    fp = fair_per(peg, g, cap)
    return {"per": fp["capped"], "price": fp["capped"] * ntm,
            "per_uncapped": fp["uncapped"], "price_uncapped": fp["uncapped"] * ntm}


def gap(target: float, price: float) -> float:
    return (target - price) / price


def zones(B: float, U: float, L: float, alpha: float, price: float, edge: bool = True) -> dict:
    """エントリー価格帯(scenario-strategy.md §6【再設計】)。"""
    z1 = min(B * (1 - alpha), L * (1 + alpha / 2))
    z2 = B * (1 - alpha / 2)
    if not edge:
        z1 = None  # 市場との差分がない場合は即エントリー圏を設けない
    if z1 is not None and price <= z1:
        zone = "即エントリー圏"
        if price > L and (U - price) / (price - L) < 2:
            zone = "分割エントリー圏(上値/下値比<2の補助条件)"
    elif price <= z2:
        zone = "分割エントリー圏"
    else:
        zone = "見送り圏"
    updown = (U - price) / (price - L) if price > L else math.inf
    return {"Z1": z1, "Z2": z2, "zone": zone, "upside_downside_ratio": updown,
            "L_above_price": L >= price}


def decision(rating: str, gap_value: float, edge: bool) -> str:
    """2軸マトリクス(valuation-model.md §4-1【再設計】)。エッジなしは「買い検討」が上限。"""
    r = rating[0]
    if r in ("D", "E", "F"):
        return "見送り"
    if gap_value >= 0.30:
        col = 0
    elif gap_value >= 0.10:
        col = 1
    elif gap_value >= -0.10:
        col = 2
    else:
        col = 3
    table = {
        "S": ["買い", "買い", "買い検討", "監視"],
        "A": ["買い", "買い", "買い検討", "監視"],
        "B": ["買い", "買い検討", "監視", "見送り"],
        "C": ["買い検討", "監視", "監視", "見送り"],
    }
    d = table[r][col]
    if not edge and d == "買い":
        d = "買い検討"
    return d


def expected_value(prices: dict[str, float], probs: dict[str, float], price: float) -> dict:
    s = sum(probs.values())
    if abs(s - 1.0) > 1e-6:
        raise ValueError(f"確率の合計が1でない: {s}")
    ev = sum(prices[k] * probs[k] for k in probs)
    return {"expected_price": ev, "expected_return": ev / price - 1.0}


def steady_state_split(steady_earnings_total: float, market_cap: float, r: float = COST_OF_CAPITAL) -> dict:
    """時価総額を定常状態価値と成長の値段に分ける(valuation-model.md §3-5)。"""
    ssv = steady_earnings_total / r
    return {"steady_state_value": ssv, "growth_price": market_cap - ssv,
            "growth_share_of_mcap": (market_cap - ssv) / market_cap}


def eps_log_decomposition(rev0, rev1, npm0, npm1, sh0, sh1) -> dict:
    """ln(EPS1/EPS0) = ln(売上比) + ln(純利益率比) − ln(株数比)(valuation-model.md §3-0)。"""
    a, b, c = math.log(rev1 / rev0), math.log(npm1 / npm0), -math.log(sh1 / sh0)
    return {"revenue": a, "margin": b, "dilution": c, "total": a + b + c}


def business_eps(adj_eps: float, sbc: float, diluted_shares: float, tax: float = 0.22) -> float:
    """事業実態EPS = 調整後EPS − SBC×(1−t)÷希薄化後株数(00_standard.md §3)。"""
    return adj_eps - sbc * (1 - tax) / diluted_shares


if __name__ == "__main__":
    # 自己テスト
    eps = {dt.date(2027, 7, 31): 3.0, dt.date(2028, 7, 31): 3.6, dt.date(2029, 7, 31): 4.3}
    v = ntm_eps(eps)  # 2027-10〜2028-09: FY28 が10か月、FY29 が2か月
    assert abs(v - (3.6 * 10 + 4.3 * 2) / 12) < 1e-9, v
    eps_jan = {dt.date(2028, 1, 31): 6.0, dt.date(2029, 1, 31): 7.5}
    v2 = ntm_eps(eps_jan)  # 2027-10〜2028-01 が FY28(4か月)、2028-02〜09 が FY29(8か月)
    assert abs(v2 - (6.0 * 4 + 7.5 * 8) / 12) < 1e-9, v2
    assert decision("A", 0.35, edge=False) == "買い検討"
    assert decision("B", 0.05, edge=True) == "監視"
    z = zones(B=100, U=140, L=70, alpha=0.2, price=75)
    assert z["zone"].startswith("即エントリー圏") or z["zone"].startswith("分割"), z
    print("valuation_lib self-test OK")
