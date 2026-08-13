# LEARN: a dataclass auto-generates __init__, __repr__, and __eq__ from the
# fields below, so you get a real typed object without writing that
# boilerplate by hand. frozen=True makes instances immutable after creation,
# which is what lets Signup("Acme", "retail", 5) == Signup("Acme", "retail", 5)
# work by value, and prevents accidentally mutating a record after it's loaded.
from dataclasses import dataclass


@dataclass(frozen=True)
class Signup:
    """A single row from the early-access signup CSV."""

    company_name: str
    industry: str
    employee_count: int
