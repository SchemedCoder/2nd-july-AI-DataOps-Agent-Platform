from fastapi import FastAPI
import pandas as pd

app = FastAPI(
    title="AI DataOps API"
)


@app.get("/")
def root():
    return {
        "message": "AI DataOps API Running"
    }


@app.get("/incidents")
def incidents():
    df = pd.read_csv("data/incidents.csv")
    return df.to_dict(orient="records")


@app.get("/pipelines")
def pipelines():
    df = pd.read_csv("data/pipeline_runs.csv")
    return df.to_dict(orient="records")


@app.get("/metrics")
def metrics():
    df = pd.read_csv("data/warehouse_metrics.csv")
    return df.to_dict(orient="records")
