# Day Log

Plain-language recap after each day, what was actually learned and what tripped you up. Written for future-you, not for the book.

## Day 1: Python syntax basics, through a JS lens

**Setup:**
- `uv init` scaffolds a Python project: `pyproject.toml` (like `package.json`), a `main.py`, `.python-version`, and its own isolated `.venv` per project (like each Node project getting its own `node_modules`).
- Hit and understood a real `uv` error: a parent folder's `pyproject.toml` without a `[project]` table confused `uv`'s workspace detection. Fixed with `uv init --no-workspace`.
- `uv run main.py` runs a file inside the project's own environment automatically, no manual `activate` needed.

**Syntax, JS to Python:**
- No `const`/`let`/`var`, no semicolons. `x = 5` is the whole statement.
- `def name(args):` defines a function; the colon starts a block, and **indentation, not `{ }`, marks what's inside it**. This is syntax, not style, inconsistent indentation breaks the code.
- `if x:` / `else:`, same shape as JS but no parens around the condition and no braces around the body.
- `in` checks substring/membership: `"book" in text` (like JS's `.includes()`, but an operator, not a method).
- `.lower()` lowercases a string (like `.toLowerCase()`).
- f-strings: `f"hello {name}"`, the `f` prefix is what activates `{}` interpolation.
- `None` is Python's one "nothing" value (JS splits this into `null` and `undefined`).
- Python's `==` already does what JS's `===` does, no separate strict-equals operator needed.

**The real bug hit and fixed:** `NameError: name 'parse_message' is not defined`, caused by calling `parse_message()` from `main()` before `parse_message`'s own `def` had executed yet. **Python does not hoist function declarations** the way JS does; a function only exists from the moment its `def` line actually runs, top to bottom. Fixed by reordering the file so `parse_message` is defined before it's called.

**What got built:** `parse_message(message: str) -> dict`, a simple rule-based classifier that checks for booking-related keywords (`"book"`, `"table"`, `"reservation"`) using `in`/`or`/`.lower()`, and returns a dict tagging the message as `"booking"` or `"other"`. Tested against two sample messages, output confirmed correct.

**Known rough edge, on purpose:** the `or`-chain of keyword checks doesn't scale past a handful of words. Day 2 replaces it with a cleaner list-based approach.
