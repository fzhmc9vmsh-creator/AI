# 一次ふるい 結果サマリー

- 生成: 2026-10-19T16:00:32
- モード: yfinance
- 為替: 2026-10-19 基準 (1 USD あたり 現地通貨: USD 1.0, JPY 158.43899536132812, HKD 7.848219871520996, CNY 6.680099964141846, SGD 1.2797900438308716, IDR 17943.0, THB 33.540000915527344, MYR 4.079999923706055)
- ユニバース: 2056 銘柄 / 取得失敗 4 / 欠損 336 / 一部ブロック欠損(yfinance) 3

## 判定基準

- g2 = (EPS_+1y平均 / 実績年EPS)^(1/2) - 1、g1f = EPS_+1y / EPS_0y - 1、g = min(g2, g1f)
- PE = 株価 / ((EPS_0y + EPS_+1y)/2)、株価 = trailingPE x trailingEps、予想EPSは株価通貨に換算
- PEG = PE / (g x 100)
- 合格: g >= 31% かつ PEG <= 0.75
- 境界: g >= 22% かつ PEG <= 1.00 (合格を除く)
- 共通必須: 実績EPS > 0、予想EPS(0y・+1y) > 0、時価総額 >= 2億USD、アナリスト数 >= 1
- 循環フラグ: 業種による機械的な印 (除外はしない)。合格・境界の件数に併記

## 市場別件数

| 市場 | 対象 | 取得失敗 | 欠損 | 不合格 | 合格 | 境界 | 循環フラグ付き(合格+境界) |
|---|---:|---:|---:|---:|---:|---:|---:|
| JP | 310 | 0 | 35 | 240 | 20 | 15 | 4 |
| US | 925 | 0 | 36 | 679 | 124 | 86 | 59 |
| HK | 226 | 0 | 36 | 101 | 53 | 36 | 25 |
| SH | 488 | 0 | 210 | 164 | 66 | 48 | 37 |
| SG | 28 | 0 | 7 | 18 | 3 | 0 | 1 |
| ID | 15 | 0 | 2 | 10 | 2 | 1 | 3 |
| TH | 28 | 4 | 8 | 13 | 1 | 2 | 0 |
| MY | 36 | 0 | 2 | 18 | 5 | 11 | 6 |
| **合計** | **2056** | **4** | **336** | **1243** | **274** | **199** | **135** |

## 合格・境界 上位50社 (合格を先、PEG 昇順)

| # | 判定 | ticker | 名称 | 市場 | 通貨 | 時価総額(百万USD) | EPS成長 g(%) | 5年成長(%) | PEG | 予想PE(x) | アナリスト数 | 循環 | 備考 |
|---:|---|---|---|---|---|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 合格 | 7241.KL | Nextgreen Global Berhad | MY | MYR | 206 | 44.07 | - | 0.003 | 0.1 | 2 |  |  |
| 2 | 合格 | 1300.HK | Trigiant Group Limited | HK | HKD | 537 | 168.19 | - | 0.018 | 3.0 | 1 |  |  |
| 3 | 合格 | INDY.JK | PT. Indika Energy Tbk | ID | IDR | 557 | 293.64 | - | 0.025 | 7.2 | 4 | ○ |  |
| 4 | 合格 | MUX | McEwen Inc. | US | USD | 970 | 159.89 | - | 0.037 | 5.9 | 2 | ○ |  |
| 5 | 合格 | GAU | Galiano Gold Inc. | US | USD | 602 | 60.53 | - | 0.057 | 3.5 | 5 | ○ |  |
| 6 | 合格 | 3396.HK | Legend Holdings Corporation | HK | HKD | 5,467 | 75.20 | - | 0.060 | 4.5 | 3 |  |  |
| 7 | 合格 | ASYS | Amtech Systems, Inc. | US | USD | 234 | 204.88 | - | 0.079 | 16.1 | 1 |  |  |
| 8 | 合格 | 603929.SS | L&K Engineering (Suzhou) Co.,Ltd. | SH | CNY | 3,662 | 109.68 | - | 0.083 | 9.1 | 1 | ○ |  |
| 9 | 合格 | BZUN | Baozun Inc. | US | USD | 220 | 64.58 | - | 0.083 | 5.4 | 5 |  |  |
| 10 | 合格 | 688349.SS | Sany Renewable Energy Co.,Ltd. | SH | CNY | 3,237 | 132.91 | - | 0.092 | 12.3 | 2 |  |  |
| 11 | 合格 | 7220.T | Musashi Seimitsu Industry Co., Ltd. | JP | JPY | 1,146 | 135.52 | - | 0.093 | 12.7 | 5 | ○ |  |
| 12 | 合格 | 2333.HK | Great Wall Motor Company Limited | HK | HKD | 7,677 | 43.65 | - | 0.103 | 4.5 | 4 | ○ |  |
| 13 | 合格 | 6865.HK | Flat Glass Group Co., Ltd. | HK | HKD | 1,561 | 53.07 | - | 0.104 | 5.5 | 1 |  |  |
| 14 | 合格 | 3858.HK | Jiaxin International Resources Investment Limited | HK | HKD | 2,142 | 43.67 | - | 0.107 | 4.7 | 5 | ○ |  |
| 15 | 合格 | HIMX | Himax Technologies, Inc. | US | USD | 2,124 | 127.13 | - | 0.108 | 13.8 | 1 |  |  |
| 16 | 合格 | 6067.HK | Shenzhen Senior Technology Material Co., Ltd. | HK | HKD | 1,099 | 80.00 | - | 0.110 | 8.8 | 1 | ○ |  |
| 17 | 合格 | 3931.HK | CALB Group Co., Ltd. | HK | HKD | 3,482 | 58.91 | - | 0.110 | 6.5 | 9 |  |  |
| 18 | 合格 | 0777.HK | NetDragon Websoft Holdings Limited | HK | HKD | 527 | 62.41 | - | 0.116 | 7.2 | 2 |  |  |
| 19 | 合格 | 9863.HK | Zhejiang Leapmotor Technology Co., Ltd. | HK | HKD | 6,373 | 87.84 | - | 0.118 | 10.4 | 18 | ○ |  |
| 20 | 合格 | MNTK | Montauk Renewables, Inc. | US | USD | 301 | 74.62 | - | 0.118 | 8.8 | 2 | ○ |  |
| 21 | 合格 | 688411.SS | Beijing HyperStrong Technology Co., Ltd. | SH | CNY | 3,864 | 74.01 | - | 0.121 | 9.0 | 3 |  |  |
| 22 | 合格 | 688525.SS | BIWIN Storage Technology Co., Ltd. | SH | CNY | 11,277 | 35.25 | - | 0.123 | 4.3 | 1 |  |  |
| 23 | 合格 | GGAL | Grupo Financiero Galicia S.A. | US | USD | 5,982 | 47.94 | - | 0.124 | 6.0 | 6 | ○ |  |
| 24 | 合格 | 3308.HK | Zhongji Innolight Co., Ltd. | HK | HKD | 119,981 | 103.49 | - | 0.128 | 13.2 | 3 |  |  |
| 25 | 合格 | 603822.SS | Zhejiang Jiaao Enprotech Stock Co., Ltd | SH | CNY | 796 | 63.27 | - | 0.128 | 8.1 | 1 | ○ |  |
| 26 | 合格 | 1921.HK | Dalipal Holdings Limited | HK | HKD | 604 | 88.54 | - | 0.129 | 11.5 | 1 | ○ |  |
| 27 | 合格 | 6185.HK | CanSino Biologics Inc. | HK | HKD | 954 | 193.17 | - | 0.131 | 25.3 | 2 |  |  |
| 28 | 合格 | 7489.HK | VOYAH Automotive Technology Co., Ltd. | HK | HKD | 800 | 34.62 | - | 0.137 | 4.8 | 1 | ○ |  |
| 29 | 合格 | 2476.HK | Victory Giant Technology (HuiZhou) Co.,Ltd | HK | HKD | 18,921 | 74.16 | - | 0.143 | 10.6 | 1 |  |  |
| 30 | 合格 | ALGT | Allegiant Travel Company | US | USD | 1,843 | 60.97 | - | 0.144 | 8.8 | 14 | ○ |  |
| 31 | 合格 | EGO | Eldorado Gold Corporation | US | USD | 9,290 | 60.28 | - | 0.144 | 8.7 | 11 | ○ |  |
| 32 | 合格 | RE4.SI | Geo Energy Resources Limited | SG | SGD | 726 | 60.92 | - | 0.145 | 8.8 | 2 | ○ |  |
| 33 | 合格 | 1030.HK | Seazen Group Limited | HK | HKD | 1,278 | 61.73 | - | 0.146 | 9.0 | 9 | ○ |  |
| 34 | 合格 | HQU.SI | Oiltek International Limited | SG | SGD | 359 | 106.02 | - | 0.156 | 16.6 | 3 |  |  |
| 35 | 合格 | 1907.HK | China Risun Group Limited | HK | HKD | 866 | 38.17 | - | 0.158 | 6.0 | 2 | ○ |  |
| 36 | 合格 | 688472.SS | CSI Solar Co., Ltd. | SH | CNY | 4,352 | 84.13 | - | 0.159 | 13.4 | 2 |  |  |
| 37 | 合格 | 603520.SS | Zhejiang Starry Pharmaceutical Co.,Ltd. | SH | CNY | 526 | 110.34 | - | 0.161 | 17.8 | 1 |  |  |
| 38 | 合格 | BTG | B2Gold Corp. | US | USD | 6,942 | 43.65 | - | 0.161 | 7.0 | 12 | ○ |  |
| 39 | 合格 | LOVE | The Lovesac Company | US | USD | 209 | 57.76 | - | 0.162 | 9.4 | 1 |  |  |
| 40 | 合格 | 1989.HK | Delton Technology (Guangzhou) Inc. | HK | HKD | 5,018 | 63.84 | - | 0.163 | 10.4 | 2 |  |  |
| 41 | 合格 | 0826.HK | Tiangong International Company Limited | HK | HKD | 885 | 45.57 | - | 0.166 | 7.5 | 3 | ○ |  |
| 42 | 合格 | TPG | TPG Inc. | US | USD | 16,847 | 90.36 | - | 0.167 | 15.1 | 1 |  |  |
| 43 | 合格 | NESR | National Energy Services Reunited Corp. | US | USD | 1,918 | 53.92 | - | 0.167 | 9.0 | 9 | ○ |  |
| 44 | 合格 | LFTO | Liftoff Mobile, Inc. | US | USD | 2,765 | 91.83 | - | 0.168 | 15.5 | 3 |  |  |
| 45 | 合格 | CDNL | Cardinal Infrastructure Group Inc. | US | USD | 340 | 33.13 | - | 0.168 | 5.6 | 2 | ○ |  |
| 46 | 合格 | ARIS | Aris Mining Corporation | US | USD | 3,598 | 40.60 | - | 0.174 | 7.0 | 5 | ○ |  |
| 47 | 合格 | 600409.SS | Tangshan Sanyou Chemical Industries Co.,Ltd | SH | CNY | 1,799 | 110.53 | - | 0.178 | 19.7 | 1 | ○ |  |
| 48 | 合格 | HRMY | Harmony Biosciences Holdings, Inc. | US | USD | 2,176 | 34.14 | - | 0.179 | 6.1 | 2 |  |  |
| 49 | 合格 | 1888.HK | Kingboard Laminates Holdings Limited | HK | HKD | 15,853 | 59.74 | - | 0.181 | 10.8 | 6 |  |  |
| 50 | 合格 | FBRT | Franklin BSP Realty Trust, Inc. | US | USD | 500 | 33.49 | - | 0.183 | 6.1 | 5 |  |  |

## 不合格の理由 (件数。1銘柄に複数理由があれば重複計上)

- EPS成長<22%(来期): 591
- EPS成長<22%: 508
- PEG>1.00: 91
- 基準EPS<=0(CAGR計算不能): 41
- 予想EPS(0y)<=0(赤字): 9
- 時価総額<2億USD: 9
- 予想EPS(+1y)<=0(赤字): 1

## 欠損の内訳 (項目別件数)

- 株価または予想EPS: 344
- 予想EPS(+1y): 336
- 予想EPS(0y): 323
- アナリスト数(+1y): 309
- yearAgoEps(0y): 27
- 実績EPS: 3
- marketCap: 2

## 取得失敗・欠損の銘柄

| ticker | 市場 | 区分 | 内容 |
|---|---|---|---|
| ASML | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| BN | US | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| CCJ | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| FOX | US | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| LEN-B | US | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| KSPI | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| COKE | US | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| SKM | US | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| FMS | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| GGB | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| CAE | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| STN | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| SBSW | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| ENIC | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| MDA | US | 欠損 | 予想EPS(0y);予想EPS(+1y);株価または予想EPS |
| BMA | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| DOO | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| AYA | US | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| SRAD | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| ZGN | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| TGB | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| KYIV | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| ALM | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| RNW | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| BGSI | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| PICS | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| NOMD | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| AGBK | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| ESRT | US | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| OBE | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| NRDS | US | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| KE | US | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| BNED | US | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| NOA | US | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| IMMR | US | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| CPSS | US | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 9843.T | JP | 欠損 | 予想EPS(0y);株価または予想EPS |
| 7419.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 8425.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 3282.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 8964.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 4107.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 1333.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 3591.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 8957.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 8966.T | JP | 欠損 | 予想EPS(0y);株価または予想EPS |
| 3481.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 8032.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 3296.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 7148.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 7512.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 8125.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 3539.T | JP | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 4326.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 8244.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 3708.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 7128.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 4022.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 6413.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 1822.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 6328.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 5461.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 7860.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 4318.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 1375.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 8281.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 5304.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 3475.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 5659.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 2792.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 6249.T | JP | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 6951.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 3996.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 3668.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| 1735.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 9889.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 2880.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 0467.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 0934.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 6190.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 1375.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 2451.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 0866.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 9936.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 6686.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 1809.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 6826.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 0581.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 2342.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 1873.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 2409.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 6626.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 0732.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 2660.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 0331.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 0882.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 0098.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 2499.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 2197.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 1899.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 1911.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 1045.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 0658.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 2219.HK | HK | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 9991.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 3798.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 2886.HK | HK | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 601868.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600010.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600221.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688313.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600869.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 601777.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600021.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688728.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 601866.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600956.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600667.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600777.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603920.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600536.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600737.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600316.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600566.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600967.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600816.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600038.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688001.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 601608.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600516.SS | SH | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603663.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603306.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688368.SS | SH | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 601101.SS | SH | 欠損 | 予想EPS(0y);株価または予想EPS |
| 600179.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603002.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603678.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688403.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688208.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600528.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600056.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600888.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688166.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603328.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603906.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603303.SS | SH | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600475.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600635.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600155.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 601068.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600877.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603626.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600416.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603693.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600864.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603283.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600651.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600456.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600420.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603203.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600572.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 601801.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 900948.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603393.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600338.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600787.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600184.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 601860.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600728.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600509.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 601003.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603300.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 605123.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688076.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600929.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603800.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603269.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 605006.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 605222.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603608.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603319.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603360.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603220.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600789.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603202.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603466.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600973.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603227.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600746.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600587.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600917.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600889.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603538.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600903.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600313.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603219.SS | SH | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603496.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600771.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 605365.SS | SH | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600108.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603196.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 601388.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 605007.SS | SH | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603985.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603091.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603980.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603977.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603229.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603279.SS | SH | 欠損 | 予想EPS(0y);株価または予想EPS |
| 603050.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600966.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688601.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600603.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 601500.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603990.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603399.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603366.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600425.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600081.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600449.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600742.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688334.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600477.SS | SH | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600106.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603098.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603311.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603012.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603111.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600230.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600829.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600576.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600165.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600284.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688623.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603211.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600644.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688109.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603499.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600790.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603158.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688226.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600681.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688711.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688267.SS | SH | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603088.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688307.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 605300.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600168.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 605268.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600976.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603097.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603661.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603020.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600101.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600628.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603615.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603611.SS | SH | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603081.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600222.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603928.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 601599.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603960.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688786.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603676.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600805.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603032.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603869.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600727.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603167.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603966.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600505.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603798.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600333.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603639.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600527.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603725.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603339.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600067.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600785.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603357.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600467.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 605077.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603231.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600731.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603987.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603350.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688070.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688722.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603315.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603289.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603970.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603886.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603527.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603280.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603585.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688687.SS | SH | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600620.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603677.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603037.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603017.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 605166.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688080.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600858.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603617.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603086.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 688201.SS | SH | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603076.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| 603326.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603787.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 900926.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603117.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603700.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600692.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603900.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 603041.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600965.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 600561.SS | SH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| G07.SI | SG | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| T14.SI | SG | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| NC2.SI | SG | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| W05.SI | SG | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| U9E.SI | SG | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 5GD.SI | SG | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| BHK.SI | SG | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| BTPN.JK | ID | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| CNMA.JK | ID | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| GULF-R.BK | TH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| TRUE.BK | TH | 取得失敗 | YFRateLimitError: Too Many Requests. Rate limited. Try after a while. |
| PTTGC.BK | TH | 取得失敗 | YFRateLimitError: Too Many Requests. Rate limited. Try after a while. |
| OR.BK | TH | 取得失敗 | YFRateLimitError: Too Many Requests. Rate limited. Try after a while. |
| CCET.BK | TH | 取得失敗 | YFRateLimitError: Too Many Requests. Rate limited. Try after a while. |
| KCE.BK | TH | 欠損 | marketCap;実績EPS;予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);yearAgoEps(0y);株価または予想EPS |
| BGRIM.BK | TH | 欠損 | marketCap;実績EPS;予想EPS(0y);予想EPS(+1y);yearAgoEps(0y);株価または予想EPS |
| LHHOTEL.BK | TH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| TPIPP.BK | TH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| SPCG.BK | TH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| WHAIR.BK | TH | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| EASTW.BK | TH | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 4162.KL | MY | 欠損 | 予想EPS(0y);予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |
| 8052.KL | MY | 欠損 | 予想EPS(+1y);アナリスト数(+1y);株価または予想EPS |

- 取得段階の記録: data/errors.csv (取得失敗 4 件 / 一部ブロック欠損 3 件)

## ユニバース段階の警告 (data/errors_universe.csv)

- [HK/no-source] 取扱銘柄の一覧が無い(data/rakuten/HK.csv を配置してください)
- [SH/no-source] 取扱銘柄の一覧が無い(data/rakuten/SH.csv を配置してください)
- [SG/no-source] 取扱銘柄の一覧が無い(data/rakuten/SG.csv を配置してください)
- [ID/no-source] 取扱銘柄の一覧が無い(data/rakuten/ID.csv を配置してください)
- [TH/no-source] 取扱銘柄の一覧が無い(data/rakuten/TH.csv を配置してください)
- [MY/no-source] 取扱銘柄の一覧が無い(data/rakuten/MY.csv を配置してください)

## 注記

- 境界の定義は、合格を除いて 'g >= 22% かつ PEG <= 1.00' を満たすもの。必須条件(EPS・時価総額・アナリスト)を満たさないものは境界に入れず不合格。
- 循環フラグは業種名の機械的判定。メモリ半導体などは人が個別に見直すこと。
- 詳細は out/all_scored.csv (全銘柄の数値と理由)、out/pass.csv、out/borderline.csv を参照。
