from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    description = Column(String)

    status = Column(String, default="active")

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User")