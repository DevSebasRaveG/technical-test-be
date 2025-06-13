from src.config.database import engine
from sqlalchemy import text

try:
    # Try to connect to the database
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Conexión exitosa a la base de datos!")
        # List all tables
        result = connection.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'"))
        print("\nTablas en la base de datos:")
        for row in result:
            print(f"- {row[0]}")
except Exception as e:
    print(f"Error al conectar a la base de datos: {str(e)}") 