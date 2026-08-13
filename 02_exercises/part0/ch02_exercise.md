# Chapter 2 Exercise — Repo Base Camp Setup

- **Objective:** Get a project repo to a real engineering baseline: version controlled, documented, licensed, and checked automatically on every push.
- **Prerequisites:** Chapter 1's exercise (know what you're building and why).
- **Steps:**
  1. Audit the existing folder structure for duplication or drift between what's documented (e.g. a CLAUDE.md or README) and what's actually on disk.
  2. Fix any structural drift found, then `git init`, add a `.gitignore` for your stack, and make a first commit.
  3. Decide a license. If the repo mixes code and non-code content (writing, data, docs) with different reuse implications, consider splitting it (e.g. MIT for code, all-rights-reserved for prose) rather than defaulting to one license for everything.
  4. Write a README that actually orients a reader: what the repo is, how it's organized, where to look for what.
  5. Add a minimal CI workflow that checks something real, even one rule, rather than a no-op placeholder. A check that does nothing gives false confidence.
  6. Before making the repo public, scan for anything that shouldn't be: credentials, personal data that will accumulate over time (like an in-progress job search tracker), proprietary business data. Gitignore it and, if the schema itself is worth documenting, commit a template/schema-only version instead.
  7. Create the remote repo, push, and actually watch the CI run, don't just assume it passed.
- **Success criteria:** A pushed, public (or intentionally private) repo with real version history, a working CI check, and nothing sensitive in git history.
- **Time estimate:** 1-2 hours, longer if CI catches something (it might).

**Reference output:** `github.com/brunomoreira86/ai-engineer-journal` and `planning_journal/2026-08-13-repo-structure-audit.md`.
