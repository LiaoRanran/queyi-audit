# Pull request

## Change description
<!-- What does this PR do, and why? Link the issue it closes. -->

## Testing
<!-- Show the gates you ran. All must be green before review. -->
- [ ] `python -m pytest tests/ -q` — unit tests pass
- [ ] `python -m ruff check tools/` — lint clean
- [ ] `python -m mypy tools/` — types clean (or justified ignore)
- [ ] `python tools/verify_paper_numbers.py --tex paper/paper1/queyi_neurips2027_v1.1.tex --tex-extra paper/paper1/supplementary/paper_appendix_extras.tex` — exits 0

## Checklist
- [ ] No detector / `detect()` is re-run; `data/frozen_matrix/` is unchanged (read-only)
- [ ] Any moved headline number updated (a) the frozen-artifact recomputation and (b) the paper, in that order, in the same PR
- [ ] Package stays double-blind: no author / affiliation / e-mail / source-repo identifier added
- [ ] Commit(s) carry a DCO `Signed-off-by` line (`git commit -s`)
- [ ] Docs / templates / config only — no core algorithm behaviour changed

## DCO
By submitting this PR I certify, per the [Developer Certificate of Origin](https://developercertificate.org/),
that I have the right to submit this contribution and every commit is signed off.
