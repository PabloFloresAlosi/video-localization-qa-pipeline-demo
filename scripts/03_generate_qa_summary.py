"""
03_generate_qa_summary.py

Generates a simple QA summary from the issue report.

Outputs:
- Total issue count
- Issues by severity
- Issues by category
- Issues by status
"""

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
CSV_DIR = BASE_DIR / "csv"

QA_REPORT_PATH = CSV_DIR / "qa_report_sample.csv"


def read_qa_report():
    if not QA_REPORT_PATH.exists():
        raise FileNotFoundError(f"QA report not found: {QA_REPORT_PATH}")

    # The CSV uses semicolon separators for better LibreOffice compatibility.
    df = pd.read_csv(QA_REPORT_PATH, sep=";")
    df.columns = df.columns.str.strip()

    return df


def print_section(title):
    print("\n" + title)
    print("=" * len(title))


def main():
    print("QA Report Summary")
    print("=================")

    df = read_qa_report()

    print(f"\nTotal issues: {len(df)}")

    if "Severity" in df.columns:
        print_section("Issues by Severity")
        print(df["Severity"].value_counts().to_string())

    if "Category" in df.columns:
        print_section("Issues by Category")
        print(df["Category"].value_counts().to_string())

    if "Status" in df.columns:
        print_section("Issues by Status")
        print(df["Status"].value_counts().to_string())

    print("\nSummary generated successfully.")


if __name__ == "__main__":
    main()