from faster_whisper import WhisperModel
from pathlib import Path
from typing import List, Dict, Optional

def transcribe_audio(audio_path: Path, model_size: str = "base", device: str = "auto") -> List[Dict]:
    """
    Transcribes audio using faster-whisper.
    
    Args:
        audio_path: Path to the audio file.
        model_size: Whisper model size (e.g., 'base', 'medium', 'large-v3').
        device: Device to use for computation ('cpu', 'cuda', 'auto').
    """
    # Use int8 quantization for CPU, float16 for GPU by default
    compute_type = "int8" if device == "cpu" else "default"
    
    model = WhisperModel(model_size, device=device, compute_type=compute_type)
    segments, info = model.transcribe(str(audio_path), beam_size=5)
    
    transcript = []
    for segment in segments:
        transcript.append({
            "start": segment.start,
            "end": segment.end,
            "text": segment.text.strip()
        })
    return transcript
