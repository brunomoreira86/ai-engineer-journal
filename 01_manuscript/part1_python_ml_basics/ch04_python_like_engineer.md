# Chapter 4: Writing Python Like an Engineer, Not a Student

## The Story

I didn't have a real messy script sitting around to use for this chapter, and I decided against faking one up as if it came from a real AskDila incident. So instead we built one on purpose: a script a founder would plausibly write at 11pm to answer one question fast, how many signups do we have, broken down by industry, and which ones are worth calling first. Global variables, no type hints, one long procedural block mixing file reading, math, and print statements, and a `# TODO clean this up later lol` comment that was never going to happen on its own.

That last part is the honest bit. I've written that exact comment for real, more than once, in more than one codebase. The script was invented for this chapter. The habit it represents isn't.

The interesting part wasn't writing the messy version, that took about two minutes. It was checking, afterward, that neither the tests nor mypy would have caught anything if I hadn't first pinned down exactly what the ugly script actually output. I ran it, wrote down the output, then refactored, then ran the new version and diffed the two outputs by eye. That step is easy to skip when you're excited about clean code and forget that "clean" and "correct" are two separate claims.

Neither pytest nor Python itself have any idea, they can't, whether a refactor changed behavior unless you've decided in advance what the behavior was supposed to be.

## The Concept

"Writing Python like an engineer" isn't really about syntax. The messy script and the refactored one do the same job; a beginner and a senior engineer can both technically produce working output. What separates them is what happens six months later when the CSV format changes, or someone else has to read the code, or a bug shows up in production at 2am.

Three things carry most of that weight, and none of them are exotic:

**Types.** A `Signup` dataclass with `company_name: str`, `industry: str`, `employee_count: int` isn't decoration, it's a contract. Once that contract exists, mypy can catch a whole category of bugs (wrong field name, wrong type passed somewhere) before the code ever runs. The untyped version only finds out at runtime, if you're lucky enough to hit the exact input that breaks it.

**Function boundaries.** The messy script has one function: the whole file, top to bottom. Nothing in it can be tested in isolation, because nothing in it is isolated. Splitting `load_signups`, `industry_breakdown`, `average_employee_count`, and `hot_leads` into separate pure functions (no I/O, no printing, just data in and data out) is what actually makes testing possible. The CLI layer becomes a thin wrapper that calls those functions and prints the result, nothing more.

**Tests as a written record of intent.** `test_average_employee_count_empty_list` exists because an empty signup list would otherwise divide by zero, a real bug the original script had and never surfaced simply because nobody had tried it with zero rows yet. The test doesn't just catch that bug, it documents that the empty case was considered on purpose, which the original code never communicated to anyone reading it.

None of this is unique to AI engineering. It's the same discipline any production Python service needs, and it's exactly what the job postings from Chapter 1 assumed without naming: nobody lists "writes testable functions" as a requirement, because not being able to is disqualifying before the conversation starts.

## The Build

**Steps I actually followed:**

1. Wrote the messy baseline (`ch04_before_messy_signup_report.py`): a single script, no types, no tests, one function that does everything, plus a synthetic signups CSV of fictional small Austrian businesses (real script pattern, invented data, no real AskDila signups per the repo's open-source policy).
2. Ran it and recorded its exact output as the regression baseline: total count, per-industry breakdown, average employee count, hot-leads list.
3. Set up a Python virtual environment at the repo root (`.venv/`, gitignored) and installed `pytest` and `mypy` via a new `requirements-dev.txt`, since neither was available yet.
4. Pulled the data model out into a typed `Signup` dataclass (`signup_report/models.py`).
5. Split the logic into pure, typed functions in `signup_report/report.py`: `load_signups`, `industry_breakdown`, `average_employee_count`, `hot_leads`, each with a single job and no side effects.
6. Wrote a thin `signup_report/cli.py` entrypoint whose only job is calling those functions and printing the result.
7. Wrote six pytest tests covering each function, including the empty-list edge case the original script never handled.
8. Ran `mypy --strict` against the module and fixed everything it flagged rather than suppressing it, configured via a `pyproject.toml` in the exercise folder.
9. Ran the refactored CLI against the same CSV and confirmed the output matched the messy version's output exactly, line for line.
10. Wired both checks into CI (`.github/workflows/ci.yml`): install `requirements-dev.txt`, then run `pytest` and `mypy --strict` against this exercise on every push, so this isn't a claim I'm making once, it's continuously verified.

**Where to find the actual output:** `02_exercises/part1/ch04_before_messy_signup_report.py` (the original), `02_exercises/part1/signup_report/` (the refactor), `02_exercises/part1/tests/test_report.py`, and `02_exercises/part1/ch04_exercise.md` for the reproducible version of this exercise.

## The Debrief

**What broke:** nothing dramatic this time, which is itself worth naming. The interesting failure mode in this chapter wasn't a bug, it was the temptation to skip step 2 (recording the baseline output) because the refactor felt obviously correct while I was writing it. It wasn't obviously correct. It was correct because I checked.

**What I'd change:** I'd build the habit of writing the "before" behavior down as an actual test (a golden-output test comparing full stdout) rather than eyeballing a diff once, by hand. I did it manually here because the exercise is small enough that eyeballing was reliable, but that stops being true the moment a script is bigger than one screen.

**What this connects to:** Python fluency sits at the very base of Tier 1 in the skill gap matrix, the assumption every posting makes and states nowhere. Chapter 5 builds directly on this: the same `Signup` dataclass pattern becomes a Pydantic schema the moment this logic needs to sit behind an API instead of a CLI.

## Status
- [x] Story drafted
- [x] Concept researched and verified
- [x] Build completed and tested
- [x] Debrief written
- [ ] Chapter reviewed
