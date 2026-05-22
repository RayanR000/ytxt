import json
from pathlib import Path
from typing import List, Dict

def format_transcript(transcript: List[Dict], format_type: str, include_timestamps: bool = False) -> str:
    """Formats transcript data into requested format."""
    if format_type == "json":
        return json.dumps(transcript, indent=2)
    
    output = []
    for segment in transcript:
        line = ""
        if include_timestamps:
            line += f"[{segment['start']:.2f} - {segment['end']:.2f}] "
        line += segment['text']
        output.append(line)
    
    if format_type == "markdown":
        return "\n\n".join(output)
    elif format_type == "srt":
        srt_output = []
        for i, segment in enumerate(transcript, 1):
            start = f"{int(segment['start']//3600):02}:{int((segment['start']%3600)//60):02}:{int(segment['start']%60):02},{int((segment['start']*1000)%1000):03}"
            end = f"{int(segment['end']//3600):02}:{int((segment['end']%3600)//60):02}:{int(segment['end']%60):02},{int((segment['end']*1000)%1000):03}"
            srt_output.append(f"{i}\n{start} --> {end}\n{segment['text']}\n")
        return "\n".join(srt_output)
        
    return "\n".join(output)
