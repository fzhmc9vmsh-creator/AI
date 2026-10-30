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
    r = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
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
    os.symlink(os.path.join(CWD, "node_modules"), os.path.join(T, "node_modules"))

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
    shutil.rmtree(T, ignore_errors=True)
    print("自己テスト:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
