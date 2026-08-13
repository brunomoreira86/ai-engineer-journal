# Chapter 2: Setting Up Your Engineering Base Camp

## The Story

Before I'd written a single real chapter, this repo already had a mess in it. Two folders held identical copies of the same three files: the README, the roadmap, the book outline. I haven't decided that on purpose, it just happened, the way clutter always happens: one file created here, another copy scaffolded there, and I did not circled back to check whether I had everything in the right place. There was no version control either. No history, no way to see what changed or when, no safety net if I broke something.

That's a messy garage. It still technically works. You can find the wrench if you dig long enough. But a senior engineer doesn't tolerate that for long, not because of vanity, but because a messy garage costs you later, at the exact moment you can least afford it: mid-debug, mid-deadline, mid-interview when someone asks to see your work.

So before writing anything else, I cleaned that up: audited the structure, collapsed the duplication, initialized git, and pushed a first real commit. I assumed that was the actual work of this chapter.

What I didn't expect came right after, once I had CI wired up. I set up a small GitHub Actions check for a rule from the book bible, no em dashes anywhere in the manuscript, since they read as AI-generated. I tested it locally against Chapter 1 first, because that was the only chapter that actually existed yet, and it passed clean. When I pushed, CI failed anyway, and not on Chapter 1 at all. Twenty-three other chapters failed the check, every one of them still nothing but placeholder scaffolding I hadn't written a single real word of, because the instructional template text sitting in those files since the very start of this project had an em dash baked into it.

I hadn't opened most of those files since creating them weeks earlier. I only found out they were wrong because a machine checked all twenty-three at once, automatically, on the first real push, before anyone reading this book ever would have. Keeping folders tidy is something you do by paying attention to them. Nobody was going to catch this by being careful, because nobody was looking at those files at all. That's what the check was actually for.

## The Concept

Git and CI aren't separate skills from AI engineering, they're the floor everything else stands on. Every job posting I read while researching Chapter 1 assumed them as baseline, not a differentiator, the same way a posting doesn't bother listing "knows how to use a keyboard." That's exactly why they're dangerous to skip: nobody will ever tell you you're missing them, they'll just quietly not move you forward.

A repo's structure is a claim about how seriously you take the work living inside it. Duplicated files, no `.gitignore`, no license, no CI: none of that stops code from running, but all of it signals that nobody has looked closely. For a portfolio repo specifically, that signal matters more than usual, because a hiring manager's first real interaction with your work is often the repo itself, before they read a word of documentation.

CI, specifically, is version control's natural extension: git tracks what changed, CI verifies that what changed didn't break anything you'd already decided mattered. In a repo this small, that's a one-line em-dash check. In a production system, it's the same idea scaled up: linting, type-checking, tests, security scans, all running automatically on every push so that a mistake gets caught by a machine in seconds instead of by a customer in production.

## The Build

**Steps I actually followed:**

1. Audited the existing repo structure and found `ai-engineer-book/` duplicating three root-level files (`README.md`, `ROADMAP.md`, `BOOK_OUTLINE.md`) exactly, with `CLAUDE.md` already documenting the flattened structure as if the duplication didn't exist.
2. Flattened the repo: moved every subfolder up to root, deleted the duplicate files, removed the now-empty `ai-engineer-book/` directory.
3. Added missing orientation READMEs to folders that didn't have one (`00_meta/`, `04_data_assets/`, `05_research_notes/`, `08_reviews_feedback/`), matching the pattern already used elsewhere.
4. Ran `git init`, added a `.gitignore` (`.DS_Store`, `__pycache__/`, `.env`, `.venv/`, `node_modules/`), and made the first commit.
5. Renamed the default branch to `main`.
6. Wrote a split `LICENSE`: MIT for code (`02_exercises/`, `03_projects/`, `06_tools_scripts/`), all-rights-reserved for the manuscript and other written content, since the book text and the code have different reuse implications.
7. Rewrote `README.md` with an actual orientation section instead of three placeholder lines.
8. Added `.github/workflows/ci.yml`: a real, working check (not a no-op stub) that fails the build if any em dash shows up anywhere in `01_manuscript/`, with a placeholder comment for future project-specific lint/type-check/test steps once real code lands in `03_projects/`.
9. Realized `07_career_prep/JOB_SEARCH_TRACKER.csv` would eventually hold real company names and application statuses, which shouldn't be public while actively interviewing. Gitignored the real file, committed a headers-only `JOB_SEARCH_TRACKER.template.csv` instead so the schema stays visible without the data.
10. Created the public GitHub repo (`ai-engineer-journal`), added it as `origin`, and pushed.
11. Watched CI fail on the first real push, not because of anything in Chapter 1, but because of the em dash baked into all twenty-three unwritten chapter placeholder templates. Fixed all twenty-three in one pass, pushed again, watched it go green.

**Where to find the actual output:** the repo itself, at `github.com/brunomoreira86/ai-engineer-journal`, plus `planning_journal/2026-08-13-repo-structure-audit.md` for the reasoning behind the structural cleanup.

## The Debrief

**What broke:** CI, on the very first real push, catching a mistake across twenty-three files that had been sitting there, wrong, since before this book had a single real chapter in it. I would not have caught this by reading. I only caught it by automating the check and letting it run against everything, not just the file I was actively thinking about.

**What I'd change:** nothing about the outcome, this is exactly what CI is supposed to do, but it's worth naming that I only wrote the check because of a style rule from Chapter 1's feedback, not because I planned base-camp setup around anticipating my own future mistakes. Good infrastructure often gets built reactively, right after the first time its absence costs you something small. The trick is making sure it's small when that happens, not large.

**What this connects to:** Git and CI fundamentals sit in Tier 1 of the skill gap matrix, the baseline bar nearly every posting assumes rather than states. This chapter is the difference between assuming I have that baseline and actually having exercised it: a real repo, a real push, a real CI failure caught and fixed in public.

## Status
- [x] Story drafted
- [x] Concept researched and verified
- [x] Build completed and tested
- [x] Debrief written
- [ ] Chapter reviewed
