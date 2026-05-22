import yt_dlp
import uuid
from pathlib import Path

def download_audio(url: str, output_dir: Path = Path("temp")) -> Path:
    """Downloads audio from any yt-dlp supported site."""
    output_dir.mkdir(exist_ok=True)
    
    # Use a unique ID for the filename to prevent collisions
    unique_id = str(uuid.uuid4())
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': str(output_dir / f"{unique_id}.%(ext)s"),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        
        # yt-dlp returns info about the download. 
        # If it was a playlist, we might need to handle multiple files, 
        # but for now we assume a single download.
        if 'entries' in info:
            # Handle playlist: get the first item
            info = info['entries'][0]
            
        audio_file = output_dir / f"{unique_id}.mp3"
        return audio_file
