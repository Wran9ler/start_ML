import datetime

from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: datetime.date


app = FastAPI()


@app.post("/user/validate")
def validate_user(user: User):
    return f"Will add user: {user.name} {user.surname} with age {user.age}"
