from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
user = "admin"
password = "admin"
host = "to-do_db"
port = 5432
db_name = "todo"

# Create the database connection
engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Import Tables in the database
from ..models.Task import Task

Base.metadata.create_all(bind=engine)


# Dependency to get the database session
def get_db():
    global SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()