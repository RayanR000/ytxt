# ytxt

`ytxt` is a local, private CLI tool for transcribing audio from YouTube, web URLs, or local files using `faster-whisper`. All processing happens securely on your machine—no external APIs or cloud services required.

## Installation

Ensure you have `ffmpeg` installed on your system. Then install `ytxt`:

```bash
pip install ytxt
```

Alternatively, to install from source:

```bash
git clone https://github.com/RayanR000/ytxt.git
cd ytxt
pip install -e .
```

## Usage

Basic usage:
```bash
ytxt <url_or_local_file_path>
```

### Options

- `--format [text|markdown|srt|json]`: Specify output format.
- `--model [base|small|medium|large]`: Choose the Whisper model size.
- `--timestamps`: Include start and end times in text/markdown output.
- `--output <path>`: Save the transcript to a file.
- `--no-cache`: Force a re-transcription by ignoring existing cache.

### Examples

**Transcribe a web URL (YouTube or other):**
```bash
ytxt https://www.example.com/audio.mp3 --format markdown --timestamps --output transcript.md
```

**Transcribe a local audio file:**
```bash
ytxt path/to/audio.mp3 --model medium --output transcript.txt
```

## Features

- **Local-Only:** Privacy-first; no data leaves your machine.
- **Universal Support:** Transcribe YouTube videos, web audio URLs, and local files.
- **Caching:** Efficiently caches results to avoid redundant work.
- **Formats:** Supports text, Markdown, SRT, and JSON.
- **Model Selection:** Flexibility to balance accuracy and performance by choosing your desired Whisper model size.
