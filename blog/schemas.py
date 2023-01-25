from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum


class Blog(BaseModel):
    title: str
    body: str
