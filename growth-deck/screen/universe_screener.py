"""Yahoo スクリーナーで8市場(楽天証券の取扱市場)の上場株を時価総額2億USD以上で一括取得する(Opus 2026-10-19)。
楽天証券の取扱一覧は JS 読み込みで取得できないため、各市場の全上場株(上位集合)を使う。
出力: data/screener_quotes.csv(1銘柄1行、スクリーナーの数値つき)"""
import time, json, csv, sys
import yfinance as yf
from yfinance import EquityQuery as Q

# 2億USD を現地通貨に換算した時価総額の下限(概算の為替。yfinance のスクリーナーは現地通貨の時価総額で絞る)
REGIONS = {
    'us': dict(cap=2e8, exch={'NMS', 'NYQ', 'ASE', 'NGM', 'NCM', 'PCX', 'BTS'}),
    'jp': dict(cap=2e8 * 150, exch={'JPX'}),
    'hk': dict(cap=2e8 * 7.8, exch={'HKG'}),
    'cn': dict(cap=2e8 * 7.1, exch={'SHH'}),          # 楽天は上海A株のみ(深センは除く)
    'sg': dict(cap=2e8 * 1.3, exch={'SES'}),
    'id': dict(cap=2e8 * 16500, exch={'JKT'}),
    'th': dict(cap=2e8 * 33, exch={'SET'}),
    'my': dict(cap=2e8 * 4.2, exch={'KLS'}),
}
FIELDS = ['symbol', 'longName', 'shortName', 'exchange', 'quoteType', 'currency', 'financialCurrency', 'marketCap', 'regularMarketPrice',
          'forwardPE', 'trailingPE', 'epsForward', 'epsCurrentYear', 'epsTrailingTwelveMonths', 'priceEpsCurrentYear',
          'averageDailyVolume3Month', 'fiftyTwoWeekChangePercent', 'fiftyTwoWeekHighChangePercent', 'averageAnalystRating']

def fetch_region(reg, cap):
    out, offset, total = [], 0, None
    q = Q('and', [Q('eq', ['region', reg]), Q('gt', ['intradaymarketcap', cap])])
    while True:
        for attempt in range(6):
            try:
                r = yf.screen(q, size=250, offset=offset, sortField='intradaymarketcap', sortAsc=False)
                break
            except Exception as e:
                w = 2 ** attempt
                print(f'  {reg} offset {offset}: {type(e).__name__} {e} -> {w}s 待ち', flush=True)
                time.sleep(w)
        else:
            print(f'  {reg}: 取得を断念 offset={offset}'); break
        total = r.get('total', 0)
        qs = r.get('quotes', [])
        out += qs
        offset += len(qs)
        if not qs or offset >= total: break
        time.sleep(0.6)
    return out, total

if __name__ == '__main__':
    rows = []
    for reg, cfg in REGIONS.items():
        qs, total = fetch_region(reg, cfg['cap'])
        keep = [x for x in qs if x.get('exchange') in cfg['exch'] and x.get('quoteType') == 'EQUITY']
        print(f'{reg}: 取得 {len(qs)}/{total} -> 取引所・株式で絞って {len(keep)}', flush=True)
        for x in keep:
            d = {k: x.get(k) for k in FIELDS}; d['region'] = reg
            rows.append(d)
    with open('data/screener_quotes.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS + ['region']); w.writeheader(); w.writerows(rows)
    print('合計', len(rows))
