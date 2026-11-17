#!/usr/bin/env python3
"""工程ごとの合否判定(銘柄分析メソッド)。FAIL のまま次の工程へ進まない。標準ライブラリだけで動く。

作業フォルダの標準のファイル名(templates/ を写して使う):
    facts.json            数字の台帳(要所の数字・前の四半期の主要な値・使わない未確認の値)
    conditions.json       13 条件の採点表
    valuation_input.json  価値評価の入力 → valuate.py が valuation.json・valuation.md を出す
    report.md             報告書(docx に変換する前の原稿)
    hypotheses.json       仮説台帳(analysis-playbook.md §3)
    change_map.json       変化の評価表(analysis-playbook.md §5)
    business_map.json     事業の地図(製品群の地図・バリューチェーン図。analysis-playbook.md §4)
    series.json           時系列の入力 → lenses.py が lenses.json・lenses.md(示唆の種)を出す(analysis-playbook.md §7)
    structure.json        事業構造の解剖(12 区画。structure-anatomy.md)。units.json → structure_lenses.py が単位のレンズを出す

    python3 gate.py facts       [作業フォルダ]   # 台帳の検査
    python3 gate.py conditions  [作業フォルダ]   # 採点表の検査(根拠・監視 KPI・二層の評価・評価保留)
    python3 gate.py conditions --before-price [作業フォルダ]   # 工程 4 の終わり: 条件6・7 が空でも止めない
    python3 gate.py valuation   [作業フォルダ]   # 計算機を通したか・採点表と評価が一致するか
    python3 gate.py report      [作業フォルダ]   # 報告書の章・数字の一致・版の言葉
    python3 gate.py hypotheses  [作業フォルダ]   # 仮説台帳(反証できる形・判定の根拠・立て直しの跡)。工程 2 の終わり
    python3 gate.py map         [作業フォルダ]   # 事業の地図(製品群の地図・バリューチェーン図)。工程 2 の途中
    python3 gate.py change      [作業フォルダ]   # 変化の評価表(15 項目の過去・現在・将来)。工程 4 の前
    python3 gate.py lenses      [作業フォルダ]   # 示唆の種(lenses.py の旗)を仮説・示唆に使ったか、理由を付けて捨てたか。工程 2 の終わり
    python3 gate.py thesis      [作業フォルダ]   # 投資仮説(市場との差分・価値の芯・撤回の線)、示唆の深さ、弱気の反論の検証。工程 6 の終わり
    python3 gate.py structure   [作業フォルダ]   # 事業構造の解剖(12 区画・単位のレンズ・盲検)。工程 2A の終わり。13 条件の採点の前
    python3 gate.py deep        [作業フォルダ]   # 13 条件の深掘り(決め手の問い・測り方・反対の評価・構造との接続)。工程 4・工程 5 の 3
    python3 gate.py final       [作業フォルダ]   # 最終の総合検査(facts〜thesis の 10 本)。報告書と資料はこれが PASS してから
    python3 gate.py all         [作業フォルダ]   # facts・conditions・valuation・report を順に
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
REPORT_HEADINGS = ["エグゼクティブサマリ", "会社と事業の概要", "業界の仕組みとお金の流れ", "最新決算", "事業本体", "収益構造", "シナリオ", "13条件", "PEG",
                   "バリュエーション", "カタリスト", "リスク", "市場との差分", "既知の制約", "計算前提"]
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
    # 必須の前提の節(2026-11-17): 中身の薄い見出しだけで逃げない
    for h, need_num in (("会社と事業の概要", 6), ("業界の仕組みとお金の流れ", 6), ("最新決算", 10)):
        m = re.search(r"^#{1,3} [^\n]*" + h + r"[^\n]*\n(.*?)(?=^#{1,3} |\Z)", t, re.M | re.S)
        if m:
            body = m.group(1)
            if len(re.sub(r"\s", "", body)) < 300 or len(NUM.findall(body)) < need_num:
                g.e(f"「{h}」の節が薄い(300 字以上・数字 {need_num} 個以上。読み手が事業と直近の数字を知らないまま分析に進ませない)")
    fp_ = os.path.join(d, "facts.json")
    if os.path.exists(fp_):
        asof = str(load(fp_).get("as_of", ""))
        mq = re.search(r"Q([1-4])\s*(\d{4})", asof)
        m = re.search(r"^#{1,3} [^\n]*最新決算[^\n]*\n(.*?)(?=^#{1,3} |\Z)", t, re.M | re.S)
        if mq and m:
            q, y = mq.group(1), mq.group(2)
            pat = rf"(第\s*{q}\s*四半期|{q}\s*Q|Q\s*{q})"
            if not re.search(pat, m.group(0)):
                g.e(f"「最新決算」の節に、台帳の基準時点({asof})の四半期が書かれていない(最新の決算を反映する)")
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


CHANGE_KEYS = ["demand", "product_mix", "pricing", "value_chain", "unit_economics", "cost_structure", "capacity",
               "capital_intensity", "cash", "balance_sheet", "returns", "moat", "cyclicality", "management", "market_view"]
PLACEHOLDER = re.compile(r"^\s*$|^\(.*\)$|\|")      # 空・ひな形の括弧書き・選択肢のままの値


def g_hypotheses(d):
    """仮説台帳(analysis-playbook.md §2〜§3)。仮説が反証できる形か、判定に根拠があるか、立て直した跡があるか。"""
    g = Gate("hypotheses")
    path = os.path.join(d, "hypotheses.json")
    if not os.path.exists(path):
        g.e("hypotheses.json が無い(templates/hypotheses.json を写して作る)")
        return g.done()
    x = load(path)
    hs = x.get("hypotheses", [])
    facts = {}
    fp = os.path.join(d, "facts.json")
    if os.path.exists(fp):
        facts = {f.get("id") for f in load(fp).get("facts", [])}
    plan = x.get("plan", {})
    for q in ("Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7"):
        v = plan.get(q, "")
        if not isinstance(v, str) or len(v.strip()) < 10 or PLACEHOLDER.search(v):
            g.e(f"plan.{q} が空(着手の宣言: 7 つの問いそれぞれに、この会社での最初の見立てを 1 文で書く。analysis-playbook.md §1)")
    if not x.get("read"):
        g.e("read(着手の前に読んだスキルの節の一覧)が空。SKILL.md・analysis-playbook.md §1〜§3・must-rules.md を読んでから始める")
    if len(hs) < 6:
        g.e(f"仮説が {len(hs)} 個しかない(6 個以上。サンキー図・会社の言葉・同業との差・市場の反応から拾う)")
    waves = [w for w in x.get("waves", []) if w.get("done")]
    if len(waves) < 4:
        g.e(f"終えた調査の波が {len(waves)} 個(波 0〜3 は必ず終える。波 4・5 は工程 5〜7 で終える)")
    for wv in waves:
        if not wv.get("evidence"):
            g.e(f"波 {wv.get('no')}: done なのに evidence(作った成果物のファイル名か台帳の id)が無い。形だけの完了にしない")
    w0 = next((wv for wv in x.get("waves", []) if wv.get("no") == 0), {})
    if w0.get("done") and len(w0.get("whys") or []) < 5:
        g.e("波 0: whys(サンキー図を読んで出た「なぜ」)が 5 個未満。問いが出るまで図を読む")
    ids = {h.get("id") for h in hs}
    results = [h.get("result") for h in hs]
    for h in hs:
        hid = h.get("id", "?")
        for k in ("question", "claim", "if_true", "if_false"):
            v = h.get(k, "")
            if not isinstance(v, str) or PLACEHOLDER.search(v) or len(v) < 8:
                g.e(f"{hid}: {k} が空かひな形のまま(反証できる一文で書く)")
        if not h.get("research"):
            g.e(f"{hid}: research(調べる資料と数字)が無い")
        r = h.get("result")
        if r not in ("支持", "棄却", "一部", "未決"):
            g.e(f"{hid}: result は 支持・棄却・一部・未決 のどれか")
        if r in ("支持", "棄却", "一部"):
            ev = h.get("evidence") or []
            if not ev:
                g.e(f"{hid}: 判定({r})に根拠(台帳の id)が無い")
            elif facts and not any(e in facts for e in ev):
                g.e(f"{hid}: evidence {ev} が台帳 facts.json に無い")
        if r in ("棄却", "一部", "未決") and not h.get("next"):
            g.e(f"{hid}: {r} のときは next(再仮説・追加調査・判別 KPI に回す)を書く")
        if h.get("parent") and h["parent"] not in ids:
            g.e(f"{hid}: parent {h['parent']} が台帳に無い")
        if not h.get("value_link"):
            g.w(f"{hid}: value_link(価値の芯の変数か条件番号)が無い。価値に効かない仮説は後回しでよい")
    # 対立仮説(thinking-moves.md 型 3): 価値の芯に関わる仮説を「支持」にするには、対立仮説を 2 つ以上消すか、残した先を書く
    with_rivals = 0
    for h in hs:
        hid, rv = h.get("id", "?"), h.get("rivals") or []
        if rv:
            with_rivals += 1
        if h.get("result") == "支持" and "芯" in str(h.get("value_link", "")) and len(rv) < 2:
            g.e(f"{hid}: 価値の芯に関わる仮説を「支持」にするには、対立仮説 rivals が 2 つ以上要る(一時・循環の説明と、業界共通・会計などのつまらない説明)")
        for i, r in enumerate(rv, 1):
            if not isinstance(r.get("claim"), str) or len(r["claim"]) < 8 or not isinstance(r.get("tell"), str) or len(r["tell"]) < 6:
                g.e(f"{hid}.rivals[{i}]: claim(対立する説明)と tell(それが真なら見えるはずの、見分ける数字)が要る")
            v = r.get("verdict")
            if v not in ("棄却", "一部", "残る"):
                g.e(f"{hid}.rivals[{i}]: verdict は 棄却・一部・残る のどれか")
            if v in ("棄却", "一部"):
                kb = r.get("killed_by") or []
                if not kb or (facts and not any(e in facts for e in kb)):
                    g.e(f"{hid}.rivals[{i}]: {v} なのに killed_by(消した証拠。台帳の id)が無いか、台帳に無い")
            if v == "残る" and not (isinstance(r.get("kept_as"), str) and len(r["kept_as"]) >= 6):
                g.e(f"{hid}.rivals[{i}]: 残る対立仮説は kept_as(どのシナリオ・確率・判別 KPI に残したか)を書く")
    if hs and with_rivals < 2:
        g.e(f"対立仮説 rivals を立てた仮説が {with_rivals} 個(2 個以上。上位の驚きには、説明を 3 つ並べて見分ける数字で消す。thinking-moves.md 型 3)")
    if hs and not any(r in ("棄却", "一部") for r in results):
        g.e("棄却・一部が 1 つも無い。確かめたのではなく探しただけになっている(最初の見立てを疑って確かめ直す)")
    if any(r == "棄却" for r in results) and not any(h.get("parent") for h in hs):
        g.e("棄却した仮説があるのに、立て直した仮説(parent つき)が無い。粒度・時間軸・因果の向き・主体を変えて立て直す(§3-4)")
    ins = x.get("insights", [])
    if len(ins) < 3:
        g.e(f"insights が {len(ins)} 個(3 個以上。開示のままでは見えず、復元・逆算・換算して初めて言える示唆を書く。§7・§8)")
    for i, it in enumerate(ins, 1):
        for k in ("claim", "lens", "so_what"):
            v = it.get(k, "")
            if not isinstance(v, str) or len(v.strip()) < 4 or PLACEHOLDER.search(v):
                g.e(f"insights[{i}]: {k} が空(claim=示唆の一文、lens=使った切り口、so_what=価値・時期・行動のどれにどう効くか)")
        if not re.search(r"\d", str(it.get("claim", ""))):
            g.e(f"insights[{i}]: claim に数字が無い(社名を替えると成り立たない数字を入れる)")
        if it.get("in_disclosure") is not False:
            g.e(f"insights[{i}]: in_disclosure が false でない。開示にそのまま載っている数字の並べ替えは示唆に数えない")
        ev = it.get("evidence") or []
        if not ev or (facts and not any(e in facts for e in ev)):
            g.e(f"insights[{i}]: evidence(台帳の id)が無いか、台帳に無い")
        if it.get("level") not in (2, 3, 4, 5):
            g.e(f"insights[{i}]: level(深さの梯子 2〜5。analysis-playbook.md §8)が無い。1(開示の写し)は示唆に数えない")
        if not re.search(r"価値|株価|EPS|ROE|時期|日|月|行動|買|売|判別|KPI", str(it.get("so_what", ""))):
            g.w(f"insights[{i}]: so_what が価値・時期・行動に着地していない")
    undecided = [h.get("id") for h in hs if h.get("result") == "未決" and "芯" in str(h.get("value_link", ""))]
    if undecided:
        g.e(f"価値の芯に関わる仮説が未決のまま: {undecided}(決着させるか、判別 KPI と日付に回して next に書く)")
    return g.done()


def g_change(d):
    """変化の評価表(analysis-playbook.md §5)。15 項目を過去・現在・将来で対比しているか。"""
    g = Gate("change")
    path = os.path.join(d, "change_map.json")
    if not os.path.exists(path):
        g.e("change_map.json が無い(templates/change_map.json を写して作る)")
        return g.done()
    x = load(path)
    items = {i.get("key"): i for i in x.get("items", [])}
    facts = set()
    fp = os.path.join(d, "facts.json")
    if os.path.exists(fp):
        facts = {f.get("id") for f in load(fp).get("facts", [])}
    for k in CHANGE_KEYS:
        if k not in items:
            g.e(f"項目 {k} が無い(15 項目を全部書く。変わらない項目は 不変 と書く)")
            continue
        it = items[k]
        for col in ("past", "now", "future"):
            v = it.get(col, "")
            if not isinstance(v, str) or len(v.strip()) < 4:
                g.e(f"{k}: {col} が空(過去・現在・将来を同じ指標で並べる)")
        if not re.search(r"\d", str(it.get("now", "")) + str(it.get("future", ""))):
            g.w(f"{k}: 現在・将来に数字が無い(指標で対比する)")
        dr = it.get("direction")
        if dr not in ("改善", "悪化", "不変"):
            g.e(f"{k}: direction は 改善・悪化・不変 のどれか")
        if it.get("priced") not in ("済", "一部", "未", "不明"):
            g.e(f"{k}: priced は 済・一部・未・不明 のどれか")
        drv = it.get("driver", "")
        if not isinstance(drv, str) or len(drv.strip()) < 6 or PLACEHOLDER.search(drv):
            g.e(f"{k}: driver(変える力、不変ならその理由)が空")
        if dr in ("改善", "悪化"):
            ev = it.get("evidence") or []
            if not ev:
                g.e(f"{k}: 変化({dr})の根拠(台帳の id)が無い")
            elif facts and not any(e in facts for e in ev):
                g.e(f"{k}: evidence {ev} が台帳 facts.json に無い")
            w = it.get("when", "")
            if not isinstance(w, str) or not re.search(r"\d", w):
                g.e(f"{k}: when(数字に出る時期・確認日)に日付や期が無い")
    changed = [i for i in items.values() if i.get("direction") in ("改善", "悪化")]
    if len(changed) < 3:
        g.w("変化のある項目が 3 個未満。過去の延長で将来を置いていないか(段差・体制の転換を探す)")
    if not any(i.get("direction") == "改善" and i.get("priced") in ("未", "一部") for i in items.values()) and        not any(i.get("direction") == "悪化" and i.get("priced") in ("未", "一部") for i in items.values()):
        g.w("市場が織り込んでいない変化が 1 つも無い → 結論は「エッジなし」になる(工程 5 の edge を false に)")
    cp = os.path.join(d, "conditions.json")
    if os.path.exists(cp):
        linked = {c for i in items.values() for c in (i.get("cond") or [])}
        if len(linked) < 6:
            g.w(f"条件番号に紐づく項目が少ない({len(linked)} 条件)。13 条件の現在と将来は、この表から導く")
    return g.done()


VC_STAGES = ("原料", "自社", "顧客", "最終需要")


def g_map(d):
    """事業の地図 business_map.json(analysis-playbook.md §4)。製品群の地図とバリューチェーン図が構造として書かれているか。"""
    g = Gate("map")
    path = os.path.join(d, "business_map.json")
    if not os.path.exists(path):
        g.e("business_map.json が無い(templates/business_map.json を写して作る)")
        return g.done()
    x = load(path)
    ps = x.get("products", [])
    if len(ps) < 4:
        g.e(f"製品群が {len(ps)} 個(決算短信の品目別の記述を全品目。4 個以上)")
    cov = x.get("coverage_pct")
    if not isinstance(cov, (int, float)) or cov < 90:
        g.e("coverage_pct(製品群で説明できる売上の比率)が 90 未満か未記入")
    moves = set()
    for p in ps:
        n = p.get("name", "?")
        for k in ("segment", "use", "position", "quote"):
            v = p.get(k, "")
            if not isinstance(v, str) or len(v.strip()) < 2 or PLACEHOLDER.search(v):
                g.e(f"製品群 {n}: {k} が空(segment=セグメント、use=用途・顧客の業界、position=会社の位置づけ、quote=決算短信の記述)")
        mv = p.get("move")
        if mv not in ("数量増", "値上げで補う", "減収", "不明"):
            g.e(f"製品群 {n}: move は 数量増・値上げで補う・減収・不明 のどれか")
        moves.add(mv)
    if ps and sum(1 for p in ps if p.get("move") == "不明") > len(ps) / 3:
        g.e("move が不明の製品群が 3 分の 1 を超える(品目別の記述を読み直す)")
    if ps and not any(p.get("strategic") for p in ps):
        g.w("strategic(会社の戦略テーマ)の印が付いた製品群が無い。中計の重点と重ねる")
    chains = x.get("value_chains", [])
    if len(chains) < 2:
        g.e(f"バリューチェーンが {len(chains)} 本(成長分野と現金を稼ぐ分野の両方で 2 本以上)")
    for c in chains:
        cn = c.get("name", "?")
        stages = {s_.get("stage"): s_ for s_ in c.get("stages", [])}
        for st in VC_STAGES:
            if st not in stages:
                g.e(f"バリューチェーン {cn}: 段 {st} が無い(原料 → 自社 → 顧客 → 最終需要)")
                continue
            for k in ("who", "pricing", "why_chosen"):
                v = stages[st].get(k, "")
                if not isinstance(v, str) or len(v.strip()) < 2 or PLACEHOLDER.search(v):
                    g.e(f"バリューチェーン {cn} の {st}: {k} が空(who=誰、pricing=値決め、why_chosen=選ばれる理由・切り替えの費用)")
        if not c.get("outside_evidence"):
            g.e(f"バリューチェーン {cn}: outside_evidence(顧客・競合・仕入先・市況など、会社の外の開示で確かめた台帳の id)が無い")
        if not c.get("profit_pool") or PLACEHOLDER.search(str(c.get("profit_pool"))):
            g.e(f"バリューチェーン {cn}: profit_pool(どの段が利益を取っているか)が空")
        if not re.search(r"\d", str(c.get("demand_growth", ""))):
            g.e(f"バリューチェーン {cn}: demand_growth(最終需要・市場の成長率。出所 2 つ以上が望ましい)に数字が無い")
    return g.done()


DATEISH = re.compile(r"\d{4}[-/年]\s?\d{1,2}|\d{1,2}月|FY\d{2,4}|Q[1-4]|四半期|通期|決算")


def _facts_ids(d):
    fp = os.path.join(d, "facts.json")
    return {f.get("id") for f in load(fp).get("facts", [])} if os.path.exists(fp) else set()


def g_lenses(d):
    """示唆の種(analysis-playbook.md §7)。lenses.py の旗を、仮説か示唆に使ったか、理由を付けて捨てたか。"""
    g = Gate("lenses")
    lp, hp = os.path.join(d, "lenses.json"), os.path.join(d, "hypotheses.json")
    if not os.path.exists(lp):
        g.e("lenses.json が無い(templates/series.json を写して埋め、python3 scripts/lenses.py <作業フォルダ> を実行する)")
        return g.done()
    x = load(lp)
    ls = x.get("lenses", [])
    ok = [l for l in ls if l.get("status") == "ok"]
    lack = [l.get("id") for l in ls if l.get("status") == "入力不足"]
    if len(ok) < 8:
        g.e(f"計算できたレンズが {len(ok)} 本(8 本以上。series.json に annual・periods・guidance・segments・peers・price を足す)")
    if lack:
        (g.e if len(lack) > 5 else g.w)(f"入力不足のレンズ: {lack}(series.json に値を足すか、開示が無いなら skip に理由を書く)")
    flags = [f.get("id") for l in ls for f in (l.get("flags") or [])]
    if not flags:
        g.w("旗が 1 本も立っていない(入力が少なすぎないか。series.json を見直す)")
    used, dismissed = set(), {}
    if os.path.exists(hp):
        h = load(hp)
        for it in (h.get("hypotheses") or []) + (h.get("insights") or []):
            sd = it.get("seed")
            for v in (sd if isinstance(sd, list) else [sd]):
                if v:
                    used.add(v)
        for it in h.get("seeds_dismissed") or []:
            if it.get("id") and len(str(it.get("why", "")).strip()) >= 6:
                dismissed[it["id"]] = it["why"]
    for f in flags:
        if f not in used and f not in dismissed:
            g.e(f"旗 {f} が使われていない(hypotheses.json の仮説か示唆の seed に書く。使わないなら seeds_dismissed に id と理由)")
    if flags and len(dismissed) > len(flags) * 0.6:
        g.e(f"旗の {len(dismissed)}/{len(flags)} を捨てている(6 割超)。異常値を説明せずに先へ進んでいる")
    if flags and not used:
        g.e("旗から立てた仮説・示唆が 1 つも無い")
    return g.done()


def g_thesis(d):
    """投資仮説(analysis-playbook.md §6・§8・§2 の波 5)。市場との差分が同じ単位の数字で並び、価値の芯と撤回の線があり、
    示唆が深さの梯子の上段まで届き、弱気の反論を数字で検証して評価に入れたか。"""
    g = Gate("thesis")
    hp = os.path.join(d, "hypotheses.json")
    if not os.path.exists(hp):
        g.e("hypotheses.json が無い")
        return g.done()
    x = load(hp)
    facts = _facts_ids(d)
    vp = os.path.join(d, "valuation.json")
    val = load(vp) if os.path.exists(vp) else None

    def has(v, n=4):
        return isinstance(v, str) and len(v.strip()) >= n and not PLACEHOLDER.search(v)

    def dig(v):
        return bool(re.search(r"\d", str(v or "")))

    # 1) 示唆の深さ
    ins = x.get("insights", [])
    by_id = {it.get("id"): it for it in ins if it.get("id")}
    if len(ins) < 5:
        g.e(f"insights が {len(ins)} 個(最終は 5 個以上)")
    if len(by_id) != len(ins):
        g.e("insights に id(I1, I2 …)が無いものがある")
    lv = [it.get("level") for it in ins]
    if sum(1 for v in lv if isinstance(v, int) and v >= 4) < 3:
        g.e("深さ 4 以上(市場の前提との差分に値段と日付が付いた示唆)が 3 個未満。逆算・同業の線・感応度の換算で市場の前提を数字にする")
    if not any(v == 5 for v in lv):
        g.e("深さ 5(弱気の反論を検証して残り、撤回の線がある示唆)が 1 つも無い")
    rebs = x.get("rebuttals", [])
    rid = {r.get("id") for r in rebs}
    for it in ins:
        iid, v = it.get("id", "?"), it.get("level")
        if isinstance(v, int) and v >= 3 and not has(str(it.get("outside") or ""), 6):
            g.e(f"{iid}: 深さ {v} なのに outside(会社の外の数字での確認: 同業・顧客・原料市況・市場規模・過去の自然実験)が無い")
        if isinstance(v, int) and v >= 4:
            if not (has(it.get("market_view"), 6) and dig(it.get("market_view"))):
                g.e(f"{iid}: 深さ {v} なのに market_view(市場・通説・会社予想が前提にしている数字)が無い")
            if not isinstance(it.get("value_per_share"), (int, float)) or it.get("value_per_share") == 0 or not has(it.get("value_via"), 3):
                g.e(f"{iid}: 深さ {v} なのに value_per_share(1 株あたりの価値への効き。valuate.py の感応度・シナリオ・交差確認から写す)と value_via が無い")
            if not (has(it.get("date"), 4) and DATEISH.search(str(it.get("date")))):
                g.e(f"{iid}: 深さ {v} なのに date(数字に出る日・織り込まれる契機の日付)が無い")
        if v == 5:
            if not (has(it.get("falsifier"), 6) and dig(it.get("falsifier"))):
                g.e(f"{iid}: 深さ 5 なのに falsifier(この数字がこうなったら撤回する、の線)が無い")
            tb = it.get("tested_by") or []
            if not tb or not all(t in rid for t in tb):
                g.e(f"{iid}: 深さ 5 なのに tested_by(検証した弱気の反論の id)が無いか、rebuttals に無い")

    # 示唆の値段は、計算機の数字と対応していること(手で作った値段を使わない)
    if val:
        cands = [abs(s_.get("diff") or 0) for s_ in val.get("sensitivities", [])]
        ent = val.get("entry") or {}
        px = ((ent.get("by_price") or {}).get("last") or {}).get("price")
        base = [ent.get(k) for k in ("B", "U", "L") if isinstance(ent.get(k), (int, float))]
        for b in base:
            if px:
                cands.append(abs(b - px))
            cands += [abs(b - o) for o in base if o != b]
        for it in ins:
            v = it.get("value_per_share")
            if (it.get("level") or 0) >= 4 and isinstance(v, (int, float)) and v != 0:
                if not any(abs(abs(v) - c) <= max(2, c * 0.02) for c in cands if c):
                    if isinstance(it.get("value_calc"), str) and len(it["value_calc"]) >= 10:
                        g.w(f"{it.get('id')}: value_per_share {v} は valuation.json に対応する数字が無い(value_calc の式で説明している)")
                    else:
                        g.e(f"{it.get('id')}: value_per_share {v} が valuation.json のどの数字(感応度の差・理論株価と現在値の差・シナリオの差)とも対応しない。"
                            "計算機の数字を写すか、計算し直した式を value_calc に書く")
    for it in ins:
        if it.get("level") == 5 and it.get("falsifier") and not DATEISH.search(str(it.get("falsifier"))):
            g.e(f"{it.get('id')}: falsifier に、測れる日(決算の日付や期)が無い。その日に開示される数字で書く")

    # 2) 市場との差分・価値の芯・撤回の線
    t = x.get("thesis") or {}
    if not t:
        g.e("thesis(投資仮説)が無い。templates/hypotheses.json の thesis を埋める")
    else:
        if not (has(t.get("one_line"), 20) and dig(t.get("one_line"))):
            g.e("thesis.one_line(市場の前提 → 自分の見立て → 差 → 埋まる時期、を数字入りの 1 文で)が空")
        if t.get("edge_type") not in ("情報", "分析", "時間軸", "行動", "エッジなし"):
            g.e("thesis.edge_type は 情報・分析・時間軸・行動・エッジなし のどれか")
        var = t.get("variant") or []
        if len(var) < 3:
            g.e(f"thesis.variant(市場の前提 | 自分の見立て の差分の表)が {len(var)} 行(3 行以上)")
        for i, r in enumerate(var, 1):
            if not (dig(r.get("market")) and dig(r.get("ours"))):
                g.e(f"thesis.variant[{i}]: market と ours の両方に数字が要る(同じ単位で並べる)")
            if not has(r.get("item"), 2) or not has(r.get("unit"), 1):
                g.e(f"thesis.variant[{i}]: item(何の数字か)と unit(単位)が要る")
            if not (r.get("basis") and (not facts or any(b in facts for b in r["basis"]))):
                g.e(f"thesis.variant[{i}]: basis(台帳の id)が無いか、台帳に無い")
            if not (has(r.get("closes_when"), 6) and DATEISH.search(str(r.get("closes_when")))):
                g.e(f"thesis.variant[{i}]: closes_when(差が埋まる契機と日付)が無い")
            if r.get("insight") and r["insight"] not in by_id:
                g.e(f"thesis.variant[{i}]: insight {r['insight']} が insights に無い")
        core = t.get("core") or {}
        for k in ("variable", "kpi", "go", "stop", "date"):
            if not has(str(core.get(k, "")), 2):
                g.e(f"thesis.core.{k} が空(価値の芯の変数・判別 KPI・続行の線・見直しの線・確認日)")
        if core and not (dig(core.get("go")) and dig(core.get("stop"))):
            g.e("thesis.core の go・stop は数字の線で書く")
        if core.get("insight") not in by_id:
            g.e("thesis.core.insight(芯を特定した示唆の id)が insights に無い")
        elif (by_id[core["insight"]].get("level") or 0) < 4:
            g.e("thesis.core.insight の示唆が深さ 4 未満")
        kill = t.get("kill") or []
        if len(kill) < 2 or not all(dig(k.get("if")) and has(k.get("then"), 4) for k in kill):
            g.e("thesis.kill(撤回の線: if=数字の条件、then=どうするか)が 2 本以上要る")
        elif not all(DATEISH.search(str(k.get("if"))) for k in kill):
            g.e("thesis.kill の if に、測れる日(決算の日付や期)が無いものがある。その日に開示される数字で書く")
        if has(t.get("one_line"), 20) and "撤回" not in t["one_line"] and "見直" not in t["one_line"]:
            g.e("thesis.one_line に撤回の線が無い(市場の前提 → 自分の見立て → 差 → 時期 → 何が起きたら撤回するか、の 5 つを 1 文に入れる)")
        if val:
            sens = {s_.get("name"): s_.get("diff") for s_ in val.get("sensitivities", [])}
            sn = core.get("sensitivity")
            if sn not in sens:
                g.e(f"thesis.core.sensitivity「{sn}」が valuation.json の感応度に無い(候補の変数を EPS の倍率に直して sensitivities に入れ、計算し直す)")
            elif isinstance(core.get("per_share"), (int, float)) and abs(abs(sens[sn]) - abs(core["per_share"])) > max(2, abs(sens[sn]) * 0.02):
                g.e(f"thesis.core.per_share {core.get('per_share')} が valuation.json の {sens[sn]:.0f} と合わない")
            dec = t.get("decision") or {}
            vd = ((val.get("decision") or {}).get("last") or {}).get("decision")
            if vd and dec.get("action") != vd:
                g.e(f"thesis.decision.action「{dec.get('action')}」が valuation.json の判断「{vd}」と違う(判断は計算機の出力を写す)")
            vb = (val.get("entry") or {}).get("B")
            if vb and isinstance(dec.get("value"), (int, float)) and abs(dec["value"] - vb) > max(1, vb * 0.005):
                g.e(f"thesis.decision.value {dec.get('value')} が valuation.json の理論株価 {vb:.0f} と違う")
        else:
            g.w("valuation.json が無いので、芯の感応度と判断の照合を省いた")

    # 2b) 価値の橋: 株価と理論株価の差を、名前のある段で全部説明する(thinking-moves.md「円に直して並べる」)
    br = (t.get("bridge") or {}) if t else {}
    steps = br.get("steps") or []
    if t and len(steps) < 2:
        g.e("thesis.bridge(価値の橋: 現在値 → 今の利益が続く場合の価値 → 成長と変化の上乗せ → 理論株価。lenses.py の L18)が無い。"
            "差を段に分け、各段を示唆に結び付ける")
    elif t:
        if not all(isinstance(st.get("per_share"), (int, float)) and has(st.get("name"), 4) for st in steps):
            g.e("thesis.bridge.steps: 各段に name と per_share(1 株あたりの円)が要る")
        elif isinstance(br.get("from"), (int, float)) and isinstance(br.get("to"), (int, float)):
            tot = br["from"] + sum(st["per_share"] for st in steps)
            if abs(tot - br["to"]) > max(2, abs(br["to"]) * 0.01):
                g.e(f"thesis.bridge: from {br['from']} + 段の合計 = {tot:.0f} が to {br['to']} と合わない(差を全部説明する。残りは「その他」の段に)")
            if val:
                vb = (val.get("entry") or {}).get("B")
                px = (((val.get("entry") or {}).get("by_price") or {}).get("last") or {}).get("price")
                if vb and abs(br["to"] - vb) > max(1, vb * 0.005):
                    g.e(f"thesis.bridge.to {br['to']} が valuation.json の理論株価 {vb:.0f} と違う")
                if px and abs(br["from"] - px) > max(1, px * 0.005):
                    g.e(f"thesis.bridge.from {br['from']} が valuation.json の株価 {px:.0f} と違う")
        else:
            g.e("thesis.bridge に from(現在値)と to(理論株価)が要る")
        if steps and not any(st.get("insight") in by_id for st in steps):
            g.e("thesis.bridge.steps: どの段も示唆(insight の id)に結び付いていない")

    # 2c) 作業仮説の書き直し: 調査の波ごとに一文を書き直し、何が結論を動かしたかを残す
    tl = x.get("thesis_log") or []
    if len(tl) < 3:
        g.e(f"thesis_log(調査の波ごとに書き直した作業仮説の一文)が {len(tl)} 個(3 個以上。最初の見立て → 波ごとの書き直し → 最終)")
    else:
        if not all(has(e_.get("one_line"), 12) for e_ in tl):
            g.e("thesis_log: 各行に one_line(その時点の結論の一文)が要る")
        if len({str(e_.get("one_line")) for e_ in tl}) < 2 or not any(has(str(e_.get("changed_because") or ""), 8) for e_ in tl[1:]):
            g.e("thesis_log: 結論が一度も動いていない(changed_because が無い)。調査が結論を動かしていないなら、裏づけ探しになっている")

    # 2d) 予測の登録: 日付と確率つきの予測を残し、決算ごとに答え合わせする
    pr = x.get("predictions") or []
    if len(pr) < 3:
        g.e(f"predictions(日付と確率つきの予測)が {len(pr)} 個(3 個以上。決算で当たり外れが決まる数字で書く)")
    for i, q in enumerate(pr, 1):
        if not (has(q.get("statement"), 8) and dig(q.get("statement")) and DATEISH.search(str(q.get("date") or ""))):
            g.e(f"predictions[{i}]: statement(数字で当たり外れが決まる文)と date(決まる日)が要る")
        if not (isinstance(q.get("p"), (int, float)) and 0 < q["p"] < 1):
            g.e(f"predictions[{i}]: p(当たる確率。0 と 1 の間)が要る")
        if not has(str(q.get("basis") or ""), 8):
            g.e(f"predictions[{i}]: basis(その確率にした根拠。基準率から何をどれだけ動かしたか)が要る")
    if pr and not any(q.get("on_core") for q in pr):
        g.e("predictions に、価値の芯の判別 KPI についての予測(on_core: true)が無い")

    # 2e) 基準率: 確率は、過去の実績の数え上げ(外の見方)から出発する
    bs = x.get("base_rates") or []
    if len(bs) < 2:
        g.e(f"base_rates(基準率)が {len(bs)} 個(2 個以上。この会社の過去・同業の過去で、同じことが何回中何回起きたかを数える。"
            "会社予想の癖は lenses.py の L19)")
    for i, b in enumerate(bs, 1):
        if not (has(b.get("claim"), 6) and has(b.get("reference_class"), 6)):
            g.e(f"base_rates[{i}]: claim(何の確率か)と reference_class(何を数えたか)が要る")
        if not (isinstance(b.get("n"), int) and isinstance(b.get("hit"), int) and 0 <= b["hit"] <= b["n"]):
            g.e(f"base_rates[{i}]: n(数えた回数)と hit(起きた回数)が要る")
        elif b["n"] < 3:
            g.w(f"base_rates[{i}]: n が {b['n']} 回しかない(基準率として弱い。期間を延ばすか同業を足す)")
        if not has(str(b.get("adjust") or ""), 8):
            g.e(f"base_rates[{i}]: adjust(基準率から今回の確率へ、何を根拠にどれだけ動かしたか)が要る")

    # 3) 弱気の反論
    if len(rebs) < 5:
        g.e(f"rebuttals(弱気の反論)が {len(rebs)} 個(5 個以上。別のモデルに全文を渡して出させ、1 つずつデータで決着させる)")
    for r in rebs:
        rr = r.get("id", "?")
        if not has(r.get("claim"), 8) or not has(r.get("data"), 6):
            g.e(f"{rr}: claim(反論)と data(決着させたデータ)が要る")
        if r.get("verdict") not in ("逆", "正しい", "一部", "未決"):
            g.e(f"{rr}: verdict は 逆・正しい・一部・未決 のどれか")
        ev = r.get("evidence") or []
        if r.get("verdict") in ("逆", "正しい", "一部") and (not ev or (facts and not any(e in facts for e in ev))):
            g.e(f"{rr}: evidence(台帳の id)が無いか、台帳に無い")
        if r.get("verdict") in ("正しい", "一部") and not has(r.get("reflected"), 6):
            g.e(f"{rr}: 正しい反論なのに reflected(価値評価のどの前提・感応度・判別 KPI に入れたか)が無い")
        if r.get("verdict") == "未決" and not (has(r.get("kpi"), 6) and DATEISH.search(str(r.get("kpi")))):
            g.e(f"{rr}: 未決なら kpi(何を、いつ見て決着させるか)が要る")
    if rebs and not any(r.get("on_core") for r in rebs):
        g.e("価値の芯(thesis.core)を狙った反論(on_core: true)が 1 つも無い")
    if len(rebs) >= 5 and not any(r.get("verdict") in ("正しい", "一部") for r in rebs):
        g.w("反論が全部「逆」か「未決」。弱い反論しか出していないか、都合よく判定していないか(正しい反論は前提に入れて計算し直す)")
    w5 = next((w for w in x.get("waves", []) if w.get("no") == 5), {})
    if not w5.get("done"):
        g.e("調査の波 5(反証)が done になっていない")

    # 4) 深さの審査(depth-review.md)。自分で採点しない
    revs = x.get("reviews") or []
    stages = {r.get("stage") for r in revs}
    if "示唆" not in stages:
        g.e("reviews に、示唆の審査(stage: 示唆)が無い。別のモデルに示唆のカードと投資仮説を審査させる(references/depth-review.md 依頼文 3)")
    if not stages & {"構造", "仮説"}:
        g.e("reviews に、構造か仮説の審査(stage: 構造・仮説)が無い(depth-review.md 依頼文 1・2)")
    for r in revs:
        st = r.get("stage", "?")
        if st not in ("構造", "仮説", "示唆"):
            g.e(f"reviews: stage は 構造・仮説・示唆 のどれか({st})")
        if not has(str(r.get("by") or ""), 3):
            g.e(f"reviews[{st}]: by(審査したモデル)が無い")
        elif "自己" in str(r.get("by")):
            g.w(f"reviews[{st}]: 自己審査になっている(別のモデルかサブエージェントに審査させる)")
        if not isinstance(r.get("findings"), int) or r.get("findings") < 1:
            g.e(f"reviews[{st}]: findings(指摘の数)が 0 か無い。何も指摘しない審査は審査になっていない(モデルを上げてやり直す)")
        for dn in r.get("downgraded") or []:
            if dn.get("id") not in by_id:
                g.e(f"reviews[{st}]: downgraded の id {dn.get('id')} が insights に無い")
            elif not has(str(dn.get("action") or ""), 6):
                g.e(f"reviews[{st}]: {dn.get('id')} は段を下げられたのに action(足したもの、または下げたままにした理由)が無い")
            elif isinstance(dn.get("to"), int) and (by_id[dn["id"]].get("level") or 0) > dn["to"] and "上げ直" not in str(dn.get("action")) and "追加" not in str(dn.get("action")):
                g.e(f"reviews[{st}]: {dn.get('id')} は審査で段 {dn['to']} とされたが、level が {by_id[dn['id']].get('level')} のまま。足して上げ直した(action に「追加」)か、level を直す")
    return g.done()


# ---------------------------------------------------------------- 事業構造の解剖(工程 2A)と 13 条件の深掘り
STRUCT_BLOCKS = ["customer", "stakeholders", "cases", "atom", "loop", "advantage", "new_product_margin", "industry", "competitors",
                 "wallet", "money", "mechanisms"]


def _filled(v, n=4):
    return isinstance(v, str) and len(v.strip()) >= n and not PLACEHOLDER.search(v.strip())


def _n(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def _pos(v):
    return _n(v) and v != 0


def g_structure(d):
    """事業構造の解剖(references/structure-anatomy.md)。12 区画が、数字と根拠つきで埋まっているか。"""
    g = Gate("structure")
    p = os.path.join(d, "structure.json")
    if not os.path.exists(p):
        g.e("structure.json がない(templates/structure.json を写し、references/structure-anatomy.md の 12 区画を埋める。13 条件の採点はその後)")
        return g.done()
    x, ids = load(p), _facts_ids(d)
    na = {str(a.get("block")): a for a in x.get("na", []) if _filled(str(a.get("why", "")), 8)}
    na = {k: v for k, v in na.items() if k in STRUCT_BLOCKS}
    if len(na) > 2:
        g.e(f"対象外(na)の区画が {len(na)} 個。2 個まで(開示が無ければ、上下の会社・統計・料金表・別の明細からの逆算で推定する)")

    def ev(obj, tag, need_outside=False):
        e_ = obj.get("evidence") or []
        if not e_ or (ids and not any(i in ids for i in e_)):
            g.e(f"{tag}: evidence(台帳の id)が無いか、台帳に無い")
        if need_outside and not any(_filled(str(o), 6) for o in (obj.get("outside") or [])):
            g.e(f"{tag}: outside(会社の外の根拠: 統計・顧客や競合の開示・料金表)が無い")

    if not (_filled(x.get("one_line", ""), 80) and re.search(r"\d", x.get("one_line", ""))):
        g.e("one_line: お金の流れの一文(型 1 の最終版)が短い・数字が無い")
    su = [s_ for s_ in x.get("surprises", []) if _filled(s_.get("fact", ""), 10) and _filled(s_.get("source", ""), 3)]
    if len(su) < 10:
        g.e(f"surprises(一次資料を主任が読んで知った事実)が {len(su)} 個。10 個以上、出所つきで(要約や下請けの報告で代えない)")

    if "customer" not in na:
        c = x.get("customer", {})
        rows = [r_ for r_ in c.get("pnl", []) if _filled(r_.get("item", ""), 2) and _pos(r_.get("value")) and _filled(r_.get("source", ""), 3)]
        if len(rows) < 4:
            g.e(f"customer.pnl: 顧客 1 単位の損益が {len(rows)} 行(売上・主な費用・利益を 4 行以上、数字と出所つきで)")
        is_rev = lambda it: it.startswith(("売上", "収入", "収益"))
        is_pf = lambda it: it.startswith(("利益", "収支差", "営業利益", "経常利益"))
        rv = [r_["value"] for r_ in rows if is_rev(r_["item"])]
        pf = [r_ for r_ in rows if is_pf(r_["item"])]
        cs = [r_["value"] for r_ in rows if not is_rev(r_["item"]) and not is_pf(r_["item"])]
        for p_ in pf:
            if rv and cs and abs(sum(cs) + p_["value"] - rv[0]) > 0.03 * rv[0]:
                g.e(f"customer.pnl: 費用の合計 {sum(cs):,.0f} + 「{p_['item'][:20]}」{p_['value']:,.0f} が売上 {rv[0]:,.0f} と合わない(±3% 超)。"
                    "費用と利益を同じ区分・同じ年でそろえる(利益だけ差し替えない。別の年・区分の利益は、その年・区分の費用の行とともに別の表に)")
        pp = c.get("price_paid", {})
        if not (_pos(pp.get("share_of_revenue_pct")) and _pos(pp.get("share_of_profit_pct"))):
            g.e("customer.price_paid: 払う額の、顧客の売上比と利益比の両方を書く(売上比だけで語らない)")
        vc = c.get("value_created", {})
        if not (_filled(vc.get("claim", ""), 8) and _filled(vc.get("measured", ""), 15) and re.search(r"\d", vc.get("measured", ""))):
            g.e("customer.value_created: 会社の主張(claim)と、利用者の群の外形データで測った結果(measured。数字入り)の両方を書く")
        for k, why in (("replaces", "置き換える顧客の費用科目と金額、または増やす売上"), ("payer", "顧客の収入を誰が何の単位で決めるか"),
                       ("billing_unit_fit", "自社の課金単位と顧客の収入の単位が合っているか、ずれる出来事")):
            if not _filled(c.get(k, ""), 12):
                g.e(f"customer.{k}: {why} を書く")
        ev(c, "customer", need_outside=True)

    if "stakeholders" not in na:
        sh = [t for t in x.get("stakeholders", []) if all(_filled(t.get(k, ""), 4) for k in ("who", "why_deal", "alternative", "exit_if"))]
        if len(sh) < 5:
            g.e(f"stakeholders: 当事者が {len(sh)} 者(5 者以上。なぜ取引するか・代わり・得・やめる条件)")
    if "cases" not in na:
        cs = [t for t in x.get("cases", []) if _filled(t.get("name", ""), 2) and re.search(r"\d", str(t.get("numbers", ""))) and _filled(t.get("why_different", ""), 8)]
        if len(cs) < 5:
            g.e(f"cases: 具体例が {len(cs)} 件(5 件以上。数字と、他の件と違う理由 why_different つき。平均に逃げない)")

    if "atom" not in na:
        a = x.get("atom", {})
        if not (_filled(a.get("unit", ""), 2) and _filled(a.get("engine", ""), 8)):
            g.e("atom: 原子単位(unit)とエンジン式(engine)を書く")
        er = a.get("reproduce_error_pct")
        if not _n(er):
            g.e("atom.reproduce_error_pct: エンジン式で報告売上を再現した誤差(%)を書く")
        elif abs(er) > 5:
            g.e(f"atom.reproduce_error_pct: 再現の誤差が {er}%(±5% 以内。未把握の収益源がある。工程 1 に戻る)")
        gs = a.get("growth_sources", {})
        if sum(1 for k in ("new", "expansion", "price", "churn") if _pos(gs.get(k))) < 2:
            g.e("atom.growth_sources: 増収の源泉(新規・拡張・値上げ・離脱)を数字で分ける(2 つ以上が 0 でない)")
        fl = a.get("flow", {})
        miss = [k for k in ("adds_per_year", "exit_rate_pct", "steady_state_stock", "current_stock", "inflow_share_pct", "stock_share_pct") if not _pos(fl.get(k))]
        if miss:
            g.e(f"atom.flow: {', '.join(miss)} が無い(定常の規模 = 流入 ÷ 流出率、流入のシェアと保有のシェア。structure_lenses.py の U01・U02)")
        if not _filled(str(fl.get("target_vs_flow", "")), 8):
            g.e("atom.flow.target_vs_flow: 経営陣の長期目標に要る流入が今の何倍かを書く(目標が無ければ「目標なし」と定常の規模の読み)")
        co = [t for t in a.get("cohort", []) if _filled(t.get("group", ""), 2) and _pos(t.get("unit_revenue"))]
        if len(co) < 3:
            g.e(f"atom.cohort: 群(年齢・規模)ごとの単位あたり売上が {len(co)} 点(3 点以上。開示が無ければ区分別の単価から近似し、方法を note に)")
        ue = a.get("unit_economics", {})
        if not all(_pos(ue.get(k)) for k in ("cac", "payback_months", "ltv_cac_low", "ltv_cac_high")):
            g.e("atom.unit_economics: 獲得費・回収月数・LTV/CAC の幅(low・high)を書く(structure_lenses.py の U08)")
        ev(a, "atom")

    if "loop" not in na:
        lp = x.get("loop", {})
        links = [t for t in lp.get("links", []) if _filled(t.get("from", ""), 2) and _filled(t.get("to", ""), 2)]
        if len(links) < 3:
            g.e(f"loop.links: 自己強化ループのリンクが {len(links)} 本(3 本以上)")
        if not any(str(t.get("status")) == "実証" and re.search(r"\d", str(t.get("evidence", ""))) for t in links):
            g.e("loop.links: 数字の証拠で「実証」したリンクが 1 本も無い(全部が仮説のループは、会社の資料の絵の写し)")
        if not (_filled(lp.get("constraint", ""), 10) and _filled(str(lp.get("released_on", "")), 2)):
            g.e("loop: 律速(constraint。内か外かの判定つき)と、外れる日付(released_on。無ければ「無い」)を書く")
    if "advantage" not in na:
        ad = [t for t in x.get("advantage", []) if all(_filled(t.get(k, ""), 8) for k in ("hard", "why_others_cant", "breaks_if")) and re.search(r"\d", str(t.get("worth", "")))
              and _pos(t.get("cap_years")) and _filled(str(t.get("protects", "")), 2)]
        if not ad:
            g.e("advantage: 優位の源が 3 段(何が難しいか・なぜ他社にできないか・円換算の価値 worth)で書けていない。続く年数・壊れる条件・守る対象(既存か新規か)も")
    if "new_product_margin" not in na:
        if not [t for t in x.get("new_product_margin", []) if _filled(t.get("product", ""), 2) and _n(t.get("inc_revenue")) and _n(t.get("inc_cost")) and (t.get("inc_revenue") or t.get("inc_cost"))]:
            g.e("new_product_margin: 新しい収益線の、増えた売上と同じ期間に増えた原価を並べる(1 件以上)")
    if "industry" not in na:
        ind = [t for t in x.get("industry", []) if _filled(t.get("fact", ""), 10) and _filled(t.get("source", ""), 3) and _filled(str(t.get("changes_on", "")), 2) and _filled(t.get("so_what", ""), 6)]
        if len(ind) < 6:
            g.e(f"industry: 業界の仕組みが {len(ind)} 件(6 件以上。出所・変わる日付・だから何か)")
    if "competitors" not in na:
        cp = [t for t in x.get("competitors", []) if all(_filled(t.get(k, ""), 6) for k in ("name", "earns_by", "funded_by", "why_chosen", "next_move"))]
        if len(cp) < 2:
            g.e(f"competitors: 競合の経済が {len(cp)} 社(2 社以上。何で儲けているか・安さの原資・選ばれる理由・次の一手)")
        if not re.search(r"\d", str((x.get("win_loss") or {}).get("numbers", ""))):
            g.e("win_loss.numbers: どこから取り、どこへ取られたかの件数(置けなければ推定の幅)を書く")
    if "wallet" not in na:
        w = x.get("wallet", {})
        if len([t for t in w.get("ladder", []) if _filled(t.get("product", ""), 2) and _pos(t.get("monthly")) and _filled(str(t.get("kind", "")), 4)]) < 2:
            g.e("wallet.ladder: 取り分の梯子が 2 段未満(製品ごとの月額と、費用の置き換えか・利益から払うかの区別)")
        if not (all(_pos(w.get(k)) for k in ("now_pct", "full_stack_pct", "customer_margin_pct")) and _filled(w.get("ceiling", ""), 10)):
            g.e("wallet: 今の取り分・全部入れた取り分・顧客の利益率(%)と、単価の上限がどの段にあるか(ceiling)を書く")
    if "money" not in na:
        m = x.get("money", {})
        sp = m.get("steady_state_profit", {})
        if not (_pos(sp.get("value")) and _filled(sp.get("method", ""), 8)):
            g.e("money.steady_state_profit: 成長のための支出を除いた定常の利益と、分けた方法を書く")
        im = m.get("incremental_margin", {})
        if not (_n(im.get("past_pct")) and _n(im.get("latest_pct"))):
            g.e("money.incremental_margin: 限界利益率を、過去と直近の両方で書く(過去の回帰を直近で確かめずに使わない)")
        for k in ("allocation_history", "owner_incentive", "funded_by"):
            if not _filled(m.get(k, ""), 8):
                g.e(f"money.{k} が空")
        ev(m, "money")
    if "mechanisms" not in na:
        ms = [t for t in x.get("mechanisms", []) if _filled(t.get("mechanism", ""), 8) and _pos(t.get("per_share")) and _n(t.get("p")) and 0 < t["p"] <= 1 and _filled(str(t.get("when", "")), 2)]
        up, dn = sum(1 for t in ms if "上" in str(t.get("dir"))), sum(1 for t in ms if "下" in str(t.get("dir")))
        if up < 4 or dn < 4:
            g.e(f"mechanisms: 上振れ {up} 個・下振れ {dn} 個(各 4 個以上。1 株あたりの円・確率・時期つきで、上と下を同じ粒度で)")

    et = x.get("explain_test", {})
    ok_q = [k for k in (f"q{i}" for i in range(1, 10)) if _filled(et.get(k, ""), 20)]
    if len(ok_q) < 9:
        g.e(f"explain_test: 説明テストの答えが {len(ok_q)}/9(structure-anatomy.md D-3 の 9 問に、2 文以内で)")
    elif sum(1 for k in ok_q if re.search(r"\d", et[k])) < 7:
        g.e("explain_test: 数字の入った答えが 7 問未満(会社の資料の言い回しではなく、数字で答える)")

    pa = {str(t.get("pattern")): t for t in x.get("patterns_applied", []) if re.fullmatch(r"P\d{1,2}", str(t.get("pattern", ""))) and _filled(str(t.get("result", "")), 6)}
    if len(pa) < 12:
        g.e(f"patterns_applied: 当てた構造インサイトの型が {len(pa)} 個(references/insight-patterns.md の 20 の型から 12 個以上。当てはまらない型は result に理由)")
    elif sum(1 for t in pa.values() if re.search(r"\d", str(t.get("result", "")))) < 8:
        g.e("patterns_applied: 数字の出た型が 8 個未満(型は計算して当てる。「当てはまらない」だけの記録を数に入れない)")
    flagged = [k for k, t in pa.items() if t.get("flag") is True and not _filled(str(t.get("used_in", "")), 2)]
    if flagged:
        g.e(f"patterns_applied: 旗が立った型 {flagged} の used_in(仮説・示唆・条件の id)が空")
    lp_ = os.path.join(d, "structure_lenses.json")
    if not os.path.exists(lp_):
        g.e("structure_lenses.json がない(units.json を埋めて scripts/structure_lenses.py を実行する)")
    else:
        blob = json.dumps(x, ensure_ascii=False)
        hp = os.path.join(d, "hypotheses.json")
        if os.path.exists(hp):
            blob += open(hp, encoding="utf-8").read()
        lost = [f["id"] for f in load(lp_).get("flags", []) if f["id"] not in blob]
        if lost:
            g.e(f"単位のレンズの旗 {lost} が使われていない(patterns_applied の used_in・仮説・示唆の seed に id を書くか、flags_dismissed に理由)")
    rv = x.get("review", {})
    if not (_filled(str(rv.get("by", "")), 2) and _filled(str(rv.get("date", "")), 6) and _pos(rv.get("findings"))):
        g.e("review: 盲検(references/depth-review.md 依頼文 4)の記録が無い。別のモデルに、社名を伏せても同業と区別できるか・業界の人にも新しい発見があるかを審査させる")
    elif not _n(rv.get("new_to_insider")) or rv.get("new_to_insider") < 3:
        g.w("review.new_to_insider: 業界の人にも新しい発見が 3 個未満。開示の言い換えにとどまっていないか")
    return g.done()


def g_deep(d):
    """13 条件の深掘り(references/condition-deep-dive.md)。決め手の問い・測り方・反対の評価の検証・構造との接続。"""
    g = Gate("条件の深掘り")
    p, sp = os.path.join(d, "conditions.json"), os.path.join(d, "structure.json")
    if not os.path.exists(p):
        g.e("conditions.json がない")
        return g.done()
    cj = load(p)
    blocks = set(load(sp).keys()) if os.path.exists(sp) else set()
    if not blocks:
        g.e("structure.json がない。条件の深掘りの材料は事業構造の解剖(工程 2A)。先に gate.py structure を通す")
    ids = _facts_ids(d)
    for c in cj.get("conditions", []):
        no, gr = c.get("no"), str(c.get("grade", "")).strip().upper()
        if no == 4 or gr in ("N/A", ""):
            continue
        tag, dp = f"条件{no}", c.get("deep") or {}
        if not dp:
            g.e(f"{tag}: deep(深掘り)が無い。理由 1 段落の採点は分析ではない(condition-deep-dive.md §1)")
            continue
        qs = [q for q in dp.get("questions", []) if _filled(q.get("q", ""), 8) and _filled(q.get("a", ""), 15) and re.search(r"\d", q.get("a", "")) and (q.get("evidence") or [])]
        if len(qs) < 3:
            g.e(f"{tag}: 決め手の問い(数字入りの答えと根拠つき)が {len(qs)} 個。3 個以上")
        elif ids and not any(e_ in ids for q in qs for e_ in q.get("evidence", [])):
            g.e(f"{tag}: 問いの根拠に台帳の id が 1 つも無い")
        t = dp.get("test", {})
        if not all(_filled(str(t.get(k, "")), 2) for k in ("metric", "value", "benchmark", "threshold")) or not re.search(r"\d", str(t.get("value", "")) + str(t.get("benchmark", ""))):
            g.e(f"{tag}: test(物差し metric・この会社の値 value・比べる相手 benchmark・この評価に要る水準 threshold)を数字で書く")
        refs = [r_ for r_ in dp.get("structure_refs", []) if str(r_).split(".")[0] in blocks]
        if blocks and not refs:
            g.e(f"{tag}: structure_refs(根拠にした structure.json の区画)が無い・区画の名前でない")
        ct = dp.get("counter", {})
        if not all(_filled(ct.get(k, ""), 10) for k in ("higher", "why_not_higher", "lower", "why_not_lower")):
            g.e(f"{tag}: counter(1 段上・1 段下だと主張する最強の論拠と、採らない理由)を 4 つとも書く")
        for k in ("upgrade_if", "downgrade_if"):
            if not (_filled(dp.get(k, ""), 10) and re.search(r"\d", dp.get(k, ""))):
                g.e(f"{tag}: {k}(評価が動く条件を、観測できる数字と日付で)を書く")
        if no == 1:
            hz = dp.get("horizon", {})
            if not all(_filled(hz.get(k, ""), 15) for k in ("now", "y5", "y10")):
                g.e("条件1: horizon(今・5 年後・10 年後の 3 時点の見立て)を書く。今の数字で 10 年を語らない")
    rv = cj.get("review", {})
    if not (_filled(str(rv.get("by", "")), 2) and _filled(str(rv.get("date", "")), 6)):
        g.e("review: 条件の審査(references/depth-review.md 依頼文 5)の記録が無い。別のモデルに全条件を 1 段動かす試みをさせる")
    elif not rv.get("moved") and not _filled(str(rv.get("notes", "")), 20):
        g.e("review: 審査で 1 つも動かなかったのに notes が無い(審査が弱い。モデルを上げるか、動かなかった理由を書く)")
    return g.done()


def main():
    args = [a for a in sys.argv[1:] if a != "--before-price"]
    before = "--before-price" in sys.argv
    if not args or args[0] not in ("facts", "conditions", "valuation", "report", "hypotheses", "change", "map", "lenses", "thesis", "structure", "deep", "final", "all"):
        print(__doc__)
        sys.exit(2)
    sys.argv = [sys.argv[0]] + args
    d = sys.argv[2] if len(sys.argv) > 2 else "."
    fns = {"facts": g_facts, "conditions": (lambda x: g_conditions(x, before)), "valuation": g_valuation, "report": g_report,
           "hypotheses": g_hypotheses, "change": g_change, "map": g_map, "lenses": g_lenses, "thesis": g_thesis, "structure": g_structure, "deep": g_deep}
    order = (["facts", "conditions", "valuation", "report"] if sys.argv[1] == "all" else
             ["facts", "lenses", "map", "structure", "hypotheses", "change", "conditions", "deep", "valuation", "thesis"] if sys.argv[1] == "final" else [sys.argv[1]])
    ok = True
    for k in order:
        ok = fns[k](d) and ok
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
