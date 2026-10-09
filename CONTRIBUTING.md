# Contributing

Thanks for looking at this package. It accompanies an anonymous submission, so please keep all
communication de-identified until the review process is over.

## Reporting a problem

Open an issue with:

1. the **file and line** you are looking at (e.g. `tools/verify_paper_numbers.py:1698`);
2. the **exact command** you ran and its output;
3. the **expected** behaviour and where the expectation comes from (paper section / table).

**Numbers take priority over prose.** If a number in a paper does not match the frozen artifact, that
is a bug: please quote both values and the artifact path.

## How to run the gates before sending a change

```bash
python -m pytest tests/ -q                     # unit tests
python -m ruff check tools/                    # lint
python -m mypy tools/                          # types
python tools/verify_paper_numbers.py --tex paper/paper1/queyi_neurips2027_v1.1.tex
```

Any change that moves a headline number must update (a) the frozen-artifact recomputation and
(b) the paper — in that order, and both in the same change.

## Code style

- Python 3.11+, **standard library only** unless a dependency is already declared.
- Every analysis script must be **read-only** with respect to `data/frozen_matrix/` and must print a
  `detect_calls = 0` marker when it writes its output.
- Prefer `fail-loud` over silent fallbacks: a missing input should raise, not be skipped.
- Inline the *research basis* of any non-obvious check as a comment (e.g. which theorem it verifies).

## Contributing human annotations (most useful contribution)

The single largest open gap is **human inter-annotator agreement (currently 0)**. The de-identified
package is in `data/annotation_package/` (145 items + guideline + calibration items). If you can
provide independent annotations, please follow the guideline in that directory and open a PR adding
your sheet — do **not** edit the original files; add a new file instead.

## Licensing and sign-off

All contributions are accepted under **Apache-2.0**. Every commit must carry a
[Developer Certificate of Origin](https://developercertificate.org/) sign-off:

```bash
git commit -s -m "your message"
```

(You do not need to add a name to the papers; the sign-off is for the repository only.)
