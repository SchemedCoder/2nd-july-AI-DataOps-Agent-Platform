import pandas as pd


def run_sql_diagnostics():
    df = pd.read_csv("data/warehouse_metrics.csv")

    anomalies = []

    for _, row in df.iterrows():

        if row["null_percentage"] > 10:
            anomalies.append({
                "table": row["table_name"],
                "issue": "HIGH_NULL_RATE"
            })

        if row["duplicate_percentage"] > 5:
            anomalies.append({
                "table": row["table_name"],
                "issue": "DUPLICATE_SPIKE"
            })

        if row["freshness_minutes"] > 60:
            anomalies.append({
                "table": row["table_name"],
                "issue": "STALE_DATA"
            })

    return anomalies


if __name__ == "__main__":
    results = run_sql_diagnostics()
    print(results)
