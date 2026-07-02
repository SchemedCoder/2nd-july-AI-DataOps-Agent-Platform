import pandas as pd
from datetime import datetime


def read_pipeline_logs(pipeline_name):
    df = pd.read_csv("data/pipeline_runs.csv")

    logs = df[df["pipeline_name"] == pipeline_name]

    return logs.to_dict(orient="records")


def run_sql_checks():
    df = pd.read_csv("data/warehouse_metrics.csv")

    anomalies = []

    for _, row in df.iterrows():

        if row["null_percentage"] > 10:
            anomalies.append(
                f"{row['table_name']} HIGH_NULL_RATE"
            )

        if row["duplicate_percentage"] > 5:
            anomalies.append(
                f"{row['table_name']} DUPLICATE_SPIKE"
            )

        if row["freshness_minutes"] > 60:
            anomalies.append(
                f"{row['table_name']} STALE_DATA"
            )

    return anomalies


def create_incident(pipeline_name, issue_type, severity):
    incident = {
        "incident_id": f"INC-{datetime.now().timestamp()}",
        "pipeline_name": pipeline_name,
        "issue_type": issue_type,
        "severity": severity
    }

    return incident


def restart_pipeline(pipeline_name):
    return {
        "pipeline_name": pipeline_name,
        "status": "RESTART_TRIGGERED"
    }
