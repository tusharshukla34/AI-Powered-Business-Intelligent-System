from backend.graph.state import AgentState
from backend.config.llm import get_llm

def router_node(state: AgentState) -> AgentState:
    query = state["user_input"]

    llm = get_llm()

    prompt = f"""
    You are an intelligent router.

    Your job is to classify the user's query into ONE of these categories:
    
    - expense → for finance, spending, budgeting
    - retail → for inventory, stock, products
    - data → for analysis, insights, trends

    ONLY return one word: expense, retail, or data

    User query: {query}
    """

    response = llm.invoke(prompt)

    decision = response.content.strip().lower()

    if "expense" in decision:
        decision = "expense"
    elif "retail" in decision:
        decision = "retail"
    elif "data" in decision:
        decision = "data"
    else:
        decision = "data"

    state["agent_type"] = decision

    return state