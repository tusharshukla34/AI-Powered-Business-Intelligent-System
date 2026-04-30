from backend.database.db import get_connection
from sqlalchemy import text
import pandas as pd


def load_expense_data():
    with get_connection() as conn:
        result = conn.execute(text("SELECT * FROM expenses"))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())

    return df