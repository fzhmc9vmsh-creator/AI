#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""投資判断報告書(Oracle)用の図 fig01〜fig12 を data/ の CSV から作成する。
データは加工せず、欠損は欠損のまま描く。"""
import csv
import os
from datetime import datetime

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import font_manager as fm
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm, to_rgb
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
FONT_PATH = '/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf'
fm.fontManager.addfont(FONT_PATH)

# ---- 配色(カテゴリ) ---------------------------------------------------
NAVY = '#1F3A5F'
BLUE = '#2E75B6'
GRAY = '#8C9BAA'
ORANGE = '#D9822B'
RED = '#B23A3A'
GREEN = '#3A8B5C'
INK = '#222B36'      # 本文
MUTED = '#5B6672'    # 注記・補助
GRID = '#E3E7EB'
AXIS = '#9AA5B1'

import logging
logging.getLogger('matplotlib.font_manager').setLevel(logging.ERROR)

plt.rcParams.update({
    'font.family': 'IPAGothic',
    'axes.unicode_minus': False,
    'font.size': 8.5,
    'axes.labelsize': 8.5,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'axes.edgecolor': AXIS,
    'axes.labelcolor': INK,
    'xtick.color': INK,
    'ytick.color': INK,
    'text.color': INK,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.8,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'savefig.facecolor': 'white',
    'legend.fontsize': 8,
})
DPI = 200


# ---- 共通ヘルパー -------------------------------------------------------
def read(name):
    with open(os.path.join(DATA, name), encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def num(s):
    s = (s or '').strip()
    return float('nan') if s == '' else float(s)


def source(fig, text):
    fig.text(0.012, 0.010, text, ha='left', va='bottom', fontsize=6.8,
             color=MUTED, linespacing=1.5)


def save(fig, name):
    path = os.path.join(HERE, name)
    fig.savefig(path, dpi=DPI, bbox_inches='tight', pad_inches=0.12, facecolor='white')
    plt.close(fig)
    print('saved', path)


def style_ax(ax, grid_axis='y'):
    ax.set_axisbelow(True)
    if grid_axis:
        ax.grid(axis=grid_axis, color=GRID, lw=0.7, zorder=0)
    ax.tick_params(length=3, width=0.7, color=AXIS)


def legend_top(ax_or_fig, handles, ncol=None, y=1.02, **kw):
    return ax_or_fig.legend(handles=handles, loc='lower center', bbox_to_anchor=(0.5, y),
                            ncol=ncol or len(handles), frameon=False, fontsize=8,
                            handlelength=1.8, columnspacing=1.6, **kw)


def luminance(rgb):
    r, g, b = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb[:3]]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


# =======================================================================
# 1. OCI 売上 と RPO
# =======================================================================
def fig01():
    rows = read('c01_quarterly_oci_rpo.csv')
    q = [r['quarter'] for r in rows]
    oci = np.array([num(r['oci_rev_busd']) for r in rows])
    yoy = np.array([num(r['oci_yoy_pct']) for r in rows])
    rpo = np.array([num(r['rpo_busd']) for r in rows])
    x = np.arange(len(q))

    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    fig.subplots_adjust(left=0.085, right=0.90, top=0.88, bottom=0.2)
    ax2 = ax.twinx()
    ax2.spines['right'].set_visible(True)
    ax2.spines['right'].set_color(AXIS)

    ax.bar(x, oci, width=0.6, color=BLUE, zorder=2)
    ax.set_ylim(0, 12)
    ax.set_yticks(range(0, 13, 2))
    ax2.set_ylim(0, 720)
    ax2.set_yticks(range(0, 721, 120))
    style_ax(ax)
    ax2.tick_params(length=3, width=0.7, color=AXIS)
    ax2.set_zorder(ax.get_zorder() + 1)
    ax2.patch.set_visible(False)

    # RPO: NaN で線が途切れる(欠損は欠損のまま)
    ax2.plot(x, rpo, color=NAVY, lw=1.8, marker='o', ms=4.6, mec='white', mew=0.8, zorder=5)

    for i, (xi, v, o) in enumerate(zip(x, yoy, oci)):
        # RPO の急な立ち上がり線(Q4 FY25→Q1 FY26)と重ならないよう Q4 FY25 のみ左へずらす
        dx = -0.17 if q[i] == 'Q4 FY25' else 0.0
        ax.text(xi + dx, o + 0.22, f'+{v:.0f}%', ha='center', va='bottom', fontsize=7.2,
                color=INK, zorder=6)

    # 主要点の値ラベル
    ax.text(x[-1], oci[-1] / 2, f'{oci[-1]:.1f}', ha='center', va='center', color='white', fontsize=7.5, zorder=3)
    bbox = dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.85)
    for i in (0, 7, 8, len(q) - 1):
        below = i in (0, 7)   # 棒の内側にある点は下側に表示(前年比ラベルとの重なり回避)
        ax2.annotate(f'{rpo[i]:.0f}', (x[i], rpo[i]), xytext=(0, -7 if below else 7), textcoords='offset points',
                     ha='center', va='top' if below else 'bottom', fontsize=7.5, color=NAVY, fontweight='bold',
                     bbox=bbox, zorder=7)

    # 欠損の注記
    miss = np.where(np.isnan(rpo))[0]
    for i in miss:
        ax2.text(x[i], 255, f'{q[i]}\nRPO 欠損', ha='center', va='bottom', fontsize=7,
                 color=MUTED, zorder=6)

    ax.set_xticks(x)
    ax.set_xticklabels([s.replace(' ', '\n') for s in q], fontsize=7.8)
    ax.set_xlim(-0.6, len(q) - 0.4)
    ax.set_ylabel('OCI 売上(B$、左軸)')
    ax2.set_ylabel('RPO(B$、右軸)')
    legend_top(ax, [Patch(fc=BLUE, label='OCI 売上(棒・左軸、B$)'),
                    Line2D([0], [0], color=NAVY, lw=1.8, marker='o', ms=4.6, label='RPO(折れ線・右軸、B$)')])
    source(fig, '出典: Oracle 決算発表(検索要約経由)。単位: 十億ドル(B$)。期間: Q1 FY24〜Q1 FY27(四半期)。\n'
                '棒の上の%は OCI 売上の前年同期比。RPO の Q3 FY25 は欠損(線を途切れさせて表示)。')
    save(fig, 'fig01_oci_rpo.png')


# =======================================================================
# 2. キャッシュフロー(年度・四半期)
# =======================================================================
def fig02():
    ann = read('c02b_annual_cf.csv')
    qtr = read('c02_quarterly_cf.csv')

    def panel(ax, labels, ocf, capex, fcf, ylim, step, sub, fcf_pad):
        x = np.arange(len(labels))
        w = 0.27
        ax.bar(x - w, ocf, w, color=BLUE, zorder=3)
        ax.bar(x, capex, w, color=NAVY, zorder=3)
        ax.bar(x + w, fcf, w, color=[GREEN if v >= 0 else RED for v in fcf], zorder=3)
        ax.axhline(0, color=INK, lw=0.8, zorder=4)
        for xi, v in zip(x + w, fcf):
            ax.text(xi, v + (fcf_pad if v >= 0 else -fcf_pad), f'{v:.1f}', ha='center',
                    va='bottom' if v >= 0 else 'top', fontsize=6.8, color=INK, zorder=5)
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.set_ylim(*ylim)
        ax.set_yticks(np.arange(ylim[0], ylim[1] + 0.01, step))
        ax.set_xlim(-0.6, len(labels) - 0.4)
        style_ax(ax)
        ax.set_title(sub, loc='left', fontsize=8.5, color=INK, pad=6)
        ax.set_ylabel('B$(十億ドル)')

    fig = plt.figure(figsize=(7.6, 4.0))
    gs = fig.add_gridspec(1, 2, width_ratios=[6, 5], wspace=0.22,
                          left=0.075, right=0.985, top=0.84, bottom=0.2)
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])
    panel(ax1, [r['fiscal_year'] for r in ann],
          [num(r['ocf_busd']) for r in ann], [num(r['capex_busd']) for r in ann],
          [num(r['fcf_busd']) for r in ann], (-30, 60), 10, '年度(FY21〜FY26)', 1.0)
    panel(ax2, [r['quarter'].replace(' ', '\n') for r in qtr],
          [num(r['ocf_busd']) for r in qtr], [num(r['capex_busd']) for r in qtr],
          [num(r['fcf_busd']) for r in qtr], (-15, 30), 5, '四半期(Q1 FY26〜Q1 FY27)', 0.5)
    ax2.set_xticklabels([r['quarter'].replace(' ', '\n') for r in qtr], fontsize=7.5)
    handles = [Patch(fc=BLUE, label='営業CF'), Patch(fc=NAVY, label='Capex(設備投資)'),
               Patch(fc=GREEN, label='FCF(プラス)'), Patch(fc=RED, label='FCF(マイナス)')]
    fig.legend(handles=handles, loc='upper center', bbox_to_anchor=(0.53, 0.995), ncol=4,
               frameon=False, fontsize=8, handlelength=1.4, columnspacing=1.8)
    source(fig, '出典: Oracle 10-K/10-Q(検索要約経由)。単位: 十億ドル(B$)。FCF = 営業CF − Capex(数値は CSV の値)。\n'
                '期間: 年度 FY21〜FY26、四半期 Q1 FY26〜Q1 FY27。左右のパネルで縦軸の目盛りが異なる。')
    save(fig, 'fig02_cashflow.png')


# =======================================================================
# 3. 資本の出し手
# =======================================================================
def fig03():
    rows = read('c03_capital_providers.csv')
    wrap = {
        '社債・借入(残高)': '社債・借入(残高)',
        '株式(2026年 ATM+強制転換優先株)': '株式\n(2026年 ATM+強制転換優先株)',
        '顧客の前払い・持込GPU(累計)': '顧客の前払い・持込GPU\n(累計)',
        '前受収益(残高)': '前受収益(残高)',
        '認識済みリース負債': '認識済みリース負債',
        '未開始リース(15〜19年)': '未開始リース(15〜19年)',
    }
    color_of = lambda who: (NAVY if who.startswith('Oracle') else GRAY if who == '株主'
                            else GREEN if who == '顧客' else ORANGE)
    n = len(rows)
    fig, ax = plt.subplots(figsize=(7.4, 3.9))
    fig.subplots_adjust(left=0.30, right=0.97, top=0.86, bottom=0.22)
    y = np.arange(n)
    for i, r in enumerate(rows):
        v = num(r['amount_busd'])
        off = '簿外' in r['who']
        c = color_of(r['who'])
        if off:
            ax.barh(i, v, height=0.62, fc='#F7E3CC', ec=c, hatch='////', lw=1.0, zorder=3)
        else:
            ax.barh(i, v, height=0.62, color=c, zorder=3)
        ax.text(v + 4, i, f'{v:.1f}', va='center', ha='left', fontsize=8, color=INK, zorder=4)
        if off:
            ax.text(v / 2, i, '簿外(貸借対照表に未計上)', va='center', ha='center', fontsize=8,
                    color=INK, bbox=dict(boxstyle='round,pad=0.25', fc='white', ec='none', alpha=0.9), zorder=5)
    ax.set_yticks(y)
    ax.set_yticklabels([wrap.get(r['provider'], r['provider']) for r in rows], fontsize=8)
    ax.invert_yaxis()
    ax.set_xlim(0, 335)
    ax.set_xlabel('金額(B$、十億ドル)')
    style_ax(ax, 'x')
    ax.spines['left'].set_color(AXIS)
    handles = [Patch(fc=NAVY, label='Oracle 負担(確定債務)'), Patch(fc=GRAY, label='株主'),
               Patch(fc=GREEN, label='顧客'), Patch(fc=ORANGE, label='貸主(開発業者)'),
               Patch(fc='#F7E3CC', ec=ORANGE, hatch='////', label='簿外(未開始リース)')]
    ax.legend(handles=handles, loc='lower center', bbox_to_anchor=(0.36, 1.01), ncol=5, frameon=False,
              fontsize=7.5, handlelength=1.3, columnspacing=1.0)
    source(fig, '出典: 本報告書の分析(各社開示に基づく整理)。単位: 十億ドル(B$)。\n'
                '注: 未開始リース(15〜19年)は貸借対照表に計上されない簿外のコミットメント。色は資本の出し手を表す。')
    save(fig, 'fig03_capital_providers.png')


# =======================================================================
# 4. H100 レンタル単価
# =======================================================================
def fig04():
    rows = read('c04_h100_rental.csv')
    pts = [(datetime.strptime(r['month'], '%Y-%m'), num(r['usd_per_gpu_hour']), r['series'], r['month'])
           for r in rows]
    style = {
        'ハイパースケーラー中央値': dict(color=GRAY, marker='s', ms=6.5),
        'Silicon Data指数': dict(color=BLUE, marker='o', ms=6.5),
        'ネオクラウド指数': dict(color=NAVY, marker='^', ms=7.5),
    }
    series_order = []
    for p in pts:
        if p[2] not in series_order:
            series_order.append(p[2])
    fig, ax = plt.subplots(figsize=(7.4, 4.0))
    fig.subplots_adjust(left=0.085, right=0.975, top=0.87, bottom=0.2)
    style_ax(ax)

    # 系列間の参考接続(定義が異なるため薄い点線)
    for a, b in zip(pts[:-1], pts[1:]):
        if a[2] != b[2]:
            ax.plot([a[0], b[0]], [a[1], b[1]], color='#B8C1CB', lw=1.0, ls=(0, (2, 3)), zorder=2)
    for s in series_order:
        sp = [p for p in pts if p[2] == s]
        st = style[s]
        ax.plot([p[0] for p in sp], [p[1] for p in sp], color=st['color'], lw=1.8, zorder=3)
        ax.plot([p[0] for p in sp], [p[1] for p in sp], color=st['color'], lw=0, marker=st['marker'],
                ms=st['ms'], mec='white', mew=0.9, zorder=4, label=s)

    # 底(2025-12)の強調
    bottom = min((p for p in pts if p[2] == 'ネオクラウド指数'), key=lambda p: p[1])
    ax.axvline(bottom[0], color=ORANGE, lw=1.0, ls=(0, (4, 3)), zorder=1)
    ax.plot([bottom[0]], [bottom[1]], marker='o', ms=15, mfc='none', mec=ORANGE, mew=1.6, zorder=5)
    ax.annotate(f'底: {bottom[3]}\n{bottom[1]:.2f} ドル/時', (bottom[0], bottom[1]),
                xytext=(-62, 34), textcoords='offset points', fontsize=8, color=ORANGE, fontweight='bold',
                ha='center', arrowprops=dict(arrowstyle='-', color=ORANGE, lw=1.0), zorder=6)

    below = {'2025-12': None, '2026-07': (0, -13), '2025-06': (0, 8), '2024-09': (0, 8)}
    for d, v, s, m in pts:
        if m == '2025-12':
            continue
        dx, dy = below.get(m) or (0, 8)
        ax.annotate(f'{v:.2f}', (d, v), xytext=(dx, dy), textcoords='offset points', ha='center',
                    va='bottom' if dy > 0 else 'top', fontsize=7.8, color=INK, zorder=6)

    ax.set_ylim(1.2, 8.6)
    ax.set_yticks(np.arange(2, 9, 1))
    ax.set_xlim(datetime(2023, 10, 15), datetime(2026, 10, 1))
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[3, 6, 9, 12]))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.setp(ax.get_xticklabels(), fontsize=7.5)
    ax.set_ylabel('H100 の GPU 時間単価(ドル/時)')
    legend_top(ax, [Line2D([0], [0], color=style[s]['color'], lw=1.8, marker=style[s]['marker'],
                           ms=style[s]['ms'] - 1, label=s) for s in series_order])
    source(fig, '出典: Silicon Data ほか(S3 調査)。単位: ドル/GPU時間。期間: 2023-12〜2026-08(データのある月のみ)。\n'
                '注: 系列ごとに定義が異なる(ハイパースケーラー中央値 / Silicon Data指数 / ネオクラウド指数)。系列間の点線は参考接続。縦軸は 1.2 ドルから。')
    save(fig, 'fig04_h100_rental.png')


# =======================================================================
# 5. 株価と 5年CDS
# =======================================================================
def fig05():
    pr = read('c05_price_monthly.csv')
    cds = read('c05b_cds.csv')

    def midx(s):
        y, m = int(s[:4]), int(s[5:7])
        return (y - 2025) * 12 + (m - 1)

    x = np.array([midx(r['month']) for r in pr])
    p = np.array([num(r['close_usd']) for r in pr])
    cx = np.array([midx(r['month']) for r in cds])
    cv = np.array([num(r['cds_5y_bp']) for r in cds])
    last = len(pr) - 1

    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    fig.subplots_adjust(left=0.085, right=0.905, top=0.88, bottom=0.2)
    ax2 = ax.twinx()
    ax2.spines['right'].set_visible(True)
    ax2.spines['right'].set_color(AXIS)
    ax.set_ylim(0, 300)
    ax.set_yticks(range(0, 301, 50))
    ax2.set_ylim(0, 240)
    ax2.set_yticks(range(0, 241, 40))
    style_ax(ax)
    ax2.tick_params(length=3, width=0.7, color=AXIS)
    ax2.set_zorder(ax.get_zorder() + 1)
    ax2.patch.set_visible(False)

    # 欠損月
    for xi, v in zip(x, p):
        if np.isnan(v):
            ax.axvspan(xi - 0.45, xi + 0.45, color='#EEF1F4', zorder=0)
            ax.text(xi, 6, '欠損', ha='center', va='bottom', fontsize=7, color=MUTED, zorder=2)

    ax.plot(x, p, color=NAVY, lw=1.7, marker='o', ms=3.6, mec='white', mew=0.6, zorder=4)
    ax.plot([x[last]], [p[last]], marker='D', ms=7, mfc=RED, mec='white', mew=0.9, zorder=6)

    ax2.plot(cx, cv, color=ORANGE, lw=1.7, marker='s', ms=6, mec='white', mew=0.8, zorder=5)
    bbox = dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.85)
    for xi, v in zip(cx, cv):
        ax2.annotate(f'{v:.0f}', (xi, v), xytext=(0, 7), textcoords='offset points', ha='center',
                     va='bottom', fontsize=7.8, color=ORANGE, fontweight='bold', bbox=bbox, zorder=8)

    pk = int(np.nanargmax(p))
    ax.annotate(f'{p[pk]:.2f}', (x[pk], p[pk]), xytext=(0, 6), textcoords='offset points', ha='center',
                va='bottom', fontsize=7.8, color=NAVY, fontweight='bold', zorder=8)
    for i, off in ((np.where(x == midx('2026-05'))[0][0], (0, 6)),
                   (np.where(x == midx('2026-07'))[0][0], (0, -12))):
        ax.annotate(f'{p[i]:.2f}', (x[i], p[i]), xytext=off, textcoords='offset points', ha='center',
                    va='bottom' if off[1] > 0 else 'top', fontsize=7.8, color=NAVY, fontweight='bold', zorder=8)
    ax.annotate(f"{pr[last]['month']}\n{p[last]:.2f}", (x[last], p[last]), xytext=(-16, 10),
                textcoords='offset points', ha='center', va='bottom', fontsize=7.8, color=RED,
                fontweight='bold', zorder=8)

    ticks = list(range(0, 22, 3))
    ax.set_xticks(ticks)
    ax.set_xticklabels([f'{2025 + t // 12}-{t % 12 + 1:02d}' for t in ticks], fontsize=7.8)
    ax.set_xlim(-0.7, 21.7)
    ax.set_ylabel('株価(ドル、左軸)')
    ax2.set_ylabel('5年CDS(bp、右軸)')
    legend_top(ax, [Line2D([0], [0], color=NAVY, lw=1.7, marker='o', ms=3.6, label='株価(月末終値・左軸、ドル)'),
                    Line2D([0], [0], color=ORANGE, lw=1.7, marker='s', ms=5.5, label='5年CDS(右軸、bp)'),
                    Line2D([0], [0], color='none', marker='D', mfc=RED, mec='white', ms=6, label='最新(2026-10-09)')])
    source(fig, '出典: 株価 Digrin 月次(検索要約、要確認)、CDS 報道(ICE 引用)。単位: 株価=ドル、CDS=bp。期間: 2025-01〜2026-10。\n'
                '注: 株価の 2026-06・2026-09 は欠損(線を途切れさせて表示)。最終点は月末ではなく 2026-10-09 の値。')
    save(fig, 'fig05_price_cds.png')


# =======================================================================
# 6. 事業実態EPS 4経路
# =======================================================================
PATHS = [  # key, 表示名, 色
    ('consensus', 'コンセンサス', BLUE),
    ('company', '会社シナリオ', ORANGE),
    ('engine', '事業エンジン', NAVY),
    ('bear', '弱気', RED),
]
MARKERS = {'consensus': 'o', 'company': 's', 'engine': 'D', 'bear': 'v'}


def fig06():
    rows = read('c06_eps_paths_br.csv')
    yrs = [r['year'] for r in rows]
    x = np.arange(len(yrs))
    val = {k: np.array([num(r[k]) for r in rows]) for k, _, _ in PATHS}
    ext_from = {'consensus': yrs.index('FY29'), 'company': yrs.index('FY31')}

    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    fig.subplots_adjust(left=0.085, right=0.975, top=0.88, bottom=0.2)
    ax.axvspan(0.5, len(yrs) + 1.0, color='#F2F4F7', zorder=0)
    ax.text(0.58, 0.97, '予測', transform=ax.get_xaxis_transform(), ha='left', va='top',
            fontsize=8.5, color=MUTED)
    style_ax(ax)
    ax.set_xlim(-0.45, len(yrs) + 1.0)

    for k, name, c in PATHS:
        v = val[k]
        if k == 'engine':
            ax.plot(x, v, color=c, lw=2.8, marker=MARKERS[k], ms=5.5, mec='white', mew=0.8, zorder=6)
            continue
        e = ext_from.get(k, len(yrs))
        # 通常の予測区間(破線)
        ax.plot(x[:e], v[:e], color=c, lw=1.6, ls=(0, (5, 2.5)), zorder=4)
        ax.plot(x[1:e], v[1:e], color=c, lw=0, marker=MARKERS[k], ms=5, mec='white', mew=0.7, zorder=5)
        if e < len(yrs):
            # 延長区間(点線 + 白抜きマーカー)
            ax.plot(x[e - 1:], v[e - 1:], color=c, lw=1.6, ls=(0, (1, 2)), zorder=4)
            ax.plot(x[e:], v[e:], color=c, lw=0, marker=MARKERS[k], ms=5.2, mfc='white', mec=c, mew=1.3, zorder=5)
    # 実績
    ax.plot([0], [val['engine'][0]], marker='o', ms=8, mfc=INK, mec='white', mew=1.0, zorder=8)
    ax.annotate(f"実績 {val['engine'][0]:.2f}", (0, val['engine'][0]), xytext=(0, 9),
                textcoords='offset points', ha='center', va='bottom', fontsize=8, fontweight='bold')

    # 末端ラベル
    for k, name, c in PATHS:
        ax.text(len(yrs) - 1 + 0.18, val[k][-1], f'{name} {val[k][-1]:.1f}', ha='left', va='center',
                fontsize=8, color=INK, fontweight='bold' if k == 'engine' else 'normal', zorder=9)

    ax.set_xticks(x)
    ax.set_xticklabels(yrs)
    ax.set_ylim(0, 30)
    ax.set_yticks(range(0, 31, 5))
    ax.set_ylabel('事業実態EPS(SBC控除後、ドル/株)')
    h = [Line2D([0], [0], color=c, lw=2.8 if k == 'engine' else 1.6, ls='-' if k == 'engine' else (0, (4, 2)),
                marker=MARKERS[k], ms=5, label=n) for k, n, c in PATHS]
    h.append(Line2D([0], [0], color=MUTED, lw=1.4, ls=(0, (1, 2)), marker='o', mfc='white', mec=MUTED, ms=5,
                    label='延長値(白抜き・点線)'))
    legend_top(ax, h, ncol=5)
    source(fig, '出典: 本報告書の分析(事業エンジン・コンセンサス・会社シナリオ・弱気の4経路)。単位: ドル/株(事業実態EPS、SBC 控除後)。期間: FY26A〜FY32。\n'
                '注: FY26A は実績、FY27 以降は予測。コンセンサスの FY29 以降と会社シナリオの FY31 以降は延長値。')
    save(fig, 'fig06_eps_paths.png')


# =======================================================================
# 7. 年度別 適正株価(中央値)
# =======================================================================
def fig07():
    rows = read('c07_fairprice_path.csv')
    yrs = [r['year'] for r in rows]
    x = np.arange(len(yrs))
    val = {k: np.array([num(r[k]) for r in rows]) for k, _, _ in PATHS}
    cur = 141.40

    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    fig.subplots_adjust(left=0.085, right=0.975, top=0.88, bottom=0.2)
    style_ax(ax)
    ax.axhline(cur, color=GRAY, lw=1.3, ls=(0, (1, 2)), zorder=2)
    ax.text(len(yrs) - 1.6, cur + 5, f'現在株価 {cur:.2f} ドル', ha='right', va='bottom', fontsize=8,
            color=MUTED, fontweight='bold', zorder=3)
    for k, name, c in PATHS:
        v = val[k]
        if k == 'engine':
            ax.plot(x, v, color=c, lw=2.8, marker=MARKERS[k], ms=5.5, mec='white', mew=0.8, zorder=6)
        else:
            ax.plot(x, v, color=c, lw=1.6, ls=(0, (5, 2.5)), marker=MARKERS[k], ms=5, mec='white', mew=0.7, zorder=4)
        ax.text(len(yrs) - 1 + 0.15, v[-1], f'{name} {v[-1]:.0f}', ha='left', va='center', fontsize=8,
                fontweight='bold' if k == 'engine' else 'normal', zorder=9)
        ax.annotate(f'{v[0]:.0f}', (0, v[0]), xytext=(-8, 0), textcoords='offset points', ha='right', va='center',
                    fontsize=7.2, color=MUTED)
    ax.set_xticks(x)
    ax.set_xticklabels(yrs)
    ax.set_xlim(-0.55, len(yrs) + 0.9)
    ax.set_ylim(0, 420)
    ax.set_yticks(range(0, 421, 60))
    ax.set_ylabel('適正株価(中央値、ドル/株)')
    h = [Line2D([0], [0], color=c, lw=2.8 if k == 'engine' else 1.6, ls='-' if k == 'engine' else (0, (4, 2)),
                marker=MARKERS[k], ms=5, label=n) for k, n, c in PATHS]
    h.append(Line2D([0], [0], color=GRAY, lw=1.3, ls=(0, (1, 2)), label='現在株価'))
    legend_top(ax, h, ncol=5)
    source(fig, '出典: 本報告書の分析(4経路別の適正株価、中央値)。単位: ドル/株。期間: FY27〜FY32(すべて予測に基づく推計)。\n'
                '注: 現在株価は 141.40 ドル(水平の点線)。弱気の FY27 は SOTP 弱気と弱気EPS×13倍の平均(84)、FY28 以降は PER 下限 14倍。')
    save(fig, 'fig07_fairprice_path.png')


# =======================================================================
# 8. トルネード図
# =======================================================================
def fig08():
    rows = read('c08_tornado.csv')
    base = 139.6
    pct_vars = {'コアの資本コスト', 'AI容量の利益率(EBIT)', 'コアの成長率(5年)', 'AI の資本コスト'}

    def fmt(name, v):
        if name in pct_vars:
            return f'{float(v) * 100:g}%'
        return v

    items = []
    for r in rows:
        items.append(dict(name=r['variable'], lc=fmt(r['variable'], r['low_case']),
                          hc=fmt(r['variable'], r['high_case']),
                          lo=float(r['value_low']), hi=float(r['value_high'])))
    items.sort(key=lambda d: -round(d['hi'] - d['lo'], 1))  # swing 降順(同値は CSV 順)
    namewrap = {'経済的寿命×更新単価(契約後の残存価格比 pr と年数)': '経済的寿命×更新単価\n(契約後の残存価格比 pr と年数)'}
    n = len(items)

    fig, ax = plt.subplots(figsize=(7.4, 5.6))
    fig.subplots_adjust(left=0.37, right=0.97, top=0.89, bottom=0.17)
    style_ax(ax, 'x')
    ax.set_xlim(100, 162)
    ax.set_ylim(n - 0.5, -1.2)
    for i, d in enumerate(items):
        ax.barh(i, d['lo'] - base, left=base, height=0.56, color=RED, zorder=3)
        ax.barh(i, d['hi'] - base, left=base, height=0.56, color=GREEN, zorder=3)
        ax.text(d['lo'] - 0.6, i, f"{d['lo']:.1f}", ha='right', va='center', fontsize=8, zorder=4)
        ax.text(d['hi'] + 0.6, i, f"{d['hi']:.1f}", ha='left', va='center', fontsize=8, zorder=4)
        ax.annotate(namewrap.get(d['name'], d['name']), xy=(0, i), xycoords=('axes fraction', 'data'),
                    xytext=(-8, 1), textcoords='offset points', ha='right', va='bottom', fontsize=8,
                    color=INK, annotation_clip=False, linespacing=1.15)
        ax.annotate(f"{d['lc']} → {d['hc']}", xy=(0, i), xycoords=('axes fraction', 'data'),
                    xytext=(-8, -1), textcoords='offset points', ha='right', va='top', fontsize=6.9,
                    color=MUTED, annotation_clip=False)
    ax.plot([base, base], [-0.5, n - 0.5], color=NAVY, lw=1.6, zorder=5)
    ax.text(base, -0.62, f'ベース {base} ドル', ha='center', va='bottom', fontsize=8.5, color=NAVY, fontweight='bold',
            bbox=dict(boxstyle='square,pad=0.2', fc='white', ec='none'), zorder=6)
    ax.set_yticks([])
    ax.spines['left'].set_visible(False)
    ax.set_xlabel('1株当たり価値(ドル)')
    legend_top(ax, [Patch(fc=RED, label='下振れ'), Patch(fc=GREEN, label='上振れ')], y=1.0)
    source(fig, '出典: 本報告書の分析(感応度分析)。単位: ドル/株。変数は 1株価値の変動幅(swing)の大きい順。\n'
                '注: 変数名の下の灰色の文字は「下振れ条件 → 上振れ条件」。ベースと同値の端は棒が現れない。')
    save(fig, 'fig08_tornado.png')


# =======================================================================
# 9. ヒートマップ(pr × m)
# =======================================================================
def fig09():
    rows = read('c09_heatmap_pr_m.csv')
    cols = [k for k in rows[0].keys() if k != 'pr\\m']
    prs = [float(r['pr\\m']) for r in rows]
    ms = [float(c) for c in cols]
    Z = np.array([[float(r[c]) for c in cols] for r in rows])
    cur = 141.4

    cmap = LinearSegmentedColormap.from_list('div', [RED, '#FFFFFF', GREEN])
    norm = TwoSlopeNorm(vmin=Z.min(), vcenter=cur, vmax=Z.max())
    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    fig.subplots_adjust(left=0.19, right=0.84, top=0.95, bottom=0.2)
    im = ax.imshow(Z, cmap=cmap, norm=norm, origin='lower', aspect='auto')
    for i in range(Z.shape[0]):
        for j in range(Z.shape[1]):
            rgb = cmap(norm(Z[i, j]))
            col = 'white' if luminance(rgb) < 0.28 else INK
            ax.text(j, i, f'{Z[i, j]:.1f}', ha='center', va='center', fontsize=9, color=col)
    # 格子(白)
    ax.set_xticks(np.arange(-0.5, Z.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-0.5, Z.shape[0], 1), minor=True)
    ax.grid(which='minor', color='white', lw=1.5)
    ax.tick_params(which='minor', length=0)
    ax.grid(which='major', visible=False)
    # ベース(139.6)のセルを太枠
    bi = [i for i in range(Z.shape[0]) for j in range(Z.shape[1]) if abs(Z[i, j] - 139.6) < 1e-9]
    bj = [j for i in range(Z.shape[0]) for j in range(Z.shape[1]) if abs(Z[i, j] - 139.6) < 1e-9]
    if bi:
        ax.add_patch(Rectangle((bj[0] - 0.5, bi[0] - 0.5), 1, 1, fill=False, ec=NAVY, lw=2.4, zorder=5))
    ax.set_xticks(range(len(ms)))
    ax.set_xticklabels([f'{m * 100:g}%' for m in ms])
    ax.set_yticks(range(len(prs)))
    ax.set_yticklabels([f'{p:.1f}' for p in prs])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xlabel('AI容量のEBIT利益率')
    ax.set_ylabel('契約後の残存価格比(当初単価比)')
    cax = fig.add_axes([0.87, 0.2, 0.025, 0.75])
    cb = fig.colorbar(im, cax=cax)
    ticks = [110, 120, 130, cur, 150, 160, 170]
    cb.set_ticks(ticks)
    cb.set_ticklabels(['110', '120', '130', f'{cur} 現在株価', '150', '160', '170'], fontsize=7.5)
    cb.outline.set_visible(False)
    cb.ax.tick_params(length=2)
    cb.set_label('1株価値(ドル)', fontsize=8, labelpad=10)
    source(fig, '出典: 本報告書の分析(感応度分析)。単位: ドル/株(1株価値)。行=契約後の残存価格比、列=AI容量のEBIT利益率。\n'
                '注: 白=現在株価 141.4 ドル付近、緑=上回る、赤=下回る。紺の太枠=ベース(139.6 ドル)。')
    save(fig, 'fig09_heatmap.png')


# =======================================================================
# 10. エントリー価格帯
# =======================================================================
def fig10():
    rows = read('c10_entry.csv')
    d = {r['item']: float(r['usd']) for r in rows}
    L = d['弱気 L']
    Z1 = d['即エントリー上限 Z1']
    Z2 = d['分割エントリー上限 Z2']
    B = d['ベース B(事業エンジン)']
    P = d['現在株価']
    C = d['コンセンサス経路']
    U = d['強気 U(会社シナリオ)']
    XMAX = 220

    fig, ax = plt.subplots(figsize=(7.4, 3.7))
    fig.subplots_adjust(left=0.04, right=0.97, top=0.97, bottom=0.25)
    ax.set_xlim(0, XMAX)
    ax.set_ylim(0.3, 9.6)
    for s in ('left', 'right', 'top'):
        ax.spines[s].set_visible(False)
    ax.set_yticks([])
    ax.set_xticks(range(0, XMAX + 1, 20))
    ax.tick_params(axis='x', length=3, color=AXIS)
    ax.set_xlabel('株価(ドル)')

    y0, y1 = 4.0, 6.0
    ax.add_patch(Rectangle((0, y0), Z1, y1 - y0, fc='#BFDDCB', ec='none', zorder=1))
    ax.add_patch(Rectangle((Z1, y0), Z2 - Z1, y1 - y0, fc='#F4E4A6', ec='none', zorder=1))
    ax.add_patch(Rectangle((Z2, y0), XMAX - Z2, y1 - y0, fc='#DDE2E7', ec='none', zorder=1))
    for xb in (Z1, Z2):
        ax.plot([xb, xb], [y0, y1], color='white', lw=1.6, zorder=2)
    ax.text(Z1 / 2, 5, '即エントリー圏\n(Z1 以下)', ha='center', va='center', fontsize=9, color='#1E5A3A', fontweight='bold')
    ax.text((Z1 + Z2) / 2, 5, '分割\nエントリー圏\n(Z1〜Z2)', ha='center', va='center', fontsize=7.2,
            color='#6B5A10', fontweight='bold', linespacing=1.2)
    ax.text((Z2 + XMAX) / 2 + 12, 5, '見送り圏\n(Z2 超)', ha='center', va='center', fontsize=9, color=MUTED, fontweight='bold')

    # (値, ラベル, 上/下, 配置, 色)
    pts = [
        (L, '弱気 L', 'up', 'right', INK),
        (Z1, '即エントリー\n上限 Z1', 'down', 'right', INK),
        (Z2, '分割エントリー\n上限 Z2', 'up', 'right', INK),
        (B, 'ベース B\n(事業エンジン)', 'down', 'right', INK),
        (P, '現在株価', 'up', 'left', RED),
        (C, 'コンセンサス\n経路', 'down', 'left', INK),
        (U, '強気 U\n(会社シナリオ)', 'up', 'center', INK),
    ]
    for v, lab, ud, ha, col in pts:
        isP = col == RED
        if ud == 'up':
            yb, ys, yt, va = y1, y1 + 1.35, y1 + 1.45, 'bottom'
        else:
            yb, ys, yt, va = y0, y0 - 1.35, y0 - 1.45, 'top'
        ax.plot([v, v], [yb, ys], color=col if isP else '#6B7785', lw=1.3 if isP else 0.9, zorder=3)
        ax.plot([v], [yb], marker='o', ms=10 if isP else 6.5, mfc=col if isP else NAVY, mec='white', mew=1.2, zorder=6)
        dx = {'left': 0.9, 'right': -0.9, 'center': 0}[ha]
        ax.text(v + dx, yt, f'{lab}\n{v:.1f}', ha=ha, va=va, fontsize=8.8 if isP else 8,
                color=col, fontweight='bold' if isP else 'normal', linespacing=1.25, zorder=7)
    ax.plot([P, P], [y0 - 0.25, y1 + 0.25], color=RED, lw=2.0, zorder=5)
    source(fig, '出典: 本報告書の分析(エントリー価格帯)。単位: ドル/株。範囲: 0〜220 ドル。\n'
                '注: 緑=Z1 以下(即エントリー圏)、黄=Z1〜Z2(分割エントリー圏)、灰=Z2 超(見送り圏)。赤=現在株価。')
    save(fig, 'fig10_entry_zones.png')


# =======================================================================
# 11. SOTP ウォーターフォール
# =======================================================================
def fig11():
    rows = read('c11_sotp_waterfall.csv')
    cur = 141.4
    lab_map = {
        'コア事業(DB保守・SaaS・非AIクラウド)': 'コア事業\n(DB保守・SaaS・\n非AIクラウド)',
        'AI 稼働中容量': 'AI\n稼働中容量',
        'AI 契約済み・未建設': 'AI\n契約済み・\n未建設',
        'AI 建設中(支出済み)': 'AI 建設中\n(支出済み)',
        'AI 未契約の成長': 'AI\n未契約の成長',
        '顧客前払い(金融要素)': '顧客前払い\n(金融要素)',
        '純有利子負債・金融リース・優先株': '純有利子負債・\n金融リース・\n優先株',
        '1株当たり価値': '1株当たり\n価値',
    }
    comps = [r['component'] for r in rows]
    vals = [num(r['usd_per_share']) for r in rows]
    n = len(rows)
    fig, ax = plt.subplots(figsize=(7.4, 4.3))
    fig.subplots_adjust(left=0.085, right=0.93, top=0.95, bottom=0.25)
    style_ax(ax)
    cum = 0.0
    prev_level = None
    for i, (c, v) in enumerate(zip(comps, vals)):
        if i == 0:
            ax.bar(i, v, width=0.6, color=BLUE, zorder=3)
            ax.text(i, v - 3, f'{v:.1f}', ha='center', va='top', color='white', fontsize=8.5, fontweight='bold', zorder=5)
            cum = v
            level = cum
        elif i == n - 1:
            ax.bar(i, v, width=0.6, color=NAVY, zorder=3)
            ax.text(i, v - 3, f'{v:.1f}', ha='center', va='top', color='white', fontsize=8.5, fontweight='bold', zorder=5)
            level = None
            if prev_level is not None:
                ax.plot([i - 1 + 0.3, i - 0.3], [prev_level, prev_level], color=AXIS, lw=0.8, zorder=2)
        else:
            if v >= 0:
                ax.bar(i, v, bottom=cum, width=0.6, color=BLUE, zorder=3)
                top = cum + v
            else:
                ax.bar(i, -v, bottom=cum + v, width=0.6, color=RED, zorder=3)
                top = cum
            ax.plot([i - 1 + 0.3, i - 0.3], [cum, cum], color=AXIS, lw=0.8, zorder=2)
            sign = '+' if v >= 0 else '-'
            ax.text(i, top + 2.5, f'{sign}{abs(v):.1f}', ha='center', va='bottom', fontsize=8.5,
                    color=INK if v >= 0 else RED, fontweight='bold', zorder=5)
            cum += v
            level = cum
        prev_level = level
    ax.axhline(cur, color=GRAY, lw=1.3, ls=(0, (1, 2)), zorder=1)
    ax.text(n - 0.3, cur + 3, f'現在株価\n{cur} ドル', ha='left', va='bottom', fontsize=8, color=MUTED, fontweight='bold')
    ax.set_xticks(range(n))
    ax.set_xticklabels([lab_map.get(c, c) for c in comps], fontsize=7.6, linespacing=1.2)
    ax.set_xlim(-0.6, n + 0.7)
    ax.set_ylim(0, 200)
    ax.set_yticks(range(0, 201, 25))
    ax.set_ylabel('1株当たり価値(ドル)')
    ax.tick_params(axis='x', length=0)
    source(fig, '出典: 本報告書の分析(部分の合計 SOTP)。単位: ドル/株。青=加算、赤=減算、紺=合計(1株当たり価値)。\n'
                '注: 各項目は四捨五入のため、積み上げと合計は一致しない場合がある。点線は現在株価 141.4 ドル。')
    save(fig, 'fig11_sotp_waterfall.png')


# =======================================================================
# 12. 売上構成(事業エンジン経路)
# =======================================================================
def fig12():
    rows = read('c12_revenue_mix_engine.csv')
    yrs = [r['year'] for r in rows]
    series = [
        ('software', 'ソフトウェア(保守・ライセンス)', GRAY),
        ('saas', 'SaaS', GREEN),
        ('oci_nonai', '非AIクラウド基盤', BLUE),
        ('oci_ai', 'AIクラウド基盤', NAVY),
        ('hw_services', 'ハード・サービス', ORANGE),
    ]
    x = np.arange(len(yrs))
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    fig.subplots_adjust(left=0.085, right=0.74, top=0.95, bottom=0.2)
    style_ax(ax)
    ax.axvspan(0.5, len(yrs) - 0.4, color='#F2F4F7', zorder=0)
    bottom = np.zeros(len(yrs))
    for key, name, c in series:
        v = np.array([num(r[key]) for r in rows])
        bars = ax.bar(x, v, bottom=bottom, width=0.62, color=c, edgecolor='white', linewidth=1.0, zorder=3)
        if key in ('oci_ai', 'oci_nonai'):
            bars[0].set_hatch('////')   # FY26A の AI/非AI 分割は推定
            bars[0].set_edgecolor('white')
        if key == 'oci_ai':
            for xi, vi, bi in zip(x, v, bottom):
                if vi >= 12:
                    ax.text(xi, bi + vi / 2, f'{vi:.1f}', ha='center', va='center', color='white', fontsize=7.8,
                            fontweight='bold', zorder=6)
        bottom = bottom + v
    for xi, t in zip(x, bottom):
        ax.text(xi, t + 3, f'{t:.1f}', ha='center', va='bottom', fontsize=8, fontweight='bold', zorder=6)
    ax.text(0, bottom[0] + 20, '実績\n(AI/非AIの\n分割は推定\n=斜線部)', ha='center', va='bottom', fontsize=7.2,
            color=MUTED, linespacing=1.25)
    ax.text(0.58, 0.985, '事業エンジン経路の予測', transform=ax.get_xaxis_transform(), ha='left', va='top',
            fontsize=8.2, color=MUTED)
    ax.set_xticks(x)
    ax.set_xticklabels(yrs)
    ax.set_xlim(-0.6, len(yrs) - 0.4)
    ax.set_ylim(0, 260)
    ax.set_yticks(range(0, 251, 50))
    ax.set_ylabel('売上(B$、十億ドル)')
    handles = [Patch(fc=c, label=n) for _, n, c in series][::-1]
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1.02, 0.55), frameon=False, fontsize=8,
              handlelength=1.4, labelspacing=0.9)
    source(fig, '出典: 本報告書の分析(事業エンジン経路)。単位: 十億ドル(B$)。期間: FY26A〜FY32。柱の上の数値は5系列の合計。\n'
                '注: FY26A は実績(AI/非AI の分割は推定)、FY27 以降は事業エンジン経路の予測。')
    save(fig, 'fig12_revenue_mix.png')


if __name__ == '__main__':
    for f in (fig01, fig02, fig03, fig04, fig05, fig06, fig07, fig08, fig09, fig10, fig11, fig12):
        f()
