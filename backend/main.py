from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from anthropic import Anthropic
import json
import os
from benefits_db import BENEFITS_DATABASE, CATEGORIES

app = FastAPI(title="NaijaBenefits AI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Anthropic()

class ChatRequest(BaseModel):
    message: str
    language: str = "english"  # "english" or "pidgin"
    history: list = []

class SearchRequest(BaseModel):
    query: str
    category: str = "all"

# ── System Prompt ─────────────────────────────────────────────────────────────

def get_system_prompt(language: str, benefits: list) -> str:
    benefits_text = json.dumps(benefits, indent=2)
    
    if language == "pidgin":
        return f"""You are NaijaBenefits AI, a helpful assistant wey dey help Nigerians find government benefits, scholarships, and social programs wey dem qualify for.

You MUST respond in Nigerian Pidgin English - the way Nigerians actually talk.

Here are all the available Nigerian government benefits programs:
{benefits_text}

Your job:
1. Ask the person about their situation (age, job status, education, family situation)
2. Match them to benefits wey dem qualify for based on wetin dem tell you
3. Explain how to apply in simple Pidgin English
4. Always give the website and contact info
5. Be warm, encouraging and helpful - like a knowledgeable friend

Important rules:
- Only recommend benefits from the database above
- Always explain eligibility clearly
- Give practical step-by-step application advice
- Mention benefit amounts when available
- If person no qualify for something, tell them kindly and suggest alternatives
- Celebrate with them when you find programs they qualify for!

Start by greeting warmly in Pidgin and asking about their situation."""

    else:
        return f"""You are NaijaBenefits AI, a knowledgeable and caring assistant that helps Nigerians find government benefits, scholarships, social programs, and support services they qualify for.

Here are all available Nigerian government benefits programs:
{benefits_text}

Your job:
1. Ask the person about their situation (age, employment status, education level, family situation, location)
2. Based on their answers, identify ALL benefits they likely qualify for
3. Explain each benefit clearly: what it is, how much, and exactly how to apply
4. Always provide the official website and contact information
5. Be warm, encouraging and empowering

Important rules:
- Only recommend benefits from the database above
- Always explain eligibility requirements clearly
- Give practical step-by-step application guidance
- Mention specific benefit amounts (money, loans, etc.)
- If they don't qualify for something, explain why and suggest alternatives
- Ask follow-up questions to find MORE programs they might qualify for
- End responses with an encouraging message

Start by warmly greeting the user and asking about their current situation."""

# ── Endpoints ─────────────────────────────────────────────────────────────────

@app.post("/chat")
async def chat(req: ChatRequest):
    system = get_system_prompt(req.language, BENEFITS_DATABASE)
    
    messages = req.history + [{"role": "user", "content": req.message}]
    
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        system=system,
        messages=messages
    )
    
    reply = response.content[0].text
    
    return {
        "reply": reply,
        "language": req.language
    }

@app.post("/search")
async def search(req: SearchRequest):
    query = req.query.lower()
    results = []
    
    for benefit in BENEFITS_DATABASE:
        score = 0
        # Check tags
        for tag in benefit["tags"]:
            if tag in query:
                score += 3
        # Check name
        if any(word in benefit["name"].lower() for word in query.split()):
            score += 2
        # Check description
        if any(word in benefit["description"].lower() for word in query.split()):
            score += 1
        # Check category filter
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
    return {
        "name": "NaijaBenefits AI",
        "description": "Helping Nigerians find government benefits and social programs",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
