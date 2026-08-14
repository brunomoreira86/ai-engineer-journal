# 2026-08-14 — 14-day Python plan adopted, split into personal vs. book tracks

**Context:** Bruno brought a detailed 14-day Python-for-AI-engineering plan (built around one running project, an AI Booking Request Parser: FastAPI + Pydantic + LLM extractor), sourced externally, and asked how it should fit given the earlier decision to keep generic Python-fundamentals content out of the book itself.

**Decision:**
- Split the plan: Days 1-8 (Python fundamentals: syntax, collections, functions, classes, files, pytest basics) stay personal practice only, no manuscript chapter comes from them.
- Days 9-14 (FastAPI, service architecture, LLM extractor, API testing, Docker) formally absorbed into Chapter 5 ("APIs, JSON, and the Contracts That Hold Systems Together"). Updated `PROJECT_BOARD.csv` P1-02's hands-on exercise and DoD to reflect the booking-parser project instead of the original generic placeholder.
- Adopted `uv` for environment/dependency management starting with this project. Chapter 4's plain venv + pip setup stays as-is (already shipped, not worth redoing).
- Scaffolded `02_exercises/part1/ai_booking_parser/` with `PLAN.md` (the full daily plan) and `NOTES.md` (interview Q&A log template), but deliberately did not write any of Day 1's actual code, that's Bruno's to write himself so the learning actually lands, with support/review rather than generated solutions.

**Why:** The plan's Days 9-14 output maps almost exactly onto what Chapter 5 already needed, and closes a real, previously-flagged gap (LLM APIs self-rated 3/5 but "heavy user, not builder" per `SKILL_GAP_MATRIX.md`). A booking-request parser also fits AskDila's actual small-business use case better than a generic FastAPI tutorial project would, reinforcing the book's AskDila-testbed thread. Days 1-8 don't map to a salary-relevant, book-worthy skill on their own, same reasoning as the earlier decision to keep Python fundamentals out of the manuscript.

**Reconsider if:** the Days 9-14 build doesn't end up matching Chapter 5's original "auth, rate limiting" scope closely enough, may need a follow-up chapter or an explicit scope note if something from the original P1-02 definition doesn't get covered.
