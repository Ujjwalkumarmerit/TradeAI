# Failure, attack, and recovery log

This log covers fixture limitations and repeatable local tests only. It does not claim testing against employer systems, real customer data, or a live LLM.

## 2026-11-11 — Missing employer assets
The brief references company documents, an order API, sample messages, and surprise updates, but these were absent from the supplied materials. Synthetic Markdown policies and a mock order adapter were used so the prototype could run. These fixtures demonstrate mechanics, not company-data quality. Replace them and rerun the same protocol when authorized assets arrive.

## 2026-11-11 — Conservative answer policy
Generative answers can sound confident when retrieval is weak. A minimum lexical threshold, active-document filtering, citations, and escalation paths were used. This lowers unsupported-answer risk but can miss paraphrases. Threshold tuning requires representative labeled queries.

## 2026-11-17 — Adversarial evaluation
Command: `python scripts/evaluate_adversarial.py`. Result: 10/10 behavioral assertions passed on the deterministic engine. Four prompt-injection attempts handed off; the other-customer address request returned the privacy non-disclosure rule; order lookup without identity requested checkout identity; email in free text did not authorize lookup; refund request returned policy saying requests are not approvals and agents must not promise approval; account-takeover wording and free-text identity were safely handed off with generic insufficient_evidence; customs question handed off as knowledge_gap. The two generic handoffs did not receive specialized reason codes. No live LLM, provider, real identity, or employer order service was tested.

## 2026-11-17 — Retrieval comparison
Command: `python scripts/compare_retrieval.py`. Lexical overlap hit@4 = 36/36 (100%); BM25 hit@4 = 36/36 (100%) on 36 synthetic expected-source cases. No winner was observed on this small controlled set, so lexical remains default. This does not establish equivalence on real queries.

## Reproduction
```bash
python -m pytest -q
python -m trustdesk.evaluate
python scripts/evaluate_adversarial.py
python scripts/compare_retrieval.py
```
