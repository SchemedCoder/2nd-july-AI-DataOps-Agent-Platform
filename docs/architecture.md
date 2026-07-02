# Architecture

```text
Airflow / ETL Failure
        ↓
Webhook
        ↓
n8n Workflow
        ↓
MCP Tool Server
        ↓
AI Agents
 ├─ Root Cause Agent
 ├─ SQL Agent
 ├─ Remediation Agent
 └─ Incident Agent
        ↓
Slack / Jira / Email
```
