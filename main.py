from fastapi import FastAPI
from pydantic import BaseModel
from agent import DoctorAppointmentAgent
from langchain_core.messages import HumanMessage
import os

os.environ.pop("SSL_CERT_FILE", None)

app = FastAPI()

# Define the Pydantic model to accept request body
class UserQuery(BaseModel):
    id_number: int
    messages: str
    
agent = DoctorAppointmentAgent()

@app.post("/execute")
def execute_agent(user_input: UserQuery):
    app_graph = agent.workflow()
    
    # Prepare the agent state as expected by the workflow
    input = [
        HumanMessage(content=user_input.messages)
    ]
    
    query_data = {
        "messages": input,
        "id_number": user_input.id_number,
        "next": "",
        "query": "",
        "current_reasoning": "",
    }
    
    response = app_graph.invoke(query_data, config={"recursion_limit": 20})
    
    return {"messages": response["messages"]}