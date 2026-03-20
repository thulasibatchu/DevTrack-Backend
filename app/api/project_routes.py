from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.project_schema import ProjectCreate, ProjectResponse
from app.models.project_model import Project
from app.core.database import get_db
from app.api.dependencies import get_current_user
from app.models.user_model import User

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=ProjectResponse)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_project = Project(
        name=project.name,
        description=project.description,
        owner_id=current_user.id
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project

@router.get("/", response_model=list[ProjectResponse])
def get_projects(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    projects = db.query(Project).offset(skip).limit(limit).all()

    return projects