from typing import Union

from fastapi import FastAPI
from . import schemas, models

from .database import engine


app = FastAPI()

models.Base.metadata.create_all(engine)


@app.post("/blog")
async def create(request: schemas.Blog):
    return request
