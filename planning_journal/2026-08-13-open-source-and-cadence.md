# 2026-08-13 — Open source policy, storytelling/build cadence clarified

**Context:** Bruno asked when storytelling happens, when build decisions get made, whether comparing against AskDila makes sense, and whether the portfolio projects should be open source.

**Decisions:**
- **Storytelling cadence:** "The Story" beat gets written alongside the build, following the existing weekly rhythm (build Tue-Thu, draft Fri). Chapter 1 is an exception — it's motivation/context rather than a build, so it can be drafted early.
- **Build decisions:** the 3 portfolio projects are already locked; concrete architecture/scope per project gets decided chapter-by-chapter as we reach that part of the roadmap, not all upfront.
- **AskDila comparisons:** confirmed as intentional — already the recurring thread in `00_meta/BOOK_BIBLE.md`, encouraged throughout.
- **Open source:** portfolio projects (`03_projects/`) will be public repos with public code, but real AskDila business data/docs stay out — synthetic/sanitized data only in anything public. Documented in `CLAUDE.md` and `04_data_assets/README.md`.

**Why:** Public repos are strong evidence for the €100k+ job search (real, inspectable code beats claims on a resume), but Project 1 in particular is built on AskDila's own docs, so a blanket "everything public" policy risked leaking real business/customer content.

**Reconsider if:** a specific project ends up needing more of AskDila's real logic/data than a synthetic stand-in can reasonably capture — may need a private-repo exception for that one project specifically.
