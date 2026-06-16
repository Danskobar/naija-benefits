# NaijaBenefits AI - Groq Version
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from openai import OpenAI
import json
import os
from benefits_db import BENEFITS_DATABASE, CATEGORIES

app = FastAPI(title="NaijaBenefits AI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.options("/{path:path}")
async def options_handler(request: Request, path: str):
    return JSONResponse(
        content={},
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        }
    )

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

class ChatRequest(BaseModel):
    message: str
    language: str = "english"
    history: list = []

class SearchRequest(BaseModel):
    query: str
    category: str = "all"

def get_system_prompt(language: str, benefits: list) -> str:
    benefits_text = json.dumps(benefits, indent=2)
    if language == "pidgin":
        return f"""You are NaijaBenefits AI, a helpful assistant wey dey help Nigerians find government benefits wey dem qualify for. Respond in Nigerian Pidgin English.

Available programs:
{benefits_text}

Ask about their situation, match them to benefits, explain how to apply, give website links. Be warm and encouraging like a knowledgeable friend."""
    else:
        return f"""You are NaijaBenefits AI, a helpful assistant that helps Nigerians find government benefits, scholarships and social programs they qualify for.

Available programs:
{benefits_text}

Ask about their situation, identify ALL benefits they qualify for, explain how to apply with official websites. Be warm and encouraging."""

@app.post("/chat")
async def chat(req: ChatRequest):
    system = get_system_prompt(req.language, BENEFITS_DATABASE)
    messages = req.history + [{"role": "user", "content": req.message}]
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1000,
        messages=[{"role": "system", "content": system}] + messages
    )
    reply = response.choices[0].message.content
    return {"reply": reply, "language": req.language}

@app.post("/search")
async def search(req: SearchRequest):
    query = req.query.lower()
    results = []
    for benefit in BENEFITS_DATABASE:
        score = 0
        for tag in benefit["tags"]:
            if tag in query:
                score += 3
        if any(word in benefit["name"].lower() for word in query.split()):
            score += 2
        if any(word in benefit["description"].lower() for word in query.split()):
            score += 1
        if req.category != "all" and benefit["category"] != req.category:
            continue
        if score > 0:
            results.append({**benefit, "score": score})
    results.sort(key=lambda x: x["score"], reverse=True)
    return {"results": results[:6]}

@app.get("/categories")
async def get_categories():
    return {"categories": CATEGORIES}

@app.get("/benefits")
async def get_all_benefits():
    return {"benefits": BENEFITS_DATABASE}

@app.get("/health")
async def health():
    return {"status": "ok", "service": "NaijaBenefits AI"}

@app.get("/")
async def root():
    return {"name": "NaijaBenefits AI", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)