# Design comparison: retrieval approaches

## Decision context
The employer corpus, labeled questions, and surprise policy updates were not available. This comparison therefore uses the synthetic knowledge base and 40 synthetic questions only.

## A — lexical overlap (shipped)
Paragraph passages are tokenized; score is the fraction of unique query tokens present in a passage, with document priority as tie-breaker. A conservative threshold controls whether the assistant answers.

**Benefits:** deterministic, transparent, low dependency, inexpensive, easy to debug, and simple to cite.

**Costs:** synonym/paraphrase weakness; query wording affects coverage; thresholds require representative labels.

## B — BM25 (offline comparator)
BM25 adds term-frequency, inverse-document-frequency, and passage-length normalization while remaining local and inspectable.

**Benefits:** discounts common terms, accounts for term frequency, and normalizes document length.

**Costs:** still lexical; introduces tunable k1/b parameters; scores cannot reuse the lexical threshold; does not solve missing policy knowledge.

## Results and decision
Run `python scripts/compare_retrieval.py`. Both rankers achieved 36/36 hit@4 (100%) on the 36 synthetic questions with expected sources. There is no winner on this small fixture; the simpler lexical baseline remains default. Do not generalize this tie to real queries.

Embeddings and end-to-end generation were not benchmarked because the employer corpus and a frozen real-data holdout were absent. A future comparison should use the same corpus, holdout questions, top-k, latency protocol, and grounded-answer precision/recall measures.
