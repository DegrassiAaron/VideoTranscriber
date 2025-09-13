"""Command line interface for video transcription."""
from argparse import ArgumentParser
from downloader import download_video
from transcriber import transcribe


def main() -> None:
    parser = ArgumentParser(description="Download and transcribe a video from a URL")
    parser.add_argument("url", help="URL of the video to transcribe")
    args = parser.parse_args()

    video_path = download_video(args.url)
    transcript = transcribe(video_path)
    print(transcript)


if __name__ == "__main__":
    main()
