# 676h · 论文数字可追溯性审计报告

- 生成时间：2026-10-10T09:10:55+08:00
- 被审计稿件：`paper/paper2/paper2_measurement_drift.tex`（正文 None 页 / 全稿 23 页，取自编译日志）
- 权威源：14 个文件
- 检察条数：**124**，其中 consistent 44，硬 missing（active）63，软 missing（not_printed 等）2，skipped/no_source 3

## 0. 结论速览

**存在 63 条 active 级数字在论文里找不到对应写法**（详见 §1）。
待 676f/676g 数据就绪后刷新的检察：0 条（见 §3）。

## 1. 硬不一致清单（missing + active：源里有值、论文里必须出现却找不到）

| ID | 分组 | 状态 | 说明 | 应有写法 | 权威源 |
|---|---|---|---|---|---|
| A01 | A.核心三臂 | missing/active | holdout 可测检出率 82.9% (34/41) CI[67.9,92.8] | `82.9`, `34/41`, `67.9, 92.8` | `data/current_numbers.json` |
| A02 | A.核心三臂 | missing/active | corpus 可测检出率 62.5% (40/64) CI[49.5,74.3] | `62.5`, `40/64`, `49.5, 74.3` | `data/current_numbers.json` |
| A03 | A.核心三臂 | missing/active | corpus 全样本口径 52.6% | `52.6` | `data/current_numbers.json` |
| A05 | A.核心三臂 | missing/active | Random† 臂 holdout 9.8% (4/41) / corpus 21.9% (14/64) | `9.8`, `4/41`, `21.9`, `14/64` | `data/current_numbers.json` |
| A06 | A.核心三臂 | missing/active | Δ(Static→FD) holdout +80.5pp CI[68.4,92.6] p=2.3e-10 h=1.98 | `+80.5pp`, `68.4, 92.6`, `2.3\times10^{-10}`, `1.98` | `data/current_numbers.json` |
| A07 | A.核心三臂 | missing/active | Δ(Random†→FD) holdout +73.2pp CI[59.6,86.7] p=1.9e-9 h=1.65 | `+73.2pp`, `59.6, 86.7`, `1.9\times10^{-9}`, `1.65` | `data/current_numbers.json` |
| A08 | A.核心三臂 | missing/active | Δ(Static→FD) corpus +45.3pp CI[33.1,57.5] p=3.7e-9 h=0.97 | `+45.3pp`, `33.1, 57.5`, `3.7\times10^{-9}`, `0.97` | `data/current_numbers.json` |
| A09 | A.核心三臂 | missing/active | Δ(Random†→FD) corpus +40.6pp CI[28.6,52.7] p=3.0e-8 h=0.85 | `+40.6pp`, `28.6, 52.7`, `3.0\times10^{-8}`, `0.85` | `data/current_numbers.json` |
| A10 | A.核心三臂 | missing/active | 配对不一致对 (b, c)（tab:e5 四行） | `(33, 0)`, `(29, 0)`, `(30, 0)`, `(26, 0)` | `data/current_numbers.json` |
| A13 | A.核心三臂 | missing/active | CP95 半宽 12.5pp（holdout） | `12.5` | `data/current_numbers.json` |
| A14 | A.核心三臂 | missing/active | 扩样前 holdout 81.0% (17/21) CI[58.1,94.6] | `81.0`, `17/21` | `data/current_numbers.json` |
| A17 | A.核心三臂 | missing/active | ±5pp 半宽所需样本量 holdout 236 / corpus 378 | `236`, `378` | `data/current_numbers.json` |
| B02 | B.reveal | missing/active | holdout 口径 B（unknown→miss）34/42 = 81.0% | `34/42`, `81.0` | `data/holdout_reveal_5_672h.json` |
| B03 | B.reveal | missing/active | holdout 分层 sanitizer 84.6% (33/39) | `84.6`, `33/39` | `data/holdout_reveal_5_672h.json` |
| B04 | B.reveal | missing/active | corpus 分层 sanitizer 85.3% (29/34) / compiler-warn 50.0% (9/18) / cross-compile 16.7% (2/12) | `85.3`, `29/34`, `50.0`, `9/18`, `16.7`, `2/12` | `data/external_corpus_reveal_672h.json` |
| B05 | B.reveal | missing/active | corpus 口径 B（unknown→miss）40/73 = 54.8% | `40/73`, `54.8` | `data/external_corpus_reveal_672h.json` |
| B06 | B.reveal | missing/active | corpus 口径 C（全样本）40/76 = 52.6% | `40/76`, `52.6` | `data/external_corpus_reveal_672h.json` |
| B10 | B.reveal | missing/active | 历史批次 660：80.0%（batch compare before） | `80.0` | `data/holdout_reveal_3_665.json` |
| F02x | D2.A5-676f | missing/active | 676f 主端点（k=4，全 8 资产池）FD/Random/Static 三臂 | `54.6`, `309/566`, `30.6`, `173/566`, `24.7`, `140/566`, `60.1`, `340/566` | `data/a5_676f_results.json` |
| F03x | D2.A5-676f | missing/active | 676f 主端点 Δ(FD−Random) +24.0pp CI[+20.5, +27.5] p=2.3e-41 h=0.49 (b=136, c=0) | `+24.0pp`, `20.5, 27.5`, `2.3\times10^{-41}`, `0.49`, `(136,0)` | `data/a5_676f_results.json` |
| F04x | D2.A5-676f | missing/active | 676f 主端点 Δ(FD−Static) +29.9pp CI[+25.2, +34.5] p=1.9e-31 | `+29.9pp`, `25.2, 34.5`, `1.9\times10^{-31}`, `0.62` | `data/a5_676f_results.json` |
| F05x | D2.A5-676f | missing/active | 676f 2000 次随机分布：FD 严格优于 97.6%（Random 均值 40.2%，SD 9.3pp） | `97.6`, `40.2`, `9.3`, `2000` | `data/a5_676f_results.json` |
| F08x.legacy | D2.A5-676f | missing/active | 676f 子组 legacy：Δ +36.2pp，BH-FDR p=5.6e-05，Bonferroni p=0.00017 | `+36.2pp`, `+36.2`, `5.6\times10^{-5}`, `1.7\times10^{-4}`, `47` | `data/a5_676f_results.json` |
| F08x.concurrency | D2.A5-676f | missing/active | 676f 子组 concurrency：Δ +7.3pp，BH-FDR p=0.0095，Bonferroni p=0.086 | `+7.3pp`, `+7.3`, `0.010`, `0.086`, `109` | `data/a5_676f_results.json` |
| F10x.planted_false | D2.A5-676f | missing/active | 676f 真实缺陷 planted=false: FD 64.7% (22/34)，Δ +29.4pp | `64.7`, `22/34`, `+29.4pp`, `14.1, 44.7`, `2.0\times10^{-3}`, `35.3` | `data/a5_676f_results.json` |
| F10x.planted_true | D2.A5-676f | missing/active | 676f planted=true: FD 53.9% (287/532)，Δ +23.7pp | `53.9`, `287/532`, `+23.7pp`, `20.1, 27.3`, `2.4\times10^{-38}`, `30.3` | `data/a5_676f_results.json` |
| E01 | E.外部工具 | missing/active | clang-analyzer holdout 48.8% (20/41) p=1.2e-4 | `48.8`, `20/41`, `1.2\times10^{-4}` | `data/673e_comparison_stats.json` |
| E02 | E.外部工具 | missing/active | cppcheck holdout 41.5% (17/41) p=1.5e-5 | `41.5`, `17/41`, `1.5\times10^{-5}` | `data/673e_comparison_stats.json` |
| E03 | E.外部工具 | missing/active | cppcheck corpus 54.7% (35/64) p=0.38331031799316406 | `54.7`, `35/64`, `0.383` | `data/673e_comparison_stats.json` |
| E03b | E.外部工具 | missing/active | cppcheck corpus Δ +7.8pp CI[-6.1, 21.7]（CI 跨 0 ⇒ tie） | `+7.8pp`, `-6.1, 21.7`, `(13,8)` | `data/673e_comparison_stats.json` |
| E04 | E.外部工具 | missing/active | E9 附录 StrictA 对照 FPR 9.1% (1/11) | `9.1\% (1/11)`, `1/11` | `data/673e_comparison_stats.json` |
| E05 | E.外部工具 | missing/active | E9 附录 cppcheck 主口径 对照 FPR 9.1% (1/11) | `9.1\% (1/11)`, `1/11` | `data/673e_comparison_stats.json` |
| E06 | E.外部工具 | missing/active | E9 附录：holdout Δ(FD−StrictA) +34.1pp [19.6, 48.7]，对子 (14,0) | `+34.1pp`, `19.6, 48.7`, `(14,0)` | `data/673e_comparison_stats.json` |
| E07 | E.外部工具 | missing/active | E9 附录：corpus StrictA 34.4% (22/64)，Δ +28.1pp 对子 (23,5)，p=9.1e-4 | `34.4`, `22/64`, `+28.1pp`, `(23,5)`, `9.1\times10^{-4}` | `data/673e_comparison_stats.json` |
| F01 | F.LLM/锚点 | missing/active | 外部锚点子集 A（准则原文）28.6% (10/35) CI[14.6,46.3] | `28.6`, `10/35`, `14.6, 46.3` | `data/external_anchor_reveal_672j.json` |
| F02 | F.LLM/锚点 | missing/active | 外部锚点子集 B（UB 片段重建）80.0% (12/15) | `80.0`, `12/15` | `data/external_anchor_reveal_672j.json` |
| F04 | F.LLM/锚点 | missing/active | LLM 臂：GLM-4 12/12 vs FD 6/12；对照误报 4/8 = 50% | `12/12`, `6/12`, `4/8`, `50.0`, `50.0` | `data/experiments/llm_arm_672i.json` |
| F05 | F.LLM/锚点 | missing/active | LLM 臂配对 b/c = (0,6)，p=0.03125 | `0,6`, `0.031` | `data/experiments/llm_arm_672i.json` |
| G01 | G.变异/注入 | missing/active | 变异（core）110/114 = 96.5% | `110/114`, `96.5`, `91.3, 99.0` | `data/656_mutation_report.json` |
| G02 | G.变异/注入 | missing/active | 变异（all-scope）130/159 = 81.8% | `130/159`, `81.8` | `data/656_mutation_report_all.json` |
| H01 | H.样本量 | missing/active | 样本量：独立两比例 0.35→0.50 ⇒ n=170 | `170`, `170 (holdout)` | `Cohen arcsine h + Connor 配对；p1=0.35,p2=0.5,psi=None, α=0.05, power=0.8, recomputed=169.09` |
| H04 | H.样本量 | missing/active | 样本量：配对 ψ=0.3 ⇒ n=103 | `103`, `103 (holdout)` | `Cohen arcsine h + Connor 配对；p1=0.35,p2=0.5,psi=0.3, α=0.05, power=0.8, recomputed=102.26` |
| H05 | H.样本量 | missing/active | 样本量：配对 ψ=0.4 ⇒ n=138 | `138`, `138 (holdout)` | `Cohen arcsine h + Connor 配对；p1=0.35,p2=0.5,psi=0.4, α=0.05, power=0.8, recomputed=137.15` |
| H06 | H.样本量 | missing/active | 样本量：配对 ψ=0.5 ⇒ n=173 | `173`, `173 (holdout)` | `Cohen arcsine h + Connor 配对；p1=0.35,p2=0.5,psi=0.5, α=0.05, power=0.8, recomputed=172.04` |
| I01 | I.CI重算 | missing/active | Static holdout 1/41 CI ⇒ [0.1, 12.9] | `0.1, 12.9` | `python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(1,41)])"` |
| I02 | I.CI重算 | missing/active | Random† holdout 4/41 CI ⇒ [2.7, 23.1] | `2.7, 23.1` | `python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(4,41)])"` |
| I03 | I.CI重算 | missing/active | FD holdout 34/41 CI ⇒ [67.9, 92.8] | `67.9, 92.8` | `python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(34,41)])"` |
| I04 | I.CI重算 | missing/active | Caliber B holdout 34/42 CI ⇒ [65.9, 91.4] | `65.9, 91.4` | `python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(34,42)])"` |
| I05 | I.CI重算 | missing/active | Static corpus 11/64 CI ⇒ [8.9, 28.7] | `8.9, 28.7` | `python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(11,64)])"` |
| I06 | I.CI重算 | missing/active | Random† corpus 14/64 CI ⇒ [12.5, 34.0] | `12.5, 34.0` | `python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(14,64)])"` |
| I07 | I.CI重算 | missing/active | FD corpus 40/64 CI ⇒ [49.5, 74.3] | `49.5, 74.3` | `python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(40,64)])"` |
| I08 | I.CI重算 | missing/active | Caliber B corpus 40/73 CI ⇒ [42.7, 66.5] | `42.7, 66.5` | `python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(40,73)])"` |
| I09 | I.CI重算 | missing/active | Caliber C corpus 40/76 CI ⇒ [40.8, 64.2] | `40.8, 64.2` | `python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(40,76)])"` |
| I10 | I.CI重算 | missing/active | 对照 FPR 0/11 CI ⇒ [0.0, 28.5] | `0.0, 28.5` | `python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(0,11)])"` |
| D11 | D.A5 | missing/active | clone-aware 重切分 Δ +23.0~+26.7pp（677b，逐 split 为 +23.02/+25.70） | `23.02`, `25.70` | `current_numbers.a5_experiments.clone_aware_677b ← data/677b_a5_results_family_random.json / _family_stratified.json` |
| D13 | D.A5 | missing/active | 非退化池选择效应 +11.31pp（677c，k=1，p=6.02e-08） | `11.31` | `current_numbers.a5_experiments.nondegenerate_pool_677c ← data/677c_a5_nondegenerate_results.json` |
| D14 | D.A5 | missing/active | 退化资产对均值的贡献 ≈+12.81pp（677c） | `12.81` | `current_numbers.a5_experiments.nondegenerate_pool_677c ← data/677c_a5_nondegenerate_results.json` |
| Z01 | Z.689重构 | missing/active | 689 TOST：±10pp 未过，90% CI [-10.61, 5.52]pp，p_TOST=0.064 | `-10.61`, `5.52`, `0.064` | `current_numbers.reframed_689.equivalence_tost ← data/689_equivalence_test.json` |
| E02 | Z.689重构 | missing/active | 689 TOST 最小通过 margin 10.61pp（deff 校正 11.67pp） | `10.61`, `11.67` | `data/689_equivalence_test.json` |
| E03 | Z.689重构 | missing/active | 689 标准化：正向 -17.92pp（R_syn_std=77.01%），反向 +1.70pp，类型级 -13.52pp | `-17.92`, `77.01`, `1.70`, `-13.52` | `current_numbers.reframed_689.standardized_analysis ← data/689_standardized_analysis.json` |
| E04 | Z.689重构 | missing/active | 689 环境：真实 59.09%→23.64%（-35.45pp，Δunknown=0），clang↔g++ 93.5% | `59.09`, `23.64`, `35.45`, `93.5` | `current_numbers.reframed_689.environment_metrics ← data/689_environment_metrics.json` |
| Z12 | Z.691修正 | missing/active | 691 四个 κ（AI 自一致）：0.727 / 0.789 / 0.437 / 0.157 | `0.727`, `0.789`, `0.437`, `0.157` | `current_numbers.reframed_691.label_kappa_ai_self_consistency ← data/682_kappa.json` |
| Z13 | Z.691修正 | missing/active | 691 治理计数：452 ledger 事件 / 67 规则 / rules_sha256 v1.0.0 | `452`, `67` | `current_numbers.reframed_691.governance` |

### 1b. 软登记：源里算了、论文没打印（not_printed / retired，非不一致）

| ID | 说明 | 状态 |
|---|---|---|
| A15 | 扩样前 corpus 54.2% (26/48) | superseded:689重构 |
| A16 | H4 子集差额 corpus +33.3pp / holdout +4.0pp | superseded:689重构 |
| B08 | holdout 新子集 17/20 = 85.0%（round5） | superseded:689重构 |
| C06 | VC 的 Clopper–Pearson 95% CI [58.0, 86.1] | superseded:689重构 |
| D01 | A5 holdout 主端点 FD 90.0% (18/20) vs Random 35.0% | superseded_by_676f |
| D01b | A5 holdout 2000 次随机分布：FD 严格优于的比例与均值/标准差 | superseded_by_676f |
| D02 | A5 corpus 主端点 FD 81.25% (13/16) vs Random 37.5% | superseded_by_676f |
| D02b | A5 corpus 2000 次随机分布：FD 严格优于的比例与均值/标准差 | superseded_by_676f |
| K01 | tab:e3 第 656 行 “变异 core 62.5% (30/48)”：无任何现存产物可复现 | unpinned_no_artifact |
| K02 | tab:e3 第 665 行 “66.7%（旧 -O1 单档口径）”：源为已退役草稿口径 | unpinned_retired_caliber |
| I11 | corpus 分层 sanitizer 29/34 CI ⇒ [68.9, 95.0] | superseded:689重构 |
| I12 | corpus 分层 compiler-warn 9/18 CI ⇒ [26.0, 74.0] | superseded:689重构 |
| I13 | corpus 分层 cross-compile 2/12 CI ⇒ [2.1, 48.4] | superseded:689重构 |
| I14 | 缺陷重注入 6/6 CI ⇒ [54.1, 100.0] | superseded:689重构 |

### 1c. un-pinned 历史值（源不可得 / 口径已退役）

| ID | 说明 | 状态 | 处置 |
|---|---|---|---|
| K01 | tab:e3 第 656 行 “变异 core 62.5% (30/48)”：无任何现存产物可复现 | unpinned_no_artifact | 论文必须显式标注该行为 un-pinned 历史值，不得当作可复现结果（676h 已加脚注） |
| K02 | tab:e3 第 665 行 “66.7%（旧 -O1 单档口径）”：源为已退役草稿口径 | unpinned_retired_caliber | 该值口径已退休，只能作为“当时口径下读到的数”引用 |

## 2. 逐组概览

| 分组 | consistent | 其它 |
|---|---|---|
| A.核心三臂 | 5 | 14 |
| B.reveal | 3 | 7 |
| C.系统计数 | 2 | 4 |
| D.A5 | 4 | 7 |
| D2.A5-676f | 14 | 8 |
| D3.盲区地图 | 6 | 0 |
| E.外部工具 | 3 | 8 |
| F.LLM/锚点 | 1 | 4 |
| G.变异/注入 | 1 | 2 |
| H.样本量 | 2 | 4 |
| I.CI重算 | 0 | 14 |
| K.历史 un-pinned | 0 | 2 |
| N.诚实性反向检察 | 1 | 0 |
| Z.689重构 | 0 | 4 |
| Z.691修正 | 2 | 2 |

## 3. 待 676f / 676g 更新清单

依赖就绪状态（712 起为严格 AND：全部必需文件满足才算 ready；部分满足单列 `partial`，不再与 `ready` 混为一谈）：

| 依赖组 | 组状态 | 满足/必需 |
|---|---|---|
| 676f | `partial`（ready=False） | 1/3 |
| 676g | `partial`（ready=False） | 1/2 |

| 依赖 | 文件 | 当前行数 | 需要 | 就绪 |
|---|---|---|---|---|
| 676f | `data/a5_676f_results.json` | 1 | ≥1 | True |
| 676f | `data/a5_676f_matrix_local.jsonl` | 673 | ≥1147 | False |
| 676f | `data/a5_676f_matrix_san.jsonl` | 1054 | ≥1147 | False |
| 676g | `data/blindspot_676g_stats.json` | 1 | ≥1 | True |
| 676g | `data/blindspot_676g_ckpt_san.jsonl` | None | ≥3126 | False |

- **676f 数量不足**：`data/a5_676f_matrix_local.jsonl`(673<1147)、`data/a5_676f_matrix_san.jsonl`(1054<1147)
- **676g 缺失文件**：`data/blindspot_676g_ckpt_san.jsonl`

### 3b. 权威重算源（712 新增，与上面的「声明依赖」并列、不互相替代）

下面这张表回答的是另一个问题：**陌生研究者要重算你的关键数字，该读哪个文件？**上面的 .jsonl 是检测过程中的流式导出，从未达到声明规模；完整矩阵是这两个 JSON。两者分别列出，既不把 JSON 塞进 DEPENDENCY_FILES 顶绿，也不让 partial 状态被掩盖。

| 组 | 权威重算源 | 样本数 | 需要 | 可重算 |
|---|---|---|---|---|
| 676f | `data/frozen_matrix/a5_676f_detection_matrix.json` | 1137 | ≥1137 | True |
| 676g | `data/frozen_matrix/blindspot_676g_detection_matrix.json` | 1147 | ≥1147 | True |

| ID | 说明 |
|---|---|

## 4. 数字覆盖度（tex 全量扫描）

扫描到数字 token **653** 个（已排除注释行与导言区行）。分类：

| 类别 | 数量 | 占比 |
|---|---|---|
| claim | 421 | 64.5% |
| unclassified | 170 | 26.0% |
| design_constant | 35 | 5.4% |
| method_constant | 7 | 1.1% |
| system_constant | 7 | 1.1% |
| structural | 3 | 0.5% |
| repro_command | 3 | 0.5% |
| engineering_narrative | 2 | 0.3% |
| thirdparty_audit | 2 | 0.3% |
| batch_id | 2 | 0.3% |
| format_layout | 1 | 0.2% |

未归类 token：170 个（前 60 条见下；全量在 json 里）。

| 行 | token | 上下文 |
|---|---|---|
| 80 | `709` | `\author{Anonymous}% 709 Task E: de-identified for double-blind review (no affiliation/email).` |
| 100 | `30.0` | `drift requires re-measurement, with residual error up to $30.0\%$. (iii)~\textbf{Sample complexity}: the` |
| 102 | `849` | `$\Rightarrow$ infinite samples), while component-removal drift costs $849$ paired samples versus $17$ for` |
| 102 | `17` | `$\Rightarrow$ infinite samples), while component-removal drift costs $849$ paired samples versus $17$ for` |
| 105 | `147` | `We instantiate the framework on a C/C++ verification apparatus ($1{,}147$ samples) and, partially, on` |
| 106 | `55.8` | `LLM-as-a-judge evaluation (migration score $55.8/100$). All numbers come from frozen artifacts of earlier` |
| 151 | `4096` | `(T1--T6). Its metatheory is settled by exhaustive model checking over all $2^{4\times3}=4096$ coverage` |
| 155 | `6` | `to a 6-tuple. Caliber arbitrage is NP-hard (max-coverage reduction) with a greedy $(1-1/e)$ approximation.` |
| 285 | `24.735` | `the same $140$ catches are reported as $24.735\%$ under the unaware denominator and as $100.0\%$ when only` |
| 286 | `75.265` | `capability-relevant negatives enter it: a $+75.265\pp$ move produced by \emph{no new measurement}. For` |
| 288 | `13` | `whose blind-spot rate exceeds $50\%$ is $13/34=38.24\%$ under the normalised vocabulary and` |
| 288 | `34` | `whose blind-spot rate exceeds $50\%$ is $13/34=38.24\%$ under the normalised vocabulary and` |
| 288 | `38.24` | `whose blind-spot rate exceeds $50\%$ is $13/34=38.24\%$ under the normalised vocabulary and` |
| 289 | `25.71` | `$18/70=25.71\%$ under the original mixed one. For Type~IV the identical $1147\times 8$ verdict matrix` |
| 290 | `17.6692` | `yields $61.6392\%$ under OR and $17.6692\%$ under the per-asset mean ($13.2518\%$ if the two structurally` |
| 290 | `13.2518` | `yields $61.6392\%$ under OR and $17.6692\%$ under the per-asset mean ($13.2518\%$ if the two structurally` |
| 292 | `33.33` | `cannot be compared across calibers, and a drift invisible under one aggregation rule can be $33.33\%$ under` |
| 302 | `5.470342` | `$g_{\text{app}}(d)=5.470342+5.284164\,d-0.259967\,d^{2}$ ($R^{2}=0.999724$) over $5.30\to29.88\pp$; the` |
| 302 | `5.30` | `$g_{\text{app}}(d)=5.470342+5.284164\,d-0.259967\,d^{2}$ ($R^{2}=0.999724$) over $5.30\to29.88\pp$; the` |
| 303 | `5.284164` | `response function $\chi=5.284164-0.519934\,d$ decreases monotonically and its stationary point` |
| 304 | `7` | `$d^{*}=10.1632$ lies \emph{outside} the data range $[0,7]$, so over the observable range there is no` |
| 313 | `6` | `We therefore downgrade C2 to a \emph{descriptive framework}: with $6$--$8$ data points and a model-implied` |
| 359 | `28` | `correct for them---superposition \emph{understates} the total, by $4.95\pp$ in the partition where $28$` |
| 407 | `23` | `Let $E_1\supseteq E_2$ and let $T_{12},T_{23},T_{13}$ be per-sample three-state transition count matrices,` |
| 407 | `13` | `Let $E_1\supseteq E_2$ and let $T_{12},T_{23},T_{13}$ be per-sample three-state transition count matrices,` |
| 408 | `23` | `with $P_{23}$ the row-normalised $T_{23}$. Then` |
| 408 | `23` | `with $P_{23}$ the row-normalised $T_{23}$. Then` |
| 409 | `13` | `$T_{13}=T_{12}P_{23}\Longleftrightarrow T^{(E_2\to E_3)}_{\miss\to\catch}=0$, i.e.\ iff` |
| 409 | `23` | `$T_{13}=T_{12}P_{23}\Longleftrightarrow T^{(E_2\to E_3)}_{\miss\to\catch}=0$, i.e.\ iff` |
| 414 | `23` | `$P_{23}[\miss][\miss]=1$ and Theorem~\ref{thm:T4} kills the reverse pair, so the $(\catch,\miss)$ cell of` |
| 451 | `256` | `the scale of the instantiation ($|A|=8$, $2^{8}=256$ calibers) the problem is trivially enumerable. Its` |
| 544 | `110` | `E1 & $8$ assets; frames $1147$, $1137$, $566$, $110$ & the five transition matrices are reproduced with` |
| 562 | `80` | `\paragraph{E4: a cross-domain arm (partial).} Setting: an LLM-as-a-judge arm with $80$ samples $\times$` |
| 573 | `42.50` | `declared label says miss---is $26.25\%$ (reasoning judge) and $42.50\%$ (non-reasoning judge). The ten most` |
| 574 | `6` | `severe cases concentrate in the \emph{embedded} (6) and \emph{concurrency} (3) defect families, exactly the` |
| 609 | `92.9` | `the environment axis has two control points; $92.9\%$ of the corpus is human-planted; the ``always true''` |
| 610 | `4096` | `metatheory verdicts hold only over the $4096$-structure, seven-aggregation domain, so they are in-domain` |
| 630 | `53.05` | `measured anti-drift score from $53.05$ to $66.67$ out of $100$ in a simulation over the same frozen matrix.` |
| 630 | `66.67` | `measured anti-drift score from $53.05$ to $66.67$ out of $100$ in a simulation over the same frozen matrix.` |
| 647 | `53.05` | `$53.05$ to $66.67$.` |
| 647 | `66.67` | `$53.05$ to $66.67$.` |
| 707 | `23` | `$V_3\in\{\miss,\unk\}$ (here $\unk\equiv0$), giving $P_{23}[\miss][\miss]=1$. \emph{One-directionality}:` |
| 709 | `23` | `$T_{12}[c][c]\cdot P_{23}[c][m]+T_{12}[c][m]\cdot1$, and` |
| 710 | `23` | `$P_{23}[c][m]=T_{23}[c][m]/|E_2\text{-catch}|$ with` |
| 710 | `23` | `$P_{23}[c][m]=T_{23}[c][m]/|E_2\text{-catch}|$ with` |
| 711 | `23` | `$|E_2\text{-catch}|=T_{12}[c][c]+T_{12}[m][c]=T_{12}[c][c]$, so the first term is $T_{23}[c][m]$ and the` |
| 712 | `23` | `product cell equals $T_{23}[c][m]+T_{12}[c][m]$. The true cell is` |
| 713 | `23` | `$\#\{V_1{=}c,V_3{=}m\}=\#\{V_2{=}c,V_3{=}m\}+\#\{V_2{=}m,V_3{=}m\}=T_{23}[c][m]+T_{12}[c][m]$ by` |
| 716 | `23` | `($\Leftarrow$) If $T_{23}[m][c]>0$ there is a sample with $V_2=\miss$, $V_3=\catch$. If` |
| 719 | `13` | `$(\miss,\catch)$ cell is non-zero whereas the true $T_{13}$ cell is $0$. $\square$` |
| 741 | `709` | `\label{sec:meta}% 709: retained so \ref{sec:meta} still resolves now that the section lives in the appendix` |
| 748 | `4096` | `$2^{4\times3}=4096$ coverage structures, crossed with seven aggregation families deliberately chosen to` |
| 753 | `4096` | `The independence witnesses for all $4096$ structures $\times$ $7$ aggregations are in Appendix~\ref{app:meta} ` |
| 791 | `38.24` | `exceeding $50\%$ blind-spot rate is $38.24\%$ under the normalised $34$-type vocabulary and $25.71\%$ under` |
| 791 | `34` | `exceeding $50\%$ blind-spot rate is $38.24\%$ under the normalised $34$-type vocabulary and $25.71\%$ under` |
| 791 | `25.71` | `exceeding $50\%$ blind-spot rate is $38.24\%$ under the normalised $34$-type vocabulary and $25.71\%$ under` |
| 815 | `4096` | `Model domain: $|X|=4$ samples, $|A|=3$ assets, all $2^{4\times3}=4096$ coverage structures, seven` |
| 899 | `4096` | `\caption{Axiom independence over all $4096$ structures $\times$ $7$ aggregations. The minimal axiom set is` |
| 899 | `7` | `\caption{Axiom independence over all $4096$ structures $\times$ $7$ aggregations. The minimal axiom set is` |
| 912 | `3840` | `A7 & theorem & none ($3840$ witnesses); provable once accounting is written into the structure (T3) \\` |

## 5. 每条检察的命中明细

**A01 · holdout 可测检出率 82.9% (34/41) CI[67.9,92.8]** — missing/active `✗✗✗`
- 源：`data/current_numbers.json`
  - ✗ `82.9` × 0 @ L
  - ✗ `34/41` × 0 @ L
  - ✗ `67.9, 92.8` × 0 @ L
**A02 · corpus 可测检出率 62.5% (40/64) CI[49.5,74.3]** — missing/active `✗✗✗`
- 源：`data/current_numbers.json`
  - ✗ `62.5` × 0 @ L
  - ✗ `40/64` × 0 @ L
  - ✗ `49.5, 74.3` × 0 @ L
**A03 · corpus 全样本口径 52.6%** — missing/active `✗`
- 源：`data/current_numbers.json`
  - ✗ `52.6` × 0 @ L
**A04 · Static 臂 holdout 2.4% (1/41) / corpus 17.2% (11/64)** — consistent/active `✓✗✗✗`
- 源：`data/current_numbers.json`
  - ✓ `2.4` × 2 @ L853,1104
  - ✗ `1/41` × 0 @ L
  - ✗ `17.2` × 0 @ L
  - ✗ `11/64` × 0 @ L
**A05 · Random† 臂 holdout 9.8% (4/41) / corpus 21.9% (14/64)** — missing/active `✗✗✗✗`
- 源：`data/current_numbers.json`
  - ✗ `9.8` × 0 @ L
  - ✗ `4/41` × 0 @ L
  - ✗ `21.9` × 0 @ L
  - ✗ `14/64` × 0 @ L
**A06 · Δ(Static→FD) holdout +80.5pp CI[68.4,92.6] p=2.3e-10 h=1.98** — missing/active `✗✗✗✗`
- 源：`data/current_numbers.json`
  - ✗ `+80.5pp` × 0 @ L
  - ✗ `68.4, 92.6` × 0 @ L
  - ✗ `2.3\times10^{-10}` × 0 @ L
  - ✗ `1.98` × 0 @ L
**A07 · Δ(Random†→FD) holdout +73.2pp CI[59.6,86.7] p=1.9e-9 h=1.65** — missing/active `✗✗✗✗`
- 源：`data/current_numbers.json`
  - ✗ `+73.2pp` × 0 @ L
  - ✗ `59.6, 86.7` × 0 @ L
  - ✗ `1.9\times10^{-9}` × 0 @ L
  - ✗ `1.65` × 0 @ L
**A08 · Δ(Static→FD) corpus +45.3pp CI[33.1,57.5] p=3.7e-9 h=0.97** — missing/active `✗✗✗✗`
- 源：`data/current_numbers.json`
  - ✗ `+45.3pp` × 0 @ L
  - ✗ `33.1, 57.5` × 0 @ L
  - ✗ `3.7\times10^{-9}` × 0 @ L
  - ✗ `0.97` × 0 @ L
**A09 · Δ(Random†→FD) corpus +40.6pp CI[28.6,52.7] p=3.0e-8 h=0.85** — missing/active `✗✗✗✗`
- 源：`data/current_numbers.json`
  - ✗ `+40.6pp` × 0 @ L
  - ✗ `28.6, 52.7` × 0 @ L
  - ✗ `3.0\times10^{-8}` × 0 @ L
  - ✗ `0.85` × 0 @ L
**A10 · 配对不一致对 (b, c)（tab:e5 四行）** — missing/active `✗✗✗✗`
- 源：`data/current_numbers.json`
  - ✗ `(33, 0)` × 0 @ L
  - ✗ `(29, 0)` × 0 @ L
  - ✗ `(30, 0)` × 0 @ L
  - ✗ `(26, 0)` × 0 @ L
  - 注：四个对比都是 c=0 结构（对手的 catch 是 FD catch 的子集）
**A11 · 对照假阳性 0.0% (0/11)** — consistent/active `✗✓`
- 源：`data/current_numbers.json`
  - ✗ `0.0\% (0/11)` × 0 @ L
  - ✓ `0.0` × 7 @ L311,384,548,776,842
**A12 · 缺陷重注入 6/6 = 100%** — consistent/active `✗✓`
- 源：`data/current_numbers.json`
  - ✗ `6/6` × 0 @ L
  - ✓ `100.0` × 1 @ L285
**A13 · CP95 半宽 12.5pp（holdout）** — missing/active `✗`
- 源：`data/current_numbers.json`
  - ✗ `12.5` × 0 @ L
**A14 · 扩样前 holdout 81.0% (17/21) CI[58.1,94.6]** — missing/active `✗✗`
- 源：`data/current_numbers.json`
  - ✗ `81.0` × 0 @ L
  - ✗ `17/21` × 0 @ L
**A15 · 扩样前 corpus 54.2% (26/48)** — retired/superseded:689重构 `✗✗`
- 源：`data/current_numbers.json`
  - ✗ `54.2` × 0 @ L
  - ✗ `26/48` × 0 @ L
  - 注：689 重构：扩样前后口径随旧正文段落移出正文（数据仍在产物）
**A16 · H4 子集差额 corpus +33.3pp / holdout +4.0pp** — retired/superseded:689重构 `✗✗`
- 源：`data/current_numbers.json`
  - ✗ `+33.3pp` × 0 @ L
  - ✗ `+4.0pp` × 0 @ L
  - 注：689 重构：H4 子集差额随旧正文段落移出正文（数据仍在产物）
**A17 · ±5pp 半宽所需样本量 holdout 236 / corpus 378** — missing/active `✗✗`
- 源：`data/current_numbers.json`
  - ✗ `236` × 0 @ L
  - ✗ `378` × 0 @ L
**A18 · ±10pp 半宽所需样本量 holdout 61 / corpus 97** — consistent/active `✓✗`
- 源：`data/current_numbers.json`
  - ✓ `61` × 3 @ L290,1035
  - ✗ `97` × 0 @ L
**B01 · holdout 累计 catch/miss/unknown = 34/7/1，分母 41** — consistent/active `✗✓`
- 源：`data/holdout_reveal_5_672h.json`
  - ✗ `34/41` × 0 @ L
  - ✓ `1` × 57 @ L105,130,155,166,397,414,430,447
**B02 · holdout 口径 B（unknown→miss）34/42 = 81.0%** — missing/active `✗✗`
- 源：`data/holdout_reveal_5_672h.json`
  - ✗ `34/42` × 0 @ L
  - ✗ `81.0` × 0 @ L
**B03 · holdout 分层 sanitizer 84.6% (33/39)** — missing/active `✗✗`
- 源：`data/holdout_reveal_5_672h.json`
  - ✗ `84.6` × 0 @ L
  - ✗ `33/39` × 0 @ L
**B04 · corpus 分层 sanitizer 85.3% (29/34) / compiler-warn 50.0% (9/18) / cross-compile 16.7% (2/12)** — missing/active `✗✗✗✗✗✗`
- 源：`data/external_corpus_reveal_672h.json`
  - ✗ `85.3` × 0 @ L
  - ✗ `29/34` × 0 @ L
  - ✗ `50.0` × 0 @ L
  - ✗ `9/18` × 0 @ L
  - ✗ `16.7` × 0 @ L
  - ✗ `2/12` × 0 @ L
**B05 · corpus 口径 B（unknown→miss）40/73 = 54.8%** — missing/active `✗✗`
- 源：`data/external_corpus_reveal_672h.json`
  - ✗ `40/73` × 0 @ L
  - ✗ `54.8` × 0 @ L
**B06 · corpus 口径 C（全样本）40/76 = 52.6%** — missing/active `✗✗`
- 源：`data/external_corpus_reveal_672h.json`
  - ✗ `40/76` × 0 @ L
  - ✗ `52.6` × 0 @ L
**B07 · corpus 分层 Excluded unknown=9 / not_error=3** — consistent/active `✓✓`
- 源：`data/external_corpus_reveal_672h.json`
  - ✓ `9` × 6 @ L650,874,994,1015,1096,1110
  - ✓ `3` × 26 @ L131,189,540,550,574,618,727,747
**B08 · holdout 新子集 17/20 = 85.0%（round5）** — retired/superseded:689重构 `✗✗`
- 源：`data/holdout_reveal_5_672h.json`
  - ✗ `17/20` × 0 @ L
  - ✗ `85.0` × 0 @ L
  - 注：689 重构：round5 子集数字随旧正文段落移出正文（数据仍在产物）
**B09 · 历史批次 669：87.5%（14/16）与 CI[61.7, 98.4]** — consistent/active `✓`
- 源：`data/holdout_reveal_3_665.json`
  - ✓ `87.5` × 1 @ L1146
**B10 · 历史批次 660：80.0%（batch compare before）** — missing/active `✗`
- 源：`data/holdout_reveal_3_665.json`
  - ✗ `80.0` × 0 @ L
**C01 · 判决规则数 67（len(gate_engine.RULES)）** — no_source_value/cmd_failed ``
- 源：`python -c "import sys;sys.path.insert(0,'tools');import gate_engine;print(len(gate_engine.RULES))"`
  - 注：in <module>
    from path_config_625 import root as _queyi_root  # noqa: E402  (625 C1 路径解耦)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'path_config_625'
**C02 · 权威账本事件数 452（decision_event_v2_ledger.jsonl 非空行）** — no_source_value/cmd_failed ``
- 源：`python -c "n=sum(1 for l in open(r'data/authority/decision_event_v2_ledger.jsonl',encoding='utf-8') if l.strip());print(n)"`
  - 注：(n)
                     ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'data/authority/decision_event_v2_ledger.jsonl'
**C03 · 实卡数 atoms_real = 0（counts_659.py 现算）** — consistent/active `✓`
- 源：`python tools/counts_659.py --json`
  - ✓ `0` × 135 @ L13,162,163,167,301,302,303,304
**C06 · VC 的 Clopper–Pearson 95% CI [58.0, 86.1]** — retired/superseded:689重构 `✗`
- 源：`python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(31,42)])"`
  - ✗ `58.0, 86.1` × 0 @ L
  - 注：689 重构：VC 及其 CI 已从论文删除（工程遥测，非科学证据）
**C07 · 规则严重度分解** — no_source_value/cmd_failed ``
- 源：`python -c "import sys;sys.path.insert(0,'tools');import gate_engine;from collections import Counter;c=Counter(getattr(r,'severity',None) for r in gate_engine.RULES);print(c.get('block',0),c.get('warn',0),c.get('advice',0))"`
  - 注：Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import sys;sys.path.insert(0,'tools');import gate_engine;from collections import Counter;c=Counter(getattr(r,'severity',No
**C08 · 边界卡 26 张；provenance 完整 26/26；scope 完整 0/26** — consistent/active `✓✗✗`
- 源：`data/boundary_provenance_658.json`
  - ✓ `26` × 4 @ L573,973,1018
  - ✗ `26/26` × 0 @ L
  - ✗ `0/26` × 0 @ L
  - 注：provenance 完整 = provenance 字典字段数 ≥3（mutationset/generator/evidence）
**N01 · 81.2% 必须在出现的每一处都被标为从未落盘/作废** — consistent/active `✓`
- 源：`673c/676h 诚实边界：81.2% 不得作为已落盘结果引用`
  - ✓ `81.2` × 1 @ L
  - 注：若 81.2 出现在没有 never-landed 标注的句子里 ⇒ 违反
**D01 · A5 holdout 主端点 FD 90.0% (18/20) vs Random 35.0%** — retired/superseded_by_676f `✗✗✗✗✗✗✗✗✗✗`
- 源：`data/experiments/a5_673p.json`
  - ✗ `90.0` × 0 @ L
  - ✗ `18/20` × 0 @ L
  - ✗ `35.0` × 0 @ L
  - ✗ `7/20` × 0 @ L
  - ✗ `10.0` × 0 @ L
  - ✗ `2/20` × 0 @ L
  - ✗ `+55.0pp` × 0 @ L
  - ✗ `33.2, 76.8` × 0 @ L
  - ✗ `9.8\times10^{-4}` × 0 @ L
  - ✗ `1.23` × 0 @ L
  - 注：673p/673r 口径；已被 676f 全量重跑取代，论文仅在 app:humanize 保留其审计轨迹
**D01b · A5 holdout 2000 次随机分布：FD 严格优于的比例与均值/标准差** — retired/superseded_by_676f `✗✗✗✗`
- 源：`data/experiments/a5_673p.json`
  - ✗ `93.75` × 0 @ L
  - ✗ `93.8` × 0 @ L
  - ✗ `55.0` × 0 @ L
  - ✗ `23.4` × 0 @ L
**D01c · A5 设计量：holdout 派生 n=21 / 评估 n=20** — consistent/superseded_by_676f `✓✓✓✗✓✗`
- 源：`data/experiments/a5_673p.json`
  - ✓ `21` × 6 @ L552,1076,1127,1128,1149
  - ✓ `20` × 3 @ L953,1018,1267
  - ✓ `4` × 26 @ L151,359,619,747,748,815,829,907
  - ✗ `2000` × 0 @ L
  - ✓ `8` × 13 @ L268,289,313,399,451,544,870,881
  - ✗ `41` × 0 @ L
**D02 · A5 corpus 主端点 FD 81.25% (13/16) vs Random 37.5%** — retired/superseded_by_676f `✗✗✗✗✗✗✗✗✗✗`
- 源：`data/experiments/a5_673p.json`
  - ✗ `81.2` × 0 @ L
  - ✗ `13/16` × 0 @ L
  - ✗ `37.5` × 0 @ L
  - ✗ `6/16` × 0 @ L
  - ✗ `37.5` × 0 @ L
  - ✗ `6/16` × 0 @ L
  - ✗ `+43.8pp` × 0 @ L
  - ✗ `13.9, 73.6` × 0 @ L
  - ✗ `0.039` × 0 @ L
  - ✗ `0.93` × 0 @ L
  - 注：673p/673r 口径；已被 676f 全量重跑取代，论文仅在 app:humanize 保留其审计轨迹
**D02b · A5 corpus 2000 次随机分布：FD 严格优于的比例与均值/标准差** — retired/superseded_by_676f `✗✗✗✗`
- 源：`data/experiments/a5_673p.json`
  - ✗ `95.80` × 0 @ L
  - ✗ `95.8` × 0 @ L
  - ✗ `53.7` × 0 @ L
  - ✗ `16.0` × 0 @ L
**D02c · A5 设计量：corpus 派生 n=48 / 评估 n=16** — consistent/superseded_by_676f `✓✓✓✗✓✗`
- 源：`data/experiments/a5_673p.json`
  - ✓ `48` × 1 @ L991
  - ✓ `16` × 2 @ L1077,1147
  - ✓ `4` × 26 @ L151,359,619,747,748,815,829,907
  - ✗ `2000` × 0 @ L
  - ✓ `8` × 13 @ L268,289,313,399,451,544,870,881
  - ✗ `64` × 0 @ L
**F01x · 676f 样本簿记：1137 总样本；派生 571；评估 566** — consistent/active `✓✓✓✗✓✓`
- 源：`data/a5_676f_results.json`
  - ✓ `1137` × 3 @ L544,971
  - ✓ `571` × 2 @ L970
  - ✓ `566` × 21 @ L166,355,384,396,416,544,549,554
  - ✗ `1063` × 0 @ L
  - ✓ `74` × 2 @ L417,551
  - ✓ `10` × 6 @ L304,945,953,991,995,1322
**F02x · 676f 主端点（k=4，全 8 资产池）FD/Random/Static 三臂** — missing/active `✗✗✗✗✗✗✗✗`
- 源：`data/a5_676f_results.json`
  - ✗ `54.6` × 0 @ L
  - ✗ `309/566` × 0 @ L
  - ✗ `30.6` × 0 @ L
  - ✗ `173/566` × 0 @ L
  - ✗ `24.7` × 0 @ L
  - ✗ `140/566` × 0 @ L
  - ✗ `60.1` × 0 @ L
  - ✗ `340/566` × 0 @ L
**F03x · 676f 主端点 Δ(FD−Random) +24.0pp CI[+20.5, +27.5] p=2.3e-41 h=0.49 (b=136, c=0)** — missing/active `✗✗✗✗✗`
- 源：`data/a5_676f_results.json`
  - ✗ `+24.0pp` × 0 @ L
  - ✗ `20.5, 27.5` × 0 @ L
  - ✗ `2.3\times10^{-41}` × 0 @ L
  - ✗ `0.49` × 0 @ L
  - ✗ `(136,0)` × 0 @ L
**F04x · 676f 主端点 Δ(FD−Static) +29.9pp CI[+25.2, +34.5] p=1.9e-31** — missing/active `✗✗✗✗`
- 源：`data/a5_676f_results.json`
  - ✗ `+29.9pp` × 0 @ L
  - ✗ `25.2, 34.5` × 0 @ L
  - ✗ `1.9\times10^{-31}` × 0 @ L
  - ✗ `0.62` × 0 @ L
**F05x · 676f 2000 次随机分布：FD 严格优于 97.6%（Random 均值 40.2%，SD 9.3pp）** — missing/active `✗✗✗✗`
- 源：`data/a5_676f_results.json`
  - ✗ `97.6` × 0 @ L
  - ✗ `40.2` × 0 @ L
  - ✗ `9.3` × 0 @ L
  - ✗ `2000` × 0 @ L
**F06x · 676f 并列分析（剔退化资产）：Δ(FD−Random)=0.0pp p=1.0；Δ(FD−Static)=+30.6pp CI[+26.0,+35.1] p=8.1e-34** — consistent/active `✓✓✗✗✗✗✗`
- 源：`data/a5_676f_results.json`
  - ✓ `0.0` × 7 @ L311,384,548,776,842
  - ✓ `1.0` × 2 @ L776,842
  - ✗ `+30.6pp` × 0 @ L
  - ✗ `26.0, 35.1` × 0 @ L
  - ✗ `8.1\times10^{-34}` × 0 @ L
  - ✗ `24.0` × 0 @ L
  - ✗ `136/566` × 0 @ L
**F07x · 676f k 扫描（k=1..8）各档 Δ 与 p** — consistent/active `✗✗✗✗✗✓✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗✓✗✗✗`
- 源：`data/a5_676f_results.json`
  - ✗ `+33.0pp` × 0 @ L
  - ✗ `+33.0` × 0 @ L
  - ✗ `29.2, 36.9` × 0 @ L
  - ✗ `1.0\times10^{-56}` × 0 @ L
  - ✗ `33.0` × 0 @ L
  - ✓ `0.0` × 7 @ L311,384,548,776,842
  - ✗ `+30.7pp` × 0 @ L
  - ✗ `+30.7` × 0 @ L
  - ✗ `26.2, 35.3` × 0 @ L
  - ✗ `7.8\times10^{-35}` × 0 @ L
  - ✗ `45.1` × 0 @ L
  - ✗ `14.3` × 0 @ L
  - ✗ `+20.5pp` × 0 @ L
  - ✗ `+20.5` × 0 @ L
  - ✗ `16.5, 24.5` × 0 @ L
  - ✗ `2.1\times10^{-22}` × 0 @ L
  - ✗ `51.1` × 0 @ L
  - ✗ `30.6` × 0 @ L
  - ✗ `+24.0pp` × 0 @ L
  - ✗ `+24.0` × 0 @ L
  - ✗ `20.5, 27.5` × 0 @ L
  - ✗ `2.3\times10^{-41}` × 0 @ L
  - ✗ `54.6` × 0 @ L
  - ✗ `30.6` × 0 @ L
  - ✗ `+20.7pp` × 0 @ L
  - ✗ `+20.7` × 0 @ L
  - ✗ `17.3, 24.0` × 0 @ L
  - ✗ `1.2\times10^{-35}` × 0 @ L
  - ✗ `59.4` × 0 @ L
  - ✗ `38.7` × 0 @ L
  - ✗ `+11.3pp` × 0 @ L
  - ✗ `+11.3` × 0 @ L
  - ✗ `8.7, 13.9` × 0 @ L
  - ✗ `1.1\times10^{-19}` × 0 @ L
  - ✗ `60.1` × 0 @ L
  - ✗ `48.8` × 0 @ L
  - ✗ `+10.6pp` × 0 @ L
  - ✗ `+10.6` × 0 @ L
  - ✗ `8.1, 13.1` × 0 @ L
  - ✗ `1.7\times10^{-18}` × 0 @ L
  - ✗ `60.1` × 0 @ L
  - ✗ `49.5` × 0 @ L
  - ✗ `+0.0pp` × 0 @ L
  - ✗ `+0.0` × 0 @ L
  - ✓ `0.0, 0.0` × 2 @ L776,842
  - ✗ `1.000` × 0 @ L
  - ✗ `60.1` × 0 @ L
  - ✗ `60.1` × 0 @ L
**F08x.undefined_behavior · 676f 子组 undefined_behavior：Δ +58.1pp，BH-FDR p=1e-06，Bonferroni p=1e-06** — consistent/active `✗✗✗✗✓`
- 源：`data/a5_676f_results.json`
  - ✗ `+58.1pp` × 0 @ L
  - ✗ `+58.1` × 0 @ L
  - ✗ `1.0\times10^{-6}` × 0 @ L
  - ✗ `1.0\times10^{-6}` × 0 @ L
  - ✓ `43` × 1 @ L1111
  - 注：子组 p 必须报校正后值；未校正 p 不得单独宣称显著
**F08x.memory_safety · 676f 子组 memory_safety：Δ +46.9pp，BH-FDR p=1e-06，Bonferroni p=3e-06** — consistent/active `✗✗✗✗✓`
- 源：`data/a5_676f_results.json`
  - ✗ `+46.9pp` × 0 @ L
  - ✗ `+46.9` × 0 @ L
  - ✗ `1.0\times10^{-6}` × 0 @ L
  - ✗ `3.0\times10^{-6}` × 0 @ L
  - ✓ `49` × 1 @ L1305
  - 注：子组 p 必须报校正后值；未校正 p 不得单独宣称显著
**F08x.legacy · 676f 子组 legacy：Δ +36.2pp，BH-FDR p=5.6e-05，Bonferroni p=0.00017** — missing/active `✗✗✗✗✗`
- 源：`data/a5_676f_results.json`
  - ✗ `+36.2pp` × 0 @ L
  - ✗ `+36.2` × 0 @ L
  - ✗ `5.6\times10^{-5}` × 0 @ L
  - ✗ `1.7\times10^{-4}` × 0 @ L
  - ✗ `47` × 0 @ L
  - 注：子组 p 必须报校正后值；未校正 p 不得单独宣称显著
**F08x.stl · 676f 子组 stl：Δ +15.0pp，BH-FDR p=0.00017，Bonferroni p=0.00067** — consistent/active `✗✗✗✗✓`
- 源：`data/a5_676f_results.json`
  - ✗ `+15.0pp` × 0 @ L
  - ✗ `+15.0` × 0 @ L
  - ✗ `1.7\times10^{-4}` × 0 @ L
  - ✗ `6.7\times10^{-4}` × 0 @ L
  - ✓ `100` × 12 @ L106,168,285,630,1039,1079,1129,1130
  - 注：子组 p 必须报校正后值；未校正 p 不得单独宣称显著
**F08x.real_world · 676f 子组 real_world：Δ +29.5pp，BH-FDR p=0.00054，Bonferroni p=0.0027** — consistent/active `✗✗✗✗✓`
- 源：`data/a5_676f_results.json`
  - ✗ `+29.5pp` × 0 @ L
  - ✗ `+29.5` × 0 @ L
  - ✗ `5.4\times10^{-4}` × 0 @ L
  - ✗ `0.003` × 0 @ L
  - ✓ `44` × 1 @ L992
  - 注：子组 p 必须报校正后值；未校正 p 不得单独宣称显著
**F08x.optimization_sensitive · 676f 子组 optimization_sensitive：Δ +55.0pp，BH-FDR p=0.0018，Bonferroni p=0.011** — consistent/active `✗✗✗✗✓`
- 源：`data/a5_676f_results.json`
  - ✗ `+55.0pp` × 0 @ L
  - ✗ `+55.0` × 0 @ L
  - ✗ `0.002` × 0 @ L
  - ✗ `0.011` × 0 @ L
  - ✓ `20` × 3 @ L953,1018,1267
  - 注：子组 p 必须报校正后值；未校正 p 不得单独宣称显著
**F08x.conditional_trigger · 676f 子组 conditional_trigger：Δ +45.0pp，BH-FDR p=0.0061，Bonferroni p=0.043** — consistent/active `✗✗✗✗✓`
- 源：`data/a5_676f_results.json`
  - ✗ `+45.0pp` × 0 @ L
  - ✗ `+45.0` × 0 @ L
  - ✗ `0.006` × 0 @ L
  - ✗ `0.043` × 0 @ L
  - ✓ `20` × 3 @ L953,1018,1267
  - 注：子组 p 必须报校正后值；未校正 p 不得单独宣称显著
**F08x.concurrency · 676f 子组 concurrency：Δ +7.3pp，BH-FDR p=0.0095，Bonferroni p=0.086** — missing/active `✗✗✗✗✗`
- 源：`data/a5_676f_results.json`
  - ✗ `+7.3pp` × 0 @ L
  - ✗ `+7.3` × 0 @ L
  - ✗ `0.010` × 0 @ L
  - ✗ `0.086` × 0 @ L
  - ✗ `109` × 0 @ L
  - 注：子组 p 必须报校正后值；未校正 p 不得单独宣称显著
**F08x.language_semantics · 676f 子组 language_semantics：Δ +17.8pp，BH-FDR p=0.0095，Bonferroni p=0.086** — consistent/active `✗✗✗✗✓`
- 源：`data/a5_676f_results.json`
  - ✗ `+17.8pp` × 0 @ L
  - ✗ `+17.8` × 0 @ L
  - ✗ `0.010` × 0 @ L
  - ✗ `0.086` × 0 @ L
  - ✓ `45` × 2 @ L952,973
  - 注：子组 p 必须报校正后值；未校正 p 不得单独宣称显著
**F08x.embedded · 676f 子组 embedded：Δ +8.1pp，BH-FDR p=0.034，Bonferroni p=0.34** — consistent/active `✗✗✗✗✓`
- 源：`data/a5_676f_results.json`
  - ✗ `+8.1pp` × 0 @ L
  - ✗ `+8.1` × 0 @ L
  - ✗ `0.034` × 0 @ L
  - ✗ `0.344` × 0 @ L
  - ✓ `74` × 2 @ L417,551
  - 注：子组 p 必须报校正后值；未校正 p 不得单独宣称显著
**F08x.odr_link · 676f 子组 odr_link：Δ +6.7pp，BH-FDR p=1，Bonferroni p=1** — consistent/active `✗✗✗✗✓`
- 源：`data/a5_676f_results.json`
  - ✗ `+6.7pp` × 0 @ L
  - ✗ `+6.7` × 0 @ L
  - ✗ `1.000` × 0 @ L
  - ✗ `1.000` × 0 @ L
  - ✓ `15` × 3 @ L992,1146,1270
  - 注：子组 p 必须报校正后值；未校正 p 不得单独宣称显著
**F09x · 676f 子组检验族大小 11** — consistent/active `✓`
- 源：`data/a5_676f_results.json`
  - ✓ `11` × 6 @ L396,418,547,551,996,1038
**F10x.planted_false · 676f 真实缺陷 planted=false: FD 64.7% (22/34)，Δ +29.4pp** — missing/active `✗✗✗✗✗✗`
- 源：`data/a5_676f_results.json`
  - ✗ `64.7` × 0 @ L
  - ✗ `22/34` × 0 @ L
  - ✗ `+29.4pp` × 0 @ L
  - ✗ `14.1, 44.7` × 0 @ L
  - ✗ `2.0\times10^{-3}` × 0 @ L
  - ✗ `35.3` × 0 @ L
**F10x.planted_true · 676f planted=true: FD 53.9% (287/532)，Δ +23.7pp** — missing/active `✗✗✗✗✗✗`
- 源：`data/a5_676f_results.json`
  - ✗ `53.9` × 0 @ L
  - ✗ `287/532` × 0 @ L
  - ✗ `+23.7pp` × 0 @ L
  - ✗ `20.1, 27.3` × 0 @ L
  - ✗ `2.4\times10^{-38}` × 0 @ L
  - ✗ `30.3` × 0 @ L
**F11x · 676f 资产诊断：8 资产各自 catch 率；wunsequenced/compile-time 100% unknown（退化）** — consistent/active `✗✗✗✓✓✓✗✗✗✗✗✗✓✗✗✗✗✗✗✓✓✓`
- 源：`data/a5_676f_results.json`
  - ✗ `35.1` × 0 @ L
  - ✗ `399` × 0 @ L
  - ✗ `0.88` × 0 @ L
  - ✓ `0.0` × 7 @ L311,384,548,776,842
  - ✓ `0` × 135 @ L13,162,163,167,301,302,303,304
  - ✓ `100` × 12 @ L106,168,285,630,1039,1079,1129,1130
  - ✗ `12.6` × 0 @ L
  - ✗ `143` × 0 @ L
  - ✗ `15.0` × 0 @ L
  - ✗ `170` × 0 @ L
  - ✗ `3.34` × 0 @ L
  - ✗ `0.9` × 0 @ L
  - ✓ `10` × 6 @ L304,945,953,991,995,1322
  - ✗ `22.4` × 0 @ L
  - ✗ `255` × 0 @ L
  - ✗ `0.88` × 0 @ L
  - ✗ `23.6` × 0 @ L
  - ✗ `268` × 0 @ L
  - ✗ `0.88` × 0 @ L
  - ✓ `0.0` × 7 @ L311,384,548,776,842
  - ✓ `0` × 135 @ L13,162,163,167,301,302,303,304
  - ✓ `100` × 12 @ L106,168,285,630,1039,1079,1129,1130
  - 注：退化资产是 A5 主/并列分析差异的唯一来源
**G01x · 676g 总盘：n=1147，catch 707，miss 440，盲区比 38.4%** — consistent/active `✓✓✓✗`
- 源：`data/blindspot_676g_stats.json`
  - ✓ `1147` × 7 @ L270,289,544,626,972,1326
  - ✓ `707` × 1 @ L972
  - ✓ `440` × 1 @ L972
  - ✗ `38.4` × 0 @ L
**G02x · 676g 互补性：6 资产并集 61.6%，最佳单资产 35.6%** — consistent/active `✗✓✗`
- 源：`data/blindspot_676g_stats.json`
  - ✗ `61.6` × 0 @ L
  - ✓ `707` × 1 @ L972
  - ✗ `35.6` × 0 @ L
**G03x · 676g 逐资产覆盖率（asan/ubsan/tsan/compiler-warn/cross-compile/linker）** — consistent/active `✗✗✗✗✗✗✓✓`
- 源：`data/blindspot_676g_stats.json`
  - ✗ `35.6` × 0 @ L
  - ✗ `23.5` × 0 @ L
  - ✗ `22.9` × 0 @ L
  - ✗ `12.5` × 0 @ L
  - ✗ `10.6` × 0 @ L
  - ✗ `0.9` × 0 @ L
  - ✓ `0.0` × 7 @ L311,384,548,776,842
  - ✓ `0.0` × 7 @ L311,384,548,776,842
**G04x · 676g 按 planted：true 41.0% [38.0, 44.1]；false 21.6% [13.8, 32.3]** — consistent/active `✗✗✗✗✓`
- 源：`data/blindspot_676g_stats.json`
  - ✗ `41.0` × 0 @ L
  - ✗ `38.0, 44.1` × 0 @ L
  - ✗ `21.6` × 0 @ L
  - ✗ `13.8, 32.3` × 0 @ L
  - ✓ `74` × 2 @ L417,551
**G05x · 676g 盲区分带：18 个类型 >50% 盲；类型总数 70** — consistent/active `✓✓✓`
- 源：`data/blindspot_676g_stats.json`
  - ✓ `18` × 3 @ L289,1017,1305
  - ✓ `70` × 5 @ L289,792,1006,1017,1110
  - ✓ `50` × 8 @ L288,791,1005,1012,1248,1249,1305,1324
**G06x · 676g TSan 稳定性：3/180 不稳定（1.7%）** — consistent/active `✓✗✗`
- 源：`data/blindspot_676g_stats.json`
  - ✓ `3` × 26 @ L131,189,540,550,574,618,727,747
  - ✗ `180` × 0 @ L
  - ✗ `1.7` × 0 @ L
**E01 · clang-analyzer holdout 48.8% (20/41) p=1.2e-4** — missing/active `✗✗✗`
- 源：`data/673e_comparison_stats.json`
  - ✗ `48.8` × 0 @ L
  - ✗ `20/41` × 0 @ L
  - ✗ `1.2\times10^{-4}` × 0 @ L
**E02 · cppcheck holdout 41.5% (17/41) p=1.5e-5** — missing/active `✗✗✗`
- 源：`data/673e_comparison_stats.json`
  - ✗ `41.5` × 0 @ L
  - ✗ `17/41` × 0 @ L
  - ✗ `1.5\times10^{-5}` × 0 @ L
**E03 · cppcheck corpus 54.7% (35/64) p=0.38331031799316406** — missing/active `✗✗✗`
- 源：`data/673e_comparison_stats.json`
  - ✗ `54.7` × 0 @ L
  - ✗ `35/64` × 0 @ L
  - ✗ `0.383` × 0 @ L
**E03b · cppcheck corpus Δ +7.8pp CI[-6.1, 21.7]（CI 跨 0 ⇒ tie）** — missing/active `✗✗✗`
- 源：`data/673e_comparison_stats.json`
  - ✗ `+7.8pp` × 0 @ L
  - ✗ `-6.1, 21.7` × 0 @ L
  - ✗ `(13,8)` × 0 @ L
**E04 · E9 附录 StrictA 对照 FPR 9.1% (1/11)** — missing/active `✗✗`
- 源：`data/673e_comparison_stats.json`
  - ✗ `9.1\% (1/11)` × 0 @ L
  - ✗ `1/11` × 0 @ L
  - 注：控制组 n=11（= holdout 对照样本数）；分母必须是 11
**E05 · E9 附录 cppcheck 主口径 对照 FPR 9.1% (1/11)** — missing/active `✗✗`
- 源：`data/673e_comparison_stats.json`
  - ✗ `9.1\% (1/11)` × 0 @ L
  - ✗ `1/11` × 0 @ L
  - 注：控制组 n=11（= holdout 对照样本数）；分母必须是 11
**E06 · E9 附录：holdout Δ(FD−StrictA) +34.1pp [19.6, 48.7]，对子 (14,0)** — missing/active `✗✗✗`
- 源：`data/673e_comparison_stats.json`
  - ✗ `+34.1pp` × 0 @ L
  - ✗ `19.6, 48.7` × 0 @ L
  - ✗ `(14,0)` × 0 @ L
**E07 · E9 附录：corpus StrictA 34.4% (22/64)，Δ +28.1pp 对子 (23,5)，p=9.1e-4** — missing/active `✗✗✗✗✗`
- 源：`data/673e_comparison_stats.json`
  - ✗ `34.4` × 0 @ L
  - ✗ `22/64` × 0 @ L
  - ✗ `+28.1pp` × 0 @ L
  - ✗ `(23,5)` × 0 @ L
  - ✗ `9.1\times10^{-4}` × 0 @ L
**E08 · E9 附录：corpus 分层 FD/ct/cp（sanitizer 29/17/26；compiler-warn 9/5/8；cross-compile 2/0/1）** — consistent/active `✗✗✗✓✗✗✗`
- 源：`data/673e_comparison_stats.json`
  - ✗ `29 / 17 / 26` × 0 @ L
  - ✗ `9 / 5 / 8` × 0 @ L
  - ✗ `2 / 0 / 1` × 0 @ L
  - ✓ `12` × 14 @ L398,407,409,415,708,709,711,712
  - ✗ `FD 29 vs clang-analyzer 17 / cppcheck 26` × 0 @ L
  - ✗ `FD 9 / cppcheck 8` × 0 @ L
  - ✗ `2 / 0 / 1` × 0 @ L
**E10 · E9 附录：clang-tidy 主口径 holdout 100% recall / 100% FPR（零区分度 ⇒ 该口径被弃用）** — consistent/active `✓✓✓✓✗✗`
- 源：`data/673e_comparison_stats.json`
  - ✓ `100.0` × 1 @ L285
  - ✓ `100` × 12 @ L106,168,285,630,1039,1079,1129,1130
  - ✓ `100.0` × 1 @ L285
  - ✓ `100` × 12 @ L106,168,285,630,1039,1079,1129,1130
  - ✗ `41/41` × 0 @ L
  - ✗ `11/11` × 0 @ L
**E09 · E9 附录：8 个反向对（工具 catch / FD miss）** — consistent/active `✓`
- 源：`data/673e_comparison_stats.json`
  - ✓ `8` × 13 @ L268,289,313,399,451,544,870,881
**F01 · 外部锚点子集 A（准则原文）28.6% (10/35) CI[14.6,46.3]** — missing/active `✗✗✗`
- 源：`data/external_anchor_reveal_672j.json`
  - ✗ `28.6` × 0 @ L
  - ✗ `10/35` × 0 @ L
  - ✗ `14.6, 46.3` × 0 @ L
**F02 · 外部锚点子集 B（UB 片段重建）80.0% (12/15)** — missing/active `✗✗`
- 源：`data/external_anchor_reveal_672j.json`
  - ✗ `80.0` × 0 @ L
  - ✗ `12/15` × 0 @ L
**F03 · 外部锚点合计 44.0% (22/50)；扫描规则 87** — consistent/active `✗✗✓✓✓✓✓✗`
- 源：`data/external_anchor_reveal_672j.json`
  - ✗ `44.0` × 0 @ L
  - ✗ `22/50` × 0 @ L
  - ✓ `22` × 3 @ L994,1015,1306
  - ✓ `50` × 8 @ L288,791,1005,1012,1248,1249,1305,1324
  - ✓ `87` × 1 @ L1146
  - ✓ `35` × 7 @ L951,952,1036,1109,1146,1252
  - ✓ `15` × 3 @ L992,1146,1270
  - ✗ `11/60` × 0 @ L
**F04 · LLM 臂：GLM-4 12/12 vs FD 6/12；对照误报 4/8 = 50%** — missing/active `✗✗✗✗✗`
- 源：`data/experiments/llm_arm_672i.json`
  - ✗ `12/12` × 0 @ L
  - ✗ `6/12` × 0 @ L
  - ✗ `4/8` × 0 @ L
  - ✗ `50.0` × 0 @ L
  - ✗ `50.0` × 0 @ L
  - 注：FD 的 6/12 由 fd_detect_rate_pct=50.0% × llm_n 重算得到
**F05 · LLM 臂配对 b/c = (0,6)，p=0.03125** — missing/active `✗✗`
- 源：`data/experiments/llm_arm_672i.json`
  - ✗ `0,6` × 0 @ L
  - ✗ `0.031` × 0 @ L
**G01 · 变异（core）110/114 = 96.5%** — missing/active `✗✗✗`
- 源：`data/656_mutation_report.json`
  - ✗ `110/114` × 0 @ L
  - ✗ `96.5` × 0 @ L
  - ✗ `91.3, 99.0` × 0 @ L
**G02 · 变异（all-scope）130/159 = 81.8%** — missing/active `✗✗`
- 源：`data/656_mutation_report_all.json`
  - ✗ `130/159` × 0 @ L
  - ✗ `81.8` × 0 @ L
**G03 · 缺陷重注入 6/6 = 100%；total 15；软覆盖 12/15** — consistent/active `✗✗✓`
- 源：`data/defect_injection_661.json`
  - ✗ `6/6` × 0 @ L
  - ✗ `12/15` × 0 @ L
  - ✓ `15` × 3 @ L992,1146,1270
**H01 · 样本量：独立两比例 0.35→0.50 ⇒ n=170** — missing/active `✗✗`
- 源：`Cohen arcsine h + Connor 配对；p1=0.35,p2=0.5,psi=None, α=0.05, power=0.8, recomputed=169.09`
  - ✗ `170` × 0 @ L
  - ✗ `170 (holdout)` × 0 @ L
**H02 · 样本量：独立两比例 0.35→0.55 ⇒ n=96** — consistent/active `✓✗`
- 源：`Cohen arcsine h + Connor 配对；p1=0.35,p2=0.55,psi=None, α=0.05, power=0.8, recomputed=95.77`
  - ✓ `96` × 1 @ L1146
  - ✗ `96 (holdout)` × 0 @ L
**H03 · 样本量：独立两比例 0.35→0.45 ⇒ n=376** — consistent/active `✓✗`
- 源：`Cohen arcsine h + Connor 配对；p1=0.35,p2=0.45,psi=None, α=0.05, power=0.8, recomputed=375.27`
  - ✓ `376` × 1 @ L970
  - ✗ `376 (holdout)` × 0 @ L
**H04 · 样本量：配对 ψ=0.3 ⇒ n=103** — missing/active `✗✗`
- 源：`Cohen arcsine h + Connor 配对；p1=0.35,p2=0.5,psi=0.3, α=0.05, power=0.8, recomputed=102.26`
  - ✗ `103` × 0 @ L
  - ✗ `103 (holdout)` × 0 @ L
**H05 · 样本量：配对 ψ=0.4 ⇒ n=138** — missing/active `✗✗`
- 源：`Cohen arcsine h + Connor 配对；p1=0.35,p2=0.5,psi=0.4, α=0.05, power=0.8, recomputed=137.15`
  - ✗ `138` × 0 @ L
  - ✗ `138 (holdout)` × 0 @ L
**H06 · 样本量：配对 ψ=0.5 ⇒ n=173** — missing/active `✗✗`
- 源：`Cohen arcsine h + Connor 配对；p1=0.35,p2=0.5,psi=0.5, α=0.05, power=0.8, recomputed=172.04`
  - ✗ `173` × 0 @ L
  - ✗ `173 (holdout)` × 0 @ L
**K01 · tab:e3 第 656 行 “变异 core 62.5% (30/48)”：无任何现存产物可复现** — missing/unpinned_no_artifact `✗✗`
- 源：`data/656_mutation_report*.json 现存值为 110/114 与 130/159；全仓扫描 `30/48` 无产物命中（唯一产出是更早被覆盖的报告）`
  - ✗ `62.5` × 0 @ L
  - ✗ `30/48` × 0 @ L
  - 注：论文必须显式标注该行为 un-pinned 历史值，不得当作可复现结果（676h 已加脚注）
**K02 · tab:e3 第 665 行 “66.7%（旧 -O1 单档口径）”：源为已退役草稿口径** — missing/unpinned_retired_caliber `✗`
- 源：`仅能追溯到 research/paper_v0.4.md 与 data/669_caliber_report.json::doc_sightings；对应 -O1 单档产物已被 665/668 双档口径取代`
  - ✗ `66.7` × 0 @ L
  - 注：该值口径已退休，只能作为“当时口径下读到的数”引用
**I01 · Static holdout 1/41 CI ⇒ [0.1, 12.9]** — missing/active `✗`
- 源：`python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(1,41)])"`
  - ✗ `0.1, 12.9` × 0 @ L
  - 注：用仓库自带 tools/stat_bounds.py::cp_interval 现算
**I02 · Random† holdout 4/41 CI ⇒ [2.7, 23.1]** — missing/active `✗`
- 源：`python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(4,41)])"`
  - ✗ `2.7, 23.1` × 0 @ L
  - 注：用仓库自带 tools/stat_bounds.py::cp_interval 现算
**I03 · FD holdout 34/41 CI ⇒ [67.9, 92.8]** — missing/active `✗`
- 源：`python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(34,41)])"`
  - ✗ `67.9, 92.8` × 0 @ L
  - 注：用仓库自带 tools/stat_bounds.py::cp_interval 现算
**I04 · Caliber B holdout 34/42 CI ⇒ [65.9, 91.4]** — missing/active `✗`
- 源：`python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(34,42)])"`
  - ✗ `65.9, 91.4` × 0 @ L
  - 注：用仓库自带 tools/stat_bounds.py::cp_interval 现算
**I05 · Static corpus 11/64 CI ⇒ [8.9, 28.7]** — missing/active `✗`
- 源：`python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(11,64)])"`
  - ✗ `8.9, 28.7` × 0 @ L
  - 注：用仓库自带 tools/stat_bounds.py::cp_interval 现算
**I06 · Random† corpus 14/64 CI ⇒ [12.5, 34.0]** — missing/active `✗`
- 源：`python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(14,64)])"`
  - ✗ `12.5, 34.0` × 0 @ L
  - 注：用仓库自带 tools/stat_bounds.py::cp_interval 现算
**I07 · FD corpus 40/64 CI ⇒ [49.5, 74.3]** — missing/active `✗`
- 源：`python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(40,64)])"`
  - ✗ `49.5, 74.3` × 0 @ L
  - 注：用仓库自带 tools/stat_bounds.py::cp_interval 现算
**I08 · Caliber B corpus 40/73 CI ⇒ [42.7, 66.5]** — missing/active `✗`
- 源：`python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(40,73)])"`
  - ✗ `42.7, 66.5` × 0 @ L
  - 注：用仓库自带 tools/stat_bounds.py::cp_interval 现算
**I09 · Caliber C corpus 40/76 CI ⇒ [40.8, 64.2]** — missing/active `✗`
- 源：`python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(40,76)])"`
  - ✗ `40.8, 64.2` × 0 @ L
  - 注：用仓库自带 tools/stat_bounds.py::cp_interval 现算
**I10 · 对照 FPR 0/11 CI ⇒ [0.0, 28.5]** — missing/active `✗`
- 源：`python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(0,11)])"`
  - ✗ `0.0, 28.5` × 0 @ L
  - 注：用仓库自带 tools/stat_bounds.py::cp_interval 现算
**I11 · corpus 分层 sanitizer 29/34 CI ⇒ [68.9, 95.0]** — retired/superseded:689重构 `✗`
- 源：`python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(29,34)])"`
  - ✗ `68.9, 95.0` × 0 @ L
  - 注：用仓库自带 tools/stat_bounds.py::cp_interval 现算；论文当前未打印该区间 ⇒ 记为 not_printed，不作不一致
**I12 · corpus 分层 compiler-warn 9/18 CI ⇒ [26.0, 74.0]** — retired/superseded:689重构 `✗`
- 源：`python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(9,18)])"`
  - ✗ `26.0, 74.0` × 0 @ L
  - 注：用仓库自带 tools/stat_bounds.py::cp_interval 现算；论文当前未打印该区间 ⇒ 记为 not_printed，不作不一致
**I13 · corpus 分层 cross-compile 2/12 CI ⇒ [2.1, 48.4]** — retired/superseded:689重构 `✗`
- 源：`python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(2,12)])"`
  - ✗ `2.1, 48.4` × 0 @ L
  - 注：用仓库自带 tools/stat_bounds.py::cp_interval 现算；论文当前未打印该区间 ⇒ 记为 not_printed，不作不一致
**I14 · 缺陷重注入 6/6 CI ⇒ [54.1, 100.0]** — retired/superseded:689重构 `✗`
- 源：`python -c "import sys;sys.path.insert(0,'tools');from stat_bounds import cp_interval;print(*[round(x*100,1) for x in cp_interval(6,6)])"`
  - ✗ `54.1, 100.0` × 0 @ L
  - 注：用仓库自带 tools/stat_bounds.py::cp_interval 现算；论文当前未打印该区间 ⇒ 记为 not_printed，不作不一致
**D03 · A5 矩阵 105×8 = 840 次 detect** — consistent/superseded_by_676f `✗✗✓`
- 源：`data/experiments/a5_673p.json`
  - ✗ `105` × 0 @ L
  - ✗ `840` × 0 @ L
  - ✓ `8` × 13 @ L268,289,313,399,451,544,870,881
**A19 · ±5pp 缺口：holdout 还差 195，corpus 还差 314** — consistent/active `✓✗`
- 源：`sample_size_672k.±5pp.n − 当前可测 n`
  - ✓ `195` × 1 @ L970
  - ✗ `314` × 0 @ L
**D11 · clone-aware 重切分 Δ +23.0~+26.7pp（677b，逐 split 为 +23.02/+25.70）** — missing/active `✗✗`
- 源：`current_numbers.a5_experiments.clone_aware_677b ← data/677b_a5_results_family_random.json / _family_stratified.json`
  - ✗ `23.02` × 0 @ L
  - ✗ `25.70` × 0 @ L
**D12 · cluster bootstrap 有效 n≈133–140（677b，design effect ≈4.1–4.3）** — consistent/active `✗✓`
- 源：`current_numbers.a5_experiments.clone_aware_677b ← data/677b_cluster_bootstrap.json`
  - ✗ `133` × 0 @ L
  - ✓ `140` × 5 @ L285,969,1294,1295
**D13 · 非退化池选择效应 +11.31pp（677c，k=1，p=6.02e-08）** — missing/active `✗`
- 源：`current_numbers.a5_experiments.nondegenerate_pool_677c ← data/677c_a5_nondegenerate_results.json`
  - ✗ `11.31` × 0 @ L
**D14 · 退化资产对均值的贡献 ≈+12.81pp（677c）** — missing/active `✗`
- 源：`current_numbers.a5_experiments.nondegenerate_pool_677c ← data/677c_a5_nondegenerate_results.json`
  - ✗ `12.81` × 0 @ L
**Z01 · 689 TOST：±10pp 未过，90% CI [-10.61, 5.52]pp，p_TOST=0.064** — missing/active `✗✗✗`
- 源：`current_numbers.reframed_689.equivalence_tost ← data/689_equivalence_test.json`
  - ✗ `-10.61` × 0 @ L
  - ✗ `5.52` × 0 @ L
  - ✗ `0.064` × 0 @ L
**E02 · 689 TOST 最小通过 margin 10.61pp（deff 校正 11.67pp）** — missing/active `✗✗`
- 源：`data/689_equivalence_test.json`
  - ✗ `10.61` × 0 @ L
  - ✗ `11.67` × 0 @ L
**E03 · 689 标准化：正向 -17.92pp（R_syn_std=77.01%），反向 +1.70pp，类型级 -13.52pp** — missing/active `✗✗✗✗`
- 源：`current_numbers.reframed_689.standardized_analysis ← data/689_standardized_analysis.json`
  - ✗ `-17.92` × 0 @ L
  - ✗ `77.01` × 0 @ L
  - ✗ `1.70` × 0 @ L
  - ✗ `-13.52` × 0 @ L
**E04 · 689 环境：真实 59.09%→23.64%（-35.45pp，Δunknown=0），clang↔g++ 93.5%** — missing/active `✗✗✗✗`
- 源：`current_numbers.reframed_689.environment_metrics ← data/689_environment_metrics.json`
  - ✗ `59.09` × 0 @ L
  - ✗ `23.64` × 0 @ L
  - ✗ `35.45` × 0 @ L
  - ✗ `93.5` × 0 @ L
**Z11 · 691 机制级：Pool A k=1 +11.31pp (p=6.0e-8)；k=2/k=3 +7.42pp；k=4 0.00pp** — consistent/active `✗✓✗✓`
- 源：`current_numbers.reframed_691.mechanism_level_poolA_vs_single_random ← data/677c_a5_nondegenerate_results.json`
  - ✗ `11.31` × 0 @ L
  - ✓ `6.0` × 1 @ L540
  - ✗ `7.42` × 0 @ L
  - ✓ `0.00` × 5 @ L1035,1036,1037,1129,1130
**Z12 · 691 四个 κ（AI 自一致）：0.727 / 0.789 / 0.437 / 0.157** — missing/active `✗✗✗✗`
- 源：`current_numbers.reframed_691.label_kappa_ai_self_consistency ← data/682_kappa.json`
  - ✗ `0.727` × 0 @ L
  - ✗ `0.789` × 0 @ L
  - ✗ `0.437` × 0 @ L
  - ✗ `0.157` × 0 @ L
**Z13 · 691 治理计数：452 ledger 事件 / 67 规则 / rules_sha256 v1.0.0** — missing/active `✗✗`
- 源：`current_numbers.reframed_691.governance`
  - ✗ `452` × 0 @ L
  - ✗ `67` × 0 @ L
**Z14 · 691 池计数：Pool B ≡ Pool C（同一六资产集）；9 个不同 (池,k) 块 / 14 块实例** — consistent/active `✓✓✓`
- 源：`current_numbers.reframed_691.pools ← data/677c_asset_pools.json + 677c_evolution_operator_results.json`
  - ✓ `2` × 46 @ L3,130,151,167,302,305,328,432
  - ✓ `9` × 6 @ L650,874,994,1015,1096,1110
  - ✓ `14` × 4 @ L793,1006,1307,1322
