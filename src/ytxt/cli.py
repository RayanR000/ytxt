import argparse
import sys
import hashlib
import re
from pathlib import Path
from .downloader import download_audio
from .transcriber import transcribe_audio
from .formatter import format_transcript
from .cache import read_cache, write_cache

def parse_args():
    parser = argparse.ArgumentParser(description="ytxt: Local YouTube transcript CLI")
    parser.add_argument("url", help="YouTube/Audio URL or local file path to transcribe")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--format", choices=["text", "markdown", "srt", "json"], default="text", help="Output format")
    parser.add_argument("--model", default="base", help="Whisper model to use")
    parser.add_argument("--device", choices=["auto", "cpu", "cuda"], default="auto", help="Device to use for computation")
    parser.add_argument("--timestamps", action="store_true", help="Include timestamps in output")
    parser.add_argument("--no-cache", action="store_true", help="Skip cache usage")
    
    return parser.parse_args()

def main():
    args = parse_args()
    
    input_path = Path(args.url)
    
    # Check if local file
    if input_path.exists() and input_path.is_file():
        audio_file = input_path
        # Use absolute path for consistent cache key
        cache_key = hashlib.md5(str(input_path.absolute()).encode()).hexdigest()
        print(f"Using local file: {input_path}", file=sys.stderr)
    else:
        # It's a URL
        # Use URL as cache key for web sources
        cache_key = hashlib.md5(args.url.encode()).hexdigest()
        
        # Check cache first
        transcript = None
        if not args.no_cache:
            transcript = read_cache(cache_key)
            if transcript:
                print("Using cached transcript...", file=sys.stderr)
        
        if not transcript:
            print(f"Downloading audio from {args.url}...", file=sys.stderr)
            audio_file = download_audio(args.url)
            print("Transcribing...", file=sys.stderr)
            transcript = transcribe_audio(audio_file, args.model, args.device)
            write_cache(cache_key, transcript)
            # Cleanup temp file
            if audio_file.exists():
                audio_file.unlink()
        else:
            # We already have the transcript from cache
            pass

    # Ensure transcript is loaded (from file transcription or cached/downloaded)
    if 'transcript' not in locals():
        print("Transcribing...", file=sys.stderr)
        transcript = transcribe_audio(audio_file, args.model, args.device)
    
    output = format_transcript(transcript, args.format, args.timestamps)
    
    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output)
        print(f"Transcript saved to {out_path}", file=sys.stderr)
    else:
        print(output)

