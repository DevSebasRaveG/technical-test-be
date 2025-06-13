from sqlalchemy import Column, Integer, String, Boolean, DateTime, func

from . import Base

class Task(Base):
    '''
    Task model using SQLAlchemy ORM.
    This model is going to be converted into a table in the database.
    '''

    __tablename__ = "tasks"

    id = Column("id", Integer, primary_key=True, index=True, autoincrement=True)
    title = Column("title", String(100), nullable=False)
    description = Column("description", String(500), nullable=True)
    completed = Column("completed", Boolean, nullable=False, default=False)
    created_at = Column("created_at", DateTime, nullable=False, server_default=func.now())