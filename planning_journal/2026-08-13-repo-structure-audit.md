# 2026-08-13 — Repo structure audit and cleanup

**Context:** Asked for an audit of the repo structure once we started treating this as a real software project, to catch anything that would cause friction later.

**Decision:**
- Flattened the repo: removed the duplicated `ai-engineer-book/` subtree (which had identical copies of `README.md`, `ROADMAP.md`, `BOOK_OUTLINE.md` sitting alongside the true root's copies), so there's now a single source of truth matching what `CLAUDE.md` already documented.
- Added missing orientation `README.md` files to `00_meta/`, `04_data_assets/`, `05_research_notes/`, `08_reviews_feedback/` for consistency with the other section folders.
- Initialized git (`main` branch), added a `.gitignore`, and made the first commit.

**Why:** Two copies of the same files is a bug waiting to happen (edit one, forget the other). No version control meant no history and nothing to point to as evidence of running this like a real project. Missing READMEs were a small but easy-to-fix inconsistency.

**Reconsider if:** the repo grows large enough that flat top-level folders (00_meta, 01_manuscript, ...) stop being enough structure — but not before then.
