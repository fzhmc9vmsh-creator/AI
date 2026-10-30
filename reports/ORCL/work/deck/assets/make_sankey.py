#!/usr/bin/env python3
"""Sankey (P&L flow) for the slide deck, slide 9. Derived from charts2/make_f19.py.
Redrawn at 8.4 x 5.0 in with the deck palette; title / subtitle / source / reading box removed.
Rendering only: every number comes from data/f19_sankey_*.csv."""
import csv
import os
import re
from decimal import Decimal, ROUND_HALF_UP

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib import font_manager
from matplotlib.patches import PathPatch, Rectangle
from matplotlib.path import Path

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

font_manager.fontManager.addfont("/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf")
plt.rcParams["font.family"] = "IPAGothic"
plt.rcParams["axes.unicode_minus"] = False

MINUS = "−"
INK = "#333333"
RED = "#C0392B"

# deck palette
REV_BAR, REV_FLOW = "#767676", "#D9D9D9"
PRO_BAR, PRO_FLOW = "#197A56", "#86C99B"
COST_BAR, COST_FLOW, COST_ALPHA = "#C0392B", "#C0392B", 0.25


# ----------------------------------------------------------------- formatting
def hu(val, nd):
    q = Decimal(1).scaleb(-nd)
    return str(Decimal(val).quantize(q, rounding=ROUND_HALF_UP))


def fmt_b(musd):
    return hu(Decimal(int(musd)) / Decimal(1000), 2)


def fmt_yoy(y, force1=False):
    d = Decimal(y)
    nd = 1 if (abs(d) < 10 or force1) else 0
    s = hu(abs(d), nd)
    if d > 0:
        return "+" + s + "%"
    if d < 0:
        return MINUS + s + "%"
    return "±" + s + "%"


# =============================================================== Sankey
def load_sankey():
    nodes, order = {}, []
    with open(os.path.join(DATA, "f19_sankey_nodes.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            nodes[r["node_id"]] = dict(
                id=r["node_id"], label=r["label_ja"], v=int(r["q1fy27_musd"]),
                v0=int(r["q1fy26_musd"]), yoy=r["yoy_pct"], share=r["pct_of_revenue_q1fy27"])
            order.append(r["node_id"])
    links = []
    with open(os.path.join(DATA, "f19_sankey_links.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            links.append(dict(s=r["source"], t=r["target"], v=int(r["value_musd"]), kind=r["kind"]))
    return nodes, links


def make_sankey():
    nodes, links = load_sankey()

    FW, FH = 8.4, 5.0
    fig = plt.figure(figsize=(FW, FH), facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, FW)
    ax.set_ylim(FH, 0)  # inches, y grows downward
    ax.axis("off")

    S = 0.000163         # inches per musd (same everywhere)
    BW = 0.07            # bar width (in)
    PLOT_TOP = 0.60
    MINH = 0.012

    XS = {0: 1.28, 1: 2.38, 2: 3.50, 3: 4.64, 4: 5.92, 5: 7.10}
    XNONOP = 5.28

    col = dict(rev_cloud=0, rev_software=0, rev_hardware=0, rev_services=0, revenue=1,
               gross_profit=2, cos=2, operating_income=3, opex=3, cos_cs=3, cos_hw=3, cos_sv=3,
               pretax=4, interest=4, sm=4, rd=4, ga=4, amort=4, restr=4, nonop=3.5,
               net_income=5, tax_nci=5)
    GREY_N = {"rev_cloud", "rev_software", "rev_hardware", "rev_services", "revenue"}
    GREEN_N = {"gross_profit", "operating_income", "pretax", "net_income", "nonop"}
    for k, n in nodes.items():
        n["col"] = col[k]
        n["x"] = XNONOP if k == "nonop" else XS[col[k]]
        n["h"] = n["v"] * S
        n["kind"] = "revenue" if k in GREY_N else ("profit" if k in GREEN_N else "cost")

    BAR = dict(revenue=REV_BAR, profit=PRO_BAR, cost=COST_BAR)
    FLOW = dict(revenue=(REV_FLOW, 1.0), profit=(PRO_FLOW, 1.0), cost=(COST_FLOW, COST_ALPHA))

    HIGHLIGHT = {"cos_cs", "cos_hw", "interest", "tax_nci"}
    MARGIN = {
        "gross_profit": ["粗利率 60.0%", "(前年 67.3%, " + MINUS + "7.3pt)"],
        "operating_income": ["営業利益率 34.8%", "(前年 28.7%, +6.1pt)"],
        "net_income": ["純利益率 24.2%", "(前年 19.6%, +4.6pt)"],
    }
    F_NAME, F_VAL = 7.6, 7.0
    LH = lambda sz: sz * 1.40 / 72.0   # line height in inches

    # ---- label content: list of (text, size, bold, color)
    for k, n in nodes.items():
        hl = k in HIGHLIGHT
        c = RED if hl else INK
        if k == "rev_software":
            name_lines = [("ソフトウェア", F_NAME, True, c), ("(ライセンス・保守)", F_NAME, True, c)]
        else:
            name_lines = [(n["label"], F_NAME, True, c)]
        lines = name_lines + [("$%sB (%s)" % (fmt_b(n["v"]), fmt_yoy(n["yoy"], k == "revenue")), F_VAL, hl, c)]
        if k.startswith("rev_"):
            lines.append(("構成比 %s%%" % hu(n["share"], 0), F_VAL, False, INK))
        if k in MARGIN:
            for ml in MARGIN[k]:
                lines.append((ml, F_VAL, False, INK))
        if hl:
            lines.append(("▲売上の伸び(+29.6%)超", F_VAL - 0.3, True, RED))
        n["lines"] = lines
        n["lab_h"] = sum(LH(sz) for _, sz, _, _ in lines)

    # ---- vertical layout (inches from top). stack() places slots with gaps.
    def slot_h(k, leaf):
        n = nodes[k]
        return max(n["h"], n["lab_h"] + 0.02) if leaf else n["h"]

    def stack(keys, top, gaps, leaf_set):
        y = top
        for i, k in enumerate(keys):
            if i > 0:
                y += gaps[i - 1] if isinstance(gaps, (list, tuple)) else gaps
            sh = slot_h(k, k in leaf_set)
            nodes[k]["yc"] = y + sh / 2
            y += sh
        return y

    LEAVES = {"rev_hardware", "rev_services", "rev_cloud", "rev_software",
              "cos_cs", "cos_hw", "cos_sv", "sm", "rd", "ga", "amort", "restr",
              "interest", "tax_nci", "net_income"}
    # col0
    stack(["rev_cloud", "rev_software", "rev_hardware", "rev_services"], 0.62, 0.10, LEAVES)
    # col1
    stack(["revenue"], 1.02, 0, set())
    # col2
    stack(["gross_profit", "cos"], 0.68, 0.30, set())
    # col3
    stack(["operating_income", "opex"], PLOT_TOP, 0.22, set())
    stack(["cos_cs", "cos_hw", "cos_sv"], 3.02, 0.06, LEAVES)
    # col4
    stack(["pretax"], PLOT_TOP, 0, set())
    stack(["interest"], 1.86, 0, LEAVES)
    stack(["sm", "rd", "ga", "amort", "restr"], 2.46, 0.03, LEAVES)
    # col5
    stack(["net_income"], PLOT_TOP, 0, LEAVES)
    stack(["tax_nci"], 1.48, 0, LEAVES)
    # nonop (col 3.5) sits above the OI->pretax band
    nodes["nonop"]["yc"] = 0.46

    for n in nodes.values():
        n["f0"] = n["yc"] - n["h"] / 2           # flow region
        n["f1"] = n["yc"] + n["h"] / 2
        bh = max(n["h"], MINH)
        n["b0"] = n["yc"] - bh / 2               # bar region
        n["b1"] = n["yc"] + bh / 2

    # ---- flow attachment offsets
    outs, ins = {}, {}
    for L in links:
        outs.setdefault(L["s"], []).append(L)
        ins.setdefault(L["t"], []).append(L)
    for k, ls in outs.items():
        ls.sort(key=lambda L: nodes[L["t"]]["yc"])
        y = nodes[k]["f0"]
        for L in ls:
            L["sy0"], L["sy1"] = y, y + L["v"] * S
            y = L["sy1"]
    for k, ls in ins.items():
        ls.sort(key=lambda L: nodes[L["s"]]["yc"])
        y = nodes[k]["f0"]
        for L in ls:
            L["ty0"], L["ty1"] = y, y + L["v"] * S
            y = L["ty1"]

    # ---- draw flows
    for L in links:
        xs = nodes[L["s"]]["x"] + BW / 2
        xt = nodes[L["t"]]["x"] - BW / 2
        xm = (xs + xt) / 2
        verts = [(xs, L["sy0"]), (xm, L["sy0"]), (xm, L["ty0"]), (xt, L["ty0"]),
                 (xt, L["ty1"]), (xm, L["ty1"]), (xm, L["sy1"]), (xs, L["sy1"]), (xs, L["sy0"])]
        codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4,
                 Path.LINETO, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CLOSEPOLY]
        fc, al = FLOW[L["kind"]]
        ax.add_patch(PathPatch(Path(verts, codes), fc=fc, ec="none", alpha=al, lw=0, zorder=1))

    # ---- draw bars
    bar_rects = []
    for k, n in nodes.items():
        r = Rectangle((n["x"] - BW / 2, n["b0"]), BW, n["b1"] - n["b0"],
                      fc=BAR[n["kind"]], ec="none", zorder=3)
        ax.add_patch(r)
        bar_rects.append((k, r))

    # ---- text helpers
    texts = []

    def put(x, y, s, size, color=INK, bold=False, ha="left", va="center", halo=True, **kw):
        effects = []
        if halo:
            effects.append(pe.Stroke(linewidth=2.2, foreground="white", alpha=0.85))
        if bold:
            effects.append(pe.Stroke(linewidth=0.4, foreground=color))
        effects.append(pe.Normal())
        t = ax.text(x, y, s, fontsize=size, color=color, ha=ha, va=va, zorder=5,
                    path_effects=effects, **kw)
        texts.append((s, t))
        return t

    def put_label(k, side="right", anchor="center", dx=0.08):
        n = nodes[k]
        H = n["lab_h"]
        if anchor == "center":
            top = n["yc"] - H / 2
        elif anchor == "top":
            top = n["b0"]
        elif anchor == "bottom":
            top = n["b1"] - H
        elif anchor == "above":
            top = n["b0"] - 0.05 - H
        y = top
        for text, sz, bold, color in n["lines"]:
            lh = LH(sz)
            if side == "right":
                put(n["x"] + BW / 2 + dx, y + lh / 2, text, sz, color, bold, ha="left")
            elif side == "left":
                put(n["x"] - BW / 2 - dx, y + lh / 2, text, sz, color, bold, ha="right")
            else:  # centred above
                put(n["x"], y + lh / 2, text, sz, color, bold, ha="center")
            y += lh

    for k in nodes:
        if k.startswith("rev_"):
            put_label(k, "left")
        elif k == "nonop":
            put_label(k, "center", anchor="above", dx=0)
        elif k == "cos_cs":
            put_label(k, "right", anchor="bottom")
        else:
            put_label(k, "right")

    out = os.path.join(HERE, "sankey_q1fy27.png")
    fig.canvas.draw()
    report_overlaps(fig, ax, texts, bar_rects, FW, FH)
    fig.savefig(out, dpi=200, facecolor="white")
    plt.close(fig)
    print("wrote", out)


def report_overlaps(fig, ax, texts, bar_rects, FW, FH):
    r = fig.canvas.get_renderer()
    inv = fig.dpi
    boxes = []
    for s, t in texts:
        bb = t.get_window_extent(r)
        boxes.append((s, bb.x0 / inv, FH - bb.y1 / inv, bb.x1 / inv, FH - bb.y0 / inv))
    bad = 0
    shrink = 0.01
    for i in range(len(boxes)):
        s, x0, y0, x1, y1 = boxes[i]
        if x0 < 0.02 or x1 > FW - 0.02 or y0 < 0.02 or y1 > FH - 0.02:
            print("OUT OF FIGURE:", repr(s[:30]), round(x0, 2), round(x1, 2), round(y0, 2), round(y1, 2))
            bad += 1
        for j in range(i + 1, len(boxes)):
            t, a0, b0, a1, b1 = boxes[j]
            if x0 + shrink < a1 and a0 + shrink < x1 and y0 + shrink < b1 and b0 + shrink < y1:
                print("TEXT OVERLAP:", repr(s[:25]), "<->", repr(t[:25]))
                bad += 1
        for k, rc in bar_rects:
            bx0, by0 = rc.get_x(), rc.get_y()
            bx1, by1 = bx0 + rc.get_width(), by0 + rc.get_height()
            if x0 < bx1 and bx0 < x1 and y0 + shrink < by1 and by0 < y1 - shrink:
                print("TEXT/BAR OVERLAP:", repr(s[:25]), k)
                bad += 1
    print("overlap issues:", bad)
    print("min left %.2f, max right %.2f in (fig width %.1f); min top %.2f, max bottom %.2f (fig height %.1f)" % (
        min(b[1] for b in boxes), max(b[3] for b in boxes), FW, min(b[2] for b in boxes), max(b[4] for b in boxes), FH))


if __name__ == "__main__":
    make_sankey()
