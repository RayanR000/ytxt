# ytxt

`ytxt` is a local, private CLI tool for transcribing YouTube videos using `faster-whisper`. All processing happens securely on your machine—no external APIs or cloud services required.

## Installation

Ensure you have `ffmpeg` installed on your system. Then, install the project:

```bash
pip install .
```

Alternatively, if you are running from the source:

```bash
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
ytxt <youtube_url_or_local_file_path>
```

### Options

- `--format [text|markdown|srt|json]`: Specify output format.
- `--model [base|small|medium|large]`: Choose the Whisper model size.
- `--timestamps`: Include start and end times in text/markdown output.
- `--output <path>`: Save the transcript to a file.
- `--no-cache`: Force a re-transcription by ignoring existing cache.

### Examples

**Save as Markdown with timestamps (YouTube):**
```bash
ytxt https://www.youtube.com/watch?v=VIDEO_ID --format markdown --timestamps --output transcript.md
```

**Transcribe a local audio file:**
```bash
ytxt path/to/audio.mp3 --model medium --output transcript.txt
```

## Features

- **Local-Only:** Privacy-first; no data leaves your machine.
- **Caching:** Efficiently caches results by video ID to avoid redundant work.
- **Formats:** Supports text, Markdown, SRT, and JSON.
- **Model Selection:** Flexibility to balance accuracy and performance by choosing your desired Whisper model size.
