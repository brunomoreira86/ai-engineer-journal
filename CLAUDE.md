# Project Context for Claude Code

## What this project is

This repo is a dual-purpose project: it is simultaneously (1) a hands-on learning path to become a production AI Engineer, and (2) the manuscript of a book being written in real time as that learning happens. The book uses storytelling, real-life examples, and hands-on exercises. The author is not writing about AI engineering after the fact — they are writing each chapter immediately after building and testing the thing that chapter teaches.

## Who is doing this

Bruno Moreira, founder of AskDila (a pre-launch AI SaaS) and B-Software (a web design agency), based in Vienna, Austria. Advanced full-stack background: React, Next.js, Node.js, PostgreSQL, Docker/Coolify, Hetzner, multi-tenant SaaS architecture. Bruno already knows how to ship production web apps and wants to add AI engineering depth on top of that — this is NOT a "learn to code from zero" project.

## The end goal

Land a job as an AI Engineer paying more than €100,000/year, most realistically via remote-EU roles or high-paying hubs (Zurich, or senior remote-US-paying roles), since Berlin/Munich senior bands typically run €85k-€140k. Everything in this repo should ultimately serve that goal: every chapter, exercise, and project should map to a real, verifiable skill that appears in actual AI Engineer job postings.

## How the repo is structured

```
ai-engineer-book/
├── README.md                 - top-level orientation
├── ROADMAP.md                - the 9-10 month learning plan, phase by phase
├── BOOK_OUTLINE.md            - full book structure: 23 chapters + 3 milestone project logs
├── PROJECT_BOARD.csv          - IT-project-style backlog: every chapter/project as a row with
│                               sprint weeks, hands-on deliverable, definition of done, and a
│                               salary-relevant skill tag
├── 00_meta/                   - book bible (voice, tone, recurring threads)
├── 01_manuscript/             - the actual book chapters, one .md file per chapter, organized
│                               into 9 parts (Foundations → Python/ML → LLM Fundamentals →
│                               RAG → Agents → Evaluation/Observability → Deployment/MLOps →
│                               Specialization → Job Launch). Each chapter file follows a fixed
│                               four-beat template: The Story / The Concept / The Build / The Debrief.
├── 02_exercises/               - hands-on exercises per part, one folder per part
├── 03_projects/                - the 3 flagship portfolio projects plus a capstone:
│                               project1_rag_chatbot, project2_agentic_workflow,
│                               project3_observability_dashboard, capstone
├── 04_data_assets/             - datasets used across exercises/projects
├── 05_research_notes/          - source material, links, and notes gathered while researching
│                               each chapter topic
├── 06_tools_scripts/           - shared utility scripts (eval runners, chunkers, cost trackers)
├── 07_career_prep/             - JOB_SEARCH_TRACKER.csv and SKILL_GAP_MATRIX.md for the job hunt
└── 08_reviews_feedback/        - feedback logs on chapter drafts
```

## The 3 milestone portfolio projects

1. **Production-grade RAG system** (`03_projects/project1_rag_chatbot`) — ingestion, chunking, hybrid search (BM25 + vector), reranking, citations, and a RAGAS-based eval harness. Ideally built on AskDila's own docs ("chat with your business").
2. **AI workflow agent** (`03_projects/project2_agentic_workflow`) — planning, tool use (5+ tools, MCP integration), retries, guardrails, structured output, tracing. Ideally automates a real AskDila business process (e.g. lead qualification).
3. **AI observability + cost dashboard** (`03_projects/project3_observability_dashboard`) — tracing, latency, token cost, and quality metrics per model, wired to Projects 1 and 2.

## Chapter writing rule

Every chapter must contain at least one real failure, surprise, or debugging story — never a clean, hindsight-polished tutorial. The narrator voice is first-person, plain English, written as the learning happens. Chapters should not be written until the corresponding code has actually been built and tested (this is enforced by the four-beat template and the chapter Status checklist).

The Build beat must include an explicit numbered step-by-step sub-section, not just prose narrative — the reader should be able to follow the steps and reproduce what was built, not just read the story of it. See `00_meta/BOOK_BIBLE.md` for the full chapter template.

## What "done" looks like per chapter

Each chapter file in `01_manuscript/` ends with a status checklist:
- [ ] Story drafted
- [ ] Concept researched and verified
- [ ] Build completed and tested
- [ ] Debrief written
- [ ] Chapter reviewed

A chapter should not be marked reviewed until the linked exercise/project code in `02_exercises/` or `03_projects/` actually runs.

## How you (Claude Code) should help

- When asked to help write a chapter, first check whether the corresponding project/exercise code exists and passes — do not help draft "The Build" or "The Debrief" sections from imagination; use what's actually in the repo.
- When asked to build a project increment, work inside the matching `03_projects/<project>/src` folder, keep code production-quality (typed, tested, documented) since it doubles as portfolio material for job interviews.
- When updating `PROJECT_BOARD.csv`, preserve the existing columns (ID, Phase, Chapter/Deliverable Title, Type, Sprint(Weeks), Skill Focus, Story/Real-world Hook, Hands-on Exercise/Project, Definition of Done, Salary-Relevant Skill Tag) and add a Status column update rather than rewriting rows.
- Keep all code aligned with Bruno's existing stack preferences where reasonable: TypeScript/Python, FastAPI, PostgreSQL, Docker, and deployable to Hetzner/Coolify-style self-hosted infra, since some projects (like the RAG chatbot) may eventually become real AskDila features.
- Always tie new work back to the Salary-Relevant Skill Tag column — if a task doesn't map to a real, hireable skill, flag that before doing it.
- The portfolio projects in `03_projects/` are meant to become public/open-source repos (strong signal for job applications). Code is public; real AskDila business data/docs are not — use synthetic or sanitized sample data in anything meant to go public, and keep real AskDila content out of files that would be committed to a public repo. See `04_data_assets/README.md`.
