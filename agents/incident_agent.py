from root_cause_agent import detect_root_cause
from remediation_agent import recommend_fix
import pandas as pd


def generate_incident_reports():
    df = pd.read_csv("data/pipeline_runs.csv")
    failed = df[df["status"] == "FAILED"]

    reports = []

    for _, row in failed.iterrows():

        root = detect_root_cause(
            row["error_message"]
        )

        fix = recommend_fix(
            root["root_cause"]
        )

        report = {
            "pipeline": row["pipeline_name"],
            "root_cause": root["root_cause"],
            "confidence": root["confidence"],
            "recommended_fix": fix
        }

        reports.append(report)

    return reports


if __name__ == "__main__":
    reports = generate_incident_reports()

    for report in reports:
        print(report)
