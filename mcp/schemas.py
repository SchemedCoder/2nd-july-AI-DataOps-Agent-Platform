from pydantic import BaseModel


class PipelineRequest(BaseModel):
    pipeline_name: str


class IncidentRequest(BaseModel):
    pipeline_name: str
    issue_type: str
    severity: str


class SQLRequest(BaseModel):
    table_name: str
