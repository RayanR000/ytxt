import yt_dlp
import os
from pathlib import Path

def download_audio(url: str, output_dir: Path = Path("temp")) -> Path:
    """Downloads audio from YouTube using yt-dlp."""
    output_dir.mkdir(exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': str(output_dir / '%(id)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        audio_file = output_dir / f"{info['id']}.mp3"
        return audio_file
