#!/usr/bin/env python3
"""アップロード用のスキル(skills/*.skill = zip)を、検査を通してから作る。

    python3 skills/build_skills.py [--node-modules <pptxgenjs の入った node_modules>]

検査(1 つでも FAIL なら zip を作らない):
  1. SKILL.md の書式: name はフォルダ名と同じ(英小文字・数字・ハイフン、64 字以内)、description は 1,024 字以内で < > を含まない
  2. SKILL.md と scripts/README.md が指すファイル(references/・scripts/・templates/・examples/)が実在する
  3. 共有ファイルが一致する(meigara-bunseki-method と invest-consulting-deck の scripts/facts.py)
  4. 環境に依存する絶対パス(/home/user など)が入っていない
  5. 自己テスト: meigara-bunseki-method の selftest.py、invest-consulting-deck の selftest_deck.py(--node-modules があるとき)
編集の正はリポジトリの .claude/skills/。zip はその写し。
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, ".claude", "skills")
OUT = os.path.join(ROOT, "skills")
SKILLS = ["meigara-bunseki-method", "invest-consulting-deck", "bcg-slide-method"]
SHARED = [("meigara-bunseki-method/scripts/facts.py", "invest-consulting-deck/scripts/facts.py")]
SKIP_DIRS = {"__pycache__", "node_modules", "_selftest", "tmp", ".git"}
SKIP_FILES = {".DS_Store"}
BAD_PATHS = re.compile(r"/home/user|/root/\.claude|reports/SOFI/work|/tmp/claude-")


def files_of(skill):
    base = os.path.join(SRC, skill)
    out = []
    for d, dirs, fs in os.walk(base):
        dirs[:] = sorted(x for x in dirs if x not in SKIP_DIRS)
        for f in sorted(fs):
            if f in SKIP_FILES or f.endswith(".pyc"):
                continue
            out.append(os.path.relpath(os.path.join(d, f), base))
    return out


def check_skill(skill, errs):
    base = os.path.join(SRC, skill)
    t = open(os.path.join(base, "SKILL.md"), encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    if not m:
        errs.append(f"{skill}: SKILL.md の先頭に --- で囲んだ name・description がない")
        return
    fm = m.group(1)
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not name or name.group(1).strip() != skill:
        errs.append(f"{skill}: name がフォルダ名と違う")
    elif not re.fullmatch(r"[a-z0-9-]{1,64}", name.group(1).strip()):
        errs.append(f"{skill}: name は英小文字・数字・ハイフンで 64 字以内")
    if not desc:
        errs.append(f"{skill}: description がない")
    else:
        d = desc.group(1).strip()
        if len(d) > 1024:
            errs.append(f"{skill}: description が {len(d)} 字(1,024 字以内)")
        if "<" in d or ">" in d:
            errs.append(f"{skill}: description に < > を使わない")
    # 指しているファイルの実在
    texts = [t]
    rd = os.path.join(base, "scripts", "README.md")
    if os.path.exists(rd):
        texts.append(open(rd, encoding="utf-8").read())
    for tx in texts:
        for ref in sorted(set(re.findall(r"(?<![\w/.-])((?:references|scripts|templates|examples)/[\w./-]+)", tx))):
            ref = ref.rstrip(".,)")
            p = os.path.join(base, ref)
            if ref.endswith("/"):
                ok = os.path.isdir(p)
            else:
                ok = os.path.exists(p) or os.path.exists(os.path.join(base, "scripts", ref))
            if not ok:
                errs.append(f"{skill}: 指しているファイルが無い: {ref}")
    for f in files_of(skill):
        if f.endswith((".md", ".py", ".js", ".json")):
            s = open(os.path.join(base, f), encoding="utf-8", errors="ignore").read()
            m2 = BAD_PATHS.search(s)
            if m2:
                errs.append(f"{skill}/{f}: 環境に依存するパス「{m2.group(0)}」")


def selftests(node_modules, errs):
    r = subprocess.run([sys.executable, os.path.join(SRC, "meigara-bunseki-method", "scripts", "selftest.py")], capture_output=True, text=True)
    print("[自己テスト] meigara-bunseki-method:", (r.stdout.strip().splitlines() or ["?"])[-1])
    if r.returncode != 0:
        errs.append("meigara-bunseki-method の自己テストが FAIL\n" + r.stdout)
    if not node_modules:
        print("[自己テスト] invest-consulting-deck: --node-modules が無いので省略(資料の自己テストは利用側の準備でも実行される)")
        return
    tmp = tempfile.mkdtemp(prefix="deck_selftest_")
    os.symlink(os.path.abspath(node_modules), os.path.join(tmp, "node_modules"))
    r = subprocess.run([sys.executable, os.path.join(SRC, "invest-consulting-deck", "scripts", "selftest_deck.py")], cwd=tmp, capture_output=True, text=True)
    print("[自己テスト] invest-consulting-deck:", (r.stdout.strip().splitlines() or ["?"])[-1])
    if r.returncode != 0:
        errs.append("invest-consulting-deck の自己テストが FAIL\n" + r.stdout + r.stderr)
    shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--node-modules", default=None)
    a = ap.parse_args()
    errs = []
    for s in SKILLS:
        check_skill(s, errs)
    for x, y in SHARED:
        if open(os.path.join(SRC, x), "rb").read() != open(os.path.join(SRC, y), "rb").read():
            errs.append(f"共有ファイルが一致しない: {x} と {y}(片方を直したらもう片方に写す)")
    selftests(a.node_modules, errs)
    if errs:
        for e in errs:
            print("誤り:", e)
        print("FAIL: zip を作らない")
        sys.exit(1)
    for s in SKILLS:
        dst = os.path.join(OUT, s + ".skill")
        fs = files_of(s)
        with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr(zipfile.ZipInfo(s + "/"), "")
            for f in fs:
                z.write(os.path.join(SRC, s, f), s + "/" + f)
        print(f"作成: skills/{s}.skill({len(fs)} ファイル、{os.path.getsize(dst) // 1024} KB)")
    print("PASS")


if __name__ == "__main__":
    main()
