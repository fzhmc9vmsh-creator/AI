#!/usr/bin/env python3
"""スライドの設計書 storyline.json の検査(references/story-design.md)。標準ライブラリだけで動く。

    python3 check_storyline.py storyline.json
    python3 check_storyline.py storyline.json --analysis <分析の作業フォルダ>   # 投資資料: 分析の示唆・投資仮説と照合する

狙い・順番・一貫性・重み付けが設計に入っているかを確かめる。FAIL のまま実装に進まない。
--analysis を付けると、meigara-bunseki-method の hypotheses.json(示唆のカード・投資仮説)と valuation.json を読み、
深さ 4・5 の示唆が主役のページになっているか、結論が投資仮説と合っているかを確かめる。

deck_type: "stock"(投資資料・第3版の 5 工程。references/stock-analysis.md §3)では、さらに次を確かめる(2026-11-18):
  章の stage が intro → current → future → risk → valuation → verdict の順に揃い、各工程の必須ページ(kind)がある /
  1 章の問いと答えにキャッシュ / 道筋(path)が将来の終点(future_structure)より前 / 目標の年とその理由(horizon) /
  説明してから使う(uses は前のページの introduces に限る。判定の章で新しい事実を出さない) / 用語の表(glossary)/
  比較の設計(benchmarks: 指標の定義と目的・比較対象の説明と理由・外した候補)
"""
import json
import os
import re
import sys

WEIGHTS = ("S", "A", "B", "C", "D")
FIGS = ("図", "関係図", "ロードマップ", "判別表", "表")
CONNECT = ("だから", "なぜなら", "では", "しかし", "具体的には", "その結果", "次に", "また")
LISTY = ("次に", "また")
STAGES = ("intro", "current", "future", "risk", "valuation", "verdict")
STAGE_JA = {"intro": "0 会社と業界の前提", "current": "1 現在の構造", "future": "2 将来の構造", "risk": "3 リスク",
            "valuation": "4 今の値段", "verdict": "5 判定と行動"}
REQ_KINDS = {"intro": ("company_profile", "industry_map"), "current": ("portfolio", "pl", "cash", "bs"),
             "future": ("company_plan", "plan_rating", "market_scenarios", "path", "future_structure"),
             "risk": ("risk_matrix", "rebuttals"), "valuation": ("market_implied", "peers"),
             "verdict": ("peg_check", "fair_value", "conditions", "action")}
S_KINDS = ("cash", "plan_rating", "path", "risk_matrix", "market_implied", "peg_check", "fair_value")
NONBODY = ("cover", "summary", "agenda", "glossary")
DESCRIPTIVE = re.compile(r"(について|の概要|の推移|の状況|の比較|の一覧|の内訳|の分析|まとめ)[。]?$")


def filled(v, n=4):
    return isinstance(v, str) and len(v.strip()) >= n and "|" not in v and not (v.strip().startswith("(") and v.strip().endswith(")"))


def check_stock(d, chs, pages, body, e, w):
    """投資資料(第3版 5 工程)の検査。stock-analysis.md §3。"""
    # 工程の順と必須ページ
    st = [c.get("stage") for c in chs if c.get("stage") not in (None, "opening")]
    for c in chs:
        if c.get("stage") not in STAGES + ("opening",):
            e(f"第{c.get('no')}章: stage は opening・{'・'.join(STAGES)} のどれか")
    for x in STAGES:
        if x not in st:
            e(f"工程「{STAGE_JA[x]}」の章(stage: {x})が無い(事実 → 予測 → 不確実性 → 値段 → 判定 の 5 工程と前提の章を揃える)")
    order = [x for x in st if x in STAGES]
    if order != sorted(order, key=STAGES.index):
        e(f"章の工程の順が {' → '.join(order)}。intro → current → future → risk → valuation → verdict の順に並べる(入れ替えない)")
    stage_of = {c.get("no"): c.get("stage") for c in chs}
    idx = {p.get("id"): i for i, p in enumerate(pages)}
    kinds = {}
    for p in pages:
        kinds.setdefault((stage_of.get(p.get("chapter")), p.get("kind")), []).append(p)
    for stg, ks in REQ_KINDS.items():
        for k in ks:
            if not kinds.get((stg, k)):
                e(f"「{STAGE_JA[stg]}」の章に kind: {k} のページが無い(stock-analysis.md §3)")
    for k in S_KINDS:
        for p in [p for (s_, kk), ps in kinds.items() if kk == k for p in ps]:
            if p.get("weight") not in ("S", None) and p.get("role", "body") == "body":
                w(f"{p.get('id')}: kind {k} は判断を決めるページ。重み S を推奨(いま {p.get('weight')})")
    paths = [idx[p["id"]] for (s_, k), ps in kinds.items() if k == "path" for p in ps]
    ends = [idx[p["id"]] for (s_, k), ps in kinds.items() if k == "future_structure" for p in ps]
    if paths and ends and min(ends) < min(paths):
        e("将来の終点(future_structure)が、現在から将来への道筋(path)より前にある。道筋 → 終点の順にする(理由付けなしに終点を出さない)")
    cur = [c for c in chs if c.get("stage") == "current"]
    if cur and not any(re.search(r"キャッシュ|現金|CF", str(c.get("question", "")) + str(c.get("answer", "")) + str(c.get("name", ""))) for c in cur):
        e("1 章(現在の構造)の問い・答えにキャッシュが無い。どこで現金を生み、どこへ投じるかを目次から示す")
    hz = d.get("horizon") or {}
    if not re.search(r"\d{4}", str(hz.get("year", ""))) or not filled(hz.get("why"), 8):
        e("horizon{year, why}(将来の構造を描く年と、なぜその年か)が無い")
    # 用語
    gl = d.get("glossary") or []
    for g_ in gl:
        t = g_.get("term", "?")
        if not filled(g_.get("plain"), 4) or not filled(g_.get("why"), 4):
            e(f"用語「{t}」: plain(平易な意味)と why(この資料でなぜ要るか)を書く")
        if g_.get("first_page") not in idx:
            e(f"用語「{t}」: first_page(初出のページ id)が pages に無い")
    if len(gl) < 5:
        w(f"glossary が {len(gl)} 語。資料に出る専門用語・略語を全部書く(lint_deck.py pptx --storyline が資料の略語と照合する)")
    if any(p.get("role") == "glossary" or p.get("kind") == "glossary" for p in pages):
        e("用語だけを並べたページ(role: glossary)がある。用語は使うページで L.termNotes で注釈する(2026-11-19 利用者: 「全く意図が違う」)")
    # 目次: 序に 1 枚と、各工程の章の頭に 1 枚(2026-11-19 利用者: 「目次がないのはなんで？」)
    for c in chs:
        if c.get("stage") in STAGES:
            cp = [p for p in pages if p.get("chapter") == c.get("no")]
            if not cp or cp[0].get("role") != "agenda":
                e(f"第{c.get('no')}章({STAGE_JA[c.get('stage')]})の頭に目次(role: agenda。L.agenda)が無い。各章の頭に、章の一覧・この章の問いと答え・構成とページの目次を置く")
    # 損益のサンキー図: 現在(pl)と、道筋の後の将来の着地(2026-11-19 利用者: 「サンキー図は？」)
    for p in pages:
        if p.get("kind") == "pl" and "サンキー" not in str(p.get("hero", "")):
            e(f"{p.get('id')}: 損益の流れ(pl)の主役はサンキー図(hero に「サンキー」)。滝グラフに置き換えない")
    fut_sk = [idx[p["id"]] for p in pages if stage_of.get(p.get("chapter")) == "future" and "サンキー" in str(p.get("hero", ""))]
    if not fut_sk:
        e("将来の構造の章に、目標の年の損益のサンキー図(hero に「サンキー」)が無い。道筋(path)の後に着地として置く")
    elif paths and min(fut_sk) < min(paths):
        e("将来のサンキー図が道筋(path)より前にある。道筋 → サンキー図(着地)の順にする")
    # 説明してから使う
    con = {c.get("id"): c for c in d.get("concepts", []) if c.get("id")}
    if not con:
        e("concepts(資料で説明する概念・数字の一覧)が無い。各ページの introduces・uses で、説明してから使う順を確かめる")
    intro_at = {}
    for i, p in enumerate(pages):
        for cid in p.get("introduces") or []:
            if cid not in con:
                e(f"{p.get('id')}: introduces の {cid} が concepts に無い")
            elif cid in intro_at:
                e(f"{p.get('id')}: {cid} は {pages[intro_at[cid]].get('id')} で説明済み(同じものを 2 回 introduces しない)")
            else:
                intro_at[cid] = i
    vstage = {}
    for i, p in enumerate(pages):
        if p.get("role", "body") in ("cover", "summary", "agenda"):
            continue
        sg = stage_of.get(p.get("chapter"))
        for cid in p.get("uses") or []:
            if cid not in con:
                e(f"{p.get('id')}: uses の {cid} が concepts に無い")
            elif cid not in intro_at or intro_at[cid] > i:
                where = pages[intro_at[cid]].get("id") if cid in intro_at else "どこにも無い"
                e(f"{p.get('id')}: 「{con[cid].get('label', cid)}」を、説明する前に使っている(説明: {where})。説明のページを前に置くか、このページで説明する")
        if p.get("role", "body") == "body" and sg in STAGES and not (p.get("introduces") or p.get("uses")):
            e(f"{p.get('id')}: introduces も uses も無い(このページが何を説明し、何を使うかを書く)")
        if sg == "verdict":
            for cid in p.get("introduces") or []:
                if con.get(cid, {}).get("type") == "fact":
                    e(f"{p.get('id')}: 判定の章で新しい事実「{con[cid].get('label', cid)}」を出している。判定は 1〜4 章で説明したものだけで行う"
                      "(判定の道具 PEG・適正株価などは type: tool)")
            vstage[p.get("kind")] = {stage_of.get(pages[intro_at[c]].get("chapter")) for c in (p.get("uses") or []) if c in intro_at}
    pc = vstage.get("peg_check")
    if pc is not None:
        for need in ("future", "risk", "valuation"):
            if need not in pc:
                e(f"PEG の照合(peg_check)が「{STAGE_JA[need]}」の章の数字を使っていない(uses)。EPS は 2 章、リスクの反映は 3 章、今の PER は 4 章から")
    cd = vstage.get("conditions")
    if cd is not None and len(cd & {"intro", "current", "future", "risk", "valuation"}) < 3:
        e("13 条件の照合(conditions)の uses が 3 つ未満の工程にしか及ばない。各条件の根拠を 1〜4 章のページから引く")
    # 比較の設計
    bms = {b.get("page"): b for b in d.get("benchmarks", [])}
    for p in pages:
        if p.get("kind") == "peers" or p.get("compares"):
            b = bms.get(p.get("id"))
            if not b:
                e(f"{p.get('id')}: 比較のページなのに benchmarks が無い(指標の定義と目的・比較対象の説明と理由・外した候補)")
                continue
            for k, lab in (("metric", "指標"), ("definition", "定義"), ("purpose", "何を判断するための指標か"), ("why_axis", "なぜその軸か(価値の芯に効くか)")):
                if not filled(b.get(k), 3):
                    e(f"{p.get('id')}: benchmarks の {k}({lab})が空")
            prs = b.get("peers") or []
            if len(prs) < 2:
                e(f"{p.get('id')}: 比較対象が {len(prs)} 社(2 社以上)")
            for pr in prs:
                if not filled(pr.get("what"), 4) or not filled(pr.get("why_comparable"), 6):
                    e(f"{p.get('id')}: 比較対象 {pr.get('name', '?')} の what(何の会社か)か why_comparable(指標を動かす仕組みが同じか)が空")
            if not b.get("rejected"):
                e(f"{p.get('id')}: rejected(外した比較の候補と理由)が無い。突っ込まれたときの答えを用意する")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    with open(sys.argv[1], encoding="utf-8") as fh:
        d = json.load(fh)
    errs, warns = [], []
    e, w = errs.append, warns.append
    adir = sys.argv[sys.argv.index("--analysis") + 1] if "--analysis" in sys.argv and len(sys.argv) > sys.argv.index("--analysis") + 1 else None
    hyp = val = None
    if adir:
        hp, vp = os.path.join(adir, "hypotheses.json"), os.path.join(adir, "valuation.json")
        if os.path.exists(hp):
            with open(hp, encoding="utf-8") as fh:
                hyp = json.load(fh)
        else:
            e(f"--analysis {adir} に hypotheses.json が無い(分析が終わっていない。資料だけ先に作らない)")
        if os.path.exists(vp):
            with open(vp, encoding="utf-8") as fh:
                val = json.load(fh)

    goal = d.get("goal", {})
    for k, label in (("reader", "読み手"), ("decision", "読後の行動"), ("claim", "最終主張")):
        if not filled(goal.get(k), 6):
            e(f"goal.{k}({label})が空(狙いが書けなければ作り始めない)")
    if filled(goal.get("claim"), 6) and not any(ch.isdigit() for ch in goal["claim"]):
        w("最終主張に数字が無い(決め手の数字を入れる)")
    if not filled(d.get("unit"), 1):
        e("unit(金額の単位。資料全体で 1 つ)が空")

    kms = {k.get("id"): k for k in d.get("key_messages", [])}
    if not 3 <= len(kms) <= 6:
        e(f"キーメッセージが {len(kms)} 本(3〜6 本)")

    chs = d.get("chapters", [])
    seen = set()
    for c in chs:
        no = c.get("no")
        if not filled(c.get("question"), 6):
            e(f"第{no}章: question(読み手の問い)が空")
        if not filled(c.get("answer"), 8):
            e(f"第{no}章: answer(この資料の答え)が空")
        for dep in c.get("depends_on", []) or []:
            if dep not in seen:
                e(f"第{no}章: 第{dep}章に依存するのに、それより前に置かれている(順番を直す)")
        seen.add(no)
    if len(chs) >= 3 and not any(c.get("depends_on") for c in chs):
        e("どの章にも depends_on が無い。入れ替えても通じる章の並びは一覧であって話ではない(問いの連鎖で並べる)")

    pages = d.get("pages", [])
    body = [p for p in pages if p.get("role", "body") == "body"]
    dt = d.get("deck_type")
    if dt not in ("stock", "general", "stock_v2"):
        e("deck_type を書く(投資資料は stock、それ以外は general)")
    elif dt == "stock_v2":
        w("deck_type stock_v2 は旧構成(7 つの問い)。新しい投資資料は stock(5 工程)で作る")
    if dt == "stock":
        check_stock(d, chs, pages, body, e, w)
    roles = [p.get("role", "body") for p in pages]
    if "summary" not in roles[:3]:
        e("結論(role: summary)が最初の 3 枚に無い(結論を先に置く)")
    if len(pages) > 10 and "agenda" not in roles[:5]:
        e("10 枚を超えるのに、意図つきの目次(role: agenda)が最初の 5 枚に無い")
    if "appendix" in roles and not goal.get("allow_appendix"):
        e("付録(role: appendix)がある。1 枚ずつ必要かどうかで判断し、要らないものは dropped へ")
    chno = {c.get("no") for c in chs}
    proven = {k: [] for k in kms}
    count = {x: 0 for x in WEIGHTS}
    per_ch = {}
    for p in body:
        pid = p.get("id", "?")
        if p.get("chapter") not in chno:
            e(f"{pid}: chapter が章の一覧に無い")
        per_ch[p.get("chapter")] = per_ch.get(p.get("chapter"), 0) + 1
        if not filled(p.get("message"), 14):
            e(f"{pid}: message(主張を含む完全文)が空か短い")
        elif DESCRIPTIVE.search(p["message"].strip()):
            e(f"{pid}: message が見出し語で終わっている(「〜の推移」「〜について」は主張ではない。何が言えるかを文で書く)")
        elif p.get("weight") in ("S", "A") and not any(ch.isdigit() for ch in p["message"]):
            (e if p.get("weight") == "S" else w)(f"{pid}: 重み {p.get('weight')} の message に数字が無い(決め手の数字を入れる)")
        if not filled(p.get("aim"), 8):
            e(f"{pid}: aim(このページは何を証明するか)が空。狙いが書けないページは要らない")
        pv = [k for k in (p.get("proves") or []) if k in kms]
        if not pv:
            e(f"{pid}: proves(どのキーメッセージを証明するか)が無い。どれも証明しないページは捨てる")
        wt = p.get("weight")
        if wt not in WEIGHTS:
            e(f"{pid}: weight は S・A・B・C・D のどれか")
            continue
        count[wt] += 1
        if wt in ("C", "D"):
            e(f"{pid}: 重み {wt} の中身に 1 枚使っている(他ページの脚注・表の 1 行にするか、dropped へ)")
        if wt == "B":
            w(f"{pid}: 重み B に 1 枚使っている(他のページの一区画にまとめられないか)")
        for k in pv:
            proven[k].append(wt)
        if p.get("form") not in FIGS:
            e(f"{pid}: form は {'・'.join(FIGS)} のどれか(文だけのページは作らない)")
        if wt == "S":
            if p.get("form") == "表":
                w(f"{pid}: 重み S の主役が表(量の比較・推移・構成なら比例描画の図にする)")
            if not filled(p.get("hero"), 6):
                e(f"{pid}: 重み S なのに hero(主役の図)が空")
            if not filled(p.get("key_number"), 1) or not any(ch.isdigit() for ch in str(p.get("key_number"))):
                e(f"{pid}: 重み S なのに key_number(タイトルに入れる決め手の数字)が無い")
            if not filled(p.get("reader_belief"), 8) or not filled(p.get("shift"), 8):
                e(f"{pid}: 重み S なのに reader_belief(読み手が読む前に思っていること)と shift(このページで変わる認識)が無い。"
                  "認識を変えないページは主役ではない(重みを A に下げるか、切り口を変える)")
        if p is not body[0] and p.get("connector") not in CONNECT:
            e(f"{pid}: connector(前のページとの接続語)は {'・'.join(CONNECT)} のどれか")
    for k, ws in proven.items():
        if not any(x in ("S", "A") for x in ws):
            e(f"キーメッセージ {k} を証明する S か A のページが無い")
    n = len(body)
    if n:
        s_share = count["S"] / n
        if count["S"] == 0:
            e("重み S のページが 1 枚も無い(資料の主役が決まっていない)")
        elif not 0.12 <= s_share <= 0.4:
            w(f"重み S が {count['S']}/{n} 枚({s_share:.0%})。目安は 15〜30%(全部が主役なら主役は無い)")
        cons = [p.get("connector") for p in body[1:]]
        listy = sum(1 for c in cons if c in LISTY)
        if cons and listy / len(cons) > 0.4:
            e(f"接続語の {listy}/{len(cons)} が「次に・また」。ページが並列に並んでいて話になっていない(問いの連鎖に組み直す)")
        for c, k in per_ch.items():
            if n >= 8 and k / n > 0.45:
                w(f"第{c}章が {k}/{n} 枚で全体の 45% を超える(章を分けるか、重みを見直す)")
    if n > 12 and not d.get("dropped"):
        w("dropped(捨てたものと理由)が空。作った分析を全部載せていないか")

    # 分析との照合(投資資料)
    if hyp:
        ins = {it.get("id"): it for it in hyp.get("insights", []) if it.get("id")}
        on_page = {}
        for p in body:
            for iid in ([p.get("insight")] if isinstance(p.get("insight"), str) else (p.get("insight") or [])):
                if iid not in ins:
                    e(f"{p.get('id')}: insight {iid} が分析の hypotheses.json に無い")
                else:
                    on_page.setdefault(iid, []).append(p.get("weight"))
        th = hyp.get("thesis") or {}
        core = (th.get("core") or {}).get("insight")
        for iid, it in ins.items():
            lv = it.get("level") or 0
            ws = on_page.get(iid, [])
            if lv >= 4 and "S" not in ws:
                e(f"分析の示唆 {iid}(深さ {lv})が重み S のページになっていない: {str(it.get('claim'))[:40]}…(深さ 4・5 の示唆が資料の主役)")
            elif lv == 3 and not ws:
                w(f"分析の示唆 {iid}(深さ 3)がどのページにも無い(載せないなら dropped に理由)")
        if core and "S" not in on_page.get(core, []):
            e(f"価値の芯の示唆 {core} が重み S のページになっていない")
        for p in body:
            if p.get("weight") == "S" and not p.get("insight"):
                w(f"{p.get('id')}: 重み S なのに insight(分析の示唆の id)が無い。開示の並べ替えを主役にしていないか(示唆に足すか、重みを A に)")
        rebs = hyp.get("rebuttals") or []
        if len(rebs) >= 5 and not any("反論" in str(p.get("message", "")) + str(p.get("aim", "")) + str(p.get("hero", "")) for p in body):
            e("弱気の反論と判定のページが無い(反論 | 検証したデータ | 判定 | 評価への反映 の 1 枚を入れる)")
        claim = str(goal.get("claim", ""))
        dec = (th.get("decision") or {})
        if dec.get("action") and dec["action"] not in claim:
            e(f"最終主張 goal.claim に、分析の判断「{dec['action']}」が入っていない")
        if val:
            vb = (val.get("entry") or {}).get("B")
            if vb and f"{round(vb):,}" not in claim and str(round(vb)) not in claim:
                e(f"最終主張 goal.claim に、理論株価 {round(vb):,} が入っていない(valuation.json と合わせる)")
        if d.get("deck_type") == "stock":
            pass   # 価値の橋は 5 章(kind: fair_value)。check_stock が必須ページとして確かめる
        elif (th.get("bridge") or {}).get("steps") and not any("橋" in str(p.get("hero", "")) + str(p.get("aim", "")) for p in body[:6]):
            e("価値の橋のページ(現在値 → 今の利益が続く場合の価値 → 成長と変化の上乗せ → 理論株価)が、本編の最初の 6 枚に無い。"
              "結論と目次の直後に置き、hero か aim に「価値の橋」と書く")
        kills = th.get("kill") or []
        if kills and not any(p.get("form") == "判別表" for p in body):
            e("判別表(続行の線・見直しの線・確認日)のページが無い(投資仮説の撤回の線を資料に載せる)")

    # 分析の 5 工程の台帳との照合(第10版: outlook.json・business_map.json)
    if adir and d.get("deck_type") == "stock":
        op, bp = os.path.join(adir, "outlook.json"), os.path.join(adir, "business_map.json")
        if os.path.exists(op):
            with open(op, encoding="utf-8") as fh:
                ol = json.load(fh)
            if str((ol.get("horizon") or {}).get("year")) != str((d.get("horizon") or {}).get("year")):
                e(f"horizon.year が分析の outlook.json({(ol.get('horizon') or {}).get('year')})と違う")
            rk = sorted([r for r in ol.get("risks", []) if isinstance(r.get("p"), (int, float)) and isinstance(r.get("impact_pct"), (int, float))],
                        key=lambda r: -r["p"] * abs(r["impact_pct"]))
            rm = [p for p in pages if p.get("kind") == "risk_matrix"]
            if rk and rm and not any(str(rk[0].get("name", ""))[:6] in str(p.get("message", "")) + str(p.get("hero", "")) or
                                     any(w_ in str(p.get("message", "")) for w_ in re.findall(r"[一-龥ァ-ヴー]{2,}", str(rk[0].get("name", "")))[:2]) for p in rm):
                w(f"リスクマトリクスのタイトルに、分析の期待損失 1 位「{rk[0].get('name')}」が出ていない(順位を分析と合わせる)")
        else:
            e(f"--analysis {adir} に outlook.json が無い(将来の構造・リスク・今の値段の台帳。meigara-bunseki-method 第10版)")
        if os.path.exists(bp):
            with open(bp, encoding="utf-8") as fh:
                bm = json.load(fh)
            mine = {g_.get("term") for g_ in d.get("glossary", [])}
            for t_ in [g_.get("term") for g_ in bm.get("glossary", []) if g_.get("term") not in mine]:
                w(f"分析の用語「{t_}」が設計書の glossary に無い(資料で使うなら足す)")
    for x in warns:
        print("注意:", x)
    for x in errs:
        print("誤り:", x)
    print(f"storyline: ページ {len(pages)}(本編 {n}: S{count['S']} A{count['A']} B{count['B']})/ 誤り {len(errs)} / 注意 {len(warns)} → {'PASS' if not errs else 'FAIL'}")
    sys.exit(0 if not errs else 1)


if __name__ == "__main__":
    main()
