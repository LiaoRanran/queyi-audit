# Queyi Audit — a reproducibility package for auditing the evaluator

**30-second version.** Clone it, run one command, read the exit code:

```bash
git clone <this-repo> queyi-audit && cd queyi-audit
python tools/verify_paper_numbers.py \
    --tex paper/paper1/queyi_neurips2027_v1.1.tex \
    --tex-extra paper/paper1/supplementary/paper_appendix_extras.tex
# -> "检察 124 条；missing 0；consistent 112"   and exit code 0
```

That single command re-derives the headline numbers of paper 1 from the **frozen matrices** in
`data/frozen_matrix/`, read-only — no detector is re-run, nothing is written except a report.
`REPRODUCTION_LOG.md` records the **measured** exit code of every other command in
`REPRODUCTION.md`, including the one that is non-zero on purpose. If you only want to find a
defect in this package, start there: it has already found ten (listed in `REPRODUCTION_LOG.md`).

> **Anonymous submission package.** This repository accompanies two papers on *measurement drift* in
> software-verification evaluation. It contains the frozen artifacts, the analysis tools, and the
> LaTeX sources needed to reproduce every number. It is distributed under Apache-2.0 and is
> **double-blind**: no author name, affiliation, e-mail or source-repository identifier appears
> in its files, commit messages or URLs; build-host temporary paths inside the frozen matrices
> were deliberately left byte-identical so that every sha256 anchor stays verifiable.

## What this is

Two companion papers ask whether an apparently convincing evaluation result survives an audit of the
evaluator that produced it:

- **Paper 1 — *Caliber Drift and Capability Boundaries: An Audit Protocol for Software-Verification
  Evaluation*** (empirical audit of one C/C++ verification apparatus). `paper/paper1/`
- **Paper 2 — *The Boundary of Evaluator Auditing: Identifiability, Correctability and Sample
  Complexity of Measurement Drift*** (the theoretical boundaries). `paper/paper2/`

Nothing here was re-measured for the papers: every headline number is recomputed from **frozen
detection matrices** (`data/frozen_matrix/`) by the tools in `tools/`.

## Core findings

- **Structural (passive) Goodhart.** A large class of evaluation failures needs **no optimisation
  pressure**: the number moves because the *caliber* of measurement moved, while capability did not.
- **Only two of seven axioms do work.** Over 4,096 coverage structures × 7 aggregations, idempotence,
  commutativity, non-invertibility and observability-stratification are **theorems**; only removal
  monotonicity (A2) and super-additivity (A5) are genuine axioms. The system is **incomplete**: label
  drift (Type III) cannot be expressed — a missing **A8** is registered.
- **Three boundaries.** Structural vs. real drift is **not identifiable** from paired data alone
  (point-identified under nesting); post-hoc repair works **only** on the post-measurement layer
  (acquisition-layer drift must be re-measured, residual error up to 30.0%); and audit cost is
  governed by the **discordance rate**, not the effect size — two of four drift types are
  undetectable by a paired design at any sample size ($n=\infty$).
- **Measured anti-drift improvement at ~zero cost.** Declaring the asset pool without zero-yield
  components, accounting for untested samples, and declaring the aggregation rule leave the detection
  rate unchanged while raising the measured anti-drift score from 53.05 to 66.67.
- **Real-world anchor.** A 110-item reconstructed CVE benchmark (NVD-verified) detects at 59.09%.

## Quick start

```bash
git clone <this-repo> queyi-audit && cd queyi-audit

# 1) number traceability (fail-closed, read-only)
python tools/verify_paper_numbers.py --tex paper/paper1/queyi_neurips2027_v1.1.tex \
    --out-json data/paper1_numbers.json --out-md data/paper1_numbers_report.md

# 2) tests (the 707 landing tools)
python -m pytest tests/ -q

# 3) compile both papers (tectonic)
cd paper/paper1 && tectonic queyi_neurips2027_v1.1.tex
cd ../paper2 && tectonic paper2_measurement_drift.tex
```

See [`REPRODUCTION.md`](REPRODUCTION.md) for environments, one-shot commands and the expected
outputs (headline numbers).

## Repository layout

```
queyi-audit/
├── paper/paper1/              # paper 1 (tex + bib + cover letter + supplementary/)
├── paper/paper2/              # paper 2 (tex + bib + cover letter + abstract)
├── data/frozen_matrix/        # frozen detection matrices + authoritative result JSONs
├── data/annotation_package/   # de-identified human-annotation package (145 items)
├── data/raw_external/         # 40 real-world CVE cases (paper-1 case library)
├── tools/                     # analysis, audit, gate and verification scripts
├── Scripts/                   # environment check + one-shot reproduction
├── docker/                    # container recipe (see REPRODUCTION.md)
└── tests/                     # pytest suite
```

## Citation

```bibtex
@misc{anonymous2027queyi,
  title  = {Caliber Drift and Capability Boundaries: An Audit Protocol for Software-Verification Evaluation},
  author = {Anonymous},
  year   = {2027},
  note   = {Anonymous submission. Companion paper: The Boundary of Evaluator Auditing.},
  license = {Apache-2.0}
}
```

Machine-readable citation: [`CITATION.cff`](CITATION.cff).

## Honest limitations

- **Human inter-annotator agreement is 0.** All $\kappa$ values in the papers are **AI
  self-consistency**, not human agreement; the annotation package is shipped but unexecuted.
- **Docker images are not build-tested** in the authors' environment.
- **English-only PoCs** for one asset; the real-world benchmark uses *reconstructions*, not original
  project contexts.
- See each paper's *Threats / Limitations* section for the full list.

## License

[Apache-2.0](LICENSE). Contributions are accepted under the same licence and require a
[DCO](https://developercertificate.org/) sign-off (`git commit -s`).
