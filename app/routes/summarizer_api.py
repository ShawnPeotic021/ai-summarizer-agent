import json

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from rich import print_json
from colorama import Fore,Style

from striprtf.striprtf import rtf_to_text

from app.services.summarize_service import summarize_from_transcript

router = APIRouter()

@router.get("/")
def root():
    return {"message": "AI Summarizer API is running"}

@router.post("/summarize")
async def summarize_endpoint(file: UploadFile = File(...)):
    '''Triger run_agent() with upload transcript and return summary JSON + formatted text'''
    raw = (await file.read()).decode("utf-8")
    transcript = rtf_to_text(raw)
    result = summarize_from_transcript(transcript)
    return JSONResponse(content={"success": True, **result})

