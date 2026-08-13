from pathlib import Path

import pytest

from signup_report.models import Signup
from signup_report.report import (
    average_employee_count,
    hot_leads,
    industry_breakdown,
    load_signups,
)


@pytest.fixture
def sample_signups() -> list[Signup]:
    return [
        Signup("Bakery Blue", "food", 4),
        Signup("Nordwind Consulting", "consulting", 25),
        Signup("Sonnenberg Cafe", "food", 2),
    ]


def test_load_signups_parses_rows(tmp_path: Path) -> None:
    csv_path = tmp_path / "signups.csv"
    csv_path.write_text("company_name,industry,employee_count\nAcme,retail,5\n")

    signups = load_signups(csv_path)

    assert signups == [Signup("Acme", "retail", 5)]


def test_industry_breakdown_counts_per_industry(sample_signups: list[Signup]) -> None:
    assert industry_breakdown(sample_signups) == {"food": 2, "consulting": 1}


def test_average_employee_count(sample_signups: list[Signup]) -> None:
    assert average_employee_count(sample_signups) == pytest.approx(31 / 3)


def test_average_employee_count_empty_list() -> None:
    assert average_employee_count([]) == 0.0


def test_hot_leads_default_threshold(sample_signups: list[Signup]) -> None:
    assert hot_leads(sample_signups) == ["Bakery Blue", "Sonnenberg Cafe"]


def test_hot_leads_custom_threshold(sample_signups: list[Signup]) -> None:
    assert hot_leads(sample_signups, threshold=3) == ["Sonnenberg Cafe"]
