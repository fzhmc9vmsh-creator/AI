#!/usr/bin/env python3
"""Sankey (P&L flow) for the slide deck, slide 9 (SOFI, Q3 2026).
Drawn at 8.4 x 5.0 in with the deck palette. Rendering only: every number comes from
data/f19_sankey_nodes.csv and data/f19_sankey_links.csv. Output: sankey_q3_2026.png.
Q3 2026 has no interest-income/expense breakdown, so NII is one source node."""
import csv
import os
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
OUT = os.path.join(HERE, "sankey_q3_2026.png")

font_manager.fontManager.addfont("/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf")
plt.rcParams["font.family"] = "IPAGothic"
plt.rcParams["axes.unicode_minus"] = False

MINUS = "−"
INK = "#333333"
SUB = "#767676"
RED = "#C0392B"

# deck palette
REV_BAR, REV_FLOW = "#767676", "#D9D9D9"
PRO_BAR, PRO_FLOW = "#197A56", "#86C99B"
COST_BAR, COST_FLOW, COST_ALPHA = "#C0392B", "#C0392B", 0.25


# ----------------------------------------------------------------- formatting
def hu(val, nd):
    q = Decimal(1).scaleb(-nd)
    return str(Decimal(val).quantize(q, rounding=ROUND_HALF_UP))


def fmt_m(musd):
    """million USD with thousands separator, one decimal (the data's own precision)."""
    return "{:,}".format(Decimal(hu(musd, 1)))


def fmt_yoy(y):
    d = Decimal(y)
    nd = 1 if abs(d) < 10 else 0
    s = hu(abs(d), nd)
    if d > 0:
        return "+" + s + "%"
    if d < 0:
        return MINUS + s + "%"
    return "±" + s + "%"


# =============================================================== Sankey
def load_sankey():
    nodes = {}
    with open(os.path.join(DATA, "f19_sankey_nodes.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            nodes[r["node_id"]] = dict(
                id=r["node_id"], label=r["label_ja"], sub=r["sub_ja"], v=Decimal(r["q3_2026_musd"]),
                v0=r["q3_2025_musd"], yoy=r["yoy_pct"], share=r["pct_of_revenue_q3_2026"])
    links = []
    with open(os.path.join(DATA, "f19_sankey_links.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            links.append(dict(s=r["source"], t=r["target"], v=Decimal(r["value_musd"]), kind=r["kind"]))
    return nodes, links


def make_sankey():
    nodes, links = load_sankey()

    FW, FH = 8.4, 5.0
    fig = plt.figure(figsize=(FW, FH), facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, FW)
    ax.set_ylim(FH, 0)  # inches, y grows downward
    ax.axis("off")

    S = 0.0019           # inches per musd (same everywhere)
    BW = 0.07            # bar width (in)
    TOP = 0.75           # top of the plot (inches)
    MINH = 0.012

    # columns: 0 = NII / 非金利収益, 1 = 総純収益, 2 = 税引前利益, 3 = 純利益・税 / 費用
    XS = {0: 2.10, 1: 3.55, 2: 5.00, 3: 6.55}
    col = dict(nii=0, nonint=0, revenue=1, pretax=2,
               net_income=3, tax=3, sm=3, tpd=3, ops_ga=3, other_adj=3)
    GREY_N = {"nonint", "revenue"}
    GREEN_N = {"nii", "pretax", "net_income"}
    for k, n in nodes.items():
        n["col"] = col[k]
        n["x"] = XS[col[k]]
        n["h"] = float(n["v"]) * S
        n["kind"] = "revenue" if k in GREY_N else ("profit" if k in GREEN_N else "cost")

    BAR = dict(revenue=REV_BAR, profit=PRO_BAR, cost=COST_BAR)
    FLOW = dict(revenue=(REV_FLOW, 1.0), profit=(PRO_FLOW, 1.0), cost=(COST_FLOW, COST_ALPHA))

    HIGHLIGHT = {"sm"}   # grows faster than 総純収益
    F_NAME, F_SUB, F_VAL = 7.6, 6.4, 7.0
    LH = lambda sz: sz * 1.40 / 72.0   # line height in inches

    # ---- label content: list of (text, size, bold, color)
    for k, n in nodes.items():
        hl = k in HIGHLIGHT
        c = RED if hl else INK
        lines = [(n["label"], F_NAME, True, c)]
        if n["sub"]:
            lines.append((n["sub"], F_SUB, False, SUB))
        val = fmt_m(n["v"])
        if n["yoy"] != "":
            val += " (%s)" % fmt_yoy(n["yoy"])
        lines.append((val, F_VAL, hl, c))
        if hl:
            lines.append(("収益の伸び(%s)を上回る" % fmt_yoy(nodes["revenue"]["yoy"]), F_VAL - 0.3, True, RED))
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

    LEAVES = {"nonint", "other_adj", "net_income", "tax", "sm", "tpd", "ops_ga"}
    # col0: NII above 非金利収益
    stack(["nii", "nonint"], TOP, 0.10, LEAVES)
    # col1: 総純収益
    stack(["revenue"], TOP, 0, set())
    # col2: 税引前利益(推定)
    stack(["pretax"], TOP, 0, set())
    # col3: 純利益・税(税引前から)、続けて費用(総純収益から)
    stack(["net_income", "tax"], TOP, 0.09, LEAVES)
    stack(["sm", "tpd", "ops_ga", "other_adj"], 2.35, 0.06, LEAVES)

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
            L["sy0"], L["sy1"] = y, y + float(L["v"]) * S
            y = L["sy1"]
    for k, ls in ins.items():
        ls.sort(key=lambda L: nodes[L["s"]]["yc"])
        y = nodes[k]["f0"]
        for L in ls:
            L["ty0"], L["ty1"] = y, y + float(L["v"]) * S
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
        elif anchor == "above":
            top = n["b0"] - 0.05 - H
        y = top
        for text, sz, bold, color in n["lines"]:
            lh = LH(sz)
            if side == "right":
                put(n["x"] + BW / 2 + dx, y + lh / 2, text, sz, color, bold, ha="left")
            elif side == "left":
                put(n["x"] - BW / 2 - dx, y + lh / 2, text, sz, color, bold, ha="right")
            else:  # centred above the bar
                put(n["x"], y + lh / 2, text, sz, color, bold, ha="center")
            y += lh

    # 左に出すラベル: 源泉の 2 つ / 上に出すラベル: 総純収益・税引前利益(右は流れと重なるため)
    PLACE = {"nii": ("left", "center"), "nonint": ("left", "center"),
             "revenue": ("center", "above"), "pretax": ("center", "above")}
    for k in nodes:
        side, anchor = PLACE.get(k, ("right", "center"))
        put_label(k, side, anchor)

    fig.canvas.draw()
    report_overlaps(fig, ax, texts, bar_rects, FW, FH)
    fig.savefig(OUT, dpi=200, facecolor="white")
    plt.close(fig)
    print("wrote", OUT)


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
