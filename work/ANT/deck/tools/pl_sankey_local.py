#!/usr/bin/env python3
"""pl_sankey.py(スキル)の配色・帯の描き方を写し、営業損失(費用が粗利を上回る)と列ごとの配置を扱えるようにした局所版。
使い方: python3 pl_sankey_local.py 入力.json 出力.png  (--compact は常に有効の扱い: 幅 w×高さ h インチで描き、貼る大きさと同じ)
入力: w,h(インチ), cols[{x(中心インチ), top_from(任意: ノード id の上端に揃える)}], nodes[{id,col,name,value,line2,color(gray|green|red),label(left|right|in),hatch(下の赤字分の値),oneline,dy}], links[[src,dst,value]]
出力: PNG と、<出力>.layout.json(各ノードの棒の位置、インチ)"""
import json, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from matplotlib import font_manager

for f in font_manager.findSystemFonts():
    if 'ipag.ttf' in f or 'ipagp.ttf' in f:
        font_manager.fontManager.addfont(f)
plt.rcParams['font.family'] = ['IPAPGothic', 'IPAGothic', 'Yu Gothic', 'Meiryo', 'sans-serif']
BAND = {'gray': '#d3d4d6', 'green': '#a8e3b4', 'red': '#eab0b0'}
BAR = {'gray': '#606166', 'green': '#1a7f4b', 'red': '#d92b2b'}


def band(ax, x0, y0t, y0b, x1, y1t, y1b, col, n=40):
    t = np.linspace(0, 1, n)
    s = t * t * (3 - 2 * t)
    xs = x0 + (x1 - x0) * t
    ax.fill_between(xs, y0b + (y1b - y0b) * s, y0t + (y1t - y0t) * s, color=col, linewidth=0.4, edgecolor=col)


def main():
    d = json.load(open(sys.argv[1], encoding='utf-8'))
    W, H = d['w'], d['h']
    fig = plt.figure(figsize=(W, H), dpi=250)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis('off')
    BW, gap, pad = d.get('bar_w', 0.11), d.get('gap', 0.14), d.get('pad', 0.12)
    nodes = {n['id']: n for n in d['nodes']}
    ncols = len(d['cols'])
    # 縮尺: 各列の(値の合計 + 隙間)が高さに収まる最大の k
    k = 1e9
    for c in range(ncols):
        ns = [n for n in d['nodes'] if n['col'] == c]
        tot = sum(n['value'] for n in ns)
        k = min(k, (H - 2 * pad - gap * (len(ns) - 1) - d.get('reserve', 0)) / tot)
    for c, spec in enumerate(d['cols']):
        ns = [n for n in d['nodes'] if n['col'] == c]
        hs = sum(n['value'] * k for n in ns) + gap * (len(ns) - 1)
        if 'top_from' in spec:
            y = nodes[spec['top_from']]['y'] + spec.get('top_off', 0)
        else:
            y = (H - hs) / 2 + spec.get('shift', 0)
        for n in ns:
            n['y'] = y + n.get('dy', 0); n['h'] = n['value'] * k; n['x'] = spec['x']
            y += n['h'] + gap
    # 帯
    outc = {i: n['y'] for i, n in nodes.items()}
    inc = dict(outc)
    for i in nodes: nodes[i]['_o'] = nodes[i]['y']; nodes[i]['_i'] = nodes[i]['y']
    links = sorted(d['links'], key=lambda l: (nodes[l[0]]['col'], nodes[l[1]]['y']))
    for s_, t_, v in links:
        a, b = nodes[s_], nodes[t_]
        hh = v * k
        band(ax, a['x'] + BW / 2, a['_o'], a['_o'] + hh, b['x'] - BW / 2, b['_i'], b['_i'] + hh, BAND[b['color']])
        a['_o'] += hh; b['_i'] += hh
    lay = {}
    for n in d['nodes']:
        x0 = n['x'] - BW / 2
        ax.add_patch(Rectangle((x0, n['y']), BW, n['h'], fc=BAR[n['color']], ec='none'))
        if n.get('hatch'):
            hh = n['hatch'] * k
            ax.add_patch(Rectangle((x0, n['y'] + n['h'] - hh), BW, hh, fc='white', ec=BAR['red'], hatch='////', lw=0.8))
        lay[n['id']] = {'x': n['x'], 'top': n['y'], 'bot': n['y'] + n['h'], 'x0': x0, 'x1': x0 + BW}
        mid = n['y'] + n['h'] / 2
        if n.get('hatch'):
            mid = n['y'] + (n['h'] - n['hatch'] * k) / 2
            ax.text(x0 + BW + 0.07, n['y'] + n['h'] - n['hatch'] * k / 2, n['hatch_label'], ha='left', va='center',
                    fontsize=d.get('fs', 9) + 0.5, color='#b01c1c', fontweight='bold')
        fs = d.get('fs', 9)
        txt1, txt2 = n['name'], n.get('line2', '')
        side = n.get('label', 'right')
        if side == 'left':
            tx, ha = x0 - 0.07, 'right'
        else:
            tx, ha = x0 + BW + 0.07, 'left'
        bbox = dict(boxstyle='square,pad=0.08', fc='white', ec='none', alpha=0.78) if side != 'left' else None
        col = n.get('txtcolor', '#222')
        if n.get('oneline'):
            ax.text(tx, mid, f"{txt1}  {txt2}", ha=ha, va='center', fontsize=fs, fontweight='bold', color=col, bbox=bbox)
        else:
            ax.text(tx, mid, f"{txt1}\n{txt2}", ha=ha, va='center', fontsize=fs, color=col, linespacing=1.25, bbox=bbox,
                    fontweight='bold')
    fig.savefig(sys.argv[2], facecolor='white')
    json.dump(lay, open(sys.argv[2] + '.layout.json', 'w'), ensure_ascii=False, indent=1)


main()
