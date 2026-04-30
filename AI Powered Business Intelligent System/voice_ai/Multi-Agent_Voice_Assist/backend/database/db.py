from sqlalchemy import create_engine, text

# 🔥 SQLite database file
DATABASE_URL = "sqlite:///backend/database/expenses.db"

engine = create_engine(DATABASE_URL, echo=False)


def get_connection():
    return engine.connect()