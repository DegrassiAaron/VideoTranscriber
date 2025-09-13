import json
import sys
import wave
from pathlib import Path
from unittest import mock

import pytest

# Ensure the project root is on the import path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from video_transcriber import (
    download_audio,
    transcribe_audio,
    transcription_to_json,
)


def test_download_audio(monkeypatch, tmp_path):
    calls = {}

    def fake_urlretrieve(url, filename):
        calls["url"] = url
        calls["filename"] = str(filename)
        Path(filename).write_bytes(b"data")

    monkeypatch.setattr("urllib.request.urlretrieve", fake_urlretrieve)
    out_file = tmp_path / "out.mp3"
    result = download_audio("http://example.com/audio.mp3", out_file)
    assert calls["url"] == "http://example.com/audio.mp3"
    assert calls["filename"] == str(out_file)
    assert result == out_file
    assert out_file.exists()


def _create_ascii_wave(text: str, path: Path) -> None:
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(1)
        wf.setframerate(8000)
        wf.writeframes(text.encode("ascii"))


def test_transcribe_audio(tmp_path):
    audio = tmp_path / "sample.wav"
    _create_ascii_wave("hello", audio)
    assert transcribe_audio(audio) == "hello"


def test_transcription_to_json():
    json_str = transcription_to_json("hello")
    data = json.loads(json_str)
    assert data == {"transcription": "hello"}
