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
python -m pip install -r requirements.txt   # pytest is the only third-party requirement
bash Scripts/verify_environment.sh --report # environment health check (reports, never blocks)
```

**Line endings.** The shell scripts are pinned to LF by `.gitattributes`
(`*.sh text eol=lf`), so they stay executable on Bash-under-Windows too. If you
copied files by hand instead of cloning and see
`set: pipefail: invalid option name` / `$'\r': command not found`, your copy has
CRLF line endings.

**Every command below was executed from a clean clone**; the measured exit code of
each step is recorded in the package's own reproducibility log (see
`REPRODUCTION_LOG.md`).


## 2. One-shot reproduction

```bash
# numbers of record, paper 1 (empirical audit; exits 0 iff all required numbers trace out)
python tools/verify_paper_numbers.py \
    --tex paper/paper1/queyi_neurips2027_v1.1.tex \
    --tex-extra paper/paper1/supplementary/paper_appendix_extras.tex \
    --out-json data/paper1_numbers.json --out-md data/paper1_numbers_report.md

# paper 2 (theory / boundaries): the same scanner can point --tex at paper 2 and
# extracts/classifies its number tokens, but its "required numbers" checklist is
# hard-wired to paper 1's empirical arms, so paper 2 exits non-zero by design
# (it reports 44 consistent mappings + the paper-1 numbers that do not appear).
# Treat the emitted JSON/MD as an extraction report, not a pass/fail gate.
python tools/verify_paper_numbers.py \
    --tex paper/paper2/paper2_measurement_drift.tex \
    --out-json data/paper2_numbers.json --out-md data/paper2_numbers_report.md

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
python ../../tools/figure_data_check_670c2.py                       # figure provenance
python ../../tools/paper_sync_check_670c2.py                        # see NOTE below

# Paper 2
cd paper/paper2 && tectonic paper2_measurement_drift.tex --keep-logs # main text <= 9 pages
python ../../tools/test_axiom_independence.py                       # 700-A classification
python ../../tools/asset_capabilities.py --validate                 # P1/P2/P3 on frozen matrices
python ../../tools/sample_size_calculator.py --type II               # 700-C sample sizes
```

> **NOTE — `paper_sync_check_670c2.py` is NOT_APPLICABLE in this package.**
> It cross-checks the LaTeX sources against a **Markdown master** (`research/paper_shturl.md`)
> that belongs to the writing repository and is *not* part of the anonymous package.
> The script therefore prints `NOT_APPLICABLE` and exits 0 instead of raising
> `FileNotFoundError`. Reported for transparency, not as a passing check.


## 5. Known limits of this package

- The **Docker recipe** (`docker/`) is provided but was **not build-tested** by the authors.
- The **human annotation package** (`data/annotation_package/`) is de-identified and shipped, but
  **unexecuted**: human IAA is 0.
- The **full detection chain** (running asan/ubsan/tsan) needs the authors' WSL + MinGW toolchain and
  is **not** part of this package; only the frozen matrices and their analyses are.
- Files under `data/frozen_matrix/` are **read-only sources of record**. Tools fail closed rather
  than silently recomputing them.
- **`Scripts/reproduce_all.sh` completes (exit 0), but two of its stages are *registered as
  skipped*** — they are written to `<out>/99_skipped.txt` and surfaced in the generated report,
  never silently passed:
  * **S2 — number re-computation via `docker/paper/run_all.sh`** needs four tools that are *not*
    shipped in this package (`tools/path_config_625.py`, `tools/stats_672k.py`,
    `tools/fix_676m_schema.py`, `tools/audit_676k_integrity.py`) plus inputs under
    `data/experiments/`. That chain belongs to the writing repository. The paper numbers are still
    covered by `tools/verify_paper_numbers.py` (§2) and by S3.
  * **S3 — `fast_gate`** bundles three writing-repository gates (`tools/run_658_gate.py`,
    `tools/run_669d_gate.py`, `tools/guard_rerun_671a.py`) that are not shipped; the stage falls
    back to `pytest tests/ -q`, which passes (18/18).
- **Line endings are part of the contract.** `data/frozen_matrix/**` and
  `data/693_data_manifest.sha256` are pinned to `-text` in `.gitattributes`. Without that pin,
  `core.autocrlf=true` rewrites **31 of the 49** frozen artifacts on clone (measured:
  `683_real_world_detection_matrix.json` 247,619 B → 254,404 B) and every sha256 anchor fails.
  Clone with `git`; do not copy the files by hand.
