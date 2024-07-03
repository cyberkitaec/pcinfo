from typing import Annotated
from fastapi import APIRouter, Depends

from api.depends import metrics_service
from services.metrics import MetricsService

router = APIRouter(prefix='/metrics', tags=['Metrics'])


@router.get("")
async def get_all(metrics_service: Annotated[MetricsService, Depends(metrics_service)],):
    users = await metrics_service.get_all_metrics()
    return users

@router.get("/limit/{limit}")
async def get_limit(metrics_service: Annotated[MetricsService, Depends(metrics_service)], limit: int = None):
    users = await metrics_service.get_limit_metrics(limit)
    return users