---
name: Bug report
about: Report a defect in the package, or a number that does not match the frozen artifacts
title: "[BUG] "
labels: bug
assignees: ''
---

Thanks for checking the package. **Numbers take priority over prose** — if a number in a paper
does not match a frozen artifact, that is a bug.

## 1. Where
- **File and line** (e.g. `tools/verify_paper_numbers.py:1698`)

## 2. What you ran
- **Exact command** and its **output** (paste, not a screenshot)

## 3. Expected vs observed
- **Expected** value and where the expectation comes from (paper section / table)
- **Observed** value and the **artifact path** it came from
- If it is a number mismatch, quote **both** values and the artifact path.

## 4. Environment
- OS / Python version (`python --version`)
- Commit you are on (`git rev-parse HEAD`)
