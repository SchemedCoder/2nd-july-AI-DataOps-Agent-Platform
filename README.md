# AI DataOps Agent Platform

An end-to-end AI-powered DataOps automation platform that uses n8n workflows, MCP-based agents, SQL diagnostics, and LLM reasoning to automatically detect, investigate, and remediate data pipeline failures.

---

## Problem Statement

Modern data teams spend significant time investigating:

- Failed ETL jobs
- Broken DAGs
- Schema drift
- Late-arriving data
- SLA breaches
- Warehouse anomalies

Manual investigation is slow and expensive.

This platform introduces AI agents that automate incident triage and root-cause analysis.

---

## Architecture

```text
Pipeline Failure Event
        ↓
n8n Trigger
        ↓
MCP Server
        ↓
Root Cause Agent
        ↓
SQL Diagnostic Agent
        ↓
Remediation Agent
        ↓
Incident Report + Alert
```

---

## Tech Stack

- Python
- n8n
- MCP (Model Context Protocol)
- FastAPI
- SQL
- DuckDB / Postgres
- Streamlit
- Docker
- GitHub Actions

---

## Core Agents

### Root Cause Agent
Detects pipeline failure reasons from logs.

### SQL Agent
Runs warehouse diagnostics.

### Remediation Agent
Suggests automated fixes.

### Incident Agent
Creates human-readable incident reports.

---

## Business Value

Useful for:

- Data Engineering teams
- Analytics Engineering teams
- Platform Engineering
- FinTech / SaaS companies
======================


## Run Instruction/Local Setup

Clone repository:

```bash
git clone https://github.com/yourusername/ai-dataops-agent-platform.git
cd ai-dataops-agent-platform
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run MCP server:

```bash
uvicorn mcp.server:app --reload
```

Server starts at:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Read Pipeline Logs

```http
GET /logs/{pipeline_name}
```

### Run SQL Checks

```http
GET /sql-checks
```

### Create Incident

```http
POST /incident
```

### Restart Pipeline

```http
POST /restart/{pipeline_name}
```
=============
## n8n Workflow

This project includes a sample n8n workflow demonstrating AI-based DataOps incident orchestration.

Workflow steps:

```text
Webhook Trigger
      ↓
Pipeline Failure Event
      ↓
AI Root Cause Analysis
      ↓
Incident Generation
      ↓
Alert Dispatch
```

The workflow JSON can be imported into n8n for live execution.

===========

## Run API

```bash
uvicorn api.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```
## REST API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Health Check |
| GET | `/logs/{pipeline_name}` | Retrieve pipeline execution logs |
| GET | `/sql-checks` | Run warehouse data quality diagnostics |
| POST | `/incident` | Create a new incident |
| POST | `/restart/{pipeline_name}` | Trigger pipeline restart |
| GET | `/incidents` | Retrieve all incidents |
| GET | `/pipelines` | Retrieve pipeline execution history |
| GET | `/metrics` | Retrieve warehouse metrics |
