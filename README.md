# learning-lab

Hands-on micro-projects I build on my path to a junior AI engineer role in the UK (Sep–Nov 2026).
Each one rebuilds a single real component of one of my portfolio projects (a RAG + agent assistant, Aegis Gateway, NHS prescribing analysis), so I understand every line of them.

## Layout
| Folder | What |
|---|---|
| `NN-topic-name/` | One micro-project per topic: code, tests and a README (spec, what I learned, score) |
| `drill/` | Daily interview drills: `neetcode/` (DSA) and `sql/` (DataLemur) |
| `log/` | Daily learning log: notes, cheat sheets, interview questions ([index](log/README.md)) |
| `templates/` | README template for new micro-projects |
| [`PLAN.md`](PLAN.md) | The plan (v4.2: essentials by 22 Nov, buffer to 29 Nov) |

## Micro-projects
| # | Project | Rebuilds | Week | Status |
|---|---|---|---|---|
| 01 | NHSBSA API downloader + CLI + tests | NHS ingestion | W2 | in progress |
| 03 | Clean + profile a real dataset (pandas + NumPy stats + tests) | Data handling | W2 | planned |
| 04+05 | FastAPI LLM service with an async retrying client + tests | Aegis /chat, project API | W3 | planned |
| 06 | LLM extractor with Pydantic validation + eval | Structured output | W3 | planned |
| 07 | RAG API on Chroma with citations | Project retrieval | W4 | planned |
| 08 | RAG eval harness + error analysis | Project evals | W4 | planned |
| 09 | Tool-calling agent from scratch + guardrails | Project agent | W5 | planned |
| 10 | Same agent in LangGraph + an MCP tool + agent eval | Project agent | W5 | planned |
| 11 | sklearn pipeline + feature engineering + metrics from scratch + MLflow | ML fundamentals | W6 | planned |
| 13 | Dockerise + deploy the RAG API to Azure (Azure OpenAI) | Project deploy | W7 | planned |
| 14 | CI with tests + eval gate + tracing | Project CI / observability | W7 | planned |
| 17 | AI take-home practice (3 h) | Interview prep | W8 | planned |

December (optional): 12 PyTorch training loop · 15 TF-IDF vs Hugging Face zero-shot · 16 LoRA fine-tune + model card. Lab 02 was folded into 03.
