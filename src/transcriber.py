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
