#!/usr/bin/env python3
"""資料の道具の自己テスト。資料の作業フォルダ(lib.js などを写し、npm i pptxgenjs@3.12.0 を済ませた所)で実行する。

    python3 selftest_deck.py        # 手本(examples/mini の 4 枚)を _selftest/ に組み、監査・文言の検査が通るかと、
                                    # わざと入れた誤り(タイトルの手書きの数字・理論株価の打ち間違い)を止めるかを確かめる

FAIL のときは道具か環境(pptxgenjs・python-pptx)が壊れている。直してから作業を始める。
"""
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CWD = os.getcwd()
T = os.path.join(CWD, "_selftest")


def run(cmd, cwd=T):
    r = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout + r.stderr).strip()


def main():
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        print(("OK   " if cond else "FAIL ") + name + (f"  ({detail})" if detail else ""))
        ok = ok and cond

    nm = os.path.join(CWD, "node_modules", "pptxgenjs")
    check("pptxgenjs が入っている(npm i pptxgenjs@3.12.0)", os.path.isdir(nm))
    try:
        import pptx  # noqa: F401
        check("python-pptx が入っている", True)
    except ImportError:
        check("python-pptx が入っている(pip install python-pptx)", False)
    if not ok:
        sys.exit(1)
    shutil.rmtree(T, ignore_errors=True)
    os.makedirs(os.path.join(T, "slides"))
    for f in ("lib.js", "facts.js", "build.js", "one.js", "audit_deck.py", "lint_deck.py"):
        shutil.copy(os.path.join(HERE, f), T)
    mini = os.path.join(HERE, "examples", "mini")
    shutil.copy(os.path.join(mini, "meta.js"), T)
    shutil.copy(os.path.join(mini, "facts_deck.json"), T)
    for f in os.listdir(os.path.join(mini, "slides")):
        shutil.copy(os.path.join(mini, "slides", f), os.path.join(T, "slides"))
    try:
        os.symlink(os.path.join(CWD, "node_modules"), os.path.join(T, "node_modules"))
    except OSError:
        shutil.copytree(os.path.join(CWD, "node_modules"), os.path.join(T, "node_modules"))

    rc, out = run("node build.js deck.pptx")
    check("手本 4 枚を組める", rc == 0 and "slides 4" in out, out.splitlines()[-1] if out else "")
    rc, out = run("python3 audit_deck.py deck.pptx")
    check("監査 PASS", rc == 0 and "RESULT: PASS" in out, out.splitlines()[-1] if out else "")
    rc, out = run("python3 lint_deck.py src .")
    check("文言の検査(ソース)PASS", rc == 0, out.splitlines()[-1] if out else "")
    rc, out = run("python3 lint_deck.py pptx deck.pptx --facts facts_deck.json")
    check("文言の検査(資料)PASS", rc == 0, out.splitlines()[-1] if out else "")
    # わざと誤りを入れる
    meta = open(os.path.join(T, "meta.js"), encoding="utf-8").read()
    open(os.path.join(T, "meta.js"), "w", encoding="utf-8").write(meta.replace("${F('val.value.engine')} ドルで", "23.9 ドルで", 1))
    rc, out = run("python3 lint_deck.py src .")
    check("タイトルの手書きの数字を止める", rc == 1 and "タイトル" in out)
    rc, _ = run("node build.js bad.pptx")
    rc, out = run("python3 lint_deck.py pptx bad.pptx --facts facts_deck.json")
    check("理論株価の打ち間違い(23.9)を止める", rc == 1 and "23.9" in out)
    s4 = os.path.join(T, "slides", "s04.js")
    src = open(s4, encoding="utf-8").read()
    bad = src.replace("['会員数', F('q2.members', { noPeriod: true }), F('q3.members')]", "['会員数', F('q2.members', { noPeriod: true }), '1,580 万人']")
    check("(準備)手本の表の行を書き換えられる", bad != src)
    open(s4, "w", encoding="utf-8").write(bad)
    open(os.path.join(T, "meta.js"), "w", encoding="utf-8").write(meta)
    run("node build.js bad2.pptx")
    rc, out = run("python3 lint_deck.py pptx bad2.pptx --facts facts_deck.json")
    check("前の四半期の値(会員 1,580 万人)を Q3 の欄に時点なしで書いたのを止める", rc == 1 and "1,580" in out)
    # 2026-11-18: 初見の読み手の検査(略語の注釈)と、5 工程の設計書の検査
    import json as _json
    open(os.path.join(T, "st_empty.json"), "w", encoding="utf-8").write(_json.dumps({"glossary": []}))
    rc, out = run("python3 lint_deck.py pptx deck.pptx --facts facts_deck.json --storyline st_empty.json")
    check("注釈の無い略語(PER など)を止める", rc == 1 and "略語「PER」" in out)
    ex = os.path.join(HERE, "..", "examples", "storyline_stock_v3_anthropic.json")
    rc, out = run(f"python3 {os.path.join(HERE, 'check_storyline.py')} {ex}")
    check("手本の設計書(5 工程)が PASS", rc == 0, out.splitlines()[-1] if out else "")
    d0 = _json.load(open(ex, encoding="utf-8"))
    ps = d0["pages"]
    i = next(k for k, p_ in enumerate(ps) if p_.get("kind") == "path")
    ps[i], ps[i + 1] = ps[i + 1], ps[i]
    next(p_ for p_ in ps if p_.get("kind") == "fair_value")["introduces"].append("c_new")
    d0["concepts"].append({"id": "c_new", "label": "判定で初めて出す事実", "type": "fact"})
    open(os.path.join(T, "st_bad.json"), "w", encoding="utf-8").write(_json.dumps(d0, ensure_ascii=False))
    rc, out = run(f"python3 {os.path.join(HERE, 'check_storyline.py')} st_bad.json")
    check("道筋より先の終点と、判定で初めて出す事実を止める", rc == 1 and "future_structure" in out and "判定の章で新しい事実" in out)
    # 手本 c01(価値の橋)を組んで監査が通ることの確認
    c01_src = os.path.join(HERE, "examples", "charts", "c01_value_bridge.js")
    shutil.copy(c01_src, os.path.join(T, "slides", "sc01.js"))
    c01_meta = meta.replace("const ORDER = ['s01', 's02', 's03', 's04'];", "const ORDER = ['sc01'];").replace(
        "s01: { ch: 1, kind: 'cover' },",
        "s01: { ch: 1, kind: 'cover' },\n  sc01: { ch: 1, sec: '1-1', theme: '価値の橋', why: '現在値と理論株価の差がどこから生まれるかを分解して確かめる', title: '株価786円はEPSが約65円に下がる前提。差219円の約9割は\\n今の利益が続くだけで埋まり、成長の上乗せは約26円にすぎない' },"
    )
    open(os.path.join(T, "meta.js"), "w", encoding="utf-8").write(c01_meta)
    rc1, out1 = run("node build.js c01.pptx")
    rc2, out2 = run("python3 audit_deck.py c01.pptx")
    check("手本 c01(価値の橋)を組んで監査 PASS", rc1 == 0 and "図の重なり 0 件" in out1 and rc2 == 0 and "RESULT: PASS" in out2, (out2 or out1).splitlines()[-1] if (out2 or out1) else "")
    # 手本 c02〜c04 を組んで監査が通ることの確認
    charts_extra = [
        ("c02_payoff.js", "sc02", "ペイオフ棒", "現在値786円に対し最悪553円(-30%)・基準1,020円(+30%)と上下は非対称\\n基準と強気(合計確率88%)の上振れ余地が大きく、775円以下なら優位性が高い"),
        ("c03_step.js", "sc03", "段差と閾値", "2026年11月の二期完工で電子材料樹脂の能力は120tから210tへ一段上がる\\n年6.5%の市場成長を上回る供給余力が生まれ、増設分の販売はシェア獲得が鍵"),
        ("c04_regime.js", "sc04", "体制転換", "過去13期、粗利率はナフサと逆に動いた(相関-0.72)。今期は初めて崩れなかった\\nその関係なら粗利率は10.3%のはずが、実績は16.9%(+6.6pt)"),
        ("c05_portfolio.js", "sc05", "製品ポートフォリオ", "現金を生むのは成熟した界面活性剤(売上22,000)で、投資先は伸び年11.5%の\\n電子材料樹脂。増設で相対シェア1.4倍に届けば、現金を生む側に移る"),
        ("c06_risk_matrix.js", "sc06", "リスクの大きさ", "期待損失の上位は原料高(確率40%・下落18%)と価格競争(30%・22%)。\\nどちらも粗利率に出るので、監視は粗利率1本に絞れる"),
    ]
    for fname, sid, theme, title in charts_extra:
        shutil.copy(os.path.join(HERE, "examples", "charts", fname), os.path.join(T, "slides", f"{sid}.js"))
        cm = meta.replace("const ORDER = ['s01', 's02', 's03', 's04'];", f"const ORDER = ['{sid}'];").replace(
            "s01: { ch: 1, kind: 'cover' },",
            f"s01: {{ ch: 1, kind: 'cover' }},\n  {sid}: {{ ch: 1, sec: '1-1', theme: '{theme}', why: '手本の図形と配置の監査を確認する', title: '{title}' }},",
        )
        open(os.path.join(T, "meta.js"), "w", encoding="utf-8").write(cm)
        rc1, out1 = run(f"node build.js {sid}.pptx")
        rc2, out2 = run(f"python3 audit_deck.py {sid}.pptx")
        check(f"手本 {sid}({theme})を組んで監査 PASS", rc1 == 0 and "図の重なり 0 件" in out1 and rc2 == 0 and "RESULT: PASS" in out2, (out2 or out1).splitlines()[-1] if (out2 or out1) else "")
    shutil.rmtree(T, ignore_errors=True)
    print("自己テスト:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
