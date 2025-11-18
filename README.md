# Financial Planner Agent using Google Gemini + LangChain + LangGraph + Streamlit

This project is a full-stack AI-powered Financial Planning Assistant built using Google Gemini, LangChain, LangGraph, and Streamlit.
It collects user financial details, analyzes the profile, determines risk tolerance, creates an asset allocation plan, and recommends ETFs — all through an autonomous LLM workflow.

The project demonstrates how to build agentic workflows, multi-step LLM pipelines, and interactive web apps using modern AI tools.

🌟 Features

🔹 Multi-step Financial Planning Agent using LangGraph

🔹 LLM reasoning powered by Google Gemini (Generative AI)

🔹 User-friendly interface built with Streamlit

🔹 Automated stages:

Profile Intake

Profile Analysis

Risk Model

Asset Allocation

ETF Suggestions

Final Summary

🔹 Clean modular architecture (each step is a graph node)

🔹 .env based secure API key handling

🔹 Easily extendable for Robo-Advisors or Personal Finance apps

📁 Project Structure
project/
│── agent.py             # Main LangGraph + Streamlit app
│── .env.example         # Environment variable sample
│── README.md            # Documentation

🔧 Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

2. Install dependencies
pip install streamlit langchain langgraph yfinance google-generativeai langchain-google-genai python-dotenv

3. Add your API keys

Create a .env file:

GEMINI_API_KEY=your_gemini_key_here
LANGCHAIN_API_KEY=your_langchain_key_here
LANGCHAIN_PROJECT=LANGCHAIN_PROMPT


(Do NOT upload your real .env file to GitHub.)

▶️ Running the Application

Run the Streamlit web app:

streamlit run agent.py


This launches the financial planner interface in your browser.

🧩 How the Agent Works (Pipeline)

Your agent follows a 6-step automated workflow:

User Input Collection
Collects age, income, goal, horizon, etc.

Profile Analyzer
Summarizes the user’s financial status.

Risk Model
Determines low/medium/high risk based on age + horizon.

Asset Allocator
Suggests percentage of Stocks / Bonds / Cash.

ETF Recommender
Gives 1 ETF per category with ticker + reason.

Final Summary
Generates a complete financial plan.

This entire workflow is managed using LangGraph for clean node-by-node execution.

🧠 Tech Stack

Google Gemini – LLM reasoning and text generation

LangChain – Prompt orchestration

LangGraph – Agent workflow graph

Streamlit – UI for user interaction

yfinance – Financial data (optional)

dotenv – Secure key management

📌 Use Cases

Personal Finance Assistant

Robo-Advisory Prototype

Investment Planning Tools

LLM Agent Demo for Portfolio

Academic or AI Internship Showcase Project

📄 Example Output

The agent generates:

Profile interpretation

Risk tolerance

Asset allocation %

ETF recommendations

Final structured plan in Markdown
