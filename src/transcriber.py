from pathlib import Path
from typing import Dict, Any

import whisper

_model = whisper.load_model("base")

def transcribe_audio(audio_path: Path) -> Dict[str, Any]:
    """Transcribe an audio file using a Whisper model.

    Parameters
    ----------
    audio_path: Path
        Path to the audio file to transcribe.

    Returns
    -------
    Dict[str, Any]
        Dictionary containing transcription text, segments and language.
    """
    result = _model.transcribe(str(audio_path))
    return {
        "text": result.get("text", ""),
        "segments": result.get("segments", []),
        "language": result.get("language")
    }
=======
import json
from typing import Any, Dict, Optional


def serialize_transcription(transcription: Dict[str, Any], output_path: Optional[str] = None) -> Optional[str]:
    """Serialize a transcription dictionary to JSON.

    Args:
        transcription: Dictionary containing the transcription data.
        output_path: Optional path to a JSON file where the transcription will be written.
            When omitted, the JSON representation is returned instead.

    Returns:
        The JSON string when ``output_path`` is not provided. ``None`` otherwise.
    """
    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(transcription, f, ensure_ascii=False, indent=2)
        return None

    return json.dumps(transcription, ensure_ascii=False, indent=2)

"""Simple transcriber placeholder."""
from pathlib import Path


def transcribe(audio_path: str) -> str:
    """Return dummy transcription for the provided audio path."""
    path = Path(audio_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {audio_path}")
    return f"Transcribed {path.name}"

