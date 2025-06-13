from sqlalchemy.orm import Session

from ..util.http_error import HttpError
from ..dto.tasks import CreateTaskDto, UpdateTaskDto, TaskDto
from ..models.Task import Task

def save_task(task: CreateTaskDto, db: Session):
    """
    Save a task to the database.
    """
    new_task = Task(**task.model_dump())

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return TaskDto.model_validate(new_task).model_dump(mode="json")

def list_tasks(db: Session, page: int = 1, limit: int = 10, title: str = None):
    """
    List all tasks from the database.
    """
    tasks = db.query(Task)
    if title:
        tasks = tasks.filter(Task.title.ilike(f"%{title}%"))
    tasks = tasks.offset((page - 1) * limit).limit(limit).all()
    return [TaskDto.model_validate(task).model_dump(mode="json") for task in tasks]

def get_task(task_id: int, db: Session):
    """
    Get a task by its ID.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HttpError(
            status_code=404,
            status="NOT_FOUND",
            message="Task not found",
            detail=f"Task with ID {task_id} does not exist."
        )
    return TaskDto.model_validate(task).model_dump(mode="json")

def update_task(task_id: int, task_data: UpdateTaskDto, db: Session):
    """
    Update a task by its ID.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HttpError(
            status_code=404,
            status="NOT_FOUND",
            message="Task not found",
            detail=f"Task with ID {task_id} does not exist."
        )

    for key, value in task_data.model_dump().items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return TaskDto.model_validate(task).model_dump(mode="json")

def delete_task(task_id: int, db: Session):
    """
    Delete a task by its ID.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HttpError(
            status_code=404,
            status="NOT_FOUND",
            message="Task not found",
            detail=f"Task with ID {task_id} does not exist."
        )

    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}