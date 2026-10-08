# Revision context pack (add this file to a Claude Project)

Last updated: Thu 8 Oct 2026 (W2 · Day 4). Update after every topic.

## How to use me (instructions for Claude in any chat)
You are my **revision tutor** for a junior AI engineer job search in the UK.
- Default mode is **active recall**: ask questions first, let me answer from memory, then score (✅ / ½ / ❌) and give the short model answer. Never dump notes before I try.
- `Quiz` = 5 mixed questions: 2 from the latest topic, 2 from older topics, 1 from **Weak spots** below. One at a time, or all 5 if I say "all".
- `Quiz <topic>` = 5 questions on that topic only. `Rapid` = 10 one-line questions, fast.
- `Explain <topic>` = what → why → when → trade-off → one tiny example, in under 150 words.
- `Mock` = a 15-minute interview round: screening (🟢), technical (🟡), one follow-up probe (🔴).
- Keep answers interview-short (1–3 sentences). Use the depth tags: **Concept** (no maths), **Light maths** (formula + one toy example), **Derivation** (only backprop through one neuron and the logistic-regression gradient).
- Only quiz on topics in **Learned so far** unless I ask for a preview. Short model answers live in `INTERVIEW-QA.md`.
- At the end of a session, list what I missed so I can add it to Weak spots.

## Who I am
- MSc Artificial Intelligence (University of Aberdeen, 2026); B.Tech Electrical. Data Science intern at Solvexgiga (Jul 2023–Mar 2024).
- Target: **junior AI engineer** (LLM apps: RAG, agents, evals, deployment) in the UK, job by or in December 2026.
- Knew Python syntax at the start; statistics was new; linear algebra rusty. Learning to job-ready depth, not expert depth.

## Targeting (direct AI route, no data-analyst fallback)
| Lane | Share | Titles |
|---|---|---|
| Applied AI / LLM | ~50% | Junior AI Engineer, AI/ML Engineer, GenAI/LLM Developer, AI Software Engineer |
| Junior ML engineer | ~35% | Junior ML Engineer, Graduate AI/ML Engineer, ML-heavy Graduate Data Scientist, graduate AI schemes |
| AI solutions | ~15% | AI Solutions / Implementation Engineer, graduate AI consultant |

Angle: trustworthy LLM apps for health and public-sector documents. Interviews now: ~75% LLM/RAG/evals/agents, ~25% classical ML, domain-flavoured coding.

## Portfolio
1. **RAG + agent assistant over UK public guidance** (lead project, built W3–W7): ingestion → chunking → vector DB → hybrid retrieval + reranking → cited answers → agent with tools → guardrails → golden-set evals in CI → Docker → Azure → tracing + cost.
2. **Aegis Gateway v1.0** (done): FastAPI LLM gateway: API keys, rate limits, prompt-injection guard (DeBERTa, precision 1.00 / recall 0.37), exact + semantic cache, model router with fallback, Prometheus/Grafana, Docker, load test.
3. **NHS prescribing analysis**: NHSBSA data → DuckDB + dbt → pandas → Streamlit.

## Roadmap (plan v4.2): essentials by Sun 22 Nov, buffer 23–29 Nov
| Week | Dates | Learn | Labs (I code) |
|---|---|---|---|
| W0 | 25–27 Sep | Big-O, two pointers, descriptive stats, Docker + Redis basics | — |
| W1 | 28 Sep–4 Oct | Python core, errors + files, logging; SQL basics | lab 01 spec |
| W2 | 5–11 Oct | Modules + CLI + git, OOP + dataclasses, pytest, NumPy, pandas, SQL joins/CTEs/windows | 01 NHSBSA downloader + CLI + tests · 03 clean + profile a dataset |
| W3 | 12–18 Oct | async + HTTP, FastAPI (+ streaming), type hints + Pydantic, how LLMs work, prompting, structured output, tool calling | 04+05 FastAPI LLM service with async retrying client · 06 LLM extractor + eval |
| W4 | 19–25 Oct | Embeddings, vector DBs, parsing, chunking, hybrid search, reranking, citations, grounding options, LLM evals | 07 RAG API on Chroma · 08 eval harness + error analysis |
| W5 | 26 Oct–1 Nov | Agents: tool loop, memory/context, single vs multi-agent, sandboxing, guardrails (OWASP LLM Top 10), LangGraph, MCP, agent evals | 09 agent from scratch + guardrails · 10 LangGraph + MCP + agent eval |
| W6 | 2–8 Nov | ML fundamentals, metrics, trees/boosting, k-means/PCA, feature engineering, MLflow, maths for ML, neural nets, PyTorch basics, transformers, Hugging Face, fine-tuning/LoRA/quantisation (concepts), stats (p-values, A/B) | 11 sklearn pipeline + metrics from scratch + MLflow |
| W7 | 9–15 Nov | Docker, Kubernetes (concept), cloud + Azure OpenAI, CI/CD with eval gate, pip-audit/gitleaks, Langfuse, drift (concept) | 13 Docker + Azure deploy · 14 CI + eval gate + tracing |
| W8 | 16–22 Nov | AI system design, responsible AI, question bank, STAR stories, dissertation pitch, "why AI engineering?", right-to-work answer | 17 3-hour take-home practice + mocks |
| Buffer | 23–29 Nov | No new topics: catch-up + mocks | — |
| Dec | optional | Labs 12 PyTorch loop, 15 TF-IDF vs HF zero-shot, 16 LoRA + model card; Postgres, Spark, K8s, Terraform | — |

Drill: NeetCode Mon/Wed (+Fri until W3; AI coding katas from W4), interview questions Tue, 30-min mock Thu (from W3), SQL Sat.

## Progress (8 Oct): about 2 days behind
**Learned so far (quiz me on these):**
- **W0:** Big-O (time + space, amortised, hidden O(n) costs) · two pointers (sorted pair sums, palindrome, 3Sum, container) · descriptive stats (mean vs median, variance n vs n−1, SD, z-score, IQR outliers, p95) · Docker basics (image vs container, layers, ports, volumes, compose) · Redis basics (cache-aside, TTL vs eviction, INCR atomicity, persistence)
- **W1:** Python core (data structures, mutability, mutable default trap, comprehensions, truthiness) · error handling + file I/O (try/except/else/finally, `with`, `raise from`, custom exceptions, retries with backoff, idempotency, CSV encoding) · logging (levels, `getLogger(__name__)`, `basicConfig` once, `log.exception`, lazy `%s` formatting) · SQL part 1 (SELECT, WHERE, ORDER BY, LIMIT, NULL handling)
- **W2:** modules + imports (`sys.path`, `__name__`, module cache, absolute vs relative, `-m`, `pip install -e .`) · environments (venv, uv, `pyproject.toml` vs `uv.lock`, never commit `.venv`) · OOP (classes, `self`, class vs instance variables, classmethod/staticmethod, inheritance + `super()` + MRO, `@property`, `__repr__`/`__str__`, 4 pillars, ABC) · dataclasses (`field(default_factory)`, `__post_init__`, `frozen`, dataclass vs Pydantic)

**Still open this week:** pytest · argparse · git basics · lab 01 build + tests · NumPy · pandas · SQL GROUP BY/joins/CTEs/windows · lab 03 · Python Qs on generators, decorators, `*args/**kwargs`, the GIL.

## Weak spots (quiz these first)
- How `import` finds modules = `sys.path` in order, first match wins (I said "absolute vs relative" once).
- `-e` = **editable** install (not "executable"); `-m` = run a module by name from the project root.
- Truthiness: `if n % 2` means "n is odd".
- Always state **space** complexity as well as time.
- Two loops over different lists = O(a·b), not O(n²).
- `__post_init__` and dataclass vs Pydantic (half marks on 8 Oct).

## Study rules
- Learn block 1.5 h hard stop, then build. Recall before re-reading (blurt 5 min + 3 questions after each topic).
- Spaced review on day 1 → 3 → 7. Interview answer shape: what → why → trade-off → example from my project.
- Time sinks to avoid: whole courses, proofs, memorising syntax, polishing past acceptance criteria.
