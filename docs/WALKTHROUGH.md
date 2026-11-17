# 5–8 minute walkthrough script (target: about 6 minutes)

This is a prepared script, not a recording. Record the actual application and repository before submission. Use only synthetic fixture data.

| Time | Show | Narration |
|---|---|---|
| 0:00–0:40 | Repository and README | TrustDesk AI is a conservative support prototype. It answers from a versioned knowledge base, cites evidence, checks mock orders, and escalates uncertain or risky requests. |
| 0:40–1:30 | trustdesk package | FastAPI exposes the API. The engine routes risk and order intents; the knowledge layer retrieves passages; the order adapter is mocked. |
| 1:30–2:30 | Run uvicorn trustdesk.api:app --reload; open /docs and / | The local web form calls /chat. This is a local demo, not a deployed service. |
| 2:30–3:20 | Ask about approved refund timing | The answer comes from the current refund fixture and returns a citation. Superseded material is excluded. |
| 3:20–4:10 | Ask for order status, then use fixture order ID and email | The lookup requires both explicit fields. The records are synthetic and not connected to a real order platform. |
| 4:10–5:10 | Run tests and evaluations | These repeatable checks use synthetic prompts and do not prove employer-data accuracy or live LLM safety. |
| 5:10–6:00 | Show design comparison, failure log, and report | Lexical overlap and BM25 tie on this small set. The company corpus, API contract, and surprise updates were unavailable. |
| 6:00–6:30 | Show repository limitations | Next steps are authorized company data, real integration, frozen evaluation, authentication, monitoring, and human handoff. |

## Recording checklist
- [ ] Capture final test/evaluation output.
- [ ] Show only synthetic order/customer records.
- [ ] Keep the recording between 5 and 8 minutes.
- [ ] State clearly that the policies and order adapter are synthetic fixtures.
- [ ] Do not claim production readiness, live AI verification, or employer-system testing.
- [ ] Upload/link the actual recording in the submission portal; this script is not the recording.
