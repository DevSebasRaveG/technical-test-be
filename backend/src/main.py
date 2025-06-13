from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .util.http_error import HttpError

app = FastAPI()


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(HttpError)
async def handle_error(_, exc: HttpError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": exc.status,
            "message": exc.message,
            "detail": exc.detail
        }
    )

@app.get("/")
async def root():
    return {"message": "Hello, World"}


# Import routers
from .controllers.tasks import router as tasks_router

app.include_router(
    tasks_router,
    prefix="/api/tasks",
    tags=["tasks"]
)