#!/usr/bin/env python3
"""数字の台帳(facts.json)の検査・表示・資料用の書き出し。標準ライブラリだけで動く。

台帳は「報告書・資料に出す数字の唯一の出所」。数字は必ず台帳に 1 行ずつ登録し、時点(period)と
出所(source)と状態(status)を付ける。資料は台帳の表示値(disp)だけを使う(invest-consulting-deck の F())。

    python3 facts.py check facts.json                    # 検査(誤りがあれば終了コード 1)
    python3 facts.py table facts.json > facts_table.md   # 人が読む表
    python3 facts.py export facts.json valuation.json -o deck/facts_deck.json --as-of "Q3 2026"
                                                          # 資料用: 台帳 + 計算機の表示値を 1 つにまとめる

台帳の 1 行(templates/facts.json を写して使う):
  {"id": "q3.revenue", "label": "総純収益", "value": 1385.1, "nd": 1, "unit": "百万ドル",
   "period": "Q3 2026", "basis": "GAAP", "source": "8-K(2026-10-27)", "tier": "T1", "status": "確認", "note": ""}
- id: 英小文字・数字・ドット・下線だけ。同じ id は 1 回だけ。
- value: 数値(未取得なら null)。単位は unit の単位のまま入れる(換算は台帳の外でしない)。
- nd: 表示の小数桁。表示値 disp は value から 1 回だけ丸めて作る(丸めた値をさらに丸めない)。
- period: いつの値か。"Q3 2026" / "2026" / "FY2026" / "2026-10-16" / "2025→2028" / "2027E" など。空は不可。
- status: 確認(一次資料・要約で確認)/ 計算(台帳の他の行から計算。note に式)/ 推定(note に方法)/ 未取得。
- tier: T1(会社開示)〜 T4(未確認の報道・ブログ)。T4 は not_for_deck: true にする(資料に出ていたら lint_deck.py が止める)。
- 任意: not_for_deck(資料に使わない)・reason(その理由)・stale_check: false(古い四半期の値と同じ数字が別の意味で
  よく出るときに、古い値の検出から外す)・match_terms(資料の中でこの値の近くに出るはずの語。例: ["SoFiUSD", "流通"]。
  有効数字 1 桁の値はこれが無いと混入の検出ができない)・disp(表示を手で決める。丸めは value から 1 回だけ)。

台帳に入れる数字(要所だけでよい):
  1. タイトル・KPI の札・結論の箱・評価の理由に出す数字(資料は F('id') で引く)
  2. 前の四半期の主要な値(資料に古い値が時点ラベルなしで残っていないかの検出に使う)
  3. 使わないと決めた未確認の値(not_for_deck。資料への混入の検出に使う)
"""
import argparse
import json
import math
import re
import sys

ID_RE = re.compile(r"^[a-z0-9_]+(\.[a-z0-9_]+)*$")
PERIOD_RE = re.compile(r"^(Q[1-4] \d{4}|[1-4]Q\d{2}|H[12] \d{4}|FY ?\d{4}|\d{4}(E|年)?|\d{4}-\d{2}(-\d{2})?|\d{4}→\d{4}|\d{4}〜\d{4}|TTM( \d{4}-\d{2})?|.+時点|計算|評価時点)$")
STATUS = {"確認", "計算", "推定", "未取得"}
TIERS = {"T1", "T2", "T3", "T4"}
REQ = ["id", "label", "value", "unit", "period", "source", "status"]


def rnd(x, nd):
    q = 10 ** nd
    v = math.floor(abs(x) * q + 0.5) / q
    v = -v if x < 0 else v
    return f"{v:,.{nd}f}" if abs(v) >= 10000 else f"{v:.{nd}f}"


def disp_of(f):
    if f.get("disp"):
        return f["disp"]
    if f.get("value") is None:
        return "未取得"
    v = f["value"]
    if isinstance(v, str):
        return v
    s = rnd(v, int(f.get("nd", 1)))
    u = f.get("unit", "")
    if u in ("%", "％"):
        return s + "%"
    if u in ("pt", "bp", "x"):
        return s + u
    return s + (" " + u if u else "")


def load(path):
    with open(path, encoding="utf-8") as fh:
        d = json.load(fh)
    return d["facts"] if isinstance(d, dict) and "facts" in d else d


def check(facts):
    errs, warns = [], []
    seen = {}
    for i, f in enumerate(facts):
        where = f"{i + 1} 行目(id={f.get('id', '?')})"
        for k in REQ:
            if k not in f:
                errs.append(f"{where}: '{k}' がない")
        fid = f.get("id", "")
        if fid and not ID_RE.match(fid):
            errs.append(f"{where}: id は英小文字・数字・ドット・下線だけにする")
        if fid in seen:
            if seen[fid] != f.get("value"):
                errs.append(f"{where}: 同じ id が 2 回あり、値が違う({seen[fid]} と {f.get('value')})。どちらかに決めて 1 行にする")
            else:
                errs.append(f"{where}: 同じ id が 2 回ある。1 行にする")
        seen[fid] = f.get("value")
        p = str(f.get("period", "")).strip()
        if not p:
            errs.append(f"{where}: period(いつの値か)が空")
        elif not PERIOD_RE.match(p):
            warns.append(f"{where}: period '{p}' の書き方が標準でない(例: Q3 2026 / 2026 / 2026-10-16 / 2025→2028)")
        st = f.get("status")
        if st and st not in STATUS:
            errs.append(f"{where}: status は 確認・計算・推定・未取得 のどれか")
        if st == "未取得" and f.get("value") is not None:
            errs.append(f"{where}: 未取得なのに value がある")
        if st != "未取得" and f.get("value") is None and not f.get("disp"):
            errs.append(f"{where}: value が null。取れていないなら status を 未取得 にする")
        if st in ("計算", "推定") and not str(f.get("note", "")).strip():
            errs.append(f"{where}: {st} の値は note に式か方法を書く")
        t = f.get("tier")
        if t and t not in TIERS:
            errs.append(f"{where}: tier は T1〜T4")
        if t == "T4" and not f.get("not_for_deck", False):
            errs.append(f"{where}: T4(未確認)の数字は資料に使えない。確認するか not_for_deck: true にする")
        if st == "確認" and not t:
            warns.append(f"{where}: 確認済みの値に tier がない")
        if isinstance(f.get("value"), (int, float)) and "nd" not in f and not f.get("disp"):
            warns.append(f"{where}: nd(表示の小数桁)がない。既定の 1 桁で表示する")
    return errs, warns


def table(facts):
    L = ["| id | 項目 | 表示値 | 時点 | 基準 | 状態 | 出所 | 注 |", "|---|---|---|---|---|---|---|---|"]
    for f in facts:
        L.append(f"| {f.get('id')} | {f.get('label', '')} | {disp_of(f)} | {f.get('period', '')} | {f.get('basis', '')} | "
                 f"{f.get('status', '')}{'(' + f['tier'] + ')' if f.get('tier') else ''} | {f.get('source', '')} | {f.get('note', '')} |")
    return "\n".join(L) + "\n"


def export(facts, valuation, as_of):
    out = {"as_of": as_of, "facts": {}, "forbidden": []}
    for f in facts:
        if f.get("not_for_deck"):
            # 資料に使えない値(未確認の報道など)。lint_deck.py が資料の中に同じ数字が無いかを探す
            out["forbidden"].append(dict(id=f["id"], disp=disp_of(f), unit=f.get("unit", ""), match_terms=f.get("match_terms", []),
                                         reason=f.get("reason", f.get("note", "未確認"))))
            continue
        out["facts"][f["id"]] = dict(disp=disp_of(f), value=f.get("value"), unit=f.get("unit", ""), period=f.get("period", ""),
                                     status=f.get("status", ""), label=f.get("label", ""))
        if f.get("stale_check") is False:
            out["facts"][f["id"]]["stale_check"] = False
        if f.get("match_terms"):
            out["facts"][f["id"]]["match_terms"] = f["match_terms"]
    if valuation:
        for k, v in valuation.get("display", {}).items():
            fid = "val." + k
            if fid in out["facts"]:
                raise SystemExit(f"id の衝突: {fid}")
            out["facts"][fid] = dict(disp=v, value=None, unit="", period="計算", status="計算", label="valuate.py の表示値")
    return out


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check"); c.add_argument("facts")
    t = sub.add_parser("table"); t.add_argument("facts")
    e = sub.add_parser("export"); e.add_argument("facts"); e.add_argument("valuation", nargs="?")
    e.add_argument("-o", "--out", required=True); e.add_argument("--as-of", required=True, help='資料の基準の時点。例: "Q3 2026"')
    a = ap.parse_args()
    facts = load(a.facts)
    if a.cmd == "check":
        errs, warns = check(facts)
        for w in warns:
            print("注意:", w)
        for er in errs:
            print("誤り:", er)
        print(f"{len(facts)} 行 / 誤り {len(errs)} / 注意 {len(warns)} → {'PASS' if not errs else 'FAIL'}")
        sys.exit(1 if errs else 0)
    if a.cmd == "table":
        sys.stdout.write(table(facts))
    if a.cmd == "export":
        errs, _ = check(facts)
        if errs:
            print("台帳に誤りがあるため書き出さない。先に `facts.py check` を通す。", file=sys.stderr)
            sys.exit(1)
        val = None
        if a.valuation:
            with open(a.valuation, encoding="utf-8") as fh:
                val = json.load(fh)
        with open(a.out, "w", encoding="utf-8") as fh:
            json.dump(export(facts, val, a.as_of), fh, ensure_ascii=False, indent=1)
        print("書き出し:", a.out)


if __name__ == "__main__":
    main()
