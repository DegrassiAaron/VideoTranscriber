"""FastAPI application exposing a transcription endpoint."""
from fastapi import FastAPI
from pydantic import BaseModel
from downloader import download_video
from transcriber import transcribe

app = FastAPI()


class TranscribeRequest(BaseModel):
    url: str


@app.post("/transcribe")
async def transcribe_endpoint(req: TranscribeRequest) -> dict:
    video_path = download_video(req.url)
    transcript = transcribe(video_path)
    return {"text": transcript}
