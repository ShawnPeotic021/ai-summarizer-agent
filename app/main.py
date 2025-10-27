#main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.summarizer_api import router as summarizer_router

app = FastAPI(title ="AI Summarizer API")

# ✅ Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to http://localhost:5173
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(summarizer_router)

