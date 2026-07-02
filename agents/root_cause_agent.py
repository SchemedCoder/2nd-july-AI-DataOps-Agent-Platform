import pandas as pd


def detect_root_cause(error_message):
    error = str(error_message).lower()

    if "schema" in error:
        return {
            "root_cause": "Schema Drift",
            "confidence": 0.95
        }

    if "duplicate" in error:
        return {
            "root_cause": "Duplicate Spike",
            "confidence": 0.91
        }

    if "null" in error:
        return {
            "root_cause": "Null Spike",
            "confidence": 0.89
        }

    if "sla" in error:
        return {
            "root_cause": "SLA Breach",
            "confidence": 0.97
        }

    return {
        "root_cause": "Unknown",
        "confidence": 0.50
    }


if __name__ == "__main__":
    df = pd.read_csv("data/pipeline_runs.csv")

    failed = df[df["status"] == "FAILED"]

    for _, row in failed.iterrows():
        result = detect_root_cause(row["error_message"])
        print(row["pipeline_name"], result)
