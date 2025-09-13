# VideoTranscriber

codex/serialize-transcription-dictionary-to-json
Utility functions for working with video transcriptions.

## JSON Output Format

Transcriptions are stored as JSON objects with the following structure:

```
{
  "text": "Full transcription text",
  "segments": [
    {"start": 0.0, "end": 3.2, "text": "First segment"}
  ]
}
```

Use `serialize_transcription` from `src/transcriber.py` to either write the
JSON to a file or obtain the JSON string directly.
=======

