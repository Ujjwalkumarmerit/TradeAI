# TrustDesk AI — Project Concierge

A conservative customer-support prototype that retrieves policy evidence, cites passages, checks mock orders, and escalates uncertain or risky requests.

## Scope and limitations
The employer-provided corpus, mock order API contract, sample messages, and surprise updates were not present in the supplied project materials. All included policies, order records, and evaluation prompts are synthetic fixtures. This is not production-ready and has not been tested against employer systems.

## Quick start
Python 3.10+:
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn trustdesk.api:app --reload
```
Open http://127.0.0.1:8000 or /docs.

## Optional generation
Set OPENAI_API_KEY and optionally OPENAI_MODEL (default gpt-4o-mini) to enable evidence-constrained drafting. Without a key or if generation fails, the engine returns retrieved evidence. A configured key does not prove live provider access. Order authorization is independent of the LLM.

## Commands
```bash
python -m pytest -q
python -m trustdesk.evaluate
python scripts/evaluate_adversarial.py
python scripts/compare_retrieval.py
```

## Architecture
- FastAPI exposes health, chat, and a small local web form.
- KnowledgeBase parses versioned Markdown, excludes superseded documents, and ranks paragraph passages with transparent lexical overlap.
- SupportEngine applies risk and prompt-injection routing, evidence thresholds, citations, and escalation.
- MockOrderService requires explicit order ID and checkout email and simulates not-found, mismatch, timeout, and malformed responses.
- GroundedGenerator is optional; deterministic extractive fallback remains available.

## Two-design comparison
The shipped lexical overlap ranker is compared with an offline BM25 alternative in docs/DESIGN_COMPARISON.md. Both reached 36/36 hit@4 on the same 36 synthetic questions with expected sources. This fixture is too small to establish a general winner; the simpler lexical baseline remains the default.

## Submission materials
- REPORT.md: results, trade-offs, limitations, and AI assistance disclosure.
- CHECKINS.md: evidence-based reconstruction. The author must enter actual hours from personal records; no hours were inferred.
- FAILURES.md: attack results and recovery log.
- docs/WALKTHROUGH.md: prepared six-minute walkthrough script, not a recording.

## AI assistance disclosure
AI assistance was used to review/refine code, add evaluation utilities, improve documentation, and prepare the walkthrough script. The project owner should verify this statement and disclose any additional tools used. No missing employer assets were fabricated and no employer system was tested.

## Replace fixtures
Replace knowledge/ with authorized company policies and replace MockOrderService in trustdesk/orders.py with the actual service adapter. Preserve source authority, authentication, and safe failure behavior. Re-run the frozen evaluation on representative, independently labeled data before making performance claims.
