import csv
from collections import Counter
from pathlib import Path

from signup_report.models import Signup

DEFAULT_HOT_LEAD_THRESHOLD = 10


def load_signups(csv_path: Path) -> list[Signup]:
    """Read a signups CSV and parse it into a list of Signup records."""
    # LEARN: Path.open() instead of the built-in open() because csv_path is a
    # pathlib.Path, not a string. Using `with` guarantees the file gets closed
    # even if something below raises, unlike the messy version's f.close().
    with csv_path.open(newline="") as f:
        reader = csv.DictReader(f)
        # LEARN: this is a list comprehension, it builds the whole list in one
        # expression instead of an empty list + a for loop + .append() each
        # time. Same result as the messy script's loop, more compact, and it
        # reads as "for each row, construct a Signup" rather than a sequence
        # of mutations to track.
        return [
            Signup(
                company_name=row["company_name"],
                industry=row["industry"],
                employee_count=int(row["employee_count"]),
            )
            for row in reader
        ]


def industry_breakdown(signups: list[Signup]) -> dict[str, int]:
    """Count signups per industry."""
    # LEARN: Counter is a stdlib dict subclass built exactly for this: give it
    # any iterable and it counts occurrences. Replaces the messy version's
    # manual "if key in dict, increment, else set to 1" pattern in one line.
    return dict(Counter(s.industry for s in signups))


def average_employee_count(signups: list[Signup]) -> float:
    """Mean employee count across all signups. 0.0 for an empty list."""
    # LEARN: this empty-list guard is the fix for the messy script's
    # ZeroDivisionError bug. Deciding what an empty input should do (here:
    # return 0.0 instead of crashing) is a real design choice, not just
    # defensive noise, and test_average_employee_count_empty_list exists
    # specifically to lock this decision in.
    if not signups:
        return 0.0
    return sum(s.employee_count for s in signups) / len(signups)


def hot_leads(
    signups: list[Signup], threshold: int = DEFAULT_HOT_LEAD_THRESHOLD
) -> list[str]:
    """Company names with fewer employees than the threshold (our easiest sell)."""
    # LEARN: threshold: int = DEFAULT_HOT_LEAD_THRESHOLD is a default
    # argument, callers can do hot_leads(signups) and get 10, or
    # hot_leads(signups, threshold=3) to override it. The messy version had
    # 10 hardcoded inline with no way to change it without editing the loop.
    return [s.company_name for s in signups if s.employee_count < threshold]
