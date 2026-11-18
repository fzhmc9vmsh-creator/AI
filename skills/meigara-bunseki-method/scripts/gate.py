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

    python3 gate.py facts       [作業フォルダ]   # 台帳の検査
    python3 gate.py conditions  [作業フォルダ]   # 採点表の検査(根拠・監視 KPI・二層の評価・評価保留)
    python3 gate.py conditions --before-price [作業フォルダ]   # 工程 4 の終わり: 条件6・7 が空でも止めない
    python3 gate.py valuation   [作業フォルダ]   # 計算機を通したか・採点表と評価が一致するか
    python3 gate.py report      [作業フォルダ]   # 報告書の章・数字の一致・版の言葉
    python3 gate.py hypotheses  [作業フォルダ]   # 仮説台帳(反証できる形・判定の根拠・立て直しの跡)。工程 2 の終わり
    python3 gate.py map         [作業フォルダ]   # 事業の地図(製品群の地図・バリューチェーン図)。工程 2 の途中
    python3 gate.py change      [作業フォルダ]   # 変化の評価表(15 項目の過去・現在・将来)。工程 4 の前
    python3 gate.py lenses      [作業フォルダ]   # 示唆の種(lenses.py の旗)を仮説・示唆に使ったか、理由を付けて捨てたか。工程 2 の終わり
    python3 gate.py outlook     [作業フォルダ]   # 将来の構造(確度 × 影響度)・リスク(確率 × 影響度)・今の値段・比較の設計。工程 6 の終わり(第10版)
    python3 gate.py thesis      [作業フォルダ]   # 投資仮説(市場との差分・価値の芯・撤回の線)、示唆の深さ、弱気の反論の検証。工程 6 の終わり
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
REPORT_HEADINGS = ["エグゼクティブサマリ", "会社と業界", "現在の構造", "製品ポートフォリオ", "キャッシュ", "将来の構造", "確度",
                   "リスク", "今の値段", "市場との差分", "PEG", "13条件", "投資行動", "既知の制約", "計算前提"]   # 第10版: 5 工程の章立て
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
    if x.get("legacy"):
        g.w("legacy: 第9版までの形式(製品ポートフォリオ・現金の地図・業界・用語の検査を飛ばした)。新しい分析では legacy を書かない")
        return g.done()
    map_v10(x, g)
    return g.done()


PLC = ("導入", "成長", "成熟", "衰退")
STATEMENTS = ("PL", "CF", "BS", "VC", "ROE")


def _num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def _txt(v, n=4):
    return isinstance(v, str) and len(v.strip()) >= n and not PLACEHOLDER.search(v)


def map_v10(x, g):
    """第10版(five-stage-analysis.md §1・§6): 製品ポートフォリオ × PLC × 現金の役割、現金の創出と投下と時間軸、業界の登場人物、用語。"""
    pf = x.get("portfolio") or []
    if len(pf) < 3:
        g.e(f"portfolio(製品ポートフォリオ)が {len(pf)} 個(製品群ごとに 3 個以上。市場の伸び・強さ・売上・PLC・現金の役割)")
    roles = set()
    for it in pf:
        n = it.get("name", "?")
        if not _num(it.get("market_growth")):
            g.e(f"portfolio {n}: market_growth(市場の伸び、年率 %)が数字でない")
        pos = it.get("position") or {}
        if not _txt(pos.get("metric"), 2) or not _num(pos.get("value")):
            g.e(f"portfolio {n}: position{{metric, value}}(相対シェアか、代わりの物差しと値)が無い")
        if not _num(it.get("revenue")):
            g.e(f"portfolio {n}: revenue(売上)が数字でない")
        if it.get("plc") not in PLC:
            g.e(f"portfolio {n}: plc は {'・'.join(PLC)} のどれか")
        if it.get("cash_role") not in ("創出", "消費", "均衡"):
            g.e(f"portfolio {n}: cash_role は 創出・消費・均衡 のどれか")
        roles.add(it.get("cash_role"))
        if not _txt(it.get("cash_basis"), 6):
            g.e(f"portfolio {n}: cash_basis(現金の役割を決めた前提: 製品群の利益 − 要る投資)が空")
        if not _txt((it.get("next5y") or {}).get("why"), 6):
            g.w(f"portfolio {n}: next5y.why(5 年後の位置と動きの理由)が空")
    if pf and not ({"創出"} & roles):
        g.w("現金を生む製品群(cash_role: 創出)が無い。全社の現金の出どころを cash_map.sources に書く")
    cm = x.get("cash_map") or {}
    if not cm.get("sources"):
        g.e("cash_map.sources(現金を生む所)が無い")
    if len(cm.get("uses") or []) < 2:
        g.e("cash_map.uses(現金を投じる所)が 2 つ未満(維持更新・成長投資・研究開発・還元・支払い義務など)")
    tm = cm.get("timing") or {}
    if tm.get("type") not in ("前受け型", "後払い型", "投資先行型", "中立"):
        g.e("cash_map.timing.type は 前受け型・後払い型・投資先行型・中立 のどれか(現金が利益より先か後か)")
    if len([m for m in tm.get("metrics") or [] if re.search(r"\d", str(m.get("value", "")))]) < 2:
        g.e("cash_map.timing.metrics に数字が 2 つ未満(前受金÷売上・契約残高・CCC・支払い義務÷年間売上・回収年数など)")
    if not _txt(tm.get("one_line"), 10):
        g.e("cash_map.timing.one_line(この会社は現金が先行するか、投資が先行するかの一文)が空")
    ind = x.get("industry") or {}
    if len(ind.get("actors") or []) < 3:
        g.e("industry.actors(業界の登場人物)が 3 未満。上流・自社・販路・顧客を平易な説明つきで")
    for a in ind.get("actors") or []:
        if not _txt(a.get("plain"), 4):
            g.e(f"industry.actors {a.get('name', '?')}: plain(平易な説明)が空")
    gl = x.get("glossary") or []
    if len(gl) < 5:
        g.e(f"glossary(用語)が {len(gl)} 語。報告書・資料に出る専門用語・略語を全部、意味(plain)と、なぜ要るか(why)つきで")
    for t in gl:
        if not _txt(t.get("plain"), 4) or not _txt(t.get("why"), 4):
            g.e(f"glossary {t.get('term', '?')}: plain と why を書く")


def g_outlook(d):
    """第10版(five-stage-analysis.md §2〜§4): 将来の構造・リスク・今の値段・比較の設計。"""
    g = Gate("outlook")
    path = os.path.join(d, "outlook.json")
    if not os.path.exists(path):
        g.e("outlook.json が無い(templates/outlook.json を写して作る)")
        return g.done()
    x = load(path)
    hz = x.get("horizon") or {}
    if not re.search(r"\d{4}", str(hz.get("year", ""))) or not _txt(hz.get("why"), 8):
        g.e("horizon{year, why}(将来の構造を描く年と、なぜその年か)が無い")
    cp = x.get("company_plan") or {}
    if not _txt(cp.get("goal"), 6) or not _txt(cp.get("source"), 4):
        g.e("company_plan.goal(会社の目標)と source(出所)を書く")

    def rate(it, where):
        n = it.get("name", "?")
        p = it.get("p")
        if not _num(p) or not 0 <= p <= 1:
            g.e(f"{where} {n}: p(確度・確率 0〜1)が無い")
        if not _txt(it.get("certainty_basis") or it.get("p_basis"), 6):
            g.e(f"{where} {n}: 確度の根拠(certainty_basis / p_basis)が空")
        if not _num(it.get("impact_pct")):
            g.e(f"{where} {n}: impact_pct(理論株価への影響 %)が数字でない(valuate.py の感応度で出す)")
        if not _txt(it.get("impact_basis"), 3):
            g.e(f"{where} {n}: impact_basis(影響を出した感応度・節点の名前)が空")
        if "statement" in it and it.get("statement") not in STATEMENTS:
            g.e(f"{where} {n}: statement は {'・'.join(STATEMENTS)} のどれか")

    pcs = cp.get("pieces") or []
    if len(pcs) < 3:
        g.e(f"company_plan.pieces が {len(pcs)} 個(3 個以上。設備・製品・提携・資本政策)")
    for it in pcs:
        rate(it, "ピース")
    ms = x.get("market_scenarios") or []
    types = {m.get("type") for m in ms}
    if not {"脅威", "機会"} <= types:
        g.e("market_scenarios に脅威と機会の両方が無い(会社の計画の外で起きることを、両側で 1 つ以上)")
    for m in ms:
        rate(m, "市場のシナリオ")
        if _num(m.get("p")) and _num(m.get("impact_pct")) and m["p"] >= 0.4 and abs(m["impact_pct"]) >= 10 and not m.get("chosen") and not _txt(m.get("reason_not"), 6):
            g.e(f"市場のシナリオ {m.get('name')}: 確度 {m['p']:.0%}・影響 {m['impact_pct']:+.0f}% は「選ぶ」水準(確度 0.4 以上かつ影響 ±10% 以上)。chosen: true で将来の構造に入れるか、reason_not に理由")
        if m.get("chosen") and not _txt(m.get("future_note"), 6):
            g.e(f"市場のシナリオ {m.get('name')}: 選んだのに future_note(将来の構造のどこが変わるか)が空")
    el = x.get("eps_lines") or {}
    vip = os.path.join(d, "valuation_input.json")
    if os.path.exists(vip):
        paths = (load(vip).get("eps_paths") or {})
        for k in ("company", "adjusted", "scenario"):
            nm = el.get(k)
            if nm and not PLACEHOLDER.search(str(nm)) and nm not in paths:
                g.e(f"eps_lines.{k} の経路 {nm} が valuation_input.json の eps_paths に無い(道筋の EPS と価値評価の EPS を同じものにする)")
        if any(m.get("chosen") for m in ms) and not el.get("scenario"):
            g.e("選んだ市場のシナリオがあるのに、eps_lines.scenario(それを入れた EPS の経路)が無い")
    else:
        g.w("valuation_input.json が無いので、道筋の EPS と価値評価の EPS の一致を確かめられない")
    fs = x.get("future_structure") or {}
    if fs.get("most_changed") not in STATEMENTS or not _txt(fs.get("why"), 8) or not _txt(fs.get("now"), 4) or not _txt(fs.get("future"), 4):
        g.e("future_structure{most_changed(PL・CF・BS・VC・ROE), why, now, future} を書く(最も変わる財務と、その理由)")
    rk = x.get("risks") or []
    if len(rk) < 5:
        g.e(f"risks が {len(rk)} 個(5〜8 個。確率 × 影響度)")
    for r in rk:
        rate(r, "リスク")
        if not re.search(r"\d", str(r.get("p_basis", ""))):
            g.e(f"リスク {r.get('name')}: p_basis(基準率: 過去に何回中何回)に数字が無い")
        if r.get("reflected_in") not in ("tree", "sensitivity", "eps_path", "未反映"):
            g.e(f"リスク {r.get('name')}: reflected_in は tree・sensitivity・eps_path・未反映 のどれか")
        if not _txt(r.get("signal_kpi"), 3) or not _txt(str(r.get("threshold", "")), 2) or not DATEISH.search(str(r.get("check_date", ""))):
            g.e(f"リスク {r.get('name')}: signal_kpi・threshold・check_date(兆候の KPI・見直しの線・確認日)を書く")
    scored = sorted([r for r in rk if _num(r.get("p")) and _num(r.get("impact_pct"))], key=lambda r: -r["p"] * abs(r["impact_pct"]))
    for r in scored[:3]:
        if r.get("reflected_in") == "未反映":
            g.e(f"期待損失の上位のリスク {r.get('name')}(p {r['p']:.0%} × {r['impact_pct']:+.0f}%)が価値評価に未反映")
    if scored:
        print("[outlook] 期待損失の順: " + " > ".join(f"{r.get('name')}({r['p'] * abs(r['impact_pct']):.1f})" for r in scored[:5]))
    mv = x.get("market_valuation") or {}
    if not _txt(mv.get("price_ref"), 1) or len(mv.get("variant") or []) < 2:
        g.e("market_valuation{price_ref, variant(市場の前提 | 自分の見立て 2 行以上)} を書く")
    vp = os.path.join(d, "valuation.json")
    if os.path.exists(vp) and not any(k.startswith("mkt.") for k in (load(vp).get("display") or {})):
        g.e("valuation.json に今の値段(mkt.*: 今の PER・今の PEG・株価が前提にする成長率)が無い。第10版の valuate.py で計算し直す")
    bms = x.get("benchmarks") or []
    if not bms:
        g.e("benchmarks(比較の設計)が無い。同業と比べるなら、指標の定義と目的・なぜその軸か・比較対象と理由・外した候補を書く")
    for b in bms:
        m = b.get("metric", "?")
        for k in ("metric", "definition", "purpose", "why_axis"):
            if not _txt(b.get(k), 3):
                g.e(f"比較 {m}: {k} が空")
        if len(b.get("peers") or []) < 2:
            g.e(f"比較 {m}: 比較対象が 2 社未満")
        for pr in b.get("peers") or []:
            if not _txt(pr.get("what"), 4) or not _txt(pr.get("why_comparable"), 6):
                g.e(f"比較 {m}: {pr.get('name', '?')} の what(何の会社か)と why_comparable(指標を動かす仕組みが同じか)を書く")
        if not b.get("rejected"):
            g.e(f"比較 {m}: rejected(外した候補と理由)が無い")
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


def main():
    args = [a for a in sys.argv[1:] if a != "--before-price"]
    before = "--before-price" in sys.argv
    if not args or args[0] not in ("facts", "conditions", "valuation", "report", "hypotheses", "change", "map", "lenses", "thesis", "outlook", "all"):
        print(__doc__)
        sys.exit(2)
    sys.argv = [sys.argv[0]] + args
    d = sys.argv[2] if len(sys.argv) > 2 else "."
    fns = {"facts": g_facts, "conditions": (lambda x: g_conditions(x, before)), "valuation": g_valuation, "report": g_report,
           "hypotheses": g_hypotheses, "change": g_change, "map": g_map, "lenses": g_lenses, "thesis": g_thesis,
           "outlook": g_outlook}
    order = ["facts", "conditions", "valuation", "report"] if sys.argv[1] == "all" else [sys.argv[1]]
    ok = True
    for k in order:
        ok = fns[k](d) and ok
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
