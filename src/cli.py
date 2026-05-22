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

import sys
from pathlib import Path
from downloader import download_audio
from transcriber import transcribe_audio
from formatter import format_transcript
from cache import read_cache, write_cache

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
    
    # Simple extraction of video ID from URL for cache key
    video_id = args.url.split("v=")[-1].split("&")[0]
    
    transcript = None
    if not args.no_cache:
        transcript = read_cache(video_id)
        if transcript:
            print("Using cached transcript...")
    
    if not transcript:
        print("Downloading audio...")
        audio_file = download_audio(args.url)
        print("Transcribing...")
        transcript = transcribe_audio(audio_file, args.model)
        write_cache(video_id, transcript)
        # Cleanup temp file
        audio_file.unlink()
        
    output = format_transcript(transcript, args.format, args.timestamps)
    
    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output)
        print(f"Transcript saved to {out_path}")
    else:
        print(output)

