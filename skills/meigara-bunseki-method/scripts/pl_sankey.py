#!/usr/bin/env python3
"""損益フロー図(サンキー、図F19): py -3 pl_sankey.py <入力.json> <出力.png> [--compact]
--compact はスライド用。見出しと KPI の札を省き、横長で文字を大きくする(スライドに貼ると 8pt 相当)。
入力: company, period, unit(既定 百万円), revenues[{name, value, yoy}], total{value,yoy}, gross{value,yoy}, cogs{value,yoy},
cogs_detail[{name,value,yoy}](省略可), op{value,yoy}, sga{value,yoy} か sga_detail, net{value,yoy}, below[{name,value,yoy}], notes[文]
値は同じ単位。yoy は前年比%(None は表示しない)。売上 → 粗利/原価 → 営業利益/販管費 → 純利益/営業外・税 の順に流す。"""
import json
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, PathPatch, Rectangle
from matplotlib.path import Path
import numpy as np

plt.rcParams['font.family'] = ['Yu Gothic', 'Meiryo', 'MS Gothic', 'sans-serif']
GRAY, GR, RED = '#c9cacc', '#a8e3b4', '#e8aaaa'
BAR_G, BAR_GN, BAR_R = '#606166', '#1db954', '#d92b2b'
UP, DN = '#2e9e57', '#d13438'


def band(ax, x0, y0a, y0b, x1, y1a, y1b, c0, c1, n=40):
    """2点間を滑らかな帯で結ぶ。色は左から右へ変える"""
    t = np.linspace(0, 1, n + 1)
    s = t * t * (3 - 2 * t)
    for i in range(n):
        xs = [x0 + (x1 - x0) * t[i], x0 + (x1 - x0) * t[i + 1]]
        top = [y0a + (y1a - y0a) * s[i], y0a + (y1a - y0a) * s[i + 1]]
        bot = [y0b + (y1b - y0b) * s[i], y0b + (y1b - y0b) * s[i + 1]]
        f = t[i] ** 2
        col = tuple(a * (1 - f) + b * f for a, b in zip(matplotlib.colors.to_rgb(c0), matplotlib.colors.to_rgb(c1)))
        ax.fill_between(xs, bot, top, color=col, linewidth=.6, edgecolor=col)


CMP = ['前年比']   # 比較の呼び名。d['compare_label'] があれば差し替える(5年後サンキー図用)


def yoy(v):
    if v is None:
        return '', '#666'
    return (f"{v:+.1f}% {CMP[0]}" if abs(v) < 1 else f"{v:+.0f}% {CMP[0]}").replace('-', '−'), (UP if v >= 0 else DN)


def label(ax, x, y, name, val, y_v, unit, ha='left', size=15, cost=False, sp=1.0):
    ax.text(x, y + 2.9 * sp, name, ha=ha, va='center', fontsize=size, fontweight='bold', color='#222')
    ax.text(x, y, f"{val:,.0f}", ha=ha, va='center', fontsize=size + 1, color='#222')
    t, c = yoy(y_v)
    if cost and y_v is not None:
        c = DN if y_v > 0 else UP
    ax.text(x, y - 2.9 * sp, t, ha=ha, va='center', fontsize=size - 1, fontweight='bold', color=c)


def main():
    d = json.load(open(sys.argv[1], encoding='utf-8'))
    compact = '--compact' in sys.argv
    CMP[0] = d.get('compare_label', '前年比')
    fig = plt.figure(figsize=(20, 10.2) if compact else (20, 15.6), dpi=110)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(-10 if compact else 0, 200); ax.set_ylim(*((8, 110) if compact else (0, 156))); ax.axis('off')
    ax.text(100, 148.5, d['company'], ha='center', va='center', fontsize=40, fontweight='bold', color='#111')
    ax.add_patch(FancyBboxPatch((73, 134.5), 54, 6.5, boxstyle='round,pad=0,rounding_size=3.5', fc='white', ec='#111', lw=2.5))
    ax.text(100, 137.7, d['period'], ha='center', va='center', fontsize=21, fontweight='bold')
    ax.plot([10, 190], [131.5, 131.5], color='#ddd', lw=2); ax.plot([10, 190], [111, 111], color='#ddd', lw=2)
    u = d.get('unit', '百万円')
    tiles = [('売上高', d['total'], False), ('売上総利益', d['gross'], False), ('売上原価', d['cogs'], True), ('純利益', d['net'], False)]
    for i, (n, o, cost) in enumerate([] if compact else tiles):
        x = 10 + i * 46.3
        ax.add_patch(FancyBboxPatch((x, 121.5), 40, 7.5, boxstyle='round,pad=0,rounding_size=1.5', fc='#0c0c0c', ec='none'))
        ax.text(x + 20, 125.2, n, ha='center', va='center', color='white', fontsize=20, fontweight='bold')
        ax.text(x, 116, f"{o['value']:,.0f}", ha='left', va='center', fontsize=25, fontweight='bold')
        ax.text(x + 15.5, 115.4, u, ha='left', va='center', fontsize=11, color='#555')
        t, c = yoy(o['yoy'])
        if o['yoy'] is None:
            continue
        if cost:
            c = DN if o['yoy'] > 0 else UP
        ax.text(x + 40, 116, ('▲ ' if o['yoy'] >= 0 else '▼ ') + t, ha='right', va='center', fontsize=14.5, fontweight='bold', color=c)
    tot = d['total']['value']
    k = 60.0 / tot            # 売上 1 単位の高さ
    X = [24, 50, 90, 126, 158] if compact else [37, 63, 105, 142, 174]
    S = 1.4 if compact else 1.0   # 図の文字の倍率
    text0 = ax.text
    ax.text = lambda *a, **kw: text0(*a, **{**kw, 'fontsize': kw['fontsize'] * S})
    top = 102.0; W = 1.5
    # 売上の柱(中央 x1)
    y1t = 88.0
    y1b = y1t - tot * k
    h = [r["value"] * k for r in d["revenues"]]
    y = top
    y1 = y1t
    for r, hh in zip(d['revenues'], h):
        hh2 = max(hh, .6)
        band(ax, X[0] + W, y, y - hh2, X[1], y1, y1 - hh, GRAY, GRAY)
        ax.add_patch(Rectangle((X[0], y - hh2), W, hh2, fc=BAR_G))
        mid = y - hh2 / 2
        ax.text(X[0] - 1.5, mid, f"{r['name']}\n{r['value']:,.0f}", ha='right', va='center', fontsize=14, color='#222', fontweight='bold', linespacing=1.3)
        t, c = yoy(r['yoy'])
        ax.text(X[0] - 1.5, mid - 4.6 * (S + 1) / 2 - (1 if compact else 0), t, ha='right', va='center', fontsize=12.5, fontweight='bold', color=c)
        ax.text(X[0] + 3, mid, f"{r['value'] / tot * 100:.0f}%", ha='left', va='center', fontsize=12, color='#555', fontweight='bold',
                bbox=dict(boxstyle='round,pad=.25', fc='white', ec='none', alpha=.9))
        y -= max(hh2 + 3.2, 13.2 if compact else 11.8)
        y1 -= hh
    ax.add_patch(Rectangle((X[1], y1b), W, tot * k, fc=BAR_G))
    label(ax, X[1] + W / 2, y1t + 6.5, '総売上高', tot, d['total']['yoy'], u, ha='center', sp=S)
    # 粗利と原価
    gv, cv = d['gross']['value'], d['cogs']['value']
    gt = y1t + 4; gb = gt - gv * k
    band(ax, X[1] + W, y1t, y1t - gv * k, X[2], gt, gb, GRAY, GR)
    ct = y1t - gv * k - 6; cb = ct - cv * k
    band(ax, X[1] + W, y1t - gv * k, y1b, X[2], ct, cb, GRAY, RED)
    ax.add_patch(Rectangle((X[2], gb), W, gv * k, fc=BAR_GN)); ax.add_patch(Rectangle((X[2], cb), W, cv * k, fc=BAR_R))
    label(ax, X[2] - 8, gt + 7.5, '売上総利益', gv, d['gross']['yoy'], u, ha='center', sp=S)
    label(ax, X[2] - 14, cb - 6.5, '売上原価', cv, d['cogs']['yoy'], u, ha='center', cost=True, sp=S)
    # 原価の内訳
    det = d.get('cogs_detail') or []
    yy = ct + 5
    for r in det:
        hh = r['value'] * k
        ny = yy
        band(ax, X[2] + W, ct, ct - hh, X[3], ny, ny - hh, RED, RED)
        ax.add_patch(Rectangle((X[3], ny - hh), W, hh, fc=BAR_R))
        t, c = yoy(r['yoy'])
        if r['yoy'] is not None:
            c = DN if r['yoy'] > 0 else UP
        ax.text(X[3] + 2.6, ny - hh / 2, f"{r['name']}  {r['value']:,.0f}  ", ha='left', va='center', fontsize=13.5, fontweight='bold', color='#222')
        ax.text(X[3] + (26 if compact else 34), ny - hh / 2, t, ha='left', va='center', fontsize=12, fontweight='bold', color=c)
        ct -= hh
        yy = ny - hh - 1.7
    # 営業利益と販管費
    ov, sv = d['op']['value'], d['sga']['value']
    ot = gt + 3; ob = ot - ov * k
    band(ax, X[2] + W, gt, gt - ov * k, X[3], ot, ob, GR, GR)
    st = ob - 4; sb = st - sv * k
    band(ax, X[2] + W, gt - ov * k, gb, X[3], st, sb, GR, RED)
    ax.add_patch(Rectangle((X[3], ob), W, ov * k, fc=BAR_GN)); ax.add_patch(Rectangle((X[3], sb), W, sv * k, fc=BAR_R))
    label(ax, X[3] - 8, ot + 7, '営業利益', ov, d['op']['yoy'], u, ha='center', sp=S)
    sga_det = d.get('sga_detail') or []
    sga_lx = X[3] + 2.6 if not sga_det else X[3] - 8        # 内訳を出すときは帯の左に見出しを置く
    ax.text(sga_lx, (st + sb) / 2 + (2.2 if sga_det else 0), f"販管費  {sv:,.0f}", ha='right' if sga_det else 'left', va='center',
            fontsize=13.5, fontweight='bold', color='#222')
    t, c = yoy(d['sga']['yoy'])
    ax.text(sga_lx, (st + sb) / 2 - 2.7 * S + (2.2 if sga_det else 0), t, ha='right' if sga_det else 'left', va='center',
            fontsize=11.5, fontweight='bold', color=DN)
    # 営業利益の行き先
    nv = d['net']['value']
    ny = ot + 7
    band(ax, X[3] + W, ot, ot - nv * k, X[4], ny, ny - nv * k, GR, GR)
    ax.add_patch(Rectangle((X[4], ny - nv * k), W, nv * k, fc='#14853b'))
    ax.text(X[4] + 2.6, ny - nv * k / 2, f"純利益\n{nv:,.0f}", ha='left', va='center', fontsize=13.5, fontweight='bold', linespacing=1.3)
    t, c = yoy(d['net']['yoy']); ax.text(X[4] + 2.6, ny - nv * k / 2 - 4.6 * (S + 1) / 2 - (1 if compact else 0), t, ha='left', va='center', fontsize=12, fontweight='bold', color=c)
    cur = ot - nv * k
    yy = ny - nv * k - 8.5
    # 下段の説明と重ならないよう、営業外・税は中段の右へ
    for r in d['below']:
        hh = r['value'] * k
        band(ax, X[3] + W, cur, cur - hh, X[4], yy, yy - hh, GR, RED)
        ax.add_patch(Rectangle((X[4], yy - hh), W, max(hh, .5), fc=BAR_R))
        t, c = yoy(r['yoy'])
        if r['yoy'] is not None:
            c = DN if r['yoy'] > 0 else UP
        ax.text(X[4] + 2.6, yy - hh / 2, f"{r['name']}  {r['value']:,.0f}", ha='left', va='center', fontsize=12.5, fontweight='bold')
        ax.text(X[4] + 2.6, yy - hh / 2 - 2.5 * S, t, ha='left', va='center', fontsize=11, fontweight='bold', color=c)
        cur -= hh
        yy -= max(hh, .5) + 6.4
    # 販管費の内訳(sga_detail): 販管費の帯から X[4] へ流し、営業外・税の下に積む
    if sga_det:
        s_cur, yy2 = st, min(yy - 4.5, sb - 3.0)
        gap = (yy2 - 14.0 - sum(r['value'] * k for r in sga_det)) / max(len(sga_det) - 1, 1)
        gap = min(max(gap, 3.6), 6.5)
        for r in sga_det:
            hh = r['value'] * k
            band(ax, X[3] + W, s_cur, s_cur - hh, X[4], yy2, yy2 - hh, RED, RED)
            ax.add_patch(Rectangle((X[4], yy2 - hh), W, max(hh, .4), fc=BAR_R))
            t, c = yoy(r['yoy'])
            if r['yoy'] is not None:
                c = DN if r['yoy'] > 0 else UP
            share = r['value'] / sv * 100
            ax.text(X[4] + 2.6, yy2 - hh / 2 + 1.2, f"{r['name']}  {r['value']:,.0f}", ha='left', va='center', fontsize=12, fontweight='bold', color='#222')
            ax.text(X[4] + 2.6, yy2 - hh / 2 - 1.9, f"販管費の{share:.0f}%" + (f"   {t}" if t else ''), ha='left', va='center', fontsize=10, color=c if t else '#666')
            s_cur -= hh
            yy2 -= max(hh, .4) + gap
    for i, n in enumerate([] if compact else d.get('notes', [])):
        ax.text(10, 6 - i * 2.8, '※ ' + n, ha='left', va='center', fontsize=12.5, color='#666')
    fig.savefig(sys.argv[2], facecolor='white')


if __name__ == '__main__':
    main()
