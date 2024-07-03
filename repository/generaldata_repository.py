from models.generaldata import GeneralData
from utils.abstactrepo import SQLAlchemyRepo


class GeneralDataRepository(SQLAlchemyRepo):
    model = GeneralData
