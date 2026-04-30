from typing import TypedDict, Optional , List

class AgentState(TypedDict):
    user_input: str
    agent_type: Optional[str]
    response: Optional[str]
    history: Optional[List[str]]