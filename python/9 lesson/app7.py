from fastapi import FastAPI
from fastapi import HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()


@app.get("/user/{id}")
def get_user(id: int):
    with psycopg2.connect(
            dbname="startml",
            host="postgres.lab.karpov.courses",
            user="robot-startml-ro",
            password="pheiph0hahj1Vaif",
            port=6432,
            cursor_factory=RealDictCursor,
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """SELECT gender, age, city FROM "user" WHERE id=%(user_id)s""",
                {"user_id": id},
            )
            result = cursor.fetchone()
    if result is None:
        raise HTTPException(404, "user not found")
    return result
