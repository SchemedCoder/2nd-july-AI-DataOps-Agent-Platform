def recommend_fix(root_cause):

    fixes = {
        "Schema Drift": """
1. Compare source schema with target schema
2. Update transformation logic
3. Re-run failed pipeline
""",

        "Duplicate Spike": """
1. Check upstream deduplication
2. Validate primary keys
3. Backfill corrected records
""",

        "Null Spike": """
1. Validate source extraction
2. Check null handling logic
3. Re-run ingestion
""",

        "SLA Breach": """
1. Inspect resource bottlenecks
2. Scale compute
3. Restart delayed job
"""
    }

    return fixes.get(
        root_cause,
        "Manual investigation required"
    )


if __name__ == "__main__":
    print(recommend_fix("Schema Drift"))
