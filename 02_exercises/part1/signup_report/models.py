from dataclasses import dataclass


@dataclass(frozen=True)
class Signup:
    """A single row from the early-access signup CSV."""

    company_name: str
    industry: str
    employee_count: int
