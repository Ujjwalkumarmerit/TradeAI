# TrustDesk AI — Project Concierge report

## 1. Problem and scope
Build a support assistant that answers from company knowledge with citations, performs safe order lookup, and hands off when evidence is missing or risk is high. The employer corpus, sample messages, mock order API contract, and Day 2/3 surprise updates were not present. All included policy/order fixtures and evaluation prompts are synthetic. This is a prototype, not production-ready.

## 2. Architecture and decisions
Markdown knowledge documents carry doc_id, status, updated_at, and priority. Only active documents are indexed into paragraph passages. The shipped ranker is transparent token overlap with a conservative evidence threshold. The engine applies risk and injection routing, citations, and escalation. Optional LLM drafting is evidence-constrained with extractive fallback. The mock order adapter requires order ID and checkout email and safely handles mismatch, not-found, timeout, malformed response, and service failure.

## 3. Two-design comparison
Approach A, lexical overlap, is deterministic, transparent, low-dependency, and easy to debug, but weak on synonyms and paraphrases. Approach B, BM25, adds term-frequency, inverse-document-frequency, and passage-length normalization, but remains lexical and introduces tunable parameters. On 36 synthetic expected-source questions both achieved 36/36 hit@4 (100%). No winner emerged; the simpler lexical baseline remains default. Embeddings/live generation were not fairly benchmarked without employer data.

## 4. Results
Latest local clean-copy verification: 24 automated tests passed; synthetic decision evaluation 40/40; synthetic retrieval hit@4 36/36; deterministic adversarial behavioral assertions 10/10; BM25 hit@4 36/36. These are fixture results, not real-world accuracy, security certification, or employer-data performance. Some safe handoffs use generic insufficient_evidence rather than a specialized reason code. No live LLM, real identity, or employer API was validated.

## 5. Failures and risks
Missing employer data is the largest blocker. Lexical retrieval can miss paraphrases; mock email matching is not authentication; live generation availability and cost/latency were not established. See FAILURES.md.

## 6. Next steps
1. Import authorized employer policies and exact surprise updates.
2. Integrate the real order API and authenticated identity.
3. Compare lexical, BM25, and embeddings on a frozen independently labeled holdout.
4. Measure latency and per-request cost under a declared provider/runtime; no credible live cost result exists yet.
5. Add audit logs, PII controls, rate limits, monitoring, and human handoff.

## 7. AI assistance disclosure
AI assistance was used to review/refine code, add adversarial and retrieval-comparison utilities, improve documentation, and prepare the walkthrough script. The project owner should verify this statement and disclose any additional tools used. AI did not create missing employer data or validate employer systems.
