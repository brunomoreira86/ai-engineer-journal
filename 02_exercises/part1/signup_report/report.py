import csv
from collections import Counter
from pathlib import Path

from signup_report.models import Signup

DEFAULT_HOT_LEAD_THRESHOLD = 10


def load_signups(csv_path: Path) -> list[Signup]:
    """Read a signups CSV and parse it into a list of Signup records."""
    with csv_path.open(newline="") as f:
        reader = csv.DictReader(f)
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
    return dict(Counter(s.industry for s in signups))


def average_employee_count(signups: list[Signup]) -> float:
    """Mean employee count across all signups. 0.0 for an empty list."""
    if not signups:
        return 0.0
    return sum(s.employee_count for s in signups) / len(signups)


def hot_leads(
    signups: list[Signup], threshold: int = DEFAULT_HOT_LEAD_THRESHOLD
) -> list[str]:
    """Company names with fewer employees than the threshold (our easiest sell)."""
    return [s.company_name for s in signups if s.employee_count < threshold]
