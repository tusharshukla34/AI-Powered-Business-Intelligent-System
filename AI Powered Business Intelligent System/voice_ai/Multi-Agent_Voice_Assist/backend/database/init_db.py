from backend.database.db import engine
from sqlalchemy import text

with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            amount FLOAT,
            date TEXT
        )
    """))

    # sample data
    conn.execute(text("""
        INSERT INTO expenses (category, amount, date) VALUES
        ('food', 500, '2024-04-01'),
        ('shopping', 500, '2024-04-02'),
        ('travel', 200, '2024-04-03'),
        ('food', 300, '2024-04-04')
    """))

    conn.commit()

print("✅ Database created")