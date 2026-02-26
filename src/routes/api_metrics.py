"""JSON API endpoints."""

from fastapi import APIRouter

from src.models.metrics import Metrics
from src.services.metrics_service import current_metrics

router = APIRouter(tags=['api'])

@router.get('/metrics', response_model=Metrics)
def metrics() -> Metrics:
    return current_metrics(service='developer-dashboard')
