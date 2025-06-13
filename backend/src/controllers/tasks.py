from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from ..config.database import get_db

from ..services.tasks import save_task, list_tasks, get_task, update_task, delete_task
from ..dto.tasks import CreateTaskDto, UpdateTaskDto

router = APIRouter()

@router.post('/') # /api/tasks/
async def create(task: CreateTaskDto, db=Depends(get_db)):
    """
    Create a new task.
    """
    new_task = save_task(task, db)
    return JSONResponse(
        status_code=201,
        content={
            "status": "CREATED",
            "message": "Task created successfully",
            "data": new_task
        }
    )

@router.get('/') # /api/tasks/
async def list(page: int = 1, limit: int = 10, title: str = None, db=Depends(get_db)):
    """
    List all tasks with pagination and optional title filter.
    """
    tasks = list_tasks(db, page, limit, title)
    return JSONResponse(
        status_code=200,
        content={
            "status": "OK",
            "message": "Tasks retrieved successfully",
            "data": tasks
        }
    )

@router.get('/{task_id}') # /api/tasks/{task_id}
async def get_single(task_id: int, db=Depends(get_db)):
    """
    Get a specific task by ID.
    """
    task = get_task(task_id, db)

    return JSONResponse(
        status_code=200,
        content={
            "status": "OK",
            "message": "Task retrieved successfully",
            "data": task
        }
    )

@router.put('/{task_id}') # /api/tasks/{task_id}
async def update(task_id: int, task_data: UpdateTaskDto, db=Depends(get_db)):
    """
    Update a specific task by ID.
    """
    updated_task = update_task(task_id, task_data, db)
    return JSONResponse(
        status_code=200,
        content={
            "status": "OK",
            "message": "Task updated successfully",
            "data": updated_task
        }
    )

@router.delete('/{task_id}') # /api/tasks/{task_id}
async def delete(task_id: int, db=Depends(get_db)):
    """
    Delete a specific task by ID.
    """
    result = delete_task(task_id, db)
    return JSONResponse(
        status_code=200,
        content={
            "status": "OK",
            "message": result["message"]
        }
    )