"""Business logic for metrics."""

from datetime import datetime

from src.models.metrics import Metrics

def current_metrics(service: str) -> Metrics:
    return Metrics(service=service, status='ok', now_utc=datetime.utcnow().isoformat())
