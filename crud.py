from sqlalchemy.orm import Session
from .models import Task
from .schemas import TaskCreate, TaskUpdate

def create_task(db: Session, task: TaskCreate):
    new_task = Task(title=task.title, completed=task.completed)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db: Session):
    return db.query(Task).all()

def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    if task:
        db.delete(task)
        db.commit()
    return task

def bulk_delete_tasks(db: Session, task_ids: List[int]):
    db.query(Task).filter(Task.id.in_(task_ids)).delete(synchronize_session=False)
    db.commit()
    return task_ids
