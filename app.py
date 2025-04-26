# app.py

import streamlit as st
from dotenv import load_dotenv
import os
import base64
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from typing import Optional, TypedDict
from langgraph.graph import StateGraph, END, START

# Load environment variables
load_dotenv()

# Set up API keys
google_api_key = os.getenv("GOOGLE_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

# Initialize models
gemini_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
tavily_tool = TavilySearch(max_results=3)

# Define Agent State
class AgentState(TypedDict):
    query: str                   # User input (required)
    image_path: Optional[str]    # Path to uploaded image (optional)
    output: str                  # Model output

# Define prompt
prompt = ChatPromptTemplate.from_template("""
You are a tenancy law expert handling FAQs about tenancy laws, agreements,
landlord/tenant responsibilities, and rental processes. Summarize clearly for a renter:
{search_results}

User Question: {query}
""")

# FAQ Agent (text-only)
def faq_agent(state: AgentState):
    tavily_results = tavily_tool.invoke({"query": state["query"]})
    response = gemini_llm.invoke(prompt.format(
        query=state["query"],
        search_results=tavily_results["answer"] or tavily_results["results"][0]["content"]
    ))
    state["output"] = response.content
    return state

# Image Agent (with optional image analysis)
def image_agent(state: AgentState):
    with open(state["image_path"], "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")
    
    response = gemini_llm.invoke([
        HumanMessage(content=[
            {"type": "text", "text": "Analyze this property image for issues and suggest fixes:"},
            {"type": "image_url", "image_url": f"data:image/jpeg;base64,{image_data}"}
        ])
    ])
    
    state["output"] = response.content
    return state

# Router
def router(state: AgentState):
    if state.get("image_path"):
        return "image_agent"
    return "faq_agent"

# Build the LangGraph workflow
workflow = StateGraph(AgentState)
workflow.add_node("faq_agent", faq_agent)
workflow.add_node("image_agent", image_agent)
workflow.add_conditional_edges(START, router, {"image_agent": "image_agent", "faq_agent": "faq_agent"})
workflow.add_edge("faq_agent", END)
workflow.add_edge("image_agent", END)
app = workflow.compile()

# -----------------------
# Streamlit Frontend App
# -----------------------

st.title("🏡 Tenancy Law Assistant + Property Image Analyzer")

query = st.text_input("Ask your tenancy question:")

uploaded_image = st.file_uploader("Optional: Upload a property image", type=["jpg", "jpeg", "png"])

if st.button("Submit Query"):
    if not query:
        st.error("Please enter a question!")
    else:
        # Save uploaded image locally if any
        image_path = None
        if uploaded_image:
            image_bytes = uploaded_image.read()
            save_path = os.path.join("uploaded_image.jpg")
            with open(save_path, "wb") as f:
                f.write(image_bytes)
            image_path = save_path

        # Run the workflow
        result = app.invoke({
            "query": query,
            "image_path": image_path,
        })

        # Display result
        st.subheader("🧠 Assistant Response:")
        st.write(result["output"])
