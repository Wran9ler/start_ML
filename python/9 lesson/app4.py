import datetime
from pydantic import BaseModel


class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: datetime.date
