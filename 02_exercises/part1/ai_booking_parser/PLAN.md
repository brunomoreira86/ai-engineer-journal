# AI Booking Request Parser: 14-Day Plan

Personal Python-relearning project (TypeScript/Node background, rusty on Python specifically), structured as one running build rather than scattered tutorials. Feeds Chapter 5 ("APIs, JSON, and the Contracts That Hold Systems Together") once Days 9-14 are done.

**Goal:** be able to say "I use Python to build and test AI-backed services, work with structured data, call external APIs, and expose reliable FastAPI endpoints," backed by a real, working, tested service, not a claim.

**Tooling:** `uv` for environment/dependency management (adopted here onward; Chapter 4 used plain venv + pip, that stays as-is, already shipped).

## Split: personal practice vs. book material

- **Days 1-8** (Python fundamentals: syntax, collections, functions, classes/dataclasses, files/JSON, pytest basics): personal practice only. Closing a rust gap, not producing book-worthy material. No manuscript chapter comes from these days.
- **Days 9-14** (FastAPI, service architecture, LLM extractor, API testing, Docker, README): this is Chapter 5's real hands-on deliverable. What actually gets built here is what Chapter 5 gets drafted from, not written in advance.

## Final project shape

A FastAPI service that accepts a booking-style message and returns validated structured data:

```json
{
  "intent": "booking_request",
  "customer_name": "Anna",
  "party_size": 4,
  "date": "2026-09-04",
  "time": "19:30",
  "confidence": 0.92
}
```

Target architecture by the end:

```text
ai_booking_parser/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── config.py
│   ├── services/
│   │   ├── extractor.py       # BookingExtractor interface
│   │   ├── rule_based.py      # RuleBasedExtractor
│   │   └── llm.py             # LLMExtractor
│   └── utils/
│       ├── dates.py
│       └── logging.py
├── tests/
│   ├── test_rule_based.py
│   ├── test_api.py
│   └── conftest.py
├── data/
│   └── booking_messages.json
├── .env.example
├── Dockerfile
├── README.md
├── NOTES.md          # interview Q&A log, one entry per day from Day 4 onward
└── pyproject.toml
```

## Daily plan

| Day | Learn | Build |
|---|---|---|
| 1 | Python syntax through a TS lens: variables, functions, conditionals, loops, f-strings, imports, venvs | `uv init`, write `parse_message(message: str) -> dict` using simple rules |
| 2 | `list`/`tuple`/`set`/`dict`, slicing, comprehensions, `enumerate`/`zip`/`sorted`/`any`/`all` | Parse a list of sample messages; dedupe with a `set`; group by intent with a `dict` |
| 3 | Functions in depth: positional/keyword args, defaults, `*args`/`**kwargs`, scope, docstrings | Refactor into `detect_intent`, `extract_party_size`, `extract_time`, `normalise_message` |
| 4 | Mutability, `is` vs `==`, copying, `None`, truthiness, exceptions | Custom `BookingParseError`; handle invalid/missing data; start `NOTES.md` |
| 5 | Classes, `dataclass`, type hints, `Enum`, basic protocols | Typed domain models: `BookingRequest`, `BookingIntent`, `ExtractionResult` |
| 6 | Files, JSON, CSV, `pathlib`, context managers | Load 30-50 sample messages from JSON; write results to JSON; handle malformed rows |
| 7 | `pytest`: assertions, fixtures, parametrization, mocks | 12+ tests: normal, malformed, missing info, duplicates, invalid dates |
| 8 | Project structure, `uv`, `.env`, logging, `ruff` | Restructure into `app/`/`tests`/`data`; add `.env.example`, `.gitignore`, `pyproject.toml`, `ruff`, logging |
| 9 | FastAPI: routes, request/response models, validation, status codes, OpenAPI | `POST /extract-booking`; run locally, check `/docs` |
| 10 | API error design, dependency injection basics, HTTP clients, timeouts/retries | `BookingExtractor` interface + `RuleBasedExtractor`, swappable without touching the route |
| 11 | Async Python: `async def`/`await`, I/O-bound concurrency, when not to use it | Make the endpoint async; simulated async provider call with timeout handling |
| 12 | LLM integration: prompts, structured JSON output, schema validation, retries, fallback | `LLMExtractor` (real API key if available, else deterministic mock); validate every result through Pydantic |
| 13 | FastAPI testing with `TestClient`, mocking external calls, unit vs integration | End-to-end test of `POST /extract-booking` with the LLM/provider mocked |
| 14 | Packaging, Docker, interview storytelling, review | Dockerfile, final README, architecture diagram in Markdown, record a 3-minute self walkthrough |

## Daily rhythm (avoid tutorial overload)

1. 30 min: read official docs or one focused lesson.
2. 75-120 min: apply it inside this project.
3. 15 min: from a blank file, write 3-5 small examples with no help.
4. 10 min: add one Q&A to `NOTES.md`.

## Day 14 standard (not "completed every lesson")

- Rebuild a small FastAPI endpoint without copying a tutorial.
- Explain the architecture and its trade-offs out loud.
- Write, run, and interpret `pytest` tests.
- Model and validate data with type hints and Pydantic.
- Handle errors and external API failures predictably.
- Explain a specific bug hit and how it got debugged.
- Demo the project locally via `/docs`.
