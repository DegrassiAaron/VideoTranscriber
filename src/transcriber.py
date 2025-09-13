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
