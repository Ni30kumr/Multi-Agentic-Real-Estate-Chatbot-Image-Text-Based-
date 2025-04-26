from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
# Define prompt template
from langchain_core.prompts import ChatPromptTemplate
from typing import Optional, TypedDict
from langgraph.graph import StateGraph, END,START
from langchain_core.messages import HumanMessage
import base64

class AgentState(TypedDict):
    query: str                   # User input (required)
    image_path: Optional[str]    # Path to uploaded image (optional)
    output: str 
 
load_dotenv()

# Now your keys are available in environment variables
google_api_key = os.getenv("GOOGLE_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

gemini_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Initialize Tavily tool (reads TAVILY_API_KEY automatically if env is loaded)
tavily_tool = TavilySearch(max_results=3)

prompt = ChatPromptTemplate.from_template("""
You are a tenancy law expert Handles frequently asked questions related to tenancy laws, agreements,
landlord/tenant responsibilities, and rental processes. Summarize this information clearly for a renter:
{search_results}

User Question: {query}
""")
def faq_agent(state: AgentState):
    # Step 1: Search Tavily
    tavily_results = tavily_tool.invoke({"query": state["query"]})
    
    # Step 2: Format with Gemini
    response = gemini_llm.invoke(prompt.format(
        query=state["query"],
        search_results=tavily_results["answer"] or tavily_results["results"][0]["content"]
    ))
    
    state["output"] = response.content
    return state

def image_agent(state: AgentState):
    # Encode image (assuming local path/URL)
    with open(state["image_path"], "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")
    
    # Call Gemini Vision
    response = gemini_llm.invoke([
        HumanMessage(content=[
            {"type": "text", "text": "Analyze this property image for issues and suggest fixes:"},
            {"type": "image_url", "image_url": f"data:image/jpeg;base64,{image_data}"}
        ])
    ])
    
    state["output"] = response.content
    return state

# Define router (unchanged)
def router(state): 
    if state.get("image_path"): 
        return "image_agent"
    return "faq_agent"

# Build graph
workflow = StateGraph(AgentState)
workflow.add_node("image_agent", image_agent)
workflow.add_node("faq_agent", faq_agent)
workflow.add_conditional_edges(START, router, {"image_agent": "image_agent", "faq_agent": "faq_agent"})
workflow.add_edge("image_agent", END)
workflow.add_edge("faq_agent", END)
app = workflow.compile()

result = app.invoke({
    "query": "What is ideal advance rent for any flat that i should pay. compare this for india and united state",
})
print(result["output"])