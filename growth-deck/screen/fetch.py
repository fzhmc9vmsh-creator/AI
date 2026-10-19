#!/usr/bin/env python3
"""Step 2: yfinance で各銘柄の数値を取得する。

出力:
  data/cache/<ticker>.json  銘柄ごとのキャッシュ(24時間以内は再取得しない)
  data/fx.json              USD建て為替 (rates[通貨] = 1 USD あたりの現地通貨額)
  data/errors.csv           取得失敗・欠損の記録(失敗しても続行する)

--offline: yfinance を呼ばず tests/mock/raw/<ticker>.json と tests/mock/fx.json を使う。
"""
import argparse
import csv
import datetime as dt
import json
import math
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from universe import DATA, MOCK, check_network, log

CACHE_DIR = DATA / "cache"
CACHE_TTL_SEC = 24 * 3600
MAX_WORKERS = 4          # 並列は最大4
MAX_RETRY = 5            # 429 のときの指数バックオフ回数
FX_SYMBOLS = {           # 通貨 -> yfinance の為替ティッカー (1 USD = X 現地通貨)
    "JPY": "USDJPY=X", "HKD": "USDHKD=X", "CNY": "USDCNY=X", "SGD": "USDSGD=X",
    "IDR": "USDIDR=X", "THB": "USDTHB=X", "MYR": "USDMYR=X",
}
_errors_lock = threading.Lock()


def clean(v):
    """numpy/pandas の値を JSON に載せられる値へ。NaN/欠損は None。"""
    if v is None:
        return None
    if hasattr(v, "item"):
        try:
            v = v.item()
        except Exception:
            pass
    if isinstance(v, float) and (math.isnan(v) or math.isinf(v)):
        return None
    if isinstance(v, (int, float, str, bool)):
        return v
    return str(v)


def df_to_dict(df):
    """yfinance の DataFrame を {行ラベル: {列名: 値}} にする。空なら None。"""
    if df is None or getattr(df, "empty", True):
        return None
    return {str(idx): {str(k): clean(v) for k, v in row.items()}
            for idx, row in df.to_dict(orient="index").items()}


def safe_name(ticker):
    return ticker.replace("/", "_").replace("^", "_")


def cache_path(ticker):
    return CACHE_DIR / f"{safe_name(ticker)}.json"


def cache_fresh(ticker):
    p = cache_path(ticker)
    if not p.exists():
        return False
    return (time.time() - p.stat().st_mtime) < CACHE_TTL_SEC


# ---------- 取得本体 ----------
def fetch_online(yf, ticker):
    """yfinance から 1 銘柄分を取る。部分的に失敗したブロックは block_errors に残す。"""
    t = yf.Ticker(ticker)
    info = t.info or {}
    block_errors = {}

    def block(name, getter):
        try:
            return getter()
        except Exception as e:
            block_errors[name] = f"{type(e).__name__}: {str(e)[:160]}"
            return None

    data = {
        "ticker": ticker,
        "shortName": info.get("shortName") or info.get("longName"),
        "currency": info.get("currency"),
        "marketCap": clean(info.get("marketCap")),
        "forwardPE": clean(info.get("forwardPE")),
        "trailingPE": clean(info.get("trailingPE")),
        "trailingEps": clean(info.get("trailingEps")),
        "forwardEps": clean(info.get("forwardEps")),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "longBusinessSummary": info.get("longBusinessSummary"),
        "earnings_estimate": block("earnings_estimate", lambda: df_to_dict(t.earnings_estimate)),
        "growth_estimates": block("growth_estimates", lambda: df_to_dict(t.growth_estimates)),
        "revenue_estimate": block("revenue_estimate", lambda: df_to_dict(t.revenue_estimate)),
        "_block_errors": block_errors,
    }
    return data


def fetch_offline(ticker):
    p = MOCK / "raw" / f"{safe_name(ticker)}.json"
    if not p.exists():
        raise FileNotFoundError(f"モックなし: {p.relative_to(MOCK.parent.parent)}")
    data = json.loads(p.read_text(encoding="utf-8"))
    if "__error__" in data:  # 取得失敗を模したモック
        raise RuntimeError(data["__error__"])
    data.setdefault("ticker", ticker)
    data.setdefault("_block_errors", {})
    return data


def with_backoff(fn):
    """429 (Too Many Requests) は指数バックオフで再試行。それ以外は即失敗。"""
    for attempt in range(MAX_RETRY + 1):
        time.sleep(random.uniform(0.3, 0.6))  # 1銘柄ごとの待ち
        try:
            return fn()
        except Exception as e:
            msg = f"{type(e).__name__}: {e}"
            rate_limited = "429" in msg or "Too Many Requests" in msg or "RateLimit" in type(e).__name__
            if not rate_limited or attempt == MAX_RETRY:
                raise
            wait = (2 ** attempt) * 2 + random.uniform(0, 1)
            log(f"  429 を受信。{wait:.1f}s 待って再試行 ({attempt + 1}/{MAX_RETRY})")
            time.sleep(wait)


def process_one(ticker, offline, yf):
    """戻り値: (ticker, status, message)  status は cache / ok / error"""
    if cache_fresh(ticker):
        return ticker, "cache", ""
    try:
        if offline:
            data = fetch_offline(ticker)
        else:
            data = with_backoff(lambda: fetch_online(yf, ticker))
        data["fetched_at"] = dt.datetime.now().isoformat(timespec="seconds")
        data["source"] = "mock" if offline else "yfinance"
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        cache_path(ticker).write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        return ticker, "ok", "; ".join(f"{k}:{v}" for k, v in data.get("_block_errors", {}).items())
    except Exception as e:
        return ticker, "error", f"{type(e).__name__}: {str(e)[:200]}"


def fetch_fx(offline, yf):
    """為替 (1 USD = X 現地通貨) を取得して data/fx.json に保存。失敗通貨は errors に残す。"""
    rates, errors = {"USD": 1.0}, []
    if offline:
        mock = json.loads((MOCK / "fx.json").read_text(encoding="utf-8"))
        rates.update(mock["rates"])
        source, as_of = "mock", mock.get("as_of", "mock")
    else:
        source, as_of = "yfinance", dt.date.today().isoformat()
        for cur, sym in FX_SYMBOLS.items():
            try:
                hist = with_backoff(lambda: yf.Ticker(sym).history(period="5d"))
                close = hist["Close"].dropna()
                if close.empty:
                    raise ValueError("終値が空")
                rates[cur] = float(close.iloc[-1])
            except Exception as e:
                errors.append((f"FX:{sym}", "fx", f"{type(e).__name__}: {str(e)[:200]}"))
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "fx.json").write_text(json.dumps(
        {"source": source, "as_of": as_of, "unit": "1 USD あたりの現地通貨額", "rates": rates},
        ensure_ascii=False, indent=1), encoding="utf-8")
    log(f"fx: {len(rates)} 通貨 ({source}, {as_of})")
    return errors


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--offline", action="store_true", help="モックデータを使う(ネットワーク不使用)")
    ap.add_argument("--universe", default=str(DATA / "universe.csv"))
    ap.add_argument("--workers", type=int, default=MAX_WORKERS)
    ap.add_argument("--limit", type=int, default=0, help="先頭 N 銘柄だけ取得(確認用)")
    args = ap.parse_args()
    t0 = time.time()

    yf = None
    if args.offline:
        log("[offline] yfinance は使わず tests/mock/ を読みます")
    else:
        check_network(["yahoo"])
        import yfinance as yf  # noqa: F811

    with open(args.universe, encoding="utf-8", newline="") as f:
        universe = list(csv.DictReader(f))
    if args.limit:
        universe = universe[: args.limit]
    log(f"fetch: {len(universe)} 銘柄 (並列 {min(args.workers, MAX_WORKERS)})")

    # (ticker, stage, message) の形で集める。FX の失敗も同じ errors.csv に残す。
    fx_errors = fetch_fx(args.offline, yf)
    market_of = {r["ticker"]: r["market"] for r in universe}
    rows_err = [(t, "", "fx", m) for t, _, m in fx_errors]
    partial = []

    counts = {"cache": 0, "ok": 0, "error": 0}
    workers = max(1, min(args.workers, MAX_WORKERS))
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for ticker, status, msg in ex.map(lambda t: process_one(t, args.offline, yf),
                                          [r["ticker"] for r in universe]):
            counts[status] += 1
            if status == "error":
                rows_err.append((ticker, market_of.get(ticker, ""), "fetch", msg))
                log(f"  ERROR {ticker}: {msg}")
            elif status == "ok" and msg:
                partial.append((ticker, msg))

    now = dt.datetime.now().isoformat(timespec="seconds")
    DATA.mkdir(parents=True, exist_ok=True)
    with open(DATA / "errors.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ticker", "market", "stage", "error", "at"])
        for ticker, mkt, stage, msg in rows_err:
            w.writerow([ticker, mkt, stage, msg, now])
        for ticker, msg in partial:
            w.writerow([ticker, market_of.get(ticker, ""), "partial", msg, now])
    log(f"fetch 結果: キャッシュ利用 {counts['cache']} / 新規取得 {counts['ok']} / 取得失敗 {counts['error']}"
        f" / 一部欠損 {len(partial)}  -> data/errors.csv")
    log(f"fetch 完了 ({time.time() - t0:.1f}s)")


if __name__ == "__main__":
    main()
