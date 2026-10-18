# 22 需給モデル入力データ(調査担当 / 2026-10-18)

対象クラックス: 「AI基板材料の不足は一過性か構造的か」
前提: 検索ツールは要約を返すのみで原文(PDF・有料記事)は開けていない。出典の多くは二次情報(証券レポートの転載、Substack、台湾・中国メディア、業界ブログ)。数値は必ず一次資料(日東紡・三井金属のIR、MS/GS/JPM/Counterpoint/Prismarkの原本)で再確認すること。【推定】は本調査担当の推定、【未確認】は一次未確認または出典間で矛盾。
不足率の定義: 原則「(需要-供給)/需要」。ただし各社の定義は不明で、MSの「40%」などはこの定義とは限らない。

---

## 0. Opusへの重要な訂正・注意(先に読むこと)

1. **MicroThinの「月60万m²超へ3倍」は誤りの可能性が高い。** 三井金属の公式文書では現状(2026年度)約490万m²/月 → 2027年度520万 → 2029年度560万(2026/3文書)。2026/8/17の新計画で2028年度中に600万、2030年度800万(300億円追加)、マレーシア新拠点で2031年以降+400万(合計1,200万)。2026年度比では2028年度で約1.2倍、2030年度で約1.6倍。「3倍」にはならない。60万は600万の桁違いの可能性がある。
   - 出典: https://news.mynavi.jp/techplus/article/20260818-4835085/ / https://www.mitsui-kinzoku.com/LinkClick.aspx?fileticket=Dm4ukdv8ZQw%3D&TabModule950=0 (2026-08-17リリース) / https://www.mitsui-kinzoku.com/LinkClick.aspx?fileticket=3KwIJEhN0bs%3D&tabid=100&mid=826 (2025-01-07リリース)
2. **「ガラスクロス価格+18%/月(2026/8)」はE-glass汎用クロス(7628等)の話で、T-glassではない。** AtlasPCB(業界ブログ、一次不明)は7628が$0.60/m(2025Q3)→$1.47/m(2026/8)、8月は+17〜18%、7月+16%。Citi引用の「累計118〜165%」は確認できず(同ブログは累計約140%)。日東紡は「T-glassの追加値上げ予定なし」(TrendForce 2026-08-06)。台湾メディアは「汎用E-glassと高階T-glassを混同している」と指摘(後述C)。T-glassの価格は上がり止まり、汎用は暴騰という二層構造。
   - https://atlaspcb.com/news/news-electronic-glass-cloth-price-surge-140-percent-ai-demand-2026/ / https://www.trendforce.com/news/2026/08/06/news-nittobo-raises-fy2027-net-profit-forecast-by-jpy-3b-no-further-t-glass-price-hikes-planned/
3. **HVLP4の「2026年1,500t→2027年2,500t不足」と「MS 2027年31%不足」は整合しない。** MS需要が2026年12,300t→2027年39,200tなら、31%不足は約12,000t。2,500tは約6%。出典違い(Digitimes/SMM経由とMS/36Kr経由)か、定義違い。どちらか(または両方)が誤りの可能性。MS原本の確認が必要。
   - https://news.metal.com/newscontent/104142677-ai-server-boom-strains-copper-foil-supply-projected-gap-widens-to-2500-tonnes-by-2027 / https://eu.36kr.com/en/p/3984081016470532
4. **日東紡の能力倍率は報道間で不一致。** 「2029/3期に2026/3期比3倍」(日経→TrendForce)と「2027年度に2倍」(Postation)が併存。福島新棟(約150億円、全部Tガラスなら最大3倍相当)の稼働は2027年1-3月(日経)。設備投資は800億→1,200億円(中計)、2026/8時点の今期設備投資見通し450億円(前期の2.1倍)。次の投資候補は「ガラス糸(溶融・紡糸)」と経営陣が発言=現状はクロス側増強が先行しており、糸が次の制約になりうる。
   - https://www.nikkei.com/article/DGXZQOCC021TM0S5A900C2000000/ / https://www.postation.jp/news/nittobo-t-glass-capacity-doubling-no-more-price-hike
5. 日経の見出し「Tガラスの増産なし」は後続のPostation記事が「会社が否定したのは増産ではなく追加の値上げ」と訂正している(5/12説明会)。株価急落の理由の読み違いに注意。
6. 三井金属の来期(2027/3期)は営業益減益計画(910億→940億円に上方修正しても前期比-28%)。要因は前期の在庫評価益の剥落(Kabutan)で、AI銅箔の失速ではない。

---

## A. 需要側

### A-1. 出荷・能力(年次)
| 項目 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 出典・備考 |
|---|---|---|---|---|---|---|---|
| AIサーバー出荷成長率 | - | - | +28%(1月予想)→約+31%(8月上方修正) | 「未充足需要が27年に繰越」 | 未入手 | 未入手 | TrendForce https://www.trendforce.com/presscenter/news/20260120-12887.html (2026-01-20) ほか |
| GPU/ASIC構成比 | - | - | GPU 69.7%/ASIC 27.8%(後に27%へ修正) | TPU急増、Meta自社ASIC加速 | 未入手 | 未入手 | 同上。台数(絶対値)は有料で未入手 |
| TSMC CoWoS能力(末、k wpm) | 未入手 | 未入手 | 115(JPM 2026/1)/120-130(MS 2025/12)/130(EDN 2026/9) | 112(JPM旧 2025/9)/170(KGI 2026/3) | 260(EDN 2026/9) | 未入手 | 範囲が大きい。OSAT合計は2026年に約200k(EDN 2026/6)。TrendForceは27年に+60%超 |
| ABF需給ギャップ | - | - | 約8-10% | 約20%(Counterpoint) / MS 9.3%(6.2%から上方修正) / 22%(別報) | 29%(BigGo報道、出典不明) | 2030に22%(TVBS報道) | 定義が各社不統一。JPM: ABF稼働率27年に100%超(需要+約40%/年 vs 供給+約10%) |
| AI関連ハイパースケーラーCapex | - | - | 約6,100億ドル(4社、前年比約+70%)※出典不明確 | 約1.08兆ドル(Vanguard)/MS: +29% | 1.19兆ドル(Vanguard) | 1.15兆ドル(Vanguard) | Wells Fargo「27年ピークを織り込み始める」、BofA「FCFは2028年までマイナス」 |

- CoWoS: https://www.trendforce.com/news/2026/09/14/news-tsmc-reportedly-targets-22-2nm-16-3nm-capacity-boost-by-mid-2027-cowos-to-double-by-2028/ / https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/tsmc_2330-tt_09032026e.pdf (KGI 2026-03)
- ABF: https://404kresearch.substack.com/p/abf-substrate-utilization-to-breach (JPM二次) / https://counterpointresearch.com/en/reports/From-T-Glass-Crisis-Capacity-Erosion-The-Multi-Year-Substrate-Shortage (2026-03-11) / https://finance.biggo.com/news/4978b0ef-fc31-4d7d-9de1-c14abbafc97b
- Capex: https://corporate.vanguard.com/etc.clientlibs/corporatesite/clientlibs/clientlib-site/resources/dwcharts/2dC6s.htm / https://seekingalpha.com/news/4629570-cloud-capex-forecast-calls-for-29-jump-in-2027-as-compute-demand-exceeds-capacity-ms / https://www.tftc.io/ai-capex-cash-flow-negative-2027-peak-hyperscalers
- 2024・2025年のCoWoS実績、GPU/ASICの絶対台数、2028-29年のサーバー出荷は無料の出典では見つからなかった(未入手)。

### A-2. 世代別の基板材料グレード
| 世代/製品 | 基板・層数 | CCLグレード | ガラスクロス | 銅箔 | 出典(信頼度) |
|---|---|---|---|---|---|
| Hopper(HGX) | 今回の検索では確認できず | 未確認(一般にM6帯との認識だが出典なし) | - | - | 未入手 |
| Blackwell GB200 | 計算トレイ22層HDI(ビルドアップ18層M8+コア4層M4) | M8(+M4) | Low-Dk2(NER) | HVLP2-3帯 | globaltechresearch https://globaltechresearch.substack.com/p/nvidia-nvda-us-gb300-vera-rubin-and (中) |
| Blackwell GB300 | 低位版16層HDI(12層M8+4層M4) | M8 | 同上 | 同上 | 同上 |
| GB200/GB300(別説) | 20-22層、6〜8次HDI | M7/M8 | NE→NER | - | 36Kr https://eu.36kr.com/en/p/3906205135247240 (中) |
| Rubin(VR200) 計算ボード | 26層(GB300の22層から) | M8〜M8.5(M9計画から格下げ報道あり) | Low-Dk2中心 | HVLP2→HVLP4(SemiAnalysis) | Jukan(X) https://x.com/jukan05/status/2009473414101156029 (低) / SemiAnalysis https://newsletter.semianalysis.com/p/vera-rubin-extreme-co-design-an-evolution (中) |
| Rubin Bianca/NVSwitch | Bianca 24層(6+12+6)M8+高級銅箔、NVSwitch 32層M9見込み | M8/M9 | NVSwitchはQ-glass併用説 | HVLP4 | globaltechresearch https://globaltechresearch.substack.com/p/nvidia-nvda-us-vr200-nvl144-cpx-an (低-中) |
| Rubin ミッドプレーン(新規) | 44層(22+22)、約420×60mm | M9(EM896K3) | **Q-glass** | **HVLP4+** | 郭明錤 https://x.com/mingchikuo/status/2008439734536986852 (中)。最も一致度の高いM9用途 |
| Rubin Ultra/Kyber | ミッドプレーン78層説 | M9+石英クロス | 石英 | - | 単一出典、低信頼。Kyber NVL144の量産は2028へ延期・4チップ版中止の報道(pccentral https://pccentral.net/nvidia-kyber-nvl144-delayed-2028-pcb-bottleneck-rubin-ultra/、低) |
| Google TPU v8 / AWS Trainium3 | 層数は未確認 | M7→M8へ移行(JPM系報道) | Low-Dk | - | itiger https://www.itiger.com/hans/news/1146769564 (低-中) |
| 800G→1.6Tスイッチ | 40層超 | M9+Q-cloth(JPM系) | Q-glass | HVLP4-5 | 同上 |

- Rubin仕様確定時期: GS引用で2026年6-7月(Lighthouse Canton https://www.lighthouse-canton.com/insights/ccls---the-invisible-bottleneck-long-term-investing-thematic)。Rubin材料サンプル提出は2025年9月開始(Meritz引用 https://x.com/jukan05/status/2003053837331104102)=サンプルから仕様確定まで約9〜10ヶ月。
- M8→M9は「低誘電ガラスをQ-glassに替える」が中心で、材料単価はおおむね倍(globaltechresearch)。NVIDIAのBOMに占める比率は1%未満(Jukan)=価格感応度は低い。
- Q-glassは供給量が少なく加工難度が極めて高い。日東紡の次世代品は顧客のDk要求を満たし切れていない(Meritz引用、低-中)。
- Rubinの基板面積は前世代比約75%大、18層(bestpcbs/atlaspcb系、低)。

### A-3. 材料別の需要量推計(t、百万m、m²/月)
- **ガラスクロス(T-glass)の絶対需要量(百万m等)は無料の出典で見つからなかった。** 能力と需要の絶対値を示す公開数値はほぼなく、Counterpoint・MS・Prismarkの有料原本が必要。
- HVLP4銅箔(MS、36Kr経由): 需要12,300t(2026)→39,200t(2027、+218%)。供給は5社で実効約1,000t/月、2026年能力の41%が三井金属。【未確認: 上記注意3の整合性問題】
- GS(Edgen/BigGo経由): HVLP3+市場は2025年約2.16億ドル→2028年約24億ドル、HVLP需要は2025〜28年で6倍超(CAGR 97%)。https://www.edgen.tech/ja/news/post/ai-server-boom-to-create-3-year-copper-foil-shortage-goldman-says / https://finance.biggo.com/news/gKGcRp4B6tLPsnrZ9pcm
- キャリア付き極薄銅箔(mSAP): 世界のmSAPキャリア基板は2024年に約1.2億m²(調査会社要約、低)。MicroThin需要の直接推計は未入手。ABF基板需要(上表)で代用するしかない。【推定】
- 【推定】T-glass需要の伸び: CoWoS能力(TSMC末値)で2026→27 +31%(KGI)、2027→28 +53%(EDN)。これに1パッケージあたり基板面積・層数の増加(+75%等)が乗る。よって素材需要の伸びは2027年+30〜60%、2028年+30〜50%程度と置く(後述D)。

### A-4. 需要を増減させる技術変化
| 技術 | 影響 | 時期 | 出典・信頼度 |
|---|---|---|---|
| CoWoP(基板レス実装) | ABF/BT基板需要を減らす可能性。ただしコストはPCB側に移転 | Digitimes: 次世代GR150(2027)で採用の報道。MS「時期尚早」、Rubin Ultraは見送り濃厚 | https://www.trendforce.com/news/2025/07/30/news-cowop-a-game-changer-beyond-cowos-or-just-hype-pcb-makers-stay-skeptical/ (中、2025-07) / https://money.udn.com/money/amp/story/5607/8907040 |
| ガラスコア基板 | ABFのコア材/ T-glass需要を一部代替。ただし量産は遅い | Intel: 約2030(自社展開)、Absolics: 2027量産目標(再三遅延)、サムスン電機: 2H27初生産、DNP: FY2028、Rapidus: 2028目標。NVIDIAが前倒しを要請との報道あり | https://www.trendforce.com/research/download/RP260224KD / https://tomshardware.com/tech-industry/manufacturing/glass-substrate-roadmap-examined (中)。T-glass需要への影響を定量した出典はなし |
| CPO | スイッチトレイの電気配線長が短くなり、超低損失CCL(M8/M9)需要が減る | 102.4Tスイッチ(Broadcom Davisson、2025/10発表)。台燿を分析した記事は「圧力は2028年以降」 | https://www.moneyweekly.com.tw/_Article?AID=250220 (低-中) |
| 次世代T-glass | CTE 2.8→2.0ppm。再び単一供給源化する可能性(需要側の格上げ) | 日東紡: 2028年実用化 | https://www.trendforce.com/news/2026/02/04/news-nittobo-reportedly-plans-2028-next-gen-t-glass-customers-may-include-nvidia-apple-and-others/ (中) |
| Rubin仕様の格下げ(M9→M8/M8.5) | 弱気側。高級グレード需要の一部が先送り | 2026/1報道(Jukan)。ミッドプレーンのM9は維持との報道が多い | 低 |

---

## B. 供給側

### B-1. 各社の能力と増強計画
| 企業 | 品目 | 現状・計画 | 稼働時期 | 出典(信頼度) |
|---|---|---|---|---|
| 日東紡 | T-glass(世界シェア約90%)、NE/NER(60-70%) | 福島新棟(約150億円)で最大3倍、全体で2029/3期に2026/3期比3倍(日経)。台湾(福隆玻璃)で糸の溶融炉増設、嘉義でT-glass量産開始。設備投資は中計で1,200億円に増額 | 福島: 竣工2026/12、稼働2027年1-3月。満負荷の実効能力は2027下半期〜2028上半期(TechNews) | Nikkei https://www.nikkei.com/article/DGXZQOCC021TM0S5A900C2000000/ ほか(中-高)。TrendForce 2026/8/6 |
| 南亜(Nan Ya) | 日東紡糸を織る第2供給源 | 2027年までに日東紡の特殊ガラスクロスの20%を織る | 2027 | https://www.trendforce.com/news/2025/11/28/news-nittobo-expands-glass-fiber-output-with-nan-ya/ (中) |
| 台湾玻璃(台玻) | Low-Dk/Low-CTE | 40.2億元超を三期に分けて投資。Low-Dk1ライン4→12本、第1期2026稼働、第2期2026年末、第3期2027完工(約20億元)。高階クロス供給+40-50%(2026) | 2026-2027 | https://tw.stock.yahoo.com/news/ (台玻関連複数)。Low-Dk認証は「主要国際顧客」取得、歩留まり・長期安定性は未実証(中)。NVIDIAでのT-glass認定は確認できず |
| 富喬(FIC) | Low-Dk/E-glass | Low-Dk2比率 3Q40%→4Q50%、先進製程比率70%目標。タイ新工場約31億元は2027年3Q〜下半期量産。E-glassの一部をLow-Dkへ転換(2027〜)。M9向け石英布を認証中 | 2026-27 | https://tw.stock.yahoo.com/news/ (富喬複数) / https://news.cnyes.com/news/id/6508216 (中) |
| 建榮、德宏 | Low-Dk | 建榮は日東紡の子会社関係。德宏の増産詳細は見つからず【未確認】 | - | - |
| 宏和(Honwa) | - | 今回の検索では情報なし【未確認】 | - | - |
| 巨石(China Jushi) | 電子糸・クロス(E〜Low-Dk中心) | 淮安100,000t糸/3.9億m クロス稼働。追加ライン50,000t/3.2億m(4.43億元)は建設約18カ月。桐郷で+2.5億m | 追加分は2027年後半頃【推定】 | https://www.compositesworld.com/news/kingboard-jushi-ramp-up-glass-fiber-output-as-ai-reshapes-pcb-demand (中)。T-glass級ではない |
| 建滔(Kingboard) | 電子糸 | 韶関70,000t/年の糸ライン、クロス1.08億m(2026Q3稼働予定) | 2026Q3 | https://www.jeccomposites.com/news/by-jec/ai-boom-kingboard-group-debuts-70000-tonne-electronic-grade-glass-fibre-yarn-production-line/ (中) |
| 中国勢(泰山、Grace Fabric、紅河/Honghe等) | Low-Dk, Low-CTE | 高階Low-Dk国産化率2024年約20%→2026年40-50%。T-glass・Q-glassの安定量産は未達。紅河がLow-CTE達成を主張(未検証、Appleが検討) | 2027-28に突破の可能性 | https://faxiangongchang.com/en/reports/china-glass-fiber-2026 (低-中) |
| 日本電気硝子(NEG) | Low-Dk(D2 Fiber)、T-glass競合品を開発中 | 認定・量産状況は確認できず | 未確認 | 低 |
| 信越・旭化成 | 石英/低誘電 | 今回の検索では能力情報なし【未確認】 | - | - |
| 菲利華ほか中国石英勢 | 石英(Q)クロス | 量産は2026Q2開始見込み(華泰)。2024年の世界石英繊維織物生産は100t未満(調査会社要約) | 2026Q2〜 | https://www.webull.com/news/13219653530330112 (低) |
| 三井金属 | HVLP(VSP) | 月620t(2025/8、台湾+マレーシア)→840t(2026/9)→1,000t(2027/9)→1,200t(2028/9)。2031年以降マレーシア新拠点+1,200t(合計2,600t、最大5,000t視野)。GSは実効HVLP3+能力を718t/871t/1,140t(2026/27/28月)と推計(歩留まり込み) | 上記 | https://www.logi-today.com/877261 / https://www.logi-today.com/989470 / https://www.bitget.com/news/detail/12560605420411 (中-高) |
| 三井金属 | キャリア付極薄銅箔(MicroThin) | 490万m²/月(2026年度)→520万(2027年度)→560万(2029年度)。2026/8の新計画: 600万(2028年度中)、800万(2030年度、300億円追加)、+400万(マレーシア2031年以降、合計1,200万)。銅箔全体で2030年度までに420億円 | 上記 | https://news.mynavi.jp/techplus/article/20260818-4835085/ (高、公式リリース引用) |
| 古河電工(Circuit Foil等) | HVLP4供給可能とされる | 具体増強は確認できず | - | 低 |
| 金居(Co-Tech) | HVLP3/4 | HVLP3+4で月150t(2026末)、三廠(雲林)が2027Q1投産、HVLP4を4ライン、2027Q4までに追加+600t/月。会社の受注見通しは2028年まで。MS推計はHVLP4月能力<50t(2025)→約200t(2026末)→700t(2027末)→800t(2028末) | 2027Q1-Q4 | https://www.ctee.com.tw/news/20260608701135-430201 (中、会社発言)。数字は出典間で大きく不一致(2026末150〜400t) |
| 德福科技(Defu) | HVLP | 2026/8にHVLP合計500t出荷、うちHVLP4は約70t、HVLP4歩留まり60%超 | 稼働中 | https://eu.36kr.com/en/p/3984081016470532 (低-中) |
| Lotte Energy Materials | 回路箔(全体) | 年産3,700t→16,000t(2027)。同社は営業赤字 | 2027 | https://www.techtimes.com/articles/316643/20260516/lotte-energy-materials-bets-big-ai-substrate-circuit-foil-high-value-strategic-pivot.html (低-中) |
| SK Nexilis | HVLP | 増強情報なし【未確認】 | - | - |
| 中国 HVLP4 | - | 中国本土でHVLP4の量産は未達。突破は2027-28の可能性 | - | https://faxiangongchang.com/en/reports/china-lithium-copper-foil-2026 (低) |

### B-2. 増強リードタイム
| 項目 | 確認できたこと | 信頼度 |
|---|---|---|
| 日東紡 福島新棟(建屋+織機) | 着工(起工式)2025/9〜10 → 竣工2026/12 → 生産開始2027年1-3月で約15〜17ヶ月。ただし満負荷は2027下半期〜2028上半期(着工から約2.5年) | 中(日経) |
| 溶融炉・紡糸 | 炉の建設期間を示す出典は見つからなかった。日東紡は「次の投資候補はガラス糸」と発言=糸が次の制約。台玻の桃園炉が予定通り完成するかが論点との報道あり | 低 |
| 織機(エアジェット) | 「納期2〜3年」を裏づける一次情報は見つからなかった。ブログ(remio.ai)が特殊織機の受注が2029年に及ぶ例を報じる程度。トヨタ織機のJAT910が事実上の標準で、細糸は振動・張力変動で切れやすく代替が難しい | 低 |
| 中国巨石の新ライン | 約18カ月(公式報道) | 中 |
| HVLP表面処理設備 | 日韓の少数メーカー(Mitsune、Nishi Kogyo、PNT等と報道)の年産合計が約20ラインで、業界全体の増設上限になっている | 低-中(二次ブログ) https://www.bitget.com/news/detail/12560605420411 経由) |
| 三井金属 VSP | 設備転用・生産性改善・表面処理機増設(60億円)で2026/9→2028/9に段階増。新拠点は2031年以降(用地取得後)=新規は5年規模 | 高 |
| 金居 三廠 | 2026Q2時点で2027Q1投産予定 | 中 |

### B-3. 認定(クオリフィケーション)
- 新規サプライヤーのT-glass認定に要する月数を示す出典は見つからなかった。**【推定】** Rubinのサンプル提出(2025/9)から仕様確定(2026/6-7)まで約9〜10ヶ月、HVLP4は剥離・反りの工程安定化が必要(SemiAnalysis)。CCL→基板→OEMの三層認定を考えると新規参入は最短でも12〜24ヶ月と見るのが妥当(推定、要検証)。
- 二次ソース状況: 日東紡の糸を使う南亜(2027年に20%)が最短の第2供給。台玻はLow-Dk認証済みだが「T-glassでNVIDIA認定」は確認できず。中国紅河はLow-CTE達成を主張(未検証)。NEGは競合品開発中。つまり**T-glassは2027年時点でも事実上単一供給**(Prismark・TrendForceの指摘と一致)。
- 日東紡T-glassのリードタイム: 8週(2025末)→約20週(三菱ガス化学・レゾナック向け、2026前半)。https://semiconsam.substack.com/p/urgent-check-on-glass-fiber (低-中)

### B-4. 価格の時系列
| 時期 | 品目 | 内容 | 出典(信頼度) |
|---|---|---|---|
| 2025 | 日東紡 電子ガラス繊維 | +20%(報道) | TrendForce系要約(中) |
| 2025Q4 | 日本勢 銅箔 | +5〜10% | 低-中 |
| 2026年 | 日東紡 T-glass | +30%(報道)。8/5説明会で「予定の値上げは概ね完了、追加の予定なし(需給を理由にはしない)」。エネルギーコスト高止まりなら再検討 | https://www.trendforce.com/news/2026/08/06/news-nittobo-raises-fy2027-net-profit-forecast-by-jpy-3b-no-further-t-glass-price-hikes-planned/ (中-高) |
| 2026Q1 | 電解銅箔(汎用) | 約+15%(LME連動+需給) | https://atlaspcb.com/news/news-copper-foil-price-surge-q1-2026-pcb-impact (低-中) |
| 2026/3/13 | 三井金属 MicroThin | 価格交渉開始の通知。+12%はOpus資料の数値で、今回の検索では12%を確認できず【未確認】 | https://www.mitsui-kinzoku.com/LinkClick.aspx?fileticket=MLfP2s%2FfOBQ%3D&tabid=199&mid=826&TabModule950=0 |
| 2026/4/28 | 建滔積層板 | FR-4 CCL・プリプレグ+10%(銅価と糸不足) | bestpcbs等(中) |
| 2026/5 | パナソニック・レゾナック | CCL/PP改定(汎用CCLの方が大きい) | 低-中 |
| 2026/5 | 韓国CCL輸入価格 | 前年比+74.5% | https://www.trendforce.com/news/2026/05/06/news-ai-demand-tightens-ccl-supply-drives-advance-orders-price-hikes-and-expansion/ (中) |
| 2026/7/1 | 台湾Fulltech | E-glassクロス+30%、FLD2クロス+15%(新規受注) | https://www.trendforce.com/news/2026/06/30/news-raw-material-inflation-deepens-as-fulltech-hikes-glass-fiber-cloth-prices-up-to-30-vpec-adjusts-epi-wafers/ (中) |
| 2026/7-8 | 7628汎用クロス | 7月+16%($1.24-1.27/m)、8月+17〜18%($1.47/m) | AtlasPCB(低) |
| 2026/8 | 建滔 CCL | 平均+10%、Citiは年末までさらに+15〜20%を予想 | https://404kresearch.substack.com/p/kingboard-laminates-deep-dive-update-e97 (低-中) |
| 2026/8/28 | 薄物プリプレグ | 7628以下で+20% | bestpcbs(低) |
| 2026年(通年) | 中国ガラスクロス | 5回連続値上げ、2025Q3の底から+100%(謝金河の発言を報じた台湾メディア) | https://www.setn.com/News.aspx?NewsID=1854639 (低-中) |
| 2026 | ABF | 味の素ABFフィルム+30%以上を検討、基板に3〜6%転嫁、2H26基板+5〜10%。Counterpoint: 1H26は前期比+3〜5% | digitalcitizen/Counterpoint(低-中) |
- スポット: T-glassは約$100/kg(中国系要約、出典不明、低)、Low-Dkスポット$37/m(AtlasPCB、低)。信頼できるスポット価格系列は見つからなかった。

---

## C. 市場の見方

### C-1. 「2027〜28年に不足が解消/緩和し価格が崩れる」側(弱気・緩和)
| 見方 | 内容 | 出典 |
|---|---|---|
| 業界推計(TrendForce系要約) | T-glassの需給ギャップは2026年がピークで、日東紡・台湾玻璃(TGI)・Grace Fabricの新能力が出る2027年から緩和 | https://www.trendforce.com/research/download/RP260324EB / https://insights.trendforce.com/p/glass-fiber-cloth-shortage (中)。TrendForce本文は「制約は2027年中頃まで」 |
| MS(2026/9/13、Chaoxiang経由) | 高階ガラスクロス不足は2026年約40%→2027年さらに拡大→2028年約30%に縮小。HVLP4+は2027年31%→2028年20% | https://www.kucoin.com/news/flash/morgan-stanley-supply-shortage-of-high-end-glass-fabric-reaches-40 (中、MS原本未確認) |
| 中国の拡産と価格競争 | 巨石46億元など。謝金河「日本龍頭が倒れた。台湾勢の試練」。ただし反論として、中国の拡産は汎用E-glassが標的でT-glassとは別の戦場、との見解 | https://fnc.ebc.net.tw/fncnews/stock/212751 / https://fnc.ebc.net.tw/fncnews/business/212836 (低-中) |
| 日東紡の方針 | 2029/3期に3倍、追加値上げせず。社長「2030年以降の需要予想は難しい」(日経 2026/9) | https://www.nikkei.com/article/DGXZQOUC101V40Q6A910C2000000/ (中、見出しのみ) |
| Capexのピーク懸念 | Wells Fargo「2027年ピークを市場が織り込み始める」、BofA「FCFが2028年までマイナス」 | https://www.tftc.io/ai-capex-cash-flow-negative-2027-peak-hyperscalers (低-中) |
| 技術代替(2028年以降) | CPO、CoWoP、ガラスコア(Aセクション参照) | 同上 |
| 低価格帯の供給過剰 | 「低位は供給過剰、高位は不足」の二極化(Nuode、中国) | https://www.itiger.com/news/1109026133 (低) |

### C-2. 「構造的に続く」側(強気)
| 見方 | 内容 | 出典 |
|---|---|---|
| Prismark | 日東紡認定供給に限ればT-glass不足は2027年まで続き2028年に向けて拡大(2028年能力シェアは日東紡55%・他45%) | https://x.com/jukan05/status/2038175585768493516 (Xの二次、低-中) |
| Counterpoint(2026/3/11) | T-glassは2026年に10%超不足、2027年は新設能力が間に合わず20%。基板は「multi-year shortage」 | リンクは上記(中、要約のみ) |
| Digitimes | T-glass ギャップは2026年40%超、2027年でも25% | https://www.macrostream.ai/articles/6a2ba2d18f2442d721542919 (低-中) |
| GS | HVLP3+の実効不足は2026年28%/2027年39%/2028年38%。「3年間が新常態」。Co-Tech(金居)を買い推奨 | https://www.bitget.com/news/detail/12560605420411 (中、原本未確認。なお対象はHVLP3+でHVLP4+ではない) |
| JPM | ABF稼働率が2027年に100%超 | 上記 substack(低-中) |
| 台玻会長 | 高階クロスの不足は2027年末まで。会社発言(株主総会、2026/6) | https://tw.stock.yahoo.com/news/ (台玻、中) |
| 金居会長 | HVLP4不足は拡大、受注能見度2028年 | https://www.ctee.com.tw/news/20260608701135-430201 (中、利害関係者発言) |
| 日東紡社長 | 「間に合わないくらい大きな需要」。NVIDIA・MS・Google・Amazonが主要能力を予約済(日経) | Nikkei/TrendForce(中) |
| 認定障壁 | T-glassの代替が事実上ない、中国はHVLP4未量産、石英は高コスト・工具摩耗 | TrendForce / faxiangongchang (中) |

### C-3. 株価の急落/上昇時の報道理由
**日東紡(3110)** ※5分割後。高値6,580円(2026/5)、分割前換算32,900円
| 日付 | 動き | 報道理由 | 出典 |
|---|---|---|---|
| 2025/9 | 発表で日東紡は大幅反発、台湾の富喬・台玻はストップ安 | 日東紡が150億円で高階クロス拡産を発表→台湾勢の供給希少性が薄れる | https://kabutan.jp/stock/news?code=3110&b=n202509010493 / https://wantrich.chinatimes.com/news/20250902900313-420101 |
| 2026/5/12-13 | 一時-12.4%(25,410円)、分割前 | 2027/3期の純利益予想が前期比-59%の170億円(QUICKコンセンサス206.7億を下回る)。前期は特殊要因で純利益が3.3倍。「追加値上げなし」が「Tガラス増産なし」と受け止められた(日経の見出し) | https://www.nikkei.com/article/DGXZQOFL132090T10C26A5000000/ / https://www.nikkei.com/article/DGXZRST0525575S6A510C2000000/ |
| 2026/6 | 高値から約50%下落 | 中国(巨石46億元、菲利華)の拡産と価格競争の懸念、AI銘柄の過熱修正 | https://news.nextapple.com/finance/20260614/3E56079E2C1CE3F0FE98DEBBCDAC5C0A / https://note.com/sumikko_money/n/na72ec6ce2c4d |
| 2026/8/6 | -17.9%(終値2,918円)、前日比-637円 | 営業益予想を260→300億円に上方修正も事前期待に届かず「材料出尽くし」。AI関連・米ハイテク安 | https://diamond.jp/zai/articles/-/1071161 / https://kabutan.jp/news/marketnews/?b=n202608060695 |
| 上記の整理 | - | 実績悪化ではなく**期待と価格形成の巻き戻し**(利益の山が2026/3期、市場予想比の未達、追加値上げなし、中国の脅威) | - |

**三井金属(5706)** ※10分割後(2026/9以降の価格は約2,500〜2,750円)
| 日付 | 動き | 報道理由 | 出典 |
|---|---|---|---|
| 2026/5/14 | 急反落 | 2027/3期の営業益-31%計画(前期の在庫評価益の剥落)。AI銅箔の失速ではない | https://kabutan.jp/news/marketnews/?b=n202605140445 |
| 2026/5/27 | 年初来高値57,700円(分割前) | 前期営業益を780億→1,170億円に上方修正、AI銅箔が牽引 | traders.co.jp/ebc要約(中) |
| 2026/6/26〜7/2 | -8.6%、-11.4%(終値38,250円) | 個別の適時開示は見つからず【未確認】。「期待が先行し需給が崩れた」との市場解説。7/16は-7.72%(出来高は爆発せず) | https://note.com/nplus_report/n/n5bd3b65075d5 (低、個人解説) / 7/16に米ハイテク・KOSPI安でAI関連全般が下落 |
| 2026/8/7-10 | 急反落 | 今期予想を上方修正(営業益910→940億円)も市場予想(営業益1,100億円強)に届かず | https://minkabu.jp/news/4592127 |
| 2026/9/3 | 25,505円(分割前) | 地合い悪化・金利上昇警戒・需給悪化。高値から約-56% | https://www.ebc.com/jp/forex/311531.html (低-中) |
| 2026/8/17-18 | 反落(別報道では続伸) | 2030年以降の銅箔増強(VSP月2,600t、MicroThin月1,200万m²)を発表 | https://kabutan.jp/news/marketnews/?b=n202608180414 |
| 2026/10/6 | 2,748円、+3.8% | 半導体・AI需要期待で買われた | https://www.ebc.com/jp/forex/313966.html |

---

## D. まとめ

### D-1. グレード別の需給(過不足率)推計表 2025〜2029
表記: 不足率(%)=(需要-供給)/需要。プラスは不足、マイナスは過剰。「-」は出典なし。各セルは出典の推計を並べた。【推定】は本調査担当の推定。

| グレード | 2025 | 2026 | 2027 | 2028 | 2029 | 出典のばらつき・コメント |
|---|---|---|---|---|---|---|
| **T-glass** | 不足が顕在化(リードタイム8→20週)。定量なし | Counterpoint 10%超 / Digitimes 40%超 / MS(高階クロス全体)約40% | Counterpoint 20% / Digitimes 25% / MS 2026より拡大 / Prismark 拡大 | MS(高階全体)約30% / Prismark 拡大(日東紡認定品のみ) / 【推定】中心シナリオ約20% | 出典なし。【推定】0〜20%(日東紡3倍と次世代T-glassの再単一供給化が綱引き) | 2026年の起点が10〜40%と開きが大きい。定義不明。2027年は4出典すべて「解消せず」で一致 |
| **Low-Dk NE/L2(第1/第2世代)** | 汎用E-glassから転換が進行 | 華泰: 第2世代Low-Dkに2026年ギャップ。MS 高階全体約40%。定量の個別出典なし | 【推定】10〜30% | 【推定】0〜15%(台玻・富喬・建榮・巨石・Kingboard・南亜の増設が重なる) | 【推定】過剰転換の可能性(-10〜+10%) | 供給者が多く、緩和は最も早い。「Low-Dk代替は2026-27で概ね完了」(TrendForce系要約)。数値出典がないため推定幅は広い |
| **Q-glass(石英)** | 世界生産100t未満(2024、調査会社要約) | 量産開始は2026Q2見込み(華泰)。需要はミッドプレーン次第 | 出典なし | 出典なし | 出典なし | 数量出典なし。需要は「Rubinミッドプレーンとスイッチ」の仕様(M9採否)で二値的に変動。格下げ報道あり。定量化不可と判断 |
| **HVLP4(および3+)** | 月産<50t(MS推計、HVLP4) | Digitimes 約1,500t不足 / GS(HVLP3+)28%(MSの2026年率は未入手) | MS 31% / Digitimes 2,500t / GS 39% | MS 20% / GS 38% | 出典なし。【推定】10〜30%(三井金属が2028/9に1,200t、2031年以降に2,600t) | MSとGSで2028年が20% vs 38%と2倍近い差。MSのt換算とも矛盾(注意3)。HVLP3以下は中国が追い上げ、HVLP4は2027-28に中国突破の可能性 |
| **キャリア付き極薄銅箔** | 出典なし | ABFギャップ代用: 約8-10% | ABF 約20%(Counterpoint) / 9.3%(MS) / JPM 稼働率100%超 | ABF 29%(BigGo) | ABF 約20%超(2030に22%、TVBS) | 銅箔そのものの需給推計は未入手。三井金属が事実上の主供給(MicroThinは2026年度490万→2028年度600万m²/月=約+22%)で、ABF需要の+40%/年(JPM)に対し供給は大きく見劣り。【推定】ABF基板ギャップと同方向で2028年まで不足 |

### D-2. 簡易需給モデル(T-glassの感度分析、【推定】)
前提と計算:
- 供給指数(2026年を100、日東紡中心の実効出力): 能力倍率は FY3/26=1.0、FY3/27=+10〜20%(旧ガイダンス)、FY3/28=2.0、FY3/29=3.0。暦年に直し、立ち上がり遅れを織り込むと2027年は×1.3〜1.7、2028年は×1.9〜2.6。中心は2027年×1.4、2028年×2.1(クロスは3倍でも糸が制約になる可能性を割り引く)。他社のT-glassは現状ほぼゼロ(単一供給)なので無視。
- 需要指数: CoWoS能力(130k→170k→260k)と、1個あたり基板面積・層数の増加より、2027年+30〜60%、2028年+30〜50%。中心は各+40%。
- 2026年起点の不足率g26は10%(Counterpoint)/25%(中間)/40%(Digitimes・MS)の3通り。

| シナリオ | 供給(2027/2028) | 需要伸び(2027/2028) | g26=10% | g26=25% | g26=40% |
|---|---|---|---|---|---|
| 弱気(緩和早い) | ×1.74 / ×2.6 | +30% / +30% | 2027年 -20%、2028年 -39% | 2027年 0%、2028年 -15% | 2027年 +20%、2028年 +8% |
| 中心 | ×1.4 / ×2.1 | +40% / +40% | 2027年 10%、2028年 4% | 2027年 25%、2028年 20% | 2027年 40%、2028年 36% |
| 強気(不足拡大) | ×1.3 / ×1.9 | +60% / +50% | 2027年 27%、2028年 29% | 2027年 39%、2028年 41% | 2027年 51%、2028年 52% |
(マイナスは供給過剰。算式: 不足率=1-(1-g26)×(供給指数/需要指数))
- 読み方: 中心シナリオ・g26=25%の結果(2027年25%、2028年20%)は、Counterpoint 20%、Digitimes 25%、MS 30%の出典レンジと一致する。**不足が解消するには「供給が毎年+40〜50%伸びる一方、需要の伸びが+30%以下に落ちる」ことが必要。** 需要の伸びが+40%以上で維持される限り、日東紡3倍でも不足は縮まらない。
- このモデルはT-glass単独の粗い試算で、台湾勢の供給追加、南亜、次世代品、仕様格下げ、在庫を含まない。精度は±10pt以上と見る。

### D-3. 需給が緩む時期の最有力の見立てと前提【推定】
**最有力: 緩みの起点は「2028年下半期〜2029年」。2027年は不足が最大化する年。価格が崩れるのはその後。ただしグレードで時期が異なる。**
| グレード | 緩む時期(最有力) | 一過性/構造的 |
|---|---|---|
| 汎用E-glass・Low-Dk第1世代 | 2027下半期〜2028(中国の巨石・建滔の新ラインで先に緩む) | 一過性(景気循環) |
| Low-Dk第2世代 | 2028 | 一過性寄り |
| T-glass | 2028年下半期以降(日東紡3倍+南亜+台玻)。ただし2028年の次世代T-glassで再び単一供給化 | 構造寄り(世代ごとに格上げ、認定障壁) |
| Q-glass | 判断不能(仕様次第) | 仕様依存 |
| HVLP4 | 2028年(MS: 20%に縮小)〜2029年。三井金属2,600t(2031年以降)・中国突破が価格の下押し要因 | 構造寄りだが、HVLP3以下は一過性 |
| キャリア付き極薄銅箔 | 2029年以降(三井金属の増強が緩やか) | 構造寄り(供給者が事実上1社、能力は+60%/2030年度) |

前提(崩れると見立てが変わる):
1. AI Capex・CoWoS能力が計画通り伸び続ける(TSMC CoWoS 130k→260kの2028年末)。2027年ピーク説が現実化し需要が+30%以下に落ちると、T-glassは2028年に過剰転換しうる(D-2の弱気)。
2. 日東紡が福島新棟を2027年Q1に稼働させ、糸の制約を回避して2028/3期に2倍、2029/3期に3倍を達成する。遅延すれば緩みは1年以上後ろへずれる。
3. 中国勢のT-glass/HVLP4が2027-28年に認定を通過しない(通過すれば緩みは前倒し、価格は先に崩れる)。認定に12〜24ヶ月かかるという推定が前提。
4. Rubin/Rubin Ultraで高級グレード(M9・Q-glass・HVLP4)の採用が維持される(M8/M8.5への格下げが進むとQ-glass・HVLP4の需要が縮む)。
5. CoWoP・ガラスコア・CPOの採用が2028年以降に限られる(NVIDIAの前倒しがあれば不足は短命)。
6. 日東紡が追加値上げを行わない方針(需給を理由にしない)を維持=T-glassの価格上昇は鈍化。利益は価格ではなく数量で増える構造。価格崩れの予兆はスポットではなく「汎用E-glassの価格反落」が先行指標になる可能性が高い【推定】。

テーマ判定への示唆(Opus向けの材料):
- 「不足の解消」自体は2028年後半〜2029年に始まる確度が高いが、2027年の利益ピークが2026/3期の特殊要因の剥落後も伸び続けるかが論点。日東紡の来期は純利益-52〜59%だが営業益は+44%(300億円)で、純利益の落ち込みは特殊要因。
- 三井金属は能力増が緩やか(MicroThin 約+22%/2028年度)で値崩れリスクはT-glassより小さいが、上方修正が市場予想に届かず売られる局面が続いている。
- 弱気側の根拠は「中国の汎用・Low-Dk増産」と「2027年Capexピーク説」に集中している。T-glass単体の弱気は、日東紡自身の3倍増産(供給側の自己責任)に依存。

---

## E. 未確認・追加調査が必要な項目
1. MS(2026/9/13)・GS・JPM・Prismark・Counterpointの原本(不足率の定義、絶対量、前提)。
2. 日東紡の2026/5/12・8/5決算説明資料(能力倍率3倍/2倍の基準年、糸の増強計画、T-glass価格方針)。
3. 三井金属のMicroThin価格改定(+12%)の確認、HVLPの品種別内訳(HVLP3/4/5)。
4. 新規T-glass・HVLP4サプライヤーの認定月数(関係者取材・決算説明会Q&A)。
5. エアジェット織機・溶融炉の実際のリードタイム(トヨタ産業車両・津田駒の決算コメント)。
6. T-glass・Low-Dkの絶対需要量(百万m、t)。
7. 德宏・宏和・信越・旭化成・SK Nexilis・古河電工の能力。今回の検索では情報が得られなかった。
8. 2024・2025年のCoWoS実績、GPU/ASIC台数、2028-29年のサーバー出荷。
