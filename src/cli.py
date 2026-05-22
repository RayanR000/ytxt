import argparse
import sys
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description="ytxt: Local YouTube transcript CLI")
    parser.add_argument("url", help="YouTube URL to transcribe")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--format", choices=["text", "markdown", "srt", "json"], default="text", help="Output format")
    parser.add_argument("--model", default="base", help="Whisper model to use")
    parser.add_argument("--timestamps", action="store_true", help="Include timestamps in output")
    parser.add_argument("--no-cache", action="store_true", help="Skip cache usage")
    
    return parser.parse_args()

def main():
    args = parse_args()
    print(f"Processing {args.url}...")
    # TODO: Initialize downloader and transcription pipeline

if __name__ == "__main__":
    main()
