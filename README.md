# VideoTranscriber

Simple utilities to download audio files, perform a toy transcription, and
format the result as JSON.

## Installation

Clone the repository and install the package:

```bash
pip install -e .
```

The project requires only the Python standard library.

## CLI usage

After cloning, you can run the simple command line interface:

```bash
python video_transcriber.py path/to/audio.wav
```

The CLI expects an audio file where each frame encodes an ASCII character.
It prints the transcription as JSON to standard output.

## API usage

```python
from video_transcriber import download_audio, transcribe_audio

# Download
download_audio("http://example.com/file.wav", "local.wav")

# Transcribe
text = transcribe_audio("local.wav")
```

## Known limits

This project is designed for demonstration purposes:

- `transcribe_audio` only decodes ASCII values embedded in the audio file.
  It is **not** a real speech recognition engine.
- No external dependencies are included; complex audio formats are not
  supported.
