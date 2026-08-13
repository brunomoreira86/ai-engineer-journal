# 9-Month Roadmap: Learn AI Engineering by Writing the Book

Target outcome: land an AI Engineer role paying €100,000+ base, most realistic in remote EU/US-remote roles or Zurich/high-tier hubs, since Berlin/Munich senior bands often sit at €85k-€140k and Zurich runs 30-45% higher [cite:9]. Treat every month as a sprint. Each sprint produces a chapter draft, a working piece of code, and an entry in PROJECT_BOARD.csv.

## Timeline Overview

| Month | Phase | Milestone |
|---|---|---|
| 1 | Part 0 - Foundations | Repo live, job specs analyzed, skill gap map done |
| 2 | Part 1 - Python & ML Basics (start) | Production-grade Python module + FastAPI service shipped |
| 3 | Part 1 (finish) | Classic ML model trained and evaluated; Mini-GPT built from scratch |
| 4 | Part 2 - LLM Fundamentals | First chatbot with memory, tool use, deployed publicly |
| 5-6 | Part 3 - RAG + Project 1 | Production RAG system deployed with eval harness |
| 7-8 | Part 4 - Agents + Project 2 | Multi-tool agent with MCP, tracing, deployed |
| 9-9.5 | Part 5-6 - Eval/Observability/Deploy + Project 3 | Dashboard live; one cloud deployment certified-grade |
| 10 | Part 7 - Specialization | Niche chosen, content published |
| 10-11 | Part 8 - Job Launch | Portfolio published, applications and interviews running |

This mirrors the consensus 8-14 month timeline reported across current roadmaps for engineers going from general dev backgrounds to production AI Engineer [cite:4][cite:7][cite:11].

## Why This Order

Foundations before frameworks: Python fluency, APIs, and Git are non-negotiable before touching LangChain or agents, since most "aspiring AI engineers skip straight to LangChain without knowing how to deploy a service" [cite:7]. ML literacy comes next so you understand what embeddings and fine-tuning actually do rather than treating models as magic boxes [cite:5][cite:7]. RAG is prioritized early because it remains "the single most common production pattern in 2026" and is where most real job tasks (ingestion, chunking, retrieval, reranking) actually live [cite:7][cite:5]. Agents come after RAG because "agents without fundamentals are just demos" [cite:5]. Evaluation and observability are placed deliberately mid-late because this is "where seniors live" and differentiates a portfolio from a tutorial-follower's [cite:1][cite:3].

## The Three Portfolio Anchors

Your book's structure is built around three flagship projects that double as your job-search portfolio, following the pattern recommended across multiple 2026 roadmaps of building 3 serious systems instead of 20 toy demos [cite:5][cite:6]:

- Production RAG system with hybrid search, reranking, and a RAGAS-based eval harness [cite:3][cite:5][cite:7]
- An AI workflow agent with tool use, retries, guardrails, and structured output, ideally automating a real AskDila business process [cite:5][cite:6]
- An AI observability and cost dashboard tracking latency, token cost, and quality per model [cite:1][cite:5]

## Skills-to-Salary Mapping

| Skill Tier | Examples | Why It Matters for €100k+ |
|---|---|---|
| Tier 1 (must-have) | Python, LLM APIs, RAG basics, FastAPI, Docker, Git/CI, PostgreSQL | Baseline entry bar across nearly every posting [cite:6][cite:10] |
| Tier 2 (differentiators) | Multi-LLM orchestration, LangGraph agents, MCP, fine-tuning (LoRA/QLoRA), Kubernetes, LLMOps tracing | These push you from mid-level (€60-95k) toward senior bands (€85-165k) [cite:6][cite:9] |
| Tier 3 (senior/staff) | System design for multi-tenant AI APIs, cost/latency optimization at scale, responsible AI governance | Staff/lead bands (€110-220k depending on hub) require this plus shipped production evidence [cite:8][cite:9] |

## Weekly Operating Rhythm

- Monday: read/research for the week's chapter topic, log sources in 05_research_notes
- Tue-Thu: build the hands-on exercise or project increment, commit code daily
- Friday: write the chapter draft in 01_manuscript using what you actually built and broke that week
- Weekend (optional): record a short demo clip, update PROJECT_BOARD.csv status column
