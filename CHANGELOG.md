# Changelog

All notable changes to the **Queyi Audit** anonymous reproduction package are documented here.
This project adheres to [Keep a Changelog](https://keepachangelog.com/), and the package
version follows the `CITATION.cff` `version` field.

## [Unreleased]

## [1.0.0] — 2026-10-09 (anonymous package baseline)

The initial anonymous reproduction package, split out of the source repository for double-blind
review.

### Added
- Frozen detection matrices: `data/frozen_matrix/` (1,147 × 8 asset detection matrix with
  four-state verdicts; 566-frame A5 evaluation; 110 reconstructed real-world C++ defects with
  NVD-verified CVE provenance).
- Analysis + audit tooling in `tools/` (read-only over `data/frozen_matrix/`):
  number-traceability auditor, capability-boundary / blind-spot analysis, sample-size calculator,
  axiom-independence checker, drift-correctability checker.
- LaTeX sources + compiled PDFs for both companion papers (`paper/paper1`, `paper/paper2`).
- `REPRODUCTION.md` (every command) and `REPRODUCTION_LOG.md` (measured exit codes).
- `CITATION.cff`, `LICENSE` (Apache-2.0), `CODE_OF_CONDUCT.md`.
- `tests/` pytest suite.

### Changed
- All author / affiliation / e-mail / source-repository identifiers scrubbed to `Anonymous` /
  `example.org` (double-blind). Byte-identical frozen-matrix temporary paths preserved so every
  `sha256` anchor stays verifiable.

## [1.0.1] — 2026-10-10 (712 / 713 batches)

### Added
- `CONTRIBUTING.md` with de-identified bug-reporting and DCO sign-off guidance.
- `README.md` 30-second entry point (clone → one command → read exit code).

### Changed
- Closed the reference closure: packaged the 702 annotation table and 701 defect list that two
  READMEs cited but had never been packaged.
- `REPRODUCTION.md`: every command measured on a clean clone; published measured exit codes
  (15/16 exit 0; the one non-zero is S04 "by design").

### Fixed
- Anonymity + package-metadata residual identifiers cleaned from `CITATION.cff` and package
  metadata.

## [1.0.2] — 2026-10-10 (718 batch)

### Changed
- `README.md` rewritten: one-line positioning, three core findings with numbers, 3-step quick
  start, project structure, paper links, BibTeX, license.
- `docs/index.html` added (dark-theme landing page, no dead links, no identity leak).

### Fixed
- **L6 residual leak**: 11 `cppbible` / `CPPBIBLE` identifiers in `tools/gate_engine.py` and
  `paper/paper1/supplementary/scripts_index.md` replaced with `queyi-audit` / `QUEYI_AUDIT`.
  Functionality unchanged (the referenced `tools/cppbible.py` was never part of the package);
  full `pytest` suite still passes.

### Added
- `CHANGELOG.md` (this file).
- `.github/ISSUE_TEMPLATE/bug_report.md`, `.github/ISSUE_TEMPLATE/feature_request.md`.
- `.github/PULL_REQUEST_TEMPLATE.md`.
