import sys
from pathlib import Path

from signup_report.report import (
    average_employee_count,
    hot_leads,
    industry_breakdown,
    load_signups,
)


def print_report(csv_path: Path) -> None:
    signups = load_signups(csv_path)
    print(f"total signups: {len(signups)}")
    print("by industry:")
    for industry, count in industry_breakdown(signups).items():
        print(f"  {industry}: {count}")
    print(f"avg employees: {average_employee_count(signups):.1f}")
    print(f"hot leads: {hot_leads(signups)}")


def main() -> None:
    csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("signups.csv")
    print_report(csv_path)


if __name__ == "__main__":
    main()
