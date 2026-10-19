# Opus による残りの確認対象の仕分け(2026-10-19)

全件(2,052社取得)の一次判定で、業種除外の後に残った確認対象は 293社。うち 44社を Sonnet の早期判定(A〜D班)に回した。
残りは次の理由で、構造A+(平均4.0以上)の見込みが低いと Opus が判断した。いずれも事業内容(longBusinessSummary)と業種・カバレッジを見て判断している。

## 共通の除外理由

- 薄いカバレッジ(予想アナリスト 2人以下)の中国A株・香港中小: コンセンサス経路が成り立たず、成長A+の3経路を満たせない。ガバナンス・情報開示で条件10・13も下がる。
- 需要の底からの反発(rebound、trailing_jump): 一次判定の成長率が実力を表さない。
- 受託・市況品・規制業種: 価格決定力(条件11)と継続性(条件12)が B 以下になる。

## Sonnet に回した銘柄

- A班: NVDA AVGO AMD MRVL CRDO ALAB MTSI LSCC CDNS 6809.HK 688256.SS
- B班: TSM AMAT 8035.T COHR VRT 3308.HK HONA FTAI KRMN AEIS
- C班: LLY ALNY CORT BMRN APP BABA 9988.HK SE RDDT HUBS LFTO
- D班: STX BE INIO 0268.HK TOST ETSY 4480.T 6526.T TSEM 688200.SS 603171.SS BSP

## 除外した銘柄(業種別)

### Advertising Agencies(2社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 1860.HK | Mobvista Inc. | pass | 32 | 0.48 | fx_converted |
| 0917.HK | Qunabox Group Limited | borderline | 23 | 0.14 | pe_suspect;fx_converted;thin_coverage;micro |

### Aerospace & Defense(9社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 7409.T | AeroEdge Co., Ltd. | pass | 60 | 0.35 | thin_coverage;micro |
| AVEX | AEVEX Corp. | pass | 60 | 0.44 |  |
| 9822.KL | SAM Engineering & Equipment (M) Be | pass | 49 | 0.57 |  |
| 688239.SS | Guizhou Aviation Technical Develop | pass | 37 | 0.69 |  |
| 600150.SS | China CSSC Holdings Limited | borderline | 30 | 0.38 | thin_coverage |
| SARO | StandardAero, Inc. | borderline | 25 | 0.65 |  |
| EMBJ | Embraer S.A. | borderline | 24 | 0.87 |  |
| RGR | Sturm, Ruger & Company, Inc. | borderline | 27 | 0.90 | thin_coverage |
| 688281.SS | Shaanxi Huaqin Technology Industry | borderline | 34 | 0.96 | thin_coverage |

### Apparel Manufacturing(3社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| VFC | V.F. Corporation | borderline | 23 | 0.59 |  |
| SGC | Superior Group of Companies, Inc. | borderline | 29 | 0.61 | micro |
| 3002.T | Gunze Limited | borderline | 30 | 0.74 | trailing_jump;thin_coverage |

### Apparel Retail(2社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| REF | Reformation Inc. | pass | 46 | 0.49 |  |
| 603877.SS | Ningbo Peacebird Fashion Co.,Ltd. | borderline | 26 | 0.81 |  |

### Asset Management(2社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| TPG | TPG Inc. | pass | 90 | 0.17 | thin_coverage |
| ARES | Ares Management Corporation | borderline | 22 | 0.80 |  |

### Biotechnology(4社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| HRMY | Harmony Biosciences Holdings, Inc. | pass | 34 | 0.18 | thin_coverage |
| JAZZ | Jazz Pharmaceuticals plc | borderline | 23 | 0.38 |  |
| 1801.HK | Innovent Biologics, Inc. | borderline | 48 | 0.89 | fx_converted |
| 6160.HK | BeOne Medicines AG | borderline | 42 | 0.92 | fx_converted |

### Building Products & Equipment(4社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| AAON | AAON, Inc. | pass | 50 | 0.51 |  |
| SWIM | Latham Group, Inc. | pass | 38 | 0.64 |  |
| 603992.SS | Xiamen Solex High-tech Industries  | pass | 38 | 0.66 | thin_coverage |
| 7943.T | Nichiha Corporation | borderline | 23 | 0.56 | thin_coverage |

### Capital Markets(2社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| PWP | Perella Weinberg Partners | pass | 40 | 0.28 |  |
| LPLA | LPL Financial Holdings Inc. | borderline | 23 | 0.52 |  |

### Communication Equipment(9社)

理由: 光ファイバー・通信機器。中国の調達価格入札で利益率が循環

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 1300.HK | Trigiant Group Limited | pass | 168 | 0.02 | pe_suspect;fx_converted;thin_coverage |
| 6869.HK | Yangtze Optical Fibre And Cable Jo | pass | 43 | 0.22 | trailing_jump;fx_converted |
| 600105.SS | Jiangsu Etern Company Limited | pass | 73 | 0.28 | thin_coverage |
| 600487.SS | Hengtong Optic-Electric Co., Ltd. | pass | 33 | 0.47 | thin_coverage |
| 601869.SS | Yangtze Optical Fibre And Cable Jo | pass | 34 | 0.73 | trailing_jump;thin_coverage |
| HPE | Hewlett Packard Enterprise Company | borderline | 23 | 0.58 |  |
| FEIM | Frequency Electronics, Inc. | borderline | 56 | 0.76 | thin_coverage |
| 600498.SS | Fiberhome Telecommunication Techno | borderline | 27 | 0.78 | thin_coverage |
| CIEN | Ciena Corporation | borderline | 44 | 0.91 |  |

### Computer Hardware(5社)

理由: PC・メモリ・ストレージ機器。市況品

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 3396.HK | Legend Holdings Corporation | pass | 75 | 0.06 | fx_converted |
| 0992.HK | Lenovo Group Limited | pass | 50 | 0.22 | fx_converted |
| 6810.HK | Shanghai Sunmi Technology Co., Ltd | pass | 112 | 0.44 | fx_converted;thin_coverage |
| SNDK | Sandisk Corporation | borderline | 24 | 0.24 |  |
| P | Everpure, Inc. | borderline | 46 | 0.82 |  |

### Consulting Services(1社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 2170.T | Link and Motivation Inc. | borderline | 29 | 0.56 | thin_coverage |

### Consumer Electronics(6社)

理由: ODM・家電。受託で価格決定力が弱い

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 9611.HK | Shanghai Longcheer Technology Co., | pass | 49 | 0.20 | thin_coverage |
| 600590.SS | Tellhow Sci-Tech Co., Ltd. | pass | 51 | 0.28 | thin_coverage |
| 603341.SS | Shanghai Longcheer Technology Co., | pass | 42 | 0.49 | thin_coverage |
| 688696.SS | XGIMI Technology Co.,Ltd. | pass | 42 | 0.50 |  |
| 1747.HK | Home Control International Limited | pass | 34 | 0.71 | thin_coverage;micro |
| 6752.T | Panasonic Holdings Corporation | borderline | 24 | 0.72 |  |

### Credit Services(3社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| ATLC | Atlanticus Holdings Corporation | pass | 39 | 0.20 |  |
| UPST | Upstart Holdings, Inc. | pass | 38 | 0.21 |  |
| SOFI | SoFi Technologies, Inc. | pass | 39 | 0.52 |  |

### Diagnostics & Research(3社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 3347.HK | Hangzhou Tigermed Consulting Co.,  | pass | 75 | 0.52 | fx_converted |
| 9860.HK | Adicon Holdings Limited | pass | 52 | 0.55 | fx_converted;thin_coverage |
| 2268.HK | WuXi XDC Cayman Inc. | borderline | 36 | 0.95 | fx_converted |

### Drug Manufacturers - General(1社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| GRFS | Grifols, S.A. | borderline | 24 | 0.24 | thin_coverage |

### Drug Manufacturers - Specialty & Generic(6社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 6185.HK | CanSino Biologics Inc. | pass | 193 | 0.13 | fx_converted;thin_coverage |
| 603520.SS | Zhejiang Starry Pharmaceutical Co. | pass | 110 | 0.16 | thin_coverage |
| 600129.SS | Chongqing Taiji Industry(Group) Co | pass | 86 | 0.22 | thin_coverage |
| ETON | Eton Pharmaceuticals, Inc. | pass | 82 | 0.30 | thin_coverage |
| TEVA | Teva Pharmaceutical Industries Lim | pass | 46 | 0.34 |  |
| IRWD | Ironwood Pharmaceuticals, Inc. | borderline | 24 | 0.11 | trailing_jump;pe_suspect |

### Education & Training Services(1社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| APEI | American Public Education, Inc. | borderline | 24 | 0.60 | thin_coverage |

### Electrical Equipment & Parts(16社)

理由: 電池・電線・電源。原材料連動の価格で価格決定力が弱い

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 3931.HK | CALB Group Co., Ltd. | pass | 59 | 0.11 | fx_converted |
| 6656.HK | Sigenergy Technology Co., Ltd | pass | 37 | 0.19 | fx_converted |
| FOIL | Londian Wason New Energy Tech Inc. | pass | 76 | 0.24 | thin_coverage |
| 600522.SS | Jiangsu Zhongtian Technology Co.,  | pass | 34 | 0.33 |  |
| ELVA | Electrovaya Inc. | pass | 85 | 0.35 | micro |
| 688772.SS | Zhuhai CosMX Battery Co., Ltd. | pass | 57 | 0.38 |  |
| FPS | Forgent Power Solutions, Inc. | pass | 50 | 0.39 |  |
| 605196.SS | Hebei Huatong Wires and Cables Gro | pass | 50 | 0.44 | thin_coverage |
| 600379.SS | Shaanxi Baoguang Vacuum Electric D | pass | 62 | 0.57 | thin_coverage |
| 688800.SS | Suzhou Recodeal Interconnect Syste | pass | 41 | 0.64 |  |
| 688676.SS | Hainan Jinpan Smart Technology Co. | pass | 38 | 0.66 | thin_coverage |
| 1729.HK | Time Interconnect Technology Limit | borderline | 29 | 0.45 |  |
| 601222.SS | Jiangsu Linyang Energy Co., Ltd. | borderline | 27 | 0.49 | thin_coverage |
| 605117.SS | Ningbo Deye Technology Group Co.,  | borderline | 26 | 0.53 |  |
| 5801.T | Furukawa Electric Co., Ltd. | borderline | 27 | 0.67 |  |
| NVT | nVent Electric plc | borderline | 31 | 0.79 |  |

### Electronic Components(30社)

理由: 受託製造・基板・部品は価格決定力と顧客集中で条件11・12が B 以下(構造平均 3.5 未満の見込み)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 2476.HK | Victory Giant Technology (HuiZhou) | pass | 74 | 0.14 | thin_coverage |
| 1989.HK | Delton Technology (Guangzhou) Inc. | pass | 64 | 0.16 | thin_coverage |
| 1888.HK | Kingboard Laminates Holdings Limit | pass | 60 | 0.18 |  |
| 1688.HK | Lingyi iTech (Guangdong) Company | pass | 45 | 0.19 | thin_coverage |
| 6997.T | Nippon Chemi-Con Corporation | pass | 37 | 0.24 |  |
| TTMI | TTM Technologies, Inc. | pass | 63 | 0.25 |  |
| CLS | Celestica Inc. | pass | 73 | 0.28 |  |
| 6088.HK | FIT Hon Teng Limited | pass | 37 | 0.33 | fx_converted |
| FLEX | Flex Ltd. | pass | 46 | 0.33 |  |
| 6613.HK | Lens Technology Co., Ltd. | pass | 41 | 0.34 | fx_converted |
| 1377.HK | Guangdong Dtech Technology Co., Lt | pass | 84 | 0.36 | fx_converted;thin_coverage |
| 600183.SS | Shengyi Technology Co.,Ltd. | pass | 83 | 0.39 |  |
| 688551.SS | Hefei Kewell Power System Co.,Ltd. | pass | 73 | 0.40 | thin_coverage |
| 6779.T | Nihon Dempa Kogyo Co., Ltd. | pass | 35 | 0.48 |  |
| MZH.SI | Nanofilm Technologies Internationa | pass | 46 | 0.53 |  |
| 688183.SS | Shengyi Electronics Co., Ltd. | pass | 44 | 0.55 | thin_coverage |
| 688582.SS | Anhui XDLK Microsystem Corporation | pass | 42 | 0.69 | thin_coverage |
| 0710.HK | BOE Varitronix Limited | borderline | 23 | 0.25 | thin_coverage |
| 2475.HK | Luxshare Precision Industry Co., L | borderline | 31 | 0.40 | fx_converted |
| JBL | Jabil Inc. | borderline | 25 | 0.57 |  |
| DAKT | Daktronics, Inc. | borderline | 23 | 0.58 | thin_coverage |
| 603312.SS | Suzhou West Deane New Power Electr | borderline | 24 | 0.65 | thin_coverage |
| 688182.SS | Jiangsu Cai Qin Technology Co., Lt | borderline | 59 | 0.78 | thin_coverage |
| HANA.BK | Hana Microelectronics Public Compa | borderline | 40 | 0.87 |  |
| 688686.SS | OPT Machine Vision Tech Co., Ltd. | borderline | 47 | 0.88 | thin_coverage |
| 688610.SS | Hefei I-TEK OptoElectronics Co., L | borderline | 46 | 0.88 | thin_coverage |
| VICR | Vicor Corporation | borderline | 43 | 0.91 |  |
| 5317.KL | CPE Technology Berhad | borderline | 27 | 0.93 | thin_coverage;micro |
| 688181.SS | Beijing Bayi Space LCD Technology  | borderline | 31 | 0.97 | thin_coverage |
| 6981.T | Murata Manufacturing Co., Ltd. | borderline | 28 | 0.97 |  |

### Electronic Gaming & Multimedia(1社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 0777.HK | NetDragon Websoft Holdings Limited | pass | 62 | 0.12 | fx_converted;thin_coverage |

### Entertainment(1社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 600977.SS | China Film Industry Group Co., Ltd | pass | 107 | 0.59 |  |

### Footwear & Accessories(1社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| DBI | Designer Brands Inc. | pass | 38 | 0.27 | thin_coverage |

### Furnishings, Fixtures & Appliances(3社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| LOVE | The Lovesac Company | pass | 58 | 0.16 | thin_coverage;micro |
| 603268.SS | Guangdong Songfa Ceramics Co.,Ltd. | pass | 75 | 0.20 |  |
| 603600.SS | UE Furniture Co., Ltd. | borderline | 26 | 0.36 | thin_coverage |

### Gambling(2社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| CDRO | Codere Online Luxembourg, S.A. | pass | 70 | 0.28 | trailing_jump;thin_coverage |
| RSI | Rush Street Interactive, Inc. | pass | 35 | 0.69 |  |

### Health Information Services(1社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| NRC | NRC Health | pass | 45 | 0.66 | thin_coverage |

### Healthcare Plans(1社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| ALHC | Alignment Healthcare, Inc. | pass | 42 | 0.35 |  |

### Home Improvement Retail(1社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| HVT | Haverty Furniture Companies, Inc. | pass | 49 | 0.28 | thin_coverage |

### Household & Personal Products(1社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 2657.HK | Shanghai Forest Cabin Cosmetics Gr | borderline | 29 | 0.30 | fx_converted |

### Information Technology Services(7社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 3778.T | SAKURA Internet Inc. | pass | 117 | 0.22 | trailing_jump |
| 688631.SS | Nanjing LES Information Technology | pass | 57 | 0.35 | thin_coverage |
| KD | Kyndryl Holdings, Inc. | borderline | 31 | 0.20 |  |
| 4819.T | Digital Garage, Inc. | borderline | 29 | 0.76 |  |
| 4413.T | baudroie,inc. | borderline | 32 | 0.78 | thin_coverage |
| 0265.KL | Infomina Berhad | borderline | 24 | 0.91 | micro |
| 688768.SS | Anhui Ronds Science & Technology I | borderline | 30 | 1.00 | thin_coverage |

### Infrastructure Operations(1社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 600020.SS | Henan Zhongyuan Expressway Company | borderline | 23 | 0.39 | thin_coverage |

### Internet Content & Information(4社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| ZG | Zillow Group, Inc. | pass | 31 | 0.39 |  |
| 1357.HK | Meitu, Inc. | borderline | 27 | 0.34 | fx_converted |
| Z | Zillow Group, Inc. | borderline | 25 | 0.49 |  |
| 9626.HK | Bilibili Inc. | borderline | 23 | 0.53 | fx_converted |

### Internet Retail(8社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| BZUN | Baozun Inc. | pass | 65 | 0.08 | fx_converted;micro |
| RERE | ATRenew Inc. | pass | 36 | 0.22 | fx_converted |
| 7618.HK | JINGDONG Industrials, Inc. | pass | 36 | 0.43 | fx_converted |
| JD | JD.com, Inc. | borderline | 24 | 0.31 | fx_converted |
| 9618.HK | JD.com, Inc. | borderline | 24 | 0.31 |  |
| 7685.T | BuySell Technologies Co.,Ltd. | borderline | 28 | 0.52 |  |
| CART | Maplebear Inc. | borderline | 26 | 0.73 |  |
| GLBE | Global-E Online Ltd. | borderline | 26 | 0.85 |  |

### Leisure(4社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| JAKK | JAKKS Pacific, Inc. | pass | 42 | 0.26 | thin_coverage |
| 9166.T | GENDA Inc. | pass | 45 | 0.32 | thin_coverage |
| 0325.HK | Bloks Group Limited | borderline | 26 | 0.57 | fx_converted |
| AS | Amer Sports, Inc. | borderline | 24 | 0.84 |  |

### Medical Care Facilities(3社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| THG.BK | Thonburi Healthcare Group Public C | pass | 86 | 0.40 | thin_coverage |
| 1951.HK | Jinxin Fertility Group Limited | borderline | 26 | 0.62 | fx_converted |
| 0303.KL | Alpha IVF Group Berhad | borderline | 24 | 0.73 | thin_coverage |

### Medical Devices(5社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 2041.HK | MEDCAPTAIN | pass | 49 | 0.25 | fx_converted;thin_coverage |
| 2235.HK | MicroTech Medical (Hangzhou) Co.,  | pass | 58 | 0.41 | fx_converted;thin_coverage |
| BWAY | BrainsWay Ltd. | pass | 65 | 0.46 |  |
| 2190.HK | Zylox-Tonbridge Medical Technology | borderline | 28 | 0.47 | fx_converted |
| 688358.SS | Chison Medical Technologies Co., L | borderline | 28 | 0.66 | thin_coverage |

### Medical Instruments & Supplies(1社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 2276.HK | Shanghai Conant Optical Co., Ltd. | borderline | 25 | 0.72 | fx_converted |

### Pollution & Treatment Controls(1社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 6254.T | Nomura Micro Science Co., Ltd. | pass | 32 | 0.30 | thin_coverage |

### Restaurants(4社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 2408.HK | Guangzhou Xiao Noodles Catering Ma | borderline | 31 | 0.34 | fx_converted;thin_coverage |
| HDL | Super Hi International Holding Ltd | borderline | 23 | 0.58 | thin_coverage |
| 1405.HK | DPC Dash Ltd | borderline | 25 | 0.60 | fx_converted |
| 3196.T | HOTLAND HOLDINGS Co., Ltd. | borderline | 52 | 0.87 | thin_coverage;micro |

### Scientific & Technical Instruments(3社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| MKSI | MKS Inc. | pass | 33 | 0.43 |  |
| VPG | Vishay Precision Group, Inc. | pass | 91 | 0.57 |  |
| 688531.SS | Unicomp Technology Group Co., Ltd. | borderline | 49 | 0.93 | thin_coverage |

### Security & Protection Services(1社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| CXW | CoreCivic, Inc. | pass | 44 | 0.34 |  |

### Semiconductor Equipment & Materials(17社)

理由: 装置・材料の中小は設備投資サイクルの山で EPS を測っている。条件(循環)と規模で 4.0 は困難

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| ASYS | Amtech Systems, Inc. | pass | 205 | 0.08 | trailing_jump;thin_coverage;micro |
| 2149.HK | BaTeLab Co., Ltd. | pass | 32 | 0.24 | thin_coverage;micro |
| KLIC | Kulicke and Soffa Industries, Inc. | pass | 53 | 0.32 | trailing_jump |
| 6266.T | Tazmo Co., Ltd. | pass | 35 | 0.36 | thin_coverage |
| 6627.T | Tera Probe, Inc. | pass | 33 | 0.39 | thin_coverage |
| VECO | Veeco Instruments Inc. | pass | 48 | 0.42 |  |
| 6590.T | Shibaura Mechatronics Corporation | pass | 32 | 0.42 |  |
| 688729.SS | Beijing E-Town Semiconductor Techn | pass | 76 | 0.46 | thin_coverage |
| ONTO | Onto Innovation Inc. | pass | 44 | 0.53 |  |
| 605111.SS | Wuxi NCE Power Co.,Ltd. | pass | 45 | 0.58 | thin_coverage |
| 688233.SS | Thinkon Semiconductor Jinzhou Corp | pass | 66 | 0.62 | thin_coverage |
| 6315.T | TOWA Corporation | borderline | 29 | 0.57 |  |
| 603806.SS | Hangzhou First Applied Material Co | borderline | 26 | 0.63 | thin_coverage |
| 688720.SS | Jiangsu Aisen Semiconductor Materi | borderline | 61 | 0.77 | thin_coverage |
| 3277.HK | Gpixel Changchun Microelectronics  | borderline | 35 | 0.81 | fx_converted;thin_coverage |
| 688630.SS | Circuit Fabology Microelectronics  | borderline | 60 | 0.91 | thin_coverage |
| 0522.HK | ASMPT Limited | borderline | 29 | 0.91 | trailing_jump |

### Semiconductors(22社)

理由: アナログ・パワー・メモリ・中国の中小設計は景気循環または国内政策依存。顧客集中・薄いカバレッジ

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| HIMX | Himax Technologies, Inc. | pass | 127 | 0.11 | thin_coverage |
| 688525.SS | BIWIN Storage Technology Co., Ltd. | pass | 35 | 0.12 | thin_coverage |
| 688825.SS | CXMT Corporation | pass | 55 | 0.19 |  |
| DIOD | Diodes Incorporated | pass | 81 | 0.23 |  |
| STM | STMicroelectronics N.V. | pass | 89 | 0.27 |  |
| ASX | ASE Technology Holding Co., Ltd. | pass | 74 | 0.33 | thin_coverage |
| SMTC | Semtech Corporation | pass | 83 | 0.34 |  |
| 688372.SS | Shanghai V-Test Semiconductor Tech | pass | 61 | 0.35 | thin_coverage |
| SIMO | Silicon Motion Technology Corporat | pass | 43 | 0.38 |  |
| 688249.SS | Nexchip Semiconductor Corporation | pass | 82 | 0.41 | trailing_jump;thin_coverage |
| 688608.SS | Bestechnic (Shanghai) Co., Ltd. | pass | 52 | 0.41 | thin_coverage |
| ON | ON Semiconductor Corporation | pass | 39 | 0.48 |  |
| 5005.KL | Unisem (M) Berhad | pass | 78 | 0.52 |  |
| ALGM | Allegro MicroSystems, Inc. | pass | 45 | 0.58 |  |
| 688270.SS | Great Microwave Technology Co., Lt | pass | 71 | 0.63 | thin_coverage |
| SKHY | SK hynix Inc. | borderline | 29 | 0.16 |  |
| MCHP | Microchip Technology Incorporated | borderline | 26 | 0.71 |  |
| 688099.SS | Amlogic (Shanghai) Co.,Ltd. | borderline | 27 | 0.81 |  |
| 600460.SS | Hangzhou Silan Microelectronics Co | borderline | 39 | 0.84 |  |
| GFS | GLOBALFOUNDRIES Inc. | borderline | 24 | 0.86 |  |
| 600584.SS | JCET Group Co., Ltd. | borderline | 41 | 0.89 |  |
| ADI | Analog Devices, Inc. | borderline | 28 | 0.96 |  |

### Software - Application(12社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| RMNI | Rimini Street, Inc. | pass | 37 | 0.26 | thin_coverage |
| 2556.HK | Marketingforce Management Ltd | pass | 56 | 0.40 | fx_converted |
| 3738.HK | Vobile Group Limited | pass | 41 | 0.46 | fx_converted;thin_coverage |
| 0596.HK | Inspur Digital Enterprise Technolo | borderline | 29 | 0.18 | thin_coverage;micro |
| VERX | Vertex, Inc. | borderline | 24 | 0.59 |  |
| DSP | Viant Technology Inc. | borderline | 31 | 0.60 |  |
| DCBO | Docebo Inc. | borderline | 23 | 0.67 |  |
| GRND | Grindr Inc. | borderline | 28 | 0.71 | thin_coverage |
| KVYO | Klaviyo, Inc. | borderline | 25 | 0.73 |  |
| YOU | Clear Secure, Inc. | borderline | 24 | 0.79 |  |
| 688692.SS | Wuhan Dameng Database Company Limi | borderline | 28 | 0.90 | thin_coverage |
| 600845.SS | Shanghai Baosight Software Co.,Ltd | borderline | 28 | 0.92 | thin_coverage |

### Software - Infrastructure(7社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 6682.HK | Phancy Group Co., Ltd. | pass | 96 | 0.49 | trailing_jump;fx_converted;thin_coverage |
| 2586.HK | Dmall Inc. | pass | 44 | 0.50 | fx_converted;thin_coverage |
| MQ | Marqeta, Inc. | pass | 85 | 0.57 | thin_coverage |
| FLYW | Flywire Corporation | borderline | 27 | 0.57 |  |
| XYZ | Block, Inc. | borderline | 29 | 0.59 |  |
| CALX | Calix, Inc. | borderline | 31 | 0.59 |  |
| NYAX | Nayax Ltd. | borderline | 50 | 0.75 | thin_coverage |

### Specialty Business Services(2社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 605108.SS | Tongqinglou Catering Co., Ltd. | borderline | 28 | 0.65 | thin_coverage |
| ARMK | Aramark | borderline | 24 | 0.93 |  |

### Specialty Industrial Machinery(19社)

理由: 風力・電池・レーザー装置など。受注産業で循環が強く、中国勢は価格競争

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 688349.SS | Sany Renewable Energy Co.,Ltd. | pass | 133 | 0.09 | thin_coverage |
| 688411.SS | Beijing HyperStrong Technology Co. | pass | 74 | 0.12 |  |
| HQU.SI | Oiltek International Limited | pass | 106 | 0.16 |  |
| 3200.HK | Shenzhen Han's CNC Technology Co., | pass | 59 | 0.19 | fx_converted;thin_coverage |
| 2208.HK | Goldwind Science&Technology Co., L | pass | 33 | 0.20 | fx_converted |
| 601615.SS | Ming Yang Smart Energy Group Limit | pass | 70 | 0.24 | thin_coverage |
| 0470.HK | Wuxi Lead Intelligent Equipment CO | pass | 33 | 0.33 | fx_converted |
| 6235.T | Optorun Co.,Ltd. | pass | 39 | 0.38 | thin_coverage |
| 688518.SS | Shenzhen United Winners Laser Co., | pass | 33 | 0.41 |  |
| 605060.SS | Allied Machinery Co., Ltd. | pass | 41 | 0.45 | thin_coverage |
| 605555.SS | Ningbo Dechang Electrical Machiner | pass | 45 | 0.46 | thin_coverage |
| 600482.SS | China Shipbuilding Industry Group  | pass | 41 | 0.50 | thin_coverage |
| GNRC | Generac Holdings Inc. | pass | 34 | 0.51 |  |
| 688006.SS | Zhejiang HangKe Technology Incorpo | pass | 33 | 0.56 |  |
| 6104.T | Shibaura Machine Co.,Ltd. | pass | 50 | 0.59 | thin_coverage |
| 603218.SS | Riyue Heavy Industry Co.,Ltd | borderline | 27 | 0.42 |  |
| 688169.SS | Beijing Roborock Technology Co., L | borderline | 27 | 0.45 |  |
| 0208.KL | Greatech Technology Berhad | borderline | 41 | 0.78 |  |
| 688392.SS | SBT Ultrasonic Technology Co., Ltd | borderline | 52 | 0.81 | thin_coverage |

### Specialty Retail(2社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 603214.SS | Shanghai Aiyingshi Co.,Ltd | borderline | 23 | 0.55 | thin_coverage;micro |
| HZO | MarineMax, Inc. | borderline | 61 | 0.76 |  |

### Staffing & Employment Services(2社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 4377.T | ONE CAREER Inc. | pass | 43 | 0.40 | thin_coverage |
| MAN | ManpowerGroup Inc. | borderline | 25 | 0.40 |  |

### Telecom Services(3社)

理由: 事業内容から、価格決定力・継続性・循環のいずれかで構造4.0に届かないと判断(個別の補足は下表)

| ticker | 名称 | 判定 | g(%) | PEG | フラグ |
|---|---|---|---:|---:|---|
| 1310.HK | HKBN Ltd. | pass | 38 | 0.33 | thin_coverage |
| 6888.KL | Axiata Group Berhad | pass | 45 | 0.37 |  |
| TIGO | Millicom International Cellular S. | pass | 35 | 0.40 |  |
## 個別の補足(名の知れた銘柄)

| ticker | 除外の決め手 |
|---|---|
| SOFI / UPST / ATLC | 与信を抱える。景気後退での貸倒れが EPS を直撃(条件 循環・資本)。SoFi は前回分析でも構造B |
| XYZ(Block)/ TOAST 以外の決済 MQ・FLYW・NYAX | 一次判定は境界。テイクレート低下の圧力と、Marqeta は顧客集中(Block)で条件11が B 以下 |
| ZG / Z(Zillow) | 不動産取引量に連動する循環。成長は市況の戻り |
| SAKURA Internet | GPU クラウドで設備負担が重く、政府案件の集中。trailing_jump |
| TEVA / IRWD / GRFS | 後発品・特許満了と負債。成長は一時的な利益改善 |
| ALHC | 医療保険(メディケア・アドバンテージ)で規制と医療費率の循環 |
| CXW | 刑務所運営。政策依存 |
| KD(Kyndryl) | 低成長の IT 保守。成長は費用削減由来 |
| CLS / FLEX / JBL | EMS(受託製造)。価格決定力が弱い |
| ON / STM / DIOD / ALGM / MCHP / ADI | アナログ・パワーの在庫循環の戻り局面。来期の伸びは底からの回復 |
| SKHY / SNDK / CXMT / SIMO / BIWIN | メモリ。市況品 |
| HIMX | ディスプレイ駆動 IC。顧客集中と循環。カバレッジ1人 |
| Lenovo / Legend | PC。市況品、Legend は持株会社 |
| AAON / GNRC / VRT 以外の DC 設備 | 空調・発電機は建設・停電需要の循環。AAON は DC 向けで伸びるが受注型 |
| Alibaba 以外の中国ネット(JD・Bilibili・Meitu) | 成長22〜27%で成長A+の 31%に届かない |
| SE / CART / GLBE / RDDT / HUBS | 境界(成長22〜31%)。うち SE・RDDT・HUBS は C班で確認、GLBE は 81_review で不通過済み |
