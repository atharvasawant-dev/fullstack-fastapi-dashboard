"""Typed metrics model."""

from pydantic import BaseModel

class Metrics(BaseModel):
    service: str
    status: str
    now_utc: str
