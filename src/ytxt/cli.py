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
import argparse
import sys
from pathlib import Path
from .downloader import download_audio
from .transcriber import transcribe_audio
from .formatter import format_transcript
from .cache import read_cache, write_cache

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
    
    input_path = Path(args.url)
    
    # Handle local file or download from URL
    if input_path.exists() and input_path.is_file():
        audio_file = input_path
        video_id = hashlib.md5(str(input_path.absolute()).encode()).hexdigest()
        print(f"Using local file: {input_path}")
    else:
        # Improved extraction of video ID from URL for cache key
        import re
        match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", args.url)
        if match:
            video_id = match.group(1)
        else:
            # Fallback if regex fails (e.g. invalid URL)
            video_id = hashlib.md5(args.url.encode()).hexdigest()
            
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
        
    # If it was a URL, we already have the transcript via the block above
    # If it was a local file, we need to transcribe it here
    if 'transcript' not in locals():
        print("Transcribing...")
        transcript = transcribe_audio(audio_file, args.model)
        output = format_transcript(transcript, args.format, args.timestamps)
    
    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output)
        print(f"Transcript saved to {out_path}")
    else:
        print(output)

