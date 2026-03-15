from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str
    status: str
    project_id: int
    assigned_to: int
    


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    project_id: int
    assigned_to: int

    class Config:
        from_attributes = True


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None