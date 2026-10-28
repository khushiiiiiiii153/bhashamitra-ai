
import os
import requests

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

load_dotenv()

API_KEY = os.getenv("SARVAM_API_KEY")
SARVAM_URL = "https://api.sarvam.ai/v1/chat/completions"
MODEL = "sarvam-105b-conversations"

app = FastAPI(
    title="BhashaMitra AI",
    description="Multilingual AI assistant with voice conversation",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

LANGUAGES = {
    "hi-IN": "Hindi",
    "mr-IN": "Marathi",
    "en-IN": "English",
}

MODES = {
    "chat": "Answer naturally and helpfully.",
    "summarize": "Summarize the user's text into clear, short points.",
    "translate": "Translate the user's text into the selected language. Preserve its meaning.",
    "improve": "Improve the user's English grammar and wording. Explain the main correction briefly.",
    "study": "Act as a friendly tutor. Explain simply, with a definition, steps and an example when useful.",
}


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=10000)
    language: str = "hi-IN"
    mode: str = "chat"
    history: list[dict] = Field(default_factory=list)


@app.get("/")
def home():
    return {"message": "BhashaMitra AI backend is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/chat")
def chat(request: ChatRequest):
    if not API_KEY:
        raise HTTPException(
            status_code=500,
            detail="SARVAM_API_KEY missing. Set it in backend/.env or deployment environment variables."
        )

    language = request.language if request.language in LANGUAGES else "hi-IN"
    mode = request.mode if request.mode in MODES else "chat"

    system_prompt = (
        "You are BhashaMitra AI, a friendly multilingual assistant. "
        f"Respond primarily in {LANGUAGES[language]}. "
        "The user may write in Hindi, Marathi, English, or Hinglish. "
        "Understand the user's intent and explain clearly for beginners. "
        "Be respectful, accurate, and concise. "
        "If unsure, say so rather than inventing facts. "
        f"Task mode: {MODES[mode]}"
    )

    messages = [{"role": "system", "content": system_prompt}]

    # Keep recent valid conversation turns to preserve context.
    for item in request.history[-12:]:
        role = item.get("role")
        content = item.get("content")

        if role in ("user", "assistant") and isinstance(content, str):
            content = content.strip()[:4000]
            if content:
                messages.append({"role": role, "content": content})

    messages.append({"role": "user", "content": request.message})

    try:
        response = requests.post(
            SARVAM_URL,
            headers={
                "api-subscription-key": API_KEY,
                "Content-Type": "application/json",
            },
            json={
                "model": MODEL,
                "messages": messages,
                "max_tokens": 700,
            },
            timeout=90,
        )

        if response.status_code != 200:
            print("Sarvam API error:", response.status_code, response.text[:500])
            raise HTTPException(
                status_code=502,
                detail="AI service returned an error. Check your Sarvam API key, access and credits."
            )

        data = response.json()
        reply = data["choices"][0]["message"]["content"]

        if not isinstance(reply, str) or not reply.strip():
            raise HTTPException(
                status_code=502,
                detail="AI returned an empty reply. Please try again."
            )

        return {"reply": reply.strip()}

    except HTTPException:
        raise
    except requests.Timeout:
        raise HTTPException(
            status_code=504,
            detail="AI took too long to respond. Please try again."
        )
    except requests.RequestException:
        raise HTTPException(
            status_code=502,
            detail="Could not connect to the AI service."
        )
    except (KeyError, IndexError, TypeError, ValueError):
        raise HTTPException(
            status_code=502,
            detail="Unexpected response from the AI service."
        )
