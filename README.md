# Queyi Audit

> A reproducibility package for **auditing the evaluator** behind software-verification
> research: measurement-drift algebra, a four-state verdict ledger, a 1,147 × 8 frozen
> detection matrix, and a 110-defect real-world C++ benchmark — every headline number
> re-derived from read-only frozen artifacts.

---

## Three core findings

1. **Evolving verifiers beat static toolchains by +29.9 pp.**
   On a 566-frame evaluation, the failure-driven verifier reaches **54.6%** recall vs
   **24.7%** for a static pipeline (McNemar *p* ≈ 2.3e-41); on held-out defects the gap is
   **82.9%** (34/41) vs **2.4%**.
2. **Real-world CVE targets: 59.1% recall, 27 unique catches.**
   On 110 reconstructed real-world C++ defects with NVD-verified CVE provenance, the evolved
   verifier uniquely finds **27 defects** that no single static analyzer catches.
3. **A blind-spot map of 34 defect types.**
   **38.4%** of 1,147 samples escape every current tool, and **13 / 34** types are >50% blind —
   quantifying exactly where verifiers fail.

---

## Quick start (3 steps)

```bash
git clone <this-repo> queyi-audit && cd queyi-audit
pip install -r requirements.txt
python tools/verify_paper_numbers.py \
    --tex paper/paper1/queyi_neurips2027_v1.1.tex \
    --tex-extra paper/paper1/supplementary/paper_appendix_extras.tex
# -> exit code 0: every headline number is traceable to the frozen matrices
```

That single command re-derives the headline numbers of Paper 1 from `data/frozen_matrix/`,
read-only — no detector is re-run. `REPRODUCTION_LOG.md` records the **measured** exit code of
every other command in `REPRODUCTION.md`, including the one that is non-zero on purpose.

---

## Project structure

```
queyi-audit/
├── data/frozen_matrix/   # read-only frozen detection matrices (the audit source of truth)
├── tools/                # analysis + audit tooling (read-only over frozen_matrix)
├── paper/                # LaTeX sources for both companion papers (+ compiled PDFs)
├── tests/                # pytest suite
├── docs/                 # project landing page (dark theme)
├── Scripts/              # environment + reproduction helpers
├── docker/               # container definition
├── REPRODUCTION.md       # every command, with measured exit codes
├── REPRODUCTION_LOG.md   # measured results of those commands
└── CITATION.cff          # machine-readable citation (double-blind)
```

---

## The two papers

- **Paper 1 —** *Caliber Drift and Capability Boundaries: An Audit Protocol for
  Software-Verification Evaluation* → `paper/paper1/queyi_neurips2027_v1.1.tex`
  (compiled PDF: `paper/paper1/queyi_neurips2027_v1.1.pdf`)
- **Paper 2 —** *The Boundary of Evaluator Auditing* →
  `paper/paper2/paper2_measurement_drift.tex`
  (compiled PDF: `paper/paper2/paper2_measurement_drift.pdf`)

> **Anonymous submission package.** Distributed under Apache-2.0 and **double-blind**: no
> author name, affiliation, e-mail or source-repository identifier appears in its files, commit
> messages or URLs. Build-host temporary paths inside the frozen matrices were deliberately left
> byte-identical so that every `sha256` anchor stays verifiable.

---

## Citation

```bibtex
@software{queyi_audit_2026,
  title        = {Queyi Audit: A Reproducibility Package for Auditing the Evaluator
                  in Software-Verification Research},
  author       = {Anonymous},
  year         = {2027},
  version      = {1.0.0},
  license      = {Apache-2.0},
  repository   = {https://example.org/anonymous/queyi-audit}
}
```

For the companion papers, cite the articles listed in `CITATION.cff`
(`preferred-citation`).

---

## License

[Apache-2.0](LICENSE). See `CONTRIBUTING.md` for how to report issues and submit changes
(all commits require a DCO `Signed-off-by` line).
