# Plan v5.1: junior AI engineer by December (28 Sep → 22 Nov 2026, buffer to 29 Nov)

**v5.1 (10 Oct):** merges v5 into v4.2, keeping only what's better. **From v5:** reading caps with a "done when" test per topic and the stuck rule (see *Reading budgets*), tokenisation + transformers + positional embeddings moved to W3 next to the LLM topics, an AWS equivalents map in W7, an optional quantisation benchmark in W6. **Kept from v4.2:** Claude builds the projects and I study them (labs are my own code), and the direct AI route (three lanes; data roles only if the reply trigger fires).

**v4.1 (5 Oct):** compressed by 1.5 weeks so every essential topic is done by **22 Nov**. 23–29 Nov is a buffer for mocks and catch-up. Every AI-role topic stays in; only optional hands-on extras move to December (listed at the end).

**v4.2 (5 Oct):** direct AI route only (no DA/NHS fallback). Added after the market + interview audit: feature engineering + MLflow in lab 11, stats for interviews, weekly mocks from W3, AI coding katas from W4, Azure OpenAI in lab 13, standard answers in W8.

Replaces v1–v3. **Goal:** a junior AI engineer role in the UK (LLM apps: RAG, agents, evals, deployment) by or in December 2026. Junior ML engineer and graduate AI/data roles count too.

**Starting point:** I know Python syntax. Everything else is learned here, at interview depth, in the order an AI engineer needs it.

**Profile (fresh start):** MSc AI (Aberdeen). The only work experience on the CV is the Data Science internship at Solvexgiga (Jul 2023–Mar 2024). The portfolio carries the CV.

## What UK AI engineer ads ask for (audit, 29 Sep 2026)
Source: 16 current Indeed UK ads (junior ML engineer, AI engineer, AI/ML engineer, graduate data roles). True "junior AI engineer" titles are rare. The entry routes are junior ML engineer, graduate AI/data roles and AI roles at startups and scale-ups.

| Skill | How common | Where it's covered |
|---|---|---|
| Python (production quality, tests, typing, async) | every ad | W1–W3 |
| LLM APIs, prompting, structured output | most AI ads | W3 |
| RAG: embeddings, vector DBs, retrieval, reranking | most AI ads | W4 |
| LLM evaluation (golden sets, faithfulness, regression tests) | about half | W4, then CI in W7 |
| Agents: tool calling, agent loops, guardrails, MCP | about half, and rising | W5 |
| FastAPI / REST APIs | most | W3, W7 |
| Docker, CI/CD | most (required at mid level) | W7 |
| Cloud (Azure named most often, then AWS/GCP) | most | W7 (Azure deploy + AWS map) |
| ML fundamentals (metrics, overfitting, CV, trees) | ML-titled ads, and asked in interviews | W6 |
| Deep learning, PyTorch, transformers | about half | W3 (tokenisation, transformers, positional embeddings), W6 (neural nets, backprop); PyTorch lab in Dec |
| Hugging Face, fine-tuning (LoRA), NLP | some | W6 (concepts); LoRA lab in Dec |
| SQL, pandas | most | W2, then the Saturday Drill |
| Git, Linux/shell | most | W2 (Missing Semester 1–2) |
| Communication, explaining trade-offs | nearly every ad | W8 + buffer week mocks, LinkedIn posts |

## Targeting: direct AI route (5 Oct audit)
Junior roles with "AI engineer" in the title are rare and mostly ask for 1–3 years; the real junior openings are AI/ML hybrids (classical ML + LLMs + FastAPI + cloud) and junior ML engineer roles. Interviews are now ~75% LLM/RAG/evals/agents, ~25% classical ML, with domain-flavoured coding.

| Lane | Share | Titles | CV |
|---|---|---|---|
| **Applied AI / LLM** | ~50% | Junior AI Engineer, AI/ML Engineer, GenAI/LLM Developer, AI Software Engineer | AI CV (Aegis + RAG project first) |
| **Junior ML engineer** | ~35% | Junior ML Engineer, Graduate AI/ML Engineer, ML-heavy Graduate Data Scientist, AI graduate schemes | ML CV (lab 11 + GridPulse + RAG evals) |
| **AI solutions** | ~15% | AI Solutions / Implementation Engineer, graduate AI consultant, Python developer on an AI team | AI CV, communication first |

- **Angle:** trustworthy LLM apps for health and public-sector documents (NHS data, UK guidance RAG, Aegis guardrails). Health-tech, NHS suppliers and GovTech notice it.
- Apply to "1–3 years" ads too: the MSc AI + 2 deployed projects with eval numbers often clear the bar.
- **Reply trigger:** fewer than 3 replies after 30 AI applications → add data roles at about 1 a week (NHS project CV). Decide on evidence, not worry.

**December, only if job ads keep asking:** Kubernetes, Terraform, Spark, recommender systems, a cloud certificate (AI-900 or AZ-900).

## Who does what
| | Portfolio projects | `learning-lab` repo |
|---|---|---|
| Who codes | **Claude builds**; I study the code and explain it back | **I code**; Claude gives staged hints (full solution only after "stuck" twice, then I rewrite it from memory) |
| Purpose | Evidence for employers | Each lab rebuilds one real piece of a project, so I can defend it in interviews |
| Output | Phase notes + ADRs in each repo | `/NN-topic-name/` + README + conventional commit, a score out of 10 + top 3 fixes |

## Portfolio (priority order)
1. **RAG + agent assistant (new, lead project, W3–W7):** an eval-first assistant over UK public guidance. Ingestion → chunking → vector DB → hybrid retrieval + reranking → answers with citations → an agent with tools → guardrails (reusing the Aegis injection guard) → golden-set evals in CI → Docker → Azure → tracing + cost. Served through Aegis.
2. **Aegis Gateway v1.0 (done):** an LLM gateway: auth, rate limits, injection guard with a measured eval, caching, routing, observability, Docker. Study it in W2–W3.
3. **Medicines Value Monitor (NHS, nearly done, ships W2):** SQL/dbt/data pipeline. Shows the data skills behind the AI work.
4. **Showcase labs (my own code):** promote 4 labs to their own pinned GitHub repos: **06** LLM extractor + eval, **08** eval harness + error analysis, **10** LangGraph + MCP agent (AI eng CV), **16** LoRA fine-tune + model card on the HF Hub (ML/DS CV, December). Gate: REVIEW ≥ 8/10 *and* a real number (accuracy, F1, latency, cost). Extra work: README with results table + 30 s GIF/screenshot, ~30–45 min in SHIP. No new side projects; other labs stay in `learning-lab`.
5. **December, optional:** EPC house-price MLOps, GridPulse-TFT.

## Applications: a feedback loop from 30 Sep
The aim of the early applications is to **measure the CV**, not to win.
- **Pace:** 10 a week, 2 a day Mon–Fri. Tailor only the top third of the CV (title, summary, top 3 bullets) to the ad's keywords.
- **Titles:** Junior AI Engineer, Junior ML Engineer, Graduate AI/ML Engineer, AI/LLM Developer, Graduate Data Scientist. **Adjacent (1 in 3):** Python developer on an AI team, AI solutions / implementation engineer, graduate tech schemes. No DA fallback: every application is an AI/ML title from the three lanes above, unless the reply trigger fires.
- **Log** every application in `D:\portfolio\job-search\job-sheet.csv` with `cv_version`, `company_type` and `sponsor_licence`.
- **Saturday funnel review:** applied → any reply → recruiter screen → technical → final. A 5–10% reply rate is normal for a junior UK candidate. Under 3% after 30 applications means the first 6 lines of the CV, or the targeting, need to change.
- **One change at a time:** CV A vs B (e.g. Aegis first vs the RAG project first, or a different summary line), about 15 applications each before judging.
- **Interview question log:** within an hour of every call, add each question to `log/interview-questions-asked.md` (company, round, question, my answer, a better answer). Claude turns them into drills.
- **Two CV versions** (Jake's Resume, one page): AI engineer (Aegis + RAG project first) and ML/DS. Bullets in XYZ form, `[TBD]` until the number exists.

## Gap-fillers (in the Apply block)
- **Volunteer data role** (CV Experience, above the internship): Reach Volunteering, CharityJob, DataKind UK, or a local charity with a scoped 4-week piece of work. **Max 4–5 h/week.** Genuine volunteering only (visa): no set hours or contractual duties.
- **Graduate visa:** apply once the university reports completion, well before January 2027.

## Daily template (5.75 h, Mon–Sat; Sunday = review + afternoon off)
| Block | Time | What |
|---|---|---|
| Learn | 1.5 h | Today's topic: reading capped at 30–60 min (see *Reading budgets*), then notes, a 60-second explanation out loud, recall, and starting the lab |
| Build | 2.25 h | learning-lab lab (my code), *or* studying the project code Claude built |
| Apply | 1 h | 2 tailored applications (Mon–Fri), logged; Saturday funnel review. **Never cut.** |
| Drill | 30 m | Mon/Wed NeetCode · Fri NeetCode (W2–W3), then an AI coding kata (W4+) · Tue 5 interview questions out loud · Thu interview questions (W2), then a 30-min mock with Claude (W3+) · Sat SQL |
| Network | 30 m | LinkedIn: 3 comments + 2 connection requests; post on Wednesdays |

Behind schedule? Cut the stretch goal first, then the Drill. Never cut Apply.

## Week by week
| Wk | Dates | Learn | learning-lab (I build) | Project (Claude builds / I study) |
|---|---|---|---|---|
| 0 | 25–27 Sep | Setup, Big-O, descriptive stats | Create `learning-lab` | NHS business question + metrics |
| 1 | 28 Sep–4 Oct | Python core, errors + files, logging; SQL basics (Drill) | — (lab 01 spec written) | NHS ingestion → DuckDB → dbt |
| 2 | 5–11 Oct | Modules + CLI + git, OOP + pytest, NumPy (essentials), pandas, type hints + Pydantic; SQL joins/CTEs/windows (Drill) | 01 NHSBSA API downloader + tests · 03 clean + profile a dataset (NumPy stats folded in, replaces 02) | NHS v1 ships · study Aegis 0–2 |
| 3 | 12–18 Oct | async + HTTP/REST, FastAPI (incl. streaming responses / SSE), how LLMs work (incl. prompt caching, reasoning effort, multimodal), tokenisation, transformers + positional embeddings (RoPE), prompting, structured output, tool calling | 04+05 FastAPI LLM service with an async retrying client + tests · 06 LLM extractor + eval | New project spec + ingestion · study Aegis 3–7 |
| 4 | 19–25 Oct | Document parsing, embeddings, vector DBs, chunking, hybrid search, reranking, citations, grounding options (prompt vs tool retrieval vs text-to-SQL), LLM evals + evaluating the judge | 07 RAG API on Chroma · 08 eval harness + error analysis | Project: retrieval + eval suite |
| 5 | 26 Oct–1 Nov | Agents: tool loop, memory + context management, single vs multi-agent, sandboxed execution, guardrails (OWASP LLM Top 10), LangGraph, MCP, agent evals | 09 agent from scratch + guardrails · 10 LangGraph + MCP + agent eval | Project: agent + guardrails |
| 6 | 2–8 Nov | ML fundamentals (metrics, overfitting, CV, trees, k-means + PCA); maths for ML (vectors, dot product, softmax, cross-entropy); DL concepts (backprop, PyTorch basics; transformers already in W3); NLP basics, Hugging Face, fine-tuning vs RAG vs prompting, LoRA + quantisation (concepts); stats for interviews (probability, p-values, A/B tests) | 11 sklearn pipeline + feature engineering + metrics from scratch + MLflow tracking · optional: 30-min quantisation benchmark (4-bit vs 8-bit in Ollama) or 2 h mini PyTorch loop (Sat) | **Project v1 ships** (demo video) |
| 7 | 9–15 Nov | Docker (+ Kubernetes in 20 min, concept), dependency/secret scanning, cloud (Azure + an AWS equivalents map: ECS/Lambda, Bedrock, IAM, Secrets Manager), CI/CD with an eval gate, observability (Langfuse), monitoring + drift (concepts) | 13 Dockerise + deploy RAG API to Azure (Azure OpenAI as the model provider) · 14 CI + eval gate + tracing | Live demo link on README + CV (**end-to-end project done**) |
| 8 | 16–22 Nov | AI system design, responsible AI, question bank (~60 Qs), STAR stories + "how I build with coding agents" story; 2-min dissertation pitch, "why AI engineering?", right-to-work answer; Skills Map checklist | 17 AI take-home practice (3 h) | Project explanations + final polish |
| Buffer | 23–29 Nov | No new topics: catch-up on any slipped lab, 2–3 mock interviews, re-drill weak questions | — | — |
| Dec | optional | Lab 12 PyTorch training loop · lab 15 TF-IDF vs HF zero-shot · lab 16 LoRA fine-tune + model card · Postgres data modelling · K8s/Terraform only if ads ask; whatever interviews exposed | — | EPC / GridPulse (optional) |

Behind by more than 2 days? Use Sunday morning first, then the buffer week. Never push a W2–W7 topic into December.

## Reading budgets (from v5)
Only the capped part of the Learn block is reading; the lab answers most of what reading can't.
- **Stuck rule:** when the timer ends, write open questions under *Parked* in today's notes and move to the lab, even if the topic still feels fuzzy. Parked questions go to Claude in the evening or to Sunday review. A topic that overruns twice in a week moves to the buffer. Never more than one extra 30-minute block on any topic.
- **How to read:** skim first (10% of the cap), then read only the 2–3 sections that answer "done when". One source per topic (a second only for a parked question, max 15 min). Videos at 1.25–1.5×, stop at the cap even mid-video. Passing "done when" early = stop and bank the time.

| Wk | Topic | Cap | Done when |
|---|---|---|---|
| W2 | Type hints + Pydantic | 30 min | You can validate a request body and show the error |
| W3 | async + HTTP | 40 min | You can say why LLM apps use async and how to handle a 429 |
| W3 | FastAPI | 45 min | You can add a validated POST route without looking |
| W3 | How LLMs work + tokenisation | 45 min | You can tokenise 3 odd words and explain the counts |
| W3 | Transformers + positional embeddings | 60 min | You can draw attention and compare RoPE with learned positions |
| W3 | Prompting + structured output | 40 min | Your extractor returns valid JSON 10 times out of 10 |
| W3 | Tool calling | 30 min | You can trace one request → tool → result loop |
| W4 | Embeddings + vector DBs | 40 min | You've ranked 10 sentences by cosine similarity in NumPy |
| W4 | Chunking, hybrid search, reranking | 50 min | You can justify your chunk size with a number |
| W4 | Grounded generation | 30 min | Your prompt refuses an out-of-scope question |
| W4 | LLM evals | 60 min | You can define hit@k and faithfulness in one sentence each |
| W4 | Error analysis | 30 min | You've named 3 failure types from real outputs |
| W5 | Agents vs workflows | 45 min | You can name 3 workflow patterns and when an agent is overkill |
| W5 | ReAct loop + memory | 40 min | Your loop stops itself after N steps |
| W5 | Guardrails (OWASP LLM Top 10) | 40 min | You can name 5 risks and one fix each |
| W5 | LangGraph | 45 min | You can rebuild your loop as a 3-node graph |
| W5 | MCP + agent evals | 30 min | One tool runs as an MCP server |
| W6 | Supervised learning + metrics | 60 min | You can pick and defend a metric for an imbalanced problem |
| W6 | Trees + boosting | 45 min | You can explain boosting vs bagging in 60 seconds |
| W6 | Neural nets + backprop | 60 min | You can walk backprop through one neuron on paper |
| W6 | Fine-tuning vs RAG vs prompting, LoRA | 40 min | You can pick one for 3 scenarios and say why |
| W6 | Quantisation | 30 min | You can explain the quality trade-off |
| W7 | Docker + compose | 45 min | Your API runs in compose from a clean clone |
| W7 | Cloud: Azure + AWS map | 45 min | You can name the AWS service for each Azure piece |
| W7 | CI/CD with an eval gate | 30 min | A failing eval blocks the merge |
| W7 | Observability | 30 min | One request shows a full trace with cost |
| W8 | System design, responsible AI | 30 min a day | You can run the design framework on a blank page in 5 minutes |

## How to study (so no time goes on the wrong depth)
Every LEARN step starts with a tag that says how deep to go:

| Tag | Topics | How to study | Done when |
|---|---|---|---|
| **Concept** (most topics) | RAG, agents, evals, APIs, Docker, CI, cloud | What it is, why it exists, trade-offs, when to use it. Draw the flow, then build it in the lab. No maths. | You can explain it in 60 s and answer "why not X instead?" |
| **Light maths** | Metrics, cosine similarity, softmax, cross-entropy, gradient descent, attention, p-values | Formula + what each symbol means + intuition. One tiny example by hand (2–3 numbers), then code it in NumPy and check against the library. | You can compute a toy example and say what changes if an input grows |
| **Derivation** (only these) | Backprop through one neuron; logistic-regression gradient | Work it on paper once, re-derive from memory 3 days later. | You can re-derive it in under 10 min |

**Habits:** active recall (close the notes, write what you remember) over re-reading · spaced review on day 1 → 3 → 7 (Sunday review covers day 7) · Feynman test (explain it simply; the gap is what to re-learn) · interview framing: what → why → trade-off → example from my project.

**Don't (time sinks):**
- No proofs or derivations beyond the two above; no maths textbooks cover to cover.
- No full courses or whole playlists: only the sections a topic links to.
- Don't memorise library APIs or syntax: know what exists and look it up.
- Don't polish a lab past its acceptance criteria; stretch goals only when ahead of schedule.
- Don't learn tools the ads don't ask for (December list stays in December).
- Stop reading after the 15-min LEARN and start building; questions get answered in BUILD.

### Active recall activities (built into the day, no extra block)
| When | Activity | Time | How |
|---|---|---|---|
| End of every LEARN | **Blurt** | 5 min | Close the notes. Write everything you remember on a blank page (or `notes.md`). Then open the notes and mark what you missed in red; the misses are tomorrow's warm-up. |
| End of every LEARN | **3 recall questions** | 5 min | Claude asks 3 questions (1 concept, 1 "why / trade-off", 1 tiny example or toy calculation). Answer without notes; score yourself /3 in `notes.md`. |
| Start of the next day | **Warm-up quiz** (`Quiz`) | 5 min | Claude asks 5 mixed questions on yesterday + one older topic. Anything wrong goes in `log/weak-spots.md`. |
| During BUILD | **Code from memory** | 10 min | Before looking anything up, write the key function (e.g. retry loop, cosine top-k, train/val split) from memory; then compare and fix. |
| Light-maths topics | **Recompute** | 5 min | Redo the toy example (2–3 numbers) on paper with no notes, e.g. softmax of [1, 2, 3], precision/recall from a 2×2 matrix. |
| Sunday review | **Blank-page cheat sheet** | 20 min | Rebuild the week's cheat sheets from memory, compare with the real ones, and re-study only the gaps. Then redo 3 questions from `weak-spots.md`. |
| Day 3 + day 7 after a topic | **Spaced re-quiz** | 5 min | `Quiz` picks topics due on that day; score must reach 4/5 or the topic goes back into `weak-spots.md`. |

Rule: **recall before re-reading.** If you can't recall it, that's the signal to re-read, and only that part.

## Commands (learning chat)
`Topic: X` start the loop · `Hint` · `Stuck` · `Review` (paste code) · `Quiz` (5 recall questions: yesterday + spaced topics + weak spots) · `Status` · `Weekly post`.
Loop per topic: LEARN (15 min read) → RECALL (blurt + 3 questions, 10 min) → SPEC (60–150 min task, acceptance criteria, stretch) → BUILD (hints) → REVIEW (/10 + top 3 fixes) → SHIP (folder, README, commit, git commands explained; labs 06/08/10/16 also get their own showcase repo if they pass the gate) → INTERVIEW (3 Qs, answers checked) → LOG (row in README.md, next topic).

## Resources
Checklist: [DeepLearning.AI AI Engineering Skills Map](https://www.deeplearning.ai/resources/ai-engineering-skills)
Core: [Python tutorial](https://docs.python.org/3/tutorial/) · [MIT Missing Semester](https://missing.csail.mit.edu/) · [FastAPI](https://fastapi.tiangolo.com/) · [Pydantic](https://docs.pydantic.dev/latest/) · [DataLemur](https://datalemur.com/) · [NeetCode 150](https://neetcode.io/practice)
LLM apps: [Claude tool use](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview) · [OpenAI function calling](https://platform.openai.com/docs/guides/function-calling) · [Prompt Engineering Guide](https://www.promptingguide.ai/) · [Chroma](https://docs.trychroma.com/) · [Eugene Yan: LLM patterns](https://eugeneyan.com/writing/llm-patterns/) · [Hamel Husain: evals](https://hamel.dev/blog/posts/evals/) · [RAGAS](https://docs.ragas.io/) · [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) · [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) · [MCP](https://modelcontextprotocol.io/) · [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) · [HF LLM course](https://huggingface.co/learn/llm-course) · [HF Agents course](https://huggingface.co/learn/agents-course)
Production: [Docker](https://docs.docker.com/get-started/) · [Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/) · [Azure for Students](https://azure.microsoft.com/en-gb/free/students) · [GitHub Actions](https://docs.github.com/en/actions) · [Langfuse](https://langfuse.com/docs) · [MLflow](https://mlflow.org/docs/latest/)
ML/DL: [StatQuest](https://www.youtube.com/@statquest) · [ISLP](https://www.statlearning.com/) · [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course/classification) · [3Blue1Brown NN](https://www.3blue1brown.com/topics/neural-networks) · [PyTorch basics](https://pytorch.org/tutorials/beginner/basics/intro.html) · [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) · [HF NLP course](https://huggingface.co/learn/nlp-course) · [PEFT](https://huggingface.co/docs/peft/index)
Interviews: [Chip Huyen: AI Engineering](https://github.com/chiphuyen/aie-book) · [ML Interviews book](https://huyenchip.com/ml-interviews-book/) · [Tech Interview Handbook](https://www.techinterviewhandbook.org/)
