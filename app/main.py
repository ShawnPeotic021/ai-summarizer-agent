#main.py
from fastapi import FastAPI
from app.routes.summarizer_api import router as summarizer_router

app = FastAPI(title ="AI Summmarizer API")
app.include_router(summarizer_router)

