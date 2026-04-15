import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", message=".*urllib3.*")

import asyncio
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator
from dotenv import load_dotenv

load_dotenv()

from retrieval import load_index
from generator import jag_query_engine, condense_question
from citation_formatter import format_citations, REFUSAL_MSG

import re
import unicodedata

def normalize_text(text: str) -> str:
    return unicodedata.normalize("NFKC", text).strip()

def remove_control_chars(text: str) -> str:
    return re.sub(r"[\x00-\x1F\x7F]", "", text)

def strip_html(text: str) -> str:
    return re.sub(r"<.*?>", "", text)

def remove_injection(text: str) -> str:
    patterns = [
        r"ignore previous instructions",
        r"system prompt",
        r"act as",
        r"you are now",
    ]
    for p in patterns:
        text = re.sub(p, "", text, flags=re.IGNORECASE)
    return text

def clean_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text)

def sanitize_input(text: str) -> str:
    text = normalize_text(text)
    text = remove_control_chars(text)
    text = strip_html(text)
    text = remove_injection(text)
    text = clean_whitespace(text)
    return text

# Load index and engine once at startup — not on every request
@asynccontextmanager
async def lifespan(app: FastAPI):
    global engine
    index = load_index()
    engine = jag_query_engine(index)
    print("JagUnify advisor ready.")
    yield

app = FastAPI(lifespan=lifespan)

# Allow requests from the configured frontend origin
_ALLOWED_ORIGIN = os.getenv("CORS_ORIGIN", "http://localhost:5173")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[_ALLOWED_ORIGIN],
    allow_methods=["POST"],
    allow_headers=["*"],
)

engine = None


MAX_QUESTION_LEN = 500   # characters
MAX_HISTORY_TURNS = 10   # prior turns kept
MAX_TURN_TEXT_LEN = 1000 # characters per turn


class HistoryTurn(BaseModel):
    role: str
    text: str = Field(max_length=MAX_TURN_TEXT_LEN)


class AskRequest(BaseModel):
    question: str = Field(max_length=MAX_QUESTION_LEN)
    history: list[HistoryTurn] = []

    @field_validator("history")
    @classmethod
    def cap_history(cls, v):
        # Keep only the most recent turns to limit prompt size
        return v[-MAX_HISTORY_TURNS:]


@app.post("/ask")
async def ask(request: AskRequest):
    if not request.question.strip():
        return {"answer": REFUSAL_MSG, "sources": []}

    try:
        loop = asyncio.get_event_loop()

        # Condense follow-up questions into standalone queries when history is present
        question = sanitize_input(request.question)
        history_dicts = [
            {"role": t.role, "text": sanitize_input(t.text)}
            for t in request.history
            ]
        question = await loop.run_in_executor(
            None, condense_question, history_dicts, question
        )

        response = await loop.run_in_executor(None, engine.query, question)
        return format_citations(response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
