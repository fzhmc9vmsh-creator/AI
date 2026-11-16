#!/usr/bin/env python3
"""eWeLL 事業エンジン(5年後モデル)。売上 = 平均稼働ST × 顧客単価(リカーリング・千円/月) × 12 + 非リカーリング。
契約ST = 前年末 + 新規獲得 − 解約率 × 前年末。費用は原価(労務・外注/サーバー・その他)と販管費を売上比で置く。
出力: model.json(3シナリオ×年度)と、感応度用の単一変数の振れ(sens)。株価は使わない(事前登録)。"""
import json, copy

SHARES = 15.131539          # 百万株(2026年9月末、自己株除く) facts: shares.sep26
TAX = 0.305
ACTIVE = 0.961              # 稼働ST ÷ 契約ST(3Q 2026: 3,695 ÷ 3,843)
Y = [2026, 2027, 2028, 2029, 2030]

BASE = dict(
    adds={2027: 660, 2028: 660, 2029: 660, 2030: 660},      # 新規獲得(件/年)= 業界の新規開設 約2,450 × 獲得率 約27%
    churn={2027: .053, 2028: .053, 2029: .053, 2030: .053},  # 解約率(年、前年末比)= 他社切替 2.6% + 廃業等 2.7%
    arpu={2026: 91.9, 2027: 98.0, 2028: 102.5, 2029: 106.6, 2030: 110.3},
    nonrec_g=.08,
    gm={2026: .762, 2027: .762, 2028: .765, 2029: .765, 2030: .765},
    sga={2026: .304, 2027: .302, 2028: .300, 2029: .295, 2030: .295},
)
BEAR = copy.deepcopy(BASE)
BEAR.update(adds={2027: 600, 2028: 560, 2029: 540, 2030: 520}, churn={y: .060 for y in Y[1:]},
            arpu={2026: 91.9, 2027: 95.5, 2028: 98.0, 2029: 100.5, 2030: 103.0},
            gm={2026: .762, 2027: .745, 2028: .740, 2029: .740, 2030: .740}, sga={y: .305 for y in Y})
BULL = copy.deepcopy(BASE)
BULL.update(adds={2027: 720, 2028: 760, 2029: 800, 2030: 820}, churn={y: .048 for y in Y[1:]},
            arpu={2026: 91.9, 2027: 99.5, 2028: 106.0, 2029: 112.0, 2030: 117.0},
            gm={2026: .762, 2027: .770, 2028: .775, 2029: .775, 2030: .775},
            sga={2026: .304, 2027: .298, 2028: .292, 2029: .290, 2030: .290})


def run(a):
    st = {2025: 3501, 2026: 3950}            # 2026年末は 3Q末 3,843 + 4Q の純増 約107(3Q と同じ)
    for y in Y[1:]:
        st[y] = round(st[y - 1] + a['adds'][y] - a['churn'][y] * st[y - 1])
    nonrec = {2026: 215.0}
    for y in Y[1:]:
        nonrec[y] = nonrec[y - 1] * (1 + a['nonrec_g'])
    out = {}
    for y in Y:
        if y == 2026:
            rev = 4210.0                      # 9か月実績 3,067.6 + 4Q 約1,142(3Q 1,076 + 法定研修・AIルートの増分)
        else:
            act = (st[y - 1] + st[y]) / 2 * ACTIVE
            rev = act * a['arpu'][y] * 12 / 1000 + nonrec[y]
        gp = rev * a['gm'][y]
        op = gp - rev * a['sga'][y]
        nonop = 12 + 4 * (y - 2026)           # 受取利息(現預金 約30〜50億円 × 0.4〜0.6%)
        net = (op + nonop) * (1 - TAX)
        out[y] = dict(stations=st[y], arpu=a['arpu'][y], revenue=round(rev, 1), gross=round(gp, 1), op=round(op, 1),
                      opm=round(op / rev * 100, 1), net=round(net, 1), eps=round(net / SHARES, 2))
    return out


def main():
    res = {k: run(v) for k, v in dict(bear=BEAR, base=BASE, bull=BULL).items()}
    # 単一変数の振れ(基準に対し、その変数だけ弱気/強気に替える)。ありうる振れ幅 = 弱気・強気シナリオの値
    sens = {}
    for name, keys in dict(stations=['adds', 'churn'], arpu=['arpu'], margin=['gm', 'sga']).items():
        for side, src in dict(down=BEAR, up=BULL).items():
            a = copy.deepcopy(BASE)
            for k in keys:
                a[k] = copy.deepcopy(src[k])
            r = run(a)
            sens[f'{name}_{side}'] = {y: round(r[y]['eps'] / res['base'][y]['eps'] - 1, 4) for y in Y}
    json.dump(dict(scenarios=res, sens=sens), open('model.json', 'w'), ensure_ascii=False, indent=1)
    for k, v in res.items():
        print(k, ' '.join(f"{y}:{v[y]['revenue']:.0f}/{v[y]['op']:.0f}({v[y]['opm']}%)/EPS{v[y]['eps']}/ST{v[y]['stations']}" for y in Y))
    for k, v in sens.items():
        print(k, v)


if __name__ == '__main__':
    main()
