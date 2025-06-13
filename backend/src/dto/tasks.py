from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class CreateTaskDto(BaseModel):
    '''
    Task Creation Validation.
    '''
    title: str = Field(..., min_length=1, max_length=100, description="Title of the task")
    description: Optional[str] = Field(None, max_length=500, description="Description of the task")

class UpdateTaskDto(BaseModel):
    '''
    Task Update Validation.
    '''
    title: str = Field(..., min_length=1, max_length=100, description="Title of the task")
    description: str = Field(None, max_length=500, description="Description of the task")
    completed: bool = Field(..., description="Completion status of the task")

class TaskDto(BaseModel):
    '''
    Task Data Transfer Object for API responses.
    '''

    id: int = Field(..., description="Unique identifier of the task")
    title: str = Field(..., min_length=1, max_length=100, description="Title of the task")
    description: str = Field(None, max_length=500, description="Description of the task")
    completed: bool = Field(..., description="Completion status of the task")

    # Datetime, no string
    created_at: datetime = Field(..., description="Creation timestamp of the task")

    class Config:
        from_attributes = True