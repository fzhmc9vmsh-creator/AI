#!/usr/bin/env python3
"""資料の文言の検査(audit_deck.py の配置・文字の収まりの検査と対で使う)。

    python3 lint_deck.py src                 # slides/*.js と meta.js: 手で打った数字・時点ラベルの外し・版の言葉
    python3 lint_deck.py pptx out/deck.pptx  # 組み上がった資料の文字: 版の言葉・仮置き・計算の失敗(NaN など)

判定: 誤りが 1 件でもあれば FAIL(終了コード 1)。FAIL のまま納品しない。
- 手で打った数字: 文字列の中の小数・%・単位つきの数(億・万・ドル・倍・pt・bp・人・件・社)は F('id') で台帳から引く。
  どうしても台帳に入れない数(図の番号の説明など)は、その行の末尾に  // lint-ok: 理由  と書く(理由のない lint-ok は誤り)。
- チャートの values: [...] に数字を直接書かない。F.v('id') で引く(同じく lint-ok で例外)。
"""
import glob
import os
import re
import sys

NUM_UNIT = re.compile(r"(?<![A-Za-z_\-./])[−\-+]?\d[\d,]*(\.\d+)?\s?(%|％|倍|ドル|円|億|万|兆|pt|bp|bps|人|件|社|x)(?![A-Za-z])")
DECIMAL = re.compile(r"(?<![A-Za-z_\-./\d§])\d+\.\d+(?![\d.]*[A-Za-z_-])")
BANNED = [
    (re.compile(r"第\s?\d+\s?版"), "版の言葉(第N版)"), (re.compile(r"前回|今回"), "版の言葉(前回・今回)"),
    (re.compile(r"(?<![A-Za-z0-9_])v\d(?![\d.])"), "版の言葉(v2 など)"), (re.compile(r"改訂|新規スライド|差し替え"), "版の言葉(改訂など)"),
    (re.compile(r"TODO|TBD|XXX|〇〇|●●|△△|ダミー|仮置き"), "仮置きの文字"),
    (re.compile(r"undefined|NaN|\[object Object\]|null(?![A-Za-z])"), "計算・参照の失敗"),
]
STR_RE = re.compile(r"'((?:[^'\\\n]|\\.)*)'|\"((?:[^\"\\\n]|\\.)*)\"|`((?:[^`\\]|\\.)*)`", re.S)


def strip_comment(line):
    out, q = [], None
    i = 0
    while i < len(line):
        ch = line[i]
        if q:
            out.append(ch)
            if ch == "\\" and i + 1 < len(line):
                out.append(line[i + 1]); i += 2; continue
            if ch == q:
                q = None
        else:
            if ch in "'\"`":
                q = ch
            if ch == "/" and line[i:i + 2] == "//":
                return "".join(out), line[i:]
            out.append(ch)
        i += 1
    return "".join(out), ""


def lint_src(root, only=None):
    files = sorted(glob.glob(os.path.join(root, "slides", "*.js")))
    if only:
        files = [f for f in files if os.path.basename(f) == only + ".js"]
    elif os.path.exists(os.path.join(root, "meta.js")):
        files.append(os.path.join(root, "meta.js"))
    errs, info = [], []
    for fp in files:
        name = os.path.relpath(fp, root)
        with open(fp, encoding="utf-8") as fh:
            for n, raw in enumerate(fh, 1):
                code, comment = strip_comment(raw.rstrip("\n"))
                if not code.strip():
                    continue
                ok = "lint-ok" in comment
                if ok and not re.search(r"lint-ok\s*:\s*\S", comment):
                    errs.append(f"{name}:{n}: lint-ok に理由がない")
                if "noPeriod" in code:
                    info.append(f"{name}:{n}: 時点ラベルを外した数字(本文に時点があるか確かめる)")
                if re.search(r"\bvalues\s*:\s*\[[^\]]*\d", code) and "F.v(" not in code and not ok:
                    errs.append(f"{name}:{n}: チャートの値を直接書いている → F.v('id') で引く")
                code_wo_f = re.sub(r"\$\{[^}]*\}", "", code)
                code_wo_f = re.sub(r"F(\.[nv])?\(\s*'[^']*'[^)]*\)", "", code_wo_f)
                for m in STR_RE.finditer(code_wo_f):
                    s = next(g for g in m.groups() if g is not None)
                    if re.fullmatch(r"[0-9A-Fa-f]{6}", s):           # 色
                        continue
                    hits = [h.group(0) for h in NUM_UNIT.finditer(s)] + [h.group(0) for h in DECIMAL.finditer(s)]
                    hits = [h for h in hits if not re.fullmatch(r"(19|20)\d\d", h.strip())]
                    if hits and not ok:
                        errs.append(f"{name}:{n}: 手で打った数字 {sorted(set(hits))[:4]} → F('id') で台帳から引く")
                for rx, what in BANNED[:5]:
                    for m in STR_RE.finditer(code):
                        s = next(g for g in m.groups() if g is not None)
                        if rx.search(s) and "source" not in code.split(":")[0]:
                            errs.append(f"{name}:{n}: {what}「{rx.search(s).group(0)}」")
    return files, errs, info


def lint_pptx(path):
    from pptx import Presentation
    errs = []
    prs = Presentation(path)
    for i, sl in enumerate(prs.slides, 1):
        texts = []
        for sh in sl.shapes:
            if sh.has_text_frame:
                texts.append(sh.text_frame.text)
            if getattr(sh, "has_table", False) and sh.has_table:
                texts += [c.text for r in sh.table.rows for c in r.cells]
        t = "\n".join(texts)
        for rx, what in BANNED:
            for m in rx.finditer(t):
                ctx = t[max(0, m.start() - 15):m.end() + 15].replace("\n", " ")
                errs.append(f"p.{i}: {what}「{m.group(0)}」… {ctx}")
    return len(prs.slides), errs


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("src", "pptx"):
        print(__doc__)
        sys.exit(2)
    if sys.argv[1] == "src":
        args = sys.argv[2:]
        only = None
        if "--only" in args:
            only = args[args.index("--only") + 1]
            args = [x for x in args if x not in ("--only", only)]
        root = args[0] if args else "."
        files, errs, info = lint_src(root, only)
        for x in info:
            print("確認:", x)
        for e in errs:
            print("誤り:", e)
        print(f"{len(files)} ファイル / 誤り {len(errs)} / 確認 {len(info)} → {'PASS' if not errs else 'FAIL'}")
    else:
        n, errs = lint_pptx(sys.argv[2])
        for e in errs:
            print("誤り:", e)
        print(f"{n} 枚 / 誤り {len(errs)} → {'PASS' if not errs else 'FAIL'}")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
