#!/usr/bin/env python3
"""スライドの設計書 storyline.json の検査(references/story-design.md)。標準ライブラリだけで動く。

    python3 check_storyline.py storyline.json
    python3 check_storyline.py storyline.json --analysis <分析の作業フォルダ>   # 投資資料: 分析の示唆・投資仮説と照合する

狙い・順番・一貫性・重み付けが設計に入っているかを確かめる。FAIL のまま実装に進まない。
--analysis を付けると、meigara-bunseki-method の hypotheses.json(示唆のカード・投資仮説)と valuation.json を読み、
深さ 4・5 の示唆が主役のページになっているか、結論が投資仮説と合っているかを確かめる。
"""
import json
import os
import re
import sys

WEIGHTS = ("S", "A", "B", "C", "D")
FIGS = ("図", "関係図", "ロードマップ", "判別表", "表")
CONNECT = ("だから", "なぜなら", "では", "しかし", "具体的には", "その結果", "次に", "また")
LISTY = ("次に", "また")
DESCRIPTIVE = re.compile(r"(について|の概要|の推移|の状況|の比較|の一覧|の内訳|の分析|まとめ)[。]?$")


def filled(v, n=4):
    return isinstance(v, str) and len(v.strip()) >= n and "|" not in v and not (v.strip().startswith("(") and v.strip().endswith(")"))


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
        if (th.get("bridge") or {}).get("steps") and not any("橋" in str(p.get("hero", "")) + str(p.get("aim", "")) for p in body[:6]):
            e("価値の橋のページ(現在値 → 今の利益が続く場合の価値 → 成長と変化の上乗せ → 理論株価)が、本編の最初の 6 枚に無い。"
              "結論と目次の直後に置き、hero か aim に「価値の橋」と書く")
        kills = th.get("kill") or []
        if kills and not any(p.get("form") == "判別表" for p in body):
            e("判別表(続行の線・見直しの線・確認日)のページが無い(投資仮説の撤回の線を資料に載せる)")
        # 2026-11-17 利用者の指摘「最新決算の内容反映してないし、事業として何をしてるかも記載ない。事業理解の項目がない。普通に有り得ない」
        STD = {"business_overview": "会社と事業の概要(何をしている会社か: 誰に・何を・どう使われ・どう課金し・沿革と規模)",
               "industry_basics": "業界の仕組みとお金の流れ(顧客の業務・収入の源・支払者・業界の規模と数・自社の位置)",
               "latest_results": "最新決算のサマリー(直近の四半期の実績と前年比・会社予想の進捗・主要KPI・トピックス・前の四半期から変わったこと)"}
        for k, what in STD.items():
            hit = [i for i, p in enumerate(body) if p.get("std") == k]
            if not hit:
                e(f"必須のページ std: \"{k}\" が無い = {what}。分析の前に、読み手が事業と直近の数字を知らないまま進まない")
            elif hit[0] >= 8:
                e(f"std: \"{k}\" のページが本編の {hit[0] + 1} 枚目。本編の最初の 8 枚に置く(分析の前提)")
            elif k == "latest_results" and not re.search(r"\d", str(body[hit[0]].get("message", ""))):
                e("最新決算のページの message に数字が無い(直近の四半期の実績を数字で言い切る)")

    for x in warns:
        print("注意:", x)
    for x in errs:
        print("誤り:", x)
    print(f"storyline: ページ {len(pages)}(本編 {n}: S{count['S']} A{count['A']} B{count['B']})/ 誤り {len(errs)} / 注意 {len(warns)} → {'PASS' if not errs else 'FAIL'}")
    sys.exit(0 if not errs else 1)


if __name__ == "__main__":
    main()
