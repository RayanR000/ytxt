import json
import hashlib
from pathlib import Path
from typing import Optional, List, Dict

CACHE_DIR = Path("cache")

def get_cache_path(video_id: str) -> Path:
    CACHE_DIR.mkdir(exist_ok=True)
    return CACHE_DIR / f"{video_id}.json"

def read_cache(video_id: str) -> Optional[List[Dict]]:
    path = get_cache_path(video_id)
    if path.exists():
        with open(path, "r") as f:
            return json.load(f)
    return None

def write_cache(video_id: str, transcript: List[Dict]):
    with open(get_cache_path(video_id), "w") as f:
        json.dump(transcript, f)
