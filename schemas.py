from pydantic import BaseModel
from typing import Optional, List

class TaskCreate(BaseModel):
    title: str
    completed: Optional[bool] = False

class TaskUpdate(BaseModel):
    title: Optional[str]
    completed: Optional[bool]

class TaskList(BaseModel):
    id: int
    title: str
    completed: bool

    class Config:
        orm_mode = True
 