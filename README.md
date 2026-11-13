# TrustDesk AI

A cautious customer-support assistant that retrieves policy evidence, cites sources, checks mock order identity, and escalates uncertain or high-risk requests.

> **Status:** prototype / evaluation build. Not production-ready. Included knowledge and order records are synthetic fixtures.

## Features
- Paragraph-level lexical retrieval over versioned Markdown knowledge.
- Source citations and conservative escalation when evidence is weak.
- Optional OpenAI-compatible drafting with extractive fallback.
- Mock order lookup requiring order ID and checkout email.
- Safe handling for identity mismatch, missing orders, service failures, prompt injection, and high-risk requests.
- FastAPI API, minimal browser UI, CLI, 40-question evaluation set, and 10 adversarial scenarios.

## Quick start
Python 3.10+ recommended.

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn trustdesk.api:app --reload
```

Open http://127.0.0.1:8000; API docs: http://127.0.0.1:8000/docs.

## Optional LLM
Set `OPENAI_API_KEY` in your environment to enable optional evidence-constrained drafting. `OPENAI_MODEL` defaults to `gpt-4o-mini`. Without a key, or if the provider call fails, the app falls back to retrieved text. The LLM does not authorize order lookups. Never commit `.env` or credentials.

## CLI
```bash
python -m trustdesk.cli "How long do refunds take?"
python -m trustdesk.cli "Where is order ORD-1001?" --order-id ORD-1001 --email maya@example.com
```

## Tests and evaluation
```bash
python -m pytest -q
python -m trustdesk.evaluate
```

Verified against the uploaded source archive on 2026-11-14: **14 automated tests passed**; synthetic decision evaluation **40/40 (100%)**; synthetic retrieval hit@4 **36/36 (100%)**. These are fixture-only results, not real-world accuracy, production readiness, or live LLM verification.

## Architecture and reports
- [Architecture](docs/ARCHITECTURE.md)
- [Test report](docs/TEST_REPORT.md)
- [Known limitations](docs/LIMITATIONS.md)
- [Screenshots](docs/SCREENSHOTS.md)
- [Failure log](FAILURES.md)

## Layout
`trustdesk/` application code; `knowledge/` synthetic policy fixtures; `evaluation/` synthetic question/adversarial sets; `tests/` automated tests; `docs/` project documentation.

## Important limitations
Retrieval is lexical, not semantic. Order identity is a mock email comparison, not authentication. The order service is local mock data. Live LLM generation was not verified. There is no production authentication, authorization service, rate limiting, monitoring, audit pipeline, or deployment hardening. No genuine screenshots were supplied, so none are fabricated.
