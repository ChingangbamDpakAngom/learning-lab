# Merged plan v2: LEARN → BUILD → SHIP (28 Sep → 29 Nov 2026)

Replaces [PLAN-v1-archived.md](log/PLAN-v1-archived.md). Goal: a UK job paying **£40–50k by December**. Apply for **Data Analyst and junior ML/AI roles in parallel** from Week 2 onwards.

**Profile (fresh start):** MSc AI (Aberdeen). The only work experience listed is the Data Science internship at Solvexgiga (Jul 2023–Mar 2024). The CV is carried by the portfolio.

## Who does what
| | Portfolio projects (4 repos) | `learning-lab` repo |
|---|---|---|
| Who codes | **Claude builds**; I study the code and explain it back | **I code**; Claude gives staged hints (full solution only after "stuck" twice, then I rewrite it from memory) |
| Purpose | Evidence for employers | Each micro-project rebuilds one real component of a project, so I understand what's been built |
| Output | Phase notes + ADRs in each repo | `/NN-topic-name/` + README + conventional commit, a score out of 10 + top 3 fixes |

## Portfolio (in the order it's built or studied)
1. **NHS prescribing analysis** (DA, built to senior standard): NHSBSA → DuckDB/dbt → pandas → Power BI + Streamlit → GitHub Actions refresh. *New. Claude builds it in W1–W4.* See the spec below.
2. **Aegis Gateway v1.0** (AI eng): *Done.* Study it for interviews in W4–W5 (a lighter pass than in v1).
3. **EPC house-price MLOps** (DS/MLOps): Land Registry + EPC → address matching → LightGBM + SHAP → MLflow/DVC/Prefect → FastAPI + Docker → Evidently drift. *New. Claude builds it in W6–W8.* kind/Terraform is the stretch goal and gets cut first.
4. **GridPulse-TFT** (DL/time series): *Exists.* Study and audit it in W8–W9.

### NHS project: senior-analyst standard (not a generic project)
1. **Business question + decision:** which ICBs and practices overspend on low-value or branded medicines, and what £/year could switching save? Scope it this narrowly so it's different from OpenPrescribing.
2. **Metric definitions doc** (`docs/metrics.md`): cost per 1,000 patients (list-size normalised), generic prescribing rate, savings opportunity. Each has a definition, caveat and owner.
3. **dbt layers:** staging → intermediate → marts; `unique`/`not_null`/`relationships` tests, source freshness, dbt docs site.
4. **Pipeline:** monthly GitHub Actions refresh, idempotent (a re-run doesn't duplicate data); data-quality checks fail the run and alert.
5. **Rigour:** funnel plots / z-scores for outliers, uncertainty stated for every finding.
6. **Deployed:** public Streamlit Community Cloud app + dbt docs on GitHub Pages + `.pbix` and screenshots (publish-to-web with the Aberdeen account while it works).
7. **Stakeholder deliverables:** a 1-page exec memo (findings, £ estimate, recommendations, limitations), ADRs, a runbook, a changelog, and a STAR story.

## Gap-fillers (in the Apply block)
- **Volunteer data role** (goes in CV Experience, above the internship): W0–1 apply to 2 [Reach Volunteering](https://reachvolunteering.org.uk/opp/data-analyst-15) roles, check [CharityJob](https://www.charityjob.co.uk/data-analyst-volunteer-volunteer-jobs), join the [DataKind UK](https://datakind.org.uk/volunteer-with-us/) mailing list (aim for a DataDive), shortlist 3 local charities to approach. W2–6 deliver one scoped piece of work with a number in it. **Max 4–5 h/week.** Genuine volunteering only (visa): no set hours or contractual duties.
- **NHS Jobs Band 6 analyst roles** (roughly £38–47k): the NHS project is aimed at these. They're the most realistic DA route to £40k+.

## Daily template (5.75 h, Mon–Sat; Sunday = review + afternoon off)
| Block | Time | What |
|---|---|---|
| Learn | 1.5 h | Today's topic: LEARN notes + cheat sheet |
| Build | 2.25 h | learning-lab micro-project (my code), *or* studying the project code Claude built |
| Apply | 1 h | Applications. **Never cut.** |
| Drill | 30 m | Mon/Wed/Fri SQL (DataLemur) · Tue/Thu/Sat NeetCode (arrays, hashing, two pointers, sliding window, stacks, binary search only) |
| Network | 30 m | LinkedIn: 3 comments + 2 connection requests; post the week's best micro-project on Wednesday |

Behind schedule? Cut the stretch goal first, then the Drill. Never cut Apply.

## Week by week
| Wk | Dates | Learn | learning-lab (I build) | Project (Claude builds / I study) | Apply focus |
|---|---|---|---|---|---|
| 0 | 26–27 Sep | Setup | Create `learning-lab` repo | NHS: business question + metric definitions | CV v1 (internship + 4 projects), job sheet, 20 target companies, 2 Reach volunteer applications, DataKind signup |
| 1 | 28 Sep | Python core (functions, data structures, OOP, errors, file I/O, modules), pytest, NumPy | 01 NHSBSA API downloader + tests · 02 NumPy prescribing stats | NHS: ingestion → DuckDB, dbt staging | Save roles; first 2 DA + NHS Band 6 applications; approach local charities |
| 2 | 5 Oct | pandas; SQL joins, CTEs, window functions (DuckDB) | 03 clean a month of EPD data · 04 top-N drugs per ICB with window functions | NHS: dbt intermediate/marts + tests + docs | ~6/week DA; start the volunteer work |
| 3 | 12 Oct | Visualisation, Power BI/DAX, statistics (distributions, CI, hypothesis tests, A/B) | 05 Streamlit page · 06 funnel plot: is regional variation significant? | NHS: analysis, Streamlit + Power BI, Actions refresh + DQ alerts | DA + NHS; volunteer work |
| 4 | 19 Oct | LLM APIs, prompting, FastAPI, Pydantic, structured logging | 07 FastAPI chat endpoint · 08 exact-match cache · 09 JSON logs + request IDs | NHS: deploy + exec memo + ADRs → **NHS v1 shipped** · Study Aegis phases 0–2 | Add junior AI/ML roles (two CV versions); NHS goes on CV + LinkedIn |
| 5 | 26 Oct | Embeddings, RAG, LLM evaluation, Docker | 10 semantic similarity check · 11 mini RAG + eval · 12 Dockerfile | **Study Aegis** 3–7 → Aegis mock interview | DA + AI; volunteer deliverable |
| 6 | 2 Nov | Classical ML: regression, trees, LightGBM, evaluation, CV, leakage | 13 address normalisation + matching · 14 baseline price model | EPC: data + matching + model | DA + DS |
| 7 | 9 Nov | Feature engineering, SHAP, MLflow, DVC | 15 SHAP report · 16 MLflow tracking | EPC: MLflow/DVC/Prefect, FastAPI + Docker | DA + DS |
| 8 | 16 Nov | CI/CD, Prefect, drift monitoring; time-series basics | 17 GitHub Actions for lab · 18 Evidently drift report | EPC: drift + retraining → **EPC v1 shipped** · GridPulse audit | All ladders |
| 9 | 23 Nov | Neural nets → attention → transformers (interview depth); revision | 19 NumPy logistic regression from scratch | **Study GridPulse** | Mock interviews, follow-ups |
| Dec | — | Kubernetes, Terraform (only if job ads ask) | — | EPC kind/Terraform stretch; GridPulse upgrades | Keep applying |

## Commands (learning chat)
`Topic: X` start the loop · `Hint` · `Stuck` · `Review` (paste code) · `Status` · `Weekly post`.
Loop per topic: LEARN (15 min read) → SPEC (60–150 min task, acceptance criteria, stretch) → BUILD (hints) → REVIEW (/10 + top 3 fixes) → SHIP (folder, README, commit, git commands explained) → INTERVIEW (3 Qs, answers checked) → LOG (row in README.md, next topic).

## Resources
Kept from v1: [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) · [DataLemur](https://datalemur.com/) · [NeetCode 150](https://neetcode.io/practice) · [StatQuest](https://www.youtube.com/@statquest) · [ISLP](https://www.statlearning.com/) · [FastAPI](https://fastapi.tiangolo.com/) · [HF LLM course](https://huggingface.co/learn/llm-course)
Added: [NHSBSA open data](https://opendata.nhsbsa.net/) · [dbt Learn](https://learn.getdbt.com/) · [Microsoft Learn: Power BI](https://learn.microsoft.com/en-us/training/powerplatform/power-bi) · [EPC open data](https://epc.opendatacommunities.org/) · [Land Registry Price Paid](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads)
