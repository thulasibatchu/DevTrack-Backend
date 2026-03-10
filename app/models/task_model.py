from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(String)

    status = Column(String, default="todo")

    project_id = Column(Integer, ForeignKey("projects.id"))

    assigned_to = Column(Integer, ForeignKey("users.id"))

    project = relationship("Project")

    user = relationship("User")