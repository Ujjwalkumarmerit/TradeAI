# Daily check-ins — evidence-based reconstruction

Integrity note: The supplied project notes contain a partial Day 1 entry and blank Day 2/Day 3 fields. No time records or dated daily notes establish actual hours or all task dates. Do not submit invented hours. The author must enter each hour total from personal records and confirm the summaries.

## Day 1
- Project evidence: runnable lexical baseline, active-document filtering, 40 synthetic evaluation prompts, and baseline tests.
- Not completed: employer corpus integration; the corpus was not supplied.
- Biggest problem: missing source data; only synthetic fixtures could be evaluated.
- Decision/uncertainty: keep the threshold conservative; tune threshold and chunk size with representative labeled data.
- Input needed: company policies, mock order API contract, and sample customer questions.
- Hours actually spent: AUTHOR TO ENTER FROM PERSONAL RECORDS; not present in supplied artifacts.
- Original next-day plan: integrate the Day 2 policy/service update and rerun the frozen evaluation.

## Day 2
- Project evidence: current and superseded refund fixture files; loader excludes superseded documents; mock order adapter has timeout, malformed-response, and service-failure paths.
- Not verifiable: no employer surprise policy or service update was present. Synthetic current/old policy files are not proof that the real update was received or integrated.
- Biggest problem/recovery: missing external update assets; retained synthetic labels and version metadata rather than inventing company changes.
- Uncertain decision: whether an actual update overrides or supplements a rule cannot be decided without the update and its authority/effective date.
- Input needed: exact Day 2 update and effective date.
- Hours actually spent: AUTHOR TO ENTER FROM PERSONAL RECORDS; not present in supplied artifacts.
- Plan: apply authentic update, add regression tests, and rerun frozen evaluation when supplied.

## Day 3
- Project evidence: 40-question synthetic evaluation, 10-case adversarial set, API/engine tests, report, failure log, design comparison, and walkthrough script. Latest local verification: 24 tests passed; 40/40 decisions; 36/36 retrieval hit@4; 10/10 adversarial checks; BM25 36/36 hit@4.
- Not completed/not verifiable: no live company integration, real-data benchmark, live-model cost/latency measurement, or recorded walkthrough. The script is not a recording.
- Biggest problem/recovery: missing company corpus, API contract, and surprise updates; used deterministic local fixtures and bounded claims.
- Uncertain decision: production retrieval, cost/latency budget, and launch thresholds require representative data and runtime.
- Input needed: employer source data, service contract, deployment constraints, and actual recording link.
- Hours actually spent: AUTHOR TO ENTER FROM PERSONAL RECORDS; not present in supplied artifacts.
- Next steps: complete employer-data evaluation, record walkthrough, and enter actual hours.

## AI assistance disclosure
AI assistance was used to review/improve code, add deterministic adversarial and retrieval-comparison scripts, revise documentation, prepare the walkthrough script, and help assemble the repository. The project owner must verify this statement and add any other tools used. AI did not supply missing employer documents or validate employer systems.
