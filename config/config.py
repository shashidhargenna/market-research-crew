import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing")

agent_llm = LLM(
    model="openai/gpt-4o-mini",
    temperature=0.2
)

manager_llm = LLM(
    model="openai/gpt-4o-mini",
    temperature=0.2
)