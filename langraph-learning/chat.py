from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages : Annotated[list, add_messages]

def chatbot(state: State):
    return {"messages": ["hi this message is from chatbot node"]}

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)