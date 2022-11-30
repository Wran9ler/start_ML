import datetime
from fastapi import FastAPI

app = FastAPI()


# обязательно укажем тип через двоеточие
# от current_date ожидается, что она будет иметь тип datetime.date
# от offset ожидается, что он будет иметь тип int
@app.get("/sum_date")
def sum_date(current_date: datetime.date, offset: int):
    # складывать date и int нельзя, будем складывать date и timedelta(days=...)
    return current_date + datetime.timedelta(days=offset)
