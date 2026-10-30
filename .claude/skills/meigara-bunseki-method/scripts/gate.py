#!/usr/bin/env python3
"""工程ごとの合否判定(銘柄分析メソッド)。FAIL のまま次の工程へ進まない。標準ライブラリだけで動く。

作業フォルダの標準のファイル名(templates/ を写して使う):
    facts.json            数字の台帳(要所の数字・前の四半期の主要な値・使わない未確認の値)
    conditions.json       13 条件の採点表
    valuation_input.json  価値評価の入力 → valuate.py が valuation.json・valuation.md を出す
    report.md             報告書(docx に変換する前の原稿)

    python3 gate.py facts       [作業フォルダ]   # 台帳の検査
    python3 gate.py conditions  [作業フォルダ]   # 採点表の検査(根拠・監視 KPI・二層の評価・評価保留)
    python3 gate.py conditions --before-price [作業フォルダ]   # 工程 4 の終わり: 条件6・7 が空でも止めない
    python3 gate.py valuation   [作業フォルダ]   # 計算機を通したか・採点表と評価が一致するか
    python3 gate.py report      [作業フォルダ]   # 報告書の章・数字の一致・版の言葉
    python3 gate.py all         [作業フォルダ]   # 上の 4 つを順に
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GRADES = {"S", "A", "B", "C", "D", "E", "F", "N/A", "保留"}
LOW = {"C", "D", "E", "F"}
GROWTH_CONDS = {1, 2, 3, 6, 7, 11, 12, 13}     # 成長企業で二層(現在と将来)の評価が要る条件
REPORT_HEADINGS = ["エグゼクティブサマリ", "事業本体", "収益構造", "シナリオ", "13条件", "PEG", "バリュエーション",
                   "カタリスト", "リスク", "市場との差分", "既知の制約", "計算前提"]
BANNED = re.compile(r"第\s?\d+\s?版|前回|今回|TODO|TBD|XXX|〇〇|●●|NaN|undefined")
NUM = re.compile(r"(?<![\d.])\d[\d,]*(?:\.\d+)?(?![\d.])")
VAL_KEYS = re.compile(r"理論株価|期待値|標準偏差|適正株価|許容 ?PEG|即時エントリー|分割エントリー")


class Gate:
    def __init__(self, name):
        self.name, self.errs, self.warns = name, [], []

    def e(self, msg):
        self.errs.append(msg)

    def w(self, msg):
        self.warns.append(msg)

    def done(self):
        for x in self.warns:
            print(f"[{self.name}] 注意: {x}")
        for x in self.errs:
            print(f"[{self.name}] 誤り: {x}")
        ok = not self.errs
        print(f"[{self.name}] 誤り {len(self.errs)} / 注意 {len(self.warns)} → {'PASS' if ok else 'FAIL'}")
        return ok


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def g_facts(d):
    g = Gate("台帳")
    p = os.path.join(d, "facts.json")
    if not os.path.exists(p):
        g.e("facts.json がない(templates/facts.json を写して作る)")
        return g.done()
    r = subprocess.run([sys.executable, os.path.join(HERE, "facts.py"), "check", p], capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode != 0:
        g.e("facts.py check が FAIL(上の誤りを直す)")
    facts = load(p)
    rows = facts["facts"] if isinstance(facts, dict) else facts
    if isinstance(facts, dict) and not facts.get("as_of"):
        g.e("facts.json に as_of(資料・報告書の基準の時点。例: \"Q3 2026\")がない")
    if len(rows) < 15:
        g.w(f"台帳が {len(rows)} 行と少ない。要所(タイトル・結論・KPI・価値評価の入力)の数字が入っているか確かめる")
    if isinstance(facts, dict) and facts.get("as_of"):
        olds = [f for f in rows if re.fullmatch(r"Q[1-4] \d{4}", str(f.get("period", ""))) and f.get("period") != facts["as_of"]]
        if not olds:
            g.w("前の四半期の主要な値が台帳にない(古い値が資料に残っていないかの検出ができない)")
    return g.done()


def g_conditions(d, before_price=False):
    g = Gate("13 条件" + ("(条件6・7 を除く)" if before_price else ""))
    p = os.path.join(d, "conditions.json")
    if not os.path.exists(p):
        g.e("conditions.json がない(templates/conditions.json を写して作る)")
        return g.done()
    cj = load(p)
    ids = set()
    fp = os.path.join(d, "facts.json")
    if os.path.exists(fp):
        fj = load(fp)
        ids = {f["id"] for f in (fj["facts"] if isinstance(fj, dict) else fj)}
    else:
        g.w("facts.json が無いので、根拠の id を確かめられない")
    conds = cj.get("conditions", [])
    nos = sorted(c.get("no") for c in conds)
    if nos != list(range(1, 14)):
        g.e(f"条件は 1〜13 を 1 つずつ(今は {nos})")
    growth = bool(cj.get("growth_company"))
    if growth and not str(cj.get("phase", "")).strip():
        g.e("成長企業(growth_company: true)は phase(フェーズ ①〜⑤)を最初に決めて書く")
    n_pending = 0
    for c in conds:
        no, gr = c.get("no"), str(c.get("grade", "")).strip().upper()
        tag = f"条件{no}"
        if before_price and no in (6, 7) and not gr:
            continue                     # 条件6・7 は株価を入れた後(工程 5 の 3)で採点する
        if gr == "保留":
            n_pending += 1
            if not (str(c.get("kpi", "")).strip() and str(c.get("trigger", "")).strip()):
                g.e(f"{tag}: 評価保留は、決め手になる確認 KPI(kpi)と閾値(trigger)が必須")
            if len(str(c.get("reason", "")).strip()) < 15:
                g.e(f"{tag}: 評価保留は reason に「何が分かれば決まるか」を書く")
            continue
        if gr not in GRADES:
            g.e(f"{tag}: grade '{c.get('grade')}' は S・A・B・C・D・E・F・保留・N/A のどれか(空なら採点する)")
            continue
        reason = str(c.get("reason", "")).strip()
        if len(reason) < 15:
            g.e(f"{tag}: reason(判定の決め手の一文)が短すぎる・空")
        if gr == "N/A":
            if no != 9:
                g.e(f"{tag}: 対象外(N/A)にできるのは条件9(AI 関連でない企業)だけ")
            continue
        ev = c.get("evidence", [])
        need = 1 if no == 4 else 2
        if len(ev) < need:
            g.e(f"{tag}: 根拠(evidence)が {len(ev)} 個。{need} 個以上(台帳の id か、数字と出所を含む文)")
        n_id = 0
        for x in ev:
            x = str(x)
            if x in ids:
                n_id += 1
            elif re.fullmatch(r"[a-z0-9_]+(\.[a-z0-9_]+)+", x):
                g.e(f"{tag}: 根拠の id '{x}' が台帳にない")
            elif not re.search(r"\d", x) and no not in (4, 9):
                g.e(f"{tag}: 根拠「{x[:20]}…」に数字がない(定量の根拠にする。例:「交換手数料は前年比 +77%(8-K)」)")
        if ids and no != 4 and n_id == 0:
            g.e(f"{tag}: 根拠に台帳の id が 1 つもない(少なくとも 1 つは台帳の数字で示す)")
        if gr in LOW and not (str(c.get("kpi", "")).strip() and str(c.get("trigger", "")).strip()):
            g.e(f"{tag}: {gr} 以下は監視 KPI(kpi)とトリガー(trigger)が必須")
        if growth and no in GROWTH_CONDS:
            fg = str(c.get("future_grade", "")).upper()
            if fg not in GRADES - {"N/A"}:
                g.e(f"{tag}: 成長企業は将来(実現性を加味)の評価 future_grade が必須(二層の構造評価)")
            elif fg != gr and not isinstance(c.get("future_p"), (int, float)):
                g.e(f"{tag}: 将来の評価が現在と違うときは実現確率 future_p(0〜1)を書く")
    if n_pending > 3:
        g.e(f"評価保留が {n_pending} 件。3 件以内にする(決め手の証拠を追加調査する。最大 2 周)")
    if str(next((c.get("grade") for c in conds if c.get("no") == 4), "")).upper() not in ("S", "A"):
        g.w("条件4(日本株か米国株)が S・A でない。ゲート審査で止めるべきかを確かめる")
    return g.done()


def g_valuation(d):
    g = Gate("価値評価")
    pi, po = os.path.join(d, "valuation_input.json"), os.path.join(d, "valuation.json")
    if not os.path.exists(pi):
        g.e("valuation_input.json がない(templates/valuation_input.json を写して作る)")
        return g.done()
    if not os.path.exists(po) or os.path.getmtime(po) < os.path.getmtime(pi):
        g.e("valuation.json が無いか、入力より古い。`python3 valuate.py valuation_input.json` を実行する(手で計算しない)")
        return g.done()
    vi, vo = load(pi), load(po)
    for c in vo.get("checks", []):
        if not c["ok"]:
            g.e(f"計算機の検査が NG: {c['name']}: {c['detail']}")
    cp = os.path.join(d, "conditions.json")
    if os.path.exists(cp):
        cg = {str(c["no"]): str(c["grade"]).upper() for c in load(cp)["conditions"]}
        vg = {str(k): str(v).upper() for k, v in vi.get("grades", {}).items()} if "grades" in vi else None
        if vg is not None and vg != cg:
            diff = [k for k in sorted(set(cg) | set(vg), key=int) if cg.get(k) != vg.get(k)]
            g.e(f"valuation_input の grades が conditions.json と違う(条件 {', '.join(diff)})。conditions_file を使えば食い違わない")
    else:
        g.w("conditions.json が無いので、評価の一致を確かめられない")
    if len(vi.get("eps_paths", {})) < 3:
        g.e("EPS 経路は 3 つ(コンセンサス・会社の計画・事業エンジン)を並べる")
    if "scenarios" not in vi and "tree" not in vi:
        g.e("シナリオ(scenarios か tree)がない。強気・弱気を同じ粒度で出す(固定の 25/50/25 は不可)")
    else:
        sc = vo.get("scenarios", {})
        if not ({"bull", "bear"} <= set(sc.get("bundles", {}))):
            g.e("シナリオに bull と bear の束がない(bundle を付ける)")
        ps = sorted({round(s["p"], 4) for s in sc.get("items", [])})
        if len(sc.get("items", [])) == 3 and ps in ([0.25, 0.5], [0.25, 0.25, 0.5]):
            g.e("シナリオ確率が固定の 25/50/25 になっている。節点ツリーか証拠で出す")
    mat = vi.get("maturity", {})
    if float(mat.get("roe", 0.18)) == 0.18 and not str(mat.get("note", "")).strip():
        g.w("maturity.roe が既定の 18% のまま。会社の定常の ROE(株主資本ベース)を根拠つきで入れ、maturity.note に書く")
    if float(vi.get("survival", 1.0)) >= 1.0 and not str(vi.get("survival_note", "")).strip():
        g.w("survival(生存確率)が 1.0。借入に頼らない企業ならその理由を survival_note に書く(借入で成長する企業は倒産確率から置く)")
    if len(vi.get("sensitivities", [])) < 2:
        g.w("感応度が 2 つ未満。最低でも EPS ±10%(株数が分かれば増資)を入れる")
    if os.path.exists(cp):
        linked = {str(c) for n in vi.get("tree", {}).get("nodes", []) for c in n.get("links", [])}
        for c in load(cp)["conditions"]:
            fg = str(c.get("future_grade") or "").upper()
            if fg and fg != str(c.get("grade", "")).upper() and str(c["no"]) not in linked and "scenarios" not in vi:
                g.w(f"条件{c['no']}: 将来の評価 {fg} が現在と違うのに、節点ツリーの links に入っていない(将来の構造が価値に入らない)")
    if not vi.get("cross_checks"):
        g.w("交差確認(DCF・同業の PER・TBV×ROTCE など)が無い。平均には入れないが並べて理由を書く")
    if vi.get("averaged") or vi.get("fair_per_mode") == "average":
        g.e("妥当 PER を他の方法と平均している。PEG × g だけで決める(第5.2版)")
    return g.done()


def g_report(d):
    g = Gate("報告書")
    p = os.path.join(d, "report.md")
    if not os.path.exists(p):
        g.e("report.md がない")
        return g.done()
    t = open(p, encoding="utf-8").read()
    heads = "\n".join(re.findall(r"^#{1,3} .*$", t, re.M))
    for h in REPORT_HEADINGS:
        if h not in heads:
            g.e(f"見出しに「{h}」がない(templates/report_outline.md の章立て)")
    for m in BANNED.finditer(t):
        g.e(f"使わない語「{m.group(0)}」… {t[max(0, m.start() - 15):m.end() + 15]!r}")
    if "エッジなし" not in t and not re.search(r"優位の種類|情報の優位|分析の優位|時間軸の優位|行動の優位", t):
        g.e("市場との差分に優位の種類(情報・分析・時間軸・行動)が書かれていない(差分がなければ「エッジなし」と書く)")
    po = os.path.join(d, "valuation.json")
    allowed = set()
    if os.path.exists(po):
        for v in load(po).get("display", {}).values():
            allowed.update(NUM.findall(str(v)))
    fp = os.path.join(d, "facts.json")
    if os.path.exists(fp):
        fj = load(fp)
        for f in (fj["facts"] if isinstance(fj, dict) else fj):
            allowed.update(NUM.findall(str(f.get("disp") or f.get("value") or "")))
    if allowed:
        for m in VAL_KEYS.finditer(t):
            nm = re.match(r"[^\d\n。、・]{0,10}?(?<![A-Za-z\d.+−-])(\d[\d,]*(?:\.\d+)?)(?![\d.])(?!\s?(pt|%|bp|通り|倍|年|件|つ))", t[m.end():m.end() + 40])
            if nm and nm.group(1) not in allowed:
                g.e(f"「{m.group(0)}」の数字 {nm.group(1)} が valuation.json・台帳の値と一致しない … {t[m.start():m.end() + 20]!r}")
    else:
        g.w("valuation.json・facts.json が無いので、数字の一致を確かめられない")
    if re.search(r"(?<![A-Za-z])[A-Za-z][A-Za-z ,'\-]{60,}", t):
        g.w("英文の長い引用がある。和訳を主にし、原文は必要最小限の括弧書きにする")
    return g.done()


def main():
    args = [a for a in sys.argv[1:] if a != "--before-price"]
    before = "--before-price" in sys.argv
    if not args or args[0] not in ("facts", "conditions", "valuation", "report", "all"):
        print(__doc__)
        sys.exit(2)
    sys.argv = [sys.argv[0]] + args
    d = sys.argv[2] if len(sys.argv) > 2 else "."
    fns = {"facts": g_facts, "conditions": (lambda x: g_conditions(x, before)), "valuation": g_valuation, "report": g_report}
    order = ["facts", "conditions", "valuation", "report"] if sys.argv[1] == "all" else [sys.argv[1]]
    ok = True
    for k in order:
        ok = fns[k](d) and ok
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
