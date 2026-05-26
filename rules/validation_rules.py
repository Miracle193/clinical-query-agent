# rules/validation_rules.py
RULES = {

    "MISSING_BP": {
        "rule_id": "VAL-001",
        "severity": "Medium",
        "message": "Missing BP",
        "recommendation":
            "Please verify and enter blood pressure value."
    },

    "MISSING_AGE": {
        "rule_id": "VAL-002",
        "severity": "Medium",
        "message": "Missing Age",
        "recommendation":
            "Please verify and enter age value."
    },

    "AGE_RANGE": {
        "rule_id": "VAL-003",
        "age_min": 18,
        "age_max": 120,
        "severity": "High",
        "message": "Unrealistic Age",
        "recommendation":
            "Verify subject age against source documents."
    },

    "VISIT_ORDER": {
        "rule_id": "VAL-004",
        "severity": "High",
        "message":
            "Visit 2 occurs before Visit 1",
        "recommendation":
            "Confirm visit chronology."
    },

    "PREGNANCY_CHECK": {
        "rule_id": "VAL-005",
        "severity": "High",
        "message":
            "Invalid pregnancy status for male subject",
        "recommendation":
            "Review subject demographics."
    },

    "INVALID_DATE": {
        "rule_id": "VAL-005",
        "severity": "Low",
        "message":
            "Invalid Visit 1 date",
        "recommendation":
            "Correct date format."
    }

}