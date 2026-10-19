#!/usr/bin/env python3
"""Step 1: 対象銘柄リストを作る -> data/universe.csv (ticker, name, market, source)

  日本  : JPX 上場銘柄一覧 (data_j.xls)。ETF・REIT・優先株を除外。ticker は XXXX.T
  米国  : 楽天の取扱CSV(data/rakuten/US.csv)があればそれを使い、無ければ
          NASDAQ Trader の全上場ファイル(Nasdaq/NYSE)をフォールバックとして使う
  その他: data/rakuten/<MKT>.csv (楽天証券の取扱銘柄を保存したCSV) があれば使う。
          無ければ銘柄を取得できず、data/errors_universe.csv に記録する。
          接尾辞: HK=.HK, SH=.SS, SG=.SI, ID=.JK, TH=.BK, MY=.KL

  --offline : ネットワークを使わず tests/mock/universe_mock.csv を使う。
"""
import argparse
import csv
import datetime as dt
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urljoin

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
MOCK = HERE / "tests" / "mock"

JPX_STATS_PAGE = "https://www.jpx.co.jp/markets/statistics-equities/misc/01.html"
NASDAQ_LISTED = "https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt"
NASDAQ_OTHER = "https://www.nasdaqtrader.com/dynamic/symdir/otherlisted.txt"
FOREIGN_SUFFIX = {"HK": ".HK", "SH": ".SS", "SG": ".SI", "ID": ".JK", "TH": ".BK", "MY": ".KL"}

# 接続確認の対象。キーは check_network() に渡す名前。
CHECK_TARGETS = {
    "jpx": JPX_STATS_PAGE,
    "yahoo": "https://query1.finance.yahoo.com/v8/finance/chart/AAPL?range=1d&interval=1d",
    "rakuten": "https://www.rakuten-sec.co.jp/",
}

EXCLUDE_JP = re.compile(r"ETF|ETN|REIT|投資法人|インフラファンド|優先|Ｅ[ＴＲ]Ｆ|上場投資")


def log(msg):
    print(f"[{dt.datetime.now():%H:%M:%S}] {msg}", flush=True)


def _ssl_context():
    cafile = (os.environ.get("REQUESTS_CA_BUNDLE") or os.environ.get("SSL_CERT_FILE")
              or os.environ.get("CURL_CA_BUNDLE"))
    return ssl.create_default_context(cafile=cafile) if cafile else ssl.create_default_context()


def http_get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (growth-deck-screen)"})
    with urllib.request.urlopen(req, timeout=timeout, context=_ssl_context()) as r:
        return r.read()


def check_network(targets, exit_on_fail=True):
    """接続先に到達できるか確認する。到達できない接続先があれば分かりやすく報告して終了する(exit 2)。
    targets: CHECK_TARGETS のキーのリスト。戻り値は {キー: 理由} の失敗一覧。"""
    failed = {}
    for key in targets:
        url = CHECK_TARGETS[key]
        try:
            http_get(url, timeout=8)
            log(f"[network] {key}: OK")
        except urllib.error.HTTPError as e:
            failed[key] = f"HTTP {e.code} (プロキシまたは接続先による拒否の可能性)"
        except Exception as e:  # 接続拒否・TLS・タイムアウトなど
            failed[key] = f"{type(e).__name__}: {str(e)[:120]}"
    if failed and exit_on_fail:
        print("", file=sys.stderr)
        print("ERROR: 外部ネットワークに接続できません。接続が拒否されています。", file=sys.stderr)
        for k, why in failed.items():
            print(f"  - {k}: {why}  [{CHECK_TARGETS[k]}]", file=sys.stderr)
        print("この環境では Yahoo / JPX / 楽天証券への接続が許可されていないため、"
              "実データ取得はできません。", file=sys.stderr)
        print("代わりに --offline を付けて実行してください(tests/mock/ のモックデータで 3 段階が動きます)。",
              file=sys.stderr)
        sys.exit(2)
    return failed


# ---------- 日本 (JPX) ----------
def load_jp():
    html = http_get(JPX_STATS_PAGE).decode("utf-8", "replace")
    m = re.search(r'href="([^"]*data_j\.xls[^"]*)"', html)
    if not m:
        raise RuntimeError("JPX ページに data_j.xls のリンクが見つからない")
    url = urljoin(JPX_STATS_PAGE, m.group(1))
    raw_dir = DATA / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    xls = raw_dir / "data_j.xls"
    xls.write_bytes(http_get(url))
    import pandas as pd  # xlrd を使用
    df = pd.read_excel(xls, dtype=str)
    col = lambda key: next(c for c in df.columns if key in str(c))
    code_c, name_c, kind_c = col("コード"), col("銘柄名"), col("市場・商品区分")
    rows, excluded = [], 0
    for _, r in df.iterrows():
        code = str(r[code_c]).strip()
        name = str(r[name_c]).strip()
        kind = str(r[kind_c])
        if not re.fullmatch(r"[0-9A-Z]{4}", code):
            continue
        if EXCLUDE_JP.search(f"{kind} {name}"):
            excluded += 1
            continue
        rows.append({"ticker": f"{code}.T", "name": name, "market": "JP", "source": "jpx:data_j.xls"})
    log(f"JP: JPX 一覧 {len(df)} 行 -> 対象 {len(rows)} (ETF/REIT/優先株 除外 {excluded})")
    return rows, []


# ---------- 米国 (NASDAQ Trader 全上場) ----------
def _parse_pipe(text):
    lines = [ln for ln in text.splitlines() if ln and not ln.startswith("File Creation Time")]
    header = lines[0].split("|")
    return [dict(zip(header, ln.split("|"))) for ln in lines[1:]]


def load_us_fallback():
    rows = []
    for url, sym_key, src in [
        (NASDAQ_LISTED, "Symbol", "nasdaqtrader:nasdaqlisted"),
        (NASDAQ_OTHER, "ACT Symbol", "nasdaqtrader:otherlisted"),
    ]:
        for r in _parse_pipe(http_get(url).decode("utf-8", "replace")):
            if r.get("ETF") == "Y" or r.get("Test Issue") == "Y":
                continue
            sym = (r.get(sym_key) or "").strip().replace(".", "-")  # BRK.B -> BRK-B (Yahoo 体系)
            if not re.fullmatch(r"[A-Z0-9-]+", sym):
                continue
            rows.append({"ticker": sym, "name": (r.get("Security Name") or "").strip(),
                         "market": "US", "source": src})
    log(f"US: NASDAQ Trader フォールバック {len(rows)} 銘柄")
    return rows, []


# ---------- その他 (楽天の取扱CSV を保存したもの) ----------
def load_rakuten_csv(market):
    """data/rakuten/<MKT>.csv: 1列目相当のコード列と銘柄名列を自動判定して読む。"""
    path = DATA / "rakuten" / f"{market}.csv"
    if not path.exists():
        return None
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = list(csv.reader(f))
    header = [h.strip() for h in reader[0]]
    code_i = next((i for i, h in enumerate(header) if re.search(r"コード|code|symbol|シンボル", h, re.I)), 0)
    name_i = next((i for i, h in enumerate(header) if re.search(r"名|name", h, re.I)), 1)
    rows = []
    for rec in reader[1:]:
        if len(rec) <= max(code_i, name_i):
            continue
        code = rec[code_i].strip()
        if not code:
            continue
        if market == "HK" and code.isdigit():
            code = code.zfill(4)
        suffix = "" if market == "US" else FOREIGN_SUFFIX[market]
        rows.append({"ticker": code + suffix, "name": rec[name_i].strip(),
                     "market": market, "source": f"rakuten:{path.name}"})
    log(f"{market}: 楽天取扱CSV {len(rows)} 銘柄 ({path})")
    return rows


def build_online():
    check_network(["jpx"])
    rows, errors = [], []
    try:
        jp_rows, _ = load_jp()
        rows += jp_rows
    except Exception as e:
        errors.append(("JP", "jpx", f"{type(e).__name__}: {e}"))
    try:
        us = load_rakuten_csv("US")
        if us is None:
            us, _ = load_us_fallback()
        rows += us
    except Exception as e:
        errors.append(("US", "us-list", f"{type(e).__name__}: {e}"))
    for mkt in FOREIGN_SUFFIX:
        if mkt == "US":
            continue
        try:
            got = load_rakuten_csv(mkt)
        except Exception as e:
            errors.append((mkt, "rakuten-csv", f"{type(e).__name__}: {e}"))
            continue
        if got is None:
            errors.append((mkt, "no-source",
                           f"取扱銘柄の一覧が無い(data/rakuten/{mkt}.csv を配置してください)"))
            continue
        rows += got
    return rows, errors


def build_offline():
    src = MOCK / "universe_mock.csv"
    with open(src, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    log(f"[offline] {src.relative_to(HERE)} から {len(rows)} 銘柄を読み込み")
    return rows, []


def write_outputs(rows, errors):
    DATA.mkdir(parents=True, exist_ok=True)
    seen, uniq = set(), []
    for r in rows:
        if r["ticker"] in seen:
            continue
        seen.add(r["ticker"])
        uniq.append(r)
    with open(DATA / "universe.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ticker", "name", "market", "source"])
        w.writeheader()
        w.writerows(uniq)
    with open(DATA / "errors_universe.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["market", "stage", "error", "at"])
        now = dt.datetime.now().isoformat(timespec="seconds")
        for mkt, stage, msg in errors:
            w.writerow([mkt, stage, msg, now])
    counts = {}
    for r in uniq:
        counts[r["market"]] = counts.get(r["market"], 0) + 1
    log(f"universe.csv: {len(uniq)} 銘柄 (重複除去後) 市場別 {counts}")
    for mkt, stage, msg in errors:
        log(f"WARN universe [{mkt}/{stage}] {msg}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--offline", action="store_true", help="ネットワークを使わずモックデータを使う")
    args = ap.parse_args()
    t0 = time.time()
    if args.offline:
        rows, errors = build_offline()
    else:
        rows, errors = build_online()
    write_outputs(rows, errors)
    log(f"universe 完了 ({time.time() - t0:.1f}s)")


if __name__ == "__main__":
    main()
