# eWeLL(5038) レンズ分析レポート

レンズ ok 19 / 入力不足 0 / 対象外 0 / 旗 7 (単位: 百万円)

## 示唆の種(旗)の一覧

| id | 旗 | 問い | 確かめ方 |
|---|---|---|---|
| L01-1 | 増益の最大項目が「価格」ではなく「売上高変化(数量等)」(シェア97.0%) | なぜ増益の主役が価格ではなく「売上高変化(数量等)」なのか？稼働率・需要の持続性はどの程度か？ | 会社の利益の増減分析と品目別の販売数量・稼働率推移の記述 |
| L02-1 | 粗利率の前年同期比が4期連続で悪化 | なぜ粗利率の悪化が4期連続で起きているのか？ | 原料価格・売価スプレッドと製品ミックスの四半期推移 |
| L05-1 | 残り期間の前提の利益率が累計より低い(営業利益率差-8.33pt) | 残り期間の利益率低下の前提は保守的な計画か、原料高・定修・値戻し等の悪化要因を織り込んでいるのか？ | 会社業績予想の前提条件(原料価格・為替前提)と足元の原料市況・下期定修予定 |
| L07-1 | 実績(2021→2025)で純利益率は上昇(28.53%→32.08%)したがROE改善は1pt未満 | なぜ純利益率が上がっても実績ROEが上がっていないのか？ | 有価証券報告書の貸借対照表(総資産と自己資本の増加要因) |
| L08-1 | 株主資本コスト(8.90%)を下回る資本使途あり: 自己株取得(益回り=12か月先EPS÷株価)、配当(配当性向24%)、現預金の保有、現預金の保有(現預金が総資産の66.7%) | なぜ資本コストより利回りの低い「自己株取得(益回り=12か月先EPS÷株価)、配当(配当性向24%)、現預金の保有、現預金の保有」に資本を滞留・配分させているのか？ | 資本コストや株価を意識した経営の開示資料・政策保有株縮減方針・借入返済と自己株買いの優先順位 |
| L12-1 | 株式数が年率+4.86%(>2%)で増加し希薄化が起きている | なぜ株式数が年2%超のペースで増えているのか(増資・CB・新株予約権か)？ | 有価証券報告書の株式総数推移・新株発行履歴と資金使途 |
| L19-1 | 会社予想は保守的に出す癖がある(今期の予想も同じ読み方ができるかを、前提の逆算 L05 と合わせて確かめる) | なぜ期初予想が保守的になりやすいのか(期中の上方修正の傾向か一過性要因か)？ | 過去の期初予想と実績・修正開示の推移および今期予想の前提条件 |

## レンズ別の詳細

### L01 利益の増減 [ok]
- 通期直近(2024→2025)は売上+31.9%・営業利益+35.4%(+402)。粗利・販管費分解では 売上変化×前期粗利率=+637、粗利率変化×当期売上=+20、−Δ販管費=-256。
- 主な数字: `{"annual_pair": "2024→2025", "annual_rev_chg_pct": 31.9, "annual_op_chg_pct": 35.36, "decomp_delta_op": 401.6, "decomp_volume_effect": 637.2, "decomp_margin_effect": 20.0, "decomp_sga_effect": -255.6, "max_positive_item": "売上高変化(数量等)", "max_positive_share_pct": 97.0}`
- **旗 L01-1**: 増益の最大項目が「価格」ではなく「売上高変化(数量等)」(シェア97.0%) / 問い: なぜ増益の主役が価格ではなく「売上高変化(数量等)」なのか？稼働率・需要の持続性はどの程度か？ / 確かめ方: 会社の利益の増減分析と品目別の販売数量・稼働率推移の記述

### L02 加速度 [ok]
- 直近期(FY26Q3)の営業利益率は47.17%(前年同期比+0.37pt、2期連続改善)。粗利率は76.79%(前年同期比-1.76pt、4期連続悪化)。営業利益率の前期比2階差分は-6.04pt。前年同期比の2階差分は-0.53pt。
- 主な数字: `{"latest_period": "FY26Q3", "latest_opm_pct": 47.17, "latest_opm_yoy_pt": 0.37, "opm_yoy_streak": 2, "opm_yoy_direction": "改善", "opm_second_diff_yoy_pt": -0.53, "opm_second_diff_seq_pt": -6.04, "latest_gm_pct": 76.79, "latest_gm_yoy_pt": -1.76, "gm_yoy_streak": 4, "gm_yoy_direction": "悪化", "gm_second_diff_yoy_pt": -0.41}`
- **旗 L02-1**: 粗利率の前年同期比が4期連続で悪化 / 問い: なぜ粗利率の悪化が4期連続で起きているのか？ / 確かめ方: 原料価格・売価スプレッドと製品ミックスの四半期推移

### L03 限界利益率と損益分岐点 [ok]
- 過去5期の回帰(営業利益 = 50.24%×売上 − 153)のR²は0.994。見かけの限界利益率は50.2%、損益分岐点売上は304、安全余裕率91.0%。
- 主な数字: `{"n_years": 5, "marginal_margin_pct": 50.24, "fixed_cost": 152.9, "r2": 0.9943, "latest_revenue": 3392.4, "breakeven_revenue": 304.3, "margin_of_safety_pct": 91.03}`

### L04 外部要因と自然実験 [ok]
- 過去5期の粗利率とドル円(年平均、サーバー費の外部要因・概数)の相関係数は-0.97(回帰予測式: 粗利率=87.63%-0.0635pt/1単位、残差σ=0.25pt)。
- ドル円(年平均、サーバー費の外部要因・概数)前年比が最大だったのは2022年(+19.7%)で、粗利率変化は-1.38pt。
- 直近(2025、ドル円(年平均、サーバー費の外部要因・概数) 150)の実績粗利率78.25%は回帰予測78.11%に対し+0.14pt(+0.55σ、対直近通期 ドル円(年平均、サーバー費の外部要因・概数)-0.9%・粗利率+0.59pt)。
- 主な数字: `{"input_price_name": "ドル円(年平均、サーバー費の外部要因・概数)", "n_years": 5, "corr": -0.9693, "r2": 0.9394, "reg_intercept": 87.633, "reg_slope_per_10k": -634.563, "residual_sigma_pt": 0.25, "residual_sigma_sample_pt": 0.32, "max_input_yoy_fy": "2022", "max_input_yoy_pct": 19.7, "max_shock_gm_delta_pt": -1.38, "latest_label": "2025", "latest_input_price": 150.0, "latest_actual_gm_pct": 78.25, "latest_pred_gm_pct": 78.11, "latest_residual_pt": 0.14, "latest_residual_sigma": 0.55, "latest_residual_sigma_sample": 0.43, "latest_input_vs_prev_pct": -0.9, "latest_gm_delta_pt": 0.59}`

### L05 会社予想の逆算 [ok]
- 会社予想(売上4,277・営業利益1,927)から累計実績を引いた残り期間(3か月)の前提は、売上1,209・営業利益473・営業利益率39.08%(累計47.41%比-8.33pt)。
- 残り期間の粗利率の前提は73.76%(累計76.35%比-2.59pt)。累計並みの粗利率なら通期営業利益は1,958(営業利益率基準では2,028)。
- 前年残り期間の営業利益率は37.18%(今期予想比+1.90pt)、営業利益率基準の通期は1,904(粗利率76.24%基準の通期は1,957)。
- 通期営業利益に対する進捗率は75.5%で、標準進捗75.0%を0.5pt上回る。
- 主な数字: `{"fy": "2026", "guidance_revenue": 4277.0, "guidance_op": 1927.0, "ytd_months": 9, "rest_revenue": 1209.4, "rest_op": 472.6, "ytd_opm_pct": 47.41, "rest_opm_pct": 39.08, "rest_minus_ytd_opm_pt": -8.33, "ytd_gm_pct": 76.35, "rest_implied_gm_pct": 73.76, "rest_minus_ytd_gm_pt": -2.59, "gm_is_estimated": false, "fy_op_if_ytd_margin": 1958.0, "fy_op_if_ytd_gm": 1958.0, "fy_op_if_ytd_opm": 2028.0, "prior_rest_opm_pct": 37.18, "prior_rest_gm_pct": 76.24, "rest_minus_prior_opm_pt": 1.9, "rest_minus_prior_gm_pt": -2.48, "fy_op_if_prior_opm": 1904.0, "fy_op_if_prior_gm": 1957.0, "op_progress_pct": 75.5, "standard_progress_pct": 75.0, "progress_excess_pt": 0.5}`
- **旗 L05-1**: 残り期間の前提の利益率が累計より低い(営業利益率差-8.33pt) / 問い: 残り期間の利益率低下の前提は保守的な計画か、原料高・定修・値戻し等の悪化要因を織り込んでいるのか？ / 確かめ方: 会社業績予想の前提条件(原料価格・為替前提)と足元の原料市況・下期定修予定

### L06 年換算と計画 [ok]
- セグメント別の年換算利益÷計画中央値: クラウド 96%(順調)、BPaaS 96%(順調)。
- 戦略セグメント合計は年換算379÷目標393=96.4%、非戦略セグメント合計は2,728÷2,826=96.5%。
- 主な数字: `{"segments": [{"name": "クラウド", "strategic": false, "ytd_profit": 2046.0, "annualized_profit": 2728.0, "plan_mid": 2826.0, "ratio_pct": 96.5, "pace": "順調"}, {"name": "BPaaS", "strategic": true, "ytd_profit": 284.0, "annualized_profit": 378.7, "plan_mid": 393.0, "ratio_pct": 96.4, "pace": "順調"}], "ahead_segments": [], "behind_segments": [], "strategic_annualized": 378.7, "strategic_plan_mid": 393.0, "strategic_ratio_pct": 96.4, "non_strategic_annualized": 2728.0, "non_strategic_plan_mid": 2826.0, "non_strategic_ratio_pct": 96.5}`

### L07 デュポン [ok]
- 実績デュポン: 実績_2021(純利益率28.53%×回転率1.12×レバ2.10=期末ROE67.49%) → 実績_2025(純利益率32.08%×回転率0.79×レバ1.27=期末ROE32.24%)
- 主な数字: `{"rows": [{"label": "実績_2021", "net_margin_pct": 28.53, "asset_turnover": 1.124, "leverage": 2.105, "roe_ending_pct": 67.49}, {"label": "実績_2025", "net_margin_pct": 32.08, "asset_turnover": 0.792, "leverage": 1.269, "roe_ending_pct": 32.24}]}`
- **旗 L07-1**: 実績(2021→2025)で純利益率は上昇(28.53%→32.08%)したがROE改善は1pt未満 / 問い: なぜ純利益率が上がっても実績ROEが上がっていないのか？ / 確かめ方: 有価証券報告書の貸借対照表(総資産と自己資本の増加要因)

### L08 資本の使い道 [ok]
- 株主資本コスト(8.90%)に対する資本使途の税後利回り順位: 1位 ソフトウエア投資(5期の税前増分利回り)(393.50%) > 2位 自己株取得(益回り)(4.35%) > 3位 自己株取得(益回り=12か月先EPS÷株価)(4.35%) > 4位 配当(配当性向24%)(0.90%) > 5位 現預金の保有(0.40%) > 6位 現預金の保有(0.10%)。
- 株主資本コストを下回る使途: 自己株取得(益回り=12か月先EPS÷株価)・配当(配当性向24%)・現預金の保有・現預金の保有。
- 自己株取得の益回り 4.35% は資本コスト 8.90% を下回る(今の株価での取得は割高)。
- 主な数字: `{"coe_pct": 8.9, "ranked_uses": [{"name": "ソフトウエア投資(5期の税前増分利回り)", "yield_pct": 393.5, "note": "lenses L13", "rank": 1, "spread_vs_coe_pt": 384.6}, {"name": "自己株取得(益回り)", "yield_pct": 4.35, "note": "eps_next 100.0 ÷ close 2297", "rank": 2, "spread_vs_coe_pt": -4.55}, {"name": "自己株取得(益回り=12か月先EPS÷株価)", "yield_pct": 4.35, "note": "2026年に300百万円を実行", "rank": 3, "spread_vs_coe_pt": -4.55}, {"name": "配当(配当性向24%)", "yield_pct": 0.9, "note": "配当利回り 21円÷2,297円", "rank": 4, "spread_vs_coe_pt": -8.0}, {"name": "現預金の保有", "yield_pct": 0.4, "note": "総資産の67%", "rank": 5, "spread_vs_coe_pt": -8.5}, {"name": "現預金の保有", "yield_pct": 0.1, "note": "現預金2,858(総資産の66.7%)・想定利回り0.10%", "rank": 6, "spread_vs_coe_pt": -8.8}], "below_coe_names": ["自己株取得(益回り=12か月先EPS÷株価)", "配当(配当性向24%)", "現預金の保有", "現預金の保有"], "cash_to_assets_pct": 66.7}`
- **旗 L08-1**: 株主資本コスト(8.90%)を下回る資本使途あり: 自己株取得(益回り=12か月先EPS÷株価)、配当(配当性向24%)、現預金の保有、現預金の保有(現預金が総資産の66.7%) / 問い: なぜ資本コストより利回りの低い「自己株取得(益回り=12か月先EPS÷株価)、配当(配当性向24%)、現預金の保有、現預金の保有」に資本を滞留・配分させているのか？ / 確かめ方: 資本コストや株価を意識した経営の開示資料・政策保有株縮減方針・借入返済と自己株買いの優先順位

### L09 織り込みROEと成長の値段 [ok]
- PBR 10.38倍(株価2,297円÷BPS221.3円)・COE 8.90%・g 2.0%からの市場織り込みROEは73.62%。
- 定常状態価値(予想EPS 100.0円÷COE)は1,124円で、株価に織り込まれた成長の値段は+1,173円。
- 直近実績ROE(32.24%)との差は+41.38pt。
- 主な数字: `{"pbr": 10.38, "implied_roe_pct": 73.62, "actual_roe_pct": 32.24, "implied_minus_actual_pt": 41.38, "model_base_roe_pct": null, "implied_minus_model_pt": null, "steady_state_value": 1123.6, "price_of_growth": 1173.4, "price_of_growth_pct_of_close": 51.1}`

### L10 同業の線 [ok]
- 同業8社のPBR-ROE回帰(PBR = 5.425 + 0.0535×ROE)のR²は0.07。
- 自社の実績ROE(32.24%)上の線上PBRは7.15倍で、実際PBR(10.38倍)との差は+45.2%。
- 自社の予想ROE(45.19%)上の線上PBRは7.84倍で、実際PBR(10.38倍)との差は+32.4%。
- ROE10%での線上PBRは5.96倍(線上株価1,319円: 参考値(線が当てはまらない))。
- 同業の PBR は ROE では説明できない(R² 0.07)。業態で同業を分け直すか、別の物差し(成長率など)を使う。
- 主な数字: `{"n_peers": 8, "reg_a": 5.4251, "reg_b": 0.0535, "r2": 0.0672, "actual_pbr": 10.38, "actual_roe_pct": 32.24, "line_pbr_at_actual_roe": 7.149, "pbr_diff_vs_line_pct": 45.2, "forward_roe_pct": 45.19, "line_pbr_at_forward_roe": 7.841, "pbr_diff_vs_line_forward_pct": 32.4, "model_base_roe_pct": null, "line_pbr_at_model_roe": null, "line_price_at_model_roe": null, "line_pbr_at_roe10": 5.96, "line_price_at_roe10": 1318.9}`

### L11 能力と市場 [ok]
- 契約ステーション数(中計): 規模・能力3843→4882件(2.25年)は年率+11.2%で市場成長率6.9%の1.63倍。現在水準20051件基準の必要増加年率は+-46.6%(-6.76倍)。
- 主な数字: `{"items": [{"name": "契約ステーション数(中計)", "unit": "件", "now": 3843.0, "after": 4882.0, "when": "2028-12", "years": 2.25, "market_cagr_pct": 6.9, "cap_cagr_pct": 11.22, "cap_vs_market_ratio": 1.63, "demand_now": 20051.0, "required_vol_cagr_pct": -46.63, "required_vs_market_ratio": -6.76}]}`

### L12 EPSの漏れ口 [ok]
- 直近期(2025)の支払利息÷営業利益は0.0%。
- 直近期(2025)の実効税率((税前−純利)÷税前)は29.6%。
- 株数(2021→2025、4年間)の年率は+4.86%。
- EPS対数分解(2021→2025): ln(EPS比)=+0.973 = ln(売上比)(+1.045) + ln(純利益率比)(+0.117) − ln(株数比)(+0.190)。
- 主な数字: `{"interest_to_op_pct": 0.0, "effective_tax_rate_pct": 29.63, "shares_cagr_pct": 4.86, "shares_span": "2021→2025", "ln_decomp_span": "2021→2025", "ln_eps_ratio": 0.9726, "ln_revenue_ratio": 1.0452, "ln_net_margin_ratio": 0.1172, "ln_shares_ratio": 0.1898}`
- **旗 L12-1**: 株式数が年率+4.86%(>2%)で増加し希薄化が起きている / 問い: なぜ株式数が年2%超のペースで増えているのか(増資・CB・新株予約権か)？ / 確かめ方: 有価証券報告書の株式総数推移・新株発行履歴と資金使途

### L13 投資と回収 [ok]
- 直近5期(2021〜2025)の設備投資累計は289(全データ5期累計は289)、営業利益増加(2021→2025)は+1,136で税前増分利回りは393.5%。
- 直近期の設備投資÷減価償却は0.75倍。総資産回転率は2021年1.124→2025年0.792(-0.332)。累計投資額は直近総資産の6.7%(全5期累計では6.7%)。
- 主な数字: `{"window_fys": "2021〜2025", "cum5_capex": 288.6, "op_base_fy": "2021", "op_gain": 1135.6, "pretax_incremental_roi_pct": 393.49, "latest_capex_to_dep": 0.75, "tat_first_fy": "2021", "tat_first": 1.124, "tat_last_fy": "2025", "tat_last": 0.792, "tat_diff": -0.332, "cum5_capex_pct_of_assets": 6.7, "cum_all_capex": 288.6, "cum_all_capex_pct_of_assets": 6.7}`

### L14 キャッシュ [ok]
- 在庫日数は2021年0.0日→2025年0.0日(+0.0日)。
- 在庫日数の式: 期末の在庫 ÷ 売上原価 × 365(2025年は 0 ÷ 738 × 365 = 0.0日、直近期FY26Q3の年換算売上原価 999 基準では 0.0日)。
- FCF(確認可能5期: 2021〜2025)の累計は+3,417、直近期(2025)は+1,191。
- 主な数字: `{"inv_days_first_fy": "2021", "inv_days_first": 0.0, "inv_days_last_fy": "2025", "inv_days_last": 0.0, "inv_days_diff": 0.0, "inv_days_period_label": "FY26Q3", "inv_days_period_annualized": 0.0, "fcf_window_fys": "2021〜2025", "fcf_n_years": 5, "fcf_cum": 3417.4, "fcf_last": 1190.7}`

### L15 利益のたまり場 [ok]
- セグメント別 利益構成比÷売上構成比: クラウド(売上86.9%・利益89.3%・利益率80.2%・倍率1.03x)、BPaaS(売上13.1%・利益10.7%・利益率64.2%・倍率0.82x)。
- 主な数字: `{"segments": [{"name": "クラウド", "revenue_share_pct": 86.9, "profit_share_pct": 89.3, "margin_pct": 80.18, "profit_to_rev_share_ratio": 1.03}, {"name": "BPaaS", "revenue_share_pct": 13.1, "profit_share_pct": 10.7, "margin_pct": 64.19, "profit_to_rev_share_ratio": 0.82}], "high_concentration_segments": []}`

### L16 感応度の換算 [ok]
- 価値の芯の候補は「契約数: 強気」(132円)。
- 事業ドライバー2位「単価: 強気」(130.3円)の1.02倍。
- なお複合/一律ショック最大は「EPS(全年度)」(165.7円)。
- 主な数字: `{"core_candidate": "契約数: 強気", "core_abs_diff": 132.4, "driver_ranking": [{"name": "契約数: 強気", "abs_diff": 132.4, "is_paired": false}, {"name": "単価: 強気", "abs_diff": 130.3, "is_paired": false}, {"name": "粗利率・販管費率: 弱気", "abs_diff": 59.5, "is_paired": false}, {"name": "単価: 弱気", "abs_diff": 37.1, "is_paired": false}, {"name": "粗利率・販管費率: 強気", "abs_diff": 32.6, "is_paired": false}, {"name": "契約数: 弱気", "abs_diff": 26.1, "is_paired": false}], "all_ranking": [{"name": "EPS(全年度)", "abs_diff": 165.7, "is_paired": true}, {"name": "契約数: 強気", "abs_diff": 132.4, "is_paired": false}, {"name": "単価: 強気", "abs_diff": 130.3, "is_paired": false}, {"name": "粗利率・販管費率: 弱気", "abs_diff": 59.5, "is_paired": false}, {"name": "単価: 弱気", "abs_diff": 37.1, "is_paired": false}, {"name": "粗利率・販管費率: 強気", "abs_diff": 32.6, "is_paired": false}, {"name": "契約数: 弱気", "abs_diff": 26.1, "is_paired": false}], "ratios_vs_top1": [{"name": "単価: 強気", "abs_diff": 130.3, "top1_div_other": 1.02}, {"name": "粗利率・販管費率: 弱気", "abs_diff": 59.5, "top1_div_other": 2.22}, {"name": "単価: 弱気", "abs_diff": 37.1, "top1_div_other": 3.57}, {"name": "粗利率・販管費率: 強気", "abs_diff": 32.6, "top1_div_other": 4.06}, {"name": "契約数: 弱気", "abs_diff": 26.1, "top1_div_other": 5.07}], "top1_to_top2_ratio": 1.02, "paired_second_name": null, "top1_to_paired_second_ratio": null}`

### L17 流動性 [ok]
- 1日売買代金85百万円の20%参加(17.00百万円/日)で算出: 5百万円は0.3日、30百万円は1.8日。
- 主な数字: `{"adv": 85.0, "participation_rate_pct": 20.0, "daily_20pct_capacity": 17.0, "positions_days": [{"position": 5.0, "days": 0.29}, {"position": 30.0, "days": 1.76}], "max_days": 1.76}`

### L18 価値の橋 [ok]
- 現在値 2,297円 → 今の利益が続く場合 1,124円(-1,173円)→ 理論株価 1,657円(成長と変化の上乗せ +534円、合計差 -640円)。株価は EPS が 204.4円(今より 104.4% 高い)で続くことを前提にしている。
- 主な数字: `{"close": 2297.0, "eps_next": 100.0, "coe_pct": 8.9, "steady_state_value": 1123.6, "current_power_gap": -1173.4, "implied_sustained_eps": 204.43, "implied_eps_vs_next_pct": 104.4, "model_base_roe_pct": null, "roe_spread_vs_coe_pt": null, "theoretical_price_B": 1657.5, "total_gap": -639.5, "growth_add": 533.9, "current_power_share_pct": 183.5, "growth_add_share_pct": -83.5}`

### L19 会社予想と計画の癖 [ok]
- 期初予想に対し、過去 4期のうち 4期で実績が上回った(中央値 +7.6%、平均 +10.2%)。
- 主な数字: `{"guidance_history": [{"fy": "2022", "initial_op": 562.0, "actual_op": 692.8, "surprise_pct": 23.3}, {"fy": "2023", "initial_op": 809.0, "actual_op": 908.7, "surprise_pct": 12.3}, {"fy": "2024", "initial_op": 1111.0, "actual_op": 1135.9, "surprise_pct": 2.2}, {"fy": "2025", "initial_op": 1494.0, "actual_op": 1537.5, "surprise_pct": 2.9}], "n_guidance_periods": 4, "n_beat": 4, "n_miss": 0, "beat_ratio_pct": 100.0, "mean_surprise_pct": 10.2, "median_surprise_pct": 7.6}`
- **旗 L19-1**: 会社予想は保守的に出す癖がある(今期の予想も同じ読み方ができるかを、前提の逆算 L05 と合わせて確かめる) / 問い: なぜ期初予想が保守的になりやすいのか(期中の上方修正の傾向か一過性要因か)？ / 確かめ方: 過去の期初予想と実績・修正開示の推移および今期予想の前提条件
