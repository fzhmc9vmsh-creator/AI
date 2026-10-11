# -*- coding: utf-8 -*-
"""chartkit の試験: 架空データ(銘柄A〜F)で全関数を実行し、_test/*.png を出力する。
実行: python3 charts/_test/run_tests.py
"""
import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import chartkit as ck  # noqa: E402

SRC = "出所: 架空データ(試験用)"
D = HERE / "data"
D.mkdir(exist_ok=True)

# ---------------------------------------------------------------- F13
def make_f13(path, price, base_eps, growth, ext_from=4):
    years = ["2026-07-31", "2027-07-31", "2028-07-31", "2029-07-31", "2030-07-31", "2031-07-31"]
    spec = {  # path: (eps倍率, g, peg_low, peg_high)
        "consensus": (1.00, 0.22, 1.2, 1.6),
        "company": (1.10, 0.26, 1.3, 1.8),
        "engine": (1.20, 0.30, 1.4, 2.0),
        "bear": (0.85, 0.16, 1.0, 1.3),
    }
    rows = []
    for p, (m, g0, pl, ph) in spec.items():
        eps = base_eps
        for i, fy in enumerate(years):
            eps = eps * (1 + growth * m) if i else base_eps * m
            g = max(0.04, g0 - 0.02 * i)
            plo, phi = g * 100 * pl, g * 100 * ph
            rows.append(dict(fy_end=fy, path=p, business_eps=round(eps, 2), g_3y=round(g, 3), peg_low=pl, peg_high=ph,
                             fair_per_low=round(plo, 1), fair_per_high=round(phi, 1),
                             fair_price_low=round(eps * plo, 1), fair_price_high=round(eps * phi, 1),
                             is_extension=1 if i >= ext_from else 0))
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


# ---------------------------------------------------------------- F18
def make_f18(path):
    import math
    qs = [f"{y}Q{q}" for y in (2024, 2025, 2026) for q in (1, 2, 3, 4)][:10]
    kpis = {"ARR(年間経常収益)": (3000, 0.36, 0.30), "NNARR(純新規ARR)": (210, 0.18, 0.12),
            "RPO(残存履行義務)": (6500, 0.24, 0.22), "NRR(既存顧客の売上継続率)": (118, -0.004, 0.0)}
    rows = []
    for k, (v0, g, ph) in kpis.items():
        prev_yoy = None
        for i, q in enumerate(qs):
            v = v0 * (1 + g / 4) ** i * (1 + 0.04 * math.sin(i * 1.3 + ph * 10))
            qoq = ((1 + g / 4 + 0.06 * math.sin(i * 1.3 + ph * 10)) ** 4 - 1)
            yoy = g + 0.04 * math.sin(i * 0.7 + ph * 5) - 0.003 * i
            sd = (yoy - prev_yoy) if prev_yoy is not None else ""
            prev_yoy = yoy
            rows.append(dict(kpi=k, period=q, value=round(v, 1), qoq_annualized=round(qoq, 4),
                             ttm_yoy=round(yoy, 4), second_diff=round(sd, 4) if sd != "" else ""))
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


# ---------------------------------------------------------------- F10
def make_f10(path, n_lines=4, n_q=10, n_fc=0):
    lines = ["サブスクリプション", "ハードウェア", "プロフェッショナルサービス", "マーケットプレイス", "その他手数料"][:n_lines]
    base = [820, 260, 120, 60, 25]
    gr = [0.07, 0.01, 0.02, 0.05, 0.0]
    rows = []
    for i in range(n_q):
        y, q = 2024 + i // 4, i % 4 + 1
        pname = f"{y}Q{q}" + ("E" if i >= n_q - n_fc else "")
        for j, ln in enumerate(lines):
            rows.append(dict(period=pname, line=ln, revenue_usd_mn=round(base[j] * (1 + gr[j]) ** i, 1)))
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


# ---------------------------------------------------------------- 横比較
TICK = ["銘柄A", "銘柄B", "銘柄C", "銘柄D", "銘柄E", "銘柄F"]
ROWS = [
    dict(name="銘柄A", growth=0.24, per=62.0, peg=2.4, expected_return=0.18, decision="買い検討",
         revenue_growth=0.15, fcf_margin=0.38, adj_eps=3.90, business_eps=3.10),
    dict(name="銘柄B", growth=0.31, per=95.0, peg=3.1, expected_return=-0.07, decision="見送り",
         revenue_growth=0.22, fcf_margin=0.28, adj_eps=3.40, business_eps=0.55),
    dict(name="銘柄C", growth=0.18, per=34.0, peg=1.9, expected_return=0.06, decision="監視",
         revenue_growth=0.12, fcf_margin=0.31, adj_eps=6.10, business_eps=4.70),
    dict(name="銘柄D", growth=0.40, per=120.0, peg=3.0, expected_return=0.24, decision="買い",
         revenue_growth=0.27, fcf_margin=0.09, adj_eps=1.20, business_eps=0.18),
    dict(name="銘柄E", growth=0.27, per=70.0, peg=2.6, expected_return=-0.12, decision="見送り",
         revenue_growth=0.29, fcf_margin=-0.04, adj_eps=0.80, business_eps=-0.15),
    dict(name="銘柄F", growth=0.20, per=28.0, peg=1.4, expected_return=0.11, decision="監視",
         revenue_growth=0.10, fcf_margin=0.30, adj_eps=8.30, business_eps=6.95),
]


def main():
    out = []
    make_f13(D / "fake_F13.csv", price=300.0, base_eps=8.0, growth=0.18)
    out.append(ck.plot_f13(D / "fake_F13.csv", HERE / "F13_test.png",
                           "銘柄A:適正株価は2029年7月期までに現在株価の1.4〜2.3倍に達する(架空)",
                           price_now=300.0, price_label="現在株価 $300", source=SRC, fictional=True))
    # 弱気だけ低く、現在株価が帯の中に入るケース(ラベル衝突の確認)
    make_f13(D / "fake_F13b.csv", price=150.0, base_eps=4.2, growth=0.10, ext_from=3)
    out.append(ck.plot_f13(D / "fake_F13b.csv", HERE / "F13_test_close.png", "銘柄B:経路が収束し現在株価が帯の中に入る(架空)",
                           price_now=150.0, source=SRC, fictional=True))

    make_f18(D / "fake_F18.csv")
    out.append(ck.plot_f18(D / "fake_F18.csv", HERE / "F18_test.png", "銘柄A:根幹KPIの成長は鈍化していない(架空)",
                           source=SRC, fictional=True))

    make_f10(D / "fake_F10.csv", n_lines=4, n_q=10)
    out.append(ck.plot_f10(D / "fake_F10.csv", HERE / "F10_test.png", "銘柄A:収益の中心はサブスクリプションで構成比が上昇(架空)",
                           source=SRC, fictional=True))
    make_f10(D / "fake_F10b.csv", n_lines=5, n_q=16, n_fc=3)
    out.append(ck.plot_f10(D / "fake_F10b.csv", HERE / "F10_test_5lines_forecast.png", "銘柄B:5ライン(畳み込み)と予測期の区別(架空)",
                           source=SRC, fictional=True))

    s1 = dict(ticker="銘柄A", price=300.0, price_date="2026-10-09",
              entry_zones=dict(alpha=0.12, Z1=240.0, Z2=330.0, zone="分割エントリー圏"),
              targets_12m=dict(consensus=350.0, company=410.0, engine=480.0, bear=210.0))
    s2 = dict(ticker="銘柄B", price=520.0, price_date="2026-10-09",
              entry_zones=dict(alpha=0.0, Z1=None, Z2=380.0, zone="見送り圏"),
              targets_12m=dict(consensus=455.0, company=520.0, engine=610.0, bear=300.0))
    (D / "fake_summary_A.json").write_text(json.dumps(s1, ensure_ascii=False, indent=1), encoding="utf-8")
    (D / "fake_summary_B_Z1null.json").write_text(json.dumps(s2, ensure_ascii=False, indent=1), encoding="utf-8")
    out.append(ck.plot_f7(D / "fake_summary_A.json", HERE / "F7_test.png", "銘柄A:現在株価は分割エントリー圏にある(架空)",
                          source=SRC, fictional=True))
    out.append(ck.plot_f7(D / "fake_summary_B_Z1null.json", HERE / "F7_test_Z1null.png",
                          "銘柄B:Z1が算定対象外のため即エントリー圏がない(架空)", source=SRC, fictional=True))

    out.append(ck.plot_scatter_growth_valuation(ROWS, HERE / "X_scatter_per_test.png",
                                                "成長率が高い銘柄ほどPERも高い(架空・6社)", y_key="per",
                                                x_label="EPS成長率(3年CAGR, %)", period="2027〜2030年度の事業実態EPS",
                                                source=SRC, fictional=True))
    out.append(ck.plot_scatter_growth_valuation(ROWS, HERE / "X_scatter_peg_test.png",
                                                "PEGで見るとD・Fが相対的に割安(架空・6社)", y_key="peg",
                                                x_label="EPS成長率(3年CAGR, %)", period="2027〜2030年度の事業実態EPS",
                                                source=SRC, fictional=True))
    out.append(ck.plot_ranking_bars(ROWS, HERE / "X_ranking_test.png", "期待リターンの順位(架空・6社)",
                                    period="12か月後(2027-10-11)", source=SRC, fictional=True))
    out.append(ck.plot_rule40(ROWS, HERE / "X_rule40_test.png", "ルール・オブ・40を満たすのはA・C・Fのみ(架空)",
                              period="直近四半期の前年同期比、FCFは直近12か月", source=SRC, fictional=True))
    out.append(ck.plot_sbc_vs_eps(ROWS, HERE / "X_sbc_vs_eps_test.png", "SBCを費用に戻すと利益の残り方は銘柄で大きく違う(架空)",
                                  period="次期(FY+1)", source=SRC, fictional=True))

    # ---------------- 端ケース(欠損・本数違い・Z1/Z2 null)
    import csv as _csv
    rows13 = [r for r in _csv.DictReader(open(D / "fake_F13.csv", encoding="utf-8")) if r["path"] != "company"]
    rows13[3]["fair_price_low"] = ""       # 欠損は点を飛ばす
    rows13[3]["fair_price_high"] = ""
    out.append(ck.plot_f13(rows13, HERE / "E_F13_3paths_missing.png", "端ケース: 3経路・1点欠損(架空)", 300.0,
                           source=SRC, fictional=True))
    f18 = list(_csv.DictReader(open(D / "fake_F18.csv", encoding="utf-8")))
    out.append(ck.plot_f18([r for r in f18 if r["kpi"].startswith("ARR")], HERE / "E_F18_1kpi.png",
                           "端ケース: KPI 1個(架空)", source=SRC, fictional=True))
    out.append(ck.plot_f18([r for r in f18 if not r["kpi"].startswith("NRR")], HERE / "E_F18_3kpi.png",
                           "端ケース: KPI 3個(架空)", source=SRC, fictional=True))
    f10 = list(_csv.DictReader(open(D / "fake_F10.csv", encoding="utf-8")))
    out.append(ck.plot_f10([r for r in f10 if r["line"].startswith("サブ")][:5], HERE / "E_F10_1line_5q.png",
                           "端ケース: 1ライン・5期(架空)", source=SRC, fictional=True))
    out.append(ck.plot_f7(dict(price=100.0, price_date="2026-10-09", entry_zones=dict(Z1=None, Z2=None, zone="算定なし"),
                               targets_12m=dict(consensus=120.0, company=None, engine=150.0, bear=70.0)),
                          HERE / "E_F7_Z1Z2null.png", "端ケース: Z1・Z2とも null、会社目標なし(架空)", source=SRC, fictional=True))
    rr = [dict(r) for r in ROWS]
    rr[1]["per"] = None
    rr[1]["peg"] = None
    out.append(ck.plot_scatter_growth_valuation(rr, HERE / "E_scatter_missing.png", "端ケース: 銘柄Bの PER 欠損(架空)",
                                                source=SRC, fictional=True))
    out.append(ck.plot_ranking_bars([{k: v for k, v in r.items() if k != "decision"} for r in ROWS],
                                    HERE / "E_ranking_nodecision.png", "端ケース: 最終判断なし(架空)",
                                    source=SRC, fictional=True))
    for o in out:
        print(o)


if __name__ == "__main__":
    main()
