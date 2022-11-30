from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def say_hello(a: int, b: int):
    return a + b
