import pandas as pd
import json
import os

from engine.validator import validate


# Read CSV
df = pd.read_csv(
    "data/clinical_data.csv"
)


# Run validation
results = validate(df)


# Create output folder
os.makedirs(
    "output",
    exist_ok=True
)


# Save JSON
with open(
    "output/validation_results.json",
    "w"
) as file:

    json.dump(
        results,
        file,
        indent=4
    )


# Print results
print(
    json.dumps(
        results,
        indent=4
    )
)