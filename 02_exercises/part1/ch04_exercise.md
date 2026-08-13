# Chapter 4 Exercise: Convert a Messy Script into a Tested, Typed, Documented Module

- **Objective:** Take a real (if small) "founder hacked this together at 11pm" script and turn it into something you'd actually let a hiring manager read.
- **Prerequisites:** Python 3.12+, `pip install -r requirements-dev.txt` (pytest, mypy) from the repo root.
- **Steps:**
  1. Start from `ch04_before_messy_signup_report.py`, a script that reads a CSV of business signups and prints a summary (count by industry, average employee count, "hot leads" under a size threshold). Run it first and note its exact output, that's your regression baseline.
  2. Identify what makes it "messy": no type hints, no error handling, one giant procedural script mixing I/O, business logic, and printing, a raw dict instead of a real data model, no tests, a stray `# TODO clean this up later` that never happened.
  3. Pull the data model out first: a typed `Signup` record instead of a raw `dict[str, str]` from `csv.DictReader`.
  4. Split the single script into pure functions with type hints: one to load data, one per calculation (industry breakdown, average, hot leads). Pure functions (no I/O, no printing) are what you can actually unit test.
  5. Keep a thin CLI/entrypoint layer separate from the logic, its only job is to call the functions and print results.
  6. Write pytest tests for every pure function, including at least one edge case (e.g. an empty list).
  7. Run `mypy --strict` against the module and fix everything it flags, don't suppress it.
  8. Re-run the new version against the same input and confirm the output matches the messy version's output exactly. A refactor that changes behavior isn't a successful refactor.
- **Success criteria:** `pytest` green, `mypy --strict` clean, output identical to the original script.
- **Time estimate:** 1-2 hours.

**Reference output:** `signup_report/` (the refactored package), `tests/test_report.py`, and `ch04_before_messy_signup_report.py` (the untouched original, kept for comparison) all live in this same folder.
