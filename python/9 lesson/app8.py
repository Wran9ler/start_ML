from fastapi import FastAPI, HTTPException, Depends
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()


def get_db():
    with psycopg2.connect(
            dbname="startml",
            host="postgres.lab.karpov.courses",
            user="robot-startml-ro",
            password="pheiph0hahj1Vaif",
            port=6432,
            cursor_factory=RealDictCursor,
    ) as conn:
        return conn


# Обратите внимание, как принимаем: db = Depends(get_db)
# нельзя делать db = get_db() - оно будет работать, но создаст соединение только один раз при импорте endpoint
# по-хорошему, стоит отдать вызов get_db на откуп fastapi (через Depends),
# т.к. он может сделать кеширование, переиспользование и т.п.
@app.get("/user/{id}")
def get_user(id: int, db=Depends(get_db)):
    with db.cursor() as cursor:
        cursor.execute(
            """SELECT gender, age, city FROM "user" WHERE id=%(user_id)s""",
            {"user_id": id},
        )
        result = cursor.fetchone()
    if result is None:
        raise HTTPException(404, "user not found")
    return result
