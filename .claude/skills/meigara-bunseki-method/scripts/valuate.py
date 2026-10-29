#!/usr/bin/env python3
"""価値評価の計算機(銘柄分析メソッド valuation-model §3-3〜§4・scenario-strategy §6・growth-stage-evaluation §12)。

使い方:
    python3 valuate.py valuation_input.json            # → valuation.json と valuation.md を同じフォルダに出す
    python3 valuate.py valuation_input.json -o out/    # 出力先を指定

方針: 規則で決まる計算はすべてここで行う。モデルは入力(EPS 経路・条件の評価・株価・シナリオ)を
決めるだけで、PEG・妥当 PER・理論株価・エントリー圏の数字を手で計算しない。資料には
valuation.json の "display"(1 回だけ丸めた表示値)を写す。標準ライブラリだけで動く。
入力の書き方は templates/valuation_input.json、手本は examples/sofi/valuation_input.json。
"""
import argparse
import itertools
import json
import math
import os
import sys

SCORE = {"S": 5, "A": 4, "B": 3, "C": 2, "D": 1, "E": 0, "F": 0}
ORDER = ["S", "A", "B", "C", "D", "E", "F"]
BANDS = {"S": (4.5, 5.0), "A": (3.5, 4.5), "B": (2.5, 3.5), "C": (1.5, 2.5)}
PEG_RANGE = {"S": (1.6, 2.0), "A": (1.3, 1.6), "B": (1.0, 1.3), "C": (0.8, 1.0)}
ALPHA_RANGE = {"S": (0.10, 0.15), "A": (0.15, 0.20), "B": (0.20, 0.25), "C": (0.25, 0.35)}
MATRIX = {  # 構造評価 × 乖離(+30%以上 / +10〜30% / −10〜+10% / −10%未満)  valuation-model §4-1
    "S": ["買い", "買い", "買い検討", "監視"], "A": ["買い", "買い", "買い検討", "監視"],
    "B": ["買い", "買い検討", "監視", "見送り"], "C": ["買い検討", "監視", "監視", "見送り"],
}


class InputError(Exception):
    pass


def need(d, key, where):
    if key not in d:
        raise InputError(f"{where} に '{key}' がありません。templates/valuation_input.json の同じ欄を見て埋めてください。")
    return d[key]


def cagr(a, b, n):
    if a is None or b is None or a <= 0 or b <= 0:
        return None
    return (b / a) ** (1.0 / n) - 1


def rnd(x, nd):
    """表示用の丸め(四捨五入。銀行丸めにしない)。全精度の値から 1 回だけ丸める。"""
    if x is None:
        return "—"
    q = 10 ** nd
    v = math.floor(abs(x) * q + 0.5) / q
    v = -v if x < 0 else v
    return f"{v:.{nd}f}"


def pct(x, nd=1):
    return "—" if x is None else rnd(x * 100, nd) + "%"


# ---------------------------------------------------------------- 構造評価 → 許容 PEG・α(valuation-model §3-3 の 1〜5)
def grade_of(grades, years, decrement):
    """grades: {"1": "B", ..., "9": "N/A"}。対象外(N/A)は除く。等級・平均点・位置・年度別 PEG・α と、発動した規則を返す。"""
    notes = []
    g = {str(k): str(v).strip().upper() for k, v in grades.items()}
    for k, v in g.items():
        if v not in SCORE and v != "N/A":
            raise InputError(f"条件{k} の評価 '{v}' は S・A・B・C・D・E・F・N/A のどれでもありません。")
    # 条件6 と条件7 の対評価: 安い理由の構造が悪い(条件7 が C 以下)なら条件6 の S は無効(A まで)
    if g.get("6") == "S" and g.get("7") in ("C", "D", "E", "F"):
        g["6"] = "A"
        notes.append("条件6・7 の対評価: 条件7 が C 以下のため条件6 の S を A にした")
    used = {k: v for k, v in g.items() if v != "N/A"}
    if len(used) < 8:
        raise InputError(f"評価のある条件が {len(used)} 個しかありません(対象外を除いて 12 個が標準)。")
    vals = list(used.values())
    avg = sum(SCORE[v] for v in vals) / len(vals)
    n_c = sum(1 for v in vals if SCORE[v] <= 2 and v != "F" and v != "E")
    worst = max(vals, key=lambda v: ORDER.index(v))
    dist = {k: sum(1 for v in vals if v == k) for k in ORDER if any(v == k for v in vals)}
    base = dict(avg=avg, n_used=len(vals), distribution=dist, grades_used=used)
    if worst in ("E", "F"):
        notes.append(f"拒否権: {worst} の条件があるため総合は {worst}(許容 PEG を設定しない)")
        return dict(base, letter=worst, pos=None, peg=None, peg_start=None, alpha=None, rules=notes)
    letter = next(k for k, (lo, hi) in BANDS.items() if lo <= avg < hi or (k == "S" and avg >= lo)) if avg >= 1.5 else "D"
    if worst == "D" and ORDER.index(letter) < ORDER.index("D"):
        notes.append("拒否権: D の条件があるため総合は D を上限とする")
        letter = "D"
    if n_c >= 4 and ORDER.index(letter) < ORDER.index("C"):
        notes.append(f"C 以下が {n_c} 条件(4 以上)のため総合は C を上限とする")
        letter = "C"
    if letter == "D":
        return dict(base, letter="D", pos=None, peg=None, peg_start=None, alpha=None, rules=notes + ["D 以下は許容 PEG を設定しない(買いの対象外)"])
    lo, hi = BANDS[letter]
    pos_raw = (avg - lo) / (hi - lo)
    pos = min(max(pos_raw, 0.0), 1.0)
    if pos_raw > 1.0:
        notes.append("規則で等級が下がったため、帯の上端(位置 1.0)に収めた")
    p_lo, p_hi = PEG_RANGE[letter]
    a_lo, a_hi = ALPHA_RANGE[letter]
    start = p_lo + pos * (p_hi - p_lo)
    peg = {str(y): start - decrement * i for i, y in enumerate(years)}
    if not notes:
        notes.append("拒否権・C×4・条件6/7 の規則はいずれも発動せず")
    return dict(base, letter=letter, pos=pos, peg=peg, peg_start=start, alpha=a_hi - pos * (a_hi - a_lo), rules=notes)


# ---------------------------------------------------------------- EPS 経路の延長と年度別の理論株価(§3-4・第5.2版)
def extend(eps, last_needed, decel, g_long):
    """入力の最終年度より先は、最後の 1 年の伸びを毎年 decel ずつ減速させて延長する(下限 g_long)。"""
    e = {int(k): float(v) for k, v in eps.items()}
    ys = sorted(e)
    if len(ys) < 2:
        raise InputError("EPS 経路は 2 年度以上必要です。")
    for y in range(ys[0], ys[-1] + 1):
        if y not in e:
            raise InputError(f"EPS 経路の {y} 年度が抜けています(途中の年度を飛ばさない)。")
    g = e[ys[-1]] / e[ys[-2]] - 1
    ext = []
    for y in range(ys[-1] + 1, last_needed + 1):
        g = max(g - decel, g_long)
        e[y] = e[y - 1] * (1 + g)
        ext.append(y)
    return e, ext


def fair_path(eps, peg, cfg):
    years, w, surv, coe = cfg["years"], cfg["weights"], cfg["survival"], cfg["coe"]
    mat, gcap, decel, g_long = cfg["maturity"], cfg["g_cap"], cfg["extend_decel"], cfg["maturity"]["g_long"]
    e, ext = extend(eps, years[-1] + 5, decel, g_long)
    base_year = years[0]
    rows = []
    for t in years:
        if t not in e or e[t] <= 0:
            raise InputError(f"{t} 年度の EPS が無いか 0 以下です。PEG × g は使えません(赤字の年度は理論式か別の方法)。")
        g = cagr(e[t], e[t + 3], 3)
        g5 = cagr(e[t], e[t + 5], 5)
        flag = None
        if g5 is not None and g5 < mat["g5_threshold"]:
            per = (1 - mat["g_long"] / mat["roe"]) / (coe - mat["g_long"])
            method = "理論式(成熟)"
            g_used = g
        else:
            g_used = g
            if g is not None and g > gcap:
                g_used = gcap
                flag = f"g {pct(g)} が上限 {pct(gcap, 0)} を超えたため上限で計算(頭打ちなしの値も併記)"
            per = peg[str(t)] * g_used * 100
            method = "PEG×g"
        price = per * e[t]
        pv = price / (1 + coe) ** (t - base_year) * surv
        row = dict(year=t, eps=e[t], g=g, g5=g5, g_used=g_used, peg=peg[str(t)], per=per, method=method, price=price, pv=pv,
                   eps_extended=t in ext)
        if flag:
            row["note"] = flag
            row["price_uncapped"] = peg[str(t)] * g * 100 * e[t]
        rows.append(row)
    value = sum(r["pv"] * wi for r, wi in zip(rows, w))
    return rows, value, ext


def gap_bucket(gap):
    return 0 if gap >= 0.30 else 1 if gap >= 0.10 else 2 if gap >= -0.10 else 3


def decide(letter, gap, edge):
    if letter not in MATRIX:
        return "見送り"
    d = MATRIX[letter][gap_bucket(gap)]
    if not edge and d == "買い":
        d = "買い検討"
    return d


# ---------------------------------------------------------------- シナリオ(明示の一覧 または 節点ツリー)
def step(grade, k):
    if grade == "N/A":
        return grade
    i = ORDER.index(grade) - k
    return ORDER[min(max(i, 0), len(ORDER) - 1)]


def scenario_value(sc, base_grades, cfg):
    if "peg_start" in sc:
        start = float(sc["peg_start"])
        peg = {str(y): start - cfg["peg_decrement"] * i for i, y in enumerate(cfg["years"])}
        gr = dict(letter=sc.get("letter", "—"), peg_start=start)
    else:
        gr = grade_of(sc.get("grades", base_grades), cfg["years"], cfg["peg_decrement"])
        if gr["peg"] is None:
            return dict(gr, value=0.0, rows=[]), None
        peg = gr["peg"]
    rows, value, _ = fair_path(sc["eps"], peg, cfg)
    return gr, dict(value=value, rows=rows)


def run_tree(tree, base_eps, base_grades, cfg):
    nodes = tree["nodes"]
    ids = [n["id"] for n in nodes]
    combos = []
    for state in itertools.product([True, False], repeat=len(nodes)):
        st = dict(zip(ids, state))
        p = 1.0
        for n in nodes:
            if "given" in n:   # 条件付き確率: {"node": "N3", "p_if_success": 0.68, "p_if_fail": 0.52}
                gv = n["given"]
                pn = gv["p_if_success"] if st[gv["node"]] else gv["p_if_fail"]
            else:
                pn = n["p"]
            p *= pn if st[n["id"]] else (1 - pn)
        eps = {}
        for y, v in base_eps.items():
            m = 1.0
            for n in nodes:
                s = float(n.get("eps_shock", {}).get(str(y), 0.0))
                m *= (1 + s) if st[n["id"]] else (1 - s)     # 振れ幅は対称
            eps[str(y)] = v * m
        grades = dict(base_grades)
        for n in nodes:
            for c in n.get("links", []):
                c = str(c)
                if c in grades:
                    grades[c] = step(grades[c], 1 if st[n["id"]] else -1)
        sc = dict(name="".join("○" if st[i] else "×" for i in ids), p=p, eps=eps, grades=grades)
        gr, res = scenario_value(sc, base_grades, cfg)
        combos.append(dict(name=sc["name"], state=st, p=p, eps=eps, grades=grades, letter=gr.get("letter"),
                           peg_start=gr.get("peg_start"), value=res["value"] if res else 0.0))
    bundles = {}
    rule = tree.get("bundles", {})
    for c in combos:
        b = "base"
        if rule.get("bull_if_all_success") and all(c["state"][i] for i in rule["bull_if_all_success"]):
            b = "bull"
        elif rule.get("bear_if_all_fail") and all(not c["state"][i] for i in rule["bear_if_all_fail"]):
            b = "bear"
        c["bundle"] = b
    return combos


def summarize(scen):
    tot = sum(s["p"] for s in scen)
    if abs(tot - 1.0) > 1e-6:
        raise InputError(f"シナリオの確率の合計が {tot:.4f} です(1.0 にする)。")
    ev = sum(s["p"] * s["value"] for s in scen)
    sd = math.sqrt(sum(s["p"] * (s["value"] - ev) ** 2 for s in scen))
    bundles = {}
    for b in ("bull", "base", "bear"):
        ss = [s for s in scen if s.get("bundle") == b]
        if ss:
            pb = sum(s["p"] for s in ss)
            bundles[b] = dict(p=pb, value=sum(s["p"] * s["value"] for s in ss) / pb,
                              peg_range=[min(s["peg_start"] for s in ss if s.get("peg_start") is not None),
                                         max(s["peg_start"] for s in ss if s.get("peg_start") is not None)]
                              if any(s.get("peg_start") is not None for s in ss) else None)
    return dict(ev=ev, sd=sd, bundles=bundles)


# ---------------------------------------------------------------- エントリー圏(scenario-strategy §6)
def entry(alpha, B, U, L, prices, edge):
    z1 = min(B * (1 - alpha), L * (1 + alpha / 2)) if L is not None else B * (1 - alpha)
    z2 = B * (1 - alpha / 2)
    out = dict(alpha=alpha, B=B, U=U, L=L, Z1=z1, Z2=z2, by_price={})
    for name, p in prices.items():
        ud = (U - p) / (p - L) if (U is not None and L is not None and p > L) else None
        if p <= z1 and edge:
            zone = "即時"
            if ud is not None and ud < 2:
                zone = "分割(上値と下値の比 < 2 のため即時を分割に)"
        elif p <= z2:
            zone = "分割"
        else:
            zone = "見送り"
        if p <= z1 and not edge:
            zone = "分割(市場との差分なしのため即時圏を設けない)"
        out["by_price"][name] = dict(price=p, zone=zone, up_down=ud, L_above_price=(L is not None and L > p))
    return out


# ---------------------------------------------------------------- 本体
def main():
    ap = argparse.ArgumentParser(description="銘柄分析メソッドの価値評価の計算機")
    ap.add_argument("input")
    ap.add_argument("-o", "--outdir", default=None)
    a = ap.parse_args()
    with open(a.input, encoding="utf-8") as f:
        x = json.load(f)
    outdir = a.outdir or os.path.dirname(os.path.abspath(a.input))
    try:
        res = compute(x)
    except InputError as e:
        print("入力の誤り:", e, file=sys.stderr)
        sys.exit(2)
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "valuation.json"), "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    with open(os.path.join(outdir, "valuation.md"), "w", encoding="utf-8") as f:
        f.write(report_md(res))
    for c in res["checks"]:
        print(("OK  " if c["ok"] else "NG  ") + c["name"] + ": " + c["detail"])
    print("出力:", os.path.join(outdir, "valuation.json"), "/ valuation.md")
    sys.exit(0 if all(c["ok"] for c in res["checks"]) else 1)


def compute(x):
    years = [int(y) for y in need(x, "years", "入力")]
    w = [float(v) for v in x.get("weights", [0.4, 0.3, 0.2, 0.1])]
    if len(w) != len(years) or abs(sum(w) - 1.0) > 1e-9:
        raise InputError("weights は years と同じ数で、合計 1.0 にしてください(標準は 0.4・0.3・0.2・0.1)。")
    c = need(x, "coe", "入力")
    coe = float(c["value"]) if "value" in c else float(need(c, "rf", "coe")) + float(need(c, "beta", "coe")) * float(need(c, "erp", "coe"))
    mat = dict(g5_threshold=0.15, roe=0.18, g_long=0.05)
    mat.update(x.get("maturity", {}))
    cfg = dict(years=years, weights=w, survival=float(x.get("survival", 1.0)), coe=coe, maturity=mat,
               g_cap=float(x.get("g_cap", 0.50)), extend_decel=float(x.get("extend_decel", 0.03)),
               peg_decrement=float(x.get("peg_decrement", 0.05)))
    paths = need(x, "eps_paths", "入力")
    adopted = need(x, "adopted_path", "入力")
    if adopted not in paths:
        raise InputError(f"adopted_path '{adopted}' が eps_paths にありません。")
    grades = need(x, "grades", "入力")
    gr = grade_of(grades, years, cfg["peg_decrement"])
    prices = {k: float(v) for k, v in need(x, "prices", "入力").items()}
    edge = bool(x.get("edge", True))
    res = dict(ticker=x.get("ticker", ""), cfg=cfg, coe=coe, grade=gr, paths={}, checks=[], display={})
    checks = res["checks"]

    if gr["peg"] is None:
        res["decision"] = dict(letter=gr["letter"], decision="見送り", reason="構造評価が D 以下で許容 PEG を設定しない")
        res["display"] = {"grade.letter": gr["letter"], "decision": "見送り"}
        checks.append(dict(name="構造評価", ok=True, detail=f"{gr['letter']}(許容 PEG なし)"))
        return res

    peg10 = {str(y): 1.0 for y in years}
    for name, eps in paths.items():
        eps_eval = {k: v for k, v in eps.items() if int(k) >= years[0]}
        rows, value, ext = fair_path(eps_eval, gr["peg"], cfg)
        _, v10, _ = fair_path(eps_eval, peg10, cfg)
        cag = {}
        for win in x.get("cagr_windows", []):
            a0, a1 = int(win[0]), int(win[1])
            e_all = {int(k): float(v) for k, v in eps.items()}
            cag[f"{a0}-{a1}"] = cagr(e_all.get(a0), e_all.get(a1), a1 - a0)
        res["paths"][name] = dict(rows=rows, value=value, value_peg10=v10, extended_years=ext, cagr=cag,
                                  gap={k: value / p - 1 for k, p in prices.items()})
        # 検算(第5.2版の 5): 許容 PEG が 1 を超えるのに PEG 1.0 の値を下回ったら計算の誤り
        if gr["peg_start"] > 1.0:
            checks.append(dict(name=f"PEG 1.0 の検算({name})", ok=value >= v10 - 1e-9,
                               detail=f"理論株価 {rnd(value, 2)} ≥ PEG 1.0 の値 {rnd(v10, 2)}"))

    # シナリオ
    scen = None
    base_eps = {k: float(v) for k, v in paths[adopted].items() if int(k) >= years[0]}
    if "tree" in x:
        scen = run_tree(x["tree"], base_eps, {str(k): str(v).upper() for k, v in grades.items()}, cfg)
    elif "scenarios" in x:
        scen = []
        for s in x["scenarios"]:
            g2, r2 = scenario_value(s, grades, cfg)
            scen.append(dict(name=s["name"], p=float(s["p"]), bundle=s.get("bundle", "base"), letter=g2.get("letter"),
                             peg_start=g2.get("peg_start"), value=r2["value"] if r2 else 0.0,
                             eps={k: float(v) for k, v in s["eps"].items()}))
    if scen:
        sm = summarize(scen)
        res["scenarios"] = dict(items=scen, **sm)
        for item in scen:
            item.pop("state", None)

    # 判断とエントリー
    B = res["paths"][adopted]["value"]
    U = L = None
    if scen and "bull" in res["scenarios"]["bundles"] and "bear" in res["scenarios"]["bundles"]:
        U, L = res["scenarios"]["bundles"]["bull"]["value"], res["scenarios"]["bundles"]["bear"]["value"]
    U = float(x["bull_value"]) if "bull_value" in x else U
    L = float(x["bear_value"]) if "bear_value" in x else L
    res["entry"] = entry(gr["alpha"], B, U, L, prices, edge)
    res["decision"] = {k: dict(gap=B / p - 1, decision=decide(gr["letter"], B / p - 1, edge)) for k, p in prices.items()}
    if not edge:
        checks.append(dict(name="市場との差分", ok=True, detail="差分なし: 判断の上限は「買い検討」、即時圏なし"))

    # 交差確認(表示だけ。平均に入れない)
    res["cross_checks"] = x.get("cross_checks", {})

    # 感応度(EPS 経路を差し替えた場合)
    sens = []
    for s in x.get("sensitivities", []):
        if "eps" in s:
            eps_s = {k: float(v) for k, v in s["eps"].items() if int(k) >= years[0]}
        else:
            mult = s.get("eps_mult", {})
            eps_s = {k: v * (1 + float(mult.get(k, 0.0))) for k, v in base_eps.items()}
        g_s = grade_of(s["grades"], years, cfg["peg_decrement"]) if "grades" in s else gr
        _, v_s, _ = fair_path(eps_s, g_s["peg"], cfg) if g_s["peg"] else (None, 0.0, None)
        if "shares_mult" in s:      # 希薄化は株数で数える(倍率で割り引かない)
            v_s = v_s / float(s["shares_mult"])
        if "add_per_share" in s:    # 一時の効果(評価減など、1 株当たり)
            v_s += float(s["add_per_share"])
        sens.append(dict(name=s["name"], value=v_s, diff=v_s - B))
    res["sensitivities"] = sens

    # 検査
    checks.append(dict(name="年度の重み", ok=True, detail="・".join(f"{y}:{wi}" for y, wi in zip(years, w))))
    for name, p in res["paths"].items():
        for r in p["rows"]:
            if "note" in r:
                checks.append(dict(name=f"g の上限({name} {r['year']})", ok=True, detail=r["note"]))
    res["display"] = display(res, adopted, prices)
    return res


def display(res, adopted, prices):
    d = {}
    g = res["grade"]
    d["grade.letter"] = g["letter"]
    d["grade.avg"] = rnd(g["avg"], 2)
    d["grade.pos"] = rnd(g["pos"], 2)
    d["grade.distribution"] = "・".join(f"{k}{v}" for k, v in g["distribution"].items())
    d["peg.start"] = rnd(g["peg_start"], 3)
    for y, v in g["peg"].items():
        d[f"peg.{y}"] = rnd(v, 3)
    d["alpha"] = pct(g["alpha"])
    d["coe"] = pct(res["coe"], 2)
    for name, p in res["paths"].items():
        d[f"value.{name}"] = rnd(p["value"], 1)
        d[f"value_peg10.{name}"] = rnd(p["value_peg10"], 1)
        for k, v in p["gap"].items():
            d[f"gap.{name}.{k}"] = ("+" if v >= 0 else "") + pct(v, 0)
        for k, v in p["cagr"].items():
            d[f"cagr.{name}.{k}"] = pct(v)
        for r in p["rows"]:
            y = r["year"]
            d[f"row.{name}.{y}.eps"] = rnd(r["eps"], 2)
            d[f"row.{name}.{y}.g"] = pct(r["g"])
            d[f"row.{name}.{y}.per"] = rnd(r["per"], 1)
            d[f"row.{name}.{y}.price"] = rnd(r["price"], 1)
            d[f"row.{name}.{y}.pv"] = rnd(r["pv"], 1)
    if "scenarios" in res:
        s = res["scenarios"]
        d["scen.ev"] = rnd(s["ev"], 1)
        d["scen.sd"] = rnd(s["sd"], 1)
        for b, v in s["bundles"].items():
            d[f"scen.{b}.p"] = pct(v["p"])
            d[f"scen.{b}.value"] = rnd(v["value"], 1)
            if v.get("peg_range"):
                lo, hi = v["peg_range"]
                d[f"scen.{b}.peg"] = rnd(lo, 2) if abs(hi - lo) < 1e-9 else f"{rnd(lo, 2)}〜{rnd(hi, 2)}"
    e = res["entry"]
    d["entry.Z1"] = rnd(e["Z1"], 1)
    d["entry.Z2"] = rnd(e["Z2"], 1)
    for k, v in e["by_price"].items():
        d[f"entry.zone.{k}"] = v["zone"]
        d[f"entry.up_down.{k}"] = rnd(v["up_down"], 1) if v["up_down"] is not None else "—"
    for k, v in res["decision"].items():
        d[f"decision.{k}"] = v["decision"]
    for s in res.get("sensitivities", []):
        d[f"sens.{s['name']}"] = rnd(s["value"], 1)
        d[f"sens.{s['name']}.diff"] = ("+" if s["diff"] >= 0 else "−") + rnd(abs(s["diff"]), 1)
    return d


def report_md(res):
    d = res["display"]
    g = res["grade"]
    L = [f"# 価値評価の計算結果 {res.get('ticker', '')}", "",
         "この表の数字は計算機の出力。資料・報告書には display の表示値を写し、手で丸め直さない。", "",
         "## 構造評価 → 許容 PEG・α", "",
         f"- 分布 {d['grade.distribution']}、平均点 {d['grade.avg']}、等級 {g['letter']}、帯の中の位置 {d.get('grade.pos', '—')}",
         f"- 許容 PEG(年度別): " + "・".join(f"{y} {d[f'peg.{y}']}" for y in g["peg"]) if g.get("peg") else "- 許容 PEG なし",
         f"- α {d.get('alpha', '—')}、株主資本コスト {d['coe']}",
         "- 規則: " + " / ".join(g["rules"]), ""]
    for name, p in res.get("paths", {}).items():
        L += [f"## 年度別の理論株価({name})", "", "| 年度 | EPS | 3 年の g | 許容 PEG | 妥当 PER | 適正株価 | 今日の価値 | 方法 |", "|---|---|---|---|---|---|---|---|"]
        for r in p["rows"]:
            L.append(f"| {r['year']}{'(延長)' if r['eps_extended'] else ''} | {rnd(r['eps'], 2)} | {pct(r['g'])} | {rnd(r['peg'], 3)} | "
                     f"{rnd(r['per'], 1)} | {rnd(r['price'], 1)} | {rnd(r['pv'], 1)} | {r['method']} |")
        L += ["", f"理論株価 **{d[f'value.{name}']}**(PEG 1.0 なら {d[f'value_peg10.{name}']})。乖離: " +
              "、".join(f"{k} {v}" for k, v in ((k, d[f'gap.{name}.{k}']) for k in p["gap"])), ""]
    if "scenarios" in res:
        L += ["## シナリオ", "", f"期待値 {d['scen.ev']}、標準偏差 {d['scen.sd']}", ""]
        for b in ("bull", "base", "bear"):
            if f"scen.{b}.p" in d:
                L.append(f"- {b}: 確率 {d[f'scen.{b}.p']}、価値 {d[f'scen.{b}.value']}" + (f"、PEG {d[f'scen.{b}.peg']}" if f"scen.{b}.peg" in d else ""))
        L.append("")
    if "entry" in res:
        e = res["entry"]
        L += ["## エントリー圏", "", f"即時 ≤ {d['entry.Z1']}、分割 {d['entry.Z1']} 超〜{d['entry.Z2']} 以下、見送り > {d['entry.Z2']}", ""]
        for k, v in e["by_price"].items():
            L.append(f"- 株価 {k}({v['price']}): {v['zone']}、上値と下値の比 {d[f'entry.up_down.{k}']}、判断 {d[f'decision.{k}']}")
        L.append("")
    if res.get("sensitivities"):
        L += ["## 感応度", ""] + [f"- {s['name']}: {d['sens.' + s['name']]}({d['sens.' + s['name'] + '.diff']})" for s in res["sensitivities"]] + [""]
    if res.get("cross_checks"):
        L += ["## 交差確認(平均に入れない)", ""] + [f"- {k}: {v}" for k, v in res["cross_checks"].items()] + [""]
    L += ["## 検査", ""] + [("- OK " if c["ok"] else "- **NG** ") + f"{c['name']}: {c['detail']}" for c in res["checks"]]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
