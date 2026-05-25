import pandas as pd
from dateutil.parser import parse
from rules.validation_rules import RULES


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
            issues.append("Missing BP")

        if pd.isna(row["age"]):
            issues.append("Missing Age")

        # Range checks
        if pd.notna(row["age"]):

            if row["age"] < RULES["age_min"] \
               or row["age"] > RULES["age_max"]:

                issues.append("Unrealistic Age")

        # Date checks
        if not is_valid_date(row["visit1_date"]):
            issues.append("Invalid Visit 1 date")

        # Logical checks
        if (
            is_valid_date(row["visit1_date"])
            and
            is_valid_date(row["visit2_date"])
        ):

            visit1 = parse(row["visit1_date"])
            visit2 = parse(row["visit2_date"])

            if visit2 < visit1:
                issues.append(
                    "Visit 2 occurs before Visit 1"
                )

        # Cross-field checks
        if (
            row["gender"] == "Male"
            and
            row["pregnant"] == "Yes"
        ):

            issues.append(
                "Invalid pregnancy status for male subject"
            )

        if issues:
            results[subject] = issues

    return results