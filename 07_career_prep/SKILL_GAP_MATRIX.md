# Skill Gap Matrix

Built from two inputs: (1) a market scan of 9 real AI Engineer postings targeting remote-EU/Zurich, €100k+ (Aug 2026, sources logged in `planning_journal/`), and (2) Bruno's self-rated current level (0-5). "Required in job specs?" reflects how often the skill actually appeared in postings, not the original roadmap's assumptions.

| Skill | Required in job specs? | Current level (0-5) | Covered in which chapter | Target level | Notes |
|---|---|---|---|---|---|
| Python | Near-universal (7/9) | 4-5 (assumed, strong full-stack background) | Part 1 | 5 | Confirm during ch04 rather than assume |
| LLM APIs & structured outputs | Required, most postings | 3 | ch09-ch11 | 5 | Heavy *user* of Claude Code but hasn't built with APIs directly (structured outputs, function calling, multi-provider) — treat as a real gap, not a head start |
| RAG (chunking, embeddings, retrieval) | High (5/9) | 0 | ch12-14, Project 1 | 5 | Biggest single gap vs. most-demanded skill — good candidate to prioritize |
| LangChain / LlamaIndex | High (5/9) | 0-1 (assumed) | ch12-14 | 4 | |
| Vector DBs (Qdrant/Milvus/Pinecone) | Moderate (3/9) | 0 | ch12-13, Project 1 | 4 | Postings name specific DBs more than "PostgreSQL" |
| Multi-agent orchestration (LangGraph/CrewAI/AutoGen) | Moderate-high (3-5/9) | 3 ("built something," single framework) | ch15-16, Project 2 | 5 | Existing head start — confirm which framework and go deeper |
| MCP | Low but rising (1/9 explicit) | 2 (assumed, may overlap with agent work) | ch16 | 3-4 | Emerging signal, not yet a filter in most JDs — don't over-invest early |
| Evals/observability (RAGAS, tracing) | Moderate (3/9) | 1-2 | ch14, ch17-18, Project 3 | 5 | Market research flags this as what separates senior/€100k+ postings from generalist ones |
| Docker | Moderate (3/9) | 4-5 (assumed, Coolify/Hetzner experience) | ch19 | 5 | Likely near target already |
| Cloud (AWS/GCP/Azure) | Moderate (3/9) | 1-2 (assumed, self-hosted/Hetzner background) | ch19 | 3-4 | Gap: existing infra experience is self-hosted, not hyperscaler |
| Kubernetes | Moderate, senior roles (2/9) | 0 (assumed) | ch19 | 3 | |
| FastAPI | Moderate (2/9) | 1-2 (assumed, Node background not Python APIs) | ch05, ch07 | 4 | |
| CI/CD | Moderate (2/9) | 3 (assumed, agency background) | ch19 | 4 | |
| Full-stack product ability (React/Node) | Underweighted by roadmap but real (3/9) | 5 (existing core strength) | not a dedicated chapter | 5 | Market research surprise: this is a differentiator, not a footnote — lean into it explicitly when positioning portfolio projects |
| Fine-tuning/LoRA/QLoRA/RLHF | Low, niche (1/9 — PhD/7+yr posting only) | 0 | ch20 | 2 | Roadmap's Tier 2 placement looks overstated for the €100-150k band being targeted — treat as light exposure, not deep competency |
| Responsible AI governance | Rare in postings | 0 | none currently | 1-2 | Mostly large-company/regulated-industry concern per research |

## Open items

- Self-ratings above marked "(assumed)" haven't actually been confirmed with Bruno yet — revisit once we hit the relevant chapter.
- See `planning_journal/` for the full market research writeup and source list.
