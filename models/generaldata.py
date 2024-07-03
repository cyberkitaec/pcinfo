from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base

from schemas.generaldata import GeneralDataSchema

class GeneralData(Base):
    __tablename__ = "general_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    hostname: Mapped[str]
    username: Mapped[str]
    count_cpu: Mapped[int]
    logic_cpu: Mapped[int]


    def to_read_model(self) -> GeneralDataSchema:
        return GeneralDataSchema(
            id=self.id,
            hostname=self.hostname,
            username=self.username,
            count_cpu=self.count_cpu,
            logic_cpu=self.logic_cpu
        )

