from backend.graph.state import AgentState
from backend.config.llm import get_llm

def retail_agent(state: AgentState) -> AgentState:
    query = state["user_input"]

    llm = get_llm()

    prompt = f"""
    You are a retail inventory expert.

    Your job:
    - Monitor stock
    - Suggest restocking
    - Optimize inventory

    User query: {query}
    """

    response = llm.invoke(prompt)

    state["response"] = response.content

    return state