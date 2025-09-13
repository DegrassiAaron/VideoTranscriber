"""Simple transcriber placeholder."""
from pathlib import Path


def transcribe(audio_path: str) -> str:
    """Return dummy transcription for the provided audio path."""
    path = Path(audio_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {audio_path}")
    return f"Transcribed {path.name}"
