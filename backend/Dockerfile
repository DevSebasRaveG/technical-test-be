FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install alembic

COPY . .
COPY .env .env

# Initialize alembic if it doesn't exist
RUN if [ ! -d "alembic" ]; then \
    alembic init alembic && \
    echo 'from src.models import Base\n\ntarget_metadata = Base.metadata' > alembic/env.py; \
    fi

EXPOSE 8001

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]