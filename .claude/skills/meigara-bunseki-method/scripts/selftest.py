#!/usr/bin/env python3
"""自己テスト: 道具が正しく動くかを、手本(examples/sofi)の既知の答えで確かめる。作業の最初に 1 回実行する。

    python3 selftest.py      # すべて OK なら終了コード 0

FAIL のときは道具が壊れているか環境が違う。道具を直さずに作業を続けない(結果の数字が信用できなくなる)。
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
EX = os.path.join(HERE, "..", "examples", "sofi")
EXPECT = {   # SOFI(Q3 2026 決算後)の既知の答え。全精度は growth_v4.py と一致
    "value_engine": 23.845783055742146, "ev": 24.194252943974934, "sd": 7.346539941410197,
    "display": {"value.engine": "23.8", "value.consensus": "21.4", "value.company": "22.9", "value_peg10.engine": "19.5",
                "peg.start": "1.275", "alpha": "20.4%", "grade.letter": "B", "grade.avg": "3.42", "scen.ev": "24.2",
                "scen.sd": "7.3", "scen.bull.value": "33.5", "scen.bear.value": "13.9", "scen.bull.peg": "1.38〜1.43",
                "entry.Z1": "15.3", "entry.Z2": "21.4", "cagr.engine.2025-2028": "43.5%", "cagr.engine.2026-2029": "32.5%",
                "sens.増資 10 億ドル": "23.4"},
}


def run(args, cwd):
    r = subprocess.run([sys.executable] + args, cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def main():
    ok = True
    tmp = tempfile.mkdtemp(prefix="meigara_selftest_")
    for f in ("facts.json", "conditions.json", "valuation_input.json"):
        shutil.copy(os.path.join(EX, f), tmp)

    def check(name, cond, detail=""):
        nonlocal ok
        print(("OK   " if cond else "FAIL ") + name + (f"  ({detail})" if detail else ""))
        ok = ok and cond

    rc, out = run([os.path.join(HERE, "valuate.py"), "valuation_input.json"], tmp)
    check("valuate.py が動く", rc == 0, out.strip().splitlines()[-1] if out.strip() else "")
    if rc == 0:
        v = json.load(open(os.path.join(tmp, "valuation.json"), encoding="utf-8"))
        check("理論株価(全精度)", abs(v["paths"]["engine"]["value"] - EXPECT["value_engine"]) < 1e-6, f"{v['paths']['engine']['value']}")
        check("期待値・標準偏差(全精度)", abs(v["scenarios"]["ev"] - EXPECT["ev"]) < 1e-6 and abs(v["scenarios"]["sd"] - EXPECT["sd"]) < 1e-6)
        for k, want in EXPECT["display"].items():
            got = v["display"].get(k)
            check(f"表示値 {k}", got == want, f"{got} / 期待 {want}")
    for args, name in ((["facts.py", "check", "facts.json"], "facts.py check"),
                       (["gate.py", "facts", "."], "gate facts"), (["gate.py", "conditions", "."], "gate conditions"),
                       (["gate.py", "valuation", "."], "gate valuation")):
        rc, out = run([os.path.join(HERE, args[0])] + args[1:], tmp)
        check(name, rc == 0, out.strip().splitlines()[-1] if out.strip() else "")
    # 誤りを止めるか(わざと壊した入力)
    vi = json.load(open(os.path.join(tmp, "valuation_input.json"), encoding="utf-8"))
    vi["weights"] = [0.5, 0.3, 0.2, 0.2]
    json.dump(vi, open(os.path.join(tmp, "bad.json"), "w", encoding="utf-8"), ensure_ascii=False)
    rc, out = run([os.path.join(HERE, "valuate.py"), "bad.json", "-o", os.path.join(tmp, "bad")], tmp)
    check("重みの合計の誤りを止める", rc == 2)
    vi2 = json.load(open(os.path.join(tmp, "valuation_input.json"), encoding="utf-8"))
    vi2["sensitivities"] = [{"name": "EPS −10%(2030 年の書き漏らし)", "eps_mult": {"2026": -0.1, "2027": -0.1, "2028": -0.1, "2029": -0.1}}]
    json.dump(vi2, open(os.path.join(tmp, "bad2.json"), "w", encoding="utf-8"), ensure_ascii=False)
    rc, out = run([os.path.join(HERE, "valuate.py"), "bad2.json", "-o", os.path.join(tmp, "bad2")], tmp)
    check("感応度の年度の書き漏らしを止める(符号の逆転を防ぐ)", rc == 2 and "eps_mult" in out)
    vi3 = json.load(open(os.path.join(tmp, "valuation_input.json"), encoding="utf-8"))
    vi3.pop("edge", None)
    json.dump(vi3, open(os.path.join(tmp, "bad3.json"), "w", encoding="utf-8"), ensure_ascii=False)
    rc, out = run([os.path.join(HERE, "valuate.py"), "bad3.json", "-o", os.path.join(tmp, "bad3")], tmp)
    check("edge(市場との差分)の書き忘れを止める", rc == 2 and "edge" in out)
    cjp = json.load(open(os.path.join(tmp, "conditions.json"), encoding="utf-8"))
    vi4 = json.load(open(os.path.join(tmp, "valuation_input.json"), encoding="utf-8"))
    vi4.pop("conditions_file", None)
    vi4["grades"] = {str(c["no"]): c["grade"] for c in cjp["conditions"]}
    vi4["grades"]["10"] = "保留"
    json.dump(vi4, open(os.path.join(tmp, "pend.json"), "w", encoding="utf-8"), ensure_ascii=False)
    rc, out = run([os.path.join(HERE, "valuate.py"), "pend.json", "-o", os.path.join(tmp, "pend")], tmp)
    vp = json.load(open(os.path.join(tmp, "pend", "valuation.json"), encoding="utf-8")) if rc == 0 else {}
    check("評価保留を B と同じ点で数え、「保留をすべて C」の感応度を出す",
          rc == 0 and vp["display"]["value.engine"] == "23.8" and any(s["name"] == "保留をすべて C" for s in vp.get("sensitivities", [])))
    cj = json.load(open(os.path.join(tmp, "conditions.json"), encoding="utf-8"))
    cj["conditions"][1]["evidence"] = ["根拠に数字がない文"]
    cj["conditions"][2]["grade"] = "C"
    json.dump(cj, open(os.path.join(tmp, "conditions.json"), "w", encoding="utf-8"), ensure_ascii=False)
    rc, out = run([os.path.join(HERE, "gate.py"), "conditions", "."], tmp)
    check("採点表の不備(根拠不足・C の監視 KPI なし)を止める", rc == 1 and "監視 KPI" in out and "根拠" in out)
    shutil.rmtree(tmp, ignore_errors=True)
    print("自己テスト:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
