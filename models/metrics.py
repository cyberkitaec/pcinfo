from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base


class Metrics(Base):
    __tablename__ = "metrics"

    id: Mapped[int] = mapped_column(primary_key=True)
    cpu_usage: Mapped[float]
    memory_usage: Mapped[float]

    def to_read_model(self):
        pass
