from faster_whisper import WhisperModel
from pathlib import Path
from typing import List, Dict

def transcribe_audio(audio_path: Path, model_size: str = "base") -> List[Dict]:
    """Transcribes audio using faster-whisper on CPU."""
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = model.transcribe(str(audio_path), beam_size=5)
    
    transcript = []
    for segment in segments:
        transcript.append({
            "start": segment.start,
            "end": segment.end,
            "text": segment.text.strip()
        })
    return transcript
