from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.task_schema import TaskCreate, TaskResponse
from app.models.task_model import Task
from app.core.database import get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):

    new_task = Task(
        title=task.title,
        description=task.description,
        project_id=task.project_id,
        assigned_to=task.assigned_to
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    project_id: int | None = None,
    db: Session = Depends(get_db)
):

    query = db.query(Task)

    if project_id:
        query = query.filter(Task.project_id == project_id)

    tasks = query.all()

    return tasks