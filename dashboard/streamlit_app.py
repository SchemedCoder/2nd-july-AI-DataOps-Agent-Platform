import streamlit as st
import pandas as pd

st.title("AI DataOps Monitoring Dashboard")

incidents = pd.read_csv("data/incidents.csv")
pipelines = pd.read_csv("data/pipeline_runs.csv")
metrics = pd.read_csv("data/warehouse_metrics.csv")

st.header("Open Incidents")
st.dataframe(incidents)

st.header("Pipeline Runs")
st.dataframe(pipelines)

st.header("Warehouse Metrics")
st.dataframe(metrics)

failed_count = len(
    pipelines[pipelines["status"] == "FAILED"]
)

st.metric(
    label="Failed Pipelines",
    value=failed_count
)
