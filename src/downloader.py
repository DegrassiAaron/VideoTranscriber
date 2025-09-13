"""Simple video downloader placeholder."""
from pathlib import Path


def download_video(url: str) -> str:
    """Pretend to download a video and return the path to a file.

    Parameters
    ----------
    url: str
        URL of the video to download.

    Returns
    -------
    str
        Path to the downloaded file.
    """
    downloads_dir = Path("downloads")
    downloads_dir.mkdir(exist_ok=True)
    file_path = downloads_dir / "video.txt"
    file_path.write_text(f"Downloaded from {url}\n")
    return str(file_path)
