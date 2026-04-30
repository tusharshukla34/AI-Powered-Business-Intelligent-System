from backend.graph.state import AgentState
from backend.config.llm import get_llm

def data_agent(state: AgentState) -> AgentState:
    query = state["user_input"]

    llm = get_llm()

    prompt = f"""
    You are a data analyst.

    Your job:
    - Analyze data
    - Give insights
    - Explain trends

    User query: {query}
    """

    response = llm.invoke(prompt)

    state["response"] = response.content

    return state