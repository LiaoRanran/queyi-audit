# Reproduction guide

This package reproduces every number in both papers **from frozen artifacts**. No detector is
re-run: the frozen matrices in `data/frozen_matrix/` are the sources of record, and all tools are
read-only with respect to them.

## 1. Environment

| Component | Version used by the authors | Required? |
|---|---|---|
| Python | 3.11+ (3.13 used for artifact generation) | yes |
| `tectonic` | 0.17.0 (XeTeX + BibTeX + xdvipdfmx) | for compiling the papers |
| `git` | any recent | yes |
| (full detection chain) | WSL Ubuntu 24.04 + g++ 13.3 + MinGW g++ 13.1 | **not needed** to reproduce paper numbers |

Setup:

```bash
python -m pip install -r requirements.txt   # if present; otherwise the stdlib suffices
bash Scripts/verify_environment.sh --report # environment health check (reports, never blocks)
```

## 2. One-shot reproduction

```bash
# numbers of record, both papers
python tools/verify_paper_numbers.py \
    --tex paper/paper1/queyi_neurips2027_v1.1.tex \
    --tex-extra paper/paper1/supplementary/paper_appendix_extras.tex \
    --out-json data/paper1_numbers.json --out-md data/paper1_numbers_report.md

# integrity of the frozen artifacts
python tools/gen_693_manifest.py --check

# tests
python -m pytest tests/ -q
```

`Scripts/reproduce_all.sh` chains environment check → integrity → number recomputation → gates.

## 3. Expected outputs (headline numbers)

Paper 1 (empirical audit, 1,147-sample × 8-asset frozen matrix):

| Quantity | Value |
|---|---|
| Eight-asset OR detection | 61.6% (707/1147) |
| All-asset blind spot | 38.4% (440/1147) |
| Defect types with >50% blindness | 13 of 34 |
| Real-world benchmark (110 reconstructed CVEs) | 59.09% (65/110) |
| A5 $k{=}4$ FD vs. Random | +24.03pp (full pool); **0.00pp** degenerate-free |

Paper 2 (boundaries):

| Quantity | Value |
|---|---|
| Genuine axioms (of seven) | 2 (A2 removal monotonicity, A5 super-additivity) |
| Model domain | 4,096 structures × 7 aggregations |
| Type I / Type II required $n$ | 849 / 17 |
| Type III / Type IV required $n$ | $\infty$ (paired design powerless) |
| Residual unrecoverable verdicts | asan 30.04%, ubsan 21.38%, tsan 21.73% |
| Anti-drift score (before → after three zero-cost fixes) | 53.05 → 66.67 |

## 4. Reproducing each paper

```bash
# Paper 1
cd paper/paper1 && tectonic queyi_neurips2027_v1.1.tex --keep-logs   # main text <= 9 pages
python ../../tools/paper_quality_gate_670c2.py                      # 6/6 gate
python ../../tools/paper_sync_check_670c2.py                        # markdown <-> LaTeX sync
python ../../tools/figure_data_check_670c2.py                       # figure provenance

# Paper 2
cd paper/paper2 && tectonic paper2_measurement_drift.tex --keep-logs # main text <= 9 pages
python ../../tools/test_axiom_independence.py                       # 700-A classification
python ../../tools/asset_capabilities.py --validate                 # P1/P2/P3 on frozen matrices
python ../../tools/sample_size_calculator.py --type II               # 700-C sample sizes
```

## 5. Known limits of this package

- The **Docker recipe** (`docker/`) is provided but was **not build-tested** by the authors.
- The **human annotation package** (`data/annotation_package/`) is de-identified and shipped, but
  **unexecuted**: human IAA is 0.
- The **full detection chain** (running asan/ubsan/tsan) needs the authors' WSL + MinGW toolchain and
  is **not** part of this package; only the frozen matrices and their analyses are.
- Files under `data/frozen_matrix/` are **read-only sources of record**. Tools fail closed rather
  than silently recomputing them.
