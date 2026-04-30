from langgraph.graph import StateGraph, END

from backend.graph.state import AgentState
from backend.graph.router import router_node

from backend.agents.expense_agent import expense_agent
from backend.agents.retail_agent import retail_agent
from backend.agents.data_agent import data_agent


def build_graph():

    workflow = StateGraph(AgentState)

    # Nodes
    workflow.add_node("router", router_node)
    workflow.add_node("expense", expense_agent)
    workflow.add_node("retail", retail_agent)
    workflow.add_node("data", data_agent)

    # Entry point
    workflow.set_entry_point("router")

    # Routing logic
    def route_decision(state: AgentState):
        return state["agent_type"]

    workflow.add_conditional_edges(
        "router",
        route_decision,
        {
            "expense": "expense",
            "retail": "retail",
            "data": "data",
        }
    )

    # End points
    workflow.add_edge("expense", END)
    workflow.add_edge("retail", END)
    workflow.add_edge("data", END)

    return workflow.compile()