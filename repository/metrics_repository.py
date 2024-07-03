from models.metrics import Metrics
from utils.abstactrepo import SQLAlchemyRepo


class MetricsRepository(SQLAlchemyRepo):
    model = Metrics
