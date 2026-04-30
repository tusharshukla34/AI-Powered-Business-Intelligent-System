from backend.graph.state import AgentState
from backend.database.db import get_connection
from sqlalchemy import text
from backend.config.llm import get_llm


def expense_agent(state: AgentState) -> AgentState:
    query = state["user_input"]
    history = state.get("history", [])

    with get_connection() as conn:
        # 🔥 total spending
        total = conn.execute(text("SELECT SUM(amount) FROM expenses")).scalar()

        # 🔥 category spending
        rows = conn.execute(text("""
            SELECT category, SUM(amount) as total
            FROM expenses
            GROUP BY category
        """)).fetchall()

    category_data = {row[0]: row[1] for row in rows}

    data_summary = f"""
    Total: {total}
    Category: {category_data}
    """

    llm = get_llm()

    prompt = f"""
You are a financial assistant.

RULES:
- One short sentence
- No greeting
- Use numbers

User:
{query}

Data:
{data_summary}

Answer:
"""

    response = llm.invoke(prompt)
    answer = response.content.strip()

    history.append(f"User: {query}")
    history.append(f"AI: {answer}")

    return {
        "response": answer,
        "history": history
    }