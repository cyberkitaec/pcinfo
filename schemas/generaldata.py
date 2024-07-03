from pydantic import BaseModel

class GeneralDataSchema(BaseModel):
    id: int
    hostname: str
    username: str
    count_cpu: int
    logic_cpu: int

    class Config:
        from_attributes = True