from pathlib import Path
from urllib.parse import urlparse

import yt_dlp


def download_audio(url: str) -> Path:
    """Download audio from the given URL using ``yt_dlp``.

    Parameters
    ----------
    url: str
        URL of the video/audio content to download.

    Returns
    -------
    Path
        Path to the downloaded audio file.

    Raises
    ------
    ValueError
        If the provided URL is not valid.
    RuntimeError
        If the download fails for any reason.
    """
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("Invalid URL provided")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
        "noplaylist": True,
        "quiet": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file = Path(ydl.prepare_filename(info)).with_suffix(".mp3")
            if not file.exists():
                wav_file = file.with_suffix(".wav")
                if wav_file.exists():
                    file = wav_file
                else:
                    raise RuntimeError("Downloaded file not found")
            return file
    except yt_dlp.utils.DownloadError as exc:  # type: ignore[attr-defined]
        raise RuntimeError(f"Failed to download audio: {exc}") from exc
    except Exception as exc:  # pragma: no cover - unexpected errors
        raise RuntimeError(f"Unexpected error during download: {exc}") from exc
