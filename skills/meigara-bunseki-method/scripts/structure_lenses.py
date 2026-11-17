#!/usr/bin/env python3
"""単位のレンズ(銘柄分析メソッド 工程 2A。references/structure-anatomy.md・insight-patterns.md)。

使い方:
    python3 structure_lenses.py <作業フォルダ>     # units.json を読み、structure_lenses.json と structure_lenses.md を出す

lenses.py は損益計算書の水準(全社・セグメント)を見る。このスクリプトは、その 1 段下の「原子単位」(顧客・事業所・店・契約)の
数と、単位あたりの売上と、業界の流量から、開示のままでは見えない構造の量を出す。入力が足りないレンズは「入力不足」と出して止まらない。

U01 流量と定常の規模   定常の単位数 = 年間の流入 ÷ 流出率。経営陣の長期目標に要る流入は今の何倍か(型 P4)
U02 流入と保有のシェア 流入のシェア(切替を除く幅)・保有のシェア・定常のシェア(型 P5)
U03 顧客の死亡率       自社の顧客の廃業率と、業界の廃止率(型 P6)
U04 増収の分解         単位数の増加と、単位あたりの増加(型 P8)
U05 単位あたりの製品別 製品ごとの単位あたり売上の変化。本体が動いているか(型 P7・P8)
U06 顧客の財布         払う額の売上比・利益比、取り分の梯子と顧客の利益率、効果の外形(型 P1・P2・P10)
U07 新製品の限界採算   増えた売上と、同じ期間に増えた原価(型 P9)
U08 獲得の採算         回収月数と LTV/CAC を、流出率 3 通りで(型 P15)
U09 定常の利益         成長のための支出を除いた利益率、直近と過去の限界利益率(型 P14)
標準ライブラリだけで動く。"""
import json
import os
import sys


def num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def r(x, nd=1):
    return None if x is None else round(x, nd)


def lens(lid, name):
    return dict(id=lid, name=name, status="ok", lines=[], values={}, flags=[])


def short(L, missing):
    L["status"] = "入力不足"
    L["lines"].append("不足: " + "、".join(missing))
    return L


def flag(L, n, text, q, check):
    L["flags"].append(dict(id=f"{L['id']}-{n}", flag=text, question=q, check=check))


def annual(rows, key, per_year):
    """直近 1 年分(per_year 期)の合計。足りなければ年換算。"""
    vals = [x.get(key) for x in rows if num(x.get(key))]
    if not vals:
        return None, 0
    take = vals[-per_year:]
    return sum(take) * per_year / len(take), len(take)


def u01(u, ctx):
    L = lens("U01", "流量と定常の規模")
    rows, py = u.get("periods", []), int(u.get("per_year", 4))
    adds, n1 = annual(rows, "adds", py)
    exits, n2 = annual(rows, "exits", py)
    stocks = [x.get("stock_end") for x in rows if num(x.get("stock_end"))]
    if adds is None or exits is None or len(stocks) < 2:
        return short(L, ["periods の adds・exits・stock_end(2 期以上)"])
    cur = stocks[-1]
    base = sum(stocks[-(min(n2, len(stocks) - 1) + 1):-1]) / max(1, min(n2, len(stocks) - 1))
    rate = exits / base
    steady = adds / rate if rate > 0 else None
    ctx.update(adds=adds, exit_rate=rate, steady=steady, cur=cur)
    L["values"] = dict(adds_per_year=r(adds, 0), exit_rate_pct=r(rate * 100, 2), current_stock=cur, steady_state_stock=r(steady, 0))
    L["lines"].append(f"年間の流入 {adds:,.0f}、流出率 {rate*100:.1f}%(年)。定常の単位数 = 流入 ÷ 流出率 = {steady:,.0f}(今 {cur:,.0f} の {steady/cur:.1f} 倍)。")
    for t in (3, 5, 10):
        s = steady - (steady - cur) * (1 - rate) ** t
        L["values"][f"stock_in_{t}y"] = r(s, 0)
    g1 = (steady - (steady - cur) * (1 - rate)) / cur - 1
    s5 = L["values"]["stock_in_5y"]
    s4 = steady - (steady - cur) * (1 - rate) ** 4
    g5 = s5 / s4 - 1
    L["values"].update(growth_next_year_pct=r(g1 * 100), growth_year5_pct=r(g5 * 100))
    L["lines"].append(f"流量が一定なら、単位数の伸びは来年 {g1*100:.1f}% → 5 年目 {g5*100:.1f}% に自動で下がる(失速ではなく算術)。5 年後 {s5:,.0f}、10 年後 {L['values']['stock_in_10y']:,.0f}。")
    tg = u.get("target") or {}
    if num(tg.get("stock")):
        t = (tg["year"] - tg["now_year"]) if num(tg.get("year")) and num(tg.get("now_year")) and tg["year"] > tg["now_year"] else None
        if t:                                    # t 年で目標に届くのに要る、一定の流入
            k = (1 - rate) ** t
            need = rate * (tg["stock"] - cur * k) / (1 - k)
            how = f"{t} 年で届くのに要る流入"
        else:                                    # 目標の規模を保つのに要る流入
            need, how = tg["stock"] * rate, "保つのに要る流入"
        mult = need / adds
        L["values"].update(target_stock=tg["stock"], target_needs_adds=r(need, 0), target_adds_multiple=r(mult, 2))
        L["lines"].append(f"経営陣の目標「{tg.get('what', '')}」({tg['stock']:,.0f})に{how}は年 {need:,.0f} = 今の {mult:.1f} 倍。")
        if mult > 1.5:
            flag(L, 1, f"長期目標に要る流入が今の {mult:.1f} 倍", "何が流入を増やすのか(製品・価格・販路・制度)。その証拠は今の四半期の数字に出ているか",
                 "四半期の新規の単位数の前年同期比、業界の流入、経営陣の説明")
    if steady / cur < 1.5:
        flag(L, 2, f"定常の規模が今の {steady/cur:.1f} 倍しかない", "単位数の成長はあと何年で止まるか。以後の成長は単位あたりだけになる", "流入と流出率の推移")
    return L


def u02(u, ctx):
    L = lens("U02", "流入のシェアと保有のシェア")
    ind = u.get("industry") or {}
    if not ctx.get("adds") or not all(num(ind.get(k)) for k in ("stock", "adds", "exits")):
        return short(L, ["U01 の入力", "industry の stock・adds・exits"])
    prev = ind.get("prev_stock") if num(ind.get("prev_stock")) else ind["stock"]
    ind_rate = ind["exits"] / prev
    in_hi = ctx["adds"] / ind["adds"]
    sw = ind.get("switch_in_share_of_adds_pct")
    sw_lo, sw_hi = ind.get("switch_in_share_of_adds_pct_lo"), ind.get("switch_in_share_of_adds_pct_hi")
    if not num(sw) and num(sw_lo) and num(sw_hi):
        sw = (sw_lo + sw_hi) / 2
    in_lo = in_hi * (1 - sw / 100) if num(sw) else None
    if num(sw_lo) and num(sw_hi):
        L["values"]["inflow_share_ex_switch_range_pct"] = [r(in_hi * (1 - sw_hi / 100) * 100), r(in_hi * (1 - sw_lo / 100) * 100)]
        L["values"]["steady_state_share_ex_switch_range_pct"] = [r(in_hi * (1 - sw_hi / 100) * ind["exits"] / prev / ctx["exit_rate"] * 100),
                                                                 r(in_hi * (1 - sw_lo / 100) * ind["exits"] / prev / ctx["exit_rate"] * 100)]
    stock_share = ctx["cur"] / ind["stock"]
    ss_share = in_hi * ind_rate / ctx["exit_rate"]
    ctx.update(ind_rate=ind_rate)
    rg = L["values"].get("inflow_share_ex_switch_range_pct")
    _keep = dict(L["values"])
    L["values"] = dict(inflow_share_pct=r(in_hi * 100), inflow_share_ex_switch_pct=r(in_lo * 100) if in_lo else None,
                       stock_share_pct=r(stock_share * 100), steady_state_share_pct=r(ss_share * 100), industry_exit_rate_pct=r(ind_rate * 100, 2),
                       industry_steady_stock=r(ind["adds"] / ind_rate, 0))
    L["values"].update(_keep)
    L["lines"].append(f"流入のシェア {in_hi*100:.1f}%" + (f"(他社からの切替を除くと {in_lo*100:.1f}%)" if in_lo else "(他社からの切替を含む上限。切替の割合が不明)")
                      + f"、保有のシェア {stock_share*100:.1f}%。")
    L["lines"].append(f"定常のシェア = 流入のシェア × 業界の流出率 {ind_rate*100:.1f}% ÷ 自社の流出率 {ctx['exit_rate']*100:.1f}% = {ss_share*100:.1f}%。")
    if rg:
        sr = L["values"]["steady_state_share_ex_switch_range_pct"]
        L["lines"].append(f"他社からの切替(新規の {sw_lo}〜{sw_hi}%)を除くと、新規開設の取り分は {rg[0]}〜{rg[1]}%、それだけで決まる定常のシェアは {sr[0]}〜{sr[1]}%"
                          "(切替の波が止まった場合の水準)。")
    if in_lo is not None and in_lo <= stock_share * 1.05:
        flag(L, 1, f"切替を除く流入のシェア {in_lo*100:.1f}% が保有のシェア {stock_share*100:.1f}% と変わらない", "新しい顧客が選ぶ場面では、もう優位が無いのではないか。シェアの上昇は他社からの切替だけに頼っていないか",
             "新規のうち新設と切替の内訳、切替の流入の推移")
    if in_lo is None:
        flag(L, 2, "流入のシェアの内訳(新設と他社からの切替)が不明", "切替を除いた流入のシェアは保有のシェアを上回るか", "会社の説明・質疑、競合の解約")
    return L


def u03(u, ctx):
    L = lens("U03", "顧客の死亡率")
    rows, py = u.get("periods", []), int(u.get("per_year", 4))
    death, n = annual(rows, "exits_death", py)
    sw, _ = annual(rows, "exits_switch", py)
    ex, _ = annual(rows, "exits", py)
    if death is None and sw is not None and ex is not None:
        death = ex - sw
    if death is None or not ctx.get("cur") or not ctx.get("ind_rate"):
        return short(L, ["periods の exits_death(か exits と exits_switch)", "U02 の入力"])
    stocks = [x.get("stock_end") for x in rows if num(x.get("stock_end"))]
    base = sum(stocks[-(py + 1):-1]) / max(1, len(stocks[-(py + 1):-1])) if len(stocks) > 1 else ctx["cur"]
    own = death / base
    ratio = own / ctx["ind_rate"]
    L["values"] = dict(own_death_rate_pct=r(own * 100, 2), industry_exit_rate_pct=r(ctx["ind_rate"] * 100, 2), ratio=r(ratio, 2),
                       switch_rate_pct=r(sw / base * 100, 2) if sw is not None else None)
    L["lines"].append(f"自社の顧客の廃業・休止による流出 {own*100:.1f}%(年)に対し、業界の廃止率 {ctx['ind_rate']*100:.1f}%。比は {ratio:.2f}。")
    ctx.update(own_death=own)
    if ratio <= 0.7:
        flag(L, 1, f"自社の顧客は業界の {ratio:.0%} しか廃業しない", "選別(良い顧客が選ぶ)か、効果(製品が存続を助ける)か。顧客の年齢・規模の構成をそろえても差は残るか",
             "顧客の規模・設立年の構成、利用の前後の比較、業界の年齢別の廃止率")
    elif ratio >= 1.2:
        flag(L, 1, f"自社の顧客は業界の {ratio:.1f} 倍廃業する", "弱い顧客(新設・小規模)を集めていないか", "顧客の年齢の構成")
    return L


def per_unit(rows, key_fn, py):
    """各期の 単位あたり・月額(千単位)= その期の売上 ÷ 期の平均単位数 ÷ 期の月数。"""
    out = []
    months = 12 / py
    for i in range(1, len(rows)):
        a = rows[i - 1].get("active_end") if num(rows[i - 1].get("active_end")) else rows[i - 1].get("stock_end")
        b = rows[i].get("active_end") if num(rows[i].get("active_end")) else rows[i].get("stock_end")
        v = key_fn(rows[i])
        out.append((rows[i].get("p"), (v / ((a + b) / 2) / months * 1000) if num(a) and num(b) and num(v) else None))
    return out


def u04(u, ctx):
    L = lens("U04", "増収の分解(単位数と単位あたり)")
    rows, py = u.get("periods", []), int(u.get("per_year", 4))
    rv = [(x.get("p"), x.get("revenue_recurring"), x.get("stock_end")) for x in rows]
    if len(rows) < py + 2 or not all(num(x[1]) and num(x[2]) for x in rv[-(py + 1):]) or not num(rv[-(py + 2)][2]):
        return short(L, [f"periods {py + 2} 期以上の revenue_recurring・stock_end"])
    pu = per_unit(rows, lambda x: x.get("revenue_recurring"), py)
    now, prev = pu[-1][1], pu[-1 - py][1]
    act = [x.get("active_end") if num(x.get("active_end")) else x.get("stock_end") for x in rows]
    avg_now = (act[-1] + act[-2]) / 2
    avg_prev = (act[-1 - py] + act[-2 - py]) / 2
    d_rev = rv[-1][1] - rv[-1 - py][1]
    months = 12 / py
    by_units = (avg_now - avg_prev) * prev * months / 1000
    by_unit_rev = avg_now * (now - prev) * months / 1000
    L["values"] = dict(period=rv[-1][0], revenue_change=r(d_rev), by_units=r(by_units), by_unit_revenue=r(by_unit_rev),
                       unit_revenue_now=r(now), unit_revenue_prev=r(prev), units_growth_pct=r((avg_now / avg_prev - 1) * 100),
                       unit_revenue_growth_pct=r((now / prev - 1) * 100))
    share = by_units / d_rev * 100 if d_rev else 0
    L["lines"].append(f"{rv[-1][0]} の増収 {d_rev:+,.1f} のうち、単位数の増加 {by_units:+,.1f}({share:.0f}%)、単位あたりの増加 {by_unit_rev:+,.1f}。"
                      f"単位数 {(avg_now/avg_prev-1)*100:+.1f}%、単位あたり {(now/prev-1)*100:+.1f}%(月 {prev:,.1f} → {now:,.1f} 千)。")
    ctx.update(unit_now=now, unit_prev=prev)
    if share >= 60:
        flag(L, 1, f"増収の {share:.0f}% は単位数の増加", "単位数は流量(U01)で決まる。流入が一定なら、この増収の源は毎年小さくなる", "U01 の定常の規模と伸び率の経路")
    return L


def u05(u, ctx):
    L = lens("U05", "単位あたりの製品別")
    rows, py = u.get("periods", []), int(u.get("per_year", 4))
    names = []
    for x in rows:
        for k in (x.get("products") or {}):
            if k not in names:
                names.append(k)
    if not names or len(rows) < py + 2:
        return short(L, [f"periods {py + 2} 期以上の products"])
    res, tot = [], 0.0
    for nme in names:
        pu = per_unit(rows, lambda x, nme=nme: (x.get("products") or {}).get(nme), py)
        a, b = pu[-1][1], pu[-1 - py][1]
        if a is None:
            continue
        b = b or 0.0
        res.append((nme, b, a, a - b))
        tot += a - b
    if not res:
        return short(L, ["products の値"])
    res.sort(key=lambda t: -abs(t[3]))
    L["values"] = dict(products=[dict(name=n_, prev=r(b, 2), now=r(a, 2), change=r(d, 2), share_of_change_pct=r(d / tot * 100) if tot else None) for n_, b, a, d in res],
                       total_change=r(tot, 2))
    L["lines"].append("単位あたり月額の前年同期からの変化(千): " + "、".join(f"{n_} {b:,.1f}→{a:,.1f}({d:+.1f})" for n_, b, a, d in res) + f"。合計 {tot:+.1f}。")
    core = max(res, key=lambda t: t[2])
    if tot > 0 and abs(core[3]) < 0.15 * tot and core[1] > 0 and abs(core[3] / core[1]) < 0.02:
        flag(L, 1, f"最大の製品「{core[0]}」の単位あたりは {core[1]:,.1f}→{core[2]:,.1f} で横ばい。伸びは他の製品",
             "本体の性質(従量・値上げ・利用の拡大)は、既存の単位では働いていないのではないか。群(規模・年齢)に分けると、伸びる群と薄める群の相殺か",
             "区分別の単位あたり売上、継続率(群別)、新規の初期単価")
    top = [t for t in res if t[3] > 0][:2]
    if tot > 0 and top and sum(t[3] for t in top) / tot >= 0.7:
        flag(L, 2, f"単位あたりの伸びの {sum(t[3] for t in top)/tot:.0%} は「{'・'.join(t[0] for t in top)}」", "その製品の限界採算はプラスか(U07)。付帯率の上限はどこか",
             "付帯率の推移、製品別の原価")
    return L


def u06(u, ctx):
    L = lens("U06", "顧客の財布(払う額・取り分の梯子・効果の外形)")
    c = u.get("customer") or {}
    rev, mg, paid = c.get("revenue_per_unit_month"), c.get("profit_margin_pct"), c.get("price_paid_month")
    if not (num(rev) and num(mg) and num(paid)):
        return short(L, ["customer の revenue_per_unit_month・profit_margin_pct・price_paid_month"])
    profit = rev * mg / 100
    L["values"] = dict(customer_profit_month=r(profit), paid_pct_of_revenue=r(paid / rev * 100, 2), paid_pct_of_profit=r(paid / profit * 100))
    L["lines"].append(f"顧客 1 単位の売上 {rev:,.0f}・利益 {profit:,.0f}(利益率 {mg}%)。払う額 {paid:,.0f} は売上の {paid/rev*100:.1f}%、利益の {paid/profit*100:.0f}%。")
    if paid / rev < 0.03 and paid / profit >= 0.10:
        flag(L, 1, f"売上比 {paid/rev*100:.1f}% だが利益比 {paid/profit*100:.0f}%", "顧客の採算が悪化したとき、この支払いは削減の対象になるか。値上げの余地を売上比だけで語っていないか",
             "顧客の利益率の分布(赤字の顧客の割合)、解約の理由")
    lad = [x for x in (u.get("ladder") or []) if num(x.get("monthly"))]
    if lad:
        full = sum(x["monthly"] for x in lad)
        repl = sum(x["monthly"] for x in lad if "置き換え" in str(x.get("kind", "")) or "増やす" in str(x.get("kind", "")))
        L["values"].update(full_stack_month=r(full), full_stack_pct_of_revenue=r(full / rev * 100, 1), replacing_part_pct=r(repl / full * 100) if full else None)
        L["lines"].append(f"全製品を入れると {full:,.0f}(売上の {full/rev*100:.1f}%)。顧客の利益率 {mg}% と並べる。うち費用の置き換え・売上を増やす段は {repl:,.0f}。")
        if full / rev * 100 >= mg * 0.8:
            flag(L, 2, f"全部入れた取り分 {full/rev*100:.1f}% が顧客の利益率 {mg}% に並ぶ", "単価の上限は、費用を置き換える段だけにある。どの段が置き換えで、置き換える科目はいくらか",
                 "顧客の費用の内訳(人件費・外注・紹介料)、製品ごとの置き換えの対象")
    own, ind = c.get("own_units_per_customer"), c.get("industry_units_per_customer")
    if num(own) and num(ind):
        L["values"].update(own_units=own, industry_units=ind, units_ratio=r(own / ind, 2))
        L["lines"].append(f"効果の外形: 利用者の{c.get('units_label', '量')} {own:,.0f} に対し業界 {ind:,.0f}(比 {own/ind:.2f})。")
        if own / ind < 1.1:
            flag(L, 3, "会社の主張する量の効果が、利用者の群の数字に現れていない", "価値の正体は何か(手間・誤り・義務への対応)。その正体なら、値上げの根拠と奪われ方はどう変わるか",
                 "利用の前後の比較、規模をそろえた比較、顧客の声")
    return L


def u07(u, ctx):
    L = lens("U07", "新製品の限界採算")
    np_ = [x for x in (u.get("new_products") or []) if num(x.get("inc_revenue")) and num(x.get("inc_cost"))]
    if not np_:
        return short(L, ["new_products の inc_revenue・inc_cost"])
    vals = []
    for x in np_:
        m = x["inc_revenue"] - x["inc_cost"]
        vals.append(dict(name=x.get("name"), period=x.get("period"), inc_revenue=x["inc_revenue"], inc_cost=x["inc_cost"], inc_margin=r(m)))
        L["lines"].append(f"{x.get('name')}({x.get('period', '')}): 増えた売上 {x['inc_revenue']:,.0f}、同じ期間に増えた原価 {x['inc_cost']:,.0f}、差 {m:+,.0f}。")
        if m <= 0:
            flag(L, len(L["flags"]) + 1, f"「{x.get('name')}」は増えた原価が増えた売上以上", "今の値付けでは売るほど粗利が減るのではないか。値上げ・課金の単位・原価の低下のどれで直すのか、日付はいつか",
                 "原価の内訳、単位あたり(1 利用)の売上と原価、値上げ・課金開始の予定")
    L["values"] = dict(items=vals)
    return L


def u08(u, ctx):
    L = lens("U08", "獲得の採算(流出率 3 通り)")
    a = u.get("acquisition") or {}
    need = ("selling_cost_year", "adds_year", "initial_unit_revenue_month", "gross_margin_pct")
    if not all(num(a.get(k)) for k in need):
        return short(L, ["acquisition の " + "・".join(need)])
    unit = u.get("unit", "")
    cac = a["selling_cost_year"] / a["adds_year"] * 1000          # 千
    gp_m = a["initial_unit_revenue_month"] * a["gross_margin_pct"] / 100
    payback = cac / gp_m
    coe = (a.get("coe_pct") or 9.0) / 100
    g = (a.get("unit_growth_pct") or 0.0) / 100
    rates = {}
    if ctx.get("own_death") is not None:
        rates["廃業だけ(下限の流出)"] = ctx["own_death"]
    if ctx.get("exit_rate"):
        rates["自社の実績"] = ctx["exit_rate"]
    if ctx.get("ind_rate"):
        rates["業界の廃止率+自社の切替"] = ctx["ind_rate"] + max(0.0, (ctx.get("exit_rate", 0) - (ctx.get("own_death") or 0)))
    if not rates:
        rates["仮に年 10%"] = 0.10
    L["values"] = dict(cac_thousand=r(cac, 0), payback_months=r(payback), cases=[])
    L["lines"].append(f"獲得費 = 販売の費用 {a['selling_cost_year']:,.0f}({unit})÷ 新規 {a['adds_year']:,.0f} = 1 単位 {cac:,.0f} 千。初期の月の粗利 {gp_m:,.1f} 千で、回収 {payback:.0f} か月。")
    for k, x in rates.items():
        den = coe + x - g
        ltv = gp_m * 12 / den if den > 0 else None
        L["values"]["cases"].append(dict(case=k, exit_rate_pct=r(x * 100), ltv_cac=r(ltv / cac, 1) if ltv else None))
        if ltv:
            L["lines"].append(f"  流出率 {x*100:.1f}%({k}): LTV/CAC {ltv/cac:.1f} 倍。")
    lo = min((c["ltv_cac"] for c in L["values"]["cases"] if c["ltv_cac"]), default=None)
    if lo and lo >= 3:
        flag(L, 1, f"幅の下限でも LTV/CAC {lo:.1f} 倍", "採算は十分なのに、なぜ獲得を増やさない・増やせないのか。律速は自社の外(市場の流入)ではないか",
             "販売の費用を増やした期の新規の単位数、業界の流入")
    elif lo and lo < 1.5:
        flag(L, 1, f"幅の下限で LTV/CAC {lo:.1f} 倍", "獲得の増加は価値を壊していないか", "コホート別の継続と単価")
    return L


def u09(u, ctx):
    L = lens("U09", "定常の利益と限界利益率")
    s = u.get("steady") or {}
    if not all(num(s.get(k)) for k in ("op", "growth_spend", "revenue")):
        return short(L, ["steady の op・growth_spend・revenue"])
    opm = s["op"] / s["revenue"] * 100
    st = (s["op"] + s["growth_spend"]) / s["revenue"] * 100
    L["values"] = dict(op_margin_pct=r(opm), steady_margin_pct=r(st))
    L["lines"].append(f"営業利益率 {opm:.1f}%。成長のための支出 {s['growth_spend']:,.0f} を除くと {st:.1f}%。")
    if num(s.get("inc_op_latest")) and num(s.get("inc_rev_latest")) and s["inc_rev_latest"]:
        im = s["inc_op_latest"] / s["inc_rev_latest"] * 100
        L["values"]["inc_margin_latest_pct"] = r(im)
        past = s.get("inc_margin_past_pct")
        L["lines"].append(f"直近の限界利益率 {im:.1f}%" + (f"(過去 {past}%)。" if num(past) else "。"))
        if num(past) and im < past - 3:
            flag(L, 1, f"限界利益率が {past}% → {im:.1f}% に下がった", "何の費用が増えたのか(原価か販管費か)。構造か一時か。定常の利益率の余地は縮んでいないか",
                 "増えた費用の科目、値上げ・課金開始の予定(U07 と合わせる)")
    if st - opm >= 10:
        flag(L, 2, f"定常の利益率が表面より {st-opm:.0f}pt 高い", "減速の局面で、経営陣は獲得の費用を落として利益率を上げるか。上げた会社の前例は", "中計の利益率の計画、経営陣の発言")
    return L


def main():
    d = sys.argv[1] if len(sys.argv) > 1 else "."
    p = os.path.join(d, "units.json")
    if not os.path.exists(p):
        print("units.json がない(templates/units.json を写して埋める)", file=sys.stderr)
        sys.exit(2)
    u = json.load(open(p, encoding="utf-8"))
    ctx, out = {}, []
    for fn in (u01, u02, u03, u04, u05, u06, u07, u08, u09):
        try:
            out.append(fn(u, ctx))
        except Exception as e:                      # 1 本の失敗で全体を止めない
            L = lens(fn.__name__.upper(), fn.__doc__ or "")
            L["status"] = "計算できず"
            L["lines"].append(f"{type(e).__name__}: {e}")
            out.append(L)
    flags = [f for L in out for f in L["flags"]]
    json.dump(dict(ticker=u.get("ticker"), unit_name=u.get("unit_name"), lenses=out, flags=flags), open(os.path.join(d, "structure_lenses.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    md = [f"# {u.get('ticker', '')} 単位のレンズ(原子単位: {u.get('unit_name', '')})", "",
          f"計算できたレンズ {sum(1 for L in out if L['status'] == 'ok')} / {len(out)}、旗 {len(flags)}", "", "## 旗(示唆の種)", "", "| id | 旗 | 問い | 確かめ方 |", "|---|---|---|---|"]
    md += [f"| {f['id']} | {f['flag']} | {f['question']} | {f['check']} |" for f in flags]
    for L in out:
        md += ["", f"## {L['id']} {L['name']} [{L['status']}]"] + [f"- {x}" for x in L["lines"]]
    open(os.path.join(d, "structure_lenses.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
    for f in flags:
        print(f"{f['id']}: {f['flag']}")
    print(f"計算できたレンズ {sum(1 for L in out if L['status'] == 'ok')} / {len(out)}、旗 {len(flags)} → structure_lenses.md")


if __name__ == "__main__":
    main()
