# REPRODUCTION_LOG — measured, not claimed

Every command in `REPRODUCTION.md` was executed **from a clean clone** on 2026-10-10 and the
measured exit code is recorded below. This file is the evidence for "the reproduction path is
aligned"; it is generated from the raw log `data/712_复现步骤逐条记录.json` kept in the source
repository.

- Host: Windows 11, Python 3.13 (Windows) / 3.12.3 (WSL Ubuntu), `tectonic` 0.17.0
- Clone command: `git clone <package> queyi-audit-clone712c`
- Working tree after clone: clean (`git status --short` empty)

| # | Stage | Command (abridged) | Exit |
|---|---|---|---|
| S01 | setup | `python -m pip install -r requirements.txt --dry-run` | **0** |
| S02 | env | `bash Scripts/verify_environment.sh --report` | **0** (OK=2 FAIL=0 WARN=12) |
| S03 | paper 1 | `python tools/verify_paper_numbers.py --tex paper/paper1/... --tex-extra ...` | **0** (124 checks, 0 missing, 112 consistent) |
| S04 | paper 2 | same scanner pointed at paper 2 | **1 — by design** (see `REPRODUCTION.md` §2) |
| S05 | integrity | `python tools/gen_693_manifest.py --check` | **0** (15 targets, 0 mismatch, 0 missing) |
| S06 | tests | `python -m pytest tests/ -q` | **0** (18 passed) |
| S07 | chain | `bash Scripts/reproduce_all.sh` | **0** (S2 = registered skip, see limits) |
| S08 | paper 1 | `tectonic queyi_neurips2027_v1.1.tex` | **0** |
| S09 | paper 1 | `python tools/paper_quality_gate_670c2.py` | **0** (6 checks, 0 failed) |
| S10 | paper 1 | `python tools/paper_sync_check_670c2.py` | **0** (`NOT_APPLICABLE`, needs the Markdown master) |
| S11 | paper 1 | `python tools/figure_data_check_670c2.py` | **0** (2 figures, 0 failed) |
| S12 | paper 2 | `tectonic paper2_measurement_drift.tex` | **0** |
| S13 | paper 2 | `python tools/test_axiom_independence.py` | **0** (A2/A5 only; A8 missing confirmed) |
| S14 | paper 2 | `python tools/asset_capabilities.py --validate` | **0** (`ALL_CLAIMS_HOLD = True`) |
| S15 | paper 2 | `python tools/sample_size_calculator.py --type II` | **0** (n = 17, matches 700-C) |
| S16 | anonymity | `python tools/sanitize_annotation_key_paths_712.py --check` | **0** (no host paths) |

**15 / 16 exit 0. The single non-zero (S04) is documented as intended behaviour, not a defect.**
It is reported here as a measured fact so that a reader does not have to trust the prose.

## What was broken before this batch (and is now fixed)

These are the defects the clean-clone run *found*; each one was reproduced before being fixed.

| Defect | Symptom on a clean clone | Fix |
|---|---|---|
| `ready = ready or ok` in the number auditor | dependency groups 676f / 676g reported `ready=true` while 2/3 and 1/2 required files were missing or short | strict `all(...)`, three-state `ready`/`partial`/`not_ready`, 11 counterexample tests |
| hard-coded `research/latex/...` paths in 3 gate scripts | `FileNotFoundError` — the three paper-1 gates could not run at all | path resolvers falling back to `paper/paper1/` |
| `data/693_data_manifest.sha256` never shipped | `gen_693_manifest.py --check` → "manifest does not exist" | manifest generated and shipped; `--check` now 15/15 |
| 6 frozen artifacts missing from the package | manifest reported 6 `missing` targets | the artifacts were re-packaged |
| shell scripts checked out as CRLF | `set: pipefail: invalid option name` — both shell scripts dead on Windows | `.gitattributes` `*.sh text eol=lf` |
| **frozen artifacts silently line-ending-converted on checkout** | 5 `MISMATCH` lines; `reproduce_all.sh` S1 failed | `.gitattributes` `data/frozen_matrix/** -text` **and** `git add --renormalize` on build |
| host absolute paths inside the shipped annotation key | 41 rows leaked `<drive>:\...\<upstream-root>\...` | text-level sanitisation to `upstream-root/<relative>`; semantics verified unchanged |
| `paper_sync_check` traced back with `FileNotFoundError` | confusing failure | prints `NOT_APPLICABLE` + exits 0, declared in `REPRODUCTION.md` §4 |
| README claimed "no personal identifiers" while host paths were present | a false anonymity claim | replaced with a verifiable statement |

## What is still out of scope (declared, not hidden)

- `docker/paper/run_all.sh` (S2 of `reproduce_all.sh`) requires the upstream book toolchain's gate
  engine, which is not part of this package — registered skip.
- Docker images were **not** build-tested by the authors.
- Human inter-annotator agreement is **0**: the annotation package is shipped but unexecuted.
