from repository.generaldata_repository import GeneralDataRepository
from repository.metrics_repository import MetricsRepository
from services.metrics import MetricsService
from services.generaldata import GeneralDataService

def generaldata_service():
    return GeneralDataService(GeneralDataRepository)

def metrics_service():
    return MetricsService(MetricsRepository)