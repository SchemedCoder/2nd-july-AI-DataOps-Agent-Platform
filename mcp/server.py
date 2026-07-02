from fastapi import FastAPI
from mcp.tools import (
    read_pipeline_logs,
    run_sql_checks,
    create_incident,
    restart_pipeline
)

app = FastAPI(
    title="AI DataOps MCP Server"
)


@app.get("/")
def root():
    return {"message": "MCP Server Running"}


@app.get("/logs/{pipeline_name}")
def logs(pipeline_name):
    return read_pipeline_logs(pipeline_name)


@app.get("/sql-checks")
def sql_checks():
    return run_sql_checks()


@app.post("/incident")
def incident(
    pipeline_name: str,
    issue_type: str,
    severity: str
):
    return create_incident(
        pipeline_name,
        issue_type,
        severity
    )


@app.post("/restart/{pipeline_name}")
def restart(pipeline_name):
    return restart_pipeline(pipeline_name)
