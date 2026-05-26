import os
import logging
import pandas as pd

from dateutil.parser import parse
from rules.validation_rules import RULES

# Setup logging folder
os.makedirs("logs", exist_ok=True)

# Setup logging configuration
logging.basicConfig(
    filename="logs/validation.log",
    level=logging.INFO,
    format=(
        "%(asctime)s | " \
        "%(message)s"
    )
)

# Helper Function for Structured Findings
def create_issue(subject, rule):

    # Create structured output
    item = {
        "subject_id": subject,
        "rule_id": rule["rule_id"],
        "issue": rule["message"],
        "severity": rule["severity"],
        "recommendation": rule["recommendation"]
    }

    # Write audit logs
    logging.info(
        f"{subject}"
        f" | "
        f"{rule['rule_id']}"
        f" | "
        f"{rule['message']}"
    )

    return item


def is_valid_date(date):

    try:
        parse(str(date))
        return True

    except:
        return False


def validate(df):

    results = {}

    for _, row in df.iterrows():

        issues = []

        subject = row["subject_id"]

        # Missing checks
        if pd.isna(row["bp"]):
            issues.append(create_issue(subject, RULES["MISSING_BP"]))

        if pd.isna(row["age"]):
            issues.append(create_issue(subject, RULES["MISSING_AGE"]))

        # Range checks
        if pd.notna(row["age"]):

            if row["age"] < RULES["AGE_RANGE"]["age_min"] \
               or row["age"] > RULES["AGE_RANGE"]["age_max"]:
                issues.append(create_issue(subject, RULES["AGE_RANGE"]))

        # Date checks
        if not is_valid_date(row["visit1_date"]):
            issues.append(create_issue(subject, RULES["INVALID_DATE"]))

        # Logical checks
        if (
            is_valid_date(row["visit1_date"])
            and
            is_valid_date(row["visit2_date"])
        ):

            visit1 = parse(row["visit1_date"])
            visit2 = parse(row["visit2_date"])

            if visit2 < visit1:
                issues.append(create_issue(subject, RULES["VISIT_ORDER"]))

        # Cross-field checks
        if (
            row["gender"] == "Male"
            and
            row["pregnant"] == "Yes"
        ):

            issues.append(create_issue(subject, RULES["PREGNANCY_CHECK"]))

        if issues:
            results[subject] = issues

    return results