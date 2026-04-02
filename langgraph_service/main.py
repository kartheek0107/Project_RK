# langgraph_service/main.py
from fastapi import FastAPI

app = FastAPI(title="LangGraph SRE Copilot")

@app.get("/health")
async def health():
    return {"status": "ok"}