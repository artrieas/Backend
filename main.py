from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, crud
from .models import SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks/", response_model=schemas.TaskList)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

@app.get("/tasks/", response_model=List[schemas.TaskList])
def list_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db=db)

@app.delete("/tasks/{task_id}", response_model=schemas.TaskList)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db=db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks/bulk_add/", response_model=List[schemas.TaskList])
def bulk_add_tasks(task_list: List[schemas.TaskCreate], db: Session = Depends(get_db)):
    return crud.bulk_add_tasks(db=db, task_list=task_list)

@app.delete("/tasks/bulk_delete/", response_model=List[int])
def bulk_delete_tasks(task_ids: List[int], db: Session = Depends(get_db)):
    return crud.bulk_delete_tasks(db=db, task_ids=task_ids)
