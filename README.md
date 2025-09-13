# VideoTranscriber

Utilities to download videos and produce transcripts.

## Usage

### CLI

```bash
python src/cli.py <URL>
```

### HTTP API

```bash
uvicorn src.api:app --reload
```

Then send a POST request:

```bash
curl -X POST http://localhost:8000/transcribe -H 'Content-Type: application/json' -d '{"url": "https://example.com/video"}'
```
