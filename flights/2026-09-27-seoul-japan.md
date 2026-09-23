# 2026-09-27(日) ソウル → 日本 片道航空券 調査結果

## 結論: ネットワークが遮断されていたため、運賃を取得できなかった

- 取得試行日時(UTC): 2026-09-23T15:54:19Z〜15:54:25Z
- 条件: 大人1名・エコノミー・片道、出発 ICN / GMP、到着 大阪(KIX/ITM)・東京(NRT/HND)・福岡(FUK)
- 目標: 1万円以内(100円≒870ウォン、1万円≒約87,000ウォン)

この実行環境の外向き通信は、エージェントプロキシの上位ゲートウェイがすべての対象サイトへの
CONNECT を **403 で拒否**した(ネットワークポリシーで拒否されたか、上流で失敗した)。
そのため、ブラウザ(Playwright)での検索は行っていない。**便・価格のデータは 1 件も取得できていない。**
下の表に数字は入れていない(推測の価格は書かない)。

## 各サイトの取得可否

| サイト | HTTP 結果 | プロキシ記録 (recentRelayFailures) |
|---|---|---|
| www.google.com (Google フライト) | 000 | connect_rejected: gateway answered 403 to CONNECT |
| www.skyscanner.co.kr | 000 | connect_rejected: 403 |
| www.skyscanner.jp | 000 | connect_rejected: 403 |
| www.kayak.co.kr | 000 | connect_rejected: 403 |
| kr.trip.com | 000 | connect_rejected: 403 |
| flight.naver.com (NAVER 항공권) | 000 | connect_rejected: 403 |
| www.flypeach.com (Peach) | 000 | connect_rejected: 403 |
| www.jejuair.net (チェジュ航空) | 000 | connect_rejected: 403 |
| www.airseoul.com (エアソウル) | 000 | connect_rejected: 403 |
| www.eastarjet.com (イースター航空) | 000 | connect_rejected: 403 |
| www.jinair.com (ジンエアー) | 000 | connect_rejected: 403 |
| www.twayair.com (ティーウェイ) | 000 | connect_rejected: 403 |

## 都市ごとの結果

| 都市 | 最安便 | 1万円以内か |
|---|---|---|
| 大阪 (KIX/ITM) | 取得不可 | 判定不可 |
| 東京 (NRT/HND) | 取得不可 | 判定不可 |
| 福岡 (FUK) | 取得不可 | 判定不可 |

## 自分で確認する場合の検索 URL

- Google フライト: 
  - 大阪 https://www.google.com/travel/flights?q=Flights%20to%20OSA%20from%20SEL%20on%202026-09-27%20oneway&curr=KRW&hl=ko
  - 東京 https://www.google.com/travel/flights?q=Flights%20to%20TYO%20from%20SEL%20on%202026-09-27%20oneway&curr=KRW&hl=ko
  - 福岡 https://www.google.com/travel/flights?q=Flights%20to%20FUK%20from%20SEL%20on%202026-09-27%20oneway&curr=KRW&hl=ko
- Skyscanner KR:
  - https://www.skyscanner.co.kr/transport/flights/sela/osaa/260927/?adultsv2=1&rtn=0
  - https://www.skyscanner.co.kr/transport/flights/sela/tyoa/260927/?adultsv2=1&rtn=0
  - https://www.skyscanner.co.kr/transport/flights/sela/fuk/260927/?adultsv2=1&rtn=0
- KAYAK KR:
  - https://www.kayak.co.kr/flights/SEL-OSA/2026-09-27?sort=price_a
  - https://www.kayak.co.kr/flights/SEL-TYO/2026-09-27?sort=price_a
  - https://www.kayak.co.kr/flights/SEL-FUK/2026-09-27?sort=price_a

## 総額に含まれていない可能性がある費用(確認時の注意)

- 受託手荷物: LCC(Peach・チェジュ航空・ジンエアー・ティーウェイ・エアソウル・イースター航空など)の最安運賃は、
  機内持ち込みのみ(多くは 7〜10kg)で、受託手荷物は別料金のことが多い。
- 決済手数料・発券手数料: 比較サイトや旅行会社経由では、最終画面で決済手数料が加算される場合がある。
- 座席指定料、燃油サーチャージ・空港使用料が表示額に含まれるかは、サイトごとに最終画面で確認する必要がある。

## 再実行に必要なこと

この環境のネットワーク設定(Claude Code on the web の環境設定の network access)で、
上記ドメインへの外向き通信を許可すれば、同じ手順でライブ取得を再実行できる。
