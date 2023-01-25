from typing import Union

from fastapi import FastAPI
from blog.schemas import Blog


app = FastAPI()


@app.post("/blog")
async def create(request: Blog):
    return request
