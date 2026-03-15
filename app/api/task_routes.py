from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.task_schema import TaskCreate, TaskResponse
from app.models.task_model import Task
from app.core.database import get_db
from fastapi import HTTPException
from app.schemas.task_schema import TaskUpdate

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):

    new_task = Task(
        title=task.title,
        description=task.description,
        status=task.status,
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

@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db)
):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task_update.title is not None:
        task.title = task_update.title

    if task_update.description is not None:
        task.description = task_update.description

    if task_update.status is not None:
        task.status = task_update.status

    db.commit()
    db.refresh(task)

    return task