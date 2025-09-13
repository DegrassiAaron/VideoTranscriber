import json
import urllib.request
import wave
from pathlib import Path


def download_audio(url: str, output_path: str | Path) -> Path:
    """Download an audio file from ``url`` to ``output_path``.

    Parameters
    ----------
    url: str
        Source URL of the audio file.
    output_path: str or Path
        Location where the downloaded file will be stored.

    Returns
    -------
    Path
        The path to the downloaded file.
    """
    output_path = Path(output_path)
    urllib.request.urlretrieve(url, output_path)
    return output_path


def transcribe_audio(audio_path: str | Path) -> str:
    """ "Transcribe" an audio file encoded with ASCII values.

    This function is intentionally simple and expects that the audio frames
    correspond directly to ASCII codes for demonstration and testing
    purposes. It is **not** a real speech recognition implementation.
    """
    audio_path = Path(audio_path)
    with wave.open(str(audio_path), "rb") as wf:
        frames = wf.readframes(wf.getnframes())
    text_bytes = frames.rstrip(b"\x00")
    return text_bytes.decode("ascii")


def transcription_to_json(text: str) -> str:
    """Format transcription text as a JSON string."""
    return json.dumps({"transcription": text}, ensure_ascii=False)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Transcribe an audio file")
    parser.add_argument("audio", help="Path to ASCII-encoded audio file")
    args = parser.parse_args()
    print(transcription_to_json(transcribe_audio(args.audio)))
