# ytxt — Local YouTube Transcript CLI Tool

## Overview

**ytxt** is a fast, fully local command-line tool that converts YouTube videos into accurate transcripts. It is designed for speed, offline use, and developer-friendly integration.

---

## Core Idea

Given a YouTube URL, the tool:

1. Extracts audio locally using `yt-dlp`
2. Transcribes speech using `faster-whisper`
3. Outputs structured transcripts in multiple formats

Everything runs locally — no external APIs required.

---

## Key Features

### ⚡ Performance

* Fully local processing
* Optimized `faster-whisper` inference
* Optional GPU acceleration
* Automatic caching for instant repeat requests

### 📄 Output Formats

* Plain text (`.txt`)
* Markdown (`.md`)
* Subtitles (`.srt`)
* Structured JSON (`.json`)

### 🧠 Smart Behavior

* Auto-detects best processing path
* Caches transcripts by video ID
* Streams results to terminal when possible

### 🛠 Developer-Friendly

* Pipeable CLI output
* Easy integration into scripts
* Optional local API server for extensions/tools

---

## Default Behavior

When no options are provided:

* Transcript prints directly to terminal
* Result is automatically cached locally
* No files are created unless explicitly requested

---

## CLI Usage

### Basic usage

```bash
ytxt <youtube_url>
```

### Save to file

```bash
ytxt <url> --output transcript.md
```

### Choose format

```bash
ytxt <url> --format txt
yt xt <url> --format md
yt xt <url> --format srt
yt xt <url> --format json
```

### Advanced options

```bash
ytxt <url> --model small --timestamps
yt xt <url> --no-cache
```

---

## Architecture

### Components

* **CLI Layer**

  * Parses arguments
  * Handles output formatting

* **Downloader**

  * Uses `yt-dlp` to extract audio

* **Transcription Engine**

  * Powered by `faster-whisper`
  * Supports CPU/GPU execution

* **Cache System**

  * Stores transcripts by video ID
  * Speeds up repeated requests

* **(Optional) Local API Server**

  * Enables integrations (browser extensions, apps)

---

## Performance Strategy

* Prioritize cached results
* Use lightweight Whisper models by default (`small`)
* Parallelize download + model loading when possible
* Stream output incrementally for perceived speed

---

## File Storage

If file output is requested:

* Saves to user-specified path, or
* Falls back to `./transcripts/`

Optional system cache:

* Stored in OS app data directory
* Used for instant retrieval on repeat requests

---

## Example Output (Markdown)

```markdown
# Transcript

[00:00] Today we're going to talk about machine learning...
[00:12] Machine learning is a subset of artificial intelligence...
```

---

## Goal

To build a **blazing-fast, fully local transcript engine** that is:

* Instant for repeat usage
* Accurate enough for real-world content
* Easy to integrate into other developer workflows
* Lightweight enough to run on consumer hardware
