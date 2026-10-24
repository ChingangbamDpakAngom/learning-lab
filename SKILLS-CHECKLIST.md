# Skills checklist: junior AI engineer (plan v7)

Tick a topic only when **both** are true: I can explain it in 60 s (what → why → trade-off → example) **and** I've used it in a lab or drill. Sub-topics can be ticked as I go.

Market demand (UK junior AI/ML ads, audits on 29 Sep, 5 Oct and 8 Oct 2026): ★★★ nearly every ad · ★★ most ads · ★ some ads / interviews only.

## v7 buckets (24 Oct): how each topic is covered
Shift weeks leave about 4 × 90-min blocks a week, so every topic below sits in one bucket. **Nothing is deleted**: 🔁 and ⏭ topics stay in this checklist and in `revision/` so they can be quizzed and ticked.

**📘 Study block (interview core, in the v7 week table):** async + HTTP · FastAPI + Pydantic · how LLMs work + tokenisation + transformers · prompting + structured output · tool calling · embeddings + vector DBs · chunking/hybrid/reranking/citations · LLM evals + error analysis · agents + guardrails · LangGraph + MCP (concept) · ML concepts (metrics, overfitting, trees/boosting) · neural nets + backprop · fine-tuning vs RAG, LoRA, quantisation · production as a story (Docker, deploy, CI eval gate, tracing) · AI system design · responsible AI · behavioural/STAR · mocks.
Labs kept: 01 (reduced), 04-06 merged, 07, 08, 09, reduced 17.

**🔁 Revision only (10–20 min: phone `Quiz`, Saturday drill, no study block):** SQL joins/GROUP BY/CTEs/windows (SQLBolt, pgexercises) · Python Qs: `*args/**kwargs`, generators, decorators, context managers, the GIL · shell basics · NumPy/pandas recall · stats for interviews (p-values, A/B) · maths for ML (one-liners) · Hugging Face `pipeline` usage · cloud: Azure ↔ AWS map · observability, monitoring/drift · Kubernetes concept · agent evals · feature engineering + MLflow (what/why) · Airflow (concept).

**⏭ Later (December, or only if an interview asks):** lab 03 (profile) · lab 10 LangGraph + MCP hands-on · lab 11 sklearn + MLflow · lab 12 PyTorch loop · lab 13 Azure deploy · lab 14 CI + eval gate · labs 15, 16 · full lab 17 · quantisation benchmark · k-means/PCA hands-on · Postgres, Spark, K8s, Terraform.

## 1. Python foundations (W1–W2)
- [x] ★★★ **Python core**
  - [x] functions, args/kwargs · [x] lists, dicts, sets, tuples · [x] comprehensions · [ ] generators · [ ] decorators · [ ] mutability gotchas · [ ] context managers (`with`, `contextlib`) · [ ] `enumerate`, `zip`, `lambda`, `is` vs `==` · [ ] the GIL
- [x] ★★★ **Errors + files**
  - [x] try/except/else/finally, raise · [x] pathlib · [x] CSV + JSON · [x] retries with backoff · [ ] HTTP `timeout=` + `raise_for_status()`
- [x] ★★ **Logging**
  - [x] levels · [x] `getLogger(__name__)` · [x] `basicConfig` once in main · [x] `log.exception`
- [x] ★★★ **Modules + packages**
  - [x] imports + `sys.path` · [x] `__name__ == "__main__"` · [x] module cache · [x] absolute vs relative · [x] `__init__.py` · [x] `python -m` · [x] `pip install -e .`
- [x] ★★★ **Environments**
  - [x] venv · [x] uv add/sync/run · [x] `pyproject.toml` + `uv.lock` · [x] requirements.txt
- [x] ★★ **CLI**
  - [ ] argparse: positional + optional args, types, defaults, `--help`
- [x] ★★★ **Git + shell**
  - [ ] add/commit/push/pull · [ ] branch + merge · [ ] PR flow + resolving a conflict · [ ] `.gitignore` · [ ] shell basics (cd, ls, pipes, env vars)
- [x] ★★★ **OOP**
  - [x] classes + `self` · [x] class vs instance variables · [x] classmethod + staticmethod · [x] inheritance + `super()` · [x] `@property` · [x] `__repr__` / `__str__` · [x] dataclasses · [ ] composition vs inheritance · [ ] `__eq__` / `__hash__`
- [x] ★★★ **pytest**
  - [ ] asserts + test discovery · [ ] fixtures · [ ] `tmp_path` · [ ] parametrize · [ ] mocking HTTP (monkeypatch / respx) · [ ] running tests: `-k`, `-x`, `-v`
- [x] ★★★ **NumPy**
  - [ ] arrays, dtypes, shape · [ ] vectorisation · [ ] broadcasting · [ ] aggregations, percentiles, z-scores · [ ] views vs copies · [ ] seeded random (`default_rng`)
- [x] ★★★ **pandas**
  - [ ] read_csv/parquet · [ ] select + filter · [ ] missing values · [ ] strings · [ ] groupby/agg · [ ] merge · [ ] profiling (nulls, dtypes, duplicates)
- [ ] ★★★ **SQL**
  - [x] SELECT, WHERE, ORDER BY, LIMIT · [ ] GROUP BY + HAVING · [ ] joins · [ ] CTEs · [ ] window functions (ROW_NUMBER, RANK, LAG, running totals) · [ ] logical order of execution · [ ] `COUNT(*)` vs `COUNT(col)` · [ ] INNER vs LEFT joins + NULLs
- [ ] ★★ **Type hints + Pydantic** (W3, with FastAPI)
  - [ ] type hints · [x] dataclasses vs Pydantic · [ ] validation at the boundary

## 2. APIs + LLM fundamentals (W3)
- [ ] ★★ **async + HTTP**
  - [ ] async/await + `asyncio.gather` · [ ] httpx client · [ ] methods + status codes · [ ] auth headers · [ ] 429 + retries + timeouts · [ ] idempotency
- [ ] ★★★ **FastAPI**
  - [ ] routes + path/query params · [ ] Pydantic request/response models · [ ] dependency injection · [ ] error handling (4xx/5xx) · [ ] streaming responses (SSE) · [ ] TestClient tests
- [ ] ★★★ **How LLMs work**
  - [ ] tokens + context window · [ ] temperature / top-p · [ ] cost + latency · [ ] local vs hosted · [ ] prompt caching · [ ] reasoning effort · [ ] multimodal inputs
- [ ] ★★★ **Prompting**
  - [ ] system prompts · [ ] few-shot · [ ] templates · [ ] step-by-step reasoning · [ ] prompt injection risk
- [ ] ★★★ **Structured output**
  - [ ] JSON mode / schemas · [ ] Pydantic validation · [ ] validate + retry · [ ] field-level accuracy eval
- [ ] ★★★ **Tool calling**
  - [ ] tool schemas · [ ] request → tool → result loop · [ ] tool errors

## 3. RAG + evaluation (W4)
- [ ] ★★★ **Embeddings + vector DBs**
  - [ ] what an embedding is · [ ] cosine similarity · [ ] embedding models from the HF Hub (sentence-transformers) · [ ] Chroma · [ ] pgvector / FAISS (when to use which)
- [ ] ★★ **Ingestion**
  - [ ] document parsing (PDF/HTML → text) · [ ] chunking (size, overlap) · [ ] metadata
- [ ] ★★ **Retrieval**
  - [ ] top-k · [ ] hybrid search (BM25 + vectors) · [ ] reranking
- [ ] ★★★ **Generation**
  - [ ] citations · [ ] "I don't know" answers · [ ] hallucination · [ ] prompt vs tool retrieval vs text-to-SQL
- [ ] ★★ **Evals**
  - [ ] golden sets · [ ] hit@k + MRR · [ ] faithfulness · [ ] LLM-as-judge · [ ] judge vs my labels · [ ] error analysis · [ ] regression tests · [ ] RAGAS

## 4. Agents (W5)
- [ ] ★★ **Agent basics**
  - [ ] workflows vs agents · [ ] ReAct loop · [ ] max steps + stopping rules · [ ] tool errors
- [ ] ★★ **Agent design**
  - [ ] memory + context management · [ ] single vs multi-agent · [ ] sandboxed code execution
- [ ] ★★ **Guardrails**
  - [ ] prompt injection · [ ] OWASP LLM Top 10 · [ ] PII · [ ] output validation
- [ ] ★★ **Frameworks**
  - [ ] LangGraph (state, nodes, edges) · [ ] LangChain / LlamaIndex: when a framework helps
- [ ] ★★ **MCP**
  - [ ] servers · [ ] tools · [ ] resources · [ ] exposing one tool
- [ ] ★ **Agent evals**
  - [ ] task success · [ ] steps · [ ] cost

## 5. ML, deep learning + Hugging Face (W6)
- [ ] ★★ **ML fundamentals**
  - [ ] train/val/test · [ ] overfitting + bias–variance · [ ] regularisation (L1/L2) · [ ] cross-validation · [ ] data leakage
- [ ] ★★ **Metrics**
  - [ ] confusion matrix · [ ] precision/recall/F1 · [ ] ROC vs PR · [ ] thresholds · [ ] imbalance · [ ] MAE/RMSE
- [ ] ★★ **Models**
  - [ ] linear + logistic regression · [ ] trees · [ ] random forests · [ ] gradient boosting (LightGBM) · [ ] k-means · [ ] PCA
- [ ] ★★ **Features + tracking**
  - [ ] encoding · [ ] scaling · [ ] new features · [ ] sklearn Pipeline · [ ] MLflow runs + metrics
- [ ] ★★ **Maths for ML**
  - [ ] vectors + dot product · [ ] matrix multiply · [ ] softmax · [ ] cross-entropy · [ ] gradient descent
- [ ] ★★ **Neural nets + PyTorch**
  - [ ] neurons + activations · [ ] loss · [ ] backprop (one neuron by hand) · [ ] tensors + autograd · [ ] what a training loop does
- [ ] ★★★ **Transformers**
  - [ ] tokenisation · [ ] embeddings · [ ] attention · [ ] decoder-only LLMs · [ ] context length
- [ ] ★★ **Hugging Face**
  - [ ] Hub: models, datasets, model cards · [ ] `pipeline()` (zero-shot, classification) · [ ] tokenizers (AutoTokenizer) · [ ] AutoModel · [ ] sentence-transformers (used in W4) · [ ] serving open models (Ollama, vLLM: concept)
- [ ] ★★ **Fine-tuning**
  - [ ] fine-tuning vs RAG vs prompting · [ ] full vs LoRA/PEFT · [ ] quantisation
- [ ] ★ **Stats for interviews**
  - [ ] probability + distributions · [ ] p-values · [ ] A/B tests

## 6. Production AI (W7)
- [ ] ★★★ **Containers**
  - [ ] images + layers · [ ] Dockerfile · [ ] compose · [ ] slim, non-root, `.dockerignore` · [ ] Kubernetes: pods + deployments (concept) · [ ] hands-on: Redis in Docker + `redis-cli` (W0 gap, do now)
- [ ] ★★★ **Cloud**
  - [ ] compute, storage, IAM, secrets · [ ] managed LLMs (Azure OpenAI, Bedrock, Vertex) · [ ] deploy to Azure Container Apps
- [ ] ★★★ **CI/CD**
  - [ ] GitHub Actions: test + lint + build · [ ] eval gate · [ ] pip-audit + gitleaks
- [ ] ★★ **Observability**
  - [ ] traces · [ ] token cost + latency · [ ] caching + rate limits · [ ] Langfuse
- [ ] ★ **Monitoring**
  - [ ] data/model drift · [ ] alerts · [ ] model registry (concept)
- [ ] ★ *Optional gap:* pipeline orchestration (Airflow, concept, 15 min)

## 7. Interview readiness (W8 + buffer)
- [ ] ★★★ **AI system design**
  - [ ] framework (requirements → data → retrieval/model → evals → serving → monitoring → cost) · [ ] design a RAG bot · [ ] design an agent · [ ] cost + latency maths
- [ ] ★★ **Responsible AI**
  - [ ] bias · [ ] privacy + UK GDPR · [ ] model cards
- [ ] ★★★ **Coding rounds**
  - [ ] NeetCode patterns · [ ] timed mediums · [ ] SQL timed sets · [ ] AI katas (cosine top-k, chunker + BM25, retry + rate limiter, JSON retry)
- [ ] ★★★ **Behavioural**
  - [ ] STAR: internship · [ ] STAR: projects · [ ] STAR: a failure · [ ] "how I build with coding agents" · [ ] dissertation pitch · [ ] "why AI engineering?" · [ ] right-to-work answer
- [ ] ★★★ **Practice**
  - [ ] 3-hour take-home · [ ] 3 full mock loops

## 8. Portfolio proof (must exist before applying hard)
- [ ] ★★★ RAG + agent project: deployed, live link, eval numbers in the README
- [ ] ★★ Aegis: can walk the system in 5 and 10 minutes
- [ ] ★★ Showcase labs 06, 08, 10 pinned with a results table
- [ ] ★★ Two CV versions (AI, ML) with real numbers, no [TBD]

## December (only if ads or interviews ask)
- [ ] ★ Hands-on: PyTorch training lab (12) · TF-IDF vs HF zero-shot (15) · LoRA fine-tune + model card on the HF Hub (16)
- [ ] ★ Postgres data modelling · Spark · Kubernetes hands-on · Terraform
- [ ] ★ Recommender systems · computer vision basics · Azure AI-900
