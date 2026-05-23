# ytxt

**Local-first, privacy-focused transcription CLI.** 

`ytxt` is a developer-centric tool for transcribing audio from YouTube, web URLs, or local files. It bridges the gap between `yt-dlp` and `faster-whisper`, providing a seamless, automated pipeline that runs entirely on your machine.

[![PyPI version](https://badge.fury.io/py/ytxt.svg)](https://badge.fury.io/py/ytxt)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Why ytxt?

- **Zero-Cloud Privacy:** No data leaves your machine. Perfect for sensitive meetings or private research.
- **High Performance:** Powered by `faster-whisper` (CTranslate2), which is up to 4x faster than OpenAI's original implementation.
- **Battery Included:** Handles downloading, audio extraction (`ffmpeg`), and transcription in one command.
- **Smart Caching:** Avoid redundant computations. `ytxt` hashes inputs to skip re-transcribing files you've already processed.
- **Universal:** Supports [1,000+ sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) including **YouTube, Spotify (Podcasts), and SoundCloud** via `yt-dlp`.

## Installation

Requires `ffmpeg` installed on your system.

```bash
# Using pip
pip install ytxt

# Using uv (recommended for speed)
uv tool install ytxt
```

## Quick Start (CLI)

Transcribe any YouTube video to Markdown with timestamps:

```bash
ytxt "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --format markdown --timestamps --output transcript.md
```

### Power User Tricks

**Pipe to an LLM for summarization:**
```bash
ytxt <url> | llm "Summarize this transcript for a technical audience"
```

**Extract metadata with `jq`:**
```bash
ytxt <url> --format json | jq '.[].text'
```

## Data Pipelines & Automation

`ytxt` is designed to be a "high-signal" component in your data infrastructure. Because status logs are routed to `stderr`, the `stdout` remains clean for programmatic use.

- **RAG Pipelines:** Use `ytxt` as an ingestion layer to feed YouTube transcripts directly into vector databases like Pinecone or Chroma.
- **AI Agents:** Pipe transcripts directly into LLMs for summarization, sentiment analysis, or entity extraction.
- **Subtitles:** Generate industry-standard `.srt` files for video editing workflows.
- **Scheduled Jobs:** Run `ytxt` in a cron job or GitHub Action to monitor and transcribe new videos from a playlist.

## Library Usage

`ytxt` is designed to be imported into your own Python automation scripts.

```python
from ytxt import download_audio, transcribe_audio

# 1. Download & Extract
audio_path = download_audio("https://youtube.com/...")

# 2. Transcribe Locally
transcript = transcribe_audio(audio_path, model_size="medium")

# 3. Use the result (list of dicts with 'start', 'end', 'text')
for segment in transcript:
    print(f"[{segment['start']}] {segment['text']}")
```

## Configuration

| Option | Description | Default |
| :--- | :--- | :--- |
| `--model` | Whisper model size (`tiny`, `base`, `small`, `medium`, `large-v3`) | `base` |
| `--format` | Output format (`text`, `markdown`, `srt`, `json`) | `text` |
| `--timestamps` | Include timestamps in text/markdown output | `False` |
| `--no-cache` | Force re-transcription by ignoring cache | `False` |

## Development

```bash
git clone https://github.com/rayanrane/ytxt.git
cd ytxt
pip install -e .
```

## License

MIT
