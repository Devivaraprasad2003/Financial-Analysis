from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph
from langchain.chat_models import ChatOpenAI  # only if you're using OpenAI instead
import streamlit as st  # only if you're using Streamlit
import yfinance as yf
import re


# Initialize your LLM (replace with your actual Google API key)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key="AIzaSyAUH70gKFSmR52QAbZq4fJFM3WSbTYCHp8",
    temperature=0.3)

# ==== 1. User Input ====
def get_user_input(state):
    # Read user inputs from Streamlit UI
    state["user_input"] = {
        "age": st.number_input("Age", min_value=18, max_value=100, value=30),
        "goal": st.text_input("Financial Goal", value="retirement"),
        "horizon": st.number_input("Investment Horizon (years)", min_value=1, max_value=100, value=25),
        "income": st.number_input("Annual Income (₹)", min_value=0, value=70000)
    }
    return state

# ==== 2. Profile Analyzer ====
def profile_analyzer(state):
    profile = state["user_input"]
    prompt = f"""
    Analyze this user profile:
    - Age: {profile['age']}
    - Goal: {profile['goal']}
    - Investment Horizon: {profile['horizon']} years
    - Income: ₹{profile['income']}

    Give a short summary and note any key financial constraints.
    """
    state["profile_summary"] = llm.predict(prompt)
    return state

# ==== 3. Risk Model ====
def risk_model(state):
    profile = state["user_input"]
    prompt = f"""
    Based on the user's age ({profile['age']}) and investment horizon ({profile['horizon']}), 
    estimate their risk tolerance (low, medium, high) with a 1-line justification.
    """
    state["risk_profile"] = llm.predict(prompt)
    return state

# ==== 4. Asset Allocator ====
def asset_allocator(state):
    prompt = f"""
    Based on this risk profile: {state['risk_profile']}, suggest an asset allocation.
    Format: Stocks %, Bonds %, Cash %.
    """
    state["allocation"] = llm.predict(prompt)
    return state

# ==== 5. Investment Suggestion ====
def investment_suggestion(state):
    prompt = f"""
    Based on this allocation: {state['allocation']}, recommend 1 ETF for each category (stocks, bonds, cash).
    Include ticker symbols and a short reason.
    """
    state["etf_suggestions"] = llm.predict(prompt)
    return state

# ==== 6 (Final Summary without live prices) ====
def final_summary(state):
    summary = f"""
    ## Profile Summary:
    {state['profile_summary']}

    ## Risk Profile:
    {state['risk_profile']}

    ## Allocation Plan:
    {state['allocation']}
    
    ## Recommended ETFs:
    {state['etf_suggestions']}

    *(Live price lookup skipped)*
    """
    state["summary"] = summary
    return state

# ==== BUILD GRAPH ====
graph = StateGraph(dict)
graph.add_node("input", get_user_input)
graph.add_node("analyzer", profile_analyzer)
graph.add_node("risk", risk_model)
graph.add_node("allocate", asset_allocator)
graph.add_node("suggest", investment_suggestion)
graph.add_node("summary", final_summary)

graph.set_entry_point("input")
graph.add_edge("input", "analyzer")
graph.add_edge("analyzer", "risk")
graph.add_edge("risk", "allocate")
graph.add_edge("allocate", "suggest")
graph.add_edge("suggest", "summary")
graph.set_finish_point("summary")

# ==== Streamlit app ====
st.title("Financial Planner")


if st.button("Analyze Profile and Suggest Investments"):
    result = graph.compile().invoke({})
    st.markdown(result["summary"])
