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
