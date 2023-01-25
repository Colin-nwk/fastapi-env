from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.post("/blog")
async def create():
    return "creating"
