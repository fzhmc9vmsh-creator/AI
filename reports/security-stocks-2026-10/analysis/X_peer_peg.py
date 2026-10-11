"""同一基準ピアPEG表(経路a)の計算。入力は data/*.md と統括の検証検索(2026-10-11)。"""
import sys
sys.path.insert(0, '/home/user/AI/reports/security-stocks-2026-10/build')
import valuation_lib as vl

T = 0.22   # 税率(共通基準)
D = 0.01   # SBC 以外の要因による将来株数の増加率は 0 とし、コンセンサスの株数増加を年1%と仮定(共通基準 §3 追記)

# price: 2026-10-09 終値 / dil: 直近四半期の希薄化後株数(百万) / eps: コンセンサス調整後EPS(会計年度順)
# rev: コンセンサス売上(US$ mn) / sbc_ratio: 直近通期 SBC÷売上
co = {
 'PANW': dict(price=418.78, dil=836, fy=['FY27(7月)','FY28','FY29'], eps=[4.19,4.88,5.45], rev=[14170,16230,17290], sbc_ratio=1712/11480, fcf_ttm=None),
 'CRWD': dict(price=275.04, dil=1042, fy=['FY27(1月)','FY28'], eps=[1.26,1.61], rev=[5993,7335], sbc_ratio=1130.6/4810),
 'FTNT': dict(price=194.75, dil=734, fy=['FY26(12月)','FY27','FY28'], eps=[3.51,3.87,4.41], rev=[8100,None,None], sbc_ratio=279.5/6800),
 'NET':  dict(price=360.93, dil=372, fy=['FY26(12月)','FY27','FY28','FY29'], eps=[1.26,1.67,2.2,2.7], rev=[2867,None,None,None], sbc_ratio=451.5/2167.9),
 'ZS':   dict(price=233.73, dil=170, fy=['FY27(7月)','FY28'], eps=[4.91,5.60], rev=[3930,4580], sbc_ratio=841.6/3352.6),
 'OKTA': dict(price=232.13, dil=178.8, fy=['FY27(1月)','FY28','FY29'], eps=[3.93,4.36,4.89], rev=[3220,None,None], sbc_ratio=544/2920),
}
rows = []
for t, c in co.items():
    e = c['eps']; n = len(e) - 1
    g = vl.cagr(e[0], e[-1], n)
    per1 = c['price'] / e[0]
    peg = per1 / (g * 100)
    sbc_ps = c['sbc_ratio'] * c['rev'][0] * (1 - T) / c['dil']
    beps = e[0] - sbc_ps
    rows.append((t, c['fy'][0], e[0], per1, g, n, peg, c['sbc_ratio'], sbc_ps, beps, c['price'] / beps if beps > 0 else float('nan'), beps / e[0]))
print('| 銘柄 | 基準年度 | 調整後EPS(FY+1) | PER(調整後) | 調整後EPS CAGR | 期間(年) | PEG(調整後) | SBC/売上 | SBC税引後/株(FY+1) | 事業実態EPS(FY+1、SBC比率一定) | PER(事業実態) | 事業実態EPS÷調整後EPS |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|')
for r in rows:
    print(f'| {r[0]} | {r[1]} | {r[2]:.2f} | {r[3]:.1f} | {r[4]*100:.1f}% | {r[5]} | {r[6]:.2f} | {r[7]*100:.1f}% | {r[8]:.2f} | {r[9]:.2f} | {r[10]:.0f} | {r[11]*100:.0f}% |')
# 低成長ピア(調整後EPS基準、FY+1 と FY+2 があるもの)
peers = {'CHKP': (137.18, [10.44], None), 'AKAM': (106.95, [6.64, 6.85], None), 'TENB': (41.59, [1.95], None), 'QLYS': (202.42, [7.31], None)}
print()
print('| ピア | 株価 | EPS(FY+1) | PER | EPS成長(入手範囲) | PEG |')
print('|---|---|---|---|---|---|')
for t, (p, e, _) in peers.items():
    per = p / e[0]
    if len(e) > 1:
        g = e[1] / e[0] - 1
        print(f'| {t} | {p} | {e[0]} | {per:.1f} | {g*100:.1f}%(1年) | {per/(g*100):.1f} |')
    else:
        print(f'| {t} | {p} | {e[0]} | {per:.1f} | 欠損 | 算出不可 |')
